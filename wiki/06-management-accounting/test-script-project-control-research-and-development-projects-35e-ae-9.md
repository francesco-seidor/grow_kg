---
id: 06-management-accounting/test-script-project-control-research-and-development-projects-35e-ae-9
title: "Test Script: Project Control – Research and Development Projects (35E_AE) (35E_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 35E (AE): create, budget, release, monitor, close R&D projects, with prerequisites and Fiori app steps."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/project-control-enterprise-projects]
aliases: [35E_S4CLD2608_BPD_EN_AE]
keywords: ["Project Control for Finance, Capital, R&D and Sales Projects", research and development projects, project control, project creation, project budget, planned costs, budget availability control, project monitoring, project coding mask, cost rates]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/35E_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-918
topic: 06-management-accounting/project-control-enterprise-projects
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Project Control – Research and Development Projects (35E_AE) (35E_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/35E_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Project Control for Finance, Capital, R&D and Sales Projects** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Project Control – Research and Development Projects (35E_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851984)

[2 Prerequisites 4](#_Toc232851985)

[2.1 System Access 4](#_Toc232851986)

[2.2 Roles 4](#_Toc232851987)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232851988)

[2.4 Business Conditions 7](#_Toc232851989)

[2.5 Preliminary Steps 7](#_Toc232851990)

[2.5.1 Setting Up Custom Fields for Project (Optional) 7](#_Toc232851991)

[2.5.2 Maintain Cost Rates 8](#_Toc232851992)

[2.5.3 Maintain Financial Statement Versions 9](#_Toc232851993)

[2.5.4 Create Project Coding Mask 9](#_Toc232851994)

[2.5.5 Create Project Types for WBS Elements (Optional) 12](#_Toc232851995)

[2.5.6 Maintain Budget Availability Profile using Self Service Configuration (SSC) UI app (Optional) 14](#_Toc232851996)

[2.5.7 Manage Situation Types (Optional) 18](#_Toc232851997)

[2.5.8 Manage Teams and Responsibilities for Projects (Optional) 20](#_Toc232851998)

[3 Overview Table 21](#_Toc232851999)

[4 Test Procedures 23](#_Toc232852000)

[4.1 Create R&D Project 23](#_Toc232852001)

[4.2 Describe Project (Optional) 27](#_Toc232852002)

[4.3 Upload Planned Costs 28](#_Toc232852003)

[4.4 Assign Project Budget 29](#_Toc232852004)

[4.5 Define Demand 31](#_Toc232852005)

[4.6 Release Project 32](#_Toc232852006)

[4.7 Time Recording 33](#_Toc232852007)

[4.8 Project Demand 33](#_Toc232852008)

[4.9 Project Control - Procurement 34](#_Toc232852009)

[4.10 Post General Journal Entries 34](#_Toc232852010)

[4.11 Monitor Projects 36](#_Toc232852011)

[4.11.1 Monitor Notification (Optional) 36](#_Toc232852012)

[4.11.2 Monitor Projects via Project Financial Controller Overview 37](#_Toc232852013)

[4.11.3 Monitor Projects via Monitor Projects App 38](#_Toc232852014)

[4.11.4 Monitor Projects via Project Cost Report 39](#_Toc232852015)

[4.11.5 Monitor Projects via Project Budget Report 40](#_Toc232852016)

[4.11.6 Monitor Projects via Manage Project Procurement 41](#_Toc232852017)

[4.11.7 Monitor Projects via P&L Plan/Actual 42](#_Toc232852018)

[4.12 Period-End Closing Projects 43](#_Toc232852019)

[4.13 Close Project 44](#_Toc232852020)

[5 Appendix 46](#_Toc232852021)

[5.1 Process Integration 46](#_Toc232852022)

[5.1.1 Preceding Processes 46](#_Toc232852023)

[5.1.2 Succeeding Processes 46](#_Toc232852024)

## Purpose

Overview

This scenario describes a project where the research and development activities related to the design of a new product are managed. Therefore, it supports the product development process by managing the related project costs, milestones, budgets, and approvals. After releasing all or part of the project, the project is executed and project-related purchasing can be performed. Through the integration with SAP Intelligent Product Design, you can leverage advanced collaboration scenarios for project execution. Period-end closing activities such as overhead application or settlement can then be executed.

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
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Analytics Specialist | SAP_BR_ANALYTICS_SPECIALIST | Analytics / Analytics | SAP_CA_SPT_ANALYTICS_PC / SAP_CORE_SPT_ANALYTICS_PC |  |
| Project Steering Committee Member | SAP_BR_PROJECT_STEER_MEMBER | Project Steering Committee | SAP_BR_PROJECT_STEER_MEMBER |  |
| Project Manager | SAP_BR_PROJECTMANAGER | Project Management | SAP_BR_PROJECTMANAGER |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Controlling Area | A000 | Controlling Area A000 |  |
| Company Code | 3310 | Company Code 3310 |  |
| Plant | 3310 | Plant 1 AE |  |
| Cost Center | 331015013310160133101321 | R&D Cost centerMarketing Cost CenterServices/Consltg |  |
| Activity Types | 811 | ConsultingPersonal Hours |  |
| Cost Rate | Actual and planned cost rates are maintained for the following combination of cost centers or activity types:Cost centers: 33101501, 33101101Activity types: 11 |  | Cost Rates are defined time-dependent |
| G/L Account | 61007000 | Trav. Expense – Airfare, Rail, Mileage |  |
| 61003000 | Travel Expenses – Hotel and Accommodation |  |  |
| 61008000 | Travel Expenses – Miscellaneous |  |  |
| 10010000 | Petty Cash |  |  |
| 50309500 | COGS - Licenses |  |  |
| 65008300 | Services – Genera |  |  |
| 50305000 | COGS Machine Time |  |  |
| 51100000 | Consumption – Raw Material |  |  |
| 50304000 | Personnel Time |  |  |
| Profit Center | YB600YB110 | Shared ServicesProduct A |  |
| Functional Area | YB75 | Research & Development |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS):

| MDS | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| 3KW | Create CO Cost Rates - MDS |
| BNH | Create Profit Center - MDS |
| BHD | Create Purchasing Info Record - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1YF - Project Review | To execute the project review and project collaboration functionalities, the project review Project Review (1YF) scope item must be activated. |
| 4RF - Project Control – Resourcing and Procurement | To execute demand planning for the project, the 4RF - Project Control – Resourcing and Procurement scope item must be activated |

### Preliminary Steps

#### Setting Up Custom Fields for Project (Optional)

Purpose

In this step, you can maintain custom fields in the project header section.

Procedure

To execute this activity, carry out the relevant steps from the Key User Extensibility topic in the Extend and Integrate Your SAP S/4HANA Cloud Public Edition guide to create and maintain custom fields that can be used to enhance applications.

The Business Context to be used is Project Header and Project Element.

#### Maintain Cost Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can maintain, check and update the actual cost rates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as a Cost Accountant - Overhead |  |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Rates - Services (F3161) | The Manage Cost Rates - Services screen is displayed. |  |
| 3 | Check Actual Cost Rates | Make the following entries and choose Go.Company Code: 3310Valid On: TodayCost Center: 33101321 and 33101101Activity Type: 8Currency: AEDCheck if there is a valid cost rate for given cost center, activity type, and period. | The actual cost rates for given cost centre, activity type and period are checked for valid values.Note You can skip the next step if there is a valid cost rate for given cost center, activity type, and period. |  |
| 4 | Maintain Additional Actual Cost Rates | Choose Add and make the following entries:Company Code: 3310Cost Center: 33101321Activity Type: 8WBS Element: <this is an optional entry>From Fiscal Year: Current YearFrom Period: Current PeriodRate: 100Currency: AEDPer:1Activity Unit: HChoose Save. | The pop-up screen Create Cost Rates-Company Code 3310 appears.Additional cost rates are created. |  |
| 4 | Maintain Additional Actual Cost Rates | Choose Add and make the following entries:Company Code: 3310Cost Center: 33101101Activity Type: 8WBS Element: <this is an optional entry>From Fiscal Year: Current YearFrom Period: Current PeriodRate: 100Currency: AEDPer:1Activity Unit: HChoose Save. | The pop-up screen Create Cost Rates-Company Code 3310 appears.Additional cost rates are created. |  |

#### Maintain Financial Statement Versions

Procedure

To execute this activity, run the preliminary step Maintain Financial Statement Versions from the Period-End Closing – Projects (BNA) test script.

#### Create Project Coding Mask

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note If you are planning to use project coding mask for your projects, remember the following:You need to define the coding key before you create the project and determine exactly what your coding mask should be.Coding mask cannot be created if project with same key already exists.Coding mask once created can be deleted, if a project with the same key does not exist.With Define Project Coding Mask, you will be able to define the Coding Keys which determine the naming/nomenclature of the projects created in the scope items, namely, 1NT- Project Control – Finance, 35E- Project Control – Research and Development Projects and 35F- Project Control – Capital Projects. The usage of Project Coding Mask is not supported for the scope items such as J11- Customer Project Management – Project-Based Services and 1A8- Internal Project Management – Project-Based Services. |

Purpose

The Define Project Coding Mask app is used to create the coding mask for the project structure. The coding mask applies to the external identification of project definitions as well as WBS elements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as aConfiguration Expert - Business Process Configuration |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Navigate to Project Coding Mask SSCUI | Choose the link Configure Your Solution.Make the following entries:Application Area: Enterprise Portfolio & Project ManagementSub Application Area: Project Financials ControlClick on the line item displayed in the Configuration Items sectionSelect Define Project Coding Mask and choose Configure | The Change View "Project Number Editing'': Overview screen is displayed. |  |
| 4 | Create a Coding Mask Entry | Perform the following actions to create the coding mask:Choose New EntriesEnter the following details:PrjID: ACoding mask: /XXXXXX-00Description: Test Coding Mask for Key ALck: <Select/Deselect>Choose Save.NoteThis step is optional.Once the coding mask is created, deletion is not possible.You cannot create commercial or internal projects in the project services processes, namely:Customer Project Management (J11)Internal Project Management (1A8)that begins with any coding key defined for coding masks. | Project Coding Mask will be saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Navigate to Project Coding Mask SSCUI | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Project Coding Mask.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Project Number Editing": Overview screen is displayed. |  |
| 3 | Create a Coding Mask Entry | Perform the following actions to create the coding mask:Choose New EntriesEnter the following details:PrjID: ACoding mask: /XXXXXX-00Description: Test Coding Mask for Key ALck: <Select/Deselect>Choose Save.NoteThis step is optional.Once the coding mask is created, deletion is not possible.You cannot create commercial or internal projects in the project services processes, namely:Customer Project Management (J11)Internal Project Management (1A8)that begins with any coding key defined for coding masks. | Project Coding Mask will be saved. |  |

#### Create Project Types for WBS Elements (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note This is an optional step. Before creating a Project Type, you must consider the following guidelines.The Project Type key is unique. Determine exactly what your Project Type key should be as you cannot edit/delete project type key once created.Project Type does not influence program control or screen selection, instead, it is used as a filtering criteria for projects. |

Purpose

Project Type is generally used to group or classify projects, it is primarily used for the reporting. The Create Project Types for WBS Elements app is used to create the project type.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Navigate to Create Project Types for WBS Elements SSCUI | Choose the link Configure your solution.Make the following entriesApplication Area: Enterprise Portfolio & Project ManagementSub Application Area: Project Financials ControlClick on the line item displayed in the worklist sectionSelect Create Project Types for WBS Elements and choose Configure | The Create Project Types for WBS Elements app is displayed. |  |
| 4 | Create a Project Type | Perform the following actions to create the project type:Choose New EntriesEnter the details as mentioned in the following example :Example Typ: RDDescription: RD ProjectsChoose Save. | Project Type is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Create Project Types for WBS Elements SSCUI | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Create Project Types for WBS Elements.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Create a Project Type | Perform the following actions to create the project type:Choose New EntriesEnter the details as mentioned in the following example :Example Typ: RDDescription: RD ProjectsChoose Save. | Project Type is saved. |  |

#### Maintain Budget Availability Profile using Self Service Configuration (SSC) UI app (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note This is an optional step. Before creating a Budget Availability Profile, you must consider the following guidelines.There are various restrictions when you try to change the budget availability control settings. If commitments or actual costs are already posted, you can no longer activate the checks. |

Purpose

The Maintain Budget Availability Profile app is used to create the Budget Availability control profile.

Prerequisites

If you intend to use Project Budget, make sure that you activate the non-standard scope item Predictive Commitments Management (2I3) which is a prerequisite for budgeting. Once activated, commitment management ledger 0E is active and applicable for all company codes and countries/regions. These commitments are updated in Extension Ledger 0E (predelivered) in ACDOCA table. Commitments are reduced by various business transactions such as goods receipt. The default content for Project Budgeting utilizes profiles PS001 and you can either update this profile or create your own profile via SSCUI Maintain Budget Availability Control Profile for Projects.

Ensure that you perform the Preliminary Steps of this document to update the following:

- Maintain Financial statement YPS2
- Tag ACT_COST which is mandatory for G/Ls relevant for Budget check. Note that currently Commitment/Budget do not work for Purchase order without material.
- Maintain Financial Statement Visions (FSV)
- Assign Semantic Tags for FSV
- Set Report Relevancy
- Replicate Runtime Hierarchy. Make sure G/Ls relevant for Budget are part of this structure.

To view commitments in the report, an open purchase order and/or requisition must exist. For details on creating purchase orders, refer to Consumable Purchasing (BNX).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Navigate to Maintain Budget Availability Control Profile for Projects | Choose the link Configure your solution.Make the following entries:Application Area: FinanceSub Application Area: Overhead Cost ManagementClick on the line item with Item Name Budget Management from the worklist section.Select Maintain Budget Availability Control Profile for Projects and choose Configure | The Maintain Budget Availability Profile app is displayed. |  |
| 4 | Create an Availability Control Profile Entry | Perform the following actions to create the availability control profile:Choose New EntriesEnter the details similar to the following example:Example Profile: ZS001Availy Ctrl Type: Project SystemBudget Availy Ctrl: Profile Name : Default Bdgt Availability prflTime Range: Annual Budget / Overall BudgetBudget Currency: Global Currency/Project CurrencyPress Enter.NoteOverall Budget needs to be selected if you want to perform the budget check across Fiscal years whereas Annual Budget needs to be selected if you want to perform the check per Fiscal year.Gobal Currency needs to be selected if you want to calculate the financials at controlling area level whereas Project Currency needs to be selected if you want to check financials at project level.For this newly created Availability Control Profile, maintain the Semantic Tags and Tolerance Limits.Select the AVC profile and choose Semantic Tags and maintain entries as shown in the following example:Choose New EntriesExample Sem. Tag: ACT_COSTSemantic Tag Name: Actual Cost% of Budget used Before First Notification: 80%% Increment for Further Notifications: 5%Press Enter.Select the Semantic tag and choose Tolerance Limits and maintain entries as shown in the following example:Choose New EntriesExample Acty Grp: All Activity GroupsMsgType: Warning/Error%: 90.00Press Enter.Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Navigate to Maintain Budget Availability Profile SSCUI | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Budget Availability Profile using Self Service.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Budget Availability Profile screen is displayed. |  |
| 3 | Create an Availability Control Profile Entry | Perform the following actions to create the availability control profile:Choose New EntriesEnter the details similar to the following example:Example Profile: ZS001Availy Ctrl Type: Project SystemBudget Availy Ctrl: Profile Name : Default Bdgt Availability prflTime Range: Annual Budget / Overall BudgetBudget Currency: Global Currency/Project CurrencyPress Enter.NoteOverall Budget needs to be selected if you want to perform the budget check across Fiscal years whereas Annual Budget needs to be selected if you want to perform the check per Fiscal year.Gobal Currency needs to be selected if you want to calculate the financials at controlling area level whereas Project Currency needs to be selected if you want to check financials at project level.For this newly created Availability Control Profile, maintain the Semantic Tags and Tolerance Limits.Select the AVC profile and choose Semantic Tags and maintain entries as shown in the following example:Choose New EntriesExample Sem. Tag: ACT_COSTSemantic Tag Name: Actual Cost% of Budget used Before First Notification: 80%% Increment for Further Notifications: 5%Press Enter.Select the Semantic tag and choose Tolerance Limits and maintain entries as shown in the following example:Choose New EntriesExample Acty Grp: All Activity GroupsMsgType: Warning/Error%: 90.00Press .Choose Save. |  |  |

#### Manage Situation Types (Optional)

Purpose

To monitor budget threshold for the project, you need to configure the situation type. In this procedure, you configure the situation type by using template.

|  |
| --- |
| Note For details on situations and the process to set up situation types, see the Setting Up Situation Handling (31N) guide. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Business Process Specialist |  |  |
| 2 | Open Manage Situation Types | Open Manage Situation Types (F2947) app. | The Manage Situation Types screen is displayed. |  |
| 3 | Select the Template to Copy | In the Situation Templates section, enter the ID EPPM_PROJBUDGETTHRESHOLDEXCEEDED and choose Go.Select EPPM_PROJBUDGETTHRESHOLDEXCEEDED, then choose Copy. | The Situation Type screen is displayed. |  |
| 4 | Maintain the Situation | Make the following entries and choose Save:Admin InformationID: <ID Name>Name: <ID Description>Example ID: Z_BUDGET THRESHOLDName: Budget Consumption SituationSituation DisplayShort Description:Details:Notification:Resend Notifications: YESConditionsMaintain the values against the corresponding attributes/ filters to configure the conditions and use this function.RecipientsResponsibility by teams: Choose Create and maintain the team created through the 'Manage Teams and Responsibilities' app and maintain the value Project Financial Controller in the field Member Functions if you intend to send notifications triggered by the situation Management to the Project Financial Controller, who is part of central project management team responsible for multiple projects.Responsibility Rules: Choose and select "Get the Project Responsible users (Project Financial Controller and Project Manager)" shown in the Rule list if you intend to trigger notifications to the project specific team defined in the project brief application. | The situation type is maintained |  |
| 5 | Enable The Situation Type | Choose Enable, it will change from NO to YES. |  |  |

#### Manage Teams and Responsibilities for Projects (Optional)

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
| 1 | Log on | Log on on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412) .Choose Create. | The Team screen is displyed. |  |
| 3 | Maintain the Team details | Make the following entries and choose Save:In the General Information tab:Name: Team_EPPMDescription: Team of EPPMStatus:EnabledType:SEPPM_PFCIn the Team Members tab:Choose + Add, and maintain the following values:Business Partner: use the search function to find the business partner of Project Financial ControllerFunctions: Project Financial Controller |  |  |
| 4 | Create the team | Choose Create. | The team is created |  |

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create R&D Project](#unique_17) [page ] 23 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project definition and WBS Elements with all the required parameters will be created. |
| [Describe Project (Optional)](#unique_18) [page ] 27 | See the scope item 1YF- Project Review | See the scope item 1YF- Project Review | See the scope item 1YF- Project Review |
| [Upload Planned Costs](#unique_19) [page ] 28 | Project Financial Controller | Import Financial Plan Data (F1711) | Planned costs for the project WBS Element would be posted |
| [Assign Project Budget](#unique_20) [page ] 29 | Project Financial Controller | Import Financial Plan Data (F1711) | Budget for the project WBS Element will be posted |
| [Define Demand](#unique_21) [page ] 31 | See the scope item 4RF- Project Control – Resourcing and Procurement | See the scope item 4RF- Project Control – Resourcing and Procurement | See the scope item 4RF- Project Control – Resourcing and Procurement |
| [Release Project](#unique_22) [page ] 32 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project status should be changed to REL (Release) |
| [Time Recording](#unique_23) [page ] 33 | See the scope item 1Q4- Time Recording | See the scope item 1Q4- Time Recording | See the scope item 1Q4- Time Recording |
| [Project Demand](#unique_24) [page ] 33 | See the scope item 4RF- Project Control – Resourcing and Procurement | See the scope item 4RF- Project Control – Resourcing and Procurement | See the scope item 4RF- Project Control – Resourcing and Procurement |
| [Project Control - Procurement](#unique_25) [page ] 34 | See the scope item 4RF- Project Control – Resourcing and Procurement | See the scope item 4RF- Project Control – Resourcing and Procurement | See the scope item 4RF- Project Control – Resourcing and Procurement |
| [Post General Journal Entries](#unique_26) [page ] 34 | General Ledger Accountant | Post General Journal Entries (F0718) | Post actual primary costs to WBS elements |
| [Monitor Projects](#unique_27) [page ] 36 | Project Financial Controller | Project Financial Controller Overview or Project Budget Report or Monitor Projects or P&L Plan/Actual or Project Cost Report Plan/Actual. | Compare Project actual vs planned and track project procurments |
| [Period-End Closing Projects](#unique_28) [page ] 43 | See the scope item BNA - Period-End Closing – Projects | See the scope item BNA - Period-End Closing – Projects | See the scope item BNA - Period-End Closing – Projects |
| [Close Project](#unique_29) [page ] 44 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project Status should be chan-ged to CLSD (Closed) |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create R&D Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create an R&D project with project definition using the Project Control fiori app.

For hierarchical project accounting requirements, you can also create a hierarchical project structure by calling up the Project Planning application from the Project Control app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215) . | The Project Control - List screen is displayed. |  |
| 3 | Create Project: Definition | Choose Create.Make the following entries in the Header tab:Project Name: e-BikeProject ID: RnD_000XX (For Example: RnD_00001)Project Profile: Overhead ProjectPlanned Start: TodayPlanned Finish : Today + 3 monthsMake the following entries in the General Information tab:Responsible Cost Centre: 33101501(R&D Cost Center)Profit Center: YB110 (Product A)Project Currency: AED (Automatically filled based on the cost center)Note You can specify the currency at project level different from controlling area currency, to run project specific financial reports.Project Manager:the Project Manager IDIn the Attachments tab, do the following:Choose Upload to upload project relevant documents from your local drive.Choose Create.A message tells you that the object is saved.When the project definition is created, Project Summary Task WBS Element will be created. | Project is created with the provided definition parameters.One WBS Element with the following details is created under the project :WBS Element ID: RnD_000XXProject Name: Overhead Project | Create budget for the new WBS element (and fund being used) |
| 4 | Add Values to the Project Summary Task WBS Element. | Once the project is created (RnD_000XX), choose Edit from the header section.Make the following entries in the General Information tab:Plant: 3310Functional Area :YB75 (Other expenses)Make the following entries in the Control tab:Costing Sheet: 3310PIThe following are optional entries, maintain them according to your requirements.Budget Availability Control Profile: Select the Budget Availability Profile created using SSCUI as mentioned in Preliminary Step ([Maintain Budget Availability Profile using Self Service Configuration (SSC) UI app (Optional)](#unique_13) [page ] 14)Example ZS001Note If project currency is maintained, you can assign a budget availability control profile where the budget currency is maintained as Global Currency or Project CurrencyIf project currency is not maintained, you can only assign a budget availability control profile where the budget currency is maintained as Global Currency.Budget Availability Control Profile is active: CheckedNoteYou can define your own budget availability profile using an SSCUI.As soon as you have planned budget for your project and activated the budget availability control, the hierarchy changes are no longer possible.Note You will be able to see Joint Venture (JV) attributes under the section Joint Venture Accounting during project creation, if the Joint Venture accounting functionality has been activated in the system. For the detailed explanation on JV attributes, you can refer to the scope item 3F7-Joint Venture Accounting .Block FunctionsTime Recording: <Selected/Not Selected>Activity Allocation: <Selected/Not Selected>Purchasing: <Selected/Not Selected>Concur Expense Posting: <Selected/Not Selected>Other Expense Posting: <Selected/Not Selected>NoteYou can also block certain functions based on the business requirement for the project being created.The Block functions need to be set at the individual WBS Element level to enable the functionality.Setting up the block functions at Project Header level will not impact the complete project hierarchy.Choose SaveA message tells you that the project is saved. | WBS Element is updated with all the provided parameters.Note In case you have entered a budget availability control profile and activated the budget availability control, all postings resulting into commitments or actual costs will be checked against the available budget of the WBS element used as account assignment object.In case the WBS element itself does not have any budget, the next higher level budget carrying WBS element will be used for the budget availability check.Depending on the tolerance limits defined for the availability control profile, the system can raise warning or error messages.Depending on the Time Range defined for the availability control profile, you will be able to check the budget consumption for a particular fiscal year or across fiscal years.This setting is valid for all kind of expense postings and expected expense postings (for example, purchase requisition or purchase orders) to a WBS element.Warning messages from budget availability check are not shown in case of automatic periodic postings and certain goods movement. |  |
| 5 | Navigate to Project Planning | Once the project is created (RnD_000XX), choose Related Apps from the header section. A pop-up screen appearsFrom the pop-up screen, select Project Planning to go to the Project Planning app.Note By default, the project will be in displayed mode, to edit the project, choose Edit | You will navigate to Project Planning app and will be able to make further entries. |  |
| 6 | Create WBS Elements under Project Summary Task WBS Element. | In the Project Structure view, select WBS Element (RnD_000XX) created in the above step, and choose Create .ID: RnD_000XX_01Name: WBS for Concept PhaseProfit Center: <This data is pre-populated from the first WBS level>Resp. Cost Cntr: 33101501 (This data is pre-populated from first WBS level)Planned Start: TodayPlanned Finish: Today + 3 monthsIn the Project Structure view, select WBS Element (RnD_000XX) created in the above step, and choose CreateID: RnD_000XX_02Name: WBS for Design PhaseProfit Center: <This data is pre-populated from the first WBS level>Resp. Cost Cntr: 33101501 (This data is pre-populated from first WBS level)Planned Start: TodayPlanned Finish: Today + 3 monthsIn the Project Structure view, select WBS Element (RnD_000XX) created in the above step, and choose Create Work Package.ID: RnD_000XX_03Name: WBS for Prototype PhaseProfit Center: <This data is pre-populated from the first WBS level>Resp. Cost Cntr: 33101501 (This data is pre-populated from first WBS level)Planned Start: TodayPlanned Finish: Today + 3 monthsNote Create WBS Element structure based on your requirementsYou can also create WBS Element by making use of the Copy functionality available in the Project Planing Application.You can also include WBS Element of another project by making use of the Include functionality available in the project planning application (While Including the WBS Elements, the existing demands and settlement rules of the source WBS Element are not included). | Project with WBS Element structure is updated with the provided parameters. |  |
| 7 | Save Project Structure | Choose Save. | Project with WBS Element structure is saved |  |

### Describe Project (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager describes the project details such as Milestones, Status and adds the Project team for the first time.

Procedure

To execute this activity, perform the steps ‘Describe Project’ (under Project Setup) and ‘Update Project Status’ (under Project Milestone Review) using the app My Projects - Project Manager (F1876) as mentioned in 1YF- Project Review test script, using the project from this document

A possible list of Milestones can be the following:

|  |
| --- |
| ExampleConcept Review and ApprovalFinal Design Review and ApprovalPrototype TestingDesign Release |

### Upload Planned Costs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you upload planned costs to Work Packages.

|  |
| --- |
| Note You will be able to use the Cloud Analytics functionality to input planned costs to the project by using the test script for scope item [2YG](https://me.sap.com/processnavigator/SolP/2YG). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller |  |  |
| 2 | Access App | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data screen is displayed. |  |
| 3 | Download Template; Fill the planned costs in the CSV file | Choose Download Templates. A pop-up window appears.In the pop-up window, choose , (Comma) from the Separator for .csv files dropdown and then choose Project Planning; the template CSV file will be downloaded to the local machine.Choose Close.Access / open the file and fill the plan values.Make sure to save the file in CSV (Comma delimited) (*.csv) format .Note Remember the location of the file stored. | CSV file is saved with the plan costs. |  |

Adapt the Project Planning Template

A template table is provided for your reference with sample values as follows:

| Category | General Ledger Fiscal Year | Posting Period | Company Code | Project Definition | Work Breakdown Structure Element (WBS Element) | Account Number | Amount in Global Currency | Global Currency |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X | X | X | X | X |  |  |  |  |
| PLN | <current year>Example 2018 | <current month>Example 8 | 3310 | RnD_00001 | RnD_000XX_01 | 94311000 | 1000 | USD |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 4 | Import Planned Cost Data | Choose Browse. Select the CSV file from the local system which has the planned cost data already maintained for the project created above.Choose Import Source File. | A message confirms that the import is successful. |  |

### Assign Project Budget

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post planned budget to Work Package.

|  |
| --- |
| Note You will be able to allocate the project budget following this procedure below or by using the Analytics Cloud functionality to input planned budget to the project by using the test script for scope item [2YG](https://me.sap.com/processnavigator/SolP/2YG). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data screen is displayed. |  |
| 3 | Download Template; Fill the planned Budget in the CSV file | Choose Download Templates. A pop-up window appears.In the pop-up window, choose , (Comma) from the Separator for .csv files dropdown and then choose Project Budgeting; the template CSV file will be downloaded to the local machine.Choose CloseAccess / open the file and fill the planned Budget values.Make sure to save the file in CSV (Comma delimited) (*.csv).Note Remember the location of the files stored. | CSV file will be saved with the budget details. |  |

Adapt the Project Budget Template

A template table is provided below for your reference with sample values:

|  |
| --- |
| Note The following account is not specific for budget allocation, you can also use a different account for the posting. |

| Category | General Ledger Fiscal Year | Posting Period | Project Definition | Work Breakdown Structure Element (WBS Element) | Account Number | Amount in Global Currency | Global Currency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| X | X | X | X |  |  |  |  |
| BUDGET01 | <current year>Example: 2018 | <current month>Example: 04 | RnD_00001 | RnD_00001_01 | Example: 94311000 | 1000 | USD |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 4 | Import Planned Budget Data | Choose Browse. Select the CSV file from the local system which already has the planned budget data maintained for the project created above.Choose Import Source File. | A system message tells you that the import is successful. |  |

### Define Demand

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity deals with demand planning activities for the project.

Procedure

To execute this activity, run the step 'Define Demand' from 4RF- Project Control – Resourcing and Procurement test script to create project related demands

### Release Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release the Project.

|  |
| --- |
| Note To use the workflow for the project release approval process, perform the steps described in Review Workflow for the Release of a Project (Optional) of the Project Review (1YF) test script, using the project from this document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215) | The Project Control screen is displayed. |  |
| 3 | Open Project | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter 'Create Project '>Example RnD_00001 (for R & D Projects) | At least one entry is displayed in the Worklist area. |  |
| 4 | Release Project and Structure | Select the project and in header section choose Processing Status > Release | Project status is changed to Released.NoteYou can also use the Change Processing status using the Project Briefs app in the role of Project Manager .Project once released cannot be renamed or deleted |  |
| 5 | Maintain actual start date in WBS Elements | Choose Related Apps > Project Planning . Choose Edit to open the project in change mode.For all created WBS elements, maintain Actual Start Date field in in WBS Element Detailed Overview pageChoose Save. | Project is saved with the Actual start dates for WBS elements. |  |

### Time Recording

Purpose

In this activity, employee enters the time recording for WBS Element via Manage My Time Sheet application.

Procedure

To execute this activity, execute 1Q4 - Time Recording test script, using the WBS Element from this document.

|  |
| --- |
| Note While creating the task, maintain the Activity Type as 11 and WBS element created in the Create Project step of this document. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element | <RnD_00001.03> | <WBS for Prototype Phase > |  |

### Project Demand

Purpose

This activity deals with planning demand activities for the project.

Procedure

To execute this activity, run steps from 4RF- Project Control – Resourcing and Procurement test script to create and process your project related demands.

### Project Control - Procurement

Purpose

This activity deals with demand planning and consumable purchasing activities for the project.

Procedure

To execute this activity, run steps from 4RF- Project Control – Resourcing and Procurement test script to process your purchase requisitions generated from project demand.

### Post General Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post actual primary costs to WBS Elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Post General Journal Entries (F0718). | The Post General Journal Entries screen is displayed. |  |
| 3 | Enter General Journal Entries | On the Post General Journal Entries screen, make the following entries:Journal Entry Date: TodayPosting Date: TodayJournal Entry Type: SACompany Code: 3310Transaction Currency: AEDIn the Line Items area, make the following entries and choose Enter:Line Item 1G/L Account: 61003000 or 50305000 or 51100000Debit: 1000Credit: 0Choose Expand All.Tax Code: <Input Tax Code>WBS Element: <Enter the WBS Element>Line Item 2G/L Account: 10010000Debit: 0Credit: 1000Choose PostCaution In case pro-rata VAT is relevant for you, please make sure you meet the prerequisites as mentioned in chapter 2. | Check that Total Balance is 0.00 |  |
| 4 | Optional: Batch upload general Journal entries | Download Template file to local:On the Post General Journal Entries screen, choose Upload New Entry.On the Upload General Journal Entries screen. Choose Download Template.On the Template Download pop-up window, make the following entries, then choose Download.Template Language: ArabicFormat: MS Excel Workbook (*.xlsx)Download the template file to the local and fill general journal entries according to the template.Upload Template file and batch upload general journal entries:On the Post General Journal Entries screen, choose Upload New Entry.On the Upload General Journal Entries screen, choose Browse.On the pop-up screen, choose your local filled out template file and upload it.A system message tells you that the held journal entries have been updated.Check batch upload general journal entries. | The General Journal Entries are posted. |  |
| 5 | Post General Journal Entries | Choose Post. | A success message appears displaying the document number. |  |

### Monitor Projects

Purpose

In this activity, you can analyze the costs (planned/actual) recorded on the project using different tiles available on the Fiori launchpad. You can also check project progress and the overall status of your project.

#### Monitor Notification (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Project Financial Controller. |  |  |
| 2 | Choose the notifications | Choose the Notifications icon at the top right of the Home screen.Choose the notifications which are generated by the system.Note This notification will be displayed only in case there is a situation of actual postings exceeding the budget threshold limit set in the AVC profile selected for the project. | The Project Budget Report-Overview screen is displayed. |  |
| 3 | Detailed information from notifications | Open Project Control - Enterprise Projects (F3215).In the Standard section, make the following entry and choose Go:Project: <Refer the Project mentioned in the notification>Select the project from the displayed list and click to open.The Situations section of the project is displayed and information like the actual posting date and the WBS, to which the postings are made, is displayed.You can also see the list of notifications from the situation management that got triggered against the project by clicking on the drop-down arrow in the notification. | Detailed information of the situation is displayed. |  |
| 4 | Actions in notifications | You can choose to dismiss the notification by selecting one of the following actions:Situation ResolvedSituation ObsoleteSituation InvalidOnce the situation is dismissed, no one can see the situation. | Situation is dismissed by selecting the appropriate option. |  |

#### Monitor Projects via Project Financial Controller Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you analyze the status, timelines, budget and costs of project.

:

|  |
| --- |
| Note You will be able to access the reports such as Project Cost,Plan vs Actual, Project Budget Report and Monitor Projects directly from Project Financial Overview. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Financial Controller Overview (F3078) | The Project Financial Controller Overview screen is displayed. |  |
| 3 | Enter Selection Criteria | In the standard section, make the following entries and choose Go.Planning Category: PLN. | Projects with selected planning category are displayed in the Data Analysis area. |  |
| 4 | Check Financials | Check Financials and Overall status of the project using various cards. | The Overall Status, Planned and Active Projects, Actual costs, Cost to Date, Timeline and Upcoming Milestone are displayed. |  |

#### Monitor Projects via Monitor Projects App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you analyze the cost and overall progress of your project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Monitor Projects (F3088) | The Monitor Projects screen is displayed. |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Project: RnD_00001Planning Category: PLN | At least one entry is shown in the Worklist display area. |  |
| 4 | Check Financials | From the Worklist area, select the project and choose View Costs to check project costs. | Project Costs report of the selected project is displayed |  |
| 5 | Check Project Progress | From the Worklist area, select the project and choose Project Progress to go to the Monitor Project Progress screen which shows the project timelines. | A detailed view of project progress is displayed in graphical form |  |

#### Monitor Projects via Project Cost Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you analyze the cost structure of your project and check planned cost.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Cost Report - Plan/Actual (F2513) | The Project Cost screen is displayed. |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Project: RnD_00001Planning Category 1: PlanPlanning Category 2: CPM Baseline | Details of the project structure and the corresponding Plan and Actual costs as well as commitments are displayed. |  |
| 4 | Navigation to Project Cost Report – Line items; view details of different cost | Select the project in the table, and choose View Details.On Project Costs - line items screen, check financials using drilldown and filter possibilities. | All Plan and Actual costs are displayed. |  |

#### Monitor Projects via Project Budget Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you analyze the cost structure of your project and check planned budget.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Budget Report (F3377) | The Project Cost screen is displayed. |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Project: RnD_00001Planning Category 1 :PlanFiscal Year: Current year | Details of the project structure and the corresponding planned budget are displayed.Note The Aggregated and Non Aggregated Costs of the selected project are displayed.In the budget report, you will see the Assigned Value (commitment +Actual) and Available budget (Budget-Assigned Value), based on which you can analyze the project. |  |
| 4 | Navigation to Project Budget Report – Line items; view details of different cost | Select the project in the table, and choose View Details.On the Project Budget Report- line items screen, check financials using drilldown and filter possibilities.Note In the Standard section, the information is shown in the Compact Filter view by default.You can also change it to Visual Filter view to get an easy understanding of overall costs of the project.This visual depiction helps the stakeholders to get an overview of the project | All Plan, Actual and Budget costs are displayed. |  |
| 5 | Navigation to Project Budget Report- Line items: view graphical representation of different costs | In the Project Budget Report - Line items screen, you will see the different cost items recorded on the project as graphical representations, such as the bubble chart, bar graph and pie chart.Note You can see the details of the cost items by hovering the cursor on the graphs. | The Cumulative Actual costs, Commitments and Budget posted on the project are displayed. |  |

#### Monitor Projects via Manage Project Procurement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor the purchasing documents via the Manage Project Procurement app and check net order value or ordered quantity for purchase order or purchase requisitions assigned to the project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Manage Project Procurement (F2930) |  |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Project: <Enter the Project>Display currency : AEDPO Delivery Status : Open | Details of the project related to purchase order and purchase requisition such as the following are displayed according to selection :delivery quantitynet order valuedelivery date and so onYou can click on each link to get more information. |  |

#### Monitor Projects via P&L Plan/Actual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you analyze the cost structure of your PS Project and compare actual vs planned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open P&L Plan/Actual - Profit and Loss (F1710)(F1710) | The P&L Plan/Actual screen is displayed. |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Ledger: 0LLedger Fiscal Year: Current yearPlanning Category: PLNProject definition: <Enter the Project Definition> | At least one entry is shown in the Data Analysis area. |  |
| 4 | Check Financials | Check financials using drilldown and filter possibilities. | All actual costs are displayed. |  |

### Period-End Closing Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Financial Controller records the percentages of actual overheads on the project, generates the settlement rule and settles the actuals on the project.

Procedure

To execute this activity, the Project Financial Controller performs the step ‘Run Actual Overhead-Projects’ and 'Period-End Process: Internal Cost Projects ' as mentioned in BNA - Period-End Closing – Projects test script, using the WBS Element from this document.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element | < RnD_000XX.03> | <WBS for Prototype Phase> |  |

### Close Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, Project Financial Controller close the completed project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215) | The Project Control screen is displayed. |  |
| 3 | Open Project | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter 'Create Project '>Example RnD_00001 (for R & D Projects) | At least one entry is displayed in the Worklist area. |  |
| 4 | Complete Project Parts and Project | Select the Project and in header section choose Processing Status and choose Complete | Project is saved with status Completed. (The system status is set to Technically Complete) |  |
| 5 | Close Project and Structure | Select the Project and in header section choose Processing Status and choose Close | Project is saved with status Closed. . |  |

## Appendix

### Process Integration

#### Preceding Processes

#### Succeeding Processes

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
> Flagged while digesting this document, not verified: Functional area YB75 is described as 'Research & Development' in the master data table but as 'Other expenses' in the Create R&D Project step.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/period-end-closing-projects-bna-ae-test-script-sap-s-4hana-cloud-publi]]
- related-to :: [[06-management-accounting/test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud]]
- related-to :: [[06-management-accounting/test-script-project-control-finance-1nt-ae-sap-s-4hana-cloud-public-ed]]
- related-to :: [[06-management-accounting/test-script-project-control-resourcing-and-procurement-4rf-ae-1049]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/35E_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 70,198 chars in the whole document
