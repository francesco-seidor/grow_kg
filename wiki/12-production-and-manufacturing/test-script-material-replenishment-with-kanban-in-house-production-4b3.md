---
id: 12-production-and-manufacturing/test-script-material-replenishment-with-kanban-in-house-production-4b3
title: "Test Script: Material Replenishment with Kanban – In-House Production (4B3_AE) (4B3_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 4B3: Kanban replenishment with in-house production, covering prerequisites, MRP, Kanban status and backflush."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/kanban-in-house-production]
aliases: [4B3_S4CLD2608_BPD_EN_AE]
keywords: ["Kanban Replenishment (In-House Production, External…", kanban replenishment, kanban control cycles, kanban container status, in-house production, repetitive manufacturing backflush, material requirements planning, planned independent requirements, production orders, kanban board]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B3_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1016
topic: 12-production-and-manufacturing/kanban-in-house-production
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Material Replenishment with Kanban – In-House Production (4B3_AE) (4B3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Kanban Replenishment (In-House Production, External Procurement, Stock Transfer)** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Material Replenishment with Kanban – In-House Production (4B3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854466)

[2 Prerequisites 4](#_Toc232854467)

[2.1 System Access 4](#_Toc232854468)

[2.2 Roles 4](#_Toc232854469)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232854470)

[2.4 Business Conditions 7](#_Toc232854471)

[2.5 Preliminary Steps 8](#_Toc232854472)

[2.5.1 Check Configuration - Define In-House Production Strategies (Optional) 8](#_Toc232854473)

[2.5.2 Create Product Cost Collectors 9](#_Toc232854474)

[2.5.3 Create Preliminary Cost for the Product Cost Collectors 10](#_Toc232854475)

[2.5.4 Control Cycle for Classic Kanban: In-House Production 11](#_Toc232854476)

[2.5.4.1 Control Cycle for In-House Production: Planned Orders with MRP 11](#_Toc232854477)

[2.5.4.2 Control Cycle for In-House Production: Production Orders with MRP 12](#_Toc232854478)

[2.5.5 Initialize Material Stock 13](#_Toc232854479)

[3 Overview Table 15](#_Toc232854480)

[4 Test Procedures 17](#_Toc232854481)

[4.1 Anonymous Forecast and MRP 17](#_Toc232854482)

[4.1.1 Create Planned Independent Requirements 17](#_Toc232854483)

[4.1.2 Material Requirements Planning 18](#_Toc232854484)

[4.1.3 Adjust Planning in Planning Table 20](#_Toc232854485)

[4.2 Production-Supply by Changing Kanban Container Status and Using Kanban Board 21](#_Toc232854486)

[4.2.1 Classic Kanban: In-House Production - Planned Orders with MRP 21](#_Toc232854487)

[4.2.1.1 Set Available Kanban to EMPTY 21](#_Toc232854488)

[4.2.1.2 Change the Kanban to FULL 23](#_Toc232854489)

[4.2.2 Classic Kanban: In-House Production - Production Orders with MRP 25](#_Toc232854490)

[4.2.2.1 Check Dependent Requirement of Material SG234 25](#_Toc232854491)

[4.2.2.2 Set Available Kanban to EMPTY 26](#_Toc232854492)

[4.2.2.3 Pick Components for Production Order 28](#_Toc232854493)

[4.2.2.4 Confirm Production Operation 29](#_Toc232854494)

[4.2.3 Kanban Control Cycles Analysis (Optional) 30](#_Toc232854495)

[4.2.4 Monitor Replenishment Situation (Optional) 31](#_Toc232854496)

[4.3 Repetitive Manufacturing Backflush 32](#_Toc232854497)

[4.4 Post Processing List of Error Records 34](#_Toc232854498)

[4.5 Review Manufacturing Object Pages 35](#_Toc232854499)

[5 Appendix 37](#_Toc232854500)

[5.1 Process Integration 37](#_Toc232854501)

[5.2 Kanban Status - Status Change/Kanban Signal 37](#_Toc232854502)

[5.2.1 Classification of the Processing Status of Kanban Container 37](#_Toc232854503)

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
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Production Supervisor - Lean Manufacturing | SAP_BR_PRODN_SUPVR_LEAN_MFG | Production Supervision - Lean Manufacturing |  |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company is created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG233 | FERT 233, PD, Repetitive Manuf. |  |
| Material | SG234 | SEMI234,PD,KANBAN, MTS |  |
| Material | SG233 | SEMI233,PD,KANBAN, REM |  |
| Material | RM234 | RAW234,VB,Repetitive Manuf. |  |
| Material | RM233-1 | RAW233-1, PD, KANBAN Stock Transfer |  |
| Material | RM233-2 | RAW233-2,ND,KANBAN,sched. agreements |  |
| Material | RM233-4 | RAW233-4,ND,KANBAN,sched. agreements |  |
| Material | RM235 | RAW235,VB |  |
| Vendor | 33300002 | Domestic UAE Supplier 2 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |
| Storage Location | 331E | Kanban |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristic of Material | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| FG233 | 0 | FERT | PC |  |  |
| SG234 | 1 | SEMI | PC |  |  |
| RM235 | 2 | RAW | PC |  |  |
| SG233 | 1 | SEMI | PC |  |  |
| RM234 | 2 | RAW | PC |  |  |
| RM233-1 | 1 | RAW | PC |  |  |
| RM233-2 | 1 | RAW | PC |  |  |
| RM233-4 | 1 | RAW | PC |  |  |

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

#### Check Configuration - Define In-House Production Strategies (Optional)

Purpose

The necessary customizing settings to run through some basic scenarios have already been created as preconfigured SAP Best Practice content. You can check detailed entries through available Self-Service Configuration UI (SSCUI). For demonstration of SAP Best Practice scope item, you may not be able to adapt pre-configured SAP Best Practice content. If necessary, you can create your own entries according to your business requirement.

| Key of Pre-delivered Replenishment Strategy | Description | Comments |
| --- | --- | --- |
| PD05 | Planned Order (MRP) |  |
| PD20 | Planned Order |  |
| PD30 | Production Orders |  |
| PD3T | Production Order (Trigger Point) |  |
| PD60 | Production Order (MRP) |  |
| PD6T | Production Order (MRP, Trigger Point) |  |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

- In the SAP S/4HANA Cloud Public Edition system, in the SAP Fiori launchpad, open Manage Your Solution (F1241) app using the business role SAP_BR_BPC_EXPERT and go to Configure your Solution.
- In the Application Area listbox, select Manufacturing.
- In the Sub Application Area listbox, select Kanban.
- In Item Name, select Replenishment Strategies.
- Choose Define In-House Production Strategies (ID: 103944).
- Choose Configure.

SAP Central Business Configuration:

- Log on to the project experience in SAP Central Business Configuration.
- Go to the Business Processes Configuration app and search for the following activity: Define In-House Production Strategies and choose Go to Activity.
- Choose OK.

#### Create Product Cost Collectors

Purpose

This step can only be executed if product cost planning is activated.

|  |
| --- |
| Note The product cost collector might have already been created in connection with other scope items. To have a check if the related ones are already created, please use the App Maintain Product Cost Collectors (KKF6N) with the selection based on the given material/plant data. In case the product cost collector already exists, the selectable entry on the left panel will be displayed and this step can be skipped. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Product Cost Collectors - Production Versions - Collective (KKF6M). | The Create Multiple Product Cost Collector for Production Versions screen displays. |  |
| 3 | Enter Relevant Values | Make the following entries and choose Execute.Plant: 3310Order Type: YBMROnly Repetitive Mfg Mat.: <select>Once the product cost collector is created, it can't be created again with the same data. |  |  |
| 4 | Select Production Versions | The Select Production Versions screen could display if there is more than one production version or more than one material. | The Select Production Versions screen may display if there is more than one production version or more than one material. |  |
| 5 | Save | Select the row for the production version of materials FG233 and SG233. Choose Save. | The message log displays. |  |
| 6 | Exit | Choose Exit. |  |  |

#### Create Preliminary Cost for the Product Cost Collectors

Purpose

In this topic, you create preliminary costs for the product cost collectors.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Preliminary Cost Estimate - Product Cost Collectors (MF30). | The Creation of Preliminary Cost Estimates For Product Cost Collectors screen displays. |  |
| 3 | Enter Relevant Values | Make the following entries and choose Execute.Costing Date : <Current Date>Plant: 3310 |  |  |

#### Control Cycle for Classic Kanban: In-House Production

##### Control Cycle for In-House Production: Planned Orders with MRP

Purpose

In this step, you create a control cycle for classic Kanban that can be used for in-house production. In the control cycle, you define the demand source, the supply source and the procedure that must be used to replenish the Kanban material. You also define the number of Kanbans that circulate among the supply source and the demand source, as well as the quantity a Kanban contains.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). |  |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Edit.Plant: 3310Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the Selection Details | Make the following entries and choose Continue:Classic KANBAN: SelectedMaterial: SG233Supply Area: KANBAN_02Lifecycle status: Released | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Make the following entries:Number of Containers: 5Container Quantity: 400Maximum Empty Containers: 2Number of Load Carriers: 1Go to the next part and in the Replenishment Strategy tab, select In-House Production, enter PD05 and choose Enter.Person Responsible: 001Production Version: 0001 |  |  |
| 6 | Save | Choose Save Control Cycle. | You have created an internal Kanban control cycle for material SG233 . |  |

##### Control Cycle for In-House Production: Production Orders with MRP

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Kanban Control Cycles (PKMC). |  |  |
| 3 | Navigate to Create Control Cycle Screen | Make the following entries and choose Edit.Plant: 3310Choose Create Control Cycle. | The Create Control Cycle screen displays. |  |
| 4 | Enter the Selection Details | Make the following entries and choose Continue:Classic Kanban: SelectedMaterial: SG234Supply Area: KANBAN_05Lifecycle status: Released | The Control Cycle Maintenance: Change screen displays. |  |
| 5 | Enter the Control Cycle Details | Number of Containers: 3Container Quantity: 10Maximum Empty Containers: 2Number of Load Carriers: 1Go to the next part and in the Replenishment Strategy section, select In-House Production, enter PD60 and choose Enter.Person Responsible: 001Production Version: 0001 |  |  |
| 6 | Save | Choose Save Control Cycle. | You have created an internal Kanban control cycle for material SG234 . |  |

#### Initialize Material Stock

Purpose

This step describes standard purchasing process. But in real business cases, raw materials are usually purchased from external vendors.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock (F1062) screen displays. |  |
| 3 | Input Material | Make the following entries and press Enter:Material: RM235; RM234Plant: Plant 1 AE3310 | The stock overview for the material displays. |  |
| 4 | Select Stock | Select the icon next to the stock where you want to add initial stock.For example:Storage Location: 331BUnrestricted Use Stock | In a dialog box, the Storage Location, Stock Type and Current Quantity fields display per your entries in previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <Today>Posting Date: <Today>Stock Change: Initial EntryQuantity: <Enter a quantity> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |
| 6 | Repeat | If you want to execute the whole production process for finished goods FG233, you can post initial stock for other necessary components, for example,RM234, RM233-2, RM233-4, RM233-1, into Storage Location 331B. |  |  |

## Overview Table

The scope item Manufacturing with Kanban supply into production consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APPs | Expected Results |
| --- | --- | --- | --- |
| Anonymous Forecast and MRP |  |  |  |
| [Create Planned Independent Requirements](#unique_15) [page ] 17 | Production Planner | Maintain PIRs (F3445) |  |
| [Material Requirements Planning](#unique_16) [page ] 18 | Production Planner | Schedule MRP Runs (F1339) |  |
| [Adjust Planning in Planning Table](#unique_17) [page ] 20 | Production Supervisor - Repetitive Manufacturing | Manage Repetitive Manufacturing (MF50) |  |
| Production-Supply by Changing Kanban Container Status and Using Kanban Board |  |  |  |
| Classic Kanban: In-House Production - Planned Orders with MRP |  |  |  |
| [Set Available Kanban to EMPTY](#unique_18) [page ] 21 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| [Change the Kanban to FULL](#unique_19) [page ] 23 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| Classic Kanban: In-House Production - Production Orders with MRP |  |  |  |
| [Check Dependent Requirement of Material SG234](#unique_20) [page ] 25 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) |  |
| [Set Available Kanban to EMPTY](#unique_21) [page ] 26 | Production Operator - Lean Manufacturing | Set Kanban Container Status (F3717) |  |
| [Pick Components for Production Order](#unique_22) [page ] 28 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) |  |
| [Confirm Production Operation](#unique_23) [page ] 29 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) |  |
| [Kanban Control Cycles Analysis (Optional)](#unique_24) [page ] 30 | Production Supervisor - Lean Manufacturing | Kanban Control Cycles Analysis (F5235) |  |
| [Monitor Replenishment Situation (Optional)](#unique_25) [page ] 31 | Production Supervisor - Lean Manufacturing | Kanban Board (F4630) |  |
| [Repetitive Manufacturing Backflush](#unique_26) [page ] 32 | Production Operator - Repetitive Manufacturing | Confirm Repetitive Manufacturing (MFBF) |  |
| [Post Processing List of Error Records](#unique_27) [page ] 34 | Production Operator - Repetitive Manufacturing | Reprocess Goods Movements (COGI). |  |
| [Review Manufacturing Object Pages](#unique_28) [page ] 35 | Production Planner | Search |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Anonymous Forecast and MRP

#### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Planned Independent Requirements (PIRs) are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, that is, splitting one planned quantity according to dates.

Note Instead of creating a single requirement, sometimes a requirement plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: FG233 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Edit PIRs | Select the material item and choose Edit on the upper right part of the screen.On the screen, enter quantities per period, for example:PIR: 100Make sure the version is active.Version Active: Yes |  |  |
| 7 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

#### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The aim of material requirements planning is to tailor available capacities and receipts on time to suit requirements quantities. You can use MRP or consumption-based planning for this purpose. Single-item multi-level requirement planning is performed for plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG233>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: FG233Changed BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG233 in the search box and choose Go at the top-right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Adjust Planning in Planning Table

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes how to plan the production of materials on the production lines.

Prerequisite

Requirements planning is performed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Repetitive Manufacturing (MF50). | The Planning Table Initial Screen: Change Mode screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.Material: FG233Plant: 3310 | The Planning Table For Repetitive Manufacturing: Change Model screen displays. |  |
| 4 | Change the Quantity | Change any planned quantities in row 0001 WINDING. | If you want to change the periods in the Planning table, choose Menu > View > Period > Week (Month or Day) . |  |
| 5 | Save | Choose Save.Confirm any warning notifications for Storage Locations. | Material production is planned on production lines and the planned orders are fixed. When there are quantity changes, log on to the SAP Fiori launchpad as a Production Planner, open Monitor Material Coverage - Net Segments to check the planned order number. |  |

### Production-Supply by Changing Kanban Container Status and Using Kanban Board

Kanban board is one of the tools that can be used to change the container status, which can provide both demand source (consumer) and supply source (supplier, producer) with a detailed overview of Kanban circulation. In addition, Material Replenishment could be quickly triggered by setting Kanban container status.

#### Classic Kanban: In-House Production - Planned Orders with MRP

In this step, you produce the material SG233 via internal Kanban in a repetitive manufacturing environment.

##### Set Available Kanban to EMPTY

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set an available Kanban to EMPTY to trigger the in-house production of material SG233 .

Prerequisite

The Kanban control cycle for material SG233 is created and inventory of component RM234 is available in storage location 331B.

Procedure

It is possible to change status of Kanban Container with various Fiori apps. You can choose one of them to execute the task in this step (set to EMPTY) and subsequent steps (for example, set to FULL) where applicable. Here we provide two options you can leverage, and you can choose either of them.

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | You can select a Kanban container on the left part of the screen. Choose Value Help icon, and the Select: Barcode dislog box displays. Choose Show Filters to make following entries and press Enter:Plant: 3310Production Supply Area: KANBAN_02From the Items list, choose one of the Kanbans for SG233 with Current Status of either WAIT or FULL. | The Kanban you entered displays. |  |
| 4 | Check Kanban Information | On the right part of the screen, check the following entry:Target Status: EMPTY |  |  |
| 5 | Set the Kanban to Empty | On the left part of the screen, choose Save at the bottom. |  |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Kanban Board (F4630).Note You can find the app under category Production Control - Kanban Monitoring. |  |  |
| 3 | Search | Make following entries and choose Go:Plant: 3310Production Supply Area: KANBAN_02Material: SG233 |  |  |
| 4 | Select Kanban Container | In the Control Cycle, choose one of the Kanban Container with WAIT or FULL status. You can check the legend for description of visual elements.Container Details panel displays on the right side.You can check detailed information. |  |  |
| 5 | Set the Kanban to Empty | Choose Set to EMPTY above the list. | The selected Kanban Container is displayed as EMPTY. |  |

##### Change the Kanban to FULL

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you change the status of the Kanban you have processed in the previous step to FULL.

Prerequisite

The status of the KANBAN is previously set to EMPTY.

Procedure

There are 2 options available for this step. Choose only one of them.

Option 1: You can post goods receipt by changing the Kanban container status directly.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | You can select a Kanban container on the left part of the screen. Choose Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_02From the Items list, choose one of the Kanban for SG233 with Current Status: EMPTY. | The Kanban you entered displays. |  |
| 4 | Check Kanban Information | On the right part of the screen, check the following entry:Target Status: FULL |  |  |
| 5 | Set the Kanban to Full | On the left part of the screen, choose Save at the bottom. | Setting the empty Kanban to FULL executes a REM Backflush in the background. This backflush receives amount specified to fill the Kanban, and consumes the components specified in the Bill of Material to produce the received amount. |  |

Option 2: As an alternative, you can post goods receipt using Kanban confirmation.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Repetitive Manufacturing - Kanban (PK41).You can find the app under category Production Control - Kanban Container Processing. |  |  |
| 3 | Select the Kanban Container | Choose Select Kanban Containers by Material and Plant and make the following entries:Material: < SG233 >Plant: 3310Choose Continue to go to the Confirmations screen with the containers. | The containers that can be confirmed are displayed. |  |
| 4 | Kanban Confirmation | In the Confirm Kanban Container table, find the container that you want to confirm and make the following entries:Confirm Container: SelectActual Quantity: <Actual Quantity>Press Save.Note In case the component posting needs to be adjusted, set the checkmark for Adjust Components. You can adjust the component in the additional screen with component details. | The confirmation is saved. The system has posted the goods receipt for SG233 and the goods issues for the components. The Kanban container is set to Full. |  |

#### Classic Kanban: In-House Production - Production Orders with MRP

This process step shows you how to produce the material SG234 via production order.

##### Check Dependent Requirement of Material SG234

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check whether planned orders for SG234 exist.

Prerequisite

The independent requirement planning for material FG233 is done and a planning run is finished.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). |  |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Check Area of Responsibility | Choose the user icon and select the App Settings. In the MRP Settings dialog box, choose Area of Responsibility.Ensure that only the following entry displays:Plant 1 AE / 001 (MRP Controller 001).Choose Back. | If there is no entry for Plant 1 AE on the Area of Responsibility screen, choose the AOR Status button to to set the status of this entry as AOR Is Assigned.For other plant entries on the Area of Responsibility screen, choose the AOR Status button to unassign them and then choose Back. |  |
| 5 | Select Material | In the search area, make the following entries and choose Go.Material: SG234Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 6 | Check the Planned Orders | Review the planned orders (PldOrd XXXX) generated for dependent requirements (DepReq XXXX). |  |  |

##### Set Available Kanban to EMPTY

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to set an available Kanban to EMPTY to trigger the in-house production of material SG234 .

Prerequisite

The Kanban control cycle for material SG234 is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Lean Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Kanban Container Status (F3717). |  |  |
| 3 | Select the Kanban | You can select a Kanban container on the left part of the screen. Choose the Value Help icon to open Select: Barcode window. Choose Show Filters to make following entries and press Enter.Plant: 3310Production Supply Area: KANBAN_05From the Items list, choose one of the Kanban for SG234 with Current Status WAIT or FULL. | The Kanban you entered displays on the Entered tab. |  |
| 4 | Check Kanban Information | On the right part of the screen, check the following entry:Target Status: EMPTY |  |  |
| 5 | Set the Kanban to Empty | On the left part of the screen, choose Save at the bottom. | Container saved. |  |
| 6 | Select Saved Container | On the left part of the screen, choose the Saved tab, and choose the changed container. |  |  |
| 7 | Check Generated Production Order | On the right part of the screen, check following:Current Status: EMPTYProduction Order: <XXXX>Note down the generated production order number. |  |  |

Result

When setting the container to empty the system will automatically create and directly release a production order with order type YPK1. With this strategy, one production order will be created for one empty Kanban container.

##### Pick Components for Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to pick the released production order.

Prerequisite

Ensure that sufficient material is present on stock for RM235 . To check the stock, you can use the warehouse user and the app Display Stock Overview (MMBE).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Pick Components for Production Orders (CO27). |  |  |
| 3 | Enter Relevant Search Criteria | Make the following entries and choose Execute.Profile: 000002Production Order: <Your Production Order number> | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking | Select the relevant reservations and choose Picking. |  |  |
| 5 | Post | Choose Post to post the goods movements. | The goods movements have been posted. |  |

##### Confirm Production Operation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents contains the processing status of orders, operations, sub-operations, and individual capacities. It is an instrument for controlling orders. This process step shows you how to uses time event confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). |  |  |
| 3 | Enter Production Order and Operation | On the Enter Order and Operation screen, make the following entries and choose Go:Order: <Your Production Order number>Operation: 0010 |  |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, make the following entries:Yield: <enter the amount you want to Confirm>Scrap: <enter the amount you want to Scrap> |  |  |
| 5 | Check Material Movements (only for Operation 0020) | In the Material Movements section, check the material list. | For Operation 0020, SG234 would list here. |  |
| 6 | Enter Fields in Activities Section | In the Activities section, make the following entries:Setup: <enter the setup time you want to confirm for this operation>Machine: <enter the machine time you want to confirm for this operation>Labor: <enter the labor time you want to confirm for this operation> |  |  |
| 7 | Save Your Entries | Choose Post and Complete to make final confirmation for this operation. |  |  |
| 8 | Repeat Steps | Go back and repeat steps 3 to 7 for operation number 0020, save your entries. |  |  |

Result

The last operation will trigger automatic GR posting when confirming the operation. Kanban container status will be set to full again.

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
| 3 | Search | You can restrict selection by certain search criteria. Make following entries and choose Go:Plant: 1010Production Supply Area: <Production Supply Area>Material: <Material> |  |  |
| 4 | Check Kanban Container | The kanban containers are represented in different colors according to their status. Choose one Kanban Container. | The Container Details panel displays at the right side where you can check detailed information. |  |
| 5 | Kanban Correction | If the desired status change results in an error, the error message is displayed in the details panel of the kanban container. You can use the Correct Kanban app to correct the Kanban Container with ERROR status. |  |  |

### Repetitive Manufacturing Backflush

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step executes multiple activities in a single step, such as finished product goods receipt, backflush of component materials, posting of costs to cost collector and creation of material and journal entries.

Errors can occur in back flushing. For example, there may not be sufficient warehouse stock available or important data, such as the issue storage location may be missing. You then have the following options:

Make corrections immediately in a component overview.

Backlogs are created for the complete requirement quantities of the components with errors.

You can process these backlogs later. If negative stocks are allowed for the material in the storage location, the system posts negative stock quantities in certain circumstances.

|  |
| --- |
| Note Goods Movement is 131 for Goods Receipt and 261 for Goods Issue. The Material is FG233 (Finished Product). |

Prerequisite

Planned orders must exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Production Operator - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Repetitive Manufacturing (MFBF). | The REM Confirmation - Transaction Variant: None screen displays. |  |
| 3 | Enter Selection Data | Make the following entries and press Enter:Assembly backflush: XMake-to-stock tab:Planned Order: <Planned order number for FG233 from previous step> | The system proposes Material and Conf. Qty. Change the Conf. Qty as needed. |  |
| 4 | Post | Choose Post with Correction.Select the production version if prompted. |  |  |
| 5 | Post | Choose Post. | The finished product is received into stock and all components listed in the bill of material are issued from stock.To view the Material document, log on to the SAP Fiori launchpad as a Warehouse Clerk and open Material Documents Overview.Debited Accounts: Credited AccountsCost collector: ConsumptionInventory: Inventory changeInventory - Finished Product: Inventory Change - ProductionConsumption - Raw Materials: Inventory - Raw Materials and semi-finished goods |  |

### Post Processing List of Error Records

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To post process backlogs from backflushing, you can use this function to create a list of components that have to be postprocessed.

Prerequisite

Material movements are missing for previous backflush operations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Reprocess Goods Movements (COGI). | The Postprocessing of Error Records from Automatic Goods Movements screen displays. |  |
| 3 | Enter Selection Data | Make the following entries and choose Enter:Plant: 3310 | The system displays a list of all assemblies that correspond to the selection criteria and that have components to be postprocessed. This list is sorted by assemblies and production versions. If you have to correct the components or if you want to check availability, select the appropriate assembly and choose Change Selected Postprocessing Recs. The system displays the components of the selected assembly. |  |
| 4 | Save | Review the generated list, then choose Save.Correct any missing material movement for planned orders processed. |  |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner.Note You can use any role in section Role above. | The SAP Fiori launchpad displays. |  |
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
> Flagged while digesting this document, not verified: Monitor Replenishment Situation step searches Plant 1010 while the rest of the script and master data use Plant 3310 (Plant 1 AE).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/material-replenishment-with-kanban-external-procurement-1e3-ae-test-sc]]
- related-to :: [[12-production-and-manufacturing/test-script-material-replenishment-with-kanban-stock-transfer-4b4-ae-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4B3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 59,727 chars in the whole document
