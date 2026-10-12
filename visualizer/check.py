#!/usr/bin/env python3
"""Check visualizer/index.html against the setup it claims to describe.

The explainer page is hand-maintained and has no build step, so it drifts
silently: an agent gains a script, a command is added, an invariant is
reworded, and the page still shows last month's pipeline. This is the gate for
that — run it after any change to `.claude/`, the folder contract or the
invariants (CLAUDE.md §Keeping the explainer in sync).

Two kinds of check:

  structure   the page is internally consistent — tags balance, every tab has a
              panel, every clickable data-* attribute and every mermaid node id
              resolves to something in the page's own JS data
  drift       the page agrees with the repo — the agents, commands, scripts and
              invariants it lists are the ones that actually exist

Stdlib only. Exits 1 on errors; warnings are printed but do not fail.
"""

import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "visualizer", "index.html")

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "source", "track", "wbr"}

errors, warnings = [], []


def error(check, msg):
    errors.append((check, msg))


def warn(check, msg):
    warnings.append((check, msg))


# --------------------------------------------------------------- structure

class TagBalance(HTMLParser):
    """Unclosed and mismatched tags. HTMLParser treats <script> content as raw
    data, so the page's JS cannot confuse it."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            error("html", f"stray </{tag}> at line {self.getpos()[0]}")
            return
        if self.stack[-1][0] != tag:
            open_tag, (line, _) = self.stack[-1]
            error("html", f"</{tag}> at line {self.getpos()[0]} closes "
                          f"<{open_tag}> opened at line {line}")
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    return
        else:
            self.stack.pop()


def check_html(src):
    p = TagBalance()
    p.feed(src)
    for tag, (line, _) in p.stack:
        error("html", f"<{tag}> opened at line {line} is never closed")


def check_tabs(src):
    buttons = re.findall(r'data-tab="([a-z-]+)"', src)
    panels = re.findall(r'id="panel-([a-z-]+)"', src)
    m = re.search(r"const TABS = \[(.*?)\];", src)
    declared = re.findall(r'"([a-z-]+)"', m.group(1)) if m else []

    if not m:
        error("tabs", "no TABS array found")
    if buttons != panels:
        error("tabs", f"tab buttons {buttons} do not match panels {panels}")
    if declared and buttons != declared:
        error("tabs", f"tab buttons {buttons} do not match the TABS array "
                      f"{declared} — a tab missing from TABS falls back to "
                      f"'simple' and is unreachable by #hash")


def check_flows(src):
    buttons = set(re.findall(r'data-flow="([a-z-]+)"', src)) - {"all"}
    sections = set(re.findall(r'data-flowsection="([a-z-]+)"', src))
    for orphan in sorted(sections - buttons):
        error("flows", f"flow section '{orphan}' has no filter button")
    for orphan in sorted(buttons - sections):
        error("flows", f"flow button '{orphan}' selects nothing")


def js_data(src):
    """The page's own data objects, by key."""
    agents = set(re.findall(r'^  "(kb-[a-z]+)":\{', src, re.M))
    scripts = set(re.findall(r'^  "([a-z_0-9]+\.py)":\[', src, re.M))
    files = set(re.findall(r'\{id:"([a-z0-9-]+)"', src))
    return agents, scripts, files


def check_data_attrs(src, agents, scripts, files):
    for attr, keys, label in (("data-agent", agents, "AGENTS"),
                              ("data-script", scripts, "SCRIPTS"),
                              ("data-file", files, "FILES")):
        used = set(re.findall(attr + r'="([^"${}]+)"', src))   # skip templates
        for missing in sorted(used - keys):
            error("clicks", f'{attr}="{missing}" resolves to nothing in {label}'
                            f" — the click opens no drawer and reports no error")


def check_mermaid_ids(src, agents, scripts, files):
    """Mermaid node ids are the click routing: A_<agent>, S_<script>,
    F_<file id with hyphens stripped> (see kbNode + FILE_BY_MERMAID)."""
    start = src.find("const DIAGRAMS = {")
    end = src.find("/* ============================ drawer")
    if start < 0 or end < 0:
        warn("mermaid", "could not locate the DIAGRAMS block — skipped")
        return
    block = src[start:end]
    by_mermaid = {"F_" + f.replace("-", ""): f for f in files}
    for node in sorted(set(re.findall(r"\b([ASF]_[A-Za-z0-9_]+)\b", block))):
        bare = node[2:].split("__")[0]
        if node.startswith("A_") and "kb-" + bare not in agents:
            error("mermaid", f"node {node} → no agent 'kb-{bare}'")
        elif node.startswith("S_") and bare + ".py" not in scripts:
            error("mermaid", f"node {node} → no script '{bare}.py' "
                             f"(the id must be the filename without .py)")
        elif node.startswith("F_") and node not in by_mermaid:
            error("mermaid", f"node {node} → no file id "
                             f"'{node[2:]}' with hyphens stripped")


# ------------------------------------------------------------------- drift

def check_agents(agents):
    d = os.path.join(ROOT, ".claude", "agents")
    if not os.path.isdir(d):
        warn("agents", ".claude/agents/ not found — skipped")
        return
    on_disk = {f[:-3] for f in os.listdir(d) if f.endswith(".md")}
    for missing in sorted(on_disk - agents):
        error("agents", f"{missing} exists in .claude/agents/ but the page "
                        f"does not describe it")
    for extra in sorted(agents - on_disk):
        error("agents", f"the page describes agent '{extra}', which no longer "
                        f"exists in .claude/agents/")


def check_commands(src):
    d = os.path.join(ROOT, ".claude", "commands")
    if not os.path.isdir(d):
        warn("commands", ".claude/commands/ not found — skipped")
        return
    on_disk = {f[:-3] for f in os.listdir(d) if f.endswith(".md")}
    named = set(re.findall(r'class="cmdname">/([a-z-]+)', src))
    for missing in sorted(on_disk - named):
        error("commands", f"/{missing} exists in .claude/commands/ but has no "
                          f"card in the Overview panel")
    for extra in sorted(named - on_disk):
        error("commands", f"the page documents /{extra}, which no longer "
                          f"exists in .claude/commands/")

    flows = set(re.findall(r'data-flowsection="([a-z-]+)"', src))
    for cmd in sorted(on_disk):
        key = cmd[3:] if cmd.startswith("kb-") else cmd
        if key not in flows and key.split("-")[0] not in flows:
            warn("commands", f"/{cmd} has no workflow section in the "
                             f"Workflows panel")


def check_scripts(scripts):
    d = os.path.join(ROOT, ".claude", "skills", "knowledge-base", "scripts")
    if not os.path.isdir(d):
        warn("scripts", "skill scripts/ not found — skipped")
        return
    on_disk = {f for f in os.listdir(d) if f.endswith(".py")}
    for missing in sorted(on_disk - scripts):
        error("scripts", f"{missing} exists but is missing from the "
                         f"Scripts table")
    for extra in sorted(scripts - on_disk):
        error("scripts", f"the page lists {extra}, which no longer exists")


def normalise(text):
    """Compare invariants on words, not on markdown emphasis or code ticks."""
    text = re.sub(r"[`*_]", "", text)
    text = text.replace("**", "").replace("—", "-").replace("–", "-")
    return " ".join(text.lower().split()).rstrip(".")


def check_invariants(src):
    claude_md = os.path.join(ROOT, "CLAUDE.md")
    if not os.path.isfile(claude_md):
        warn("invariants", "CLAUDE.md not found — skipped")
        return
    body = open(claude_md, encoding="utf-8").read()
    m = re.search(r"\n## Invariants\n(.*?)(?=\n## )", body, re.S)
    if not m:
        warn("invariants", "no §Invariants section in CLAUDE.md — skipped")
        return
    # one entry per top-level bullet, continuation lines folded in
    entries, current = [], None
    for line in m.group(1).splitlines():
        if line.startswith("- "):
            if current:
                entries.append(current)
            current = line[2:].strip()
        elif line.startswith("  ") and current:
            current += " " + line.strip()
        elif not line.strip() and current:
            entries.append(current)
            current = None
    if current:
        entries.append(current)

    # scanned line by line rather than with one regex: a non-greedy match to
    # `];` runs into the next array whenever the closing bracket is indented
    lines = src.splitlines()
    try:
        start = next(i for i, ln in enumerate(lines)
                     if ln.startswith("const INVARIANTS = ["))
    except StopIteration:
        error("invariants", "no INVARIANTS array in the page")
        return
    page = []
    for ln in lines[start + 1:]:
        if ln.strip().startswith("];"):
            break
        entry = re.match(r'\s*"(.*)",?\s*$', ln)
        if entry:
            page.append(entry.group(1))
        elif ln.strip():
            error("invariants", f"unparsable line in INVARIANTS: {ln.strip()}")
    else:
        error("invariants", "INVARIANTS array is never closed")

    want, have = [normalise(e) for e in entries], [normalise(p) for p in page]
    if len(want) != len(have):
        error("invariants", f"CLAUDE.md lists {len(want)} invariants, the page "
                            f"lists {len(have)}")
    for w in want:
        if w not in have:
            error("invariants", f"missing from the page: \"{w[:90]}…\""
                  if len(w) > 90 else f'missing from the page: "{w}"')
    for h in have:
        if h not in want:
            error("invariants", f"on the page but not in CLAUDE.md: "
                                f"\"{h[:90]}…\"" if len(h) > 90 else
                                f'on the page but not in CLAUDE.md: "{h}"')


# -------------------------------------------------------------------- main

def main():
    if not os.path.isfile(PAGE):
        print(f"visualizer/index.html not found at {PAGE}")
        return 1
    src = open(PAGE, encoding="utf-8").read()

    check_html(src)
    check_tabs(src)
    check_flows(src)
    agents, scripts, files = js_data(src)
    check_data_attrs(src, agents, scripts, files)
    check_mermaid_ids(src, agents, scripts, files)
    check_agents(agents)
    check_commands(src)
    check_scripts(scripts)
    check_invariants(src)

    for level, items in (("warning", warnings), ("error", errors)):
        for check, msg in items:
            print(f"{level:8} {check:11} {msg}")

    print(f"\nvisualizer/index.html — {len(errors)} errors, "
          f"{len(warnings)} warnings "
          f"({len(agents)} agents, {len(scripts)} scripts, "
          f"{len(files)} generated files described)")
    if errors:
        print("the explainer has drifted from the setup — see "
              "CLAUDE.md §Keeping the explainer in sync")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
