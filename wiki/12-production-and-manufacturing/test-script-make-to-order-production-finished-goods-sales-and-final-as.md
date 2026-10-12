---
id: 12-production-and-manufacturing/test-script-make-to-order-production-finished-goods-sales-and-final-as
title: "Test Script: Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE_AE) (BJE_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item BJE: make-to-order quotation, sales order, MRP, production, delivery and billing steps."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/make-to-order-production]
aliases: [BJE_S4CLD2608_BPD_EN_AE]
keywords: [Make-to-Order Production, sales quotation, sales order processing, order bom, material requirements planning, production orders, production confirmation, goods receipt, delivery processing, billing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJE_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1272
topic: 12-production-and-manufacturing/make-to-order-production
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE_AE) (BJE_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJE_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Make-to-Order Production** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861798)

[2 Prerequisites 4](#_Toc232861799)

[2.1 System Access 4](#_Toc232861800)

[2.2 Roles 4](#_Toc232861801)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861802)

[2.4 Business Conditions 8](#_Toc232861803)

[2.5 Preliminary Steps 8](#_Toc232861804)

[2.5.1 Initial Stock Posting for the Material in BoM 8](#_Toc232861805)

[2.5.2 Create Master Data for Material FG227 (Optional) 10](#_Toc232861806)

[3 Overview Table 11](#_Toc232861807)

[4 Test Procedures 13](#_Toc232861808)

[4.1 MTO Sales Processing (Material w/o Sales Order BoM) 13](#_Toc232861809)

[4.1.1 Receive Customer Request for Quotation 13](#_Toc232861810)

[4.1.2 Create and Send Sales Quotation to Customer 13](#_Toc232861811)

[4.1.3 Change Sales Quotation 15](#_Toc232861812)

[4.1.4 Create Sales Order with Ref. to Quotation 16](#_Toc232861813)

[4.2 MTO Sales Processing (Material with Sales Order BoM) (Optional) 19](#_Toc232861814)

[4.2.1 Create Sales Order 19](#_Toc232861815)

[4.3 Down Payment Processing 22](#_Toc232861816)

[4.3.1 Create Down Payment Request 22](#_Toc232861817)

[4.3.2 Post Down Payment 22](#_Toc232861818)

[4.4 Production Planning 22](#_Toc232861819)

[4.4.1 Material Requirements Planning for Sales Order 22](#_Toc232861820)

[4.5 Process Technical Change BoM in Sales Order (Optional) 24](#_Toc232861821)

[4.5.1 Change Order BoM for Sales Order 24](#_Toc232861822)

[4.5.2 Recalculation of Costs in Sales Order 25](#_Toc232861823)

[4.5.3 Rerun MRP for Sales Order 27](#_Toc232861824)

[4.6 Production Processing 29](#_Toc232861825)

[4.6.1 Create Production Order 29](#_Toc232861826)

[4.6.2 Review Order Progress 31](#_Toc232861827)

[4.6.3 Release Production Orders 32](#_Toc232861828)

[4.6.4 Pick Components (Picking List) 33](#_Toc232861829)

[4.6.5 Confirm Assembly Activities 35](#_Toc232861830)

[4.6.6 Post Goods Receipt for Production Order 36](#_Toc232861831)

[4.7 Delivery Processing 37](#_Toc232861832)

[4.7.1 Create Delivery with Order Reference 37](#_Toc232861833)

[4.7.2 Execute Picking 38](#_Toc232861834)

[4.7.3 Post Goods Issue 38](#_Toc232861835)

[4.8 Billing Process 38](#_Toc232861836)

[4.8.1 Change Sales Orders (Remove Billing Block) 39](#_Toc232861837)

[4.8.2 Billing 39](#_Toc232861838)

[4.9 Review Manufacturing Object Pages 39](#_Toc232861839)

[5 Appendix 41](#_Toc232861840)

[5.1 Process Integration 41](#_Toc232861841)

[5.2 Succeeding Processes 41](#_Toc232861842)

[5.3 Additional Functional Information 41](#_Toc232861843)

## Purpose

Overview

The Make-to-Order process starts with a customer quotation and ends with the clearing of a customer account after a payment is received.

The process starts with the creation of a quote that includes a price and lead time estimate. Once the customer accepts the quote, a sales order is created that references the quote. The billing plan containing multiple customer payments (including down payment) may be set up in the order.

The production process is triggered by a material requirement planning (MRP) run for the finished product and BoM components. Once the finished product is manufactured (and confirmations entered and components issued) and received into stock, the delivery and final billing occurs.

Optionally, you can set up an order BoM that contains the components required for the customer’s specific requirements. A cost estimate can be generated based on an order-specific BoM.

Components can be preplanned using the Semi-finished Goods Planning and Assembly (1BM) scope item.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| System | Access using the SAP Fiori® Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| BOM Engineer - Customer Order | SAP_BR_BOM_ENG_CUST_ORDER | Bills of Material - Customer Orders | SAP_BR_BOM_ENG_CUST_ORDER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG228 | FIN228, MTO, PD, Fifo | Material FG228 adopts Strategy Group B6 (Planning w/o final assy – MTO w/o costing) in material master - MRP3 view. |
| Material | FG227 | FIN227, MTO, PD | To test order BOM management process, you can use FG227.Material FG227 adopts Strategy Group S5 (Planning w/o final assy – MTO w/o costing) in material master - MRP3 view. |
| Material | SG21 | SEMI21,PD,RepetitiveManuf. |  |
| Material | SG22 | SEMI22,PD,Phantom |  |
| Material | SG25 | SEMI25,PD,ExternalProcurement |  |
| Material | SG23 | SEMI23,PD,Subcontracting |  |
| Material | RM13 | RAW13,PD,Subcontracting |  |
| Material | RM14 | RAW14,PD,Subcontracting |  |
| Material | SG224 | SEMI224,MTO,PD,Subassembly |  |
| Material | RM16 | RAW16,PD |  |
| Material | RM20 | RAW20,PD |  |
| Material | RM27 | RAW27,PD,PackagingBox |  |
| Material | RM122 | RAW122,PD,Batch-Fifo,ProcureImport |  |
| Material | RM124 | RAW124,VB,Consumption,FixedBin |  |
| Material | RM128 | RAW128,PD,Consignment |  |
| Customer | 33100001 | Domestic UAE Customer 1 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

Bill of Material Structure for SG224

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristic of Material |
| --- | --- | --- | --- | --- |
| SG224 | 0 | SEMI | PC | Semifinished Good Repetitive Manuf. |
| RM124 | 1 | RAW | PC | Raw Material |

Bill of Material for FG228 and FG227

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristic of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| FG228 | 0 | FERT | PC | Finished Good for MT0 processing |  |
| FG227 | 0 | FERT | PC | Finished Good for MT0 processing |  |
| SG22 | 1 | SEMI | PC | SF, Phantom Assembly | Initial Stock Posting |
| RM16 | 2 | RAW | PC | External procured | Initial Stock Posting |
| RM122 | 1 | RAW | PC | External procured with Batch Management (FIFO-Strategy) | Initial Stock Posting |
| RM128 | 1 | RAW | PC | External procured with Consignment Processing | Initial Stock Posting |
| SG25 | 1 | SEMI | PC | SF Ext. Procurement | Initial Stock Posting |
| SG224 | 1 | SEMI | PC | Internal production of subassembly (MTO strategy) |  |
| RM27 | 1 | RAW | PC | External procured, Packaging Box | Initial Stock Posting |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BND | Create Customer Master - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |
| 2ZW | Create Batch Management Master Data - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNU - Create Costing Run - MDS | You have completed the steps described in the master data script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the steps described in the master data script. Posting Period is up-to-date. |

### Preliminary Steps

#### Initial Stock Posting for the Material in BoM

|  |
| --- |
| Note Initial stock posting is not required if you want to execute complete procurement or semifinished component production processes for selected materials in the multilevel BoM of FG228 and FG227.For the semifinished material SG224, you can either post initial stock here, or run through Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM) scope item first to produce enough stock before creating sales orders for finished goods.For the semifinished material SG21, you can either post initial stock here, or run through Make-to-Stock Production – Repetitive Manufacturing (BJH) scope item to produce enough stock via repetitive manufacturing process.For the remaining semifinished and raw materials in the multilevel BoM of FG228 or FG227 you can post initial stock. |

Purpose

This process step shows you how to post initial stock for BoM materials of FG228 and FG227.

|  |
| --- |
| Note Alternatively, you can run the procurement scope items. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) | The Goods Receipt Other - XXX (your user name) screen displays. |  |
| 3 | Enter Details | Make the following entries:Trans./Event: Goods ReceiptReference Document: OtherIn the Detail Data section, make the following entries and press Enter. Select Next Item icon to add entries.On the Where tab:Goods Movement Type: 561 (Init.entry of stBal.)Plant: 3310Storage Location: 331BOn the Quantity tab:Quantity: <Quantity>, for example, <100>On the Material tab:Material: <BOM Material>, see the Bill of Material Structure for FG228 and FG227 in the Master Data, Organizational Data, and Other Data section for a detailed materials list.Run through Make-to-Order Production – Semifinished Goods Planning and Assembly (1BM) test script if you do not want to post initial stock for SG224.Select Item OK, and choose Check. | A message displays: The Document is OK. You also post initial stock for material RM20 in case you test with material FG227. |  |
| 4 | Post | Confirm the message that the batch has been created and choose Post. | A message displays: Material document XXXXXXXX posted. |  |

#### Create Master Data for Material FG227 (Optional)

Material FG227 is used to test the order BoM change process in the Post Down Payment section. Therefore you create master data for material FG227 before testing.

Follow below master data script to create relevant master data for material FG227.

| Master Data ID | Description | Comment |
| --- | --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS | You can copy from material FG228 which is available in system.Note In MRP 3 view, strategy group for material FG227 should be S5. |
| BNK | Create Material BOM for Production and Sales - MDS | Create a production BOM for material FG227 with reference to BOM of FG228. |
| BNL | Create Routing - MDS | Create routing for material FG227 with reference to group ID 43310046 and group counter 1. |
| BLD | Create Production Version - MDS | Create production version for material FG227. |
| BET | Create Sales Pricing Condition - MDS | Create pricing condition for material FG227. Refer to FG228. |

Use Below organization data when you create master data.

| Master | Value | Details |
| --- | --- | --- |
| Plant | 3310 | Plant 1 AE |
| Storage Location | 331A | Std. storage 1 |
| Shipping Point | 3310 | Shipping Point 3310 |
| Sales Organization | 3310 | Dom. Sales Org |
| Distribution Channel | 10 | Direct Sales |
| Division | 00 | Product Division 00 |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [MTO Sales Processing (Material w/o Sales Order BoM)](#unique_10) [page ] 13 |  |  |  |
| [Receive Customer Request for Quotation](#unique_11) [page ] 13 |  |  |  |
| [Create and Send Sales Quotation to Customer](#unique_12) [page ] 13 | Internal Sales Representative | Manage Sales Quotations (F1852) |  |
| [Change Sales Quotation](#unique_13) [page ] 15 | Internal Sales Representative | Manage Sales Quotations (F1852) |  |
| [Create Sales Order with Ref. to Quotation](#unique_14) [page ] 16 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| MTO Sales Processing (Material with Sales Order BoM) (Optional) |  |  |  |
| [Create Sales Order](#unique_15) [page ] 19 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| Down Payment Processing |  |  |  |
| [Create Down Payment Request](#unique_16) [page ] 22 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Post Down Payment](#unique_17) [page ] 22 | Accounts Receivable Accountant | Post Incoming Payments (F1345) |  |
| Production Planning |  |  |  |
| [Material Requirements Planning for Sales Order](#unique_18) [page ] 22 | Production Planner | Monitor External Requirements (F0246A) |  |
| [Process Technical Change BoM in Sales Order (Optional)](#unique_19) [page ] 24 |  |  |  |
| [Change Order BoM for Sales Order](#unique_20) [page ] 24 | BOM Engineer - Customer Order | Maintain Bill Of Material - Create, change & display BOMs (F1813) |  |
| [Recalculation of Costs in Sales Order](#unique_21) [page ] 25 | Internal Sales Representative | Change Sales Orders - VA02 (VA02) |  |
| [Rerun MRP for Sales Order](#unique_22) [page ] 27 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| Production Processing |  |  |  |
| [Create Production Order](#unique_23) [page ] 29 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| [Review Order Progress](#unique_24) [page ] 31 | Production Planner | Review Order Progress - Multilevel View (F7681) |  |
| [Release Production Orders](#unique_25) [page ] 32 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) |  |
| [Pick Components (Picking List)](#unique_26) [page ] 33 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) |  |
| [Confirm Assembly Activities](#unique_27) [page ] 35 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) |  |
| [Post Goods Receipt for Production Order](#unique_28) [page ] 36 | Warehouse Clerk | Post Goods Receipt for Production Order (F3110) |  |
| Delivery Processing |  |  |  |
| [Create Delivery with Order Reference](#unique_29) [page ] 37 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Execute Picking](#unique_30) [page ] 38 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Post Goods Issue](#unique_31) [page ] 38 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Billing Process](#unique_32) [page ] 38 |  |  |  |
| [Change Sales Orders (Remove Billing Block)](#unique_33) [page ] 39 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Billing](#unique_34) [page ] 39 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Review Manufacturing Object Pages](#unique_35) [page ] 39 | Any role for production listed in the Roles chapter | Search function |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### MTO Sales Processing (Material w/o Sales Order BoM)

Prerequisite

Forecast for finished product is planned.

#### Receive Customer Request for Quotation

Purpose

A customer sends us a specification document (Customer_Specification_EN_<Country/Region>.DOCX) and asks us to create a quotation based on the specification. The customer specification document is assigned in a later step to the quotation.

You can download the document via the following link: [Customer specification](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/Others/Customer_Specification_EN_DE.docx)

Result

You, as a manufacturer, must create a sales quotation based on the specification received from the customer.

#### Create and Send Sales Quotation to Customer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As a manufacturer, you have received a customer request for a make-to-order sales quotation in form of a customer specification document. The specification document from the customer consists of detailed requirements that the product should fulfill to meet the customer’s expectations. This process step shows you how to create a sales quotation and send it to the customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). |  |  |
| 3 | Create Sales Quotation | On the Manage Sales Quotations (F1852) screen, choose Create Quotation.Make the following entries and press Enter:Quotation Type: QTSales Organization: 3310Distribution Channel: 10Division: 00 | The Create Quotation: Overview screen displays. |  |
| 4 | Enter the Quotation Details | Make the following entries:Sold - to Party: 33100001Ship - to Party: 33100001Cust. Reference: <PO Number>Cust. Ref. Date: <Today's Date>Req. Deliv. Date: <Today plus 1 month>Valid to: <Today plus 6 weeks>In the All Items table, create an entry with the following data:Material: FG228Order Quantity: <Quantity>, for example: <10>Choose Save (Ctrl+S). | A message displays: Message Quotation XXXXXXXX has been saved.The order is saved and the quotation is sent to the printer.Note Ignore any dialog box. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations screen displays. |  |
| 3 | Search for Sales Quotation | Use filter bar to search for the created sales quotation.Enter <sales quotation number> in the Sales Quotation field. | Searched sales quotation displays. |  |
| 4 | Display Quotation Print Preview | Choose sales quotation number and choose Display Sales Quotations - VA23.On the Display Sales Quotations - VA23 screen, choose Menu > Extras > Output > Header > Edit . Select the sales quotation line item and choose Display PDF Document. | Preview for PDF document displays. |  |

Result

A sales quotation is created and sent to the customer.

#### Change Sales Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you have set the quotation to customer, the customer sends a specification document and requests a commercial change(discount). Therefore, you change the quotation and sent to the customer. A file of the specification document is attached to sales quotation as well. This process step shows you how to change sales quotation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Quotations (F1852). | The Manage Sales Quotations screen displays. |  |
| 3 | Search for Sales Quotation | Use filter bar to search for the created sales quotation.Enter <sales quotation number> in the Sales Quotation field. | Searched sales quotation displays. |  |
| 4 | Navigate to Sales Quotation Screen | Choose sales quotation number and choose Change Sales Quotation. | The Change Quotation XXXXXXXX: Overview screen displays. |  |
| 5 | Create Attachment for Sales Quotation | Choose Services for Object on top right corner of the screen, choose Create Attachment.In the File Upload dialog box, choose OK.Choose local path and Customer specification file you downloaded. | A message displays: The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object, choose Attachment list and Continue. | Attachment brings up on the Service: Attachment list screen. |  |
| 7 | Enter Discount Amount and Save | On the Sales tab, in the All Items table, select the line item, scroll to the right, and double click on PPR0(CnTy).On the Change Quotation XXXXXXXX: Item Data screen, choose Conditions tab.In the Pricing Element table, choose + (Insert Rows) icon to add a new entry with the following data and press Enter:CnTy: DPG4Amount: <10>Choose Save. | The Change Quotation screen displays with a message: Quotation XXXXXXXX has been saved. |  |

Result

You entered a customer discount and created an attachment for sales quotation.

#### Create Sales Order with Ref. to Quotation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the customer accepted the follow-on quotation, a customer order is created based on the negotiated quotation including a billing plan for a down payment. Finally, the order confirmation is printed and can be sent to the customer. This process step shows you how to create sales order with Ref. to quotation. If you enable BOM explosion number functionality, you can specify the BOM explosion number in sales order. And this BOM explosion number is copied to the subsequently generated receipt elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Create Sales Documents screen, choose Create, and choose Create Sales Order-VA01.Make the following entries and choose Create with Reference:Order Type: ORSales Organization: 3310In the Create with Reference dialog box, make the following entries and choose Copy.Quot.: <Sales Quotation Number Created Previously>On the Review Availability Check Result screen, choose Apply. | The Create Standard Order: Overview screen displays. |  |
| 4 | Enter Order Details | Make the following entries and press Enter.Cust. Reference: <Cust. Reference>Cust. Ref. Date: <Today's Date>On the Sales tab:Req. Deliv. Date<Today's Date + 1 Month> |  |  |
| 5 | Choose Billing Plan | On the Create Standard Order: Overview screen, in the All Items table, select the item. Choose : Menu > Goto > Item > Billing Plan .Note If the Selection Criteria - Milestones for billing plan dialog box displays, choose Cancel:. If the billing plan item existed, you can skip the step 6. |  |  |
| 6 | Enter Billing Plan Details and Save | On the Create Standard Order: Item Data screen, make the first entry (down payment) with the following data:Billing Date: <Today's Date>DtDS (Date Description): <Y009>Bill.value: <Down Payment Value to be Invoiced>, for example, <10>DCat (Date Category): <03>Press Enter.Block: Delete <Y2>Make the second entry with the following data:Billing Date: <Today's Date + 1 Month>DtDS (Date Description): <Y008>DCat (Date Category): <02>Press Enter.Choose Back icon, and choose Save.Note If the sales order requires approval, refer to Sell from Stock (BD9) scope item, and complete the Process Sales Order Approval (Optional) step.Note If down payment is not required, at least create a billing plan item with DtDS (Date Description) Y008 and Date Category 02. | A message displays: Standard Order XXXXX has been saved. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays |  |
| 3 | Search for Sales Order | Use filter bar to search for the created sales order.Enter <sales order number> in the Sales Order field. | Searched sales order displays. |  |
| 4 | Print Sales Order | Choose sales order number and choose Display Sales Order - VA03 (If it is not displayed, find it from More Links).On the Display Standard Order XXX: Overview screen, choose Menu > Extras > Output > Header > Edit .Select the line created with completed status and choose Display PDF Document.Choose Print icon to print your sales order. | Sales order is printed. |  |

|  |
| --- |
| Note If you maintain different material prices by Ledger (scope item 1ZT - Managing Material Price Changes and Inventory Values) and want to do Ledger specific sales order costing, please refer to the scope item BEG - Standard Cost Calculation and its step Appendix > Manage Order BOM Cost Estimates in Parallel Valuation . |

### MTO Sales Processing (Material with Sales Order BoM) (Optional)

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a sales order according to customer requirement. Later customer may require a technical change for the product. In this case, a sales order is created without reference to quotation. For this test, you can use sample material FG227.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders (F1873) screen, choose Create > Create Sales Order – VA01 .Make the following entries and choose Continue:Order Type: ORSales Organization: 3310 | The Create Standard Order: Overview screen displays. |  |
| 4 | Enter Order Details | Make the following entries and press Enter:Sold-to Party: 33100001Ship-to Party: 33100001Cust. Reference: <PO number>Cust. Ref. Date: <Today's Date>On the Sales tab:Req.deliv.date: <Delivery Date (Today + 1 Month)>In the All Items table:Material: FG227Order Quantity: <Quantity>, for example, 10 | The Create Standard Order: Overview screen displays. |  |
| 5 | Choose Billing Plan | On the Create Standard Order: Overview screen, in the All Items table, select the item. Choose Menu > Goto > Item > Billing Plan .Note If the Selection Criteria - Milestones for billing plan dialog box displays, choose Cancel. |  |  |
| 6 | Enter Billing Plan Details and Save | On the Create Standard Order: Item Data screen, make the first entry (down payment) with the following data:Billing Date: <Today's Date>DtDS (Date Description): <Y009>Bill.value: <Down Payment Value to be Invoiced>, for example, <10>DCat (Date Category): <03>Press Enter.Block: Delete <Y2>Make the second entry with the following data:Billing Date: <Today's Date + 1 Month>DtDS (Date Description): <Y008>DCat (Date Category): <02>Press Enter.Choose Back icon, and choose Save.Note If the sales order requires approval, refer to Sell from Stock (BD9) scope item, and complete the Process Sales Order Approval (Optional) step.After sales order is saved, you can check costing of sales order in display mode.Follow menu path Menu > Extras > Costing .On the Costing Structure session, check if the component is the same as in BoM of FG227. | A message displays: Standard Order XXXXX has been saved. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Use filter bar to search for the created sales order.Enter <sales order number> in the Sales Order field. | Searched sales order displays. |  |
| 4 | Print Sales Order | Choose sales order number and choose Display Sales Order - VA03 (If it is not displayed, find it from More Links).On the Display Standard Order XXX: Overview screen, choose Header Output Preview.Select the line created with completed status and choose Display Document.Choose Print icon to print your sales order. | Sales order is printed. |  |

|  |
| --- |
| Note If you maintain different material prices by Ledger (scope item 1ZT - Managing Material Price Changes and Inventory Values) and want to do Ledger specific sales order costing, please refer to the scope item BEG - Standard Cost Calculation and its step Appendix > Manage Order BOM Cost Estimates in Parallel Valuation . |

### Down Payment Processing

#### Create Down Payment Request

Purpose

This process step shows you how to create an invoice according to your billing plan. Finally, you print out the down payment request and sent it to your customer.

Procedure

Go to Sales Order Processing with Customer Down Payment (BKJ) test script and run Create Down Payment Request step as a Billing Clerk with master data for this test script.

#### Post Down Payment

Purpose

This process step shows you how to post the down payment received from your customer.

Procedure

Go to Sales Order Processing with Customer Down Payment (BKJ) test script and run Post a Down Payment step as an Accounts Receivable Accountant with master data for this test script.

### Production Planning

#### Material Requirements Planning for Sales Order

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
| 2 | Access the App | Open Monitor External Requirements (F0246A). | The Monitor External Requirements screen displays. |  |
| 3 | Check Default Area of Responsibility | Choose user icon and select App Settings. In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, ensure that only the following entries are assigned:Plant 1 AE 3310MRP Controller 001 (001)Tip If not, set the AOR Status toggle for the aforementioned entries to AOR Is Assigned and for all the other entries to AOR Is Unassigned.Choose Back. |  |  |
| 4 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 5 | Search for Material | On the upper-right screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, select Material and choose OK.Enter the following data and choose Go:Material: FG228 or FG227Select the line item with your sales order number, such as CusOrd-XXXXX-10.Choose Manage Requirements. | The Manage External Requirements screen displays. |  |
| 6 | Start MRP Run | Choose the material item. On the lower-right screen, choose Start MRP Run. | An MRP run is started immediately in background. |  |
| 7 | Check Generated Planned Order | Choose the generated planned order, and choose Open > Document Info .Choose Components, and check if the components are the same as those in BoM. | If you have entered BOM explosion number for material in sales order, this BOM explosion number will be copied to generated planned order. |  |

### Process Technical Change BoM in Sales Order (Optional)

This step is valid only when you create sales order with material FG227 in previous step 4.2 MTO Sales Processing (Material with Sales Order BoM) (Optional).

#### Change Order BoM for Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The customer asks for a technical change for finished goods. In this step, you therefore create an order BoM for the sales order and maintain order BoM according to customer requirement (adding material RM20 for this testing).

This process step shows you how to create an order BoM for sales order and maintain the order BoM according to customer requirement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an BOM Engineer - Customer Order. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Order Bill of Material (Version 2) - Create, Change and Display BOMs (F4339A). | The Manage Order Bill of Material screen displays. |  |
| 3 | Select Material BoM | Choose Copy Material BOM. Enter following value in the dialog box and choose Go.Material: FG227Plant: 3310BOM Usage: Production (1)Choose the searched material BoM and choose OK. |  |  |
| 4 | Create Order BoM for Sales Order | Make the following entries and choose Copy.Sales Order: <Sales Order Number Created Previously>Item: 10Material: FG227BOM Usage: 1 (Production) |  |  |
| 5 | Maintain Order BoM | Choose + Add button on the tool bar with the following values:Item: 0100Component: RM20Component Quantity: 100 PC |  |  |
| 6 | Save Order BoM | Choose Create. | Message Bill of material saved. displays. |  |

#### Recalculation of Costs in Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After order BoM is changed, you recalculate the sales order and put additional price for extra component. An order confirmation is printed and can be sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Sales Orders - VA02 (VA02). | The Change Sales Orders screen displays. |  |
| 3 | Navigate to Chang Sales Order Screen | On the Change Sales Orders screen, enter the following value and choose Continue.Order: <Sales Order Number Created Previously> |  |  |
| 4 | Recost Sales Order | Choose the following menu path Menu > Extras > Costing . In the Marked Cost Estimate dialog box , choose Continue.On the Sales Order Costing screen, press Enter. | On the Costing Structure session, check if component RM20 is taken into calculation. |  |
| 5 | Save Costing Result | Choose Save. In the Update Parameters dialog box , choose Continue and Save.In the The costing has not been marked dialog box, choose Yes. |  |  |
| 6 | Add Additional Price | On the Change Sales Order XXX: Overview screen, choose line item and choose the Item Conditions icon on the tool bar above the All Items section.In the Pricing Elements table, add a new entry as below:CnTy: DRQ1Amount: <2>CrCy: AEDPer: <1>UoM: <PC>Press Enter. |  |  |
| 7 | Save Changed Sales | Choose Save. |  |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays |  |
| 3 | Search for Sales Order | Use filter bar to search for the created sales order.Enter <sales order number> in the Sales Order field. | Searched sales order displays. |  |
| 4 | Print Sales Order | Choose sales order number and choose Display Sales Order.On the Display Standard Order XXX: Overview screen, choose More > Extras > Output > Header > Edit .Select the line created with completed status and choose Display Document.Choose Print icon to print your sales order. | Sales order is printed. |  |

|  |
| --- |
| Note If you maintain different material prices by Ledger (scope item 1ZT - Managing Material Price Changes and Inventory Values) and want to do Ledger specific sales order costing, please refer to the scope item BEG - Standard Cost Calculation and its step Appendix > Manage Order BOM Cost Estimates in Parallel Valuation . |

#### Rerun MRP for Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You have added a material for the finished good and evaluate the effects by rerun MRP for the sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Area of Responsibility | On the Monitor Material Coverage - Net / Individual Segments screen, choose your user icon and select APP Settings. In the MRP Settings dialog box, choose Area of Responsibility.Check if only the following entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)If not, set the AOR Status toggle for the previous entries to AOR Is Assigned and for all the other entries to AOR Is Unassigned.Choose Back. |  |  |
| 4 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 5 | Select the Material | Enter the following data and choose Go:Material: FG227Select the line items with your sales quotation / sales order number, such as CustSt XXXXXX-10.Choose Manage Materials. | The Manage Material Coverage screen displays.Note that you select the right individual segment for the customer order. |  |
| 6 | Start MRP Run | Choose a material item and choose Start MRP Run on the right screen. | An MRP run is started immediately in background. |  |
| 7 | Check Generated Planned Order | Choose the newly generated planned order, and choose Document Info.Choose Components, and check the new components RM20 is added. |  |  |

Result

Planned order for the final assembly of material finished good FG227 is updated.

### Production Processing

#### Create Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a production order without an external processing operation.

Prerequisite

Planned orders for assembly finished good (FG228 or FG227 ) is generated in the same way as for parts production.

Procedure

Access the transaction choosing one of the following navigation options:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Area of Responsibility | Choose user icon and select APP Settings icon. In the MRP Settings dialog box, choose Area of Responsibility.Check if only the following entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status button to set the status for the above entry to AOR Is Assigned if not yet assigned.Choose AOR Status button to unassign the rest of other entries.Choose Back. |  |  |
| 4 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 5 | Search for Material | Enter the following data and choose Go:Material: <FG228 or FG227>Select the line item with your sales quotation / sales order number, such as CustSt XXXXXX-10..Choose Manage Materials. | The Manage Material Coverage screen displays.Note that you select the right individual segment for the WBS ID. |  |
| 6 | Convert Planned Order to Production Order | Choose the material item and then choose the generated planned order on the right screen. Select Convert from the dropdown list under column Actions. Choose Convert. | A message displays: Production order XXXXXXXX was created. |  |
| 7 | Rescheduling Check (Optional) | On the Stock/Requirements List tab, the Rescheduling column displays the rescheduling status of the following MRP Elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersIf needed, you can choose the following icons in Rescheduling column for corresponding functions:Reschedule in (bring operation forward if the receipt element lies after the requirement date)Reschedule out (postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment | Corresponding actions perform. |  |

#### Review Order Progress

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to solve material shortage issues of a sales order after reviewing the material availability in a BOM structure.

Prerequisite

Before performing this step, you can adjust the date of the production order to create a shortage.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Review Order Progress - Multilevel View (F7681). | You can also navigate to Review Order Progress – Multilevel View through app Manage Material Coverage - New Version (F0251A) or Monitor External Requirements (F0246A).Access the app Manage Material Coverage - New Version (F0251A). Make the following entries and choose Go:Material: FG228 or FG227Plant: 3310Choose the line item with your sales order number such as CusOrd-XXXXX-10. Under tab Stock/Requirements List, click the sales order in the MRP Element column, and choose Review Order Progress – Multilevel View.Access the app Monitor External Requirements (F0246A). Select Ordered Requirements from Shortage Definition, choose Adapt Filters, adopt the Order filter to search your sales order number, and click the affected sales order number. Choose Related Actions > Review Order Progress – Multilevel View. |  |
| 3 | Display Multilevel Order Report | On the Review Order Progress – Multilevel View screen, make the following entries and choose Go.Note Add the Sales Order Item field by using Adapt Filters.Document Type: Sales Order (VC)Sales Order Number: <Sales Order Number>Sales Order Item: <Item Number>Use the value help to find the sales order item and sales order number. | The BOM structure of the order is displayed and the component availability is checked.For listed components, if there is missing quantity or component that requires reschedule in action/finish date in the past, the following icons are displayed:The error icon indicates detailed errors at the corresponding component level.The warning icon indicates if there is a start date or opening date in the past. |  |
| 4 | Review Order Issues | In the Issues column, choose the icon in the top row. | The overall issues for fulfilling the order are displayed.You can also check issues at different levels by choosing the error icon listed in different rows. |  |
| 5 | Solve Order Issues | In the Material Number column, click the component which is causing issues.In the pop-up window, choose Related Actions > Manage Material Coverage. | The Manage Material Coverage screen displays.The production planner can adopt corresponding actions to make up the shortage. |  |

#### Release Production Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

The production order created by the MRP controller is assigned a release date in accordance with the scheduling margin key.

Purpose

This process step shows you how to release production orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Orders screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisor.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE (3310)MTO w/o VC Val. (YB4)Choose Back. |  |  |
| 4 | Search for Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options.Choose More Filters, and select Material and Production Plant. Choose Go.Enter the following filter criteria to search for your production order and press Enter:Status: CreatedMaterial: FG228 or FG227Production Plant: 3310Choose the filtered production order entry. | The Material and Production Plants fields are added to the filter bar.Searched production order displays. |  |
| 5 | Release Production Order | Choose the production order you created previously.On the XXXXXXX (production order number) page, choose Release in the top right corner of the screen. | Order is released. |  |

#### Pick Components (Picking List)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Ensure that sufficient material is present on stock. To check this, use Monitor Stock / Requirements List - Old Version (MD04) App.

Purpose

The released production order is now ready for picking. Only those materials that are not in the service stock at the assembly aisle are to be picked. For picking, the operator selects the specific picking list that can be called up directly with the production order number. The operator has a series of further selection options to allow for optimal worklist selection. This process step shows you how to pick components (picking list).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen displays. |  |
| 3 | Enter Relevant Search Criteria | Make the following entries and choose Execute.Profile: 000002Production Order: <Your Production Order number> | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking | Select the relevant reservations and choose Picking. | A list of all the selected reservations displays. |  |
| 5 | Batch Determination | Some materials are batch managed, for example: RM122, select relation line item and choose Batch Determination.Make the following entry and choose Copy.Split Quantity: <split quantity> | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Post | Choose Post to post the goods movements. |  |  |

#### Confirm Assembly Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents the processing status of orders, operations, sub operations, and individual capacities. It is an instrument for controlling orders. This scope item uses time event confirmation. This process step shows you how to confirm assembly activities.

|  |
| --- |
| Note In practice, some operations produce scrap due to operational or component defects. To simulate this process, refer to Rework Processing – Work-in-Process (BJQ) scope item and perform steps described in the related test scripts. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Perform Work screen displays. |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and press Enter:Order: <Production Order Number>Operation: <Operation Number>, for example, <0010> |  |  |
| 4 | Enter Quantities Data | In the Quantities section, make the following entries:Yield: <Yield Amount>Scrap: <Scrap Amount> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list. | The system displays an overview table of all materials for which the withdrawing is automatically done with the confirmation of the operation.If there are not any materials set for backflush (in material master), then no materials display in the table. |  |
| 6 | Enter Activities Data | In the Activities section, make the following entries:Setup: <Setup Time>Machine: <Machine Time>Labor: <Labor Time> |  |  |
| 7 | Save your Entries | For partial confirmation, choose Post.For final confirmation for this operation, choose Post and Complete. | Confirmation is made. |  |
| 8 | Repeat Steps | Go back and repeat steps 3-7 for Operation <0020> and <0040>. |  |  |

#### Post Goods Receipt for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Production Order (F3110). | The Post Goods Receipt for Production Order screen displays. |  |
| 3 | Enter Order Number | Make the following entry and press Enter:Order: <Production Order Number Created Previously> |  |  |
| 4 | Check and Post | In the Items section, select the item and choose Post.The Success dialog box displays with the following message: 1 material document(s)posted: XXXXXXXXX.Choose OK. | Goods receipt for production order has been posted. |  |

### Delivery Processing

#### Create Delivery with Order Reference

Purpose

This process step shows you how to create delivery to customer.

Procedure

Go to Sales Order Processing with Customer Down Payment (BKJ) test script and run Create Delivery step as a Shipping Specialist using master data from this test script.

Result

You successfully created the delivery for the finished good.

#### Execute Picking

Purpose

In this step, we take goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

Go to Sales Order Processing with Customer Down Payment (BKJ) test script and run Execute Picking step as a Shipping Specialist using master data from this test script.

Result

You successfully picked finished goods for delivery.

#### Post Goods Issue

Purpose

This process step shows you how to post goods issue for the delivery.

Procedure

Go to Sales Order Processing with Customer Down Payment (BKJ) test script and run Post Goods Issue step as a Shipping Specialist using master data from this test script.

Result

You successfully posted goods issue for delivery.

### Billing Process

During billing, the revenue for order items from make-to-order production are passed on to financial accounting. Once the item is fully invoiced, the status is set to fully invoiced. In this scope item, partial amounts are billed via down payment and closing invoice.

#### Change Sales Orders (Remove Billing Block)

Purpose

After the finished goods are shipped, it is ready to invoice the customer. The billing blocks in sales order are removed before billing takes place. This process step shows you how to change sales orders(remove billing block).

Procedure

Go to Sales Order Processing with Customer Down Payment (BKJ) test script and run Change Sales Orders (Remove Billing Block) step as an Internal Sales Representative using master data from this test script.

#### Billing

Purpose

This process step shows you how to bill the customer.

Procedure

Go to Sales Order Processing with Customer Down Payment (BKJ) test script and run Billing step as a Billing Clerk using master data from this test script.

### Review Manufacturing Object Pages

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the different objects pages available for different roles in the area of manufacturing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner.Note You can use any role in the Roles section above. | The SAP Fiori launchpad displays. |  |
| 2 | Search Material | Choose the Search icon in the upper right area of the launchpad.Make the following entries and choose Search:Search: <BOM Header Material>, refer to the Master Data, Organizational Data, and Other Data section | The system displays a list of objects using the selected material. |  |
| 3 | Display Object | In the All field, select an object from the dropdown list and choose the Search icon. | The list of objects is limited to the object type selected. If no object is selected, a message is displayed instead. |  |
| 4 | Tailor the Result Display | Under the search line, choose an icon (for example, Show filters, Display as Table, Sort and so on) to filter the results list. | The results list is filtered according to your selections. |  |
| 5 | Review Production Order Fact Sheet | Choose searched production order number and go into production order fact sheet.Check details in production order fact sheet. | If the product is configurable, you can choose Display in the Items section to display configuration details for the product. |  |
| 6 | Repeat Steps | Repeat steps 1-5 for any other role in this test script and any other object offered in the search function. | The list of objects offered for search differs by the role you used to log on. |  |

## Appendix

### Process Integration

The process to been tested in this test script is part of a chain of integrated processes.

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Complete the following activities:Posting a Customer Invoice in AccountingOverdue ReceivablesDisplay Customer BalancesManage Customer Line Items |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

### Additional Functional Information

If you want to know functional information for Discrete and Process Manufacturing beyond what is described in the test scripts of the best practice scope items for SAP S/4HANA Cloud Public Edition, you could check SAP Note [3441318](https://me.sap.com/notes/3441318).

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
- related-to :: [[12-production-and-manufacturing/test-script-make-to-order-production-process-manufacturing-3ok-ae-966]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJE_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 68,760 chars in the whole document
