---
id: 08-sales-order-management/test-script-customer-returns-with-direct-shipment-from-customer-to-sup
title: "Test Script: Customer Returns with Direct Shipment from Customer to Supplier (1Z3_AE) (1Z3_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud test script (1Z3_AE): customer return shipped directly to supplier, supplier credit memo, refund by credit memo or replacement."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-returns-and-refunds]
aliases: [1Z3_S4CLD2608_BPD_EN_AE]
keywords: [Customer Returns and Refunds, customer returns, direct shipment to supplier, returns order, supplier credit memo, refund determination, customer credit memo, replacement delivery, picking, goods issue]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Z3_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-791
topic: 08-sales-order-management/customer-returns-and-refunds
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Customer Returns with Direct Shipment from Customer to Supplier (1Z3_AE) (1Z3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Z3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Customer Returns and Refunds** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Customer Returns with Direct Shipment from Customer to Supplier (1Z3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848428)

[2 Prerequisites 4](#_Toc232848429)

[2.1 System Access 4](#_Toc232848430)

[2.2 Roles 4](#_Toc232848431)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232848432)

[2.4 Business Conditions 6](#_Toc232848433)

[2.5 Preliminary Steps 7](#_Toc232848434)

[2.5.1 Create Info Record 7](#_Toc232848435)

[2.5.2 Set Initial Stock for Material 9](#_Toc232848436)

[2.5.3 Create Condition Records (Optional) 10](#_Toc232848437)

[3 Overview Table 11](#_Toc232848438)

[4 Test Procedures 12](#_Toc232848439)

[4.1 Create Returns Order 12](#_Toc232848440)

[4.2 Create Supplier Credit Memo 14](#_Toc232848441)

[4.3 Determine Refund 16](#_Toc232848442)

[4.4 Display Returns Overview 18](#_Toc232848443)

[4.5 Refund Customer with Credit Memo 19](#_Toc232848444)

[4.5.1 Create Credit Memo 19](#_Toc232848445)

[4.6 Refund Customer with Replacement Product 21](#_Toc232848446)

[4.6.1 Create Free-of-Charge Delivery 21](#_Toc232848447)

[4.6.2 Execute Picking 22](#_Toc232848448)

[4.6.3 Post Goods Issue 23](#_Toc232848449)

[4.6.4 Create Pro-forma Invoice 25](#_Toc232848450)

[4.6.5 Create Customer Invoice 26](#_Toc232848451)

[5 Appendix 29](#_Toc232848452)

[5.1 Process Integration 29](#_Toc232848453)

[5.1.1 Succeeding Processes 29](#_Toc232848454)

## Purpose

Overview

The customer contacts the seller and informs the internal sales representative that they want to return products. The sales representative decides that the products must be returned directly to the supplier. This can be the case, for example, when products are initially shipped to the customer via third-party delivery by the supplier.

The sales representative creates a returns order to initiate the return of products to the supplier. Once the returns order is saved and released, a returns purchase order is generated automatically. After the supplier has received the returned products, the seller gets a credit memo from the supplier. The seller compensates the customer with a credit memo or replacement product.

The progress of the customer return processes is monitored by tracking the follow-up documents of returns orders.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |

### Master Data, Organizational Data, and Other Data

SAP Best Practices Standard Values based on new global template will be used once available. In the table you still see the master data used for the current baseline.

Essential master and organizational data was created in your S/4HANA system in the implementation phase, such as the data that reflects the organizational structure of your company and master data that suits its operational focus, for example, master data for materials, vendors, and customers.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

This master data usually consists of standardized SAP Best Practices default values, and enables you to go through the process steps of this scope item.

| Master / Org. Data | Value | Master / Org. Data Details | Comments |
| --- | --- | --- | --- |
| Material | TG10 | Trad.Good 10,PD,Third PartyTrading Good for regular Trading (MRP planning) with item category group CBORno Serial no.; no batch |  |
| Material | TG13 | Trad.Good 13,Reorder Point,Thrd PartyTrading Good for Regular Trading (reorder point planning) with item category group CBNAno Serial no.; no batch |  |
| Sold-to party | 33100003 | Domestic UAE Customer 3 | Sold-to party |
| Ship-to party | 33100003 | Domestic UAE Customer 3 | Ship-to party |
| Payer | 33100003 | Customer domestic 03 | Payer |
| Supplier | 33300006 | Domestic UAE Supplier 6 | Supplier |
| Plant | 3310 |  | Storage Location |
| Storage Location | 331A331R |  | Storage Location |
| Shipping Point | 3310331R |  | Shipping Point |
| Sales Organization | 3310 |  | Sales organization |
| Distribution Channel | 10 |  | Distribution channel |
| Division | 00 |  | Division |

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

The business process described in this Test Script is part of a bigger chain of integrated business processes or scope items. As a consequence, you must have completed the following processes and fulfilled the following business conditions before you are able to start going through this scope item:

| Scope Item | Business Condition |
| --- | --- |
| BD3 - Sales Processing using Third-Party with Shipping Notification orBDK - Sales Processing Using Third-Party Without Shipping Notification | Before running this test script, complete all activities in test scripts BD3 or BDK using master data, which is listed in the previous section Master Data, Organizational Data, and Other Data, and note down the created document numbers of sales order and billing document for further use. |

### Preliminary Steps

#### Create Info Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create info records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchasing Info Records (F1982). |  |  |
| 3 | Open New Purchasing Info Record | Choose Create Purchasing Info Records. | The Purchasing Info Record screen displays. |  |
| 4 | Enter Header Data | Go to Header area, make the following entries:Purchasing Info Record Category: StandardPurchasing Organization: 3310Supplier: 33300006Material: TG10Plant: 3310Purchasing Group: 001 | Header data is added. |  |
| 5 | Enter Delivery and Quantity Data | Go to Delivery and Quantity area, make the following entries:Delivery Time in Days: <Delivery Time>, for example, 1Under Delivery Tolerance in %: <Under Delivery Tolerance>, for example, 10Over Delivery Tolerance in %: <Over Delivery Tolerance>, for example, 10Tax Code: <Tax Code>, for example, <Input Tax Code>Tax Rate Valid From: For example, TodayOrder Unit: <Order Unit>, for example, PCStandard Order Quantity: <Standard Order Quantity>, for example, 1Select the following entries if required:Unlimited Delivery: <unselected>Goods-Receipt-Based Invoice Verification: <unselected>No Evaluated Receipt Settlement: < unselected>Order Acknowledgment Requirement: <unselected> | Delivery and Quantity Data is added. |  |
| 6 | Enter Condition Data | Go to the Condition area, choose Create. Enter the following data:Valid From: <Valid from Date>Amount: <Amount>, for example, 14Pricing Unit: <Pricing Unit>, for example, 1Valid To: <Valid to Date>Currency: <Currency>, for example, AED.Choose Apply. | Condition Data is added. |  |
| 7 | Save Your Data | Choose Save. | A purchasing info record is saved. |  |
| 8 | Repeat Entire Steps and Create An New Info Record | Repeat the entire steps and create an new info record for below master data.Supplier: 33300006Material: TG13 | Follow-up activity information is maintained. |  |

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

The Customer Returns with Direct Shipment from Customer to Supplier scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Order](#unique_11) [page ] 12 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Returns order is created, returns purchase order is generated in the background |
| [Create Supplier Credit Memo](#unique_12) [page ] 14 | Accounts Payable Accountant | Create Supplier Invoice - Advanced (MIRO) | The credit memo for purchase order from supplier is created. |
| [Determine Refund](#unique_13) [page ] 16 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Refund determination is checked or triggered |
| [Display Returns Overview](#unique_14) [page ] 18 | Returns and Refund Clerk | Manage Customer Returns - Version 2 (F4832) | Document flow is displayed |
| Refund Customer with Credit Memo |  |  |  |
| [Create Credit Memo](#unique_15) [page ] 19 | Billing Clerk | Create Billing Documents (F0798) | Credit memo is created |
| Refund Customer with Replacement Product |  |  |  |
| [Create Free-of-Charge Delivery](#unique_16) [page ] 21 | Shipping Specialist | Create Outbound Deliveries | Replacement delivery is created |
| [Execute Picking](#unique_17) [page ] 22 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done |
| [Post Goods Issue](#unique_18) [page ] 23 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Goods issue is posted for delivery |
| [Create Pro-forma Invoice](#unique_19) [page ] 25 | Billing Clerk | Create Billing Documents (F0798) | Pro-forma invoice is created |
| [Create Customer Invoice](#unique_20) [page ] 26 | Billing Clerk | Create Billing Documents (F0798) | Customer invoice is created |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, such as: apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

1. Log on to the SAP Fiori Launchpad using the respective user example, Internal Sales Representative.
2. Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.
3. The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your search criteria and choose the business object type, example: Customer Returns from dropdown menu in 1st field, enter customer return order number in 2nd field and choose Search, The sales order is listed.
4. Choose the sales order number link, the system navigates to fact sheet screen and return order related information is integrated and summarized in one Fiori page. You can get detailed data via choosing the corresponding links.

There are fact sheets available for the following objects (visibility depends on the assigned roles):

- Sales (return) order
- Quotation
- Billing document
- Credit memo
- Debit memo
- Customer 360 fact sheet

### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you create a returns order.

Prerequisite

The preceding sales business process is completed, sales order and billing document are created (refer to [Business Conditions](#unique_6) [page ] 6).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon to SAP Fiori Launchpad | Logon to the SAP Fiori launchpad using the role Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Navigate to New Customer Return Screen | Choose Create with Reference, then choose Create from Invoice. | The Create from Invoice pop-up screen displays. |  |
| 4 | Maintain Data | Enter the following data and then choose Select Items.Returns Order Type: Standard Return (CBAR)Invoice: Billing document number created previously |  |  |
| 5 | Maintain Return Quantity | Select the item(s) to be returned and enter the return quantity, then choose Continue. | New: Returns Order screen displays. |  |
| 6 | Maintain Data | Under tab General Information, enter the following data:Return Order Reason: for example, Standard Return(009)Under tab Items, choose the arrow button at the end of the item, enter the following data and choose Apply.In section Product:Return Reason: for example, Product damaged (003)In section Follow-up Activity:Follow-up Activity: Direct Shipment to Supplier (0007)Supplier: 33300006In section Refund:Refund Type: Credit MemoRefund Code: <select one from the downdrop list>, for example, 10%.Refund Control: Decide Later |  |  |
| 7 | Save and Release | On New: Returns Order screen, choose Save and Release. | Returns order is released, the subsequent returns purchase order is generated automatically.Note If returns order workflow is activated, next need to perform returns order approval process, details refer to the chapter Process Returns Order Approval in test script BKP. |  |
| 10 | Check Process Flow | Under the Process Flow tab, make a note of follow-up return purchase order number 45XXXXXXXX. |  |  |

Print Form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon to SAP Fiori Launchpad | Logon to the SAP Fiori launchpad using the role Returns & Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Enter search term(s) in filter bar and choose Go:For example, enter returns order number in field Returns Order. | The returns order is displayed in result list. |  |
| 4 | Navigate to Standard Returns Order Overview Screen | Choose the arrow at the end of item.On right-top area, choose Related Apps > Display Customer Return . | The Display Standard Return 6XXXXXXX: Overview screen displays. |  |
| 5 | Check Output Condition | Choose Header Output Preview. | The Display Standard Return 6XXXXXXX: Output screen displays. |  |
| 6 | Display Print Preview | Select the line already created for the print output and choose Display PDF Document. | The printing form is displayed. |  |

### Create Supplier Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter the credit memo received from the supplier for the returns purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Supplier Invoice - Advanced (MIRO).Make following entry and choose Enter.Company Code: 3310Note Company code can only be edited by choosing More > Edit > Switch Company Code . |  |  |
| 3 | Enter General Data | Transaction: < Credit Memo>Go to Basic Data tab:Invoice date: <Today>Posting Date: <Today>Reference: <Fill the reference information>Tax Code (Next to field Tax Amount): <Input Tax Code>Calculate Tax: <selected>Amount: <Value in PO Calculate Tax> | The Enter Incoming Invoice: Company Code XXXX displays. |  |
| 4 | Enter Purchase Order References | Go to PO Reference tab, make the following entries:Reference Document Category: <Purchase Order/Scheduling Agreement>Purchase Order: <Enter a PO you created previously>Choose Enter. |  |  |
| 5 | Check or Maintain the Purchase Order Items Data | Check or maintain the Amount, the Quantity, and the Tax Code. |  |  |
| 6 | Simulate Credit Memo and Check Messages | Choose Simulate (Ctrl+Shift+F7).If there are no differences (or if the value is within the defined tolerance), a new screen Simulation displays. You can check the simulation results. |  |  |
| 7 | Post Credit Memo | Choose Post. | The Invoice is posted. The system displays the message Document no. 51xxxxxxxx created. |  |

### Determine Refund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, refund decision is made: either refund the customer with a credit memo or compensate with a replacement product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon to SAP Fiori Launchpad | Logon to the SAP Fiori launchpad using the role Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen is displayed. |  |
| 3 | Search for Returns Order | Enter the following data in the filter bar and choose Go:Returns Order:Returns order number 6XXXXXXX | Returns order is found and displayed. |  |
| 4 | Navigate to Determine Refund Screen | Select the returns order entry and choose the Determine Refund. | Determine Refund screen displays. |  |
| 5 | Choose One of the Following Options | The system provides two options as refund types for your reference: credit memo or product replacement, please choose one to continue. |  |  |
| 5a | Option 1: Refund Customer with Credit Memo | On the Items to be Refunded tab, choose Change Refund in the Refund Details column for the return item, enter the following data:Refund type: Credit MemoRefund Code: A percentage number, for example: 10% RefundChoose the OK.Select the item and choose the Release Selected Items. | Refund setting is maintained, credit memo request document is created in background. |  |
| 5b | Option 2: Refund Customer with Product Replacement | On the Items to be Refunded tab, choose Change Refund in Refund Details column for the return item, enter the following data:Refund Type: Replacement ProductReplacement Product: <Material>Supplying Plant: 3310Replacement Quantity: <Quantity> / PCChoose the OK.Select the item(s) and choose the Release Selected Items. |  |  |
| 6 | Check Refund Results | On the Completed Items tab, refund result is displayed, follow-up document number is shown in Refund Detailscolumn, make a note of document number for further use. You can click the created document number to check detailed information.Click the document number and choose Change Credit Memo Request.Choose Save.A window with update success message appears, choose Exit.You are navigated back to Returns Order screen.Choose Release. | Refund result is displayed. |  |

|  |
| --- |
| Note If requested delivery date is reached and delivery document has not been created, warning information delivery issue is shown in process flow as reminder. Once delivery document is generated later, such alert disappears. |

### Display Returns Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can check the progress of return process. All dependent documents are available in process flow.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Logon to SAP Fiori Launchpad | Logon to the SAP Fiori Launchpad using the role Returns and Refund Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Manage Customer Returns - Version 2 (F4832) | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose the Show Filter Bar if it is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Go to Item Details | Choose the arrow at the end of the item. | The Display Returns Order screen displays. |  |
| 5 | Check Process Flow | In the Process Flow subarea, check the dependent documents shown in process flow.Make a note of follow-up document number(s) of credit memo request or replacement order for further use. | The dependent documents display. |  |

|  |
| --- |
| Note After you have completed this activity:Option A: If credit memo request is generated, go to chapter Refund Customer with Credit Memo.Option B: If replacement order is generated, go to chapter Refund Customer with Replacement Materialt. |

### Refund Customer with Credit Memo

#### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity credit memo is created.

Procedure

Table 3: Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk . |  |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Click Billing Settings.Maintain the settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create Billing Documents. | The Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Credit Memo (G2) and maintain billing date, such as the current date, and then press OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | In the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Final credit memo is generated. |  |

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the app | Open Manage Billing Documents. | The Manage Billing Documents screen displays. |  |
| 2 | Search the billing document | Enter the billing document number recorded previously in the Billing Document field and choose Enter. | The billing document, which is created previously displays. |  |
| 3 | Display the billing document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to the last assignment block - Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select a certain billing document and choose Cancel Billing Document. | A log displays the following message: Billing Document Canceled. |  |
| 7 | Update new Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update new Text (Optional) | In the Edit mode, you can add, delete, and update the texts. Save your changes by choosing Save in the footer bar. |  |  |

### Refund Customer with Replacement Product

#### Create Free-of-Charge Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, replacement delivery free of charge is created with reference to replacement order.

Prerequisite

Replacement order is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Shipping Specialist. |  |  |
| 2 | Access the App | Open Create Outbound Deliveries - From Sales Orders (F0869A). | The Create Outbound Deliveries screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Go:Shipping Point: 3310Planned Creation Date:: <Delivery selection date>Sales Document: <replacement order number created previously> |  |  |
| 4 | Create Delivery | Select your items and choose Create Deliveries. |  |  |
| 5 | Check Details | Choose Display Log. | The Analyze Delivery Log screen displays. Delivery is created successfully with delivery number shown on tab Deliveries. |  |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori Launchpad | Log onto the SAP Fiori Launchpad using the Shipping Specialist role. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: for example, 3310Only Picking without WM: Select the checkbox |  |  |
| 5 | Change Outbound Delivery | On the Day’s Workload for Picking screen. Select your outbound delivery and choose Change Outbound Delivery. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, enter the following data:Picked Qty: Equal to delivery quantity |  | Picking status is set to complete if picked quantity and delivery quantity is equal. Deviations in quantity can be solved by the function Copy Picked Quantity as Delivery Quantity. |
| 7 | Choose Enter | Choose the Enter. |  |  |
| 8 | Save | Choose Save. | The delivery has been picked. |  |

#### Post Goods Issue

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open the Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries - VL06O screen displays. |  |
| 3 | Choose Goods Issue | Choose the For Goods Issue. |  |  |
| 4 | Enter Shipping point | Make the following entries and choose Execute:Shipping Point: 3310 |  |  |
| 5 | Post Goods Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date and choose Continue in the dialog box. | The goods issue is posted. |  |

Financial Posting

| Material | Debited Accounts | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Goods (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

Printing form

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Outbound Delivery | The Display Outbound Delivery screen displays |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the delivery number and click Continue.From the Outbound Delivery Display: Overview screen, choose Menu > Extras > Delivery Output > Output Control | The Delivery: Output screen is displayed. |  |
| 4 | Print Preview | On the Delivery: Output screen, select the line with output type Delivery Note and choose Display Document. | A preview of the print document is displayed. |  |
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

In this activity, pro-forma invoice is created with reference to delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Click Billing Settings at the Header bar.Maintain the settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose the billing type Pro Forma Invoice for Delivery (F8) and Billing date, such as the current date, then choose OK. | The draft billing document displays. |  |
| 7 | Save Billing Document | In the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Proforma invoice is generated. |  |

Alternatively, it is supported to create pro-forma (type F5) with reference to replacement order.

#### Create Customer Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, F2 type of invoice is created, and costs are transferred to accounting accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open Create Billing Documents (F0798) | The Create Billing Documents screen displays. |  |
| 3 | Define billing setting | Click Billing Settings.Maintain the settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for billing list | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of delivery document created previously and choose Create Billing Documents. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Invoice (F2) and maintain Billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx is displayed. |  |
| 7 | Save Billing Document | In the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Customer invoice is generated. |  |

Financial Postings

| Material | Debited Accounts | Credited Accounts |
| --- | --- | --- |
| Trading Good (HAWA) | 44002000Sales Disc Domestic | 41000000Rev Domestic Prod |

If change is needed you can change the branch code in FI document after posting.

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open the App Manage Billing Documents. | The Manage Billing Document screen displays. |  |
| 2 | Search the billing document created in previous step | Input the pro-forma invoice number recorded in previous step. Choose Enter. | The billing document created in previous step displays. |  |
| 3 | Display the billing document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block – Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel billing Docs. | Log displayed: Billing Document Canceled. |  |
| 7 | Update new attachment (optional) | In the Edit mode, you can add, delete, and update the attachments. Choose Save to save your changes in the footer bar. |  |  |
| 8 | Update new Text (optional) | In the Edit mode, you can add, delete, and update these texts. Choose Save to save your changes in the footer bar. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

Table 4:

| Process | Business Condition |
| --- | --- |
| Sales Order Fulfillment Monitoring and Operations (BKK) (optional) | Using the master data from this document, complete the following activities described in the test script:Sales Order Fulfillment Monitoring and Operations (BKK) (Review Incomplete Sales Orders, Review Incomplete SD Documents (deliveries) and Review Outbound Deliveries for Goods Issue Sections) |

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
- related-to :: [[08-sales-order-management/customer-returns-for-non-stock-and-service-materials-3te-ae-test-scrip]]
- related-to :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]
- related-to :: [[08-sales-order-management/test-script-customer-returns-involving-supplier-by-message-exchange-3q]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1Z3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 45,801 chars in the whole document
