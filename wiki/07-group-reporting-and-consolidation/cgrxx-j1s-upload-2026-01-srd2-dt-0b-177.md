---
id: 07-group-reporting-and-consolidation/cgrxx-j1s-upload-2026-01-srd2-dt-0b-177
title: CGRXX J1S UPLOAD 2026 01 SRD2 DT 0B (CGRXX_J1S_UPLOAD_2026_01_SRD2_DT_0B)
description: "Sample consolidation data upload (version J1S, FY2026 period 1, item S00004): parameters block plus 5 rows of PRC quantities per partner unit."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/investment-and-quantity-data-uploads]
aliases: [CGRXX_J1S_UPLOAD_2026_01_SRD2_DT_0B]
keywords: [Investment and Equity Data Uploads (Doc Type 0B), consolidation data upload, upload parameters, partner consolidation units, investee consolidation units, update mode, document type, financial statement items, consolidation versions, quantity in base unit]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/CGRXX_J1S_UPLOAD_2026_01_SRD2_DT_0B.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-177
topic: 07-group-reporting-and-consolidation/investment-and-quantity-data-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# CGRXX J1S UPLOAD 2026 01 SRD2 DT 0B (CGRXX_J1S_UPLOAD_2026_01_SRD2_DT_0B)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/CGRXX_J1S_UPLOAD_2026_01_SRD2_DT_0B.xlsx`, extracted with `xlsx2md`. Grouped under **Investment and Equity Data Uploads (Doc Type 0B)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## CGRXX J1S UPLOAD 2026 01 SRD2 DT 0B

### Sheet: CGRXX_J1S_UPLOAD_2026_01_SRD2_D

| * Parameters |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P | PERIODICAL | X | Input Type | X:periodic | blank: YTD |  |  |  |  |  |
| P | UPDATEMODE | 2 | Update Mode: | 1: Delete all | 2: Overwrite | 5: Add |  |  |  |  |
| P | DOCTY | 0B | Document type | 00; 0B… | if empty the first doctype posting level 00 will be taken |  |  |  |  |  |
| * |  |  |  |  |  |  |  |  |  |  |
| D | ConsolidationChartOfAccounts | ConsolidationVersion | FiscalYear | FiscalPeriod | ConsolidationUnit | FinancialStatementItem | PartnerConsolidationUnit | BaseUnit | QuantityInBaseUnit | InvesteeConsolidationUnit |
| *D | RITCLG | RVERS | RYEAR | POPER | RBUNIT | RITEM | RBUPTR | RUNIT | MSL | COICU |
| 2 | Y1 | J1S | 2026 | 1 | MXX00 | S00004 | MXX08 | PRC | 30 | MXX08 |
| 2 | Y1 | J1S | 2026 | 1 | MXX00 | S00004 | MXX04 | PRC | 60 | MXX04 |
| 2 | Y1 | J1S | 2026 | 1 | MXX00 | S00004 | MXX01 | PRC | 60 | MXX01 |
| 2 | Y1 | J1S | 2026 | 1 | MXX00 | S00004 | MXX05 | PRC | 22 | MXX05 |
| 2 | Y1 | J1S | 2026 | 1 | MXX00 | S00004 | MXX07 | PRC | -10 | MXX07 |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/cgrxx-a10-upload-2023-12-srd2-dt-0b-143]]
- related-to :: [[07-group-reporting-and-consolidation/cgrxx-a10-upload-2024-01-srd2-dt-0b-145]]
- related-to :: [[07-group-reporting-and-consolidation/cgrxx-a10-upload-2025-12-srd2-dt-0b-149]]
- related-to :: [[07-group-reporting-and-consolidation/cgrxx-a10-upload-2026-01-srd2-dt-0b-151]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/CGRXX_J1S_UPLOAD_2026_01_SRD2_DT_0B.xlsx` — full document · extracted with `xlsx2md` · 1,189 chars in the whole document
