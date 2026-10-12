---
id: 03-financial-accounting-and-close/asset-under-construction-additional-depreciation-area-5kf-ae-test-scri
title: Asset Under Construction – Additional Depreciation Area (5KF_AE) – Test Script (5KF_S4CLD2608_BPD_EN_AE)
description: "S/4HANA Cloud Public Edition test script for scope item 5KF_AE: AuC additional depreciation area, prerequisites, legacy transfer, AuC acquisition, settlement."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/assets-under-construction]
aliases: [5KF_S4CLD2608_BPD_EN_AE]
keywords: [Assets Under Construction, asset under construction, additional depreciation area, test scripts, auc settlement, distribution rules, legacy data transfer, supplier invoice, asset accounting, legacy assets]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5KF_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1107
topic: 03-financial-accounting-and-close/assets-under-construction
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Asset Under Construction – Additional Depreciation Area (5KF_AE) – Test Script (5KF_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5KF_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Assets Under Construction** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Asset Under Construction – Additional Depreciation Area (5KF_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Asset Under Construction – Additional Depreciation Area (5KF_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232857337)

[2 Prerequisites 4](#_Toc232857338)

[2.1 System Access 4](#_Toc232857339)

[2.2 Roles 4](#_Toc232857340)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232857341)

[2.4 Business Conditions 7](#_Toc232857342)

[2.5 Preliminary Steps 8](#_Toc232857343)

[2.5.1 Validate Asset Accounting System Readiness 8](#_Toc232857344)

[2.5.1.1 Confirm Takeover Date Information 8](#_Toc232857345)

[2.5.1.2 Confirm Run of Balance Carryforward for Current Fiscal Year 9](#_Toc232857346)

[2.5.1.3 Create Asset Master Record for Legacy Asset 10](#_Toc232857347)

[2.5.1.4 Transfer Open Items of AuC for Legacy Asset 12](#_Toc232857348)

[2.5.1.5 Acquisition Assets 13](#_Toc232857349)

[2.5.2 Activate Direct Posting to Asset 13](#_Toc232857350)

[3 Overview Table 15](#_Toc232857351)

[4 Test Procedures 16](#_Toc232857352)

[4.1 Asset Acquisition for Constructed Assets (External Procurement) 16](#_Toc232857353)

[4.1.1 Create Assets 16](#_Toc232857354)

[4.1.2 Post Acquisition (Integrated AP) Without Purchase Order 17](#_Toc232857355)

[4.1.3 Define Distribution Rules for Assets Under Construction (Periodic Processing) 19](#_Toc232857356)

[4.1.4 Execute Settlement for Assets Under Construction (Periodic Processing) 21](#_Toc232857357)

[5 Appendix 23](#_Toc232857358)

[5.1 Post Acquisition (Integrated AP) Without Purchase Order 23](#_Toc232857359)

[5.2 Disable Period Check for Material Master (Optional) 24](#_Toc232857360)

## Purpose

Overview

This scope item is optional.

Some local or industry-specific rules (for example, for utility companies) may contain specific rules for depreciation and reporting. Companies may need to report insurance values to insurers for high valued assets. To fulfill these requirements, you can activate this scope item. The scope item provides preconfigured content such as a specific valuation view and specific depreciation terms at accounting principle level and valuation view level for asset classes.

An additional depreciation area is added when you activate the scope item. This depreciation area is for Asset Accounting purposes only and it contains statistical postings. You can define the depreciation parameters in this depreciation area (for example, for assets, you can define useful life, maximum amount for low-value assets and so on).

|  |
| --- |
| Note The additional depreciation area can only be activated during initial activation, meaning that the Asset Under Construction – Additional Depreciation Area (5KF) scope item is unavailable for subsequent scoping selections. |

|  |
| --- |
| Note If you have activated the feature toggle for the new design, use Depreciation Profile instead of Depreciation Key. |

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

Table 1: Required Business Roles and Spaces

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Asset Accountant | SAP_BR_AA_ACCOUNTANT | Fixed Assets | SAP_BR_AA_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you’ve installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Asset Class for Asset under Construction | 4000 |  |  |
| Asset Class for final settlement | * | all classes, except 4000, 4001 |  |
| Vendor | * | Domestic vendor | If no vendor is available in your system yet, create a domestic vendor. |
| Cost Center | 33101301 | Manufacturing – 1 | You can also use another Cost Center, but you must make sure that you use a consistent combination of Cost Center and Profit Center (see table Overview of assignments below). |
| Profit Center | YB110 | Product A | You can also use another Profit Center, but you must make sure that you use a consistent combination of Cost Center and Profit Center (see table Overview of assignments below). |
| Functional Area | YB20 | Production | You can also use another Functional Area, but you must make sure that you use a consistent combination of Cost Center and Functional Area (see table Overview of assignments below). |
| Company Code | 3310 |  |  |
| Chart of Depreciation | 3310 |  |  |
| Controlling Area | A000 |  |  |

Table 2: Overview of Assignments: Cost Centers, Profit Center, Functional Areas, Segments

| Cost Center | Profit Center | Functional Area | Segment |
| --- | --- | --- | --- |
| 33101101 | YB600 | YB40 | 1000_C |
| 33101201 | YB700 | YB20 | 1000_C |
| 33101202 | YB700 | YB20 | 1000_C |
| 33101301 | YB110 | YB20 | 1000_A |
| 33101302 | YB111 | YB20 | 1000_B |
| 33101321 | YB111 | YB20 | 1000_B |
| 33101401 | YB600 | YB40 | 1000_C |
| 33101501 | YB600 | YB50 | 1000_C |
| 33101601 | YB600 | YB35 | 1000_C |
| 33101602 | YB600 | YB30 | 1000_C |
| 33101701 | YB600 | YB40 | 1000_C |
| 33101750 | YB900 | YB40 | 1000_C |
| 33101751 | YB600 | YB40 | 1000_C |
| 33101752 | YB600 | YB40 | 1000_C |
| 33101753 | YB600 | YB40 | 1000_C |
| 33101801 | YB600 | YB40 | 1000_C |
| 33101901 | YB600 | YB30 | 1000_C |
| 33101902 | YB101 | YB25 | 1000_A |
| 33101903 | YB102 | YB25 | 1000_B |
| 33101904 | YB103 | YB25 | 1000_C |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 3: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNH | Create Profit Center - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

|  |
| --- |
| Note This test script is relevant for systems in which additional depreciation area 16 - Customer specific purpose is activated. |

| Scope Item | Business Condition |
| --- | --- |
| BNI - Create Asset - MDS | During the execution of this scope item, asset master records are created for assets under construction and the assets to which final settlement is performed. To create the assets, use the master data script Create Asset - MDS (BNI) using the data described in this test script. |

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

In this activity, you create legacy Assets Under Construction (AUC) assets with values. These assets may be used for various testing scenarios. You create five legacy AUC assets in Asset Class 4000 with different descriptions.

You first create the asset master record for the legacy asset and then transfer the open items for the legacy asset.

Procedure

| Process Step# | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the Fiori App | Open Manage Legacy Assets - Deprecated (F7280). |  |  |
| 3 | Create Fixed Asset | Choose Create > Create Legacy Asset Main Number . | The Create Legacy Asset Main Number dialog box is displayed. |  |
| 4 | Asset Class | Make the following entries and choose OK:Company Code: For example, 3310Asset Class: <asset class; see the Master Data, Organization Data, and Other Data topic> |  |  |
| 5 | Legacy Asset | Make the following entry:Asset Description: Legacy AUC Asset xxxxxxCaution Ensure that the asset descriptions begin with the words Legacy AUC. |  |  |
| 6 | Ledger | Choose the Ledger tab. |  |  |
| 7 | Enter Capitalization Date | For the appropriate ledger, make the following entry and press EnterCapitalized On: date, for example, 04/08/2016Note : This is a prior year AUC asset, so this date must be in a past fiscal year. |  |  |
| 8 | Time Dependent Tab | Choose the Time- Dependent Data tab. |  |  |
| 9 | Cost Center | Make the following entries and press Enter:Cost Center: For example, 33101301Note You can enter the Cost Center and/or the WBS Element. |  |  |
| 10 | Valuation | Choose the Valuation tab. |  |  |
| 11 | Confirm Values | Confirm Dep. Key, UL in Years (or UL in Periods), and Dep. Start Date.Note If you activated the feature toggle for the new design, use Depreciation Profile instead of Dep.Key/Depreciation Key.Note You may need to choose Details (>) for the row to see some of these fields. | The fields are verified. |  |
| 12 | Save the Record | Choose Create. | Make a note of the asset number: _________________. |  |
| 13 | Home | Choose the Home button to return to the SAP Fiori launchpad. | The SAP Fiori launchpad displays. |  |

##### Transfer Open Items of AuC for Legacy Asset

Purpose

In this activity, you create five legacy Assets Under Construction (AUC) in Asset Class 4000 or 4010, each with values and unique descriptions. These assets are intended for various testing scenarios. The process involves two main steps: first, creating the asset master record for each legacy asset, and then transferring the open items associated with them.

Procedure

| Process Step# | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Transfer Open Items of AuC - For Legacy Asset (ABLDT_OI).Note This is for an AUC asset in Asset Class 4000 or 4010. | The Create General Header Data for Posting dialog box is displayed. |  |
| 3 | Enter the Company and Legacy AUC Asset | Enter a legacy asset to be updated with values (this is an AUC asset in Asset Class 4000 or 4010).Make the following entries and choose Continue:Company Code: For example, 3310Asset: <asset number>Transaction Type: 900 | Note Transaction Type 900 lets you enter open items for a legacy AUC asset in Asset Class 4000 or 4010. |  |
| 4 | Enter Values for Legacy AUC Asset | Make the following entries and choose Simulate:Ledger: <ledger>Transfer Date: <transfer date; defaulted per data takeover date>Document Date: <document date; defaulted per data takeover date>Posting Date: <posting date; defaulted per data takeover date>Asset Value Date: <asset value date; defaulted per data takeover date>Amount Posted: For example, 3600.00 | The Enter Asset Transaction: Legacy Data-Transfer Open Items screen is displayed.Confirm the respective dates and amount posted.The system displays the Posting will take place in an earlier fiscal year message. Bypass this warning.If any errors are RED coded, these must be corrected before posting. |  |
| 5 | Post Legacy AUC Asset Transaction | Choose Post.Choose Continue. | Make a note of the document number for each accounting principle:AEAP ______________________IFRS ____________________ |  |

##### Acquisition Assets

Purpose

Some test procedures in this script are based on AuCs managed by line item. Asset class 4000 is identified in Customizing as managed by line item for this purpose.

1. Create an asset master record in asset class 4000.
2. Post an acquisition to this asset under construction.
3. Create an asset master record in asset class 2000 (Machinery).

The settlement profile can include both FXA (Asset) and CTR (Cost Center).

|  |
| --- |
| Note In the Test Procedure section, steps are included to offer support in asset master data creation and acquisition posting. |

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

## Overview Table

This scope item consists of several process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 4: Asset Acquisition for Constructed Assets (External Procurement)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
| [Create Assets](#unique_14) [page ] 16 | Asset Accountant | See the Create Asset - MDS (BNI) master data script. | You created two master records:An Asset Under ConstructionAn Asset Master (for final settlement) |
| [Post Acquisition (Integrated AP) Without Purchase Order](#unique_15) [page ] 17 | Asset Accountant | Create Supplier Invoice (F0859) | You posted the acquisition from purchase with vendor. |
| [Define Distribution Rules for Assets Under Construction (Periodic Processing)](#unique_16) [page ] 19 | Asset Accountant | Define Distribution Rules - For AuC (AIAB) | You defined the distribution rules for assets under construction. |
| [Execute Settlement for Assets Under Construction (Periodic Processing)](#unique_17) [page ] 21 | Asset Accountant | Execute Settlement - For AuC (AIBU) | Assets under Construction are settled according to their settlement rules. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Asset Acquisition for Constructed Assets (External Procurement)

#### Create Assets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step you create an asset under construction (AuC) and an asset master record for the final settlement.

Prerequisite

For an AuC, use an asset that meets the following criteria:

Table 5: Asset under Construction - Details

| Field | Value |
| --- | --- |
| Asset class | 4000 |
| Cost Center | 33101301 |
| Capitalization Date | None |

For an asset for final settlement, use an asset that meets the following criteria:

Table 6: Asset for Final Settlement - Details

| Field | Value |
| --- | --- |
| Asset Class | 2000 |
| Cost Center | 33101301 |
| Capitalization Date | None |

Procedure

To execute this activity, run the processes described in the Create Asset - MDS (BNI) master data script. Use the data mentioned above to run the processes.

|  |
| --- |
| Note You can also use another cost center, but you must ensure that you use a consistent combination of cost center and profit center (see the Overview of Assignments table in the Master Data and Organizational Data section). |

Result

You created two asset master records, one AuC and one for the final settlement.

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
| Note By default, the system checks if the corresponding period is open for posting a supplier invoice. To deactivate the period check for material master records, perform the [Disable Period Check for Material Master (Optional)](#unique_19) [page ] 24 step in the Appendix.If you deactivate the period check, the system no longer performs the check for G/L account postings and postings to assets. However, the check still takes place for direct postings to the material and for invoices with purchase order reference. |

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

#### Define Distribution Rules for Assets Under Construction (Periodic Processing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you maintain the settlement rules for the asset under construction created in the previous steps.

Prerequisites

You executed all the previous steps related to assets under construction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Define Distribution Rules - For AuC (AIAB). | The view displays. |  |
| 3 | Maintain Settlement Rule | Make the following entries and choose Settlement AuC: Initial screenExecute:Company Code: 3310Asset: <No. of asset> For example, from asset class 4000Note The asset number is the asset created in the previous step.Ledger: <optional; see note>Note If you enter a ledger value (for example, 0L or 2L), distribution rules should be defined for both ledgers. If you only have distribution rules defined for 0L, enter 0L. If you only have distribution rules defined for 2L, enter 2L. | The Settlement AuC: Line item listSettleme view displays. |  |
| 3.1 | Enter Distribution Rules | Select the line items you posted and choose DistrRule.Note Each ledger has separate line items. Ensure that you select all. | The Maintain Settlement Rule: Overview view displays. |  |
| 4 | Enter Distribution Rules | To maintain the distribution rule for the local ledger, select the line for ledger 0L and depreciation area 01. Select the document displayed and choose Enter Distribution Rule.Note To maintain the distribution rule for the second ledgers, select a line item for ledger 2L and depreciation area 32, or the line for ledger 3L and depreciation area 34.Make the following entries:Cat: <FXA> AssetSettlement Receivers: <No. of asset in class 2000> (such as your Depreciating Asset. For example, in asset class 2000).%: <Portion of AuC APC that can be capitalized> For example, 90%.After indicating the first category FXA, press Enter.Cat: <CTR> Cost CenterSettlement Receivers: <Cost Center> on the asset master data created in previous step (for example, 33101301)%: <Portion of AuC APC that cannot be capitalized> For example, 10.After indicating the second category CTR, press Enter. |  |  |
| 6 | Save Settlement Rule | Choose Back.Choose Save. | You maintained the rules for the settlement. The system displays the Distribution rules saved notification. The execution of the settlement is part of the periodic processing. |  |

#### Execute Settlement for Assets Under Construction (Periodic Processing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the execution of this step, assets under construction are settled according to their settlement rules.

Prerequisite

You must have maintained the settlement rules for the Asset under Construction you want to settle.

|  |
| --- |
| Note Under certain conditions, you may need to capitalize an asset under construction before all suppliers have presented their closing invoices. This can cause a few difficulties, especially if the closing invoice can’t be posted until the fiscal year following the capitalization of the asset under construction, and down payments were already posted to the asset under construction. |

Initially, you post the down payment normally. If you need to capitalize the asset under construction at the end of the fiscal year, but before the closing invoice is received, you post reserves for the total amount of the expected invoice. You post these reserves directly to the capitalized asset (external acquisition with vendor, transaction type 100). If you plan to distribute the values from the asset under construction to several final assets, it makes sense to post the reserve to the asset under construction first, and then capitalize it. Whichever method you use, you must reverse the down payment on the asset under construction, because the down payment isn’t allowed to appear in the account for down payments to fixed assets. Instead, it must appear in the account for completed assets.

To settle the asset under construction, down payments must be cleared with an invoice or forecasted invoice (reserve). The asset under construction can only be settled after this clearing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app. | Open Execute Settlement - For AuC (AIBU). | The AuC Settlement: Initial Screen view displays. |  |
| 3 | Execute AUC settlement | Make the following entries and choose Simulate:Company Code: 3310Asset: <no. of the asset under construction>Ledger: <ledger (optional)>Note If you enter a ledger value (for example, 0L or 2L), distribution rules should be defined for both ledgers. If you only have distribution rules defined for 0L, enter 0L. If you only have distribution rules defined for 2L, enter 2L.Document date: <document date>Asset value date: <asset value date>Posting date: <posting date>Period: <derived from Posting Date> | The Settlement AuC: Line Item List view displays. |  |
| 4 | Execute AUC settlement | Select the line for ledger and depreciation area for which settlement should be executed. Choose Save. | The relevant line items are displayed. |  |

## Appendix

### Post Acquisition (Integrated AP) Without Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the acquisition from purchase with a vendor.

An external asset acquisition is a business transaction that results from the acquisition of an asset from a business partner (in contrast to an in-house acquisition). You can post the acquisition of an external asset in the following ways:

- In Asset Accounting (FI-AA) integrated with Accounts Payable (FI-AP)
- In Asset Accounting without integration with Accounts Payable (posting to a clearing account - with or without clearing).

There are two scenarios:

- The asset acquisition comes before the receipt of the invoice. The offsetting entry is posted automatically.
- The asset acquisition is posted after the receipt of the invoice. The invoice was posted as an open item to a clearing account. This scenario isn’t described further here. For more information, see Accounts Payable Accounting.

In this activity, the asset acquisition is posted integrated with Accounts Payable (FI-AP).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Create Supplier Invoice - Advanced (MIRO). |  |  |
| 3 | Navigation | If the system prompts you, make the following entries and choose Continue:Company Code: 3310 |  |  |
| 4 | Basic Data | On the Basic Data tab, enter the following data:Invoice Date: <Your document date, for example, today>Posting Date: <Your document date, for example, today>Reference: anyAmount: 1000Currency: AEDCalculate tax : SelectedTax code: <Input Tax Code>Tax Country/Region: <Tax country/region> |  |  |
| 5 | Payment | In the Payment tab, enter the following data:BaselineDt: <Your document date, for example, today>Pyt Terms : 0001 |  |  |
| 6 | Details | In the Details tab, enter the following data:Inv. Party: 33300001 |  |  |
| 7 | Enter Asset Details | In the Asset section, make the following entries and press Enter:Asset: <Your asset number>Asset subnumber: <Your asset subnumber>A mount : 1000 | All required entries are made. |  |
| 8 | Post Document | Choose Post. | The Address and Bank Data dialog box is displayed. |  |
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
> Flagged while digesting this document, not verified: Takeover date section says the date is usually the prior year-end, yet its example says fiscal year 2025 implies loading legacy assets as of year end 2023 (prior year-end would be 2024).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/test-script-asset-under-construction-bfh-ae-sap-s-4hana-cloud-public-e]]
- related-to :: [[03-financial-accounting-and-close/test-script-asset-under-construction-group-ledger-ifrs-1gf-ae-720]]
- related-to :: [[03-financial-accounting-and-close/test-script-asset-under-construction-group-ledger-us-gaap-33g-ae-899]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5KF_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 44,018 chars in the whole document
