---
id: 08-sales-order-management/test-script-automation-of-order-to-invoice-with-sap-business-network-4
title: "Test Script: Automation of Order-to-Invoice with SAP Business Network (4A1_AE) - SAP S/4HANA Cloud Public Edition (4A1_S4CLD2608_BPD_EN_AE)"
description: "SAP Best Practices test script (scope item 4A1, UAE) for supplier-side order-to-invoice with SAP Business Network: prerequisites, setup, 14 test steps."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/b2b-sales-integration, topic/business-network-purchase-to-pay]
aliases: [4A1_S4CLD2608_BPD_EN_AE]
keywords: [B2B Sales Integration with Buyers and SAP Business Network, order-to-invoice automation, sap business network, test scripts, business roles, purchase orders, purchase order approval, flexible workflow, sales orders, outbound delivery]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4A1_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1006
topic: 08-sales-order-management/b2b-sales-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Automation of Order-to-Invoice with SAP Business Network (4A1_AE) - SAP S/4HANA Cloud Public Edition (4A1_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4A1_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **B2B Sales Integration with Buyers and SAP Business Network** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Automation of Order-to-Invoice with SAP Business Network (4A1_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854381)

[2 Prerequisites 4](#_Toc232854382)

[2.1 Additional Manual Configuration 4](#_Toc232854383)

[2.2 System Access 4](#_Toc232854384)

[2.3 Roles at Purchasing Side 4](#_Toc232854385)

[2.4 Roles at Sales Side 5](#_Toc232854386)

[2.5 Master Data, Organizational Data at Purchasing Side 6](#_Toc232854387)

[2.6 Master Data, Organizational Data at Sales Side 7](#_Toc232854388)

[2.7 Business Conditions 8](#_Toc232854389)

[2.8 Preliminary Steps 8](#_Toc232854390)

[2.8.1 Open New MM Posting Period 8](#_Toc232854391)

[2.8.2 Activate Flexible Workflow for Purchase Orders 9](#_Toc232854392)

[2.8.3 Configure Flexible Workflow for Purchase Order 10](#_Toc232854393)

[2.8.4 Set Initial Stock for Material 12](#_Toc232854394)

[2.8.5 Change Pricing Condition 14](#_Toc232854395)

[3 Overview Table 16](#_Toc232854396)

[4 Test Procedures 18](#_Toc232854397)

[4.1 Create Purchase Order 18](#_Toc232854398)

[4.2 Approve Purchase Order (Optional) 20](#_Toc232854399)

[4.3 Display Purchase Order (as a Supplier in SAP Business Network) 21](#_Toc232854400)

[4.4 Display Sales Orders 22](#_Toc232854401)

[4.5 Send Order Confirmation 23](#_Toc232854402)

[4.6 Check Order Confirmation (as a Supplier in SAP Business Network) 24](#_Toc232854403)

[4.7 Create Outbound Delivery 24](#_Toc232854404)

[4.8 Pick Delivery Item and Post Goods Issue 25](#_Toc232854405)

[4.9 Send Advanced Shipping Notification 26](#_Toc232854406)

[4.10 Check Advanced Shipping Notification (as a Supplier in SAP Business Network) 27](#_Toc232854407)

[4.11 Check Inbound Delivery for Purchase Order Confirmations (Optional) 27](#_Toc232854408)

[4.12 Create Billing Document 28](#_Toc232854409)

[4.13 Send Customer Invoice 29](#_Toc232854410)

[4.14 Check Invoice (as a Supplier in SAP Business Network) 30](#_Toc232854411)

## Purpose

Overview

Integrate SAP S/4HANA Cloud Public Edition with SAP Business Network to simplify and automate exchanging sales documents and their follow-on messages as a supplier (SAP S/4HANA Cloud Public Edition) with buyers through SAP Business Network.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/c80f42e1f13dfde8d7e47a1a0d62a758)

### System Access

| System | Details |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles at Purchasing Side

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
| Configuration Expert (Cloud) | SAP_BR_BPC_EXPERT |  |  |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable | SAP_BR_AP_MANAGER |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |

### Roles at Sales Side

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) |
| --- | --- | --- | --- |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |

### Master Data, Organizational Data at Purchasing Side

The organizational structure and master data of your company is created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing Group | 001 | Group 001 |  |
| Vendor/Supplier | 33300084 | Vendor domestic United Arab Emirates Ariba |  |
| Material | SP001 | Trading Good for Regular Procurement (PD planning) |  |

### Master Data, Organizational Data at Sales Side

The organizational structure and master data of your company is created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure:

| Master data | Value | Master. data details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Shipping Point | 3310 |  |  |
| Customer | 33100080 | Vendor domestic United Arab Emirates Ariba |  |
| Material | TG11 | Trading Good for Regular Procurement (PD planning) |  |

For more information on creating master data objects, refer to the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Master Data Script Text |
| --- | --- |
| BET | Create Sales Pricing Condition - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the procedure described in the Create New Open MM Posting Period - MDS (BNZ) master data script. The posting period is up to date. |
| J60 - Accounts Payable | Update BP master data with payment method T.Review and complete the Invoice payment preparation section. |

To run through this scope item, the materials must be available in stock. You can create stock using the Manage Stock (F1062__sap_mmimtype_manage) app, or the Transfer Stock - In-Plant (F1061) app in the SAP Fiori launchpad.

### Preliminary Steps

#### Open New MM Posting Period

|  |
| --- |
| Note This is an external process. |

Information on material stock and certain valuation data such as total stock value, total stock, evaluation elements class, price control indicator, and price unit are held by financial posting period. The period must be set up at the beginning of each new posting period to ensure that values and goods movement are posted to the correct period. Usually, only the current posting period is open for posting. All other posting periods are closed.

To close an MM posting period, and open a new posting period, run the procedure described in the Create New Open MM Posting Period - MDS (BNZ) master data script.

#### Activate Flexible Workflow for Purchase Orders

Use

In this procedure, you activate flexible workflow for purchase order approval.

If you want to use the flexible workflow to approve the purchase order, you have to process the following procedure, and the procedure described in [Configure Flexible Workflow for Purchase Order](#unique_12) [page ] 10.

Prerequisites

To carry out the following activity, a business user with a business role must exist. The business role must contain the business catalog SAP_CORE_BC_COM (Communication Management), for example, the business role SAP_BR_ADMINISTRATOR (Administrator) is required.

Additionally, the business role SAP_BR_BPC_EXPERT must be assigned to the user

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
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Flexible Workflow for Purchase Orders.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT). |  |  |
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

In this procedure, you configure your release conditions for purchase order approval.

When you start to process this step, please make sure that the flexible workflow for purchase document type NB has been activated in your system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Workflows for Purchase Orders (F2872) app. | The Manage Workflow screen is displayed. |  |
| 3 | Create a New Workflow | On the Manage Workflow screen, choose Add, and enter the following data:Header sectionIn the Name field, enter Test Workflow for Purchase Order.Properties sectionIn the Description field, enter Test Workflow for Purchase Order.Start Conditions sectionFrom the dropdown list, select Purchasing group of purchase order is.In the Purchasing Group field, enter 001.Choose Add another condition (  ). From the dropdown list, select Total net amount of purchase order is greater than, and enter the following data:Amount: 100Currency: AEDIn the Step Sequence section, choose Add. The Automatic Release of Purchase Order screen is displayed.On the Automatic Release of Purchase Order screen, enter the following data:Header sectionIn the Step Type field, select Release Purchase Order from the dropdown list.Recipients sectionIn the Assignment By field, select Manager of Workflow Initiator from the dropdown list.In the Role field, select Manager of Workflow Initiator from the dropdown list.In the Step to be completed by field, select the One of the Recipients checkbox.Choose Add > Save . | The workflow for purchase order is configured. |  |
| 4 | Activate Workflow Item | Select the created workflow item, and choose Activate. | The workflow item is activated. |  |

#### Set Initial Stock for Material

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This procedure describes how to set the initial stock for material.

Prerequisites

To run through this scope item, the materials must be available in stock.

Procedure

| Test Step # | Test step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as Warehouse Clerk. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Post Goods Movement (MIGO) app. | The Goods Receipt Other screen is displayed.It's displayed this way only if it was your last transaction. Select the Reference Document for MIGO TransactionOther field. |  |
| 3 | Enter Movement Type | Select the following options:Goods Receipt - Executable Action in Transaction MIGOOther - Reference Document for MIGO TransactionChoose Enter. |  |  |
| 4 | Enter Material Number | On the Material tab, enter a material number in the Material field, and choose Enter. |  |  |
| 5 | Enter Material Quantity | On the Quantity tab, enter the following data according to your business requirements:ExampleQty in Unit of Entry: Quantity in UOMUnit of Entry: PCChoose Enter. |  |  |
| 6 | Enter Location Information | On the Where tab, enter the following data:ExampleMovement Type: 561- Receipt per initial entry of stock balances into unr.-usePlant: <Plant>Storage Location: <Storage Location>Choose Enter. |  |  |
| 7 | Enter Batch Information (Optional) | Note This step is required for batch-relevant materials only.On the Batch tab, enter a date in the Date of manufacture field, and choose Enter. |  |  |
| 8 | Post Information | Save your entries, and choose Post. |  |  |

#### Change Pricing Condition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This procedure describes how to change pricing conditions. The price in the sales order needs to correspond with the price in the purchase order.

Prerequisites

For more information on creating master data objects, refer to the Master Data Scripts (MDS) Create Sales Pricing Condition - MDS (BET) as listed in [Master Data, Organizational Data at Sales Side](#unique_8) [page ] 7.

Procedure

| Test Step # | Test step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad as Pricing Specialist. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Set Material Prices - Sales (VK12) app. | The Change Condition Records screen is displayed. |  |
| 3 | Set Pricing Condition Type | In the Condition Type field, enter PPR0, for example.Note You can use the Value Help (), to search for a specific condition type.Press Enter. | The Key Combination dialog box is displayed. |  |
| 4 | Select Key Combination | In the Key Combination dialog box, select the Material with release status checkbox, and choose Choose. | The Change Price (PPR0): Selection screen is displayed. |  |
| 5 | Select Key Combination | On the Change Price (PPR0): Selection screen, enter the following data according to your business requirements:ExampleSales Organization: 3310Distribution Channel: 10Material: TG11Valid On: <Today>Choose Execute. | The Change Price Condition (PPR0) : Overview screen is displayed. |  |
| 6 | Change Price Condition | On the Change Price Condition (PPR0) : Overview screen, enter the following data according to your business requirements:ExampleMaterial: TG11Amount: 20.05Unit: AEDValid From: <First day of the current year>Valid To: <Last day of the current year>Choose Save. | You've changed the pricing condition. |  |

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

|  |
| --- |
| Note Only the mandatory chapters that need to be edited manually are displayed in the overview. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Purchase Order](#unique_16) [page ] 18 | Purchaser | Create Purchase Order - Advanced (ME21N) | A new purchase order is created. |
| [Approve Purchase Order (Optional)](#unique_17) [page ] 20 | Purchasing Manager | My Inbox - All Items (F5331) | A purchase order is approved. |
| [Display Purchase Order (as a Supplier in SAP Business Network)](#unique_18) [page ] 21 | Supplier in SAP Business Network | [supplier.ariba.com](https://service.ariba.com/) | A purchase order is displayed. |
| [Display Sales Orders](#unique_19) [page ] 22 | Internal Sales Representative | Manage Sales Orders (F1873) | The newly created sales order is displayed in SAP S/4HANA Cloud Public Edition. |
| [Send Order Confirmation](#unique_20) [page ] 23 | Internal Sales Representative |  | The order confirmation is automatically created based on the sales order. |
| [Check Order Confirmation (as a Supplier in SAP Business Network)](#unique_21) [page ] 24 | Supplier in SAP Business Network | [supplier.ariba.com](https://service.ariba.com/) | You reviewed the purchase order confirmation. |
| [Create Outbound Delivery](#unique_22) [page ] 24 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | The creation of an outbound delivery for the previously received sales order (purchase order) is triggered. |
| [Pick Delivery Item and Post Goods Issue](#unique_23) [page ] 25 | Shipping Specialist | Pick Outbound Delivery (F0868) | The delivery is picked, and the goods issue is posted. |
| [Send Advanced Shipping Notification](#unique_24) [page ] 26 | Shipping Specialist |  | The Advanced Shipping Notification (ASN) is automatically sent by the supplier with details about the purchase order, and quantity to the buyer. |
| [Check Advanced Shipping Notification (as a Supplier in SAP Business Network)](#unique_25) [page ] 27 | Supplier in SAP Business Network | [supplier.ariba.com](https://service.ariba.com/) | The order status of the purchase order is Shipped. |
| [Check Inbound Delivery for Purchase Order Confirmations (Optional)](#unique_26) [page ] 27 | Purchaser | Manage Purchase Orders (Version 2) (F0842A) | You checked the inbound delivery for purchase order confirmation. |
| [Create Billing Document](#unique_27) [page ] 28 | Billing Clerk. | Create Billing Documents (F0798) | The system generates an invoice for billing. |
| [Send Customer Invoice](#unique_28) [page ] 29 |  |  | The supplier invoice is automatically sent by the supplier to the buyer. |
| [Check Invoice (as a Supplier in SAP Business Network)](#unique_29) [page ] 30 | Supplier in SAP Business Network | [supplier.ariba.com](https://service.ariba.com/) | The invoice document is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Caution To complete the end-to-end test, the scope item [Automation of Source-to-Pay with SAP Business Network (42K)](https://me.sap.com/processnavigator/SolP/42K) needs to be activated and set up. |

### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create a purchase order for stock material.

Prerequisites

|  |
| --- |
| Note This procedure is a preliminary step before you can start testing this scope item. For questions and issues with the following procedure, see scope item [Automation of Source-to-Pay with SAP Business Network (42K)](https://me.sap.com/processnavigator/SolP/42K). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as Purchaser. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the Manage Purchase Orders (F0842A) app. | The Manage Purchase Orders screen is displayed. |  |
| 3 | Create Purchase Order | Choose Create. | The New Purchase Order screen is displayed. |  |
| 4 | Enter Purchase Order Data | Enter the following data:Basic DataOrder Type: Standard PO (NB)Supplier: 33300084OrganizationPurchasing Group: 001Company Code: 3310Purchasing Organization: 3310ItemsChoose Create and enter the following data.Material: SP001Plant: 3310Order Quantity: 100 PCNet Order Price: 17.55 AEDSelect the purchase order item. On the Purchase Order Item screen, go to the Delivery Details tab and enter the following data:Overdelivery Tolerance Limit: 10%Underdelivery Tolerance Limit: 15%Storage Location: 331AGo to the Supplier Confirmation Control tab. In the Confirmation Control field, select Confirmations from the dropdown list.Note The supplier material number is not visible in the Manage Purchase Orders (F0842A) app. To check the supplier material number, access the Display Purchase Order - Advanced (ME23N) app. |  |  |
| 5 | Change Delivery Address | Go to the Delivery Address tab. Change the delivery address according to your business requirements. | The delivery address is changed. |  |
| 6 | Return to Header Level | Choose Apply. | The New Purchase Order screen is displayed. |  |
| 7 | Attach File | Go to the Attachments tab. To upload an attachment, choose Upload.Select an attachment and choose Open. | The uploaded file is displayed in the Attachments section. |  |
| 8 | Save Purchase Order | To save the purchase order, choose Order. | A new purchase order is created. The system message Purchase order has been created is displayed.Note To use this purchase order number for further procedures, make a note of it. |  |

### Approve Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to approve and release a purchase order. For the purchasing groups 001 and 003, purchase orders with a net value of 500 USD (global release amount is configured in USD and converted to the country/region currency amount) or more require an approval.

Prerequisites

|  |
| --- |
| Note This procedure is a preliminary step before you can start testing this scope item. For questions and issues with the following procedure, see scope item [Automation of Source-to-Pay with SAP Business Network (42K)](https://me.sap.com/processnavigator/SolP/42K). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to SAP Fiori launchpad using the Purchasing Manager role. | SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen is displayed.A list of already created purchase orders with needed approval is displayed. |  |
| 3 | Select Purchase Order | Search for Purchase Order xxx and select one. | The Purchase Order xxx is displayed.The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 USD or more have the status In Approval. |  |
| 4 | Approve the Purchase Order | Choose Approve.If needed, enter the approval reason, and choose Submit. |  |  |

### Display Purchase Order (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display a purchase order as a supplier in SAP Business Network.

Prerequisites

|  |
| --- |
| Note This procedure is a preliminary step before you can start testing this scope item. For questions and issues with the following procedure, see scope item [Automation of Source-to-Pay with SAP Business Network (42K)](https://me.sap.com/processnavigator/SolP/42K). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Access SAP Business Network as a Supplier on [https://supplier.ariba.com/](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | Choose Orders > Purchase Orders , and select the Purchase Order ID. | The purchase order is displayed. |  |

### Display Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to display newly created sales orders in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad of your SAP S/4HANA Cloud Public Edition system as a Internal Sales Representative. |  |  |
| 2 | Access App | Open the Manage Sales Orders (F1873) app. |  |  |
| 3 | Search for Sales Order | In the Customer Reference field, enter the purchase order number of the purchase order that you've created in [Create Purchase Order](#unique_16) [page ] 18. Choose Go. | A search results list is displayed. |  |
| 4 | Display Sales Order | Select a sales order number from the search results list and select Change Sales Order. | The sales order is displayed. |  |
| 5 | Check Ship-to Address | On the General Information tab, check the ship-to address. | The partner address equals the partner address that was set in [Create Purchase Order](#unique_16) [page ] 18. |  |
| 6 | Check Price | On the Items tab, check if the price of the sales order corresponds with the price of the purchase order that you've created in [Create Purchase Order](#unique_16) [page ] 18.Note If the price doesn't correspond, correct the price of the sales order manually. |  |  |
| 7 | Check Status Overview | On the Status and Blocks tab, check the order status. | The status for header and items fields is Complete. |  |
| 8 | Display Sales Order in VA02 | Go back to the Manage Sales Orders screen.Select a sales order number from the search results list and select Change Sales Order - VA02. | The Change Standard Order <Sales Order Number>: Overview screen is displayed. |  |
| 9 | Check Delivery Tolerance | On the Sales tab, go to the All Items section.Select the sales document item 10.Go to the Shipping tab. Check whether the delivery tolerance with the values set in [Create Purchase Order](#unique_16) [page ] 18. |  |  |

### Send Order Confirmation

Purpose

The order confirmation change is automatically sent to the buyer system.

Prerequisites

A sales order must have been created in the SAP S/4HANA Cloud Public Edition system on supplier side.

Procedure

This step is automatically generated.

### Check Order Confirmation (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the order confirmation as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [https://supplier.ariba.com/](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | Choose Orders > Purchase Orders . Select the Purchase Order ID. | The purchase order is in status Confirmed. |  |

### Create Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to create an outbound delivery for the previously received sales order (purchase order) in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Open the Create Outbound Deliveries - From Sales Orders (F0869A) app. | The Create Outbound Deliveries screen is displayed. |  |
| 3 | Search Sales Order | To search for a sales order, enter the following data:Shipping point: 3310Sales Document: <Sales order number created previously>Choose Go. | The sales order is displayed. |  |
| 4 | Create Delivery | Select your sales order, and choose Create Deliveries. | The creation of an outbound delivery for the previously received sales order (purchase order) is triggered. |  |

### Pick Delivery Item and Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to enter the results of the picking process for a particular delivery. The picking process involves taking goods from a storage location, and staging the right quantity in a picking area, where the goods are prepared for shipping. The goods issue is posted in the SAP S/4HANA Cloud Public Edition.

|  |
| --- |
| Note The Pick Outbound Delivery (F0868) app can't handle delivery items with batches. To edit handle deliveries with batch-manages materials, use the Change Outbound Delivery (VL02N) app instead. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access App | Choose the Pick Outbound Delivery (F0868) tile. |  |  |
| 3 | Enter Delivery Number | To display an outbound delivery, enter a delivery number in the Delivery field.Note You can use the Value Help (), to search for a specific outbound delivery. | The outbound delivery is displayed. |  |
| 4 | Enter Actual GI Date | In the Actual GI Date field, enter today's date. |  |  |
| 5 | Enter Picked Quantity | On the Picking tab, choose Delivery Items by selecting the respective checkbox.For each selected delivery item, enter a quantity in the Picking Quantity field.Choose Copy Picking Quantity. | The system message Available picking quantities successfully copied to delivery quantity is displayed and you're forwarded to the GI ready tab. |  |
| 6 | Post Goods Issue | On the GI ready tab, choose Post GI. | The system message GI posted is displayed. |  |

### Send Advanced Shipping Notification

Purpose

The Advanced Shipping Notification (ASN) is automatically sent by the supplier with details about the purchase order, and quantity to the buyer.

Prerequisites

Goods issued must have been posted in SAP S/4HANA Cloud Public Edition.

Procedure

This step is automatically generated.

### Check Advanced Shipping Notification (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the invoice of the purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [https://supplier.ariba.com/](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | Choose Orders > Purchase Orders . Select the Purchase Order ID. | The purchase order is in status Shipped. |  |

### Check Inbound Delivery for Purchase Order Confirmations (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the inbound delivery for purchase order confirmations.

Prerequisites

|  |
| --- |
| Note This procedure is a necessary step before you can continue testing this scope item. For questions and issues with the following procedure, see scope item [Automation of Source-to-Pay with SAP Business Network (42K)](https://me.sap.com/processnavigator/SolP/42K). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Purchaser. |  |  |
| 2 | Access App | Open the Manage Purchase Orders (Version 2) (F0842A) app. | The Manage Purchase Orders screen, and a list of already created purchase orders are displayed. |  |
| 3 | Select Purchase Order | Select the purchase order, you previously created. | The Standard PO XXX screen is displayed. |  |
| 4 | Open Confirmations | Expand the Item Details section, and navigate to the Confirmations tab. | The Inbound Delivery Number is displayed in the Inb Delivery column. |  |

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how the supplier creates an invoice for billing in SAP S/4HANA Cloud Public Edition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Log on to SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access App | Open the Create Billing Documents (F0798) app. |  |  |
| 3 | Define Billing Setting | Choose Billing Settings.Enable all of the following settings:Set billing date and type before billingCreate separate billing date for each item of billing due listAutomatically post Billing DocumentsDisplay billing documents after creation. |  |  |
| 4 | Search for Delivery Document | To search for a delivery document, set filter criteria, and choose Go. | A search result list with delivery documents is displayed. |  |
| 5 | Select Delivery Document | Select the delivery document you previously created, and choose Create. | The Create Billing Documents screen is displayed. |  |
| 6 | Maintain Billing Date | On the Create Billing Documents screen, choose the billing type F2 Invoice (F2), and maintain as billing date, for example, the current date. Choose OK > Save. | A new billing document is created. |  |
| 7 | Display Billing Document After Creation | The billing document is automatically displayed. | The system generates an invoice for billing. |  |

### Send Customer Invoice

Purpose

The customer invoice is automatically sent to the buyer.

Prerequisites

The billing document must have been created in SAP S/4HANA Cloud Public Edition.

Procedure

This step is automatically generated.

### Check Invoice (as a Supplier in SAP Business Network)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes how to check the invoice of the purchase order as a supplier in SAP Business Network.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Access SAP Business Network as a Supplier on [https://supplier.ariba.com/](https://supplier.ariba.com/). | The Home screen is displayed. |  |
| 2 | Select Purchase Order | Choose Orders > Purchase Orders . Select the Purchase Order ID and check the invoice number in the Related Documents field. | The invoice number is listed in the Related Documents field. |  |

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
> Flagged while digesting this document, not verified: PO approval threshold: the Approve Purchase Order section says POs of 500 USD or more (purchasing groups 001 and 003) require approval, while the flexible workflow configured in the preliminary steps triggers on purchasing group 001 with net amount greater than 100 AED; the two thresholds differ.

> [!warning] Conflict
> Flagged while digesting this document, not verified: App identifiers differ within the document: the Overview Table lists My Inbox - All Items as F5331 while the Approve Purchase Order procedure uses F0862; the Overview lists Create Purchase Order - Advanced (ME21N) while the procedure uses Manage Purchase Orders (F0842A).

> [!warning] Conflict
> Flagged while digesting this document, not verified: Example prices do not match although the script requires sales and purchase prices to correspond: PO net order price is 17.55 AED while the sales pricing condition PPR0 is set to 20.05 AED.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Check Inbound Delivery for Purchase Order Confirmations is titled (Optional) but its prerequisite note calls it a necessary step before continuing to test this scope item.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/integration-of-sales-with-external-buyers-2el-ae-test-script-sap-s-4ha]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4A1_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 47,994 chars in the whole document
