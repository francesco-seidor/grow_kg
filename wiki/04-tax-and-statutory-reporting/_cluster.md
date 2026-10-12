---
title: Tax and Statutory Reporting
description: "Country VAT calculation and returns, Intrastat, EC sales lists and compliance formats, UAE tax codes, purchasing tax conditions, PEPPOL e-invoicing, Brazil Nota Fiscal and excise tax."
cluster: 04-tax-and-statutory-reporting
type: cluster
tags: [kb/tax-and-statutory-reporting, kb/hub]
keywords: [VAT, tax code, VAT return, Intrastat, EC Sales List, advanced compliance reporting, PEPPOL, eDocument, Nota Fiscal, excise tax]
node_count: 31
created: 2026-10-12
updated: 2026-10-12
---

# Tax and Statutory Reporting

Covers indirect tax setup and legal reporting by country. Excludes general G/L posting (see 03), the sales and billing processes that carry the tax (see 08), and customs declarations and embargo screening (see 13).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Belgium VAT, Intrastat and Compliance Formats

How Belgian VAT is calculated and reported, Intrastat declared, and VAT return, VAT unit declaration and EC Sales List prepared.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/test-script-vat-tax-calculation-and-reporting-for-belgium-5is-1105\|Test Script: VAT Tax Calculation and Reporting for Belgium (5IS) (5IS_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5IS: Belgium VAT calculation and reporting, with prerequisites, tax code setup and test steps. |
| [[04-tax-and-statutory-reporting/compliance-formats-support-preparation-for-belgium-5p9-test-script-111\|Compliance Formats – Support Preparation for Belgium (5P9) Test Script (5P9_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5P9: Belgium statutory reports (VAT return, VAT unit declaration, EC Sales List) for foreign company codes via RITA. |
| [[04-tax-and-statutory-reporting/intrastat-processing-for-belgium-5pa-test-script-1120\|Intrastat Processing for Belgium (5PA) - Test Script (5PA_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5PA: Belgian Intrastat declarations, with prerequisites, configuration, roles, apps and test steps. |

### Brazil Nota Fiscal Master Data and Tax Configuration

How Brazil business places, partners, materials, tax laws, CNAE, CFOP and other Nota Fiscal tax settings are configured for testing.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/master-data-script-sap-s-4hana-cloud-public-edition-nota-fiscal-brazil\|Master Data Script - SAP S/4HANA Cloud Public Edition - Nota Fiscal Brazil (JD0_BR) (JD0_S4CLD2608_Master_Data_EN_BR)]] | SAP Best Practices 2608 test script for Brazil master data and tax configuration (business place, BP, material, tax laws, CNAE, CFOP, SUFRAMA, CPRB, ICMS-ST, jurisdictions). |

### Czech Republic VAT, Intrastat and Compliance Formats

How Czech VAT is calculated and reported, Intrastat declared, and Czech statutory reports (VAT return, EC Sales List, financial statements) prepared.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/vat-tax-calculation-and-reporting-for-czech-republic-5z2-test-script-1\|VAT Tax Calculation and Reporting for Czech Republic (5Z2) - Test Script (5Z2_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5Z2: Czech VAT calculation and reporting, prerequisites, tax code setup, journal entries, advance return, e-tax return. |
| [[04-tax-and-statutory-reporting/test-script-intrastat-processing-for-czech-republic-5z4-1135\|Test Script: Intrastat Processing for Czech Republic (5Z4) (5Z4_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5Z4: Intrastat declarations for Czech Republic, with prerequisites, configuration and test procedures. |
| [[04-tax-and-statutory-reporting/compliance-formats-support-preparation-for-czech-republic-5z7-test-scr\|Compliance Formats – Support Preparation for Czech Republic (5Z7) Test Script (5Z7_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5Z7: Czech Republic statutory reports (VAT return, EC Sales List, financial statement, cash flow) via F1515_CZ. |

### SAP Excise Tax Management by Vistex

How SAP Excise Tax Management by Vistex is enabled and how order-to-excise postings are tested.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/test-script-enablement-of-sap-excise-tax-management-4lo-1033\|Test Script: Enablement of SAP Excise Tax Management (4LO) (4LO_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 4LO: testing S/4HANA Cloud APIs integrating with SAP Excise Tax Management (BTP): org data, master data, material documents. |
| [[04-tax-and-statutory-reporting/test-script-enablement-of-sap-excise-tax-management-by-vistex-7z8-ae-s\|Test Script: Enablement of SAP Excise Tax Management by Vistex (7Z8_AE), SAP S/4HANA Cloud Public Edition (7Z8_S4CLD2608_BPD_EN_AE)]] | SAP test script (scope item 7Z8, AE, dated 19-06-26) for SAP Excise Tax Management by Vistex: prerequisites, preliminary setup and order-to-excise-posting test steps. |

### Germany VAT Returns and Intrastat

How German VAT is calculated and the advance return and electronic tax return filed, and how German Intrastat declarations are generated.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/vat-tax-calculation-and-reporting-for-germany-55u-test-script-1071\|VAT Tax Calculation and Reporting for Germany (55U) - Test Script (55U_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 55U: German VAT calculation and reporting (journal entries, advance return, electronic tax return). |
| [[04-tax-and-statutory-reporting/test-script-compliance-formats-support-preparation-for-germany-5o6-sap\|Test Script: Compliance Formats – Support Preparation for Germany (5O6), SAP S/4HANA Cloud Public Edition (5O6_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud test script for scope item 5O6: German statutory reporting (Audit Z3, EC Sales List, Advance VAT Return, extensions, euBP) via Advanced Compliance Reporting. |
| [[04-tax-and-statutory-reporting/test-script-intrastat-processing-for-germany-5ol-sap-s-4hana-cloud-pub\|Test Script: Intrastat Processing for Germany (5OL) - SAP S/4HANA Cloud Public Edition (5OL_S4CLD2608_BPD_EN_XX)]] | SAP test script for scope item 5OL: Intrastat declarations for Germany (RITA) in S/4HANA Cloud Public Edition 2608 - prerequisites, configuration, commodity codes, POI, declarations. |

### PEPPOL Electronic Invoicing

How PEPPOL e-invoicing is set up and how billing documents are submitted and monitored in the eDocument Cockpit.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/test-script-invoice-correction-process-with-debit-memo-bdq-ae-1257\|Test Script: Invoice Correction Process with Debit Memo (BDQ_AE) (BDQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item BDQ (UAE): debit memo request, billing, eDocument PEPPOL submission, plus prerequisites and job scheduling. |
| [[04-tax-and-statutory-reporting/test-script-debit-memo-processing-1f1-ae-sap-s-4hana-cloud-public-edit\|Test Script: Debit Memo Processing (1F1_AE) - SAP S/4HANA Cloud Public Edition (1F1_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 1F1 (UAE): debit memo request, billing block removal, debit memo creation, PEPPOL eDocument cockpit, plus PEPPOL setup and billing job scheduling. |
| [[04-tax-and-statutory-reporting/sale-of-services-2eq-ae-test-script-sap-s-4hana-cloud-public-edition-8\|Sale of Services (2EQ_AE) Test Script - SAP S/4HANA Cloud Public Edition (2EQ_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 2EQ_AE Sale of Services (UAE): prerequisites, PEPPOL e-invoicing setup, sales order to billing, eDocument Cockpit, billing jobs. |

### Tax Condition Records and Purchasing Price Conditions

How to create tax determination condition records (MEK2) and create or change purchasing price conditions (MEK1/MEK2).

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/stammdatenskript-steuerkondition-anlegen-mds-2sw-274\|Stammdatenskript - Steuerkondition anlegen – MDS (2SW) (2SW_S4CLD2608_Master_Data_DE_XX)]] | German master data script (2SW) for SAP S/4HANA Cloud Public Edition: creating tax condition records (MEK2) and creating/changing purchasing price conditions (MEK1/MEK2). |
| [[04-tax-and-statutory-reporting/master-data-script-create-tax-condition-2sw-275\|Master Data Script: Create Tax Condition (2SW) (2SW_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud 2608 master data script 2SW: creating purchasing tax condition records (MEK2) and creating/changing price conditions (MEK1/MEK2). |
| [[04-tax-and-statutory-reporting/crear-condicion-para-determinacion-de-impuestos-mds-2sw-276\|Crear condición para determinación de impuestos - MDS (2SW) (2SW_S4CLD2608_Master_Data_ES_XX)]] | Spanish master data test script (2SW) for SAP S/4HANA Cloud Public Edition 2608: tax determination condition records and purchasing price conditions via Fiori apps. |
| [[04-tax-and-statutory-reporting/mds-2sw-277\|税条件の登録 - MDS (2SW) (2SW_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud Public Edition 2608 master data script for maintaining tax condition records (MEK2) and purchasing price conditions PPR0 (MEK1/MEK2). |
| [[04-tax-and-statutory-reporting/objetivo-script-de-dados-mestre-criar-condicao-de-imposto-mds-2sw-port\|Objetivo (Script de dados mestre: Criar condição de imposto - MDS 2SW, Portuguese) (2SW_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (2SW) for SAP S/4HANA Cloud 2608: creating tax condition records and creating/modifying purchasing price conditions (MEK1/MEK2). |
| [[04-tax-and-statutory-reporting/mds-2sw-279\|创建税收条件 - MDS (2SW) (2SW_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud 2608 master data script 2SW: create tax condition records (MEK2) and create/change purchasing price conditions (MEK1, MEK2). |

### South Africa VAT Calculation and Reporting

How South African VAT tax codes are set up, journal entries posted and the VAT return generated.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/test-script-vat-tax-calculation-and-reporting-for-south-africa-5z0-113\|Test Script: VAT Tax Calculation and Reporting for South Africa (5Z0) (5Z0_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 5Z0: South Africa VAT calculation and reporting, covering prerequisites, journal entries, advance return and electronic tax return. |
| [[04-tax-and-statutory-reporting/compliance-formats-support-preparation-for-south-africa-5z5-test-scrip\|Compliance Formats – Support Preparation for South Africa (5Z5) – Test Script (5Z5_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5Z5: South Africa VAT201, BBBEE AP analytics and cash flow statutory reports, with setup steps. |

### Sweden VAT, Intrastat and Compliance Formats

How Swedish VAT tax codes post and returns are filed, Intrastat declared, and EC Sales List and VAT return run in advanced compliance reporting.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/test-script-vat-tax-calculation-and-reporting-for-sweden-5z1-1132\|Test Script: VAT Tax Calculation and Reporting for Sweden (5Z1) (5Z1_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5Z1: Swedish VAT tax code setup, journal entry posting and advance return on sales/purchase tax. |
| [[04-tax-and-statutory-reporting/test-script-intrastat-processing-for-sweden-5z3-1134\|Test Script: Intrastat Processing for Sweden (5Z3) (5Z3_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5Z3: Intrastat declarations for Sweden, covering prerequisites, configuration, and step-by-step test procedures. |
| [[04-tax-and-statutory-reporting/test-script-compliance-formats-support-preparation-for-sweden-5z6-1137\|Test Script: Compliance Formats – Support Preparation for Sweden (5Z6) (5Z6_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script (5Z6) for Sweden advanced compliance reporting: setup, RITA, running the EC Sales List and VAT Return via Run Statutory Reports (F1515). |

### Preconfigured UAE VAT Tax Codes

Which UAE VAT tax codes are predelivered in 2608, their rates, tax box and tax group mappings, and tax account determination in the YCOA account master.

| Node | Description |
| --- | --- |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-01\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 1 of 6]] | SAP Best Practices 2608 YCOA template chart of accounts: G/L master data, account purposes, account determination, local CoA alternatives and per-country usage. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-02\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 2 of 6]] | SAP S/4HANA Cloud Public Edition 2608 best-practice G/L account master list for chart of accounts YCOA; this slice covers accounts 22006013 to 71010100. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-03\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 3 of 6]] | SAP S/4HANA Cloud 2608 best-practice workbook: YCOA template chart of accounts, G/L master data, local-CoA alternatives and per-country usage flags. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-04\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 4 of 6]] | YCOA chart-of-accounts workbook, part 4: leasing additional-scope accounts, IFRS account hierarchy, T030H FX revaluation and T030K tax account determination. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-05\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 5 of 6]] | YCOA chart-of-accounts workbook (S/4HANA Cloud 2608); this part: tax-code, FX-difference, balance-sheet-transfer, MM and withholding-tax account determination. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-06\|BP CLD ENTPR 2608 Account Master Data for YCOA (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA) — part 6 of 6]] | SAP Best Practices 2608 YCOA workbook: chart of accounts, T030 MM/withholding tax, asset (T095/T095B), special G/L (T074) account determination. |
| [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-ae-133\|BP CLD ENTPR 2608 Account Master Data for YCOA AE (BP_CLD_ENTPR_2608_Account_Master_Data_for_YCOA_AE)]] | SAP S/4HANA Cloud Public Edition 2608 best-practice G/L account master data for chart YCOA, UAE company code 3310, plus SD account determination, CO defaults and UAE VAT tax codes. |
| [[04-tax-and-statutory-reporting/2608-pre-configured-tax-codes-en-ae-702\|2608 Pre configured Tax Codes EN AE (2608_Pre-configured_Tax_Codes_EN_AE)]] | Pre-delivered United Arab Emirates (AE) VAT tax codes in S/4HANA Cloud content 2608: rates, EU codes, and tax box/tax group mappings, plus glossary of tax terms. |

### External Tax Audit and Auditor Access

How external tax auditors get time-restricted direct, indirect or file-based access with audit filters and data extracts to G/L and FI-CA data, plus tax reconciliation reports.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/test-script-external-tax-audit-2oo-ae-sap-s-4hana-cloud-public-edition\|Test Script: External Tax Audit (2OO_AE) - SAP S/4HANA Cloud Public Edition (2OO_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 2OO_AE External Tax Audit: auditor roles, time restrictions, audit filters, Auditor Direct Access, tax reconciliation reports. |
| [[04-tax-and-statutory-reporting/test-script-contract-accounting-external-tax-audit-and-compliance-repo\|Test Script: Contract Accounting – External Tax Audit and Compliance Reporting (2SJ_AE) (2SJ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 2SJ_AE: FI-CA external auditor access (direct, indirect, file), data extracts, and tax report steps. |

### UAE VAT Return and Statutory Reports

How the UAE VAT return, FAF audit file and cash flow statement are set up and generated as compliance formats for company code 3310.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/test-script-compliance-formats-support-preparation-1j2-ae-sap-s-4hana\|Test Script: Compliance Formats – Support Preparation (1J2_AE) – SAP S/4HANA Cloud Public Edition 2608 (1J2_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for UAE statutory reporting (scope 1J2_AE): config prerequisites, VAT return, FAF audit file, cash flow statement. |

### Document and Reporting Compliance Framework

How the eDocument Cockpit and statutory reporting framework process electronic documents and report runs, with e-mail delivery, approval workflow and consistency checks.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/document-and-reporting-compliance-5xu-test-script-sap-s-4hana-cloud-pu\|Document and Reporting Compliance (5XU) - Test Script, SAP S/4HANA Cloud Public Edition (5XU_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 5XU Document and Reporting Compliance (S/4HANA Cloud 2608): eDocuments, statutory reports, email, approval workflow, consistency. |

## Related categories
- related-to :: [[03-financial-accounting-and-close/_cluster]]
- related-to :: [[08-sales-order-management/_cluster]]
