---
id: 08-sales-order-management/customer-returns-for-non-stock-and-service-materials-3te-ae-test-scrip
title: "Customer Returns for Non-Stock and Service Materials (3TE_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3TE_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script 3TE_AE: returns order, goods receipt, refund determination, credit memo or replacement delivery for non-stock/service materials."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-returns-and-refunds]
aliases: [3TE_S4CLD2608_BPD_EN_AE]
keywords: [Customer Returns and Refunds, customer returns, returns order, refund determination, credit memo, replacement delivery, non-stock materials, goods receipt, billing documents, pro-forma invoice]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3TE_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-970
topic: 08-sales-order-management/customer-returns-and-refunds
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Customer Returns for Non-Stock and Service Materials (3TE_AE) - Test Script, SAP S/4HANA Cloud Public Edition (3TE_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3TE_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Customer Returns and Refunds** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Customer Returns for Non-Stock and Service Materials (3TE_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853664)

[2 Prerequisites 4](#_Toc232853665)

[2.1 System Access 4](#_Toc232853666)

[2.2 Roles 4](#_Toc232853667)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232853668)

[2.4 Business Conditions 6](#_Toc232853669)

[2.5 Preliminary Steps 6](#_Toc232853670)

[2.5.1 Create Condition Records (Optional) 6](#_Toc232853671)

[3 Overview Table 8](#_Toc232853672)

[4 Test Procedures 9](#_Toc232853673)

[4.1 Create Returns Order 9](#_Toc232853674)

[4.2 Post Goods Receipt (Statistical Confirmation) 12](#_Toc232853675)

[4.3 Determine Refund 13](#_Toc232853676)

[4.4 Display Returns Overview 14](#_Toc232853677)

[4.5 Refund Customer with Credit Memo (Option A) 15](#_Toc232853678)

[4.5.1 Create Credit Memo 15](#_Toc232853679)

[4.6 Refund Customer with Replacement Product (Option B) 17](#_Toc232853680)

[4.6.1 Create Free-of-Charge Delivery 17](#_Toc232853681)

[4.6.2 Post Goods Issue (Statistical Confirmation) 18](#_Toc232853682)

[4.6.3 Create Pro-forma Invoice 20](#_Toc232853683)

[4.6.4 Create Customer Invoice 21](#_Toc232853684)

[5 Appendix 24](#_Toc232853685)

[5.1 Process Integration 24](#_Toc232853686)

[5.2 Scheduling Job (Alternative) 24](#_Toc232853687)

[5.2.1 Job Scheduling for Delivery Creation (Alternative) 24](#_Toc232853688)

[5.2.2 Job Scheduling for Goods Issue Deliveries (Alternative) 25](#_Toc232853689)

[5.2.3 Job Scheduling for Billing Creation (Alternative) 26](#_Toc232853690)

[5.2.4 Job Scheduling for Billing Release (Alternative) 27](#_Toc232853691)

[5.2.5 Job Scheduling for Billing Output (Alternative) 28](#_Toc232853692)

[5.3 Succeeding Processes 29](#_Toc232853693)

## Purpose

Overview

A non-stock or service material can be used in the returns order. Non-stock and service materials are not included in inventory management. With creation of a returns delivery, the goods receipt is reflected by a confirmation posting. Non-stock and service items can be handled along with stock items in one returns order.

The user can influence when the refunding documents are created: either directly when releasing a returns order, or after materials are received physically. Finally, the user can decide on the compensation type for the customer: paying a credit memo or shipping a replacement.

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
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | NS0002 | Non-Stock Material 02 (No MRP planning)No serial number, no batch |  |
| Material | SM0001 | Service Material 01 |  |
| Sold-to Party | 33100003 | Domestic UAE Customer 3 |  |
| Ship-to Party | 33100003 | Domestic UAE Customer 3 |  |
| Payer | 33100003 | Customer domestic 03 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A331R |  |  |
| Shipping Point | 331A331R |  |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 31Y | Create Product Master of type "Non-Stock Material" - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2ET- Sales Order Processing for Non-Stock Material | Complete all activities described in test script 2ET using master data, which is listed in the previous section Master Data, Organizational Data, and Other Data and note down the created document numbers of sales order and billing document for further use. |
| 2EQ- Sale of Services | Complete all activities described in test script 2EQ using master data, which is listed in the previous section Master Data, Organizational Data, and Other Data and note down the created document numbers of sales order and billing document for further use. |
| BKJ- Sales Order Processing with Customer Down Payment | Complete all activities described in test script BKJ using master data, which is listed in the previous section Master Data, Organizational Data, and Other Data and note down the created document numbers of sales order and billing document for further use. |

### Preliminary Steps

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Order](#unique_9) [page ] 9 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Returns order is created, returns delivery is generated in the background. |
| [Post Goods Receipt (Statistical Confirmation)](#unique_10) [page ] 12 | Shipping Specialist | Change Outbound Delivery (VL02N) | The goods receipt (statistical confirmation) is posted for returns delivery. |
| [Determine Refund](#unique_11) [page ] 13 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Refund determination is checked or triggered. |
| [Display Returns Overview](#unique_12) [page ] 14 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Document flow is displayed. |
| Refund Customer with Credit Memo |  |  |  |
| [Create Credit Memo](#unique_13) [page ] 15 | Billing Clerk | Create Billing Documents (F0798) | Credit memo is created. |
| Refund Customer with Replacement Product |  |  |  |
| [Create Free-of-Charge Delivery](#unique_14) [page ] 17 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Replacement delivery is created. |
| [Post Goods Issue (Statistical Confirmation)](#unique_15) [page ] 18 | Shipping Specialist | Change Outbound Delivery (VL02N) | Goods issue (statistical confirmation) is posted for delivery. |
| [Create Pro-forma Invoice](#unique_16) [page ] 20 | Billing Clerk | Create Billing Documents (F0798) | Pro-forma invoice is created. |
| [Create Customer Invoice](#unique_17) [page ] 21 | Billing Clerk | Create Billing Documents (F0798) | Customer invoice is created. |

## Test Procedures

The test should take around 60 minutes. The Enterprise Search function provides a central entry point for finding business objects in your company from different sources using a single search request, such as Apps and fact sheets, for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

- Log on to the SAP Fiori launchpad using the respective user example, Internal Sales Representative.
- Access the Enterprise Search bar and choose the magnifying glass button in the upper right corner.
- The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your search criteria and choose the business object type. For example, select Customer Returns from dropdown menu in the first field, enter customer returns order number in the second field and choose Search. The sales order is listed.
- Choose the sales order number link, the system navigates to fact sheet screen and returns order related information is integrated and summarized on one Fiori page. You can get detailed data via choosing the corresponding links.

There are fact sheets available for the following objects (Visible depending on the assigned role):

- Sales (return) order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

This section describes test procedures for each process step that belongs to this scope item.

### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns order.

Prerequisite

You must have billing document or sales order as reference (refer to section Business Conditions).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Create Customer Return | Choose Create with Reference, then choose Create from Invoice.Note System also supports to create CBAR order for below cases:From sales order: click Create with Reference, then choose Create from Sales Order.From sales order without charge: click Create with Reference, then choose Create from Sales Order Without Charge.No Reference: click Create. | The Create from Invoice pop-up screen displays. |  |
| 4 | Enter Data | Enter the following data and then choose Select Items.Returns Order Type: Standard Return (CBAR)Invoice: Billing document number created previously |  |  |
| 5 | Maintain Return Quantity | Select the item(s) to be returned and enter the return quantity, then choose Continue. | New: Returns Order screen displays. |  |
| 6 | Maintain Data | Under tab General Information, enter the following data:Return Order Reason: for example, Standard Return(009)Under tab Items, choose the arrow button at the end of the item, and enter the following data.In section Product:Return Reason: for example, Product damaged (003)In section Follow-up Activity:Follow-up Activity: for example, Receive into Plant (0001) |  |  |
| 7 | Choose One of the Following Options | The user can influence the point in time when the refunding document is created: either immediately when the returns order is saved and released, or at a later point of time. Combination of the refund setting determines follow-up document creation. System provides four options for your reference. Choose one of the following options to continue:Note If your item category is RAXP - Ret NLAG FoC Proform, choose option 5 - No Refund directly. |  |  |
| 7a | Option 1: Execute Refund with Credit Memo Request Immediately | In the Refund section, enter the following data or action and choose Apply:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Create Credit Memo RequestChoose Save and Release. | Returns order is released.Returns delivery and credit memo request are generated automatically.Note If returns order workflow is activated, next need to perform returns order approval process, details refer to the chapter Process Returns Order Approval in test script BKP. |  |
| 7b | Option 2: Execute Refund with Replacement Order Immediately (Not relevant to service material SM0001) | In the Refund section, enter the following data or action and choose Apply:Refund Type: Replacement ProductRefund Control: Create Replacement OrderChoose Save.Refund Control: Create Replacement OrderChoose Save and Release. | Returns order is released.Returns delivery and Replacement Order are generated automatically. |  |
| 7c | Option 3: Refund on Hold, Choose Credit Memo as Temporary Refund Type | In the Refund section, enter the following data or action and choose Apply:Refund Type: Credit MemoRefund Code: 10%(select from dropdown list)Refund Control: Decide LaterChoose Save and Release. | Returns order is released.Returns delivery is generated automatically. |  |
| 7d | Option 4: Refund on Hold, Choose Replacement Product as Temporary Refund Type (Not relevant to service material SM0001) | In the Refund section, enter the following data or action and choose Apply:Refund Type: Replacement ProductRefund Control: Decide LaterChoose Save and Release. | Returns order is released.Returns delivery is generated automatically. |  |
| 7e | Option 5: No Refund | In the Refund section, make the following entry and choose Apply:Refund Control: No RefundChoose Save and Release. | Returns order is created.Returns delivery is generated automatically. |  |
| 8 | Check Process Flow | On the Manage Customer Returns - Version 2 screen, choose arrow at end of the item.Under the Process Flow tab, check dependent documents in process flow.Make a note of the follow-up document numbers for further use:__________. | The Display Returns Order screen displays.The dependent document(s) display(s). |  |

### Post Goods Receipt (Statistical Confirmation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the non-stock material is received physically, goods receipt is posted for returns delivery, statistical confirmation is generated. This process step shows you how to post a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Outbound Delivery Number | Make the following entry and choose Enter .Outbound Delivery: <delivery number created previously> |  |  |
| 4 | Post Goods Receipt | Choose Post Goods Receipt. | The goods receipt is posted, statistical confirmation is generated. |  |

### Determine Refund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, refund decision is made or checked: either refund the customer with a credit memo or compensate with a replacement product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order: <return sales order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Navigate to Determine Refund Screen | Select the returns order entry and choose Determine Refund. | The Determine Refund screen displays. |  |
| 5 | Check Refund Progress | In the upper area, check percentage number in the Refund Progressfield and then take next action accordingly:If <100%: Refund determination is not completed. Go to Section A and then Section B.If 100%: Refund determination is completed. Skip Section A and go to Section B. |  |  |
| Section A: Refund Determined with Reference to Material Inspection Results | Option 1: Credit Memo | On the Items to Be Refunded tab, choose Change Refund in the Refund Details column for the return item.Enter the following data:Refund Type: Credit MemoRefund Code: <10% Refund>Choose OK.Select the item and choose Release Selected Items. | Refund setting is maintained, and credit memo request document is created in background. |  |
| Section A: Refund Determined with Reference to Material Inspection Results | Option 2: Product Replacement (Not relevant to service material SM0001) | On the Items to Be Refunded tab, choose Change Refund in Refund Details column for the return item.Enter the following data:Refund Type: Replacement ProductReplacement Product: <Material>Supplying Plant: 3310Replacement Quantity: <Quantity> / PCChoose OK.Select the item and choose Release Selected Items. | Refund setting is maintained, and replacement order document is created in background. |  |
| Section B: Check Refund Determination Result | Check Refund Results | On the Completed Items tab, refund result is displayed. Follow-up document number is shown in Refund Details column. Make a note of document number for further use. You can click the created document number to check detailed information. | The refund result displays. |  |

### Display Returns Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the progress of return process. All dependent documents are available in process flow.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Order Overview | Choose the created returns order number 6XXXXXXX and choose Display Customer Return. | The Display Standard Return 6XXXXXXX: Overview screen displays. |  |
| 5 | Document Flow | On the Returns tab, choose Returns Overview in the Returns Control area. | The Returns Overview for Returns Order 6XXXXXXX - 10 screen displays. |  |
| 6 | Check Document Flow | In Document Number column, make a note of follow-up document number(s) of credit memo request or replacement order (subsequent delivery free of charge) for further use. |  |  |

After you have completed this activity:

Option A: If credit memo request is generated, go to the Refund Customer with Credit Memo chapter.

Option B: If replacement order is generated, go to the Refund Customer with Replacement Product chapter.

### Refund Customer with Credit Memo (Option A)

#### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a credit memo.

Procedure

Table 3: Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Click Billing Settings at the Header bar.Keep the settings below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) display(s) in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Date | Choose billing type Credit Memo (G2) and maintain billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Final credit memo is generated. |  |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search Billing Document | Enter the billing document number recorded previously in the Billing Document field, and press Enter. | The billing document which is created previously displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select a certain billing document and choose Cancel Billing Document. | A log displays the following message: Billing Document Canceled. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete and update the texts. Save your changes by choosing Save in the footer bar. |  |  |

### Refund Customer with Replacement Product (Option B)

|  |
| --- |
| Note This section is not relevant to service material SM0001. |

#### Create Free-of-Charge Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how a replacement delivery free of charge is created with reference to replacement order.

Prerequisite

Replacement order is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries - From Sales Orders screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date: <delivery selection date>Order: <replacement order number created previously> |  |  |
| 4 | Create Delivery | Select your items and choose Create Deliveries. |  |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on the Deliveries tab. |  |

#### Post Goods Issue (Statistical Confirmation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the non-stock replaced material is sent physically, goods issue is posted for free-of-charge delivery, statistical confirmation is generated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Outbound Delivery Number | Make the following entry.Outbound Delivery: <delivery number created previously> |  |  |
| 4 | Post Goods Issue | Choose Post Goods Issue. | The goods issue is posted, statistical confirmation is generated. |  |

Printing Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter <your delivery number> and choose Menu > Outbound Delivery > Issue Delivery Output. | The Output Details screen displays. |  |
| 4 | Print Preview | Select the line with output type Delivery Note and choose Print Preview. | A preview of the print document displays. |  |
| 5 | Print Delivery Note | From the preview of the document, choose Print. | The delivery note is printed. |  |

#### Create Pro-forma Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a pro-forma invoice with reference to delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Click Billing Settings.Keep the settings below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose the billing type Pro Forma Invoice for Delivery (F8) and billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Proforma invoice is generated. |  |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search for Billing Document | Input the pro-forma invoice number recorded in the previous step.Press Enter. | The billing document created in the previous step displays. |  |
| 3 | Display Billing Document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Update New Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Choose Save to save your changes in the footer bar. |  |  |
| 7 | Update New Text (optional) | In the Edit mode, you can add, delete, and update these texts. Choose Saveto save your changes in the footer bar. |  |  |

#### Create Customer Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, ‘F2’ type of invoice is created, and costs are transferred to accounting accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Click Billing Settings at the Header bar.Keep the settings below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Invoice (F2) and maintain Billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Customer invoice is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Non-stock mateial (NLAG) | 44910000Sales Deduction Domestic | 41910000Billed Revenue Domestic |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search the billing document created in previous step | Enter the invoice number recorded in the previous step.Press Enter. | The billing document created in the previous step displays. |  |
| 3 | Display the billing document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block, and choose Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Update New attachment (optional) | In the Edit mode, you can add, delete, and update the attachments. Choose Save to save your changes in the footer bar. |  |  |
| 7 | Update New Text (optional) | In the Edit mode, you can add, delete, and update these texts. Choose Save to save your changes in the footer bar. |  |  |
| 8 | Cancel Billing Document (Optional) | Select certain billing document and choose Cancel Billing Docs. | Log displayed: Billing Document Canceled. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

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

#### Job Scheduling for Billing Creation (Alternative)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can schedule a background job for creation billing documents.

This app can be used as an alternative instead of the manual creation of billing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule Billing Creation (F1519). | The Application Jobs screen displays. The app automatically shows the history of application jobs. |  |
| 3 | Create Billing Creation Schedule | Choose New to define a new job for billing creation. | The New Job screen displays. The Job Template should be defaulted as Schedule Billing Creation. |  |
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

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BKK-Sales Order Fulfillment Monitoring and Operations(Optional) | Using the master data from this document, complete the following activities described in the test script:Review sections: Incomplete SD Documents (Deliveries) and Review Outbound Deliveries for Goods Issue |

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
- related-to :: [[08-sales-order-management/customer-returns-bkp-ae-test-script-sap-s-4hana-cloud-public-edition-1]]
- related-to :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]
- related-to :: [[08-sales-order-management/test-script-customer-returns-involving-supplier-by-message-exchange-3q]]
- related-to :: [[08-sales-order-management/test-script-customer-returns-with-direct-shipment-from-customer-to-sup]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3TE_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 48,925 chars in the whole document
