---
id: 07-group-reporting-and-consolidation/upload-2023-11-cg2-cuxxxx-pu1710-219
title: Upload 2023 11 CG2 CUXXXX PU1710 (Upload_2023_11_CG2_CUXXXX_PU1710)
description: "Sample consolidation data upload for FY2023 period 11 (version Y10, chart Y1, USD): upload parameters and 18 balanced rows for units XXXX and CXXXX."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/reported-financial-data-uploads]
aliases: [Upload_2023_11_CG2_CUXXXX_PU1710]
keywords: ["Reported Financial Data Flexible Uploads (A10, J-versions)", consolidation data upload, upload parameters, update mode, digit separator, consolidation document type, partner consolidation unit, financial statement items, assignment reference]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Upload_2023_11_CG2_CUXXXX_PU1710.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-219
topic: 07-group-reporting-and-consolidation/reported-financial-data-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Upload 2023 11 CG2 CUXXXX PU1710 (Upload_2023_11_CG2_CUXXXX_PU1710)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Upload_2023_11_CG2_CUXXXX_PU1710.xlsx`, extracted with `xlsx2md`. Grouped under **Reported Financial Data Flexible Uploads (A10, J-versions)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## Upload 2023 11 CG2 CUXXXX PU1710

### Sheet: 2402_Upload_2016_11_CG2_CUXXXX_

| * Parameters |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P | PERIODICAL | X | Input Type | X:periodic | blank: YTD |  |  |  |  |  |  |  |  |  |
| P | UPDATEMODE | 1 | Update Mode: | 1: Delete all | 2: Overwrite | 5: Add |  |  |  |  |  |  |  |  |
| P | NSEP | 2 | Digit Seperator: | 1: 1,000.00 | 2: 1.000,00 |  |  |  |  |  |  |  |  |  |
| P | DOCTY | 00 | Document type | 00; 0B… | if empty the first doctype posting level 00 will be taken |  |  |  |  |  |  |  |  |  |
| * |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| D | ConsolidationChartOfAccounts | ConsolidationVersion | FiscalYear | FiscalPeriod | ConsolidationUnit | FinancialStatementItem | PartnerConsolidationUnit | SubItem | Segment | AmountInLocalCurrency | AmountInGroupCurrency | AmountInTransactionCurrency | TransactionCurrency | AssignmentReference |
| *D | RITCLG | RVERS | RYEAR | POPER | RBUNIT | RITEM | RBUPTR | SUBIT | SEGMENT | HSL | KSL | TSL | RTCUR | AssignmentReference |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 111100 |  | 915 |  | 1000 | 1000 | 1000 | USD | 202010 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 211100 | 1710 | 915 |  | -1000 | -1000 | -1000 | USD | 202010 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 111100 |  | 915 |  | 850 | 850 | 850 | USD | 202020 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 211100 | 1710 | 915 |  | -850 | -850 | -850 | USD | 202020 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 111100 |  | 915 |  | 700 | 700 | 700 | USD | 202030 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 211100 | 1710 | 915 |  | -700 | -700 | -700 | USD | 202030 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 111100 |  | 915 |  | 500 | 500 | 500 | USD | 202040 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 211100 | 1710 | 915 |  | -500 | -500 | -500 | USD | 202040 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 111100 |  | 915 |  | 1000 | 1000 | 1000 | USD | 202050 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 211100 | 1710 | 915 |  | -1000 | -1000 | -1000 | USD | 202050 |
| 2 | Y1 | Y10 | 2023 | 11 | CXXXX | 111100 |  | 901 |  | -2004800 | -2004800 | -2004800 | USD |  |
| 2 | Y1 | Y10 | 2023 | 11 | CXXXX | 111200 |  | 901 |  | 110000 | 110000 | 110000 | USD |  |
| 2 | Y1 | Y10 | 2023 | 11 | CXXXX | 121100 |  | 901 |  | 16594 | 16594 | 16594 | USD |  |
| 2 | Y1 | Y10 | 2023 | 11 | CXXXX | 121100 |  | 901 |  | 1878206 | 1878206 | 1878206 | USD |  |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 111100 |  | 915 |  | 800 | 800 | 800 | USD | 202060 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 601000 | 1710 | YD70 |  | -800 | -800 | -800 | USD | 202060 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 111100 |  | 915 |  | 1000 | 1000 | 1000 | USD | 202070 |
| 2 | Y1 | Y10 | 2023 | 11 | XXXX | 515000 | 1710 | YD20 |  | -1000 | -1000 | -1000 | USD | 202070 |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-upload-2018-12-srd2-dt-00-13]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-upload-2019-01-srd2-dt-00-15]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-upload-2019-02-srd2-dt-00-17]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-upload-2019-03-srd2-dt-00-19]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Upload_2023_11_CG2_CUXXXX_PU1710.xlsx` — full document · extracted with `xlsx2md` · 2,837 chars in the whole document
