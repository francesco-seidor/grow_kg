---
title: Leasing and Real Estate
description: "Real estate rental objects and contracts, lease-in and lease-out/sublease accounting in local, IFRS and US GAAP ledgers, sales-based rent, and earmarked funds from lease-in contracts."
cluster: 17-leasing-and-real-estate
type: cluster
tags: [kb/leasing-and-real-estate, kb/hub]
keywords: [leasing, lease-in, lease-out, sublease, real estate, rental object, contract management, lease accounting, sales-based rent, earmarked funds]
node_count: 19
created: 2026-10-12
updated: 2026-10-12
---

# Leasing and Real Estate

Covers real estate rental objects and contract/lease management: lease-in (lessee) and lease-out/sublease (lessor) contracts, valuation, periodic posting, rent and index adjustments, sales-based rent, and earmarked funds generated from lease-in contracts. Excludes general G/L, AP/AR, fixed assets and general earmarked funds (see 03).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Real Estate Rental Objects and Lease Accounting

How rental objects are created, expense types and G/L determination set for contract and lease management, and buildings linked from SAP Cloud for Real Estate.

| Node | Description |
| --- | --- |
| [[17-leasing-and-real-estate/test-script-integration-of-sap-s-4hana-and-sap-cloud-for-real-estate-4\|Test Script: Integration of SAP S/4HANA and SAP Cloud for Real Estate (4X3) (4X3_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 4X3: assigning a building in SAP Cloud for Real Estate to an existing or new leasing contract via app F6627 (S/4HANA Cloud Public 2608). |
| [[17-leasing-and-real-estate/accounting-interface-for-contract-and-lease-management-7od-ae-test-scr\|Accounting Interface for Contract and Lease Management (7OD_AE) - Test Script (7OD_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7OD (AE): real estate expense types, G/L determination, posting periods, and reviewing finance notifications. |
| [[17-leasing-and-real-estate/stammdatenskript-mietobjekt-anlegen-sds-7ad-520\|Stammdatenskript: Mietobjekt anlegen – SDS (7AD) (7AD_S4CLD2608_Master_Data_DE_XX)]] | German master data script (SAP S/4HANA Cloud Public Edition 2608, scope 7AD): creating generic rental objects (usable/rentable, intercompany) with prerequisites and test steps. |
| [[17-leasing-and-real-estate/create-rental-object-master-data-script-7ad-521\|Create Rental Object – Master Data Script (7AD) (7AD_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (scope item 7AD) for creating usable, rentable and intercompany rental objects, with prerequisites and test steps. |
| [[17-leasing-and-real-estate/script-de-datos-maestros-crear-objeto-de-alquiler-mds-7ad-522\|Script de datos maestros - Crear objeto de alquiler – MDS (7AD) (7AD_S4CLD2608_Master_Data_ES_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (7AD, Spanish): creating usable and rentable generic rental objects, incl. intercompany, with test steps. |
| [[17-leasing-and-real-estate/sap-s-4hana-cloud-public-edition-mds-7ad-523\|マスタデータスクリプト SAP S/4HANA Cloud Public Edition - 賃貸対象の登録 – MDS (7AD) (7AD_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (7AD, SAP S/4HANA Cloud Public Edition 2608) for registering general rental objects: usable, rentable and intercompany, with/without portfolio structure. |
| [[17-leasing-and-real-estate/script-de-dados-mestre-criar-objeto-de-locacao-mds-7ad-524\|Script de dados mestre - Criar objeto de locação (MDS 7AD) (7AD_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (7AD) for SAP S/4HANA Cloud Public Edition 2608: creating generic lease objects (usable/rentable, intercompany), prerequisites and test steps. |
| [[17-leasing-and-real-estate/sap-s-4hana-cloud-public-edition-mds-7ad-525\|主数据脚本 SAP S/4HANA Cloud Public Edition - 创建租赁对象 - MDS (7AD) (7AD_S4CLD2608_Master_Data_ZH_XX)]] | Chinese machine-translated master data script (7AD) for creating generic lease objects (usable/leasable, intercompany) in S/4HANA Cloud Public Edition 2608, with test steps. |

### Lease-In Accounting

How lease-in and service contracts are created, valuated in local, IFRS or US GAAP ledgers, posted, adjusted for rent and index changes, renewed, terminated and turned into earmarked funds.

| Node | Description |
| --- | --- |
| [[17-leasing-and-real-estate/test-script-earmarked-funds-for-real-estate-contracts-6r3-sap-s-4hana\|Test Script: Earmarked Funds for Real Estate Contracts (6R3) - SAP S/4HANA Cloud Public Edition (6R3_S4CLD2608_BPD_EN_XX)]] | SAP test script for scope item 6R3: configure and test earmarked funds auto-generated from lease-in contracts (create, approve, post, report) in S/4HANA Cloud. |
| [[17-leasing-and-real-estate/test-script-sap-s-4hana-cloud-public-edition-lease-in-accounting-1t6-a\|Test Script SAP S/4HANA Cloud Public Edition - Lease-In Accounting (1T6_AE) (1T6_S4CLD2608_BPD_EN_AE)]] | SAP best-practice test script (scope item 1T6, AE, release 2608) for Lease-In Accounting: prerequisites, config steps and step-by-step test procedures for contracts, valuation, posting, adjustment. |
| [[17-leasing-and-real-estate/lease-in-accounting-group-ledger-ifrs-21p-ae-test-script-797\|Lease-In Accounting – Group Ledger IFRS (21P_AE) Test Script (21P_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 21P Lease-In Accounting Group Ledger IFRS: prerequisites, config steps and Fiori test procedures. |
| [[17-leasing-and-real-estate/test-script-sap-s-4hana-cloud-public-edition-service-contract-21r-ae-7\|Test Script SAP S/4HANA Cloud Public Edition - Service Contract (21R_AE) (21R_S4CLD2608_BPD_EN_AE)]] | Test script (21R, UAE localization, 2608) for Service Contract / lease contract management: config prerequisites, contract lifecycle, postings, adjustments, reports, archiving. |
| [[17-leasing-and-real-estate/test-script-lease-in-accounting-group-ledger-us-gaap-34n-ae-914\|Test Script: Lease-In Accounting – Group Ledger US GAAP (34N_AE) (34N_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (2608, AE) for scope item 34N: lease-in contracts, valuation, postings, adjustments, prerequisites and technical jobs. |

### Lease-Out, Sublease and Sales-Based Rent Accounting

How lease-out and sublease contracts (incl. intercompany) are valuated, invoiced and posted periodically, and how sales-based rent is reported, settled and adjusted.

| Node | Description |
| --- | --- |
| [[17-leasing-and-real-estate/test-script-lease-out-accounting-21q-ae-sap-s-4hana-cloud-public-editi\|Test Script: Lease-Out Accounting (21Q_AE) - SAP S/4HANA Cloud Public Edition (21Q_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 21Q (UAE) Lease-Out Accounting, release 2608: prerequisites, SSCUI setup, and test steps for contracts, periodic posting, invoicing, adjustment. |
| [[17-leasing-and-real-estate/intercompany-process-for-sublease-accounting-2o9-test-script-sap-s-4ha\|Intercompany Process for Sublease Accounting (2O9) - Test Script, SAP S/4HANA Cloud Public Edition (2O9_S4CLD2608_BPD_EN_XX)]] | SAP test script for scope item 2O9: intercompany sublease accounting (lease-out) under local GAAP (2SB), IFRS (2SA) and US GAAP (34O), with prerequisites and test steps. |
| [[17-leasing-and-real-estate/lease-out-for-sublease-accounting-group-ledger-ifrs-2sa-ae-858\|Lease-Out for Sublease Accounting – Group Ledger IFRS (2SA_AE) (2SA_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 2SA: IFRS 16 lease-out sublease contracts, valuation, posting, invoicing, adjustment, with prerequisites. |
| [[17-leasing-and-real-estate/test-script-lease-out-for-sublease-accounting-2sb-ae-859\|Test Script: Lease-Out for Sublease Accounting (2SB_AE) (2SB_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2SB (UAE, company code 3310): lease-out sublease contracts, valuation, posting, invoicing, adjustment. |
| [[17-leasing-and-real-estate/test-script-lease-out-for-sublease-accounting-group-ledger-us-gaap-34o\|Test Script: Lease-Out for Sublease Accounting – Group Ledger US GAAP (34O_AE) (34O_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 34O (UAE, company code 3310): lease-out sublease contracts, valuation, posting, invoicing, adjustment, admin. |
| [[17-leasing-and-real-estate/test-script-sales-based-rent-3f4-ae-sap-s-4hana-cloud-public-edition-9\|Test Script: Sales-Based Rent (3F4_AE) - SAP S/4HANA Cloud Public Edition (3F4_S4CLD2608_BPD_EN_AE)]] | SAP test script (scope item 3F4, UAE) for sales-based rent in leasing: prerequisites, config SSCUIs, and step-by-step tests for contracts, accounting, settlement, adjustment, jobs, archiving. |

## Related categories
- related-to :: [[03-financial-accounting-and-close/_cluster]]
