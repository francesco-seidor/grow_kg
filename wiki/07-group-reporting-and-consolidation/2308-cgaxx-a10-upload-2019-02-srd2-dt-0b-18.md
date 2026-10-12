---
id: 07-group-reporting-and-consolidation/2308-cgaxx-a10-upload-2019-02-srd2-dt-0b-18
title: 2308 CGAXX A10 UPLOAD 2019 02 SRD2 DT 0B (2308_CGAXX_A10_UPLOAD_2019_02_SRD2_DT_0B)
description: "Consolidation data upload sample (version A10, FY 2019 period 2, unit MXX03, doc type 0B) with investment activity type, subitem and group-currency amounts for items 314100/314150."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/investment-and-quantity-data-uploads]
aliases: [2308_CGAXX_A10_UPLOAD_2019_02_SRD2_DT_0B]
keywords: [Investment and Equity Data Uploads (Doc Type 0B), consolidation data upload, upload parameters, investment activity, financial statement items, subitems, consolidation units, group currency amounts, consolidation versions, 2308]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_CGAXX_A10_UPLOAD_2019_02_SRD2_DT_0B.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-18
topic: 07-group-reporting-and-consolidation/investment-and-quantity-data-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2308 CGAXX A10 UPLOAD 2019 02 SRD2 DT 0B (2308_CGAXX_A10_UPLOAD_2019_02_SRD2_DT_0B)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_CGAXX_A10_UPLOAD_2019_02_SRD2_DT_0B.xlsx`, extracted with `xlsx2md`. Grouped under **Investment and Equity Data Uploads (Doc Type 0B)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2308 CGAXX A10 UPLOAD 2019 02 SRD2 DT 0B

### Sheet: Data

| * Parameters |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P | PERIODICAL | X | Input Type |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| P | UPDATEMODE | 1 | Update Mode |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| P | DOCTY | 0B |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| * |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| D | ConsolidationChartOfAccounts | ConsolidationVersion | FiscalYear | FiscalPeriod | ConsolidationUnit | FinancialStatementItem | PartnerConsolidationUnit | BaseUnit | QuantityInBaseUnit | InvestmentActivityType | InvestmentActivity | InvesteeConsolidationUnit | AmountInLocalCurrency | AmountInGroupCurrency | SubItem | Segment | SubItemCategory | ProfitCenter | PartnerProfitCenter | PartnerSegment | ControllingArea |
| *D | RITCLG | RVERS | RYEAR | POPER | RBUNIT | RITEM | RBUPTR | RUNIT | MSL | COIAC | COINR | COICU | HSL | KSL | SUBIT | SEGMENT | SITYP | PRCTR | PPRCTR | PSEGMENT | KOKRS |
| 2 | Y1 | A10 | 2019 | 2 | MXX03 | 314100 |  |  |  | 02 |  |  | -20000 | -14184 | 950 |  | 1 |  |  |  |  |
| 2 | Y1 | A10 | 2019 | 2 | MXX03 | 314150 |  |  |  | 02 |  |  | 7000 | 4965 | 950 |  | 1 |  |  |  |  |
| 2 | Y1 | A10 | 2019 | 2 | MXX03 | 314100 |  |  |  | 02 |  |  | 20000 | 14184 | 955 |  | 1 |  |  |  |  |
| 2 | Y1 | A10 | 2019 | 2 | MXX03 | 314150 |  |  |  | 02 |  |  | -7000 | -4965 | 955 |  | 1 |  |  |  |  |
| 2 | Y1 | A10 | 2019 | 2 | MXX03 | 314100 |  |  |  |  |  |  | 20000 |  | 950 |  | 1 |  |  |  |  |
| 2 | Y1 | A10 | 2019 | 2 | MXX03 | 314150 |  |  |  |  |  |  | -7000 |  | 950 |  | 1 |  |  |  |  |
| 2 | Y1 | A10 | 2019 | 2 | MXX03 | 314100 |  |  |  |  |  |  | -20000 |  | 955 |  | 1 |  |  |  |  |
| 2 | Y1 | A10 | 2019 | 2 | MXX03 | 314150 |  |  |  |  |  |  | 7000 |  | 955 |  | 1 |  |  |  |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-upload-2018-12-srd2-dt-0b-14]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-upload-2019-01-srd2-dt-0b-16]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-j10-j20-j1r-j2r-upload-2018-12-srd2-dt-0b-21]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-j10-j20-upload-2019-01-srd2-dt-0b-25]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_CGAXX_A10_UPLOAD_2019_02_SRD2_DT_0B.xlsx` — full document · extracted with `xlsx2md` · 2,022 chars in the whole document
