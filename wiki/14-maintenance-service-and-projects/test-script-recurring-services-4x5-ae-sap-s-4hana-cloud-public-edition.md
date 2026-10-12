---
id: 14-maintenance-service-and-projects/test-script-recurring-services-4x5-ae-sap-s-4hana-cloud-public-edition
title: "Test Script: Recurring Services (4X5_AE) - SAP S/4HANA Cloud Public Edition (4X5_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 4X5 Recurring Services (AE), S/4HANA Cloud 2608: maintenance plans, scheduling, mass scheduling, logs, counter readings."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/preventive-and-proactive-maintenance]
aliases: [4X5_S4CLD2608_BPD_EN_AE]
keywords: [Preventive and Proactive Maintenance Plans, recurring services, maintenance plans, time-based maintenance plan, performance-based maintenance plan, multiple counter plan, maintenance plan scheduling, mass scheduling, mass scheduling logs, counter readings]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X5_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1055
topic: 14-maintenance-service-and-projects/preventive-and-proactive-maintenance
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Recurring Services (4X5_AE) - SAP S/4HANA Cloud Public Edition (4X5_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X5_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Preventive and Proactive Maintenance Plans** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Recurring Services (4X5_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232855082)

[2 Prerequisites 4](#_Toc232855083)

[2.1 System Access 4](#_Toc232855084)

[2.2 Roles 4](#_Toc232855085)

[2.3 Master Data, Organizational Data, and Transactional Data 5](#_Toc232855086)

[2.4 Business Conditions 6](#_Toc232855087)

[2.5 Preliminary Steps 6](#_Toc232855088)

[2.5.1 Create Counters (Optional) 6](#_Toc232855089)

[2.5.2 Create Measurement Documents (Optional) 7](#_Toc232855090)

[2.5.3 Specify Transaction Types for Contract Determination 8](#_Toc232855091)

[2.5.4 Settings for Situation Handling (Optional) 10](#_Toc232855092)

[3 Overview Table 11](#_Toc232855093)

[4 Test Procedures 12](#_Toc232855094)

[4.1 Create Service Contract 12](#_Toc232855095)

[4.2 Create Service Order Template 12](#_Toc232855096)

[4.3 Create Maintenance Plan 12](#_Toc232855097)

[4.3.1 Time-Based Single Cycle Plan 12](#_Toc232855098)

[4.3.2 Performance-Based Single Cycle Plan 15](#_Toc232855099)

[4.3.3 Multiple Counter Plan 18](#_Toc232855100)

[4.4 Schedule Maintenance Plan (Optional) 20](#_Toc232855101)

[4.5 Mass Schedule Maintenance Plans (Optional) 21](#_Toc232855102)

[4.6 Monitor Mass Scheduling Logs (Optional) 22](#_Toc232855103)

[4.7 Update Counter Reading for the Technical Objects (Optional) 23](#_Toc232855104)

[5 Appendix 25](#_Toc232855105)

[5.1 Process Integration 25](#_Toc232855106)

[5.1.1 Preceding Processes 25](#_Toc232855107)

[5.1.2 Succeeding Processes 25](#_Toc232855108)

## Purpose

Overview

This scope item covers the creation of maintenance plans in SAP S/4HANA Cloud Public Edition, as well as scheduling and service order creation. Maintenance plans can be set up to release the service order automatically when you create the service order or let the user release the order manually afterwards. Service order items are copied from the service order templates that are assigned to maintenance items in the maintenance plan. A released Service contract item (Scope item 3MO) and Service order template (Scope item 3D2) is the prerequisite for this scope item.

The Service Order Management (3D2) scope item is the follow-on process to further process the service order such as planning, releasing, time and material confirmation, billing, and order completion.

The completion date is updated automatically in the maintenance plan either upon completion of service order or manually by the user. Updating the measuring counter reading is an optional step during confirmation.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

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
| Service Planner - Recurring Service | SAP_BR_SERVICE_PLANNER | Recurring Service | SAP_BR_SERVICE_PLANNER |  |
| Master Data Specialist - Maintenance Management | SAP_BR_MD_SPECIALIST_EAM | Master Data - Maintenance Management | SAP_EAM_SPT_MD_SPECIALIST_PC |  |
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC |  |
| Service Technician - Customer Service | SAP_BR_CUSTOMER_SRVC_TEC | Service Processing | SAP_BR_CUSTOMER_SRVC_TEC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Transactional Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Customer | 33100001 | Domestic UAE Customer 1 |  |
| Employee | - | < Use your own employee ID that is assigned to your user ID.> |  |
| Material | SRV_CONTRACT | Service Contract Product |  |
| Material | SRV_01 | Service | A service is usually performed by an internal employee. Alternatively, it can be procured from a third party (external workforce procurement). In that case, the scope item 3NI is required. |
| Material | SRV_02 | Service Expenses |  |
| Material | SRV_04 | Service Part (Defined) |  |
| Material | SRV_05 | Stock Service Part |  |
| Equipment | 217100901 | Printer Professional IHR1911 Printer |  |
| Equipment | 217100902 | Printer Professional IHR1911 Printer |  |
| Company Code | 3310 | Company Code 3310 |  |
| Sales Organization | 3310 | ( Dom. Sales Org AE) |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 3KV | Create Service Product for Service Processes - MDS |
| 3U3 | Create Plant Maintenance Master Data for Service - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3MO - Service Contract Management | A service contract is created with Released status from 3MO Service Contract Management. |
| 3D2 - Service Order Management and Monitoring | A service template is created with Released status from 3D2 Service Order Management and Monitoring. |

### Preliminary Steps

#### Create Counters (Optional)

Use

Counters represent the wear and tear of an object, consumption, or the reduction of an object’s useful life. In this procedure, you can create counters for performance-based single cycle plan or multiple counter plans.

To create a counter, make sure business catalog SAP_EAM_BC_MESP_MNG_PC is included in your business role assigned to your user.

Procedure

Table 2: Create Odometer Range Counter

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Maintenance Management | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Choose the Master Data Specialist - Maintenance Management tab.Under the Technical Objects, open Create Measuring Point. |  |  |
| 3 | Create Measuring Point | Make following entries:MeasPointObject: IEQ EquipmentEquipment: for example, 217100901MeasPtCategory: M MeasPoint (general)MeasPoint is counter: SelectedPress Enter. | The view Create Measuring Point (Counter) is displayed. |  |
| 4 | Maintain the Details | In the General Data section, make following entries:Description: <Any meaningful description>Characteristic: OPERATING_HOURIn the Counter Data section, make following entries:CntrOverReadg：10000AnnualEstimate: 3000Then choose Save. | Measuring Point is created. |  |

#### Create Measurement Documents (Optional)

Use

The measurement document is the result of a measurement or counter reading being entered in the system. In this procedure, you can create measure documents for counter.

To create a measurement document, make sure business catalog SAP_EAM_BC_MEADOC_MC is included in your business role assigned to your user.

Procedure

Table 3: Create Measuring Document for Odometer Range Counter

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Service Planner - Recurring Service. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the APP | Open Create Measurement Document for Technical Object. |  |  |
| 3 | Maintain Parameters | Make following entries:Basis for Measurement Reading: Measuring PointMeasuring Point: : <The one created for OPERTING_HOUR>Then choose Continue. | The view Create Measurement Documents is displayed. |  |
| 4 | Maintain Readings | In the Measurement Readings section, set Reading as 100Then choose Save. | Measurement document is saved. |  |

#### Specify Transaction Types for Contract Determination

When you want to use the service order template SVT2 Fixed Price Service Order (Template) in Maintenance Plans, you first have to specify the corresponding transaction type for fixed price Service Orders SVO2 as relevant for Contract Determination.

Procedure

Depending on your [configuration environment for SAP S/4HANA Cloud Public Edition](https://help.sap.com/docs/SAP_S4HANA_CLOUD/adbae5bcd5994f159bf2847a11397b61/0b3f87579f345c08e10000000a441470.html?version=2202.501), proceed with the steps described in Configuration with Manage Your Solution, or in Configuration with SAP Central Business Configuration.

Configuration with Manage Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Your Solution application | Choose the Manage Your Solution application tile. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Configure Your Solution | Choose Configure Your Solution. | The list report page is displayed in the screen Configure Your Solution: Realize Phase.Configuration Items are displayed in the list. |  |
| 4 | Find configuration item SLA Determination | Select Service in the filter ‘Application Area’And Service Contract Management in the filter ‘Sub Application Area’ and you will see the configuration item Service Contract DeterminationChoose the icon > at the end of this line. | The sub screen Configure Your Solution – Service Contract Determination is displayed. |  |
| 5 | Go to the configuration screen | On step 1 Specify Contract Determination Option for Trans.Types.Choose Configure in the column Actions. | The screen Change View "Specify Contract Determination Option for Trans. Types ": is displayed. |  |
| 6 | Specify transaction types for contract determination | In column Trans. Types select the row with the entry SVO2 Fixed Price Service OrderIn column Contract Determination select Only at Item level if External System Does Not Determine.Choose Save. | Transaction type SVO2 is specified for contract determination |  |

Configuration with SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Find Configuration Item Service Contract Determination | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Specify Contract Determination Option for Trans. Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SSCUI will open on SAP S/4HANA Cloud Public Edition system. |  |
| 3 | Specify transaction types for contract determination | In column Trans. Types select the row with the entry SVO2 Fixed Price Service Order.In column Contract Determination select Only at Item level if External System Does Not Determine.Choose Save. | Transaction type SVO2 is specified for contract determination. |  |

#### Settings for Situation Handling (Optional)

Purpose

Notifications are only created in the system once the required configurations in the situation template (including notification recipient settings) are set up.

This additional configuration step should be carried out by customers to activate situation handling.

Prerequisite

To set up situation handling, create your ready-to-use situation type, maintain the message to be displayed, define the conditions when the situation will be triggered, define recipient groups who will receive notifications, and monitor the instances.

For more information, see the Set-Up Instructions for the scope item Situation Handling (31N).

This document describes the configuration steps for situation handling, which includes the Manage Situation Types app to adapt messages and notification recipients.

The following standard situation templates are defined and delivered by SAP for Recurring Services:

- SRVC_MPLAN_MASS_SCHEDULING_ISSUE (Service Maint. Plan Mass Schedule Issue)

For more information and situation template details (default settings, conditions, notification recipients), see documentation: [Situation templates in Service](https://help.sap.com/viewer/adbae5bcd5994f159bf2847a11397b61/latest/en-US/9d6cee508b2e44a39e93474ee68e6ba9.html)

For each situation template, a corresponding responsibility rule is defined in which the responsible person will receive the situation notification.

## Overview Table

This scope item consists of several steps provided in the table below.

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Service Contract](#unique_12) [page ] 12 | Customer Service Manager | Manage Service Contracts | A service Contract is released without error. |
| [Create Service Order Template](#unique_13) [page ] 12 | Customer Service Manager | Manage Service Order Templates | A service order temple is released without error. |
| Create Maintenance Plan |  |  |  |
| [Time-Based Single Cycle Plan](#unique_14) [page ] 12 | Service Planner - Recurring Service | Create Maintenance Plan | A time-based maintenance plan is created successfully. |
| [Performance-Based Single Cycle Plan](#unique_15) [page ] 15 | Service Planner - Recurring Service | Create Maintenance Plan | A Performance-based maintenance plan is created successfully. |
| [Multiple Counter Plan](#unique_16) [page ] 18 | Service Planner - Recurring Service | Create Maintenance Plan | A multiple counter maintenance plan is created. |
| [Schedule Maintenance Plan (Optional)](#unique_17) [page ] 20 | Service Planner - Recurring Service | Schedule Maintenance Plan | Service order generation of the available calls are triggered once based on the current date. |
| [Mass Schedule Maintenance Plans (Optional)](#unique_18) [page ] 21 | Service Planner - Recurring Service | Mass Schedule Maintenance Plan | A background job is created and service order generation of the available calls will be triggered consequently. |
| [Monitor Mass Scheduling Logs (Optional)](#unique_19) [page ] 22 | Service Planner - Recurring Service | Monitor Mass Scheduling Logs-Service | Log details are displayed. |
| [Update Counter Reading for the Technical Objects (Optional)](#unique_20) [page ] 23 | Service Technician - Customer Service | Create Measurement Document for Technical Object | Counter Reading is updated. |

## Test Procedures

This section describes the test procedures for each process step that belongs to this scope item.

### Create Service Contract

The Customer Service Manager creates and releases service contracts in the SAP Fiori app Manage Service Contracts

- To create a service contract and release it, refer to the chapter Create Service Contract in scope item 3MO Service Contract Management

### Create Service Order Template

The Customer Service Manager creates and releases service order templates in the SAP Fiori app Manage Service Order Templates.

- To create a service order template and release it, refer to the chapters Create Service Order Template and Release Service Order Template in scope item 3D2 Service Order Management and Monitoring.

### Create Maintenance Plan

#### Time-Based Single Cycle Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can create a time-based single cycle maintenance plan.

For the details of scheduling parameters in maintenance plans, refer to the following documentation: [https://help.sap.com/s4hana_cloud](https://help.sap.com/viewer/product/SAP_S4HANA_CLOUD/2208.500/en-US?task=discover_task) >Product Assistance > Service > Recurring Service > Creation of Maintenance Plans > Scheduling Parameters.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Service Planner - Recurring Service. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Maintenance Plan. | The view Create Maintenance Plan is displayed. |  |
| 3 | Maintain Maintenance Plan Parameters | Make the following entries:Maintenance Plan For: Service Order SOMaintenance Plan Type: Single Cycle (Time Based)Choose Continue. | The view Create Maintenance Plan: Single-Cycle Plan is displayed.The default view is Items. |  |
| 4 | Maintain Maintenance Plan Item Data | On the Items tab, make the following entries for the first item:Item Description: for example, Recurring ServiceTechnical Object: 217100901Service Contract: choose any service contract item you have created with search helpService Template: choose any service order template you have created with search helpService Call Object: Service OrderOn the lower screen, choose General Data tab. Make the following entries:Service Priority: MediumLong Text: <any comment>On the General Data tab, Object List section, choose the equipment, then choose OK if any pop-up is displayed. If there is no pop-up window for equipment, specify 217100901 as Technical Object in Object List.Note If the object list has been specified in the service contract item that you have specified, you are prompted to select technical objects upon the first time you fill in the object list for the maintenance plan. | The Maintenance Plan Planning Data view is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | On the Planning Data tab, in Date Determination section, make the following entries:Start Date for Scheduling: <Current date>End Date for Scheduling: < Current date+ 1 Year>Note When you specify the start date for scheduling and end date for scheduling, ensure that this period is within the start date and end date of the specified service contract item with the release status.Also ensure that this period is within the start date and end date of the specified service order template. If the end date for scheduling is not specified, the maintenance plan can be repeatedly scheduled. It is recommended that you specify the start date for scheduling. If you do not specify the start date for scheduling, the maintenance plan cannot be scheduled through mass scheduling.Shift Factor for Early Completion: 100Shift Factor for Late Completion: 100Note The shift factor in the event of early/late completion defines the percentage of the shift to be applied to the calculation of the next due date.Tolerance (+): 10Tolerance (-): 10Note The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cyclesCycle Modification Factor: 1In the Call Control section, make the following entries:Scheduling Period: 365 DAYNote You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.Call Horizon: 0 %Note The call horizon determines when a maintenance call object, for example, a service order should be generated for a maintenance call.Completion Required: XNote If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.In the Cycle section, make the following entries:Cycle / Unit: 1 MONNote Cycle /unit defines the duration in which the maintenance is to be executed.Cycle Description: Monthly |  |  |
| 6 | Save Maintenance Plan | Choose Save. | The Maintenance Plan is created. |  |

#### Performance-Based Single Cycle Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can create a performance based single cycle plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as Service Planner - Recurring Service. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Maintenance Plan. | The view Create Maintenance Plan is displayed. |  |
| 3 | Maintain Maintenance Plan Parameters | Make the following entries:Maintenance Plan For: Service Order SOMaintenance Plan Type: Single Cycle (Performance-Based)Choose Continue. | The view Create Maintenance Plan: Single-Cycle Plan is displayed.The default view is Items. |  |
| 4 | Maintain Maintenance Plan Item Data | On the Items tab, make the following entries for the first item:Item Description: For example, Recurring ServiceTechnical Object : 217100901Service Contract: choose any service contract item you have created with search helpService Template: choose any service order template you have created with search helpService Call Object: Service OrderOn the lower screen, choose General Data tab. Make the following entries:Service Priority: MediumLong Text: <any comment>On the General Data tab,in the Object List section, choose the equipment, then choose OK if any pop-up displays. If there is no pop-up window for equipment, specify 217100901 as Technical Object in Object List.Note If the object list has been specified in the service contract item that you have specified, you are prompted to select technical objects upon the first time you fill in the object list for the maintenance plan. | The Maintenance Plans Planning Data view is displayed. |  |
| 5 | Maintain Maintenance Plan Planning Data | On the Planning Data tab, in the Date Determination section, make the following entries:Start Counter Reading: 1End Counter for Scheduling: 10000End Date for Scheduling: < Current date+ 1 Year>Shift Factor for Early Completion: 100Shift Factor for Late Completion: 100Note The shift factor in the event of early/late completion defines the percentage of the shift to be applied to the calculation of the next due date.Tolerance (+): 10Tolerance (-): 10Note The tolerance, in the case of early/late completion, determines the time span in which variances between actual and planned dates do not influence subsequent scheduling. The tolerance is defined as a percentage rate of the smallest interval between the maintenance cyclesCycle Modification Factor: 1In the Call Control section, make the following entries:Scheduling Period: 365 DAYNote You can use the scheduling period to determine the length of time for which the system creates maintenance calls during maintenance plan scheduling.Call Horizon: 0 %Note The call horizon determines when a maintenance call object, for example, a service order should be generated for a maintenance call.Completion Required: XNote If you set this indicator, the system only generates the next call object once the preceding call object has been confirmed.In the Cycle section, make the following entries:Cycle / Unit: 100 HNote Cycle /unit defines the duration in which the maintenance is to be executed.Cycle Description: Per 100 HCounter: The one created in preliminary steps for OPERATING_HOUR |  |  |
| 6 | Save Maintenance Plan | Choose Save. | The Maintenance Plan is created. |  |

#### Multiple Counter Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can create a multiple counter plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as Service Planner - Recurring Service. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Maintenance Plan. | The view Create Maintenance Plan is displayed. |  |
| 3 | Maintain Maintenance Plan Parameters | Make the following entries:Maintenance Plan For: Service Order SOMaintenance Plan Type: Multiple CounterChoose Continue. | The view Create Maintenance Plan: 'Multiple-Counter Plan is displayed.The default view is Items. |  |
| 4 | Maintain Maintenance Plan | On the Planning Data tab, make following entries,Long Text: <Any meaningful comment>Description: <Any meaningful title>In the Data Determination section under Planning Data tab, make following entries:Start Date: <Today>End Date for Scheduling: <Today+1 Year>Lead Float: 7In the Call Control section under Planning Data tab, make following entries:Scheduling Period: 365 DAYCompletion Required: XOperation Type: X OR OperationIn the first line item, please make following entriesCycle set Sequence: 1Cycle: 24Unit: HDescription of Cycle: <Any description >Counter: <The one created in preliminary steps for OPERATING_HOUR>In the second line item, please make following entries:Cycle set Sequence: 2Cycle: 48Unit: HDescription of Cycle: <Any description >Counter: <The one created in preliminary steps for OPERATIBG_HOUR>Choose Items tab, make the following entries for the first item:Item Description: for example, Multiple Counter for Recurring ServiceTechnical Object: 217100901Service Contract: choose any service contract item you have created using the search helpService Template: choose any service order template you have created using the search helpService Call Object: Service OrderCycle Set Sequence: Cycle Set Sequence 2For the second item, make the following entries:Item Description: for example, Multiple Counter for Recurring ServiceTechnical Object: 217100901Service Contract: choose any service contract item you have created using the search helpService Order Template: choose any service order template you have created using the search helpService Order Type: Service OrderCycle Set Sequence: Cycle Set Sequence 2On the lower screen, choose General Data tab. Make the following entries:Service Priority: MediumLong Text: <any comment >On the General Data tab,in the Object List section, choose the equipment, then choose OK if any pop-up displays. If there is no pop-up window for equipment, please specify 217100901 as Technical Object in Object List.Note If the object list has been specified in the service contract item that you have specified, you are prompted to select technical objects upon the first time you fill in the object list for the maintenance plan. | The Maintenance Plans Planning Data view is displayed. |  |
| 5 | Save Maintenance Plan | Choose Save. | The Maintenance Plan is created. |  |

### Schedule Maintenance Plan (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can schedule a maintenance plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as Service Planner - Recurring Service. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Schedule Maintenance Plan - Service. | The view Schedule Maintenance Plan is displayed. |  |
| 3 | Input Maintenance Plan | Enter the previous maintain plan, then choose Execute. |  |  |
| 4 | Option A: Schedule Maintenance Plan | Choose Start, In the following pop-up window, specify Start of cycle as Today, then choose Continue. |  |  |
| 5 | Option B: Schedule Maintenance Plan | Choose Manual call, specify Manual call as Today, then choose Continue. | Note Manual calls are not supported for multiple counter maintenance plans. |  |
| 6 | Save your data | Choose Save. | Service order generation of the available calls are triggered.Note Once service order is completed, then completion date will be updated in the maintenance plan. |  |

### Mass Schedule Maintenance Plans (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you can mass schedule maintenance plans.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Service Planner - Recurring Service. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Mass Schedule Maintenance Plans - Service. | The view Application Jobs are displayed. |  |
| 3 | Create Job | Choose Create. | The view New Job: Mass Schedule Maintenance Plans - Service is displayed. |  |
| 4 | Check Template Selection | The default Job Template is Mass Schedule Maintenance Plans for Service.The default Job Name is Mass Schedule Maintenance Plans for Service.Give a meaningful name for Job Name, then choose Step 2. | The details of Scheduling Options are displayed. |  |
| 5 | Check Scheduling Options | Check or specify Scheduling Options, then choose Step 3. | The details of parameters are displayed. |  |
| 6 | Schedule Parameters | Make following entries:Call Object Horizon (Days): 1Number of Parallel Processes: 10Service Group for parallel Proc.: parallel_generatorsIn the Technical Objects section, specify Equipment as 217100901.Then choose Schedule. | Job is scheduled successfully.Once the service order is completed, the completion date will be updated in the maintenance plan. |  |

### Monitor Mass Scheduling Logs (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to monitor mass scheduling logs

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Service Planner - Recurring Service. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Monitor Mass Scheduling Logs-Service. | A list of application logs is displayed. |  |
| 3 | Navigate to Log Details | Choose any entry, in order to navigate to the Log details. | The Log Details are displayed. |  |
| 4 | Check Log Details | Choose one entry or multiple entries against Severity, choose Go.Note It is supported to specify description of log detail or maintenance plan ID in the search box at the right side of Log Details section. | The Log Details list is displayed. |  |

### Update Counter Reading for the Technical Objects (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to update counter reading for the technical object.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Service Technician - Customer Service. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Measurement Document for Technical Object. | The view Create Measurement Documents is displayed. |  |
| 3 | Maintain Parameters | Make the following entries:Basis for Measurement Reading: Reference ObjectReference Object Type: Technical ObjectTechnical Object: 217100901 |  |  |
| 4 | Maintain Readings | In the Measurement Readings section,Set Reading respectively for each counter, then choose Save. | Measurement document is saved. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

The following processes and conditions can proceed this process.

| Process | Business Condition |
| --- | --- |
| 3D2 - Service Order Management and Monitoring | A service template is created with Released status from 3D2 Service Order Management and Monitoring |
| 3MO - Service Contract Management | A service Contract is created with Released status from 3MO Service Contract Management |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3D2 - Service Order Management and Monitoring | The service order triggered from maintenance plan can be processed further in 3D2 Service Order Management and Monitoring. |

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
- related-to :: [[14-maintenance-service-and-projects/test-script-preventive-maintenance-bj2-ae-sap-s-4hana-cloud-public-edi]]
- related-to :: [[14-maintenance-service-and-projects/test-script-proactive-maintenance-4hi-ae-sap-s-4hana-cloud-public-edit]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4X5_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 39,775 chars in the whole document
