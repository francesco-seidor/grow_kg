---
id: 07-group-reporting-and-consolidation/mcrxx-a10-upload-2025-12-srd2-dt-0b-198
title: MCRXX A10 UPLOAD 2025 12 SRD2 DT 0B (MCRXX_A10_UPLOAD_2025_12_SRD2_DT_0B)
description: "Sample consolidation upload sheet for version A10, fiscal year 2025 period 12: two quantity rows for item S00004 from unit MCXX00, plus upload parameters."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/matrix-consolidation-samples]
aliases: [MCRXX_A10_UPLOAD_2025_12_SRD2_DT_0B]
keywords: [Matrix Consolidation Sample Data (MCRXX), consolidation data upload, upload parameters, partner consolidation units, base unit quantities, update mode, periodic input type, document type, financial statement items, sub items]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/MCRXX_A10_UPLOAD_2025_12_SRD2_DT_0B.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-198
topic: 07-group-reporting-and-consolidation/matrix-consolidation-samples
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# MCRXX A10 UPLOAD 2025 12 SRD2 DT 0B (MCRXX_A10_UPLOAD_2025_12_SRD2_DT_0B)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/MCRXX_A10_UPLOAD_2025_12_SRD2_DT_0B.xlsx`, extracted with `xlsx2md`. Grouped under **Matrix Consolidation Sample Data (MCRXX)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## MCRXX A10 UPLOAD 2025 12 SRD2 DT 0B

### Sheet: MCRXX_A10_UPLOAD_2025_12_SRD2_D

| * Parameters |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P | PERIODICAL | X | Input Type | X:periodic | blank: YTD |  |  |  |  |  |  |  |  |
| P | UPDATEMODE | 1 | Update Mode: | 1: Delete all | 2: Overwrite | 5: Add |  |  |  |  |  |  |  |
| P | DOCTY | 0B | Document type | 00; 0B… | if empty the first doctype posting level 00 will be taken |  |  |  |  |  |  |  |  |
| * |  |  |  |  |  |  |  |  |  |  |  |  |  |
| D | ConsolidationChartOfAccounts | ConsolidationVersion | FiscalYear | FiscalPeriod | ConsolidationUnit | FinancialStatementItem | SubItemCategory | SubItem | PartnerConsolidationUnit | InvesteeConsolidationUnit | BaseUnit | QuantityInBaseUnit | AmountInLocalCurrency |
| *D | RITCLG | RVERS | RYEAR | POPER | RBUNIT | RITEM | SITYP | SUBIT | RBUPTR | COICU | RUNIT | MSL | HSL |
| 2 | Y1 | A10 | 2025 | 12 | MCXX00 | S00004 |  |  | MCXX01 |  | PRC | 20 |  |
| 2 | Y1 | A10 | 2025 | 12 | MCXX00 | S00004 |  |  | MCXX02 |  | PRC | 80 |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/mcrxx-a10-mje-2025-12-pl-10-195]]
- related-to :: [[07-group-reporting-and-consolidation/mcrxx-a10-mje-2026-02-pl-10-196]]
- related-to :: [[07-group-reporting-and-consolidation/mcrxx-a10-upload-2025-12-srd2-dt-00-197]]
- related-to :: [[07-group-reporting-and-consolidation/mcrxx-a10-upload-2026-01-srd2-dt-00-199]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/MCRXX_A10_UPLOAD_2025_12_SRD2_DT_0B.xlsx` — full document · extracted with `xlsx2md` · 1,123 chars in the whole document
