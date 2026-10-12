---
id: 06-management-accounting/test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud
title: "Test Script: Project Control – Capital Projects (35F_AE), SAP S/4HANA Cloud Public Edition (35F_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 35F (AE): prerequisites and test steps to create, budget, release, monitor, settle and close capital investment projects."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/project-control-enterprise-projects]
aliases: [35F_S4CLD2608_BPD_EN_AE]
keywords: ["Project Control for Finance, Capital, R&D and Sales Projects", capital investment projects, project creation, project budget, budget availability control, planned costs, project monitoring, assets under construction, project settlement, project status management]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/35F_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-919
topic: 06-management-accounting/project-control-enterprise-projects
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Project Control – Capital Projects (35F_AE), SAP S/4HANA Cloud Public Edition (35F_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/35F_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Project Control for Finance, Capital, R&D and Sales Projects** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Project Control – Capital Projects (35F_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232852025)

[2 Prerequisites 5](#_Toc232852026)

[2.1 System Access 5](#_Toc232852027)

[2.2 Roles 5](#_Toc232852028)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232852029)

[2.4 Business Conditions 8](#_Toc232852030)

[2.5 Preliminary Steps 8](#_Toc232852031)

[2.5.1 Setting Up Custom Fields for Project (Optional) 8](#_Toc232852032)

[2.5.2 Maintain Cost Rates 9](#_Toc232852033)

[2.5.3 Maintain Financial Statement Versions 10](#_Toc232852034)

[2.5.4 Create Project Coding Mask 11](#_Toc232852035)

[2.5.5 Create Project Types for WBS Elements (Optional) 13](#_Toc232852036)

[2.5.6 Maintain Budget Availability Profile using Self Service Configuration (SSC) UI app (Optional) 15](#_Toc232852037)

[2.5.7 Manage Situation Types (Optional) 19](#_Toc232852038)

[2.5.8 Manage Teams and Responsibilities for Projects (Optional) 21](#_Toc232852039)

[2.5.9 Maintain Cost Element Groups (Optional) 22](#_Toc232852040)

[3 Overview Table 23](#_Toc232852041)

[4 Test Procedures 26](#_Toc232852042)

[4.1 Create Project 26](#_Toc232852043)

[4.1.1 Create Capital Investment Project 26](#_Toc232852044)

[4.1.2 Create Capital Investment Project Using Copy Functionality (Optional) 32](#_Toc232852045)

[4.2 Describe Project (Optional) 33](#_Toc232852046)

[4.3 Capture Planned Costs 34](#_Toc232852047)

[4.4 Review and Approve Project(Optional) 36](#_Toc232852048)

[4.5 Capture Project Budget 36](#_Toc232852049)

[4.5.1 Upload Project Budget 37](#_Toc232852050)

[4.5.2 Transfer Project Budget (Optional) 38](#_Toc232852051)

[4.6 Define Demand 40](#_Toc232852052)

[4.7 Release Projects 41](#_Toc232852053)

[4.8 Time Recording 42](#_Toc232852054)

[4.9 Post General Journal Entries 43](#_Toc232852055)

[4.10 Project Control Procurement 45](#_Toc232852056)

[4.11 Monitor Projects 45](#_Toc232852057)

[4.11.1 Monitor Notification (Optional) 46](#_Toc232852058)

[4.11.2 Monitor Projects via Project Financial Controller Overview 47](#_Toc232852059)

[4.11.3 Monitor Projects via Monitor Projects App 48](#_Toc232852060)

[4.11.4 Monitor Projects via Project Cost Report 49](#_Toc232852061)

[4.11.5 Monitor Projects via Project Budget Report 50](#_Toc232852062)

[4.11.6 Monitor Projects via Manage Project Procurement 51](#_Toc232852063)

[4.11.7 Monitor Projects via P&L Plan/Actual 52](#_Toc232852064)

[4.12 Maintain Settlement Rule Parameters (Optional) 53](#_Toc232852065)

[4.12.1 Maintain Settlement Rule Parameters For Project Header 54](#_Toc232852066)

[4.12.2 Maintain Settlement Rule Parameters For WBS Element 54](#_Toc232852067)

[4.12.3 Generate Settlement Rule (Optional) 55](#_Toc232852068)

[4.13 Run Actual Overhead-Projects 56](#_Toc232852069)

[4.14 Asset Under Construction Settlement 57](#_Toc232852070)

[4.15 Update Project Status (Optional) 57](#_Toc232852071)

[4.16 Review Project(Optional) 58](#_Toc232852072)

[4.17 Adjust Project Budget (Optional) 59](#_Toc232852073)

[4.18 Complete Project 59](#_Toc232852074)

[4.19 Post General Journal Entries 60](#_Toc232852075)

[4.20 Time Recording 61](#_Toc232852076)

[4.21 Monitor Projects 61](#_Toc232852077)

[4.22 Create Fixed Asset 62](#_Toc232852078)

[4.23 Maintain Settlement Rule for Final Settlement 62](#_Toc232852079)

[4.24 Allocate Overheads 63](#_Toc232852080)

[4.25 Final Settlement of the Investment Projects 64](#_Toc232852081)

[4.26 Close Project 64](#_Toc232852082)

[5 Appendix 66](#_Toc232852083)

[5.1 Process Integration 66](#_Toc232852084)

[5.1.1 Preceeding Processes 66](#_Toc232852085)

[5.1.2 Succeeding Processes 66](#_Toc232852086)

## Purpose

Overview

This scenario helps you to manage and control the enterprise wide project related investments. Starting with project creation, it covers project structuring, budgeting, execution, and monitoring, enabling transparency to all project stakeholders. This helps to reduce the risk of budget overruns and project delays.

Special functions can be used for investment projects. Investment projects are used to capture the costs of assets under construction (AuC) during the construction phase. Once the AuC is complete, the final asset is created in the appropriate asset class, and the investment project is set to complete. The next settlement transfers the AuC asset value to the completed asset.

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
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
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
| Cost Center | 3310130133101321 | Manufacturing 1 (AE)Services/Consltg |  |
| Activity Types | 11 | Personnel Hours |  |
| Cost Rate | Actual and planned cost rates are maintained for the following combination of cost centers or activity types:Cost centers: 33101301 , 33101101Activity types: 11 |  | Cost Rates are defined time-dependent |
| G/L Account | 61005000 | Trav. Expense – Ground transportation |  |
| 61007000 | Trav. Expense – Airfare, Rail, Mileage |  |  |
| 61003000 | Travel Expenses – Hotel and Accommodation |  |  |
| 61008000 | Travel Expenses – Miscellaneous |  |  |
| 10010000 | Petty CashNote For reporting and budget availability control, certain prerequisites with regard to Financial Statement Version (FSV) item assignment needs to be fulfilled in case new G/L accounts are created. |  |  |
| Profit Center | YB110 | Product A |  |
| Functional Area | YB75 | Other expenses |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS):

| MDS | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| 3KW | Create CO Cost Rates - MDS |
| BNH | Create Profit Center - MDS |
| BNI | Create Asset - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1YF - Project Review | To execute the project review and project collaboration functionalities, the Project Review (1YF) scope item must be activated. |
| BNA - Period-End Closing – Projects | To execute the period end closing activities for the project, the BNA - Period-End Closing – Projects scope item must be activated. |
| J62 - Asset Accounting | To perfom the step Release Projects, you need to execute the step Year End Closing of the J62 - Asset Accounting scope item to define the asset accounting specific company code settings. |
| 4RF - Project Control – Resourcing and Procurement | To plan demand for the project, the 4RF- Project Control – Resourcing and Procurement scope item must be activated.. |
| BNI - Create Asset - MDS | During the execution of this scope item, asset master records will be created for assets under construction and the assets to which final settlement is performed. To create the assets, use the Create Asset - MDS (BNI) master data script using the data described in this test script. |

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

#### Maintain Cost Element Groups (Optional)

This is an optional step before creating a Project.

|  |
| --- |
| Note you also define your own investment profile and source structure with the help of the following available SSCUIs as mentioned in BNA- Period-End Closing – Projects test script.Define Investment Profile (104255)Define Assignment of AuC Classes per Source Assignment (104256) |

Purpose

The Edit Cost Element Groups app is used to update the cost elements / GLs and cost element groups in the predeliverd cost element groups.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead |  |  |
| 2 | Access App | Open Manage Cost Element Groups (F5373) . | The Change Cost Element Group: Initial Screen is displayed. |  |
| 3 | Update the missing GL | Maintain the following Information and choose Enter.Cost Element Group: Example: YS100Select the cost element group and choose Cost Element icon to update the desired GLs.Note You can update the cost element grouping for any missing GL using the Manage Cost element Group app and do not need to update the allocation structure. Updating the predelivered cost element groups should be sufficient to avoid any error. | The Change Cost Element Group: Structure Screen is displayed |  |

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Project](#unique_18) [page ] 26 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project definition and WBS Elements with all the required parameters will be created. |
| [Create Capital Investment Project](#unique_19) [page ] 26 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project definition and WBS Elements with all the required parameters will be created. |
| [Create Capital Investment Project Using Copy Functionality (Optional)](#unique_20) [page ] 32 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project definition and WBS Elements with all the required parameters will be created. |
| [Describe Project (Optional)](#unique_21) [page ] 33 | See the scope item 1YF- Project Review | See the scope item 1YF- Project Review | See the scope item 1YF- Project Review |
| [Capture Planned Costs](#unique_22) [page ] 34 | Project Financial Controller | Import Financial Plan Data (F1711) | Planned costs for the project WBS Element are posted |
| [Review and Approve Project(Optional)](#unique_23) [page ] 36 | See the scope item 1YF- Project Review | See the scope item 1YF- Project Review | See the scope item 1YF- Project Review |
| [Upload Project Budget](#unique_24) [page ] 37 | Project Financial Controller | Import Financial Plan Data (F1711) | Budget for the Project WBS elements are posted |
| [Transfer Project Budget (Optional)](#unique_25) [page ] 38 | Project Financial Controller | Manage Budget Documents - Projects (F5342) | Budget is transferred from one WBS element to another WBS element. |
| [Define Demand](#unique_26) [page ] 40 | See scope item 4RF- Project Control – Resourcing and Procurement | See scope item 4RF- Project Control – Resourcing and Procurement | See the scope item 4RF- Project Control – Resourcing and Procurement |
| [Release Projects](#unique_27) [page ] 41 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project status should be changed to REL (Release) |
| [Time Recording](#unique_28) [page ] 42 | See scope item 1Q4- Time Recording | See scope item 1Q4- Time Recording | See scope item 1Q4- Time Recording |
| [Post General Journal Entries](#unique_29) [page ] 43 | General Ledger Accountant | Post General Journal Entries (F0718) | Post actual primary costs to WBS elements |
| [Project Control Procurement](#unique_30) [page ] 45 | See scope item 4RF- Project Control – Resourcing and Procurement | See scope item 4RF- Project Control – Resourcing and Procurement | See scope item 4RF- Project Control – Resourcing and Procurement |
| [Monitor Projects](#unique_31) [page ] 45 | Project Financial Controller | Project Financial Controller Overview or Project Budget Report or Monitor Projects or P&L Plan/Actual or Project Cost Report Plan/Actual. | Compare Project actual vs planned and track project procurments |
| [Maintain Settlement Rule Parameters (Optional)](#unique_32) [page ] 53 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Settlement rule parameters for settlement to Multiple AuCs are maintained. |
| [Run Actual Overhead-Projects](#unique_33) [page ] 56 | See scope item BNA – Period-End Closing – Projects | See scope item BNA – Period-End Closing – Projects | See scope item BNA – Period-End Closing - Projects |
| [Asset Under Construction Settlement](#unique_34) [page ] 57 | See scope item BNA- Period-End Closing – Projects | See scope item BNA- Period-End Closing – Projects | See scope item BNA- Period-End Closing – Projects |
| [Update Project Status (Optional)](#unique_35) [page ] 57 | See the scope item 1YF- Project Review | See the scope item 1YF- Project Review | See the scope item 1YF- Project Review |
| [Review Project(Optional)](#unique_36) [page ] 58 | See scope item 1YF- Project Review | See scope item 1YF- Project Review | See scope item 1YF- Project Review |
| [Adjust Project Budget (Optional)](#unique_37) [page ] 59 | Project Financial Controller | Import Financial Plan Data (F1711) | Budget for the Project WBS elements are adjusted |
| [Complete Project](#unique_38) [page ] 59 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project Status should be changed to TECO (Technically complete) |
| [Post General Journal Entries](#unique_39) [page ] 60 | General Ledger Accountant | Post General Journal Entries (F0718) | Post actual primary costs to WBS elements |
| [Time Recording](#unique_40) [page ] 61 | See scope item 1Q4- Time Recording | See scope item 1Q4- Time Recording | See scope item 1Q4- Time Recording |
| [Monitor Projects](#unique_41) [page ] 61 | Project Financial Controller | Project Financial Controller Overview or Project Budget Report or Monitor Projects or P&L Plan/Actual or Project Cost Report Plan/Actual. | Compare Project actual vs planned and track project procurements |
| [Create Fixed Asset](#unique_42) [page ] 62 | See scope item BNA- Period-End Closing – Projects | See scope item BNA- Period-End Closing – Projects | See scope item BNA- Period-End Closing – Projects |
| [Maintain Settlement Rule for Final Settlement](#unique_43) [page ] 62 | See scope item BNA- Period-End Closing – Projects | See scope item BNA- Period-End Closing – Projects | See scope item BNA- Period-End Closing – Projects |
| [Allocate Overheads](#unique_44) [page ] 63 | See scope item BNA- Period-End Closing – Projects | See scope item BNA- Period-End Closing – Projects | See scope item BNA- Period-End Closing – Projects |
| [Final Settlement of the Investment Projects](#unique_45) [page ] 64 | See scope item BNA- Period-End Closing – Projects | See scope item BNA- Period-End Closing – Projects | See scope item BNA- Period-End Closing – Projects |
| [Close Project](#unique_46) [page ] 64 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project Status should be changed to CLSD (Closed) |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Project

Purpose

In this activity, you can create Investment projects with the project definition and WBS Elements using the Fiori app Project Control - Enterprise Projects (F3215) directly from scratch or by using the copy functionality.

For hierarchical project accounting requirements, you can also create a hierarchical project structure by calling up the Project Planning application from the Project Control - Enterprise Projects (F3215) app.

#### Create Capital Investment Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create a Capital Investment project with project definition and WBS Elements.

For hierarchical project accounting requirements, you can also create a hierarchical project structure by calling up the Project Planning application from the Project Control app

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215) | The Project Control – List screen is displayed. |  |
| 3 | Create Project: Header | Choose Create.Make the following entries in the Header section:Project Name: General Capital ProjectProject ID: I.000XX (For Example:I.00001)Project Profile: Investment ProjectPlanned Start: TodayPlanned Finish: Today + 3 monthsMake the following entries in the and General Information section:Resp. Cost Cntr: 33101301 (Manufacturing 1)Profit Center: YB110 (Product A)Project Currency: AED(Automatically filled based on the cost center)Note You can specify the currency at project level different from controlling area currency, to run project specific financial reports.Project Manager: The Project Manager IDPriority: the priority suitable for projectProject Type: Project type created using SSCUIIn the Attachments section, do the following:Choose + to upload project relevant documents from your local drive.Choose CreateA system message tells you that the object is created.When the project header is being created, Project Summary Task WBS Element will be automatically created.In the Settlement section, do the following:Settlement Rule Maintenance: Without Pass-Down OptionNote During project creation, the Settlement Rule Maintenance is set to Without Pass-Down Option by default. You can change it to With Pass-Down Option if required.If you want to pass the project header settlement rule down to the subordinate WBS element in the WBS hierarchy, select the Pass-Down Settlement Rule checkbox also.For more information on maintaining project settlement rules, on [https://help.sap.com](https://help.sap.com), search for Project Control-Enterprise Projects, and refer to the Maintain Project Settlement Rules section. | Project is created with the provided definition parameters.WBS Element ID: I.000XXDescription: General Capital Project. |  |
| 4 | Add Values to the Project | Once the project is created (I.000XX), from the header section, choose Edit.Make the following entries in the General Information section:Plant: 3310Functional Area :YB75 (Other expenses)Make the following entries in the Control section:Investment Profile: <Example: 000001 - Model with AuC, summary settlement>Note If you need settlement to multiple AuCs, select investment profile YS0001- Model for AuC per source structure/assignmentCosting Sheet: 3310PIThe following are optional entries, maintain them according to your requirements.Budget Availability Control Profile: Select the Budget Availability Profile created using SSCUI as mentioned in Preliminary Step ([Maintain Budget Availability Profile using Self Service Configuration (SSC) UI app (Optional)](#unique_13) [page ] 15)Example ZS001Note If project currency is maintained, you can assign a budget availability control profile where the budget currency is maintained as Global Currency or Project CurrencyIf project currency is not maintained, you can only assign an availability control profile where the budget currency is maintained as Global Currency.Budget Availability Control Profile is active: SelectedNoteYou can define your own budget availability profile using an SSCUI.As soon as you have planned budget for your project and activated the budget availability control, the hierarchy changes are no longer possible.Note You will be able to see Joint Venture (JV) attributes under the section Joint Venture Accounting during project creation, if the Joint Venture accounting functionality has been activated in the system. For the detailed explanation on JV attributes, you can refer to the scope item 3F7-Joint Venture Accounting .Block FunctionsTime Recording: <Selected/Not Selected>Activity Allocation: <Selected/Not Selected>Purchasing: <Selected/Not Selected>Concur Expense Posting: <Selected/Not Selected>Other Expense Posting: <Selected/Not Selected>NoteSetting up the block functions at Project Header level will not impact the complete project hierarchy.The Block functions need to be set at the individual Work Package level to enable the functionality.Even if the user blocks purchasing for a WBS Element, the system can still generate purchasing documents if the account assignment category in the purchase document is "Q" (Project Make-to-Order) and the account is associated with that WBS Element. [https://me.sap.com/notes/3459521](https://me.sap.com/notes/3459521)Choose SaveA message tells you that the project is saved. | Project is updated with all the provided parameters.Note In case you have entered a budget availability control profile and activated the budget availability control, all postings resulting into commitments or actual costs will be checked against the available budget of the WBS Element used as account assignment object.In case the WBS Element itself does not have any budget, the next higher level budget carrying WBS Element will be used for the budget availability check.Depending on the tolerance limits defined for the availability control profile, the system can raise warning or error messages.Depending on the Time Range defined for the availability control profile, you will be able to check the budget consumption for a particular fiscal year or across fiscal years.This setting is valid for all kind of expense postings and expected expense postings (for example, purchase requisition or purchase orders) to a WBS Element.Warning messages from budget availability check are not shown in case of automatic periodic postings and certain goods movement. |  |
| 5 | Navigate to Project Planning | Once the project is created (I.00001), from the header section, choose Related Apps A pop-up screen appears.From the pop-up screen, select Project Planning to navigate to the Project Planning app.Note By default the project will be in Display mode. To edit the project, choose Edit . | The Project Planning app is open and you can make further entries. |  |
| 6 | Create WBS Element under Project. | In the Project Planning view, select project created (I.000XX) in the above step, and choose Create.ID : I.000XX1Name: WBS for project managementProfit Center: <This data is pre-populated from the Project>Resp. Cost Cntr: 33101301 (Manufacturing 1) (This data is pre-populated from first WBS level).Planned Start Date: TodayPlanned Finish Date: Today + 3 monthsIn the Project Planning view, select Project (I.000XX) created in the above step, and choose CreateID: I.000XX2Name: WBS for project planningProfit Center:<This data is pre-populated from the project>Resp. Cost Cntr: 33101301 (Manufacturing 1) (This data is pre-populated from project).Planned Start Date: TodayPlanned Finish Date: Today + 3 monthsNote You can also include WBS Element of another project by making use of the Include functionality available in the project planning application (while Including the WBS Element, the existing demands and settlement rules of the source WBS Element are not included).Create WBS Element structure based on your requirements or refer to the following example:Example1I.00001General Project all Sub-Projects2I.000011Project Management3I.0000111Coordination- AuC1-A14I.0000112Monitoring- Auc2-A15I.0000113Reporting-AuC3-A16I.000012Planning7I.0000121Object Part I8I.00001211Set up Project Plan & Team9I.00001212Specification10I.00001213Quality and Detail Planning11I.00001214Review Requirements12I.00001215Acceptance and Approval13I.0000122Object Part II14I.00001221Set up Project Plan & Team15I.00001222Specification16I.00001223Quality and Detail Planning17I.00001224Review Requirements18I.00001225Acceptance and Approval19I.000013Realization & Settlement20I.0000131Object Part I21I.00001311Procurement Processes22I.00001312Postings of internal labour services23I.00001313Postings of external efforts24I.00001314Efforts of general Project-related activities25I.0000132Object Part II26I.00001321Procurement processes27I.00001322Postings of internal labour services28I.00001323Postings of external efforts29I.00001324Efforts of general Project-related activitiesNote During WBS element creation, by default, Pass-Down Settlement Rule is not selected. However, you can select it if required. (A WBS element can only be defined as a settlement element if the pass-down option for settlement rule maintenance is enabled in the project header.)For this, in the Project Planning view, select the created WBS element (I.000XX1) in the above step, and choose Details.In the General Information section: Select the Pass-Down Settlement Rule checkbox for those WBS elements whose settlement rule is passed down to the WBS elements in their subtrees. | Project with WBS Element structure is updated with the provided parameters. |  |
| 7 | Save Project Structure | Choose Save. | Project with WBS Element structure is saved |  |

#### Create Capital Investment Project Using Copy Functionality (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create a Capital Investment project by copying the WBS element structure from the existing project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215). | The Project Control screen is displayed. |  |
| 3 | Create Project | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter [Create Project](#unique_18) [page ] 26 >Example I.00001 (for Investment Project)Select the project displayed in the list view and choose CopyMake the following entries in the Copy pop-up screen:Project ID: I.000XX (For Example:I.00002)Project Name: General Capital ProjectPlanned Start: TodayPlanned Finish: Today + 3 monthsEnter either the Planned Start Date or the Planned Finish DateChoose CopyNote You can either maintain the Planned Start or the Planned Finish Dates, but not both of them.In the Project Overview screen, the details of the reference project is displayed. Make changes if required.Choose Create. | Project is created with the provided definition parameters.One WBS element with the following details is created under the project :WBS element ID: I.000XXDescription: General Capital Project. |  |

### Describe Project (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager describes the project details such as Milestones, Status and Project team for the first time.

Procedure

To execute this activity, perform the following steps using the app My Projects - Project Manager (F1876) as mentioned in 1YF - Project Review test script, using the project from this document.

- ‘Project Setup' →'Describe Project’
- 'Project Milestone Review (Single Project Review)→ Update Project Status '

### Capture Planned Costs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you upload planned costs to WBS Elements.

|  |
| --- |
| Note You will be able to use the Analytics Cloud functionality to input planned costs to the project by using the test script for scope item [2YG](https://me.sap.com/processnavigator/SolP/2YG). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data screen is displayed. |  |
| 3 | Download Template; Fill the planned costs in the CSV file | Choose Download Templates. A pop-up window appears.In the pop-up window, choose , (Comma) from the Separator for .csv files dropdown and then choose Project Planning; the template CSV file will be downloaded to the local machine.Choose Close.Access / open the file and fill the plan values.Make sure to save the file in CSV (Comma delimited) (*.csv) format .Note Remember the location of the file stored. | CSV file is saved with the plan costs. |  |

Adapt the Project Planning Template

A template table is provided for your reference with sample values as follows:

| Category | General Ledger Fiscal Year | Posting Period | Company Code | Project Definition | Work Breakdown Structure Element (WBS Element) | Account Number | Amount in Global Currency | Global Currency |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X | X | X | X | X |  |  |  |  |
| PLN | <current year>Example 2018 | <current month>Example 4 | 3310 | I.00001 | I.000011 | 61005000 | 1000 | USD |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 4 | Import Planned Cost Data | Choose Browse. Select the CSV file from the local system which has the planned cost data already maintained for the project created above.Choose Import Source File. | A system message tells you that the import is successful. |  |

### Review and Approve Project(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the project steering committee members get the information on projects status. They review all the projects in the Project Overview app to prepare themselves for upcoming steering committee meeting.

Procedure

To execute this activity, perform the step ‘Project Milestone Review (Single Project Review)’ as mentioned in 1YF - Project Review test script, using the project from this document.

|  |
| --- |
| Note With the help of Projects (By Key Figures) app you will be able to review multiple projects based on their Priorities and Project Type to check their statuses and project costs.The costs of the projects with the selected project type is shown as a Bubble chart graph, which helps the steering committee members to get an overview |

### Capture Project Budget

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post planned Budget to WBS elements.

|  |
| --- |
| Note You will be able to use the Analytics Cloud functionality to input planned budget to the project by using the test script for scope item [2YG](https://me.sap.com/processnavigator/SolP/2YG). |

#### Upload Project Budget

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post planned budget to WBS Elements.

|  |
| --- |
| Note You will be able to use the Cloud Analytics functionality to input planned budget to the project by using the test script for scope item [2YG](https://me.sap.com/processnavigator/SolP/2YG). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data screen is displayed. |  |
| 3 | Download Template; Fill the planned Budget in the CSV file | Choose Download Templates. A pop-up window appears.In the pop-up window, choose , (Comma) from the Separator for .csv files dropdown and then choose Project Budgeting; the template CSV file will be downloaded to the local machine.Choose CloseAccess / open the file and fill the planned Budget values.Make sure to save the file in CSV (Comma delimited) (*.csv) format.Note Remember the location of the files stored. | CSV file will be saved with the Budget details. |  |

Adapt the Project Budget Template

A template table is provided below for your reference with sample values:

|  |
| --- |
| Note The account provided in the following table is not specific for budget allocation. You can also use a different account for the posting, but the G/L account that is being used should be mapped to the proper semantic tag to show up in the reporting. |

.

| Category | General Ledger Fiscal Year | Posting Period | Project Definition | Work Breakdown Structure Element (WBS Element) | Account Number | Amount in Global Currency | Global Currency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| X | X | X | X |  |  |  |  |
| BUDGET01 | <current year>Example 2018 | <current month>Example 4 | I.00001 | I.000011 | 61005000 | 1000 | USD |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 4 | Import Planned Budget Data | Choose Browse. Select the CSV file from the local system which already has the planned budget data maintained for the project created above.Choose Import Source File. | A system message tells you that the import is successful. |  |

#### Transfer Project Budget (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage (transfer, return and supplement) the budget allocated to WBS element.

You will be able to use the Analytics Cloud functionality to input planned budget to the project by using the test script for scope item [2YG](https://me.sap.com/processnavigator/SolP/2YG).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller . |  |  |
| 2 | Access App | Open Manage Budget Documents - Projects (F5342) | The Manage Budget Documents - Projects screen is displayed. |  |
| 3 | Initiate Project Budget Transfer | Choose Create and select Budget Transfer from the drop down listMake entries as shown in the following example in the General Information and other sections:General InformationPlan Category : Project Budget (BUDGET01)Posting Date : Todays Date (MM/dd/yyyy)Budget Sender ItemsWBS Element: O.0000011Account Number: 61005000Amount in Global Currency: 500Budget Receiver ItemsWBS Element: O.0000012Account Number: 61007000Amount in Global Currency: 500The total of the sender budget items should be equal to the sum of receiver items.Choose Create. | The Budget Transfer document is created. |  |
| 4 | Initiate Project Budget Return | Choose Create and select Budget Return from the drop down listMake entries as shown in the following example in the General Information and other sections:General InformationPlan Category : Project Budget (BUDGET01)Posting Date : Todays Date (MM/dd/yyyy)Budget Return ItemsWBS Element: O.0000012Account Number: 61007000Amount in Global Currency: 500Choose Create.Note The budget return document created can be reversed by choosing the Reverse icon and providing a proper reversal reason. | The budget return document is created |  |
| 5 | Initiate Project Budget Supplement | Choose Create and select Budget Supplement from the drop down listMake entries as shown in the following example in the General Information and other sections:General InformationPlan Category : Project Budget (BUDGET01)Posting Date : Todays Date (MM/dd/yyyy)Budget Supplement ItemsWBS Element: O.0000012Account Number: 61007000Amount in Global Currency: 500Choose Create.Note The budget supplement document created can be reversed, by choosing Reverse icon and providing a proper reversal reason. | The budget supplement document is created |  |

### Define Demand

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity deals with demand planning for project.

Procedure

To execute this activity, execute the scope item 4RF- Project Control – Resourcing and Procurement to create and process your project related demands.

While creating the demand, use the WBS Element created in the test procedure [Create Capital Investment Project](#unique_19) [page ] 26 .

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element | <I.000XX2> | <WBS for planning> |  |

### Release Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity,you release the project to assign or post the actual cost through service and expenses.

|  |
| --- |
| Note To use the workflow for the project release approval process, perform the steps described in Review Workflow for the Release of a Project (Optional) of the Project Review (1YF) test script, using the project from this document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open the Project Control - Enterprise Projects (F3215) | The Project Control screen is displayed. |  |
| 3 | Open Project | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter 'Create Project' >Example I.00001 (for Investment Project) | At least one entry is displayed in the Worklist area. |  |
| 4 | Release Project and Structure | Select the project and in header section choose Processing Status > Release | Project status is changed to Released. AuCs will be created for the WBS elements with a proper investment profile assignedNoteAs a Project Manager, you can also change the processing status by choosing Processing status from the header section of the Project Briefs AppProject once released cannot be renamed or deleted |  |
| 5 | Maintain Actual Start Date in WBS Elements | Choose Related Apps > Project Planning . Choose Edit to open the project in change mode.For all created WBS elements, maintain Actual Start Date field under the WBS Element Detailed Overview page.Choose Save. | Project is saved with the Actual Start Dates for the WBS elements. |  |

### Time Recording

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter the time recording for WBS Element using the Manage My Time sheet application.

Procedure

To execute this activity, execute the 1Q4 - Time Recording test script, using the WBS Element from this document.

|  |
| --- |
| Note While creating the task, maintain the Activity Type as 11 and WBS Element created in the chapter 'Create Project' of this document.. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element | I.000XX2 | WBS for planning |  |

### Post General Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post actual primary costs to Work Packages.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Post General Journal Entries (F0718). | The Post General Journal Entries screen is displayed. |  |
| 3 | Enter General Journal Entries | On the Post General Journal Entries screen, make the following entries:Journal Entry. Date: TodayPosting Date: TodayJournal Entry Type: SACompany Code: 3310Transaction Currency: AEDIn the Line Items area, make the following entries and choose Enter:Line Item 1G/L Account: 61003000Debit: 1000Credit: 0Choose Expand All.Tax Code: <Input Tax Code>WBS Element: I.000XX.01Line Item 2G/L Account: 10010000Debit: 0Credit: 1000Caution In case pro-rata VAT is relevant for you, please make sure you meet the prerequisites as mentioned in chapter 2. | The Total Balance is 0.00 |  |
| 4 | Optional: Batch Upload General Journal Entries | Download the template file to your local machine:On the Post General Journal Entries screen, choose Upload New Entry.On the Document Upload pop-up screen, Choose Download Template.On the Template Download screen, make the following entries and choose Download.Template Language: ArabicFormat: MS Excel Workbook (*.xlsx)Download the template file to your local machine and fill General Journal Entries according to the template.Upload Template file and batch upload General Journal Entries:On the Post General Journal Entries screen, choose Upload New Entry.On the Document Upload screen, choose Browse.On the pop-up screen, choose the template file that you had filled in your local machine and choose Upload File.In the upper area, a system message confirms that the uploaded file has been saved.Check batch upload general journal entries. | The General Journal entries are batch uploaded. |  |
| 5 | Post General Journal Entries | Choose Post. | A success message appears displaying the document number. |  |

### Project Control Procurement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity deals with demand planning and consumable purchasing activities for project.

Procedure

To execute this activity, run steps from 4RF - Project Control – Resourcing and Procurement to process your purchase requisitions generated from project demand.

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
| 3 | Detailed information from notifications | Open Project Control - Enterprise Projects (F3215).In the Standard section, make the following entry and choose Go:Project: <Refer the Project mentioned in the notification>Select the project from the displayed list and click to open.In the Related Situations section of the project, the complete details of the situation, the WBS element details to which the postings are made and the date it got triggered is displayed.You can also see the list of notifications from the situation management that got triggered against the project. | Detailed information of the situation is displayed. |  |
| 4 | Actions in Situation | Click on the line items in Related Situations to navigate to the Project Budget Report-Overview screen.You can check the budget cost defined and the actual cost posted on the project for further analysis |  |  |
| 5 | Actions in notifications | Click on the WBS element shown in the Project Budget Report -Overview screen and choose to dismiss the notification by selecting one of the following actions:Situation ResolvedSituation ObsoleteSituation InvalidOnce the situation is dismissed, no one can see the situation. | Situation is dismissed by selecting the appropriate option. |  |

#### Monitor Projects via Project Financial Controller Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, analyze the status, timelines, budget and costs of the project.

|  |
| --- |
| Note You will be able to access the reports such as Project Cost,Plan vs Actual, Project Budget Report and Monitor Projects directly from Project Financial Overview |

.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Financial Controller Overview (F3078) | The Project Financial Controller Overview screen is displayed. |  |
| 3 | Enter Selection Criteria | In the standard section, make the following entries and choose Go.Planning Category: PLN. | Projects with selected planning category are displayed in the Data Analysis area. |  |
| 4 | Check Financials | Check Financials and Overall Status of the project using various cards. | The Overall Status, Planned and Active Projects, Actual costs, Cost to Date, Timeline and Upcoming Milestone are displayed. |  |

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
| 2 | Access App | Open Monitor Projects (F3088) . | The Monitor Projects screen is displayed. |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Project: I.000XXPlanning Category: PLN | At least one entry is shown in the Worklist area. |  |
| 4 | Check Financials | From the Worklist area, select the project and choose View Costs to check project costs. | Project Costs report of the selected project is displayed |  |
| 5 | Check Project Progress | From the Worklist area, select the project and choose Project Progress to go to the Monitor Project Progress screen which shows the project timelines.Note this will only be possible if 1YF - Project Review is active. | A detailed view of project progress is displayed in graphical form |  |

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
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Project: I.000XXPlanning Category 1: PlanPlanning Category 2: CPM Baseline | Details of the project structure and the corresponding Planned, Actual, and Project Stock costs as well as commitments are displayed. |  |
| 4 | Check Project Cost Report in Detail | Select the project in the table, and choose View Details.On Project Costs - line items screen, check financials using drilldown and filter possibilities. | All Plan and Actual costs are displayed. |  |

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
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Project: I.000XXPlanning Category : PlanFiscal Year: Current year | Details of the project structure and the corresponding planned budget are displayed.Note The aggregated and non aggregated costs of the selected project are displayed.In the budget report, you will see the assigned value (commitment +actual) and available budget (budget-assigned value), based on which you can analyze the project. |  |
| 4 | Navigation to Project Budget Report – Line items; view details of different cost | Select the project in the table, and choose View Details.On the Project Budget Report - line items screen, check the financials using drilldown and filter possibilities.Note In the Standard section, the information is shown in the Compact Filter view by default.You can also change it to Visual Filter view to get an easy understanding of overall costs of the project. This visual depiction helps the stakeholders to get an overview of the project | All the Plan, Actual and Budget costs are displayed. |  |
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

In this activity, you monitor the purchasing documents via the manage project procurment app and check the net order value or ordered quantity for purchase order or purchase requisitions assigned to the project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Manage Project Procurement (F2930) | The Manage Project Procurement screen is displayed. |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Project: I.000XXDisplay currency : AEDPO Delivery Status : Open | Details of the project related to purchase order and purchase requisition such as delivery quantity, net order value, delivery date and so on are displayed according to the selection and you can click on each link to get more information. |  |

#### Monitor Projects via P&L Plan/Actual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can analyze the cost structure of your Project and compare Actual vs Planned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open P&L Plan/Actual - Profit and Loss (F1710) | The P&L Plan/Actual screen is displayed. |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Ledger: 0LLedger Fiscal Year: Current yearPlanning Category: PLNProject definition: I.000XX | At least one entry is shown in the Data Analysis area. |  |
| 4 | Check Financials | Check financials using drilldown and filter possibilities. | All actual costs are displayed. |  |

### Maintain Settlement Rule Parameters (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you maintain the settlement rule parameters if you want the settlement to Multiple AuCs for your investment project.

#### Maintain Settlement Rule Parameters For Project Header

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215) | The Project Control - List screen is displayed. |  |
| 3 | Open the Project | From the Worklist displayed, select the project created and choose Settlement Rule to display the Settlement Overview | The Maintain Settlement Rule: Overview page is displayed for the selected project. |  |
| 4 | Maintain Settlement Parameters | Choose Menu and then select GoTo from the drop down list and click on Settlement Parameters | Maintain Settlement Rule: Parameters page is displayed. |  |
| 5 | Maintain Settlement Parameters - Assign Source Structure | In Maintain Settlement Rule: Parameters page check and maintain the following information and choose SaveSettlement Profile: YPSAUCAllocation Structure: YISource Structure : <Example:YS - Asset AUC w Source Structure>Choose OK.Note If With Pass-Down Option is selected at the project header level then settlement rule pa-rameters defined at project header level will be passed down in the hierarchy until the WBS for which Pass-Down Settlement Rule is explicitly selected. | A success message "Settlement Rule Saved" is displayed.You can see an additional column Source Assignment under Distribution Rules section of the Maintain Settlement Rule: Overview page |  |

#### Maintain Settlement Rule Parameters For WBS Element

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller |  |  |
| 2 | Access App | Open Project Control(F3215) | The Project Control - List screen is displayed. |  |
| 3 | Open the Project | From the Worklist displayed, select the project created. | Project control view is displayed |  |
| 4 | Navigate To Project Planning App | Select Project Planning from Related Apps. | Project Planning view is displayed |  |
| 5 | Select the WBS Element | In the Standard section, Select the WBS Element for which you want to maintain settlement rule parameters and choose Details. |  |  |
| 6 | Maintain Settlement Parameters | Choose Menu and then select GoTo from the drop down list and choose Settlement Parameters. | Maintain Settlement Rule: Parameters page is displayed. |  |
| 7 | Maintain Settlement Parameters - Assign Source Structure | In Maintain Settlement Rule: Parameters page check and maintain the following information and choose SaveSettlement Profile: YPSAUCAllocation Structure: YISource Structure : <Example:YS - Asset AUC w Source Structure>Choose OKNote If With Pass-Down Option is selected at WBS Element then settlement rule parameters defined will be passed down in the WBS hierarchy until the WBS for which Pass-Down Settlement Rule is explicitly selected. | A success message "Settlement Rule Saved" is displayed.You can see an additional column Source Assignment under Distribution Rules section of the Maintain Settlement Rule: Overview page |  |

#### Generate Settlement Rule (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you generate the settlement rules for investment type projects. In the case of direct settlement for each WBS element, it reduces maintenance work. This step is only required if you have selected investment Project WBS with pass-down option for the Settlement Rule Maintenance field. In this case, settlement rules are completely copied down/taken from settlement element to all elements of subtree settled to same receiver during this run.

Procedure

For details to execute this process step, see the Period-End Process: Assets under Construction projects > Optional: Generate Settlement Rule (only relevant for investment projects with pass-down option selected for settlement rule maintenance) test procedure of the Period-End Closing – Projects (BNA) test script.

### Run Actual Overhead-Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you record the percentages of actual overheads on the project.

Prerequisite

The overhead calculation can be carried out only if you have maintained a costing sheet (as described in the ‘Create Project’ topic of this test script)

Procedure

To execute this activity, perform the Run Actual Overhead-Projects step of the Period-End Closing – Projects (BNA) test script using the WBS Element from this document.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element | <I.000XX.02> | <WBS for project planning> |  |

### Asset Under Construction Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can generate the settlement rule and settle the actuals on the project.

|  |
| --- |
| Note Settlement rule is automatically created upon running settlement for the first time as described in BNA Period End Closing – Projects test script. |

|  |
| --- |
| Example All costs collected on the investment project will be settled to the automatically created AuC. |

Procedure

To execute this activity, perform the step ‘Period End Process: Assets Under Construction Projects -Assets under Construction Settlement’ using the app Run Settlement - Actual (F4568) as mentioned in BNA - Period-End Closing – Projects test script, using the WBS Element from this document.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element | <I.000XX.02> | <WBS for project planning> |  |

### Update Project Status (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Manager updates the project details such as Milestones, Status and after discussion with the steering committee, he/she completes the milestones and sets the actual dates for the approved milestones.

Procedure

To execute this activity, perform the steps ‘Update Project Status, Milestone Review and Complete Milestone’ (under Project Milestone Review) using the app My Projects - Project Manager (F1876) as mentioned in 1YF - Project Reviewtest script, using the project from this document

### Review Project(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, project steering committee members get the information on projects status. They review all the projects in the Project Overview app to prepare themselves for upcoming steering committee meeting.

Procedure

To execute this activity, perform the step ‘Analyze Project (under Project Milestone Review)’ as mentioned in 1YF - Project Review test script, using the project from this document.

|  |
| --- |
| Note With the help of Projects (By Key Figures) app you will be able to review multiple projects based on their Priorities and Project Type to check their statuses and project costs.The costs of the projects with the selected project type is shown as a Bubble chart graph, which helps the steering committee members to get an overview |

### Adjust Project Budget (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you update planned budget to WBS elements.

|  |
| --- |
| Note You will be able to use the Cloud Analytics functionality to input planned budget to the project by using the test script for scope item [2YG](https://me.sap.com/processnavigator/SolP/2YG). |

Procedure

To execute this activity, perform the step [Upload Project Budget](#unique_24) [page ] 37 using the app Import Financial Plan Data (F1711) as mentioned in this test script.

### Complete Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, Project Financial Controller completes the status of the project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215). |  |  |
| 3 | Open Project | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter 'Create Project '>Example I.00001 (for Investment Project) | At least one entry is displayed in the Worklist area. |  |
| 4 | Complete Project and Structure | Select the Project and in the header section choose Processing Status > Complete | Project is saved with status Completed. (The system status is set to Technically Complete) |  |

### Post General Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post actual primary costs that have incurred after the previous postings on the WBS Elemens.

Procedure

To execute this activity, perform the steps as mentioned in the section [Post General Journal Entries](#unique_29) [page ] 43 of this document, using the app Post General Journal Entries (F0718).

### Time Recording

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter the time recording of the effort spent for WBS element after the initial Time Recording.

Procedure

To execute this activity, perform the steps as mentioned in section [Time Recording](#unique_28) [page ] 42 of this document

### Monitor Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you monitor the actual cost postings made on the WBS elements during the project tenure.

Procedure

To execute this activity, perform the steps as mentioned in the section [Monitor Projects via Project Budget Report](#unique_53) [page ] 50 of this document

### Create Fixed Asset

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, all actual postings are assigned to the AuC. Once the asset is complete, a transfer is made to the final fixed asset.

Procedure

To execute this activity, perform the step ‘Period End Process: Assets Under Construction Projects – Create Assets for Complete AuC Settlement’ of BNA - Period-End Closing – Projects test script, using the Project from this document

### Maintain Settlement Rule for Final Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the settlement rule for the final settlement is maintained.

Procedure

To execute this activity, perform the step ‘Period-End Process: Assets Under Construction Projects – Maintain Settlement Rule for Final Settlement’ using the app Project Control - Enterprise Projects (F3215) as mentioned in BNA - Period-End Closing – Projects test script, using the WBS element from this document.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS element | <I.000XX.02> | <WBS for project planning> |  |

|  |
| --- |
| Note If you want the settlement to multiple AuCs, that is, to a fixed asset and a cost center and you have maintained the investment profile as YS0001 during project creation, perform the step ‘Period-End Process: Assets Under Construction Projects – Maintain settlement Rule for final settlement with source structure’ using the app Project Control (F3215) as mentioned in BNA- Period-End Closing – Projects test script.ExampleCatSettlement Receiver%Equivalence no.AmountSettlement TypeSource assignmentNoCTR1010150120FUL200FXA<Created in the previous step>80FUL100 |

### Allocate Overheads

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the Project Financial Controller records the percentages of actuals overheads on the project that have been recorded after the tehnical completion of the project.

Procedure

To execute this activity, perform the steps using the app Schedule Overhead Accounting Jobs (F3767) as mentioned in the section [Run Actual Overhead-Projects](#unique_33) [page ] 56 of this document

### Final Settlement of the Investment Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can execute the final settlement for projects / WBS element by transferring the costs from AuCs to the completed Assets. After the final Settlement, the balance of the investment project and of the AuC is Zero.

Prerequisite

All previous process steps are completed successfully.

Procedure

To execute this activity, perform the step ‘Period End Process: Asset Under Construction Projects – Final Settlement of the Investment Project (Collective Processing)’ using the app Schedule Project Accounting Jobs (F5090) as mentioned in BNA - Period-End Closing – Projects test script, using the WBS element from this document.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS element | <I.000XX.O2> | <WBS for project planning> |  |

### Close Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you close the completed project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215) | The Project Control screen is displayed. |  |
| 3 | Open Project | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter 'Create Project '>Example I.00001 (for Investment Project) | At least one entry is displayed in the Worklist area. |  |
| 4 | Close Project and Structure | Select the Project and in header section choose Processing Status > Close | Project is saved with status Closed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceeding Processes

Complete the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| <Scope Item ID> – <Scope Item Title> | <Enter business condition.> |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
|  |  |

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
> Flagged while digesting this document, not verified: Internal contradiction on project coding mask deletion: the note says a coding mask once created can be deleted if no project with the same key exists, while the configuration step notes say once the coding mask is created, deletion is not possible.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Internal sample-data inconsistency: master data lists cost rates for cost centers 33101301 and 33101101 with activity type 11, but the Maintain Cost Rates steps use cost centers 33101321 and 33101101 with activity type 8.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/period-end-closing-projects-bna-ae-test-script-sap-s-4hana-cloud-publi]]
- related-to :: [[06-management-accounting/test-script-project-control-finance-1nt-ae-sap-s-4hana-cloud-public-ed]]
- related-to :: [[06-management-accounting/test-script-project-control-research-and-development-projects-35e-ae-9]]
- related-to :: [[06-management-accounting/test-script-project-control-resourcing-and-procurement-4rf-ae-1049]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/35F_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 103,403 chars in the whole document
