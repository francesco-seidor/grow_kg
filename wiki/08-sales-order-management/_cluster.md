---
title: Sales Order Management
description: "Inquiries, sales orders, pricing, free goods, customer hierarchies, ATP and substitution, third-party and intercompany sales, billing, memos, returns, complaints and card payments."
cluster: 08-sales-order-management
type: cluster
tags: [kb/sales-order-management, kb/hub]
keywords: [sales order, pricing, free goods, customer hierarchy, ATP, substitution, third-party sales, intercompany sales, billing, credit memo, returns, complaints]
node_count: 116
created: 2026-10-12
updated: 2026-10-12
---

# Sales Order Management

Covers order-to-cash, including intercompany sales between company codes of one system. Excludes subscription and usage billing (see 09), EWM outbound and stock transfers (see 11), service orders and project billing (see 14), retail store sales (see 15), VAT and PEPPOL setup (see 04), credit management (see 03) and HQ-subsidiary sales (see 16).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Advanced Intercompany Sales

How advanced intercompany sales between company codes post goods issue into stock in transit, and how roles, postings and valuation work.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-advanced-intercompany-sales-5d2-ae-sap-s-4hana-cloud-publi\|Test Script: Advanced Intercompany Sales (5D2_AE) - SAP S/4HANA Cloud Public Edition (5D2_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5D2 Advanced Intercompany Sales (AE): prerequisites, test steps by role, postings, value chain monitoring. |
| [[08-sales-order-management/test-script-advanced-intercompany-sales-make-to-order-and-variant-conf\|Test Script: Advanced Intercompany Sales – Make-to-Order and Variant Config (7DM_AE) (7DM_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script (7DM_AE): advanced intercompany sales with make-to-order and variant configuration, prerequisites to value chain monitoring. |

### Available-to-Promise and Backorder Processing

How product availability is checked and monitored, backorder processing runs, and advanced ATP alternative-based confirmation and supply protection work.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-advanced-available-to-promise-consumer-products-6n0-ae-117\|Test Script: Advanced Available-to-Promise - Consumer Products (6N0_AE) (6N0_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 6N0 (aATP, Alternative-Based Confirmation, Supply Protection), AE localization, dated 19-06-26. |
| [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-advanced-available-to-pro\|Test Script: SAP S/4HANA Cloud Public Edition - Advanced Available-to-Promise Processing (1JW_AE) (1JW_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 1JW_AE (AE): Release for Delivery, Product Allocation, Alternative-Based Confirmation, Supply Protection, BPS. |
| [[08-sales-order-management/basic-available-to-promise-processing-2ln-ae-test-script-832\|Basic Available-to-Promise Processing (2LN_AE) - Test Script (2LN_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2LN_AE: product availability monitoring, backorder processing (BOP) setup and runs, ATP log deletion. |

### Customer Complaint Handling

How customer complaints are created, submitted and approved, and how follow-up credit/debit documents and document flow work.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-complaint-handling-7bg-12\|Test Script SAP S/4HANA Cloud Public Edition - Complaint Handling (7BG) (7BG_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 7BG Complaint Handling (2608): create, submit, approve customer complaints, follow-up documents, document flow, pricing, partners, PDF output. |

### Opportunity to Order with SAP Sales Cloud and Cloud for Customer

How master data replicates and opportunities, quotes and sales orders flow between SAP Sales Cloud (C4C or V2) and S/4HANA.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-opportunity-to-order-with-sap-sales-cloud-version-2-6ko-11\|Test Script: Opportunity to Order with SAP Sales Cloud Version 2 (6KO) (6KO_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 6KO: integration of SAP Sales Cloud V2 with S/4HANA, from master data replication to quote and order. |
| [[08-sales-order-management/test-script-opportunity-to-order-with-sap-cloud-for-customer-1vp-765\|Test Script: Opportunity-to-Order with SAP Cloud for Customer (1VP) (1VP_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1VP: C4C-to-S/4HANA master data replication, opportunity, quote, sales order, equipment and BP blocking. |

### Customer Hierarchies

How customers are created and assigned into customer hierarchies used for sales pricing and reporting.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/stammdatenskript-kundenhierarchiestammdatenskript-anlegen-6n3-514\|Stammdatenskript: Kundenhierarchiestammdatenskript anlegen (6N3) (6N3_S4CLD2608_Master_Data_DE_XX)]] | German master data test script (6N3) for SAP S/4HANA Cloud Public Edition 2608: create customer master data (general, company code, sales area) and customer hierarchies. |
| [[08-sales-order-management/create-customer-hierarchy-master-data-script-6n3-515\|Create Customer Hierarchy Master Data Script (6N3) (6N3_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script (6N3): create customer master data (general, company code, sales area) and customer hierarchies in Fiori. |
| [[08-sales-order-management/script-de-datos-maestros-crear-script-de-datos-maestros-de-jerarquia-d\|Script de datos maestros - Crear script de datos maestros de jerarquía de clientes (6N3) (6N3_S4CLD2608_Master_Data_ES_XX)]] | Spanish test script (6N3) for SAP S/4HANA Cloud Public Edition 2608: creating customer master data (general, company code, sales area) and customer hierarchies. |
| [[08-sales-order-management/6n3-517\|マスタデータスクリプト 得意先階層マスタデータスクリプトの登録 (6N3) (6N3_S4CLD2608_Master_Data_JA_XX)]] | Japanese SAP S/4HANA Cloud Public Edition master data script (6N3): create customer master (general, company code, sales area) and customer hierarchies via BP and F0850A/F5794. |
| [[08-sales-order-management/script-de-dados-mestre-criar-script-de-dados-mestre-de-hierarquia-de-c\|Script de dados mestre - Criar script de dados mestre de hierarquia de clientes (6N3) (6N3_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script (PT) for creating customer master data (general, company, sales area) and customer hierarchies via Fiori apps. |
| [[08-sales-order-management/6n3-519\|创建客户层次结构主数据脚本 (6N3) (6N3_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 6N3 for SAP S/4HANA Cloud Public Edition: create customer master data (general, company code, sales area) and customer hierarchies. |

### Customer-Material Info Records

How to create customer-material info records with customer material numbers and sales unit conversion in Manage Customer Materials (F2499).

| Node | Description |
| --- | --- |
| [[08-sales-order-management/kundenmaterial-infosatz-anlegen-sds-2yx-292\|Kundenmaterial-Infosatz anlegen – SDS (2YX) (2YX_S4CLD2608_Master_Data_DE_XX)]] | German SAP master data script (2YX, 2608): create a customer-material info record in app F2499 as internal sales representative, incl. sales unit conversion. |
| [[08-sales-order-management/create-customer-material-info-record-mds-2yx-293\|Create Customer-Material Info Record - MDS (2YX) (2YX_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script for creating a customer-material info record in Manage Customer Materials (F2499), incl. sales unit conversion. |
| [[08-sales-order-management/crear-registro-info-para-cliente-y-material-mds-2yx-294\|Crear registro info para cliente y material - MDS (2YX) (2YX_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) master data script 2YX: create customer-material info record via Gestionar materiales de cliente (F2499) in S/4HANA Cloud 2608. |
| [[08-sales-order-management/mds-2yx-295\|得意先/品目情報レコード登録 - MDS (2YX) (2YX_S4CLD2608_Master_Data_JA_XX)]] | SAP S/4HANA Cloud Public Edition 2608 マスタデータスクリプト (2YX): 得意先品目管理 (F2499) で得意先/品目情報レコードを登録する手順 (日本語)。 |
| [[08-sales-order-management/criar-registro-info-de-material-do-cliente-mds-2yx-296\|Criar registro info de material do cliente – MDS (2YX) (2YX_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP master data script (2YX, 2608): create a customer-material info record in app F2499 as internal sales representative, incl. sales unit conversion. |
| [[08-sales-order-management/mds-2yx-297\|创建客户物料信息记录 - MDS (2YX) (2YX_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script 2YX: create a customer-material information record with Manage Customer Materials app F2499. |

### Customer Returns for Variant-Configured Materials

How returns of variant-configured materials flow from returns order through goods receipt and inspection to credit memo.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/customer-returns-for-material-with-variant-configuration-7kw-ae-test-s\|Customer Returns for Material with Variant Configuration (7KW_AE) - Test Script (7KW_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 7KW: customer returns of variant-configured materials, from returns order to credit memo, with job scheduling appendix. |

### Debit and Credit Memo Processing

How debit and credit memo requests are created, approved, billing blocks removed and memos billed, including variant-configured items.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/test-script-invoice-correction-process-with-debit-memo-bdq-ae-1257\|Test Script: Invoice Correction Process with Debit Memo (BDQ_AE) (BDQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item BDQ (UAE): debit memo request, billing, eDocument PEPPOL submission, plus prerequisites and job scheduling. |
| [[04-tax-and-statutory-reporting/test-script-debit-memo-processing-1f1-ae-sap-s-4hana-cloud-public-edit\|Test Script: Debit Memo Processing (1F1_AE) - SAP S/4HANA Cloud Public Edition (1F1_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 1F1 (UAE): debit memo request, billing block removal, debit memo creation, PEPPOL eDocument cockpit, plus PEPPOL setup and billing job scheduling. |
| [[08-sales-order-management/test-script-credit-and-debit-memo-processing-with-variant-configuratio\|Test Script: Credit and Debit Memo Processing with Variant Configuration (7TZ_AE) (7TZ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item 7TZ: credit/debit memo requests with variant configuration, approval workflow, billing. |
| [[08-sales-order-management/invoice-correction-process-with-credit-memo-bkl-ae-test-script-sap-s-4\|Invoice Correction Process with Credit Memo (BKL_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BKL_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition 2608 UAE test script (BKL_AE): credit memo request, credit memo billing, PEPPOL eDocument cockpit, prerequisites, optional steps. |
| [[08-sales-order-management/test-script-credit-memo-processing-1ez-ae-sap-s-4hana-cloud-public-edi\|Test Script: Credit Memo Processing (1EZ_AE) - SAP S/4HANA Cloud Public Edition 2608, United Arab Emirates (1EZ_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script for scope item 1EZ_AE: UAE credit memo requests, optional AED-threshold approval workflow, credit memo billing, PEPPOL eDocument cockpit, billing jobs. |

### Outbound Delivery Without Order Reference

How to create an outbound delivery without a sales order and process picking, goods issue and proof of delivery.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-delivery-processing-without-order-reference-1mi-ae-736\|Test Script: Delivery Processing Without Order Reference (1MI_AE) (1MI_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 1MI: outbound delivery without order reference through picking, goods issue, POD and billing. |

### Digital Payments and Card Payments in Sales

How credit cards are registered on customers and payment card authorization, reauthorization and settlement work in sales orders.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-digital-payments-foundation-53v-1062\|Test Script: Digital Payments Foundation (53V) (53V_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 53V: adding and registering credit card data on a customer business partner via SAP digital payments in S/4HANA Cloud Public Edition 2608. |
| [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-digital-payments-1s2-ae-7\|Test Script: SAP S/4HANA Cloud Public Edition - Digital Payments (1S2_AE) (1S2_S4CLD2608_BPD_EN_AE)]] | SAP test script (release 2608, AE) for scope item 1S2 Digital Payments: card authorization, payment run, settlement, advice, clearing, refunds. |
| [[08-sales-order-management/test-script-digital-payments-sales-1z1-ae-sap-s-4hana-cloud-public-edi\|Test Script: Digital Payments – Sales (1Z1_AE), SAP S/4HANA Cloud Public Edition (1Z1_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for Digital Payments – Sales (1Z1): credit card authorization, cancellation, reauthorization and billing checks. |
| [[08-sales-order-management/external-digital-payments-2lz-ae-test-script-833\|External Digital Payments (2LZ_AE) Test Script (2LZ_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 2LZ_AE External Digital Payments in SAP S/4HANA Cloud Public Edition: prerequisites, AR/GL jobs, advice processing, card data. |

### External Billing Interface

How billing documents created through the external billing interface are checked.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-omnichannel-convergent-billing-1mc-ae-sap-s-4hana-cloud-pu\|Test Script: Omnichannel Convergent Billing (1MC_AE) - SAP S/4HANA Cloud Public Edition (1MC_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 1MC: combining external and internal billable data into one invoice via EBDR. |
| [[08-sales-order-management/external-billing-1z6-ae-test-script-792\|External Billing (1Z6_AE) Test Script (1Z6_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1Z6_AE: checking billing documents created via the external billing interface (AE). |

### Free Goods and Free-of-Charge Delivery

How free goods conditions are kept in VBN2 and flow through order, delivery and billing (BKA), and how free-of-charge deliveries run from CBFD order to pro forma invoice (BDA).

| Node | Description |
| --- | --- |
| [[08-sales-order-management/free-of-charge-delivery-bda-ae-test-script-sap-s-4hana-cloud-public-ed\|Free of Charge Delivery (BDA_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BDA_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 (AE) test script for free-of-charge delivery: CBFD sales order, delivery, picking, goods issue, pro forma and F2 invoice. |
| [[08-sales-order-management/free-goods-processing-bka-ae-test-script-sap-s-4hana-cloud-public-edit\|Free Goods Processing (BKA_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BKA_S4CLD2608_BPD_EN_AE)]] | SAP test script for Free Goods Processing (BKA_AE, UAE): sales order to delivery, picking, goods issue and billing, with prerequisites, roles, postings and alternative job scheduling. |
| [[08-sales-order-management/naturalrabattkondition-anlegen-sds-bew-544\|Naturalrabattkondition anlegen – SDS (BEW) (BEW_S4CLD2608_Master_Data_DE_XX)]] | German master data script (BEW) for creating a natural discount (free goods) condition in app VBN2 in SAP S/4HANA Cloud Public Edition 2608. |
| [[08-sales-order-management/master-data-script-create-free-goods-condition-mds-bew-545\|Master Data Script - Create Free Goods Condition - MDS (BEW) (BEW_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud 2608 master data script BEW: how a Pricing Specialist maintains free goods conditions per customer and material in app VBN2. |
| [[08-sales-order-management/script-de-datos-maestros-crear-condicion-de-bonificacion-en-especie-md\|Script de datos maestros - Crear condición de bonificación en especie - MDS (BEW) (BEW_S4CLD2608_Master_Data_ES_XX)]] | Spanish master data script (MDS BEW) with test steps to create free-goods (bonificación en especie) pricing conditions via app VBN2 in SAP S/4HANA Cloud Public Edition. |
| [[08-sales-order-management/mds-bew-547\|無償品条件の登録 - MDS (BEW) (BEW_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script BEW: creating free goods (excluded goods) condition records via app VBN2 for sales in SAP S/4HANA Cloud Public Edition 2608. |
| [[08-sales-order-management/criar-condicao-de-bonificacao-em-mercadoria-mds-bew-548\|Criar condição de bonificação em mercadoria – MDS (BEW) (BEW_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud master data script (BEW) for creating free-goods (bonificação em mercadoria) conditions via app VBN2, for the Pricing Specialist. |
| [[08-sales-order-management/mds-bew-549\|创建赠品条件 - MDS (BEW) (BEW_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script BEW for creating free goods conditions in sales via Manage Free Goods - Sales (VBN2) in S/4HANA Cloud 2608. |

### Intercompany Customer Returns

How intercompany customer returns are refunded by credit memo or replaced, with return delivery between company codes.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-intercompany-process-for-customer-returns-2f4-ae-820\|Test Script: Intercompany Process for Customer Returns (2F4_AE) (2F4_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 2F4: intercompany customer returns, refund by credit memo or replacement, with roles, apps and postings. |

### Intercompany Make-to-Order Sales

How an intercompany make-to-order sales order for a configurable product is created and fulfilled across company codes.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-advanced-intercompany-sales-make-to-order-and-variant-conf\|Test Script: Advanced Intercompany Sales – Make-to-Order and Variant Config (7DM_AE) (7DM_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script (7DM_AE): advanced intercompany sales with make-to-order and variant configuration, prerequisites to value chain monitoring. |
| [[08-sales-order-management/intercompany-sales-order-processing-make-to-order-6gc-ae-1166\|Intercompany Sales Order Processing – Make-to-Order (6GC_AE) (6GC_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for scope item 6GC_AE: creating an intercompany make-to-order sales order for a configurable forklifter (UAE/DE). |

### Intercompany Sales Order Processing (Domestic and International)

How domestic and international intercompany sales flow from order to delivery, customer invoice, intercompany IV invoice and AP posting.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/intercompany-sales-order-processing-domestic-1ho-ae-724\|Intercompany Sales Order Processing – Domestic (1HO_AE) (1HO_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1HO_AE: domestic intercompany trading-goods sales order to AP journal entry, UAE sample data. |
| [[08-sales-order-management/intercompany-sales-order-processing-international-1mx-ae-741\|Intercompany Sales Order Processing – International (1MX_AE) (1MX_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for scope item 1MX_AE: intercompany international sales from order through delivery, F2 and IV invoices to AP document (UAE). |
| [[08-sales-order-management/extended-intercompany-processes-for-sales-1wo-ae-test-script-sap-s-4ha\|Extended Intercompany Processes for Sales (1WO_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1WO_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 1WO (AE): intercompany free-of-charge, credit/debit memo, non-stock, sales kits, down payment and consignment, domestic and international. |

### Sales Orders for One-Time Customers

How a sales order for a one-time customer is entered and processed through delivery, goods issue and billing.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-sales-order-entry-with-one-time-customer-bdh-ae-1254\|Test Script: Sales Order Entry with One-Time Customer (BDH_AE) (BDH_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item BDH (AE): sales order with one-time customer through delivery, goods issue and billing. |

### Product, Plant and Storage Location Substitution

How to set up product substitutions and exclusions, plant/storage location substitutions, and the characteristic combinations and access sequences that drive them.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/stammdatenskript-produktsubstitution-anlegen-sds-4vo-418\|Stammdatenskript: Produktsubstitution anlegen – SDS (4VO) (4VO_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud Public Edition master data script (4VO) for creating product substitutions and exclusions via Fiori apps, with optional reason/group/control setup. |
| [[08-sales-order-management/create-product-substitution-mds-4vo-419\|Create Product Substitution - MDS (4VO) (4VO_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (4VO): create product substitution and exclusion, with optional reason, group and control setup. |
| [[08-sales-order-management/creacion-de-sustitucion-de-producto-mds-4vo-420\|Creación de sustitución de producto - MDS (4VO) (4VO_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) master data script 4VO: test steps to create product substitution and product exclusion master data, with optional reason, group and control, in S/4HANA Cloud 2608. |
| [[08-sales-order-management/mds-4vo-421\|製品代替の登録 - MDS (4VO) (マスタデータスクリプト) (4VO_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (4VO) for SAP S/4HANA Cloud Public Edition: creating product substitutions and product exclusions, with substitution reasons, groups and managements. |
| [[08-sales-order-management/script-de-dados-mestre-criar-substituicao-de-produto-mds-4vo-422\|Script de dados mestre - Criar substituição de produto - MDS (4VO) (4VO_S4CLD2608_Master_Data_PT_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (PT) for creating product substitutions and product exclusions, with optional reason, group and control setup. |
| [[08-sales-order-management/mds-4vo-423\|创建产品替代 - MDS (4VO) (4VO_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script for creating product substitutions and exclusions, with optional reason, group and control setup. |
| [[08-sales-order-management/lokationsersetzung-und-ausschluss-anlegen-sds-5ng-472\|Lokationsersetzung und -ausschluss anlegen – SDS (5NG) (5NG_S4CLD2608_Master_Data_DE_XX)]] | German master data script (5NG) for SAP S/4HANA Cloud Public Edition 2608: creating plant and storage location substitutions and exclusions via Fiori apps F5311-F5315. |
| [[08-sales-order-management/master-data-script-create-location-substitution-and-exclusion-mds-5ng\|Master Data Script: Create Location Substitution and Exclusion - MDS (5NG) (5NG_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data test script (5NG) for creating plant and storage location substitution and exclusion records in Fiori. |
| [[08-sales-order-management/script-de-datos-maestros-crear-sustitucion-y-exclusion-de-ubicacion-md\|Script de datos maestros - Crear sustitución y exclusión de ubicación - MDS (5NG) (5NG_S4CLD2608_Master_Data_ES_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script (ES, machine-translated) for creating plant and storage location substitutions and exclusions via Fiori apps. |
| [[08-sales-order-management/mds-5ng-475\|マスタデータスクリプト: ロケーション代替および除外の登録 - MDS (5NG) (5NG_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (5NG) for SAP S/4HANA Cloud Public Edition: registering plant and storage location substitutions and exclusions via Fiori apps. |
| [[08-sales-order-management/script-de-dados-mestre-criar-substituicao-e-exclusao-de-local-mds-5ng\|Script de dados mestre - Criar substituição e exclusão de local (MDS 5NG) (5NG_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (5NG): test steps to create plant and storage location substitutions and exclusions via Fiori apps. |
| [[08-sales-order-management/mds-5ng-477\|主数据脚本 - 创建位置替代和排除 - MDS (5NG) (5NG_S4CLD2608_Master_Data_ZH_XX)]] | Chinese machine-translated SAP S/4HANA Cloud master data script (5NG) for creating plant and storage location substitutions and exclusions in Fiori apps. |
| [[08-sales-order-management/objekt-und-wertermittlung-anlegen-sds-5nh-478\|Objekt- und Wertermittlung anlegen – SDS (5NH) (5NH_S4CLD2608_Master_Data_DE_XX)]] | German master data script 5NH: test steps to create characteristic combinations and access sequences for substitution (product/plant/storage location) in S/4HANA Cloud Public Edition 2608. |
| [[08-sales-order-management/create-object-and-value-determination-mds-5nh-479\|Create Object and Value Determination - MDS (5NH) (5NH_S4CLD2608_Master_Data_EN_XX)]] | Master data test script (5NH) for substitution controls, characteristic combinations and access sequences used for product/plant/storage location substitution with AATP ABC in S/4HANA Cloud 2608. |
| [[08-sales-order-management/crear-determinacion-de-objeto-y-valor-mds-5nh-480\|Crear determinación de objeto y valor - MDS (5NH) (5NH_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud 2608 master data script 5NH: create substitution controls, characteristic combination and access for object and value determination. |
| [[08-sales-order-management/mds-5nh-481\|マスタデータスクリプト: オブジェクトおよび値決定 - MDS (5NH) (5NH_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data/test script (5NH) for substitution: characteristic combinations (F5303), searches (F5302) and optional product/plant/storage location controls in S/4HANA Cloud 2608. |
| [[08-sales-order-management/criar-determinacao-de-objeto-e-valor-mds-5nh-482\|Criar determinação de objeto e valor - MDS (5NH) (5NH_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (5NH) for SAP S/4HANA Cloud Public Edition: create characteristic combinations, accesses and substitution controls for product/plant/warehouse substitution in AATP. |
| [[08-sales-order-management/5nh-483\|主数据脚本: 创建对象和值确定 (5NH) (5NH_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud master data script for creating characteristic combinations and accesses for substitution control (product/plant/ |

### Sale of Services

How a service sales order is created and billed without delivery, with e-invoicing submission.

| Node | Description |
| --- | --- |
| [[04-tax-and-statutory-reporting/sale-of-services-2eq-ae-test-script-sap-s-4hana-cloud-public-edition-8\|Sale of Services (2EQ_AE) Test Script - SAP S/4HANA Cloud Public Edition (2EQ_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 2EQ_AE Sale of Services (UAE): prerequisites, PEPPOL e-invoicing setup, sales order to billing, eDocument Cockpit, billing jobs. |

### Sales Inquiries

How to create, change and reject sales inquiries in Manage Sales Inquiries (F2370).

| Node | Description |
| --- | --- |
| [[08-sales-order-management/sales-inquiry-1iq-ae-test-script-726\|Sales Inquiry (1IQ_AE) Test Script (1IQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1IQ (AE): create, change and reject a sales inquiry in Manage Sales Inquiries (F2370). |

### Sales Kits with Variant Configuration and Their Returns

How configurable sales kit (SET) orders are created and how sales kit returns are received, inspected and refunded.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-make-to-order-production-for-sales-kits-with-variant-confi\|Test Script: Make-to-Order Production for Sales Kits with Variant Configuration (4OC_AE) (4OC_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (4OC_AE, 19-06-26) for creating a sales order for a configurable robot bundle SET material, with prerequisites and succeeding processes. |
| [[08-sales-order-management/customer-returns-for-sales-kits-5cx-ae-test-script-sap-s-4hana-cloud-p\|Customer Returns for Sales Kits (5CX_AE) - Test Script, SAP S/4HANA Cloud Public Edition (5CX_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (5CX_AE, UAE) for customer returns of sales kits: returns order, goods receipt, inspection, refund by credit memo or replacement. |
| [[08-sales-order-management/test-script-sales-order-processing-for-sales-kits-31q-ae-896\|Test Script: Sales Order Processing for Sales Kits (31Q_AE) (31Q_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud test script (scope item 31Q_AE, UAE): sales kit BOMs ERLA, LUMF, CPFH, DISH from sales order through delivery, picking, goods issue and billing. |

### Sales Order Automation and Creation from Unstructured Data

How AI recommendations complete sales orders and returns, and how sales orders are extracted from PDF purchase orders.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-create-sales-orders-from-unstructured-data-4x9-ae-sap-s-4h\|Test Script: Create Sales Orders from Unstructured Data (4X9_AE) - SAP S/4HANA Cloud Public Edition (4X9_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4X9 (AE): creating sales orders by automatic extraction from PDF purchase orders, with optional setup steps. |
| [[08-sales-order-management/sales-order-automation-73p-ae-test-script-1203\|Sales Order Automation (73P_AE) Test Script (73P_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 73P: AI recommendations for sales order completion and customer returns, incl. Turnkey model training. |

### Sales Order Scheduling with Business Process Scheduling

How Business Process Scheduling is activated for sales documents and calculates material availability and delivery dates.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-basic-business-process-scheduling-6jm-ae-1173\|Test Script: Basic Business Process Scheduling (6JM_AE) (6JM_S4CLD2608_BPD_EN_AE)]] | Test script (UAE/AE) for scope item 6JM, Basic Business Process Scheduling in SAP S/4HANA Cloud Public Edition 2608: activation config and sales order scheduling with days granularity. |

### Sales Planning and Sales Performance

How sales plans are maintained in Manage Sales Plans (F2512) and plan/actual sales performance analyzed (F2941).

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-planning-apps-for-sales-1o0-750\|Test Script: Planning Apps for Sales (1O0) (1O0_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1O0: Manage Sales Plans (F2512) and Sales Performance - Plan/Actual (F2941) as Sales Manager. |

### Sales Price Conditions and Statistical Conditions

How to maintain sales price condition records (PPR0) in VK12 and how statistical conditions like cash discount post to extension ledgers.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/verkaufspreiskondition-anlegen-sds-bet-538\|Verkaufspreiskondition anlegen – SDS (BET) (BET_S4CLD2608_Master_Data_DE_XX)]] | German sales data script BET: create sales price condition (PPR0) for material TG11 via Materialpreise festlegen – Verkauf (VK12) as Preisfindungssachbearbeiter |
| [[08-sales-order-management/create-sales-pricing-condition-mds-bet-539\|Create Sales Pricing Condition - MDS (BET) (BET_S4CLD2608_Master_Data_EN_XX)]] | English SAP master data script (BET, 2608): create a sales pricing condition (e.g. PPR0) with Set Material Prices - Sales (VK12) as Pricing Specialist. |
| [[08-sales-order-management/script-de-datos-maestros-crear-condicion-de-determinacion-de-precio-de\|Script de datos maestros: Crear condición de determinación de precio de venta - MDS (BET) (BET_S4CLD2608_Master_Data_ES_XX)]] | Spanish master data script (BET) for creating sales price conditions (e.g. PPR0) in SAP S/4HANA Cloud Public Edition using app VK12. |
| [[08-sales-order-management/mds-bet-541\|販売価格設定条件の登録 - MDS (BET) (BET_S4CLD2608_Master_Data_JA_XX)]] | マスタデータスクリプト（日本語）：VK12 で販売価格設定条件（PPR0 など）を登録する手順。 |
| [[08-sales-order-management/script-de-dados-mestre-criar-condicao-de-determinacao-de-preco-de-vend\|Script de dados mestre: Criar condição de determinação de preço de venda (BET) (BET_S4CLD2608_Master_Data_PT_XX)]] | Portuguese SAP S/4HANA Cloud master data script for creating sales pricing conditions (e.g. PPR0) with transaction VK12 for a pricing specialist. |
| [[08-sales-order-management/mds-bet-543\|创建销售定价条件 - MDS (BET) (BET_S4CLD2608_Master_Data_ZH_XX)]] | Master data script (Chinese, machine-translated) for creating sales pricing conditions (e.g. PPR0) with Set Material Prices - Sales (VK12). |
| [[08-sales-order-management/statistical-sales-conditions-34b-ae-test-script-906\|Statistical Sales Conditions (34B_AE) - Test Script (34B_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 34B (AE): statistical sales conditions such as cash discount posted to extension ledger 0C. |

### Sell from Stock with Valuated Stock in Transit

How a sell-from-stock order with valuated stock in transit flows from sales order through goods issue, transit and billing.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-sell-from-stock-with-valuated-stock-in-transit-5mq-ae-1109\|Test Script: Sell from Stock with Valuated Stock in Transit (5MQ_AE) (5MQ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item 5MQ: sell from stock with valuated stock in transit, from sales order to billing, with job alternatives. |

### Third-Party Sales Processing

How third-party sales orders create purchase requisitions/POs, with or without shipping notification, statistical goods receipt and billing, including variant configuration.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/sales-processing-using-third-party-with-variant-configuration-4r6-ae-1\|Sales Processing using Third-Party with Variant Configuration (4R6_AE) (4R6_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 4R6: third-party sales order with variant-configurable material, prerequisites, preliminary steps and follow-ups. |
| [[08-sales-order-management/sales-processing-using-third-party-with-shipping-notification-bd3-ae-t\|Sales Processing using Third-Party with Shipping Notification (BD3_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BD3_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item BD3 (AE): third-party sales order, purchase requisition/PO, statistical goods receipt, billing and supplier invoice, with prerequisites and appendix. |
| [[08-sales-order-management/sales-processing-using-third-party-without-shipping-notification-bdk-a\|Sales Processing Using Third-Party Without Shipping Notification (BDK_AE) - Test Script (BDK_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item BDK: third-party sales order, requisition, PO, supplier invoice and billing, with roles and steps. |

### Sell from Stock Order-to-Cash

How a standard sales order from stock flows through outbound delivery, picking, goods issue and billing, incl. preliminary billing and invoice before goods issue.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-sell-from-stock-consumer-products-5hl-ae-sap-s-4hana-cloud\|Test Script: Sell from Stock – Consumer Products (5HL_AE), SAP S/4HANA Cloud Public Edition (5HL_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 5HL_AE: sell from stock and from valuated stock in transit, order to invoice list, with roles, apps, test data and postings. |
| [[08-sales-order-management/sell-from-stock-with-invoice-creation-before-goods-issue-7ua-ae-test-s\|Sell from Stock with Invoice Creation Before Goods Issue (7UA_AE) - Test Script (7UA_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 7UA_AE: sell from stock, invoice created before goods issue; prerequisites and test steps. |
| [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-sell-from-stock-bd9-ae-12\|Test Script SAP S/4HANA Cloud Public Edition - Sell from Stock (BD9_AE) (BD9_S4CLD2608_BPD_EN_AE)]] | SAP test script (2608, UAE/AE) for scope item BD9 Sell from Stock: prerequisites, sales order to billing and PEPPOL eDocument test steps, approvals, jobs. |

### Invoice Lists, Collective Billing and Self-Billing

How billing documents are combined into invoice lists for a central payer or collective billing, and how customer self-billing is transmitted, simulated and executed.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/self-billing-4h2-ae-test-script-sap-s-4hana-cloud-public-edition-1028\|Self-Billing (4H2_AE) Test Script - SAP S/4HANA Cloud Public Edition (4H2_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 4H2_AE Self-Billing (UAE): prerequisites, tolerance and sender setup, API transmission, simulation and execution of self-billing. |
| [[08-sales-order-management/test-script-sales-order-processing-with-invoice-list-and-collective-bi\|Test Script: Sales Order Processing with Invoice List and Collective Billing (BKZ_AE) (BKZ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 (AE) test script: order-to-invoice with invoice lists to a central payer and collective billing, covering apps, roles and postings. |

### Customer Returns and Refunds

How customer returns orders flow through return delivery, inspection and refund by credit memo or replacement, incl. returns shipped to or exchanged with the supplier.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s\|Customer Returns Management – Consumer Products (61V_AE) – Test Script, SAP S/4HANA Cloud Public Edition (61V_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 61V_AE (Customer Returns, Consumer Products): roles, master data and test steps from returns order to refund and credit memo. |
| [[08-sales-order-management/test-script-lean-customer-returns-bdd-ae-sap-s-4hana-cloud-public-edit\|Test Script: Lean Customer Returns (BDD_AE) - SAP S/4HANA Cloud Public Edition (BDD_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script (2608, AE country version) for scope item BDD Lean Customer Returns: returns order to credit memo steps, roles, data, limitations, jobs. |
| [[08-sales-order-management/customer-returns-bkp-ae-test-script-sap-s-4hana-cloud-public-edition-1\|Customer Returns (BKP_AE) Test Script, SAP S/4HANA Cloud Public Edition (BKP_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script for scope item BKP (Customer Returns, AE localization, 2608): prerequisites, roles, three return scenarios, refunds, appendix jobs. |
| [[08-sales-order-management/test-script-customer-returns-with-direct-shipment-from-customer-to-sup\|Test Script: Customer Returns with Direct Shipment from Customer to Supplier (1Z3_AE) (1Z3_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script (1Z3_AE): customer return shipped directly to supplier, supplier credit memo, refund by credit memo or replacement. |
| [[08-sales-order-management/test-script-customer-returns-involving-supplier-by-message-exchange-3q\|Test Script: Customer Returns Involving Supplier by Message Exchange (3QD_AE) - SAP S/4HANA Cloud Public Edition (3QD_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud 2608 test script for scope item 3QD (AE): seller-supplier returns via EDI RMA, refund by credit memo or replacement, with test steps. |
| [[08-sales-order-management/customer-returns-for-non-stock-and-service-materials-3te-ae-test-scrip\|Customer Returns for Non-Stock and Service Materials (3TE_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3TE_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script 3TE_AE: returns order, goods receipt, refund determination, credit memo or replacement delivery for non-stock/service materials. |

### Sales Quotations

How sales quotations are created, sent through an optional approval workflow with approval reasons, changed, approved or rejected.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-sales-quotation-bdg-ae-sap-s-4hana-cloud-public-edition-26\|Test Script: Sales Quotation (BDG_AE) - SAP S/4HANA Cloud Public Edition 2608 (BDG_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script (AE) for Sales Quotation: roles, sample data, optional approval-workflow setup, and create/approve/change/reject steps. |

### Sales Contracts and Customer Down Payments

How quantity and value sales contracts and price agreements are processed, and how down payment requests and milestone billing plans collect customer prepayments.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-sales-order-processing-with-customer-down-payment-bkj-ae-1\|Test Script: Sales Order Processing with Customer Down Payment (BKJ_AE) (BKJ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (BKJ_AE, UAE) for sales order processing with customer down payment, with PEPPOL e-invoicing prerequisites. |
| [[08-sales-order-management/test-script-sales-contract-management-i9i-ae-sap-s-4hana-cloud-public\|Test Script: Sales Contract Management (I9I_AE) - SAP S/4HANA Cloud Public Edition (I9I_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script, scope item I9I_AE (UAE): quantity/value sales contracts, contract down payments and price agreements. |

### Sales Order Fulfillment Monitoring and Sales Analytics

How incomplete, duplicate or blocked sales documents are tracked and mass-changed, and which analytical apps show quotations, orders, returns and sales volume.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-sales-order-fulfillment-monitoring-and-operations-bkk-ae-1\|Test Script: Sales Order Fulfillment Monitoring and Operations (BKK_AE) (BKK_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (BKK_AE) for sales order fulfillment monitoring: mass change, incomplete/duplicate docs, delivery, billing. |
| [[08-sales-order-management/test-script-sap-fiori-analytical-apps-for-sales-1bs-sap-s-4hana-cloud\|Test Script: SAP Fiori Analytical Apps for Sales (1BS) - SAP S/4HANA Cloud Public Edition (1BS_S4CLD2608_BPD_EN_XX)]] | Test script for SAP scope item 1BS: Fiori test procedures for 18 sales analytical apps (overviews, quotations, orders, returns, sales volume, O2C). |

### Sales of Non-Stock Materials

How sales orders for non-stock items are fulfilled, with or without order-specific purchase orders, through goods receipt, delivery, proof of delivery and billing.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-sales-of-non-stock-item-with-order-specific-procurement-bd\|Test Script: Sales of Non-Stock Item with Order-Specific Procurement (BDN_AE) - SAP S/4HANA Cloud Public Edition (BDN_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item BDN_AE (UAE): sales order, purchase order, goods receipt, delivery, billing and supplier invoice steps, with test data. |
| [[08-sales-order-management/sales-order-processing-for-non-stock-material-2et-ae-test-script-818\|Sales Order Processing for Non-Stock Material (2ET_AE) - Test Script (2ET_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition 2608 UAE test script for scope item 2ET: non-stock sales order through delivery, goods issue, POD and billing. |

### Sales Scheduling Agreements and JIT Supply to Customer

How sales scheduling agreements with forecast and JIT delivery schedules, summarized and sequenced JIT calls and JIT delivery confirmation supply customers.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-just-in-time-supply-to-customer-with-delivery-confirmation\|Test Script: Just-In-Time Supply to Customer with Delivery Confirmation (53X_AE) (53X_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 53X: sequenced JIT calls, JIT delivery confirmation, goods issue and invoicing, with master data and roles. |
| [[08-sales-order-management/automotive-supply-to-customer-inventory-management-55f-ae-test-script\|Automotive Supply to Customer – Inventory Management (55F_AE) Test Script (55F_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 AE test script for scope item 55F: automotive supply to customer with sales scheduling agreements, JIT calls, consignment, billing and payments. |
| [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-just-in-time-supply-to-cu\|Test Script SAP S/4HANA Cloud Public Edition - Just-In-Time Supply to Customer (2EM_AE) (2EM_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 2EM (AE, release 2608): JIT supply to customer, summarized and sequenced JIT calls, from stock or production, through delivery and billing. |
| [[08-sales-order-management/test-script-sales-scheduling-agreements-3nr-ae-sap-s-4hana-cloud-publi\|Test Script: Sales Scheduling Agreements (3NR_AE) - SAP S/4HANA Cloud Public Edition (3NR_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3NR_AE (UAE): sales scheduling agreement through delivery, goods issue, billing and EDI messages. |

### Customer Consignment

How consignment stock at the customer is filled up, issued, picked up and returned, via sales orders or consignment scheduling agreements.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-sales-scheduling-agreement-with-consignment-4lz-ae-sap-s-4\|Test Script: Sales Scheduling Agreement with Consignment (4LZ_AE) - SAP S/4HANA Cloud Public Edition (4LZ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for scope item 4LZ_AE: consignment scheduling agreements, fill-up, issue, pick-up, return, corrections, EDI checks. |
| [[08-sales-order-management/test-script-customer-consignment-1iu-ae-sap-s-4hana-cloud-public-editi\|Test Script: Customer Consignment (1IU_AE) - SAP S/4HANA Cloud Public Edition 2608 (1IU_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for Customer Consignment (1IU_AE): fill-up, issue, pick-up, return, with roles, sample data and postings. |

### Rebates, Commissions and Royalties Settlement

How condition contracts accrue and settle sales rebates, sales commissions and royalties via settlement runs, process variants, workflow and Vistex margin optimization.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/royalties-settlement-for-sales-55i-ae-test-script-sap-s-4hana-cloud-pu\|Royalties Settlement for Sales (55I_AE) - Test Script, SAP S/4HANA Cloud Public Edition (55I_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 55I (AE, 2608): configuring and testing royalties settlement with condition contracts, process variants, workflow, intercompany and subscription cases. |
| [[08-sales-order-management/test-script-condition-contract-with-customer-hierarchy-consumer-produc\|Test Script: Condition Contract with Customer Hierarchy – Consumer Products (6V0_AE) (6V0_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 6V0_AE: sell from stock, then rebate condition contracts on a customer hierarchy and final settlement. |
| [[08-sales-order-management/margin-optimization-sap-solution-extensions-by-vistex-7uq-test-script\|Margin Optimization – SAP Solution Extensions by Vistex (7UQ) – Test Script (7UQ_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 7UQ: integrating SAP margin optimization solutions by Vistex with S/4HANA Cloud Public Edition; prerequisites, preliminary steps, 11 test procedures. |
| [[08-sales-order-management/sales-rebate-processing-1b6-ae-test-script-sap-s-4hana-cloud-public-ed\|Sales Rebate Processing (1B6_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1B6_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 1B6 (UAE) Sales Rebate Processing: condition contracts, process variants, settlement runs, workflow, fixed amounts, reversals; release 2608. |
| [[08-sales-order-management/test-script-sales-commissions-external-sales-representative-2tt-ae-863\|Test Script: Sales Commissions – External Sales Representative (2TT_AE) (2TT_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for external sales commission settlement via condition contracts: prerequisites, variants, workflow, settlement steps. |
| [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-internal-commissions-sett\|Test Script SAP S/4HANA Cloud Public Edition - Internal Commissions Settlement for Sales (3TD_AE) (3TD_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 3TD (AE): internal sales commissions settlement via workforce condition contracts or SuccessFactors Incentive Management, with prerequisites and payroll follow-up. |

### Returnable Packaging and Pallets

How returnable packaging and pallets are shipped and returned, tracked in returnable packaging accounts for customers and suppliers, and billed when not returned.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-sap-returnable-packaging-management-7ho-ae-1215\|Test Script: SAP Returnable Packaging Management (7HO_AE) (7HO_S4CLD2608_BPD_EN_AE)]] | Test script for SAP S/4HANA Cloud scope item 7HO (SAP Returnable Packaging Management, AE): customer and supplier returnable packaging prerequisites and steps. |
| [[08-sales-order-management/test-script-returnables-processing-bdw-ae-sap-s-4hana-cloud-public-edi\|Test Script: Returnables Processing (BDW_AE) - SAP S/4HANA Cloud Public Edition (BDW_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item BDW: shipping pallets, pallet returns and billing of unreturned pallets, with roles and data. |

### B2B Sales Integration with Buyers and SAP Business Network

How sales orders, order confirmations, ASNs, deliveries and invoices are exchanged automatically with external buyers via SOAP APIs or SAP Business Network.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4\|Test Script: Automation of Order-to-Invoice with SAP Business Network (4A1_AE) - SAP S/4HANA Cloud Public Edition (4A1_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script (scope item 4A1, UAE) for supplier-side order-to-invoice with SAP Business Network: prerequisites, setup, 14 test steps. |
| [[08-sales-order-management/integration-of-sales-with-external-buyers-2el-ae-test-script-sap-s-4ha\|Integration of Sales with External Buyers (2EL_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2EL_S4CLD2608_BPD_EN_AE)]] | Test script for SAP scope item 2EL_AE: automated sales order, delivery, billing and returns exchange with external buyers via SOAP APIs. |

## Related categories
- related-to :: [[02-business-partner-and-product-master-data/_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/_cluster]]
