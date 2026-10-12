---
id: 13-quality-ehs-and-compliance/test-script-compliance-management-for-environment-health-and-safety-4c
title: "Test Script: Compliance Management for Environment, Health, and Safety (4C8) - SAP S/4HANA Cloud Public Edition (4C8_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 4C8: EHS compliance management (locations, permits, requirements, tasks, deviations) with step tables."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/environmental-compliance-and-emissions]
aliases: [4C8_S4CLD2608_BPD_EN_XX]
keywords: [Environmental Compliance and Emissions Management, ehs compliance management, test scripts, ehs locations, permits, compliance requirements, compliance obligation assignments, compliance tasks, task execution, task monitoring]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4C8_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1020
topic: 13-quality-ehs-and-compliance/environmental-compliance-and-emissions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Compliance Management for Environment, Health, and Safety (4C8) - SAP S/4HANA Cloud Public Edition (4C8_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4C8_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Environmental Compliance and Emissions Management** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Compliance Management for Environment, Health, and Safety (4C8) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232841765)

[2 Prerequisites 3](#_Toc232841766)

[2.1 System Access 3](#_Toc232841767)

[2.2 Preliminary Configuration 3](#_Toc232841768)

[2.3 Roles 3](#_Toc232841769)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232841770)

[2.5 Preliminary Steps 4](#_Toc232841771)

[3 Overview Table 6](#_Toc232841772)

[4 Test Procedures 7](#_Toc232841773)

[4.1 Manage Locations 7](#_Toc232841774)

[4.2 Manage Permits 8](#_Toc232841775)

[4.3 Manage Compliance Requirements 10](#_Toc232841776)

[4.4 Manage Compliance Obligation Assignments 12](#_Toc232841777)

[4.5 Set Up Compliance Tasks 14](#_Toc232841778)

[4.6 Manage Compliance Tasks 16](#_Toc232841779)

[4.7 Execute Tasks 17](#_Toc232841780)

[4.8 Monitor Compliance Tasks 19](#_Toc232841781)

[4.9 Manage Deviations 23](#_Toc232841782)

## Purpose

Overview

This scope item helps you to manage compliance, and as a result, reduce operational risk in your company. You can manage compliance information about permits, regulations, and policies. You can import compliance requirements from a spreadsheet and streamline compliance planning by associating tasks directly with compliance requirements. The process also enables you to handle deviations.

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

### Preliminary Configuration

Purpose

Some of the process steps in the current test script depend on configurations that are not included in the standard Cloud Best Practices content delivery of predefined configurations. To be able to perform these process steps, additional manual configurations are required. They are described in the following procedures.

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Environmental Manager | SAP_BR_EHS_ENV_MGMT | Environment Management | SAP_BR_EHS_ENV_MGMT |  |
| Production Operator - EHS Info | SAP_BR_PRODN_OPTR_EHS_INFO |  |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Location | Division ABC | Location of a Company type. Parent location for all other sample locations. |  |
| Location | Tank Area | Location of a Site type. Sublocation of Division ABC. |  |
| Location | Ethanol Storage Tank R5-BB7 | Location of a Storage Location type. Sublocation of Tank Area. |  |
| Location | Ethanol Storage Tank R6-BB9 | Location of a Storage Location type. Sublocation of Tank Area. |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 3SR | Create EHS Location - MDS |

### Preliminary Steps

Purpose

Before you begin with the test procedures, make sure that you complete the steps below.

Procedure

1. Start the SAP Fiori launchpad.
2. If the Manage Locations (WDA0983) tile is not available on your SAP Fiori launchpad home screen, add it via the App Finder.

|  |
| --- |
| Note To add a tile to your SAP Fiori launchpad home screen, go to your profile in the upper right corner of the screen. Select the Edit Home Page option from the list. Then, select the blank tile that appears to go to the App Finder. In the Search field on the upper right side of the screen, enter the name of the app that you want to add to your SAP Fiori launchpad, and press Enter. The app appears in your search results. Select the pin to add the app tile to your SAP Fiori launchpad home screen. In the footer, the system shows a message that the tile has been added successfully. To exit edit mode, go back to your SAP Fiori launchpad home screen and select the Exit Edit Mode option from the list under your profile. |

1. Start the Manage Locations (WDA0983) app.
2. Select the Division ABC location and choose the hyperlink.
3. Navigate to the Persons Responsible tab.
4. Add your user as a person responsible with the Environmental Manager role.
5. Save your entries.
6. Repeat steps 4 - 7 to assign your user as a person responsible with the Environmental Manager role for all other locations (Tank Area, Ehtanol Storage Tank R5-BB7, and Ethanol Storage Tank R6-BB9).

|  |
| --- |
| Note Make sure that all locations are set to Active to enable their use in the test procedures. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manage Locations](#unique_9) [page ] 7 | Environmental Manager | Manage Locations (WDA0983) | A new location record is created within the location structure. The record is activated. |
| [Manage Compliance Requirements](#unique_10) [page ] 10 | Environmental Manager | Manage Compliance Requirements - Regulations, Permits, Policies (F5038) | A new compliance requirement record is created to reflect changes in requirement data from permits, regulations, or policies. Two paragraphs are added to it. |
| [Set Up Compliance Tasks](#unique_11) [page ] 14 | Environmental Manager | Compliance Requirement Tasks (F4346) | Tasks are created in the compliance requirement. Assignment to paragraphs is done automatically or manually. Reference to other existing paragraphs can be added. Task recurrence is set to manage compliance over time. |
| [Manage Compliance Tasks](#unique_12) [page ] 16 | Environmental Manager | Task Calendar (F3840) | Tasks are monitored and rescheduled, as needed, to meet the requirements and fit the schedule of the team. |
| [Execute Tasks](#unique_13) [page ] 17 | Production Operator - EHS Info | My Inbox - Environment Management (F0862) | Assigned tasks are received in the assignee’s inbox. Further information on received tasks might be requested. After information is provided, tasks are performed and the results - recorded. |
| [Monitor Compliance Tasks](#unique_14) [page ] 19 | Environmental Manager | Monitor Tasks (F2527) | Task execution is monitored.With this, related issues are identified and additional actions initiated to manage them. These actions might include creating and managing deviations, rescheduling or reassignment of ongoing tasks. |
| [Manage Deviations](#unique_15) [page ] 23 | Environmental Manager | Manage Deviation Incidents (WDA0449) | Deviations are created.Triggering tasks can be added to deviations for further root cause investigation. Based on investigation outcomes, corrective and preventive measures are planned. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Locations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a new location record in the location structure. The new record is required because there’s new or changed equipment in the location. The data of the new location record is updated.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Locations. | The Locations screen is displayed. |  |
| 3 | Navigate to Location Structure | On the Locations screen, choose Edit Location Structure. Make sure that Division ABC is set as My Location. | The Location Structure screen is displayed. |  |
| 4 | Create New Location Record | On the Location Structure screen, select the row with the Tank Area location as a parent and choose New. | The Create Location screen is displayed. |  |
| 5 | Edit Location Record | On the Create Location screen under the Basic Information tab, enter the following data:Location: Ethanol Storage Tank R2-BB4Location Type: Storage LocationRevision Start Date: <First day of calendar year>Note You can only enter start dates that are within the revision period of the Tank Area location where the Ethanol Storage Tank R2-BB4 location record is created.Choose Save. | The Ethanol Storage Tank R2-BB4 location record data is updated. |  |
| 6 | Edit Location Address | On the same screen, navigate to the Address tab and enter the following data:Country/Region: DEChoose Save. Then, choose Return to Location Structure to navigate back.Note You can edit the address data of any of your locations in this tab. | The Ethanol Storage Tank R2-BB4 address data is updated. |  |
| 7 | Activate Location Record | From the list of locations in the hierarchy, navigate to the newly created location (Ethanol Storage Tank R2-BB4).While on the same screen, go to the Set Status dropdown list and choose Active. Then choose Save in the lower right corner of the screen. | The location record is saved in Active status in the location structure. |  |

### Manage Permits

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager can create new permits for the locations assigned to them to meet compliance requirements. The Environmental Manager is able to adjust the settings in this app to optimize business processes.

|  |
| --- |
| Note The Environmental Manager is able to add as many permits as necessary to fulfill the requirements and to manage compliance over time. |

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open My Permits (F5192). | The My Permits screen is displayed. |  |
| 3 | Create New Permit | On the My Permits screen, choose Create. | The Create Permit screen is displayed. |  |
| 4 | Edit General Information Data | On the Create Permit screen, under the General Information tab, enter the following data:Name: Storm Water Discharge Tank Version 1Permit Number: Vdr. 86.03/2Description: Permit to discharge storm water from tank R5 - R6Location: Tank AreaDomain: WaterIssuing Organization: Berlin Water Control DepartmentIssuing Authority: Berlin Water Control DepartmentNote This is not a mandatory field. If you would like to input an Issuing Authority, please maintain the corresponding business partner first.Effective Date: <Today's date>Expiration Date: <Two years from tomorrow>Note You can use the value help to find the corresponding Location and Issuing Authority. | General Information for the permit is added. |  |
| 5 | Create Permit | On the same screen, choose Create. | A permit is created. |  |
| 6 | Navigate Back to the My Permits Screen | Choose the Back arrow on the upper left part of the screen. | The My Permits screen is displayed. |  |
| 7 | Select Created Permit | Navigate to the Search bar and enter the permit name to find the newly created permit and select it from the results list.Note Alternatively, use one of the other filters to search and find a permit. | The Permits screen is displayed. |  |
| 8 | Edit Permit Lifecycle Value | In the Permit Lifecycle dropdown list, verify that the following values are shown: In Preparation, Application Submitted, Active, For Renewal and Expired.Select Application Submitted. | Permit Lifecycle status is updated. |  |
| 9 | Edit Set “For Renewal” on Date | On the same screen, select the calendar icon and choose a date that is one to two months from the Effective Date.Note The Send Notification checkbox is automatically selected.You can unselect the checkbox if you do not want to receive an email notification when the permit reaches the Set "For Renewal" on date. | Set “For Renewal” on date is updated. |  |
| 10 | Edit Permit Lifecycle Value | While on the Permit screen, select Active from the Permit Lifecycle dropdown list. | Permit Lifecycle is updated. |  |
| 11 | Edit Status | On the same screen, under the Set Status dropdown list, select Released.Note Permit Lifecycle must be set to Active before Status can be updated. | Status is updated. |  |
| 12 | Save Changes | On the Permit screen, choose Save. | Data changes are saved. |  |

### Manage Compliance Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a new compliance requirement record. The new record is required because there’s new or changed requirement data from permits, regulations, or policies. After creating the compliance requirement record, the Environmental Manager adds paragraphs to it to describe specific requirements.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Compliance Requirements - Regulations, Permits, Policies (F5038). | The Compliance Requirements screen is displayed. |  |
| 3 | Navigate to Create Policy | On the Compliance Requirements screen, choose Create Policy to create a new compliance requirement record of type Policy. | The Create New Policy screen is displayed. |  |
| 4 | Edit Policy Data | On the Create New Policy screen, under the Basic Information section, enter the following data about the compliance requirement and then choose Save:Compliance Requirement Name: Tank leakage prevention programIssuing Organization: My CompanyValid From: <First day of calendar year>Domain: WaterNote If applicable, on the same screen under the Validity Area section, you can enter or select the countries and regions that the created requirement record of type Policy is relevant for.Choose Save in the lower right corner of the screen. | Your compliance requirement record of type Policy is saved. You are redirected to the Policy: Tank leakage prevention program screen. |  |
| 5 | Add Paragraph to Policy | Note Make sure that you are on the Policy: Tank leakage prevention program screen: Contents tab.On the Policy: Tank leakage prevention program screen: Contents tab, choose Add (+ icon) to create a new paragraph within the Tank leakage prevention program compliance requirement record. | The Create New Paragraph dialog box is displayed. |  |
| 6 | Edit Paragraph Data | In the Create New Paragraph dialog box, enter or select the following data and then choose OK:Name: Regular internal tank inspectionsType: Requirement | Paragraph data is updated. |  |
| 7 | Save Paragraph | Choose Save to save the paragraph data. | Paragraph data is saved. |  |
| 8 | Navigate to Paragraph Information | Open the Regular internal tank inspections paragraph. | The Paragraph:Regular internal tank inspections screen is displayed. |  |
| 9 | Edit Basic Information | On the Paragraph:Regular internal tank inspections screen under the Basic Information tab, enter the following information in the Requirement Text field and then choose Save:Requirement Text: Do monthly inspections to monitor leakage. Any leak above 20L is considered a reportable leakage. | In the footer, the system shows a message that data is saved successfully. |  |
| 10 | Return to Policy | Choose Back to Compliance Requirement to go back to the previous screen. | The Policy: Tank leakage prevention program screen is displayed. |  |
| 11 | Add Second Paragraph to Policy | On the Policy: Tank leakage prevention program screen: Contents tab, choose Add (+icon) to create a second paragraph within the Tank leakage prevention program compliance requirement record.Make sure that the Tank leakage prevention program row is selected under Paragraph Name to allow the creation of another paragraph within the compliance requirement record. | The Create New Paragraph dialog box is displayed. |  |
| 12 | Edit Paragraph Data | In the Create New Paragraph dialog box, enter or select the following data and then choose OK:Name: Tank inspection after leakageType: Requirement | Paragraph data is updated. |  |
| 13 | Save Paragraph | Choose Save to save the paragraph data. | Paragraph data is saved. |  |
| 14 | Navigate to Paragraph Information | Open the Tank inspection after leakage paragraph. | The Paragraph:<Paragraph name> screen is displayed. |  |
| 15 | Edit Basic Information | On the Compliance Requirement Content Configuration screen under the Basic Information tab, enter the following information in the Requirement Text field and then choose Save:Requirement Text: Due to discovered leakage of 20L or more, perform weekly inspections in the next 4 months to monitor leakage levels. | In the footer, the system shows a message that the data is saved successfully. |  |
| 16 | Return to Policy | Choose Back to Compliance Requirement to go back to the previous screen. | The Policy: Tank leakage prevention program screen is displayed. |  |
| 17 | Save Paragraphs | If both paragraphs are visible under Paragraph Name Tank leakage prevention program, choose Save. | In the footer, the system shows a message that the data is saved successfully. |  |

### Manage Compliance Obligation Assignments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager monitors the compliance status of locations under their responsibility in relation to applicable internal or external requirements. The Environmental Manager assigns a requirement to a location and processes the applicability and status of each underlying requirement paragraph in relation to the assigned location, indicating whether further action is required and setting up tasks if necessary.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Compliance Register (F8632). | The Manage Compliance Register screen is displayed. |  |
| 3 | Create a Compliance Obligation Assignment | Choose Add, enter or select the following data and then choose OK:Locations:Ethanol Storage Tank R2-BB4Compliance Obligations:Tank leakage prevention program | Your compliance obligation assignment is saved, and the search results table is updated with the new entry. |  |
| 4 | Navigate to Compliance Obligation Assignment | Open the Tank leakage prevention program entry under the new Ethanol Storage Tank R2-BB4 section in the results table. | The Tank leakage prevention program screen is displayed. |  |
| 5 | Navigate to a Requirement (Paragraph) | In the Requirements section, under the All Requirements tab, open the Regular internal tank inspections paragraph (requirement). | The Regular internal tank inspections screen is displayed. |  |
| 6 | Set Requirement Applicability | Choose Set Applicability. From the dropdown menu, select Applicable, enter a brief assessment and confirm. | The requirement (paragraph) assignment is set to Applicable for the assigned location. |  |
| 7 | Set Requirement Status | Choose Set Status. From the dropdown menu, select Fulfilled, enter a brief comment and confirm. | The requirement assignment status is set to Fulfilled. |  |
| 8 | Indicate That Action Is Required | Choose Set Action Required. From the dropdown menu, select Yes, enter a brief comment and confirm. | The requirement assignment status is marked as Action Required.Note The entire obligation assignment is also automatically marked as Action Required, as soon as one of its Applicable requirements is set to that status. |  |
| 9 | Navigate Back to Compliance Obligation Assignment | Navigate back to the main compliance obligation assignment page using the Back arrow in the top left of the screen. | The Tank leakage prevention program screen is displayed. |  |
| 10 | Set Obligation Applicability | Choose Set Applicability. From the dropdown menu, select Applicable, enter a brief assessment and confirm. | The obligation assignment is set to Applicable for the assigned location. |  |
| 11 | Set Obligation Status | Choose Set Status. From the dropdown menu, select Fulfilled, enter a brief comment and confirm. | The obligation assignment status is set to Fulfilled. |  |
| 12 | Indicate That No Action Is Required | Choose Clear Action Required. | The obligation assignment status is marked as No Action Required. |  |

### Set Up Compliance Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager plans activities to ensure compliance with applicable requirements by setting up tasks and adding a reference to the identified compliance requirement. This compliance requirement was recorded in the previous test procedure ([Manage Compliance Requirements](#unique_10) [page ] 10). The Environmental Manager adds recurrence to tasks to fulfill the requirements and to manage compliance over time.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Compliance Requirements - Regulations, Permits, Policies (F5038). | The Compliance Requirements screen is displayed. |  |
| 3 | Select Compliance Requirement | On the Compliance Requirements screen under the Recent tab, select the Tank leakage prevention program requirement from the list.Note Alternatively, if the compliance requirement is not in the list under the Recent tab, use the Search tab to find it, and select it. | The Policy: Tank leakage prevention program screen is displayed. |  |
| 4 | Navigate to Task | Note Go to the Policy: Tank leakage prevention program screen: Tasks tab.On the Policy: Tank leakage prevention program screen: Tasks tab, choose Manage Tasks to enter in the Tank leakage prevention program compliance requirement. | The Compliance Requirement Tasks screen is displayed. |  |
| 5 | Add Task | On the Compliance Requirement Tasks screen, choose Create Task to create a task within the Tank leakage prevention program compliance requirement. | The Select Task Type dialog box is displayed. |  |
| 6 | Select Task Type | In the Select Task Type dialog box, select Task from the list. | The Task Definition screen is displayed. |  |
| 7 | Edit Task Definition Data | On the Task Definition screen, under the Task Information tab, enter the following data:Title: internal tank inspectionLocation: Ethanol Storage Tank R2-BB4Owner: Example Environmental Manager userNavigate down to the Assignee Assignment section to select an assignee for the task. You can either select an assignee by business user or location role. To enable more flexibility with the processing of the task, assign it to a location role. This way, the task is routed to everyone with that role for the respective location.Assignment Type of Assignee: Location RoleAssignee: Example Production Operator - EHS Info userNote If some of the fields are not visible, press F5.You can alternatively use the value help to select the applicable Assignee, Owner, and Location entries. | Task data is added. |  |
| 8 | Go to Task Recurrence | While on the Task Definition screen, choose Recurrence to enter in the task recurrence. | The Recurrence dialog box is displayed. |  |
| 9 | Set Task Recurrence | Using the Based on Start Date scheduling mode of the Recurrence dialog box, enter the following information to set the task recurrence and then choose OK:Start Date: <First of May of this calendar year>End Date: <Thirthieth of November of this calendar year>Note Task End Date must be in the future.Recur Every: 1 MonthsOn: Second MondayDue In: 3 Days | Task recurrence is set. |  |
| 10 | Manage References | While on the Task Definition screen, choose Manage References to add reference to the Regular internal tank inspections compliance requirement paragraph, recorded in test procedure [Manage Compliance Requirements](#unique_10) [page ] 10. Select the requirement paragraphs from the list and choose Select. | Reference is updated. |  |
| 11 | Save Changes | On the Task Definition screen, choose Create. | Task is created and assigned for processing. |  |

### Manage Compliance Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager monitors and reschedules tasks, as needed, to meet the requirements and fit the schedule of the team.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Task Calendar (F3840). | The Task Calendar screen is displayed. |  |
| 3 | Find Task | In the calendar view, find the internal tank inspection task instance that you want to reschedule. Switch to the Months calendar view to check all task instances and locate the specific task instance that you want to reschedule more easily.Use the Location filter to narrow down your search to the Ethanol Storage Tank R2-BB4 location. Choose Go. |  |  |
| 4 | Reschedule Task | Reschedule the internal tank inspection task instance for today by using one of the following two options:Drag-and-drop the task instance to the desired start date in the calendar. Make sure that you have switched to the 1 Months view for this. In the Approve confirmation dialog, choose Approve.Open the task instance. In the Task Details dialog box, change the task instance Start Date to <Today’s date>. Choose OK. | The Internal tank inspection task instance is rescheduled for today.As a result, the system generates a workflow item to the assignee’s inbox in the background. This may take up to a few minutes. |  |

### Execute Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Tasks are assigned to, and sent to the inbox of, the Production Operator - EHS Info. After receiving this information, the Production Operator - EHS Info performs the assigned tasks and records the results.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - EHS Info. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open My Inbox - Environment Management (F8329).Note that the app is not available as a tile on the SAP Fiori launchpad. Use the search field or the App Finder to find it. | The My Inbox screen is displayed. |  |
| 3 | Find Task | In the list of tasks, find the internal tank inspection task assigned to you and select it. | The internal tank inspection dialog box is displayed on the right side of the screen. |  |
| 4 | Request More Details | You review the task details but need further instructions how to proceed.Choose Reject in the lower right corner of the screen to return the task to the Owner (the Environmental Manager) for more details. | The Submit Decision dialog box is displayed. |  |
| 5 | Edit Decision Note | In the Submit Decision dialog box, enter the following in the Decision Note field and choose Submit:Please provide a .TXT file with more detailed instructions on how to perform the task. | The task is sent to the Owner’s (Environmental Manager’s) inbox. |  |
| 6 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 7 | Access App | Open My Inbox - Environment Management. | The My Inbox screen is displayed. |  |
| 8 | Find Task | In the list of tasks, find the Handle Rejection of Task: internal tank inspection task assigned to you and select it. | The Handle Rejection: internal tank inspection screen is displayed. |  |
| 9 | Review Task Comments | Choose the Comments icon tab to check the comments added to the task by the Assignee ( Production Operator - EHS Info). |  |  |
| 10 | Add Attachment | Prepare instructions for the Production Operator - EHS Info in a .TXT file.Go to the Attachments icon tab and upload the prepared .TXT file. | A success message is displayed at the bottom of the screen. The attachment is uploaded to the task. |  |
| 11 | Add Comment | Go back to the Comments icon tab. Enter the following information in the Comments field and choose Submit:Instructions are attached.Choose Re-send. | The task is sent back to the Assignee’s ( Production Operator - EHS Info) inbox. |  |
| 12 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - EHS Info. | The SAP Fiori launchpad is displayed. |  |
| 13 | Access App | Open My Inbox - Environment Management.Note that the app is not available as a tile on the SAP Fiori launchpad. Use the search field or the App Finder to find it. | The My Inbox screen is displayed. |  |
| 14 | Check Task Instructions | In the list of tasks, find the internal tank inspection task assigned to you and select it.Check the task instructions provided in the Attachments icon tab. |  |  |
| 15 | Claim Task | Once you have reviewed the instructions, choose Claim in the lower right corner of the screen to start working on the task. | A success message is displayed at the bottom of the screen. |  |
| 16 | Record Results | On the same screen, go to the Comments icon tab and enter the following comment:Leakage was found. | Results from work on task are recorded. |  |
| 17 | Add Attachment | On the same screen, go to the Attachments icon tab and add a protocol (.TXT file) to it. | Attachment from work on task is added. |  |
| 18 | Complete Task | Once you have finished working on the task, choose Completed in the lower right corner of the screen. | Task is marked as completed. |  |

### Monitor Compliance Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager Environmental Manager monitors task execution. This helps the Environmental Manager to identify related issues and initiate actions to manage them, such as creating and managing deviations, rescheduling or reassignment of ongoing tasks.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Monitor Tasks (F2527). | The Monitor Tasks screen is displayed. |  |
| 3 | Find Task | In the list of tasks, find and open the internal tank inspection task instance which is in status Completed.Note You can use the filter options to tailor your search and find the task instance more easily. You can search by task Start Date, Due Date, Completion Date, Status, Owner, Current Processor, Priority, Origin Type, Location. Once you have entered the data relevant for your search, choose Go. | The Task Instance screen is displayed. |  |
| 4 | Verify Task Details | On the Task Instance screen under the Comments section, verify that the comment entered in the previous test procedure ([Execute Tasks](#unique_13) [page ] 17) about this task is visible:Leakage was found.On the same screen under the Attachments section, verify that the attached file in the previous test procedure ([Execute Tasks](#unique_13) [page ] 17) is visible. |  |  |
| 5 | Create Deviation | Due to the leakage found, create a deviation. To do this, go to the upper right corner of the screen and choose Create Deviation. | The Create Deviation Incident dialog box is displayed. |  |
| 6 | Enter Deviation Information | In the Create Deviation Incident dialog box, enter the following information and choose Create:Title: internal tank inspection - leakage foundStart Date: same start date as the start date of the rescheduled internal tank inspection task instance in test step 4 of process step Manage Compliance TasksEnd Date: <Second of December of this calendar year>Follow Up Category: Issue FoundDescription of Events: During regular inspection of Ethanol Storage Tank R2-BB4, leakage was reported from valve 3.Note The relevant compliance requirement and location should appear in the dialog box automatically. | A success message is displayed at the bottom of the screen. The deviation is created. |  |
| 7 | Create New Task | Due to the leakage found, create a new task for inspection.To do this, open Manage Compliance Requirements - Regulations, Permits, Policies (F5038). | The Manage Compliance Requirements screen is displayed. |  |
| 8 | Select Compliance Requirement | On the Compliance Requirements screen under the Recent tab, select the Tank leakage prevention program requirement from the list.Note Alternatively, if the compliance requirement is not in the list under the Recent tab, use the Search tab to find it, and select it. | The Policy: Tank leakage prevention program screen is displayed. |  |
| 9 | Navigate to Create Task | Note Go to the Policy: Tank leakage prevention program screen: Contents tab.On the Policy: Tank leakage prevention program screen: Contents tab, select the Tank inspection after leakage paragraph entry. Then, choose Create Task from the Content section toolbar. | The Select Task Type dialog box is displayed. |  |
| 10 | Select Task Type | In the Select Task Type dropdown list, select Task from the list. | The Task Definition screen is displayed. |  |
| 11 | Edit Task Definition Data | On the Task Definition screen, under the Task Information tab, enter the following data:Title: leakage monitoring inspectionLocation: Ethanol Storage Tank R2-BB4Owner: Example Environmental Manager userNavigate down to the Assignee Assignment section to select an assignee for the task. You can either select an assignee by business user or location role. To enable more flexibility with the processing of the task, assign it to a location role. This way, the task is routed to everyone with that role for the respective location.Assignment Type of Assignee: Location RoleAssignee: Example Production Operator - EHS Info userNote If some of the fields are not visible, press F5.You can alternatively use the value help to select the applicable Assignee, Owner, and Location entries. | Task data is added. |  |
| 12 | Go to Task Recurrence | While on the Task Definition screen, choose Recurrence to enter in the task recurrence. | The Recurrence dialog box is displayed. |  |
| 13 | Set Task Recurrence | Using the Based on Start Date scheduling mode of the Recurrence dialog box, enter the following information to set the task recurrence and then choose OK:Start Date: set to <Today's date>End Date: <4 Months after Start Date>Note Task End Date must be in the future.Recur Every: 1 WeeksOn: First MondayDue In: 4 Months | Task recurrence is set. |  |
| 14 | Check References | While on the Task Definition screen, check that the reference to the Tank inspection after leakage paragraph appears automatically under References. | Reference is updated. |  |
| 15 | Save Changes | On the Task Definition screen, choose Create. | Data changes are saved. |  |
| 16 | Log Off | Log out of the system from your current user. | The logoff screen is displayed. |  |
| 17 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - EHS Info. | The SAP Fiori launchpad is displayed. |  |
| 18 | Access App | Open My Inbox - Production Operator (F8329).Note that the app is not available as a tile on the SAP Fiori launchpad. Use the search field or the App Finder to find it. | The My Inbox screen is displayed. |  |
| 19 | Find Task | In the list of tasks, find the leakage monitoring inspection task assigned to you and select it. | The internal tank inspection dialog box is displayed on the right side of the screen. |  |
| 20 | Claim Task | Review the details and claim the task.Choose Claim in the lower right corner of the screen to claim the task to your business user. You are now the task's Current Processor. | The task status (in the upper right corner of the screen) changes from Ready to Reserved. |  |
| 21 | Log Off | Log out of the system from your current user. | The logoff screen is displayed. |  |
| 22 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 23 | Access App | Open the Monitor Tasks app. | The Monitor Tasks screen is displayed. |  |
| 24 | Select Tasks to Forward | In the list of tasks, find the leakage monitoring inspection task instance which is in status Due, Overdue, or Scheduled. Select the checkbox in front of it. | The leakage monitoring inspection task is selected. |  |
| 25 | Forward Task | Choose Forward to change the Current Processor of the task instance. | The Forward Tasks dialog box is displayed. |  |
| 26 | Select Next Processor | Use the value help of the Forward to Processor field to select a user to forward the selected task instance to. You can use the value help to locate the user more easily. Double-click on the user entry to confirm your selection. | The desired user is populated in the Forward to Processor field. |  |
| 27 | Confirm Selection | Choose OK to confirm your selection. | The leakage monitoring inspection task instance is forwarded.Note Where relevant, you can forward multiple task instances at once. |  |

### Manage Deviations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Environmental Manager creates a deviation incident based on identified issues in the previous test procedure ([Monitor Compliance Tasks](#unique_14) [page ] 19). Then, the Environmental Manager investigates the deviation and initiates preventive and corrective measures as tasks assigned to the deviation.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Environmental Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Deviation Incidents (WDA0449). | The Manage Deviation Incidents (WDA0449) screen is displayed. |  |
| 3 | Find Deviation | Under the Recent tab, select the internal tank inspection - leakage found deviation created in test procedure [Monitor Compliance Tasks](#unique_14) [page ] 19 from the list. | The Edit Incident Deviation screen is displayed. |  |
| 4 | Check Triggering Task to the Deviation | Navigate to the Deviation tab.Under the Deviation Information section, go to the Triggering Tasks tab.Verify that the triggering task for the deviation is automatically displayed. |  |  |
| 5 | Navigate to the Tasks Tab | On the same screen, navigate to the Tasks tab. Confirm the warning message. Once under the Taskstab, choose Manage Tasks. | The Incident Tasks screen is displayed. |  |
| 6 | Add Task | On the Incident Tasks screen, choose Add Task to create a task within the internal tank inspection - leakage found deviation. | The Select Task Type dialog box is displayed. |  |
| 7 | Select Task Type | In the Select Task Type dialog box, select Maintenance Notification from the list. | The Task Definition screen is displayed. |  |
| 8 | Edit Task Definition Data | On the Task Definition screen, under the Task Information tab, enter the following data:Title: Valve 3 to be replacedOwner: Environmental Manager userApprover: Environmental Manager userDescription: Due to leakage reported, Valve 3 has to be replaced.Note If some of the fields are not visible, press F5.You can alternatively use the value help to select the applicable Owner and Approver entries. | Task data is added. |  |
| 9 | Select Notification Type | On the same screen, under the Notification Information section, select one of the available options that you have previously specified in [Preliminary Configuration](#unique_4) [page ] 3. If there are no notification types specified, skip this and the following steps. | If available, the notification type is selected. |  |
| 10 | Create Task | On the same screen, choose Create. | Data changes are saved and task is created. |  |

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
> Flagged while digesting this document, not verified: The My Inbox - Environment Management app is given as F0862 in the Overview Table but as F8329 in the Execute Tasks and Monitor Compliance Tasks procedures.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/test-script-emissions-management-4xd-sap-s-4hana-cloud-public-edition]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4C8_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 48,853 chars in the whole document
