---
id: 12-production-and-manufacturing/rework-processing-stock-manufactured-material-bjn-ae-test-script-1275
title: Rework Processing – Stock-Manufactured Material (BJN_AE) Test Script (BJN_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item BJN (AE): rework production order for stock-manufactured material, from order creation to goods receipt."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/rework-processing]
aliases: [BJN_S4CLD2608_BPD_EN_AE]
keywords: [Rework Processing, rework production order, goods issue, goods receipt, production confirmation, test scripts, production order release, manage production operations, goods movement slips, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJN_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1275
topic: 12-production-and-manufacturing/rework-processing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Rework Processing – Stock-Manufactured Material (BJN_AE) Test Script (BJN_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJN_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Rework Processing** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Rework Processing – Stock-Manufactured Material (BJN_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Rework Processing – Stock-Manufactured Material (BJN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861888)

[2 Prerequisites 4](#_Toc232861889)

[2.1 System Access 4](#_Toc232861890)

[2.2 Roles 4](#_Toc232861891)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232861892)

[2.4 Business Conditions 6](#_Toc232861893)

[2.5 Preliminary Steps 6](#_Toc232861894)

[2.5.1 Initial Stock Posting 6](#_Toc232861895)

[3 Overview Table 8](#_Toc232861896)

[4 Test Procedures 9](#_Toc232861897)

[4.1 Create Rework Production Order 9](#_Toc232861898)

[4.2 Release Rework Production Order 10](#_Toc232861899)

[4.3 Goods Issue for Defective Materials 11](#_Toc232861900)

[4.4 Preview Goods Issue Slip 12](#_Toc232861901)

[4.5 Confirmation of Rework Production Activities 13](#_Toc232861902)

[4.6 Manage Production Operations 15](#_Toc232861903)

[4.7 Post Goods Receipt for Rework Production Order 16](#_Toc232861904)

[4.8 Preview Goods Receipt Slip 17](#_Toc232861905)

[4.9 Review Manufacturing Object Pages 18](#_Toc232861906)

[5 Appendix 20](#_Toc232861907)

## Purpose

Overview

This scope item focuses on rework activities and material postings after production execution for the original material (including goods receipt for the product), with an additional rework production order. Issues with the produced material are monitored after it is posted to inventory.

The rework process of stock-manufactured materials begins with the creation of a new production order. This is done using the material to be reworked as both input and output.

Costs are listed in the new production order, and are settled within controlling as production variants. The input component and product have the same material number.

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
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data.

Manufacturing / Trading

Production Plant

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG126 | FIN126,MTS-DI,PD,Batch-Fifo,SerialNo |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Bill of Material | FG126 | FIN126,MTS-DI,PD,Batch-Fifo,SerialNo |  |
| Routing Group Counter 1 | 43310000 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |
| BNU - Create Costing Run - MDS | You have completed the steps described in the Create Costing Run - MDS (BNU) master data script. |

### Preliminary Steps

In this section, you are provided a detailed step-by-step description of technical or other prerequisites that are valid for all process step, report, or items.

#### Initial Stock Posting

Purpose

|  |
| --- |
| Note Initial stock posting is not required if you fulfilled one of the business conditions listed in the [Business Conditions](#unique_6) [page ] 6 section of this document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO) | The Goods Receipt Other - Your User name screen displays. |  |
| 3 | Enter Details | Select Goods Receipt and Other from the dropdown lists.Make the following entries and press Enter:On the Material tab: Material: FG126On the Quantity tab: Quantity : For example, 10On the Where tab:Movement Type: 561Plant: 3310Storage Location: 331A |  |  |
| 4 | Create Serial Numbers | Choose the Serial Numbers tab, and then set Auto-Create Serial Numbers. |  |  |
| 5 | Check | Select the Item OK indicator and choose Check. |  |  |
| 6 | Post | Choose Post and make a note of the material document number. |  |  |
| 7 | Execute Initial Stock Posting for Material RM20 | Repeat steps 1 to 5 with Material RM20.In the Storage Location field, enter 331C.You don't run the serial number check in step 4 for RM20. |  |  |

## Overview Table

The scope item Rework Processing – Stock-Manufactured Material consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Create Rework Production Order](#unique_10) [page ] 9 | Production Supervisor - Discrete Manufacturing | Create Production Order (CO01) | Rework production order is created |
| [Release Rework Production Order](#unique_11) [page ] 10 | Production Supervisor - Discrete Manufacturing | Change Production Order (CO02) | Rework production order is released |
| [Goods Issue for Defective Materials](#unique_12) [page ] 11 | Warehouse Clerk | Post Goods Movement (MIGO) | Material document created, costs of material value transferred to production order |
| [Preview Goods Issue Slip](#unique_13) [page ] 12 | Warehouse Clerk | Material Documents Overview (F1077) | Goods Issue Slip opens as a PDF |
| [Confirmation of Rework Production Activities](#unique_14) [page ] 13 | Production Supervisor - Discrete Manufacturing | Confirm Production Operation (F3069) | Final confirmation of rework operation |
| [Manage Production Operations](#unique_15) [page ] 15 | Production Supervisor - Discrete Manufacturing | Manage Production Operations (F2335) | Order confirmations are reviewed |
| [Post Goods Receipt for Rework Production Order](#unique_16) [page ] 16 | Warehouse Clerk | Post Goods Movement (MIGO) | Product FG126 is posted into inventory |
| [Preview Goods Receipt Slip](#unique_17) [page ] 17 | Warehouse Clerk | Material Documents Overview (F1077) | The Material Document screen displays. |
| [Review Manufacturing Object Pages](#unique_18) [page ] 18 | Production Planner | Search |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Rework Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the manufacturing staff reworks the manufactured material from stock.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Production Order (CO01). | The Production Order Create: Initial Screen displays. |  |
| 3 | Enter the Order Information | Make the following entries and press Enter:Materials : FG126Production Plant : 3310Order Type: YBW1 | The Production Order Create: Header screen displays. |  |
| 4 | Enter the Order Details | Make the following entries and press Enter:Quantity : <Quantity>End Date: <Date>, for example, Today's date +2 Days | The Select Production Version for Material and Plant dialog box displays. |  |
| 5 | Select the Production Version | Select the Production Version 0099 line and select Choose. |  |  |
| 6 | Save | Choose Save and make a note of your production order number. |  |  |

### Release Rework Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to release the production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Production Order (CO02). | The Production Order Change: Initial Screen displays. |  |
| 3 | Enter relevant search criteria | Make the following entries and press Enter:Order: <Order Number from the previous step>, for example, 60000XX | The Production Order Change: Header screen displays. |  |
| 4 | Release the Production Order | Choose Release Order (Ctrl +F1). |  |  |
| 5 | Save | Choose Save. |  |  |

### Goods Issue for Defective Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the system performs a goods issue for the defective material that must be reworked.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Issue Order - Your User name screen displays. |  |
| 3 | Enter Details | Make the following entries:Trans./Event: Goods IssueReference Document: OrderOrder Number: <XXXX> (from previous steps)Movement Type: 261Expand Head.data area, and make the following entries:Print via Output Control (Checkbox next to printer icon): <Select>Print Version of GR/GI Slip: Individual SlipPress Enter. |  |  |
| 4 | Review the Details | Choose the Where tab and check the following settings:Plant: 3310Storage Location: 331A |  |  |
| 5 | Enter the Serial Number | Choose the Serial Numbers tab, choose the find button (magnifier icon), and the Display Material Serial Number: Serial Number Selection screen displays. Then choose Execute.The Display Material Serial Number: Serial Number List screen displays, select the rows with the same number of production order quantity. Then select Choose.Then the Goods Issue Order screen displays with the filled Serial Number. |  |  |
| 6 | Post | Set Item OK indicator and choose Post. | Material document XXX is posted. |  |

### Preview Goods Issue Slip

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
| 2 | Access the App | Open Material Documents Overview (F1077). |  |  |
| 3 | Search for Goods Receipts Material Document | Make the following entries:Plant: 3310Material Document: <Material document number>, from the previous procedure and choose Go. | The relevant Material Document item displays. |  |
| 4 | Select Material Document for Goods Receipt | Select the row to view the material documents. | The Material Document view displays. |  |
| 5 | Review Goods Issue Details | Review the information for General Information, Attachment, Items and Process Flow. | In the General Information section, Posting Date and Document Date display. |  |
| 6 | Select the Material Document Item | In the Items section, select the row of material document item to preview. | The Material Document Item view displays. |  |
| 7 | Preview the Material Document Goods Receipt Slip | In the Output Management section, choose the Settings icon and ensure all columns are selected in Columns tab.Choose the Display Document icon for the item with Output Type as GOODS_ISSUE_SLIP. | The Goods Issue Slip displays in PDF format. |  |
| 8 | Back to Launchpad | Choose Home to return to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

### Confirmation of Rework Production Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to execute and record confirmations of all rework activities of the rework production order before posting the goods receipt in usual business practice.

Prerequisite

The goods issue for the defective material has been completed in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Perform Work screen displays. |  |
| 3 | Enter Production Order and Operation | On the Perform Work screen, make the following entries and choose Enter:Order: 60000XX (from the previous step)Operation: 0010 |  |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, make the following entries:Yield: <Quantity - the quantity you want to confirm>Scrap: <Quantity - the quantity that cannot be reworked> |  |  |
| 5 | Post Additional Goods Movements | In the Material Movements section, choose Add Material. | The Add Material screen display.Only when you need additional goods issue posting in your rework process, you need proceed with these next two steps. If you have no additional goods issues posting, continue with step 7. |  |
| 6 | Enter Goods Movement Details | Make the following entries and choose Add:Material: RAW MATERIAL, for example, RM20Plant: 3310Storage Location: 331CQuantity to be Posted: 3UoM: PC |  |  |
| 7 | Enter Fields in Activities Section | In the Activities section, make the following entries:Setup: <enter the setup time you want to confirm for this operation>Labor: <enter the labor time you want to confirm for this operation > |  |  |
| 8 | Save Your Entries | Choose Post and Complete to make final confirmation for this operation. | Confirmation has been created. |  |

### Manage Production Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to display and check the order using the Manage Production Operations (F2335) app for Finished Good Made To Stock (FG126) after the release/confirm of finished goods orders is performed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Operations (F2335) | The Manage Production Operations (F2335) screen displays. |  |
| 3 | Select Production Order | On the Manage Production Operations (F2335) screen, enter the following search condition as filter.To review the Default Area of Responsibility (supervisor), select the user from the top left of the App Settings Area of Responsibility Production Supervisor screen and ensure only the following displays:Plant: 3310MTS DI - Valuated (YB1)Select Adapt Filters to display more selection filters. Select the checkbox for Material and Plant, and choose OK.Result: Material and Plant fields are then added to filter bar.Status: ConfirmedMaterial: FG126Plant: 3310 (Production plant)Choose Go to execute. | Selected order displays. |  |
| 4 | Check Detailed Operations Status | Check detailed information for selected production operations.Operation Issues:Empty if there is no issue for production order.Delay/Missing Components/PRT issue/Quantity Deviation/Quality Issue information displays when relevant issues exist.Components:Material, total quantity and Issued/open quantity information for order components displays.Order Schedule:Detailed operation information with relevant work center, confirmed quantity, start/end time displays.Work Center Schedule:The relevant order covering the same work center capacity (operation is partially confirmed) displays.Confirmation:Detailed confirmation information with Yield, Scrap & Rework quantity displays when confirmation is executed.Inspection:Detailed inspection lots information displays when available. | Detailed operations status displays. |  |

### Post Goods Receipt for Rework Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the rework production order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Goods Receipt Order - Your User name screen displays. |  |
| 3 | Enter Details | Make the following entries and press Enter:Trans./Event: Goods ReceiptReference Document: OrderOrder Number: <XXXX> (Rework Production Order Number from previous step)Make the following entries and press Enter again:Movement Type: 101Plant: 3310Storage Location: 331ANote Choose the Serial Numbers tab, and ensure the amount of Serial Numbers is the same quantity as the confirmed yield quantity in final operation.If the quantity of listed serial numbers exceed, then delete certain rows.Choose Head.data, and make the following entries:Print via Output Control (Checkbox next to the printer icon): <Select>Print Version of GR/GI Slip: Individual Slip |  |  |
| 4 | OK Item and Check | Select the Item OK checkbox and choose Check. |  |  |
| 5 | Post | Choose Post. | Material document XXX is posted. |  |

### Preview Goods Receipt Slip

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
| 2 | Access the App | Open Material Documents Overview (F1077). |  |  |
| 3 | Search for Goods Receipts Material Document | Make the following entries and choose Go.Plant: 3310Material Document: <Material document number> (you created in the in previous procedure) | The relevant Material Document item displays. |  |
| 4 | Select Material Document for Goods Receipt | Select the row for which you would like to see the material documents. | The Material Document view displays. |  |
| 5 | Review Goods Receipt Details | Review the information for General Information, Attachment, Items and Process Flow. | In the General Information section, you see Posting Date and Document Date |  |
| 6 | Select the Material Document Item | In the Items section, select the row of material document item that you want to preview. | The Material Document Item screen displays. |  |
| 7 | Preview the Material Document Goods Receipt Slip | In the Output Management section, choose the Settings icon and ensure all columns are selected in the Columns tab.Choose Display Document icon for the item with Output Type as GOODS_RECEIPT_ORD_SLIP. | The Goods Receipt Slip opens in a PDF format. |  |
| 8 | Back to Launchpad | Choose Home to go back to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

### Review Manufacturing Object Pages

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the different objects pages available for different roles in the area of manufacturing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner.Note You can use any role in the Roles section above. | The SAP Fiori launchpad displays. |  |
| 2 | Start Search | Choose Search in the upper right area of the launchpad. | An input field displays. |  |
| 3 | Search Criteria | Make the following entries and choose Search:Products: Material (see the Master Data section) | The system displays a list of objects that use the selected material. |  |
| 4 | Display Object | In the All field, choose Down arrow.Select an object and choose Search. | The list of objects is limited to the object type selected. If no object is selected, a message is displayed instead. |  |
| 5 | Tailor the Result Display | Below the search line, choose a symbol (for example, filter, display as table, sort) to filter the results list. | The results list is filtered according to your selections. |  |
| 6 | Repeat Steps | Repeat steps 1-5 for any other role in this test script and any other object offered in the search function. | The list of objects offered for search differs by the role you used to log on. |  |

## Appendix

Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3F0 - Event-Based Production Cost Posting (Optional) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

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
- related-to :: [[12-production-and-manufacturing/test-script-rework-processing-work-in-process-bjq-ae-1276]]
- related-to :: [[12-production-and-manufacturing/test-script-rework-with-quality-management-consumer-products-6a9-ae-11]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJN_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 31,264 chars in the whole document
