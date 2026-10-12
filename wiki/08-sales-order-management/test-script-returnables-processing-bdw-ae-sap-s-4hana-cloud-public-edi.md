---
id: 08-sales-order-management/test-script-returnables-processing-bdw-ae-sap-s-4hana-cloud-public-edi
title: "Test Script: Returnables Processing (BDW_AE) - SAP S/4HANA Cloud Public Edition (BDW_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item BDW: shipping pallets, pallet returns and billing of unreturned pallets, with roles and data."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/returnable-packaging]
aliases: [BDW_S4CLD2608_BPD_EN_AE]
keywords: [Returnable Packaging and Pallets, returnable packaging, pallet returns, unreturned pallets billing, sales order creation, outbound delivery, picking and goods issue, billing documents, delivery without order reference, scope item testing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDW_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1258
topic: 08-sales-order-management/returnable-packaging
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Returnables Processing (BDW_AE) - SAP S/4HANA Cloud Public Edition (BDW_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDW_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Returnable Packaging and Pallets** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Returnables Processing (BDW_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861297)

[2 Prerequisites 4](#_Toc232861298)

[2.1 System Access 4](#_Toc232861299)

[2.2 Roles 4](#_Toc232861300)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861301)

[2.4 Business Conditions 6](#_Toc232861302)

[2.5 Preliminary Steps 7](#_Toc232861303)

[2.5.1 Set Initial Stock for Material 7](#_Toc232861304)

[2.5.2 Create Condition Records (Optional) 8](#_Toc232861305)

[3 Overview Table 9](#_Toc232861306)

[4 Test Procedures 11](#_Toc232861307)

[4.1 Sales Process Including Returnable Materials 11](#_Toc232861308)

[4.1.1 Display Pallets Stock 11](#_Toc232861309)

[4.1.2 Create Sales Order 12](#_Toc232861310)

[4.1.3 Create Attachment for Sales Order (Optional) 14](#_Toc232861311)

[4.1.4 Create Delivery 15](#_Toc232861312)

[4.1.5 Create Attachment for Delivery (Optional) 17](#_Toc232861313)

[4.1.6 Add Delivery Item for Pallet 18](#_Toc232861314)

[4.1.7 Execute Picking 19](#_Toc232861315)

[4.1.8 Check Batches (Optional) 20](#_Toc232861316)

[4.1.9 Post Goods Issue 21](#_Toc232861317)

[4.1.10 Display Pallets Stock 23](#_Toc232861318)

[4.1.11 Create Billing Documents 23](#_Toc232861319)

[4.1.12 Create Attachment for Billing (Optional) 26](#_Toc232861320)

[4.1.13 Post Incoming Payment 27](#_Toc232861321)

[4.2 Delivery Process for Returnable Materials (Optional) 27](#_Toc232861322)

[4.2.1 Create Outbound Delivery without Order Reference (Optional) 27](#_Toc232861323)

[4.3 Return Process for Returnable Materials 28](#_Toc232861324)

[4.3.1 Create Pallets Return Sales Order 28](#_Toc232861325)

[4.3.2 Create Attachment for Sales Order (Optional) 29](#_Toc232861326)

[4.3.3 Post Goods Receipt 30](#_Toc232861327)

[4.3.4 Display Pallets Stock 32](#_Toc232861328)

[4.4 Return Process for Returnable Materials (Second Variant) 32](#_Toc232861329)

[4.4.1 Create Outbound Delivery w/o Order Reference 33](#_Toc232861330)

[4.4.2 Create Attachment for Delivery (Optional) 34](#_Toc232861331)

[4.5 Billing of Returnable Materials Which Were Not Returned 35](#_Toc232861332)

[4.5.1 Create Pallets Issue Order 35](#_Toc232861333)

[4.5.2 Post Goods Issue 37](#_Toc232861334)

[4.5.3 Create Billing Document 38](#_Toc232861335)

[4.5.4 Create Attachment for Billing (Optional) 39](#_Toc232861336)

[4.5.5 Post Incoming Payment 40](#_Toc232861337)

[4.5.6 Display Pallets Stock 41](#_Toc232861338)

[5 Appendix 42](#_Toc232861339)

[5.1 Process Integration 42](#_Toc232861340)

[5.1.1 Succeeding Processes 42](#_Toc232861341)

[5.2 Scheduling Job (alternative) 42](#_Toc232861342)

[5.2.1 Job Scheduling for Delivery Creation (Alternative) 42](#_Toc232861343)

[5.2.2 Job Scheduling for Goods Issue Deliveries (Alternative) 43](#_Toc232861344)

[5.2.3 Job Scheduling for Billing Creation (Alternative) 44](#_Toc232861345)

[5.2.4 Job Scheduling for Billing Release (Alternative) 45](#_Toc232861346)

[5.2.5 Job Scheduling for Billing Output (Alternative) 46](#_Toc232861347)

## Purpose

Overview

This scope item enables the shipping of standard pallets and their return. When you create a standard sales order, the delivery is automatically created based on this sales order. During the picking and shipping steps of this process, a pallet (returnable packaging) is added to the delivery. During the billing process, pallets can also be returned to manufacturers using a pallet return order with pallet return delivery and goods receipt, or a pallet return delivery without reference and goods receipt.

If customers do not return pallets, you can issue debit memo requests. Triggered by billing, the system issues debit memos based on such debit memo requests. Once this has been carried out, you can synchronize the consignment stock quantity and value, and then post a manual goods issue for the unreturned pallet.

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)no Serial no.; no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.no Serial no.; no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | RP001 | Empties,ND |  |
| Material | CM-FL-V00 | Forklift | Only use if you have activated the scope item Make-to-Order Production with Variant Configuration (1YT). |
| Sold-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Ship-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A |  |  |
| Shipping Point | 3310 |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| 65B | Create Product Master of type "Returnable Packaging" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | Material must be available in stock.For trading goods (HAWA) or returnable materials (LEIH), perform one of the following activities:Execute the Procurement without QM test script Procurement of Direct Materials(J45)Create stock using FLP Tile Post Goods Movement (for details see section Preliminary Steps). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS(BNZ) master data script. Posting Period is up to date. |

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

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| Sales Process Including Returnable Materials |  |  |  |
| [Display Pallets Stock](#unique_10) [page ] 11 | Warehouse Clerk | Display Stock Overview (MMBE) |  |
| [Create Sales Order](#unique_11) [page ] 12 | Internal Sales Representative | Manage Sales Orders - Version 2 (F3893) | Sales order saved demand created for MRP within delivery plant |
| [Create Attachment for Sales Order (Optional)](#unique_12) [page ] 14 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Delivery](#unique_13) [page ] 15 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Delivery created. |
| [Create Attachment for Delivery (Optional)](#unique_14) [page ] 17 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| [Add Delivery Item for Pallet](#unique_15) [page ] 18 | Shipping Specialist | Change Outbound Delivery (VL02N) |  |
| [Execute Picking](#unique_16) [page ] 19 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done |
| [Check Batches (Optional)](#unique_17) [page ] 20 | Shipping Specialist | Change Outbound Delivery (VL02N) | Batch numbers are assigned to the materials |
| [Post Goods Issue](#unique_18) [page ] 21 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. The system prints a delivery note. |
| [Display Pallets Stock](#unique_19) [page ] 23 | Warehouse Clerk | Display Stock Overview (MMBE) |  |
| [Create Billing Documents](#unique_20) [page ] 23 | Billing Clerk | Create Billing Documents (F0798) | Invoice created and posted in FI/CO |
| [Create Attachment for Billing (Optional)](#unique_21) [page ] 26 | Billing Clerk | Manage Billing Documents (F2250) | The attachment for billing is created. |
| [Post Incoming Payment](#unique_22) [page ] 27 |  |  |  |
| Delivery Process for Returnable Materials (Optional) |  |  |  |
| [Create Outbound Delivery without Order Reference (Optional)](#unique_23) [page ] 27 | Shipping Specialist | Create Outbound Delivery - Without Order Reference (VL01NO) |  |
| Return Process for Returnable Materials |  |  |  |
| [Create Pallets Return Sales Order](#unique_24) [page ] 28 | Internal Sales Representative | Manage Sales Orders (F1873) | Pallets return sales order created |
| [Create Attachment for Sales Order (Optional)](#unique_25) [page ] 29 | Internal Sales Representative | Manage Customer Returns (F1708) |  |
| [Post Goods Receipt](#unique_26) [page ] 30 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted. |
| [Display Pallets Stock](#unique_27) [page ] 32 | Warehouse Clerk | Display Stock Overview (MMBE) |  |
| Return Process for Returnable Materials (Second Variant) |  |  |  |
| [Create Outbound Delivery w/o Order Reference](#unique_28) [page ] 33 | Shipping Specialist | Create Outbound Delivery - Without Order Reference (VL01NO) | The pallet return delivery is created |
| [Create Attachment for Delivery (Optional)](#unique_29) [page ] 34 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| Billing of Returnable Materials Which Were Not Returned |  |  |  |
| [Create Pallets Issue Order](#unique_30) [page ] 35 | Internal Sales Representative | Manage Sales Orders (F1873) | Returnable packaging issue order is created. |
| [Post Goods Issue](#unique_31) [page ] 37 | Shipping Specialist | Change Outbound Delivery (VL02N) | The goods issue is posted. |
| [Create Billing Document](#unique_32) [page ] 38 | Billing Clerk | Create Billing Documents (F0798) | Billing document created |
| [Create Attachment for Billing (Optional)](#unique_21) [page ] 26 | Billing Clerk | Manage Billing Documents (F2250) | The attachment for billing is created. |
| [Display Pallets Stock](#unique_33) [page ] 41 | Warehouse Clerk | Display Stock Overview (MMBE) |  |

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

### Sales Process Including Returnable Materials

#### Display Pallets Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the pallet stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Stock Overview (MMBE). | The Stock Overview: Company Code/plant/Storage Location/Batch screen displays. |  |
| 3 | Enter Material Data | Make the following entries:Material : <Material Number> For example, RP001Plant: 3310Display Version: 01 | The Stock Overview: Basic List screen displays. |  |
| 4 | Choose Execute | Choose Execute. |  |  |

|  |
| --- |
| Note If you can't find Display Stock Overview app, open Show/Hide Group Panel in the SAP Fiori launchpad, choose Tile Catalog, and navigate to Display Stock Overview under Material Management - Warehouse Management and add it to My Home group. |

#### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a sales order for a customer and a standard product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). |  |  |
| 3 | Create Sales Order | On Manage Sales Orders - Version 2 screen, choose Create. | The Create Sales Order: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries and choose Create:Order Type: <Sales Order Type> For example, OR(Standard Order)Distribution Channel: 10Sales Organization: 3310Division: 00 |  |  |
| 5 | Enter Customer Information | Make the following entries:Sold-to Party: <Sold-to Party> For example, 33100001 |  |  |
| 6 | Enter Order Details | Make the following entries and choose Enter:Customer Reference: <Reference>Cust. Ref. Date: <Date>Material: <Material Number> For example, TG11Order Quantity: <Quantity> For example, 5Order Reason: <Order Reason>, for example, Good ServiceOptional: Item: 20, Material: RP001, Order Quantity: 4PC. |  |  |
| 7 | Save | Choose Save. | The standard sales order is saved.Note Please ignore any dialog boxes. |  |

|  |
| --- |
| Note If you have installed the scope item Rebate Processing: Free Goods in your system and you use material TG11 and customer 33100001, the following warning may appear: Minimum quantity 1.000 PC of free goods has not been reached. To skip this warning, choose Enter. |

Printing form - Output Management

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Order - Version 2 screen displays. |  |
| 3 | Search for Sales Order | Enter search term(s) in filter bar and choose GoFor example, enter sales order number in Sales Order field. | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Choose > on the right side of the Sales Order item and navigate to Display Standard Orders xxx: Overview screen. | The Display Sales Order xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Orders xxx: Overview screen, choose Extras > Output > Header > Edit . |  |  |
| 6 | Display Print Preview | On the Display Standard Orders xxx: Overview screen, choose Header Output Preview. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in the Manage Sales Orders - Version 2 (F3893) app:On the Manage Sales Order screen, enter search terms in filter bar and choose Go.In search result, choose your Sales Order Number, and choose More Links. |

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

This process step shows you how to create a delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries-From Sales Orders screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go :Shipping point: 3310Planned Creation Date: <Delivery selection date>Order: Sales order number created previously |  |  |
| 4 | Create Delivery | Select your sales order items and choose Create Deliveries. | A delivery is triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. A delivery is created successfully with delivery number shown on tab Deliveries. |  |

|  |
| --- |
| Note With the Analyze Outbound Delivery Logs app, you can display an overview about the logs of all delivery creation in system. You can search for logs according to different filter criteria, for example, Created by and additional settings. Detailed log information is listed via selecting the arrow on the right of each delivery log entry:If delivery is created successfully, delivery number is shown on tab Deliveries, else, you can display the exact message type, text and also the related sales document on tab Messages. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) | The Change Outbound Delivery (VL02N) screen displays |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the Delivery number and click Continue.From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Outbound Control . | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Delivery_Pick_List output type, and choose Display PDF Document. | A preview of the print document is displayed. |  |
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

#### Add Delivery Item for Pallet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to add a pallet item to the delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Outbound Delivery | Make the following entries and choose Enter:Outbound Delivery: <Outbound Delivery> |  |  |
| 4 | Enter delivery details | On the Delivery 8xxxxxx Change: Overview screen, on the Picking tab, make the following entries and choose Enter:Material: <Material number> RP001Plant: <Plant> For example, 3310Storage Location: <Storage location> For example, 331ADelivery Quantity: screen<Delivery Qty> For example, 3 |  |  |
| 5 | Save | Choose Save. | Pallets have been added to the delivery document. |  |

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
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: 3310Under the Picking Data tab, selectOnly Picking Without WM: X |  |  |
| 5 | Change Outbound Deliveries | Choose your delivery number, and choose Change Outbound Deliveries. |  |  |
| 6 | Check Batch Split | Choose the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 7 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to expand sub item(s), enter <quantity equal to Deliv. Qty> in Picked Qty field for sub item.If batch split doesn't exist, enter <quantity equal to Deliv. Qty> in Picked Qty field for picking related item(s). |  |  |
| 8 | Choose Enter | Choose Enter. |  |  |
| 9 | Save | Choose Save. | The delivery has been decided. |  |

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

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Make the following entries and choose ExecuteShipping Point: 3310 |  |  |
| 4 | Post Good Issue | Select your outbound delivery note, and choose Post Goods Issues.Select today’s date from the dialog box, and choose Continue. | A message confirms the goods issue has been posted. |  |

Financial Posting

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000Inv Chg COGS w/CE | 13600000Inventory TradingGd | none |

|  |
| --- |
| Note When the bundling functionality in context of IFRS15 is tested, the financial document in IFRS ledger (Ledger Group 2L) with the adjusted revenue amount displays.To check the financial document, use the Warehouse Clerk role, and access the Display Material Document List - Deprecated (MB51) app. |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery (VL03N) screen displays. |  |
| 3 | Issue Delivery Output | In the Outbound Delivery field, enter <Outbound Delivery Number>, and choose Continue.On the Delivery xxxxxxxx Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note, and choose Display Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Display Pallets Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the pallet stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Stock Overview (MMBE). | The Stock Overview: Company Code/plant/Storage Location/Batch screen displays. |  |
| 3 | Enter Material Data | Make the following entries:Material: <Material Number> For example, RP001Plant: <Plant>Display Version: 01 | The Stock Overview: Basic List screen displays. |  |
| 4 | Choose Execute | Choose Execute. |  |  |

|  |
| --- |
| Note If you can't find Display Stock Overview app, open Show/Hide Group Panel in the SAP Fiori launchpad, choose Tile Catalog, and navigate to Display Stock Overview under Material Management - Warehouse Management and add it to My Home group. |

#### Create Billing Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a billing document.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the right bottom of the screen.Keep the settings below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for billing list | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Choose Individual Billing Document | Select a row of delivery document created previously and choose button Create Billing Documents. | There is one window Create Billing Documents (F0798) displaying. |  |
| 6 | Maintain Billing Date | Choose Invoice (F2) billing type and maintain billing date, for example current date, then press button OK. | The draft billing document is created.Note The item with pallets is not relevant for billing, ignore the log information Item category LF CB10 cannot be invoiced with billing type F2. |  |
| 7 | Save Billing Document | On the Billing Document screen, click Save. The draft billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | Final billing document is generated. |  |

Financial posting:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 Rcvbls Domestic | 41000000 Rev Domestic Prod22000000 Output tax | none |

Manage billing documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797) under Sales > Billing Documents | The screen Manage Billing Document will display. |  |
| 2 | Search the billing document created in previous step | Input the Billing document number recorded in previous step. Choose Enter. | The billing document created in previous step will display. |  |
| 3 | Display the billing document | Select the billing document item, and choose Display. | The billing document shall be displayed. |  |
| 4 | Check Output Condition | On the Billing Document (F1901) screen, choose the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document (F1901) screen choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel Billing Docs | There is log display - Billing Document Canceled. |  |
| 7 | Update new Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing Save in the footer bar. |  |  |
| 8 | Update new Text (optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by pressing Save in the footer bar. |  |  |

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

#### Post Incoming Payment

Procedure

Complete all activities described in the test script of the scope item: Accounts Receivable (J59) (Chapter Posting Incoming Payments) using the master data from this document.

### Delivery Process for Returnable Materials (Optional)

In parallel with chapter [Sales Process Including Returnable Materials](#unique_35) [page ] 11, if pallets are sent to your customer without accompanying with goods , execute the following activities.

#### Create Outbound Delivery without Order Reference (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step can be used if the pallets are sent to customer without accompanying with goods. Technically speaking, the delivery type LO does not require an order to be created first before the delivery can take place. This process step shows you how to create outbound delivery without order reference.

Prerequisite

You can only send pallets to customer if you own enough of them.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Delivery - Without Order Reference (VL01NO). | The Create Outbound Delivery without Order Reference screen displays. |  |
| 3 | Enter Shipping Point | Make the following entries and choose Enter:Shipping Point: <Shipping Point> For example, 3310.Delivery Type: <LO> Delivery w/o Ref.Sales Organization: <Sales Organization> For example, 3310.Distribution Channel: <Distribution Channel>Division: <Division> |  |  |
| 4 | Enter Delivery Details | Make the following entries and choose Enter:Ship-to Party: <Ship-to party> For example, 33100001Planned GI: <Today's Date>Material: <Material number> For example, RP001Deli. Qty: <Quantity to be Delivered> For example, 1 |  |  |
| 5 | Post Goods Issue | Choose Post Goods Issue.Note Please ignore any pop-up information. |  |  |

### Return Process for Returnable Materials

#### Create Pallets Return Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a return sales order for pallets.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Documents screen displays. |  |
| 3 | Enter Sales Document Type | Make the following entries and choose Enter:Sales Document Type: <Sales order type> For example, CBG0 (Return pack./empties)Sales organization: <Sales organization>Distribution channel: <Distribution channel>Division: <Division> |  |  |
| 4 | Enter Order Details | Make the following entries and choose Enter:Sold-to party: <Sold to party> For example, 33100001Material : <Material number> For example, RP001Order Quantity: <Quantity> For example, 1 |  |  |
| 5 | Save | Choose Save.Note Please ignore any pop-up windows. | A return delivery document is created as well. |  |

#### Create Attachment for Sales Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to upload an attachment for a sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708). | The Manage Customer Returns screen displays. |  |
| 3 | Navigate to Display Return Order Screen | On the Manage Customer Returns screen, enter the respective order number created in previous step in the Customer Returns field and choose Go.Choose the return order line that displays. |  |  |
| 4 | Create Attachment | From the top menu bar, choose Services for Object and Create Attachment.Note If Services for Object does not display, select More to expand the dropdown list. | The Import file screen displays. |  |
| 5 | Import File | Choose OK in the File Upload pop-up screen.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on the top menu bar and choose Attachment List.Note If Services for Object does not display, select the More dropdown list. | Attachment shows up in the Service: Attachment list view. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Outbound Delivery Monitor screen displays. |  |
| 3 | Choose Goods Issue | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping point | Make the following entries and choose Execute:Shipping point: <Shipping point> For example,3310 |  |  |
| 5 | Post Goods Receipt | Mark the relevant delivery and choose post Good Issue . Select today’s date and choose Continue in the dialog box. | The goods receipt is posted |  |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N) | The Display Outbound Delivery (VL03N) screen displays |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery (VL03N) screen, enter the Delivery number and click Continue.From the Delivery xxxxxxxx Display: Overview screen, choose More > Extras > Delivery Output > Output Control | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery Note and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Display Pallets Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the pallet stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Stock Overview (MMBE). | The Stock Overview: Company Code/plant/Storage Location/Batch screen displays. |  |
| 3 | Enter Material number | Make the following entries:Material: <Material Number> For example, RP001Plant: <Plant>Display Version: 01 | The Stock Overview: Basic List screen displays. |  |
| 4 | Choose Execute | Choose Execute. |  |  |

|  |
| --- |
| Note If you can't find Display Stock Overview app, open Show/Hide Group Panel in the SAP Fiori launchpad, choose Tile Catalog, and navigate to Display Stock Overview under Material Management - Warehouse Management and add it to My Home group. |

### Return Process for Returnable Materials (Second Variant)

|  |
| --- |
| Note In parallel with chapter [Return Process for Returnable Materials](#unique_37) [page ] 28, if pallets are returned to your plant without first notifying by customer, execute the following activities. |

#### Create Outbound Delivery w/o Order Reference

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step can be used if the customer returns the pallet without first notifying the vendor of the return. Technically speaking, the delivery type CBG5 does not require that an order is first created before the return delivery can take place.

Prerequisite

You can only return pallets if the customer owns enough of them.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Delivery - Without Order Reference (VL01NO). | The Create Outbound Delivery Without Order Reference screen displays. |  |
| 3 | Enter Shipping Point | Make the following entries and choose Enter:Shipping Point: <Shipping Point> For example, 3310Delivery Type: CBG5Pallet returnsSales Organizaiton: <Sales Organization>For example, 3310Distribution channel: <Distribution Channel>Division: <Division> | The Pallet returns Create: Overview screen displays. |  |
| 4 | Enter Delivery Details | Make the following entries and choose Enter:Ship-to party: <Ship-to party> For example, 33100001Planned GI: <today's date> Pallet returnsMaterial : <Material Number> For example, RP001Deli.Qty: <Quantity to be returned> For example, 1 |  |  |
| 5 | Post Goods Receipt | Choose Post Goods Receipt (MIGO_GR).Note Please ignore any pop-up information. |  |  |

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

### Billing of Returnable Materials Which Were Not Returned

#### Create Pallets Issue Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a pallets issue order for unreturned pallets. The customer has not returned one or more pallets. The reason could be that they have been broken or simply forgotten.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Create Sales Order | On the Manage Sales Orders screen, choose Create, then choose Create Sales Order - VA01. |  |  |
| 4 | Enter the Order type CCLN (Ret. Packaging Issue) | On the Create Sales Order: Initial Screen, make the following entries and choose Continue:Order Type: CCLNSales Organization: 3310Distribution Channel: 10Division:00 |  |  |
| 5 | Enter Order Details | On the Create Sales Order: Overview screen, make the following entries:Sold to party: For example, 33100001Ship to party: For example, 33100001Cust. Reference: <PO number>Order reason: <Order Reason>Material Number: <Material number>, for example, RP001Quantity: <Quantity> | PO number: Enter a customer purchase order number as referenceOrder reason : for example, Excellent priceQuantity: for example, 1 PC |  |
| 6 | Save Document | Choose Save. Make a note of the sales order number: __________. The Delivery document number: __________.Note If you have installed the scope item Free Goods Processing in your system and you use material TG11 and customer 33100001, the following warning may appear: Minimum quantity 1.000 PC of free goods has not been reached. To skip this warning, choose Enter. | The order is saved and the order confirmation is printed out. Meanwhile，the Delivery document is automatically generated. |  |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Search for Sales Order | Enter search term(s) in filter bar and choose Go.For example, enter sales order number in field Sales Order. | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Click sales order number and choose Display Sales order. | The Display Sales Order xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Orders xxx: Overview screen, choose Extras > Output > Header > Edit . |  |  |
| 6 | Display Print Preview | On the Display Standard Orders xxx: Overview screen, choose Header Output Preview. | Preview for PDF document displays. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in app Manage Sales Orders (F1873):1. On Manage Sales Orders (F1873) screen, enter search terms in filter bar and choose Go.2. In search result, click your sales order number and choose Display Fact sheet. |

#### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery (VL02N) screen displays. |  |
| 3 | Change Outbound Delivery | Make the following entries and Choose Continue.Outbound Delivery: delivery number created previously | The Delivery XXX Change: Overviewscreen displays. |  |
| 4 | Post Good Issue | Choose Post Goods Issue | The goods issue is posted. |  |

#### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a billing document.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the right bottom bar.There are five settings, we should maintain these settings as bellow:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Select Item(s) for Billing | Select row(s) of delivery document created previously and choose button Create Billing Documents. | There is one window Create Billing Documents (F0798) displaying. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then choose OK button . | The draft billing document with ID Sxxxxxxxx will be displayed. |  |
| 7 | Save Billing Document | Save you entries. Make a note of the billing document number: __________. | The system generates an invoice for billing.Material : EMPTIES,ND (LEIH)Debited Accounts: 10100001; Rcvbls Domestic DE 1Credited Accounts: 41000000; Revenue Domestic - Product; 22000000; Output tax (MWS)Cost Element / CO Object: none |  |
| 8 | Access the App | Open Display Billing Document. | The Display Billing Document screen displays. |  |
| 9 | Enter Billing Number | In the Billing Document (F1901) field, enter the respective invoice number and choose Enter. | The Invoice xxx Display: Overview of Billing Items screen displays. |  |
| 10 | Check Output Condition | On the Invoice xxx Display: Overview of Billing Items screen choose MenuMore > Goto > Header > Output. | The Invoice XXX Display: Output screen displays. |  |
| 11 | Display Print Preview | On the Invoice xxx Display: Output screen select the line already created for the print output and choose Display PDF Document. | Preview for PDF document displays. |  |

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

#### Post Incoming Payment

Procedure

Complete all activities described in the test script of the scope item: Accounts Receivable (J59) (Chapter Posting Incoming Payments) using the master data from this document.

#### Display Pallets Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display the pallet stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Stock Overview (MMBE). | The Stock Overview: Company Code/plant/Storage Location/Batch screen displays. |  |
| 3 | Enter Material number | Make the following entries:Material : <Material Number> For example, RP001Plant: <Plant>Display Version: 01 | The Stock Overview: Basic List screen displays. |  |
| 4 | Choose Execute | Choose Execute. |  |  |

|  |
| --- |
| Note If you can't find Display Stock Overview app, open Show/Hide Group Panel in the SAP Fiori launchpad, choose Tile Catalog, and navigate to Display Stock Overview under Material Management - Warehouse Management and add it to My Home group. |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following test scripts:

| Scope Item | Business Condition |
| --- | --- |
| BKK - Sales Order Fulfillment Monitoring and Operations (optional) | Complete the following activities:Review Incomplete Sales OrdersReview Incomplete SD Documents (deliveries)Review Outbound Deliveries for Goods IssueReview List Blocked (for accounting) Billing Documents) |

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
> Flagged while digesting this document, not verified: The Purpose says unreturned pallets are handled with debit memo requests, debit memos and a manual goods issue after consignment stock synchronization, but the procedure uses a CCLN pallets issue order, VL02N goods issue and an F2 invoice, with no debit memo or consignment sync step.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Receivables account differs between the two billing sections: 12100000 Rcvbls Domestic in Create Billing Documents versus 10100001 Rcvbls Domestic DE 1 in the unreturned-pallets Create Billing Document, a German-named account in a UAE script; the 'separate billing document per item' setting is also ON in one and OFF in the other.

> [!warning] Conflict
> Flagged while digesting this document, not verified: The Overview Table names different apps than the procedures for some steps: sales order attachment lists Manage Sales Orders (F1873) but the procedure uses F3893, and the pallets return sales order lists F1873 but the procedure uses Create Sales Orders - VA01.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/test-script-sap-returnable-packaging-management-7ho-ae-1215]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDW_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 78,149 chars in the whole document
