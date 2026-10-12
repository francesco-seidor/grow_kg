---
description: Incrementally recompile the wiki/ knowledge base for documents added or changed in raw_assets/
argument-hint: [optional: "allow structural changes" to permit new/split clusters]
---

Run the **knowledge-base** skill in **Update** mode.

Follow `.claude/skills/knowledge-base/SKILL.md` §Mode 2 and
`references/pipeline.md` §Incremental update: re-extract by sha256, digest only
new and changed documents, run the architect in incremental mode, rewrite only
affected nodes, then link and audit in full.

Hard constraints:
- **Never renumber or rename an existing cluster** — it breaks every node `id`,
  wikilink and router path.
- Propose structural changes (new or split clusters) for approval rather than
  applying them, unless the user's instructions below authorise them.
- Never auto-delete nodes whose sources vanished from `raw_assets/` — report them.

If nothing changed, say so and stop.

Additional instructions from the user (may be empty): $ARGUMENTS
