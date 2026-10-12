---
id: 10-procurement/test-script-automated-purchase-to-pay-with-sap-ariba-commerce-automati
title: "Test Script: Automated Purchase-to-Pay with SAP Ariba Commerce Automation (J82_AE) (J82_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud Public Edition test script for scope item J82 (UAE): Ariba-integrated PO-to-invoice process, prerequisites and 15 test procedures."
cluster: 10-procurement
tags: [kb/procurement, topic/business-network-purchase-to-pay]
aliases: [J82_S4CLD2608_BPD_EN_AE]
keywords: [Purchase-to-Pay Automation with SAP Business Network, ariba commerce automation, purchase-to-pay automation, sap business network, flexible workflow, purchase order creation, purchase order approval, goods receipt, supplier invoice, scope item 42k]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J82_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1310
topic: 10-procurement/business-network-purchase-to-pay
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Automated Purchase-to-Pay with SAP Ariba Commerce Automation (J82_AE) (J82_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J82_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Purchase-to-Pay Automation with SAP Business Network** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Automated Purchase-to-Pay with SAP Ariba Commerce Automation (J82_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232863824)

[2 Prerequisites 4](#_Toc232863825)

[2.1 System Access 4](#_Toc232863826)

[2.2 Roles 4](#_Toc232863827)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232863828)

[2.4 Business Conditions 6](#_Toc232863829)

[2.5 Preliminary Steps 6](#_Toc232863830)

[2.5.1 Opening New MM Period 6](#_Toc232863831)

[2.5.2 Activate Flexible Workflow for Purchase Orders 7](#_Toc232863832)

[2.5.3 Configure Flexible Workflow for Purchase Order 8](#_Toc232863833)

[3 Overview Table 10](#_Toc232863834)

[4 Test Procedures 11](#_Toc232863835)

[4.1 Create Purchase Order Using Advanced App (Optional) 11](#_Toc232863836)

[4.2 Approve Purchase Order 12](#_Toc232863837)

[4.3 Display Purchase Order (as a Supplier in SAP Business Network for Procurement) 13](#_Toc232863838)

[4.4 Change Purchase Order (Optional) 14](#_Toc232863839)

[4.5 Create Confirmation in SAP Business Network for Procurement (Optional) 15](#_Toc232863840)

[4.6 Check Purchase Order Confirmation (Optional) 16](#_Toc232863841)

[4.7 Create Shipping Notification in SAP Business Network for Procurement (Optional) 17](#_Toc232863842)

[4.8 Check Inbound Delivery for Purchase Order (Optional) 18](#_Toc232863843)

[4.9 Set Up the Putaway of Goods for Inbound Delivery 19](#_Toc232863844)

[4.10 Post Goods Receipt for Inbound Delivery 20](#_Toc232863845)

[4.11 Check Goods Receipt Details (optional) 21](#_Toc232863846)

[4.12 Display Goods Receipt (as a Supplier in SAP Business Network for Procurement) 22](#_Toc232863847)

[4.13 Create Supplier Invoice with PO/GR Relation 22](#_Toc232863848)

[4.14 Release Supplier Invoice for Payment (Optional) 25](#_Toc232863849)

[4.15 Display Invoice Status Change (as a Supplier in SAP Business Network for Procurement) 25](#_Toc232863850)

## Purpose

Overview

By automating purchase order to invoice processing in the SAP Business Network for Procurement, you can seamlessly connect from SAP S/4HANA Cloud Public Edition to your suppliers in SAP Business Network for Procurement. You can send electronic purchase orders to your suppliers using SAP Business Network for Procurement and receive electronic order confirmations, advance shipping notices, and invoices from your suppliers in SAP Business Network for Procurement in SAP S/4HANA Cloud Public Edition. You can use SAP Business Network for Procurement integration in the procurement of direct or indirect materials and in the procurement of project-based services processes.

Digitized collaboration with your suppliers in SAP Business Network for Procurement supports you in speeding up procurement processes and in reducing the number of manual process steps, thereby reducing the cost of transactions with your suppliers.

The Automation of Source-to-Pay with Ariba Network (42K) scope item is the successor to Automated Purchase-to-Pay with SAP Ariba Commerce Automation (J82), leveraging SOAP APIs and SAP Cloud Integration to integrate with SAP Business Network for Procurement. Customers who haven't previously activated J82 need to activate 42K instead. Customers who have already activated J82 can continue to use it until further notification.

New functionalities will be added only to the 42K scope item. Presently, 42K does not fully cover all functionalities of J82. The existing gaps will be closed with future releases of SAP S/4HANA Cloud Public Edition. Once the gaps are closed and 42K covers all of J82's functionalities, Automated Purchase-to-Pay with SAP Ariba Commerce Automation (J82) will be deprecated.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Vendor | 33300080 | Vendor domestic United Arab Emirates Ariba |  |
| Material | TG0011 | Trading Good for Regular Procurement (PD planning) |  |
| no Serial no.; no batch no. | See [Business Conditions](#unique_6) [page ] 6 and Preliminary Steps sections. |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Master Data Script Text |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

|  |
| --- |
| Note To run through this scope item, the materials must be available in stock. You can create stock using the Manage Stock (F1062__sap_mmimtype_manage) app or the Transfer Stock - In-Plant (F1061) app in the SAP Fiori launchpad. |

### Preliminary Steps

#### Opening New MM Period

External Process

For this activity, run the following steps from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period: Closing MM Period and Opening New Posting Period.

#### Activate Flexible Workflow for Purchase Orders

Use

This procedure describes how to activate the flexible workflow for purchase orders.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open the Manage Your Solution (APS_BCT_SPRO) app. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | On the Manage Your Solution screen, choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 4 | Search for Application Area | On the Configure Your Solution: Realize Phase screen, set the following search filters:Application Area: Sourcing and ProcurementSub Application Area: Operational Procurement | A search result list is displayed. |  |
| 5 | Select Configuration Item | From the search result list, select the Purchase Order Processing configuration item. | The Configure Your Solution - Purchase Order Processing screen is displayed. |  |
| 6 | Select Configuration Step | On the Configure Your Solution - Purchase Order Processing screen, in the Configuration Steps section, choose Configure for the Activate Flexible Workflow for Purchase Orders configuration step. | The Document Types Purchase order Change screen is displayed. |  |
| 7 | Activate Flexible Workflow for Purchase Orders | Enter the following data:Document Type: NB (Standard PO)Scenario based workflow: Select the checkbox. | The scenario-based workflow is active for standard purchase orders.If you’re asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue.Choose Save. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).You're redirected to SAP S/4HANA Cloud Public Edition, where you can log on with your credentials. |  |  |
| 3 | Activate Flexible Workflow for Purchase Orders | Enter the following data:Document Type: NB (Standard PO)Scenario based workflow: Select the checkbox. | The scenario-based workflow is active for standard purchase orders.If you’re asked to enter a customizing request number, either choose your own customizing request or create a new one, then choose Continue.Choose Save. |  |

#### Configure Flexible Workflow for Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this procedure, you configure your release conditions for Purchase Order Approval.

|  |
| --- |
| Note When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as a Configuration Expert . | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Workflow for Purchase Order | Open Manage Workflows for Purchase Order. | The Manage Workflow screen is displayed. |  |
| 3 | Create Manage Workflow | Choose Add and make following entries:Name: Test Workflow for Purchase OrderDescription: Test Workflow for Purchase OrderIn the Preconditions area, select Purchasing group of purchase order is and make following entry:Purchasing group of purchase order is: 001Choose Add another condition and make following entries:Choose Total net amount of purchase order is greater than withPrice: 100Currency: AEDIn Step Sequence area, choose the Add button and make following entries:Type: Release Purchase OrderIn the RECIPIENTS area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHAS-ING_MANAGER)Choose Ok.Step to be completed by: One of the recipients.Choose Add.Choose Save. | The Workflow for Purchase Order is configured. |  |
| 4 | Activate Workflow Item | Select the just created Workflow Item and choose Activate. | The Workflow Item is activated. |  |

## Overview Table

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order Using Advanced App (Optional)](#unique_11) [page ] 11 | Purchaser | This activity is used to create Purchase Orders manually (without requisitions). | Purchase Order is created. |
| [Approve Purchase Order](#unique_12) [page ] 12 | Purchasing Manager | This activity is used to approve Purchase Orders. | Purchase Order is approved. |
| [Display Purchase Order (as a Supplier in SAP Business Network for Procurement)](#unique_13) [page ] 13 | Supplier(!) via supplier.ariba.com | This activity is used to display the purchase order in the Ariba Network. | PO is sent out to supplier according to the customizing in the output parameters. |
| [Change Purchase Order (Optional)](#unique_14) [page ] 14 | Purchaser | This activity is used to edit/display a purchase order. |  |
| [Create Confirmation in SAP Business Network for Procurement (Optional)](#unique_15) [page ] 15 | Purchaser | This activity is used to edit/display a purchase order. |  |
| [Check Purchase Order Confirmation (Optional)](#unique_16) [page ] 16 | Purchaser | This activity is used to edit/display a purchase order. |  |
| [Create Shipping Notification in SAP Business Network for Procurement (Optional)](#unique_17) [page ] 17 | Purchaser | This activity is used to edit/display a purchase order. |  |
| [Check Inbound Delivery for Purchase Order (Optional)](#unique_18) [page ] 18 | Purchaser | This activity is used to edit/display a purchase order. |  |
| [Set Up the Putaway of Goods for Inbound Delivery](#unique_19) [page ] 19 | Warehouse Clerk | This activity is used to post the Goods Receipt. | Goods receipt for PO is posted. |
| [Check Goods Receipt Details (optional)](#unique_20) [page ] 21 | Warehouse Clerk | Verify part number and quantity of goods received. |  |
| [Display Goods Receipt (as a Supplier in SAP Business Network for Procurement)](#unique_21) [page ] 22 | Supplier(!) via supplier.ariba.com | This activity is used to display the goods receipt in the Ariba Network. |  |
| [Create Supplier Invoice with PO/GR Relation](#unique_22) [page ] 22 | Supplier(!) via supplier.ariba.com | This activity is used to create the supplier invoice. | The Supplier Invoice/Credit Memo is created. |
| [Release Supplier Invoice for Payment (Optional)](#unique_23) [page ] 25 | Accounts Payable Accountant | This activity is used to approve the supplier invoice. |  |
| [Display Invoice Status Change (as a Supplier in SAP Business Network for Procurement)](#unique_24) [page ] 25 | Supplier(!) via supplier.ariba.com |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Purchase Order Using Advanced App (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

|  |
| --- |
| Note Use Advanced app if you want to see the Confirmation and Inbound Delivery and this is optional. |

In this procedure, you create a purchase order for stock material directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad using the Purchaser role. | The Fiori Launchpad displayed. |  |
| 2 | Open Create Purchase Order App | In the Purchase Orders Processing group, open Create Purchase Order Advanced. | The Create Purchase Order screen is displayed. |  |
| 3 | Enter Purchase Order data | Enter all of the necessary data.Order Type: Standard OrderVendor: 33300080Company Code: 3310Purchasing Group: 001Purchasing Org.: 3310ItemsMaterial: TG0011Quantity: 100 PCDelivery date: Today + 1 monthNet Price: 30 AEDPlant: 3310Storage Location: 331AItem Details - ConfirmationsConf Control: Confirmations |  |  |
| 4 | Check Purchase Order for completeness | Choose the Check button. | The Purchase Order is complete if no error dialog box is displayed.If a dialog box is displayed, a correction of the entries must be made to correct the purchase order. |  |
| 5 | Correct Issues | Choose the Display Messages button. Check and correct the entries for errors. | You have corrected any issues. |  |
| 6 | Save Purchase Order | Choose Save. | A new Purchase Order is created, and the system displays Standard PO created under the number 450000XXXX. Make a note of this purchase order number. |  |

### Approve Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you release a purchase order. Purchase orders with a net value of 500 USD (global release amount is configured in USD and converted to the country/region currency amount) or more require an approval (for Purchasing Group 001 and 003).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad using the Purchasing Manager role. | The Fiori Launchpad is displayed. |  |
| 2 | Open Approve Purchase Order | Open My Inbox. | The My Inbox screen is displayed.A list of already created Purchase Orders with needed approval is displayed. |  |
| 3 | Select Purchase Order | Search for Purchase Order xxx and select. | The Purchase Order xxx is displayed.'The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 USD or more have the status In Approval. |  |
| 4 | Approve the Purchase Order | Choose the Approve button.Enter the approval reason if needed, then choose Submit. |  |  |

### Display Purchase Order (as a Supplier in SAP Business Network for Procurement)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log in to SAP Business Network for Procurement as a supplier and display the purchase order in SAP Business Network for Procurement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network for Procurement as a Supplier on supplier.ariba.com. | The Home screen opens. |  |
| 2 | Select the purchase order | Choose Orders > Orders and Releases . Select a Purchase Order ID. | The Purchase Order is displayed. |  |

|  |
| --- |
| Note Remember that the following steps are again performed in the SAP S/4HANA system. |

### Change Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can change an existing purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using the Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Manage Purchase Orders. | The Manage Purchase Orders screen is displayed.A list of already created Purchase Orders is displayed. |  |
| 3 | Select Purchase Order | Select the row for a Purchase Order. | The Edit Purchase Order xxx screen is shown. The Purchase order is opened in change mode. |  |
| 4 | Change Purchase Order | Change certain field values of the Purchase Order. | The Purchase Order values are changed. |  |
| 5 | Check Purchase Order for completeness | Choose the Simulate button. | The Purchase Order is complete. |  |
| 6 | Messages | Choose the Messages button (if possible). | If a message is displayed, a correction of the purchase order entries is necessary. If no message is displayed, the Purchase Order is complete. |  |
| 7 | Save Purchase Order | Choose the Submit button to save the Purchase Order. | The Purchase Order is saved and the system displays a message Purchase order xxx updated. |  |

### Create Confirmation in SAP Business Network for Procurement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, the supplier confirms the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network for Procurement as a Supplier on supplier.ariba.com | The Home screen displayed. |  |
| 2 | List New Purchase Orders | Click on Inbox and then on Orders and Releases.Open the Search Filters pane.Set the value of Data Range field as Last 24 HoursClick on Search. | The system displays a list of new purchase orders. |  |
| 3 | Display Purchase Order | Click on the Purchase Order number to display the Purchase Order. | The purchase order displayed |  |
| 4 | Confirm Purchase Order | Click on Create Order Confirmation button and select Confirm Entire Order button.Enter the following values:Confirmation #: PO ConfirmationEst. Shipping Date: TodayEst. Delivery Date: TodayPress Next button, then Submit. | Status of Purchase Order is changed to Confirmed. |  |
| 5 | Back to Launchpad | Choose the Done button to return to the list | List of Purchase Orders displayed |  |

### Check Purchase Order Confirmation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can check purchase order confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad using the Purchaser role. | The Fiori Launchpad displayed. |  |
| 2 | Open Tile Manage Purchase Order | In the Purchase Orders Processing group, open Manage Purchase Orders. | The Manage Purchase Orders screen displayed.A list of already created Purchase Orders displayed. |  |
| 3 | Select Purchase Order | Click on the row for a purchase order number you created in previous step. | The Standard PO XXX screen shown. |  |
| 4 | Open Confirmations | Expand Item Details and go to Confirmations tab. | The Purchase Order Confirmation displayed in the list |  |

### Create Shipping Notification in SAP Business Network for Procurement (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes, how to create a shipping notification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Business Network for Procurement as a Supplier on supplier.ariba.com. | The Home screen is displayed. |  |
| 2 | List New Purchase Orders | Choose Inbox > Orders and Releases .Open the Search Filters pane.In the Data Range field, enter Last 24 Hours.Choose Search. | A list of new purchase orders is displayed. |  |
| 3 | Display Purchase Order | Choose a Purchase Order number. | The purchase order is displayed. |  |
| 4 | Create Shipping Notification | Choose Create Ship Notice > Confirm Entire Order .Enter the following data:Packing Slip ID: SLIP ##Actual Shipping Date: TodayActual Delivery Date: Today |  |  |
|  |  | Choose Next > Submit . | The status of the purchase order is changed to Shipped. |  |
| 5 | Return to SAP Fiori launchpad | To return to the list of new purchase orders, choose Done. | The list of new purchase orders is displayed. |  |

### Check Inbound Delivery for Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can check purchase order confirmation

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad using the Purchaser role. | The Fiori Launchpad is displayed. |  |
| 2 | Open Tile Manage Purchase Order | In the Purchase Orders Processing group, open Manage Purchase Orders. | The Manage Purchase Orders screen displayed.A list of already created Purchase Orders displayed. |  |
| 3 | Select Purchase Order | Click on the row for a purchase order number you created in previous step. | The Standard PO XXX screen shown. |  |
| 4 | Open Confirmations tab | Expand Item Details and go to Confirmations tab. | Inbound Delivery number displayed in the Inb Delivery column |  |

### Set Up the Putaway of Goods for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to set up the putaway of material. When material is put away in the warehouse, it is generally transferred from the goods receipt interim storage.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Receiving Specialist or . Inventory Manager |  |  |
| 2 | Access App | Open the Change Inbound Delivery (VL32N) app. | The Change Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (  ), to search for a specific inbound delivery number.Choose Continue. | The Inbound Delivery <Inbound Delivery Number> Change: Overview screen is displayed. |  |
| 4 | Enter Putaway Quantity | On the Inbound Delivery <Inbound Delivery Number> Change: Overview screen, select the Stock placement tab.For the relevant item, copy the value of the Delivery Quantity column and paste the value in the PutawayQty column.Choose Save. | The system message Inbound Delivery <Inbound Delivery Number> has been saved is displayed. |  |

### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to post a goods receipt after the goods that were ordered by a purchase order have arrived at the warehouse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to the SAP Fiori launchpad as Warehouse Clerk. |  |  |
| 2 | Access App | Open the Post Goods Receipt for Inbound Delivery (F2502) app. | The Post Goods Receipt for Inbound Delivery screen is displayed. |  |
| 3 | Search for Inbound Delivery | In the Inbound Delivery field, enter an inbound delivery number.Note You can use the Value Help (), to search for a specific inbound delivery number. | The inbound delivery is automatically displayed. |  |
| 4 | Enter Delivery Note | On the General Information tab, enter a delivery note in the Delivery Note field. |  |  |
| 5 | Select Item | On the Items tab, select the items for which a goods receipt is to be posted. For each of the selected items, choose Unrestricted-Use from the dropdown list in the Stock Type column. | The Post button is activated. |  |
| 6 | Post | Choose Post. | The system message Document created: Material Document <Material Document Number> is displayed. |  |

### Check Goods Receipt Details (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the goods receipt fact sheet is displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad using the Warehouse Clerk role. | The Fiori Launchpad is displayed. |  |
| 2 | Open Material Documents Overview | Open Material Documents Overview. | The Material Documents Overview screen is displayed. |  |
| 3 | Search for Goods Receipts Material Document | Enter the following entries in the data fields, and choose the Go button.Plant: 3310Purchase Order: <xxx> | On the Material Document Overview screen, the relevant Material Documents / Material Document items are shown. |  |
| 4 | Select Material Document for Goods Receipt | Select the row for which you would like to see the material documents. | The list of the Material Documents is displayed.The Goods Receipts Details are shown. |  |
| 5 | Check Goods Receipts Details | Check the Status, the General Data, and the Material Document Items. | The Number of reversed Items should be 0. In the General Data section, the correct Posting Date, Document Date and the Delivery Note are shown. |  |
| 6 | Display Document Flow | Switch to the Document Flow section. | The Document Flow shows the Purchase Order and the Material Document as a flow chart. |  |
| 7 | Back to Launch Pad | Choose the Home button to go back to the Fiori Launch pad. | The Fiori Launch Pad is displayed. |  |

### Display Goods Receipt (as a Supplier in SAP Business Network for Procurement)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log in to SAP Business Network for Procurement as a supplier and display the goods receipt in SAP Business Network for Procurement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Access SAP Business Network for Procurement as a Supplier on supplier.ariba.com | The Home screen opens. |  |
| 2. | Select the Goods Receipt | Inbox > Receipts , select the Receipt Number ID to the corresponding Purchase Order. | The Goods Receipt is displayed. |  |

### Create Supplier Invoice with PO/GR Relation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the supplier invoice. You have two possibilities to create the supplier invoice. In the first procedure (which is the most practical one), the supplier invoice is created by the supplier in SAP Business Network for Procurement. The supplier logs on to their SAP Business Network for Procurement account (on supplier.ariba.com), selects the purchase order to be invoiced, and creates the supplier invoice against it. In the second procedure, the supplier invoice is created in the SAP S/4HANA Cloud Public Edition system (SAP Ariba calls this feature CC invoice). The second procedure is an option if you’ve received a paper invoice instead of an invoice created in SAP Business Network for Procurement.

Procedure 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network for Procurement as a Supplier on [supplier.ariba.com](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Pick Purchase Order to be Invoiced | Choose Inbox > Orders and Releases, select the purchase order to be invoiced, and choose Create Invoice > Standard Invoice. | The Create Invoice screen is displayed. |  |
| 3 | Enter Invoice Header Data | Enter the Invoice #. |  |  |
| 4 | Enter Taxes | On the TAX tab, enter the Rate: (%). |  |  |
| 5 | Post Invoice | To get to the Invoice Submission screen, choose Next. Review the invoice details, and choose Submit. | The invoice is submitted to SAP Business Network for Procurement. It’s routed to the buyer's SAP S/4HANA Cloud Public Edition system.Note If the system requires a Remit To ID, navigate to Invoice Header > View/Edit Addresses, and enter Remit To ID: 1000. |  |

Procedure 2

|  |
| --- |
| Note This procedure is optional. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to your SAP S/4HANA Cloud Public Edition system as an Accounts Payable Accountant - Procurement. |  |  |
| 2 | Access App | Open the Manage Supplier Invoices (F0859) app. | The Create Supplier Invoice screen is displayed. |  |
| 3 | Enter General Data | Make the following entries:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: xxxCurrency: AEDInvoice Date: TodayPosting Date: TodayInvoice Party: 33300080 | The Create Supplier Invoices screen is displayed. |  |
| 4 | Enter Purchase Order References | In the Purchase Order References section, check the references.Enter the following data (use a PO you've created previously).References Document Category: Purchase Order / Scheduling AgreementPurchase Order: xxx | The Purchase Order References screen is displayed. |  |
| 5 | Check Data of Purchase Order Items | Check the amount, the quantity, the tax code, and the tax jurisdiction. | The Purchase Order Item’s table is displayed.The amount and the quantity correspond to the values of the goods receipts. |  |
| 6 | Check Tax code | In the Tax section, check if there’s tax code information and enter the tax amount.Tax Code: If there’s no tax, specify the tax code as Input Tax Non Taxable. | The tax code is included in the simulation. . |  |
| 7 | Simulate Supplier Invoice and Check Messages | Choose Simulate.If there are no differences, the supplier invoice is complete to post.Check the Gross Invoice Amount against the items plus tax amount. (If you use the nontaxable tax code, you don’t have any tax amount.)Choose Nota Fiscal, and check the NF information. | The supplier is complete to post. |  |
| 8 | Post Invoice | Choose Post. | The invoice is posted. The system message Invoice xxx has been posted is displayed. |  |
| 9 | Logon | Log on to SAP Business Network for Procurement on supplier.ariba.com as Supplier. | The Home screen is displayed.Note Please note that this step is performed in Ariba Network (as a Supplier). |  |
| 10 | Display Invoice | Choose Outbox > Invoices, and select the Invoice ID. | The invoice is displayed. |  |

### Release Supplier Invoice for Payment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, a supplier invoice is approved.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad using the Accounts Payable Accountant role. | The Fiori Launchpad is displayed. |  |
| 2 | Open Tile Supplier Invoice List | Open Supplier Invoices List. | The Supplier Invoices list screen is displayed. |  |
| 3 | Search for Blocked Supplier Invoices | On the Supplier Invoice List list, search for your invoice, which is Blocked for Payment. | If an invoice has been blocked for payment, a Blocked for Payment: Yes message is displayed. |  |
| 4 | Release the Invoice | Choose Release. | The invoice is released. |  |
| 5 | Back to Fiori Launch Pad | Choose the Home button to go back to the Fiori Launch Pad. | The Fiori Launch Pad is displayed. |  |

### Display Invoice Status Change (as a Supplier in SAP Business Network for Procurement)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you log in to SAP Business Network for Procurement as a Supplier and display the status of the update of the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network for Procurement as a Supplier on supplier.ariba.com. | The Home screen opens. |  |
| 2 | Display Invoice | Go to Outbox > Invoices .Display the invoice related to the previously created Purchase Order (xxx). | The invoice is displayed. |  |
| 3 | Check Invoice Status | The invoice status should be Sent or Approved. |  |  |

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
> Flagged while digesting this document, not verified: Approval threshold appears inconsistent within the document: the Approve Purchase Order section says POs of 500 USD or more require approval (Purchasing Groups 001 and 003), while the Configure Flexible Workflow step sets the release condition at total net amount greater than 100 AED for purchasing group 001.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[10-procurement/test-script-automation-of-central-procurement-quote-with-sap-business]]
- related-to :: [[08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4]]
- related-to :: [[10-procurement/test-script-automation-of-source-to-pay-with-sap-business-network-42k]]
- related-to :: [[10-procurement/test-script-integration-of-procurement-with-external-suppliers-2ej-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J82_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 45,225 chars in the whole document
