# The router playground (`wiki/chat.html`)

The page is a verbatim copy of `assets/chat-viewer.html`, installed by
`init_wiki.py` together with `assets/chat-app.js` and the vendored Anthropic JS
SDK. Only its corpus is rebuilt per compile, by `scripts/build_chat_data.py` —
which matters more here than for the graph, because that corpus carries every
node body untruncated and reaches tens of MB.

No server, no npm, and it never fetches: everything arrives as classic
`<script src>` siblings under `_meta/`, which load from `file://` where `fetch()`
and `type="module"` do not.

It exists to fill the hole `references/router-index.md` leaves open: that file
specifies the index and then stops at `pick(query, candidates)`. This is the
`pick`, with every parameter exposed.

## What is embedded

`_meta/chat-data.js` assigns `window.__KB_CHAT__`: the layer-1 catalog verbatim
from `categories.json`, every layer-2 node entry, and **the full body of every
node**. Unlike the graph payload, bodies are never truncated: a node with no body
cannot be answered from, so `--max-total-mb` (default 40) only warns.

With no `chat-data.js` beside it the page says so and names the command to run,
rather than opening an empty chat.

`content_hash` from `_meta/router/index.json` namespaces the page's local
storage, so two vaults on one machine keep separate settings.

## The three modes

| Mode | What it does | Cost |
| --- | --- | --- |
| `two_layer` | Score the catalog → keep top *N* clusters over the L1 floor → **one** call over the union of their nodes → keep top *M* over the L2 floor → answer | 3 calls |
| `flat` | One scoring call over every node description; skips layer 1 entirely | 2 calls |
| `bm25` | Okapi BM25 over the pre-joined `embedding_text`, in the browser | 1 call (answer only) |

`flat` is the control: it tells you whether layer 1 is helping or hurting. `bm25`
is the free floor — an LLM router that cannot beat keyword matching on your vault
is not earning its tokens.

Layer 2 scores the **union** of the kept clusters in a single call. Scoring each
cluster separately would produce numbers from different contexts, and ranking
across them would be meaningless.

## Floors

Two of them, because picking a cluster and picking a note are different decisions
with different costs of being wrong. Defaults: L1 `0.25`, L2 `0.45`.

The model is asked for a score per candidate and never told the floor or the
keep-count — the moment it knows the threshold it games it, and you lose the
ability to move the floor without re-prompting. The page applies:

```
clamp to 0-1 → dedupe by key → sort desc → truncate to keep → apply floor
```

The floor comes last on purpose. Applied earlier, a below-floor candidate could
still occupy one of the `keep` slots.

**BM25 floors are relative** (`cut = floor × top score`), because BM25 scores are
unbounded and corpus-dependent. One consequence is worth knowing: normalising
against the top hit means the winner always scores 1.0, so **raising the floor in
BM25 mode prunes runners-up and never the winner**. The only BM25 refusal is a
query where no term matches anything. The stage note in the trace says so.

## Below the floor

| Setting | Behaviour | Extra spend |
| --- | --- | --- |
| `refuse` *(default)* | No answer call. Names the nearest misses and diagnoses the gap | none |
| `answer_anyway` | Answers from the top candidates, flagged low-confidence in both the answer and the trace | 1 call |
| `widen` | Retries layer 2 once at `keep × 2`, `floor × 0.5`, reusing layer 1's scores | 1 call |
| `escalate` | Re-runs the deciding layer on a better model at high effort | 1 call |
| `bm25_rescue` | Falls back to keyword matching over the whole vault | 1 call |

`escalate` is the one that answers the question you actually have while tuning:
it separates "the cheap router was the problem" from "the content isn't there".
`bm25_rescue` catches the classic LLM-router miss — a rare proper noun or exact
identifier that appears in no description.

## Diagnosis

Emitted on every refusal. This is the `/kb-ask` rule "say whether the gap is
missing content or a weak description", made mechanical:

| Code | Means | Fix |
| --- | --- | --- |
| `missing_content` | The right cluster exists, nothing in it answers | Write the note |
| `missing_cluster_or_weak_descriptions` | Nothing cleared layer 1 | Add a cluster, or say in the descriptions what they cover |
| `overlapping_descriptions` | Top two clusters within 0.05 | Fix the taxonomy boundary, not the wording |
| `overlapping_nodes` | Top two notes within 0.05 | Merge them, or sharpen the boundary |
| `no_keyword_match` | BM25 only: no query term appears anywhere | Try the two-layer router — it matches meaning, not words |

`overlapping_descriptions` is the most valuable of these: it is the failure mode
`router-index.md` warns about, and it is invisible from any single answer.

## Models

| Model | `temperature` | `effort` | thinking | min cacheable prefix |
| --- | --- | --- | --- | --- |
| `claude-opus-5` | 400 | low–max | adaptive | 512 |
| `claude-opus-4-8` | 400 | low–max | adaptive | 1024 |
| `claude-sonnet-5` | 400 | low–max | adaptive | 1024 |
| `claude-haiku-4-5` | allowed | **400** | `budget_tokens` | 4096 |
| `claude-fable-5-1` | 400 | low–max | **always on — omit the field** | 512 |

**There is no temperature control, deliberately.** It is removed API-wide on
current models; a slider would only produce 400s. `effort` is the equivalent
lever.

Every request is built by one function, so illegal combinations cannot be sent:
an effort the table doesn't list is dropped, `thinking` is shaped by the model
family, and `temperature` has no code path. The panel hides the controls a model
does not accept, and `sanitize()` repairs stored presets on load and save — so a
preset written before a model changed degrades with a note instead of 400ing.

`answer.model: "none"` is retrieve-only: no synthesis call. It makes retrieval
tuning free and the whole page exercisable with no API key.

## Prompt caching

`cache: auto | on | off`. Placement is static-first: system block 1 is the frozen
instructions with no breakpoint, block 2 is the candidate list carrying
`cache_control`, and the question goes last in `messages`.

`auto` attaches the breakpoint only when the block clears that model's minimum.
Do the arithmetic before expecting savings: a six-cluster catalog is roughly 500
tokens, and **Haiku 4.5 — the natural cheap layer-1 router — has the highest
minimum of any current model at 4096**. So the place you would instinctively
cache is the place it provably cannot fire, silently. Where it does pay is layer
2 on a real vault, and the answer synthesiser's node bodies across turns.

Candidate blocks are built from `slug/title/description/keywords` only, sorted by
identifier — never by serialising the router JSON, which carries a fresh
`generated` timestamp on every rebuild and would invalidate the cache each time.

The trace reports `cache_read_input_tokens` per stage, so this stays a number you
watch rather than an argument you have. `cache: on` attaches the breakpoint
regardless of size, which is how you confirm the minimum is what is blocking you.

## Flat-mode guard

Over `flat_max_input_tokens` (default 60 000), or over 2000 candidate ids, the
page **refuses and explains** rather than truncating. Flat mode is an accuracy
baseline; a baseline that quietly drops half the corpus is not merely wrong, it
is confidently wrong.

## Two different confidences

`content_confidence` comes from a node's frontmatter and is the **compiler's**
confidence in the content. `match_score` is the **router's** confidence in the
match. They are named apart at the data layer so the UI cannot render them in one
column. A `content_confidence: low` note can still be the right answer — it shows
as a caveat, never a demotion, and the answer prompt is told to surface it.

## Storage, and the `file://` caveat

Settings, presets, the API key (only if you tick "remember") and a 300-entry run
log live in `localStorage`, namespaced by `content_hash`.

`file://` local storage is unreliable: Safari blocks it, and Chrome shares one
bucket across all `file://` pages. Every read and write is wrapped, falling back
to memory with a visible banner. Two ways out:

- **Export settings** / **Import settings** — a JSON file, never containing the key.
- Serve the folder properly: `cd wiki && python3 -m http.server`, then open
  `http://localhost:8000/chat.html`. No custom server, just the stdlib one.

## The API key

Entered in the panel, held in memory for the session. It is never baked into the
generated page, never written to an exported settings file, never put in the run
log, and never printed. A `redact()` pass strips anything matching
`sk-ant-[A-Za-z0-9_-]{8,}` from every string reaching the trace or the log, as
insurance against an SDK error echoing a header.

The page calls `api.anthropic.com` directly from the browser with
`dangerouslyAllowBrowser: true`, which makes the SDK send
`anthropic-dangerous-direct-browser-access: true`. The API allows this from a
`file://` origin.

## Feeding settings back to `/kb-ask`

**Export for /kb-ask** emits the tuned sizing, floors and prompts as a block to
paste into `.claude/commands/kb-ask.md`. The page never writes that file itself.

## Rebuilding the vendored SDK

Only needed when bumping the SDK version. It must be an **IIFE** bundle with a
global — a page loading it with a classic `<script src>` cannot get at an ESM
bundle's exports.

```bash
echo 'export * from "@anthropic-ai/sdk";' > entry.js
npm i @anthropic-ai/sdk@<version> esbuild
npx esbuild --bundle --format=iife --global-name=AnthropicSDK \
  --platform=browser --target=es2020 --minify \
  --outfile=assets/vendor/anthropic-sdk.browser.js entry.js
shasum -a 256 assets/vendor/anthropic-sdk.browser.js > assets/vendor/anthropic-sdk.browser.js.sha256
```

`init_wiki.py` copies that bundle into `wiki/_meta/vendor/`, comparing it
against the committed `.sha256` on the way — a mismatch is reported and the file
installed anyway, since refusing to copy would leave the page with no SDK at all.
Inspect a built corpus with `build_chat_data.py --check`.

## Gotcha for anyone editing the viewer

`[hidden]{display:none !important}` in the stylesheet is load-bearing. The UA's
`[hidden]{display:none}` loses to any author rule that sets `display`, and the
panel rows are `display:flex` — without the override, capability gating computes
correctly and then fails to hide anything.
