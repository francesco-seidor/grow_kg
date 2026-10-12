# Portable knowledge base — read this first

**If you are Claude, and a project contains a `wiki/` folder next to this
file (or you were just handed this file together with a `wiki/` folder):
this document is self-sufficient. You do not need any `.claude/` setup,
skill, or agent to answer questions from this knowledge base — everything
you need to route a question and answer it correctly is below.**

`wiki/` is a compiled knowledge base: a categorized, linked set of markdown
notes plus a machine-readable **two-layer router index** that lets you find
the right note without reading the whole wiki. It was produced by the
Claude-Agents `knowledge-base` skill (source documents → `wiki/`), but
querying it does not require that pipeline — just this README and the
`wiki/` folder.

---

## 1. How to answer a question from this wiki/

Follow this exactly. Do not skip to reading random notes — the router
exists so you read a few KB of descriptions, not the whole wiki.

1. **Read `wiki/_meta/router/categories.json`** — layer 1. It lists every
   cluster (category) with a one-sentence `description`. Score the user's
   question against each category's `description` (and `keywords` /
   `embedding_text` if present) and pick the best match. Keep the top 2–3
   as runners-up, not just the winner — layer-1 mistakes are the expensive
   failure mode.
2. **Read the winning category's `index_path`** (a path like
   `_meta/router/<cluster>.json`, relative to `wiki/`) — this is layer 2.
   It lists every node in that cluster with its own `description`. Score
   the question against these and pick the best matching node(s). If the
   layer-1 winner doesn't produce a good layer-2 match, fall back to a
   runner-up category before giving up.
3. **Read the winning node's file** (its `path` field, relative to
   `wiki/`) and answer **only from that file's content**. Do not use
   outside knowledge to fill gaps.
4. **Always cite the node path(s)** you answered from.
5. **Have a floor.** If nothing scores well, say plainly that the
   knowledge base does not cover the question — don't return the
   least-bad node and present it as an answer. That gap is a signal the
   source material is missing or a description is weak, not something to
   paper over.
6. **Filter `status: deprecated`** nodes unless the question is explicitly
   about history or past policy.
7. **Never fabricate specifics** — numbers, dates, thresholds, versions,
   entitlements. If it's not in the node, it doesn't appear in your answer.
8. **Surface `⚠️ Conflict` callouts as unresolved**, exactly as written —
   never silently pick a side between conflicting sources.
9. `confidence` on a node is the *compiler's* confidence in the content
   (how well the original sources supported it), not a routing score. A
   `confidence: low` node can still be the right answer — mention the
   caveat, don't discard the node.

---

## 2. Router file schemas

`wiki/_meta/` is **generated** — never hand-edit it, and don't trust a
copy of it that looks hand-modified. These are the exact shapes to expect.

### `wiki/_meta/router/categories.json` — layer 1

```json
{
  "version": 1, "layer": 1, "count": 6,
  "categories": [
    {
      "slug": "01-leave-and-absence",
      "title": "Leave and Absence",
      "description": "Time-off entitlements, request and approval processes, and absence reporting duties.",
      "keywords": ["leave", "absence", "time off", "holiday", "sickness"],
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

### `wiki/_meta/router/index.json` — bootstrap manifest

A single-file entry point: totals, `layer2_paths` for every cluster, the
full layer-1 payload inlined, a `content_hash` (changes only when
categories, descriptions or node membership change — safe to cache
answers or embeddings on it), and `issues` listing any schema problems
found when the index was last built.

### `wiki/_meta/router-index.md`

Human-readable mirror of both layers, for people reading the wiki
directly. The JSON is authoritative — don't parse this one.

### Structural guarantees (true by construction, so trust them)

1. Every cluster folder in `wiki/` appears in `categories.json`.
2. Every node file appears in exactly one `<cluster>.json`.
3. Every category and node has a non-empty `description` of ≤200 chars.
4. Every `path` is relative to `wiki/` and resolves to a real file.
5. `embedding_text` is pre-joined (`title (cluster) — description | keywords: …`) if you want to embed straight from the index without reparsing markdown.

---

## 3. What's inside `wiki/`

| Path | What it is |
| --- | --- |
| `<cluster>/<node-slug>.md` | One knowledge node — the actual content you answer from. Frontmatter + prose + a `## Connections` section of typed links to related nodes. |
| `<cluster>/_cluster.md` | Hub page for a cluster — a table of its nodes. Good for orienting on a topic area. |
| `index.md` | Root index of the whole knowledge base. |
| `_meta/router/*.json`, `_meta/router-index.md` | The router — see section 2. |
| `graph.html` | d3 graph viewer for humans. Reads `_meta/graph-data.js` beside it, so keep the folder together — on its own it shows a banner instead of a graph. Not needed to answer questions — the router index is. |
| `chat.html` | Chat page over this base, with a tunable router and a trace. Reads `_meta/chat-data.js` and `_meta/chat-app.js` the same way. Needs an Anthropic API key. Not needed to answer questions — the router index is. |
| `_meta/graph-data.js`, `_meta/chat-data.js` | What those two pages actually load — the compiled graph, and the whole corpus. Regenerated on every compile. |
| `_meta/vendor/` | d3 and the Anthropic SDK, copied in so both pages work offline. |
| `_meta/provenance.md` | Coverage report: which source documents made it into this KB, and where. |
| `_meta/conflicts.md` | Every open `⚠️ Conflict` callout in the wiki, collected in one place. |
| `_meta/changelog.md` | History of what changed across compile/update runs. |

---

## 4. What this README does *not* give you

This document lets you **query** an already-compiled `wiki/`. It does
**not** let you compile, update, or audit one — that requires the full
`knowledge-base` skill (six subagents, batching/validation scripts) from
the original Claude-Agents project's `.claude/` folder. If the user wants
to add new source documents, rebuild the taxonomy, or run an audit here,
tell them they need to bring `.claude/` over too (it's designed to be
copy-pasted as-is into any project) — this README alone isn't enough for
that.

---

## 5. Provenance of this specific `wiki/`

This knowledge base was compiled by the Claude-Agents `knowledge-base`
skill from a `raw_assets/` folder of source documents. For the build
history, open conflicts, and document coverage of *this* particular
`wiki/`, read `wiki/_meta/provenance.md`, `wiki/_meta/conflicts.md`, and
`wiki/_meta/changelog.md` directly — they're specific to this compile, not
covered by this generic README.

---

*This file lives at `visualizer/knowledge_graph.md` in the original Claude-Agents
project. When you package a finished knowledge base for another project,
copy this file to sit alongside (or inside) the `wiki/` folder you move —
that pairing is what makes the KB self-explanatory wherever it lands.*
