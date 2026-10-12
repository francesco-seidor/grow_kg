# Pipeline mechanics

State, batching, resume and incremental rules. Read this before orchestrating a
run; the scale behaviour lives here.

## Directories

```
raw_assets/   input. Never modified, never written to. Any structure.
.kb/          pipeline state. Disposable but expensive to rebuild.
wiki/         output wiki. The deliverable.
exports/      generated distributions of wiki/. Regenerable, never hand-edited.
```

`.kb/` and `exports/` sit **outside** `wiki/` so neither staging state nor a
generated distribution ever lands in the knowledge base or the graph viewer.
Every `.md` under the vault except `_meta/` is scanned as a node, so anything
written inside it would fail validation and pollute the router index.

## `.kb/` contents

| Path | Written by | Contents |
| --- | --- | --- |
| `manifest.json` | `extract.py` | One record per source document: `doc_id`, `rel_path`, `sha256`, `chars`, `method`, `title`, `outline`, `warnings`, `status` |
| `unsupported.json` | `extract.py` | Files skipped by type, with reasons |
| `extracted/<doc_id>.md` | `extract.py` | Normalised markdown, one per document |
| `batches/digest-batches.json` | `plan_batches.py digest` | Digest fan-out plan |
| `batches/writer-batches.json` | `plan_batches.py writer` | Writer fan-out plan |
| `digests/<doc_id>.json` | `kb-digest` | Per-document digest (see below) |
| `topic-pool.json` | `aggregate_topics.py` | Deduped topic pool + document one-liners |
| `shards/pool-NN.json` | `aggregate_topics.py` | Architect shards, large corpora only |
| `taxonomy.json` | `kb-architect` | Clusters and node specs |
| `state.json` | orchestrator | Stage progress and per-item status |
| `validation.json` | `validate.py` | Full issue report |

`status` on a manifest document is one of `new`, `changed`, `unchanged`,
`failed`. It is derived from the sha256 comparison and is what every later stage
filters on.

## `state.json`

```json
{
  "run_id": "2026-09-01T10:22:04Z",
  "mode": "build",
  "stages": {
    "extract":   {"status": "done", "at": "...", "documents": 412},
    "digest":    {"status": "running", "batches_done": ["digest-0001"], "batches_total": 58},
    "architect": {"status": "pending"},
    "writer":    {"status": "pending"},
    "linker":    {"status": "pending"},
    "audit":     {"status": "pending"}
  }
}
```

Stage status: `pending` | `running` | `done` | `failed`. The orchestrator writes
this after each wave, which is what makes a run resumable after an interruption
or a context reset — on restart, read `state.json`, skip `done` stages, and
re-plan the current one (planning is idempotent and skips completed items).

## Digest schema

`kb-digest` writes one file per document to `.kb/digests/<doc_id>.json`:

```json
{
  "doc_id": "hr-leave-policy-2025",
  "title": "Leave Policy 2025",
  "doc_type": "policy",
  "one_line": "Company-wide leave entitlements and request process, effective Jan 2025.",
  "topics": [
    {"label": "parental leave", "weight": "primary", "anchor": "## Parental Leave"},
    {"label": "notice periods", "weight": "secondary", "anchor": "## Notice"}
  ],
  "entities": [{"name": "Workday", "kind": "system"}],
  "key_claims": [
    {"claim": "Parental leave is 26 weeks at full pay after 2 years' service.",
     "anchor": "## Parental Leave"}
  ],
  "dates_versions": ["effective 2025-01-01", "v3.2"],
  "suggested_tags": ["topic/parental-leave", "topic/notice-periods"],
  "conflicts_suspected": ["notice period differs from the employee handbook"],
  "chars": 18432
}
```

Field discipline that makes the later stages work:
- `topics` are the clustering signal. 3–15 per document, `primary` for what the
  document is *about*, `secondary` for what it merely touches. Reuse obvious
  phrasing across documents — the aggregator merges near-duplicates, so
  consistent wording clusters better than creative wording.
- `one_line` is what the architect sees when it cannot afford the whole digest.
- `key_claims` carry `anchor`s so the writer can find the passage again without
  re-reading the whole document.
- `doc_type`: `policy` | `guide` | `reference` | `notes` | `spec` | `report` |
  `faq` | `contract` | `presentation` | `other`.

## Batching

**Digest** (`plan_batches.py digest`): ≤60,000 characters or ≤8 documents per
batch, whichever binds first. A document over the character budget gets its own
batch, marked `oversized` with a `read_in_parts` count — read it with `Read`
`offset`/`limit` rather than in one call.
Above 250,000 characters the document is cut into line-bounded **segments**, one
batch each (`segment: {index,total,start_line,end_line,part_file}`); each agent reads
its whole slice and writes `.kb/digests/parts/<doc_id>.part-NN.json`, and
`merge_digest_parts.py` folds complete sets into `.kb/digests/<doc_id>.json`. Every
digest agent reads all of what it is handed — skimming is a failed batch.

**Writer** (`plan_batches.py writer`): ≤10 nodes or ≤90,000 characters of source
per batch, never spanning clusters. Each batch carries its node specs *and* the
exact list of extracted files those nodes cite, so a writer reads only what it
needs.

**Verbatim mode** skips the writer fan-out: `assemble_verbatim.py` builds every
node from the extracted text itself (one node per document, one per segment for
documents over 250k chars), plus the hubs and `index.md`, from `.kb/taxonomy.json`
and the digests. Re-runs are idempotent; a page a later run no longer produces is
marked `status: deprecated`, never deleted (`.kb/verbatim-written.json` tracks
what was written).

**Waves**: batches are tagged `wave`, 6 per wave by default. Launch one wave per
message (parallel tool calls), wait, record progress, launch the next. Six
concurrent subagents is a balance between throughput and leaving the orchestrator
context room to track results.

Rough shape at different corpus sizes:

| Documents | Digest batches | Architect | Writer batches | Subagent calls |
| --- | --- | --- | --- | --- |
| 10 | 2 | 1 pass | 2–4 | ~8 |
| 100 | 15 | 1 pass | 10–20 | ~40 |
| 1000 | 140 | shards + merge | 60–120 | ~220 |

## Cost guardrail

Before the digest fan-out, report document count, total characters, batch count
and wave count. Above **100 documents**, stop and ask the user to confirm before
launching — a 1000-document compile is a real spend and should never be a
surprise.

## Incremental update

`/kb-update` differs from `/kb-build` only in what it skips:

1. `extract.py` — sha256 against the previous manifest marks each document
   `new` / `changed` / `unchanged`. Only the first two are re-extracted.
2. `plan_batches.py digest` — defaults to `new` + `changed` only. Unchanged
   documents keep their existing digest.
3. `aggregate_topics.py` — always re-run; it is cheap and the pool must reflect
   the whole corpus, not just the delta.
4. `kb-architect` — **incremental mode**: load the existing `taxonomy.json` and
   place new topics into existing clusters where they fit. Only propose new or
   split clusters when something genuinely does not belong, and never renumber or
   rename an existing cluster (that would break every `id`, link and router path).
   Report proposed structural changes for approval rather than applying them.
5. `plan_batches.py writer --clusters <affected>` — rewrite only nodes whose
   sources changed. Untouched nodes keep their `updated` date.
6. Linker and auditor stages — always run in full. They are scripted and cheap,
   and the router index and graph viewer must reflect the final state.

Documents that vanished from `raw_assets/` appear in
`manifest.removed_since_last_run`. Nodes citing them are **not** deleted; they
are reported so a human decides between deprecating and keeping.

## Resume after interruption

```
1. Read .kb/state.json
2. Skip stages marked done
3. Re-run the current stage's planner — it skips items already complete
   and returns only the remainder
4. Continue from there
```

Both planners decide "already complete" by modification time, which makes resume
and incremental fall out of the same rule:

- **digest** — a `.kb/digests/<doc_id>.json` newer than its extracted source is
  done. A re-extracted (changed) document has a newer source, so it re-enters the
  plan automatically.
- **writer** — a node file newer than `.kb/taxonomy.json` is done. A fresh
  taxonomy therefore invalidates the nodes it describes, which is what an
  incremental architect pass should do.

`--redo` on either planner ignores all of that and re-plans everything.

Every stage is safely re-runnable. Nothing appends blindly; everything writes
whole files.

## Failure handling

- **Extraction failure** — recorded as `status: failed` with the error, reported,
  pipeline continues. A corrupt file must not stop 999 good ones.
- **Digest subagent failure** — its batch has no digest files; the next
  `plan_batches.py digest` run picks it up again. Retry once, then report.
- **Writer subagent failure** — its nodes are missing; `validate.py` catches them
  as taxonomy nodes with no file. Re-plan that cluster and retry.
- **Validation errors** — report them; never paper over them by editing content.
  Only mechanical fixes (a mistyped link target, a missing frontmatter field with
  an obvious value) may be applied directly.

## Script reference

All scripts take `--root DIR` (or `$KB_ROOT`) and default to the current
directory. Run them from the project root.

```bash
S=.claude/skills/knowledge-base/scripts

python3 $S/bootstrap.py --check          # what extraction fidelity is available
python3 $S/bootstrap.py                  # create .kb/venv (mammoth, pyyaml)
python3 $S/extract.py [--force] [--dry-run]
python3 $S/plan_batches.py digest [--all] [--redo]
python3 $S/aggregate_topics.py [--max-labels 800]
python3 $S/plan_batches.py writer [--clusters a,b] [--redo]
python3 $S/init_wiki.py                  # wiki/ skeleton + _meta stubs + the viewers
python3 $S/build_router_index.py         # the two-layer router index
python3 $S/build_graph_data.py [--max-body-chars N] [--max-total-mb N]
python3 $S/validate.py [--strict]

# post-compile consumers, not pipeline stages — run on demand
python3 $S/build_chat_data.py [--max-total-mb N]
python3 $S/build_project_export.py [--tier T] [--max-chars N] [--check]
```

`extract.py` re-executes itself inside `.kb/venv` automatically when `mammoth`
is available there, so plain `python3` is always the right way to call it.
