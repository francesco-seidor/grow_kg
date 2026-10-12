---
id: 12-production-and-manufacturing/production-capacity-evaluation-and-leveling-consumer-products-5oi-ae-t
title: Production Capacity Evaluation and Leveling – Consumer Products (5OI_AE) – Test Script (5OI_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5OI_AE: PIRs, pMRP simulations, MRP, capacity evaluation and leveling for a coffee MTS process."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/capacity-evaluation-and-leveling, topic/end-to-end-produce-and-sell]
aliases: [5OI_S4CLD2608_BPD_EN_AE]
keywords: [Capacity Evaluation and Leveling, production capacity leveling, capacity evaluation, planned independent requirements, pmrp simulations, material requirements planning, work center capacity, production scheduling, make-to-stock production, work center schedules]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OI_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1114
topic: 12-production-and-manufacturing/capacity-evaluation-and-leveling
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Production Capacity Evaluation and Leveling – Consumer Products (5OI_AE) – Test Script (5OI_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OI_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Capacity Evaluation and Leveling** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Production Capacity Evaluation and Leveling – Consumer Products (5OI_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857552)

[2 Prerequisites 4](#_Toc232857553)

[2.1 System Access 4](#_Toc232857554)

[2.2 Roles 4](#_Toc232857555)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232857556)

[2.4 Business Conditions 9](#_Toc232857557)

[2.5 Preliminary Steps 9](#_Toc232857558)

[2.5.1 Create Work Center Group 9](#_Toc232857559)

[2.5.2 Check Available Capacity in Work Center 10](#_Toc232857560)

[2.5.3 Check Formulas in Work Center 12](#_Toc232857561)

[2.5.4 Check Routings 13](#_Toc232857562)

[2.5.5 Check Production Version 15](#_Toc232857563)

[3 Overview Table 16](#_Toc232857564)

[4 Test Procedures 18](#_Toc232857565)

[4.1 Anonymous Forecast and MRP 18](#_Toc232857566)

[4.1.1 Option 1: Create Planned Independent Requirements 18](#_Toc232857567)

[4.1.2 Option 2: Create Planned Independent Requirements by Upload File 20](#_Toc232857568)

[4.1.3 Schedule pMRP Simulation Creation 23](#_Toc232857569)

[4.1.4 Process pMRP Simulations 24](#_Toc232857570)

[4.1.5 Check Planned Independent Requirements 27](#_Toc232857571)

[4.1.6 Material Requirements Planning 28](#_Toc232857572)

[4.2 Evaluate Capacity Situation 30](#_Toc232857573)

[4.2.1 Check Capacity Situation 30](#_Toc232857574)

[4.2.2 Apply Changes to Available Capacity 32](#_Toc232857575)

[4.3 Production Capacity Leveling 34](#_Toc232857576)

[4.3.1 Production Scheduling 34](#_Toc232857577)

[4.3.2 Review Work Center Schedules 36](#_Toc232857578)

[4.3.3 Review Capacity Situation 37](#_Toc232857579)

[5 Appendix 40](#_Toc232857580)

[5.1 Process Integration 40](#_Toc232857581)

[5.1.1 Succeeding Processes 40](#_Toc232857582)

## Purpose

Overview

This scope item supports production planning and capacity evaluation for a Consumer Products Industry-flavored Make-to-stock process and provides options from prompt reaction. The Consumer Products industry-flavored process describes a two-stage production process for coffee displays. The first stage reflects the roasting and packaging process of medium resp. dark roasted beans under consideration of a fixed capacity of the roasting drums. The second stage reflects a display packaging process where two different finished products (medium and dark roasted coffee beans bags) are packed into a display.

The process starts with the creation of a demand forecast for finished material (display) represented by planned independent requirements (PIRs). You can create the PIRs manually or via upload file. Predictive Material and Resource Planning (pMRP) is used to create, schedule and evaluate pMRP simulations that support you in making informed decisions for your production planning. The results can be taken over and will be released to your operational data as planned independent requirements.

As a result, component production and raw material demand are planned. All orders and operations that are planned with the MRP are allocated to the required capacities. Production planners can evaluate the capacity utilization for a defined time horizon and execute manual changes in orders to resolve upcoming bottleneck situations in the defined area of responsibility.

The process of production capacity leveling represents a central part of preparation for the manufacturing process of components. Production planners can assign orders and operations from the production plan to available timeslots of capacities. Additionally, the planners can simulate and choose other alternatives for production by assigning other available production versions, letting the planners schedule the best option for their manufacturing.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Material Master Data:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG0502 | Display Med + Dark 48 * 1kg Arabica | Batch Managed Finished Material, QM, Manufacturing Date |
| Material | FG0511 | Carton 12 x 1kg Bags Medium Beans Arabica | Batch Managed Finished Material, MTS with Maximum Lot Size, QM |
| Material | FG0512 | Carton 12 x 1kg Bags Dark Beans Arabica | Batch Managed Finished Material, MTS with Maximum Lot Size, QM |
| Material | PK0501 | Coffee Bag "Medium" 1 kg | Batch Managed Packaging Material, MRP and Costing Relevant |
| Material | PK0502 | Coffee Bag "Dark" 1 kg | Batch Managed Packaging Material, MRP and Costing Relevant |
| Material | PK0504 | Label | Batch Managed Packaging Material, MRP and Costing Relevant |
| Material | PK0507 | Carton for 12 x 1kg Bags | Packaging Material, MRP and Costing Relevant |
| Material | PK0508 | Display Carton Coffee Beans 48 x 1 kg | Packaging Material, MRP and Costing Relevant |
| Material | RM0501 | Raw Coffee Beans- Arabica | Batch Managed Raw Material |

Organizational Data:

| Data | Sample Value | Description | Other Attributes |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |

Bill of Material Structure

| Product | Level | Material Type | Unit | Description |
| --- | --- | --- | --- | --- |
| FG0502 | 0 | FERT | PC | Finished Good for MTS Processing with Batch Management |
| FG0511 | 1 | FERT | PC | Finished Material, Batch Managed, QM, MTS |
| PK0501 | 2 | VERP | PC | Packaging Material, Batch Managed, External Procurement |
| PK0504 | 2 | VERP | PC | Label |
| PK0507 | 2 | VERP | PC | Packaging Material |
| RM0501 | 2 | RAW | KG | Raw Material, Batch Managed, External Procurement |
| FG0512 | 1 | FERT | PC | Finished Material, Batch Managed, QM, MTS |
| PK0502 | 2 | VERP | PC | Packaging Material, Batch Managed, External Procurement |
| PK0504 | 2 | VERP | PC | Label |
| PK0507 | 2 | VERP | PC | Packaging Material |
| RM0501 | 2 | RAW | KG | Raw Material, Batch Managed, External Procurement |
| PK0508 | 1 | VERP | PC | Packaging Material |
| PK0504 | 1 | VERP | PC | Label |

Work Center

| Work Center | Plant | Work Center Category | Work Center Description |
| --- | --- | --- | --- |
| DP050001 | 3310 | 0001 | Display Packaging 1 |
| DR050001 | 3310 | 0001 | Drum Roasting Machine 1 |
| PM050001 | 3310 | 0001 | Packaging Machine 1 |
| CS050001 | 3310 | 0001 | Cooling Sieve 1 |
| DR050002 | 3310 | 0001 | Drum Roasting Machine 2 |
| PM050002 | 3310 | 0001 | Packaging Machine 2 |
| CS050001 | 3310 | 0001 | Cooling Sieve 2 |
| DP050002 | 3310 | 0001 | Display Packaging 2 |

Available capacity for Work Center

This overview shows predefined shifts (Shift Sequence: Capacity Group PP):

| Shift | Start time | End time | Length of break |
| --- | --- | --- | --- |
| YS1, Early Shift | 06:00:00 | 14:00:00 | 00:30:00 |
| YS2, Late Shift | 14:00:00 | 22:00:00 | 00:30:00 |
| YS3, Night Shift | 22:00:00 | 06:00:00 | 00:30:00 |

Routing:

| Material | Plant | Routing Number | Group Counter Routing |
| --- | --- | --- | --- |
| FG0502 | 3310 |  | 1 |
| FG0502 | 3310 |  | 2 |
| FG0511 | 3310 |  | 1 |
| FG0511 | 3310 |  | 2 |
| FG0512 | 3310 |  | 1 |
| FG0512 | 3310 |  | 2 |

Production Version:

Create production versions for the Finished Material FG0502, FG0511 and FG0512 using the BOM and routing created in the above steps.

| Material | Plant | Production Version | Routing Number | Group Counter Routing | BOM Alternative |
| --- | --- | --- | --- | --- | --- |
| FG0502 | 3310 | 0001 |  | 1 | 1 |
| FG0502 | 3310 | 0002 |  | 2 | 1 |
| FG0511 | 3310 | 0001 |  | 1 | 1 |
| FG0511 | 3310 | 0002 |  | 2 | 1 |
| FG0511 | 3310 | 0001 |  | 1 | 1 |
| FG0512 | 3310 | 0002 |  | 2 | 1 |

Routing

This overview shows routings for Finished Materials. In the predelivered demo data, two routings were created for each Material with same operations but different work centers.

| Product | Operation | Description | Work Center | Work Center (Alternative) |
| --- | --- | --- | --- | --- |
| FG0511 / FG0512 | 0010 | Drum Roasting | DR050001 | DR050002 |
|  | 0020 | Cooling Sieve | CS050001 | CS050002 |
|  | 0030 | Packaging Machine | PM050001 | PM050002 |
| FG0502 | 0010 | Material Staging | DP050001 | DP050002 |
|  | 0020 | Display Packaging | DP050001 | DP050002 |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |
| 3Y1 | Create Product Master of Type "Packaging" - MDS |
| BNJ | Create Production Work Center - MDS |
| 2ZW | Create Batch Management Master Data - MDS |

### Business Conditions

The following business conditions must be met before this scope item can be tested.

| Scope Item ID | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Test Script Standard Cost Calculation (BEG) |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up-to-date. |

### Preliminary Steps

#### Create Work Center Group

In this business process, you are responsible for the capacity planning of some coffee roasting and packaging machines. With the function of work center groups you are able to combine them to one group an use this group as simplified entry for selected capacity apps instead of entering work center individually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Groups (F4044). | The Manage Work Center Groups screen is displayed. |  |
| 3 | Enter Data | On the Manage Work Center Groups screen, choose Create. In the Selection Conditions area, enter the following data and press Enter.In the Create Group dialog box, make the following entries and choose Create:Group: 05_CoffeeDescription: Coffee ProductionGroup Type: ALTERNATIVPlant: 3310 |  |  |
| 4 | Manage Work Center Groups | On the Manage Work Center Groups screen, choose Assign Work Center.In the Work Center dialog box, select the following work center and choose OK:Work Center: DR050001, DR050002, CS050001, CS050002, PM050001, PM050002, DP050001, DP050002 |  |  |

#### Check Available Capacity in Work Center

Purpose

Standard available capacity is applied to the work centers and no shifts are assigned initially. In case these values have been adjusted during testing, we recommend that you have a check to better understand the current available capacity for work centers DR050001, PM050001, CS050001, and DP050001.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Groups (F4044). | The Manage Work Center Groups screen is displayed. |  |
| 3 | Enter Work Center Group | On the Manage Work Center Groups screen, select the following entries and choose the details arrow:Name: 05_COFFEEPlant: 3310 |  |  |
| 4 | Choose Work Center | On the Manage Work Center Groups screen, in section Assigned Work Centers click on one of the work centers. A pop up appears where you choose Change Work Center.Work Center: DR050001, PM050001, CS050001 and DP050001 |  |  |
| 5 | Choose Capacity Category 001 | Choose Capacities tab. There, you can find two Capacity categories defined: 001 and 002.Double-click Capacity category: 001. | The Change Work Center: Capacity Overview screen displays.Note Capacity Category 002 is not available for work center CS050001. |  |
| 6 | Check Standard Available Capacity | On the Change Work Center Capacity: Header screen for capacity 001, check standard available capacity. Following values are preset in this scenario:Start time: 06:00:00End time: 22:00:00Length of break: 01:00:00Capacity Utilization: 80No. Ind. Capacities: 1For testing purpose, we recommend using the same values as above. |  |  |
| 7 | Check Intervals and Shifts | Choose Intervals and Shifts in the upper left corner (If you cant see this option then click Menu > Goto > Intervals and Shifts ).On the Change Work Center Capacity: Intervals of Available Capacity screen for capacity 001, available shifts are listed in the table at the bottom of the page. We recommend deleting any additional shifts effective within next 6 weeks.Choose any line you want to delete, then choose Delete line icon in the upper right.Choose Back twice to screen Change Work Center Capacity: Overview. |  |  |
| 8 | Choose Capacity Category 002 | Under Capacities tab, double-click Capacity category: 002. | The Change Work Center: Capacity Overview screen displays.Note Capacity Category 002 is not available for work center CS050001. Hence skip steps #8 and #9 for this work center. |  |
| 9 | Check Default Settings for Capacity Category 002 | Repeat step #6 and #7 for category 002. |  |  |
| 10 | Save | Choose Save. | Work center XXX in plant 3310 was changed. |  |

#### Check Formulas in Work Center

Purpose

This process step shows you how to check and set the formulas used in work centers for critical operation. Formula under Capacities tab is used to calculate the capacity requirements of the operation segments; while formula under Scheduling tab is used to calculate execution time of the operation. You need to check and set formulas for following work centers: DR050001, PM050001, CS050001 and DP050001.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Work Center (CR02). |  |  |
| 3 | Enter Plant and Work Center | On the Change Work Center: Initial Screen, make the following entries and press Enter:Plant: 3310Work Center: <Work Center>, e.g. DR050001, PM050001, CS050001 and DP050001. |  |  |
| 4 | Check Formulas under Capacities Tab | Choose Capacities tab, check formulas under Capacity category section: 001. For test purpose, we recommend using the same values as below:Setup Formula: SAP005Processing Formula: SAP006 |  |  |
| 5 | Check Formulas under Capacities Tab | Choose Capacities tab, check formulas under Capacity category section: 002. For test purpose, we recommend using the same values as below:Setup Formula: SAP005Processing Formula: SAP007 | Note Capacity Category 002 is not available for work center CS050001. |  |
| 6 | Check Formulas under Scheduling Tab | Choose Scheduling tab, check following settings. For test purpose, we recommend using the same values as below:Scheduling basis section:Capacity category: 001Execution time section:Duration of Setup: SAP001Processing Duration: SAP002 |  |  |
| 7 | Exit | Choose Save or Cancel. |  |  |

#### Check Routings

Purpose

If you want to use SAP pre-delivered demo data to run through this scenario, you need to check Routing settings in your system. We recommend to be consistent with what is described in section Routing in chapter Master Data. If it is not consistent, you need to manually change it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Routing (CA02). |  |  |
| 3 | Select Finished Material | On the Change Routing: Initial Screen screen, enter the following data and choose Continue:Plant: 3310Material: FG0511 |  |  |
| 4 | Check Routing for Finished Material (Cartons with Coffee Bags) | In the list under Header Overview, check listed routing versions. You can tick each line, choose Operation to see detailed operations for each Routing version. For pre-delivered demo data, we deliver two routing versions with respective operations.GrC: 1Operation 0010 - Work Center: DR050001Operation 0020 - Work Center: CS050001Operation 0030 - Work Center: PM050001GrC: 2Operation 0010 - Work Center: DR050002Operation 0020 - Work Center: CS050002Operation 0030 – Work Center: PM050002If the work center in respective operation in your system is not identical with above, you need to manually change it. |  |  |
| 5 | Select Finished Material (Carton with Coffee Bags) | Go back to the selection page, enter the following data and press Enter:Plant: 3310Material: FG0512 |  |  |
| 6 | Check Routing for Finished Material (Carton with Coffee Bags) | Check listed Routing versions for Finished Material FG0512 as mentioned in step #4. |  |  |
| 7 | Select Finished Material (Display) | Go back to the selection page, enter the following data and press Enter:Plant: 3310Material: FG0502 |  |  |
| 8 | Check routing for Finished Material (Display) | In the list under Header Overview, check listed routing versions. You can tick each line, choose Operation to see detailed operations for each Routing version. For pre-delivered demo data, we deliver two routing versions with respective operations.GrC: 1Operation 0010 - Work Center: DP050001Operation 0020 - Work Center: DP050001GrC: 2Operation 0010 - Work Center: DP050002Operation 0020 - Work Center: DP050002If the work center in respective operation in your system is not identical with above, you need to manually change it. |  |  |

#### Check Production Version

Purpose

Production Versions are used as source of supply during production scheduling. This process step shows you how to check the alternative work centers which are assigned to the critical operation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Versions - C223 (C223). | The Production Version: Mass Processing screen displays. |  |
| 3 | Select Finished Material (Carton with Coffee Bean Bags) | In the Selection Conditions area, enter the following data and press Enter:Plant: 3310Material: FG0511 |  |  |
| 4 | Check Production Version for Finished Materials (Carton with Coffee Bean Bags) | Check listed production versions. For pre-delivered demo data, we deliver two production versions with respective production line assignment.Production Version: 0001Production Line: Drum Roast 1Production Version: 0002Production Line: Drum Roast 2 |  |  |
| 5 | Repeat Steps | Repeat steps #3 and #4 for Finished Material FG0512. |  |  |
| 6 | Select Finished Material (Display) | In the Selection Conditions area, enter the following data and press Enter:Plant: 3310Material: FG0502 |  |  |
| 7 | Check Production Version for Finished Materials (Display) | Check listed production versions. For pre-delivered demo data, we deliver two production versions with respective production line assignment.Production Version: 0001Production Line: Display Packaging 1Production Version: 0002Production Line: Display Packaging 2 |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Anonymous Forecast and MRP |  |  |  |
| [Option 1: Create Planned Independent Requirements Manually](#unique_14) | Production Planner | Maintain PIRs (F3445) | Independent Requirements for Finished Goods are created. |
| [Option 2: Create Planned Independent Requirements by Upload File](#unique_15) [page ] 20 | Production Planner | Maintain PIRs (F3445) | Independent Requirements for Finished Goods are created. |
| [Schedule pMRP Simulation Creation](#unique_16) [page ] 23 | Production Planner | Schedule pMRP Simulation Creation (F3968) | Application job is finished with no error. |
| [Process pMRP Simulations](#unique_17) [page ] 24 | Production Planner | Process pMRP Simulations(F3934) | The capacity issues are reduced. |
| [Check Planned Independent Requirements](#unique_18) [page ] 27 | Production Planner | Check Planned Independent Requirement | The PIRs for top level materials are updated into requirement plan version 00. |
| [Material Requirements Planning](#unique_19) [page ] 28 | Production Planner | Schedule MRP Runs (F1339) | MRP Run is executed. |
| Evaluate Capacity Situation |  |  |  |
| [Check Capacity Situation](#unique_20) [page ] 30 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity Bottleneck is identified. |
| [Apply Changes to Available Capacity](#unique_21) [page ] 32 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity Bottleneck is resolved. |
| Production Capacity Leveling |  |  |  |
| [Production Scheduling](#unique_22) [page ] 34 | Production Planner | Capacity Scheduling Table (F3770) | Order is rescheduled and dispatched. |
| [Review Work Center Schedules](#unique_23) [page ] 36 | Production Planner | Capacity Scheduling Board (F3951) | Capacity situation has been reviewed and adopted (optional). |
| [Review Capacity Situation](#unique_24) [page ] 37 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity situation is finally reviewed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Anonymous Forecast and MRP

#### Option 1: Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use planned independent requirements (PIRs) to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates. In Option 1 these PIRs will be created manually.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: FG0502 | Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case leave this app and access the app Create PIR, make the following entries on the Create Planned Independent Requirements: Initial screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version Active: 00Search: FG0502Choose Save and continue with step #4. |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Select Material Item | Select the material item, and choose Edit in the upper right. |  |  |
| 7 | Edit PIRs | On the screen, enter quantities per period, for example:In the upcoming several weeks, enter following values for PIR:In the upcoming several weeks, enter following values for PIR:Week 1 (current week + 2 weeks): 600 PCWeek 2 (current week + 3 weeks): 300 PCWeek 3 (current week + 4 weeks): 400 PCWeek 4 (current week + 5 weeks): 400 PCWeek 5 (current week + 6 weeks): 300 PCWeek 7 (current week + 7 week): 100 PCVersion is Active: YES | Note We recommend to check the stock for finished material before entering the PIRs (see prerequisites). If there is still stock available for FG0502, enhance the first PIR for the stock already available to generate a reproducable capacity situation (e.g. actual stock plus 250 PC). To check the stock, you can logon to the SAP Fiori launchpad as a Production Planner and open the app Manage Material Coverage - New Version (F0251A). |  |
| 8 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

#### Option 2: Create Planned Independent Requirements by Upload File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use planned independent requirements (PIRs) to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates. In Option 2 these PIRs will be loaded by Upload File.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: FG0502 | Note If no PIRs for FG0502 have been maintained in the system before, the selection is empty in the app. In that case leave this app and access the app Create PIR, make the following entries on the Create Planned Independent Requirements: Initial screen and choose Continue:Plant: 3310Period Indicator: Weekly (W)Version Active: 00Search: FG0502Choose Save and continue with step #4. |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Download template | Select the material item and choose Edit in the upper right.Choose button Download to Spreadsheet to download the template to your local work space.Afterward choose Back without saving. |  |  |
| 7 | Edit PIRs | Open the Spreadsheet in an adequate program and enter quantities per period, for example:In the upcoming several weeks, enter following values for PIR:Week 1 (current week + 2 weeks): 600 PCWeek 2 (current week + 3 weeks): 300 PCWeek 3 (current week + 4 weeks): 400 PCWeek 4 (current week + 5 weeks): 400 PCWeek 5 (current week + 6 weeks): 300 PCWeek 7 (current week + 7 week): 100 PCVersion is Active: YESSave your PIRs in the spreadsheet. | Note We recommend to check the stock for finished material before entering the PIRs (see prerequisites). If there is still stock available for FG0502, enhance the first PIR for the stock already available to generate a reproducible capacity situation (e.g. actual stock plus 250 PC). To check the stock, you can log on to the SAP Fiori launchpad as a Production Planner and open the app Manage Material Coverage - New Version (F0251A). |  |
| 8 | Upload PIRs | On the Maintain PIRs screen, choose button Upload and Edit. On the Pop Up select the file you adjusted in previous step and choose Continue. Review the uploaded data. |  |  |
| 9 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

#### Schedule pMRP Simulation Creation

Purpose

This process step shows you how to create pMRP simulation.

|  |
| --- |
| Note Besides of creating a pMRP simulation via top level materials, there are two more job templates for creating pMRP simulations. One is Creation of pMRP Data via Work center and the other is Creation of pMRP Data via Components. In this test script, we only focus on the pMRP simulation creation via top level materials. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule pMRP Simulation Creation (F3968). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Job Details | In the 1. Template Selection area, enter the following entries:Job Template: <Creation of pMRP Data via Top Level Materials>Job Name: <Creation of pMRP Data via Top Level Materials - FG0502> |  |  |
| 5 | Define Recurrence Pattern | Choose Step 2.In the 2. Scheduling Option area, maintain the following entry:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries and choose OK.Start Immediately: <select>Recurrence Pattern: Single Run | The Scheduling Information screen displays. |  |
| 6 | Enter Selection Criteria | Choose Step 3.In the Parameter Section area, make the following entries:ID for Reference Plan: 5OI_PMRP_<MMDD>_XXBucket Category: WStart Date of Reference: <Today’s date + 1 day>End Date of Reference: <Today’s date + 16 weeks>Simulation ID: 5OI_PMRP_SIM_<MMDD>_XXSimulation Description: 5OI_PMRP_SIM_<MMDD>_XXFor Object Selection sub-area:Plant: 3310Material: FG0502MRP Controller: 001For Document Data sub-area:Opening Stock: <blank> | MMDD is today’s date, for example, if the date is August 1st, then MMDD = 0801. XX is a running number, eg 01, 02 etc. |  |
| 7 | Schedule New Job | Choose Check.If there are no error messages, choose Schedule.A new job is created and displays in the Application Jobs table. | Confirm that the application job is finished with no error. Warning can be accepted for production versions 0003 and 0099 of material FG0502. |  |

#### Process pMRP Simulations

Purpose

This process step shows you how to process the created pMRP Simulation to handle bottlenecks and constraints.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Process pMRP Simulations (F3934). | The Process pMRP Simulations screen displays. |  |
| 3 | Filter the Simulation | On the Process pMRP Simulations screen, filter the simulation with the reference ID you just created and choose Go.Reference Data : 5OI_PMRP_<MMDD>_XX | The simulation displays. |  |
| 4 | Copy the Simulation | Choose the check-box of the filtered simulation, and choose Copy in the upper right corner.On the Copy screen, make the following entries and choose Copy.Copy from Current Simulation: XNew Simulation ID: 5OI_PMRP_SIMU_<MMDD>_CNew Simulation Description: 5OI_PMRP_SIMU_<MMDD>_COPYOverload Tolerance: 2% | It shows Simulation Copied.You can repeat this step to create several copies of one pMRP Simulation to figure out the best adjusted simulation. |  |
| 5 | Check the Copied Simulation | On the Process pMRP Simulations screen, choose against the row of the new copied simulation with simulation ID: 5OI_PMRP_SIMU_<MMDD>_C | The Demand Plan Simulation screen displays. |  |
| 6 | Check the Demand-Plan Simulation | On the Demand Plan Simulation screen, you can check the Capacity Issues, Delivery Performance, and Violated Constraints.You can check the demand plan simulation quantities for materials in each period, you can switch the displayed mode, for example:Simulation Table Selection: Reference /Simulation | In our scenario, we would only focus to reduce the capacity issue from top-level material FG0502If there is no capacity issue or violated constraints, skip step 7 - 15. |  |
| 7 | Check Issue Worklist | On the top of screen, choose the Capacity Issues Quantity, the Capacity Issues page displays.Choose Show in Issue List, the Issue List screen displays.In the Issues area, you could see Issue Category, Affected Objects, Affected Weeks, Affected Demands, Impact Score, Impact Cause By and Impact Cause.You could choose Clear Filter icon after Filterd by: Capacity Issues, then you could get the overall issue lists, including Violated Constraints if applicable.Optionally, you can choose one Capacity Overload issue, choose Disregard Capacity Issues. On the pop-up Disregard Capacity Issues screen, choose OK.Choose Demand Plan Simulation on the top of screen and navigate back. | The selected issues have been disregarded in this simulation.And the capacity issue quantites are reduced. |  |
| 8 | Check Capacity Plan Simulation | On the Demand Plan Simulation screen.Choose the <600> (simulation quantity) in the red box for FG0502, the Inspector area displays the relevant capacity overload issues.In the Issues area, choose Capacity Plan Simulation.On the Capacity Plan Simulation screen, you can check the Demand/Remaining Capacity in Hours in table view by default.Choose Show Work Center Overview near the top right corner of Capacity Plan Simulation screen, then it shows in graphic view.Check the overload demand in red for work center whose remaining capacity is less than zero, it indicates the capacity issue. | Continue to reduce the capacity issues or violated constraints in step 9-15. |  |
| 9 | Shift Demand | Choose one of the demands (in red if available) for the work center, for example, DP050001.In Top-Level Materials area, navigate to FG0502 for the latest week, choose Shift Demand on the right.On the Shift Top-Level Demand screen, maintain the following entry:Shift Demand To: <the earliest week>Choose Adopt Proposal, the Quantity is automatically updated with the Proposed Quantity.Choose Apply. | The capacity issues are reduced.You can choose Undo or Redo icon to withdraw or resume your changes of simulation.You can choose Show Change History icon to review all your changes in the Global Hisotry area. |  |
| 10 | Check Multi-Level Material Simulation | Choose the next demand in red for a work center, for example, DP050001.In the Top-Level Materials area, navigate to FG0502, and choose Multi-Level Material Simulation. | The Multi-Level Material Simulation screen displays. |  |
| 11 | Change Source of Supply | On the Multi-Level Material Simulation screen, you could see simulation details for BOM components in Bill of Material area.Choose Finished good FG0502, then you choose Change Source of Supply to distribute demand into different production versions to balance workload.On the Change Source of Supply screen, choose Adopt Proposal, the Quantity Distribution for two production versions are automatically updated with the Proposed Distribution, choose Apply. | The capacity issues are reduced. |  |
| 12 | Check Simulation Component | Choose Simulation Views at the top and choose Simulation Components.On the Simulation Components screen, you could see simulation quantities for both head materials and components. You can change display mode from Materials to Supply. | The Simulation Components screen displays. |  |
| 13 | Check Simulation Summary | Choose Simulation Summary at the top.On the Simulation Summary screen, you could check Change in Demand Change in Capacity, Production, Change of Source of Supply, Unresolved Issues, and Disregarded Capacity Issues. | The Simulation Summary screen displays. |  |
| 14 | Check Demand Plan Simulation Again | Choose Simulation Views at the top and navigate back to Demand Plan Simulation. | The Demand Plan Simulation screen displays. |  |
| 15 | Release Simulation | Choose Navigation Menu icon at the top left and navigate to Process pMRP Simulations.On the Process pMRP Simulations screen, filter the simulation with the reference ID and choose Go.Reference Data : 5OI_PMRP_<MMDD>_XXChoose Release for the copied simulation with less capacity issues.On the Release screen, make following entries and choose Release.Create PIRs for Demand-Driven MRP Components: unmarkedCreate PIRs for Top-Level Materials: <X>Create PIRs for Subassembly Components: <X>Requirement Version for Top-Level Materials: 00 REQUIREMENTS PLANVersion Active for Top-Level Materials: YesRequirement Version for Subassembly Components: 00 REQUIREMENTS PLANVersion Active for Subassembly Components: Yes | The simulation status is changed into Released. |  |

#### Check Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to check the adjusted PIRs for top level material FG0502. They are adjusted to ensure less capacity issues.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Material: FG0502Plant: 3310Period Indicator: Weekly (W)Version Active: Select all options |  |  |
| 5 | Filter Result | Choose Go to execute. | The material item displays. |  |
| 6 | Check PIRs | Select the filtered material items whose last modified date is today, and choose Edit in the upper-right corner.On the Edit PIRs screen, check the generated PIRs for FG0502. | The PIRs for top level materials are updated into requirement plan version 00. |  |

#### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to tailor available capacities and receipts on time to suit requirement quantities. You can use MRP or consumption-based planning for this purpose. Single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The finished material (FG0502) is planned at plant level. There is now a requirement for the finished material (FG0502) in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG0502>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Option screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: FG0502Changed BOM Components: selectScheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG0502 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

### Evaluate Capacity Situation

All orders and operations that are planned with the MRP are allocated to the required capacities. Production planners can evaluate the capacity utilization for a defined time horizon and execute manual changes in orders to resolve upcoming bottleneck situations in the defined area of responsibility.

To solve the bottleneck situation the available capacities will be adopted.

#### Check Capacity Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During MRP, planned orders are created and scheduled to meet the material requirements. This process step shows you how to check the capacities for overload on bottleneck resources.

The Work center group is used as selection criterion to cover all coffee production resources the planner is responsible for.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity (F3289) screen displays. |  |
| 3 | Check App Settings | Choose the user icon, and select App Settings.In the App Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if only following entry is assigned:Plant: 3310 ( Plant 1 AE) / MRP Controller: 001.Choose AOR status button of this entry if not assigned, click AOR status button of the corresponding entry to unassign any other entry then choose Back.Check entries for Load Personalization:Critical Load: 100%Normal Load: 80%Note You add Work Center Group as a filter by choosing Adapt Filters > More Filters (Master Data). Select Work Center Group, choose OK, and then choose Go. |  |  |
| 4 | Filter | Choose following entries as filter, and choose Go.Editing Status: AllLoad Type: OverLoadEvaluation Horizon: From today to 8 weeks afterWork Center Group: 05_COFFEEWe here only focus on capacity requirement due to PIRs we just created. | You can also use dynamic Evaluation Horizon: “Today – X / + Y days” and Overdue Horizon to calculate the overdue in a user-defined timeframe/ help checking utilization for the past.A list of bottleneck work centers with Overload situations are presented in an overview list.If no Overload work center listed, for test purpose, you can go back to Section “Create Planned Independent Requirements”, increase the PIRs for FG0502 in step 7. Then rerun the whole process.Note If you want to check all work center of the work center group 05_COFFEE, choose Load Type: All |  |
| 5 | Check Bottleneck Work Centers | Choose button Settings above table. From Columns, you can choose different KPIs.KPIs on Capacity load (e.g. Max. Load, First Overload, Total Capacity Requirement etc.) give an overview on capacity situation.Critical situations are highlighted by utilization chart. Red/Yellow/Green bar shows different percentage level of capacity utilization, with color coding according to the Critical Load/Normal Load settings. The red bar indicates the available capacity exceeds Critical Load percentage, thus there is bottleneck with the work center.Note If the button Show Details is displayed on top of the table, click on it to display all selected columns. |  |  |
| 6 | Next Step | After identifying the bottleneck work center(s), stay on this page and go on with the test as described in the next section. |  |  |

#### Apply Changes to Available Capacity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For the bottleneck work centers, you may need to optimize capacity utilization by changing available capacity, e.g., via adding/changing shifts.

|  |
| --- |
| Note If you want to apply changes to multiple work centers at once, please use the app Mass Maintenance of Work Center Capacities (F5381). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity (F3289) screen displays. |  |
| 3 | Check Capacity Situation | Check capacity utilization to identify bottleneck work center, as described in last section Check Capacity Situation. |  |  |
| 4 | Choose Bottleneck Work Center | Use the Work Center filter to filter bottleneck work centers with value help. From the displayed list, choose one of the work centers, for example:Work center: DR050001( Drum Roasting Machine 1)Capacity Category: Machine (001) |  |  |
| 5 | Check Detailed Capacity Load | Details on capacity load of the specific work center capacity can be seen on the detailed page. Different views are available for monitoring composition and source order operations of capacity load.In Overview section, Utilization Chart gives graphical presentation of capacity load for specific period. You can choose different filter to show utilization in different period. Find the specific dates or period in which bottleneck would occur.In Operations section, the list provides details on related source orders, e.g. Planned Order for FG0512 resp. FG0511.The Shift section provides a review of available capacity for the specific work center. Check the shifts on bottleneck dates and consider which shifts can be added on these dates to increase available capacity. For example, if shift YS3 is not arranged, you might consider adding YS3 on these dates for this work center. | Bottleneck dates and possible additional shifts are identified. |  |
| 6 | Choose Edit | Choose Edit in the upper right of the page. | Entries under section Shift become editable. |  |
| 7 | Add Shift | Under section Shift, choose +, and choose Add Shift. Enter following entries, and choose OK.Date Range: specific period during which you would like to add shift, dependent on the bottleneck datesShift Definition: YS3 (add other shifts if YS3 is already assigned)Recurrence: Daily | Add Shift screen pops up. |  |
| 8 | Check Shift is Added | Check items in Shift section, choose More at the bottom of the page to show more entries. Shift YS3 is added for the Date Range you specified.You can choose Settings icon above the table, to set filter e.g., Shift Definition equals to YS3, in order to shorten the list.After checking, choose Save. |  |  |
| 9 | Further Adjustment (Optional) | On the detailed Work Center Capacity screen, choose Edit in the upper right of the page.Under section Shift, you can adjust following parameters if needed, and choose Save.Shift Utilization: for example, 150%Number of Capacities: for example, 2In order to resolve your overload situation you could also use the function Copy Shifts in the Display mode of work center capacity, to copy a shift from one work center to another. |  |  |
| 10 | Check Bottleneck | Check capacity utilization in Overview section. After adding shift, capacity utilization during the specific period should be decreased, to reflect better match between requirement capacity and available capacity. Check if the bottleneck is resolved (all the bars are green), if not, please go back and repeat step 2-6 till no overload anymore. | The bottleneck is resolved. |  |
| 11 | Check Bottleneck for all the Resources | For all the other bottleneck resources, repeat step 1-7 to apply changes to available capacity.Note If you already solve all bottlenecks here, you will not have bottleneck situations available for the following Production Capacity Leveling Process. Even though you can execute capacity leveling without bottleneck situation we recommend to partly keep the bottlenecks. | The bottleneck for all resources is resolved. |  |

### Production Capacity Leveling

The process of production capacity leveling represents a central part of preparation for the manufacturing process of components. This process enables production planners to assign orders and operations from the production plan to available timeslots of capacities. Additionally, the planners can simulate and choose other alternatives for production by assigning other available production versions, letting the planners schedule the best option for their manufacturing.

#### Production Scheduling

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In preliminary steps, the planned orders are generated after MRP Run, and the capacity situation is evaluated and adjusted. This process step shows you how to assign orders and operations from the initially created production plan to available timeslots of capacities.

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Capacity Scheduling Table (F3770). |  |  |
| 3 | Check App Settings | In the App Settings dialog box, check if only below entry is assigned:For Industry Type, select the following value and choose OK:Industry Type: DiscreteIn the Basis Controls section, select Area for Responsibility. Select Plant and MRP Controller and choose Assign. Check if only below entries are assigned:Plant 1 AE (3310)MRP Controller 001 (001) |  |  |
| 4 | Filter | Choose Adapt Filters. Flag the entry Work Center Group and choose OK.Choose the following entries as filter and choose Go.Work Center Group: 05_COFFEEEvaluation Horizon: for example, next 1 monthStatus: Not Dispatched and Dispatched | Critical operation for orders which fulfill the search criteria are displayed.If the tested products are MTO relevant, choose the settings to check Sales Orders and Sales Order Items. |  |
| 5 | Choose Order | Orders for FG0511, FG0512 and FG0502 are displayed in the list. Choose the desired order you want to dispatch. | The Capacity Scheduling Table screen displays. |  |
| 6 | Check Operation Information | In the top section of the detailed screen, check the detailed information about the critical operation.. |  |  |
| 7 | Check Available Time Buckets | In the below area of the right panel, the available source of supply would display under the grid table.Use the calendar selection box to adjust the date bucket in which you need to dispatch the order.For orders producing FG0511 and FG0512, the work centers DR050001 and DR050002 can be used as alternative work centers.For orders producing FG0502, the work centers DP050001 and DP050002 can be used as alternative work centers. | The available capacity (XX H) for each day displays in the time bucket table. |  |
| 8 | Check Strategy | Choose Set Strategy in the upper right corner of the left panel. You can check relevant settings here and adjust if necessary.Planning ModeScheduling ControlDirectionIn this case, we choose the Bucket mode as an example. | There are two planning modes:Bucket: Allocate orders to first available timeslot.Sequence: Define an exact time for the order to start/end (depending on the planning direction). |  |
| 9 | Check Order Information | Under Sourcing & Scheduling section, on the right panel, choose the tab page Additional Information to check detailed order information. |  |  |
| 10 | Check Source of Supply | Under Available Sources of Supply in the bucket table, relevant production version displays. Check the production version marked as Assign. If you want to adopt some other production version instead, you can check the relevant line in the Assign column. |  |  |
| 11 | Choose Available Time Bucket | In the bucket table, choose the radio button before the available capacity (XX H) you want to assign. You may view the available capacity (XX H) by Day, Week or Shift, as well as select the date range. |  |  |
| 12 | Dispatch and Review the Dispatched Orders | Choose Dispatch.Mark the radio button in front of the available capacity once again.Choose Review Dispatched Orders to review the dispatched orders. | A message displays: Dispatch of Order XXXX Operation XXXX scheduled from XXX to XXX was successful. |  |
| 13 | Cancel Dispatch (Optional) | If you need to cancel the dispatch process, select the corresponding operation and choose Deallocate. | The Status becomes Not Dispatched. |  |
| 14 | Realign Schedules (Optional) | If you need to realign the schedule, select corresponding items and choose Realign Schedules.Note Realigning the schedule is only available on the overview screen. Choose back to return to this screen from the details view.Enter the off-set number of days and time, choose Realign (choose Save and Realign if you want to set the day and time as default). | A message Realign Schedules executed appears. For details, see Message Manager.You could choose Insert Operation for Future or Past. The offset threshold for Past is defined in App Settings > Past Threshold (Maximum of 30 days). |  |
| 15 | Choose Save | Choose Save at the bottom of the left panel. |  |  |

Result

The planned orders are rescheduled according to the available timeslot you choose.

#### Review Work Center Schedules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step enables production planner to monitor schedule status by the visualization of Gantt chart.

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Capacity Scheduling Board (F3951). |  |  |
| 3 | Filter | Choose Adapt Filters. Flag the entry Work Center Group and choose OK.Choose following entries as filter and choose Go.Horizon: for example, next 1 monthWork Center Group: 05_COFFEEStatus: Dispatched |  |  |
| 4 | Monitor Status | Monitor the schedule status in dashboard.View detailed information by selecting an operation and choosing Operation Info. |  |  |
| 5 | Adopt Planning for Work Center (Optional) | If you want to execute further adoptions in capacity planning, mark the work center you want to change capacity planning for and choose button Schedule Production. You will be moved to the Capacity Scheduling table and do further adoptions as already mentioned in previous step. |  |  |
| 6 | Adopt Planning for Operation (Optional) | If you need to execute further adoptions for an operation, select the operations on a resource you want to execute rescheduling for and choose button Manage Operation. On the Manage Operation screen, you can reschedule, deallocate and allocate operations by selecting the corresponding operations in the scheduling board and choosing an appropriate activity button on top of scheduling board.Note Only the actions which are executable with this operation are selectable.As an alternative, you can manually add a rescheduling date for the corresponding operation in the header section and choose the button Reschedule.Note The button Reschedule is only selectable when the scheduling date is changed and Enter is pressed on the keyboard. |  |  |

#### Review Capacity Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you have solved all capacity bottlenecks, you finally check the capacity situation of the work centers you are responsible for.

After this final check you can internally produce the planned orders for goods (not part of this scope item - see succeeding processes).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity (F3289) screen displays. |  |
| 3 | Check App Settings | Choose the button, App Settings above the table.In the App Settings dialog box, choose Area of Responsibility.On My Area of Responsibility screen, check if only following entry is assigned:Plant: 3310 ( Plant 1 AE) / MRP Controller: 001.Choose AOR status button of this entry if not assigned, click AOR status button of the corresponding entry to unassign any other entry then choose Back.Check entries for Load Personalization:Critical Load: 100%Normal Load: 80%Choose OK, twice. |  |  |
| 4 | Filter | If not already available, add the Work Center Group as filter, by choosing Adapt Filters. Select Work Center Group and choose OK.Choose following entries as filter, and choose Go.Editing Status: AllLoad Type: AllEvaluation Horizon: From today to 8 weeks afterWork Center Group: 05_COFFEE | You can also use dynamic Evaluation Horizon: “Today – X / + Y days” and Overdue Horizon to calculate the overdue in a user-defined timeframe/ help checking utilization for the past.A list of all work centers of the work center group 05_COFFEE are displayed. |  |
| 5 | Check Work Centers | Choose Settings from above table. From Columns, you can choose different KPIs.KPIs on Capacity load (e.g. Max. Load, First Overload, Total Capacity Requirement etc.) give an overview on capacity situation.Check capacity utilization in Overview section. Capacity changes and capacity leveling should result in a better match between requirement capacity and available capacity. Check if the bottlenecks are resolved (all the bars are green).If there are still red bars available, you can repeat the steps in the section Apply changes to Available Capacity or Production Capacity Leveling and check again. You can follow this logic until all bottlenecks are resolved. |  |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| 5HK - Quality Management in Discrete Manufacturing – Consumer Products | You can follow this test script to execute the production process for the finished materials. |
| 5HL - Sell from Stock – Consumer Products | You can follow the test script to sell the produced displays and cartons with coffee bean bags from this scope items to the customer (can be executed if optional steps for production order processing have been executed). |
| 5W3 - Procurement of Production Components – Consumer Products | To purchase the raw and packaging materials, you can follow the test script. |
| 5W4 - Subcontracting – Consumer Products | You can follow this test script to execute the production process for the finished material FG0502 as subcontracting process. |
| 3F0 - Event-Based Production Cost Posting | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to BEI - Period-End Closing – Plant till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

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
- related-to :: [[12-production-and-manufacturing/test-script-capacity-planning-evaluation-scope-item-31l-sap-s-4hana-cl]]
- related-to :: [[12-production-and-manufacturing/test-script-production-capacity-leveling-3lq-ae-sap-s-4hana-cloud-publ]]
- see-also :: [[08-sales-order-management/customer-returns-management-consumer-products-61v-ae-test-script-sap-s]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OI_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 70,435 chars in the whole document
