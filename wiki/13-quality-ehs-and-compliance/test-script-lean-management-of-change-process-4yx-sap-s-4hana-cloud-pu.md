---
id: 13-quality-ehs-and-compliance/test-script-lean-management-of-change-process-4yx-sap-s-4hana-cloud-pu
title: "Test Script: Lean Management of Change Process (4YX) - SAP S/4HANA Cloud Public Edition (4YX_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4YX, Lean Management of Change: change request lifecycle, analysis apps and change request type configuration."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/management-of-change]
aliases: [4YX_S4CLD2608_BPD_EN_XX]
keywords: [Lean Management of Change, management of change, change requests, change request approval, initial review, change activities, activity templates, change request types, change request closure, change analysis dashboards]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4YX_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1059
topic: 13-quality-ehs-and-compliance/management-of-change
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Lean Management of Change Process (4YX) - SAP S/4HANA Cloud Public Edition (4YX_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4YX_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Lean Management of Change** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Lean Management of Change Process (4YX) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232830226)

[2 Prerequisites 4](#_Toc232830227)

[2.1 System Access 4](#_Toc232830228)

[2.2 Roles 4](#_Toc232830229)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232830230)

[3 Overview Table 6](#_Toc232830231)

[4 Test Procedures 7](#_Toc232830232)

[4.1 Create a Change Request 7](#_Toc232830233)

[4.2 Carry Out an Initial Review 9](#_Toc232830234)

[4.3 Approve a Change Request 10](#_Toc232830235)

[4.4 Drive a Change Request and Perform Activities 12](#_Toc232830236)

[4.5 Close a Change Request 15](#_Toc232830237)

[4.6 Additional Process Steps (Optional) 16](#_Toc232830238)

[4.6.1 Perform Analysis 16](#_Toc232830239)

[4.6.1.1 Perform a Detailed Analysis of Change Requests and Activities 16](#_Toc232830240)

[4.6.1.2 Get an Overview of Change Requests 17](#_Toc232830241)

[4.6.1.3 Get an Overview of Change Activities 19](#_Toc232830242)

[5 Appendix 21](#_Toc232830243)

[5.1 Perform Activities 21](#_Toc232830244)

[5.1.1 Perform an Activity of Category “Task” 21](#_Toc232830245)

[5.1.2 Perform an Activity of Category “Approval” 22](#_Toc232830246)

[5.1.3 Perform an Activity of Category “Notification” 23](#_Toc232830247)

[5.2 Configure Your Solution 24](#_Toc232830248)

[5.2.1 Define Codes 24](#_Toc232830249)

[5.2.2 Define Catalogs and Code Groups 26](#_Toc232830250)

[5.2.3 Define Activity Templates 29](#_Toc232830251)

[5.2.4 Define Change Request Types 35](#_Toc232830252)

## Purpose

Overview

With this scope item, you can manage and streamline changes to products, procedures, processes, and equipment. You can also monitor and organize reviews, approvals, and other actions necessary to implement the change, such as updating documentation, training materials, or master data. Employees can easily communicate change requests. Based on standard templates, you can decrease implementation and adoption costs and ensure that the company-specific or industry-specific change procedures are followed.

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
| Change Management Coordinator | SAP_BR_CHG_MGMT_COORDINATOR | Management of Change | SAP_BR_CHG_MGMT_COORDINATOR |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 3SR | Create EHS Location - MDS |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create a Change Request](#unique_7) [page ] 7 | Change Management Coordinator | Create Change Request (/MOC/WDA_CHANGE_REQUEST) | A change request is created and submitted. The necessary information is provided, so that the persons responsible can decide if the change is applicable. |
| [Carry Out an Initial Review](#unique_8) [page ] 9 | Change Management Coordinator | Manage Change Requests (F3406) | The initial review of the change request that has been reported via the Create Change Request (/MOC/WDA_CHANGE_REQUEST) app is carried out. This includes checking the available information, collecting additional information, and involving experts. |
| [Approve a Change Request](#unique_9) [page ] 10 | Change Management Coordinator | Manage Change Requests (F3406) | The change request is approved. The change management coordinator can decide whether the change will be implemented based on his or her expertise and the information that has been maintained in the change request. |
| [Drive a Change Request and Perform Activities](#unique_10) [page ] 12 | Change Management Coordinator | Manage Change Requests (F3406)Manage Change Activities (F3405) | The change management coordinator has driven the completion of all assigned activities and they are performed by their owners or approvers. The approved change is implemented. After the change has been implemented and all activities have been completed, the coordinator closes the change request. |
| [Close a Change Request](#unique_11) [page ] 15 | Change Management Coordinator | Manage Change Requests (F3406) | The change management coordinator has checked if all activities are completed. The change request is closed. |
| [Perform a Detailed Analysis of Change Requests and Activities](#unique_12) [page ] 16 | Change Management Coordinator | Change Requests and Activities - Detailed Analysis (F5469) | The change management coordinator has performed a comprehensive analysis of the change requests and activities in the system by creating an analysis path. |
| [Get an Overview of Change Requests](#unique_13) [page ] 17 | Change Management Coordinator | Change Requests Dashboard (F5760) | The change management coordinator has performed an analysis and got an overview of the change requests in the system. |
| [Get an Overview of Change Activities](#unique_14) [page ] 19 | Change Management Coordinator | Change Activities Dashboard (F5761) | The change management coordinator has performed an analysis and got an overview of the change activities in the system. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create a Change Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A change request has to be reported and submitted in the system with basic information to help the persons responsible decide if the change is applicable.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Change Management Coordinator. |  |  |
| 2 | Access App | Open Create Change Request (/MOC/WDA_CHANGE_REQUEST). | The Change Request: New screen is displayed. |  |
| 3 | Choose a Change Request Type | On the entry screen of the Create Change Request app, choose MOC Change Request.Note You can create a custom change request type by following the test procedures in [Configure Your Solution](#unique_16) [page ] 24. | The Change Request 'MOC Change Request': New screen is displayed. |  |
| 4 | Enter Object Details | In the Object Information and Dates section, under Object, make the following entries:Type: EquipmentObject: Use the value help to select equipmentNote In the Search: Equipment dialog box, enter at least one search criteria to search for equipment. For example, under the By Plant tab, in the Plant field, enter 1010, and then select equipment from the search results.Location: Use the value help to select a locationNote Each change request must have a location assigned.You can find information on creating locations in the master data script 3SR (Create EHS Location). For more information, see [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 5.(Optional) Under Proposed Dates, make the following entry:Duration/Reversal: Permanent | The object details are populated in the Object Information and Dates section.In the References section, in the Related Objects table, an entry is created for the object of type Equipment that is marked as Leading Object.In the Related Locations table, an entry is created for the related object of type Location that is marked as Leading Object.Note In every change request, two related objects can be marked as leading: one of type Location, and one of the remaining related object types, such as Equipment. |  |
| 5 | Enter Change Definition Details | In the Change Definition section, make the following entries:Description: <Enter free text>(Optional) Impact: High(Optional) Detailed Description: <Enter free text>(Optional) Proposed Solution: <Enter free text> | The change definition details are populated in the Change Definition section. |  |
| 6 | Attach Files(Optional) | In the References section, under Attachments, choose Add File. In the Upload File dialog box, navigate to select the desired file, and choose OK. | The file is uploaded and added to the Attachments table. |  |
| 7 | Enter Analysis Details (Optional) | In the Initial Risk Analysis section, select the appropriate values for the initial risk assessment of an incident and add comments, if needed.In the Impact Analysis section, select the areas that are impacted by the change and add comments, if needed. | The analysis details are populated. |  |
| 8 | Add a Coordinator | In the People Involved section, select Coordinator in the Role column. In the Business Partner column, enter your business partner number or use the value help and search by your name. | The details are populated in the table for the Coordinator role. |  |
| 9 | Submit the Change Request | Choose Save and Submit in the bottom-right corner. | The change request status is changed to Submitted and the following success messages are displayed in the message popover:Data saved successfullyChange request <description> has been submitted for review |  |

### Carry Out an Initial Review

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The change management coordinator carries out an initial review of the change request to check the information available, collect additional information, and involve experts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Change Management Coordinator. |  |  |
| 2 | Access App | Open Manage Change Requests (F3406). | The Manage Change Requests screen is displayed. |  |
| 3 | Open a Change Request | Open the change request that you have just created in the previous process step.Note To find your change request easier, you can search for it by entering the description of the change request or part of it in the Search field. Alternatively, you can search by the following criteria:Status: SubmittedRole of the Person Involved: CoordinatorPerson Involved: <your user> | The Change Request 'MOC Change Request': < change request ID - description> screen is displayed, and the status of the change request is Submitted. |  |
| 4 | Check the Created Activities | Go to the Activities section and make sure that the following activities have been created with the needed subactivities:Initial ReviewEvaluation and ApprovalPre-ImplementationImplementationPost-ImplementationFollow-up and Closeout |  |  |
| 5 | Edit the Change Request | In the page header, choose Edit. Make changes, if needed. | The following buttons are displayed in the page header:Edit – inactiveReview CompleteResubmit (Incomplete)RejectNot applicableHold |  |
| 6 | Open the Review Change Request Subactivity | From the Activities section, choose Review Change Request to navigate to the activity. | The Activity 'Approval': <activity number>, Review Change Request screen is displayed. |  |
| 7 | Perform the Review Change Request Subactivity | To perform the Review Change Request subactivity, you can refer to the procedure described in [Perform an Activity of Category Approval](#unique_17) [page ] 22. | The status of the Review Change Request subactivity is changed to Approved. |  |
| 8 | Open the Initial Review Activity | From the Activities section, choose Initial Review to navigate to the activity. | The Activity 'Phase': <activity number>, Initial Review screen is displayed. |  |
| 9 | Perform the Initial Review Activity | To perform the Initial Review activity, you can refer to the procedure described in [Perform an Activity of Category Task](#unique_18) [page ] 21. | The status of the Initial Review activity is changed to Completed.The status of the change request is changed to Awaiting Approval.Note It is possible to set the status of the change request to Awaiting Approval manually. You can do so by choosing Review Complete from the page header in the change request. |  |

### Approve a Change Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The change management coordinator decides if the change will be implemented based on his or her expertise and the information that has been maintained in the change request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Change Management Coordinator. |  |  |
| 2 | Access App | Open Manage Change Requests (F3406). | The Manage Change Requests screen is displayed. |  |
| 3 | Open a Change Request | Search for the change request that you have created and open it.Note To find your change request easier, you can search for it by entering the description of the change request or part of it in the Search field. Alternatively, you can search by the following criteria:Status: Awaiting ApprovalRole of the Person Involved: CoordinatorPerson Involved: <your user> | The Change Request 'MOC Change Request': < change request ID - description> screen is displayed, and the status of the change request is Awaiting Approval. |  |
| 4 | Edit the Change Request | In the page header, choose Edit. | The following buttons are displayed in the page header:Edit - inactiveApproveResubmit (Incomplete)RejectNot applicableHold |  |
| 5 | Complete the Initial Risk Analysis | In the Initial Risk Analysis section, select a value of the initial risk assessment for Severity, Likelihood, and Rating, if you haven't done it earlier. |  |  |
| 6 | Open the Review SME Evaluations Subactivity | From the Activities section in the change request, choose Review SME Evaluations to navigate to the activity. | The Activity 'Approval': <activity number>, Review SME Evaluations screen is displayed. |  |
| 7 | Perform the Review SME Evaluations Subactivity | To perform the Review SME Evaluations subactivity, you can refer to the procedure described in [Perform an Activity of Category Approval](#unique_17) [page ] 22. | The status of the Review SME Evaluations subactivity is changed to Approved.The status of the change request is changed to Approved.Note It is possible to set the status of the change request to Approved manually. You can do so by choosing Approve from the page header in the change request. |  |
| 8 | Open the SME Evaluations Subactivity | From the Activities section in the change request, choose SME Evaluations to navigate to the activity. | The Activity 'Notification': <activity number>, SME Evaluations screen is displayed. |  |
| 9 | Perform the SME Evaluations Subactivity | To perform the SME Evaluations subactivity, you can refer to the procedure described in [Perform an Activity of Category Notification](#unique_19) [page ] 23. | The status of the SME Evaluations subactivity is changed to Completed. |  |
| 10 | Open the Evaluation and Approval Activity | From the Activities section in the change request, choose Evaluation and Approval to navigate to the activity. | The Activity 'Phase': <activity number>, Evaluation and Approval screen is displayed. |  |
| 11 | Perform the Evaluation and Approval Activity | To perform the Evaluation and Approval activity, you can refer to the procedure described in [Perform an Activity of Category Notification](#unique_19) [page ] 23. | The status of the Evaluation and Approval activity is changed to Completed. |  |

### Drive a Change Request and Perform Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

All assigned activities have to be completed in order to implement the approved change. The change management coordinator drives the completion of all activities, so that they are completed by their owners or approvers.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Change Management Coordinator. |  |  |
| 2 | Access App | Open Manage Change Requests (F3406). | The Manage Change Requests screen is displayed. |  |
| 3 | Open a Change Request | Search for the change request that you have created and open it.Note To find your change request easier, you can search for it by entering the description of the change request or part of it in the Search field. Alternatively, you can search by the following criteria:Status: ApprovedRole of the Person Involved: CoordinatorPerson Involved: | The Change Request 'MOC Change Request': < change request ID - description> screen is displayed, and the status of the change request is <your user>Approved. |  |
| 4 | Complete the Initial Review Activity | Make sure that the Initial Review activity and all its subactivities are completed as described in the Carry Out Initial Review step. |  |  |
| 5 | Complete the Evaluation and Approval Activity | Make sure that the Evaluation and Approval< activity and all its subactivities are completed as described in the Approve Change Request step. |  |  |
| 6 | Complete the Pre-Implementation Activity | Make sure that the following subactivities are completed:Engineering and Design FinalizationPurchase Long-Lead MaterialRed-line DrawingsUpdate DocumentationInform Operators of New TaskSafety Training UpdateMSDS UpdateConfirm Readiness for PSSRNote For more information on how to complete subactivities of different categories, see [Perform Activities](#unique_20) [page ] 21.Perform the Pre-Implementation activity. You can refer to the procedure described in [Perform an Activity of Category Notification](#unique_19) [page ] 23. |  |  |
| 7 | Complete the Implementation Activity | Make sure that the following subactivities are completed:Pre-startup Safety ReviewMaintenance NotificationNote You can create a maintenance notification as a follow-up action if you have an active BAdI implementation of the Create Maintenance Notification as a Follow-Up Action BAdI. In the Maintenance Notification subactivity, choose Create Maintenance Notification. The system generates a maintenance notification in the Plant Maintenance (PM) component with the change request details. The newly created maintenance notification is available under the References section, in the Related Objects table. You can navigate to the maintenance notification in the PM component from there.Approve to StartupNote The status of the change request is changed from Approved to In Process automatically when this subactivity is completed. Alternatively, you can set the status to In Process manually by choosing Release and Create Activities.Note For more information on how to complete subactivities of different categories, see [Perform Activities](#unique_20) [page ] 21.Perform the Implementation activity. You can refer to the procedure described in [Perform an Activity of Category Notification](#unique_19) [page ] 23. |  |  |
| 8 | Complete the Post-Implementation Activity | Make sure that the following subactivities are completed:Operator TrainingReview PSSR and Action Item CompletionFinal Documentation UpdatesNote For more information on how to complete subactivities of different categories, see [Perform Activities](#unique_20) [page ] 21.Perform the Post-Implementation activity. You can refer to the procedure described in [Perform an Activity of Category Notification](#unique_19) [page ] 23. |  |  |
| 9 | Complete the Follow-up and Close-out Activity | Make sure that the following subactivity is completed:Lesson LearnedNote For more information on how to complete subactivities of different categories, see [Perform Activities](#unique_20) [page ] 21.Perform the Follow-up and Close-out activity. You can refer to the procedure described in [Perform an Activity of Category Notification](#unique_19) [page ] 23. |  |  |

### Close a Change Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The change management coordinator closes the change request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Change Management Coordinator. |  |  |
| 2 | Access App | Open Manage Change Requests (F3406). | The Manage Change Requests screen is displayed. |  |
| 3 | Open a Change Request | Search for the change request that you have created and open it.Note To find your change request easier, you can search for it by entering the description of the change request or part of it in the Search field. Alternatively, you can search by the following criteria:Status: In ProcessRole of the Person Involved: CoordinatorPerson Involved: <your user> | The Change Request 'MOC Change Request': < change request ID - description> screen is displayed, and the status of the change request is In Process. |  |
| 4 | Check Activities | Make sure that all of the assigned activities in the Activities section are completed. | All activities are carried out and completed. There is a green square in front of each activity that indicates that the activity is completed. |  |
| 5 | Close the Change Request | Choose Edit and then choose Close the Change Request. | The status of the change request is changed to Closed and the following success message is displayed in the message popover:Status of change request changed from In Process to Closed |  |
| 6 | Save Your Changes | Choose Save. | The following success message is displayed in the message popover:Data saved successfully |  |

### Additional Process Steps (Optional)

#### Perform Analysis

This section contains process steps that allow you to analyze the change requests and activities data in your system.

##### Perform a Detailed Analysis of Change Requests and Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The change management coordinator reviews, analyze, and get a graphical representation of the data in the system for change requests and activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Change Management Coordinator. |  |  |
| 2 | Access App | Open Change Requests and Activities - Detailed Analysis (F5469). | The Change Requests and Activities - Detailed Analysis screen is displayed. |  |
| 3 | Add an Analysis Step | Choose Add Analysis Step (+ icon).In the Category dialog box, make the following selections:Change Requests > Change Requests by Status > Pie Chart | The Change Requests by Status step is added to the analysis path.All available records are counted and displayed in a pie chart in the Current Analysis Step view. |  |
| 4 | Display Step Details | Hover over the largest piece of the chart with the cursor. | Details about the status and the number of the change requests of this status are displayed in a mouseover. |  |
| 5 | Refine Analysis | Select the largest piece of the chart and choose Add Analysis Step (+ icon). | All available records are counted and displayed in a line chart in the Current Analysis Step view. |  |
| 6 | Add Further Steps | Add one or more steps as described in steps 3 and 5. | The selected steps are added to the analysis path. |  |
| 7 | Save the Analysis | Choose the Related Options icon next to the Unnamed Analysis Path title and select Save.Enter a name for the analysis path and choose OK. | The analysis path is saved. The entered name is displayed above the analysis path. |  |

##### Get an Overview of Change Requests

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The change management coordinator review, filter, and analyze the data in the system for change requests.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Change Management Coordinator. |  |  |
| 2 | Access App | Open Change Requests Dashboard (F5760). | The Change Requests Dashboard screen is displayed.The filter bar contains the following filters with graphical representations:Change Requests by TypeChange Requests by Status GroupChange Requests by Leading Object Type |  |
| 3 | Set a Filter | For the Change Requests by Type filter, select the MOC Change Request type via the dropdown list, and choose OK. | The MOC Change Request type is selected. The rest of the filters are automatically configured to show data only for the selected type. |  |
| 4 | Adapt Filters | Choose Adapt Filters.In the dialog box, select the Show on Filter Bar checkbox for the Change Requests by Impact filter.Choose OK. | The Change Requests by Impact filter is shown in the filter bar. |  |
| 5 | Set an Additional Filter | For the Change Requests by Impact filer, select the largest piece of the pie chart. | The impact is selected. The rest of the filters are automatically configured to show data only for the selected impact, considering the selection for the type as well. |  |
| 6 | Check the Search Results | The search results are updated automatically after each filter selection. Check the search results as shown in the following two sections:Graphical representation of the filtered change requests by country/region and plant.Change Requests – table view of the search results.From the table view, you can navigate to view a selected change request. |  |  |

##### Get an Overview of Change Activities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The change management coordinator review, filter, and analyze the data in the system for change activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Change Management Coordinator. |  |  |
| 2 | Access App | Open Change Activities Dashboard (F5761). | The Change Activities Dashboard screen is displayed.The filter bar contains the following filters with graphical representations:Change Activities by TypeChange Activities by StatusChange Activities by Overdue StatusChange Activities by Main Responsible Assigned |  |
| 3 | Set a Filter | For the Change Activities by Type filter, select the first type in the dropdown list on the right, and choose OK. | The type is selected.The rest of the filters are automatically configured to show data only for the selected type. |  |
| 4 | Set an Additional Filter | For the Change Activities by Status, select the largest piece of the pie chart. | The status is selected.The rest of the filters are automatically configured to show data only for the selected status, considering the selection for the type as well. |  |
| 5 | Check the Search Results | The search results are updated automatically after each filter selection. Check the search results as shown in the following two sections:Graphical representation of the filtered change activities by country/region and plant.Change Activities - table view of the search results.From the table view, you can navigate to view a selected change activity. |  |  |

## Appendix

### Perform Activities

Purpose

The responsible persons perform activities of different categories by carrying out reviews, tasks, or approvals.

#### Perform an Activity of Category “Task”

Purpose

The responsible persons perform activities of category “Task”.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Notify the Activity Owner | Search and open an activity of category Task via the Manage Change Activities (F3405) app. For example, you can use the following search criteria:Choose Adapt Filters and select the Activity Category filter. In the Activity Category field, select Task.Choose Adapt Filters and select the Change Request ID filter. In the Change Request ID field, enter the description of the change request.Choose Edit.In the People Involved section, select Activity Owner in the Role column. In the Business Partner column, enter your business partner number or use the value help and search by your name.Choose Notify. | The activity status is changed to Notified and the following success message is displayed in the message popover:Status of activity changed from Created to Notified |  |
| 2 | Complete the Activity | Choose Complete. | The activity status is changed to Completed and the following success message is displayed in the message popover:Status of activity changed from Notified to Completed |  |
| 3 | Save Your Changes | Choose Save. | The following success message is displayed in the message popover:Data saved successfully |  |
| 4 | Return to the Change Request | Use the link to the change request in the Overview section of the activity to go back to the change request. | The Change Request 'MOC Change Request': < change request ID - description> screen is displayed. In the Activities section, the activity that has just been completed is with status Completed and has a green indicator in front. |  |

#### Perform an Activity of Category “Approval”

Purpose

The responsible persons perform activities of category “Approval”.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Notify the Approver | Search and open an activity of category Approval via the Manage Change Activities (F3405) app. For example, you can use the following search criteria:Choose Adapt Filters and select the Activity Category filter. In the Activity Category field, select Approval.Choose Adapt Filters and select the Change Request ID filter. In the Change Request ID field, enter the description of the change request.Choose Edit.In the People Involved section, select Approver in the Role column. In the Business Partner column, enter your business partner number or use the value help and search by your name.Choose Notify. | The activity status is changed to Notified and the following success message is displayed in the message popover:Status of activity changed from Created to Notified |  |
| 2 | Approve the Activity | Choose Approve. | The activity status is changed to Approved and the following success message is displayed in the message popover:Status of activity changed from Notified to Approved |  |
| 3 | Save Your Changes | Choose Save. | The following success message is displayed in the message popover:Data saved successfully |  |
| 4 | Return to the Change Request | Use the link to the change request in the Overview section of the activity to go back to the change request. | The Change Request 'MOC Change Request': < change request ID - description> screen is displayed. In the Activities section, the activity that has just been completed is with status Approved and has a green indicator in front. |  |

#### Perform an Activity of Category “Notification”

Purpose

The responsible persons perform activities of category “Notification”.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Notify the Activity Owner | Search and open an activity of category Notification via the Manage Change Activities (F3405) app. For example, you can use the following search criteria:Choose Adapt Filters and select the Activity Category filter. In the Activity Category field, select Notification.Choose Adapt Filters and select the Change Request ID filter. In the Change Request ID field, enter the description of the change request.Choose Edit.In the People Involved section, select Activity Owner in the Role column. In the Business Partner column, enter a business partner number or use the value help to select a business partner.Choose Notify. | The activity status is changed to Completed and the following success message is displayed in the message popover:Status of activity changed from Created to Completed |  |
| 2 | Save Your Changes | Choose Save. | The following success message is displayed in the message popover:Data saved successfully |  |
| 3 | Return to the Change Request | Use the link to the change request in the Overview section of the activity to go back to the change request. | The Change Request 'MOC Change Request': < change request ID - description> screen is displayed. In the Activities section, the activity that has just been completed is with status Completed and has a green indicator in front. |  |

### Configure Your Solution

This section contains process steps that allow you to configure a custom change request type and its properties.

#### Define Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The configuration expert creates the codes that can later be grouped into code groups and used as possible answers to a question in a questionnaire.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, follow the steps as described below for either Configure Your Solution, or SAP Central Business Configuration.

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Set Local Version | Choose Set Local Version that is in the bottom-right corner.Select the relevant country/region from the dropdown list in the newly opened dialog box.Choose Set Local Version to confirm. | The local version is set. |  |
| 4 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 5 | Navigate to a Configuration Item | Make the following entries in the search fields and press Enter:Application Area: Asset ManagementSub Application Area: Environment, Health, and SafetyFrom the search results, choose the Management of Change item. | The Configure Your Solution – Management of Change split screen is displayed on the right. |  |
| 6 | Open a Configuration Step | Go to the Define Codes step and choose Configure. | The Change View "Code": Overview screen is displayed. |  |
| 7 | Create New Codes | Choose New Entries, make the following entries, and choose Save:CodeDescriptionZ01_COST_000Not applicableZ01_COST_010Up to 15.000 USDZ01_COST_020More than 15.000 USD | The entries are saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Codes.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Define Codes" screen is displayed. |  |
| 3 | Create New Codes | Choose New Entries, make the following entries, and choose Save:CodeDescriptionZ01_COST_000Not applicableZ01_COST_010Up to 15.000 USDZ01_COST_020More than 15.000 USD | The entries are saved. |  |

#### Define Catalogs and Code Groups

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The configuration expert creates code groups with the possible answers to questions in a questionnaire.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, follow the steps as described below for either Configure Your Solution, or SAP Central Business Configuration.

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Set Local Version | Choose Set Local Version that is in the bottom-right corner.Select the relevant country/region from the dropdown list in the newly opened dialog box.Choose Set Local Version to confirm. | The local version is set. |  |
| 4 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 5 | Navigate to a Configuration Item | Make the following entries in the search fields and press Enter:Application Area: Asset ManagementSub Application Area: Environment, Health, and SafetyFrom the search results, choose the Management of Change item. | The Configure Your Solution – Management of Change split screen is displayed on the right. |  |
| 6 | Open a Configuration Step | Go to the Define Catalogs and Code Groups step and choose Configure. | The Change View "Catalog": Overview screen is displayed. |  |
| 7 | Create a New Catalog | Choose New Entries, make the following entries, and choose Save:Catalog: Z01Description: Catalog for Z01Application: MOC​ | A new catalog is created. |  |
| 8 | Assign Codes to Catalog | Select the newly created catalog and open Assign Codes to Catalog from the Dialog Structure on the left.Choose New Entries and add the following codes that you have created in the Define Codes procedure:Z01_COST_000Z01_COST_010Z01_COST_020Choose Save. | All codes are added to the catalog. |  |
| 9 | Create a Code Group | Open Code Groups from the Dialog Structure on the left.Choose New Entries, create an entry with the following data, and choose Save:Code Group: Z01_COSTDescription: Estimated CostCatalog: Z01 | The entry is saved. |  |
| 10 | Assign Codes to a Code Group | Select the Z01_COST code group and open Assign Codes to Code Group from the Dialog Structure on the left.Choose New Entries, make the following entries in the Codes column, and choose Save:Z01_COST_000Z01_COST_010Z01_COST_020 | The codes are assigned to the code group. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Catalogs and Code Groups.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Catalog": Overview screen is displayed. |  |
| 3 | Create a New Catalog | Choose New Entries, make the following entries, and choose Save:Catalog: Z01Description: Catalog for Z01Application: MOC​ | A new catalog is created. |  |
| 4 | Assign Codes to Catalog | Select the newly created catalog and open Assign Codes to Catalog from the Dialog Structure on the left.Choose New Entries and add the following codes that you have created in the Define Codes procedure:Z01_COST_000Z01_COST_010Z01_COST_020Choose Save. | All codes are added to the catalog. |  |
| 5 | Create a Code Group | Open Code Groups from the Dialog Structure on the left.Choose New Entries, create an entry with the following data, and choose Save:Code Group: Z01_COSTDescription: Estimated CostCatalog: Z01 | The entry is saved. |  |
| 6 | Assign Codes to a Code Group | Select the Z01_COST code group and open Assign Codes to Code Group from the Dialog Structure on the left.Choose New Entries, make the following entries in the Codes column, and choose Save:Z01_COST_000Z01_COST_010Z01_COST_020 | The codes are assigned to the code group. |  |

#### Define Activity Templates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The configuration expert creates activity templates of different types and organizes them in a hierarchy, so that they can later be included in a change request type.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, follow the steps as described below for either Configure Your Solution, or SAP Central Business Configuration.

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Set Local Version | Choose Set Local Version that is in the bottom-right corner.Select the relevant country/region from the dropdown list in the newly opened dialog box.Choose Set Local Version to confirm. | The local version is set. |  |
| 4 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 5 | Navigate to a Configuration Item | Make the following entries in the search fields and press Enter:Application Area: Asset ManagementSub Application Area: Environment, Health, and SafetyFrom the search results, choose the Management of Change item. | The Configure Your Solution – Management of Change split screen is displayed on the right. |  |
| 6 | Open a Configuration Step | Go to the Define Activity Templates step and choose Configure. | The Change View "Activity Template": Overview screen is displayed. |  |
| 7 | Create Activity Templates | Choose New Entries and make the following entries using Next Entry to create a new entry:QuestionnaireActy Template: Z01_N_1000Activity Template Text: Initial AssessmentActivity Type: QuestionnaireResponse Type: NoneQuestion CatalogActy Template: Z01_C_1100Activity Template Text: Category of the ChangeActivity Type: Question CatalogResponse Type: NoneQuestionActy Template: Z01_Q_1110Activity Template Text: Production Facility or EquipmentActivity Type: QuestionResponse Type: BooleanQuestionActy Template: Z01_Q_1120Activity Template Text: Processes or MethodsActivity Type: QuestionResponse Type: BooleanQuestion CatalogActy Template: Z01_C_1200Activity Template Text: Impact of the ChangeActivity Type: Question CatalogResponse Type: NoneQuestionActy Template: Z01_Q_1210Activity Template Text: Estimated CostActivity Type: QuestionResponse Type: CodeTaskActy Template: Z01_T_1000Activity Template Text: Review Technical RequirementsActivity Type: TaskResponse Type: NoneTaskActy Template: Z01_T_1100Activity Template Text: Create Technical RequirementsActivity Type: TaskResponse Type: NoneApprovalActy Template: Z01_A_1200Activity Template Text: Approve Technical RequirementsActivity Type: ApprovalResponse Type: NoneChoose Save. | The activity templates are saved. |  |
| 8 | Assign Code Groups to Activity Templates | Go back to the activity templates and select the Z01_Q_1210 activity template that has Code as a response type.Open Code Group from the Dialog Structure on the left.Choose New Entries, make the following entry, and choose Save:Code Group: Z01_COST | The code group is assigned to the activity template. |  |
| 9 | Assign Questions to a Question Catalog | Go back to the activity templates, select the Z01_C_1100 activity template of type question catalog, and open Assign Activity Templates from the Dialog Structure on the left.Choose New Entries and add the following activity templates of type question with the respective sorting number:Z01_Q_1110, sorting number: 10Z01_Q_1120, sorting number: 20Choose Save.Go back to the activity templates and select the Z01_C_1200 activity template of type question catalog. Following the same procedure, assign the Z01_Q_1210 activity template of type question. | The question catalog has questions assigned. |  |
| 10 | Assign Question Catalogs to a Questionnaire | Go back to the activity templates and select Z01_N_1000.Open Assign Activity Templates from the Dialog Structure on the left.Choose New Entries and add the following activity templates:Z01_C_1100, sorting number: 10Z01_C_1200, sorting number: 20Choose Save. | The questionnaire has a question catalog assigned. |  |
| 11 | Create an Activity Structure | Go back to the activity templates and select Z01_T_1000.Open Assign Activity Templates from the Dialog Structure on the left.Choose New Entries and add the following activity templates:Z01_T_1100, sorting number: 10Z01_A_1200, sorting number: 20Choose Save. | The entries are saved. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Activity Templates.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View " Define Activity Template" screen is displayed. |  |
| 3 | Create Activity Templates | Choose New Entries and make the following entries using Next Entry to create a new entry:QuestionnaireActy Template: Z01_N_1000Activity Template Text: Initial AssessmentActivity Type: QuestionnaireResponse Type: NoneQuestion CatalogActy Template: Z01_C_1100Activity Template Text: Category of the ChangeActivity Type: Question CatalogResponse Type: NoneQuestionActy Template: Z01_Q_1110Activity Template Text: Production Facility or EquipmentActivity Type: QuestionResponse Type: BooleanQuestionActy Template: Z01_Q_1120Activity Template Text: Processes or MethodsActivity Type: QuestionResponse Type: BooleanQuestion CatalogActy Template: Z01_C_1200Activity Template Text: Impact of the ChangeActivity Type: Question CatalogResponse Type: NoneQuestionActy Template: Z01_Q_1210Activity Template Text: Estimated CostActivity Type: QuestionResponse Type: CodeTaskActy Template: Z01_T_1000Activity Template Text: Review Technical RequirementsActivity Type: TaskResponse Type: NoneTaskActy Template: Z01_T_1100Activity Template Text: Create Technical RequirementsActivity Type: TaskResponse Type: NoneApprovalActy Template: Z01_A_1200Activity Template Text: Approve Technical RequirementsActivity Type: ApprovalResponse Type: None | The activity templates are saved. |  |
| 4 | Assign Code Groups to Activity Templates | Go back to the activity templates and select the Z01_Q_1210 activity template that has Code as a response type.Open Code Group from the Dialog Structure on the left.Choose New Entries, make the following entry, and choose Save:Code Group: Z01_COST | The code group is assigned to the activity template. |  |
| 5 | Assign Questions to a Question Catalog | Go back to the activity templates, select the Z01_C_1100 activity template of type question catalog, and open Assign Activity Templates from the Dialog Structure on the left.Choose New Entries and add the following activity templates of type question with the respective sorting number:Z01_Q_1110, sorting number: 10Z01_Q_1120, sorting number: 20Choose Save.Go back to the activity templates and select the Z01_C_1200 activity template of type question catalog. Following the same procedure, assign the Z01_Q_1210 activity template of type question. | The question catalog has questions assigned. |  |
| 6 | Assign Question Catalogs to a Questionnaire | Go back to the activity templates and select Z01_N_1000.Open Assign Activity Templates from the Dialog Structure on the left.Choose New Entries and add the following activity templates:Z01_C_1100, sorting number: 10Z01_C_1200, sorting number: 20Choose Save. | The questionnaire has a question catalog assigned. |  |
| 7 | Create an Activity Structure | Go back to the activity templates and select Z01_T_1000.Open Assign Activity Templates from the Dialog Structure on the left.Choose New Entries and add the following activity templates:Z01_T_1100, sorting number: 10Z01_A_1200, sorting number: 20Choose Save. | The entries are saved. |  |

#### Define Change Request Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The configuration expert creates a custom change request type and configures its properties.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, follow the steps as described below for either Configure Your Solution, or SAP Central Business Configuration.

Configure Your Solution

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Set Local Version | Choose Set Local Version that is in the bottom right corner.Select the relevant country/region from the dropdown list in the newly opened dialog box.Choose Set Local Version to confirm. | The local version is set. |  |
| 4 | Configure Your Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase screen is displayed. |  |
| 5 | Navigate to a Configuration Item | Make the following entries in the search fields and press Enter:Application Area: Asset ManagementSub Application Area: Environment, Health, and SafetyFrom the search results, choose the Management of Change item. | The Configure Your Solution – Management of Change split screen is displayed on the right. |  |
| 6 | Open a Configuration Step | Go to the Define Change Request Types step and choose Configure. | The Change View "Change Request Type": Overview screen is displayed. |  |
| 7 | Create a Change Request Type | Choose New Entries and create a new change request type with the following details:CR Type: Z01Type: Technical ChangeCR Category: Change RequestCR Number Range: M1Acty No.Rng: M1Init. Review: 01Resp.Partn. Role: CoordinatorReporter Role: Reporter​Print Layout: /MOC/PF_CHG_REQ_GATEWAYChoose Save. | The change request type is created. |  |
| 8 | Assign Activity Templates | Select the newly created change request type and open Assign Activity Templates.Choose New Entries and add the following activity templates:Z01_T_1000, sorting number: 10Z01_N_1000, sorting number: 20Choose Save. | The entries are populated. |  |
| 9 | Specify Reference Objects | Open Reference Objects from the Dialog Structure on the left.Choose New Entries and add the following object types:EQ, select Main Ref. ObjectFL, select Main Ref. ObjectChoose Save. | The entries are populated.You can now create a change request of the configured type. |  |

SAP Central Business Configuration

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Change Request Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Define Change Request Type" screen is displayed. |  |
| 3 | Create a Change Request Type | Choose New Entries and create a new change request type with the following details:CR Type: Z01Type: Technical ChangeCR Category: Change RequestCR Number Range: M1Acty No.Rng: M1Init. Review: 01Resp.Partn. Role: CoordinatorReporter Role: Reporter​Print Layout: /MOC/PF_CHG_REQ_GATEWAYChoose Save. | The change request type is created. |  |
| 4 | Assign Activity Templates | Select the newly created change request type and open Assign Activity Templates.Choose New Entries and add the following activity templates:Z01_T_1000, sorting number: 10Z01_N_1000, sorting number: 20Choose Save. | The entries are populated. |  |
| 5 | Specify Reference Objects | Open Reference Objects from the Dialog Structure on the left.Choose New Entries and add the following object types:EQ, select Main Ref. ObjectFL, select Main Ref. ObjectChoose Save. | The entries are populated.You can now create a change request of the configured type. |  |

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
- see-also :: [[13-quality-ehs-and-compliance/ehs-lokation-anlegen-sds-3sr-358]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4YX_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 63,471 chars in the whole document
