---
id: 12-production-and-manufacturing/test-script-material-replenishment-with-kanban-stock-transfer-4b4-ae-s
title: "Test Script: Material Replenishment with Kanban – Stock Transfer (4B4_AE), SAP S/4HANA Cloud Public Edition (4B4_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud 2608 (AE) test script for scope item 4B4: classic and one-card Kanban stock-transfer replenishment, roles, master data, control cycles."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/kanban-in-house-production]
aliases: [4B4_S4CLD2608_BPD_EN_AE]
keywords: ["Kanban Replenishment (In-House Production, External…", kanban replenishment, kanban control cycles, classic kanban, one-card kanban, kanban container status, kanban board, stock transfer strategies, kanban analysis, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B4_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1017
topic: 12-production-and-manufacturing/kanban-in-house-production
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Material Replenishment with Kanban – Stock Transfer (4B4_AE), SAP S/4HANA Cloud Public Edition (4B4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Kanban Replenishment (In-House Production, External Procurement, Stock Transfer)** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Material Replenishment with Kanban – Stock Transfer (4B4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854862)

[2 Prerequisites 4](#_Toc232854863)

[2.1 System Access 4](#_Toc232854864)

[2.2 Roles 4](#_Toc232854865)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232854866)

[2.4 Business Conditions 6](#_Toc232854867)

[2.5 Preliminary Steps 7](#_Toc232854868)

[2.5.1 Check Configuration - Define Stock Transfer Strategies (Optional) 7](#_Toc232854869)

[2.5.2 Create Control Cycle 8](#_Toc232854870)

[2.5.2.1 Control Cycle for Classic Kanban: Stock Transfer 8](#_Toc232854871)

[2.5.2.2 Control Cycle for One-Card Kanban with Trigger Quantity 9](#_Toc232854872)

[2.5.3 Initialize Material Stock 10](#_Toc232854873)

[3 Overview Table 12](#_Toc232854874)

[4 Test Procedures 13](#_Toc232854875)

[4.1 Production-Supply by Changing Kanban Container Status and Using Kanban Board 13](#_Toc232854876)

[4.1.1 Classic Kanban: Stock Transfer 13](#_Toc232854877)

[4.1.1.1 Set Available Kanban to EMPTY 13](#_Toc232854878)

[4.1.1.2 Change the Kanban to FULL 15](#_Toc232854879)

[4.1.1.3 Withdraw Quantity (Optional) 16](#_Toc232854880)

[4.1.2 One-Card Kanban Procedure with Trigger Quantity 17](#_Toc232854881)

[4.1.2.1 Start with a Full Container 18](#_Toc232854882)

[4.1.2.2 Withdraw Current Container till Trigger Quantity 19](#_Toc232854883)

[4.1.2.3 New Container Arrives 20](#_Toc232854884)

[4.1.2.4 Withdraw Current Container till Empty 21](#_Toc232854885)

[4.1.3 Kanban Control Cycles Analysis (Optional) 23](#_Toc232854886)

[4.1.4 Monitor Replenishment Situation (Optional) 24](#_Toc232854887)

[4.2 Review Manufacturing Object Pages 25](#_Toc232854888)

[5 Appendix 27](#_Toc232854889)

[5.1 Process Integration 27](#_Toc232854890)

[5.2 Kanban Status - Status Change/Kanban Signal 27](#_Toc232854891)

[5.2.1 Classification of the Processing Status of Kanban Container 27](#_Toc232854892)

## Purpose

Overview

The Kanban method for controlling production and material flow is based on the actual stock quantity in production. With Kanban, instead of being pushed through production by higher-level planning, materials are called from the supply source by production at the manufacturing level where they’re needed (pull principle). Replenishment or production of a material is only triggered when a higher production level requires the material. This replenishment is triggered directly in production using previously maintained master data.

Kanban replenishment is commonly used in – but not restricted to – repetitive manufacturing environments, when a production process requires that the same or similar products are produced over a certain period at a certain rate per period. The products produced always follow the same sequence through the machines and work centers in production. Routings tend to be simple and don’t vary much.

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
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV | Production Management - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV |  |
| Production Planner - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG | Production Planning - Lean Manufacturing | SAP_BR_PRODN_PLNR_LEAN_MFG |  |
| Production Operator - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV | Production Execution - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV |  |
| Production Operator - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG | Production Execution - Lean Manufacturing | SAP_BR_PRODN_OPTR_LEAN_MFG |  |
| Production Supervisor - Lean Manufacturing | SAP_BR_PRODN_SUPVR_LEAN_MFG | Production Supervision - Lean Manufacturing | SAP_BR_PRODN_SUPVR_LEAN_MFG |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | RM233-1 | RAW233-1, PD, KANBAN Stock TransferDemo material for Classic Kanban - Stock Transfer |  |
| Material | RM233-6 | RAW233-6, PD, One-Card KanbanDemo material for One-Card Kanban process |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Production Supply Area | KANBAN_03 | 331B is assigned. |  |

For more information about creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNE | Create Supplier Master - MDS |
| 40D | Create Production Supply Area - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Test Script Standard Cost Calculation (BEG). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

This Business Process Documentation contains process steps that must be completed before you can start to work through the standard Business Process Documentation of selected logistics scenarios.

#### Check Configuration - Define Stock Transfer Strategies (Optional)

Purpose

The necessary customizing settings to run through some basic scenarios have already been created as preconfigured SAP Best Practice content. You can check detailed entries through available Self-Service Configuration UI (SSCUI). For demonstration of SAP Best Practice scope item, you may not be able to adapt pre-configured SAP Best Practice content. If necessary, you can create your own entries according to your business requirement.

| Key of Pre-delivered Replenishment Strategy | Description | Comments |
| --- | --- | --- |
| PD03 | Reservation (MRP) |  |
| PD10 | Reservation |  |
| PD80 | Warehouse Task | Available if EWM relevant scenario (3VT) is enabled. |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

In the SAP S/4HANA Cloud Public Edition system, in the SAP Fiori launchpad, open Manage Your Solution (F1241) app using the business role SAP_BR_BPC_EXPERT and go to Configure your Solution.

In the Application Area listbox, select Manufacturing.

In the Sub Application Area listbox, select Kanban.

In Item Name, select Replenishment Strategies.

Choose Define Stock Transfer Strategies (ID: 103917).

Choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. Search for the configuration activity Define Stock Transfer Strategies and navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

#### Create Control Cycle

##### Control Cycle for Classic Kanban: Stock Transfer

Purpose

In this step, you create a control cycle for classic Kanban that can be used for direct stock transfer. In the control cycle, you define the demand source, the supply source and the procedure that must be used to replenish the Kanban material. You also define the number of Kanbans that circulate among the supply source and the demand source, as well as the quantity a Kanban contains.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). |  |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Edit.Plant: 3310Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the Selection Details | Make the following entries and choose Continue:Classic KANBAN: SelectedMaterial: RM233-1Supply Area: KANBAN_03Lifecycle status: Released | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Make the following entries:Number of Containers: 5Container quantity: 100Maximum Empty Containers: 2Number of Load Carriers: 1Go to the next part and in Replenishment Strategy tab, select Stock Transfer, enter PD03 and choose Enter.Storage Location: 331C |  |  |
| 6 | Save | Choose Save Control Cycle. | You have created a Kanban control cycle for material RM233-1 . |  |

##### Control Cycle for One-Card Kanban with Trigger Quantity

Purpose

In this step, you create a control cycle for One-Card Kanban process with trigger quantity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). |  |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Edit.Plant: 3310Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the Selection Details | Make the following entries and choose Continue:Classic KANBAN: SelectedMaterial: RM233-6Supply Area: KANBAN_03Lifecycle status: Released | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Make the following entries:Number of Containers: 2Container Quantity: 15Go to the next part. On the Replenishment Strategy tab, select Stock Transfer, enter PD03 and choose Enter.Storage Location: 331C |  |  |
| 6 | Enter Trigger Replenish-ment | On the Flow Control tab, make the following entries and choose Enter:Trigger Replenishment: 3 (At trigger quantity)Trigger Quantity: 5 |  |  |
| 7 | Save | Choose Save Control Cycle. | You have created a Kanban control cycle for material RM233-6. |  |

#### Initialize Material Stock

Purpose

This step describes standard purchasing process. But in real business cases, raw materials are usually purchased from external vendors.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock (F1062). screen displays. |  |
| 3 | Input Material | Make the following entries and press Enter:Material: RM233-1Plant: Plant 1 AE 3310 | The stock overview for the material displays. |  |
| 4 | Select Stock | Select the icon next to the stock where you want to add initial stock.For example:Storage Location:331Cfor RM233-1Unrestricted Use Stock | In a dialog box, the Storage Location, Stock Type and Current Quantity fields display per your entries in previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <Today>Posting Date: <Today>Stock Change: Initial EntryQuantity: <Enter a quantity> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |
| 6 | Repeat | Repeat step 3-5 for material RM233-6. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APPs | Expected Results |
| --- | --- | --- | --- |
| [Production-Supply by Changing Kanban Container Status and Using Kanban Board](#unique_14) [page ] 13 |  |  |  |
| [Classic Kanban: Stock Transfer](#unique_15) [page ] 13 |  |  |  |
| [Set Available Kanban to EMPTY](#unique_16) [page ] 13 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| [Change the Kanban to FULL](#unique_17) [page ] 15 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| [Withdraw Quantity (Optional)](#unique_18) [page ] 16 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| [One-Card Kanban Procedure with Trigger Quantity](#unique_19) [page ] 17 |  |  |  |
| [Start with a Full Container](#unique_20) [page ] 18 | Production Operator - Lean Manufacturing | Kanban Board (F4630) |  |
| [Withdraw Current Container till Trigger Quantity](#unique_21) [page ] 19 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| [New Container Arrives](#unique_22) [page ] 20 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| [Withdraw Current Container till Empty](#unique_23) [page ] 21 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| [Kanban Control Cycles Analysis (Optional)](#unique_24) [page ] 23 | Production Supervisor - Lean Manufacturing | Kanban Control Cycles Analysis (F5235) |  |
| [Monitor Replenishment Situation (Optional)](#unique_25) [page ] 24 | Production Supervisor - Lean Manufacturing | Kanban Board (F4630) |  |
| [Review Manufacturing Object Pages](#unique_26) [page ] 25 | Production Planner | Search |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Production-Supply by Changing Kanban Container Status and Using Kanban Board

Kanban board is one of the tools that can be used to change the container status, which can provide both demand source (consumer) and supply source (supplier, producer) with a detailed overview of Kanban circulation. In addition, Material Replenishment could be quickly triggered by setting Kanban container status.

#### Classic Kanban: Stock Transfer

If you want to transfer components with a previous reservation, you can use this function. When the Kanban is set to status Empty, it automatically triggers a reservation for material RM233-1.

##### Set Available Kanban to EMPTY

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set an available Kanban to EMPTY to trigger a reservation for material RM233-1 .

Prerequisite

The Kanban control cycle for material RM233-1 is created and sufficient stock is available of material RM233-1 in storage location 331C.

Procedure

It is possible to change status of Kanban Container with various Fiori apps. You can choose one of them to execute the task in this step (set to EMPTY) and subsequent steps (for example, set to FULL) where applicable. Here we provide two options you can leverage, and you can choose either of them.

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | Select a Kanban container on the left part of the screen. Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_03From the Items list, choose one of the Kanban for RM233-1 with Current Status of either WAIT or FULL. | The Kanban you entered displays. |  |
| 4 | Check Kanban Information | On the right part of the screen, check the following entry:Target Status: EMPTY |  |  |
| 5 | Set the Kanban to Empty | On the left part of the screen, choose Save at the bottom. | Setting an available KANBAN to empty results in a reservation for the material. |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Board (F4630).Note You can find the app under category Production Control - Kanban Monitoring. |  |  |
| 3 | Search | Make following entries and choose Go:Plant: 3310Production Supply Area: KANBAN_03Material: RM233-1 |  |  |
| 4 | Select Kanban Container | In the Control Cycle, choose Kanban Container with WAIT or FULL status. You can check the legend for description of visual elements.Container Details panel displays on the right side.You can check detailed information. |  |  |
| 5 | Set the Kanban to Empty | Choose Set to EMPTY above the list. |  |  |

##### Change the Kanban to FULL

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you change the status of the Kanban you processed in the previous step to FULL. This will be done when the material is delivered.

Prerequisite

The status of the Kanban is previously set to EMPTY.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | Select a Kanban container on the left part of the screen. Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make the following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_03From the Items list, choose one of the Kanban for RM233-1 with Current Status: EMPTY. | The Kanban you entered displays. |  |
| 4 | Check Kanban Information | On the right part of the screen, check the following entry:Target Status: FULL |  |  |
| 5 | Set the Kanban to Full | On the left part of the screen, choose Save at the bottom. |  |  |

##### Withdraw Quantity (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can withdraw a partial or the complete quantity of a material from a kanban container.

Prerequisite

The kanban container is previously set to status Full or In Use.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | Select a kanban container on the left part of the screen. Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make the following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_03From the Items list, choose the kanban container for RM233-1 you want to withdraw quantity. | The Kanban you entered displays. |  |
| 4 | Input Withdraw Quantity | On the right part of the screen, make the following entries and press Enter:Kanban Action: Withdraw QuantityWithdraw Quantity: <for example, 10>Note The Withdraw Quantity can only be the defined with the value of Container Quantity or less. Based on the former used demo data, the Withdraw Quantity can be set to 50 or less. | In case the default status sequence is used, if partial quantity is withdrawn, the Target Status will be changed to IN USE; If complete quantity is withdrawn, the Target Status will be changed to EMPTY. |  |
| 5 | Save | On the left part of the screen, choose Save at the bottom. |  |  |

#### One-Card Kanban Procedure with Trigger Quantity

The process demonstrates one kind of One-Card Kanban procedure, using two kanban containers in a control cycle with trigger quantity. This process starts with one full container, in which the material quantity can be withdrawn based on actual consumption. When the remaining material reaches or exceeds the trigger quantity, the second Kanban container would be set to status Empty automatically, thus triggering replenishment. The new kanban container then arrives before the current container has been completely emptied.

During this procedure, you can always check Kanban status using app Kanban Board.

##### Start with a Full Container

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is a prepation step to start One-Card Kanban procedure. The two Kanban containers both have initial status Wait after control cycle creation. We will set one of them as status Full.

Prerequisite

The Kanban control cycle for material RM233-6 is properly maintained and sufficient stock is available in storage location 331C.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Board (F4630).You can find the app under category Production Control - Kanban Monitoring. |  |  |
| 3 | Search | Make following entries and choose Go:Plant: 3310Production Supply Area: KANBAN_03Material: RM233-6 |  |  |
| 4 | Select Kanban Container | In the Control Cycle, 2 kanban containers both have initial status WAIT. Choose one of them as current container to start. | Mark both container IDs for further use. |  |
| 5 | Set the Kanban to Empty | Choose Set to EMPTY above the list. |  |  |
| 6 | Set the Kanban to Full | Select the same container, and choose Set to FULL above the list. | Now in the control cycle, you have one container with status Full (current container) and another Wait. |  |

##### Withdraw Current Container till Trigger Quantity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You now start One-Card Kanban circulation with the current container as status Full. In this step, you withdraw quantity of material from the current container based on real consumption. When the remaining quantity reaches or smaller than trigger quantity maintained in the control cycle, the other kanban container would be set to status Empty automatically, thus trigger replenishment.

Prerequisite

The current kanban container is previously set to status Full, or falls into status In Use during consumption.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select current Kanban Container | Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_03Material: RM233-6From the Items list, choose current kanban container which is under consumption. | The Kanban container displays. |  |
| 4 | Input withdrawl quantity | On the right part of the screen, make the following entry and press Enter:Kanban Action: Withdraw QuantityWithdrawl Quantity: 10Note For test purpose, we entered this elaborated quantity at one time manually. In real case, there could be multiple inputs with a smaller quantity entered each time, espe-cially when you use a scanning device. | If you follow exact number settings we described in this document, the full container quantity is 15, and trigger quantity is 5. So if you withdraw 10 or more than 10 pieces out from the full container, the trigger quantity will be reached and another container would be set to status Empty. |  |
| 5 | Save | On the left part of the screen, choose Save at the bottom. | The second kanban container is set to status Empty. |  |

##### New Container Arrives

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Change the second kanban container to status Full when it arrives.

Prerequisite

The second kanban container is previously set to status Empty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the second Kanban Container | Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_03Material: RM233-6From the Items list, choose the second kanban container. | Kanban container displays. |  |
| 4 | Change Status | On the right part of the screen, make the following entry:Kanban Action: Change StatusTarget Status: FULL |  |  |
| 5 | Save | On the left part of the screen, choose Save at the bottom. | The second kanban container is set to status Full. |  |

##### Withdraw Current Container till Empty

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you continuously withdraw quantity of material from current kanban container until it gets empty completely.

Prerequisite

The current kanban container is in status In Use.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select current Kanban Container | Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_03Material: RM233-6From the Items list, choose current kanban container. | The Kanban you entered displays. |  |
| 4 | Input Withdraw Quantity | On the right part of the screen, make the following entry and press Enter:Kanban Action: Withdraw QuantityWithdraw Quantity: 5, to make the Remaining Quantity equals to zero. |  |  |
| 5 | Save | On the left part of the screen, choose Save at the bottom. | The kanban container currently in use is set to status Wait. |  |

Result

Now in the control cycle, you will again have one kanban container with status Full and another Wait. Again, you start with the full container and withdraw quantity from it, thus repeat the One-Card Kanban procedure.

#### Kanban Control Cycles Analysis (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can evaluate your kanban control cycles with the flexibility in selection, aggregation and visualization. You can first get insights into the overall kanban replenishment situation at the aggregated level, and then drill-down to the details by selecting the dimensions and measures of your interest. This enables you to identify critical situations early and quickly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Control Cycles Analysis (F5235). |  |  |
| 3 | Filter | Filter by dimensions like plant, production supply area, material, and others. For example:Plant: 3310Choose Go. | Under default layout, the stacked chart will illustrate the percentage of kanban container distribution for each status. In the table, the kanban control cycles are displayed with their number of containers, number of empty containers, and number of containers with error. |  |
| 4 | View Mode | On the upper right part of the screen, you can toggle between different view modes by selecting different icons:Chart and Table ViewChart ViewTable View |  |  |
| 5 | View Settings | Choose Settings icon to open View Settings window.You can check and adjust how the Dimensions and Measures are shown in this analysis app. |  |  |
| 6 | Navigate | You can explore the app with rich set of visualization elements (a range of chart types, drill down, and so on) to better evaluate your kanban control cycle situation.Note In the upper left corner, you can take advantage of preset view varaints from the dropdown list. You can create and manage views under My Views. |  |  |

#### Monitor Replenishment Situation (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You may need to monitor the replenishment situation during the whole process. The kanban board is a tool for monitoring circulating kanban containers and evaluations, providing an overview of work progress and material consumption. The status of the kanban containers and the error situations are represented by different colors. You can also use the kanban board to trigger the kanban signal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Board (F4630).Note You can find the app under category Production Control - Kanban Monitoring. |  |  |
| 3 | Search | You can restrict selection by certain search criteria. Make following entries and choose Go:Plant: 3310Production Supply Area: <Production Supply Area>Material: <Material> |  |  |
| 4 | Check Kanban Container | The kanban containers are represented in different colors according to their status. Choose one Kanban Container. | The Container Details panel displays at the right side where you can check detailed information. |  |
| 5 | Kanban Correction | If the desired status change results in an error, the error message is displayed in the details panel of the kanban container. You can use the Correct Kanban app to correct the Kanban Container with ERROR status. |  |  |

### Review Manufacturing Object Pages

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review different object pages available for different roles in Manufacturing area.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner.Note You can use any role in section [Roles](#unique_4) [page ] 4 above. | The SAP Fiori launchpad displays. |  |
| 2 | Start Search | Choose Search in the upper right part of the screen. | An input field displays. |  |
| 3 | Search Criteria | Make the following entries and choose Search:BOM Header Material: <Material> (refer to section Master Data, Organizational Data, and Other Data) | The system displays a list of objects using the selected material. |  |
| 4 | Display Object | In the All field, choose Down arrow.Select an object and choose Search. | The displaying list of objects is limited to the object type selected. If no object is selected, a message would display instead. |  |
| 5 | Tailor the Result Display | Under the search line, choose an icon (for example, filter, display as table, sort and so on) to filter the results list. | The results list is filtered according to your selections. |  |
| 6 | Repeat Steps | Repeat steps 1 to 5 for any other role in this test script and any other object offered in the search function. | The result list of objects displayed differs by the role you use to log on. |  |

## Appendix

### Process Integration

For the complete production process, you can refer to corresponding business processes mentioned in below test script depending on your production environment:

BJH: Make-to-Stock Production – Repetitive Manufacturing

BJ5: Make-to-Stock Production – Discrete Manufacturing

### Kanban Status - Status Change/Kanban Signal

#### Classification of the Processing Status of Kanban Container

The course of Kanban Container processing is controlled and made visible through setting the Kanban Containers to appropriate status. Usually, only the statuses "Empty" and "Full" are used. As a rule, if a material in a Kanban Container has been used and a Kanban Container is then set to "Empty", this Kanban Container status automatically triggers the replenishment process. The source of supply (producer, supplier) receives the signal to fill up the Kanban Container again. When the full Kanban Container arrives back at the demand source (the consumer), the latter sets the Kanban Container to the status "Full" and the goods receipt is posted for the material. Normally, Kanban Container is possible with both statuses "Empty" and "Full".

| Status - Description | Business Condition |
| --- | --- |
| Waiting - 1 | Indicates that although the material has been consumed, the supply source is not yet to supply any more of it. This status is also set if a new Kanban Container has been created.If a new Kanban Container has been included in the control cycle and no replenishment has yet been triggered, it has the status "Waiting" and can then be set to "Empty" by the demand source (consumer). |
| In Process - 3 / In Transit - 4 | The statuses "In Process" and "In Transit" are set by the supply source (supplier) to inform the demand source (consumer) that the Kanban Containers are either being processed or are in transit.If you use Kanban Containers with purchase orders, the status of a Kanban Container is automatically set to IN TRANSPORT if an inbound delivery has been generated for the order. |
| Full - 5 | The status "Full" is assigned by the demand source (consumer) upon receipt of the container or if the goods receipt has been posted for the kanban. Exception: Decoupling of Status Change and Goods Receipt Posting. |
| In Use -6 | The status "In Use" is set by the demand source to inform the supply source which Kanban Containers are currently being emptied. (This status can only be set on the kanban board.) |
| Error - 9 | The status "Error" is set only by the system. It is set if an error occurs during the processing of a Kanban Container. This may happen, for instance, if a Kanban Container is set to "Empty" and a purchase order is simultaneously to be created. If the desired vendor is invalid at this time, it does not make sense to resolve the situation in dialog mode here. The status of the Kanban Container is then set to "Error" with an appropriate system message.If you have specified in Customizing for Kanban that only an error message is to be issued when a certain error occurs, the kanban status is not set to "Error". For more information, see: Error Handling. |
| Empty - 2 | The status "Empty" is set by the demand source (consumer) when the kanban quantity has been consumed. Depending on the replenishment strategy, this immediately triggers replenishment. |

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
> Flagged while digesting this document, not verified: Withdraw Quantity note says it can be 50 or less 'based on the demo data', but the RM233-1 control cycle defined in the same script has Container quantity 100, so the limit would be 100 or less.

> [!warning] Conflict
> Flagged while digesting this document, not verified: One-card Kanban overview says the second container is set to Empty when remaining material 'reaches or exceeds' the trigger quantity, whereas the step purpose and example (15 in container, trigger 5, withdraw 10 or more) say it triggers when remaining quantity reaches or falls below the trigger quantity.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/material-replenishment-with-kanban-external-procurement-1e3-ae-test-sc]]
- related-to :: [[12-production-and-manufacturing/test-script-material-replenishment-with-kanban-in-house-production-4b3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 45,010 chars in the whole document
