---
id: 03-financial-accounting-and-close/master-data-script-create-asset-bni-sap-s-4hana-cloud-public-edition-6
title: "Master Data Script - Create Asset (BNI), SAP S/4HANA Cloud Public Edition (BNI_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for fixed asset master data: create, change, display, block, delete, sub assets, change documents, depreciation keys."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/fixed-asset-master-data]
aliases: [BNI_S4CLD2608_Master_Data_EN_XX]
keywords: [Fixed Asset Master Records, asset master data, create asset, change asset, block asset, delete asset, sub assets, asset classes, legacy data transfer, asset accounting]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-611
topic: 03-financial-accounting-and-close/fixed-asset-master-data
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script - Create Asset (BNI), SAP S/4HANA Cloud Public Edition (BNI_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **Fixed Asset Master Records** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create Asset - MDS (BNI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc233904938)

[2 Prerequisites 4](#_Toc233904939)

[2.1 System Access 4](#_Toc233904940)

[2.2 Roles 4](#_Toc233904941)

[2.3 Required Organizational Units 4](#_Toc233904942)

[2.4 Mandatory and Optional Master Data 5](#_Toc233904943)

[2.5 Main Parameters for Data Creation 5](#_Toc233904944)

[2.5.1 Asset Classes and Number Ranges 5](#_Toc233904945)

[2.6 Preliminary Steps 7](#_Toc233904946)

[2.6.1 Validate Asset Accounting System Readiness 7](#_Toc233904947)

[2.6.1.1 Confirm Takeover Date Information 7](#_Toc233904948)

[2.6.1.2 Confirm Run of Balance Carry Forward for Current Fiscal Year 9](#_Toc233904949)

[3 Overview Table 11](#_Toc233904950)

[4 Test Procedures 12](#_Toc233904951)

[4.1 Create Asset 12](#_Toc233904952)

[4.2 Change Asset 14](#_Toc233904953)

[4.3 Display Asset 15](#_Toc233904954)

[4.4 Block Assets 16](#_Toc233904955)

[4.5 Delete Asset 16](#_Toc233904956)

[4.6 Create Asset Sub Asset 17](#_Toc233904957)

[4.7 Change Documents for Asset Master Record 19](#_Toc233904958)

[4.8 Depreciation Key: Display Details 20](#_Toc233904959)

## Purpose

A fixed asset is an object, a right, or another item owned by an enterprise that is intended for long-term use and can be individually identified in the balance sheet. Maintaining fixed assets involves creating, changing, and displaying asset master records.

The different items of information are structured according to area of use and functions in the system to make it easier for users to create, maintain, and evaluate master data.

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

### Required Organizational Units

Fixed asset master data is dependent on the organizational unit of the company.

The following table gives an overview of this organizational unit:

| Data Segment | Depends On | Field Examples | Comments | Organizational Unit to be Used |
| --- | --- | --- | --- | --- |
| Company Code Data | Company Code | ID, Description, Cost Center, and so on | Company code data can exist for every company code ID of your enterprise structure for which the fixed asset master record is used. | <your company code> |

### Mandatory and Optional Master Data

Fixed asset master data records may refer to other master data. The following table gives an overview of optional and mandatory master data objects to be used in a fixed asset master data record.

| Master Data Object | Used in Data Segment | Mandatory / Optional | Comments |
| --- | --- | --- | --- |
| Cost Center | In the asset master, you find the entry of cost center in the Time-dependent tab. | Mandatory | In order to enter the fixed asset's cost center, you must have created the cost center before. In the fixed asset master records, you can then enter the actual cost center. |

### Main Parameters for Data Creation

In this section, we describe some basic parameters that influence the behavior of a master record and are always required to create a fixed asset master data record:

#### Asset Classes and Number Ranges

Asset classes determine the number ranges for the fixed asset master record IDs. You cannot change the assignment or IDs afterwards, but only transfer it to another fixed asset master record created for another asset class. If an asset class is assigned to an internal number range, you cannot enter the asset master record ID manually. In this case, leave the field blank as the system automatically chooses a number from the assigned numeric number range.

The following asset classes and corresponding number ranges are defined for fixed assets in company code 1010:

| Asset Class | Number Range / Asset Master record ID | Comments |
| --- | --- | --- |
| 1000 | Internal numeric number range:10000000 – 19999999 | Real Estate and Similar Rights |
| 1100 | Internal numeric number range:10000000 – 19999999 | Buildings |
| 1200Not Relevant For All Countries/Regions | Internal numeric number range:10000000 – 19999999 | Land Improvements |
| 1500Not Relevant For All Countries/Regions | Internal numeric number range:10000000 – 19999999 | Leasehold Improvements |
| 2000 | Internal numeric number range:20000000 – 29999999 | Machinery and Equipment |
| 3000 | Internal numeric number range:30000000 – 39999999 | Fixtures and Fittings |
| 3100 | Internal numeric number range:50000000 – 59999999 | Vehicles |
| 3200 | Internal numeric number range:60000000 – 69999999 | Computer Hardware |
| 3210 | Internal numeric number range:60000000 – 69999999 | Computer Software |
| 3300 | Internal numeric number range:30000000 – 39999999 | Office Equipment |
| 4000 | Internal numeric number range:40000000 – 49999999 | Assets under Construction (Tangible) |
| 4010 | Internal numeric number range:40000000 – 49999999 | Assets under Construction (Intangible) |
| 4001 | Internal numeric number range:40000000 – 49999999 | AuC as Investment Measure (Tangible) |
| 4011 | Internal numeric number range:40000000 – 49999999 | AuC as Investment Measure (Intangible) |
| 5000 | Internal numeric number range:80000000 – 89999999 | Low-value Assets |
| 8200 | Internal numeric number range:90000000 – 99999999 | Goodwill |
| 8300 | Internal numeric number range:80000000 - 89999999 | Other Intangible Assets |
| 9000 | Internal numeric number range:90000000 - 99999999 | Tax only Assets |

### Preliminary Steps

#### Validate Asset Accounting System Readiness

##### Confirm Takeover Date Information

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you confirm values for data takeover date, status, and document type for entering legacy assets.

|  |
| --- |
| Note After the initial content activation is finalized, you must define a take-over date. This defines the current fiscal year and last closed fiscal year in Asset Accounting. The takeover date is critical for system processing, as it identifies the point in time that old asset values are loaded. For SAP S/4HANA Cloud Public Edition systems, this is usually the prior year end day. For example, if the system is in FY-2020 and the company is on a standard calendar Fiscal Year, the TAKEOVER DATE is 12/31/2020. |

|  |
| --- |
| Caution This implies the loading of old legacy assets is as of the year end of 2020. |

Procedure

| Process Step# | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log into the SAP Fiori launchpad as an Asset Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori App | Open Make Company Code Settings - Asset Accounting-Specific (F7312). | The Display Settings for Company Code in Asset Accounting screen is displayed.To switch between change and display mode, choose Change / Display. |  |
| 3 | Select Company Code | Select your company code on the left side of the screen and choose Select Company Code. |  |  |
| 4 | General Settings | Choose the General Settings tab. |  |  |
| 5 | Check the General Settings | Check the status for your Company. | The General Information tab shows your Company Code settings. The Company Code Status should be For Testing. |  |
| 6 | Maintain Parameters for Legacy Data Transfer | In the Legacy Data transfer section, check or change the following entries:Note If required, create a new legacy transfer segment first by choosing Create legacy transfer segment.Transfer Date: for testing purposes set this date to the LAST DAY of the PRIOR FISCAL YEAR ENDLegacy Data Transfer Status: for testing purposes set this status to ONGOING (Other Postings Allowed)Document Type: for testing purposes set this to AANote For the Transfer Date value, this is usually a year end date for a prior year. If you are instructed to use a mid-year date, this would be a month-end date. The date should always move forward (do not change it backward).Note For the Legacy Data Transfer Status value, you have four options:In Preparation: The system allows incomplete customizing settings for the legacy data transfer (No document postings are allowed at this phase.)Ongoing: Only legacy data transfer postings are permitted (For example, other types of postings, acquisition, retirements are not permitted.)Ongoing (Other Postings Allowed): Both legacy data transfer postings and other postings are permitted. This status makes sense when you perform further legacy data transfers in a company code that is already productive.Completed: The legacy data transfer is completed. Legacy Data Transfer postings are not allowed and you are not allowed to create legacy assets. |  |  |
| 7 | Save the Changes | Choose Menu > General > Save. |  |  |

##### Confirm Run of Balance Carry Forward for Current Fiscal Year

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you confirm that Balance Carry Forward has been run for the current fiscal year.

|  |
| --- |
| Note If your implementation does not use a specific ledger, disregard that ledger. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule General Ledger Jobs (F1927). |  |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Details | Make the following entries and choose Step 2:Job Template: Balance CarryforwardJob Name: Balance Carryforward |  |  |
| 5 | Enter Details | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Details | Make the following entries and choose Schedule:Ledger: <ledger>, for example, 0LCompany Code: <company code>Carry Forward to Fiscal Year: <fiscal year>Test Run: Selected | You scheduled the job run as a test run. |  |
| 7 | Review Results | To review the results of your test run, find your run in the Jobs pane and choose the arrow button to the right of its row. |  |  |
| 8 | Run Details | Choose the Run Details tab. Review the log status. |  |  |
| 9 | Productive Run | To perform a productive run, repeat this process, but deselect Test Run. | You scheduled the job run as a productive run. |  |

## Overview Table

This scope item consists of the process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Asset](#unique_12) [page ] 12 | Asset Accountant | Open Manage Fixed Assets (F3425A) | Fixed Asset Master is created on Company Code (Chart of Depreciation) level. |
| [Change Asset](#unique_13) [page ] 14 | Asset Accountant | Open Manage Fixed Assets (F3425A) | Fixed Asset Master is updated. |
| [Display Asset](#unique_14) [page ] 15 | Asset Accountant | Open Manage Fixed Assets (F3425A) | Fixed Asset Master is displayed. |
| [Block Assets](#unique_15) [page ] 16 | Asset Accountant | Open Manage Fixed Assets (F3425A) | Fixed Asset is blocked. |
| [Delete Asset](#unique_16) [page ] 16 | Asset Accountant | Open Manage Fixed Assets (F3425A) | Fixed Asset Master is deleted. |
| [Create Asset Sub Asset](#unique_17) [page ] 17 | Asset Accountant | Open Manage Fixed Assets (F3425A) | Sub asset is created. |
| [Change Documents for Asset Master Record](#unique_18) [page ] 19 | Asset Accountant | Open Manage Fixed Assets (F3425A) | All the past changes of an existing asset master data record (main or sub asset) are displayed. |
| [Depreciation Key: Display Details](#unique_19) [page ] 20 | Asset Accountant | Depreciation Key: Display Details (FAA_DEPRKEY_SHOW)Note If you have activated the feature toggle for the new design, the app Depreciation Key: Display Details (FAA_DEPRKEY_SHOW) will not apply. | With this app, the information about settings behind depreciation keys delivered by standard content is provided. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Asset

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Fixed Assets (F3425A). | The Manage Fixed Assets screen displays. |  |
| 3 | Enter Asset Master Details | Choose Create > Create Main Asset.Make the following entries:Company Code: <Your company code>Asset Class: <Asset class for which you want to create a new asset>Post-capitalization: <Only required if you want to use this master record to post a post-capitalization>A reference asset master data can be used. If this is needed, the asset to be used as reference should be entered in the Asset Main Number field under the Reference section.Choose OK. | The Create Main Asset screen displays. |  |
| 4 | Enter Asset Description and Base Unit of Measure | Make the following entries:Description: <Your asset description>Base Unit of Measure: <Enter the required unit of measure> |  |  |
| 5 | Choose Time Dependant Data Tab | Choose the Time Dependant Data tab. | The Time Dependant Data tab displays. |  |
| 6 | Enter Cost Center | Make the following entries:Cost Center: <Your cost center>WBS_Element: <Your WBS_Element>Note Cost Center and/or WBS_Element are allowed to be entered as cost collector for depreciation. |  |  |
| 7 | Enter Capitalization Date | You only need to enter the Capitalized on date if the asset was created with the post-capitalization indicator.Capitalized on: <Your capitalization date> |  |  |
| 8 | Check Other Tabs | Go to other tabs and make any necessary entries or changes. |  |  |
| 9 | Enter, Check, or Adapt Depreciation Parameters | Make the following entries for all the available depreciation areas:DKey: <Your depreciation key>Note If you have activated the feature toggle for the new design, use the depreciation profile instead of the depreciation key.UseLife: <Useful life in years>Prd: <Useful life in periods> | All the required depreciation parameters are correctly maintained. |  |
| 10 | Save New Asset Master | Choose Create to save your entries. | The asset master record is created. The system message confirms creation and displays the new asset number. |  |

### Change Asset

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can change an existing asset master data record (main or subnumber) as part of your daily business.

|  |
| --- |
| Note Changing the asset class is only possible via an intra-company transfer to a new asset master record created within the new asset class. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Fixed Assets (F3425A). | The Manage Fixed Assets screen displays. |  |
| 3 | Enter Asset Information | Make the following entries:Company Code: <Your company code>Asset: <Your asset number>Choose Go.Select your asset number from the table by using the link with your asset number.On the next screen, choose Edit. | The Manage Fixed Assets screen displays.Note Display, change, and deletion capabilities are available by selecting the asset, choosing the action to be displayed in the dialog box, and then selecting that action again. |  |
| 4 | Change Asset Master | Make any required changes to the asset master data. | The required changes are made. |  |
| 5 | Save the Changed Asset Master | Choose Create to save your entries.Note The system displays a Success notification. You need to verify your changes. | The asset master changes are saved.The performed changes are displayed under the Change Document tab. |  |

### Display Asset

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display an existing asset data record (main or subnumber) as part of your daily business.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Fixed Assets (F3425A). | The Manage Fixed Assets screen displays. |  |
| 3 | Enter Asset Information | Make the following entries:Company Code: <Your company code>Asset: <Your asset number>Subnumber: <Your asset subnumber in case>Choose Go.Select your Asset Number, from the table by using the link with your asset number.Review your asset master record by selecting each Tab page. |  |  |

### Block Assets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you lock an existing asset master data record (main or subnumber) for further acquisitions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Fixed Assets (F3425A). | The Manage Fixed Assets screen displays. |  |
| 3 | Enter Asset Information | Make the following entries and choose Go:Company Code: <Your company code>Asset: <Your asset number> | The Manage Fixed Assets screen displays. |  |
| 4 | Set the Lock Indicator | Select your Asset Number from the table.On the new screen, select Block.Note The Asset <Asset number> blocked notification displays. | The lock indicator is set.The asset is locked against further acquisitions.The performed changes display under the Change Document tab. |  |

### Delete Asset

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can delete an existing asset master data record (main or subnumber).

|  |
| --- |
| Note Only assets without capitalization date and without values can be deleted directly. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Fixed Assets (F3425A). | The Manage Fixed Assets screen displays. |  |
| 3 | Enter Asset Information | Make the following entries and choose Go:Company Code: <Your company code>Asset: <Your asset number> |  |  |
| 4 | Set the Deletion Indicator | Select your Asset Number, and on the new screen, choose Delete. | The indicator is set. |  |
| 5 | Confirm | A Delete object? message displays on the screen. Choose Delete to confirm it. |  |  |

### Create Asset Sub Asset

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create a new asset sub asset data record as part of your daily business.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Fixed Assets (F3425A). | The Manage Fixed Assets screen displays. |  |
| 3 | Enter Main Asset Reference | On the Manage Fixed Assets screen, choose Create Asset > Create Asset Sub Asset.Make the following entries and press Enter:Company Code: <Your company code>Asset: <Asset main number for which you want to create sub asset>Post-capitalization: <Only required if you want to use this master record to post a post-capitalization> | The Create Sub Asset screen displays.The General tab displays. |  |
| 4 | Enter General Data | On the General tab, make the following entries:Asset Description: <Your asset description>Unit of Measure: <Unit of measure>Capitalized on: <Your date> |  |  |
| 5 | Time Dependant Data | Choose the Time Dependant Data tab. |  |  |
| 6 | Cost Center or WBS_Element | Make, check, or adapt the following entries:Cost Center: <Your cost center>Or WBS_Element: <Your WBS_Element> |  |  |
| 7 | Check Other Tabs | Go to the other tabs and make any necessary entries or changes. | All required asset master fields are filled. |  |
| 8 | Enter, Check, or Adapt Depreciation Parameters | For all available depreciation areas, if required, make or adapt the following entries:DKey: <Your depreciation key>Note If you have activated the feature toggle for the new design, use the depreciation profile instead of the depreciation key.UseLife: <Your useful life in years>Prd: <Your useful life in periods> | All required depreciation parameters are correctly maintained. |  |
| 9 | Save New Asset Sub Asset | Save your entries. | The asset master sub asset is created.Sub asset starts with 1, for example, xxxxx-1. |  |

### Change Documents for Asset Master Record

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display all the past changes of an existing asset master data record (main or subnumber).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Fixed Assets (F3425A). | The Manage Fixed Assets screen displays. |  |
| 3 | Enter Asset Information | Make the following entries and choose Go:Company Code: <Your company code>Asset Number: <Your asset number>Asset Subnumber: <Your asset subnumber> | The Changes to Asset Master Records screen displays. |  |

### Depreciation Key: Display Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display all the past changes of an existing asset master data record (main or sub asset).

|  |
| --- |
| Note If you have activated the feature toggle for the new design, the app Depreciation Key: Display Details (FAA_DEPRKEY_SHOW) will not apply. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Depreciation Key: Display Details (FAA_DEPRKEY_SHOW). | The app opens. |  |
| 3 | Enter Asset Information | Make the following entries and choose Execute:Chart of Depreciation: <Chart of depreciation>Depreciation Key: <Depreciation key> | The Depreciation Key <XXXX> in Chart of Depreciation <XXXX> screen displays.The settings behind the selected depreciation key display. |  |

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
- related-to :: [[03-financial-accounting-and-close/mds-bni-613]]
- related-to :: [[03-financial-accounting-and-close/sap-s-4hana-cloud-public-edition-mds-bni-615]]
- related-to :: [[03-financial-accounting-and-close/script-de-dados-mestre-criar-imobilizado-mds-bni-614]]
- related-to :: [[03-financial-accounting-and-close/script-de-datos-maestros-crear-activo-fijo-mds-bni-612]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNI_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 30,114 chars in the whole document
