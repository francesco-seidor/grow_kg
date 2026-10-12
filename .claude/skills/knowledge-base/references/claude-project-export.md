# Claude Project export contract

A Claude Project has two halves: an **instructions** field and a pile of
**uploaded files**. Uploading `wiki/` raw throws away everything the compile
produced — the taxonomy, the router descriptions, the typed edges, the conflict
flags, the deprecation markers. The Project is left doing undifferentiated
search over prose.

`build_project_export.py` projects the vault into that shape instead. It is the
fourth consumer of the router index, alongside the graph payload, the
playground's corpus and Mode 3 query routing, and like them it is **generated
from frontmatter** — never hand-edited.

```
question
  │
  ├─ instructions ─► layer 1 table          pick the category
  │                  layer 2 node list      pick the node id
  │
  └─ uploaded file ─► knowledge/<cluster>.md
                      find `## <node-id>`, answer, cite the node's Sources
```

## Output layout

The export lives **outside `wiki/`**, and the script refuses `--out` paths
inside the vault. `kblib.iter_wiki_files` scans every `.md` under `wiki/` except
`_meta/` as a knowledge-base node, so an export written into the vault would
fail `validate.py` on every bundle and pollute the router index with phantom
nodes.

```
exports/claude-project/
  project-instructions.md   paste into the Project's Instructions field
  README.md                 setup steps and the staleness warning
  manifest.json             content_hash, tier, char counts, file inventory
  knowledge/                upload all of these
    00-INDEX.md             the complete two-layer index, always full fidelity
    00-CONFLICTS.md         copy of wiki/_meta/conflicts.md, when it exists
    01-<cluster-slug>.md    every node of that cluster
    02-<cluster-slug>.md
```

## Bundle format

One file per cluster: a header carrying the cluster description and a node
table, then each node as a section anchored at `## <node-id>` — the same id the
instructions and `00-INDEX.md` name, so "open `02-expenses-and-travel.md` and
find `## 02-expenses-and-travel/expense-limits`" is an instruction the Project
can actually follow.

Each node section carries a metadata block (node id, cluster, what it answers,
status, source confidence, alternate terms, last updated, sources) followed by
the node body, transformed:

| Transform | Why |
| --- | --- |
| Leading `# Title` stripped, all other headings demoted one level | The `## <node-id>` anchor replaces it; nesting stays valid inside a bundle |
| `[[target]]` / `[[target\|Alias]]` → ``Alias (node `id`)`` | A Project cannot follow an Obsidian link, but it can follow a node id that appears verbatim in the index |
| `## Connections` edges → `- <type> :: `<node-id>` (Title)` | This is the graph, made traversable: `depends-on` points at a findable id instead of a filename |
| `> [!warning] Conflict` preserved verbatim | The grounding rules key off it — the Project must present both versions unresolved |
| Deprecated nodes get a `> [!warning] DEPRECATED` banner naming the successor | Prevents answering a current question from a superseded rule |

Headings inside fenced code blocks are left alone. Unresolved wikilinks keep
their text, are counted in `manifest.json` and warned about — an unresolved link
is usually a broken link in the wiki itself.

Bundles above `--max-bundle-kb` (default 512) split at **node boundaries only**
into `<slug>-1.md`, `<slug>-2.md`, …; a half node is a node that can be answered
from wrongly. The index records the part file each node landed in.

## Instruction tiers

The instructions field has a practical size limit. `--max-chars` (default 30000)
is a conservative budget, not a claimed platform limit. The script emits the
largest tier that fits; `--tier` forces one.

| Tier | Inline in the instructions |
| --- | --- |
| `full` | categories + every node with its description and alternate terms |
| `standard` | categories + every node with its description |
| `clusters` | categories only; the instructions direct the Project to read `00-INDEX.md` **before answering anything** |

Descriptions are never truncated — a truncated description is a broken router
payload. Below roughly 5k chars no tier fits, because the grounding contract,
routing protocol and answer rules are fixed prose; the script says so rather
than silently trimming them.

`00-INDEX.md` always carries the complete index at full fidelity regardless of
tier, so degrading the inline index never loses information.

## Staleness

The export is a **snapshot**. `manifest.json` records the router index's
`content_hash`, and `--check` compares it against the live wiki:

```bash
python3 build_project_export.py --check   # exit 0 current, exit 1 stale
```

`content_hash` moves when categories, category descriptions or node membership
change. It deliberately does not move on a node body edit — re-export after any
`/kb-update` regardless, and replace **both** the instructions and the uploaded
files. A stale instruction prompt names nodes that may no longer exist.

## Guarantees

1. Every node in the router index appears in exactly one bundle file.
2. Every node in a bundle appears in `00-INDEX.md` with the file it lives in.
3. Every node section is anchored at `## <node-id>`, matching its router `id`.
4. No `[[wikilink]]` survives into an exported file.
5. Deprecated nodes are shipped, flagged in the index, and banner-marked in the
   bundle — never silently dropped, matching the never-delete-a-node invariant.
6. Nothing is written inside `wiki/`.

## Not part of the compile

The export is not a pipeline stage and is not run by `/kb-build` or `kb-linker`.
It duplicates the whole knowledge base into a second format; generating that on
every build is cost with no default consumer. Run it when you want to load the
base into a Project, and again whenever the base changes.
