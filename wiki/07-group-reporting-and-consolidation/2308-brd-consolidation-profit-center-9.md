---
id: 07-group-reporting-and-consolidation/2308-brd-consolidation-profit-center-9
title: 2308 BRD Consolidation Profit Center (2308_BRD_Consolidation_Profit_Center)
description: "Sample consolidation profit center hierarchy BRD (Brand), controlling area A000: root, nodes BRDA00/BRDB00/BRDC00 and profit centers PC0001-PC0010."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/consolidation-hierarchy-uploads]
aliases: [2308_BRD_Consolidation_Profit_Center]
keywords: ["Consolidation Hierarchy Upload Samples (Region, Segment…", consolidation profit center, profit center hierarchy, consolidation hierarchy, consolidation controlling area, hierarchy validity, hierarchy version status, 2308]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_BRD_Consolidation_Profit_Center.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-9
topic: 07-group-reporting-and-consolidation/consolidation-hierarchy-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2308 BRD Consolidation Profit Center (2308_BRD_Consolidation_Profit_Center)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_BRD_Consolidation_Profit_Center.xlsx`, extracted with `xlsx2md`. Grouped under **Consolidation Hierarchy Upload Samples (Region, Segment, Brand, Line of Business)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2308 BRD Consolidation Profit Center

### Sheet: Hierarchy

| Consolidation Profit Center |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchy ID: | BRD |  |  |  |  |  |  |  |
| Valid From: | 01/01/2016 |  |  |  |  |  |  |  |
| Valid To: | 12/31/9999 |  |  |  |  |  |  |  |
| Consolidation Controlling Area: | A000 |  |  |  |  |  |  |  |
| Consolidation Profit Center | Level | Type | ID (From) | ID (To) | Description (English) | Parent ID | Reference Hierarchy ID | Reference Hierarchy Validity |
| \|- BRD (Brand) | 1 | Root | BRD |  | Brand |  |  |  |
| \|- BRDB00 (BRDB00) | 2 | Node | BRDB00 |  | BRDB00 | BRD |  |  |
| < PC0004 (PC0004) > | 3 | Consolidation Profit Center | PC0004 |  | PC0004 | BRDB00 |  |  |
| < PC0006 (PC0006) > | 3 | Consolidation Profit Center | PC0006 |  | PC0006 | BRDB00 |  |  |
| < PC0007 (PC0007) > | 3 | Consolidation Profit Center | PC0007 |  | PC0007 | BRDB00 |  |  |
| \|- BRDA00 (BRDA00) | 2 | Node | BRDA00 |  | BRDA00 | BRD |  |  |
| < PC0001 (PC0001) > | 3 | Consolidation Profit Center | PC0001 |  | PC0001 | BRDA00 |  |  |
| < PC0005 (PC0005) > | 3 | Consolidation Profit Center | PC0005 |  | PC0005 | BRDA00 |  |  |
| < PC0009 (PC0009) > | 3 | Consolidation Profit Center | PC0009 |  | PC0009 | BRDA00 |  |  |
| < PC0010 (PC0010) > | 3 | Consolidation Profit Center | PC0010 |  | PC0010 | BRDA00 |  |  |
| \|- BRDC00 (BRDC00) | 2 | Node | BRDC00 |  | BRDC00 | BRD |  |  |
| < PC0008 (PC0008) > | 3 | Consolidation Profit Center | PC0008 |  | PC0008 | BRDC00 |  |  |
| < PC0002 (PC0002) > | 3 | Consolidation Profit Center | PC0002 |  | PC0002 | BRDC00 |  |  |
| < PC0003 (PC0003) > | 3 | Consolidation Profit Center | PC0003 |  | PC0003 | BRDC00 |  |  |

### Sheet: Validation (hidden)

| Node | Consolidation Profit Center | Root | Reference Node |  |
| --- | --- | --- | --- | --- |
| {"CLIENT":"","VER_ID":"42010AEF4E0E1EEDBBFD902816FAAB7C","VER_PID":"","VER_STATUS":"S","VER_VLDFM":"20160101","VER_VLDTO":"99991231","VER_MSG":"","VER_NBR":"","VER_IDX":"000000000000001","HIER_HID":"BRD","HIER_CATG":"CS04","UPDATED_AT":20230512063718 ,"UPDATED_BY":"_SAPI061738","CREATED_AT":20230511111058 ,"CREATED_BY":"CB9980001486","LOCKED_BY":"","LOCKED_AT":0 ,"ALLOW_LEGACY_TCODE_USAGE":"","VER_SRC":"","MAINTENANCE_LANG":"E","REF_UPDATED_AT":0 ,"CREATED_ON":"20230511","CATEGORYTEXT":"Consolidation Profit Center","HIER_DESC":"Brand","HRY_CLASS":"","STATUSTEXT":"Draft","SIMULATE_REPORT_ID":"","ACTIVE_REPORT_ID":"","IS_UNASSIGNED_SHOW":"","IS_RANGE_SUPPORTED":"X","HIDE_VALIDITY":"","ATTRIBUTEVALUES":"","LOCK_HIER_ATTR_EDIT":"","HIERARCHY_TAG":"","HIERARCHY_TAG_TEXT":"","HAS_REFERENCE_NODE":"","ISPRIVATE":"","VIAJOB":"","ACTJOBNAME":"","ACTJOBCOUNT":"","ACTJOBSTATUS":"","ACTJOBACTION":"","DOWNLOADJOBNAME":"","DOWNLOADJOBCOUNT":"","DOWNLOADJOBSTATUS":"","DOWNLOADJOBACTION":""} | [{"CLIENT":"","OBJ_ID":"42010AEF4E0E1EEDBBFD902816FAAB7C","FLD_NAME":"CONTROLLINGAREA","VAL_SIGN":"S","VAL_LOW":"A000","VAL_HIGH":"","VER_ID":"42010AEF4E0E1EEDBBFD902816FAAB7C","VAL_LOW_TEXT":"","VAL_HIGH_TEXT":"","LANG":""}] |  |  |  |
| 8 |  |  |  |  |
| G |  |  | H | I |
|  |  | F | E |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2308-lob-consolidation-profit-center-54]]
- related-to :: [[07-group-reporting-and-consolidation/2308-region-consolidation-unit-69]]
- related-to :: [[07-group-reporting-and-consolidation/2308-seg-consolidation-segment-70]]
- related-to :: [[07-group-reporting-and-consolidation/2402-brd-consolidation-profit-center-72]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_BRD_Consolidation_Profit_Center.xlsx` — full document · extracted with `xlsx2md` · 3,160 chars in the whole document
