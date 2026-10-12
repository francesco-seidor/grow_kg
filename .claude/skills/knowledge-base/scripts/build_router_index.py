#!/usr/bin/env python3
"""Build the two-layer router index from the wiki's frontmatter.

Frontmatter on disk is the single source of truth, so the index can never drift
from the notes. Progressive disclosure, same shape as skill frontmatter:

  layer 1  categories.json   pick a cluster from cluster descriptions
  layer 2  <cluster>.json    pick a node from node descriptions in that cluster

Outputs (all under wiki/_meta/):
  router/categories.json     layer 1 payload
  router/<cluster>.json      layer 2 payload, one per cluster
  router/index.json          manifest + inline layer 1, single-file bootstrap
  router-index.md            human-readable mirror of both layers

Usage:
  python3 build_router_index.py [--root DIR] [--max-description N] [--strict]
"""

import argparse
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kblib as K  # noqa: E402

MAX_DESCRIPTION = 200
FILLER_PREFIXES = (
    "this page", "this note", "this document", "this node", "describes the",
    "a page about", "information about", "overview of the page",
)


def embedding_text(title, description, keywords, aliases, cluster_title):
    bits = [str(title).strip()]
    if cluster_title:
        bits.append(f"({cluster_title})")
    if description:
        bits.append("— " + str(description).strip().rstrip("."))
    extras = [k for k in list(keywords) + list(aliases) if k]
    if extras:
        bits.append("| keywords: " + ", ".join(dict.fromkeys(extras)))
    return " ".join(bits)


def check_description(description, where, warnings, max_len):
    text = (description or "").strip()
    if not text:
        warnings.append({"level": "error", "where": where, "issue": "missing description"})
        return
    if len(text) > max_len:
        warnings.append({
            "level": "error", "where": where,
            "issue": f"description is {len(text)} chars (max {max_len})",
        })
    low = text.lower()
    if low.startswith(FILLER_PREFIXES):
        warnings.append({
            "level": "warning", "where": where,
            "issue": "description opens with filler; state what it answers instead",
        })
    # word count misreads CJK, which has no spaces: there, count the characters instead
    cjk = len(re.findall(r"[぀-ヿ㐀-鿿가-힯]", text))
    if len(text.split()) < 4 and cjk < 12:
        warnings.append({
            "level": "warning", "where": where,
            "issue": "description is too thin to route on",
        })


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root")
    ap.add_argument("--max-description", type=int, default=MAX_DESCRIPTION)
    ap.add_argument("--strict", action="store_true", help="exit 1 on warnings too")
    args = ap.parse_args()

    root = K.project_root(args.root)
    P = K.paths(root)
    if not os.path.isdir(P["wiki"]):
        raise SystemExit(f"error: no wiki at {P['wiki']}")

    nodes, hubs = K.scan_vault(P["wiki"])
    warnings = []

    clusters = {}
    for hub in hubs:
        fm = hub["frontmatter"]
        slug = str(fm.get("cluster") or os.path.basename(os.path.dirname(hub["path"])))
        title = str(fm.get("title") or slug)
        desc = str(fm.get("description") or "")
        check_description(desc, f"cluster {slug}", warnings, args.max_description)
        keywords = K.as_list(fm.get("keywords"))
        if not keywords:
            warnings.append({"level": "warning", "where": f"cluster {slug}",
                             "issue": "no keywords — layer-1 matching will be weaker"})
        clusters[slug] = {
            "slug": slug,
            "title": title,
            "description": desc,
            "keywords": keywords,
            "tags": K.as_list(fm.get("tags")),
            "hub_path": K.rel(hub["path"], P["wiki"]),
            "index_path": f"{K.META_DIR}/router/{slug}.json",
            "nodes": [],
        }

    orphan_clusters = set()
    for note in nodes:
        fm = note["frontmatter"]
        folder = os.path.basename(os.path.dirname(note["path"]))
        slug = str(fm.get("cluster") or folder)
        if slug not in clusters:
            orphan_clusters.add(slug)
            clusters[slug] = {
                "slug": slug, "title": slug, "description": "",
                "keywords": [], "tags": [],
                "hub_path": f"{slug}/{K.CLUSTER_HUB}",
                "index_path": f"{K.META_DIR}/router/{slug}.json",
                "nodes": [],
            }
        node_id = str(fm.get("id") or f"{slug}/{note['basename']}")
        title = str(fm.get("title") or note["basename"])
        desc = str(fm.get("description") or "")
        check_description(desc, f"node {node_id}", warnings, args.max_description)
        keywords = K.as_list(fm.get("keywords"))
        aliases = K.as_list(fm.get("aliases"))
        status = str(fm.get("status") or "active")
        if not note["has_frontmatter"]:
            warnings.append({"level": "error", "where": f"node {node_id}",
                             "issue": "no YAML frontmatter"})
        clusters[slug]["nodes"].append({
            "id": node_id,
            "title": title,
            "description": desc,
            "keywords": keywords,
            "aliases": aliases,
            "tags": K.as_list(fm.get("tags")),
            "path": K.rel(note["path"], P["wiki"]),
            "cluster": slug,
            "status": status,
            "confidence": str(fm.get("confidence") or "unknown"),
            "sources": K.as_list(fm.get("sources")),
            "updated": str(fm.get("updated") or ""),
            "embedding_text": embedding_text(
                title, desc, keywords, aliases, clusters[slug]["title"]
            ),
        })

    for slug in orphan_clusters:
        warnings.append({"level": "error", "where": f"cluster {slug}",
                         "issue": f"no {K.CLUSTER_HUB} hub note — cluster has no layer-1 description"})

    K.ensure_dir(P["router"])
    ordered = sorted(clusters.values(), key=lambda c: c["slug"])

    categories = []
    for cluster in ordered:
        active = [n for n in cluster["nodes"] if n["status"] != "deprecated"]
        categories.append({
            "slug": cluster["slug"],
            "title": cluster["title"],
            "description": cluster["description"],
            "keywords": cluster["keywords"],
            "tags": cluster["tags"],
            "node_count": len(active),
            "deprecated_count": len(cluster["nodes"]) - len(active),
            "hub_path": cluster["hub_path"],
            "index_path": cluster["index_path"],
            "embedding_text": embedding_text(
                cluster["title"], cluster["description"], cluster["keywords"], [], ""
            ),
        })

    layer1 = {
        "version": 1,
        "layer": 1,
        "generated": K.now_iso(),
        "vault": "wiki",
        "usage": (
            "Layer 1 of a two-layer router. Score the query against each category's "
            "description/keywords/embedding_text, pick the best with a confidence "
            "score, then load that category's index_path for layer 2."
        ),
        "count": len(categories),
        "categories": categories,
    }
    K.write_json(os.path.join(P["router"], "categories.json"), layer1)

    written = []
    for cluster in ordered:
        payload = {
            "version": 1,
            "layer": 2,
            "generated": K.now_iso(),
            "cluster": cluster["slug"],
            "cluster_title": cluster["title"],
            "cluster_description": cluster["description"],
            "usage": (
                "Layer 2 of a two-layer router. Score the query against each node's "
                "description/keywords/embedding_text, pick the best with a confidence "
                "score, then read `path` (relative to the wiki/ vault root)."
            ),
            "count": len(cluster["nodes"]),
            "nodes": sorted(cluster["nodes"], key=lambda n: n["id"]),
        }
        path = os.path.join(P["router"], f"{cluster['slug']}.json")
        K.write_json(path, payload)
        written.append(K.rel(path, P["wiki"]))

    # Remove per-cluster indexes for clusters that no longer exist.
    valid = {f"{c['slug']}.json" for c in ordered} | {"categories.json", "index.json"}
    stale = []
    for name in sorted(os.listdir(P["router"])):
        if name.endswith(".json") and name not in valid:
            os.remove(os.path.join(P["router"], name))
            stale.append(name)

    fingerprint = hashlib.sha256(
        json.dumps(
            [[c["slug"], c["description"], [n["id"] for n in c["nodes"]]] for c in ordered],
            sort_keys=True,
        ).encode()
    ).hexdigest()[:16]

    total_nodes = sum(len(c["nodes"]) for c in ordered)
    errors = [w for w in warnings if w["level"] == "error"]
    manifest = {
        "version": 1,
        "generated": K.now_iso(),
        "content_hash": fingerprint,
        "vault": "wiki",
        "how_to_route": [
            "1. Load _meta/router/categories.json and score the query against each category.",
            "2. Take the best category (plus runners-up above your confidence floor).",
            "3. Load that category's index_path and score the query against its nodes.",
            "4. Read the winning node's `path`. Every node is self-contained.",
            "5. Below your confidence floor, say the knowledge base does not cover it.",
        ],
        "totals": {
            "categories": len(ordered),
            "nodes": total_nodes,
            "deprecated_nodes": sum(c["deprecated_count"] for c in categories),
            "errors": len(errors),
            "warnings": len(warnings) - len(errors),
        },
        "layer1_path": f"{K.META_DIR}/router/categories.json",
        "layer2_paths": {c["slug"]: c["index_path"] for c in categories},
        "categories": categories,
        "issues": warnings,
    }
    K.write_json(os.path.join(P["router"], "index.json"), manifest)

    # Human-readable mirror.
    lines = [
        "---",
        K.dump_frontmatter({
            "title": "Router Index",
            "description": "Human-readable mirror of the two-layer router index; the JSON under _meta/router/ is authoritative.",
            "tags": ["kb/meta"],
            "generated": K.now_iso(),
        }, order=["title", "description", "tags", "generated"]),
        "---",
        "",
        "# Router Index",
        "",
        f"Generated {K.now_iso()} · {len(ordered)} categories · {total_nodes} nodes · hash `{fingerprint}`",
        "",
        "Machine-readable payloads live in [`_meta/router/`](router/). This page mirrors them for humans.",
        "",
        "## Layer 1 — categories",
        "",
        "| Category | Nodes | Description |",
        "| --- | --- | --- |",
    ]
    for c in categories:
        desc = (c["description"] or "*missing*").replace("|", "\\|")
        lines.append(f"| [[{c['slug']}/_cluster\\|{c['title']}]] | {c['node_count']} | {desc} |")
    lines += ["", "## Layer 2 — nodes by category", ""]
    for cluster in ordered:
        lines += [f"### {cluster['title']} (`{cluster['slug']}`)", ""]
        if not cluster["nodes"]:
            lines += ["*No nodes yet.*", ""]
            continue
        lines += ["| Node | Description |", "| --- | --- |"]
        for n in sorted(cluster["nodes"], key=lambda n: n["id"]):
            desc = (n["description"] or "*missing*").replace("|", "\\|")
            flag = " `deprecated`" if n["status"] == "deprecated" else ""
            stem = n["path"][:-3] if n["path"].endswith(".md") else n["path"]
            lines.append(f"| [[{stem}\\|{n['title']}]]{flag} | {desc} |")
        lines.append("")
    with open(os.path.join(P["meta"], "router-index.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines).rstrip() + "\n")

    print(f"router index: {len(ordered)} categories, {total_nodes} nodes, hash {fingerprint}")
    for c in categories:
        print(f"  {c['slug']:<34} {c['node_count']:>4} nodes")
    if stale:
        print(f"  removed stale index files: {', '.join(stale)}")
    if warnings:
        print(f"\nissues ({len(errors)} error, {len(warnings) - len(errors)} warning):")
        for w in warnings[:30]:
            print(f"  [{w['level']}] {w['where']}: {w['issue']}")
        if len(warnings) > 30:
            print(f"  ... and {len(warnings) - 30} more (see _meta/router/index.json)")
    else:
        print("  no issues")

    if errors:
        return 1
    return 1 if (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
