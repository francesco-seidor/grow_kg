---
id: 03-financial-accounting-and-close/test-script-asset-accounting-additional-depreciation-area-5hg-ae-1095
title: "Test Script: Asset Accounting – Additional Depreciation Area (5HG_AE) (5HG_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (scope item 5HG_AE, UAE/AED) for the optional additional depreciation area in Asset Accounting: prerequisites and test procedures."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/asset-accounting-acquisition-to-year-end]
aliases: [5HG_S4CLD2608_BPD_EN_AE]
keywords: ["Asset Accounting: Acquisition to Year-End Close", additional depreciation area, asset accounting test script, legacy asset transfer, legacy data transfer date, business roles, asset master data, asset acquisition, asset retirement, asset valuation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HG_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1095
topic: 03-financial-accounting-and-close/asset-accounting-acquisition-to-year-end
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Asset Accounting – Additional Depreciation Area (5HG_AE) (5HG_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HG_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Asset Accounting: Acquisition to Year-End Close** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Asset Accounting – Additional Depreciation Area (5HG_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232856967)

[2 Prerequisites 5](#_Toc232856968)

[2.1 System Access 5](#_Toc232856969)

[2.2 Roles 5](#_Toc232856970)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232856971)

[2.4 Business Conditions 7](#_Toc232856972)

[2.5 Preliminary Steps 9](#_Toc232856973)

[2.5.1 Validate Asset Accounting System Readiness 9](#_Toc232856974)

[2.5.1.1 Confirm Takeover Date Information 9](#_Toc232856975)

[2.5.1.2 Confirm Run of Balance Carryforward for Current Fiscal Year 10](#_Toc232856976)

[2.5.2 Create Asset Master Record for Legacy Asset 11](#_Toc232856977)

[2.5.3 Post Transfer Values for Legacy Asset 13](#_Toc232856978)

[2.5.4 Activate Direct Posting to Asset 15](#_Toc232856979)

[2.5.5 Asset Revaluation Index (Optional) 16](#_Toc232856980)

[2.5.5.1 Maintain Asset Revaluation Index 16](#_Toc232856981)

[2.5.5.2 Assign Asset Revaluation Index in Asset Master Data 17](#_Toc232856982)

[2.5.5.3 Assign Asset Revaluation Index - View Results 18](#_Toc232856983)

[3 Overview Table 19](#_Toc232856984)

[4 Test Procedures 22](#_Toc232856985)

[4.1 Master Data 22](#_Toc232856986)

[4.1.1 Create Asset Master 22](#_Toc232856987)

[4.1.2 Change Asset 23](#_Toc232856988)

[4.1.3 Display Asset 23](#_Toc232856989)

[4.1.4 Block Assets 23](#_Toc232856990)

[4.1.5 Delete Asset 24](#_Toc232856991)

[4.1.6 Create Asset Subnumber 24](#_Toc232856992)

[4.1.7 Change Documents for Asset Master Record 24](#_Toc232856993)

[4.1.8 Asset Values 25](#_Toc232856994)

[4.1.9 Maintain Number of Units for Unit of Production Depreciation 25](#_Toc232856995)

[4.2 Acquisition 26](#_Toc232856996)

[4.2.1 Post Acquisition (Integrated AP) Without Purchase Order 26](#_Toc232856997)

[4.2.2 Post Asset Acquisition 26](#_Toc232856998)

[4.2.3 Post Credit Memo - in Year of Invoice 27](#_Toc232856999)

[4.2.4 Post Credit Memo After Year of Invoice 28](#_Toc232857000)

[4.2.5 Post Quantity Adjustment 28](#_Toc232857001)

[4.3 Retirement 29](#_Toc232857002)

[4.3.1 Post Retirement (Integrated AR) with Customer 29](#_Toc232857003)

[4.3.2 Post Retirement with Revenue 30](#_Toc232857004)

[4.3.3 Post Retirement Without Revenue 30](#_Toc232857005)

[4.4 Valuation (Transfer and Manual Value Correction) 31](#_Toc232857006)

[4.4.1 Reverse Journal Entry (Asset Accounting-Specific) 31](#_Toc232857007)

[4.4.2 Post Transfer Within Company Code 32](#_Toc232857008)

[4.4.3 Post Post-Capitalization 33](#_Toc232857009)

[4.4.4 Post Write-Up 33](#_Toc232857010)

[4.4.5 Post Depreciation Manually - Unplanned and Planned 34](#_Toc232857011)

[4.4.6 Recalculating Values 35](#_Toc232857012)

[4.4.7 Depreciation Forecast 35](#_Toc232857013)

[4.5 Month End Closing 37](#_Toc232857014)

[4.5.1 Manage Depreciation Run 37](#_Toc232857015)

[4.5.2 Asset Balances 37](#_Toc232857016)

[4.5.3 Asset Transactions 38](#_Toc232857017)

[4.5.4 Depreciation Lists 38](#_Toc232857018)

[4.5.5 Asset Values 39](#_Toc232857019)

[4.6 Year End Closing 39](#_Toc232857020)

[4.6.1 Asset History Sheet 39](#_Toc232857021)

[4.6.2 Depreciation Lists 40](#_Toc232857022)

[4.6.3 Year-End Closing 40](#_Toc232857023)

[4.6.4 Year-End Closing Asset Accounting (Cross-Company Code and Ledgers) 41](#_Toc232857024)

[4.6.5 Undo Year-End Closing 42](#_Toc232857025)

[5 Appendix 43](#_Toc232857026)

[5.1 Post Acquisition (Integrated AP) Without Purchase Order - MIRO 43](#_Toc232857027)

[5.2 Disable Period Check for Material Master (Optional) 45](#_Toc232857028)

## Purpose

Overview

This scope item is optional.

Some local or industry-specific rules (for example, for utility companies) may contain specific rules for depreciation and reporting. Companies may need to report insurance values to insurers for high-valued assets. To fulfill these requirements, you can activate this scope item. The scope item provides preconfigured content such as a specific valuation view and specific depreciation terms at the accounting principle level and valuation view level for asset classes.

An additional depreciation area is added when you activate the scope item. This depreciation area is for Asset Accounting purposes only and it contains statistical postings. You can define the depreciation parameters for depreciation key, useful life, and maximum amount for low-value assets for assets in this depreciation area.

|  |
| --- |
| Note If you activated the feature toggle for the new design, use the Depreciation Profile field in all procedures instead of Depreciation Key. |

|  |
| --- |
| Note The additional depreciation area can only be activated during initial activation, meaning that the Asset Accounting – Additional Depreciation Area (5HG) scope item is unavailable for subsequent scoping selections. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Purchasing Manager | SAP_BR_PURCHASING_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Manager - Procurement | SAP_BR_MANAGER_PROCUREMENT | My Inbox / My Inbox - Buying | SAP_CORE_SPT_MYINBOX_PC / SAP_MM_SPT_BUYING_MYINBOX_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Chart of Depreciation | 3310 |  |  |
| Asset Class | Any available asset class (such as 1000, 1100, 1200, 1500, 3000). If a special asset class is required, the Procedure section of each step mentions it. |  |  |
| Asset | Any available asset master |  | If no asset master is available in your system yet, create an asset master. If a special asset is required, see Procedures for each process step. |
| Vendor | Any domestic vendor | For example: 33300001 | If no vendor is available in your system yet, create a domestic vendor. Ensure complete name, address, postal code, and country is entered. |
| Customer | Any domestic customer | For example, 33100001 | If no customer is available in your system yet, create a domestic customer. Ensure complete name, address, postal code, and country is entered. |
| Cost Center | Any cost center |  | If no cost center is available in your system yet, create a cost center. |
| Ledger | 0L |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |
| BNI | Create Asset - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

|  |
| --- |
| Note This test script is relevant for systems in which additional depreciation area 16 - Customer specific purpose is activated. |

| Scope Item | Business Condition |
| --- | --- |
| BNI - Create Asset - MDS | During the execution of this scope item, asset master records are created for assets under construction and the assets to which final settlement is performed. To create the assets, use the master data script Create Asset - MDS (BNI) using the data described in this test script. |
| J45 - Procurement of Direct Materials | Must be run before this test script. Invoices are created and posted to accounting. |

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

#### Create Asset Master Record for Legacy Asset

Purpose

In this activity, you can create legacy assets with values. These assets may be used for various testing scenarios.

Prerequisites

To take over your legacy data in asset accounting, only one fiscal year can be open. If you receive an error stating that more than one year is open, check that the previous fiscal year is closed in asset accounting. To check, use the Make Company Code Settings - Asset Accounting-Specific (F7312) app. For your company code, the previous fiscal year must be closed.

Procedure

|  |
| --- |
| Note Create five legacy assets with different descriptions. Ensure that the asset description begins with the word Legacy. |

Table 2: Create Asset Master Record for Legacy Asset

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

#### Post Transfer Values for Legacy Asset

Purpose

In this activity, you post the transfer values for the legacy assets.

Prerequisites

To take over your legacy data in asset accounting, only one fiscal year is open. If an error states that more than one year is open, check that the previous fiscal year is closed in asset accounting. To check, use the Make Company Code Settings - Asset Accounting-Specific (F7312) app. Ensure that the previous fiscal year is closed for your company code.

Procedure

Table 3: Post Transfer Values for Legacy Asset (Accumulated APC and Accumulated Depreciation)

| Process Step | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log into the SAP Fiori launchpad as an Asset Accountant . |  |  |
| 2 | Access the SAP Fiori app | Open Post Transfer Values - For Legacy Asset (ABLDT) . | The Create General Header Data for Posting box is displayed. |  |
| 3 | Enter the Company and Legacy Asset | Make the following entries and choose Continue:Company Code: For example, 3310Asset: For example, xxxxxx |  |  |
| 4 | Enter values for Legacy Asset | Based on the ledger selection, the assigned depreciation areas are listed.If you select the Calculate Currencies checkbox, the values entered for company code currency are translated into the group currency using the exchange rate available in the system. These settings are recommended for testing purposes.If you need to manually maintain currency conversion due to different exchange rates, don't select the Calculate Currencies checkbox. Enter the values for group currency manually in the Amount in Global Currency column.On the Cumulated Values tab, enter values for the following lines for Amount in Company Code currency:Ledger 0L:Depreciation area 0107000 Cumulative Acquisition Costs: 3600.00 AED07005 Cumulative Ordinary Depreciation: -900.00 AEDLedger 0L:Depreciation area 1507000 Cumulative Acquisition Costs: 3600.00 AED07005 Cumulative Ordinary Depreciation: -900.00 AEDLedger 2L:Depreciation area 3207000 Cumulative Acquisition Costs: 3600.00 AED07005 Cumulative Ordinary Depreciation: -900.00 AEDNote The depreciation amounts in the bulleted lists above should be entered as negative amounts.Note Enter values for each depreciation area. | The Enter Asset Transaction Legacy Data view is displayed. The following tabs are available:Cumulated Values - The relevant amounts for APC, Ordinary Depreciation, Special Depreciation, and other items are required when the date for Legacy Transfer Segment is the end of the previous year.Posted Values - The relevant amounts for Ordinary Depreciation, Special Depreciation, and other items are required for cases where the date for Legacy Transfer Segment is during the current year. In this case, the last period for depreciation run should be entered in addition to the depreciation amount posted for current year.Bypass the warning Posting will take place in an earlier fiscal year.If any errors are RED coded, correct these before posting. |  |
| 5 | Post Legacy Asset Transaction | Choose Post.Choose Continue. | Note Document number for each accounting principle:AE AP _________IFRS _________USGP _______ |  |

#### Activate Direct Posting to Asset

Purpose

To use the Create Supplier Invoice - Advanced (MIRO) app (or the Create Supplier Invoice (F0859) app) to post to assets in the Post Acquisition (Integrated AP) Without Purchase Order procedure step, you must first activate direct posting to assets.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Sourcing and Procurement

Sub Application Area: Invoice Processing

1. For the row with Item Name of Incoming Invoice, choose Details (>).
2. For the Activate Direct Posting to G/L & Material Accounts & Assets row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Direct Posting to G/L & Material Accounts & Assets.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Activate Direct Posting | Select the Dir. posting to asset = active checkbox. |  |  |
| 2 | Save | Choose Save. |  |  |

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

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 4: Master Data

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Asset Master](#unique_16) [page ] 22 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. | The asset master record is created. The system message confirms creation and displays the new asset number. |
| [Change Asset](#unique_17) [page ] 23 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. | Asset master changes are saved. |
| [Display Asset](#unique_18) [page ] 23 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. | The Asset Explorer screen displays all asset values for each existing depreciation area. |
| [Block Assets](#unique_19) [page ] 23 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. | Asset is locked against further acquisitions. |
| [Delete Asset](#unique_20) [page ] 24 | Asset Accountant | See the Create Asset - MDS (BNI) scope item.Only assets without capitalization date and without values can be deleted directly | Asset master record has been deleted |
| [Create Asset Subnumber](#unique_21) [page ] 24 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. | The asset master subnumber is created.Subnumbering starts with 1. |
| [Change Documents for Asset Master Record](#unique_22) [page ] 24 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. |  |
| [Asset Values](#unique_23) [page ] 25 | Asset Accountant | Manage Fixed Assets (F3425A) | The Asset Explorer view displays. |
| [Maintain Number of Units for Unit of Production Depreciation](#unique_24) [page ] 25 | Asset Accountant | Maintain Number of Units - For UoP Depreciation (F4907)Manage Fixed Assets (F3425A) | You maintained the number of units for UoP Depreciation. |

Table 5: Acquisition

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Post Acquisition (Integrated AP) Without Purchase Order](#unique_25) [page ] 26 | Asset Accountant | Create Supplier Invoice (F0859) | You posted an asset acquisition without purchase order directly against a vendor as part of your daily business. |
| [Post Asset Acquisition](#unique_26) [page ] 26 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | You posted the asset acquisition. |
| [Post Credit Memo - in Year of Invoice](#unique_27) [page ] 27 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | You posted a credit memo in the year of invoice. |
| [Post Credit Memo After Year of Invoice](#unique_28) [page ] 28 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | You posted a credit memo after the year of invoice. |
| [Post Quantity Adjustment](#unique_29) [page ] 28 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | You posted a quantity adjustment. |

Table 6: Retirement

| Process Step | Business Role | Transaction / App | Expecte |
| --- | --- | --- | --- |
| [Post Retirement (Integrated AR) with Customer](#unique_30) [page ] 29 | Asset Accountant | Post Retirement (Integrated AR) - With Customer (F-92) | You posted a retirement from asset sale directly against a customer. |
| [Post Retirement with Revenue](#unique_31) [page ] 30 | Asset Accountant | Post Asset Retirement (F7107) | You posted a retirement from asset sale directly against a clearing account. |
| [Post Retirement Without Revenue](#unique_32) [page ] 30 | Asset Accountant | Post Asset Retirement (F7107) | You posted an asset retirement via scrapping. |

Table 7: Valuation (Transfer and Manual Value Correction)

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Reverse Journal Entry (Asset Accounting-Specific)](#unique_33) [page ] 31 | Asset Accountant | Manage Fixed Assets (F3425A) | The journal entry is reversed. |
| [Post Transfer Within Company Code](#unique_34) [page ] 32 | Asset Accountant | Post Asset Transfer (F9302) | You performed a transfer from one asset master data record to another asset master within the same company code. |
| [Post Post-Capitalization](#unique_35) [page ] 33 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | You entered a post-capitalization for an asset master data record. |
| [Post Write-Up](#unique_36) [page ] 33 | Asset Accountant | Post Writeup (ABZU) | You posted a write-up for an asset master data record. |
| [Post Depreciation Manually - Unplanned and Planned](#unique_37) [page ] 34 | Asset Accountant | Post Depreciation Manually - Unplanned and Planned (ABAAL) | You manually entered unplanned depreciation amount to be posted within the next depreciation run. |
| [Recalculating Values](#unique_38) [page ] 35 | Asset Accountant | Schedule Asset Accounting Jobs (F1914) | You recalculated values. |
| [Depreciation Forecast](#unique_39) [page ] 35 | Asset Accountant | See Procedure section in the test procedure topic. | You forecasted depreciation. |

Table 8: Month-End Closing

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Manage Depreciation Run](#unique_40) [page ] 37 | Asset Accountant | Schedule Asset Accounting Jobs (F1914) | You created a depreciation run. |
| [Asset Balances](#unique_41) [page ] 37 | Asset Accountant | Asset Balances (FAA_FPM_OVP_ASTBAL) | You created an Asset Balances report. |
| [Asset Transactions](#unique_42) [page ] 38 | Asset Accountant | Asset Transactions (F1614) | You created a report showing all transactions posted in asset accounting. |
| [Depreciation Lists](#unique_43) [page ] 38 | Asset Accountant | Depreciation Lists (F1616) | You created a report displaying all deprecation posted to asset accounting. |
| [Asset Values](#unique_44) [page ] 39 | Asset Accountant | Manage Fixed Assets (F3425A) | You displayed relevant values for an asset master data record. |

Table 9: Year-End Closing

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Asset History Sheet](#unique_45) [page ] 39 | Asset Accountant | Asset History Sheet (FIS_FPM_OVP_AA_AHS) | You created an Asset History report. |
| [Depreciation Lists](#unique_46) [page ] 40 | Asset Accountant | Depreciation Lists (F1616) | You created an Asset Total Depreciation report. |
| [Year-End Closing](#unique_47) [page ] 40 | Asset Accountant | Make Company Code Settings - Asset Accounting Specific (F7312) | You performed year-end closing. |
| [Year-End Closing Asset Accounting (Cross-Company Code and Ledgers)](#unique_48) [page ] 41 | Asset Accountant | Schedule Asset Accounting Jobs (F1914) | You performed year-end closing for asset accounting. |
| [Undo Year-End Closing](#unique_49) [page ] 42 | Asset Accountant | Make Company Code Settings - Asset Accounting Specific (F7312) | You undid the year-end closing. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Master Data

#### Create Asset Master

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create a new asset main data record as part of your daily business.

Procedure

To execute this activity, run the processes in the Create Asset section in the Create Asset - MDS(BNI) Master Data Script, using the master data from this document.

|  |
| --- |
| Note In the Manage Fixed Assets (F3425A) app, in the asset worklist, you have additional options under the Post button that direct you to the following apps:Post Asset Acquisition - And Quantity Adjustment (F6488)Used for Post transfer values for legacy assets, Post Acquisition, Post Post-Capitalization, Post Credit Memo, and Post Quantity AdjustmentPost Asset Retirement (F7107)Used for Post Retirement - Retirement with Revenue and Post Retirement - Retirement Without RevenuePost Asset Transfer (F9302)Post Transfer (ABT1N)Post Miscellaneous Transactions (ABSOL)Select an asset from the worklist and choose the appropriate app under the Post button to go to that app for the selected asset. |

#### Change Asset

Purpose

In this activity, you can change an existing asset data record (main or subnumber) as part of your daily business.

Procedure

To execute this activity, run the processes in section Change Asset in the Create Asset - MDS(BNI) Master Data Script, using the master data from this document.

|  |
| --- |
| Note In the Change Asset: Master Data view, change in depreciation area 16.Depreciation Area 16:Choose Depreciation area: 16.Choose Area-06.Choose More Interval.Choose Add Interval.For the new interval, enter the From Date and choose YES.Enter a change on the specific line item and choose Save. The system display a success message. |

#### Display Asset

Purpose

In this activity, you can display an existing asset data record (main or subnumber) as part of your daily business.

Procedure

To execute this activity, run the processes in the Display Asset task in the Create Asset - MDS (BNI) master data script, using the master data from this document.

#### Block Assets

Purpose

In this activity, you can lock an existing asset master data record (main or subnumber) for further acquisitions.

Procedure

To execute this activity, run the processes in section Block Assets in the Create Asset - MDS(BNI) Master Data Script, using the master data from this document.

#### Delete Asset

Purpose

In this activity, you can delete an existing asset master data record (main or subnumber).

Procedure

To execute this activity, run the processes in section Delete Asset in the Create Asset - MDS(BNI) Master Data Script, using the master data from this document.

#### Create Asset Subnumber

Purpose

In this activity, you create a new asset master subnumber data record as part of your daily business.

Procedure

To execute this activity, run the processes in the Create Asset Subnumber section in the Create Asset - MDS(BNI) Master Data Script, using the master data from this document.

#### Change Documents for Asset Master Record

Purpose

In this activity, you can display all past changes of an existing asset master data record (main or subnumber).

Procedure

To execute this activity, run the processes in Change Documents for Asset Master Record in the Create Asset - MDS(BNI) Master Data Script, using the master data from this document.

#### Asset Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can directly display all relevant values for an asset master record (main or subnumber) as part of your daily business.

Procedure

To execute this activity, run the processes in the Asset Values section in the Asset Accounting (J62) test script, using the master data from this document.

#### Maintain Number of Units for Unit of Production Depreciation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you maintain the number of units for Unit of Production (UoP) depreciation.

Procedure

To execute this activity, run the processes in the Maintain Number of Units for Unit of Production Depreciation section in the Asset Accounting (J62) test script, using the master data from this document.

### Acquisition

#### Post Acquisition (Integrated AP) Without Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter a supplier invoice for asset acquisition without reference to a purchase order.

|  |
| --- |
| Note By default, the system checks if the corresponding period is open for posting a supplier invoice. To deactivate the period check for material master records, perform the [Disable Period Check for Material Master (Optional)](#unique_51) [page ] 45 step in the Appendix.If you deactivate the period check, the system no longer performs the check for G/L account postings and postings to assets. However, the check still takes place for direct postings to the material and for invoices with purchase order reference. |

|  |
| --- |
| Note The Create Supplier Invoice (F0859) app is used for simpler supplier invoices and the Create Supplier Invoice - Advanced (MIRO) app is used for more complex supplier invoices. To see a comparison, see [Feature Comparison for Managing Supplier Invoices and Creating Supplier Invoices (Advanced)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/c7c55da4af0a49d08d7df04fc5b39138.html?version=latest). |

Procedure

To execute this activity, run the processes in the Post Acquisition (Integrated AP) Without Purchase Order section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Asset Acquisition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can post an asset acquisition without purchase order automatically against a clearing account as part of your daily business. No vendor is involved.

Prerequisites

To execute this activity, run the processes in the Create Asset - MDS(BNI) Master Data Script, using the master data from this document.

Procedure

To execute this activity, run the processes in the Post Asset Acquisition section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Credit Memo - in Year of Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can post an asset credit memo in the acquisition year automatically against a clearing account as part of your daily business (main or subnumber). No vendor is involved.

Prerequisites

To execute this activity, run the processes in the Create Asset(BNI) Master Data Script, using the master data from this document. Then, post acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app .

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

In this activity, you can post an asset credit memo later than in the acquisition year automatically against a clearing account as part of your daily business (main or subnumber). No vendor is involved.

This can be applied to post-capitalized assets.

Prerequisites

To execute this activity, run the processes in the Create Asset - MDS (BNI) Master Data Script, using the master data from this document.

This transaction is normally used with an asset that was acquired in a prior fiscal year (meaning that the capitalization date of the asset is in a prior year). If you can’t create a post-capitalized asset with a posting date in a prior fiscal year because the prior year is closed, test the transaction with an asset acquired in the current fiscal year. You should then use a posting date in the next fiscal year. Before proceeding, make sure that the next fiscal year is open for posting by executing the Schedule General Ledger Jobs - Carry Forward Balances step in the Appendix section of the Accounting and Financial Close (J58) test script.

Procedure

To execute this activity, run the processes in the Post Credit Memo After Year of Invoice section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Quantity Adjustment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post a quantity adjustment to an asset.

Procedure

To execute this activity, run the processes in the Post Quantity Adjustment section in the Asset Accounting (J62) test script, using the master data from this document.

### Retirement

#### Post Retirement (Integrated AR) with Customer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can post a retirement from asset sale directly against a customer as part of your daily business (main or subnumber).

Prerequisites

To execute this activity, run the processes in the Create Asset - MDS(BNI) Master Data Script, using the master data from this document. When that process is completed, post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

To execute this activity, run the processes in the Post Retirement (Integrated AR) with Customer section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Retirement with Revenue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can post a retirement from asset sale automatically against a clearing account as part of your daily business (main or subnumber). No customer is involved. If necessary, you can designate an accounting principle in the transaction to post the retirement to a specific ledger.

Prerequisites

Use an existing asset in any asset class (except 4000, 4001, 4010, or 4011) that has acquisition postings. If no suitable asset exists, you must create asset master data.

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

In this activity, you can post an asset retirement by scrapping as part of your daily business (main or subnumber).

Prerequisites

Use an existing asset in any asset class except 4001 that has acquisition postings. If no suitable asset exists, then, you must create asset master data.

To execute this activity, run the processes in the Create Asset (BNI) Master Data Script, using the master data from this document. After completing that process, post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

To execute this activity, run the processes in the Post Retirement Without Revenue section in the Asset Accounting (J62) test script, using the master data from this document.

### Valuation (Transfer and Manual Value Correction)

#### Reverse Journal Entry (Asset Accounting-Specific)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can cancel documents posted in asset accounting as part of your daily business.

Prerequisites

Use an existing asset in any asset class that has acquisition postings. If no suitable asset exists, you must create asset master data.

To execute this activity, run the processes in the Create Asset - MDS (BNI) master data script, using the master data from this document. Post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

|  |
| --- |
| Caution You can’t reverse documents posted from Materials Management with the Manage Fixed Assets (F3425A) app. To reverse those documents, use the Supplier Invoices List (F1060A) app. |

Procedure

To execute this activity, run the processes in the Reverse Journal Entry (Asset Accounting-Specific) section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Transfer Within Company Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can carry out a transfer from one asset master data record to another asset master within the same company code as part of your daily business.

|  |
| --- |
| Note Intra-company transfers are used to correct wrong account assignments like asset class. |

Prerequisites

Use an existing asset in any asset class except 4001 and 4011 that has acquisition postings. If no suitable asset exists, you must create asset master data.

To execute this activity, run the processes in the Create Asset - MDS (BNI) scope item, using the master data from this document. Then post acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

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

In this activity, you can enter a post-capitalization for an asset master data record.

Post-capitalization represents subsequent corrections to the acquisition and production costs (APC) of a fixed asset. An example of when you need this type of correction is if you neglected to add expenditures and costs linked with the acquisition or assembly of an asset to its APC in a past fiscal year.

In this example, a new asset master record is created as a prerequisite to be used in the post-capitalization. However, post capitalization can also be performed on an existing asset.

Procedure

To execute this activity, run the processes in the Post Post-Capitalization section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Write-Up

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can post a write-up for an asset master data record.

A write-up is understood to be a subsequent change to the valuation of an asset (reversal of depreciation). Write-ups increase the book value of a fixed asset. When used with a depreciation method based on the net book value, write-ups increase the planned depreciation. During a fiscal year change, the write-ups posted up to end of the year are balanced with the depreciation amounts.

Prerequisite

Write-ups can only be created for depreciation in the past (that is, depreciation from previous years). Various standard transaction types are configured for write-ups. These transaction types differ according to the depreciation type to be corrected (for example, ordinary depreciation or unplanned depreciation) and the depreciation areas to be posted (for example, book depreciation only).

In the following procedure, the ordinary depreciation is corrected for all the managed depreciation areas as an example.

Use an existing asset in any asset class that has acquisition postings for previous years. You can use an asset master data record created for Legacy Data Transfer and for which values are posted. If no suitable asset exists, create the asset master data with the Manage Legacy Assets (F7280A) app, then post the values for this asset using the Post Transfer Values - For Legacy Asset (ABLDT) app.

Procedure

To execute this activity, run the processes in the Post Write-Up section in the Asset Accounting (J62) test script, using the master data from this document.

#### Post Depreciation Manually - Unplanned and Planned

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can manually enter unplanned depreciation amount to be posted within the next depreciation run.

Prerequisites

Use an existing asset in any asset class that has acquisition postings. If no suitable asset exists, then: Create Asset Master Data.

To execute this activity, run the processes in the Create Asset - MDS (BNI) Master Data Script, using the master data from this document. Assign the asset master data used in this process to depreciation key MANU (Manual depreciation only). Then, post the acquisition costs to the asset using the app Post Asset Acquisition - And Quantity Adjustment (F6488).

|  |
| --- |
| Note If you activated the feature toggle for the new design, instead of Deprecation Key MANU, use Depreciation Profile 00_MANUAL instead. |

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

In this activity, you recalculate the depreciation of an asset master data record. Recalculation may be necessary if there's a configuration change to the depreciation keys or terms. Changing the depreciation key or useful life on the asset master doesn't usually require recalculation, because the system automatically adjusts the planned depreciation at the time of the change. Nevertheless, it's a best practice to include this as part of your periodic processing to ensure G/L and fixed assets are in balance. Because no configuration changes are made in this test script, you can expect the detail log to be empty.

|  |
| --- |
| Note If you activated the feature toggle for the new design, use the Depreciation Profile field instead of the Depreciation Key field. |

Prerequisites

You may need to recalculate planned annual depreciation in certain company codes or for individual fixed assets. This may be necessary if:

- You've changed the depreciation calculation relevant parameter in Customizing.
- You've made mass changes that you programmed yourself and these changes affected data relevant to depreciation.

Procedure

To execute this activity, run the processes in the Recalculating Values section in the Asset Accounting (J62) test script, using the master data from this document.

#### Depreciation Forecast

Use

In this activity, the planning horizon serves as a reference for calculating planned depreciation. You can define the planning horizon for up to five years. Asset Accounting reporting considers the planning horizon and enables the evaluation of planned values in reports.

Enter the number of years for which the system should calculate and update planned values. If you don't want the planned values to be updated, enter zero years. This corresponds with the standard setting. In this case, the evaluation of planned depreciation is possible only until the end of the current fiscal year. If you want the planned values to be updated, enter a value from one through five.

Dependencies

To change entries for the planning horizon, consider the following:

- If you define a planning horizon (a number from one through five), you must manually recalculate the depreciation for the depreciation areas belonging to the ledger in the company code. The planned values for the planning horizon are then available in reporting.
- If you later increase the number of years (for example, from three years to five years), you must recalculate depreciation.
- To deactivate the planned value calculation, enter zero. The system deletes the existing planned values for the following years in the current fiscal year from the database after you confirm this in the dialog box.
- To decrease the number of years, enter the new number. The system deletes the existing planned values from the database accordingly after you confirm this in the dialog box.

Prerequisites

1. Log on to SAP Fiori Launchpad as an Asset Accountant.
2. Open Make Company Code Settings - Asset Accounting-Specific (F7312).
3. Enter your company code in the filter area and choose Go.
4. Select your company code from the table.
5. On the next view, choose Edit.
6. On the Ledger Settings tab, make the following entries:

Planning Horizon: <number from 1 through 5 for years to forecast>

1. Save your changes.

Procedure

Planned values are visible in following reports:

| Report | For more information |
| --- | --- |
| Asset History Sheet (Key Figure Group – AHS_PLAN) | See the Year End Closing section of the Asset Accounting (J62) test script |
| Asset Balances (Key Figure Group – ABS_DEF or DEPR_TOTAL) | See the Month End Closing section of the Asset Accounting (J62) test script |
| Depreciation List | See the Month End Closing section of the Asset Accounting (J62) test script |

### Month End Closing

#### Manage Depreciation Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create a depreciation run in asset accounting as part of your periodical business.

Procedure

To execute this activity, run the processes in the Manage Depreciation Run section in the Asset Accounting (J62) test script, using the master data from this document.

#### Asset Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create an Asset Balances report according to your country/region requirements as part of your year-end close in asset accounting.

Procedure

To execute this activity, run the processes in the Asset Balances section in the Asset Accounting (J62) test script, using the master data from this document.

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

Procedure

To execute this activity, run the processes in the Asset Transactions section in the Asset Accounting (J62) test script, using the master data from this document.

#### Depreciation Lists

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create a report displaying all depreciation posted in asset accounting as part of your periodic processing business.

Procedure

To execute this activity, run the processes in the Depreciation Lists section in the Asset Accounting (J62) test script, using the master data from this document.

#### Asset Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can directly display all relevant values for an asset master record (main or subnumber) as part of your daily business.

Procedure

To execute this activity, run the processes in the Asset Values section in the Asset Accounting (J62) test script, using the master data from this document.

### Year End Closing

#### Asset History Sheet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create an asset history sheet report according to your country/region requirements as part of your year-end close in asset accounting.

Procedure

To execute this activity, run the processes in the Asset History Sheet section in the Asset Accounting (J62) test script, using the master data from this document.

#### Depreciation Lists

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create an Asset Total Depreciation report in asset accounting as part of your periodic processing.

Procedure

To execute this activity, run the processes in the Depreciation Lists section in the Asset Accounting (J62) test script, using the master data from this document.

#### Year-End Closing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create a year-end closing for asset accounting as part of your periodical business.

|  |
| --- |
| Caution Ensure all depreciation periods for the year are completed. |

|  |
| --- |
| Note If your implementation doesn't use a specific ledger, disregard that ledger. |

Procedure

To execute this activity, run the processes in the Year-End Closing topic in the Asset Accounting (J62) test script, using the master data from this document.

#### Year-End Closing Asset Accounting (Cross-Company Code and Ledgers)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can run a year-end closing for asset accounting as part of your periodical business. Several company codes and several ledgers are supported as selection criteria in the Year-End Closing Asset Accounting (Cross-Company Code and Ledgers) template.

|  |
| --- |
| Caution Ensure that all depreciation periods for the year are completed. If your implementation doesn't use a specific ledger, disregard that ledger. |

Procedure

To execute this activity, run the processes in the Year-End Closing Asset Accounting (Cross-Company Code and Ledgers) section in the Asset Accounting (J62) test script, using the master data from this document.

#### Undo Year-End Closing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can open a prior year for a company in asset accounting. This requires authorization and coordination with FI. Only perform this activity on an exception basis, as most companies don't allow opening of a prior year.

|  |
| --- |
| Note If your implementation doesn't use a specific ledger, disregard that ledger. |

|  |
| --- |
| Note If the prior year is opened, the prior year must be closed again. Typically, this would be done during a low peak time frame (for example: week end) |

Procedure

To execute this activity, run the processes in the Undo Year-End Closing section in the Asset Accounting (J62) test script, using the master data from this document.

## Appendix

### Post Acquisition (Integrated AP) Without Purchase Order - MIRO

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can post an asset acquisition without purchase order directly against a vendor as part of your daily business.

|  |
| --- |
| Note By default, the system checks if the corresponding period is open for posting a supplier invoice. To deactivate the period check for material master records, perform the [Disable Period Check for Material Master (Optional)](#unique_51) [page ] 45 step in the Appendix.If you deactivate the period check, the system no longer performs the check for G/L account postings and postings to assets. However, the check still takes place for direct postings to the material and for invoices with purchase order reference. |

|  |
| --- |
| Note The Create Supplier Invoice (F0859) app is used for simpler supplier invoices and the Create Supplier Invoice - Advanced (MIRO) app is used for more complex supplier invoices. To see a comparison, see [Feature Comparison for Managing Supplier Invoices and Creating Supplier Invoices (Advanced)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/c7c55da4af0a49d08d7df04fc5b39138.html?version=latest). |

Prerequisites

To execute this activity, run the processes in the Create Asset - MDS (BNI) Master Data Script, using the master data from this document.

To enable posting to assets, ensure that you've executed the [Activate Direct Posting to Asset](#unique_11) [page ] 15 preliminary step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Create Supplier Invoice - Advanced (MIRO). | The Create Supplier Invoice - Advanced screen displays. |  |
| 3 | Navigation | If the system prompts you, make the following entries and choose Continue:Company Code: 3310 |  |  |
| 4 | Basic data | On the Basic Data tab, enter the following data:Invoice Date: <Your document date, for example, today>Posting Date:Reference: <any><Your document date, for example, today>Amount: 1000.00Currency: AEDCalculate tax: SelectedTax code: <Input Tax Code> or <Input Tax Code> |  |  |
| 5 | Payment | In the Payment tab, enter the following data:BaselineDt: <Your document date, for example, today>Pyt Terms : 0001. |  |  |
| 6 | Details | In the Details tab, enter the following data:Inv. Party: 33300001 |  |  |
| 7 | Enter Asset Details | In the Asset section, make the following entries and press Enter:Asset: <Your asset number>Asset subnumber: <Your asset subnumber>Amount : 1000.00Quantity: Your quantity if required | All required entries are made. |  |
| 8 | Post Document | Choose Post. |  |  |
| 9 | Exit | To return to the SAP Fiori launchpad, choose Home. |  |  |

### Disable Period Check for Material Master (Optional)

Purpose

By default, the system checks if the corresponding period is open to post a supplier invoice. This activity disables the period check or material master records. Disabling the period check means that the system doesn't perform the check for G/L account postings and postings to assets. The check still occurs for direct postings to the material and for invoices that reference purchase orders.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Sourcing and Procurement

Sub Application Area: Invoice Processing

1. For the row with Item Name of Incoming Invoice, choose Details (>).
2. For the Disable Period Check for Material Master row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Disable Period Check for Material Master.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instructions | Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Disable Check | In the Disable MM Period Check pane, make the following entries:No Check: Selected |  |  |
| 2 | Save | Choose Save. | The period check is disabled. |  |

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
> Flagged while digesting this document, not verified: The takeover date note says the date is usually the prior year-end day, but its example says that in fiscal year 2025 legacy assets are loaded as of year end 2023 (not 2024); the example looks inconsistent with the rule.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/test-script-asset-accounting-j62-ae-sap-s-4hana-cloud-public-edition-1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5HG_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 79,727 chars in the whole document
