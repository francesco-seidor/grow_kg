"""Dependency-free HTML -> Markdown converter.

Covers the tag subset that `mammoth` (docx) and macOS `textutil` (doc/rtf)
actually emit. Unknown tags are transparent: the tag is dropped, its text is
kept. Deliberately stdlib-only so extraction degrades gracefully when no
virtualenv is available.
"""

import re
from html.parser import HTMLParser

VOID = {"br", "hr", "img", "meta", "link", "input", "col", "base", "area"}

# Tags whose content is rendered but which contribute no markup of their own.
TRANSPARENT = {
    "html", "body", "head", "div", "section", "article", "main", "header",
    "footer", "span", "font", "a:p", "o:p", "tbody", "thead", "tfoot",
    "colgroup", "center", "nav", "figure", "abbr", "cite", "small", "label",
}

DROP = {"script", "style", "title", "noscript"}

BLOCK = {
    "p", "div", "section", "article", "h1", "h2", "h3", "h4", "h5", "h6",
    "ul", "ol", "li", "table", "blockquote", "pre", "hr", "figure", "figcaption",
}


class _Node:
    __slots__ = ("tag", "attrs", "children")

    def __init__(self, tag, attrs=None):
        self.tag = tag
        self.attrs = dict(attrs or {})
        self.children = []


class _TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = _Node("#root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        node = _Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(_Node(tag.lower(), attrs))

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in VOID:
            return
        # Close the nearest matching open tag; tolerate unbalanced markup.
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if data:
            self.stack[-1].children.append(data)


def _escape(text, in_table=False):
    text = text.replace("\u00a0", " ")
    if in_table:
        text = text.replace("|", "\\|").replace("\n", " ")
    return text


def _is_ws(s):
    return isinstance(s, str) and not s.strip()


class _Renderer:
    def __init__(self, image_placeholder=True):
        self.image_placeholder = image_placeholder
        self.images = []

    # -- inline ----------------------------------------------------------
    def inline(self, node, in_table=False):
        out = []
        for child in node.children:
            if isinstance(child, str):
                out.append(_escape(re.sub(r"[ \t\r\n]+", " ", child), in_table))
                continue
            t = child.tag
            if t in DROP:
                continue
            inner = self.inline(child, in_table)
            if t in ("strong", "b"):
                out.append(f"**{inner.strip()}**" if inner.strip() else "")
            elif t in ("em", "i"):
                out.append(f"*{inner.strip()}*" if inner.strip() else "")
            elif t in ("s", "strike", "del"):
                out.append(f"~~{inner.strip()}~~" if inner.strip() else "")
            elif t == "code":
                out.append(f"`{inner.strip()}`" if inner.strip() else "")
            elif t == "a":
                href = (child.attrs.get("href") or "").strip()
                label = inner.strip() or href
                if href and not href.lower().startswith("javascript:"):
                    out.append(f"[{label}]({href})")
                else:
                    out.append(label)
            elif t == "br":
                out.append(" " if in_table else "\n")
            elif t == "img":
                name = (
                    child.attrs.get("alt")
                    or child.attrs.get("src", "")[:80]
                    or "unnamed"
                )
                self.images.append(name)
                if self.image_placeholder:
                    out.append(f"<!-- image omitted: {name} -->")
            elif t == "sup":
                out.append(f"^{inner.strip()}" if inner.strip() else "")
            elif t == "sub":
                out.append(f"_{inner.strip()}" if inner.strip() else "")
            else:
                out.append(inner)
        return "".join(out)

    # -- blocks ----------------------------------------------------------
    def blocks(self, node, depth=0):
        parts = []
        for child in node.children:
            if isinstance(child, str):
                if child.strip():
                    parts.append(_escape(re.sub(r"[ \t\r\n]+", " ", child)).strip())
                continue
            parts.extend(self.block(child, depth))
        return parts

    def block(self, node, depth=0):
        t = node.tag
        if t in DROP:
            return []
        if t in ("h1", "h2", "h3", "h4", "h5", "h6"):
            text = self.inline(node).strip()
            return [f"{'#' * int(t[1])} {text}"] if text else []
        if t == "p" or t == "figcaption":
            text = self.inline(node).strip()
            return [text] if text else []
        if t == "hr":
            return ["---"]
        if t == "br":
            return []
        if t == "pre":
            code = self.inline(node).rstrip()
            return [f"```\n{code}\n```"] if code.strip() else []
        if t == "blockquote":
            inner = "\n\n".join(self.blocks(node, depth))
            if not inner.strip():
                return []
            quoted = "\n".join(
                ("> " + ln) if ln else ">" for ln in inner.split("\n")
            )
            return [quoted]
        if t in ("ul", "ol"):
            return [self.render_list(node, depth)] if self.render_list(node, depth) else []
        if t == "table":
            rendered = self.render_table(node)
            return [rendered] if rendered else []
        if t == "img":
            return self.block_from_inline(node)
        if t in TRANSPARENT or t not in BLOCK:
            # Transparent container: recurse, but if it holds no block-level
            # children treat it as one inline run.
            if any(
                isinstance(c, _Node) and (c.tag in BLOCK or c.tag == "table")
                for c in node.children
            ):
                return self.blocks(node, depth)
            return self.block_from_inline(node)
        return self.blocks(node, depth)

    def block_from_inline(self, node):
        text = self.inline(node).strip()
        return [text] if text else []

    def render_list(self, node, depth):
        ordered = node.tag == "ol"
        lines = []
        idx = 1
        for child in node.children:
            if not isinstance(child, _Node):
                continue
            if child.tag in ("ul", "ol"):
                nested = self.render_list(child, depth + 1)
                if nested:
                    lines.append(nested)
                continue
            if child.tag != "li":
                continue
            marker = f"{idx}." if ordered else "-"
            idx += 1
            own = []
            sub = []
            for gc in child.children:
                if isinstance(gc, _Node) and gc.tag in ("ul", "ol"):
                    nested = self.render_list(gc, depth + 1)
                    if nested:
                        sub.append(nested)
                else:
                    holder = _Node("span")
                    holder.children = [gc]
                    own.append(self.inline(holder))
            text = re.sub(r"\s+", " ", "".join(own)).strip()
            pad = "    " * depth
            if text:
                lines.append(f"{pad}{marker} {text}")
            elif sub:
                lines.append(f"{pad}{marker}")
            lines.extend(sub)
        return "\n".join(l for l in lines if l.strip())

    def render_table(self, node):
        rows = []
        caption = ""
        for tr in self._iter_rows(node):
            cells = []
            header = False
            for cell in tr.children:
                if not isinstance(cell, _Node) or cell.tag not in ("td", "th"):
                    continue
                if cell.tag == "th":
                    header = True
                cells.append(re.sub(r"\s+", " ", self.inline(cell, in_table=True)).strip())
            if cells:
                rows.append((header, cells))
        for c in node.children:
            if isinstance(c, _Node) and c.tag == "caption":
                caption = self.inline(c).strip()
        if not rows:
            return ""
        width = max(len(cells) for _, cells in rows)
        rows = [(h, cells + [""] * (width - len(cells))) for h, cells in rows]

        first_is_header = rows[0][0] or (
            len(rows) > 1 and all(c and len(c) < 60 for c in rows[0][1])
        )
        out = []
        if caption:
            out.append(f"*{caption}*")
        head = rows[0][1] if first_is_header else [""] * width
        body = rows[1:] if first_is_header else rows
        out.append("| " + " | ".join(head) + " |")
        out.append("| " + " | ".join("---" for _ in range(width)) + " |")
        for _, cells in body:
            out.append("| " + " | ".join(cells) + " |")
        return "\n".join(out)

    def _iter_rows(self, node):
        for child in node.children:
            if not isinstance(child, _Node):
                continue
            if child.tag == "tr":
                yield child
            elif child.tag in ("tbody", "thead", "tfoot"):
                for sub in self._iter_rows(child):
                    yield sub


def html_to_markdown(html, image_placeholder=True):
    """Convert an HTML string to Markdown. Returns (markdown, image_names)."""
    builder = _TreeBuilder()
    builder.feed(html or "")
    builder.close()
    renderer = _Renderer(image_placeholder=image_placeholder)
    parts = renderer.blocks(builder.root)
    text = "\n\n".join(p for p in parts if p and p.strip())
    return normalize_markdown(text), renderer.images


def normalize_markdown(text):
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u00a0", " ").lstrip("\ufeff")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n" if text.strip() else ""
