#!/usr/bin/env python3
"""Generate wiki/_meta/chat-data.js — the corpus wiki/chat.html answers from.

The page itself is not generated: `wiki/chat.html` is a verbatim copy of
`assets/chat-viewer.html`, installed by init_wiki.py along with `chat-app.js`
and the vendored SDK. This script writes only the data they load, so a corpus
that reaches tens of MB stops being rewritten into a fresh HTML file every
compile.

It exists because the router has no scorer. How many clusters layer 1 keeps, how
many nodes layer 2 keeps, the confidence floors and the model per layer are all
tunable in the page, and every answer shows the route it took.

  payload     router index + full node bodies (never fetched — see below)
  defaults    seeded from this vault's actual shape (clusters, nodes per cluster)
  degrades    a missing router index is an error; a missing vault writes nothing

Unlike the graph payload this never truncates node bodies: a node with no body
cannot be answered from, so --max-total-mb warns rather than drops.

The output is a `.js` assigning `window.__KB_CHAT__`, not a `.json`: browsers
block fetch() of a sibling file on file://, so a double-clicked chat.html could
never read a .json beside it. A classic <script src> loads fine.

Usage:
  python3 build_chat_data.py [--root DIR] [--vault DIR] [--out PATH]
                             [--max-total-mb N] [--title TEXT]
                             [--dump-json PATH] [--check]
"""

import argparse
import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kblib as K  # noqa: E402

DEFAULT_MAX_TOTAL_MB = 40

SDK_VERSION = "0.124.0"

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(SKILL_DIR, "assets")
VIEWER_PATH = os.path.join(ASSETS_DIR, "chat-viewer.html")
APP_PATH = os.path.join(ASSETS_DIR, "chat-app.js")

TOKEN_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


# --------------------------------------------------------------------------
# payload
# --------------------------------------------------------------------------
def load_router(router_dir):
    """(categories, layer2_by_slug). Missing or unreadable is a hard error."""
    cats_path = os.path.join(router_dir, "categories.json")
    if not os.path.exists(cats_path):
        raise SystemExit(
            "error: no router index at %s — run build_router_index.py first"
            % K.rel(router_dir, os.path.dirname(os.path.dirname(router_dir)))
        )
    cats_doc = K.read_json(cats_path, default={}) or {}
    categories = cats_doc.get("categories") or []

    layer2 = {}
    for cat in categories:
        slug = cat.get("slug")
        name = os.path.basename(cat.get("index_path") or ("%s.json" % slug))
        doc = K.read_json(os.path.join(router_dir, name), default=None)
        if doc is None:
            K.eprint("warning: layer-2 index missing for cluster %s" % slug)
            layer2[slug] = []
            continue
        layer2[slug] = doc.get("nodes") or []
    return categories, layer2


def strip_frontmatter(text):
    _fm, _raw, body = K.split_frontmatter(text)
    return (body or "").strip()


def load_bodies(wiki_dir):
    """{relpath: body} for every node on disk, frontmatter removed."""
    nodes, _hubs = K.scan_vault(wiki_dir)
    bodies = {}
    for note in nodes:
        bodies[note["rel"].replace(os.sep, "/")] = strip_frontmatter(note["text"])
    return bodies


def seed_defaults(categories, layer2):
    """Sizing that suits this vault, so a fresh page opens sensibly.

    Layer 1 keeps at least 2 wherever there is more than one category to choose
    between: a layer-1 miss is the expensive failure — layer 2 never sees the
    right cluster — so runners-up are worth their tokens.
    """
    counts = sorted(len(layer2.get(c.get("slug"), [])) for c in categories)
    median = counts[len(counts) // 2] if counts else 0
    total = len(categories)
    l1_keep = min(3, max(2, int(math.ceil(total / 4.0))), total) if total else 1
    l2_keep = max(1, min(5, median)) if median else 3
    return {"layer1_keep": l1_keep, "layer2_keep": l2_keep}


def build_payload(root, wiki_dir, title):
    router_dir = os.path.join(wiki_dir, K.META_DIR, "router")
    categories, layer2 = load_router(router_dir)
    bodies = load_bodies(wiki_dir)
    index_doc = K.read_json(os.path.join(router_dir, "index.json"), default={}) or {}

    nodes = []
    missing_body = []
    for cat in categories:
        for entry in layer2.get(cat.get("slug"), []):
            path = entry.get("path") or ""
            body = bodies.get(path)
            if body is None:
                missing_body.append(path)
                body = ""
            nodes.append({
                "id": entry.get("id"),
                "title": entry.get("title"),
                "description": entry.get("description") or "",
                "keywords": entry.get("keywords") or [],
                "aliases": entry.get("aliases") or [],
                "tags": entry.get("tags") or [],
                "path": path,
                "cluster": entry.get("cluster"),
                "status": entry.get("status") or "active",
                # The compiler's confidence in the CONTENT — never the router's
                # confidence in a match. Named apart so the UI cannot conflate them.
                "content_confidence": entry.get("confidence") or "unknown",
                "sources": entry.get("sources") or [],
                "updated": entry.get("updated") or "",
                "embedding_text": entry.get("embedding_text") or "",
                "body": body,
                "has_conflict": bool(K.CALLOUT_CONFLICT_RE.search(body)),
            })

    for path in missing_body:
        K.eprint("warning: no body on disk for %s — it will not be answerable" % path)

    deprecated = sum(1 for n in nodes if n["status"] == "deprecated")
    payload = {
        "schema": 1,
        "generated": K.now_iso(),
        "vault": K.rel(wiki_dir, root),
        "title": title,
        "content_hash": index_doc.get("content_hash") or "",
        "totals": {
            "clusters": len(categories),
            "nodes": len(nodes),
            "deprecated_nodes": deprecated,
            "conflicts": sum(1 for n in nodes if n["has_conflict"]),
            "missing_bodies": len(missing_body),
        },
        "categories": categories,
        "nodes": nodes,
        "defaults": seed_defaults(categories, layer2),
    }
    return payload


def encode_payload(payload):
    """JSON that is inert wherever it lands.

    The escaping of `<`, `>` and `&` predates the data file and is kept: they
    are ordinary JSON escape sequences that JSON.parse reads back transparently,
    and they mean a node body containing `</script>` stays harmless if this
    payload is ever embedded in a page again rather than loaded as a sibling.
    U+2028/9 are escaped for older parsers.
    """
    text = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return (text.replace("<", "\\u003c").replace(">", "\\u003e")
                .replace("&", "\\u0026")
                .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))


def report_size(payload, size_bytes, max_total_mb):
    """Warn on a browser-hostile file, but never drop bodies to hit a budget."""
    size_mb = size_bytes / (1024.0 * 1024.0)
    if not max_total_mb or size_mb <= max_total_mb:
        return
    by_cluster = {}
    for node in payload["nodes"]:
        by_cluster[node["cluster"]] = by_cluster.get(node["cluster"], 0) + len(node["body"])
    worst = sorted(by_cluster.items(), key=lambda kv: -kv[1])[:3]
    K.eprint("warning: chat-data.js is %.1f MB, over the %.0f MB guide — browsers "
             "will be slow to open chat.html" % (size_mb, max_total_mb))
    for slug, chars in worst:
        K.eprint("  %-38s %.1f MB of node bodies" % (slug, chars / (1024.0 * 1024.0)))
    K.eprint("  bodies are never dropped: a node with no body cannot be answered from")


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def check_viewer_asset():
    """Guard the contract a hand-maintained viewer can silently break.

    `assets/chat-viewer.html` has no build step, so a `{{TOKEN}}` left over from
    the template it used to be would be copied into every vault with no error —
    `render()` used to make exactly that a hard failure.
    """
    problems = []
    for path in (VIEWER_PATH, APP_PATH):
        if not os.path.exists(path):
            problems.append("missing asset %s" % K.rel(path, SKILL_DIR))
            continue
        with open(path, "r", encoding="utf-8") as fh:
            leftovers = sorted(set(TOKEN_RE.findall(fh.read())))
        if leftovers:
            problems.append("%s still has template token(s): %s"
                            % (os.path.basename(path),
                               ", ".join("{{%s}}" % t for t in leftovers)))
    return problems


def describe(path):
    payload = K.read_data_payload(path)
    if payload is None:
        K.eprint("error: no parseable %s payload in %s" % (K.CHAT_GLOBAL, path))
        return 1
    totals = payload.get("totals") or {}
    print("%s: schema %s, generated %s" % (path, payload.get("schema"),
                                           payload.get("generated")))
    print("  clusters %s  nodes %s  deprecated %s  conflicts %s"
          % (totals.get("clusters"), totals.get("nodes"),
             totals.get("deprecated_nodes"), totals.get("conflicts")))
    print("  content_hash %s" % (payload.get("content_hash") or "(none)"))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root")
    ap.add_argument("--vault", help="default: <root>/wiki")
    ap.add_argument("--out", help="default: <vault>/_meta/chat-data.js")
    ap.add_argument("--max-total-mb", type=float, default=DEFAULT_MAX_TOTAL_MB,
                    help="warn above this size (bodies are never dropped)")
    ap.add_argument("--title")
    ap.add_argument("--dump-json", help="write the payload alone and exit")
    ap.add_argument("--check", action="store_true",
                    help="describe an existing chat-data.js instead of building one")
    args = ap.parse_args()

    root = K.project_root(args.root)
    wiki_dir = os.path.abspath(args.vault) if args.vault else K.paths(root)["wiki"]
    out_path = args.out or os.path.join(wiki_dir, K.META_DIR, K.CHAT_DATA)

    if args.check:
        return describe(out_path)

    if not os.path.isdir(wiki_dir):
        K.eprint("no vault at %s — nothing to build" % K.rel(wiki_dir, root))
        return 0

    title = args.title or "Knowledge Base — Router Playground"
    payload = build_payload(root, wiki_dir, title)

    if args.dump_json:
        K.write_json(args.dump_json, payload)
        t = payload["totals"]
        print("payload: %s nodes, %s clusters" % (t["nodes"], t["clusters"]))
        print("written to %s" % args.dump_json)
        return 0

    for problem in check_viewer_asset():
        raise SystemExit("error: %s" % problem)

    data = K.encode_data_file(K.CHAT_GLOBAL, encode_payload(payload)).encode("utf-8")
    K.ensure_dir(os.path.dirname(out_path))
    tmp = out_path + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(data)
    os.replace(tmp, out_path)

    t = payload["totals"]
    size_mb = len(data) / (1024.0 * 1024.0)
    print("%s: %s nodes in %s clusters" % (K.rel(out_path, root), t["nodes"], t["clusters"]))
    print("  deprecated %s  conflicts %s  missing bodies %s"
          % (t["deprecated_nodes"], t["conflicts"], t["missing_bodies"]))
    print("  size: %.2f MB  defaults: L1 keep %s, L2 keep %s"
          % (size_mb, payload["defaults"]["layer1_keep"],
             payload["defaults"]["layer2_keep"]))
    report_size(payload, len(data), args.max_total_mb)
    return 0


if __name__ == "__main__":
    sys.exit(main())
