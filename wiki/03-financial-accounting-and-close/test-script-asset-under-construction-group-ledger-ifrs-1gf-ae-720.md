---
id: 03-financial-accounting-and-close/test-script-asset-under-construction-group-ledger-ifrs-1gf-ae-720
title: "Test Script: Asset Under Construction – Group Ledger IFRS (1GF_AE) (1GF_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for Asset Under Construction, Group Ledger IFRS (1GF_AE): legacy AuC setup, distribution rules, settlement."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/assets-under-construction]
aliases: [1GF_S4CLD2608_BPD_EN_AE]
keywords: [Assets Under Construction, auc settlement, distribution rules, legacy asset transfer, takeover date, balance carryforward, legacy asset master record, business roles, test data, activate features]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GF_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-720
topic: 03-financial-accounting-and-close/assets-under-construction
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Asset Under Construction – Group Ledger IFRS (1GF_AE) (1GF_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GF_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Assets Under Construction** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Asset Under Construction – Group Ledger IFRS (1GF_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232847059)

[2 Prerequisites 3](#_Toc232847060)

[2.1 System Access 3](#_Toc232847061)

[2.2 Roles 3](#_Toc232847062)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232847063)

[2.4 Business Conditions 6](#_Toc232847064)

[2.5 Preliminary Steps 7](#_Toc232847065)

[2.5.1 Validate Asset Accounting System Readiness 7](#_Toc232847066)

[2.5.1.1 Confirm Takeover Date Information 7](#_Toc232847067)

[2.5.1.2 Confirm Run of Balance Carryforward for Current Fiscal Year 8](#_Toc232847068)

[2.5.1.3 Create Asset Master Record for Legacy Asset 9](#_Toc232847069)

[2.5.1.4 Transfer Open Items of AuC for Legacy Asset 11](#_Toc232847070)

[3 Overview Table 13](#_Toc232847071)

[4 Test Procedures 14](#_Toc232847072)

[4.1 Define Distribution Rules for Assets under Construction (Periodic Processing) 14](#_Toc232847073)

[4.2 Execute Settlement for Assets Under Construction (Periodic Processing) 15](#_Toc232847074)

## Purpose

Overview

Assets under Construction (AuC) are a special form of tangible assets. They are usually displayed as a separate balance sheet item, requiring separate account determination and their own asset classes. During the construction phase of an asset, all actual postings are assigned to the AuC. Once the asset is completed, a transfer is made to the final fixed asset. Ledger-specific transactions such as Settlement Distribution Rule may influence the settlement result in different accounting principles.

This scope item is for IFRS.

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
| Asset Accountant | SAP_BR_AA_ACCOUNTANT | Fixed Assets | SAP_BR_AA_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Asset Class for Asset under Construction | 4000 |  |  |
| Asset Class for final settlement | * | All classes except 4000, 4001 |  |
| Supplier | * | Domestic supplier | When no vendor is available in your system, create a domestic supplier. A detailed description to create such a vendor master record could be found in the Create Supplier Master - MDS (BNE) Master Data Script. |
| Cost Center | 33101301 | Manufacturing – 1 | You can also use another cost center, but you must ensure that you use a consistent combination of cost center and profit center (see the Overview of Assignments table below). In addition, you must use the same assignment of cost center and profit center for the asset and the investment order. |
| Company Code | 3310 |  |  |
| Chart of Depreciation | 3310 |  |  |

Table 1: Overview of Assignments: Cost Centers, Profit Centers, Functional Areas, and Segment

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

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |
| BNI | Create Asset - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Items | Business Condition |
| --- | --- |
| BNI - Create Asset - MDS | Create two asset master records (one in Asset Under Construction asset class and one in Machinery asset class). To create the assets, use the Create Asset - MDS (BNI) master data script using the data described in this test script. |
| BFH - Asset Under Construction | Complete the test procedures in the Asset Acquisition for Constructed Assets (External Procurement) section. Use the asset master record created under the asset class Assets Under Construction for this test script.If you cannot use the asset master record previously created in the Asset Under Construction (BFH) test script, create a new asset under construction and post costs to it using the Post Acquisition (Integrated AP) Without Purchase Order app in the Asset Acquisition for Constructed Assets (External Procurement) section of the Asset Under Construction (BFH) test script. |
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

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create legacy assets with values. These assets may be used for various testing scenarios.

Prerequisites

To take over your legacy data in asset accounting, only one fiscal year can be open. If you receive an error stating that more than one year is open, check that the previous fiscal year is closed in asset accounting. To check, use the Make Company Code Settings - Asset Accounting-Specific (F7312) app. For your company code, the previous fiscal year must be closed.

Procedure

|  |
| --- |
| Note Create five legacy assets with different descriptions. Ensure that the asset description begins with the word Legacy. |

Table 3: Create Asset Master Record for Legacy Asset

| Process Step | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant . |  |  |
| 2 | Access the SAP Fiori app | Open Manage Legacy Assets - Deprecated (F7280) . | The Manage Fixed Assets - Legacy view is displayed. |  |
| 3 | Create Fixed Asset | Choose Create > Create Legacy Asset Main Number . |  |  |
| 4 | Enter Transaction Details | Make the following entries and press Enter:Company Code: For example, 3310Asset Class: For example, <asset class; See the Master Data, Organizational Data, and Other Data topic> |  |  |
| 5 | Enter Transaction Details | Make the following entry:Description: Legacy Asset xxxxxx |  |  |
| 6 | Enter Capitalization Date | Choose the Ledger tab.Make the following entry:Capitalized On: for example, 31/12/2020 ( December 31, 2020)Note This is a prior year asset.Choose the Time- Dependent tab. |  |  |
| 7 | Enter Transaction Details | Make the following entries:Cost Center: For example, 33101301Note You can enter the Cost Center and/or the WBS Element. |  |  |
| 8 | Enter Transaction Details | Choose the Valuation tab.Confirm Key, Life, and Start Date.Note If you activated the feature toggle for the new design, confirm Depreciation Profile, Useful Life, and Start Date. |  |  |
| 9 | Create the Record | Choose Create (at lower right). | Note Make a note of the asset number generated by the system: ______________. |  |

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

## Overview Table

This scope item consists of the process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Define Distribution Rules for Assets under Construction (Periodic Processing)](#unique_12) [page ] 14 | Asset Accountant | Define Distribution Rules - For AuC (AIAB) | The rules for the settlement are maintained. |
| [Execute Settlement for Assets Under Construction (Periodic Processing)](#unique_13) [page ] 15 | Asset Accountant | Execute Settlement - For AuC (AIBU) | Assets under Construction are settled according to their settlement rules. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Define Distribution Rules for Assets under Construction (Periodic Processing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you maintain the settlement rules for the asset under construction (AuC) created in the previous steps.

Prerequisite

You have executed all the previous steps related to Assets under Construction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Define Distribution Rules - For AuC (AIAB). | The Settlement AuC: Initial view is displayed. |  |
| 3 | Maintain Settlement Rule | Make the following entries and choose Execute.Company Code: 3310Asset: <Number of asset>Note The asset number is the asset under construction created in a prior procedure.Ledger: <optional; see note>Note If you enter a ledger value (for example, 0L or 2L), distribution rules should be defined for both ledgers. If you only have distribution rules defined for 0L, enter 0L. If you only have distribution rules defined for 2L, enter 2L. |  |  |
| 4 | Enter Asset Data | To maintain the distribution rule for the local ledger, select the line for ledger 0L and depreciation area 01. Select the document displayed and choose Enter Distribution Rule.Note To maintain the distribution rule for the second ledgers, select a line item for ledger 2L and depreciation area 32.Choose Enter and complete the following values:Cat: <FXA>Asset,Settlement Receivers: <asset number created in previous step> in class 2000%: <number portion of AuC to capitalize> , for example, 90 |  |  |
| 5 | Enter Cost Center Data | Enter the following values:Cat: <CTR> Cost CenterSettlement Receivers: <Number> of Cost Center, for example, 33101301% : <number portion of AuC APC to capitalize>, for example, 10 |  |  |
| 6 | Save Settlement Rule | Choose Back and save the settlement rule. | You maintained the rules for the settlement. The execution of the settlement is part of the periodic processing. |  |

### Execute Settlement for Assets Under Construction (Periodic Processing)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, assets under construction (AuC) are settled according to their settlement rules.

Prerequisite

Settlement rules are maintained for the AuC you want to settle.

|  |
| --- |
| Note Under certain conditions, you may need to capitalize an AuC before all suppliers have presented their closing invoices. This can cause a few difficulties, especially if the closing invoice can’t be posted until the fiscal year following the capitalization of the asset under construction, and down payments were already posted to the AuC. |

Initially, you post the down payment normally. If you then need to capitalize the AuC at the end of the fiscal year, but before the closing invoice is received, you post reserves for the total amount of the expected invoice. You post these reserves directly to the capitalized asset (external acquisition with vendor, transaction type 100). If you plan to distribute the values from the AuC to several final assets, post the reserve to the AuC first and then capitalize it. Whichever method you use, you must reverse the down payment on the AuC, because the down payment isn’t allowed to appear in the account for down payments to fixed assets. Instead, it must appear in the account for completed assets.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Access the SAP Fiori app. | Open Execute Settlement - For AuC (AIBU). | The AuC Settlement: Initial view is displayed. |  |
| 3 | Enter Data | Make the following entries and choose Simulate.Company Code: 3310Asset: <number of asset under construction>Ledger: <ledger (optional)>Note If you enter a ledger value (for example, 0L or 2L), distribution rules should be defined for both ledgers. If you only have distribution rules defined for 0L, enter 0L. If you only have distribution rules defined for 2L, enter 2L.Document date: <document date, for example, Month End 02/28/2020>Asset value date: <asset value date, for example, Month End>Posting date: <posting date, for example, Month End>Period: <derived from Posting Date> | The asset transaction is posted with the document number xxxxxxxxxx. The asset is settled to the receiver. Make note of the document numbers.Note Before doing an actual run, we recommend that you perform a test run. |  |
| 4 | Save | Select the line for the ledger and depreciation area for which you executed the settlement and choose Save. |  |  |

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
- related-to :: [[03-financial-accounting-and-close/asset-under-construction-additional-depreciation-area-5kf-ae-test-scri]]
- related-to :: [[03-financial-accounting-and-close/test-script-asset-under-construction-bfh-ae-sap-s-4hana-cloud-public-e]]
- related-to :: [[03-financial-accounting-and-close/test-script-asset-under-construction-group-ledger-us-gaap-33g-ae-899]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GF_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 29,947 chars in the whole document
