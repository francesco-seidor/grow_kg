---
id: 08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s
title: "Customer Returns Management – Consumer Products (61V_AE) – Test Script, SAP S/4HANA Cloud Public Edition (61V_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 61V_AE (Customer Returns, Consumer Products): roles, master data and test steps from returns order to refund and credit memo."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/customer-returns-and-refunds, topic/end-to-end-produce-and-sell]
aliases: [61V_S4CLD2608_BPD_EN_AE]
keywords: [Customer Returns and Refunds, customer returns, returns order creation, refund determination, material inspection, credit memo, delivery refusal, background job scheduling, business roles, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/61V_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1140
topic: 08-sales-order-management/customer-returns-and-refunds
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Customer Returns Management – Consumer Products (61V_AE) – Test Script, SAP S/4HANA Cloud Public Edition (61V_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/61V_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Customer Returns and Refunds** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Customer Returns Management – Consumer Products (61V_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857939)

[2 Prerequisites 4](#_Toc232857940)

[2.1 **System Access** 4](#_Toc232857941)

[2.2 **Roles** 4](#_Toc232857942)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232857943)

[2.4 Business Conditions 7](#_Toc232857944)

[2.5 SSCUIs 8](#_Toc232857945)

[2.5.1 Additional Return Reason “Delivery Refusal” 8](#_Toc232857946)

[3 Overview Table 10](#_Toc232857947)

[4 Test Procedures 11](#_Toc232857948)

[4.1 Goods are Returned to Seller 11](#_Toc232857949)

[4.1.1 Create Returns Order 11](#_Toc232857950)

[4.1.2 Execute Picking 15](#_Toc232857951)

[4.1.3 Post Goods Receipt 16](#_Toc232857952)

[4.1.4 Perform Material Inspection 17](#_Toc232857953)

[4.1.5 Determine Refund 18](#_Toc232857954)

[4.1.6 Display Returns Overview 20](#_Toc232857955)

[4.1.7 Credit Memo 21](#_Toc232857956)

[4.1.7.1 Create Credit Memo 21](#_Toc232857957)

[4.2 Scheduling Job (Alternative) 23](#_Toc232857958)

[4.2.1 Job Scheduling for Goods Issue Deliveries (Alternative) 23](#_Toc232857959)

[4.2.2 Job Scheduling for Billing Creation (Alternative) 24](#_Toc232857960)

[4.2.3 Job Scheduling for Billing Release (Alternative) 25](#_Toc232857961)

[4.2.4 Job Scheduling for Billing Output (Alternative) 26](#_Toc232857962)

[5 Appendix 28](#_Toc232857963)

[5.1 Process Integration 28](#_Toc232857964)

[5.2 Preceding Processes 28](#_Toc232857965)

[5.3 Succeeding Processes 28](#_Toc232857966)

## Purpose

Overview

This scope item covers the Return to Seller process for a customer return scenario in the Consumer Products industry.

A return order is created in reference to the original billing document. Once saved, a return delivery is automatically generated. The goods, once received, are inspected at the warehouse.

The user can influence when the refunding documents are created: either directly, when releasing a return order, or after the inspection. Finally, the user can decide on the compensation for the customers: full or partial refund.

The progress of the return process can be monitored using a returns overview.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites to conduct the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role for the Administrator in the product assistance for SAP S/4HANA Cloud Public Edition.

Table 1:

| Name (Role Template) | ID (Role Template) | Name (Space) | ID (Space) | Log On |
| --- | --- | --- | --- | --- |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

This scope item requires new master data set to be created and the needed master data objects are mentioned below:

Material Master Data:

| Data | Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Material | FG0502 | Display Med + Dark 48 * 1kg Arabica | Batch administrated, best before date, Sales BOM |
| Material | FG0511 | Carton 12 x 1kg Bags Medium Beans Arabica | Batch administrated, best before date |
| Material | FG0512 | Carton 12 x 1kg Bags Dark Beans Arabica | Batch administrated, best before date |
| Material | TG0501 | Thermo Coffee Cup 0,4l | No serial number, no batch |

Organization Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A331R | Std. storage 1Storage Location Returns |  |
| Controlling Area | A000 | Controlling Area A000 |  |
| Shipping Point | 3310331R | Shipping Point 3310Shipping Point 331R |  |
| Sales organization | 3310 | Dom. Sales Org |  |
| Distribution channel | 10 | Direct Sales |  |
| Division | 00 | Product Division 00 |  |

Customer:

Customer masters (Business Partners) provided as part of standard best practices will be used. No need to create new Customer masters for this E2E scenario. Below mentioned Customers (Business Partners) will be used in this scenario.

| Master Data | Value | Master Data Details | Comments |
| --- | --- | --- | --- |
| Sold-to Party | 33105001 | Domestic CP Customer 01 |  |
| Ship-to Party | 33105001 | Domestic CP Customer 01 |  |
| Payer | 33105010 | Domestic CP Payer Customer 10 |  |
| Sales Organization | 3310 |  |  |
| Distribution Channel | 10 |  |  |
| Division | 00 |  |  |
| Shipping point | 3310 |  |  |
| Company code | 3310 |  |  |

For more information on creating your own master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met

Table 2:

| Scope Item | Business Condition |
| --- | --- |
| 5HL - Sell from Stock – Consumer Products | Before running this test script, complete all activities in test script 5HL using master data, which is listed in the previous section Master Data, Organizational Data, and Other Data and note down the created document numbers of sales order and billing document for further use. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period (BNZ) master data script. Posting Period is up to date. |

.

### SSCUIs

#### Additional Return Reason “Delivery Refusal”

In the CP industry it often occurs that customers refuse to accept the goods shipped to them, for example if the agreed delivery window agreed upon was missed. In such a case the truck returns to the delivering plant without having the goods unloaded. It is then a 100% return of the complete delivery. Still one wants to at least briefly inspect the goods if there has been damaged during transport. For this process a special return reason “delivery refusal” shall be created.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define the additional return reason.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the App | Open Manage Your Solution (F1241) | The Manage Your Solution screen displays. |  |
| 3 | Configure your solution | Configure Your Solution | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Filter Selection Criteria | Choose the following entries in filter bar and press Enter:Application Area: SalesSub Application Area: Claims, Returns, and Refund Management | All entries display in All Items section. |  |
| 5 |  | Find the entry with item name Customer Returns and choose arrow at the item end. | Configure Your Solution – Customer Returns screen displays. |  |
| 6 |  | In Configuration Steps section, choose Configure in column Actions for step Define Return Reasons for Customer Returns | Change View “Define Return Reasons for Customer Returns”: Change screen displays. |  |
| 7 |  | Choose New Entries, enter the following data and choose Save.Ret.Reason: for example: ZC1Return Reason Description: for example: Delivery Refusal | Return reason is defined. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Return Reasons for Customer Returns | In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Return Reasons for Customer Returns.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Display View Define Return Reasons for Customer Returns screen displays. |  |
| 3 |  | Choose New Entries, enter the following data and choose Save.Return Reason: ZC1Description: Delivery Refusal | Return reason is defined. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the home page will only contain the essential apps for performing the typical tasks of a business role.

You can find all other apps not included on the home page using the search bar.

If you want to personalize the home page and include the hidden apps, navigate to your user profile and choose Settings > App Finder .

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Goods are Returned to Seller |  |  |  |
| [Create Return Order](#unique_9) | Customer Returns | Open Manage Customer Returns (F1708) | Return order is created, return delivery is generated in the background. |
| [Execute Picking](#unique_10) | Shipping | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | Picking is done for the return delivery. |
| [Post Goods Receipt](#unique_11) | Shipping | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) | The goods receipt is posted for return delivery. |
| [Perform Material Inspection](#unique_12) | Receiving | Enter Inspection Results - From Warehouse (MSR_INSPWH) | Inspection results are recorded. |
| [Determine Refund](#unique_13) | Customer Returns | Manage Customer Returns (F1708) | Refund determination is checked or triggered. |
| [Display Return Overview](#unique_14) | Customer Returns | Manage Customer Returns (F1708) | Document flow is displayed. |
| Credit Memo |  |  |  |
| [Create Credit Memo](#unique_15) | Billing | Create Billing Documents (F0798) | Credit memo is created. |
| Scheduling Job (Alternative) |  |  |  |
| [Job Scheduling for Goods Issue Deliveries (Alternative)](#unique_16) | Shipping | Schedule Goods Issue for Deliveries (F2259) | Job for goods issue posting with reference to outbound deliveries is scheduled. |
| [Job Scheduling for Billing Creation (Alternative)](#unique_17) | Billing | Schedule Billing Creation (F1519) | Job for creating billing documents is scheduled. |
| [Job Scheduling for Billing Release (Alternative)](#unique_18) | Billing | Schedule Billing Release (F1518) | Job for release billing documents to accounting is scheduled. |
| [Job Scheduling for Billing Output (Alternative)](#unique_19) | Billing | Schedule Billing Output (F1510) | Job for billing document outputs is scheduled. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The test should take around 60 minutes. The Enterprise search function provides a central entry point for finding business objects in your company from different sources using a single search request, such as: Apps, fact sheets for business objects. From the data found, you can go directly to the respective apps and fact sheets to display, edit the data or find related objects.

How to access and check a fact sheet:

Log on to the SAP Fiori Launchpad using the respective user example, Internal Sales Representative.

Access the Enterprise Search Bar and choose the magnifying glass button in the upper right corner.

The Enterprise Search bar is displayed, two filter fields appear left to the search button. Enter your search criteria and choose the business object type, example: Customer Returns from dropdown menu in 1st field, enter customer return order number in 2nd field and choose Search, The sales order is listed.

Choose the sales order number link, the system navigates to fact sheet screen and return order related information is integrated and sum-marized in one Fiori page. You can get detailed data via choosing the corresponding links.

There are fact sheets available for the following objects (Visible depending on the assigned role):

- Sales (return) order
- Quotation
- Billing document
- Credit Memo
- Debit Memo
- Customer 360 Fact sheet

### Goods are Returned to Seller

#### Create Returns Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a returns order.

|  |
| --- |
| Note This chapter mainly introduces follow-up activity 0001 - Receive into Plant after which material inspection needs to be performed for further inventory movement of returned materials. If you can specify the final destination of the returned materials when creating returns order and expect to skip subsequent material inspection chapter, just choose one alternatively from below:* 0002 - Immediately Move to Free Available Stock* 0003 - Immediately Move to Scrap* 0014 - Immediately Move to Specified StockWith above follow-up activities 0002 or 0003, it is mandatory to maintain inspection result in returns order. Once returns order is saved, returns delivery, picking and goods receipt will be generated automatically in background, next run the refund relevant steps:[Determine Refund](#unique_13)[Display Return Overview](#unique_14)Refund Customer with Credit Memo |

Prerequisite

You must have billing document, pro-froma invoice or sales order as reference (refer to [Business Conditions](#unique_17))

|  |
| --- |
| NoteGenerally, you take over the product ownership from the customer and the product is valuated when you refund a customer with either a replacement or a credit memo. There may be scenarios where you want to refund the customer but do not expect the refund to signal the decision on the ownership because the product inspection has not been completed yet. In such cases, perform the following steps to suspend product valuation until final logistical follow-up activity is confirmed in product inspection.Depending on your environment in SAP S/4HANA Cloud Public Edition, use SSCUI 106396 in SAP Fiori Launchpad or configuration activity Configure Returns Order Type for Standard Return in SAP Central Business Configuration to activate the function of suspending product valuation.Check the checkbox Suspend Valuation of the returns item of CBAR order which is created via app Manage Customer Returns - Version 2 (F4832) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708).Note Alternatively, SAP system supports creating returns order without reference using app Manage Customer Returns - Version 2 (F4832). On the Manage Customer Returns - Version 2 (F4832) screen, choose Create > Create Returns Order - VA01. After manually entering order type CBAR and other necessary data, choose Save to create returns order without reference. | The Manage Customer Returns screen displays. |  |
| 3 | Create Returns Order | Choose Create. | The Create Returns Order from Reference Document screen displays. |  |
| 4 | Enter Data | Use Adapt Filters to add Reference Document field if it is hidden.Enter the following selection criteria in the filter bar and choose Go:Reference Document:: <billing document number, which is created previously> | Billing (sales) documents are displayed in the Reference Documents table. |  |
| 5 | Choose Create | Choose Create in the billing (sales) document entry. | The dialog box Create Returns Order from Invoice (Sales) appears. |  |
| 6a | Option 1: Enter Data for normal return | Enter the following data and choose CreateReturn Reason: for example, Customer ordered too muchQuantity: <quantity to be returned> | Returns order is created.System navigates to Edit Returns Order screen. |  |
| 6b | Option 2: Enter Data for delivery Refusal | Enter the following data and choose Create:• Return Reason: for example, Delivery RefusalChoose Auto Fill to copy the items and quantities from the referenced invoice. | returns order is created with open quantitySystem navigates to Edit Returns Order screen. |  |
| 8 | Navigate to Follow-up Activities Screen | On the top right corner of the screen, choose Followup Activities. | The Follow-up Activities screen displays. |  |
| 9 | Check Follow-up Activity | Check Receive into Plant (0001) is maintained in the Follow-Up Activity column.Choose Back. | The Edit Returns Order screen displays. |  |
|  |  | The user can influence the point in time when the refunding document must be created: Either immediately when the returns order is saved and released or at a later point of time. Combination of the refund setting determines follow-up document creation. Choose one among the following options to continue: |  |  |
| 11 | Option 1: Execute Refund with Credit Memo Request Immediately | In the Refund section, enter the following data or action, then choose Apply:Refund Type: Credit MemoRefund Code: <select one from down-drop list>, for example, 10%.Note Refund deduction (condition type DRE1) is determined automatically based on the refund code entered.The following steps guides you how to define more refund codes and related condition records:Define returns refund codes via SSCUI 104235Maintain condition records for DRE1 using the Set Material Prices – Sales app. For more details, refer to master data script Create Sales Pricing Condition - MDS (BET).Refund Control: Create Credit Memo RequestChoose Save and Release. | returns order is created.Note Returns delivery and credit memo request are generated automatically. |  |
|  | Option 2: Execute Refund with Credit Memo | On the top right corner of the screen, choose Follow-up Activities, maintain the following data and choose Back:Follow-up Activity: Receive into Plant (0001)Product Received: XOn the Edit Returns Order screen, in the Item area, in the Refund Details column, enter the following data or action:Refund Type: Credit MemoRefund Code: 10% (select from dropdown list)Refund Control: Create Credit MemoChoose Save and Release. | Returns order is created.Note Subsequent documents are generated in background including:Returns deliveryGoods receipt of returns deliveryCredit memo |  |
| 13 | Check Process Flow | On the Manage Customer Returns screen, choose arrow at the end of the item. In the Process flow area, check dependent documents in process flow. Make a note of the follow-up document numbers for further use.Note If you need to delete returns order, execute below steps after its subsequent documents are deleted: On the Manage Customer Returns screen, select your returns order and choose Delete. | The Display Returns Order screen displays and the dependent document(s) display(s). |  |

|  |
| --- |
| Note If freight was maintained in previous delivery document header and material was partly returned regarding billing document, please check (or change if necessary) freight amount for condition type YBHD in the header(s) of returns order (and credit memo request document if it is generated automatically) using the role Internal Sales Representative (SAP_BR_INTERNAL_SALES_REP) and the Change Sales Order tile.If requested delivery date is reached and delivery document has not been created, warning information delivery issue will show in process flow as a reminder. Once delivery document is generated later, such alert will disappear. |

#### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, picking is done for returns delivery created previously. This process step shows you how to perform picking.

In Case of Refund Control: Create Credit Memo, picking quantity is not applicable.

If batch managed material, enter the batch number as well (batch number can be referred from original Delivery document).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Picking | Choose For Picking. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: 331R |  |  |
| 5 | Change Outbound Deliveries | On the Day’s Workload for Picking screen, select your delivery number and choose Change Outbound Deliveries. |  |  |
| 6 | Enter Picked Quantity | On the Picking tab, input quantity equal to delivery quantity in the Picked Qty field.Enter batch number in the Batch field if the material is batch managed.Note In case the return delivery contains product FG0502, the BOM-sub items are as well shown in the picking overview. They are logistically not relevant and can be ignored. |  |  |
| 7 | Choose Enter | Press Enter. |  |  |
| 8 | Save | Choose Save. | The delivery is picked. |  |

#### Post Goods Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the returned material is received, goods receipt is posted for returns delivery. This process step shows you how to post a goods receipt.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Outbound Deliveries - VL06O (VL06O_CLOUD). |  |  |
| 3 | Choose Goods Issue | Choose For Goods Issue. |  |  |
| 4 | Enter Shipping Point | Make the following entries and choose Execute:Shipping Point: 331R. |  |  |
| 5 | Post Goods Receipt | Mark the relevant delivery and choose Post Goods Issue. Choose date of today from the dialog box. | The goods receipt is posted. |  |

#### Perform Material Inspection

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

The returned goods are received.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH). | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Maintain Selection Criteria | Enter the following entries and choose Execute:Delivery Items Waiting for Inspection: <select>Delivery: <enter returns delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Choose Item Tab | Choose Item tab. |  |  |
|  | Inspection Split (Optional) | If different inspection results need to be recorded for the same delivery item, perform below actions, otherwise you can directly skip this step.Select the delivery item and choose Create Split Item, then run steps 5-6 for all inspection items. |  |  |
| 5 | Maintain Inspection Result | In the Inspection Result subarea, enter the following data, and press Enter:Inspection Code: <enter inspection code>Inspected Quantity: <enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Maintain Follow-up Activity | In the Logistical Follow-up subarea, enter the following data and press Enter:Follow-up Activity: <enter follow-up activity>Note Choose appropriate follow-up activity according to inspection code. For example, choose follow-up activity Transfer to Free Available Stock responding to inspection code 0001.Choose suitable Follow-Up Activity from below options according to your subsequent scenarios:0011 Transfer to Free Available Stock0012 Transfer to Scrap0015 Transfer to Specified Stock0018 Transfer to Scrap for Customer0021 Send Back to Customer0023 goods receipt quantity correction |  |  |
| 7 | Check Inspection Status | On the Header tab, in the Basic Data subarea, Inspection Status shows Inspected, which means all received materials are inspected completely. | All received materials are inspected completely. |  |
| 8 | Save and Confirm | In menu bar at the top of screen, choose Save and Confirm.Note Do not choose Save Inspection Results at the bottom right of the screen, as subsequent material documents will not be automatically generated. | Inspection result is recorded, and goods movement is posted accordingly. |  |

#### Determine Refund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, refund decision is made.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns - Version 2 (F4832). | The Manage Customer Returns - Version 2 screen displays. |  |
| 3 | Search for Returns Order | Choose Adapt Filters to add Returns Order field, if it is hidden. Enter the following data and choose Go:Returns Order : <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Navigate to Determine Refund Screen | Select the returns order entry and choose Determine Refund. | The Determine Refund screen displays. |  |
| 5 | Check Refund Progress | In the upper area, check percentage number in the field Refund Progress and then take next action accordingly:<100%: Refund determination is not completed. Go to Section A and then Section B.100%: Refund determination is completed. Skip Section A and go to Section B. |  |  |
| Section A: Refund is determined with reference to product inspection results | Option 1: Credit Memo | On the Items to Be Refunded tab, choose Change Refund in the Refund Details column for the return item.Enter the following data:Refund Type: Credit MemoExtent of Refund: <a percentage number>, for example, 10% RefundChoose OK.Select the item and choose Release Selected Items.Note For send back to customer scenario, enter the following data:Refund Type: No RefundCMR Rejection Reason: 59 Damaged by customer | Refund setting is maintained, and credit memo request document is created in background. |  |
| Section B: Check refund determination result | Check refund results | On the Completed Items tab, refund result is displayed. Follow-up document number is shown in Refund Details column. Make a note of document number for further use. You can click the created document number to check detailed information. | The refund result displays. |  |

#### Display Returns Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the progress of returns process. All dependent documents are available in process flow.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Returns and Refund Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Customer Returns (F1708). | The Manage Customer Returns screen displays. |  |
| 3 | Search for returns Order | Choose Adapt Filters if Returns Order field is hidden. Enter the following data and choose Go:Returns Order: <returns order number 6XXXXXXX> | Returns order is found and displayed. |  |
| 4 | Order Overview | Click the created returns order number 6XXXXXXX and choose Display Customer Return. | The Display Standard Return 6XXXXXXX: Overview screen displays. |  |
| 5 | Document Flow | On Returns tab, choose Returns Overview in Returns Control area. | The Returns Overview for Returns Order 6XXXXXXX - 10 screen displays. |  |
| 6 | Check Document Flow | In Document Number column, make a note of follow-up document number(s) of credit memo request for further use. |  |  |

|  |
| --- |
| Note After you have completed this activity:Option A: If credit memo request is generated, go to the Refund Customer with Credit Memo chapter. |

#### Credit Memo

##### Create Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a credit memo.

Applicable in case where Refund Control: Create Credit Memo Request

Procedure

Table 3: Create Billing Document

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents (F0798). | The Create Billing Document screen displays. |  |
| 3 | Define Billing Setting | Choose Billing Settings.Maintain settings as below.Set Billing Data and type before billing: ONCreate separate Billing Documents for Each item of Billing Due List: ON.Automatically Post Billing Documents: ONDisplay Billing Document after creation: ON.Choose delivery item to be billed and select quantities: OFF. |  |  |
| 4 | Search for Billing List | In the search condition, enter criteria if necessary. | SD document(s) display(s) in the result. |  |
| 5 | Choose SD Document | Select the row of credit memo request document recorded previously and choose Create Billing Documents. | The Create Billing Documents (F0798) screen displays. |  |
| 6 | Maintain Billing Type and Date | Choose billing type Credit Memo (G2) and maintain billing date, such as the current date, and then choose OK. | The draft billing document with ID Sxxxxxxxx displays. |  |
| 7 | Save Billing Document | On the Manage Billing Documents screen, choose Save. The draft version billing document with ID Sxxxxxxxx turns into a saved billing document with ID xxxxxxxx. Make a note of the billing document number: __________. | Final credit memo is generated. |  |

Table 4: Manage Billing Documents

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Access the App | Open Manage Billing Documents (F0797). | The Manage Billing Documents screen displays. |  |
| 2 | Search Billing Document | Enter the billing document number recorded previously, and press Enter. | The billing document which is created previously displays. |  |
| 3 | Display Billing Document | Select the billing document item, and choose Display. | The billing document displays. |  |
| 4 | Check Output Condition | On the Billing Document screen, go to the last assignment block, Output Items. | There is one entry in the item and the output type is BILLING_DOCUMENT. |  |
| 5 | Display Print Preview | On the Billing Document screen, choose Preview. | Preview for PDF document displays. |  |
| 6 | Cancel Billing Document (Optional) | On the Billing Document screen, select a certain billing document and choose Cancel Billing Document. | A log displays the following message: Billing Document Canceled. |  |
| 7 | Update new Attachment (Optional) | In the Edit mode, you can add, delete, and update the attachments. Save your changes by choosing Save in the footer bar. |  |  |
| 8 | Update new Text (Optional) | In the Edit mode, you can add, delete, and update the texts. Save your changes by choosing Save in the footer bar. |  |  |

### Scheduling Job (Alternative)

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
| 3 | Create Goods Issue Deliveries Schedule | Choose Create to define a new job. | The New Job screen displays. The Job Template should be defaulted as Schedule goods issue for Deliveries. |  |
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

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Preceding Processes

Before this scope item can be tested, the following business conditions must be met

Table 5:

| Scope Item | Business Condition |
| --- | --- |
| 5HL - Sell from Stock - Consumer Products | Before running this test script, complete all activities in test script 5HL using master data, which is listed in the previous section Master Data, Organizational Data, and Other Data and note down the created document numbers of sales order and billing document for further use. |

.

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes

Table 6:

| Process | Business Condition |
| --- | --- |
| Sales Order Fulfillment Monitoring (BKK) (optional) | Using the master data from this document, complete the following activities described in the test script:Review sections: Incomplete SD Documents (deliveries) and Review Outbound Deliveries for Goods Issue |

:

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
> Flagged while digesting this document, not verified: Overview Table lists Determine Refund under Manage Customer Returns (F1708), but the Determine Refund procedure uses Manage Customer Returns - Version 2 (F4832).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[08-sales-order-management/customer-returns-bkp-ae-test-script-sap-s-4hana-cloud-public-edition-1]]
- related-to :: [[08-sales-order-management/customer-returns-for-non-stock-and-service-materials-3te-ae-test-scrip]]
- related-to :: [[08-sales-order-management/test-script-customer-returns-involving-supplier-by-message-exchange-3q]]
- related-to :: [[08-sales-order-management/test-script-customer-returns-with-direct-shipment-from-customer-to-sup]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/61V_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 48,717 chars in the whole document
