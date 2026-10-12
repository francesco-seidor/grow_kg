---
id: 07-group-reporting-and-consolidation/2308-cgrxx-j1s-mje-2022-01-pl-10-import-group-journal-entries-49
title: 2308 CGRXX J1S MJE 2022 01 PL 10 (Import Group Journal Entries) (2308_CGRXX_J1S_MJE_2022_01_PL_10)
description: "Excel template sample for importing group journal entries (template 01 Manual Correction), version J1S, 2022 period 1, goodwill postings for units MXX01 and MXX05."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/group-journal-entries]
aliases: [2308_CGRXX_J1S_MJE_2022_01_PL_10]
keywords: [Group Journal Entry Import Templates, group journal entries, consolidation import, manual correction template, goodwill postings, consolidation units, 2308]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_CGRXX_J1S_MJE_2022_01_PL_10.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-49
topic: 07-group-reporting-and-consolidation/group-journal-entries
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2308 CGRXX J1S MJE 2022 01 PL 10 (Import Group Journal Entries) (2308_CGRXX_J1S_MJE_2022_01_PL_10)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_CGRXX_J1S_MJE_2022_01_PL_10.xlsx`, extracted with `xlsx2md`. Grouped under **Group Journal Entry Import Templates** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2308 CGRXX J1S MJE 2022 01 PL 10

### Sheet: Data

| Import Group Journal Entries |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Last Updated: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Template: 01 Manual Correction |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Header Data |  |  |  |  |  |  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | ConsolidationDocumentType | ConsolidationChartOfAccounts | ConsolidationVersion | FiscalYear | FiscalPeriod | ConsolidationUnit | DocumentItemText | ConsolidationPostingItem | FinancialStatementItem | SubItemCategory | SubItem | PartnerConsolidationUnit | AmountInLocalCurrency | AmountInGroupCurrency | ControllingArea | ChartOfAccounts | CostCenter | GLAccount | ProfitCenter | AssignmentReference | Segment | Customer | FunctionalArea | FinancialTransactionType | PartnerProfitCenter | PartnerSegment |
| *Journal Entry ID (10) | *Document Type (2) | *Consolidation Chart of Accounts (2) | *Consolidation Version (3) | *Fiscal Year (4) | *Posting Period (3) | *Consolidation Unit (18) | Remarks (50) | *Line Item (6) | *Financial Statement Item (10) | Subitem Category (3) | Subitem (10) | Partner Unit (18) | *Value in Local Currency | *Value in Group Currency | Controlling Area (4) | Chart of Accounts (4) | Cost Center (10) | Account Number (10) | Profit Center (10) | Assignment number (18) | Segment for Segmental Reporting (10) | Customer Number (10) | Functional Area (16) | Transaction type (3) | Partner Profit Center | Partner Segment for Segmental Reporting |
| 5 | 10 | Y1 | J1S | 2022 | 1 | MXX01 | Goodwill | 000001 | 163100 |  | 901 | MXX00 | 1027083 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 10 | Y1 | J1S | 2022 | 1 | MXX01 | Goodwill | 000002 | 316000 |  | 901 | MXX00 | -1027083 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 10 | Y1 | J1S | 2022 | 1 | MXX05 | Goodwill | 000001 | 163100 |  | 992 | MXX00 | 40528 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 10 | Y1 | J1S | 2022 | 1 | MXX05 | Goodwill | 000002 | 316000 |  | 992 | MXX00 | -40528 |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-mje-2018-12-pl-10-10]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-mje-2019-01-pl-10-11]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-mje-2019-01-pl-30-12]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-j10-j20-mje-2018-12-pl-10-22]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_CGRXX_J1S_MJE_2022_01_PL_10.xlsx` — full document · extracted with `xlsx2md` · 2,362 chars in the whole document
