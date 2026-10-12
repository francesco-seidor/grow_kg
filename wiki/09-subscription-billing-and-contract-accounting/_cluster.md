---
title: Subscription Billing and Contract Accounting
description: "Subscription products, SAP Subscription Billing, Convergent Invoicing (billable and consumption items, rating, partner settlement) and FI-CA contract accounting integration."
cluster: 09-subscription-billing-and-contract-accounting
type: cluster
tags: [kb/subscription-billing-and-contract-accounting, kb/hub]
keywords: [subscription, SAP Subscription Billing, convergent invoicing, billable items, consumption items, rating, FI-CA, contract accounting, provider contract]
node_count: 50
created: 2026-10-12
updated: 2026-10-12
---

# Subscription Billing and Contract Accounting

Covers recurring and usage-based billing and FI-CA. Excludes standard SD billing (see 08) and event-based revenue recognition for subscriptions (see 06).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Consumption Items and Service-Type-Based Rating

How consumption items are uploaded and rated into billable items, and how service-type pricing conditions (PST0-PST2) drive rating.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/serviceartbasierte-preiskondition-anlegen-sds-3gd-316\|Serviceartbasierte Preiskondition anlegen – SDS (3GD) (3GD_S4CLD2608_Master_Data_DE_XX)]] | German master data script 3GD: create service-type-based sales price conditions PST0, PST1, PST2 via Set Material Prices - Sales (VK12) for convergent billing rating. |
| [[09-subscription-billing-and-contract-accounting/master-data-script-create-service-type-based-pricing-condition-mds-3gd\|Master Data Script - Create Service Type Based Pricing Condition - MDS (3GD) (3GD_S4CLD2608_Master_Data_EN_XX)]] | Master data script (3GD) for creating service-type-based pricing conditions PST0, PST1, PST2 via Set Material Prices - Sales (VK12) for Convergent Invoicing rating. |
| [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-condicion-de-determinacion-de-precios-b\|Script de datos maestros - Crear condición de determinación de precios basada en clase de servicio – MDS (3GD) (3GD_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) master data script (3GD) for SAP S/4HANA Cloud: creating service-class-based pricing conditions PST0, PST1, PST2 via VK12. |
| [[09-subscription-billing-and-contract-accounting/mds-3gd-319\|サービスタイプに基づく価格設定条件の登録 - MDS (3GD) (3GD_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script 3GD: maintaining service-type based pricing conditions PST0, PST1, PST2 via app VK12 for consolidated billing in S/4HANA Cloud Public Edition 2608. |
| [[09-subscription-billing-and-contract-accounting/criar-condicao-de-determinacao-de-precos-baseada-em-tipo-de-servico-md\|Criar condição de determinação de preços baseada em tipo de serviço – MDS (3GD) (3GD_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP master data script 3GD: creating service-type-based pricing conditions PST0, PST1, PST2 in VK12 as Pricing Specialist (convergent billing). |
| [[09-subscription-billing-and-contract-accounting/mds-3gd-321\|创建基于服务类型的定价条件 - MDS (3GD) (3GD_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 3GD for creating service-type-based pricing conditions PST0, PST1, PST2 via Manage Material Prices - Sales (VK12 |
| [[09-subscription-billing-and-contract-accounting/test-script-convergent-invoicing-management-and-rating-of-consumption\|Test Script - Convergent Invoicing – Management and Rating of Consumption Items (3DX_AE) (3DX_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3DX: uploading, displaying and rating consumption items to create billable items in Convergent Invoicing. |

### Convergent Invoicing Analytical Apps

How to analyze unbilled items (F1427) and unrated items (F1977) as Convergent Invoicing specialist.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/test-script-sap-fiori-analytical-apps-for-convergent-invoicing-special\|Test Script: SAP Fiori Analytical Apps for Convergent Invoicing Specialist (2KF) (2KF_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud 2608 test script for scope item 2KF: analyzing unbilled items (F1427) and unrated items (F1977) as Convergent Invoicing Specialist. |

### Cost Handling for Subscriptions and Usage

How cost of sales is posted through billable items, billing and invoicing in Convergent Invoicing.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/convergent-invoicing-cost-handling-for-subscriptions-and-usage-6wd-ae\|Convergent Invoicing – Cost Handling for Subscriptions and Usage (6WD_AE) Test Script (6WD_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 6WD: posting cost of sales via billable items, billing and invoicing in Convergent Invoicing. |

### Contract Accounting Cash Application

How ML-based cash application in FI-CA transfers clarification cases and posts payment lot proposals.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-cash-application-47i-ae-1001\|Test Script - Contract Accounting – Cash Application (47I_AE) (47I_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for scope item 47I: ML-based cash application in FI-CA, transferring and processing clarification cases and posting ML proposals. |

### Contract Accounting with Contract-Based Revenue Recognition

How FI-CA integrates with contract-based revenue recognition: performance obligations, fulfillment and postings.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-contract-based-revenue-recognition-3l3\|Test Script: Contract Accounting – Contract-Based Revenue Recognition (3L3_AE) (3L3_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3L3 (AE): integrating contract accounting with contract-based revenue recognition, with prerequisites and steps. |

### Contract Accounting Integration with Sales Documents

How SD billing documents post to FI-CA contract accounts in the lean scenario and how billing is reconciled.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-integration-with-sales-documents-43y-a\|Test Script: Contract Accounting - Integration with Sales Documents (43Y_AE) - SAP S/4HANA Cloud Public Edition (43Y_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 43Y_AE: SD billing posted to FI-CA (lean scenario), with configuration, test steps and reconciliation. |

### Convergent Invoicing: Recurring, One-Off and Usage Billing, Invoice Correction

How Convergent Invoicing turns billing plans and usage into billable items, runs billing and invoicing (2T3, 2BG), and corrects invoices via credit/debit memo requests (2BE).

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/convergent-invoicing-invoice-correction-processing-2be-ae-test-script\|Convergent Invoicing – Invoice Correction Processing (2BE_AE) – Test Script (2BE_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud test script, scope item 2BE_AE: invoice correction via credit/debit memo billing requests, optional approval workflow, billing, invoicing, print. |
| [[09-subscription-billing-and-contract-accounting/test-script-convergent-invoicing-invoice-creation-for-usage-and-servic\|Test Script: Convergent Invoicing – Invoice Creation for Usage and Service (2BG_AE) (2BG_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (scope item 2BG, AE) for Convergent Invoicing: billable items, billing, invoicing, clarification, reversal, with preliminary config steps. |
| [[09-subscription-billing-and-contract-accounting/convergent-invoicing-recurring-and-one-off-items-2t3-ae-test-script-86\|Convergent Invoicing – Recurring and One-Off Items (2T3_AE) Test Script (2T3_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (2T3_AE) for Convergent Invoicing: billing plans, billable items, billing and invoicing runs. |

### Revenue Sharing, Partner and Intercompany Settlement

How Convergent Invoicing calculates partner shares from billable items and settles them to partners (42L) or between company codes as intercompany settlement (6WC).

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/convergent-invoicing-intercompany-settlement-6wc-ae-1197\|Convergent Invoicing – Intercompany Settlement (6WC_AE) (6WC_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition test script (scope item 6WC_AE): configure and test Convergent Invoicing intercompany settlement, from billable items to payment. |
| [[09-subscription-billing-and-contract-accounting/test-script-convergent-invoicing-revenue-sharing-and-partner-settlemen\|Test Script: Convergent Invoicing – Revenue Sharing and Partner Settlement (42L_AE) (42L_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 42L: revenue sharing and partner settlement in Convergent Invoicing, from billable items to partner invoicing. |

### Subscription Management with Convergent Invoicing

How subscriptions create provider contracts, billable items and invoices in Convergent Invoicing.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/test-script-subscription-management-with-convergent-invoicing-5ik-ae-1\|Test Script: Subscription Management with Convergent Invoicing (5IK_AE) (5IK_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5IK (AE): subscriptions in SAP Subscription Billing, provider contract, pre-bill and convergent invoicing. |

### Subscription Management with Sales Billing

How subscriptions in SAP Subscription Billing create pre-bills, SD billing documents, credits and renewals.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/test-script-subscription-management-with-sales-billing-57z-ae-1072\|Test Script: Subscription Management with Sales Billing (57Z_AE) (57Z_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 57Z: subscriptions in SAP Subscription Billing, pre-bill, billing document, credit and debit memos. |

### Subscription Products and Rate Plans

How subscription products, rate elements, rate plan templates and pricing lookup tables are created and enriched as SBPD/SBRE products.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/test-script-subscription-management-for-software-5sw-ae-sap-s-4hana-cl-part-01\|Test Script: Subscription Management for Software (5SW_AE) - SAP S/4HANA Cloud Public Edition 2608 (5SW_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | Test script for scope item 5SW_AE: software subscription master data, solution orders, entitlements, provisioning, billing, revenue recognition, changes. |
| [[09-subscription-billing-and-contract-accounting/test-script-subscription-management-for-software-5sw-ae-sap-s-4hana-cl-part-02\|Test Script: Subscription Management for Software (5SW_AE) - SAP S/4HANA Cloud Public Edition 2608 (5SW_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | Test script (part 2 of 2): SAP Entitlement Management jobs, provisioning/decommissioning responses via SoapUI, Subscription Billing checks, end-of-contract. |
| [[09-subscription-billing-and-contract-accounting/stammdatenskript-abonnementprodukt-anlegen-sales-billing-sds-5bd-424\|Stammdatenskript: Abonnementprodukt anlegen (Sales Billing) – SDS (5BD) (5BD_S4CLD2608_Master_Data_DE_XX)]] | German master data script (5BD) for creating subscription products in SAP Subscription Billing, Price Calculation Service and S/4HANA Cloud Public Edition 2608, US and DE variants. |
| [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-sales-billing-mds-5bd-4\|Master Data Script: Create Subscription Product Sales Billing - MDS (5BD) (5BD_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (5BD): create subscription products and rate elements in SAP Subscription Billing, then enrich them in S/4HANA. |
| [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-crear-facturacion-de-ventas-de-productos-de-s\|Script de datos maestros: Crear facturación de ventas de productos de suscripción - MDS (5BD) (5BD_S4CLD2608_Master_Data_ES_XX)]] | Spanish SAP S/4HANA Cloud Public Edition 2608 master data script (5BD): create subscription products, rate elements, rate plan templates and pricing lookup tables. |
| [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-mds-5bd-427\|マスタデータスクリプト SAP S/4HANA Cloud Public Edition - サブスクリプション製品販売請求の登録 - MDS (5BD) (5BD_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (5BD) for creating subscription products in SAP Subscription Billing, Price Calculation lookup tables, and extending SBPD/SBRE products in S/4HANA. |
| [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-de-vendas-de-produto-de-assin\|Script de dados mestre - Criar faturamento de vendas de produto de assinatura - MDS (5BD) (5BD_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (PT, 5BD): create subscription products in SAP Subscription Billing and extend them in S/4HANA. |
| [[09-subscription-billing-and-contract-accounting/mds-5bd-429\|创建订阅产品销售开票 - MDS (5BD) (5BD_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 5BD for SAP S/4HANA Cloud 2608: creating subscription billing products, rate elements, pricing lookup tables and S/4HANA product enrichment. |
| [[09-subscription-billing-and-contract-accounting/stammdatenskript-abonnementprodukt-anlegen-convergent-invoicing-sds-5l\|Stammdatenskript: Abonnementprodukt anlegen (Convergent Invoicing) – SDS (5LP) (5LP_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition 2608 master data script (5LP): create business partner, contract account, Subscription Billing products, rate plans, price lookup tables. |
| [[09-subscription-billing-and-contract-accounting/master-data-script-create-subscription-product-convergent-invoicing-md\|Master Data Script: Create Subscription Product Convergent Invoicing - MDS (5LP) (5LP_S4CLD2608_Master_Data_EN_XX)]] | Step-by-step master data script (5LP) for S/4HANA Cloud Public Edition 2608: FI-CA business partner, contract account, SAP Subscription Billing products and SBPD/SBRE enrichment. |
| [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-facturacion-convergente-de-produc\|Script de datos maestros - Creación de facturación convergente de productos de suscripción (5LP) (5LP_S4CLD2608_Master_Data_ES_XX)]] | Spanish master data script (5LP, S/4HANA Cloud Public Edition 2608): create business partner, contract account, subscription products, price tables and extend SBPD/SBRE products. |
| [[09-subscription-billing-and-contract-accounting/mds-5lp-451\|サブスクリプション製品統合請求の登録 - MDS (5LP) (5LP_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (5LP) for SAP S/4HANA Cloud Public Edition 2608: creating BPs, contract accounts, and subscription products in SAP Subscription Billing and S/4HANA. |
| [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-faturamento-convergente-de-produto-de-ass\|Script de dados mestre - Criar faturamento convergente de produto de assinatura - MDS (5LP) (5LP_S4CLD2608_Master_Data_PT_XX)]] | Master data script (PT) for SAP S/4HANA Cloud Public Edition 2608: create subscription products, rate elements, price lookup tables and enrich SBPD/SBRE products (5LP). |
| [[09-subscription-billing-and-contract-accounting/sap-s-4hana-cloud-public-edition-convergent-invoicing-mds-5lp-453\|主数据脚本 SAP S/4HANA Cloud Public Edition - 创建订阅产品 Convergent Invoicing - MDS (5LP) (5LP_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 5LP: create business partners, contract accounts and subscription products in SAP Subscription Billing and enrich them in S/4HANA. |

### Variant-Configured Products in Provider Contracts

How configurable products with variant pricing are used in provider contracts for consumption-based rating, billing and invoicing.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/stammdatenskript-produktstamm-fur-verbrauchsbasierte-abrechnung-anlege\|Stammdatenskript - Produktstamm für verbrauchsbasierte Abrechnung anlegen (3JA) (3JA_S4CLD2608_Master_Data_DE_XX)]] | German master data script (3JA) for SAP S/4HANA Cloud Public Edition: create configurable material with variant pricing for consumption-based billing. |
| [[09-subscription-billing-and-contract-accounting/master-data-script-create-product-master-for-consumption-based-billing\|Master Data Script: Create Product Master for Consumption Based Billing - MDS (3JA) (3JA_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (3JA) for creating a configurable product master with variant pricing for consumption-based billing. |
| [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-maestro-de-productos-para-factura\|Script de datos maestros - Creación de maestro de productos para facturación basada en consumo (3JA) (3JA_S4CLD2608_Master_Data_ES_XX)]] | Spanish SAP S/4HANA Cloud 2608 master data script (3JA): create configurable material with variant pricing for consumption-based billing, step by step. |
| [[09-subscription-billing-and-contract-accounting/mds-3ja-325\|使用量基準料金計算の製品マスタ登録 - MDS (3JA) (3JA_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud Public Edition 2608 master data script (3JA): create configurable product master with characteristics, class, variant pricing for usage-based billing. |
| [[09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-dados-mestre-do-produto-para-faturamento\|Script de dados mestre - Criar dados mestre do produto para faturamento baseado em consumo (3JA) (3JA_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (3JA) for SAP S/4HANA Cloud Public Edition: create configurable material with variant pricing for consumption-based billing. |
| [[09-subscription-billing-and-contract-accounting/mds-3ja-327\|为基于消耗的开票创建产品主数据 - MDS (3JA) (3JA_S4CLD2608_Master_Data_ZH_XX)]] | Chinese machine-translated SAP S/4HANA Cloud 2608 master data script (3JA): create configurable product master with characteristics, class, variant pricing for consumption-based billing. |
| [[09-subscription-billing-and-contract-accounting/contract-accounting-enabling-of-products-with-variant-configuration-3l\|Contract Accounting – Enabling of Products with Variant Configuration (3L8_AE) – Test Script (3L8_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3L8_AE: variant configuration products in provider contracts, with rating, billing and invoicing. |

### Contract Accounting Master Data and Basic Functions

How FI-CA business partners, contract accounts and provider contracts are created, and account statements, correspondence and data privacy handled.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-master-data-and-basic-functions-2ar-ae\|Test Script: Contract Accounting – Master Data and Basic Functions (2AR_AE) (2AR_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition test script for scope item 2AR (FI-CA, AE): business partner, contract account, provider contract, correspondence, privacy. |

### Contract Accounting Incoming and Outgoing Payments

How FI-CA handles customer-initiated payments (cards, payment service providers, pay-by-link, payment and check lots) and company-initiated payment runs and returns.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo-part-01\|Test Script SAP S/4HANA Cloud Public Edition - Contract Accounting – Customer Initiated Payments (2BI_AE) (2BI_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | Test script for scope item 2BI_AE (FI-CA customer-initiated payments, AED): payment cards, PSP, pay-by-link, payment/check lots, returns, workflows. |
| [[09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo-part-02\|Test Script SAP S/4HANA Cloud Public Edition - Contract Accounting – Customer Initiated Payments (2BI_AE) (2BI_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | Test script for FI-CA customer-initiated payments (S/4HANA Cloud 2608); this part: External Cash Desk setup and APIs, intraday bank statement posting. |
| [[09-subscription-billing-and-contract-accounting/contract-accounting-company-initiated-payments-2dp-ae-test-script-813\|Contract Accounting – Company Initiated Payments (2DP_AE) Test Script (2DP_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 2DP_AE (UAE): FI-CA company-initiated payments, payment runs, card orders, returns, revenue distribution. |

### Contract Accounting Closing and Valuation

How FI-CA day-end and month-end closing posts value adjustments, write-offs, FX valuation and reclassifications in local, IFRS and US GAAP ledgers.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-daily-and-monthly-closing-2bk-ae-812\|Test Script: Contract Accounting – Daily and Monthly Closing (2BK_AE) (2BK_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (scope item 2BK, UAE/AED) for FI-CA day-end and month-end closing: value adjustments, write-offs, FX valuation, reclassification, G/L reconciliation. |
| [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-group-ledger-us-gaap-33v-ae-904\|Test Script: Contract Accounting – Group Ledger US GAAP (33V_AE) (33V_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script (33V_AE, company code 3310): US GAAP ledger FI-CA steps for doubtful receivables, FX valuation, reclassification, closing. |
| [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-group-ledger-ifrs-33x-ae-905\|Test Script: Contract Accounting – Group Ledger IFRS (33X_AE) (33X_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 33X_AE: IFRS ledger doubtful receivables, FX valuation, reclassifications and closing in FI-CA. |

### Contract Accounting Open Item Management and Collections

How FI-CA dunning, installment plans, interest, deposits, disputes and collections manage open items, and which analytical apps track overdue items and worklists.

| Node | Description |
| --- | --- |
| [[09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-sap-fiori-analytical-apps\|Test Script SAP S/4HANA Cloud Public Edition - SAP Fiori Analytical Apps for Contract Accounting Manager (2KH) (2KH_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 2KH: Fiori analytical apps for FI-CA (overdue items, locks, dunning, collections, returns, incoming payments) and My Open Worklists, release 2608. |
| [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-open-item-management-2uj-ae-872-part-01\|Test Script: Contract Accounting – Open Item Management (2UJ_AE) (2UJ_S4CLD2608_BPD_EN_AE) — part 1 of 2]] | S/4HANA Cloud test script, Contract Accounting Open Item Management (2UJ_AE): dunning, installment plans, interest, credits, deposits, disputes, collections. |
| [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-open-item-management-2uj-ae-872-part-02\|Test Script: Contract Accounting – Open Item Management (2UJ_AE) (2UJ_S4CLD2608_BPD_EN_AE) — part 2 of 2]] | Step-by-step test script (AE, company code 3310) for SAP S/4HANA Cloud 2608 Contract Accounting 2UJ: factoring, promise to pay, dunning, transfers, APIs. |

## Related categories
- related-to :: [[08-sales-order-management/_cluster]]
- related-to :: [[06-management-accounting/_cluster]]
