---
id: 08-sales-order-management/test-script-sales-order-processing-with-invoice-list-and-collective-bi
title: "Test Script: Sales Order Processing with Invoice List and Collective Billing (BKZ_AE) (BKZ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 (AE) test script: order-to-invoice with invoice lists to a central payer and collective billing, covering apps, roles and postings."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/invoice-lists-collective-billing-self-billing]
aliases: [BKZ_S4CLD2608_BPD_EN_AE]
keywords: ["Invoice Lists, Collective Billing and Self-Billing", invoice lists, collective billing, sales order processing, test scripts, outbound delivery, billing documents, picking, goods issue posting, financial postings]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKZ_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1282
topic: 08-sales-order-management/invoice-lists-collective-billing-self-billing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales Order Processing with Invoice List and Collective Billing (BKZ_AE) (BKZ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKZ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Invoice Lists, Collective Billing and Self-Billing** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Order Processing with Invoice List and Collective Billing (BKZ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862656)

[2 Prerequisites 4](#_Toc232862657)

[2.1 System Access 4](#_Toc232862658)

[2.2 Roles 4](#_Toc232862659)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862660)

[2.4 Business Conditions 7](#_Toc232862661)

[2.5 Preliminary Steps 7](#_Toc232862662)

[2.5.1 Set Initial Stock for Material 7](#_Toc232862663)

[2.5.2 Create Condition Records (Optional) 9](#_Toc232862664)

[3 Overview Table 10](#_Toc232862665)

[4 Test Procedures 12](#_Toc232862666)

[4.1 Sales Order Processing with Invoice Lists 12](#_Toc232862667)

[4.1.1 Create Sales Order 12](#_Toc232862668)

[4.1.2 Create Attachment for Sales Order (Optional) 14](#_Toc232862669)

[4.1.3 Create Delivery 15](#_Toc232862670)

[4.1.4 Create Attachment for Delivery (Optional) 17](#_Toc232862671)

[4.1.5 Execute Picking 18](#_Toc232862672)

[4.1.6 Check Batches (Optional) 19](#_Toc232862673)

[4.1.7 Post Goods Issue 20](#_Toc232862674)

[4.1.8 Create Billing Document 22](#_Toc232862675)

[4.1.9 Create Attachment for Billing (Optional) 24](#_Toc232862676)

[4.1.10 Create Invoice List 25](#_Toc232862677)

[4.2 Sales Order Processing with Collective Billing 27](#_Toc232862678)

[4.2.1 Create Sales Order 27](#_Toc232862679)

[4.2.2 Create Attachment for Sales Order (Optional) 29](#_Toc232862680)

[4.2.3 Create Delivery 30](#_Toc232862681)

[4.2.4 Create Attachment for Delivery (Optional) 32](#_Toc232862682)

[4.2.5 Execute Picking 33](#_Toc232862683)

[4.2.6 Check Batches (Optional) 34](#_Toc232862684)

[4.2.7 Post Goods Issue 35](#_Toc232862685)

[4.2.8 Create Billing Document 37](#_Toc232862686)

[4.2.9 Create Attachment for Billing (Optional) 39](#_Toc232862687)

[5 Appendix 41](#_Toc232862688)

[5.1 Process Integration 41](#_Toc232862689)

[5.2 Succeeding Processes 41](#_Toc232862690)

[5.3 Scheduling Job (alternative) 41](#_Toc232862691)

[5.3.1 Job Scheduling for Delivery Creation (Alternative) 41](#_Toc232862692)

[5.3.2 Job Scheduling for Goods Issue Deliveries (Alternative) 42](#_Toc232862693)

[5.3.3 Job Scheduling for Billing Creation (Alternative) 43](#_Toc232862694)

[5.3.4 Job Scheduling for Billing Release (Alternative) 44](#_Toc232862695)

[5.3.5 Job Scheduling for Billing Output (Alternative) 45](#_Toc232862696)

## Purpose

Overview

With invoice lists, you can send a list that involves several billing documents to a central payer with special discount applicable at specific time intervals. The process starts with the creation of several standard sales orders for different sold-to parties that share the same payer. After individual billing documents are generated and forwarded to Financial Accounting, invoice lists can be created with reference to multiple billing documents for the central payer. Factoring discount and possible taxes are posted to FI.

This scope item describes the usage of standard sales processing for mass-processing billing. For optimization of shipping costs, all sales orders that are delivered to the same customer are packed into one delivery document. For cost optimization, all deliveries due to be invoiced to the same customer are packed into one invoice document. The revenue is posted to accounting accordingly.

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
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)No serial number, no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.No serial number, no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG) (BLH) (BLJ) (BLP)..See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date) | Only use if you have activated the building blockBatch Management (BLG) (BLH) (BLJ) (BLP)..See sections Business Conditions and Preliminary Steps. |
| Material | CM-FL-V00 | Forklift | Only use if you have activated the scope item Make-to-Order Production with Variant Configuration (1YT). |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| For Collective Billing |  |  |  |
| Sold-to party | 33100001 | Domestic UAE Customer 1 | Order combination is switched off in customer master. |
| Ship-to party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Sold-to party | 33100002 | Domestic UAE Customer 2 | Order combination is switched off in customer master. |
| Ship-to party | 33100002 | Domestic UAE Customer 2 |  |
| Payer | 33100002 | Domestic UAE Customer 2 |  |
| For Invoice List |  |  |  |
| Sold-to party | 33100012 | Domestic Customer Invoice List |  |
| Ship-to party | 33100012 | Domestic Customer Invoice List |  |
| Payer | 33100014 | PAYER - Central |  |
| Sold-to party | 33100013 | Domestic Customer Invoice List |  |
| Ship-to party | 33100013 | Domestic Customer Invoice List |  |
| Payer | 33100014 | PAYER - Central |  |

For more information about creating master data, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Script documentation.

Table 1: Master Data Script Reference

| Master Data Script ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either:Run through the Procurement of Direct Materials (J45) process,Or create stock using Fiori Launchpad tile Post Goods Movement (for details see section Preliminary Steps). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Set Initial Stock for Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set initial stock to execute this scope item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk (Retail). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Other screen displays. |  |
| 3 | Enter Movement Type | Make the following entry and choose Enter.Executable Action in Transaction MIGO: Goods Receipt & Other |  |  |
| 4 | Edit Material | On the Goods Receipt Other Screen: Material tab, make the following entry, and choose Enter:Material : <Material Number> . |  |  |
| 5 | Edit Quantity Data | On the Goods Receipt Other Screen: Quantity tab, make the following entry, and choose Enter:Qty in Unit of Entry: 1000Unit of Entry: <PC> |  |  |
| 6 | Enter the Goods Receipt Other Screen: Where Tab | On the Goods Receipt Other Screen: Where tab, make the following entries and choose Enter:Movement Type: 561 (Receipt per initial entry of stock balances into unrestricted use)Plant: <Enter a Plant>Storage Location: <Enter a Storage Location> |  |  |
| 7 | Enter the Goods Receipt Other Screen: Batch Tab | On the Goods Receipt Other Screen: Batch tab, make the following entry and choose Enter:Date of Manufacture: <Enter the Current Date or a Date in the Past> | Only relevant for batch relevant materials. |  |
| 8 | Save Your Entries | Choose Post. |  |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 13600000Inventory TradingGd | 39912000Inv Init SF&amp;Fin Bal |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

## Overview Table

The scope item Sales Order Processing with Invoice List and Collective Billing consists of several choose the appropriate entity: process steps, reports, items provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Overview of the process for Sales Order Processing with Invoice Lists:

| Sales Order | Delivery | Invoice (Billing Document) | Invoice List |
| --- | --- | --- | --- |
| Order 1 from Customer 33100012 with Material 1 | Delivery 1 to customer 33100012 | Invoice 1 to customer 33100012 | Invoice List 1 to payer 33100014 |
| Order 2 from Customer 33100013 with Material 1 | Delivery 2 to customer 33100013 | Invoice 2 to customer 33100013 |  |
| Order 3 from Customer 33100014 with Material 1 | Delivery 3 to customer 33100014 | Invoice 3 to customer 33100014 |  |

Payer 33100014 is responsible to pay all invoices for goods that are shipped to customers 33100012, 33100013 and 33100014. After sales order, delivery and invoice are created, invoice list including all invoices with same payer is generated, certain factoring discount and discount tax are calculated and posted to accounting.

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_10) [page ] 12 | Internal Sales Representative | Manage Sales Orders - Version 2 (F3893) |  |
| [Create Attachment for Sales Order (Optional)](#unique_11) [page ] 14 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Delivery](#unique_12) [page ] 15 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Create Attachment for Delivery (Optional)](#unique_13) [page ] 17 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| [Execute Picking](#unique_14) [page ] 18 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Check Batches (Optional)](#unique_15) [page ] 19 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Post Goods Issue](#unique_16) [page ] 20 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Create Billing Document](#unique_17) [page ] 22 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Create Attachment for Billing (Optional)](#unique_18) [page ] 24 | Billing Clerk | Manage Billing Documents (F0797) |  |
| [Create Invoice List](#unique_19) [page ] 25 | Billing Clerk | Manage Invoice Lists (F2740) |  |

Overview of the process for Sales Order Processing with Collective Billing:

| Customer Order | Delivery | Invoice |
| --- | --- | --- |
| Order 1 from Customer 33100001 with Material 1 | Delivery 1 to customer 33100001 | Invoice 1 to customer 33100001 |
| Order 2 from Customer 33100001 with Material 1 | Delivery 2 to customer 33100001 | Invoice 1 to customer 33100001 |
| Order 3 from Customer 33100002 with Material 1 | Delivery 3 to customer 33100002 | Invoice 2 to customer 33100002 |
| Order 4 from Customer 33100002 with Material 1 | Delivery 3 to customer 33100002 | Invoice 2 to customer 33100002 |

For customer 33100002, the Order Combination (sales area data) checkbox is switched on. Therefore, when created with Collective Processing of Documents Due for Delivery, several customer orders from this customer are merged into one delivery. Customer 33100001 has not switched on this flag and so gets separate deliveries.

By creating the invoices via the mass-process Billing Due List, all deliveries for one customer are listed in one invoice for the customer.

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Sales Order](#unique_20) [page ] 27 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Attachment for Sales Order (Optional)](#unique_11) [page ] 14 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Delivery](#unique_21) [page ] 30 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Create Attachment for Delivery (Optional)](#unique_22) [page ] 32 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| [Execute Picking](#unique_23) [page ] 33 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Check Batches (Optional)](#unique_24) [page ] 34 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Post Goods Issue](#unique_25) [page ] 35 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Create Billing Document](#unique_26) [page ] 37 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Create Attachment for Billing (Optional)](#unique_27) [page ] 39 | Billing Clerk | Manage Billing Documents (F2250) |  |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

The enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request. You can search for objects such as: apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

1. Log on to the SAP Fiori launchpad as a respective user, for example, Internal Sales Representative.
2. Access the Enterprise Search Bar by choosing the magnifying glass icon in the upper right corner.
3. The Enterprise Search bar displays two filter fields next to the search icon: all dropdown menu and a search field. Enter your Search Criteria and choose the business object type, for example, select Sales orders from the dropdown menu, and enter a sales order number in the search field and choose Search, the sales order lists.
4. Choose the sales order number link. The system navigates to the fact sheet screen and sales order related information is integrated and summarized in one Fiori page. You can get detailed data by choosing the corresponding links.

There are fact sheets available for the following objects (visible depending on the assigned role):

- Sales order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Sales Order Processing with Invoice Lists

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2 screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders - Version 2 screen, choose Create. |  |  |
| 4 | Enter Order Details | On the Create Standard Order: Initial screen, make the following entries and choose Continue:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On the New: Sales Order screen, make the following entries and choose Continue:Sold-To Party: 33100012Ship-To Party: 33100012Customer Reference: <Reference number> Enter a customer purchase order number as reference.Customer Reference Date: <today>Go to item Overview TabProduct: <product material>Order Quantity: <quantity> |  |  |
| 6 | Save | Choose Create. Make a note of the sales order number:___________. | Sales order with customer 33100012 is created. |  |
| 7 | Create More Sales Orders | Repeat above steps to create 2 more sales orders: one with Sold-to party33100013, the other two with Sold-to party 33100014.Make a note of the sales order numbers:___________. | Sales orders are created respectively for customers 33100013 and 33100014. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2 screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar and choose Go, for example, enter sales order number in field Sales Order. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right of the Sales Order item and navigate to Display Standard Orders xxx: Overview screen. | The Display Standard Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Header Output Preview. |  |  |
| 6 | Display Print Preview | On the Display Standard Order xxx: Output screen, select the line already created for the print output and choose Display Document. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in app Manage Sales Orders - Version 2 (F3893):On the Manage Sales Orders (Original) screen, enter search terms in filter bar and choose Go.In search result, choose your Sales Order Number and choose More Links. |

#### Create Attachment for Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachment for a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2screen displays. |  |
| 3 | Navigate to Change Sales Order Screen | On the Manage Sales Orders - Version 2 screen, enter the respective order number created in previous step and choose Go.Click the sales order number and choose Change Sales Order - VA02. |  |  |
| 4 | Create Attachment for Sales Order | Choose Services for Object on the top right corner of screen, choose Create Attachment. | The File Upload screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of screen, choose Attachment List. | Attachment brings up on the Service: Attachment list screen. |  |

#### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three deliveries from three sales orders created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Order: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales orders and choose Create Deliveries. | Deliveries are triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. The failed entries will display in Messages tab. The delivery number will display in the Deliveries tab.Three deliveries are created, for customer 33100012, 33100013, 33100014, |  |

|  |
| --- |
| Note At delivery creation, the scope item settings for check availability use available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities and does not start the warehouse management picking process. As soon as there is sufficient stock at delivery creation, the system creates a delivery with further picking process in warehouse management. To avoid open deliveries, ensure that there is sufficient inventory quantity at delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.- You may increase replenishment lead time that is used during the availability check (must be larger than the selection period used for delivery creation).- You may change the customizing settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.- You may change the customizing settings for the used delivery item category.The Check quantity 0 field must be adapted to B = Situation rejected with an error message. |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, created by and Additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the delivery number and choose Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control . | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery_Pick_List and choose Display Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Create Attachment for Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachment for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Display Outbound Delivery: Initial screen displays. |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <the outbound delivery number created in previous step> and choose Continue. | The Display Outbound Delivery xxx: Overview screen displays. |  |
| 4 | Create Delivery Attachment | Choose Services for Object on the top right corner of screen, choose Services for Object and then choose Create Attachment. | The File Upload screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object, then choose Attachment List. | Attachment shows up on Service: Attachment List screen. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to execute picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad screen displays. |  |
| 2. | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3. | Choose Picking | Choose For Picking. |  |  |
| 4. | Enter Shipping point | Make the following entries and choose Execute.Shipping point: 3310Only Picking without WM: X |  |  |
| 5. | Change Outbound Delivery | From Day’s Workload for Picking, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6. | Check If Batch Split Exists | Navigate to the Picking tab, check if batch split exists in Batch Split Indicator column:Yes: go to 7.a,No: go to 7.b. |  |  |
| 7. | Enter Picked Quantity | Choose Batch Split Exists to expand sub item(s), enter quantity equal to delivery Qty in field Picked Qty for sub item.Enter quantity equal to delivery Qty in field Picked Qty for picking related item(s). |  |  |
| 8. | Choose Enter | Choose Enter. |  |  |
| 9. | Save | Choose Save. | Three deliveries have been picked. |  |

#### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the batch number assigned to the material.

Prerequisites

Execute this step if batch management is used, such as TG21 and TG22.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3 | Enter Outbound Delivery Number | In the Outbound Delivery field, enter <outbound delivery number>, and choose Enter. |  |  |
| 4 | Check Batch Number Assignment | If Expand Batch Split exists, go to the Batch field, and check the batch number assignment. | Batch numbers are assigned to the materials. |  |
| 5 | Save Document | Choose Save. |  |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute.Shipping Point: 3310 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box and choose Continue. | The goods issues are posted for three deliveries. |  |

Financial Postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

|  |
| --- |
| Note When the bundling functionality in context of IFRS15 is tested the financial document in IFRS ledger (Ledger Group 2L) with the adjusted revenue amount is displayed.To check the financial document, please use the role: SAP_BR_WAREHOUSE_CLERK and tile: Display Material Document List. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the delivery number and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Delivery Note Output Type and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle the billing: Create three billing documents referring to the deliveries created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using Role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings. You can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities：OFF |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Select Item(s) for Billing | Select row(s) of sales document created previously and choose button Create Billing Document. | There is one window Creating Billing Documents displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date. For example: current date, then choose OK. | The draft billing document with ID TMPxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document (F1901) screen, choose Save. The draft version billing document with ID TMPxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

|  |
| --- |
| Note After this step, the Electronic Nota Fiscal must be handled. This is part of scope item 1J5_BR (section Electronic Fiscal Documents). |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | Enter G/L Acc 12100000 | 41000000 Rev Domestic Prod | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | In the billing document number recorded in previous step, choose Enter. | The billing document created in previous step displays. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document (F1901) screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel Billing Document. | Billing Document Canceled log displays. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing the button Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, add, delete and update the text. Save your changes by pressing the button Save in the footer bar. |  |  |

#### Create Attachment for Billing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create an attachment for a billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 3 | Search Billing | Make the following entry, and choose Enter:Billing Document: <Billing Document Number Created Previously> |  |  |
| 4 | Choose Billing Number | On the Manage Billing Documents screen, select your billing document created in the previous step, and choose Display. | The Billing Document screen displays. |  |
| 5 | Edit | On the Billing Documents screen, choose Edit. |  |  |
| 6 | Create Billing Attachment | Scroll down and choose Upload in the ATTACHMENTS section. | The Open File screen displays. |  |
| 7 | Import File | In the Open window, select a local path or file and choose Open.Choose Save. | The attachment is successfully created. |  |
| 8 | Check Attachment | In the ATTACHMENTS section, you can see the uploaded document. Choose the document you want to open. |  |  |

#### Create Invoice List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create invoice list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Invoice Lists (F2740). | The Manage Invoice Lists (F2740) screen displays. |  |
| 3 | Navigate to Edit Worklist for Invoice Lists Screen | Choose Create. | The Edit Worklist for Invoice Lists screen displays. |  |
| 4 | Search Billing Documents | Make the following data in section Customer Data and choose Display Worklist for Invoice Lists:Payer: 33100014 | Billing documents displays in the result. |  |
| 5 | Select item(s) for Invoice List | Select the rows of Billing documents created previously and choose Collective Billing Document. | The system generates an invoice list for billing. |  |
| 6 | Check Invoice List Document | On the Edit Worklist for Invoice Lists screen, choose Log Display. And then choose Documents, make a note of the invoice list document number in SD Document column: __________. | Invoice list document number displays. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 44002000 Sales Disc Domestic22000000 Output tax (MWS) | Enter G/L Acc 1210000012100000 Description. | none |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Invoice Lists (F2740). |  |  |
| 3 | Search for Invoice List | Enter search term(s) in filter bar and choose Go:For example, enter invoice list number in field Invoice List. | The invoice list is displayed in result list. |  |
| 4 | Navigate to Invoice List Overview Screen | Click invoice list number 9XXXXXXX and choose Display Invoice Lists (VF23). | The Invoice List Display: Invoice List Items Overview screen displays. |  |
| 5 | Check Output Condition | Choose Output. | The Invoice List Display: Output screen displays. |  |
| 6 | Display Print Preview | Select the line already created for the print output and choose Display Document. | The printing form is displayed. |  |

|  |
| --- |
| Note The invoice list can consolidate a list of billing documents: Not only standard invoices with type F2 as above, but also debit memos, credit memos, and convergent billing types (CBD1, CBD2 and CBC1). To simulate invoice lists from debit memo，credit memo, or convergent billing, firstly complete all activities till debit memo/credit memo / convergent billing generation in the following scope item(s) using the data listed in chapter Master Data, Organizational Data, and Other Data:1F1 - Debit Memo Processing1IU - Customer ConsignmentBDD - Lean Customer ReturnsBKP - Customer Returns1EZ - Credit Memo Processing1MC - Omnichannel Convergent Billing |

### Sales Order Processing with Collective Billing

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to enter four sales orders: sales orders 1 and 2 are for customer 33100001, sales orders 3 and 4 are for customer 33100002.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). |  |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Order screen, choose Add, then select Create Sales Order |  |  |
| 4 | Enter Sales Document Type | On Create Standard Order: Initial screen, make the following entries and choose Enter:Order Type: ORSales organization: 3310Distribution channel: 10Division: 00 |  |  |
| 5 | Enter Order Details | On Create Standard Order: Overview screen, make the following entries and choose Enter:Sold-To Party: 33100001Ship-To Party: 33100001Customer Reference: <Customer Reference>Customer Reference Date: <Date>Material: <material number> , TG11 for example.Order Quantity: <quantity> | Make a note of the sales order number. |  |
| 6 | Save | Choose Save. Make a note of the sales order number:___________.Note If you have installed the scope item Free Goods Processing in your system and you use material TG11 and customer 33100001, the following warning may appear: Minimum quantity 1.000 PC of free goods has not been reached. To skip this warning, choose Enter. | Sales order with customer 33100001 is created. |  |
| 7 | Create More Sales Orders | Repeat above steps to create 3 more sales orders: one with Sold-to party33100001, the other two with Sold-to party33100002.Make a note of the sales order numbers:___________. | Three more sales orders are created. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). |  |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar and choose Go:for exmple, enter sales order number in the Sales Order field. | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right of the Sales Oder item and navigate to Display Standard Oders xxx: Overview screen. | The Display Standard Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Orders XXX: Overview screen choose Extras > Output > Header > Edit . |  |  |
| 6 | Display Print Preview | On the Display Standard Oders xxx: Output screen select the line already created for the print output and choose Display PDF Document. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in app Manage Sales Orders:On the Manage Sales Orders screen, enter search terms in filter bar and choose Go.In search result, choose your Sales Order Number and choose More Links. |

#### Create Attachment for Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create attachment for a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2screen displays. |  |
| 3 | Navigate to Change Sales Order Screen | On the Manage Sales Orders - Version 2 screen, enter the respective order number created in previous step and choose Go.Click the sales order number and choose Change Sales Order - VA02. |  |  |
| 4 | Create Attachment for Sales Order | Choose Services for Object on the top right corner of screen, choose Create Attachment. | The File Upload screen displays. |  |
| 5 | Import File | Choose OK in the File Upload dialog box.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of screen, choose Attachment List. | Attachment brings up on the Service: Attachment list screen. |  |

#### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create three deliveries: two deliveries are for customer 33100001, one delivery is for customer 33100002.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <Delivery selection date>Sales Document: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales orders and choose Create Deliveries. | A delivery is triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. The failed entries will display in Messages tab. The delivery number will display in the Deliveries tab.Three deliveries are created, for customer 33100002, , the Order Combination checkbox is switched on, several sales orders for this customer are merged together into one delivery. The flag is not set for the customer 33100001, . |  |

|  |
| --- |
| Note At delivery creation, the scope item settings for check availability use available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities and does not start the warehouse management picking process. As soon as there is sufficient stock at delivery creation, the system creates a delivery with further picking process in warehouse management. To avoid open deliveries, ensure that there is sufficient inventory quantity at delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.- You may increase replenishment lead time that is used during the availability check (must be larger than the selection period used for delivery creation).- You may change the customizing settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.- You may change the customizing settings for the used delivery item category.The Check quantity 0 field must be adapted to B = Situation rejected with an error message. |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app you can display an overview about the logs of all the deliveries which have been created in your system. You can filter by, for example, created by and Additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text and also the related sales document. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) | The Change Outbound Delivery (VL02N) screen displays |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the Delivery number and click Continue. From the Delivery xxxxxxxx Change: Overview screen, choose More > Extras > Delivery Output > Output Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery_Pick_List and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

#### Create Attachment for Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery: Initial screen displays. |  |
| 3. | Enter the Outbound Delivery Number | On the Display Outbound Delivery screen, enter the outbound delivery number created in previous step and choose Enter. | The Display Outbound Delivery xxx: Overview screen displays. |  |
| 4. | Create Attachment for Delivery | Choose Services for Object on top right corner of screen, and then choose Create Attachment. | Import file screen pops up. |  |
| 5. | Import File | Choose Import from native file system.On the Open screen, choose local path and file, choose Open.Click OK in pop-up screen that shows import finished.Navigate Back to Import file screen, select file item, and click Choose to close window. | The attachment was successfully created. |  |
| 6. | Check Attachment | Click button Services for Object on top right corner of screen, choose Attachment list. | Attachment brings up in Service: Attachment list screen. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to execute picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad screen displays. |  |
| 2. | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3. | Choose Picking | Choose For Picking. |  |  |
| 4. | Enter Shipping point | Make the following entries and choose Execute.Shipping point: 3310Only Picking without WM: X |  |  |
| 5. | Change Outbound Delivery | From Day’s Workload for Picking , select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6. | Check If Batch Split Exists | Navigate to the Picking tab, check if batch split exists in Batch Split Indicator column:Yes: go to 7.a,No: go to 7.b. |  |  |
| 7. | Enter Picked Quantity | Choose Batch Split Exists to expand sub item(s), enter quantity equal to delivery Qty in field Picked Qty for sub item.Enter quantity equal to delivery Qty in field Picked Qty for picking related item(s). |  |  |
| 8. | Choose Enter | Choose Enter. |  |  |
| 9. | Save | Choose Save. | The three deliveries have been picked. |  |

#### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the batch number assignment to the material.

Prerequisites

Use this step if batch management is used. E.g. TG21 and TG22

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2. | Access the App | Open Change Outbound Delivery (VL02N). |  |  |
| 3. | Enter the Outbound Delivery Number | On the Change Outbound Delivery (VL02N) screen, enter the outbound delivery number and choose Enter. |  |  |
| 4. | Check the Batch Number Assignment | Expand Batch Spilit exists. In the Batch field, check the batch number assignment. | Batch numbers are assigned to the materials. |  |
| 5. | Save Document | Choose Save. |  |  |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods issues for three deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2. | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3. | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entries and choose Execute.Shipping point: 3310 |  |  |
| 4. | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select todayâ€™s date from the dialog box and choose Continue. | The goods issue is posted. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Consptn Trde Gds | 13600000Inventory TradingGd | none |

|  |
| --- |
| Note When the bundling functionality in context of IFRS15 is tested the financial document in IFRS ledger (Ledger Group 2L) with the adjusted revenue amount is displayed.To check the financial document, please use the role: SAP_BR_WAREHOUSE_CLERK and tile: Display Material Document List. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). |  |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the Delivery Number and choose Continue. From the Delivery xxxxxxxx Display: Overview screen, choose More > Extras > Delivery Output > Output Control . | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note and choose Display PDF Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create two invoices: one is for customer 33100001, the other is for customer 33100002.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the bottom bar. You can make the following settings as below:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities：OFF |  |  |
| 4 | Search for Billing Due List | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Select Item(s) for Billing | Select row(s) of sales document created previously and choose Create Billing Documents. | There is one window Creating Billing Documents displaying. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date. For example: current date, then choose button OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Documents screen, choose Save All. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | Enter G/L Acc 12100000 | 41000000 Rev Domestic Prod | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Access the App | Open Manage Billing Documents (F0797) | The Manage Billing Documents (F0797) screen displays. |  |
| 2. | Search the Billing Document Created in Previous Step | In the billing document number recorded in previous step, choose Enter. | The billing document created in previous step displays. |  |
| 3. | Display the Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4. | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and output type is BILLING_DOCUMENT. |  |
| 5. | Display Print Preview | On the Billing Documents screen, choose Preview. | Preview for PDF document displays. |  |
| 6. | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel Billing Docs. | There is log display - Billing Document Canceled. |  |
| 7. | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8. | Update New Text (Optional) | In the Edit mode, add, delete and update the text. Save your changes by choosing Save in the footer bar. |  |  |

#### Create Attachment for Billing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to upload the attachment in billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Billing Documents (F2250). | The Manage Billing Documents (F2250) screen displays. |  |
| 3 | Enter the Billing Number | On the Manage Billing Documents (F2250) screen, enter the respective invoice number created in the previous step and choose Continue. | The F2 Invoice xxx(F2) Display: Overview of Billing Items screen displays. |  |
| 4 | Create Attachment | Choose Services for Object on top right corner of the screen. Choose Create Attachment. | The Import file screen displays. |  |
| 5 | Import File | Choose Import from native file system.In the Open window, select a local path or file, and choose Open.Choose OK in pop up screen that shows import finished.Navigate back to the Import file screen and select a file item.Choose Choose. | The attachment is successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of the screen. Choose Attachment list. | Attachment brings up on the Service: Attachment list screen. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

Table 3:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable(J59) | Posting a Customer Invoice in Accounting, etc. Using the master data from this document, complete the following activities described in the test script:Posting a Customer Invoice in AccountingOverdue Receivables, Display Customer BalancesManage Customer Line Items |
| Sales Order Fulfillment Monitoring and Operations (BKK) (optional) | This scope item describes the collection of periodic activities such as day ending activities, or reporting. Using the master data from this document, complete all the activities described in the Test Script of the scope item:Review Incomplete SD Documents (deliveries),Review Sales Documents blocked for billingReview Log of collective invoice creation |

### Scheduling Job (alternative)

#### Job Scheduling for Delivery Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for creating outbound deliveries.

This app can be used as an alternative instead of the manual creation of outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose Create to define a new job. | The New Job screen displays. The Job Template should be Schedule Delivery Creation for Sales Orders. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A delivery creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Delivery Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details displays. |  |

#### Job Scheduling for Goods Issue Deliveries (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for goods issue posting with reference to outbound deliveries.

This app can be used as an alternative instead of the manual goods issue posting for outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries (F2259). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job screen displays. The Job Template should be defaulted as Schedule goods issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for deliveries job is scheduled. The screen goes back to Application Jobs. |  |
| 6 | Check Goods Issue Deliveries Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will refresh. | The job log details are displayed. |  |

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
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. Screen goes back to Application Jobs. |  |
| 6 | Check Billing Creation Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose the Magnifier, and the job list will refresh. | The log details display. |  |

#### Job Scheduling for Billing Release (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for release billing documents to accounting.

This app can be used as an alternative instead of the manual release to accounting for billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Release (F1518). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template defaultly should be Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Release Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details displays. |  |

#### Job Scheduling for Billing Output (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to schedule a background job for when and how billing documents are sent to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output (F1510). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose Create to define a new job for billing creation. | The New Job screen displays. Job Template should default as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary.Choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Return to Application Jobs. |  |
| 6 | Check Billing Output Job Log | On the Application Jobs screen, after job item’s status turned to Finish, choose Job Log.Note Choose Magnifier, and the job list will refresh. | The log details display. |  |

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
> Flagged while digesting this document, not verified: Master data table says Order combination is switched off in the customer master for both 33100001 and 33100002, but the Overview Table and the collective-billing Create Delivery step say the Order Combination checkbox is switched on for 33100002 (its orders merge into one delivery).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Goods issue debit account differs between the two processes: 51600000 Consptn Trde Gds in the invoice list section versus 54083000 Consptn Trde Gds in the collective billing section, for the same Trading Good (HAWA) posting.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/self-billing-4h2-ae-test-script-sap-s-4hana-cloud-public-edition-1028]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BKZ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 78,742 chars in the whole document
