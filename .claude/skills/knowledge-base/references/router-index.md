# Router index contract

The compiled wiki is a substrate for a **two-layer retrieval router**, not just
something to read. This file defines what the pipeline guarantees to whatever
consumes it.

```
query
  │
  ├─ layer 1 ─► _meta/router/categories.json     score query vs. category descriptions
  │             pick best category + confidence
  │
  ├─ layer 2 ─► _meta/router/<cluster>.json      score query vs. node descriptions
  │             pick best node(s) + confidence
  │
  └─ read ────► wiki/<cluster>/<node>.md         self-contained answer
```

The point is progressive disclosure, the same trick skill frontmatter uses: a
router reads a few KB of descriptions, not a few MB of documents, and only the
winning node is ever loaded in full.

## Files

`build_router_index.py` writes all of these from the frontmatter on disk. **The
notes are the source of truth** — the index is derived, never hand-edited, and
regenerating it is cheap. Anything hand-edited here is lost on the next build.

### `wiki/_meta/router/categories.json` — layer 1

```json
{
  "version": 1, "layer": 1, "generated": "...", "vault": "wiki",
  "usage": "...",
  "count": 6,
  "categories": [
    {
      "slug": "01-leave-and-absence",
      "title": "Leave and Absence",
      "description": "Time-off entitlements, request and approval processes, and absence reporting duties.",
      "keywords": ["leave", "absence", "time off", "holiday", "sickness"],
      "tags": ["kb/leave-and-absence", "kb/hub"],
      "node_count": 7,
      "deprecated_count": 0,
      "hub_path": "01-leave-and-absence/_cluster.md",
      "index_path": "_meta/router/01-leave-and-absence.json",
      "embedding_text": "Leave and Absence — Time-off entitlements... | keywords: leave, absence, ..."
    }
  ]
}
```

### `wiki/_meta/router/<cluster>.json` — layer 2

```json
{
  "version": 1, "layer": 2, "cluster": "01-leave-and-absence",
  "cluster_title": "...", "cluster_description": "...", "count": 7,
  "nodes": [
    {
      "id": "01-leave-and-absence/parental-leave",
      "title": "Parental Leave",
      "description": "Eligibility, duration, pay bands and notice periods for parental leave.",
      "keywords": ["parental leave", "maternity", "paternity"],
      "aliases": ["Maternity Leave"],
      "tags": ["kb/leave-and-absence", "topic/parental-leave"],
      "path": "01-leave-and-absence/parental-leave.md",
      "cluster": "01-leave-and-absence",
      "status": "active",
      "confidence": "high",
      "sources": ["raw_assets/hr/leave-policy-2025.docx#parental-leave"],
      "updated": "2026-09-01",
      "embedding_text": "Parental Leave (Leave and Absence) — Eligibility... | keywords: ..."
    }
  ]
}
```

### `wiki/_meta/router/index.json` — manifest

Single-file bootstrap: routing instructions, totals, a `content_hash` (changes
only when categories, descriptions or node membership change — cache on it),
`layer2_paths` for every cluster, the full layer-1 payload inline, and `issues`
carrying any schema problems found while building.

### `wiki/_meta/router-index.md`

Human-readable mirror of both layers. For reading and reviewing, not for
machines — the JSON is authoritative.

## Guarantees

1. Every cluster folder on disk appears in `categories.json`.
2. Every node file appears in exactly one `<cluster>.json`.
3. Every category and node entry has a non-empty `description` of ≤200 chars.
4. `path` is relative to `wiki/` and resolves to a real file.
5. `embedding_text` is pre-joined `title (cluster) — description | keywords: …`,
   so a consumer can embed straight from the index without reparsing markdown.
6. `content_hash` is stable across rebuilds that change nothing material.

`validate.py` fails the build if 1–4 break, which is what keeps a downstream
router from silently losing access to part of the corpus.

## Consuming it

Minimum viable router, no dependencies:

```python
import json, pathlib
V = pathlib.Path("wiki")
cats = json.loads((V / "_meta/router/categories.json").read_text())["categories"]
# layer 1: score `query` against each cat["embedding_text"] (LLM, embeddings, BM25...)
best = pick(query, cats)                       # keep runners-up above your floor
nodes = json.loads((V / best["index_path"]).read_text())["nodes"]
# layer 2: score against node["embedding_text"]
hit = pick(query, nodes)
answer_context = (V / hit["path"]).read_text()  # self-contained by construction
```

Notes for whoever builds the router:
- **Keep runners-up.** Layer 1 mistakes are the expensive failure mode; carrying
  the top 2–3 categories forward costs little.
- **Have a floor.** Below it, answer "the knowledge base does not cover this"
  rather than returning the least-bad node. That gap is a compile-time signal:
  it means material is missing or a description is weak.
- **Filter `status: deprecated`** unless the query is explicitly historical.
- **Cache on `content_hash`**, and re-embed only when it changes.
- `confidence` on a node is the *compiler's* confidence in the content (how well
  the sources supported it), not the router's confidence in the match. A node
  with `confidence: low` may still be the correct answer — surface the caveat.

## Keeping descriptions routable

The index is only as good as the descriptions in it. Two failure modes to watch,
both reported by `validate.py`:

- **Vague categories.** If two category descriptions could be swapped without
  anyone noticing, layer 1 will coin-flip. Fix the taxonomy, not the wording.
- **Overlapping nodes.** Two nodes answering the same question split the router's
  signal. Merge them, or sharpen the boundary and say what each excludes.

Full field-by-field rules live in [node-format.md](node-format.md).
