---
title: Two-Tier ERP and Central Finance
description: "Headquarter-subsidiary scenarios between SAP Cloud ERP and ECC/Private Edition: integration setup, master data replication, intercompany supply, projects and Central Finance."
cluster: 16-two-tier-erp-and-central-finance
type: cluster
tags: [kb/two-tier-erp-and-central-finance, kb/hub]
keywords: [two-tier ERP, headquarters, subsidiary, ECC, Private Edition, DRF, replication, IDoc, Central Finance]
node_count: 33
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier ERP and Central Finance

Covers processes spanning a headquarter system and a Public Edition subsidiary, and replication to Central Finance. Excludes same-system intercompany processes (see 03, 08, 11, 14) and consolidation in Group Reporting (see 07).

Every node below is the verbatim text of one source document (or one part of a long one), grouped by topic.

## Nodes

### Two-Tier Customer and Supplier Replication

How customer and supplier business partners replicate from headquarter Private Edition to a subsidiary via DRF.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-business-partner-master-customer-233\|Two-Tier: Master Data Replication - Business Partner Master (Customer) (S4CLD2608_2T_Customer Master)]] | Customer guide for replicating customer business partner master data from headquarter S/4HANA Cloud Private Edition to a subsidiary's SAP Cloud ERP via DRF, with test script. |
| [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-supplier-master-235\|Two-Tier: Master Data Replication - Supplier Master (S4CLD2608_2T_Supplier Master)]] | Customer guide for replicating supplier master data from headquarter S/4HANA Cloud Private Edition to a subsidiary's Public Edition via DRF, with test script. |
| [[16-two-tier-erp-and-central-finance/contentmetadata-240\|Contentmetadata (contentmetadata)]] | Machine-generated contentmetadata file (single base64 string, no prose) from the Master data / MasterData Replication Two tier ERP user-guide asset folder; decodes to version properties. |

### Central Finance Replication from Subsidiaries

How subsidiary journal entries, invoices, payments and project data replicate to a Central Finance system for consolidation.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/test-script-process-integration-of-sap-s-4hana-finance-with-central-fi\|Test Script: Process Integration of SAP S/4HANA Finance with Central Finance (88K) (88K_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for 88K: replicating supplier invoices, reversals, changes and billing documents to Central Finance and verifying them. |
| [[16-two-tier-erp-and-central-finance/two-tier-consolidation-of-autonomous-subsidiaries-via-central-finance\|Two-Tier – Consolidation of autonomous subsidiaries via Central Finance (1W4) (S4CLD2608_2T__Consolidation_with_CFINEN)]] | Customer guide and test script for scope item 1W4: replicating finance documents from an S/4HANA Cloud Public Edition subsidiary to an on-premise Central Finance HQ. |
| [[16-two-tier-erp-and-central-finance/test-script-subsidiary-integration-of-sap-s-4hana-cloud-to-central-fin\|Test Script: Subsidiary Integration of SAP S/4HANA Cloud to Central Finance (1W4) (1W4_S4CLD2608_BPD_EN_XX)]] | SAP S/4HANA Cloud Public Edition test script for scope item 1W4: replicating supplier invoices, payments and outgoing invoices to Central Finance (CFIN). |
| [[16-two-tier-erp-and-central-finance/test-script-project-data-replication-to-central-finance-3w1-978\|Test Script - Project Data Replication to Central Finance (3W1) (3W1_S4CLD2608_BPD_EN_XX)]] | Test script for scope item 3W1: create and release a project in the source system and verify replication of project accounting data to Central Finance. |

### Central Financial Compliance Management

How Cloud ERP and on-premise systems connect to SAP Financial Compliance Management for central control monitoring.

| Node | Description |
| --- | --- |
| [[01-solution-foundation-and-platform/test-script-continuous-control-monitoring-with-sap-process-control-2oh\|Test Script: Continuous Control Monitoring with SAP Process Control (2OH) (2OH_S4CLD2608_BPD_EN_XX)]] | S/4HANA Cloud Public Edition test script, scope item 2OH: SAP Process Control data sources, business rules and ad-hoc queries for continuous control monitoring. |
| [[16-two-tier-erp-and-central-finance/two-tier-central-financial-compliance-management-225\|Two-Tier: Central Financial Compliance Management (S4CLD2608_2T_Central Financial Compliance Management)]] | Customer guide for connecting SAP Cloud ERP and on-premise/private S/4HANA systems to SAP Financial Compliance Management in a Two-Tier setup, with test steps and use cases. |

### Two-Tier Cost Center and Profit Center Replication

How cost centers and profit centers replicate from HQ ECC/Private Edition to the subsidiary via Cloud Integration.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-erpcost-center-and-profit-center-replication-using-cloud-inte\|Two Tier ERP–Cost center and Profit center replication using Cloud Integration (S4CLD2608_2T_CC_PC_Replication_Guide)]] | Customer guide for replicating cost center and profit center master data from HQ (ECC/Private) to S/4HANA Cloud public edition via Cloud Integration iFlows, with mapping and test script. |

### Two-Tier Equipment Calibration and Refurbishment

How equipment calibration and refurbishment-with-service run between subsidiary and HQ with event-based integration.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/equipment-calibration-in-two-tier-erp-223\|Equipment Calibration in Two-Tier ERP (S4CLD2608_2T_Equip_Calibration)]] | Customer guide for the Two-Tier ERP equipment calibration scenario between subsidiary (SAP Cloud ERP) and headquarters, with event-based integration and test steps. |
| [[16-two-tier-erp-and-central-finance/two-tier-erp-scenario-refurbishment-with-service-customer-guide-224\|Two-Tier ERP scenario: Refurbishment with Service (Customer Guide) (S4CLD2608_2T_Refurbishment with Service)]] | Customer guide for Two-Tier ERP equipment refurbishment with service between HQ (Tier 1) and subsidiary on SAP Cloud ERP (Tier 2), with event-based integration and test steps. |

### Two-Tier Financial Planning

How HQ plan data is uploaded into a subsidiary and how integrated financial planning with SAP Analytics Cloud spans HQ and subsidiary.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-subsidiary-as-financial-planning-and-upload-of-plan-data-from\|Two-Tier – Subsidiary as Financial Planning and Upload of Plan data from Headquarters (1HB) (S4CLD2608_2T_Financial Plng_upload_plan)]] | SAP Cloud ERP Customer Guide and test script for uploading HQ plan data via CSV into a subsidiary (Import Financial Plan Data) and comparing P&L actual vs plan. |
| [[16-two-tier-erp-and-central-finance/two-tier-erp-integrated-financial-planning-with-sap-analytics-cloud-22\|Two-Tier ERP: Integrated Financial Planning with SAP Analytics Cloud (S4CLD2608_2T_Integrated Financial Planning)]] | Customer guide for hybrid two-tier headquarter/subsidiary integrated financial planning with SAP Analytics Cloud and S/4HANA: prerequisites, connections, test steps (scope 4RC, 1YB). |

### Two-Tier Multiple Specification Inspection

How HQ produces and inspects against country-specific specifications for subsidiary orders.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-erp-scenario-integrated-multiple-specification-inspection-in\|Two-Tier ERP scenario: Integrated Multiple Specification Inspection in Two-Tier ERP (S4CLD2608_2T_Int Multi_Spec Insp)]] | Customer guide for a Two-Tier ERP scenario where a subsidiary on SAP Cloud ERP orders from a headquarter that produces and inspects against country-specific quality standards via APIs. |

### Two-Tier Pricing Replication and Harmonization

How HQ pricing condition records (COND_A04) replicate and how HQ sales prices update subsidiary purchasing info records via Event Mesh.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-erp-pricing-master-integration-using-cloud-integration-237\|Two Tier ERP – Pricing Master Integration using Cloud Integration (S4CLD2608_2T_Pricing Master_Userguide)]] | Customer guide for replicating SD pricing condition records (IDoc COND_A04) from HQ SAP Cloud ERP Private/SAP ERP to a subsidiary SAP Cloud ERP via Cloud Integration, with test script. |
| [[16-two-tier-erp-and-central-finance/two-tier-erp-product-centric-pricing-harmonization-customer-guide-238\|Two Tier ERP – Product-Centric Pricing Harmonization (Customer Guide) (S4CLD2608_2T_Product_Pricing Harmonization)]] | Customer guide and test script for replicating HQ sales pricing conditions to subsidiary purchasing info records in a Two-Tier ERP via Event Mesh and a custom iFlow. |

### Two-Tier Product Master and BOM Replication

How product masters (DRF) and BOMs (BOMMAT01 IDoc) replicate from headquarters to the subsidiary.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-master-data-replication-product-master-customer-guide-234\|Two-Tier: Master Data Replication - Product Master (Customer Guide) (S4CLD2608_2T_Product Master)]] | Two-Tier ERP guide for replicating Product Master data from headquarter S/4HANA Cloud Private Edition to subsidiary SAP Cloud ERP via DRF, with test script (scope 1RO). |
| [[16-two-tier-erp-and-central-finance/two-tier-erp-bill-of-material-integration-using-cloud-integration-236\|Two Tier ERP – Bill of Material Integration using Cloud Integration (S4CLD2608_2T_BoM_Int_User_Guide)]] | Customer guide for replicating BOMs from HQ (Cloud ERP Private/SAP ERP) to a subsidiary SAP Cloud ERP via BOMMAT01 IDoc, Cloud Integration and OData, with field mapping and test script. |

### Two-Tier Engineer-to-Order and Multi-Level Projects

How project-based engineer-to-order and multi-level portfolio/EPPM projects integrate between HQ and subsidiary via APIs.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-scenario-project-based-engineer-to-order-customer-guide-241\|Two-Tier scenario: Project Based Engineer-to-Order (Customer Guide) (S4CLD2608_2T_ETO)]] | Customer guide for the two-tier HQ/subsidiary project-based engineer-to-order integration between SAP Cloud ERP and SAP Cloud ERP (Private) via APIs. |
| [[16-two-tier-erp-and-central-finance/two-tier-multi-level-project-scenario-eppm-customer-guide-243\|Two-Tier: Multi-Level Project Scenario - EPPM (Customer Guide) (S4CLD2608_2T__Multilevel_Project)]] | Conceptual customer guide on integrating headquarters (S/4HANA On-Premise) and subsidiary SAP Cloud ERP via APIs for multi-level portfolio and enterprise project management; no out-of-box… |

### Subsidiary Sales from Local Stock and Returns

How a subsidiary sells and handles returns from local stock while headquarters sees quotes, orders, stock and receivables via APIs.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-sell-from-local-stock-returns-customer-guide-248\|Two Tier – Sell from Local Stock: Returns (Customer Guide) (S4CLD2608_2T_Local_Stock_Returns)]] | SAP Cloud ERP two-tier customer guide and test script for customer returns at a subsidiary (return order to credit memo) with HQ visibility via API/CDS views. |
| [[16-two-tier-erp-and-central-finance/two-tier-sale-from-local-stock-by-subsidiary-249\|Two-Tier: Sale from Local Stock by Subsidiary (S4CLD2608_2T_Sale_from_Local_Stock)]] | SAP Cloud ERP Two-Tier customer guide: subsidiary sells from local stock with HQ visibility on quotes, orders, stock, receivables; APIs, CDS views, test script. |

### Manufacturing Subsidiary Assembly for Headquarters

How a manufacturing subsidiary performs make-to-order assembly for headquarters from sales order to billing (2WL).

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/test-script-enable-manufacturing-subsidiary-to-handle-assembly-for-hea\|Test Script: Enable Manufacturing Subsidiary to Handle Assembly for Headquarter (2WL_AE) (2WL_S4CLD2608_BPD_EN_AE)]] | SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 2WL: subsidiary performs make-to-order assembly for headquarters, from sales order to invoice. |

### Subsidiary Procurement with HQ Visibility

How a subsidiary runs its own procurement and sales while headquarters gains visibility through APIs and CDS views (J45).

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-procurement-directly-by-subsidiary-with-visibility-to-headqua\|Two-Tier Procurement directly by subsidiary with visibility to Headquarters (J45) (S4CLD2608_2T_Proc_J45)]] | SAP S/4HANA Cloud 2608 customer guide and test script for scope item J45: subsidiary-run procurement and sales with HQ visibility via APIs and CDS views. |

### Subsidiary Procurement from Headquarters

How subsidiary POs become HQ sales orders via EDI/IDoc, with ASN, billing and conversion of HQ invoices into supplier invoices.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-erp-procurement-by-subsidiary-from-headquarters-replenishment\|Two-Tier ERP: Procurement by Subsidiary from Headquarters (Replenishments) (S4CLD2608_2T_Replenishment_Guide)]] | SAP Two-Tier ERP customer guide: subsidiary replenishment from HQ via EDI/IDoc (PO to sales order, ASN, billing), with configuration, master data and test script. |
| [[16-two-tier-erp-and-central-finance/two-tier-erp-billing-document-to-supplier-invoice-integration-using-cl\|Two Tier ERP – Billing Document to Supplier Invoice Integration using Cloud Integration (S4CLD2608_Two tier ERP_Bill_Invoice_User_Guide_EN)]] | Customer guide for two-tier ERP integration converting an HQ billing document (IDoc INVOIC02) into a supplier invoice in S/4HANA Cloud Public Edition via Cloud Integration, with test script. |

### Subsidiary as Sales Office with HQ Drop Shipment

How a subsidiary sales office sells while headquarters drop-ships to the customer via EDI/IDoc.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-erp-subsidiary-as-sales-office-drop-shipment-from-headquarter\|Two-Tier ERP: Subsidiary as Sales Office, Drop-shipment from Headquarter - Customer Guide (S4CLD2608_2T_ Drop Shipment_User_Guide)]] | SAP Cloud ERP two-tier guide: subsidiary sales office with drop shipment from headquarters; prerequisites, EDI/IDoc setup, master data, and test script (scope BD3/2EJ). |

### Subsidiary Service Order Delivery for Headquarters

How a subsidiary delivers services against a headquarter purchase order via EDI/IDoc and APIs.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-erp-service-order-management-in-headquarter-subsidiary-model\|Two-Tier ERP: Service Order Management in Headquarter-Subsidiary Model (2-Tier ERP) (S4CLD2608_2T_Service ord)]] | SAP customer guide for two-tier ERP where a subsidiary on Cloud ERP delivers services against a headquarter purchase order: process, EDI/IDoc/API setup, test script. |

### Two-Tier MRP Visibility and Demand Planning

How HQ and subsidiary see each other's MRP supply/demand and run SAP IBP demand planning ending in PIRs.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/material-requirement-planning-visibility-in-two-tier-erp-232\|Material Requirement Planning Visibility in Two-Tier ERP (S4CLD2608_2T_MRP_Analytics)]] | Customer guide for the Two-Tier ERP scenario giving headquarters and subsidiary API-based visibility of each other's MRP supply and demand results. |
| [[16-two-tier-erp-and-central-finance/demand-planning-with-sap-ibp-for-headquarter-subsidiary-model-252\|Demand Planning with SAP IBP for Headquarter-Subsidiary model (S4CLD2608_2T_DP_IBP)]] | Two-Tier ERP customer guide: SAP IBP demand planning for HQ-subsidiary model with scope items, integration setup, roles and test script ending in PIR transfer. |

### Two-Tier ERP Integration Setup

How ECC or on-premise S/4HANA connects to S/4HANA Cloud via SAP Cloud Integration: communication arrangements, inbound and outbound setup.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-erp-integration-setup-document-230\|Two-Tier ERP Integration Setup Document (S4CLD2608_2T_Int_Setup_Guide_EN)]] | Customer guide for configuring integration between SAP ECC / on-premise S/4HANA and S/4HANA Cloud Public Edition via SAP Cloud Integration, inbound and outbound IDoc scenarios. |

### Two-Tier Professional Services Projects

How HQ and subsidiary procure, staff and bill project-based services across two tiers, including intercompany professional services projects.

| Node | Description |
| --- | --- |
| [[16-two-tier-erp-and-central-finance/two-tier-scenario-managing-intercompany-professional-services-projects\|Two-Tier scenario: Managing Intercompany Professional Services Projects (S4CLD2608_2T_Managing PFS Projects)]] | Customer guide for the two-tier headquarters/subsidiary scenario for intercompany professional services projects: process flows, communication arrangements, prerequisites, scope items. |
| [[16-two-tier-erp-and-central-finance/two-tier-project-based-services-procurement-between-headquarter-and-su\|Two Tier - Project Based Services Procurement between Headquarter and Subsidiary (S4CLD2608_2T_Proj_ServiceProcurement)]] | SAP S/4HANA Cloud Public Edition customer guide and test script for two-tier project-based services procurement: HQ on-premise/ECC buys services from a Cloud ERP subsidiary. |

## Related categories
- related-to :: [[07-group-reporting-and-consolidation/_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/_cluster]]
