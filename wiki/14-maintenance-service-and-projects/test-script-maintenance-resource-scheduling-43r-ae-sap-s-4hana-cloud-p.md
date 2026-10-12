---
id: 14-maintenance-service-and-projects/test-script-maintenance-resource-scheduling-43r-ae-sap-s-4hana-cloud-p
title: "Test Script: Maintenance Resource Scheduling (43R_AE), SAP S/4HANA Cloud Public Edition (43R_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 43R Maintenance Resource Scheduling: prerequisites, Fiori app test steps, process chain."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/maintenance-resource-scheduling]
aliases: [43R_S4CLD2608_BPD_EN_AE]
keywords: [Maintenance Resource Scheduling, scope item testing, maintenance schedule, work center utilization, work center capacity, schedule freezing, operation dispatching, maintenance scheduling board, maintenance schedule for assets, person responsible assignment]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/43R_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-999
topic: 14-maintenance-service-and-projects/maintenance-resource-scheduling
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Maintenance Resource Scheduling (43R_AE), SAP S/4HANA Cloud Public Edition (43R_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/43R_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Maintenance Resource Scheduling** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Maintenance Resource Scheduling (43R_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854538)

[2 Prerequisites 4](#_Toc232854539)

[2.1 System Access 4](#_Toc232854540)

[2.2 Roles 4](#_Toc232854541)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232854542)

[2.4 Business Conditions 5](#_Toc232854543)

[2.5 Assign Work Centers 6](#_Toc232854544)

[2.6 Create Work Center Team 7](#_Toc232854545)

[2.7 Create Planning Bucket 8](#_Toc232854546)

[3 Overview Table 10](#_Toc232854547)

[4 Test Procedures 11](#_Toc232854548)

[4.1 Manage Schedule 11](#_Toc232854549)

[4.2 Freeze Schedule 14](#_Toc232854550)

[4.3 Assign Person Responsible to Order Operations 15](#_Toc232854551)

[4.4 Work with the Maintenance Scheduling Board 16](#_Toc232854552)

[4.5 Work with the Maintenance Schedue for Assets App 18](#_Toc232854553)

[5 Appendix 20](#_Toc232854554)

[5.1 Process Integration 20](#_Toc232854555)

[5.2 Preceding Processes 20](#_Toc232854556)

[5.3 Succeeding Processes 20](#_Toc232854557)

## Purpose

Overview

Resource scheduling provides you with insights into your maintenance workload and available capacities for current and upcoming maintenance activities. Use the apps for resource scheduling to check current and forecast work center utilization, build schedules, and determine required capacities before dispatching the scheduled work.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | You can access this app using the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Maintenance Planner - Resource Scheduling | SAP_BR_MAINTENANCE_PLANNER_RSH |  |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Maintenance Plant | 1710 | Plant 1 |  |
| Work Center | RES-0100 | Mechanics |  |
| Work Center | RES-0200 | Electric |  |
| Work Center | RES-0300 | Instrumentation |  |

You must have the required authorizations to work with maintenance orders, work centers, and plants.

You must ensure that maintenance orders and operations are available.

You must ensure that work centers have been set up, and capacities have been defined for these work centers.

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BH1 - Corrective Maintenance | Create maintenance orders with operations as described in any of these scope items to use RSH functionality. |
| BH2 - Emergency Maintenance | Create maintenance orders with operations as described in any of these scope items to use RSH functionality. |
| 4HH - scope_item_titles/4HH_desc | Create maintenance orders with operations as described in any of these scope items to use RSH functionality. |
| 4HH - Reactive Maintenance | Create maintenance orders with operations as described in any of these scope items to use RSH functionality. |
| 4HI - Proactive Maintenance | Create maintenance orders with operations as described in any of these scope items to use RSH functionality. |
| 4VT - Improvement Maintenance | Create maintenance orders with operations as described in any of these scope items to use RSH functionality. |
| 4WM - Operational and Overhead Maintenance | Create maintenance orders with operations as described in any of these scope items to use RSH functionality. |

### Assign Work Centers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To see work center data in the app, you can assign the relevant work centers to yourself before you start working with the apps.

|  |
| --- |
| Note In order to be shown in the resource scheduling apps, work centers must be set up correctly and capacities must be defined for each work center. This is usually done by a key user. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner - Resource Scheduling. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Access the Resource Scheduling for Maintenance Planners (F2227) appChoose the user profile button on the top right hand corner of the screen.Choose My Work Centers. | The Assign Work Centers popup screen is displayed. |  |
| 3 | Assign work centers to yourself | Add a row (+) and enter the name of the work center that you want to assign to yourself.Select the right work center from the list of proposed work centers.Choose Assign. | The work center is assigned to your user. Data for the selected work center is shown in the resource scheduling apps. |  |
| 4 | Change work center capacity (optional step) | Choose the Work Center Utilization card.Choose Change Work Center Capacity.The work centers that are currently assigned to you are shown.Select a calendar week and find the work center for which you want to change the capacity.Change the number of resources if required.You can change capacity for the current date or a date in the future. Once you've started making changes, the Target Week field becomes read-only.Choose Save.Note To change the work center capacity, it is mandatory that the active version, for example, '01 normal available capacity' is assigned to the required work center master.Go to Change Work Center, choose Scheduling. Scroll down to Capacity tab and assign the active version in section Available Capacity. | Work center capacity for the selected period is changed. |  |

### Create Work Center Team

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step helps you create a team of people that are assigned to a performing work center. Any person who is a member of a performing work center's team can be selected by a maintenance planner or a supervisor during planning to carry out tasks at that work center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner - Resource Scheduling. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the app | Access the Manage Teams and Responsibilities - Asset Management (F4988) app | The Manage Teams and Responsibilities for Work Centers (F4988) app opens. |  |
| 3 | Get List of Teams | Enter the following:Category: MAINT_TEAM (Maintenance Work Center Team)Choose Go. | Based on the filter criteria, a list of Teams is displayed. |  |
| 4 | Create Team and Assign Members | Choose CreateOn the New Team screen, in the General Information section, enter the following:Name: <Entry of your choice>Description: <Entry of your choice>Status: EnabledType: SMNT_TEAM (Maintenance Work Center Team)In the Responsibility Definitions section, enter the following:PerformingWorkCtr: <Entry of your choice>In the Team Owners section, choose Create and enter the following:Business Partner: <Entry of your choice>Press EnterNote By default, this field is populated with business partner of the user who creates the team, but you can choose to update the team owner.In the Team Members section:Choose CreateSelect the team member and choose OKEnter Functions: <Entry of your choice>Note More than one team member can be assigned to a work center team.Choose Create | Team is created and team members are assigned to team. |  |

### Create Planning Bucket

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can create maintenance planning buckets that aid you in effectively managing your maintenance backlog. By defining maintenance planning buckets, you can divide the maintenance effort into manageable groups based on their scope. The scope of a planning bucket includes time, but also other important attributes of the maintenance jobs such as the planner group.

Procedure

This section describes test procedures for each process step that belongs to this scope item.

Table 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Maintenance Planner. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Manage Maintenance Planning Buckets (F3888) | The app opens. |  |
| 3 | Create New Planning Bucket | Choose the Create button. Enter the following information:Label: <PUMP_3310>Description: <Planning Bucket for Pump Unit>Type: Event Based MaintenancePlanning Plant: 3310Start Date and Time: Todays date/TimeDuration: 7 DaysRecurrence: OnceScope:Planner Group: <Entry of your Choice >Maintenance Plant: 3310Technical Object: 233100091Plant Section: <Entry of your Choice >Main Work Center: <Entry of your Choice >Choose Create. | Planning bucket is created. |  |

## Overview Table

The scope item 43R - Maintenance Resource Scheduling consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step # | Business Role | Transaction App | Expected Result |
| --- | --- | --- | --- |
| [Manage Schedule](#unique_11) | Maintenance Planner - Resource Scheduling | Resource Scheduling for Maintenance Planners (F2227) | A schedule is created with the required order operations. The order operations are scheduled and dispatched. |
| [Freeze Schedule](#unique_12) [page ] 14 | Maintenance Planner - Resource Scheduling | Manage Schedules (F3326) | The schedule is frozen and is ready for execution. |
| [Assign Person Responsible to Order Operations](#unique_13) [page ] 15 | Maintenance Planner - Resource Scheduling | Assign Maintenance Order Operations (F3423) | A person responsible is assigned to the relevant order operations. |
| [Work with the Maintenance Scheduling Board](#unique_14) [page ] 16 | Maintenance Planner - Resource Scheduling | Maintenance Scheduling Board (F2603) | Operations and suboperations are dispatched. Work center utilization is manged. |
| [Work with the Maintenance Schedue for Assets App](#unique_15) [page ] 18 | Maintenance Planner - Resource Scheduling | Manage Maintenance Schedule for Assets (F4577) | When an asset (functional location or equipment) is under maintenance in the next 4 weeks is shown. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Order operations can be scheduled based on the priority/criticality of the work. Schedules can be created for a target week by selecting operations from multiple maintenance orders. Refinement of the schedules can be done based on the utilization forecast of the work centers for the week.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Maintenance Planner - Resource Scheduling | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the Resource Scheduling for Maintenance Planners (F2227)app | Choose the Resource Scheduling for Maintenance Planners tile. | The Manage Work Center Utilization (F2222)appopens. |  |
| 3 | Enter the Filter Values | Enter the required filter values and choose Go button.Note You can use a variant with auto apply. You have to manually adjust existing variants if desired. | The cards of resource scheduling will get displayed. |  |
| 4 | Access the Work Center Utilization card. | Choose the header area of Work Center Utilization card. | The Manage Work Center Utilization (F2222) app opens, showing a list of order operations with selected parameters. By default, the following filters are set:Time Period: Next 4 Weeks |  |
| 5 | Create Schedule | Select due order operations by selecting the checkbox.Choose Add to Schedule. A dialog box opens.Select Create New Schedule and enter a schedule name and the time period (define timeframe for the schedule).Note You can also add the selected order operations to an existing schedule.Choose Create and Open Schedule.Note The option to add to schedule is now available on order level. Select Maintenance Orders tab in the Manage Work Center Utilization screen and follow the same steps mentioned above for orders.Note You can also use Generate Schedules (F6966) app to allow the system to generate automatic schedules. | The Manage Schedules (F3326) app opens with the newly created schedule. The schedule includes the selected operations as well as operations that have already been dispatched or are in process and whose dates overlap with the time period of schedule. |  |
| 6 | Level Work Center Utilization | Check the weekly utilization forecast on the List View tab.If work center utilization is not yet optimal, use one of the following options:Add more due order operations. To do so, use the back button and follow these steps:Select few more due order operations by selecting the checkbox.Choose Add to Schedule. A dialog box opens.Select the radio button Add to Existing Schedule and then select the schedule created in previous step.Choose Add and Open Schedule.Remove order operations from the schedule if there's not enough capacity to complete them in the target week. To do so, follow these steps on the Manage Schedule page:Select the operation on the List View tab.Choose the Remove button.To move order operations to another work center, select the operation by marking the checkbox and choose the required work center from the Change Work Center dropdown list. | The weekly forecast is updated according to your changes. |  |
| 7 | Refine Schedule | In the Manage Schedules (F3326) app, choose Refine Schedule to start planning at day level.Select the order operations whose start day you want to set by marking the checkbox.Schedule the selected order operations by using one of the following options:Choose Schedule Automatically.The app finds a start day and time slot for each order operation.An information popup is displayed. Select on Do not show again and choose OK.Choose Set Start Date and Time.Note If the schedule is for more than 7 days, you can select the start date and time by choosing the Set Start Date and Time button.If the schedule is for 7 days, you can select the start date by choosing the Set Start Date dropdown list. | The status is changed to Refinement and the order operations are scheduled. |  |
| 8 | Dispatch Order Operations | Choose the arrow on the Freeze Schedule button.Choose Save and Dispatch Operations. The app tries to dispatch all scheduled operations.Note • In the 9-phase maintenance process, the order must be released to be able to dispatch them.• It is also possible to dispatch individual operations without having a schedule. To do so, open the Resource Scheduling for Maintenance Planners (F2227) app and choose the Work Center Utilization card. Then, select the Operation checkbox and choose the Dispatch button. Alternatively, you can open the Maintenance Scheduling Board (F2603) app and dispatch the operations. | The scheduled order operations are dispatched. |  |
| 9 | Cancel the Dispatch | Open the Resource Scheduling for Maintenance Planners (F2227) app.Choose the header area of the Work Center Utilization card.The Manage Work Center Utilization app opens.Filter the list of order operations for the order operations whose dispatch you want to cancel.Note You may have to change the time period and work center in the filter bar.Select the relevant order operations by marking the checkbox.Choose Cancel Dispatch.Note Alternatively, the Maintenance Scheduling Board (F2603) app could be used to cancel and dispatch the operations. | The status of the selected order operations changes back to Due. |  |
| 10 | Change Start Date of Dispatched Operations | Note You are still in the Manage Work Center Utilization app.Select the relevant order operations by marking the checkbox.Choose Change.Enter a new start date (and, if required, time).To immediately dispatch the operation, select the relevant value in the Trigger or Cancel Dispatch field.Choose Change.Note Alternatively the Maintenance Scheduling Board (F2603) app could be used to reschedule or move the operations. You can also drag and drop the operations. | The dates of the selected order operations are changed. |  |

### Freeze Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When you are satisfied with the utilization forecast for the target week, you can dispatch the scheduled order operations and freeze the schedule. Freezing a schedule allows you to monitor schedule attainment and track schedule execution once the target week starts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Maintenance Planner - Resource Scheduling | The SAP Fiori launchpad is displayed. |  |
| 2 | Open the Manage Schedules (F3326) App | Choose the Manage Schedules tile. | The Manage Schedules (F3326)app opens, showing a list of your schedules. |  |
| 3 | Select Schedule | Choose the schedule that you want to freeze. | The schedule opens. |  |
| 4 | Finalize Schedule | If you are ready to hand the schedule over for execution, choose Freeze Schedule.Any remaining due operations are removed automatically.Note The app also “freezes” the planned work and work center for an operation as well as the available work center capacity. This is required so that you can track and monitor schedule attainment once the target week starts. | The schedule has been frozen and is ready for execution. |  |

### Assign Person Responsible to Order Operations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use this app to assign a person responsible to operations.

Procedure

| Test Step # | Test Step Name | Instruction | Pass / Fail / Comment |
| --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Maintenance Planner - Resource Scheduling | The SAP Fiori launchpad screen displayed. |
| 2 | Open the Assign Maintenance Order Operations (F3423)app. | Choose the Assign Maintenance Order Operations tile. | The Assign Maintenance Order Operations (F3423)app opens. |
| 3 | Select Order Operations | To find the order operations that have not yet been assigned to a person responsible, follow these steps:In the filter bar, in the Assignment Status field, enter Unassigned.Choose Go.Note You can also change other filter values, for example, the time period. | The app shows a list of unassigned order operations for the relevant time period. |
| 4 | Assign Person Responsible | To assign a person responsible, follow these steps:Select the order operations to which you want to assign a person responsible by marking the checkbox.Choose Assign.Enter the name of the person that you want to assign and select a name from the list that appears or you can choose the Filter button and select people based on the performing work center.Choose Save. | The selected person is assigned as person responsible to the selected operations. |
| 5 | Unassign Person Responsible | To take back the assignment of a person responsible, follow these steps:Select the relevant operations by marking the checkbox.Choose Unassign.Choose Save. | The selected order operations no longer have a person responsible assigned. |

### Work with the Maintenance Scheduling Board

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This app allows you to visualize on a timeline the maintenance orders, order operations, and suboperations in your work centers. You can also dispatch operations, suboperations and level work center utilization by changing the start date and work center for order operations.

Procedure

| Test Step # | Test Step Name | Instruction | Pass / Fail / Comment |
| --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Maintenance Planner - Resource Scheduling | The SAP Fiori launchpad home page is displayed. |
| 2 | Open the app. | Choose Maintenance Scheduling Board (F2603). |  |
| 3 | View a list of maintenance orders with operations and suboperations | Enter the required filter values and choose Go.Expand the table entries to see order operations and suboperations included in an order. | The relevant maintenance orders are shown in their hierarchical structure in the table area and in the Gantt chart. |
| 4 | Assign People | Right-click on the maintenance operation bar and choose Assign in the context menu.A Gantt chart will open with the list of people assigned to the team.Click on Assign button.Choose Save.Note The availability and assignments of each person is shown in white and gray color.White area - Person is available.Gray area - Person is not available.If the assigned people are already having some other assignment in the same interval, then in the chart it will show ‘Conflicts’ using a red line. |  |
| 5 | See assigned person in the chart(Optional) | Display the name of the assigned person in the chart next to the operation bar.Go to Settings.Select the Labels tab.Choose Maintenance Order Operation from dropdown list.Choose Assigned People from dropdown list for one of label position and choose OK. | The name of assigned person is shown in the chart. |
| 6 | Add new columns in the table area. | Choose the Column Settings iconIn the Columns tab, select the columns that should be displayed in the table.Choose OK. | The column is added and the corresponding values are displayed in table area. |
| 7 | Make settings to show additional information and enable the toggle buttons in the Gantt chart. | Open the settings and select the relevant options.For example:You can set the layout for indicating the current time, showing the cursor line, and so on in the Layout tab.You can set the utilization threshold and change the colors accordingly. By selecting the Utilization checkbox under Work Centers tab, you can enable the quick toggle button for showing or hiding the work center utilization.By selecting Show Implicit Relationships and Show Explicit Relationships checkboxes under Elements tab, you can enable the quick toggle button for showoing or hiding the relationships.You can add labels for order bars of maintenance orders or maintenance order operations under Labels tab.Choose OK. | Graphical elements and quick toggle buttons are added to the chart based on your settings. |
| 8 | Move order operations to another date | To move multiple order operations at the same time:Select the operations and choose Change.In the dialog box that opens,Enter the new date and time in Must Start On field (Note that the date and time must be in the future).Select the relevant value in the Trigger or Cancel Dispatch field.Choose Change.To move multiple orders or multiple operations, drag and drop the order or operation bar at the new date in the Gantt chart. | The operations are moved accordingly and a Must start on constraint is set. If an operation had already been dispatched, the processing status changes back to Due.If an operation could not be moved, you will see an error message.If you move an operation using drag and drop, the app adjusts the start time to the nearest hour to the drop position. |
| 9 | Remove constraints for order operations | Select the relevant order operations in the table area. Note that the order operations must not yet be in process.Choose Remove Constraints. | All constraints are removed for the select order operations. |

### Work with the Maintenance Schedue for Assets App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Maintenance Schedule for Assets app shows you when an asset (functional location or equipment) is under maintenance in the next 4 weeks. You can view the asset in its hierarchical structure, including all subassets.

Procedure

| Test Step # | Test Step Name | Instruction | Pass / Fail / Comment |
| --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as Maintenance Planner - Resource Scheduling | The SAP Fiori launchpad home page is displayed. |
| 2 | Open the app. | Choose Maintenance Scheduling Board (F2603). |  |
| 3 | View a list of maintenance orders and add column for technical object. | Enter the required filter values and choose Go.Choose the Column Settings iconIn the Columns tab, select Technical Object.Choose OK. | Technical object column displayed. |
| 4 | Navigate to the maintenance schedule for an asset | In the table area, chose the Technical Object hyperlink.You can also use the link in the Equipment or Functional Location hyperlink, depending on the type of technical object.2. In the pop-up, choose Open Maintenance Schedule. | The Manage Maintenance Schedule for Assets (F4577) app opens.The table area shows the asset in its hierachical structure, including all subassets that are currently installed. The Gantt chart shows you when the asset is under maintenance in the next 4 weeks. |
| 5 | Display maintenance event | Open the settings and select the Show Maintenance Events check box under Elements tab then choose OK.Note Event-based maintenance planning bucket was created for at least one of the shown assets (technical objects). | Maintenance Events is now displayed in the chart. |
| 6 | Move order to another date | Select the order bar in chart and then drag and drop it to required date. | Order is shifted to new date. |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

### Preceding Processes

You should create maintenance order with operations by following the process mentioned as part of the any of the below business process.

| Process | Business Condition |
| --- | --- |
| BH1 - Corrective MaintenanceBH2 - Emergency MaintenanceBJ2 - Preventive Maintenance4HH - Reactive Maintenance4HI - Proactive Maintenance | This is the main end-to-end business process. Resource requests are derived from this process. |

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BH1 - Corrective MaintenanceBH2 - Emergency MaintenanceBJ2 - Preventive Maintenance4HH - Reactive Maintenance4HI - Proactive Maintenance4VT - Improvement Maintenance4WM - Operational and Overhead Maintenance | This is the main end-to-end business process. Resource requests are coming from this process. |

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
> Flagged while digesting this document, not verified: Internal inconsistency on prerequisite scope items: Business Conditions lists BH1, BH2, 4HH, 4HI, 4VT, 4WM (no BJ2), while Preceding Processes lists BH1, BH2, BJ2, 4HH, 4HI (no 4VT or 4WM); Succeeding Processes lists all seven including BJ2, 4VT and 4WM.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[14-maintenance-service-and-projects/zweck-stammdatenskript-instandhaltungsarbeitsplatz-anlegen-sds-5mh-460]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/43R_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 34,977 chars in the whole document
