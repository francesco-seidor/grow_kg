---
id: 07-group-reporting-and-consolidation/cgrxx-j1s-upload-2024-01-srd2-dt-0b-175
title: CGRXX J1S UPLOAD 2024 01 SRD2 DT 0B (CGRXX_J1S_UPLOAD_2024_01_SRD2_DT_0B)
description: "Consolidation data upload sample for version J1S, FY 2024 period 1, doc type 0B, update mode 2 (Overwrite): investment-holding quantities (item 172100) from unit MXX00."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/investment-and-quantity-data-uploads]
aliases: [CGRXX_J1S_UPLOAD_2024_01_SRD2_DT_0B]
keywords: [Investment and Equity Data Uploads (Doc Type 0B), consolidation data upload, upload parameters, update mode, investee consolidation units, financial statement items, consolidation units, subitems, consolidation versions, CGRXX]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/CGRXX_J1S_UPLOAD_2024_01_SRD2_DT_0B.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-175
topic: 07-group-reporting-and-consolidation/investment-and-quantity-data-uploads
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# CGRXX J1S UPLOAD 2024 01 SRD2 DT 0B (CGRXX_J1S_UPLOAD_2024_01_SRD2_DT_0B)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/CGRXX_J1S_UPLOAD_2024_01_SRD2_DT_0B.xlsx`, extracted with `xlsx2md`. Grouped under **Investment and Equity Data Uploads (Doc Type 0B)** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## CGRXX J1S UPLOAD 2024 01 SRD2 DT 0B

### Sheet: CGRXX_J1S_UPLOAD_2022_01_SRD2_D

| * Parameters |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P | PERIODICAL | X | Input Type | X:periodic | blank: YTD |  |  |  |  |  |  |  |
| P | UPDATEMODE | 2 | Update Mode: | 1: Delete all | 2: Overwrite | 5: Add |  |  |  |  |  |  |
| P | DOCTY | 0B | Document type | 00; 0B… | if empty the first doctype posting level 00 will be taken |  |  |  |  |  |  |  |
| * |  |  |  |  |  |  |  |  |  |  |  |  |
| D | ConsolidationChartOfAccounts | ConsolidationVersion | FiscalYear | FiscalPeriod | ConsolidationUnit | FinancialStatementItem | PartnerConsolidationUnit | BaseUnit | QuantityInBaseUnit | InvesteeConsolidationUnit | SubItem | SubItemCategory |
| *D | RITCLG | RVERS | RYEAR | POPER | RBUNIT | RITEM | RBUPTR | RUNIT | MSL | COICU | SUBIT | SITYP |
| 2 | Y1 | J1S | 2024 | 1 | MXX00 | 172100 | MXX08 | PRC | 30 | MXX08 | 920 | 1 |
| 2 | Y1 | J1S | 2024 | 1 | MXX00 | 172100 | MXX04 | PRC | 60 | MXX04 | 901 | 1 |
| 2 | Y1 | J1S | 2024 | 1 | MXX00 | 172100 | MXX01 | PRC | 60 | MXX01 | 901 | 1 |
| 2 | Y1 | J1S | 2024 | 1 | MXX00 | 172100 | MXX05 | PRC | 22 | MXX05 | 920 | 1 |
| 2 | Y1 | J1S | 2024 | 1 | MXX00 | 172100 | MXX07 | PRC | -10 | MXX07 | 930 | 1 |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/cgrxx-a10-upload-2023-12-srd2-dt-0b-143]]
- related-to :: [[07-group-reporting-and-consolidation/cgrxx-a10-upload-2024-01-srd2-dt-0b-145]]
- related-to :: [[07-group-reporting-and-consolidation/cgrxx-a10-upload-2025-12-srd2-dt-0b-149]]
- related-to :: [[07-group-reporting-and-consolidation/cgrxx-a10-upload-2026-01-srd2-dt-0b-151]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/CGRXX_J1S_UPLOAD_2024_01_SRD2_DT_0B.xlsx` — full document · extracted with `xlsx2md` · 1,325 chars in the whole document
