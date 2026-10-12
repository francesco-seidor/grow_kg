---
id: 03-financial-accounting-and-close/test-script-asset-accounting-group-ledger-ifrs-1gb-ae-719
title: "Test Script: Asset Accounting – Group Ledger IFRS (1GB_AE) (1GB_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (1GB_AE) for Asset Accounting with Group Ledger IFRS: prerequisites, legacy asset setup, revaluation index, test procedures."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/asset-accounting-ifrs-and-us-gaap]
aliases: [1GB_S4CLD2608_BPD_EN_AE]
keywords: [Asset Accounting with IFRS and US GAAP Group Ledgers, asset accounting, group ledger ifrs, legacy asset transfer, asset revaluation, asset revaluation index, test prerequisites, business roles, balance carryforward, asset acquisition]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GB_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-719
topic: 03-financial-accounting-and-close/asset-accounting-ifrs-and-us-gaap
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Asset Accounting – Group Ledger IFRS (1GB_AE) (1GB_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GB_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Asset Accounting with IFRS and US GAAP Group Ledgers** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Asset Accounting – Group Ledger IFRS (1GB_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847023)

[2 Prerequisites 4](#_Toc232847024)

[2.1 System Access 4](#_Toc232847025)

[2.2 Roles 4](#_Toc232847026)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847027)

[2.4 Business Conditions 6](#_Toc232847028)

[2.5 Preliminary Steps 7](#_Toc232847029)

[2.5.1 Validate Asset Accounting System Readiness 7](#_Toc232847030)

[2.5.1.1 Confirm Takeover Date Information 7](#_Toc232847031)

[2.5.1.2 Confirm Run of Balance Carryforward for Current Fiscal Year 8](#_Toc232847032)

[2.5.1.3 Create Asset Master Record for Legacy Asset 9](#_Toc232847033)

[2.5.1.4 Post Transfer Values for Legacy Asset 11](#_Toc232847034)

[2.5.2 Asset Revaluation Index (Optional) 13](#_Toc232847035)

[2.5.2.1 Maintain Asset Revaluation Index 13](#_Toc232847036)

[2.5.2.2 Assign Asset Revaluation Index in Asset Master Data 14](#_Toc232847037)

[2.5.2.3 Assign Asset Revaluation Index - View Results 15](#_Toc232847038)

[3 Overview Table 16](#_Toc232847039)

[4 Test Procedures 18](#_Toc232847040)

[4.1 Create Asset Subnumber 18](#_Toc232847041)

[4.2 Acquisition 19](#_Toc232847042)

[4.2.1 Post Credit Memo - in Year of Invoice 19](#_Toc232847043)

[4.2.2 Post Credit Memo After Year of Invoice 19](#_Toc232847044)

[4.3 Retirement 20](#_Toc232847045)

[4.3.1 Post Retirement with Revenue 20](#_Toc232847046)

[4.3.2 Post Retirement Without Revenue 21](#_Toc232847047)

[4.4 Valuation (Transfer and Manual Value Correction) 22](#_Toc232847048)

[4.4.1 Reverse Journal Entry (Asset Accounting Specific) 22](#_Toc232847049)

[4.4.2 Post Transfer - Within Company Code 22](#_Toc232847050)

[4.4.3 Post Post-Capitalization 23](#_Toc232847051)

[4.4.4 Post Writeup 24](#_Toc232847052)

[4.4.5 Post Depreciation Manually - Unplanned and Planned 25](#_Toc232847053)

[4.4.6 Recalculating Values 25](#_Toc232847054)

[4.4.7 Post Asset Revaluation 26](#_Toc232847055)

[4.5 Closings 28](#_Toc232847056)

[4.5.1 Manage Depreciation Run 28](#_Toc232847057)

[4.5.2 Depreciation Lists - Year End Closing 29](#_Toc232847058)

## Purpose

Overview

Asset accounting is a subsidiary ledger of the general ledger and is used to manage and document fixed asset transactions in detail. In general ledger accounting, you can update depreciation and changes to asset balance sheet values in asset accounting. You can also make various account assignments to cost accounting for these transactions. Because of the integration in SAP S/4HANA Cloud Public Edition, Asset Accounting (FI-AA) transfers data directly to and from other SAP S/4HANA Cloud Public Edition components like Financial Accounting (FI) components.

Ledger-specific transactions and reports support analysis of depreciation and asset balance to fulfill different accounting principle, such as Asset Revaluation, Depreciation Reporting, Manage Depreciation Runs, Asset Balance, and Asset Total Depreciation.

This scope item is for IFRS.

|  |
| --- |
| Note When you perform a ledger switch, IFRS is assigned to ledger 0L and the local ledger is assigned to ledger 2L. Index-based revaluation may apply because it's based on the local ledger (not IFRS). Revaluation of the local ledger is determined in the valuation view based on local accounting laws.As an example, the following tables show this using the U.S. The same logic applies for all countries/regions using your own local ledger:Table 1: Example: SAP Best Practices Solution for US with IFRSLedgerAccounting PrincipleRevaluation0LUSAPNo revaluation2LIFRSRevaluation allowedTable 2: Example: Ledger Switch Solution for USLedgerAccounting PrincipleRevaluation0LIFRSRevaluation allowed2LUSAPNo revaluation |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/1GB_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Asset Accountant | SAP_BR_AA_ACCOUNTANT | Fixed Assets | SAP_BR_AA_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Baseline Package, you can use the following Baseline Package scenario data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Chart of Depreciation | 3310 |  |  |
| Asset Class | Any available asset class, except 4000 and 4001 |  | If a special asset class is required see the Prerequisites section for each process step. |
| Asset | Any available asset master |  | If no asset master is available in your system, create an asset master. If a special asset is required, see the Prerequisites section for each process step. |
| Vendor | Any domestic vendor |  | If no vendor is available in your system yet, create a domestic vendor. |
| Customer | Any domestic customer |  | If no customer is available in your system, create a domestic customer. |
| Cost Center | Any domestic cost center |  | If no cost center is available in your system, create a cost center. |
| Ledger | 2L |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 3: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |
| BNI | Create Asset - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNI - Create Asset - MDS | During the execution of this scope item, asset master records are created. To create the assets, use the Create Asset - MDS (BNI) master data script and then use the data described in this test script. |
| J62 - Asset Accounting | The test script must be executed in its entirety. The business processes described in this scope item build upon the data processed in J62. |
| 1GA - Accounting and Financial Close – Group Ledger IFRS | The test script must be executed in its entirety to set up the Group Ledger IFRS. |

Activate Features

In a software update, SAP delivers certain features that could have an impact on your implemented solution initially in an inactive state. You can choose to already activate these features before they become available by default in a later release.

The test procedures in this document describe the software behavior when all features have been activated. It is a prerequisite for testing that you have activated all of the following features in each of your systems using the configuration activity Activate Features. For more information about this activity, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/3e94fcc37b42433b97d6aef0c830dc52.html) for SAP S/4HANA Cloud Public Edition.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution. Search for Activate Features. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Features. Choose the link to navigate directly to the target system of SAP S/4HANA Cloud Public Edition. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

| Feature ID | Feature Title |
| --- | --- |
| FAA_DEPRECIATION_PROFILE | Introduction of configurable depreciation profiles |

### Preliminary Steps

#### Validate Asset Accounting System Readiness

##### Confirm Takeover Date Information

Purpose

In this activity, you create a legacy data transfer segment to allow for transfer of fixed assets on a specific transfer date. You can also define additional parameters for the legacy data transfer.

|  |
| --- |
| Note Once you complete the initial content activation, you must define a take-over date. This defines the current fiscal year and last closed fiscal year in Asset Accounting. The takeover date is critical for system processing, as it identifies the point in time that old asset values are loaded. This is usually the prior year-end day. For AuC Asset Value Date, the value is automatically set to the first day of the new fiscal year (1/1/YYYY+1) instead of the transfer date (12/31/YYYY). For example, if you're in fiscal year 2025, this implies the loading of old legacy assets is as of the year end 2023. |

|  |
| --- |
| Caution If Legacy Data Transfer is defined in the general ledger, the Legacy Data Transfer Date in Asset Accounting can’t be set as an earlier date. |

Procedure

1. Log on to the SAP Fiori launchpad as an Asset Accountant.
2. Open Make Company Code Settings - Asset Accounting-Specific (F7312).

|  |
| --- |
| Note Company codes are automatically synchronized. If problems occur, you can manually start the synchronization by choosing Synchronize Company Codes. |

1. Enter your company code in the filter area and choose Go.
2. Select your company code. On the next view, choose Edit.
3. Check the status for your company. If it isn't in For Testing status, set it to that status.
4. On the Legacy Data Transfer Settings tab, check or change the following entries (if necessary, to create a new legacy transfer segment, choose Create):

| Field | Value | Comments |
| --- | --- | --- |
| Transfer Date | <last day of prior fiscal year end> | This date is usually the year-end date of the previous year. If you are instructed to use a mid-year date, choose a month-end date instead. The date should always move forward; do not change it backward.The current and closed fiscal years are determined based on the Transfer Date. To check these fiscal years, double-click the ledger on the left side of the screen. The result is displayed on the right side of the screen, under the Ledger Settings tab.If the Legacy Data Transfer Segment isn't required, you can manually enter the current fiscal year. The closed fiscal year is then derived automatically. Without defining the Legacy Data Transfer Segment, no legacy asset master data can be created. |
| Legacy Data Transfer Status | Ongoing (Other Postings Allowed) | Possible settings:In Preparation: The system allows incomplete customizing settings for the legacy data transfer (for example, the document type for posting of the legacy data transfer can be missing). When set to In Preparation, no postings are allowed.Ongoing: Only legacy data transfer postings are permitted. Other types of postings, such as acquisitions or retirements aren’t permitted.Ongoing (Other Postings Allowed): Both legacy data transfer postings and other postings are permitted. This status is useful when performing further legacy data transfers in an already productive company code.Completed: The legacy data transfer is completed. Legacy Data Transfer postings and creation of legacy assets aren’t allowed. The Completed status becomes visible only after you complete the segment. |
| Document Type | AA – Asset Posting |  |

1. After the legacy data transfer is completed, set the Legacy Data Transfer Status to Completed.
2. Before you make postings in Asset Accounting in your P-system, repeat the preceding steps to confirm values for data the takeover date, the status, and the document type for entering legacy assets already done in the Q-system.

##### Confirm Run of Balance Carryforward for Current Fiscal Year

Purpose

In this activity, you confirm that Balance Carryforward is run for the current fiscal year.

|  |
| --- |
| Note If your implementation doesn't use a specific ledger, disregard that ledger. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Schedule General Ledger Jobs (F1927). | The Application Jobs view is displayed. |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Details | Make the following entries and choose Step 2:Job Template: Balance CarryforwardJob Name: Balance Carryforward |  |  |
| 5 | Enter Details | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Details | Make the following entries and choose Schedule:Ledger: <ledger; use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Company Code: 3310Carry Forward to Fiscal Year: <fiscal year>Test Run: Selected | You scheduled the job run as a test run. |  |
| 7 | Review Results | To review the results of your test run, find your run in the Jobs pane and choose Details (>) on the right side of its row. |  |  |
| 8 | Run Details | Choose the Run Details tab. Review the log status. |  |  |
| 9 | Productive Run | To perform a productive run, repeat this process, but deselect Test Run. | You scheduled the job run as a productive run. |  |

##### Create Asset Master Record for Legacy Asset

Purpose

In this activity, you can create legacy assets with values. These assets may be used for various testing scenarios.

Prerequisites

To take over your legacy data in asset accounting, only one fiscal year can be open. If you receive an error stating that more than one year is open, check that the previous fiscal year is closed in asset accounting. To check, use the Make Company Code Settings - Asset Accounting-Specific (F7312) app. For your company code, the previous fiscal year must be closed.

Procedure

|  |
| --- |
| Note Create five legacy assets with different descriptions. Ensure that the asset description begins with the word Legacy. |

Table 4: Create Asset Master Record for Legacy Asset

| Process Step | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant . |  |  |
| 2 | Access the SAP Fiori app | Open Manage Legacy Assets (F7280A). | The Manage Fixed Assets - Legacy view is displayed. |  |
| 3 | Create Fixed Asset | Choose Create > Create Main Asset . |  |  |
| 4 | Enter Transaction Details | Make the following entries and press Enter:Company Code: For example, 3310Asset Class: For example, <asset class; See the Master Data, Organizational Data, and Other Data topic> |  |  |
| 5 | Enter Transaction Details | Make the following entry:Asset Description: Legacy Asset xxxxxx |  |  |
| 6 | Enter Capitalization Date | Choose the Ledger tab.Make the following entry:Capitalized On: for example, 12/31/2020 ( December 31, 2020)Note This is a prior year asset.Choose the Time- Dependent Data tab. |  |  |
| 7 | Enter Transaction Details | Make the following entries:Cost Center: For example, 33101301Note You can enter the Cost Center and/or the WBS Element. |  |  |
| 8 | Enter Transaction Details | Choose the Valuation tab.Confirm Key, Life, and Start Date.Note If you activated the feature toggle for the new design, also confirm Depreciation Profile, Useful Life, and Start Date. |  |  |
| 9 | Create the Record | Choose Create (at lower right). | Note Make a note of the asset number generated by the system: ______________. |  |

##### Post Transfer Values for Legacy Asset

Purpose

In this activity, you post the transfer values for the legacy assets.

Prerequisites

To take over your legacy data in asset accounting, only one fiscal year is open. If an error states that more than one year is open, check that the previous fiscal year is closed in asset accounting. To check, use the Make Company Code Settings - Asset Accounting-Specific (F7312) app. Ensure that the previous fiscal year is closed for your company code.

Procedure

Table 5: Post Transfer Values for Legacy Asset (Accumulated APC and Accumulated Depreciation)

| Process Step | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log into the SAP Fiori launchpad as an Asset Accountant . |  |  |
| 2 | Access the SAP Fiori app | Open Post Transfer Values - For Legacy Asset (ABLDT) . | The Create General Header Data for Posting box is displayed. |  |
| 3 | Enter the Company and Legacy Asset | Make the following entries and choose Continue:Company Code: For example, 3310Asset: For example, xxxxxx |  |  |
| 4 | Enter values for Legacy Asset | Based on the ledger selection, the assigned depreciation areas are listed.If you select the Calculate Currencies checkbox, the values entered for company code currency are translated into the group currency using the exchange rate available in the system. These settings are recommended for testing purposes.If you need to manually maintain currency conversion due to different exchange rates, don't select the Calculate Currencies checkbox. Enter the values for group currency manually in the Amount in Global Currency column.On the Cumulated Values tab, enter values for the following lines for Amount in Company Code currency:Ledger 0L:Depreciation area 0107000 Cumulative Acquisition Costs: 3600.00 AED07005 Cumulative Ordinary Depreciation: -900.00 AEDLedger 0L:Depreciation area 1507000 Cumulative Acquisition Costs: 3600.00 AED07005 Cumulative Ordinary Depreciation: -900.00 AEDLedger 2L:Depreciation area 3207000 Cumulative Acquisition Costs: 3600.00 AED07005 Cumulative Ordinary Depreciation: -900.00 AEDNote The depreciation amounts in the bulleted lists above should be entered as negative amounts.Note Enter values for each depreciation area. | The Enter Asset Transaction Legacy Data view is displayed. The following tabs are available:Cumulated Values - The relevant amounts for APC, Ordinary Depreciation, Special Depreciation, and other items are required when the date for Legacy Transfer Segment is the end of the previous year.Posted Values - The relevant amounts for Ordinary Depreciation, Special Depreciation, and other items are required for cases where the date for Legacy Transfer Segment is during the current year. In this case, the last period for depreciation run should be entered in addition to the depreciation amount posted for current year.Bypass the warning Posting will take place in an earlier fiscal year.If any errors are RED coded, correct these before posting. |  |
| 5 | Post Legacy Asset Transaction | Choose Post.Choose Continue. | Note Document number for each accounting principle:AE AP _________IFRS _________USGP _______ |  |

#### Asset Revaluation Index (Optional)

##### Maintain Asset Revaluation Index

Purpose

Use the new app to perform automatic revaluations based on index values. In this app, you maintain index values for revaluation indexes. You can source index values from various places, such as an index officially released by an authority.

To activate automatic periodic revaluation calculations for assets, ensure the revaluation index is active and its ID is assigned to the asset master record. You can use the revaluation index in one or more valuations. The system calculates and posts automatic revaluations based on these index values. It posts the calculated revaluation amounts automatically during the periodic depreciation posting run when the calculation is triggered.

|  |
| --- |
| Note These prerequisites steps are required only for asset revaluation when using a revaluation index. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access App | Open Maintain Asset Revaluation Index (F8119). |  |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter RevaluationID | Make the following entries and choose Continue:Revaluation Index ID: <revaluation index ID>Index Type: Replacement Value Index |  |  |
| 5 | Header | Maintain your required index settings and choose Create:Index Description: <index description>Country/Region Key: <your country or region> | The system displays the message Object created. |  |
| 6 | Index Items | In the Index Items pane, make the following entries:Valid To: <date>, for example, 12/31/2025Index Points: <index points>, for example, 100Repeat this for each year's index.When done, choose Save. |  |  |
| 7 | Activate Revaluation index | Choose Activate. | The system displays the message Index _____ was activated. |  |

##### Assign Asset Revaluation Index in Asset Master Data

Purpose

In this activity, you assign the asset index revaluation to an asset master data.

|  |
| --- |
| Note The Asset Revaluation Index is assigned to a ledger. If you use multiple ledgers, repeat this instruction for each ledger that needs to be revalued. |

|  |
| --- |
| Note Depending on your requirements, you might need to perform the following steps for each ledger. |

Procedure

| Process Step | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Fixed Assets (F3425A). |  |  |
| 3 | Enter Asset Information | Make the following entries and choose Go:Company Code: <your company code>Main Asset Number: <your asset number> |  |  |
| 4 | Edit Asset | For the row with your asset number, choose > (Details). Choose Edit. |  |  |
| 5 | Assign Revaluation Index | Choose the Valuation tab. |  |  |
| 6 | Assign Revaluation Index | Select your ledger and choose Details (>). |  |  |
| 7 | Assign Revaluation Index | Choose the General Parameters tab. |  |  |
| 8 | Assign Revaluation Index | Enter the Revaluation Index ID and choose Apply. |  |  |
| 9 | Save Changed Asset Master | Save your entries. | Asset master data is saved. |  |

##### Assign Asset Revaluation Index - View Results

Purpose

After you assign the asset revaluation index, results are updated for future calculations.

|  |
| --- |
| Note The Asset Revaluation Index is assigned to a ledger. You'll need to repeat this procedure for each ledger to be revalued. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Fixed Assets (F3425A). |  |  |
| 3 | Asset Information | Make the following entries and choose Go:Company Code: 3310Main Asset Number: <asset number> |  |  |
| 4 | Select Asset | Select your asset number from the list. |  |  |
| 5 | Valuation | Choose the Valuation tab. |  |  |
| 6 | Ledger | Select the ledger and choose > (Details). |  |  |
| 7 | Value DIsplay | Choose the Value Display tab. |  |  |
| 8 | Key Figures | Choose the Key Figures tab.Make the following entries and press Enter:Fiscal Year of Ledger: <YYYY +1> |  |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 6: Master Data

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Asset Subnumber](#unique_15) [page ] 18 | Asset Accountant | Run the processes in the Create Asset - MDS (BNI) master data script. | The asset master subnumber is created.Subnumbering starts with 1. |

Table 7: Acquisition

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Post Credit Memo - in Year of Invoice](#unique_16) [page ] 19 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | A debit memo is posted to the asset against the automatic clearing account. |
| [Post Credit Memo After Year of Invoice](#unique_17) [page ] 19 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | A debit memo is posted to the asset against the automatic clearing account. |

Table 8: Retirement

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Post Retirement with Revenue](#unique_18) [page ] 20 | Asset Accountant | Post Asset Retirement (F7107) | The asset is retired against the automatic clearing account. |
| [Post Retirement Without Revenue](#unique_19) [page ] 21 | Asset Accountant | Post Asset Retirement (F7107) | The Asset is scrapped. |

Table 9: Valuation (Transfer and Manual Value Correction)

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Reverse Journal Entry (Asset Accounting Specific)](#unique_20) [page ] 22 | Asset Accountant | Manage Fixed Assets (F3425A) | The document is reversed. |
| [Post Transfer - Within Company Code](#unique_21) [page ] 22 | Asset Accountant | Post Asset Transfer (F9302) | The Asset is transferred. |
| [Post Post-Capitalization](#unique_22) [page ] 23 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | The post-capitalization is posted to a Post Capitalization asset master record. |
| [Post Writeup](#unique_23) [page ] 24 | Asset Accountant | Post Writeup (ABZUL) | The write-up is posted to a prior year asset.Note A subsequent change to the valuation of an asset (reversal of depreciation) is required. |
| [Post Depreciation Manually - Unplanned and Planned](#unique_24) [page ] 25 | Asset Accountant | Post Depreciation Manually - Unplanned and Planned (ABAAL) | The unplanned depreciation is posted to the asset. |
| [Recalculating Values](#unique_25) [page ] 25 | Asset Accountant | Schedule Asset Accounting Jobs (F1914) | The depreciation of an asset master data record is recalculated. |
| [Post Asset Revaluation](#unique_26) [page ] 26 | Asset Accountant | Post Asset Revaluation (F7775) | Revaluation is posted to the asset and will be posted to GL with the next depreciation run. |

Table 10: Closings

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Depreciation Run](#unique_27) [page ] 28 | Asset Accountant | Schedule Asset Accounting Jobs (F1914) | The Depreciation Posting Run screen displays the log. |
| [Depreciation Lists - Year End Closing](#unique_28) [page ] 29 | Asset Accountant | Depreciation Lists (F1616) | The Depreciation Lists report displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Asset Subnumber

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a new asset master subnumber data record as part of your daily business. You use subnumbers when the asset consists of components that must be recorded separately or may have different depreciation terms. For example, under IFRS guidelines, if an asset is made up of multiple components and these components have different useful lives, each component should be treated as a separate subnumber asset.

Procedure

You must create asset master data. Initially, you should create the following:

- Asset master record
- Asset master records with subnumbers

|  |
| --- |
| Note To execute this activity, run the processes in the Create Asset - MDS (BNI) master data script to create the asset master data necessary to use a parallel ledger for asset accounting. |

### Acquisition

#### Post Credit Memo - in Year of Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post an asset credit memo in the acquisition year automatically against a clearing account as part of your daily business (main or subnumber). No vendor is involved. If necessary, you can designate an accounting principle in the transaction to post the credit memo to a specific ledger.

Prerequisites

Use an existing asset in any asset class (except 4000, 4001, 4010, and 4011) that has acquisition postings. If no suitable asset exists, you must create asset master data.

To create the asset master data, run the processes in the Create Asset - MDS (BNI) master data script, using the master data from this document. Post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app. You can then complete the following credit memo procedure.

Procedure

To execute this activity, run the processes in the Post Credit Memo - in Year of Invoice section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Credit Memo After Year of Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can post an asset credit memo later than in the acquisition year automatically against a clearing account as part of your daily business (main or subnumber). No vendor is involved. If necessary, you can designate an accounting principle in the transaction to post the credit memo to a specific ledger. This can be applied to post-capitalized assets.

Prerequisites

Use an existing asset in any asset class (except 4000, 4001, 4010, and 4011) that has acquisition postings. If no suitable asset exists, you must create asset master data.

To create asset master data, run the processes in the Create Asset - MDS (BNI) master data script, using the master data from this document. Post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app. You normally use this transaction with an asset that was acquired in a prior fiscal year (for example, the capitalization date of the asset is in a prior year).

If you can’t create a post-capitalized asset with a posting date in a prior fiscal year because the prior year is closed, test the transaction with an asset acquired in the current fiscal year. You should then use a posting date in the next fiscal year. Before proceeding, make sure that the next fiscal year is open for posting by executing the Carry Forward G/L Balances step in the Prerequisites section of the Accounting and Financial Close (J58) test script.

Procedure

To execute this activity, run the processes in the Post Credit Memo After Year of Invoice section in the Asset Accounting (J62) test script, using the master data from this document.

### Retirement

#### Post Retirement with Revenue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can post a retirement from the sale of an asset automatically against a clearing account as part of your daily business (main or subnumber). No customer is involved. If necessary, you can designate an accounting principle in the transaction to post the retirement to a specific ledger.

Prerequisites

Use an existing asset in any asset class (except 4000, 4001, 4010, and 4011) that has acquisition postings. If no suitable asset exists, you must create asset master data.

To execute this activity, run the processes in the Create Asset - MDS (BNI) Master Data Script, using the master data from this document.

Upon completion of those processes, post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

To execute this activity, run the processes in the Post Retirement with Revenue section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Retirement Without Revenue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post an asset retirement by scrapping as part of your daily business (main or subnumber). If necessary, you can designate an accounting principle in the transaction to post the retirement to a specific ledger.

Prerequisites

Use an existing asset in any asset class (except 4001 and 4011) that has acquisition postings. If no suitable asset exists, you must create asset master data.

To execute this activity, run the processes in the Create Asset - MDS (BNI) Master Data Script, using the master data from this document. After completing that process, post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

To execute this activity, run the processes in the Post Retirement Without Revenue section in the Asset Accounting (J62) test script, using the master data from this document.

### Valuation (Transfer and Manual Value Correction)

#### Reverse Journal Entry (Asset Accounting Specific)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can cancel documents posted to a specific ledger in asset accounting as part of your daily business.

|  |
| --- |
| Caution The original document must only post to this specific ledger. For example, you have an asset, but only posted value to the IFRS ledger that is depreciation area 32. |

You can post the reversal to a specific ledger by designating the appropriate depreciation area in the transaction, for example 2L, representing a specific ledger.

Prerequisite

Use an existing asset in any asset class that has a specific ledger acquisition posting, for example 2L. If no suitable asset exists, you must create asset master data.

To create asset master data, run the processes in the Create Asset - MDS (BNI) master data script, using the master data from this document. Post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

To execute this activity, run the processes in the Reverse Journal Entry (Asset Accounting-Specific) section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Transfer - Within Company Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform a transfer from one asset master data record to another asset master data record within the same company code as part of your daily business. If necessary, you can designate an accounting principle in the transaction note to post the transfer to a specific ledger.

Intracompany transfers are used to correct wrong account assignments such as asset class.

Prerequisite

Use an existing current year asset in any asset class (except 4000, 4001, 4010, and 4011) that has acquisition postings. If no suitable asset exists, you must create asset master data.

To create asset master data, run the processes in the Create Asset - MDS (BNI) master data script, using the master data from this document. Post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

To execute this activity, run the processes in the Post Transfer Within Company Code section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Post-Capitalization

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can enter a post-capitalization for a specific accounting principle on a new post-capitalization asset master data record. Post-capitalization represents subsequent corrections to the acquisition and production costs (APC) of a fixed asset. For example, you could use this correction type if you neglected to add expenditures and costs linked with the acquisition or assembly of an asset to its APC in a past fiscal year. In this example, a new asset master record is created in the same transaction as the post-capitalization. However, post capitalization can also be performed on an existing asset.

Procedure

To execute this activity, run the processes in the Post Post-Capitalization section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Writeup

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can post a writeup for an asset master data record.

Prerequisite

Writeups are only created for depreciation in the past (that is, depreciation from previous years). This implies an asset capitalized from a prior year and depreciation was incurred in the prior year. The writeup amount can’t exceed the life-to-date depreciation of this asset. Various standard transaction types are configured for writeups. These transaction types differ according to the depreciation type to be corrected (for example, ordinary depreciation or unplanned depreciation) and the depreciation areas to be posted (for example, book depreciation only).

In the following procedure, the ordinary depreciation is corrected for a specific accounting principle and its respective depreciation areas as an example.

|  |
| --- |
| Note Writeups are used for correction of depreciation values of a past year. If you only have the current year available:Execute the Carry Forward G/L Balances steps in the Prerequisites section of the Accounting and Financial Close (J58) test script to open the next fiscal yearPost a writeup with Posting Date and Asset Value Date in the next year for a current year asset |

|  |
| --- |
| Note Use an existing asset in any asset class that has acquisition postings. If no suitable asset exists, then create asset master data. To create asset master data, run the processes in the Create Asset - MDS (BNI) master data script, using the master data from this document. Afterwards, post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app. |

Procedure

To execute this activity, run the processes in the Post Write-up section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Depreciation Manually - Unplanned and Planned

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can manually enter unplanned depreciation amount to be posted within the next depreciation run. If necessary, you can designate an accounting principle in the transaction to post the unplanned depreciation to a specific ledger.

Prerequisite

Use an existing asset in any asset class that has acquisition postings. If no suitable asset exists, then create asset master data. To create master data, run the processes in the Create Asset - MDS (BNI) master data script, using the master data from this document. Then post acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

To execute this activity, run the processes in the Post Depreciation Manually - Unplanned and Planned section in the Asset Accounting (J62) test script, using the master data from this document.

#### Recalculating Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you recalculate the depreciation of an asset master data record. Recalculation may be necessary if there’s a configuration change to the depreciation keys or terms. Changing the depreciation key or useful life on the asset master usually doesn’t require recalculation since the system automatically adjusts the planned depreciation at the time of the change. Nevertheless, it’s a best practice to include this as part of your periodic processing to ensure G/L and fixed assets are in balance. Since no configuration changes are made in this test script, the detail log should be empty.

|  |
| --- |
| Note If you activated the feature toggle for the new design, use the Depreciation Profile field instead of the Depreciation Key field. |

Prerequisite

You may need to recalculate planned annual depreciation in certain company codes or for individual fixed assets. This may be necessary if:

- You've changed the depreciation calculation relevant parameter in Customizing.
- You made mass changes that you programmed yourself and these changes affected data relevant to depreciation

Procedure

To execute this activity, run the processes in the Recalculating Values section (in Month-End Closing) in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Asset Revaluation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can revaluate single assets as part of your periodic business. Starting with the 2408 release, there’s a new revaluation app that provides users more flexibility when revaluing an asset. The Post Asset Revaluation (F7775) app offers users the capability of selecting individual parameters such as debit or credit along with the year of acquisition. By providing users individual selection, the new app is more flexible and multifunctional.

The local or corporate accounting principle determines if revaluation is allowed. For example, corporate accounting ledger IFRS (ledger 2L) allows revaluation while USGP (ledger 3L) doesn’t.

Prerequisites

Use an existing asset in any asset class that has acquisition postings. If no suitable asset exists, you must create asset master data. To perform this activity, run the processes in the Create Asset - MDS (BNI) master data script, using the master data from this document. Post the acquisition costs to the asset using the  Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Asset Revaluation (F7775). |  |  |
| 3 | General | Choose the General Information tab. |  |  |
| 4 | General information | Make the following entries:Company Code: 3310Main Asset Number: <Your asset number>Asset subnumber: <Your asset subnumber>Journal Entry Date: <Your document date, for example, today>Posting Date: <Your document date, for example, today>Asset Value Date: <Your value date, for example, today> |  |  |
| 5 | Posting Information | Choose the Posting information tab. |  |  |
| 6 | Posting information | Make the following entries:Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Depreciation Area: <empty for all depreciation areas or depreciation areas based on ledger selection.>Caution If you don't enter a depreciation area, all depreciation areas assigned to ledger 0L are posted to. The revaluation process isn't open for all depreciation areas.Debit/Credit Code : <Revaluation (Debit) or Revaluation (Credit)>Note Revaluation debits increase the value of the asset and credits decrease the asset value.Year of Acquisition: <Current Year or Prior Year>Note The fields available for entry differ depending on the chosen year.Current Year – Revaluation Amount for APC and Revaluation of Current Year Depreciation.Prior Year – Revaluation Amount for APC, Revaluation of Current Year Depreciation and Revaluation of Prior Year DepreciationRevaluation Amount for APC: 1000Revaluation of Current Year Depreciation <Your amount>Revaluation of Prior Year Depreciation <Your amount>Note This field only appears when Year of Acquisition Prior Year is selected. |  |  |
| 7 | Simulate Document | Choose Simulate. | The revaluation is simulated.The entered document can be simulated for every ledger and depreciation area and for all ledgers and depreciation areas depending on your selections. |  |
| 8 | Post Document | Choose Post. | The Information dialog box displays the new document number. |  |

### Closings

#### Manage Depreciation Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a depreciation run in asset accounting as part of your periodic business.

Procedure

To execute this activity, run the processes in the Manage Depreciation Run section in the Asset Accounting (J62) test script, using the master data from this document.

#### Depreciation Lists - Year End Closing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a report displaying all depreciation posted in asset accounting as part of your periodic business.

Procedure

To execute this activity, run the processes in the Depreciation Lists (under Year End Closing) section in the Asset Accounting (J62) test script, using the master data from this document.

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
> Flagged while digesting this document, not verified: Ledger mapping is described inconsistently: the Purpose note says IFRS is on 0L (local on 2L) after a ledger switch, while sample data and the revaluation section treat 2L as IFRS and 3L as USGP; may differ from other test scripts in the set.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/sap-fiori-analytical-apps-for-asset-accounting-in-finance-2qy-853]]
- related-to :: [[03-financial-accounting-and-close/test-script-asset-accounting-group-ledger-us-gaap-33f-ae-898]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GB_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 55,977 chars in the whole document
