---
id: 06-management-accounting/test-script-project-review-1yf-ae-sap-s-4hana-cloud-public-edition-787
title: "Test Script: Project Review (1YF_AE) - SAP S/4HANA Cloud Public Edition (1YF_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud test script for scope item 1YF Project Review: roles, apps and test steps for project setup, release workflow and milestone review."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/project-control-enterprise-projects]
aliases: [1YF_S4CLD2608_BPD_EN_AE]
keywords: ["Project Control for Finance, Capital, R&D and Sales Projects", project review, test script, project milestones, project setup, project release workflow, project status, steering committee review, business roles, team responsibility]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YF_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-787
topic: 06-management-accounting/project-control-enterprise-projects
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Project Review (1YF_AE) - SAP S/4HANA Cloud Public Edition (1YF_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YF_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Project Control for Finance, Capital, R&D and Sales Projects** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Project Review (1YF_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848555)

[2 Prerequisites 4](#_Toc232848556)

[2.1 System Access 4](#_Toc232848557)

[2.2 Roles 4](#_Toc232848558)

[2.3 Business Conditions 5](#_Toc232848559)

[2.4 Preliminary Steps 5](#_Toc232848560)

[2.4.1 Manage Teams and Responsibility for Projects (Optional) 5](#_Toc232848561)

[2.4.2 Configure Flexible Workflow for Project Release (Optional) 7](#_Toc232848562)

[3 Overview Table 9](#_Toc232848563)

[4 Test Procedures 10](#_Toc232848564)

[4.1 Project Setup 10](#_Toc232848565)

[4.1.1 Describe Project 10](#_Toc232848566)

[4.2 Review Workflow for the Release of a Project (Optional) 12](#_Toc232848567)

[4.2.1 Approve Project Release by Project Manager 12](#_Toc232848568)

[4.2.2 Approve Project Release by Project Steering Committee Member 13](#_Toc232848569)

[4.3 Project Milestone Review - Single Project Review (Optional) 14](#_Toc232848570)

[4.3.1 Monitor Upcoming Milestones 14](#_Toc232848571)

[4.3.2 Update Project Status 15](#_Toc232848572)

[4.3.3 Analyze Project 17](#_Toc232848573)

[4.3.3.1 Analyze Project via My Projects (Active Projects) 17](#_Toc232848574)

[4.3.3.2 Analyze Project via My Projects (Key Figures) 18](#_Toc232848575)

[4.3.4 Milestone Review 19](#_Toc232848576)

[4.3.5 Complete Milestone 20](#_Toc232848577)

[5 Appendix 22](#_Toc232848578)

[5.1 Process Integration 22](#_Toc232848579)

[5.1.1 Preceding Processes 22](#_Toc232848580)

[5.1.2 Succeeding Processes 22](#_Toc232848581)

## Purpose

Overview

This scope item helps you to determine the right projects to work on by keeping all project stakeholders (such as the steering committee) informed, enabling the review and approval of project milestones, and accelerating central project review or ranking meetings.

Using the project brief (a condensed, changeable, and integrated project plan with key information such as status, milestones, costs, and contacts), you can provide a low-level entry point and common discussion basis for decision makers. The Project Ranking provides a common, integrated frame to collect all required information and organize the process of central project review.

This scope item provides two examples:

Companies where project milestones are locally reviewed and approved when a milestone is upcoming (starting with the Monitor upcoming milestone process step).

Companies where projects and/or project milestones are reviewed and approved centrally during regular review meetings (starting with the Setup central review process step).

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
| SAP CP Intelligent Product Design (IPD) | Your system administrator provides you with the URL of the SAP CP Intelligent Product Design (IPD).For more Configurations Information on Intelligent Product Design, search for SAP S/4HANA Cloud Public Edition for Intelligent Product Design. Click Administration Guide for Collaboration under the Administration section on SAP Help Portal. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |
| Project Manager | SAP_BR_PROJECTMANAGER | Project Management | SAP_BR_PROJECTMANAGER |  |
| Project Steering Committee Member | SAP_BR_PROJECT_STEER_MEMBER | Project Steering Committee | SAP_BR_PROJECT_STEER_MEMBER |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1NT - Project Control – Finance | A project must be created and preliminary costing has been done on the project. |

### Preliminary Steps

#### Manage Teams and Responsibility for Projects (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you define teams which are responsible for handling multiple projects across organisations.

|  |
| --- |
| Note For details on the process of setting up teams and responsibility determination, see the Setting Up Responsibility Management (1NJ) guide. |

You can also define your own responsibility management (functions, teams, and responsibilities) by making use of the following SSCUIs:

- Map Function Profiles to Standard Team Category
- Classify Functions for Standard Team Category
- Map Custom Responsibility Definitions to Standard Team Category
- Define Team Types

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on on to the SAP Fiori launchpad as a Business Process Specialist |  |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412) .Choose Create. | The Team screen is displyed. |  |
| 3 | Maintain the Team details | Make the following entries and choose Create :In the General Information tab:Name: Team_EPPMDescription: Team of EPPMStatus:EnabledType: SEPPM_PFCIn the Team Members tab:Choose Create, and maintain the following values:Business Partner: use the search function to find the business partner of Project Financial ControllerFunctions: Project Financial Controller |  |  |
| 4 | Create the Team | Choose Create. | The team is created |  |

#### Configure Flexible Workflow for Project Release (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you configure your release conditions for project release approval.

|  |
| --- |
| Note Before you start this procedure, ensure that the project team has been created in your system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the App | Open Manage Workflows for Enterprise Project (F6158) app. | The Manage Workflows screen is displayed. |  |
| 3 | Create Workflow for Project Release | Choose Create. On the New Workflow screen, enter a workflow name in the Workflow Name field. For example, 'Test Workflow' for Project Release.Select the Properties tab. Enter a description in the Description field, for example, Test Workflow for Project Release. Maintain the following values:Valid From:Valid To:Select the Start Conditions tab. In the Only start the workflow if all of the following preconditions are met: field, select Responsible Cost Center from the dropdown list and enter the cost center. <For Example: 10101321>.Choose Create Alternative Preconditions and maintain the conditions and their corresponding data that is required.Select the Steps tab. Choose Create.On the New Step screen, select the Header tab. In the Step Type field, select Release of Enterprise Project from the dropdown list.Select the Recipients tab and maintain the following settings:Assignment By: RoleRole: Project Financial Controller / Project Manager / Steering Committee MemberOr Assignment By: TeamTeam: You can select/assign the team created in the previous step [Manage Teams and Responsibility for Projects (Optional)](#unique_6) [page ] 5Step to be completed by: One of the recipients / All of the recipientsSelect the Exception Handling tab and make the following entries:Required Action: Do nothingAction Result: Cancel Workflow / Continue / Repeat Step / Restart Workflow (select from the drop down list based on your requirement).Choose Create and Save | The workflow item is successfully created |  |
| 4 | Activate Workflow Item | On the Workflow Details screen, choose Activate. | The workflow item is activated. |  |

## Overview Table

This scope item consists of the process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Project Setup](#unique_9) [page ] 10 |  |  |  |
| [Describe Project](#unique_10) [page ] 10 | Project Manager | My Projects - Project Manager (F1876) |  |
| [Review Workflow for the Release of a Project (Optional)](#unique_11) [page ] 12 |  |  |  |
| [Approve Project Release by Project Manager](#unique_12) [page ] 12 | Project Manager | My Inbox - All Items (F0862) |  |
| [Approve Project Release by Project Steering Committee Member](#unique_13) [page ] 13 | Project Steering Committee Member | My Inbox - All Items (F0862) |  |
| [Project Milestone Review - Single Project Review (Optional)](#unique_14) [page ] 14 |  |  |  |
| [Monitor Upcoming Milestones](#unique_15) [page ] 14 | Project Manager | My Projects - Project Manager (F1876) |  |
| [Update Project Status](#unique_16) [page ] 15 | Project Manager | My Projects - Project Manager (F1876) |  |
| [Analyze Project via My Projects (Active Projects)](#unique_17) [page ] 17 | Project Steering Committee Member | My Projects - Steering Committee (F2945) |  |
| [Analyze Project via My Projects (Key Figures)](#unique_18) [page ] 18 | Project Steering Committee Member | My Projects - Key Figures (F3376) |  |
| [Milestone Review](#unique_19) [page ] 19 | Project Manager | My Projects - Project Manager (F1876) |  |
| [Complete Milestone](#unique_20) [page ] 20 | Project Manager | My Projects - Project Manager (F1876) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Project Setup

#### Describe Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager describes the project details, such as Milestones, for the first time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Project Manager. |  |  |
| 2 | Get Notification | You (Project Manager) get a notification from the Project Financial Controller that a project is created. | Notification is received. |  |
| 3 | Access My Projects (Active Projects) | Open My Projects - Project Manager (F1876) app. Choose Planned Projects to go to Project Briefs . | The Project Briefs screen appears. |  |
| 4 | Open the Project | From the Projects displayed, select the project and click to open the project | Selected project is displayed. |  |
| 5 | Open Project in Project Planning App | Choose the Related Apps Icon and from the drop down select Project Planing to navigate to the Project Planning page.Note By default project will open in display mode | The Project Planning screen is displayed. |  |
| 6 | Maintain Work packages | To update timeline for Work packages, choose Edit and click on the individual Work package to navigate to the Work package screen and change the timelines if required. |  |  |
| 7 | Maintain Priority and Project Type | Click on the first line item/ project in the Project Planning screen to navigate to the project screen.Select the priority and project type suitable for the project from the drop-down option list .Choose SaveChoose Back once to come back to the Project Planning screen |  |  |
| 8 | Define Milestones | Choose the Related Apps icon and from the drop-down menu, select Project Briefs to navigate to the Project page.Choose Edit to change the project from Display to Edit mode.From the Milestones tab, choose Create to add the list of relevant milestones | All the milestones are saved and displayed |  |
| 9 | Maintain the Planned Finish Dates for the Milestones | For each milestone, select the Planned Finish date. | Planned Finish dates for the milestone are maintained. |  |
| 10 | Create Collaboration | Scroll down to the Related Objects section and choose Create.In the Related Objects section, the Object Type and Object are automatically created.Note Depending on your system setup, the following object types are supported:Collaboration Project in SAP Project and Resource Management, Collaborative Project ManagementCollaboration in SAP Intelligent Product Design.The system automatically chooses the object type set up in your system. If both integration scenarios are active, Collaborative Project Management from SAP Project and Resource Management takes precedence. | A system message tells you that the collaboration will be created upon saving.The collaboration or collaboration project is created and a link to it is added in the Related Objects table of the project brief. |  |
| 11 | Define Team | Scroll down to the Responsibilities section and choose Create to maintain the names of steering committee team members, project financial controller and team members with relevant roles.Note The assigned team members will be able to find the WBS elements of Projects assigned in the search box of the Time Recording app and create tasks with those WBS elements and record their time according to the steps mentioned in 1Q4 (Time Recording)Choose Save. | Team member details are maintained |  |

### Review Workflow for the Release of a Project (Optional)

Purpose

In this activity, the Project Manager and Project Steering Committee member reviews workflow for the release of a project triggered by the project financial controller with the help of the My Inbox app, the Project Manager and, the Steering Committee member would provide their decision for project release.

|  |
| --- |
| Note This is an optional step, therefore, before executing this activity, configure the workflow as described in the [Configure Flexible Workflow for Project Release (Optional)](#unique_7) [page ] 7 under preliminary steps. |

#### Approve Project Release by Project Manager

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, as part of the two-step workflow process for project approval, the Project Manager provides his decision using the 'My Inbox' app.

Procedure

This procedure describes how to approve a project.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager. |  |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen with a list of already created projects that need to be approved is displayed. |  |
| 3 | Select Project Workflow Item | To search for a specific project, enter the required search criteria.From the search result list, select a project. | The project workflow item is displayed. |  |
| 4 | Approve the Project | Choose Approved.If required, enter the approval reason in the Decision Note. Choose Submit. |  |  |

#### Approve Project Release by Project Steering Committee Member

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, as part of the two-step workflow process for project approval, the Project Steering Committee Member provides his decision on top of project managers decision using the My Inbox app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Steering Committee Member. |  |  |
| 2 | Access App | Open the My Inbox - All Items (F0862) app. | The My Inbox screen with a list of already created projects that need to be approved is displayed. |  |
| 3 | Select Project Workflow Item | To search for a specific project, enter the required search criteria.From the search result list, select a project. | The project workflow item is displayed. |  |
| 4 | Approve the Project | Choose Approved.If required, enter the approval reason in the Decision note. Choose Submit. |  |  |

### Project Milestone Review - Single Project Review (Optional)

Purpose

In this activity, the Project Manager organizes a local review of an upcoming milestone for one of his/her projects. With the help of the Project Brief app, Project Manager brings all involved people and steering committee members on the same page for the milestone review. To prepare themselves for the upcoming review, Steering committee members cannot only analyze the project to be reviewed, but also its impact on the whole project landscape.

#### Monitor Upcoming Milestones

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager organizes a local review for the approval of this single upcoming milestone shown in the Overiew page through the Upcoming milestones card and prepares himself/herself for the upcoming steering committee review meeting.

The following Business Process must be executed before this step:

1NT Project Control – Finance

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager. |  |  |
| 2 | Access App | Open My Projects - Project Manager (F1876) app. Go to My Projects- Upcoming milestones using the card Upcoming Milestones . | The My Projects - Upcoming Milestones screen appears. |  |
| 3 | Open the Project | From the Projects list displayed, select the project and click to open the project | The Project Briefs screen is displayed. |  |
| 4 | Analyze the Upcoming Project Milestones | Scroll down to the Milestones section and analyze the milestones in detail. | He/She analyzes the upcoming milestone |  |

#### Update Project Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager reviews and updates the project status, costs, timelines and project milestones and prepares himself/herself for upcoming project steering committee meeting,

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager. |  |  |
| 2 | Access App | Open My Projects - Project Manager (F1876) app. Go to Project Briefs Overview page using the card Overall Status - Active Projects . | The Project Manager is able to see the overall status of the project . |  |
| 3 | Select the Project. | Select the project from the list and click to open. | Selected project is open for review. |  |
| 4 | Review the Cost of the Project | Scroll down to the Cost section to view the Cost overview.Note You will be able to see the cost, once the plan and actual costs are updated using 1NT - Project Control – Finance scope item. | Cost overview graph is displayed and cost can be reviewed. |  |
| 5 | Analyze Costs in Detail | Select an Item from the Costs section and choose Details in the Cost Overview section, to analyze the costs in detail. | Costs in detail are displayed. |  |
| 6 | Choose Edit | Choose Edit to change the project from Display to Edit mode.Note By default the project will open in display mode. | Selected project is open in editable mode. |  |
| 7 | Update the Forecast Finish dates | Update the Forecast Finish dates for milestones. | The Forecast Finish dates for milestones are updated. |  |
| 8 | Update the Project Status | Scroll up to the Status section to view the Status overviewUpdate the Status to display the traffic lights for the project | Project Status is updated. |  |
| 9 | Update the Trend for the Project | Update the Trend under the Status section to display the traffic lights for the project | Project Trend is updated. |  |
| 10 | Update the Comments | Add comments in the status section for relevant status areas | Comments are added in the Status section |  |
| 11 | Upload Documents Required for the Project | Scroll down to the Attachments section and choose + to upload relevant documents from your local drive. | Documents are uploaded successfully |  |
| 12 | Set the next Milestone for Review | Scroll up to the Milestones section and only for the next milestone, set the Milestone Approval Status to For Approval.Choose Save. | Milestone Approval Status is added in the Milestone section. |  |

#### Analyze Project

##### Analyze Project via My Projects (Active Projects)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, project steering committee members get the information on project statuses either from the Project manager or the Project Financial Controller. They prepare themselves for an upcoming review meeting in order to be able to ask the right questions and make informed decisions during the upcoming review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Steering Committee Member |  |  |
| 2 | Get Overview | The Project Steering Committee member gets information from Project Managers that project is prepared for upcoming review meeting |  |  |
| 3 | Access App | Open My Projects - Steering Committee (F2945) app.In the Standard section, enter the project ID and choose Go. Using the card Overall Status - Active Projects, you will see the list of active projects, click on the project to review in detail. | The My Project - Steering Committee screen appears with the different cards. |  |
| 4 | Review the Projects to be Presented | Navigate to different sections on the Project Brief screen to review cost and statuses of the selected project. | Details of the project are displayed. |  |
| 5 | Monitor Project Progress | Select the project to be reviewed and the related projects and choose Project Progress to go to the Monitor Project Progress screen and review the project timelines. | Graphical representation of the project timeline is displayed. |  |
| 6 | Review Projects with Critical Status in Detail | Choose Back and choose the Detailed Status card to go to My Projects- Detailed Status screen and review project statuses. | Details of the selected project are displayed in detail. |  |
| 7 | Review Project Costs | Choose Back and then choose the Cost to Date - Active Projects card to go to Project Briefs screen and review project costs.Select the project from the list displayed and scroll down to the Cost Section to view the Cost Overview and choose Details to analyze the project cost in detail.Note You will be able to see the cost once the Plan and Actual costs are updated using the 1NT - Project Control – Finance scope item. | Details of the project costs are displayed. |  |

##### Analyze Project via My Projects (Key Figures)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the project steering committee members get the information on project statuses either from the Project manager or the Project Financial Controller. They prepare themselves for an upcoming review meeting in order to be able to ask the right questions and make informed decisions during the upcoming review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Steering Committee Member |  |  |
| 2 | Get Overview | Project Steering Committee member gets information from Project Managers that projects are prepared for upcoming review meeting |  |  |
| 3 | Access App | Open My Projects - Key Figures (F3376) app . | The Projects by Key Figures screen appears. |  |
| 4 | Review the Projects Based on Project Type | In the Project Type value help box, select the required project type. | The projects of the selected project type are displayed, including details such as Plan Costs (in the form of a bubble chart) and project status |  |
| 5 | Review the Projects based on Priority | In the Priority value help box, select the desired priority. | The projects of the selected priority are displayed, including details such as Plan Costs (in the form of a bubble chart) and project status. |  |
| 6 | Review Projects with Critical Status in Detail | Click on the project to go to the Project Brief screen to review project status | Details of the selected project will be displayed in detail. |  |
| 7 | Review Project Costs | The Aggregated and Non Aggregated Costs of the selected project are displayed.In the project cost report, you can view the Assigned Value (Commitment +Actual) and Available budget (Budget-Assigned Value), based on which you can analyze the projectNote You will be able to see the cost once the Plan and Actual costs are updated using the 1NT - Project Control – Finance scope item. | Details of the project costs will be displayed.Note In the Standard section, the information is shown in the Compact Filter view by default. You can also change it to the Visual Filter view to get easy understanding of overall costs of the project. This visual depiction helps the stakeholders to get an overview of the project. |  |

#### Milestone Review

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager does a review of a milestone together with the Steering Committee. He/she demonstrates his/her project to the Steering Committee and updates the project according to discussions in the review meeting

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager. |  |  |
| 2 | Access App | Open My Projects - Project Manager (F1876) app. Go to My Projects - Upcoming Milestones using the card Upcoming Milestone | The Project Overview screen appears with the list of Planned projects. |  |
| 3 | Select the Project to be Presented | Select the project and click to navigate to the Project Brief screenChoose the Edit icon to open the project in edit mode. | Details of the selected project are displayed. |  |
| 4 | Display the Cost, Timeline and Present Status of the Project | Navigate to a different section on the Project Overview screen to view Cost, Status, Milestone and Project timelines. | Project overview and status is showcased to the stakeholders. |  |
| 5 | Update Project based on Feedback | Scroll down to the Status section and update the status and trend of the project based on the feedback received from the review meeting. |  |  |

#### Complete Milestone

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager changes the status of the milestone to be approved based on the feedback received from the Project Steering Committee during the review meeting and sets the actual dates for the approved milestones.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager. |  |  |
| 2 | Access App | Open My Projects - Project Manager (F1876) app.Go to Project Brief Overview using the card Upcoming Milestones - Active Projects. | The Project Overview screen appears and the list of projects is displayed |  |
| 3 | Select Project in which Milestones are to be Approved | Select the project and click to navigate to the Project Brief screen | Details of the selected project are displayed.Selected project is open and can be updated. |  |
| 4 | Choose Edit | Choose Edit to change the project from Display to Edit mode.Note By default, the project will open in display mode. | Selected project is open in editable mode. |  |
| 5 | Set Milestones Status to Approved | Set Milestone Approval Status to Approved | Milestone Approval Status is added in the Milestone section |  |
| 6 | Update the Actual Finish Date | Update the Actual Finish date for the approved Milestones.Note Actual Date can be updated only for the released projects. For releasing a project, refer to scope item 1NT-Project Control – FinanceChoose Save | The Actual Finish date is updated. |  |

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

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/period-end-closing-projects-bna-ae-test-script-sap-s-4hana-cloud-publi]]
- related-to :: [[06-management-accounting/test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud]]
- related-to :: [[06-management-accounting/test-script-project-control-finance-1nt-ae-sap-s-4hana-cloud-public-ed]]
- related-to :: [[06-management-accounting/test-script-project-control-research-and-development-projects-35e-ae-9]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1YF_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 37,094 chars in the whole document
