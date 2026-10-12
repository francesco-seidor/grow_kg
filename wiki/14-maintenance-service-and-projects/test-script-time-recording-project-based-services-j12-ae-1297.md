---
id: 14-maintenance-service-and-projects/test-script-time-recording-project-based-services-j12-ae-1297
title: "Test Script: Time Recording – Project-Based Services (J12_AE) (J12_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 (AE) test script for J12: timesheet entry, contingent worker time, approval, missing time, team utilization, closed periods."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/time-recording, topic/customer-project-management]
aliases: [J12_S4CLD2608_BPD_EN_AE]
keywords: [Time Recording, manage my timesheet, manage timesheet app, contingent worker time recording, unstaffed project tasks, timesheet approval, missing time notification, team utilization, closed period time confirmation, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J12_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1297
topic: 14-maintenance-service-and-projects/time-recording
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Time Recording – Project-Based Services (J12_AE) (J12_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J12_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Time Recording** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Time Recording – Project-Based Services (J12_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232862692)

[2 Prerequisites 4](#_Toc232862693)

[2.1 System Access 4](#_Toc232862694)

[2.2 Roles 4](#_Toc232862695)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232862696)

[2.4 Business Conditions 6](#_Toc232862697)

[3 Overview Table 8](#_Toc232862698)

[4 Test Procedures 9](#_Toc232862699)

[4.1 Time Recording 9](#_Toc232862700)

[4.1.1 Time Recording through Manage My Timesheet 9](#_Toc232862701)

[4.1.2 Time Recording through new Manage Timesheet App (Optional) 14](#_Toc232862702)

[4.2 Time Recording for Contingent Worker 20](#_Toc232862703)

[4.2.1 Optional: Create Task through Manage My Timesheet 20](#_Toc232862704)

[4.2.2 Time Recording through Manage My Timesheet 22](#_Toc232862705)

[4.3 Approval or Rejection of Working Times 26](#_Toc232862706)

[4.3.1 Working Times with App My Inbox 26](#_Toc232862707)

[4.4 Notify Missing Time 28](#_Toc232862708)

[4.5 Analyze Team Utilization 30](#_Toc232862709)

[5 Appendix 32](#_Toc232862710)

[5.1 Process Chains 32](#_Toc232862711)

[5.1.1 Succeeding Processes 32](#_Toc232862712)

[5.1.2 Preceding Processes 32](#_Toc232862713)

[5.1.3 Time Confirmation in Closed Periods 32](#_Toc232862714)

## Purpose

Overview

The Time Recording for Project Services scenario provides employees a quick entry method for recording time against customer or internal projects. In the time entry sheet, all work packages or work items assigned to the employee are visible. Nonbillable times can also be entered for full time accountability. Time recording on behalf of the employee and approval of time sheet entries is possible.

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT | Suggested sample user OVERHEAD_ACCOUNTANT representing the business role Cost Accountant - Overhead. |
| Employee | SAP_BR_EMPLOYEE | Self Services / Self Services / Employee Overview Space | SAP_BR_EMPLOYEE / SAP_CA_SPT_EMPLOYEE_CROSS_PC / SAP_EAM_SPT_EMPLOYEE_PC | Suggested sample user EMPLOYEE representing the business role Employee. |
| Project Manager - Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Project Management – Professional Services | SAP_BR_PROJECT_MANAGER_PROF | Suggested sample user PROJECT_MANAGER_PROF representing the business role Project Manager – Professional Services. |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC | Suggested sample user ADMINISTRATOR representing the business role Administrator. |
| Manager - HR Info | SAP_BR_MANAGER_HRINFO |  |  | Suggested sample user MANAGER_HRINFO representing the business role Manager - HR Info. |

|  |
| --- |
| Note The role template Project Manager - Commercial Services and generic role SAP_BR_PROJ_MANAGE_COMM are deprecated from CE2202 and are respectively replaced by the role template Project Manager - Professional Services and generic role SAP_BR_PROJECT_MANAGER_PROF. For customers installing the system before CE2202, you can still use the role template Project Manager - Commercial Services for your existing projects. However, we recommend that you to use the role template Project Manager - Professional Services for creating new projects. For more details, please refer to [https://launchpad.support.sap.com/#/notes/3121435](https://me.sap.com/notes/https:/launchpad.support.sap.com/#/notes/3121435). |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Service Organization | Service Organization – Company AE | The following Enterprise Structures are assigned to the Service Organization:Controlling Area A000Company Code 3310Cost Center 33101902Cost Center 33101903Cost Center 33101904Plant 3310Distribution Channel 10Division 00Sales Organization 3310 |  |
| Cost Center | Csltg Unit ACsltg Unit BCustomer Dev | 331019023310190333101904 | The standard configuration design is as follows:All the consultants who want to record time on real projects are belong to consulting cost centers with Category=C.Cost Center of type "W" is for admin cost center and colleagues assigned to admin cost center are not allowed to book as role such as senior consultant , junior consultant and so on.If customer wants to allow people belonging to W cost center also to record time on project, please use the Manage Activity Types (F1605A) app as a Cost Accountant - Overhead to change the activity type and make allowed category from C to *. |
| Customer | Domestic UAE Customer 1 | 33100001 |  |
| Cost Rates | Actual and planned cost rates are maintained for the following combination of cost centers / activity types:Cost centers: 331019023310190333101904Activity types: T001 - T006 | Please refer to Check and Maintain Cost Rates the J11 preliminary steps . | This is to ensure employee/contingent worker assigned to projects has a cost rate. By multiplying the time recorded for the project, you can collect relevant cost, for example, consulting costs for the project. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BND | Create Customer Master - MDS |
| 3KW | Create CO Cost Rates - MDS |

### Business Conditions

Before testing this scope item, you must meet either of following business conditions.

| Scope Item | Business Condition |
| --- | --- |
| J11 - Customer Project Management – Project-Based Services | Must be run before this test script. A project must be created and the employee must be assigned to a project. |
| 1A8 - Internal Project Management – Project-Based Services | Must be run before this test script. A project must be created and the employee must be assigned to a project. |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| Time Recording |  |  |  |
| [Time Recording through Manage My Timesheet](#unique_8) [page ] 9 | Internal Worker | Manage My Timesheet (F1823) / Manage Timesheet (F1823A) | Time is recorded for a project or work package or work item. |
| [Time Recording through Manage My Timesheet](#unique_8) [page ] 9 | Contingent Worker | Manage My Timesheet (F1823) | Time is recorded for a project or work package or work item. |
| Time Recording for Contingent Worker |  |  |  |
| [Optional: Create Task through Manage My Timesheet](#unique_9) [page ] 20 | Contingent Worker | Manage My Timesheet (F1823) |  |
| [Time Recording through Manage My Timesheet](#unique_10) [page ] 22 | Contingent Worker | Manage My Timesheet (F1823) |  |
| [Approval or Rejection of Working Times](#unique_11) [page ] 26 | Project Manager - Professional Services | Manage Your Solution (F1241) | Personalized email address can be prepared. |
| [Working Times with App My Inbox](#unique_12) [page ] 26 | Project Manager - Professional Services | My Inbox (F0862) |  |
| [Notify Missing Time](#unique_13) [page ] 28 | Project Manager - Professional Services | Notify Missing Times (F2556) | Identify missing time recording and send reminders to relevant consultants. Project Manager wants to know the missing time recording for his projects and send reminders to people who have missing time. |
| [Analyze Team Utilization](#unique_14) [page ] 30 | Manager - HR Info (a.k.a Line Manager) | Team Utilization (F2582) | Understand team resources and staffing situation. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

In SAP S/4HANA Cloud Public Edition, Core Data Services (CDS) are introduced in any consuming stack variant. To access CDS Views for Professional Services, you may follow the link: [https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD) to visit Product Assistance. Click English and navigate by: SAP S/4HANA Cloud Public Edition - Generic Information - Analytics - CDS View - CDS Views for Professional Services.

To access CDS Views for Human Resources, you may follow the link: [https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD) to visit the Product Assistance. Click English and navigate by: Generic Information - Analytics - CDS View - CDS Views for Human Resources

SAP S/4HANA Cloud Public Edition provides Self-Service Configuration User Interface (SSCUI) to allow key users (BPC_EXPERT) to adapt a pre-configured SAP Best Practices process. The App is called Configure Your Solution, which is part of Manage Your Solution app. Key users may refer to on-line help for each SSCUI.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options to proceed:

- Manage Your Solution:

In the SAP S/4HANA Cloud Public Edition system, in the SAP Fiori launchpad, open the Manage Your Solution app and go to View Solution Scope.

- SAP Central Business Configuration:

In the Scope and Organizational Structure phase, navigate to the Activities tab. Search for Define Scope and choose Open.

### Time Recording

#### Time Recording through Manage My Timesheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform the time recording process through the Manage My Timesheet (F1823) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On and Access My Timesheet | Option 1: Log on to the SAP Fiori launchpad with the user for whom timesheet is to be recorded, and then open Manage My Timesheet (F1823).In case users can't record time for themselves, line manager and project manager can record timesheet on behalf.Option 2: Timesheet on behalf by line manager.Log on to SAP Fiori launchpad as a line manager and open Team Utilization. Select the user for whom timesheet is to be recorded and choose Edit Timesheet.Option 3: Timesheet on behalf by project manager.Log on to SAP Fiori launchpad as a project manager and open Notify Missing Times (F2556). Select the user for whom timesheet is to be recorded and choose Edit Timesheet. | The My Timesheet screen displays.Note Timesheet on behalf can also be done by project controller. They can be specified as a project role during the process of J11/1A8 Project Management.Note Field extensibility is enabled. you may transfer additional customer field like jira ticket. |  |
| 2 | Select Date Range | By default, the timesheet shows the current week.If you want to record times in a different week, select the date range line on the top of the screen under My Timesheet. | A calendar entry dialog box displays allowing you to choose the week you wish to display.The Calendar Settings allows you to set Show Work Week (if no, Saturday and Sunday are shown), Start Week From (for example, Monday), and Time Format (12:30 or 12.5).There are also Minimum Time Slot and Intervals for Time Recording (in Minutes) two items . If you are in custom settings (choose Custom Settings), you can change Intervals for Time Recording (in Minutes) in calendar settings. If you are in default settings, you will use the values defined in SSCUI.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |  |
| 3 | Explore Your Tasks |  | The tasks (labeled by combination of: customer name, work packages, activity type, work items) assigned to you are displayed on the right side of the screen under My Tasks with the description of the projects, work packages, activity type, and work items. By selecting Group Tasks icon which is in the right middle of My Tasks, you can group the tasks by accounting objects like cost center, WBS elements and so on, and customer projects: billable or non-billable.They are automatically prefilled in the My Tasks list if the employee is staffed to a work package of commercial projects. The automatically created tasks cannot be deleted.On the top-right corner of each task, you would see the hours already recorded for that task.Non-project related task types, which are non-billable, are automatically prefilled in the My Tasks list for internal employees.To employee (also applies to contingent workers) who has multiple employments, the tasks within his active employment will be shown. In case there are multiple active employments for user cases like country/region transfer or global assignment, you can find Employment link on upper left of screen. By choosing the employment link, Select Employment, the pop up screen comes out for you to select the right employment for time recording.Note Specify Task Types, Components, and Levels, the self service configuration UI, can be used to define these non-project related task types. |  |
| 4 | Search Your Tasks (optional) | On the right side of the screen, insert a text in the search box just below My Tasks.The text search can be performed through three attributes: project title description, work package title description/work item title description, role description | The tasks assigned to you are filtered according to the text inserted in the search box. |  |
| 5 | Select a Task | On the right side of the screen, under My Tasks, the tasks assigned to you are shown.By default, the five most recently used tasks are shown. choose a task. | You have selected a task on which you can record times. The selected task is shown in a different color. |  |
| 6 | Record Working time - Create New Time Entry | Choose a task from the list of the available tasks. To enter the working times, click on the number of hours you want to record. A rectangular area just below the date range, shows all the days of the chosen week on the top horizontal axis, the working hours for each day on the left vertical axis, and the total hours recorded per day in the bottom horizontal axis. The left vertical axis is labeled with a number that helps you in understanding how many hours to record.The minimum time slot is by default 30 minutes, which means if you maintain an entry less than 30 minutes, system will initially provide a time block of 30 minutes. For entries less than 15 minutes, there is no task label or description in the time block. If there are multiple entries that are less than 15 minutes, they will be grouped together. By clicking the time block, you will get an entry list, each entry with a task label and description. You can choose an entry for editing.To create a new time entry, click on the cell corresponding to the day and the number of hours that you want to record. For example, if you want to record 5 hours, click on the cell just below the number 5 on the day on which you want to record the hours.Interval for Time Recording is by default 30 minutes. You can change Interval for Time Recording (in Minutes) in calendar setting. For example, if the time interval is set to 5 minutes, when mouse across calendar, time will jump from, for example, 2:55 h to 3:00 h. | The new time entry is visualized on the day you have chosen as a rectangular box. The height of this box fits the number of hours you have inserted. The entry shows the task title descriptions and the number of hours recorded in the hh:mm format. The system calculates total hours automatically per day and can be viewed on the bottom bar per day and on the bottom left corner as total per week. |  |
| 7 | Record Working time – Create Additional Time Entries | Repeat steps 5 and 6 for any additional time entry you want to record taking into account the already existing entries. For example, if 2 hours are already registered on a day, and you want to record 5 hours, click on the cell just below the number 7 on the day on which you want to record the hours. If you want to record additional time entries on a day on which you have already recorded, all the times allowed on the grid, just click on the top row and the grid will enlarge. | The new time entries are visualized on the days you have chosen as rectangular boxes. The height of each box fits the number of hours you have inserted. Each entry shows the task title descriptions and the number of hours recorded in the hh:mm format. The left vertical axis shrinks up showing more hours if the total hours on a day exceeds the hours currently visualized. A vertical scroll bar appears on the right side of the screen, so that you can scroll up and down for a better visualization. If recording a time entry on a day the total would exceed 24 hours, the system prompts an error message and prevents you from recording that time entry. The system calculates total hours automatically per day and can be viewed on the bottom bar per day and on the bottom left corner as total per week. |  |
| 8 | Record Working Time – Modify Existing Entries | Choose an existing entry, and in the details dialog box, adapt the Duration field by inserting the number of hours in the hh:mm format.If you want to create an entry which is less than 30 minutes, such as 4 minutes, you need to change Minimum Time Slot to less than 4 minutes by SSCUI. Then you can adapt the Duration to 4 minutes.Save your entry.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | The time entry is adapted. The height of the time entry is adapted according to the new recorded hours.If the entry you adapted had been approved before, by choosing the adapted entry, in the Sent for Approval dialog box, you can get information like previous approved duration by clicking icon Last Approved Entry. If you want to modify a previously rejected entry, you have maintained a note before submitting for approval. |  |
| 9 | Record Working Time – Delete Existing Entries | Choose Delete that is on the cross icon on the top right corner of an entry. Choose Save & Submit, a Zero Hour Entries icon appears on the time axis. | The selected entry disappears.Note In case the time entry was approved by manager and then deleted, a Zero Hour Entries icon is displayed on the time axis. |  |
| 10 | Enter a Work Location and/or Note for an Activity (optional) | To enter an optional work location and/or note for an activity, just choose the entry and open a dialogue box. In Work Location field, choose F4 to select a proper Work Location. These work locations are maintained in SSCUI Maintain Work Locations. To enable the Work Location field in the Manage My Timesheet (F1823) app, you need to select Work Location in SSCUI Maintain Data Entry Profile. Enter a description up to 300 characters in the Note field and choose Save.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | The details of the activity are saved. The long text note can be transferred to the My Inbox (F0862) app so that approver can get the information. Project manager can edit the long text during the billing preparation in the Manage Project Billing (F4374) application. The updated long text is displayed on the invoice to the customers. |  |
| 11 | Record Time | Save your entries. | The times are saved.There is a UI adaptation for lower right Save & Submit controlled by SSCUI.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.For details please refer to SAP Product Assistance: [https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD): choose a specific language version of product assistance and navigate by: Configuration Apps > Configuration Apps for Professional Services .If you changed the configuration to Approval Required, in Manage My Timesheet (F1823) app, after choosing Save & Submit, the left side of the time-block turns yellow, indicating it is waiting for approval. If a previously approved or rejected time entry has been modified, you can see Previous Duration to show how many hours have been previously approved or rejected for this time entry.Note BADI (HCM_CATS_V1_B_TS_VALIDATION) provides checks before saving timesheet entries.Please only be aware that you need to select Business Context =HCM: TimeSheet Entry Validation. |  |
| 12 | Overtime Time Recording | To enter Overtime Category for an activity, choose the entry and open a dialogue box. In the Overtime Category field, choose F4 to select a proper overtime category and choose Save. Overtime categories are maintained in SSCUI Maintain Overtime Categories. To enable Overtime Category field in the Manage My Timesheet (F1823) app, you need to select overtime in Maintain Data Entry Profile SSCUI.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | The details of the activity are saved. |  |
| 13 | Create an Unstaffed Project Task | At the right top, choose the  icon in the right side of My Tasks, then open the list item Manage My Tasks. In the lower right hand corner, choose Create Task and Unstaffed Project. In the New Task window, enter the Work Package ID which you are not staffed, and use F4 tab to choose other fields. Choose Save.Note Please enter the exact work package ID. Since all other information is from work package. You can't create tasks beyond existing project information. | An unstaffed project task is created. Comparing with staffed project tasks, it has no planned hours.To enable the feature of unstaffed project time recording, the following prerequisites must be met:The service organization of the employee needs to be planned as demand accordingly in the work package.In SSCUI Maintain Data Entry Profile, choose Unstaffed Project.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.When creating a project, Restrict Unstaffed Posting under Project Settings must be No.Note If the unstaffed employee becomes staffed, it is the employee's duty to delete manually created task, since it will be duplicated with system created tasks. |  |
| 14 | Unstaffed Project Time Recording | Choose the Unstaffed Project task to create a new entry, or modify/delete existing entries. For details please refer to step 6-9. | The time entry can be created, modified or deleted. |  |

#### Time Recording through new Manage Timesheet App (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform the time recording process through the Manage Timesheet app.

|  |
| --- |
| Note The Manage Timesheet app (F1823A) is limited to internal employees assigned to PSA projects. Enablement for contingent workers (CWs) is planned as part of future enhancement and currently not supported. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On and Access My Timesheet | Log on to the SAP Fiori launchpad with the user for whom timesheet is to be recorded and then open Manage Timesheet.Note The time recording in Manage Timesheet App (F1823A) can be done only by the employee and not on behalf either by the project manager and line manager. | The My Timesheet screen displays. |  |
| 2 | Select Date Range | By default, the timesheet shows the current week.The target hours on the header area indicate the total hours that need to be submitted for the current week (excluding weekends). Submitted hours include hours which are submitted for approval, which are already approved and approved absence hours. The hours not submitted include the hours which are in draft state and hours that are ready to be submitted. Hours not recorded are those hours which are yet to be recorded/submitted in the timesheet. The rejected hours indicate those hours which has been rejected by the approver.If you want to record times in a different week, select the date range line, just below the create button in the Manage Timesheet app. | A calendar entry dialog box displays allowing you to choose the week you wish to display.The monthly overview, which is available on the top right corner gives an overview of the entire months with different color coding which indicates if the timesheet is approved/ready to submit/missing time/non-working day/today/selected/non-working day. The color coding can be viewed by clicking on the button near the monthly overview tile.Note By default, the work week is visible. It can also be changed to day view using the day button. If the entire week has to be shown, click on the setting icon near work week and disable the show work week toggle. Additionally the time format can be changed to decimal notation (1,00 H) or clock notation (Ex: 01:00 H). |  |
| 3 | Explore Your Tasks |  | The tasks (labeled by combination of: project, customer name, work packages, activity type, work items, task start date, task end date, accounting category, planned hours, recorded hours, source type) assigned to you are displayed on the right side of the screen under Tasks tab.They are automatically prefilled in the Tasks list if the employee is staffed to a work package. The automatically created tasks cannot be deleted. The manually created tasks can be deleted via manage tasks for timesheet app (F8824).Across each task, you would see the hours already recorded for that task.Note Specify Task Types, Components, and Levels, the self service configuration UI, can be used to define these non-project related task types. |  |
| 4 | Search for Your Tasks (optional) | On the right side of the screen, click on the filter button.The search can be performed through various attributes: Customer, project id/name, work item id/name and work package id/name. | The tasks assigned to you are filtered according to the text inserted in the search box. |  |
| 5 | Record Working Time - Create draft version of the task | Click on the create button. The create time recording pop-up appears. Enter the duration (for example 2 hours) without selecting any task and click on keep draft. | The draft version of the timesheet is created. The hours updated are visible on the timesheet entry. |  |
| 6 | Record Working Time - Update the draft version of the task | Select the draft version of the added hours (from the previous step). The time recording details pop-up appears. Perform the below steps:Task: Select the task from the F4 help.Date: Change it to tomorrow's date if required.Duration: Update it with the new hours for example, 3 H.Note (optional): Timesheet entry.Work Location (optional): Select the value from the F4 help.Click on save. | The draft version of the timesheet entry changes to Ready To Submit once all the mandatory parameters/attributes are filled. |  |
| 7 | Record Working Time - Discard the draft version of the task | Select the draft version of the added hours (from the previous step). The time recording details pop-up appears. Click on discard. | The draft version of the timesheet entry is discarded. |  |
| 8 | Record Working Time - Create an entry using create button | Click on the create button. The create time recording pop-up appears. Perform the below steps:Task: Select the task from the F4 help.Date: Change it to tomorrow's date if required.Duration: Update it with the new hours for example, 2 H.Note (optional): Timesheet entry.Work Location (optional): Select the value from the F4 help.Click on save.Alternatively, you can record time to a task by selecting a task (from the right side of the screen) from the tasklist by clicking on the add button. | The timesheet entry is created and the status is ready to submit with the work package information task in the timesheet. |  |
| 9 | Select a Task | On the right side of the screen, under Tasks, the tasks assigned to you are shown.By default, the recently used tasks are shown. Choose the task for which the hours need to be booked and click on Add.Note Click on the star button if the task needs to be marked as favourite. Click on the eye symbol if the task needs to be hidden. Using the manage tasks for timesheet we can unhide the task. The Manage Task for Timesheet app is not standalone. It requires an existing task in the Manage Timesheet app first, which then becomes viewable there. | You have selected a task on which you can record times. |  |
| 10 | Record Working time - Create New Time Entry | Choose a task from the list of the available tasks using the add button. The create time recording pop-up appears with the task auto populated.Enter the below values:Duration: Update it with the new hours for example, 2 H.Note (optional): Timesheet entry.Work Location (optional): Select the value from the F4 help.Click on save. | The timesheet entry is created and the status is ready to submit with the work package information task in the timesheet. |  |
| 11 | Record Working time – Create Additional Time Entries | Repeat the step 10, to create additional time entries for the respective tasks. | The timesheet entry is created and the status is ready to submit with the work package information task in the timesheet. |  |
| 12 | Record Working Time – Modify Existing Entries | Choose an existing entry, and in the details dialog box, adapt the Duration field by inserting the number of hours.Save your entry. | The time entry is adapted. |  |
| 13 | Overtime Time Recording | To enter Overtime Category for an activity, choose the respective timesheet entry and click on edit. A dialogue box appears. Alternatively the overtime category can be maintained during the timesheet creation stage itself.In the Overtime Category field, choose F4 to select a proper overtime category and choose Save. Overtime categories are maintained in SSCUI Maintain Overtime Categories.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | The details of the activity are saved. |  |
| 14 | Record Working Time – Delete Existing Entries/Delete Submitted for Approval/Approved entries | Select the timesheet entry that has to be deleted. On the pop-up click on Delete button.Note Approved time recordings, when deleted, are sent to your manager again to approve the deletion. | The selected entry disappears. |  |
| 15 | Record working time - Day functionality | To record working time for day view, switch to Day view. Repeat the steps from 5 to 14 to create/modify/delete the timesheet entry.Note The date will be defaulted to the date which we have chosen. | The timesheet will be created/modified/deleted. |  |
| 16 | Create an Unstaffed Project Task (optional) | At the right top, choose Create Task. In the New Task window, enter the following:Accounting category: Choose customer project/Internal project based on the project which was created.Work Package ID: Enter the work package ID created from the project.Activity type: Choose as junior consultant/senior consultant.Work item (optional): Select from the drop down.Favourite (optional): Choose yes.Click on create task.Note Please enter the exact work package ID. Since all other information is from work package. You can't create tasks beyond existing project information.Alternatively, we can navigate to the manage tasks for timesheet and create the task using the above steps.The timesheet can be submitted using the previous steps (steps 5 to 10). | An unstaffed project task is created. Compared with staffed project tasks, it has no planned hours.To enable the feature of unstaffed project time recording, the following prerequisites must be met:The service organization of the employees needs to be planned as demand according in the work package.In SSCUI Maintain Data Entry Profile, choose Unstaffed Project.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.When creating a project, Enable time posting without staffing under Project Settings must be Yes.Note If the unstaffed employee becomes staffed, it is the employee's duty to delete manually created tasks, since it will be duplicated with system created tasks. |  |
| 17 | Delete a task (optional) | Click on the ... near the create task and navigate to the manage timesheet for tasks.Use the filters project, customer, task, accounting category to find out task which needs to be deleted and click on go.Select the task and click on delete button. A pop-up appears. Choose ok in the pop-up. | The selected task gets deleted. |  |
| 18 | Record working Time - Copy Entries | To copy the timesheet entry, click on the copy button and select either day or week radio button.For day radio button:Select Source Type: choose Single Day.Select Source Date: choose a day with time entries that you want to copy to other days.Select Target Date(s): choose calendar with start date and finish date.Choose Copy.For week radio button:Select Source Date: choose the calendar with a single week with time entries. For example, if you choose from last Monday to last Sunday, and there are time entries within this period, then the start date will be Monday, which is aligned with Calendar Settings, Start Week From: Monday.Select Target Date(s): choose the calendar with a start date and finish date. It must be on weekly base. Here you can choose from Monday to Sunday.Choose Copy. | The timesheet entry will be copied to the respective dates mentioned in the target date column with the status as ready to submit. |  |
| 19 | Record Time | Submit your entries. | The time is saved. Once the entries are submitted, the timesheet entry which are 'ready to be submitted' will turn to orange color with the status as 'submitted for approval' (if approval configuration is enabled).There is a UI adaptation for Submit controlled by SSCUI.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.For details please refer to SAP Product Assistance: [https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD): choose a specific language version of product assistance and navigate by: Configuration Apps > Configuration Apps for Professional Services .If you changed the configuration to Approval Required, in Manage Timesheet (F1823A) app, after choosing Submit, the left side of the time-block turns orange, indicating it is waiting for approval.Note BADI (HCM_CATS_V1_B_TS_VALIDATION) provides checks before saving timesheet entries. To create the BADI please refer to section Custom Logic in 1N9 where a generic example is provided.Please only be aware that you need to select Business Context =HCM: TimeSheet Entry Validation. |  |

### Time Recording for Contingent Worker

#### Optional: Create Task through Manage My Timesheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This optional process step shows you how to create task through manage my timesheet.

Prerequisites

The following business process must be run before this step:

- Create External Service Purchase Orders in Service and Material Procurement – Project-Based Services (J13). The service performer is specified with this contingent worker. When creating PO for external service, please use the right service material item, for example, T001 in order to record the timesheet.
- Maintain the Staffing Work Package in Customer Project Management – Project-Based Services (J11).This contingent worker is selected in the project staffing.

|  |
| --- |
| Note You can create a task in timesheet only if there exists similar planning data in customer project management. System provides following checks when creating a task for a contingent worker:Check on work item selection. If work package is with a work item, then in timesheet creation of tasks without a work item for related work package is not allowed.Check on billing control category based on the purchase order account assignment category:For PO with Account Assignment Category "P" (Project) and "U"(Unknown), Activity Type is optional, you need to enter "Billing Control Category" as "Billable".For PO with Account Assignment Category "K" (Cost Center): Activity Type is a mandatory field. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Contingent Worker (EXTSERVPERF3310 for AE Company). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage My Timesheet (F1823). | My Timesheet displays. |  |
| 3 | Manage My Task | At the right top, choose the  icon in the right side of My Tasks, then open the list item Manage My Tasks. | My task list displays. |  |
| 4 | Create a Task | In the lower right hand corner, choose the Create Task. | The New Task window displays. |  |
| 5 | Enter Field Values | Choose the assigned work package, Purchase Order (the one created in Service and Material Procurement – Project-Based Services for the contingent worker), Work Item (must be filled if it is maintained in work package), Billing Control Category (must be billable if PO account assignment category is P or U) , and Activity Type (optional if PO account assignment category is P or U) .Go back to the My Timesheet screen. | NoteThe work package is staffed with this Contingent Worker (log-in ID), and the staffing status is Confirmed.The external service purchase order is specified with this contingent worker as the service performer. |  |
| 6 | Save the Entry | The new task is saved. | If the new task is duplicated with task created by system, an error message will appear. |  |

#### Time Recording through Manage My Timesheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a time recording is performed and (optionally) approved, a service entry sheet (SES) is created automatically. For each time recording, one SES will be created with one item. Bundling multiple time-recordings within one SES is not supported.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On and Open Manage My Timesheet | Option 1: Log on to the SAP Fiori launchpad as a contingent worker (EXTSERVPERF3310 for AE Company) and open Manage My Timesheet (F1823).In case the contingent workers can't record time for themselves, line manager and project manager can record timesheet on-behalf.Option 2: Timesheet on-behalf by line manager.Log on to SAP Fiori launchpad as a line manager and open Team Utilization (F2582). Select the contingent worker for whom time is to be recorded and choose Edit Timesheet.Option 3: Timesheet on behalf by project manager.Log on to SAP Fiori launchpad as a project manager and open Notify Missing Times (F2556). Select the contingent worker for whom time is to be recorded and select Edit Timesheet. | The My Timesheet screen displays.Note Timesheet on behalf can also be done by project controller. They can be specified as a project role during the run of J11/1A8 Project Management. |  |
| 2 | Select a Task | In the top-right corner of each task, you can see the hours already recorded for that task.Choose a task. | You have selected a task on which you can record time. The selected task is shown in a different color.The tasks assigned to a contingent worker are prefilled in the My Tasks list on the right side. The automatically created tasks cannot be deleted. Only the purchase orders with account assignment type Cost Center and Project will be shown in the task list. Only if a service performer is assigned during the purchase order creation, those tasks will be shown in the My Task list.On the right side of the screen under My Tasks, tasks are labelled with the description of the Projects, Work Packages, Customer, Activity Type, Purchase Order, Work Items.In the top-right corner of each task, you can see the hours already recorded for that task. |  |
| 3 | Record Working Time – Create New Time Entry | To create a new time entry, choose the cell corresponding to the day and the number of hours that you want to record. For example, if you want to record 5 hours, choose the cell just below the number 5 on the day on which you want to record the hours.Interval for Time Recording is by default 30 minutes.You can change Interval for Time Recording (in Minutes) in calendar settings, for example, if the time interval is set to 5 minutes, and you move your mouse across calendar, time will jump from, for example, 2:55 h to 3:00 h.The minimum time slot is preset as 30 minutes, which means if you maintain an entry less than 30 minutes, system will initially provide a time block of 30 minutes. |  |  |
| 4 | Record Working Time – Create Additional Time Entries | Repeat steps 3 for any additional time entry you want to record taking into account the already existing entries. For example, if 2 hours are already registered on a day, and you want to record 5 hours, choose on the cell just below the number 7 on the day on which you want to record the hours. | The new time entries are visualized on the days you have chosen as rectangular boxes. The height of each box fits the number of hours you have inserted. Each entry shows the task title descriptions and the number of hours recorded in the hh:mm format. The left vertical axis shrinks up showing more hours if the total hours on a day exceeds the hours currently visualized. A vertical scroll bar appears on the right side of the screen, so that you can scroll up and down for a better visualization. If recording a time entry on a day the total would exceed 24 hours, the system prompts an error message and prevents you from recording that time entry. The system calculates total hours automatically per day and can be viewed on the bottom bar per day and in the bottom left corner as total per week. |  |
| 5 | Copy Time Entries with Single Day | Choose Copy Time Entries. The Copy Time Entries screen displays.Select Source Type, choose Single Day.Select Source Date: choose a day with time entries that you want to copy to other days.Select Target Date(s): choose calendar with start date and finish date.Choose Copy. | The time entries are copied to target dates. |  |
| 6 | Copy Time Entries with Calendar Week | Choose Copy Time Entries. The Copy Time Entries screen displays.Select Source Type, choose Calendar Week.Select Source Week: choose the calendar with a single week with time entries. For example, if you choose from last Monday to last Sunday, and there are time entries within this period, then the start date will be Monday, which is aligned with Calendar Settings, Start Week From: Monday.Select Target Week: choose the calendar with a start date and finish date. It must be on weekly base. Here you can choose from Monday to Sunday.Choose Copy. | The time entries are copied to target weeks. |  |
| 7 | Record working time – Modify existing entries | Choose an existing entry, and in the Details, adapt the Duration field by inserting the number of hours in the hh:mm format. Save your entry. | The time entry is adapted. The height of the time entry is adapted according to the new recorded hours. |  |
| 8 | Record Working Time – Delete Unapproved Entries | Choose Delete that is on the cross icon in the top-right corner of an entry. | The selected entry disappears. |  |
| 9 | Enter a Work Location and/or Note for an Activity (optional) | To enter an optional work location and a note for an activity, just choose the entry and open a dialogue box. In the Work Location field, choose F4 to select a proper work location. These work locations are maintained in SSCUI Maintain Work Locations. Enter a description up to 300 characters in the Note field and choose Save.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | The details of the activity are saved.The long text note gets displayed in the My Inbox app. Project manager can edit the long text during the billing preparation in the Manage Project Billing (F4374) application. If the Purchase Orders is with Account Assignment Category K, the updated long text can be displayed on the invoice to customers. |  |
| 10 | Record Time | Save your entries. | The times are saved.Note You can write own checks with BADI (HCM_CATS_V1_B_TS_VALIDATION) before saving timesheet entries. |  |
| 11 | Submit for Approval | Choose Submit Week. | The time is ready for approval.After approval, the left side of the time-block turns to green.If the entry is rejected, you will receive a reject notification in upper right of SAP Fiori launchpad. By clicking the notification, you will navigate to the Manage My Timesheet (F1823) app where you can find the left side of rejected entry turns to red. You can modify the entry and submit again. Then the notification is gone. |  |
| 12 | Delete Approved Entries | Choose a timesheet which has been approved, then choose Delete that is the cross icon in the top-right corner of an entry. Choose Save, a Zero Hour Entries Icon appears on the time axis. Choose Submit, this zero hour entry will be sent for approval.Note You are not allowed to modify or delete time recordings if supplier invoices have been created. | After approval, the Zero Time Entries icon disappears. The time recording has been deleted. The according SES will be deleted automatically when the corresponding time recording is deleted.If the time records can’t be deleted, please follow the revoke process as follows:Purchaser uses Manage Service Entry Sheet app to revoke approval for approved service entry sheet and delete the service entry sheet item, then send for approval to project manager.Project manager approves the SES via My Inbox app.Consultant deletes the entries in Manage My Timesheet (F1823) app.Project Manager approves the time entry deletion in My Inbox app. |  |
| 13 | Create an Unstaffed Project Task | At the right top, choose the  icon in the right side of My Tasks, then open the list item Manage My Tasks. In the lower right hand corner, choose Create Task, then Unstaffed Project. In the New Task window, enter the Work Package ID which you are not staffed, and use F4 tab to choose other fields. Choose Save.Note Please enter the exact work package ID, since all other information is from work package. You can't create tasks beyond existing project information. | An unstaffed project task is created. Comparing with staffed project tasks, it has no planned hours.To enable feature of unstaffed project time recording, here are prerequisites:The service organization of the employee needs to be planned as demand accordingly in the work package.In SSCUI Maintain Data Entry Profile, choose Unstaffed Project.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration.When creating a project, Restrict Unstaffed Posting under Project Settings must be No.Note If the unstaffed employee becomes staffed, it is the employee's duty to delete manually created task, since it will be duplicated with system created tasks. |  |
| 14 | Unstaffed Project Time Recording | Choose the Unstaffed Project task to create a new entry, or modify/delete existing entries. For details please refer to step 3-6. | The time entry can be created, modified or deleted. |  |

|  |
| --- |
| Note Skip the following [Approval or Rejection of Working Times](#unique_11) [page ] 26 step if the left side of the time-block turns green. |

### Approval or Rejection of Working Times

Purpose

This process step shows you how to approve or reject time recording.

|  |
| --- |
| NoteAs a key user, when configuring your solution to maintain data entry profiles, you can:Switch on or off the approval process. By default, approval is required for contingent workers.Select the accounting objects that is used by the customer for their processes like Cost Center, Activity Type, and Receiver Order.Enable Extensibility Mode to transfer additional customer field.Define the period for which you want to get the missing time entries (like 60 days or 120 days).With BAdi (HCM_CATS_VI_B_APPROVER_DETEMN), you can determine the approver for the time entries. Please only be aware that you need to select Business Context = HCM: Timesheet Approver Determination.If line manager is determined as the approver, please assign business catalog SAP_HCM_BC_TS_WIAPPROVE_PC to business role line manager, so that My Inbox app is available for time entry approval. |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, you can choose one of the following options to access configuration steps:

- Manage Your Solution:

In the SAP S/4HANA Cloud Public Edition system, in the SAP Fiori launchpad, open the Manage Your Solution (F1241) app and go to View Solution Scope.

- SAP Central Business Configuration:

In the Scope and Organizational Structure phase, navigate to the Activities tab. Search for Define Scope and choose Open.

#### Working Times with App My Inbox

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to work times with My Inbox (F0862) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open My Inbox (F0862). On the left part of the screen, choose the Approval of Working Times task. | In the right part, you can see the Approval of Working Times app. |  |
| 3 | Explore the App Approval of Working Times | Navigate and create your own views. | The app is now supporting to search/filter by both projects/work packages and employee.You can create your own view and set default view on My Views screen by choosing Select View.You can add additional filters/fields by choosing Setting.In Time Entries list, you can open it on full screen by choosing Maximize icon. You can also see Previous Duration indicating how many hours have been previously approved for this time entry by choosing Previous Time Entry icon.Note maintained in the Manage My Timesheet (F1823) app (for example, a long text) is also visible here.For Priority: If first time entry difference is greater than 7 days when we compare with the current date, then the priority is high otherwise medium.Note Field extensibility is enabled in the My Inbox (F0862) app, the transferred customized fields are hidden fields. |  |
| 4 | Approve the Timesheet | Select entries that can be approved, and then choose Approve. | The Approve Time Entries screen displays. Choose Approve, and the time entries are approved. |  |
| 5 | Reject the Timesheet | Select entries that can be rejected, and then choose Reject. | The Reason for Rejection screen displays for you to select a rejection reason. After that, the Rejection Time Entries screen displays.Choose Reject, and the time entries are rejected.Note You can define your own rejection reasons by SSCUI with the Manage Your Solution (F1241) app in the SAP Fiori launchpad or via the configuration activity in the Realize phase in the project experience of SAP Central Business Configuration. |  |
| 6 | Log On and Open Manage My Timesheet (Old Application) and Find the Approved/Rejected Entries | Log on to the SAP Fiori launchpad with the user whose time recording has been approved or rejected (e.g. INTSERVPERF3310), then open Manage My Timesheet Fiori app. | The left side of the time-block turns green indicating it has been approved.The left side of the time-block turns red indicating it has been rejected.Choose Notifications in the upper right corner. In the tab By Priority, a rejection notification is shown. |  |
| 7 | Log On and Open Manage Timesheet (New Application) and Find the Approved/Rejected Entries (Optional) | Log on to the SAP Fiori launchpad with the user whose time recording has been approved or rejected (e.g. INTSERVPERF3310), then open Manage Timesheet Fiori app. | The left side of the time-block turns green indicating it has been approved.The left side of the time-block turns red indicating it has been rejected.Choose Notifications in the upper right corner. In the tab By Priority, a rejection notification is shown. |  |

### Notify Missing Time

Purpose

This process step shows you how to use the APP to check if all the timesheets are up to date before creating a billing document request. This ensures that every month before creating a billing document request, the user can review the timesheets and notify employees if there are missing entries so that there is no error during billing process. To do this, you need to:

1. Whitelist the domain in the system. For details, please refer to SAP Product Assistance - [https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD): choose a specific language version of product assistance and navigate by: Human Resources → Time and Attendance Management → Schedule Job for Sending E-mails - Missing Time Entries. Details are in the last section of Configurations.
2. Prepare an email address to receive missing time notification emails.

The following steps show you how the project manager reviews if there is missing time recording and notifies the project members with missing entries so that there is no error during billing process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager - Professional Services. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Notify Missing Times (F2556). | The title shows missing time recordings of the project members via KPI (launchpad view) for Current and Last month.The Notify Missing Time screen opens showing a list of all project members of the current month assigned in projects. The Time Period is preset to current month.Note The Notify Missing Time app is also available for project controllers. They can be specified as a project role during the run of J11/1A8 Project Management. |  |
| 3 | View Missing Time Information | Search/ filter (Project, Work Package, Activity Type, Work Package, Work Item, Activity Type, Planned Effort, Recorded Hours, Approved Hours, Missing Hours, Missing Hours (%), Activity Type ID, Employee External ID, Project ID, Type of Workforce, Unapproved Hours, Work Item ID, Work Package ID) manually for project members with missing time recordings, that are beyond a selected threshold.Revise the following filter and choose Go.Time Period: Last MonthMissing Hours (%): >20Check the following information:NameProjectWork PackageWork ItemActivity TypePlanned EffortRecorded HoursApproved HoursMissing Hours | The list is refreshed. System provides notifications with the missing time information.System provides a list with all consultants that have missing time recordings, based on the selected threshold value.You can press the Export to Spreadsheet icon to export the Project Member list.Clicking the link on Name.The contact card of the project members opens.Note Planned Effort is from work packages of project. If in work package there are distributions between several months, the system will only show the distribution for selected time period.Recorded Hours only gets updated after project members recording time in the past: |  |
| 4 | Send Reminders to Project Members | Choose one checkbox for one project member with a missing time record and choose Send Reminder. | The system sends out email to the selected project member.Note You can also schedule a job to notify missing time. For details, please refer to [SAP Product Assistance](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD): choose a specific language version of product assistance and navigate by: Human Resources > Time and Attendance Management > Schedule job for Sending E-mails-Missing Time Entries .System provides a default email template. However, you can customize an e-mail template if you want to provide a different email text to the employees. For details, please refer to [SAP Product Assistance](https://help.sap.com/viewer/p/SAP_S4HANA_CLOUD): Choose a specific language version of product assistance and navigate by: Human Resources > Time and Attendance Management > Notify Missing Time . |  |
| 5 | Check the Application Log | Find and open Monitor Missing Time Notifications. | The Application Log is pre-filtered with category CATS and subcategory EMAIL_PMTS so that information on sent email notifications is displayed. |  |
| 6 | Check the Notification Email | Please use your pre-defined email to check the notification.Note This step is not in SAP S/4HAHA. | The notification mail is received. |  |

### Analyze Team Utilization

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, with the Team Utilization (F2582) app, a line manager will be able to see the average utilization of his/her team. This app helps the line manager to get an overview of his team’s utilization and take actions on resources who are not utilized fully.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Manager - HR Info (a.k.a Line Manager). | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Team Utilization (F2582). | The tile shows the team utilization rate for last three months.The Team Utilization screen opens showing a list of all your team members' utilization. The Time Period is preset to current month. |  |
| 3 | View Team Utilization | Revise filter, for example: Date Range and choose Go. You may choose Adapt Filters to select more filters.With View Setting icon, you can select more items like Image, Name, Utilization Rate (%), Billable Hours, Non-billable Hours, Available Hours, Organizational Unit, Cost Center Name, Service Cost Level, Job Title, Employee ID, Approved Hours, Company Code, Cost Center, Organization Unit Code, Personnel Number, Total Recorded Hours, Type of Workforce, and Unapproved Hours.You may choose the Export to Spreadsheet icon to download the team member list. | The list is refreshed.The list shows information such as Name, Utilization, Billable Hours, Non-billable Hours, Available Hours, and so on.Utilization bar chart will turn to green when utilization is over 70%. |  |

## Appendix

### Process Chains

The process to be tested in this test case is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test case, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Customer Project Management – Project-Based Services (J11) | This is the main end-to-end business process. |
| Internal Project Management – Project-Based Services (1A8) | This is the main end-to-end business process. |

#### Preceding Processes

You may first have completed the following business processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| Customer Project Management – Project-Based Services (J11) | Employee must be assigned to a project created in J11. |
| Internal Project Management – Project-Based Services (1A8) | Employee must be assigned to a project in 1A8. |
| Exception-Based Core HR with SAP SuccessFactors Employee Central (JB1) | This process should be run to have employee data replicated to SAP S/4HANA Cloud Public Edition. |

#### Time Confirmation in Closed Periods

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In case a consultant records time in a closed financial accounting period, the time confirmations are still saved to ensure a correct utilization reporting and a correct confirmation date on the billing document. However, the transfer of the timesheet documents to accounting fails. The failed documents are stored in an operation que and an error log is created. As a result, you need to transfer the failed time recordings to controlling with a posting date in an open period.

For example:

- The consultant enters his time on March 26 for February 7, with February being a closed financial period.
- An accountant can post this confirmation in the next open period by providing a posting date, for example, March 1.
- This will create a journal entry with:
    - Document date March 26
    - Posting date March 1
    - Service rendered date February 7

Procedure

There are two options to process unposted time confirmation.

Option1: through the app, Process Unposted Time Confirmations (CAT7)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the App | Open Process Unposted Time Confirmations (CAT7). | CATS: Transfer to Controlling app is opened. |  |
| 3 | Find out the Time Recordings in Closed Periods | Choose Test Run and choose Execute.Make a note of the Employee ID, Date, or Document Number for which you want to correct the CO postings (for example, Employee ID: EMPLOYEE), then go back to CATS: Transfer to Controlling. | A list of records containing errors (and also time recordings in closed periods) is displayed.Note down the time recordings in closed periods which you want to transfer to controlling. |  |
| 4 | Transfer Time Recording to Controlling | Enter the noted selection parameters (for example, Insert EMPLOYEE as Employee ID) as well as a posting date in an open period.Deselect Test Run and choose Execute. | All applicable time entries will result in journal entries (for example, all time recordings of EMPLOYEE)A journal entry will be created including new field service rendered date, for which the consultant entered the confirmation. The service rendered date is stored in the journal entry and forwarded to time and material billing. With the service rendered date the cost rate is derived. |  |

Option 2: through an application Job, Process Unposted Time Confirmations (SAP), in app “ Schedule Overhead Accounting Jobs (F3767)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the App | Open Schedule Overhead Accounting Jobs (F3767). | A list of application jobs is displayed. |  |
| 3 | Create a New Job to Process Unposted Time Confirmation | Choose Create. | The New Job screen displays, which includes three steps. |  |
| 4 | Schedule a New Job to Process Unposted Time Confirmation | Under 1.Template Selection, field Job Template, please choose F4 to search and select Process Unposted Time Confirmations (SAP).Choose Step 2 to revise your Schedule Options.Step 3 is optional, which allows you change Selection Parameters. For example, Insert EMPLOYEE as Employee ID, as well as a posting date in an open period.Choose Schedule. | All applicable time entries will result in journal entries (for example, all time recordings of EMPLOYEE)A journal entry will be created including new field service rendered date, for which the consultant entered the confirmation. The service rendered date is stored in the journal entry and forwarded to time and material billing. With the service rendered date the cost rate is derived. |  |

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
- related-to :: [[14-maintenance-service-and-projects/test-script-sap-s-4hana-cloud-public-edition-time-recording-1q4-ae-754]]
- see-also :: [[10-procurement/test-script-service-and-material-procurement-project-based-services-j1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J12_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 74,041 chars in the whole document
