---
id: 12-production-and-manufacturing/produce-and-sell-standard-products-warehouse-managed-54v-ae-test-scrip
title: "Produce and Sell Standard Products – Warehouse Managed (54V_AE) – Test Script, SAP S/4HANA Cloud Public Edition (54V_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 54V_AE (UAE, plant 3310): MTS planning, repetitive and discrete production, WM-managed warehouse, QM, sales, billing and AP/AR posting."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/end-to-end-produce-and-sell]
aliases: [54V_S4CLD2608_BPD_EN_AE]
keywords: [End-to-End Produce-and-Sell Scenarios, make-to-stock production, planned independent requirements, material requirements planning, repetitive manufacturing, production orders, warehouse tasks, production supply area, material staging, quality inspection]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54V_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1067
topic: 12-production-and-manufacturing/end-to-end-produce-and-sell
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Produce and Sell Standard Products – Warehouse Managed (54V_AE) – Test Script, SAP S/4HANA Cloud Public Edition (54V_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54V_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **End-to-End Produce-and-Sell Scenarios** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Produce and Sell Standard Products – Warehouse Managed (54V_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Produce and Sell Standard Products – Warehouse Managed (54V_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232855894)

[2 Prerequisites 5](#_Toc232855895)

[2.1 System Access 5](#_Toc232855896)

[2.2 Roles 5](#_Toc232855897)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232855898)

[2.4 Business Conditions 12](#_Toc232855899)

[2.5 Additional Manual Configuration 13](#_Toc232855900)

[2.6 Preliminary Steps 13](#_Toc232855901)

[2.6.1 Create Purchasing Info Records 13](#_Toc232855902)

[2.6.2 Create Purchase Contract 16](#_Toc232855903)

[2.6.3 Generate Source List 17](#_Toc232855904)

[2.6.4 Define Default Values for Clerk(WM) 19](#_Toc232855905)

[2.6.5 Define Default Values for Warehouse Operative (WM) 19](#_Toc232855906)

[2.6.6 Assign Fixed Storage Bins to Component 20](#_Toc232855907)

[2.6.7 Create Control Cycle (IM-managed Production Supply Area) 21](#_Toc232855908)

[2.6.8 Create Control Cycle 22](#_Toc232855909)

[2.6.9 Assign Bins to PSA 23](#_Toc232855910)

[2.6.10 Define Favorite Packaging Materials 25](#_Toc232855911)

[2.6.11 Staging Area and Door Determination (Outbound) 26](#_Toc232855912)

[2.6.12 Create Product Cost Collectors 26](#_Toc232855913)

[2.6.13 Create Preliminary Cost for the Product Cost Collector 27](#_Toc232855914)

[2.6.14 Access Sequence to Staging Areas and Door Determination 28](#_Toc232855915)

[3 Overview Table 29](#_Toc232855916)

[4 Test Procedures 34](#_Toc232855917)

[4.1 Anonymous Forecast and MRP Data 34](#_Toc232855918)

[4.1.1 Create Planned Independent Requirements 34](#_Toc232855919)

[4.1.2 Material Requirements Planning at Plant Level 35](#_Toc232855920)

[4.1.3 Evaluate Stock/Requirements Situation (Optional) 37](#_Toc232855921)

[4.2 Procurement of Raw Material 39](#_Toc232855922)

[4.2.1 Convert Purchase Requisitions to Purchase Orders 39](#_Toc232855923)

[4.2.2 Display Purchase Order 41](#_Toc232855924)

[4.2.3 Create Inbound Delivery 42](#_Toc232855925)

[4.2.4 Create Handling Unit (Optional) 43](#_Toc232855926)

[4.2.5 Post Goods Receipt 44](#_Toc232855927)

[4.2.6 Create Putaway Warehouse Tasks 46](#_Toc232855928)

[4.2.7 Confirm Warehouse Tasks 47](#_Toc232855929)

[4.2.8 Check Stock Level (Optional) 48](#_Toc232855930)

[4.2.9 Evaluate Stock/Requirements Situation (Optional) 50](#_Toc232855931)

[4.2.10 Display Procurement Overview (Optional) 52](#_Toc232855932)

[4.3 Repetitive Manufacturing for Semi-Finished Products 53](#_Toc232855933)

[4.3.1 Adjust Planning in Planning Table 53](#_Toc232855934)

[4.3.2 Check Range of Stock Coverage 54](#_Toc232855935)

[4.3.3 Material Staging 55](#_Toc232855936)

[4.3.4 Create Staging Warehouse Tasks 58](#_Toc232855937)

[4.3.5 Confirm Staging Warehouse Tasks 59](#_Toc232855938)

[4.3.6 Post Goods Issue for Staging 60](#_Toc232855939)

[4.3.7 Confirm Repetitive Manufacturing Inclusive Backflush of Materials for (non-JIT) 61](#_Toc232855940)

[4.3.8 Post Processing of Error Records for non-JIT production 63](#_Toc232855941)

[4.3.9 Check Material Document (Optional) 64](#_Toc232855942)

[4.3.10 Check Goods Movement Document (Optional) 65](#_Toc232855943)

[4.3.11 Check Warehouse Task 65](#_Toc232855944)

[4.3.12 Confirm Putaway Warehouse Tasks 66](#_Toc232855945)

[4.4 Production Order Execution Finished Product 67](#_Toc232855946)

[4.4.1 Convert Planned Order to Production Order 67](#_Toc232855947)

[4.4.2 Maintain Serial Numbers in Production Order 68](#_Toc232855948)

[4.4.3 Review Production Order 70](#_Toc232855949)

[4.4.4 Release Production Order 72](#_Toc232855950)

[4.4.5 Trigger Creation of Production Material Request 73](#_Toc232855951)

[4.4.6 Check Production Material Request (Optional) 75](#_Toc232855952)

[4.4.7 Create Staging Warehouse Tasks 76](#_Toc232855953)

[4.4.8 Confirm Staging Warehouse Tasks 77](#_Toc232855954)

[4.4.9 Post Consumption of Components 78](#_Toc232855955)

[4.4.9.1 Confirm Production Operations 79](#_Toc232855956)

[4.4.9.2 Review Production Order (Optional) 80](#_Toc232855957)

[4.4.10 Clear Production Supply Area (Optional) 82](#_Toc232855958)

[4.4.11 Confirm Warehouse Task for PSA Clearence (Optional) 83](#_Toc232855959)

[4.4.12 Create Inbound Delivery for Production Order 84](#_Toc232855960)

[4.4.13 Create Handling Unit 85](#_Toc232855961)

[4.4.14 Post Goods Receipt 87](#_Toc232855962)

[4.4.15 Create Putaway Warehouse Tasks 88](#_Toc232855963)

[4.4.16 Confirm Putaway Warehouse Tasks 89](#_Toc232855964)

[4.5 Quality Inspection 91](#_Toc232855965)

[4.5.1 Display Open Inspection Lots (Optional) 91](#_Toc232855966)

[4.5.2 Record Inspection Results 92](#_Toc232855967)

[4.5.3 Make Usage Decision 94](#_Toc232855968)

[4.5.4 Confirm Putaway Warehouse Tasks 96](#_Toc232855969)

[4.5.5 Evaluate Stock/Requirements Situation 97](#_Toc232855970)

[4.6 Customer Order Creation and Outbound Delivery Creation 98](#_Toc232855971)

[4.6.1 Create Sales Order 98](#_Toc232855972)

[4.6.2 Create Delivery with Order Reference 100](#_Toc232855973)

[4.6.3 Create Pick Warehouse Tasks 101](#_Toc232855974)

[4.6.4 Confirm Pick Warehouse Tasks 102](#_Toc232855975)

[4.6.5 Pack Goods into Shipping Handling Units (Optional) 104](#_Toc232855976)

[4.6.6 Enter Serial Number for Outbound Delivery Order (Optional) 105](#_Toc232855977)

[4.6.7 Print Loading Instruction (Optional) 106](#_Toc232855978)

[4.6.8 Post Goods Issue 107](#_Toc232855979)

[4.7 Accounts Receivable 108](#_Toc232855980)

[4.7.1 Create Billing Document 108](#_Toc232855981)

[4.7.2 Post Incoming Payments 109](#_Toc232855982)

[4.8 Accounts Payable 111](#_Toc232855983)

[4.8.1 Create Supplier Invoice with PO/GR Relation 111](#_Toc232855984)

[4.8.2 Post Outgoing Payment 113](#_Toc232855985)

## Purpose

Overview

This scope item enables production planning and execution for a finished good in make-to-stock scenarios, as well as prompt reactions to incoming sales orders (sell from stock).

The process starts with the creation of a demand forecast for finished goods represented by planned independent requirements (PIRs). Based on PIRs, material requirements planning (MRP) creates a production plan for finished goods and explodes the entire bill of material. This planning results in raw material demand. Production planners can analyze and manually change the planned order-based production plan.

Raw material demand leads to component demands that trigger external procurement via purchase orders and inbound delivery.

The semi-finished product is produced via repetitive manufacturing into the warehouse. With the repetitive manufacturing confirmation, semi-finished material is received into the specified warehouse goods receipt bin and raw material is issued from stock. The goods receipt (movement type 131) and the goods issue (movement type 261) are posted synchronously in one material document. In addition, the system automatically generates a warehouse task.

The production process of the finished product via discrete manufacturing includes converting planned orders to production orders, releasing orders, staging and picking materials, confirming order operations, and posting goods receipts. Upon acceptance of quality inspection results, finished product is moved to unrestricted stock.

The process continues with creating sales orders, performing deliveries from the stock present in a warehouse-managed location, invoicing, and clearing after incoming payment.

All products in this scenario use warehouse-managed storage locations. Quality inspection is triggered during goods receipt for production orders.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Planner | SAP_BR_QUALITY_PLANNER | Quality Planning | SAP_BR_QUALITY_PLANNER |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |
| Production Supervisor - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV | Production Management - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV |  |
| Production Operator - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV | Production Execution - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV |  |
| Master Data Specialist - Handling Unit Data | SAP_BR_HU_MASTER_SPECIALIST | Master Data - Handling Units | SAP_BR_HU_MASTER_SPECIALIST |  |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |
| BOM Engineer | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |  |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Material Master Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG012 | BEARING | Finished Product with Serial number.Relevant for planning. MRP planned and produced internally as per make-to-stock strategy. Lot for lot planning. NOT Batch Managed. Not Handling Unit Managed. Not split valuated.Sold to customer. WM managed. Product is to be costed. costing and accounting views to be maintained.This product will undergo quality inspection just before delivery to customer and hence Quality Management view to be enabled with respect to outbound delivery process. |
| Material | RM015 | INNER RING | Externally Procured Material.MRP Planned and procured from external supplier. Lot for lot planning,Not applicable for Quality Management.NOT Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | RM016 | OUTER RING | Externally Procured Material.MRP Planned and procured from external supplier. Lot for lot planningWM managed. Not applicable for Quality Management.NOT Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | RM021 | STEEL WIRE | Externally Procured Material.MRP Planned and procured from external supplier. Lot for lot planningWM managed. Not applicable for Quality Management.NOT Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | SG012 | STAINLESS STELEL BEARING BALLS | Semifinished Material.MRP Planned and produced internally using repetitive manufacturing process.Only Inventory Managed (WM managed). Not applicable for Quality Management. Not Serial number managed. Not Batch Managed. Not Handling Unit Managed. |
| Material | PMPALLET | Packing Material |  |

Extension of Material Master with warehouse data:

Products FG012, SG012, RM021, RM015 and RM016 must be extended with warehouse data setting the correct Putaway control indicator and Stock Removal control indicator.

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Warehouse | 3350 | Warehouse |  |
| Party entitled to Dispose | 33413310 |  |  |

Organizational Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Storage Location | 335W | Storage Location for Cloud WM |  |
| Production Supply Area (PSA) | PSA_03 | PSA for advanced production integration |  |

Material Master: Enable QM view

The finished product FG012 of this scope item is subject to quality inspection at time of goods receipt from production. Hence, the material master of FG012 needs to be enabled with Quality Management view and inspection type 04 Goods receipt inspection from production that must be set in QM view of material master.

Bill of Material Structure

BOM structure mentioned below must be created and made available as part of this scope item. The BOM must be created in the plant.

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG012 | 0 | FERT | PC | Finished Good for MTS processing with Serial Number. |  |  |
| RM015 | 1 | ROH | PC | External procured. Fixed bin, WM Managed. | 1 | PC |
| RM016 | 1 | ROH | PC | External procured. Fixed bin, WM Managed. | 1 | PC |
| SG012 | 1 | HALB | PC | Produced In House, WM managed | 10 | PC |
| RM021 | 2 | ROH | KG | External procured. Fixed bin, WM Managed. | 0.10 | KG |

Please refer to the above table for the values to be populated in the BOM structure.

Work center

The below table mentions the work centers to be used in this scenario. These are standard work centers available and there is no need to create new Work Centers.

| Work Center | Plant | Work Center Category | Work center Description |
| --- | --- | --- | --- |
| ASSEMBLY | 3310 | 0001 | Assembly |
| PACK01 | 3310 | 0001 | Packing Line 1 |
| TESTING | 3310 | 0001 | Testing |

Routing:

Create a routing for the Finished product FG012 (BEARING) and Semi finished Product, SG012 – STAINLESS STEEL BEARING BALLS . The routing must be created in the plant.

Production Version:

Create production version for the finished product FG012 (BEARING) and Semi finished Product, SG012 – STAINLESS STEEL BEARING BALLS using the BOM and routing created in the steps above. The production version must be created in the plant.

Suppliers:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Supplier | 33300001 | Domestic Supplier 1 |  |
| Supplier | 33300002 | Domestic Supplier 2 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |

Customer:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Ship-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |
| Shipping point | 3310 |  |  |
| Company code | 3310 |  |  |

Purchasing Info Record:

A new purchasing info record needs to be created between the supplier (33300001) and raw material (RM016) in plant 3310 and purchasing organization 3310. Similarly, a new purchasing info record must be created between supplier (33300002) and raw material (RM015) as well as raw material (RM021) in plant 3310 and purchasing organization 3310. Purchasing info records must be setup in both, plant and purchasing organization.

Quality Inspection Plan:

Quality Inspection Plan uses the standard work center ‘QMLABS’.

Quality inspection needs to be created in the plant.

Warehouse-Specific Master Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Storage Type | SF01 | Fixed Bin Storage |  |
| Storage Type | SB01 | Bulk Storage |  |
| Storage Type | S105 | Production Supply |  |
| Storage Type | S915 | Goods Receipt from Production |  |
| Storage Type | S970 | Clarification Zone |  |

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of Type "Raw Material" |
| BNT | Create Product Master of Type "Finished Good" |
| BNJ | Create Production Work Center |
| BNK | Create Material BOM for Production and Sales |
| BNL | Create Routing |
| BLD | Create Production Version |
| BNQ | Create Quality Inspection Plan |
| BNE | Create Supplier Master |
| BHD | Purchasing Info Record |
| BND | Create Customer Master |
| 3KQ | Create Warehouse Attributes for Material/Product Master |
| 3KR | Create Warehouse Storage Bins and Fixed Bin Assignments |
| 3KS | Create Warehouse Master Data for Production Supply |
| 40D | Create Production Supply Area |

### Business Conditions

Before this scenario can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Standard Cost Calculation (BEG) test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| BNY- Create Quality Management Attributes for Material/Product Master - MDS | Complete all steps in the master data script for inspection type 10. |
| BNQ - Create Quality Inspection Plan - MDS | To create Quality Inspection Plan. |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |
| BFA - Basic Bank Account Management | Bank account master data is processed. |
| 3BR - Warehouse Inbound Processing | Warehouse Inbound Processing scope item must be activated in the system. |
| 3DV - Warehouse Production Integration | Warehouse Production Integration scope item must be activated in the system. |
| 41U - Warehouse Goods Receipt from Repetitive Manufacturing | 41U - Warehouse Goods Receipt from Repetitive Manufacturing |
| 6NI - Warehouse Advanced Production Integration | Warehouse Advanced Production Integration scope item must be activated in the system |
| 1E1 - Quality Management in Discrete and Process Manufacturing | Quality Management in Discrete Manufacturing scope item must be activated in the system. |

### Additional Manual Configuration

Before starting the execution of this scenario, the warehouse setup has been completed as per instructions mentioned in the setup guide of warehouse management of SAP S/4HANA Cloud Public Edition. For more information, refer to the following [set-up instructions](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_588%20Warehouse%20Management%20Setup.docx) available in the SAP Activate methodology for SAP S/4HANA Cloud Public Edition.

### Preliminary Steps

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

#### Create Purchasing Info Records

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note If the info record for the material and supplier mentioned in this step already exists in the system, you can skip this step. Otherwise, complete the following procedure for each material mentioned below. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Organization: 3310Purchasing Info Record Category: StandardSupplier: 33300001Material: RM016 (for component 1)Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | In the General Information section, make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | In the Purchasing Data section, make the following entries:Incoterm: EXWNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an incoterm automatically populates its associated version, which can be subsequently modified or removed if needed.Incoterm Location 1: Vendor Location | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 2Under Delivery Tolerance in %: 0Over Delivery Tolerance in %: 0Tax Code: <Input Tax Code>Note When the TDT (time dependent tax) is activated via SSCUI 101016 (Define Tax Codes for Sales and Purchases) for Country of company code and Tax Code is given, the Tax RateValid From field is mandatory. You can enter the current date which will be adjusted to validity start date of tax code according to the setting in SSCUI.Confirmation Control: Inbound DeliveryOrder Unit: PCStandard Order Quantity: 1Goods-Receipt-Based Invoice Verification: selectNo Evaluated Receipt Settlement: select | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 10Pricing Unit: 1Unit of Measure: PCCurrency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Tax Rate Valid from Date | Tax Rate Valid From:Today's dateNote After the user selects this date, the system changes date in Tax Rate Valid From to Validity start date of Tax code. This is expected behavior. | Tax rate valid from date is populated. |  |
| 10 | Create your data | Choose Create. | The purchasing info record is created. |  |

|  |
| --- |
| Note Repeat the above steps to create the Info Record for Material RM015 and Supplier 33300002 and for Material RM021 and Supplier 33300002. |

#### Create Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a Reference Purchase Contract.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Choose Manage Purchase Contracts (F1600A) . | The Manage Purchase Contracts screen displays. |  |
| 3 | Enter Contract Header details | On the screen Manage Purchase Contracts, choose Create and make the following entries:Contract Type: Choose MK Quantity ContractSupplier: 33300002Purchasing Org.: 3310Valid From: Start date of the contract, for example, todayValid To: End date of the contract, for example, the end of this yearTarget value: For example, 1000 AEDPurchasing Group:001Currency: AEDIn section Delivery and Payment Terms:Incoterm: EXWIncoterm Location: Vendor Location |  |  |
| 4 | Enter Contract Item details | In the Items tab, choose Create and make the following entries:Material: RM015Plant: 3310.In section Quantity and Price:Net price: <Automatically Updated>Target Quantity: For example, 5000. If RITA is enabled at company code level, Tax Country field is available for input in purchase contract item GR/IR facet during creation and updating.In the Supplier Confirmation Control tab:Confirmation Control: 0004Note It is mandatory to include confirmation control key in this step.Choose Apply. | The Purchase Contract screen displays. |  |
| 5 | Save the Purchase Contract | Choose Create and when the purchase contract number is displayed, write it down for further use. | A new Purchase Contract is created. The Purchase Contract Number is displayed |  |

#### Generate Source List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you maintain the contract as the source.

Table 1: Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the Fiori launchpad with the Purchaser role. | The Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Manage Source Lists (F1859) app. | The Manage Source Lists screen is displayed. |  |
| 3. | Maintain the filter of the source list | In the filter, make the following entries:Material: RM015.Plant: 3310.Then choose Go. | If the source list item was already maintained, it will be shown. |  |
| 4. | Check the source list | If there is one item that is valid in the current period, ignore the following steps. If there isn't a valid item, continue with the next steps. |  |  |
| 5. | Create source list | Choose the Create button. | The Source List screen is displayed. |  |
| 6. | Enter the detail data | Enter data in the following fields:Material For example: RM015Plant For example:3310Choose Generate. |  |  |
| 7. | Use the Generated source to choose determine source | In the Generated Sources screen, enter data in the following fields:Valid From: For example, TodayValid to: For example, Today +99 daysChoose Go.Then choose the check box of one contract, for example, select the contract that you created in step Create Purchase Contract of this scenario.And choose Add to Existing. |  |  |
| 8. | Save the source list | Choose Save.Note If there are any empty lines highlighted in red color, then these empty lines with red must be deleted by selecting them and clicking Delete. After all the empty lines are deleted, choose Create. | The source list is saved. |  |

#### Define Default Values for Clerk(WM)

Purpose

In this step, you can define the default warehouse number for the Warehouse Clerk (EWM).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Choose Avatar | Choose Icon for the logon user.Choose Settings. |  |  |
| 3 | Enter Default Value | Choose Default Values.And make the following entry in the section Material Management:Warehouse Number: 3350.Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (WM)

Purpose

In this step, you can define the default warehouse number for the Warehouse Operative (EWM).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The Fiori launchpad is displayed. |  |
| 2 | Choose Avatar | Choose the Icon for your logon user.Then, choose Settings. |  |  |
| 3 | Enter Default Value | Choose Default Values.In the Material Management section, enter the following data:Warehouse Number: 3350.Choose Save. |  |  |

#### Assign Fixed Storage Bins to Component

Purpose

In this step, you assign fixed storage bins to products.

You are required to complete this procedure thrice, making assignments for both the RM015RM016 and RM021 materials. This is described in the appropriate steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Assign Fixed Bins (/SCWM/BINMAT). | The Assign Fixed Storage Bins screen displays. |  |
| 3 | Enter Data | On the Assign Fixed Storage Bins screen, enter the following data:Warehouse Number: 3350Product: RM015.Choose Run. |  |  |
| 4 | Maintain Fixed Bin | Choose Edit to switch to change mode.Choose Create button.Enter the following data:WhN: 3350.Disposal: 33413310Storage Bin: SF01-03-02.Product: RM015.Choose Save. |  |  |
| 5 | Repeat steps 3 and 4 | Repeat steps 3 and 4 with Storage Bin: SF01-03-03 for Product: RM016. |  |  |
| 6 | Repeat steps 3 and 4 | Repeat steps 3 and 4 with Storage Bin: SF01-03-04 for Product: RM021. |  |  |

#### Create Control Cycle (IM-managed Production Supply Area)

Purpose

In this activity, you create a control cycle that can be used for in-house production in the production supply area. In the control cycle, you define the demand source, the supply source, and the material staging indicator. The material staging indicator defines the method of how needed materials can be supplied for production with the assistance of the warehouse management system.

To create the control cycle for the RM021 material, complete the following procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Control Cycle for WM (LPK1). | The Create Control Cycle: Initial Screen (WM) screen is displayed. |  |
| 3 | Enter Data | Make the following entries and choose Enter.Material: RM021Plant: 3310Supply Area: PSA_01 |  |  |
| 4 | Choose Enter | Choose Enter. | The Create Control Cycle: Data Screen (WM) screen is displayed. |  |
| 5 | Enter Control Cycle Details | Make the following entries:In the Destination section:Staging Ind.: 3 (Release order part)In the Source section:Stor. Location: 335WWarehouse No: 335In the Destination Bin Assignment section: Destination Bin: PROD-SUPPLYChoose Save | The Destination Stor. Location, Destination Warehouse Number, Source Issuing Plant, and Source Warehouse No fields are automatically filled by the system.The Source Warehouse No. is not for input initially and it is automatically filled after entering the Source Storage Location.You’ve created the control cycle for material RM021. |  |

#### Create Control Cycle

Purpose

In this activity, you create a control cycle that can be used for in-house production in the production supply area. In the control cycle, you define the demand source, the supply source, and the material staging indicator. The material staging indicator defines the method of how needed materials can be supplied for production with the assistance of the warehouse management system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Control Cycle for WM (LPK1). | The Create Control Cycle: Initial Screen (WM) screen is displayed. |  |
| 3 | Enter Data | On the Create Control Cycle: Initial Screen (WM) screen, make the following entries:Material: RM015Plant: 3310.Supply Area: PSA_03. |  |  |
| 4 | Choose Enter | Choose Enter. | The Create Control Cycle: Data Screen (WM) screen is displayed. |  |
| 5 | Enter Control Cycle Details | Make the following entries:In the Destination section:Staging Ind.: 5 (EWM Staging)In the Source section:Stor. Location: 335W | The Destination Stor. Location, Destination Warehouse Number, Source Issuing Plant, and Source Warehouse No fields are automatically filled by the system. |  |
| 6 | Choose Save | Choose Save. | The following system message appears:Control cycle RM015 PSA_03 will be created. |  |
| 7 | Repeat for remaining Components | Repeat above steps and create control cycles for materials RM016, and SG012. | You have created control cycles for WM staging of materials RM016, and SG012. |  |

#### Assign Bins to PSA

Use

In this activity, you manage the storage bins that are used for production supply at the level of the production supply area. You assign each of them to a production supply area, a party entitled to dispose, and a product. You maintain additional attributes related to the production supply process such as staging methods, quantities, and the warehouse process types used for creation of the staging warehouse tasks and the warehouse tasks for clearing the PSA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Assign Bin to PSA (/SCWM/PSASTAGE2). | The Determine Work Area: Entry dialog box appears. |  |
| 3 | Make Entries | In the Determine Work Area: Entry dialog box, make the following entries:Warehouse Number: 1750Party Entitled to Dispose:33413310Supply Area: PSA_03 /3310For the field Supply Area, use the value help. |  |  |
| 4 | Choose Enter | Choose Apply (Enter). | The Assign Bin to PSA: Change screen appears. |  |
| 5 | Choose New Entries | On the Assign Bin to PSA: Change screen, choose New Entries. | The New Entries: Details of Added Entries screen appears. |  |
| 6 | Make Entries | On the New Entries: Details of Added Entries screen, make the following entries:Product: RM015In the Assign Bin Section:Storage Bin: PROD-SUPPLY-5Staging Method: Single-Order StagingQty Calc. Type: Quantity - Based CalculationChoose Enter.Replmt Qty: 20Min.Prd.Qty PSA: 200Unit: PCStaging WPT: S220Clear PSA WPT: S325 |  |  |
| 7 | Choose Save | Save your entries. | The following system message appears:Data was savedYou have created an entry for material RM015.The New Entries: Added Entries screen appears. |  |
| 8 | Choose Cancel | On the New Entries: Added Entries screen, choose cancel to return to the Assign Bin to PSA: Change screen. | The Assign Bin to PSA: Change screen appears. |  |
| 9 | Repeat the Steps | Repeat steps 5 to 8 and make the following entries:For material RM016:Product: RM016In the Assign Bin section:Storage Bin: PROD-SUPPLY-5Staging Method: Single-Order StagingQty Calc. Type: Quantity-Based CalculationChoose Enter.Replmt Qty: 10Min.Prd.Qty PSA: 10Unit: PCStaging WPT: S220Clear PSA WPT: S325For material RM021:Product: RM021In the Assign Bin Section:Storage Bin: PROD-SUPPLY-6Staging Method: Single-Order StagingQty Calc. Type: Quantity-Based CalculationChoose Enter.Replmt Qty: 100Min.Prd.Qty PSA: 200Unit: KGStaging WPT: S220Clear PSA WPT: S325 | You have created entries for material , RM016, and SG012. |  |

#### Define Favorite Packaging Materials

In this step, you define the favorite packaging materials to be used in the app.

Use

In this step, you define the packaging material(s) that will be proposed when creating handling units at specific work centers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Define Favorite Packaging Materials (/SCWM/TWSPACKMAT) | The Define Favorite Packaging Materials (/SCWM/TWSPACKMAT) screen is displays. |  |
| 3. | Enter Warehouse Number | At first, the dialog box displays Determine Work Area: Entry displays. Make the following entry:Warehouse Number: 3350Choose Continue. | The Define Favorite Packaging Materials screen is displays. |  |
| 4. | Switch the Mode | Choose Edit on the upper right. | The screen name changes to Define Favorite Packaging Materials: Change. |  |
| 5. | Choose New Entries | Once you have switched the mode, you can see different options.Choose New Entries. | The gray fields are open for editing your required packaging materials now. |  |
| 6. | Fill in Required Entries | Work Center: PackProduct: for example PMPALLETDefault: XSequence: 1Choose Save. | A dialog box with the message Data was saved appears in the right corner. |  |

#### Staging Area and Door Determination (Outbound)

Use

In this step, you define the logic in the outbound process to determine which outbound delivery order with respective materials should go to which Storage Bin in the Outbound Staging Area. This can help you distribute your materials by, for example carriers, for a better separation and planning.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Determine Staging Area - Outbound (/SCWM/STADET_OUT) | The Determine Staging Area - Outbound (/SCWM/STADET_OUT) screen displays. |  |
| 3. | Create new entries | Choose New Entries and create the first entry with the following values:Warehouse Number:3350Carrier: 33300001Sequence Number: 1Stg. Area Group: S920Staging Bay: GI-AREA-02Choose Save. |  |  |
| 4. | Create new entries | Create the second entry with the following values:Warehouse Number: 3350Whse Proc. Type: S210Sequence Number: 1Stg. Area Group: S920Staging Bay:GI-AREA-01Choose Save. |  |  |

#### Create Product Cost Collectors

Purpose

This step can only be executed if product cost planning is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Product Cost Collectors - Production Versions - Collective (KKF6M). |  |  |
| 3 | Enter Relevant Values | On the Create Multiple Product Cost Collectors for Production Versions screen, make the following entries and choose Run.Plant: 3310Material: SG012Order Type: YBMROnly Repetitive Mfg Mat.: select |  |  |
| 4 | Exit | Choose Exit. |  |  |

#### Create Preliminary Cost for the Product Cost Collector

Purpose

This process step shows you how to create preliminary cost for the product cost collector.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Preliminary Cost Estimate - Product Cost Collectors (MF30). | The Creation of Preliminary Cost Estimates for Product Cost Collectors screen displays. |  |
| 3 | Enter Relevant Values | Make the following entries and choose Run.Costing Date: Current DatePlant :3310Material:SG012 |  |  |

#### Access Sequence to Staging Areas and Door Determination

Use

In this step, you create the access sequence that defines which combination of fields the system should use while searching for a match between the attributes of an out-bound document and a set of determination rules. The matching determination rule that the system finds is used to determine to which staging area a delivery item should be sent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Define Access Sequence - Staging Areas - Outbound (/SCWM/STADET_ASS_OUT) | The Define Access Sequence - Staging Areas - Outbound screen displays. |  |
| 3. | Create New Entries | First Door DeterminationWarehouse Number: 3350Access Sequence Number: 1Use Carrier: XChoose Save. | Should be created. |  |
| 4. | Create New Entries | Second Door DeterminationWarehouse Number: 3350Access Sequence Number: 2Use Whse Proc. Type: XChoose Save. | Should be created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Anonymous Forecast and MRP Data |  |  |  |
| [Create Planned Independent Requirements](#unique_24) [page ] 34 | Production Planner | Maintain PIRs (F3445) | Independent Requirements for Finished Goods are created. |
| [Material Requirements Planning at Plant Level](#unique_25) [page ] 35 | Production Planner | Schedule MRP Runs (F1339) | MRP run executed for Finished Goods and its component materials. |
| [Evaluate Stock/Requirements Situation (Optional)](#unique_26) [page ] 37 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned materials are analyzed. |
| Procurement of Raw Material: |  |  |  |
| [Convert Purchase Requisitions to Purchase Orders](#unique_27) [page ] 39 | Purchaser | Process Purchase Requisitions (F1048A) | A list of PurchaseRequisitions is displayed.Source of supply is assigned to Purchase Requisition. Purchase Requisition converted to Purchase Order. |
| [Display Purchase Order](#unique_28) [page ] 41 | Purchaser | Manage Purchase Orders (F0842A) | The Manage Purchase Orders screen is displayed with a list of existing Purchasing Document Items.Check the status of Purchase Order. |
| [Create Inbound Delivery](#unique_29) [page ] 42 | Receiving Specialist | Inbound Deliveries for Purchase Orders (VL34) | Inbound delivery created with reference to purchase Order. |
| [Create Handling Unit (Optional)](#unique_30) [page ] 43 | Warehouse Clerk (EWM) | SAP Fiori App Change Inbound Deliveries - Deliveries (F1706) | The Delivery Items have been removed from the Unpacked Items section. |
| [Post Goods Receipt](#unique_31) [page ] 44 | Warehouse Clerk (EWM) | SAP Fiori App Change Inbound Deliveries - Deliveries (F1706) | Goods receipt posted. |
| [Create Putaway Warehouse Tasks](#unique_32) [page ] 46 | Warehouse Clerk (EWM) | SAP Fiori App Change Inbound Deliveries - Deliveries (F1706) | Able to create Putaway warehouse tasks. |
| [Confirm Warehouse Tasks](#unique_33) [page ] 47 | Warehouse Operative (EWM) | SAP Fiori App Process Warehouse Tasks (F4595) | Able to confirm warehouse tasks |
| [Check Stock Level (Optional)](#unique_34) [page ] 48 | Warehouse Operative (EWM) | Warehouse Monitor (/SCWM/MON) | Storage Bin, Stock level validated for component materials. |
| [Evaluate Stock/Requirements Situation (Optional)](#unique_35) [page ] 50 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned materials are analyzed. |
| [Display Procurement Overview (Optional)](#unique_36) [page ] 52 | Purchaser | Procurement Overview (F1990) | Cards for various procurement documents displayed. |
| Repetitive Manufacturing for Semi-Finished Products |  |  |  |
| [Adjust Planning in Planning Table](#unique_37) [page ] 53 | Production Supervisor - Repetitive Manufacturing | Manage Repetitive Manufacturing (MF50) | You can monitor capacity load utilization of the production lines. |
| [Check Range of Stock Coverage](#unique_38) [page ] 54 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| [Material Staging](#unique_39) [page ] 55 | Production Operator - Repetitive Manufacturing | Stage Materials for Production (MF60) | The Material Staging for Planned Orders screen displays. |
| [Create Staging Warehouse Tasks](#unique_40) [page ] 58 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) | You have created the staging warehouse tasks. |
| [Confirm Staging Warehouse Tasks](#unique_41) [page ] 59 | Warehouse Operative (EWM) | Open Process Warehouse Tasks - Picking (F3880). | You have confirmed the staging warehouse tasks. |
| [Post Goods Issue for Staging](#unique_42) [page ] 60 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) | You have posted the goods issue for staging. |
| [Confirm Repetitive Manufacturing Inclusive Backflush of Materials for (non-JIT)](#unique_43) [page ] 61 | Production Operator - Repetitive Manufacturing | Confirm Repetitive Manufacturing (MFBF) |  |
| [Post Processing of Error Records for non-JIT production](#unique_44) [page ] 63 | Production Operator - Repetitive Manufacturing | Reprocess REM Goods Movements (MF47) |  |
| [Check Material Document (Optional)](#unique_45) [page ] 64 | Warehouse Clerk | Material Documents Overview (F1077) |  |
| [Check Goods Movement Document (Optional)](#unique_46) [page ] 65 | Warehouse Clerk | Warehouse Monitor (/SCWM/MON) |  |
| [Check Warehouse Task](#unique_47) [page ] 65 | Warehouse Clerk | Warehouse Monitor (/SCWM/MON) |  |
| [Confirm Putaway Warehouse Tasks](#unique_48) [page ] 66 | Warehouse Operative (EWM) | Confirm Warehouse Tasks (/SCWM/MONNAV_WT_CONF) |  |
| Production Order Execution Finished Product: |  |  |  |
| [Convert Planned Order to Production Order](#unique_49) [page ] 67 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Planned Orders for Finished Goods are converted to Production Orders. |
| [Maintain Serial Numbers in Production Order](#unique_50) [page ] 68 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Maintain Serial Numbers in Production Order. |
| [Review Production Order](#unique_51) [page ] 70 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | Validate the availability of components used in production order. |
| [Release Production Order](#unique_52) [page ] 72 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | You have released the production order. |
| [Trigger Creation of Production Material Request](#unique_53) [page ] 73 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | You have created a production material request. |
| [Check Production Material Request (Optional)](#unique_54) [page ] 75 | Warehouse Clerk (EWM) | Display Production Material Requests (/SCWM/MONNAV_PMR). | You have verified that the production material request was created successfully. |
| [Create Staging Warehouse Tasks](#unique_55) [page ] 76 | Warehouse Clerk (EWM) | Create Warehouse Tasks - Staging for Production (/SCWM/STAGE) | You have created the staging warehouse tasks. |
| [Confirm Staging Warehouse Tasks](#unique_56) | Warehouse Operative (EWM) | Process Warehouse Tasks (F4595) | You have confirmed the staging warehouse tasks. |
| Post consumption of Components |  |  |  |
| [Confirm Production Operations for Subassembly](#unique_57) | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069). | You posted the consumption of the required components. |
| [Review Production Order (Optional)](#unique_58) [page ] 80 | Production Supervisor - Discrete Manufacturing | Manage Production Operations (F2335) |  |
| [Clear Production Supply Area (Optional)](#unique_59) [page ] 82 | Warehouse Clerk (EWM) | Clear Production Supply Areas (/SCWM/MFG_STAGING_REVERSAL) | You created warehouse tasks to move components from PSA back to the final storage bin. |
| [Confirm Warehouse Task for PSA Clearence (Optional)](#unique_60) [page ] 83 | Warehouse Operative (EWM) | Process Warehouse Tasks (F4595) | You have confirmed the warehouse tasks to move the components back to the final storage bin. |
| [Create Inbound Delivery for Production Order](#unique_61) [page ] 84 | Warehouse Clerk | Post Goods Movement (MIGO) | Inbound delivery for the production order created successfully. |
| [Create Handling Unit](#unique_62) [page ] 85 | Warehouse Clerk (EWM). | Change Inbound Deliveries - Production (F5162). | Handling unit created successfully. |
| [Post Goods Receipt](#unique_63) | Warehouse Clerk (EWM) | Change Inbound Deliveries - Production (F5162) | You have posted the goods receipt for staging. |
| [Create Putaway Warehouse Tasks](#unique_64) | Warehouse Clerk (EWM) | Change Inbound Deliveries - Production (F5162) | Warehouse Tasks are created |
| [Confirm Putaway Warehouse Tasks](#unique_65) | Warehouse Operative (EWM) | Process Warehouse Tasks - Putaway (F4150) | Warehouse tasks are confimed. |
| Quality Inspection |  |  |  |
| [Display Open Inspection Lots (Optional)](#unique_66) [page ] 91 | Quality Technician | Display Inspection Lots - Without Usage Decision (QVM3) | The Inspection Lots without Usage Decision screen displays. |
| [Record Inspection Results](#unique_67) [page ] 92 | Quality Technician | Display Inspection Lots - Without Usage Decision (QVM3). | Inspection Results are recorded |
| [Make Usage Decision](#unique_68) [page ] 94 | Quality Engineer. | Record Usage Decision (QA11) | Usage Decision is made. System creates follow-up WTs |
| [Confirm Putaway Warehouse Tasks](#unique_69) [page ] 96 | Warehouse Operative (EWM) | Process Warehouse Tasks - Putaway (F4150) | Warehouse Tasks are confirmed |
| [Evaluate Stock/Requirements Situation](#unique_70) [page ] 97 | Production Planner | Manage Material Coverage - New Version (F0251A). | Stock/Requirements situation for the planned materials are analyzed. |
| Customer Order Creation and Outbound Delivery Creation |  |  |  |
| [Create Sales Order](#unique_71) [page ] 98 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales order is created. |
| [Create Delivery with Order Reference](#unique_72) [page ] 100 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created for sales order. |
| [Create Pick Warehouse Tasks](#unique_73) [page ] 101 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) | Warehouse Task created for Picking. |
| [Confirm Pick Warehouse Tasks](#unique_74) [page ] 102 | Warehouse Operative (EWM) | Process Warehouse Tasks (F4595) | Picking activity for warehouse task is completed. |
| [Pack Goods into Shipping Handling Units (Optional)](#unique_75) [page ] 104 | Warehouse Operative (EWM) | Pack Outbound Deliveries (F3193) | Shipping Handling units created |
| [Enter Serial Number for Outbound Delivery Order (Optional)](#unique_76) [page ] 105 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) | Serial Number captured in Outbound Delivery. |
| [Print Loading Instruction (Optional)](#unique_77) [page ] 106 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) | Able to preview the loading instruction. |
| [Post Goods Issue](#unique_78) [page ] 107 | Warehouse Clerk (EWM) | Manage Outbound Delivery Orders (F6498) | Goods issue with respect to Outbound Delivery completed |
| Accounts Receivable |  |  |  |
| [Create Billing Document](#unique_79) [page ] 108 | Billing Clerk | Create Billing Documents (F0798) | Billing document is created for the delivery. |
| [Post Incoming Payments](#unique_80) [page ] 109 | Accounts Receivable Accountant | Post Incoming Payments (F1345) . | Incoming Payment is posted. |
| Accounts Payable |  |  |  |
| [Create Supplier Invoice with PO/GR Relation](#unique_81) [page ] 111 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Supplier invoice created in system. |
| [Post Outgoing Payment](#unique_82) [page ] 113 | Accounts Payable Accountant | Post Outgoing Payments (F1612) . | Outgoing Payment is posted. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Anonymous Forecast and MRP Data

#### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Planned Independent Requirements (PIRs). PIRs are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes one or more planned independent requirements can be maintained and included in a requirement plan for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries and choose Go:Material: FG012Plant: 3310Period Indicator: Weekly(W)Version Active: Select all optionsNote Period is set to Week, because it is set in material master of the bearing. | The searched material item displays. |  |
| 5 | Edit PIRs | Select the material item and choose Edit in the upper-right corner of the screen.On the screen, enter quantities per period, for example:PIR: 100 for all 12 periodsMake sure the version is active.Version Active: Yes |  |  |
| 6 | Save PIRs Draft | Choose Save in the bottom right corner of the screen. | The PIRs draft is saved. |  |

#### Material Requirements Planning at Plant Level

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use Material Requirement Planning (MRP) to tailor available capacities and receipts on time to suit requirement quantities. As a result, single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The Make-to-Stock finished goods are planned at plant level. There is now a requirement for FG012 in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: <MRP for FG012 >Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3.Parameters section:Plant: 3310Material: FG012Changed BOM Components: <select>All Order BOM Components: <select>Stock Transfer Materials: <select>Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG012 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate Stock/Requirements Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for FG012.

Prerequisite

Requirement planning is carried out for raw materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage (F2101A) screen displays. |  |
| 3 | Select Material | In the field Material, enter material FG012, RM016, RM021, SG012 and RM015 and choose GO. | Stock Availability situation of all materials FG012, RM016, RM021, SG012 and RM015 will be displayed. |  |
| 4 | Review Stock Availability | Analyze the stock availability situation of materials FG012, RM016, RM021, SG012 and RM015 | Stock availability situation of materials FG012, RM016, RM021, SG012 and RM015 is noted with the data present under First Shortage, Shortage quantity, Shortage Duration (Working Days), Stock availability. |  |
| 5 | Selection of materials | Use the Check box and select the rows which have the Material No FG012, RM016, RM021, SG012 and RM015 and click Manage Materials. | The Material and Material Details subscreens display.Stock/Requirement list for all the selected materials is displayed. |  |
| 6 | Display Planned Order | From the list on the Material sub screen on your left, select the material for which you want to check for the planned order:Material: FG012On the Material Details subscreen, choose PldOrd XXXX in the MRP Element column. You can choose the earliest planned order.Note If no planned orders are generated, it could be because FG012 has sufficient amount of stock in store. In this case, remove some stock. Go back to create PIRs and run MRP again to generate planned orders. If there is no sufficient stock for FG012, system generates planned orders. | The selected planned order details are displayed on pop-up screen.The planned order is generated only when there is shortage for these materials.If you want to display more information of the planned order, choose Open... > Planned Order at the bottom right of the dialog box.Note down the planned order number. |  |
| 7 | Display Purchase Requisition | From the list on the Material sub screen on your left, select the material for which you want to check for the purchase requisition:Material: RM016On the Material Details subscreen, choose PurRqs XXXX in the MRP Element column. You can choose the earliest purchase requisition.The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, purchase requisitions are created for externally procured materials. | The selected purchase requisition details are displayed on pop-up screen.The purchase requisition is generated only when there is shortage for these materials.If you want to display more information of the purchase requisition, choose Open... > Document Info at the bottom right of the dialog box.Note down the purchase requisition number. |  |
| 8 | Display Purchase Requisition | From the list on the Material sub screen on your left, select the following materials for which you want to check for the purchase requisition:Material: RM015Material: RM021On the Material Details subscreen, choose PurRqs XXXX in the MRP Element column. You can choose the earliest purchase requisition. | The selected purchase requisition details are displayed on pop-up screen.The purchase requisition is generated only when there is shortage for these materials.If you want to display more information of the purchase requisition, choose Open... > Document Info at the bottom right of the dialog box.Note down the purchase requisition number. |  |
| 9 | Display Planned Order | From the list on the Material sub screen on your left, select the material for which you want to check for the planned order:Material: SG012On the Material Details subscreen, choose PldOrd XXXX in the MRP Element column. You can choose the earliest planned order.Note If no planned orders are generated, it could be because SG012 has sufficient amount of stock in store. In this case, remove some stock. Go back to create PIRs and run MRP again to generate planned orders. If there is no sufficient stock for SG012, system generates planned orders | The selected planned order details are displayed on pop-up screen.The planned order is generated only when there is shortage for these materials.If you want to display more information of the planned order, choose Open... > Planned Order at the bottom right of the dialog box.Note down the planned order number. |  |

### Procurement of Raw Material

#### Convert Purchase Requisitions to Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to convert assigned purchase requisitions to purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Purchase Requisitions (F1048A) .Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | Process Purchase Requisitions screen is displayed. |  |
| 3 | Search for Purchase Requisition | Enter the Purchase Requisition Number for material RM016 (obtained from the previous step) and choose Go.Note If your purchase requisition number is not displayed in the Filters, choose Adapt Filters. On the Adapt Filters pop-up screen find Purchase Requisition Data choose More Filters. Select Purchase Requisition Number and choose OK. Choose Go.Another option is to search for the purchase requisition by using the material number | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition. | The Purchase Requisition has been selected for source assignment. |  |
| 5 | Assign Source to Purchase Requisition | Choose Show More per Row button on the side of Create Contract. If the Purchase Requisition has been assigned the source, the same is displayed under the Assigned Supplier column, then you do not need to assign source again in this step and proceed to next step.If the purchase requisition has not been assigned to the source, choose Assign Source of Supply, and select Info record (XXXXXX) as the source. | The assignment of one source to the requisition is done. |  |
| 6 | Prepare the Purchase Order | Select the purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order.You can close any warning or error messages that are displayed. | The Purchase Order Preview screen is displayed. |  |
| 7 | Create the Purchase Order | In the New Purchase Order screen, make the following entries:Purchasing Doc. Type: Standard PO.Choose Order. | The purchase order is created. |  |
| 8 | Back to Process Purchase Requisition | Click on Back to go to Process Purchase Requisitions (F1048A). | Purchase Requisition list is displayed again.The Processing Status of Purchase Requisition has been changed to PO created. |  |
| 9 | Convert Purchase Requisition to Purchase Order | Repeat steps 2 to 8 of this process to convert the Purchase Requisition of RM015 to Purchase Order.In step 5, choose Contract (xxxxx) as the source instead of Purchase Info Record if there is no assigned supplier. | The Purchase Order is created. Note the Purchase Order number. |  |
| 10 | Convert Purchase Requisition to Purchase Order | Repeat steps 2 to 8 of this process to convert the Purchase Requisition of RM021 to Purchase Order. | The Purchase Order is created. Note the Purchase Order number. |  |

#### Display Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you view the status of purchase orders created in above step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A). | The Manage Purchase Orders (F0842A)screen is displayed. |  |
| 3 | Search for Purchase Order | Enter the Purchase Order number noted in the earlier step for material RM016 and choose Go. | The Purchase Order is displayed. |  |
| 4 | Check status of Purchase Order | Status of Purchase Order is mentioned under column Approval Status. Check the code present under this column. | The Purchase Order must be in status Approved. |  |
| 5 | Check for confirmation control key in purchase order | Select the purchase order and go into details of purchase order by clicking on > and then go into details of purchase order item by clicking on > and in screen purchase order item, click on tab Supplier confirmation control. Here, for the field Confirmation Control, value of Inbound delivery (0004) must be available. | Purchase order item has confirmation control set with Inbound delivery (0004). |  |
| 6 | Repeat the steps to check the status of remaining Purchase Orders | Repeat step number 2 to 5 for the Purchase Order for material RM015, RM021. Use the Purchase Order number of RM015, RM021 noted in the previous step. | The Purchase Order must be in status Approved and confirmation control set for purchase order item. |  |

If the purchase orders that you have created are to be approved and if you do not know who should approve the purchase orders you created, then you can use the Manage Purchase Orders (F0842A) app to display the created purchase order: Go to the Approval Details tab and check the approvers listed in section . For more information about approving the purchase order, refer to the test script of scope item J45.

#### Create Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist . | The Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Inbound Deliveries for Purchase Orders (VL34) . | The Generation of Inbound Deliveries screen displays. |  |
| 3 | Create Inbound Delivery | Make the following entries then choose Execute:Document Number: XXX (Enter the purchase order number created in previous step for material RM016.)Delivery Date: XXX Delete the default date and enter the delivery date in purchase order.Test Run: uncheckedThe Inbound Delivery Number is displayed, write it down for further use. | A new Inbound Delivery is created.The Inbound Delivery Number is displayed. |  |
| 4 | Repeat step 3 to create inbound delivery for remaining purchase order.. | Repeat step 3 to create inbound delivery for the purchase order created for materialsRM015 and RM021, by entering the Purchase Order number of RM015 and RM021 respectively. | A new Inbound Delivery is created.The Inbound Delivery Number is displayed.Note the Inbound Delivery document number. |  |

#### Create Handling Unit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Clerk (EWM) chooses the delivery. He or she chooses the Unpacked Items tab and creates handling units.

If the products have the C-Serial Number Profile (Serialization in Stock) assigned and are to be packed into HUs, you can assign Serial Numbers in this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Change Inbound Deliveries - Deliveries (F1706). | The Change Inbound Deliveries - Deliveries (F1706) screen appears. |  |
| 3. | Choose Filters | On the Change Inbound Deliveries screen, choose Adapt Filters. | The Filters dialog box appears. |  |
| 4. | Enter Purchase Order Number | On the Filters dialog box, make the following entries:Purchase Order: <your purchase order number>Delivery Date: < Purchase Order planned delivery date > |  |  |
| 5. | Choose Go | Choose Go. | The Change Inbound Deliveries screen appears and your Inbound Delivery is displayed. |  |
| 6. | Choose Inbound Delivery | On the Change Inbound Deliveries screen, choose your Inbound Delivery. | Your Inbound Delivery is displayed. |  |
| 7. | Select Unpacked Items | On the Change Inbound Deliveries screen in the Items section, choose the Unpacked Items tab. |  |  |
| 8. | Choose Create HU | Choose Create HU. |  |  |
| 9. | Enter Packaging Material and Number of HUs | On the Create Handling Unit dialog box, make the following entries:Pack. Material: PMPALLET.Number of HUs: <number of handling units>. |  |  |
| 10. | Choose Create | Choose Create. | The Change Inbound Deliveries screen appears.The Delivery Items have been removed from the Unpacked Items section. |  |
| 11. | Note Down your Delivery Number | Note down your delivery number for testing purposes. |  |  |
| 12. | Repeat the steps for creating HU for other material | Repeat the steps 2 to 10 to create HU for Inbound delivery of remaining Material RM015 and RM021 that you have created . | HU created successfully for Inbound delivery of remaining raw materials. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods receipt is being posted. SAP S/4HANA Cloud Public Edition system is being updated accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Change Inbound Deliveries - Deliveries (F1706). | The Change Inbound Deliveries - Deliveries (F1706) screen appears. |  |
| 3. | Choose Filters | On the Change Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
| 4. | Enter Purchase Order Number | On the Adapt Filters dialog box, make the following entries:Planned Dlv. Date: <your planned delivery date>.Purchase Order: <your purchase order number> for RM016. |  |  |
| 5. | Choose Go | Choose Go. | The Change Inbound Deliveries screen appears and your Inbound Delivery is displayed. |  |
| 6. | Choose Inbound Delivery | On the Change Inbound Deliveries screen, choose your Inbound Delivery. | Your Inbound Delivery is displayed. |  |
| 7. | Choose Delivery Items | On the Change Inbound Deliveries screen, choose your Delivery Items. |  |  |
| 8. | Post Goods Receipt | Choose Goods Receipt. | The following system message appears:Goods receipt posted. |  |
| 9. | Repeat the process for RM015 | Repeat the steps 2 to 8, to perform goods receipt for RM015. While repeating the steps, in step number 4, enter the purchase order number of RM015. | Goods Receipt is posted for RM015 material. |  |
| 10. | Repeat the process for RM021 | Repeat the steps 2 to 8, to perform goods receipt for RM021. While repeating the steps, in step number 4, enter the purchase order number of RM021. | Goods Receipt is posted for RM021 material. |  |

#### Create Putaway Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) creates warehouse tasks for putaway.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Change Inbound Deliveries - Deliveries (F1706). | The Change Inbound Deliveries - Deliveries (F1706)screen appears. |  |
| 3. | Choose Filters | On the Change Inbound Deliveries screen, choose Adapt Filters. | The Adapt Filters dialog box appears. |  |
| 4. | Enter Purchase Order Number | On the Adapt Filters dialog box, make the following entries:Purchase Order: <your purchase order number> of RM016Delivery Date: < Purchase Order planned delivery date > |  |  |
| 5. | Choose Go | Choose Go. | The Change Inbound Deliveries screen appears and your Inbound Delivery is displayed. |  |
| 6. | Choose Inbound Delivery | On the Change Inbound Deliveries screen, choose your Inbound Delivery. | Your Inbound Delivery is displayed. |  |
| 7. | Choose Delivery Items | On the Change Inbound Deliveries screen, choose your Delivery Items. |  |  |
| 8. | Choose Create Tasks | Choose Create Tasks. | The following system message appears:Tasks created. |  |
| 9. | Choose Warehouse Tasks | In the Delivery Item section, choose Warehouse Tasks. | The warehouse task(s) created is displayed. Make a note of the warehouse task number. |  |
| 10. | Repeat step to create Putaway task for remaining delivery | Repeat the steps 2 to 9, to create Putaway task for RM015.While repeating the steps, in step number 4, enter the purchase order number of RM015. | Putaway task for RM015 is created. |  |
| 11. | Repeat step to create Putaway task for remaining delivery | Repeat the steps 2 to 9, to create Putaway task for RM021.While repeating the steps, in step number 4, enter the purchase order number of RM021. | Putaway task for RM021 is created. |  |

#### Confirm Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Putaway List is printed and handed over to the Warehouse Operative (EWM). The user performs the warehouse tasks and confirms them in the system. Note that he or she can also confirm warehouse tasks using the app Warehouse Monitor (/SCWM/MON) (Business Catalog WM - Monitoring).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Process Warehouse Tasks (F4595). | The Process Warehouse Tasks (F4595) screen appears. |  |
| 3. | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Choose your Warehouse Task: <Your warehouse task number> of RM016.Choose Go. |  |  |
| 4. | View the Destination Bin | Select the warehouse task created in previous step and go into details of the warehouse task to view the destination bin proposed by system. If there is no need to validate destination bin, proceed to step 6. | Screen Warehouse Task Appears. |  |
| 5. | Validate Destination Bin | In screen Warehouse Task, under the tab Movement Data, field Destination Bin is present. Here, the destination bin must not be CL-AREA. If the destination bin appears as CL-AREA, stop executing further steps and contact your administrator. If destination bin is not CL-AREA, then click Confirm. Destination storage type should be SF01. | Destination Bin validated and warehouse task is confirmed. |  |
| 6. | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task confirmed |  |
| 7. | Repeat steps to confirm the second warehouse task | Repeat the steps 2 to 4 to confirm the Putaway task of RM015. While repeating the steps, in step number 3 key in the warehouse task number of RM015. | Warehouse Task of INNER RINGis confirmed. |  |
| 8. | Repeat steps to confirm the third warehouse task | Repeat the steps 2 to 4 to confirm the Putaway task of RM021. While repeating the steps, in step number 3 key in the warehouse task number of RM021. | Warehouse Task of STEEL WIRE is confirmed. |  |

#### Check Stock Level (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display and identify the storage bin where the stock is present and also the stock level.

Prerequisite

Goods receipt posting is carried out for purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk (EWM). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Warehouse Monitor (/SCWM/MON). | The Warehouse Management Monitor SAP - Warehouse Number XXXX screen displays. |  |
| 3 | Check the Storage Bin where stock is present | Select Stock and Bin > Storage Bin > Physical Stock. In the pop-up screen (/SCWM/SAPLSTOCK_OVERVIEW_MON),enter data in the following fields:Product: RM015Storage Type: SF01 (optional)Click Run.In the pop-up screen click YesNote Stock you have posted for components in previous should be available in SF01 storage type. | Screen Physical Stock is displayed.Here, the columnsTy.displays the storage type value.Storage Bin displays the storage bin where the stock is physically present.Product displays the product.Quantity: displays the quantity.Description of Stock Type: displays the stock type |  |
| 4 | Repeat the steps to know the stock details of the other component material | Repeat step 3 with product: RM016 | Screen Physical Stock is displayed.Here, the columnsTy. displays the storage type value.Storage Bin displays the storage bin where the stock is physically present.Product displays the product.Quantity: displays the quantity.Description of Stock Type: displays the stock type |  |
| 5 | Repeat the steps to know the stock details of the other component material | Repeat step 3 with product: RM021 | Screen Physical Stock is displayed.Here, the columnsTy. displays the storage type value.Storage Bin displays the storage bin where the stock is physically present.Product displays the product.Quantity: displays the quantity.Description of Stock Type: displays the stock type |  |

#### Evaluate Stock/Requirements Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for FG012, SG012.

Prerequisite

Requirement planning is carried out for raw materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage (F2101A) screen displays. |  |
| 3 | Select Material | Search the following materials in the Material bar, select both materials and then choose Manage MaterialsMaterial: FG012Material: SG012 | The Material and Material Details subscreens display. |  |
| 4 | Review Stock / Requirements List | Select the corresponding material on the Material screen on the left side. | The detailed stock / requirements list for each material displays. |  |
| 5 | Display Planned Order | From the list on the Material subscreen on your left, select the material for which you want to check for the planned order.Material: FG012Material: SG012On the Material Details subscreen, choose PldOrd XXXX in the MRP Element column.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, planned orders and purchase requisitions are created for both inhouse-produced and externally-procured materials.Depending on the elements created in the MRP run, refer to Procurement of Direct Materials(J45) or Scheduling Agreements in Procurement (BMR) test scripts for processing externally-procured materials. | The selected planned order displays.The planned order is generated only when there is storage for these materials.If you want to display more information of the planned order, choose Open... > Planned Order at the bottom right of the dialog box. |  |
| 6 | Rescheduling Check (Optional) | On the Stock/Requirements List tab, the Rescheduling column displays the rescheduling status of the following MRP elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersIf needed,you can choose the following icons in Rescheduling column for corresponding functions:Reschedule in (bring operation forward if the receipt element lies after the requirement date)Reschedule out (postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment |  |  |

#### Display Procurement Overview (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In a single page, Purchaser can have a look at details of multiple purchasing documents. For example, purchaser can monitor purchase contracts, monitor unsourced purchase requisition items, Monitor overdue purchase order items. Monitor purchase order items by delivery schedule date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Procurement Overview (F1990). | The Procurement Overview (F1990) screen displays. |  |
| 3 | Selection criteria | Enter data in following fields and choose GO.Display Currency: AEDPurchasing Organisation: 3310Objective of this step is to show the inbuilt analytical capabilities in procurement area. Expectation in this step for the tester is to ensure that system displays different procurement object cards and no need to do any additional validation. | System displays multiple purchase cards on the screen.For example:Monitor purchase contracts: Displays the number of purchase contracts (X of XXX) on this card. This card also displays limited number of purchase contract numbers on screen.Monitor purchase requisition items: Displays the number of purchase requisitions (X of XXX) on this card. We can sort it by criteria: Open or unsourced.Monitor Purchase Order Items: Displays the number of purchase orders (X of XXX) on this card. We can sort it by criteria: overdue or in approval.Monitor Supplier confirmations: We can sort it by Missing Confirmation, Delivery Date Variance, Quantity Variance.And other procurement related cards will appear |  |

### Repetitive Manufacturing for Semi-Finished Products

#### Adjust Planning in Planning Table

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to plan the production of materials on the production lines.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Repetitive Manufacturing (MF50). |  |  |
| 3 | Enter Details | On the Planning Table Initial Screen: Change Mode screen, make the following entries:Plant: 3310Under Selection by Production Version section, choose radio button Material and then enter material number：Material: SG012Choose Execute. | The Planning Table for Repetitive Manufacturing: Change Mode screen displays. |  |
| 4 | Change the Quantity | In the Material Data section, change any planned quantities in the row 0001 WINDING.If you want to change the periods in the planning table, choose Menu > View > Period > Week (Month or Day) . | In the Total Capacity Data section, you can monitor capacity load utilization of the production lines.More information about usage of the planning table for capacity planning and planning quantities, please refer to appendix Usage of the Planning Table for planning Production Quantities. |  |
| 5 | Save | Choose Save. |  |  |

Result

Material production is planned on production lines and the planned orders are fixed.

When there are quantity changes, log on the SAP Fiori launchpad as a Production Planner, access the Monitor Material Coverage app, and review the planned order number.

#### Check Range of Stock Coverage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Select Material | Choose Adapt Filters to add the Material filter if not added, enter the following value:Material: SG012Select the material and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 4 | Rescheduling Check (Optional) | In the Stock/Requirements List, the Rescheduling column displays the rescheduling status of the following MRP Elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersYou can choose below icons in the Rescheduling column to perform correspending actions.Reschedule in (Bring operation forward if the receipt element lies after the requirement date)Reschedule out (Postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment | Corresponding actions perform. |  |
| 5 | Review the Status and Coverage Days | Make following entries and choose Refresh:Shortage Definition: Stock Day's Supply |  |  |
| 6 | Return to Home | Choose the Home icon. |  |  |

#### Material Staging

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to stage materials for production. In case there is sufficient stock available on the production storage location 331B, no line items are generated. If you want to print the Pull List, please also execute relevant steps and check printing result.

Prerequisites

Stock must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.Staging Types: SLoc.Level (Activate checkbox)Plant: 3310Selection Horizon for Remts: <A date>Note Requirements falling on a later date will not be taken into account in the pull list.Planned Orders: <Planned Order Number> Access Manage Material Coverage - New Version (F0251A) app as a Production Planner to view the planned order generated for SG012.Bulk Material: <Adapt Indicator if necessary>Choose Global Settings.In the Global Settings dialog box, choose Dialog Control. On the Dialog Control tab, in the logging section, select the display message log automatically checkbox.Choose Continue | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Proposal | Select the required line items from the left-hand margin and choose Replenishment proposal from the Top of the screen. |  |  |
| 5 | Choose Replenishment Elements | Review the staged quantity and choose Replenishment elements. |  |  |
| 6 | Enter Replenishment Storage Location | On the bottom half of the split screen, select the lines and enter the replenishment storage location 335W for material RM021 |  |  |
| 7 | Choose Print | If you want to print the Pull List, you can execute following printing steps, else please go directly to step 13.Choose Print at the upper right of the screen. |  |  |
| 8 | Print List Selection | In the popup window Print List Selection, choose following entries and choose Continue :Print List Selection: Replenishment Proposals | The print list will be displayed. |  |
| 9 | Check Print List | Check the print list, and choose Print at the upper right of the screen. |  |  |
| 10 | Select Output Parameters | In the popup window Print ALV List, choose following entries and choose Continue.Output Device: expand Name of Device list in the system, choose a known device, or the one with exactly the same name with the Queue you created in Preliminary steps, for example, Pull_List_PrintNote if the Output Device does not exist, please wait for some time until it is validPrint Time: Immediately | Message “Spool request (number XXXX) sent to SAP printer XXXX” indicates successful printing. |  |
| 11 | Go Back | Go back to the stage screen before Printing. |  |  |
| 12 | Select Stage | Select the replenishment element in the bottom half of the screen, and choose Stage at the middle of the screen. |  |  |
| 13 | Choose Save | Choose Save. Note down the delivery number. | The log with the following system message appears: EWM release order delivery <delivery number> successfully generated forRM021 |  |
| 14 | Choose Back | Choose Exit in the upper right corner of the screen. | The following system message appears: Data posted successfully. |  |

Result

Missing materials are transferred to the shop floor from the designated storage area.

#### Create Staging Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create pick warehouse tasks for the staging process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Manage Outbound Delivery Orders (F6498) | The Manage Outbound Delivery Orders (F6498) screen displays |  |
| 3 | Enter Warehouse Number | On the Manage Outbound Delivery Orders screen, make the following entries.Warehouse No: 3350. |  |  |
| 4 | Select Filters | On the Manage Outbound Delivery Orders screen, select Adapt Filters. | The Adapt Filters dialog box is displayed. |  |
| 5 | Select Filters | In the Adapt Filters dialog box, find Document Number. Select the checkbox for Document Number and choose OK. | The Document Number filter criteria is displayed on the Manage Outbound Delivery Orders screen. |  |
| 6 | Enter Filter Criteria | On the Manage Outbound Delivery Orders screen, enter your Delivery, and choose Go. |  |  |
| 7 | Create Warehouse Tasks | Mark your outbound delivery and choose Create Pick Warehouse Tasks to create the warehouse tasks. | The following system message appears: Pick warehouse task(s) created. |  |
| 8 | Choose Outbound Delivery Order | Choose your Outbound Delivery Order to find the created warehouse task. | The Outbound Delivery Order details are displayed on the right side of the screen. |  |
| 9 | Choose Warehouse Tasks | Scroll down to the Others section and choose Yes under Process Relevant WTs . | The Process Warehouse Tasks screen is displayed. |  |
| 10 | Note Down Warehouse Task Number | Note down the warehouse task number. |  |  |

#### Confirm Staging Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A put-away list / warehouse tasks list / pick list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks - Picking (F3880). |  |  |
| 3 | Enter your Warehouse Task | On the Process Warehouse Tasks - Picking screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>.Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears:<Warehouse task confirmed>. |  |

#### Post Goods Issue for Staging

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods issue (GI) for the staging outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Manage Outbound Delivery Orders (F6498) | The Manage Outbound Delivery Orders (F6498) screen displays |  |
| 3 | Enter Warehouse Number | On the Manage Outbound Delivery Orders screen, make the following entries.Warehouse No: 3350. |  |  |
| 4 | Select Filters | On the Manage Outbound Delivery Orders screen, select Adapt Filters. | The Adapt Filters dialog box is displayed. |  |
| 5 | Select Filters | In the Adapt Filters dialog box, find Document Number. Select the checkbox for Document Number and choose OK. | The Document Number filter criteria is displayed on the Manage Outbound Delivery Orders screen. |  |
| 6 | Enter Filter Criteria | On the Manage Outbound Delivery Orders screen, enter your Delivery, and choose Go. |  |  |
| 7 | Create Warehouse Tasks | Mark your outbound delivery and choose Post Goods Issue to post goods issue for your delivery. | The following system message appears: Goods issue posted. |  |

#### Confirm Repetitive Manufacturing Inclusive Backflush of Materials for (non-JIT)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity executes multiple activities in a single step, such as finished product goods receipt, backflush of component materials, posting of costs to cost collector, and creation of material and Journal Entry.

Errors can occur in backflushing. For example, there may not be sufficient warehouse stock available or important data, such as the issue storage location, may be missing. You then have the following options:

Make corrections immediately in a component overview.

Backlogs are created for the complete requirement quantities of the components with errors.

You can process these backlogs later. If negative stocks are allowed for the material in the storage location, the system posts negative stock quantities in certain circumstances.

|  |
| --- |
| Note Goods Receipt's Goods Movement Type is 131 and Goods Issue's Goods Movement Type is 261. |

Prerequisite

Planned orders must exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Repetitive Manufacturing role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Repetitive Manufacturing (MFBF). | The REM Confirmation - Transaction Variant: None screen displays. |  |
| 3 | Enter Selection Data | Make the following entries:Assembly backflush: XMake-to-Stock: system proposesPlanned Order: Planned Order Number (from previous step for SG012)Note When the system proposes quantities, change as required.Press Enter. | Note down the Posting Date and Document Date on the screen. |  |
| 4 | Post with Corrections | Choose Post with Correction.Select the production version, if prompted. |  |  |
| 5 | Post | Choose Post. |  |  |

|  |
| --- |
| Note The app Confirm Repetitive Manufacturing (MFBF) can be used to perform Reporting Point (RP) confirmation and backflush.Process step:Reporting point confirmation related steps can be performed by logging in as the Production Operator - Repetitive Manufacturing role.To perform reporting point confirmation in the app, enable the indicator for RP Backflush and provide the operation number of the reporting point in the field Reporting Point.Purpose of RP confirmation:Reporting Points are operations in the routing where milestone confirmation is enabled using the appropriate control key.Reporting Point (RP) confirmation allows users to:Record and calculate the work in process quantitiesRecord component consumption at a specific operation (reporting point)Record scrap quantities at a specific operation (reporting point)Prerequisites for RP confirmation:Enable RP backflush indicator during configuration of the appropriate REM profile and assign the REM profile to the material master. The REM profile can be adjusted to make RP backflush optional or mandatory.In routing, use control keys that have milestone confirmation enabled and assign the routing to appropriate production version.A standard cost estimate or cost estimate based on production version is completed for the material.Additional processes related to reporting point confirmation available for this role are:Use the app Display Reporting Point Quantity (MF26) to provide an overview of confirmation quantities at reporting points.Use the app Reset Reporting Point Confirmations (MF4R) to reverse the confirmation and backflush done at a reporting point. |

Result

Finished Goods material is received into stock and Semi finished materials are issued from stock. To view the Material document, log on the SAP Fiori Launchpad as the Warehouse Clerk, then open Material Documents Overview.

#### Post Processing of Error Records for non-JIT production

Purpose

This process step shows you how to use this function to create a list of components that have to be postprocessed to post process backlogs from backflushing.

Prerequisites

Material movements are missing for previous backflush operations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Reprocess REM Goods Movements (MF47). | The Postprocessing List for Components on Line: Initial Screen screen displays. |  |
| 3 | Enter Selection Data | Make the following entries and choose Run:Plant: 3310Posting Date and Document Date could be retrieved from previous steps. | The system displays a list of all assemblies that correspond to the selection criteria and that have components to be postprocessed. This list is sorted by assemblies and production versions. If you have to correct the components or if you want to check availability, select the appropriate assembly and choose Change Selected Postprocessing Recs. The system displays the components of the selected assembly. |  |
| 4 | Save | Review the generated list, and then choose Post. |  |  |

#### Check Material Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for checking material document posted during repetitive manufacturing backflush.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Open the SAP Fiori Launchpad with the Warehouse Clerk role. | The SAP Fiori launchpad displays. |  |
| 2 | Open Management Document Overview | Open Material Documents Overview (F1077). | The Material Documents Overview displays. |  |
| 3 | Search for Material Document | Search material documents using different criteria. Select Adapt Filters and all basic filters are displayed. Enter the entries accordingly, then choose Go.For example:Stock Change: AllPosting Date: <Date repetitive manufacturing was confirmed for SG012>Material: SG012Choose the row of a certain material document to view details. | The relevant Material Documents / Material Document items are shown.The GR with movement type 131 and the GI with movement type 261 are posted synchronously in one material movement document. |  |

#### Check Goods Movement Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for checking goods movement document of goods receipt posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Fiori Warehouse Monitor (/SCWM/MON) |  |  |
| 3. | Select the node | On the Warehouse Management Monitor SAP - Warehouse Number xxxx screen, choose Documents > Warehouse Tasks and doubleclick on the node. |  |  |
| 4. | Enter the selection data | Make the following entries:Whse Proc. Category: 5 Goods Receipt PostingProduct: SG012 .Choose Run. | The goods receipt is reflected in a warehouse task of Warehouse Process Category 5 (Goods Receipt Posting) for the finished product SG012.The goods movement document is reflected in a warehouse task of Warehouse Process Category 6 (Goods Issue Posting) for Raw Material RM021. |  |

#### Check Warehouse Task

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for checking warehouse task from the production goods receipt storage type to the final storage type.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Open Warehouse Monitor (/SCWM/MON) |  |  |
| 3. | Select the node | On the Warehouse Management Monitor SAP - Warehouse Number xxxx screen, choose Documents > Warehouse Task and doubleclick on the node. |  |  |
| 4. | Enter the selection data | Make the following entries:Whse Process Type: S117.Product: SG012.Choose Run. | The warehouse task for synchronous goods movement during backflush for repetitive manufacturing should be displayed. |  |

#### Confirm Putaway Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A putaway list / warehouse tasks list / pick list is printed and handed over to the Warehouse Operative (EWM) who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Confirm Warehouse Tasks (/SCWM/MONNAV_WT_CONF) |  |  |
| 3 | Enter Selection Data | Make the following entries:Warehouse Task: <Warehouse Task Number>Use the warehouse task number that was created in the previous step.Choose Run. | The Confirm Warehouse Task screen displays. |  |
| 4 | Select Warehouse Task | Select your Warehouse Task. |  |  |
| 5 | Confirm Warehouse Task | Choose More Methods > Confirm WT in Background. | The log is displayed, stating that your warehouse task was confirmed. |  |

### Production Order Execution Finished Product

#### Convert Planned Order to Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to convert planned order to production order.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |  |
| 3 | Select Criteria | In the Search bar, enter FG012 and choose GO. | Stock Availability situation of all materials starting with FG012 will be displayed. |  |
| 4 | Selection of Materials | Use the Check box and select the row which has Material No as FG012 and click on Manage Materials present at the right side corner of the screen. | The Material and Material Details sub screens display.Stock/Requirement list for the selected material is displayed. |  |
| 5 | Convert Planned Order to Production Order | For the planned order (PldOrd XXXX) noted in previous section, select Convert from Edit dropdown list in the Action column.In the Convert Planned Order XXXX dialog box, choose Convert to Production Order radio button, confirm End Date and Quantity. Choose OK.Note Select the planned order which is available in next calendar week. | The production order is created. Note the Production Order number. |  |

#### Maintain Serial Numbers in Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To Maintain serial numbers in the production order.

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | Screen Manage Production Orders (F2336)is displayed. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. In the Area of Responsibility dialog box, choose Production Supervisor, check if this entry displays and choose OK:3310MTS DI - Valuated (YB1)Choose the toggle button under AOR Status to toggle the entries and assign the selected entry; choose the toggle button to unassign any other plant entries. Choose Back |  |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, choose More filters. Select Material and Production Plant and choose OK. Choose Go.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: FG012Production Plant: 3310 | The Material and Production Plant fields are added to the filter bar.Corresponding orders display. |  |
| 5 | Check details of Production Order | Select the production order to be reviewed (which we have created in the previous step).Choose Edit in the top right corner. | The screen Production Order Change: Header is displayed.Details of selected production order is displayed. |  |
| 6 | Maintain Serial numbers | Click on Header > Serial numbers | Pop-up screen: Maintain Serial numbers appears |  |
| 7 | Maintain Serial numbers | On the pop-up screen: Maintain Serial Numbers , click on Create serial numbers automatically.System should generate serial numbers and populate them in the column ‘Serial Number’. Click on Select all and the click on Continue (Tick Icon).Note down the serial numbers … | Serial numbers maintained in the production Order.Serial numbers are noted. |  |
| 8 | Save the Production Order | Click on the Save button present at the bottom of the screen. | System gives a message Order number XXXX saved. |  |

#### Review Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To review the production order details, schedule production order, perform availability check on components of production order.

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. In the Area of Responsibility dialog box, choose Production Supervisor.Check if only this entry displays, and choose OK:Plant 1 AE 3310MTS DI- Valuated (YB1)Choose + to select this entry if not displayed; choose the Delete icon to remove any other plant entries and then choose OK.Choose OK again to come back to Manage Production Orders screen | The Manage Production Order screen displays. |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, choose More Filters. Select Material and Production Plant and choose OK. Choose Go.Status: CreatedMaterial: FG012Production Plant: 3310 | The Material and Production Plant fields are added to the filter bar.The searched order displays. |  |
| 5 | Check details of Production Order | Select the production order to be reviewed (created in the previous step). If there are issues for the selected production order, the issues will be shown under the Issues column.Choose Edit Order in the top right corner. | The Production Order Change: Header screen is displayed.Details of the selected production order are displayed. |  |
| 6 | Schedule, cost and availability check functions on Production Order | On the Production Order Change: Header screen, click Schedule Order > Cost Order > Material. | For Schedule Order, the Scheduling is carried out message is displayed.Upon click of Cost Order, system should give a message that Costs determined --> see cost display.Upon click of Material, if all component materials are available, system should give a message that All checked materials in order xxxx are availableIf there are missing components, system displays the Availability Check screen that lets you know that there are missing components. If material RM015, RM016 or SG012 is mentioned in missing parts, then accordingly the stock need to be procured or produced. If sufficient stock is available then perform staging mentioned in next section |  |
| 7 | Save the Production Order | Click Save. | System gives a message Order number XXXX saved. |  |

#### Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A release at order operation level results in the order and all its operations being released. The order and the operations receive the REL (released) status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing | The SAP Fiori Launchpad opens. |  |
| 2 | Access App | Open Manage Production Orders (F2336). | The Manage Production Orders (F2336) screen appears. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | On the Manage Production Orders screen, maintain the following entries:Check the default area of responsibility (supervisor) by choosing your avatar (from the top-right corner) and selecting App Settings > Area of Responsibility > Production Supervisor and choose Go. Check that only this entry is assigned:Plant 1(AE) 3310.MTS DI - Valuated (YB1). | If the Plant 1(AE)3310/MTS DI - Valuated (YB1) entry in the Plant / Prodn Supervisor Combinations section is not assigned, adapt the filter settings. Choose Go. Select the AOR Status checkbox . For other plant entries, unselect the AOR Status checkbox. Choose Back in the top left corner to return to the Manage Production Orders screen. |  |
| 4 | Select Production Order | On the Manage Production Orders(F2336) screen, enter the following search conditions as a filter.Choose Adapt Filters to display more selection filters. In the Adapt Filters dialogbox, choose Group View on the top right corner. Expand the Production Orders node. Select the checkbox for Material and Production Plant and choose OK. The Material and Production Plant fields are then added to the filter bar.Status: Created.Material: FG012.Production Plant: 3310.Choose Go to execute. | The Manage Production Orders(F2336) screen appears. |  |
| 5 | Select Order | On the Manage Production Orders(F2336) screen, select your production order by choosing the checkbox beside the order number.Choose Edit. | The Production order Change: Header screen appears.Note down your production order number: ______________ |  |
| 6 | Execute Release | Choose Menu > Functions > Release . | The Release Order dialog box appears. |  |
| 7 | Release Order | Choose Release Order. | A system message tells you that the release has been carried out, and refers to the log. |  |
| 8 | Save | Save your entries. | A system message tells you that the corresponding order number has been saved. |  |

#### Trigger Creation of Production Material Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you trigger the creation of the production material request by executing the WM material staging function. The production material request is a representation of the manufacturing order in warehouse management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Supervisor - Discrete Manufacturing | The SAP Fiori Launchpad opens. |  |
| 2 | Access App | Open Manage Production Orders (F2336). | The Manage Production Orders (F2336) screen appears. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | On the Manage Production Orders screen, maintain the following entries:Check the default area of responsibility (supervisor) by choosing your avatar (from the top-right corner) and selecting App Settings > Area of Responsibility > Production Supervisor and choose Go. Check that only this entry is assigned:Plant 1( AE )3310.MTS DI - Valuated (YB1) | If the Plant 1( AE) 3310/MTS DI - Valuated (YB1) entry in the Plant / Prodn Supervisor Combinations section is not assigned, adapt the filter settings, choose Go and select the AOR Status checkbox. For other plant entries, unselect the AOR Status checkbox. Choose Back in the top left corner to return to the Manage Production Orders screen. |  |
| 4 | Select Production Order | On the Manage Production Orders(F2336) screen, enter the following search conditions as a filter.Choose Adapt Filters to display more selection filters. In the Adapt Filters dialog box, choose Group View on the top right corner. Expand the Production Orders node. Select the checkbox for Material and Production Plant and choose OK. The Material and Production Plant fields are then added to the filter bar.Status: Released.Material: FG012.Production Plant: 3310.Choose Go to execute. | The Manage Production Orders(F2336) screen appears. |  |
| 5 | Select Order | On the Manage Production Orders(F2336) screen, select your production order by choosing the checkbox beside the order number.Choose Edit. | The Production order Change: Header screen appears. |  |
| 6 | Execute Release | On the Production order Change: Header screen, choose Menu > Functions > WM Material Staging > Execute . | The following system message is displayed: Material staging was executed successfully. |  |
| 7 | Save | Choose Save. | A dialog box with the following system message appears: Order number <your order number> saved. |  |

#### Check Production Material Request (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you verify that the production material request was created successfully.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad opens. |  |
| 2 | Access App | Open Display Production Material Requests (/SCWM/MONNAV_PMR). | The Production Material Request screen appears. |  |
| 3 | Set Filter Criteria | On the Production Material Request screen, choose Set Selection Criteria. | A dialog box with filter options appears. |  |
| 4 | Set Filter Criteria | In the dialog box with the filter criteria, make the following entries:Manufacturing Order: <your order number>Choose Run. | The Production Material Request screen appears.The Production Material Request associated with your manufacturing order is listed. |  |
| 5 | Select PMR | On the Production Material Request screen, select the line item with your production material request and choose Mat.Req.Items. | The Material Request Items section appears on the bottom half of the screen. |  |
| 6 | Verify Items | On the Production Material Request screen, in the Material Request Itemssection,Verify that there is a line item for each component RM015 ,RM016, and SG012 as component for FG012 with the corresponding staging methods and associated staging bins. | There is a line item for each component. |  |

#### Create Staging Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create warehouse tasks for the staging process. The warehouse tasks are for moving the components from the storage bin to the production supply area.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad opens. |  |
| 2 | Access App | Open Create Warehouse Tasks - Staging for Production (/SCWM/STAGE). | The Schedule Staging for Production screen, appears. |  |
| 3 | Make Entries | On the Schedule Staging for Production screen, make the following entries:Warehouse Number: 3350Manufacturing Order: <your manufacturing order>Select the Period ends at specific time checkbox.In the Date and Time input fields, enter values after the requirement date of your manufacturing order.Deselect the Test Mode checkbox.Choose Execute. | The Display Logs screen appearsOn the bottom section, the following system messages appear for each warehouse order created:Warehouse order <warehouse order number> createdNote down the warehouse order numbers. |  |

#### Confirm Staging Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A warehouse tasks list / pick list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks (F4595). | The Process Warehouse Tasks (F4595) screen appears. |  |
| 3 | Enter your Warehouse Order | On the Process Warehouse Tasks screen, make the following entries:Warehouse Order: <Warehouse Order Number from previous step>Choose Go. | The Warehouse Tasks associated with your warehouse order are displayed. |  |
| 4 | Choose Warehouse Task | On the Process Warehouse Tasks screen, in the Warehouse Tasks section, choose a Warehouse Task to go into the warehouse task details. | The Warehouse Task screen is displayed. |  |
| 5 | Maintain Pick-HU | On the Warehouse Task screen, in the Movement Data tab, choose Maintain Pick-HU. | The Maintain Pick-HU dialog box is displayed. |  |
| 6 | Create Pick-HU | In the Maintain Pick-HU dialog box, select Create Pick-HU. | The Create Pick-HU dialog box is displayed. |  |
| 7 | Enter Packaging Material | In the Create Pick-HU dialog box, enter a Packaging Material, for example PMPALLET and choose Create. | The Maintain Pick-HU dialog box with the newly created Pick-HU is displayed. Note down the HU number. |  |
| 8 | Return to Warehouse Task Screen | In the Maintain Pick-HU dialog box, select Close. | The Warehouse Task screen is displayed and the Destination Handling Unit dropdown menu is populated with the HU number. |  |
| 9 | Confirm Warehouse Task | On the Warehouse Task screen, choose Confirm. | You have confirmed the warehouse task.The following system message appears:Warehouse task <ware-house task number> confirmed. |  |
| 10 | Confirm the remaining Warehouse Task | Repeat steps 4 to 9 for the remaining WTs created in previous step. |  |  |

|  |
| --- |
| Note If you prefer to execute this step with Radio Frequency Devices please refer to the respective process step 'Variant 2: with Radio Frequency Devices' in Scope Item Warehouse Advanced Production Integration (6NI).For working with Mobile RF Devices, make sure all the steps as described in the setup instruction guide for scope item 63W - Mobile RF Devices in Warehousing with Production Integration have been performed. |

#### Post Consumption of Components

In this section, you post the consumption of the components for your production material request/ production order. You can either post consumption by confirming the production order operations, if the components are set up to backflush or consume the components directly in your warehouse. In case you are testing the process variant with backflush components (materials RM015,RM016 and SG012) , proceed with the Confirm Production Operations for Subassembly step.

##### Confirm Production Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of orders, operations, sub-operations, and individual capacities. It's an instrument for controlling orders. This process step shows you how to confirm subassembly production order operations for semifinished material FG012. A goods movement document is generated when the last operation is confirmed. The backflush is carried out together with the confirmation steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <Production Order Number for FG012>Operation: <operation number> for example, <0010> |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <Quantity of prod. order less scrap>Scrap: <scrap amount> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list.Note The system shows you an overview materials table, for which the material withdraws are done along with operation confirmation.The materialRM015,RM016 and SG012,areset for backflush (in material master) for withdraws to be done automatically after the operation is confirmed. |  |  |
| 6 | Enter Activities Data and Save | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time>For partial confirmation, choose Post.For final confirmation, choose Post and Complete. | Confirmation is made. |  |
| 7 | Repeat Steps | Go back and repeat steps 3 to 6 for Operation0020 and 0030. |  |  |
| 8 | Good Issue | When all operations are finally confirmed, all materials consumed in production are backflushed. | Backflush for all consumed materials is done. |  |

##### Review Production Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display and check the production order for finished goods after its release or confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Operations (F2335) | The Manage Production Operations screen displays. |  |
| 3 | Select Production Order | On the Manage Production Operations screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, select Material and Production Plant and choose OK.Enter the following filters criteria and choose Go.Material: FG012Plant: 3310 | The Material and Plant fields are then added to filter bar.Selected order displays.Operations of production order must be in status Confirmed. |  |
| 4 | Check Detailed Operations Status | Check detailed information for selected production operations.Operation Issue:Empty if there is no production order issue.Delay or Missing Components / PRT issue or Quantity Deviation / Quality Issue information shows if relevant issue exists.Components:Material, total quantity and Issued / open quantity information for order components displays.Order Schedule:Detailed operation information with relevant work center, confirmed quantity, start and end time displays.Work Center Schedule:The relevant order covering the same work center capacity (operation is partially confirmed) displays.Operations not Started:The relevant order that would cover the same work center capacity (operation is released) displays.Confirmation:Detailed confirmation information with Yield, Scrap, Rework quantity displays if confirmation has been executed.Inspection:Detailed inspection lots information displays if existed. |  |  |

#### Clear Production Supply Area (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create warehouse tasks to move material, which hasn’t been consumed during the production process from the production supply area back to the final storage bin.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori Launchpad opens. |  |
| 2 | Access App | Open Clear Production Supply Areas (/SCWM/MFG_STAGING_REVERSAL). | The Clear Production Supply Areas (/SCWM/MFG_STAGING_REVERSAL) screen appears. |  |
| 3 | Choose Settings | On the Clear Production Supply Area screen, choose Settings on the top left. | The Maintain Default Values dialog box appears. |  |
| 4 | Apply Settings | In the Maintain Default Values dialog box, make the following entries:Warehouse Number: 3350Hours in Past (Consumption Posting): 500Choose Enter. | The Clear Production Supply Area screen appears. |  |
| 5 | Enter Search Criteria | On the Clear Production Supply Area - Warehouse 3350 screen, in the Search Criteria section, set the following criteria:From the left dropdown list, select Production Supply Area as search criteria.From the dropdown list in the center, select equals to as search operator.In the right value field, enter PSA_03 /3310 using the value help.Choose Search. | In the bottom half of the screen, in the Stock Without Released Production Material Request section, the stock items matching your search criteria appear. |  |
| 6 | Release Stock from PMR (optional) | On the Clear Production Supply Area - Warehouse 3350 screen, in the Stock Without Released Production Material Request Section, select the stock items you want to release from the PMR.Choose Release Reference Document. | The following system message appears: <number of selected stock items> stock items released.The selected stock items no longer have references to a production material request or manufacturing order. |  |
| 7 | Create WT | On the Clear Production Supply Area - Warehouse 3350 screen, in the Stock Without Released Production Material Request section, select the stock items.Choose Create Warehouse Task. | The following system message appears: Warehouse task <WT number> created.Note down the warehouse task number |  |

#### Confirm Warehouse Task for PSA Clearence (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A Putaway List is printed and handed over to the Warehouse Operative (EWM). The user performs the warehouse tasks and confirms them in the system. Note that he or she can also confirm warehouse tasks using the app Warehouse Monitor (/SCWM/MON) (Business Catalog WM – Monitoring).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to the SAP Fiori Launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open the SAP Fiori app Process Warehouse Tasks (F4595). | The Confirm Warehouse Tasks screen appears. |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <Your warehouse task number>.Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears: Warehouse task confirmed. |  |

|  |
| --- |
| Note If you prefer to execute this step with Radio Frequency Devices please refer to the respective process step 'Variant 2: with Radio Frequency Devices' in Scope Item Warehouse Advanced Production Integration (6NI).For working with Mobile RF Devices, make sure all the steps as described in the setup instruction guide for scope item 63W - Mobile RF Devices in Warehousing with Production Integration have been performed. |

#### Create Inbound Delivery for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the Warehouse Clerk creates the inbound delivery for the production order by posting the goods receipt (GR) for the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Post Goods Receipt | Choose Goods Receipt and Order.Enter the released production order that you’ve created in the previous step.Goods Movement Type: 101 (GR Goods Receipt).Choose Enter. Then, choose Where tab.Storage Location: 335W.Check Item Ok.Choose Post.Note An additional storage location 335I and the corresponding availability group 002 can be introduced in the Cloud WM as an optional setup. Compared to the single storage location 335W / availability group 001 setup, the new setup can help distinguish stock that is still in the process of putaway and that is already in the warehouse.For example, the storage location 335I is used as the goods receipt storage location. During the goods receipt process, the stock remains in the storage location 335I and isn't available for sale (Stock Type F0 – Unrestricted Use in Putaway) until the putaway warehouse task(s) is/are confirmed. Once the putaway is finished, the stock is automatically posted to the storage location 335W and becomes available for sale (Stock Type F – Unrestricted Use in Warehouse).To enable the 335I storage location / availability setup, there are manual setup steps to be performed according to the instructions provided in the Warehouse Management Setup Guide. For more information, see chapter Additional Manual Configuration. |  |  |
| 4 | Note Down Inbound Delivery Number | Note down the inbound delivery number. |  |  |

#### Create Handling Unit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the Warehouse Clerk (EWM) selects the delivery, selects the Unpacked Items tab and creates handling units (HUs). He or she can print the HU Label by navigating from the app to the monitor.

|  |
| --- |
| Note Note that handling unit management is not a general prerequisite of production integration. In this example process, creating handling units is mandatory only due to the bulk storage type to which material SG012 is put away to. Therefore, using material SG012, you create handling units and pack your material in this step.In case you want to store unpacked material, you should use the general storage type, the standard storage type, or your own storage type without HU requirements instead.Skip this step if you are using configurable materials and material variants. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Change Inbound Deliveries - Production (F5162). |  |  |
| 3 | Select Filters | On the Change Inbound Deliveries screen, select Adapt Filters. | The Adapt Filters dialog box is displayed. |  |
| 4 | Enter Order Number | In the Adapt Filters dialog box, make the following entries:Example Manufacturing Order: <your production order number>.Adjust the Planned Delivery Date/Time if necessary. |  |  |
| 5 | Choose Go | Choose Go. |  |  |
| 6 | Select Inbound Delivery | On the Change Inbound Deliveries screen, select your Inbound Delivery. | Your Inbound Delivery is displayed. |  |
| 7 | Select Unpacked Items | In the Items section, select the Unpacked Items tab. |  |  |
| 8 | Select Create HU | Choose Create HU. |  |  |
| 9 | Enter Packaging Material and Number of HUs | In the Create Handling Unit dialog box, make the following entries:Example Pack. Material: PMPALLET.Number of HUs: <number of handling units>. |  |  |
| 10 | Choose Create HU | Choose Create. | The Change Inbound Deliveries (Original) screen is displayed.The Delivery Items have been removed from the Unpacked Items section. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) posts the goods receipt for the inbound delivery of the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Inbound Deliveries – Warehouse (F7922). |  |  |
| 3 | Select Filters | On the Manage Inbound Deliveries screen, select AdaptFilters. | The Adapt Filters dialog box is displayed. |  |
|  | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Delivery Date/TimeManufacturing Order.Choose OK. |  |  |
| 5 | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Manufacturing Order: <your production order number>.Adjust the Planned Delivery Date/Time, if necessary.Choose Go. | Your inbound delivery is displayed. |  |
| 6 | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your Inbound Delivery. |  |  |
|  | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
| 8 | Select Delivery Items | On the Manage Inbound Deliveries screen, select your Delivery Items. |  |  |
| 9 | Optional: Enter Serial Number | Enter the serial number, if required. |  |  |
| 10 | Post Goods Receipt | Choose Goods Receipt. | A system message tells you that the goods receipt is posted. |  |

#### Create Putaway Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Clerk (EWM) creates warehouse tasks for putaway.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Inbound Deliveries – Warehouse (F7922). |  |  |
| 3 | Select Filters | On the Manage Inbound Deliveries screen, select Adapt Filters. | The Adapt Filters dialog box is displayed. |  |
|  | Select Fields for Filter | On the Adapt Filters dialog box, make sure the following fields are selected for the current filter:Planned Delivery Date/TimeManufacturing Order.Choose OK. |  |  |
| 5 | Search for Inbound Delivery | On the Manage Inbound Deliveries screen, make the following entries:Manufacturing Order: <your production order number>.Adjust the Planned Delivery Date/Time if necessary.Choose Go. | Your Inbound Delivery is displayed. |  |
| 6 | Select Inbound Delivery | On the Manage Inbound Deliveries screen, select your Inbound Delivery. |  |  |
| 7 | Choose Details | Choose button Details. | Inbound delivery details are displayed. |  |
| 8 | Select Delivery Items | Select your Delivery Items. |  |  |
| 9 | Choose Create Tasks | Choose Create Putaway Tasks Automatically. | A system message tells you that the tasks have been created. |  |
| 10 | Choose Warehouse Tasks | In the Items section, choose Yes in the Open PutawayWarehouse Tasks field. | The warehouse task(s) created is displayed. Make a note of the warehouse task number. |  |

#### Confirm Putaway Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A putaway list / warehouse tasks list / pick list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks - Putaway (F4150) |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose ConfirmNote If you have the two availability groups setup for your warehouse, as soon as the putaway warehouse tasks are confirmed, the system automatically posts the stock type for this stock from ‘Unrestricted Use in Putaway (F0)’ to ’Unrestricted Use in Warehouse (F)’. | The following system message appears:Warehouse task confirmed. |  |

|  |
| --- |
| Note If you prefer to execute this step with Radio Frequency Devices please refer to the respective process step 'Variant 2: with Radio Frequency Devices' in Scope Item Warehouse Advanced Production Integration (6NI).For working with Mobile RF Devices, make sure all the steps as described in the setup instruction guide for scope item 63W - Mobile RF Devices in Warehousing with Production Integration have been performed. |

### Quality Inspection

#### Display Open Inspection Lots (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to display the open inspection lot list via the Manage Inspection Lots app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Inspection Lots - Without Usage Decision (QVM3). | The Inspection Lots without Usage Decision screen displays. |  |
| 3 | Enter Filter FIelds | In screen Inspection Lots without Usage Decision, make the following entries and choose Run:Lot created: Ensure correct valid to date (for example: 10 days in future as the valid to date)Plant: 3310Insp. Lot Origin: 17Material: FG012 | Screen Inspection Lots without Usage Decision is displayed.Inspection lots without usage decision are displayed as per the selection criteria. |  |
| 4 | Select Inspection Lot | In the inspection lot list, click the inspection lot that was created before. | Screen Display Inspection lot is displayed. |  |
| 5 | Check Inspection Lot | Under tab Data for Lot Origin, in section Data for Order, verify the referenced order number and delivery number. | The order number, delivery number from which the inspection lot originates is displayed. |  |

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The quality technician executes the quality inspection and records inspection results for the inspection lot.

Procedure

Record Inspection Results for one Inspection Lot

If inspection results shall be recorded for one or only a few inspection lots, execute the following process flow:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A) | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.If Order is not displayed in the Filters, choose Adapter Filters. On the popup screen Adapter Filters, select Order and choose OK. Choose Go.Plant: 3310Material: FG012Order: <from previous step>. |  |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot.Choose Record Multiple Results at top of the table. |  |  |
| 5 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive ResultSurface: Code Group - Code: SURFACE 0020 (Smooth)Negative ResultSurface: Code Group - Code: SURFACE 0010 (Rough) | For the qualitative characteristic (surface) the search help is needed to select a value. For the quantity characteristic (length) a number can be entered directly.The valuation and close are performed automatically, and the status is set to Valuated.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. As well a number of nonconforming objects can be maintained directly in the respective fields for every inspection characteristic. |  |
| 6 | Save Inspection Lot | Choose Save. | The inspection lot is saved. QM Inspection for manufactured goods has been performed and result recorded. |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for several inspection lots at the same time, execute the following process flow.

|  |
| --- |
| Caution Note that this app can only be used for quality inspections with master inspection characteristics. It is not possible to capture inspection results for inspections with plan characteristics. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results in Table Form (F3365). | The Record Inspection Results in Table Form screen displays. |  |
| 3 | Enter Filter Fields | Maintain filter values and choose Go. | A list of inspection lots is displayed. |  |
| 4 | Select Inspection Lots and Inspection Characteristics | Select the inspection lots for which inspection results shall be recorded and choose Record Multiple Results.In the dialogue box Select Characteristics for Result Recording, select the master inspection characteristics for which inspection results shall be recorded and choose button OK. | The Record Inspection Results in Table Form screen displays.Note The system creates one table line item per inspection lot operation. Each master inspection characteristic is displayed in a separate column. The valuation of the inspection characteristic is displayed in a separate adjacent column. If a master inspection characteristic is assigned to another inspection operation, the respective table field is grayed out. |  |
| 5 | Show Inspection Details (Optional) | Click one inspection characteristic in the table and choose Show Details. | The side panel opens and detailed inspection data are displayed (e.g. inspection specifications, master inspection characteristic, inspection method, test equipment, and inspection remarks). |  |
| 6 |  | Choose Settings button in the upper right corner of the table. In the Define Column Properties dialogue box, select Work Center and choose OK. | An additional Work Center column is displayed. |  |
| 7 | Enter Inspection Results | Enter inspection results. See above for example data. | For qualitative results, a corresponding value help is provided. Quantitative inspection results can be entered directly.Note Depending on the defined valuation mode (check inspection method details), the valuation is either done automatically by the system or must be done manually by the user.If an inspection result requires an inspection remark (check master inspection characteristic settings), it is not possible to navigate to the next inspection result. Open Details side panel and maintain the inspection remark in section Remarks. |  |
| 8 | Save Inspection Data | Choose Save. | Inspection results are saved and a success message is displayed. |  |

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the assembly depending on the inspection result. If you do not want to use the Quality Engineer Overview (F2360), you can open the Record Usage Decision (QA11) app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Usage Decision (QA11). | The Record Usage Decision (QA11) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries in the F4 help screen and choose Go:Plant: 3310Material: FG012 |  |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot. |  |  |
| 5 | Display Defects | Check the details of Defects, on the Defects tab. | Only available if you have recorded a Negative result. For a surface rejection, there will be a surface defect, for a length rejection, there will be a tolerance defect displayed. |  |
| 6 | Enter UD code | Depending on the inspection result, select one of the following two options via search help and confirm with Choose.Positive ResultUD code: UD04 A1 (Accepted - unrestricted stock)Negative ResultUD code: UD04 R1 (Rejected-blocked Stock)UD code: UD04 R320 Rejected–scrap (complete quantity)If the dialogue Some required characteristics are still open. Do you want to force inspection completion? appears, choose Yes. | The corresponding stock posting is processed automatically in background for the complete quantity for Usage Decision codes A1, R1, and R320. |  |
| 7 | Save Usage Decision | Choose Save. | The usage decision is made with regard to the manufactured goods. The system automatically triggers the material movements if associated with the usage decision code.Positive Result: The usage decision made for the inspection is Quality Inspection Passed. A goods movement is posted automatically from quality inspection stock to unrestricted use stock for the assembly FG012.Note In case of positive inspection result ensure that an empty storage bin is available in storage type S001Negative Result: The usage decision made for the inspection is Quality Inspection Failed. A goods movement is posted automatically from quality inspection stock to blocked stock for the assembly FG012. |  |

#### Confirm Putaway Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A putaway list / warehouse tasks list / pick list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks - Putaway (F4150) |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>In case the Warehouse task number is not available, Please follow the below steps to identify the Warehouse task number.Warehouse Number: 3350 for AEWarehouse Task Status: OpenClick on Adapt Filters. Select additional filter, Product & Source Bin.Select Ok.Enter Product: FG012Enter Source Bin: QUAL-I01Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm | The following system message appears:<Warehouse task confirmed>. |  |

#### Evaluate Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for FG012 BEARING.

Prerequisite

Goods Receipt for Production Order is completed in the previous steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage (F2101A) screen is displayed. |  |
| 3 | Select Criteria | In the Search bar, enter FG012 and choose GO. | Stock Availability situation of FG012 will be displayed. |  |
| 4 | Selection of Materials | Use the checkbox and select the rows which have the material No as FG012 and click on Manage Materials present at the right-side corner of the screen. | The Material and Material Details sub screens display.Stock/Requirement list for all the selected materials is displayed. |  |
| 5 | Check the stock situation | Screen Stock/Requirements list should show the updated stock quantity.Stock information appears as first row in the table present in this screen. Stock quantity is displayed under columns Quantity, Available. | Updated Stock Quantity is displayed. Stock quantity is increased by the amount of quantity posted as goods receipt for Production Order. |  |

### Customer Order Creation and Outbound Delivery Creation

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order for material FG012.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) . | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders screen, select Create Sales Order - VA01. |  |  |
| 4 | Enter the Order type OR (Standard Order) | On the Create Sales Documents screen, make the following entries and choose Enter:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold To party: 33100001Ship To party: 33100001Cust. Reference: <Reference number> Enter a customer purchase order number as referenceRequested Delivery Date: Current date plus 2 working daysNote If a popup appears for example after changing the Delivery Date, choose Enter and accept it.Material Number: FG012Order Quantity: 2Plant: 3310Once the above data is entered, go into the details of sales order line item. To go to the details of the sales order line item, either double click on the sales order line item or select the line item and click on the Display Item details icon.If the Complementary Business Transaction feature is activated in your system, then select the “Additional Fiscal Data” button and enter the country specific attributes and confirm: |  |  |
| 6 | Enter storage location data in sales order line item | On the Create Standard Order: Item Data screen, click the Shipping tab.Enter data in following fields:Storage Location:335WClick the Back button | System accepts storage location details entered by user. |  |
| 7 | Perform Availability check | Select the line item of sales order and click on the Check item Availability icon.Results of availability check should be displayed in the Review Availability Check Result screen. Choose Apply. | Review Availability Check Result screen appears.Confirmed Delivery date appears under column confirmed Del. Date.Confirmed Quantity appears under column Confirmed Quantity.If you are OK with the results, click on Apply. This should take you back to the Create Standard Order: Overview screen.If you want to know the details of Availability check, then click online item and system should take you the screen: Standard Order Availability Control where you should see the details of availability check. |  |
| 8 | Save Document | Choose Save. Make a note of the sales order number. | The order is saved and sales order number is displayed at the bottom of screen.System gives a message: Standard Order XXXX has been saved. |  |

#### Create Delivery with Order Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the delivery document with reference to sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2. | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3. | Search Sales Order | Make the following entries and choose Go:Shipping point: 3310Planned Creation Date: <input the date range>Sales Document: Sales order number created previously |  |  |
| 4. | Create Delivery | Select your sales order items and choose Create Deliveries. | Creation of a delivery is triggered. |  |
| 5. | Check Details | Choose Display Log. | The Analyze Delivery Logs screen displays, delivery is created successfully with delivery number shown on tab Deliveries.Make a note of the delivery number. | Make a note of the delivery number. |

#### Create Pick Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3 | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4 | Set Departure Date / Time for Route value | Departure Date for Route: Select the date/time range that your Outbound Delivery Order falls inChoose Go. | Your outbound delivery orders is visible now. |  |
| 5 | Select your Outbound Delivery | Select your outbound delivery order. |  |  |
| 6 | Create Pick Warehouse Tasks | Choose Create Pick Warehouse Tasks.Caution In case of not enough stock, you can reduce the quantity of delivery item. | The WH Task is created. The picking list is automatically printed in the background. |  |
| 7 | Choose your Outbound Delivery Order to Display the ODO details | Choose your outbound delivery order by clicking the Outbound Delivery Order number. | The Outbound Delivery Order details is displayed on the right side of the screen. |  |
| 8 | Display Warehouse Tasks | In the Items section, choose Yes in the Open Warehouse Tasks field of any item to display the open warehouse tasks for that item.Note Due to display resolution or page size settings, the Yes is likely not displayed for the item in the Open Warehouse Tasks field. In this case, choose Show More per Row to make it visible.You can also choose Yes in the Process Relevant WTs field in the General Information section to display all warehouse task for the outbound delivery order. | The Process Warehouse Tasks screen is visible now. |  |
| 9 | Note the Warehouse Task number | Note down the appearing number. | Note down the task number. |  |

#### Confirm Pick Warehouse Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Pick List is printed in the step before and handed over now to the Warehouse Operative (EWM). He or she performs the warehouse tasks and confirms them in the system.

If the Warehouse Tasks involve products with C-Serial Number Profile (Serialization in Stock), please enter Serial Numbers in this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Fiori Process Warehouse Tasks (F4595). |  |  |
| 3 | Enter your Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>.Choose Go. |  |  |
| 4 | Check Warehouse Task Details | If the product is Serial Number managed on stock level (Seriliaziation in Stock), you have to enter Serial Number during picking WT confirmation. In this case, follow step 4-6. Otherwise go directly to step 7.Choose the Warehouse Task to go into the Warehouse Task details. |  |  |
| 5 | Choose Serial Number link | On the Warehouse Task screen in the Movement Data section, choose No. of Serial Numbers Entered: 0 / X. |  |  |
| 6 | Enter Serial Number and Confirm Warehouse Task | On the Serial Number Assignment screen, enter the serial numbers in the Enter Serial Number field one by one.Note The Serial Numbers entered here have to be the actual numbers assigned to the product / stock.Choose Okay when finished.Choose Confirm | Serial numbers are entered.The No. of Serial Numbers Entered: 0 / X has become No. of Serial Numbers Entered: X / X.The following system message appears after confirming Warehouse Task:Warehouse task <Warehouse Task Number> confirmed |  |
| 7 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | The following system message appears:Warehouse task <Warehouse Task Number> confirmed |  |

#### Pack Goods into Shipping Handling Units (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is to pack the confirmed warehouse tasks as preparation step for the final physical delivery outgoing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Open the Fiori Launch Pad with the Warehouse Operative (EWM) role. | The Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Pack Outbound Deliveries (F3193). | The Pack Outbound Deliveries (F3193) screen displays. |  |
| 3 | Enter your required values | Work Center: PACKStorage Bin: For example GI-AREA-01Choose Start Packing. | The Pack Outbound Deliveries (F3193) screen displays with a new view. |  |
| 4 | Create Handling Unit | Fill in your Reference Number:Outbound Delivery Order | A dialog box Create Shipping Handling Unit is displayed now. |  |
| 5 | Create Shipping Handling Unit | Select your favorite Packaging Material. Afterwards choose Create. | Your shipping unit is automatically created now. You can verify the Shipping Handling Unit number on the upper right corner. |  |
| 6 | Select stock to be packed | Select the material to be packed and choose Pack. Repeat this step as long as your destination handling unit has the right value of materials and quantity according to your needs.Note You are asked to enter serial numbers if the product concerned is serial number-managed on documentation level (Documentation Serialization). | According to your pack steps, you see on the right side (Destination HU) your packed materials. |  |
| 7 | Printing Shipping HU Label | To print the manual shipping handling unit label, choose Print. | Your Shipping HU Label is printed now. |  |
| 8 | Close the Shipping Handling Unit | Choose Close for finalizing the pack process step.Then choose Leave for proceeding with the next step. | Note Consider that your destination handling unit is automatically created. The HU Label is automatically printed. On the left corner below, you can verify the created status. |  |

#### Enter Serial Number for Outbound Delivery Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You don’t need to perform this step if your product is NOT serial number-managed.

If the products have an A-Serial Number profile (documentation serialization) assigned and you haven’t entered any serial number in the previous Pack Goods into Ship-ping Handling Units (Optional) step because packing is irrelevant to your business, you need to do it in this step.

If the products have a C-Serial Number profile (serialization in stock) assigned, the serial numbers are already entered in the previous step Confirm Pick Warehouse Tasks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2. | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3. | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4. | Set Departure Date / Time for Route Value | Departure Date for Route: <Select the date/time range that your Outbound Delivery Order falls in>Choose Go. | Your outbound delivery orders is visible now. |  |
| 5. | Choose your Outbound Delivery Order | Choose your outbound delivery order by choosing your outbound delivery order number | Your outbound delivery order details is displayed on the right side of the screen. |  |
| 6. | Choose Edit | Choose Edit in the outbound delivery order screen. |  |  |
| 7. | Select Item | Select one of the items of the outbound delivery order | The item details in displayed on the right side of the screen. |  |
| 8. | Enter Serial Number | In the Serial Numbers section, enter the serial numbers one by one.Choose Apply when finished. | Serial numbers are entered. |  |
| 9. | Save Document | Choose Save. |  |  |

#### Print Loading Instruction (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a list of loading instructions as an information for the carrier.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launch Pad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2. | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3. | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4. | Set Departure Date / Time for Route value | Departure Date for Route: Select the date/time range that your Outbound Delivery Order falls inChoose Go. |  |  |
| 5. | Select your Outbound Delivery Order | Select your Outbound Delivery Order which should be printed. |  |  |
| 6. | Print the Loading List | Choose Print loading Instruction. | Loading list is printed. |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is for finalizing the outbound process via posting the done status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto | Open the SAP Fiori Launchpad with the Warehouse Clerk (EWM) role. | The SAP Fiori Launch Pad is displayed. |  |
| 2 | Access the App | Open Fiori Manage Outbound Delivery Orders (F6498). | The Manage Outbound Delivery Orders (F6498) screen displays. |  |
| 3 | Enter Warehouse Number | Warehouse No: Enter your Warehouse Number, for example 3350. |  |  |
| 4 | Set Departure Date / Time for Route Value | Departure Date for Route: <Select the date/time range that your Outbound Delivery Order falls in>.Choose Go. | Your outbound delivery orders is visible now. |  |
| 5 | Select your Outbound Delivery | Select your outbound delivery order. |  |  |
| 6 | EWM: Post Goods Issue | Choose Post Goods Issue. | The goods issue is posted and has generated a warehouse material document. |  |

### Accounts Receivable

#### Create Billing Document

Purpose

In this activity, you handle the billing.

Procedure

Table 2: Overview

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen is displayed. |  |
| 3 | Define Billing Settings | Choose Billing Settings and make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document (Outbound delivery) created previously and choose button Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then press button OK. | The draft billing document with ID TMPxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save.The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | ODN Number | Check whether the ODN number is generated for the billing document. | ODN number is generated in the Reference field. |  |

#### Post Incoming Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the incoming payments from the customer. For a payment of an invoice where a down payment is applied, the incoming payment amount should be the remainder invoice balance (the remainder invoice balance is the invoice value less the down payment to be applied).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Incoming Payments (F1345) | The Post Incoming Payments view displays. |  |
| 3 | Enter General Information | Make the following entries in the General Information area:Company Code: 3310Posting date: dateJournal Entry date: dateValue date: today’s dateJournal Entry Type: DZ (Customer Payment) |  |  |
| 4 | Enter Bank Data | Make the following entries in the Bank data area.House Bank/Account ID: AEBK1/AEAC1G/L Account: <account (not a bank subaccount)> (see note)Note To determine the account value, log in as a Cash Management Specialist and open Manage Bank Accounts (F1366A). Enter your Company Code, House Bank, and House Bank Account and choose Go. Choose Details for the row. Choose House Bank Account Connectivity, then in the House Bank Account Data section, make a note of the value in the G/L Account field. Use this value for the G/L Account field above.Amount: customer invoice amountNote If the incoming payment is part of a down payment, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Currency: AED |  |  |
| 5 | Enter Open Items | Make the following entries:Customer Account: 33100001 \| 33100050Choose the Propose Items button. | The open items are displayed in the bottom half of the view. |  |
| 6 | Clear Items | Choose Items to Clear by choosing the Clear button in last item column. | The selected item is transferred to view Items to be Cleared. |  |
| 7 | Post Entries | Choose Post. | The Activated dialog box displays details of document number generated. |  |

### Accounts Payable

#### Create Supplier Invoice with PO/GR Relation

Purpose

In this activity, you perform the invoice verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Supplier Invoice (F0859). | The New Supplier Invoice screen displays. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Reference: Enter the reference document number of the supplier for example: 33300001Gross Invoice Amount : XXXCurrency: AEDInvoice Date: TodayPosting Date TodayBaseline Date: : Today (in Payment tab)Invoice Party: 33300001 |  |  |
| 4 | Enter Purchase Order References | In Purchasing Document References, make the following entries (use a PO you created previously) and Press Enter key.Make the following entries (use a PO you created previously for procuring RM016).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: PO number (Used to procure RM016) | The Purchase Order References screen displays. |  |
| 5 | Select Purchase Order Items | Check the selection of the Purchase Order Items.Confirm the warning messages. | All items of the selected Purchase Order are added to the Purchase Order Item table. |  |
| 6 | Check the Purchase Order Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Purchase Order Item's table displays. |  |
| 7 | Check Tax code | In the section Tax check if there is tax code information and enter the tax amount.when the tax code value is greater than zero | In the Tax tab, you should see the same tax codes as in the items.If there is no tax, specify the tax code V0. |  |
| 8 | Check the balance | Calculate the tax amount from the item amount multiplied by the tax value. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 9 | Simulate Supplier Invoice and Check Messages | Choose the Simulate button.You can check the simulation results in Simulation Overview and Simulation Details area. Choose Back. | The supplier invoice is simulated. |  |
| 10 | Post Invoice | Choose Post. | The system displays the message that the Documents have been created. Supplier invoice xxx posted. |  |
| 11 | Repeat the steps for creating invoice for the second Purchase Order | Repeat the steps 3 to 10 for creating the invoice for the purchase order used for procuring the material: RM015. While doing this, in step 3, it is important to key in the correct invoice party as 33300002 and in step 4, enter the purchase order of RM015. | Invoice saved for Purchase Order of RM015 Material. |  |
| 12 | Repeat the steps for creating invoice for the second Purchase Order | Repeat the steps 3 to 10 for creating the invoice for the purchase order used for procuring the material: RM021. While doing this, in step 3, it is important to key in the correct invoice party as 33300002 and in step 4, enter the purchase order of RM021. | Invoice saved for Purchase Order of RM021 Material. |  |

#### Post Outgoing Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can post outgoing payments either manually or automatically. The manual posting process is described in the following example. The manual outgoing payment generated in this step does not go through an approval process and does not create a payment medium.

When an invoice is paid and the supplier is subject to withholding tax, the tax is withheld from the total invoice amount when the payment is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Outgoing Payments (F1612). | The Post Outgoing Payments (F1612) view displays. |  |
| 3 | General Information | Make the following entries:General Information sectionCompany Code: 3310Posting Date: <Today's date>Journal Entry Date: <Today's date>Value Date: <Today's date>Reference (optional): <reference>Journal Entry Type: KZHeader Text: <header text>Bank Data sectionG/L Account: 11001000House Bank / Account: AEBK1/AEAC1Note For invoices in USD, use account USDAC.Amount / Currency: <amount to pay on existing invoice>, for example, 60 AEDFees: OptionalAssignment: OptionalExchange Rate: OptionalAmount / CCode Currency: Optional | A list of open items is displayed in the Open Items \| Standard section. |  |
| 4 | Open Item Selection | In the Open Item Selection section, make the following entries:Supplier Account: 33300001and choose the Show Items button.This is used for doing the payment for RM016. |  |  |
| 5 | Select/Deselect | Select an item to pay, and in the Clear column, choose Clear. | The item to pay transfers to the Items to be Cleared / Standard section. |  |
| 6 | Post | Choose Post.Note The generated payment does not require approval. | The system displays Journal entry xxxxxxxxxx was successfully posted in company code 3310 notification. |  |
| 7 | Display | To view the posted document, choose Display. | The posted document is displayed. |  |
| 8 | Back | Choose the Back button. | The system displays Journal entry has already been posted. You can now post a new payment notification. |  |
| 9 | Dismiss notification | Choose OK to dismiss the notification. |  |  |
| 10 | Repeat steps to do the payment for second invoice | Repeat the steps 3 to 9 to do the payment for invoice of purchase order for material: RM015. While repeating the steps, in step number 4, it is important to use supplier account: 33300002. | Outgoing payment is successfully posted for the purchase order of the RM015 material. |  |
| 11 | Repeat steps to do the payment for third invoice | Repeat the steps 3 to 9 to do the payment for invoice of purchase order for material: RM021. While repeating the steps, in step number 4, it is important to use supplier account: 33300002. | Outgoing payment is successfully posted for the purchase order of the RM021 material. |  |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example | Words or characters quoted from the screen. These include field names, screen titles, pushbuttons labels, menu names, menu paths, and menu options.Textual cross-references to other documents. |
| Example | Emphasized words or expressions. |
| EXAMPLE | Technical names of system objects. These include report names, program names, transaction codes, table names, and key concepts of a programming language when they are surrounded by body text, for example, SELECT and INCLUDE. |
| Example | Output on the screen. This includes file and directory names and their paths, messages, names of variables and parameters, source text, and names of installation, upgrade and database tools. |
| Example | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example> | Variable user entry. Angle brackets indicate that you replace these words and characters with appropriate entries to make entries in the system. |
| EXAMPLE | Keys on the keyboard, for example, F2 or ENTER. |

|  |
| --- |
|  |
| www.sap.com/contactsap |
| © 2026 SAP SE or an SAP affiliate company. All rights reserved.No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company. The information contained herein may be changed without prior notice. Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors. National product specifications may vary.These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP or its affiliated companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP or SAP affiliate company products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty. SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other countries. All other product and service names mentioned are the trademarks of their respective companies. See [www.sap.com/copyright](http://www.sap.com/copyright) for additional trademark information and notices. |

<!-- image omitted: SAP Logo -->

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Assign Bins to PSA step uses Warehouse Number 1750 while all other steps and org data use warehouse 3350.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Create Control Cycle (IM-managed PSA) for RM021 uses supply area PSA_01 and warehouse no 335, while org data lists only PSA_03 and warehouse 3350.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]
- related-to :: [[12-production-and-manufacturing/production-capacity-evaluation-and-leveling-consumer-products-5oi-ae-t]]
- related-to :: [[10-procurement/test-script-procurement-of-production-components-consumer-products-5w3]]
- related-to :: [[12-production-and-manufacturing/test-script-produce-and-sell-standard-products-inventory-management-54-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/54V_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 199,204 chars in the whole document
