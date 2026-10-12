#!/usr/bin/env python3
"""Generate wiki/_meta/graph-data.js — the payload wiki/graph.html renders.

The viewer itself is not generated: `wiki/graph.html` is a verbatim copy of
`assets/graph-viewer.html`, installed by init_wiki.py. This script writes only
the data it loads, so the 400KB page stops being rewritten on every compile and
a viewer fix no longer needs a recompile.

The payload covers every cluster, node and typed connection, plus everything
wrong with the build — open conflicts, validation errors, coverage gaps and
unsupported documents.

Reads `wiki/` for the graph itself and `.kb/` for the build's own findings.
`.kb/` is disposable, so every section degrades explicitly rather than silently:
coverage without a manifest reports "unavailable", never "zero gaps".

The output is a `.js` assigning `window.__KB_GRAPH__`, not a `.json`: browsers
block fetch() of a sibling file on file://, so a double-clicked graph.html could
never read a .json beside it. A classic <script src> loads fine.

Usage:
  python3 build_graph_data.py [--root DIR] [--out PATH] [--max-body-chars N]
                              [--max-total-mb N] [--dump-json PATH] [--check]
"""

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kblib as K  # noqa: E402

DEFAULT_MAX_BODY_CHARS = 20000

# Budgets the data file alone. Before the viewer was split out this same number
# also had to cover ~400KB of template and inlined d3; it now does not, so the
# effective body allowance is slightly larger at the same setting.
DEFAULT_MAX_TOTAL_MB = 12

D3_VERSION = "7.9.0"
# Recorded in the payload only. The viewer holds its own copy of this URL, as
# the fallback it writes out when the vendored file is not beside it.
D3_CDN = f"https://cdn.jsdelivr.net/npm/d3@{D3_VERSION}/dist/d3.min.js"

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(SKILL_DIR, "assets")
VIEWER_PATH = os.path.join(ASSETS_DIR, "graph-viewer.html")
D3_VENDORED = os.path.join(ASSETS_DIR, "vendor", "d3.v7.min.js")

TOKEN_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")
SCHEMA_RE = re.compile(r"\bSCHEMA_EXPECTED\s*=\s*(\d+)")

# Reciprocal pairs collapse into one link so lineage is not double-stroked.
RECIPROCAL = {"related-to", "see-also", "contradicts"}
SUPERSEDE_PAIR = {"supersedes", "superseded-by"}


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def node_key(path, wiki_dir):
    """Wiki-relative path minus `.md` — the graph's identity.

    Deliberately not the frontmatter `id`: paths are unique by construction
    while `id` can be duplicated or disagree with its path, both of which
    validate.py already flags. `fm_id`/`id_mismatch` carry that separately.
    """
    relpath = K.rel(path, wiki_dir).replace(os.sep, "/")
    return relpath[:-3] if relpath.endswith(".md") else relpath


def norm_source(src):
    """`raw_assets/x.docx#section` -> `raw_assets/x.docx`, quoting stripped."""
    text = str(src or "").strip().strip("`").strip()
    return text.split("#")[0].strip()


def truncate_body(body, limit):
    """Cut at a line boundary so a table or callout never ends mid-row."""
    if not limit or len(body) <= limit:
        return body, False
    cut = body[:limit]
    nl = cut.rfind("\n")
    if nl > limit * 0.5:
        cut = cut[:nl]
    return cut.rstrip() + "\n", True


# --------------------------------------------------------------------------
# payload sections
# --------------------------------------------------------------------------
def build_clusters(graph, wiki_dir):
    """One entry per cluster folder, with a stable colour index.

    `color_index` is the position in the lexicographic sort of slugs. Slugs are
    numerically prefixed and the pipeline never renumbers a cluster on update,
    so this is append-only: a 14th cluster cannot repaint the first 13. Hashing
    the slug would collide arbitrarily and reshuffle on any rename.
    """
    slugs = sorted(set(list(graph["by_cluster"].keys()) + list(graph["hubs"].keys())))
    out = []
    for i, slug in enumerate(slugs):
        hub = graph["hubs"].get(slug)
        fm = (hub or {}).get("frontmatter", {}) or {}
        members = graph["by_cluster"].get(slug, [])
        out.append({
            "slug": slug,
            "title": str(fm.get("title") or slug),
            "description": str(fm.get("description") or ""),
            "keywords": K.as_list(fm.get("keywords")),
            "node_count": sum(
                1 for n in members
                if str(n["frontmatter"].get("status") or "active") != "deprecated"),
            "total_count": len(members),
            "deprecated_count": sum(
                1 for n in members
                if str(n["frontmatter"].get("status") or "") == "deprecated"),
            "hub_key": node_key(hub["path"], wiki_dir) if hub else None,
            "has_hub": hub is not None,
            "color_index": i,
        })
    return out


def build_nodes(graph, wiki_dir, max_body_chars):
    """Every node and hub as a graph member, bodies included."""
    members = []
    for note in graph["nodes"]:
        members.append((note, "node"))
    for slug in sorted(graph["hubs"]):
        members.append((graph["hubs"][slug], "hub"))

    outbound = Counter()
    for src, _dst, _t in graph["links"]:
        outbound[src] += 1

    nodes = []
    truncated_count = 0
    for note, kind in members:
        fm = note["frontmatter"] or {}
        key = node_key(note["path"], wiki_dir)
        cluster = graph["cluster_of"].get(
            note["path"], os.path.basename(os.path.dirname(note["path"])))
        body, was_cut = truncate_body(note["body"] or "", max_body_chars)
        if was_cut:
            truncated_count += 1
        fm_id = str(fm.get("id") or "") or None
        nodes.append({
            "key": key,
            "path": K.rel(note["path"], wiki_dir).replace(os.sep, "/"),
            "kind": kind,
            "title": str(fm.get("title") or note["basename"]),
            "description": str(fm.get("description") or ""),
            "cluster": cluster,
            "status": str(fm.get("status") or "active"),
            "confidence": str(fm.get("confidence") or ""),
            "tags": K.as_list(fm.get("tags")),
            "keywords": K.as_list(fm.get("keywords")),
            "aliases": K.as_list(fm.get("aliases")),
            "sources": K.as_list(fm.get("sources")),
            "created": str(fm.get("created") or ""),
            "updated": str(fm.get("updated") or ""),
            "fm_id": fm_id,
            "id_mismatch": bool(fm_id) and fm_id != key,
            "has_frontmatter": note["has_frontmatter"],
            "in_degree": int(graph["inbound"].get(note["path"], 0)),
            "out_degree": int(outbound.get(note["path"], 0)),
            "body": body,
            "_full_body": note["body"] or "",   # scanned for conflicts, never serialised
            "body_chars": len(note["body"] or ""),
            "truncated": was_cut,
            "body_omitted": False,
            "problems": [],
            "conflicts": [],
        })
    nodes.sort(key=lambda n: n["key"])
    return nodes, truncated_count


def build_edges(graph, wiki_dir, key_of_path):
    """Typed edges, deduped, with reciprocal pairs collapsed.

    Returns (edges, asymmetries) where an asymmetry is a one-sided
    `superseded-by` — meaning the pair disagrees on disk, which is worth
    reporting rather than quietly normalising.
    """
    raw = set()
    for src, dst, etype in graph["links"]:
        a, b = key_of_path.get(src), key_of_path.get(dst)
        if a and b and a != b:
            raw.add((a, b, etype))

    handled = set()
    edges = []
    asymmetries = []

    for a, b, etype in sorted(raw):
        if (a, b, etype) in handled:
            continue
        both = False
        if etype in RECIPROCAL and (b, a, etype) in raw:
            both = True
            handled.add((b, a, etype))
        elif etype == "supersedes" and (b, a, "superseded-by") in raw:
            both = True
            handled.add((b, a, "superseded-by"))
        elif etype == "superseded-by":
            if (b, a, "supersedes") in raw:
                continue  # emitted from the `supersedes` side
            asymmetries.append((a, b))
        handled.add((a, b, etype))
        edges.append({
            "source": a,
            "target": b,
            "type": etype,
            "inferred": False,
            "cross_cluster": False,
            "both": both,
        })

    # An inline-wikilink-only link is recorded by collect_graph as related-to;
    # mark those so the viewer can separate authored edges from incidental ones.
    return edges, asymmetries


def collect_conflicts(nodes, wiki_dir):
    """Every `> [!warning] Conflict` callout, always derived from wiki/.

    Never taken from .kb/validation.json, which truncates the detail to 240
    chars and carries no source attribution — so deriving is strictly better
    and makes this panel identical with or without .kb/.
    """
    conflicts = []
    for node in nodes:
        # the full body: verbatim pages put their callouts at the end, past any truncation
        body = node.get("_full_body", node["body"]) or ""
        for m in K.CALLOUT_CONFLICT_RE.finditer(body):
            # The match ends before its own newline, so drop that first empty
            # fragment before walking the callout's continuation lines.
            tail = body[m.end():].split("\n")
            if tail and not tail[0].strip():
                tail = tail[1:]
            lines = []
            for line in tail:
                stripped = line.strip()
                if not stripped.startswith(">"):
                    break
                lines.append(stripped.lstrip(">").strip())
            detail = " ".join(l for l in lines if l).strip()
            named = [
                s for s in node["sources"]
                if any(os.path.basename(norm_source(s)).lower() in q.lower()
                       for q in re.findall(r"`([^`]+)`", detail))
            ]
            conflicts.append({
                "node": node["key"],
                "node_title": node["title"],
                "where": node["path"],
                "detail": detail,
                "sources": [norm_source(s) for s in (named or node["sources"])],
            })
    return conflicts


def collect_problems(P, nodes, edges, asymmetries, wiki_dir):
    """Validation findings, from .kb/validation.json when it exists.

    Without it, only the two families that are free from data already in hand
    are derived; the rest are named in `validation.derived` so the viewer can
    say what was not checked. The schema/cluster/router/coverage checks are
    deliberately NOT reimplemented here — that is validate.py's job and a
    second implementation would drift from it.
    """
    by_path = {n["path"]: n["key"] for n in nodes}
    by_key = {n["key"]: n["key"] for n in nodes}
    by_fm_id = {n["fm_id"]: n["key"] for n in nodes if n["fm_id"]}

    def resolve_where(where):
        text = str(where or "").strip()
        for table in (by_path, by_key, by_fm_id):
            if text in table:
                return [table[text]]
        if text.endswith(".md") and text[:-3] in by_key:
            return [text[:-3]]
        return []

    problems = []
    report = K.read_json(P["validation"], None)

    if isinstance(report, dict) and isinstance(report.get("issues"), list):
        for issue in report["issues"]:
            # A viewer cannot report on itself: the report being embedded was
            # written before this file existed, so its `viewer` findings are
            # about the previous build. Carrying them in would make a fresh page
            # claim "graph.html: missing".
            if str(issue.get("check")) == "viewer":
                continue
            problems.append({
                "level": str(issue.get("level") or "info"),
                "check": str(issue.get("check") or "other"),
                "where": str(issue.get("where") or ""),
                "issue": str(issue.get("issue") or ""),
                "hint": issue.get("hint") or None,
                "nodes": resolve_where(issue.get("where")),
            })
        validation = {
            "available": True,
            "generated": report.get("generated"),
            "by_check": report.get("by_check") or {},
            "totals": report.get("totals") or {},
            "derived": [],
            "source": ".kb/validation.json",
        }
    else:
        # No report on disk. Derive only what the wiki alone can prove.
        notes = K.load_all_notes(P["wiki"])
        resolve, _ambiguous = K.build_link_resolver(notes, [], P["wiki"])
        for node in nodes:
            for link in K.extract_wikilinks(node["body"] or ""):
                abs_from = os.path.join(P["wiki"], node["path"])
                if not resolve(link["target"], abs_from):
                    problems.append({
                        "level": "error", "check": "links", "where": node["path"],
                        "issue": f"unresolved wikilink [[{link['target']}]]",
                        "hint": None, "nodes": [node["key"]],
                    })
            if node["kind"] == "node" and node["in_degree"] == 0:
                problems.append({
                    "level": "warning", "check": "graph", "where": node["path"],
                    "issue": "orphan — no inbound link", "hint": None,
                    "nodes": [node["key"]],
                })
        validation = {
            "available": False,
            "reason": "no .kb/validation.json — run validate.py for the full report",
            "generated": None,
            "by_check": {},
            "totals": {},
            "derived": ["links", "graph"],
            "not_checked": ["schema", "clusters", "coverage", "router",
                            "viewer", "conflicts"],
            "source": None,
        }

    for a, b in asymmetries:
        problems.append({
            "level": "info", "check": "graph",
            "where": next((n["path"] for n in nodes if n["key"] == a), a),
            "issue": (f"`{a}` declares superseded-by `{b}` but `{b}` does not "
                      f"declare supersedes — the pair is asymmetric on disk"),
            "hint": "add the reciprocal edge, or drop this one",
            "nodes": [k for k in (a, b) if k in by_key],
        })

    return problems, validation


def collect_coverage(P, nodes):
    """Which source documents reached a node.

    Without .kb/manifest.json this is `available: false` with null counts, never
    zero: claiming no gaps because the evidence is missing would make this panel
    worse than not having it.
    """
    manifest = K.read_json(P["manifest"], None)
    unsupported_doc = K.read_json(P["unsupported"], None) or {}

    cited = defaultdict(list)
    for node in nodes:
        for src in node["sources"]:
            cited[norm_source(src)].append(node["key"])

    if not isinstance(manifest, dict) or not isinstance(manifest.get("documents"), list):
        return {
            "available": False,
            "reason": ("no .kb/manifest.json — coverage cannot be measured from "
                       "wiki/ alone; run extract.py"),
            "documents_total": None,
            "compiled": None,
            "uncovered": [],
            "failed": [],
            "unsupported": [],
            "cited_not_in_manifest": sorted(cited.keys()),
        }

    docs = manifest["documents"]
    known = {str(d.get("rel_path") or "") for d in docs}
    uncovered, failed = [], []
    compiled = 0
    for d in docs:
        relp = str(d.get("rel_path") or "")
        if str(d.get("status")) == "failed":
            failed.append({"rel_path": relp,
                           "error": "; ".join(K.as_list(d.get("warnings"))) or "extraction failed"})
            continue
        if cited.get(relp):
            compiled += 1
        else:
            uncovered.append({"rel_path": relp, "title": str(d.get("title") or "")})

    return {
        "available": True,
        "documents_total": len(docs),
        "compiled": compiled,
        "uncovered": uncovered,
        "failed": failed,
        "unsupported": [
            {"rel_path": str(f.get("rel_path") or f.get("path") or ""),
             "reason": str(f.get("reason") or "unsupported format")}
            for f in (unsupported_doc.get("files") or [])
        ],
        "cited_not_in_manifest": sorted(k for k in cited if k and k not in known),
    }


def collect_provenance(P, nodes, conflicts, edges):
    """Source document -> the nodes it fed, and which sources contradict.

    Uses the manifest when present; otherwise reconstructs the document set from
    node `sources:` alone and leaves every manifest-only field null. It never
    invents an extraction method.
    """
    manifest = K.read_json(P["manifest"], None)
    cited = defaultdict(list)
    for node in nodes:
        for src in node["sources"]:
            cited[norm_source(src)].append(node["key"])

    documents = []
    if isinstance(manifest, dict) and isinstance(manifest.get("documents"), list):
        derived_from = "manifest"
        for d in sorted(manifest["documents"], key=lambda x: str(x.get("rel_path"))):
            relp = str(d.get("rel_path") or "")
            documents.append({
                "rel_path": relp,
                "doc_id": d.get("doc_id"),
                "title": d.get("title") or "",
                "method": d.get("method"),
                "status": d.get("status"),
                "extracted_at": d.get("extracted_at"),
                "in_manifest": True,
                "nodes": sorted(cited.get(relp, [])),
                "node_count": len(cited.get(relp, [])),
            })
        for relp in sorted(cited):
            if relp and not any(doc["rel_path"] == relp for doc in documents):
                documents.append({
                    "rel_path": relp, "doc_id": None, "title": "",
                    "method": None, "status": "cited-not-in-manifest",
                    "extracted_at": None, "in_manifest": False,
                    "nodes": sorted(cited[relp]), "node_count": len(cited[relp]),
                })
    else:
        derived_from = "frontmatter"
        for relp in sorted(k for k in cited if k):
            documents.append({
                "rel_path": relp, "doc_id": None, "title": "",
                "method": None, "status": None, "extracted_at": None,
                "in_manifest": False,
                "nodes": sorted(cited[relp]), "node_count": len(cited[relp]),
            })

    # Sources that disagree: both sides of a conflict callout, and the source
    # sets either end of a `contradicts` edge.
    sources_of = {n["key"]: [norm_source(s) for s in n["sources"]] for n in nodes}
    pairs = {}

    def add_pair(a, b, node_keys, kind, detail=""):
        if not a or not b or a == b:
            return
        key = tuple(sorted((a, b)))
        entry = pairs.setdefault(key, {"a": key[0], "b": key[1], "via_nodes": [],
                                       "kind": kind, "detail": detail})
        for nk in node_keys:
            if nk not in entry["via_nodes"]:
                entry["via_nodes"].append(nk)

    for c in conflicts:
        srcs = [s for s in c["sources"] if s]
        for i in range(len(srcs)):
            for j in range(i + 1, len(srcs)):
                add_pair(srcs[i], srcs[j], [c["node"]], "conflict-callout", c["detail"])

    for e in edges:
        if e["type"] != "contradicts":
            continue
        for a in sources_of.get(e["source"], []):
            for b in sources_of.get(e["target"], []):
                add_pair(a, b, [e["source"], e["target"]], "contradicts-edge")

    return {
        "available": True,
        "derived_from": derived_from,
        "manifest_present": derived_from == "manifest",
        "documents": documents,
        "source_conflicts": [pairs[k] for k in sorted(pairs)],
    }


# --------------------------------------------------------------------------
# assembly
# --------------------------------------------------------------------------
def build_payload(P, wiki_dir, args):
    graph = K.collect_graph(wiki_dir)
    clusters = build_clusters(graph, wiki_dir)
    nodes, truncated_count = build_nodes(graph, wiki_dir, args.max_body_chars)

    key_of_path = {}
    for note in graph["nodes"]:
        key_of_path[note["path"]] = node_key(note["path"], wiki_dir)
    for hub in graph["hubs"].values():
        key_of_path[hub["path"]] = node_key(hub["path"], wiki_dir)

    edges, asymmetries = build_edges(graph, wiki_dir, key_of_path)

    cluster_of_key = {n["key"]: n["cluster"] for n in nodes}
    for e in edges:
        e["cross_cluster"] = (cluster_of_key.get(e["source"])
                              != cluster_of_key.get(e["target"]))

    conflicts = collect_conflicts(nodes, wiki_dir)
    problems, validation = collect_problems(P, nodes, edges, asymmetries, wiki_dir)
    coverage = collect_coverage(P, nodes)
    provenance = collect_provenance(P, nodes, conflicts, edges)
    for n in nodes:
        n.pop("_full_body", None)

    index_of = {n["key"]: i for i, n in enumerate(nodes)}
    for pi, prob in enumerate(problems):
        for nk in prob["nodes"]:
            if nk in index_of:
                nodes[index_of[nk]]["problems"].append(pi)
    for ci, conf in enumerate(conflicts):
        if conf["node"] in index_of:
            nodes[index_of[conf["node"]]]["conflicts"].append(ci)

    levels = Counter(p["level"] for p in problems)
    router_index = K.read_json(os.path.join(P["router"], "index.json"), None) or {}

    payload = {
        "schema": K.GRAPH_SCHEMA,
        "generated": K.now_iso(),
        "content_hash": router_index.get("content_hash"),
        "d3": {"mode": None, "version": D3_VERSION, "url": D3_CDN},
        "truncation": {
            "bodies_truncated": truncated_count,
            "bodies_omitted": 0,
            "max_body_chars": args.max_body_chars,
        },
        "totals": {
            "nodes": sum(1 for n in nodes if n["kind"] == "node"),
            "hubs": sum(1 for n in nodes if n["kind"] == "hub"),
            "clusters": len(clusters),
            "edges": len(edges),
            "errors": levels.get("error", 0),
            "warnings": levels.get("warning", 0),
            "infos": levels.get("info", 0),
            "open_conflicts": len(conflicts),
            "deprecated": sum(1 for n in nodes if n["status"] == "deprecated"),
            "documents": coverage.get("documents_total"),
            "documents_covered": coverage.get("compiled"),
        },
        "clusters": clusters,
        "nodes": nodes,
        "edges": edges,
        "problems": problems,
        "validation": validation,
        "coverage": coverage,
        "provenance": provenance,
        "conflicts": conflicts,
        "edge_types": K.EDGE_TYPES,
        "edge_colors": K.EDGE_COLORS,
        "cluster_palette": K.CLUSTER_PALETTE,
    }
    return payload


def encode_payload(payload):
    """JSON safe to sit inside a <script> element.

    Escaping `<`, `>` and `&` is not optional: a node body containing
    `</script>` or `<!--` would otherwise terminate the element and leave a
    blank page that passes a casual eyeball. JSON.parse reads the escapes back
    transparently. U+2028/9 are escaped for older parsers.
    """
    text = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return (text.replace("<", "\\u003c").replace(">", "\\u003e")
                .replace("&", "\\u0026")
                .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))


def apply_size_budget(payload, max_total_mb, out_size_hint):
    """Drop bodies from the least-connected nodes until the file fits.

    1000 nodes x 5KB is a browser-hostile file; degrading visibly beats emitting
    it. The page states what was dropped so nothing is silently missing.
    """
    if not max_total_mb:
        return 0
    budget = int(max_total_mb * 1024 * 1024) - out_size_hint
    if budget <= 0:
        budget = 1
    if len(encode_payload(payload).encode("utf-8")) <= budget:
        return 0

    order = sorted(
        (n for n in payload["nodes"] if n["body"]),
        key=lambda n: (n["in_degree"] + n["out_degree"], -len(n["body"] or "")),
    )
    dropped = 0
    for node in order:
        node["body"] = None
        node["body_omitted"] = True
        dropped += 1
        if len(encode_payload(payload).encode("utf-8")) <= budget:
            break
    payload["truncation"]["bodies_omitted"] = dropped
    return dropped


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def check_viewer_asset():
    """Guard the two contracts a hand-maintained viewer can silently break.

    `assets/graph-viewer.html` has no build step, so nothing else would notice
    either of these — and both fail as a blank or wrongly-worded page in someone
    else's browser rather than as an error here.

    1. A leftover `{{TOKEN}}` from the template it used to be. `render()` used to
       make that a hard error; copying the file verbatim would ship it.
    2. `SCHEMA_EXPECTED` drifting from `kblib.GRAPH_SCHEMA`. The whole point of
       that constant is to detect a payload the viewer cannot read, which it
       cannot do if it disagrees with the writer.

    Returns a list of problem strings; empty means the asset is sound.
    """
    problems = []
    if not os.path.exists(VIEWER_PATH):
        return [f"missing viewer asset {K.rel(VIEWER_PATH, SKILL_DIR)}"]
    with open(VIEWER_PATH, "r", encoding="utf-8") as fh:
        text = fh.read()
    leftovers = sorted(set(TOKEN_RE.findall(text)))
    if leftovers:
        problems.append(
            "graph-viewer.html still has template token(s): "
            + ", ".join("{{" + t + "}}" for t in leftovers))
    match = SCHEMA_RE.search(text)
    if not match:
        problems.append("graph-viewer.html declares no SCHEMA_EXPECTED")
    elif int(match.group(1)) != K.GRAPH_SCHEMA:
        problems.append(
            f"graph-viewer.html expects payload schema {match.group(1)}, "
            f"this script writes {K.GRAPH_SCHEMA}")
    return problems


def do_check(path):
    payload = K.read_data_payload(path)
    if payload is None:
        K.eprint(f"error: no parseable {K.GRAPH_GLOBAL} payload in {path}")
        return 1
    t = payload.get("totals") or {}
    print(f"{path}: schema {payload.get('schema')}, generated {payload.get('generated')}")
    print(f"  nodes {t.get('nodes')}  hubs {t.get('hubs')}  clusters {t.get('clusters')}  "
          f"edges {t.get('edges')}")
    print(f"  errors {t.get('errors')}  warnings {t.get('warnings')}  "
          f"open conflicts {t.get('open_conflicts')}")
    print(f"  d3: {(payload.get('d3') or {}).get('mode')}")
    return 0


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root")
    ap.add_argument("--out", help="default: wiki/_meta/graph-data.js")
    ap.add_argument("--max-body-chars", type=int, default=DEFAULT_MAX_BODY_CHARS,
                    help="per-node body cap, 0 for unlimited "
                         f"(default {DEFAULT_MAX_BODY_CHARS})")
    ap.add_argument("--max-total-mb", type=float, default=DEFAULT_MAX_TOTAL_MB,
                    help=f"data file budget (default {DEFAULT_MAX_TOTAL_MB})")
    ap.add_argument("--dump-json", help="write the payload alone and exit")
    ap.add_argument("--check", action="store_true",
                    help="inspect an existing graph-data.js instead of building one")
    args = ap.parse_args()

    root = K.project_root(args.root)
    P = K.paths(root)
    out_path = args.out or P["graph_data"]

    if args.check:
        return do_check(out_path)

    if not os.path.isdir(P["wiki"]):
        raise SystemExit(f"error: no wiki at {P['wiki']} — nothing to visualise")

    for problem in check_viewer_asset():
        raise SystemExit(f"error: {problem}")

    payload = build_payload(P, P["wiki"], args)

    # Recorded for the viewer and for validate.py, and derived from what is
    # actually on disk in the vault — not from a decision this script makes.
    # The copy step places d3; asserting a mode we no longer choose would be a
    # claim that can quietly disagree with reality.
    payload["d3"]["mode"] = (
        "vendored" if os.path.exists(os.path.join(P["wiki_vendor"], "d3.v7.min.js"))
        else "cdn-fallback")

    # Applied before --dump-json too, so a dumped payload is exactly what would
    # have been written rather than a rosier version of it.
    dropped = apply_size_budget(payload, args.max_total_mb, 0)
    if dropped:
        K.eprint(f"warning: dropped {dropped} node bodies to fit "
                 f"--max-total-mb {args.max_total_mb}")

    if args.dump_json:
        K.write_json(args.dump_json, payload)
        t = payload["totals"]
        print(f"payload: {t['nodes']} nodes, {t['clusters']} clusters, "
              f"{t['edges']} edges, {t['open_conflicts']} open conflicts")
        print(f"written to {args.dump_json}")
        return 0

    data = K.encode_data_file(K.GRAPH_GLOBAL, encode_payload(payload))

    K.ensure_dir(os.path.dirname(out_path))
    tmp = out_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(data)
    os.replace(tmp, out_path)

    size_mb = os.path.getsize(out_path) / (1024 * 1024)
    t = payload["totals"]
    print(f"{K.rel(out_path, root)}: {t['nodes']} nodes + {t['hubs']} hubs in "
          f"{t['clusters']} clusters, {t['edges']} edges")
    print(f"  problems carried: {t['errors']} errors, {t['warnings']} warnings, "
          f"{t['open_conflicts']} open conflicts")
    print(f"  d3: {payload['d3']['mode']}  size: {size_mb:.2f} MB"
          + (f"  bodies truncated: {payload['truncation']['bodies_truncated']}"
             if payload["truncation"]["bodies_truncated"] else "")
          + (f"  bodies omitted: {dropped}" if dropped else ""))
    if not payload["coverage"]["available"]:
        print("  coverage: unavailable (no .kb/manifest.json)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
