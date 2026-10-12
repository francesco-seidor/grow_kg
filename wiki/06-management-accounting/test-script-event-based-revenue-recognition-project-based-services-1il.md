---
id: 06-management-accounting/test-script-event-based-revenue-recognition-project-based-services-1il
title: "Test Script: Event-Based Revenue Recognition – Project-Based Services (1IL_AE) (1IL_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (1IL_AE) for event-based revenue recognition in project-based services: prerequisites, setup, test steps."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/ebrr-for-projects]
aliases: [1IL_S4CLD2608_BPD_EN_AE]
keywords: [Event-Based Revenue Recognition for Projects, event-based revenue recognition, project-based services, recognition keys, financial statement versions, semantic tags, project profitability, revenue recognition issues, revenue recognition run, imminent loss handling]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1IL_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-725
topic: 06-management-accounting/ebrr-for-projects
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Event-Based Revenue Recognition – Project-Based Services (1IL_AE) (1IL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1IL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Event-Based Revenue Recognition for Projects** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Event-Based Revenue Recognition – Project-Based Services (1IL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847169)

[2 Prerequisites 4](#_Toc232847170)

[2.1 System Access 4](#_Toc232847171)

[2.2 Roles 4](#_Toc232847172)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847173)

[2.4 Business Conditions 5](#_Toc232847174)

[2.5 Preliminary Steps 6](#_Toc232847175)

[2.5.1 Set Report Relevancy 6](#_Toc232847176)

[2.5.2 Project Profitability Report 7](#_Toc232847177)

[2.5.3 Maintain Financial Statement Versions 8](#_Toc232847178)

[2.5.4 Replicate Runtime Hierarchy 11](#_Toc232847179)

[2.5.5 Maintain Settings for Event-Based Revenue Recognition 12](#_Toc232847180)

[2.5.6 Check and Update Derivation of Recognition Key for Project-Based Service Documents 14](#_Toc232847181)

[2.5.7 Revenue Recognition Key for Time and Expense for Usage-Based Billing 15](#_Toc232847182)

[3 Overview Table 17](#_Toc232847183)

[4 Test Procedures 18](#_Toc232847184)

[4.1 Monitor Revenue Recognition (Event-Based): Projects 18](#_Toc232847185)

[4.2 Manage Real-Time Revenue Recognition Issues 19](#_Toc232847186)

[4.3 Run Revenue Recognition: Projects 20](#_Toc232847187)

[4.4 Manage Revenue Recognition Issues: Projects 21](#_Toc232847188)

[4.5 Optional: Revenue Recognition Reversal 22](#_Toc232847189)

[4.6 Project Actual Data Reporting 22](#_Toc232847190)

[4.7 Project WIP Details Reporting 23](#_Toc232847191)

[5 Appendix 25](#_Toc232847192)

[5.1 Reverse Month-End Revenue Recognition Postings 25](#_Toc232847193)

[5.2 Inspect Revenue Recognition Postings 26](#_Toc232847194)

## Purpose

Overview

Event-based Revenue Recognition calculates and posts real-time revenue and cost adjustment for professional services for fixed price, time and material, and periodic service-type projects.

Processes that don't write a source document don't result in any real-time revenue recognition postings (for example, changes of plan data don't directly result in revenue recognition postings). If necessary, period-end closing postings (periodic revenue recognition) correct the event-based postings. This scope item covers best-guess reporting, as figures are only correct after period-end closing.

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Controlling area | A000 | Controlling Area A000 |  |
| Company code | 3310 | Company Code 3310 |  |
| Cost Center | 33101902, 33101903 | Cost Centers |  |
| Activity Types | T001-T006 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J11 - Customer Project Management – Project-Based Services | All steps of test script must be completed. |
| J12 - Time Recording – Project-Based Services orJ13 - Service and Material Procurement – Project-Based Services orJ14 - Sales Order Processing – Project-Based Services | All steps of test script must be completed. |

### Preliminary Steps

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

#### Project Profitability Report

Purpose

The SAP Project Profitability report comes with predelivered KPIs (see table below). In SAP S/4HANA Cloud Public Edition, these KPIs are linked to the predelivered financial statement version (FSV) YPS2 (GLs) via semantic tags.

| Project KPI | Associated Semantic Tag | Linked FSV node YPS2 |
| --- | --- | --- |
| Billed Revenue | BILL_REV | 23- Revenue |
| Actual Cost | ACT_COST | 24- Material Costs, 26- Costs third party, 27- Labor Costs, 28- Manufact. costs Setup time, 29- Manufact. costs Machine Time, 30- Overhead costs-Material, 33- Licenses Cost, 36- Overhead costs-Production, 29- Manufact. costs Machine Time, 47- Time recording cost, 48- Travel Cost, 49- Purchased Services, 50- Overhead Cost Admin, 51- Other Miscellaneous Cost, 52- Hardware Cost, 56-Settlement Cost via Maintenance Order, 57- Secondary GL Settlement Cost via FXA and GL |
| Recognized Revenue | RECO_REV | #20- Net Sales/Revenue |
| Recognized COS | RECO_COS | #38- Cost of Goods Sold |
| Recognized Margin | REC_MARGIN | #12- CM II |
| Revenue Adjustment | ADJ_REV | #25- Revenue Adjustments |
| COS Adjustment | ADJ_COS | #45- Rev rec cost adjustmentsNote If you use imminent loss functionality with assignment rule COSTPOCL, add the imminent loss P&L GL to ADJ_COS to get the right margin. |
| Deferred COS | DEF_COST | #44- Deferred Cost |
| Deferred Revenue | DEF_REV | #42- Deferred Revenue |
| Accrued Revenue | ACR_REV | #41- Accrued Revenue |
| Accrued COS | ACR_COST | #43- Accrued Cost |
| Reserves |  |  |
| Margin in Percent |  | Calculated |

|  |
| --- |
| Note If you want to add your own G/L accounts or create additional nodes in FSV YPS2 that are relevant for Project Profitability report, the G/L or the new node must be under one of the existing nodes (non-calculated one). See the next step for details on how to update FSV. |

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

#### Maintain Settings for Event-Based Revenue Recognition

Purpose

In the activity, you can check and update configuration of recognition key for project-based sales documents.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Profitability Analysis

1. For the row with Item Name of Revenue Recognition, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Maintain Settings for Event-Based Revenue Recognition row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration (CBC).
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Maintain Settings for Event-Based Revenue Recognition activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add/Change Entry for Recognition Key | In this configuration step, you can add G/L to predelivered sources based on your business needs.You can also update the assignment rule with the necessary G/L.For more information, see the notes below. |  |  |

|  |
| --- |
| Note You can change the source of plan values for the following RA keys via SSCUI:SPFC: Allows you to change the source of plan values from the default 306 to 305 or 500 when using the plan category version associated with Application type 1 - Project Management and Usage 4 - Manual Update.SPFCTR: Allows you to change the source of plan values from the default 306 to 305.SPFCFX: Allows you to change the source of plan values from the default 305 to 306, 303, or 500 when using the plan category version for Application type 1 - Project Management and Usage 4 - Manual Update. |

|  |
| --- |
| Note With the automatic loss handling feature, event-based revenue recognition calculates the amount needed for loss provision and the necessary adjustments to the loss provision automatically with period-end closing.If you want to use the imminent loss functionality for cost-based POC, revenue-based POC, or the completed contract method, we predeliver assignment rules COSTPOCL. You can assign this rule to recognition key SPFC.Update the G/L for Usage 300-Loss Provisioning where you intend to record the imminent loss. A specific G/L account must be used for usage 300 to prevent any potential impact on the manual loss processing with usage 301, if applicable.In Document types, change the Loss Handling to 3-Automatic creation and usage (closing).Update the financial statement version YPS2 to include imminent loss (ADJ_COS).The assignment of a balance sheet account for imminent loss reserves is not necessary for the FSV YPS2, as reporting is managed by SAP. |

|  |
| --- |
| Note CBC only: You can create your own revenue sources with names starting with Z and assign them to the provided assignment rules using customer sequence numbers that start with 1000. Additionally, you can configure the extra P&L and Balance Sheet accounts for revenue/cost adjustments and accrued/deferred revenue. Ensure that the custom source is only assigned to usage 100: Revenue for Revenue Recognition Processing. You must also add usage 400: Currency Result and usage 401: Currency Valuation to the custom source, as well as usage 103 if the default revenue source is assigned with these usages. |

|  |
| --- |
| Note CBC only: Avoid assigning the same G/L account to two source lines. When assigning a source to the assignment rule, the system ensures that no other source is already assigned that would derive the same G/L account. If this condition is met, the assignment is forbidden. During transaction processing, the assignment rule evaluates each source sequence sequentially, regardless of the source's nature (for example, revenue versus cost). Once a G/L account is determined, the process stops and proceeds with the identified source. |

#### Check and Update Derivation of Recognition Key for Project-Based Service Documents

Purpose

In the activity, you can check and update derivation of recognition key for project-based service documents.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Profitability Analysis

1. For the row with Item Name of Revenue Recognition, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Derivation of Recognition Key for Projects row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Derivation of Recognition Key for Projects activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add/Change Entry for Required Item Category | Choose the New Entries button and make the following entries:Company Code: <enter your company code>Contract Type: <enter an item category, for example, PS01>Material : <for example, *>Note Keep material as * if the same recognition key is valid for all the materials.Recognition Key: <SPFC or any other key as per your business requirements>Save the entries. | The following item categories are supported in event-based revenue recognition and based on your scope activated and business requirements, you must ensure that the derivation is set for all used item categories.The allowed item categories are PS01, PS02, PS06, PS07.Note The recognition key is represented by RecKeyArea 100, and SPTMWP to support T&E customer projects based on a shared risk agreement.Note The new key NONREV - Universal No Rev Rec is now available for use across the RA key area. This generic non-revenue recognition key represents method 2 for all scenarios supported by Event-Based Revenue Recognition.Note With key SPFCFX- SP: Fix Price Cost-Based POC Based on Object Currency, the percentage of completion (POC) is based on the project/object currency rather than the company code currency. This approach eliminates the impact of exchange rate fluctuations on POC calculations. |  |

#### Revenue Recognition Key for Time and Expense for Usage-Based Billing

Purpose

Usage-based billing (UBB) uses the contract type for periodic service. Therefore the standard derives a revenue recognition key for period service SPPC. If you would like to use the revenue recognition key for time and expense for UBB, you must follow the procedure below.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Profitability Analysis

1. For the row with Item Name of Revenue Recognition, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Derivation of Recognition Key for Projects row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Derivation of Recognition Key for Projects activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Derivation of Recognition Key for Projects | Choose the New Entries button. | The New Entries: Overview of Added Entries view displays. |  |
| 2 | Contract Type and Material | Make the following entries:Contract Type: PS06Material: <Use a material starting with U, for example U001 as per scope item Customer Project Management – Project-Based Services (J11) and key SPPC or any other key per your business requirements> |  |  |
| 3 | Save | Save the entries. |  |  |

## Overview Table

The scope item Event Based Revenue Recognition – Project Services consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | App Name | Expected Results |
| --- | --- | --- | --- |
| [Monitor Revenue Recognition (Event-Based): Projects](#unique_15) [page ] 18 | Cost Accountant - Sales | Event-Based Revenue Recognition - Projects (F4767) | Project documents are reviewed. |
| [Manage Real-Time Revenue Recognition Issues](#unique_16) [page ] 19 | Cost Accountant - Sales | Manage Real-Time Revenue Recognition Issues (F4101) | Posting entries where no corresponding real time revenue recognition posting exists are listed and the necessary corrections can be made. |
| [Run Revenue Recognition: Projects](#unique_17) [page ] 20 | Cost Accountant - Sales | Run Revenue Recognition - Projects (F4277). | Values for real-time revenue and cost adjustment for professional service for fixed price, time and materials (T&M), and periodic service projects are posted. |
| [Manage Revenue Recognition Issues: Projects](#unique_18) [page ] 21 | Cost Accountant - Sales | Manage Revenue Recognition Issues - Projects (F4100) | Resolve Revenue recognition issues. |
| [Optional: Revenue Recognition Reversal](#unique_19) [page ] 22 | Cost Accountant - Sales | Revenue Recognition Reversal (F4869) | The document is reversed. |
| [Project Actual Data Reporting](#unique_20) [page ] 22 | Cost Accountant - Sales | Projects - Actuals (F0961) | You can view actual figures based on your selection criteria. |
| [Project WIP Details Reporting](#unique_21) [page ] 23 | Cost Accountant - Sales | Project WIP Details (F1757) - if not using scope item 4E9: Project Billing – Project-Based ServicesDisplay Project WIP Details (F4766) - if using scope item 4E9: Project Billing – Project-Based Services | Report consisting the WIP details for T&M project for employee is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Monitor Revenue Recognition (Event-Based): Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Event-based revenue recognition calculates and posts real-time revenue and cost adjustment for professional service for fixed price, time and materials (T&M), and periodic service projects.

Processes that do not write a general ledger entry do not result in any real-time revenue recognition postings. For example, changes of plan data do not directly result in revenue recognition postings. Period-end-closing postings (periodic revenue recognition) correct the event-based postings. After period-end-closing, the posted values are correct and no separate settlement is required any longer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Event-Based Revenue Recognition - Projects (F4767). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Company Code: 3310Project Def.: <enter your definition> | Your project revenue recognition details are shown. |  |
| 4 | Review Detail | Select your billing element and to review details, choose the > button. | The project detail is now shown for the current period and includes details such as project status and periodic view/charts.To view a different period, choose the Set Parameters tab and change to another To Period value. |  |

### Manage Real-Time Revenue Recognition Issues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During cost or revenue posting on the cost object, errors that stop real time revenue postings can occur. This activity allows you to review these posting entries where no corresponding real time revenue recognition posting exists and make the necessary corrections. All errors must be addressed prior to the month end revenue recognition month end process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. |  |  |
| 2 | Access the App | Open Manage Real-Time Revenue Recognition Issues (F4101). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:To Fiscal Period/Year: <mm.yyyy>Company Code: 3310 | No data found indicates that there are no issues. If issues are shown, review and process corrections.Tip To download the issue list, make your filter selections and select Show Error Summary. From the list, you can choose the Download button. |  |

### Run Revenue Recognition: Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the event-based revenue recognition for projects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Revenue Recognition - Projects (F4277). | The New Job: Run Revenue Recognition - Projects view displays. |  |
| 3 | New Job | Choose the Create button. | The New Job view displays. |  |
| 4 | Enter Selection Criteria | Make the following entries and choose the Schedule button:Job Template: Run Revenue Recognition – ProjectsJob Name: <Enter a description or leave the default description>Choose Step 2.Start Immediately: <checked>Choose Step 3. Select the Fixed Period or Dynamic Period. If you select the dynamic period, in To Dynamic Fiscal Period/Year, use the dropdown to select, for example, Current Fiscal Period.Company Code: 3310Ledger: 0L | The new job is executed. |  |

### Manage Revenue Recognition Issues: Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The errors occurred during Run Revenue Recognition Projects, can be monitored and reprocessed after the error is fixed via this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Revenue Recognition Issues - Projects (F4100). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:To Fiscal Period/Year: <PPP/YYYY>Company Code: 3310Ledger: 0LProject Definition: <your definition> | No data found indicates that there are no issues. If issues are shown, review and process corrections.Tip To download the issue list: Make your filter selections and choose the Show Error Summary button. Once the list is displayed, choose the Download button. |  |

### Optional: Revenue Recognition Reversal

You could reverse revenue recognition if you made an error. For information on revenue recognition reversal, see the [Reverse Month-End Revenue Recognition Postings](#unique_23) step in the Appendix section.

### Project Actual Data Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the Project Actual Data report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Projects - Actuals (F0961). | The Projects - Actuals screen displays. |  |
| 3 | Enter Report Criteria | Make the following entries:Ledger: 0LFiscal Year of Ledger: <current year>Key Date: <Current date>Company Code: 3310G/L Account Hierarchy: YPS2 | The actual figures for projects - actuals display. |  |
| 4 | Accept | Choose OK. |  |  |

### Project WIP Details Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report is only relevant for a Time and Materials (T&M) project, when Work In Progress (WIP) reporting details are from your own database - combining Dynamic Item Processor (DIP) data and revenue recognition values.

The database updates the event-based revenue recognition app postings (for example, manual adjustment from either app or revaluation) with the post processing run. The report does not include the event-based revenue recognition entries. The main purpose of a Project WIP report is for displaying WIP project details for employees.

Procedure (if you are NOT using non-standard scope item 4E9: Project Billing – Project-Based Services)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Project WIP Details (F1757). | The Projects WIP Detailsscreen displays. |  |
| 3 | Enter Report Criteria | Make the following entries:Company Code: 3310WBS Element: <Enter your specific WBS element>To Fiscal Period/Year: <Current period>Employee Name: <Employee for which you want to see the WIP Details> | The figures for projects - actuals display. |  |
| 4 | Accept | Choose the Go button. |  |  |

Procedure (if you are using non-standard scope item 4E9: Project Billing – Project-Based Services)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Project WIP Details (F4766). | The Projects WIP Details (2) screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entry and choose Go:Project Definition: <Enter your project definition>Fiscal Year Period: Current periodEmployee Name: <Employee for which you want to see the WIP Details> | The figures for projects display. |  |
| 4 | Refine your View | To further refine the view, expand the lines and see additional detail, choose Settings. For example, in the View Settings window, select G/L Account and choose Go. | The project detail would now list separate lines for every different G/L. |  |

## Appendix

### Reverse Month-End Revenue Recognition Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Occasionally, you may be required to reverse revenue recognition posts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Revenue Recognition (F4869). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job: Reverse Revenue Recognition view displays. |  |
| 4 | Enter Selection Criteria | In the Template Selection section, make the following entries:Job Template: Reverse Revenue RecognitionJob Name: Reverse Revenue RecognitionChoose Step 2. | The Scheduling Options view display. |  |
| 5 | Scheduling Options | Select Start Immediately checkbox and choose Step 3. | The Parameters view display. |  |
| 6 | Parameters | Make the following entries:Posting Date: <Enter a desired date>Note This must be a month-end date. Otherwise, no selection will be returned.Company Code: 3310Ledger: <enter a ledger>Journal Entry: <Enter the document you want to reverse> | The figures for projects display. |  |
| 7 | Schedule Job | Choose the Schedule button. | The document is reversed. |  |

### Inspect Revenue Recognition Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The project revenue recognition and flows are shown.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Inspect Revenue Recognition Postings (F4008). |  |  |
| 3 | Enter Selection Criteria | Make the following entries:Account Assignment Object: <project or WBS element>Ledger: 0LCurrency Type: Company Code CurrencyDocument Range: All |  |  |
| 4 | Execute | Choose Go. |  |  |

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
- related-to :: [[06-management-accounting/event-based-revenue-recognition-project-based-sales-4gq-ae-1024]]
- related-to :: [[06-management-accounting/event-based-revenue-recognition-project-based-services-us-gaap-33o-ae]]
- related-to :: [[06-management-accounting/test-script-event-based-revenue-recognition-project-based-sales-ifrs-4]]
- related-to :: [[06-management-accounting/test-script-event-based-revenue-recognition-project-based-sales-us-gaa]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1IL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 47,021 chars in the whole document
