---
title: Financial Accounting and Close
description: "G/L accounts and journal entries, receivables, payables, direct debit, credit management, fixed assets, accruals, period-end close, intercompany postings, public sector."
cluster: 03-financial-accounting-and-close
type: cluster
tags: [kb/financial-accounting-and-close, kb/hub]
keywords: [G/L account, YCOA, journal entry, accounts receivable, accounts payable, SEPA, credit management, fixed assets, period-end close, public sector, intercompany posting]
node_count: 86
created: 2026-10-12
updated: 2026-10-12
---

# Financial Accounting and Close

Covers operational entity-level accounting (company code 3310 and similar). Excludes VAT and statutory reports (see 04), treasury instruments, bank statements and cash pooling (see 05), cost/profit center controlling and revenue recognition (see 06), consolidation (see 07), FI-CA (see 09) and Central Finance (see 16), and leasing, real estate contracts and lease accounting (see 17).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Account Reconciliation and Transaction Matching with BlackLine

How the BlackLine cloud connector imports G/L, AP, AR and currency data for account reconciliation and transaction matching.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-account-reconciliation-sap-solution-extensions-by-blacklin\|Test Script: Account Reconciliation – SAP Solution Extensions by BlackLine (6IL) (6IL_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 6IL: BlackLine Cloud connector imports (currency, G/L, AP, AR, multi-currency, account analysis) and certification. |
| [[03-financial-accounting-and-close/test-script-transaction-matching-sap-solution-extensions-by-blackline\|Test Script: Transaction Matching - SAP Solution Extensions by BlackLine (6IM) (6IM_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script (19-06-26) for BlackLine transaction matching: importing G/L and open item transactions via the BlackLine SAP Connector. |

### Accounting and Financial Close with a Parallel Group Ledger (US GAAP or IFRS)

How ledger-group journal entries, clearing, FX valuation, accruals and period-end close run with a parallel US GAAP (2VA) or IFRS (1GA) group ledger.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-accounting-and-financial-close-group-ledger-ifrs-1ga-ae-sa\|Test Script: Accounting and Financial Close - Group Ledger IFRS (1GA_AE) - SAP S/4HANA Cloud Public Edition (1GA_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for Group Ledger IFRS (1GA_AE, UAE): journal entries, clearing, FX valuation, reports; company code 3310. |
| [[03-financial-accounting-and-close/accounting-and-financial-close-group-ledger-us-gaap-2va-ae-test-script\|Accounting and Financial Close – Group Ledger US GAAP (2VA_AE) Test Script (2VA_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2VA_AE (UAE, company code 3310): ledger-group journal entries, clearing, FX valuation, trial balance. |

### Accounts Payable and Payment Runs

How supplier invoices, BRF+ payment settings, automatic payment runs and payables reporting are processed for company code 3310.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-accounts-payable-j60-ae-sap-s-4hana-cloud-public-edition-2\|Test Script: Accounts Payable (J60_AE) - SAP S/4HANA Cloud Public Edition 2608, United Arab Emirates (J60_S4CLD2608_BPD_EN_AE)]] | SAP test script J60_AE for Accounts Payable (UAE, company code 3310): prerequisites, BRF+ setup and step-by-step procedures for invoices, payment runs, approvals, reporting. |

### Accounts Receivable

How customer invoices, incoming payments, clearing, dunning and receivables reporting are processed for company code 3310.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounts-receivable-j59-a\|Test Script: SAP S/4HANA Cloud Public Edition - Accounts Receivable (J59_AE) (J59_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script for Accounts Receivable scope item J59 (United Arab Emirates), release 2608: prerequisites, preliminary config and step-by-step test procedures. |
| [[03-financial-accounting-and-close/customer-payments-1s0-ae-test-script-760\|Customer Payments (1S0_AE) Test Script (1S0_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud test script for Customer Payments (1S0, UAE, company code 3310): sample invoice and bank statement setup, and displaying open invoices. |

### SAP Advanced Financial Closing Integration

How to connect S/4HANA Cloud to SAP Advanced Financial Closing on BTP and manage closing task lists and closing tasks.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/advanced-financial-closing-integration-4hg-1029\|Advanced Financial Closing Integration (4HG) (4HG_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud test script for scope item 4HG: connecting to SAP Advanced Financial Closing on BTP, managing closing task lists and processing closing tasks. |

### Asset Accounting with IFRS and US GAAP Group Ledgers

How asset acquisitions, depreciation, revaluation, transfers and retirements post in parallel IFRS/US GAAP ledgers, and the Asset Accounting Overview page.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-asset-accounting-group-ledger-ifrs-1gb-ae-719\|Test Script: Asset Accounting – Group Ledger IFRS (1GB_AE) (1GB_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (1GB_AE) for Asset Accounting with Group Ledger IFRS: prerequisites, legacy asset setup, revaluation index, test procedures. |
| [[03-financial-accounting-and-close/sap-fiori-analytical-apps-for-asset-accounting-in-finance-2qy-853\|SAP Fiori Analytical Apps for Asset Accounting in Finance (2QY) (2QY_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud 2608 test script for scope item 2QY: testing the Asset Accounting Overview (F3096) page, filters, cards and drill-down navigation. |
| [[03-financial-accounting-and-close/test-script-asset-accounting-group-ledger-us-gaap-33f-ae-898\|Test Script: Asset Accounting – Group Ledger US GAAP (33F_AE) (33F_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 33F (Asset Accounting, Group Ledger US GAAP, AE): prerequisites, legacy asset setup and test procedures. |

### Assets Under Construction

How AuC is capitalized, distribution rules defined and settled to final assets in the IFRS group ledger.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/asset-under-construction-additional-depreciation-area-5kf-ae-test-scri\|Asset Under Construction – Additional Depreciation Area (5KF_AE) – Test Script (5KF_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition test script for scope item 5KF_AE: AuC additional depreciation area, prerequisites, legacy transfer, AuC acquisition, settlement. |
| [[03-financial-accounting-and-close/test-script-asset-under-construction-bfh-ae-sap-s-4hana-cloud-public-e\|Test Script: Asset Under Construction (BFH_AE) - SAP S/4HANA Cloud Public Edition (BFH_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for Assets under Construction (BFH_AE, no Controlling integration): prerequisites, legacy AuC, acquisition, settlement. |
| [[03-financial-accounting-and-close/test-script-asset-under-construction-group-ledger-ifrs-1gf-ae-720\|Test Script: Asset Under Construction – Group Ledger IFRS (1GF_AE) (1GF_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for Asset Under Construction, Group Ledger IFRS (1GF_AE): legacy AuC setup, distribution rules, settlement. |
| [[03-financial-accounting-and-close/test-script-asset-under-construction-group-ledger-us-gaap-33g-ae-899\|Test Script: Asset Under Construction - Group Ledger US GAAP (33G_AE) (33G_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud test script (33G_AE) for Assets under Construction, US GAAP: legacy AuC setup, distribution rules (AIAB) and settlement (AIBU). |

### Average Daily Balances for Banking

How to analyze average daily balances with the Trial Balance apps (W0166 deprecated, F9114) for banking.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/average-daily-balances-for-banking-649-test-script-1148\|Average Daily Balances for Banking (649) - Test Script (649_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 649: analysing average daily balances via Trial Balance apps W0166 (deprecated) and F9114. |

### Basic and Advanced Payment Management

How payment requests are approved with classifiers, rules and workflow (7MJ), and how Advanced Payment Management (4MT) runs payments, bank statement forwarding and watch lists.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-advanced-payment-management-4mt-sap-s-4hana-cloud-public-e\|Test Script: Advanced Payment Management (4MT) - SAP S/4HANA Cloud Public Edition (4MT_S4CLD2608_BPD_EN_XX)]] | S/4HANA Cloud 2608 test script for 4MT Advanced Payment Management: config prerequisites and tests for payments, bank statement forwarding, watch list screening |
| [[03-financial-accounting-and-close/test-script-basic-payment-management-7mj-1221\|Test Script: Basic Payment Management (7MJ) (7MJ_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 7MJ Basic Payment Management: functional approval classifier, payment rules, workflow, requested payments, approval. |

### Bills of Exchange and Postdated Checks

How bill of exchange receivables and postdated checks are posted, presented, discounted and cleared.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/bill-of-exchange-1wq-ae-test-script-sap-s-4hana-cloud-public-edition-7\|Bill of Exchange (1WQ_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1WQ_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 1WQ_AE (UAE): bill of exchange / postdated check receivable processing in SAP S/4HANA Cloud Public Edition 2608, with prerequisites and 10 procedures. |

### Cash Application with Machine Learning

How ML-based invoice matching clears incoming payments, lockbox and bank statement items are reprocessed, and BAI2 lockbox files are built.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/steps-to-create-bai2-format-file-207\|Steps to Create BAI2 Format File (Steps_To_Create_BAI2_File)]] | Guide to manually building a BAI2 bank statement text file for lockbox upload in SAP S/4HANA; the format must match SAP's BAI2 or the file cannot be processed. |
| [[03-financial-accounting-and-close/test-script-cash-application-integration-1mv-740\|Test Script: Cash Application Integration (1MV) (1MV_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1MV Cash Application Integration: ML invoice matching, lockbox reprocessing, payment advice extraction. |

### Cash Journal

How to post cash journal entries, print receipts and display the cash journal balance for petty cash.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-cash-journal-1go-ae-721\|Test Script: Cash Journal (1GO_AE) (1GO_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1GO_AE (Cash Journal): posting entries, printing receipts and displaying the cash journal, company code 3310. |

### Chart of Accounts YCOA and G/L Account Creation

Which G/L accounts the YCOA chart contains for company code 3310, account determination, and how to create a G/L account and cost element by copying.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-01\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 1 of 6]] | SAP Best Practices 2608 YCOA template chart of accounts: G/L master data, account purposes, account determination, local CoA alternatives and per-country usage. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-02\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 2 of 6]] | SAP S/4HANA Cloud Public Edition 2608 best-practice G/L account master list for chart of accounts YCOA; this slice covers accounts 22006013 to 71010100. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-03\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 3 of 6]] | SAP S/4HANA Cloud 2608 best-practice workbook: YCOA template chart of accounts, G/L master data, local-CoA alternatives and per-country usage flags. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-04\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 4 of 6]] | YCOA chart-of-accounts workbook, part 4: leasing additional-scope accounts, IFRS account hierarchy, T030H FX revaluation and T030K tax account determination. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-05\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 5 of 6]] | YCOA chart-of-accounts workbook (S/4HANA Cloud 2608); this part: tax-code, FX-difference, balance-sheet-transfer, MM and withholding-tax account determination. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-06\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 6 of 6]] | SAP Best Practices 2608 YCOA workbook: chart of accounts, T030 MM/withholding tax, asset (T095/T095B), special G/L (T074) account determination. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-ae-133\|BP CLD ENTPR 2608 Account Master Data for YCOA AE (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA_AE)]] | SAP S/4HANA Cloud Public Edition 2608 best-practice G/L account master data for chart YCOA, UAE company code 3310, plus SD account determination, CO defaults and UAE VAT tax codes. |
| [[03-financial-accounting-and-close/sachkonto-und-kostenart-anlegen-sds-bng-598\|Sachkonto und Kostenart anlegen – SDS (BNG) (BNG_S4CLD2608_Master_Data_DE_XX)]] | German master data script BNG for SAP S/4HANA Cloud Public Edition: creating a G/L account and cost element by copying an existing account via Configure Your Solution or SAP Central Business… |
| [[03-financial-accounting-and-close/master-data-script-create-g-l-account-and-cost-element-mds-bng-599\|Master Data Script: Create G/L Account and Cost Element - MDS (BNG) (BNG_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (BNG) for creating a G/L account and cost element by copying an account, with prerequisites and test steps. |
| [[03-financial-accounting-and-close/script-de-datos-maestros-crear-cuenta-de-mayor-y-clase-de-coste-mds-bn\|Script de datos maestros: Crear cuenta de mayor y clase de coste - MDS (BNG) (BNG_S4CLD2608_Master_Data_ES_XX)]] | Spanish master data script (BNG) for SAP S/4HANA Cloud Public Edition 2608: prerequisites and test steps to create a G/L account and cost element via Manage Your Solution (F1241). |
| [[03-financial-accounting-and-close/g-l-mds-bng-601\|マスタデータスクリプト: G/L 勘定および原価要素の登録 - MDS (BNG) (BNG_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data test script (BNG): create G/L accounts and cost elements by copying, via Solution Settings or Central Business Configuration. |
| [[03-financial-accounting-and-close/criar-conta-do-razao-e-classe-de-custo-mds-bng-602\|Criar conta do Razão e classe de custo - MDS (BNG) (BNG_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (BNG) for SAP S/4HANA Cloud Public Edition: creating G/L accounts by copying, via Manage Your Solution (F1241) or SAP Central Business Configuration. |
| [[03-financial-accounting-and-close/mds-bng-603\|创建总账科目和成本要素 - MDS (BNG) (BNG_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud Public Edition master data script (BNG) for creating G/L accounts and cost elements by copying via F1241. |

### Credit Management and Credit Agency Integration

How credit limits are set, blocked sales orders released or rejected, credit jobs scheduled, and external credit agency reports imported.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-basic-credit-management-bd6-ae-sap-s-4hana-cloud-public-ed\|Test Script: Basic Credit Management (BD6_AE) - SAP S/4HANA Cloud Public Edition (BD6_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item BD6_AE Basic Credit Management: credit limits, blocked order release/reject, reporting and credit background jobs (S/4HANA Cloud 2608). |
| [[03-financial-accounting-and-close/advanced-credit-management-1qm-ae-test-script-sap-s-4hana-cloud-public\|Advanced Credit Management (1QM_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1QM_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 1QM_AE Advanced Credit Management, S/4HANA Cloud Public Edition 2608: credit limits, ratings, requests, blocked orders, reports, jobs |
| [[03-financial-accounting-and-close/test-script-credit-agency-integration-1ry-759\|Test Script: Credit Agency Integration (1RY) (1RY_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1RY: importing external credit agency reports and viewing the updated credit profile. |

### Direct Debit and SEPA Mandates

How to create, display and manage SEPA direct debit mandates and collect receivables by direct debit payment run and payment medium.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/sepa-mandat-anlegen-sds-bnv-682\|SEPA-Mandat anlegen – SDS (BNV) (BNV_S4CLD2608_Master_Data_DE_XX)]] | German master data script (BNV) for creating, displaying, listing and managing SEPA mandates in SAP S/4HANA Cloud Public Edition 2608. |
| [[03-financial-accounting-and-close/create-sepa-mandate-mds-bnv-683\|Create SEPA Mandate - MDS (BNV) (BNV_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition master data script (BNV) with test steps to create, display, list and manage SEPA direct debit mandates for customers. |
| [[03-financial-accounting-and-close/crear-mandato-sepa-mds-bnv-684\|Crear mandato SEPA - MDS (BNV) (BNV_S4CLD2608_Master_Data_ES_XX)]] | Spanish master data script (BNV) for creating, displaying, listing and managing SEPA direct debit mandates in SAP S/4HANA Cloud Public Edition, dated 02-07-26. |
| [[03-financial-accounting-and-close/sepa-mds-bnv-685\|SEPA 委任の登録 - MDS (BNV) (BNV_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script for registering, displaying, listing and managing SEPA mandates in SAP S/4HANA Cloud Public Edition (scope item BNV). |
| [[03-financial-accounting-and-close/criar-mandato-sepa-mds-bnv-686\|Criar mandato SEPA – MDS (BNV) (BNV_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data test script (BNV) for SAP S/4HANA Cloud Public Edition 2608: creating, displaying, listing and administering SEPA mandates. |
| [[03-financial-accounting-and-close/sepa-mds-bnv-687\|创建 SEPA 授权 - MDS (BNV) (BNV_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud Public Edition 2608 master data script to create, display, list and manage SEPA mandates (FSEPA_M1/M3/M4, F5158). |
| [[03-financial-accounting-and-close/test-script-direct-debit-19m-ae-sap-s-4hana-cloud-public-edition-707\|Test Script: Direct Debit (19M_AE) - SAP S/4HANA Cloud Public Edition (19M_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 19M (AE): direct debit collection, SEPA mandates, payment run, payment medium, prerequisites and BRF+ setup. |

### Fixed Asset Master Records

How to create, change, block and delete fixed asset master records and sub-assets, with asset classes and number ranges.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/stammdatenskript-sap-s-4hana-cloud-public-edition-anlage-anlegen-sds-b\|Stammdatenskript SAP S/4HANA Cloud Public Edition - Anlage anlegen – SDS (BNI) (BNI_S4CLD2608_Master_Data_DE_XX)]] | German master data script for asset master records (Anlagenstamm) in SAP S/4HANA Cloud Public Edition 2608: prerequisites, asset classes, number ranges, test procedures. |
| [[03-financial-accounting-and-close/master-data-script-create-asset-bni-sap-s-4hana-cloud-public-edition-6\|Master Data Script - Create Asset (BNI), SAP S/4HANA Cloud Public Edition (BNI_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for fixed asset master data: create, change, display, block, delete, sub assets, change documents, depreciation keys. |
| [[03-financial-accounting-and-close/script-de-datos-maestros-crear-activo-fijo-mds-bni-612\|Script de datos maestros - Crear activo fijo - MDS (BNI) (BNI_S4CLD2608_Master_Data_ES_XX)]] | Spanish SAP S/4HANA Cloud Public Edition 2608 master data script: prerequisites and test procedures to create, change, display, block, delete fixed assets (F3425A). |
| [[03-financial-accounting-and-close/mds-bni-613\|マスタデータスクリプト 資産の登録 - MDS (BNI) (BNI_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud Public Edition 2608 master data script (BNI) for fixed asset master records: prerequisites, asset classes/number ranges, and test steps. |
| [[03-financial-accounting-and-close/script-de-dados-mestre-criar-imobilizado-mds-bni-614\|Script de dados mestre - Criar imobilizado – MDS (BNI) (BNI_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (PT): prerequisites, asset classes/number ranges and test procedures to create, change, block and delete fixed assets. |
| [[03-financial-accounting-and-close/sap-s-4hana-cloud-public-edition-mds-bni-615\|主数据脚本 SAP S/4HANA Cloud Public Edition - 创建资产 - MDS (BNI) (BNI_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script for fixed asset master records in S/4HANA Cloud Public Edition 2608: prerequisites, asset classes, and test steps via F3425A. |

### General Journal Entry Upload Template

How the general journal entry Excel upload template is laid out (header and line-item fields) with sample intercompany loan entries.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/2608-journal-entry-template-xxxx-pu1010-115\|2608 Journal Entry Template XXXX PU1010 (2608_Journal_Entry_Template_XXXX_PU1010)]] | 2608 'Upload General Journal Entry' spreadsheet template for company code XXXX: header and line-item field layout plus 10 sample G/L postings dated 2025-11-21. |
| [[03-financial-accounting-and-close/journal-entry-template-40y-193\|Journal Entry Template 40Y (JournalEntry_Template_40Y)]] | Upload General Journal Entry template (SAP S/4HANA Cloud) with 37 sample batches of paired AP/AR postings and trading-partner matching scenarios. |
| [[03-financial-accounting-and-close/journal-entry-template-78i-194\|Journal Entry Template 78I (JournalEntry_Template_78I)]] | Excel upload template for general journal entries (sheet Data) with header and line-item field layout and eight sample intercompany loan entries for company codes 1710 and 17US. |
| [[03-financial-accounting-and-close/2402-journal-entry-template-xxxx-pu1010-75\|2402 Journal Entry Template XXXX PU1010 (2402_Journal_Entry_Template_XXXX_PU1010)]] | 2402 'Upload General Journal Entry' spreadsheet template for company code XXXX: header and line-item field layout plus 10 sample G/L postings dated 2016-11-21. |
| [[03-financial-accounting-and-close/2502-journal-entry-template-xxxx-pu1010-91\|2502 Journal Entry Template XXXX PU1010 (2502_Journal_Entry_Template_XXXX_PU1010)]] | 2502 'Upload General Journal Entry' spreadsheet template for company code XXXX: header and line-item field layout plus 10 sample G/L postings dated 2021-11-21. |
| [[03-financial-accounting-and-close/2508-journal-entry-template-xxxx-pu1010-98\|2508 Journal Entry Template XXXX PU1010 (2508_Journal_Entry_Template_XXXX_PU1010)]] | Excel upload template for general journal entries in SAP S/4HANA Cloud (header and line-item field layout) with ten sample batches posting to company code XXXX. |

### GR/IR Account Monitoring and Reconciliation

How GR/IR clearing accounts are monitored, reconciled and analyzed, including ML prediction of reconciliation status (FI_GRIR_RECONCILE).

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-monitoring-of-goods-and-invoice-receipts-2v7-ae-876\|Test Script: Monitoring of Goods and Invoice Receipts (2V7_AE) (2V7_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 2V7: reconciling, monitoring and analyzing GR/IR accounts, with optional notification setup via situation handling. |
| [[03-financial-accounting-and-close/test-script-machine-learning-for-monitoring-of-goods-and-invoice-recei\|Test Script: Machine Learning for Monitoring of Goods and Invoice Receipts (2ZS_AE) (2ZS_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 2ZS: training, deploying and activating the GR/IR prediction ML model (FI_GRIR_RECONCILE) and scheduling the DAR status prediction job. |

### Billing of Costs Between Affiliated Companies

How costs incurred for an affiliate are billed via sales order, billing request, EDI and supplier invoice, including cross-company cost accounting postings.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/intercompany-billing-for-cross-company-cost-accounting-postings-4an-ae\|Intercompany Billing for Cross-Company Cost Accounting Postings (4AN_AE) - Test Script (4AN_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4AN: intercompany sales order, billing request and invoice between US (delivering) and DE (ordering). |
| [[03-financial-accounting-and-close/billing-of-costs-between-affiliated-companies-3zb-ae-test-script-989\|Billing of Costs Between Affiliated Companies (3ZB_AE) - Test Script (3ZB_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3ZB_AE (UAE): billing costs between affiliates via PO, sales order, billing, EDI and supplier invoice. |

### Cross-Company-Code Journal Postings

How cross-company-code journal entries are posted, displayed, changed and reversed, and intercompany clearing accounts verified.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-intercompany-financial-posting-1gp-ae-722\|Test Script: Intercompany Financial Posting (1GP_AE) (1GP_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1GP_AE: post, display, change and reverse cross-company-code journal entries, plus verification workflow appendix. |

### Provisioning of Overdue Receivables (IFRS 9)

How IFRS 9 valuation runs post provisions for overdue receivables and how doubtful debts are analyzed.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/provisioning-of-overdue-receivables-2pd-ae-test-script-847\|Provisioning of Overdue Receivables (2PD_AE) - Test Script (2PD_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (2PD, AE) for IFRS 9 provisioning of overdue receivables: valuation run, doubtful debts analysis, bad debt write-off. |

### Payment Advice Exchange with Buyers and Suppliers

How payment advice and cancellation messages are exchanged via SOAP between buyer and supplier systems after payment runs.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/integration-of-payment-advice-with-buyers-and-suppliers-2mb-ae-test-sc\|Integration of Payment Advice with Buyers and Suppliers (2MB_AE) - Test Script (2MB_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2MB_AE: payment runs, SOAP payment advice and cancellation exchange between buyer and supplier systems. |

### Payroll Posting Integration (Employee Central Payroll and HCM Payroll)

How cost centers replicate to payroll and payroll results post to FI from SuccessFactors Employee Central Payroll or SAP ERP HCM, by country.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-exception-based-core-hr-with-sap-successfactors-employee-c\|Test Script: Exception-Based Core HR with SAP SuccessFactors Employee Central (JB1_AE) (JB1_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud 2608 test script for JB1 (UAE): replicating banks, company codes, cost centers, workers and photos with SuccessFactors Employee Central. |
| [[03-financial-accounting-and-close/payroll-processing-with-sap-successfactors-employee-central-payroll-1n\|Payroll Processing with SAP SuccessFactors Employee Central Payroll (1NL) - Test Script (1NL_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1NL: cost center replication, payroll posting to FI, and country-specific procedures (US, ES, PT, BR, CO). |
| [[03-financial-accounting-and-close/test-script-payroll-processing-with-sap-erp-hcm-payroll-3up-sap-s-4han\|Test Script: Payroll Processing with SAP ERP HCM Payroll (3UP) - SAP S/4HANA Cloud Public Edition (3UP_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3UP: cost center replication, payroll posting to FI from HCM Payroll, plus US/CA, ES, PT, BR, CO procedures. |

### Fund Accounting and Public Sector Setup

How fund accounting FSVs, semantic tags, financial positions and budget controls are set up, and how a starter system is prepared for Public Sector Management.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-fund-accounting-7au-sap-s-4hana-cloud-public-edition-1206\|Test Script: Fund Accounting (7AU) - SAP S/4HANA Cloud Public Edition (7AU_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7AU Fund Accounting: FSV configuration, semantic tags, financial positions, 0DFLT constant, Funds Overview app. |
| [[03-financial-accounting-and-close/psm-preparation-guide-254\|PSM Preparation Guide (BP_CLD_ENTPR_PSM_Preparation_Guide)]] | Preparation steps in a starter system and test-script adjustments needed to test SAP S/4HANA Cloud with Public Sector Management (non-US countries). |

### Public Sector Grants Management

How grants are set up and created, budgets uploaded and PO/invoice postings tracked against grants.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-grants-management-71s-sap-s-4hana-cloud-public-edition-120\|Test Script: Grants Management (71S) - SAP S/4HANA Cloud Public Edition (71S_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 71S Grants Management: master data setup, grant creation, budget upload, PO/invoice postings, IDC, billing, monitoring. |

### Receivables and Payables Financing with Taulia

How Taulia receivables financing (Non-Dominion, Cash Dominion) and payables financing (dynamic discounting, supply chain finance, virtual card) are configured and posted.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-receivables-financing-with-taulia-7dx-ae-1214\|Test Script: Receivables Financing with Taulia (7DX_AE) (7DX_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (7DX_AE, 2608) for Taulia receivables financing: prerequisites, config steps, Non-Dominion and Cash Dominion test procedures. |
| [[03-financial-accounting-and-close/test-script-payables-financing-with-taulia-7mg-ae-1219\|Test Script: Payables Financing with Taulia (7MG_AE) (7MG_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition 2608 (AE) test script, scope item 7MG: Taulia Dynamic Discounting, Supply Chain Finance, Virtual Card; prerequisites and steps. |

### Service Entry Sheet Based Accruals

How purchase order accruals are proposed, simulated and posted from service entry sheets.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/service-entry-sheet-based-accruals-63l-ae-1143\|Service Entry Sheet Based Accruals (63L_AE) (63L_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 63L_AE: configuring, proposing, posting and simulating accruals from service entry sheets in SAP S/4HANA Cloud Public Edition 2608. |
| [[03-financial-accounting-and-close/test-script-purchase-order-accruals-2vb-ae-sap-s-4hana-cloud-public-ed\|Test Script: Purchase Order Accruals (2VB_AE) - SAP S/4HANA Cloud Public Edition (2VB_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 2VB: purchase order accruals and simulation, with prerequisites, roles, apps, steps. |

### General Ledger Accounting and Financial Close

How leading-ledger journal entries are posted and reviewed, G/L master data and financial statement versions maintained, and period-end close run for company code 3310.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounting-and-financial-part-01\|Test Script SAP S/4HANA Cloud Public Edition - Accounting and Financial Close (J58_AE) (J58_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for Accounting and Financial Close (J58_AE): prerequisites, config steps and G/L test procedures. |
| [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounting-and-financial-part-02\|Test Script SAP S/4HANA Cloud Public Edition - Accounting and Financial Close (J58_AE) (J58_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | SAP Fiori test script, company code 3310 (UAE): FX valuation, currency adjustments, impairment, reclassification, period close, tax, reporting, validation. |

### Asset Accounting: Acquisition to Year-End Close

How fixed assets in company code 3310 are transferred from legacy data, acquired, retired and valuated, and month- and year-end closing run, incl. an optional additional depreciation area.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-asset-accounting-additional-depreciation-area-5hg-ae-1095\|Test Script: Asset Accounting – Additional Depreciation Area (5HG_AE) (5HG_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (scope item 5HG_AE, UAE/AED) for the optional additional depreciation area in Asset Accounting: prerequisites and test procedures. |
| [[03-financial-accounting-and-close/test-script-asset-accounting-j62-ae-sap-s-4hana-cloud-public-edition-1\|Test Script: Asset Accounting (J62_AE) - SAP S/4HANA Cloud Public Edition (J62_S4CLD2608_BPD_EN_AE)]] | Test script for scope item J62 Asset Accounting (UAE, company code 3310): prerequisites, legacy transfer, acquisition, retirement, valuation, month-end and year-end closing steps. |

### Earmarked Funds

How funds reservations, precommitments and commitments are created, approved by workflow, consumed by supplier invoices and reported (78S Earmarked Funds).

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-earmarked-funds-78s-1205\|Test Script SAP S/4HANA Cloud Public Edition - Earmarked Funds (78S) (78S_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 78S Earmarked Funds in SAP S/4HANA Cloud Public Edition: reservation, precommitment, commitment, supplier invoice, workflow approval. |

### Government Budget Planning and Budget Management

How government expense, revenue and project budgets are planned in SAP Analytics Cloud, then uploaded, supplemented, transferred, released and approved with availability control.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-government-budget-planning-6uc-sap-s-4hana-cloud-public-ed\|Test Script: Government Budget Planning (6UC) - SAP S/4HANA Cloud Public Edition (6UC_S4CLD2608_BPD_EN_XX)]] | SAP test script for scope item 6UC Government Budget Planning in SAP Analytics Cloud: data load, expense/revenue/project planning, reports, analytics (2608). |
| [[03-financial-accounting-and-close/government-budget-management-6yu-test-script-sap-s-4hana-cloud-public\|Government Budget Management (6YU) - Test Script, SAP S/4HANA Cloud Public Edition (6YU_S4CLD2608_BPD_EN_XX)]] | Test script for SAP scope item 6YU Government Budget Management (S/4HANA Cloud Public Edition 2608): prerequisites and Fiori steps for budgeting, RIB, AVC. |

### Collections and Dispute Management

How collection strategies, groups and worklists prioritize receivables follow-up, and how dispute cases are created, processed and automated.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-collections-and-dispute-a\|Test Script SAP S/4HANA Cloud Public Edition - Collections and Dispute Automation (7MA_AE) (7MA_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7MA (AE): setup, dispute creation and processing, collections worklist, background jobs. |
| [[03-financial-accounting-and-close/collections-and-dispute-management-bfc-ae-test-script-1264\|Collections and Dispute Management (BFC_AE) Test Script (BFC_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for Collections and Dispute Management (BFC_AE): prerequisites, roles, Fiori apps and step-by-step test procedures. |

### Travel Expense Integration with SAP Concur

How cost objects and master data export to SAP Concur, and how cash advances, expense reports, payments and budgets integrate with S/4HANA Cloud accounting.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-travel-expense-processing-with-sap-concur-1m1-734\|Test Script: Travel Expense Processing with SAP Concur (1M1) (1M1_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 1M1: testing SAP S/4HANA Cloud and SAP Concur integration (cost object export, cash advances, expense reports, payment, budget). |

### Banking and Insurance Charts of Accounts

Which G/L accounts, with long texts, the banking (BCOA, scope item 5NU) and insurance (ICOA) industry charts of accounts contain.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/coa-overview-banking-180\|COA Overview Banking (COA_Overview_Banking)]] | SAP S/4HANA Cloud Public Edition 2608 banking chart of accounts (scope item 5NU, BCOA): G/L accounts with long text and DE (1010) / US (1710) availability flags. |
| [[03-financial-accounting-and-close/coa-overview-insurance-181\|COA Overview Insurance (COA_Overview_Insurance)]] | Insurance chart of accounts (sheet 78J - ICOA): 396 eight-digit G/L account numbers with long texts, from bonds and premiums receivable to benefits and expenses |

### Error Correction and Suspense Accounting for Banking

How ECS environments, error categories and teams route erroneous banking journal entries to suspense, then correct, approve by workflow and repost or reverse them.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/test-script-error-correction-and-suspense-accounting-for-banking-6sz-1\|Test Script: Error Correction and Suspense Accounting for Banking (6SZ) (6SZ_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 6SZ: ECS configuration, journal entry upload/SOAP posting, error processing, workflow approval, and reversals. |

## Related categories
- related-to :: [[04-tax-and-statutory-reporting/_cluster]]
- related-to :: [[05-treasury-and-cash-management/_cluster]]
- related-to :: [[06-management-accounting/_cluster]]
- related-to :: [[17-leasing-and-real-estate/_cluster]]
