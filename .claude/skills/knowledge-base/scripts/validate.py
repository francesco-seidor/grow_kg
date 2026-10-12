#!/usr/bin/env python3
"""Validate the compiled wiki. Exits 1 on errors, 0 otherwise (--strict: also warnings).

Checks:
  schema      frontmatter present, required fields, description length/quality
  links       unresolved wikilinks, ambiguous basenames, unknown edge types
  graph       orphan nodes (no inbound link; deprecated pages exempt), clusters without a hub
  clusters    hub exists per cluster, cluster field matches folder, size balance
  coverage    manifest documents that reached no node; sources not in the manifest
  router      router JSON in sync with the files on disk
  viewer      the viewer copies are current; _meta/graph-data.js is present
              and consistent with the nodes
  conflicts   open conflict callouts, listed for review (never auto-resolved)

Usage:
  python3 validate.py [--root DIR] [--strict] [--json]
"""

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kblib as K  # noqa: E402

REQUIRED_NODE_FIELDS = ["id", "title", "description", "cluster", "tags", "sources", "status"]
REQUIRED_HUB_FIELDS = ["title", "description", "cluster", "type"]
MAX_DESCRIPTION = 200
MAX_CLUSTER_NODES = 40
MIN_CLUSTER_NODES = 2


class Report:
    def __init__(self):
        self.items = []

    def add(self, level, check, where, issue, hint=None):
        self.items.append({"level": level, "check": check, "where": where,
                           "issue": issue, **({"hint": hint} if hint else {})})

    error = lambda self, *a, **k: self.add("error", *a, **k)  # noqa: E731
    warn = lambda self, *a, **k: self.add("warning", *a, **k)  # noqa: E731
    info = lambda self, *a, **k: self.add("info", *a, **k)  # noqa: E731

    def count(self, level):
        return sum(1 for i in self.items if i["level"] == level)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    root = K.project_root(args.root)
    P = K.paths(root)
    R = Report()

    if not os.path.isdir(P["wiki"]):
        raise SystemExit(f"error: no wiki at {P['wiki']} — nothing to validate")

    nodes, hubs = K.scan_vault(P["wiki"])
    # Resolve against every file in wiki/, including _meta/ and index.md.
    resolve, ambiguous = K.build_link_resolver(K.load_all_notes(P["wiki"]), [], P["wiki"])
    hub_clusters = {
        str(h["frontmatter"].get("cluster") or os.path.basename(os.path.dirname(h["path"]))): h
        for h in hubs
    }

    # ---- schema -----------------------------------------------------------
    seen_ids, seen_titles = {}, defaultdict(list)
    for note in nodes:
        fm = note["frontmatter"]
        where = note["rel"]
        if not note["has_frontmatter"]:
            R.error("schema", where, "no YAML frontmatter",
                    "every node needs the full frontmatter block")
            continue
        for field in REQUIRED_NODE_FIELDS:
            if field not in fm or fm.get(field) in ("", None, []):
                if field in ("tags", "sources"):
                    R.warn("schema", where, f"empty `{field}`")
                else:
                    R.error("schema", where, f"missing `{field}`")
        desc = str(fm.get("description") or "").strip()
        if desc and len(desc) > MAX_DESCRIPTION:
            R.error("schema", where,
                    f"description is {len(desc)} chars (max {MAX_DESCRIPTION})",
                    "the router reads this; keep it one tight sentence")
        # word count misreads CJK, which has no spaces: there, count the characters instead
        cjk = len(re.findall(r"[぀-ヿ㐀-鿿가-힯]", desc))
        if desc and len(desc.split()) < 4 and cjk < 12:
            R.warn("schema", where, "description too thin to route on")
        if desc.lower().startswith(("this page", "this note", "this document")):
            R.warn("schema", where, "description opens with filler",
                   "say what questions it answers instead")
        node_id = str(fm.get("id") or "")
        if node_id:
            if node_id in seen_ids:
                R.error("schema", where, f"duplicate id `{node_id}` (also {seen_ids[node_id]})")
            seen_ids[node_id] = where
            expected = K.rel(note["path"], P["wiki"])[:-3]
            if node_id != expected:
                R.warn("schema", where, f"id `{node_id}` does not match its path `{expected}`")
        title = str(fm.get("title") or "").strip().lower()
        if title:
            seen_titles[title].append(where)
        status = str(fm.get("status") or "")
        if status not in ("active", "deprecated", ""):
            R.warn("schema", where, f"unexpected status `{status}`")
        if str(fm.get("confidence") or "") not in ("high", "medium", "low", ""):
            R.warn("schema", where, f"unexpected confidence `{fm.get('confidence')}`")
        if not re.search(r"^#\s+\S", note["body"], re.MULTILINE):
            R.warn("schema", where, "no H1 heading in the body")
        if "## Sources" not in note["body"]:
            R.warn("schema", where, "no `## Sources` section")
        if "## Connections" not in note["body"]:
            R.warn("graph", where, "no `## Connections` section — node will be isolated")

    for title, places in seen_titles.items():
        if len(places) > 1:
            R.warn("schema", places[0], f"title reused by {len(places)} nodes: {', '.join(places)}")

    for hub in hubs:
        fm = hub["frontmatter"]
        for field in REQUIRED_HUB_FIELDS:
            if field not in fm or fm.get(field) in ("", None, []):
                R.error("schema", hub["rel"], f"hub missing `{field}`")
        desc = str(fm.get("description") or "").strip()
        if desc and len(desc) > MAX_DESCRIPTION:
            R.error("schema", hub["rel"],
                    f"cluster description is {len(desc)} chars (max {MAX_DESCRIPTION})")

    # ---- links & graph ----------------------------------------------------
    inbound = Counter()
    root_index_path = os.path.join(P["wiki"], "index.md")
    linkers = list(nodes) + list(hubs)
    if os.path.exists(root_index_path):
        idx = K.load_note(root_index_path)
        idx["rel"] = "index.md"
        linkers.append(idx)  # the root index's own links must resolve too
    for note in linkers:
        for link in K.extract_wikilinks(note["body"]):
            dest = resolve(link["target"], note["path"])
            if dest is None:
                level = "error"
                hint = None
                if os.path.basename(link["target"]) in ambiguous:
                    level = "warning"
                    hint = "basename is ambiguous; use `cluster/note`"
                R.add(level, "links", note["rel"],
                      f"unresolved wikilink [[{link['target']}]]", hint)
            else:
                inbound[dest] += 1
        for edge in K.extract_edges(note["body"]):
            if edge["type"] not in K.EDGE_TYPES:
                R.warn("links", note["rel"],
                       f"unknown edge type `{edge['type']}`",
                       "allowed: " + ", ".join(K.EDGE_TYPES))

    for note in nodes:
        retired = str(note["frontmatter"].get("status") or "") == "deprecated"
        if inbound[note["path"]] == 0 and not retired:   # nothing should link to a retired page
            R.warn("graph", note["rel"], "orphan: nothing links to it",
                   "add it to its cluster hub or link it from a related node")

    # ---- clusters ---------------------------------------------------------
    by_cluster = defaultdict(list)
    for note in nodes:
        folder = os.path.basename(os.path.dirname(note["path"]))
        declared = str(note["frontmatter"].get("cluster") or folder)
        by_cluster[declared].append(note)
        if declared != folder:
            R.error("clusters", note["rel"],
                    f"cluster `{declared}` does not match folder `{folder}`")
    for slug, members in sorted(by_cluster.items()):
        if slug not in hub_clusters:
            R.error("clusters", slug, f"no {K.CLUSTER_HUB} hub note",
                    "layer-1 routing needs a cluster description")
        if len(members) > MAX_CLUSTER_NODES:
            R.warn("clusters", slug,
                   f"{len(members)} nodes (soft cap {MAX_CLUSTER_NODES}) — consider splitting")
        if len(members) < MIN_CLUSTER_NODES:
            R.warn("clusters", slug,
                   f"only {len(members)} node(s) — consider merging into a neighbour")
    for slug in hub_clusters:
        if slug not in by_cluster:
            R.warn("clusters", slug, "hub with no nodes")

    if not os.path.exists(root_index_path):
        R.error("clusters", "index.md", "missing root index (wiki/index.md)")

    # ---- coverage ---------------------------------------------------------
    manifest = K.read_json(P["manifest"])
    if manifest:
        known_sources = {d["rel_path"] for d in manifest.get("documents", [])}
        cited = set()
        for note in nodes:
            for src in K.as_list(note["frontmatter"].get("sources")):
                base = src.split("#")[0].strip().strip("`")
                cited.add(base)
                if base and base not in known_sources:
                    R.warn("coverage", note["rel"],
                           f"source `{base}` is not in .kb/manifest.json",
                           "renamed or removed from raw_assets?")
        uncited = sorted(
            d["rel_path"] for d in manifest.get("documents", [])
            if d.get("status") != "failed" and d["rel_path"] not in cited
        )
        for path in uncited:
            R.warn("coverage", path, "document reached no node")
        failed = [d for d in manifest.get("documents", []) if d.get("status") == "failed"]
        for d in failed:
            R.error("coverage", d["rel_path"], f"extraction failed: {d.get('error', '')[:120]}")
    else:
        R.info("coverage", ".kb/manifest.json", "no manifest — coverage not checked")

    unsupported = K.read_json(P["unsupported"], {})
    for f in (unsupported or {}).get("files", []):
        R.info("coverage", f["rel_path"], f"skipped: {f['reason']}")

    # ---- router ----------------------------------------------------------
    cat_path = os.path.join(P["router"], "categories.json")
    categories = K.read_json(cat_path)
    if not categories:
        R.error("router", "_meta/router/categories.json", "missing",
                "run build_router_index.py")
    else:
        indexed = {c["slug"] for c in categories.get("categories", [])}
        for slug in by_cluster:
            if slug not in indexed:
                R.error("router", slug, "cluster missing from categories.json")
        for slug in indexed:
            if slug not in by_cluster and slug not in hub_clusters:
                R.error("router", slug, "categories.json lists a cluster that is not on disk")
        for slug in indexed:
            layer2 = K.read_json(os.path.join(P["router"], f"{slug}.json"))
            if not layer2:
                R.error("router", slug, f"missing layer-2 index {slug}.json")
                continue
            listed = {n["id"] for n in layer2.get("nodes", [])}
            actual = {
                str(n["frontmatter"].get("id") or K.rel(n["path"], P["wiki"])[:-3])
                for n in by_cluster.get(slug, [])
            }
            for missing in sorted(actual - listed):
                R.error("router", slug, f"node `{missing}` missing from the layer-2 index")
            for extra in sorted(listed - actual):
                R.error("router", slug, f"layer-2 index lists `{extra}` which is not on disk")
            for n in layer2.get("nodes", []):
                if not str(n.get("description") or "").strip():
                    R.error("router", n.get("id", slug), "router entry has no description")

    # ---- viewer ----------------------------------------------------------
    # The family is named `viewer`, not `graph`: `graph` is already used above
    # for orphans and missing Connections sections, and merging the two would
    # corrupt the by_check counts that kb-auditor reports on.
    graph_data = P["graph_data"]
    where = os.path.join(K.META_DIR, K.GRAPH_DATA)
    disk_paths = {K.rel(n["path"], P["wiki"]) for n in list(nodes) + list(hubs)}

    # The viewers are shipped, not generated, so the thing that can drift is a
    # copy nobody would think to look at. Nothing else checks it.
    missing_copies, drifted_copies = K.viewer_assets_status(P)
    for item in missing_copies:
        R.warn("viewer", item, "viewer file not installed", "run init_wiki.py")
    for item in drifted_copies:
        R.warn("viewer", item,
               "differs from the shipped asset — hand-edited, or from another "
               "version of this skill",
               "run init_wiki.py; viewer behaviour is changed in "
               "assets/, never in wiki/")

    if not os.path.exists(graph_data):
        # The markdown and the router index ARE the knowledge base; the viewer
        # is a view of it, so a missing view must not fail the build. The page
        # itself handles this state — it shows its "run /kb-build first" banner.
        R.warn("viewer", where, "missing", "run build_graph_data.py")
    else:
        payload = K.read_data_payload(graph_data)
        if payload is None:
            # Worse than missing: it looks authoritative and is not.
            R.error("viewer", where,
                    "no parseable payload — truncated or hand-edited",
                    "regenerate with build_graph_data.py")
        else:
            embedded = {n.get("path") for n in payload.get("nodes", [])}
            if embedded != disk_paths:
                R.error("viewer", where,
                        f"carries {len(embedded)} nodes but {len(disk_paths)} are on disk",
                        "re-run build_graph_data.py")
                for extra in sorted(embedded - disk_paths)[:10]:
                    R.error("viewer", where, f"carries a node not on disk: `{extra}`")
                for missing in sorted(disk_paths - embedded)[:10]:
                    R.error("viewer", where, f"node `{missing}` is missing from the viewer")
            keys = {n.get("key") for n in payload.get("nodes", [])}
            bad = [e for e in payload.get("edges", [])
                   if e.get("source") not in keys or e.get("target") not in keys]
            if bad:
                R.error("viewer", where,
                        f"{len(bad)} edge(s) reference a node not in the payload, first: "
                        f"`{bad[0].get('source')} -> {bad[0].get('target')}`")
            if payload.get("schema") != K.GRAPH_SCHEMA:
                R.warn("viewer", where,
                       f"payload schema {payload.get('schema')} "
                       f"(this validate.py expects {K.GRAPH_SCHEMA})")
        # mtime is fallible (git checkout, cp -r, touch all reorder it without a
        # real change), so staleness is a prompt to regenerate, never a gate.
        # It is measured against the data file, never graph.html: that is now a
        # copy, whose timestamp moves when the viewer changes and never when the
        # wiki does — comparing nodes against it would be worse than fallible.
        newest = max(((os.path.getmtime(n["path"]), n["path"])
                      for n in list(nodes) + list(hubs)), default=(0, ""))
        if newest[0] > os.path.getmtime(graph_data) + 2:
            R.warn("viewer", where, "older than the newest node markdown",
                   f"`{K.rel(newest[1], P['wiki'])}` changed after it — "
                   f"re-run build_graph_data.py")

    d3_installed = os.path.join(P["wiki_vendor"], "d3.v7.min.js")
    if os.path.exists(P["graph_html"]) and not os.path.exists(d3_installed):
        R.warn("viewer", K.rel(d3_installed, P["wiki"]),
               "missing — graph.html will fall back to the d3 CDN and need the network",
               "run init_wiki.py")

    for leftover in K.stale_obsidian_artifacts(P["wiki"]):
        R.info("viewer", leftover,
               "stale Obsidian artefact — no longer generated or read",
               "safe to delete by hand; the viewer is wiki/graph.html")

    # The data file is missing before the first compile, which is a state the
    # page is designed for. A chat.html with no corpus beside it is the same.
    if os.path.exists(P["chat_html"]) and not os.path.exists(P["chat_data"]):
        R.warn("viewer", os.path.join(K.META_DIR, K.CHAT_DATA), "missing",
               "run build_chat_data.py")

    # ---- conflicts -------------------------------------------------------
    conflicts = []
    for note in nodes:
        for m in K.CALLOUT_CONFLICT_RE.finditer(note["body"]):
            tail = note["body"][m.end():m.end() + 400].split("\n")
            detail = " ".join(
                l.lstrip("> ").strip() for l in tail if l.strip().startswith(">")
            )[:240]
            conflicts.append({"node": note["rel"], "detail": detail})
    for c in conflicts:
        R.info("conflicts", c["node"], f"open conflict: {c['detail'] or '(no detail)'}")

    # ---- output ----------------------------------------------------------
    summary = {
        "generated": K.now_iso(),
        "totals": {
            "nodes": len(nodes),
            "clusters": len(by_cluster),
            "hubs": len(hubs),
            "errors": R.count("error"),
            "warnings": R.count("warning"),
            "infos": R.count("info"),
            "open_conflicts": len(conflicts),
        },
        "by_check": dict(Counter(i["check"] for i in R.items)),
        "issues": R.items,
    }
    K.write_json(P["validation"], summary)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        t = summary["totals"]
        print(f"wiki: {t['nodes']} nodes in {t['clusters']} clusters")
        print(f"errors: {t['errors']}  warnings: {t['warnings']}  "
              f"notes: {t['infos']}  open conflicts: {t['open_conflicts']}")
        for level in ("error", "warning", "info"):
            items = [i for i in R.items if i["level"] == level]
            if not items:
                continue
            shown = items if level == "error" else items[:40]
            print(f"\n{level.upper()}S ({len(items)}):")
            for i in shown:
                hint = f"  [{i['hint']}]" if i.get("hint") else ""
                print(f"  {i['check']:<9} {i['where']}: {i['issue']}{hint}")
            if len(shown) < len(items):
                print(f"  ... and {len(items) - len(shown)} more (see .kb/validation.json)")
        if not R.items:
            print("\nclean.")
        print(f"\nfull report: {K.rel(P['validation'], root)}")

    if R.count("error"):
        return 1
    return 1 if (args.strict and R.count("warning")) else 0


if __name__ == "__main__":
    sys.exit(main())
