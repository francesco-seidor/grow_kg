---
id: 12-production-and-manufacturing/test-script-lot-size-of-one-based-on-make-to-order-7dw-ae-sap-s-4hana
title: "Test Script: Lot Size of One based on Make to Order (7DW_AE) - SAP S/4HANA Cloud Public Edition (7DW_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7DW (AE): make-to-order lot size one, from sales order and down payment through production, QM, delivery, billing, payments."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/make-to-order-production]
aliases: [7DW_S4CLD2608_BPD_EN_AE]
keywords: [Make-to-Order Production, make to order, sales orders, milestone billing plan, down payments, mrp run, production orders, batch management, quality inspection, outbound delivery]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DW_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1213
topic: 12-production-and-manufacturing/make-to-order-production
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Lot Size of One based on Make to Order (7DW_AE) - SAP S/4HANA Cloud Public Edition (7DW_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DW_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Make-to-Order Production** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Lot Size of One based on Make to Order (7DW_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232860663)

[2 Prerequisites 5](#_Toc232860664)

[2.1 System Access 5](#_Toc232860665)

[2.2 Roles 5](#_Toc232860666)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232860667)

[2.4 Business Conditions 14](#_Toc232860668)

[2.5 Preliminary Steps 14](#_Toc232860669)

[2.5.1 Create Purchase Info Record 14](#_Toc232860670)

[2.5.2 Edit User-Specific Parameters for Supplier Invoices (Optional) 16](#_Toc232860671)

[2.5.3 Adapt Routing for Finished Goods 17](#_Toc232860672)

[2.5.4 Create Initial Material Stock 19](#_Toc232860673)

[2.5.5 Price Change for Individual Material 20](#_Toc232860674)

[2.5.6 Assign Dependencies 21](#_Toc232860675)

[2.5.7 Assign Materials to Inspection Plan 23](#_Toc232860676)

[2.5.8 Set Delivery Block Automatically in Milestone Billing Plan (Optional) 24](#_Toc232860677)

[2.5.9 Remove Delivery Block Reason Code Automatically in Milestone Billing Plan (Optional) 26](#_Toc232860678)

[3 Overview Table 29](#_Toc232860679)

[4 Test Procedures 33](#_Toc232860680)

[4.1 Customer Sales Order and MRP 33](#_Toc232860681)

[4.1.1 Create Sales Orders with Billing Plan 33](#_Toc232860682)

[4.1.2 Sales Order Pricing (Optional) 36](#_Toc232860683)

[4.1.3 Change Sales Orders (Remove Billing Block) 37](#_Toc232860684)

[4.1.4 Material Requirements Planning at Plant Level 38](#_Toc232860685)

[4.1.5 Evaluating Stock/Requirements Situation 39](#_Toc232860686)

[4.2 Accounts Receivable 42](#_Toc232860687)

[4.2.1 Create Down Payment Request 42](#_Toc232860688)

[4.2.2 Post a Down payment 44](#_Toc232860689)

[4.3 Procurement of Component 46](#_Toc232860690)

[4.3.1 Convert Purchase Requisitions to Purchase Orders 46](#_Toc232860691)

[4.3.2 Preview Purchase Order (Optional) 47](#_Toc232860692)

[4.3.3 Post Goods Receipt 48](#_Toc232860693)

[4.3.4 Maintain Batch Classification 49](#_Toc232860694)

[4.3.5 Check Range of Stock Coverage 50](#_Toc232860695)

[4.4 Production Order Execution for Semifinished Product 52](#_Toc232860696)

[4.4.1 Convert Planned Order to Production Order for Semifinished Product 52](#_Toc232860697)

[4.4.2 Execute Material Staging for Production Order 54](#_Toc232860698)

[4.4.3 Release Production Order 55](#_Toc232860699)

[4.4.4 Pick Components for Assembly 56](#_Toc232860700)

[4.4.5 Final Confirmation of Production Operations 57](#_Toc232860701)

[4.4.6 Event-Based Work in Progress (Optional) 58](#_Toc232860702)

[4.4.7 Post Goods Receipt for Production Order 60](#_Toc232860703)

[4.4.8 Review Production Order (Optional) 61](#_Toc232860704)

[4.5 Production Order Execution for Finished Product 62](#_Toc232860705)

[4.5.1 Convert Planned Order to Production Order for Finished Product 62](#_Toc232860706)

[4.5.2 Material Staging for Production Order 64](#_Toc232860707)

[4.5.3 Release Production Order 65](#_Toc232860708)

[4.5.4 Final Confirmation of Production Operations 66](#_Toc232860709)

[4.5.5 Post Goods Issue for Final Assembly Production Order Components 67](#_Toc232860710)

[4.5.6 Post Goods Receipt for Finished Product Production Order 69](#_Toc232860711)

[4.5.7 Evaluate Stock/Requirement Situation (Optional) 70](#_Toc232860712)

[4.5.8 Batch Information Cockpit - Batch Selection (Optional) 71](#_Toc232860713)

[4.5.9 Batch Information System - Batch Analysis (Optional) 72](#_Toc232860714)

[4.5.10 Event-Based Production Costing - Order Costs (Optional) 74](#_Toc232860715)

[4.5.11 Product Profitability with Production Variances 75](#_Toc232860716)

[4.6 Quality Inspection during Goods Receipt from Production 76](#_Toc232860717)

[4.6.1 Display Material Stock Before Quality Inspection 76](#_Toc232860718)

[4.6.2 Display Open Inspection Lots 77](#_Toc232860719)

[4.6.3 Record Inspection Results 78](#_Toc232860720)

[4.6.4 Make Usage Decision 79](#_Toc232860721)

[4.6.5 Display Material Stock after Usage Decision 80](#_Toc232860722)

[4.7 Outbound Delivery Processing 81](#_Toc232860723)

[4.7.1 Create Delivery 81](#_Toc232860724)

[4.7.2 Execute Picking 82](#_Toc232860725)

[4.7.3 Post Goods Issue 83](#_Toc232860726)

[4.8 Accounts Receivable 85](#_Toc232860727)

[4.8.1 Change Sales Orders (Remove Billing Block) 85](#_Toc232860728)

[4.8.2 Create Billing Document 86](#_Toc232860729)

[4.8.3 Post Incoming Payment 88](#_Toc232860730)

[4.9 Accounts Payable 90](#_Toc232860731)

[4.9.1 Create Supplier Invoice with PO/GR relation 90](#_Toc232860732)

[4.9.2 Post Outgoing Payment 92](#_Toc232860733)

## Purpose

Overview

The scope item focuses on Lot Size of One based on make-to-order end to end scenario using standard material as an example. The business flow depicts from creation of sale order, covering deficit by material requirement planning runs, production executions followed by logistics and billing.

In this scope item articulation of the make-to-order flow depicted with example of robotic base. The process flow starts with creation of sale order with a billing plan where sale executive details the requirement. Based on the order the MRP run is scheduled to procure or produce the components needed for the production staging and execution. The procured components like steel plates are batch managed.

The procured materials are staged for production. On confirmation of manufacturing operations the finished product is identified as special stock for a sale order at all times. The manufactured product is subject to quality inspection, the quality technician records the inspection results on the inspection lot and confirms the usage decision of the manufactured product. The material is ready for outbound delivery involving picking, packing and goods issue. The story line concluded by creation of billing documents, and completing the outgoing and incoming financial settlements.

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
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST |  |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |
| BOM Engineer | SAP_BR_BOM_ENGINEER | Bills Of Material | SAP_BR_BOM_ENGINEER |  |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing Clerk | SAP_BR_BILLING_CLERK |  |
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Technician | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineer | SAP_BR_QUALITY_ENGINEER |  |
| Quality Planner | SAP_BR_QUALITY_PLANNER | Quality Planning | SAP_BR_QUALITY_PLANNER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Materiel Master Data

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG041 | Roboter Base 1000x2000 Silver | Finished ProductRelevant for planning. MRP Planned and Produced internally as per Make to Order strategy.Inventory Managed. Not Batch Managed. Not split valuated.Sold to customer. This product will undergo quality inspection just before delivery to customer. |
| Material | FG042 | Roboter Base 1500x2000 Silver | Finished ProductRelevant for planning. MRP Planned and Produced internally as per Make to Order strategy.Inventory Managed. Not Batch Managed. Not split valuated.Sold to customer. This product will undergo quality inspection just before delivery to customer. |
| Material | FG043 | Roboter Base 1000x2000 Green | Finished ProductRelevant for planning. MRP Planned and Produced internally as per Make to Order strategy.Inventory Managed. Not Batch Managed. Not split valuated.Sold to customer. This product will undergo quality inspection just before delivery to customer. |
| Material | FG044 | Roboter Base 1500x2000 Green | Finished ProductRelevant for planning. MRP Planned and Produced internally as per Make to Order strategy.Inventory Managed. Not Batch Managed. Not split valuated.Sold to customer. This product will undergo quality inspection just before delivery to customer. |
| Material | SG034 | Servo Motor | Semi-Finished ProductMRP Planned and procured externally.Inventory Managed. Not applicable for Quality Management. Not Batch Managed |
| Material | SG035 | Cut Steel Plate 1000x2000 | Semi-Finished ProductMRP Planned and procured internally.Inventory Managed. Not applicable for Quality Management. Batch Managed |
| Material | SG036 | Cut Steel Plate 1500x2000 | Semi-Finished ProductMRP Planned and procured internally.Inventory Managed. Not applicable for Quality Management. Batch Managed |
| Material | RM027 | Steel Plate | Raw MaterialProcurement with reference to a Purchase Order.MRP Planned and procured externally.Inventory Managed. Not applicable for Quality Management. Batch Managed |
| Material | RM028 | Paint Silver | Raw MaterialProcurement with reference to a Purchase Order.MRP Planned and procured externally.Inventory Managed. Not applicable for Quality Management. Batch Managed |
| Material | RM029 | Paint Green | Raw MaterialProcurement with reference to a Purchase Order.MRP Planned and procured externally.Inventory Managed. Not applicable for Quality Management. Batch Managed |

Organization Data

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Cost Center | 33101301 | Demo Store 3 |  |

Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| FG041 | 0 | FERT | PC | Finished Good for MTO processing with Discrete Manufacturing. | 1 | PC |
| SG034 | 1 | HALB | PC | Externally Procured | 4 | PC |
| RM028 | 1 | ROH | ML | Externally Procured | 1500 | ML |
| SG035 | 1 | HALB | PC | Internally Procured | 1 | PC |
| FG042 | 0 | FERT | PC | Finished Good for MTO processing with Discrete Manufacturing | 1 | PC |
| SG034 | 1 | HALB | PC | Externally Procured | 4 | PC |
| RM028 | 1 | ROH | ML | Externally Procured | 1500 | ML |
| SG036 | 1 | HALB | PC | Internally Procured | 1 | PC |
| FG043 | 0 | FERT | PC | Finished Good for MTO processing with Discrete Manufacturing | 1 | PC |
| SG034 | 1 | HALB | PC | Externally Procured | 4 | PC |
| RM029 | 1 | ROH | ML | Externally Procured | 1500 | ML |
| SG035 | 1 | HALB | PC | Internally Procured | 1 | PC |
| FG044 | 0 | FERT | PC | Finished Good for MTO processing with Discrete Manufacturing | 1 | PC |
| SG034 | 1 | HALB | PC | Externally Procured | 4 | PC |
| RM029 | 1 | ROH | ML | Externally Procured | 1500 | ML |
| SG036 | 1 | HALB | PC | Internally Procured | 1 | PC |

Bill of Material Structure

| Material | Level | Material Type | Unit | Characteristics of Material | Component Quantity | Component UOM |
| --- | --- | --- | --- | --- | --- | --- |
| SG035 | 1 | HALB | PC | Internally Procured | 1 | PC |
| RM027 | 2 | ROH | PC | Externally Procured | 1 | PC |
| SG036 | 1 | HALB | PC | Internally Procured | 1 | PC |
| RM027 | 2 | ROH | PC | Externally Procured | 1 | PC |

Characteristics Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Characteristic | E2E_WIDTH | Width [mm] |  |
| Characteristic | E2E_LENGTH | Length [mm] |  |
| Characteristic | E2E_THICKNESS | Thickness [mm] |  |
| Characteristic | E2E_DENSITY | Density [kg/m3] |  |
| Characteristic | E2E_AREA | Area [mm2] |  |
| Characteristic | E2E_VOLUME | Volume [mm3] |  |
| Characteristic | E2E_WEIGHT | Weight [kg] |  |

Classs Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Class | E2E_ROH | Batch – Class for Raw Material | Class of Type 023 |
| Class | E2E_HALB | Batch – Class for Semi-finished Material | Class of Type 023 |

Work Center:

| Work Center | Plant | Work Center Category | Work center Description |
| --- | --- | --- | --- |
| ASSEMBLY | 3310 | 0001 | Assembly |
| CLEAN | 3310 | 0001 | Clean |
| CUT | 3310 | 0001 | Cut |
| STAMP | 3310 | 0001 | Stamp |
| COAT | 3310 | 0001 | Coat |

Routing:

| Product | Operation | Description | Work Center | Work Center (Alternative) |
| --- | --- | --- | --- | --- |
| FG041 | 0010 | Stamping | STAMP |  |
| 0020 | Spray coating and finish | COAT |  |  |
| 0030 | Assembly | ASSEMBLY |  |  |
| FG042 | 0010 | Stamping | STAMP |  |
| 0020 | Spray coating and finish | COAT |  |  |
| 0030 | Assembly | ASSEMBLY |  |  |
| FG043 | 0010 | Stamping | STAMP |  |
| 0020 | Spray coating and finish | COAT |  |  |
| 0030 | Assembly | ASSEMBLY |  |  |
| FG044 | 0010 | Stamping | STAMP |  |
| 0020 | Spray coating and finish | COAT |  |  |
| 0030 | Assembly | ASSEMBLY |  |  |
| SG035 | 0010 | De-greasing and cleaning | CLEAN |  |
| 0020 | Cutting | CUT |  |  |
| SG036 | 0010 | De-greasing and cleaning | CLEAN |  |
| 0020 | Cutting | CUT |  |  |

Quality Master Inspection Characteristics:

| Master Data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Master Inspection Characteristic | VISINSP | Visual Inspection |  |

Suppliers:

| Master Data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Supplier | 33300001 | Domestic Supplier 1 |  |
| Company Code | 3310 | Company Code 1010 |  |
| Purchase Organization | 3310 | Purch. Org. 1010 |  |

Customer:

| Master Data | Value | Master Data Details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Ship-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Shipping point | 3310 | Shipping Point 1010 |  |
| Company code | 3310 | Company Code 1010 |  |

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference:

| Master Data ID | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |
| BNQ | Create Quality Inspection Plan - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation (Optional) | You have completed the step described in the Standard Cost Calculation (BEG) test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| BFA - Basic Bank Account Management | Bank account master data is processed |
| J58 - Accounting and Financial Close | Execute to create open posting periods |

### Preliminary Steps

#### Create Purchase Info Record

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). | The Manage Purchasing Info Records screen is displayed. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen is displayed. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300001Material: RM027Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 31.12.9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 10Tax Code: <Input Tax Code>Note If time dependent tax (TDT) is activated, and fields Country/Region Key for company code, Validity Periods and Tax Code are maintained via SSCUI 101016 in SAP S/4HANA Cloud Public Edition or the configuration activity Define Tax Codes for Sales and Purchases in Central Business Configuration, you must maintain the Tax Rate Valid From field in the New Purchasing Info Record screen. If you enter the current date, this date will be adjusted to a valid start date for your tax code according to the SSCUI/configuration activity settings.If Registration for Indirect Taxation Abroad (RITA) is activated, and tax registration country and tax code are maintained for company code via SSCUI 103464 in SAP S/4HANA Cloud Public Edition or the configuration activity Activate RITA and Maintain Tax Registration Countries in Central Business Configuration, you must maintain the Tax Country field. The default value of this field is the country ID of company code, but you can change it to a valid country ID that is maintained in the SSCUI/configuration activity accordingly.Order Unit: PCStandard Order Quantity: 1Goods-Receipt-Based Invoice Verification: selectNo Evaluated Receipt Settlement: select | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Conditions section, choose Create.In the General Information area, make the following entries:Valid From: TodayValid To: 12.31.9999Amount: 245,00Currency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | You can enter reference data. | Reference data is added. |  |
| 10 | Create your data | Choose Create. | The purchasing info record is created. |  |

#### Edit User-Specific Parameters for Supplier Invoices (Optional)

Purpose

In this procedure, you will edit User-Specific parameters for supplier invoices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Edit Supplier Invoice Settings (F3813) | The Edit Supplier Invoice Settings screen is displayed. |  |
| 3 | Set parameter | Check parameter Display Journal Entry: XNote If parameter is checked, when invoice is created, system message contains invoice and journal entry number.If parameter is unchecked, when invoice is created, system message contains invoice number only.When this parameter is changed, for APP Create Supplier Invoice, it will take effective immediately. For APP Create Supplier Invoice – Advanced, user needs to logout and login again to make it take effective. | Change has been saved successfully. |  |

Result

Parameter Display Journal Entry has been set successfully.

#### Adapt Routing for Finished Goods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To run through this business scenario, the routing for finished goods need to be enhanced with the final assembly activity to routing operations other than operation 0010 and 0020.

After activating the Scope Item, the following two operations will already be present in the system for all four finished materials (FG041, FG042, FG043, FG044).

| Product | Operation | Description | Work Center | Work Center (Alternative) |
| --- | --- | --- | --- | --- |
| FG041, FG042, FG043, FG044 | 0010 | Stamping | STAMP |  |
| 0020 | Spray Coating and Finish | COAT |  |  |

The third operation 0030, of assembling the product should be added with the Work Center named ASSEMBLY.

| Product | Operation | Description | Work Center | Work Center (Alternative) |
| --- | --- | --- | --- | --- |
| FG041, FG042, FG043, FG044 | 0010 | Stamping | STAMP |  |
| 0020 | Spray Coating and Finish | COAT |  |  |
| 0030 | Assembly | ASSEMBLY |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Change Routing (CA02). | The Change Routing (CA02) screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Continue:Material: FG041Plant: 3310Group: | The Change Routing: Operation Overview screen is displayed. |  |
| 4 | Adapt routing and add third Operation | Make the following entries and choose Go:Operation: 0030Work Center: ASSEMBLYControl Key: YBP1Description: Assembly and press ENTERBase Quantity: 1 PCSet Up: 30 MINMachine: 50 MINLabour: 50 MIN |  |  |
| 5 | Save the Data | Choose Save. | Routing will be saved with group and given material. |  |
| 6 | Add other Data | Repeat steps 2 to 5 for the following materials:FG042FG043FG044 |  |  |

#### Create Initial Material Stock

Purpose

In a real business scenario, initial material stock are usually purchased from external suppliers through standard purchasing or subcontracting processes. For only testing purpose, this process step shows you how to create and post the initial material stock to storage locations directly.

Prerequisite

Before creating initial material stocks, we recommend that you check stock level for RM028, RM029 and SG034. To do that, log onto the SAP Fiori launchpad as a Production Planner, and open Manage Material Coverage - New Version (F0251A) app. You can either post initial stock directly to the storage locations, or refer to test scripts from Procurement of Direct Materials (J45) test scripts for purchasing processes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Choose Document Type | Select Goods Receipt and Other. | The Goods Receipt Other - XXXX screen displays. |  |
| 4 | Enter Data | In the Detail Data section, make the following entries and press Enter.On the Where tab:Movement Type: 561Plant: 3310Storage Location: 331COn the Quantity tab:Quantity:<100 L>On the Material tab:Material: RM028Choose Next Item and select Item OK to add entries. |  |  |
| 5 | Create stock for RM029 | Repeat step 4 for material RM029. |  |  |
| 6 | Create stock for SG034 | Repeat step 4 for material SG034 with storage location 331C and Quantity 50 PC |  |  |
| 7 | Check | Choose Check.If warning message For batch XXXXXX of material XXXXX, no class could be determined is displayed, Click on Continue. | The document is ready to be posted. |  |
| 8 | Post | Choose Post. | Material document XXX is posted and materials are available in stock. |  |

#### Price Change for Individual Material

Purpose

In a real business scenario, valuation price of externally procured materials are determined based on purchase order prices. For only testing purpose, this process step shows you how to maintain a valuation price for materials where initial material stock was created directly.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity updates the material price of a single material with immediate effect.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Material Valuations (F2680). | The Manage Material Valuations (F2680) screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Material: RM027Plant: 3310 | The Current Material Valuation table displays by ledger. |  |
| 4 | Enter Data | Select the first entry in the table to navigate to the details page. Choose Change Inventory Prices on the top right of the screen (if Change Inventory Prices is not visible, choose the More icon first.)Select the current date as the Posting Date.In the Company code currency row of the Reference Price area, change the value of New Price to 250,00.In the Prices in other Valuations area, select the overall check box left of the Valuation View. Now the Convert Prices button becomes active. Choose Convert Prices.Choose Save. |  |  |
| 5 | Maintain Price | Repeat step 3 and 4 for material RM028 and RM029 with price 200. | The Current Material Valuation table displays by ledger. |  |

#### Assign Dependencies

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Some characteristic values of the batch classification are calculated. To do so, dependencies need to be maintained and assigned to the characteristics.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a BOM Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP App | Open Manage Classes. | The Class screen displays. |  |
| 3 | Enter selection criteria | Enter the following data and press enter.Class: E2E_ROHClass Type: 023 | The Change Class screen displays. |  |
| 4 | Go to characteristic details | Go to tab Char. and select E2E_WIDTH. Go to Menu > Environment > Change Characteristic . | Change Characteristic screen is displayed. |  |
| 5 | Create Dependency for E2E_WIDTH | On the Change Characteristic Screen Go to Menu > Extras > Object Dependencies > Editor .Select Procedure in the Dependency Type pop-up and press Continue.Enter the following text to the Editor.$self.E2E_AREA = $self.E2E_LENGTH * $self.E2E_WIDTHif ($self.E2E_LENGTH NE 0 AND $self.E2E_WIDTH NE 0).Choose Save. | Dependency is maintained for E2E_WIDTH. |  |
| 6 | Create Maintain Dependency description | Click on the Object Dependencies button in Basic Data section and select Basic data.Maintain the following data and Save:Description: Area calculation | Dependency is maintained for E2E_WIDTH. |  |
| 7 | Go to characteristic details | Go to tab Char. and select E2E_THICKNESS. Go to Menu > Environment > Change Characteristic . | Change Characteristic screen is displayed. |  |
| 8 | Create Dependency for E2E_THICKNESS | Go to Menu > Extras > Object Dependencies > Editor .Select Procedure in the Dependency Type pop-up and press Continue.Enter the following text to the Editor.$self.E2E_VOLUME = ($self.E2E_LENGTH * $self.E2E_WIDTH * $self.E2E_THICKNESS)if ($self.E2E_LENGTH NE 0 AND $self.E2E_WIDTH NE 0).Press Save. | Dependency is maintained for E2E_THICKNESS. |  |
| 9 | Maintain Dependency description | Click on the Object Dependencies button in Basic Data section and select Basic data.Maintain the following data and Save:Description: Volume calculation | Dependency is maintained for E2E_THICKNESS. |  |
| 10 | Go to characteristic details | Go to tab Char. and select E2E_DENSITY. Go to Menu > Environment > Change Characteristic . | Change Characteristic screen is displayed. |  |
| 11 | Create Dependency for E2E_DENSITY | Go to Menu > Extras > Object Dependencies > Editor .Select Procedure in the Dependency Type pop-up and press Continue.Enter the following text to the Editor.$self.E2E_WEIGHT = ($self.E2E_VOLUME * $self.E2E_DENSITY)/1000000000if ($self.E2E_VOLUME NE 0 AND $self.E2E_DENSITY NE 0).Press Save. | Dependency is maintained for E2E_DENSITY. |  |
| 12 | Maintain Dependency description | Click on the Object Dependencies button in Basic Data section and select Basic data.Maintain the following data and Save:Description: Weight calculation | Dependency is maintained for E2E_DENSITY. |  |
| 13 | Change Display status of characteristic (optional) | In this scenario characteristics are setup to be displayed. If you don’t want to see all characteristics for the batch, the display status can be changed.Select the characteristic and go to Menu > Environment > Change Characteristic .In the Display Characteristics screen select Addnl data and set the No Display flag. Press Save. | Display status of characteristic is changed. |  |

#### Assign Materials to Inspection Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to assign materials to an existing inspection plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Quality Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Plans (F3788) tile. | The Manage Inspections Plans screen displays. |  |
| 3 | Search for Inspection Plan | Make the following entries choose Go.Plant: 3310Material : FG041Go to detailed view. | The Manage Inspections Plans screen displays. |  |
| 4 | Assign Materials to Inspection Plan | Click on Edit on top right cornerIn Material assignment section click on Assign Materials button.In the Select Materials button search for FG042, FG043 and FG044Select the entries with plant 3310 and click OK | Additional materials are assigned to Inspection Plan. |  |
| 5 | Save Inspection Plan | Click on Save. | Changes to Inspection Plan are saved |  |

#### Set Delivery Block Automatically in Milestone Billing Plan (Optional)

Purpose

This optional process step shows you how to set delivery block to sales order items in sales order processing with milestone billing plan.

You can set delivery block automatically with help of SSCUI 102792 Define Date Categories for Billing Plan Types, when using milestone billing plan. Once delivery block reason code is selected from this SSCUI, the delivery block will be set in the schedule lines of corresponding sales order items.

If Apply to BOMs checkbox is selected, the delivery block can be set in all BOM items when at least for one BOM item with billing plan the corresponding delivery block reason code has been selected.

Once down payment is received – steps in chapter [Post a Down payment](#unique_15) [page ] 44 have been completed, delivery block will be removed automatically.

|  |
| --- |
| Note If there is an existing delivery block reason code in a schedule line, it will not be overwritten by the delivery block reason code from billing plan date category. And the delivery block in a schedule line won’t be removed automatically if the delivery block reason code differs from the one set in SSCUI Define Date Categories for Billing Plan Types. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241)Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Configuration Item for Billing Plans | Enter the following filters:Application Area: SalesSub-Application Area: Sales BillingItem Name: Billing Plans | The Configure Your Solution - Billing Plans screen displays. |  |
| 5 | Go to Maintain Date Categories for Milestone Billing Plans Overview | Choose Configure on the right of Define Date Categories for Billing Plan Types. | The Define Date Categories for Billing Plan Types: Change: Details screen displays. |  |
| 6 | Go to Maintain Date Categories for Milestone Billing Plans Detail | Select the line to be edited, for example the line with Billing Plan type 90 and Date Category 04.Choose Details. | The Change View "Define Date Categories for Billing Plan Types": Details screen displays. |  |
| 7 | Set Delivery Block | In the Billing Data area, set delivery block from drop down list, for example, choose 53 Check Prepayment. | Delivery block is set. |  |
| 8 | Set Apply to BOMs (Optional for Sales Kits) | Press Enter after setting delivery block. Select checkbox Apply to BOMs and choose Save. | Apply to BOMs is set.Note Once this checkbox is set, delivery block will be set to all Sales BOM items. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access the Activity | Go to the Business Processes Configuration app and search for the following activity: Define Date Categories for Billing Plan Types.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system.Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Define Date Categories for Billing Plan Types": Overview screen displays. |  |
| 3 | Go to Maintain Date Categories for Milestone Billing Plans Detail | Select the line to be edited, for example the line with Billing Plan type 90 and Date Category 04.Choose Details. | The Change View "Define Date Categories for Billing Plan Types": Details screen displays. |  |
| 4 | Set Delivery Block | In the Billing Data area, set delivery block from drop down list, for example, choose 53 Check Prepayment. | Delivery block is set. |  |
| 5 | Set Apply to BOMs (Optional for Sales Kits) | Press Enter after setting delivery block. Select checkbox Apply to BOMs and choose Save. | Apply to BOMs is set.Note Once this checkbox is set, delivery block will be set to all Sales BOM items. |  |

#### Remove Delivery Block Reason Code Automatically in Milestone Billing Plan (Optional)

Prerequisites

The preliminary steps to this chapter are described in chapter [Set Delivery Block Automatically in Milestone Billing Plan (Optional)](#unique_14) [page ] 24. Only after setting automatic delivery block can the automatic removal of delivery block reason code be enabled.

Purpose

This optional process step shows you how to remove delivery block reason code automatically in milestone billing plan.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241)Note If required, choose Set Local Version to set the desired local version. | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution screen displays. |  |
| 4 | Open Configuration Item for Billing Plans | Enter the following filters:Application Area: SalesSub-Application Area: Sales BillingItem Name: Billing Plans | The Configure Your Solution - Billing Plans screen displays. |  |
| 5 | Access the Configuration Activity | Choose Configure for Define Billing Plan Types for Milestone Billing. | The Define Billing Plan Types for Milestone Billing screen displays. |  |
| 6 | Remove Delivery Block | Select the line to be edited, for example the line with Billing Plan Type 90, choose the checkbox Relevant for Down Payments, and choose Save. | Delivery block reason code will be removed automatically after the down payment is cleared.Note The delivery block in a schedule line won’t be removed automatically if the delivery block reason code differs from the one set in chapter [Set Delivery Block Automatically in Milestone Billing Plan (Optional)](#unique_14) [page ] 24. |  |

Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP CBC page displays. |  |
| 2 | Access the Activity | Go to the Business Processes Configuration app and search for the following activity: Define Billing Plan Types for Milestone Billing.Choose Open Documentation for the line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Billing Plan Types for Milestone Billing screen displays. |  |
| 3 | Remove Delivery Block | Select the line to be edited, for example the line with Billing Plan Type 90, choose the checkbox Relevant for Down Payments, and choose Save. | Delivery block reason code will be removed automatically after the down payment is cleared.Note The delivery block in a schedule line won’t be removed automatically if the delivery block reason code differs from the one set in chapter [Set Delivery Block Automatically in Milestone Billing Plan (Optional)](#unique_14) [page ] 24. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the home page using the search bar.

If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose Settings > App Finder.

| Process Step | Business Role | Transaction/App | Expected Output |
| --- | --- | --- | --- |
| Customer Sales Order and MRP |  |  |  |
| [Create Sales Orders with Billing Plan](#unique_18) [page ] 33 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales Order is created. |
| [Sales Order Pricing (Optional)](#unique_19) [page ] 36 | Internal Sales Representative | Change Sales Orders - VA02 (VA02) | Sales Order price is maintained. |
| [Change Sales Orders (Remove Billing Block)](#unique_20) [page ] 37 | Internal Sales Representative | Manage Sales Orders (F1873) | The billing block is removed. |
| [Material Requirements Planning at Plant Level](#unique_21) [page ] 38 | Production Planner | Monitor External Requirements (F0246A) | An MRP run is started immediately in background. |
| [Evaluating Stock/Requirements Situation](#unique_22) [page ] 39 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| Accounts Receivable |  |  |  |
| [Create Down Payment Request](#unique_23) [page ] 42 | Billing Clerk | Create Billing Documents (F0798) | Billing document is generated. |
| [Post a Down payment](#unique_15) [page ] 44 | Accounts Receivable Accountant | Post Incoming Payments (F1345) |  |
| Procurement of Component |  |  |  |
| [Convert Purchase Requisitions to Purchase Orders](#unique_24) [page ] 46 | Purchaser | Process Purchase Requisitions (F1048A) |  |
| [Preview Purchase Order (Optional)](#unique_25) [page ] 47 | Purchaser | Manage Purchase Orders (F0842A) |  |
| [Post Goods Receipt](#unique_26) [page ] 48 | Warehouse Clerk | Post Goods Receipt for Purchasing Document (F0843) |  |
| [Maintain Batch Classification](#unique_27) [page ] 49 | Quality Technician | Change Batch (MSC2N) |  |
| [Check Range of Stock Coverage](#unique_28) [page ] 50 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| Production Order Execution for Semi finished Product |  |  |  |
| [Convert Planned Order to Production Order for Semifinished Product](#unique_29) [page ] 52 | Production Planner | Manage Material Coverage - New Version (F0251A) |  |
| [Execute Material Staging for Production Order](#unique_30) [page ] 54 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) |  |
| [Release Production Order](#unique_31) [page ] 55 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) |  |
| [Pick Components for Assembly](#unique_32) [page ] 56 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) |  |
| [Final Confirmation of Production Operations](#unique_33) [page ] 57 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) |  |
| [Event-Based Work in Progress (Optional)](#unique_34) [page ] 58 | Cost Accountant - Production. | Work in Process - Event-Based (F3498) |  |
| [Post Goods Receipt for Production Order](#unique_35) [page ] 60 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Review Production Order (Optional)](#unique_36) [page ] 61 | Production Supervisor - Discrete Manufacturing | Manage Production Operations (F2335) |  |
| Production Order Execution for Finished Product |  |  |  |
| [Convert Planned Order to Production Order for Finished Product](#unique_37) [page ] 62 | Production Planner | Manage Material Coverage - New Version (F0251A) |  |
| [Material Staging for Production Order](#unique_38) [page ] 64 | Production Operator - Discrete Manufacturing | Stage Materials for Production (MF60) |  |
| [Release Production Order](#unique_39) [page ] 65 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) |  |
| [Final Confirmation of Production Operations](#unique_40) [page ] 66 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) |  |
| [Post Goods Issue for Final Assembly Production Order Components](#unique_41) [page ] 67 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Post Goods Receipt for Finished Product Production Order](#unique_42) [page ] 69 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Evaluate Stock/Requirement Situation (Optional)](#unique_43) [page ] 70 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| [Batch Information Cockpit - Batch Selection (Optional)](#unique_44) [page ] 71 | Quality Technician | Batch Information Cockpit (BMBC) |  |
| [Batch Information System - Batch Analysis (Optional)](#unique_45) [page ] 72 | Quality Technician | Batch Information Cockpit (BMBC) |  |
| [Event-Based Production Costing - Order Costs (Optional)](#unique_46) [page ] 74 | Cost Accountant - Production | Analyze Production Costs - Event-Based (F4059) |  |
| [Product Profitability with Production Variances](#unique_47) [page ] 75 | Cost Accountant - Sales | Product Profitability with Production Variances (W0182) |  |
| Quality Inspection during Goods Receipt from Production |  |  |  |
| [Display Material Stock Before Quality Inspection](#unique_48) [page ] 76 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Display Open Inspection Lots](#unique_49) [page ] 77 | Quality Technician | Manage Inspection Lots (F2343) |  |
| [Record Inspection Results](#unique_50) [page ] 78 | Quality Technician | Manage Inspection Lots (F2343) |  |
| [Make Usage Decision](#unique_51) [page ] 79 | Quality Engineer | Manage Usage Decisions (F2345) |  |
| [Display Material Stock after Usage Decision (Optional)](#unique_52) | Warehouse Clerk | Stock - Single Material (F1076) |  |
| Outbound Delivery Processing |  |  |  |
| [Create Delivery](#unique_53) [page ] 81 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Execute Picking](#unique_54) [page ] 82 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Post Goods Issue](#unique_55) [page ] 83 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| Accounts Receivable |  |  |  |
| [Change Sales Orders (Remove Billing Block)](#unique_56) [page ] 85 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Billing Document](#unique_57) [page ] 86 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Post Incoming Payment](#unique_58) [page ] 88 | Accounts Receivable Accountant | Post Incoming Payments (F1345) |  |
| Accounts Payable |  |  |  |
| [Create Supplier Invoice with PO/GR relation](#unique_59) [page ] 90 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) |  |
| [Post Outgoing Payment](#unique_60) [page ] 92 | Accounts Payable Accountant | Post Outgoing Payments (F1612) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Customer Sales Order and MRP

#### Create Sales Orders with Billing Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to require a down payment from the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders screen, choose Create and select Create Sales Order - VA01. | The Create Sales Documents screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Sales Document Type: OR (Standard Order)Sales organization: 3310Distribution channel: 10Division: 00Choose Continue. | The Create Standard Order: Overview screen displays. |  |
| 5 | Enter Customer Number | Make the following entries:Sold-To Party: 33100001Customer Reference: <Reference>Cust. Ref. Date: <Date>Choose Enter. |  |  |
| 6 | Enter Order Details | Make the following entries:Material: <FG041 or FG042 or FG043 or FG044 depending on size and colour>Order Quantity: 1Req. Deliv.Date: <In 3 weeks>Note The billing of this business process is order-related. This means that the down payment request and the final invoice only contain the information that is available from the sales order like material, quantity, and batch number.Choose Enter. |  |  |
| 7 | Choose Billing Plan | Select the item. Choose Menu > Goto > Item > Billing Plan .Note Alternatively, you can assign billing plan on header level: Choose Menu > Goto > Header > Billing Plan . The header billing plan will be applied to all items with item category CBAO, CTAD or CTAX. Amount is proportionally to the value of the items participating in the down payment process distributed to the items. |  |  |
| 8 | Enter Details | For the first line item (Down Payment), make the following entries for the advance payment:Billing Date: <billing date>. For example, enter today's date.Bill Value: <amount of billing>. For example: Down Payment amountDate category (DCat): 04 | You can create more than one Down Payment by using same entries as 1st Down Payment. |  |
| 9 | Enter Details | For the second line item (Final Invoice), make the following entries for the advance payment:Billing Date: <billing date>. For example, in 3 weeks.Date category (DCat): 02 |  |  |
| 10 | Enter | Choose Enter. Confirm system messages with enter if necessary. | Final Invoice related data is determined. For example, in Bill value field, the amount of billing is calculated by the system. |  |
| 11 | Back | Choose Back. |  |  |
| 12 | Save | Save your entries. |  |  |

|  |
| --- |
| Note Via SSCUI Maintain Date Categories for Milestone Billing Plans, you can assign a delivery block reason code to milestone billing plan. In this case, when creating a sales order and using this billing plan together with item category CBAO (Milestone Bill.Plan), the delivery block reason code will be copied to the schedule lines. If you delete the billing plan from sales order afterwards, the schedule lines will not be updated automatically. In case the item category or schedule line category changes afterwards, delivery block reason code will still be kept. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Enter search term(s) in filter bar and choose Go. For example, enter sales order number in the Sales Order field. | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right side of the Sales Order item and navigate to Display Standard Order xxx: Overview screen. | The Display Sales Order xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Menu > Extras > Output > Header > Edit . |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display Document. | Preview for PDF document displays. |  |

#### Sales Order Pricing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows how to check sales order price conditions and change the sales order specific pricing. It also shows the sales order costing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Sales Orders - VA02 (VA02). | The Change Sales Documents screen displays. |  |
| 3 | Open Sales Order | Enter the following data and press Continue:Order : <Sales Order number created above> | Sales Order is displayed. |  |
| 4 | Check Sales Order Pricing | Select the Item and press Item Condition. | Sales order pricing conditions are displayed. |  |
| 5 | Change PPR0 (optional) | To change the PPR0 pricing condition specifically for this sales order change the price in field Amount for condition type PPR0.Click Save. | Price is updated. |  |

#### Change Sales Orders (Remove Billing Block)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove billing block from a sales order, if it exists. Otherwise this process step can be skipped.

Prerequisite

The billing block must be manually removed for the first down payment request to be processed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Enter search term(s) in filter bar and choose Go: for example, enter sales order number in Sales Order field. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Select the sales order number and choose Change Sales Order - VA02. | The Change Sales Order xxx: Overview screen displays. |  |
| 5 | Choose Billing Plan | Select the line item. From the menu, choose Menu > Go to > Item > Billing plan .Note Alternatively, If you assign billing plan on header level: Choose Menu > Goto > Item > Billing plan . Removal of billing block on header level also unlocks items automatically. | The Change Standard Order xxx: Item Data screen displays. |  |
| 6 | Delete Billing Block | In the Dates section, in the Block column delete the billing block for the Down payment item, if it exists (keep the billing block for the Final Invoice item). |  |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Save | Save your entries. | The billing block is removed. |  |

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

The finished goods are planned at plant level. There is now a requirement for the finished good from sales order created above in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Schedule MRP Runs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: < MRP for FG041/FG042/FG043/FG044 >Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: < Material used in sales order created above FG041, FG042, FG043 or FG044 >All Order BOM Components: <select>Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG041/FG042/FG043/FG044 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Jobs table when refreshed. |  |

#### Evaluating Stock/Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Order finished goods (FG041, FG042, FG043 or FG044) in the stock/requirements list after the requirement planning is performed.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net and Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | Search in the Material bar, select the following materials and then choose Manage Materials:Material: <Material used in sales order created above FG041, FG042, FG043 or FG044)>Material: SG034Material:SG035 if FG041 or FG043 is maintained in Sales OrderSG036 if FG042 or FG044 is maintained in Sales OrderMaterial: RM027Material:RM028 if FG041 or FG042 is maintained in Sales OrderRM029 if FG043 or FG044 is maintained in Sales Order | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock / Requirements List | Choose the corresponding material in the Materials list on the left side. | The detailed stock / requirements list for each material displays. |  |
| 6 | Display Planned Order | From the Materials list on the left side, choose the material for which you want to check for the planned order:Material: <Material used in sales order created above FG041, FG042, FG043 or FG044)>Material:SG035 if FG041 or FG043 is maintained in Sales OrderSG036 if FG042 or FG044 is maintained in Sales OrderOn the right screen, choose PldOrd XXXX in the MRP Element column.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If there is not enough inventory to fulfill the requirements, planned orders and purchase requisitions are created for both inhouse-produced and externally-procured materials.Depending on the elements created in the MRP run, refer to Procurement of Direct Materials(J45) or Scheduling Agreements in Procurement (BMR) test scripts for processing externally-procured materials. | The selected planned order displays.Note The planned order is generated only when there is shortage for these materials.If you want to display more information of the planned order, choose Document Info at the bottom of the dialog box. |  |
| 7 | Rescheduling Check (Optional) | On the Stock/Requirements List tab, the Rescheduling column displays the rescheduling status of the following MRP elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersIf needed,you can choose the following icons in Rescheduling column for corresponding functions:Reschedule in (bring operation forward if the receipt element lies after the requirement date)Reschedule out (postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment |  |  |

### Accounts Receivable

#### Create Down Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a down payment request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings. You can make the settings as follows :Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose Sales Document | More than one SD document item appear in Billing Due List Items table, select the row relevant to down payment request, and choose Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Down payment request (FAZ) and maintain billing date, for example current date, then choose OK. | The draft billing document is created. |  |
| 7 | Save Billing Document | On the Manage Billing Document screen, choose Save.The draft billing document with ID TMPxxxxxxxx turns into a saved billing document with ID xxxxxxxx.Make a note of the billing document number: __________. | Billing document is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Good (FERT) | 21191000 Down payment requests (customers) | none | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797) | The Manage Billing Documents screen displays. |  |
| 2 | Search the Billing Document | Enter the billing document number recorded previously in Billing Document field and choose Enter. | The billing document which is created previously displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The Manage Billing Documents screen displays. |  |
| 4 | Check Output Condition | On the Manage Billing Documents screen, go to Output Items, the last assignment block. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Manage Billing Documents screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Manage Billing Documents screen, select certain Billing document and choose Cancel billing Document. | Billing Document Canceled log displays. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete, and update the attachments.Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete and update the texts.Save your changes by choosing Save in the footer bar. |  |  |

#### Post a Down payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process steps shows you how to post a down payment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Incoming Payments (F1345). | The Post Incoming Payments screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Propose Items:General Information area:Company Code: 3310Posting Date: <Current Date>Journal Entry Date: <Current Date>Value Date: <Current Date>Period: <Current Period>Journal Entry Type: <DZ(Customer Payment)>Bank Data area:G/L Account (Company Code CoA): 11001060House Bank: AEBK1Bank Account: AEAC1Amount: Down Payment Amount / AEDNote Enter the amount of the journal entry the customer has been debited with in the previous step(billing value plus value added tax)Open Item Selection areaAccount Type/Account ID: 33100001 |  |  |
| 4 | Search for Down Payment Request | Choose Select More.In Line Item Type field, select the checkbox in Special G/L Transactions and deselect other values from the dropdown menu, then choose OK. | The Select More dialog box displays.All down payment request documents which meet the conditions are listed in the Open AP/AR Items table. |  |
| 5 | Select Down Payment Request | Choose Clear in the down payment request document entry in the Open AP/AR Items table. | The item is copied to the Items to Be Cleared table. |  |
| 6 | Post | Choose Post. | Success dialog box pop ups. The information Journal entry 14XXXXXXXX successfully posted displays. |  |
| 7 | Display Journal Entry | Choose Display. | Journal Entry screen displays. Detailed information involved in down payment journal entry is shown. |  |

|  |
| --- |
| Note After the down payment is cleared, the delivery block set from SSCUI Define Date Categories for Billing Plan Types in chapter [Set Delivery Block Automatically in Milestone Billing Plan (Optional)](#unique_14) [page ] 24 can be removed automatically if the check box Relevant for Down Payments is flagged in SSCUI Define Billing Plan Types for Milestone Billing for billing plan type 90.The delivery block in a schedule line won’t be removed automatically if the delivery block reason code differs from the one set in SSCUI Define Date Categories for Billing Plan Types |

Table 1: Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Finished Good (FERT) | 11001060Bank Account21191500 Tax sett.dwn pmt cus | 21190000 Down Payments - Customers22000000 Output tax (MWS) | none |

### Procurement of Component

#### Convert Purchase Requisitions to Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to convert assigned Purchase Requisitions to Purchase Orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Purchase Requisitions (F1048A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of Requisitions are displayed. |  |
| 3 | Search for Purchase Requisition | Enter the Purchase Requisition number (RM027) from above step and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the Purchase Requisition. | The Purchase Requisition has been selected for source assignment. |  |
| 5 | Assign Source to Purchase Requisition | Choose Show More per Row button on the side of Create Contract. If the Purchase Requisition has been assigned the source, then you don't need to assign source again for this step. If the Purchase Requisition hasn't been assigned the source, choose Assign Source of Supply, and then enter a source. | The assignment of one source to the requisition is done. |  |
| 6 | Prepare the Purchase Order | Select the purchase Requisition where the assigned supplier is displayed and choose Create Purchase Order. | The Purchase Order Preview screen is displayed. |  |
| 7 | Create the Purchase Order | In the New Purchase Order screen, make the following entry:Purchase Doc. Type: Standard PO (NB).Choose Order. | The purchase order is created. |  |
| 8 | Back to Process Purchase Requisition | Click on Back to go to Process Purchase Requisitions (F1048A). | Purchase Requisition list is displayed again.The Processing Status of Purchase Requisition has been changed to PO created (B). |  |

#### Preview Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can preview an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Purchase Orders (F0842A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Select Purchase Order | Enter the Purchase Order number in the Purchase Order search box, and choose Go. Select the row for the Purchase Order you want to preview and use the little arrow on the right side to check the PO detail. | The Purchase Order screen is displayed. |  |
| 4 | Preview the Purchase Order | Note When the Relevant and Merge are both selected for the document type SL1 and channel print in SSCUI: 103542 (Define Output Settings for Document Type), you upload the attachments of SL1 document type in Attachments Tab at the item level in App: Manage Purchase Orders, then the output should contain the Attachments as Document along with PO output.At the Output Management line item, the number of attachments for the Line item should match the number of attachments we attached. | The Purchase Order is opened in PDF format. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Goods ordered by a purchase order arrive at warehouse. The goods receipt is to be posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Goods Receipt for Purchasing Document (F0843). | The Post Goods Receipt for Purchasing Document screen is displayed. |  |
| 3 | Enter Purchase Order | Enter the Purchase Order ID and choose Enter. | The system displays the data for the goods receipt on the Post Goods Receipt for Purchasing Document screen. |  |
| 4 | Enter Delivery Note | Make the following entries and choose Enter:Delivery Note: <Delivery Note>Printing: Individual slip |  |  |
| 5 | Maintain Batch | Click on the item line in the Items section to go to Goods Receipt Item Screen.Click on Maintain Batch button in Plant Options section.Press Apply.Note To maintain batch classification during goods receipt processing use a personalized user with all required Business Roles. |  |  |
| 6 | Select Item | From the Items section, select the goods receipt item to be posted.Choose Storage Location (for example) 331C.Note Select an item with a quantity of two or more pieces. | You can see that the Post button is activated. |  |
| 7 | Post | Choose Post. | The system displays the message 1 document(s) created: Material Document: 5XXXXXXXXX. |  |

#### Maintain Batch Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintain batch characteristics values for procured batch relevant material RM027.

Prerequisite

Batch has to be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Change Batch (MSC2N).Note To maintain batch classification during goods receipt processing use a personalized user with all required Business Roles. | The Change Batch screen displays. |  |
| 3 | Select Batch | To maintain batch characteristic values, enter the following data and press Continue.Material: <Material from purchase order RM027 or RM028>Batch: <Batch created in step above> | Batch details are displayed. |  |
| 4 | Maintain batch characteristic values | Maintain batch characteristic values for material procured in step above.Under Classification tab, click on Create Classification button and enter the following :Length: <more than 2000>Width: <more than 1500>Thickness: <enter a value>Density: <enter a value>Area, Volume and Weight are calculated based on the values entered for Length, Width, and Thickness.Press Save. | Batch characteristics values are maintained. |  |

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
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net and Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon and select App Settings. In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage (F0251A) is on.Turn it on if the toggle button is oﬀ . | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage.If the toggle button is oﬀ, you will be navigated to Check Material Coverage (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | Choose Adapt Filters to add the Material and Plant filter if not added, enter the following value, and choose Go:.Material: <Material used in sales order created above (FG041, FG042, FG043 or FG044)>Material: SG034Material:SG035 if FG041 or FG043 is maintained in Sales OrderSG036 if FG042 or FG044 is maintained in Sales OrderMaterial: RM027Material:RM028 if FG041 or FG042 is maintained in Sales OrderRM029 if FG043 or FG044 is maintained in Sales OrderPlant: 3310Select the material and choose Manage Materials | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock / Requirements List | To display Rescheduling column click on settings icon, select Rescheduling Date in pop up and press OK.On the Stock/Requirements List tab, the rescheduling status of the following MRP elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersYou can choose the following icons for corresponding functions:Reschedule in (bring operation forward if the receipt element lies after the requirement date)Reschedule out (postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment | Corresponding action to be performed. |  |
| 6 | Review the Status and Coverage Days | Make following entries and choose Refresh:Shortage Definition: MRP Standard | The selected planned order displays.Note The planned order is generated only when there is shortage for these materials.If you want to display more information of the planned order, choose Open... > Planned Order at the bottom right of the dialog box. |  |
| 7 | Return to Home | Choose the Home icon |  |  |

### Production Order Execution for Semifinished Product

#### Convert Planned Order to Production Order for Semifinished Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to convert the planned orders to production orders for both semi finished goods and finished goods when reached the planned start date.

Prerequisite

The MRP run has generated planned orders for SG035/SG036 (sub assembly) and FG041/FG042/FG043/FG044 (final assembly).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | On the Manage Material Coverage screen, enter the following data and choose Go.Material:SG035 if FG041 or FG043 is maintained in Sales OrderSG036 if FG042 or FG044 is maintained in Sales OrderPlant: 3310Shortage Definition: MRP StandardCheck column Individual Segment for the Sales Order Number and Item created above.Choose the row of the filtered material to check more details. | The Manage Material Coverage screen displays with more details. |  |
| 4 | Find Planned Order | Check the generated planned orders. |  |  |
| 5 | Add Planned Order Long Text (Optional) | Click on the planned order number (PldOrd XXXX) under column MRP Element. In the pop-up dialog PldOrd XXXX, choose Change Planned Order.On the Change Planned Order screen, choose tab Long Text, enter the text, and choose Save. | The long text maintained here can be later copied to the converted production order. |  |
| 6 | Convert Planned Order to Production Order | Select Convert from Edit dropdown list in the Actions column for a planned order (PldOrd XXXX).In the Convert Planned Order XXXX dialog box, choose Convert to Production Order, confirm Delivery Date and Quantity. Choose Convert. | The production order is created. |  |

|  |
| --- |
| Note Start from CE2202, it's possible to change the default settlement rule receiver from material to cost center or WBS element for event-based production orders/process orders. For details, you can check the chapter Create/Change Settlement Rule for Non-Material Settlement in Scope Item 3F0 (Event-Based Production Cost Posting). |

#### Execute Material Staging for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to stage materials for final assembly production.

|  |
| --- |
| Note If there is sufficient stock available in the production storage location, then no line items are generated. |

Prerequisite

Stock must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.In the Staging Types section:SLoc Level: <select>Plant: 3310Selection Horizon for Reqmts: <date must be in the future - after scheduled start date>On the Production/Process Orders tab:Order: <Production Order Number created in above step> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | In the Total Reqmts table, select the line items and choose Replenishment Proposals on the top of the screen.Maintain the quantity to be staged in field Quantity staged.Review staged quantities and choose Replenishment Elements. |  |  |
| 5 | Enter Replenishment Storage Location and Batch Number | At the bottom half of the split screen, in the RepLoc column of the Replen. Element table, enter 331C for staged materials.In the bottom half of the screen select the replenishment element and press Batch/Stck Determination. The batch is determined based on the Inventory Management Batch Search Strategy. |  |  |
| 6 | Stage and Save | Choose Stage and choose Save.Note Missing materials are transferred to the shop floor from the designated storage area.The shortage of raw material for final assembly production order is supplied with this step. | Material is staged for final assembly. |  |

#### Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A release at order operation level results in the release of the order and all its operation. The order and the operations receive the REL (released) status.

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE (3310)MTO w/o VC - Val.(YB4)Choose Back. |  |  |
| 4 | Select Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, select Material and Production Plant and choose OK.Enter the following filter criteria, and choose Go:Status: CreatedMaterial:SG035 if FG041 or FG043 is maintained in Sales OrderSG036 if FG042 or FG044 is maintained in Sales OrderProduction Plant: 3310 | The Material and Production Plant fields are added to the filter bar.Corresponding orders display. |  |
| 5 | Release the production order | Select the order to be released.Choose Release in the top right corner. | The 1 of 1 orders have been released message displays and the order is released. |  |

#### Pick Components for Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to pick components.

Prerequisite

Ensure there is sufficient amount of component in the service stock. To check the stock level, you can use the Inventory Manager user role to access the Display Stock Overview (MMBE) App.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen displays. |  |
| 3 | Enter Relevant Search Criteria | Make the following entries and choose Run.Profile: <000002>Production Order: <production order for created in step above> | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking | Select the relevant reservations and choose Picking. | A list of all the selected reservations displays. |  |
| 5 | Batch Determination | Select relevant line item and choose Batch Determination to assign batch numbers. | Batch is determined for RM027. |  |
| 6 | Post | Press Post. | The goods movements is posted. |  |

#### Final Confirmation of Production Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to execute confirmations of all assembly activities of the production order before posting the goods receipt. The backflush is carried out together with the confirmation steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <Production Order number>Operation:0010 |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <yield amount>Scrap: <scrap amount> |  |  |
| 5 | Enter Activities Data | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time> |  |  |
| 6 | Save Your Entries | Choose Post and Complete to make final confirmation for this operation. | The final confirmation is made |  |
| 7 | Confirm second Operation | Repeat steps 3 – 6 for Operation 0020 |  |  |

#### Event-Based Work in Progress (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run the report to review event-based WIP and variance. This step is executed in the same manner for partially and totally delivered production orders.

|  |
| --- |
| Note Event-based WIP is posted by Ledger. So if you have any other standard ledgers like 2L OR 3L, you can execute the report for each ledger to review the WIP. |

|  |
| --- |
| Note The Display Journal Entries - In T-Account View (F3664) and Display Document Flow (F3665) apps that are part of the General Ledger Accountant role can be used to review the WIP and variance posted with goods issue, goods receipt, and activity confirmation of orders. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Work in Process - Event-Based (F3498). | The Work in Process - Event-Based screen displays. |  |
| 3 | Enter Selection Parameters | Make the following entries:Key Date: <Current date>Ledger: 0LCompany Code: 3310Currency: AEDPlant: 3310Order Type: <YBM4>Order: <Order created in step above> |  |  |
| 4 | Run the Event-Based Work in Process | Choose the Go button. | The production order does not display on the result list in the following cases:technically completed (TECO)delivery completed (DLV) including Goods Receipt Quantity >= Order QuantityDel. Completed Ind. is set on the order and/or on the last Goods Receipt posting |  |

#### Post Goods Receipt for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for production order of final assembly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Receipt Order | Choose Goods Receipt > Order in the header area and make the following entries:Order: <production order created in step above>GR goods receipt: <101>Document date: <default>Posting date: <default>On the General tab, next to the Printer icon, select Print via Output Control (mouseover) checkbox, and choose Individual Slip. |  |  |
| 4 | Enter Quantity | On the Quantity tab, confirm production order quantities.On the Where tab, confirm Storage Location 331B |  |  |
| 5 | Maintain Batch | To create a new batch, go to Batch Tab and select Classification.Maintain the following Characteristic Values:Length: 2000Width: <1000 for SG035, 1500 for SG036>Thickness: <maintain a value>Density: <maintain a value>Go back to previous screen. |  |  |
| 6 | Set Item OK and Post | Select the Item OK checkbox and choose Post. | The system displays the message Material document 500xxxxxxx posted. |  |

#### Review Production Order (Optional)

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
| 3 | Select Production Order | On the Manage Production Operations screen, choose Adapt Filters to display more filter options.In the Adapt Filters dialog box, select Material and Production Plant (3310) and choose OK.Enter the following filters criteria and choose Go.Material:SG035 if FG041 or FG043 is maintained in Sales OrderSG036 if FG042 or FG044 is maintained in Sales Order | The Material and Plant fields are then added to filter bar.Selected order displays. |  |
| 4 | Check Detailed Operations Status | Check detailed information for selected production operations.Operation Issues:Empty if there is no production order issue.Delay or Missing Components / PRT issue or Quantity Deviation / Quality Issue information shows if relevant issue exists.Components:Material, total quantity and Issued / open quantity information for order components displays.Order Schedule:Detailed operation information with relevant work center, confirmed quantity, start and end time displays.Work Center Schedule:The relevant order covering the same work center capacity (operation is partially confirmed) displays.Operations not Started:The relevant order that would cover the same work center capacity (operation is released) displays.Confirmation:Detailed confirmation information with Yield, Scrap, Rework quantity displays if confirmation has been executed.Inspection:Detailed inspection lots information displays if existed. | Detailed operations status displays. |  |

### Production Order Execution for Finished Product

#### Convert Planned Order to Production Order for Finished Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Daily MRP run creates planned orders for goods to be produced internally. This process step shows you how to convert the planned orders to production orders for both semifinished goods and finished goods when reached the planned start date.

Prerequisite

Procedure

The MRP run has generated planned orders for SG035/SG036 (sub assembly) and FG041/FG043 or FG042/FG044 (final assembly).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | On the Manage Material Coverage screen, enter the following data and choose Go.Material: <Material used in sales order created above FG041, FG042, FG043 or FG044>Plant: 3310Shortage Definition: MRP StandardCheck column Individual Segment for the Sales Order Number and Item created above.Choose the row of the filtered material to check more details. | The Manage Material Coverage screen displays with more details. |  |
| 4 | Find Planned Order | Check the generated planned orders.If no planned orders are generated, it could be because the material has sufficient amount of stock in store. In this case, remove some stock. Go back to create PIRs and run MRP again to generate planned orders. |  |  |
| 5 | Add Planned Order Long Text (Optional) | Click on the planned order number (PldOrd XXXX) under column MRP Element. In the pop-up dialog PldOrd XXXX, choose Change Planned Order.On the Change Planned Order screen, choose tab Long Text, enter the text, and choose Save. | The long text maintained here can be later copied to the converted production order. |  |
| 6 | Convert Planned Order to Production Order | Select Convert from Edit dropdown list in the Actions column for a planned order (PldOrd XXXX).In the Convert Planned Order XXXX dialog box, choose Convert to Production Order, confirm Delivery Date and Quantity. Choose Convert. | The production order is created. |  |

#### Material Staging for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to stage materials for final assembly production.

|  |
| --- |
| Note If there is sufficient stock available in the production storage location, then no line items are generated. |

Prerequisite

Stock must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.In the Staging Types section:SLoc Level: <select>Plant: 3310Selection Horizon for Reqmts: <date must be in the future - after scheduled start date>On the Production/Process Orders tab:Order: <Production Order Number created in step above> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Elements | In the Total Reqmts table, select the line items and choose Replenishment Proposals on the top of the screen.Review staged quantities and choose Replenishment Elements. |  |  |
| 5 | Enter Replenishment Storage Location and Batch Number | In the bottom half of the screen select the replenishment element and press Batch/Stck Determination. The batch is determined based on the Inventory Management Batch Search Strategy.In the RepLoc column of the Replen. Element table,Enter 331C for material SG034 and RM028/RM029 |  |  |
| 6 | Stage and Save | Select all materials in Replen. Elements table.Choose Stage and choose Save.Note Missing materials are transferred to the shop floor from the designated storage area.The shortage of raw material for final assembly production order is supplied with this step. | Material is staged for final assembly. |  |

#### Release Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A release at order operation level results in the release of the order and all its operation. The order and the operations receive the REL (released) status.

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). |  |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE (3310)MTO w/o VC - Val.(YB4)Choose Back. |  |  |
| 4 | Select Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, select Material and Production Plant and choose OK.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: <Material used in sales order created above FG041, FG042, FG043 or FG044>Production Plant: 3310 | The Material and Production Plant fields are added to the filter bar.Corresponding orders display. |  |
| 5 | Release the production order. | Select the order to be released.Choose Release in the top right corner. | The 1 of 1 orders have been released message displays and the order is released. |  |

#### Final Confirmation of Production Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to execute confirmations of all assembly activities of the production order before posting the goods receipt. The backflush is carried out together with the confirmation steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <Production Order Number>Operation:0010 |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <yield amount>Scrap: <scrap amount> |  |  |
| 5 | Enter Activities Data | In the Activities section, make the following entries:Setup: <setup time>Machine: <machine time>Labor: <labor time> |  |  |
| 6 | Save Your Entries | Choose Post and Complete to make final confirmation for this operation. | The final confirmation is made. |  |
| 7 | Enter second and third Operation | Repeat steps 3 – 6 for Operation 0020 and 0030. |  |  |

#### Post Goods Issue for Final Assembly Production Order Components

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods issue for production order of final assembly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Issue Order | Choose Goods Issue > Order in the header area and make the following entries:Order: <production order number for finished goods>GR goods receipt: <261>Document date: <default>Posting date: <default>On the General tab, next to the Printer icon, select Print via Output Control (mouseover) checkbox, and choose Individual Slip. |  |  |
| 4 | Enter Quantity | For material RM028 / RM029 check and maintain the following tabs,On the Quantity tab, confirm production order quantities.On the Where tab, confirm Storage Location 331BOn the Batch tab, enter the batch. |  |  |
| 5 | Set Item OK and Post | Select the Item OK checkbox and choose Post. | The system displays the message Material document 500xxxxxxx posted. |  |
| 6 | Enter Quantity | For material SG035/SG036 check and maintain the following tabs,On the Quantity tab, confirm production order quantities.On the Where tab, confirm Storage Location 331BOn the Batch tab, enter the batch created during semi finished production above for this Sales order. |  |  |
| 7 | Post Goods Movement | Select the Item OK checkbox and choose Post. | The system displays the message Material document 49xxxxxxx posted. |  |

#### Post Goods Receipt for Finished Product Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for production order of final assembly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Enter Goods Receipt Order | Choose Goods Receipt > Order in the header area and make the following entries:Order: <production order number for finished goods>GR goods receipt: <101>Document date: <default>Posting date: <default>On the General tab, next to the Printer icon, select Print via Output Control (mouseover) checkbox, and choose Individual Slip. |  |  |
| 4 | Enter Quantity | On the Quantity tab, confirm production order quantities.On the Where tab, enter the following entry:Storage Location: <331A (Std. storage 1)> |  |  |
| 5 | Set Item OK and Post | Select the Item OK checkbox and choose Post. | The system displays the message Material document 500xxxxxxx posted. |  |

#### Evaluate Stock/Requirement Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the stock/requirements situation for Make-to-Order finished goods (FG041/FG042/FG043/FG044) in the stock/requirements list after the requirement planning is performed.

Prerequisite

Requirement planning is carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net and Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage.If the toggle button is off, you will be navigated to Check Material Coverage.The following steps are described with the toggle button on. |  |
| 4 | Select Material | Search in the Material bar, select the following materials and then choose Manage Materials:Material: <Material used in sales order created above FG041, FG042, FG043 or FG044> | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock / Requirements List | Choose the corresponding material in the Materials list on the left side.Observe the stock situation for the material. | The detailed stock / requirements list for each material displays.QM lot has been created at goods receipt from Production Order. |  |

#### Batch Information Cockpit - Batch Selection (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this functionality you can search for batches according to different selection criteria, like material data, classification, best-before date, … You can adapt the selection in the Batch Information Cockpit to customer-specific requirements by creating user-specific groups. You can get additional information by using subsequent actions.

|  |
| --- |
| Note You can use each batch managed material that is delivered to a customer. If you do not have an adequate material, run test script (Make-to-Order Production – Finished Goods Sales and Final Assembly) BJE. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Select Batches for semifinished materials | On the Batch Information Cockpit screen, make the following entries.Go to the Material tab:Material:SG035 if FG041 or FG043 is maintained in Sales OrderSG036 if FG042 or FG044 is maintained in Sales OrderPlant: 3310Go to the Classification tab.Batch Class: E2E_HALBChoose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Display Stock Information | Choose Display Selection Result for Stock. | A new screen section on the left hand panel is opened, displaying the selected batches sorted by plant and storage location. |  |
| 5 | Display Worklist | Choose Display Worklist. | A new screen section on the left hand panel is opened, displaying the batches for later processing. Also batches from previous assignments are displayed. |  |
| 6 | Select Batches for Steel Plate | Repeat Step 3 for material RM027 and Batch Class E2E_ROH. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 7 | Select Batches for Paint | Repeat Step 3 for materials RM028 and RM029 without Batch Class. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number |  |

#### Batch Information System - Batch Analysis (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this functionality you can identify which batches are delivered to which customer and which raw material batches are used for the production of which finished product. You can adapt the selection in the Batch Information Cockpit to customer-specific requirements by creating user-specific groups. You can get additional information by using subsequent actions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Batch Information Cockpit (BMBC). | The Batch Information Cockpit screen displays. |  |
| 3 | Select Batches | On the Batch Information Cockpit screen, make the following entries.Go to the Material tab.Material :SG035 if FG041 or FG043 is maintained in Sales OrderSG036 if FG042 or FG044 is maintained in Sales OrderPlant: 3310Go to the Classification tab.Batch Class: E2E_HALBChoose Execute Selection. | One or multiple batches are displayed in the left screen area Selection Result for Batches. The standard sorting is done per material number. |  |
| 4 | Expand Selection | In the section Selection Result for Batches. Select the checkbox for the material and then choose Expand subtree or Expand node. | The selection result is analyzed and a batch for further investigation is identified. |  |
| 5 | Start Analysis | Right-click on one selected batch and choose either Usage(Top-Down) or Usage(Bottom-up). | The batch where-used list displays. |  |
| 6 | Analyze the Batch Where Used List | The usage of the batch can be analyzed and the specific documents (such as batch master record, sales order) can be accessed via double click. |  |  |
| 7 | Analyze Batch Master | Choose Details in the header area and select Batch Master. | The batch master screen displays. |  |
| 8 | Analyze Material Document | Choose Details again and select Usage.Select one document and choose Documents. | The usage displays again and after selecting documents the respective material document display. |  |
| 9 | Go to the Material Document | Choose the material document in the pop up dialog and choose Choose (F2). | The material document displays.Note that your user has to have the appropriate authorizations. |  |

#### Event-Based Production Costing - Order Costs (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This step allows you to analyze production costs in real time.

|  |
| --- |
| Note For detailed information on reports, see [here](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4032610758dc437089f0c28320eec93f/7907ffc9fef14500912e933cffa2b814.html?state=DRAFT). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Analyze Production Costs - Event-Based (F4059). | The Analyze Production Costs - Event-Based screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:From Fiscal Period : <enter period>To Fiscal Period: <enter period>Currency: AEDCompany Code: 3310 | A list of production orders displays. |  |
| 4 | Select Order Details | Select the order number and choose More Links. | The options to view more detailed information regarding the order are displayed. |  |

#### Product Profitability with Production Variances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you can analyze information such as contribution margins for individual products with related product information and profitability characteristics.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Product Profitability with Production Variances (W0182). | The Product Profitability with Production Variances screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:FSV: YPS2Ledger: 0LCompany Code: 3310Fiscal Year: <current year> | Data for all product groups that meet the selection criteria displays. |  |

### Quality Inspection during Goods Receipt from Production

#### Display Material Stock Before Quality Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, a review of the subassembly material stock is done. Due to quality inspection, the material is not available for other processing.

Prerequisite

The goods receipt from production order was posted for the subassembly material directly to quality inspection stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Stock Overview (MMBE). | The Stock Overview: Company Code/Plant/Storage Location/Batch screen displays. |  |
| 3 | Enter Material | Make the following entries and choose Run.Material: <Finished Good produced in production order above (FG041, FG042, FG043 or FG044)> | Stock for the material is displayed. |  |
| 4 | Check Stock Quantity | Check the Quality Inspection Stock under the plant 3310. |  |  |

#### Display Open Inspection Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection lot is used to record the results of the inspection operation. In this optional step, the references to the goods receipt and purchase order are verified as well as the sample size used for quality inspection reviewed.

Prerequisite

In this scope item, the inspection lot is created automatically upon goods receipt for the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Add Filter | Click on Adapt Filters on the right side and select Production Order. |  |  |
| 4 | Filter Fields | Make the following entries and choose GO.Plant: 3310Production Order: <Production Order for finished good processed in steps above> |  |  |
| 5 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot. | The Production Order number assigned with Inspection Lot is displayed.If the Production Order column does not appear, please choose the button Settings. In the View Settings dialog box, select Production Order and choose OK.Note down the inspection lot ____. |  |
| 6 | Check Inspection Lot. | In the Origin tab, verify the referenced production order and material document. | The production number and material document number from which the inspection lot originates are displayed. |  |
| 7 | Check Inspection Lot – Quantities. | Under Origin , check the sample size | The size of the sample for quality inspection is displayed. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343). | The Manage Inspection Lots screen displays. |  |
| 3 | Add Filter | Click on Adapt Filters on the right side and select Production Order. |  |  |
| 4 | Filter Fields | Make the following entries and choose GO.Plant: 3310Production Order: Production Order for finished good processed in steps above | Production Order is displayed. |  |
| 5 | Go to Edit Mode | Select the inspection lot and press Result Recording.Choose Edit. | Inspection lot can be edited. |  |
| 6 | Record result | In field Code Group – Code enter QUAL01 (OK) and press Save. | Inspection result is recorded |  |

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The quality technician executes the quality inspection and records inspection results for the inspection lot. The quality engineer makes a usage decision.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions screen displays. |  |
| 3 | Add Filter | Click on Adapt Filters on the right side and select Production Order. |  |  |
| 4 | Filter Fields | Make the following entries and choose GO.Plant: 3310Production Order: <Production Order for finished good processed in steps above> | Production Order is displayed. |  |
| 5 | Make Quick Usage Decision | Select the inspection lot and press Make Quick Usage Decision | Usage Decision is made. |  |

#### Display Material Stock after Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, we now verify the material movement done based on the usage decision codes by looking again at the material stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Stock Overview (MMBE). | The Stock Overview: Company Code/Plant/Storage Location/Batch screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Run.Material: <Material used in sales order created above (FG041, FG042, FG043 or FG044)> |  |  |
| 4 | Check Stock Quantity | Check the changed quantities of the Quality Inspection Stock, Unrestricted Use Stock (in case of positive usage decision) or Blocked Stock (in case of negative usage decision). | The stock quantities for material are updated based on the quality inspection and respective usage decision of the previous steps. |  |

### Outbound Delivery Processing

#### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a delivery.

Prerequisite

The goods receipt was posted to the individual customer’s stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: <shipping point> for example, 3310Planned Creation Date: <Delivery selection date>Sales Document: <Sales order number created previously> |  |  |
| 4 | Create Delivery | Select your sales order and choose Create Deliveries. | A delivery is triggered to be created. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Logs screen displays, delivery is created successfully with delivery number shown on tab Deliveries. |  |

|  |
| --- |
| Note With app Analyze Delivery Logs (F0870A), you can display an overview about the logs of all delivery creation in system. You can search for logs according to different filter criteria, for example: created by and additional settings. Detailed log information is listed via selecting the arrow on the right of each delivery log entry:If delivery is created successfully, delivery number is shown on tab Deliveries, else, you can display the exact message type, text and also the related sales document on tab Messages. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) | The Change Outbound Delivery screen displays. |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery screen, enter the delivery number and click Continue.From the Outbound Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control | The Outbound Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Outbound Delivery: Output screen, select the line with the Output Type Delivery_Pick_List and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point/Receiving Pt: 3310 |  |  |
| 5 | Change Outbound Deliveries | Select your delivery number, and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | Go to tab Picking and enter <quantity equal to delivery Qty> in Picked Qty field for picking related item(s). |  |  |
| 7 | Choose Enter | Choose Enter. |  |  |
| 8 | Save | Choose Save. | The delivery has been decided. |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpaddisplays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Make the following entry and choose Execute:Shipping Point/Receiving Pt: 3310 |  |  |
| 4 | Post Goods Issue | Select your outbound delivery note, and choose Post Goods Issue.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted. |  |

Financial Posting

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Inv Chg COGS w/CE | 13400000Inventory FinishedGd | none |

|  |
| --- |
| Note When the bundling functionality in context of IFRS15 is tested, the financial document in IFRS ledger (Ledger Group 2L) with the adjusted revenue amount displays.To check the financial document, use the Warehouse Clerk role, and access the Display Material Document List - Deprecated (MB51) app. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Issue Delivery Output | In the Outbound Delivery field, enter <Outbound Delivery Number>, and choose Continue.On the Outbound Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Outbound Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Outbound Delivery: Output screen, select the line with the Output Type Delivery Note, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

### Accounts Receivable

#### Change Sales Orders (Remove Billing Block)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove a billing block from a sales order.

Prerequisite

COGS has been recognized. To recognize revenue in the same month to keep FI and PA in synch, the billing block must be removed manually to process the final invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Enter search term(s) in filter bar, and choose Go:Sales Order: <Sales Order Number> | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Select sales order number and choose Change Sales Order - VA02. | Sales order is displayed in result list. |  |
| 5 | Choose Billing Plan | Select the line item. From the menu, choose Menu > Goto > Item > Billing Plan .Note Alternatively, If you assign billing plan on header level: Choose Menu > Goto > Header > Billing Plan . Removal of billing block on header level also unlocks items automatically. | The Change Standard Order xxx: Item Data screen displays. |  |
| 6 | Delete Billing Block | In the Dates section, in the Block column, delete the billing block for the Final Invoice item. |  |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Save | Save your entries. | The billing block is removed. |  |

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle the billing.

Create Billing Document

Table 2: Overview

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings, you can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for billing due list | In the search condition, use criteria if necessary. | Sales document(s) display in the result. |  |
| 5 | Select item(s) for billing | Select row(s) of SD Document created previously and choose button Create Billing Documents. | The Create Billing Documents pop up displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then press button OK. | The draft billing document with TMP xxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save.The draft version billing document with TMPxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

#### Post Incoming Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the incoming payments from the customer. For a payment of an invoice where a down payment is applied, the incoming payment amount should be the remainder invoice balance (the remainder invoice balance is the invoice value less the down payment to be applied).

|  |
| --- |
| Note If you want to link a down payment to a particular invoice, use the Clear Incoming Payments - Manual Clearing (F0773) app. Select the down payment and invoice, then assign the invoice. Enter the down payment amount in the Allocated amount field and post a partial payment on the invoice with the invoice reference (REBZG). The counter-posting line is a clearing of the down payment. This step clears the down payment on the alternative reconciliation account and posts a new partial payment line item with the invoice reference on the normal reconciliation account. Use the procedure below to post the incoming payment for the remaining amount. |

Prerequisites

Invoices are posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Incoming Payments (F1345). | The Post Incoming Payments screen displays. |  |
| 3 | Enter General Information | Make the following entries in the General Information area:Company Code : 3310Posting date : <current date>Journal Entry date : <current date>Value date : <current date>Journal Entry Type : DZ (Customer Payment) |  |  |
| 4 | Enter Bank Data | Make the following entries in the Bank data area.G/L Account: 11001060House Bank/Account ID : AEBK1/AEAC1Amount : <customer invoice amount>Note If the incoming payment is part of a down payment, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Currency : AED |  |  |
| 5 | Enter Open Items | Make the following entries:Customer Account : 33100001Choose the Propose Items button. | The open items are displayed in the bottom half of the view. |  |
| 6 | Clear Items | Choose Items to Clear by choosing the Clear button in last item column. | The selected item is transferred to view Items to be Cleared. |  |
| 7 | Down Payment | Note Only execute this step if the payment is for an invoice where a down payment is applied.In the Items to Be Cleared column, Allocated Amount, enter the remainder invoice balance amount, which is the invoice value less the down payment amount to be applied.Choose Enter. | The balance is zero and the document can be posted. |  |
| 8 | Post Entries | Choose Post button. | The Activated dialog box displays details of document number generated. |  |
| 9 | Post on Account | Repeat steps 1–4. |  |  |
| 10 | Enter Data | Choose Post on account and enter the following:Account Type: CustomerCustomer: 33100001Credit Amount: <same amount as in step 4> |  |  |
| 11 | Save | Choose Post. | Document is posted. |  |

### Accounts Payable

#### Create Supplier Invoice with PO/GR relation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation. You have two options to create the supplier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) . | The Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system , make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency : AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party: 33300001For now, if you move the mouse to the Invoicing Party in the header of the supplier invoice, then click the Invoicing Party, the Company Date with Address and Contact Details are displayed.In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency : AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx> (reference invoice number from invoicing party)Invoice Party: 33300001Select See More at header area, make the following entries.Exchange Rate: <XXX> | The Supplier Invoice screen is displayed.The Exchange Rate should be changed from USD to EUR according to the customizing settings. The Exchange Rate is changeable |  |
| 4 | Enter Purchase Order References | In Purchasing Document References section, add the references.Make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Add Notes (Optional) | Enter notes on Note tab, if you want to add more detailed long text for the supplier invoice. |  |  |
| 6 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 7 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 8 | Check Tax Date(Optional) | In case the time dependent tax is activated, in the section Tax, the Tax Date indicates the tax calculation date according to the tax rates settings in the prerequisites.Make the following entries.Tax Reporting Date: <Today>Tax Date: <Today>Note The Tax Date is the key date for calculating tax, please maintain it carefully according to your financial business requirements. |  |  |
| 9 | Check Tax code | In the section Tax, check if there is tax code information and enter the tax amount when the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the itemsIf there is no tax, specify the tax code V0. |  |
| 10 | Block invoice on item level (optional) | Choose the invoice item arrow on the right side of the item to navigate to the item details.On the next screen, set flag for Manually Blocked. Click Check and on the lower part of the details screen, the Blocking Reasons section shows the text Manual. Click Back to Supplier Invoice | The item is blocked with a blocking reason. |  |
| 11 | Check the balance | Calculate the tax choosing Propose Tax. Check the balance (diﬀerence between the calculated amount and the gross Amount you entered step 3). | The balance should be zero (or within the defined tolerance). |  |
| 12 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation Details area. | The supplier Invoice is complete to post. |  |
| 13 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

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

Prerequisite

Review the house bank assignment to G/L account before you start the test so that you can use the proper G/L account in step 3 General Information in the Procedure section below.

To review, select the house bank and company code to test and use the Manage Bank Accounts (F1366A)app. In the app go to House Bank Account Connectivity House Bank Account DataG/L Account Data

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Outgoing Payments (F1612). | The Post Outgoing Payments screen displays |  |
| 3 | General Information | Make the following entries.General Information sectionCompany Code: 3310Posting Date: <Today's date>Journal Entry Date: <Today's date>Value Date: <Today's date>Reference (optional): <your reference>Journal Entry Type: KZHeader Text: <header text>Bank Data sectionG/L Account: 11001000(see Prerequisites above)House Bank / Account: AEBK1/AEAC1Note For invoices in USD, use account USDAC.Amount / Currency: amount to pay on existing invoice for example, 119,00 AEDFees: OptionalAssignment: OptionalExchange Rate: OptionalCurrency:Optional |  |  |
| 4 | Open Item Selection | In the Open Items Selection section, make the following entries:Account Type/Account ID: Supplier/33300001.Click on Show Items button. | A list of open items is displayed in the Open Items section. |  |
| 5 | Select/Deselect | Select an item to pay in the Open AP/AR Items table and in the Clear column section, choose Clear.Allocated Amount: Invoice amount less the down payment amountand choose Enter | The item to pay transfers to the Items to be Cleared section. |  |
| 6 | Post | Choose Post.Note The generated payment doesn't require approval | Journal entry xxxxxxxxxx posted |  |
| 7 | Display | To view the posted document, choose Display. | The posted document is displayed . |  |
| 8 | Back | Choose the Back button. | Journal entry has already been posted. You can now post a new payment. |  |
| 9 | Dismiss notification | Choose OK to dismiss notification. |  |  |

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
- related-to :: [[12-production-and-manufacturing/test-script-make-to-order-production-finished-goods-sales-and-final-as]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-order-production-process-manufacturing-3ok-ae-966]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DW_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 154,234 chars in the whole document
