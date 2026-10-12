---
id: 08-sales-order-management/sales-processing-using-third-party-with-shipping-notification-bd3-ae-t
title: "Sales Processing using Third-Party with Shipping Notification (BD3_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BD3_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item BD3 (AE): third-party sales order, purchase requisition/PO, statistical goods receipt, billing and supplier invoice, with prerequisites and appendix."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/third-party-sales]
aliases: [BD3_S4CLD2608_BPD_EN_AE]
keywords: [Third-Party Sales Processing, third-party sales order, purchase requisitions, purchase order creation, purchase order approval, statistical goods receipt, billing documents, supplier invoice, item category determination, pro forma invoice]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BD3_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1248
topic: 08-sales-order-management/third-party-sales
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Sales Processing using Third-Party with Shipping Notification (BD3_AE) - Test Script, SAP S/4HANA Cloud Public Edition (BD3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BD3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Third-Party Sales Processing** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales Processing using Third-Party with Shipping Notification (BD3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860845)

[2 Prerequisites 4](#_Toc232860846)

[2.1 System Access 4](#_Toc232860847)

[2.2 Roles 4](#_Toc232860848)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232860849)

[2.4 Business Conditions 6](#_Toc232860850)

[2.5 Preliminary Steps 7](#_Toc232860851)

[2.5.1 Check Flexible Workflow for Purchase Order Approval 7](#_Toc232860852)

[2.5.2 Configure Flexible Workflow for Purchase Order 8](#_Toc232860853)

[2.5.3 Create Purchasing Info Record 9](#_Toc232860854)

[2.5.4 Create Condition Records (Optional) 11](#_Toc232860855)

[3 Overview Table 12](#_Toc232860856)

[4 Test Procedures 13](#_Toc232860857)

[4.1 Sales Contract Management (I9I) (Optional) 13](#_Toc232860858)

[4.2 Sales Quotation (BDG) (Optional) 14](#_Toc232860859)

[4.3 Create Third-Party Sales Order 14](#_Toc232860860)

[4.4 Process Sales Order Approval (Optional) 17](#_Toc232860861)

[4.5 Create Attachment for Sales Order (Optional) 17](#_Toc232860862)

[4.6 Change Order Quantity (Optional) 18](#_Toc232860863)

[4.7 Credit Management Check for Sales Order (Optional) 19](#_Toc232860864)

[4.8 Display List of Purchase Requisitions to be Assigned 19](#_Toc232860865)

[4.9 Convert Assigned Requisitions into Purchase Orders 20](#_Toc232860866)

[4.10 Approve and Release Purchase Orders (Optional) 21](#_Toc232860867)

[4.11 Post Statistical Goods Receipt 22](#_Toc232860868)

[4.12 Create Billing Document 24](#_Toc232860869)

[4.13 Create Attachment for Billing (Optional) 26](#_Toc232860870)

[4.14 Create Pro Forma Invoice – for Free or Charge Items (Optional) 27](#_Toc232860871)

[4.15 Create Invoice 29](#_Toc232860872)

[5 Appendix 32](#_Toc232860873)

[5.1 Process Integration 32](#_Toc232860874)

[5.2 Relevant Processes 32](#_Toc232860875)

[5.3 Succeeding Processes 33](#_Toc232860876)

[5.4 Limitations 34](#_Toc232860877)

[5.5 Determination of item category 34](#_Toc232860878)

[5.6 Integration with Advanced ATP – Scope item 1JW 34](#_Toc232860879)

[5.7 Scheduling Job (alternative) 35](#_Toc232860880)

[5.7.1 Job Scheduling for Billing Creation (Alternative) 35](#_Toc232860881)

[5.7.2 Job Scheduling for Billing Release (Alternative) 36](#_Toc232860882)

[5.7.3 Job Scheduling for Billing Output (Alternative) 37](#_Toc232860883)

## Purpose

Overview

This scope item enables you to forward orders to third-party vendors who ship the goods directly to customers and then bill you directly. The standard sales order automatically creates a purchase requisition for the materials to be delivered by third-party vendors. Once vendors have sent a shipping notification, a statistical goods receipt can be posted. Once this has taken place, invoices can be created and issued based on the goods receipt quantities.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/BD3_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG10 | Trading Good for regular Trading (MRP planning) with item category group CBORno Serial no.; no batch. | See sections Preliminary Steps. |
| Sold-to party | 33100001 | Domestic UAE Customer 1 | You can test the scope item using another domestic customer. |
| Ship-to party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Vendor | 3330000133300002 | Domestic UAE Supplier 1Domestic UAE Supplier 2 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Shipping Point | 3310 | Shipping Point 3310 |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Company Code | 3310 | Company Code 3310 |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2EJ - Integration of Procurement with External Suppliers | In case you want to exchange messages with Supplier per EDI(Execute steps of (EDI ,Option )), you have to activate Scope Item 2EJ. |

### Preliminary Steps

#### Check Flexible Workflow for Purchase Order Approval

Purpose

This process step shows you how to check the flexible workflow for purchase order approval.

When you use the flexible workflow to approve the purchase order, make sure Flexible Workflow for Purchase Order with NB document is activated, and Flexible Workflow for Purchase Order Approval is configured.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241). | The Manage Your Solution screen displays. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. | The Configure Your Solution screen displays. |  |
| 4 | Open Active Flexible Workflow | On the Configure Your Solution screen, search Activate Flexible Workflow for Purchase Orders, then choose Go.Select the line of the item and go to the next screen.On the Configure Your Solution – Purchase Order Processing screen, choose Configure on the line of configuration step with name Activate Flexible Workflow for Purchase Orders. | The Document Types Purchase order Change screen displays. |  |
| 5 | Check Flexible Workflow for PO Approval | Check the following entries:Purchasing Doc. Type: NBScenario based workflow:<Selected> | The scenario based workflow is active for purchase orders with document type: NB. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Document Types Purchase order Change screen displays. |  |
| 3 | Check Flexible Workflow for PO Approval | Check the following entries:Purchasing Doc. Type: NBScenario based workflow:<Selected> | The scenario based workflow is active for purchase orders with document type: NB. |  |

#### Configure Flexible Workflow for Purchase Order

Purpose

This process step shows you how to configure release conditions for Purchase Order Approval.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Workflows for Purchase Orders (F2872) . | The Manage Workflows screen displays. |  |
| 3 | Create Manage Workflow | Choose Create and make the following entries:Name: Test Workflow for Purchase OrderIn the START CONDITIONS area select Purchasing group of purchase order is and enter 003 value:Choose Create Alternative Preconditions and make the following entries:Choose Total net amount of purchase order is greater than,Purchase Order Total Net Amount: for example, 10Purchase Order Currency: AEDIn STEP SEQUENCE area, choose Create and make the following entries:Type: Release of Purchase OrderIn RECIPIENTS area:Assignment By: UserUser: select user with Purchasing_manager from F4 help.Step to be completed by: One of the recipients.Choose Create.Choose Save. | The workflow for purchase order is configured. |  |
| 4 | Activate Workflow Item | Select the just created workflow item and choose Activate. | The workflow item is activated. |  |

|  |
| --- |
| Note Please make sure default workflow automatic release of purchase order has been activated. |

#### Create Purchasing Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a purchase info record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Purchasing Info Record (ME11). | The Create Info Record: Initial screen displays. |  |
| 3 | Enter Data | Make the following entries:Supplier: 33300001/ 33300002Material: TG10Purchasing Organization: 3310Plant: 3310And Choose Enter | The Create Info Record: General Data screen displays. |  |
| 4 | Navigate to Purch. Org. Data 1 | Choose Purch. Org. Data 1. |  |  |
| 5 | Enter Purchasing Data | Make the following entries:Delivery Time in Days: 2 DaysPurchasing Group: 001Standard Quantity: 10Tol. Underdl: 10Tol. Overdl: 10Tax Code: <Input Tax Code>Net Price: 12.35Incoterm: EXWIncoterm Location 1:VENDOR | Purchasing Data is added. |  |
| 5 | Save Your Data | Choose Save. | A purchasing info record is saved. |  |

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
| Sales Contract Management (I9I) (Optional) | Internal Sales Representative | See scope item no. I9I |  |
| Sales Quotation (BDG) (Optional) | Internal Sales Representative | See scope item no. BDG |  |
| [Create Third-Party Sales Order](#unique_12) [page ] 14 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |
| [Process Sales Order Approval (Optional)](#unique_13) [page ] 17 |  |  |  |
| [Create Attachment for Sales Order (Optional)](#unique_14) [page ] 17 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Change Order Quantity (Optional)](#unique_15) [page ] 18 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage Sales Orders screen displays. |
| [Credit Management Check for Sales Order (Optional)](#unique_16) [page ] 19 |  |  |  |
| [Display List of Purchase Requisitions to be Assigned](#unique_17) [page ] 19 | Purchaser | Process Purchase Requisitions (F1048A) | A list of Purchase Requisitions displays. |
| [Convert Assigned Requisitions into Purchase Orders](#unique_18) [page ] 20 | Purchaser | Process Purchase Requisitions (F1048A) | A list of Purchase Requisitions displays. |
| [Approve and Release Purchase Orders (Optional)](#unique_19) [page ] 21 | Purchasing Manager | My Inbox - All Items (F0862) |  |
| [Post Statistical Goods Receipt](#unique_20) [page ] 22 | Warehouse Clerk | Post Goods Movement (MIGO) | The Post Goods Receipt for Purchase Order screen displays. |
| [Create Billing Document](#unique_21) [page ] 24 | Billing Clerk | Create Billing Documents (Work List) | The Create Billing Document screen displays. |
| [Create Attachment for Billing (Optional)](#unique_22) [page ] 26 | Billing Clerk | Manage Billing Documents (F0797) | The Display Billing Document screen displays. |
| [Create Pro Forma Invoice – for Free or Charge Items (Optional)](#unique_23) [page ] 27 | Billing Clerk | Create Billing Documents (F0798) | Pro Forma invoice is created. |
| [Create Invoice](#unique_24) [page ] 29 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) |  |

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

### Sales Contract Management (I9I) (Optional)

|  |
| --- |
| Note Sales Contract Management (I9I) |

Purpose

This process step shows you the process for sales quantity contract.

Procedure

Complete all the activities described in the test script of the scope item: Sales Contract Management (I9I).

|  |
| --- |
| Note If you want to use the optional link between scope item Sales Contract Management (I9I) and Sales Processing using Third-Party with Shipping Notification (BD3) this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order). |

### Sales Quotation (BDG) (Optional)

|  |
| --- |
| Note Sales Quotation (BDG) |

Purpose

This process step shows you the process for a standard sales quotation.

Procedure

Complete all the activities described in the test script of the scope item: Sales Quotation (BDG).

|  |
| --- |
| Note If you want to use the optional link between scope item Sales Quotation (BDG) and Sales Processing using Third-Party with Shipping Notification (BD3) this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order). |

### Create Third-Party Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a third-party sales order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Select Create Sales Order Screen | On the Manage Sales Orders screen:Select Create buttonChoose Create Sales Orders - VA01. |  |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00Choose Continue. | The Create Standard Order: Overview window displays. |  |
| 5 | Enter Order Details | Make the following entries:Sold-To Party: 33100001Cust. Reference: PO numberReq.Deliv Date: <Date>Material: <Material Number>, for example, TG10.Order Quantity: <quantity>, for example, 10Item Category: CB1.Note 1. You can manually change the item category to CB3 if the item is free of charge for 3rd party sales order with shipping notification. This item category is free of charge with a 100% rebate and can be invoiced ( external & proforma invoice).2. You can manually change the item category to C3L if the item is free of charge for 3rd party sales order with shipping notification. This item category is without pricing and can NOT be invoiced ( external & proforma invoice).3. You can manually change the item category to DB1 if the item is down payment relevant for 3rd party sales order with shipping notification, and proceed with following steps: Change Sales Orders (Remove Billing Block), Create Down Payment Request and Post a Down Pay-ment from scope item Sales Order Processing with Customer Down Payment.4. You can manually change the schedule line category to SD if the material is subcontract relevant. To finish the whole subcontract process, kindly please maintain the cost center after the purchase document is created.Choose Save. |  |  |
| 6 | Complete Delivery | From the Standard Order: Purchase Order Scheduling screen, choose Complete dlv.. | The third-party sales order is created. A Purchase Requisition is created automatically.You can find the purchase requisition number by doing the following:From the Item Overview tab select the Display items details icon, and then select Schedule Lines.The order confirmation is only processed when the purchase requisition is converted into a purchase order.Make a note of the sales order number. |  |

Printing Form

|  |
| --- |
| Note The order confirmation print-out is executed automatically or manually only after the purchase requisition has been transferred to a purchase order.For instructions on manually printing the output, see Manual Printing below. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Order screen displays. |  |
| 3 | Search for Sales Order | Enter search terms in filter bar and choose GoFor example, enter sales order number in Sales Order field. | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Click sales order number, and choose Display Sales Order - VA03.Note If there is not a Display Sales Order - VA03, then click Define Links. Select Display Sales Order - VA03, and choose OK. | The Display Sales Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Header Output Preview . | The document displays. |  |

|  |
| --- |
| Note In the Manage Sales Orders app, you can navigate to a fact sheet:On the Manage Sales Orders screen, enter search terms in the filter bar and choose Go.In the search result, select your sales order number and choose Sales Order Number. |

### Process Sales Order Approval (Optional)

Follow the procedure for Process Sales Order Approval steps in the scope item Sell from Stock (BD9).

Purpose

This optional process step shows you how to review the sales orders that might need to be approved.

Procedure

Complete the activities of Process Sales Order Approval step described in the Sell from Stock (BD9) scope item.

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
| 1 | Log on | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Select Order Number to Change | In Manage Sales Orders, choose on the sales order number and choose Change Sales Order - VA02. |  |  |
| 4 | Change Document | Change the quantity as needed. |  |  |
| 5 | Save Document | Save your entries. | The sales order quantity has been changed. If a PO existed, you have changed the PO quantity. Otherwise, you have changed the requisition quantity. |  |

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

### Convert Assigned Requisitions into Purchase Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You perform this activity when you want to convert the assigned requisitions into purchase orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad using the role Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process Purchase Requisitions (F1048A).Note If you want to use the Save Draft feature in this app, you have to use a personalized user. | A list of Requisitions is listed. |  |
| 3 | Search for Purchase Requisition | Enter the purchase requisition number and choose Go. | The Purchase Requisition is displayed. |  |
| 4 | Select Purchase Requisition | Select the purchase requisition. | The purchase requisition is selected. |  |
| 5 | Create Purchase Order | Choose the purchase requisition where the assigned supplier is displayed and choose Create Purchase Orders.Note Choose Yes to continue the process if any warning message occurs. | The Purchase Order screen displays. |  |

### Approve and Release Purchase Orders (Optional)

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox - All Items (F0862). | A list of previously created Purchase Orders display. |  |
| 3 | Search for Purchase Order Status | Enter the Purchase order number in the search area, and then choose the Search. | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 AED or more have the status In Approval. |  |
| 4 | Release Purchase Order | Select the Purchase order in left of the screen and choose Release in bottom right. | The Submit Decision dialog box displays. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, and then choose Submit. | The Purchase Order is approved. |  |
| 6 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

|  |
| --- |
| Note If an attachment is uploaded during purchase order creation, in My Inbox APP, the attachment can be found under Attachments tab of the purchase order. The attachment will be renamed with prefix “H_”. |

### Post Statistical Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the vendor has sent the shipping notification, you post a statistical goods receipt

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Goods Movement (MIGO). | The Goods Receipt Purchase Order - warehouse screen displays. |  |
| 3 | Choose Good Receipt | Make the following entries:From the Trans./Event pull-down, select Goods ReceiptFrom the Reference Document pull-down menu, select Purchase orderIn thePurchase Orderfield, enter a <PO number>GR goods receipt: 101Choose Enter: | The Goods Receipt Purchase Order XXXXXXXXXX screen displays. |  |
| 4 | Change the quantity if necessary | If necessary, change the quantity in Detail Data section, Quantity tab. |  |  |
| 5 | Enter Goods Recipient | In Detail Data section, choose Where tab.Make the following entry:Goods Recipient: for example 331AChoose Enter. |  |  |
| 6 | Select Item OK | Select the Item OK checkbox at the bottom of the screen. |  |  |
| 7 | Save the documents | Choose Post. | The system generates a material document.You may record down the posted material document number at the bottom. |  |

|  |
| --- |
| Note To view the material document in FLP, open Display Material Documents List. |

Financial postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 54083000 (Inv Chg COGS w/CE) | 21120000 GR/IR | none |

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

Procedure

Table 3: Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Billing Clerk . | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the bottom bar, you can make the following settings as below:1. Set billing date and type before billing: ON2. Create separate billing document for each item of billing due list: ON3. Automatically post billing documents: ON4. Display billing documents after creation: ON5. Choose delivery items to be billed and select quantities ： OFF |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) will display in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of sales document created previously and choose Create. | The Create Billing Documents window displays. |  |
| 6 | Maintain Billing Date | From the Billing Type drop-down menu, select F2 Invoice (F2) and from the Billing Date field select a date. For example, current date.Choose OK. | The new billing document will be created. |  |
| 7 | Save the Billing Document | Choose Save. |  |  |
| 8 | Display Billing Document after Creation | The billing document displays automatically. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |
| 9 | ODN Number | Check whether the ODN number is generated for the billing document. | ODN number is generated in the Reference field. |  |

Table 4: Manage billing documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Open Manage Billing Documents． | The Manage Billing Documents screen displays. |  |
| 2 | Search the Billing Document Created in Previous Step | Enter or Select from the Billing Documents list the billing document number recorded in previous step.Select Display. | The billing document created in the previous step displays. |  |
| 3 | Display the billing document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain billing document and choose Cancel billing Docs. | A log displays: Billing Document Canceled. |  |
| 7 | Update new Attachment (Optional) | In the Edit mode, you can add, delete and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update new Text (optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by choosing Save in the footer bar. |  |  |

Financial postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 G/L (for Item category CB1)44002000 G/L (for Item category CB3) | 41000000 Rev Domestic Prod22000000 (only for CB1) Output tax (MWS) | none |

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

### Create Pro Forma Invoice – for Free or Charge Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you handle Pro Forma invoice only when you are using item category CB1 or CB3 in the previous steps.

|  |
| --- |
| Note Item category C3L does not support the creation of a proforma invoice. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define billing setting | Choose Billing Settings at the right bottom of the screen.There are four settings. You should turn all of these settings into ON.Enter Billing Data before billingSeparate Billing Documents for Each Billing Due List Item.Automatically Post Billing DocumentsDisplay Billing Document after creation. |  |  |
| 4 | Search for billing list | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of Sales document created previously and choose Create. | The Create Billing Documents window displays. |  |
| 6 | Maintain Billing Date | Choose billing type Pro Forma for Order (F5) and maintain billing date, such as the current date.Choose OK. | The new billing document will be created. |  |
| 7 | Display Billing document after creation | The billing document displays automatically. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Table 5: Manage billing documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access APP | Open APP Manage Billing Documents under Sales Billing Document. | The screen Manage Billing Document displays. |  |
| 2 | Search the billing document created in previous step | Input the billing document number recorded in the previous step. Press Enter. | The billing document created in the previous step displays. |  |
| 3 | Display the billing document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel billing Docs. | A log displays: Billing Document Canceled. |  |
| 7 | Update new Attachment (Optional) | In the Edit mode, you can add, delete and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update new Text (optional) | In the Edit mode, you can add, delete and update these texts. Save your changes by choosing Save in the footer bar. |  |  |

### Create Invoice

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

Option B: Create Supplier Invoice with PO/GR relation (with Invoice Reduction).

You can choose either option A or option B to execute the supplier invoice creation with PO/GR relation. For more information, see the next two tasks.

Only choose either option A or B (not both).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountant role. | The SAP Fiori launchpad displays. |  |
| 2 | Open Create Supplier Invoice App | Open Create Supplier Invoice - Advanced (MIRO). | The Create Supplier Invoice screen displays. |  |
| 3 | Enter General Data | Local Currency: If a purchase order was created with local currency in your system, make the following entries:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx> (reference invoice number from invoicing party)Invoicing Party:Foreign Currency: If a purchase order was created using foreign currency in your system, make the following entries:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: XXX (change the invoice currency, for example from EUR to USD)Invoice Date: <Today>Posting Date: <Today>Reference: <xxx> (reference invoice number from invoicing party)Invoicing Party:Select See More at header area, make the following entries. :Exchange Rate: <XXX> | The Exchange Rate should be changed from USD to AED according to the customizing settings.The Exchange Rate is interchangeable. |  |
| 4 | Enter Purchase Order References | In Purchase Order References section, add the references.Make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Verify the Invoice Items data | Verify the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Verify Tax code | In the section Tax, verify if there is tax code information and enter the tax amount if the tax code value is greater than zero.In the Tax area, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code> . |  |  |
| 8 | Block invoice on item level (optional) | From the Purchase Order References section, choose the invoice item arrow (located on the right side of the item) to navigate to the item details.Select Manually Blocked.Select Check from the lower part of the details screen. The Blocking Reasons section shows the text Manual.Choose Back to Supplier Invoice . | The Create Supplier Invoice screen displays.The item is blocked with a blocking reason. |  |
| 9 | Verify the Balance | Calculate the tax by choosing Propose Tax. Verify the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 10 | Simulate Supplier Invoice and Check Messages | Choose the Simulate button.You can check the simulation results in Simulation Overview and Simulation Details area. | The supplier Invoice is simulated. |  |
| 11 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Your Solution (F1241). |  |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution.Note To create country-/region-dependent settings for the intended local version, choose Set Local Version. |  |  |
| 4 | Open Assign Item Categories | Choose Assign Item Categories in the following area: Sale -> Sales Order Management and Processing -> Sales Documents . |  |  |
| 5 | Go to Configuration Details | Choose Configure. |  |  |
| 6 | Change item category assignment | Double-click the line with sales document type OR and item category group CBOR， input the Manual item category to CBTA, and choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Assign Item Categories.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Check Flexible Workflow for PO Approval | Double-click the line with sales document type OR and item category group CBOR， input the Manual item category to CBTA, and choose Save. |  |  |

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Payable (J60) | Post the outgoing payment.Using the master data from this document, complete the following activities described in the test script:Post Payments Using the Payment ProgramPost Manual Outgoing payment |
| Accounts Receivable (J59) | Posting a Customer Invoice in Accounting, etc.Using the master data from this document, complete the following activities described in the test script:Posting a Customer Invoice in AccountingOverdue Receivables, Display Customer BalancesManage Customer Line Items |
| Sales Order Fulfillment Monitoring and Operations(BKK) (optional) | This scope item describes the collection of periodic activities such as day ending activities, or reporting.Using the master data from this document, complete all the activities described in the Test Script of the scope item:Review Incomplete SD Documents (deliveries),Review Sales Documents blocked for billingReview Log of collective invoice creation |

### Limitations

Preliminary billing documents cannot be used in the current process, please don’t create relevant document.

### Determination of item category

There are three options to trigger a third party direct ship process with item category CB1:

1. When entering the product in the sales order, choose item category group CBOR in the material master to determine CB1 as default value.
2. Choose item Category CB1 manually in the sales order for materials which have a different item category group in the material master ( if allowed via configuration in SSCUI 102807 )
3. CB1 can also be determined automatically based on the advanced ATP features via a rules framework within the ATP check. Please see scope item 1JW ( Advanced ATP) for details.

### Integration with Advanced ATP – Scope item 1JW

Scope item BD3 is using item category CB1 as standard item category to initiate the BD3 process.

In addition to the 3 standard ways to determine the item category CB1 - which are:

1. Manually enter item category

2. Default item category via item category group CBOR assigned in the material master to the material and configuration in SSCUI 102807.

3. Flexible item category determination [Flexible Item Category Determination](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/66327f62527a4a988c1976c23e8ba3c4.html?version=2402.502) .

4. NEW: Based on the configuration of the Advanced ATP check, please see scope item 1JW - Advanced Available-to-Promise Processing for details and prerequisites.

"

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
> Flagged while digesting this document, not verified: Workflow configuration example uses a total net amount threshold greater than 10 AED, while the approval step states POs of 500 AED or more with purchasing group 003 require approval; thresholds differ.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Item category determination is described as 'three options' in one section, and as 3 standard ways plus a NEW fourth (Advanced ATP) in the 1JW integration section.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/sales-processing-using-third-party-with-variant-configuration-4r6-ae-1]]
- related-to :: [[08-sales-order-management/sales-processing-using-third-party-without-shipping-notification-bdk-a]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BD3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 63,542 chars in the whole document
