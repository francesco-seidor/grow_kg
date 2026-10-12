---
id: 07-group-reporting-and-consolidation/2602-region-consolidation-unit-107
title: 2602 REGION Consolidation Unit (2602_REGION_Consolidation_Unit)
description: "Sample consolidation unit hierarchy REGION grouping units MXX00-MXX08 into NA, EMEA and APJ nodes by country, with node validity 20231231 to 99991231."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/consolidation-hierarchy-uploads]
aliases: [2602_REGION_Consolidation_Unit]
keywords: ["Consolidation Hierarchy Upload Samples (Region, Segment…", consolidation unit, consolidation hierarchy, region hierarchy, node validity, hierarchy version status, 2602]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2602_REGION_Consolidation_Unit.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-107
topic: 07-group-reporting-and-consolidation/consolidation-hierarchy-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2602 REGION Consolidation Unit (2602_REGION_Consolidation_Unit)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2602_REGION_Consolidation_Unit.xlsx`, extracted with `xlsx2md`. Grouped under **Consolidation Hierarchy Upload Samples (Region, Segment, Brand, Line of Business)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2602 REGION Consolidation Unit

### Sheet: Hierarchy

| Consolidation Unit |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchy ID: | REGION |  |  |  |  |  |  |  |  |  |
| Valid From: | N/A |  |  |  |  |  |  |  |  |  |
| Valid To: | N/A |  |  |  |  |  |  |  |  |  |
| Consolidation Unit | Level | Type | ID (From) | ID (To) | Node Valid From (YYYYMMDD) | Node Valid To (YYYYMMDD) | Description | Parent ID | Reference Hierarchy ID | Reference Hierarchy Validity |
| \|- REGION (REGION) | 1 | Root | REGION |  | 20231231 | 99991231 | REGION |  |  |  |
|  |  | Node | NA |  | 20231231 | 99991231 | NA | REGION |  |  |
|  |  | Consolidation Unit | MXX03 |  | 20231231 | 99991231 | USA East | NA |  |  |
|  |  | Consolidation Unit | MXX04 |  | 20231231 | 99991231 | USA West | NA |  |  |
|  |  | Node | EMEA |  | 20231231 | 99991231 | EMEA | REGION |  |  |
|  |  | Consolidation Unit | MXX00 |  | 20231231 | 99991231 | Germany | EMEA |  |  |
|  |  | Consolidation Unit | MXX02 |  | 20231231 | 99991231 | France | EMEA |  |  |
|  |  | Consolidation Unit | MXX05 |  | 20231231 | 99991231 | Belgium | EMEA |  |  |
|  |  | Consolidation Unit | MXX07 |  | 20231231 | 99991231 | Austria | EMEA |  |  |
|  |  | Node | APJ |  | 20231231 | 99991231 | APJ | REGION |  |  |
|  |  | Consolidation Unit | MXX06 |  | 20231231 | 99991231 | Japan | APJ |  |  |
|  |  | Consolidation Unit | MXX08 |  | 20231231 | 99991231 | China | APJ |  |  |

### Sheet: Validation (hidden)

| Node | Node: Consolidation Group | Consolidation Unit | Root | Reference Node |
| --- | --- | --- | --- | --- |
| {"CLIENT":"","VER_ID":"42010AEEC4581FD0AFDA24D17D0BDFF2","VER_PID":"","VER_STATUS":"S","VER_VLDFM":"00000000","VER_VLDTO":"00000000","VER_MSG":"","VER_NBR":"","VER_IDX":"000000000000001","HIER_HID":"REGION","HIER_CATG":"CS17","UPDATED_AT":20251111073636 ,"UPDATED_BY":"CB9980000750","CREATED_AT":20251111073636 ,"CREATED_BY":"CB9980000750","LOCKED_BY":"CB9980000750","LOCKED_AT":20251111073647 ,"ALLOW_LEGACY_TCODE_USAGE":"","VER_SRC":"","MAINTENANCE_LANG":"E","REF_UPDATED_AT":0 ,"NODE_TIMEDEP":"X","CREATED_ON":"20251111","CATEGORYTEXT":"Consolidation Unit","HIER_DESC":"REGION","HRY_CLASS":"","STATUSTEXT":"Draft","SIMULATE_REPORT_ID":"","ACTIVE_REPORT_ID":"","IS_UNASSIGNED_SHOW":"X","IS_RANGE_SUPPORTED":"X","HIDE_VALIDITY":"X","ATTRIBUTEVALUES":"","LOCK_HIER_ATTR_EDIT":"","HIERARCHY_TAG":"","HIERARCHY_TAG_TEXT":"","HAS_REFERENCE_NODE":"","ISPRIVATE":"","VIAJOB":"","ACTJOBNAME":"","ACTJOBCOUNT":"","ACTJOBSTATUS":"","ACTJOBACTION":"","DOWNLOADJOBNAME":"","DOWNLOADJOBCOUNT":"","DOWNLOADJOBSTATUS":"","DOWNLOADJOBACTION":"","HAS_REF_BY_NODE":""} | [] |  |  |  |
| 7 |  |  |  |  |
| I |  |  | J | K |
|  |  | H | E |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2602-brd-consolidation-profit-center-100]]
- related-to :: [[07-group-reporting-and-consolidation/2602-lob-consolidation-profit-center-101]]
- related-to :: [[07-group-reporting-and-consolidation/2602-seg-consolidation-segment-108]]
- related-to :: [[07-group-reporting-and-consolidation/2308-brd-consolidation-profit-center-9]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2602_REGION_Consolidation_Unit.xlsx` — full document · extracted with `xlsx2md` · 2,757 chars in the whole document
