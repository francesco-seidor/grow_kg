---
id: 07-group-reporting-and-consolidation/upload-zb2-2024-cgrxx-srd2-209
title: UPLOAD ZB2 2024 CGRXX SRD2 (UPLOAD_ZB2_2024_CGRXX_SRD2)
description: "Consolidation upload spreadsheet (version ZB2, FY2024 periods 4-12) with intercompany FS item postings between units MXX00-MXX08; periodic, overwrite mode."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/intercompany-version-uploads]
aliases: [UPLOAD_ZB2_2024_CGRXX_SRD2]
keywords: ["Sample Uploads for Consolidation Versions ZB2, ZB4 and ZF2", consolidation data upload, upload parameters, financial statement items, intercompany postings, consolidation units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/UPLOAD_ZB2_2024_CGRXX_SRD2.xlsx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-209
topic: 07-group-reporting-and-consolidation/intercompany-version-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# UPLOAD ZB2 2024 CGRXX SRD2 (UPLOAD_ZB2_2024_CGRXX_SRD2)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/UPLOAD_ZB2_2024_CGRXX_SRD2.xlsx`, extracted with `xlsx2md`. Grouped under **Sample Uploads for Consolidation Versions ZB2, ZB4 and ZF2** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## UPLOAD ZB2 2024 CGRXX SRD2

### Sheet: UPLOAD_ZB4_2024_SRD2

| * Parameters |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P | PERIODICAL | X | Input Type | X:periodic | blank: YTD |  |  |  |  |  |  |
| P | UPDATEMODE | 2 | Update Mode: | 1: Delete all | 2: Overwrite | 5: Add |  |  |  |  |  |
| P | DOCTY | 00 | Document type | 00; 0B… | if empty the first doctype posting level 00 will be taken |  |  |  |  |  |  |
| * |  |  |  |  |  |  |  |  |  |  |  |
| D | ConsolidationChartOfAccounts | ConsolidationVersion | FiscalYear | FiscalPeriod | ConsolidationUnit | FinancialStatementItem | SubItem | PartnerConsolidationUnit | Segment | ControllingArea | AmountInLocalCurrency |
| *D | RITCLG | RVERS | RYEAR | POPER | RBUNIT | RITEM | SUBIT | RBUPTR | SEGMENT | KOKRS | HSL |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX00 | 181100 | 920 | MXX02 |  |  | 255 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX00 | 582000 | YB85 |  |  |  | -255 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX02 | 181200 | 915 | MXX03 |  |  | 150 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX02 | 585000 | YB85 |  |  |  | -150 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX03 | 181400 | 915 | MXX04 |  |  | 360 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX03 | 560000 | YB85 |  |  |  | -360 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX04 | 181600 | 915 | MXX05 |  |  | 270 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX04 | 515000 | YB85 | MXX06 |  |  | -270 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX05 | 181800 | 915 | MXX07 |  |  | 850 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX05 | 516000 | YB90 |  |  |  | -850 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX07 | 181890 | 915 |  |  |  | 790 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX07 | 517000 | YB90 |  |  |  | -790 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX08 | 183100 | 915 |  |  |  | 840 |
| 2 | Y1 | ZB2 | 2024 | 4 | MXX08 | 583000 | YB90 |  |  |  | -840 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX00 | 181100 | 920 | MXX02 |  |  | 160 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX00 | 582000 | YB85 |  |  |  | -160 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX02 | 181200 | 915 | MXX03 |  |  | 26 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX02 | 585000 | YB85 |  |  |  | -26 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX03 | 181400 | 915 | MXX04 |  |  | 785 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX03 | 560000 | YB85 |  |  |  | -785 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX04 | 181600 | 915 | MXX05 |  |  | 45 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX04 | 515000 | YB85 | MXX06 |  |  | -45 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX05 | 181800 | 915 | MXX07 |  |  | 950 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX05 | 516000 | YB90 |  |  |  | -950 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX07 | 181890 | 915 |  |  |  | 7200 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX07 | 517000 | YB90 |  |  |  | -7200 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX08 | 183100 | 915 |  |  |  | 8569 |
| 2 | Y1 | ZB2 | 2024 | 5 | MXX08 | 583000 | YB90 |  |  |  | -8569 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX00 | 181100 | 920 | MXX02 |  |  | 240 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX00 | 582000 | YB85 |  |  |  | -240 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX02 | 181200 | 915 | MXX03 |  |  | 39 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX02 | 585000 | YB85 |  |  |  | -39 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX03 | 181400 | 915 | MXX04 |  |  | 1178 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX03 | 560000 | YB85 |  |  |  | -1178 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX04 | 181600 | 915 | MXX05 |  |  | 68 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX04 | 515000 | YB85 | MXX06 |  |  | -68 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX05 | 181800 | 915 | MXX07 |  |  | 1425 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX05 | 516000 | YB90 |  |  |  | -1425 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX07 | 181890 | 915 |  |  |  | 10800 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX07 | 517000 | YB90 |  |  |  | -10800 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX08 | 183100 | 915 |  |  |  | 12854 |
| 2 | Y1 | ZB2 | 2024 | 6 | MXX08 | 583000 | YB90 |  |  |  | -12854 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX00 | 181100 | 920 | MXX02 |  |  | 306 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX00 | 582000 | YB85 |  |  |  | -306 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX02 | 181200 | 915 | MXX03 |  |  | 180 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX02 | 585000 | YB85 |  |  |  | -180 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX03 | 181400 | 915 | MXX04 |  |  | 432 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX03 | 560000 | YB85 |  |  |  | -432 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX04 | 181600 | 915 | MXX05 |  |  | 324 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX04 | 515000 | YB85 | MXX06 |  |  | -324 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX05 | 181800 | 915 | MXX07 |  |  | 1020 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX05 | 516000 | YB90 |  |  |  | -1020 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX07 | 181890 | 915 |  |  |  | 948 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX07 | 517000 | YB90 |  |  |  | -948 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX08 | 183100 | 915 |  |  |  | 1008 |
| 2 | Y1 | ZB2 | 2024 | 7 | MXX08 | 583000 | YB90 |  |  |  | -1008 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX00 | 181100 | 920 | MXX02 |  |  | 176 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX00 | 582000 | YB85 |  |  |  | -176 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX02 | 181200 | 915 | MXX03 |  |  | 30 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX02 | 585000 | YB85 |  |  |  | -30 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX03 | 181400 | 915 | MXX04 |  |  | 865 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX03 | 560000 | YB85 |  |  |  | -865 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX04 | 181600 | 915 | MXX05 |  |  | 50 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX04 | 515000 | YB85 | MXX06 |  |  | -50 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX05 | 181800 | 915 | MXX07 |  |  | 1045 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX05 | 516000 | YB90 |  |  |  | -1045 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX07 | 181890 | 915 |  |  |  | 7920 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX07 | 517000 | YB90 |  |  |  | -7920 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX08 | 183100 | 915 |  |  |  | 9427 |
| 2 | Y1 | ZB2 | 2024 | 8 | MXX08 | 583000 | YB90 |  |  |  | -9427 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX00 | 181100 | 920 | MXX02 |  |  | 204 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX00 | 582000 | YB85 |  |  |  | -204 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX02 | 181200 | 915 | MXX03 |  |  | 120 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX02 | 585000 | YB85 |  |  |  | -120 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX03 | 181400 | 915 | MXX04 |  |  | 288 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX03 | 560000 | YB85 |  |  |  | -288 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX04 | 181600 | 915 | MXX05 |  |  | 216 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX04 | 515000 | YB85 | MXX06 |  |  | -216 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX05 | 181800 | 915 | MXX07 |  |  | 680 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX05 | 516000 | YB90 |  |  |  | -680 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX07 | 181890 | 915 |  |  |  | 632 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX07 | 517000 | YB90 |  |  |  | -632 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX08 | 183100 | 915 |  |  |  | 672 |
| 2 | Y1 | ZB2 | 2024 | 9 | MXX08 | 583000 | YB90 |  |  |  | -672 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX00 | 181100 | 920 | MXX02 |  |  | 245 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX00 | 582000 | YB85 |  |  |  | -245 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX02 | 181200 | 915 | MXX03 |  |  | 145 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX02 | 585000 | YB85 |  |  |  | -145 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX03 | 181400 | 915 | MXX04 |  |  | 345 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX03 | 560000 | YB85 |  |  |  | -345 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX04 | 181600 | 915 | MXX05 |  |  | 260 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX04 | 515000 | YB85 | MXX06 |  |  | -260 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX05 | 181800 | 915 | MXX07 |  |  | 816 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX05 | 516000 | YB90 |  |  |  | -816 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX07 | 181890 | 915 |  |  |  | 760 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX07 | 517000 | YB90 |  |  |  | -760 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX08 | 183100 | 915 |  |  |  | 800 |
| 2 | Y1 | ZB2 | 2024 | 10 | MXX08 | 583000 | YB90 |  |  |  | -800 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX00 | 181100 | 920 | MXX02 |  |  | 150 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX00 | 582000 | YB85 |  |  |  | -150 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX02 | 181200 | 915 | MXX03 |  |  | 130 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX02 | 585000 | YB85 |  |  |  | -130 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX03 | 181400 | 915 | MXX04 |  |  | 70 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX03 | 560000 | YB85 |  |  |  | -70 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX04 | 181600 | 915 | MXX05 |  |  | 152 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX04 | 515000 | YB85 | MXX06 |  |  | -152 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX05 | 181800 | 915 | MXX07 |  |  | 165 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX05 | 516000 | YB90 |  |  |  | -165 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX07 | 181890 | 915 |  |  |  | 152 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX07 | 517000 | YB90 |  |  |  | -152 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX08 | 183100 | 915 |  |  |  | 160 |
| 2 | Y1 | ZB2 | 2024 | 11 | MXX08 | 583000 | YB90 |  |  |  | -160 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX00 | 181100 | 920 | MXX02 |  |  | 300 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX00 | 582000 | YB85 |  |  |  | -300 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX02 | 181200 | 915 | MXX03 |  |  | 260 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX02 | 585000 | YB85 |  |  |  | -260 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX03 | 181400 | 915 | MXX04 |  |  | 140 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX03 | 560000 | YB85 |  |  |  | -140 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX04 | 181600 | 915 | MXX05 |  |  | 304 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX04 | 515000 | YB85 | MXX06 |  |  | -304 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX05 | 181800 | 915 | MXX07 |  |  | 330 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX05 | 516000 | YB90 |  |  |  | -330 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX07 | 181890 | 915 |  |  |  | 304 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX07 | 517000 | YB90 |  |  |  | -304 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX08 | 183100 | 915 |  |  |  | 320 |
| 2 | Y1 | ZB2 | 2024 | 12 | MXX08 | 583000 | YB90 |  |  |  | -320 |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: sheet name says UPLOAD_ZB4 while title/version is ZB2

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2208-upload-zb2-2022-cgrxx-srd2-4]]
- related-to :: [[07-group-reporting-and-consolidation/2208-upload-zb2-2023-cgrxx-srd2-5]]
- related-to :: [[07-group-reporting-and-consolidation/2208-upload-zb2-2024-cgrxx-srd2-6]]
- related-to :: [[07-group-reporting-and-consolidation/2208-upload-zb2-2025-cgrxx-srd2-7]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/UPLOAD_ZB2_2024_CGRXX_SRD2.xlsx` — full document · extracted with `xlsx2md` · 9,607 chars in the whole document
