---
id: 07-group-reporting-and-consolidation/2502-mje-ct-template-93
title: 2502 MJE CT Template (2502_MJE_CT_Template)
description: "Import template (01 Manual Correction) for Group Journal Entries in consolidation: header and line-item field list with lengths and one sample row (FY 2021)."
cluster: 07-group-reporting-and-consolidation
tags: [kb/group-reporting-and-consolidation, topic/group-journal-entries]
aliases: [2502_MJE_CT_Template]
keywords: [Group Journal Entry Import Templates, group journal entries, manual correction template, consolidation data upload, journal entry fields, consolidation units, financial statement items, subitems, segment reporting, 2502]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2502_MJE_CT_Template.xlsx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-93
topic: 07-group-reporting-and-consolidation/group-journal-entries
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# 2502 MJE CT Template (2502_MJE_CT_Template)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2502_MJE_CT_Template.xlsx`, extracted with `xlsx2md`. Grouped under **Group Journal Entry Import Templates** in Group Reporting and Consolidation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

## 2502 MJE CT Template

### Sheet: Data

| Import Group Journal Entries |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Last Updated: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Template: 01 Manual Correction |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Header Data |  |  |  |  |  |  | Line Items |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | ConsolidationDocumentType | ConsolidationChartOfAccounts | ConsolidationVersion | FiscalYear | FiscalPeriod | ConsolidationUnit | DocumentItemText | ConsolidationPostingItem | FinancialStatementItem | SubItemCategory | SubItem | PartnerConsolidationUnit | AmountInLocalCurrency | AmountInGroupCurrency | QuantityInBaseUnit | BaseUnit | ControllingArea | ChartOfAccounts | CostCenter | GLAccount | ProfitCenter | AssignmentReference | Segment | Customer | FunctionalArea | FinancialTransactionType | PartnerProfitCenter | PartnerSegment |
| *Journal Entry ID (10) | *Document Type (2) | *Consolidation Chart of Accounts (2) | *Consolidation Version (3) | *Fiscal Year (4) | *Posting Period (3) | *Consolidation Unit (18) | Remarks (50) | *Line Item (6) | *Financial Statement Item (10) | Subitem Category (3) | Subitem (10) | Partner Unit (18) | *Value in Local Currency | *Value in Group Currency | Quantity (29) | Base Unit of Measure (3) | Controlling Area (4) | Chart of Accounts (4) | Cost Center (10) | Account Number (10) | Profit Center (10) | Assignment number (18) | Segment for Segmental Reporting (10) | Customer Number (10) | Functional Area (16) | Transaction type (3) | Partner Profit Center | Partner Segment for Segmental Reporting |
| 1 | 1X | Y1 | Y10 | 2021 | 11 | CXXXX |  | 000001 | S00003 |  |  |  |  |  | 1.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Connections
- part-of :: [[_cluster]]
- related-to :: [[07-group-reporting-and-consolidation/2502-xxxx-y10-mje-2021-11-pl-0c-97]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-mje-2018-12-pl-10-10]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-mje-2019-01-pl-10-11]]
- related-to :: [[07-group-reporting-and-consolidation/2308-cgaxx-a10-mje-2019-01-pl-30-12]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/2502_MJE_CT_Template.xlsx` — full document · extracted with `xlsx2md` · 2,042 chars in the whole document
