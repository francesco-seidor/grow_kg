---
id: 08-sales-order-management/test-script-intercompany-process-for-customer-returns-2f4-ae-820
title: "Test Script: Intercompany Process for Customer Returns (2F4_AE) (2F4_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 2F4: intercompany customer returns, refund by credit memo or replacement, with roles, apps and postings."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/intercompany-customer-returns]
aliases: [2F4_S4CLD2608_BPD_EN_AE]
keywords: [Intercompany Customer Returns, return order creation, refund determination, customer credit memo, internal credit memo, material replacement, intercompany invoice, material inspection, picking and goods issue, pro-forma invoice]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F4_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-820
topic: 08-sales-order-management/intercompany-customer-returns
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Intercompany Process for Customer Returns (2F4_AE) (2F4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Intercompany Customer Returns** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Process for Customer Returns (2F4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849419)

[2 Prerequisites 4](#_Toc232849420)

[2.1 System Access 4](#_Toc232849421)

[2.2 Roles 4](#_Toc232849422)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232849423)

[2.4 Additional Manual Configuration 7](#_Toc232849424)

[2.5 Business Conditions 7](#_Toc232849425)

[2.6 Preliminary Steps 8](#_Toc232849426)

[2.6.1 Create Initial Stock in the Domestic Shipping Plant 8](#_Toc232849427)

[2.6.2 Create Initial Stock in the International Shipping Plant 9](#_Toc232849428)

[2.6.3 Create Condition Records (Optional) 10](#_Toc232849429)

[3 Overview Table 11](#_Toc232849430)

[4 Test Procedures 13](#_Toc232849431)

[4.1 Generate Return Order 13](#_Toc232849432)

[4.2 Perform Picking 16](#_Toc232849433)

[4.3 Post Goods Receipt 17](#_Toc232849434)

[4.4 Perform Material Inspection 17](#_Toc232849435)

[4.5 Determine Refund 19](#_Toc232849436)

[4.6 Display Return Overview 20](#_Toc232849437)

[4.7 Refund Customer with Credit Memo 21](#_Toc232849438)

[4.7.1 Create Customer Credit Memo 21](#_Toc232849439)

[4.7.2 Create Internal Credit Memo 23](#_Toc232849440)

[4.7.3 Display AP Accounting Document 24](#_Toc232849441)

[4.8 Refund Customer with Material Replacement 25](#_Toc232849442)

[4.8.1 Change Replacement Order 25](#_Toc232849443)

[4.8.2 Create Free-of-Charge Delivery 26](#_Toc232849444)

[4.8.3 Perform Picking 27](#_Toc232849445)

[4.8.4 Post Goods Issue 28](#_Toc232849446)

[4.8.5 Create Customer Invoice 30](#_Toc232849447)

[4.8.6 Create Intercompany Invoice 31](#_Toc232849448)

[4.8.7 Display AP Accounting Document 33](#_Toc232849449)

[4.8.8 Create Internal Credit Memo 34](#_Toc232849450)

[4.8.9 Display AP Accounting Document 35](#_Toc232849451)

[4.8.10 Create Pro-forma Invoice (Optional) 36](#_Toc232849452)

## Purpose

Overview

This scope item helps the company to manage customer returns and refunds using affiliated plants. It integrates customer processes with intercompany processes. Material returned to the affiliated plant is internally credited. Accounts payable documents can be created automatically.

If the customer gets a free-of-charge delivery (from the affiliated plant) as a refund, an intercompany invoice can be created. Accounts payable documents can be created automatically.

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG12 | Trading Good for Reg. Trading (MRP planning)No Serial no.; no batch. |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Distribution Channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |
| Variant 1: Domestic intercompanyThe selling sales organization is located in United Arab Emirates (represented by company code 3310), the supplying company is also located in United Arab Emirates (represented by company code 3320) |  |  |  |
| Sold-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Ship-to Party | 33100001 | Domestic UAE Customer 1 |  |
| Payer | 33100001 | Domestic UAE Customer 1 |  |
| Plant | 3330 | Plant 3 AE | Flex.Org App or Set Up Organizational (CBC) extension |
| Storage Location | 333A333R | Std. storage 1Storage Location 333R | Flex.Org App or Set Up Organizational (CBC) extensionShop floor w/o lean WM |
| Shipping Point | 3330333R | Shipping Point 3330Shipping Point 333R | Flex.Org App or Set Up Organizational (CBC) extension |
| Variant 2: International intercompanyThe selling sales organization is located in United Arab Emirates, the supplying company is located in the foreign country/region for example: US |  |  |  |
| Sold-to Party | 33100002 | Domestic UAE Customer 2 |  |
| Ship-to Party | 33100002 | Domestic UAE Customer 2 |  |
| Payer | 33100002 | Domestic UAE Customer 2 |  |
| Plant | 3310 | Plant in supplying company |  |
| Storage Location | 331A331R |  |  |
| Shipping Point | 3310331R |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/10882e7ee6f555a234fe47ba83482495)

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Open new posting period in company codes 3310 and 3320 respectively. |
| 1HO - Intercompany Sales Order Processing – Domestic | For running variant 1 (domestic IC returns) |
| 1MX - Intercompany Sales Order Processing – International | For running variant 2 (international IC returns) |
| BKP - Customer Returns | Advanced Returns |

### Preliminary Steps

#### Create Initial Stock in the Domestic Shipping Plant

Purpose

This process step shows you how to create initial stock for the domestic shipping plants.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and choose Enter:Material: TG12Plant: Plant 1 <Supply Plant in affiliate company>, for example: 3330 | The Stock overview for the material displays. |  |
| 4 | Select Stock | Select an initial stock to add, for example:Storage Location: <Storage Location in the affiliate supply plant>, for example: 333AIn the columm Unrestricted-Use Stock, choose the icon ‘Unrestricted-Use Stock’ | A dialog displays. The Storage Location, Stock Type, and Current Quantity are displayed per the previous step entries. |  |
| 5 | Add Initial Entry | Make the following entry and choose Post:Document Date: <today>Posting Date: <today>Stock Change: Initial EntryQuantity: <enter a number>, for example: 100 | The system displays Material document XXX created. The stock has been added. |  |

Result

The stock quantity is posted and increased.

#### Create Initial Stock in the International Shipping Plant

Purpose

Create Initial Stock for the international shipping plants.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Stock. | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and choose Enter:Material: TG12Plant: Plant 1 <Supply Plant in the affiliate/foreign company>, for example: 3310 | The Stock overview for the material displays. |  |
| 4 | Select Stock | Select an initial stock to add, for example:Storage Location: <Supply Plant in the affiliate/foreign company>, for example: 331AIn the columm Unrestricted-Use Stock, choose the icon ‘Unrestricted-Use Stock’ | A dialog displays. The Storage Location, Stock Type, and Current Quantity are displayed per the previous step entries. |  |
| 5 | Add Initial Entry | Make the following entry and choose Post:Document Date: <today>Posting Date: <today>Stock Change: Initial EntryQuantity: <enter a number>, for example: 100 | The system displays Material document XXX created. The stock has been added. |  |

Result

The stock quantity is posted and increased.

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

| Process Step | Business Role | Transaction/ App | Expected Results |
| --- | --- | --- | --- |
| [Generate Return Order](#unique_12) [page ] 13 | Returns and Refund Clerk | Manage Customer Returns (F1708) | Return order is created, return delivery is generated in the background. |
| [Perform Picking](#unique_13) [page ] 16 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Picking is done for the return delivery. |
| [Post Goods Receipt](#unique_14) [page ] 17 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | The goods receipt is posted for return delivery. |
| [Perform Material Inspection](#unique_15) [page ] 17 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) | Inspection results are recorded. |
| [Determine Refund](#unique_16) [page ] 19 | Returns and Refund Clerk | Manage Customer Returns (F1708) | Refund determination is checked or triggered. |
| [Display Return Overview](#unique_17) [page ] 20 | Returns and Refund Clerk | Manage Customer Returns (F1708) | Document flow is displayed. |
| Refund Customer with Credit Memo |  |  |  |
| [Create Customer Credit Memo](#unique_18) [page ] 21 | Billing Clerk | Create Billing Documents (F0798) | Credit memo is created. |
| [Create Internal Credit Memo](#unique_19) [page ] 23 | Billing Clerk | Create Billing Documents (F0798) | Internal Credit memo is created. |
| [Display AP Accounting Document](#unique_20) [page ] 24 | General Ledger Accountant | Manage Journal Entries (F0717A) | AP journal entry displays |
| Refund Customer with Replacement Material |  |  |  |
| [Change Replacement Order](#unique_21) [page ] 25 | Returns and Refund Clerk | Manage Sales Orders Without Charge (F2305) | Item category is changed to CBXN. |
| [Create Free-of-Charge Delivery](#unique_22) [page ] 26 | Shipping Specialist | Create Outbound Delivery - With Order Reference (VL01N) | Replacement delivery is created. |
| [Perform Picking](#unique_23) [page ] 27 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Picking is done. |
| [Post Goods Issue](#unique_24) [page ] 28 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | Goods issue is posted for delivery. |
| [Create Customer Invoice](#unique_25) [page ] 30 | Billing Clerk | Create Billing Documents (F0798) | Customer invoice is created. |
| [Create Intercompany Invoice](#unique_26) [page ] 31 | Billing Clerk | Create Billing Documents (F0798) | Billing with IV types is created |
| [Display AP Accounting Document](#unique_27) [page ] 33 | General Ledger Accountant | Manage Journal Entries (F0717A) | AP journal entry displays |
| [Create Internal Credit Memo](#unique_28) [page ] 34 | Billing Clerk | Create Billing Documents (F0798) | Internal Credit memo is created. |
| [Display AP Accounting Document](#unique_29) [page ] 35 | General Ledger Accountant | Manage Journal Entries (F0717A) | AP journal entry displays |
| [Create Pro-forma Invoice (Optional)](#unique_30) [page ] 36 | Billing Clerk | Create Billing Documents (F0798) | Pro-forma invoice is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The test should take around Enter a duration, example, 60 minutes. The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, such as: Apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

- Log on to the SAP Fiori launchpad as an Internal Sales Representative.
- Access the Enterprise Search Bar and choose Magnifying glass in the upper right corner.
- The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your search criteria and choose the business object type, for example: Customer Returns from dropdown menu in first field, enter customer return order number in second field and choose Search, The sales order is listed.
- Choose the sales order number link, the system navigates to fact sheet screen and return order-related information is integrated and summarized in one Fiori page. You can get detailed data via choosing the corresponding links.
- There are fact sheets available for the following objects (Visible depending on the assigned role):
    - Sales (return) order
    - Quotation
    - Billing document
    - Credit Memo
    - Debit Memo
    - Customer 360 Fact sheet

### Generate Return Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a return order.

Prerequisite

You must have billing document, pro-forma invoice or sales order as reference (refer to[Business Conditions](#unique_7) [page ] 7).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708). |  |  |
| 3 | Navigate to New Customer Return Screen | Choose Create. | The Create Customer Return with Reference screen displays. |  |
| 4 | Search for Billing (sales) Document to be Referenced | Use Adapt Filters to add Reference Document field if it is hidden.Enter the following selection criteria in filter bar and choose Go:Reference Document: <sales order number or customer billing document number, or pro-forma invoice number which are created previously> | Billing (sales) documents are displayed in the Reference Documents table. |  |
| 5 | Choose Create | Choose Create in the billing (sales) document entry. | Dialog box Create Return from Invoice appears. |  |
| 6 | Enter Return Reason and Quantity | Enter the following data and choose Create:Return Reason: for example, Customer ordered too muchItems area:Quantity:V,quantity to be returned | Return order is created.System navigates to Edit Customer Return screen. |  |
| 7 | Change Refund | Select item and then go to column Refund Details. |  |  |
|  |  | The user can influence the point in time when the refunding document must be created: either immediately when the return order is saved and released or at a later point of time. Combination of the refund setting determines follow-up document creation. System provides four options for your reference, choose one among them to continue: |  |  |
|  | Option 1: Execute refund with credit memo immediately | In the Refund Details column of Item area, enter the following data or action:Refund type (upper field): Credit MemoRefund Code (right field): <select one from down-drop list>, for example: 10%.Refund Control: (lower field): <Create Credit Memo Request>Choose Save and Release. | Return order is created,Return delivery and credit memo request are generated automatically. |  |
|  | Option 2: Execute refund with replacement material immediately | In Item area, Refund Details column, enter the following data or action:Refund type (upper field): Replacement ProductNote Refund code is only relevant to Credit Memo, it will be invisible if you have chosen Replacement Material in field Refund type.Refund Control:(lower field): <Create Replacement Order>Choose Save and Release. | Return order is created, Return delivery and Replacement Order are generated automatically. |  |
|  | Option 3: Refund on hold, choose credit memo as temporary refund type | In the Refund Details column of Item area, enter the following data or action:Refund type (upper field): Credit MemoRefund Code (right field): <Select one from down-drop list>, for example: 10%.Refund Control: (lower field): <Decide Later>Choose Save and Release. | Return order is created, Return delivery is generated automatically. |  |
|  | Option 4: Refund on hold, choose replacement material as temporary refund type | In Refund area, enter the following data or action:Refund type (upper field): Replacement MaterialRefund Control: (lower field): <Decide Later>Choose Save and Release. | Return order is created, Return delivery is generated automatically. |  |
| 8 | Check Process Flow | On the Display Customer Return screen, Process Flow subarea: Check dependent documents in process flow. Make a note of the follow-up document numbers for further use.. | The dependent documents are displayed. |  |

If freight was maintained in previous delivery document header and material is partly returned regarding billing document, please check (or change if needed) freight amount for condition type YBHD in the header(s) of return order (and credit memo request document if it is generated automatically) using role Internal Sales Representative (SAP_BR_INTERNAL_SALES_REP) and tile Change Sales Order.

If requested delivery date is reached and delivery document has not been created, warning information delivery issue is shown in process flow as reminder. Once delivery document is generated later, such alert disappears.

### Perform Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform picking for return delivery created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose the Execute:Shipping Point: for example, 333R(Domestic)/ 331R (International). |  |  |
| 5 | Change Outbound Delivery | On the Day’s Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter picked quantity | On the Picking tab, input quantity equal to delivery quantity in field Picked Qty. |  |  |
| 7 | Choose Enter | Choose Enter. |  |  |
| 8 | Save | Choose Save. | The delivery has been picked. |  |

### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods receipt for return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |
| 3 | Choose Good Issue | Choose For Goods Issue. |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: For example, 333R (Domestic)/ 331R (International). |  |
| 5 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue, choose today’s date from the dialog box. |  |

### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The material inspection takes place after the returned goods have been received in the warehouse. The further handling of the returned goods is decided. This process step shows you how to perform material inspection.

Prerequisite

The returned goods are received. During goods receipt for returns an inspection document is created automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | Worklist Selection of Deliveries screen displays. |  |
| 3 | Maintain selection criteria | Enter the following entries and choose Run:Delivery items waiting for inspection: <select>Delivery: <Enter return delivery number> | Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Choose Item Tab | Choose the Item tab. |  |  |
| 5 | Maintain Inspection Result | In the Inspection Result subarea, enter the following data and choose Enter:Inspection Code: <Enter inspection code>Inspected quantity: <Enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Maintain Follow-up Activity | In Logistical Follow-Up subarea, enter the following data and choose Enter:Follow-Up Activity: <Enter follow-up activity>Note Choose appropriate follow-up activity according to inspection code. For example, choose follow-up activity Transfer to Free Available Stock responding to inspection code 0001. |  |  |
| 7 | Check Inspection Status | On the Header tab, in Basic Data subarea, Inspection status shows Inspected, which means all received material is inspected completely. | All received material is inspected completely. |  |
| 8 | Save and Confirm | Choose the Save and Confirm. | Inspection result is recorded, goods movement is posted accordingly. |  |

### Determine Refund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, refund decision is made or checked: either refund the customer with a credit memo or compensate with a replacement material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708). | The Manage Customer Returns screen displays. |  |
| 3 | Search for Return Order | Choose the Show Filter Bar if it is hidden, enter the following data and choose Go:Customer Return: <Return sales order number 6XXXXXXX> | Return order is found and displayed. |  |
| 4 | Navigate to Determine Refund Screen | Select the return order entry and choose the Determine Refund. | Determine Refund screen displays. |  |
| 5 | Check Refund Progress | In the upper area, check percentage number in field Refund Progress then take next action accordingly:100%: Refund determination is not completed, go to Section A, then Section B.100%: Refund determination is completed, skip Section A and go to Section B. |  |  |
| Section A: Refund is determined with reference to material inspection results | Option 1: Credit Memo | On the Items to be Refunded tab, choose Change Refund in the Refund Details column for the return item. Enter the following data:Refund type: Credit MemoExtent of Refund: <A percentage number>, for example, 10% RefundChoose the OKSelect the item and choose Release Selected Items. | Refund setting is maintained, credit memo request document is created in background. |  |
| Section A: Refund is determined with reference to material inspection results | Option 2: Material Replacement | On the Items to be Refunded tab, choose Change Refund in Refund Details column for the return item:Enter the following data:Refund type: Replacement MaterialChoose the OK.Select the item and choose the Release Selected Items. | Refund setting is maintained, Replacement order document is created in background. |  |
| Section B: Check refund determination result | Check Refund Results | On the Completed Items tab, refund result is displayed, follow-up document number is shown in Refund Details column, make a note of document number for further use. You can click the created document number to check detailed information. | Refund result is displayed. |  |

### Display Return Overview

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
| 2 | Access the App | Open Manage Customer Returns (F1708). | The Manage Customer Returns screen displays. |  |
| 3 | Search for return order | Choose the Show Filter Bar if it is hidden, enter the following data and choose the Go:Customer Return: <Return sales order number 6XXXXXXX> | Return order is found and displayed. |  |
| 4 | Go to Item Details | Choose the arrow at end of the item. | The Display Customer Return screen displays. |  |
| 5 | Check Process Flow | In the Process Flow subarea, check dependent documents shown in process flow.Make a note of follow-up document number(s) of credit memo request or replacement order for further use. | The dependent documents are displayed. |  |

After you have completed this activity:

Option A: If credit memo request is generated, go to chapter Refund Customer with Credit Memo

Option B: If replacement order is generated, go to chapter Refund Customer with Material Replacement

### Refund Customer with Credit Memo

#### Create Customer Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to credit memo is created.

Prerequisites

Ensure that Customer Credit Memo should be created before Internal Credit Memo.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using role Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose the Billing Setting in the bottom bar. Make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create. | Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Credit Memo (G2) and maintain billing date, for example, current date, then press the OK button. | The draft billing document with ID TMPxxxxxxx is displayed. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save, The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | Final credit memo is generated. |  |

Financial Posting for Domestic

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41000000 Revenue Domestic – Product22000000 Output Tax (MWS) | 12100000 Domestic AE Customer 144002000 Sales Discounts – Domestic | none |

Financial Posting for International

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41000000 Revenue Domestic – Product22000000 Output Tax (MWS) | 12100000 Domestic AE Customer 144002000 Sales Discounts – Domestic | none |

#### Create Internal Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the internal credit memo is created in delivery company code, and how the AP Journal Entry is generated in ordering company via IDOC in background.

Prerequisites

Customer Credit Memo must be created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose the Billing Setting in the bottom bar. Make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose SD Document | Select the row of return delivery document created previously and choose Create. | Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Internal Credit memo (IG) and maintain billing date, for example, current date, then choose OK. | The draft billing document with ID TMPxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Billing Document screen, choose Save, the draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________.Note To check the details of the iDoc generated by the intercompany billing document, you can check the section Message Monitor of the customer facing document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). | Internal credit memo is generated. |  |

Financial Posting for Domestic

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41001500 Revenue Affiliate - Product22000000 Output Tax (MWS) | 12300000 company code 3310 as a business partner | none |

Financial Posting for International

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41001500 Revenue Affiliate - Product | 12300000 company code 3310 as a business partner | none |

#### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display account payable accounting documents generated by internal credit memo IDoc.

Procedure

| Test Step | Test Step Name | Instruction | Expected Results | Pass/ Fail/ Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing Internal Credit Memo | Make the following entry:Original Reference Document: <00+ internal credit memo number generated in previous step>.Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

### Refund Customer with Material Replacement

#### Change Replacement Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to change item category to CBXN to meet the requirement of invoice creation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk . |  |  |
| 2 | Access the App | Open the Manage Sales Orders Without Charge (F2305). | The Manage Sales Orders Without Charge screen displays. |  |
| 3 | Maintain Selection Criteria | Make the following data and choose Go:Sales Order without Charge: <Replacement order number> | Replacement order is listed in search result. |  |
| 4 | Navigate to Change Sales Order Screen | Select replacement order number and then choose the Tab Change in the next dialog box. | The Change Deliv.Free of Charge XX : Overview displays. |  |
| 5 | Change Item Category | In All items table, change the item category (in field ItCa) to CBXNChoose Enter to confirm pop-up information. | Item category is changed. |  |
| 6 | Save | Choose Save. | Replacement order is saved. |  |

#### Create Free-of-Charge Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create replacement delivery free of charge with reference to replacement order.

Prerequisite

Replacement order is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist . | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Delivery - With Order Reference (VL01N). | The Create Outbound Delivery with Order Reference screen displays. |  |
| 3 | Search Sales Order | Make the following entries and choose Continue:Shipping Point: for example, 3330 (Domestic)/ 3310 (International).Planned Creation Date: <Delivery selection date>Order: <Replacement order number created previously> |  |  |
| 4 | Save Delivery | Choose Save | Delivery is created with a number ______________ |  |

#### Perform Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to perform picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries, and choose Execute:Shipping Point: <Enter the shipping point>, for example,3330 (Domestic)/ 3310 (International).Only Picking without WM: <Select the checkbox>Picking Date: <Picking selection date> |  |  |
| 5 | Change Outbound Delivery | On the Day’s Workload for Picking screen, select your delivery note and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, enter the following data:Picked Qty: <Equal to delivery quantity> |  |  |
| 7 | Choose Enter | Choose Enter. |  |  |
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

This process step shows you how to post the goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). | The Manage Outbound Deliveries screen displays. |  |
| 3 | Choose Good Issue | Choose the For Goods Issue. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping point: For example, 3330 (Domestic)/ 3310 (International). |  |  |
| 5 | Post Good Issue | Mark the relevant delivery and choose Post Goods Issue. Select today’s date and choose Continue in the dialog box. | The goods issue is posted. |  |

Financial Posting

| Material | Debited Accounts | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 51600000Consptn Trde Gds | 13600000Inventory TradingGd | none |

Printing Form

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. |  |  |
| 2 | Access the App | Open Display Outbound Delivery (VL03N). | The Display Outbound Delivery screen displays. |  |
| 3 | Issue Delivery Output | On the Display Outbound Delivery screen, enter the Delivery number. From the menu, choose More > Outbound Delivery > Issue Delivery Output |  |  |
| 4 | Print | Print preview: Select the line with the message type LD00 and choose Print Preview.Print Delivery Order: select the line with the message type LD00 and choose Print in the dialog box, choose the Print. | The preview document displays.The document prints. |  |

#### Create Customer Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create ‘F2’ type of invoice, costs are transferred to accounting accordingly.

Prerequisites

Item category CBXN is manually maintained in replacement order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose the Billing Setting in the bottom bar. Make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of Free-of-Charge delivery document created previously and choose Create. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Invoice (F2) and maintain Billing date, for example current date, then choose OK. | The draft billing document with ID TMPxxxxxxx is displayed. |  |
| 7 | Save Billing Document | In the Billing Document screen, click button Save. The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | Customer invoice is generated. |  |

Financial Posting for Domestic

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 44002000 Sales Discounts - Domestic | 41000000 Revenue Domestic - Product | none |

Financial Posting for International

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 44002000 Sales Discounts - Domestic | 41000000 Revenue Domestic - Product | none |

#### Create Intercompany Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create intercompany invoice in delivery company code, AP Journal Entry is generated in ordering company via IDOC in background.

Prerequisites

Customer invoice created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose the Billing Setting in the bottom bar. Make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose SD Document | Select the row of Free-of-Charge delivery document created previously and choose Create. | Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Intercompany Billing(IV) and maintain billing date, for example, current date, then press the OK button. | The draft billing document with ID TMPxxxxxxx is displayed. |  |
| 7 | Save Billing Document | In the Billing Document screen, choose Save, The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________.Note To check the details of the iDoc generated by the intercompany billing document, you can refer to the section Message Monitor of the customer facing document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). | Intercompany invoice is generated. |  |

Financial Posting for Domestic

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12300000 company code 3310 as a business partner | 41001500 Rev Affiliate- Prod22000000 Output tax (MWS) | none |

Financial Posting for International

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 12300000 company code 3310 as a business partner | 41001500 Rev Affiliate- Prod | none |

#### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display account payable accounting documents generated by IV invoice IDoc.

Procedure

| Test Step | Test Step Name | Instruction | Expected Results | Pass/ Fail/ Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.If app Manage Journal Entries (F0717A) is not there on the Home Page, search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing IV Invoice | Make the following entry:Original Reference Document: <00+ Intercompany invoice number generated in previous step>Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Create Internal Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create internal credit memo in delivery company code, AP Journal Entry is generated in ordering company via IDOC in background.

Prerequisites

Customer invoice created previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose the Billing Setting in the bottom bar. Make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) displays in the result. |  |
| 5 | Choose SD Document | Select the row of return delivery document created previously and choose Create. | Create Billing Documents screen displays. |  |
| 6 | Maintain Billing Type and Billing Date | Choose billing type Internal Credit memo (IG) and maintain billing date, for example, current date, then press the OK button. | The draft billing document with ID TMPxxxxxxx is displayed. |  |
| 7 | Save Billing Document | In the Billing Document screen, choose Save, The draft version billing document with ID TMPxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________.Note To check the details of the iDoc generated by the intercompany billing document, you can refer to the section Message Monitor of the customer facing document [Intercompany Sales Order Processing Setup (1HO 1MX 1WO) (SAP Customer)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_489%20Intercompany%20Sales%20Order%20Processing%20%20Setup%20(1HO%201MX%201WO).docx). | Internal credit memo is generated. |  |

Financial Posting for Domestic

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41001500 Revenue Affiliate - Product22000000 Output Tax (MWS) | 12300000 company code 3310 as a business partner | none |

Financial Posting for International

| Material | Debited Account | Credited Account | Cost Element / CO Object |
| --- | --- | --- | --- |
| Trading Good (HAWA) | 41001500 Revenue Affiliate - Product | 12300000 company code 3310 as a business partner | none |

#### Display AP Accounting Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display account payable accounting documents generated by internal credit memo IDoc.

Procedure

| Test Step | Test Step Name | Instruction | Expected Results | Pass/ Fail/ Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries screen displays.If app Manage Journal Entries (F0717A) is not there on the Home Page, please search and find it using the magnifier icon. |  |
| 3 | Add the Original Reference Document Field as Filter | Choose Adapt Filters, select Original Reference Document option, and choose OK. | The Original Reference Document field is added as a filter. |  |
| 4 | Filter AP Accounting Document by Referencing Internal Credit Memo | Make the following entry:Original Reference Document: <00+ internal credit memo number generated in previous step>.Choose Go. | AP accounting document number displays. |  |
| 5 | Display AP Accounting Document | Choose AP accounting number in the Journal Entry column.Choose Display Journal Entries - New Version. | AP accounting document displays. |  |

#### Create Pro-forma Invoice (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create pro-forma invoice with reference to delivery.

Prerequisites

Item category CBXN is manually maintained in replacement order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open the Create Billing Documents (F0798). | The Create Billing Documents screen displays. |  |
| 3 | Define Billing Setting | Choose the Billing Setting in the bottom bar. Make the following settings:Set billing date and type before billing: ONCreate separate billing document for each item of billing due list: OFFAutomatically post billing documents: ONDisplay billing documents after creation: ONChoose delivery items to be billed and select quantities: OFF |  |  |
| 4 | Search for Billing List | In the search condition, use criteria if necessary. | Sales document(s) displays in the result. |  |
| 5 | Choose Individual Billing Document | Select the row of Free-of-Charge delivery document created previously and choose Create. |  |  |
| 6 | Maintain Billing Type and Billing Date | Choose the billing type Invoice (F8) and Billing date, for example current date, then choose OK. | The draft billing document with ID Sxxxxxxxx is displayed. |  |
| 7 | Save Billing Document | In the Billing Document screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx, make a note of the billing document number: __________. | Pro-forma invoice is generated. |  |

Alternatively, it is supported to create pro-forma (type F5) with reference to replacement order.

Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open the App Manage Billing Documents. | The Manage Billing Document screen displays. |  |
| 2 | Search the billing document created in previous step | Input the pro-forma invoice number recorded in previous step. Choose Enter. | The billing document created in previous step displays. |  |
| 3 | Display the billing document | Select the billing document item and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, choose the last assignment block – Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | Select certain Billing document and choose Cancel billing Docs. | Log displayed: Billing Document Canceled. |  |
| 6 | Update new Attachment (Optional) | In the Edit mode, add, delete, and update the attachments. Choose Save to save your changes in the footer bar. |  |  |
| 7 | Update new Text (optional) | In the Edit mode, you can add, delete, and update these texts. Choose Save to save your changes in the footer bar. |  |  |

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
- see-also :: [[08-sales-order-management/customer-returns-for-material-with-variant-configuration-7kw-ae-test-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 63,926 chars in the whole document
