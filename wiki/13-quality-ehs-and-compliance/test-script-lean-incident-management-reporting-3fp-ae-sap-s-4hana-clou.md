---
id: 13-quality-ehs-and-compliance/test-script-lean-incident-management-reporting-3fp-ae-sap-s-4hana-clou
title: "Test Script: Lean Incident Management Reporting (3FP_AE) - SAP S/4HANA Cloud Public Edition (3FP_S4CLD2608_BPD_EN_AE)"
description: "SAP test script (scope item 3FP, release 2608) for incident, near miss and safety observation reporting, investigations, tasks, OSHA/BG reports and workplace safety."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-incident-management]
aliases: [3FP_S4CLD2608_BPD_EN_AE]
keywords: [EHS Incident Management, incident reporting, incident management, near miss, safety observation, incident investigation, incident tasks, regulatory reports, osha electronic submission, workplace safety overview]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3FP_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-934
topic: 13-quality-ehs-and-compliance/ehs-incident-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Lean Incident Management Reporting (3FP_AE) - SAP S/4HANA Cloud Public Edition (3FP_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3FP_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **EHS Incident Management** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Lean Incident Management Reporting (3FP_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852453)

[2 Prerequisites 4](#_Toc232852454)

[2.1 System Access 4](#_Toc232852455)

[2.2 Preliminary Configuration 4](#_Toc232852456)

[2.2.1 Specify Notification Types 4](#_Toc232852457)

[2.3 Roles 6](#_Toc232852458)

[2.4 Master Data, Organizational Data, and Other Data 6](#_Toc232852459)

[2.5 Additional Manual Configuration 7](#_Toc232852460)

[2.6 Business Conditions 8](#_Toc232852461)

[2.7 Preliminary Steps 8](#_Toc232852462)

[3 Overview Table 9](#_Toc232852463)

[4 Test Procedures 12](#_Toc232852464)

[4.1 Capture an Initial Incident Record 12](#_Toc232852465)

[4.2 Process an Incident 17](#_Toc232852466)

[4.2.1 Review and Complete an Incident 17](#_Toc232852467)

[4.2.1.1 Search for Incidents 17](#_Toc232852468)

[4.2.1.2 Open an Incident 19](#_Toc232852469)

[4.2.1.3 Manage Details 21](#_Toc232852470)

[4.2.1.4 Manage Location 24](#_Toc232852471)

[4.2.1.5 Manage People 25](#_Toc232852472)

[4.2.1.5.1 Enter Details for All Persons 26](#_Toc232852473)

[4.2.1.5.2 Enter Details for Persons with Special Roles 28](#_Toc232852474)

[4.2.1.5.3 Enter Health Information 32](#_Toc232852475)

[4.2.1.5.4 Enter Influences on Health and Safety 34](#_Toc232852476)

[4.2.1.6 Manage Assets 37](#_Toc232852477)

[4.2.1.7 Manage Releases 40](#_Toc232852478)

[4.2.1.8 Manage Notices of Violation 42](#_Toc232852479)

[4.2.1.9 Manage Financial Tracking 43](#_Toc232852480)

[4.2.1.10 Manage Documents 45](#_Toc232852481)

[4.2.1.11 Review and Complete an Incident (Optional Steps) 46](#_Toc232852482)

[4.2.1.11.1 Manage a Near Miss 46](#_Toc232852483)

[4.2.1.11.2 Manage a Safety Observation 47](#_Toc232852484)

[4.2.1.11.3 Change the Status of an Incident Record 48](#_Toc232852485)

[4.2.1.11.4 Change the Category of an Incident Record 48](#_Toc232852486)

[4.2.2 Create an Investigation 49](#_Toc232852487)

[4.2.3 Create and Send an Incident Report 51](#_Toc232852488)

[4.2.4 Define and Manage Tasks 54](#_Toc232852489)

[4.2.4.1 Define a Task 54](#_Toc232852490)

[4.2.4.2 Edit a Task 57](#_Toc232852491)

[4.2.4.3 Implement a Task 58](#_Toc232852492)

[4.2.4.4 Reject a Task with Approval 59](#_Toc232852493)

[4.2.4.5 Create and Complete a Maintenance Notification Task 60](#_Toc232852494)

[4.2.4.6 Create and Complete a Change Request Task 62](#_Toc232852495)

[4.2.4.7 Monitor Tasks 63](#_Toc232852496)

[4.2.4.8 Manage Tasks in a Calendar View 65](#_Toc232852497)

[4.2.5 Close an Incident Record 66](#_Toc232852498)

[4.3 Process an Investigation 67](#_Toc232852499)

[4.4 Review Workplace Safety Data 70](#_Toc232852500)

[4.5 Additional Process Steps (Optional) 71](#_Toc232852501)

[4.5.1 Create Incident by Category 71](#_Toc232852502)

[4.5.2 Manage Hours Worked 73](#_Toc232852503)

[4.5.3 Manage Summary Reports 74](#_Toc232852504)

[4.5.4 Manage Injury/Illness Log 76](#_Toc232852505)

[4.5.5 Manage Electronic Submissions of Injury and Illness Data to OSHA (USA) 78](#_Toc232852506)

## Purpose

Overview

You can use this scope item to record and process incidents, safety observations, and near misses. After initial recording, you can collect additional information about the people involved and damaged assets. You can attach related documents, investigate why an incident occurred, and define tasks for prevention of further incidents. You can report data to the relevant authorities to meet legal requirements. In addition, you can perform comprehensive analyses of incidents and injuries/illnesses.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/3FP_S4CLD2602_BPD_EN_AE.docx) ). |

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Preliminary Configuration

Purpose

Some of the process steps in the current test script depend on configurations that are not included in the standard Cloud Best Practices content delivery of predefined configurations. To be able to perform these process steps, additional manual configurations are required. They are described in the following procedures.

#### Specify Notification Types

Purpose

In this activity, you can specify notification types to use for the creation of maintenance notification tasks.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT). |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. | You are navigated to the Configure Your Solution app. |  |
| 4 | Go to Specify Notification Types | On the Configure Your Solution screen, search for the following configuration step: Specify Notification Types (SSCUI ID 105888). Choose Go.In the search result, select the configuration item and go to the next screen.On the Configure Your Solution – Foundation for Environment, Health, and Safety screen, go to the configuration step Specify Notification Types (SSCUI ID 105888) and choose Configure. | The Specify Notification Types screen is displayed. |  |
| 5 | Specify Notification Types | If there are no available entries, create at least one entry. Use the value help to select from all available notification types in the system. For example, Y1: Reactive Work. Confirm your selection.Note It is possible that this configuration contains no records and also, no notification types are available in the system. In this case, you can skip this configuration step. | If available, the notification type is selected. |  |
| 6 | Save | Choose Save. | The notification type is saved. |  |

SAP Central Business Configuration:

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access App | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Specify Notification Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Specify Notification Types screen is displayed. |  |
| 3 | Specify Notification Types | If there are no available entries, create at least one entry. Use the value help to select from all available notification types in the system. For example, Y1: Reactive Work. Confirm your selection.Note It is possible that this configuration contains no records and also, no notification types are available in the system. In this case, you can skip this configuration step. | If available, the notification type is selected. |  |
| 4 | Save | Choose Save. | The notification type is saved. |  |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration (role necessary for preliminary configuration) | SAP_BR_BPC_EXPERT |  |  |  |
| Employee - EHS Info (incident reporting person) | SAP_BR_EMPLOYEE_EHS_INFO |  |  |  |
| Industrial Hygienist (incident manager) | SAP_BR_INDUSTRIAL_HYGIENIST | Workplace Safety | SAP_BR_INDUSTRIAL_HYGIENIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Location | Division ABC | Location of type Company. Parent location for all other sample locations. |  |
| Location | Tank Area | Location of type Site. Sublocation of Division ABC. |  |
| Location | Ethanol Storage Tank R5-BB7 | Location of type Storage Location. Sublocation of Tank Area. |  |
| Location | Ethanol Storage Tank R6-BB9 | Location of type Storage Location. Sublocation of Tank Area. |  |

Note that there are no responsible persons (with the Incident Manager role) assigned to any location as part of the sample master data. The responsible person with the Incident Manager role receives the work items to review and complete incidents, near misses, and safety observations. If there are no responsible persons with the Incident Manager role assigned to any location, when you report a new incident, near miss, or safety observation, the lifecycle workflow goes to status Error. If you have not set a person responsible for the location of the incident, follow the steps described in the [Preliminary Steps](#unique_8) [page ] 8 chapter to do so.

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 3SR | Create EHS Location - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/23070e4420319897cd58747939ef938a)

### Business Conditions

This scope item has no business conditions.

### Preliminary Steps

Purpose

Before you begin with the test procedures, make sure you complete the steps below.

Procedure

1. Log on to the SAP Fiori launchpad.
2. If the Manage Locations (EHFND_UI_LOC_ENTRY) tile is not available on your SAP Fiori launchpad home screen, add it via the App Finder.

|  |
| --- |
| Note To add a tile to your SAP Fiori launchpad home screen, go to your profile in the upper right corner of the screen. Select the Edit Current Page option from the list. Then, choose Add Tile in the desired section to go to the App Finder. In the Search field on the upper right side of the screen, enter the name of the app you want to add to your SAP Fiori launchpad, and press Enter. The app appears in your search results. Select the plus sign to add the app tile to your SAP Fiori launchpad home screen. In the footer, the system shows a message that the tile has been added successfully. To exit edit mode, go back to your SAP Fiori launchpad home screen and select the Exit Edit Mode option from the list under your profile. |

1. Open the Manage Locations (EHFND_UI_LOC_ENTRY) app.
2. Navigate to the Structure View tab.
3. Select the Division ABC location and choose the hyperlink.
4. Navigate to the Persons Responsible tab.
5. Add your user as a person responsible with the Incident Manager role.
6. Save your entries.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Capture an Initial Incident Record](#unique_12) [page ] 12 | Employee - EHS Info | Report Incident (F1992) | An initial incident record is created in the system. |
| Process an Incident |  |  |  |
| Review and Complete an Incident | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident | All necessary data is added to the incident record. |
| [Search for Incidents](#unique_13) [page ] 17 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) |  |
| [Open an Incident](#unique_14) [page ] 19 | Industrial Hygienist | Manage Incidents - Incident Management (F4759)My Inbox - Incident Management (F7992)Monitor Incident Work Items (F6217) |  |
| [Manage Details](#unique_15) [page ] 21 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident |  |
| [Manage Location](#unique_16) [page ] 24 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident |  |
| [Manage People](#unique_17) [page ] 25[Enter Details for All Persons](#unique_18) [page ] 26[Enter Details for Persons with Special Roles](#unique_19) [page ] 28[Enter Health Information](#unique_20) [page ] 32[Enter Influences on Health and Safety](#unique_21) [page ] 34 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident |  |
| [Manage Assets](#unique_22) [page ] 37 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident |  |
| [Manage Releases](#unique_23) [page ] 40 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident |  |
| [Manage Notices of Violation](#unique_24) [page ] 42 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident |  |
| [Manage Financial Tracking](#unique_25) [page ] 43 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident |  |
| [Manage Documents](#unique_26) [page ] 45 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident |  |
| Review and Complete an Incident (optional steps)[Manage a Near Miss](#unique_27) [page ] 46[Manage a Safety Observation](#unique_28) [page ] 47[Change the Status of an Incident Record](#unique_29) [page ] 48[Change the Category of an Incident Record](#unique_30) [page ] 48 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident |  |
| [Create an Investigation](#unique_31) [page ] 49 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident | An investigation is created. |
| [Create and Send an Incident Report](#unique_32) [page ] 51 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident | A regulation-specific report is generated and sent to the relevant authority. |
| Define and Manage Tasks | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident > Manage Incident Tasks (F3091) | Tasks are defined and scheduled for implementation. |
| [Define a Task](#unique_33) [page ] 54 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident > Manage Incident Tasks (F3091) > Task Definition (F2528) |  |
| [Edit a Task](#unique_34) [page ] 57 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident > Manage Incident Tasks (F3091) > Task Definition (F2528) |  |
| [Implement a Task](#unique_35) [page ] 58 | Industrial Hygienist | My Inbox - Incident Management (F7992) |  |
| [Reject a Task with Approval](#unique_36) [page ] 59 | Industrial Hygienist | My Inbox - Incident Management (F7992) |  |
| [Create and Complete a Maintenance Notification Task](#unique_37) [page ] 60 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident > Manage Incident Tasks (F3091) > Task Definition Maintenance Notification (F3359) |  |
| [Create and Complete a Change Request Task](#unique_38) [page ] 62 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident > Manage Incident Tasks (F3091) > Task Definition Change Request (F3415) |  |
| [Monitor Tasks](#unique_39) [page ] 63 | Industrial Hygienist | Monitor Tasks (F2527) |  |
| [Manage Tasks in a Calendar View](#unique_40) [page ] 65 | Industrial Hygienist | Task Calendar (F3840) |  |
| [Close an Incident Record](#unique_41) [page ] 66 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) > Edit Incident | All activities related to the incident are completed and the incident is closed in the system. |
| [Process an Investigation](#unique_42) [page ] 67 | Industrial Hygienist | Manage Investigations (F7969) | An investigation is planned, processed, and closed. |
| [Review Workplace Safety Data](#unique_43) [page ] 70 | Industrial Hygienist | Workplace Safety Overview (F7512) | An overview of incidents, near misses, and safety observations and the related tasks. |
| Additional Process Steps (optional) |  |  |  |
| [Create Incident by Category](#unique_44) [page ] 71 | Industrial Hygienist | Manage Incidents - Incident Management (F4759) | An incident record with detailed data is created. |
| [Manage Hours Worked](#unique_45) [page ] 73 | Industrial Hygienist | Manage Hours Worked - Incident Management (F3372) | Hours worked are added for different locations. |
| [Manage Summary Reports](#unique_46) [page ] 74 | Industrial Hygienist | Manage Summary Reports - Incident Management (F4758) | Incident summary reports are generated for legal purposes. |
| [Manage Injury/Illness Log](#unique_47) [page ] 76 | Industrial Hygienist | Create Injury/Illness Log Entry (EHHSS_INC_REC_OIF_V3)Manage Injury/Illness Log (F4026) |  |
| [Manage Electronic Submissions of Injury and Illness Data to OSHA (USA)](#unique_48) [page ] 78 | Industrial Hygienist | Manage Electronic Submissions (F8152) | Injury and illness data is reported electronically. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Capture an Initial Incident Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident happened and an employee (Employee - EHS Info) reports it in the system.

Procedure

Report an Incident

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Employee - EHS Info. |  |  |
| 2 | Access App | Open Report Incident (F1992). | The Report Incident screen is displayed. All incidents reported by you are listed in the Incidents section on the left. |  |
| 3 | Create an Incident | Choose New (+ icon) and select the New Incident option. | An empty New Incident template is displayed. |  |
| 4 | Enter a Description | In the New Incident section, in the What happened? field, enter <incident title text> to describe the incident. | The <incident title text> is populated in the field. |  |
| 5 | Specify Immediate Actions | In the Immediate Actions field, describe the actions that were taken immediately after the incident occurred. | The Immediate Actions field is updated. |  |
| 6 | Add a Picture | Choose Add a Photo (camera icon).Browse and select a picture that is relevant for the incident. | The selected picture is previewed. |  |
| 7 | Enter the Date and Time of the Incident | In the When did it happen? field, select <17.02.2020, 15:00 (3 PM)> via the date and time picker and choose OK. | The selected date and time are populated in the field. |  |
| 8 | Enter a Location | In the Where did it happen? field, enter Division ABC via the value help. | The location Division ABC is populated in the field. |  |
| 9 | Enter Location Information | In the field below the selected location, enter <location text> to add more details for the selected location. | The <location text> is populated in the field. |  |
| 10 | Add Injured Persons | In the Was anyone injured? field, select the option Yes. | The option Yes is selected and a text field for the name of the injured person appears.The Add Another Injured Person button is displayed. |  |
| 11 | Assign Injured Persons | In the field below the selected option, use the value help to select a person that exists in the system. You can search for existing business users by multiple criteria.Choose Add Another Injured Person to add another injured person.Note Alternatively, you can type in the injured person's name. A preliminary person is created on the incident record level. The initial person is stored locally and is not created as a business user.In the [Review and Complete an Incident](#unique_50) [page ] 17 process step, you need to find the corresponding existing business user in the system and replace the initial person with this business user. | The <names of the injured persons> are populated in the fields. |  |
| 12 | Add Witnesses | In the Were there any witnesses? field, select the option Yes. | The option Yes is selected and a text field for the name of the witness appears.The Add Another Witness button is displayed. |  |
| 13 | Assign Witnesses | In the field below the selected option, use the value help to select a person that exists in the system. You can search for existing business users by multiple criteria.Choose Add Another Witness to add another witness.Note Alternatively, you can type in the person's name. A preliminary person is created on the incident record level. The initial person is stored locally and is not created as a business user.In the [Review and Complete an Incident](#unique_50) [page ] 17 process step, you need to find the corresponding existing business user in the system and replace the initial person with this business user. | The <names of the witnesses> are populated in the fields. |  |
| 14 | Add Damaged Equipment | In the Was anything damaged? field, select the option Yes. | The option Yes is selected and a text field for the description of the damaged equipment appears. |  |
| 15 | Specify the Damaged Equipment | In the field below the selected option, enter a description of the damaged equipment as a free text. | The entered value is populated in the field.After sending the incident information, this value is added to the incident record as Equipment Description. |  |
| 16 | Add a Release | In the Was any material released? field, select the option Yes. | The option Yes is selected, and more fields are displayed below for additional information. |  |
| 17 | Enter Release Information | In the newly displayed fields, enter the following additional information:Release TypeReleased MaterialReleased AmountUnit of Measurement | The entered values are populated in the fields.After sending the incident information, the release is added to the incident record under the Releases tab. |  |
| 18 | Send Data | Choose Send. | A new incident of category Incident is created in the system.The new incident appears on top of the list in the Incidents section on the left. |  |

Report a Near Miss

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Employee - EHS Info. |  |  |
| 2 | Access App | Open Report Incident (F1992). | The Report Incident screen is displayed. All incidents reported by you are listed in the Incidents section on the left. |  |
| 3 | Create a Near Miss | Choose New (+ icon) and select the New Near Miss option. | An empty New Near Miss template is displayed. |  |
| 4 | Report Anonymously | Select the Report Anonymously checkbox. | When you select the Report Anonymously checkbox, no information about the reporting person is included in the near miss record. |  |
| 5 | Enter a Description | In the New Near Miss section, in the What happened? field, enter <near miss title text> to describe the near miss. | The <near miss title text> is populated in the field. |  |
| 6 | Add a Picture | Choose Add a Photo (camera icon).Browse and select a picture that is relevant for the near miss. | The selected picture is previewed. |  |
| 7 | Enter the Date and Time of the Near Miss | In the When did it happen? field, select <17.02.2020, 15:00 (3 PM)><safety observation title text> via the date and time picker and choose OK. | The selected date and time are populated in the field. |  |
| 8 | Enter a Location | In the Where did it happen? field, enter Division ABC via the value help. | The location Division ABC is populated in the field. | < |
| 9 | Enter Location Information | In the field below the selected location, enter <location text> to add more details for the selected location. | The <location text> is populated in the field. |  |
| 10 | Add Nearly Injured Persons | In the Was anyone nearly injured? field, select the option Yes. | The option Yes is selected and a text field for the name of the nearly injured person appears.The Add Another Nearly Injured Person button is displayed. |  |
| 11 | Assign Nearly Injured Persons | In the field below the selected option, use the value help to select a person that exists in the system.Choose Add Another Nearly Injured Person to add another injured person. | The <names of the nearly injured persons> are populated in the fields. |  |
| 12 | Add Circumstances | In the Do you know about the circumstances? field, select the option Yes.In the field Select one or more circumstances, select any of the available options.Describe the situation in the Situation Description field.Describe the cause in the Cause field.In the field What is the risk of these circumstances causing an injury or incident in the future? select any of the available options. | Your entries are populated in the fields Select one or more circumstances, Situation Description, Cause, and What is the risk of these circumstances causing an injury or incident in the future?. |  |
| 13 | Send Data | Choose Send. | A new incident of category Near Miss is created in the system.The new incident appears on top of the list in the Incidents section on the left. |  |

Report a Safety Observation

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Employee - EHS Info. |  |  |
| 2 | Access App | Open Report Incident (F1992). | The Report Incident screen is displayed. All incidents reported by you are listed in the Incidents section on the left. |  |
| 3 | Create a Safety Observation | Choose New (+ icon) and select the New Safety Observation option. | An empty New Safety Observation template is displayed. |  |
| 4 | Report Anonymously | Select the Report Anonymously checkbox. | When you select the Report Anonymously checkbox, no information about the reporting person is included in the safety observation record. |  |
| 5 | Enter a Description | In the New Safety Observation section, in the What happened? field, enter <safety observation title text> to describe the safety observation. | The <safety observation title text> is populated in the field. |  |
| 6 | Add a Picture | Choose Add a Photo (camera icon).Browse and select a picture that is relevant for the safety observation. | The selected picture is previewed. |  |
| 7 | Enter the Date and Time of the Safety Observation | In the When did it happen? field, select <17.02.2020, 15:00 (3 PM)> via the date and time picker and choose OK. | The selected date and time are populated in the field. |  |
| 8 | Enter a Location | In the Where did it happen? field, enter Division ABC via the value help. | The location Division ABC is populated in the field. |  |
| 9 | Enter Location Information | In the field below the selected location, enter <location text> to add more details for the selected location. | The <location text> is populated in the field. |  |
| 10 | Add Observed Persons | In the Was anyone observed? field, select the option Yes. | The option Yes is selected and a text field for the name of the injured person appears.The Add Another Observed Person button is displayed. |  |
| 11 | Assign an Observed Person | In the field below the selected option, use the value help to select a person that exists in the system.Choose Add Another Observed Person to add another observed person. | The <names of the observed persons> are populated in the fields. |  |
| 12 | Add Circumstances | In the Do you know about the circumstances? field, select the option Yes.In the field Select one or more circumstances, select any of the available options.Describe the situation in the Situation Description field.In the field What is the risk of these circumstances causing an injury or incident in the future? select any of the available options. | Your entries are populated in the fields Select one or more circumstances, Situation Description, and What is the risk of these circumstances causing an injury or incident in the future?. |  |
| 13 | Send Data | Choose Send. | A new incident of category Safety Observation is created in the system.The new incident appears on top of the list in the Incidents section on the left. |  |

### Process an Incident

This section contains test procedures for processing incidents.

#### Review and Complete an Incident

This section contains process steps that allow you to add relevant information and complete the incident.

##### Search for Incidents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager (Industrial Hygienist) searches for incidents, near misses, and safety observations that have been reported in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. |  |  |
| 2 | Access App | Open Manage Incidents - Incident Management (F4759). | The Manage Incidents screen is displayed.In the filter area, a free-text search field and the following filters are available:Incident CategoryDateLocationInclude SublocationsInvolved PersonGroupStatus |  |
| 3 | Search for Incidents by Title | In the Search field, enter part of the <incident title text>.Choose Go.Note In the Search field, you can also search by incident ID and location name. | All incident records that match the search criteria are displayed in the results table.You can navigate to an incident by choosing the corresponding row. |  |
| 4 | Search for Incidents by Category | In the Incident Category field, select Incident from the dropdown list.Choose Go. | All incident records that match the search criteria are displayed in the results table.You can navigate to an incident by choosing the corresponding row. |  |
| 5 | Search for Incidents by Date | In the Date field, use the value help to select <17.02.2020>.Choose Go. | All incident records that match the search criteria are displayed in the results table.You can navigate to an incident by choosing the corresponding row. |  |
| 6 | Search for Incidents by Location | In the Location field, open the value help.On the Structure View tab, navigate to and select the Division ABC location in the location hierarchy.Choose OK to confirm your selection in the value help.Choose Go to search for incidents.Note Alternatively, under the Search Location tab of the value help, you can also search for the Division ABC location by entering the name in the Search field. | All incident records that match the search criteria are displayed in the results table.You can navigate to an incident by choosing the corresponding row. |  |
| 7 | Search for Incidents by Status | In the Status field, the following statuses are preselected: Closed, In Process, New, and Reopened.Deselect the checkboxes for all preselected statuses except New.Choose Go to search for incidents. | All incident records that match the search criteria are displayed in the results table.You can navigate to an incident by choosing the corresponding row. |  |
| 8 | Search for Incidents by Involved Person | In the Involved Person field, open the value help.In the First Name and Last Name fields, enter the corresponding name of a person and choose Go to search.Select the person from the results.Choose Go to search for incidents. | All incident records that match the search criteria are displayed in the results table.You can navigate to an incident by choosing the corresponding row. |  |
| 9 | Search for Incidents by Group | In the Group field, select Injury / Illness from the dropdown list.Choose Go. | All incident records that match the search criteria are displayed in the results table.You can navigate to the desired incident by choosing the corresponding row. |  |
| 10 | Search for Incidents by Additional Criteria | In the filter area, choose Adapt Filters.Select one or more additional search criteria, for example ID, Country/Region, and Plant ID.Choose OK.Enter data in the newly added filters and choose Go to search for incidents. | The selected filters are added to the filter area.All relevant incidents are displayed in the results table.You can navigate to an incident by choosing the corresponding row. |  |

##### Open an Incident

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Open an incident, near miss, or safety observation via the Manage Incidents - Incident Management (F4759), My Inbox - Incident Management (F7992), or Monitor Incident Work Items (F6217) app.

Procedure

Open an incident via the Manage Incidents - Incident Management (F4759) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. |  |  |
| 2 | Access App | Open Manage Incidents - Incident Management (F4759). | The Manage Incidents screen is displayed. |  |
| 3 | Find an Incident | In the Search field, enter <incident title text> and choose Go. | The newly reported incident is displayed in the results list. |  |
| 4 | Open the Incident | Choose the <incident title text> row in the results list to navigate to the incident record. | The incident <incident title text> is loaded. |  |

Open an Incident via the My Inbox - Incident Management (F7992) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. |  |  |
| 2 | Access App | Open My Inbox - Incident Management (F7992). | The My Inbox screen is displayed. |  |
| 3 | Find an Incident | In the Search field, enter the incident title or part of it. | The work item list is reduced to the relevant Review and Complete Incident work items that match the search criteria. |  |
| 4 | Open the Incident | Select the work item from the results list.Choose Open Task. | The incident <incident title text> is loaded.Note For incidents of category Near Miss or Safety Observation, find the corresponding work items in the list and open their tasks. |  |

Open an Incident via the Monitor Incident Work Items (F6217) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. |  |  |
| 2 | Access App | Open Monitor Incident Work Items (F6217). | The Process Incident Work Items screen is displayed. |  |
| 3 | Find an Incident | In the smart filter bar, make the following entries:Search: <incident title or part of it>Type: Review and Complete Incident | The work item list is reduced to the relevant Review and Complete Incident work items that match the search criteria. |  |
| 4 | Open the Incident | Select the work item from the results list. | The incident <incident title text> is loaded. |  |

##### Manage Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The responsible incident manager (Industrial Hygienist) enters additional details about the incident.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed.Note The Details tab is available for all incident categories. |  |
| 2 | Change Classification | In the header toolbar, choose Classification.In the Classification dialog box, select the checkbox for the Notice of Violation group and 2 - Medium in the Severity Level dropdown list.Choose OK. | In the Classification dialog box, the groups Injury / Illness and Release (detected at the initial reporting), are selected and read-only.At confirming the Classification dialog box, the Notice of Violation group is added and displayed in the Classification field in the header. |  |
| 3 | Select Regulations | In the header toolbar, choose Regulations.Select the checkbox for the OSHA (USA) regulation. Alternatively, select a regulation that is relevant for your region.Choose OK. | The selected regulations are displayed in the Regulations field in the header. |  |
| 4 | Set Restricted Access | In the header toolbar, choose Restrict Data Access.For the Basic Information page, select No from the Restricted Access dropdown menu.Choose OK. | The option is set. |  |
| 5 | Change Data in the Description Section | In the Event section, under Description:Change the text in the Title field (initially populated with <incident title text> ).Change the text in the Description of Events field (initially populated with <incident title text> ).Choose Translate below the Description of Events field and add translations of the text for different languages.Set the option Emergency Responder Called to Yes.Change the text in the Immediate Actions field (initially populated with the information entered during incident reporting).Choose Translate below the Immediate Actions field and add translations of the text for different languages. | The texts for all fields are changed.Translations are added for Description of Events and Immediate Actions.The Emergency Responder Called option is set.Note This option is relevant and therefore visible for the OSHA (USA) regulation only. |  |
| 6 | Change Reporting Date and Time | In the Event section under Description, the Reporting Date / Time fields are populated with data from the initial reporting.Change the Date / Time fields via the corresponding value help options. | The fields are updated. |  |
| 7 | Replace the Reporting Person | In the Event section under Description, the Reporting Person field is retrieved from the initial reporting.Open the value help and search for a <person> by one or more search criteria. Select a record to assign it as Reporting Person. | The selected <person> is assigned as Reporting Person. |  |
| 8 | Display Details About the Reporting Person | In the Event section under Description, choose the Details link for the Reporting Person field. | A Person Details dialog box displays data about the person in the following sections: Person/Organization, Street Address, Communication, and Organizational Assignment. |  |
| 9 | Change Date and Time | In the Event section, under Date and Time:Change the date in the Date / Time / Time Zone field from <17.02.2020> to <14.02.2020>.Change the time manually. Keep the same time format.Change the time zone using the value help.Save your entries. | The date and time are saved in the corresponding fields and updated in the page header. |  |
| 10 | Set Time Unknown | In the Event section, under Date and Time, set the Time Unknown option to Yes.Save your entries. | The date remains the same.The time is set to 00:00.The Time and Time Zone fields are disabled.The date and time are updated in the page header. |  |
| 11 | Add a Link to an Incident (Optional) | In the header toolbar, choose Linked Objects.In the Linked Objects dialog box:Choose Add and select Incident in the dropdown list.Open the value help in the Object ID column. In the Select: Object ID dialog box:Search for an incident (by Incident ID, Incident Record Status, Plant ID, Title, or Incident Start Date).Find and select an incident in the results table.Back in the Linked Objects dialog box, the selected incident is displayed.Add a comment for the added link in the Comment on Link field.Choose the Translations link to translate the text in another language.Choose OK. | The link between the two incidents is established and visible only in the Linked Objects dialog box.Note To remove the link, choose Delete in the Linked Objects dialog box. |  |
| 12 | View Change Documents (Optional) | In the header toolbar, choose Display Change Documents.Select a Date via the date picker.Choose Go. | All changes made in different fields of the incident record are displayed in a table.For each change record, the following information is displayed:DateTimeChange TypeNode NameField DescriptionOld valueNew valueUserActionNote When you choose the Action link, more details about the change record are displayed in the Additional Information section below the table. |  |

##### Manage Location

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The incident manager (Industrial Hygienist) enters information about the location of incident.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed.Note The Details tab is available for all incident categories. |  |
| 2 | Navigate to the Location Tab | Navigate to the Location tab. | The Location tab is loaded.The following sections are displayed:AssignmentDetails |  |
| 3 | Assign Location | In the Assignment section, in the Location field, use the value help to select the Division ABC location, if it is not already selected. | The name and ID of the selected location are displayed in the Location field. |  |
| 4 | Display Location | In the Assignment section, choose the Details link next to the Location field. | The selected location object is displayed. |  |
| 5 | Enter Plant ID | In the Assignment section, in the Plant ID field, use the value help to enter a plant. | The selected plant ID is displayed in the Plant ID field. |  |
| 6 | Add Location Classification | In the Details section, under Description, use the value help for the Location Classification field to select Assembly Line. | Assembly Line is displayed in the Location Classification field. |  |
| 7 | Enter Location Description | In the Details section, in the Location Description field, change or add <additional location description> text. | The <additional location description> text is displayed in the Location Description field. |  |
| 8 | Add Geographic Location | In the Details section, under Geographic Location, make the following entries:Latitude: 51Longitude: 8 | The Latitude and Longitude fields are updated. |  |
| 9 | Change Address | In the Details section, under Address:Change the text manually in the fields Street and Number, Postal Code, and City.Use the value help to enter values for Country/Region and Region. | All fields under Address are updated. |  |

##### Manage People

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The responsible incident manager (Industrial Hygienist) enters information about the people involved in the incident.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed. |  |
| 2 | Access the People Tab | Navigate to the People tab. | The People tab is loaded.In the People table, the first person on the list is selected. |  |
| 3 | Add a Person with a Witness Role | In the People section, choose Add.In the Choose Person dialog box:In the Involved Person field, open the value help.Search for a <witness person> by one or more search criteria and select a record.Select the checkbox for the Witness role.Choose OK. | The selected <witness person> name is added to the People table.The <witness person> is displayed in the Name column. The Witness role is displayed in the Role(s) column. |  |
| 4 | Remove a Person from the Incident | In the People section:Select the <witness person>.Choose Delete.In the confirmation dialog box, choose Yes. | The <witness person> is removed from the list. |  |

###### Enter Details for All Persons

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The responsible incident manager (Industrial Hygienist) enters basic information about the people involved in the incident.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed. |  |
| 2 | Access the People Tab | Navigate to the People tab. | The People tab is loaded. |  |
| 3 | Select a Reporting Person | In People section, choose the person with the Reporting Person role. | The details about the selected person are displayed on a new screen.In the Details area, the following fields are displayed: Name, Date of Birth, Age, and Position.The Statements area contains the Add Statement option. |  |
| 4 | Change Roles | In the header toolbar, choose Change Role.In the dialog box that opens, select one or more checkboxes next to the listed roles and choose OK. | The selected roles are updated in the Roles field in the header. |  |
| 5 | Replace a Person | In the Details section, open the value help for the Name field and select another person from the dialog box. | The Name field is updated. |  |
| 6 | View More Person Details | In the Details section, choose Details below the Name field. | A Details dialog box displays data for the person in the following sections: Person/Organization, Street Address, Communication, and Organizational Assignment. |  |
| 7 | Add a Statement | In the Statements section, choose Add Statement.In the Add Statement dialog box, make the following entries and choose OK:Leave the current date and time in the Date / Time field.Add a statement in the Statement text field.Leave your user name set in the Statement Recorder field.Leave the Exclude from Report checkbox not selected. | All data entered in the Add Statement dialog box is added to the incident record and displayed in the Statements section.Next to each statement there are 4 links:To preview details about the Statement RecorderTo Edit Translation of the statementTo Edit the statementTo Delete the statementNote If there are 2 or more statements, then they are sorted by date/time – the newest on top. |  |
| 8 | Edit Statement | In Statements section, choose the Edit link next to a statement.Follow the instructions described in step 7 and make the necessary changes. | The changes in the statement are displayed in the Statements section. |  |
| 9 | Edit Translation for a Statement | In the Statements section, choose the Edit Translation link for a statement.In the Edit Translation dialog box, make the following entries in the Edit Texts in Other Languages section and choose OK:Language: GermanText: <Text für die Übersetzung> | The translation is added to this statement. It is visible when the user logs on to the system with German language. |  |
| 10 | Delete a Statement (Optional) | In the Statements section, you can delete a statement by choosing the Delete link for a statement. Then, choose Yes in the confirmation dialog.Note A statement is required for the Create and Send an Incident Report procedure. | The statement is removed from the incident. |  |
| 11 | Set Restricted Access | Choose Done to go back to the People tab.In the header toolbar, choose Restrict Data Access.From the Restricted Access dropdown menu, select the option No for all people.Choose OK. | The option is set. |  |

###### Enter Details for Persons with Special Roles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The incident manager responsible (Industrial Hygienist) enters role-specific information about people involved in the incident.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed. |  |
| 2 | Access the People Tab | Navigate to the People tab. | The People tab is loaded. |  |
| 3 | Select an Injured Person | In the People section, choose the person with the Injured Person role from the list. | The details for the selected person are displayed on a new screen. |  |
| 4 | Add Reporting Criteria for an Injured Person | On the Details tab, in the Personal Data section, under Reporting Criteria, make the following entries:In the Incident Type field, use the value help to select Work-Related Incident.Fatality: YesIn the newly appeared Fatality section, enter date and time in the past in the Date/Time field. |  |  |
| 5 | Add OSHA (USA) Reporting Criteria for an Injured Person | Select the OSHA (USA) regulation for the incident, if not already done in the [Enter Details for All Persons](#unique_18) [page ] 26 section.On the Details tab, in the Personal Data section, under Reporting Criteria, select the following options:Privacy Case: YesInjured on Site: YesInjured on Duty: YesAdditional Criteria: select Hearing Loss Based on STS via the value help.In the Fatality section, make the following entries:Location of Death: select Ambulance via the value help.Cause of Death: select Accident via the value help.Choose Done. | All fields in the Reporting Criteria and Fatality sections contain the selected data. |  |
| 6 | Add Employment Details | In the Employment section, under Details, make the following entries depending on the chosen regulation.At Organization Since: Set a <date in the past> via the date picker.Note The At Organization Since field is visible if the OSHA (USA) regulation has been assigned.At Position Since: Set a <date in the past> via the date picker.Note The At Position Since and Ceased Work Date / Time fields are visible if the Berufsgenossenschaft (Germany) regulation has been assigned.In the Employment section, under Working Time on Day of Incident, make the following entry for the OSHA (USA) and the Berufsgenossenschaft (Germany) regulations:Actual Start / End: 08:00 / 17:00 | The fields are populated with the entered data. |  |
| 7 | Add Working Time on Day of Incident | In the Employment section under Working Time on Day of Incident, make the following entry for the OSHA (USA) and the Berufsgenossenschaft (Germany) regulations:Actual Start / End: 08:00, 17:00 | The Actual Start / End field is updated. |  |
| 8 | Add a Comment | In the Comment field, enter a comment. |  |  |
| 9 | Add an Absence | In the Work Absences and Restrictions table, choose Add, and select Absence from the dropdown list. | A new record with category Absence is added to the Work Absences and Restrictions table. The current date is set by default in the Start Date column. |  |
| 10 | Edit an Absence | Select the newly added absence record and make the following entries:Start Date: Select <17.02.2020> via the date picker.End Date: Select <24.02.2020> via the date picker.Alternatively, set <25.02.2020> for Estimated End Date via the date picker. | The selected dates are populated in the table.In the Work Absences and Restrictions table, the following fields are calculated when you choose Done:Actual Workdays displays the value 6.Actual Calendar Days displays the value 8. |  |
| 11 | Add a Restriction | In the Work Absences and Restrictions table, choose Add, and select Restriction from the dropdown list. | A new record with category Restriction is added to the Work Absences and Restrictions table. The current date is set by default in the Start Date column. |  |
| 12 | Edit a Restriction | Select the newly added restriction record and make the following entries:Start Date: Select <21.02.2020> via the date picker.End Date: Select <29.02.2020> via the date picker.Alternatively, set <01.03.2020> for Estimated End Date via the date picker. | The selected dates are populated in the table.In the Work Absences and Restrictions table, the following fields are calculated when you choose Done:Actual Workdays displays the value 6.Actual Calendar Days displays the value 9. |  |
| 13 | Set Permanent Absence (Optional) | In the Work Absences and Restrictions table, select the absence record.Select the checkbox in the Permanent column. | In the Work Absences and Restrictions table, the Estimated End Date field is cleared, and the End Date is set to the current date.In the Actual Calendar Days section, the Absences and Restrictions fields are recalculated accordingly after you choose Done.Note The calendar days of absence and of restriction, as well as their sum, are limited to 180. |  |
| 14 | Set Permanent Restriction (Optional) | In the Work Absences and Restrictions table, select the restriction record.Select the checkbox in the Permanent column and choose Save. | In the Work Absences and Restrictions table, the Estimated End Date field is cleared, and the End Date is set to the current date.In the Actual Calendar Days section, the Absences and Restrictions fields are recalculated accordingly after you choose Done.Note The calendar days of absence and of restriction, as well as their sum, are limited to 180. |  |
| 15 | Add Job Transfer | In the Work Absences and Restrictions table, select the restriction record.Select the checkbox in the Job Transfer column. | The checkbox in the Job Transfer column is selected. |  |
| 16 | Delete an Absence (Optional) | In the Work Absences and Restrictions table, select an absence record and choose Delete.Choose Yes in the confirmation dialog box. | The absence record is removed from the Work Absences and Restrictions table.In the Actual Calendar Days section, the Absences and Restrictions fields are recalculated accordingly after you choose Done. |  |
| 17 | Delete a Restriction (Optional) | In the Work Absences and Restrictions table, select a restriction record and choose Delete.Choose Yes | The restriction record is removed from the Work Absences and Restrictions table.In the Actual Calendar Days section, the Absences and Restrictions fields are recalculated accordingly after you choose Done. |  |
| 18 | Add a Witness | Go back to the People section, select a person and add the Witness role to this person by choosing Change Role.In the Witness For area that appears for the person, select one or more of the checkboxes. | The Witness For area appears at the bottom of the Person section. It contains:a list of all injured persons in the incidenta checkbox for each of the injured persons |  |
| 19 | Add a Supervisor | Go back to the People section, select a person and add the Supervisor role to the person by choosing Change Role.In the Supervisor Of area that appears for the person, select one or more of the checkboxes. | The Supervisor Of area appears at the bottom of the Person section. It contains:a list of all injured persons in the incidenta checkbox for each of the injured persons |  |

###### Enter Health Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The responsible incident manager (Industrial Hygienist) enters health information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed. |  |
| 2 | Select an Injured Person | Navigate to the People tab. In the People section, choose the person with the Injured Person role. | The details for the selected person are displayed on a new screen. |  |
| 3 | Display Health | Navigate to the Health tab. | The following sections are available:Injuries / IllnessesTreatmentThe Injuries/Illnesses table is loaded and one record with Injury classification is available. |  |
| 4 | Edit an Injury/Illness Record | Select the Injury record in the table and make the following entries in the table:Classification: Hearing LossInjury/Illness Type: Diseases of external earInjury/Illness Description: <additional information for the injury>Body Part: EarBody Part Description: <additional information for the ear>Body Side: BothReporting Required: Select the checkbox if not already selected.Main Injury/Illness: Select the checkbox if not already selected.Note The checkbox is visible for the Berufsgenossenschaft (Germany) regulation only.Choose Translate Injury/Illness Description and add a translation for the text in a selected language.Choose Translate Body Part Description and add a translation for the text in a selected language. | All data about the selected injury/illness is filled in the table. |  |
| 5 | Add a New Injury/Illness | Choose Add. | A new record with classification Injury is added to the table. |  |
| 6 | Delete an Injury/Illness | Select the record from the previous step in the table and choose Delete.Choose Yes in the confirmation dialog box. | The Injury/Illness record is removed from the table. |  |
| 7 | Add Data to the Treatment Section | In the Treatment section, make the following entries:First Physician: Use the value help to select a personFurther Treatment Provider: Use the value help to select a personNote You can use the Details link to display more information about each of the selected persons.Comment: <text for comment>.Choose Translate to add a translation for the comment in a selected language.On the Health tab, select the following options for the injured person:First Aid Treatment: YesTreatment Beyond First Aid: YesEmergency Room: YesImpatient Overnight: YesUnconsciousness: YesImmediate Resuscitation: YesIn the Transportation section, select the following options via the value help:To First Aid: AmbulanceTo Further Treatment: Ambulance | All selected data is populated in the fields.The selected persons for first physician and further treatment provider are visible in the Treatment section.The same persons are added to the People table and the corresponding roles are assigned to them.Note These persons can be replaced or removed from the incident via the Treatment section only. |  |

###### Enter Influences on Health and Safety

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The responsible incident manager (Industrial Hygienist) enters information about factors of influence on the health and safety of people involved in the incident.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed. |  |
| 2 | Select an Injured Person | On the People tab, choose a person with the Injured Person role from the list. | The details for the selected person are displayed on a new screen. |  |
| 3 | Display Influences on Health and Safety Information | Navigate to the Influences on Health and Safety tab. | The Influences on Health and Safety table is loaded and the records for all available influencing factor categories are displayed.Note The Influences on Health and Safety tab is also available for persons with the Nearly Injured role in a Near Miss incident. |  |
| 4 | Edit an External Influence | Select the External Influence record in the table and make the following entries:Influencing Factor: Select Bad Visibility via the value helpDescription: <additional description text> |  |  |
| 5 | Edit an Immediate Action | Select the Immediate Action record in the table and make the following entries:Influencing Factor: Select Cleanup via the value helpDescription: <additional description text> |  |  |
| 6 | Edit an Incident-Causing Object | Select the Incident-Causing Object record in the table and make the following entries:Influencing Factor: Select Biological Agent via the value helpDescription: <additional description text>Movement: select Standing via the value help. | Note This factor category is also available for persons with the Nearly Injured role in a Near Miss incident. It appears as Near Miss-Causing Object. |  |
| 7 | Edit an Incident-Causing Substance | Select the Incident-Causing Substance record in the table and make the following entry:Description: <additional description text> | Note This factor category is also available for persons with the Nearly Injured role in a Near Miss incident. It appears as Near Miss-Causing Substance. |  |
| 8 | Edit an Activity of Injured Person | Select the Activity of Injured Person record in the table and make the following entries:Influencing Factor: Select Cleaning via the value helpDescription: <additional description text> | Note This factor category is also available for persons with the Nearly Injured role in a Near Miss incident. It appears as Activity of Nearly Injured Person. |  |
| 9 | Edit a Movement of Injured Person | Select the Movement of Injured Person record in the table and make the following entries:Influencing Factor: Select Jumping via the value helpDescription: <additional description text> | Note This factor category is also available for persons with the Nearly Injured role in Near Miss incident. It appears as Movement of Nearly Injured Person. |  |
| 10 | Edit a Personal Protective Equipment | Select the Personal Protective Equipment record in the table and make the following entries:Influencing Factor: Select Protective Garment via the value helpDescription: <additional description text>Required: YesUsed: YesMalfunction: Yes |  |  |
| 11 | Edit a Technical Safety Device | Select the Technical Safety Device record in the table and make the following entries:Influencing Factor: Select Other Technical Safety Device via the value helpDescription: <additional description text>Required: YesUsed: YesMalfunction: Yes |  |  |
| 12 | Edit Near Miss Cause (Only for a Near Miss) | Select the Near Miss Cause record in the table and make the following entries:Influencing Factor: Select Communication Problem via the value helpDescription: <additional description text> | Note This factor is only available for persons with the Nearly Injured role in a Near Miss incident. |  |
| 13 | Add a Translation Description for a Factor | Select a record in the table and choose Translate Description....Add a translation for the description in the desired language. |  |  |
| 14 | Add a New Influencing Factor | Choose Add.Select Add Technical Safety Device from the dropdown list. | A new record with the Technical Safety Device category is added to the table. |  |
| 15 | Remove an Influencing Factor | Select the second record with category Technical Safety Device.Choose Delete.Choose Yes in the confirmation popup.Choose Done. | The selected record with category Technical Safety Device is removed from the table. |  |

##### Manage Assets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The responsible incident manager (Industrial Hygienist) enters information about assets that were involved in the incident.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed. |  |
| 2 | Navigate to the Assets Tab | Go to the Assets tab. | The Assets tab is loaded. |  |
| 3 | Add Equipment | In the Assets section, choose Add, and select Equipment from the dropdown list. | A new page is loaded.In the Assignment section, the Plant field is populated with the value from the Location tab of the incident record. |  |
| 4 | Enter Equipment Description | In the Description section, make the following entries:Description: <description text>Additional Information: <additional information text>Company-Owned: YesStill Operational: Yes | The data is visible in the corresponding fields. |  |
| 5 | Enter Equipment Assignment | In the Assignment section, make the following entries:Object Type: Select a value via the value help.Equipment: Select a value via the value help.Location Description: <location description text> | The following fields are populated automatically with the data that has been specified for the selected piece of equipment in the Plant Maintenance component:DescriptionFunctional LocationThe Plant field is overwritten with the plant specified for the equipment in the Plant Maintenance component. |  |
| 6 | Enter Involved People | In the Involved People section select an Operator via the value help | The Operator field is populated. |  |
| 7 | Enter Damages Information for Equipment | In the Damages section:Choose Add.In the Damage Type column, use the value help to select Collision.In the Description column, enter <damage description text>.Choose Done. | The Assets tab is loaded, and the equipment is added to the Assets table. |  |
| 8 | Add Vehicle | In the Assets section, choose Add, and select Vehicle from the dropdown list. | A new page is loaded.In the Assignment section, the Plant field is populated with the value from the Location tab of the incident record. |  |
| 9 | Enter Vehicle Description | In the Description section, make the following entries:Vehicle Description: <description text>Additional Description: <additional description text>Company-Owned: YesStill Operational: Yes | The data is visible in the corresponding fields. |  |
| 10 | Enter Vehicle Assignment | In the Assignment section, make the following entries:Object Type: Select a value via the value help.Vehicle: Select a value via the value help.In the Vehicle Data section, make the following changes:Country/Region of Registration: Select a value via the value helpPlace of Registration: <Place of registration text> | The following fields are filled in automatically with the data that has been specified for the vehicle:Vehicle DescriptionVehicle ManufacturerVehicle ModelLicense Plate NumberThe Plant field is overwritten with the plant specified for the vehicle. |  |
| 11 | Enter Involved People | In the Involved People section use the value help to fill in the Driver, Owner, and Insurer fields. | All persons are added to the People tab of the incident record and the corresponding roles are assigned to them. |  |
| 12 | Enter Passengers | In the Passengers section:Choose Add.In the Passenger Name column, enter a person via the value help. | A new entry is added to the Passengers table.The passenger's phone number and email address are populated automatically in the corresponding fields.All passengers are added to the People tab of the incident record and the corresponding roles are assigned to them. |  |
| 13 | Enter Damages Information for Vehicle | In the Damages section:Choose Add.In the Damage Type column, use the value help to select Collision.In the Description column, enter <damage description text>.Choose Done. | The Assets tab is loaded, and the equipment is added to the Assets table. |  |
| 14 | Add Property | In the Assets section, choose Add, and select Property from the dropdown list. | A new page is loaded.In the Assignment section, the Plant field is populated with the value from the Location tab of the incident record. |  |
| 15 | Enter Property Description | In the Description section, make the following entries:Property Description: <description text>Additional Description: <additional description text>Company-Owned: YesStill Usable: Yes | The data is visible in the corresponding fields. |  |
| 16 | Enter Property Assignment | In the Assignment section, make the following entries:Object Type: Select a value via the value help.Property: Select a value via the value help. | The following fields are populated automatically with the data that has been specified for the property:Property DescriptionStreet / House No.Postal CodeCityCountry/RegionRegionThe Plant field is overwritten with the plant specified for the property. |  |
| 17 | Enter Involved People | In the Involved People section use the value help to fill in the Tenant, Owner, and Insurer fields. | All persons are added to the People tab of the incident record and the corresponding roles are assigned to them. |  |
| 18 | Enter Damages Information for Property | In the Damages section:Choose Add.In the Damage Type column, use the value help to select Collision.In the Description column, enter <damage description text>.Choose Done. | The Assets tab is loaded, and the equipment is added to the Assets table. |  |
| 19 | Edit an Asset (Optional) | To edit an asset, select it in the Assets table and then change the data in the corresponding details page as described in the previous steps. | The changed data is displayed in the corresponding fields. |  |
| 20 | Delete an Asset (Optional) | To remove an asset from the incident record, select it in the Assets table and choose Delete.Save your changes. | The asset is removed from the Assets table. |  |

##### Manage Releases

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The responsible incident manager (Industrial Hygienist) enters information about releases that were involved in the incident.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed.Release is listed in the Classification field. |  |
| 2 | Open the Releases Tab | Navigate to the Releases tab.Note If the Releases tab is not visible, choose Classification in the header toolbar and select the Release group. | The Releases tab is loaded.The Releases table contains the released material that was entered during initial reporting. |  |
| 3 | Add a Release | Choose Add.Note If you have reported a release during the initial reporting, you can skip this step. | A new page is loaded.The following tabs are displayed:ReleaseMaterialsCleanup Responses |  |
| 4 | Enter Release Details | In the Details section, make the following entries:Release Type: GroundRelease Size: SmallCleanup Performed: YesReporting Required: NoRelease Description: <enter free text> | The selected type is displayed in the Releases table. |  |
| 5 | Enter Material Information | On the Materials tab, choose Add, and make the following entries:Material: Select a material via the value helpDescription: <enter free text>Material State: LiquidAffected Area: use the value help to select Company/OrganizationIn the Material Release and Recovery section, make the following entries:Released / Unit: 3 LRecovered / Unit: 3 LRecovery Method: use the value help to select Chemical Response MethodsChoose Save. | All fields in the Details section are populated.The selected material is displayed in the Release column of the Releases table. |  |
| 6 | Enter Cleanup Responses Information | In the Cleanup Responses subtab, choose Add, and make the following entry:Cleanup Method: use the value help to select IncinerationIn the Cleanup Response Details section, make the following entry:Description: <enter free text>Choose Save. | The entered data is saved, and the Releases tab is loaded. |  |

##### Manage Notices of Violation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The responsible incident manager (Industrial Hygienist) enters details about notices of violation that were issued to the organization.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed. Notice of Violation is listed in the Classification field in the header. |  |
| 2 | Access the Violations Tab | Navigate to the Violations tab.Note If the Violations tab is not visible, choose Classification in the header toolbar, and select the Notice of Violation group. | The Violations tab is loaded.The Notices of Violation list is initially empty. |  |
| 3 | Add a Notice of Violation | In the Notices of Violation table, choose Add. | A new page is loaded. The following sections are available:InformationNoticePenaltyAttachments |  |
| 4 | Edit the Information Section | In the Information section, make the following entries:Violation Type: select Actual Exposure via the value help.Violation Category: use the value help to select RepeatedViolation Source: Employee | The selected type is populated in the Notices of Violation table and is displayed as a title of the page.The Violation Category and Violation Source fields are populated. |  |
| 5 | Edit the Notice Section | In the Notice section, make the following entries:Issued Date / Time: set <yesterday’s date> for a date and change the time and time zoneViolation Notice ID: <notice ID>Issuing Organization: use the value help to select an organizationReceived Date / Time: Enter <today’s date> and the current time.Summary: <free text>Choose Translate and add translated text for different languages. | The date and time values are saved in the corresponding fields.The Received Date/Time must be the same as, or later than, the Issued Date/Time. |  |
| 6 | Display Details About the Issuing Organization | In the Notice section, choose Details below the Issuing Organization field. | The Organization Details dialog box appears and displays data about the company in the following areas:Person / OrganizationStreet AddressCommunication |  |
| 7 | Add Penalty Information | In the Penalty section, make the following entries:Proposed Penalty / Currency: <amount> EURFinal Penalty / Currency: <amount> EUR | The values are converted to the company currency and the corresponding values are displayed in the fields Amount in Local Currency when you choose Done. |  |
| 8 | Manage Documents Related to the Notice of Violation | In the Attachments section, choose Add and select Document.Browse and select a file to upload, then choose OK.Choose Done. | The name and the link to the file are displayed.All selected files are listed on the Documents tab. |  |

##### Manage Financial Tracking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The responsible incident manager (Industrial Hygienist) enters financial details to track costs and income that are associated with the incident.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed. |  |
| 2 | Open the Finance Tab | Navigate to the Finance tab. | The Finance tab is loaded. |  |
| 3 | Make Estimations (Optional) | In the Estimation section, make the following entries and choose Save:Estimated Total Expenses / Currency: <amount> EUREstimated Total Income / Currency: <amount> EUR | In the Overview table, the Estimated Amount column is updated with the entered amounts, recalculated for the company currency, and the Net Income / Loss is calculated accordingly. |  |
| 4 | Add a Financial Transaction Manually | In the Financial Transactions section, choose Add, and select Add Manually.In the newly added row, make the following entries and choose Save:Category: use the value help to select Labor CostExpenses / Income: ExpensesReference: Person : <name of the injured person>Amount: <amount>Currency: EUR | The Overview table is updated with the entered amount, recalculated for the company currency. |  |
| 5 | Add an Internal Order (Optional) | In the Financial Transactions section, choose Add, and select Internal Order.In the Add Internal Order dialog box, choose an existing internal order or create a new one. | The internal order data is populated in the Financial Transactions table and the amounts in the Overview table are updated. |  |
| 6 | Add a Maintenance Order (Optional) | In the Financial Transactions section, choose Add, and select Maintenance Order.In the Add Maintenance Order dialog box, choose an existing maintenance order or create a new one. | The maintenance order data is populated in the Financial Transactions table and the amounts in the Overview table are updated. |  |

##### Manage Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident has been reported in the system. The responsible incident manager (Industrial Hygienist) uploads relevant documents to the incident record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed. |  |
| 2 | Access the Documents Tab | Navigate to the Documents tab. | The Documents table contains all documents that were added at the initial incident reporting:The PDF document of type Initial Incident Record (also known as Actual Event report).The photo that was added to the incident.The Documents table also contains the documents that were uploaded on the Notices of Violation tab.Note The Documents tab is available for all incident categories. |  |
| 3 | Add a Document | In the Documents table, choose Add and select the Document from the dropdown list.In the Choose File dialog box, browse and select a file to upload:Choose OK. | The selected document is added to the table and the corresponding data is populated in the fields. |  |
| 4 | Delete a Document (Optional) | You can delete a document of type Other Document by selecting the record in the Documents table and choosing Delete.Save your changes. | The selected record of type Other Document is removed from the table.Note The document with type Initial Incident Record cannot be deleted from the incident. |  |

##### Review and Complete an Incident (Optional Steps)

###### Manage a Near Miss

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident of the category Near Miss has been reported in the system. The responsible incident manager (Industrial Hygienist) enters category-specific information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the Reported Near Miss | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The near miss <near miss title text> is loaded. The Details tab is displayed. |  |
| 2 | Enter Data for Near Miss | In the Event section under Description, make the following entries:Change the text in the Situation Description field.Change the text in the Cause field.You can add translations by choosing Translate below the respective field.Estimated Risk: 2 - Medium RiskSave your entries. | The texts are saved. |  |

###### Manage a Safety Observation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident of the category Safety Observation has been reported in the system. The responsible incident manager (Industrial Hygienist) enters category-specific information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the Reported Safety Observation | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The safety observation <safety observation title text> is loaded. The Details tab is displayed. |  |
| 2 | Enter Data for the Safety Observation | In the Event section under Description, make the following entries:Change the text in the Situation Description field.Change the text in the Cause field.You can add translations by choosing Translate below the respective field.Estimated Risk: 2 - Medium RiskSave your entries. | The text is saved. |  |

###### Change the Status of an Incident Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager (Industrial Hygienist) changes the status of an incident record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. |  |
| 2 | Cancel the Incident | In the header toolbar, choose Status and select the Void option.Choose OK in the warning dialog box.Note This option is used to invalidate an incident record. | The incident record is set to status Void.The record is read-only. |  |
| 3 | Reopen the Incident | If an incident record has been canceled by accident, it can be reopened.Open the incident that you set to status Void in step 2.In the header toolbar, choose Status and select the Reopened option.Choose OK in the warning dialog box. | The incident record is set to status Reopened.The record is editable. |  |

###### Change the Category of an Incident Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager (Industrial Hygienist) changes the category of an incident record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section to open an incident of category Near Miss. | The incident <near miss title text> is loaded. |  |
| 2 | Change the Category | In the header toolbar, choose Category and select the Incident option.Choose Yes to confirm the change.In the Change Category Details dialog box, make the following selections:In the Groups table, select the checkbox for Injury/Illness.In the Regulations table, select the checkbox for OSHA (USA).In the People table, select the <name of the nearly injured person> and choose Assign Roles.In the newly opened Assign Roles (Change Category) dialog box, select the Injured Person checkbox and choose OK.Choose OK. | The near miss record is closed.A new incident record is created based on the data that was entered for the near miss.The new incident with the same title <near miss title text> is loaded.Note The functionality is available for all incident categories. |  |

#### Create an Investigation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The investigation lead (Industrial Hygienist role) creates an investigation to determine the causes that led to an incident.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist |  |  |
| 2 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section to open the incident. | The incident is loaded. The Details tab is displayed. |  |
| 3 | Create an Investigation | In the header toolbar, choose Investigation > Create .In the Create dialog box, enter the following:Investigation Type: Internal InvestigationIncident: <automatically populated with the title of the incident you're currently processing>Choose Continue. | The Plan tab of the investigation record is loaded. |  |
| 4 | Assign Members to the Investigation Team | In the Team section, in the empty field in the Team Member column, use the value help to select a person.Note Only people with existing work agreements appear in the value help. Work agreements can be defined in the Manage Workforce Version 2 app (F6097A).To create an investigation, you must specify an investigation lead. Select the Investigation Lead checkbox for the person you added. | The person you added is displayed in the Team section, and the checkbox in the Investigation Lead column is selected. |  |
| 5 | Create an Activity | In the Activities section, choose Create.In the dialog box, in the Type field, select Evidence Collection. In the Activity field, enter a description of the activity.Choose Continue. | The activity is added to the Activities table, and the activity details page is loaded or the right hand side of the screen. |  |
| 6 | Enter Activity Details | In the Details section, in the Description field, enter a <free-text description>.In the Dates section, in the Due Date field, use the value help to select a future date.In the Responsibilities section, enter the following information:Owner: Use the value help to select a person.Responsible: Use the value help to select a person.Note You can only assign members of the investigation team as Owner and Responsible for an activity (see step 4).In the footer of the activity details page, choose Apply. | The activity details are saved, and the details page is closed. |  |
| 7 | Create the Investigation | In the footer of the page, choose Create. | The investigation record is saved, and the investigation status in the header is set to New.The Investigation screen is in read-only mode.In the header, the following buttons appear: Edit, Start, Cancel, and Display Report. |  |
| 8 | Process the Investigation | Follow the steps described in the [Process an Investigation](#unique_42) [page ] 67 section to complete the investigation. |  |  |

#### Create and Send an Incident Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A regulation-specific report is generated and sent to the relevant authority.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Details tab is displayed. |  |
| 2 | Add a Report Record Automatically | In the header toolbar, choose Regulations.Select the regulation that is relevant for your region, if not done already, and choose OK.Navigate to the Reports tab.Note Depending on the selected regulation, a report record is added automatically. The following regulations are available as part of the Best Practices content:OSHA (USA)Berufsgenossenschaft (Germany) | The Reports tab is loaded.The Reports table contains records for the selected regulations with the following data:Report Type:For the OSHA (USA) regulation:OSHA 301 (Injuries and Illnesses Incident Report)For the Berufsgenossenschaft (Germany) regulation:BG Incident Report (Germany)BG Incident Report (Germany) via Web ServiceReference Category: Injured PersonReference: <injured person name>Reporting Required: UnknownReport Status: NewDue Date: <incident date + 4> |  |
| 3 | Add a Report Record Manually | In the Reports section, choose Add.In the Add Report Form dialog box, select the relevant report for the injured person <name of the injured person> and choose OK. | The Reports table contains two identical records (with the same data as described in step 2). |  |
| 4 | Set Reporting Duty | In the Reports table, select the first record added for the injured person. The value in the Reporting Required column is still Unknown.Choose Determine Reporting Duty.Alternatively, select Yes from the dropdown list in the Reporting Required column. | The value in the Reports table, in the Reporting Required column, is set to Yes.The value in the Reporting Required field in the page header is set to Yes. |  |
| 5 | Set a Due Date for the Report | In the Reports table, select the first record added for the injured person and change the Due Date via the date picker to a date in the future.Save your changes. |  |  |
| 6 | Generate an OSHA 301 Report | Select a record added for the injured person with report type OSHA 301 (Injuries and Illnesses Incident Report) and choose Generate.In the Generate OSHA 301 for <injured person's name> dialog box, make the following selections:Report Language: ENCountry/Region: USLeave <your user name> as set by default in the Sender field.Choose OK. | The PDF report is generated. A link to the file is added to the Report Forms table in the File Name column.The value in the Report Status column is set to Generation Finished. |  |
| 7 | Generate a BG Incident Report (Optional) | Select a record added for the injured person with report type BG Incident Report (Germany) via Web Service and choose Generate.In the Generate BG Unfallanzeige for <injured person's name> dialog box, make the following entries:Membership Number: Select a relevant entry from the dropdown menu.Note The membership number and other employer details are maintained in the Specify Employer Details Configuration step.Which department is the insured person assigned to?: <department's name>What are the name and the address of the insurer?: <free text>Telephone: <telephone number>Choose OK. | The XML report is generated. A link to the file is added to the Reports table in the File Name column.The value in the Report Status column is set to Generation Finished. |  |
| 8 | Display a Generated Report | In the Reports table, choose the link in the File Name column to open the generated report. | The generated report is loaded. |  |
| 9 | Send a Report | Select a record with a generated report.Choose Send and select Send via Email from the dropdown list.In the newly opened dialog box, make the following entries:Recipient: <recipient name>Send Via: Leave the default option E-MailE-Mail of Report Recipient: Leave the automatically populated e-mailIn the Additional Recipients (CC) table:Choose Add.Select another recipient via the value help.Choose Details to display more details about the recipient.Choose Delete to remove the recipient from the table, if needed.When you have entered the data in the dialog box, choose OK. | The report file is sent to all recipients.The value in the Reports table, in the Report Status column, is set to Sent.Note You can send the report of type BG Incident Report (Germany) via Web Service directly to the authority via a web service if you have a communication arrangement created for the Environment, Health and Safety - Workers' Compensation Associations Integration (SAP_COM_0671) communication scenario. |  |
| 10 | Delete a Report | Select a record with or without a generated report.Choose Delete.Confirm the dialog box. | The selected record is removed from the table. |  |

#### Define and Manage Tasks

##### Define a Task

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager (Industrial Hygienist) assigns and schedules the work required to prevent an unsafe condition or event.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. |  |
| 2 | Open the Tasks Tab | Navigate to the Tasks tab. | The Tasks tab is loaded.The Tasks table is initially empty.Note The Tasks tab is available for all incident categories. |  |
| 3 | Open the Incident Tasks App | On the Tasks tab, choose Manage Tasks.Note Alternatively, choose Create Task and continue with steps 5 through 8. | The Incident Tasks screen is displayed.The Tasks table is initially empty. |  |
| 4 | Add a New Task with Approval | Choose Add Task.Select the Task with Approval (Classic) option. | The Task Definition screen is displayed.Note The procedure for defining a Task and a Task with Approval is described in the table below. The differences are marked in the corresponding cells. |  |
| 5 | Add Task Information | In the Task Information section, enter the following information:Title: <new task with approval>.Description: <description of the new task>.Owner: Leave the predefined value.Note Your user is set by default in this field.Priority: Leave the default value Medium.Start Date: Leave the default <tomorrow's date>.Due Date: Leave the default <tomorrow's date +7>.In the Assignee Assignment and Approver Assignment sections, you can select an assignee and approver for the task. You can either select by business user or location role. To enable more flexibility with the processing of the task, assign it to a location role. This way, the task is routed to everyone with the role for the respective location.Assignment Type of Assignee: Business UserAssignee: Enter a person <assignee name> via the value help.Assignment Type of Approver: Location RoleApprover Location Role: Incident Manager | The values are populated to the corresponding fields.Note For a Task, the Approver Assignment section is not available. |  |
| 6 | Add a Reference | In the References section, choose Manage References.Select the checkbox for <name of the injured person>.Choose Select. | The <name of the injured person> is added to the References section. |  |
| 7 | Add an Attachment | In the Attachments section, choose Upload.Browse and select a file, then choose Open. | The selected file is added to the Attachments section.The number of attachments is incremented by 1. The following information is displayed for the attachment:<file name> with a link to open the fileStatus: DraftUploaded By: The name of the current userUploaded On: The current date and timeSource: GOS |  |
| 8 | Create the Task | Choose Create. | The task is saved and appears as read-only. |  |
| 9 | Preview the Task in the List | Choose Back (< icon). | The Incident Tasks screen is displayed. The following details are displayed for the created task:IDTitle: <new task with approval>Type: Task with Approval (Classic)Status: Scheduled in 1 daysDue Date: <tomorrow's date +7>Recurrence: NoCurrent Processor: <assignee name>Reference: Person <name of the injured person> |  |

##### Edit a Task

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager (Industrial Hygienist) edits the information of a task required to prevent an unsafe condition or event.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open the Task Definition for Editing | Open an incident and navigate to the Tasks tab.Choose Manage TasksIn the Tasks list, select the newly created task.Choose Edit. | The Task Definition app is loaded in edit mode. |  |
| 2 | Change the Task Schedule | Choose Recurrence.In the Recurrence dialog box, choose the Based on Start Date schedule mode, and enter the following information:In the Recurrence Period section:Start Date: <today's date>End Date: <today's date +3>In the Recurrence Pattern section:Recur Every: Enter 1 and select Days from the dropdown list.Due In: Enter 2 and select Days from the dropdown list.Choose OK. | The Recurrence field in the Task Information section is updated. It displays the summary of the recurrence setup:The task occurs every 1 day from <today's date> to <today's date +3>. It is due 2 days after the start date. |  |
| 3 | Change the Assignee and Approver | In the Assignee field, use the value help to replace the <assignee name> with your user name.In the Approver Assignment section, change the assignment type to Business User. In the Approver field, use the value help to select your user name. | The selected values are displayed. |  |
| 4 | Save the Task | Save your entries. | The task is saved and appears as read-only. |  |
| 5 | Preview the Task in the List | Choose Back (< icon). | The Incident Tasks app is loaded. The following details are displayed for the first instance of the created task under the Task Instances tab:ID: <Task Definition ID>-1Title: <new task with approval>Type: Task with Approval (Classic)Status: Scheduled for todayDue Date: today's date +2Recurrence: YesCurrent Processor: <your user name>Reference: Person: <name of the injured person> |  |

##### Implement a Task

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The assignee of a task sets the status of the task to Completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. |  |  |
| 2 | Open the Work Item for Task Implementation | Open My Inbox - Incident Management (F7992).In the task list on the left, select the Execute Task: <new task with approval> work item. | The following details are displayed for the task:Title: Execute Task: <new task with approval>Task Owner: your user nameDue on: today's date + 2, recalculated for your time zoneCreated on: today's datePriority: MediumOn the Related Objects icon tab, the incident title <incident title text> with a link to the object is displayed. |  |
| 3 | Implement the Task | Choose Completed.In the Submit Decision dialog box:In the Decision Note field, enter <text for note>.Choose Submit.Note Alternatively, you can choose Reject to return the task to the task owner, for example to request more information. The task owner can provide the requested information and resend the task to the assignee or cancel the task. | The work item is completed and removed from your task list. |  |

##### Reject a Task with Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The person assigned as an approver of the task rejects the task.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. |  |  |
| 2 | Open the Work Item for Task Approval | Make sure that you have completed the steps in the [Implement a Task](#unique_35) [page ] 58 section.Open My Inbox - Incident Management (F7992).In the task list on the left, select the work item Approve Task: <new task with approval>. | The following details are displayed for the task:Title: Approve Task: <new task with approval>Task Owner: your user nameStatus: ReadyCreated on: today's datePriority: MediumOn the Information tab, the task title <new task with approval> and task description <description of the new task> are displayed.On the Comments tab, the following information is displayed:The comment submitted by the assignee: <text for note>The name of the assignee:<your name>The implementation date and timeOn the Related Objects tab, the incident title <incident title text> is displayed with a link to the object. |  |
| 3 | Reject the Task | Choose Rejected.In the Submit Decision dialog box, in the Decision Note field, enter <text for rejection>.Choose Submit. | The work item is removed from your task list.Note For further processing, a work item for task implementation is sent to the assignee's inbox. The procedure for task implementation is restarted. |  |

##### Create and Complete a Maintenance Notification Task

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager (Industrial Hygienist) creates a maintenance notification task. As a result, a Plant Maintenance (PM) notification is created automatically in the system. When the PM notification has been completed by the Maintenance Technician (SAP_BR_MAINTENANCE_TECHNICIAN) and if the maintenance notification task requires approval, a work item is sent to the approver's inbox. Otherwise, the maintenance notification task is completed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Basic Information tab is displayed. |  |
| 2 | Open the Tasks Tab | Navigate to the Tasks tab. | The Tasks tab is loaded. |  |
| 3 | Open the Incident Tasks App | On the Tasks tab, choose Manage Tasks. | The Incident Tasks app is loaded. |  |
| 4 | Add a Maintenance Notification Task | Choose Add Task.Select the Maintenance Notification option. | The Task Definition Maintenance Notification (F3359) app is loaded. |  |
| 5 | Add Task Information | In the Task Information section, make the following entries:Title: <new maintenance notification>.Description: <description of the new task>.Owner: Leave the default value with <your user name>.Approver: Enter <your user name> via the value help.Priority: Leave the default value Medium.Start Date: Select <today's date>.Due Date: Leave the default <tomorrow's date +7>. | The values are populated in the corresponding fields. |  |
| 6 | Enter Notification Information | In the Notification Information section:In the Notification Type field, select one of the available options that you have previously specified in [Preliminary Configuration](#unique_4) [page ] 4. If there are no notification types specified, skip this and the following steps.In the Technical Object field, select an entry via the value help. | The values are populated in the corresponding fields. |  |
| 7 | Create the Task | Choose Create. |  |  |
| 8 | Preview the Task in the List | Choose Back (<) icon. | The Incident Tasks app is loaded. The Status column of the newly created task displays Scheduled for today. When the task is started, the status changes to Due in 1 weeks. |  |
| 9 | Open the Task Instance | Select the row to navigate to the Task Definition Maintenance Notification (F3359) app. | When the maintenance notification task is started, the system creates a maintenance notification object, which is displayed in the Related Objects section of the corresponding task instance. |  |
| 10 | Complete the Maintenance Notification (Optional) | Select the maintenance notification object to process it in the relevant Plant Maintenance app.Note For this action, you need the Maintenance Technician role. | After the maintenance notification is completed, a work item for approval is sent to the approver's inbox. |  |
| 11 | Approve the Maintenance Notification (Optional) | Open My Inbox - Incident Management (F7992).Find the work item for approval and choose Approve. | The work item is removed from the approver's inbox.The status of the maintenance notification task is set to Completed. |  |

##### Create and Complete a Change Request Task

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager (Industrial Hygienist) creates a change request task because a change is required to operations or equipment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section. | The incident <incident title text> is loaded. The Basic Information tab is displayed. |  |
| 2 | Open the Tasks Tab | Navigate to the Tasks tab. | The Tasks tab is loaded. |  |
| 3 | Open the Incident Tasks App | On the Tasks tab, choose Manage Tasks. | The Incident Tasks screen is displayed. |  |
| 4 | Add a Change Request Task | Choose Add Task and select the Change Request type from the dialog box. | The Task Definition Change Request (F3415) app is loaded. |  |
| 5 | Enter Task Information | In the Task Information section, make the following entries:Title: <new change request>Description: <description of the new task>Priority: Leave the default value Medium |  |  |
| 6 | Enter Change Request Information | In the Change Request Information section, choose MOC Change Request from the Change Request Type dropdown list. |  |  |
| 7 | Add References (Optional) | In the References section, choose Manage References, and select one of the suggested options. |  |  |
| 8 | Create the Change Request Task | Choose Create. | The task of type Change Request is created. The system creates a change request in the Management of Change component and automatically set the task to Completed. |  |

##### Monitor Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager (Industrial Hygienist) monitors the tasks required to prevent unsafe conditions or events.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. |  |  |
| 2 | Access the App | Open Monitor Tasks (F2527). | The Monitor Tasks app is loaded.The following filter criteria are displayed:Start DateDue DateCompletion DateStatusOwnerCurrent ProcessorPriorityOrigin TypeLocationIDThe results list is initially empty. |  |
| 3 | Search for a Task | In the Start Date search filter, use the date picker to select the period from today's date to today's date +1.Choose Go. | The tasks are displayed in the results list.You can narrow down the results using other filters, as well. |  |
| 4 | Open the Host Object (Optional) | In the results list, choose the <incident title text> link in the Origin column.Note If the Origin column is not visible on your screen, choose Show Details to display the fields that don't fit in the table. | The incident is loaded and the Basic Information tab is displayed by default. |  |
| 5 | Open a Task (Optional) | Back in the results list, choose the row for <new task with approval>. | The task is loaded in read-only mode. |  |
| 6 | Forward a Task | Back in the results list, you can forward one or more task instances to another processor.To do so, select one or more task instances and choose Forward.In the Forward Tasks dialog box, in the Forward to Processor field, select a processor via the value help. | The name of the new processor is displayed in the Current Processor field in the Tasks list. |  |

##### Manage Tasks in a Calendar View

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager (Industrial Hygienist) gets an overview of tasks in a time schedule. Based on the overall schedule, the status of the tasks, and the workload of the team members, the incident manager adjusts the plan by reassigning and rescheduling the tasks between assignees.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. |  |  |
| 2 | Access the App | Open Task Calendar (F3840). | The Task Calendar screen is displayed. The calendar view contains a row with your user name.The following filter criteria are available:Task Type: initially <empty>Task Status: with default values Overdue, Due, Error, Scheduled, and CompletedOrigin Type: initially <empty>Location: initially <empty> |  |
| 3 | Find a Task | In the calendar view, find the task you created in the [Define a Task](#unique_33) [page ] 54 step: <new task with approval>. |  |  |
| 3 | Reschedule the Task | Reschedule a future instance of the <new task with approval> task for today using one of the following options:Drag and drop the task instance to the desired start date in the calendar. In the Approve dialog box, choose Approve.Open the task instance. In the Task Details dialog box, change the task instance Start Date to <today's date>. Choose OK. | The <new task with approval> task instance is rescheduled for today.As a result, the system generates a workflow item to the assignee's inbox in the background. |  |

#### Close an Incident Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager (Industrial Hygienist) closes an incident record.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open an Incident | Follow the steps described in the [Open an Incident](#unique_14) [page ] 19 section to open an incident in status New, In Process, or Reopened. | The incident <incident title text> is loaded. |  |
| 2 | Close the Incident | In the header toolbar, choose Status and select the Closed option.Choose OK in the dialog box. | When closing an incident, a check for completeness is executed in the background.Depending on the information entered for the incident, error messages are displayed for missing entries in mandatory fields. Once the missing information is filled in, it is possible to close the incident. |  |
| 3 | Fix Errors | Check the displayed error messages.Enter information in the required fields, mentioned in the error messages.Repeat the activities of step 2. | Upon successful check for completeness, the incident is set to status Closed.The incident record is read-only. |  |

### Process an Investigation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The investigation lead (Industrial Hygienist role) performs an investigation to determine the causes that led to an incident.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | In the Investigations section, open the Manage Investigations (F7969) app. | The Manage Investigations screen is displayed. |  |
| 3 | Open an Investigation Record | Choose Go.From the results list, select the investigation record you created in the [Create an Investigation](#unique_31) [page ] 49 section. | The Overview tab of the investigation record is loaded. |  |
| 4 | Start an Investigation | Navigate to the Plan tab.From the header toolbar, choose Start. | The status of the investigation is set to In Progress.The Start Date field is populated with the current date. |  |
| 5 | Plan an Investigation | In the Scope > Duration section, use the date picker to enter a future date in the Planned End Date field. | The date you selected is displayed in the Planned End Date field.The Expected Duration field appears in the header and is populated based on the start date and the planned end date. |  |
| 6 | Collect Evidence | Navigate to the Collect tab.In the Evidence section, choose Create.In the dialog, in the Type field, select Statement and choose Continue.On the evidence details page, under Details, in the Description field, enter a <free-text description>.Choose Apply. | Your entry is displayed in the Evidence table. |  |
| 7 | Start and Complete an Activity | Navigate to the Plan tab.In the Activities section, select the activity you created in step 5 of [Create an Investigation](#unique_31) [page ] 49.Choose Start to start the activity.Choose Complete to complete the activity. Confirm the dialog that appears.Choose Apply. | The activity status changes to In Progress and Completed after the respective actions. |  |
| 8 | Define a Problem | Navigate to the Analyze tab.In the Problems section, select the automatically created problem.On the problem's details page, in the Description section, in the Description field, enter a <free-text description>. | The problem is displayed in the Problems table.The problem's status is set to New. |  |
| 9 | Start Analysis | In the header of the problem's details page, choose Start Analysis.In the Start Analysis dialog, choose Why-Why from the Methodology dropdown list and choose Start Analysis. | In the Analysis section, a new entry is displayed: Why #1.The problem's status is set to Under Analysis. |  |
| 10 | Perform Analysis | In the Analysis section, select the Why #1 question and choose Add Answer.In the Add Answer dialog box, in the Answer field, enter a <free-text answer> and choose Add Answer. | The answer is saved and displayed in the table in the Analysis section. |  |
| 11 | Identify a Root Cause | In the Analysis table, select the Why #1 entry and choose Set as Root Cause in the table toolbar to set the answer as a root cause.In the Set as Root Cause dialog, enter the following information:Root Cause: <free-text root cause>Category: DocumentationPriority: Low (01)Choose Set as Root Cause.Close the problem analysis panel. | The root cause is saved and displayed in the Root Causes table. The Problem column displays the associated problem. |  |
| 12 | Add a Root Cause from a Predefined Hierarchy | In the Root Causes section, choose Add from Hierarchy.In the Select Root Cause from Hierarchy dialog, expand the Technical Factors node and select Malfunction.Choose Add.Optional: Click on the  (Show Path) icon to show the entire hierarchy path of the selected root cause. | The selected root cause is added to the Root Causes table. The Root Cause and Category fields are in read-only mode. |  |
| 13 | Enter a Recommendation | In the Recommendations section, choose Create and make the following entries:Recommendation: <free-text recommendation>Priority: MediumFrequency: Select Monthly from the dropdown list.Choose Apply.In the Root Causes section, in the Recommendation field of the root cause you added in the previous step, use the value help to assign the recommendation.Choose Save. | The recommendation is displayed in the Recommendations table and assigned to the selected root cause. |  |
| 14 | Create a Recommendation Task | On the Analyze tab, choose Edit.In the Recommendations section, open the recommendation created in the previous step (> icon).In the Tasks section, choose Create.On the New Task screen, make the following entries:Title: <free-text task title>Assignee: Select a user from the value help.Due Date: <tomorrow's date>Start Date:Before Due Date: 1Select Days from the dropdown list.Choose Create to save your entries.Choose Apply. | The task appears in display mode.After you select Apply, you're navigated back to the Analyze tab. |  |
| 15 | Complete Recommendation Task | Complete the task you created in the previous step as described under [Implement a Task](#unique_35) [page ] 58.Note You can only close the investigation after all recommendation tasks are completed. | The system sets the task status to Completed, and the investigation can be closed. |  |
| 16 | Complete Analysis | On the Analyze tab, select the problem you added in the Problems table to open its details page, then choose Complete to complete the analysis. | The status of the problem is set to Root Cause Identified. |  |
| 17 | Save Investigation | Choose Save. | All changes to the investigation record are saved. |  |
| 18 | Close Investigation | From the header toolbar, choose Close. | The status of the investigation is set to Closed.The Actual Duration field appears in the header. The actual duration of the investigation is calculated based on the start date and the end date. The end date is automatically populated on the Plan tab when an investigation is closed. |  |
| 19 | Display Investigation Report | From the header toolbar, choose Display Report. | The investigation report opens in PDF format in a separate window. |  |

### Review Workplace Safety Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager gets an overview of incidents, near misses, and safety observations and the related tasks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Workplace Safety Overview (F7512). | The initial screen of the app is displayed.Note If you've set your preferred location in the Set My Location app, this location is populated in the Location global filter, and the app displays data for this location and its sublocations. |  |
| 3 | Set Location | Choose the header of the My Location card.In the Set My Location app, select the Division ABC location, then choose Set as "My Location".Choose Back (< icon).Alternatively, you can enter the Division ABC location in the Location filter and choose Go. | The Workplace Safety Overview screen is displayed.The selected location is displayed on the My Location card, and the information on the rest of the cards is updated. |  |
| 4 | Edit Filters | On the Active Incidents Overview card, select By Status from the dropdown menu.On the Recent Incidents card, select Incident.On the Active Incidents Over Time card, select Incident. | The data on the corresponding cards is updated according to the selected filters. |  |
| 5 | Manage Cards | To customize the cards on the overview page, choose the user icon on the screen, then Manage Cards. Make the settings of your choice, and choose OK. | The cards on the overview page can be rearranged, hidden, and displayed again. |  |

### Additional Process Steps (Optional)

#### Create Incident by Category

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident happened and an incident manager (Industrial Hygienist) creates a record for it in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Incidents - Incident Management (F4759). | The Manage Incidents screen is displayed.In the filter area, a free-text search field and the following filters are available:Incident CategoryDateLocationInclude SublocationsInvolved PersonGroupStatus |  |
| 3 | Create an Incident | Choose Create.In the Create dialog box, in the Incident Category field, select Incident and choose Continue. | The Incident screen is loaded. |  |
| 4 | Enter Incident Details | In the Event section, under Description, fill in the following fields:Title: <incident title text>.Description of Events: <description of events>.Immediate Actions: Describe the actions that were taken immediately after the incident occurred. | The changes are saved. |  |
| 5 | Assign a Location | Navigate to the Location tab.In the Assignment section, in the Location field, use the value help to select the Division ABC location. | The name and ID of the selected location are displayed in the Location field. |  |
| 6 | Add an Injured Person | Navigate to the People tab.Choose Add and use the value help to select a person. Select the checkbox for the Injured Person role and choose OK. | The injured person is added to the People table. |  |
| 7 | Save Incident Record | Choose Save. | The incident record is saved. |  |

#### Manage Hours Worked

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager adds records of hours worked for different locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. |  |  |
| 2 | Access App | Open Manage Hours Worked - Incident Management (F3372). | The Manage Hours Worked screen is displayed.The following filter criteria are available:Editing Status: with default value AllWork Period: initially <empty>Location: initially <empty>Include Sublocations: YesWorker Type: initially <empty> |  |
| 3 | Add Hours Worked | Choose Create.On the New Record screen, enter the following information:Location: Use the value help to select the location Division ABC.Note You can find the location in the location structure, or search by Location Name, Location ID, and Location Type.Start Date: 01.01.2020End Date: 31.01.2020Hours Worked: 1760Number of Workers: 10Worker Type: EmployeeNote The start date and the end date of a work period must be the first and the last day of the same month.Choose Create.Tip Alternatively, you can use the Import from Spreadsheet functionality to download a template file that you can fill in and upload to the system. | The newly added record is saved. |  |
| 4 | Edit Hours Worked | Select the newly created record in the Records table.Choose Edit.Replace the Hours Worked entry with 2500.Choose Save. | The changes are saved and updated in the Records table. |  |
| 5 | Delete Hours Worked | Add another record for hours worked, as described in step 3, using the following data:Start Date: 01.02.2020End Date: 29.02.2020Choose Delete.Choose Delete in the dialog box. | The newly added record is deleted. |  |

#### Manage Summary Reports

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Incident summary reports are generated for legal purposes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. |  |  |
| 2 | Access App | Open Manage Summary Reports - Incident Management (F4758). | The Manage Summary Reports screen is displayed.A free-text search field and the following filter criteria are available:Editing Status: AllReporting Period: initially emptyLocation: initially emptyInclude Sublocations: YesForm Type: initially empty |  |
| 3 | Create OSHA 300 Summary Report | Choose Create, then select OSHA 300 (Log of Work-Related Injuries and Illnesses) in the Select Form Type dialog box.On the next screen, use the value help to fill in the following information:Date From: 01.02.2020.Date To: 29.02.2020.Location: Division ABC.Language: EN.Choose Create. All input fields become read-only.Choose Generate to generate the report file. | After you choose Generate, a message is displayed that the generation of the report has started.When the report has been generated, the Report File section appears on the screen and contains the following information:File Name: Contains a link to the generated report file.Generated On/At: Displays the report generation date.Status: Generation Finished.Note The procedure to generate OSHA 300A and OSHA 300A CSV reports follows the same steps.The OSHA 300A and the OSHA 300A CSV reports additionally contain the NAICS Code and Industry Description fields.The OSHA 300A CSV report also contains the Establishment Size, Establishment Type, and Reason for Change fields. |  |
| 4 | Navigate to Manage Summary Reports List | Choose Back (< icon) to navigate back to the Manage Summary Reports screen. | The record for the newly created OSHA 300 report is displayed in the Reports table.Note If the newly created record is not visible by default, you can reload the page or choose Go to update the search results.The report counter, which is visible in the header of the table, is increased by 1. |  |
| 5 | Preview OSHA 300 Summary Report | Choose the link to the OSHA 300 report file in the File Name column. | The OSHA 300 report file is loaded. |  |
| 6 | Delete OSHA 300 Summary Report (Optional) | Select a record in the Reports list.Choose Delete.Choose OK in the dialog box. | The report is deleted. |  |

#### Manage Injury/Illness Log

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An incident is created based on an injury/illness log entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Injury/Illness Log Entry (EHHSS_INC_REC_OIF_V3). | The Injury/Illness Log screen is displayed.Note Alternatively, you can open Manage Injury/Illness Log (F4026) and choose Create. |  |
| 3 | Enter Basic Information | In the Basic Information tab, make the following entries:Type of Injury/Illness Log Entry: select a type via the value helpIn the Date and Time section:Date/Time: 17.02.2020, 15:00, UTCIn the Incident Location section:Location: Division ABCPlant ID: select a plant ID via the value help |  |  |
| 4 | Add an Injured Person | Navigate to the People tab.In the People section, choose Add.In the Choose Person dialog box, make the following entries and choose OK:Involved Person: select a person via the value helpSelect the Injured Person role. | The selected injured person is added to the People table and the following subtabs for the person are displayed:Basic InformationAid/Follow-Up TreatmentInjuries/IllnessesTreatment |  |
| 5 | Enter Aid/Follow-Up Treatment Information for the Injured Person | In the Aid/Follow-Up Treatment subtab for the injured person, choose Add.Use the value help to select Aid Given Type and Actual Date.In the Additional Information section, enter a person in the Responsible Person field. | The selected responsible person is added to the People table. |  |
| 6 | Add Injuries/Illnesses Information for the Injured Person | In the Injuries/Illnesses subtab for the injured person, choose Add, and make the following entries:Classification: InjuryInjury/Illness Type: use the value help to select Injuries to the wrist and handInjury/Illness Description: <additional information for the injury>Body Part: use the value help to select Palm of HandBody Part Description: <additional information for the palm>Body Side: use the value help to select Left |  |  |
| 7 | Add Treatment Information for the Injured Person | In the Treatment subtab for the injured person, make the following entries:First Aid Location: use the value help to select a locationFirst Physician: use the value help to select a first physicianFurther Treatment Provider: use the value help to select a further treatment providerTreatment Beyond First Aid: YesEmergency Room: YesImpatient Overnight: YesUnconsciousness: NoImmediate Resuscitation: NoIn the Transportation section, make the following entries via the value help:To First Aid: AmbulanceTo Further Treatment: Ambulance | The selected first physician and further treatment provider are added to the People table. |  |
| 8 | Add Documents to the Injury/Illness Log Entry | Navigate to the Documents tab and choose Add.Choose a file and reference it to the injury/illness log. | The selected document is added to the Documents table. |  |
| 9 | Save Your Entries | Choose Save. | The data is saved, the injury/illness log entry ID is displayed in the header, and the status is changed to In Process. |  |
| 10 | Create an Incident Based on an Injury/Illness Log Entry | Choose Create Incident. | An incident is created based on the information from the injury/illness log entry. A success massage is displayed with the incident ID. |  |
| 11 | Close the Injury/Illness Log Entry | Choose Set Status and select Closed from the dropdown list.Choose OK to confirm the warning message. | The status of the injury/illness log entry is changed to Closed and the record cannot be edited. |  |

#### Manage Electronic Submissions of Injury and Illness Data to OSHA (USA)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The incident manager submits injury and illness data electronically to the Occupational Safety and Health Administration (OSHA) in the USA.

Prerequisites

Carry out the following steps:

1. Create an account in the preview environment of OSHA's Injury Tracking Application (ITA).
2. In the preview environment of the ITA, create an establishment.
3. Set up the integration scenario according to the Set-Up Instructions.
4. Create a location with the information of the establishment you created in the ITA.
    1. Open the Manage Locations app, create or select a location, then navigate to the Identification tab.
    2. Add the Establishment ID and Establishment Name identifiers using the information you entered in the ITA.
    3. Save your entries.
5. Create an incident with the following information (see [Capture an Initial Incident Record](#unique_12) [page ] 12).
    1. Location: Select the location you created in the previous step.
    2. Injured Person: Add at least one injured person.
6. Update the newly created incident.
    1. Assign the OSHA (USA) regulation to the incident. For more information, see [Manage Details](#unique_15) [page ] 21.
    2. Set the Incident Type to Work-Related Incident. See [Enter Details for Persons with Special Roles](#unique_19) [page ] 28.
    3. Adjust the incident data according to OSHA's criteria for recordable cases, for example, set the Additional Criteria field to Needlesticks and Sharps Injury.
    4. Generate an OSHA 301 report form (Injuries and Illnesses Incident Report) for the injured person. See [Create and Send an Incident Report](#unique_32) [page ] 51.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Industrial Hygienist. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Electronic Submissions (F8152). | The Manage Electronic Submissions screen is displayed. |  |
| 3 | Create an Electronic Submission | Choose Create.In the Create dialog box, make the following selections and choose Continue:Location: the location for which you have specified an Establishment ID and Establishment Name.Regulation: OSHA (USA).On the Electronic Submission screen, choose Create. | The Electronic Submission screen is displayed.The From Date and To Date fields are populated with the first and the last day of the current year.In the header, the status of the electronic submission is set to Not Generated. |  |
| 4 | Generate Data | In the header toolbar, choose Generate Data. | In the header, the status is set to Not Sent. |  |
| 5 | Send Data | In the header toolbar, choose Send Data. | In the header, the status is set to Not Submitted. |  |
| 6 | Complete Submission | In the header toolbar, choose Complete Submission. | In the header, the status of the electronic submission is set to Submitted. |  |

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
- see-also :: [[13-quality-ehs-and-compliance/test-script-audit-and-inspection-management-for-ehs-7z7-1241]]
- see-also :: [[13-quality-ehs-and-compliance/ehs-lokation-anlegen-sds-3sr-358]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3FP_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 148,058 chars in the whole document
