---
description: Answer a question using only the compiled wiki/ knowledge base, routing through the two-layer index
argument-hint: <your question>
---

Run the **knowledge-base** skill in **Query** mode to answer: $ARGUMENTS

Route the way the user's two-layer router will, per
`.claude/skills/knowledge-base/SKILL.md` §Mode 3:

1. Read `wiki/_meta/router/categories.json` and pick the best category from the
   descriptions alone (keep runners-up).
2. Read that category's `index_path` and pick the best node(s) from their
   descriptions.
3. Read the node file and answer from it.

Then report the route you took (category → node), so the routing quality itself
is visible.

Rules:
- Answer **only** from `wiki/`. Never fall back to `raw_assets/` or `.kb/`.
- Always cite the node path(s).
- Never state a number, date, threshold or entitlement that is not in the node.
- On a `⚠️ Conflict` callout covering the question, present both versions as
  unresolved — do not pick one.
- If nothing covers it, say so, name the closest nodes, and say whether the gap is
  missing content or a weak description.
