---
title: Procurement
description: "Purchase requisitions and purchase orders through goods receipt, info records, scheduling agreements, RFQs and sourcing, consignment, ERS, supplier evaluation, returns, Ariba and Fieldglass."
cluster: 10-procurement
type: cluster
tags: [kb/procurement, kb/hub]
keywords: [purchase requisition, purchase order, goods receipt, purchasing, info record, scheduling agreement, RFQ, sourcing, consignment, ERS, supplier evaluation, SAP Ariba, guided buying, Fieldglass, pipeline]
node_count: 65
created: 2026-10-12
updated: 2026-10-12
---

# Procurement

Covers source-to-pay purchasing documents and integrations. Excludes supplier master records (see 02), supplier invoice accounting and payment (see 03), quality info records (see 13), retail consignment (see 15) and HQ-subsidiary purchasing (see 16).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### SAP Ariba Buying Purchase Requests

How SAP Ariba Buying (incl. Base Edition and Procurement Expansion Package) processes purchase requests to PO, goods receipt and supplier invoice.

| Node | Description |
| --- | --- |
| [[10-procurement/sap-ariba-buying-4ai-1009\|SAP Ariba Buying (4AI) (4AI_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 4AI, SAP Ariba Buying: purchase request through approval, purchase order, goods receipt and supplier invoice. |
| [[10-procurement/sap-ariba-buying-base-edition-7ym-test-script-1237\|SAP Ariba Buying Base Edition (7YM) Test Script (7YM_S4CLD2608_BPD_EN_XX)]] | Test script for SAP Ariba Buying Base Edition (7YM) on S/4HANA Cloud Public Edition: purchase request to PO, goods receipt and supplier invoice test steps. |
| [[10-procurement/test-script-sap-ariba-buying-procurement-expansion-package-81y-1244\|Test Script: SAP Ariba Buying Procurement Expansion Package (81Y) (81Y_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 81Y: SAP Ariba Buying purchase request through PO, goods receipt and supplier invoice in S/4HANA Cloud Public Edition 2608. |

### Contracts with SAP Ariba Contracts

How contracts and scheduling agreements, including central purchase contracts, are created in SAP Ariba Contracts and reviewed in S/4HANA.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-contract-management-with-sap-ariba-contracts-4az-ae-1014\|Test Script: Contract Management with SAP Ariba Contracts (4AZ_AE) (4AZ_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script (scope item 4AZ) for creating contracts or scheduling agreements in SAP Ariba Contracts and reviewing them in S/4HANA. |
| [[10-procurement/contract-for-central-procurement-with-sap-ariba-contracts-4b0-test-scr\|Contract for Central Procurement with SAP Ariba Contracts (4B0) - Test Script (4B0_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 4B0: creating, reviewing and updating central purchase contracts in SAP Ariba Contracts and creating a sourcing project, with S/4HANA Cloud Public Edition. |

### Guided Buying with SAP Ariba Buying

How guided buying in SAP Ariba Buying turns shopping carts into PRs and POs in S/4HANA, including central procurement.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-guided-buying-capability-with-sap-ariba-buying-2nv-ae-836\|Test Script: Guided Buying Capability with SAP Ariba Buying (2NV_AE) (2NV_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 2NV (AE): guided buying with SAP Ariba Buying, from shopping cart to PR, PO, GR/SES and supplier invoice. |
| [[10-procurement/test-script-guided-buying-for-central-procurement-with-sap-ariba-buyin\|Test Script: Guided Buying for Central Procurement with SAP Ariba Buying (3EN) (3EN_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3EN: Guided Buying with SAP Ariba Buying and Central Procurement, from shopping cart to supplier invoice. |

### Invoice Processing with SAP Ariba Invoicing

How supplier invoices from SAP Ariba Invoicing are uploaded, auto-posted or processed manually.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-invoice-processing-with-sap-ariba-invoicing-4n6-1038\|Test Script: Invoice Processing with SAP Ariba Invoicing (4N6) (4N6_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 4N6: upload, view, auto-post and manually process supplier invoices via SAP Ariba Invoicing. |
| [[10-procurement/test-script-invoice-processing-with-sap-ariba-invoicing-7yh-1236\|Test Script: Invoice Processing with SAP Ariba Invoicing (7YH) (7YH_S4CLD2608_BPD_EN_XX)]] | SAP test script for scope item 7YH: step-by-step tests for supplier invoice upload, posting, approval and import with SAP Ariba Invoicing and S/4HANA Cloud. |

### Central Sourcing and Central Procurement

How central RFQs, supplier quotations and awards create central contracts or purchase orders in connected systems.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-automation-of-central-procurement-quote-with-sap-business\|Test Script: Automation of Central Procurement Quote with SAP Business Network (5JT) (5JT_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script 5JT: central RFQ via SAP Business Network, supplier quote, award, follow-on PO, supplier quick enablement. |
| [[10-procurement/test-script-central-sourcing-3zf-sap-s-4hana-cloud-public-edition-990\|Test Script: Central Sourcing (3ZF) - SAP S/4HANA Cloud Public Edition (3ZF_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 3ZF Central Sourcing: central RFQ, supplier quotation, award, central contract or PO follow-ons. |

### Complementary Procurement for Operating Supplies, Batches and Serial Numbers

How operating supplies and batch- or serial-number-managed materials are purchased, received and invoiced.

| Node | Description |
| --- | --- |
| [[10-procurement/complementary-procurement-functions-2tw-ae-test-script-sap-s-4hana-clo\|Complementary Procurement Functions (2TW_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2TW_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 2TW_AE: procuring operating supplies, batch- and serial-number-managed materials (PO, goods receipt, supplier invoice), UAE plant 3310. |

### Automated Invoice Settlement (ERS)

How evaluated receipt settlement creates supplier invoices automatically from goods receipts.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-automated-invoice-settlement-2lh-ae-831\|Test Script: Automated Invoice Settlement (2LH_AE) (2LH_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2LH Automated Invoice Settlement (ERS), UAE (AE) baseline: prerequisites, PO-to-ERS test steps. |

### Procurement of Pipeline Materials

How pipeline withdrawals are posted and settled via pipeline settlement or scheduled supplier invoices.

| Node | Description |
| --- | --- |
| [[10-procurement/procurement-of-pipeline-materials-41f-ae-993\|Procurement of Pipeline Materials (41F_AE) (41F_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for scope item 41F_AE: pipeline info record, consumption posting and pipeline settlement or scheduled supplier invoice jobs. |

### Procurement of Variant-Configured Materials

How variant-configured materials are purchased: configurable PO through goods receipt and supplier invoice.

| Node | Description |
| --- | --- |
| [[10-procurement/procurement-of-materials-with-variant-configuration-2xu-ae-test-script\|Procurement of Materials with Variant Configuration (2XU_AE) - Test Script (2XU_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (scope item 2XU, UAE) for procuring variant-configured materials: prerequisites, PO to goods receipt to supplier invoice. |

### Supplier Classification and Purchasing Categories

How purchasing categories are created and managed to classify and segment suppliers.

| Node | Description |
| --- | --- |
| [[10-procurement/supplier-classification-and-segmentation-19e-ae-test-script-706\|Supplier Classification and Segmentation (19E_AE) – Test Script (19E_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 19E_AE: creating and managing purchasing categories in app F0337 as Purchaser. |

### Purchasing Info Records

How to create and mass-change purchasing info records for standard, consignment, subcontracting and pipeline procurement.

| Node | Description |
| --- | --- |
| [[10-procurement/einkaufsinfosatz-anlegen-sds-bhd-stammdatenskript-562\|Einkaufsinfosatz anlegen – SDS (BHD) Stammdatenskript (BHD_S4CLD2608_Master_Data_DE_XX)]] | German SAP S/4HANA Cloud master data script for creating purchasing info records (standard, consignment, subcontracting, pipeline) and mass changes. |
| [[10-procurement/create-purchasing-info-record-mds-bhd-master-data-script-563\|Create Purchasing Info Record - MDS (BHD) Master Data Script (BHD_S4CLD2608_Master_Data_EN_XX)]] | Master data script for creating and mass-changing purchasing info records (standard, consignment, subcontracting, pipeline) in S/4HANA Cloud Public Edition. |
| [[10-procurement/script-de-datos-maestros-creacion-de-registro-info-de-compras-mds-bhd\|Script de datos maestros - Creación de registro info de compras - MDS (BHD) (BHD_S4CLD2608_Master_Data_ES_XX)]] | Spanish SAP S/4HANA Cloud Public Edition 2608 master data script: test procedures to create and mass-change purchasing info records (BHD). |
| [[10-procurement/mds-bhd-565\|購買情報の登録 - MDS (BHD) (BHD_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data script (BHD) for creating and mass-changing purchasing info records (standard, consignment, subcontracting, pipeline) in SAP S/4HANA Cloud Public Edition. |
| [[10-procurement/criar-registro-info-para-compras-mds-bhd-566\|Criar registro info para compras – MDS (BHD) (BHD_S4CLD2608_Master_Data_PT_XX)]] | Script de dados mestre (PT) do SAP S/4HANA Cloud Public Edition 2608: testes para criar e modificar registros info para compras, incl. consignação, subcontratação, pipeline e massa. |
| [[10-procurement/mds-bhd-567\|创建采购信息记录 - MDS (BHD) (BHD_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) SAP S/4HANA Cloud Public 2608 master data script BHD: creating purchasing info records (standard, consignment, subcontracting, pipeline) and mass changes. |

### Request for Price and Quotation Comparison

How RFQs are created and sent, supplier quotations compared and awarded, and contracts or POs created as follow-on.

| Node | Description |
| --- | --- |
| [[10-procurement/request-for-quotation-customer-specification-en-de-255\|Request for Quotation (Customer Specification EN/DE) (Customer_Specification_EN_DE)]] | Bilingual (English/German) blank Request for Quotation letter template with product description, quantity and technical detail fields, signed by Purchase/Einkauf. |
| [[10-procurement/test-script-request-for-price-1xf-ae-780\|Test Script - Request for Price (1XF_AE) (1XF_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud 2608 test script for scope item 1XF_AE (UAE): RFQ creation, supplier quotations, award, purchase contract follow-on, low-quotation situation handling. |

### Return to Supplier

How defective or excess stock is returned to the supplier with return POs, return deliveries and credit memos.

| Node | Description |
| --- | --- |
| [[10-procurement/return-to-supplier-bmk-ae-test-script-sap-s-4hana-cloud-public-edition\|Return to Supplier (BMK_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BMK_S4CLD2608_BPD_EN_AE)]] | SAP test script for the Return to Supplier scope item (BMK_AE, UAE): prerequisites, roles, master data and step-by-step Fiori tests for advanced and basic returns to a supplier. |

### Purchase Scheduling Agreements

How to create standard, consignment and subcontracting scheduling agreements in Manage Scheduling Agreements (F2179).

| Node | Description |
| --- | --- |
| [[10-procurement/scheduling-agreements-in-procurement-bmr-ae-test-script-sap-s-4hana-cl\|Scheduling Agreements in Procurement (BMR_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BMR_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scheduling agreements in procurement: prerequisites, three test cases, Fiori apps, roles, sample data. |
| [[10-procurement/stammdatenskript-lieferplan-anlegen-sds-bf6-556\|Stammdatenskript: Lieferplan anlegen – SDS (BF6) (BF6_S4CLD2608_Master_Data_DE_XX)]] | German master data script (BF6) for SAP S/4HANA Cloud Public Edition 2608: creating scheduling agreements (Lieferplan) for standard, consignment and subcontracting procurement. |
| [[10-procurement/master-data-script-create-scheduling-agreement-mds-bf6-557\|Master Data Script: Create Scheduling Agreement - MDS (BF6) (BF6_S4CLD2608_Master_Data_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 master data script for creating purchase scheduling agreements (standard, consigned, subcontracting) in Fiori app F2179. |
| [[10-procurement/script-de-datos-maestros-creacion-de-plan-de-entregas-mds-bf6-558\|Script de datos maestros - Creación de plan de entregas - MDS (BF6) (BF6_S4CLD2608_Master_Data_ES_XX)]] | Spanish (machine-translated) SAP S/4HANA Cloud Public Edition master data script BF6: prerequisites and test steps to create purchasing scheduling agreements (plan de entregas). |
| [[10-procurement/mds-bf6-559\|マスタデータスクリプト: 分納契約の登録 - MDS (BF6) (BF6_S4CLD2608_Master_Data_JA_XX)]] | Japanese master data/test script (BF6) for creating scheduling agreements (分納契約) in SAP S/4HANA Cloud Public Edition 2608 via app F2179: standard, consignment, subcontracting. |
| [[10-procurement/script-de-dados-mestre-criar-programa-de-remessas-mds-bf6-560\|Script de dados mestre - Criar programa de remessas – MDS (BF6) (BF6_S4CLD2608_Master_Data_PT_XX)]] | Portuguese master data script (BF6) for SAP S/4HANA Cloud Public Edition: creating scheduling agreements (programas de remessas) for standard, consignment and subcontracting procurement. |
| [[10-procurement/mds-bf6-561\|主数据脚本: 创建计划协议 - MDS (BF6) (BF6_S4CLD2608_Master_Data_ZH_XX)]] | Chinese (machine-translated) master data script BF6 for creating scheduling agreements (standard, consignment, subcontracting) via app F2179 in SAP S/4HANA Cloud Public. |
| [[10-procurement/test-script-scheduling-agreement-for-subcontracting-procurement-2nx-ae\|Test Script: Scheduling Agreement for Subcontracting Procurement (2NX_AE) - SAP S/4HANA Cloud Public Edition (2NX_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud 2608 (AE) test script, scope item 2NX: subcontracting scheduling agreements, with and without serial numbers, from creation to supplier invoice. |
| [[10-procurement/test-script-scheduling-agreement-for-consignment-procurement-2ny-ae-sa\|Test Script: Scheduling Agreement for Consignment Procurement (2NY_AE) - SAP S/4HANA Cloud Public Edition (2NY_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 2NY (AE): consignment scheduling agreement from requisition to settlement, with roles, apps and sample data. |

### Service Procurement with SAP Fieldglass and Business Network

How service POs, Fieldglass statements of work, service entry sheets and Business Network invoices integrate.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-service-procurement-with-sap-business-network-and-sap-fiel\|Test Script: Service Procurement with SAP Business Network and SAP Fieldglass (4R2) (4R2_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4R2: service PO, Fieldglass SOW/events, service entry sheet, Business Network invoice, payment. |
| [[10-procurement/external-workforce-procurement-via-sap-fieldglass-22k-test-script-sap\|External Workforce Procurement via SAP Fieldglass (22K) - Test Script, SAP S/4HANA Cloud Public Edition (22K_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 22K: SAP Fieldglass to S/4HANA Cloud Public Edition integration for work orders, statements of work, time sheets, invoices, ERS; dated 19-06-26. |

### Supplier Consignment

How consignment info records, POs, goods receipt, withdrawal and consignment settlement work.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-scheduling-agreement-for-consignment-procurement-2ny-ae-sa\|Test Script: Scheduling Agreement for Consignment Procurement (2NY_AE) - SAP S/4HANA Cloud Public Edition (2NY_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud test script for scope item 2NY (AE): consignment scheduling agreement from requisition to settlement, with roles, apps and sample data. |
| [[10-procurement/test-script-supplier-consignment-2lg-ae-sap-s-4hana-cloud-public-editi\|Test Script: Supplier Consignment (2LG_AE) - SAP S/4HANA Cloud Public Edition (2LG_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item Supplier Consignment (2LG): info record, PO, goods receipt, stock transfer, consignment settlement. |

### Supplier Evaluation and Vendor Performance

How suppliers are evaluated with weighting, scores, questionnaires and appraisals.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-vendor-performance-consumer-products-6a6-ae-1154\|Test Script: Vendor Performance – Consumer Products (6A6_AE) (6A6_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 6A6: supplier evaluation via weighting/scoring, questionnaires, templates, appraisals and scorecards. |
| [[10-procurement/test-script-supplier-evaluation-and-performance-monitoring-sl4-ae-sap\|Test Script: Supplier Evaluation and Performance Monitoring (SL4_AE) - SAP S/4HANA Cloud Public Edition (SL4_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (SL4_AE, 2608): set up and test supplier evaluation by operational KPIs, questionnaires and user-defined criteria. |

### Requisitioning and Consumable Purchasing

How purchase requisitions for consumables are created, approved by flexible workflow and converted to purchase orders, goods receipts and invoices, incl. invoicing plans.

| Node | Description |
| --- | --- |
| [[10-procurement/consumable-purchasing-bnx-ae-test-script-sap-s-4hana-cloud-public-edit\|Consumable Purchasing (BNX_AE) Test Script - SAP S/4HANA Cloud Public Edition (BNX_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item BNX_AE (Consumable Purchasing, UAE): PR, PO, approval, goods receipt, supplier invoice, invoicing plan, retention; release 2608. |
| [[10-procurement/test-script-requisitioning-18j-ae-sap-s-4hana-cloud-public-edition-705\|Test Script - Requisitioning (18J_AE), SAP S/4HANA Cloud Public Edition (18J_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 18J (AE): requisition to PO, approval workflows, goods receipt, supplier invoice, reservation; prerequisites and sample data. |

### Direct Material Procurement

How stock materials are procured from requisition or automatic PO through supplier confirmation, inbound delivery, goods receipt and invoice, incl. cross-company purchasing.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3\|Test Script: Procurement of Production Components – Consumer Products (5W3_AE) (5W3_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5W3 (AE): procure batch-managed raw material with QM and packaging without QM, plant 3310. |
| [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-procurement-of-direct-mat\|Test Script SAP S/4HANA Cloud Public Edition - Procurement of Direct Materials (J45_AE) (J45_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item J45: direct-material procurement from requisition to PO, goods receipt, invoice, plus optional variants. |
| [[10-procurement/test-script-cross-company-purchasing-organization-2r3-ae-854\|Test Script: Cross-Company Purchasing Organization (2R3_AE) (2R3_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script (scope item 2R3, UAE) for cross-company purchasing organization setup, then PO, goods receipt and supplier invoice. |
| [[10-procurement/direct-procurement-with-inbound-delivery-2tx-ae-test-script-sap-s-4han\|Direct Procurement with Inbound Delivery (2TX_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2TX_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition test script for scope item 2TX_AE (UAE): PO, supplier confirmation, inbound delivery, goods receipt and supplier invoice, with roles, sample data and Fiori apps. |

### Purchase Contracts

How quantity purchase contracts with item hierarchies are created, versioned and approved by flexible workflow as sources of supply for purchase orders.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-purchase-contract-bmd-ae-sap-s-4hana-cloud-public-edition\|Test Script: Purchase Contract (BMD_AE) - SAP S/4HANA Cloud Public Edition (BMD_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item BMD Purchase Contract: prerequisites, configuration and step-by-step test procedures. |

### Central Requisitioning, Purchasing and Purchase Contracts

How a hub system centrally processes requisitions, purchase orders and central purchase contracts for connected systems, incl. contract distribution and confirmations.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-central-procurement-with-sap-business-network-for-procurem\|Test Script: Central Procurement with SAP Business Network for Procurement (6BJ) (6BJ_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 6BJ: central purchase orders and supplier confirmations via SAP Business Network. |
| [[10-procurement/test-script-central-requisitioning-1xi-sap-s-4hana-cloud-public-editio\|Test Script: Central Requisitioning (1XI) - SAP S/4HANA Cloud Public Edition (1XI_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for Central Requisitioning (1XI): hub/connected-system setup, PR-to-invoice and reservation test steps. |
| [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchase-contract\|Test Script SAP S/4HANA Cloud Public Edition - Central Purchase Contracts (2ME_AE) (2ME_S4CLD2608_BPD_EN_AE)]] | SAP test script, scope item 2ME (AE): setup and test steps for central purchase contracts, distribution, hierarchy, versioning, mass changes, situations. |
| [[10-procurement/test-script-sap-s-4hana-cloud-public-edition-central-purchasing-2xt-88\|Test Script SAP S/4HANA Cloud Public Edition - Central Purchasing (2XT) (2XT_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 2XT Central Purchasing (hub system 2608): prerequisites, roles, Fiori apps and step-by-step tests for central PR/PO processing, confirmations, automation. |

### Sourcing with SAP Ariba Sourcing

How RFQs become SAP Ariba Sourcing projects and events (guided or classic UI), are awarded, and return as supplier quotations, contracts or purchase orders.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-sourcing-with-sap-ariba-sourcing-4bl-ae-sap-s-4hana-cloud\|Test Script: Sourcing with SAP Ariba Sourcing (4BL_AE) - SAP S/4HANA Cloud Public Edition (4BL_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 4BL_AE: RFQ in S/4HANA Cloud, Ariba sourcing project, event and award (Guided/Classic UI), then supplier quotation, PO, contract. |
| [[10-procurement/central-procurement-with-sap-ariba-sourcing-4qn-test-script-sap-s-4han\|Central Procurement with SAP Ariba Sourcing (4QN) - Test Script, SAP S/4HANA Cloud Public Edition (4QN_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 4QN: central RFQ, Ariba Sourcing (guided/classic UI), award, supplier quotation and follow-on contract or PO in S/4HANA Cloud Public. |

### Purchase-to-Pay Automation with SAP Business Network

How POs, confirmations, ASNs, service sheets and invoices are exchanged with suppliers via SAP Business Network, Ariba Commerce Automation or APIs, incl. supplier search.

| Node | Description |
| --- | --- |
| [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4\|Test Script: Automation of Order-to-Invoice with SAP Business Network (4A1_AE) - SAP S/4HANA Cloud Public Edition (4A1_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script (scope item 4A1, UAE) for supplier-side order-to-invoice with SAP Business Network: prerequisites, setup, 14 test steps. |
| [[10-procurement/test-script-search-for-supplier-in-sap-business-network-7vl-1231\|Test Script: Search for Supplier in SAP Business Network (7VL) (7VL_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 7VL: searching suppliers in SAP Business Network from S/4HANA Cloud, requesting supplier creation, and informing the buyer. |
| [[10-procurement/test-script-automated-purchase-to-pay-with-sap-ariba-commerce-automati\|Test Script: Automated Purchase-to-Pay with SAP Ariba Commerce Automation (J82_AE) (J82_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud Public Edition test script for scope item J82 (UAE): Ariba-integrated PO-to-invoice process, prerequisites and 15 test procedures. |
| [[10-procurement/test-script-integration-of-procurement-with-external-suppliers-2ej-ae\|Test Script: Integration of Procurement with External Suppliers (2EJ_AE) - SAP S/4HANA Cloud Public Edition (2EJ_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item 2EJ_AE (UAE): API-based procurement and return exchange with external suppliers, S/4HANA-to-S/4HANA and third-party via Postman. |
| [[10-procurement/test-script-automation-of-source-to-pay-with-sap-business-network-42k\|Test Script: Automation of Source-to-Pay with SAP Business Network (42K_AE) (42K_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 42K: source-to-pay with SAP Business Network, covering material, service, enhanced limit and ERS procurement. |
| [[10-procurement/test-script-automation-of-central-procurement-quote-with-sap-business\|Test Script: Automation of Central Procurement Quote with SAP Business Network (5JT) (5JT_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script 5JT: central RFQ via SAP Business Network, supplier quote, award, follow-on PO, supplier quick enablement. |

### Supply Chain Collaboration with SAP Business Network

How subcontracting, scheduling agreement, consignment and MRP change request collaboration with direct-material suppliers runs through SAP Business Network.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-supply-chain-automation-with-sap-business-network-5i2-ae-1\|Test Script: Supply Chain Automation with SAP Business Network (5I2_AE) (5I2_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5I2 (AE): subcontracting, scheduling agreements, multi-tier and consignment with SAP Business Network. |
| [[10-procurement/test-script-mrp-change-request-integration-with-sap-business-network-6\|Test Script: MRP Change Request Integration with SAP Business Network (65D_AE) (65D_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud test script (scope 65D_AE) for MRP change requests negotiated with suppliers via SAP Business Network: prerequisites and test steps. |

### Subcontracting Procurement

How subcontracting purchase orders provide components to the supplier and receive finished goods, incl. serial numbers, batches, subcontracting MRP areas and invoicing.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-scheduling-agreement-for-subcontracting-procurement-2nx-ae\|Test Script: Scheduling Agreement for Subcontracting Procurement (2NX_AE) - SAP S/4HANA Cloud Public Edition (2NX_S4CLD2608_BPD_EN_AE)]] | S/4HANA Cloud 2608 (AE) test script, scope item 2NX: subcontracting scheduling agreements, with and without serial numbers, from creation to supplier invoice. |
| [[10-procurement/test-script-subcontracting-consumer-products-5w4-ae-sap-s-4hana-cloud\|Test Script: Subcontracting - Consumer Products (5W4_AE), SAP S/4HANA Cloud Public Edition (5W4_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5W4_AE: subcontracting with batch anonymization, MRP areas, quality inspection and invoicing (plant 3310). |
| [[10-procurement/test-script-subcontracting-bmy-ae-sap-s-4hana-cloud-public-edition-129\|Test Script: Subcontracting (BMY_AE) - SAP S/4HANA Cloud Public Edition (BMY_S4CLD2608_BPD_EN_AE)]] | SAP test script for scope item BMY (UAE) subcontracting in S/4HANA Cloud Public Edition 2608: prerequisites and test steps, with and without serial numbers. |

### Procurement of Services

How services are procured with service POs, contracts and item hierarchies and confirmed by service entry sheets, incl. procurement for customer projects and service orders.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-service-and-material-procurement-project-based-services-j1\|Test Script: Service and Material Procurement – Project-Based Services (J13_AE) (J13_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item J13: service, consumable and third-party procurement for project-based services, with prerequisites and steps. |
| [[10-procurement/test-script-procurement-of-services-22z-ae-sap-s-4hana-cloud-public-ed\|Test Script: Procurement of Services (22Z_AE) - SAP S/4HANA Cloud Public Edition (22Z_S4CLD2608_BPD_EN_AE)]] | SAP Best Practices test script for scope item 22Z (UAE, company code 3310): service PO, service entry sheet, supplier invoice, with prerequisites and workflow setup. |
| [[10-procurement/test-script-procurement-for-service-management-3ni-ae-964\|Test Script: Procurement for Service Management (3NI_AE) (3NI_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 3NI: procurement of consumption materials and external workforce integrated with service orders. |

### Procurement Analytics and Monitoring

Which overview pages and analytical list pages monitor purchase contracts, RFQs, purchase orders, supplier confirmations and spend in real time.

| Node | Description |
| --- | --- |
| [[10-procurement/test-script-real-time-reporting-and-monitoring-for-procurement-1ji-729\|Test Script: Real-Time Reporting and Monitoring for Procurement (1JI) (1JI_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud 2608 test script for scope item 1JI: roles, prerequisites and tests of Procurement Overview, analytical list pages and Spend Dashboard. |

### Purchasing Rebate Processing

How supplier rebate condition contracts accrue business volume and settle partial, delta and final rebates, with scales, fixed amounts, workflow and reversal.

| Node | Description |
| --- | --- |
| [[10-procurement/purchasing-rebate-processing-2r7-ae-test-script-sap-s-4hana-cloud-publ\|Purchasing Rebate Processing (2R7_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2R7_S4CLD2608_BPD_EN_AE)]] | Test script for scope item 2R7 (AE) Purchasing Rebate Processing: config prerequisites, condition contract types, settlements, workflow, fixed amounts, scales, reversal. |

## Related categories
- related-to :: [[02-business-partner-and-product-master-data/_cluster]]
- related-to :: [[03-financial-accounting-and-close/_cluster]]
