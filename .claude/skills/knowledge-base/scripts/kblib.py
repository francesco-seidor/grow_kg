"""Shared helpers for the knowledge-base pipeline scripts.

Stdlib-only by design (PyYAML is used when importable, with a fallback parser
for the frontmatter subset this pipeline emits).
"""

import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone

try:  # optional, nicer YAML handling when available
    import yaml  # type: ignore

    HAVE_YAML = True
except Exception:  # pragma: no cover
    yaml = None
    HAVE_YAML = False

SUPPORTED_EXT = {".md", ".markdown", ".txt", ".docx", ".doc", ".rtf", ".xlsx", ".xlsm", ".csv"}
KNOWN_UNSUPPORTED = {
    ".pdf": "PDF is out of scope for this pipeline",
    ".ppt": "PowerPoint is out of scope for this pipeline",
    ".pptx": "PowerPoint is out of scope for this pipeline",
    ".xls": "Legacy .xls is not supported; re-save as .xlsx",
    ".key": "Keynote is out of scope for this pipeline",
    ".pages": "Pages is out of scope for this pipeline",
    ".odt": "OpenDocument is not supported; re-save as .docx",
    ".epub": "E-books are out of scope for this pipeline",
    ".html": "HTML is not supported; re-save as .docx or .md",
    ".htm": "HTML is not supported; re-save as .docx or .md",
}
IGNORED_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini", ".gitkeep", ".gitignore"}

CLUSTER_HUB = "_cluster.md"
META_DIR = "_meta"
GRAPH_HTML = "graph.html"
CHAT_HTML = "chat.html"
GRAPH_DATA = "graph-data.js"
CHAT_DATA = "chat-data.js"
GRAPH_GLOBAL = "__KB_GRAPH__"
CHAT_GLOBAL = "__KB_CHAT__"
VENDOR_DIR = "vendor"

# The viewers are shipped, not generated: `wiki/graph.html` and `wiki/chat.html`
# are byte-for-byte copies of the assets below, and only their data files are
# rebuilt per compile. Destinations are wiki-relative.
#
# The data files are `.js`, not `.json`, and that is load-bearing: browsers block
# fetch()/XHR of a sibling file from a file:// page, so a double-clicked
# graph.html could never read a .json next to it. A classic <script src> does
# load from file://, so the payload arrives as an assignment to a global. A
# missing file then fails silently and leaves the global undefined — which is
# exactly the "run /kb-build first" banner condition, with no probing needed.
VIEWER_ASSETS = [
    ("graph-viewer.html", GRAPH_HTML),
    ("chat-viewer.html", CHAT_HTML),
    ("chat-app.js", os.path.join(META_DIR, "chat-app.js")),
    (os.path.join(VENDOR_DIR, "d3.v7.min.js"),
     os.path.join(META_DIR, VENDOR_DIR, "d3.v7.min.js")),
    (os.path.join(VENDOR_DIR, "anthropic-sdk.browser.js"),
     os.path.join(META_DIR, VENDOR_DIR, "anthropic-sdk.browser.js")),
]


# --------------------------------------------------------------------------
# paths
# --------------------------------------------------------------------------
def project_root(explicit=None):
    """Resolve the project root: explicit flag, env var, or cwd."""
    if explicit:
        return os.path.abspath(explicit)
    env = os.environ.get("KB_ROOT")
    if env:
        return os.path.abspath(env)
    return os.path.abspath(os.getcwd())


def paths(root):
    root = os.path.abspath(root)
    return {
        "root": root,
        "raw": os.path.join(root, "raw_assets"),
        "kb": os.path.join(root, ".kb"),
        "wiki": os.path.join(root, "wiki"),
        "extracted": os.path.join(root, ".kb", "extracted"),
        "digests": os.path.join(root, ".kb", "digests"),
        "batches": os.path.join(root, ".kb", "batches"),
        "shards": os.path.join(root, ".kb", "shards"),
        "manifest": os.path.join(root, ".kb", "manifest.json"),
        "unsupported": os.path.join(root, ".kb", "unsupported.json"),
        "state": os.path.join(root, ".kb", "state.json"),
        "taxonomy": os.path.join(root, ".kb", "taxonomy.json"),
        "topic_pool": os.path.join(root, ".kb", "topic-pool.json"),
        "validation": os.path.join(root, ".kb", "validation.json"),
        "router": os.path.join(root, "wiki", META_DIR, "router"),
        "meta": os.path.join(root, "wiki", META_DIR),
        "wiki_vendor": os.path.join(root, "wiki", META_DIR, VENDOR_DIR),
        "graph_html": os.path.join(root, "wiki", GRAPH_HTML),
        "chat_html": os.path.join(root, "wiki", CHAT_HTML),
        "graph_data": os.path.join(root, "wiki", META_DIR, GRAPH_DATA),
        "chat_data": os.path.join(root, "wiki", META_DIR, CHAT_DATA),
    }


def skill_dir():
    """The knowledge-base skill root — the parent of scripts/."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def assets_dir():
    return os.path.join(skill_dir(), "assets")


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
    return path


def rel(path, root):
    try:
        return os.path.relpath(path, root)
    except ValueError:
        return path


# --------------------------------------------------------------------------
# json io
# --------------------------------------------------------------------------
def read_json(path, default=None):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError as exc:
        raise SystemExit(f"error: {path} is not valid JSON ({exc})")


def write_json(path, data):
    ensure_dir(os.path.dirname(path))
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False, sort_keys=False)
        fh.write("\n")
    os.replace(tmp, path)
    return path


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# --------------------------------------------------------------------------
# slugs
# --------------------------------------------------------------------------
def slugify(value, max_len=60):
    value = unicodedata.normalize("NFKD", str(value or ""))
    value = value.encode("ascii", "ignore").decode("ascii").lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    value = re.sub(r"-{2,}", "-", value)
    if len(value) > max_len:
        value = value[:max_len].rstrip("-")
    return value or "untitled"


def unique_slug(candidate, taken):
    slug = candidate
    n = 2
    while slug in taken:
        slug = f"{candidate}-{n}"
        n += 1
    taken.add(slug)
    return slug


# --------------------------------------------------------------------------
# frontmatter
# --------------------------------------------------------------------------
FM_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.DOTALL)


def split_frontmatter(text):
    """Return (frontmatter_dict_or_None, raw_fm_string, body)."""
    match = FM_RE.match(text or "")
    if not match:
        return None, "", text or ""
    raw = match.group(1)
    body = (text or "")[match.end():]
    return parse_yaml_block(raw), raw, body


def parse_yaml_block(raw):
    if HAVE_YAML:
        try:
            data = yaml.safe_load(raw)
            return data if isinstance(data, dict) else {}
        except Exception:
            pass
    return _mini_yaml(raw)


def _mini_yaml(raw):
    """Parse the flat subset this pipeline emits: scalars, inline and dash lists."""
    out = {}
    key = None
    for line in (raw or "").split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\s*-\s+", line) and key:
            out.setdefault(key, [])
            if isinstance(out[key], list):
                out[key].append(_scalar(re.sub(r"^\s*-\s+", "", line)))
            continue
        m = re.match(r"^([A-Za-z0-9_.-]+)\s*:\s*(.*)$", line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        if value == "":
            out[key] = []
        elif value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            out[key] = [_scalar(p) for p in _split_inline(inner)] if inner else []
        else:
            out[key] = _scalar(value)
    return out


def _split_inline(inner):
    parts, buf, quote = [], "", None
    for ch in inner:
        if quote:
            if ch == quote:
                quote = None
            buf += ch
        elif ch in "\"'":
            quote = ch
            buf += ch
        elif ch == ",":
            parts.append(buf)
            buf = ""
        else:
            buf += ch
    if buf.strip():
        parts.append(buf)
    return [p.strip() for p in parts if p.strip()]


def _scalar(value):
    value = (value or "").strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    if value.lower() in ("true", "false"):
        return value.lower() == "true"
    if re.fullmatch(r"-?\d+", value):
        try:
            return int(value)
        except ValueError:
            return value
    return value


def dump_frontmatter(data, order=None):
    """Serialise a flat dict to a YAML frontmatter block (without --- fences)."""
    keys = list(order or []) + [k for k in data if k not in (order or [])]
    lines = []
    for key in keys:
        if key not in data:
            continue
        value = data[key]
        if isinstance(value, (list, tuple)):
            items = ", ".join(_fm_scalar(v) for v in value)
            lines.append(f"{key}: [{items}]")
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif value is None:
            lines.append(f"{key}:")
        else:
            lines.append(f"{key}: {_fm_scalar(value)}")
    return "\n".join(lines)


def _fm_scalar(value):
    text = str(value)
    if text == "":
        return '""'
    if re.search(r"[:#\[\]{},\"']", text) or text.strip() != text:
        return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return text


def as_list(value):
    if value is None or value == "":
        return []
    if isinstance(value, (list, tuple)):
        return [str(v).strip() for v in value if str(v).strip()]
    return [p.strip() for p in str(value).split(",") if p.strip()]


# --------------------------------------------------------------------------
# wiki scanning
# --------------------------------------------------------------------------
# Tolerates the backslash-escaped pipe Obsidian requires inside table cells:
# [[node\|Display]] must parse with target "node", not "node\".
WIKILINK_RE = re.compile(
    r"\[\[([^\[\]|#\\]+)(?:\\?#([^\[\]|\\]+))?(?:\\?\|([^\[\]]+))?\]\]"
)
EDGE_RE = re.compile(r"^\s*[-*]\s*([a-z][a-z-]*)\s*::\s*(.+?)\s*$", re.MULTILINE)
CALLOUT_CONFLICT_RE = re.compile(r"^>\s*\[!warning\]\s*Conflict\s*$", re.MULTILINE | re.IGNORECASE)

EDGE_TYPES = [
    "part-of",
    "depends-on",
    "supersedes",
    "superseded-by",
    "contradicts",
    "related-to",
    "see-also",
]


def iter_wiki_files(wiki_dir, include_meta=False, include_hubs=True):
    """Yield absolute paths of markdown files in the vault."""
    for dirpath, dirnames, filenames in os.walk(wiki_dir):
        dirnames[:] = [
            d for d in sorted(dirnames)
            if not d.startswith(".") and (include_meta or d != META_DIR)
        ]
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            if not include_hubs and name == CLUSTER_HUB:
                continue
            yield os.path.join(dirpath, name)


def load_note(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    fm, raw, body = split_frontmatter(text)
    return {
        "path": path,
        "text": text,
        "frontmatter": fm or {},
        "has_frontmatter": fm is not None,
        "body": body,
    }


def load_all_notes(wiki_dir):
    """Every markdown file in the vault, `_meta/` and index.md included.

    Link resolution must see these: notes legitimately link to `_meta/conflicts`
    and to `index`, and treating them as unresolvable would be a false alarm.
    """
    notes = []
    if not os.path.isdir(wiki_dir):
        return notes
    for path in iter_wiki_files(wiki_dir, include_meta=True):
        note = load_note(path)
        note["rel"] = rel(path, wiki_dir)
        note["basename"] = os.path.basename(path)[:-3]
        notes.append(note)
    return notes


def scan_vault(wiki_dir):
    """Return (nodes, hubs) lists of parsed notes, excluding _meta and index."""
    nodes, hubs = [], []
    if not os.path.isdir(wiki_dir):
        return nodes, hubs
    for path in iter_wiki_files(wiki_dir):
        name = os.path.basename(path)
        note = load_note(path)
        note["rel"] = rel(path, wiki_dir)
        note["basename"] = name[:-3]
        if name == CLUSTER_HUB:
            hubs.append(note)
        elif note["rel"] == "index.md":
            continue
        else:
            nodes.append(note)
    return nodes, hubs


def extract_wikilinks(body):
    return [
        {"target": m.group(1).strip(), "heading": (m.group(2) or "").strip(),
         "alias": (m.group(3) or "").strip()}
        for m in WIKILINK_RE.finditer(body or "")
    ]


def extract_edges(body):
    """Parse the `- type :: [[target]]` lines from a Connections section."""
    section = connections_section(body)
    edges = []
    for m in EDGE_RE.finditer(section):
        etype = m.group(1).strip()
        for link in extract_wikilinks(m.group(2)):
            edges.append({"type": etype, "target": link["target"]})
    return edges


def connections_section(body):
    match = re.search(
        r"^##\s+Connections\s*$(.*?)(?=^##\s+|\Z)", body or "", re.MULTILINE | re.DOTALL
    )
    return match.group(1) if match else ""


def build_link_resolver(notes, hubs, wiki_dir):
    """Map wikilink targets to note paths the way Obsidian's shortest-path mode does.

    Resolves, in order: exact vault-relative path, unique basename, and
    `<cluster>/<basename>`. Returns (resolve, ambiguous_basenames).
    """
    by_rel, by_base = {}, {}
    for note in list(notes) + list(hubs):
        relpath = rel(note["path"], wiki_dir)
        stem = relpath[:-3] if relpath.endswith(".md") else relpath
        by_rel[stem] = note["path"]
        by_rel[relpath] = note["path"]
        by_base.setdefault(os.path.basename(stem), []).append(note["path"])

    ambiguous = {b for b, paths in by_base.items() if len(paths) > 1}

    def resolve(target, from_path=None):
        target = (target or "").strip().lstrip("./")
        if not target:
            return None
        if target in by_rel:
            return by_rel[target]
        if target + ".md" in by_rel:
            return by_rel[target + ".md"]
        base = os.path.basename(target)
        # Prefer a sibling in the linking note's own cluster.
        if from_path:
            sibling = os.path.join(os.path.dirname(from_path), base + ".md")
            if os.path.exists(sibling):
                return sibling
        hits = by_base.get(base, [])
        if len(hits) == 1:
            return hits[0]
        return None

    return resolve, ambiguous


# --------------------------------------------------------------------------
# the graph
# --------------------------------------------------------------------------
def collect_graph(wiki_dir):
    """The node/edge graph exactly as it exists on disk — never inferred.

    Typed edges from `## Connections` come first; an inline wikilink to a note
    not already reached by a typed edge is recorded as `related-to`. Self-links
    and unresolvable targets are dropped.

    Returns:
      {
        "nodes":      [note dict, ...],           # scan_vault nodes, each + "cluster"
        "hubs":       {cluster_slug: note dict},  # _cluster.md per cluster
        "by_cluster": {cluster_slug: [note dict, ...]},
        "cluster_of": {abs_path: cluster_slug},   # nodes and hubs
        "links":      [(src_abs_path, dst_abs_path, edge_type), ...],
        "inbound":    Counter({abs_path: inbound_degree}),
      }
    """
    nodes, hubs = scan_vault(wiki_dir)
    resolve, _ = build_link_resolver(load_all_notes(wiki_dir), [], wiki_dir)
    hub_by_cluster = {}
    for hub in hubs:
        slug = str(hub["frontmatter"].get("cluster")
                   or os.path.basename(os.path.dirname(hub["path"])))
        hub_by_cluster[slug] = hub

    by_cluster = defaultdict(list)
    for note in nodes:
        slug = str(note["frontmatter"].get("cluster")
                   or os.path.basename(os.path.dirname(note["path"])))
        note["cluster"] = slug
        by_cluster[slug].append(note)

    cluster_of = {n["path"]: n["cluster"] for n in nodes}
    for slug, hub in hub_by_cluster.items():
        cluster_of[hub["path"]] = slug

    links = []
    inbound = Counter()
    for note in nodes:
        typed = {(e["type"], e["target"]) for e in extract_edges(note["body"])}
        seen = set()
        for etype, target in typed:
            dest = resolve(target, note["path"])
            if dest and dest != note["path"]:
                links.append((note["path"], dest, etype))
                inbound[dest] += 1
                seen.add(dest)
        for link in extract_wikilinks(note["body"]):
            dest = resolve(link["target"], note["path"])
            if dest and dest != note["path"] and dest not in seen:
                links.append((note["path"], dest, "related-to"))
                inbound[dest] += 1
                seen.add(dest)

    return {
        "nodes": nodes,
        "hubs": hub_by_cluster,
        "by_cluster": dict(by_cluster),
        "cluster_of": cluster_of,
        "links": links,
        "inbound": inbound,
    }


# --------------------------------------------------------------------------
# graph viewer
# --------------------------------------------------------------------------
# One hue per cluster in the viewer. Colour-blind-tolerant, and deliberately a
# fixed list: the viewer composites hue with a solid/hollow tier so more
# clusters than hues never forces a generated colour.
CLUSTER_PALETTE = [
    "#4c78a8", "#f58518", "#54a24b", "#e45756", "#72b7b2", "#b279a2",
    "#ff9da6", "#9d755d", "#bab0ac", "#59a14f", "#edc948", "#86bcb6",
]

# Edge hue does 4-way work only (directed / lateral / conflict / chrome); the
# viewer carries the 7-way distinction with width, dash and arrowhead so it
# survives colour-blindness, greyscale and forced-colors.
EDGE_COLORS = {
    "part-of": "#8e8e93",
    "depends-on": "#4c78a8",
    "supersedes": "#4c78a8",
    "superseded-by": "#4c78a8",
    "contradicts": "#d1265b",
    "related-to": "#54a24b",
    "see-also": "#54a24b",
}

GRAPH_SCHEMA = 1

_DATA_PREFIX_RE = re.compile(r"^\s*window\.(__[A-Z_]+__)\s*=\s*", re.DOTALL)


def encode_data_file(global_name, payload_json):
    """Wrap an encoded payload as the one-line data file a viewer loads.

    `payload_json` is already-encoded JSON (see build_graph_data.encode_payload),
    so this only adds the assignment the <script src> needs.
    """
    return f"window.{global_name} = {payload_json};\n"


def read_data_payload(path, max_bytes=256 * 1024 * 1024):
    """Parse a generated `_meta/*-data.js` file back into its payload dict.

    Returns None when the file is missing, implausibly large, not an assignment
    to a `window.__…__` global, or not parseable JSON — every one of which means
    the viewer cannot be trusted to describe the wiki.
    """
    try:
        if os.path.getsize(path) > max_bytes:
            return None
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError:
        return None
    match = _DATA_PREFIX_RE.match(text)
    if not match:
        return None
    body = text[match.end():].strip()
    if body.endswith(";"):
        body = body[:-1]
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


# Kept under its old name because `viewer`-family callers read like prose:
# "the payload the graph viewer would show".
read_graph_payload = read_data_payload


def sha256_file(path):
    import hashlib

    h = hashlib.sha256()
    try:
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                h.update(chunk)
    except OSError:
        return None
    return h.hexdigest()


def sync_viewer_assets(P, assets=None):
    """Copy the shipped viewers and their vendored libraries into `wiki/`.

    Idempotent and content-addressed: a destination whose sha256 already matches
    is left alone, so a compile that changes nothing touches nothing. Returns
    `(copied, notes)` — `copied` is the list of wiki-relative destinations
    written, `notes` the human-readable problems worth printing.

    This is what puts a viewer in a brand-new `wiki/` before any data exists:
    opened then, it shows its "run /kb-build first" banner rather than a 404.
    """
    import shutil

    src_root = assets_dir()
    copied, notes = [], []
    for src_rel, dst_rel in (assets or VIEWER_ASSETS):
        src = os.path.join(src_root, src_rel)
        dst = os.path.join(P["wiki"], dst_rel)
        if not os.path.exists(src):
            notes.append(f"missing asset {rel(src, skill_dir())} — {dst_rel} not installed")
            continue
        digest = sha256_file(src)

        # Vendored libraries carry a committed checksum. A mismatch is reported
        # and the file still installed: refusing to copy would leave the viewer
        # loading nothing, which is a worse failure than an unverified d3.
        checksum_path = src + ".sha256"
        if os.path.exists(checksum_path):
            try:
                with open(checksum_path, "r", encoding="utf-8") as fh:
                    expected = fh.read().split()[0].strip()
            except (OSError, IndexError):
                expected = None
            if expected and digest and expected != digest:
                notes.append(
                    f"{src_rel} checksum mismatch (expected {expected[:12]}…, "
                    f"got {digest[:12]}…) — installing it anyway"
                )

        if os.path.exists(dst) and sha256_file(dst) == digest:
            continue
        ensure_dir(os.path.dirname(dst))
        tmp = dst + ".tmp"
        shutil.copyfile(src, tmp)
        os.replace(tmp, dst)
        copied.append(dst_rel)
    return copied, notes


def viewer_assets_status(P, assets=None):
    """Which installed copies are missing or differ from the shipped asset.

    Returns `(missing, drifted)` as lists of wiki-relative paths. Drift means
    the copy in `wiki/` was hand-edited or came from another version of this
    skill — the viewer on disk is then not the viewer this repo describes.
    """
    src_root = assets_dir()
    missing, drifted = [], []
    for src_rel, dst_rel in (assets or VIEWER_ASSETS):
        src = os.path.join(src_root, src_rel)
        dst = os.path.join(P["wiki"], dst_rel)
        if not os.path.exists(dst):
            missing.append(dst_rel)
        elif os.path.exists(src) and sha256_file(dst) != sha256_file(src):
            drifted.append(dst_rel)
    return missing, drifted


def stale_obsidian_artifacts(wiki_dir):
    """Leftovers from before the graph viewer. Reports; never deletes anything.

    These may be committed, and `.obsidian/` may hold a reader's own hand-tuned
    settings — wikilinks still work, so opening wiki/ in Obsidian stays a valid
    personal choice that this pipeline simply no longer manages.
    """
    found = []
    if not os.path.isdir(wiki_dir):
        return found
    if os.path.isdir(os.path.join(wiki_dir, ".obsidian")):
        found.append(".obsidian/")
    for dirpath, dirnames, filenames in os.walk(wiki_dir):
        dirnames[:] = [d for d in sorted(dirnames) if d != ".obsidian"]
        for name in sorted(filenames):
            if name.endswith(".canvas"):
                found.append(rel(os.path.join(dirpath, name), wiki_dir))
    canvas_dir = os.path.join(wiki_dir, META_DIR, "canvas")
    if os.path.isdir(canvas_dir) and not os.listdir(canvas_dir):
        found.append(f"{META_DIR}/canvas/  (empty)")
    return found


def eprint(*args):
    print(*args, file=sys.stderr)
