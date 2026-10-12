---
id: 11-inventory-warehouse-and-transportation/warehouse-kanban-supply-into-production-3vt-ae-test-script-977
title: Warehouse Kanban Supply into Production (3VT_AE) - Test Script (3VT_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3VT: Kanban replenishment from warehouse to production, with prerequisites, roles and test steps."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/ewm-production-integration]
aliases: [3VT_S4CLD2608_BPD_EN_AE]
keywords: [EWM Production Supply and Receipt, kanban replenishment, warehouse tasks, kanban control cycle, production supply area, set kanban status, radio frequency devices, fixed storage bins, business roles, test data prerequisites]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3VT_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-977
topic: 11-inventory-warehouse-and-transportation/ewm-production-integration
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Warehouse Kanban Supply into Production (3VT_AE) - Test Script (3VT_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3VT_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EWM Production Supply and Receipt** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Warehouse Kanban Supply into Production (3VT_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853797)

[2 Prerequisites 4](#_Toc232853798)

[2.1 System Access 4](#_Toc232853799)

[2.2 Roles 4](#_Toc232853800)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232853801)

[2.4 Business Conditions 6](#_Toc232853802)

[2.5 Preliminary Steps 7](#_Toc232853803)

[2.5.1 Define Default Values for Warehouse Clerk (EWM) 7](#_Toc232853804)

[2.5.2 Define Default Values for Warehouse Operative (EWM) 7](#_Toc232853805)

[2.5.3 Assign Fixed Storage Bins to Component 8](#_Toc232853806)

[2.5.4 Check Production Supply Area 9](#_Toc232853807)

[2.5.5 Control Cycle for Kanban: Stock Transfer 9](#_Toc232853808)

[2.5.5.1 Control Cycle for Inventory Managed PSA 10](#_Toc232853809)

[2.5.5.2 Control Cycle for Bin Managed PSA 11](#_Toc232853810)

[2.5.6 Create Initial Stock for Component 12](#_Toc232853811)

[3 Overview Table 13](#_Toc232853812)

[4 Test Procedure 14](#_Toc232853813)

[4.1 Set Kanban to EMPTY 14](#_Toc232853814)

[4.2 Option 1: Status Control in Warehouse 15](#_Toc232853815)

[4.2.1 Confirm Warehouse Task 15](#_Toc232853816)

[4.2.1.1 Variant 1: With Fiori App 15](#_Toc232853817)

[4.2.1.2 Variant 2: With Radio Frequency Device 16](#_Toc232853818)

[4.3 Option 2 : Status Control in production 18](#_Toc232853819)

[4.3.1 Set Kanban to FULL 18](#_Toc232853820)

[5 Appendix 20](#_Toc232853821)

[5.1 Process Integration 20](#_Toc232853822)

[5.1.1 Succeeding Process 20](#_Toc232853823)

## Purpose

Overview

This scope item allows you to replenish material from your warehouse to production. The process starts with a notification of the empty container status in the system. By setting the Kanban status to EMPTY, the system triggers the creation of a warehouse task. A warehouse operative picks the material from the replenishment storage type, moves it to the production supply area storage bin, and confirms the task in the system. The Kanban container status is automatically set to FULL. If the production supply area is not WM-managed, the stock transfer to the production storage location is executed immediately with the confirmation. This helps to keep the manual posting effort to a minimum.

Second option: On receipt of the material, the demand source can set the Kanban container status to FULL. The warehouse task is immediately confirmed and the stock transfer to the production storage location is triggered accordingly, if required.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions

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
| Production Supervisor - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV | Production Management - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV |  |
| Production Planner - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG | Production Planning - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG |  |
| Production Operator - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG | Production Execution - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG |  |
| Warehouse Clerk (EWM) | SAP_BR_WAREHOUSE_CLERK_EWM | Warehouse Office | SAP_BR_WAREHOUSE_CLERK_EWM |  |
| Warehouse Operative (EWM) | SAP_BR_WAREHOUSE_OPERATIVE_EWM | Warehouse Floor | SAP_BR_WAREHOUSE_OPERATIVE_EWM |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Material | RM233-1 |  |  |
| Packaging Material | PMPALLET |  |  |
| Packaging Material | PMPALLET_GTL | Pallet for GTL |  |
| Company Code | 3310 |  |  |
| Plant | 3310 |  |  |
| Storage Location | 335W |  | Warehouse |
| Storage Location | 331B |  | Production Storage Location |
| Production Supply Area | PSA_01 |  |  |

Organizational Master Data in Warehouse:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Warehouse | 3350 |  |  |
| Custodian | 33413310 |  |  |
| Entitled to Dispose | 33413310 |  |  |

Warehouse-Specific Master Data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Storage Type | SF01 | Fixed Bin Storage |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| 3KQ | Maintain Warehouse Products Attributes - MDS |
| 3KR | Maintain Storage Bins and Fixed Bin Assignments - MDS |
| 3KS | Maintain Production Supply Area - MDS |
| 40D | Create Production Supply Area - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting Period is up to date. |
| 4B4 - Material Replenishment with Kanban – Stock Transfer | Complete the following preliminary step:Create Queue for Kanban Card Printing (Optional). |
| 3BR - Warehouse Inbound Processing | You have completed the step described in the Warehouse Inbound Processing test script so that you have the stock to do the Kanban Supply. |

### Preliminary Steps

#### Define Default Values for Warehouse Clerk (EWM)

Purpose

In this step, you assign a default value, for example, the warehouse number for the Warehouse Clerk (EWM).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori Launchpad as Warehouse Clerk (EWM). |  |  |
| 2. | Choose the User Icon | Choose the Icon for the logon user.Select Settings. |  |  |
| 3. | Enter Default Value | Choose Default Values.Make the following entry in the section Material Management:Warehouse No. : 3350 .Choose Save. |  |  |

#### Define Default Values for Warehouse Operative (EWM)

Purpose

In this step, you assign a default value, for example, the warehouse number for the Warehouse Operative (EWM).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log onto SAP Fiori Launchpad | Open the SAP Fiori launchpad as Warehouse Operative (EWM). |  |  |
| 2. | Choose the User Icon | Choose the Icon for the logon user.Choose Settings |  |  |
| 3. | Enter Default Value | Choose Default Values and make the following entry in the section Material Management:Warehouse No. : 3350 .Choose Save. |  |  |

#### Assign Fixed Storage Bins to Component

Purpose

In this step, you assign fixed storage bins to products.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Warehouse Clerk (EWM). |  |  |
| 2 | Access App | Open Assign Fixed Bins (/SCWM/BINMAT). |  |  |
| 3 | Enter Data | On the Assign Fixed Storage Bins screen, enter the following data:Warehouse Number: 3350.Product: RM233-1.Choose Run. |  |  |
| 4 | Maintain Fixed Bin | Choose Edit to switch to change mode.Choose Append Row.Enter the following data:WhN: 3350Ent.toDisp: 33413310.Storage Bin: SF01-03-01Product: RM233-1.Choose Save. |  |  |

#### Check Production Supply Area

Purpose

In this step, you check the data in production supply area

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Production Planner - Lean Manufacturing. |  |  |
| 2 | Access App | Open Maintain Production Supply Area. |  |  |
| 3 | Enter Plant | On the Determine Work Area: Entry screen, make the following entry:Plant: 3310Choose Continue. |  |  |
| 4 | Choose PSA | Select the line for plant 3310 and production supply area PSA_01. Choose Details. |  |  |
| 5 | Check Data | Enter the following data:Storage Location: 331B.Responsible: 001.Choose Save. |  |  |
| 6 |  | Repeat steps 4 and 5 to check the Bin Managed Production Supply Area PSA_02, ensure that the Storage Location 335W is assigned. |  |  |

#### Control Cycle for Kanban: Stock Transfer

Purpose

In this activity, you create a control cycle for a classic kanban that can be used for direct stock transfer. In the control cycle, you define the demand source, the supply source, and the procedure that must be used to replenish the Kanban material. In the control cycle, you also define the number of kanbans that circulate between the supply source and the demand source, as well as the quantity a kanban contains.

##### Control Cycle for Inventory Managed PSA

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). | The Manage Kanban Control Cycles (PKMC) displays. |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Display/Change.Plant: 3310.Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the selection details | Make the following entries and choose Continue:Classic KANBAN: Selected.Material: RM233-1.Prodn Supply Area: PSA_01 .Storage Location 331B.Lifecycle Status: Released. | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Make the following entries:No. of Kanbans: 5.Maximum Empty: 2.Container Qty: 100.No. Load Carrier: 1.Replenishment Strategy: Select Stock Transfer: Enter the value PD80 and choose Enter.Storage Location: 335W.Source PSA: <Blank> .Source Bin: <Blank> .Whse Proc. Type: S201.Destination Bin: PROD-SUPPLY. |  |  |
| 6 | Save | Choose Save Control Cycle. | You have created a kanban control cycle for Material RM233-1. |  |

##### Control Cycle for Bin Managed PSA

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). | The Manage Kanban Control Cycles (PKMC) displays. |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Display/Change.Plant: 3310Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the selection details | Make the following entries and choose Continue:Classic KANBAN: Selected.Material: RM233-1.Prodn Supply Area: PSA_02 （storage location 335W).Lifecycle status: Released. | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Make the following entries:Destination Bin: PROD-SUPPLY-2.No. of Kanbans: 5.Maximum Empty: 2.Container Qty: 100.No. Load Carrier: 1.Replenishment Strategy: Select Stock Transfer: Enter the value PD80 and choose Enter.Storage Location: 335W.Source PSA: <Blank>.Source Bin: <Blank>.Whse Proc. Type: S201. |  |  |
| 6 | Save | Choose Save Control Cycle. | You have created a kanban control cycle for material RM233-1. |  |

#### Create Initial Stock for Component

Refer to scope item Warehouse Inbound Processing (3BR) to create initial stock for RM233-1 in the fixed storage bin SF01-03-01 of the 3350 warehouse.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App / Transaction | Expected Results |
| --- | --- | --- | --- |
| [Set Kanban to EMPTY](#unique_16) [page ] 14 | Production Operator - Lean Manufacturing | SAP Fiori App Display Kanbans: Demand View (PK13N). | When a Kanban container is set to Empty, one warehouse task for replenishment is created automatically. |
| [Confirm Warehouse Task](#unique_17) [page ] 15 | Warehouse Operative (EWM) | SAP Fiori App Process Warehouse Tasks (F4595) | After the warehouse task is confirmed, the stock is picked and transferred to the PSA bin.For the Inventory Managed Production Supply Area PSA_01, the goods issue is posted from the PSA bin to the production storage location 331B automatically.For the bin-managed Production Supply Area PSA_02, the stock stays in PSA bin PROD-SUPPLY-2 and is consumed from there.The Kanban status is set to Full automatically. |
| [Set Kanban to FULL](#unique_18) [page ] 18 | Production Operator - Lean Manufacturing | SAP Fiori App Display Kanbans: Demand View (PK13N). | The warehouse task for replenishment is confirmed automatically.The stock is picked and transferred to the PSA bin.For the Inventory Managed Production Supply Area PSA_01, the goods issue is posted from the PSA bin to the production storage location 331B automatically.For the bin-managed Production Supply Area PSA_02, the stock stays in PSA Bin PROD-SUPPLY-2 and is consumed from there. |

## Test Procedure

### Set Kanban to EMPTY

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you set an available Kanban to EMPTY to trigger a replenishment for material RM233-1.

Prerequisite

The Kanban control cycle for material RM233-1 is created and sufficient stock is available of material RM233-1 in storage location 335W.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Kanbans: Demand View (PK13N). | The Kanban Board: Demand Source View, Initial Screen displays. |  |
| 3 | Select the Kanban | Make following entries and choose Enter.Plant: 3310.Production Supply Area: PSA_01 or PSA_02.Note For staging to Inventory Managed PSA, choose PSA_01.For staging to Bin Managed PSA, choose PSA_02. | The Kanban Board: Demand Source View From XX:XX Time screen displays. |  |
| 4 | Set the Kanban to Empty | Mark one line of the Kanban for RM233-1 and choose Set to Empty. | When a Kanban container is set to Empty, one warehouse task for replenishment is created automatically. |  |
| 5 | Check the Kanban Information | Double-click the empty Kanban to display the replenishment warehouse task. |  |  |
| 6 | Exit | Choose Home. |  |  |

### Option 1: Status Control in Warehouse

#### Confirm Warehouse Task

##### Variant 1: With Fiori App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A pick list is printed and handed over to the Warehouse Operative (EWM), who performs the warehouse tasks and confirms them in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Warehouse Tasks(F4595). |  |  |
| 3 | Enter Warehouse Task Number | On the Process Warehouse Tasks screen, make the following entries:Warehouse Task: <WT number noted down in the previous step>.Choose Go. |  |  |
| 4 | Confirm Warehouse Task | Mark the checkbox for the selected warehouse task and choose Confirm. | After the warehouse task confirmation, the stock is picked and transferred to the PSA bin.For the inventory-managed production supply area PSA_01, the goods issue is posted from the PSA bin to the production storage location 171B automatically.For the bin-managed production supply area PSA_02, the stock stays in PSA bin PROD-SUPPLY-2 and is consumed from there.The kanban status is set to Full automatically. |  |

##### Variant 2: With Radio Frequency Device

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Warehouse Operative (EWM) performs the replenishment warehouse tasks and confirms them in the system with the mobile Radio Frequency device.

|  |
| --- |
| Note For Working with Mobile RF Devices, make sure all the steps as described in the Setup Instruction guide for scope item 63V - Mobile RF Devices in Warehousing have been performed. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on to the SAP Fiori launchpad | Log on to the SAP Fiori launchpad as a Warehouse Operative (EWM). | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open the SAP Fiori app Test RF Environment (/SCWM/RFUI)Note The app allows you to test working in an RF environment. For working with mobile RF devices, see also SAP Note [3048632](https://me.sap.com/notes/3048632). |  |  |
| 3 | Enter Data for RFUI | Whse No: 3350Resource: SHR1-1Dflt Dvc.: SE01Choose Enter. |  |  |
| 4 | Choose Menu | Choose 01 System-Guided > 02 SystemGuided Queue. |  |  |
| 5 | Enter Queue Name | In the Queue field, enter for example SR-F01-105Choose Enter |  |  |
| 6 | Create Picking HU | Make the following entries:Pack.Mat: PMPALLETChoose Handling.The picking HU is created. |  |  |
| 7 | Choose Next | Scroll the screen to right by using > and choose Next . |  |  |
| 8 | Enteror Verify the Source Information fields | Enter or Verify the following fields, if required:Src.Bin (Source Bin)SrceHU (Source HU)Prod. (Product)ActQty (Quantity)Choose Enter . |  |  |
| 9 | Verify the Destination information fields | Verify the following fields:DstBin (Destination Bin)Choose Enter |  |  |
| 10 | Repeat Steps | Repeat steps 6 to 9 until no suitable warehouse orders are found. |  |  |
| 11 | Logoff RFUI | You can choose Back to the previous screens.Choose Logoff.Choose Save. |  |  |

### Option 2 : Status Control in production

#### Set Kanban to FULL

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you change the status of the Kanban you processed in the previous step to FULL. This gets done when the material is delivered.

Prerequisite

The status of the Kanban is previously set to EMPTY.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Kanbans: Demand View (PK13N). | The Kanban Board: Demand Source View, Initial Screen displays. |  |
| 3 | Choose the Kanban | Make the following entries and choose Enter.Plant:3310.Production Supply Area: PSA_01 or PSA_02.Note Choose the same production supply area as selected in the previous step (Set Kanban to EMPTY). | The Kanban Board: Demand Source View From XX:XX Time screen displays. |  |
| 4 | Set the Kanban to Empty | Mark one line of the empty Kanban for RM233-1 and choose Set to Full. |  |  |
| 5 | Check the Kanban Information | Double-click the full Kanban to display the replenishment warehouse task. | The warehouse task for replenishment is confirmed automatically.The stock is picked and transferred to the PSA Bin.For the Inventory Managed Production Supply Area PSA_01, the goods issue is posted from the PSA Bin to the production storage location 331B automatically.For the Bin Managed Production Supply Area PSA_02, the stock stays in the PSA Bin PROD-SUPPLY-2 and gets consumed from there. |  |
| 6 | Exit | Choose Home. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Process

After completing the activities in this test script, you can continue testing the following business processes:

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
> Flagged while digesting this document, not verified: Variant 1 step 4 says goods issue posts to production storage location 171B, while the rest of the document uses 331B.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/atualizar-area-de-abastecimento-da-producao-mds-3ks-344]]
- related-to :: [[11-inventory-warehouse-and-transportation/maintain-production-supply-area-mds-3ks-341]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-343]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-3ks-345]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3VT_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 27,178 chars in the whole document
