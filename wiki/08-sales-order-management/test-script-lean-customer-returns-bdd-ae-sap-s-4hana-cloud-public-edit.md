---
id: 08-sales-order-management/test-script-lean-customer-returns-bdd-ae-sap-s-4hana-cloud-public-edit
title: "Test Script: Lean Customer Returns (BDD_AE) - SAP S/4HANA Cloud Public Edition (BDD_S4CLD2608_BPD_EN_AE)"
description: "SAP Best Practices test script (2608, AE country version) for scope item BDD Lean Customer Returns: returns order to credit memo steps, roles, data, limitations, jobs."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-returns-and-refunds]
aliases: [BDD_S4CLD2608_BPD_EN_AE]
keywords: [Customer Returns and Refunds, lean customer returns, scope item testing, returns order, returns delivery, goods receipt, billing block, credit memo billing, job scheduling, standard customer returns]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDD_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1252
topic: 08-sales-order-management/customer-returns-and-refunds
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Lean Customer Returns (BDD_AE) - SAP S/4HANA Cloud Public Edition (BDD_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDD_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Customer Returns and Refunds** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Lean Customer Returns (BDD_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861154)

[2 Prerequisites 4](#_Toc232861155)

[2.1 System Access 4](#_Toc232861156)

[2.2 Roles 4](#_Toc232861157)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861158)

[2.4 Business Conditions 6](#_Toc232861159)

[2.5 Preliminary Steps 7](#_Toc232861160)

[2.5.1 Create Condition Records (Optional) 7](#_Toc232861161)

[3 Overview Table 8](#_Toc232861162)

[4 Test Procedures 10](#_Toc232861163)

[4.1 Create Returns Order 10](#_Toc232861164)

[4.2 Create Attachment for Returns Order (Optional) 12](#_Toc232861165)

[4.3 Create Returns Delivery 13](#_Toc232861166)

[4.4 Create Attachment for Delivery (Optional) 14](#_Toc232861167)

[4.5 Post Goods Receipt 15](#_Toc232861168)

[4.6 Remove Billing Block 16](#_Toc232861169)

[4.7 Create Billing Document 17](#_Toc232861170)

[4.8 Create Attachment for Billing (Optional) 19](#_Toc232861171)

[5 Appendix 21](#_Toc232861172)

[5.1 Process Integration 21](#_Toc232861173)

[5.1.1 Succeeding Processes 21](#_Toc232861174)

[5.2 Limitations 22](#_Toc232861175)

[5.3 Scheduling Job (alternative) 23](#_Toc232861176)

[5.3.1 Job Scheduling for Delivery Creation (Alternative) 23](#_Toc232861177)

[5.3.2 Job Scheduling for Goods Issue Deliveries (Alternative) 24](#_Toc232861178)

[5.3.3 Job Scheduling for Billing Creation (Alternative) 25](#_Toc232861179)

[5.3.4 Job Scheduling for Billing Release (Alternative) 26](#_Toc232861180)

[5.3.5 Job Scheduling for Billing Output (Alternative) 27](#_Toc232861181)

## Purpose

Overview

The process starts with the creation of a lean returns order, optionally with reference to the original sales order or invoice. A returns delivery is created with reference to the lean returns order. When the products are shipped back, a goods receipt is posted to unrestricted-use stock. To compensate the customer, a credit memo is created manually or by the billing run.

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

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your S/4 HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

|  |
| --- |
| Note Additional Master Data (Default Values)You can test the scope item with other SAP Best Practices default values that have the same characteristics.Check your SAP system to find out which other material master data exists.Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning)no Serial no.; no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG12 | Trad.Good 12,Reorder Point,Reg.Trad.no Serial no.; no batch | See sections Business Conditions and Preliminary Steps. |
| Material | TG21 | Trad.Good 21,Reorder Point,Batch-FIFONo serial number, batch controlled (FIFO strategy) | Only use if you have activated the building block Batch Management (BLG) (BLH) (BLJ)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | TG22 | Trad.Good 22,Reorder Point,Batch-ExpDNo serial number, batch controlled (Exp. Date) | Only use if you have activated the building block Batch Management (BLG) (BLH) (BLJ)(BLP).See sections Business Conditions and Preliminary Steps. |
| Material | CM-FL-V00 | Forklift | Only use if you have activated the scope item Make-to-Order Production with Variant Configuration (1YT). |
| Sold-to party | 33100001 | Domestic UAE Customer 1 |  |
| Ship-to party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331R | Storage Location Returns |  |
| Shipping Point | 331R | Shipping Point 331R |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock or BDA - Free of Charge Delivery | To run through this scope item, you must already have sold some goods. |

### Preliminary Steps

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

## Overview Table

The scope item Lean Customer Returns consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Order](#unique_9) [page ] 10 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | Returns order is created. |
| [Create Attachment for Returns Order (Optional)](#unique_10) [page ] 12 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) |  |
| [Create Returns Delivery](#unique_11) [page ] 13 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | Returns delivery is created. |
| [Create Attachment for Delivery (Optional)](#unique_12) [page ] 14 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| [Post Goods Receipt](#unique_13) [page ] 15 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods receipt is posted for returns delivery.Note Goods is returned to unrestricted-use stock with schedule line WN (movement type 653) by default. You can use configuration step Assign Schedule Line Categories(SSCUI 105642） in Configure Your Solution or configuration activity Assign Schedule Line Categories in SAP Central Business Configuration to post return to blocked stock with schedule line DN (movement type 651) . |
| [Remove Billing Block](#unique_14) [page ] 16 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Billing block indicator is removed from returns order. |
| [Create Billing Document](#unique_15) [page ] 17 | Billing Clerk | Create Billing Documents - Billing Due List Items | Billing document is created. |
| [Create Attachment for Billing (Optional)](#unique_16) [page ] 19 | Billing Clerk | Manage Billing Documents (F0797) |  |

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

Prerequisites

You must have a reference invoice number and a billing document according to Sell from Stock (BD9).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01). | The Create Sales Orders screen displays. |  |
| 3 | Enter Sales Document Type | Make the following entries and choose Create with Reference:Sales Document Type: <sales order type>CBRESales Organization: 3310Distribution channel: 10Division: 00Note Alternatively, system supports to create returns order without reference: After entering necessary data on initial screen, choose Enter to directly navigate to Create Lean Return: Overview screen, skip next steps 4 and 5, enter other needed data besides those mentioned below.Sales Office: 330 | The Create with Reference dialog box displays. |  |
| 4 | Enter Reference Billing Document | Make the following entries and choose Item selection:Billing Document: <Billing document number to be referenced> | The Create with Reference screen displays. |  |
| 5 | Copy | Select the items to be referenced in which open quantity is not equal to ‘0’ and choose Copy: | The Create Lean Return: Overview screen displays. |  |
| 6 | Enter Order Details | Make the following entries:Order Reason: <Order Reason, such as Poor Quality.> |  |  |
| 7 | Enter Storage Location | Select the item, choose Display Item Detail.Navigate to Shipping tab.Enter 331R in Storage Location field to ensure that it is the correct storage for returned goods. |  |  |
| 8 | Maintain Batch Number | Only relevant for material TG21 and TG22:Double click the item and maintain the batch number on Sales A tab. |  |  |
| 9 | Save | Choose Save.Note Please ignore any dialog boxes. | The returns order has been created. |  |

|  |
| --- |
| Note If you have installed the Free Goods Processing (BKA) scope item in your system and you use material TG11 and customer 33100001, the following warning may appear: Minimum quantity 1.000 PC of free goods has not been reached. To skip this warning, choose Enter. |

### Create Attachment for Returns Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to upload an attachment for a returns order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Navigate to Display Returns Order Screen | Enter the returns order number created in previous step in the Returns Order field and choose Go.Choose the returns order line that displays. |  |  |
| 4 | Create Attachment | Choose Change.From the top menu bar, choose Services for Object and Create Attachment.Note If Services for Object does not display, select More to expand the dropdown list. | The Import file screen displays. |  |
| 5 | Import File | Choose OK in the File Upload pop-up screen.In the Open view, choose local path and file, and choose Open. | The attachment was successfully created. |  |
| 6 | Check Attachment | Choose Services for Object on the top menu bar and choose Attachment List.Note If Services for Object does not display, select the More dropdown list. | Attachment shows up in the Service: Attachment list view. |  |

### Create Returns Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Enter :Shipping Point: <Shipping point>, for example, 331RPlanned Creation Date: <Delivery selection date>Sales Document: <Returns order number created previously> |  |  |
| 4 | Create Delivery | Select your returns order and choose Create Deliveries. | A delivery is triggered to create. |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Logs screen displays.A delivery is created successfully with delivery number shown on Deliveries tab. |  |

|  |
| --- |
| Note With the Analyze Delivery Logs app, you can display an overview about the logs of all delivery creation in system. You can search for logs according to different filter criteria, such as created by or additional settings. You can see detailed log information through selecting the arrow on the right of each delivery log entry. If a delivery is created successfully, the delivery number is displayed on Deliveries tab. Otherwise, you can display the exact message type, text and the related sales document on Messages tab. |

### Create Attachment for Delivery (Optional)

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

### Post Goods Receipt

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

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Open Outbound Delivery Monitor | Choose For Goods Issue.Make the following entry, and choose Execute.Shipping Point: 331R |  |  |
| 4 | Post Goods Receipt | Mark the relevant delivery and choose Post Goods Issue.Select today’s date from the dialog box and choose Continue. | The goods receipt is posted. |  |

### Remove Billing Block

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove billing blocks from a returns order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Navigate to Display Lean Return Screen | Enter returns order number created in previous step in the Returns Order field, and choose Go.Choose the returns order line that displays. | The Display Lean Return XXXX: Overview screen displays. |  |
| 4 | Navigate to Change Lean Return Screen | Choose Change. | The Change Lean Return XXXX: Overview screen displays. |  |
| 5 | Remove Billing Block | On the Sales tab, remove Check Credit Memo in the Billing Block field, then choose Save. | Billing block is removed from the returns order. |  |

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to handle billing activity.

Procedures

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Setting.Maintain settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search Billing List | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Choose SD Document | Select the row of return delivery document created previously and choose Create Billing Documents. | The Create Billing Document screen displays. |  |
| 6 | Maintain Billing Type and Date | Choose billing type Credit Memo for Returns (CBRE) and maintain Billing Date, for example <current date>, then press OK. | The draft billing document is created. |  |
| 7 | Save Billing Document | In the Manage Billing Document screen, choose Save.The draft billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | ODN Number | Check whether the ODN number is generated for the billing document. | ODN number is generated in the Reference field. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41000000Rev Domestic Prod10100001 Rcvbls Domestic DE 1 |  | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Document screen displays. |  |
| 2 | Search for Billing Document | Enter the billing document number recorded previously in the Billing Document field, and choose Enter. | The billing document which create in previous step displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT |  |
| 5 | Display Print Preview | On the Billing Document screen, and choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Documentscreen, select certain billing document and choose Cancel Billing Document | There is a log display: Billing Document Canceled. |  |
| 7 | Update New Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing Save in the footer bar. |  |  |
| 8 | Update New Text (Optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by choosing Save in the footer bar. |  |  |

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

| Process | Business Condition |
| --- | --- |
| Accounts Receivable (J59) | Post the incoming payment.Using the master data from this document, complete the following activities described in the test script:Accounts Receivable(J59) (Section Post Incoming Payments) |
| Return to Supplier (BMK) (optional) | Dispose of the inventory by returning to the vendor. Do not process any other activities in this document after running the external process.Using the master data from this document, complete the following activities described in the test script:Return to Supplier (BMK) |
| Core Inventory Management(BMC) (Optional) | Returned material can be blocked or scrapped.Using the master data from this document, complete the following activities described in the test script:Core Inventory Management(BMC) |
| Rework Processing – Stock-Manufactured Material(BJN) (optional) | Rework activities and material postings after production execution for the original material (including goods receipt of the product) with an additional rework production order.Using the master data from this document, complete the following activities described in the test script:Rework Processing – Stock-Manufactured Material (BJN) |
| Sales Order Fulfillment Monitoring and Operations(BKK) (optional) | Collection of periodic activities such as day ending activities.Using the master data from bthis document, complete the following activities described in the test script:Sales Order Fulfillment Monitoring and Operations(BKK) (Sections on Review Sales Documents blocked for billing, Review Billing Due List, Review Log of collective invoice creation and Review List Blocked (for accounting) Billing Documents) |

### Limitations

Please consider a number of limitations in Lean Customer Returns(BDD) when using sales document type CBRE.

When running one of the outlined return process variants below please use Standard Customer Returns with sales document type CBAR, since Lean Customer Returns(BDD) is not supporting these:

- BKP: Customer Returns [sales document type: CBAR]
    - Return of trading goods with milestone-billing plan [item category: CBAO]
    - Return of make-to-order goods with milestone-billing plan [item category: CBTA]
    - Return of bought-in goods [item category: CBAB]
    - Return with selection of an alternative replacement material (and plant)
- 1Z3: Customer Returns with Direct Shipment from Customer to Supplier [sales document type: CBAR]
    - Direct return of 3rd party goods [item category: CB2, CB3, CB4]
- 3QD: Customer Returns Involving Supplier by Message Exchange [sales document type: CBAR]
    - Return of 3rd party goods [item category: CB2, CB3, CB4] via seller to supplier – using a Return Purchase Order with Return Material Authorization
- 3TE: Customer Returns for Non-Stock and Service Materials [sales document type: CBAR]
    - Return of non-stock goods [item category: TAX]
    - Return of non-stock goods with milestone-billing plan [item category: CTAX]
    - Return of free-of-charge non-stock goods [item category: TAXN]
    - Return of service [item-category: TAD] with Credit Memo in context of Return Order
    - Return of free-of-charge service [item category: TADN]
    - Return of service with milestone-billing plan [item category: CTAD]
- 2F4: Intercompany Process for Customer Returns [sales document type: CBAR]
    - Return and refunds using affiliated plants
- 5CX: Customer Returns for Sales Kits [sales document type: CBAR]
    - Return of ERLA goods [item categories: TAQ, TAQF, CBTQ]
    - Return of LUMF goods [item categories: TAP, TAPF, CBTP, TAPN]
    - Return of CPFH goods [item categories: CPHD, CFHD, CNHD, CMHD]
    - Return of DISH goods [item categories: FPHD, FBHD, FFOC]

Due to these limitations in BDD - Lean Customer Returns, it is recommended to directly start with standard customer returns. This also brings the advantage that the Sales & Refund clerk can decide on compensation options without waiting for inspection results..

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
> Flagged while digesting this document, not verified: Create Attachment for Delivery is listed in the Overview Table with app Display Outbound Delivery (VL03N), but the test procedure opens Change Outbound Delivery (VL02N).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Purpose says the returns order is created optionally with reference to the original sales order or invoice, and the Create Returns Order step notes it can be created without reference, yet that step's Prerequisites say you must have a reference invoice number and a billing document from BD9.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/customer-returns-bkp-ae-test-script-sap-s-4hana-cloud-public-edition-1]]
- related-to :: [[08-sales-order-management/customer-returns-for-non-stock-and-service-materials-3te-ae-test-scrip]]
- related-to :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]
- related-to :: [[08-sales-order-management/test-script-customer-returns-involving-supplier-by-message-exchange-3q]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDD_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 43,998 chars in the whole document
