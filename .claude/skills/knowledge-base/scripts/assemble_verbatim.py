#!/usr/bin/env python3
"""Stage 3 (verbatim mode) — build wiki/ node pages from the source text itself.

The alternative to the kb-writer fan-out when the knowledge base must carry the
documents exactly as they are. Nothing is summarised or rewritten: every node
body is the extracted text of one source document, and the intelligence goes
into *where* it sits and *how it is found*:

  cluster   (taxonomy, layer 1)  — wiki/<cluster>/_cluster.md
    topic   (taxonomy node)      — a section of the cluster hub, plus a
                                   `topic/` tag and keyword on every member
      node  (one per document)   — wiki/<cluster>/<slug>.md, verbatim text

Documents longer than plan_batches.SEGMENT_CHARS become one node per segment —
the same line-bounded slices the digest stage read — so no node is too large to
answer from, and each part routes on its own part digest.

What the script adds around the verbatim text, and nothing else:
- frontmatter from the digest (description = `one_line`, keywords = topics)
  and from the taxonomy (cluster, topic);
- headings shifted one level down, so the page's own H1 is its title;
- the spreadsheet interning marker `[[Vn]]` (written by xlsx2md, not by any
  source) rendered as `⟦Vn⟧`, since a wikilink-shaped token would fail link
  validation; a part whose `### Shared values` legend lies in another part gets
  the entries it references copied in, verbatim;
- `> [!warning] Conflict` callouts for every suspected conflict the digest
  recorded (labelled unverified), `## Connections`, `## Sources`.

It also writes every cluster hub and the root `wiki/index.md`, so in verbatim
mode the kb-linker's judgement step is not needed — run build_router_index.py,
build_graph_data.py, build_chat_data.py and validate.py next.

Re-runs are idempotent. A verbatim page that a later run no longer produces is
never deleted: it is marked `status: deprecated` with a `[DEPRECATED] ` title.

Usage:
  python3 assemble_verbatim.py [--root DIR] [--dry-run]
"""

import argparse
import json
import os
import re
import sys
from collections import OrderedDict, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kblib as K  # noqa: E402
from plan_batches import SEGMENT_CHARS, segments_of  # noqa: E402

WRITTEN_LOG = "verbatim-written.json"
HEADER_RE = re.compile(r"^<!-- kb:doc_id=.*?-->\s*$")
HEADING_RE = re.compile(r"^(#{1,6})(\s)")
MARKER_RE = re.compile(r"\[\[(V\d+|Vn)\]\]")
SHEET_RE = re.compile(r"^##\s+Sheet:\s*(.*?)\s*$")
LEGEND_HEAD_RE = re.compile(r"^###\s+Shared values\s*$")
LEGEND_ENTRY_RE = re.compile(r"^- \*\*(V\d+)\*\* — ")
LANG_RE = re.compile(r"_([A-Z]{2})_(?:[A-Z]{2}|XX)$")
LANGS = {"EN", "DE", "ES", "PT", "ZH", "JA", "FR", "IT", "NL", "RU", "KO", "PL", "CS", "HU", "TR", "SV", "DA", "FI", "NO"}
SCOPE_RE = re.compile(r"^([0-9A-Z]{2,5})_")
MAX_SIBLINGS = 4


def clean_line(text, limit=200):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    # digests may quote the [[Vn]] legend notation; in metadata it would read as a wikilink
    text = MARKER_RE.sub(lambda m: "⟦" + m.group(1) + "⟧", text)
    if len(text) > limit:
        text = text[: limit - 1].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return text


def cell(text):
    return clean_line(text).replace("|", "\\|")


def cluster_tag(slug):
    return "kb/" + re.sub(r"^\d+-", "", slug)


def load_digest(path):
    data = K.read_json(path, None)
    return data if isinstance(data, dict) else {}


def doc_number(doc_id):
    m = re.search(r"-(\d+)$", doc_id)
    return m.group(1) if m else doc_id


def sheet_map(lines):
    """Per line: index of the sheet it belongs to; plus per-sheet legend entries."""
    sheet_of, legend = [], defaultdict(dict)   # legend[sheet] = {label: (line_no, text)}
    sheet, in_legend = -1, False
    names = {}
    for i, line in enumerate(lines, 1):
        m = SHEET_RE.match(line)
        if m:
            sheet += 1
            names[sheet] = m.group(1)
            in_legend = False
        elif LEGEND_HEAD_RE.match(line):
            in_legend = True
        elif in_legend:
            e = LEGEND_ENTRY_RE.match(line)
            if e:
                legend[sheet][e.group(1)] = (i, line)
        sheet_of.append(sheet)
    return sheet_of, legend, names


def render_body(lines):
    out = []
    for line in lines:
        if HEADER_RE.match(line):
            continue
        line = MARKER_RE.sub(lambda m: "⟦" + m.group(1) + "⟧", line)
        line = HEADING_RE.sub(lambda m: ("#" + m.group(1) if len(m.group(1)) < 6 else m.group(1)) + m.group(2), line)
        out.append(line)
    return "\n".join(out).strip("\n")


def borrowed_legend(lines, start, end, sheet_of, legend, names):
    """Legend entries referenced in lines start..end whose definition lies outside."""
    need = OrderedDict()
    for i in range(start, end + 1):
        line = lines[i - 1]
        if "[[V" not in line:
            continue
        sheet = sheet_of[i - 1]
        for label in MARKER_RE.findall(line):
            if label == "Vn":
                continue
            entry = legend.get(sheet, {}).get(label)
            if entry and not (start <= entry[0] <= end):
                need.setdefault(sheet, OrderedDict())[label] = entry[1]
    if not need:
        return ""
    parts = ["## Shared values used in this part",
             "",
             "Copied verbatim from the `### Shared values` legend of the same sheet, "
             "which sits in another part of this document. A cell reading `⟦Vn⟧` holds "
             "the full text of `Vn`."]
    for sheet, entries in need.items():
        parts += ["", f"### Sheet: {names.get(sheet, sheet)}", ""]
        parts += list(entries.values())
    return "\n".join(parts)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root")
    ap.add_argument("--dry-run", action="store_true", help="report what would be written")
    args = ap.parse_args()

    root = K.project_root(args.root)
    P = K.paths(root)
    manifest = K.read_json(P["manifest"])
    taxonomy = K.read_json(P["taxonomy"])
    if not manifest or not taxonomy:
        raise SystemExit("error: needs .kb/manifest.json and .kb/taxonomy.json")

    clusters = OrderedDict((c["slug"], c) for c in taxonomy.get("clusters", []))
    topics = OrderedDict((n["id"], n) for n in taxonomy.get("nodes", []))
    docs = {d["doc_id"]: d for d in manifest.get("documents", []) if d.get("status") != "failed"}

    topics_of = defaultdict(list)          # doc_id -> [topic ids], taxonomy order
    for tid, t in topics.items():
        for doc_id in t.get("source_doc_ids", []):
            if doc_id in docs and tid not in topics_of[doc_id]:
                topics_of[doc_id].append(tid)
    unplaced = sorted(d for d in docs if d not in topics_of)

    today = K.today()
    taken = set()
    pages = []                              # one per node to write
    lead_of_doc = {}                        # doc_id -> first page
    pages_of_topic = defaultdict(list)      # topic id -> lead pages of member docs

    # ---- plan every page ---------------------------------------------------
    for doc_id in sorted(topics_of, key=lambda d: (topics_of[d][0], d)):
        d = docs[doc_id]
        primary = topics_of[doc_id][0]
        cluster = topics[primary]["cluster"]
        digest = load_digest(os.path.join(P["digests"], doc_id + ".json"))
        stem = os.path.splitext(os.path.basename(d["rel_path"]))[0]
        lang = LANG_RE.search(stem)
        lang = lang.group(1) if lang and lang.group(1) in LANGS else ""
        scope = SCOPE_RE.match(stem)
        scope = scope.group(1) if scope else ""
        base_title = clean_line(digest.get("title") or d.get("title") or stem, 120)

        chars = int(d.get("chars") or 0)
        if chars > SEGMENT_CHARS:
            segs = segments_of(root, d)
        else:
            segs = [{"index": 1, "total": 1, "start_line": None, "end_line": None}]

        for seg in segs:
            i, n = seg["index"], seg["total"]
            part_digest = digest
            if n > 1:
                pd = load_digest(os.path.join(P["digests"], "parts", f"{doc_id}.part-{i:03d}.json"))
                part_digest = pd or digest
            title = f"{base_title} ({stem})" + (f" — part {i} of {n}" if n > 1 else "")
            slug = K.slugify(f"{base_title}-{doc_number(doc_id)}", 70)
            if n > 1:
                slug = f"{slug}-part-{i:02d}"
            slug = K.unique_slug(slug, taken)
            desc = clean_line(part_digest.get("one_line") or digest.get("one_line") or "")
            if not desc:
                desc = clean_line(f"Verbatim text of {base_title} ({stem})")
            if n > 1 and part_digest is digest:
                desc = clean_line(f"Part {i} of {n}: {desc}")
            labels = [t.get("label") for t in sorted(
                part_digest.get("topics") or [], key=lambda t: t.get("weight") != "primary")]
            kws = []
            for kw in [topics[primary].get("title")] + labels + [scope]:
                kw = clean_line(kw, 60)
                if kw and kw.lower() not in {k.lower() for k in kws}:
                    kws.append(kw)
            conflicts = [clean_line(c, 600) for c in (part_digest.get("conflicts_suspected") or []) if c]
            page = {
                "doc": d, "doc_id": doc_id, "cluster": cluster, "slug": slug, "title": title,
                "description": desc, "keywords": kws[:10], "topic": primary,
                "topics": topics_of[doc_id], "lang": lang, "scope": scope, "stem": stem,
                "part": i, "parts": n, "seg": seg, "conflicts": conflicts,
                "method": d.get("method") or "", "edges": [],
            }
            pages.append(page)
            if i == 1:
                lead_of_doc[doc_id] = page
                for tid in topics_of[doc_id]:
                    pages_of_topic[tid].append(page)

    # parts of one document whose digests share a one_line would be identical to the
    # router; number them so every page keeps a description of its own
    same = defaultdict(list)
    for p in pages:
        if p["parts"] > 1:
            same[(p["doc_id"], p["description"])].append(p)
    for group in same.values():
        if len(group) > 1:
            for p in group:
                p["description"] = clean_line(f"Part {p['part']} of {p['parts']}: {p['description']}")

    by_slug = {p["slug"]: p for p in pages}

    def ref(p):
        return f"{p['cluster']}/{p['slug']}"

    # ---- edges ----------------------------------------------------------------
    parts_of = defaultdict(list)
    for p in pages:
        parts_of[p["doc_id"]].append(p)
    for p in pages:
        edges = [("part-of", "_cluster")]
        siblings = parts_of[p["doc_id"]]
        if p["parts"] > 1:
            for q in siblings:
                if abs(q["part"] - p["part"]) == 1:
                    edges.append(("related-to", ref(q)))
        mates = [q for q in pages_of_topic[p["topic"]] if q["doc_id"] != p["doc_id"]]
        mates.sort(key=lambda q: (not (p["scope"] and q["scope"] == p["scope"]), q["slug"]))
        for q in mates[:MAX_SIBLINGS]:
            edges.append(("related-to", ref(q)))
        if len(edges) == 1:
            for hint in topics[p["topic"]].get("edges_hint") or []:
                target = pages_of_topic.get(hint.get("target"))
                if target and target[0]["doc_id"] != p["doc_id"]:
                    edges.append(("see-also", ref(target[0])))
                if len(edges) >= 4:
                    break
        for tid in p["topics"][1:]:
            lead = pages_of_topic.get(tid, [None])[0]
            if lead and lead["doc_id"] != p["doc_id"] and ("see-also", ref(lead)) not in edges:
                edges.append(("see-also", ref(lead)))
        p["edges"] = edges

    # ---- write nodes ------------------------------------------------------------
    written, skipped = [], []
    text_cache = {}
    for p in pages:
        d = p["doc"]
        path = os.path.join(P["wiki"], p["cluster"], p["slug"] + ".md")
        if os.path.exists(path):
            fm = K.load_note(path)["frontmatter"]
            if fm.get("kind") != "verbatim":
                skipped.append(K.rel(path, P["wiki"]))
                continue
        src_path = os.path.join(root, d["extracted_path"])
        if src_path not in text_cache:
            text_cache.clear()
            with open(src_path, "r", encoding="utf-8") as fh:
                text_cache[src_path] = fh.read().split("\n")
        lines = text_cache[src_path]
        seg = p["seg"]
        start = seg["start_line"] or 1
        end = seg["end_line"] or len(lines)
        body_text = render_body(lines[start - 1:end])
        legend = ""
        if p["parts"] > 1 and any("[[V" in l for l in lines[start - 1:end]):
            sheet_of, leg, names = sheet_map(lines)
            legend = borrowed_legend(lines, start, end, sheet_of, leg, names)

        topic = topics[p["topic"]]
        cl = clusters.get(p["cluster"], {})
        where = f"`{d['rel_path']}`"
        span = (f", part {p['part']} of {p['parts']} (lines {start}–{end} of the extracted text)"
                if p["parts"] > 1 else "")
        fm = {
            "id": f"{p['cluster']}/{p['slug']}",
            "title": p["title"],
            "description": p["description"],
            "cluster": p["cluster"],
            "tags": [cluster_tag(p["cluster"])] + ["topic/" + t.split("/", 1)[1] for t in p["topics"]],
            "aliases": [p["stem"]] if p["parts"] == 1 else [],
            "keywords": p["keywords"],
            "sources": [d["rel_path"] + (f"#lines-{start}-{end}" if p["parts"] > 1 else "")],
            "confidence": "low" if p["conflicts"] else "high",
            "status": "active",
            "kind": "verbatim",
            "doc_id": p["doc_id"],
            "topic": p["topic"],
            "language": p["lang"],
            "part": f"{p['part']}/{p['parts']}",
            "created": today,
            "updated": today,
        }
        out = ["---", K.dump_frontmatter(fm), "---", "",
               f"# {p['title']}", "",
               f"*Verbatim text of {where}{span}, extracted with `{p['method']}`. "
               f"Grouped under **{topic.get('title')}** in {cl.get('title', p['cluster'])}. "
               "Nothing below the rule has been rewritten; headings are shifted one level down.*",
               "", "---", "", body_text, ""]
        if legend:
            out += [legend, ""]
        if p["conflicts"]:
            out += ["## Suspected conflicts", ""]
            for c in p["conflicts"]:
                out += ["> [!warning] Conflict", f"> Flagged while digesting this document, not verified: {c}", ""]
        out += ["## Connections"]
        out += [f"- {t} :: [[{target}]]" for t, target in p["edges"]]
        out += ["", "## Sources",
                f"- {where} — " + (f"lines {start}–{end} of the extracted text" if p["parts"] > 1 else "full document")
                + f" · extracted with `{p['method']}` · {int(d.get('chars') or 0):,} chars in the whole document", ""]
        if not args.dry_run:
            K.ensure_dir(os.path.dirname(path))
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("\n".join(out))
        written.append(K.rel(path, P["wiki"]))

    # ---- hubs ---------------------------------------------------------------------
    own = defaultdict(list)
    for p in pages:
        own[p["cluster"]].append(p)
    for slug, c in clusters.items():
        rows = ["---", K.dump_frontmatter({
            "title": c.get("title"),
            "description": clean_line(c.get("description")),
            "cluster": slug,
            "type": "cluster",
            "tags": [cluster_tag(slug), "kb/hub"],
            "keywords": c.get("keywords") or [],
            "node_count": len(own[slug]),
            "created": today,
            "updated": today,
        }), "---", "", f"# {c.get('title')}", ""]
        if c.get("scope_note"):
            rows += [clean_line(c["scope_note"], 2000), ""]
        rows += ["Every node below is the verbatim text of one source document (or one part "
                 "of a long one), grouped by topic.", "", "## Nodes", ""]
        for tid, t in topics.items():
            if t.get("cluster") != slug:
                continue
            members = []
            for lead in pages_of_topic.get(tid, []):
                members += parts_of[lead["doc_id"]]
            if not members:
                continue
            rows += [f"### {t.get('title')}", "", clean_line(t.get("description")), "",
                     "| Node | Description |", "| --- | --- |"]
            for q in members:
                rows.append(f"| [[{ref(q)}\\|{cell(q['title'])}]] | {cell(q['description'])} |")
            rows.append("")
        related = [r for r in (c.get("related_clusters") or []) if r in clusters and r != slug]
        if related:
            rows += ["## Related categories"] + [f"- related-to :: [[{r}/_cluster]]" for r in related] + [""]
        if not args.dry_run:
            K.ensure_dir(os.path.join(P["wiki"], slug))
            with open(os.path.join(P["wiki"], slug, K.CLUSTER_HUB), "w", encoding="utf-8") as fh:
                fh.write("\n".join(rows))

    # ---- root index ---------------------------------------------------------------
    idx = ["---", K.dump_frontmatter({
        "title": "Knowledge Base",
        "description": "Root map of the knowledge base: every category, what it covers and how many verbatim source nodes it holds.",
        "tags": ["kb/meta"],
        "updated": today,
    }), "---", "", "# Knowledge Base", "",
        f"{len(pages)} nodes holding the verbatim text of {len(lead_of_doc)} source documents, "
        f"grouped into {len(clusters)} categories and {sum(1 for t in pages_of_topic if pages_of_topic[t])} topics. "
        "Node pages are not summaries: each one is the source document itself.", "",
        "## Categories", "", "| Category | Description | Nodes |", "| --- | --- | --- |"]
    for slug, c in clusters.items():
        idx.append(f"| [[{slug}/_cluster\\|{cell(c.get('title'))}]] | {cell(c.get('description'))} | {len(own[slug])} |")
    idx += ["", "## How to navigate", "",
            "- [[_meta/router-index|Router index]] — both routing layers in one page",
            "- [[_meta/conflicts|Conflicts]] — every suspected conflict, collected",
            "- `graph.html` (graph) and `chat.html` (ask questions) — open in a browser", ""]
    if not args.dry_run:
        with open(os.path.join(P["wiki"], "index.md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(idx))

    # ---- deprecate pages a previous run wrote but this one did not -----------------
    log_path = os.path.join(P["kb"], WRITTEN_LOG)
    previous = set(K.read_json(log_path, []) or [])
    deprecated = []
    for relp in sorted(previous - set(written)):
        path = os.path.join(P["wiki"], relp)
        if not os.path.exists(path):
            continue
        note = K.load_note(path)
        fm = dict(note["frontmatter"])
        if fm.get("status") == "deprecated":
            continue
        fm["status"] = "deprecated"
        fm["title"] = "[DEPRECATED] " + str(fm.get("title") or "")
        fm["updated"] = today
        if not args.dry_run:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("---\n" + K.dump_frontmatter(fm) + "\n---\n" + note["body"])
        deprecated.append(relp)
    if not args.dry_run:
        K.write_json(log_path, sorted(set(written) | set(deprecated)))

    parts_total = sum(1 for p in pages if p["parts"] > 1)
    print(f"{'[dry-run] ' if args.dry_run else ''}verbatim nodes: {len(written)} "
          f"from {len(lead_of_doc)} documents ({parts_total} part pages) in {len(clusters)} clusters")
    for slug in clusters:
        print(f"  {slug:55s} {len(own[slug]):4d}")
    if skipped:
        print(f"skipped {len(skipped)} existing non-verbatim page(s): {', '.join(skipped[:5])}")
    if deprecated:
        print(f"marked {len(deprecated)} page(s) deprecated (no longer produced)")
    if unplaced:
        print(f"\nUNPLACED: {len(unplaced)} document(s) are in no taxonomy node — run the architect "
              "in incremental mode to place them:")
        for doc_id in unplaced[:10]:
            print(f"  - {docs[doc_id]['rel_path']}")
        if len(unplaced) > 10:
            print(f"  ... and {len(unplaced) - 10} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
