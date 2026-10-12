#!/usr/bin/env python3
"""Token-budget batching for the fan-out stages.

  digest  — group extracted documents into batches for kb-digest subagents
  writer  — group taxonomy nodes into batches for kb-writer subagents

This is what makes the pipeline scale: no subagent is ever handed more than a
bounded slice, so a 10-document corpus and a 1000-document corpus differ only
in how many batches run.

Usage:
  python3 plan_batches.py digest [--root DIR] [--all] [--max-chars N] [--max-docs N]
  python3 plan_batches.py writer [--root DIR] [--max-nodes N] [--max-chars N]
"""

import argparse
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kblib as K  # noqa: E402

DIGEST_MAX_CHARS = 60_000
DIGEST_MAX_DOCS = 8
# A document longer than this is cut into segments on line boundaries, one digest
# agent per segment, so every agent can read its whole slice — nothing is skimmed.
SEGMENT_CHARS = 250_000
WRITER_MAX_NODES = 10
WRITER_MAX_CHARS = 90_000
WAVE_SIZE = 6


def segments_of(root, d):
    """Cut an extracted document into <=SEGMENT_CHARS slices on line boundaries.

    Returns [{index, total, start_line, end_line, chars, part_file}] — 1-based,
    inclusive lines, for Read offset/limit. A part whose digest already exists in
    .kb/digests/parts/ is left out (resume); `total` still counts every segment.
    """
    P = K.paths(root)
    with open(os.path.join(root, d["extracted_path"]), "r", encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    segs, start, size = [], 1, 0
    for n, line in enumerate(lines, 1):
        if size and size + len(line) + 1 > SEGMENT_CHARS:
            segs.append((start, n - 1, size))
            start, size = n, 0
        size += len(line) + 1
    segs.append((start, len(lines), size))
    out = []
    for i, (a, b, c) in enumerate(segs, 1):
        rel = os.path.join(".kb", "digests", "parts", f"{d['doc_id']}.part-{i:03d}.json")
        out.append({"index": i, "total": len(segs), "start_line": a, "end_line": b,
                    "chars": c, "part_file": rel})
    return out


def plan_digest(root, args):
    P = K.paths(root)
    manifest = K.read_json(P["manifest"])
    if not manifest:
        raise SystemExit("error: no .kb/manifest.json — run extract.py first")

    wanted = ("new", "changed") if not args.all else ("new", "changed", "unchanged")
    docs, resumed = [], 0
    for d in manifest.get("documents", []):
        if d.get("status") == "failed" or d.get("status") not in wanted:
            continue
        digest_path = os.path.join(P["digests"], d["doc_id"] + ".json")
        # Resume semantics: a digest that is newer than its extracted source is
        # already done. A re-extracted (changed) document has a newer source, so
        # it comes back into the plan on its own.
        if os.path.exists(digest_path) and not args.redo:
            extracted = os.path.join(root, d.get("extracted_path") or "")
            try:
                if os.path.getmtime(digest_path) >= os.path.getmtime(extracted):
                    resumed += 1
                    continue
            except OSError:
                pass
        docs.append(d)

    docs.sort(key=lambda d: (-int(d.get("chars") or 0), d["doc_id"]))

    batches, current, current_chars = [], [], 0
    oversized = []
    for d in docs:
        chars = int(d.get("chars") or 0)
        entry = {
            "doc_id": d["doc_id"],
            "title": d.get("title") or d["doc_id"],
            "source": d["rel_path"],
            "extracted_path": d.get("extracted_path"),
            "chars": chars,
            "outline_depth": len({h["level"] for h in d.get("outline", [])}),
        }
        if chars > args.max_chars:
            entry["oversized"] = True
            entry["read_in_parts"] = max(2, math.ceil(chars / args.max_chars))
            oversized.append(d["doc_id"])
            if chars > SEGMENT_CHARS:
                for seg in segments_of(root, d):
                    e = dict(entry)
                    e["chars"] = seg["chars"]
                    e["segment"] = seg
                    batches.append({"docs": [e], "total_chars": seg["chars"]})
                continue
            batches.append({"docs": [entry], "total_chars": chars})
            continue
        if current and (current_chars + chars > args.max_chars or len(current) >= args.max_docs):
            batches.append({"docs": current, "total_chars": current_chars})
            current, current_chars = [], 0
        current.append(entry)
        current_chars += chars
    if current:
        batches.append({"docs": current, "total_chars": current_chars})

    batches = [b for b in batches
               if not (b["docs"][0].get("segment")
                       and os.path.exists(os.path.join(root, b["docs"][0]["segment"]["part_file"]))
                       and not args.redo)]
    for i, b in enumerate(batches, 1):
        b["batch_id"] = f"digest-{i:04d}"
        b["wave"] = (i - 1) // args.wave_size + 1
        b["doc_count"] = len(b["docs"])

    out = {
        "stage": "digest",
        "generated": K.now_iso(),
        "budget": {"max_chars": args.max_chars, "max_docs": args.max_docs,
                   "wave_size": args.wave_size},
        "totals": {
            "documents": len(docs),
            "batches": len(batches),
            "waves": max((b["wave"] for b in batches), default=0),
            "oversized_documents": len(oversized),
            "already_digested": resumed,
            "chars": sum(b["total_chars"] for b in batches),
        },
        "batches": batches,
    }
    K.write_json(os.path.join(P["batches"], "digest-batches.json"), out)
    return out


def plan_writer(root, args):
    P = K.paths(root)
    taxonomy = K.read_json(P["taxonomy"])
    if not taxonomy:
        raise SystemExit("error: no .kb/taxonomy.json — run the architect stage first")
    manifest = K.read_json(P["manifest"], {"documents": []})
    chars_by_doc = {d["doc_id"]: int(d.get("chars") or 0) for d in manifest["documents"]}
    path_by_doc = {d["doc_id"]: d.get("extracted_path") for d in manifest["documents"]}
    source_by_doc = {d["doc_id"]: d.get("rel_path") for d in manifest["documents"]}

    only = set(args.clusters.split(",")) if args.clusters else None
    all_nodes = taxonomy.get("nodes", [])
    # Incremental mode: when the architect tagged nodes with an action, only
    # create/update ones need writing. Absent the field, write everything.
    actioned = [n for n in all_nodes if n.get("action")]
    if actioned and not args.redo:
        all_nodes = [n for n in actioned if n["action"] in ("create", "update")]

    by_cluster, resumed = {}, 0
    for node in all_nodes:
        cluster = node.get("cluster")
        if only and cluster not in only:
            continue
        # Resume semantics: a node file newer than the taxonomy is already written.
        node_path = os.path.join(P["wiki"], (node.get("id") or "") + ".md")
        if os.path.exists(node_path) and not args.redo:
            try:
                if os.path.getmtime(node_path) >= os.path.getmtime(P["taxonomy"]):
                    resumed += 1
                    continue
            except OSError:
                pass
        by_cluster.setdefault(cluster, []).append(node)

    cluster_meta = {c["slug"]: c for c in taxonomy.get("clusters", [])}
    batches = []
    for cluster, nodes in sorted(by_cluster.items()):
        nodes.sort(key=lambda n: n.get("id", ""))
        current, current_chars = [], 0
        chunks = []
        for node in nodes:
            docs = list(dict.fromkeys(node.get("source_doc_ids", [])))
            cost = sum(chars_by_doc.get(d, 0) for d in docs)
            if current and (
                len(current) >= args.max_nodes
                or (current_chars + cost > args.max_chars and len(current) > 1)
            ):
                chunks.append((current, current_chars))
                current, current_chars = [], 0
            current.append(node)
            current_chars += cost
        if current:
            chunks.append((current, current_chars))

        for part, (chunk_nodes, cost) in enumerate(chunks, 1):
            doc_ids = list(dict.fromkeys(
                d for n in chunk_nodes for d in n.get("source_doc_ids", [])
            ))
            batches.append({
                "cluster": cluster,
                "cluster_title": cluster_meta.get(cluster, {}).get("title", cluster),
                "cluster_description": cluster_meta.get(cluster, {}).get("description", ""),
                "part": part,
                "parts": len(chunks),
                "node_count": len(chunk_nodes),
                "source_chars": cost,
                "nodes": chunk_nodes,
                "sources": [
                    {"doc_id": d, "extracted_path": path_by_doc.get(d),
                     "source": source_by_doc.get(d), "chars": chars_by_doc.get(d, 0)}
                    for d in doc_ids
                ],
            })

    for i, b in enumerate(batches, 1):
        b["batch_id"] = f"writer-{i:04d}"
        b["wave"] = (i - 1) // args.wave_size + 1

    out = {
        "stage": "writer",
        "generated": K.now_iso(),
        "budget": {"max_nodes": args.max_nodes, "max_chars": args.max_chars,
                   "wave_size": args.wave_size},
        "totals": {
            "clusters": len(by_cluster),
            "nodes": sum(b["node_count"] for b in batches),
            "batches": len(batches),
            "waves": max((b["wave"] for b in batches), default=0),
            "already_written": resumed,
        },
        "batches": batches,
    }
    K.write_json(os.path.join(P["batches"], "writer-batches.json"), out)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=["digest", "writer"])
    ap.add_argument("--root")
    ap.add_argument("--all", action="store_true", help="digest: include unchanged documents")
    ap.add_argument("--redo", action="store_true",
                    help="ignore existing digests/nodes and re-plan everything")
    ap.add_argument("--clusters", help="writer: comma-separated cluster slugs only")
    ap.add_argument("--max-chars", type=int)
    ap.add_argument("--max-docs", type=int, default=DIGEST_MAX_DOCS)
    ap.add_argument("--max-nodes", type=int, default=WRITER_MAX_NODES)
    ap.add_argument("--wave-size", type=int, default=WAVE_SIZE)
    args = ap.parse_args()

    root = K.project_root(args.root)
    if args.stage == "digest":
        args.max_chars = args.max_chars or DIGEST_MAX_CHARS
        out = plan_digest(root, args)
        t = out["totals"]
        print(f"digest plan: {t['documents']} documents -> {t['batches']} batches "
              f"in {t['waves']} wave(s) of <= {args.wave_size}")
        if t["oversized_documents"]:
            print(f"  {t['oversized_documents']} oversized document(s) get a batch each "
                  f"(read in parts with Read offset/limit)")
        if t["already_digested"]:
            print(f"  {t['already_digested']} already digested — skipped (resume)")
        print(f"  written to .kb/batches/digest-batches.json")
    else:
        args.max_chars = args.max_chars or WRITER_MAX_CHARS
        out = plan_writer(root, args)
        t = out["totals"]
        print(f"writer plan: {t['nodes']} nodes across {t['clusters']} cluster(s) "
              f"-> {t['batches']} batches in {t['waves']} wave(s)")
        if t["already_written"]:
            print(f"  {t['already_written']} already written — skipped (resume)")
        print(f"  written to .kb/batches/writer-batches.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
