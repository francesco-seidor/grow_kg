# Claude-Agents

A knowledge-base compiler: turns a folder of raw documents into a categorized,
linked markdown knowledge graph, a `wiki/graph.html` d3 viewer, a
`wiki/chat.html` router playground, and a two-layer retrieval router index.

## Folder contract

```
raw_assets/   input documents (.md .markdown .txt .docx .doc .rtf .xlsx .xlsm .csv) — READ ONLY
.kb/          pipeline state: extraction, digests, taxonomy, validation — disposable
wiki/         the compiled knowledge base — the deliverable, incl. graph.html,
              chat.html and their data under _meta/
exports/      generated distributions of wiki/ (Claude Project) — regenerable
visualizer/   index.html, the explainer for this setup, and knowledge_graph.md,
              the portable README that ships next to a finished wiki/
```

Put documents in `raw_assets/` (any subfolder structure) and run `/kb-build`.
Open `wiki/graph.html` in a browser to explore the result — clusters,
connections, contradictions and things to fix, in one page. It reads its data
from `wiki/_meta/` beside it, so keep the folder together; opened before a build
it says so and names the command to run.
Open `wiki/chat.html` to ask it questions and tune the router: it needs an
Anthropic API key, pasted into its admin panel.

## Commands

| Command | Does |
| --- | --- |
| `/kb-build` | Full compile of everything in `raw_assets/` |
| `/kb-update` | Incremental recompile of what changed (sha256-based) |
| `/kb-ask <question>` | Answer from `wiki/` only, routing through the two-layer index |
| `/kb-audit` | Validation, coverage gaps, conflicts, staleness, router readiness |
| `/kb-export-project` | Export `wiki/` as a Claude Project: instruction prompt + knowledge bundles |

All logic lives in the `knowledge-base` skill
(`.claude/skills/knowledge-base/SKILL.md`), which orchestrates six subagents in
`.claude/agents/`: `kb-ingest`, `kb-digest`, `kb-architect`, `kb-writer`,
`kb-linker`, `kb-auditor`.

**Verbatim mode** replaces the writer fan-out and the linker's judgement with
one script, `scripts/assemble_verbatim.py`: every node is the unedited extracted
text of one source document (one node per segment for documents over 250k chars),
grouped into the architect's clusters and topics. Use it when the documents must
stay exactly as they are; SKILL.md §Verbatim mode has the command sequence.

## Invariants

- `raw_assets/` is never modified.
- Never fabricate specifics — numbers, dates, thresholds, entitlements and
  versions come from sources or do not appear.
- Conflicts between sources are flagged, never silently resolved.
- Nodes are never deleted; superseded ones are marked `status: deprecated`.
- No document is silently dropped: everything is compiled, listed as unsupported,
  listed as failed, or reported as uncovered.
- Existing clusters are never renumbered or renamed on an update — that breaks
  every node `id`, wikilink and router path.
- Every node and cluster `description` is a router payload: one sentence, ≤200
  chars, saying what questions it answers.
- `wiki/_meta/router/*.json`, `wiki/_meta/graph-data.js`, `wiki/_meta/chat-data.js`
  and everything under `exports/` are **generated**; `wiki/graph.html`,
  `wiki/chat.html`, `wiki/_meta/chat-app.js` and `wiki/_meta/vendor/*` are verbatim
  copies of `.claude/skills/knowledge-base/assets/`. Never hand-edit either — node
  content comes from frontmatter, viewer behaviour from the assets. Fix the source
  and rebuild.
- Nothing writes markdown into `wiki/` except the compiler — every `.md` under
  the vault (bar `_meta/`) is scanned as a node, so exports live outside it.

## Keeping the explainer in sync

`visualizer/index.html` is the explainer for this whole setup — a single static
page, hand-maintained, with **nothing generating it**. It therefore goes stale
silently, and a stale explainer is worse than none: it describes a pipeline that
no longer exists.

**Any change to `.claude/`, to the folder contract, or to the invariants must be
applied to `visualizer/index.html` in the same change** — not deferred, not
listed as a follow-up. Treat it as part of the edit, the way you would a test.
Update `README.md` and this file too whenever the change is visible at their
level (a new command, a new folder, a changed invariant).

Where each kind of change lands in the page:

| Changed | Update in `visualizer/index.html` |
| --- | --- |
| A command in `.claude/commands/` | the `.cmdgrid` card in the Overview panel, its `.flowsection` in Workflows, and the "things you can ask for" card in Start here |
| An agent in `.claude/agents/` | its entry in the `AGENTS` object (desc, tools, model, fan-out, reads, writes, scripts, hand-off) and, in plain words, its `HELPERS` entry |
| A stage's script chain | the agent's `handoff`/`scripts` fields, the `.floop` step in the affected flow, and the `pipeline` and `sequence` mermaid sources |
| A script in `scripts/` | the `SCRIPTS` object — key is the exact filename, since the drawer looks it up by name |
| `assets/graph-viewer.html` or `assets/chat-viewer.html` | nothing generates these either — they ship as-is into every vault, so the same "hand-maintained, goes stale silently" rules apply. `build_graph_data.py` guards the two mechanical contracts (no leftover `{{TOKEN}}`, `SCHEMA_EXPECTED` matching `kblib.GRAPH_SCHEMA`); the rest is on you |
| A generated file's shape | its entry in `KB_FILES` / `WIKI_FILES` / `EXPORT_FILES` (add `example:` for a JSON payload) |
| The folder contract | the `.contract` boxes in Overview and the "boxes on your computer" cards in Start here |
| An invariant | the `INVARIANTS` array — keep the wording identical to §Invariants above — and, in plain words, the `promises` list |
| `graph.html` viewer behaviour | the `wiki-graph-html` entry in `WIKI_FILES` — presets, force and display controls, hash-persisted view state. The behaviour itself lives in the hand-maintained `assets/graph-viewer.html` |
| `chat.html` router behaviour | the Playground panel: modes, floors, below-floor, diagnosis codes, models, caching, storage |
| The Claude Project export | the export section and `EXPORT_FILES` tree in the Output panel, plus the `/kb-export-project` flow in Workflows |
| A vendored asset under `assets/vendor/` | the Setup section in Overview, and the file's note in `WIKI_FILES` — `init_wiki.py` also copies it into `wiki/_meta/vendor/` |

Two mechanical rules the page depends on, easy to break:

- Mermaid node ids route the click-to-drawer: `A_<agent-without-kb->`,
  `S_<script-without-.py>`, `F_<file-id-with-hyphens-stripped>`. An id that
  does not resolve is a dead click with no error — check any new node against
  `AGENTS`, `SCRIPTS` and the `FILES` map.
- A new tab needs three things in agreement: the `.tabbtn`, the
  `#panel-<name>`, and the name in the `TABS` array.

Verify before reporting done — the page has no build step, so nothing else will:

```bash
python3 visualizer/check.py
```

Exits 1 on drift. It checks tag balance, that tabs/panels/`TABS` agree, that
every `data-agent` / `data-script` / `data-file` and every mermaid node id
resolves (an unresolved one is a dead click with **no** error in the browser),
and that the agents, commands, scripts and invariants the page describes are the
ones that actually exist in `.claude/` and in §Invariants above.

It cannot check prose. Two things to confirm by hand after a change: that the
mermaid sources still render (`npx @mermaid-js/mermaid-cli -i x.mmd -o x.svg` —
a syntax error only surfaces as a fallback message in the browser), and that
what the page *says* about a stage still matches what the agent actually does.

## Setup

Optional but recommended, once:

```bash
python3 .claude/skills/knowledge-base/scripts/bootstrap.py
```

Creates `.kb/venv` with `mammoth` (preserves Word heading styles) and `pyyaml`.
Without it, extraction falls back to a bundled dependency-free docx reader that
keeps headings, lists and tables but loses inline bold/italic.

## Formats

Markdown, plain text, Word and spreadsheets (`.xlsx` `.xlsm` `.csv`, read by the
dependency-free `scripts/xlsx2md.py`: one `## Sheet:` table per worksheet, no cell is ever truncated; a long value
repeated across rows is written once in a `### Shared values` legend and cells
reference it as `[[Vn]]`, which loses nothing). A spreadsheet sitting beside a Word document of the same name (SAP
ships test scripts as both) is a *companion*: reported in `unsupported.json`, not
compiled twice — `extract.py --no-companions` overrides. **PDF and PowerPoint are
out of scope** — they are reported as unsupported rather than silently skipped.
Convert to `.docx` or `.md` to include one.

## Gates

```bash
python3 .claude/skills/knowledge-base/scripts/validate.py   # the knowledge base
python3 visualizer/check.py                                 # the explainer page
```

Both exit 1 on errors. For `validate.py`, errors mean the knowledge base or its
router index is broken; warnings are worth attention but not blocking. For
`check.py`, errors mean `visualizer/index.html` no longer describes this setup —
see §Keeping the explainer in sync.
