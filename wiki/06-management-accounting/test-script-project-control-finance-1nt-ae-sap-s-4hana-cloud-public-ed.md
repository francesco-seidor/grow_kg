---
id: 06-management-accounting/test-script-project-control-finance-1nt-ae-sap-s-4hana-cloud-public-ed
title: "Test Script: Project Control – Finance (1NT_AE), SAP S/4HANA Cloud Public Edition (1NT_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1NT (Project Control – Finance, AE): create, budget, monitor, settle, complete and close projects."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/project-control-enterprise-projects]
aliases: [1NT_S4CLD2608_BPD_EN_AE]
keywords: ["Project Control for Finance, Capital, R&D and Sales Projects", project control finance, project creation, project budget, budget availability control, planned costs, project monitoring, project settlement, period-end closing, project release]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NT_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-749
topic: 06-management-accounting/project-control-enterprise-projects
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Project Control – Finance (1NT_AE), SAP S/4HANA Cloud Public Edition (1NT_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NT_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Project Control for Finance, Capital, R&D and Sales Projects** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Project Control – Finance (1NT_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847388)

[2 Prerequisites 4](#_Toc232847389)

[2.1 System Access 4](#_Toc232847390)

[2.2 Roles 4](#_Toc232847391)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847392)

[2.4 Business Conditions 7](#_Toc232847393)

[2.5 Preliminary Steps 8](#_Toc232847394)

[2.5.1 Setting Up Custom Fields for Project (Optional) 8](#_Toc232847395)

[2.5.2 Maintain Cost Rates 8](#_Toc232847396)

[2.5.3 Maintain Financial Statement Versions 10](#_Toc232847397)

[2.5.4 Create Project Coding Mask 10](#_Toc232847398)

[2.5.5 Create Project Types for WBS Elements (Optional) 12](#_Toc232847399)

[2.5.6 Maintain Budget Availability Profile using Self Service Configuration (SSC) UI app (Optional) 14](#_Toc232847400)

[2.5.7 Manage Teams and Responsibilities for Projects (Optional) 18](#_Toc232847401)

[2.5.8 Manage Situation Types (Optional) 19](#_Toc232847402)

[3 Overview Table 22](#_Toc232847403)

[4 Test Procedures 24](#_Toc232847404)

[4.1 Create Project 24](#_Toc232847405)

[4.1.1 Create Project Using Copy Functionality (Optional) 29](#_Toc232847406)

[4.2 Project Review (Optional) 31](#_Toc232847407)

[4.3 Update Project (Optional) 31](#_Toc232847408)

[4.3.1 Mass Changes to Projects and Work Packages (Optional) 31](#_Toc232847409)

[4.4 Capture Planned Costs 32](#_Toc232847410)

[4.5 Capture Project Budget 34](#_Toc232847411)

[4.5.1 Upload Project Budget (Optional) 34](#_Toc232847412)

[4.5.2 Manage Project Budget (Optional) 36](#_Toc232847413)

[4.6 Define Demand 38](#_Toc232847414)

[4.7 Release Projects/Project Parts 39](#_Toc232847415)

[4.8 Direct Activity Allocation 40](#_Toc232847416)

[4.9 Post General Journal Entry 41](#_Toc232847417)

[4.10 Time Recording 43](#_Toc232847418)

[4.11 Project Control Procurement 43](#_Toc232847419)

[4.12 Monitor Projects 44](#_Toc232847420)

[4.12.1 Monitor Notification (Optional) 44](#_Toc232847421)

[4.12.2 Monitor Projects via Project Financial Controller Overview 45](#_Toc232847422)

[4.12.3 Monitor Projects via Monitor Projects App 46](#_Toc232847423)

[4.12.4 Monitor Projects via Project Cost Report 47](#_Toc232847424)

[4.12.5 Monitor Projects via Project Budget Report 48](#_Toc232847425)

[4.12.6 Monitor Projects via Manage Project Procurement 50](#_Toc232847426)

[4.12.7 Monitor Projects via P&L Plan/Actual 51](#_Toc232847427)

[4.13 Check/update Settlement Rules (Optional) 52](#_Toc232847428)

[4.13.1 Settlement Rule for Overhead Projects 52](#_Toc232847429)

[4.13.2 Settlement Rule for Investment Projects 54](#_Toc232847430)

[4.14 Period End Closing Projects (Optional) 55](#_Toc232847431)

[4.14.1 Period End Closing Projects - Apply Overhead (Optional) 55](#_Toc232847432)

[4.14.2 Period End Closing Projects – Run Settlements 56](#_Toc232847433)

[4.14.3 Period End Closing Projects- Monitor Financials 57](#_Toc232847434)

[4.15 Complete Project Parts and Project 57](#_Toc232847435)

[4.16 Close Project Parts and Project 58](#_Toc232847436)

[5 Appendix 60](#_Toc232847437)

[5.1 Process Integration 60](#_Toc232847438)

[5.1.1 Preceding Processes 60](#_Toc232847439)

[5.1.2 Succeeding Processes 60](#_Toc232847440)

## Purpose

Overview

For many purposes, companies run projects to plan and coordinate the work, staff employees, and track project progress and costs. In this scenario, a Work Breakdown Structure (WBS) as an accounting structure is created. Planned project costs (uploaded by the project financial controller) can be captured in SAP Analytics Cloud. After releasing all or part of the project, the project is executed. Time can be recorded, and project-related purchasing can be performed. In finance, allocations or general journal entries can be done with regard to project WBS elements. The project financial controller monitors the project costs through overview pages and detailed project reporting. At period end, depending on the type of project, different period-end closing activities such as overhead application or settlement can be executed for a project. Afterwards, the financial controller completes and closes project parts and then closes the complete project.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/1NT_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
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
| Activity Types | 8 | Consulting |  |
| Cost Rate | Actual and planned cost rates are maintained for the following combination of cost centers and activity types:Cost centers: 33101321, 33101101Activity types: 8 |  | Cost Rates are defined time-dependent |
| G/L Account | 61005000 | Trav. Expense – Ground transportation |  |
| 61007000 | Trav. Expense – Airfare, Rail, Mileage |  |  |
| 61003000 | Travel Expenses – Hotel and Accommodation |  |  |
| 61008000 | Travel Expenses – Miscellaneous |  |  |
| 10010000 | Petty Cash |  |  |
| Profit Center | YB600YB110 | Shared ServicesProduct A |  |
| Functional Area | YB25YB75 | Consulting/ServicesOther expenses |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 3KW | Create CO Cost Rates - MDS |
| BHD | Create Purchasing Info Record - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |
| BNI | Create Asset - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 4RF - Project Control – Resourcing and Procurement | To plan demand of consumables or services for the project, the Project Control – Resourcing and Procurement (4RF) scope item must be activated. |
| J62 - Asset AccountingAsset Accounting | To perfom the step 'Release Projects' for Investment Project, you need to execute the step 'Year End Closing' of the Asset Accounting (J62) test script to define the asset accounting specific company code settings. |
|  |  |
| BNI - Create Asset - MDS | During the execution of this scope item, asset master records will be created for assets under construction and the assets to which final settlement is performed. To create the assets, use the Create Asset - MDS (BNI) master data script using the data specified in this test script. |
| BNA - Period-End Closing – ProjectsPeriod-End Closing – Projects | To execute the settlement related activities for the project, the scope item must be activated. |
| 3F7 - Joint Venture Accounting | To execute the joint venture attributes in the project, the Joint Venture Accounting (3F7) scope item must be activated. |
| 1NJ - Responsibility Management | To enable notifications for business users with the Project Financial Controller role, you need to define teams and their responsibilities. To define teams and their responsibilities, the Responsibility Management (1NJ) scope item must be activated. |
| 31N - Situation Handling | To monitor budget threshold for the project, you need to configure the situation type using a template. To be able to do that, the Situation Handling (31N) scope item must be activated. |

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

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Project](#unique_17) [page ] 24 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project definition and WBS Elements with all the required parameters will be created. |
| [Project Review (Optional)](#unique_18) [page ] 31 | Project Financial Controller | See the test script. | See the test script. |
| [Update Project (Optional)](#unique_19) [page ] 31 | Project Financial Controller | Project Control - Enterprise Projects (F3215) and Mass Changes to Projects (F3891) | Created projects can be updated. |
| [Mass Changes to Projects and Work Packages (Optional)](#unique_20) [page ] 31 | Project Financial Controller | Mass Changes to Projects (F3891) | Multiple projects can be modified simultaneously. |
| [Capture Planned Costs](#unique_21) [page ] 32 | Project Financial Controller | Import Financial Plan Data (F1711) | Planned costs for the project WBS Element are posted |
| [Capture Project Budget](#unique_22) [page ] 34 | Project Financial Controller | Import Financial Plan Data (F1711) | Budget for the project WBS Element is posted |
| [Define Demand](#unique_23) [page ] 38 | See the test script. | See the test script. | See the test script. |
| [Release Projects/Project Parts](#unique_24) [page ] 39 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | The project status is changed to REL (Release) |
| [Direct Activity Allocation](#unique_25) [page ] 40 | Project Financial Controller | Manage Direct Activity Allocation - Deprecated (F3697) | Actual activities that occurred in relation to a WBS element are confirmed |
| [Post General Journal Entry](#unique_26) [page ] 41 | General Ledger Accountant | Post General Journal Entries (F0718) | Post actual primary costs to WBS elements |
| [Time Recording](#unique_27) [page ] 43 | See the test script. | See the test script. | See the test script. |
| [Project Control Procurement](#unique_28) [page ] 43 | See the test script. | See the test script. | See the test script. |
| [Monitor Projects](#unique_29) [page ] 44 | Project Financial Controller | Project Financial Controller Overview or Project Budget Report or Monitor Projects or P&L Plan/Actual or Project Cost Report Plan/Actual | Compare Project actual vs planned |
| [Monitor Notification (Optional)](#unique_30) [page ] 44 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Notifications triggered by situation management are displayed. |
| [Monitor Projects via Project Financial Controller Overview](#unique_31) [page ] 45 | Project Financial Controller | Project Financial Controller Overview (F3078) | The Overall Status, Planned and Active Projects, Actual costs, Cost to Date-Timeline and Upcoming Milestones are displayed. |
| [Monitor Projects via Monitor Projects App](#unique_32) [page ] 46 | Project Financial Controller | Monitor Projects (F3088) | A detailed view of the project cost, project progress is displayed in graphical form.. |
| [Monitor Projects via Project Cost Report](#unique_33) [page ] 47 | Project Financial Controller | Project Cost Report - Plan/Actual (F2513) | All plan, actual costs and their variances are displayed. |
| [Monitor Projects via Project Budget Report](#unique_34) [page ] 48 | Project Financial Controller | Project Budget Report (F3377) | The cumulative actual costs, commitments, budget planned and available budget on the project are displayed. |
| [Monitor Projects via Manage Project Procurement](#unique_35) [page ] 50 | Project Financial Controller | Manage Project Procurement (F2930) | Details of the project related to purchase order and purchase requisition, such as delivery quantity, net order value, delivery date and so on are displayed |
| [Monitor Projects via P&L Plan/Actual](#unique_36) [page ] 51 | Project Financial Controller | P&L Plan/Actual - Profit and Loss (F1710) | Variance of planned vs actual costs on the project are displayed. |
| [Check/update Settlement Rules (Optional)](#unique_37) [page ] 52 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Settlement rule is updated |
| [Period End Closing Projects (Optional)](#unique_38) [page ] 55 | See the Period-End Closing – Projects (BNA) test script. | See the Period-End Closing – Projects (BNA) test script. | See the Period-End Closing – Projects (BNA) test script. |
| [Complete Project Parts and Project](#unique_39) [page ] 57 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project Status should be changed to TECO (Technically complete) |
| [Close Project Parts and Project](#unique_40) [page ] 58 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project Status should be changed to CLSD (Closed) |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Project

Purpose

In this activity, you can create projects of the following type based on the business requirement, with the project definition and WBS element using the Fiori app Project Control - Enterprise Projects (F3215):

- Overhead Project
- Investment Project
- Project with Revenue
- Statistical Project

Overhead Projects profile is used to support the planning and monitoring of project-related costs ranging from simple, internal order such as projects to hierarchical projects accounting structures, such as R&D projects. The user can plan and post costs for the project, monitor the project, and finally close the project. Overhead projects allow the settlement of costs to different G/L accounts and costs centers based on the settlement rule created.

Investment projects profile is used in Capital Investment scenarios with the purpose of supporting companies to manage and control the enterprise-wide project related investments. Capital Investment projects are used to capture the costs of assets under construction (AuC) during the construction phase and create the final asset once this phase is completed. Capital investment Projects are mostly undertaken by asset and product centric companies.

Projects with Revenue allows revenue G/L journal entries postings after release. The profitability segment characteristics can be maintained in the settlement rule, however running the settlement is not required anymore due to the direct attribution of cost postings.

Statistical projects are used for statistical cost postings and project cost reporting purposes only. Therefore, in statistical projects, no overhead calculations or settlements can be executed. At the WBS element level, you must set the cost center to which the costs are actually posted by default.

For hierarchical project accounting requirements, you can also create a hierarchical project structure by calling up the Project Planning application from the Project Control app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215). | The Project Control screen is displayed. |  |
| 3 | Create Project: Definition | Choose Create.Make entries as shown in the following example in the Header and General Information sections:HeaderExample Project Name: Overhead ProjectProject ID: O.000001Project Profile: Overhead ProjectPlanned Start: Today (MM/dd/yyyy)Planned Finish: Today + 3 months (MM/dd/yyyy)General information:Responsible Cost Center: <Example:33101501(R&D)>Profit Center: <YB600 (Shared Services)>Project Currency: AED(Automatically filled based on the cost center)Note You can specify the currency at project level different from controlling area currency, to run project specific financial reports.Project Manager : the Project Manager IDPriority: the priority suitable for projectProject Type: Project Type created in [Create Project Types for WBS Elements (Optional)](#unique_12) [page ] 12Attachments: Choose Upload to upload project relevant documents from your local drive.Note To rename the existing attachment, choose the Edit icon present next to the attachment and change the file name according to the requirement and choose Rename.Choose Create.A success message tells you that the project is created. | Project is created with the provided definition parameters.WBS Element ID: <O.000001>Project Name: <Overhead Project> |  |
| 4 | Add Values to the Project | Once the project is created, from the header section, choose Edit.Make the following entries:General InformationPlant: 3310Functional Area: YB75 (Other expenses)ControlInvestment Profile: Example: 000001 - Model with AuC, summary settlementNote The investment profile field is relevant only for investment projects and the profile can be selected based on the business requirement.If you need settlement to multiple AuCs, select investment profile YS0001 - Model for AuC per source structure/assignment.Costing Sheet: 3310PIThe following are optional entries, maintain them according to your requirements.Budget Availability Control Profile: Select the Budget Availability Profile created using SSCUI as mentioned in Preliminary Step ([Maintain Budget Availability Profile using Self Service Configuration (SSC) UI app (Optional)](#unique_13) [page ] 14)Example ZS001Note If project currency is maintained, you can assign an availability control profile where the budget currency is maintained as Global Currency or Project CurrencyIf project currency is not maintained, you can only assign an availability control profile where the budget currency is maintained as Global Currency.Budget Availability Control Profile is Active: SelectedYou can define your own budget availability control profile using the Maintain Budget Availability Profile SSCUI.As soon as you have planned budget for your project and activated the budget availability control, the hierarchy changes are no longer possible.Note You would be able to see Joint Venture (JV) attributes under the section Joint Venture Accounting during project creation, if the Joint Venture accounting functionality has been activated in the system. For the detailed explanation on JV attributes, you can refer to the scope item 3F7-Joint Venture Accounting.Block FunctionsTime Recording: <Selected/Not Selected>Activity Allocation: <Selected/Not Selected>Purchasing: <Selected/Not Selected>Concur Expense Posting: <Selected/Not Selected>Other Expense Posting: <Selected/Not Selected>NoteSetting up the block functions at Project Header level will not impact the complete project hierarchy.The Block functions need to be set at the individual Work Package level to enable the functionality.Even if the user blocks purchasing for a WBS Element, the system can still generate purchasing documents if the account assignment category in the purchase document is "Q" (Project Make-to-Order) and the account is associated with that WBS Element.To resolve this issue, refer to the following Knowledge Base Article (KBA) note and apply the resolution mentioned in it. [https://me.sap.com/notes/3459521](https://me.sap.com/notes/3459521)Choose Save.A system message tells you that the project has been saved. | Project updates with all the provided parameters.Note In case you have entered a budget availability control profile and activated the budget availability control, all postings resulting into commitments or actual costs will be checked against the available budget of the work packages used as account assignment object. In case the work package itself does not have any budget, the next higher level budget carrying work package will be used for the budget availability check. Depending on the tolerance limits defined for the availability control profile, the system can raise warning or error messages. Depending on the Time Range defined for the availability control profile, you will be able to check the budget consumption for a particular fiscal year or across fiscal years. This setting is valid for all kind of expense postings and expected expense postings (for example, purchase requisition or purchase orders) to a work package. Warning messages from budget availability check are not shown in case of automatic periodic postings and certain goods movement. |  |
| 5 | Update settlement rule to Project. (Only Applicable for Project with Revenue) | From the header section, choose Settlement Rule.On the Maintain Settlement Rule: Overview screen, make the following entries:Cat: PSGChoose Enter.Maintain the required information and choose Continue.Choose Save and then Back. | The Program WBS_SETTLEMENT screen appears with the system message that the Settlement Rule is saved |  |
| 6 | Navigate to Project Planning | Once the project is created, from the header section, choose Related Apps. A pop-up screen appearsFrom the pop-up screen, select Project Planning to go to the Project Planning app.Note By default, the project will open in the Display mode. To edit the project, choose Edit. | The Project Planning app is opened and you can make further entries. |  |
| 7 | Create WBS Elements under Project | In the Project Structure view, select Project WBS created in the above step, and choose Create.ID: <Example: O.0000011>Name: WBS Element for project planningProfit Center: <This data is pre-populated from the first WBS level>Responsible Cost Center: <This data is pre-populated from first WBS level>Planned Start: TodayPlanned Finish: Today + 3 monthsIn the Project Structure view, select the project created in the above step, and choose Create .ID: <Example: O.0000012>Name: WBS Element for project executionProfit Center: <This data is pre-populated from the first work package level>Responsible Cost Center: <This data is pre-populated from first workpackage level>Planned Start: TodayPlanned Finish: Today + 3 monthsCreate WBS element structure based on your requirements.Note You can also create WBS Elements by making use of the Copy functionality available in the Project Planing Application.You can also include WBS Elements of another project by making use of the Include functionality available in the project planning application (while including the WBS Elements, the existing demands and settlement rules of the source WBS Element are not included). | Project with WBS Element structure is updated with the provided parameters. |  |
| 8 | Save Project Structure | Choose Save. | Project with WBS Element structure is saved |  |

|  |
| --- |
| Note By following the above procedure, you can also create projects such as the Investment Project, Project with Revenue and Statistical Project based on the business requirement by selecting the appropriate project profiles and their respective project attributes as mentioned in the following table: |

Project Attributes Overview:

| Project Name | Project ID | Project Profile | Responsible Cost Centre | Profit Center | Functional Area |
| --- | --- | --- | --- | --- | --- |
| Investment Project | I.000001 | Investment Project (YP02) | 33101301 (Manufacturing 1) | YB110 (Product A) | YB75(Other expenses) |
| Project with Revenue | R.000001 | Project with Revenue (YP05) | 33101501 (R&D) | YB600 (Shared Services) | YB25 (Consulting/Services) |
| Statistical Project | S.000001 | Statistical Project (YP04) | 33101501 (R&D) | YB600 (Shared Services) | YB75(Other expenses) |

#### Create Project Using Copy Functionality (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create an overhead project by copying the WBS element structure from the existing project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215). | The Project Control screen is displayed. |  |
| 3 | Create Project | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter [Create Project](#unique_17) [page ] 24 >Example O.000001 (for Overhead Project)Select the project displayed in the list view and choose CopyMake the following entries in the Copy Project pop-up screen:Project ID: O.000XX (For Example:O.00002)Project Name: Overhead ProjectPlanned Start: TodayORPlanned Finish: Today + 3 monthsAlso CopyDemand: <Example: Selected>Settlement Rule: <Example: Selected>Note You can choose the Demand and Settlement Rule check boxes if you would like to copy the existing demands and settlement rule from the source projectChoose CopyNote You can either maintain the Planned Start or the Planned Finish Dates, but not both of them.In the Project Overview screen, the details of the reference project is displayed. Make changes if required.Choose Save | Project is created with the provided definition parameters.WBS Element ID: O.000XXDescription: Overhead Project. |  |

### Project Review (Optional)

Purpose

In this activity, the Project Financial Controller sends a notification to the Project Manager about the project created and also reminds the Project Manager about the upcoming steering commitee meetings during the later stages of the project.

Procedure

To execute this activity, perform the steps in Project Review (1YF) test script, using the project from this document

### Update Project (Optional)

Purpose

In this activity, you can make changes to the projects based on the business requirement,using the Fiori apps Project Control and Mass Changes to Projects.

You can modify project attributes such as the Profit Center, Cost Center and Project dates/timelines for single or multiple projects by making use of the following mentioned application:

- Mass Changes to Projects

#### Mass Changes to Projects and Work Packages (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can edit the project attributes such as Profit Center, Responsible Cost Center and Project Manager for the project. You can make the changes either for a single project or multiple projects in a single instance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Mass Changes to Projects (F3891) |  |  |
| 3 | Choose Project | From the Worklist displayed, select the projects or WBS Elements created and choose Mass Change icon to carry out the changes. | The Mass Change pop-up screen appears. |  |
| 4 | Maintain Values | Make the following changesProcessing Status: <Replace Field Value>Priority: <Replace Field Value>Project Manager : <Replace Field Value>Choose Apply.Enter the description for Job Name and choose ConfirmNote The Mass change fields can be extended using extensibility.You can also make the changes to the attributes of work packages.A job is scheduled for the mass changes made. However, the changes might not appear immediately and require some time to reflect. | The Mass Change pop-up window is displayed with some project attributes.Once the changes are saved, a success message is displayed. |  |

### Capture Planned Costs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you upload planned costs to WBS elements.

|  |
| --- |
| Note You will be able to use the Analytics Cloud functionality to input planned costs to the project by using the test script for scope item [2YG](https://me.sap.com/processnavigator/SolP/2YG). |

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
| PLN | <current year>Example 2018 | <current month>Example 4 | 3310 | O.000001 | O.0000011 | 61005000 | 1000 | USD |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 4 | Import Planned Cost Data | Choose Browse. Select the CSV file from the local system which has the planned cost data already maintained for the project created above.Choose Import Source File. | The plan data has been imported successfully. |  |

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

#### Upload Project Budget (Optional)

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller .. |  |  |
| 2 | Access App | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data screen is displayed. |  |
| 3 | Download Template; Fill the planned Budget in the CSV file | Choose Download Templates. A pop-up window appears.In the pop-up window, choose , (Comma) from the Separator for .csv files dropdown and then choose Project Budgeting; the template CSV file will be downloaded to the local machine.Choose CloseAccess/open the file and fill the planned budget values.Make sure to save the file in CSV (Comma delimited) (*.csv).Note Remember the location of the files stored. | A CSV file will be saved with the budget details. |  |

Adapt the Project Planning Template

Refer the following table for sample values:

|  |
| --- |
| Note The following account is not specific for budget allocation. You can also use a different account for the posting. |

| Category | General Ledger Fiscal Year | Posting Period | Project definition | Work Breakdown Structure Element (WBS Element) | Account Number | Amount in Global Currency | Global Currency | Company Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X | X | X | X |  |  |  |  |  |
| BUDGET01 | <current year>Example: 2018 | <current month>Example: 11 | O.000001 | O.0000011 | 61005000 | 1000 | USD | 3310 |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 4 | Import Planned Budget Data | Choose Browse. Select the CSV file from the local system which already has the planned budget data maintained for the project created above.Choose Import Source File . | A system message is displayed confirming that the planned data has been imported successfully |  |

#### Manage Project Budget (Optional)

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

This activity deals with demand planning for the project.

Procedure

To execute this activity, run the step 'Define Demand' from 4RF- Project Control – Resourcing and Procurement test script to create and process your project related demands

### Release Projects/Project Parts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release the project to enable the project execution.

|  |
| --- |
| Note To use the workflow for the project release approval process, perform the steps described in Review Workflow for the Release of a Project (Optional) of the Project Review (1YF) test script, using the project from this document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215) | The Project Control screen is displayed. |  |
| 3 | Open Project | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter [Create Project](#unique_17) [page ] 24>Example O.000001 (for Overhead Project)I.000001 (for Investment Project)R.000001 (for Revenue Project)S.000001 (for Statistical Project) | At least one entry is displayed in the Worklist area. |  |
| 4 | Release project and structure | Select the project and in header section choose Processing Status > Release | Project status changed to Released.NoteFor investment projects AuCs will be created for those WBS elements with a proper investment profile assigned.You can also use the Change Processing status using the Project Briefs app in the Project Manager role.You can also change the processing status of the Work Package using the Project Planning app in the Project Financial Controller role.Project once released cannot be renamed or deleted. |  |
| 5 | Maintain actual start date in WBS Elements | Choose Related Apps > Project Planning . Choose Edit to open the project in change mode.For all created WBS elements, maintain Actual Start Date field under WBS Element Detailed Overview pageChoose Save. | Project saved with WBS elements Actual start dates. |  |

### Direct Activity Allocation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you confirm actual activities that occurred in relation to a WBS element.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Manage Direct Activity Allocation - Deprecated (F3697). | The Manage Direct Activity Allocation screen is displayed. |  |
| 3 | Enter Activity Allocation | In the Activity Allocations tab choose Create and , make the following entries:Header Information:Journal Entry Date: TodayPosting Date: TodayIn the Allocation Items area, make the following entries and press Enter:Sender Cost Center: 33101321Sender Activity Type: 8Receiver WBS Element: <Refer the respective WBS element created in the chapter Create Project >Choose Show More per Row.Quantity: 10 | A new object page appears. |  |
| 4 | Post Activity Allocation | Choose Create. | The Journal Entries section appears showing the document number. |  |

### Post General Journal Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post actual primary costs to WBS elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter General Journal Entries | On the Post General Journal Entries screen, make the following entries:Journal Entry. Date: TodayPosting Date: TodayJournal Entry Type: SACompany Code: 3310Transaction Currency: AEDIn the Line Items area, make the following entries and choose Enter:Line Item 1G/L Account: 61003000Debit: 1000Credit: 0Choose Expand All button.Tax Code: <Input Tax Code>WBS Element: <Refer the respective WBS element created in the chapter Create Project >Line Item 2G/L Account:10010000Debit: 0Credit: 1000Check that Total Balance is 0.00Choose PostCaution In case pro-rata VAT is relevant for you, please make sure you meet the prerequisites as mentioned in chapter 2. | A success message appears showing the document number. |  |
| 4 | Optional: Batch upload general Journal entries | Download Template file to local:On the Post General Journal Entries screen, choose Upload New Entry.On the Document Upload popup window. Download Template.On the Template Download screen. Make the following entries, then choose Download.Template Language: ArabicFormat: Spreadsheet (*.xlsx)Download the template file to the local and fill general journal entries according to the template.Upload Template file and batch upload general journal entries:On the Post General Journal Entries screen, choose Upload New Entry.On the Document Upload screen, choose Browse.On the popup screen, choose your local filled out template file and choose Upload File.In the upper area, system have a message: Your uploaded file has been saved as a held document UPLD: 20XX-XX-XX XX: XX: XX (XXXXXXX).Check batch upload general journal entries.Choose Post. | A success message appears showing the document number. |  |

### Time Recording

Purpose

In this activity, employee enters the time recording for WBS Element using Manage My Timesheet (F1823) application.

Procedure

To execute this activity, execute Time Recording (1Q4) test script, using the WBS Element from this document.

|  |
| --- |
| Note While creating the task, maintain the Activity Type as 11 and WBS element created in the Create Project step of this test script. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element ID | <O.0000012> | <WBS for project execution> |  |

### Project Control Procurement

Purpose

This activity deals with demand planning and consumable purchasing activities for projects.

Procedure

To execute this activity, run steps from 4RF - Project Control – Resourcing and Procurement test script to process your purchase requisitions generated from project demand.

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

In this activity, you can analyze the status, timelines, budget and costs of your project.

|  |
| --- |
| Note You will be able to access the reports such as Project Cost, Plan vs Actual, Project Budget Report and Monitor Projects directly from Project Financial Overview. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller . |  |  |
| 2 | Access App | Open Project Financial Controller Overview (F3078) |  |  |
| 3 | Enter Selection Criteria | In the Standard section, make the following entries and choose Go.Planning Category: PLN | Projects with selected planning category are displayed in the Data Analysis area. |  |
| 4 | Check Financials | Check financials and Overall status of the project using various cards | The Overall Status, Planned and Active Projects, Actual costs, Cost to Date-Timeline and Upcoming Milestones are displayed. |  |

#### Monitor Projects via Monitor Projects App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can analyze the cost and overall progress of your project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Monitor Projects (F3088) | The Monitor Projects screen is displayed. |  |
| 3 | Enter Selection Criteria | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter Create Project >Example O.000001 (for Overhead Project)I.000001 (for Investment Project)R.000001 (for Revenue Project)S.000001 (for Statistical Project)Planning Category : PLN | At least one entry is displayed in the Worklist area. |  |
| 4 | Check Financials | From the Worklist area, select the project.Choose View Costs to check project costs.Choose View Budget to check project budget.Choose Back to go to the previous screen | Project Costs and Project Budget reports of the selected project are displayed |  |
| 5 | Check Project Progress | From the Worklist area, select the project and choose Project Progress to go to the Monitor Project Progress screen which shows the project timelines.Note This would only be possible in case 1YF-Project Review is active, too. | A detailed view of project progress is displayed in graphical form. |  |

#### Monitor Projects via Project Cost Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, analyze the cost structure of your project and check planned cost.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller . |  |  |
| 2 | Access App | Open Project Cost Report - Plan/Actual (F2513) | The Project Cost screen displays. |  |
| 3 | Enter Selection Criteria | In the Standard section, make the following entries and choose Go.Project:<Refer the respective Project created in the chapter Create Project >Planning Category 1: PlanPlanning Category 2: CPM BaselineExample O.000001 (for Overhead Project)I.000001 (for Investment Project)R.000001 (for Revenue Project)S.000001 (for Statistical Project) | Details of the project structure and the corresponding planned and Actual costs as well as commitments are displayed. |  |
| 4 | Navigation to Project Cost Report - Line items; view details of different cost | Select the project in the table, and choose View Details.On Project Costs - line items screen, check financials using drilldown and filter possibilities. | All Plan and Actual costs are displayed. |  |

#### Monitor Projects via Project Budget Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can analyze your project's cost structure and check the planned budget. Depending on the budget availability profile selected during the project creation, you can view the budget consumption report for a specific fiscal year or the overall project duration.

Prerequisites

If you plan to use Project Budget, make sure that you activate the non-standard scope item Predictive Commitments Management (2I3), as it is a prerequisite for budgeting. Once activated, the commitment management ledger 0E becomes active and applicable across all company codes and countries.

|  |
| --- |
| Note You can check, review, and update the project budget profiles as described in the section Optional: Updating Project Budget Profiles under the Preliminary Steps of Predictive Commitments Management (2I3). |

Procedure

|  |
| --- |
| Caution This Project Budget Report (F3377) app doesn’t display data associated with the semantic tag PSQBUDGET. To see data related to PSQBUDGET, use the Project Cost Report - Plan/Actual (F2513) which accurately displays the project budget, project stock, actual costs, and commitments in global currency. You can manually calculate the available budget using the formula: Available Budget = Project Budget - (Project Stock Costs + Actual Costs + Commitments). |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller . | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Project Budget Report (F3377). | The Project Budget Report - Overview screen displays. |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Project : <Refer the respective project created in the Create Project section>Example O.000001 (for Overhead Project)I.000001 (for Investment Project)R.000001 (for Revenue Project)S.000001 (for Statistical Project)Planning Category: PlanFiscal Year: Current year | Details of the project structure and the corresponding planned budget display.Note The aggregated and non- aggregated costs of the selected project are displayed. In the budget report, you would see the assigned value (Commitment +Actual) and available budget (Budget-Assigned Value) based on which you can analyze the project. |  |
| 4 | Navigation to Project Budget Report - Line items; view details of different cost | Select the project in the table, and choose View Details.On the Project Budget Report - Line items screen, check the financials using drilldown and filter possibilities.Note In the Standard section, the information is shown in the Compact Filter view by default.You can also change it to Visual Filter view to get an easy understanding of overall costs of the project. This visual depiction helps the stakeholders to get an overview of the project. | All the plan, actual, and budget costs display. |  |
| 5 | Navigation to Project Budget Report- Line items: view graphical representation of different costs | In the Project Budget Report - Line items screen, once you ensure all required search fields are filled, you can see the different cost items recorded on the project as graphical representations, such as the bubble chart, bar graph and pie chart.Note You can see the details of the cost items by hovering the cursor on the graphs. | The cumulative actual costs, commitments and budget posted on the project display. |  |

#### Monitor Projects via Manage Project Procurement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can monitor the purchasing documents using the Manage Project Procurement app and check the net order value or ordered quantity for purchase order or purchase requisitions assigned to the project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Manage Project Procurement (F2930) |  |  |
| 3 | Enter Selection Criteria | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter Create Project >Example O.000001 (for Overhead Project)I.000001 (for Investment Project)R.000001 (for Revenue Project)S.000001 (for Statistical Project)Display currency : AEDPO Delivery Status : Open | Details of the project related to purchase order and purchase requisition, such as delivery quantity, net order value, delivery date and so on are displayed according to the selection and you can click on each link to get more information. |  |

#### Monitor Projects via P&L Plan/Actual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, analyze the cost structure of your project and compare actual vs planned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open P&L Plan/Actual - Profit and Loss (F1710) |  |  |
| 3 | Enter Selection Criteria | In the Standard section, make the following entries and choose Go.Ledger:0LLedger Fiscal Year: Current yearPlanning Category: PLNProject: <Refer the respective Project created in the chapter [Create Project](#unique_17) [page ] 24>Example O.000001 (for Overhead Project)I.000001 (for Investment Project)R.000001 (for Revenue Project)S.000001 (for Statistical Project) | At least one entry is shown in the Data Analysis area. |  |
| 4 | Check Financials | Check financials using drilldown and filter possibilities. | All actual costs are displayed. |  |

### Check/update Settlement Rules (Optional)

Purpose

In this activity, check the settlement rule generated or maintain settlement rules as required.

|  |
| --- |
| Note Settlement is not supported for projects with revenue and statistical projects. |

#### Settlement Rule for Overhead Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, check the settlement rule generated.

Prerequisite

Execute the step 'Period-End Process: Internal Cost Projects-Generate Settlement Rule' of the Period-End Closing – Projects (BNA) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215). |  |  |
| 3 | Open Project | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter [Create Project](#unique_17) [page ] 24>Example O.000001 (for Overhead Project) | At least one entry is displayed in the worklist area. |  |
| 4 | Open Workpackage Details | In the project list view, choose the project displayed to navigate to the detailed Overview page.From the header section, choose Related Apps. A pop-up screen appears.From the pop-up screen, select Project Planning to go to the Project Planning app.Choose the Work Package ID: <Refer the respective Work Package created in the chapter [Create Project](#unique_17) [page ] 24 > to navigate to the Work Package page. | Work Package details are shown in detailed view. |  |
| 5 | Navigate to the Settlement Rule and Check | From the Header section, choose Settlement Rule to go to maintain settlement rule overview page.Check the details of the settlement rule generated from the previous step. | Settlement rule will be generated with regard to cost centers. |  |
| 6 | Optional: Update Settlement Rule According to your Requirement. | On the Maintain Settlement Rule: Overview screen, make the following entries:Line1:Cat: CTRSettlement Receiver: 33101501%: 50.00Settlement Type: PERNO: 1Line 2:Cat: CTRSettlement Receiver: 33101501%: 50.00Settlement Type: PERNO: 2Choose Back and then choose Save. | Settlement rule would be generated with regard to cost centers. |  |

#### Settlement Rule for Investment Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

By executing this process, the periodic settlement is executed and all costs collected on the investment project will be settled to the automatically created AuC.

Procedure

|  |
| --- |
| Note Settlement rule is automatically created upon running settlement for the first time as described in the Period-End Closing – Projects (BNA) test script. For Example: All costs collected on the investment project will be settled to the automatically created AuC. |

Execute the step "Period-End Process: Assets under Construction projects > Assets under Construction Settlement of the Period-End Closing – Projects (BNA) test script

### Period End Closing Projects (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can carry out Period End Closing for the projects created in the steps mentioned earlier in this test script.

#### Period End Closing Projects - Apply Overhead (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the actual overheads calculated for the projects / Work Packages.

|  |
| --- |
| Note The application of overheads is not supported for statistical projects |

Prerequisite

The overhead calculation can be carried out only if you have maintained the costing sheet value (as described in the 'Create Project' topic of this test script)

Procedure

To execute this activity, perform the step 'Run Actual Overhead - Projects' of the Period-End Closing – Projects (BNA) test script, using the Work Package from this document.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Work Package | <O.0000012> | <WBS for project execution> |  |

#### Period End Closing Projects – Run Settlements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you execute Period End closing for projects / Work Packages.

Prerequisite

All previous process steps are completed successfully.

Procedure

To execute this activity, perform the step “Period-End Process: Internal Cost Projects -> Actual Project Settlement “ of the Period-End Closing – Projects (BNA) test script, using the Work Package from this document and for investment projects, perform the steps “Period-End Process: Asset Under Construction Projects -> Create Assets for Complete AuC Settlement, Maintain Settlement Rule for Final Settlement & Final Settlement of the Investment Project (Collective Processing) “ of the Period-End Closing – Projects (BNA) test script, using the Work Package from this document.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Work Package | <O.0000012> | WBS for project execution |  |
| Work Package | <I.0000012> | <WBS for project execution> |  |

#### Period End Closing Projects- Monitor Financials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity , you can analyze the cost structure of your project and check Plan and Actual cost.

Procedure

To execute this activity, execute Monitor projects using the Period-End Closing – Projects (BNA) test script, using the WBS Element from this document.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element | <O.0000012> | <WBS for project execution> |  |

### Complete Project Parts and Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you technically complete the project, that is, set the status to Complete. For investment projects, the final settlement gets transferred from the AuC asset to the completed asset and to the cost center as specified in the settlement rules (as specified in the Period-End Closing – Projects (BNA) test script).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215). |  |  |
| 3 | Open Project | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter 'Create Project '>Example O.000001 (for Overhead Project)I.000001 (for Investment Project)R.000001 (for Revenue Project)S.000001 (for Statistical Project) | At least one entry is displayed in the Worklist area. |  |
| 4 | Complete Project and Structure | Select the Project and in the header section choose Processing Status > Complete | Project is saved with status Completed. (The system status is set to Technically Complete) |  |

### Close Project Parts and Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you close the completed project, that is, set the project status to Close.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215) | The Project Control screen displays. |  |
| 3 | Open Project | In the Standard section, make the following entries and choose Go.Project : <Refer the respective Project created in the chapter 'Create Project '>Example O.000001 (for Overhead Project)I.000001 (for Investment Project)R.000001 (for Revenue Project)S.000001 (for Statistical Project) | At least one entry is displayed in the Worklist area. |  |
| 4 | Close project and structure | Select the Project and in header section choose Processing Status and choose Close | Project is saved with status Closed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

Complete the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| <Scope Item ID> – <Scope Item Title> | <Enter business condition.> |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BNA | Period-End Closing - Projects |

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
> Flagged while digesting this document, not verified: Internal contradiction on project coding masks: the Create Project Coding Mask note says a mask once created can be deleted if no project with the same key exists, while the step notes say that once the coding mask is created, deletion is not possible.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/period-end-closing-projects-bna-ae-test-script-sap-s-4hana-cloud-publi]]
- related-to :: [[06-management-accounting/test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud]]
- related-to :: [[06-management-accounting/test-script-project-control-research-and-development-projects-35e-ae-9]]
- related-to :: [[06-management-accounting/test-script-project-control-resourcing-and-procurement-4rf-ae-1049]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1NT_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 98,584 chars in the whole document
