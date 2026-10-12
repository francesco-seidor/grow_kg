---
name: knowledge-base
description: Compile a folder of raw documents (raw_assets/) into a durable, categorized markdown knowledge base in wiki/ — nodes, clusters and typed edges, browsable as markdown, visualised as an offline d3 HTML graph, queryable through an offline chat page with a tunable router, and indexed for a two-layer retrieval router. Then answer questions grounded only in the compiled wiki, and audit it for gaps, conflicts and staleness. Use this whenever the user wants to build, rebuild, update, query or audit a knowledge base / internal wiki / policy base / documentation graph from a pile of Markdown or Word documents, following Andrej Karpathy's LLM-wiki pattern (synthesise knowledge once into reviewable markdown, then reason over that instead of doing live RAG over raw files). Scales from 10 documents to 1000 by fanning out over subagents. Trigger it even when the user does not say "wiki" — e.g. "turn raw_assets into a knowledge base", "compile these policies", "build me a knowledge graph from these docs", "what does our knowledge base say about X", "audit the wiki".
---

# Knowledge Base Compiler

Compiles `raw_assets/` into `wiki/`: a knowledge **graph** of markdown **nodes**,
grouped into **clusters** (categories), joined by typed **edges**, with a
machine-readable index for a two-layer retrieval router. `wiki/graph.html` is
the page for exploring the result — the graph itself, plus everything wrong with
it, read from `wiki/_meta/graph-data.js` beside it. `wiki/chat.html` is a second
one for querying it: a
chat window over the base with every router parameter exposed, and a trace of
how each answer was routed.

The premise (Karpathy's LLM-wiki pattern): instead of retrieving over messy raw
documents on every question, synthesise the knowledge **once** into clean,
reviewable, self-contained markdown, and reason over that. Compilation is where
the thinking happens; retrieval afterwards is cheap and auditable.

```
raw_assets/   .md .markdown .txt .docx .doc .rtf .xlsx .xlsm .csv — input, never modified
.kb/          pipeline state, extraction, digests   — staging, outside wiki/
wiki/         the knowledge base                    — the deliverable
```

## Pipeline

Six stages. Scripts do everything mechanical; subagents do the synthesis.

```
0 ingest     kb-ingest      raw_assets/** ──► .kb/extracted/*.md + manifest    script-driven
1 digest     kb-digest ×N   documents ──► .kb/digests/<doc>.json               fan-out
2 architect  kb-architect   topic pool ──► .kb/taxonomy.json                   1 pass (+shards)
3 write      kb-writer ×N   taxonomy ──► wiki/<cluster>/*.md                   fan-out
4 link       kb-linker      edges, hubs, index, router JSON, graph data         1 pass
5 audit      kb-auditor     validation, conflicts, coverage, changelog         1 pass
```

Stage 1 is the compression step that makes scale possible: after it, nothing
reads whole documents again except the writer for the nodes that cite them.

**References** (read the relevant one before acting, don't guess):

| File | When |
| --- | --- |
| `references/pipeline.md` | Orchestrating a run: state, batching, waves, resume, incremental rules, full script reference |
| `references/node-format.md` | Anything about node structure, frontmatter, edges, conflicts |
| `references/router-index.md` | Anything about the router index or its consumers |
| `references/wiki-format.md` | Wiki layout, links, tags, callouts, the graph viewer |
| `references/claude-project-export.md` | Exporting the base into a Claude Project |

## Mode 1: Build

Full compile. Triggered by "build the knowledge base", "compile raw_assets", or a
first run.

**Before starting**, verify `raw_assets/` exists and has files. If it does not,
say so and stop — do not invent content or create placeholder documents.

### Stage 0 — ingest

Run `kb-ingest`. Then read its report: if extraction is degraded or a significant
share of documents failed, surface that to the user **now** rather than compiling
a knowledge base on broken text.

### Cost guardrail

```bash
python3 .claude/skills/knowledge-base/scripts/plan_batches.py digest
```

Report documents, characters, batch count and wave count. **Above 100 documents,
stop and ask the user to confirm before fanning out.** A 1000-document compile is
a real spend and must never be a surprise.

### Stage 1 — digest (fan-out)

Read `.kb/batches/digest-batches.json`. Launch one `kb-digest` per batch, **one
wave at a time** (all batches with the same `wave` value in a single message, as
parallel tool calls — default 6). Put the batch entry in each prompt — `batch_id`
plus every document's `doc_id`, `extracted_path`, `chars` and any `segment` — so
the agent never has to look itself up in the plan: `kb-digest` has no shell,
because inline Python (`python3 -c`, even one line) stops at approval prompts
that allow rules do not silence. Agents that keep a shell run script files only. After each wave, parse every new digest as JSON (re-run a batch whose
file does not load), update `.kb/state.json` and
verify the digest files landed:

```bash
ls .kb/digests | wc -l
```

If a batch produced nothing, retry it once, then report and continue. One failed
batch must not sink the run.

Documents over 250k chars arrive as **segment batches** (one agent per slice, each
reading its whole slice). After the last wave run
`python3 .claude/skills/knowledge-base/scripts/merge_digest_parts.py`; it folds the
parts into `.kb/digests/<doc_id>.json` and lists any document with a missing part —
re-run those segments before Stage 2. Digest agents read every character they are
given; a report that admits skimming is a failed batch, re-run it.

### Stage 2 — architect

```bash
python3 .claude/skills/knowledge-base/scripts/aggregate_topics.py
```

- Single pool → one `kb-architect` pass over `.kb/topic-pool.json`.
- Sharded (the script says so) → one `kb-architect` per `.kb/shards/pool-NN.json`
  in shard mode, then one more in **merge mode**.

Then read `.kb/taxonomy.json` yourself and sanity-check it before spending the
writer budget: 5–15 clusters, 5–40 nodes each, no two cluster descriptions that
could be swapped without anyone noticing, every document assigned or explicitly
listed in `unassigned_topics`. Fix or re-run before proceeding — a bad taxonomy
costs the entire writer stage.

For large or high-stakes corpora, show the user the cluster list with descriptions
and node counts before writing. It is the cheapest possible review point.

### Stage 3 — write (fan-out)

```bash
python3 .claude/skills/knowledge-base/scripts/plan_batches.py writer
```

Launch one `kb-writer` per batch, one wave at a time. Batches never span
clusters, so waves are safe to parallelise. Update `.kb/state.json` per wave.

#### Verbatim mode (no writers)

When the user wants the documents kept exactly as they are — grouped for
retrieval, never rewritten — replace Stages 3 and 4's judgement work with one
script:

```bash
S=.claude/skills/knowledge-base/scripts
python3 $S/merge_digest_parts.py
python3 $S/init_wiki.py
python3 $S/assemble_verbatim.py        # nodes, hubs, index.md — no subagents
python3 $S/build_router_index.py
python3 $S/validate.py || true
python3 $S/build_graph_data.py
python3 $S/build_chat_data.py
python3 $S/validate.py
```

Each node is the verbatim extracted text of one source document; documents over
250k chars become one node per digest segment. The taxonomy still decides the
structure: clusters are layer 1, its nodes become **topics** (a section of the
cluster hub, a `topic/` tag and a keyword on every member), and each document
sits under the topic(s) that cite it. Descriptions and keywords come from the
digests, so every document must be digested and placed in the taxonomy first —
the script lists anything unplaced. `references/node-format.md` §Verbatim nodes
has the page contract. It costs no subagent tokens; the price is size —
`chat-data.js` carries every body in full.

### Stage 4 — link

Run `kb-linker` once. It resolves edges, rebuilds hubs and the root index, and
generates the router index and the graph viewer.

### Stage 5 — audit

Run `kb-auditor` once. Report its findings verbatim — especially documents that
reached no node, open conflicts, and failed router traces.

### Final report

```
KNOWLEDGE BASE COMPILED

Sources:    <n> documents (<n> unsupported, <n> failed)
Structure:  <n> clusters, <n> nodes, <n> typed edges
Router:     _meta/router/categories.json (<n> categories) + <n> layer-2 indexes
Viewer:     wiki/graph.html (open in a browser — works offline; keep _meta/ with it)

Open conflicts:     <n>  → wiki/_meta/conflicts.md
Uncovered docs:     <n>  → wiki/_meta/provenance.md
Validation:         <n> errors, <n> warnings

Needs a human decision:
  - <items>
```

## Mode 2: Update (incremental)

Triggered by "update the wiki", "I added documents", "recompile".

Same pipeline, less work. `references/pipeline.md` §Incremental update has the
full rules; the essentials:

1. `kb-ingest` — sha256 marks documents `new` / `changed` / `unchanged`.
2. If nothing changed, say so and stop. Do not recompile for appearances.
3. Digest only new and changed documents (the planner defaults to this).
4. `aggregate_topics.py` — always full; the pool must reflect the whole corpus.
5. `kb-architect` in **incremental mode**: place new material into existing
   clusters. **Never renumber or rename an existing cluster** — that breaks every
   `id`, wikilink and router path. Structural changes get proposed, not applied,
   unless the user authorised them.
6. `plan_batches.py writer --clusters <affected>` — rewrite only affected nodes.
7. `kb-linker` and `kb-auditor` in full: cheap, scripted, and the router index
   must reflect the final state.

Documents that vanished from `raw_assets/` appear in
`manifest.removed_since_last_run`. Nodes citing them are **never** auto-deleted —
report them for a human decision.

## Mode 3: Query

Triggered by any question the knowledge base should answer.

**Route the way a router would** — this both answers the question and tests the
deliverable:

1. Read `wiki/_meta/router/categories.json`. Pick the best category (keep
   runners-up) from the descriptions.
2. Read that category's `index_path`. Pick the best node(s) from the descriptions.
3. Read the node file and answer from it.

Rules:
- **Answer only from `wiki/`.** Never fall back to `raw_assets/` or `.kb/`. If the
  wiki lacks the answer, the wiki is incomplete — that is a finding, not a licence
  to re-derive from raw sources.
- **Always cite the node path(s)** you answered from.
- **Never fabricate specifics** — no number, date, threshold or entitlement that
  is not in the node.
- If the node carries a `⚠️ Conflict` callout covering the question, present both
  versions and say it is unresolved. Do not pick one.
- If nothing covers it, say so plainly, name the closest nodes, and say what raw
  material would need compiling. Then note whether the gap is missing content or
  a weak description — those need different fixes.
- If routing landed in the wrong category, report that too. It means a description
  needs sharpening, and that is exactly the feedback the compile stage needs.

## Mode 4: Audit

Triggered by "audit the wiki", "is the knowledge base still accurate", or
periodically. Run `kb-auditor` and report its findings. It checks validation,
coverage, conflicts, staleness and router readiness, and fixes only mechanical
defects.

## Mode 5: Export to a Claude Project

Triggered by "put this in a Claude Project", "export the knowledge base",
"I want to use this on claude.ai".

Runs on an already-compiled wiki — it derives entirely from frontmatter, so
nothing about it needs deciding before a build. Full contract in
`references/claude-project-export.md`.

```bash
S=.claude/skills/knowledge-base/scripts
python3 $S/build_router_index.py      # the export mirrors the index — refresh it first
python3 $S/build_project_export.py    # writes exports/claude-project/
```

It emits an instruction prompt carrying the two-layer index plus the routing and
grounding protocol, and one knowledge bundle per cluster with every node
anchored at `## <node-id>`. Wikilinks become node ids and `## Connections`
becomes `type :: id`, so the graph stays traversable somewhere `[[sick-leave]]`
means nothing.

Report the tier, the character count, the files, and the setup steps: paste
`project-instructions.md` into the Project's Instructions, upload everything in
`knowledge/`.

**Say that it is a snapshot.** It must be regenerated after every build or
update, replacing both halves — a stale prompt names nodes that no longer
exist. `--check` exits 1 when an existing export has gone stale.

Not part of the compile: it duplicates the base into a second format, so it runs
on demand, never from `/kb-build`.

## Invariants

These hold in every mode:

- **`raw_assets/` is read-only.** Never modify, move, rename or delete a source.
- **Never fabricate specifics.** Numbers, dates, thresholds, entitlements,
  versions and names come from sources or do not appear.
- **Never silently resolve a conflict.** Flag it in the node, register it in
  `_meta/conflicts.md`, leave the decision to a human.
- **Never delete a node.** Superseded nodes get `status: deprecated`, a
  `superseded-by` edge, and a `[DEPRECATED] ` title prefix.
- **Never silently drop a document.** Every file is compiled, listed as
  unsupported, listed as failed, or reported as uncovered.
- **Never renumber or rename an existing cluster** on an update.
- **Nodes are self-contained.** No "see the attached document" — the reader has
  only the page.
- **Descriptions are load-bearing.** Every node and cluster description is a
  router payload: one sentence, ≤200 chars, saying what questions it answers. If
  two sibling descriptions could be swapped without anyone noticing, the
  taxonomy or the wording is wrong.
- **Prefer many small focused nodes** over few large ones.
- **Generated files are generated.** `_meta/router/*.json`,
  `_meta/graph-data.js`, `_meta/chat-data.js` and everything under `exports/` are
  rebuilt from frontmatter; fix the frontmatter, never the generated file.
  `graph.html` and `chat.html` are neither generated nor yours to edit: they are
  copies of `assets/*-viewer.html`, and `init_wiki.py` overwrites them.

## Scripts

Run from the project root; all accept `--root DIR` or `$KB_ROOT`.

```bash
S=.claude/skills/knowledge-base/scripts

python3 $S/bootstrap.py --check          # extraction fidelity available
python3 $S/extract.py [--force]          # stage 0
python3 $S/plan_batches.py digest        # stage 1 plan
python3 $S/merge_digest_parts.py         # stage 1 close: merge per-segment digests
python3 $S/aggregate_topics.py           # stage 2 input
python3 $S/plan_batches.py writer        # stage 3 plan
python3 $S/init_wiki.py                  # wiki/ skeleton + _meta stubs + the viewers
python3 $S/build_router_index.py         # the two-layer router index
python3 $S/build_graph_data.py           # wiki/_meta/graph-data.js — the viewer's data
python3 $S/build_chat_data.py            # wiki/_meta/chat-data.js — the playground's corpus
python3 $S/build_project_export.py       # exports/claude-project/ — for a Claude Project
python3 $S/validate.py                   # gate: exits 1 on errors
```

## Notes

- **Formats**: Markdown, text, Word and spreadsheets (`xlsx2md.py`; same-named
  spreadsheet+Word pairs compile once, the spreadsheet is reported as a companion). PDF and PowerPoint are deliberately
  out of scope — they are reported as unsupported, never silently skipped. To
  include one, convert it to `.docx` or `.md` first.
- **Resume**: `.kb/state.json` tracks stage progress. After an interruption, read
  it, skip `done` stages, and re-run the current stage's planner — planners skip
  completed items.
- **Model choice**: `kb-architect` runs on Opus (taxonomy quality determines
  everything downstream); the fan-out agents run on Sonnet. For a small,
  high-stakes corpus, raising `kb-writer` to Opus in
  `.claude/agents/kb-writer.md` is a reasonable trade.
