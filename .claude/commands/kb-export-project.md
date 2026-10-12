---
description: Export the compiled wiki/ as a Claude Project — an instruction prompt carrying the full cluster and node index, plus per-cluster knowledge bundles to upload
argument-hint: [optional flags, e.g. "--tier clusters" or "--max-chars 20000"]
---

Run the **knowledge-base** skill in **Export** mode, per
`.claude/skills/knowledge-base/SKILL.md` §Mode 5.

```bash
S=.claude/skills/knowledge-base/scripts
python3 $S/build_router_index.py      # the export mirrors the index — make it current first
python3 $S/build_project_export.py    # writes exports/claude-project/
```

Then report:

1. The index tier chosen and the instruction character count.
2. The files written, with sizes.
3. Any warnings — unresolved wikilinks, nodes with no body, an instruction
   prompt over budget, stale bundles removed.
4. The setup steps: paste `exports/claude-project/project-instructions.md` into
   the Project's Instructions field, upload everything in
   `exports/claude-project/knowledge/`.

Rules:
- **Read-only over `wiki/`.** The export derives from frontmatter; it never
  edits, moves or rewrites a node.
- **Never hand-edit the export.** It is generated. Fix the node, rebuild the
  router index, re-export. `references/claude-project-export.md` has the
  contract.
- If `wiki/` or `_meta/router/` is missing, say so and stop — do not export an
  empty knowledge base. Build it first with `/kb-build`.
- The export is a **snapshot**. Say plainly that it must be regenerated after
  every `/kb-build` or `/kb-update`, and both the instructions and the uploaded
  files replaced. `--check` reports whether an existing export has gone stale.
- If the run reports unresolved wikilinks, name them: those are edges the
  Project cannot follow, and they usually mean a broken link in the wiki itself.

Additional instructions from the user (may be empty): $ARGUMENTS
