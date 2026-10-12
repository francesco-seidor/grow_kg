---
id: 07-group-reporting-and-consolidation/2608-brd-consolidation-profit-center-110
title: 2608 BRD Consolidation Profit Center (2608_BRD_Consolidation_Profit_Center)
description: "2608 hierarchy BRD (Brand) grouping consolidation profit centers PC0001-PC0010 under nodes BRDA00/BRDB00/BRDC00, controlling area A000."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/consolidation-hierarchy-uploads]
aliases: [2608_BRD_Consolidation_Profit_Center]
keywords: ["Consolidation Hierarchy Upload Samples (Region, Segment…", consolidation profit center hierarchy, brand hierarchy, profit center assignment, controlling area, hierarchy validity, hierarchy metadata, 2608]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_BRD_Consolidation_Profit_Center.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-110
topic: 07-group-reporting-and-consolidation/consolidation-hierarchy-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2608 BRD Consolidation Profit Center (2608_BRD_Consolidation_Profit_Center)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_BRD_Consolidation_Profit_Center.xlsx`, extracted with `xlsx2md`. Grouped under **Consolidation Hierarchy Upload Samples (Region, Segment, Brand, Line of Business)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2608 BRD Consolidation Profit Center

### Sheet: Hierarchy

| Consolidation Profit Center |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchy ID: | BRD |  |  |  |  |  |  |  |  |  |
| Valid From: | N/A |  |  |  |  |  |  |  |  |  |
| Valid To: | N/A |  |  |  |  |  |  |  |  |  |
| Controlling Area: | A000 |  |  |  |  |  |  |  |  |  |
| Consolidation Profit Center | Level | Type | ID (From) | ID (To) | Node Valid From (YYYYMMDD) | Node Valid To (YYYYMMDD) | Description | Parent ID | Reference Hierarchy ID | Reference Hierarchy Validity |
| \|- BRD (Brand) | 1 | Root | BRD |  | 20251231 | 99991231 | Brand |  |  |  |
|  |  | Node | BRDB00 |  | 20251231 | 99991231 | BRDB00 | BRD |  |  |
|  |  | Consolidation Profit Center | PC0004 |  | 20251231 | 99991231 | PC0004 | BRDB00 |  |  |
|  |  | Consolidation Profit Center | PC0006 |  | 20251231 | 99991231 | PC0006 | BRDB00 |  |  |
|  |  | Consolidation Profit Center | PC0007 |  | 20251231 | 99991231 | PC0007 | BRDB00 |  |  |
|  |  | Node | BRDA00 |  | 20251231 | 99991231 | BRDA00 | BRD |  |  |
|  |  | Consolidation Profit Center | PC0001 |  | 20251231 | 99991231 | PC0001 | BRDA00 |  |  |
|  |  | Consolidation Profit Center | PC0005 |  | 20251231 | 99991231 | PC0005 | BRDA00 |  |  |
|  |  | Consolidation Profit Center | PC0009 |  | 20251231 | 99991231 | PC0009 | BRDA00 |  |  |
|  |  | Consolidation Profit Center | PC0010 |  | 20251231 | 99991231 | PC0010 | BRDA00 |  |  |
|  |  | Node | BRDC00 |  | 20251231 | 99991231 | BRDC00 | BRD |  |  |
|  |  | Consolidation Profit Center | PC0008 |  | 20251231 | 99991231 | PC0008 | BRDC00 |  |  |
|  |  | Consolidation Profit Center | PC0002 |  | 20251231 | 99991231 | PC0002 | BRDC00 |  |  |
|  |  | Consolidation Profit Center | PC0003 |  | 20251231 | 99991231 | PC0003 | BRDC00 |  |  |

### Sheet: Validation (hidden)

| Node | Consolidation Profit Center | Root | Reference Node |  |
| --- | --- | --- | --- | --- |
| {"CLIENT":"","VER_ID":"42010AEEC4581FE0AFF27F7410744085","VER_PID":"","VER_STATUS":"S","VER_VLDFM":"00000000","VER_VLDTO":"00000000","VER_MSG":"","VER_NBR":"","VER_IDX":"000000000000001","HIER_HID":"BRD","HIER_CATG":"CS04","UPDATED_AT":20251112065115 ,"UPDATED_BY":"CB9980000750","CREATED_AT":20251112065115 ,"CREATED_BY":"CB9980000750","LOCKED_BY":"CB9980000750","LOCKED_AT":20251112065127 ,"ALLOW_LEGACY_TCODE_USAGE":"","VER_SRC":"","MAINTENANCE_LANG":"E","REF_UPDATED_AT":0 ,"NODE_TIMEDEP":"X","CREATED_ON":"20251112","CATEGORYTEXT":"Consolidation Profit Center","HIER_DESC":"Brand","HRY_CLASS":"","STATUSTEXT":"Draft","SIMULATE_REPORT_ID":"","ACTIVE_REPORT_ID":"","IS_UNASSIGNED_SHOW":"X","IS_RANGE_SUPPORTED":"X","HIDE_VALIDITY":"X","ATTRIBUTEVALUES":"","LOCK_HIER_ATTR_EDIT":"","HIERARCHY_TAG":"","HIERARCHY_TAG_TEXT":"","HAS_REFERENCE_NODE":"","ISPRIVATE":"","VIAJOB":"","ACTJOBNAME":"","ACTJOBCOUNT":"","ACTJOBSTATUS":"","ACTJOBACTION":"","DOWNLOADJOBNAME":"","DOWNLOADJOBCOUNT":"","DOWNLOADJOBSTATUS":"","DOWNLOADJOBACTION":"","HAS_REF_BY_NODE":""} | [{"CLIENT":"","OBJ_ID":"42010AEEC4581FE0AFF27F7410744085","FLD_NAME":"CONTROLLINGAREA","VAL_SIGN":"S","VAL_LOW":"A000","VAL_HIGH":"","VER_ID":"42010AEEC4581FE0AFF27F7410744085","VAL_LOW_TEXT":"","VAL_HIGH_TEXT":"","LANG":""}] |  |  |  |
| 8 |  |  |  |  |
| I |  |  | J | K |
|  |  | H | E |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2608-lob-consolidation-profit-center-116]]
- related-to :: [[07-group-reporting-and-consolidation/2608-region-consolidation-unit-127]]
- related-to :: [[07-group-reporting-and-consolidation/2608-seg-consolidation-segment-128]]
- related-to :: [[07-group-reporting-and-consolidation/2308-brd-consolidation-profit-center-9]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2608_BRD_Consolidation_Profit_Center.xlsx` — full document · extracted with `xlsx2md` · 3,336 chars in the whole document
