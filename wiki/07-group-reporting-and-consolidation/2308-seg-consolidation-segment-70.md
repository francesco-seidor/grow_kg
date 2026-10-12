---
id: 07-group-reporting-and-consolidation/2308-seg-consolidation-segment-70
title: 2308 SEG Consolidation Segment (2308_SEG_Consolidation_Segment)
description: "Consolidation Segment hierarchy SEG (SEGMENT) with three nodes SEGA00, SEGB00, SEGC00 and segments SE0001-SE0005; valid from 01/01/2016 to 12/31/9999."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/consolidation-hierarchy-uploads]
aliases: [2308_SEG_Consolidation_Segment]
keywords: ["Consolidation Hierarchy Upload Samples (Region, Segment…", consolidation segment hierarchy, consolidation segments, segment reporting, hierarchy validity, hierarchy versions, reference hierarchies, 2308]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_SEG_Consolidation_Segment.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-70
topic: 07-group-reporting-and-consolidation/consolidation-hierarchy-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2308 SEG Consolidation Segment (2308_SEG_Consolidation_Segment)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_SEG_Consolidation_Segment.xlsx`, extracted with `xlsx2md`. Grouped under **Consolidation Hierarchy Upload Samples (Region, Segment, Brand, Line of Business)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2308 SEG Consolidation Segment

### Sheet: Hierarchy

| Consolidation Segment |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchy ID: | SEG |  |  |  |  |  |  |  |
| Valid From: | 01/01/2016 |  |  |  |  |  |  |  |
| Valid To: | 12/31/9999 |  |  |  |  |  |  |  |
| Consolidation Segment | Level | Type | ID (From) | ID (To) | Description (English) | Parent ID | Reference Hierarchy ID | Reference Hierarchy Validity |
| \|- SEG (SEGMENT) | 1 | Root | SEG |  | SEGMENT |  |  |  |
| \|- SEGC00 (SEGC00) | 2 | Node | SEGC00 |  | SEGC00 | SEG |  |  |
| < SE0005 (SE0005) > | 3 | Consolidation Segment | SE0005 |  | SE0005 | SEGC00 |  |  |
| \|- SEGB00 (SEGB00) | 2 | Node | SEGB00 |  | SEGB00 | SEG |  |  |
| < SE0003 (SE0003) > | 3 | Consolidation Segment | SE0003 |  | SE0003 | SEGB00 |  |  |
| < SE0004 (SE0004) > | 3 | Consolidation Segment | SE0004 |  | SE0004 | SEGB00 |  |  |
| \|- SEGA00 (SEGA00) | 2 | Node | SEGA00 |  | SEGA00 | SEG |  |  |
| < SE0001 (SE0001) > | 3 | Consolidation Segment | SE0001 |  | SE0001 | SEGA00 |  |  |
| < SE0002 (SE0002) > | 3 | Consolidation Segment | SE0002 |  | SE0002 | SEGA00 |  |  |

### Sheet: Validation (hidden)

| Node | Consolidation Segment | Root | Reference Node |  |
| --- | --- | --- | --- | --- |
| {"CLIENT":"","VER_ID":"42010AEF4E361EEDBC92308CFCFBC049","VER_PID":"","VER_STATUS":"S","VER_VLDFM":"20160101","VER_VLDTO":"99991231","VER_MSG":"","VER_NBR":"","VER_IDX":"000000000000001","HIER_HID":"SEG","HIER_CATG":"CS01","UPDATED_AT":20230512065621 ,"UPDATED_BY":"_SAPI061738","CREATED_AT":20230512065211 ,"CREATED_BY":"_SAPI061738","LOCKED_BY":"","LOCKED_AT":0 ,"ALLOW_LEGACY_TCODE_USAGE":"","VER_SRC":"","MAINTENANCE_LANG":"E","REF_UPDATED_AT":0 ,"CREATED_ON":"20230512","CATEGORYTEXT":"Consolidation Segment","HIER_DESC":"SEGMENT","HRY_CLASS":"","STATUSTEXT":"Draft","SIMULATE_REPORT_ID":"","ACTIVE_REPORT_ID":"","IS_UNASSIGNED_SHOW":"","IS_RANGE_SUPPORTED":"X","HIDE_VALIDITY":"","ATTRIBUTEVALUES":"","LOCK_HIER_ATTR_EDIT":"","HIERARCHY_TAG":"","HIERARCHY_TAG_TEXT":"","HAS_REFERENCE_NODE":"","ISPRIVATE":"","VIAJOB":"","ACTJOBNAME":"","ACTJOBCOUNT":"","ACTJOBSTATUS":"","ACTJOBACTION":"","DOWNLOADJOBNAME":"","DOWNLOADJOBCOUNT":"","DOWNLOADJOBSTATUS":"","DOWNLOADJOBACTION":""} | [] |  |  |  |
| 7 |  |  |  |  |
| G |  |  | H | I |
|  |  | F | E |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2308-brd-consolidation-profit-center-9]]
- related-to :: [[07-group-reporting-and-consolidation/2308-lob-consolidation-profit-center-54]]
- related-to :: [[07-group-reporting-and-consolidation/2308-region-consolidation-unit-69]]
- related-to :: [[07-group-reporting-and-consolidation/2402-brd-consolidation-profit-center-72]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_SEG_Consolidation_Segment.xlsx` — full document · extracted with `xlsx2md` · 2,348 chars in the whole document
