---
id: 14-maintenance-service-and-projects/collaborative-project-management-6jn-test-script-sap-s-4hana-cloud-pub
title: "Collaborative Project Management (6JN) - Test Script, SAP S/4HANA Cloud Public Edition (6JN_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 6JN: step-by-step tests of collaborative project initiation, planning and execution in SAP Project and Resource Management."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/internal-and-collaborative-projects]
aliases: [6JN_S4CLD2608_BPD_EN_XX]
keywords: [Internal and Collaborative Project Management, collaborative projects, project initiation, project partners, project plans, project scheduling, risk management, task management, issue management, document management]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6JN_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1174
topic: 14-maintenance-service-and-projects/internal-and-collaborative-projects
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Collaborative Project Management (6JN) - Test Script, SAP S/4HANA Cloud Public Edition (6JN_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6JN_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Internal and Collaborative Project Management** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Collaborative Project Management (6JN)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Collaborative Project Management (6JN) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232841562)

[2 Prerequisites 4](#_Toc232841563)

[2.1 Additional Manual Configuration (Optional) 4](#_Toc232841564)

[2.2 System Access 4](#_Toc232841565)

[2.3 Roles 5](#_Toc232841566)

[2.4 Business Conditions 5](#_Toc232841567)

[3 Overview Table 6](#_Toc232841568)

[4 Test Procedures 8](#_Toc232841569)

[4.1 Project Initiation 8](#_Toc232841570)

[4.1.1 Create Project Collaboration via Project Briefs App for Enterprise Projects 8](#_Toc232841571)

[4.1.2 Create Project Collaboration via My Collaborative Projects App 10](#_Toc232841572)

[4.1.3 Upload Legal Documents 11](#_Toc232841573)

[4.1.4 Invite Stakeholders 12](#_Toc232841574)

[4.1.4.1 Team Member 12](#_Toc232841575)

[4.1.4.2 Invite Project Partner 13](#_Toc232841576)

[4.1.5 Define Project Plan 14](#_Toc232841577)

[4.1.5.1 Import Project Plan 14](#_Toc232841578)

[4.1.5.2 Create Project Plan 16](#_Toc232841579)

[4.1.5.2.1 Create Workpackage 18](#_Toc232841580)

[4.1.5.2.2 Create Milestone 19](#_Toc232841581)

[4.2 Project Planning 21](#_Toc232841582)

[4.2.1 Refine Project Structure for Operational Planning 21](#_Toc232841583)

[4.2.2 Schedule Project 22](#_Toc232841584)

[4.2.3 Identify & Capture Risks 25](#_Toc232841585)

[4.2.4 Share Execution Plan 27](#_Toc232841586)

[4.2.5 Define and Assign Tasks 28](#_Toc232841587)

[4.3 Project Execution 29](#_Toc232841588)

[4.3.1 Execute Tasks 30](#_Toc232841589)

[4.3.2 Document Issues 31](#_Toc232841590)

[4.3.3 Upload Documents 32](#_Toc232841591)

[4.3.3.1 Share and Approve Documents 34](#_Toc232841592)

[4.3.4 Monitor and Mitigate Risks 35](#_Toc232841593)

[4.3.5 Establish References with Relevant Business Objects 37](#_Toc232841594)

[5 Appendix 39](#_Toc232841595)

[5.1 Process Integration 39](#_Toc232841596)

[5.1.1 Preceding Processes 39](#_Toc232841597)

[5.1.2 Succeeding Processes 39](#_Toc232841598)

## Purpose

Overview

SAP Project and Resource Management enhances the project management capabilities of SAP Cloud ERP by providing intuitive tools for collaborative project planning and execution. With features such as project structuring, project scheduling, document handling, and built-in task and issue tracking, it enables project managers to plan effectively, coordinate stakeholders, and execute projects with greater accuracy and transparency.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

Testing in a 3-System Landscape

In a 3-system landscape with SAP Central Business Configuration as your configuration environment, changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape.

A synchronization is required, for example, after you have enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer [product assistance](https://help.sap.com/viewer/b249d650b15e4b3d9fc2077ee921abd0/latest/en-US/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal

Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert of your organization to upgrade the configuration content and deploy the configuration data to your system landscape.

### Additional Manual Configuration (Optional)

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/9b0993580d410161bcbfbc2eec538270)

### System Access

| System | Details |
| --- | --- |
| System | Accessible through SAP Fiori launchpad. Your system administrator will provide you the URL to access the various apps assigned to your role. |
| SAP Project and Resource Management | Your system administrator provides you with the URL of the SAP Project and Resource Management application in BTP.For more information on Project Management, search for SAP Project and Resource Management. Choose Administration Guide for Project Management in SAP Project and Resource Management under the Administration section on SAP Help Portal. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template)ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Project Manager | SAP_BR_PROJECTMANAGER | Project Management | SAP_BR_PROJECTMANAGER |  |

Required Roles or Role Collection for Project Management in SAP Project and Resource Management application users

1. Open [https://help.sap.com](https://help.sap.com).
2. Search for SAP Project and Resource Management in the search box and chooseSAP Project and Resource Management under the Suggested Products section.
3. In the Administration section, choose Administration Guide for Project Management in SAP Project and Resource Management.
4. Check the chapter under the User Management section.

|  |
| --- |
| Note Please Assign the c4p-copm-projectmanager role collection to project manager and assign c4p-copm-projectmember role collection to project team member to execute the respective steps successfully. |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1NT – Project Control – Finance | A project must be created and preliminary costing has been done on the project. |

## Overview Table

This scope item consists of the process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all the other apps that are not included on the homepage using the search bar.If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Project Initiation

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Project Collaboration via Project Briefs App for Enterprise Projects](#unique_8) [page ] 8 | Project Manager | Project Briefs (F2602) |  |
| [Create Project Collaboration via My Collaborative Projects App](#unique_9) [page ] 10 | Project Manager | My Collaborative Projects (F3145) |  |
| [Upload Legal Documents](#unique_10) [page ] 11 | Project Manager | My Collaborative Projects (F3145) |  |
| [Team Member](#unique_11) [page ] 12 | Project Manager | My Collaborative Projects (F3145) |  |
| [Invite Project Partner](#unique_12) [page ] 13 | Project Manager | My Collaborative Projects (F3145) |  |
| [Import Project Plan](#unique_13) [page ] 14 | Project Manager | My Collaborative Projects (F3145) |  |
| [Create Workpackage](#unique_14) [page ] 18 | Project Manager | Manage Project Plans (F5671) |  |
| [Create Milestone](#unique_15) [page ] 19 | Project Manager | Manage Project Plans (F5671) |  |

Project Planning

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Refine Project Structure for Operational Planning](#unique_16) [page ] 21 | Project Manager | Manage Project Plans (F5671) |  |
| [Schedule Project](#unique_17) [page ] 22 | Project Manager | Manage Project Plans (F5671) |  |
| [Identify & Capture Risks](#unique_18) [page ] 25 | Project Manager | My Collaborative Projects (F3145) |  |
| [Share Execution Plan](#unique_19) [page ] 27 | Project Manager | My Collaborative Projects (F3145) |  |
| [Define and Assign Tasks](#unique_20) [page ] 28 | Project Manager | My Collaborative Projects (F3145) |  |

Project Execution

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Execute Tasks](#unique_21) [page ] 30 | Project Team Member | My Collaborative Projects (F3145) |  |
| [Document Issues](#unique_22) [page ] 31 | Project Manager | My Collaborative Projects (F3145) |  |
| [Share and Approve Documents](#unique_23) [page ] 34 | Project Team Member | My Collaborative Projects (F3145) |  |
| [Monitor and Mitigate Risks](#unique_24) [page ] 35 | Project Team Member | My Collaborative Projects (F3145) |  |
| [Establish References with Relevant Business Objects](#unique_25) [page ] 37 | Project Manager | My Collaborative Projects (F3145) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Project Initiation

#### Create Project Collaboration via Project Briefs App for Enterprise Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager creates Project Collaboration in the Project Management capability of SAP Project and Resource using Project Brief App.

|  |
| --- |
| Note The following Business Process must be executed before you execute this process step:1NT – Project Control – Finance |

Prerequisite

The following Business Process Step must be run from 1NT – Project Control – Finance Script before this step:

- Create Project

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager. |  |  |
| 2 | Access App | Open the Project Briefs (F2602) |  |  |
| 3 | Open the Project | From the Worklist displayed, choose the project. | Project screen displays. |  |
| 4 | Create Collaboration | Choose Edit to change the project from Display to Edit mode.Choose the Related Objects section and choose Create.In the Related Objects section, the Object Type and Object are automatically created.Choose Save. | A system message notifies you that the collaboration will be created after saving.The collaboration or collaboration project is created and a link to it is added in the Related Objects table of project briefs.Note If a user is executing this action for the first time, then another dialog pops up, which explains that the user has to first get authorized in the Project Management capability of SAP Project and Resource Management.For this, the user has to copy-paste the URL, which is displayed in the dialog. After that the access token is stored on the S4 side that is technically needed to call the SAP Project and Resource Management API to create a collaborative project. |  |
|  | Navigate to My Collaborative Project | Click hyperlink of object type in the Related Objects table of the project brief. | It will navigate to the “My collaborative project App” in the same session.Please note: The required project will be shown if the logged in user is the same user who created the project in Project Control - Enterprise Projects App in S/4 System or if the project manager or the person navigating is invited and active in the system in manage Project Partners. |  |
|  | Navigate to My Collaborative Project | Open Projects Brief (F2602) appFrom the Worklist displayed, select the projectClick hyperlink and choose My Collaborative Projects. | It will navigate to the “My collaborative project “App with the Project name and Project ID as the filter.“My collaborative project” App opened in a new tab.Please note: The required project will be shown if the logged in user is the same user who created the project in Project Control - Enterprise Projects App in S/4 System.If the logged in user for the BTP application is Project Manager, he sees the project name and Project filters, but no project is displayed.If the logged in user for the BTP application is proj_fin_controller, he sees the project name and Project filters, and specified project is displayed. |  |

#### Create Project Collaboration via My Collaborative Projects App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager directly creates Project Collaboration in the connected SAP Project and Resource Management system by navigation through the UI from SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager. |  |  |
| 2 | Access the App. | Open My Collaborative Projects (F3145) app. | My Collaborative Projects screen is displayed. |  |
| 3 | Create Collaboration Project. | Choose Create on the My Collaborative Projects screen.Make the following entries in the Create project pop up screen.Name: <Collaborative Project Name>ID: Suitable id for the collaborative project to be created <Example: ABC.XYZ>Start Date: Suitable start dateEnd Date: Suitable end dateLocation: <Optional> Suitable location or address of the project, if applicable.Choose Create. | A collaborative Project is created with the provided parameters. |  |

#### Upload Legal Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager upload legal documents. This is mandatory to invite project partners.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management in SAP Project and Resource Management as a Project Manager. |  |  |
| 2 | Access App | Open My Collaborative Projects(F3145) app. | The My Projects screen appears. |  |
| 3 | Open the Project | From the Projects list displayed, select the project and click to open the project | The Project Details screen is displayed. |  |
| 4 | Upload Data Privacy Statement | From Header section, select Data Privacy Statement field.Click on Browse to Select Legal Document.Select applicable legal document and click Open.Click on Upload to upload document in collaborative project. | Message ‘Document Uploaded’ appears on screen. |  |
| 5 | Upload Terms of Use | From Header section, select Terms of Use field.Click on Browse to Select Legal Document.Select applicable legal document and click Open.Click on Upload to upload document in collaborative project. | Message ‘Document Uploaded’ appears on screen. |  |
| 6 | Save Project | Click on Save to save the project. |  |  |

#### Invite Stakeholders

##### Team Member

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager invites internal stakeholders to the Collaboration project such as partners from various disciplines to collaborate on the project created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management in SAP Project and Resource Management as a Project Manager. |  |  |
| 2 | Access App | Open My Collaborative Projects(F3145) app. | The My Projects screen appears. |  |
| 3 | Open the Project | From the Projects list displayed, select the project and click to open the project | The Project Details screen is displayed. |  |
| 4 | Navigate to Project Partner Details. | Scroll down to the Project Partners section and select a colleague from the existing list of project partners to be invited to the project. | The Project Partner Details screen is displayed. |  |
| 5 | Add User | Under Users section click Add. | Add User screen is displayed. |  |
| 6 | Invite Team Member | From the User list select the User to be added and Choose InviteNote:We can also Invite the External Stakeholders to the Project who are not part of the list shown in the Add User screen by clicking on Add button and providing the User Name and Email of the user.The Invited Team Member should accept the Invite received by logging in to the My Collaborative Projects App under Invites section to successfully access the Collaborative project to which he been invited and perform the task assigned during the Project Execution Phase. | Invitation is sent to the user with the link to access |  |

Note: The User List in the Add User screen includes all users of the selected company which have activated the visibility flag in the User profile.

##### Invite Project Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager invites project partners to collaborate on the project.

The project management capability offers a business network for the execution of projects. The projects can either be internal projects or cross-company projects. You can set up a project and invite users from various project partners to collaborate on the project

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management in SAP Project and Resource Management as a Project Manager. |  |  |
| 2 | Access App | Open My Collaborative Projects(F3145) app. | The My Projects screen appears. |  |
| 3 | Open the Project | From the Projects list displayed, select the project and click to open the project. | The Project Details screen is displayed. |  |
| 4 | Navigate to Project Partner Details. | Scroll down to the Project Partners section and selectInvite New PartnerNote: Once you select Invite New Partner, the system displays the list of companies who have made themselves visible for invitations. Companies can make themselves visible for invitations by changing the visibility settings in the My Company Profile app. You can either invite companies from the list of available companies or add a new company by selecting New Company. | The Invite Project Partner screen is displayed. |  |
| 5 | Add Project Partner | Select Project Partner Company | The Invite Project Partner-Details screen is displayed. |  |
| 6 | Add Company role | In the details screen, make the following entry and select a user from the users list and press Invite.Company Role: <Partner Company Role>I.e: Design Review | Invitation Screen is displayed |  |
| 7 | Write Custom Invitation text | In the Invitation screen, make the following entry and Press SendCustom Text: <Enter Custom Text>Note: Once you send an invitation e-mail to the selected user from the invited company, the user becomes the company representative for the selected company role and is also marked as the key contact of the company in the collaborative project.Note: You can also Invite the External Stakeholders to the Project who are not part of the list shown in the Add User screen, for this click on the Add button and provide the User Name and e-mail of the user. | Selected user is invited for collaboration project with the link to access. |  |

#### Define Project Plan

##### Import Project Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you will be able to import the plan for the collaboration project from SAP S/4HANA Cloud Public Edition system (External System) for both Enterprise & Professional Services projects.

|  |
| --- |
| Note Either of the below Business Process must be executed before you execute this process step:1NT – Project Control – FinanceJ11 – Customer Project Management – Project-Based Services1A8 – Internal Project – Project-Based Services |

Prerequisite

The following Business Process Step must be run from 1NT – Project Control – Finance Script before this step:

- Create Project

The following Business Process Step must be run from J11 – Customer Project Management – Project-Based Services before this step:

- Create a New Customer Project
- Create a New Internal Project

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Manager. |  |  |
| 2 | Access App | Open Manage Project Plans (F5671) app. | The My Project Plans screen is displayed. |  |
| 3 | Create Project Plan | Choose Create and select From Other System from the drop-down. | The Create from Other System pop screen is displayed. |  |
| 4 | Make the entries | Make the following entries in the Create from Other System pop screen:Under Select a collaborative project and a source system SectionCollaborative Project: Select a collaborative project to which the project plan is to be imported.Source system: Select the source system from which the project plan is to be imported.Project from Source System:You can search and select the desired project from the source system using the value help.Note To display only those projects from the source systems that are linked as related object in the selected collaborative project, select Created in collaborative project check box.Choose Go.Under Projects SectionChoose the project whose Is Imported status is No.Choose Continue.Next choose Create.Note You can import only those projects from the source system that haven’t yet been imported to any collaborative project across your organization. | Plan is created with provided parameters. A project plan is created. The plan is prefilled with the project hierarchy of the project that is imported. |  |

##### Create Project Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you will create the plan in SAP Project and Resource Management as a Project Manager. This step is relevant for project plans that are linked to SAP S/4HANA Cloud projects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Manager. |  |  |
| 2 | Access App | Open My Collaborative Projects (F5671) app. | The Manage Project Plans screen is displayed. |  |
| 3 | Create Project Plan | Choose Create and select From New Plan from the drop down | The New Plan pop screen is displayed. |  |
| 4 | Make the entries | Make the following entries in the New Plan pop screen:ID: Suitable id for the collaborative project to be created <Example: ABC.XYZ>Name: Suitable <Collaborative Project Name>Collaborative Project: Select a collaborative project to which the project plan is to be importedClick New Plan. | The Project Plan details screen is displayed. |  |
| 5 | Make the entries | Make the following entries in the Project Plan details pop screen:Under Dates SectionPlanned Start: Suitable start datePlanned Finish: Suitable end dateActual Start: Suitable start dateActual Finish: Suitable end dateForecast Start: Suitable start dateForecast Finish: Suitable end datePlanned Duration: Automatically calculated based on the respective start and end datesNote You can also manually enter a value in the Duration field. Based on the date selected in the start field, the date in the respective finish field is automatically calculated. It isn’t possible to define the actual duration manually.Click Create. | The Project Plan details screen is displayed. |  |

###### Create Workpackage

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you will create work packages for the new Project Plan created before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Manager. |  | Log On |
| 2 | Access App | Open Manage Project Plans (F5671) app. | The Manage Project Plans screen is displayed. | Access App |
| 3 | Enter the Collaborative Project | In the Manage Project Plans screenUnder selection parametersCollaborative Project: Enter a collaborative project which is created in the either section 4.1.1 or 4.1.2Click Go. |  |  |
| 4 | Select the Project Plan and Edit | From the Project Plans list displayed Under Project Plans Section, select the project plan which is created in the section 4.1.5.2 and click to open the projectClick Edit to open the project plan in change mode. | The Project Plan Details screen is displayed. |  |
| 5 | Create Work Package | Select the Project Element and Click Create select Work Package from the drop downNote You need to select a project element to make the Create button active. | The Project Plan Details screen is displayed. |  |
| 6 | Make the entries | Make the following entries in the Project Plan details pop screen:Under Project Elements SectionName: Suitable work package nameID: Suitable work package namePlanned Start: Suitable start datePlanned Finish: Suitable end dateActual Start: Suitable start dateActual Finish: Suitable end dateForecast Start: Suitable start dateForecast Finish: Suitable end datePecentage of Completion: Maintain as requiredNote The value in the Duration field is automatically calculated based on the dates selected in the respective start and end dates. You can also manually enter a value in the Duration field. Based on the date selected in the start field, the date in the respective finish field is automatically calculated based on the duration entered.Click Save. | The Project Plan details screen is displayed. |  |

###### Create Milestone

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you will create work packages for the new Project Plan created before.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Manager. |  | Log On |
| 2 | Access App | Open Manage Project Plans (F5671) app. | The Manage Project Plans screen is displayed. | Access App |
| 3 | Enter the Collaborative Project | In the Manage Project Plans screenUnder selection parametersCollaborative Project: Enter a collaborative project which is created in the either section 4.1.1 or 4.1.2Click Go. |  |  |
| 4 | Select the Project Plan and Edit | From the Project Plans list displayed Under Project Plans Section, select the project plan which is created in the section 4.1.5.2 and click to open the projectClick Edit to open the project plan in change mode. | The Project Plan Details screen is displayed. |  |
| 5 | Create Milestone | Select the Project Element and Click Create select Milestone from the drop downNote You need to select a project element to make the Create button active. | The Project Plan Details screen is displayed. |  |
| 6 | Make the entries | Make the following entries in the Project Plan details pop screen:Under Project Elements SectionName: Suitable milestone nameID: Suitable milestone namePlanned Finish: Suitable end dateActual Finish: Suitable end dateForecast Finish: Suitable end dateClick Save. | The Project Plan details screen is displayed. |  |

### Project Planning

#### Refine Project Structure for Operational Planning

Purpose

In this activity, You can manage the duration of the work packages and also define relationships and relationship types between project elements on the project element details page and in the Gantt chart.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Manager. |  | Log On |
| 2 | Access App | Open Manage Project Plans (F5671) app. | The Manage Project Plans screen is displayed. | Access App |
| 3 | Enter the Collaborative Project | In the Manage Project Plans screenUnder selection parametersCollaborative Project: Enter a collaborative project which is created in the Project Initiation Phase.Click Go. |  |  |
| 4 | Receive Updates | choose Sync Actions button on top right corner ans select Receive Updates from the drop down to get the latest version of the project plan from the source system.Select a work package to change its attributes.Note For detailed information about which project elements can be edited depending on their processing status, visit [https://help.sap.com/docs/](https://help.sap.com/docs/) and search for User Guide for Project Management in SAP Project and Resource Management. Then refer to the Editing Imported Project Plans chapter under the Manage Project Plan section within Applications in Project Management | The Project Plan Details screen is displayed. |  |
| 5 | Select the Project Plan and Edit | From the Project Plans list displayed Under Project Plans Section, select the project plan and click to open the projectClick Edit to open the project plan in change mode. | The Project Plan Details screen is displayed. |  |
| 6 | Optional:Maintain Duration of Work Packages According to your Requirement | Under Projects Elements SectionChoose the work package for which you want to update the Planned duration by adjusting the Planned Start and Planned Finish according the latest stage of the project | The Project Plan Details screen is displayed. |  |
| 7 | Create Relationships between Project Elements through Projects Elements Details Page | Under Projects Elements SectionChoose small arrow (>) to Navigate to the Work Package details screenScroll down to the Plan Related Elements section and choose Create.Select a Project element (target) that you want to link with the Project element (source).Select the Relationship (either Predecessor or Successor).Select a Relationship type (Finish to Start)Choose Save.You can create multiple relationships simultaneously.Note For more information on project elements relationships types open [https://help.sap.com](https://help.sap.com/docs/) and see the Relationships between Project Elements under Manage Project Plan section of the User Guide for Project Management for SAP Project and Resource Management. | The Project Plan Details screen is displayed. |  |
| 8 | Create Relationships between Project Elements through Gantt Chart | Under Projects Elements SectionSelect the predecessor project element in the Gantt chart.Based on what relationship you want to create, link the predecessor project element to the successor project element.For example, if you want to create a Finish to Start relationship, link the end of the predecessor project element to the start of the successor project element.Note You can right click on Relationship and change the relationship type, if required.3. Choose Save. | The Project Plan Details screen is displayed. |  |

#### Schedule Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

Ensure that the required planned date and duration entries are maintained and that the required relationships among project elements are established. The actual and forecast start and finish dates are not involved in scheduling.

Ensure that the hierarchy is maintained as well as the Finish to Start relationships among project elements.

Purpose

In this activity, we organize project elements and set deadlines for them. It helps ensure that the project is completed on time, improving the overall project management efficiency. This feature allows you to run scheduling on a project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Manager. |  | Log On |
| 2 | Access App | Open Manage Project Plans (F5671) app. | The Manage Project Plans screen is displayed. | Access App |
| 3 | Enter the Collaborative Project | In the Manage Project Plans screenUnder selection parametersCollaborative Project: Enter a collaborative project which is created in the Project Initiation PhaseClick Go. |  |  |
| 4 | Select the Project Plan and Edit | From the Project Plans list displayed Under Project Plans Section, select the project plan and click to open the projectClick Edit to open the project plan in change mode. | The Project Plan Details screen is displayed. |  |
| 5 | Manage Date Constraints through Projects Elements Details Page | Under Projects Elements SectionChoose small arrow (>) to Navigate to the Work Package details screenScroll down to the Date Constraints section and select start and finish date constraint types.Note If the project element has no planned start or finish date, the field of constraint start or finish date will be left empty and you can fill them by typing in the input field or choosing a date from the calendar. | The Project Plan Details screen is displayed. |  |
| 6 | Manage Date Constraints through Actions Button | From the project plan hierarchy, select the work packages or milestones that you want to set or remove date constraints. Select Actions and you can choose Set Date Constraints or Remove Date Constraints.Note As Actions button serves as a shortcut for date constraints management, you can only set Must Start On and Must Finish On constraints simultaneously or remove all constraints together. For more information on Date Constraints open https://help.sap.com and see the Date Constraints under Manage Project Plan section of the User Guide for Project Management for SAP Project and Resource Management. |  |  |
| 7 | Manage Date Constraints through Gantt Chart | Under Projects Elements SectionIn the Gantt chart, right-click the selected work packages or milestones to set or remove date constraints. You can choose Set Date Constraints or Remove Date Constraints. In the flyout submenu, you can independently choose the start or finish date constraints.In Start Date Constraint and Finish Date Constraint column of project plan hierarchy, select start and finish date constraint types and the constraint start and finish dates are filled automatically by the planned start and finish date if they are available.Note These two columns are not displayed by default in the project plan hierarchy. To include them, you can choose the Settings icon, select Start Date Constraint and Finish Date Constraint, and choose OK. |  |  |
| 8 | Schedule the Project | Choose Schedule.Note For more information on Scheduling types open visit [https://help.sap.com/docs/](https://help.sap.com/docs/) and see the Scheduling Types under Manage Project Plan section of the User Guide for Project Management for SAP Project and Resource Management.For more information on Total Float open visit [https://help.sap.com/docs/](https://help.sap.com/docs/) and see the Critical Project Elements under Manage Project Plan section of the User Guide for Project Management for SAP Project and Resource Management.Note For the projects which are imported from SAP S/4HANA Cloud Public Edition, all the project elements can be edited, except those marked with the Processing Status of Complete, Locked, or Closed.Note • If you don’t enter a duration for a child work package, the duration is set to 1 day by default. • If there are relationship conflicts between child work packages, you can’t complete scheduling the project before you resolve the conflicts.Note If you make any changes to work packages after you run scheduling, the system will not automatically reschedule the project. You will have to click Schedule again to run scheduling.Choose Save. | Project plan is scheduled |  |
| 9 | Optional: Check Send Staus | Choose Sync Actions button on top right corner and select Check Send Status from the drop down to check the sync status of the plan with the source system.Note For more information on Sync Actions,visit [https://help.sap.com/docs/](https://help.sap.com/docs/) and search for User Guide for Project Management in SAP Project and Resource Management. Then refer to the Editing Imported Project Plans chapter under the Manage Project Plan section within Applications in Project management. | The Project Plan Details screen is displayed. |  |

#### Identify & Capture Risks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can define risks to the project elements that have a negative impact on project activities with a certain likelihood for the collaboration project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Team Member. |  |  |
| 2 | Access App | Open My Collaborative Projects (F3145) app. | The My Collaborative Projects screen is displayed. |  |
| 3 | Open the Project | From the Projects list, choose the project. | The Project Details screen is displayed. |  |
| 4 | Navigate to Manage Issues details | Scroll down to the Overview section and then choose Open Issues– Manage Issues. | The Open Issues– Manage Issues is displayed. |  |
| 5 | Create Issue | Choose Create on the Manage Issues screen. | The Create Issue pop screen is displayed. |  |
| 6 | Make the entries | Make the following entries in the Create issue pop screen:Subject: <Example: Delivery Delay>Type: <Example: Risk>Confidential : Select either Yes or No.Note If an issue is marked as confidential, only the responsible user is given permission to access the issue when it is created. If you subsequently change the value from "No" to "Yes", permissions that have already been granted are retained. In any case, the responsible user can manually change permissions.Category: Select the suitable category for which the task has been created.Responsible: Enter the name of either the person or the company to whom the issue must be assigned to.Priority: The priority suitable for projectDue Date: Suitable due dateDescription: Suitable description for the issueChoose Create and Open. | Issue is created with provided parameters |  |
| 7 | Type Specific Information | Make the following entries in the Issue Details screen:Under Type Specific Information section Choose Edit in the Edit Type-Specific Information pop up screen make following entries accordinglyImpact Level/ Description : Level of impact and description of the expected impact if the risk occursOccurrence Window: Timeframe in which the risk could occurEstimated Loss: Estimated loss caused by the riskFinal Loss: Final loss caused by the riskLikelihood: Likelihood of the risk occurringImpact: Severity of the impact if the risk occursRisk Score: Risk assessment (calculated from likelihood and impact)Response Type / Description: Strategy to manage the riskMitigation Cost: Cost of the risk mitigation strategyChoose Save.Note For details on how to create different type of the issues (for change requests or opportunities) please , open https://help.sap.com and see the Manage Issues under Applications in Project Management section of the User Guide for Project Management for SAP Project and Resource Management. Also you can Set Status for the Issues based on stage at which the issue is and more details refer the same source as mentioned in the above Note | The Issue Details screen is displayed. |  |

#### Share Execution Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the project manager manages the authorization of users for the project plan. The user can add, edit, and remove authorizations from users and groups.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Manager. |  |  |
| 2 | Access App | Open My Collaborative Projects (F3145) app. | The My Collaborative Projects screen appears. |  |
| 3 | Open the Project | From the My Collaborative Projects list, choose the project. | The Project Details screen is displayed. |  |
| 4 | Navigate to Project Plan Details | Scroll down to the Overview section and then choose the Project Plans – Manage Multi- Project Plans displayed. | The Manage Multi-Project Plans screen is displayed. |  |
| 5 | Open the Project Plan | From the Project Plans list displayed, choose the project plan click to open the project plan. | The Project Plan Details screen is displayed. |  |
| 6 | Navigate to Authorization | Choose small arrow (>) to Navigate to the Project details screen.Under the Authorization section, choose Add. | The Add Permission screen is displayed. |  |
| 7 | Maintain Authorization | On the Add Permission dialog box, select the users and choose Next.Under the Permission sub section, select the suitable permission for the user.Example View Only, Edit, Full ControlChoose Add.Note For details, open [https://help.sap.com](https://help.sap.com) and see the Permissions on Documents, Folders, and Links under Manage Permissions section of the Administrative Guide for Project Management.. | Permissions are created successfully. |  |

#### Define and Assign Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can define tasks to project elements and assign them to users or project partners of the collaboration project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to Project Management capability in SAP Project and Resource Management as a Project Manager. |  |  |
| 2 | Access App | Open My Collaborative Projects (F3145) app. | The My Collaborative Projects screen appears. |  |
| 3 | Open the Project | From the Projects list displayed, select the project and click to open the project. | The Project Details screen is displayed. |  |
| 4 | Navigate to Task screen | Click on Manage Tasks link to get to the app and click Create in the Manage Task screen. | The Create task pop screen is displayed. |  |
| 5 | Create & Assign Task | Make the following entries in the Create task pop up screen.Subject: <Example: Update Design Document>Description: Suitable description of the taskCategory: Select the suitable category for which the task needs to be created.Assign To: Enter the name of either the person or the company to which the task needs to be assigned.Note If you assign a task to a company, then the user listed as the key contact of that company is assigned to the task.Priority: The priority suitable for projectStart Date: Suitable start dateDue Date: Suitable end dateEffort: <Example: 8>Unit: <Example: hours>Choose Create.After creating the task, assign a project element to it by going to the Project Elements section within the task, choosing Assign, and selecting the appropriate project element. | Task is created and the relevant project element is assigned. |  |

### Project Execution

Purpose

In this activity, you can manage your projects in Project Management capability of SAP Project and Resource Management using the My Collaborative Projects application.

SAP Project and Resource Management offers a platform for collaboration between business partners in a cross-company project.

A Collaboration project provides you options where you can define and manage tasks and issues to coordinate across multiple companies and share information such as documents and project plans.

#### Execute Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can execute tasks by changing the status of the tasks of project element of a collaboration project using the drag and drop option in a particular week.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Team Member.Note Please verify that the Project Team Member role has required role collection assigned as mentioned in the Roles chapter under Prerequisites to execute this chapter and also please have the SAP Project and Resource Management application URL to access this app as Project Team Member |  |  |
| 2 | Access App | Open My Collaborative Projects (F3145) app. | The My Collaborative Projects screen appears. |  |
| 3 | Open the Project | From the Projects list, choose the project. Select the project and click to open the project | The Project Details screen is displayed. |  |
| 4 | Navigate to Task screen | Scroll down to the Tasks section and then choose Open Tasks – Manage Tasks. | The Manage Tasks screen is displayed. |  |
| 5 | Select Task | From tasks list displayed in Manage Tasks screen, choose the required task. |  |  |
| 6 | Change the task status | On the Task Details screen, choose Set Status To on the header section.On the Set Status and Percentage Completed pop up screen, make the following entries:Status: Select the required status from the drop down. The available statuses are:OpenIn ProcessCompletedBlockedPercentage Completed: Set the percentage completed. <Example: 80%>Choose Save. | Task statues is updated. |  |

#### Document Issues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can define problems or issues to project elements and assign them to users or project partners of the collaboration project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Team Member.Note Please verify that the Project Team Member role has required role collection assigned as mentioned in the Roles chapter under Prerequisites to execute this chapter and also please have the SAP Project and Resource Management application URL to access this app as Project Team Member |  |  |
| 2 | Access App | Open My Collaborative Projects (F3145) app. | The My Collaborative Projects screen is displayed. |  |
| 3 | Open the Project | From the Projects list, choose the project. | The Project Details screen is displayed. |  |
| 4 | Navigate to Manage Issues details | Scroll down to the Overview section and then choose Open Issues– Manage Issues. | The Open Issues– Manage Issues is displayed. |  |
| 5 | Create Issue | Choose Create on the Manage Issues screen. | The Create Issue pop screen is displayed. |  |
| 6 | Make the entries | Make the following entries in the Create issue pop screen:Subject: <Example: Delivery Delay>Category: Select the suitable category for which the task has been created.Responsible: Enter the name of either the person or the company to whom the issue must be assigned to.Note If you assign a task to a company, then the user listed as the key contact of that company is assigned to the task.Priority: The priority suitable for projectDue Date: Suitable due dateDescription: Suitable description for the issueChoose Create. | Issue is created with provided parameters |  |

#### Upload Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can use the Manage Documents application to upload project related documents and share them with project partners in a cross-company collaboration project.

In this app, you can also perform other document related operations like create, upload, view, download, edit, move, reference and, delete with required permissions.

|  |
| --- |
| Note It is not possible to upload multiple documents in the documents section of the issue details and task details page. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Team Member.Note Please verify that the Project Team Member role has required role collection assigned as mentioned in the Roles chapter under Prerequisites to execute this chapter and also please have the SAP Project and Resource Management application URL to access this app as Project Team Member |  |  |
| 2 | Access App | Open My Collaborative Projects (F3145) app. | The My Collaborative Projects is displayed. |  |
| 3 | Open the Project | From the Projects list, choose the project. | The Project Details screen is displayed. |  |
| 4 | Navigate to Documents | Scroll down to the Documents section and then choose Documents Changed By Me – Manage Documents . |  |  |
| 5 | Manage Document operations | On the Manage Documents screen displayed, choose Add .Option 1:Choose the New Folder option from the drop down.On the New Folder pop up screen, make the following entries and choose Create.Name: <Example:Project Documents>Description: <Example:Project Documents>Option 2:Choose the New Document option from the drop down.On the New Document pop up screen, make the following entries and choose Add.Name:<Example:Info Document>File: Choose Browse to upload the file from your local folder.Level of Detail:<Optional> Select the appropriate numberDiscipline:<Optional> Select the appropriate disciplineDescription:<Optional> Enter the appropriate descriptionNote You can only change the folder of the uploading document to a folder which is part of this collaboration project.Option 3: New LinkChoose the New Link option from the drop down.In the New URL/ Reference pop up screen, select the document from the list displayed and choose Add.URL: <Valid URL of the document>Link Name: <Example:Info Document>Description: <Enter suitable description for the document>Option 4:Choose Multiple Documents option from the drop down.In the Select Documents to upload pop up screen, make the following entries and choose Ok.Document: Choose Browse to upload the file from your local folder. | Document is created and referenced. |  |

##### Share and Approve Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can share documents with other users and project partners of the collaboration project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Team Member.Note Please verify that the Project Team Member role has required role collection assigned as mentioned in the Roles chapter under Prerequisites to execute this chapter and also please have the SAP Project and Resource Management application URL to access this app as Project Team Member |  |  |
| 2 | Access App | Open My Collaborative Projects (F3145) app. | The My Collaborative Projects screen is displayed. |  |
| 3 | Open the Project | From the Projects list displayed, select the project and click to open the project | The Project Details screen is displayed. |  |
| 4 | Navigate to Documents | Scroll down to the Documents section and then choose Documents Changed By Me – Manage Documents . |  |  |
| 5 | Open Manage Documents | From the Documents list displayed, choose the document and click to open the details of the documents . | The Manage Documents page is displayed. |  |
| 6 | Navigate to Authorizations | Under the Authorization section, choose Add. | The Add Permission screen is displayed |  |
| 7 | Maintain Authorizations | On the Add Permission dialog box, select the users and choose Next.In the Permission sub section, select the suitable permission for the user.Example View Only, Edit, Full ControlChoose Add.Note For details, open the [https://help.sap.com](https://help.sap.com) portal and see the see the Permissions on Documents, Folders, and Links under Manage Permissions section of the Administrative Guide for Project Management. | Permissions are created successfully. |  |

#### Monitor and Mitigate Risks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager keeps a check on the risks that were planned earlier and adapts the risk response appropriately, for example mitigation or avoidance. You can also update the risk dictionary description to add more details as needed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management capability in SAP Project and Resource Management as a Project Team Member.Note Please verify that the Project Team Member role has required role collection assigned as mentioned in the Roles chapter under Prerequisites to execute this chapter and also please have the SAP Project and Resource Management application URL to access this app as Project Team Member |  |  |
| 2 | Access App | Open My Collaborative Projects (F3145) app. | The My Collaborative Projects screen is displayed. |  |
| 3 | Open the Project | From the Projects list, choose the project. | The Project Details screen is displayed. |  |
| 4 | Navigate to Manage Issues | Scroll down to the Overview section and choose Open Issues - Manage Issues. | The Open Issues - Manage Issues screen is displayed. |  |
| 5 | Select the Issue/Risk and Edit | From the Issues list displayed under All Issues, select the issue and choose Edit to open the issue in change mode. | The Project Plan Details screen is displayed. |  |
| 6 | Type Specific Information | Make the following entries in the Issue Details screen:Under Type Specific Information section choose Edit in the Edit Type-Specific Information pop up screen and make the following entries accordingly:Response Type / Description: Strategy to manage the riskMitigation Cost: Cost of the risk mitigation strategyChoose Save.Note For details please, open [https://help.sap.com/docs/](https://help.sap.com/docs/) and see the Manage Issues under Applications in Project Management section of the User Guide for Project Management for SAP Project and Resource Management.You can also set status for the issues based on stage which the issue is in and more details refer the same source as mentioned in the above note.Note You can assign project elements to a task or change such assignments. Alternatively, you can manage assignments between project elements and tasks using the Manage Multiple Project Plans app.For details, open [https://help.sap.com/docs/](https://help.sap.com/docs/) and see the Manage Tasks under Applications in Project Management section of the User Guide for Project Management for SAP Project and Resource Management. | The Issue Details screen is displayed. |  |

#### Establish References with Relevant Business Objects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can integrate SAP S/4HANA Cloud Public Edition and Project Management in SAP Project and Resource Management for certain business objects, via related objects capability. After configuring the integration, while creating a related object; on selecting the relevant SAP S/4HANA Cloud Public Edition system ID and object type, the External ID list is pre-populated with the associated business objects. The related object URL is also automatically generated by the system.

You can create a related object by specifying an External ID, Name, URL, Description, System ID, and Object Type in the Create Related Object dialog box. The System ID corresponds to the business system in which the related object exists. The URL link directs you to the object outside of the Project Management in SAP Project and Resource Management.

|  |
| --- |
| Note You can modify the Name, URL, Description, System ID, and Object Type of a related object. The uniqueness of a related object is determined by the combination of its External ID, URL, System ID, and Object Type. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Project Management in SAP Project and Resource Management as a Project Manager.Note Please verify that the Project Team Member role has required role collection assigned as mentioned in the Roles chapter under Prerequisites to execute this chapter and also please have the SAP Project and Resource Management application URL to access this app as Project Team Member |  |  |
| 2 | Access App | Open My Collaborative Projects (F3145) app. | The My Collaborative Projects screen is displayed. |  |
| 3 | Open the Project | From the My Collaborative Projects list displayed, choose the project. | The Project Details screen is displayed. |  |
| 4 | Navigate to Related Objects | Choose Related Objects section. | The Related Object screen is displayed. |  |
| 5 | Create Related Object | On the Project Details screen, choose Create. | The Create Related Object pop screen is displayed. |  |
| 6 | Make the entries | On the Create Related Object pop-up screen, make the following entries:System ID:<Example: S4H_XYZ>Object Type:Select the suitable Object type <Example: Project>External ID:Enter the External IDNote For SAP systems in which auto-creation of URLs are not supported, ensure that correct and verified URLs are entered while creating/modifying related objects connections. This helps to avoid any malicious activity.Name:suitable name for the projectURL:the correct URL of the object to be createdDescription:suitable description for the ObjectChoose Create. | Related object is created with the provided parameters. |  |
| 7 | Open the Related Object screen | Click on External Id hyperlink on the Related Object screen | Related Object Pop-up is displayed. |  |
| 8 | Navigate to Related Object in SAP S/4HANA Cloud Public Edition system | Click on Link to Object hyperlink on the Related Object pop-up screen | New session is opened for logging in. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| 1NT - Project Financial Control | A project must be created and planned project cost is captured |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 1NT - Project Financial Control | Release the project after the steering committee review. |

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
> Flagged while digesting this document, not verified: Business role for several steps differs between the Overview Table and the procedure: Identify & Capture Risks (table: Project Manager, procedure logs on as Project Team Member), Document Issues (table: Project Manager, procedure: Project Team Member), Monitor and Mitigate Risks (table: Project Team Member, but Purpose says the Project Manager monitors risks).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[14-maintenance-service-and-projects/internal-project-management-project-based-services-1a8-ae-test-script]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6JN_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 67,967 chars in the whole document
