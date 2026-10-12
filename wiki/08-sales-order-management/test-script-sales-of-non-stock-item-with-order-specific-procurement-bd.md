---
id: 08-sales-order-management/test-script-sales-of-non-stock-item-with-order-specific-procurement-bd
title: "Test Script: Sales of Non-Stock Item with Order-Specific Procurement (BDN_AE) - SAP S/4HANA Cloud Public Edition (BDN_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item BDN_AE (UAE): sales order, purchase order, goods receipt, delivery, billing and supplier invoice steps, with test data."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/non-stock-material-sales]
aliases: [BDN_S4CLD2608_BPD_EN_AE]
keywords: [Sales of Non-Stock Materials, non-stock item sales, order-specific procurement, sales order creation, purchase order creation, purchase order approval, flexible workflow, goods receipt, outbound delivery, picking]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDN_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1256
topic: 08-sales-order-management/non-stock-material-sales
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Sales of Non-Stock Item with Order-Specific Procurement (BDN_AE) - SAP S/4HANA Cloud Public Edition (BDN_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDN_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Sales of Non-Stock Materials** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Sales of Non-Stock Item with Order-Specific Procurement (BDN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861213)

[2 Prerequisites 4](#_Toc232861214)

[2.1 System Access 4](#_Toc232861215)

[2.2 Roles 4](#_Toc232861216)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861217)

[2.4 Business Conditions 6](#_Toc232861218)

[2.5 Preliminary Steps 7](#_Toc232861219)

[2.5.1 Check Flexible Workflow for Purchase Order Approval 7](#_Toc232861220)

[2.5.2 Configure Flexible Workflow for Purchase Order 8](#_Toc232861221)

[2.5.3 Create Purchasing Info Record 9](#_Toc232861222)

[2.5.4 Create Condition Records (Optional) 11](#_Toc232861223)

[3 Overview Table 12](#_Toc232861224)

[4 Test Procedures 14](#_Toc232861225)

[4.1 External Process (Basic Credit Management) (BD6) (Optional) 14](#_Toc232861226)

[4.2 Sales Inquiry (1IQ) (Optional) 14](#_Toc232861227)

[4.3 Sales Contract Management (I9I) (Optional) 15](#_Toc232861228)

[4.4 Sales Quotation (BDG) (Optional) 15](#_Toc232861229)

[4.5 Create Sales Order 16](#_Toc232861230)

[4.6 Process Sales Order Approval (Optional) 18](#_Toc232861231)

[4.7 Create Attachment for Sales Order (Optional) 19](#_Toc232861232)

[4.8 Credit Management Check for Sales Order (Optional) 20](#_Toc232861233)

[4.9 Create Purchase Order 20](#_Toc232861234)

[4.10 Approve and Release Purchase Order (Optional) 21](#_Toc232861235)

[4.11 Post Goods Receipt 22](#_Toc232861236)

[4.12 Create Delivery 24](#_Toc232861237)

[4.13 Create Attachment for Delivery (Optional) 26](#_Toc232861238)

[4.14 Execute Picking 27](#_Toc232861239)

[4.15 Post Goods Issue 28](#_Toc232861240)

[4.16 Create Billing Document 30](#_Toc232861241)

[4.17 Create Attachment for Billing (Optional) 32](#_Toc232861242)

[4.18 Create Supplier Invoice 33](#_Toc232861243)

[5 Appendix 36](#_Toc232861244)

[5.1 Process Integration 36](#_Toc232861245)

[5.1.1 Succeeding Processes 36](#_Toc232861246)

[5.2 Limitations 36](#_Toc232861247)

[5.3 Scheduling Job (alternative) 37](#_Toc232861248)

[5.3.1 Job Scheduling for Delivery Creation (Alternative) 37](#_Toc232861249)

[5.3.2 Job Scheduling for Goods Issue Deliveries (Alternative) 38](#_Toc232861250)

[5.3.3 Job Scheduling for Billing Creation (Alternative) 39](#_Toc232861251)

[5.3.4 Job Scheduling for Billing Release (Alternative) 40](#_Toc232861252)

[5.3.5 Job Scheduling for Billing Output (Alternative) 41](#_Toc232861253)

[5.4 Integration with Advanced ATP – Scope item 1JW 42](#_Toc232861254)

## Purpose

Overview

This scope item enables customers to order goods that may not be in stock. In this case, goods are procured from an external supplier. During sales order creation, a purchase requisition is generated and then converted into a purchase order for the supplier. Goods receipt is created for customer and special stock. After delivery and the creation of a customer invoice, the vendor invoice for the goods receipt can be created.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
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
| Material | TG14 | Trading material with item category group CBUK (Reorder point planning, bought in item)no batch |  |
| Sold-to party | 33100003 | Domestic UAE Customer 3 | You can test the test script using another domestic customer. |
| Ship-to party | 33100003 | Domestic UAE Customer 3 |  |
| Payer | 33100003 | Customer domestic 03 |  |
| Vendor | 3330000133300002 | Domestic UAE Supplier 1Domestic UAE Supplier 2 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A |  | Shipping w/o LWM |
| Shipping Point | 3310 |  |  |
| Sales organization | 3310 |  |  |
| Distribution channel | 10 |  |  |
| Division | 00 |  |  |
| Purchasing Organization | 3310 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS– MDS |
| BND | Create Customer Master - MDS– MDS |
| BNE | Create Supplier Master - MDS– MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

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
| 3 | Create Manage Workflow | Choose Create, and make the following entries:Workflow Name: <Test Workflow for Purchase Order>From the Start Conditions section, add the following preconditions:Purchasing group of purchase order is: SelectedPurchasing Group: 003Choose Create another condition, and make the following entries:Total net amount of purchase order is greater than: SelectedAmount: For example, 10Currency: AEDIn the Steps area, choose Create and make the following entries:Step Type: Release of Purchase OrderIn the RECIPIENTS area, make the following entries:Assignment By: UserUser: Select User from value help (with Employee ID PURCHASING_MANAGER)Choose OK.Step to be completed by: One of the recipients.Choose Create.Choose Save. | The Workflow for Purchase Order is configured. |  |
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

This process step shows you how to create purchasing info record.

|  |
| --- |
| Note If the Info Record for the material TG14 and suppliers 33300001 already exists in the system, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Purchasing Info Records | Choose Manage Purchasing Info Records (F1982) . | The Manage Purchasing Info Records screen displays. |  |
| 3 | Open New Purchasing Info Record | Choose Create. | The Purchasing Info Record Screen displays. |  |
| 4 | Enter Header Data | Make the following entries:Purchasing Info Record Category: <Standard>Purchasing Organization: 3310Supplier: 33300001Material: TG14Plant: 3310Purchasing Group: 002 | Header data is added. |  |
| 5 | Enter General Information | Make the following entries:Available From: TodayAvailable To: 12/31/9999 | General Information is added. |  |
| 6 | Enter Purchasing Data | Make the following entries:Incoterm: EXWIncoterm Location 1: VENDOR | Purchasing Data is added. |  |
| 7 | Enter Delivery and Quantity Data | Make the following entries:Delivery Time in Days: 1Under Delivery Tolerance in %: 10.0Over Delivery Tolerance in %: 10%Tax Code: <Input Tax Code>Order Unit: PCStandard Order Quantity: 10Select the following entries:Goods-Receipt-Based Invoice Verification (GR-Bsd_IV)No Evaluated Receipt Settlement (No ERS) | Delivery and Quantity Data is added. |  |
| 8 | Enter Condition Data | In the Condition section, choose Create. Enter the following data:Valid From: TodayValid To: 12/31/9999Amount: 300Pricing Unit: 1Currency: AEDChoose Apply. | Condition Data is added |  |
| 9 | Enter Reference Data (optional) | Optionally, you can enter reference data. | Reference data is added. |  |
| 10 | Save Your Data | Choose Create. | A purchasing info record is saved. |  |

|  |
| --- |
| Note Material TG14 and Supplier 33300001, its net price is 35 AED. |

|  |
| --- |
| Note Repeat the above step to create the Info Record for Material TG14 and Supplier 33300001, its purchase group is 001. Repeat the above steps to create the Info Record for Material TG14 , its net price is 25 AED. Repeat the above steps and for step 7, don’t select No Evaluated Receipt Settlement. |

#### Create Condition Records (Optional)

Purpose

In case you have finetuned the access sequence of SAP pre-shipped condition types, the relative condition records should be created accordingly.

You can find general information on how to create your own master data in the following: [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BEW | Create Free Goods Condition - MDS |

## Overview Table

The test script Sales of Non-Stock Item with Order-Specific Procurement (BDN) consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [External Process (Basic Credit Management) (BD6) (Optional)](#unique_12) [page ] 14 |  |  |  |
| [Sales Inquiry (1IQ) (Optional)](#unique_13) [page ] 14 |  |  |  |
| [Sales Contract Management (I9I) (Optional)](#unique_14) [page ] 15 |  |  |  |
| [Sales Quotation (BDG) (Optional)](#unique_15) [page ] 15 |  |  |  |
| [Create Sales Order](#unique_16) [page ] 16 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage sales order screen displays. |
| [Create Attachment for Sales Order (Optional)](#unique_17) [page ] 19 | Internal Sales Representative | Manage Sales Orders (F1873) | The Manage sales order screen displays. |
| [Credit Management Check for Sales Order (Optional)](#unique_18) [page ] 20 |  |  |  |
| [Create Purchase Order](#unique_19) [page ] 20 | Purchaser | Process Purchase Requisitions (F1048A) | The Process Purchase Requisitions screen displays. |
| [Approve and Release Purchase Order (Optional)](#unique_20) [page ] 21 | Purchasing Manager | Approve Purchase Orders |  |
| [Post Goods Receipt](#unique_21) [page ] 22 | Warehouse Clerk | Post Goods Movement (MIGO) |  |
| [Create Delivery](#unique_22) [page ] 24 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) |  |
| [Create Attachment for Delivery (Optional)](#unique_23) [page ] 26 | Shipping Specialist | Display Outbound Delivery (VL03N) |  |
| [Execute Picking](#unique_24) [page ] 27 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Post Goods Issue](#unique_25) [page ] 28 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods Issue is posted. |
| [Create Billing Document](#unique_26) [page ] 30 | Billing Clerk | Create Billing Documents (F0798) | The Create Billing Document screen displays. |
| [Create Attachment for Billing (Optional)](#unique_27) [page ] 32 | Billing Clerk | Manage Billing Documents (F0797) | The Manage Billing Documents screen displays. |
| [Create Supplier Invoice](#unique_28) [page ] 33 | Accounts Payable Accountant | Create Supplier Invoice (F0859) |  |

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

### External Process (Basic Credit Management) (BD6) (Optional)

External Process

For this activity, run the following steps from the Basic Credit Management (BD6) test script:

- Set a Credit Limit

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
| Note If you want to use the optional link between scope item Sales Inquiry (1IQ) and Sales of Non-Stock Item with Order-Specific Procurement (BDN) this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order). |

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
| Note If you want to use the optional link between scope item Sales Contract Management (I9I) and Sales of Non-Stock Item with Order-Specific Procurement (BDN) this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order). |

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
| Note If you want to use the optional link between scope item Sales Quotation (BDG) and Sales of Non-Stock Item with Order-Specific Procurement (BDN) this reference only works if you use consistent master data (such as Business Partner for the customer quotation and the customer sales order). |

### Create Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the sales order for a material procured externally (bought-in-item).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873) . | The Manage Sales Order screen displays |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders screen, choose Create and select Create Sales Order - VA01. |  |  |
| 4 | Enter Sales Document Type | Make the following entries and choose Continue:Order Type: ORSales Organization: 3310Distribution Channel: 10Division: 00 | The Create Standard Order: Overview screen displays. |  |
| 5 | Enter Order Details | Make the following entries:Sold-to Party: 33100005Cust. Reference: <Reference number>,for example, BII-001Material: <Material Number>, for example, TG14Order Quantity: <Quantity>, for example, 10UN: <Sales Unit> , for example, PCPlant: 3310NoteYou can manually change the item category to DBAB if the item is down payment relevant for 3rd party sales order with Order-Specific Procurement, and proceed with following steps: Change Sales Orders (Remove Billing Block), Create Down Payment Request and Post a Down Payment from scope item Sales Order Processing with Customer Down Payment (BKJ).You can manually change the item category to CBXB if the item is free of charge for 3rd party sales order with shipping notification. This item category is free of charge with a 100% rebate and can be invoiced ( external & proforma invoice).You can manually change the item category to CBXL if the item is free of charge for 3rd party sales order with shipping notification. This item category is without pricing and can NOT be invoiced ( external & proforma invoice).You can manually change the schedule line category to SI if the material is subcontract relevant. |  |  |
| 6 | Save | Choose Save.If it pops up the screen Standard Order: Purchase Order Scheduling, choose Complete dlv. and then choose Save. | The sales order is created. The purchase requisition is generated using the item category of the sales order. And, you can find Purchase Requisition number in the tab of Schedule lines at item level. |  |

|  |
| --- |
| Note If the credit limit check was unsuccessful, the system does not generate a purchase requisition. Depending on the setting in customizing, the sales order would then be incomplete.Depending on the entries within the sales order, you might receive warning messages (for example, warnings regarding prices, quantities, delivery dates, or reorder points; configuration not possible for material TG14).The pricing conditions are determined automatically, however you can change the prices manually. You can view the pricing by Select the Item or Choose Item Conditions.The print-out of the order confirmation is executed automatically, or manually only after the purchase requisition has been transferred to a purchase order. For instructions on manually printing the output, see Manual Printing below. |

Printing form- Output Management

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Order screen displays. |  |
| 3 | Search for Sales Order | Enter search terms in filter bar and choose GoFor example, enter sales order number in Sales Order field. | Sales order is displayed in result list. |  |
| 4 | Navigate to Sales Order Screen | Click sales order number, and choose Display Sales Orders.Note If there is not a Display Sales Orders, then click Define Links. Select Display Sales Orders, and choose OK. | The Display Sales Orders xxx: Overview screen displays. |  |
| 5 | Check Output Condition | On the Display Standard Order xxx: Overview screen, choose Header Output Preview . | The document prints. |  |

|  |
| --- |
| Note It can also be navigated to a fact sheet screen in Manage Sales Orders:On the Manage Sales Orders screen, enter search terms in filter bar and choose Go.In search result, click your sales order number and choose sales order number. |

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

### Credit Management Check for Sales Order (Optional)

External Process

For this activity, run the following steps from the Basic Credit Management (BD6) test script to review the sales orders that might have been blocked due to the credit limit check:

- Management of Blocked Sales Orders

### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A purchase order is the request or instruction from a purchasing organization to a vendor (external supplier) or a plant to deliver a certain quantity of material or to perform services at a certain date. This process step shows you how to create purchase order.

Prerequisite

A purchase requisition has been generated through the sales order in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Process Purchase Requisitions (F1048A). | The Process Purchase Requisitions (F1048A) screen displays. |  |
| 3. | Find the Purchase Requisition | Input the filters in Filter Bar and choose Go if necessary.Plant: 3310 | You can find the purchase requisition number in step Create Sales Order. |  |
| 4. | Choose the Sources of Supply | Click the sources in the line of your purchase requisition, and choose one by click |  |  |
| 5. | Create Purchase Order | Choose the purchase requisition and click Create Purchase Order at the right side center of the screen.If there is any warning message display, choose OK | The Purchase Orders Preview screen displays |  |
| 6. | Submit the Purchase Order | Select the purchase order type: Standard PO, and then choose Save.The purchase order number would be shown in the screen. | The purchase order is created in the SAP system. The system creates a message for the purchase order, so that the information from the purchase order can be transmitted to the vendor |  |

|  |
| --- |
| Note The print-out of the order confirmation is executed after the Purchase Order is created automatically and immediately. |

### Approve and Release Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to release a purchase order. If the total amount of PO >= 500 USD and purchase group is 003. Then the PO should do the approval.

Prerequisite

A purchase order must exist for release.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchasing Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox (F2097). | A list of previously created Purchase Orders display. |  |
| 3 | Search for Purchase Order Status | Make the following entry and choose Enter:Search: <Purchase Order number> | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 AED or more have the status In Approval. |  |
| 4 | Release Purchase Order | Select the Purchase order in left of the screen and choose Release in bottom right. | The Purchase Orders without follow-on documents (w/o status Follow-On Documents) and a net value of 500 USD or more have the status In Approval. |  |
| 5 | Enter Release Reason | Enter the approval reason if needed, and then choose Submit. | The Purchase Order is approved. |  |
| 6 | Back to SAP Fiori Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

|  |
| --- |
| Note If an attachment is uploaded during purchase order creation, in My Inbox APP, the attachment can be found under Attachments tab of the purchase order. The attachment is renamed with prefix “H_”. |

### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A goods receipt is the physical entry of the goods and materials on-stock. The goods receipt usually comes from external suppliers or from in-house production. All goods receipts increase the stock. This process step shows you how to post goods receipt.

|  |
| --- |
| Note In this test script, the goods receipt is posted to an individual sales order stock. The valuation results from the purchase order. |

Prerequisite

The purchase order is created and the purchased material (bought-in-item) has arrived.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). |  |  |
| 3 | Choose Field | Make the following entries and choose Enter:Executable Action in Transaction MIGO: <Goods Receipt>Reference Document for MIGO Transaction: <Purchase Order> |  |  |
| 4 | Input Purchase Order Number | Make the following entries, and choose Enter:Movement Type: GR Goods receipt 101Field next to Purchase Order: <Purchase Order Number> |  |  |
| 5 | Change Quantity | Change the quantity in Unit of Entry in Item details, Quantity tab, from 10 to 9.Note The delivered quantity (9 PC) varies from the ordered quantity (10 PC). |  |  |
| 6 | Enter Goods Recipient | In Detail data, navigate to Where tab, Make the following entries, and choose EnterStorage Location For example: 331A |  |  |
| 7 | Select Item OK | Select the item OK checkbox at the bottom of the screen |  |  |
| 8 | Save the Documents | Click Post button. | The goods receipt for the purchase order was posted to the sales order stock (look on the Where tab).You may record down the posted material document number at the bottom. |  |

|  |
| --- |
| Note As soon as the goods receipt is posted, you get a system message regarding the document number of the goods receipt. To view the material document in FLP, In the Materials Management Warehouse Processing group, open Material Documents Overview. |

Financial postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 13600000 Inventory TrandingGd | 21120000 GR/IR | none |

### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the delivery.

Prerequisite

The goods receipt was posted to the individual customer’s stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2. | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A) | The Create Outbound Deliveries - From Sales Orders (F0869A) screen displays. |  |
| 3. | Search Sales Order | Make the following entries and choose Go:Shipping point: 3310Planned Creation Date: <Delivery selection date>SD Document: Sales order number created previously |  |  |
| 4. | Create Delivery | Select your sales order items and choose Create Deliveries. | A delivery is triggered to create. |  |
| 5. | Check Details | Choose Display Log | The Analyze Delivery Log screen displays, delivery is created successfully with delivery number shown on tab Deliveries. |  |

|  |
| --- |
| Note Depending on the scope item-settings, the availability is checked at the delivery creation using the available inventory and replenishment lead time. Without sufficient stock, the created delivery has no confirmed quantities, and therefore does not start the warehouse management picking process. As soon as there is sufficient stock for delivery creation, the system creates a delivery with the starting of the picking process in warehouse management.To avoid open deliveries, ensure that there is sufficient inventory quantity at the time of delivery creation. Additionally, you have the following options to restrict the creation of deliveries with no confirmed quantities.You may increase the replenishment lead time which is used during the availability check (has to be larger than the selection period used for delivery creation).You may change the customization settings for the incompleteness procedure for delivery creation, so that only complete deliveries may be saved.You may change the customization settings for the used delivery-item-category. The Check quantity 0 field must be adapted to B = Situation rejected with an error message. |

|  |
| --- |
| Note With the Analyze Delivery Logs app, you can display an overview about the logs of all delivery creation in system. You can filter by choosing Created by and other additional settings. Detailed log information is listed via selecting the arrow on the right of each delivery log entry:If delivery is created successfully, delivery number is shown on tab Deliveries, else, you can display the exact message type, text and also the related sales document on tab Messages. |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N) | The Change Outbound Delivery (VL02N) screen displays |  |
| 3 | Issue Delivery Output | On the Change Outbound Delivery (VL02N) screen, enter the Delivery number nad click Continue. From the Delivery xxxxxxxx Change: Overview screen, choose Menu > Extras > Delivery Output > Output Control | The Delivery: Output screen displays. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with the Output Type Delivery_Pick_List and choose Display PDF Document. | A preview of the print document is displayed. |  |
| 5 | Print Delivery Pick List | From the preview of the document, choose Print. | The delivery pick list is printed. |  |

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

### Execute Picking

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

### Post Goods Issue

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

### Create Billing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The billing document is created with reference to a preceding document, for example, to create an invoice or a credit memo.

Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad using the role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings in the right bottom of the screen.The four settings, that are marked as ON in the settings.Enter Billing Data before billingSeparate Billing Documents for Each Billing Due List Item.Automatically Post Billing DocumentsDisplay Billing Document after creation. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) will displays. |  |
| 5 | Choose Individual Billing Document | Select a row of SD Document created previously and choose Create. | The Create Billing Documents (F0798) window displays. |  |
| 6 | Maintain Billing Date | Choose billing type Invoice (F2) and maintain billing date, for example current date, then choose OK. | The new billing document is created. |  |
| 7 | Display Billing Document after Creation | The billing document displays automatically. Make a note of the billing document number: __________. | The system generates an invoice for billing. |  |

Financial postings

| Material | Debited Accounts | Credited Accounts | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12100000 G/L | 41000000 Rev Domestic Prod | none |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Access the App | Open Manage Billing Documents (F0797) . | The screen Manage Billing Document displays. |  |
| 2. | Search the billing document created in previous step | Input the Billing document number recorded in previous step.Choose Enter. | The billing document created in previous step displays. |  |
| 3. | Display the billing document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4. | Check Output Condition | Choose the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5. | Display Print Preview | Choose Preview. | Preview for PDF document displays. |  |
| 6. | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel Billing Docs | Log displays - Billing Document Canceled. |  |
| 7. | Update new Attachment (Optional) | In the Edit mode, add, delete and update the attachments.Choose Save |  |  |
| 8. | Update new Text (optional) | In the Edit mode, you can add, delete and update these texts.Choose Save |  |  |

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
| 1 | Log on | Open the SAP Fiori launchpad with the Accounts Payable Accountantrole. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Supplier Invoice App | Open Create Supplier Invoice (F0859). | The Create Supplier Invoices screen is displayed. |  |
| 3 | Enter General Data | In case of purchase orders created with local currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: AEDInvoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:In case of purchase orders created with foreign currency in your system, make the following entries.Transaction: InvoiceCompany Code: 3310Gross Invoice Amount : <XXX>Currency: XXX (change the invoice currency, for example from EUR to USD)Invoice Date: <Today>Posting Date: <Today>Reference: <xxx>(reference invoice number from invoicing party)Invoice Party:Select See More at header area, make the following entries.Exchange Rate: <XXX> | The Exchange Rate should be changed from USD in EUR according to the customizing settings. The Exchange Rate is changeable |  |
| 4 | Enter Purchase Order References | In Purchase Order References section, add the references.Make the following entries (use a PO you created previously).References Document Category: Purchase Order/ Scheduling AgreementPurchase Order: <xxx> | All items of the referenced Purchase Order are added to the Invoice Items section. |  |
| 5 | Select Invoice Items | Select the Invoice Items you want to create invoice for. | You should see material items and delivery costs items, which refer to the entered purchase order document. Check if items for planned delivery costs have an item text. |  |
| 6 | Check the Invoice Items data | Check the Amount, the Quantity, the Tax Code (there may already be a tax code that was copied from the purchase order). | The Amount, the Quantity, the Tax Code are consistent. |  |
| 7 | Check Tax code | In the section Tax, check if there is tax code information and enter the tax amount if the tax code value is greater than zero. | In the Tax area, you should see the same tax codes as in the items.If there is no tax, specify the tax code <Input Tax Code> . |  |
| 8 | Block invoice on item level (optional) | Choose the invoice item arrow on the right side of the item to navigate to the item details.On the next screen, set flag for Manually Blocked. Click Check and on the lower part of the details screen, the Blocking Reasons section shows the text Manual. Click Back to Supplier Invoice. | The item is blocked with a blocking reason. |  |
| 9 | Check the balance(optional) | Calculate the tax by choosing Propose Tax. Check the balance (difference between the calculated amount and the gross Amount you entered in step 3). | The balance should be zero (or within the defined tolerance). |  |
| 11 | Simulate Supplier Invoice and Check Messages | Choose Simulate.You can check the simulation results in Simulation Overview and Simulation Details area. | The Supplier Invoice is simulated. |  |
| 12 | Post Invoice | Choose Post. | The invoice is posted. The system message is shown. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Accounts Receivable | Posting a Customer Invoice in Accounting, etc.Using the master data from this document, complete the following activities described in the test script:Accounts Receivable (Sections Posting a Customer Invoice in Accounting, Overdue Receivables, Display Customer Balances, Manage Customer Line Items) |
| Sales Order Fulfillment Monitoring and Operations (Optional) | Collection of periodical activities, such as day ending activities reporting.Using the master data from this document, complete the following activities described in the test script:Sales Order Fulfillment Monitoring and Operations(Sections Review Incomplete Sales Orders, Review Incomplete SD Documents (deliveries), Review Outbound Deliveries for Goods Issue and Review List Blocked (for accounting) Billing Documents |
| Stock Transfer with Delivery | Usually, Purchase Requisitions for STOs are created after MRP(additional step). In case an individual Stock Transfer Order(BME) shall be directly triggered with sales order, please use alternative schedule line category CU, it could lead to a direct link in SD document flow between standard order (SO) and stock transfer order(STO).Note Specific master data required: Indicator for "Dependent requirements" must be Blank or 1 = Individual requirement.Additional manual step for end user at procuring plant:Transfer posting via movement type 413 in order to transfer from unrestricted stock to special stock 'E' before transferring from procuring to shipping plant(movement type: 643 and 101). |

### Limitations

Preliminary billing documents cannot be used in the current process, please don’t create relevant document.

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

### Integration with Advanced ATP – Scope item 1JW

Scope item BDN is using item category CBAB as standard item category to initiate the BDN process.

In addition to the 3 standard ways to determine the item category CBAB - which are:

1. Manually enter item category
2. Default item category via item category group CBUK assigned in the material master to the material and configuration in SSCUI 102807
3. [Flexible item category determination](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a376cd9ea00d476b96f18dea1247e6a5/66327f62527a4a988c1976c23e8ba3c4.html?version=2402.502)
4. NEW: Based on the configuration of the Advanced ATP check, please see scope item Advanced Available-to-Promise Processing for details and prerequisites

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
> Flagged while digesting this document, not verified: PO approval threshold is stated inconsistently: Purpose says '>= 500 USD' with purchase group 003, step 3 says net value of '500 AED or more', step 4 says '500 USD or more', and the workflow configuration example uses 'greater than 10' in AED.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sold-to party: sample master data lists 33100003 (Domestic UAE Customer 3), but the Create Sales Order step enters Sold-to Party 33100005.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Purchasing group: the purchasing info record is created with purchasing group 002 (repeat with 001), whereas the PO approval workflow and rule require purchasing group 003.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Info record price: step 8 enters condition amount 300 AED, while the following notes state net prices of 35 AED and 25 AED for the same material.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Table app names differ from the procedures: Create Delivery lists VL01N but the procedure opens F0869A; sales order attachment lists F1873 but the procedure opens F3893; Approve and Release PO lists 'Approve Purchase Orders' but the procedure opens My Inbox (F2097).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/sales-order-processing-for-non-stock-material-2et-ae-test-script-818]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BDN_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 70,402 chars in the whole document
