---
id: 12-production-and-manufacturing/test-script-capacity-planning-evaluation-scope-item-31l-sap-s-4hana-cl
title: "Test Script - Capacity Planning Evaluation (scope item 31L), SAP S/4HANA Cloud Public Edition 2608 (31L_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for capacity evaluation in make-to-stock Discrete and Process Manufacturing: PIRs, MRP, bottleneck check, shift changes, order conversion."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/capacity-evaluation-and-leveling]
aliases: [31L_S4CLD2608_BPD_EN_AE]
keywords: [Capacity Evaluation and Leveling, capacity planning evaluation, planned independent requirements, material requirements planning, work center capacity, capacity bottlenecks, planned order conversion, work center groups, discrete manufacturing, process manufacturing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31L_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-894
topic: 12-production-and-manufacturing/capacity-evaluation-and-leveling
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script - Capacity Planning Evaluation (scope item 31L), SAP S/4HANA Cloud Public Edition 2608 (31L_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31L_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Capacity Evaluation and Leveling** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | **Error! Reference source not found.**Purpose PUBLIC 1 **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851282)

[2 Prerequisites 4](#_Toc232851283)

[2.1 System Access 4](#_Toc232851284)

[2.2 Roles 4](#_Toc232851285)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232851286)

[2.4 Business Conditions 10](#_Toc232851287)

[2.5 Preliminary Steps 11](#_Toc232851288)

[2.5.1 Preliminary Steps for Discrete Manufacturing 11](#_Toc232851289)

[2.5.1.1 Create Initial Material Stock 11](#_Toc232851290)

[2.5.1.2 Check Available Capacity in Work Center 12](#_Toc232851291)

[2.5.1.3 Create and Assign Work Center Group 14](#_Toc232851292)

[2.5.2 Preliminary Steps for Process Manufacturing 15](#_Toc232851293)

[2.5.2.1 Create Initial Material Stock 15](#_Toc232851294)

[2.5.2.2 Check Available Capacity in Resource 16](#_Toc232851295)

[3 Overview Table 18](#_Toc232851296)

[4 Test Procedures 20](#_Toc232851297)

[4.1 Capacity Planning Evaluation for Discrete Manufacturing 20](#_Toc232851298)

[4.1.1 Create Planned Independent Requirements 20](#_Toc232851299)

[4.1.2 Material Requirements Planning 21](#_Toc232851300)

[4.1.3 Evaluate Capacity Situation 23](#_Toc232851301)

[4.1.3.1 Check Capacity Situation 23](#_Toc232851302)

[4.1.3.2 Apply Changes to Available Capacity 25](#_Toc232851303)

[4.1.4 Conversion to Production Orders 27](#_Toc232851304)

[4.1.5 Production Order Processing for Subassembly 28](#_Toc232851305)

[4.1.6 Production Order Processing for Final Assembly 29](#_Toc232851306)

[4.1.7 Evaluate Capacity (Optional) 30](#_Toc232851307)

[4.2 Capacity Planning Evaluation for Process Manufacturing 31](#_Toc232851308)

[4.2.1 Create Planned Independent Requirements 31](#_Toc232851309)

[4.2.2 Material Requirements Planning 33](#_Toc232851310)

[4.2.3 Evaluate Capacity Situation 35](#_Toc232851311)

[4.2.3.1 Check Capacity Situation 35](#_Toc232851312)

[4.2.3.2 Apply Changes to Available Capacity 36](#_Toc232851313)

[4.2.4 Conversion to Process Orders 38](#_Toc232851314)

[4.2.5 Process Order Processing 39](#_Toc232851315)

[5 Appendix 41](#_Toc232851316)

[5.1 Succeeding Processes 41](#_Toc232851317)

## Purpose

Overview

This scope item enables quick capacity evaluation and planning for make-to-stock scenarios in Discrete and Process Manufacturing. You can determine the industry type selection and displayed data in the app settings.

The process starts with the creation of a demand forecast for finished goods represented by Planned Independent Requirements (PIRs). Based on PIRs, Material Requirements Planning (MRP) creates a production plan for finished goods and explodes the entire bill of material structure.

As a result, semifinished component production and raw material demand is planned. All orders and operations that are planned with the MRP are allocated to the required capacities. Production planners can evaluate the capacity utilization for a defined time horizon and execute manual changes in orders to resolve upcoming bottleneck situations in the defined area of responsibility.

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
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |
| Production Engineer - Process Manufacturing | SAP_BR_PRODN_ENG_PROC | Production Engineering - Process Manufacturing | SAP_BR_PRODN_ENG_PROC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Master Data for Discrete Manufacturing

This section describes sample Master Data for Discrete Manufacturing. Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG1_CP | CP-FG1, Shaft with Rolling Bearings |  |
| Material | SG1_CP | CP-SG1, Shaft |  |
| Material | RM1_CP | CP-RM1, Steel |  |
| Material | RM2_CP | CP-RM2, Rolling Bearing |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristics of Material |
| --- | --- | --- | --- | --- |
| FG1_CP | 0 | FERT | PC | Finished Good |
| SG1_CP | 1 | SEMI | PC | Semi-finished Goods |
| RM1_CP | 2 | RAW | PC | Raw material, component for SG1_CP |
| RM2_CP | 2 | RAW | PC | Raw material |

Work Center

This overview shows work centers used for this scenario.

| Work Center | Description |
| --- | --- |
| TURNING1 | CP-WC1, Turning 1 |
| TURNING2 | CP-WC2, Turning 2 |
| TURNING9 | CP-WC2 (Alt), Turning 9 |
| DRILING | CP-WC3, Drilling |
| FINICLN | CP-WC4, FINISHING AND CLEANING |
| ASSPKG | CP-WC5, ASSEMBLY AND PACKAGING |
| ASSPKG9 | CP-WC5 (Alt), ASSEMBLY AND PACKAGING 9 |

Routing

This overview shows Routing for Semi-finished goods and Finished goods.

| Material | Operation | Description | Work Center |
| --- | --- | --- | --- |
| SG1_CP | 0010 | Turning Machine 1 | TURNING1 |
| SG1_CP | 0020 | Turning Machine 2 | TURNING2 |
| SG1_CP | 0030 | Drilling machine | DRILING |
| SG1_CP | 0040 | Finishing | FINICLN |
| SG1_CP | 0050 | Clearing | FINICLN |
| FG1_CP | 0010 | Assembly | ASSPKG |
| FG1_CP | 0020 | Finish and clean | FINICLN |

Available capacity for work center

This overview shows predefined shifts.

| Shift | Start time | End time | Length of break |
| --- | --- | --- | --- |
| YS1, Early Shift | 06:00:00 | 14:00:00 | 00:30:00 |
| YS2, Late Shift | 14:00:00 | 22:00:00 | 00:30:00 |
| YS3, Night Shift | 22:00:00 | 06:00:00 | 00:30:00 |

For more information about creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Master Data for Process Manufacturing

This section describes sample Master Data for Process Manufacturing. Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG2_CP | CP-FG2, Ink Bottled, 15 ml |  |
| Material | SG2_CP | CP-SG2, Ink Bottled |  |
| Material | RM5_CP | CP-RM5, Varnish |  |
| Material | RM7_CP | CP-RM7, Label |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Material | Level | Material Type | Unit | Characteristics of Material |
| --- | --- | --- | --- | --- |
| FG2_CP | 0 | FERT | PC | Finished Good |
| SG2_CP | 1 | SEMI | PC | Semi-finished Goods |
| RM5_CP | 2 | RAW | PC | Raw material, component for SG2_CP |
| RM7_CP | 1 | RAW | PC | Raw material |

Resource

This overview shows sample Resources for Process Manufacturing.

| Resource | Description |
| --- | --- |
| MIX01_CP | CP-RES01, Ink Mixing 01 |
| BOT01_CP | CP-RES02, Bottling 01 |
| BOT02_CP | CP-RES03, Bottling 02 (ALT) |
| PAC01_CP | CP-RES04, Ink Packing 01 |
| PAC02_CP | CP-RES05, Ink Packing 02 (ALT) |

Master Recipe

This overview shows Master Recipe for Semi-finished goods and Finished goods for Process Manufacturing.

| Material | Operation | Phase | Description | Resource | Resource (alternative) |
| --- | --- | --- | --- | --- | --- |
| SG2_CP | 0010 |  | Mixing Operation | MIX01_CP |  |
| SG2_CP | 0020 | X | Mixing Phase | MIX01_CP |  |
| SG2_CP | 0030 |  | Bottling Operation | BOT01_CP | BOT02_CP |
| SG2_CP | 0040 | X | Bottling Phase 1 | BOT01_CP | BOT02_CP |
| SG2_CP | 0050 | X | Bottling Phase 2 | BOT01_CP | BOT02_CP |
| FG2_CP | 0010 |  | Packing Operation | PAC01_CP | PAC02_CP |
| FG2_CP | 0020 | X | Packing Phase | PAC01_CP | PAC02_CP |

Available capacity for work center

This overview shows predefined shifts.

| Shift | Start time | End time | Length of break |
| --- | --- | --- | --- |
| YS1, Early Shift | 06:00:00 | 14:00:00 | 00:30:00 |
| YS2, Late Shift | 14:00:00 | 22:00:00 | 00:30:00 |
| YS3, Night Shift | 22:00:00 | 06:00:00 | 00:30:00 |

For more information about creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS - relevant for Discrete Manufacturing and Process Manufacturing |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS - relevant for Discrete Manufacturing and Process Manufacturing |
| BNT | Create Product Master of type "Finished Good" - MDS - relevant for Discrete Manufacturing and Process Manufacturing |
| BNJ | Create Production Work Center - MDS - relevant for Discrete Manufacturing |
| BNK | Create Material BOM for Production and Sales - MDS - relevant for Discrete Manufacturing and Process Manufacturing |
| BNL | Create Routing - MDS - relevant for Discrete Manufacturing |
| BLD | Create Production Version - MDS - relevant for Discrete Manufacturing and Process Manufacturing |
| 3X8 | Create Resource - MDS - relevant for Process Manufacturing |
| 3X9 | Create Master Recipe - MDS - relevant for Process Manufacturing |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Test Script Standard Cost Calculation (BEG) |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up-to-date. |

Activate Features

In a software update, SAP delivers certain features that could have an impact on your implemented solution initially in an inactive state. You can choose to already activate these features before they become available by default in a later release.

The test procedures in this document describe the software behavior when all features have been activated. It is a prerequisite for testing that you have activated all of the following features in each of your systems using the configuration activity Activate Features. For more information about this activity, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/3e94fcc37b42433b97d6aef0c830dc52.html) for SAP S/4HANA Cloud Public Edition.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution. Search for Activate Features. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Features. Choose the link to navigate directly to the target system of SAP S/4HANA Cloud Public Edition. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

| Feature ID | Feature Title |
| --- | --- |
| FTGL_2602_LINEMICROCHART | Feature toggle for the line micro chart on the LR page. |

### Preliminary Steps

#### Preliminary Steps for Discrete Manufacturing

##### Create Initial Material Stock

Purpose

In a real business case, the materials are usually purchased from external suppliers in that case, process is covered by the standard purchasing or subcontracting processes. This process step shows you how to post initial stock directly to the storage locations for raw materials RM1_CP and RM2_CP.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). |  |  |
| 3 | Input Material | Make the following entries and press Enter:Material: RM1_CPPlant: Plant 1 AE (3310) |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock:Storage Location: Raw mat. stoloc. (331C)Unrestricted-Use Stock | The Manage Stock dialog box opens. The Storage Location, Stock Type and Current Quantity are displayed according to your entries in previous steps. |  |
| 5 | Add Initial Stock | Make the following entries and choose Post:Stock Change: Initial EntryQuantity: Enter a number, for example, 1000Document Date: <Today>Posting Date: <Today> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

We recommend that you check the stock for SG1_CP and FG1_CP . To check, log on to the SAP Fiori launchpad as a Production Planner and open Manage Stock (F1062). If there is sufficient stock, remove some stock; otherwise, no plan orders are generated later. After removing some stock, run the test again.

You can either post initial stock directly to the storage location or refer to test scripts Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR).

##### Check Available Capacity in Work Center

Purpose

In the Best Practice pre-delivered contents, standard available capacity is applied to the work centers, and no shifts are assigned initially. In case these values have been adjusted during test, we recommend that you have a check to have better understanding of current available capacity for work center TURNING1, TURNING2, DRILING, FINICLN and ASSPKG.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Work Center (CR02). | The Change Work Center: Initial Screen displays.You can also add this app to the main page if it’s not listed: Choose the user icon, and select App Finder. Click the plus icon of Change Work Center to add the tile. |  |
| 3 | Enter Plant and Work Center | On the Change Work Center (CR02) screen, make the following entries, and press Enter:Plant: 3310Work Center: <Work Center>, for example, TURNING1, TURNING2, DRILING, FINICLN and ASSPKG |  |  |
| 4 | Choose Capacity Category 001 | Choose the Capacities tab, and you can find there are two capacity categories defined: 001 and 002.Double-click Capacity category: 001 | The Change Work Center Capacity: Header screen displays. |  |
| 5 | Check Standard Available Capacity | On the Change Work Center Capacity: Header screen for capacity 001, check standard available capacity. The following values are pre-set in this test scenario:Start time: 07:00:00End time: 16:00:00Length of breaks: 01:00:00Capacity Utilization: 100No. Ind. Capacities: 1For test purpose, we recommend using the same values as above. |  |  |
| 6 | Check Intervals and Shifts | Choose Intervals and Shifts in the upper left corner.On the Change Work Center Capacity: Intervals of Available Capacity screen for capacity 001, available shifts are listed in the table at the bottom of the page. We recommend deleting any additional shifts effective within next 6 weeks.Choose any line you want to delete, and then choose Delete in the upper right corner.Choose Back twice to screen Change Work Center: Capacity Overview. |  |  |
| 7 | Choose Capacity Category 002 | Under the Capacities tab, double-click Capacity category: 002. | The Change Work Center Capacity: Header screen displays. |  |
| 8 | Check Default Settings for Capacity Category 002 | Repeat step #5 and #6 for category 002. |  |  |
| 9 | Save | Choose Save. | Work center XXX in plant 3310 was changed. |  |

##### Create and Assign Work Center Group

Purpose

Before you perform the step [Evaluate Capacity (Optional)](#unique_10) [page ] 30 and evaluate capacity at work center group level, you need to create relevant Work Center Groups.

Additional required Master Data Work Center Groups can be created by following the description in master data script BNJ:

- Step Create Work Center Group (Optional): This process step shows you how to create work center group.
- Step Assign Work Center (Optional): This process step shows you how to assign work centers to work center group.

By following the preceding BNJ steps, you can manually create the following sample Work Center Groups.

| Work Center Group | Description | Work Center Group Type | Plant | Assigned Work Centers |
| --- | --- | --- | --- | --- |
| TURN_ALT | Alternative Machines | ALTERNATIV | 3310 |  |
|  |  |  |  | TURNING2 |
|  |  |  |  | TURNING9 |
| CP_SG1 | Same Line for SG1 | SAME LINE | 3310 |  |
|  |  |  |  | TURNING1 |
|  |  |  |  | TURNING2 |
|  |  |  |  | DRILING |
|  |  |  |  | FINICLN |

#### Preliminary Steps for Process Manufacturing

##### Create Initial Material Stock

Purpose

In a real business case, the materials are usually purchased from external suppliers in that case, process is covered by the standard purchasing or subcontracting processes. For the purpose of this test, we post initial stock directly to the storage locations. This process step shows you how to post initial stock directly to the storage locations for raw materials RM5_CP and RM7_CP.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). |  |  |
| 3 | Input Material | Make the following entries and press Enter:Material: RM5_CPPlant: Plant 1 AE (3310) |  |  |
| 4 | Select Stock | Choose Add Storage Location, search and select Raw mat. stoloc. (331C)Choose the icon beside the Unrestricted-Use Stock in the storage location where you want to add initial stock. | The Manage Stock dialog box opens.The Storage Location, Stock Type and Current Quantity are displayed according to your entries in previous steps. |  |
| 5 | Add Initial Stock | Make the following entries and choose Post:Stock Change: Initial EntryQuantity: Enter a number, for example, 1000Document Date: <Today>Posting Date: <Today> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

We recommend that you check the stock for SG2_CP and FG2_CP. To check, log on to the SAP Fiori launchpad as a Production Planner and open Manage Material Coverage - New Version (F0251A). If there is sufficient stock, remove some stock; otherwise, no plan orders are generated later. After removing some stock, run the test again.

You can either post initial stock directly to the storage location or refer to the test scripts Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR).

##### Check Available Capacity in Resource

Purpose

In the Best Practice pre-delivered contents, standard available capacity is applied to the resources, and no shifts assigned initially. In case these values have been adjusted during test, we recommend that you have a check to have better understanding of current available capacity for resources MIX01_CP, BOT01_CP, BOT02_CP, PAC01_CP and PAC02_CP.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Resource (CRC2). | The Change Resource: Initial Screen displays.You can also add this app to the main page if it’s not listed: Choose the user icon, and select App Finder. Click the plus icon of Change Resource to add the tile. |  |
| 3 | Enter Plant and Work Center | On the Change Resource: Initial Screen, make the following entries, and press Enter:Plant: 3310Resource: <resource>, for example, MIX01_CP, BOT01_CP, BOT02_CP, PAC01_CP and PAC02_CP |  |  |
| 4 | Choose Capacity Category 001 | Choose the Capacities tab, and you can find there are two capacity categories defined: 001 and 002.Double-click Capacity category: 001 | The Change Resource Capacity: Header screen displays. |  |
| 5 | Check Standard Available Capacity | On the Change Resource Capacity: Header screen for capacity 001, check standard available capacity. The following values are pre-set in this test scenario:Start time: 07:00:00End time: 16:00:00Length of breaks: 01:00:00Capacity Utilization: 100No. Ind. Capacities: 1Active Version: 1For test purpose, we recommend using the same values as above. |  |  |
| 6 | Check Intervals and Shifts | Choose Intervals and Shifts in the upper left corner.On the Change Resource Capacity: Intervals of Available Capacity screen for capacity 001, available shifts are listed in the table at the bottom of the page. We recommend deleting any additional shifts effective within next six weeks.Choose any line you want to delete, then choose Delete in the upper right.Choose Back twice to screen Change Resource: Capacity Overview. |  |  |
| 7 | Choose Capacity Category 002 | Under the Capacities tab, double-click Capacity category: 002 | The Change Resource Capacity: Header screen displays. |  |
| 8 | Check Default Settings for Capacity Category 002 | Repeat step 5 and 6 for category 002 |  |  |
| 9 | Save | Choose Save | Resource XXX in plant 3310 is changed. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Capacity Planning Evaluation for Discrete Manufacturing |  |  |  |
| [Create Planned Independent Requirements](#unique_14) [page ] 20 | Production Planner | Maintain PIRs (F3445). | Independent Requirements for Finished Goods are created. |
| [Material Requirements Planning](#unique_15) [page ] 21 | Production Planner | Schedule MRP Runs (F1339) | MRP Run is executed. |
| Evaluate Capacity Situation |  |  |  |
| [Check Capacity Situation](#unique_16) [page ] 23 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity Bottleneck is identified. |
| [Apply Changes to Available Capacity](#unique_17) [page ] 25 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity Bottleneck is resolved. |
| [Conversion to Production Orders](#unique_18) [page ] 27 | Production Planner | Manage Material Coverage - New Version (F0251A) | Production Order is created. |
| [Production Order Processing for Subassembly](#unique_19) [page ] 28 | Refer to Scope Item BJ5 | Refer to Scope Item BJ5 | Semifinished goods are produced. |
| [Production Order Processing for Final Assembly](#unique_20) [page ] 29 | Refer to Scope Item BJ5 | Refer to Scope Item BJ5 | Finished goods are produced. |
| [Evaluate Capacity (Optional)](#unique_10) [page ] 30 | Production Planner | Evaluate Capacity (F6798) | Capacity at work center group level is evaluated. |
| Capacity Planning Evaluation for Process Manufacturing |  |  |  |
| [Create Planned Independent Requirements](#unique_21) [page ] 31 | Production Planner | Maintain PIRs (F3445) | Independent Requirements for Finished Goods are created. |
| [Material Requirements Planning](#unique_22) [page ] 33 | Production Planner | Schedule MRP Runs (F1339). | MRP Run is executed. |
| Evaluate Capacity Situation |  |  |  |
| [Check Capacity Situation](#unique_23) [page ] 35 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity Bottleneck is identified. |
| [Apply Changes to Available Capacity](#unique_24) [page ] 36 | Production Planner | Manage Work Center Capacity (F3289) | The Capacity Bottleneck is resolved. |
| [Conversion to Process Orders](#unique_25) [page ] 38 | Production Planner | Manage Material Coverage - New Version (F0251A). | Process Order is created. |
| [Process Order Processing](#unique_26) [page ] 39 | Refer to Scope Item BJ8 | Refer to Scope Item BJ8 | Semifinished goods and finished goods are produced. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Capacity Planning Evaluation for Discrete Manufacturing

#### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use planned independent requirements to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates.

|  |
| --- |
| Note Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 002 (002)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: FG1_CP |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Select Material Item | Select the material item, and choose Edit in the upper right. |  |  |
| 7 | Edit PIRs | On the screen, enter quantities per period, for example:In the upcoming several weeks, enter following values for PIR:Week 1 (current week + 2 weeks): 20 PC.Week 2 (current week + 3 weeks): 20 PC.Week 3 (current week + 4 weeks): 100 PC.Week 4 (current week + 5 weeks): 100 PC.Version Active: YES |  |  |
| 8 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

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

The finished product for MTS ( FG1_CP ) is planned at plant level. There is now a requirement for the material Finished Product MTS ( FG1_CP ) in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG1_CP >Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Option screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: FG1_CPChanged BOM Components: selectScheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG1_CP in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate Capacity Situation

##### Check Capacity Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During MRP, planned orders are created and scheduled to meet the material requirements. This process step shows you how to check the capacities for overload on bottleneck resources.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity (F3289) screen displays. |  |
| 3 | Check App Settings | Choose the user icon, and select App Settings.In the App Settings dialog box, expand Area of Responsibility. Choose Plant and MRP Controller, and choose Assign.On the My Area of Responsibility screen, check if only the following entry is assigned:Plant: 3310 ( Plant 1 AE) / MRP Controller: 002.Choose the AOR status button of this entry if not assigned. Choose the AOR status button of the corresponding entry to unassign any other entries, and then choose Back.Choose the user icon, and select App Settings.Choose Work Center Group and choose Assign. Select work center group 05_COFFEE for plant 3310 ( Plant 1 AE). Choose Assign and choose Back.Choose the user icon, and select App Settings.Check entries for Load Personalization:Critical Load: 100%Normal Load: 80% |  |  |
| 4 | Filter | Make the following entries as filters, and choose Go.Editing Status: AllLoad Type: OverloadEvaluation Horizon: From today to 8 weeks afterWork Center: TURNING1, TURNING2 , TURNING9 , DRILING, FINICLN, ASSPKG , ASSPKG9We here only focus on capacity requirement due to PIRs we just created.Note You add Work Center Group as a filter by choosing Adapt Filters > More Filters (Master Data). Select Work Center Group, and choose OK. | You can also use dynamic Evaluation Horizon: “Today – X / + Y days” and Overdue Horizon to calculate the overdue in a user-defined time frame/help checking utilization for the past.A list of bottleneck work centers with Overload situations are presented in an overview list.If no Overload work center listed, for test purpose, you can go back to Section “Create Planned Independent Requirements”, increase the PIRs for FG1_CP in step 7. Then rerun the whole process. |  |
| 5 | Check Bottleneck Work Centers | Choose the Settings icon in the upper-right corner of the table. From Columns, you can select different KPIs.KPIs on capacity load (e.g. Max. Load, First Overload, Total Capacity Requirement etc.) give an overview on capacity situation.Critical situations are highlighted by utilization chart. The red/yellow/green dots on the chart show different percentage levels of capacity utilization. The color coding corresponds to the Critical Load and Normal Load settings. A red dot indicates that the available capacity exceeds Critical Load percentage, indicating a bottleneck at the work center. The utilization below the horizontal line represents the Normal Load or Critical Load.You can view the utilization percentage for the specified date range within the evaluation horizon by clicking on the micro line chart.Note If the button Show Details is displayed on top of the table, choose it to display all selected columns. |  |  |
| 6 | Continue with Next Step | After identifying the bottleneck work centers, stay on this page and go on with the test as described in the next section. |  |  |

##### Apply Changes to Available Capacity

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
| 4 | Choose Bottleneck Work Center | Use the Work Center filter to filter bottleneck work centers with value help. From the displayed list, choose one of the work centers, for example:Work Center: TURNING1 (CP-WC1, Turning 1)Capacity Category: Machine (001) |  |  |
| 5 | Check Detailed Capacity Load | Details on capacity load of the specific work center capacity can be seen on the detailed page. Different views are available for monitoring composition and source order operations of capacity load.In Overview section, Utilization Chart gives graphical presentation of capacity load for specific period. You can choose different filter to show utilization in different period. Find the specific dates or period in which bottleneck would occur.In Operations section, the list provides details on related source orders, e.g. Planned Order for SG1_CP resp. .The Shift section provides a review of available capacity for the specific work center. Check the shifts on bottleneck dates and consider which shifts can be added on these dates to increase available capacity. For example, if shift YS3 is not arranged, you might consider adding YS3 on these dates for this work center. | Bottleneck dates and possible additional shifts are identified. |  |
| 6 | Choose Edit | Choose Edit in the upper right of the page. | Entries under section Shift become editable. |  |
| 7 | Add Shift | Under section Shift, choose +, and choose Add Shift. Enter following entries, and choose OK.Date Range: specific period during which you would like to add shift, dependent on the bottleneck datesShift Definition: YS3 (add other shifts if YS3 is already assigned)Recurrence: Daily | Add Shift screen pops up. |  |
| 8 | Check Shift is Added | Check items in Shift section, choose More at the bottom of the page to show more entries. Shift YS3 is added for the Date Range you specified.You can choose Settings icon above the table, to set filter e.g., Shift Definition equals to YS3, in order to shorten the list.After checking, choose Save. |  |  |
| 9 | Further Adjustment (Optional) | On the detailed Work Center Capacity screen, choose Edit in the upper right of the page.Under section Shift, you can adjust following parameters if needed, and choose Save.Shift Utilization: for example, 120%Number of Capacities: for example, 2In order to resolve your overload situation you could also use the function Copy Shifts in the Display mode of work center capacity, to copy a shift from one work center to another. |  |  |
| 10 | Check Bottleneck | Check capacity utilization in Overview section. After adding shift, capacity utilization during the specific period should be decreased, to reflect better match between requirement capacity and available capacity. Check if the bottleneck is resolved (all the bars are green), if not, please go back and repeat step 2-6 till no overload anymore. | The bottleneck is resolved. |  |
| 11 | Check Bottleneck for all the Resources | For all the other bottleneck resources, repeat step 1-7 to apply changes to available capacity. | The bottleneck for all resources is resolved. |  |

#### Conversion to Production Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to internally produce the planned orders for goods after capacity bottleneck is resolved.

Prerequisite

The MRP run has generated planned orders for material Subassembly ( SG1_CP ) and Final Assembly ( FG1_CP ).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | Make the following entries, and then choose Go.Material: FG1_CPPlant: 3310Shortage Definition: MRP Standard | The material item displays. |  |
| 4 | Find Planned Order | Choose the material item, and then find the generated planned order on the right screen. | Order information displays. |  |
| 5 | Convert Planned Order to Production Order | From the dropdown list next to the planned order, select Convert. Confirm date and quantity, and choose Convert.Repeat step#2 to #5 for SG1_CP . | The production order is created. |  |

#### Production Order Processing for Subassembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute the scope item BJ5 for complete processing of production for semi-finished products: SG1_CP.

Procedure

Complete all the activities under “Production Order Processing for Subassembly” described in the Test Script of the scope item: Make-to-Stock Production – Discrete Manufacturing (BJ5), including:

Material Staging for Subassembly

Release Production Order for Subassembly

Confirm Production Operations for Subassembly

Post Goods Receipt for Subassembly Production Order

Result

Semifinished goods SG1_CP is produced.

#### Production Order Processing for Final Assembly

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute the scope item BJ5 for complete processing of production for Finished products: FG1_CP.

Procedure

Complete relevant activities under “Production Order Processing for Final Assembly” described in the Test Script of the scope item: Make-to-Stock Production - Discrete Manufacturing (BJ5), including:

Material Staging for Final Assembly

Release Production Order for Final Assembly

Pick Components for Final Assembly

Confirm Production Operations for Final Assembly

Post Goods Receipt for Final Assembly Production Order

Result

Finished goods FG1_CP is produced.

#### Evaluate Capacity (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This is an optional step. If you want to evaluate capacity at work center group level, you must have work center groups. You can create the demo work center groups in [Create and Assign Work Center Group](#unique_9) [page ] 14 according to step Manage Work Center Groups (Optional) in MDS BNJ. In this step, you can evaluate capacity at work center group level.

If you have no work center group, please skip this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |
| 2 | Access the App | Open Evaluate Capacity (F6798). | The Evaluate Capacity screen displays. |
| 3 | Check App Settings | Choose the user icon, and select App Settings.In the App Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility – Work Center Groups screen, make the following entry to filter work center groups and then choose Go:Plant: 3310 ( Plant 1 AE)In the AOR Status column, choose AOR status button to set status AOR Is Assigned for critical work center groups if not assigned, and choose the AOR status button to unassign any other uncritical work center groups if assigned originally. Then choose Back.Choose the user icon, and select App Settings.In the App Settings dialog box, choose Configure Thresholds/Colors.Maintain entries for Load Personalization:Critical Load: 100%Normal Load: 80%Maintain entries for Focus Situation – Same Line and choose OK.Immediate Focus: 3Focus: 2 | Please assign AOR Status for at least one work center group. If not, you cannot see any results on the Evaluate Capacity screen.You can change thresholds by yourself. |
| 4 | Evaluate Capacity for Alternative Groups | On the Evaluate Capacity screen, make the following entries and choose Go:Evaluate Horizon: Today -0/+30 daysBucket Type: WeekWork Center Group Type: Alternative Groups & Work CentersThe alternative work center groups display in chart view by default; choose the Chart and Table View icon, and then the Operations table displays.If the utilization for the week is in red/yellow, choose this time period, choose View by and select Work Center, and then you can see detailed utilization for each work center in this group.Choose Time Period. | The Alternative work center groups display.If the type of the work center group assigned with AOR status is Same Line, there are no results displayed in this step. |
| 5 | Evaluate Capacity for Same Line Groups | On the Evaluate Capacity screen, make the following entries and choose Go:Evaluate Horizon: Today -0/+30 daysBucket Type: WeekWork Center Group Type: Same Line Groups & Work CentersThe Same Line work center groups display in chart view by default; choose the Chart and Table View icon, and then the Operations table displays.If several work centers need focus in the week which is in red/yellow, choose such time period, choose View by and select Work Center, and then you can see detailed utilization for each work center in this group.Choose Time Period. | The Same Line work center groups display.If the type of the work center group assigned with AOR status is Alternative, there are no results displayed in this step. |

### Capacity Planning Evaluation for Process Manufacturing

#### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use planned independent requirements used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, such as one planned quantity split over time according to dates.

Instead of creating a single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 002 (002)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: FG2_CP |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Select Material Item | Select the material item, and choose Edit in the upper-right corner. |  |  |
| 7 | Edit PIRs | On the screen, enter quantities per period, for example:In the upcoming several weeks, enter the following values for PIR:Week 1 (current week + 2 weeks): 500 BT.Week 2 (current week + 3 weeks): 500 BT.Week 3 (current week + 4 weeks): 1500 BT.Week 4 (current week + 5 weeks): 1500 BT.Version Active: YES |  |  |
| 8 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

#### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use material requirement planning to tailor available capacities and receipts on time to suit requirement quantities. You can use MRP or consumption-based planning for this purpose. Single-item multi-level requirement planning is performed for plant 3310.

Prerequisite

The finished product for MTS (FG2_CP) is planned at plant level. There is now a requirement for the material Finished Product MTS in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG2_CP>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Option screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.Choose 4 Parameters and make the following entries:Plant: 3310Material: FG2_CPChanged BOM Components: <select>Scheduling: 2Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG2_CP in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate Capacity Situation

##### Check Capacity Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During MRP, planned orders are created and scheduled to meet the material requirements. In this activity, the capacities are checked for overload on bottleneck resources.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity screen displays. |  |
| 3 | Check App Settings | On the Manage Work Center Capacity screen, choose your user icon and select App Settings.In the App Settings dialog box, expand Area of Responsibility. Choose Plant and MRP Controller, and choose Assign.On the My Area of Responsibility screen, check if only the following entry is assigned:Plant 1 AE (3310)MRP Controller 002 (002)Choose the AOR status button of this entry if not assigned. Choose the AOR status button of the corresponding entry to unassign any other entries, and then choose Back.Choose your user icon and select App Settings.Check entries for Load Personalization:Critical Load:100%Normal Load: 80% |  |  |
| 4 | Filter | Make the following entries as filters, and choose Go.Editing Status: AllLoad Type: OverloadEvaluation Horizon: From today to 42 days or moreWork Center: MIX01_CP, BOT01_CP, BOT02_CP, PAC01_CP, PAC02_CPWe here only focus on capacity requirement due to PIRs we just created. | You can also use dynamic Evaluation Horizon: “Today – X / + Y days” and Overdue Horizon to calculate the overdue in a user-defined time frame/help checking utilization for the past.A list of bottleneck work centers with Overload situations are presented in an overview list.If no Overload work center listed, for test purpose, you can go back to Section “Create Planned Independent Requirements”, increase the PIRs for FG2_CP in step 7. Then rerun the whole process. |  |
| 5 | Check Bottleneck Work Centers | Choose the Settings icon in the upper-right corner of the table. From Columns, you can select different KPIs.KPIs on capacity load (e.g. Max. Load, First Overload, Total Capacity Requirement etc.) give an overview on capacity situation.Critical situations are highlighted by utilization chart. The red/yellow/green dots on the chart show different percentage levels of capacity utilization. The color coding corresponds to the Critical Load and Normal Load settings. A red dot indicates that the available capacity exceeds Critical Load percentage, indicating a bottleneck at the work center. The utilization below the horizontal line represents the Normal Load or Critical Load.You can view the utilization percentage for the specified date range within the evaluation horizon by clicking on the micro line chart. |  |  |
| 6 | Continue with Next Step | After identifying the bottleneck work centers, stay on this page and go on test as described in the next section. |  |  |

##### Apply Changes to Available Capacity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For the bottleneck resources, you may need to optimize capacity utilization by changing available capacity, for example, via adding/changing shifts.

|  |
| --- |
| Note If you want to apply changes to multiple resources at once, please use the app Mass Maintenance of Work Center Capacities (F5381). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Work Center Capacity (F3289). | The Manage Work Center Capacity (F3289) screen displays. |  |
| 3 | Check Capacity Situation | Check capacity utilization to identify bottleneck work center, as described in last section Check Capacity Situation. |  |  |
| 4 | Choose Bottleneck Resource | From the bottleneck work center list, choose one of them, for example:Work center: MIX01_CP (Ink Mixing 01)Capacity Category: Machine (001) |  |  |
| 5 | Check Detailed Capacity Load | Details on capacity load of the specific work center capacity can be seen on the detailed page. Different views are available for monitoring composition and source order operations of capacity load.In Overview section, Utilization Chart gives graphical presentation of capacity load for specific period. You can choose different filter to show utilization in different period. Find the specific dates or period in which bottleneck would occur.In Operations section, the list provides details on related source orders, for example, Planned Order for SG2_CP.The Shift section provides a review of available capacity for the specific work center. Check the shifts on bottleneck dates and consider which shifts can be added on these dates to increase available capacity. For example, if shift YS3 is not arranged, you might consider adding YS3 on these dates for this work center. | Bottleneck dates and possible additional shifts are identified. |  |
| 6 | Choose Edit | Choose Edit in the upper right of the page. | Entries under section Shift become editable. |  |
| 7 | Add Shift | Under section Shift, choose +, and choose Add Shift. Enter following entries, and choose OK.Date Range: specific period during which you would like to add shift, dependent on the bottleneck datesShift Definition: YS3 (add other shifts if YS3 is already assigned)Recurrence: Daily | Add Shift screen pops up. |  |
| 8 | Check Shift is Added | Check items in Shift section, choose More at the bottom of the page to show more entries. Shift YS3 is added for the Date Range you specified.You can choose Settings icon above the table, to set filter for example, Shift Definition equals to YS3, in order to shorten the list.After checking, choose Save. |  |  |
| 9 | Further Adjustment (Optional) | On the detailed Work Center Capacity screen, choose Edit in the upper right of the page.Under section Shift, you can adjust following parameters if needed, and choose Save.Shift Utilization: for example, 120%Number of Capacities: for example, 2In order to resolve your overload situation you could also use the function Copy Shifts in the Display mode of work center capacity, to copy a shift from one work center to another. |  |  |
| 10 | Check Bottleneck | Check capacity utilization in section Overview. After adding shift, capacity utilization during the specific period should be decreased, to reflect better match between requirement capacity and available capacity. Check if the bottleneck is resolved (all the bars are green), if not, please go back and repeat step 2-6 till no overload anymore. | The bottleneck is resolved. |  |
| 11 | Check Bottleneck for All the Resources | For all the other bottleneck resources, repeat step 1-7 to apply changes to available capacity. | The bottleneck for all resources is resolved. |  |

#### Conversion to Process Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to internally produce the planned orders for goods after capacity bottleneck is resolved.

Prerequisite

The MRP run has generated planned orders for semifinished goods (SG2_CP) and finished goods (FG2_CP).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Material Coverage - New Version (F0251A). | The Manage Material Coverage screen displays. |  |
| 3 | Select Material | Make the following entries, and then choose Go.Material: FG2_CPPlant: 3310Shortage Definition: MRP Standard | The material item displays. |  |
| 4 | Find Planned Order | Choose the material item, and then find the generated planned order on the right screen. | Order information displays. |  |
| 5 | Convert Planned Order to Process Order | From the dropdown list next to the planned order (PldOrd XXXX), select Convert. Choose Convert to Process Order. Confirm date and quantity, and choose Convert.Repeat step 2 to 5 for SG2_CP. | The process order is created. |  |

#### Process Order Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can execute the scope item BJ8 to continue with the production part. The production process has to be executed at first for the semifinished material (SG2_CP) and afterwards for the finished product (FG2_CP).

Procedure

Complete all the activities under “Process Order Processing” described in the Test Script of the scope item: Make-to-Stock – Process Manufacturing Based on Process Order (BJ8), including:

Goods Issue of Batch-Managed Components

Monitor Order Progress

Confirm Production incl.Component Backflush

Post Goods Receipt for Process Order

Result

Semifinished goods and finished goods are produced.

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

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
> Flagged while digesting this document, not verified: Check Capacity Situation (discrete) step 3 assigns work center group 05_COFFEE for plant 3310, but the sample work center groups defined in this script are TURN_ALT and CP_SG1 (created via BNJ).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/production-capacity-evaluation-and-leveling-consumer-products-5oi-ae-t]]
- related-to :: [[12-production-and-manufacturing/test-script-production-capacity-leveling-3lq-ae-sap-s-4hana-cloud-publ]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/31L_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 68,127 chars in the whole document
