---
id: 13-quality-ehs-and-compliance/quality-management-for-complaints-from-customers-2fa-ae-test-script-sa
title: "Quality Management for Complaints from Customers (2FA_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2FA_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 2FA: customer complaint quality notifications, root cause, actions, closure."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/complaint-quality-notifications]
aliases: [2FA_S4CLD2608_BPD_EN_AE]
keywords: [Quality Notifications for Customer and Supplier Complaints, customer complaints, quality notifications, root cause analysis, corrective actions, preventive actions, notification tasks, test scripts, notification completion, notification worklists]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2FA_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-823
topic: 13-quality-ehs-and-compliance/complaint-quality-notifications
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Quality Management for Complaints from Customers (2FA_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2FA_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2FA_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Quality Notifications for Customer and Supplier Complaints** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Quality Management for Complaints from Customers (2FA_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232849358)

[2 Prerequisites 3](#_Toc232849359)

[2.1 System Access 3](#_Toc232849360)

[2.2 Roles 3](#_Toc232849361)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232849362)

[2.4 Business Conditions 4](#_Toc232849363)

[2.5 Preliminary Steps 4](#_Toc232849364)

[3 Overview Table 5](#_Toc232849365)

[4 Test Procedures 7](#_Toc232849366)

[4.1 Create Quality Notification with Basic Data 7](#_Toc232849367)

[4.2 Capture Defects, Define Root Cause Analysis, and Document Immediate Actions 8](#_Toc232849368)

[4.3 Define Corrective Actions and Correction Tasks 10](#_Toc232849369)

[4.4 Execute Root Cause Analysis, Corrective Actions, Correction Tasks and Document Outcome 11](#_Toc232849370)

[4.5 Review Root Cause Analysis and Document Root Cause, Review Corrective Actions and Correction Tasks 13](#_Toc232849371)

[4.6 Define Preventive Actions 14](#_Toc232849372)

[4.7 Execute Preventive Actions and Document Outcome 14](#_Toc232849373)

[4.8 Review Preventive Actions 15](#_Toc232849374)

[4.9 Complete Notification 15](#_Toc232849375)

[4.10 Display a List of Quality Notifications (optional) 16](#_Toc232849376)

[4.11 Display a List of Quality Notification Tasks (optional) 17](#_Toc232849377)

## Purpose

Overview

This scope item describes the management of customer complaints, for example, after delivery of a product. Using quality notifications, the quality engineer can capture all complaint-related information provided by the customer. The quality engineer enriches the notification by adding internal logistical information, such as delivery and purchase documents. Further immediate actions can be captured for documentation purposes. To identify the complaint's root cause, the engineer documents a root cause analysis. After having identified the error and the related root cause, the quality engineer classifies this information using code groups, codes, and free text information.

The quality engineer defines corrective and preventive actions either globally at notification level or per defect. The engineer assigns one processor to each action. The action is processed, and action processors give feedback per action.

Finally, the quality engineer reviews each action and closes the notification.

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
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure. Alternatively, you can refer to data from test script 1MP - Quality Management in Sales.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Company Code | 3310 | Company Code 3310 |  |
| Customer | 33100050 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNQ | Create Quality Inspection Plan - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met. Alternatively, you can refer to data from test script 1MP - Quality Management in Sales.

| Scope Item | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | To run through this scope item, the materials must be available in stock. If you use trading goods (HAWA) you can either:Run through the Procurement of Direct Materials (J45) processOr create stock using FLP tile Post Goods Movement (for details see section Preliminary Steps). |
| BNQ - Create Quality Inspection Plan - MDS | If you want to use self-defined actions and task codes, please refer to Chapter Characteristic Attributes - Edit Code Groups for Selected Sets in BNQ with catalog 2 and/or 8. |

### Preliminary Steps

To run through this scope item, a sales order and/or a delivery to customer are required.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Quality Notification with Basic Data](#unique_9) [page ] 7 | Quality Engineer | Create Quality Notification (QM01) | A quality notification is created. |
| [Capture Defects, Define Root Cause Analysis, and Document Immediate Actions](#unique_10) [page ] 8 | Quality Engineer | Change Quality Notification (QM02) | Defects are captured, root cause analysis is defined and immediate actions are documented. |
| [Define Corrective Actions and Correction Tasks](#unique_11) [page ] 10 | Quality Engineer | Change Quality Notification (QM02) | Corrective actions and correction tasks are defined. |
| [Execute Root Cause Analysis, Corrective Actions, Correction Tasks and Document Outcome](#unique_12) [page ] 11 | Quality Engineer | Change Quality Notification Tasks - Worklist (QM12) | Root cause analysis, corrective actions, correction tasks are executed and documented. |
| [Review Root Cause Analysis and Document Root Cause, Review Corrective Actions and Correction Tasks](#unique_13) [page ] 13 | Quality Engineer | Change Quality Notification (QM02) | Root cause analysis, corrective actions and correction tasks are reviewed and documented. |
| [Define Preventive Actions](#unique_14) [page ] 14 | Quality Engineer | Change Quality Notification (QM02) | Preventive actions are defined. |
| [Execute Preventive Actions and Document Outcome](#unique_15) [page ] 14 | Quality Engineer | Change Quality Notification Tasks - Worklist (QM12) | Preventive actions are executed and documented. |
| [Review Preventive Actions](#unique_16) [page ] 15 | Quality Engineer | Change Quality Notification (QM02) | Preventive actions are reviewed. |
| [Complete Notification](#unique_17) [page ] 15 | Quality Engineer | Change Quality Notification (QM02) | Notification is completed. |
| [Display a List of Quality Notifications (optional)](#unique_18) [page ] 16 | Quality Engineer | Display Quality Notifications - Worklist (QM11) | A list of quality notifications is displayed. |
| [Display a List of Quality Notification Tasks (optional)](#unique_19) [page ] 17 | Quality Engineer | Display Quality Notification Tasks - Worklist (QM13) | A list of notification tasks is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Quality Notification with Basic Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a customer complaint quality notification and capture the most important data. Processing of the notification is started by setting a corresponding lifecycle status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Quality Notification (QM01). | The Create Notification: Initial Screen displays. |  |
| 3 | Create the Notification | Make the following entries and choose Notification:Notification Type: Q1In the dialogue box Create Notification: Initial Screen, enter the following data and choose Continue:Sales Order: sales order and sales order itemDelivery: delivery and delivery item | A new quality notification of type customer plaint is created in status Notification in process.By entering sales order and/or delivery, related data will be automatically transferred to the notification. |  |
| 4 | Enter Notification Data | In the Reference Object section under the Reference Objects tab, make the following entries:Material: <Material Number>, for example, QM001Plant for Material: 3310In the Linked Documents section under the Reference Objects tab, you can attach documents by choosing + or clicking Create Document.In the Subject section under the Subject tab, make the following entries:Coding: for example,QM-COD (Problem Details); 0002(Product Complaint)Description: for example, Surface DamageLong text: enter the long text to describe the complaintIn the Execution section under the Subject tab, make the following entries:Priority: select a priorityRequired Start: todayRequired End: today + 30 daysCoordinator: enter the coordinatorOn the Dates/Times tab, you can check the Notification Date created automatically as today's date. Enter your name in the filed Reported By. You can also edit Start/End Dates of the notification.(Optional) Choose Menu > Goto > Partner to navigate to the Partners screen and add additional partner functions and partner IDs (e.g. Interested Party). After having completed partner maintenance, navigate back.Change notification status by choosing Put in Process. | Required start and required end date are changed according the selected priority after choosing enter button. |  |
| 5 | Save Notification | At the bottom of the page, choose Save. | Notification is saved and notification ID is generated. |  |

### Capture Defects, Define Root Cause Analysis, and Document Immediate Actions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, a root cause analysis is triggered, and defects are maintained. Furthermore, immediate actions on defect or notification level are entered for documentation purposes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entry and choose Notification:Notification: notification ID |  |  |
| 4 | Update the notification | To define a root cause analysis, navigate to the tab Tasks and make the following entries:Code Group: for example, QM-TASKTask Code: for example, 0004 - Root Cause AnalysisTask Text: Root cause analysisResponsible: responsible user namePlanned Start Date: todayPlanned End: today +2 daysRelease activity by selecting the corresponding entry and pressing button Release below the table.To capture defects, navigate to the tab Items and maintain defects in the Overview table:Code Group: DEF-LOC (Defect location)Defect loc.: 0003 (Outside)Code Group: DEF-SURF Surface DefectsDefect type: 0003 ScratchedText: Scratches ~ 3 mmItem long text: Long textDefectiveQty (external) / DefectiveQty (internal): 1 pcTo document immediate/corrective actions per defect, select a defect item in the Overview table and navigate to tab Correction Activities on the Items tab. In the table Activities for Item, make the following entries:Code Group: for example, QM-ACTActivity Code: for example, 0001 - Immediate ActivityActivity Text: Acknowledgment mail sent to customerStart Date: todayEnd Date: todayTo document immediate actions on notification level, navigate to tab Activities and make the following entries:Code Group: for example, QM-ACTActivity Code: for example, 0001 - Immediate ActivityActivity Text: Acknowledgment mail sent to customerStart Date: todayEnd Date: today | A root cause analysis is defined as task on notification level and released.Note Corrective actions on defect level do not have a status and action responsible. To define actions with status and action responsible on defect level, see tab Correction Tasks.The system might issue a warning if task dates do not lie within the notification dates.Defects are added to the notification.Immediate / corrective actions are added on notification or defect level.Note Activities on notification level do not have a status and action responsible. To define actions with status and action responsible, see tab Tasks. |  |
| 5 | Save the notification | Choose Save button. | Notification is saved. The status is updated to outstanding task exists. |  |

### Define Corrective Actions and Correction Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, corrective actions on notification level and correction tasks on defect level are created, assigned to responsible processors and released for processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Quality Engineer. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entries and choose Notification:Notification: notification ID |  |  |
| 4 | Create and release corrective action | Navigate to tab Tasks and make the following entries to define a corrective action on notification level:Code Group: for example, QM-TASKTask code: for example, 0001 - Corrective taskTask Text: Rework surfaceResponsible: responsible user namePlanned Start Date: todayPlanned End: today + 1 daySelect the corresponding entry and press button Release below the table to release the corrective action. | A corrective action has been defined as a task on notification level. The action has been released for processing.Note The system might issue a warning if action dates do not lie within the notification dates. |  |
| 5 | Create and release correction task on defect level | Navigate to tab Items and select a defect item.Navigate to tab Correction Tasks on Tab Items and make the following entries to define a correction task on defect level:Code Group: for example, QM-TASKTask code: for example, 0001 - Corrective taskTask Text: Rework surfaceResponsible: responsible user namePlanned Start Date: todayPlanned End: today + 1 dayRelease correction task by selecting the corresponding entry and pressing button Release below the table. | A correction task has been defined on defect item level. The task has been released for processing.Note The system might issue a warning if task dates do not lie within the notification dates. |  |
| 6 | Save the notification | Choose Save button. | Notification is saved. The status is updated to outstanding task exists. |  |

### Execute Root Cause Analysis, Corrective Actions, Correction Tasks and Document Outcome

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the tasks that are assigned to a user with the role user responsible are displayed in a worklist. Feedback to tasks is entered and processing is finished by changing the task status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Quality Engineer. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Quality Notification Tasks - Worklist (QM12). | The Change Tasks: Selection of Notifications displays. |  |
| 3 | Enter selection parameters | On the selection screen, different search parameters can be specified to retrieve a list of tasks.Make the following entries and choose Execute:Person responsible for task: user name | A list of tasks assigned to the responsible user displays.Note Note that the selection criteria include notification and task data.Note From the worklist, it is also possible to jump to the respective notification by selecting the task and choosing button Notification. |  |
| 4 | Open root cause analysis task | In the Change tasks: List of notifications, select the root cause analysis defined above and choose the button Task in the top. | Root cause analysis opens. |  |
| 5 | Update the task | In the Task area, input the feedback in the long text field.Expand the Planning area, make the following entries:Completed On: todayBy: user nameChoose button Complete Task. | Status of the task changes to task completed. Fields are read-only.Note The fields Completed on and By are automatically filled at status change.Note By choosing button Notification, a notification summary is displayed.Note It is also possible to assign causes to defects in a systematic manner. A detailed description is provided in the next step. |  |
| 6 | Save the task | Choose Save. | Data is saved. |  |
| 7 | Process other tasks | Process the corrective actions and correction tasks defined in the previous step in a similar way. |  |  |

### Review Root Cause Analysis and Document Root Cause, Review Corrective Actions and Correction Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, completed tasks are reviewed and the root cause identified in the root cause analysis is documented on defect item level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Quality Engineer. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entries and choose Execute:Notification: notification ID |  |  |
| 4 | Review root cause analysis | Navigate to tab Tasks and open the root cause analysis by a double click on the respective line item.Display task long text by choosing the button Text right to the field Task Text.Choose back and close Task Detail pop up. | Task long text is displayed. |  |
| 5 | Mark root cause analysis successful (Optional) | Select the root cause analysis line item and choose button Successful located below the tasks table. | Task status changes to successful.Note If root cause analysis is not successful, a new task must be defined. |  |
| 6 | Enter root causes for item | It is also possible to maintain root causes per item leveraging code groups and codes. Navigate to tab Items. Select one defect item in the Overview list and navigate to tab Causes in the tab Items. Make the tollowing entries:Code Group: QM-CAU (Problem Causes, Defect Causes)Cause code: 0012 (Human / Training or Awareness)Cause text: Scratches due to incorrect handling | A cause is assigned to the defect. |  |
| 7 | Process other tasks | Process steps 4 and 5 (optional) for the corrective actions and correction tasks. |  |  |
| 8 | Save | Choose Save. | Data is saved.Note The system indicates via a system status if all tasks of the notification are completed. |  |

### Define Preventive Actions

Purpose

In this process step, preventive actions on notification and defect level are created, assigned to responsible processors and released for processing.

Procedure

Execute the steps described in chapter Define Corrective Actions and Correction Tasks to define a preventive action on notification and defect level.

### Execute Preventive Actions and Document Outcome

Purpose

In this process step, the tasks that are assigned to a user with the role user responsible are displayed in a worklist. Feedback to tasks is entered and processing is finished by changing the task status.

Procedure

Execute the steps described in Chapter Execute Root Cause Analysis, Corrective Actions, Correction Tasks and Document Outcome to execute a preventive action.

### Review Preventive Actions

Purpose

In this process step, completed tasks are reviewed.

Procedure

Execute steps 1 through 5 and 8 described Chapter Review Root Cause Analysis and Document Root Cause, Review Corrective Actions and Correction Tasks to review preventive actions.

### Complete Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the notification and related objects are reviewed and the notification is closed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Quality Engineer. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entries and choose Execute:Notification: notification ID |  |  |
| 4 | Review the notification and all related objects | Navigate through all tabs and review the information. Check whether all tasks are at least in status completed. If not, change the task status accordingly or remove the task. | All tasks are in status completed. |  |
| 5 | Close the notification | Choose Complete.In the window Close, maintain the following fields and choose Continue to close the Notification:Completion Date: todayCompletion Time: nowNotification: Internal Origin or External Origin | Notification status is updated and saved.Note Completion Date and Completion time are automatically filled. |  |

### Display a List of Quality Notifications (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, a list of notifications with respect to a certain material is displayed in a worklist for overview purposes or management quality analysis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Quality Engineer. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Display Quality Notifications - Worklist (QM11). | The initial selection screen displays. |  |
| 3 | Enter selection parameters | Make the following entries and choose Execute:Material: QM001 | Note Different selection parameters (notification status, date, partners, code group and code) can be entered.Note The value selected in the field Ref. Field Monitor determines whether the traffic light is calculated using the notification priority or notification date.A list of quality notifications matching the specified selection criteria displays. |  |
| 4 | Access individual notification information | Select one quality notification in the result list and choose button Notification to display all notification details.Choose Back to return to the worklist.Select one quality notification in the result list and choose button Long Text to display the notification longtext.Choose Back to return to the worklist. | Detailed notification information shows. |  |

### Display a List of Quality Notification Tasks (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can get a list of tasks, for example, tasks that a specific user is responsible for, tasks for a department ans tasks that are connected to a certain material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Display Quality Notification Tasks - Worklist (QM13). | The initial selection screen displays. |  |
| 3 | Enter Selection Parameters | Make the following entries and choose Execute:Person responsible for task: user name | Note Different selection parameters with respect to task and notification (e.g. notification and task status, date, partners, code group and code) can be entered.Note The value selected in the field Ref. Field Monitor determines whether the traffic light is calculated using the notification priority or task dates.A list of tasks matching the specified selection criteria displays. |  |
| 4 | Access Individual Task Information | Select one task in the result list and choose button Task to display all task details.Choose Back to return to the worklist.Select one task in the result list and choose button Long Text to display the task longtext.Choose back to return to the worklist.Select one task in the result list and choose button Notification to display the related quality notification.Choose back to return to the worklist. | Detailed task and notification data shows. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/test-script-quality-management-for-complaints-against-suppliers-2f9-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2FA_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 32,802 chars in the whole document
