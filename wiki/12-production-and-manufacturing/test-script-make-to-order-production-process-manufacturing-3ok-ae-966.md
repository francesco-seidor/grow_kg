---
id: 12-production-and-manufacturing/test-script-make-to-order-production-process-manufacturing-3ok-ae-966
title: "Test Script: Make-to-Order Production – Process Manufacturing (3OK_AE) (3OK_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 3OK: make-to-order process manufacturing from sales order/quotation through MRP, process order, delivery and billing."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/make-to-order-production]
aliases: [3OK_S4CLD2608_BPD_EN_AE]
keywords: [Make-to-Order Production, process manufacturing, sales order processing, sales quotations, material requirements planning, process order processing, goods issue, process order confirmation, delivery processing, billing documents]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3OK_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-966
topic: 12-production-and-manufacturing/make-to-order-production
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Make-to-Order Production – Process Manufacturing (3OK_AE) (3OK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3OK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Make-to-Order Production** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Make-to-Order Production – Process Manufacturing (3OK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853499)

[2 Prerequisites 4](#_Toc232853500)

[2.1 System Access 4](#_Toc232853501)

[2.2 Roles 4](#_Toc232853502)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232853503)

[2.4 Business Conditions 7](#_Toc232853504)

[2.5 Preliminary Steps 7](#_Toc232853505)

[2.5.1 Initial Stock Posting 7](#_Toc232853506)

[3 Overview Table 9](#_Toc232853507)

[4 Test Procedures 11](#_Toc232853508)

[4.1 Sales Order Processing 11](#_Toc232853509)

[4.1.1 Option 1: Create Sales Order Directly 11](#_Toc232853510)

[4.1.2 Option 2: Create Sales Order including Quotation Processing 13](#_Toc232853511)

[4.1.2.1 Create Sales Quotation 13](#_Toc232853512)

[4.1.2.2 Create Sales Orders with Ref. to Quotation 14](#_Toc232853513)

[4.2 Production Planning 15](#_Toc232853514)

[4.2.1 Material Requirements Planning 15](#_Toc232853515)

[4.2.2 Monitor Material Coverage 17](#_Toc232853516)

[4.3 Process Order Processing 18](#_Toc232853517)

[4.3.1 Create Process Order 18](#_Toc232853518)

[4.3.2 Review Process Order 19](#_Toc232853519)

[4.3.3 Preview Output Document for Process Order 20](#_Toc232853520)

[4.3.4 Goods Issue of Batch-Managed Components 21](#_Toc232853521)

[4.3.4.1 Goods Issue via Pick List 21](#_Toc232853522)

[4.3.4.2 Manual Goods Issue (Instead of Picking List) 23](#_Toc232853523)

[4.3.5 Monitor Order Progress 24](#_Toc232853524)

[4.3.6 Confirm Process Order 25](#_Toc232853525)

[4.3.7 Post Goods Receipt for Process Order 26](#_Toc232853526)

[4.4 Delivery Processing 27](#_Toc232853527)

[4.4.1 Create Delivery with Order Reference 27](#_Toc232853528)

[4.4.2 Execute Picking 28](#_Toc232853529)

[4.4.3 Post Goods Issue 29](#_Toc232853530)

[4.5 Billing Process 30](#_Toc232853531)

[4.5.1 Create Billing Document 30](#_Toc232853532)

[5 Appendix 31](#_Toc232853533)

[5.1 Succeeding Processes 31](#_Toc232853534)

## Purpose

Overview

The standard sales process (make-to-order) for batch-managed finished goods starts with a customer quotation or sales order and ends with the clearing of a customer account after a payment is received.

The process starts with the creation of a quotation and then a sales order that references it, or by creating a sales order directly.

The production process based on process orders is triggered by a material requirement planning (MRP) run for the product ordered by the customer and all its components. Once the finished product with a batch is in stock, the delivery and billing of the goods completes the process.

The process can be enhanced by executing optional steps, such as procurement of components or period-end closing.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

Manufacturing

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG6200 | FIN6200, MTO-PI, PD, Batch |  |
| Material | SG6100 | SEMI6100, PI, PD, Batch |  |
| Material | RM15 | RAW15,PD |  |
| Material | SG23 | SEMI23,PD,Subcontracting |  |
| Material | RM128 | RAW128,PD,Consignment |  |
| Plant | 3310 | Plant 1 AE |  |
| Customer | 33100001 | Domestic UAE Customer 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |

Bill of Materials Structure

This overview shows the bill of materials structure and the usage of each component.

| Material | Level | Material Type | Base quantity | Unit | Material description |
| --- | --- | --- | --- | --- | --- |
| FG6200 | 0 | FERT | 100 | KG | FIN6200, MTO-PI, PD, Batch |
| SG6100 | 1 | SEMI | 100 | KG | SEMI6100, PI, PD, Batch |
| RM09 | 2 | RAW | 100 | KG | FIN29,MTS-PI,PD,Batch-ExpirationDate |
| RM1420 | 2 | RAW | 500 | L | RM1420, PD, Solvent |
| RM1430 | 2 | RAW | 100 | KG | RM1430, PD, Catalyst |
| RM15 | 1 | RAW | 10 | PC | RAW15,PD |
| SG23 | 1 | SEMI | 10 | PC | SEMI23,PD,Subcontracting |
| RM128 | 1 | RAW | 10 | PC | RAW128,PD,Consignment |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| 3X8 | Create Resource - MDS |
| 3X9 | Create Master Recipe - MDS |
| BLD | Create Production Version - MDS |
| 2ZW | Create Batch Management Master Data - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the BEG test script |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the BNZ test script. Posting Period is up-to-date. |

### Preliminary Steps

#### Initial Stock Posting

Purpose

Initial stock posting is not required if you want to play through complete procurement or semifinished component production processes for selected materials in the BOM of FG6200.

- For semifinished material SG23, you can post initial stock. Alternatively, you can run the scope item BMY to produce the demand for the semifinished SG23 via Subcontracting.
- For semifinished material SG6100, you can post initial stock. Alternatively, you can run relevant production process.
- For the remaining raw materials the BOM structure, you can post initial stock. Alternatively, you can run the procurement scope items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | Screen name adapts according to entries. |  |
| 3 | Choose Goods Receipt-Other | Make the following entries and choose Enter.Trans./Event: Goods ReceiptReference Document: OtherMovement Type: 561 | Screen name adapts after entries are made. |  |
| 4 | Specify Material | On the Material tab, make the following entries:Material: RM15 | Ensure that detail data is expanded. |  |
| 5 | Specify Quantity | On the Quantity tab, make the following entries:Qty in Unit of Entry: 1000 |  |  |
| 6 | Specify Plant and Storage Location | On the Where tab, make the following entries:Plant: 3310Storage location: 331B |  |  |
| 7 | Check Item | Press Enter, and ensure Item OK is selected. |  |  |
| 8 | Add Other Materials | Choose Next Item, then repeat the steps 4 to 7 for the following materials:Material: RM128Material: SG6100Material: SG23 |  |  |
| 9 | Post Goods Movement | Choose Post. | Material document XXX posted.Materials are available in stock. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Sales Order Processing |  |  |  |
| [Option 1: Create Sales Order Directly](#unique_9) [page ] 11 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales Order is created. |
| Option 2: Create Sales Order including Quotation Processing |  |  |  |
| [Create Sales Quotation](#unique_10) [page ] 13 | Internal Sales Representative | Manage Sales Quotations (F1852) | Sales Quotation is created. |
| [Create Sales Orders with Ref. to Quotation](#unique_11) [page ] 14 | Internal Sales Representative | Manage Sales Orders (F1873) | Sales Order is created. |
| Production Planning |  |  |  |
| [Material Requirements Planning](#unique_12) [page ] 15 | Production Planner | Schedule MRP Runs (F1339) |  |
| [Monitor Material Coverage](#unique_13) [page ] 17 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Generate Planned Order is checked. |
| Process Order Processing |  |  |  |
| [Create Process Order](#unique_14) [page ] 18 | Production Planner | Convert Planned Orders - to Process Orders (COR8) | Process Order is created for Sales Order, to produce the finished goods. |
| [Review Process Order](#unique_15) [page ] 19 | Production Supervisor - Process Manufacturing | Display Process Order (COR3) | Process Order is reviewed. |
| [Preview Output Document for Process Order](#unique_16) [page ] 20 | Production Supervisor - Process Manufacturing | Display Process Order (COR3) |  |
| Goods Issue of Batch-Managed Components |  |  |  |
| [Goods Issue via Pick List](#unique_17) [page ] 21 | Production Operator - Process Manufacturing | Pick Components for Process Orders (COIK) | Components for Process Order is picked. |
| [Manual Goods Issue (Instead of Picking List)](#unique_18) [page ] 23 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods Issue is posted for the Process Order. |
| [Monitor Order Progress](#unique_19) [page ] 24 | Production Supervisor - Process Manufacturing | Monitor Order Progress (CO46) |  |
| [Confirm Process Order](#unique_20) [page ] 25 | Production Operator - Process Manufacturing | Confirm Process Order Phase (COR6N) | Final confirmation is carried out. |
| [Post Goods Receipt for Process Order](#unique_21) [page ] 26 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt for the process order is posted. |
| Delivery Processing |  |  |  |
| [Create Delivery with Order Reference](#unique_22) [page ] 27 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Outbound delivery is created for sales order. |
| [Execute Picking](#unique_23) [page ] 28 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The outbound delivery is picked. |
| [Post Goods Issue](#unique_24) [page ] 29 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods issues for delivery are posted. |
| Billing Process |  |  |  |
| [Create Billing Document](#unique_25) [page ] 30 | Billing Clerk | Create Billing Documents (F0798) | Billing document is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Sales Order Processing

Purpose

You can create Sales Order directly or with Reference to Quotation. For test purpose, you can just choose one option to create your sales order.

#### Option 1: Create Sales Order Directly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create Sales Order directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders (F1873) screen, choose Create Sales Orders - VA01 (VA01). |  |  |
| 4 | Enter the Order Type and the Sales Organization | On the Create Sales Documents screen, make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the Create Standard Order: Overview screen, make the following entries:Sold-to Party: 33100001Ship-to Party: 33100001Customer Reference: <Enter a reference number>Req. Deliv. Date: <Delivery Date> (Today plus 1 month)Material Number: FG6200Order Quantity: <Quantity> (For example, 100 KG) |  |  |
| 6 | ATP Check | If the Standard Order: Availability Control screen displays:Check the Dely/Conf.Date and Confirmed qty in Dely proposal. Make a note of the Delivery Date.Choose Complete dlv.. |  |  |
| 7 | Save Document | Choose Save. Make a note of the sales order number. | The order is saved. |  |

|  |
| --- |
| Note If you maintain different material prices by Ledger (scope item 1ZT - Managing Material Price Changes and Inventory Values) and want to do Ledger specific sales order costing, please refer to the scope item BEG - Standard Cost Calculation and its step Appendix > Manage Order BOM Cost Estimates in Parallel Valuation. |

#### Option 2: Create Sales Order including Quotation Processing

##### Create Sales Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations (F1852) displays. |  |
| 3 | Navigate to Create Sales Quotation Screen | On the Manage Sales Quotations (F1852) screen, choose Create Quotation. | The Create Quotation: Initial screen displays. |  |
| 4 | Enter Quotation Type and Sales Organization | Make the following entries and choose Enter:Quotation Type: QTSales Organization: 3310 | The Create MTO Quotation: Overview screen displays. |  |
| 5 | Enter the Quotation Details | Make the following entries:Sold-to Party: 33100001Ship-to Party: 33100001Cust. Reference: <Enter a reference number>Cust. Reference date: <Today's Date>Req.deliv.date: <Delivery Date> (Today plus 1 month)Valid to: <A date> (Today plus 6 weeks)Material: FG6200Order Quantity: Quantity (For example: 100 KG) |  |  |
| 6 | Save | Choose Save (Ctrl+S). | Note Ignore any dialog box. |  |

##### Create Sales Orders with Ref. to Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A customer order is created based on the negotiated quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Orders (F1873) screen, choose Create Sales Orders - VA01 (VA01). |  |  |
| 4 | Enter the Order Type and the Sales Organization | Make the following entries and choose Create with Reference:Order Type: ORSales Organization: 3310 | The Create with Reference dialog box displays. |  |
| 5 | Enter the Second Quotation Number | Make the following entries and choose Copy.Quotation: <Quotation number> (The Quotation from last step) |  |  |
| 6 | Check the Delivery Date and Order Details | Check and make necessary changes for the following entries and choose Enter.Cust. Reference: <Enter a reference number>Cust. Reference Date: <Today's Date>Req. Delivery Date: <Today's Date + 1 Month> |  |  |
| 7 | Save | Choose Save. | Note If the sales order might require approval, refer to Sell from Stock (BD9) scope item, and complete the activities of Process Sales Order Approval. |  |

|  |
| --- |
| Note If you maintain different material prices by Ledger (scope item 1ZT - Managing Material Price Changes and Inventory Values) and want to do Ledger specific sales order costing, please refer to the scope item BEG - Standard Cost Calculation and its step Appendix > Manage Order BOM Cost Estimates in Parallel Valuation . |

### Production Planning

#### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to start the MRP run for the sales order you created before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG6200>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: FG6200Changed BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG6200 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Monitor Material Coverage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor the material coverage situation for the material after the requirements planning is carried out.

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net and Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Check Area of Responsibility | Choose the user icon, select App Settings > Area of Responsibility , and make sure only following values are assigned:Plant 1 AE (3310)MRP Controller 001(001)Choose AOR status button of this entry if not assigned, choose AOR status button of the corresponding entry to unassign any other entry then choose Back. |  |  |
| 5 | Select Material | In the search area, make the following entries and choose Go.Material: FG6200Individual Segment: CustSt xxxxxxxx-10 (the quotation or sales order number created by you)Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 6 | Check Planned Order | Find the generated planned order, and make a note of the number of this Planned Order.Stay in this page for following processing. | An individual Planned Order is created for the Sales Order you created before. |  |

### Process Order Processing

#### Create Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create process orders. The created process order are released automatically according to pre-defined settings. You can continue the processing after execute last step within the same app Monitor Material Coverage - Net / Individual Segments (F2101A).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner and open Monitor Material Coverage - Net / Individual Segments (F2101A).Check the planned order as indicated in last step and stay on the page. | The SAP Fiori launchpad displays. |  |
| 2 | Choose Action Convert | For the generated planned order, select Convert from the dropdown list under column Actions. |  |  |
| 3 | Convert to Process Order | In the dialog box, Convert to Process Order is selected by default. Choose Convert. | Planned orders were converted to process orders. |  |

As an alternative, you can also use some other app to covert the planned order to process order. If you already converted it through above procedure, you do not need to execute below procedure again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Convert Planned Orders - to Process Orders (COR8). | The Collective Conversion of Planned Orders: Initial screen displays. |  |
| 3 | Enter Restriction | Make the following entries and choose Execute:Production Plant: 3310Material: FG6200 | The system displays a list of all planned orders, which match the restriction. |  |
| 4 | Convert Planned Order to Process Order | Select the planned order for conversion, and then choose Convert Planned Order. | Planned orders were converted to process orders. |  |

#### Review Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review created process orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order (COR3). | The Display Process Order: Initial screen displays. |  |
| 3 | Enter Process Order Number | Make the following entries and choose Continue.Process Order: XXXX (From previous steps) | The Display Process Order: Header - General Data screen displays.On this screen, you find the order’s detailed information.Process orders are reviewed and checked within your responsibility area. |  |

#### Preview Output Document for Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to preview the output document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order (COR3). | The Display Process Order: Initial screen displays. |  |
| 3 | Enter Process Order Number | Make the following entries and choose Continue.Process Order: XXXX (From previous steps) |  |  |
| 4 | Navigate to Output Management | Select More > Process Order > Output > Manage Output Items . | The Overview Output Management: Output screen displays. |  |
| 5 | Check Output Item | On the Overview Output Management: Output screen, you could check output item lists under Output section.Typically, following 2 items should be listed with status of Completed:Output Type: PICK_LIST; Channel: PRINTOutput Type: ORDER_DATA_LIST; Channel: PRINT |  |  |
| 6 | Display PDF Document | Select the output item with Channel: PRINT, and choose Display PDF Document. | PDF document displays for the selected item. |  |

#### Goods Issue of Batch-Managed Components

Purpose

The withdrawal of the raw materials is used for the process order. This withdrawal can be done by using the picking list or doing a manual goods issue.

Prerequisites

Ensure that sufficient material is present on stock. You can check the stock levels using the app Monitor Stock / Requirements List - Old Version (MD04) available for the Production Planner role.

##### Goods Issue via Pick List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how all materials that are moved to the production storage location can be issued to the process order using the pick list when the released process order is ready for picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Process Orders (COIK). | The Picking List: Initial screen displays. |  |
| 3 | Enter Restriction and Execute | Make the following entries and then choose Execute.Profile: 000002Process Order: <XXXX> (from previous steps)Plant: 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Select the relevant reservations and choose Picking. | The Picking list screen displays. On this screen, a list of all the selected reservations displays. |  |
| 5 | Perform Batch Determination for Batch-managed Components | Select the picking lines for following batch-managed material and choose Batch Determination:Material: SG6100 | The Batch Determination MM: Select Batches screen displays.If the system shows the message Batch determination was carried out without selection specification, ignore it.If during batch determination only part of the required quantity is found to be available, the unconfirmed quantity remains as an open line item within the picking list. You should then delete the line item from the picking list before saving, as this line item cannot be posted. |  |
| 6 | Copy Batch Determination Result | Choose Copy. | The Picking list screen displays again. In addition, the batch numbers have been determined. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements are posted. |  |

##### Manual Goods Issue (Instead of Picking List)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the system performs a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then choose Enter.Trans./Event: Goods IssueReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Perform Batch Determination for Batch-managed Material | For item with batch managed material, navigate to the Quantity tab in the Detail Data section, choose Stock Determ. icon besides Qty.Material: SG6100 | The Batch Determination MM: Select Batches screen displays. |  |
| 5 | Copy Batch Determination Result | Check the required batch and choose Copy. | The Goods Issue Order XXXX screen displays. In addition, the batch numbers have been determined. |  |
| 6 | Check Each Item | For each item shown, select Item OK. | Ensure that detail data is expanded. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements have been posted. |  |

#### Monitor Order Progress

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a worklist for process orders, components and operations, with user-specific selection and layout settings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Order Progress (CO46). | The Order Progress Report: Selection screen displays. |  |
| 3 | Enter Overall Profile | Make the following entries and choose Production/Process Order tab.Overall Profile: SAP000000002 |  |  |
| 4 | Enter Process Order Number | Make the following entries and choose Execute.Production/Process Order: <XXXX> (from previous steps) | The Stock/Requirements List as of XX hrs screen displays.You can review the required lists, such as order header and components lists. |  |

#### Confirm Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of order, operations, phases and individual capacities. It is an instrument to control the order. The time ticket confirmation allows recording either the default times for machine and labour usage, or record actual times for major deviations. Backflushed materials will be posted automatically during respective phase confirmations. You can post scrap quantities as an optional. If no major deviations occurred, only the last phase (milestone) must be confirmed. Using milestone confirmation, all prior phases are confirmed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Process Order Phase (COR6N). | The Enter Time Ticket for Process Order screen displays. |  |
| 3 | Enter Confirmation Option | Make the following entries.Order: <XXXX> (from previous steps)Choose Enter or select phase (0040) from search help of Phase field.Confirm.type: Final confirmationClear open reservations: X | If the system shows the message Total quantity confirmed not equal to planned quantity to be confirmed, press Enter to ignore it. |  |
| 4 | Propose Actual Data | Choose Actual Data, make the changes for the following fields:Scrap: <Enter the amount you want to Scrap>Yield: <Based on the origin quantities minus Scrap>Reason for Var: <Enter scarp reason if need>, for example, 0001 | The Quantities and Activities will be filed automatically. You can make necessary change. |  |
| 5 | Choose Goods Movements | Choose Goods Movements. | The Enter Confirmation for Production Order: Goods Movement screen displays. RM15 should be listed here, check the material entries and quantities. |  |
| 6 | Save Confirmation | Choose the Back icon to navigate to the Enter Time Ticket for Process Order screen. Choose Save. | Backflushed component RM15 is issued with the confirmation posting automatically.The final confirmation of the last operation is carried out. Costs and activity quantities are recalculated in proportion to the yield quantity. |  |

#### Post Goods Receipt for Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the process order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then press Enter.Trans./Event: Goods ReceiptReference Document: OrderOrder Number: <XXXX> (from previous steps)Movement Type: 101 | Screen name adapts after entries are made. |  |
| 4 | Check Product | Check the products listed in the table.Choose the Where tab, make the following entries, and press Enter:Storage Location: 331A |  |  |
| 5 | Check Item | Select Item OK for each line. | Ensure that detail data is expanded. |  |
| 6 | Check | Choose Check in the lower right corner. | The batch number is created automatically. |  |
| 7 | Post Goods Movement | Choose Post. | The goods movements for produced product are posted. |  |

### Delivery Processing

#### Create Delivery with Order Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create delivery to customer.

Procedure

To execute this activity, process the following steps using the master data from this document (see also the following table). When you search sales order, kindly input proper date range for "Planned Creation Date" or just remove value for this filter.

| Steps |
| --- |
| Create Delivery (BD9) |

| Master Data | Sample Value |
| --- | --- |
| Shipping Point | 3310 |
| Sales Order | <Sales Order Number> |

Result

You successfully created the delivery for the sales order.

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to take goods from a storage location and stage the right quantity in a picking area where the goods are prepared for shipping.

Procedure

To execute this activity, process the following steps using the master data from this document (see also the following table). When you search outbound deliveries, please kindly input proper Time Data. If you follow this test script when creating Sales Order, here you can input the "Picking Date" from current day to current day plus one month, in order to successfully find your outbound delivery.

| Steps |
| --- |
| Execute Picking (BD9) |

| Master Data | Sample Value |
| --- | --- |
| Shipping Point | 3310 |
| Delivery | <Delivery Number> |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issue for the delivery.

Procedure

To execute this activity, process the following steps using the master data from this document (see also the following table). When you search outbound deliveries for Goods Issue, kindly input proper Time Data. If you follow this test script when creating Sales Order, here you can input the "Pland Gds Mvmnt Date" from current day to current day plus one month, in order to successfully find your outbound delivery.

| Steps |
| --- |
| Post Goods Issue for Delivery (BD9) |

| Master Data | Sample Value |
| --- | --- |
| Shipping Point | 3310 |
| Delivery | <Delivery Number> |

### Billing Process

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to bill the customer.

Procedure

To execute this activity, process the following steps using the master/transaction data from this document:

| Steps |
| --- |
| Create Billing Document (BD9) |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | These activities are executed for accounts receivables handling. For more information about the month-end closing procedure, see the J59 Test Script. |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

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
- related-to :: [[12-production-and-manufacturing/test-script-lot-size-of-one-based-on-make-to-order-7dw-ae-sap-s-4hana]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-order-production-finished-goods-sales-and-final-as]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3OK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 47,890 chars in the whole document
