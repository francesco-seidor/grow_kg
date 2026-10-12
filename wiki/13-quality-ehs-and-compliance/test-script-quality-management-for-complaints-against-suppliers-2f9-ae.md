---
id: 13-quality-ehs-and-compliance/test-script-quality-management-for-complaints-against-suppliers-2f9-ae
title: "Test Script: Quality Management for Complaints Against Suppliers (2F9_AE) (2F9_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 (AE) test script for scope item 2F9: supplier complaint quality notifications (QM01/QM02/QM12) and optional complaints (F8685)."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/complaint-quality-notifications]
aliases: [2F9_S4CLD2608_BPD_EN_AE]
keywords: [Quality Notifications for Customer and Supplier Complaints, complaints against suppliers, quality notifications, defect capture, quality notification tasks, supplier root cause analysis, complaint processing, return purchase orders, test scripts, test prerequisites]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F9_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-822
topic: 13-quality-ehs-and-compliance/complaint-quality-notifications
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Quality Management for Complaints Against Suppliers (2F9_AE) (2F9_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F9_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Quality Notifications for Customer and Supplier Complaints** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Quality Management for Complaints Against Suppliers (2F9_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232849476)

[2 Prerequisites 4](#_Toc232849477)

[2.1 System Access 4](#_Toc232849478)

[2.2 Roles 4](#_Toc232849479)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232849480)

[2.4 Business Conditions 5](#_Toc232849481)

[2.5 Preliminary Steps 6](#_Toc232849482)

[3 Overview Table 7](#_Toc232849483)

[4 Test Procedures 8](#_Toc232849484)

[4.1 QM Notification for Complaints Against Suppliers 8](#_Toc232849485)

[4.1.1 Create Quality Notification with Basic Data 8](#_Toc232849486)

[4.1.2 Capture Defects and Document Immediate Actions 10](#_Toc232849487)

[4.1.3 Define Tasks 11](#_Toc232849488)

[4.1.4 Execute Tasks and Document Outcome 12](#_Toc232849489)

[4.1.5 Review Tasks 14](#_Toc232849490)

[4.1.6 Document Supplier Root Cause Analysis 15](#_Toc232849491)

[4.1.7 Complete Notification 16](#_Toc232849492)

[4.1.8 Display a List of Quality Notifications (optional) 17](#_Toc232849493)

[4.1.9 Display a List of Quality Notification Tasks (optional) 18](#_Toc232849494)

[4.2 QM Complaint Processing for Complaints Against Suppliers (Optional) 19](#_Toc232849495)

[4.2.1 Create a Complaint (Optional) 19](#_Toc232849496)

[4.2.2 Add Defects to a Complaint (Optional) 20](#_Toc232849497)

[4.2.3 Send a Complaint Report to Supplier (Optional) 21](#_Toc232849498)

[4.2.4 Create a Return Purchase Order (Optional) 22](#_Toc232849499)

## Purpose

Overview

This scope item describes the management of complaints against suppliers, such as after delivery of a product.

Leveraging quality notifications, the quality engineer captures all complaint-related information including the observed defects. The quality engineer enters immediate actions for documentation purposes and requests a root cause analysis from the supplier. Furthermore, the quality engineer can keep a record of his communication with the supplier.

Leveraging the new nonconformance management business object Complaint against Supplier, the quality engineer records the complaint basic data, maintains the involved roles, assigns existing defects, and initiates logistical follow-up actions such as creating a returns purchase order — directly within the process flow. The system facilitates seamless communication with the supplier by generating a detailed complaint report to request formal feedback. Finally, the quality engineer reviews the findings, monitors the status of the complaint, and completes the process, ensuring full transparency from initial defect identification to final resolution.

The quality engineer defines tasks either globally at notification level or per defect. The quality engineer assigns one processor to each task. The task is processed, and task processors give feedback per task. After the quality engineer receives the supplier's root cause analysis, identified root causes can be assigned to each defect.

Finally, the quality engineer reviews each task and closes the notification.

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
| Company Code | 3310 | Company Code 3310 |  |
| Purchasing Organization | 3310 | Purch. Org. 3310 |  |
| Supplier | 33300006 | Domestic UAE Supplier 6 |  |
| Material | QM001 | QM Regular |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNQ | Create Quality Inspection Plan - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | To run through this scope item, it must be possible to purchase materials. Prerequisite for 2F9 Quality Management for Complaints Against Suppliers is that the scope item J45 is active and available in the system. |
| BNQ - Create Quality Inspection Plan - MDS | If you want to use self-defined actions and task codes, please refer to Chapter Characteristic Attributes - Edit Code Groups for Selected Sets in BNQ with catalog 2 and/or 8. |

### Preliminary Steps

To run through this scope item, a purchase order is required. Please refer to the scope item Procurement of Direct Materials - J45 (AE) to create a purchase order.

|  |
| --- |
| Note Issue reports can only be generated and sent to suppliers if the prerequisite BRF+ configuration is already made. See [Output Management for Complaints Against Suppliers](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d1e58be39d884a0dbf75a7526a9acbf4/cfcbd3c0938340f9bc5285cf08d6cbb8.html) for more details. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| QM Notification for Complaints Against Suppliers |  |  |  |
| [Create Quality Notification with Basic Data](#unique_9) [page ] 8 | Quality Engineer | Create Quality Notification (QM01) | Quality notification is created. |
| [Capture Defects and Document Immediate Actions](#unique_10) [page ] 10 | Quality Engineer | Change Quality Notification (QM02) | Defects are captured and documented. |
| [Define Tasks](#unique_11) [page ] 11 | Quality Engineer | Change Quality Notification (QM02) | Tasks are defined and released. |
| [Execute Tasks and Document Outcome](#unique_12) [page ] 12 | Quality Engineer | Change Quality Notification Tasks - Worklist (QM12) | Tasks are executed, and outcome is documented. |
| [Review Tasks](#unique_13) [page ] 14 | Quality Engineer | Change Quality Notification (QM02) | Tasks feedback is reviewed. |
| [Document Supplier Root Cause Analysis](#unique_14) [page ] 15 | Quality Engineer | Change Quality Notification (QM02) | Supplier root cause analysis is documented. |
| [Complete Notification](#unique_15) [page ] 16 | Quality Engineer | Change Quality Notification (QM02) | Notification is completed. |
| [Display a List of Quality Notifications (optional)](#unique_16) [page ] 17 | Quality Engineer | Display Quality Notification Tasks - Worklist (QM13) | Notifications are displayed. |
| [Display a List of Quality Notification Tasks (optional)](#unique_17) [page ] 18 | Quality Engineer | Display Quality Notification Tasks - Worklist (QM13) | Tasks are displayed. |
| [QM Complaint Processing for Complaints Against Suppliers (Optional)](#unique_18) [page ] 19 |  |  |  |
| [Create a Complaint (Optional)](#unique_19) [page ] 19 | Quality Engineer | Manage Complaints Against Suppliers (F8685) | A complaint is created. |
| [Add Defects to a Complaint (Optional)](#unique_20) [page ] 20 | Quality Engineer | Manage Complaints Against Suppliers (F8685) | Defects are added to the complaint. |
| [Send a Complaint Report to Supplier (Optional)](#unique_21) [page ] 21 | Quality Engineer | Manage Complaints Against Suppliers (F8685) | A complaint report is created. |
| [Create a Return Purchase Order (Optional)](#unique_22) [page ] 22 | Quality Engineer | Manage Complaints Against Suppliers (F8685) | A return purchase order is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### QM Notification for Complaints Against Suppliers

#### Create Quality Notification with Basic Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a quality notification of complaint against supplier and capture the most important data. Processing of the notification is started by setting a corresponding lifecycle status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Quality Notification (QM01). | The Create Notification: Initial Screen displays. |  |
| 3 | Create the Notification | Make the following entries and choose Notification.Notification Type: Q2In the dialogue box Create Notification: Initial Screen, enter the following data and choose Continue.Purchasing Document: purchase order and purchase order item | The Create Notification: Complaints ag. Suppl. screen displays.By entering material document and/or purchasing document, related data will be automatically transferred to the notification. |  |
| 4 | Enter Notification Data | In the Reference Object part under the Reference Objects tab, make the following entries:Material: <Material Number>, for example, QM001Plant for Material: 3310In the Contact Person part under the Reference Objects tab, make the following entries:Supplier: <Supplier Number>In the DMS Links part under the Reference Objects tab, you can attach a document by choosing + or click Create Document.In the Subject part under the Subject tab, make the following entries:Coding: for example, QM-COD (Problem Details); 0001 (Logistical issue)Description: for example, Delivery issueLong text: enter the short text to describe the complaint, for example, delivered product damagedIn the Execution part, on the Subject tab, make the following entriesPriority: select a priorityRequired Start: todayRequired End: today + 30 daysCoordinator: enter the coordinatorIn the Quantities part, on the Subject tab, make the following entries:Complaint Qty: number of defect itemsRef. Quantity: number of delivered itemsOn the Dates/Times tab, you can check the Notification Date created automatically as today's date. Enter your name in the filed Reported By. You can also edit Start/End Dates of the notification.If required, select Goto > Partner in the application menu to navigate to the Partners screen and add additional partner functions and partner IDs (e.g. Interested Party). After having completed partner maintenance, navigate back.Change notification status by choosing Put in Process. | Required start and end date are changed according the selected priority after pressing Enter.Quantities are copied from the referenced purchase order at the creation of the notification. |  |
| 5 | Save Notification | Choose Save to save the notification.Write down notification number: ____________________ | Notification is saved and notification ID is generated. |  |

#### Capture Defects and Document Immediate Actions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, defects are documented using code groups and codes for defect type. Furthermore, immediate actions on defect or notification level are entered for documentation purposes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Quality Engineer. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entries and choose Notification:Notification: notification ID | The Change Notification: Complaint ag. Suppl. displays. |  |
| 4 | Update the Notification | To capture defects, navigate to the tab Items and maintain defects in the Overview table:Code Group-Code Group Problem: for example, DEF-FUNC Functional DefectsDefect type: 0010 No functionText: Impossible to switch on the deviceItem long text: Long textDefectiveQty (External) / DefectiveQty (Internal): 1 pcTo document immediate actions per defect, select a defect item in the Overview table and navigate to tab Activities on the Items tab. In the table Activities for Item, make the following entries to document in immediate action:Code Group- Activity : for example, QM-ACT General ActivityActivity Code: for example, 0001 Immediate ActivityActivity Text: Supplier informed by mailLong Text: Supplier informed by mail. Detailed investigation report requested. Broken device was sent to supplier.Start Date: todayEnd Date: todayOptional: Document an additional immediate/corrective action, e.g. Documentation of stock transfer posting from unrestricted to quality inspection or blocked stock.Optional: To document immediate actions on complaint level, use tab Activities on header level. | Note The system might issue a warning if task dates do not lie within the notification dates.Note In order to keep track of the communication between supplier and quality engineer, corresponding predefined activities can be added to the notification and further information documented in the long text of each activity.Note Activities on defect level do not have a status and action responsible. To define actions with status and action responsible on defect level, see tab Tasks. |  |
| 5 | Save the Notification | Choose the Save button to save the notification | Notification is saved. |  |

#### Define Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, tasks on notification and/or defect level are created, assigned to responsible processors and released for processing. Note that tasks can be used to capture corrections, corrective, and preventive actions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entries and choose Notification:Notification: notification ID |  |  |
| 4 | Create and Release Tasks on Notification Level | Navigate to tab Tasks and make the following entries to define a task on notification level:Code Group- Task: for example, QM-TASK tasksTask code: for example, 0003 Preventive taskTask Text: Adapt goods receipt inspectionResponsible: responsible user namePlanned Start Date: todayPlanned End: today + 1 daySelect the corresponding entry and press button Release below the table to release the task. | A corrective/preventive action has been defined as a task on notification level. The action has been released for processing.Note The system might issue a warning if action dates do not lie within the notification dates. |  |
| 5 | Create and Release Tasks on Defect Level | Navigate to tab Items and select a defect item.Navigate to tab Tasks on tab Items and make the following entries to define a task on defect level:Code Group: for example, QM-TASK tasksTask code: for example, 0003 - Preventive taskTask Text: Adapt goods receipt inspectionResponsible: responsible user namePlanned Start Date: todayPlanned End: today + 1 daySelect the corresponding entry and press button Release below the table to release the task.Optional: To define a task on notification level, use tab tasks on header level. | A corrective/preventive action has been defined as a task on defect item level. The action has been released for processing.Note The system might issue a warning if action dates do not lie within the notification dates. |  |
| 6 | Save the Tasks | Choose Save button. | Notification is saved. The status is updated to Outstanding task(s) exist(s). |  |

#### Execute Tasks and Document Outcome

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Quality Notification Tasks - Worklist (QM12). | The Change Tasks: Selection of Notifications displays. |  |
| 3 | Enter Selection Parameters | On the selection screen, different search parameters can be specified to retrieve a list of tasks.Make the following entries and choose Execute:Person responsible for task: user name | Note The selection criteria include notification and task data.Note From the worklist, it is also possible to jump to the respective notification by selecting the task and choosing button Notification. |  |
| 4 | Open the Task | In the Change tasks: List of notifications, select one of the tasks defined above and choose the button Task in the top. | Task opens. |  |
| 5 | Update the Task | In the Task area, input the feedback in the long text field.Expand the Planning area, make the following entries:Completed On: todayBy: user nameChoose Complete Task. | Note The fields Completed on and By are automatically filled at status change.Note By choosing button Notification, a notification summary is displayed. |  |
| 6 | Process other Tasks | Repeat steps 4 and 5 (optional) for other tasks. |  |  |
| 7 | Save | Choose Save. | Data is saved. |  |

#### Review Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, completed tasks are reviewed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entries and choose Notification:Notification: notification ID |  |  |
| 4 | Update the Task on Notification Level | Navigate to tab Tasks on notification level. Select one task line item and choose button Successful located below the tasks table. |  |  |
| 5 | Update the Task on Defect Item Level | Navigate to tab Items. Select one defect item and navigate to tab Tasks on defect item level. Select one task line item and choose button Successful located below the tasks table. |  |  |
| 6 | Process Other Tasks | Repeat steps 4 and 5 (optional) for other tasks. |  |  |
| 7 | Save | Choose Save. | Notification is saved.Note The system indicates via a system status if all tasks of the notification are completed. |  |

#### Document Supplier Root Cause Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the mean time, a detailed supplier error analysis (e.g. in the form of an 8D report) arrived. The corresponding information is also added to the notification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Quality Notification (QM02). | The Change Notification: Initial screen displays. |  |
| 3 | Choose the Notification | Make the following entries and choose Notification:Notification: notification ID |  |  |
| 4 | Document Supplier Root Cause Analysis | Navigate to tab Items and select one defect item. Navigate to tab Causes and enter the root cause communicated by the supplier:Code Group- Cause: for example, QM-CAU (Problem Causes, Defect Causes)Code: for example, 0016 (Material Defect)Cause Text: Supplier Info: Short circuit | Root cause information is maintained.Note Corrective and preventive actions defined by the supplier could also be transferred for documentation purposes. |  |
| 5 | Save | Choose Save. | Notification is saved. |  |

#### Complete Notification

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
| 5 | Close the Notification | Choose Complete.In the window Close, maintain the following fields and choose Continue to close the notification:Completion Date: todayCompletion Time: nowNotification: Internal Origin or External Origin | Notification status is updated and saved.Note Completion Date and Completion Time are automatically filled. |  |

#### Display a List of Quality Notifications (optional)

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Quality Notifications - Worklist (QM11). | The initial selection screen displays. |  |
| 3 | Enter Selection Parameters | Make the following entries and choose Execute:Material: <Material Number> for example, QM001 | Note Different selection parameters (notification status, date, partners, code group and code) can be entered.Note The value selected in the field Ref. Field Monitor determines whether the traffic light is calculated using the notification priority or notification date.A list of quality notifications matching the specified selection criteria displays. |  |
| 4 | Access Individual Notification Information | Select one quality notification in the result list and choose Notification to display all notification details.Choose Back to return to the worklist.Select one quality notification in the result list and choose Long Text to display the notification long text.Choose Back to return to the worklist. | Detailed notification information shows. |  |

#### Display a List of Quality Notification Tasks (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you can get a list of tasks, for example, tasks that a specific user is responsible for, tasks for a department, tasks that are connected to a certain material.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Quality Notification Tasks - Worklist (QM13). | The initial selection screen displays. |  |
| 3 | Enter Selection Parameters | Make the following entry and choose Execute:Person Responsible: user name | Note Different selection parameters with respect to task and notification (for example, notification and task status, date, partners, code group and code) can be entered.The value selected in the field Ref. Field Monitor determines whether the traffic light is calculated using the notification priority or task dates.A list of tasks matching the specified selection criteria displays. |  |
| 4 | Access Individual Task Information | Select one task in the result list and choose button Task to display all task details.Choose Back to return to the worklist.Select one task in the result list and choose Long Text to display the task long text.Choose Back to return to the worklist.Select one task in the result list and choose button Notification to display the related quality notification.Choose Back to return to the worklist. | Detailed task and notification data shows. |  |

### QM Complaint Processing for Complaints Against Suppliers (Optional)

A complaint against a supplier is an object in quality management. It relates to the delivery of goods or services by a supplier or manufacturer. It is raised by the receiver in the case of a nonconformance, for example, when items are damaged or deviate from specifications, standards, or expectations.

The overall goals of a complaint against a supplier are to document and resolve the raised issues, improve future performance, and maintain constructive business relationships. This process helps both parties reach a mutual agreement on a satisfactory resolution that addresses the issues raised.

#### Create a Complaint (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a complaint against supplier and assign responsible external and internal roles to your complaint.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad is displays. |  |
| 2 | Access the App | Open Manage Complaints Against Suppliers (F8685). | The Manage Complaints Against Suppliers displays. |  |
| 3 | Create a Complaint | Choose Create.Make the following entry:Complaint Description: for example, Late Delivery | The New Complaint page displays. |  |
| 4 | Add Internal/External Roles to the Complaint | Choose tab Roles, and choose External Roles.Make the following entries:Partner Function: for example, SupplierBusiness Partner: for example, 10100006Under tab Roles, choose Internal Roles.Make the following entries:Partner Function: for example, CoordinatorUser ID: for example, Quality EngineerChoose Create. | By entering the complaint description and saving the complaint, a complaint number is generated in the upper left corner.Note down the complaint number. |  |

#### Add Defects to a Complaint (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you add inspected defects to the complaint created from previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Complaints Against Suppliers (F8685). | The Manage Complaints Against Suppliers: Initial Screen displays. |  |
| 3 | Find the Complaint | Make the following entries:Complaint: XXXXX(Created from last step)Choose Go.Choose the arrow icon (Details icon) at the end of the row to view more details. | The complaint details are displayed on the New Object page. |  |
| 4 | Add Defects to the Complaint | Choose Edit and navigate to the Defects tab.Enter the Defect number generated from previous inspection activites.Choose Save. | The defects are added to the complaint. |  |
| 5 | Check Complaint Items Information (Optional) | Choose the Items tab. | Information such as Material and Item Quantity should be copied and updated from the Defects after the complaint is saved. |  |

#### Send a Complaint Report to Supplier (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you send a complaint report based on the complaint created from the previous step.

|  |
| --- |
| Note Issue reports can only be generated and sent to suppliers if the prerequisite BRF+ configuration is already made. See [Output Management for Complaints Against Suppliers](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d1e58be39d884a0dbf75a7526a9acbf4/cfcbd3c0938340f9bc5285cf08d6cbb8.html) for more details. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Complaints Against Suppliers (F8685). | The Manage Complaints Against Suppliers screen displays. |  |
| 3 | Find the Complaint | Make the following entry:Complaint: XXXXX(Created from last step)Choose Go.Choose the arrow icon Details at the end of the row. | The complaint gets displayed. |  |
| 4 | Change Complaint Status | Choose Edit first and then choose Set In Process. | The complaint status is set as In Process. |  |
| 5 | Send Issue Report to Supplier | Choose the Output Items tab.Choose Determine.Select one of the output items with output channel, such as Email, and choose Send. | The system generates a PDF version of the issue report for different output channels with status In Preparation, which is based on the pre-configured BRF+ settings.A corresponding issue report with detailed defects information is sent to the responsible supplier for further processing.The status for the sent item changes from In Preparation to Completed. |  |

#### Create a Return Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a return purchase order based on the complaint created in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Quality Engineer. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Complaints Against Suppliers (F8685). | The Manage Complaints Against Suppliers screen displays. |  |
| 3 | Find the Complaint | Make the following entry:Complaint: XXXXX (Created from last step)Choose Go.Choose the arrow icon Details at the end of the row. | The complaint gets displayed. |  |
| 4 | Input Return Purchase Order Data | Choose Edit.Choose the Items tab.Make the following entries for the defective material that needs to be returned to the supplier:Return Quantity: The number of items to be returnedStorage Location: The storage locationChoose the Additional Data tab.Make the following entries:Purchasing Doc. Type: Standard PO (NB)Purchasing Group: Group 001 (001)Purchasing Organization: 3310Company Code: 3310Choose Create Return and Save. | The complaint is saved with a newly generated purchase order number on tab Additional Data. |  |
| 5 | Close the Complaint | Choose Complete. | The complaint status changes from In Process to Completed. |  |

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
> Flagged while digesting this document, not verified: Overview Table lists 'Display a List of Quality Notifications (optional)' under app QM13 (Display Quality Notification Tasks - Worklist), but the procedure for that step opens QM11 (Display Quality Notifications - Worklist).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/quality-management-for-complaints-from-customers-2fa-ae-test-script-sa]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2F9_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 40,812 chars in the whole document
