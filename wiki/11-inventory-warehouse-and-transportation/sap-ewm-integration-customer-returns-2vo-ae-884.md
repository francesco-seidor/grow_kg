---
id: 11-inventory-warehouse-and-transportation/sap-ewm-integration-customer-returns-2vo-ae-884
title: SAP EWM Integration – Customer Returns (2VO_AE) (2VO_S4CLD2608_BPD_EN_AE)
description: "Test script for scope item 2VO_AE: customer return order, return delivery, SAP EWM goods receipt and putaway in SAP S/4HANA Cloud Public Edition 2608."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-customer-returns]
aliases: [2VO_S4CLD2608_BPD_EN_AE]
keywords: [EWM Customer Returns, customer returns, ewm integration, return order, return delivery, goods receipt, warehouse tasks, putaway, material documents, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VO_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-884
topic: 11-inventory-warehouse-and-transportation/ewm-customer-returns
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# SAP EWM Integration – Customer Returns (2VO_AE) (2VO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Customer Returns** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP EWM Integration – Customer Returns (2VO_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | SAP EWM Integration – Customer Returns (2VO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851033)

[2 Prerequisites 4](#_Toc232851034)

[2.1 Additional Manual Configuration 4](#_Toc232851035)

[2.2 System Access 4](#_Toc232851036)

[2.3 Roles 4](#_Toc232851037)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232851038)

[2.5 Business Conditions 6](#_Toc232851039)

[3 Overview Table 7](#_Toc232851040)

[4 Test Procedures 8](#_Toc232851041)

[4.1 Create Return Order 8](#_Toc232851042)

[4.2 Create Return Delivery 9](#_Toc232851043)

[4.3 Post Goods Receipt in SAP EWM 10](#_Toc232851044)

[4.4 Create Warehouse Tasks for Putaway in SAP EWM 13](#_Toc232851045)

[4.5 Putaway of Products in SAP EWM 14](#_Toc232851046)

[4.6 Check Return Delivery (Optional) 15](#_Toc232851047)

[4.7 Check Material Document (Optional) 16](#_Toc232851048)

[5 Appendix 18](#_Toc232851049)

[5.1 Process Integration 18](#_Toc232851050)

[5.2 Succeeding Processes 18](#_Toc232851051)

## Purpose

Overview

The process starts with the creation of a return order and a return delivery in the SAP S/4HANA Cloud Public Edition system. The delivery is then transferred to SAP Extended Warehouse Management (EWM). In SAP EWM, a goods receipt is posted for the delivery and warehouse tasks are created to put the received goods back to the warehouse. The process ends with the confirmation of the warehouse tasks.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conduct the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/266cfafb22adf33f4bb5b5af99e11bfe)

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
| Receiving Specialist | SAP_BR_RECEIVING_SPECIALIST | Receiving | SAP_BR_RECEIVING_SPECIALIST |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | TG11 | Trading Good for Reg. Trading (MRP planning) |  |
| Sales Organization | 3310 | Dom. Sales Org |  |
| Plant | 3310 |  |  |
| Supply Chain Unit | YWAREHOUSE-3330 |  |  |
| Storage Location | 333D |  | Decentral EWM received on dock. |
| Storage Location | 333S |  | Decentral EWM available for sales. |
| Warehouse | 333 |  |  |
| EWM Warehouse | 3330 |  |  |
| Division | 00 |  |  |
| Distribution Channel | 00 |  |  |
| Shipping Point | 331R |  |  |
| Payer | 33100003 | Customer domestic 03 |  |
| Ship to party | 33100003 | Domestic UAE Customer 3 |  |
| Sold to party | 33100003 | Domestic UAE Customer 3 |  |
| Ent. To Dispose | 33413310 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| Master Data Script | Description |
| --- | --- |
| BNF | Create Product Master of type "Trading Good" - MDS |

### Business Conditions

Before testing this scope item, you have to meet the following business conditions.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting Period is up to date. |
| BD9 - Sell from Stock | To run through this scope item, you must already have sold some goods. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | System | Expected Result |
| --- | --- | --- | --- | --- |
| [Create Return Order](#unique_9) [page ] 8 | Internal Sales Representative | Create Sales Orders - VA01 (VA01) | SAP S/4HANA | The following system message appears: Lean Return Lean Return number has been saved. |
| [Create Return Delivery](#unique_10) [page ] 9 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) | SAP S/4HANA | The following system message appears: Returns Delivery Return delivery number has been saved. |
| [Post Goods Receipt in SAP EWM](#unique_11) [page ] 10 |  | /SCWM/PRDI | SAP Extended Warehouse Management | The following system message appears: Inbound Delivery number changed. |
| [Check Material Document (Optional)](#unique_12) [page ] 16 | Receiving Specialist | Material Documents Overview (F1077) | SAP S/4HANA | The Delivery Note is equal to the reference Warehouse Material Document from the previous step. |
| [Create Warehouse Tasks for Putaway in SAP EWM](#unique_13) [page ] 13 |  | /SCWM/TODLV_I | SAP Extended Warehouse Management | The following system message appears: Warehouse order number created. |
| [Putaway of Products in SAP EWM](#unique_14) [page ] 14 |  | /SCWM/TO_CONF | SAP Extended Warehouse Management | The following system message appears: Warehouse task warehouse task number was confirmed. |
| [Check Return Delivery (Optional)](#unique_15) [page ] 15 | Shipping Specialist | Manage Outbound Deliveries (F0867A) | SAP S/4HANA | In the Overall Status - Delivery table, check that the Overall Goods Movement Status is C Completely processed.In the Delivery Item Status (All Items) table, check that the Goods Movement Status for the items is C Completely processed. |
| [Check Material Document (Optional)](#unique_12) [page ] 16 | Inventory Manager | Material Documents Overview (F1077) | SAP S/4HANA | In the Material Documents table, the Storage Location is EWM Int ROD 333D and the Goods Movement Type is TF SLoc to SLoc (411) |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Return Order

Purpose

In this activity, you create the return order.

Prerequisites

You must have a reference sales order document according to Sell from Stock (BD9).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Sales Orders - VA01 (VA01) | The Create Sales Documents screen displays.Fast Entry |  |
| 3 | Enter Order Type | On the Create Sales Documents screen, make the following entries:Order Type: CBRE Lean ReturnSales Organization: 3310-Dom. Sales OrgDistribution channel: 10 - Direct SalesDivision:00 - Product Division 00 |  |  |
| 4 | Create Sales Document with Reference | Choose Create with Reference. | The Create with Reference screen appears. |  |
| 5 | Enter Sales Order Number | On the Order tab, make the following entries:Order: <Standard Order>Enter the sales order number to be referenced. |  |  |
| 6 | Item selection | Choose Item selection. |  |  |
| 7 | Copy | On the Standard Order <sales order number>: Selection List for Reference Document screen, select the items to be referenced in which open quantity is not equal to ‘0’ and choose Copy. | The Standard Order Sales Order Number: Selection List for Reference Document screen displays. |  |
| 8 | Enter Order Details | On the Create Lean Return: Overview screen, on the Sales tab, make the following entries:Order Reason: <Order Reason> For example, Poor quality. |  |  |
| 9 | Save | Choose Save.Note You can ignore any dialog box. | The following system message appears: Lean Return Lean Return number has saved. |  |

### Create Return Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the return delivery.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on to SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Outbound Delivery - With Order Reference (VL01N). | The Create Outbound Delivery with Order Reference screen displays. |  |
| 3 | Search Sales Order | On the Create Outbound Deliveries with Order Reference screen, make the following entries:Shipping Point: Shipping point, for example 331RSelection Date: current dateOrder: Return Order number created previously | The Delivery Create: Overview screen displays. |  |
| 4 | Choose Continue | Choose Continue. | The Returns Delivery Create: Overview screen displays. |  |
| 5 | Display Item Overview | On the Item Overview tab, make the following entries:SLoc: <Storage Location>, for example 333D |  |  |
| 6 | Confirm | Choose Save. | The following system message appears: Returns Delivery <Return delivery number> was saved and distributed to the WMS |  |

### Post Goods Receipt in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inbound delivery is used as a working object in the inbound delivery process.

You can use this document in delivery processing when executing the following actions:

- Registering the delivery in the yard
- Placing the delivery into stock
- Canceling the "delivery putaway"
- Adjusting the delivery quantity to the quantity posted in the goods receipt (in case of over delivery or under delivery).
- Adjusting the delivery quantity and the transferred quantity

|  |
| --- |
| Note In this case, the delivery quantity is adjusted to the quantity posted in the goods receipt. The quantity in the inbound delivery notification is also adjusted and a new inbound delivery is created. |

- Posting a goods movement
- Canceling a goods movement
- Creating items
- Deleting items

You can save, validate, and delete an inbound delivery.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/PRDI | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Delivery Processing > Inbound Delivery > Maintain Inbound Delivery |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Maintain Inbound Delivery screen appears. |  |
| 2 | Choose Default Values (F5). | On the Maintain Inbound Delivery screen, choose Default Values (F5). | The Maintain Inbound Delivery - Warehouse Number dialog box appears. |  |
| 3 | Check or make the following entries | In the Maintain Inbound Delivery - Warehouse Number dialog box, check or make the following entries:Warehouse No.:3330Goods Receipt Office:YWAREHOUSE-3330Ent. to Dispose:33413310 |  |  |
| 4 | Choose Continue (Enter) | Choose Continue (Enter). |  |  |
| 5 | Choose Find Purchase Order | On the Maintain Inbound Delivery screen, from the Find drop-down list choose ERP Document. |  |  |
| 6 | Enter purchase order number | Make the following entries:FindERP Document <your Return Delivery number> |  |  |
| 7 | Choose Perform Search | Choose Perform Search. | The following system message appears: One document was read.The Return Delivery (Original) appears in the table. |  |
| 8 | Select the Inbound Delivery. | In the List View, choose Inbound Delivery. |  |  |
| 9 | In the Inbound Delivery menu, choose Follow-On Functions > Pack . | In the Inbound Delivery menu, choose Follow-On Functions > Pack . | The Work Center Packing for Inbound Delivery screen appears. |  |
| 10 | On the Work Center Packing for Inbound Delivery screen, navigate to the Create HU tab | On the Work Center Packing for Inbound Delivery screen, navigate to the Create HU tab. |  |  |
| 11 | Enter packaging material | On the Create HU tab, make the following entries:Pack. Material: PMPAL00 |  |  |
| 12 | On the Create HU tab, choose Execute. | On the Create HU tab, choose Execute. | The following system message appears: HU <number> (PMPAL00) was constructed |  |
| 13 | Drag and Drop Inbound Delivery Item Node to HU Node. | On the Work Center Packing for Inbound Delivery screen in the tree area, drag the node with your product from the inbound delivery item. Drop it to the node with the HU number you created in the previous step. | The inbound delivery item is packed on the HU. |  |
| 14 | Choose Save and Go back. | Choose Save and go back. |  |  |
| 15 | On the Work Center Packing for Inbound Delivery screen, choose Goods Receipt. | On the Maintain Inbound Delivery screen, choose Goods Receipt. | The following system message appears:Inbound Delivery <number> changed.In the Document Flow tab in the document flow table, a new line with the document category Goods Receipt is added.On the Status tab, the Status Type Goods Receipt is set to completed. |  |

### Create Warehouse Tasks for Putaway in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create warehouse tasks manually using the user interface for Putaway for Inbound Delivery.

Procedure

| Transaction Code | SAP EWM Menu |
| --- | --- |
| /SCWM/TODLV_I | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Work Scheduling > Create Warehouse Task for Warehouse Request > Putaway for Inbound Delivery |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Create Warehouse Task - Warehouse Number Number - Putaway screen appears. |  |
| 2 | Choose Find Purchase Order | On the Create Warehouse Task - Warehouse Number <number> - Putaway screen, from the Find drop-down list choose DLVNO Warehouse Request. |  |  |
| 3 | Enter Inbound Delivery Number | Make the following entries:Find Warehouse Request <your Inbound Delivery Number from Step 4.3 Post Goods Receipt in SAP EWM> |  |  |
| 4 | Choose Perform Search. | Choose Perform Search. | The Warehouse Request appears in the table. |  |
| 5 | Select the Warehouse Request | On the Warehouse Request tab, choose Warehouse Request. |  |  |
| 6 | Choose Create + Save. | On the Warehouse Request tab, choose Create +Save. | The following system message appears:Number warehouse tasks were created |  |
| 7 | Note down the warehouse order | Note down the warehouse order for testing purposes. |  |  |

### Putaway of Products in SAP EWM

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can confirm and save all warehouse tasks in one go, in the background. If you want to change data, you can also confirm individual warehouse tasks manually and then save them, in other words, confirm the individual warehouse tasks in the foreground. The following procedure describes the manual confirmation in the foreground.

Procedure

| Transaction Code | /SCWM/TO_CONF |
| --- | --- |
| SAP EWM Menu | SAP Menu > SCM Extended Warehouse Management > Extended Warehouse Management > Execution > Confirm Warehouse Task |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access Transaction | Access the transaction using one of the navigation options above. | The Confirm Warehouse Task in Warehouse Number number screen appears. |  |
| 2 | Choose Find Warehouse Order | On the Confirm Warehouse Task in Warehouse Number number screen, from the Find drop-down list choose Warehouse Order. |  |  |
| 3 | Enter warehouse order number | Make the following entries:Find: Warehouse Order your warehouse order number |  |  |
| 4 | Choose Perform Search. | Choose Perform Search. | The following system message appears: Selection produced number resultsThe Warehouse Order appears. |  |
| 5 | Select the Warehouse Order. | In the List View, select Warehouse Order. |  |  |
| 6 | Choose Confirm in Foreground | Choose Confirm in Foreground. | The warehouse task(s) appears on the tab Product WT. |  |
| 7 | Navigate to the Product WT tab | Navigate to the Product WT tab. |  |  |
| 8 | Choose the warehouse task(s) | On the Product WT tab in the warehouse task table, choose the warehouse task(s). |  |  |
| 9 | Choose Confirm in Foreground | Choose Confirm in Foreground. | The WT Status is updated to Confirmed in Foreground. |  |
| 10 | Save your entries | Save your entries. | The following system message appears: Warehouse task warehouse task number was confirmed |  |

### Check Return Delivery (Optional)

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
| 1 | Log on | Open the SAP Fiori launchpad as a Shipping Specialist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose Display Outbound Delivery (VL03N). | The Display Outbound Delivery (VL03N) screen appears. |  |
| 3 | Enter Outbound Delivery | Make the following entries:Outbound Delivery: your return delivery number created in step 4.2 Create Return Delivery | The Delivery Overview screen displays. |  |
| 4 | Choose Continue | On the Display Outbound Delivery (VL03N) screen, choose Continue. | The Delivery number Display: Overview screen appears. |  |
| 5 | Navigate to the Status Overview tab | Navigate to the Status Overview tab. |  |  |
| 6 | Check that the Overall Goods Movement Status is C Completely processed. | In the Overall Status - Delivery table, check that the Overall Goods Movement Status is C Completely processed. |  |  |
| 7 | Check that the Goods Movement Status for the items is C Completely processed. | In the Delivery Item Status (All Items) table, check the Goods Movement Status for the items is C Completely processed. |  |  |
| 8 | Choose Document Flow. | On the Return Delivery <number> Display: Overview screen, choose Document Flow. | The Document Flow screen appears. |  |
| 9 | Note down the material document number for goods movement type TF SLoc to SLoc. | On the Document Flow screen in the Document column, note down the material document number for goods movement type TF SLoc to SLoc for testing purposes. |  |  |

### Check Material Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The check step to show you the material document in the SAP S/4HANA system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Open the SAP Fiori launchpad with the Inventory Manager role. | The SAP Fiori launchpad is displayed. |  |
| 2. | Access the App | Choose Material Documents Overview (F1077). | The Material Documents Overview (F1077) screen appears. |  |
| 3. | Change Settings | On the Material Documents Overview (F1077) screen in section Material Documents, choose Settings on the right-hand side. | The View Settings dialog box appears. |  |
| 4. | View Settings | In the View Settings dialog box, choose the column for Goods Movement Type. |  |  |
| 5. | Confirm | Choose OK. |  |  |
| 6. | Enter Selection Data | On top of the screen, make the following entries:Example:Stock Change: TRANSFER POSTINGStock Change Level: PlantPlant: 3310Material Document: Material Document Number from step Check Return Delivery |  |  |
| 7. | Check the Material Document | Choose Go. | Material documents are listed. |  |
| 8. | Check the Storage Location | In the Material Documents table, check that the Storage Location is EWM Int ROD333D. |  |  |
| 9. | Check the Goods Movement Type | In the Material Documents table, check that the Goods Movement Type is TF SLoc to SLoc (411). |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BDD - Lean Customer Returns | After completing the steps in this scope item, you can continue with the Remove Billing Block step from scope item Lean Customer Returns. |

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
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 28,705 chars in the whole document
