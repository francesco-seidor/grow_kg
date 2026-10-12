#!/usr/bin/env python3
"""Export the compiled wiki as a Claude Project — instructions + knowledge bundles.

A Claude Project has two halves: an instructions field, and a pile of uploaded
files. Uploading `wiki/` raw throws away everything the compile produced — the
taxonomy, the router descriptions, the typed edges, the conflict flags. This
projects the vault into that shape instead:

  project-instructions.md   paste into the Project's Instructions field:
                            the two-layer index plus the routing and grounding
                            protocol, so the Project routes deliberately
  knowledge/<cluster>.md    one bundle per cluster, every node under a
                            `## <node-id>` anchor the instructions can name
  knowledge/00-INDEX.md     the complete index, always at full fidelity

Wikilinks are rewritten to node ids and `## Connections` to `type :: id`, so the
graph stays traversable in a place where `[[sick-leave]]` means nothing.

The output lives OUTSIDE `wiki/`. Anything `.md` under the vault (except
`_meta/`) is scanned as a node by kblib.iter_wiki_files, so exporting into it
would break validate.py and the router index.

Usage:
  python3 build_project_export.py [--root DIR] [--vault DIR] [--out DIR]
                                  [--max-chars N] [--tier full|standard|clusters]
                                  [--max-bundle-kb N] [--intro PATH]
                                  [--title TEXT] [--check]
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kblib as K  # noqa: E402

EXPORT_DIRNAME = os.path.join("exports", "claude-project")
KNOWLEDGE_DIRNAME = "knowledge"
INSTRUCTIONS_NAME = "project-instructions.md"
MANIFEST_NAME = "manifest.json"
INDEX_NAME = "00-INDEX.md"
CONFLICTS_NAME = "00-CONFLICTS.md"

# A conservative budget for the Project instructions field, not a claimed
# platform limit — raise or lower it with --max-chars.
DEFAULT_MAX_CHARS = 30000
DEFAULT_MAX_BUNDLE_KB = 512

TIERS = ["full", "standard", "clusters"]


# --------------------------------------------------------------------------
# loading
# --------------------------------------------------------------------------
def load_router(router_dir):
    """(categories, layer2_by_slug, manifest). Missing index is a hard error."""
    cats_path = os.path.join(router_dir, "categories.json")
    if not os.path.exists(cats_path):
        raise SystemExit(
            "error: no router index at %s — run build_router_index.py first"
            % router_dir
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

    manifest = K.read_json(os.path.join(router_dir, "index.json"), default={}) or {}
    return categories, layer2, manifest


def load_bodies(wiki_dir):
    """{relpath: body} for every node on disk, frontmatter removed."""
    nodes, _hubs = K.scan_vault(wiki_dir)
    bodies = {}
    for note in nodes:
        _fm, _raw, body = K.split_frontmatter(note["text"])
        bodies[note["rel"].replace(os.sep, "/")] = (body or "").strip()
    return bodies


def vault_title(wiki_dir, explicit=None):
    if explicit:
        return explicit
    index_path = os.path.join(wiki_dir, "index.md")
    if os.path.exists(index_path):
        fm = K.load_note(index_path)["frontmatter"]
        title = str(fm.get("title") or "").strip()
        if title:
            return title
    return "Knowledge Base"


def build_id_map(wiki_dir, categories):
    """abs path -> ("node", id, title) or ("cluster", slug, title).

    Wikilinks resolve to paths; the Project only understands node ids, so every
    resolvable target needs a name that appears verbatim in the index.
    """
    id_of = {}
    nodes, hubs = K.scan_vault(wiki_dir)
    for note in nodes:
        fm = note["frontmatter"]
        slug = str(fm.get("cluster") or os.path.basename(os.path.dirname(note["path"])))
        node_id = str(fm.get("id") or "%s/%s" % (slug, note["basename"]))
        id_of[note["path"]] = ("node", node_id, str(fm.get("title") or note["basename"]))
    titles = {c.get("slug"): c.get("title") or c.get("slug") for c in categories}
    for hub in hubs:
        fm = hub["frontmatter"]
        slug = str(fm.get("cluster") or os.path.basename(os.path.dirname(hub["path"])))
        id_of[hub["path"]] = ("cluster", slug, str(fm.get("title") or titles.get(slug) or slug))
    return id_of


# --------------------------------------------------------------------------
# body transforms
# --------------------------------------------------------------------------
FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADING_RE = re.compile(r"^(#{1,6})(\s+)(.*)$")
EDGE_LINE_RE = re.compile(r"^(\s*)[-*]\s*([a-z][a-z-]*)\s*::\s*(.+?)\s*$")
CONNECTIONS_RE = re.compile(
    r"^(##\s+Connections\s*$)(.*?)(?=^##\s+|\Z)", re.MULTILINE | re.DOTALL
)


def iter_lines_outside_fences(text):
    """Yield (line, in_fence). Headings inside code fences must not be touched."""
    fence = None
    for line in text.split("\n"):
        match = FENCE_RE.match(line)
        if match:
            token = match.group(1)
            if fence is None:
                fence = token
            elif line.strip().startswith(fence):
                fence = None
            yield line, True
            continue
        yield line, fence is not None


def strip_leading_h1(body):
    """Drop the body's own `# Title` — the bundle's `## <id>` anchor replaces it."""
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        if re.match(r"^#\s+", line):
            return "\n".join(lines[i + 1:]).lstrip("\n")
        return body
    return body


def demote_headings(body, by=1):
    out = []
    for line, in_fence in iter_lines_outside_fences(body):
        match = HEADING_RE.match(line) if not in_fence else None
        if match:
            level = min(6, len(match.group(1)) + by)
            out.append("#" * level + match.group(2) + match.group(3))
        else:
            out.append(line)
    return "\n".join(out)


def name_target(target, from_path, resolve, id_of, unresolved):
    """(display_name, id_or_None) for one wikilink target."""
    dest = resolve(target, from_path)
    if dest and dest in id_of:
        kind, ident, title = id_of[dest]
        return title, ident, kind
    unresolved.append(target)
    return target, None, None


def rewrite_connections(body, from_path, resolve, id_of, unresolved):
    """`- part-of :: [[_cluster]]` -> `- part-of :: `01-x` (Leave and Absence)`.

    This is the graph, made followable: the Project reads a node id it can find
    in the index and in a bundle heading, instead of an Obsidian link.
    """
    def repl(match):
        head, section = match.group(1), match.group(2)
        lines = []
        for line in section.split("\n"):
            edge = EDGE_LINE_RE.match(line)
            if not edge:
                lines.append(line)
                continue
            indent, etype = edge.group(1), edge.group(2)
            targets = K.extract_wikilinks(edge.group(3))
            if not targets:
                lines.append(line)
                continue
            for link in targets:
                title, ident, kind = name_target(
                    link["target"], from_path, resolve, id_of, unresolved
                )
                if ident and kind == "cluster":
                    lines.append("%s- %s :: cluster `%s` (%s)" % (indent, etype, ident, title))
                elif ident:
                    lines.append("%s- %s :: `%s` (%s)" % (indent, etype, ident, title))
                else:
                    lines.append("%s- %s :: %s (unresolved)" % (indent, etype, title))
        return head + "\n".join(lines)

    return CONNECTIONS_RE.sub(repl, body)


def rewrite_wikilinks(body, from_path, resolve, id_of, unresolved):
    """Inline `[[target|Alias]]` -> ``Alias (node `id`)``."""
    def repl(match):
        target = (match.group(1) or "").strip()
        alias = (match.group(3) or "").strip()
        title, ident, kind = name_target(target, from_path, resolve, id_of, unresolved)
        label = alias or title
        if not ident:
            return label
        if kind == "cluster":
            return "%s (cluster `%s`)" % (label, ident)
        return "%s (node `%s`)" % (label, ident)

    return K.WIKILINK_RE.sub(repl, body)


def transform_body(body, node_path, resolve, id_of, unresolved):
    body = strip_leading_h1(body)
    body = rewrite_connections(body, node_path, resolve, id_of, unresolved)
    body = rewrite_wikilinks(body, node_path, resolve, id_of, unresolved)
    return demote_headings(body).strip()


# --------------------------------------------------------------------------
# rendering
# --------------------------------------------------------------------------
def cell(text):
    return str(text or "").replace("|", "\\|").replace("\n", " ").strip()


def superseded_by(body):
    """The `superseded-by` target named in a node's Connections, if any."""
    for edge in K.extract_edges(body):
        if edge["type"] == "superseded-by":
            return edge["target"]
    return None


def render_node_section(entry, raw_body, wiki_dir, resolve, id_of, unresolved):
    """One node as a bundle section, anchored at `## <node-id>`."""
    node_id = entry.get("id") or entry.get("path", "")
    node_path = os.path.join(wiki_dir, (entry.get("path") or "").replace("/", os.sep))
    deprecated = (entry.get("status") or "active") == "deprecated"

    lines = ["## %s" % node_id, "", "**%s**" % (entry.get("title") or node_id), ""]

    if deprecated:
        target = superseded_by(raw_body)
        successor = ""
        if target:
            title, ident, _kind = name_target(target, node_path, resolve, id_of, unresolved)
            successor = " Superseded by `%s` (%s)." % (ident, title) if ident else \
                        " Superseded by %s." % title
        lines += [
            "> [!warning] DEPRECATED — do not answer current questions from this node.%s"
            % successor,
            "",
        ]

    meta = [
        "- **Node id**: `%s`" % node_id,
        "- **Cluster**: `%s`" % (entry.get("cluster") or ""),
        "- **Answers**: %s" % (entry.get("description") or ""),
        "- **Status**: %s" % ("DEPRECATED" if deprecated else "active"),
        "- **Source confidence**: %s" % (entry.get("confidence") or "unknown"),
    ]
    if entry.get("keywords") or entry.get("aliases"):
        terms = list(dict.fromkeys(list(entry.get("keywords") or []) + list(entry.get("aliases") or [])))
        meta.append("- **Also called**: %s" % ", ".join(terms))
    if entry.get("updated"):
        meta.append("- **Last updated**: %s" % entry["updated"])
    if entry.get("sources"):
        meta.append("- **Sources**: %s" % ", ".join("`%s`" % s for s in entry["sources"]))
    lines += meta + [""]

    body = transform_body(raw_body, node_path, resolve, id_of, unresolved)
    lines += [body or "*This node has no body on disk — it cannot be answered from.*", ""]
    return "\n".join(lines)


def render_cluster_header(cat, entries, filename, part, parts_total):
    title = cat.get("title") or cat.get("slug")
    lines = [
        "# %s" % title,
        "",
        "Cluster `%s`%s" % (
            cat.get("slug"),
            "" if parts_total == 1 else " — part %d of %d" % (part, parts_total),
        ),
        "",
        "%s" % (cat.get("description") or ""),
        "",
    ]
    if cat.get("keywords"):
        lines += ["Keywords: %s" % ", ".join(cat["keywords"]), ""]
    lines += [
        "Nodes in this file — find one by its `## <node-id>` heading:",
        "",
        "| Node id | Answers questions about |",
        "| --- | --- |",
    ]
    for entry in entries:
        flag = " **[DEPRECATED]**" if (entry.get("status") or "active") == "deprecated" else ""
        lines.append("| `%s`%s | %s |" % (cell(entry.get("id")), flag, cell(entry.get("description"))))
    lines += ["", "---", "", ""]
    return "\n".join(lines)


def pack_bundles(categories, layer2, sections, max_bundle_bytes):
    """[(filename, text, [entries])] — one file per cluster, split on overflow.

    Splitting happens at node boundaries only: a node must never be cut in half,
    because a half node is a node that can be answered from wrongly.
    """
    bundles = []
    for cat in categories:
        slug = cat.get("slug")
        entries = layer2.get(slug) or []
        if not entries:
            continue
        groups, current, size = [], [], 0
        for entry in entries:
            chunk = sections[entry["id"]]
            chunk_bytes = len(chunk.encode("utf-8"))
            if current and size + chunk_bytes > max_bundle_bytes:
                groups.append(current)
                current, size = [], 0
            current.append(entry)
            size += chunk_bytes
        if current:
            groups.append(current)

        for i, group in enumerate(groups, start=1):
            name = "%s.md" % slug if len(groups) == 1 else "%s-%d.md" % (slug, i)
            text = render_cluster_header(cat, group, name, i, len(groups))
            text += "\n\n---\n\n".join(sections[e["id"]] for e in group)
            bundles.append((name, text.rstrip() + "\n", group))
    return bundles


def render_index(title, categories, layer2, file_of, generated, content_hash, totals):
    """The complete two-layer index — never tiered, never truncated."""
    lines = [
        "# %s — complete index" % title,
        "",
        "Every category and every node in this knowledge base, with the file each",
        "node lives in. Use this to find the right node, then open that file and",
        "search for the node's `## <node-id>` heading.",
        "",
        "%d categories · %d nodes (%d deprecated) · generated %s · content hash `%s`"
        % (totals["clusters"], totals["nodes"], totals["deprecated_nodes"],
           generated, content_hash or "unknown"),
        "",
        "## Layer 1 — categories",
        "",
        "| Category | Cluster | File | Nodes | Answers questions about |",
        "| --- | --- | --- | --- | --- |",
    ]
    for cat in categories:
        slug = cat.get("slug")
        entries = layer2.get(slug) or []
        files = list(dict.fromkeys(file_of.get(e["id"], "") for e in entries))
        lines.append("| %s | `%s` | %s | %d | %s |" % (
            cell(cat.get("title")), cell(slug),
            ", ".join("`%s`" % f for f in files) or "—",
            len(entries), cell(cat.get("description")),
        ))

    lines += ["", "## Layer 2 — nodes by category", ""]
    for cat in categories:
        slug = cat.get("slug")
        entries = layer2.get(slug) or []
        lines += ["### %s (`%s`)" % (cat.get("title") or slug, slug), ""]
        if not entries:
            lines += ["*No nodes.*", ""]
            continue
        lines += ["| Node id | File | Answers questions about | Also called |",
                  "| --- | --- | --- | --- |"]
        for entry in entries:
            flag = " **[DEPRECATED]**" if (entry.get("status") or "active") == "deprecated" else ""
            terms = list(dict.fromkeys(
                list(entry.get("keywords") or []) + list(entry.get("aliases") or [])
            ))
            lines.append("| `%s`%s | `%s` | %s | %s |" % (
                cell(entry.get("id")), flag, cell(file_of.get(entry["id"], "")),
                cell(entry.get("description")), cell(", ".join(terms)),
            ))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_instructions(title, categories, layer2, file_of, tier, intro,
                        generated, content_hash, totals, has_conflicts):
    """The Project instructions: scope, routing protocol, index, answer rules."""
    cluster_lines = []
    for cat in categories:
        cluster_lines.append("- **%s** — %s" % (
            cat.get("title") or cat.get("slug"), cat.get("description") or ""
        ))

    lines = [
        "# %s" % title,
        "",
        "You answer questions from a compiled knowledge base. It was built by",
        "synthesising a corpus of source documents into self-contained nodes,",
        "grouped into categories and joined by typed links. Every node is uploaded",
        "to this project's knowledge, bundled one file per category.",
        "",
        "## The contract",
        "",
        "- Answer **only** from the uploaded knowledge files. They are the whole",
        "  world. Never fill a gap with general knowledge, and never guess.",
        "- **Never state a number, date, threshold, entitlement, price, version or",
        "  name that does not appear verbatim in a node.** If a specific is not in",
        "  the node, say it is not recorded.",
        "- Always cite the node id you answered from, and its `Sources` line so the",
        "  reader can trace the claim back to the original document.",
        "- If the knowledge base does not cover the question, say so plainly and",
        "  name the closest nodes. A wrong answer is far worse than a gap.",
        "",
        "## What this knowledge base covers",
        "",
    ]
    if intro:
        lines += [intro.strip(), ""]
    lines += cluster_lines
    lines += [
        "",
        "Anything outside these areas is not covered — say so rather than",
        "answering from general knowledge.",
        "",
        "## How to find the answer — do this every time",
        "",
        "1. **Pick the category.** Match the question against the category table",
        "   below. Keep the runner-up: picking the wrong category is the expensive",
        "   mistake, because you then never see the right node.",
    ]
    if tier == "clusters":
        lines += [
            "2. **Pick the node.** Open `%s` in the project knowledge and use its"
            % INDEX_NAME,
            "   layer-2 tables to choose the node(s) whose description matches. The",
            "   full node list is there, not in these instructions — read it before",
            "   answering anything.",
        ]
    else:
        lines += [
            "2. **Pick the node.** Match the question against that category's node",
            "   list below. `%s` in the project knowledge carries the same" % INDEX_NAME,
            "   index with extra search terms if the descriptions here are not enough.",
        ]
    lines += [
        "3. **Read the node.** Open the category's file and find the `## <node-id>`",
        "   heading. Each node is self-contained — it is written to be answered from",
        "   without any other document.",
        "4. **Follow the links.** A node's `Connections` list names related node ids",
        "   (`depends-on`, `part-of`, `see-also`, `contradicts`, …). When the answer",
        "   depends on another node, follow the id rather than searching again.",
        "5. **Show the route.** State which category and node(s) you used.",
        "",
        "## Layer 1 — categories",
        "",
        "| Category | Cluster id | File | Nodes | Answers questions about |",
        "| --- | --- | --- | --- | --- |",
    ]
    for cat in categories:
        slug = cat.get("slug")
        entries = layer2.get(slug) or []
        files = list(dict.fromkeys(file_of.get(e["id"], "") for e in entries))
        lines.append("| %s | `%s` | %s | %d | %s |" % (
            cell(cat.get("title")), cell(slug),
            ", ".join("`%s`" % f for f in files) or "—",
            len(entries), cell(cat.get("description")),
        ))

    if tier != "clusters":
        lines += ["", "## Layer 2 — nodes", ""]
        for cat in categories:
            slug = cat.get("slug")
            entries = layer2.get(slug) or []
            if not entries:
                continue
            files = list(dict.fromkeys(file_of.get(e["id"], "") for e in entries))
            lines += ["### %s — %s" % (
                cat.get("title") or slug, ", ".join("`%s`" % f for f in files)
            ), ""]
            for entry in entries:
                flag = " **[DEPRECATED]**" if (entry.get("status") or "active") == "deprecated" else ""
                line = "- `%s`%s — %s" % (
                    entry.get("id"), flag, entry.get("description") or ""
                )
                if tier == "full":
                    terms = list(dict.fromkeys(
                        list(entry.get("keywords") or []) + list(entry.get("aliases") or [])
                    ))
                    if terms:
                        line += " *(also: %s)*" % ", ".join(terms)
                lines.append(line)
            lines.append("")
    else:
        lines += ["",
                  "The node-level index is in `%s`. Consult it before answering."
                  % INDEX_NAME, ""]

    lines += [
        "## Answering",
        "",
        "- **Cite the node.** Give the node id and its sources. If two nodes",
        "  contributed, cite both.",
        "- **Conflicts are not yours to resolve.** A node carrying a",
        "  `> [!warning] Conflict` callout has sources that disagree. Present both",
        "  versions, name the sources, and say it is unresolved. Never pick one.",
        "- **Deprecated nodes are history.** A node marked `[DEPRECATED]` describes",
        "  a superseded rule. Answer from it only when the question is explicitly",
        "  about the past. Otherwise name its successor and answer from that. If a",
        "  deprecated node is the only match, say the rule was superseded.",
        "- **Low source confidence is a caveat, not a disqualifier.** A node marked",
        "  `Source confidence: low` may still be right — surface the caveat.",
        "- **Gaps are findings.** When nothing covers the question, say the",
        "  knowledge base does not cover it, name the closest nodes, and stop.",
    ]
    if has_conflicts:
        lines += [
            "- `%s` lists every open conflict in the base. Check it when a"
            % CONFLICTS_NAME,
            "  question touches a contested area.",
        ]

    lines += [
        "",
        "---",
        "",
        "Generated %s from %d categories and %d nodes (%d deprecated) · content hash `%s`."
        % (generated, totals["clusters"], totals["nodes"],
           totals["deprecated_nodes"], content_hash or "unknown"),
        "Regenerate with `/kb-export-project` after every knowledge base update,",
        "and replace both these instructions and the uploaded files.",
    ]
    return "\n".join(lines).rstrip() + "\n"


def render_readme(title, tier, instruction_chars, bundles, totals, generated):
    lines = [
        "# %s — Claude Project export" % title,
        "",
        "Generated %s · %d categories · %d nodes · index tier `%s` (%d chars)"
        % (generated, totals["clusters"], totals["nodes"], tier, instruction_chars),
        "",
        "## Setting it up",
        "",
        "1. Create a new Project on claude.ai.",
        "2. Open its **Instructions** and paste the entire contents of",
        "   `%s`." % INSTRUCTIONS_NAME,
        "3. Add **every** file in `%s/` to the project knowledge:" % KNOWLEDGE_DIRNAME,
        "",
    ]
    lines += ["   - `%s`" % name for name in sorted(bundles)]
    lines += [
        "",
        "That is the whole setup. The instructions carry the category and node",
        "index, so the Project routes to a named node instead of searching blind.",
        "",
        "## Keeping it current",
        "",
        "This export is a snapshot. After `/kb-build` or `/kb-update`, re-run",
        "`/kb-export-project`, then replace both the instructions and the uploaded",
        "files — a stale index points at nodes that may no longer exist.",
        "",
        "`python3 build_project_export.py --check` compares this export against the",
        "live router index and exits non-zero when it has gone stale.",
        "",
        "## Do not hand-edit",
        "",
        "Everything here is generated from the frontmatter in `wiki/`. Fix the",
        "node, rebuild, re-export — an edit made here is lost on the next run.",
    ]
    return "\n".join(lines).rstrip() + "\n"


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def write_text(path, text):
    K.ensure_dir(os.path.dirname(path))
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.replace(tmp, path)
    return path


def run_check(out_dir, content_hash):
    manifest = K.read_json(os.path.join(out_dir, MANIFEST_NAME), default=None)
    if manifest is None:
        print("stale: no export at %s" % out_dir)
        return 1
    exported = manifest.get("content_hash") or ""
    if exported != content_hash:
        print("stale: export hash %s, wiki hash %s — re-run the export"
              % (exported or "none", content_hash or "none"))
        return 1
    print("current: export matches the wiki (hash %s, generated %s)"
          % (content_hash, manifest.get("generated")))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root")
    ap.add_argument("--vault", help="vault directory (default <root>/wiki)")
    ap.add_argument("--out", help="output directory (default <root>/exports/claude-project)")
    ap.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS,
                    help="budget for the instructions field (default %d)" % DEFAULT_MAX_CHARS)
    ap.add_argument("--tier", choices=TIERS, help="force an index tier instead of auto-fitting")
    ap.add_argument("--max-bundle-kb", type=int, default=DEFAULT_MAX_BUNDLE_KB,
                    help="split a cluster bundle above this size (default %d)" % DEFAULT_MAX_BUNDLE_KB)
    ap.add_argument("--intro", help="file whose contents open the scope section")
    ap.add_argument("--title", help="knowledge base title (default from wiki/index.md)")
    ap.add_argument("--check", action="store_true",
                    help="report whether an existing export is current; exit 1 if stale")
    args = ap.parse_args()

    root = K.project_root(args.root)
    P = K.paths(root)
    wiki_dir = os.path.abspath(args.vault) if args.vault else P["wiki"]
    out_dir = os.path.abspath(args.out) if args.out else os.path.join(root, EXPORT_DIRNAME)

    if not os.path.isdir(wiki_dir):
        raise SystemExit("error: no wiki at %s — nothing to export" % wiki_dir)

    router_dir = os.path.join(wiki_dir, K.META_DIR, "router")
    categories, layer2, router_manifest = load_router(router_dir)
    content_hash = router_manifest.get("content_hash") or ""

    if args.check:
        return run_check(out_dir, content_hash)

    # Refuse to write into the vault: kblib.iter_wiki_files would scan the
    # bundles as nodes and break validate.py and the router index.
    if os.path.commonpath([os.path.abspath(out_dir), wiki_dir]) == wiki_dir:
        raise SystemExit(
            "error: --out is inside the vault (%s). Markdown under wiki/ is scanned "
            "as knowledge-base nodes; export to a sibling directory instead." % wiki_dir
        )

    title = vault_title(wiki_dir, args.title)
    bodies = load_bodies(wiki_dir)
    id_of = build_id_map(wiki_dir, categories)
    resolve, _ambiguous = K.build_link_resolver(K.load_all_notes(wiki_dir), [], wiki_dir)

    intro = ""
    if args.intro:
        with open(args.intro, "r", encoding="utf-8") as fh:
            intro = fh.read().strip()

    # ---- node sections ----------------------------------------------------
    unresolved, missing_body, conflicts = [], [], 0
    sections = {}
    for cat in categories:
        for entry in layer2.get(cat.get("slug")) or []:
            raw = bodies.get(entry.get("path") or "")
            if raw is None:
                missing_body.append(entry.get("path"))
                raw = ""
            if K.CALLOUT_CONFLICT_RE.search(raw):
                conflicts += 1
            sections[entry["id"]] = render_node_section(
                entry, raw, wiki_dir, resolve, id_of, unresolved
            )

    bundles = pack_bundles(categories, layer2, sections, args.max_bundle_kb * 1024)
    file_of = {}
    for name, _text, group in bundles:
        for entry in group:
            file_of[entry["id"]] = name

    all_nodes = [e for cat in categories for e in (layer2.get(cat.get("slug")) or [])]
    totals = {
        "clusters": len(categories),
        "nodes": len(all_nodes),
        "deprecated_nodes": sum(1 for e in all_nodes if (e.get("status") or "active") == "deprecated"),
        "conflicts": conflicts,
        "bundles": len(bundles),
    }
    generated = K.now_iso()

    # ---- tier fitting -----------------------------------------------------
    conflicts_src = os.path.join(wiki_dir, K.META_DIR, "conflicts.md")
    has_conflicts = os.path.exists(conflicts_src)

    def instructions_for(tier):
        return render_instructions(title, categories, layer2, file_of, tier, intro,
                                   generated, content_hash, totals, has_conflicts)

    if args.tier:
        tier = args.tier
        instructions = instructions_for(tier)
    else:
        tier, instructions = TIERS[-1], instructions_for(TIERS[-1])
        for candidate in TIERS:
            text = instructions_for(candidate)
            if len(text) <= args.max_chars:
                tier, instructions = candidate, text
                break

    # ---- write ------------------------------------------------------------
    knowledge_dir = os.path.join(out_dir, KNOWLEDGE_DIRNAME)
    K.ensure_dir(knowledge_dir)

    written = set()
    for name, text, _group in bundles:
        write_text(os.path.join(knowledge_dir, name), text)
        written.add(name)

    index_md = render_index(title, categories, layer2, file_of, generated,
                            content_hash, totals)
    write_text(os.path.join(knowledge_dir, INDEX_NAME), index_md)
    written.add(INDEX_NAME)

    if has_conflicts:
        with open(conflicts_src, "r", encoding="utf-8", errors="replace") as fh:
            _fm, _raw, body = K.split_frontmatter(fh.read())
        write_text(os.path.join(knowledge_dir, CONFLICTS_NAME),
                   "# Open conflicts\n\n" + (body or "").strip() + "\n")
        written.add(CONFLICTS_NAME)

    # Clusters that no longer exist must not leave a bundle behind: an uploaded
    # stale bundle is a node the Project will happily answer from.
    removed = []
    for name in sorted(os.listdir(knowledge_dir)):
        if name.endswith(".md") and name not in written:
            os.remove(os.path.join(knowledge_dir, name))
            removed.append(name)

    write_text(os.path.join(out_dir, INSTRUCTIONS_NAME), instructions)
    write_text(os.path.join(out_dir, "README.md"),
               render_readme(title, tier, len(instructions),
                             [n for n, _t, _g in bundles] + sorted(written - {n for n, _t, _g in bundles}),
                             totals, generated))

    files = [{"path": INSTRUCTIONS_NAME, "kind": "instructions",
              "chars": len(instructions)}]
    for name in sorted(written):
        path = os.path.join(knowledge_dir, name)
        files.append({"path": "%s/%s" % (KNOWLEDGE_DIRNAME, name),
                      "kind": "knowledge", "bytes": os.path.getsize(path)})

    K.write_json(os.path.join(out_dir, MANIFEST_NAME), {
        "version": 1,
        "generated": generated,
        "content_hash": content_hash,
        "vault": K.rel(wiki_dir, root),
        "title": title,
        "tier": tier,
        "instruction_chars": len(instructions),
        "max_chars": args.max_chars,
        "totals": totals,
        "files": files,
        "unresolved_links": sorted(set(unresolved)),
        "missing_bodies": sorted(set(p for p in missing_body if p)),
    })

    # ---- report -----------------------------------------------------------
    print("claude project export: %s" % K.rel(out_dir, root))
    print("  instructions  %s  tier %s, %d/%d chars"
          % (INSTRUCTIONS_NAME, tier, len(instructions), args.max_chars))
    print("  knowledge     %d files (%d clusters, %d nodes, %d deprecated)"
          % (len(written), totals["clusters"], totals["nodes"], totals["deprecated_nodes"]))
    for name in sorted(written):
        size = os.path.getsize(os.path.join(knowledge_dir, name))
        print("    %-44s %7.1f KB" % (name, size / 1024.0))
    if removed:
        print("  removed stale bundles: %s" % ", ".join(removed))
    if tier != "full":
        print("  note: index tier degraded to `%s` to fit %d chars — the complete "
              "index is in %s/%s" % (tier, args.max_chars, KNOWLEDGE_DIRNAME, INDEX_NAME))
    if len(instructions) > args.max_chars:
        # The contract, routing protocol and answer rules are fixed prose; below
        # roughly 5k chars no tier can fit, and trimming them would cost the
        # grounding that makes the export worth having.
        print("  warning: instructions are %d chars, over the %d budget. Tier `%s` is "
              "the smallest available — raise --max-chars or split the base."
              % (len(instructions), args.max_chars, tier))
    if unresolved:
        uniq = sorted(set(unresolved))
        print("  warning: %d unresolved wikilink target(s): %s"
              % (len(uniq), ", ".join(uniq[:8]) + (" …" if len(uniq) > 8 else "")))
    if missing_body:
        print("  warning: %d node(s) with no body on disk" % len(set(missing_body)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
