---
id: 08-sales-order-management/sales-processing-using-third-party-without-shipping-notification-bdk-a
title: Sales Processing Using Third-Party Without Shipping Notification (BDK_AE) - Test Script (BDK_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for scope item BDK: third-party sales order, requisition, PO, supplier invoice and billing, with roles and steps."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/third-party-sales]
aliases: [BDK_S4CLD2608_BPD_EN_AE]
keywords: [Third-Party Sales Processing, third-party sales, sales order creation, purchase requisitions, purchase order approval, supplier invoice, billing documents, flexible workflow, pro forma invoice, purchasing info record]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDK_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1255
topic: 08-sales-order-management/third-party-sales
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sales Processing Using Third-Party Without Shipping Notification (BDK_AE) - Test Script (BDK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Third-Party Sales Processing** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Sales Processing Using Third-Party Without Shipping Notification (BDK_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Sales Processing Using Third-Party Without Shipping Notification (BDK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861269)

[2 Prerequisites 4](#_Toc232861270)

[2.1 System Access 4](#_Toc232861271)

[2.2 Roles 4](#_Toc232861272)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861273)

[2.4 Business Conditions 7](#_Toc232861274)

[2.5 Preliminary Steps 7](#_Toc232861275)

[2.5.1 Check Flexible Workflow for Purchase Order Approval 7](#_Toc232861276)

[2.5.2 Configure Flexible Workflow for Purchase Order 9](#_Toc232861277)

[2.5.3 Create Purchasing Info Record 10](#_Toc232861278)

[2.5.4 Create Condition Records (Optional) 11](#_Toc232861279)

[3 Overview Table 12](#_Toc232861280)

[4 Test Procedures 13](#_Toc232861281)

[4.1 Sales Inquiry (1IQ) (Optional) 13](#_Toc232861282)

[4.2 Sales Contract Management (I9I) (Optional) 14](#_Toc232861283)

[4.3 Sales Quotation (BDG) (Optional) 14](#_Toc232861284)

[4.4 Create Sales Order 15](#_Toc232861285)

[4.5 Process Sales Order Approval (Optional) 17](#_Toc232861286)

[4.6 Create Attachment for Sales Order (Optional) 17](#_Toc232861287)

[4.7 Change Order Quantity (Optional) 18](#_Toc232861288)

[4.8 Credit Management Check for Sales Order (Optional) 19](#_Toc232861289)

[4.9 Display List of Purchase Requisitions to be Assigned 20](#_Toc232861290)

[4.10 Convert Assigned Requisitions to Purchase Orders 21](#_Toc232861291)

[4.11 Approve and Release Purchase Order (Optional) 22](#_Toc232861292)

[4.12 Create Supplier Invoice 23](#_Toc232861293)

[4.13 Accounts Payable (Optional) 25](#_Toc232861294)

[4.14 Create Pro Forma Invoice - for Free of Charge Items (Optional) 26](#_Toc232861295)

[4.15 Create Billing Document 27](#_Toc232861296)

[4.16 Create Attachment for Billing (Optional) 29](#_Toc232861297)

[5 Appendix 31](#_Toc232861298)

[5.1 Process Integration 31](#_Toc232861299)

[5.1.1 Succeeding Processes 31](#_Toc232861300)

[5.2 Relevant Processes 31](#_Toc232861301)

[5.3 Scheduling Job (alternative) 33](#_Toc232861302)

[5.3.1 Job Scheduling for Billing Creation (Alternative) 33](#_Toc232861303)

[5.3.2 Job Scheduling for Billing Release (Alternative) 34](#_Toc232861304)

[5.3.3 Job Scheduling for Billing Output (Alternative) 35](#_Toc232861305)

## Purpose

Overview

This scope item enables you to automatically create a purchase requisition for the materials to be delivered by the third-party vendor. The incoming invoice from the vendor updates the billing quantity. You can only create the customer billing document after entering the invoice from the vendor.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/BDK_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
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
| Material | TG13 | Trading Good for Regular Trading (reorder point planning) with item category group CBNAno batch |  |
| Sold-to party | 33100001 | Domestic UAE Customer 1 | You can test the test script using another domestic customer. |
| Ship-to party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Vendor | 3330000133300002 | Domestic UAE Supplier 1Domestic UAE Supplier 2 |  |
| Plant | 3310 |  |  |
| Storage Location | 331A |  | w/o lean WM |
| Shipping Point | 3310 |  |  |
| Sales organization | 3310 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |
| Company Code | 3310 |  |  |
| Currency | AED |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS– MDS |
| BND | Create Customer Master - MDS– MDS |
| BNE | Create Supplier Master - MDS– MDS |

### Business Conditions

The business process described in this Test Script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS(BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Check Flexible Workflow for Purchase Order Approval

Purpose

In this procedure, you check the flexible workflow for purchase order approval.

When you use the flexible workflow to approve the purchase order, make sure Flexible Workflow for Purchase Order with NB document is activated, and Flexible Workflow for Purchase Order Approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen is displayed. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution: Realize Phase screen, search Activate Flexible Workflow for Purchase Orders, then choose Search.Select the line of the item and go to the next screen.On the Configure Your Solution - Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen is displayed. |  |
| 5 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Check Flexible Workflow for PO Approval | Verify the following entries:Purchasing Doc. Type: NBScenario based workflow: <Selected> | The Scenario based workflow is active for Purchase Orders with Document Type: NB. |  |

Result

The Scenario based workflow is active for Document Type: NB.

#### Configure Flexible Workflow for Purchase Order

Purpose

This process step shows you how to configure release conditions for Purchase Order Approval.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872) . | The Manage Workflows screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Add and make the following entries:Name: Test Workflow for Purchase OrderIn the START Condition area select Purchasing group of purchase order is and enter 003 value:Choose Add alternative conditions and make the following entries:Choose Total net amount of purchase order is greater thanPurchaseOrderTotalNetAmount: For example, 10PurchaseOrderCurrency: AEDIn STEP SEQUENCE area, choose Add and make the following entries:Type: Release of Purchase OrderIn RECIPIENTS area:Assignment By: UserUser: Select User with Purchasing_manager from F4 help.Step to be completed by: One of the recipients.Choose Add.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The Workflow Item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow Automatic Release of Purchase Order has been activated. |

#### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Purchase Info Record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Purchaser. | The SAP Fiori launchpad displays. |  |
| 3 | Open Create Purchasing Info Records | Choose the Create Purchasing Info Record (ME11). | The Create Info Record: Initial Screen displays. |  |
| 4 | Enter Data | Make the following entries:Supplier: 33300001 / 33300002Material: TG13Purchasing Organization: 3310Plant: 3310And press Enter. | The Create Info Record: General Data screen displays. |  |
| 5 | EnterPurchasing Data | Choose Purch. Org. Data 1, then make the following entries:Delivery Time in Days: 2 DaysPurchasing Group: 001Standard Quantity: 10Tol. Underdl. 10Tol. Overdl: 10Tax Code: <Input Tax Code>TxValidFrm: MM/DD/YYYYNote When TDT is active for country of company code and Tax Code is given, the Tax Valid From field is mandatory. When TXA is active for company code and Tax Code is given, the Tax Country field is mandatory."Net Price: <Net Price>Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 6 | Save your data | Choose Save. | A purchasing info record is saved. |  |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

## Overview Table

The test script Sales Processing Using Third-Party Without Shipping Notification (BDK) consists of several process steps, reports, items provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/ App | Expected Results |
| --- | --- | --- | --- |
| [Sales Inquiry (1IQ) (Optional)](#unique_12) [page ] 13 | Internal Sales Representative | See scope item no. 1IQ |  |
| [Sales Contract Management (I9I) (Optional)](#unique_13) [page ] 14 | Internal Sales Representative | See scope item no. I9I |  |
| [Sales Quotation (BDG) (Optional)](#unique_14) [page ] 14 | Internal Sales Representative | See scope item no. BDG |  |
| [Create Sales Order](#unique_15) [page ] 15 | Internal Sales Representative | Manage Sales Orders - Version 2 (F3893) | The Manage Sales Order screen displays. |
| [Create Attachment for Sales Order (Optional)](#unique_16) [page ] 17 | Internal Sales Representative | Manage Sales Orders (F1873) | The Display Sales Order: Initial Screen displays. |
| [Change Order Quantity (Optional)](#unique_17) [page ] 18 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |
| [Credit Management Check for Sales Order (Optional)](#unique_18) [page ] 19 | See scope item BD6 | See scope item BD6 |  |
| [Display List of Purchase Requisitions to be Assigned](#unique_19) [page ] 20 | Purchaser | Process Purchase Requisitions (F1048A) | A list of Purchase Requisitions displays. |
| [Convert Assigned Requisitions to Purchase Orders](#unique_20) [page ] 21 | Purchaser | Process Purchase Requisitions (F1048A) | A list of Purchase Requisitions displays. |
| [Approve and Release Purchase Order (Optional)](#unique_21) [page ] 22 | Purchasing Manager | Approve Purchase Orders |  |
| [Create Supplier Invoice](#unique_22) [page ] 23 | Accounts Payable Accountant | Create Supplier Invoice (F0859). |  |
| [Accounts Payable (Optional)](#unique_23) [page ] 25 | See Accounts Payable (J60) scope item | See Accounts Payable (J60) scope item |  |
| [Create Billing Document](#unique_24) [page ] 27 | Billing Clerk | Create Billing Documents (F0798) | The Create Billing Document screen displays. |
| [Create Attachment for Billing (Optional)](#unique_25) [page ] 29 | Billing Clerk | Display Billing Documents (VF03) | The Display Billing Document screen displays. |
| [Create Pro Forma Invoice - for Free of Charge Items (Optional)](#unique_26) [page ] 26 | Billing Clerk | Create Billing Documents (F0798) | The Pro Forma Invoice is created. |

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

### Sales Inquiry (1IQ) (Optional)

|  |
| --- |
| Note Sales Inquiry (1IQ) |

Purpose

This scope item describes the process for a standard Sales Inquiry.

Procedure

Complete all the activities described in the Test script of the scope item: Sales Inquiry (1IQ).

|  |
| --- |
| Note If you want to use the optional link between scope item Sales Inquiry (1IQ) and Sales Processing Using Third-Party Without Shipping Notification (BDK) this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order). |

### Sales Contract Management (I9I) (Optional)

|  |
| --- |
| Note Sales Contract Management (I9I) |

Purpose

This scope item describes the process for Sales Quantity contract.

Procedure

Complete all the activities described in the Test script of the scope item: Sales Contract Management (I9I).

|  |
| --- |
| Note If you want to use the optional link between scope item Sales Contract Management (I9I) and Sales Processing Using Third-Party Without Shipping Notification (BDK) this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order). |

### Sales Quotation (BDG) (Optional)

|  |
| --- |
| Note Sales Quotation (BDG) |

Purpose

This scope item describes the process for a standard sales quotation.

Procedure

Complete all the activities described in the Test script of the scope item: Sales Quotation (BDG).

|  |
| --- |
| Note If you want to use the optional link between scope item Sales Quotation (BDG) and Sales Processing Using Third-Party Without Shipping Notification (BDK) this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order). |

### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Third-Party Sales Order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access Sales order worklist | Manage Sales Orders - Version 2 (F3893). | The Manage Sales Orders - Version 2 screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On the Manage Sales Order - Version 2 screen, choose Create. |  |  |
| 4 | Enter Sales Document Type | In the Create dialog, make the following entries and choose Continue:Sales Order Type: Standard Order (OR)Sales Organization: 3310Distribution Channel: 10Division: 00 | The New: Sales Order screen displays. |  |
| 5 | Enter Order Details | In the General Information tab, under Basic Data, make the following entries:Sold-to Party: 33100001Customer Reference: <Reference number>In the Items tab, make the following entries:Product: <Material Number>, for example,TG13Requested Quantity: <Quantity>, for example, 10Item Category: CB2Please check the entry is correctly setNote 1. You can manually change the item category to CB4 if the item is free of charge for 3rd party sales order without shipping notification.2. You can manually change the item category to DB2 if the item is down pay-ment relevant for 3rd party sales order without shipping notification, and proceed with following steps: Change Sales Orders (Remove Billing Block), Create Down Payment Request and Post a Down Payment from scope item Sales Order Processing with Customer Down Payment.. |  |  |
| 6 | Save | Choose Create.If it pops up the screen Standard Order: Purchase Order Scheduling, choose Complete dlv. and then choose Save. | The third-party sales order is created. A Purchase Requisition is created automatically. The order confirmation is only processed when the purchase requisition is converted into a purchase order.Make a note of the sales order number: And, you can find Purchase Requisition number in the tab of Schedule lines at item level. |  |

|  |
| --- |
| Note The print-out of the order confirmation is executed automatically, or manually only after the purchase requisition has been transferred to a purchase order For instructions on manually printing the output, see detail below. |

Printing form- Output Management

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays.Open |  |
| 2 | Access the App | Open Manage Sales Orders - Version 2 (F3893). | The Manage Sales Order - Version 2 screen displays. |  |
| 3 | Search for Sales Order | Enter search terms in filter bar and choose GoFor example, enter sales order number in Sales Order field. | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Click sales order number, and choose Display Sales Orders.Note If there is not a Display Sales Orders, then click Define Links. Select Display Sales Orders, and choose OK. | The Display Sales Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview Open screen, choose Header Output Preview . | The document prints. |  |

|  |
| --- |
| Note It can also be navigated to a factsheet screen in app Manage Sales Orders - Version 2 (F3893):On the Manage Sales Orders screen, enter search terms in filter bar and choose Go.In search result, choose your Sales Order Number and choose More Links. |

### Process Sales Order Approval (Optional)

Follow the procedure for Process Sales Order Approval steps in the scope item Sell from Stock (BD9).

Purpose

This process step shows you how to review the sales orders that might need to be approved.

Procedure

Complete the activities of Process Sales Order Approval step described in the scope item Sell from Stock (BD9).

### Create Attachment for Sales Order (Optional)

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

### Change Order Quantity (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you change the order quantity. This step is optional.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the role Internal Sales Representative. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the Sales order worklist | Open Manage Sales Orders (F1873) | The Manage Sales Orders (Original)screen displays |  |
| 3 | Navigate to Create Sales Order Screen | In Manage Sales Orders, choose on the sales order number and choose Change Sales Order - VA02. | Choose the sales order line that displays. |  |
| 4 | Change Documents | Change the quantity and save your entries. |  |  |
| 5 | Save Documents | Save your entries. | The sales order quantity has changed. If a PO existed, you have changed the PO quantity. Otherwise, you have changed the requisition quantity. |  |

|  |
| --- |
| Note If a PO has not been created yet, to confirm the quantity change in the requisition, change the sales order by select the item and choose Schedule lines for item. Double-click schedule line with the confirmed quantity. Choose the Procurement tab. Choose Edit and check if the quantity for the purchase requisition is updated. If a PO has already been created, to confirm the PO change you must select the purchase order and choose Display Document. |

### Credit Management Check for Sales Order (Optional)

External Process

For this activity, run the following steps from the Basic Credit Management (BD6) test script to review the sales orders that might have been blocked due to the credit limit check:

- Management of Blocked Sales Orders

### Display List of Purchase Requisitions to be Assigned

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed when you want to review your Purchase Requisitions and assign them to a vendor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Purchaser. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Purchase Requisitions (F1048A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of Requisitions is listed. |  |
| 3 | Search for Purchase Requisition | Enter the Purchase Requisition number and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition. | The purchase requisition is selected. |  |
| 5 | Assign Supplier | Choose the Assign Source of Supply button. Select one source and choose the Assign button. | The Source of Supply is assigned.The Purchase Requisition is updated successfully. |  |

### Convert Assigned Requisitions to Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note If you want to use the Save Draft feature in this app, you have to use a personalized user. |

Purpose

You perform this activity to convert the assigned requisitions into purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Purchase Requisitions (F1048A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of Requisitions is listed. |  |
| 3 | Search for Purchase Requisition | Enter the purchase requisition number and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition. | The purchase requisition is selected. |  |
| 5 | Create Purchase Order | Choose the purchase requisition where the assigned supplier is displayed and choose Create Purchase Orders.Note Choose Yes to continue the process if any warning message occurs. | The Purchase Order screen displays. |  |

|  |
| --- |
| Note The print-out of the order confirmation is executed after the Purchase Order is created automatically and immediately.For handling print and for processing of purchase orders, see Building Block Procurement of Direct Materials, Step Review Purchase Order. |

### Approve and Release Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase order. If the total amount of PO >= 500 AED and purchase group is 003. Then the PO should do the approval.

Prerequisite

A purchase order must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of previously created Purchase Orders display. |  |
| 3 | Search for Purchase Order Status | Enter the Purchase order number in the search area, and then choose the Search. | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 AED or more have the status In Approval. |  |
| 4 | Release Purchase Order | Select the Purchase order in left of the screen and choose Release in bottom right. | The Submit Decision dialog box displays. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, and then choose Submit. | The Purchase Order is approved. |  |
| 6 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

|  |
| --- |
| Note If an attachment is uploaded during purchase order creation, in My Inbox APP, the attachment can be found under Attachments tab of the purchase order. The attachment will be renamed with prefix “H_”. |

### Create Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice with PO/GR relation. You have two options to create the supplier invoice:

Option A: Create Supplier Invoice with PO/GR relation.

Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction)

You can choose either option A or option B to execute the supplier invoice creation with PO/GR relation. For more information, see the next two tasks.

|  |
| --- |
| Note Only choose either option A or B (not both). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Supplier Invoice App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: XXX (change the invoice currency, for example from EUR to USD)Invoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoicing Party:Select See More at header area, make the following entries.Exchange Rate: <XXX> | The Exchange Rate should be changed from USD in EUR according to the customizing settings. The Exchange Rate is changeable |  |
| 4 | Enter Purchase Order References | In Purchasing Order References section, add the references.Make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Check Tax code | In the section Tax, check if there is tax code information and enter the tax amount if the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code>. |  |
| 8 | Block invoice on item level (optional) | Choose the invoice item arrow on the right side of the item to navigate to the item details.On the next screen, set flag for Manually Blocked. Click Check and on the lower part of the details screen, the Blocking Reasons section shows the text Manual. Click Back to Supplier Invoice. | The item is blocked with a blocking reason. |  |
| 9 | Check the balance | Calculate the tax by choosing Propose Tax. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 11 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation Details area. | The Supplier Invoice is simulated. |  |
| 12 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

### Accounts Payable (Optional)

External Processes

For this activity, run the following steps from theAccounts Payable (J60) test script to post the outgoing payment:

- Post Outgoing Payment
- Create Manual Payment

### Create Pro Forma Invoice - for Free of Charge Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle Pro Forma invoice only when you are using item category CB2 or CB4 in the previous steps. Item category C4L does not support the creation of a proforma invoice.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using role Billing Clerk. |  |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents (F0798) screen displays. |  |
| 3 | Define billing setting | Choose Billing Settings in the right bottom of the screen, make all of these settings to ON, then choose OK:Enter Billing Data before billingSeparate Billing Documents for Each Billing Due List Item.Automatically Post Billing DocumentsDisplay Billing Document after creation. |  |  |
| 4 | Search for billing list | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose button Create. | The window Create Billing Documents (F0798) displays. |  |
| 6 | Maintain Billing Date | Choose billing type Pro Forma for Order (F5) and maintain billing date, for example current date, then choose OK . | The new billing document will be created |  |
| 7 | Display Billing Document after Creation | The billing document displays automatically, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Manage billing documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access APP | Open APP Manage Billing Documents (F0797). | The screen Manage Billing Document displays. |  |
| 2 | Search the billing document created in previous step | Input the Billing number recorded in previous step. Choose Enter. | The billing document created in previous step displays. |  |
| 3 | Display the billing document | Select the billing document item and choose Display. | The billing document shall be displayed. |  |
| 4 | Check Output Condition | On the Billing Document (F1901)screen, choose the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document (F1901) screen choose Preview. | Preview for PDF document displays. |  |
| 6. | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel billing Docs. | There is log display - Billing Document Canceled. |  |
| 7 | Update new Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Save your changes by pressing the button Save in the footer bar. |  |  |
| 8 | Update new Text (optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by pressing the button Save in the footer bar. |  |  |

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle billing.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad using the role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798) . | The Create Billing Document screen displays. |  |
| 3 | Define billing setting | Choose Billing Settings in the bottom bar, you can make the following settings as below:1. Set billing date and type before billing: ON2. Create separate billing document for each item of billing due list: ON3. Automatically post billing documents: ON4. Display billing documents after creation: ON5. Choose delivery items to be billed and select quantities ： OFF |  |  |
| 4 | Search for billing list | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Choose Individual Billing Document | Select a row of sales document created previously and choose Create. | The Create Biling Document displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then choose OK. | The new billing document will be created. |  |
| 7 | Display Billing Document after Creation | The billing document automatically displays, make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 8 | ODN Number | Check whether the ODN number is generated for the billing document. | ODN number is generated in the Reference field. |  |

Financial postings:

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 G/L (for Item category CB2)44002000 G/L (for Item category CB4) | 41000000 Rev Domestic Prod(only for CB2) beside the output tax | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access APP | Open APP Manage Billing Documents (F0797). | The screen Manage Billing Document displays. |  |
| 2 | Search the billing document created in previous step | Input the Billing document number recorded in previous step. Choose Enter. | The billing document created in previous step displays. |  |
| 3 | Display the billing document | Select the billing document item, and choose Display. | The billing document will displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel Billing Docs | The log displays - Billing Document Canceled. |  |
| 7 | Update new Attachment (Optional) | In the Edit mode, add, delete and update the attachments. Choose Save in the footer bar. |  |  |
| 8 | Update new Text (optional) | In the Edit mode, you can add, delete and update texts. Choose Save in the footer bar. |  |  |

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
| J59 - Accounts Receivable | Posting a Customer Invoice, etc.Using the master data from this document, complete the following activities described in the test script:Accounts Receivable(J59) (Sections Posting a Customer Invoice in Accounting, Overdue Receivables, Display Customer Balances, Manage Customer Line Items ) |
| BKK - Sales Order Fulfillment Monitoring and Operations(optional) | Collection of periodic activities such as day ending activities or legal requirements like Intrastat and Extrastat reporting.Using the master data from this document, complete the following activities described in the test script:Sales Order Fulfillment Monitoring and Operations(BKK) (Sections Review Incomplete SD Documents (deliveries), Review Sales Documents blocked for billing, Review Log of collective invoice creation) |

### Relevant Processes

Purpose

It’s allowed to switch between MTO and 3rd party process, please use app Manage Your Solution with SSCUI 102807 - Assign Item Categories to extend relevant item category assignment. Then you can choose the corresponding item category during the sales order creation, and follow the process to complete the sales order.

| Process | Item Category |
| --- | --- |
| Make-to-Order Production - Finished Goods Sales and Final Assembly (BJE) | CBTA |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). |  |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. |  |  |
| 4 | Open Assign Item Categories | Choose Assign Item Categories in the following area: Sale -> Sales Order Management and Processing -> Sales Documents . |  |  |
| 5 | Go to Configuration Details | Choose Configure. |  |  |
| 6 | Change item category assignment | Double-click the line with sales document type OR and item category group CBNA， input the Manual item category to CBTA, and choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Item Categories | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Item Categories.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Open search bar | Double-click the line with sales document type OR and item category group CBNA， input the Manual item category to CBTA, and choose Save. |  |  |

### Scheduling Job (alternative)

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
> Flagged while digesting this document, not verified: Approval threshold is inconsistent within the document: the workflow configuration example uses total net amount greater than 10 AED, while the release section states approval is needed for PO >= 500 AED with purchasing group 003.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/sales-processing-using-third-party-with-shipping-notification-bd3-ae-t]]
- related-to :: [[08-sales-order-management/sales-processing-using-third-party-with-variant-configuration-4r6-ae-1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 61,366 chars in the whole document
