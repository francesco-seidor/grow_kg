# Knowledge-Graph-Agentic-Setup

A knowledge-base compiler for Claude Code. Point it at a folder of raw documents
and it produces a categorized, linked markdown knowledge graph, a
`wiki/graph.html` d3 visualisation of it, a `wiki/chat.html` router playground,
and a two-layer retrieval router index.

The premise (Karpathy's LLM-wiki pattern): instead of doing RAG over messy raw
files on every question, synthesise the knowledge **once** into clean,
reviewable, self-contained markdown — then reason over that. Compilation is where
the thinking happens; retrieval afterwards is cheap and auditable.

## Quickstart

```bash
# 1. optional but recommended, once — better Word extraction
python3 .claude/skills/knowledge-base/scripts/bootstrap.py

# 2. drop documents into raw_assets/ (any subfolder structure)

# 3. in Claude Code:
/kb-build
```

Then open `wiki/graph.html` in a browser — no server, works offline — or read
the markdown in `wiki/` directly. It reads its data from `wiki/_meta/` beside it,
so keep the folder together; opened on its own, or before a build, it says so and
names the command to run. To ask the knowledge
base questions, open `wiki/chat.html` and paste an Anthropic API key into its
admin panel.

## Folders

```
raw_assets/   input documents (.md .markdown .txt .docx .doc .rtf .xlsx .xlsm .csv) — READ ONLY
.kb/          pipeline state: extraction, digests, taxonomy, validation — disposable
wiki/         the compiled knowledge base — the deliverable, incl. graph.html,
              chat.html and their data under _meta/
exports/      generated distributions of wiki/ (Claude Project) — regenerable
visualizer/   an explainer page for the setup + a portable README for finished wikis
```

`.kb/` and `exports/` sit outside `wiki/` so neither staging state nor a
generated distribution lands in the knowledge base or the viewer. Both are
gitignored — regenerable, but `.kb/` is expensive to rebuild.

## Commands

| Command | Does |
| --- | --- |
| `/kb-build` | Full compile of everything in `raw_assets/` |
| `/kb-update` | Incremental recompile of what changed (sha256-based) |
| `/kb-ask <question>` | Answer from `wiki/` only, routing through the two-layer index |
| `/kb-audit` | Validation, coverage gaps, conflicts, staleness, router readiness |
| `/kb-export-project` | Export `wiki/` as a Claude Project: instruction prompt + knowledge bundles |

All logic lives in the `knowledge-base` skill
([.claude/skills/knowledge-base/SKILL.md](.claude/skills/knowledge-base/SKILL.md)),
which orchestrates six subagents in [.claude/agents/](.claude/agents/).
In **verbatim mode** the writer fan-out is replaced by
`scripts/assemble_verbatim.py`, which keeps every document's text unedited and
only groups it (cluster → topic → document) for retrieval.

## How a build works

Six stages. Scripts do everything mechanical; subagents do the synthesis.

```
0 ingest     kb-ingest      raw_assets/** ──► .kb/extracted/*.md + manifest    script-driven
1 digest     kb-digest ×N   documents ──► .kb/digests/<doc>.json               fan-out
2 architect  kb-architect   topic pool ──► .kb/taxonomy.json                   1 pass (+shards)
3 write      kb-writer ×N   taxonomy ──► wiki/<cluster>/*.md                   fan-out
4 link       kb-linker      edges, hubs, index, router JSON, viewer data       1 pass
5 audit      kb-auditor     validation, conflicts, coverage, changelog         1 pass
```

Stage 1 is the compression step that makes scale possible: after it, nothing
reads whole documents again except the writer, for the nodes that cite them.

Fan-out runs 6 subagents per wave. Rough shape:

| Documents | Digest batches | Architect | Writer batches | Subagent calls |
| --- | --- | --- | --- | --- |
| 10 | 2 | 1 pass | 2–4 | ~8 |
| 100 | 15 | 1 pass | 10–20 | ~40 |
| 1000 | 140 | shards + merge | 60–120 | ~220 |

Above 100 documents the orchestrator stops and asks for confirmation before
fanning out — a 1000-document compile is a real spend and should never be a
surprise.

Runs are resumable: `.kb/state.json` tracks stage progress, and both planners
skip work that is already complete, so an interrupted build picks up where it
stopped.

## What you get in `wiki/`

| Path | What it is |
| --- | --- |
| `<cluster>/<node>.md` | One knowledge node — frontmatter, prose, typed links, cited sources |
| `<cluster>/_cluster.md` | Hub page listing the cluster's nodes |
| `graph.html` | The d3 graph viewer — graph, problems, provenance, offline. A copy of the skill's asset, not generated |
| `chat.html` | Router playground — ask the base questions, tune the router, read the trace. A copy too |
| `_meta/graph-data.js` | The compiled graph the viewer loads — regenerated every build |
| `_meta/chat-data.js` | The whole corpus the playground answers from — regenerated every build |
| `index.md` | Root index of the knowledge base |
| `_meta/router/*.json` | The two-layer router index (layer 1 categories → layer 2 nodes) |
| `_meta/provenance.md` | Which source documents made it in, and where |
| `_meta/conflicts.md` | Every open `⚠️ Conflict` callout, collected |
| `_meta/changelog.md` | What changed across runs |

## Formats

Markdown, plain text, Word and spreadsheets (`.xlsx` `.xlsm` `.csv`, read by the
dependency-free `scripts/xlsx2md.py`: one `## Sheet:` table per worksheet, no cell is ever truncated; a long value
repeated across rows is written once in a `### Shared values` legend and cells
reference it as `[[Vn]]`, which loses nothing). A spreadsheet sitting beside a Word document of the same name (SAP
ships test scripts as both) is a *companion*: reported in `unsupported.json`, not
compiled twice — `extract.py --no-companions` overrides. **PDF and PowerPoint are
out of scope** — they are reported as unsupported rather than silently skipped.
Convert to `.docx` or `.md` to include one.

`bootstrap.py` creates `.kb/venv` with `mammoth` (preserves Word heading styles)
and `pyyaml`. Without it, extraction falls back to a bundled dependency-free docx
reader that keeps headings, lists and tables but loses inline bold/italic.

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

## Graph viewer

`wiki/graph.html` is **not** regenerated on every build — it is a verbatim copy
of `.claude/skills/knowledge-base/assets/graph-viewer.html`, installed by
`init_wiki.py`. What is regenerated is `wiki/_meta/graph-data.js`, which carries
the whole graph plus the build's own findings — open conflicts, validation
errors, coverage gaps — so the compile result is reviewable in one place.

Splitting them means a 400KB page stops being rewritten on every compile, and a
viewer fix ships without recompiling anything. The page loads its data and d3 as
classic `<script src>` siblings rather than fetching them, because browsers block
`fetch()` from a `file://` page and a script tag still works — that is what keeps
double-click opening alive.

d3 is copied into `wiki/_meta/vendor/` from a vendored file, sha256-verified on
the way, so the page works with no network. Fetch it once (committed, pinned):

```bash
mkdir -p .claude/skills/knowledge-base/assets/vendor
curl -fsSL https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js \
  -o .claude/skills/knowledge-base/assets/vendor/d3.v7.min.js
```

Without it the page falls back to the d3 CDN and needs the network —
`validate.py` reports the missing copy as a warning. `wiki/_meta/vendor/` is
gitignored, since committing it would duplicate a dependency the repo already
carries: after a fresh clone, run `/kb-build` (or `init_wiki.py` alone) once to
restore it.

Wikilinks, tags and callouts remain Obsidian-compatible, so opening `wiki/` as a
vault still works; the pipeline just no longer generates `.obsidian/` or
`*.canvas`.

## Router playground

`wiki/chat.html` is the other viewer — a chat window over this knowledge base,
plus an admin panel for every parameter the router actually depends on. Like the
graph it is a copy; its corpus lives in `wiki/_meta/chat-data.js`, which is where
the size goes, since node bodies are never truncated there.
Double-click it, paste an Anthropic API key into the panel, and ask.

It exists because the router has no scorer. `/kb-ask` says "score the categories,
keep the runners-up, have a floor" — but how many clusters layer 1 keeps, how
many nodes layer 2 keeps, what the floor is and which model does the scoring are
all unspecified, so there is nothing to tune. The playground makes them real:

- **Three retrieval modes** — the two-layer router, a flat one-shot over every
  node description, and a BM25 keyword baseline that costs nothing. The baseline
  is the point: if BM25 beats the LLM router on your vault, that is the finding.
- **Separate floors for layer 1 and layer 2**, applied in the page after the
  model returns scores — never by the model, so changing a floor never means
  re-prompting.
- **A per-layer model**, so a cheap router can feed an expensive answer.
- **A trace under every answer** — what scored what and why, what was cut and
  why, tokens, cache hits, latency, cost, and the exact prompt sent, with a copy
  button.
- **A diagnosis on every refusal**, saying whether the gap is missing content or
  two descriptions that overlap. Those need different fixes, and it is the only
  thing here that improves the wiki rather than just querying it.

Settings and named presets live in the browser's local storage; **Export
settings** writes them to a file, and **Export for /kb-ask** emits the tuned
numbers as a block to paste into `.claude/commands/kb-ask.md`. The API key is
kept in memory for the session unless you tick "remember", and is never written
into the generated page or an exported settings file.

The Anthropic JS SDK is inlined from a vendored bundle, so the page needs no npm
and no server. Rebuild the bundle only when bumping the SDK:

```bash
npm i @anthropic-ai/sdk@0.124.0 esbuild
npx esbuild --bundle --format=iife --global-name=AnthropicSDK \
  --platform=browser --target=es2020 --minify \
  --outfile=.claude/skills/knowledge-base/assets/vendor/anthropic-sdk.browser.js entry.js
shasum -a 256 .claude/skills/knowledge-base/assets/vendor/anthropic-sdk.browser.js
```

where `entry.js` is `export * from "@anthropic-ai/sdk";`. Details and the full
knob reference: `.claude/skills/knowledge-base/references/chat-playground.md`.

## Gate

```bash
python3 .claude/skills/knowledge-base/scripts/validate.py
```

Exits 1 on errors. Errors mean the knowledge base or its router index is broken;
warnings are worth attention but not blocking.

## Taking a wiki elsewhere

A compiled `wiki/` is portable. Copy it into another project together with
[visualizer/knowledge_graph.md](visualizer/knowledge_graph.md) — that document
tells any Claude session how to route and answer from the wiki with no `.claude/`
setup at all. To *compile*, *update* or *audit* a wiki you also need this
project's `.claude/` folder, which is designed to be copy-pasted as-is.

[visualizer/index.html](visualizer/index.html) is a standalone page explaining the
whole setup — open it in a browser. It is hand-maintained with no build step, so
it is kept current as part of any change to `.claude/` (CLAUDE.md §Keeping the
explainer in sync) and gated by:

```bash
python3 visualizer/check.py
```

which fails when the page's agents, commands, scripts or invariants no longer
match the repo, or when a click in it would resolve to nothing.

## Scripts

Run from the project root; all accept `--root DIR` or `$KB_ROOT`.

```bash
S=.claude/skills/knowledge-base/scripts

python3 $S/bootstrap.py --check          # what extraction fidelity is available
python3 $S/extract.py [--force]          # stage 0
python3 $S/plan_batches.py digest        # stage 1 plan
python3 $S/aggregate_topics.py           # stage 2 input
python3 $S/plan_batches.py writer        # stage 3 plan
python3 $S/init_wiki.py                  # wiki/ skeleton + _meta stubs + the viewers
python3 $S/build_router_index.py         # the two-layer router index
python3 $S/build_graph_data.py           # wiki/_meta/graph-data.js — the viewer's data
python3 $S/build_chat_data.py            # wiki/_meta/chat-data.js — the playground's corpus
python3 $S/build_project_export.py       # exports/claude-project/ — on demand
python3 $S/validate.py                   # gate: exits 1 on errors
```
