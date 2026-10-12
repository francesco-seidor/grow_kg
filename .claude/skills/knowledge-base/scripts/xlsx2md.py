#!/usr/bin/env python3
"""Dependency-free spreadsheet reader: .xlsx / .xlsm / .csv -> markdown.

Each worksheet becomes a `## Sheet: <name>` section holding one markdown table.
Empty rows and columns are dropped, cells with line breaks keep them as <br>,
dates are rendered ISO from their number format, formulas contribute their cached
value. Nothing is truncated: a large sheet is a large section, and the digest
stage already reads oversized documents in parts.

Reads the OOXML zip directly (zipfile + ElementTree), so it works without the
.kb/venv — same stance as the bundled docx fallback in extract.py.
"""

import csv
import datetime
import html
import io
import posixpath
import re
import zipfile
import xml.etree.ElementTree as ET

M = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PR = "{http://schemas.openxmlformats.org/package/2006/relationships}"

BUILTIN_DATE_FMTS = set(range(14, 23)) | set(range(45, 48))
EPOCH = datetime.datetime(1899, 12, 30)


def col_index(ref):
    letters = re.match(r"[A-Za-z]+", ref).group(0).upper()
    n = 0
    for ch in letters:
        n = n * 26 + ord(ch) - 64
    return n - 1


MAX_CELL_CHARS = None  # no cap by default: the full text of every cell is kept
INTERN_MIN = 300  # a cell this long that repeats within a sheet is stored once (lossless)
TAG_RE = re.compile(r"</?(?:h[1-6]|p|div|br|li|ul|ol|table|tr|td|th|span|b|i|u|strong|em|a)\b[^>]*>", re.I)
_stats = {"truncated": 0}


def cell_text(value, limit=None):
    """Normalise one cell. `limit` caps its length: SAP catalogs carry cells that
    are 27k-char comma lists, and a marker with the true length beats a silent cut."""
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    if TAG_RE.search(value):  # cells that hold HTML (e.g. test-script instructions)
        value = re.sub(r"</(?:h[1-6]|p|div|li|tr)>|<br\s*/?>", "\n", value, flags=re.I)
        value = html.unescape(TAG_RE.sub("", value))
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r"\n\s*\n+", "\n", value).strip()
    if limit and len(value) > limit:
        _stats["truncated"] += 1
        value = value[:limit].rstrip() + f" [… cell truncated, {len(value):,} chars in source]"
    return value.replace("|", "\\|").replace("\n", "<br>")


def fmt_number(raw):
    try:
        f = float(raw)
    except ValueError:
        return raw
    if f == int(f) and abs(f) < 1e15:
        return str(int(f))
    return repr(f) if "e" in raw.lower() else raw


def is_date_format(code):
    code = re.sub(r'"[^"]*"|\[[^\]]*\]|\\.', "", code or "").lower()
    return bool(re.search(r"[dmyhs]", code)) and "general" not in code


def fmt_date(raw):
    try:
        serial = float(raw)
        dt = EPOCH + datetime.timedelta(days=serial)
    except (ValueError, OverflowError):
        return raw
    if serial == int(serial):
        return dt.strftime("%Y-%m-%d")
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def _si_text(si):
    # rich text runs live in <r><t>; phonetic hints (<rPh>) are not content
    parts = []
    for node in si:
        if node.tag == M + "t":
            parts.append(node.text or "")
        elif node.tag == M + "r":
            t = node.find(M + "t")
            parts.append((t.text or "") if t is not None else "")
    return "".join(parts)


def _shared_strings(zf):
    try:
        fh = zf.open("xl/sharedStrings.xml")
    except KeyError:
        return []
    out = []
    for _, el in ET.iterparse(fh, events=("end",)):
        if el.tag == M + "si":
            out.append(_si_text(el))
            el.clear()
    return out


def _date_styles(zf):
    """Set of cellXfs indexes whose number format is a date/time."""
    try:
        root = ET.parse(zf.open("xl/styles.xml")).getroot()
    except KeyError:
        return set()
    custom = {}
    fmts = root.find(M + "numFmts")
    if fmts is not None:
        for nf in fmts:
            custom[int(nf.get("numFmtId"))] = nf.get("formatCode")
    xfs = root.find(M + "cellXfs")
    dates = set()
    if xfs is not None:
        for i, xf in enumerate(xfs):
            fid = int(xf.get("numFmtId") or 0)
            if fid in BUILTIN_DATE_FMTS or (fid in custom and is_date_format(custom[fid])):
                dates.add(i)
    return dates


def _sheets(zf):
    """[(name, state, path)] in workbook order."""
    wb = ET.parse(zf.open("xl/workbook.xml")).getroot()
    rels = {}
    for rel in ET.parse(zf.open("xl/_rels/workbook.xml.rels")).getroot().iter(PR + "Relationship"):
        target = rel.get("Target")
        rels[rel.get("Id")] = target.lstrip("/") if target.startswith("/") else posixpath.normpath(posixpath.join("xl", target))
    out = []
    sheets = wb.find(M + "sheets")
    for s in (sheets if sheets is not None else []):
        path = rels.get(s.get(R + "id"))
        if path:
            out.append((s.get("name") or "Sheet", s.get("state") or "visible", path))
    return out


def _read_sheet(zf, path, shared, date_styles, limit=MAX_CELL_CHARS):
    rows = {}
    with zf.open(path) as fh:
        for _, row in ET.iterparse(fh, events=("end",)):
            if row.tag != M + "row":
                continue
            r_idx = int(row.get("r") or (max(rows) + 2 if rows else 1)) - 1
            cells = {}
            for pos, c in enumerate(row.findall(M + "c")):
                ref = c.get("r")
                ci = col_index(ref) if ref else pos
                t = c.get("t")
                v = c.find(M + "v")
                raw = v.text if v is not None and v.text is not None else ""
                if t == "s":
                    text = shared[int(raw)] if raw.isdigit() and int(raw) < len(shared) else ""
                elif t == "inlineStr":
                    is_ = c.find(M + "is")
                    text = _si_text(is_) if is_ is not None else ""
                elif t == "b":
                    text = "TRUE" if raw == "1" else "FALSE" if raw == "0" else raw
                elif t in ("str", "e"):
                    text = raw
                elif raw:
                    text = fmt_date(raw) if int(c.get("s") or 0) in date_styles else fmt_number(raw)
                else:
                    text = ""
                text = cell_text(text, limit)
                if text:
                    cells[ci] = text
            if cells:
                rows[r_idx] = cells
            row.clear()
    return rows


def intern_repeats(rows):
    """Lossless dedupe of long repeated cells -> (rows, [(label, text)]).

    SAP catalogs repeat the same 20k-char scope-item list on thousands of rows.
    Each distinct long value is written once, in a legend, and the cells carry its
    label — every character survives, the repetition does not."""
    counts = {}
    for r in rows.values():
        for t in r.values():
            if len(t) >= INTERN_MIN:
                counts[t] = counts.get(t, 0) + 1
    shared = [t for t, n in counts.items() if n > 1]
    if not shared:
        return rows, []
    labels = {t: f"V{i + 1}" for i, t in enumerate(shared)}
    out = {ri: {c: (f"[[{labels[t]}]]" if t in labels else t) for c, t in r.items()}
           for ri, r in rows.items()}
    return out, [(labels[t], t) for t in shared]


def rows_to_table(rows):
    """rows: {row_idx: {col_idx: text}} -> markdown table (or paragraphs if 1 column)."""
    if not rows:
        return ""
    cols = sorted({c for r in rows.values() for c in r})
    remap = {c: i for i, c in enumerate(cols)}
    grid = []
    for r in sorted(rows):
        line = [""] * len(cols)
        for c, t in rows[r].items():
            line[remap[c]] = t
        grid.append(line)
    if len(cols) == 1:
        return "\n\n".join(line[0].replace("<br>", "\n") for line in grid)
    width = len(cols)
    out = ["| " + " | ".join(grid[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    out += ["| " + " | ".join(line) + " |" for line in grid[1:]]
    return "\n".join(out)


def xlsx_to_markdown(path, title, limit=MAX_CELL_CHARS):
    """-> (markdown, warnings). Raises on a file that is not a workbook."""
    warnings = []
    _stats["truncated"] = 0
    with zipfile.ZipFile(path) as zf:
        if "xl/workbook.xml" not in zf.namelist():
            raise RuntimeError("not a spreadsheet (missing xl/workbook.xml)")
        shared = _shared_strings(zf)
        date_styles = _date_styles(zf)
        sheets = _sheets(zf)
        parts = [f"# {title}"]
        empty = []
        for name, state, spath in sheets:
            try:
                rows = _read_sheet(zf, spath, shared, date_styles, limit)
            except KeyError:
                warnings.append(f"sheet '{name}' part missing from the file")
                continue
            if not rows:
                empty.append(name)
                continue
            heading = f"## Sheet: {name}"
            if state != "visible":
                heading += f" ({state})"
            rows, legend = intern_repeats(rows)
            section = heading + "\n\n" + rows_to_table(rows)
            if legend:
                section += ("\n\n### Shared values\n\nLong cell values that repeat in this sheet are written "
                            "once here; a cell reading `[[Vn]]` holds the full text of `Vn`.\n\n"
                            + "\n".join(f"- **V{lb[1:]}** — {t}" for lb, t in legend))
            parts.append(section)
        if empty:
            parts.append("*Empty sheets: " + ", ".join(empty) + "*")
        if len(parts) == 1:
            warnings.append("workbook has no cell content")
        if _stats["truncated"]:
            warnings.append(f"{_stats['truncated']} cell(s) longer than {limit} chars were truncated (marked in place); full text is in the source file")
    return "\n\n".join(parts), warnings


def csv_to_markdown(path, title, limit=MAX_CELL_CHARS):
    _stats["truncated"] = 0
    with open(path, "rb") as fh:
        data = fh.read()
    text = data.decode("utf-8-sig", "replace")
    try:
        dialect = csv.Sniffer().sniff(text[:8192], delimiters=",;\t|")
    except csv.Error:
        dialect = csv.excel
    csv.field_size_limit(1 << 24)
    rows = {}
    for i, rec in enumerate(csv.reader(io.StringIO(text), dialect)):
        cells = {j: cell_text(v, limit) for j, v in enumerate(rec) if v.strip()}
        if cells:
            rows[i] = cells
    body = rows_to_table(rows)
    warnings = [] if body else ["file has no content"]
    if _stats["truncated"]:
        warnings.append(f"{_stats['truncated']} cell(s) longer than {limit} chars were truncated (marked in place)")
    return f"# {title}\n\n{body}" if body else f"# {title}", warnings
