---
id: 06-management-accounting/test-script-project-control-sales-4i9-ae-sap-s-4hana-cloud-public-edit
title: "Test Script: Project Control – Sales (4I9_AE), SAP S/4HANA Cloud Public Edition (4I9_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 4I9_AE: fixed-price projects with revenue, from project creation and sales order billing plan to revenue recognition and closure."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/project-control-enterprise-projects, topic/ebrr-for-projects]
aliases: [4I9_S4CLD2608_BPD_EN_AE]
keywords: ["Project Control for Finance, Capital, R&D and Sales Projects", project with revenue, fixed-price project billing, sales order billing plan, customer down payment, event-based revenue recognition, free of charge sales order, budget availability control, planned costs upload, project milestones]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4I9_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1032
topic: 06-management-accounting/project-control-enterprise-projects
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Project Control – Sales (4I9_AE), SAP S/4HANA Cloud Public Edition (4I9_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4I9_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Project Control for Finance, Capital, R&D and Sales Projects** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Project Control – Sales (4I9_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854786)

[2 Prerequisites 4](#_Toc232854787)

[2.1 System Access 4](#_Toc232854788)

[2.2 Roles 4](#_Toc232854789)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232854790)

[2.4 Business Conditions 6](#_Toc232854791)

[2.5 Preliminary Steps 7](#_Toc232854792)

[2.5.1 Maintain Financial Statement Versions 7](#_Toc232854793)

[2.5.2 Create Project Coding Mask (Optional) 7](#_Toc232854794)

[2.5.3 Create Project Types for WBS Elements (Optional) 9](#_Toc232854795)

[2.5.4 Maintain Budget Availability Profile (Optional) 11](#_Toc232854796)

[2.5.5 Manage Situation Types (Optional) 15](#_Toc232854797)

[2.5.6 Manage Teams and Responsibility for Projects (Optional) 16](#_Toc232854798)

[3 Overview Table 18](#_Toc232854799)

[4 Test Procedures 21](#_Toc232854800)

[4.1 Create Project 21](#_Toc232854801)

[4.2 Describe Project 25](#_Toc232854802)

[4.3 Upload Planned Costs and Revenues 27](#_Toc232854803)

[4.4 Define Milestones (Optional) 28](#_Toc232854804)

[4.5 Release Project 29](#_Toc232854805)

[4.6 Create Sales Order 30](#_Toc232854806)

[4.6.1 Option 1: Create Sales Orders with Billing Plan and Assign WBS Element to the Leading Sales Item 30](#_Toc232854807)

[4.6.1.1 Link Project/WBS milestones to Sales order Item (Optional) 34](#_Toc232854808)

[4.6.1.2 Change Sales Order (Remove Billing Block) 35](#_Toc232854809)

[4.6.1.3 Create Down Payment Request 35](#_Toc232854810)

[4.6.1.4 Post a Down Payment 36](#_Toc232854811)

[4.6.1.5 Create Delivery 36](#_Toc232854812)

[4.6.1.6 Execute Picking 37](#_Toc232854813)

[4.6.1.7 Post Goods Issue 37](#_Toc232854814)

[4.6.1.8 Check Event Based Revenue Recognition – Project Accounted Sales 38](#_Toc232854815)

[4.6.1.9 Change Sales Order (Remove Billing Block) 39](#_Toc232854816)

[4.6.1.10 Automatic Remove Billing Block for Invoice 39](#_Toc232854817)

[4.6.1.11 Billing 40](#_Toc232854818)

[4.6.1.12 Check Event Based Revenue Recognition – Project Accounted Sales 41](#_Toc232854819)

[4.6.1.13 Accounts Receivable 42](#_Toc232854820)

[4.6.2 Option 2: Create Sales Order with Free of Charge Item and Assign Billing or Non-Billing WBS Element 42](#_Toc232854821)

[4.6.2.1 Create Delivery 44](#_Toc232854822)

[4.6.2.2 Execute Picking 45](#_Toc232854823)

[4.6.2.3 Post Goods Issue 45](#_Toc232854824)

[4.6.2.4 Create Invoice 46](#_Toc232854825)

[4.7 Time Recording 46](#_Toc232854826)

[4.8 Complete Milestone 47](#_Toc232854827)

[4.9 Monitor Projects 48](#_Toc232854828)

[4.9.1 Monitor Projects via Project Financial Controller Overview 48](#_Toc232854829)

[4.9.2 Monitor Projects via Monitor Projects App 49](#_Toc232854830)

[4.9.3 Monitor Projects via Project Cost Report 50](#_Toc232854831)

[4.9.4 Project Financial Booklet - Enterprise Projects 51](#_Toc232854832)

[4.9.5 Monitor Projects via P&L Plan/Actual 52](#_Toc232854833)

[4.10 Close Project 53](#_Toc232854834)

[5 Appendix 55](#_Toc232854835)

[5.1 Process Integration 55](#_Toc232854836)

[5.1.1 Succeeding Processes 55](#_Toc232854837)

## Purpose

Overview

As a core ERP functionality, project integration with sales orders enables the direct flow of revenues to the project. The margin can be easily analyzed along with the incurred costs. This scenario covers the fixed-price project billing with the possibility of a down-payment and billing plan. Using the Projects with Revenue profile, the user can create a hierarchy as an accounting structure, set up billing elements, and plan costs and revenues. As soon as the project is released, actual costs and revenues are captured, allowing the project profitability to be analyzed. At the same time, the revenue is recognized with each cost posting. At the period end, no settlement run is necessary as the postings already have the CO-PA characteristics maintained in the settlement rule or derived from the sales order.

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
| Project Manager | SAP_BR_PROJECTMANAGER | Project Management | SAP_BR_PROJECTMANAGER |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Shipping Specialist | SAP_BR_SHIPPING_SPECIALIST | Shipping | SAP_BR_SHIPPING_SPECIALIST |  |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

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
| Cost Center | 3310150133101321 | R&D Cost centerServices/Consltg |  |
| Costing Sheet | 3310PI | Costing Sheet-PS Projects |  |
| Activity Types | 8 | Consulting |  |
| G/L Account | 6100500061007000610030006100800010010000440020004100000041000400 | Trav. Expense - Ground transportationTrav. Expense - Airfare, Rail, MileageTravel Expenses - Hotel and AccommodationTravel Expenses - MiscellaneousPetty CashSales Discounts - DomesticRev Domestic ProdSales Revenue w/ Cost Element |  |
| Profit Center | YB600 | Shared Services |  |
| Functional Area | YB25 | Consulting/Services |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BKJ - Sales Order Processing with Customer Down Payment | To execute the sales order related activities for the project, the scope item must be activated. |
| BDA - Free of Charge Delivery | To execute the sales order for free goods related activities for the project, the scope item must be activated. |
| J59 - Accounts Receivable | To manage the open receivable invoices that are automatically created from the sales processes for the project, the scope item must be activated. |
| 4GQ - Event-Based Revenue Recognition – Project-Based Sales | To execute the Revenue Recognition for Project based sales, the 4GQ- Event-Based Revenue Recognition – Project-Based Sales scope item must be activated. |
| 31Q - Sales Order Processing for Sales Kits | To execute the event based revenue recognition for project based sales,the 31Q- Sales Order Processing for Sales Kits scope item must be activated |

### Preliminary Steps

#### Maintain Financial Statement Versions

Procedure

To execute this activity, run the preliminary step Maintain Financial Statement Versions from the BNA - Period-End Closing - Projects test script.

#### Create Project Coding Mask (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create the coding mask for the project structure. The coding mask applies to the external identification of project definitions as well as WBS elements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as aConfiguration Expert - Business Process Configuration |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Navigate to configuration activity | Choose the link Configure Your Solution.Make the following entries:Application Area: Enterprise Portfolio & Project ManagementSub Application Area: Project Financials ControlClick the line item displayed in the Configuration Items sectionSelect Define Project Coding Mask and choose Configure | The Change View "Project Number Editing': Overview screen is displayed. |  |
| 4 | Create a Coding Mask Entry | Perform the following actions to create the coding mask:Choose New EntriesEnter the following details:PrjID: ACoding mask: /XXXXXX-00Description: Test Coding Mask for Key ALock: <Select/Deselect>Choose Save.This step is optional.Once the coding mask is created, deletion is not possible.You cannot create commercial or internal projects in the project services processes, namely:Customer Project Management (J11)Internal Project Management (1A8)that begins with any coding key defined for coding masks. | Project Coding Mask will be saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Navigate to configuration activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Create a Project Coding Mask.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Project Number Editing": Overview screen is displayed. |  |
| 3 | Create a Coding Mask Entry | Perform the following actions to create the coding mask:Choose New EntriesEnter the following details:PrjID: ACoding mask: /XXXXXX-00Description: Test Coding Mask for Key ALck: <Select/Deselect>Choose Save.This step is optional.Once the coding mask is created, deletion is not possible.You cannot create commercial or internal projects in the project services processes, namely:Customer Project Management (J11)Internal Project Management (1A8)that begins with any coding key defined for coding masks. | Project Coding Mask will be saved. |  |

#### Create Project Types for WBS Elements (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Project Type is generally used to group or classify projects, it is primarily used for the reporting.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the Fiori Launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). | The Manage Your Solution screen is displayed. |  |
| 3 | Navigate to configuration activity | Choose the link Configure your solution.Make the following entriesApplication Area: Enterprise Portfolio & Project ManagementSub Application Area: Project Financials ControlClick on the line item displayed in the worklist sectionSelect Create Project Types for WBS Elements and choose Configure | The Create Project Types for WBS Elements app is displayed. |  |
| 4 | Create a Project Type | Perform the following actions to create the project type:Choose New EntriesEnter the details as mentioned in the following example :Typ: RDDescription: RD ProjectsChoose Save. | Project Type is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Navigate to configuration activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Create Project Types for WBS Eleements.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Create Project Types for WBS Elements screen is displayed. |  |
| 3 | Create a Project Type | Perform the following actions to create the project type:Choose New EntriesEnter the details as mentioned in the following example :Typ: RDDescription: RD ProjectsChoose Save. | Project Type is saved. |  |

#### Maintain Budget Availability Profile (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Maintain Budget Availability Profile app is used to create the Budget Availability control profile.

Prerequisites

If you intend to use Project Budget, make sure that you activate the non-standard scope item Commitment Management (2I3) which is a prerequisite for budgeting. Once activated, commitment management ledger 0E is active and applicable for all company codes and countries/regions. These commitments are updated in Extension Ledger 0E (predelivered) in ACDOCA table. Commitments are reduced by various business transactions such as goods receipt. The default content for Project Budgeting utilizes profiles PS001 and you can either update this profile or create your own profile via configuration activity Maintain Budget Availability Control Profile for Projects.

Ensure that you perform the Preliminary Steps of this document to update the following:

- Maintain Financial statement YPS2
- Tag ACT_COST which is mandatory for G/Ls relevant for Budget check. Note that currently Commitment/Budget do not work for Purchase order without material.
- Maintain Financial Statement Versions (FSV)
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
| 3 | Navigate to configuration activity | Choose the link Configure your solution.Make the following entries:Application Area: FinanceSub Application Area: Overhead Cost ManagementClick on the line item Budget Management displayed in the list.Select Maintain Budget Availability Control Profile for Projects and choose Configure. | The Maintain Budget Availability Profile app is displayed. |  |
| 4 | Create an Availability Control Profile Entry | Perform the following actions to create the availability control profile:Choose New EntriesEnter the details as shown in the following example:Profile: ZS001Availy Ctrl Type: Project SystemBudget Availy Ctrl: Profile Name : Default Bdgt Availability prflTime Range: Annual Budget / Overall BudgetBudget Currency: Global Currency/Project CurrencyPress Enter.Overall Budget needs to be selected if you want to perform the budget check across Fiscal years whereas Annual Budget needs to be selected if you want to perform the check per Fiscal year.Gobal Currency needs to be selected if you want to calculate the financials at controlling area level whereas Project Currency needs to be selected if you want to check financials at project level.For this newly created Availability Control Profile, maintain the Semantic Tags and Tolerance Limits.Select the AVC profile and choose Semantic Tags and maintain entries as shown in the following example:Choose New EntriesSem. Tag: ACT_COSTSemantic Tag Name: Actual Cost% of Budget used Before First Notification: 80%% Increment for Further Notifications: 5%Press Enter.Select the Semantic tag and choose Tolerance Limits and maintain entries as shown in the following example:Choose New EntriesActy Grp: All Activity GroupsMsgType: Warning/Error%: 90.00Press Enter.Choose Save. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Navigate to configuration activity | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Maintain Budget Availability Control Profile for Projects.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Budget Availability Profile screen is displayed. |  |
| 3 | Create an Availability Control Profile Entry | Perform the following actions to create the availability control profile:Choose New EntriesEnter the details as shown in the following example:Profile: ZS001Availy Ctrl Type: Project SystemBudget Availy Ctrl: Profile Name : Default Bdgt Availability prflTime Range: Annual Budget / Overall BudgetBudget Currency: Global Currency/Project CurrencyPress Enter.Overall Budget needs to be selected if you want to perform the budget check across Fiscal years whereas Annual Budget needs to be selected if you want to perform the check per Fiscal year.Gobal Currency needs to be selected if you want to calculate the financials at controlling area level whereas Project Currency needs to be selected if you want to check financials at project level.For this newly created Availability Control Profile, maintain the Semantic Tags and Tolerance Limits.Select the AVC profile and choose Semantic Tags and maintain entries as shown in the following example:Choose New EntriesSem. Tag: ACT_COSTSemantic Tag Name: Actual Cost% of Budget used Before First Notification: 80%% Increment for Further Notifications: 5%Press Enter.Select the Semantic tag and choose Tolerance Limits and maintain entries as shown in the following example:Choose New EntriesActy Grp: All Activity GroupsMsgType: Warning/Error%: 90.00Press Enter.Choose Save. |  |  |

|  |
| --- |
| Note In a real business scenario, projects sometimes run overbudget. With the automatic loss handling feature, event-based revenue recognition calculates the amount needed for loss provision and the necessary adjustments to the loss provision automatically with period-end closing. Refer to Maintain Settings for Event-Based Revenue Recognition under Preliminary Steps in the scope item 4GQ - Event-Based Revenue Recognition – Project-Based Sales. |

#### Manage Situation Types (Optional)

Purpose

In this procedure, you configure the situation type by using template.

Note For details on situations and the process to set up situation types, see the Setting Up Situation Handling (31N) guide.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Business Process Specialist - Business Process Configuration |  |  |
| 2 | Open Manage Situation Types | Open Manage Situation Types (F2947) app. | The Manage Situation Types screen is displayed. |  |
| 3 | Select the Template to Copy | In the Standard section, enter the ID EPPM_PROJBUDGETTHRESHOLDEXCEEDED and choose Go.Select the latest version of EPPM_PROJBUDGETTHRESHOLDEXCEEDED, then choose Copy. | The Situation Type screen is displayed. |  |
| 4 | Maintain the Situation | Make the following entries and choose Save:Admin InformationID: <ID Name>Name: <ID Description>ID: Z_BUDGET THRESHOLDName: Budget Consumption SituationSituation DisplayShort Description:Details:Notification:Resend Notifications: YESConditionsMaintain the values against the corresponding attributes/ filters to configure the conditions and use this function.Notification RecipientsResponsibility by teams: Choose + and maintain the team created through the 'Manage Teams and Responsibilities' app and maintain the value Project Financial Controller in the field Member Functions if necessary.Responsibility Rules: Choose + and maintain the project related users mapped/linked to the projects in the 'Project Brief' app for the roles of Project Financial Controller and Project Manager. | The situation type is maintained |  |
| 5 | Enable The Situation Type | Choose Enable, it will change from NO to YES. |  |  |

#### Manage Teams and Responsibility for Projects (Optional)

Purpose

In this procedure, you configure teams and responsibility for projects.

Note For details on the process of setting up teams and responsibility determination, see the Setting Up Responsibility Determination (1NJ) guide.

You can also define your own responsibility management (functions, teams, and responsibilities) by making use of the following SSCUIs:

- Map Function Profiles to Standard Team Category
- Classify Functions for Standard Team Category
- Map Custom Responsibility Definitions to Standard Team Category
- Define Team Types

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration |  |  |
| 2 | Access the App | Open Manage Teams and Responsibilities (F2412) .Choose Create. | The New Team screen is displyed. |  |
| 3 | Maintain the Team details | Make the following entries:On the Team Information tab:Name: Team_EPPM Description: Team of EPPMStatus:EnabledType: SEPPM_PFCOn the Team Members tab:Choose Create, and maintain the following values:Business Partner: use the search function to find the business partner of Project Financial ControllerFunctions: Project Financial Controller |  |  |
| 4 | Create the Team | Choose Create. | The team is created. |  |

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Project](#unique_14) [page ] 21 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project definition and WBS Elements with all the required parameters will be created. |
| [Describe Project](#unique_15) [page ] 25 | Project Manager | My Projects - Project Manager (F1876) | Project details and team members are added. |
| [Upload Planned Costs and Revenues](#unique_16) [page ] 27 | Project Financial Controller | Import Financial Plan Data (F1711) | Planned costs for the project WBS Element are posted. |
| [Release Project](#unique_17) [page ] 29 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | The project status is changed to REL (Release). |
| Create Sales Order |  |  |  |
| [Option 1: Create Sales Orders with Billing Plan and Assign WBS Element to the Leading Sales Item](#unique_18) [page ] 30 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Change Sales Order (Remove Billing Block)](#unique_19) [page ] 35 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Create Down Payment Request](#unique_20) [page ] 35 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Post a Down Payment](#unique_21) [page ] 36 | Accounts Receivable Accountant | Post Incoming Payments (F1345) |  |
| [Create Delivery](#unique_22) [page ] 36 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Execute Picking](#unique_23) [page ] 37 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Post Goods Issue](#unique_24) [page ] 37 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Check Event Based Revenue Recognition – Project Accounted Sales](#unique_25) [page ] 38 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Change Sales Order (Remove Billing Block)](#unique_26) [page ] 39 | Internal Sales Representative | Manage Sales Orders (F1873) |  |
| [Billing](#unique_27) [page ] 40 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Check Event Based Revenue Recognition – Project Accounted Sales](#unique_28) [page ] 41 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Accounts Receivable](#unique_29) [page ] 42 | Accounts Receivable Accountant | Accounts Receivable Overview (F3242) |  |
| [Option 2: Create Sales Order with Free of Charge Item and Assign Billing or Non-Billing WBS Element](#unique_30) [page ] 42 | Internal Sales Representative | Manage Sales Orders Without Charge (F2305) |  |
| [Create Delivery](#unique_31) [page ] 44 | Shipping Specialist | Create Outbound Deliveries - From Sales Orders (F0869A) |  |
| [Execute Picking](#unique_32) [page ] 45 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Post Goods Issue](#unique_33) [page ] 45 | Shipping Specialist | Manage Outbound Deliveries - VL06O (VL06O_CLOUD) |  |
| [Create Invoice](#unique_34) [page ] 46 | Billing Clerk | Create Billing Documents (F0798) |  |
| [Time Recording](#unique_35) [page ] 46 | See the test script. | See the test script. | See the test script. |
| [Complete Milestone](#unique_36) [page ] 47 | Project Manager | My Projects - Project Manager (F1876) |  |
| [Monitor Projects](#unique_37) [page ] 48 | Project Financial Controller | Project Financial Controller Overview (F3078) or Project Budget Report (F3377) or Monitor Projects (F3088) or P&L Plan/Actual - Profit and Loss (F1710) or Project Cost Report - Plan/Actual (F2513) | Compare project actual vs planned. |
| [Monitor Projects via Project Financial Controller Overview](#unique_38) [page ] 48 | Project Financial Controller | Project Financial Controller Overview (F3078) | The Overall Status, Planned and Active Projects, Actual costs, Cost to Date-Timeline and Upcoming Milestones are dis-played. |
| [Monitor Projects via Monitor Projects App](#unique_39) [page ] 49 | Project Financial Controller | Monitor Projects (F3088) | A detailed view of the project cost, project progress is dis-played in graphical form. |
| [Monitor Projects via Project Cost Report](#unique_40) [page ] 50 | Project Financial Controller | Project Cost Report - Plan/Actual (F2513) | All plan, actual costs, and their variances are displayed. |
| [Monitor Projects via P&L Plan/Actual](#unique_41) [page ] 52 | Project Financial Controller | P&L Plan/Actual - Profit and Loss (F1710) | Variance of planned vs actual costs on the project is displayed. |
| [Close Project](#unique_42) [page ] 53 | Project Financial Controller | Project Control - Enterprise Projects (F3215) | Project Status is changed to CLSD (Closed). |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Project

Purpose

In this activity, you can create a project with revenue with the project definition and WBS element using the Project Control - Enterprise Projects (F3215) app.

Projects with Revenue allow revenue G/L journal entries postings after release. The profitability segment characteristics can be maintained in the settlement rule, however running the settlement isn’t required anymore due to the direct attribution of cost postings.

For hierarchical project accounting requirements, you can also create a hierarchical project structure by calling up the Project Planning application from the Project Control - Enterprise Projects (F3215) app.

|  |
| --- |
| Note For extended project management capabilities like project scheduling, please refer to the scope item Collaborative Project Management (6JN ) |

Procedure

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Control - Enterprise Projects (F3215). | The Project Control screen is displayed. |  |
| 3 | Create Project: Definition | Choose Create.Make entries as shown in the following example in the Header and General Information sections:HeaderProject Name: Project with RevenueProject ID: R.000001Project Profile: Project with RevenueMultiple Sales Order Item Scenario: SelectedNote By selecting this check box, you can assign more than one billing relevant sales order item to the same billing work package.Choose the right setting on the project before the first save. After the first save, this decision cannot be changed.The setting done on the project level would be valid for all the billing work packages in that project.Sales order items having different revenue recognition keys cannot be assigned to the same billing work package.In case the Multiple Sales Order Item Scenario is NOT selected, the profitability characteristics are automatically derived based on the sales order and sales order item. In case the Multiple Sales Order Item Scenario is selected, the profitability characteristics must be defined by the user in the Settlement Rule.Planned Start: Today (MM/dd/yyyy)Planned Finish: Today + 3 months (MM/dd/yyyy)General information:Responsible Cost Center: 33101501 (R&D Cost center) (for example)Profit Center: YB600 (Shared Services)Project Currency: AED(Automatically filled based on the cost center)Note You can specify the currency at project level different from controlling area currency, to run project- specific financial reports.Project Manager: the Project Manager IDPriority: the priority suitable for projectProject Type: Project Type created in [Create Project Types for WBS Elements (Optional)](#unique_9) [page ] 9Attachments: Choose + to upload project relevant documents from your local drive.Note To rename the existing attachment, choose the Edit icon present next to the attachment and change the file name according to the requirement and choose Rename.Choose Create.The project is saved and a confirmation message is displayed. | Project is created with the provided definition parameters.One WBS Element with details as shown in the following example will be created under the project:WBS Element ID: R.000001Project Name: Project with Revenue |  |
| 4 | Add Values to the Project Summary Task WBS Element | Once the project is created, from the header section, choose Edit.Make the following entries:General InformationPlant: 3310Functional Area: YB25 (Consulting/Services)ControlCosting Sheet: 3310PIThe following are optional entries, maintain them according to your requirements.Budget Availability Control Profile: ZS001If project currency is maintained, you can assign a budget availability control profile where the budget currency is maintained as Global Currency or Project Currency.If project currency is not maintained, you can only assign an availability control profile where the budget currency is maintained as Global Currency.Budget Availability Control Profile is active: SelectedAs soon as you have selected and used a Budget Avability Control Profile, a budget needs to be uploaded.You can define your own budget availability control profile using the Maintain Budget Availability Profile SSCUI.As soon as you have planned budget for your project and activated the budget availability control, the hierarchy changes are no longer possible.Block FunctionsTime Recording: <Selected/Not Selected>Activity Allocation: <Selected/Not Selected>Purchasing: <Selected/Not Selected>Concur Expense Posting: <Selected/Not Selected>Other Expense Posting: <Selected/Not Selected>Setting up the block functions at Project Header level will not impact the complete project hierarchy.The Block functions need to be set at the individual Work Package level to enable the functionalityEven if the user blocks purchasing for a WBS Element, the system can still generate purchasing documents if the account assignment category in the purchase document is "Q" (Project Make-to-Order) and the account is associated with that WBS Element.To resolve this issue, refer to the following Knowledge Base Article (KBA) note and apply the resolution mentioned in it.[https://me.sap.com/notes/3459521](https://me.sap.com/notes/3459521)Choose Save.A system message tells you that the project has been savedNote In case you have entered a budget availability control profile and activated the budget availability control, all the postings resulting into commitments or actual costs will be checked against the available budget of the WBS element used as account assignment object.In case the WBS element does not have any budget, the next higher level budget carrying WBS element will be used for the budget availability check.Depending on the tolerance limits defined for the availability control profile, the system can raise warning or error messages.Depending on the Time Range defined for the availability control profile, you will be able to check the budget consumption for a particular fiscal year or across fiscal years. This setting is valid for all kind of expense postings and expected expense postings (for example, purchase requisition or purchase orders) to a WBS element.Warning messages from budget availability check are not shown in case of automatic periodic postings and certain goods movement. | WBS Element updates with all the provided parameters. |  |
| 6 | Navigate to Project Planning | Once the project is created, from the header section, choose Related Apps. A pop-up screen appearsFrom the pop-up screen, select Project Planning to go to the Project Planning app.Note By default, the project will open in the Display mode. To edit the project, choose Edit. | The Project Planning app is opened and you can make further entries. |  |
| 7 | Create WBS Packages under Project Summary Task WBS Element | In the Project Structure view, select WBS Element created in the above step, and choose Create.Make the following entries in the Details screen onto the right.ID: <Example: R.0000011>Name: WBS for project planningProfit Center: <This data is pre-populated from the first WBS level>Responsible Cost Center: <This data is pre-populated from first WBS level>Planned Start: TodayPlanned Finish: Today + 3 monthsIn the Project Structure view, select WBS Element created in the above step, and choose Create.ID: <Example: R.0000012>Name: WBS for project executionProfit Center: <This data is pre-populated from the first WBS level>Responsible Cost Center: <This data is pre-populated from first WBS level>Planned Start: TodayPlanned Finish: Today + 3 monthsCreate work package structure based on your requirements.Note You can also create workpackage by making use of the Copy functionality available in the Project Planing ApplicationNote In the Project Planning app, the user is able to maintain multiple billing work packages by setting the Billing Element flag. In order to ensure the correct handling of CO-PA attributes, the billing work packages can not be in the same sub-structure, meaning that it is not allowed to have one billing element under another billing element in the structure. Also, the work packages that are under a billing element must have the same company code, profit center and functional area to ensure the same profitability segment postings. | Project with WBS Element structure is updated with the provided parameters. |  |
| 8 | (Optional) Assign Profitability Segment | From the header section, choose EditUnder the Control section choose the Assign button below the field Profitability SegmentOn the Assignment to Profitability Segment pop screen, make the following entries:Functional Area: YB10Plant : 1010Choose Derive and CloseNote Once the project / billing work package is account assigned to only one billing and pricing relevant sales order items (and multiple free of charge SO items), the profitability characteristics are automatically derived once the billing work package is assigned to the sales order item. In this case, the maintenance of the profitability segment is optional. However, If a profitability segment is maintained, this would have priority and the profitability characteristics for each posting would be taken from profitability segment.In case the project/ billing work package is account assigned to multiple billing and pricing relevant sales order items (and multiple free of charge SO items) it is recommended to maintain the profitability segment attributes so that postings can derive the values from the segment. In case these are not maintained, no profitability attribute would be derived. | The Project Control screen is displayed with the system message confirming that the settlement rule is saved.Note Users can maintain a profitability segments for the billing element only. The characteristics are used to attribute cost/revenue postings to the billing and lower level Work Packages. |  |
| 10 | Save Project Structure | Choose Save. | Project with WBS Element structure is saved. |  |

### Describe Project

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Manager. |  |  |
| 2 | Access My Projects (Active Projects) | Open My Projects - Project Manager (F1876) app. Choose Planned Projects to go to Project Briefs. | The Project Briefs screen appears. |  |
| 3 | Open the Project | From the Projects displayed, select the project and click to open the project. | Selected project is displayed. |  |
| 4 | Choose Edit | Choose Edit to change the project from Display to Edit mode.Note By default, the project will open in the display mode. | Project is editable. |  |
| 5 | Maintain Priority and Project Type | Select the priority and project type suitable for the project from the drop-down option list. |  |  |
| 6 | Define Milestones | From the Milestones tab, click Create to add the list of relevant milestones. | All the milestones are saved and displayed. |  |
| 7 | Maintain the Planned Finish Dates for the Milestones | For each milestone, select the Planned Finish date. | Planned Finish dates for the milestone are maintained. |  |
| 8 | Define Team | Scroll down to the Team section and choose + to maintain the names of steering committee team members, project financial controller and team members with relevant roles.Note The assigned team members will be able to find the WBS elements of Projects assigned in the search box of the Time Recording app and create tasks with those WBS elements and record their time according to the steps mentioned in the Time Recording (1Q4) test script.Choose Create. | Team member details are maintained |  |

### Upload Planned Costs and Revenues

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
| Note You will be able to use the Analytics Cloud functionality to input planned costs to the project by using the test script for scope item [2YG](https://me.sap.com/processnavigator/SolP/2YG).If Project Budget Profile is selected and used, upload a budget using the planning template (see Adapt the Project Planning Template section below) and planning category BUDGET01. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open the Import Financial Plan Data (F1711) app. | The Import Financial Plan Data screen is displayed. |  |
| 3 | Download Template; Fill the planned costs in the CSV file | Choose Download Templates. A pop-up window appears.In the pop-up window, choose , (Comma) from the Separator for .csv files dropdown and then choose Project Planning; the template CSV file will be downloaded to the local machine.Choose Close.Access the file and fill the plan values.Make sure to save the file in CSV (Comma delimited) (*.csv) format.Note Remember the location of the file stored. | CSV file is saved with the plan costs. |  |

Adapt the Project Planning Template

A template table is provided for your reference with sample values as follows:

| Category | General Ledger Fiscal Year | Posting Period | Company Code | Project Definition | Work Breakdown Structure Element (WBS Element) | Account Number | Amount in Global Currency | Global Currency |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X | X | X | X | X |  |  |  |  |
| PLN | <current year>Example 2020 | <current month>Example 2 | 3310 | R.000001 | R.000001 | 41000400 | -2000 | USD |
| PLN | <current year>Example 2020 | <current month>Example 2 | 3310 | R.000001 | R.0000011 | 61005000 | 1000 | USD |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 4 | Import Planned Cost Data | Choose Browse. Select the CSV file from the local system which has the planned cost data already maintained for the project created above.Choose Import Source File. | The plan data has been imported successfully. |  |

### Define Milestones (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define milestones for Project/WBS element.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open the Project Control - Enterprise Projects (F3215) app. | The Project Control screen is displayed. |  |
| 3 | Open Project | In the Standard section, make the following entries, and choose Go.Project : <Refer the respective Project created in Create Project 21.R.000001 (for Revenue Project) | At least one entry is displayed in the Worklist area. |  |
| 4 | Open the Project | From the Projects displayed, select the project and click to open the project. | Selected project is displayed. |  |
| 5 | Open Project in Project Briefs App | Choose the Related Apps icon and from the drop-down menu, select Project Briefs to navigate to the Project page.Note By default project will open in display mode | The Project Planning screen is displayed. |  |
| 6 | Define Milestones | Choose Edit to change the project from Display to Edit mode.From the Milestones tab, choose Create to add the list of relevant milestonesMilestone Name 1: Down Payment (for Project/WBS Down Payment) (for example)Milestone Name 2 : Invoice (for Project/WBS Invoice) (for example)Milestone Name 3 : Closure (for Project/WBS Closure) (for example) | All the milestones are saved and displayed |  |

### Release Project

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
| 2 | Access App | Open the Project Control - Enterprise Projects (F3215) app. | The Project Control screen is displayed. |  |
| 3 | Open Project | In the Standard section, make the following entries, and choose Go.Project : <Refer the respective Project created in [Create Project](#unique_14) [page ] 21.R.000001 (for Revenue Project). | At least one entry is displayed in the Worklist area. |  |
| 4 | Release project and structure | Select the project and in header section choose Processing Status > Release. | Project status is changed to Released.You can also use the Change Processing Status option in the Project Briefs app in a Project Manager role.Project once released cannot be renamed or deleted. |  |
| 5 | Maintain actual start date in WBS Elements | Choose Related Apps > Project Planning. Choose Edit to open the project in change mode.For all the created WBS elements, maintain the Actual Start Date field in the Project Structure View page.Choose Save. | Project is saved with WBS elements Actual start dates. |  |

### Create Sales Order

#### Option 1: Create Sales Orders with Billing Plan and Assign WBS Element to the Leading Sales Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create a sales order with a sales order item that has a billing plan, where the first item is a down-payment. The sales order item has the project created before as account assignment.

Procedure

To execute this activity, perform he following steps. For more information, refer Create Sales Orders with Billing Plan step in the Sales Order Processing with Customer Down Payment (BKJ) test script.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen displays. |  |
| 3 | Navigate to Create Sales Order Screen | On Manage Sales Orders screen, choose Create and select Create Sales Order - VA01. | The Create Sales Documents: Initial screen displays. |  |
| 4 | Enter Sales Document Type | Make the following entries:Order Type: <sales order type>, for example, OR (Standard Order)Organizational DataSales organization: 3310Distribution channel: 10Division: 00Choose Enter. | The Create Standard Order xxx: Overview screen displays. |  |
| 5 | Enter Customer Number | Make the following entries:Sold-To Party: 33100004Cust. Reference: <Reference>Cust. Ref. Date: <Date>Choose Enter. |  |  |
| 6 | Enter Order Details | Make the following entries:Order Reason: <Order Reason>Material: <material number>Order Quantity: <quantity>, for example, 10Item Category:CBAO : Milestone billing plan for Trading goods, for example, TG0012.CTAD: Milestone billing plan service for Service material SM0001.CTAX: Milestone billing plan non-stock for Non-stock material NS0002.CBTC: Configuration at material levelCBTD: Configuration milestone billing planTAN: Standard itemTAD: Standard Service ItemTAX: Standard Non-StockCBTA: Standard Make-to-OrderCB1 : Third Party items with Shipping Notification (3rd Party with SN)CB2 : Third Party items without Shipping Notification (3rd Party w/o SN)CB1C : Third Party variant configuration with shipping configurationCB2C : Third Party variant configuration without shipping configurationCBAB : Bought-In Item (Bought-In Item)DB1 : Milestone Billing Plan with Shipping Notification (MilstBillPl 3Pw/ASN)DB2 : Milestone Billing Plan without Shipping Notification (MilstBillPl 3Pw/oASN)DBAB : Milestone Billing Plan with bought-in Items (MilstBillPl OrdSProc)CBTQ : Pricing header milestone billing planTAQ : Pricing at Header LevelNote A service product SM0001 is used in the sales order. It allows the sales of services without delivery and direct order-related billing. You may skip the steps from [Create Delivery](#unique_22) [page ] 36 to [Post Goods Issue](#unique_24) [page ] 37.Batch: <batch number> This step is optional.Note The billing of this business process is order-related. This means that the down payment request and the final invoice only contain the information that is available from the sales order like material, quantity, and batch number. If you need a batch number on the down payment request and the final invoice you must enter it in the sales order.Choose Enter. |  |  |
| 7 | Choose WBS Element | Select the item. Choose More > Goto > Item > Account Assignment .Note Alternatively, you can assign Account Assignment on header level: Choose More > Goto > Header > Account Assignment .WBS Element: <Example: R.000001>Profit Center: < Automatically picked from WBS Element. For example, YB600>NoteIf the multiple sales order items is not selected during project creation, only one billing and pricing relevant item (Item categories CBAO, CTAD, CTAX, CBTC, CBTD, TAN) can be assigned to one billing work package. However, for the same billing work package, additionally, multiple free of charge sales order items can be account assigned.. |  |  |
| 8 | Choose Billing Plan | Select the item. Choose Menu > Goto > Item > Billing plan .Note Alternatively, you can assign billing plan on header level: Choose More > Goto > Header > Billing Plan . The header billing plan will be applied to all items with item category CBAO, CTAD, or CTAX. The amount is proportionally to the value of the item participating in the down payment process distributed to the items. |  |  |
| 9 | Enter Details | For the first line item, Down Payment, make the following entries for the advance payment:Billing Date: <billing date>. For example, enter today's date.Bill Value: <amount of billing>. For example: Down Payment amount.Date category (DCat): 04 |  |  |
| 10 | Enter Details | For the second line item (Closing Invoice), make the following entries for the advance payment:Billing Date: <billing date>. For example, enter today's date.Date category(DCat): 02 |  |  |
| 11 | Enter | Choose Enter. Confirm system messages with enter, if necessary. | Closing invoice related data is determined. For example, in the Bill value field, the amount of billing is calculated by the system. |  |
| 12 | Save Sales Order | Choose Back.Choose Save and save your entries. |  |  |

##### Link Project/WBS milestones to Sales order Item (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, we link the milestones of the Project/WBS created with a sales order item that has a billing plan.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative . | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders (F1873) screen displays. |  |
| 3 | Search For Sales Order | Enter search term(s) in filter bar and choose Go; for example, enter sales order number in Sales Order field. | Sales order displays in result list. |  |
| 4 | Navigate to Sales Order Screen | Open the sales order number via Manage Sales Order - Version 2 app and click on edit button. Please click on the items tab and expand it to navigate to the dates section. | The Change Sales Order xxx: Overview screen displays. |  |
| 5 | Choose Billing Plan | Select the line item. From the menu, choose Menu > Goto > Item > Billing plan .Note Alternatively, If you assign billing plan on header level: Choose Menu > Goto > Header > Billing Plan . Removal of billing block on header level also unlocks items automatically. | The Change Standard Order xxx: Item Data screen displays. |  |
| 6 | Link Project/WBS Milestones | In the Dates section, in select button Create from Milestones A pop-up window appears.In the Create Billing Plan Dates from Project Milestones pop-up window, select , milestones relevant for attaching to the billing plan. |  |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Save | Save your entries. | The billing block is removed. |  |

##### Change Sales Order (Remove Billing Block)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove billing block from a sales order.

Procedure

To execute this activity, execute the Change Sales Order (Remove Billing Block) step from the Sales Order Processing with Customer Down Payment (BKJ) test script.

##### Create Down Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a down payment request.

Procedure

To execute this activity, execute the Create Down Payment Request step from the Sales Order Processing with Customer Down Payment (BKJ) test script

##### Post a Down Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post a down payment.

Procedure

To execute this activity, execute the Post a Down Payment step from the Sales Order Processing with Customer Down Payment (BKJ) test script

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a delivery.

Prerequisite

The goods receipt are posted to the individual customer’s stock.

Procedure

To execute this activity, execute the Create Delivery step from the Sales Order Processing with Customer Down Payment (BKJ) test script.

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

To execute this activity, execute the Execute Picking step from the Sales Order Processing with Customer Down Payment (BKJ) test script.

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

To execute this activity, execute the Post Goods Issue step from the Sales Order Processing with Customer Down Payment (BKJ) test script.

##### Check Event Based Revenue Recognition – Project Accounted Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you the profitability and the recognized revenue for the project at the time of posting goods issue for deliveries from the sales order item.

Procedure

To execute this activity, execute the following steps from the 4GQ- Event-Based Revenue Recognition – Project-Based Sales test script:

1. Monitor Revenue Recognition (Event-Based): Projects
2. Run Revenue Recognition: Projects

|  |
| --- |
| Note In order to check the revenue recorded on the project, maintain the details as follows while executing the above mentioned steps:Fiscal Year Period: <enter a period in the PPP/YYYY format>Ledger: 0LCompany Code: 3310Project Definition: <R.000001> |

##### Change Sales Order (Remove Billing Block)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove billing block from a sales order.

Prerequisite

COGS must be recognized. To recognize revenue in the same month to keep FI and PA in sync, the billing block must be removed manually to process the final invoice.

Procedure

To execute this activity, execute the Change Sales Order (Remove Billing Block) step from the Sales Order Processing with Customer Down Payment (BKJ) test script.

##### Automatic Remove Billing Block for Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to remove billing block from a sales order second line item (Final Invoice).

Prerequisite

COGS must be recognized. To recognize revenue in the same month to keep FI and PA in sync, the billing block must be removed to process the final invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open the Project Control - Enterprise Projects (F3215) app. | The Project Control screen is displayed. |  |
| 3 | Open Project | In the Standard section, make the following entries, and choose Go.Project : <Refer the respective Project created in Create Project 21. R. 000001 (for Revenue Project). | At least one entry is displayed in the Worklist area. |  |
| 4 | Open the Project | From the Projects displayed, select the project and click to open the project | Selected project is displayed. |  |
| 5 | Open Project in Project Briefs App | Choose the Related Apps icon and from the drop-down menu, select Project Briefs to navigate to the Project page.Note By default project will open in display mode | The Project Planning screen is displayed. |  |
| 6 | Update the Actual Finish Date | Update the Actual Finish date for the Milestone linked to Invoice (815).Note Actual Date can be updated only for the released projects/work packages.Note When you set the actual finish date for a milestone that is used in a billing plan, the billing block for the relevant billing plan item is automatically removed. The entry in the Used for Billing column indicates if the milestone is used in a billing plan.Choose Save | The Actual Finish date is updated. |  |

##### Billing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to bill a customer.

Procedure

To execute this activity, execute the Billing step from the Sales Order Processing with Customer Down Payment (BKJ) test script.

##### Check Event Based Revenue Recognition – Project Accounted Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you the profitability and the recognized revenue for the project after billing the sales order item.

Procedure

To execute this activity, execute the following steps from the 4GQ- Event-Based Revenue Recognition – Project-Based Sales test script:

1. Manage Real-Time Revenue Recognition Issues
2. Run Revenue Recognition: Projects
3. Project Actual Data Reporting

|  |
| --- |
| Note In order to check the revenue recorded on the project, maintain the details as follows while executing the above mentioned steps:Fiscal Year Period: <enter a period in the PPP/YYYY format>Ledger: 0LCompany Code: 3310Project Definition: <R.000001> |

##### Accounts Receivable

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure guides you through the Accounts Receivable Overview. In this activity, you review an overview of relevant figures and statistics related to the accounts receivable process. The Accounts Receivable Overview (F3242) app offers a central point of entry and an overview of the department.

|  |
| --- |
| Note For more information, see the SAP Fiori Analytical Apps for Financial Accounting (2JB) test script. |

Procedure

To execute this activity, execute the Accounts Receivable Overview sub-step of the Invoice Management Reporting step from the Accounts Receivable (J59) test script.

#### Option 2: Create Sales Order with Free of Charge Item and Assign Billing or Non-Billing WBS Element

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a free of charge sales order.

Procedure

To execute this activity, proceed with the following steps. For more information, you can refer to the Create Sales Orders step in the Free of Charge Delivery (BDA) test script.

|  |
| --- |
| Note If you have activated the Accounts Receivable (J59) scope item in your system and if you use the TG11 material and the 33100001 customer, the Minimum quantity 1.000 PC of free goods has not been reached warning notification may be displayed. To skip the warning, choose Enter. |

| Test Step # | Test Step Name | Instructions | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Sales Orders (F1873). | The Manage Sales Orders screen is displayed. |  |
| 3 | Navigate to Create Sales Order screen | On Manage Sales Orders screen, choose Add and select Create Sales Order - VA01 | The Create Sales Documents: Initial screen is displayed. |  |
| 4 | Enter Sales Document Type | Make the following entries and choose Continue:Sales Document Type: OR (Standard Order)Sales Organization: 3310Distribution Channel: 10Division: 00 |  |  |
| 5 | Enter Customer Information | Make the following entries and choose Enter:Sold-to Party: 33100001 |  |  |
| 6 | Enter Order Details | Make the following entries:Cust. Reference: <Reference Number>Under Sales tab, enter the following entries:Order Reason: select Free of Charge Sample from the dropdown listMaterial: <Material Number>Order Quantity: <Quantity> , for example, 2Item Category::CBXN:Stock item free of chargeTAXN:Non-stock item free of chargeTADNService item free of chargeCB3: Third-Party with Shipping Notification Free of ChargeCB4: Third-Party without Shipping Notification Free of ChargeCBLN: Free of Charge ExpressCBTN: Configuration at Material Level Free of ChargeCBXB: Bought-In Free of ChargeCB3C:Variant Configuration with Shipping Notification Free of ChargeCB4C:Variant Configuration without Shipping Notification Free of Charge | Item category CBXN is determined automatically supporting transfer of costs to accounting and creation of proforma invoices. |  |
| 7 | Choose WBS Element | Select the item. Choose More > Goto > Item > Account Assignment .Note Alternatively, you can assign Account Assignment on header level: Choose More > Goto > Header > Account Assignment .WBS Element: <Example: R.000001>Note In the WBS Element field, you can assign billing or non-billing WBS element.Profit Center: <Will automatically pick from WBS Element. For example, YB600> |  |  |
| 8 | Save | Choose Save.Note Please ignore any pop-up windows. |  |  |

##### Create Delivery

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a free of charge delivery.

Procedure

To execute this activity, execute the Create Delivery step from the Free of Charge Delivery (BDA) test script.

##### Execute Picking

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The picking process involves taking goods from a storage location and staging the right quantity in a picking area where the goods are prepared for shipping. This process step shows you how to pick deliveries.

Procedure

To execute this activity, execute the Execute Picking step from the Free of Charge Delivery (BDA) test script.

##### Post Goods Issue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post goods issues for delivery.

Procedure

To execute this activity, execute the Post Goods Issue step from the Free of Charge Delivery (BDA) test script.

##### Create Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create a Pro Forma invoice with reference to delivery and how to create a F2 type of invoice with costs transferred to accounting accordingly.

Procedure

To execute this activity, execute the Create Pro Forma Invoice & Create Customer Invoice step from the Free of Charge Delivery (BDA) test script.

### Time Recording

Purpose

In this activity, employee enters the time recording for WBS Element using Manage My Timesheet (F1823) application.

Procedure

To execute this activity, you must execute the procedure in the following sub-step (which is from the Time Recording (1Q4) test script) using the WBS Element from this document: Record Actual Working Time.

|  |
| --- |
| Note While creating the task, maintain the Activity Type as 18 and use the WBS element created in the [Create Project](#unique_14) step of this test script. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| WBS Element | <R.0000012> | <WBS for project execution> |  |

### Complete Milestone

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
| 2 | Access App | Open the My Projects - Project Manager (F1876) app. Go to Project Brief Overview using the card Upcoming Milestones - Active Projects. | The Project Overview screen appears and the list of projects is displayed. |  |
| 3 | Select Project in which Milestones are to be Approved | Select the project and click to navigate to the Project Brief screen. | Details of the selected project are displayed.Selected project opens and can be updated. |  |
| 4 | Choose Edit | Choose Edit to change the project from Display to Edit mode.Note By default, the project opens in the display mode. | Selected project opens in the edit mode. |  |
| 5 | Set Milestones Status to Approved | Set Milestone Approval Status to Approved. | Milestone Approval Status is added in the Milestone section. |  |
| 6 | Update the Actual Finish Date | Update the Actual Finish Date for the approved Milestones.Note Actual Date can be updated only for the released projects.Choose Save. | The Actual Finish date is updated. |  |

### Monitor Projects

Purpose

In this activity, you can analyze the costs (planned/actual) recorded on the project using different tiles available on the Fiori launchpad. You can also check project progress and the overall status of your project.

#### Monitor Projects via Project Financial Controller Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can analyze the status, timelines, budget, and costs of your project.

|  |
| --- |
| Note You will be able to access the reports such as Project Cost, Plan versus Actual, Project Budget Report and Monitor Projects directly from Project Financial Overview. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Project Financial Controller Overview (F3078). |  |  |
| 3 | Enter Selection Criteria | In the Standard section, make the following entries and choose Go.Planning Category: PLN | Projects with selected planning category are displayed in the Data Analysis area. |  |
| 4 | Check Financials | Check financial and overall status of the project using the displayed cards. | The Overall Status, Planned and Active Projects, Actual costs, Cost to Date-Timeline and Upcoming Milestones are displayed. |  |

#### Monitor Projects via Monitor Projects App

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can analyze the cost and the overall progress of your project.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open Monitor Projects (F3088) | The Monitor Projects screen is displayed. |  |
| 3 | Enter Selection Criteria | In the Standard section, make the following entries and choose Go.Project: <Refer the respective Project created in the chapter Create Project >Example R.000001 (for Revenue Project)Planning Category : PLN | At least one entry is displayed in the Worklist area. |  |
| 4 | Check Financials | From the Worklist area, select the project.Choose View Costs to check project costs.Choose View Budget to check the project budget.Choose Back to go to the previous screen. | Project Costs and Project Budget reports of the selected project are displayed. |  |
| 5 | Check Project Progress | From the Worklist area, select the project and choose Project Progress to go to the Monitor Project Progress screen, which displays the project timelines.Note This would only be possible in case the 1YF-Project Review is active. | A detailed view of the project progress is displayed in graphical form. |  |

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
| 2 | Access App | Open the Project Cost Report - Plan/Actual (F2513) app. | The Project Cost screen displays. |  |
| 3 | Enter Selection Criteria | In the Standard section, make the following entries, and choose Go.Project: <Refer to the project created in [Create Project](#unique_14)>Planning Category 1: PlanPlanning Category 2: CPM BaselineR.000001 (for Revenue Project) | Details of the project structure and the corresponding planned, actual costs, project stock costs, and commitments are displayed. |  |
| 4 | Navigation to Project Cost Report - Line items; view details of different cost | Select the project in the table, and choose View Details.On the Project Costs - line items screen, check financials using the drill-down and filter options. | Plan and Actual costs are displayed. |  |

#### Project Financial Booklet - Enterprise Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, the review booklet applications provide a guided margin analysis and various KPIs. You can explore and drill down into your financial data, as well as reveal and understand interdependencies in a conversational style. It combines various analytic views of the project into one report.

This report covers the following:

- Enterprise Projects with Revenue (Project Control – Sales - 4I9), Project Profile: YP05-Project with Revenue
    - Project Margin Overview
    - Project Billing Element View
    - Project Assigned Orders

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Project Financial Booklet - Enterprise Projects (F3698). | The Project Financial Booklet - Enterprise Projects screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Project: <Enter your desired project name>Company Code: 1010Fiscal Year: <current year>Fiscal Period: <current period> | An overview of various metrics related to the selection criteria displays. |  |
| 4 | Select Required Project Type | Under Projects with Revenue, select one of the following options:Project Margin OverviewProject Billing Element ViewProject Budget AVCNote The Project Budget AVC functionality is only available when using the Predictive Commitments Management (2I3). |  |  |

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
| 2 | Access App | Open P&L Plan/Actual - Profit and Loss (F1710)(F1710). |  |  |
| 3 | Enter Selection Criteria | In the Standard section, make the following entries and choose Go.Ledger:0LLedger Fiscal Year: Current yearPlanning Category: PLNProject definition: <Refer the respective Project created in the chapter [Create Project](#unique_14) [page ] 21R.000001 (for Revenue Project) | At least one entry is shown in the Data Analysis area. |  |
| 4 | Check Financials | Check financials using drill-down and filter options. | All actual costs are displayed. |  |

### Close Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

|  |
| --- |
| Note All the pending down payments should be cleared before you proceed with the project closure. You can use the app Manage Customer Line Items and search for your WBS.A detailed process on clearing down payments is explained in the Accounts Receivable (J59) test script.. |

In this activity, you close the completed project, that is, you set the project processing status to Closed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller. |  |  |
| 2 | Access App | Open the Project Control - Enterprise Projects (F3215) app. | The Project Control screen displays. |  |
| 3 | Open Project | In the Standard section, make the following entries, and choose Go.Project: <Refer to the project created in the [Create Project](#unique_14) test procedure.> | At least one entry is displayed in the Worklist area. |  |
| 4 | Close project and structure | Select the Project and in the header section, choose Processing Status > Complete . Then, choose Processing Status > Close . | The project is saved with the processing status Closed. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| BNA | Period-End Closing – Projects |

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
> Flagged while digesting this document, not verified: Internal sample-data inconsistency: master data and revenue recognition checks use Company Code 3310 (plant 3310, functional area YB25, Activity Type 8), but the Project Financial Booklet step uses Company Code 1010, the profitability segment step uses Plant 1010 / Functional Area YB10, and the Time Recording note says Activity Type 18.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/period-end-closing-projects-bna-ae-test-script-sap-s-4hana-cloud-publi]]
- related-to :: [[06-management-accounting/test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud]]
- related-to :: [[06-management-accounting/test-script-project-control-finance-1nt-ae-sap-s-4hana-cloud-public-ed]]
- related-to :: [[06-management-accounting/test-script-project-control-research-and-development-projects-35e-ae-9]]
- see-also :: [[06-management-accounting/event-based-revenue-recognition-project-based-sales-4gq-ae-1024]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4I9_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 90,242 chars in the whole document
