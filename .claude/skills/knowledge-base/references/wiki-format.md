# Wiki output

`wiki/` is the deliverable. `wiki/graph.html` is how you look at it: no server
and no network, showing every cluster and node, every typed connection, and
everything wrong with the build. It reads its data from `wiki/_meta/` next to it,
so the folder travels together — `graph.html` on its own shows a banner asking
for a build.

## Layout

```
wiki/
├── graph.html                    the d3 graph viewer — a copy, double-click it
├── chat.html                     the router playground — a copy too
├── index.md                      root Map of Content — layer-1 view for humans
├── 01-<cluster>/
│   ├── _cluster.md               MOC hub; its description is the router's layer 1
│   ├── <node>.md
│   └── <node>.md
├── 02-<cluster>/
└── _meta/
    ├── graph-data.js             the compiled graph, as the viewer loads it
    ├── chat-data.js              the whole corpus, as the playground loads it
    ├── chat-app.js               the playground's code — a copy
    ├── vendor/                   d3 and the Anthropic SDK — copies, verified
    ├── router/                   machine-readable router index (JSON)
    ├── router-index.md           human mirror of both router layers
    ├── conflicts.md              every open ⚠️ conflict, collected
    ├── provenance.md             source document → node coverage table
    └── changelog.md              what each compile run changed
```

Cluster folders are numbered (`01-`, `02-`) so the file explorer orders them
deliberately rather than alphabetically. The number is part of the slug and
therefore part of every `id`, tag, router path and the viewer's colour index —
renumbering later means rewriting links, so decide the order once at
architecture time.

## Links

- Wikilinks only: `[[node-name]]`, never markdown links between notes. Link
  resolution, backlink discovery, unresolved-link detection and the viewer's
  in-page navigation all key off wikilinks.
- Same cluster: `[[parental-leave]]`. Cross-cluster: `[[02-pay-and-benefits/statutory-pay]]`.
- Display text: `[[parental-leave|Parental Leave]]`. Inside a markdown **table**
  the pipe must be escaped: `[[parental-leave\|Parental Leave]]`.
- Resolution follows shortest-path, implemented in `kblib.build_link_resolver`:
  a unique basename is enough; when two clusters hold the same basename the full
  path is required and `validate.py` flags the ambiguity. The viewer mirrors this
  rule exactly, so a link that resolves in the graph resolves in validation too.
- Headings: `[[node-name#Eligibility]]` — only to headings that exist.

## Tags

Two namespaces, both flat, both without spaces:

- `kb/<cluster-topic>` — one per node, matching its cluster. A search and filter
  facet. (Cluster colour in the viewer comes from the cluster **folder**, not
  from this tag.)
- `topic/<slug>` — subject tags, reusable across clusters. This is where
  cross-cutting themes become visible without inventing folders for them.
- `kb/hub` on cluster hubs, `kb/meta` on `_meta/` pages.

## Callouts

Used for exactly two purposes so they stay meaningful:

```markdown
> [!warning] Conflict
> Sources disagree: …

> [!info] Not stated in sources
> The sources do not specify …
```

`> [!warning] Conflict` is **load-bearing**, not decoration. It is the marker
that `kblib.CALLOUT_CONFLICT_RE` matches, and it drives the viewer's conflict
list, `_meta/conflicts.md` and the open-conflict count in every report. Write it
exactly in that form.

## Frontmatter properties

`aliases` makes `[[Maternity Leave]]` resolve to the parental-leave node, and
feeds both the router's `embedding_text` and the viewer's search index — worth
filling in for every term a reader might type. `status` and `confidence` are
filters in the viewer.

## The graph viewer

`wiki/graph.html` is **not** generated. It is a verbatim copy of
`assets/graph-viewer.html`, installed by `init_wiki.py`; only its data is rebuilt
per compile, by `build_graph_data.py`. That is what stops a 400KB page being
rewritten on every run, and lets a viewer fix ship without recompiling anything.

It loads two siblings as classic `<script src>` tags: `_meta/graph-data.js`
(`window.__KB_GRAPH__`, the whole compiled graph) and `_meta/vendor/d3.v7.min.js`.
Classic script tags, never `fetch()` and never `type="module"` — **this is the
constraint the whole design rests on.** Browsers block both of those from a
`file://` page, so either would break double-click opening on the most common
browser, and the failure would look exactly like a vault that was never compiled.
As it is, it opens by double-click from `file://` — no server, no npm, no
network.

Three regions, all visible at once:

- **Findings rail** — Problems (validation errors and warnings, open conflicts,
  coverage gaps, unsupported and failed documents), Clusters, and Sources
  (source document → the nodes it fed, plus which sources contradict each
  other). Clicking any row highlights the offending nodes in the graph. This is
  co-visible with the graph on purpose: a problem you cannot locate in the graph
  is half a finding.
- **Graph** — force-directed, clusters as spatially separated lobes with a
  labelled hull, edges styled per relation type, nodes ringed and badged when
  they carry a problem.
- **Inspector** — the selected node's description, its rendered markdown body
  with working `[[wikilink]]` navigation, its typed connections and its cited
  sources.

Plus an `Audit report` view (`r`) — a printable single-column summary of every
problem, the provenance table and the source-conflict matrix.

### Flags

| Flag | Why |
| --- | --- |
| `--max-body-chars N` | Per-node body cap (default 20000, `0` = unlimited). |
| `--max-total-mb N` | Data file budget (default 12). Over it, bodies are dropped least-connected-first and the page says so. It budgets `graph-data.js` alone — before the viewer was split out, the same number also had to cover ~400KB of page. |
| `--dump-json PATH` | The payload alone as `.json`, for debugging. |
| `--check` | Inspect an existing `_meta/graph-data.js` and report its totals. |

### Vendoring d3

Done once, by hand, and committed — a compile step must never silently reach the
internet:

```bash
mkdir -p .claude/skills/knowledge-base/assets/vendor
curl -fsSL https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js \
  -o .claude/skills/knowledge-base/assets/vendor/d3.v7.min.js
shasum -a 256 .claude/skills/knowledge-base/assets/vendor/d3.v7.min.js \
  > .claude/skills/knowledge-base/assets/vendor/d3.v7.min.js.sha256
```

`init_wiki.py` copies that file into `wiki/_meta/vendor/`, comparing it against
the committed `.sha256` on the way. Without it the page falls back to the d3 CDN
and needs the network; `validate.py` reports the missing copy as a `viewer`
warning. If d3 does not arrive either way, the page renders a cluster outline
from the payload rather than a blank page.

**Never hand-edit `wiki/graph.html`.** `init_wiki.py` overwrites it with the
asset, and `validate.py` warns as soon as the two differ. To change what the
viewer *does*, edit `assets/graph-viewer.html` — it is hand-maintained with no
build step, so `build_graph_data.py` guards its two silent failure modes: a
leftover `{{TOKEN}}` and a `SCHEMA_EXPECTED` that disagrees with the payload
writer. To change what it *shows*, fix the frontmatter and rebuild.

### Degraded output is explicit

With no `_meta/graph-data.js` beside it, the page says so and names the command
to run rather than rendering an empty canvas — the state of a wiki nobody has
compiled yet is not an error.

`.kb/` is disposable, so the payload can be built from `wiki/` alone. When it is,
the page says what it could not measure rather than implying a clean result:
coverage reads "unknown", the Sources tab is labelled as derived from node
`sources:` only, and the Problems tab names the check families that never ran.
A coverage figure of zero gaps is only ever shown when a manifest actually
proved it.

## What good output looks like

- Distinct, visually separate cluster lobes with their hubs legible — not one
  hairball.
- Zero unresolved links; every node reachable within two clicks of `index.md`.
- The Problems panel free of errors, with any remaining warnings understood.
- Coverage showing every source document landing on at least one node.
- Every open conflict discoverable from the rail, and each one naming both
  sources.

## Using Obsidian anyway

Nothing here is Obsidian-hostile: wikilinks, `kb/` tags, callouts and
frontmatter properties all still work if you open `wiki/` as a vault. The
pipeline simply no longer generates or manages `.obsidian/` or `*.canvas`. If an
older build left those behind, `init_wiki.py` and `validate.py` both report them
as safe to delete — neither ever deletes them for you.
