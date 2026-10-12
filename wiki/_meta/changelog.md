---
title: Changelog
description: "What each compile run added, updated, deprecated or flagged."
tags: [kb/meta]
created: 2026-10-09
updated: 2026-10-12
---

# Changelog

## 2026-10-12 — post-audit fixes

- Clusters: 01 and 10 descriptions now name their main content (SSCUI list and process steps; requisition-to-receipt purchasing); no cluster renamed or renumbered
- Pages: parts of one document that shared a description are now numbered (3 duplicate pairs resolved)
- Viewer: graph.html conflict panel reads conflicts from full page text — 709 open conflicts (was 72, under-counted)
- Checks: CJK descriptions no longer flagged as thin by the router build or the validator; deprecated pages exempt from the orphan check
- Validation: 0 errors, 14 warnings (13 cluster size, inherent to verbatim mode; 1 uncompiled error log)

## 2026-10-12 — audit (verbatim build)

- Documents: 1,312 compiled (623 unsupported or skipped, of which 600 are xlsx companions of compiled Word documents; 0 failed in the manifest)
- Clusters: 17 (1 new this run: 17-leasing-and-real-estate, split out of 03 with user approval)
- Nodes: 1,439 pages (1,420 active, 19 deprecated: the old 03 locations of leasing pages that moved to 17)
- Conflicts: 709 open callouts on 439 pages (all unverified digest flags, none resolved); register in `conflicts.md`
- Coverage: 1 document reached no node (conversion-error log `Failed_~$8_S4CLD2608_Master_Data_ES_XX.odt.txt`)
- Validation: 0 errors, 14 warnings (13 cluster-size, 1 coverage)
- Router: 17 categories, 1,439 nodes, 6 pages with descriptions too thin to route on

## 2026-10-09 — init

- Skeleton created.
