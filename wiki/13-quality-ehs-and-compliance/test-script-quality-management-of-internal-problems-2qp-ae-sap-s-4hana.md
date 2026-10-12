---
id: 13-quality-ehs-and-compliance/test-script-quality-management-of-internal-problems-2qp-ae-sap-s-4hana
title: "Test Script: Quality Management of Internal Problems (2QP_AE) - SAP S/4HANA Cloud Public Edition (2QP_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 2QP_AE: internal quality notifications, root cause analysis, corrective/preventive actions, closure (QM01/QM02/QM12)."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/internal-quality-problems]
aliases: [2QP_S4CLD2608_BPD_EN_AE]
keywords: [Quality Management of Internal Problems, quality notifications, internal problems, root cause analysis, corrective actions, preventive actions, defect capture, notification tasks, notification completion, notification worklists]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QP_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-852
topic: 13-quality-ehs-and-compliance/internal-quality-problems
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Quality Management of Internal Problems (2QP_AE) - SAP S/4HANA Cloud Public Edition (2QP_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QP_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Quality Management of Internal Problems** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Quality Management of Internal Problems (2QP_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232849803)

[2 Prerequisites 3](#_Toc232849804)

[2.1 System Access 3](#_Toc232849805)

[2.2 Roles 3](#_Toc232849806)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232849807)

[2.4 Business Conditions 4](#_Toc232849808)

[2.5 Preliminary Steps 4](#_Toc232849809)

[3 Overview Table 5](#_Toc232849810)

[4 Test Procedures 7](#_Toc232849811)

[4.1 Create Quality Notification with Basic Data 7](#_Toc232849812)

[4.2 Capture Defects, Define Root Cause Analysis, and Document Immediate Actions 8](#_Toc232849813)

[4.3 Define Corrective Actions 10](#_Toc232849814)

[4.4 Execute Root Cause Analysis and Corrective Actions, and Document Outcome 11](#_Toc232849815)

[4.5 Review Root Cause Analysis and Document Root Cause, Review Corrective Actions 13](#_Toc232849816)

[4.6 Define Preventive Actions 14](#_Toc232849817)

[4.7 Execute Preventive Actions and Document Outcome 14](#_Toc232849818)

[4.8 Review Preventive Actions 15](#_Toc232849819)

[4.9 Complete Quality Notification 15](#_Toc232849820)

[4.10 Display a List of Quality Notifications (Optional) 16](#_Toc232849821)

[4.11 Display a List of Quality Notification Tasks (Optional) 17](#_Toc232849822)

## Purpose

Overview

This scope item describes the management of internal problems, for example, deviations observed during production or storage of goods.

Leveraging quality notifications, the quality engineer can capture all problem-related information. Further immediate actions can be captured for documentation purposes. To identify the root cause of the complaint, the quality engineer starts a root cause analysis. After having identified the error and the related root cause, the quality engineer classifies this information using code groups, codes, and free text information.

The quality engineer defines corrective and preventive actions either globally at notification level or per defect. The quality engineer assigns one processor to each action. The action is processed and action processors give feedback per action.

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

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Plant | 3310 | Plant 1 AE |  |
| Material | QM001 | QM Regular |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNQ | Create Quality Inspection Plan - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BMC - Core Inventory Management | Complete all steps in the test script. |
| BNY - Create Quality Management Attributes for Material/Product Master - MDS | Complete all steps in the master data script for inspection type 08. |

### Preliminary Steps

To run through this scope item, the materials must be available in stock. Please refer to preliminary steps of 1MR to complete this process.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Quality Notification with Basic Data](#unique_9) [page ] 7 | Quality Engineer | Create Quality Notification (QM01) | A quality notification is created. |
| [Capture Defects, Define Root Cause Analysis, and Document Immediate Actions](#unique_10) [page ] 8 | Quality Engineer | Change Quality Notification (QM02) | Defects are captured, root cause analysis is defined and immediate actions are documented. |
| [Define Corrective Actions](#unique_11) [page ] 10 | Quality Engineer | Change Quality Notification (QM02) | Corrective actions and correction tasks are defined. |
| [Execute Root Cause Analysis and Corrective Actions, and Document Outcome](#unique_12) [page ] 11 | Quality Engineer | Change Quality Notification Tasks - Worklist (QM12) | Root cause analysis, corrective actions, correction tasks are executed and documented. |
| [Review Root Cause Analysis and Document Root Cause, Review Corrective Actions](#unique_13) [page ] 13 | Quality Engineer | Change Quality Notification (QM02) | Root cause analysis, corrective actions and correction tasks are reviewed and documented. |
| [Define Preventive Actions](#unique_14) [page ] 14 | Quality Engineer | Change Quality Notification (QM02) | Preventive actions are defined. |
| [Execute Preventive Actions and Document Outcome](#unique_15) [page ] 14 | Quality Engineer | Change Quality Notification Tasks - Worklist (QM12) | Preventive actions are executed and documented. |
| [Review Preventive Actions](#unique_16) [page ] 15 | Quality Engineer | Change Quality Notification (QM02) | Preventive actions are reviewed. |
| [Complete Quality Notification](#unique_17) [page ] 15 | Quality Engineer | Change Quality Notification (QM02) | Notification is completed. |
| [Display a List of Quality Notifications (Optional)](#unique_18) [page ] 16 | Quality Engineer | Display Quality Notifications - Worklist (QM11) | A list of quality notifications is displayed. |
| [Display a List of Quality Notification Tasks (Optional)](#unique_19) [page ] 17 | Quality Engineer | Display Quality Notification Tasks - Worklist (QM13) | A list of notification tasks is displayed. |

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

In this process step, you create an internal quality notification and capture the most important data. Processing of the notification is started by setting a corresponding lifecycle status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Quality Notification (QM01). | The Create Notification: Initial screen displays. |  |
| 3 | Create the Notification | Make the following entries and choose Notification:Notification Type: Q3 | A new quality notification of internal problem is created in status Notification in process. |  |
| 4 | Enter Notification Data | In the Reference Object section under the Reference Objects tab, make the following entries:Material: <Material Number>, for example, QM001Plant for Material: 3310In the Author Address section of the Reference Objects tab, you can check author details.In the Linked Documents section of the Reference Objects tab, you can attach documents (Type: SQM) by choosing + or choosing Create Document.In the Execution section under the Subject tab, make the following entries:Priority: <select a priority>, for example, mediumRequired Start: <today>Required End: <today + 30 days>Coordinator: <coordinator user name>In the Subject section of the Subject tab, make the following entries:Coding: <QM-COD(Problem Details)>; <0004(Storage Issue)>Description: <Issue in warehouse>Long Text: <long text to describe the issue>On the Dates/Times tab, you can check the Notification Date created automatically as today's date. Enter your name in the Reported By field. You can also edit Start/End Dates of the notification.(Optional) Choose Menu > Goto > Partner to navigate to the Partners screen and add additional partner functions and partner IDs (e.g. Interested Party). After completing partner maintenance, navigate back.Change notification status by choosing Put in Process. | Required start and required end date are changed according the selected priority after choosing enter button. |  |
| 5 | Save Notification | Choose Save. | Notification is saved and notification ID is generated.Notification ID: ______. |  |

### Capture Defects, Define Root Cause Analysis, and Document Immediate Actions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, a root cause analysis is triggerered and defects are maintained. Furthermore, immediate actions (e.g. defect containment actions or defect mitigation actions) are documented.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entries and choose Notification:Notification: notification ID |  |  |
| 4 | Update the Notification | a) To define a root cause analysis, navigate to the tab Tasks and make the following entries:Code Group: for example, QM-TASKTask Code: for example, 0004 - Root Cause AnalysisTask Text: Root cause analysisResponsible: responsible user namePlanned Start Date: todayPlanned End: today +2 daysRelease activity by selecting the corresponding entry and pressing button Release below the table.b) To capture defects, navigate to the tab Items and maintain defects in the Overview table:Code Group: DEF-LOC (Defect location)Defect loc.: 0003 (Outside)Code Group: DEF-SURF Surface DefectsDefect type: 0003 ScratchedText: Scratches ~ 3 mmItem long text: Long textDefectiveQty (external) / DefectiveQty (internal): 1 pcc) To document immediate actions on notification level, navigate to tab Activities and make the following entries:Code Group: for example, QM-ACTActivity Code: for example, 0001 - Immediate ActivityActivity Text: Stock moved to quality inspection stockStart Date: todayEnd Date: todayLongtext: For example, ID of respective inspection lotOptionally, the inspection lot number can also be maintained on the header level of the notification (Tab Reference Objects, section Reference Documents):Reference No: Document ID of inpsection Lotd) (Optional) To document immediate actions on defect level, navigate to tab Items and select the respective defect line item. Then navigate to tab Item Activities and enter an immediate action as described in paragraph c). | a) A root cause analysis is defined as task on notification level and released.The system might issue a warning if task dates do not lie within the notification dates.b) Defects are added to the notification.c and d) Immediate actions are added on notification(c) or defect level(d).Note Item activities on defect level do not have a status and action responsible. To define actions with status and action responsible on defect level, see tab Item Tasks.Note Activities on notification level do not have a status and action responsible. To define actions with status and action responsible, see tab Tasks.Note To document an inspection lot ID, a stock transfer inspection lot is required.Please refer to scope item 1MR for a detailed process description. |  |
| 5 | Save the Notification | Choose Save. | Notification is saved. The status is updated to outstanding task exists. |  |

### Define Corrective Actions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, corrective actions on notification and on defect level are created, assigned to responsible processors and released for processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entries and choose Notification:Notification: notification ID |  |  |
| 4 | Create and Release Corrective Action | Navigate to tab Tasks and make the following entries to define a corrective action on notification level:Code Group: for example, QM-TASKTask code: for example, 0001 - Corrective taskTask Text: Rework surfaceResponsible: responsible user namePlanned Start Date: todayPlanned End: today + 1 daySelect the corresponding entry and press button Release below the table to release the corrective action. | A corrective action has been defined as a task on notification level. The action has been released for processing.Note The system might issue a warning if action dates do not lie within the notification dates. |  |
| 5 | Create and Release Correction Action on Defect Level | Navigate to tab Items and select a defect item.Navigate to tab Item Tasks on Tab Items and make the following entries to define a correction task on defect level:Code Group: for example, QM-TASKTask code: for example, 0001 - Corrective taskTask Text: Rework surfaceResponsible: responsible user namePlanned Start Date: todayPlanned End: today + 1 dayRelease correction task by selecting the corresponding entry and pressing button Release below the table. | A correction action has been defined on defect item level. The action has been released for processing.Note The system might issue a warning if task dates do not lie within the notification dates. |  |
| 6 | Save the Notification | Choose Save. | Notification is saved. The status is updated to outstanding task exists. |  |

### Execute Root Cause Analysis and Corrective Actions, and Document Outcome

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Change Quality Notification Tasks - Worklist (QM12). | The Change Tasks: Selection of Notifications displays. |  |
| 3 | Enter Selection Parameters | On the selection screen, different search parameters can be specified to retrieve a list of tasks.Make the following entries and choose Execute:Person responsible for task: user name | A list of tasks assigned to the responsible user displays.Note Note that the selection criteria include notification and task data.Note From the worklist, it is also possible to jump to the respective notification by selecting the task and choosing button Notification. |  |
| 4 | Open Root Cause Analysis Task | In the Change tasks: List of notifications, select the root cause analysis defined above and choose the button Task in the top. | Root cause analysis opens. |  |
| 5 | Update the Task | In the Task area, input the feedback in the long text field.Expand the Planning area, make the following entries:Completed On: todayBy: user nameChoose button Complete Task. | Status of the task changes to task completed. Fields are read-only.Note The fields Completed on and By are automatically filled at status change.Note By choosing button Notification, a notification summary is displayed.Note It is also possible to assign causes to defects in a systematic manner. A detailed description is provided in the next step. |  |
| 6 | Save the Task | Choose Save. | Data is saved. |  |
| 7 | Process Other Tasks | Process the corrective actions defined in the previous step in a similar way. |  |  |

### Review Root Cause Analysis and Document Root Cause, Review Corrective Actions

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entries and choose Notification:Notification: notification ID |  |  |
| 4 | Review Root Cause Analysis | Navigate to tab Tasks and open the root cause analysis by a double click on the respective line item.Display task long text by choosing the button Text right to the field Task Text.Choose back and close Task Detail pop up. | Task long text is displayed. |  |
| 5 | Mark Root Cause Analysis Successful (Optional) | Select the root cause analysis line item and choose button Successful located below the tasks table. | Task status changes to successful.Note If root cause analysis is not successful, a new task must be defined. |  |
| 6 | Enter Root Causes for Item | It is also possible to maintain root causes per item leveraging code groups and codes. Navigate to tab Items. Select one defect item in the Overview list and navigate to tab Causes in the tab Items. Make the tollowing entries:Code Group: QM-CAU (Problem Causes, Defect Causes)Cause code: 0012 (Human / Training or Awareness)Cause text: Scratches due to incorrect handling | A cause is assigned to the defect. |  |
| 7 | Process Other Tasks | Process steps 4 and 5 (optional) for the remainder corrective actions. |  |  |
| 8 | Save | Choose Save. | Data is saved.Note The system indicates via a system status if all tasks of the notification are completed. |  |

### Define Preventive Actions

Purpose

In this process step, preventive actions on notification and defect level are created, assigned to responsible processors and released for processing.

Procedure

Execute the steps described in chapter Define Corrective Actions to define a preventive action on notification and defect level.

### Execute Preventive Actions and Document Outcome

Purpose

In this process step, the tasks that are assigned to a user with the role user responsible are displayed in a worklist. Feedback to tasks is entered and processing is finished by changing the task status.

Procedure

Execute the steps described in Chapter Execute Root Cause Analysis, Corrective Actions and Document Outcome to execute a preventive action.

### Review Preventive Actions

Purpose

In this process step, completed tasks are reviewed.

Procedure

Execute steps 1 through 5 and 8 described Chapter Review Root Cause Analysis and Document Root Cause, Review Corrective Actions to review preventive actions.

### Complete Quality Notification

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entries and choose Notification:Notification: notification ID |  |  |
| 4 | Review the Notification and All Related Objects | Navigate through all tabs and review the information. Check whether all tasks are at least in status completed. If not, change the task status accordingly or remove the task. | All tasks are in status completed. |  |
| 5 | Close the Notification | Choose Complete.In the window Close, maintain the following fields and choose Continue to close the Notification:Completion Date: todayCompletion Time: nowNotification: Internal Origin or External Origin | Notification status is updated and saved.Note Completion Date and Completion time are automatically filled. |  |

### Display a List of Quality Notifications (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Quality Notifications - Worklist (QM11). | The initial selection screen displays. |  |
| 3 | Enter Selection Parameters | Make the following entries and choose Execute:Material: QM001 | Note Different selection parameters (notification status, date, partners, code group and code) can be entered.Note The value selected in the field Ref. Field Monitor determines whether the traffic light is calculated using the notification priority or notification date.A list of quality notifications matching the specified selection criteria is displayed. |  |
| 4 | Access Individual Notification Information | Select one quality notification in the result list and choose button Notification to display all notification details.Choose Back to return to the worklist.Select one quality notification in the result list and choose button Long Text to display the notification longtext.Choose Back to return to the worklist. | Detailed notification information shows. |  |

### Display a List of Quality Notification Tasks (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can get a list of tasks, for example, tasks that a specific user is responsible for, tasks for a department and tasks that are connected to a certain material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
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
- related-to :: [[13-quality-ehs-and-compliance/nonconformance-management-2qn-ae-test-script-sap-s-4hana-cloud-public]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QP_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 31,992 chars in the whole document
