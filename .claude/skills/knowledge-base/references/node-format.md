# Node format

The contract every node page must satisfy. `validate.py` enforces most of it, so
deviating produces errors rather than surprises.

## Template

```markdown
---
id: 01-leave-and-absence/parental-leave
title: Parental Leave
description: Eligibility, duration, pay bands and notice periods for parental leave.
cluster: 01-leave-and-absence
tags: [kb/leave-and-absence, topic/parental-leave]
aliases: [Maternity Leave, Paternity Leave]
keywords: [parental leave, maternity, paternity, entitlement, notice period]
sources: ["raw_assets/hr/leave-policy-2025.docx#parental-leave"]
confidence: high
status: active
created: 2026-09-01
updated: 2026-09-01
---

# Parental Leave

Plain-language summary in one paragraph: what this covers and the single most
important thing a reader needs to know. Self-contained — a reader who has never
seen the source documents must be able to act on this page alone.

## Eligibility

Body content under clear `##` headings. Specifics — numbers, dates, thresholds,
entitlements — must come from the sources, never from general knowledge.

## Notice periods

> [!warning] Conflict
> `leave-policy-2025.docx` states 8 weeks' notice; `employee-handbook.docx`
> states 12 weeks. Neither is marked as superseding the other. Needs a human
> decision.

## Connections
- part-of :: [[_cluster]]
- depends-on :: [[eligibility-and-service-length]]
- related-to :: [[02-pay-and-benefits/statutory-pay]]

## Sources
- `raw_assets/hr/leave-policy-2025.docx` — §Parental Leave, §Notice
- `raw_assets/hr/employee-handbook.docx` — §12 Family Leave
```

## Frontmatter fields

| Field | Required | Rules |
| --- | --- | --- |
| `id` | yes | `<cluster-slug>/<node-slug>` — must equal the file path minus `.md` |
| `title` | yes | Human title, unique across the wiki |
| `description` | yes | **The router's layer-2 payload.** One sentence, ≤200 chars |
| `cluster` | yes | Must equal the containing folder name |
| `tags` | yes | `kb/<cluster-topic>` plus `topic/<slug>` per subject. No spaces |
| `aliases` | no | Other names a reader or router might search for |
| `keywords` | yes | 4–10 retrieval terms, including synonyms and acronyms |
| `sources` | yes | `raw_assets/...` paths, optionally `#section`. Every claim traceable |
| `confidence` | yes | `high` (sources explicit and agreeing) / `medium` (some inference) / `low` (thin or conflicting) |
| `status` | yes | `active` or `deprecated` |
| `created` / `updated` | yes | `YYYY-MM-DD`. Leave `created` alone on updates |

## Writing the `description`

This single line decides whether the router ever reaches the page, so it carries
more weight than any other line in the file.

- State **what questions the node answers**, using the words a person would use.
- One sentence, ≤200 characters, no trailing prose.
- Front-load the distinguishing terms; the router may only see the first clause.
- Never open with filler: "This page describes…", "Information about…",
  "Overview of…". Start with the substance.
- It must distinguish this node from its siblings. If two descriptions in a
  cluster could be swapped without anyone noticing, both are too vague.

```
bad   This page provides information about the leave policy.
bad   Leave.
good  Eligibility, duration, pay bands and notice periods for parental leave.
good  How to request time off in Workday, approval chain, and cancellation rules.
```

## Edge vocabulary

Typed edges go in `## Connections` as `- <type> :: [[target]]`. The vocabulary
is closed — `validate.py` warns on anything else:

| Type | Meaning |
| --- | --- |
| `part-of` | This node is a component of the target (every node has one, usually `[[_cluster]]`) |
| `depends-on` | Understanding this node requires the target first |
| `supersedes` | This node replaces the target |
| `superseded-by` | The target replaces this node (pair with `status: deprecated`) |
| `contradicts` | The two nodes make incompatible claims — always also flag a conflict |
| `related-to` | Same subject area, no dependency |
| `see-also` | Useful next read, weaker than `related-to` |

Link rules:
- `[[note-name]]` for a node in the same cluster; `[[cluster/note-name]]` across
  clusters. Never invent a target — links must resolve or validation fails.
- Every node needs at least `part-of :: [[_cluster]]` plus one real edge.
  Orphans are a warning, not an aesthetic complaint: nothing routes to them.
- Aim for 2–5 edges. Twenty edges is the same as none.

## Conflicts

When sources disagree, or one appears to supersede another without saying so:

```markdown
> [!warning] Conflict
> <what each source says, naming both> — <why it cannot be resolved from the sources>
```

Rules that do not bend:
- Never silently pick a winner, average two numbers, or pick the newer file.
- Name both sources and quote the competing specifics.
- Set `confidence: low` on the node.
- The auditor collects every callout into `wiki/_meta/conflicts.md`.

## Hard rules

- **Never fabricate specifics.** No number, date, threshold, entitlement, name or
  version appears in a node unless it appears in a source. If a reader would
  want a specific and the sources do not give one, say the sources do not state it.
- **Self-contained.** No "as mentioned in the attached PDF", no "see the source
  document". The reader has only this page.
- **Never delete a node.** Superseded nodes get `status: deprecated`, a
  `superseded-by` edge, and their title prefixed `[DEPRECATED] `.
- **Topic-shaped, not file-shaped.** One node may draw on ten documents; one
  document may feed ten nodes. A node that is just "the contents of file X"
  usually means the taxonomy needs work.
- **Small and focused beats large and complete.** If a node needs more than
  ~6 `##` sections, it is probably two nodes.

## Verbatim nodes

Written by `assemble_verbatim.py` instead of `kb-writer`, when the knowledge base
must carry its documents unchanged. They keep the frontmatter contract above and
add `kind: verbatim`, `doc_id`, `topic`, `language` and `part` (`i/n`). Two hard
rules are deliberately inverted, because the user asked for the source itself:

- **File-shaped, not topic-shaped.** One node is one source document (or one
  segment of a long one). The topic grouping lives in the cluster hub, the
  `topic/` tags and the keywords — not in the page body.
- **Unedited body.** Below the provenance line, the body is the extracted text
  exactly as extracted. The only changes are mechanical: headings shift one level
  down, and xlsx2md's own `[[Vn]]` interning marker (never source text) renders as
  `⟦Vn⟧` so it cannot be mistaken for a wikilink. A segment whose `### Shared
  values` legend lies in another segment gets the entries it uses copied in.

`description` and `keywords` come from the document's digest (a digest that
quotes the `[[Vn]]` notation gets the same `⟦Vn⟧` rendering; parts of one
document that would share a description are prefixed `Part i of n:`); every suspected
conflict the digest recorded becomes a `> [!warning] Conflict` callout labelled
as unverified, and sets `confidence: low`. Edges are mechanical: `part-of` the
hub, `related-to` the other members of the same topic (language variants of the
same script first) and adjacent segments, `see-also` the lead node of any other
topic the document also feeds.

## Cluster hub (`_cluster.md`)

```markdown
---
title: Leave and Absence
description: Time-off entitlements, request and approval processes, and absence reporting duties.
cluster: 01-leave-and-absence
type: cluster
tags: [kb/leave-and-absence, kb/hub]
keywords: [leave, absence, time off, holiday, sickness]
node_count: 7
created: 2026-09-01
updated: 2026-09-01
---

# Leave and Absence

What this category covers, and where its boundary with neighbouring categories
falls — one short paragraph.

## Nodes

| Node | Description |
| --- | --- |
| [[parental-leave\|Parental Leave]] | Eligibility, duration, pay bands and notice periods for parental leave. |

## Related categories
- related-to :: [[02-pay-and-benefits/_cluster]]
```

The hub's `description` is the router's **layer-1** payload and follows the same
rules, one level up: it must say what the category covers well enough that a
router can choose between categories without opening any node.
