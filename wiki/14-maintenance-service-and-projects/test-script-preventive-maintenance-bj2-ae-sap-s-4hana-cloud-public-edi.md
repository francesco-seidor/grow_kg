---
id: 14-maintenance-service-and-projects/test-script-preventive-maintenance-bj2-ae-sap-s-4hana-cloud-public-edi
title: "Test Script: Preventive Maintenance (BJ2_AE) - SAP S/4HANA Cloud Public Edition (BJ2_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for Preventive Maintenance (BJ2, AE): time/performance/multiple-counter plans, scheduling and order processing."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/preventive-and-proactive-maintenance]
aliases: [BJ2_S4CLD2608_BPD_EN_AE]
keywords: [Preventive and Proactive Maintenance Plans, preventive maintenance, task lists, maintenance items, maintenance plans, maintenance strategies, maintenance plan scheduling, measurement documents, maintenance order processing, test prerequisites]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJ2_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1269
topic: 14-maintenance-service-and-projects/preventive-and-proactive-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Preventive Maintenance (BJ2_AE) - SAP S/4HANA Cloud Public Edition (BJ2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJ2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Preventive and Proactive Maintenance Plans** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Preventive Maintenance (BJ2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861661)

[2 Prerequisites 4](#_Toc232861662)

[2.1 System Access 4](#_Toc232861663)

[2.2 Roles 4](#_Toc232861664)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232861665)

[2.4 Business Conditions 7](#_Toc232861666)

[2.5 Initializing Material Stock 7](#_Toc232861667)

[3 Overview Table 9](#_Toc232861668)

[4 Test Procedures 12](#_Toc232861669)

[4.1 Time-Based Single Cycle Plan 12](#_Toc232861670)

[4.1.1 Create General Task List 12](#_Toc232861671)

[4.1.2 Create Maintenance Item 15](#_Toc232861672)

[4.1.3 Create Maintenance Plan 16](#_Toc232861673)

[4.1.4 Schedule Maintenance Plan 18](#_Toc232861674)

[4.2 Time-Based Strategy Plan 20](#_Toc232861675)

[4.2.1 Maintain Maintenance Strategies 20](#_Toc232861676)

[4.2.2 Create General Task List 22](#_Toc232861677)

[4.2.3 Create Maintenance Item 25](#_Toc232861678)

[4.2.4 Create Maintenance Plan 26](#_Toc232861679)

[4.2.5 Schedule Maintenance Plan 28](#_Toc232861680)

[4.3 Performance-Based Single Cycle Plan 30](#_Toc232861681)

[4.3.1 Create General Task List 30](#_Toc232861682)

[4.3.2 Create Maintenance Item 33](#_Toc232861683)

[4.3.3 Create Maintenance Plan 34](#_Toc232861684)

[4.3.4 Create Measurement Document 36](#_Toc232861685)

[4.3.5 Schedule Maintenance Plan 37](#_Toc232861686)

[4.4 Performance-Based Strategy Plan 39](#_Toc232861687)

[4.4.1 Maintain Maintenance Strategies 39](#_Toc232861688)

[4.4.2 Create General Task List 41](#_Toc232861689)

[4.4.3 Create Maintenance Item 44](#_Toc232861690)

[4.4.4 Create Maintenance Plan 45](#_Toc232861691)

[4.4.5 Create Measurement Document 48](#_Toc232861692)

[4.4.6 Schedule Maintenance Plan 49](#_Toc232861693)

[4.5 Multiple Counter Plan 50](#_Toc232861694)

[4.5.1 Create General Task List 50](#_Toc232861695)

[4.5.2 Create Maintenance Item 53](#_Toc232861696)

[4.5.3 Create Maintenance Plan 54](#_Toc232861697)

[4.5.4 Create Measurement Document 57](#_Toc232861698)

[4.5.5 Schedule Maintenance Plan 58](#_Toc232861699)

[4.6 Order Processing 60](#_Toc232861700)

[4.6.1 Release Preventive Maintenance Order and Print to Job List 60](#_Toc232861701)

[4.6.2 Confirm Preventive Maintenance Order 61](#_Toc232861702)

[4.6.3 Create Follow-On Order 63](#_Toc232861703)

[4.6.4 Show Costs on Preventive Maintenance Order 65](#_Toc232861704)

[4.6.5 Technically Complete Preventive Maintenance Order 66](#_Toc232861705)

[4.6.6 Review Document Flow of Preventive Maintenance Order 68](#_Toc232861706)

[4.6.7 Review Asset Maintenance Object Pages 69](#_Toc232861707)

[5 Appendix 70](#_Toc232861708)

[5.1 Maintenance Planning Overview 70](#_Toc232861709)

[5.2 Process Integration 71](#_Toc232861710)

[5.2.1 Preceding Processes 71](#_Toc232861711)

[5.2.2 Succeeding Processes 71](#_Toc232861712)

## Purpose

Overview

This scope item describes the processes you perform to prevent system breakdowns or breakdowns of other objects that have high repair costs. Such breakdowns result in greater costs due to production downtime. Preventive maintenance support processes to plan the scope and time of maintenance work for inspections, maintenance, and repairs, in advance. The quality of products manufactured is substantially affected by the operational condition of the production plant. There is a requirement for quality assurance to be more cost effective to maintain objects regularly, and in return avoid a more expensive breakdown. You determine the data required for preventive maintenance by using previous data supplied by the system. In addition to internal company aspects for planned maintenance, you should consider external factors due to an increasing number of conditions set by legislative bodies demanding more stringent requirements on planned monitoring and maintenance of objects.

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
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |
| Maintenance Technician | SAP_BR_MAINTENANCE_TECHNICIAN | Maintenance Execution | SAP_BR_MAINTENANCE_TECHNICIAN |  |
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Maintenance Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage 2 |  |
| Material | SP001 | Bearing | Spare Parts |
| Material | SP002 | Coupling | Spare Parts |
| Material | SP003 | Shaft | Spare Parts |
| Material | SP004 | Gaskets 1mm | Spare Parts |
| Material | SP005 | Mechanical Seal | Spare Parts |
| Material | SP006 | Spur gear IS651 | Spare Parts |
| Work Center | RES-0100 | Mechanics |  |
| Work Center | RES-0200 | Electric |  |
| Work Center | RES-0300 | Instrumentation |  |
| Characteristics | OPERATING_HOUR | Hour Meter Reading |  |
| Characteristics | PRESSURE | Pressure Reading |  |
| Counter Measuring Point | XXXXXX | Operating Hour | 1-999999 |
| Non Counter Measuring Point | XXXXXX | Pressure Guage | 1-999999 |
| Functional Location | 3310 -XXX-XXX-XXXXX-XXXX-XXXX |  | 3310 and the substructures |
| Equipment | 2 3310 XXXX |  | 2 3310 0001 ~233100092 |
| Equipment BOM | 233100091 |  | With SP001 ~ SP006 assigned |

For more information on creating master data objects, see the following Master Data Scripts (MDS):

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 5LM | Create Functional Location |
| 5MF | Create Equipment |
| 5MH | Create Maintenance Work Center |
| 5MI | Measuring Point |
| 2J7 | Spare Parts |

This overview shows the bill of material structure and the usage of each component if you have activated all optional enhancements.

Table 2:

| Material | Level | Material Type | Unit | Characteristics of Material |
| --- | --- | --- | --- | --- |
| 233100091 | 0 | Equipment | PC | Cooling Water Circulation Pump |
| SP001 | 1 | ERSA | PC | Bearing |
| SP002 | 1 | ERSA | PC | Coupling |
| SP003 | 1 | ERSA | PC | Shaft |
| SP004 | 1 | ERSA | PC | Gaskets 1mm |
| SP005 | 1 | ERSA | PC | Mechanical Seal |
| SP006 | 1 | ERSA | PC | Spur gear IS651 |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. The posting period is up to date.To run through this scope item, the materials must be available in stock. |

### Initializing Material Stock

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In a real business case, the materials are usually purchased from external suppliers. In this case, the process is covered by the standard purchasing or subcontracting processes. This process step shows you how to post initial stock directly to the storage locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock screen displays. |  |
| 3 | Input Material | Make the following entries and choose Enter:Material: < material number>. Select one of the Spare Parts Material mentioned in the previous section Master Data, Organizational Data, and Other Data.Plant: Plant 1 AE (3310) |  |  |
| 4 | Select Stock | Select the icon beside the stock that you want to add initial stock, for example:Storage Location: Std. storage 2 (331B)Unrestricted-Use Stock | A dialog box opens. The Storage Location, Stock Type and Current Quantity display according to your entries in the previous steps. |  |
| 5 | Add Initial Entry | Make the following entries and choose Post:Document Date: <today>Posting Date: <today>Stock Change: initial entryQuantity: <quantity number> | The system displays Material document XXX created. The stock has been added. |  |

## Overview Table

The scope item Preventive Maintenance consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Preventive Maintenance - Time Based Single Cycle Plans |  |  |  |
| [Create General Task List](#unique_9) [page ] 12 | Maintenance Planner | Create Task List | The task list is created. |
| [Create Maintenance Item](#unique_10) [page ] 15 | Maintenance Planner | Manage Maintenance Items (F5356) | The maintenance item is created. |
| [Create Maintenance Plan](#unique_11) [page ] 16 | Maintenance Planner | Manage Maintenance Plans (F5325) | The maintenance plan is created. |
| [Schedule Maintenance Plan](#unique_12) [page ] 18 | Maintenance Planner | Mass Schedule Maintenance Plans (F2774) | The maintenance plan is scheduled. |
| Preventive Maintenance - Time Based Strategy Plans |  |  |  |
| [Maintain Maintenance Strategies](#unique_13) [page ] 20 | Maintenance Planner | Maintenance Strategies (IP12) | The maintenance strategy is created. |
| [Create General Task List](#unique_14) [page ] 22 | Maintenance Planner | Create Task List | The task list is created. |
| [Create Maintenance Item](#unique_15) [page ] 25 | Maintenance Planner | Manage Maintenance Items (F5356) | The maintenance item is created. |
| [Create Maintenance Plan](#unique_16) [page ] 26 | Maintenance Planner | Manage Maintenance Plans (F5325) | The maintenance plan is created. |
| [Schedule Maintenance Plan](#unique_12) [page ] 18 | Maintenance Planner | Mass Schedule Maintenance Plans (F2774) | The maintenance plan is scheduled. |
| Preventive Maintenance - Performance Based Single Cycle Plan |  |  |  |
| [Create General Task List](#unique_17) [page ] 30 | Maintenance Planner | Create Task List | The task list is created. |
| [Create Maintenance Item](#unique_18) [page ] 33 | Maintenance Planner | Manage Maintenance Items (F5356) | The maintenance item is created. |
| [Create Maintenance Plan](#unique_19) [page ] 34 | Maintenance Planner | Manage Maintenance Plans (F5325) | The maintenance plan is created. |
| [Create Measurement Document](#unique_20) [page ] 36 | Maintenance Planner | Create Measurement Document (IK11) | The measurement document is created. |
| [Schedule Maintenance Plan](#unique_12) [page ] 18 | Maintenance Planner | Mass Schedule Maintenance Plans (F2774) | The maintenance plan is scheduled. |
| Preventive Maintenance - Performance Based Strategy Plan |  |  |  |
| [Maintain Maintenance Strategies](#unique_21) [page ] 39 | Maintenance Planner | Maintenance Strategies (IP12) | The maintenance strategy is created. |
| [Create General Task List](#unique_22) [page ] 41 | Maintenance Planner | Create Task List | The task list is created. |
| [Create Maintenance Plan](#unique_23) [page ] 45 | Maintenance Planner | Manage Maintenance Items (F5356) | The maintenance item is created. |
| [Create Maintenance Plan](#unique_23) [page ] 45 | Maintenance Planner | Manage Maintenance Plans (F5325) | The maintenance plan is created. |
| [Create Measurement Document](#unique_24) [page ] 48 | Maintenance Planner | Create Measurement Document (IK11) | The measurement document is created. |
| [Schedule Maintenance Plan](#unique_25) [page ] 49 | Maintenance Planner | Mass Schedule Maintenance Plans (F2774) | The maintenance plan is scheduled. |
| Preventive Maintenance - Multiple Counter Plan |  |  |  |
| [Create General Task List](#unique_26) [page ] 50 | Maintenance Planner | Create Task List | The task list is created. |
| [Create Maintenance Item](#unique_27) [page ] 53 | Maintenance Planner | Manage Maintenance Items (F5356) | The maintenance item is created. |
| [Create Maintenance Plan](#unique_28) [page ] 54 | Maintenance Planner | Manage Maintenance Plans (F5325) | The maintenance plan is created. |
| [Create Measurement Document](#unique_29) [page ] 57 | Maintenance Technician | Create Measurement Document (IK11) | The measurement document is created. |
| [Schedule Maintenance Plan](#unique_30) [page ] 58 | Maintenance Planner | Mass Schedule Maintenance Plans (F2774) | The maintenance plan is scheduled. |
| Preventive Maintenance - Order Processing |  |  |  |
| [Release Preventive Maintenance Order and Print to Job List](#unique_31) [page ] 60 | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | The maintenance order is released and job card is printed. |
| [Confirm Preventive Maintenance Order](#unique_32) [page ] 61 | Maintenance Technician | Perform Maintenance Jobs (F5104A) | Maintenance order is confirmed. |
| [Create Follow-On Order](#unique_33) [page ] 63 | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | Follow-on order is created. |
| [Show Costs on Preventive Maintenance Order](#unique_34) [page ] 65 | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | Preventive maintenance order costs are displayed. |
| [Technically Complete Preventive Maintenance Order](#unique_35) [page ] 66 | Maintenance Planner | Find Maintenance Orders - Completion (F2175) | Preventive maintenance order is technically completed. |
| [Review Document Flow of Preventive Maintenance Order](#unique_36) [page ] 68 | Maintenance Planner | Display Maintenance Order (MaintenanceOrder-display) | Preventive maintenance order document flow is re-viewed. |
| [Review Asset Maintenance Object Pages](#unique_37) [page ] 69 | Maintenance Planner | Not applicable | Asset maintenance object pages are reviewed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Time-Based Single Cycle Plan

#### Create General Task List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using task lists, you can centrally define and manage maintenance tasks for your technical objects. General task lists can also help you to prepare maintenance plans and orders.

A task list group combines one or more task lists according to their logical features. Within a task list group, each task list is identified by a group counter. This enables you, for example, to combine several task lists in one group. Within the group, the system allocates a sequential number (the group counter) to each individual task list.

Prerequisites

- Technical objects in the form of functional locations, equipment, and maintenance assemblies.
- Organizational units such as maintenance planners and work centers.
- Cost centers defined in the master data of the technical objects.
- Maintenance spare parts and assemblies in the MM (Materials Management) module.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad displays. |  |
| 2 | Open Create Task List | Open Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)). | The Create Task List page appears. |  |
| 3 | Choose Task List Type | Choose Task List Type: General Maintenance Task List. | The Create General Maintenance Task List screen displays. |  |
| 4 | Enter Creation Parameters | Make the following entries and choose Continue.Task List Group:Comment: Task List Group uses internal number range.Planning Plant: 3310Group Counter:Comment: The group counter would increase automatically if you create another task list under the same task list group.Overall Status: Released (general)Select the relevant profile for the plant.Key Date: <Today>Choose Continue. | The Create General Maintenance Task List page displays. |  |
| 5 | Maintain General Data | Make the following entries:Description: <Description> Enter a description. For example, Mechanical Inspection.Planner Group: YB1Work Center: RES-0100Work Center Plant: 3310System Condition: not in operationChoose Operation Data. | The Operation Data tab appears. |  |
| 6 | Maintain Operation Data | Make the following entries and choose Enter.Operation: 0010Description: Check the pumpWork: 2Unit: HCapacities: 2Operation: 0020Description: Check the bearingsWork: 1Unit: HCapacities: 1Operation : 0030Description: Check the couplingWork: 2Unit: HCapacities: 2Operation: 0040Description: Check the shaftWork: 3Unit: HCapacities: 3Choose the Operation 0010.In the lower part of the screen, Details: Operation 0010, Check the pump section, choose Materials.Make the following entries and choose Enter.Material: SP005Quantity: 1Repeat the above step for other operations.Operation Item: 0020Material: SP001Quantity: 2Operation Item: 0030Material: SP002Quantity: 1Operation Item: 0040Material: SP003Quantity: 2Choose Save | The general task list is created. |  |

#### Create Maintenance Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance item describes which preventive maintenance tasks should take place regularly at a technical object or a group of technical objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Maintenance Items app | Open Manage Maintenance Items (F5356). | The Manage Maintenance Items page appears. |  |
| 3 | Create Maintenance Item | To create a maintenance item, choose Create button on the top of the screen. Enter following details in the pop-up window:Item Description: Mechanical Inspection for PumpPlan Category: PM (Maintenance Order)Reference Object Type: EquipmentReference Object: 2 1710 XXXXTask List: <Entry of choice>You can use the task list created in the previous step.Order Type: YBA2.Choose Create.Maintenance Item screen displays, enter following details under Basic Details tab:Maintenance Activity Type: YB4Priority: <Entry of your choice>Choose Create.Note Maintenance items can also be created through the Manage Maintenance Plans (F5325) app. | The maintenance item is created. |  |

#### Create Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance plan will have maintenance or inspection activities to be carried out for technical objects.

The frequency or strategy and, scope of the activities are defined in the maintenance plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Maintenance Plan | Open Manage Maintenance Plans (F5325). | The Manage Maintenance Plan page is displayed. |  |
| 3 | Create Maintenance Plan | To create a maintenance plan, choose Create on the top of the screen. Enter the following details in the dialog box:Plan Description: Mechanical Inspection for PumpPlan Category: Maintenance OrderPlan Type: Single Cycle (Time-Based)Choose Create. | The Maintenance Plan page is displayed. |  |
| 4 | Maintain Maintenance Plan Item Data | To create a maintenance item choose Create Item button by scrolling down to Maintenance item section. Enter the following details in the popup window:Item Description: Mechanical Inspection for PumpReference Object Type: EquipmentReference Object: 23310XXXXTask List: <Entry of choice>You can use the task list created in the previous step.Order Type: YBA2Choose Create.Click on Maintenance Item line and enter following details under Basic Details tab:Maintenance Activity Type: YB4Priority: <Entry of your choice>Planning Plant: 3310Choose Apply. | The details of the maintenance item are updated and the Maintenance Plan screen is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | In the Cycle section, make following entries:Cycle Length: 1Cycle UoM: MONComment: Cycle Length/Cycle UoM defines the duration in which the maintenance is to be executed.Cycle Text: MonthlyIn the Schedule section, make following entries:Scheduling Duration: 365Comment: You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.Start Date for Scheduling: <Current date>Comment: The start date is needed for mass schedule maintenance plans.End Date for Scheduling: <Entry of Choice>In the Scheduling Parameters section, make following entries:Shift Factor for Early Completion (as Percentage): 100Shift Factor for Late Completion (as Percentage): 100Comment: The shift factor in the event of early/late completion of a maintenance task defines the percentage of the shift to be applied to the calculation of the next date.Tolerance for Early Completion (as Percentage): 10Tolerance for Late Completion (as Percentage): 10Comment: The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cycles of the maintenance strategy.Cycle Modification Factor: 1Call Horizon: 50Comment: The call horizon determines when a maintenance call object, for example, a maintenance order should be generated for a maintenance call related to the maintenance planned date.Completion Required: Select Yes or No using the toggle buttonComment: If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.Scheduling Indicator: TimeChoose Create. | The maintenance plan is created. |  |
| 6 | Assign Maintenance Item (Optional) | Alternatively, it is possible to assign existing maintenance item to a maintenance plan using the Assign Item button. To assign an item, follow these steps:Open the maintenance plan in Manage Maintenance Plans (F5325) app.Choose Assign Item.Select the required maintenance item and choose OK. | The maintenance item is assigned to the maintenance plan. |  |

#### Schedule Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you schedule your maintenance plan for the first time, you trigger the maintenance cycle. The system uses the scheduling information in the maintenance plan to calculate the due date of maintenance call object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Schedule Maintenance Plan | Open Schedule Maintenance Plan (IP10). | The Schedule Maintenance Plan: Initial page displays. |  |
| 3 | Search Maintenance Plan | Make the following entries and choose Enter.MaintenancePlan: <Maintenance Plan number>Use the single cycle plan (time based) created in the previous step. | The Schedule Maintenance Plan: Single Cycle Plan <Maintenance Plan number> page displays. |  |
| 4 | Schedule Maintenance Plan | Choose Start.On the Start Date screen, enter a start date. For example, enter current date.Start of cycle: <Current Date>Choose Continue.You receive an overview of scheduled calls with plan date and call date of a schedule call based on the start date you entered and based on the scheduling parameters that are maintained in the maintenance plan.Comment: The scheduling list shows scheduled calls with assigned call dates. Each call has its own system status with scheduling type. The first call has the Type New Start with status Hold.When you want to create a planned order for the first time before reaching the call date, you can use the function release call.Flag the first row in Scheduling List.Choose Release Call.Choose Save and confirm all the messages that appear.To check the automatically created preventive maintenance order, follow these steps:Open Schedule Maintenance Plan again.Enter the maintenance plan number.Choose Enter.In the Scheduling List, choose the first line you have called.Choose Display Call Object.Note the maintenance order number. | The first checking step of the maintenance plan has been scheduled.The preventive maintenance order is created automatically.The notification of activity report is created automatically.The material reservation is created automatically if stock material is needed. |  |

Result

The maintenance plan has been scheduled.

Hint: In case you want to use mass scheduling instead of manually scheduling maintenance plans, you can use the tile Mass Schedule Maintenance Plans (F2774) with the business role Maintenance Planner.

To start mass scheduling, you must have entered a start date in the maintenance plan or have scheduled the maintenance plan once.

### Time-Based Strategy Plan

#### Maintain Maintenance Strategies

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance strategy represents a rule for the sequence of planned maintenance and inspection tasks.

A time based maintenance strategy contains the maintenance packages that define the cycle in which the tasks must be performed, for example, every 10 days, every 3 months, and so on. It contains additional scheduling parameters such as shift factor, preliminary and follow-up buffers, and hierarchy. Maintenance strategies are required in strategy plans.

For each plant, you may use the same maintenance strategy. You can skip this step if the maintenance strategy exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Maintenance Strategy | Open Maintenance Strategies (IP12). | The Display Maintenance Strategies: Overview screen displays. |  |
| 3 | Create Maintenance Strategy | Choose New Entries. Make the following entries.Name:EAM_<XX>Description: <Description> for example: Mechanical InspectionScheduling Indicator: TimeStrategy unit: MONChoose Save. | The new maintenance strategy is created. |  |
| 4 | Add Maintenance Packages | On the left side of the screen, in the Dialog Structure, double-click on the Packages folder.Choose New Entries.Make the following entries:Package No.: 1Cycl. Length: 1Unit: MONMaintenance cycle text: MonthlyCycle short text: 1MHierarchy: 1Hierarchy short text: 1HRepeat the above step for further cycles. Create the following packages.Package No.: 2Cycl. Length: 3Unit: MONMaintenance cycle text: QuarterlyCycle short text: 3MHierarchy: 1Hierarchy short text: 1HPackage No.: 3Cycl. Length: 6Unit: MONMaintenance cycle text: Half-yearlyCycle short text: 6MHierarchy: 1Hierarchy short text: 1HPackage No.: 4Cycl. Length: 12Unit: MONMaintenance cycle text: YearlyCycle short text: 1YHierarchy: 1Hierarchy short text: 1HChoose Save. | The Change Maintenance Packages page displays.The Maintenance Packages are maintained in Maintenance Strategy. |  |

#### Create General Task List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using task lists, you can centrally define and manage maintenance tasks for your technical objects. General task lists can also help you to prepare maintenance plans and orders.

A task list group combines one or more task lists according to their logical features. Within a task list group, each task list is identified by a group counter. This enables you, for example, to combine several task lists in one group. Within the group, the system allocates a sequential number (the group counter) to each individual task list.

Prerequisite

Technical objects in the form of functional locations, equipment, and maintenance assemblies.

Organizational units such as maintenance planners and work centers.

Costs centers defined in the master data of the technical objects.

Maintenance spare parts and assemblies in the MM (Materials Management) module.

Maintenance strategy.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Open Create Task List | Open Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)). | The Create Task List page appears. |  |
| 3 | Choose Task List Type | Choose Task List Type: General Maintenance Task List. | The Create General Maintenance Task List screen displays. |  |
| 4 | Enter Creation Parameters | Make the following entries:Task List Group:Comment: Task list group uses internal number range.Planning Plant: 3310Group Counter:Comment: The group counter would increase automatically if you create another task list for the same technical object.Overall Status: Released (general)Select the relevant profile for the plant.Key Date: <Today>Choose Continue. | The Create General Maintenance Task List page displays. |  |
| 5 | Maintain General Data | Enter the following entries:Description: <Description>Make your own description. For example, Mechanical InspectionStatus: Released (General)Planner Group: YB1Work Center: RES-0100Work Center Plant: 3310Maintenance Strategy: EAM_<XX>Comment: Please use the maintenance strategy created in the previous step.System Condition: not in operationChoose Operation Data. | The Operation Data tab appears. |  |
| 6 | Maintain Operation Data | Enter the following entries and choose Enter.Operation: 0010Description: Check the pumpWork: 2Unit: HCapacities: 2Operation: 0020Description: Check the BearingsWork: 1Unit: HCapacities: 1Operation : 0030Description: Check the couplingWork: 2Unit: HCapacities: 2Operation: 0040Description: Check the shaftWork: 3Unit: HCapacities: 3Choose the operation 0010.In the lower part of the screen, Details: Operation 0010, Check the pump section, choose Materials.Make the following entries and choose Enter.Material: SP005Quantity : 1Repeat the above step for other operationsOperation Item: 0020Material: SP001Quantity: 2Operation Item: 0030Material: SP002Quantity: 1Operation Item: 0040Material: SP003Quantity: 2Choose Maintenance Packages. | The Maintenance Packages tab appears. |  |
| 7 | Maintain Maintenance Packages | Make the following entries and choose Save.For operation 0010, set flag for MonthlyFor operation 0020, set flag for QuarterlyFor operation 0030, set flag for Half-yearlyFor operation 0040, set flag for Yearly | The general task list is created. |  |

#### Create Maintenance Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance item describes which preventive maintenance tasks should take place regularly at a technical object or a group of technical objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Maintenance Items app | Open Manage Maintenance Items (F5356). | The Manage Maintenance Items page appears. |  |
| 3 | Create Maintenance Item | To create a maintenance item, choose Create button on the top of the screen. Enter following details in the dialog box:Item Description: Mechanical Inspection for PumpPlan Category: PM (Maintenance Order)Reference Object Type: EquipmentReference Object: 23310XXXXMaintenance Strategy: EAM_<XX>You can use the maintenance strategy created in the previous step.Task List: <Entry of choice>You can use the task list created in the previous step.Order Type: YBA2.Choose Create.Maintenance Item screen is displayed. Enter following details under Basic Details tab:Maintenance Activity Type: YB4Priority: <Entry of your choice>Choose Create.Note Maintenance items can also be created through the Manage Maintenance Plans (F5325) app. | The maintenance item is created. |  |

#### Create Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance plan will have maintenance or inspection activities to be carried out for technical objects.

The frequency or strategy and, scope of the activities are defined in the maintenance plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Maintenance Plan | Open Manage Maintenance Plans (F5325). | The Manage Maintenance Plan page is displayed. |  |
| 3 | Create Maintenance Plan | To create a maintenance plan, choose Create on the top of the screen. Enter the following details in the dialog box:Plan Description: Mechanical Inspection for PumpPlan Category: Maintenance OrderPlan Type: StrategySelect the Time radio button.Strategy: Entry of your choiceChoose Create. | The Maintenance Plan page is displayed. |  |
| 4 | Maintain Maintenance Plan Item Data | To create a maintenance item choose Create Item button by scrolling down to Maintenance item section. Enter the following details in the popup window:Item Description: Mechanical Inspection for PumpReference Object Type: EquipmentReference Object: 23310XXXXMaintenance Strategy: EAM <XX>Task List: <Entry of choice>You can use the task list created in the previous step.Order Type: YBA2Choose Create.Click on Maintenance Item line and enter following details under Basic Details tab:Maintenance Activity Type: YB4Priority: <Entry of your choice>Choose Apply. | The details of the maintenance item are updated and the Maintenance Plan screen is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | In the Schedule section, make following entries:Scheduling Duration: 365Comment: You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.Start Date for Scheduling: <Current date>Comment: The start date is needed for mass schedule maintenance plans.End Date for Scheduling: <Entry of Choice>In the Scheduling Parameters section, make following entries:Shift Factor for Early Completion (as Percentage): 100Shift Factor for Late Completion (as Percentage): 100Comment: The shift factor in the event of early/late completion of a maintenance task defines the percentage of the shift to be applied to the calculation of the next date.Tolerance for Early Completion (as Percentage): 10Tolerance for Late Completion (as Percentage): 10Comment: The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cycles of the maintenance strategy.Cycle Modification Factor: 1Call Horizon: 50Comment: The call horizon determines when a maintenance call object, for example, a maintenance order should be generated for a maintenance call wrt maintenance planned date.Completion Required: Select Yes or No using the toggle buttonComment: If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.Choose Create. | The maintenance plan is created. |  |
| 6 | Assign Maintenance Item (Optional) | Alternatively, it is possible to assign existing maintenance item to a maintenance plan using the Assign Item button. To assign an item, follow these steps:Open the maintenance plan in Manage Maintenance Plans (F5325) app.Choose Assign Item.Select the required maintenance item and choose OK. | The maintenance item is assigned to the maintenance plan. |  |

#### Schedule Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you schedule your maintenance plan for the first time, you trigger the maintenance cycle. The system uses the scheduling information in the maintenance plan to calculate the maintenance package that is due next.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Schedule Maintenance Plan | Open Schedule Maintenance Plan (IP10). | The Schedule Maintenance Plan: Initial page displays. |  |
| 3 | Search Maintenance Plan | Make the following item entries and choose Enter.MaintenancePlan: <Maintenance Plan number>Use the maintenance plan created in the previous step. | The Schedule Maintenance Plan: Strategy Plan <Maintenance Plan number> page displays. |  |
| 4 | Schedule Maintenance Plan | Choose Start.On the Start Date screen, enter a start date. For example, enter current day's date.Start of cycle: <Current Date>Choose Continue.You receive an overview of scheduled calls with plan date and call date of a schedule call based on the start date you entered and the scheduling parameters that are maintained in the maintenance plan.Comment: The scheduling list shows scheduled calls with assigned call dates. Each call has its own system status with the scheduling type.The first call has the scheduling type New Start with status Hold. When you want to create a planned order for the first time before reaching the call date you can use the function Release Call.Flag the first row in Scheduling List.Choose Release Call.Choose Save and confirm all the messages that appear.To check the automatically created preventive maintenance order:Open Schedule Maintenance Plan again.Enter the maintenance plan number.Choose Enter.In the Scheduling List, choose the first line you have called.Choose Display Call Object.Note the maintenance order number. | The first checking step of maintenance plan has been scheduled.The preventive maintenance order is created automatically.The notification of activity report is created automatically.The material reservation is created automatically if stock material is needed. |  |

Result

The maintenance plan has been scheduled.

Hint: In case you want to use mass scheduling instead of manually scheduling maintenance plans, you can use the tile Mass Schedule Maintenance Plans (F2774) with the business role Maintenance Planner.

To start mass scheduling, you must have entered a start date in the maintenance plan or have scheduled the maintenance plan once.

### Performance-Based Single Cycle Plan

#### Create General Task List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using task lists, you can centrally define and manage maintenance tasks for your technical objects. General task lists can also help you prepare maintenance plans and orders.

A task list group combines one or more task lists according to their logical features. Within a task list group, each task list is identified by a group counter. This enables you, for example, to combine several task lists in one group. Within the group, the system allocates a sequential number (the group counter) to each individual task list.

Prerequisite

Technical objects in the form of functional locations, equipment, and maintenance assemblies.

Organizational units such as maintenance planners and work centers.

Costs centers defined in the master data of the technical objects.

Maintenance spare parts and assemblies in the Materials Management (MM) module.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner . | The SAP Fiori launchpad displays. |  |
| 2 | Open Create Task List | Open Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)). | The Create Task List screen displays. |  |
| 3 | Choose Your Task List Type | Choose Task List Type : General Maintenance Task List | The Create General Maintenance Task List screen appears. |  |
| 4 | Enter Creation Parameters | Make the following entries:Task List Group:Comment: The task list group uses internal number range.Planning Plant: 3310Group Counter:Comment: The group counter would increase automatically if you create another task list for the same technical object.Overall Status: Released (general)Select the relevant profile for the plant.Key Date: <Today>Choose Continue. | The Create General Maintenance Task List screen displays. |  |
| 5 | Maintain General Data | Make the following entries:Description: DescriptionMake your own description. For example, Mechanical InspectionOverall Status: Released (General)Planner Group: YB1Work Center: RES-0100Work Center Plant: 3310System Condition: not in operationChoose Operation Data. | The Operation Data tab displays. |  |
| 6 | Maintain Operation Data | Enter the following entries and choose Enter.Operation: 0010Description: Check the pumpWork: 2Unit: HCapacities: 2Operation: 0020Description: Check the bearingsWork: 1Unit: HCapacities: 1Operation : 0030Description: Check the couplingWork: 2Unit: HCapacities: 2Operation: 0040Description: Check the shaftWork: 3Unit: HCapacities: 3Choose the Operation 0010.In the lower part of the screen, Details: Operation 0010, check the pump section, choose Materials.Make the following entries and choose Enter.Material: SP005Quantity: 1Repeat the above step for other operationsOperation Item: 0020Material: SP001Quantity: 2Operation Item: 0030Material: SP002Quantity: 1Operation Item: 0040Material: SP003Quantity: 2Choose Save | The general task list is created. |  |

#### Create Maintenance Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance item describes which preventive maintenance tasks should take place regularly at a technical object or a group of technical objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Maintenance Items app | Open Manage Maintenance Items (F5356). | The Manage Maintenance Items page appears. |  |
| 3 | Create Maintenance Item | To create a maintenance item, choose Create button on the top of the screen. Enter following details in the popup window:Item Description: Mechanical Inspection for PumpPlan Category: PM (Maintenance Order)Reference Object Type: EquipmentReference Object: 23310XXXXTask List: <Entry of choice>You can use the task list created in the previous step.Order Type: YBA2.Choose Create.Maintenance Item screen is displayed. Enter following details under Basic Details tab:Maintenance Activity Type: YB4Priority: <Entry of your choice>Choose Create.Note Maintenance items can also be created through the Manage Maintenance Plans (F5325) app. | The maintenance item is created. |  |

#### Create Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance plan will have maintenance or inspection activities to be carried out for technical objects.

The frequency or strategy and, scope of the activities are defined in the maintenance plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Maintenance Plan | Open Manage Maintenance Plans (F5325) | The Manage Maintenance Plan screen is displayed. |  |
| 3 | Create Maintenance Plan | To create a maintenance plan, choose Create on the top of the screen. Enter the following details in the dialog box:Plan Description: Mechanical Inspection for PumpPlan Category: Maintenance OrderPlan Type: Single Cycle (Performance Based)Choose Create. | The Maintenance Plan screen is displayed. |  |
| 4 | Maintain Maintenance Plan Item Data | To create a maintenance item choose Create Item button by scrolling down to Maintenance item section. Enter following details in the pop-up window-Item Description: Mechanical Inspection for PumpReference Object Type: EquipmentReference Object: 23310XXXXTask List: Entry of your choiceYou can use the task list created in the previous step.Order Type: YBA2Choose Create.Click on Maintenance Item line and enter following details under Basic Details tab:Maintenance Activity Type: YB4Priority: <Entry of your choice>Choose Apply. | The Maintenance Plan Planning Data screen is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | In the Cycle section, make the following entries:Cycle Length: 100Cycle UoM: HComment: Cycle Length/Cycle UoM defines the duration in which the maintenance is to be executed.Cycle Text: Every 100 HoursCounter: < Measuring Point No >Comment: Enter the measuring point number created for the technical object type. Based on readings entered according to the mentioned measuring point, maintenance call will be trigerred once the plan is scheduled.In the Schedule section, enter the following:Scheduling Duration: 365Comment: You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.End Date for Scheduling: <Entry of Choice>In the Scheduling Parameters section, enter the following:Shift Factor for Early Completion (as Percentage): 100Shift Factor for Late Completion (as Percentage): 100Comment: The shift factor in the event of early/late completion of a maintenance task defines the percentage of the shift to be applied to the calculation of the next date.Tolerance for Early Completion (as Percentage): 10Tolerance for Late Completion (as Percentage): 10Comment: The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cycles of the maintenance strategy.Cycle Modification Factor: 1Call Horizon: 50Comment: The call horizon determines when a maintenance call object, for example, a maintenance order should be generated for a maintenance call for the maintenance planned date.Completion Required: Select Yes or No using the toggle buttonComment: If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.Choose Create. | The maintenance plan is created. |  |
| 6 | Assign Maintenance Item (Optional) | Alternatively, it is possible to assign existing maintenance item to a maintenance plan using the Assign Item button. To assign an item, follow these steps:Open the maintenance plan in Manage Maintenance Plans (F5325) app.Choose Assign Item.Select the required maintenance item and choose OK. | The maintenance item is assigned to the maintenance plan. |  |

#### Create Measurement Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Maintenance Planner needs to record initial reading of the technical objects (equipment / functional location) in the SAP system. At least one measurement document is required for scheduling the plan. Once the scheduling is done, regular readings must also be recorded in the system by the Maintenance Technician. This process can also be automated my making use of systems which get the reading from technical objects and load to SAP system through interfaces.

Time-to-time recording of these readings are relevant for accurate determination of maintenance due dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Create Measurement Document | Open Create Measurement Document for Technical Object (EAMS_WDA_MD_OIF).On the Create Measurement Documents screen, make the following entries:Basis for Measurement Reading:Measuring PointMeasuring Point: <Measuring Point No>Comment: Enter the measuring point number created against the technical object.Choose Continue. | The Create Measurement Documents screen displays. |  |
| 3 | Enter Counter | A new screen appears with the measuring point that was entered.Enter Reading: <Counter reading>Choose Save. | The measurement document is created. |  |

Result

The measurement documents are created and they help to determine the accurate maintenance due dates.

#### Schedule Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you schedule your maintenance plan for the first time, you trigger the maintenance cycle. The system uses the scheduling information in the maintenance plan to calcu-late the due date of the maintenance call object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Open Schedule Maintenance Plan | Open Schedule Maintenance Plan (IP10). | The Schedule Maintenance Plan: Initial screen displays. |  |
| 3 | Search Maintenance Plan | Make the following item entries and choose Enter.Maintenance Plan: <Maintenance Plan number>Use the single cycle plan (perfomance-based) created in the previous step. | The Schedule Maintenance Plan: Single Cycle Plan <Maintenance Plan number> screen displays. |  |
| 4 | Schedule Maintenance Plan | Follow these steps:Choose Start.On the Start Date screen, enter a start date. For example, enter current date.Start of cycle:<Counter reading >Note If a start counter reading was entered during the maintenance plan creation, the system will propose that reading as the start counter reading. It can be changed to a different reading as well, if required.Choose Continue.You will receive an overview of scheduled calls with plan date and call date of a scheduled call.The overview is based on your start of cycle counter reading, annual estimate (entered against respective measuring point), and scheduling parameters that are maintained in the maintenance plan.Comment: The scheduling list shows scheduled calls with assigned call dates. Each call has its own system status with scheduling type. The first call has the type New Start with status Hold.When you want to create a planned order for the first time before reaching the call date, you can use the function Release Call.Flag the first row in the scheduling list.Choose Release Call.Choose Save and confirm all the messages that appear.To check the automatically created preventive maintenance order:Open the schedule maintenance plan again.Enter the maintenance plan number.Choose Enter.In the Scheduling List, choose the first line you have called.Choose Display Call Object.Note the maintenance order number. | The first checking step of maintenance plan has been scheduled.The preventive maintenance order is created automatically.The notification of activity report is created automatically.The material reservation is created automatically if stock material is needed. |  |

Result

The maintenance plan has been scheduled.

Hint: In case you want to use mass scheduling instead of manually scheduling maintenance plans, you can use the tile Mass Schedule Maintenance Plans (F2774) with the business role Maintenance Planner.

To start mass scheduling, you must have entered a start date in the maintenance plan or have scheduled the maintenance plan once.

### Performance-Based Strategy Plan

#### Maintain Maintenance Strategies

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance strategy represents a rule for the sequence of planned maintenance and inspection tasks. A maintenance strategy for performance plan contains the maintenance packages that define the cycle in which the tasks must be performed. For example, every 5000 km, every 500 operating hours, and so on. It contains additional scheduling parameters such as shift factor, preliminary and follow-up buffers, and hierarchy. Maintenance strategies are required in strategy plans.

For each plant, you may use the same maintenance strategy. You can skip this step if the maintenance strategy exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Open Maintenance Strategy | Open Maintenance Strategies (IP12). | The Display Maintenance Strategies: Overview screen displays. |  |
| 3 | Create Maintenance Strategy | Choose New Entries. Make the following entries.Name: EAM_<XX>Description: <Description> for example: Mechanical InspectionScheduling Indicator: ActivityStrategy unit: HChoose Save. | The new maintenance strategy is created. |  |
| 4 | Add Maintenance Packages | On the left side of the screen, in Dialog Structure, double-click on the Packages folder.Choose New Entries.Make the following entries:Package No.: 1Cycl. Length: 100Unit: HMaintenance cycle text: 100OPHCycle short text: 1HHierarchy: 1Hierarchy short text: 1HRepeat the above step for further cycles. Create the following packages.Package No.: 2Cycl. Length: 250Unit: HMaintenance cycle text: 250 OPHCycle short text: 2HHierarchy: 1Hierarchy short text: 1HPackage No.: 3Cycl. Length: 500Unit: HMaintenance cycle text: 500 OPHCycle short text: 3HHierarchy: 1Hierarchy short text: 1HPackage No.: 4Cycl. Length: 1000 OPHUnit: HMaintenance cycle text: 1000 OPHCycle short text: 4HHierarchy: 1Hierarchy short text: 1HChoose Save. | The Change Maintenance Packages page displays.The maintenance packages are maintained in Maintenance Strategy. |  |

#### Create General Task List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using task lists, you can centrally define and manage maintenance tasks for your technical objects. General task lists can also help you to prepare maintenance plans and orders.

A task list group combines one or more task lists according to their logical features. Within a task list group, each task list is identified by a group counter. This enables you, for example, to combine several task lists in one group. Within the group, the system allocates a sequential number (the group counter) to each individual task list.

Prerequisite

Technical objects in the form of functional locations, equipment, and maintenance assemblies.

Organizational units such as maintenance planners and work centers.

Costs centers defined in the master data of the technical objects.

Maintenance spare parts and assemblies in the Materials Management (MM) module.

Maintenance strategy.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Open Create Task List | Open Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)). | The Create Task List screen appears |  |
| 3 | Choose Task List Type | Choose Task List Type: General Maintenance Task List. | The Create General Maintenance Task List screen displays. |  |
| 4 | Enter Creation Parameters | Make the following entries.Task List Group:Comment: Task List Group uses internal number range.Planning Plant: 3310Group Counter:Comment: The group counter would increase automatically if you create another task list for the same technical object.Overall Status: Released (general)Select the relevant profile for the plant.Key Date:<Today>Choose Continue. | The Create General Maintenance Task List screen displays. |  |
| 5 | Maintain General Data | Make the following entries:Description:<Description>Make your own description. For example: Mechanical InspectionStatus: Released (General)Planner Group: YB1Work Center: RES-0100Work Center Plant: 3310Maintenance Strategy: EAM_<XX>Comment: You can use the maintenance strategy created in the previous step.System Condition: not in operationChoose Operation Data. | The Operation Data tab appears. |  |
| 6 | Maintain Operation Data | Make the following entries and choose Enter.Operation: 0010Description: Check the pumpWork: 2Unit: HCapacities: 2Operation: 0020Description: Check the bearingsWork: 1Unit: HCapacities: 1Operation : 0030Description: Check the couplingWork: 2Unit: HCapacities: 2Operation: 0040Description: Check the shaftWork: 3Unit: HCapacities: 3Choose the Operation 0010.In the lower part of the screen, Details: Operation 0010, check the pump section. Choose Materials.Make the following entries and choose Enter.Material: SP005Quantity: 1Repeat the above step for other operations.Operation Item: 0020Material: SP001Quantity: 2Operation Item: 0030Material: SP002Quantity: 1Operation Item: 0040Material: SP003Quantity: 2Choose Maintenance Packages. | The Maintenance Packages tab appears. |  |
| 7 | Maintain Mainte-nance Packages | Enter the following entries and choose Save.For Operation 0010, set Flag for 100 OPHFor Operation 0020, set Flag for 250 OPHFor Operation 0030, set Flag for 500 OPHFor Operation 0040, set Flag for 1000 OPH | The general task list is created. |  |

#### Create Maintenance Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance item describes which preventive maintenance tasks should take place regularly at a technical object or a group of technical objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Maintenance Items app | Open Manage Maintenance Items (F5356). | The Manage Maintenance Items page appears. |  |
| 3 | Create Maintenance Item | To create a maintenance item, choose Create button on the top of the screen. Enter following details in the popup window:Item Description: Mechanical Inspection for PumpPlan Category: PM (Maintenance Order)Reference Object Type: EquipmentReference Object: 23310XXXXMaintenance Strategy : EAM_<XX>You can use the maintenance strategy created in the previous step.Task List: <Entry of choice>You can use the task list created in the previous step.Order Type: YBA2.Choose Create.Maintenance Item screen is displayed. Enter following details under Basic Details tab:Maintenance Activity Type: YB4Priority: <Entry of your choice>Choose Create.Note Maintenance items can also be created through the Manage Maintenance Plans (F5325) app. | The maintenance item is created. |  |

#### Create Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance plan will have maintenance or inspection activities to be carried out for technical objects.

The frequency or strategy and, scope of the activities are defined in the maintenance plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Maintenance Plan | Open Manage Maintenance Plans (F5325) | The Manage Maintenance Plan screen is displayed. |  |
| 3 | Create Maintenance Plan | To create a maintenance plan, choose Create on the top of the screen. Enter the following details in the dialog box:Plan Description: Mechanical Inspection for PumpPlan Category: Maintenance OrderPlan Type: StrategySelect Counter radio button.Reference Object Type: EquipmentStrategy: Entry of your choiceChoose Create. | The Maintenance Plan screen is displayed. |  |
| 4 | Maintain Maintenance Plan Item Data | To create a maintenance item choose Create Item button by scrolling down to Maintenance item section. Enter following details in the pop-up window-Item Description: Mechanical Inspection for PumpReference Object Type: EquipmentReference Object: 23310XXXXMaintenance Strategy: EAM_<XX>You can use the maintenance strategy created in the previous step.Task List: Entry of your choiceYou can use the task list created in the previous step.Order Type: YBA2Choose Create.Click on Maintenance Item line and enter following details under Basic Details tab:Maintenance Activity Type: YB4Priority: <Entry of your choice>Choose Apply. | The Maintenance Plan Planning Data screen is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | In the Cycle section, make following entries:Counter: <Measuring Point No>Comment: Enter the measuring point number created for the technical object type. Based on readings entered according to the mentioned measuring point, the maintenance call will be triggered once the plan is scheduled.In the Schedule section, enter the following:Scheduling Duration: 365Comment: You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.Start Counter Reading for Scheduling: <Entry of Choice>End Counter Reading for Scheduling: <Entry of Choice>In the Scheduling Parameters section, make following entries:Shift Factor for Early Completion (as Percentage): 100Shift Factor for Late Completion (as Percentage): 100Comment: The shift factor in the event of early/late completion of a maintenance task defines the percentage of the shift to be applied to the calculation of the next date.Tolerance for Early Completion (as Percentage): 10Tolerance for Late Completion (as Percentage): 10Comment: The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cycles of the maintenance strategy.Cycle Modification Factor: 1Call Horizon: 50Comment: The call horizon determines when a maintenance call object, for example, a maintenance order should be generated for a maintenance call according to the maintenance planned date.Completion Required: Select Yes or No using the toggle buttonComment: If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.Choose Create. | The maintenance plan is created. |  |
| 6 | Assign Maintenance Item (Optional) | Alternatively, it is possible to assign existing maintenance item to a maintenance plan using the Assign Item button. To assign an item, follow these steps:Open the maintenance plan in Manage Maintenance Plans (F5325) app.Choose Assign Item.Select the required maintenance item and choose OK. | The maintenance item is assigned to the maintenance plan. |  |

#### Create Measurement Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance Planner needs to record initial reading of the technical objects (equipment / functional location) in the SAP system. Atleast one measurement document is required for scheduling the plan. Once scheduling is done, regular readings must also be recorded in the system by the Maintenance Tehnician. This process also can be automated my making use of the systems which gets the reading from technical objects and loads to SAP system through interfaces.

Time-to-time recording of these readings are relevant for accurate determination of maintenance due dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Create Measurement Document | Open Create Measurement Document for Technical Object (EAMS_WDA_MD_OIF)On the Create Measurement Documents screen, make the following entries:Basis for measurement reading: Measuring PointMeasuring Point: < Measuring Point No>Comment: Enter the measuring point number that was created against the technical object.Choose Continue. | The Create Measurement Documents screen displays. |  |
| 3 | Enter Counter Reading | A new screen appears with the measuring points you entered:Reading: <Counter reading >Choose Save | Measurement document is created. |  |

Result

The measurement documents are created and these will serve to determine the accurate maintenance due dates.

#### Schedule Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you schedule your maintenance plan for the first time, you trigger the maintenance cycle. The system uses the scheduling information in the maintenance plan to calculate the maintenance package that is due next.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Open Schedule Maintenance Plan | Open Schedule Maintenance Plan (IP10). | The Schedule Maintenance Plan: Initial screen displays. |  |
| 3 | Search Maintenance Plan | Make the following item entries and choose Enter.Maintenance Plan: <Maintenance Plan number>You can use the maintenance strategy created in the previous step. | The Schedule Maintenance Plan: Strategy Plan <Maintenance Plan number> screen displays. |  |
| 4 | Schedule Maintenance Plan | Follow these steps:Choose Start.Start of cycle: <Current counter reading>Choose Continue.You receive an overview of scheduled calls with plan date and call date of a schedule call based on the start date you entered and on the scheduling parameters maintained in the maintenance plan.Comment: The scheduling list shows scheduled calls with assigned call dates. Each call has its own system status with the scheduling type.The first call has the Type New Start with Status Hold. When you want to create a planned order for the first time before reaching the call date you can use the function Release Call.Flag the first row in Scheduling List.Choose Release Call.Choose Save and confirm all the messages that appear.To automatically check the created preventive maintenance order, follow these steps:Open Schedule Maintenance Plan again.Enter the maintenance plan number.Choose EnterIn the Scheduling List, choose the first line you have called.Choose Display Call Object.Note the maintenance order number. | The first checking step of maintenance plan has been scheduled.The preventive maintenance order is created automatically.The notification of activity report is created automatically.The material reservation is created automatically if stock material is needed. |  |

Result

The maintenance plan has been scheduled.

Hint: In case you want to use mass scheduling instead of manually scheduling maintenance plans, you can use the tile Mass Schedule Maintenance Plans (F2774) with the business role Maintenance Planner.

To start mass scheduling, you must have entered a start date in the maintenance plan or have scheduled the maintenance plan once.

### Multiple Counter Plan

#### Create General Task List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Using task lists, you can centrally define and manage maintenance tasks for your technical objects. General task lists can also help you to prepare maintenance plans and orders.

A task list group combines one or more task lists according to their logical features. Within a task list group, each task list is identified by a group counter. This enables you, for example, to combine several task lists in one group. Within the group, the system allocates a sequential number (the group counter) to each individual task list.

Prerequisite

Technical objects in the form of functional locations, equipment, and maintenance assemblies.

Organizational units such as maintenance planners and work centers.

Costs centers defined in the master data of the technical objects.

Maintenance spare parts and assemblies in the MM (Materials Management) module.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Open Create Task List | Open Create Task List (EAMS_WDA_TL_OIF_V2 (EAMS_WDA_TL_OIF_CFG_V2)). | The Create Task List screen appears. |  |
| 3 | Choose Task List Type | Choose Task List Type: General Maintenance Task List. | The Create General Maintenance Task List screen displays. |  |
| 4 | Enter Creation Parameters | Make the following entries:Task List Group:Comment: The task list group uses internal number range.Planning Plant: 3310Group Counter:Comment: The group counter would increase automatically if you create another task list for the same technical object.Overall Status: Released (general)Select the relevant profile for the plant.Key Date: <Today>Choose Continue. | The Create General Maintenance Task List screen displays. |  |
|  | Maintain General Data | Make the following entries:.Description:<Description>Make your own description. For example: Mechanical InspectionStatus: Released (General)Planner Group: YB1Work Center: RES-0100Work Center Plant: 3310System Condition: not in operationChoose Operation Data. | The Operation Data tab appears. |  |
|  | Maintain Operation Data | Make the following entries and choose Enter.Operation: 0010Description: Check the pumpWork: 2Unit: HCapacities: 2Operation: 0020Description: Check the bearingsWork: 1Unit: HCapacities: 1Operation : 0030Description: Check the couplingWork: 2Unit: HCapacities: 2Operation: 0040Description: Check the shaftWork: 3Unit: HCapacities: 3Choose the Operation 0010.In the lower part of the screen, Details: Operation 0010, check the pump section, choose Materials.Make the following entries and choose Enter.Material: SP005Quantity : 1Repeat the above step for other operationsOperation Item: 0020Material: SP001Quantity: 2Operation Item: 0030Material: SP002Quantity: 1Operation Item: 0040Material: SP003Quantity: 2Choose Save | The general task list is created. |  |

#### Create Maintenance Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A maintenance item describes which preventive maintenance tasks should take place regularly at a technical object or a group of technical objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Maintenance Planner. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Open Manage Maintenance Items app | Open Manage Maintenance Items (F5356). | The Manage Maintenance Items page appears. |  |
| 3 | Create Maintenance Item | To create a maintenance item, choose Create button on the top of the screen. Enter following details in the popup window:Item Description: Mechanical Inspection for PumpPlan Category: PM (Maintenance Order)Reference Object Type: EquipmentReference Object: 23310XXXXTask List: <Entry of choice>You can use the task list created in the previous step.Order Type: YBA2.Choose Create.Maintenance Item screen is displayed. Enter following details under Basic Details tab:Maintenance Activity Type: YB4Priority: <Entry of your choice>Choose Create.Note Maintenance items can also be created through the Manage Maintenance Plans (F5325) app. | The maintenance item is created. |  |

#### Create Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance plan will have maintenance or inspection activities to be carried out for technical objects.

The frequency or strategy and, scope of the activities are defined in the maintenance plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Create Maintenance Plan | Open Manage Maintenance Plans (F5325) | The Mangae Maintenance Plan screen is displayed. |  |
| 3 | Create Maintenance Plan | To create a maintenance plan, choose Create on the top of the screen. Enter the following details in the dialog box:Plan Description: Mechanical Inspection for PumpPlan Category: Maintenance RequestPlan Type: StrategySelect the Counter radio button.Strategy: Entry of your choiceChoose Create. | The Maintenance Plan screen is displayed. |  |
| 4 | Maintain Maintenance Plan Item Data | To create a maintenance item choose Create Item by scrolling down to the Maintenance item section. Enter the following details in the dialog box:Item Description: Mechanical Inspection for PumpReference Object Type: EquipmentReference Object: 23310XXXXTask List Type: Entry of your choiceYou can use the task list created in the previous step.Order Type: YBA2Choose Create.Click on Maintenance Item line and enter following details under Basic Details tab:Maintenance Activity Type: YB4Priority: <Entry of your choice>Choose Apply. | The Maintenance Plan Planning Data screen is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | In the Cycle section, enter the following:Operator : Choose OR type using the toggle switch.If you select the OR operation, it means that a notification will be created for the earliest planned date. It is the case that occurs first.If you select the AND operation, it means that a notification will be created for the last planned date. It is the case that occurs last.Choose Create and enter the following:Cycle Length: 100 HComment: The cycle length defines the duration in which the maintenance is to be executed.Cycle Text: Every 100 HoursCounter: <Counter No>Comment: Enter the counter number created for the technical object type. Readings entered according to the mentioned counter number will be used to trigger the maintenance call object.Again choose Create and enter the following:Cycle Length: 6 MONComment: The cycle length defines the duration in which the maintenance is to be executed.Cycle Text: Every 6 MonthsIn the Schedule section, enter the following:Scheduling Duration: 365Comment: You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.Start Date for Scheduling: <Current date>Comment: The start date is needed for mass schedule maintenance plans.End Date for Scheduling: <Entry of Choice>In the Scheduling Parameters section, make following entries:Shift Factor for Early Completion (as Percentage): 100Shift Factor for Late Completion (as Percentage): 100Comment: The shift factor in the event of early/late completion of a maintenance task defines the percentage of the shift to be applied to the calculation of the next date.Tolerance for Early Completion (as Percentage): 10Tolerance for Late Completion (as Percentage): 10Comment: The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cycles of the maintenance strategy.Cycle Modification Factor: 1Completion Required: Select Yes or No using the toggle buttonComment: If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.Choose Create. | The maintenance plan is created. |  |
| 6 | Assign Maintenance Item (Optional) | Alternatively, it is possible to assign existing maintenance item to a maintenance plan using the Assign Item button. To assign an item, follow these steps:Open the maintenance plan in Manage Maintenance Plans (F5325) app.Choose Assign Item.Select the required maintenance item and choose OK. | The maintenance item is assigned to the maintenance plan. |  |

#### Create Measurement Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Maintenance Planner needs to record initial reading of the technical objects (equipment / functional location) in the SAP system. Atleast one measurement document is required for scheduling the plan.

Once the scheduling is done, regular readings must also be recorded in the system by the Maintenance Technician.

This process can also be automated my making use of systems which get the reading from technical objects and loads to SAP system through interfaces.

Time-to-time recording of these readings are relevant for accurate determination of maintenance due dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Create Measurement Document | Open Create Measurement Document for Technical Object (EAMS_WDA_MD_OIF).On the Create Measurement Documents screen, make the following entries:Basis for measurement reading: Measuring PointMeasuring Point: <Measuring Point No>Comment: Enter the measuring point number created against the technical object.Choose Continue. | The Create Measurement Documents screen displays. |  |
| 3 | Enter Counter Reading | A new screen appears with measuring point you entered.Reading: <Counter Reading>Choose Save. | The measurement document is created. |  |

Result

Measurement documents are created and these will help to schedule maintenance plan.

#### Schedule Maintenance Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you schedule your maintenance plan for the first time, you trigger the maintenance cycle. The system uses the scheduling information in the maintenance plan to calculate the maintenance package that is due next.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Schedule Maintenance Plan | Open Schedule Maintenance Plan (IP10). | The Schedule Maintenance Plan: Initial screen displays. |  |
| 3 | Search Maintenance Plan | Make the following item entries and choose Enter:Maintenance Plan: <Maintenance Plan number>You can use the multiple counter plan created in the previous step. | The Schedule Maintenance Plan: Single Cycle Plan <Maintenance Plan Number screen displays. |  |
| 4 | Schedule Maintenance Plan | Choose Start.Choose Continue button on the information screens which appear.Choose Save buttonYou receive an overview of scheduled calls with plan date and call date of the scheduled call. This is based on your start of cycle counter reading, annual estimate (entered against respective measuring point), and the scheduling parameters maintained in the maintenance plan.Comment: The Scheduling List shows scheduled calls with assigned call dates. Each call has its own system status with scheduling type. The first call has the type New Start with status Hold.When you want to create a planned order for the first time before reaching the call date, you can use the function Release Call.Flag the first row in Scheduling List.Choose Release Call.Choose Save and confirm all the messages if appear.To check the automatically created preventive maintenance order, follow these steps:Open Schedule Maintenance Plan again.Enter the maintenance plan number.Choose Enter.In the Scheduling List, choose the first line you have called.Choose Display Call Object.Note the maintenance order number. | The first checking step of maintenance plan has been scheduled.The preventive maintenance order is created automatically.The notification of activity report is created automatically.The material reservation is created automatically if stock material is needed. |  |

Result

The maintenance plan has been scheduled.

Hint: In case you want to use mass scheduling instead of manually scheduling maintenance plans, you can use the tile Mass Schedule Maintenance Plans (F2774) with the business role Maintenance Planner.

To start mass scheduling, you must have entered a start date in the maintenance plan or have scheduled the maintenance plan once.

### Order Processing

#### Release Preventive Maintenance Order and Print to Job List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The maintenance order is used to collect all costs for a maintenance task and to debit the cost center that incurred the costs using the settlement functions in the CO module (Controlling).

Hint: Before or after you release the maintenance order, you can use tile Schedule Material Availability Check with business role Maintenance Planner to run material ATP check for daily check. If parts are missing, the maintenance order will show system status MSPT Material shortage when you check the maintenance order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Find Maintenance Orders - Completion (F2175). | The Maintenance Order screen is displayed. |  |
| 3 | Search for Order Number | On the Maintenance Order screen, make the following entries:Order Type: Preventive MaintenanceChoose GO.Choose the order that you created in the previous step. | Order list is displayed. |  |
| 4 | Navigate to Change Maintenance Order | Click the description of the order and choose Change Maintenance Order. | Change Maintenance Order screen is displayed. |  |
| 5 | Set Order Status | Choose Set System Status > Release and choose Save. | The maintenance order is released. |  |
| 6 | Print Job Card | Choose Additional Functions > Print. On the next screen, select the Select All checkbox and choose OK. | The job card is printed. |  |

#### Confirm Preventive Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After finishing the preventive maintenance, we have to confirm the order to record the real work time and the spare parts consumption. The data would be used for follow-up cost evaluation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Technician. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Confirm Jobs | Open Perform Maintenance Jobs (F5104A) . | The app opens. |  |
| 3 | Access Order Operations | Use the filter on the top to enter the order ID and choose Go. | A list of operations for the selected order is displayed. |  |
| 4 | Assign Operation | Select the operation and choose Assign to Me.The Assign to Me button is enabled only if the order operation is not assigned to anyone. | The operation is assigned to you. |  |
| 5 | Select the Operation for Processing | Choose the operations to navigate to the Perform Maintenance Job screen. | It will display the Perform Maintenance Job screen for the operation which was selected on the list page. |  |
| 6 | Start the Operation | Choose Start. | The order status is updated with JIPR (Job In Process) |  |
| 7 | Review components | Check the components which are associated with the order in the respective section on the Perform Maintenance Jobs screen. | It will show the list of components that are associated with the order. |  |
| 8 | Goods Issue or Return (Optional) | Go to Components tabChoose Post.The Post Goods Issue screen is displayed. Enter the required quantity and choose Post.Choose Return for the material that has to be returnedThe Return Goods screen is displayed. Enter the required quantity and choose Return.A new line item for the material is generatedChoose Post.The Post Goods Return screen is displayed. Enter the required quantity and choose Post. | Material is issued or returned. |  |
| 9 | Review Attachments | Check the Attachments tab which is associated with the order in the respective section on the Perform Maintenance Jobs screen. | It will show the list of attachments associated with the order. |  |
| 10 | Pause and Resume Work | Choose Pause button to pause the work.After you pause the work, you can restart the work by choosing Resume. | Work is paused or resumed. |  |
| 11 | Time Confirmation | Choose Record Time on the top left corner of the operation object page to perform time confirmation. The Record Time screen is displayed. Enter the following:Actual work. For example, 4 hoursRemaining work, if any. For example, 2 hours.Enter the confirmation text as required.Select the check box Final Confirmation and choose Record when the time confirmation for the operation is completed.This needs to be repeated for all the operations. | You will receive a message confirming that the time confirmations have been posted. You can view the number of time confirmations that have been posted in the Operation Details screen.The progress of work is shown as 100 %. |  |

#### Create Follow-On Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use this function to create maintenance orders as follow-on orders for an order or order operation. When you create a follow-on order, you create a relationship to the reference order or operation. You can display this relationship in the document flow.

You can create follow-on orders directly from Fiori tile Create Maintenance Order (EAMS_WDA_ORDNTF_OIF (EAMS_WDA_ORDNTF_OIF_CFG)) or when you change or display an order.

You can display the relationship between the preceding order and the follow-on order in a hierarchical structure using the document flow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Search for Confirmed Preventive Maintenance Order | Follow these steps:Choose Search in the upper right area of the launchpad.In the drop down list of Search In, choose Maintenance Orders.Fill in the field Search In: Maintenance Orders with order number which is noted in the previous step.Choose Search. | The system displays the found maintenance order in the list of results. |  |
| 3 | Choose Your Preventive Maintenance Order | Choose Change Maintenance Order in the Results view. | The Change Preventive Maintenance: xxxxxxx screen appears. |  |
| 4 | Created Follow-on Order | On the Change Preventive Maintenance: xxxxxxx page, choose Additional Functions > Create Follow-On Order.Or you can follow these steps:Choose Operation Data tab.Right-click on the operation entries.Choose Create Follow-On Order from the context menu to copy the operations. | The Create Order screen displays. |  |
| 5 | Maintain Follow-On Order Parameters | Make the following entries:Order Type: Corrective MaintenancePriority:Technical Object: <Technical Object>Comment: Use the technical object you used in previous step for Preventive Maintenance Order.Assembly:Planning Plant: 3310Business Area:In the Create by Copying area, make the following entries:Order / Operation: <Preventive Maintenance Order / Operation number>Comment: Keep the default valuesCreate Follow-On Order: XYou may check the following options to copy the relevant data from original preventive maintenance order. For this testing, keep the default values.Operations:Components:Relationships:Document Links:Settlement Rules:Order Descriptions:Choose Continue. | The Create Maintenance Order: %00000000001 screen displays. |  |
|  | Maintain the General Data of the Follow-On Order | On the General Data tab, make the following entries:Description: <Description>Priority: <Priority>Required Start:<Start Date>Required End:<End Date>Assembly:System Condition: <System Condition>Choose Operation Data tab. | The Operation Data tab displays. |  |
|  | Maintain the Operation Data of the Follow-On Order | On the Operation Data tab, make the following entries:Description: <Operation Description>Work: <Work time>Number of Capacities: <Number of Capacities>In the Details: Operation xxxx section, choose Material tab. Switch Materials to Standard view.Make the following entries:Material: <Material> for example: SP001Quantity: <Quantity> for example: 1 |  |  |
|  | Save the Follow-On Order. | Choose Check Entries. Choose Save. | The follow-on order is saved. A left arrow flag represents follow-on order.You can check the follow-on order in Display Maintenance Order with menu.You can also check by going to Display Document Flow (IW12) > Follow-On Orders. |  |

Result

The follow-on corrective maintenance order is created. You can continue testing the following business process for the follow-on order:

| Process | Business Condition |
| --- | --- |
| Corrective Maintenance (BH1)Release Maintenance OrderConfirm Maintenance OrderShow Costs on Maintenance OrderTechnically Complete Maintenance Order | A follow-on corrective maintenance order is created. |

#### Show Costs on Preventive Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The planned and actual costs are displayed here.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Find Maintenance Orders - Completion (F2175). | The Maintenance Order screen displays. |  |
| 3 | Search Confirmed Maintenance Order | On the Maintenance Order screen, search for your confirmed order either by plain text in Search field or via applying some filters. For example:Order Type: Preventive MaintenanceTechnical Object: <Technical Object ID>Order Status: ReleasedChoose GO.Choose the order line that you confirmed in the previous step. |  |  |
| 4 | Review Costs | Follow these steps:Choose the Costs tab.Check the costs. | The preventive maintenance order cost is reviewed. |  |

#### Technically Complete Preventive Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If an order is executed, it must be completed in the system to be dealt with. In the Plant Maintenance module, there are two types of completion, technical completion and business completion.

Technical completion shows that an order was technically successful (or can be seen as technically completed by Plant Maintenance).

The following process shows how technical completion works.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as aMaintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Find Maintenance Orders - Completion (F2175). | The Maintenance Order screen is displayed. |  |
| 3 | Search for Order Number | On the Maintenance Order screen, make the following entries:Order Type: Preventive MaintenanceAnd choose GO.Choose the order that you confirmed in the previous step. |  |  |
| 4 | Navigate to Change Maintenance Order | Choose Related Apps at the upper right corner of the screen, and choose Change Maintenance Order. |  |  |
| 5 | Set Complete (Technically) Status | Choose Set System Status > Complete Technically . | The Complete(Technically) screen is displayed. |  |
| 6 | Reference Data | Make the following entries:Reference Date: <Date>Reference Time: <Time>Complete Assigned Notifications: flag setChoose OKChoose Save. | The Complete (Technically) status for the maintenance order is done. |  |

#### Review Document Flow of Preventive Maintenance Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can display the document flow of the order in a hierarchical list. You can then select the order in the document flow and choose Follow-On Orders. The system displays the relationship between the preceding order and the follow-on order. This list displays at most one level above and one level below the selected order. In other words, only the orders directly preceding and directly following the order that you selected are displayed.

If you have created follow-on orders for more than one order operation, the system displays all the follow-on orders that have been created for the selected order or its operations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Display Maintenance Order | Open Display Maintenance Order (W0033).Fill in the created preventive maintenance order number. Or use the Value Help to search for the order. Select this result item to return with the result.Choose Continue. | The Display Preventive Maintenance: xxxxxxx screen appears. |  |
| 3 | Display Document Flow | On the Display Preventive Maintenance: xxxxxxx page, choose You can also -> Display Document Flow (IW12). | The Display Document Flow screen appears. |  |
| 4 | Review the Follow-on Order | Choose Follow-On Orders. | The follow-on order is reviewed. |  |

#### Review Asset Maintenance Object Pages

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the different objects pages available for different roles in Enterprise Asset Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner.Note You can use any of the maintenance roles from the sections above. | The SAP Fiori launchpad displays. |  |
| 2 | Start Search | Choose Search in the upper right area of the launchpad. |  |  |
| 3 | Set Search Criteria | In the dropdown list, choose Equipment, for example:233100091. |  |  |
| 4 | Tailor the Result Display | Below the search line, choose a symbol (for example, filter, display as table, sort, and so on) to filter the results list. | The result list is filtered according to your selection. |  |
| 5 | Review Object Page | Review overview information for the equipment via the Object Page. |  |  |
| 6 | Repeat Steps | Repeat steps 1 to 5 for any other role in this test script and any other object offered in the search function.For example:NotificationOrderOrder Confirmation |  |  |

## Appendix

### Maintenance Planning Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Maintenance Planning Overview (F2828) provides a role-based and personalized entry page for maintenance planners to monitor the progress of various maintenance activities that impact asset availability and reliability. It also provides maintenance planners with clear overview of the current situations in their area of responsibility and enables quick actions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Maintenance Planning Overview | Open Maintenance Planning Overview (F2828). | The Maintenance Planning Overview screen displays. |  |
| 3 | Search for Notifications and Orders | Set Reference Period or Reference Date on the upper part of the screen.You can display outstanding notifications by choosing Priority, Activity or Notification Type in the Notifications for Screening card.You can also check Missing Components, Overdue Orders, Orders for Completion, Orders for Planning, Purchase Requisitions and so on in other cards.You can find relevant applications on the Quick Links card on the lower left corner of the screen. | The notifications filtered by different criterias will be shown as bar chart in Notifications for screening card. You can choose different segments of the bar to see more details. |  |

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before starting with the test steps:

| Process | Business Condition |
| --- | --- |
| MDS: Create New Open MM Posting Period - MDS (BNZ) | ScopeItem_BusinessCondition |
|  |  |
| Create Measuring Point master data script (5MI) | Measuring point creation |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Period-End Closing – Maintenance Orders (BF7) | A maintenance order has been technically completed. |

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
- related-to :: [[14-maintenance-service-and-projects/test-script-proactive-maintenance-4hi-ae-sap-s-4hana-cloud-public-edit]]
- related-to :: [[14-maintenance-service-and-projects/test-script-recurring-services-4x5-ae-sap-s-4hana-cloud-public-edition]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJ2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 112,773 chars in the whole document
