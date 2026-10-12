---
id: 07-group-reporting-and-consolidation/2308-region-consolidation-unit-69
title: 2308 REGION Consolidation Unit (2308_REGION_Consolidation_Unit)
description: "Consolidation unit hierarchy REGION (valid 01/01/2016 to 12/31/9999): NA, EMEA and APJ nodes with eight consolidation units MXX00 to MXX08 (excluding MXX01)."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/consolidation-hierarchy-uploads]
aliases: [2308_REGION_Consolidation_Unit]
keywords: ["Consolidation Hierarchy Upload Samples (Region, Segment…", consolidation unit hierarchy, consolidation units, regional grouping, hierarchy validity, hierarchy import template, 2308]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_REGION_Consolidation_Unit.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-69
topic: 07-group-reporting-and-consolidation/consolidation-hierarchy-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2308 REGION Consolidation Unit (2308_REGION_Consolidation_Unit)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_REGION_Consolidation_Unit.xlsx`, extracted with `xlsx2md`. Grouped under **Consolidation Hierarchy Upload Samples (Region, Segment, Brand, Line of Business)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2308 REGION Consolidation Unit

### Sheet: Sheet1

| Consolidation Unit |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hierarchy ID: | REGION |  |  |  |  |  |  |  |
| Valid From: | 01/01/2016 |  |  |  |  |  |  |  |
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

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2308-brd-consolidation-profit-center-9]]
- related-to :: [[07-group-reporting-and-consolidation/2308-lob-consolidation-profit-center-54]]
- related-to :: [[07-group-reporting-and-consolidation/2308-seg-consolidation-segment-70]]
- related-to :: [[07-group-reporting-and-consolidation/2402-brd-consolidation-profit-center-72]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_REGION_Consolidation_Unit.xlsx` — full document · extracted with `xlsx2md` · 1,347 chars in the whole document
