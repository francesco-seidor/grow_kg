---
description: Compile every document in raw_assets/ into the wiki/ knowledge base (full build)
argument-hint: [optional notes, e.g. "focus clusters on delivery process"]
---

Run the **knowledge-base** skill in **Build** mode: compile everything in
`raw_assets/` into `wiki/`.

Follow `.claude/skills/knowledge-base/SKILL.md` §Mode 1 exactly — all six stages
in order (ingest → digest → architect → write → link → audit), with the fan-out
waves and the cost guardrail above 100 documents.

Do not skip the taxonomy sanity-check before Stage 3: a bad taxonomy wastes the
entire writer budget.

Additional instructions from the user (may be empty): $ARGUMENTS
