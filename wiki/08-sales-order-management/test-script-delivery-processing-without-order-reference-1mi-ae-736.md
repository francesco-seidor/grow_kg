---
id: 08-sales-order-management/test-script-delivery-processing-without-order-reference-1mi-ae-736
title: "Test Script: Delivery Processing Without Order Reference (1MI_AE) (1MI_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 1MI: outbound delivery without order reference through picking, goods issue, POD and billing."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/delivery-without-order-reference]
aliases: [1MI_S4CLD2608_BPD_EN_AE]
keywords: [Outbound Delivery Without Order Reference, delivery without order reference, outbound delivery, picking, goods issue, proof of delivery, billing documents, pro forma invoices, freight costs, delivery split]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MI_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-736
topic: 08-sales-order-management/delivery-without-order-reference
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Delivery Processing Without Order Reference (1MI_AE) (1MI_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MI_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Outbound Delivery Without Order Reference** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Delivery Processing Without Order Reference (1MI_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847345)

[2 Prerequisites 4](#_Toc232847346)

[2.1 System Access 4](#_Toc232847347)

[2.2 Roles 4](#_Toc232847348)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847349)

[2.4 Business Conditions 6](#_Toc232847350)

[2.5 Preliminary Steps 7](#_Toc232847351)

[2.5.1 Set Initial Stock for Material 7](#_Toc232847352)

[2.5.2 Set Relevant for Proof of Delivery in BP Master Data 8](#_Toc232847353)

[3 Overview Table 10](#_Toc232847354)

[4 Test Procedures 12](#_Toc232847355)

[4.1 Create Delivery 12](#_Toc232847356)

[4.2 Create Attachment for Delivery (Optional) 14](#_Toc232847357)

[4.3 Enter Batch Number (Optional) 15](#_Toc232847358)

[4.4 Execute Picking 16](#_Toc232847359)

[4.5 Execute Packing (Optional) 17](#_Toc232847360)

[4.6 Split Outbound Delivery (Optional) 17](#_Toc232847361)

[4.7 Add Freight Costs (Optional) 18](#_Toc232847362)

[4.8 Posting Goods Issue 19](#_Toc232847363)

[4.9 Create Pro Forma Invoices (Optional) 21](#_Toc232847364)

[4.10 Proof of Delivery (Optional) 23](#_Toc232847365)

[4.11 Create Billing Documents 24](#_Toc232847366)

[4.12 Create Attachment for Billing (Optional) 26](#_Toc232847367)

[5 Appendix 28](#_Toc232847368)

[5.1 Process Integration 28](#_Toc232847369)

[5.1.1 Succeeding Processes 28](#_Toc232847370)

[5.2 Scheduling Job (alternative) 28](#_Toc232847371)

[5.2.1 Job Scheduling for Goods Issue Deliveries (Alternative) 28](#_Toc232847372)

[5.2.2 Job Scheduling for Billing Creation (Alternative) 29](#_Toc232847373)

[5.2.3 Job Scheduling for Billing Release (Alternative) 30](#_Toc232847374)

[5.2.4 Job Scheduling for Billing Output (Alternative) 31](#_Toc232847375)

## Purpose

Overview

The process begins with the creation of a standard delivery, assuming the necessary master data (such as the Business Partner for Customer) is already maintained. From this delivery document, a picking list is generated to prepare products for shipment.

For deliveries with batch-managed materials, a batch number can be assigned to each item. If items from different batches are used, delivery items can be split to accurately record quantities for each batch.

Delivery documents can be split into multiple deliveries to accommodate changes in transportation planning. Freight costs can also be added to ensure accurate invoicing.

After picking, the shipping specialist posts a goods issue to relieve inventory, recording the physical quantity shipped. This action also records the cost of goods sold in financial accounting.

Once inventory is relieved, the delivery can be invoiced. If a proof-of-delivery is required, the customer must confirm the delivered quantity. Invoicing is then based on these confirmed quantities, and both revenue and cost of goods sold are recorded in management accounting.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| Ariba Sourcing | Accessible from Ariba Sourcing. Your system administrator provides you with the URL and logon data to access the Ariba Sourcing. |
| System | Accessible from the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) | See sections Business Conditions and Preliminary Steps. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad. | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFO | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ) (BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpD | Only use if you have activated the building block Batch Management (BLG) (BLH)(BLJ) (BLP)..See sections Business Conditions and Preliminary Steps. |
| Sold-To Party | 3310000333100009 | Domestic UAE Customer 3Domestic UAE Customer 9 | You can test the scope item using another domestic customer.33100009 is for customer material record and POD (Proof-of-Delivery) |
| Ship-To Party | 3310000333100009 | Domestic UAE Customer 3Domestic UAE Customer 9 |  |
| Payer | 3310000333100009 | Customer domestic 03Domestic UAE Customer 9 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information about creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

The business process described in this Test Script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either:Run through the Procurement of Direct Materials processOr create stock using the SAP Fiori launchpad tile Post Goods Movement (for details see section Preliminary Steps). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting Period is up to date. |

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

#### Set Relevant for Proof of Delivery in BP Master Data

Purpose

In order to run step [Proof of Delivery (Optional)](#unique_9) [page ] 23, customer master data have to maintain POD relevant indicator. From demo data, only customer 33100009 has been set, following procedure can help user to set POD relevant for other customer master data if necessary.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto the SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the Role Master Data Specialist - Business Partner Data. |  |  |
| 2. | Access the App | Open Maintain Business Partner. |  |  |
| 3. | Enter Business Partner | On the entry screen of the Maintain Business Partner app, make the following entry and choose Enter.Business Partner : Customer ID |  |  |
| 4. | Switch to change mode | On screen Display Organization : XXXXXXXX, choose button Switch Between Display and Change. |  |  |
| 5. | Goto Sales Area – Shipping Tab | On screen Change Organization : XXXXXXXX, choose Customer (defined) in field Change in BP role.Choose Sales and Distribution .Then choose Shipping. |  |  |
| 6. | Set POD- Relevant | Select the checkbox of POD-Relevant. |  |  |
| 7. | Save | Choose Save. |  |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create Delivery](#unique_11) [page ] 12 | Shipping Specialist | Create Outbound Delivery - Without Order Reference (VL01NO) | An outbound delivery is created. |
| [Create Attachment for Delivery (Optional)](#unique_12) [page ] 14 | Shipping Specialist | Change Outbound Delivery (VL02N) | An attachment is added to the outbound delivery. |
| [Enter Batch Number (Optional)](#unique_13) [page ] 15 | Shipping Specialist | Change Outbound Delivery (VL02N) | Batch numbers are assigned. |
| [Execute Picking](#unique_14) [page ] 16 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking for an outbound delivery is completed. |
| [Execute Packing (Optional)](#unique_15) [page ] 17 | Shipping Specialist | Change Outbound Delivery (VL02N) | Packing results together with the outbound delivery is saved. |
| [Split Outbound Delivery (Optional)](#unique_16) [page ] 17 | Shipping Specialist | Split Outbound Delivery (VLSP) | An additional outbound delivery is created. |
| [Add Freight Costs (Optional)](#unique_17) [page ] 18 | Shipping Specialist | Change Outbound Delivery (VL02N) | Freight costs are added to the outbound delivery and will later be copied to the invoice. |
| [Posting Goods Issue](#unique_18) [page ] 19 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods issue is posted. |
| [Create Pro Forma Invoices (Optional)](#unique_19) [page ] 21 | Billing Clerk | Create Billing Documents (F0798) | A pro forma invoice is generated. |
| [Proof of Delivery (Optional)](#unique_9) [page ] 23 | Shipping Specialist | Change Outbound Delivery - Proof of Delivery (VLPOD) | Delivery is confirmed. |
| [Create Billing Documents](#unique_20) [page ] 24 | Billing Clerk | Create Billing Documents (F0798) | A billing document is created. |
| [Create Attachment for Billing (Optional)](#unique_21) [page ] 26 | Billing Clerk | Manage Billing Documents (F0797) | An attachment is added to the billing document. |

## Test Procedures

This section describes procedures for each process step that belongs to this scope item.

By using a single search request, the enterprise search function provides a central entry point for finding business objects from different sources within your company. You can search for objects such as apps or object pages for business objects. From the data found, you can go directly to the respective apps and object pages to display, edit the data, or find related objects.

How to access and check an object page:

1. Log on to the SAP Fiori Launchpad using the respective user, for example, Shipping Specialist.
2. To access the enterprise search, choose the magnifying glass in the upper right corner.
3. The enterprise search bar is displayed with two filter fields to the left of the search button. Enter your search criteria and choose the business object type, for example, choose Deliveries from the drop-down menu in the first field, enter the delivery number in the second field, and then, choose Search. The delivery you searched for should be listed.
4. Once you choose the delivery number link, the system navigates to the object page screen where delivery related information is displayed and summarized on one Fiori page, You can display more detailed data by choosing the available links.

There are object pages available for the following objects: (Visible depending on the assigned role)

- Outbound Delivery
- Returns Delivery
- Customer
- Material
- Purchase Order
- Purchase Requisition Item
- Sales Order
- Supplier

### Create Delivery

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
| Note For executing packing, Create Product Master of Type "Packaging" - MDS (3Y1) master data script is the prerequisite. For more information on creating packing related master data, please check this test script.For detailed information about handling unit management, you can also refer to:[https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD) to visit Product Assistance. Choose English and navigate by: Supply Chain > Logistics Cross Topics > Handling Unit Management . |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Delivery - Without Order Reference (VL01NO). | The Create Outbound Delivery Without Order Reference screen displays. |  |
| 3 | Enter Key Data for Outbound Delivery Creation | On the Create Outbound Delivery Without Order Reference screen, make the following entries, and choose Continue:Shipping Point: 3310Delivery Type: LOSales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 4 | Enter Delivery Details | On the Delivery without Reference Create: Overview screen, make the following entries:Ship-to Party: 33100003Planned GI: <Planned goods movement date>, for example, <Today's Date>Material Number: <Material number>Deliv. Quantity: Quantity , For example, 1 PCNote If any warning pop up comes, please ignore it. |  |  |
| 5 | Save Document | Choose Save Document.Make a note of the delivery number: __________. | An outbound delivery is created. |  |

Depending on the scope item settings, the stock availability is checked at delivery creation using the available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities, and therefore the picking process cannot start. As soon as there is sufficient stock for delivery creation, the system creates a delivery and the picking process can start.

To avoid open deliveries, ensure that there is sufficient inventory quantity at the time of delivery creation. Additionally, you can restrict the creation of deliveries with no confirmed quantities by:

- Increasing the replenishment lead time that is used during the availability check (has to be larger than the selection period used for delivery creation).
- Changing the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries can be saved.
- Changing the customization settings for the used delivery item category. The Check quantity 0 field must be adapted to B = Situation rejected with an error message.

With the Analyze Outbound Delivery Logs app, you can display, in a log, an overview of all the deliveries that have been created in your system. You can filter by Created By and other additional settings. If you select the arrow on the right of each delivery log entry you can display the exact message type and text.

### Create Attachment for Delivery (Optional)

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
| 1 | Log On | Logon to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter the Outbound Delivery Number | On the Change Outbound Delivery screen, enter the outbound delivery number created in previous step and choose Continue. | The Change Outbound Delivery xxx: Overview screen displays. |  |
| 4 | Create Attachment for Delivery | Choose Services for Object on top right corner of screen, and then choose Create Attachment. | The Import file screen displays . |  |
| 5 | Import File | Choose OK in the File Upload pop-up screen.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on top right corner of screen, and then choose Attachment list. | Attachment brings up the Service: Attachment list screen. |  |

### Enter Batch Number (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the batch number assignment to the materials.

Prerequisite

Use this step if batch management is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter the Outbound Delivery Number | On the Change Outbound Delivery screen, enter the outbound delivery number and choose Continue. |  |  |
| 4 | Enter the Batch Number | In the Batch field, enter the batch number. | Batch numbers are assigned to the materials. |  |
| 5 | Save Document | Choose Save. |  |  |

### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area, where these goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Open Outbound Delivery Monitor | On the Manage Outbound Deliveries – VL06O screen, choose For Picking. | The Manage Outbound Deliveries – VL06O screen displays. |  |
| 4 | Enter Shipping Point | On the Outbound Deliveries for Picking screen, make the following entry:Shipping Point: 3310 |  |  |
| 5 | Select the Only Picking without WM checkbox and choose Execute | Select the Only Picking without WM checkbox and choose Execute. |  |  |
| 6 | Select the Outbound Delivery | On the Day's Workload for Picking screen, select your outbound delivery and choose Change Outbound Deliveries. |  |  |
| 7 | Input Picked Quantity | On the Delivery xxxxxxxx change: Overview screen, choose the Picking tab, and input a quantity in the Picked Qty field.Picking status is set to complete if the picked quantity and the delivery quantity are equal. Deviations in quantity can be solved by choosing Copy Picked Quantity as Delivery Quantity.When using the material with batch management, for example: TG21 or TG22, choose Batch Split Exists first, then input the quantity in the second line in the Picked Qty field. |  |  |
| 8 | Save Document | Choose Save. | Picking for the outbound delivery is completed. |  |

### Execute Packing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute packing for delivery items right in an outbound delivery.

Procedure

Complete all the activities related to outbound delivery in the test script of Handling Unit Management (4MM) scope item.

Depending on your settings in the section Configure Delivery Item Generation for Packaging Material (Optional) of test script 4MM Handling Unit Management, packaging material might be automatically generated as delivery items.

### Split Outbound Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the user can split up single or multiple items from an existing, completely picked outbound delivery and move them to a new delivery document before posting goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Split Outbound Delivery (VLSP). | The Split Outbound Delivery screen displays. |  |
| 3 | Enter Shipping Point | On the entry screen of the Split Outbound Delivery app, make the following entry:Shipping Point: 3310 |  |  |
| 4 | Enter Outbound Delivery | To speed up selection, make the following entry on the same screen:Outbound Delivery: [your Outbound Delivery Document Number] |  |  |
| 5 | Choose Split Profile | In the Split Profile field, make the following entry or select the following value from the list:Split Profile: 0003 (Delivery Split - LE Components) |  |  |
| 6 | Start Selection | Choose Run. | A list of outbound delivery items for the selected shipping point and outbound delivery is displayed. |  |
| 7 | Select Items for Split | Select the items that should become part of a new delivery or that should be split from the current delivery.Enter the <Split Quantity> and choose Save Split. | The selected items are displayed with a new delivery document number. The items not selected for the split still appear with the former document number. |  |

### Add Freight Costs (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After picking, you may want to add the actual freight costs to the outbound delivery if you know the exact weights and freight charges.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter the Outbound Delivery Number | On the Change Outbound Delivery screen, enter the outbound delivery number and choose Continue. |  |  |
| 4 | Enter the Freight Costs | From the menu, choose Goto > Header > Conditions .In the Condition Type column, enter YBHD.In the Amount column, enter the freight costs, such as 100 EUR.Note You can only add additional delivery costs at the delivery header level.The system distributes the entered amount across the delivery items.The distribution is executed based on the net weight of each item. This includes automatically generated delivery items for packaging materials if any exist. |  |  |
| 5 | Save Your Outbound Delivery | Save your outbound delivery. | Freight costs are added to the outbound delivery and will later be copied to the invoice. |  |

### Posting Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries – VL06O screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue. Make the following entry and choose Execute.Shipping Point: 3310 |  |  |
| 4 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date from the dialog box. | The goods issue is posted. |  |

Table 2: Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory Trading Gd | none |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Issue Delivery Output | On the Delivery Output Delivery screen, enter <delivery number> and choose Continue.On the Delivery w/o Ref. xxxxxxx Display: Overview screen, choose Extras > Delivery Output > Output Control. | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery w/o Ref. : Output screen, choose the line with Delivery Note output type, and choose Display Document. | A preview of the print document displays. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

### Create Pro Forma Invoices (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create pro forma invoices with reference to delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings, and make the following entries:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: ONAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery item to be billed and select quantities: OFFChoose OK. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales documents are displayed in the results. |  |
| 5 | Choose Individual Billing Document | Select the row of the delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Set the Billing Type to Pro Forma Invoice for Delivery (F8) and specify a billing date, such as the current date, and then choose OK. | The draft billing document with ID TMPxxxxxxxx is displayed. |  |
| 7 | Check the Billing Document | If you created items for the billable package materials, you can view the header level pricing on the Pricing Elements tab.Choose the arrow icon (>) to the right of an item on the Items tab, and view item level pricing on the Pricing Elements tab.If you added Freight Costs, you can view the distributed costs at the item level.If a non-billable packaging material is generated as a delivery item, you can find some difference in the total Freight Costs between the delivery document and the billing document. This is because the costs allocated on the non-billable packaging material cannot be billed. |  |  |
| 8 | Save Billing Document | On the Pro Forma Invoice for Delivery screen, choose Save.The draft billing document with ID TMPxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | A pro forma invoice is generated. |  |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search for the Billing Document | Input the pro forma invoice number recorded in the previous step.Press Enter. | The billing document created in the previous step is displayed. |  |
| 3 | Display the Billing Document | Select the billing document item and choose Display. | The billing document details are displayed. |  |
| 4 | Check Output Condition | On the Manage Billing Documents screen, choose the last tab, Output Items. | There is one item row with the output type BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Manage Billing Documents screen, choose Preview. | The preview of a PDF document is displayed. |  |
| 6 | Update Attachments (Optional) | In the Edit mode, you can add, delete, or update the attachments. Choose Save to save your changes. |  |  |
| 7 | Update Texts (Optional) | In the Edit mode, you can add, delete, or update the texts. Choose Save to save your changes. |  |  |

### Proof of Delivery (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this test procedure, the user can record the quantity of goods that was actually delivered, as confirmed by the customer. This information ensures that the user bills the customer for the correct amount of goods. This is only possible for outbound deliveries where the customer master data has been maintained so that it is "POD-relevant" (on sales area level).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Change Outbound Delivery - Proof of Delivery (VLPOD). | The POD - Change Outbound Delivery screen displays. |  |
| 3 | Enter Outbound Delivery | On the entry screen of the app, make the following entry:Outbound Delivery: [your Outbound Delivery Document Number] and choose Continue. | The selected outbound delivery document is displayed and the Overview POD tab is opened. |  |
| 4 | Customer Reports Different Quantity | If there is a quantity difference between shipping and receiving, go to step 5 and 6. |  |  |
| 5 | Enter Reason for Variance in POD Delivery (optional) | In the line of the item for which a differing quantity was reported by the customer, make the following entry or select the following value from the list:Reason: DFG2 (Under delivery, reason unknown) |  |  |
| 6 | Enter Deviation in Quantity Actually Delivered (optional) | In the Quantity Difference field in Sales Unit (QtyDiffinSalesUn), enter the respective quantity that differs from the expected delivery quantity and choose Enter. | The quantity displayed for the respective item in the field POD quantity has been recalculated (Quantity Difference subtracted from Delivery Quantity), and value for the field POD Status has changed to B (Differences reported). |  |
| 7 | Confirm Proof of Delivery | Choose Confirm Proof of Delivery. | The POD Date field has been filled with the current date, and the value for the POD Status field has changed to C (Confirmed). |  |
| 8 | Save Outbound Delivery Document with Proof of Delivery | Choose Save. | The outbound delivery document is saved with confirmation for actually delivered quantities. These will be used for the consecutive billing step. |  |

### Create Billing Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle the billing.

Create Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Settings | Choose Billing Settings in the upper right corner of the screen, and make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery item to be billed and select quantities: OFFChoose OK. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales documents are displayed in the results. |  |
| 5 | Choose Individual Billing Document | From the list, select the delivery you previously created and choose Create Billing Documents. | The Create Billing Documents window displays. |  |
| 6 | Maintain Billing Date | Choose Billing Type Invoice (F2) and maintain the billing date, for example current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx is displayed. |  |
| 7 | Check the Billing Document | If you created items for the billable package materials, you can view the header level pricing on the Pricing Elements tab.Choose the arrow icon (>) to the right of an item on the Items tab, and view item level pricing on the Pricing Elements tab.If you added Freight Costs, you can view the distributed costs at the item level.If a non-billable packaging material is generated as a delivery item, you can find some difference in the total Freight Costs between the delivery document and the billing document. This is because the costs allocated on the non-billable packaging material cannot be billed. |  |  |
| 8 | Save Billing Document | On the Manage Billing Documents screen, choose Save.The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number : _____________________ | The system generates an invoice for billing. |  |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | Input the billing document number recorded in the previous step. Press Enter. | The billing document created in the previous step is displayed. |  |
| 3 | Display the Billing Document | Select the billing document item, and choose Display. | The billing document is displayed. |  |
| 4 | Check Output Condition | On the Manage Billing Documents screen, choose the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT |  |
| 5 | Display Print Preview | On the Manage Billing Documents screen, choose Preview. | A preview of a PDF document is displayed. |  |
| 6 | Cancel Billing Document (Optional) | Choose Cancel Billing Document. | The billing document is canceled. |  |
| 7 | Update Attachments (Optional) | In the Edit mode, you can add, delete, or update the attachments. Save your changes by choosing Save on the footer bar. |  |  |
| 8 | Update Texts (Optional) | In the Edit mode, you can add, delete, or update these texts. Save your changes by choosing Save on the footer bar. |  |  |

### Create Attachment for Billing (Optional)

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

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| J59- Accounts Receivable | Posting a Customer Invoice in Accounting, etc. Using the master data from this document, complete the following activities described in the test script:Posting a Customer Invoice in AccountingOverdue Receivables, Display Customer BalancesManage Customer Line Items |
| BKK – Sales Order Fulfillment Monitoring and Operations | This scope item describes the collection of periodic activities, such as day ending activities or legal requirements.Using the master data from this document, complete all the activities described in the test script of Sales Order Fulfillment Monitoring and Operations (BKK) scope item (Chapters Review Billing Due List, Review Log of collective invoice creation Review List Blocked (for Accounting) Billing Documents). |

### Scheduling Job (alternative)

#### Job Scheduling for Goods Issue Deliveries (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for goods issue posting regarding outbound deliveries.

This app can be used as an alternative instead of the manual goods issue posting for outbound deliveries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Shipping Specialist. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule Goods Issue for Deliveries. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Goods Issue Deliveries Schedule | Choose New to define a new job. | The New Job screen is displayed. Job Template should default as Schedule Goods Issue for Deliveries. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A schedule goods issue for delivery job is scheduled. Returns to Application Jobs screen. |  |
| 6 | Check Goods Issue Deliveries Job Log | In the Application Jobs screen, after the job item's status has changed to Finish, choose Status symbol in the Log column.Note To refresh the job list, choose Magnifier. | Screen goes to job log details. |  |

#### Job Scheduling for Billing Creation (Alternative)

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
| 1 | Log On | Log on to the SAP Fiori Launchpad using role Billing Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose New to define a new job for billing creation. | The New Job screen is displayed. Job Template should default as Schedule Billing Creation. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing creation job is scheduled. Returns to Application Jobs screen. |  |
| 6 | Check Billing Creation Job Log | In the Application Jobs screen, after the job item’s status has changed to Finish, choose Job Log.Note To refresh the job list, choose Magnifier. | Screen goes to log details. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using role Billing Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Release. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Release Schedule | Choose New to define a new job for billing creation. | The New Job screen is displayed. Job Template should default as Schedule Billing Release. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Returns to Application Jobs screen. |  |
| 6 | Check Billing Release Job Log | In the Application Jobs screen, after the job item’s status has changed to Finish, choose Job Log.Note To refresh the job list, choose Magnifier | Screen goes to log details. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using role Billing Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Output. | The Application Jobs screen is displayed. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Output Schedule | Choose New to define a new job for billing creation. | The New Job screen is displayed. Job Template should default as Schedule Billing Output. |  |
| 4 | Job Parameters | Define scheduling options and parameters for the batch job if necessary, then choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 5 | Schedule | Choose Schedule. | A billing release job is scheduled. Returns to Application Jobs screen. |  |
| 6 | Check Billing Output Job Log | In the Application Jobs screen, after the job item’s status has changed to Finish, choose Job Log.Note To refresh the job list, choose Magnifier. | Screen goes to log details. |  |

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
- see-also :: [[11-inventory-warehouse-and-transportation/sap-ewm-integration-outbound-processing-to-customer-2vk-ae-test-script]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MI_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 54,371 chars in the whole document
