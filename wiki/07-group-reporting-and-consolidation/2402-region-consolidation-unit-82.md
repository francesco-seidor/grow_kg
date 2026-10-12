---
id: 07-group-reporting-and-consolidation/2402-region-consolidation-unit-82
title: 2402 REGION Consolidation Unit (2402_REGION_Consolidation_Unit)
description: "REGION consolidation unit hierarchy (2402): NA, EMEA, APJ nodes grouping eight units MXX00-MXX08; valid 2021-12-31 to 12/31/9999; hidden draft metadata."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/consolidation-hierarchy-uploads]
aliases: [2402_REGION_Consolidation_Unit]
keywords: ["Consolidation Hierarchy Upload Samples (Region, Segment…", consolidation unit hierarchy, region hierarchy, consolidation units, hierarchy validity, hierarchy metadata, 2402]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2402_REGION_Consolidation_Unit.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-82
topic: 07-group-reporting-and-consolidation/consolidation-hierarchy-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2402 REGION Consolidation Unit (2402_REGION_Consolidation_Unit)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2402_REGION_Consolidation_Unit.xlsx`, extracted with `xlsx2md`. Grouped under **Consolidation Hierarchy Upload Samples (Region, Segment, Brand, Line of Business)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2402 REGION Consolidation Unit

### Sheet: Hierarchy

| Consolidation Unit |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchy ID: | REGION |  |  |  |  |  |  |  |
| Valid From: | 2021-12-31 |  |  |  |  |  |  |  |
| Valid To: | 12/31/9999 |  |  |  |  |  |  |  |
| Consolidation Unit | Level | Type | ID (From) | ID (To) | Description (English) | Parent ID | Reference Hierarchy ID | Reference Hierarchy Validity |
| \|- REGION (REGION) | 1 | Root | REGION |  | REGION |  |  |  |
| \|- NA (NA) | 2 | Node | NA |  | NA | REGION |  |  |
| < MXX03 (USA East) > | 3 | Consolidation Unit | MXX03 |  | USA East | NA |  |  |
| < MXX04 (USA West) > | 3 | Consolidation Unit | MXX04 |  | USA West | NA |  |  |
| \|- EMEA (EMEA) | 2 | Node | EMEA |  | EMEA | REGION |  |  |
| < MXX00 (Germany) > | 3 | Consolidation Unit | MXX00 |  | Germany | EMEA |  |  |
| < MXX02 (France) > | 3 | Consolidation Unit | MXX02 |  | France | EMEA |  |  |
| < MXX05 (Belgium) > | 3 | Consolidation Unit | MXX05 |  | Belgium | EMEA |  |  |
| < MXX07 (Austria) > | 3 | Consolidation Unit | MXX07 |  | Austria | EMEA |  |  |
| \|- APJ (APJ) | 2 | Node | APJ |  | APJ | REGION |  |  |
| < MXX06 (Japan) > | 3 | Consolidation Unit | MXX06 |  | Japan | APJ |  |  |
| < MXX08 (China) > | 3 | Consolidation Unit | MXX08 |  | China | APJ |  |  |

### Sheet: Validation (hidden)

| Node | Consolidation Unit | Root | Reference Node |  |
| --- | --- | --- | --- | --- |
| {"CLIENT":"","VER_ID":"42010AEF4E5F1EDDBC924E80A6DEC284","VER_PID":"","VER_STATUS":"S","VER_VLDFM":"20160101","VER_VLDTO":"99991231","VER_MSG":"","VER_NBR":"","VER_IDX":"000000000000001","HIER_HID":"REGION","HIER_CATG":"CS17","UPDATED_AT":20230512070126 ,"UPDATED_BY":"_SAPI061738","CREATED_AT":20230512065852 ,"CREATED_BY":"_SAPI061738","LOCKED_BY":"","LOCKED_AT":0 ,"ALLOW_LEGACY_TCODE_USAGE":"","VER_SRC":"","MAINTENANCE_LANG":"E","REF_UPDATED_AT":0 ,"CREATED_ON":"20230512","CATEGORYTEXT":"Consolidation Unit","HIER_DESC":"REGION","HRY_CLASS":"","STATUSTEXT":"Draft","SIMULATE_REPORT_ID":"","ACTIVE_REPORT_ID":"","IS_UNASSIGNED_SHOW":"","IS_RANGE_SUPPORTED":"X","HIDE_VALIDITY":"","ATTRIBUTEVALUES":"","LOCK_HIER_ATTR_EDIT":"","HIERARCHY_TAG":"","HIERARCHY_TAG_TEXT":"","HAS_REFERENCE_NODE":"","ISPRIVATE":"","VIAJOB":"","ACTJOBNAME":"","ACTJOBCOUNT":"","ACTJOBSTATUS":"","ACTJOBACTION":"","DOWNLOADJOBNAME":"","DOWNLOADJOBCOUNT":"","DOWNLOADJOBSTATUS":"","DOWNLOADJOBACTION":""} | [] |  |  |  |
| 7 |  |  |  |  |
| G |  |  | H | I |
|  |  | F | E |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2402-brd-consolidation-profit-center-72]]
- related-to :: [[07-group-reporting-and-consolidation/2402-lob-consolidation-profit-center-76]]
- related-to :: [[07-group-reporting-and-consolidation/2402-seg-consolidation-segment-83]]
- related-to :: [[07-group-reporting-and-consolidation/2308-brd-consolidation-profit-center-9]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2402_REGION_Consolidation_Unit.xlsx` — full document · extracted with `xlsx2md` · 2,530 chars in the whole document
