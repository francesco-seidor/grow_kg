#!/usr/bin/env python3
"""Stage 0 — extract raw_assets/** into normalised markdown under .kb/extracted/.

Supported inputs: .md .markdown .txt .docx .doc .rtf .xlsx .xlsm .csv
Everything else is recorded in .kb/unsupported.json and reported — never
silently dropped.

Extraction routes, best first:
  .docx  -> mammoth (preserves Word heading styles) -> html2md
  .docx  -> bundled XML reader (fallback, no deps)
  .doc   -> textutil -convert html (macOS) -> html2md
  .rtf   -> textutil -convert html (macOS) -> html2md
  .md    -> normalised copy
  .txt   -> normalised copy with a title heading
  .xlsx/.xlsm/.csv -> xlsx2md: one `## Sheet:` table per worksheet (stdlib only)

Companions: a spreadsheet next to a Word document with the same filename stem
(SAP ships test scripts as both) is recorded as a companion of that document and
not compiled twice; `--no-companions` compiles it anyway.

Usage:
  python3 extract.py [--root DIR] [--raw DIR] [--force] [--dry-run] [--json]
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import kblib as K  # noqa: E402
import xlsx2md  # noqa: E402
from html2md import html_to_markdown, normalize_markdown  # noqa: E402


def reexec_in_venv(root):
    """If mammoth is missing here but present in .kb/venv, re-exec there."""
    if os.environ.get("KB_NO_REEXEC"):
        return
    try:
        import mammoth  # noqa: F401
        return
    except ImportError:
        pass
    venv_py = os.path.join(root, ".kb", "venv", "bin", "python")
    # Compare literal paths, not realpath: a venv's bin/python is a symlink to the
    # same base interpreter, so realpath would make these compare equal.
    if os.path.exists(venv_py) and os.path.abspath(venv_py) != os.path.abspath(sys.executable):
        os.environ["KB_NO_REEXEC"] = "1"  # guards against an exec loop
        os.execv(venv_py, [venv_py, os.path.abspath(__file__)] + sys.argv[1:])


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# --------------------------------------------------------------------------
# docx
# --------------------------------------------------------------------------
STYLE_MAP = """
p[style-name='Title'] => h1:fresh
p[style-name='Subtitle'] => h2:fresh
p[style-name^='Heading 1'] => h1:fresh
p[style-name^='Heading 2'] => h2:fresh
p[style-name^='Heading 3'] => h3:fresh
p[style-name^='Heading 4'] => h4:fresh
p[style-name^='Heading 5'] => h5:fresh
p[style-name^='Heading 6'] => h6:fresh
p[style-name^='TOC'] => p:fresh
p[style-name='Quote'] => blockquote:fresh
p[style-name='Intense Quote'] => blockquote:fresh
r[style-name='Code'] => code
"""


def docx_via_mammoth(path):
    import mammoth  # local import: optional dependency

    with open(path, "rb") as fh:
        result = mammoth.convert_to_html(
            fh,
            style_map=STYLE_MAP,
            convert_image=mammoth.images.img_element(lambda image: {"src": ""}),
        )
    warnings = [m.message for m in result.messages if getattr(m, "type", "") != "info"]
    md, images = html_to_markdown(result.value)
    return md, "mammoth", warnings, images


DOCX_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def docx_via_xml(path):
    """Dependency-free docx reader: paragraphs, heading levels, lists, tables."""
    import xml.etree.ElementTree as ET

    with zipfile.ZipFile(path) as zf:
        try:
            xml = zf.read("word/document.xml").decode("utf-8", "replace")
        except KeyError:
            raise RuntimeError("not a Word document (missing word/document.xml)")
    root = ET.fromstring(xml)
    body = root.find(f"{DOCX_NS}body")
    out, images = [], []

    def para_text(p):
        buf = []
        for node in p.iter():
            tag = node.tag
            if tag == f"{DOCX_NS}t":
                buf.append(node.text or "")
            elif tag in (f"{DOCX_NS}tab",):
                buf.append(" ")
            elif tag in (f"{DOCX_NS}br", f"{DOCX_NS}cr"):
                buf.append("\n")
            elif tag == f"{DOCX_NS}drawing":
                images.append("embedded image")
                buf.append("<!-- image omitted: embedded image -->")
        return re.sub(r"[ \t]+", " ", "".join(buf)).strip()

    def para_style(p):
        ppr = p.find(f"{DOCX_NS}pPr")
        if ppr is None:
            return "", None
        style_el = ppr.find(f"{DOCX_NS}pStyle")
        style = (style_el.get(f"{DOCX_NS}val") or "") if style_el is not None else ""
        numpr = ppr.find(f"{DOCX_NS}numPr")
        level = None
        if numpr is not None:
            ilvl = numpr.find(f"{DOCX_NS}ilvl")
            level = int(ilvl.get(f"{DOCX_NS}val") or 0) if ilvl is not None else 0
        return style, level

    def emit_list_item(line):
        """Keep consecutive list items inside one markdown block, nesting included."""
        if out and re.match(r"^\s*- ", out[-1].rsplit("\n", 1)[-1]):
            out[-1] += "\n" + line
        else:
            out.append(line)

    def emit_para(p):
        text = para_text(p)
        if not text:
            return
        style, list_level = para_style(p)
        m = re.match(r"^Heading(\d)$", style) or re.match(r"^heading\s*(\d)$", style, re.I)
        if m:
            out.append("#" * min(6, int(m.group(1))) + " " + text)
        elif style in ("Title",):
            out.append("# " + text)
        elif style in ("Subtitle",):
            out.append("## " + text)
        elif style in ("Quote", "IntenseQuote"):
            out.append("> " + text.replace("\n", "\n> "))
        elif list_level is not None:
            emit_list_item("    " * list_level + "- " + text.replace("\n", " "))
        else:
            out.append(text)

    def emit_table(tbl):
        rows = []
        for tr in tbl.findall(f"{DOCX_NS}tr"):
            cells = []
            for tc in tr.findall(f"{DOCX_NS}tc"):
                cell = " ".join(
                    para_text(p) for p in tc.findall(f"{DOCX_NS}p")
                ).strip()
                cells.append(cell.replace("|", "\\|").replace("\n", " "))
            if cells:
                rows.append(cells)
        if not rows:
            return
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        lines = ["| " + " | ".join(rows[0]) + " |",
                 "| " + " | ".join("---" for _ in range(width)) + " |"]
        lines += ["| " + " | ".join(row) + " |" for row in rows[1:]]
        out.append("\n".join(lines))  # one block, or the table breaks

    if body is not None:
        for child in body:
            if child.tag == f"{DOCX_NS}p":
                emit_para(child)
            elif child.tag == f"{DOCX_NS}tbl":
                emit_table(child)

    md = normalize_markdown("\n\n".join(out))
    return md, "docx-xml", ["extracted without mammoth: inline emphasis lost"], images


def via_textutil(path):
    if not os.path.exists("/usr/bin/textutil"):
        raise RuntimeError("textutil unavailable (macOS only)")
    proc = subprocess.run(
        ["/usr/bin/textutil", "-convert", "html", "-stdout", path],
        capture_output=True,
        timeout=180,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            "textutil failed: " + proc.stderr.decode("utf-8", "replace").strip()[:200]
        )
    html = proc.stdout.decode("utf-8", "replace")
    md, images = html_to_markdown(html)
    return md, "textutil", ["converted via textutil: heading styles may be lost"], images


def plain_text(path, title):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    text = normalize_markdown(text)
    if not re.match(r"^#\s", text or ""):
        text = f"# {title}\n\n{text}"
    return text, "verbatim", [], []


def markdown_passthrough(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    fm, _, body = K.split_frontmatter(text)
    warnings = []
    if fm:
        warnings.append("source frontmatter preserved as a note at the top")
        keep = "\n".join(f"- {k}: {v}" for k, v in list(fm.items())[:20])
        body = f"<!-- source frontmatter -->\n{keep}\n\n{body}"
    return normalize_markdown(body), "verbatim", warnings, []


ROUTES = {
    ".docx": "docx",
    ".doc": "textutil",
    ".rtf": "textutil",
    ".md": "markdown",
    ".markdown": "markdown",
    ".txt": "text",
    ".xlsx": "sheet",
    ".xlsm": "sheet",
    ".csv": "sheet",
}


def extract_one(path, ext, title):
    if ROUTES.get(ext) == "docx":
        try:
            return docx_via_mammoth(path)
        except ImportError:
            return docx_via_xml(path)
        except Exception as exc:
            md, method, warns, imgs = docx_via_xml(path)
            return md, method, warns + [f"mammoth failed ({exc}); used XML fallback"], imgs
    if ROUTES.get(ext) == "textutil":
        try:
            md, method, warns, imgs = via_textutil(path)
        except RuntimeError:
            md, method, warns, imgs = "", "textutil", [], []
        if not md.strip() and ext == ".rtf":  # mislabelled plain text: textutil yields nothing
            md, _, _, imgs = plain_text(path, title)
            return md, "verbatim", ["named .rtf but holds plain text; read verbatim"], imgs
        return md, method, warns, imgs
    if ROUTES.get(ext) == "markdown":
        return markdown_passthrough(path)
    if ROUTES.get(ext) == "sheet":
        if ext == ".csv":
            md, warns = xlsx2md.csv_to_markdown(path, title)
        else:
            md, warns = xlsx2md.xlsx_to_markdown(path, title)
        return md, "xlsx2md", warns, []
    return plain_text(path, title)


def outline_of(md):
    return [
        {"level": len(m.group(1)), "text": m.group(2).strip()}
        for m in re.finditer(r"^(#{1,6})\s+(.+?)\s*$", md or "", re.MULTILINE)
    ][:200]


def title_of(md, fallback):
    m = re.search(r"^#\s+(.+?)\s*$", md or "", re.MULTILINE)
    if m and m.group(1).strip():
        return m.group(1).strip()
    return fallback


def humanize(name):
    text = re.sub(r"[_\-]+", " ", name)
    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:1].upper() + text[1:] if text else name


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", help="project root (default: cwd or $KB_ROOT)")
    ap.add_argument("--raw", help="override the raw_assets directory")
    ap.add_argument("--force", action="store_true", help="re-extract everything")
    ap.add_argument("--no-companions", action="store_true", help="compile spreadsheets that duplicate a Word document too")
    ap.add_argument("--dry-run", action="store_true", help="report only, write nothing")
    ap.add_argument("--json", action="store_true", help="machine-readable summary")
    args = ap.parse_args()

    root = K.project_root(args.root)
    reexec_in_venv(root)
    P = K.paths(root)
    raw_dir = os.path.abspath(args.raw) if args.raw else P["raw"]

    if not os.path.isdir(raw_dir):
        raise SystemExit(
            f"error: no raw_assets directory at {raw_dir}\n"
            f"Create it and put your .md / .docx source documents inside."
        )

    previous = K.read_json(P["manifest"], {}) or {}
    prev_by_path = {d["rel_path"]: d for d in previous.get("documents", [])}

    documents, unsupported, errors, companions = [], [], [], []
    # Ids already issued stay reserved: a new file must never be handed the id of an
    # existing document, or it overwrites that document's extracted text.
    taken_ids = {d["doc_id"] for d in previous.get("documents", []) if d.get("doc_id")}

    for dirpath, dirnames, filenames in os.walk(raw_dir):
        dirnames[:] = [d for d in sorted(dirnames) if not d.startswith(".")]
        for name in sorted(filenames):
            if name in K.IGNORED_NAMES or name.startswith("~$") or name.startswith("."):
                continue
            abspath = os.path.join(dirpath, name)
            # The folder's own README explains what to put here; it is not source
            # material. Nested READMEs are compiled normally.
            if name.lower() == "readme.md" and os.path.samefile(dirpath, raw_dir):
                continue
            relpath = os.path.join("raw_assets", K.rel(abspath, raw_dir)) if raw_dir == P["raw"] else K.rel(abspath, root)
            ext = os.path.splitext(name)[1].lower()

            if ext not in K.SUPPORTED_EXT:
                unsupported.append({
                    "rel_path": relpath,
                    "ext": ext or "(none)",
                    "bytes": os.path.getsize(abspath),
                    "reason": K.KNOWN_UNSUPPORTED.get(ext, "unrecognised file type"),
                })
                continue

            if ROUTES.get(ext) == "sheet" and not args.no_companions:
                twin = next((os.path.join(dirpath, os.path.splitext(name)[0] + t)
                             for t in (".docx", ".DOCX") if os.path.exists(os.path.join(dirpath, os.path.splitext(name)[0] + t))), None)
                if twin:
                    entry = {
                        "rel_path": relpath,
                        "ext": ext,
                        "bytes": os.path.getsize(abspath),
                        "companion_of": os.path.splitext(relpath)[0] + os.path.splitext(twin)[1],
                        "reason": "companion of the same-named Word document, which is compiled; not compiled twice (--no-companions overrides)",
                    }
                    companions.append(entry)
                    unsupported.append(entry)  # reported with the skipped files: never silent
                    continue

            stem = os.path.splitext(K.rel(abspath, raw_dir))[0]
            prev = prev_by_path.get(relpath)
            if prev and prev.get("doc_id"):
                doc_id = prev["doc_id"]  # ids are stable across runs
            else:
                doc_id = K.unique_slug(K.slugify(stem.replace(os.sep, "-")), taken_ids)
            digest = sha256_file(abspath)
            prev = prev_by_path.get(relpath)
            out_path = os.path.join(P["extracted"], doc_id + ".md")

            if (
                not args.force
                and prev
                and prev.get("sha256") == digest
                and os.path.exists(out_path)
            ):
                entry = dict(prev)
                entry["status"] = "unchanged"
                entry["doc_id"] = prev.get("doc_id", doc_id)
                documents.append(entry)
                continue

            if args.dry_run:
                documents.append({
                    "doc_id": doc_id,
                    "rel_path": relpath,
                    "ext": ext,
                    "sha256": digest,
                    "bytes": os.path.getsize(abspath),
                    "status": "changed" if prev else "new",
                    "planned_route": ROUTES.get(ext, "text"),
                })
                continue

            fallback_title = humanize(os.path.splitext(name)[0])
            try:
                md, method, warnings, images = extract_one(abspath, ext, fallback_title)
            except Exception as exc:  # keep going; report at the end
                errors.append({"rel_path": relpath, "error": f"{type(exc).__name__}: {exc}"})
                documents.append({
                    "doc_id": doc_id,
                    "rel_path": relpath,
                    "ext": ext,
                    "sha256": digest,
                    "bytes": os.path.getsize(abspath),
                    "status": "failed",
                    "error": str(exc)[:400],
                })
                continue

            md = normalize_markdown(md)
            if not md.strip():
                warnings = list(warnings) + ["extraction produced no text"]

            header = (
                f"<!-- kb:doc_id={doc_id} source={relpath} method={method} -->\n\n"
            )
            K.ensure_dir(P["extracted"])
            with open(out_path, "w", encoding="utf-8") as fh:
                fh.write(header + md)

            documents.append({
                "doc_id": doc_id,
                "rel_path": relpath,
                "ext": ext,
                "sha256": digest,
                "bytes": os.path.getsize(abspath),
                "chars": len(md),
                "words": len(md.split()),
                "method": method,
                "extracted_path": K.rel(out_path, root),
                "title": title_of(md, fallback_title),
                "outline": outline_of(md),
                "images_omitted": len(images),
                "warnings": warnings,
                "status": "changed" if prev else "new",
                "extracted_at": K.now_iso(),
            })

    dropped = [d for d in prev_by_path if d not in {x["rel_path"] for x in documents}]

    manifest = {
        "version": 1,
        "generated": K.now_iso(),
        "root": root,
        "raw_dir": K.rel(raw_dir, root),
        "counts": {
            "documents": len(documents),
            "new": sum(1 for d in documents if d.get("status") == "new"),
            "changed": sum(1 for d in documents if d.get("status") == "changed"),
            "unchanged": sum(1 for d in documents if d.get("status") == "unchanged"),
            "failed": sum(1 for d in documents if d.get("status") == "failed"),
            "unsupported": len(unsupported) - len(companions),
            "companions": len(companions),
            "removed_since_last_run": len(dropped),
            "total_chars": sum(int(d.get("chars") or 0) for d in documents),
        },
        "removed_since_last_run": dropped,
        "documents": documents,
        "errors": errors,
    }

    if not args.dry_run:
        K.write_json(P["manifest"], manifest)
        K.write_json(P["unsupported"], {
            "generated": K.now_iso(),
            "count": len(unsupported),
            "files": unsupported,
        })

    if args.json:
        import json

        print(json.dumps({k: v for k, v in manifest.items() if k != "documents"}, indent=2))
    else:
        c = manifest["counts"]
        prefix = "[dry-run] " if args.dry_run else ""
        print(f"{prefix}documents: {c['documents']}  "
              f"new: {c['new']}  changed: {c['changed']}  unchanged: {c['unchanged']}  "
              f"failed: {c['failed']}")
        print(f"{prefix}characters extracted: {c['total_chars']:,}")
        if companions:
            print(f"companions (twin Word document is compiled instead): {len(companions)}")
        if unsupported:
            print(f"\nunsupported ({len(unsupported)}) — reported, not processed:")
            for u in unsupported[:25]:
                print(f"  - {u['rel_path']}  ({u['reason']})")
            if len(unsupported) > 25:
                print(f"  ... and {len(unsupported) - 25} more (see .kb/unsupported.json)")
        if dropped:
            print(f"\ngone from raw_assets since last run ({len(dropped)}):")
            for d in dropped[:25]:
                print(f"  - {d}")
        warned = [d for d in documents if d.get("warnings")]
        if warned:
            print(f"\nwarnings ({len(warned)} documents):")
            for d in warned[:15]:
                print(f"  - {d['rel_path']}: {'; '.join(d['warnings'][:3])}")
        if errors:
            print(f"\nERRORS ({len(errors)}):")
            for e in errors:
                print(f"  - {e['rel_path']}: {e['error']}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
