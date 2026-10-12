---
id: 13-quality-ehs-and-compliance/nonconformance-management-2qn-ae-test-script-sap-s-4hana-cloud-public
title: "Nonconformance Management (2QN_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2QN_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud test script for scope item 2QN_AE: record, process (notification/8D), analyze, close defects; manual inspection lots and usage decisions."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/internal-quality-problems]
aliases: [2QN_S4CLD2608_BPD_EN_AE]
keywords: [Quality Management of Internal Problems, nonconformance management, defect recording, production defects, quality notifications, quality tasks, 8d problem solving, defect completion, defect analysis, manual inspection lots]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QN_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-851
topic: 13-quality-ehs-and-compliance/internal-quality-problems
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Nonconformance Management (2QN_AE) - Test Script, SAP S/4HANA Cloud Public Edition (2QN_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QN_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Quality Management of Internal Problems** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Nonconformance Management (2QN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849921)

[2 Prerequisites 4](#_Toc232849922)

[2.1 System Access 4](#_Toc232849923)

[2.2 Roles 4](#_Toc232849924)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232849925)

[2.4 Business Conditions 5](#_Toc232849926)

[3 Overview Table 6](#_Toc232849927)

[4 Test Procedures 8](#_Toc232849928)

[4.1 Manage Defects 8](#_Toc232849929)

[4.1.1 Record Defect 8](#_Toc232849930)

[4.1.2 Process Defect 10](#_Toc232849931)

[4.1.2.1 Process Defect via Quality Notification 10](#_Toc232849932)

[4.1.2.1.1 Process Defect and Define Quality Task 10](#_Toc232849933)

[4.1.2.1.2 Processor Receives the Notification 11](#_Toc232849934)

[4.1.2.1.3 Execute Quality Task and Document Outcome 12](#_Toc232849935)

[4.1.2.2 Process Defect via Eight Disciplines of Problem Solving (8D) 13](#_Toc232849936)

[4.1.3 Complete Defect Processing 17](#_Toc232849937)

[4.1.4 Record Defect Using CoPilot (Optional) 18](#_Toc232849938)

[4.1.5 Assign Defect to Quality Notification (Optional) 19](#_Toc232849939)

[4.2 Analyze Defects (Optional) 20](#_Toc232849940)

[4.3 Overview Page for Quality Engineer (Optional) 22](#_Toc232849941)

[4.4 Manual Inspection Process 23](#_Toc232849942)

[4.4.1 Create Inspection Lot 23](#_Toc232849943)

[4.4.2 Record Inspection Results 24](#_Toc232849944)

[4.4.3 Make Usage Decision 27](#_Toc232849945)

## Purpose

Overview

This scope item describes the management of defects and nonconformances. The quality technician creates a defect record and if necessary, adds a picture that documents the defect. The quality engineer further processes the defect record by documenting or defining immediate, corrective, and preventive actions. The quality technician executes the defined actions and confirms processing by setting a respective status. After defect resolution, the quality engineer closes the defect record.

In addition to general defect category, a new defect category is introduced which can be used to handle defects that occur during production. That is, the assignment of production order, material, plant, and defective quantity has been enabled.

Furthermore, the quality engineer monitors and analyzes defect records from various sources (for example, defects detected during quality inspection or manually created defects) and deduces common preventive actions.

If necessary, the quality technician creates additional, manual inspection lots for the available inspection origins to perform additional quality inspections. After inspection results are captured, the quality engineer makes a usage decision to close the manual inspection process.

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
| Quality Technician | SAP_BR_QUALITY_TECHNICIAN | Quality Inspection | SAP_BR_QUALITY_TECHNICIAN |  |
| Quality Engineer | SAP_BR_QUALITY_ENGINEER | Quality Engineering | SAP_BR_QUALITY_ENGINEER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Defect code Group | DEF-SURF | Surface |  |
| Defect code | 0001 | Dirty |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BNQ - Create Quality Inspection Plan - MDS | If you want to use self-defined actions and task codes, please refer to Chapter Characteristic Attributes - Edit Code Groups for Selected Sets in BNQ with catalog 2 and/or 8. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

|  |
| --- |
| Note There are two kinds of defect categories (Generic and Production). Select the appropriate app depending on the defect category you want to create. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Defects](#unique_8) [page ] 8 |  |  |  |
| [Record Defect](#unique_9) [page ] 8 | Quality Technician | Record Production Defect (F2929) |  |
| [Process Defect](#unique_10) [page ] 10 |  |  |  |
| Process Defect via Quality Notification |  |  |  |
| [Process Defect and Define Quality Task](#unique_11) [page ] 10 | Quality Engineer | Process Defects (F8046) | Defect is in process. |
| [Processor Receives the Notification](#unique_12) [page ] 11 | Quality Engineer | My Inbox (F0862) |  |
| [Execute Quality Task and Document Outcome](#unique_13) [page ] 12 | Quality Engineer | Process Quality Tasks (F3250) | The task is updated. |
| [Process Defect via Eight Disciplines of Problem Solving (8D)](#unique_14) [page ] 13 | Quality Engineer | Process Defects (F8046) |  |
| [Complete Defect Processing](#unique_15) [page ] 17 | Quality Engineer | Process Defects (F8046) | Defect is completed. |
| [Record Defect Using CoPilot (Optional)](#unique_16) [page ] 18 | Quality Engineer | Record Defects with SAP CoPilot (F2987) | Defect is created. |
| [Assign Defect to Quality Notification (Optional)](#unique_17) [page ] 19 | Quality Engineer | Manage Defects (F2649) | Defect is assigned to quality notification. |
| [Analyze Defects (Optional)](#unique_18) [page ] 20 | Quality Engineer | Manage Defects (F2649) | Defect is analyzed. |
| [Overview Page for Quality Engineer (Optional)](#unique_19) [page ] 22 | Quality Engineer | Quality Engineer Overview (F2360) | Defect is viewed via overview page. |
| [Create Inspection Lot](#unique_20) [page ] 23 | Quality Technician | Manage Inspection Lots (F2343) | Inspection lot is created. |
| [Record Inspection Results](#unique_21) [page ] 24 | Quality Technician | Record Inspection Results (F1685A) | Inspection result is recorded. |
| [Make Usage Decision](#unique_22) [page ] 27 | Quality Engineer | Manage Usage Decisions (F2345) | The usage decision is saved and the manual quality inspection is completed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Defects

|  |
| --- |
| Note Based on the embedded predictive analytics model, a Quality Technician can get proposals for defect codes based on the defect description and detailed description. Refer to Predictive Analytics Model Training – Supply Chain (20N) scope item for more details on the predictive model training and activation. |

Purpose

In this step, you can continue processing of a defect in a quality notification (notification type Q3 – Internal Problem Notification) in order to enable a more comprehensive processing of the defect. In addition the light defect and task management described in the previous steps, definition of immediate, corrective, and preventive actions as well as the assignment of one or more root causes to the defect is possible in the quality notification.

Note that it is currently only possible to continue the defect in a quality notification if no tasks have been assigned to the defect, yet.

#### Record Defect

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create the generic or production defect in this step.

Procedure

Table 1: For Generic Defect

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Defect (F2929). | The Defect screen displays. |  |
| 3 | Maintain Defect Data | Make the following entries and choose Create.Description: <enter short description>, for example, Surface is dirtyDefect Detailed Description: <enter long description>Defect Code Group: DEF-SURFDefect Code: 0001 dirtyReference Number: <enter a reference number>Optionally, attach a picture that documents the defect. | The defect is saved.Note down the defect number. |  |

Procedure

Table 2: For Production Defect

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Technician. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Record Production Defect (F2929). | The Defect screen displays. |  |
| 3 | Maintain Defect Data | Make the following entries and choose Create.Description: <enter short description>, for example, Wrong Parts/ComponentsDetailed Description: <enter long description>Defect Code Group: DEF-PACKDefect Code: 0004 Wrong Parts / ComponentsReference Number: <enter a reference number>You can either maintain production operation or production order number.Production Order Operation: <enter production order operation>When you enter values by using the value help for Production Order Operation field for all other fields, some values shall be determined by the system: production order, material (if order has some material assigned), plant, quantity, quanitity unit of measure, workcenter, workcenter plantPlant shall be taken from production orderQuantity shall be "1"Production Order Number: <enter production order>When you select some production order, for the following fields some values shall be derived:Material is taken from the production order (if there is some assigned)Plant shall be taken from production orderQuantity shall be "1"Optionally, attach a picture that documents the defect. | The production defect is saved.Note down the defect number. |  |

|  |
| --- |
| Note Subsequent steps for generic / production defect remains the same. |

#### Process Defect

There are two options for processing and completing a defect:

1. via Notifications or
2. via Eight Disciplines of Problem Solving (8D)

##### Process Defect via Quality Notification

###### Process Defect and Define Quality Task

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality engineer further processes the defect. He can add additional information to the defect or complete missing fields. Furthermore, he assigns a quality task to the defect and enters a responsible task processor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Process Defects (F8046). | The Process Defects screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Go.Defect Number: <the defect number noted down in previous step>Select the defect created. | The defect is displayed. |  |
| 4 | Edit the Defect | Choose Edit.In the Detailed Description field, enter additional information (for example, defect analysis). | Detailed description is maintained. |  |
| 5 | Add Quality Task | In the section Tasks, choose Add (+ button on the upper right of the table) to add a new task.Maintain the following fields:Description: Corrective ActionTask Processor: <User ID>Choose Save to save the task. | Task is added to the defect and released for processing. |  |
| 6 | Set Defect Status (Optional) | Go back to Defect. In the upper right corner, choose Set in Process. |  |  |
| 7 | Save the Defect | Choose Save. | The defect is saved with status In Process. |  |

###### Processor Receives the Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to receive a notification of task assigned to you in the My Inbox - All Items (F0862).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Check for Notification | Choose the notification in the notification section. | Notification displays. |  |
| 3 | Choose the Notification | Choose any one of the notifications to navigate to the My Inbox (F0862) app. | Task displays. |  |
| 4 | Open Quality Task | Choose Open Task to navigate to Task object page. | The Quality Task page displays. |  |

|  |
| --- |
| Note If the task processor changes, the respective notification is also transferred from one user to another. Also when the task is completed, the respective task is removed from the worklist of the processor. |

###### Execute Quality Task and Document Outcome

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the task processor opens the task and documents the task’s outcome in the processor notes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log onto the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2. | Access the App | Open Process Quality Tasks (F3250). | The Process Quality Tasks (Original) screen is displayed. |  |
| 3. | Enter Selection Fields | Make the following entries and choose Go: Task Processor: User ID | Results are displayed in the result table. |  |
| 4. | Open Quality Task | In the result table Quality Tasks, choose the task created in the previous step. | The defect and the assigned quality task are opened. |  |
| 5. | Maintain Task Data | Choose Edit.Maintain Processor Notes. | Processor notes are added to the task. |  |
| 6. | Save the Task | Choose Save. | The task is updated. |  |

##### Process Defect via Eight Disciplines of Problem Solving (8D)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The eight disciplines (8D) model is a problem solving approach. Its purpose is to identify, correct, and eliminate recurring problems. In this step, the quality engineer is guided through the 8 process steps of the 8D model.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Process Defects (F8046). | The Process Defects screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Go:Defect Number: <the defect number noted down in previous step>Select the defect created. | The defect displays. |  |
| 4 | Start new Problem-Solving Process | Choose Start Problem-Solving Process. | A new problem-solving process is created and a new section Problem-Solving Process is added to the process defects page of your current defect.Note The Start Problem-Solving Process button is only visible when in display mode. If it does not appear directly in the toolbar, then it can be found by opening the overflow menu. |  |
| 5 | Navigate to problem-solving process | Navigate to section Problem-Solving Process of the Defect screen and select the link representing the ID and description of the generated problem solving process. | The Problem-Solving Process screen (F4197) displays with the list of available process steps D1, …,D8. |  |
| 6 | Edit Problem-Solving | Choose Edit. |  |  |
| 7 | Step D1: Define Team | Choose D1 Team from the Problem-Solving Steps listed. Choose Add on the D1 Teams screen and enter the desired team members by making the following entries:Partner: <Business Partner ID>Partner Role: <8D Team Leader or 8D Team member>Choose Apply to conclude this process step. | On the right hand side of your screen, the D1 Team screen displays. |  |
| 8 | Step D2: Problem Description | Choose D2 Problem Description from the Problem-Solving Steps listed. On the D2 Problem Description screen, the Problem Description can be amended as required.Choose Apply to conclude this process step. | On the right hand side of your screen, the D2 Problem Description screen displays. |  |
| 9 | Step D3: Containment Actions | Choose D3 Containment Actions from the Problem-Solving Steps listed. On the D3 Containment Actions screen, choose Create to define required Quality Tasks. Make the following entries and choose Save:Task Processor: <User ID>Task Code: <respective task Code>, for example, <0003>Task Code Group: <respective task code group>, for example, <QM-TASK>Description: <a short description>Planned End Date: <planned end date>Use the Back Navigation (less-than symbol on the top left corner of the Process Quality Tasks screen) to move back to the of the D3 Containment Actions screen.Once you have created all required quality tasks, choose Apply to conclude this process step. | On the right hand side of your screen the D3 Containment Actions screen displays.The Process Quality Tasks (F3250) app displays when choose Create. |  |
| 10 | Step D4: Root Cases | Choose D4 Root Causes from the Problem-Solving Steps listed. On the D4 Root Causes screen, choose Create to define the root causes.Make the following entries:Cause Code: <respective cause code>, for example, <0010>Cause Code Group: <respective cause code group>, for example, <QM-CAU>Choose the greater-than symbol, located to the right of each Cause Description field, and enter the following information on the Description screen:Cause Description: <a short description>Detailed Description: <a detailed description>Choose Apply and close the Description screen to get back to the D4 Root Causes screen. Once you have created the root causes, choose Apply to conclude this process step.Choose Save from the Resolve Internal Problems screen.Switch back to edit mode by choosing Edit. | On the right hand side of your screen, the D4 Root Causes screen displays. |  |
| 11 | Step D5: Defined Corrective Actions | Choose D5 Defined Corrective Actions from the Problem-Solving Steps listed. The list of root cases entered at process step 4 are shown on the D5 Defined Corrective Actions screen. Choose the Show More per Row icon to display more details, and choose Create Task, which is located on the right side of each root-cause listing, to define required Quality Tasks.Make the following entries and choose Save:Task Processor: <User ID>Task Code: <respective task Code>, for example, <0003>Task Code Group: <respective task code group>, for example, <QM-TASK>Description: <a short description>Planned End Date: <planned end date>Use the Back Navigation (less-than symbol on the top left corner of the Process Quality Tasks screen) to move back to the of the D5 Defined Corrective Actions screen.Note You can create several Quality Tasks per cause in the Tasks section of the D5 Defined Corrective Actions screen where the list of defined quality tasks is shown. To implement the defined quality tasks, choose the radio button in front of the task and choose Implement. You can only implement one Quality Task at the time.Choose Close to confirm the popup.Once you have created and implemented all required quality tasks, choose Apply to conclude this process step. | On the right hand side of your screen, the D5 Defined Corrective Actions screen displays.The Process Quality Tasks (F3250) app displays when choose Create.When choose Impement, a dialog box appears showing the following success messages:Task <ID of task you marked> completed. Quality task <ID of new task now implementing your tasks> created as successor for quality task <ID of task you marked>. |  |
| 12 | Step D6: Implemented Corrective Actions | Choose D6 Implemented Corrective Actionsfrom the Problem-Solving Steps listed. The list of Quality Tasks, which were entered and implemented at process step D5, are shown on the D6 Implemented Corrective Actions screen.By choosing the Task ID of the quality task in the table you can navigate to Manage Quality Tasks (F3381) app which allows you to display and manage quality tasks. Actions such as, assign processor, change status, change planned end date, and enter notes for processor can be performed.Use Process Qualtiy Task (F3250) app to review and amend the quality tasks.Use the Back Navigation (less-than symbol on the top left corner of the Manage Quality Tasks or Qualtiy Task screen) to move back to the D6 Implemented Corrective Actions screen.Once you create and implement the corrective actions, choose Apply to conclude this process step. | On the right hand side of your screen D6 Implemented Corrective Actions screen displays.The Process Quality Task (F3250) app displays when choosing Edit. |  |
| 13 | Step D7: Preventive Actions | Choose D7 Preventive Actions from the Problem-Solving Steps listed. Choose Create to define required quality tasks.Make the following entries and choose Save:Task Processor: <User ID>Task Code: <respective task code>, for example, <0003>Task Code Group: <respective task code group>, for example, <QM-TASK>Description: <a short description>Planned End Date: <planned end date>Once you create and implement the corrective actions, choose Apply to conclude this process step.Use the Back Navigation (less-than symbol on the top left corner of the Process Quality Tasks screen) to move back to the of the D7 Preventive Actions screen.Once you create the preventive actions, choose Apply to conclude this process step. | On the right hand side of your screen D7 Corrective Actions screen displays.The Process Quality Task (F3250) app displays when choose Create. |  |
| 14 | Step D8: Congratulate Your Team | Choose D8 Congratulate Your Team from the Problem-Solving Steps listed. The D8 Congratulate Your Team screen provides a Detailed Description field that can be used to document lessons learned, as well as recognition and communication to the members of the problem resoving team.Choose Apply to conclude this process step.Choose Save to conclude the 8D process. |  |  |

#### Complete Defect Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality engineer reviews the outcome of the quality task and completes the defect.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Process Defects (F8046). | The Display Defects screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries and choose Go.Defect Number: <the defect number noted down in previous step>.Select the defect. | The defect is displayed. |  |
| 4 | Edit the Defect and Verify Quality Task | Check Processor Notes of quality task.Choose Complete. | Defect status is changed. |  |
| 5 | Save the Defect | Choose Save. | The defect is saved with status Completed. |  |
| 6 | Defect Mass Status Change (Optional) | Return to the worklist and select several defects. Choose one of the actions Complete, Set in Process, or Set to Not Relevant to trigger a status change for the selected defects. | Defect status values are changed (if allowed by lifecycle). |  |

#### Record Defect Using CoPilot (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can record the defect.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open CoPilot from the right top of the screen.. | The CoPilot dialog displays. |  |
| 3 | Create Chat | In the Chat tab, choose New Chat to create a new chat. | The chat is displayed. |  |
| 4 | Create Object | Choose Create New Object. In the New Object page, choose Record Defect. Enter the following entries:Description: Dirty surfaceDefect Code: 0001 dirtyNote You can use the F4 help button and filter Code Group, for example, DEF-SURF.Detailed Discrition: <enter detailed discription on the defect>Choose Create. | A new defect is created. Note down the defect number.Note You can also take a screen shot with the defect and invite participants to share this defect. |  |

#### Assign Defect to Quality Notification (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can continue processing of a defect in a quality notification (notification type Q3 - Internal Problem Notification) in order to enable a more comprehensive processing of the defect. In addition the the light defect and task management described in the previous steps, definition of immediate, corrective, and preventive actions as well as the assignment of one or more root causes to the defect is possible in the quality notification.

Note that it is currently only possible to continue the defect in a quality notification if no tasks have been assigned to the defect, yet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Defects (F2649). | The screen Manage Defects (Original) is displayed. |  |
| 3 | Continue Defect in Quality Notification | Select a defect line item that has no task assigned and choose Continue in Notification button.Write down the notification ID: __________________________ | A new notification (notification type Q3 - Internal Problem Notification) with one defect item is created. The selected defect corresponds to the defect item of the quality notification. |  |
| 4 | Navigate to Quality Notification and Maintain Additional Data | Choose Display Notification to navigate to the notification object.Choose More > Notification > Change from the menu bar to open the Change Notification app. On the initial screen, choose button Notification to open the quality notification in change mode.Maintain the quality notification header. Navigate to tab Subject and maintain the following data:Coordinator: <User ID>Choose Save. | Quality notification is saved. |  |
| 5 | Process Quality Notification (Optional) | Refer to scope item Quality Management of Internal Problems (2QP) for a detailed description of the following steps:Define, execute, and review root cause analysisDocument immediate actions on notification header and/or defect levelDefine, execute, and review corrective and/or preventive actions |  |  |
| 6 | Complete the Quality Notification | Refer to scope item Quality Management of Internal Problems (2QP) for a detailed description of the following step:Complete quality notification | Notification status is updated and quality notification is saved. |  |

### Analyze Defects (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality engineer can analyze defects that have been captured in the system. See also Scope Item SAP Fiori Analytical Apps for Quality Management for a more comprehensive explanation of this app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Defects (F2649). | The Manage Defects screen displays. |  |
| 3 | Enter Selection Fields | Make the following entries.Defect Category: for example, Generic DefectCreated on: for example, from the beginning of the year to today. | The selected defects are displayed.Note You can also maintain other criteria for the select of defects such as inspection lot origin, defect code, etc.Note For the criteria Defect Category, please note that defects created via CoPilot and app Record Defect are assigned to the defect category General Defect. If a defect was created automatically during results recording, the defect would be assigned to category Inspection Characterisitic or Inspection Point Characteristic.By default, defects are displayed in a chart and table view. You can adjust the layout with the buttons listed and select the chart type as line chart, pie chart, etc. |  |
| 4 | Select the Defect in the Chart View | Select defect entries in the chart. | In the table view, only the selected defect(s) will be displayed. |  |
| 5 | Select the Defect in the Table View | Select a defect in the table. Choose Details at the end of the line. | The defect details are displayed. |  |
| 6 | Go back to the app | Choose Back. | The Manage Defects screen displays. You can navigate other defects with different criteria. |  |

### Overview Page for Quality Engineer (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Quality Engineer Overview shows in a single page the most important information and tasks related to inspection management that are relevant for you right now. The information is displayed on set of cards. See also Scope Item Scope Item SAP Fiori Analytical Apps for Quality Management for a more comprehensive explanation of this overview page.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open app Quality Engineer Overview (F2360). | The Quality Engineer Overview screen displays. |  |
| 3 | Access the Card (Optional) | Access the card Top Defective Materials.Go back to Quality Engineer Overview. | The top defective materials are displayed. By clicking the card, you can see the information in Manage Defects view. |  |
| 4 | Access the Card (Optional) | Access the card Top Defects.Go back to Quality Engineer Overview. | The top defective codes are displayed. By clicking the card, you can see the information in Manage Defects view. |  |
| 5 | Access the Card (Optional) | Access the card Inspection Lots with Defects.Go back to Quality Engineer Overview. | The defects by inspection lot origin are displayed. By clicking the card, you can see the information in Manage Defects view. |  |
| 6 | Access the Card (Optional) | Access the card Quality Tasks by Date or Quality Tasks by Processor.Go back to Quality Engineer Overview. | A list of tasks is displayed in the Manage Quality Tasks app. |  |

### Manual Inspection Process

Purpose

This process describes the handling of inspection lots that were created manually. If required, the quality technician creates additional, manual inspection lots for the available inspection origins in order to perform additional quality inspections. After inspection results have been captured, the quality engineer makes a usage decision to close the manual inspection process.

#### Create Inspection Lot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the quality technician manually creates an inspection lot. An inspection plan is assigned and the sample size is calculated automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Inspection Lots (F2343) and choose Create Inspection Lot (+ button on the upper right of the Inspection Lotstable). | The Create Inspection Lot Manually: Initial screen displays. |  |
| 3 | Maintain Data on Initial Screen | Make the following entries and choose Continue:Material (Original) : QM001Plant: 3310Inspection Lot Origin: 89 | The Create Inspection Lot Manually: Origin screen displays. |  |
| 4 | Enter Quantity | In the Origin tab, make the following entry and choose Enter.Inspection Lot Quantity: 100 | The Inspection lot quantity is recorded, the inspection plan is assigned and the sample size is calculated |  |
| 5 | Check Assigned Inspection Plan and Sample Size (optional) | In the Inspection Specifications tab check the assigned specifications.In the Sample tab, check the sample size. | The inspection plan is assigned to the inspection lot. The sample size is 10% of the lot size |  |
| 6 | Save the Inspection Lot | Choose Save. | Manual inspection lot is created.Write down inspection lot ID:__________________________________ |  |

#### Record Inspection Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The quality engineer records inspection results.

Procedure

Record Inspection Results for one Inspection Lot

If inspection results shall be recorded for one or only a few inspection lots, execute the following process flow:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results (F1685A). | The Record Inspection Results screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go.Lot Origin: Miscellaneous (89) | The inspection lots displays. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot created in the previous step. Choose Record Multiple Results in the bottom right. | The inspection lot opens. |  |
| 5 | Enter Inspection Result | Depending on the inspection result, select one of the following two options:Positive ResultSurface Code Group - Code: SURFACE 0020 (Smooth)Length Mean Value (cm): 160Negative ResultSurface: Code Group - Code SURFACE 0010 (Rough)Length Mean Value (cm): 90Enter a <negative result>.In case of error (notification type or update of infostructure) see details in configuration guide. | For qualitative characteristic ( Surface) the search help is needed to select a value. For the quantitative characteristic ( Length) a number can be entered directly.The default number of inspected objects is calculated based on the sample size reviewed in an earlier step. The number of inspected objects can be manually changed. As well a number of nonconforming objects can be maintained directly in the respective fields for every inspection characteristic. |  |
| 6 | Save Inspection Lot | Choose Save. | The inspection lot is saved. |  |

Optional: Process-Optimized Results Recording for Multiple Inspection Lots

If inspection results shall be recorded for several inspection lots at the same time, execute the following process flow.

|  |
| --- |
| Caution Note that this app can only be used for quality inspections with master inspection characteristics. It is not possible to capture inspection results for inspections with plan characteristics. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Quality Technician. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Record Inspection Results in Table Form (F3365). | The Record Inspection Results in Table Form screen displays. |  |
| 3 | Enter Filter Fields | Maintain filter values and choose Go. | A list of inspection lots is displayed. |  |
| 4 | Select Inspection Lots and Inspection Characteristics | Select the inspection lots for which inspection results shall be recorded and choose Record Multiple Results.In the dialogue Select Characteristics for Result Recording, select the master inspection characteristics for which inspection results shall be recorded and choose button OK. | The Record Inspection Results in Table Form screen displays.Note The system creates one table line item per inspection lot operation. Each master inspection characteristic is displayed in a separate column. The valuation of the inspection characteristic is displayed in a separate adjacent column. If a master inspection characteristic is assigned to another inspection operation, the respective table field is grayed out. |  |
| 5 | Show Inspection Details (Optional) | Click one inspection characteristic in the table and choose Show Details. | The side panel opens and detailed inspection data are displayed (e.g. inspection specifications, master inspection characteristic, inspection method, test equipment, and inspection remarks). |  |
| 6 | Show Work Center (Optional) | Choose Settings button in the upper right corner of the table. In the Define Colunm Properties dialogue box, select Work Center and choose OK. | An additional Work Center column is displayed. |  |
| 7 | Enter Inspection Results | Enter inspection results. See above for example data. | For qualitative results, a corresponding value help is provided. Quantitative inspection results can be entered directly.Note Depending on the defined valuation mode (check inspection method details), the valuation is either done automatically by the system or must be done manually by the user.If a inspection result requires an inspection remark (check master inspection characteristic settings), it is not possible to navigate to the next inspection result. Open Details side panel and maintain the inspection remark in section Remarks. |  |
| 8 | Save Inspection Data | Choose Save. | Inspection results are saved and a success message is displayed. |  |

#### Make Usage Decision

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The inspection is done and the inspection result is recorded. You must decide whether or not to accept the assembly depending on the inspection result. If you do not want to use the Quality Engineer Overview, you can open the Manage Usage Decisions (F2345)s app directly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Usage Decisions (F2345). | The Manage Usage Decisions (Original) screen displays. |  |
| 3 | Enter Filter Fields | Make the following entries and choose Go:Inspection Lot Origin: Miscellaneous | Results display. |  |
| 4 | Select the Corresponding Inspection Lot | In the inspection lot list, select the inspection lot created above. | The inspection lot is opened. |  |
| 5 | Enter UD code | Choose Edit. In the Usage Decisionsection, depending on the inspection result, select one of the following two options.Positive ResultUD code: A (Accepted)Negative ResultUD code: R (Rejected) | The usage decision is recorded. |  |
| 6 | Add Attachment to the Inspection Lot (Optional) | In the Document section choose Add, select the path and add the document. |  |  |
| 7 | Save Usage Decision | Choose Save. | The usage decision is saved and the manual quality inspection is completed. |  |

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
> Flagged while digesting this document, not verified: Record Inspection Results purpose says the quality engineer records results, but the overview table and test step 1 use the Quality Technician role.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Purpose says the quality technician executes the defined actions and sets the status, but the Execute Quality Task steps and the overview table assign this to the Quality Engineer (Process Quality Tasks F3250).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-quality-management-of-internal-problems-2qp-ae-sap-s-4hana]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QN_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 48,647 chars in the whole document
