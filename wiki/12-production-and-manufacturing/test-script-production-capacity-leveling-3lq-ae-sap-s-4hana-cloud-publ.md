---
id: 12-production-and-manufacturing/test-script-production-capacity-leveling-3lq-ae-sap-s-4hana-cloud-publ
title: "Test Script: Production Capacity Leveling (3LQ_AE) - SAP S/4HANA Cloud Public Edition (3LQ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3LQ_AE: prerequisites, sample data and steps for production capacity leveling, discrete and process manufacturing."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/capacity-evaluation-and-leveling]
aliases: [3LQ_S4CLD2608_BPD_EN_AE]
keywords: [Capacity Evaluation and Leveling, production capacity leveling, capacity scheduling table, capacity scheduling board, discrete manufacturing, process manufacturing, test scripts, business roles, master data, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3LQ_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-956
topic: 12-production-and-manufacturing/capacity-evaluation-and-leveling
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Production Capacity Leveling (3LQ_AE) - SAP S/4HANA Cloud Public Edition (3LQ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3LQ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Capacity Evaluation and Leveling** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Production Capacity Leveling (3LQ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853193)

[2 Prerequisites 4](#_Toc232853194)

[2.1 System Access 4](#_Toc232853195)

[2.2 Roles 4](#_Toc232853196)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232853197)

[2.4 Business Conditions 9](#_Toc232853198)

[2.5 Preliminary Steps for Discrete Manufacturing 10](#_Toc232853199)

[2.5.1 Check Formulas in Work Center 10](#_Toc232853200)

[2.5.2 Check Routings 11](#_Toc232853201)

[2.5.3 Check Production Version 12](#_Toc232853202)

[2.6 Preliminary Steps for Process Manufacturing 13](#_Toc232853203)

[2.6.1 Check Formulas in Resource 13](#_Toc232853204)

[2.6.2 Check Production Version 14](#_Toc232853205)

[3 Overview Table 16](#_Toc232853206)

[4 Test Procedures 17](#_Toc232853207)

[4.1 Production Capacity Leveling for Discrete Manufacturing 17](#_Toc232853208)

[4.1.1 Production Scheduling 17](#_Toc232853209)

[4.1.2 Review Work Center Schedules 20](#_Toc232853210)

[4.2 Production Capacity Leveling for Process Manufacturing 22](#_Toc232853211)

[4.2.1 Production Scheduling 22](#_Toc232853212)

[4.2.2 Review Work Center Schedules 25](#_Toc232853213)

[5 Appendix 27](#_Toc232853214)

[5.1 Process Integration 27](#_Toc232853215)

[5.1.1 Preceding Processes 27](#_Toc232853216)

[5.1.2 Succeeding Processes 27](#_Toc232853217)

## Purpose

Overview

This scope item supports both Discrete and Process Manufacturing capacity leveling functionality for their demands. You can determine the industry type and displayed data under the app settings. The process of production capacity leveling represents a central part of preparation for the manufacturing process of components.

After you forecast a demand for finished goods represented by Planned Independent Requirements (PIR) and the Material Requirements Planning (MRP) run created a production plan, the process of capacity leveling (scheduling) takes place.

This process enables production planners to assign orders and operations from the production plan to available timeslots of capacities. Additionally, the planners can simulate and choose other alternatives for production by assigning other available production versions, letting the planners schedule the best option for their manufacturing.

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
| Production Engineer - Process Manufacturing | SAP_BR_PRODN_ENG_PROC | Production Engineering - Process Manufacturing | SAP_BR_PRODN_ENG_PROC |  |
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Master Data for Discrete Manufacturing

This section describes sample Master Data for Discrete Manufacturing. Use your own master data or the following sample data to go through the test procedure.

Product

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Product | FG1_CP | CP-FG1, Shaft with Rolling Bearings |  |
| Product | SG1_CP | CP-SG1, Shaft |  |
| Product | RM1_CP | CP-RM1, Steel |  |
| Product | RM2_CP | CP-RM2, Rolling Bearing |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Product | Level | Material Type | Unit | Description |
| --- | --- | --- | --- | --- |
| FG1_CP | 0 | FERT | PC | Finished Good for MTS processing |
| SG1_CP | 1 | SEMI | PC | Semi-finished Goods |
| RM1_CP | 2 | RAW | PC | Raw material, component for SG1_CP |
| RM2_CP | 1 | RAW | PC | Raw material |

Routing

This overview shows Routing for Semi-finished goods and Finished goods. In the pre-delivered demo data, two routings were created for each product with same operation but different work centers for the critical operation.

| Product | Operation | Description | Work Center | Work Center (Alternative) |
| --- | --- | --- | --- | --- |
| SG1_CP | 0010 | Turning Machine 1 | TURNING1 |  |
| SG1_CP | 0020 (Critical Operation) | Turning Machine 2 | TURNING2 | TURNING9 |
| SG1_CP | 0030 | Drilling machine | DRILING |  |
| SG1_CP | 0040 | Finishing | FINICLN |  |
| SG1_CP | 0050 | Clearing | FINICLN |  |
| FG1_CP | 0010 (Critical Operation) | Assembly | ASSPKG | ASSPKG9 |
| FG1_CP | 0020 | Finish and clean | FINICLN |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Master Data for Process Manufacturing

This section describes sample Master Data for Process Manufacturing. Use your own master data or the following sample data to go through the test procedure.

Product

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Product | FG2_CP | CP-FG2, Ink Bottled, 15 ml |  |
| Product | SG2_CP | CP-SG2, Ink Bottled |  |
| Product | RM5_CP | CP-RM5, Varnish |  |
| Product | RM7_CP | CP-RM7, Label |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 |  |
| Storage Location | 331B | Std. storage 2 |  |
| Storage Location | 331C | Raw mat. stoloc. |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

| Product | Level | Material Type | Unit | Description |
| --- | --- | --- | --- | --- |
| FG2_CP | 0 | FERT | PC | Finished Good for MTS processing |
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

| Product | Operation | Phase | Description | Work Center | Work Center (Alternative) |
| --- | --- | --- | --- | --- | --- |
| SG2_CP | 0010 |  | Mixing Operation | MIX01_CP |  |
| SG2_CP | 0020 | X | Mixing Phase | MIX01_CP |  |
| SG2_CP | 0030 |  | Bottling Operation | BOT01_CP | BOT02_CP |
| SG2_CP | 0040 (Critical Phase) | X | Bottling Phase1 | BOT01_CP | BOT02_CP |
| SG2_CP | 0050 (Critical Phase) | X | Bottling Phase 2 | BOT01_CP | BOT02_CP |
| FG2_CP | 0010 |  | Packing Operation | PAC01_CP | PAC02_CP |
| FG2_CP | 0020 (Critical Operation) | X | Packing Phase | PAC01_CP | PAC02_CP |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

The following business conditions must be met before this scope item can be tested.

| Scope Item ID | Business Condition |
| --- | --- |
| 31L - Production Capacity Evaluation | All relevant steps described in the Business Conditions are completed. The process of capacity leveling can take place after capacity evaluation.For discrete manufacturing use case (working with finished goods FG1_CP), you need to complete the following activities described in the test script 31L under chapter Capacity Planning and Evaluation for Discrete Manufacturing as preceding steps.Section Create Planned Independent RequirementsSection Material Requirement PlanningSection Evaluate Capacity SituationFor process manufacturing use case (working with finished goods FG2_CP), you need to complete the following activities described in the test script 31L under chapter Capacity Planning and Evaluation for Process Manufacturing as preceding steps.Section Create Planned Independent RequirementsSection Material Requirement PlanningSection Evaluate Capacity Situation |

### Preliminary Steps for Discrete Manufacturing

#### Check Formulas in Work Center

Purpose

This process step shows you how to check and set the formulas used in work centers for critical operation. Formula under the Capacities tab is used to calculate the capacity requirements of the operation segments, while formula under the Scheduling tab is used to calculate execution time of the operation. You need to check and set formulas for following work centers: TURNING2, TURNING9, ASSPKG and ASSPKG9.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Work Center (CR02). |  |  |
| 3 | Enter Plant and Work Center | On the Change Work Center: Initial Screen, make the following entries and press Enter:Plant: 3310Work Center: <Work Center> |  |  |
| 4 | Check Formulas under Capacities Tab | Choose Capacities tab, check formulas under Capacity category section: 001. For test purpose, we recommend using the same values as below:Setup Formula: SAP005Processing Formula: SAP006 |  |  |
| 5 | Check Formulas under Scheduling Tab | Choose Scheduling tab, check following settings. For test purpose, we recommend using the same values as below:Scheduling basis section:Capacity category: 001Execution time section:Duration of Setup: SAP001Processing Duration: SAP002 |  |  |
| 6 | Exit | Choose Save or Cancel |  |  |

#### Check Routings

Purpose

If you want to use SAP pre-delivered demo data to run through this scenario, you need to check Routing settings in your system. We recommend it to be consistent with what we described in section Routing under chapter Master Data for Discrete Manufacturing. If it is not consistent, you need to manually change it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Routing (CA02). |  |  |
| 3 | Select Finished Goods | On the Change Routing: Initial Screen screen, enter the following data and choose Continue:Plant: 3310Material: FG1_CP |  |  |
| 4 | Check Routings for Finished Goods | In the list under Header Overview, check listed routing versions. You can tick each line, choose Operation to see detailed operations for each Routing version. For pre-delivered demo data, we deliver two routing versions with respective operations.GrC: 1Operation 0010 - Work Center: ASSPKGOperation 0020 - Work Center: FINICLNGrC: 2Operation 0010 - Work Center: ASSPKG9Operation 0020 - Work Center: FINICLNIf the work center in respective operation in your system is not identical with above, you need to manually change it. |  |  |
| 5 | Select Semi-finished Goods | Go back to the selection page, enter the following data and press Enter:Plant: 3310Material: SG1_CP |  |  |
| 6 | Check Routings for Semi-finished Goods | Check listed Routing versions for semi-finished goods as the same way in step 4. For detailed Operation information, please check chapter Master Data for Discrete Manufacturing. |  |  |

#### Check Production Version

Purpose

Production Versions are used as source of supply during production scheduling. This process step shows you how to check the alternative work centers which are assigned to the critical operation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Versions - C223 (C223). | The Production Version: Mass Processing screen displays. |  |
| 3 | Select Semi-finished Goods | In the Selection Conditions area, enter the following data and press Enter:Plant: 3310Material: SG1_CP |  |  |
| 4 | Check Production Version for Semi-finished Goods | Check listed production versions. For pre-delivered demo data, we deliver two production versions with respective production line assignment.Production Version: 0001Production Line: TURNING2Production Version: 0002Production Line: TURNING9 |  |  |
| 5 | Select Finished Goods | In the Selection Conditions area, enter the following data and press Enter:Plant: 3310Material: FG1_CP |  |  |
| 6 | Check Production Version for Finished Goods | Check listed production versions. For pre-delivered demo data, we deliver two production versions with respective production line assignment.Production Version: 0001Production Line: ASSPKGProduction Version: 0002Production Line: ASSPKG9 |  |  |

### Preliminary Steps for Process Manufacturing

#### Check Formulas in Resource

Purpose

In this step, you need to check and set the formulas used in resources for critical operation. Formula under the Capacities tab is used to calculate the capacity requirements of the operation segments, while formula under the Scheduling tab is used to calculate the execution time of the operation. You need to check and set formulas for the following resources: BOT01_CP, BOT02_CP, PAC01_CP and PAC02_CP. Define them as pacemaker resources by assigning them to production line in production version.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Resource (CRC2). |  |  |
| 3 | Enter Plant and Work Center | On the Change Resource: Initial Screen, make the following entries and press Enter:Plant: 3310Resource: Select one of the resources mentioned above |  |  |
| 4 | Check Formulas under Capacities Tab | Choose the Capacities tab, check formulas under Capacity category section 001 and 002. For test purpose, we recommend using the same values as below:Other Formula: YBPI01Int. dist. key: SAP060 |  |  |
| 5 | Check Formulas under Scheduling Tab | Choose Scheduling tab, check following settings. For test purpose, we recommend using the same values as below:Scheduling basis section:Capacity category: 001Execution time section:Int. Proc. Duration: YBPI01 |  |  |
| 6 | Exit | Choose Save or Cancel. |  |  |

#### Check Production Version

Purpose

Production Versions are used as source of supply during production scheduling. You can check the alternative work centers which are assigned to the critical operation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Engineer - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Versions - C223 (C223). | The Production Version: Mass Processing screen displays. |  |
| 3 | Select Semi-finished Goods | In the Selection Conditions area, enter the following data and press Enter:Plant: 3310Material: SG2_CP |  |  |
| 4 | Check Production Version for Semi-finished Goods | Check listed production versions. For pre-delivered demo data, we deliver two production versions with respective production line assignment.Production Version: 0001Production Line: BOT01_CPProduction Version: 0002Production Line: BOT02_CP |  |  |
| 5 | Select Finished Goods | In the Selection Conditions area, enter the following data and press Enter:Plant: 3310Material: FG2_CP |  |  |
| 6 | Check Production Version for Finished Goods | Check listed production versions. For pre-delivered demo data, we deliver two production versions with respective production line assignment.Production Version: 0001Production Line: PAC01_CPProduction Version: 0002Production Line: PAC02_CP |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Production Capacity Leveling for Discrete Manufacturing |  |  |  |
| [Production Scheduling](#unique_13) [page ] 17 | Production Planner | Capacity Scheduling Table (F3770) | Order is rescheduled and dispatched. |
| [Review Work Center Schedules](#unique_14) [page ] 20 | Production Planner | Capacity Scheduling Board (F3951) |  |
| Production Capacity Leveling for Process Manufacturing |  |  |  |
| [Production Scheduling](#unique_15) [page ] 22 | Production Planner | Capacity Scheduling Table (F3770) | Order is rescheduled and dispatched. |
| [Review Work Center Schedules](#unique_16) [page ] 25 | Production Planner | Capacity Scheduling Board (F3951) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Production Capacity Leveling for Discrete Manufacturing

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
| 3 | Check App Settings | In the App Settings dialog box, check if only below entry is assigned:For Industry Type, select the following value and choose OK:Industry Type: DiscreteIn the Basis Controls section, select Area for Responsibility. Select Plant and MRP Controller and choose Assign. Check if only below entries are assigned:Plant 1 AE (3310)MRP Controller 002 (002) |  |  |
| 4 | Filter | Choose the following entries as filter and choose Go.Product: SG1_CP , FG1_CPHorizon : for example, next 1 monthStatus: Not Dispatched and Dispatched | Critical operation for orders which fulfill the search criteria are displayed.If the tested products are MTO relevant, choose the settings to check Sales Orders and Sales Order Items. |  |
| 5 | Choose Order | Orders for SG1_CP and FG1_CP are displayed in the list. Choose the desired order you want to dispatch. | The Capacity Scheduling Table screen displays. |  |
| 6 | Check Operation Information | In the top section of the detailed screen, check the detailed information about the critical operation.. |  |  |
| 7 | Check Available Time Buckets | In the below area of the right panel, the available source of supply would display under the grid table.Use the calendar selection box to adjust the date bucket in which you need to dispatch the order.For orders producing SG1_CP , the work centers TURNING2 and TURNING9 can be used as alternative work centers.For orders producing FG1_CP , the work centers ASSPKG and ASSPKG9 can be used as alternative work centers. | The available capacity (XX H) for each day displays in the time bucket table. |  |
| 8 | Check Strategy | Choose Set Strategy in the upper right corner of the left panel. You can check relevant settings here and adjust if necessary.Planning ModeScheduling ControlDirectionIn this case, we choose the Bucket mode as an example. | There are two planning modes:Bucket: Allocate orders to first available timeslot.Sequence: Define an exact time for the order to start/end (depending on the planning direction). |  |
| 9 | Check Order Information | Under Sourcing & Scheduling section, on the right panel, choose the tab page Additional Information to check detailed order information. |  |  |
| 10 | Check Source of Supply | Under Available Sources of Supply in the bucket table, relevant production version displays. Check the production version marked as Assign. If you want to adopt some other production version instead, you can check the relevant line in the Assign column. |  |  |
| 11 | Choose Available Time Bucket | In the bucket table, choose the radio button before the available capacity (XX H) you want to assign. You may view the available capacity (XX H) by Day, Week or Shift, as well as select the date range. | If you want to schedule the operation to past, you could select the date interval through date range picker. The threshold for Past is defined in App Settings > Past Threshold (Maximum of 30 days). |  |
| 12 | Dispatch and Review the Dispatched Orders | Choose Dispatch.Choose Review Dispatched Orders to review the dispatched orders. | A message displays: Dispatch of Order XXXX Operation XXXX scheduled from XXX to XXX was successful. |  |
| 13 | Cancel Dispatch (Optional) | If you need to cancel the dispatch process, choose Deallocate. | The Status becomes Not Dispatched. |  |
| 14 | Realign Schedules (Optional) | If you need to realign the schedule, select corresponding items and choose Realign Schedules.Note Realigning the schedule is only available on the overview screen. Choose back to return to this screen from the details view.Enter the off-set number of days and time, choose Realign (choose Save and Realign if you want to set the day and time as default). | A message Realign Schedules executed appears. For details, see Message Manager.You could choose Insert Operation for Future or Past. The offset threshold for Past is defined in App Settings > Past Threshold (Maximum of 30 days). |  |
| 15 | Check Missing Components Availability (Optional) | If you want to check the missing components availability for production orders, select production orders and choose Check Availability.Note The availability check for missing components is only accessible on the overview screen. Choose Back to return to this screen from the details view.Click the messages icon at the bottom left to view the missing components details. In the Issues column, the Missing Components icon turns red for the selected production orders if any missing components are found. | Expand the dropdown menu of Check Availability to access the following options if needed:Reset Availability clears all quantities that have been committed and grays out the Missing Components icons.Reset and Check Availability first clears all quantities that have been committed and then performs the availability check.Note This feature currently only supports production and process orders, but not planned orders. |  |
| 16 | Choose Save | Choose Save at the bottom of the left panel. |  |  |

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

This step allows the production planner to monitor schedule status by the visualization of Gantt chart.

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Capacity Scheduling Board (F3951). |  |  |
| 3 | Check App Settings | On the Capacity Scheduling Board screen, choose your user icon and select App Settings. Switch on the Activity Coloring toggle, and choose OK. |  |  |
| 4 | Filter | Choose the following entries as filters and choose Go.Evaluation Horizon: for example, next 1 monthProduct: SG1_CP , FG1_CPStatus: Not Dispatched and Dispatched | Under Operation Info > Activities, the setup, process, and teardown information is designated in different colors within the selected operation bar. |  |
| 5 | Monitor Status | Click the Show Legend icon at the top right. The color samples for both filtered and unfiltered operations are displayed.The Status filter affects the displayed color of operations. Operations that meet the filter criteria are shown in specific colors.To view not-dispatched operations, deselect the Status filter option Dispatched and choose Go. The not-dispatched operations are shown in colors, representing the filtered operations in the Legend list, while other operations are grayed out.Choose Filtered Operations to select all colored operations. Then choose Operation Info, select one of the orders, and the operation details are displayed. |  |  |
| 6 | Reschedule the Operation | Hover over a bar (operation) to display the order information tooltip.Click on a bar and choose Manage Operation.Move the operation by dragging and dropping the bar within the same production version or across different production versions on the Manage Operation page. | The following messages are displayed:Order XXX saved successfully. Order XXX Operation XXX is rescheduled successfully from XXX to XXX.Note You can only drag and drop bars to reschedule bottleneck operations.A single bar (operation) can be dropped across different production versions. Multiple bars (operations) that are selected at one time can only be dropped in the assigned production version and the order is rescheduled accordingly in the same production version. |  |
| 7 | Save Gantt Chart Settings (Optional) | On the Capacity Scheduling Board screen, you can personalize your Gantt chart settings and save the view.Display Work Center GroupsIn the upper left corner, expand the dropdown box, and you can choose to display Pacemaker Work Centers or All Work Centers. Choose the Settings icon on the left, select Work Center Group, and choose OK. The work center groups are displayed on the left.Display Order ID, Product ID, and Product DescriptionIn the upper right corner, choose the Zoom In or Zoom Out icon to adjust the scale of the Gantt chart. Choose the Gantt Settings icon on the right to adjust the Gantt chart settings. From the pop-up dialog, select Order ID, Product ID, and Product Description. Choose OK. The order ID, product ID, and product description are now displayed on the bar.Save Your Personalized ViewAfter configuring your personalized settings, you can save the view by choosing the arrow icon next to the Standard view under the Evaluation Horizon. Choose Save As. Name your view and choose Save. | Your personalized Gantt chart settings are saved as a new view.On the Manage Operation page, the changes to the zoom value and the Gantt chart settings will be reflected on the Capacity Scheduling Board screen.On the Order Details page, only the changes to the Gantt chart settings will be reflected on the Capacity Scheduling Board screen. |  |

### Production Capacity Leveling for Process Manufacturing

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
| 3 | Check App Settings | On the Capacity Scheduling Table screen, choose your user icon and select App Settings.In the dialog box, check if only below entries are assigned:Plant 1 AE (3310)MRP Controller 002 (002)Choose AOR status button of this entry if not assigned, choose AOR status button of the corresponding entry to unassign any other entry then choose Back.Note You can select the Area of Responsibility by Plant and MRP Controller or Work Center Group.For Industry Type, select following value and choose OK.Industry Type: Process |  |  |
| 4 | Filter | Choose following entries as filter and choose Go.Product: SG2_CP, FG2_CPHorizon: for example, next 1 monthStatus: Not Dispatched and Dispatched | Critical operation for orders which fulfill the search criteria would display. |  |
| 5 | Choose Order | Orders for SG2_CP and FG2_CP will be displayed in the list. Choose the desired order you want to dispatch. | The Schedule Production screen displays. |  |
| 6 | Check Operation Information | In the upper area of the right panel, check detailed information of the critical operation. |  |  |
| 7 | Check Available Time Buckets | In the below area of the right panel, the available source of supply would display under the grid table.Using calendar selection box to adjust the date bucket in which you need to dispatch the order.For orders producing SG2_CP, BOT01_CP and BOT02_CP would supply as two possible work centers.For orders producing FG2_CP, PAC01_CP and PAC02_CP would supply as two possible work centers. | The available capacity (XX H) for each day displays in the time bucket table. |  |
| 8 | Check Strategy | Choose Set Strategy in the upper right corner of the left panel. You can check relevant settings here and adjust if necessary.Planning ModeScheduling ControlDirectionIn this case, we choose the Bucket mode as an example. | There are two planning modes:Bucket: Allocate orders to first available timeslot.Sequence: Define an exact time for the order to start/end (depending on the planning direction). |  |
| 9 | Check Order Information | Under Sourcing & Scheduling section, choose the Show More (mouseover) icon to check detailed order information. |  |  |
| 10 | Check Source of Supply | Under Available Sources of Supply in the bucket table, relevant production version displays. Check the production version marked as Assign. If you want to adopt some other production version instead, you can check the relevant line in the Assign column. |  |  |
| 11 | Choose Available Time Bucket | In the bucket table, choose the radio button before the available capacity (XX H) you want to assign. You may view the available capacity (XX H) by Day, Week or Shift, as well as select the date range. | If you want to schedule the operation to past, you could select the date interval through date range picker. The threshold for Past is defined in App Settings > Past Threshold (Maximum of 30 days). |  |
| 12 | Dispatch and Review the Dispatched Orders | Choose Dispatch. Choose Review Dispatched Orders to review the dispatched orders. | A message displays: Dispatch of Order XXXX Operation XXXX scheduled from XXX to XXX was successful. |  |
| 13 | Cancel Dispatch (Optional) | If you need to cancel the dispatch process, choose Deallocate. | The Status becomes Not Dispatched. |  |
| 14 | Realign Schedules (Optional) | If you need to realign the schedule, select corresponding items and choose Realign Schedules.Enter the off-set number of days and time, choose Realign (choose Save and Realign if you want to set the day and time as default). | A message Realign Schedules executed appears. For details, see Message Manager.You could choose Insert Operation for Future or Past. The offset threshold for Past is defined in App Settings > Past Threshold (Maximum of 30 days). |  |
| 15 | Check Missing Components Availability (Optional) | If you want to check the missing components availability for process orders, select process orders and choose Check Availability.Note The availability check for missing components is only accessible on the overview screen. Choose Back to return to this screen from the details view.Click the messages icon at the bottom left to view the missing components details. In the Issues column, the Missing Components icon turns red for the selected process orders if any missing components are found. | Expand the dropdown menu of Check Availability to access the following options if needed:Reset Availability clears all quantities that have been committed and grays out the Missing Components icons.Reset and Check Availability first clears all quantities that have been committed and then performs the availability check.Note This feature currently only supports production and process orders, but not planned orders. |  |
| 16 | Choose Save | Choose Save at the bottom of the left panel. |  |  |

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

This step allows the production planner to monitor schedule status by the visualization of Gantt chart.

Procedure

| Procedure Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Capacity Scheduling Board (F3951). |  |  |
| 3 | Filter | Choose the following entries as filters and choose Go.Horizon: for example, next 1 monthProduct: SG2_CP, FG2_CPStatus: Non Dispatched and Dispatched |  |  |
| 4 | Monitor Status | Monitor the schedule status in the dashboard.View detailed information by selecting the color-bar and choosing Operation Info. |  |  |
| 5 | Reschedule the Operation | Hover over a bar (operation) to display the order information tooltips.Click on a bar and choose Manage Operation.Move the operation by dragging and dropping the bar within the same production version or across different production versions on the Manage Operation page. | The following messages are displayed:Order XXX saved successfully. Order XXX Operation XXX is rescheduled successfully from XXX to XXX. Note You can only drag and drop bars to reschedule bottleneck operations.A single bar (operation) can be dropped across different production versions. Multiple bars (operations) that are selected at one time can only be dropped in the assigned production version and the order is rescheduled accordingly in the same production version. |  |
| 6 | Save Gantt Chart Settings (Optional) | On the Capacity Scheduling Board screen, you can personalize your Gantt chart settings and save the view.Display Work Center GroupsIn the upper left corner, expand the dropdown box, and you can choose to display Pacemaker Work Centers or All Work Centers. Choose the Settings icon on the left, select Work Center Group, and choose OK. The work center groups are displayed on the left.Display Order ID, Product ID, and Product DescriptionIn the upper right corner, choose the Zoom In or Zoom Out icon to adjust the scale of the Gantt chart. Choose the Gantt Settings icon on the right to adjust the Gantt chart settings. From the pop-up dialog, select Order ID, Product ID, and Product Description. Choose OK. The order ID, product ID, and product description are now displayed on the bar.Save Your Personalized ViewAfter configuring your personalized settings, you can save the view by choosing the arrow icon next to the Standard view under the Evaluation Horizon. Choose Save As. Name your view and choose Save. | Your personalized Gantt chart settings are saved as a new view.On the Manage Operation page, the changes to the zoom value and the Gantt chart settings will be reflected on the Capacity Scheduling Board screen.On the Order Details page, only the changes to the Gantt chart settings will be reflected on the Capacity Scheduling Board screen. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have the following processes and conditions completed before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| 31L - Production Capacity Evaluation | For discrete manufacturing use case, below sections under chapter Capacity Planning and Evaluation for Discrete Manufacturing:Section Conversion to Production OrdersSection Material Requirement PlanningSection Evaluate Capacity SituationFor process manufacturing use case, below sections under chapter Capacity Planning and Evaluation for Process Manufacturing:Section Conversion to Production OrdersSection Material Requirement PlanningSection Evaluate Capacity Situation |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 31L - Production Capacity Evaluation | For discrete manufacturing use case, below sections under chapter Capacity Planning and Evaluation for Discrete Manufacturing:Section Conversion to Production OrdersSection Production Order Processing for SubassemblySection Production Order Processing for Final AssemblyFor process manufacturing use case, below sections under chapter Capacity Planning and Evaluation for Process Manufacturing:Section Conversion to Process OrdersSection Process Order Processing |

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
> Flagged while digesting this document, not verified: Preceding-process list differs between sections: Business Conditions (2.4) lists Create Planned Independent Requirements, Material Requirement Planning and Evaluate Capacity Situation from 31L, while Appendix 5.1.1 Preceding Processes lists Conversion to Production Orders, Material Requirement Planning and Evaluate Capacity Situation.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/production-capacity-evaluation-and-leveling-consumer-products-5oi-ae-t]]
- related-to :: [[12-production-and-manufacturing/test-script-capacity-planning-evaluation-scope-item-31l-sap-s-4hana-cl]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3LQ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 45,928 chars in the whole document
