---
id: 07-group-reporting-and-consolidation/2308-cgaxx-j10-j20-mje-2019-01-pl-30-import-group-journal-entries-24
title: 2308 CGAXX J10 J20 MJE 2019 01 PL 30 (Import Group Journal Entries) (2308_CGAXX_J10_J20_MJE_2019_01_PL_30)
description: "Spreadsheet template sample for importing group journal entries (Template 03 Group-Dependent Adjustments) with dividend, NCI and sale reclassification entries for CGAXX 2019."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/group-journal-entries]
aliases: [2308_CGAXX_J10_J20_MJE_2019_01_PL_30]
keywords: [Group Journal Entry Import Templates, group journal entries, consolidation, group-dependent adjustments, non-controlling interest, dividend elimination, import templates, 2308]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_CGAXX_J10_J20_MJE_2019_01_PL_30.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-24
topic: 07-group-reporting-and-consolidation/group-journal-entries
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2308 CGAXX J10 J20 MJE 2019 01 PL 30 (Import Group Journal Entries) (2308_CGAXX_J10_J20_MJE_2019_01_PL_30)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_CGAXX_J10_J20_MJE_2019_01_PL_30.xlsx`, extracted with `xlsx2md`. Grouped under **Group Journal Entry Import Templates** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2308 CGAXX J10 J20 MJE 2019 01 PL 30

### Sheet: CGAXX_J10_J20_MJE_2019_01_P

| Import Group Journal Entries |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Last Updated: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Template: 03 Group-Dependent Adjustments |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Header Data |  |  |  |  |  |  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | ConsolidationDocumentType | ConsolidationChartOfAccounts | ConsolidationVersion | FiscalYear | FiscalPeriod | ConsolidationGroup | DocumentItemText | ConsolidationPostingItem | FinancialStatementItem | SubItem | ConsolidationUnit | PartnerConsolidationUnit | AmountInLocalCurrency | AmountInGroupCurrency | AmountInTransactionCurrency | TransactionCurrency | QuantityInBaseUnit | BaseUnit | ControllingArea | ChartOfAccounts | CostCenter | GLAccount | ProfitCenter | PartnerProfitCenter | AssignmentReference | Segment | PartnerSegment | Customer | FunctionalArea | InvesteeConsolidationUnit | InvestmentActivityType | PostingDate | FinancialTransactionType |
| *Journal Entry ID (10) | *Document Type (2) | *Consolidation Chart of Accounts (2) | *Consolidation Version (3) | *Fiscal Year (4) | *Posting Period (3) | *Consolidation Group (18) | Remarks (50) | *Line Item (6) | *Financial Statement Item (10) | Subitem (10) | *Consolidation Unit (18) | Partner Unit (18) | Value in Local Currency | *Value in Group Currency | Value in Transaction Currency | Currency Key (5) | Quantity (29) | Base Unit of Measure (3) | Controlling Area (4) | Chart of Accounts (4) | Cost Center (10) | Account Number (10) | Profit Center (10) | Partner Profit Center (10) | Assignment number (18) | Segment for Segmental Reporting (10) | Partner Segment for Segmental Reporting (10) | Customer Number (10) | Functional Area (16) | Investee Unit (18) | Consolidation of Investments Activity (2) | Posting Date in the Document | Transaction type (3) |
| 1 | 33 | Y1 | J10 | 2019 | 1 | CGAXX | Dividende MXX05 | 1 | 171000 | 906 | MXX00 |  |  | -6500 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX05 | 02 |  |  |
| 1 | 33 | Y1 | J10 | 2019 | 1 | CGAXX | Dividende MXX05 | 2 | 603000 | YB99 | MXX00 | MXX05 |  | 6500 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX05 | 02 |  |  |
| 1 | 33 | Y1 | J20 | 2019 | 1 | CGAXX | Dividende MXX05 | 1 | 171000 | 906 | MXX00 | MXX05 |  | -9056 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX05 | 02 |  |  |
| 1 | 33 | Y1 | J20 | 2019 | 1 | CGAXX | Dividende MXX05 | 2 | 603000 | YB99 | MXX00 |  |  | 9056 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX05 | 02 |  |  |
| 3 | 33 | Y1 | J10 | 2019 | 1 | CGAXX | Reclassification G/L on sale of MXX07 | 1 | 512000 | YB77 | MXX00 | MXX07 |  | 20000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX07 | 02 |  |  |
| 3 | 33 | Y1 | J10 | 2019 | 1 | CGAXX | Reclassification G/L on sale of MXX07 | 2 | 318000 | 992 | MXX00 |  |  | -20000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX07 | 02 |  |  |
| 3 | 33 | Y1 | J20 | 2019 | 1 | CGAXX | Reclassification G/L on sale of MXX07 | 1 | 512000 | YB77 | MXX00 |  |  | 27866 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX07 | 02 |  |  |
| 3 | 33 | Y1 | J20 | 2019 | 1 | CGAXX | Reclassification G/L on sale of MXX07 | 2 | 318000 | 992 | MXX00 | MXX07 |  | -27866 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX07 | 02 |  |  |
| 4 | 33 | Y1 | J10 | 2019 | 1 | CGAXX | NCI dividende MXX03 / MXX02 | 1 | 321100 | 906 | MXX02 |  |  | -143544.20000000001 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX03 | 02 |  |  |
| 4 | 33 | Y1 | J10 | 2019 | 1 | CGAXX | NCI dividende MXX03 / MXX02 | 2 | 316000 | 906 | MXX02 |  |  | 143544.20000000001 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX03 | 02 |  |  |
| 4 | 33 | Y1 | J20 | 2019 | 1 | CGAXX | NCI dividende MXX03 / MXX02 | 1 | 321100 | 906 | MXX02 |  |  | -200000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX03 | 02 |  |  |
| 4 | 33 | Y1 | J20 | 2019 | 1 | CGAXX | NCI dividende MXX03 / MXX02 | 2 | 316000 | 906 | MXX02 |  |  | 200000 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX03 | 02 |  |  |
| 8 | 33 | Y1 | J10 | 2019 | 1 | CGAXX | NCI Net income MXX06 | 1 | 321100 | 998 | MXX06 |  |  | 9811.41 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX06 | 02 |  |  |
| 8 | 33 | Y1 | J10 | 2019 | 1 | CGAXX | NCI Net income MXX06 | 2 | 321150 | 998 | MXX06 |  |  | -9811.41 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX06 | 02 |  |  |
| 8 | 33 | Y1 | J20 | 2019 | 1 | CGAXX | NCI Net income MXX06 | 1 | 321100 | 998 | MXX06 |  |  | 13670.2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX06 | 02 |  |  |
| 8 | 33 | Y1 | J20 | 2019 | 1 | CGAXX | NCI Net income MXX06 | 2 | 321150 | 998 | MXX06 |  |  | -13670.2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | MXX06 | 02 |  |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-mje-2018-12-pl-10-10]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-mje-2019-01-pl-10-11]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-mje-2019-01-pl-30-12]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-j10-j20-mje-2018-12-pl-10-22]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2308_CGAXX_J10_J20_MJE_2019_01_PL_30.xlsx` — full document · extracted with `xlsx2md` · 5,185 chars in the whole document
