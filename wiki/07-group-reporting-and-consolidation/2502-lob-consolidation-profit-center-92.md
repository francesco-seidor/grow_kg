---
id: 07-group-reporting-and-consolidation/2502-lob-consolidation-profit-center-92
title: 2502 LOB Consolidation Profit Center (2502_LOB_Consolidation_Profit_Center)
description: "2502 hierarchy LOB (Lines of Business) grouping consolidation profit centers PC0001-PC0010 under nodes LOBA00/LOBB00/LOBC00, controlling area A000."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/consolidation-hierarchy-uploads]
aliases: [2502_LOB_Consolidation_Profit_Center]
keywords: ["Consolidation Hierarchy Upload Samples (Region, Segment…", consolidation profit center hierarchy, lines of business hierarchy, profit center assignment, controlling area, hierarchy validity, hierarchy metadata, 2502]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2502_LOB_Consolidation_Profit_Center.xlsx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-92
topic: 07-group-reporting-and-consolidation/consolidation-hierarchy-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2502 LOB Consolidation Profit Center (2502_LOB_Consolidation_Profit_Center)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2502_LOB_Consolidation_Profit_Center.xlsx`, extracted with `xlsx2md`. Grouped under **Consolidation Hierarchy Upload Samples (Region, Segment, Brand, Line of Business)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2502 LOB Consolidation Profit Center

### Sheet: Hierarchy

| Consolidation Profit Center |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchy ID: | LOB |  |  |  |  |  |  |  |
| Valid From: | 2023-12-31 |  |  |  |  |  |  |  |
| Valid To: | 12/31/9999 |  |  |  |  |  |  |  |
| Consolidation Controlling Area: | A000 |  |  |  |  |  |  |  |
| Consolidation Profit Center | Level | Type | ID (From) | ID (To) | Description (English) | Parent ID | Reference Hierarchy ID | Reference Hierarchy Validity |
| \|- LOB (Lines of Business) | 1 | Root | LOB |  | Lines of Business |  |  |  |
| \|- LOBC00 (LOBC00) | 2 | Node | LOBC00 |  | LOBC00 | LOB |  |  |
| < PC0008 (PC0008) > | 3 | Consolidation Profit Center | PC0008 |  | PC0008 | LOBC00 |  |  |
| < PC0009 (PC0009) > | 3 | Consolidation Profit Center | PC0009 |  | PC0009 | LOBC00 |  |  |
| < PC0010 (PC0010) > | 3 | Consolidation Profit Center | PC0010 |  | PC0010 | LOBC00 |  |  |
| \|- LOBB00 (LOBB00) | 2 | Node | LOBB00 |  | LOBB00 | LOB |  |  |
| < PC0004 (PC0004) > | 3 | Consolidation Profit Center | PC0004 |  | PC0004 | LOBB00 |  |  |
| < PC0005 (PC0005) > | 3 | Consolidation Profit Center | PC0005 |  | PC0005 | LOBB00 |  |  |
| < PC0006 (PC0006) > | 3 | Consolidation Profit Center | PC0006 |  | PC0006 | LOBB00 |  |  |
| < PC0007 (PC0007) > | 3 | Consolidation Profit Center | PC0007 |  | PC0007 | LOBB00 |  |  |
| \|- LOBA00 (LOBA00) | 2 | Node | LOBA00 |  | LOBA00 | LOB |  |  |
| < PC0001 (PC0001) > | 3 | Consolidation Profit Center | PC0001 |  | PC0001 | LOBA00 |  |  |
| < PC0002 (PC0002) > | 3 | Consolidation Profit Center | PC0002 |  | PC0002 | LOBA00 |  |  |
| < PC0003 (PC0003) > | 3 | Consolidation Profit Center | PC0003 |  | PC0003 | LOBA00 |  |  |

### Sheet: Validation (hidden)

| Node | Consolidation Profit Center | Root | Reference Node |  |
| --- | --- | --- | --- | --- |
| {"CLIENT":"","VER_ID":"42010AEF4E0E1EEDBBFD884E6A62488C","VER_PID":"","VER_STATUS":"S","VER_VLDFM":"20160101","VER_VLDTO":"99991231","VER_MSG":"","VER_NBR":"","VER_IDX":"000000000000001","HIER_HID":"LOB","HIER_CATG":"CS04","UPDATED_AT":20230512064946 ,"UPDATED_BY":"_SAPI061738","CREATED_AT":20230511110912 ,"CREATED_BY":"CB9980001486","LOCKED_BY":"","LOCKED_AT":0 ,"ALLOW_LEGACY_TCODE_USAGE":"","VER_SRC":"","MAINTENANCE_LANG":"E","REF_UPDATED_AT":0 ,"CREATED_ON":"20230511","CATEGORYTEXT":"Consolidation Profit Center","HIER_DESC":"Lines of Business","HRY_CLASS":"","STATUSTEXT":"Draft","SIMULATE_REPORT_ID":"","ACTIVE_REPORT_ID":"","IS_UNASSIGNED_SHOW":"","IS_RANGE_SUPPORTED":"X","HIDE_VALIDITY":"","ATTRIBUTEVALUES":"","LOCK_HIER_ATTR_EDIT":"","HIERARCHY_TAG":"","HIERARCHY_TAG_TEXT":"","HAS_REFERENCE_NODE":"","ISPRIVATE":"","VIAJOB":"","ACTJOBNAME":"","ACTJOBCOUNT":"","ACTJOBSTATUS":"","ACTJOBACTION":"","DOWNLOADJOBNAME":"","DOWNLOADJOBCOUNT":"","DOWNLOADJOBSTATUS":"","DOWNLOADJOBACTION":""} | [{"CLIENT":"","OBJ_ID":"42010AEF4E0E1EEDBBFD884E6A62488C","FLD_NAME":"CONTROLLINGAREA","VAL_SIGN":"S","VAL_LOW":"A000","VAL_HIGH":"","VER_ID":"42010AEF4E0E1EEDBBFD884E6A62488C","VAL_LOW_TEXT":"","VAL_HIGH_TEXT":"","LANG":""}] |  |  |  |
| 8 |  |  |  |  |
| G |  |  | H | I |
|  |  | F | E |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Visible header Valid From is 2023-12-31 but the hidden Validation sheet still records VER_VLDFM 20160101 (the 2308 version shows 01/01/2016 in both places).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2502-brd-consolidation-profit-center-86]]
- related-to :: [[07-group-reporting-and-consolidation/2502-region-consolidation-unit-94]]
- related-to :: [[07-group-reporting-and-consolidation/2502-seg-consolidation-segment-95]]
- related-to :: [[07-group-reporting-and-consolidation/2308-brd-consolidation-profit-center-9]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2502_LOB_Consolidation_Profit_Center.xlsx` — full document · extracted with `xlsx2md` · 3,196 chars in the whole document
