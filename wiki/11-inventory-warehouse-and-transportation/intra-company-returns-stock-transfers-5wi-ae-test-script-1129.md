---
id: 11-inventory-warehouse-and-transportation/intra-company-returns-stock-transfers-5wi-ae-test-script-1129
title: Intra-Company Returns Stock Transfers (5WI_AE) - Test Script (5WI_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud test script for scope item 5WI_AE: returning stock between plants of one company code, with prerequisites, roles, apps and test steps."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/stock-transfer-returns]
aliases: [5WI_S4CLD2608_BPD_EN_AE]
keywords: [Stock Transfer Returns, intra-company returns, stock transport orders, test scripts, outbound delivery, goods issue, inbound delivery, goods receipt, material inspection, putaway]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WI_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1129
topic: 11-inventory-warehouse-and-transportation/stock-transfer-returns
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Intra-Company Returns Stock Transfers (5WI_AE) - Test Script (5WI_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WI_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Stock Transfer Returns** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Intra-Company Returns Stock Transfers (5WI_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Intra-Company Returns Stock Transfers (5WI_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857290)

[2 Prerequisites 4](#_Toc232857291)

[2.1 System Access 4](#_Toc232857292)

[2.2 Roles 4](#_Toc232857293)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232857294)

[2.4 Additional Manual Configuration 6](#_Toc232857295)

[2.5 Business Conditions 6](#_Toc232857296)

[2.6 Preliminary Steps 6](#_Toc232857297)

[2.6.1 Open New MM Period 6](#_Toc232857298)

[2.6.2 Creating Stock in Ordering Plant 7](#_Toc232857299)

[3 Overview Table 8](#_Toc232857300)

[4 Test Procedures 9](#_Toc232857301)

[4.1 Create Returns Stock Transport Order 9](#_Toc232857302)

[4.2 Create Outbound Delivery for Return Stock Transport Order 10](#_Toc232857303)

[4.3 Optional: Create Pro Forma F8 Invoice 11](#_Toc232857304)

[4.4 Perform Picking and Post Goods Issue for Outbound Delivery 12](#_Toc232857305)

[4.5 Check Batches (Optional) 13](#_Toc232857306)

[4.6 Check Status of Stock Transfer 14](#_Toc232857307)

[4.7 Check Inbound Delivery 15](#_Toc232857308)

[4.8 Confirm Quantities for Putaway 16](#_Toc232857309)

[4.9 Post Goods Receipt for Inbound Delivery 17](#_Toc232857310)

[4.10 Perform Material Inspection 17](#_Toc232857311)

[4.11 Check Stock Status 19](#_Toc232857312)

[5 Appendix 20](#_Toc232857313)

[5.1 Job Scheduling (Alternative) 20](#_Toc232857314)

[5.1.1 Job Scheduling for Delivery Creation (Alternative) 20](#_Toc232857315)

## Purpose

Overview

The intra-company returns stock transfer process begins with a requirement to return a material from one plant to another plant within the same company code. The return of the material is triggered for a number of reasons, such as damage during transportation, product defect or damage, over-delivery or wrong delivery, end of promotion or season, and so on.

The issuing plant creates a returns stock transport order in the system. A shipping specialist at the issuing plant monitors the materials due to be shipped and creates deliveries as required. Once a return delivery is created, a pick list is generated for the outbound delivery. A warehouse clerk gathers the materials and confirms the picked quantities. The delivery quantities are issued when the return delivery is complete. When you post the goods issue for the outbound delivery, the system automatically creates an inbound delivery for the receiving plant.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP FIORI Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, refer to How to Create a Business Role for the Administrator in the [product assistance](https://help.sap.com/viewer/a630d57fc5004c6383e7a81efee7a8bb/latest/en-US/8fa28e0107984d42a99b9eea67856cea.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Plant | 3320 | Plant 2 AE | Flex.Org App or Set Up Organizational (SAP Central Business Configuration) extensionNote The second set of organization entity IDs here is an example. In an evaluation project of the SAP Central Business Configuration environment, the ID follows the naming rule described in [Using the Set Up Organizational Structure App](https://help.sap.com/docs/CENTRAL_BUSINESS_CONFIGURATION/55c9333eed324cd284f6c4e5dab8462f/d020ff461d504421bcc55d87cbc0ae57.html). |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 332R | Returns | Flex.Org App or Set Up Organizational (SAP Central Business Configuration) extensionShop floor w/o lean WM |
| Company Code | 3310 | Company Code 3310 |  |
| Purchase Organization | 3310 | Purch. Org. 3310 |  |
| Purchasing group | 001 /002 | Group 001 /Group 002 |  |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) |  |

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNE | Create Supplier Master - MDS |
| BND | Create Customer Master - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/91fff1745e573e79b14fb086c1080ef4)

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | Complete all relevant steps. |

Before you start the testing, please make sure the set_up in the scope item specific customer facing document [Intracompany Stock Transfer with Delivery Setup (BME).docx (Public)](https://support.sap.com/content/dam/SAAP/SAP_Activate/S4H_506%20Intracompany%20Stock%20Transfer%20with%20Delivery%20Setup%20(BME).docx) has been completed.

### Preliminary Steps

#### Open New MM Period

External Process

For this activity, run the following step from the Create New Open MM Posting Period - MDS (BNZ) to close MM period and open new posting period.

Closing MM Period and Opening New Posting Period

#### Creating Stock in Ordering Plant

Purpose

For the purpose of this test, we post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Enter Material | Make the following entry and choose Enter.Material: TG11Plant: 3310 |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: 331AUnrestricted-Use Stock | The Manage Stock dialog box opens. The Storage Location, Stock Type and Current Quantity are displayed according to your entries in previous steps. |  |
| 5 | Add Initial Stock | Make the following entries and choose Post:Document Date: <Today>Posting Date: <Today>Stock Change: Initial EntryQuantity: Enter a number, for example, <100> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

## Overview Table

The scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App Name / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Returns Stock Transport Order](#unique_11) [page ] 9 | Purchaser | Create Purchase Order - Advanced (ME21N) | A new purchase order is created. Purchase order number is displayed. |
| [Create Outbound Delivery for Return Stock Transport Order](#unique_12) [page ] 10 | Shipping Specialist | My Purchase Orders - Due for Delivery (VL10B) | A delivery is created. |
| [Optional: Create Pro Forma F8 Invoice](#unique_13) [page ] 11 | Billing Clerk | Create Billing Documents - VF01 (VF01) | A Pro Forma invoice is created. |
| [Perform Picking and Post Goods Issue for Outbound Delivery](#unique_14) [page ] 12 | Shipping Specialist | Change Outbound Delivery (VL02N) | Outbound Delivery is created. |
| [Check Batches (Optional)](#unique_15) [page ] 13 | Shipping Specialist | Change Outbound Delivery (VL02N) | Batch numbers are assigned to the materials. |
| [Check Status of Stock Transfer](#unique_16) [page ] 14 | Warehouse Clerk | Stock - Single Material (F1076) |  |
| [Check Inbound Delivery](#unique_17) [page ] 15 | Purchaser | Manage Purchase Orders (Version 2) (F0842A) |  |
| [Confirm Quantities for Putaway](#unique_18) [page ] 16 | Receiving Specialist | Change Inbound Delivery (VL32N) | The material of the Inbound Delivery has been Putaway |
| [Post Goods Receipt for Inbound Delivery](#unique_19) [page ] 17 | Receiving Specialist | Inbound Deliveries for Goods Receipt (VL06IG) | The goods receipt is posted. |
| [Perform Material Inspection](#unique_20) [page ] 17 | Receiving Specialist | Enter Inspection Results - From Warehouse (MSR_INSPWH) | Inspection result is recorded, logistical follow-up document is posted accordingly. |
| [Check Stock Status](#unique_21) [page ] 19 | Warehouse Clerk | Stock - Single Material (F1076) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Returns Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order screen displays. |  |
| 3 | Enter Purchase Order Document Type | Enter the following data:Order Type: UD2 (STO Del Return)Then choose Enter. |  |  |
| 4 | Enter Purchase Order Data | Enter the following data:Supplying Plant: 3320On the Org. Data tab:Purchasing Org.: 3310Purchasing Group: 002Company Code: 3310In the area of Overview Item:Material: TG11Quantity: x pcDelivery Date: any date in the futurePlant: 3310Storage Location: 331AThen choose Enter. | All data are entered, the item detail screen displays. |  |
| 5 | Save Purchase Order | Choose Save and when the stock transfer returns order number is displayed, write it down for further use.You may get a warning message Following mandatory roles missing in partner maintenance: VN if partner function VN is not maintained on purchaser order header. You can refer to the Setup Instruction of 5WI to omit this warning message. | A new stock transfer returns order is created. Stock transfer returns number is displayed.Write down the stock transport returns order number for further usage. |  |

### Create Outbound Delivery for Return Stock Transport Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Purchase Orders - Due for Delivery (VL10B). | The Goods Movement screen displays |  |
| 3 | Enter data for PO display | Choose the Purchase Orders tab and make the following entries then choose Execute:Shipping Point: 3310Delivery Creation Date (From): <delivery creation From date>Delete the default date.Delivery creation dates (To): <delivery creation To date>Delete the default date.Calc Rule: <calculation rule> 3 | The Activities Due for Shipping Purchase Orders, Fast Display screen appears. PO due to delivery is listed out. |  |
| 4 | Enter PO Number | Go to tab: Purchase OrdersEnter PO number created in previous step.Choose Execute. |  |  |
| 5 | Create Delivery | Select stock transport orders from the list. Choose Background to create delivery in background. | The Activities due for shipping purchase orders, fast display screen appears. |  |
| 6 | Check Delivery Number | Choose More > Show/Hide Delivery and note down the outbound delivery number shown in the SD Doc. field | A delivery is created. |  |

### Optional: Create Pro Forma F8 Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create the Pro Forma invoice in the selling company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Billing Documents - VF01 (VF01). | The Create Billing Documents screen displays. |  |
| 3 | Maintain Billing Date | Make the following entries:Billing Type: Pro Forma Invoice for Delivery (F8)Billing Date: For example, <current date>Enter delivery number in the Document field and press Enter. |  |  |
| 4 | Save | Choose Save. | The F8 billing document is created.Note down the document number. |  |
| 5 | Search Billing Document | Open Display Billing Documents (VF03). | The Display Billing Documents screen displays. |  |
| 6 | Display Billing Document | On the Display Billing Documents screen, enter the Billing Document number, and choose Continue. | The Pro Forma Invoice for Delivery xxxxxxxx Display: Overview of Bi screen displays. |  |
| 7 | Check Output Condition | On the Pro Forma Invoice for Delivery xxxxxxxx Display: Overview of Bi screen, choose Change Bill. Doc. and then choose Menu > Goto > Header > Output . | The Pro Forma Invoice for Delivery xxxxxxxx Change: Output screen displays. |  |
| 8 | Display Print Preview | On the Pro Forma Invoice for Delivery xxxxxxxx Change: Output screen, select the output entry and choose Display Document. | A preview for PDF document displays. |  |
| 9 | Print Billing Document | From the preview of the document, choose Print. |  |  |

### Perform Picking and Post Goods Issue for Outbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Adv.Returns Delivery XXXXXXXX Change: Overviewscreen displays. |  |
| 4 | Check Batch Split | Navigate to the Picking tab, check if batch split exists in the Batch Split Indicator column. |  |  |
| 5 | Enter Picked Quantity | If batch spilt exists, choose Batch Split Exists to expand sub item(s), enter quantity equal to delivery Qty in Picked Qty field for sub item.If batch spilt doesn't exist, enter quantity equal to Delivery Qty in Picked Qty field for picking related item(s). | The system shows the message: Adv.Returns Delivery XXXXXXX has been saved.. The screen returns to Change Outbound Delivery screen. |  |
| 6 | Post Goods Issue | On the Change Outbound Delivery screen, choose Post Goods Issue. |  |  |

### Check Batches (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Outbound Delivery (VL02N). | The Change Outbound Delivery screen displays. |  |
| 3 | Enter Delivery Number | On the Change Outbound Delivery screen, enter the delivery document number from the earlier section and choose Continue. | The Adv.Returns Delivery XXXXXXXX Change: Overview screen displays. |  |
| 4 | Check Batch Number Assignment | If Expand Batch Spilit exists, select the Batch Split Indicator field, and check the batch number assignment. | Batch numbers are assigned to the materials. The batch numbers are required to be entered during Post Goods Receipt step. |  |
| 5 | Save Document | Choose Save. |  |  |

### Check Status of Stock Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock - Single Material screen displays. |  |
| 3 | Enter Transfer Order Data | Enter material TG11 and choose Enter. | You receive an overview of the material. This concerns all material that has left the supplying plant and has not yet arrived at the receiving plant. |  |

### Check Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the inbound delivery which the system generates automatically when you psot the goods issue for the outbound delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Purchase Orders (Version 2) (F0842A). | The Manage Purchase Order screen displays. |  |
| 3 | Search for Returns Stock Transport Order Number | Enter the returns stock transport order number in Search field.Then choose GO. | All data is entered. |  |
| 4 | Display Returns Stock Transport Order | Select the returns stock transport order which is in the purchase orders list. | The Display Purchase Order screen appears. |  |
| 5 | Check Inbound Delivery Number | On the Display Purchase screen, choose Returns in Item Detail tab.Choose Returns Overview on Returns tab. The Returns Overview for Returns STO xxxxxxx-xx screen displays.You can check the inbound delivery number in returns steps list. | Write down the inbound delivery number for further usage. |  |

### Confirm Quantities for Putaway

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is to confirm all the materials of the inbound delivery that have been put away in the correct quantities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori Launchpad as a Receiving Specialist. | The Fiori Launchpad displays. |  |
| 2. | Access the App | Open Change Inbound Delivery (VL32N). | The Change Inbound Delivery screen appear. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries then choose Execute:Inbound Delivery: Enter the Inbound Delivery Number Created in the Previous Step. | The Inbound IC Inb.Returns Del. XXX Change: Overview screen appears. |  |
| 4 | Confirm Quantities for Putaway | On Item Overview tab:Storage Location: 332REnter the Putaway Qty for the items: XXXThe putaway quantity should equal to the Delivery Qty.And choose Save. | Back to the Inbound Deliveries for Putaway screen and the "Inbound Delivery XXX has been saved."message displays. |  |

### Post Goods Receipt for Inbound Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity is performed to Post Goods Receipt for the Inbound Delivery to receive the materials to stock. The step Optional: Confirm Quantities for Putaway is a prerequisite process step and has to be performed before this activity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2. | Access the App | Open Inbound Deliveries for Goods Receipt (VL06IG). | The Inbound Deliveries for Goods Receipt screen displays. |  |
| 3 | Enter Inbound Delivery Number | Make the following entries then choose Execute:Inbound Delivery: Enter Inbound Delivery number created in the previous step.Delivery Date: Delete the default date | The Goods Receipt for Inbound Deliveries to be Posted screen shows up.The selected inbound deliveries display. |  |
| 4 | Change the Inbound Delivery | Check the selected inbound deliveries and choose Post Goods Receipt.The specify Actual Goods Receipt Date dialog box displays and choose Continue. | The goods receipt is posted.A success message is shown. |  |

### Perform Material Inspection

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The material inspection takes place after you have posted the goods receipt in the receiving plant. The further logistical handling of the returned materials is decided. This process step shows you how to perform material inspection.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Receiving Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Enter Inspection Results - From Warehouse (MSR_INSPWH) | The Worklist Selection of Deliveries screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Delivery items waiting for inspection: <select>Delivery: <Enter Inbound delivery number> | The Change: Material Inspection in Warehouse for Delivery screen displays. |  |
| 4 | Choose Item Tab | Choose Item. |  |  |
| 5 | Enter Inspection Result | In the Inspection Result subarea, enter the following data and choose Enter:Inspection Code: <Enter inspection code>Inspected quantity: <Enter inspected quantity>If the Confirmation of Redetermination dialog box appears, choose Yes to confirm. |  |  |
| 6 | Enter Follow-Up Activity | In Logistical Follow-Up subarea, enter the following data and choose Enter:Follow-Up Activity: <Enter follow-up activity>Note Choose appropriate logistical follow-up activity according to inspection code. For example, choose follow-up activity 0011--Transfer to Free Available Stock responding to inspection code 0001. |  |  |
| 7 | Check Inspection Status | Under the Header tab, in Basic Data subarea, Inspection status shows Inspected, which means all received material is inspected completely. | All received material is inspected completely. |  |
| 8 | Save and Confirm | Choose Save and Confirm.Note Please do not choose Save Inspection Results. | Inspection result is recorded, logistical follow-up document is posted accordingly. |  |

### Check Stock Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check stock status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stock - Single Material (F1076). | The Stock Single Material screen displays. |  |
| 3 | Enter Transfer Order Data | Enter material and choose Enter. | You receive an overview of the materials. This concerns all materials that have left the supplying plant and have already reached the receiving plant. Unrestricted use stock is increased after confirming the follow-up activity 0011--Transfer to Free Available Stock. |  |

## Appendix

### Job Scheduling (Alternative)

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
| 2 | Access App | Open Schedule Delivery Creation (F2228). | The Application Jobs screen displays.The app automatically shows the history of application jobs. |  |
| 3 | Create Delivery Creation Schedule | Choose Create to define a new job. | The New Job screen displays. The Job Template should be set to Schedule Delivery Creation for Purchase Orders by default. |  |
| 4 | Scheduling Options | Choose Step 2 to define scheduling for the batch job if necessary. | Depending on the scheduling options, the delivery creation is started immediately or at a specific time. |  |
| 5 | Job Parameters | Choose Step 3 to define parameters. Make at least the following entries:Shipping Point: 3310Purchasing Document: Stock Transport Order # created aboveThen choose Check. | The system displays the message Go ahead and schedule the job. |  |
| 6 | Schedule | Choose Schedule. | A delivery creation job is scheduled.The screen goes back to Application Jobs. |  |
| 7 | Check Delivery Creation Job Log | On the Application Jobs screen, after the status of the job item turns to Finished, choose Status symbol in the Log column.Note Choose the Magnifier, and the job list will be refreshed. | The Job Log screen displays. |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/test-script-intercompany-stock-transfer-returns-2ts-ae-sap-s-4hana-clo]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WI_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 34,887 chars in the whole document
