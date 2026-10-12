---
description: Audit the wiki/ knowledge base for validation errors, coverage gaps, conflicts, staleness and router readiness
argument-hint: [optional focus, e.g. "router quality" or "staleness"]
---

Run the **knowledge-base** skill in **Audit** mode by launching the `kb-auditor`
subagent, then report its findings verbatim.

It checks validation, coverage (documents that reached no node), the conflicts
register, staleness, and router readiness — including the swap test on
descriptions and live routing traces for sample questions.

It fixes mechanical defects only. Anything touching factual content goes on the
"needs a human decision" list.

Optional focus from the user (may be empty): $ARGUMENTS
