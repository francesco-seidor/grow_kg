---
id: 07-group-reporting-and-consolidation/2608-seg-consolidation-segment-128
title: 2608 SEG Consolidation Segment (2608_SEG_Consolidation_Segment)
description: "SEG consolidation segment hierarchy (2608): root Segment with nodes SEGA00, SEGB00, SEGC00 grouping segments SE0001-SE0005, node validity 20251231 to 99991231."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/consolidation-hierarchy-uploads]
aliases: [2608_SEG_Consolidation_Segment]
keywords: ["Consolidation Hierarchy Upload Samples (Region, Segment…", consolidation segment hierarchy, consolidation segments, segment hierarchy, hierarchy node validity, hierarchy metadata, 2608]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_SEG_Consolidation_Segment.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-128
topic: 07-group-reporting-and-consolidation/consolidation-hierarchy-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2608 SEG Consolidation Segment (2608_SEG_Consolidation_Segment)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_SEG_Consolidation_Segment.xlsx`, extracted with `xlsx2md`. Grouped under **Consolidation Hierarchy Upload Samples (Region, Segment, Brand, Line of Business)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2608 SEG Consolidation Segment

### Sheet: Hierarchy

| Consolidation Segment |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchy ID: | SEG |  |  |  |  |  |  |  |  |  |
| Valid From: | N/A |  |  |  |  |  |  |  |  |  |
| Valid To: | N/A |  |  |  |  |  |  |  |  |  |
| Consolidation Segment | Level | Type | ID (From) | ID (To) | Node Valid From (YYYYMMDD) | Node Valid To (YYYYMMDD) | Description | Parent ID | Reference Hierarchy ID | Reference Hierarchy Validity |
| \|- SEG (Segment) | 1 | Root | SEG |  | 20251231 | 99991231 | Segment |  |  |  |
|  |  | Node | SEGC00 |  | 20251231 | 99991231 | SEGC00 | SEG |  |  |
|  |  | Consolidation Segment | SE0005 |  | 20251231 | 99991231 | SE0005 | SEGC00 |  |  |
|  |  | Node | SEGB00 |  | 20251231 | 99991231 | SEGB00 | SEG |  |  |
|  |  | Consolidation Segment | SE0003 |  | 20251231 | 99991231 | SE0003 | SEGB00 |  |  |
|  |  | Consolidation Segment | SE0004 |  | 20251231 | 99991231 | SE0004 | SEGB00 |  |  |
|  |  | Node | SEGA00 |  | 20251231 | 99991231 | SEGA00 | SEG |  |  |
|  |  | Consolidation Segment | SE0001 |  | 20251231 | 99991231 | SE0001 | SEGA00 |  |  |
|  |  | Consolidation Segment | SE0002 |  | 20251231 | 99991231 | SE0002 | SEGA00 |  |  |

### Sheet: Validation (hidden)

| Node | Consolidation Segment | Root | Reference Node |  |
| --- | --- | --- | --- | --- |
| {"CLIENT":"","VER_ID":"42010AEEC45C1FE0AFF1860888CD6391","VER_PID":"","VER_STATUS":"S","VER_VLDFM":"00000000","VER_VLDTO":"00000000","VER_MSG":"","VER_NBR":"","VER_IDX":"000000000000001","HIER_HID":"SEG","HIER_CATG":"CS01","UPDATED_AT":20251112055528 ,"UPDATED_BY":"CB9980000750","CREATED_AT":20251112055528 ,"CREATED_BY":"CB9980000750","LOCKED_BY":"","LOCKED_AT":0 ,"ALLOW_LEGACY_TCODE_USAGE":"","VER_SRC":"","MAINTENANCE_LANG":"E","REF_UPDATED_AT":0 ,"NODE_TIMEDEP":"X","CREATED_ON":"20251112","CATEGORYTEXT":"Consolidation Segment","HIER_DESC":"Segment","HRY_CLASS":"","STATUSTEXT":"Draft","SIMULATE_REPORT_ID":"","ACTIVE_REPORT_ID":"","IS_UNASSIGNED_SHOW":"X","IS_RANGE_SUPPORTED":"X","HIDE_VALIDITY":"X","ATTRIBUTEVALUES":"","LOCK_HIER_ATTR_EDIT":"","HIERARCHY_TAG":"","HIERARCHY_TAG_TEXT":"","HAS_REFERENCE_NODE":"","ISPRIVATE":"","VIAJOB":"","ACTJOBNAME":"","ACTJOBCOUNT":"","ACTJOBSTATUS":"","ACTJOBACTION":"","DOWNLOADJOBNAME":"","DOWNLOADJOBCOUNT":"","DOWNLOADJOBSTATUS":"","DOWNLOADJOBACTION":"","HAS_REF_BY_NODE":""} | [] |  |  |  |
| 7 |  |  |  |  |
| I |  |  | J | K |
|  |  | H | E |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2608-brd-consolidation-profit-center-110]]
- related-to :: [[07-group-reporting-and-consolidation/2608-lob-consolidation-profit-center-116]]
- related-to :: [[07-group-reporting-and-consolidation/2608-region-consolidation-unit-127]]
- related-to :: [[07-group-reporting-and-consolidation/2308-brd-consolidation-profit-center-9]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_SEG_Consolidation_Segment.xlsx` — full document · extracted with `xlsx2md` · 2,498 chars in the whole document
