---
id: 06-management-accounting/period-end-closing-projects-bna-ae-test-script-sap-s-4hana-cloud-publi
title: "Period-End Closing – Projects (BNA_AE) – Test Script, SAP S/4HANA Cloud Public Edition 2608 (BNA_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 (AE) test script for project period-end closing: overhead, project and AuC settlement, final settlement, reports, config prerequisites."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/project-control-enterprise-projects]
aliases: [BNA_S4CLD2608_BPD_EN_AE]
keywords: ["Project Control for Finance, Capital, R&D and Sales Projects", project period-end closing, project settlement, assets under construction, overhead calculation, settlement rules, final settlement, settlement profiles, event-based settlement, investment profiles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BNA_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1293
topic: 06-management-accounting/project-control-enterprise-projects
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Period-End Closing – Projects (BNA_AE) – Test Script, SAP S/4HANA Cloud Public Edition 2608 (BNA_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BNA_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Project Control for Finance, Capital, R&D and Sales Projects** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 02-08-26 |
| --- | --- |
|  | Period-End Closing – Projects (BNA_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc237129118)

[2 Prerequisites 4](#_Toc237129119)

[2.1 System Access 4](#_Toc237129120)

[2.2 Roles 4](#_Toc237129121)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc237129122)

[2.4 Business Conditions 6](#_Toc237129123)

[2.5 Preliminary Steps 6](#_Toc237129124)

[2.5.1 User Settings - Set Controlling Area 6](#_Toc237129125)

[2.5.2 Set Report Relevancy 7](#_Toc237129126)

[2.5.3 Maintain Financial Statement Versions 8](#_Toc237129127)

[2.5.4 Replicate Runtime Hierarchy 11](#_Toc237129128)

[2.5.5 Open Cost Accounting Period 12](#_Toc237129129)

[2.5.6 Update Overhead Rates in Costing Sheet 13](#_Toc237129130)

[2.5.7 Create and Update Allocation Structure 15](#_Toc237129131)

[2.5.8 Optional: Maintain Ledger-Specific Allocation Structures 16](#_Toc237129132)

[2.5.9 Create and Update Investment Profile 16](#_Toc237129133)

[2.5.10 Create and Update Source Structure 17](#_Toc237129134)

[2.5.11 Define Assignment of AuC Classes per Source Structure 18](#_Toc237129135)

[2.5.12 Update Settlement Profile 19](#_Toc237129136)

[2.5.13 Project Profile to Settlement Profile Mapping 20](#_Toc237129137)

[2.5.14 Optional: Posting Scheme for Intercompany Clearing 21](#_Toc237129138)

[2.5.15 Optional: Map CO Intercompany Accounts 23](#_Toc237129139)

[2.5.16 Optional: Currency Conversion Settings for Activity Allocation 24](#_Toc237129140)

[3 Overview Table 26](#_Toc237129141)

[4 Test Procedures 28](#_Toc237129142)

[4.1 Run Actual Overhead - Projects 28](#_Toc237129143)

[4.2 Period-End Process: Internal Cost Projects 29](#_Toc237129144)

[4.2.1 Generate Settlement Rule 30](#_Toc237129145)

[4.2.2 Actual Project Settlement 31](#_Toc237129146)

[4.3 Period-End Process: Assets under Construction Projects 32](#_Toc237129147)

[4.3.1 Assets under Construction Settlement 32](#_Toc237129148)

[4.3.2 Optional: Postprocess Event-Based Postings – Settlement (only relevant with Event-Based Settlement Profile) 35](#_Toc237129149)

[4.3.3 Create Assets for Complete AuC Settlement 36](#_Toc237129150)

[4.3.4 Maintain Settlement Rule for Final Settlement 36](#_Toc237129151)

[4.3.5 Optional: Generate Settlement Rule (only relevant for investment projects with pass-down option selected for settlement rule maintenance) 38](#_Toc237129152)

[4.3.6 Final Settlement of the Investment Project 39](#_Toc237129153)

[4.3.7 Asset Transactions 42](#_Toc237129154)

[4.4 Analytics 43](#_Toc237129155)

[4.4.1 Monitor Projects via Project Cost Report 43](#_Toc237129156)

[4.4.2 Monitor Projects via Project Budget Report 44](#_Toc237129157)

[4.4.3 Project Financial Booklet - Professional Services 46](#_Toc237129158)

[4.4.4 Project Financial Booklet - Enterprise Projects 48](#_Toc237129159)

[5 Appendix 50](#_Toc237129160)

[5.1 Optional: Manage Settlement Rule 50](#_Toc237129161)

## Purpose

Overview

This scope item consolidates several cost allocation and reporting functions:

- Overhead calculation: This process allocates indirect expenses associated with project execution using costing sheets to define the rules for overhead calculation.
- Cost settlement: This involves transferring costs from the project to respective cost objects like cost centers or Assets under Construction (AuC). Settlement rules specify how costs are distributed from WBS elements.
- Cost settlement for investment projects/AuC: This applies when a company creates its own assets. During the construction phase, all actual postings are assigned to an AuC. Once the asset is completed, the next project settlement run transfers the AuC asset value to the finished asset. You can settle costs to an AuC either periodically or through event-based settlement. With the event-based approach, costs are automatically settled from the investment project to the AuC with each posting made to the investment project.

Overhead accountants must ensure all project-related costs are accurately recorded in the system. Several reports support this task.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |
| Asset Accountant | SAP_BR_AA_ACCOUNTANT | Fixed Assets | SAP_BR_AA_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Operating Concern | A000 | Description, for example, Plant 1 |  |
| Controlling Area | A000 |  |  |
| Company Code | 3310 |  |  |
| Cost Center | 33101101 or 33101301 | Manufacturing 1(AE) |  |
| WBS |  |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNI | During the execution of this scope item, asset master records will be created for assets under construction and the assets to which final settlement is performed. To create the assets, use the master data script Create Asset - MDS using the data described in this test script. |
| 3KW | Create CO Cost Rates - MDS |

### Business Conditions

Before this scope item can be tested, at least one of the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1NT – Project Control – Finance or35E – Project Control – Research and Development Projects or35F – Project Control – Capital Projects | Before executing this test script, you must perform the steps from at least one of these scope items. |

### Preliminary Steps

#### User Settings - Set Controlling Area

Purpose

The controlling area must be set before you carry out the first steps in controlling.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Choose User Preferences | Choose the user icon on the top right corner of the screen, and choose Settings.Choose Default Values. | The Default Values dialog box displays. |  |
| 3 | Enter Data | On the CO Area field,enter the following value: A000.Choose Save. | Controlling area A000 is set for your user. |  |

#### Set Report Relevancy

Purpose

Report relevancy must be done when you execute any reports for the first time. If you make a subsequent change in cost center, profit center, or G/L hierarchy, perform this step again to get the latest information.

Also, you must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally, this would be created as a periodic job that would run in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Report Relevancy - Set-Based Hierarchies (F5295). | The Set Report Relevancy for Set-Based Hierarchies screen displays. |  |
| 3 | Enter Header Data | Make the following entries and choose Go:Set Class: For example,0101, for the cost center groupOrganizational Unit: A000Set Name: A000Include Subnodes: Yes |  |  |
| 4 | Mark as Report Relevant | In the Set Report Relevancy section, select the row and choose Edit. In the dialog box, make the following entries:Report Relevant: Yes |  |  |
| 5 | Save | Choose Save.Note If you are using the optional procedure Commitment Management and Cost Center Budgeting, repeat steps 1-5 with the following entries instead:Set Class: 0102Organizational Unit: YCOASet Name: YBA000_CEInclude Subnodes: <Select> | Set updated message displays. |  |

#### Maintain Financial Statement Versions

Purpose

In this activity, you maintain the financial statement (FS) version. This activity must be carried out only if you choose to add additional G/L accounts.

|  |
| --- |
| Note Please make sure the Set-up Instructions have been completed before continuing. |

|  |
| --- |
| Note You can access and use Manage Financial Statement Versions (OB58) as a General Ledger Accountant to display financial statement version data. However, changes can only be made and saved using the procedure below. |

|  |
| --- |
| Caution This test step is relevant only if the new Q2P maintenance mode for G/L accounts is switched on. In case you are not on new Q2P for G/Ls, you need to use the Manage Financial Statement Versions (OB58) app. |

It is important that all G/L accounts used for revenue/deductions in a project/product profitability must be included and mapped to the Financial Statement Version YPS2 and tagged to a single respective semantic tag. Note that if you are just adding GL to an existing predelivered node, tags are already mapped. This is essential as many functionalities in project reporting and budgeting use these values to report all costs booked.

There are two factors to consider:

1. Assign all the G/Ls relevant for cost booking under any existing node/item under Cost of Goods Sold. All the predelivered existing items are already mapped.

2. Create a new node/item under Cost of Goods Sold. All nodes/items must be mapped to semantic tag ACT_COST and an individual tag. For example, material cost is mapped to overall cost tag ACT_COST and individual tag MATCST.

|  |
| --- |
| Note This step is only required if you add a new node/item under Cost of Goods Sold. If you are using project budgeting, the budget controls are via semantic tags. In the budget, you can either map ACT_COST tag or any other child level tag as long as it is a part of overall ACT_COST and assigned to FSV YPS2. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Chart of Accounts, choose Details (>).
2. For the Define Financial Statement Versions row, choose Configure.

|  |
| --- |
| Note If you cannot find the configuration activity, the Q2P maintenance mode for FSVs is not active for your system. Complete the changes with the Manage Financial Statement Versions (OB58) app (part of General Ledger Accountant). |

1. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Financial Statement Versions activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Financial Statement Version | Select the following financial statement version and choose the Financial Statement Items button.FS Version: YPS2 | The Change Financial Statement Version view displays. |  |
| 2 | New Node | Drill at the top nodes until you find the Cost of Goods Sold node. To add your new node, choose the Create Items button. |  |  |
| 3 | Save | Choose Save. |  |  |

Add Semantic Tags to Newly Created Node

Purpose

In this activity, you assign semantic tags to the newly created node.

Prerequisites

Before you do this step, you need to know the item number for the newly created item. To find this item number:

- Open the Manage Financial Statement Versions (OB58) app as a General Ledger Accountant.
- In the Change View "Financial Statement Versions": Overview view, select the YPS2 financial statement version and choose the Financial Statement Items button.
- Choose Menu > Settings > Change, in the Change Settings dialog box, select Item keys visible and choose the Continue button. Note the number of the new items created.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. Choose Configure Your Solution.
4. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Chart of Accountss, choose Details (>).
2. For the Assign Semantic Tags to Financial Statement Versions row, choose Configure.

|  |
| --- |
| Note If you cannot find the SSCUI, the Q2P maintenance mode for FSVs is not active for your system. Complete the changes with Assign Semantic Tags to Financial Statement Versions (FINSC_FAGL2SEMTA) app (part of General Ledger Accountant). |

1. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app.
3. Search for the Assign Semantic Tags to Financial Statement Versions activity and choose Go to Activity.
4. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose the New Entries button. | The New Entry dialog box displays. |  |
| 2 | New Entry Type | Select Assign Semantic Tag to FS Item and choose Continue. | The New Entries: Details of Added Entries view displays. |  |
| 3 | Enter Data | Make the following entries and choose Save:FS Version: YPS2FS Items: <The new item you created as part of the Prerequisites section in this step>Semantic Tag: ACT_COSTRepeat the step with individual tag. Select the tag from existing available tags. |  |  |

#### Replicate Runtime Hierarchy

Purpose

You must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally, this would be created as a periodic job that would run in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Overhead Accounting Jobs (F3767). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job: Replicate Runtime Hierarchy (SAP) view displays. |  |
| 4 | Header Data for Hierarchy ID 0101/A000/A000 | In the header area, make the following entries and choose Schedule:Job Template: Replicate Runtime Hierarchy (SAP)Job Name: <Enter a text>Choose the Step 2 button.Start Immediately: SelectChoose the Step 3 button.In the Create Hierarchy area, make the following entry:Hierarchy ID: 0101/A000/A000Note If you are using the optional procedure Commitment Management and Cost Center Budgeting, follow steps 1-4, but make the following entries instead:Job Template: Manually Replicate Runtime HierarchyHierarchy ID: 0102/YCOA/YBA000_CE |  |  |
| 5 | Hierarchy ID YPS2 | Repeat the above steps using hierarchy ID YPS2. |  |  |

#### Open Cost Accounting Period

Use

The posting period for cost accounting must be open.

Prerequisites

Check and ensure that the cost accounting period is open for the period you are working.

|  |
| --- |
| Note For more details on this step, see the Manage Posting Periods step in Accounting and Financial Close (J58) script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Posting Periods - Cost Accounting (F4684). | The Manage Posting Periods - Cost Accounting view displays. |  |
| 3 | Check/Open Period | Make the following entries and choose Go:Company Code: 3310Fiscal Year: <current fiscal year> | Controlling posting period is now open. |  |

#### Update Overhead Rates in Costing Sheet

Purpose

For projects, the costing sheet XXXXPI (where XXXX represent your country's company code) must have overhead rates maintained for allocation.

|  |
| --- |
| Note Costing sheet is ledger-independent, so it is not possible to define different overhead rates for different ledgers. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Define Costing Sheets (102922).
6. For the displayed row, choose Details (>).
7. For the Define Costing Sheets row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Costing Sheets activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Costing Sheet and Create Overhead Rate YOH5 | Select the costing sheet XXXXPI. Expand Costing sheets and double-click on the Costing sheet row in the Dialog Structure pane to view the detail. Select row line 109 YOH5 and double-click on the Overhead rate folder in the Dialog Structure pane. | The Change View "Overhead rate": Overview screen displays. |  |
| 2 | Maintain Overhead Rate | Choose the New Entries button and make the following entries:Valid From: 01012019Valid To: 12319999CO Area: A000Ovrhd Type: 1 ActualPlant: 3310Percentage: <for example, 8>Choose New Entries and create another entry line:Valid From: 01012019Valid To: 12319999CO Area: A000Ovrhd Type: 2 PlanPlant: 3310Percentage: <for example, 8>Save the entries. | Two overhead percentage rates are created for the costing sheet for the plant. |  |
| 3 | Select Costing Sheet and Create Overhead Rate YOH6 | Repeat steps 7 and 8 but this time select row 300 YOH6 and maintain the following:Valid From: 01012019Valid To: 12319999CO Area: A000Ovrhd Type: 1 ActualPlant: 3310Percentage: <for example, 5>Choose New Entries and create another entry line:Valid From: 01012019Valid To: 12319999CO Area: A000Ovrhd Type: 2 PlanPlant: 3310Percentage: <for example, 5>Save the entries. |  |  |

#### Create and Update Allocation Structure

Purpose

This activity lets you create and update allocation structure to meet your business requirements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Maintain Allocation Structure (104073).
6. For the displayed row, choose Details (>).
7. For the Maintain Allocation Structure row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Maintain Allocation Structure activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Allocation Structure and Select Assignment | Select the allocation structure and double-click on the Dialog Structure pane to view the detail.You can now create your own allocation structures or update the predelivered allocation based on your requirements. | Update and create new allocation structures.Note Deletion of predelivered allocation structure and line ID is not allowed. Only update is possible. |  |

#### Optional: Maintain Ledger-Specific Allocation Structures

#### Create and Update Investment Profile

Purpose

This activity lets you create and update investment profile to meet your business requirements. The default content is delivered with the following investment profiles:

- 000001 Asset under Construction class for tangible assets with asset class 4001
- 000003 Asset under Construction class for intangible assets with asset class 4011

|  |
| --- |
| Note We have predelivered two separate profiles to meet requirements when you want to distinguish between tangible and intangible assets, for example, AuC like real estate as part of tangible assets, and software as part of intangible assets. |

- YS0001 is with source structure if you want to segregate costs into capitalized and non-capitalized costs for AuC
- 000002 and 000004 are for simulation purposes only without any asset class assigned
- EB0001: The event-based model with Asset under Construction (AuC), summary settlement is predelivered with Event-Based Settlement to AuC and asset class 4001. With this profile, AuC is automatically settled.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Define Investment Profile (104255).
6. For the displayed row, choose Details (>).
7. For the Define Investment Profile row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Investment Profile activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Investment Profile and Select Details | You can update the asset class in predelivered investment profile or create a new investment profile. You can also select event-based settlement to AuC. | Update and create new investment profiles.Note Deletion of predelivered investment profiles is not allowed. Only update is possible. |  |

#### Create and Update Source Structure

Purpose

This activity lets you create and update source structure to meet your business requirements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Maintain Source Structure (104308).
6. For the displayed row, choose Details (>).
7. For the Define Investment Profile row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Maintain Source Structure activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Allocation Structure and Select Assignment | Select the source structure and double-click on the Dialog Structure pane to view the details.You can now create your own allocation structures or update the predelivered allocation as per your requirements. | Update and create new source structures.Note Deletion of predelivered allocation structure and line ID is not allowed. Only update is possible.Note If you use investment profile with source structure YS, you must update the predelivered cost element group YS100 (for tangible/capitalized costs) and YS200 (intangible/non-capitalized cost) in source structure YS to avoid the error via the Manage cost element group app. Predelivered content is with empty groups and all G/Ls tht are relevant for posting must be added to groups. |  |

#### Define Assignment of AuC Classes per Source Structure

Purpose

This activity lets you create and update assignment of AuC per source assignment to meet your business requirements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Define Assignment of AuC Classes per Source Assignment (104256).
6. For the displayed row, choose Details (>).
7. For the Define Assignment of AuC Classes per Source Assignment row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Assignment of AuC Classes per Source Assignment activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Investment Profile and Select Details | You can update the asset class in predelivered investment profile by source structure or create your own combination. | Update and create new investment profile source structure.Note Deletion of predelivered investment profiles is not allowed. Only update is possible. |  |

#### Update Settlement Profile

Purpose

This activity lets you update settlement profile.

|  |
| --- |
| Note The following settlement profiles are not editable as they are for specific scope: YB00AI-Settlement asset under construction (for deprecated internal order), YBMF99-REWORK-VIA NOTIFICATION, YBMFP1-PP Valuated to COPA, and YNS-No Settlement. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Create Settlement Profile (105768).
6. For the displayed row, choose Details (>).
7. For the Create Settlement Profile: Change row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Create Settlement Profile activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Allowed Settlement Profile for Edit | Select the settlement profile and double-click on the Dialog Structure pane to view the detail.You can now update the predelivered settlement profile based on your requirements. | Updates the settlement profile.Note Deletion of predelivered settlement profile is not allowed. Only update is possible. |  |

#### Project Profile to Settlement Profile Mapping

This section describes the assignment design flow of each project profile to its respective settlement/allocation.

|  |
| --- |
| Note From the 2105 release, all settlements are by Ledger. For more information, see SAP Note [3066714](https://me.sap.com/notes/3066714). |

| Project Profile | Settlement Profile | Allocation Structure | Line ID | Cost Element Group of Line ID | Receivers |
| --- | --- | --- | --- | --- | --- |
| YP02 - Investment Project | YPSAUC - PS Settlement AUC Project | YI | Y10 - Primary Costs | 100_CE | FXA, CTR, G/L by original cost element |
| YP02 - Investment Project | YPSAUC - PS Settlement AUC Project | YI | Y20 - Secondary Costs | 200_CE | CTR by original cost element and FAX and G/L by settlement cost element 55110000-Sec.Cost Ext.Settlmt |
| YP03 - Overhead Project | YPSOVH - PS Settlement Overhead ProjectNote It is now possible to settle from project to project with the following two exceptions: 1. Sender and Receiver WBS element cannot be part of the same project. 2. Receiver Project is not of Time and Material, otherwise it will error at the time of settlement. | YO | Primary Costs | 100_CE | CTR, WBS and G/L by original cost element |
| YP03 - Overhead Project | YPSOVH - PS Settlement Overhead ProjectNote Same as the above note | YO | Secondary Costs | 200_CE | CTR, WBS by orignal cost element and G/L by settlement cost element 55110000-Sec.Cost Ext.Settlmt |
| YNS - Statistical Project | No Settlement (statistical) | N/A | N/A | N/A | N/A |
| YP05 - Project with Revenue | YPSREV - Project with Revenue | Y2 | 100 - All cost elements | YB_ALL | No settlement of revenue carrying project possible |

|  |
| --- |
| Note You can update the cost element grouping for any missing GL via the Manage Cost element Group app and do not need to update the allocation structure. Updating the predelivered cost element groups should be sufficient to avoid any error. |

#### Optional: Posting Scheme for Intercompany Clearing

Purpose

With this configuration setting, you can choose whether P&L accounts or Balance Sheet accounts are utilized for Intercompany (ICO) clearing. This setting is relevant for ICO postings such as activity allocation/time recording, universal allocation, travel expenses (including Concur postings and supplier invoices), and CO reporting.

|  |
| --- |
| Note If this setting is not enabled, the default P&L logic applies, which uses the non-operating G/L. |

Prereqisite

G/L accounts and the corresponding clearing accounts must be maintained.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Intercompany Clearing Accounts (107107).
6. For the displayed row, choose Details (>).
7. For the Define Posting Scheme for Intercompany Clearing Accounts row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Posting Scheme for Intercompany Clearing Accounts activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entry | Scheme: <Select X B/S Account or N P&L Account (Non operating)> |  |  |
| 2 | Alternative Scheme for Selected Company Codes | You can also specify the account type to be used based on the company code. Choose Review and then Save.If you select the P&L account, follow the procedure from the next topic [Optional: Map CO Intercompany Accounts](#unique_21) [page ] 23.ORIf you select the balance sheet account, use the Automatic Account Determination SSCUI to map G/L account:Area: Financial AccountingSub Area: General Ledger AccountingProcess: Prepare Intercompany TransactionsChoose Step 2.Transaction Key: BULPosting Between: <Select a company code>And: <Select a company code that is different from the above> |  |  |

#### Optional: Map CO Intercompany Accounts

Purpose

Intercompany controlling postings are supported.

|  |
| --- |
| Note This step should only be used if you need to do intercompany allocations or posting. You must map the accounts you are using and assign a relevant clearing account. |

Prereqisite

G/L accounts and the corresponding clearing accounts must be maintained.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Chart of Accounts, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Automatic Account Determination row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Automatic Account Determination activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Step 1: Area | Make the following etries and choose Step 2:Area: ControllingSubarea: Cost Center AccountingProcess: Assign Intercompany Clearing Accounts for Actual Postings |  |  |
| 2 | Step 2: Parameters | Make the following entry and choose Step 3:Chart of Accounts: YCOA |  |  |
| 3 | Step 3: Account Assignments | Select for example, the line containing the GL 65000000 and map the GL account 68888800 to the Clearing Account - Debit and to the Clearing Account - Credit.Choose Review and then Save. |  |  |

#### Optional: Currency Conversion Settings for Activity Allocation

Purpose

This configuration setting provides flexible options for currency conversion in direct activity allocation. By default, the system uses the P‑rate and the exchange rate valid on the first day of the fiscal year. However, using this SSCUI, you can adjust the setting so that the current exchange rate at the time the activity is posted is applied. This ensures that acitivty postings follow the same exchange-rate logiv used in regular financial transactions.

Prerequisite

G/L accounts and the corresponding clearing accounts must be maintained.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Intercompany Clearing Accounts (107337).
6. For the displayed row, choose Details (>).
7. For the Currency Conversion Settings for Activity Allocation row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Automatic Account Determination activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entry | Select G/L conversion. | With this change, the exchange rate applicable at the posting time is used. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

1. For a statistical project, overhead is not calculated and settlement is not required.
2. If you have revenue booked on a project, settlement is not required for revenue projects, and revenue carrying projects must not be settled.

| Process Step | Business Role | Transaction /App | Expected Results |
| --- | --- | --- | --- |
| [Run Actual Overhead - Projects](#unique_24) [page ] 28 | Cost Accountant - Overhead | Schedule Overhead Accounting Jobs (F3767) | Overheads are posted on the project. |
| [Generate Settlement Rule](#unique_25) [page ] 30 | Cost Accountant - Overhead | Generate Settlement Rules - Projects (CJB1) | Settlement rules are generated from selection variants. |
| [Actual Project Settlement](#unique_26) [page ] 31 | Cost Accountant - Overhead | Run Settlement - Actual (F4568) | The project is settled to the cost center. |
| [Assets under Construction Settlement](#unique_27) [page ] 32 | Cost Accountant - Overhead | Schedule Overhead Accounting Jobs (F3767) | The monthly costs from the investment project are posted to the AuC asset. |
| [Optional: Postprocess Event-Based Postings – Settlement (only relevant with Event-Based Settlement Profile)](#unique_28) [page ] 35 | Cost Accountant - Overhead | Postprocess Event-Based Postings - Settlement (F8485) | Any errors during the AuC settlement can be reviewed and checked. |
| [Create Assets for Complete AuC Settlement](#unique_29) [page ] 36 | Asset Accountant |  | One or more assets are created for complete AuC settlement. |
| [Maintain Settlement Rule for Final Settlement](#unique_30) [page ] 36 | Cost Accountant - Overhead | Project Control - Enterprise Projects (F3215) | Project for AuC asset is Technically Complete so the system performs Full Settlement during next project settlement run. |
| [Optional: Generate Settlement Rule (only relevant for investment projects with pass-down option selected for settlement rule maintenance)](#unique_31) [page ] 38 | Project Financial Controller | Generate Settlement Rules - Projects (CJB1) | Settlement rules are generated for investment type projects. |
| [Final Settlement of the Investment Project](#unique_32) [page ] 39 | Cost Accountant - Overhead | Schedule Overhead Accounting Jobs (F3767) | All costs are settled to the assigned receivers. |
| [Asset Transactions](#unique_33) [page ] 42 | Asset Accountant | Asset Transactions (F1614) | You created a report showing all transactions posted in asset accounting. |
| [Monitor Projects via Project Cost Report](#unique_34) [page ] 43 | Cost Accountant - Overhead | Projects - Plan/Actual (W0080) | Details of the project structure and the corresponding planned and actual costs are displayed. |
| [Monitor Projects via Project Budget Report](#unique_35) [page ] 44 | Project Financial Controller | Project Budget Report (F3377) | Monitor Projects and view Project Budget Report. |
| [Project Financial Booklet - Professional Services](#unique_36) [page ] 46 | Cost Accountant - Sales | Project Financial Booklet - Professional Services (F7479) | An overview of different metrics related to the selection criteria displays. |
| [Project Financial Booklet - Enterprise Projects](#unique_37) [page ] 48 | Cost Accountant - Sales | Project Financial Booklet - Enterprise Projects (F8698) | An overview of different metrics related to the selection criteria displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Run Actual Overhead - Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity charges the percentages of actual overheads on the project.

|  |
| --- |
| Note Overheads are now calculated and posted by Ledger. If you keep the Ledger field empty, it would post the same value (from the leading ledger 0L) to all the standard ledgers such as 0L, and 2L or 3L (if you have that in FI). If you want to have overhead values calculated per ledger, you have to start overhead calculation for every single ledger (for example, 0L, 2L, or 3L). |

|  |
| --- |
| Note SAP predelivered costing sheet comes with the overhead base and associated cost element group. Overhead base key Y001-Material is linked to cost element group 1200_CE. You can modify this group to include/exclude any GL account from the base. Also, note that it is now possible to update the predelivered costing sheet and create your own costing sheet via SSCUI 102922. |

Prerequisite

Primary cost booking is done on the project in the prerequisite scope item 1NT: Project Control – Finance or other overhead projects such as 35E: Project Control – Research and Development Projects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Overhead Accounting Jobs (F3767). | The Appplication Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job view displays. |  |
| 4 | Enter Selection Criteria | In the Template Selection section, make the following entries:Job Template: <Clear the default value and from the dropdown, select Actual Overhead Calculation: Projects (SAP)>Job Name: Actual Overhead Calculation: Projects (SAP)Choose Step 2. | The Scheduling Options view displays. |  |
| 5 | Scheduling Options | Select Start Immediately checkbox and choose Step 3. | The Parameters view display. |  |
| 6 | Parameters | Make the following entries and choose the Schedule button:Period: <period to be settled>Fiscal Year: <current fiscal year>Ledger: <0L, for example>Note Overheads are now posted by Ledger. If you keep the Ledger field empty, it would post to all the standard Ledgers such as 0L, and 2L or 3L (if you have that in FI). If you want to have overhead values calculated per ledger, you have to start overhead calculation for every single ledger (for example, 0L, 2L, or 3L).Company Code: 3310Project Definition: <Project definition that you created>Actual Overhead Calculation: SelectTest Run: Deselect | Actual overheads calculation for project is posted. |  |

### Period-End Process: Internal Cost Projects

|  |
| --- |
| NoteIf you have revenue booked on a project, settlement is not required for revenue projects.Before you execute these steps, refer to the assignment design flow of each project profile to its respective settlement/allocation [Project Profile to Settlement Profile Mapping](#unique_19) [page ] 20 section. |

|  |
| --- |
| Caution If using Assets under Construction 35F – Project Control – Capital Projects, skip this section and proceed to Period-End Process: Asset under Construction Projects section. |

#### Generate Settlement Rule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you generate the settlement rules for overhead type project such as Investment, Overhead or R&D Projects. If the settlement rules for a project can be represented using a strategy, this function supports your settlement rule generation work. In the case of direct settlement for each WBS element, it reduces maintenance work. If required, the generated settlement rules can be modified (modification of automatic generated rule is covered in 1NT: Project Control – Finance scope item).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Generate Settlement Rules - Projects (CJB1). | The Generate Settlement Rules: WBS Elements screen displays. |  |
| 3 | Create Selection Variant | Choose Create on the right of Selection variant.On the ABAP: Variants - Initial Screen, enter the name of the variant you want to create and choose Create.In the Enter profile dialog box, make the following entry and choose Continue:Database prof.: 000000000001Standard selection (structure)In the Project field, enter the project definition to be settled.Choose Attributes.Enter a description and choose Save.Choose Back twice. | The selection variant is created. |  |
| 4 | Enter Processing Data | Make the following entries:Selection variant: Selection variant created in the above stepPeriod: <enter the period>Fiscal year: <enter the fiscal year>Test Run: DeselectDetail List: Select | You have created a selection variant.Note Settlement rule is the same for all ledgers. |  |
| 5 | Select Execution Type | Choose Execute. |  |  |

#### Actual Project Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Costs are collected in projects only temporarily. They are settled to one or more receivers as part of period-end processing. This step demonstrates settlement to a cost center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Settlement - Actual (F4568). | The Run Settlement - Actual screen displays. |  |
| 3 | Select Type | Make the following selection and choose Go.Cost Object Type: <Select the project you want to settle> | A list of projects displays. |  |
| 4 | Create a Settlement Run | Select the project you created in the prerequisite script as stated in the Business Conditions section. Choose Run or Test Run. |  |  |
| 5 | Run the Settlement | In the corresponding Settlement Test Run view, make the following entries and choose Confirm:Settlement Period: <current period>Fiscal Year: <current year>Processing Type: AutomaticLedger: 0LNote For projects created before 2105, keep the Ledger blank and it would settle the same values to all ledgers but for new projects created after 2105, settlement must be executed by each Ledger independently. Repeat these steps for 2L or 3L ledger. Settlements are now run by Ledger. | The results display. |  |

### Period-End Process: Assets under Construction Projects

|  |
| --- |
| Note Before you execute these steps, refer to the assignment design flow of each project profile to its respective settlement/allocation [Project Profile to Settlement Profile Mapping](#unique_19) [page ] 20 section. |

#### Assets under Construction Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note Skip this step if you are working with Internal Cost Project and have already done the [Period-End Process: Internal Cost Projects](#unique_39) [page ] 29. |

Purpose

In contrast to assessment, you cannot perform settlement across fiscal year boundaries. The system automatically determines the posting date from the posting period/fiscal year using the last day of the posting period. There are three processing types defined for settlement:

- Automatic: The system selects all the distribution rules for a sender.
- Periodic: All distribution rules with settlement types PER and AuC are selected. PER rules are applied first. In investment measures, this is followed by settlement to assets under construction.
- Partial capitalization: Use this processing type if you want to partially capitalize an investment measure which is not yet complete, that is if you want to settle part of the overall cost to finished assets.

With this process step, a periodic settlement is executed. All costs collected on the investment project would be settled to the automatically created asset under construction (AuC).

Prerequisite

All previous process steps from scope item 35F - Project Control – Capital Projects O5F - Project Control – Capital Projects or similar are completed successfully.

|  |
| --- |
|  |

Skip this step if you are using the event-based investment profile EB0001 or any other profile marked as an Investment Measure with Event-Based Settlement to AuC. With event-based, AuC is automatically settled by line item during primary or secondary cost posting, Event-based settlement only supports 100% allocation to AuC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Overhead Accounting Jobs (F3767). | The Application Jobs view displays. |  |
| 3 | Enter Processing Data | Choose Create and make the following entries:Job Template: Actual Settlement: Projects (SAP)Job Name: <enter a name>Choose Step 2 and make the following entry:Start Immediately: <Select the checkbox>Choose Step 3 and make the following entries:Parameters:Settlement Period: <enter current period, for example 002>Fiscal Year: <enter current year, for example 2020>Ledger: <for example, 0L or your lead ledger>Note If you have a combination of projects created before 2105 and projects created after 2105 for the same project type, you must execute the collective settlement:1. Settlement with Lead Ledger would ensure all projects (old and new projects) are settled. For projects created before 2105, the app would settle the same values to all ledgers as the older project settlement rule is not configured for settlement with parallel ledger. For new projects with parallel settlement rule, Lead Ledger ONLY settles to Lead Ledger and you would require additional jobs for Ledger 2L OR 3L.2. For projects created after 2105, create settlement job for any additional ledgers 2L or 3L (if you have that in FI), otherwise balances would remain in Ledger and not specifically settled. Each ledger needs to be settled separately.Company Code: 3310Processing Type: <keep the default setting>Projects:Project Definition: <Project definition that you created>Actual Settlement: SelectTest Run: DeselectChoose the Schedule button. |  |  |

#### Optional: Postprocess Event-Based Postings – Settlement (only relevant with Event-Based Settlement Profile)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the report to review, correct/post or reverse the AuC settlement.

|  |
| --- |
|  |

This is only relevant for the event-based investment profile EB0001 or any other profile marked as an investment measure with event-based settlement to AuC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Postprocess Event-Based Postings - Settlement (F8485). | The Postprocess Event-Based Postings - Settlementscreen displays. |  |
| 3 | Enter Selection Parameters | Make the following entries and choose Go:Company Code: 3310Plant: 3310Posting Date: <Keep the default (the current period-end date of leading ledger)>WBS Element: <Enter the WBS relevant for AuC> |  |  |
| 4 | Postprocess Event-Based Postings - Settlement | At the bottom of the screen, select the WBS and decide whether to reverse the settlement or, if the error is resolved, proceed with posting the settlement.On the dialog box, select reversal reason and posting date, and choose Reverse or Post settlement. | This app shows you postings on WBS with AuC that do not result in automatic AuC posting. |  |

#### Create Assets for Complete AuC Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create one or more assets for complete AuC settlement.

Procedure

For this activity, run the Create Asset - MDS master data script, using Asset Class 2000 and Company Code 3310. Also, use Cost Center 33101001 in the Time-dependent tab.

|  |
| --- |
| Note You can use a different cost center, but ensure that you maintain a consistent combination of cost center and profit center (see the Overview of assignments table in the Master Data, Organizational Data, and Other Data section). Additionally, you must use the same assignment of cost center and profit center for the asset and the investment project. |

#### Maintain Settlement Rule for Final Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, the settlement rules for the final settlement are maintained and the status of the investment project will be set to technically complete that allows the final settlement of the project.

Prerequisite

All previous process steps are completed successfully.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Project Control - Enterprise Projects (F3215). | The Project Builder view displays. |  |
| 3 | Open Project Details | Choose the Open button and make the following entry:Project Definition: Your AuC project created in scope item 1NTChoose Enter. | Project details open in Change mode. |  |
| 4 | Maintain Settlement Rule | In the left pane, select the WBS Element (second below below the project) and then choose More > Edit > Costs > Settlement rule. | The Maintain Settlement Rule: Overview screen appears. |  |
| 5 | Enter Distribution Rules | Under the Distribution rules section, add the following two rows:1st row:Cat: FXASettlement Receiver:Asset no. created in previous step%: Portion of AUC APC that can be capitalized, e.g. 90Settlement Type: Full Settlement2nd row:Cat: CTRSettlement Receiver: Any Cost Center%: Portion of AUC APC that can be capitalized, e.g. 10Settlement Type: Full SettlementChoose OK.Note Settlement rules are common for all the standard ledgers and not different by Ledger. | If you use investment profile investment profile YS0001 with source structure YS, you must maintain the distribution rule by source structure. If you assign investment profile YS0001 with source structure YS to your project, distribution rules by each source is possible and you can select the source line ID in such cases. |  |
| 6 | Save | Choose Enter and go back to save the entries. |  |  |

#### Optional: Generate Settlement Rule (only relevant for investment projects with pass-down option selected for settlement rule maintenance)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you generate the settlement rules for investment type projects. In the case of direct settlement for each WBS element, it reduces maintenance work. This step is only required if you have selected investment Project WBS with pass-down option for the Settlement Rule Maintenance field. In this case, settlement rules are completely copied down/taken from settlement element to all elements of subtree settled to same receiver during this run.

This functionality only copies settlement rule but each lower level WBS element has its own AuC created and settle individually, and this is not a cost roll-up feature.

|  |
| --- |
| Note Pass-down settlement rule functionality is not possible with amount settlement. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Generate Settlement Rules - Projects (CJB1). | The Generate Settlement Rules: WBS Elements screen displays. |  |
| 3 | Create Selection Variant | Choose Create on the right of Selection variant.On the ABAP: Variants - Initial Screen, enter the name of the variant you want to create and choose Create.In the Enter profile dialog box, make the following entry and choose Continue:Database prof.: 000000000001Standard selection (structure)In the Project field, enter the project definition to be settled.Choose Attributes.Enter a description and choose Save.Choose Back twice. | The selection variant is created. |  |
| 4 | Enter Processing Data | Make the following entries:Selection variant: Selection variant created in the above stepPeriod: <enter the period>Fiscal year: <enter the fiscal year>Test Run: DeselectDetail List: Select | You have created a selection variant.Note Settlement rule is the same for all ledgers. |  |
| 5 | Execute | Choose Execute. |  |  |

#### Final Settlement of the Investment Project

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The final settlement transfers the costs from the AuC asset to the completed asset and to the cost center as specified in the settlement rules. After the final settlement the balance of the investment project and of the AuC is zero.

Prerequisite

The status of the project is set to technically completed and the settlement rules for the final settlement are maintained.

|  |
| --- |
| Note This step must be performed for each Ledger individually, settlements are now run by Ledger. Repeat these steps for any additional standard ledger such as 2L or 3L that you may have for parallel settlement. |

|  |
| --- |
| Note RELEVANT FOR EXISTING CUSTOMERS ONLY: For projects created before 2105, collective settlement of leading ledger would settle the same values to all ledgers but for new projects created after 2105, settlement has to has be executed by each Ledger independently. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Overhead Accounting Jobs (F3767). | The Application Jobs view displays. |  |
| 3 | Enter Processing Data | Choose Create and make the following entries:Job Template: Actual Settlement: Projects (SAP)Job Name: <enter a name>Choose Step 2 and make the following entry:Start Immediately: <Select the checkbox>Choose Step 3 and make the following entries:Parameters:Settlement Period: <enter current period, for example 002>Fiscal Year: <enter current year, for example 2020>Asset Value Date: <See the note below>Note For testing purposes, the Asset Value Date needs to be entered with a date that occurs after the asset value date used in step Assets under Construction Settlement.Ledger: <for example, 0L or your lead ledger>Note If you have a combination of projects created before 2105 and projects created after 2105 for the same project type, you must execute the collective settlement:1. Settlement with Lead Ledger would ensure all projects (old and new projects) are settled. For projects created before 2105, the app would settle the same values to all ledgers as the older project settlement rule is not configured for settlement with parallel ledger. For new projects with parallel settlement rule, Lead Ledger ONLY settles to Lead Ledger and you would require additional jobs for Ledger 2L OR 3L.2. For projects created after 2105, create settlement job for any additional ledgers 2L or 3L (if you have that in FI), otherwise balances would remain in Ledger and not specifically settled. Each ledger needs to be settled separately.Company Code: 3310Processing Type: Full SettlementProjects:Project Definition: <Project definition that you created>Actual Settlement: SelectTest Run: DeselectChoose the Schedule button. |  |  |

#### Asset Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create a report displaying all transactions posted in asset accounting as part of your periodic business.

|  |
| --- |
|  |

This step is only required if you are using the event-based investment profile EB0001 or any other profile marked as an Investment Measure with Event-Based Settlement to AuC.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Asset Transactions (F1614). |  |  |
| 3 | Enter Selection Details | Make the following entries and choose Go.Key Figure Group: For example, TRANS_ALL (All Transactions))Company Code: For example, 3310Ledger: For example, 0LFisc.Year of Ledger: For example, 2023Depreciation Area: For example, 01Display Currency: For example, AED | The Asset Transactions report displays. |  |
| 4 | Review Transactions | Expand Company Code, then expand a specific transaction. Choose the Details arrow at the right of the row. Review the information, then choose Back. |  |  |
| 5 | Asset Number | In the selected asset row, choose the asset number.Note Choose the blue link for the asset number. | A dialog box displays. |  |
| 6 | More Links | Choose More Links. | The Define Link List dialog box displays. |  |
| 7 | Manage Fixed Assets | Select Manage Fixed Assets and choose OK. | The prior dialog box displays a new link for Manage Fixed Assets. |  |
| 8 | Manage Fixed Assets | Choose Manage Fixed Assets. | The Manage Fixed Assets view displays. Review the information. |  |

### Analytics

#### Monitor Projects via Project Cost Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can analyze the cost structure of your EPMM project, and check plan/actual costs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Projects - Plan/Actual (W0080). | The Projects - Plan/Actual screen displays. |  |
| 3 | Enter Report Criteria | Make the following entries and choose Go:Ledger: 0LLedger Fiscal Year: <enter the current year>Plan Category: PLNKey Date: <end of the month>Company Code: 3310Project: <your project> | Details of the project structure and the corresponding planned and actual costs are displayed. |  |

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

#### Project Financial Booklet - Professional Services

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

- Customer Projects (Customer Project Management – Project-Based Services - J11), Project Profile: P001-Customer Project
    - Project Margin Overview
    - Project Billing Element View
    - Project Hour Details
    - Profit Center View
- Internal Projects (Internal Project Management – Project-Based Services - 1A8), Project Profiles: P002-Internal Project
    - Project Actuals
    - Project Plan/Actuals
- Projects with Revenue (Project Control – Sales - 4I9), Project Profile: YP05-Project with Revenue
    - Project Margin Overview
    - Project Billing Element View
- Overhead/Statistical Projects (Project Control – Finance - 1NT), YP03-Overhead Project, YP04-Statistical Project
    - Project Actuals
    - Plan/Actual/Commitments
    - Project Budget/Commitments
- Investment Projects (Project Control – Capital Projects - 35F), YP02-Investment Project
    - Actuals
    - Plan/Actual/Commitments
    - Budget Availability Control

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Project Financial Booklet - Professional Services (F7479). | The Project Financial Booklet - Professional Services view is displayed. |  |
| 3 | Enter Data | Make the following entries and choose Go:Project: <Enter your desired project name>Company Code: 3310Fiscal Year : <current year>Fiscal Period : <current period> | An overview of various metrics related to the selection criteria displays. |  |
| 4 | Select Required Project Type | Based on the scope covered, select one of the following options:Customer Projects (CPM project)Internal ProjectsProject with Revenue (EPMM project)Overhead/Statistical ProjectsInvestment Projects |  |  |

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
- Overhead/Statistical Projects (Project Control – Finance - 1NT), YP03-Overhead Project, YP04-Statistical Project
    - Project Actuals
    - Plan/Actual/Commitments
    - Project Budget/Commitments
- Investment Projects (Project Control – Capital Projects - 35F), YP02-Investment Project
    - Actuals
    - Plan/Actual/Commitments
    - Budget Availability Control

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Project Financial Booklet - Enterprise Projects (F8698). | The Project Financial Booklet - Professional Services view is displayed. |  |
| 3 | Enter Data | Make the following entries and choose Go:Project: <Enter your desired project name>Company Code: 3310Fiscal Year : <current year>Fiscal Period : <current period> | An overview of various metrics related to the selection criteria displays. |  |
| 4 | Select Required Project Type | Under Projects with Revenue, select one of the following options:Project Margin OverviewProject Billing Element ViewProject Budget AVCUnder the Overhead/Statistical Projects section, select one of the following options:Project ActualsPlan/Actual/CommitmentsProject Budget/CommitmentsUnder the Investment Projects section, select one of the following options:ActualsPlan/Actual/CommitmentsBudget Availability ControlNote The Project Budget AVC functionality is only available when using the Predictive Commitments Management (2I3). |  |  |

## Appendix

### Optional: Manage Settlement Rule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This app is an alternative to view existing settlement rules. It is intended for maintenance of settlement rules for individual objects, and later for mass maintenance with excel download/upload.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Settlement Rules - Projects (F6842). | The Manage Settlement Rules - Projects screen displays. |  |
| 3 | Enter Processing Data | Make the following selection and choose Go:Object Type: <Select Project or WBS element>Project: <enter a name>orWBS Element: <Select your WBS element>Distribution Rule Created: <Select Yes or No>Company Code: 3310Created By: <keep the field blank>Changed By: <keep the field blank>Processing Type: Full SettlementSelect the line and choose the > (Details) button. |  |  |
| 4 | View and Edit Details | You can view and edit the following:• Distribution Rules• Settlement Parameters• Sender Details• Settlement History Per Ledger Displays |  |  |

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
> Flagged while digesting this document, not verified: Statistical project profile is identified as YNS in the Project Profile to Settlement Profile Mapping table but as YP04 in the Project Financial Booklet sections; the document does not reconcile the two IDs.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/test-script-project-control-capital-projects-35f-ae-sap-s-4hana-cloud]]
- related-to :: [[06-management-accounting/test-script-project-control-finance-1nt-ae-sap-s-4hana-cloud-public-ed]]
- related-to :: [[06-management-accounting/test-script-project-control-research-and-development-projects-35e-ae-9]]
- related-to :: [[06-management-accounting/test-script-project-control-resourcing-and-procurement-4rf-ae-1049]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BNA_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 86,731 chars in the whole document
