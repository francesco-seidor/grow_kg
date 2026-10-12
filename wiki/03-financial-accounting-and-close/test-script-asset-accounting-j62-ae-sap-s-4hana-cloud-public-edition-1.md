---
id: 03-financial-accounting-and-close/test-script-asset-accounting-j62-ae-sap-s-4hana-cloud-public-edition-1
title: "Test Script: Asset Accounting (J62_AE) - SAP S/4HANA Cloud Public Edition (J62_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item J62 Asset Accounting (UAE, company code 3310): prerequisites, legacy transfer, acquisition, retirement, valuation, month-end and year-end closing steps."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/asset-accounting-acquisition-to-year-end]
aliases: [J62_S4CLD2608_BPD_EN_AE]
keywords: ["Asset Accounting: Acquisition to Year-End Close", asset accounting, legacy data transfer, asset acquisition, asset retirement, asset valuation, month-end closing, year-end closing, depreciation run, asset master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J62_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1307
topic: 03-financial-accounting-and-close/asset-accounting-acquisition-to-year-end
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Asset Accounting (J62_AE) - SAP S/4HANA Cloud Public Edition (J62_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J62_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Asset Accounting: Acquisition to Year-End Close** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Asset Accounting (J62_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232863489)

[2 Prerequisites 5](#_Toc232863490)

[2.1 Roles 5](#_Toc232863491)

[2.2 System Access 6](#_Toc232863492)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232863493)

[2.4 Business Conditions 7](#_Toc232863494)

[2.5 Preliminary Steps 8](#_Toc232863495)

[2.5.1 Validate Asset Accounting System Readiness 8](#_Toc232863496)

[2.5.1.1 Confirm Takeover Date Information 8](#_Toc232863497)

[2.5.1.2 Confirm Run of Balance Carryforward for Current Fiscal Year 10](#_Toc232863498)

[2.5.2 Create Asset Master Record for Legacy Asset 11](#_Toc232863499)

[2.5.3 Post Transfer Values for Legacy Asset 12](#_Toc232863500)

[2.5.4 Activate Direct Posting to Asset 14](#_Toc232863501)

[2.5.5 Asset Revaluation Index (Optional) 15](#_Toc232863502)

[2.5.5.1 Maintain Asset Revaluation Index 15](#_Toc232863503)

[2.5.5.2 Assign Asset Revaluation Index in Asset Master Data 16](#_Toc232863504)

[2.5.5.3 Assign Asset Revaluation Index - View Results 17](#_Toc232863505)

[3 Overview Table 19](#_Toc232863506)

[4 Test Procedures 22](#_Toc232863507)

[4.1 Master Data 22](#_Toc232863508)

[4.1.1 Create Asset Master 22](#_Toc232863509)

[4.1.2 Change Asset 23](#_Toc232863510)

[4.1.3 Display Asset 24](#_Toc232863511)

[4.1.4 Block Assets 24](#_Toc232863512)

[4.1.5 Delete Asset 24](#_Toc232863513)

[4.1.6 Create Asset Subnumber 24](#_Toc232863514)

[4.1.7 Change Documents for Asset Master Record 25](#_Toc232863515)

[4.1.8 Asset Values 25](#_Toc232863516)

[4.1.9 Maintain Number of Units for Unit of Production Depreciation 26](#_Toc232863517)

[4.2 Acquisition 29](#_Toc232863518)

[4.2.1 Post Acquisition (Integrated AP) Without Purchase Order 29](#_Toc232863519)

[4.2.2 Post Asset Acquisition 31](#_Toc232863520)

[4.2.3 Post Credit Memo - in Year of Invoice 32](#_Toc232863521)

[4.2.4 Post Credit Memo After Year of Invoice 34](#_Toc232863522)

[4.2.5 Post Quantity Adjustment 36](#_Toc232863523)

[4.3 Retirement 37](#_Toc232863524)

[4.3.1 Post Retirement (Integrated AR) with Customer 37](#_Toc232863525)

[4.3.2 Post Retirement with Revenue 39](#_Toc232863526)

[4.3.3 Post Retirement Without Revenue 40](#_Toc232863527)

[4.4 Valuation (Transfer and Manual Value Correction) 42](#_Toc232863528)

[4.4.1 Reverse Journal Entry (Asset Accounting-Specific) 42](#_Toc232863529)

[4.4.2 Post Asset Transfer Within Company Code 44](#_Toc232863530)

[4.4.3 Post Post-Capitalization 45](#_Toc232863531)

[4.4.4 Post Write-Up 47](#_Toc232863532)

[4.4.5 Post Depreciation Manually - Unplanned and Planned 48](#_Toc232863533)

[4.4.6 Depreciation Forecast 50](#_Toc232863534)

[4.5 Month-End Closing 51](#_Toc232863535)

[4.5.1 Recalculating Values 51](#_Toc232863536)

[4.5.2 Manage Depreciation Run 53](#_Toc232863537)

[4.5.3 Asset Balances 55](#_Toc232863538)

[4.5.4 Asset Transactions 56](#_Toc232863539)

[4.5.5 Depreciation Lists 57](#_Toc232863540)

[4.5.6 Asset Values 58](#_Toc232863541)

[4.6 Year-End Closing 59](#_Toc232863542)

[4.6.1 Asset History Sheet 59](#_Toc232863543)

[4.6.2 Depreciation Lists 60](#_Toc232863544)

[4.6.3 Year-End Closing 62](#_Toc232863545)

[4.6.4 Year-End Closing Asset Accounting (Cross-Company Code and Ledgers) 63](#_Toc232863546)

[4.6.5 Undo Year-End Closing 64](#_Toc232863547)

[5 Appendix 66](#_Toc232863548)

[5.1 Post Acquisition (Integrated AP) Without Purchase Order - MIRO 66](#_Toc232863549)

[5.2 Disable Period Check for Material Master (Optional) 68](#_Toc232863550)

[5.3 Post Asset Transfer Within Company Code 69](#_Toc232863551)

## Purpose

Overview

Asset accounting, a subsidiary ledger of the general ledger, is used to manage and document fixed asset transactions in detail. In general ledger accounting, you update depreciation and changes to asset balance sheet values in asset accounting. You make various account assignments to cost accounting for these transactions. Because of the integration in SAP S/4HANA Cloud, public edition, Asset Accounting (FI-AA) transfers data directly to and from other components from SAP S/4HANA Cloud, public edition such as Financial Accounting (FI) components.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/J62_S4CLD2602_BPD_EN_AE.docx) ). |

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

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

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

Invoices to be paid must be available.

| Test Script/Scenario | Business Condition |
| --- | --- |
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

The scope item Asset Accounting consists of several process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 4: Master Data

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Create Asset Master](#unique_16) [page ] 22 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. | The asset master record is created. The system message confirms creation and displays the new asset number. (BNI) scope item. |
| [Change Asset](#unique_17) [page ] 23 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. | Asset master changes are saved. |
| [Display Asset](#unique_18) [page ] 24 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. | The Asset Explorer screen displays all asset values for each existing depreciation area. |
| [Block Assets](#unique_19) [page ] 24 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. | Asset is locked against further acquisitions. |
| [Delete Asset](#unique_20) [page ] 24 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. | Asset master record has been deleted |
| [Create Asset Subnumber](#unique_21) [page ] 24 | Asset Accountant | See the Create Asset - MDS BNI) scope item. | The asset master subnumber is created.Subnumbering starts with 1. |
| [Change Documents for Asset Master Record](#unique_22) [page ] 25 | Asset Accountant | See the Create Asset - MDS (BNI) scope item. |  |
| [Asset Values](#unique_23) [page ] 25 | Asset Accountant | Open Manage Fixed Assets (F3425A) | You displayed all relevant values for an asset master record. |
| [Maintain Number of Units for Unit of Production Depreciation](#unique_24) [page ] 26 | Asset Accountant | Maintain Number of Units - For UoP Depreciation (F4907)Open Manage Fixed Assets (F3425A) | You maintained the number of units for UoP Depreciation. |

Table 5: Acquisition

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Post Acquisition (Integrated AP) Without Purchase Order](#unique_25) [page ] 29 | Asset Accountant | Create Supplier Invoice (F0859) | You posted an asset acquisition without purchase order directly against a vendor as part of your daily business. |
| [Post Asset Acquisition](#unique_26) [page ] 31 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | You posted an asset acquisition without purchase order automatically against a clearing account as part of your daily business. No vendor is involved. |
| [Post Credit Memo - in Year of Invoice](#unique_27) [page ] 32 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | You posted an asset credit memo in the acquisition year automatically against a clearing account as part of your daily business. |
| [Post Credit Memo After Year of Invoice](#unique_28) [page ] 34 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | You posted an asset credit memo later than in the acquisition year automatically against a clearing account as part of your daily business. |
| [Post Quantity Adjustment](#unique_29) [page ] 36 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | You posted a quantity adjustment. |

Table 6: Retirement

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Post Retirement (Integrated AR) with Customer](#unique_30) [page ] 37 | Asset Accountant | Post Retirement (Integrated AR) - With Customer (F-92) | You posted a retirement from asset sale directly against a customer. |
| [Post Retirement with Revenue](#unique_31) [page ] 39 | Asset Accountant | Post Asset Retirement (F7107) | You posted a retirement from asset sale directly against a clearing account. |
| [Post Retirement Without Revenue](#unique_32) [page ] 40 | Asset Accountant | Post Asset Retirement (F7107) | You posted an asset retirement via scrapping. |

Table 7: Valuation (Transfer and Manual Value Correction)

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Reverse Journal Entry (Asset Accounting-Specific)](#unique_33) [page ] 42 | Asset Accountant | Manage Fixed Assets (F3425A) | The journal entry is reversed. |
| [Post Asset Transfer Within Company Code](#unique_34) [page ] 44 | Asset Accountant | Post Asset Transfer (F9302) | You performed a transfer from one asset master data record to another asset master within the same company code. |
| [Post Post-Capitalization](#unique_35) [page ] 45 | Asset Accountant | Post Asset Acquisition - And Quantity Adjustment (F6488) | You entered a post-capitalization for an asset master data record. |
| [Post Write-Up](#unique_36) [page ] 47 | Asset Accountant | Post Writeup (ABZU) | You posted a write-up for an asset master data record. |
| [Post Depreciation Manually - Unplanned and Planned](#unique_37) [page ] 48 | Asset Accountant | Post Depreciation Manually - Unplanned and Planned (ABAAL) | You manually entered unplanned depreciation amount to be posted within the next depreciation run. |
| [Depreciation Forecast](#unique_38) [page ] 50 | Asset Accountant | See Procedure section in the test procedure topic. | You forecasted depreciation. |

Table 8: Month-End Closing

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Recalculating Values](#unique_39) [page ] 51 | Asset Accountant | Schedule Asset Accounting Jobs (F1914) | You recalculated the depreciation of an asset master data record. |
| [Manage Depreciation Run](#unique_40) [page ] 53 | Asset Accountant | Schedule Asset Accounting Jobs (F1914) | You created a depreciation run. |
| [Asset Balances](#unique_41) [page ] 55 | Asset Accountant | Asset Balances (F1617) | You created an Asset Balances report. |
| [Asset Transactions](#unique_42) [page ] 56 | Asset Accountant | Asset Transactions (F1614) | You created a report showing all transactions posted in asset accounting. |
| [Depreciation Lists](#unique_43) [page ] 57 | Asset Accountant | Depreciation Lists (F1616) | You created a report displaying all depreciation posted to asset accounting. |
| [Asset Values](#unique_44) [page ] 58 | Asset Accountant | Open Manage Fixed Assets (F3425A) | You displayed relevant values for an asset master data record. |

Table 9: Year-End Closing

|  |  |  |  |
| --- | --- | --- | --- |
| Process Step | Business Role |  | Expected Results |
| [Asset History Sheet](#unique_45) [page ] 59 | Asset Accountant | Asset History Sheet (F1615) | You created an Asset History report. |
| [Depreciation Lists](#unique_46) [page ] 60 | Asset Accountant | Depreciation Lists (F1616) | You created an Asset Total Depreciation report. |
| [Year-End Closing](#unique_47) [page ] 62 | Asset Accountant | Make Company Code Settings - Asset Accounting-Specific (F7312) | You performed year-end closing. |
| [Year-End Closing Asset Accounting (Cross-Company Code and Ledgers)](#unique_48) [page ] 63 | Asset Accountant | Schedule Asset Accounting Jobs (F1914) | You performed year-end closing for asset accounting. |
| [Undo Year-End Closing](#unique_49) [page ] 64 | Asset Accountant | Make Company Code Settings - Asset Accounting-Specific (F7312) | You undid the year-end closing. |

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
| Note In the Change Asset: Master Data screen, you can make a change in any depreciation area. Below are examples for areas 01, 32, and 34. Although you can change many fields in the asset master record, this example focuses on changes to depreciation areas 01, 32, and 34.Depreciation Area 01:Choose Depreciation area: 01.Under Depreciation Area 01, General Parameters, choose Add an Interval.For the new interval, enter a date in the Valid From field and choose OK.Enter a change on the specific line item and choose Save. The system display a success message.Depreciation Area 32:Choose Depreciation Area: 32Under Depreciation Area Area-32, General Parameters, choose Add an Interval.For the new interval, enter a date in the Valid From field and choose OK.Enter a change on the specific line item and choose Save. The system displays a success message.Depreciation Area 34:Choose Depreciation Area: 34Under Depreciation Area-34, General Parameters, choose Add an Interval.For the new interval, enter a date in the Valid From field and choose OK.Enter a change on the specific line item and choose Save. The system displays a success message. |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Fixed Assets (F3425A). | The Manage Fixed Assets view is displayed. |  |
| 3 | Enter Asset Information | Make the following entries and choose Go:Company Code 3310Main Asset Number: <Your asset number>Asset Subnumber: <Your asset subnumber> |  |  |
| 4 | Select Asset | In the table, for the desired asset, choose > (Details). |  |  |
| 5 | Valuation | Choose the Valuation tab. | All depreciation areas are listed. |  |
| 6 | Asset Values | For a ledger/depreciation area, choose > (Details). | The right pane displays the Value Display tab. |  |
| 7 | View Values/Amounts | You can navigate each area (such as Key Figures, Journal Entries, and so on) to view values and amounts. To return to the SAP Fiori launchpad, choose Home. |  |  |

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

Procedure - Maintain Number of Units for UoP Depreciation

| Process Step# | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Maintain Number of Units - For UoP Depreciation (F4907). |  |  |
| 3 | Create Usage Object | Choose Create.Note If the Create Usage Object dialog box displays, enter your company code and choose Continue. | The New Usage Object view is displayed. |  |
| 4 | Enter Data for Usage Object | Make entries in the following fields and choose Create:DescriptionBase Unit of Measure | The system displays the message Object Created. |  |
| 5 | Complete Definition of Usage Object | Ensure that you're in Change mode. If you aren't, choose Edit. |  |  |
| 6 | Define Total Units for Usage Object | Choose the Total Units tab. |  |  |
| 7 | Enter Data for Total Units for Usage Object | Make the following entries:Valid From: <beginning of current fiscal month>Valid To:<end of current fiscal month>Depreciation Area: *Total Units Expected as of This Period: 1200 |  |  |
| 8 | Define Period Units for Usage Object | Choose the Period Units tab. |  |  |
| 9 | Enter Data for Period Units for Usage Object | Make the following entries:Valid From: <beginning of current fiscal month>Valid To:<end of current fiscal month>Planned Number of Units of the Period: 100 |  |  |
| 10 | Save | Choose Save. |  |  |
| 11 | Activate Usage Object | Choose Activate.Caution Only activated usage objects can be assigned to asset master data. |  |  |

Procedure - Maintain Number of Units for UoP Depreciation Assignment to Fixed Asset Master Data

| Process Step# | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Fixed Assets (F3425A). |  |  |
| 3 | Create Asset Master Data | Choose Create > Create Main Asset . |  |  |
| 4 | Enter Details | Make the following entries and choose OK:Company Code: 3310Asset Class: <asset class for new asset>Post-capitalization: <only enter a value here if you want to use this master record to post a post-capitalization>Note You can use reference asset master data. If this is needed, the asset to be used as reference should be entered in the Asset Main Number field in the Reference section. |  |  |
| 5 | Enter Asset Description and Base Unit of Measure | Make entries in the following fields:Asset Description: <your asset description>Base Unit of Measure: <unit of measure> |  |  |
| 6 | Time-Dependent Data | Make entries in the following fields:Cost CenterProfit Center |  |  |
| 7 | Enter, Check, or Adapt Depreciation Parameters | Make the following entries:Depreciation key: <depreciation key; see caution>Note If you activate the feature toggle for the new design, make the following entries:Depreciation Profile: <depreciation profile; see caution>Caution Only depreciation keys UOPT and UOPR support the Unit of Production process.If you activated the feature toggle for the new design, use depreciation profiles 00_UOP_RU and 00_UOP_TU to support the Unit of Production process.UL in Years: 2 |  |  |
| 8 | Enter Usage Object | Under Depreciation area, General Parameters section, enter the usage object you created previously. |  |  |

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
| Note By default, the system checks if the corresponding period is open for posting a supplier invoice. To deactivate the period check for material master records, perform the [Disable Period Check for Material Master (Optional)](#unique_51) [page ] 68 step in the Appendix.If you deactivate the period check, the system no longer performs the check for G/L account postings and postings to assets. However, the check still takes place for direct postings to the material and for invoices with purchase order reference. |

|  |
| --- |
| Note The Create Supplier Invoice (F0859) app is used for simpler supplier invoices and the Create Supplier Invoice - Advanced (MIRO) app is used for more complex supplier invoices. To see a comparison, see [Feature Comparison for Managing Supplier Invoices and Creating Supplier Invoices (Advanced)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/c7c55da4af0a49d08d7df04fc5b39138.html?version=latest). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859).If the Data from Previous Invoice Entry Exist dialog box displays, choose No.Note To use Create Supplier Invoice - Advanced (MIRO), see the Post Acquisition (Integrated AP) Without Purchase Order - MIRO topic in the Appendix. | The New Supplier Invoice(F0859) view is displayed. |  |
| 3 | General Information | In the Basic Data section, enter the following data:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: 1000.00Currency: For example, AEDNote If the entry is tax relevant, the gross amount is inclusive of taxes. Verify the amount.Invoice Date: <Today's date>Posting Date: <Today's date>Reference: <any>Invoicing Party: 33300001 |  |  |
| 4 | Enter Asset Details | In the Asset Items area, select Add and enter your Asset details:Asset <Your asset Number>Asset sub number <Your asset Sub Number>Amount: 1000Quantity: 1Note The Quantity field must only be entered if Unit of Measure is populated in the asset master record used here.Tax code: <your tax code>Note Depending on your country/region, additional tax-related fields may require input. |  |  |
| 5 | Simulate Supplier Invoice and Check Messages | After entering all required details choose Simulate .If there are no differences, the supplier invoice is complete to post.Verify the Gross Invoice Amount against the items plus the tax amount.If the tax code is an exempt tax code, you don't have any tax amount. | The supplier Invoice is complete to post. |  |
| 6 | Post Invoice | Choose Post. | The Invoice is posted. The system displays the message Invoice xxx has been posted. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Asset Acquisition - And Quantity Adjustment (F6488). | The Post Acquisition screen is displayed. |  |
| 3 | General information | In the General Information area, make the following entries:Company Code: 3310Main Asset Number: <Your asset number>Asset subnumber: <Your asset subnumber>Journal Entry Date: <Your document date, for example, today>Posting Date: <Your document date, for example, today>Asset Value Date: <Your value date, for example, today>Transaction Currency Key: AED | The General information tab is displayed. |  |
| 4 | Posting information | In the Posting information area make the following entries:Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Amount Posted in Transaction Currency: 1000.00Quantity: <Your quantity>Note The Quantity field must only be entered if Unit of Measure is populated in the asset master record used here. | The Posting information tab is displayed. |  |
| 5 | Simulate Document | Choose Simulate. | The entered document can be simulated for every ledger and depreciation area and for all ledgers and depreciation areas depending on your selections. |  |
| 6 | Post Document | Choose Post. | The Information dialog box displays the new document number. |  |

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

To execute this activity, run the processes in the Create Asset - MDS (BNI) Master Data Script, using the master data from this document. Then, post acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Post Asset Acquisition - And Quantity Adjustment (F6488). | The Post Acquisition screen is displayed. |  |
| 3 | Select Post Credit Memo transaction | Choose Other Posting Transaction > Post Acquisition > Post Credit Memo . | The Post Credit Memo screen is displayed. |  |
| 4 | General information | In the General Information area, make the following entries:Company Code: 3310Main Asset Number: <Your asset number>Asset subnumber: <Your asset subnumber>Journal Entry Date: <Your document date, for example, today>Posting Date: <Your document date, for example, today>Asset Value Date: <Your value date, for example, today>Transaction Currency Key: AED | The General information tab is displayed. |  |
| 5 | Posting information | In the Posting information area make the following entries:Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Amount Posted in Transaction Currency: 1000Year of acquisition: <Current year >Quantity: <Your quantity>Note The Quantity field must only be entered if Unit of Measure is populated in the asset master record used here. | The Posting information tab is displayed. |  |
| 6 | Simulate Document | Choose Simulate. | Depending on the selections you made, you can simulate the entered document for every ledger and depreciation area and for all ledgers and depreciation areas. |  |
| 7 | Post Document | Choose Post. | The Information dialog box displays the new document number. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Post Asset Acquisition - And Quantity Adjustment (F6488). | The Post Acquisition screen is displayed. |  |
| 3 | Select Post Credit Memo transaction | Choose Other Posting Transaction > Post Acquisition > Post Credit Memo . | The Post Credit Memo screen is displayed. |  |
| 4 | General information | In the General Information area make the following entries:Company Code: 3310Main Asset Number: <Your asset number>Note Use a legacy asset number. For more information, see the Preliminary Steps section.Asset subnumber: <Your asset subnumber>Journal Entry Date: <Your document date, for example, today>Posting Date: <Your document date, for example, today>Asset Value Date: <Your value date, for example, today>Transaction Currency Key: AED | The General information tab is displayed. |  |
| 5 | Posting information | In the Posting information area make the following entries:Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Amount Posted in Transaction Currency: 1000Year of acquisition: <Prior year >Quantity: <Your quantity>Note The Quantity field must only be entered if Unit of Measure is populated in the asset master record used here. | The Posting information tab is displayed. |  |
| 6 | Simulate Document | Choose Simulate. | Depending on the selections you made, you can simulate the entered document for every ledger and depreciation area and for all ledgers and depreciation areas. |  |
| 7 | Post Document | Choose Post. | The Information dialog box displays the new document number. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Post Asset Acquisition - And Quantity Adjustment (F6488). | The Post Acquisition screen is displayed. |  |
| 3 | Select Post Quantity Adjustment transaction | Choose Other Posting Transaction > Post Acquisition > Post Quantity Adjustment . | The Post Quantity Adjustment screen is displayed. |  |
| 4 | General information | In the General Information area make the following entries:Company Code: 3310Main Asset Number: <Your asset number>Asset subnumber: <Your asset subnumber>Journal Entry Date: <Your document date, for example, today>Posting Date: <Your document date, for example, today> | The General information tab is displayed. |  |
| 5 | Posting data | In the Posting data area make the following entries:Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Select either Increase Quantity or Decrease Quantity.Quantity: <number of pieces purchased> | The Posting data tab is displayed. |  |
| 6 | Simulate Document | Choose Simulate. |  |  |
| 7 | Post Document | Choose Post. | The quantity adjustment is visible in the asset master data on the Ledger tab. |  |

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

To complete this activity, run the processes in the Create Asset - MDS(BNI) Master Data Script, using the master data from this document. When that process is completed, post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Post Retirement (Integrated AR) - With Customer (F-92). | The Asset Retire. Frm Sale w/ Customer: Header Data view is displayed. |  |
| 3 | Enter Transaction Details | Make the following entries and press Enter:Document Date: <Your document date, for example, today>Type: DRCompany Code: 3310Posting Date: <Your posting date, for example, today>Currency: AEDPstKy: 01Account: <customer number>, for example, 33100001Note If your country/region has a business place, add it as needed. For UAE, use DXB. | Data is validated. The Enter Customer Invoice: Add Customer item view is displayed.Note If you're creating your own customer, ensure that you enter the complete name, address, postal code, and country/region. If the information is incomplete, the customer won't accept postings. |  |
| 4 | Enter Customer Details | Make the following entries and press Enter:Amount: <Amount>Calculate tax: SelectedTax code: <Output Tax Code>PstKy: 50Account: <Manual revenue account>, for example, 70020000 | Data is validated.The Enter Customer Invoice: Add G/L account item view is displayed.Note Potential tax codes S0 for A/R exempt, <Output Tax Code> for A/R taxable |  |
| 5 | Enter G/L Revenue Account Details | Make the following entries and choose Enter:Output tax Code should be transferred.Amount: <Same amount again>Tax code: <Same output tax code>Asst retirement: Selected | Data is validated. The Create Asset Retirement view is displayed. |  |
| 6 | Enter Asset Details | Make the following entries and choose Continue.Asset: <Your asset number>Subnumber: <Your asset subnumber in case>Transaction Type: 210Note Choose an appropriate transaction type: 210 Retirement with revenue or 260 Retirement of current-year acquis. with revenue.Asset Val. Date: <Your asset value date>Complete Retirement: Selected | Data is validated. The Create Asset Retirement view is displayed.. |  |
| 7 | Post Document | Choose Post. | The asset is retired against a customer. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Post Asset Retirement (F7107). | The Asset Retirement with Revenue screen displays. |  |
| 3 | General information | In the General Information area make the following entries:Company Code: 3310Main Asset Number: <Your asset number>Asset subnumber: <Your asset subnumber>Journal Entry Date: <Your document date, for example, today>Posting Date: <Your document date, for example, today>Asset Value Date: <Your value date, for example, today> | The General information tab is displayed. |  |
| 4 | Posting information | In the Posting information area make the following entries:Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Revenue Amount: 1000.00Currency type of Revenue: 10-Company code currency or 30–Group CurrencyRetirement type: <Select the retirement type from available options, for example Complete Retirement> | The Posting information tab is displayed. |  |
| 5 | Simulate Document | Choose Simulate. |  |  |
| 6 | Post Document | Choose Post. | The asset is retired with revenue. |  |

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

Use an existing asset in any asset class (except 4001 and 4011) that has acquisition postings. If no suitable asset exists, then, you must create asset master data.

To execute this activity, run the processes in the Create Asset (BNI) Master Data Script, using the master data from this document. After completing that process, post the acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Post Asset Retirement (F7107). | The Asset Retirement with Revenue screen displays. |  |
| 3 | Select Retirement without revenue transaction | Choose Other Posting Transaction > Post Retirement > Retirement without Revenue . | The Retirement without revenue screen is displayed. |  |
| 4 | General information | In the General Information area make the following entries:Company Code: 3310Main Asset Number: <Your asset number>Asset subnumber: <Your asset subnumber>Journal Entry Date: <Your document date, for example, today>Posting Date: <Your document date, for example, today>Asset Value Date: <Your value date, for example, today> | The General information tab is displayed. |  |
| 5 | Posting information | In the Posting information area make the following entries:Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Retirement type: <Select the retirement type from available options, for example Complete Retirement> | The Posting information tab is displayed. |  |
| 6 | Simulate Document | Choose Simulate. |  |  |
| 7 | Post Document | Choose Post. | The asset is retired without revenue. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Fixed Assets (F3425A). | The Manage Fixed Assets view is displayed. |  |
| 3 | Enter Asset Details | Make the following entries and choose Go:Company Code: 3310Asset Main Number: <Your asset number>Asset Subnumber: <Your asset subnumber if needed> | The Standard pane displays a list of matching assets. |  |
| 4 | Select Valuation | For the desired asset, choose Details (>) at the right side of the row. | The right pane opens to display the asset details. |  |
| 5 | Valuation | In the right pane, choose the Valuation tab. |  |  |
| 6 | Valuation Line Item | In the Valuation pane, for the row with your Ledger and Depreciation area1 (Book Depreciation), choose Details (>) at the right side of the row. | Another pane opens to the right. |  |
| 7 | Journal Entries | On the Value Display tab, choose the Journal Entries tab. | The Standard pane shows a list of journal entries. |  |
| 8 | Select Document To Reverse | For the journal entry you want to reverse, click the blue journal entry number. From the menu that displays, choose Reverse Journal Entries - In Asset Accounting. | The Reverse Document view is displayed. Document details are displayed.Note If you’ve selected a retirement document for reversal, the Reverse Document selection screen displays.The following steps can be applied for both options offered. |  |
| 9 | Complete Reversal Specifications | Enter Reversal Reason and check the date specifications.Reversal reason <reversal reason, for example, 01> | The reversal specifications are validated. |  |
| 10 | Post Reversal | Choose Save. | The document is reversed. |  |

#### Post Asset Transfer Within Company Code

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

|  |
| --- |
| Note If you want to use the Post Transfer (ABUMN) app, see the [Post Asset Transfer Within Company Code](#unique_52) [page ] 69 topic in the appendix. |

Prerequisites

Use an existing asset in any asset class except 4001 and 4011 that has acquisition postings. If no suitable asset exists, you must create asset master data.

To execute this activity, run the processes in the Create Asset - MDS (BNI) scope item, using the master data from this document. Then post acquisition costs to the asset using the Post Asset Acquisition - And Quantity Adjustment (F6488) app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Asset Transfer (F9302). | The Post Asset Transfer view is displayed. |  |
| 3 | General Information | In the General Information area, make the following entries:Company Code: 3310Main Asset Number: <asset number to be transferred from>Asset Subnumber: <asset subnumber to be transferred from>Journal Entry Date: <document date>, for example, todayPosting Date: <document date>, for example, todayAsset Value Date: <value date>, for example, todayBusiness transaction type: Transfer within Company Code |  |  |
| 4 | Posting Information | In the Posting Information area, make the following entries and choose Post:Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Transfer type: <transfer type>, for example, Complete TransferReceiver Company Code: 3310Receiver Asset: <asset number to be transferred to>Receiver asset subnumber: <asset subnumber to be transferred to> | The asset is transferred. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Post Asset Acquisition - And Quantity Adjustment (F6488). | The Post Acquisition screen is displayed. |  |
| 3 | Select Post Post-Capitalization transaction | Choose Other Posting Transaction > Post Acquisition > Post Post-Capitalization . | The Post Post-Capitalization screen is displayed. |  |
| 4 | General information | In the General Information area make the following entries:Company Code: 3310Main Asset Number: <Your asset number>Asset subnumber: <Your asset subnumber>Note Use a legacy asset number. For more information, see the Preliminary Steps section of this document.Journal Entry Date: <Your document date, for example, today>Posting Date: <Your document date, for example, today>Original Value Date: <Your value date, for example, today>Transaction Currency Key: AED | The General information tab is displayed. |  |
| 5 | Posting information | In the Posting information area make the following entries:Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Amount posted in Transaction ccy: 1000Quantity: <Your quantity>Note The Quantity field must only be entered if Unit of Measure is populated in the asset master record used here. | The Posting information tab is displayed. |  |
| 6 | Simulate Document | Choose Simulate. |  |  |
| 7 | Post Document | Choose Post. | The Information dialog box displays the new document number. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Post Writeup (ABZU). | The Create General Header Data for Posting view is displayed. |  |
| 3 | Enter Header Data | Make the following entries and choose Continue:Company Code: 3310Asset: <Your asset number>Note Use a legacy asset number. For more information, see the Preliminary Steps section.Subnumber: <Your asset subnumber in case>Trans. Type: 700 | The Enter Asset Transaction: Write-up screen displays the Transaction data tab. |  |
| 4 | Enter Transaction Details | Make the following entries and press Enter:Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Document Date: <Your document date, for example, today or a day in the next year>Posting Date: <Your posting date, for example, today or a day in the next year>Asset Value Date: <Your value date, for example, today or a day in the next year>Ordinary dep. PY: <Amount for write-up> |  |  |
| 5 | Post Document | Choose the Post button. | The write-up is posted to the asset. |  |

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
| Note If you activated the feature toggle for the new design, instead of Depreciation Key MANU, use Depreciation Profile 00_MANUAL instead. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Post Depreciation Manually - Unplanned and Planned (ABAAL). | The Create General Header Data for Posting view is displayed. |  |
| 3 | Enter Header Data | Make the following entries and choose Continue:Company Code: 3310Asset: <Your asset number>Subnumber: <Your asset subnumber in case>Trans Type: See noteNote For manual ordinary depreciation, use one of the following transaction types:600 - Manual ordinary depreciation on prior-yr acquis.610 - Manual ordinary depreciation on current-yr acquis.For unplanned depreciation, use one of the following transaction types:640 - Unplanned depreciation on prior-year acquisitions650 - Unplanned depreciation on current-yr acquisitionTransaction types 645 and 655 can be used in some countries/regions when allowed by the local accounting standards. If you receive the error message Unplanned Depreciation positive in Area XX, you may post transaction types 645 and 655 only if there is an existing posting (posted previously with 640 or 650) up to the amount of the previous posting.Select the appropriate transaction type according to the acquisition year of the asset. | The Enter Asset Transaction: Unplanned depreciation view is displayed.The Transaction data tab is displayed. |  |
| 4 | Enter Transaction Details | Make the following entries and press Enter:Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Document Date: <Your document date, for example, today>Posting Date: <Your posting date, for example, today>Asset Value Date: <Your value date, for example, today>Amount posted: <Amount for unplanned depreciation> | Data is validated. AMOUNT can ONLY be up to the NBV of the asset. |  |
| 5 | Post Document | Choose the Post button. | The unplanned depreciation is posted to the asset. |  |

#### Depreciation Forecast

Use

In this activity, the planning horizon is defined as a reference for planned depreciation calculation.

|  |
| --- |
| Caution The planning horizon can only be defined up to 5 years. |

Asset Accounting reporting takes the planning horizon into account and enables the evaluation of planned values in reports.

Enter the number of years that the system should calculate and update planned values:

- If you don’t want the planned values to be updated, enter 0 years. This corresponds with the standard setting.

In this case, the evaluation of planned depreciation is ONLY possible until the end of the current fiscal year.

- If you want the planned values to be updated, enter a value from 1 through 5 .

Dependencies

If you want to change your entries for the planning horizon, consider the following:

- If you define a planning horizon (a number from 1 through 5), you must manually recalculate the depreciation for those depreciation areas belonging to the ledger in the company code. The planned values for the planning horizon is then available in reporting.
- If you later increase the number of years (for example, from 3 years to 5 years), you must recalculate depreciation.
- If you want to deactivate the planned value calculation, enter 0. The system deletes the existing planned values for the following years on the current fiscal year from the database (after you’ve confirmed this in the dialog box).
- If you want to decrease the number of years, enter the new number. The system deletes the existing planned values from the database accordingly (after you’ve confirmed this in the dialog box).

Prerequisites

1. Log on to SAP Fiori Launchpad as an Asset Accountant.
2. Open Make Company Code Settings - Asset Accounting-Specific (F7312).
3. Enter your company code in the filter area and choose Go.
4. Select your company code from the table. On the next view, choose Edit.
5. On the Ledger Settings tab, make the following entries:

Planning Horizon: <number from 1 through 5 for years to forecast>

1. Save your changes.

Procedure

Planned values are visible in following reports:

| Report | For more information |
| --- | --- |
| Asset History Sheet (Key Figure Group – AHS_PLAN) | See the Year-End Closing section of this test script |
| Asset Balances (Key Figure Group – ABS_DEF or DEPR_TOTAL) | See the Month-End Closing section of this test script |
| Depreciation List | See the Month-End Closing section of this test script |

### Month-End Closing

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Schedule Asset Accounting Jobs (F1914). |  |  |
| 3 | Create New Recalculation Run Job | Choose Create. | The New Job view is displayed. |  |
| 4 | Enter Depreciation Run Job Details | Make the following entries and choose Step 2:Job Template: Recalculate DepreciationJob Name: Recalculate Depreciation | The recalculation run is scheduled. |  |
| 5 | Enter Depreciation Run Job Details | Make the following entries and choose Step 3:Start immediately: Selected |  |  |
| 6 | Enter Depreciation Run Job Details | Make the following entries and choose Schedule:Caution For the Ledger radio button, only select it if you want to run the job for one accounting principle. If you select it, enter the accounting principle in the Ledger field.Ledger (radio button): <see caution above>Ledger (field): <see caution above>Caution For the Depreciation Area radio button, only select it if you want to run the job for one depreciation area. If you select it, enter the depreciation area in the Depreciation Area field.Note Depreciation Area (radio button): <see caution above>Depreciation Area (field): <see caution above>FROM Fiscal year: <Current fiscal year>Asset: <leave blank; if you want to run the job for one asset, specify the asset>Company Code: 3310Test Run: <select to perform a test run/simulation; deselect to perform an actual run>Detailed Logs: SelectedSave the job. |  |  |
| 7 | Check Recalculation Run Job Details | In the Application Jobs pane, select your Recalculate Depreciation line.Note You can only display details for jobs you created. | The Recalculate Depreciation screen displays the details. If the list contains Depreciation changes, go back to the Recalculate Depreciation view, deselect Test Run and schedule the job again. |  |
| 8 | Check Recalculation Run Job Log | Choose Log. | The Recalculate Depreciation view displays the log. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Schedule Asset Accounting Jobs (F1914). |  |  |
| 3 | Create New Depreciation Run Job | Choose Create. | The New Job view is displayed. |  |
| 4 | Enter Depreciation Run Job Details | Make the following entries and choose Step 2:Job Template: Depreciation Posting RunJob Name: Depreciation Posting Run | The posting run is scheduled. |  |
| 5 | Step 2 | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Schedule | Make the following entries and choose Schedule:Company Code: 3310Fiscal Year: <Current fiscal year>Posting Period: <Next period due to posting cycle>Test Run: A check indicates a test run. Absence of a check indicates a real run.Note It's a good practice to do a test run before doing a real run. Depreciation can also be run with Ledger selection. |  |  |
| 7 | Adopt Job Selection | Make the following entries and choose Go:Status: <Activate all status>Date From-To: <Proper date interval> | Selected application jobs are displayed. |  |
| 8 | Check Depreciation Run Job Details | For the job you ran, choose Details (>) at the right side of the row.Note You can only display details for jobs you created. | The Job Details screen displays the details. |  |
| 9 | Check Depreciation Run Job Log | In the Log and Results pane, choose the icon in the Results field. | The Depreciation Posting Run screen displays the log. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Asset Balances (F1617). | The Prompts view is displayed. |  |
| 3 | Entries | Make the following entries and choose Go:Key Figure Group: For example, ABS_DEFCompany Code: For example, 3310Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Depreciation Area: For example, 01Fisc. Year of Ledger: <current year>To Period: For example, xxCurrency Type: For example, 10 | Note Familiarize yourself with the Asset Balances report. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Asset Transactions (F1614). |  |  |
| 3 | Enter Selection Details | Make the following entries and choose Go.Key Figure Group: For example, TRANS_ALL (All Transactions))Company Code: For example, 3310Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Fisc.Year of Ledger: For example, 2023Depreciation Area: For example, 01Display Currency: For example, AED | The Asset Transactions report displays. |  |
| 4 | Review Transactions | Expand Company Code, then expand a specific transaction. Choose the Details arrow at the right of the row. Review the information, then choose Back. |  |  |
| 5 | Asset Number | In the selected asset row, choose the asset number.Note Choose the blue link for the asset number. | A dialog box displays. |  |
| 6 | More Links | Choose More Links. | The Define Link List dialog box displays. |  |
| 7 | Manage Fixed Assets | Select Manage Fixed Assets (New Version) and choose OK. | The prior dialog box displays a new link for Manage Fixed Assets. |  |
| 8 | Manage Fixed Assets | Choose Manage Fixed Assets. | The Manage Fixed Assets view displays. Review the information. |  |

#### Depreciation Lists

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create a report that displays all depreciation posted in Asset Accounting during periodic processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Depreciation Lists (F1616). | The Posted Depreciation selection view is displayed. |  |
| 3 | Enter Selection Details | Make the following entries and choose Go:Fisc.Year of Ledger: For example, 2023To-Period: For example, 012Depreciation Variant: For example, Ordinary DepreciationCompany Code: For example, 3310Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Depreciation Area: For example, 01Display Currency: For example, AED | The Posted Depreciation report displays. |  |
| 4 | Display Details | Expand the Company Code node, then expand into a specific asset class. Choose the Details button at the right side of the row. | Review and explore the scroll bars. |  |
| 5 | Detail | Review the asset details, then choose Back. |  |  |
| 6 | Asset | Select a specific asset, then choose Manage Fixed Assets to see values for each depreciation area. In the Values section, the posted and planned amounts are displayed. Highlight a depreciation area to view depreciation amounts. |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Fixed Assets (F3425A). | The Manage Fixed Assets view is displayed. |  |
| 3 | Enter Asset Information | Make the following entries and choose Go:Company Code 3310Main Asset Number: <Your asset number>Asset Subnumber: <Your asset subnumber> | All asset value categories and asset transactions are displayed for each depreciation area. |  |
| 4 | Select Asset | In the table, for the desired asset, choose > (Details). |  |  |
| 5 | Valuation | Choose the Valuation tab. | All depreciation areas are listed. |  |
| 6 | Asset Values | For a ledger/depreciation area, choose > (Details). | The right pane displays the Value Display tab. |  |
| 7 | View Values/Amounts | You can navigate each area (such as Key Figures, Journal Entries, and so on) to view values and amounts. To return to the SAP Fiori launchpad, choose Home. |  |  |

### Year-End Closing

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Asset History Sheet (F1615). |  |  |
| 3 | Enter Selection Details | Make the following entries and choose Go:Key Figure Group: AHSCompany Code: <company code>, for example, 3310Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Depreciation Area: <depreciation area>, for example, 01, 32, or 34Fisc.Year of Ledger: For example, 2023To Period: For example, 12Currency Type: For example, 10 | The Asset History Sheet report displays.Scroll down to see horizontal scroll bars. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Depreciation Lists (F1616). | The Depreciation Lists view is displayed. |  |
| 3 | Enter Selection Details | Make the following entries and choose Go:Key Date: <date>, for example, Today's dateFisc.Year of Ledger: for example, 2023To Period: for example, 012Depreciation Variant: for example, Ordinary DepreciationCompany Code: for example, 3310Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Depreciation Area: for example, 1Display Currency: for example, AED | The Posted Depreciation report displays. |  |
| 4 | Display Details | Expand Company Code, then expand to a specific asset class. To view asset details, choose the Details (>) button to the right of an asset's row. | The right pane opens to display asset details. |  |
| 5 | Back | Choose Back. |  |  |
| 6 | More Links | In the Fixed Asset column, click the asset number, then choose More Links. |  |  |
| 7 | Select Apps | Select the following checkboxes and choose OK:Manage Fixed AssetsNote In the Valuation section, the posted and planned amounts displays.Asset Balances | The links are displayed in the dialog box. |  |
| 8 | Go to Apps | To view information in one of the apps, choose the appropriate link. |  |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Make Company Code Settings - Asset Accounting-Specific (F7312). |  |  |
| 3 | Company Code | Select your company code from the table. | A new view is displayed. |  |
| 4 | Edit | Choose the Edit button. |  |  |
| 5 | Select Ledger | In Ledger Settings, select the appropriate ledger (for example, 0L, 2L, 3L) for your company code. |  |  |
| 6 | Select Depreciation Area | Select the depreciation area and choose Close Fiscal Year. |  |  |
| 7 | Save | Choose Save. | The closed fiscal year is displayed for the selected depreciation area. |  |

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
| Note Ensure that all depreciation periods for the year are completed.If your implementation doesn't use a specific ledger, disregard that ledger. |

Procedure

| Process Step# | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Schedule Asset Accounting Jobs (F1914). |  |  |
| 3 | Create New Year-End Closing Job | Choose Create. | The New Job view is displayed. |  |
| 4 | Enter Data for Step 1 – Template Selection | Make the following entries and choose Step 2:Job Template: Year-End Closing Asset Accounting (Cross-Company Code and Ledger)Job Name: Year-End Closing Asset Accounting (Cross-Company Code and Ledger) |  |  |
| 5 | Enter Data for Step 2 – Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Data for Step 3 – Parameters | Make the following entries and choose Schedule:Closing Parameters section:Company Code: 3310Note More than one company codes can be selected.Ledger: <one or more ledgers>Note More than one ledger can be selected.Fiscal Year to be Closed: Current YearNote To reopen the closed fiscal year, use the Make Company Code Settings - Asset Accounting Specific (F7312) app.Additional Parameters section:Test Run: <see note below>Note To run a test run, select the Test Run checkbox. To run a productive mode run, deselect the Test Run checkbox. | The selected company code and ledgers are closed when the job has a Finalized status.The result can be validated using the Make Company Code Settings - Asset Accounting-Specific (F7312) app. |  |

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Make Company Code Settings - Asset Accounting-Specific (F7312). |  |  |
| 3 | Company Code | Select your company code from the table. | A new view is displayed. |  |
| 4 | Edit | Choose the Edit button. |  |  |
| 5 | Select Ledger | In Ledger Settings, select the appropriate ledger (for example, 0L, 2L, 3L) for your company code. |  |  |
| 6 | Select Depreciation Area | Select the depreciation area and choose Reopen Fiscal Year. | The closed fiscal year should be one year before the one stored before this action (for example, if the closed FY is 2020, you can open FY 2020 and then the closed FY is 2019). |  |
| 7 | Save | Choose Save. | The closed fiscal year is opened for the selected depreciation area. |  |

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
| Note By default, the system checks if the corresponding period is open for posting a supplier invoice. To deactivate the period check for material master records, perform the [Disable Period Check for Material Master (Optional)](#unique_51) [page ] 68 step in the Appendix.If you deactivate the period check, the system no longer performs the check for G/L account postings and postings to assets. However, the check still takes place for direct postings to the material and for invoices with purchase order reference. |

|  |
| --- |
| Note The Create Supplier Invoice (F0859) app is used for simpler supplier invoices and the Create Supplier Invoice - Advanced (MIRO) app is used for more complex supplier invoices. To see a comparison, see [Feature Comparison for Managing Supplier Invoices and Creating Supplier Invoices (Advanced)](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0e602d466b99490187fcbb30d1dc897c/c7c55da4af0a49d08d7df04fc5b39138.html?version=latest). |

Prerequisites

To execute this activity, run the processes in the Create Asset - MDS (BNI) Master Data Script, using the master data from this document.

To enable posting to assets, ensure that you've executed the [Activate Direct Posting to Asset](#unique_11) [page ] 14 preliminary step.

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

### Post Asset Transfer Within Company Code

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Post Transfer (ABUMN). | The Enter a Company Code selection view is displayed. |  |
| 3 | Enter Company Code | Make the following entry and choose Continue:Company Code: 3310 | The Enter Asset Transaction: Transfer within Company Code view is displayed.The Transaction data tab is displayed. |  |
| 4 | Enter Transaction Details | Make the following entries and choose Enter.Asset: <Your asset number to be transferred from>Ledger: <empty for all ledgers, or use the Ledger value in the Master Data, Organizational Data, and Other Data topic>Document Date: <Your document date, for example, today>Posting Date: <Your posting date, for example, today>Asset Value Date: <Your value date, for example, today>Existing Asset: <Your asset number to be transferred to> | Data are validated. |  |
| 5 | Partial Transfer | Choose the Partial Transfer tab. |  |  |
| 6 | Prior or Current Year Asset | Select the appropriate radio button according to the acquisition year of the asset to be retired.Prior.-year acquis. or From curr.-yr acquis. |  |  |
| 7 | Post Document | Choose Post. | The asset is transferred. |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-asset-accounting-additional-depreciation-area-5hg-ae-1095]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J62_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 118,731 chars in the whole document
