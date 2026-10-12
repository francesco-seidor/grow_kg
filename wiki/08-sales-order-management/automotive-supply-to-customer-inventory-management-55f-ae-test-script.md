---
id: 08-sales-order-management/automotive-supply-to-customer-inventory-management-55f-ae-test-script
title: Automotive Supply to Customer – Inventory Management (55F_AE) Test Script (55F_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 AE test script for scope item 55F: automotive supply to customer with sales scheduling agreements, JIT calls, consignment, billing and payments."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-scheduling-agreements-and-jit]
aliases: [55F_S4CLD2608_BPD_EN_AE]
keywords: [Sales Scheduling Agreements and JIT Supply to Customer, sales scheduling agreements, just-in-time calls, jit master data, purchase scheduling agreements, repetitive manufacturing, outbound delivery, consignment issue, jit delivery confirmation, billing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/55F_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1069
topic: 08-sales-order-management/sales-scheduling-agreements-and-jit
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Automotive Supply to Customer – Inventory Management (55F_AE) Test Script (55F_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/55F_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales Scheduling Agreements and JIT Supply to Customer** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Automotive Supply to Customer – Inventory Management (55F_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Automotive Supply to Customer – Inventory Management (55F_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232856077)

[2 Prerequisites 6](#_Toc232856078)

[2.1 System Access 6](#_Toc232856079)

[2.2 Roles 6](#_Toc232856080)

[2.3 Master Data, Organizational Data, and Other Data 8](#_Toc232856081)

[2.4 Business Conditions 16](#_Toc232856082)

[2.5 Preliminary Steps 16](#_Toc232856083)

[2.5.1 Maintain JIT Production Confirmation Profile 16](#_Toc232856084)

[2.5.2 Create Purchasing Info Record 17](#_Toc232856085)

[2.5.3 Create Purchase Scheduling Agreement w/o Release doc - Standard 22](#_Toc232856086)

[2.5.4 Edit User-Specific Parameters for Supplier Invoices (Optional) 24](#_Toc232856087)

[2.5.5 Maintain Customer-Material Info Record (Optional) 25](#_Toc232856088)

[2.5.6 Create Pricing Condition 26](#_Toc232856089)

[2.5.7 Create Product Cost Collectors 27](#_Toc232856090)

[2.5.8 Create Preliminary Cost for the Product Cost Collector 28](#_Toc232856091)

[2.5.9 Create Packing Instruction 29](#_Toc232856092)

[2.5.10 Create Packing Instruction Determination 30](#_Toc232856093)

[2.5.11 Create Just-In-Time Customer Master Data 31](#_Toc232856094)

[2.5.12 Create Customer Supply Control Records 33](#_Toc232856095)

[2.5.13 Define Packing Group Specification 34](#_Toc232856096)

[2.5.14 Create Just-In-Time Delivery Sequence Groups 35](#_Toc232856097)

[2.5.15 Create Just-In-Time Teams and Define Responsibilities 36](#_Toc232856098)

[3 Overview Table 40](#_Toc232856099)

[4 Test Procedures 45](#_Toc232856100)

[4.1 Sales Scheduling Agreement 45](#_Toc232856101)

[4.1.1 Create Sales Scheduling Agreement 45](#_Toc232856102)

[4.1.1.1 Create Sales Scheduling Agreement without JIT 45](#_Toc232856103)

[4.1.1.2 Create Sales Scheduling Agreement for Summarized JIT 46](#_Toc232856104)

[4.1.1.3 Create Sales Scheduling Agreement for Sequenced JIT with Consignment 48](#_Toc232856105)

[4.1.2 Update Scheduling Agreement for Forecast Delivery Schedule Manually 49](#_Toc232856106)

[4.1.3 Maintain Planning Delivery Schedule Instruction (Optional) 50](#_Toc232856107)

[4.1.4 Generate Planning Delivery Schedule (Optional) 51](#_Toc232856108)

[4.1.5 Check Planning Delivery Schedule (Optional) 51](#_Toc232856109)

[4.1.6 Sales Scheduling Agreements – Product Demand 52](#_Toc232856110)

[4.1.7 Create Customer Just-in-Time Call 53](#_Toc232856111)

[4.1.7.1 Create Customer Summarized Just-in-Time Call Manually 53](#_Toc232856112)

[4.1.7.2 Create Customer Sequenced Just-In-Time Call Manually 55](#_Toc232856113)

[4.1.8 Monitor Customer JIT Calls 57](#_Toc232856114)

[4.1.9 Create JIT Delivery Schedule – Background Job (Optional) 58](#_Toc232856115)

[4.1.10 Demand analysis of JIT Calls 59](#_Toc232856116)

[4.1.11 Evaluating Stock/Requirements Situation 60](#_Toc232856117)

[4.1.12 Schedule MRP Run 61](#_Toc232856118)

[4.1.13 Evaluating Stock/Requirements Situation 62](#_Toc232856119)

[4.2 Procurement of semi-finished material based on Purchase Scheduling Agreement: 65](#_Toc232856120)

[4.2.1 Display Delivery Schedule 65](#_Toc232856121)

[4.2.2 Print Scheduling Agreement (Optional) 66](#_Toc232856122)

[4.2.3 Create Inbound Delivery 67](#_Toc232856123)

[4.2.4 Confirm Quantities for Putaway 68](#_Toc232856124)

[4.2.5 Post Goods Receipt for Inbound Delivery 69](#_Toc232856125)

[4.2.6 Evaluating Stock/Requirements Situation (Optional) 70](#_Toc232856126)

[4.2.7 Execute Evaluated Receipt Settlement 71](#_Toc232856127)

[4.2.8 Check Supplier Invoice List (Optional) 73](#_Toc232856128)

[4.2.9 Display Procurement Overview (Optional) 74](#_Toc232856129)

[4.3 Repetitive Production Execution 75](#_Toc232856130)

[4.3.1 Release Summarized JIT Call Component Groups to Production 75](#_Toc232856131)

[4.3.2 Schedule Packing Group Creation / Update 76](#_Toc232856132)

[4.3.3 Release Sequenced JIT Call Component Groups to Production 77](#_Toc232856133)

[4.3.4 Check Planning in Planning Table (Optional) 78](#_Toc232856134)

[4.3.5 Check Range of Stock Coverage 79](#_Toc232856135)

[4.3.6 Material Staging 80](#_Toc232856136)

[4.3.7 Production Confirmation 82](#_Toc232856137)

[4.3.7.1 Confirm Repetitive Manufacturing Inclusive Backflush of Materials for (non-JIT) 82](#_Toc232856138)

[4.3.7.2 Post Processing of Error Records for non-JIT production 84](#_Toc232856139)

[4.3.7.3 Confirm Production of JIT Calls (Alternative) 85](#_Toc232856140)

[4.3.7.4 Reprocessing of Failed Stock Posting After Confirmation of Production (Optional) 86](#_Toc232856141)

[4.3.8 Manage JIT Packing Groups 87](#_Toc232856142)

[4.3.9 Stock availability analysis for JIT Calls 88](#_Toc232856143)

[4.3.10 Evaluating Stock/Requirements Situation (Optional) 89](#_Toc232856144)

[4.4 Outbound Delivery to Customer 90](#_Toc232856145)

[4.4.1 Scheduling Agreement Non-JIT 91](#_Toc232856146)

[4.4.1.1 Create Delivery 91](#_Toc232856147)

[4.4.1.2 Execute Picking 92](#_Toc232856148)

[4.4.1.3 Execute Automatic Packing 93](#_Toc232856149)

[4.4.2 Summarized JIT Calls 94](#_Toc232856150)

[4.4.2.1 Create Outbound Delivery from Summarized JIT Calls 94](#_Toc232856151)

[4.4.2.2 Execute Picking 96](#_Toc232856152)

[4.4.2.3 Execute Automatic Packing 97](#_Toc232856153)

[4.4.3 Sequenced JIT Call 99](#_Toc232856154)

[4.4.3.1 Create Handling Units from Packing Groups for Sequenced JIT Calls 99](#_Toc232856155)

[4.4.3.2 Create Outbound Delivery from Sequenced JIT Calls 100](#_Toc232856156)

[4.4.4 Schedule Goods Movement from Production for Customer JIT Calls (Optional) 101](#_Toc232856157)

[4.4.5 Post Goods Issue 102](#_Toc232856158)

[4.5 Consignment Issue 103](#_Toc232856159)

[4.5.1 Check Stock Overview 103](#_Toc232856160)

[4.5.2 Create Consignment Issue Order with Reference to Scheduling Agreement Manually (non-JIT) 104](#_Toc232856161)

[4.5.3 Create JIT Delivery Confirmation 106](#_Toc232856162)

[4.5.4 Release Delivery Confirmation for Sequenced JIT 107](#_Toc232856163)

[4.5.5 Create Delivery (Automatically) 108](#_Toc232856164)

[4.5.6 Post Goods Issue 108](#_Toc232856165)

[4.5.7 Check Stock Overview 109](#_Toc232856166)

[4.6 Billing 110](#_Toc232856167)

[4.6.1 Create Billing Document 110](#_Toc232856168)

[4.6.2 Job Scheduling for Billing Creation (Alternative) 112](#_Toc232856169)

[4.7 Accounts Receivable 113](#_Toc232856170)

[4.7.1 Post Incoming Payments 113](#_Toc232856171)

[4.8 Accounts Payable 115](#_Toc232856172)

[4.8.1 Post Outgoing Payment 115](#_Toc232856173)

[5 Appendix 117](#_Toc232856174)

[5.1 Scheduling Job (Alternative) 117](#_Toc232856175)

[5.1.1 Job Scheduling for Delivery Creation (Alternative) 117](#_Toc232856176)

[5.1.2 Job Scheduling for Goods Issue Deliveries (Alternative) 118](#_Toc232856177)

[5.1.3 Job Scheduling for Billing Release (Alternative) 119](#_Toc232856178)

[5.1.4 Job Scheduling for Billing Output (Alternative) 120](#_Toc232856179)

[5.2 Transmission Example – JIT Delivery Creation 121](#_Toc232856180)

[5.3 Send Transmission with Postman 123](#_Toc232856181)

## Purpose

Overview

This scope item validates the execution of an end-to-end automotive supply-to-customer process, focusing on integrated activities across procurement, production, delivery, billing, and payment, with full inventory management support.

The process begins with creating a sales scheduling agreement and maintaining forecast delivery schedules. Planning delivery schedules can be generated to smooth demand for production. Just-in-Time (JIT) calls, which include component details and requirements, can be created manually.

Components are planned and procured through material requirements planning (MRP) and purchase scheduling agreements with external suppliers. Inbound deliveries are created, goods receipts are posted, and supplier invoices are generated. MRP also generates planned orders for production. Repetitive manufacturing confirmation triggers activities like finished goods receipt, component backflush, and cost posting.

For JIT calls, production-relevant components or package units are released. Outbound deliveries to customers are created based on open quantities. After picking and packing, the goods issue is posted. Goods can be posted as consignment stock, stored at the customer location but owned by suppliers. As goods are consumed, customers send JIT delivery confirmations via the SOAP API, or a consignment issue order is created manually. Delivery confirmations are matched with existing JIT call deliveries, and once released, subsequent documents are created, and the goods issue is posted.

Deliveries can be invoiced once goods are delivered. All incoming and outgoing payments are posted, and all products in this scenario are inventory managed.

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

Note regarding the integrated process with SAP S/4HANA Cloud Public Edition:

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Material Planner - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC | Material Planning - External Procurement | SAP_BR_MATL_PLNR_EXT_PROC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_BR_PURCHASER |  |
| Master Data Specialist - Product Data | SAP_BR_PRODMASTER_SPECIALIST | Master Data - Products / Product Governance | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Production Supervisor - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV | Production Management - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV |  |
| Production Operator - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV | Production Execution - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |
| Master Data Specialist - Handling Unit Data | SAP_BR_HU_MASTER_SPECIALIST | Master Data - Handling Units | SAP_BR_HU_MASTER_SPECIALIST |  |
| Master Data Specialist - Just-In-Time Supply | SAP_BR_MD_SPECIALIST_JIT | Master Data - Just-In-Time | SAP_BR_MD_SPECIALIST_JIT |  |
| Material Planner - Just-In-Time Supply | SAP_BR_MATL_PLNR_JIT_S_TO_C | Material Planning - Just-In-Time | SAP_BR_MATL_PLNR_JIT_S_TO_C |  |
| Shipping Specialist - Just-In-Time Supply | SAP_BR_SHIP_SPECIALIST_JIT | Shipping - Just-In-Time | SAP_BR_SHIP_SPECIALIST_JIT |  |
| Production Planner - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG | Production Planning - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG |  |
| Production Supervisor - Lean Manufacturing | SAP_BR_PRODN_SUPVR_LEAN_MFG | Production Supervision - Lean Manufacturing | SAP_BR_PRODN_SUPVR_LEAN_MFG |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT | Business Network Integration / Business Network Integration - Concur Integration / Business Network Integration - Output Control / Business Network Integration - Data Replication / Configuration Expert - Business Network Integration Cross Applications | SAP_CORE_SPT_INT_PC / SAP_CON_SPT_CONCUR_INT_PC / SAP_OC_SPT_INT_PC / SAP_CA_SPT_DATA_REP_PC / SAP_CA_SPT_BUS_NETWORK_INT_PC |  |
| Pricing Specialist | SAP_BR_PRICING_SPECIALIST | Price Management | SAP_BR_PRICING_SPECIALIST |  |
| Production Operator - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG | Production Execution - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Material Master Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG031 | RIGHT SIDE DOOR | Finished Product relevant for planning. MRP Planned and Produced internally with Repetitive manufacturing. NOT Batch Managed. Not split valuated. Not applicable for Quality Management.Sold to customer. Only Inventory Managed & NOT eWM managed. Product is to be costed, costing and accounting views to be maintained. |
| Material | FG032 | LEFT SIDE DOOR | Finished Product relevant for planning. MRP Planned and Produced internally with Repetitive manufacturing. NOT Batch Managed. Not split valuated. Not applicable for Quality Management.Sold to customer. Only Inventory Managed & NOT eWM managed. Product is to be costed, costing and accounting views to be maintained. |
| Material | SG031 | Right Side Door Assembly | Externally Procured Material using a Purchasing Scheduling Agreement.MRP Planned and procured from external supplier.Only Inventory Managed & NOT eWM managed. Not applicable for Quality Management.NOT Serial number managed. Not Batch Managed. |
| Material | SG032 | Door Speaker | Externally Procured Material using a Purchasing Scheduling Agreement.MRP Planned and procured from external supplier.Only Inventory Managed & NOT eWM managed. Not applicable for Quality Management.NOT Serial number managed. Not Batch Managed. |
| Material | SG033 | Left Side Door Assembly | Externally Procured Material using a Purchasing Scheduling AgreementMRP Planned and procured from external supplier.Only Inventory Managed & NOT eWM managed. Not applicable for Quality ManagementNOT Serial number managed. Not Batch Managed. |
| Material | PMPallet | PALLET 48x40 | PackagingOnly Inventory Managed & NOT eWM managed. Not applicable for Quality Management.NOT Serial number managed. Not Batch Managed. |
| Material | PKGJITSEQ | JIT Packaging Material | PackagingOnly Inventory Managed & NOT eWM managed. Not applicable for Quality Man-agement.NOT Serial number managed. Not Batch Managed. |

Organizational Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Cost center | 33101301 | Manufacturing 1 (AE) |  |

Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG031 | 0 | FERT | PC | Finished Good for Repetitive processing. |  |  |
| SG031 | 1 | HALB | PC | External procured. | 1 | PC |
| SG032 | 1 | HALB | PC | External procured. | 1 | PC |

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG032 | 0 | FERT | PC | Finished Good for Repetitive processing. |  |  |
| SG033 | 1 | HALB | PC | External procured. | 1 | PC |
| SG032 | 1 | HALB | PC | External procured. | 1 | PC |

Work Center:

Below table mentions the work center to be used in this scenario. These are standard work centers available as part of best practice and hence it is not needed to create new Work Centers.

| Work Center | Plant | Work Center Category | Work Center Description |
| --- | --- | --- | --- |
| FABRIC | 3310 | 0007 | Fabrication |

Routing:

Create a routing for the Finished product- FG031 mentioned in this document. Routing must be created in 3310 Plant

Production Version:

Create production version for the finished product FG031 using the BOM and routing created in the above steps. Production Version must be created in Plant.

Suppliers:

Below mentioned Suppliers (Business Partners) will be used in this scenario.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Supplier | 33300003 | Domestic UAE Supplier 3 |  |
| Supplier | 33300063 | Domestic AE Supplier 63 (with ERS) |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |

Customer:

Below mentioned Customers (Business Partners) will be used in this scenario.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 33100020 | Customer: Domestic AE Customer 20 |  |
| Ship-to Party | 33100020 | Customer: Domestic AE Customer 20 |  |
| Payer | 33100020 | Customer: Domestic AE Customer 20 |  |
| Sold-to Party | 33154801 | JIT Customer 01 |  |
| Ship-to Party | 33154801 | JIT Customer 01 |  |
| Payer | 33154801 | JIT Customer 01 |  |
| Sold-to Party | 33154802 | JIT Company |  |
| Ship-to Party | 33154802 | JIT Company |  |
| Payer | 33154802 | JIT Company |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |
| Shipping point | 3310 |  |  |
| Company code | 3310 |  |  |

Overview of Master Data by Scenario:

Table 1: Scenario 1 : Process with Sales Scheduling Agreements, without consignment and without JIT

| Data | Sample Value | Description |
| --- | --- | --- |
| Material | FG031 | RIGHT SIDE DOOR |
| Material | SG031 | Right Side Door Assembly |
| Material | SG032 | Door Speaker |
| Material | PMPallet | PALLET 48x40 |
| Supplier | 33300003 | Domestic UAE Supplier 3 |
| Supplier | 33300063 | Domestic AE Supplier 63 (with ERS) |
| Sold-to Party | 33100020 | Customer: Domestic AE Customer 20 |
| Ship-to Party | 33100020 | Customer: Domestic AE Customer 20 |
| Payer | 33100020 | Customer: Domestic AE Customer 20 |

Table 2: Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG031 | 0 | FERT | PC | Finished Good for Repetitive processing. |  |  |
| SG031 | 1 | HALB | PC | External procured. | 1 | PC |
| SG032 | 1 | HALB | PC | External procured. | 1 | PC |

Table 3: Scenario 2: Process with Sales Scheduling Agreements and Customer Consignment, without JIT

| Data | Sample Value | Description |
| --- | --- | --- |
| Material | FG031 | RIGHT SIDE DOOR |
| Material | SG031 | Right Side Door Assembly |
| Material | SG032 | Door Speaker |
| Material | PMPallet | PALLET 48x40 |
| Supplier | 33300003 | Domestic UAE Supplier 3 |
| Supplier | 33300063 | Domestic AE Supplier 63 (with ERS) |
| Sold-to Party | 33100020 | Customer: Domestic AE Customer 20 |
| Ship-to Party | 33100020 | Customer: Domestic AE Customer 20 |
| Payer | 33100020 | Customer: Domestic AE Customer 20 |

Table 4: Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG031 | 0 | FERT | PC | Finished Good for Repetitive processing. |  |  |
| SG031 | 1 | HALB | PC | External procured. | 1 | PC |
| SG032 | 1 | HALB | PC | External procured. | 1 | PC |

Table 5: Scenario 3: Process with Sales Scheduling Agreement with JIT, without Customer Consignment

| Data | Sample Value | Description |
| --- | --- | --- |
| Material | FG031 | RIGHT SIDE DOOR |
| Material | SG031 | Right Side Door Assembly |
| Material | SG032 | Door Speaker |
| Material | PMPallet | PALLET 48x40 |
| Supplier | 33300003 | Domestic UAE Supplier 3 |
| Supplier | 33300063 | Domestic AE Supplier 63 (with ERS) |
| Sold-to Party | 33154801 | JIT Customer 01 |
| Ship-to Party | 33154801 | JIT Customer 01 |
| Payer | 33154801 | JIT Customer 01 |

Table 6: Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG031 | 0 | FERT | PC | Finished Good for Repetitive processing. |  |  |
| SG031 | 1 | HALB | PC | External procured. | 1 | PC |
| SG032 | 1 | HALB | PC | External procured. | 1 | PC |

Table 7: Scenario 4: Process with Sales Scheduling Agreement with JIT and Customer Consignment

| Data | Sample Value | Description |
| --- | --- | --- |
| Material | FG032 | LEFT SIDE DOOR |
| Material | SG032 | Door Speaker |
| Material | SG033 | Left Side Door Assembly |
| Material | PKGJITSEQ | JIT Packaging Material |
| Supplier | 33300003 | Domestic UAE Supplier 3 |
| Supplier | 33300063 | Domestic AE Supplier 63 (with ERS) |
| Sold-to Party | 33154802 | JIT Company |
| Ship-to Party | 33154802 | JIT Company |
| Payer | 33154802 | JIT Company |

Table 8: Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG032 | 0 | FERT | PC | Finished Good for Repetitive processing. |  |  |
| SG032 | 1 | HALB | PC | External procured. | 1 | PC |
| SG033 | 1 | HALB | PC | External procured. | 1 | PC |

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| 3Y1 | Create Product Master of Type "Packaging" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |
| BNE | Create Supplier Master - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BET | Create Sales Pricing Condition - MDS |
| BND | Create Customer Master - MDS |
| 2YX | Create Customer-Material Info Record - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Standard Cost Calculation (BEG) test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| J58- Accounting and Financial Close | Execute to create open posting periods. |
| BFA - Basic Bank Account Management | Bank account master data is processed. |
| 2EM - Just-In-Time Supply to Customer | You have to complete the setup guide for relevant master data |
| 53X - Just-In-Time Supply to Customer with Delivery Confirmation | You have to complete the setup guide for relevant master data |

### Preliminary Steps

#### Maintain JIT Production Confirmation Profile

This step needs to be executed in order to maintain appropriate profiles for execution of backflush/goods movement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Product Data . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Choose Manage Product Master Data (F1602). | The Manage Product Master Data screen opens. |  |
| 3 | Search Material | FG031in Product filter and choose Go | Product FG031 is filtered. |  |
| 4 | Navigate to Object Page | Click on the chevron to navigate to the object page. | Object page of chosen material is displayed. |  |
| 5 | Navigate to Plant 3310 | Choose Plants and click on chevron against plant 3310. | Object page of chosen plant is displayed. |  |
| 6 | Navigate to Repetitive Manufacturing section | Choose MRP Data and select Repetitive Manufacturing. | Repetitive Manufacturing section is displayed. |  |
| 7 | Maintain JIT Production Confirmation Profile | Choose Edit. Choose the menu option for JIT Production Confirmation Profile. Select value Asynchronous execution of Backflush. Choose Apply. | The chosen entry is saved as draft entry. |  |
| 8 | Save the changes | Choose Save.Note Repeat the steps for material FG032 and if Production Confirmation profile is maintained Consider from Component Group material, then in that case repeat the steps from 1-7 for component materials example SG031, SG032, SG033 | Appropriate JIT Production Confirmation Profile is saved for materials FG031, FG032, SG031, SG032 and SG033 |  |

#### Create Purchasing Info Record

Purpose

To run through this test script, the info records for the necessary materials must be available as master data. If the Info Record has not been maintained in the system yet, create the required master data. Otherwise you can skip this step.

The purpose of this activity is to create the info records for products. This step is obsolete if the necessary info records are present.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The New Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Under the Header Section make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300003Material: SG031Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter General Information | Under General Information section make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Under the Purchasing Data section, make the following entries:Incoterm: EXWNote Incoterms and their corresponding versions are grouped in the F4 value help. Selecting an incoterm automatically populates its associated version, which can be subsequently modified or removed if needed.Incoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Under the Delivery and Quantity Data section, make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Tax Rate Valid From: TodayOrder Unit: PCStandard Order Quantity: 1000Goods-Receipt-Based Invoice Verification: X | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Conditions section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 1755Pricing Unit: 100Currency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Save your data | Choose Create. | The purchasing info record is saved. |  |
| 11 | Repeat steps | Repeat above steps 3 to 10 to create another info record for the other material using the following data:Header Data:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300063Material: SG032Plant: 3310Purchasing Group: 001General Data:Available From:TodayAvailable To:12/31/9999Purchasing Data:Incoterm: EXWIncoterm Location 1:VENDORDelivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Note When the TDT(time dependent tax) is activated via SSCUI 101016 (Define Tax Codes for Sales and Purchases) for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in SSCUI.When the RITA (Registration for Indirect Taxation Abroad) is activated, tax registration country is maintained for company code in SSCUI 103464 (Activate RITA and Maintain Tax Registration Countries) and tax code is given, the Tax Country field is mandatory, in which the country ID of company code is given as a default value, but you can change to the valid country ID that is maintained in SSCUI accordingly.Tax Rate Valid From:TodayOrder Unit: PCStandard Order Quantity: 2000Goods-Receipt-Based Invoice Verification: XCondition Data:Valid From: TodayValid To: 12/31/9999Amount: 170Pricing Unit: 1Currency: AEDPress Enter. | The purchasing info record is saved. |  |
| 12 | Repeat steps | Repeat steps 3 to 10 to create another info record for the material using the following data:Header Data:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300003Material: SG033Plant: 3310Purchasing Group: 001General Data:Available From:TodayAvailable To:12/31/9999Purchasing Data:Incoterm: EXWIncoterm Location 1:VENDORDelivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10.0Tax Code: <Input Tax Code>Note When the TDT(time dependent tax) is activated via SSCUI 101016 (Define Tax Codes for Sales and Purchases) for Country of company code and Tax Code is given, the Tax Rate Valid From field is mandatory. You can enter current date, which will be adjusted to validity start date of tax code according to the setting in SSCUI.When the RITA (Registration for Indirect Taxation Abroad) is activated, tax registration country is maintained for company code in SSCUI 103464 (Activate RITA and Maintain Tax Registration Countries) and tax code is given, the Tax Country field is mandatory, in which the country ID of company code is given as a default value, but you can change to the valid country ID that is maintained in SSCUI accordingly.Tax Rate Valid From:TodayOrder Unit: PCStandard Order Quantity: 1000Goods-Receipt-Based Invoice Verification: XCondition Data:Valid From: TodayValid To: 12/31/9999Amount: 1755Pricing Unit: 100Currency: AEDPress Enter. |  |  |

#### Create Purchase Scheduling Agreement w/o Release doc - Standard

Purpose

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad, as Purchaser . | SAP Fiori launchpad displays |  |
| 2 | Access the SAP Fiori app | Open Manage Purchase Scheduling Agreements (F2179) tile. | The Manage Purchase Scheduling Agreements list page displays |  |
| 3 | Create Purchase Scheduling Agreement | Select Create to create a new purchase scheduling agreement | The New Purchase Scheduling Agreement header view displays. |  |
| 4 | Enter Header Data | Create a new purchase scheduling agreement with the following data:Supplier: 33300003Agreement type: LP (Scehduling agreement)Valid To:MM/DD/YYYYPurchasing Organization: 3310Purchasing Group: 001Target Value:200000 AED |  |  |
| 5 | Add Items to Purchase Scheduling Agreement | From the New Purchase Scheduling Agreement view, choose the Items facets and select Create. | The Purchase Scheduling Agreement Item view displays. |  |
| 6 | Enter Item data | On the Items facets view, make the following entries:Plant: 3310Material: SG031Target Quantity: 10000Confirmation Control: 0004Net Order Price: Defaulted from Info recordTax Code: <Input Tax Code> (Default Value from Info Record)Tax Date: Default TodayChoose Apply at the bottom of the view. |  |  |
| 7 | Save | Return to the New Purchase Scheduling Agreement header view and choose Create at the bottom of the view.Make a note of the schedule agreement number. |  |  |
| 8 | Create the Second purchase scheduling agreement | Repeat the steps 3 to 7 using the following data:Header Data:Supplier: 33300063Agreement type: LP (Scheduling Agreement)Valid End: MM/DD/YYYYPurchasing Organization: 3310Purchasing Group: 001Target Value: 200000 AEDItem Data:Plant: 3310Material: SG032Target Quantity: 20000Confirmation Control: 0004Net Order Price: Defaulted from Info recordTax Code: <Input Tax Code> (Default Value from Info Record)Tax Date: Default TodayChoose Apply at the bottom of the view. |  |  |
| 9 | Create the third purchase scheduling agreement | Repeat the steps 3 to 7 using the following data:Header Data:Supplier: 33300003Agreement type: LP (Scheduling Agreement)Valid End: MM/DD/YYYYPurchasing Organization: 3310Purchasing Group: 001Target Value: 200000 AEDItem Data:Plant: 3310Material: SG033Target Quantity: 10000Confirmation Control: 0004Net Order Price: Defaulted from Info recordTax Code: <Input Tax Code> (Default Value from Info Record)Tax Date: Default TodayChoose Apply at the bottom of the view. |  |  |

#### Edit User-Specific Parameters for Supplier Invoices (Optional)

Purpose

In this procedure, you will edit User-Specific parameters for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Edit Supplier Invoice Settings (F3813) | The Edit Supplier Invoice Settings screen is displayed. |  |
| 3 | Set parameter | Check parameter Display Journal Entry: XNote If parameter is checked, when invoice is created, system message contains invoice and journal entry number.If parameter is unchecked, when invoice is created, system message contains invoice number only.When this parameter is changed, for APP Create Supplier Invoice, it will take effective immediately. For APP Create Supplier Invoice – Advanced, user needs to logout and login again to put it into effect. | Change has been saved successfully. |  |

Result

Parameter Display Journal Entry has been set successfully.

#### Maintain Customer-Material Info Record (Optional)

Purpose

This process shows you how to maintain the customer-material info record to run through this scope item.

If the customer-material info record already exists, or you want to maintain the customer material manually when creating the scheduling agreement, please skip the step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Materials (F2499). |  |  |
| 3 | Access the Creation of Customer Material | Choose Create. | The Customer Material screen displays. |  |
| 4 | Enter Basic Customer-Material Information Value Mappings | Make the following entries:Customer: 33100020Product: FG031Sales Organization: 3310Distribution Channel: 10Customer Material Description: RSD129 | Basic customer-material information is maintained. |  |
| 5 | Save | Choose .Create | Customer Material successfully created. |  |
| 6 | Maintain additional Customer- Master Data | Repeat steps 4 and 5 with the follwoing data:Customer: 33154801Product: FG031Sales Organization: 3310Distribution Channel: 10Customer Material Description: RSD129_JIT | Customer Material successfully created |  |
| 7 | Maintain additional Customer- Master Data | Repeat steps 4 and 5 with the follwoing data:Customer: 33154802Product: FG032Sales Organization: 3310Distribution Channel: 10Customer Material Description: RSD129_SEQ_CNJIT | Customer Material successfully created |  |

#### Create Pricing Condition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes creating sales pricing conditions.

In case you have fine-tuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the Master Data descriptions of scope item BET.

If the pricing condition already exist, or you want to maintain the price manually when creating the scheduling agreement, please skip the step

|  |
| --- |
| Remember Sample values for master data values are country/region-specific. Substitute the country/region-specific values provided by the SAP S/4HANA Cloud Public Edition system or use master data values you have created for this purpose. |

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Pricing Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Material Prices - Sales (VK12). | The Create Mandate: Initial Screen displays. |  |
| 3 | Pricing Condition Type | In the Change Condition Records view, enter the following information:Condition Type: for example, PPR0Press Enter. | The Key Combination view displays. |  |
| 4 | Key Combination | In the Key combination view, choose Material with release status and click Choose. | The Change Price (PPR0): Selection view displays. |  |
| 5 | Selection | In the Change Price (PPR0): Selection view, enter the following information:Sales Organization: 3310Distribution Channel: 10Material: FG031Valid On: for example, <Date>Choose Execute. | The Change Price Condition (PPR0): Overview view displays. |  |
| 6 | Change Price Condition | In the Change Price Condition (PPR0): Overview view, enter the following data:Material: FG031Amount: for example, 1913.50Valid From: for example, <Current date>Valid To: for example, <Current date + one year> | Material pricing condition is maintained. |  |
| 7 | Save | Choose Save. | The pricing condition is saved. |  |
| 8 | Maintain Price Condition for additional product | Repeat step 5, 6 and 7 with the following data:Sales Organization:3310Distribution Channel:10Material: FG032Valid On : for example,<Date>Amount: for example, 1913.50Valid From: for example, <Current date>Valid To: for example, <Current date + one year> |  |  |

#### Create Product Cost Collectors

Purpose

The product cost collector might already be created in connection with other scope items.

For a possible check, if the related ones are already created, please use the App Maintain Product Cost Collectors (KKF6N) with the selection based on the given material/plant data. In case the product cost collector already exists, the selectable entry on the left panel is displayed and this step can be skipped.

Prerequisites

This step can only be executed if product cost planning is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Product Cost Collectors - Production Versions - Collective (KKF6M). |  |  |
| 3 | Enter Relevant Values | On the Create Multiple Product Cost Collectors for Production Versions screen, make the following entries:Plant: 3310Material: FG031Order Type: YBMROnly Repetitive Mfg Mat.: selectChoose Execute. |  |  |
| 4 | Exit | Choose Exit. |  |  |
| 5 | Repeat for other product | Repeat step 3 and 4 with the following data:Plant: 3310Material: FG032Order Type: YBMROnly Repetitive Mfg Mat.: selectChoose Execute |  |  |

#### Create Preliminary Cost for the Product Cost Collector

Purpose

This process step shows you how to create preliminary cost for the product cost collector.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Preliminary Cost Estimate - Product Cost Collectors (MF30). | The Creation of Preliminary Cost Estimates for Product Cost Collectors screen displays. |  |
| 3 | Enter Relevant Values | Make the following entries and choose Execute.Costing Date: Current DatePlant: 3310Material: FG031 |  |  |
| 4 | Repeat for other Product | Repeat step 3 with the following data:Costing Date:Current DatePlant: 3310Material: FG032 |  |  |

#### Create Packing Instruction

Purpose

In this step, you create a Packing Instruction.

A packing instruction serves as a template for the creation of a handling unit. In a packing instruction, you define the materials and packaging materials to be packed in a handling unit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Handling Unit Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Packing Instruction - Master Data (POP1). | The Create Packing Instruction: Initial screen displays. |  |
| 3 | Create Packing Instruction | To create a new Packing Instruction, choose Continue or press Enter.If you want to create packing instruction from reference packing instruction, choose a reference packing instruction and press Enter. |  |  |
| 4 | Maintain the description of Packing Instruction | Enter the short text field for the description of Packing Instruction. |  |  |
| 5 | Enter Packaging Material | Enter the packaging material number PMPALLET Component of item 10.Note The Item category P of item 10 means packaging materials. The first line is mandatory for every packing instruction because every packing instruction needs at least 1 packaging material.Note Please ensure that you have assigned the Packaging Material Type, for example, SP21 in the view Sales: General/Plant when creating the Packaging Material that you’re going to enter here. |  |  |
| 6 | Maintain material and target quantity | In item 20, make the following entries:Item category: M MaterialComponent: Material number to be packed, for example, FG031 .Target Quantity: 1 |  |  |
| 7 | Enter Check Profile | On the Admin.data tab, enter 01 in the Check Profile field.01 is the pre-delivered SAP Standard Profile. |  |  |
| 8 | Save | Choose Save.Make a note of the packing instruction number: _____. | A packing instruction is created. |  |

#### Create Packing Instruction Determination

Purpose

In this step, you create Packing Instruction Determination Records.

This function enables the system to find a packing instruction by specific characteristics. The condition technique is applied for this. You define a packing instruction that refers to specific characteristics, such as material and ship-to-party.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Handling Unit Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Determination Records - Master Data (POF1). | The Create Determination Recs for Pkg Instruction: Init.Screen displays. |  |
| 3 | Enter Determination Type for Outbound Delivery | On the Pkg Instruction - Create Determination Recs: Initial Screen, make the following entry, and press Enter:Determination Type: For example, SHIP |  |  |
| 4 | Choose a Key Combination | In the key combination window, choose a key combination, and choose Choose.For example, choose Material/Ship-to-Party. |  |  |
| 5 | Enter the Packing Instruction Determination | On the Create Ship. pack. inst: Fast Entry screen, make the following entries:Material:FG031Ship-to-pt: 33100020Packing instruction: <The Packing instruction number noted in the last section>. |  |  |
| 6 | Save | Choose Save. | Packing Instruction Determination Record for outbound delivery is created. |  |
| 7 | Create additional Pakcing Instruction | Repeate step 5 and 6 with the following dataMaterial: FG031Ship-to-pt: 33154801Packing instruction: <The Packing instruction number noted in the last section>. |  |  |

#### Create Just-In-Time Customer Master Data

Purpose

To maintain JIT-specific information for a JIT customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage JIT Customer Data (F3011) app. | Customer information is displayed. | By default, all the customers for whom the JIT-relevant information is maintained are displayed. You can filter to narrow down the customers list. |
| 3 | Create JIT-relevant Customer | Choose Create to create a JIT-relevant customer. | Object screen is displayed. |  |
| 4 | Maintain Customer ID | Choose Enter Customer and enter 33154801 |  | By default, the following information is displayed on the screen:Sales Area, Country, City, Status |
| 5 | Maintain Additional JIT-specific Information for a Customer | On the Customer Detail screen, make the following entries and choose Save and Activate:DestinationsCustomer Supply Area: RO_PSA_01Unloading Point: UL01Customer Assembly Location: <Body Shop>External Status MappingTransmitted Status: <Blank>External Status: SNEWCall ProcessingExt. JIT Call No. Unique for (Days): 9999Sequence Number Profile: <Blank>[Optional] Split criteria for summarized JIT calls: No split[Optional] Split criteria for sequenced JIT calls: No split |  | For Delivery Split Criteria, there is no default option selected. Either of the following options can be selected from the menu:External Component Group Number: Selecting this option splits the delivery document based on external component group number.External JIT Call Number: Selecting this option splits the delivery document based on external JIT call number. |
| 6 | Save the Entries | Choose Save and Activate | The status of the customer is set to Active. |  |
| 7 | Maintain another JIT Customer | Repeat steps 4 to 6 with the following dataCustomer: 33154802 |  |  |

#### Create Customer Supply Control Records

Purpose

To create a customer supply control.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage JIT Customer Supply Controls (F3010) app. |  |  |
| 3 | Create Customer Supply Control | Choose Create to create a new customer supply control | Object screen is displayed to create a new customer supply control |  |
| 4 | Maintain Customer Supply Control | On the Supply Control Detail screen, make the following entries and choose Save and Activate:Supply ControlSupply Control DescriptionCustomer: 33154801Plant: 3310Customer Supply Area: RO_PSA_01Component Group Material: FG031Call ProcessingAction Control: S2C_SUMJCCall Type: Summarized JIT CallRepetitive Manufacturing is Allowed: Yes (In case of repetitive manufacturing scenarios only)Production Version: 0001Delivery ControlPartial Delivery Allowed: YesUnderdelivery Tolerance (%): 99Overdelivery Tolerance (%): 0.00Unlimited Tolerance Allowed: No |  | By default, the following information is displayed on the screen:Sales Area, Country, City, Status |
| 5 | Save the Entries | Choose Save and Activate | The status of the supply control is set to Active. |  |
| 6 | Create new supply control for material FG032 | Follow steps 3 to 5 above to create a new supply control for material FG032 with changes to below entries:Supply ControlSupply Control DescriptionUnloading Point: UL01Customer: 33154802Plant: 3310Customer Supply Area: RO_PSA_01Component Group Material: FG032Call ProcessingAction Control: S2C_SEQJCCall Type: Sequenced CallRepetitive Manufacturing is Allowed: YesProduction Version: 0001Delivery ControlPartial Delivery Allowed: No |  |  |

#### Define Packing Group Specification

Purpose

To create a packing group specification as per customer requirements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Manage Packing Group Specification for Sequenced JIT Calls (F3896) app. |  |  |
| 3 | Create a New Package Specification | Choose Create to create a new package specification | Object screen is displayed to create a new package specification. |  |
| 4 | Maintain Package Specification | On the Package Specification Detail screen, make the following entries and choose Save and Activate:Packing Group Specification Description: <Package Specification for <Customer Name>Packaging Material: PKGJITSEQTotal Number of Slots: 2Reorder Package Specification: No |  |  |
| 5 | Maintain Slot Group Information | On the Package Specification Detail screen, choose Create in the Slot Group section.Make the following entries and choose Save and Activate:Slot GroupFirst Slot ID: 1Last Slot ID: 2Increment: 1Content Type: Component Group MaterialComponent Group Material: FG032Withdrawal Sort Sequence: AscendingPacking Sort Sequence: Ascending |  |  |
| 6 | Save the Entries | Choose Save and Activate | The status of the package specification is set to Active. |  |

#### Create Just-In-Time Delivery Sequence Groups

Purpose

In order to deliver products for individual manufacturing orders according to the production sequence, delivery sequence groups are created. JIT call component groups are packed together into handling units according to the production sequence at the customer. Delivery and processing at supplier and customer of those handling units must follow the production sequence as well.

For managing delivery and processing in sequence, the following conditions are necessary:

- Subsequent alternative handling unit IDs are used for each delivery sequence
- Component group materials could be grouped together to follow a common delivery sequence

The alternative handling unit number is the concatenation of prefix, the number between from-value and to-value, and suffix.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Master Data Specialist - Just-In-Time Supply (SAP_BR_MD_SPECIALIST_JIT). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage JIT Delivery Sequence Groups for Sequence JIT Calls (F4879) app. |  |  |
| 3 | Create JIT delivery sequence groups | Click on Create to create a new JIT delivery sequence group. | Object screen is displayed to create a new JIT delivery sequence group |  |
| 4 | Maintain JIT Delivery Sequence Group | On Just-In-Time Delivery Sequence Group screen, make the following entries and choose Save:HeaderDescription: <fill in the description without any spaces>Customer: 33154802Plant: 3310Customer Supply Area: RO_PSA_01Number SettingsTo add number settings, choose Add Normal Setting.Prefix: <fill in the description without any spaces>From: 00001To: 99999Length of Short Number: 3Customer Supply Control Assignments.Customer Supply Control: To add customer supply control assignments, choose Add. Assign the supply control created for material FG032 in previous steps.Packing Group Specification AssignmentIn the Packing Group Specification Assignment facet, choose Create. Then assign the packing group specification created for material FG032 in the previous step. You must also specify appropriate Valid From and Valid To dates for this assignment. |  |  |
| 5 | Save the Entries | Choose Save and Activate | The status of the delivery sequence group is set to Active. |  |

#### Create Just-In-Time Teams and Define Responsibilities

Purpose

To create different teams for processing JIT calls by component groups (JIT1CG) and packing groups (JIT1PG).

Multiple teams could be created based on different team types per standard team category of component group/packing group. Responsibility definitions can be maintained for each team as pre-filters. Users can be assigned as team members and various functions shall be assigned for each user.

The user can log on to different applications (as mentioned below) to perform business processes based on the team to which he/she is assigned.

Team definition is a prerequisite to be able to perform business processes via applications:

- Process Customer JIT Calls – by Scan/Data Entry
- Manage JIT Customer JIT Call – by Component Groups
- Manage JIT Packing Groups

Prerequisites

- If you are using a standard business user as Team Member to perform business operations (using the above mentioned applications), you must assign the appropriate business roles authorized to perform the business operations (Refer to Overview table above) to the respective business user.

For example, if you are using the business user Material Planner Just-In-Time Supply (MATL_PLNR_JIT_S_TO_C) as a team member and would like to perform confirm production, then you need to assign role SAP_BR_PRODN_OPTR_LEAN_MFG to that business user.

- If you are creating your own business user assign this newly created business user as team member to perform various business operations using the above mentioned applications, you need to assign the appropriate business roles authorized to perform the business operations (Refer to Overview table above) to the business user created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the roleBusiness Process Specialist (SAP_BR_BUSINESS_PROCESS_SPEC). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Teams and Responsibilities (F5787). |  | Access the SAP Fiori App |
| Create a Team for Release Summarized JIT Calls to Production and Confirm Production activity |  |  |  |  |
| 3 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 4 | Maintain JIT Teams | On Team screen, make the following entries:HeaderDescription: <fill in the description>Name: <fill in the name>Global ID: <fill in the ID / Use auto-populated ID>Type: Process JIT Call Component Groups Generally (JIT1CGGEN)Status: EnabledResponsibility Definitions:Component Group Material: FG031, FG032Customer Supply Area: RO_PSA_01JIT Customer: 33154801, 33154802Plant: 3310Team MembersClick on Create and <Select a team member who would be performing Release Summarized JIT Call to Production and Confirm Production business processes>.Click on OK.In Function field click on F4 (Value help), select the following functions and click on OK.S1_JC_R2P (Release Summarized JIT Call to Production)S1_JC_CP (Confirm Production) |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 5 | Save the Entries | Choose Save. | The status of the team is set to Enabled. |  |
| Create a Team for Release Sequenced JIT Calls to Production |  |  |  |  |
| 6 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 7 | Maintain JIT Team | On Team screen, make the following entries:HeaderName: <fill in the name>Description: <fill in the description>Global ID: <fill in the ID / Use auto-populated ID>Type: Release Production for JIT Packing Groups (JIT1PGRPR)Status: EnabledResponsibility Definitions:Customer Supply Area: RO_PSA_01JIT Customer: 33154802Plant: 3310Assign Team MemberClick on Create and <Select a team member who would be performing Release Sequenced JIT Call to Production business processes>.Click on OK.In Function field click on F4 (Value help), select the following function and click on OK.S1_PG_R2P (Release Sequenced JIT Call to Production) |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 8 | Save the Entries | Choose Save. | The status of the team is set to Enabled. |  |
| Create a Team for Packing activities and HU creation for Sequenced JIT Calls |  |  |  |  |
| 9 | Create JIT Team | Click on Create to create a new JIT team. | Object screen is displayed to create a new JIT team |  |
| 10 | Maintain JIT Team | On Team screen, make the following entries:HeaderName: <fill in the name>Description: <fill in the description>Global ID: <fill in the ID / Use auto-populated ID>Type: Process JIT Packing Groups Generally (JIT1PGGEN)Status: EnabledResponsibility Definitions:Customer Supply Area: RO_PSA_01JIT Customer: 33154802Plant: 3310Assign Team MemberClick on Create and <Select a team member who would be performing Release to Packing, Confirm Packing and Create Handling Unit from Package Group business processes>.Click on OK.In Function field click on F4 (Value help), select the following functions and click on OK.S1_PG_RPCK (Release to Packing)S1_PG_PACK (Confirm Packing)S1_PG_HUCR (Create Handling Unit from Package Group) |  | After selecting Team Type, press Enter to refresh responsibility definition fields. |
| 11 | Save the Entries | Choose Save. | The status of the team is set to Enabled. |  |

## Overview Table

The Automotive Supply to Customer – Inventory Management scenario consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Sales Scheduling Agreement: |  |  |  |
| [Create Sales Scheduling Agreement without JIT](#unique_24) [page ] 45 | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | Create scheduling agreement without JIT |
| [Create Sales Scheduling Agreement for Summarized JIT](#unique_25) [page ] 46 | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | Create scheduling agreement for Summerized JIT |
| [Create Sales Scheduling Agreement for Sequenced JIT with Consignment](#unique_26) [page ] 48 | Internal Sales Representative | Manage Sales Scheduling Agreements (F3515) | Create scheduling agreement for Sequenced JIT |
| [Update Scheduling Agreement for Forecast Delivery Schedule Manually](#unique_27) [page ] 49 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32) | Manually maintain the forecast delivery schedule. |
| [Maintain Planning Delivery Schedule Instruction (Optional)](#unique_28) [page ] 50 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32) | Maintain planning delivery schedule instruction. |
| [Generate Planning Delivery Schedule (Optional)](#unique_29) [page ] 51 | Internal Sales Representative | Change Sales Scheduling Agreements (VA32) | Manually generate planning delivery schedule. |
| [Check Planning Delivery Schedule (Optional)](#unique_30) [page ] 51 | Internal Sales Representative | Display Sales Scheduling Agreements (VA33) | Check planning delivery schedule. |
| [Sales Scheduling Agreements - Product Demand](#unique_31) | Internal Sales Representative | Sales Scheduling Agreements - Product Demand (F4508) | Have an insight of customer demand |
| [Create Customer Sequenced Just-In-Time Call Manually](#unique_32) [page ] 55 | Material Planner - Just-In-Time Supply | Manage Customer JIT Calls (F6078) | Create Sequence JIT calls |
| [Create Customer Summarized Just-in-Time Call Manually](#unique_33) [page ] 53 | Material Planner - Just-In-Time Supply | Manage Customer JIT Calls (F6078) | Create Summerized JIT calls |
| [Monitor Customer JIT Calls](#unique_34) [page ] 57 | Material Planner - Just-In-Time Supply | Monitor Customer JIT Calls - Component Groups (F4749) | Monitor status of JIT calls |
| [Create JIT Delivery Schedule – Background Job (Optional)](#unique_35) [page ] 58 | Material Planner - Just-In-Time Supply | Schedule JIT Delivery Schedule Creation - For Customer JIT Calls (F5001) | Create JIT Delivery Schedule |
| [Demand analysis of JIT Calls](#unique_36) [page ] 59 | Material Planner - Just-In-Time Supply | Demand Analysis - For Customer JIT Calls (F3009) | Analysis of JIT calls |
| [Evaluating Stock/Requirements Situation](#unique_37) [page ] 60 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock / Requirements situation is evaluated. |
| [Schedule MRP Run](#unique_38) [page ] 61 | Production Planner | Schedule MRP Runs (F1339) | MRP run executed for Finished Goods and its component materials. |
| [Evaluating Stock/Requirements Situation](#unique_39) [page ] 62 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock / Requirements situation is evaluated. |
| Procurement of semi-finished material based on Purchase Scheduling Agreement: |  |  |  |
| Procurement of semi-finished material based on Purchase Scheduling Agreement: |  |  |  |
| [Display Delivery Schedule](#unique_40) [page ] 65 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | A Delivery Schedule of purchase scheduling agreement is displayed. |
| [Print Scheduling Agreement (Optional)](#unique_41) [page ] 66 | Purchaser | Manage Purchase Scheduling Agreements (F2179) | Schedule Agreement is printed. |
| [Create Inbound Delivery](#unique_42) [page ] 67 | Receiving Specialist | Inbound Deliveries for Purchase Orders (VL34) | Create Inbound Delivery |
| [Confirm Quantities for Putaway](#unique_43) [page ] 68 | Receiving Specialist | Inbound Deliveries for Putaway (VL06IP) | Confirm Putaway |
| [Post Goods Receipt for Inbound Delivery](#unique_44) | Receiving Specialist | Change Inbound Delivery (VL32N) | Goods receipt is posted against Inbound Delivery |
| [Evaluating Stock/Requirements Situation (Optional)](#unique_45) [page ] 70 | Material Planner - External Procurement | Monitor Material Coverage - Net / Individual Segments (F2101A) | The stock/requirement situation is displayed. |
| [Execute Evaluated Receipt Settlement](#unique_46) [page ] 71 | Accounts Payable Accountant | Schedule Supplier Invoice Jobs - Advanced (F1683) | The ERS is executed. |
| [Check Supplier Invoice List (Optional)](#unique_47) [page ] 73 | Accounts Payable Accountant | Supplier Invoices List (F1060A) | The Credit Memo is displayed and sent. |
| [Display Procurement Overview (Optional)](#unique_48) [page ] 74 | Purchaser | Procurement Overview (F1990) | Cards for various procurement documents displayed. |
| Repetitive Production Execution: |  |  |  |
| [Release Summarized JIT Call Component Groups to Production](#unique_49) [page ] 75 | Production Planner - Lean Manufacturing | Release Summarized JIT Calls to Production - Deprecated (F4330) | Release Summerized JIT Calls |
| [Schedule Packing Group Creation / Update](#unique_50) [page ] 76 | Shipping Specialist - Just-In-Time Supply | Schedule Packing Group Creation/Update (F4960) | Packaging Unit is created for sequential JIT call |
| [Release Sequenced JIT Call Component Groups to Production](#unique_51) [page ] 77 | Production Planner - Lean Manufacturing | Release Sequenced JIT Calls to Production - Deprecated (F4331) | Release Sequential JIT Calls |
| [Check Planning in Planning Table (Optional)](#unique_52) [page ] 78 | Production Supervisor - Repetitive Manufacturing | Manage Repetitive Manufacturing (MF50) | The Planning Table Initial Screen: Change Mode displays. |
| [Check Range of Stock Coverage](#unique_53) [page ] 79 | Production Planner | Monitor Material Coverage - Net Segments (F0247A) | The Monitor Material Coverage screen displays. |
| [Material Staging](#unique_54) [page ] 80 | Production Operator - Repetitive Manufacturing | Stage Materials for Production (MF60) | The Material Staging for Planned Orders screen displays. |
| [Confirm Repetitive Manufacturing Inclusive Backflush of Materials for (non-JIT)](#unique_55) [page ] 82 | Production Operator - Repetitive Manufacturing | Confirm Repetitive Manufacturing (MFBF) | The REM Confirmation - Transaction Variant: None screen displays. |
| [Post Processing of Error Records for non-JIT production](#unique_56) [page ] 84 | Production Operator - Repetitive Manufacturing | Reprocess REM Goods Movements (MF47) | The Postprocessing List for Components on Line: Initial Screen displays. |
| [Confirm Production of JIT Calls (Alternative)](#unique_57) [page ] 85 | Production Operator - Lean Manufacturing | Manage Customer JIT Calls - By Component Groups (F6077) | confirm Production of JIT Calls , updates status |
| [Reprocessing of Failed Stock Posting After Confirmation of Production (Optional)](#unique_58) [page ] 86 | Production Supervisor - Lean Manufacturing | Manage Reprocessing List - For Customer JIT Calls (F5092) | Reprocessing of JIT calls |
| [Manage JIT Packing Groups](#unique_59) [page ] 87 | Material Planner - Just-In-Time Supply | Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) | Release packing is done |
| [Schedule Goods Movement from Production for Customer JIT Calls (Optional)](#unique_60) [page ] 101 | Production Operator - Lean Manufacturing | Schedule goods movement from production for customer JIT calls (F5168) | Confirmation of JIT calls , goods movement posted |
| [Stock availability analysis for JIT Calls](#unique_61) [page ] 88 | Material Planner - Just-In-Time Supply | Stock Availability Analysis (F3923) | Stock/Requirements situation for the planned materials are analyzed. |
| [Evaluating Stock/Requirements Situation (Optional)](#unique_62) [page ] 89 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned materials are analyzed. Stock of material produced should increase. |
| Outbound Delivery to Customer |  |  |  |
| [Scheduling Agreement Non-JIT-Create Delivery](#unique_63) | Shipping Specialist | My Sales Order Schedule Lines - Due for Delivery (VL10E) | Outbound delivery is created for Without JIT calls. |
| [Scheduling Agreement Non-JIT-Execute Picking](#unique_64) | Shipping Specialist | Outbound Delivery for Picking (VL06P) | The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. |
| [Scheduling Agreement Non-JIT-Execute Automatic Packing](#unique_65) | Shipping Specialist | Change Outbound Delivery (VL02N) | Packing for outbound delivery is completed. |
| [Summarized JIT Calls-Create Outbound Delivery from Summaried JIT Calls](#unique_66) | Shipping Specialist - Just-In-Time Supply | Create Outbound Deliveries - From Summarized JIT Calls (F3922) | Outbound delivery is created for Summerized JIT calls |
| [Summarized JIT Calls-Execute Picking](#unique_64) | Shipping Specialist | Outbound Delivery for Picking (VL06P) | The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. |
| [Summarized JIT Calls-Execute Automatic Packing](#unique_65) | Shipping Specialist | Change Outbound Delivery (VL02N) | Packing for outbound delivery is completed. |
| [Sequenced JIT Call-Create Handling Units from Packing Groups for Sequenced JIT Calls](#unique_67) | Material Planner - Just-In-Time Supply | Schedule Handling Units Creation (F5260) | Handling Units created from Package Groups for Sequenced JIT Calls |
| [Sequenced JIT Call-Create Outbound Delivery from Sequenced JIT Calls](#unique_68) | Shipping Specialist - Just-In-Time Supply | Create Outbound Deliveries from Sequenced JIT Calls (F3897) | Outbound delivery is created for Sequential JIT calls |
| [Post Goods Issue](#unique_69) [page ] 102 | Shipping Specialist | Outbound Deliveries for Goods Issue (VL06G) | Goods Issue is posted. |
| Consignment Issue |  |  |  |
| [Check Stock Overview](#unique_70) [page ] 103 | Shipping Specialist | Stock - Multiple Materials (F1595) | Stock/Requirements situation for the planned materials are analyzed. |
| [Create Consignment Issue Order with Reference to Scheduling Agreement Manually (non-JIT)](#unique_71) [page ] 104 | Internal Sales Representative | Manage Sales Orders (F1873) | Consignment order is created |
| [Create JIT Delivery Confirmation](#unique_72) [page ] 106 | Configuration Expert - Business Network Integration | Communication Arrangements (F1763) | JIT Delivery Confirmation is created |
| [Release Delivery Confirmation for Sequenced JIT](#unique_73) [page ] 107 | Material Planner - Just-In-Time Supply | Manage JIT Delivery Confirmations (F5268) | Release JIT Delivery Confirmation |
| [Create Delivery (Automatically)](#unique_74) [page ] 108 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Delivery is created agaisnt Consignment order |
| [Post Goods Issue](#unique_75) [page ] 108 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | An advanced shipping notification is sent to the Buyer system. |
| [Check Stock Overview](#unique_76) [page ] 109 | Shipping Specialist | Stock - Multiple Materials (F1595) | Stock/Requirements situation for the planned materials are analyzed. |
| Create Billing: |  |  |  |
| [Create Billing Document](#unique_77) [page ] 110 | Billing Clerk | Create Billing Documents (F0798) | Invoice is created and sent from the SAP S/4HANA system (supplier side) to the buyer system. |
| [Job Scheduling for Billing Creation (Alternative)](#unique_78) | Billing Clerk | Schedule Billing Creation (F1519) | Background job for billing document creation is scheduled. |
| Accounts Receivable: |  |  |  |
| [Post Incoming Payments](#unique_79) [page ] 113 | Accounts Receivable Accountant | Post Incoming Payments for Japan - For Customers (FBZ1) (F1345). | Incoming Payment is posted. |
| Accounts Payable: |  |  |  |
| [Post Outgoing Payment](#unique_80) | Accounts Payable Accountant | Post Outgoing Payments (F1612) . | Outgoing Payment is posted. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Sales Scheduling Agreement

#### Create Sales Scheduling Agreement

Purpose

This process step shows you how to create a Scheduling Agreement. The Scheduling Agreement Type has to be chosen according to the desired process

- LZ for a process with Sales Scheduling Agreements, without consignment and without JIT
- LK for a process with Sales Scheduling Agreements and Customer Consignment, without JIT
- LZJ for a Sales Scheduling Agreement with Summarized JIT, without Customer Consignment
- LKJ for a Sales Scheduling Agreement with Sequenced JIT and Customer Consignment

##### Create Sales Scheduling Agreement without JIT

Purpose

This process step shows you how to create a Scheduling Agreement. The Scheduling Agreement Type has to be chosen according to the desired process

- LZ for a process with Sales Scheduling Agreements, without consignment and without JIT
- LK for a process with Sales Scheduling Agreements and Customer Consignment, without JIT

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Scheduling Agreements (F3515). |  |  |
| 3 | Navigate to Create Scheduling Agreement Screen | On the Manage Sales Scheduling Agreements screen, choose Create Scheduling Agreements. |  |  |
| 4 | Enter Data | On the Create Scheduling Agreements screen, make the following entries and choose Continue:Sched. Agreemt Type: LZSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Scheduling Agreement Details | On the Create Sched. Agr. w/Rel: Overview screen, make the following entries:Sold-To Party: 33100020Ship-To Party: 33100020Customer Reference: Purchase scheduling agreement number from customerMaterial : FG031Customer Material Number: from customer- Material Info Record if maintained example RSD129 |  |  |
| 6 | Save Document | Choose Save.Make a note of the scheduling agreement number: __________.Note If you have created a scheduling agreement with the same data in your system and you use material FG031 and customer 33100020, the following warning may appear:There is already a scheduling agreement with this same data.To skip this warning, choose Enter. |  |  |
| 7 | Create another Sales Scheduling Agreement | Repeat steps 3 to 6 with ,Sched. Agreemt Type: LK |  |  |

##### Create Sales Scheduling Agreement for Summarized JIT

Purpose

This process step shows you how to create a Scheduling Agreement. The Scheduling Agreement Type has to be chosen to the desired process.

This is a scenario with Summarized JIT without consignment. Scheduling agreement type to be chosen is LZJ

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Scheduling Agreements (F3515). |  |  |
| 3 | Navigate to Create Scheduling Agreement Screen | On the Manage Sales Scheduling Agreements screen, choose Create Scheduling Agreements. |  |  |
| 4 | Enter Data | On the Create Scheduling Agreements screen, make the following entries and choose Continue:Sched. Agreemt Type: LZJSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Scheduling Agreement Details | On the Create Sched. Agr. w/Rel: Overview screen, make the following entries:Sold-To Party: 33154801Ship-To Party: 33154801Customer Reference: Purchase scheduling agreement number from customerMaterial : FG031Customer Material Number: from customer- Material Info Record if maintained example: RSD129_JIT |  |  |
| 5 | Maintain Header Data | Go to Menu -> Goto -> Header -> SalesCheck the following data:MRP for DS type :A-Requirements acc. to fore.dlv.sched/Delivery acc. to validity |  |  |
| 6 | Save Document | Choose Save.Make a note of the scheduling agreement number: __________.If you have created a scheduling agreement with the same data in your system and you use material FG031 and customer 33154801, the following warning may appear:There is already a scheduling agreement with this same data.To skip this warning, choose Enter. |  |  |

##### Create Sales Scheduling Agreement for Sequenced JIT with Consignment

Purpose

This process step shows you how to create a Scheduling Agreement. The Scheduling Agreement Type has to be chosen according to the desired process.

This is a scenario with Sequenced JIT with consignment. The scheduling agreement type to be chosen is LKJ.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Scheduling Agreements (F3515). |  |  |
| 3 | Navigate to Create Scheduling Agreement Screen | On the Manage Sales Scheduling Agreements screen, choose Create Scheduling Agreements. |  |  |
| 4 | Enter Data | On the Create Scheduling Agreements screen, make the following entries and choose Continue:Sched. Agreemt Type: LKJSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Scheduling Agreement Details | On the Create JIT Sched Agr w/cne: Overview screen, make the following entries:Sold-To Party: 33154802Ship-To Party: 33154802Customer Reference: Purchase scheduling agreement number from customerMaterial : FG032Customer Material Number: from customer- Material Info Record if maintained Example: RSD129_SEQ_CNJIT |  |  |
| 6 | Enter Storage Location | On the Create JIT Sched Agr w/cne: Item Data screen, select the Item line and choose Display Item Details.Go to Shipping Tab and enter the following valuesStorage Location: 331A. |  |  |
| 7 | Maintain Header Data | Select Go to > Header > SalesCheck the following data:MRP for DS type: A-Requirements acc. to fore.dlv.sched/Delivery acc. to validity |  |  |
| 8 | Save Document | Choose Save.Make a note of the scheduling agreement number: __________.If you have created a scheduling agreement with the same data in your system and you use material FG032 and customer 33154802, the following warning may appear:There is already a scheduling agreement with this same data.To skip this warning, choose Enter. |  |  |

#### Update Scheduling Agreement for Forecast Delivery Schedule Manually

Purpose

This process step shows you how to manually create the forecast delivery schedule in predefined scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Change Sales Scheduling Agreements (VA32). |  |  |
| 3 | Choose Scheduling Agreement | On the Change Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Choose Forecast Delivery Schedule | On the Change Sched.Agr.w/ Rel. XXXXXXXX: Overview screen, choose the line Item and choose Fore. DlSch. |  |  |
| 5 | Enter the Forecast Delivery Schedule | On the Change Sched.Agr.w/ Rel. XXXXXXXX: Item Data screen, make the following entries and choose Enter.Dlv. Schedule: 0 (Del.sched.no. must be different from the previous one, so in case of existings ones choose previous no. +1)Dlv. Sched. Date: <Today>Date Type: WDate: <Today>Order Quantity: <6>Create similar entries for next 3 weeks. |  |  |
| 6 | Save Document | Choose Save to save your changes. |  |  |

#### Maintain Planning Delivery Schedule Instruction (Optional)

Purpose

This process step shows you how to maintain planning delivery schedule instruction.

|  |
| --- |
| Note The step is only relevant that if you want to create planning delivery schedule according to forecast delivery schedule. Planning delivery schedule only relevant to the forecast delivery schedule based on week or Month. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Sales Scheduling Agreements (VA32). |  |  |
| 3 | Choose Scheduling Agreement | On the Change Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Navigate to Item level | On the Change Sched.Agr.w/ Rel.XXXXXXXX: Overview screen, choose the Item line, and choose Display Item Details |  |  |
| 5 | Enter Planning Delivery Schedule Instruciton | On the Change Sched.Agr.w/ Rel.XXXXXXXX: Item Data screen, choose Call Control Parameter and make the following entries:PlanDS instruction: SAP1 |  |  |
| 6 | Save Document | Choose Save. |  |  |

#### Generate Planning Delivery Schedule (Optional)

Purpose

This process step shows you how to generate planning delivery schedule manually.

Prerequisite

Planning delivery schedule instruction has been set. Forecast delivery schedule has been created manually with date type week or month. For delivery schedule generated via EDI, planning delivery schedule will generate automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Change Sales Scheduling Agreements (VA32). |  |  |
| 3 | Choose Scheduling Agreement | On the Change Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Navigate to Item level | On the Change Sched.Agr.w/ Rel.XXXXXXXX: Overview screen, choose the Item line, and choose Display Item Details. |  |  |
| 5 | Enter Planning Delivery Schedule Instruction | On the Change Sched.Agr.w/ Rel.XXXXXXXX: Item Data screen, choose Planning Delivery Schedule, and choose Generate plan. dlv.sched. |  |  |
| 6 | Save Document | Choose Save. |  |  |

#### Check Planning Delivery Schedule (Optional)

Purpose

This optional process step shows you how to check plannig delivery schedule.

Prerequisite

Planning delivery schedule is generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. |  |  |
| 2 | Access the App | Open Display Sales Scheduling Agreements (VA33). |  |  |
| 3 | Choose Scheduling Agreement | On the Display Scheduling Agreements screen, make the following entries and choose Enter:Scheduling Agreement: <Created in previous step> |  |  |
| 4 | Navigate to Item level | On the Display Sched.Agr.w/ Rel.XXXXXXXX: Overview screen, choose the item line, and choose Display Item Details. |  |  |
| 5 | Enter Planning Delivery Schedule Instruciton | On the Display Sched.Agr.w/ Rel.XXXXXXXX: Item Data screen, choose Planning Delivery Schedule. |  |  |

#### Sales Scheduling Agreements – Product Demand

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you as an internal sales representative can

Have an insight of customer demand on different delivery schedule versions. It helps user see customer demands are fluctuated in certain period.

Have an insight of customer demand for one product

Have an insight between demand and supplier for one product in certain period.

Have an insight of customer demand of different products for one customer

Have a possibility of navigating from high level demand view into detail level view as well as fulfillment overview

Have an insight of delivery reliability on sales scheduling agreement

Have an insight of open schedule lines for scheduling agreements and drill down to find issue

It is possible to drill down to the detail view to analyze the demand fluctuation on schedule line level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Sales Scheduling Agreements – Product Demand (F4508) . | The app is opened. |  |
| 3 | Set Filters | Set filters for Release Type, Time Period, Delivery Date Range and other filters if necessary, and then choose Go. | The chart and table are shown according to the filters. |  |
| 4 | Check Visual Filter | Click Visual Filter to change the filter mode to visual filter. | The filter is changed to Visual Filter and it’s consistent with Compact Filter. |  |
| 5 | Drill Down in Chart and Table | Choose View By in the chart to analyze in more dimensions, for example select Sales Organization. | The data displayed in the chart and table changes accordingly. |  |
| 6 | View Settings | Choose Settings in chart view, more settings can be done for Chart, Sort and Filter.Choose Settings in table view, more settings can be done for Columns, Sort, Filter and Group. | The Chart and Table can be set as needed. |  |
| 7 | View Management | You can define, save, and share separate views for filter, chart, and table sections.To apply some filters in the section, choose the Select View icon. On the My Views screen, choose Save As. On the Save Viewscreen, enter view name and mark the necessary checkbox, then choose Save. You can also manage the view by choosing Manage on the My Views screen. | The views can be defined, saved, shared, and managed. |  |
| 8 | Share the App | Choose the Share icon at the right top of the screen. It can share the app for quick and easy accessibility. The following options listed are possible:• Send Email• Save as Tile | Tile sharing with an email, or as a tile on the SAP Fiori launchpad is possible. |  |

#### Create Customer Just-in-Time Call

##### Create Customer Summarized Just-in-Time Call Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Post sales scheduling agreement for summarized process , JIT calls are placed

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls (F6078) |  |  |
| 3 | Create JIT Call | Choose Create. |  |  |
| 4 |  | On Manage Customer JIT Calls screen, make the following entry and choose Save:Header DetailsExternal Call Number: <Number to identify the JIT call uniquely from customer perspective>Call Type: Summarized JIT CallMaterial Usage Indicator: S SeriesReorder: NoPartner DataPartner Description of Ship-To Party: P001Description of Supplier: <Description>Ship-To Party ID: 33154801 | Summarized JIT Call is created and transmitted to vendor via IDOC. |  |
| 5 | Add Components | To add components into a JIT call, navigate to Components facet and choose Create. | Dialog box to maintain components appears. |  |
| 6 |  | Make the following entries. Choose Apply after maintaining the below components:First ComponentCustomer Material Number: <Customer Material Number maintained in Scheduling Agreement>Customer Supply Area: RO_PSA_01Unloading Point: UL01Customer Assembly Location: <Body Shop>Transmitted External Status: SNEWRequirement Data and Time: <Enter the requirement date>Requested Quantity: 4 | The following are derived and auto-filled:Internal Material NumberInternal Material Desc.Sales Scheduling Agreement No.Sales Scheduling Agreement ItemUnloading PointShipping PointPlantStorage LocationCustomer Supply Area Desc.Assembly Location |  |
| 7 |  | Choose Create. | Dialog box is closed and the component groups are derived automatically, either based on the BADI implementation or on rules set in the SAP Business Rules service or default component group determination.The following entries appear for component group.Component Group NumberExternal Call StatusInternal Processing StatusComponent Group MaterialRequirement DatePlantCustomer Supply ControlCustomer Supply Area |  |

##### Create Customer Sequenced Just-In-Time Call Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Post sales scheduling agreement for sequence process , Sequenced JIT calls are placed

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls (F6078) |  |  |
| 3 | Create JIT Call | Choose Create. |  |  |
| 4 |  | On Manage Customer JIT Calls screen, make the following entries:Header DetailsExternal Call Number: <Number to identify the JIT call uniquely from customer perspective>Call Type: Sequenced JIT CallMaterial Usage Indicator: S SeriesReorder: NoVehicle InformationVehicle Number: <Vehicle No.>Vehicle Model: <Vehicle Model>External Sequence Number: <Sequence No.> (Important for appropriate processing of sequenced JIT calls)Partner DataPartner Description of Ship-To Party: <P001>Partner Description of Supplier: 33154802 | The following attributes are derived and populated automatically:Ship-To PartySold-To PartySales OrganizationDistribution ChannelDivisionUnloading Point |  |
| 5 | Add Components | To add components into a JIT call, navigate to Components facet and choose Create. | Object page for maintaining data related to component material is displayed. |  |
| 6 |  | Make the following entries in the object page. Choose Apply after maintaining the below data:Customer Material Number: <Customer Material Number maintained in Scheduling Agreement>External Component Group Number: <Number to group the component groups together> [Optional]Customer Assembly Location: <Body Shop>Customer Supply Area: RO_PSA_01Requested Quantity: 1Requirement Date and Time: <Enter the requirement date>Transmitted External Status: SNEW | The following are derived and auto-filled, while the object page is closed automatically:Component Material NumberComponent Material Desc.Sales Scheduling Agreement No.Sales Scheduling Agreement ItemCustomer Supply Area Desc. |  |
| 7 |  | Choose Create. | The component groups are derived automatically, either based on the BADI implementation or on rules set in the SAP Business Rules service or default component group determination.The following entries are filled for component group:Component Group NumberComponent Group MaterialCustomer Supply ControlInternal Processing StatusRequirement DatePlanned Delivery Creation Date/TimePlanned Goods Issue Date/TimePlantCustomer Supply AreaOnce all the above information is derived successfully, the JIT call is saved and activated with life cycle status Active. |  |

#### Monitor Customer JIT Calls

Purpose

In this step, you monitor and analyse JIT call component groups based on internal processing status.

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
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Customer JIT Calls - Component Groups (F4749) app. |  |  |
| 3 | Select Criteria | Enter the following search criteria and press GOShip-To-Party: <Ship-To-Party from scheduling agreement> | Component Groups , External JIT Call Number and Internal Processing Status is displaydd |  |
| 4 | Select Line | Select an entry | Detailed information is displayed |  |

#### Create JIT Delivery Schedule – Background Job (Optional)

Purpose

In this step, you schedule a background job to create JIT delivery schedules.

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
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule JIT Delivery Schedule Creation - For Customer JIT Calls (F5001) app. |  |  |
| 3 | Create a New Job | Choose Create to create a new job. | Template section is displayed with appropriate job template by default. |  |
| 4 | Maintain Schedule Information | Choose Step 2.Make the following entries and choose Schedule:Scheduling Options - Choose Start Immediately or define the recurring pattern and maintain the scheduling information.Choose Step 3. | Delivery schedule background job is scheduled. |  |

#### Demand analysis of JIT Calls

Purpose

In this step, you monitor and analyse JIT call component groups based on internal processing status.

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
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Demand Analysis - For Customer JIT Calls (F3009) app. |  |  |
| 3 | Select Criteria | Enter the following search criteria and press GoDeviation Profile: <choose a profile>Sales Scheduling Agreement: <sales scheduling agreement created above>Time Horizon: NEXT30DAYSView Type: Forecast Delivery ScheduleNote If deviation profile is missing, please maintain the same using app - "Manage Deviation Profiles" | Customer Requirements within the selected horizon are displayed |  |
| 4 |  | Bar chart of quantity deviations is displayedSelect scheduling agreement in table view to see details | Comparison of Schedule Line Quantity and JIT Requested Quantity on daily and cumulative basis are displayed. |  |

#### Evaluating Stock/Requirements Situation

Purpose

This process step shows you how to display the stock/requirements situation for the finished product.

Prerequisite

No prerequisites necessary.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Material Planner - External Procurement. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A) | The Monitor Material Coverage screen displays. |  |
| 3 | Select Criteria | In the Material field, enter the following materials and choose GO. Material: FG031 , SG031 and SG032 | The Material screen and Material Details screen display. | Stock Availability situation for all materials displays. |
| 4 | Review Stock Availability | Analyze the stock availability situation of materials FG031 , SG031 and SG032. |  | The stock availability situation of the materials is noted from the Shortage Quantity and Stock Availability columns. |
| 5 | Selection of Materials | Use the Check box and select the rows which have FG031 , SG031 and SG032 as the Material No and click Manage Materials |  | The Material and Material Details screens display. Stock/Requirement list for all the selected materials is displayed. Rows with SchLne items are displayed for the finished product. |
| 6 | Repeat Pro-cess for other finished good | Repeat steps 3 - 5 for JIT Sequence process with material FG032,SG032 and SG033 |  |  |

#### Schedule MRP Run

Purpose

This process step shows you how to schedule MRP run for material with scheduling change agreements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG031>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: FG031Changed BOM Components: selectAll Order BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG031 in the search box and choose Go at the top right of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |
| 5 | Repeat Process for other finished good | Repeat steps 3 and 4 for the following Material:FG032 |  |  |

#### Evaluating Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for the finished product.

Prerequisite

Requirement planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A) | The Monitor Material Coverage screen displays. |  |
| 3 | Select Criteria | In the Material field, enter the following materials and choose GO.Material: FG031 , SG031 and SG032 | The Material screen and Material Details screen display. | Stock Availability situation for all materials displays. |
| 4 | Review Stock Availability | Analyze the stock availability situation of materials FG031 , SG031 and SG032 . |  | The stock availability situation of the materials is noted from the Shortage Quantity and Stock Availability columns. |
| 5 | Selection of Materials | Use the Check box and select the rows which have FG031, SG031 and SG032 as the Material No and click Manage Materials on the screen |  | The Material and Material Details screens display.Stock/Requirement list for all the selected materials is displayed.Rows with SchLne items are displayed for the finished product. |
| 6 | Review Stock/Requirements List | Select the corresponding material on the left Material screen. | The detailedStock/Requirements List for each material displays. |  |
| 7 | Open Quickview for MRP Element | On the Material Details screen, click the SchLne XXXX in columnMRP Element. | The SchLne XXX you clicked will display on the pop-up. |  |
| 8 | Open Scheduling Agreement | On the Pop-up SchLne XXX screen, choose Open and then select Scheduling Agreement | The Display Scheduling Agreement: Item Overview screen displays. |  |
| 9 | Display Planned Order | From the list on the Material screen on your left, select the material for which you want to check for the planned order.Material: FG031On the Material Details screen, choose PldOrd XXXX in the MRP Element column.Note If no planned orders are generated, it could be because the finished product has sufficient amount of stock in store. In this case, remove some stock. Run MRP again to generate planned orders. If there is no sufficient stock for the finished product, system generates planned orders. | The selected planned order details are displayed on pop-up screen.The planned order is generated only when there is storage for these materials.If you want to display more information of the planned order, choose Open > Planned Order at the bottom right of the dialog box.Note down the planned order number. |  |
| 10 | Display Purchase Requisition (Optional) | From the list on the Material sub screen on your left, select the material for which you want to check for the Purchase Requisition.Material: SG031On the Material Details sub screen, choose PldOrd XXXX in the MRP Element column.Note The BOM explosion during the MRP run has generated dependent requirements for the planned components. If there is not enough inventory to fulfill the requirements, planned orders and purchase requisitions are created for both in-house-produced and externally-procured materials. | The selected purchase Requistion details are displayed on pop-up screen.The Purchase Requisition is generated only when there is storage for these materials.If you want to display more information of the Purchase Requisition, choose Open > Document Info at the bottom right of the dialog box.Note down the Purchase Requistion number. |  |
| 11 | Display Purchase Requisition (Optional) | From the list on the Material screen on your left, select the material for which you want to check for the planned order.Material: SG032On the Material Details screen, choose PldOrd XXXX in the MRP Element column.Note If no planned orders are generated, it could be because the finished product has sufficient amount of stock in store. In this case, remove some stock. Run MRP again to generate planned orders. If there is no sufficient stock for the finished product, system generates planned orders. | The selected purchase Requistion details are displayed on pop-up screen.The Purchase Requisition is generated only when there is storage for these materials.If you want to display more information of the Purchase Requisition, choose Open > Document Info at the bottom right of the dialog box.Note down the Purchase Requistion number. |  |
| 12 | Rescheduling Check (Optional) | On the Stock/Requirements List tab, the Rescheduling column displays the rescheduling status of the following MRP elements:PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersIf needed,you can choose the following icons in Rescheduling column for corresponding functions:Reschedule in (bring operation forward if the receipt element lies after the requirement date)Reschedule out (postpone operation, if the receipt element lies before the re-quirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment |  |  |
| 13 | Repeat Process for other finished good | Repeat steps 3 - 9 for JIT Sequence process with MaterialFG032 , SG032 and SG033 |  |  |

### Procurement of semi-finished material based on Purchase Scheduling Agreement:

#### Display Delivery Schedule

Purpose

The purpose of this activity is to display the delivery schedule for the scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori launchpad | Log onto the Fiori launchpad using the role Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3 | Find scheduling agreement number | Enter the purchasing scheduling agreement created above or find the appropriate newly created scheduling agreement through the following search criteria and choose GoSupplier: <new supplier created for this scope item>Agreement Type: LPPurchasing Organization: 3310Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4 | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Chevron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5 | Display Delivery Schedule | In Items tab, click on the desired item for which delivery schedule needs to be viewed. | The Purchase Scheduling Agreement Item screen displays. |  |
| 6 | Display Delivery Schedule | Go to the Schedule Lines section on the Purchase Scheduling Agreement Item screen. The schedules for the item generated by MRP are displayed. | You will be navigated back to Scheduling Agreement Header object page. |  |

#### Print Scheduling Agreement (Optional)

Purpose

The purpose of this activity is to print view the scheduling agreement for the product/supplier combination for the new Scheduling agreement or for the one which is already present in the system

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto Fiori launchpad | Log onto the Fiori launchpad as Purchaser . | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Manage Purchase Scheduling Agreements (F2179) . | The Manage Purchase Scheduling Agreements screen displays. |  |
| 3. | Find scheduling agreement number | Enter the purchase scheduling agreement created above or find the appropriate scheduling agreement through the search criteria, such as: Supplier<supplier number created for this scenario>, Agreement Type LP, Purchasing Organization 3310, then choose Go. Select one item from the search result. | The desired scheduling agreement appears on the list page of Manage Purchase Scheduling Agreements. |  |
| 4. | Select Scheduling Agreement | Navigate to the selected scheduling agreement by clicking on Chevron (>) or by directly clicking on the Scheduling agreement number from the list page. | The Scheduling agreement header object page appears in display mode. |  |
| 5. | View the output form for scheduling agreement | Go to the Output controls tab and view the output settings maintained for the scheduling agreement. Click on Show More per Row to see PDF sign | PDF form for scheduling agreement shall open. |  |

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
| 3 | Create Inbound Delivery | Make the following entries and choose Execute:Document Number: XXX (Enter the scheduling agreement number created in previous step for material SG031 and uncheck Test run).Delivery Date: XXX (Delete the default date and enter the delivery date in schedule line).The Inbound Delivery Number is displayed, write it down for further use.Repeat steps 2 and 3 for the SG032 and SG033 material. | A new Inbound Delivery is created.The Inbound Delivery Number is displayed. |  |

#### Confirm Quantities for Putaway

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity confirms that all the materials have been put away in the correct quantities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad using the Role Receiving Specialist . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Inbound Deliveries for Putaway (VL06IP) . | The Inbound Deliveries for Putaway screen displays. |  |
| 3 | Enter inbound delivery number | Make the following entry and choose Execute:Inbound Delivery: XXX created in the previous step for materials SG031 | The selected Inbound Delivery displays. |  |
| 4 | Change the in-bound delivery | Select Inbound deliveries and click Change Inbound Deliveries. | The Inbound Delivery XXX Change: Overview screen displays. |  |
| 5 | Confirm Quantities for Putaway | In Item Overview tab, input the Putaway Qty: XXXNote The put away quantity should equal to the delivery quantity.And choose Save.Repeat the steps for all deliveries. | Back to the Inbound Deliveries for Putaway screen and Inbound Delivery XXX has been saved message displays. |  |
| 6 | Confirm Quantities for Putaway for other materials | Repeat steps 3 -5 for the inbound deliveries created for materials SG032 and SG033 |  |  |

#### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the goods receipt for the material against the inbound delivery of scheduling agreement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto Fiori Launchpad | Log onto the SAP Fiori launchpad as Receiving Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen appears. |  |
| 3 | Enter detail data | On the initial screen, enter the following value then choose Continue:Inbound Delivery Number: Select your inbound delivery using input help. | The Inbound Delivery xxxxxxxxx Change: Overview screen displays. |  |
| 4 | Post Goods Receipt | Choose Post Goods Receipt. | The system message Goods receipt for inbound delivery xxxxxxxxx posted (material Document 500xxxxxxx) appears. The material is posted to the unrestricted use stock with plant Plant 1 AE. You can display the stock overview in APP Display Stock Overview. |  |

#### Evaluating Stock/Requirements Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for semi-finished materials.

Prerequisite

Goods Receipt posting is carried out for semi-finished materials.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage screen displays. |  |
| 3 | Select Criteria | In the Material field, enter the following materials and choose GO.Material: SG031 , SG032and SG033. | The Material screen and Material Details screen display. | Stock Availability situation for all materials displays. |
| 4 | Review Stock Availability | Analyze the stock availability situation of materialsSG031 ,SG032and SG033. |  | The stock availability situation of the materials is noted from the Shortage Quantity and Stock Availability columns. |
| 5 | Selection of Materials | Use the Check box and select the rows which have SG031, SG032and SG033 as the Material No and click Manage Materials on the screen |  | The Material and Material Details screens display.Stock/Requirement list for all the selected materials is displayed.Rows with SchLne items are displayed for the finished product. |
| 6 | Display Stock situation of semi-finished materials | From the list on the Material screen on your left, select the material for which you want to check for the planned order.Material: SG031Observe the stock situation for material | Stock quantity has increased by the quantity of goods receipt done in earlier step. |  |
| 7 | Display Stock situation of semi-finished materials | From the list on the Material sub screen on your left, select the material for which you want to check for the Purchase Requisition.Material: SG032Observe the stock situation for material | Stock quantity has increased by the quantity of goods receipt done in earlier step. |  |
| 8 | Display Stock situation of semi-finished materials | From the list on the Material sub screen on your left, select the material for which you want to check for the Purchase Requisition.Material: SG033Observe the stock situation for material | Stock quantity has increased by the quantity of goods receipt done in earlier step. |  |
| 9 | End of validation | Click the Back button twice. | SAP Fiori App home screen appears. End of validation of stock check.. |  |

#### Execute Evaluated Receipt Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You should only use ERS if agreements with the supplier are clear, and you update the price agreements in the purchase orders in the system. You also need to create goods movements promptly and accurately. Created goods movements can be settled without receipt of an invoice. The system can create and post the appropriate invoices itself. ERS is especially effective if you create settlement documents periodically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Supplier Invoice Jobs - Advanced (F1683). | The Application Jobs screen is displayed. |  |
| 3 | Create Application Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Execute ERS | Make the following entries:For Step 1, in the Template Selection section, from the drop-down box of Job Template, choose Evaluated Receipt Settlement (ERS).Then choose Step 2, in the Scheduling Options section, make sure that Start Immediately checkbox is checked. Or you can also set the start date and start time.Then choose Step 3, in the Parameters section, make the following entries:Company Code: 3310Plant: 3310Goods Receipt Document: Material document number created from the last step.Document Year of Goods Receipt: For example, Current YearSupplier: 33300003Document Selection: 1 <Document Selection per Supplier>Test Run: CheckedChoose Check. | The system message displays: You can go ahead and schedule the job. |  |
| 5 | Schedule the job without Test Run | Uncheck Test Run, and then choose Schedule. |  |  |
| 6 | Check the result | In the Application Jobs screen, find the job you created. You may need to wait several minutes to see the results after the job status becomes finished.Choose Results. | The detailed log is displayed in the Document (ID, XXXXX) screen. You can find the corresponding Document number and FI Document number created. |  |
| 7 | Repeat Steps | Repeat steps 3 to 6 for Supplier :33300063 |  |  |

#### Check Supplier Invoice List (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can review the document created in the last step, and get the generated Credit Memo.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the Fiori Launchpad tile | Open the Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Supplier Invoices List (F1060A). | The Supplier Invoices List screen is displayed. |  |
| 3 | Search for the document | On the Supplier Invoices List screen, enter the following values, then choose Go:Invoicing Party : 33300003, 33300063Company Code: 3310 | Invoices list is displayed. |  |
| 4 | Go to the invoice detailed page | Choose the invoice you created, whose Entry Type is ERS | The screen will be navigated to the Supplier Invoice detailed page. |  |
| 5 | Display the document | On the Supplier Invoice screen, go to the Output tab. In the Output Details table, find the line with Output Type of EVALUATED_RECEIPT_SETTLEMENT. Choose Display Document in the Display column. | The document (in this case, Credit Memo) is displayed. |  |
| 6 | Download the document | Download the document. | The document is downloaded to your local workspace. |  |
| 7 | Send Documents to Supplier (Optional) | Send the downloaded document to the supplier as printed document, or by fax or by e-mail or via the Internet.The step is executed offline. | The document is sent to your supplier. |  |

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
| 3 | Selection criteria | Enter data in following fields and choose GO:Display Currency:AEDPurchasing Organisation: 3310If needed, user can enter more parameters as part of selection criteria. | System displays multiple purchase cards on the screen. |  |

### Repetitive Production Execution

#### Release Summarized JIT Call Component Groups to Production

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release a summarized JIT call to production.

Procedure

|  |
| --- |
| Note If you are using a standard business user as Team Member to perform business operations, you must assign the appropriate business roles authorized to perform the business operations to the respective business user. For example, add Material Planner Just-In-Time Supply (MATL_PLNR_JIT_S_TO_C) to Production Planner - Lean Manufacturing (PRODN_PLNR_LEAN_MFG). |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Planner - Lean Manufacturing . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) App. |  |  |
| 3 | Filter JIT Calls to be Released for Production | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for production activities> | Based on the responsibility definitions filter, the appropriate JIT call component groups are displayed that could be released to production. |  |
| 4 | Release to Production | Choose component group and choose the function Release Summarized JIT to Production. | Accordingly the JIT call status is updated to Released for Production. |  |
| 5 | View Logs | Choose Application Log button to view successes, errors, or warnings that occurred during release to production. | The standard application log screen is displayed with details. |  |

#### Schedule Packing Group Creation / Update

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule a background job to create packing groups for sequenced JIT calls based on the package specification defined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Packing Group Creation/Update (F4960) app. |  |  |
| 3 | Create a new job | Choose Create to create a new job. | Template section is displayed with appropriate job template by default. |  |
| 4 | Maintain Information and Schedule Job | Choose Step 2.Scheduling OptionsChoose Start Immediately or define the recurring pattern and maintain the scheduling information.Choose Step 3.ParametersShip-To Party: 33154802Component Group Material: FG032 | Packing groups would be created for materials FG032. | For reorder JIT calls, a separate packing group is created, based on the package specification. |

#### Release Sequenced JIT Call Component Groups to Production

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release a sequenced JIT call to production.

Prerequisites

You have created packing groups based on the packing group specification defined. Proceed as described in Schedule Packing Group Creation / Update chapter.

Procedure

|  |
| --- |
| Note If you are using a standard business user as Team Member to perform business operations, you must assign the appropriate business roles authorized to perform the business operations to the respective business user. For example, add Material Planner Just-In-Time Supply (MATL_PLNR_JIT_S_TO_C) to Production Planner - Lean Manufacturing (PRODN_PLNR_LEAN_MFG). |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Planner - Lean Manufacturing . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) |  |  |
| 3 | Filter JIT Calls to be Released for Production | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for production activities for Sequenced JIT Call (Supply with Production)> | Based on the responsibility definitions filter, appropriate JIT call component groups are displayed that could be released to production. |  |
| 4 | Release to Production | Choose component group(s) and choose the function Release Sequenced JIT Call to Production. | Accordingly the JIT call component group status is updated to Released for Production. |  |
| 5 | View Logs | Choose Application Log in the confirmation dialog box to view any errors or warnings that occurred during release to production. | The standard application log screen is displayed with details. |  |

#### Check Planning in Planning Table (Optional)

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
| 3 | Enter Details | On the Planning Table Initial Screen: Change Mode screen, make the following entries and execute:Plant: 3310Under Selection by production version section,choose radio button Material and then enter material number：Material:FG031 or FG032 | The Planning Table for Repetitive Manufacturing: Change Mode screen displays. |  |
| 4 | Check the Quantity | In the Material Data section, check the requirement quantities in the row 0001 FABRIC.If changes made, click Save. | The MRP run updated the requirements quantities.In the Total Capacity Data section, you can monitor capacity load utilization of the production lines. |  |

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
| 3 | Select Material | Choose Adapt Filters to add the Material filter if not added, enter the following value:Material: SG031Select the material and choose Manage Material. | The Manage Material Coverage screen displays. |  |
| 4 | Rescheduling Check (Optional) | In the Stock/Requirements List, the Rescheduling column displays the rescheduling status of the following MRP Elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersYou can choose below icons in the Rescheduling column to perform corresponding actions.Reschedule in (Bring operation forward if the receipt element lies after the requirement date)Reschedule out (Postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment | Corresponding actions perform. |  |
| 5 | Review the Status and Coverage Days | Make following entries and choose Refresh:Shortage Definition: Stock Day's Supply |  |  |
| 6 | Repeat for other material | Repeat the steps 2 to 5 for the SG032 and SG033 material. |  |  |
| 7 | Return to Home | Choose the Home icon. |  |  |

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
| 3 | Enter Details | Make the following entries and choose Execute.Staging Types: SLoc.Level (Activate checkbox)Plant: 3310Selection Horizon for Remts: <A date>Note Requirements falling on a later date will not be taken into account in the pull list.Planned Orders: <Planned Order Number> Access Manage Material Coverage - New Version (F0251A) app as a Production Planner to view the planned order generated for the material used in sales scheduling agreement, example FG031.Bulk Material: <Adapt Indicator if necessary> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Proposals | Select the required line items from the left-hand margin and choose Replenishment Proposals from the Top of the screen. |  |  |
| 5 | Choose Replenishment Elements | Review the staged quantity and choose Replenishment Elements. |  |  |
| 6 | Enter Replenishment Storage Location | On the bottom half of the split screen, select the lines and enter the replenishment storage location 331C for the material, for Example SG031 ,SG032and SG033 |  |  |
| 7 | Choose Print | If you want to print the Pull List, you can execute following printing steps, else please go directly to step 13.Choose Go to Menu ->Pull List -> Print at the upper right of the screen. |  |  |
| 8 | Print List Selection | In the popup window Print List Selection, choose following entries and choose Continue :Print List Selection: Replenishment Proposals | The print list will be displayed. |  |
| 9 | Check Print List | Check the print list, and choose Print at the upper right of the screen. |  |  |
| 10 | Select Output Parameters | In the popup window Print ALV List, choose following entries and choose Continue.Output Device: expand Name of Device list in the system, choose a known device.Print Time: Immediately | Message “Spool request (number XXXX) sent to SAP printer XXXX” indicates successful printing. |  |
| 12 | Go Back | Go back to the stage screen before Printing. |  |  |
| 13 | Select Stage | Select the replenishment element in the bottom half of the screen, and choose Stage at the middle of the screen. |  |  |
| 14 | Save | Choose Save (Ctrl+S). |  |  |

#### Production Confirmation

##### Confirm Repetitive Manufacturing Inclusive Backflush of Materials for (non-JIT)

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
| 3 | Enter Selection Data | Make the following entries:Assembly backflush: XMake-to-Stock: system proposesPlanned Order: Planned Order Number (from previous step for FG031)Note When the system proposes quantities, change as required.Press Enter. | Note down the Posting Date and Document Date on the screen. |  |
| 4 | Post with Corrections | Choose Post with Correction.Select the production version, if prompted. |  |  |
| 5 | Post | Choose Post. |  |  |

|  |
| --- |
| Note The app Confirm Repetitive Manufacturing (MFBF) can be used to perform Reporting Point (RP) confirmation and backflush.Process step:Reporting point confirmation related steps can be performed by logging in as the Production Operator - Repetitive Manufacturing role.To perform reporting point confirmation in the app, enable the indicator for RP Backflush and provide the operation number of the reporting point in the field Reporting Point.Purpose of RP confirmation:Reporting Points are operations in the routing where milestone confirmation is enabled using the appropriate control key.Reporting Point (RP) confirmation allows users to:Record and calculate the work in process quantitiesRecord component consumption at a specific operation (reporting point)Record scrap quantities at a specific operation (reporting point)Prerequisites for RP confirmation:Enable RP backflush indicator during configuration of the appropriate REM profile and assign the REM profile to the material master. The REM profile can be adjusted to make RP backflush optional or mandatory.In routing, use control keys that have milestone confirmation enabled and assign the routing to appropriate production version.A standard cost estimate or cost estimate based on production version is completed for the material.Additional processes related to reporting point confirmation available for this role are:Use the app Display Reporting Point Quantity (MF26) to provide an overview of confirmation quantities at reporting points.Use the app Reset Reporting Point Confirmations (MF4R) to reverse the confirmation and backflush done at a reporting point. |

Result

Finished Goods material is received into stock and Semi finished materials are issued from stock. To view the Material document, log on the SAP Fiori Launchpad as the Warehouse Clerk, then open Material Documents Overview.

##### Post Processing of Error Records for non-JIT production

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

##### Confirm Production of JIT Calls (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

|  |
| --- |
| Note If you are using a standard business user as Team Member to perform business operations, you must assign the appropriate business roles authorized to perform the business operations to the respective business user. For example, add Material Planner Just-In-Time Supply (MATL_PLNR_JIT_S_TO_C) to Production Operator - Lean Manufacturing (PRODN_OPTR_LEAN_MFG). |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) . |  |  |
| 3 | Filter JIT Calls to Confirm Production | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for production activities for Summarized or Sequenced JIT Calls> | Based on the responsibility definitions filter, appropriate JIT call component groups are displayed that could be confirmed for production. |  |
| 4 | Confirm Production | Choose component group(s) and choose the function Confirm Production. | Accordingly the JIT call component group status is updated to Production Confirmed and the component groups disappear from the list based on the internal processing status. |  |
| 5 | View Logs | Choose Application Log in the confirmation dialog box to view any errors or warnings that occurred during production confirmation. | The standard application log screen is displayed with details. |  |

##### Reprocessing of Failed Stock Posting After Confirmation of Production (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If goods movement fails for components in the previous step, the failed entries appear in the app and goods movement can be re-triggered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Supervisor - Lean Manufacturing | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Reprocessing List - For Customer JIT Calls (F5092) . | List of component materials for which goods movement have failed gets displayed. |  |
| 3 | Filter JIT Call to be Edited | Make the following entry in filters and choose Ship-To Party ID/Description:<Ship-To-Party from Sales,Scheduling Agreements> example, 33154802 | Ship-to party is displayed with additional information. |  |
| 4 | Reprocess Goods Movement | Choose a material and execute reprocessing. | After resolving the issue based on message short text column, goods movement can be re-triggered. |  |

#### Manage JIT Packing Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note Optionally, this could also be achieved with Manage Customer JIT Calls - By Component Groups (F6077) or Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) applications if the team is created with the appropriate responsibility definitions, users and function assignments. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with the same user assigned to the team for production operations, with the role Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) | List of teams to which the user is assigned is displayed with the appropriate function that could be performed with selection of the team. |  |
| 3 | Choose an appropriate team for further processing | Select the appropriate team created with function Release to Packing. |  |  |
| 4 | Process Packing Group to be Released for Packing | Enter the alternative packing group ID that shall be released for packing. | The status of component group is set to Released for Packing. | 4 |
| 5 | Navigate Back to List of Teams | Click the Back button to navigate back to the list page with teams and functions. | List page is displayed with appropriate functions for release to packing and confirmation of packing. | 5 |
| 6 | Choose an appropriate team for further processing | Select the appropriate team with function Confirm Packing. |  | 6 |
| 7 | Process Component Group(s) to be Confirmed for Packing | Enter the external JIT call number of the component group that shall be confirmed for packing. | The internal processing status of scanned component group is set to Packing Confirmed. | 7 |
| 8 | Process all component groups belonging to the packing group for packing confirmation | Repeat previous step for all component groups/external JIT call numbers that need to be confirmed for packing/ belonging to the same packing group. | The internal processing status of all component groups is set to Packing Confirmed. | 8 |

#### Stock availability analysis for JIT Calls

Purpose

In this step, you can view a mapping of components requested in JIT calls to the available stock. In other words, you can analyze which JIT calls from customers can or cannot be fulfilled by the available stock of components.

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
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock Availability Analysis (F3923) app. |  |  |
| 3 | Select Criteria | Make the following entry in filters and choose GO:Component Group: <Component Groups from JIT Call>, example FG031 or FG032Plant: 3310 |  |  |
| 4 | Check Results | Stock Coverage for each Component Group is displayed.Click on entry to see details | Stock Coverage is displayed |  |

#### Evaluating Stock/Requirements Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for finished materials.

Prerequisite

Goods Receipt posting is carried out for production orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage screen displays. |  |
| 3 | Select Criteria | In the Search bar, enter material from sales scheduling agreement , for example,FG031 and choose GO. | Stock Availability situation for all materials displays. |  |
| 4 | Selection of Materials | Use the Check box and select the rows which have FG031 as the Material No and click Manage Materials on the screen | The Material and Material Details screens display.Stock/Requirement list for all the selected materials is displayed.Rows with SchLne items are displayed for the finished product. |  |
| 5 | Display Stock situation | The Screen Stock/Requirements list should show the updated stock quantity.Stock information appears as first row in the table present in this screen. Stock quantity is displayed under the Quantity and Available columns. | Updated Stock Quantity is displayed. Stock quantity is increased by the amount of quantity posted as goods receipt for Production Order. |  |

### Outbound Delivery to Customer

Purpose

This process step shows you how to create an outbound delivery manually. It is also possible to schedule background jobs for outbound delivery creation.

The following apps are available for job scheduling of delivery creation:

- Schedule Delivery Creation (F2228)
- Create Outbound Deliveries ( in Background) from Summarized JIT call (F4963)
- Create Outbound Deliveries ( in Background) from Sequenced JIT call (F4962)

#### Scheduling Agreement Non-JIT

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to log on to the SAP S/4HANA system to create an outbound delivery for the previously received delivery schedule (scheduling agreement).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open My Sales Order Schedule Lines - Due for Delivery (VL10E). | The Sales Order Schedule Lines screen displays. |  |
| 3 | Search Scheduling Agreement | On the Sales Order Schedule Lines screen, make the following entries and choose Continue:Shipping Point/Receiving Pt: 3310Deliv. Creation Date: <Shipping date>CalcRuleDefltDlvCrDt: <Blank>On the Sales Orders tab:SD Document: <Scheduling Agreement number created previously>Choose Execute. |  |  |
| 4 | Create Delivery | On the Activities Due for Shipping “Sales Order Schedule Lines” screen, choose Sales Sched. Agr. No. created in previous step, and choose Dialog. |  |  |
| 5 | Save Delivery | Choose Save, make a note of the delivery number. | Creation of a delivery is triggered. |  |

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries, if the items is not relevant for picking please exclude this step execution : Example Consignment

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Outbound Deliveries for Picking (VL06P) . |  |  |
| 3 | Enter Shipping Point | Make the following entries, and choose Execute.Shipping Point/Receiving Pt: 3310Select Only Picking Without WM optionPicking Date: <Picking date from delivery > |  |  |
| 4 | Choose Delivery | On the Day’s Workload for Picking screen, choose the Delivery document created in previous step, and choose Change Outbound Deliveries. |  |  |
| 5 | Enter Picked Quantity | On the Delivery XXXXXXX Change: Overview screen, go to the Picking tab and enter quantity equal to delivery Qty in Picked Qty field for picking related item(s). |  |  |
| 6 | Choose Enter | Choose Enter. |  |  |
| 7 | Save | Choose Save. | The delivery is picked now. |  |

##### Execute Automatic Packing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute automatic packing for delivery items right in an outbound delivery.

Automatic packing allows you to use packing instructions to create handling units automatically in outbound deliveries. The system automatically determines the packing instructions for the materials to be packed and then the material is packed according to the packing instructions that were found.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter the Outbound Delivery Number | On the Change Outbound Delivery screen, enter the outbound delivery number created above and choose Continue. |  |  |
| 4 | Choose Packing | In the header section, choose Pack. |  |  |
| 5 | Choose Automatic Packing | On the Processing of Handling Units for Outbound Delivery screen, choose Automatic Packing. | Handling units were created automatically based on the packing instruction that was determined according to the Packing Instruction Determination you maintained in the preliminary steps. |  |
| 6 | Maintain Serial Numbers (Optional) | On the Total Content tab, choose the material being packed, and then choose Serial Nos..Enter the serial numbers on the Maintain Serial Numbers screen.In addition, the Create serial number automatically field can be set if the required serial numbers are created by the system automatically.Note This step only applies to the materials that use serial number management. |  |  |
| 7 | Check General Overview | Choose General Overview in the header section to have a visualized hierarchy of all handling units. |  |  |
| 8 | Check the Handling Units | On the General Overview screen, choose (+) of each Handling Unit to expand the line items.Check the material and quantity packed in each Handling Unit which were created according to the packing instruction in the section Create Packing Instruction. |  |  |
| 9 | Save Your Outbound Delivery | Choose Save to save packing results and your outbound delivery. | The packing results together with the outbound delivery are saved. |  |

#### Summarized JIT Calls

##### Create Outbound Delivery from Summarized JIT Calls

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
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Summarized JIT Calls (F3922). |  |  |
| 3 | Filter JIT Call to be Edited | Make the following entry in filters and choose Go:Ship-to Party: 33154801 | Ship-to party 33154801 is displayed with additional information. |  |
| 4 | Create Outbound Delivery | Choose Component Group FG031 and choose Create Outbound DeliveryNote Ensure that both the overdelivery and underdelivery tolerance values set in customer supply controls are less than 100%. | Accordingly the JIT call status is updated to Delivery Created. | Note Outbound delivery is created based on the selected split criteria; refer to section Create Just-In-Time Customer Master Data. |
| 5 | View Logs | Choose View Logs to view any errors/warnings that occured during delivery creation | The delivery view logs application screen is displayed with details. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the Shipping Specialist role. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_PICK_LIST and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries, if the items is not relevant for picking please exclude this step execution : Example Consignment

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Outbound Deliveries for Picking (VL06P) . |  |  |
| 3 | Enter Shipping Point | Make the following entries, and choose Execute.Shipping Point/Receiving Pt: 3310Select Only Picking Without WM optionPicking Date: <Picking date from delivery > |  |  |
| 4 | Choose Delivery | On the Day’s Workload for Picking screen, choose the Delivery document created in previous step, and choose Change Outbound Deliveries. |  |  |
| 5 | Enter Picked Quantity | On the Delivery XXXXXXX Change: Overview screen, go to the Picking tab and enter quantity equal to delivery Qty in Picked Qty field for picking related item(s). |  |  |
| 6 | Choose Enter | Choose Enter. |  |  |
| 7 | Save | Choose Save. | The delivery is picked now. |  |

##### Execute Automatic Packing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute automatic packing for delivery items right in an outbound delivery.

Automatic packing allows you to use packing instructions to create handling units automatically in outbound deliveries. The system automatically determines the packing instructions for the materials to be packed and then the material is packed according to the packing instructions that were found.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter the Outbound Delivery Number | On the Change Outbound Delivery screen, enter the outbound delivery number created above and choose Continue. |  |  |
| 4 | Choose Packing | In the header section, choose Pack. |  |  |
| 5 | Choose Automatic Packing | On the Processing of Handling Units for Outbound Delivery screen, choose Automatic Packing. | Handling units were created automatically based on the packing instruction that was determined according to the Packing Instruction Determination you maintained in the preliminary steps. |  |
| 6 | Maintain Serial Numbers (Optional) | On the Total Content tab, choose the material being packed, and then choose Serial Nos..Enter the serial numbers on the Maintain Serial Numbers screen.In addition, the Create serial number automatically field can be set if the required serial numbers are created by the system automatically.Note This step only applies to the materials that use serial number management. |  |  |
| 7 | Check General Overview | Choose General Overview in the header section to have a visualized hierarchy of all handling units. |  |  |
| 8 | Check the Handling Units | On the General Overview screen, choose (+) of each Handling Unit to expand the line items.Check the material and quantity packed in each Handling Unit which were created according to the packing instruction in the section Create Packing Instruction. |  |  |
| 9 | Save Your Outbound Delivery | Choose Save to save packing results and your outbound delivery. | The packing results together with the outbound delivery are saved. |  |

#### Sequenced JIT Call

##### Create Handling Units from Packing Groups for Sequenced JIT Calls

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, handling units are created from packing groups; the information is cascaded to the delivery document.

|  |
| --- |
| Note Optionally, this could also be achieved with Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) applications if the team is created with the appropriate responsibility definitions and function assignments. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer JIT Calls - By Component Groups (F6077) app. |  |  |
| 3 | Filter JIT Calls to Create Handling Unit | Make the following entry in filters and choose Enter:Team ID: <Team ID that was created earlier for creating Handling Unit for Sequenced JIT Call> | Based on the responsibility definitions filter, appropriate JIT call component groups are displayed that could be confirmed for production. |  |
| 4 | Create Handling Unit | Choose component group(s) and choose the function Create Handling Unit from Package Group. | Accordingly the JIT call component group status is updated to HU Created. |  |
| 5 | View Logs | Choose Application Log in the confirmation dialog box to view any errors or warnings that occurred during production confirmation. | The standard application log screen is displayed with details. |  |

##### Create Outbound Delivery from Sequenced JIT Calls

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the delivery.

|  |
| --- |
| Note Optionally, this could also be achieved with Manage Customer JIT Calls - By Component Groups (F6077) or Manage JIT Packing Groups - For Sequenced JIT Calls (F5457) applications if the team is created with the appropriate responsibility definitions and function assignments. |

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist - Just-In-Time Supply. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries from Sequenced JIT Calls (F3897) app. |  |  |
| 3 | Filter JIT Call to be Edited | Make the following entry in filters and choose Go:Ship-To Party ID/Description: 33154802 | Ship-to party33154802 is displayed with additional information. |  |
| 4 | View Contents | Choose packing group and select Chevron. | The package contents are displayed. | [Optional: Only if delivery sequence group is created] Packing group is displayed based on ascending Alternative Handling Unit ID generated, which is based on JIT delivery sequence group created in an earlier step. |
| 5 | Create Outbound Delivery | Choose Create Outbound Delivery | Accordingly the JIT call status is updated to Delivery Created. |  |
| 6 | View Logs | Choose View Logs to view any errors/warnings that occurred during delivery creation | The delivery view logs application screen is displayed with details. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On to SAP Fiori Launchpad | Log on to the SAP Fiori Launchpad using the role Shipping Specialist. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) app. | The Change Outbound Delivery screen is displayed |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type DELIVERY_PICK_LIST and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Schedule Goods Movement from Production for Customer JIT Calls (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Based on settings in the supply control, goods movement can be scheduled using a background job.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Production Operator - Lean Manufacturing | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule goods movement from production for customer JIT calls (F5168). |  |  |
| 3 | Create a New Job | Choose Create to create a new job. | The Scheduling Information screen is displayed. |  |
| 4 | Maintain Schedule Information | Make the following entries and choose Schedule:Step 1: Job NameStep 2: Start ImmediatelyStep 3: Component Group Material: component group material from JIT call, example FG032 | Goods movement gets scheduled. |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery in the SAP S/4HANA system (supplier side).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Outbound Deliveries for Goods Issue (VL06G). |  |  |
| 3 | Open Outbound Delivery Monitor | On the Outbound Deliveries for Goods Issue screen, make the following entries and choose Execute.Shipping Point/Receiving Pt: 3310Pland Gds Mvmnt Date: Pl. Gds Mvmt date from delivery |  |  |
| 4 | Choose Outbound Delivery | On the Goods issue for Outbound Deliveries to be Posted screen, choose the outbound delivery document created in previous step, and choose Change Outbound Deliveries. |  |  |
| 5 | Post Good Issue | On the Delivery XXXXXXXX Change: Overview screen, choose Post Goods Issue. | The goods issue is posted. |  |

Financial Posting(only relevant for non-consignment scenarios)

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Good (FERT) | 54083000Inv Chg COGS w/CE | 13400000Inventory FinishedGd | none |

### Consignment Issue

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are now in the customer's consignment stock. The stock overview reflects this transfer of products. This process step shows you how to check the stock overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: Enter material numbers used in the scheduling agreement consignment fill-up.Customer: Enter the customer used in scheduling agreement.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock.You may need to adapt the following filters:Special Stock TypeCustomer: You may need to adapt column settings. For example, Customer. |  |

#### Create Consignment Issue Order with Reference to Scheduling Agreement Manually (non-JIT)

Note: This chapter is only used for internal testing purpose, normally the Consignment Issue Order is automatically generated via inbound delivery note from external agent or customer.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You create a delivery by external agent , document type ED , on the basis of the external agent delivery note. You do this in the same way as creating a [sales order](https://help.sap.com/viewer/7027faa96fc547d4a83845fe8bbfd6a8/6.00.31/en-US/f564b65334e6b54ce10000000a174cb4.html) with reference to the scheduling agreement (Doc Type - LK).

Or at regular intervals, the customer reports either how many products have been sold, or consumed, or how many products are in the current stock (inventory).A corresponding order is entered, documenting the issue from the consignment stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). |  |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create and then choose Create Sales Order - VA01. |  |  |
| 4 | Enter Order Type | On the Create Sales Documents screen, make the following entries and choose Create with Reference:Order Type: EDSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Refered Scheduling Agreement | On the Create with Reference dialog box, make the following entry and choose Copy:SchedAgree: <the sales scheduling agreement number created previously with Doc Type : LK> |  |  |
| 6 | Enter Material Data | On the Create CsgmtIssueSchedAgr : Overview screen, make the following entries:Sold-to Party: 33100020Ship-to Party: 33100020Cust. Reference: <the customer purchase order number>On the Items tab, make the following entries:Material: FG031Order Quantity: <the required quantity>, for example, 2 PC |  |  |
| 7 | Save Document | Choose Save.CsgmtIssueSchedAgr xxxxx has been saved (delivery xxxxxxxxx created).Make a note of the delivery number__________. | The consignment issue order is created. |  |

#### Create JIT Delivery Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process shows you how to format and simulate sending the transmission for testing.

Prerequisite

Before proceeding with testing this step, you need to have completed the additional and mandatory configuration steps that are described in the setup instructions for scope item [53X](https://me.sap.com/processnavigator/SolS/SolS-013/2608/SolP/53X) in the SAP Signavio Process Navigator. These configuration steps are specific for your implementation. These include mandatory settings that are not delivered by SAP and must be created by you.

Procedure

The consignment issue process is triggered by receiving the transimission of delivery confirmation documents from the customer. SOAP API JIT Delivery Confirmation is provided to send transmissions and published in the SAP API Hub with detail introduction and implementation information. You can use general SOAP API testing tool like Postman, SoapUI etc to call the API and send test transmission.

| Token | Buyer Product ID | Supplier Product ID | Quantity Code | Quantity Unit | Buyer JIT Call ID |
| --- | --- | --- | --- | --- | --- |
| <Unique Delivery Confirmation Number> | <Customer Material number from scheduling agreement> | <material number from scheduling agreement> | ST | <exact match or difference to JIT Call> | <JIT Call Number> |

|  |
| --- |
| Note The example transmission is provided in Transmission Example – JIT Delivery Creation with all mandatory fields maintained based on scenario listed above.To receive transmission for testing, take Postman to call the API as the example, detail steps are listed in Send Transmission with Postman .Sold-to party determination needs to be maintained for scope item 53X at SAP S/4HANA Cloud Public Edition system by using Fiori App Assign Sold-to Parties. Please refer to set-up instruction for scope item 53X in Convert External to Internal Partner Num-ber. Entry details are as below:Customer Number: 33154802Partner Function: SHExternal Partner Number:P001Internal Partner Number |

#### Release Delivery Confirmation for Sequenced JIT

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Manage JIT Delivery Confirmation app is primarily for Material Planner - Just-In-Time Supply to monitor and manage incoming JIT delivery confirmations. The material planner can launch the app and check the matching and release status. If a JIT delivery confirmation is matched or over-confirmed, it gets released automatically; subsequent documents and actions get triggered, for example, customer consignment issue order, delivery based on customer consignment issue order, and post goods issue.

If the JIT delivery confirmation is not matched, the material planners can monitor the details on the object screen of the JIT delivery confirmation. They can also refer to reference JIT calls along with process flows and related JIT delivery confirmation by navigating to delivery confirmation items.

Prerequisites

Ensure that confirmation is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Material Planner - Just-In-Time Supply. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage JIT Delivery Confirmations (F5268). |  |  |
| 3 | View Delivery Confirmation Items | Choose the chevron icon of a JIT delivery confirmation to navigate to the object page. | The JIT delivery confirmation item details are displayed. Matching status and release status for each item can be viewed. |  |
| 4 | Manually Release Partially Confirmed JIT Delivery Confirmations | Choose one or multiple delivery confirmation items and choose Release button. Select a reason code from the menu options and choose OK. | The processing status of the chosen delivery confirmation items changes to Released/ Consignment Issue Order Created.If all items of a delivery confirmation are released, the release status of the delivery confirmations changes to Released. If a few items of the selected delivery confirmations are released, the release status of the delivery confirmations changes to Partially Released.The process flow in the third section of FCL (Go to delivery confirmation and choose Delivery Confirmation Items) gets updated with subsequent documents such as customer consignment issue order and delivery based on customer consignment issue order. | Delivery confirmations that are matched or over-confirmed are automatically released. |

#### Create Delivery (Automatically)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you save the delivery by external agent document, the system automatically creates an immediate delivery.

Procedure

This step is automatically generated.

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods issue for this delivery to reduce the consignment stock on record and increase the cumulative quantity issued by the external agent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries - VL06O screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute:Shipping Point/Receiving Pt: 331C |  |  |
| 4 | Post Goods Issue | Select the relevant delivery and choose Post Goods Issue. In the dialog box, choose today’s date and choose Continue. | The goods issue is posted. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Goods (FERT) | 54083000Inv Chg COGS w/CE | 13400000Inventory FinishedGd | none |

#### Check Stock Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The goods are transferred from the customer's consignment stock and are no longer owned by the company. The stock overview reflects this transfer of products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Multiple Materials (F1595). | The Stock - Multiple Materials screen displays. |  |
| 3 | Enter Plant, Material Data, and Customer | On the Stock - Multiple Materials screen, make the following entries:Plant: 3310Material Number: Enter material numbers used in the scheduling agreement consignment fill-up.Customer: Enter the customer used in scheduling agreement.Special Stock Type: WChoose Go. | The customer consignment stock is displayed. The delivered quantity is posted into the consignment stock.You may need to adapt the following filters:Special Stock TypeCustomer: You may need to adapt column settings, for example, Customer. |  |

### Billing

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create invoices in SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798) | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings in the upper bar, you can make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Choose Individual Billing Document | Select row of delivery document created previously and choose Create Billing Documents. | The Create Billing Document screen displays |  |
| 5 | Maintain Billing Data | Choose billing type F2 Invoice and maintain billing date, for example current date, then choose OK and Save. | New billing document is created. |  |
| 6 | Display Billing Document | The billing document appears automatically. | The system generates an invoice for billing. |  |

|  |
| --- |
| Note Optionally based on customer business requirement you would be able to use scope item 4H2 for self-billing. Incase you have price / quantity differences, subsequent debit / credit can be created and posted.Please also validate availability of scope item 4H2 to your specific country localization. |

Financial Postings

Example

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finsihed Goods (FERT) | 33100020Customer: 33100020 | 41000000Rev Domestic Prod22001000Sales Tax Accrued21730000 (optional)Freight Clrg MM | None |

#### Job Scheduling for Billing Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creation billing documents.

This app can be used as an alternative instead of the manual creation of billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation (F1519). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Creation. |  |
| 4 | Job Parameters | Make the following entries:For Step 1, in the Template Selection section, from the drop-down box of Job Template, choose Schedule Billing Creation. Maintain a job name.Then choose Step 2, in the Scheduling Options section, make sure that Start Immediately checkbox is checked. Or you can also set the start date and start time.Then choose Step 3. In the Parameters section, make the following entries:Billing Date From: <today – 1 day>To: <today + 1 day>Sales Organization: 3310SD Document: <sales scheduling agreement created above>Sold-to-Party: <Customer from sales scheduling agreement> example 33100020Documents to Be Selected: Delivery-RelatedChoose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, and the job list will refresh. | The log details display. |  |

### Accounts Receivable

#### Post Incoming Payments

Purpose

In this activity, you post the incoming payments from the customer.

Prerequisites

Invoices are posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Incoming Payments (F1345).Note For some countries, if withholding tax is to be posted during payment, use the Post Incoming Payments for Japan - For Customers (FBZ1) app. | The Post Incoming Payments view displays. |  |
| 3 | Enter General Information | Make the following entries in the General Information area:Company Code : 3310Posting date : today’s dateJournal Entry date : today’s dateValue date : today’s dateJournal Entry Type : DZ (Customer Payment) |  |  |
| 4 | Enter Bank Data | Make the following entries in the Bank data area.G/L Account: 11001060House Bank/Account ID : AEBK1/AEAC1 or AEBK2/AEAC2Amount : customer invoice amountNote If the incoming payment is part of a down payment, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Currency : AED |  |  |
| 5 | Enter Open Items | Make the following entries:Customer Account : <Customer from sales scheduling agreement> example 33100020Choose the Propose Items button. | The open items are displayed in the bottom half of the view. |  |
| 6 | Clear Items | Choose Items to Clear by choosing the Clear button in last item column. | The selected item is transferred to view Items to be Cleared. |  |
| 7 | Post Entries | Choose Post. | The Activated dialog box displays details of document number generated. |  |

### Accounts Payable

#### Post Outgoing Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can post outgoing payments either manually or automatically. The manual posting process is described in the following example. The manual outgoing payment generated in this step doesn't go through an approval process and doesn't create a payment medium.

Prerequisites

Review the house bank assignment to G/L account before you start the test so that you can use the proper G/L account in step 3 General Information in the Procedure section below.

To review, select the house bank and company code to test and use the Manage Bank Accounts (F1366A) app. In the app, go to House Bank Account Connectivity > House Bank Account Data > G/L Account Data .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Outgoing Payments (F1612). | The Post Outgoing Payments (F1612) view displays. |  |
| 3 | General Information | Make the following entries:General Information sectionCompany Code: 3310Posting Date: <Today's date>Journal Entry Date: <Today's date>Value Date: <Today's date>Reference (optional): <reference>Journal Entry Type: KZHeader Text: <header text>Bank Data sectionHouse Bank / Account: AEBK1/AEAC1 or AEBK2/AEAC2G/L Account: 11001000 (see Prerequisites above)Amount / Currency: <amount to pay on existing invoice>, for example, 119,00AEDFees: OptionalAssignment: OptionalExchange Rate: OptionalAmount / CCode Currency: Optional | A list of open items is displayed in the Open Items \| Standard section. |  |
| 4 | Open Item Selection | In the Open Item Selection section, make the following entries:Supplier Account: 33300003and choose the Show Items button.This is used for doing the payment for material SG031and SG033. |  |  |
| 5 | Select/Deselect | Select an item to pay, and in the Clear column, choose Clear. | The item to pay transfers to the Items to be Cleared / Standard section. |  |
| 6 | Post | Choose Post.Note The generated payment doesn't require approval. | The system displays Journal entry xxxxxxxxxx was successfully posted in company code 3310 notification. |  |
| 7 | Display | To view the posted document, choose Display. | The posted document is displayed. |  |
| 8 | Back | Choose the Back button. | The system displays Journal entry has already been posted. You can now post a new payment notification. |  |
| 9 | Dismiss notification | Choose OK to dismiss the notification. |  |  |
| 10 | Repeat | Repeat steps 3 to 9 for material SG032 with the following data:Supplier Account: 33300063 |  |  |

## Appendix

### Scheduling Job (Alternative)

#### Job Scheduling for Delivery Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for creating outbound deliveries.

This app can be used as an alternative instead of the manual creation of outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose New to define a new job. | The New Job screen is displayed. Job Template should default as Schedule Delivery Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message: Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | Screen goes to job log details. |  |

#### Job Scheduling for Goods Issue Deliveries (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for goods issue posting with reference to outbound deliveries.

This app can be used as an alternative instead of the manual goods issue posting for outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job screen displays. The Job Template should be defaulted as Schedule goods issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message: Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details display. |  |

#### Job Scheduling for Billing Release (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for release billing documents to accounting.

This app can be used as an alternative instead of the manual release to accounting for billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Release (F1518). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. The Job Template should be defaulted as Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message: Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Release Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, and the job list will refresh. | The log details display. |  |

#### Job Scheduling for Billing Output (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output (F1510). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. The Job Template should be defaulted as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message: Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Output Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details display. |  |

### Transmission Example – JIT Delivery Creation

The example transmission filling with the data for designed scenario is as below:

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:njit="http://sap.com/xi/NJIT">

<soapenv:Header/>

<soapenv:Body>

<njit:JITDeliveryConfirmation>

<MessageHeader>

<ID schemeID="Token 1" schemeAgencyID="Token 2" schemeAgencySchemeAgencyID="Tok">Token 4</ID>

<UUID schemeID="Token 5" schemeAgencyID="Token 6">12345678-90AB-CDEF-0123-456789ABCDEF</UUID>

<ReferenceID schemeID="Token 7" schemeAgencyID="Token 8" schemeAgencySchemeAgencyID="Tok">Token 10</ReferenceID>

<ReferenceUUID schemeID="Token 11" schemeAgencyID="Tok">12345678-90AB-CDEF-0123-456789ABCDEF</ReferenceUUID>

<CreationDateTime>2021-04-15T12:00:00.1234567Z</CreationDateTime>

<TestDataIndicator>true</TestDataIndicator>

<ReconciliationIndicator>true</ReconciliationIndicator>

<SenderBusinessSystemID>NJIT_API</SenderBusinessSystemID>

<RecipientBusinessSystemID>XXX</RecipientBusinessSystemID>

</MessageHeader>

<DeliveryConfirmationHeader>

<DeliveryConfirmationNumber schemeID="Token 80" schemeVersionID="Token 81" schemeAgencyID="Token 82" schemeAgencySchemeID="Token 83" schemeAgencySchemeAgencyID="Tok">XXXXXX</DeliveryConfirmationNumber>

<ConfirmationDate>year-month-day</ConfirmationDate>

<InvoiceDocumentNumber schemeID="Token 86" schemeVersionID="Token 87" schemeAgencyID="Token 88" schemeAgencySchemeID="Token 89" schemeAgencySchemeAgencyID="Tok"></InvoiceDocumentNumber>

<InvoiceDocumentDate></InvoiceDocumentDate>

<ReorderIndicator></ReorderIndicator>

<Party>

<PartyType>VN</PartyType>

<GlobalLocationNumber></GlobalLocationNumber>

<BuyerPartyID>33154802/BuyerPartyID>

<SupplierPartyID></SupplierPartyID>

</Party>

<Party>

<PartyType>SH</PartyType>

<GlobalLocationNumber></GlobalLocationNumber>

<BuyerPartyID>P001</BuyerPartyID>

<SupplierPartyID></SupplierPartyID>

</Party>

<DeliveryConfirmationItem>

<ComponentMaterial>

<GlobalTradeItemNumber></GlobalTradeItemNumber>

<BuyerProductID>RSD129_SEQ_CNJIT</BuyerProductID>

<SupplierProductID>FG032</SupplierProductID>

</ComponentMaterial>

<Quantity unitCode="ST">1</Quantity>

<BuyerCallItemID schemeID="Token 12" schemeVersionID="Token 13" schemeAgencyID="Token 14" schemeAgencySchemeID="Token 15" schemeAgencySchemeAgencyID="Tok">10</BuyerCallItemID>

<ReferenceJITCall>

<BuyerJITCallID>XXXXXXXXXX</BuyerJITCallID>

</ReferenceJITCall>

</DeliveryConfirmationItem>

</DeliveryConfirmationHeader>

</njit:JITDeliveryConfirmation>

</soapenv:Body>

</soapenv:Envelope>

### Send Transmission with Postman

Purpose

The process is to simulate sending transmission for testing. Here, use Postman as the example.

Procedure

Table 9:

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Get the test tool Postman | Download Postman via below link: https://www.getpostman.com/downloads/Install the package. |  | Choose suitable version based on your operation system, Windows 32-bit or Windows 64-bit.If you already have Postman installed, please skip this step. |
| 2 | Choose New > Collection at the top left of the screen and make the following entry:Name: <Enter the name for your identification>Choose Create. |  |  |  |
| 3 | Create Request | Find the collection just created on the leftside of the screen. Choose View more actions.Choose Add Request from the drop down list and make the following entry:Request Name: <Enter the name for your identification>Choose Save to <collection name defined in previous step>. |  |  |
| 4 | Maintain Request | Choose the request just created on the leftside of the screen under the collection and make the following entry for the details display on the right side of the screen.Change the action from GET to POST.Enter request URL: <URL can be found in app Communication Arrangement>Choose Authorization tab, select TYPE: Basic Auth, maintain Username and Password.Choose Headers tab and add one line entry with the following:KEY: Content-TypeVALUE: text/xmlChoose Body tab, select the radio button of Raw.Fill in transmission details, example provided in previous Transmission ExampleChoose Save. |  | <Service URL/Service Interface is the end point URL Please refer to Instruction of Scope item 53X to identify correct Scenario ID, |
| 5 | Send the transmission | Choose Send on the upper right of the screen. |  | Whether the transmission has been successfully received will be displayed at the button after choosing Send. |

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

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-just-in-time-supply-to-customer-with-delivery-confirmation]]
- related-to :: [[08-sales-order-management/test-script-sales-scheduling-agreements-3nr-ae-sap-s-4hana-cloud-publi]]
- related-to :: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-just-in-time-supply-to-cu]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/55F_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 207,983 chars in the whole document
