---
id: 06-management-accounting/test-script-financial-plan-data-upload-from-file-1hb-ae-sap-s-4hana-cl
title: "Test Script: Financial Plan Data Upload from File (1HB_AE) - SAP S/4HANA Cloud Public Edition (1HB_S4CLD2608_BPD_EN_AE)"
description: "SAP Best Practices test script (scope item 1HB_AE, release 2608): uploading, updating, copying, deleting and compressing financial plan data via CSV in Fiori."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/financial-plan-data-and-integrated-planning]
aliases: [1HB_S4CLD2608_BPD_EN_AE]
keywords: [Financial Plan Data Upload and Integrated Financial Planning, financial plan data upload, plan data file format, plan data scope, statistical key figures, actual versus plan reporting, copy plan data, delete plan data, compress plan data, sap analytics cloud integration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1HB_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-723
topic: 06-management-accounting/financial-plan-data-and-integrated-planning
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Financial Plan Data Upload from File (1HB_AE) - SAP S/4HANA Cloud Public Edition (1HB_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1HB_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Financial Plan Data Upload and Integrated Financial Planning** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Financial Plan Data Upload from File (1HB_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847104)

[2 Prerequisites 4](#_Toc232847105)

[2.1 System Access 4](#_Toc232847106)

[2.2 Roles 4](#_Toc232847107)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847108)

[2.4 File Format Requirements 5](#_Toc232847109)

[2.5 Preliminary Steps 7](#_Toc232847110)

[2.5.1 Set Report Relevancy 7](#_Toc232847111)

[2.5.2 Replicate Runtime Hierarchy 8](#_Toc232847112)

[2.5.3 User Settings - Set Controlling Area 9](#_Toc232847113)

[3 Overview Table 11](#_Toc232847114)

[4 Test Procedures 14](#_Toc232847115)

[4.1 Create P&L Actual Data (optional) 14](#_Toc232847116)

[4.2 View P&L Actuals 14](#_Toc232847117)

[4.3 Upload Financial Plan Data 16](#_Toc232847118)

[4.3.1 Template for File Upload 16](#_Toc232847119)

[4.3.2 Prepare File for Cost Center Plan Upload 17](#_Toc232847120)

[4.3.3 Prepare File for Market Segment Plan Upload 18](#_Toc232847121)

[4.3.4 Import Financial Plan Data 19](#_Toc232847122)

[4.3.5 Optional: Display Financial Plan Data Jobs 20](#_Toc232847123)

[4.3.6 P&L Actual versus Plan 21](#_Toc232847124)

[4.4 Update Plan Data 22](#_Toc232847125)

[4.4.1 Prepare File for Additional Cost Center Plan Data Import 23](#_Toc232847126)

[4.4.2 Import Financial Plan Data File 23](#_Toc232847127)

[4.4.3 P&L Actuals versus Plan 24](#_Toc232847128)

[4.4.4 Prepare File with Changes to the Characteristics of Plan Data Scope 26](#_Toc232847129)

[4.4.5 Import Financial Plan Data File 27](#_Toc232847130)

[4.4.6 Optional: Display Financial Plan Data Jobs 28](#_Toc232847131)

[4.4.7 P&L Actuals versus Plan 28](#_Toc232847132)

[4.5 Import Statistical Key Figure Plan Data 30](#_Toc232847133)

[4.5.1 Prepare File for Cost Center Plan Upload 30](#_Toc232847134)

[4.5.2 Import Statistical Key Figure Plan Data 31](#_Toc232847135)

[4.6 Optional: Copy Financial Plan Data 32](#_Toc232847136)

[4.7 Optional: Delete Financial Plan Data 33](#_Toc232847137)

[4.7.1 Optional: Delete Financial Plan Data with Timestamp 33](#_Toc232847138)

[4.7.2 Optional: Set Financial Plan Data to Zero 34](#_Toc232847139)

[4.7.3 Optional: Delete Financial Plan Data 35](#_Toc232847140)

[4.8 Optional: Compress Financial Plan Data 36](#_Toc232847141)

[4.9 Cost Estimate Data Preparation for Transfer from SAP S/4HANA to SAP Analytics Cloud 37](#_Toc232847142)

[4.9.1 Optional: Manage Cost Estimate Item Jobs for SAP Analytics Cloud Integration 37](#_Toc232847143)

[4.9.2 Optional: Schedule Cost Estimate Item Jobs for SAP Analytics Cloud Integration 39](#_Toc232847144)

[4.10 Analytics 40](#_Toc232847145)

[4.10.1 Commitments by Cost Center 40](#_Toc232847146)

[5 Appendix 42](#_Toc232847147)

[5.1 Configure and Extract Financial Plan Data from SAP Analytics Cloud to SAP S/4HANA Cloud Public Edition Systems 42](#_Toc232847148)

## Purpose

Overview

Using the Import P&L Data SAP Fiori application, you can load a semicolon separated file for PLAN data into the SAP S/4HANA Cloud Public Edition application. A template is provided to ensure that the file is successfully loaded into the application. Once uploaded, you can open the Actual versus Plan P&L application to see the results.

|  |
| --- |
| Note The Delete Financial Plan Data (F4074) app may be used to clean up financial plan data entries, but this should be done only as a corrective measure. |

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
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |

For details about the business role content, refer to the Maintenance of SAP Fiori Artefacts for SAP S/4HANA section in the Check S/4HANA Technical Settings (BG0) configuration guide.

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Baseline Package, you can use the following Baseline Package scenario data.

|  |
| --- |
| Note All organizational units and all master data for which you want to plan must exist in the system in order to perform the upload successfully. |

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| G/L Account | any applicable G/L Account |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNG | Create G/L Account and Cost Element - MDS |

### File Format Requirements

Format Values:

Plan data must be formatted as a comma separated values file (CSV file).

All organizational units and all master data for which you want to plan must exist in the system.

For the time-dependent organizational units or master data, the following applies :

- It must exist in the period specified in the same data row
- If period 0 is specified, the master data must exist in period 1
- If a special period is specified, the master data must exist in the last normal period of the fiscal year
- If only the fiscal year is provided, the master data must exist at some time during the fiscal year

The source files in this example should use the following values :

- Category, use PLN as default
- Company Code
- Controlling Area
- Ledger
- Cost Center
- Customer Group
- Account Number
- Fiscal Year
- Posting Period (values defined by fiscal year variant)
- Amount in Global Currency
- Global Currency

Decimal Digits :

The amounts may have a currency sign (for example, €). The import cuts it off and reads the currency code from the next column.

The upload accepts only two decimal digits.

The following decimal marks or thousands indicators may be used :

European format:

- Comma (,) as decimal mark
- Point (.) as thousands indicator

For example, 1.234.567,89

US format:

- Point (.) as decimal mark
- Comma (,) as thousands indicator

For example 1,234,567.89

No decimal mark and no thousands indicator (for example, 12345)

Currency As used by the system, for example, EUR instead of €

CSV Files :

The csv-upload supports the following separators :

- , (comma)
- ; (semi colon)
- . (period)
- | (pipe)

If you use Microsoft Excel to create the CSV file, you can specify the separator in your Microsoft Windows control panel by choosing Region and Language Formats.

The source CSV files must have the following structure :

1. Row: The technical name of the field for which you want to import data.
2. Row: Any explanatory text, for example, the field description.
3. Row: The characteristics defining the plan data scope of the source file flagged by an X (capitalized or non capitalized). For the values of these characteristics, the plan data from the source file overwrites the existing plan data.

To prevent the plan data scope of a source file becomes too big, the app expects a minimal set of characteristics defining the plan data scope.

You must at least flag the following characteristics :

-
    - Category (CATEGORY)
    - Company Code (RBUKRS) or Controlling Area (KOKRS)
    - Fiscal year (RYEAR)

The app reads the plan data starting from the fourth line.

|  |
| --- |
| Note If the third row contains other characters than X, the system assumes that the third row contains plan data and starts reading from there. In this case, the system uses the following default set of characteristics defining the plan data scope :Category (CATEGORY)Company Code (RBUKRS)Fiscal year (RYEAR) |

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

#### User Settings - Set Controlling Area

Purpose

The controlling area must be set before you carry out the first steps in controlling.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Choose User Preferences | Choose the user icon on the top right corner of the screen, and choose Settings.Choose Default Values. | The Default Values dialog box displays. |  |
| 3 | Enter Data | On the CO Area field,enter the following value: A000.Choose Save. | Controlling area A000 is set for your user. |  |

## Overview Table

The scope item Financial Plan Data Upload from File consists of several process steps provided in the following table :

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Create P&L Actual Data (optional)](#unique_11) [page ] 14 | Internal Sales Representative | Refer to Sales Order Processing with Customer Down Payment(BKJ) |  |
| [View P&L Actuals](#unique_12) [page ] 14 | Cost Accountant - Sales | P&L Plan/Actual - Profit and Loss (F1710) | You can view your current actuals in the system and view if there is any plan data previously uploaded in the system. |

Table 2: Upload Financial Plan Data

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Template for File Upload](#unique_13) [page ] 16 | Cost Accountant - Sales | Import Financial Plan Data (F1711) | Planned data is prepared for upload. |
| [Prepare File for Cost Center Plan Upload](#unique_14) [page ] 17 |  |  | Planned data is prepared from an external system for upload. |
| [Prepare File for Market Segment Plan Upload](#unique_15) [page ] 18 |  |  | Market segment plan data is prepared for upload. |
| [Import Financial Plan Data](#unique_16) [page ] 19 | Cost Accountant - Sales | Import Financial Plan Data (F1711) | Financial plan data file imports successfully. |
| [Optional: Display Financial Plan Data Jobs](#unique_17) [page ] 20 | Cost Accountant - Overhead | Display Financial Plan Data Jobs (F4848) | All import jobs that are currently running or that have been completed. |
| [P&L Actual versus Plan](#unique_18) [page ] 21 | Cost Accountant - Sales | P&L Plan/Actual - Profit and Loss (F1710) | Consolidated view of planning from both the Cost Center and Market Segment displays. |

Table 3: Update Plan Data

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Prepare File for Additional Cost Center Plan Data Import](#unique_19) [page ] 23 |  |  | Additional plan data is prepared for comparison. |
| [Import Financial Plan Data File](#unique_20) [page ] 23 | Cost Accountant - Sales | Import Financial Plan Data (F1711) | Financial plan data file successfully imports. |
| [Optional: Display Financial Plan Data Jobs](#unique_17) [page ] 20 | Cost Accountant - Overhead | Display Financial Plan Data Jobs (F4848) | All import jobs that are currently running or that have been completed. |
| [P&L Actuals versus Plan](#unique_21) [page ] 24 | Cost Accountant - Sales | P&L Plan/Actual - Profit and Loss (F1710) | Consolidated view of planning from both the Cost Center and Market Segment displays. |
| [Prepare File with Changes to the Characteristics of Plan Data Scope](#unique_22) [page ] 26 |  |  |  |
| [Import Financial Plan Data File](#unique_20) [page ] 23 | Cost Accountant - Sales | Import Financial Plan Data (F1711) | Financial plan data file imports successfully. |
| [P&L Actuals versus Plan](#unique_23) [page ] 28 | Cost Accountant - Sales | P&L Plan/Actual - Profit and Loss (F1710) | Consolidated view of planning from both the Cost Center and Market Segment displays. |

Table 4: Import Statistical Key Figure Plan Data

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Prepare File for Cost Center Plan Upload](#unique_24) [page ] 30 |  |  | Planned data is prepared from an external system for upload. |
| [Import Statistical Key Figure Plan Data](#unique_25) [page ] 31 | Cost Accountant - Overhead | Import Statistical Key Figure Plan Data (F3779) | Statistical key figure plan data file imports successfully. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Optional: Copy Financial Plan Data](#unique_26) [page ] 32 | Cost Accountant - Overhead | Copy Financial Plan Data (F3396) | Plan data is copied from one Plan Category to another plan category. |
| [Optional: Delete Financial Plan Data with Timestamp](#unique_27) [page ] 33 | Cost Accountant - Overhead | Delete Financial Plan Data - with Timestamp (F4074) | Plan data is deleted based on the timestamp of the plan data entries. |
| [Optional: Set Financial Plan Data to Zero](#unique_28) [page ] 34 | Cost Accountant - Overhead | Set Financial Plan Data to Zero (F4850) |  |
| [Optional: Delete Financial Plan Data](#unique_29) [page ] 35 | Cost Accountant - Overhead | Delete Financial Plan Data (F4851) |  |
| [Optional: Compress Financial Plan Data](#unique_30) [page ] 36 | Cost Accountant - Overhead | Compress Financial Plan Data (F6537) |  |
| [Optional: Manage Cost Estimate Item Jobs for SAP Analytics Cloud Integration](#unique_31) [page ] 37 | Cost Accountant - Overhead | Manage Cost Estimate Item Jobs - for SAP Analytics Cloud Integration (FCOMV_CEPRE_CONF) |  |
| [Optional: Schedule Cost Estimate Item Jobs for SAP Analytics Cloud Integration](#unique_32) [page ] 39 | Cost Accountant - Overhead | Schedule Cost Estimate Item Jobs - for SAP Analytics Cloud Integration (F7750) |  |
| [Commitments by Cost Center](#unique_33) [page ] 40 | Cost Accountant - Overhead | P&L - Plan/Actual/Committed (W0170) | A report showing plan, actual, and commitments for the cost object displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note The optional steps described in this script do not represent a sequential process. They are either/or options and do not need to be carried out in sequence. The choice of which step to execute depends on your business process and requirements. |

### Create P&L Actual Data (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For the upload of planning data, creating sales information allows you to see both actual and plan data at the end of the upload process (optional step).

Procedure

Create and process sales orders: To execute this activity, run the processes such as Sales Order Processing with Customer Down Payment(BKJ).

### View P&L Actuals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can view your current actuals in the system and view if there is any plan data previously uploaded in the system.

|  |
| --- |
| Note P&L actual data is only available if there are processed sales orders in the system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open P&L Plan/Actual - Profit and Loss (F1710). | The P&L - Plan/Actual screen displays. |  |
| 3 | Enter Information | Make the following entries :Ledger: 0L (Ledger 0L)Fiscal Year of Ledger: Current fiscal yearFiscal Period: 005Plan Category: PLNCompany Code : 3310G/L Account Hierarchy:YBA000_CENote The G/L Account Hierarchy YBA000_CE is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement.Key Date: Enter a dateChoose OK. |  |  |
| 4 | Review | You can view the current actuals in the system and check the input of plan data. |  |  |

### Upload Financial Plan Data

#### Template for File Upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you download the template and prepare your plan data for upload. Depending on the scope of your solution, the plan data you fill the template with will differ. In this script you download two templates: Cost Center Planning Data and Market Segment Planning Data. Use the sample data to populate the template. If you have plan data already in your system and would like to copy the data to a new Plan Category, application Copy Financial Plan Data can achieve this without the need to manually upload the data.

|  |
| --- |
| Note If any data exists in the target Plan Category, it will be overwritten by this copy functionality. |

|  |
| --- |
| Note Planning for Cost Centers, Internal Orders, and WBS elements automatically derive the Profit Center and Segment organizational fields from the corresponding Plan/Actual report. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data (F1711) screen displays. |  |
| 3 | Cost Center Planning Template | Choose the Download Templates button. In the Download Templates screen, select the comma as separator and then the Cost Center Planning template.Open the downloaded CSV template.Enter the field values as listed in the step Prepare the File for Cost Center Plan Upload of this script. |  |  |
| 4 | Save Template | Save the file in CSV format. |  |  |
| 5 | Market Segment Planning Template | Repeat all steps in this section, download template Market Segment Planning and enter the field values as listed in the step Prepare the File for Market Segment Plan Upload of this script. |  |  |

#### Prepare File for Cost Center Plan Upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you prepare your plan data from an external system for upload. Fill in the downloaded template Cost Center Planning with the data listed below. The exact same data is presented in two ways: Table and CSV format.

- The table format is for clarity of what data is being entered.
- The CSV format is how the exact data must be entered in the CSV file in order for the upload to be successful.

The file must use one of the four acceptable separators listed in section 2.4 and be saved as a CSV file. In our example, we use a semicolon as the separator.

|  |
| --- |
| Note The data field KSL (Amount) is represented as a positive (debit) or negative (credit) value depending on the accounting view of the G/L account being planned. For example, revenue G/L account plan data would be entered as a negative (credit) in the KSL column. Similarly, expense and asset GL accounts are planned as positive (debit). |

|  |
| --- |
| Caution The following sample is provided as an example only and this may differ from country to country. The global currency (RKCUR) in predelivered content is USD but can vary depending on the actual system setup. Contact your test administrator for specific data on country and global currency. |

Procedure

Review the following cost center plan data :

| CATEGORY | RYEAR | POPER | RBUKRS | RCNTR | RACCT | KSL | RKCUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Category | General Ledger Fiscal Year | Posting Period | Company Code | Cost Center | Account Number | Amount in Global Currency | Global Currency |
| X | X | X | X | X |  |  |  |
| PLN | 2022 | 5 | 3310 | 33101101 | 61003000 | 1000 | USD |
| PLN | 2022 | 5 | 3310 | 33101101 | 65008300 | 2000 | USD |
| PLN | 2022 | 5 | 3310 | 33101101 | 94308000 | 3000 | USD |
| PLN | 2022 | 5 | 3310 | 33101101 | 61007000 | 4000 | USD |

#### Prepare File for Market Segment Plan Upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you prepare your plan data from an external system for upload. Fill in the downloaded template Market Segment Planning with the data listed below. The exact same data is presented two ways: Table and CSV format. The table format is for clarity of what data is being entered. The CSV format is how the exact data must be entered in the CSV file in order for the upload to be successful. The file must use one of the four acceptable separators listed in section 2.4 and be saved as a CSV file. In our example, we use a semicolon as the separator.

|  |
| --- |
| Note The data field KSL (Amount) is represented as a positive (debit) or negative (credit) value dependent on the accounting view of the G/L account being planned. For example, revenue G/L account plan data would be entered as a negative (credit) in the KSL column. Similarly expense and asset GL accounts are planned as positive (debit). |

|  |
| --- |
| Caution The following sample is provided as an example only and this may differ from country to country. Contact your Test administrator for country-specific data. |

Procedure

Review the following market segment plan data :

| CATEGORY | RYEAR | POPER | RBUKRS | MATKL | KDGRP | RACCT | KSL | RKCUR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Category | General Ledger Fiscal Year | Posting Period | Company Code | Material Group | Customer Group | Account Number | Amount in Global Currency | Global Currency |
| X | X | X | X | X | X | X |  |  |
| PLN | 2022 | 5 | 3310 |  | 01Note The field must be entered with 2 digits. | 41000000 | -90000 | USD |
| PLN | 2022 | 5 | 3310 |  | 02Note The field must be entered with 2 digits. | 41001000 | -50000 | USD |

#### Import Financial Plan Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the plan data file is saved in the template, open the Import P&L Plan Data app and select a source file.

The app performs the following checks:

1. The app checks whether the values in the source file are valid. If required, it returns a list of error messages. You must correct the values in the source file until they are all valid before you can proceed.
2. If all values are valid, the app selects the distinct values for all characteristics of the plan data scope (as defined in the third row of the source file).
    - If no plan data exists in the system for any combination of these characteristic values, you can directly import the plan data.
    - If plan data exists in the system for any combination of these characteristic values, the app displays the affected values. It assumes that you want to completely replace the existing plan data by the new plan data import.

|  |
| --- |
| Note One source file must therefore always contain full plan data sets for a certain combination of the characteristics you specified in the third row (the plan data scope). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data (F1711) screen displays. |  |
| 3 | Enter Source File | Use the Browse CSV Files button to select the CSV extension file you wish to upload and choose Enter.Enter the following field value:Source File:Your .CSV file that contains your plan |  |  |
| 4 | File check | The upload performs a check to ensure that the format is correct.Correct any error message that appears. | The selected file contains data that replaces or deletes the following datamessage appears. |  |
| 5 | Review | Once successfully uploaded the message appears.The selected file has the following plan data scope.Note the two informational messages in the upper left of the screen.On the messageYour plan data import will upload X plan items,select the Show Details, review the data and then select the back icon.On the messageYour plan data import will overwrite x items,select the Show Details, review the data and then select the back icon proceed to the next step Import. | The list of the data uploaded appears. |  |
| 6 | Import | Choose Import Source File. | Import successfulmessage appears. |  |

#### Optional: Display Financial Plan Data Jobs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display all import jobs that are currently running or that have been completed.

|  |
| --- |
| Note This step is relevant only if you have imported financial plan data in the [Import Financial Plan Data](#unique_16) [page ] 19 step using background processing. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Financial Plan Data Jobs (F4848). | The Display Financial Plan Data Job screen displays. |  |
| 3 | Enter Selection Criteria | Choose the Go button.Note You can’t create new jobs or copy, cancel, or restart existing jobs in this app. |  |  |

#### P&L Actual versus Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view your current actuals and plan in the system. The P&L Actual versus Plan report shows a consolidated view of planning from both the Cost Center and Market Segment level. Specific reports for Cost Center and Market Segment Actual versus Plan are also available.

|  |
| --- |
| Note P&L actual data is only available if there are processed sales orders in the system. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open P&L Plan/Actual - Profit and Loss (F1710). | The P&L - Plan/Actual screen displays. |  |
| 3 | Enter Information | Make the following entries and choose Go:Ledger : 0L (Ledger 0L)Fiscal Year of Ledger : <Current fiscal year>Fiscal Period : 005Plan Category : PLNKey Date : <Enter a date>Company Code : 3310G/L Account Hierarchy :0102/YCOA/YBA000_CENote The G/L Account Hierarchy YBA000_CE is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement. |  |  |
| 4 | Review | You can view the actuals and plan data. |  |  |

### Update Plan Data

Context

As previously explained, the third row of the file format defines the characteristics of the plan data scope and are files flagged with an X. If more characteristics are flagged with an X, the more specific target plan data is overwritten. Correspondingly, if fewer characteristics are flagged, the broader the population of the target data is overwritten. The characteristics of this functionality also apply to other planning templates available in the Import Financial Plan Data application such as for Project Budgeting. For more information about Project Budgeting, you can view step Upload Planned Costs and Revenues in scope item 4I9 Sales Order Processing with Project Account Assignment.

This example illustrates the effects of changes to the characteristics of the plan data scope.

#### Prepare File for Additional Cost Center Plan Data Import

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you load additional plan data needed for comparison.

Procedure

Prepare a plan csv data file that is similar to the one created in the step Prepare file for Cost Center plan data upload.

For this data file, the column POPER (Fiscal Period), has the value 6. Save the CSV file.

|  |
| --- |
| Note The sample is provided as an example only. |

| CATEGORY | RYEAR | POPER | RBUKRS | RCNTR | RACCT | KSL | RKCUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Category | General Ledger Fiscal Year | Posting Period | Company Code | Cost Center | Account Number | Amount in Global Currency | Global Currency |
| X | X | X | X | X |  |  |  |
| PLN | 2017 | 6 | 3310 | 33101101 | 61003000 | 1000 | USD |
| PLN | 2017 | 6 | 3310 | 33101101 | 65008300 | 2000 | USD |
| PLN | 2017 | 6 | 3310 | 33101101 | 94308000 | 3000 | USD |
| PLN | 2017 | 6 | 3310 | 33101101 | 61007000 | 4000 | USD |

#### Import Financial Plan Data File

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data (F1711) screen displays. |  |
| 3 | Enter Source File | Use the Browse CSV Files button to select the CSV extension file you wish to upload.Enter the following and choose Enter :Source File:Your .CSV file that contains your plan | The plan data scope for the CSV file uploads.The upload performs a check to ensure that the format is correct.Corrections can be made if any error messages appear. |  |
| 4 | Import | Choose Import. | The file import is successful. |  |

#### P&L Actuals versus Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can view both the previously imported plan data for month 5 and the newly imported plan data for month 6.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open P&L Plan/Actual - Profit and Loss (F1710). | The P&L Plan/Actual screen displays. |  |
| 3 | Enter Information | Make the following entries :Ledger : 0L (Ledger 0L)Ledger Fiscal Year : Current fiscal yearFiscal Period : 005 and 006Planning Category : PLNCompany Code : 3310G/L Account (Hierarchy) :YBA000_CENote The G/L Account Hierarchy YBA000_CE is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement.Key Date : Enter a dateChoose OK. |  |  |
| 4 | Review | View Actual versus Plan. | Note The period 5 plan data remains unchanged. |  |
| 5 | Repeat steps 1-4 | Make the following new entries and choose Go:Enter the following Field Values:Ledger : 0L (Ledger 0L)Ledger Fiscal Year : Current fiscal yearFiscal Period : 006Planning Category : PLNCompany Code : 3310G/L Account (Hierarchy) :YBA000_CENote The G/L Account Hierarchy YBA000_CE is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement.Key Date : Enter a date |  |  |
| 6 | Review | View Actual versus Plan. | Note the plan data in period 6. |  |

#### Prepare File with Changes to the Characteristics of Plan Data Scope

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, change the csv file by deselecting the characteristic POPER (Fiscal Period) by removing the X from the third row. Because this file has fewer selection criteria, more data will be overwritten and removed. Specifically, both Period 5 & Period 6 are removed and replaced by this new plan data that only has period 6 data.

Procedure

Prepare a plan csv data file identical to the one created in step Prepare file for additional service plan data import.

Note the change to the table for the value POPER (Posting Period), in the row 3, the value from X was changed to blank. Save the csv file.

|  |
| --- |
| Caution The sample is provided as an example only. |

| CATEGORY | RYEAR | POPER | RBUKRS | RCNTR | RACCT | KSL | RKCUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Category | General Ledger Fiscal Year | Posting Period | Company Code | Cost Center | Account Number | Amount in Global Currency | Global Currency |
| X | X |  | X | X |  |  |  |
| PLN | 2017 | 6 | 3310 | 33101101 | 61003000 | 1000 | USD |
| PLN | 2017 | 6 | 3310 | 33101101 | 65008300 | 2000 | USD |
| PLN | 2017 | 6 | 3310 | 33101101 | 94308000 | 3000 | USD |
| PLN | 2017 | 6 | 3310 | 33101101 | 61007000 | 4000 | USD |

#### Import Financial Plan Data File

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data (F1711) screen displays. |  |
| 3 | Enter Source File | Use the Browse CSV Files button to select the CSV extension file you wish to upload.Enter the following and choose Enter :Source File:Your .CSV file that contains your plan | The plan data scope for the CSV file uploads.The upload performs a check to ensure that the format is correct.Corrections can be made if any error messages appear. |  |
| 4 | Import | Choose Import. | The file import is successful. |  |

#### Optional: Display Financial Plan Data Jobs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display all import jobs that are currently running or that have been completed.

|  |
| --- |
| Note This step is relevant only if you have imported financial plan data in the [Import Financial Plan Data](#unique_16) [page ] 19 step using background processing. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Financial Plan Data Jobs (F4848). | The Display Financial Plan Data Job screen displays. |  |
| 3 | Enter Selection Criteria | Choose the Go button.Note You can’t create new jobs or copy, cancel, or restart existing jobs in this app. |  |  |

#### P&L Actuals versus Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can view the results of removing the update characteristic POPER.

As a result of the removing the flag (X) from the characteristic POPER (Fiscal Period), the applicable records updated are no longer limited to a specific fiscal period. The plan therefore updates all plan, company code, cost center, customer, G/L, year matches. Since the file provided no data from period 5, the previous values are removed. Only period 6 data was in this file and therefore only plan data 6 is available for all periods that match the selection criteria.

The more specific characteristics chosen through the flag with an X in the third row, the more targeted plan data population is updated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open P&L Plan/Actual - Profit and Loss (F1710). | The P&L Plan/Actual screen displays. |  |
| 3 | Enter Information | Make the following entries and choose Go :Ledger : 0L (Ledger 0L)Fiscal Year of Ledger : <Current fiscal year>Fiscal Period : 005Plan Category : PLNKey Date : <Enter a date>Company Code : 3310G/L Account Hierarchy:YBA000_CENote The G/L Account Hierarchy YBA000_CE is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement. |  |  |
| 4 | Review | View Actual versus Plan. | Note the changes in period 5 plan data. |  |
| 5 | Repeat steps 1-4 | Make the following entries and choose Go :Ledger : 0L (Ledger 0L)Fiscal Year of Ledger : <Current fiscal year>Fiscal Period : 006Plan Category : PLNKey Date : <Enter a date>Company Code : 3310G/L Account Hierarchy:YBA000_CENote The G/L Account Hierarchy YBA000_CE is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement. |  |  |
| 6 | Review | View Actual versus Plan. | Note the plan data in period 6. |  |

### Import Statistical Key Figure Plan Data

Context

Plan statistical key figures are used to create relative weighted values for use in allocations like overhead. Common statistical key figures include headcount and square footage.

#### Prepare File for Cost Center Plan Upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

There is no template to download for import plan statistical key figures. In this activity, you prepare your plan data from an external system for upload. Fill in the downloaded template Cost Center Planning with the data listed below. The exact same data is presented in two ways: Table and CSV format.

- The table format is for clarity of what data is being entered.
- The CSV format is how the exact data must be entered in the CSV file in order for the upload to be successful.

The file must use one of the four acceptable separators listed in section 2.4 and be saved as a CSV file. In our example, we use a semicolon as the separator.

|  |
| --- |
| Note The data field KSL (Amount) is represented as a positive (debit) or negative (credit) value depending on the accounting view of the G/L account being planned. For example, revenue G/L account plan data would be entered as a negative (credit) in the KSL column. Similarly, expense and asset GL accounts are planned as positive (debit). |

|  |
| --- |
| Caution The following sample is provided as an example only and this may differ from country to country. Contact your test administrator for country-specific data. |

Procedure

Review the following statistical key figure plan data :

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CATEGORY | KOKRS |  | RCNTR |  | RBUKRS | RYEAR | POPER | MSL | RUNIT | STAGR |
| Category | Controlling Area |  | Cost Center |  | Company Code | General Ledger Fiscal Year | Posting Period | Quantity | Quantity Unit | Statistical Key Figure |
| X | X |  | X |  | X | X | X |  |  | X |
| PLN | A000 |  | 33101101 |  | 3310 | 2017 | 11 | 100 | PC | 1001 |
| PLN | A000 |  | 33101301 |  | 3310 | 2017 | 11 | 50 | PC | 1001 |

Here is a sample view of the CSV comma delimited file of the statistical key figure plan data :

CATEGORY;KOKRS;RCNTR;RBUKRS;RYEAR;POPER;MSL;RUNIT;STAGR

Version;Controlling Area;Cost center;Company Code;Fiscal Year;Fiscal Period;Quantity;Quantity Unit;Statistical Keyfigure

x;x;x;x;x;x;;;x

PLN;A000;10101101;1010;2018;11;100;PC;1001

PLN;A000;10101301;1010;2018;11;50;PC;1001

#### Import Statistical Key Figure Plan Data

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Import Statistical Key Figure Plan Data (F3779). | The Import Statistical Key Figure Plan Data (F3779) screen displays. |  |
| 3 | Enter Source File | Use the Browse button to select the CSV extension file you wish to upload.Enter the following Field Value:Source File :Your .CSV file that contains your planChoose Enter | The Plan Data Scope for the CSV file uploads.The upload performs a check to ensure that the format is correct.Corrections can be made if any error messages appear. |  |
| 4 | Import | Choose Import Source File. | The file import is successful. |  |

### Optional: Copy Financial Plan Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can copy plan data from one plan category, such as PLN, to a new plan category. You can create a new plan category via the configuration activity Maintain Category for Planning.

When you create a new plan category, you must ensure that the new category matches the category from which you wish to copy data, PLN in this case, and also select the checkboxes allowing for import, copy, and delete.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Copy Financial Plan Data (F3396). | The Copy Financial Plan Data (F3396) screen displays. |  |
| 3 | Enter Parameters | Enter the following values and choose Copy to Target Category:Plan Category: PLNLedger: 0LFiscal Year of Ledger: <Current fiscal year>Fiscal Period: <Enter fiscal periods to copy, for example, between 1 and 12>Company Code: 3310 | The Select Target Category pop up appears. |  |
| 4 | Enter Target Category | In the Target Category parameter, use the search help to specify the Plan Category you wish to copy data to and choose Copy. | The file import is successful. |  |

### Optional: Delete Financial Plan Data

#### Optional: Delete Financial Plan Data with Timestamp

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, you can delete plan data based on the timestamp of the plan data entries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Delete Financial Plan Data - with Timestamp (F4074). | The Delete Financial Plan Data - with Timestamp (F4074) screen displays. |  |
| 3 | Enter Parameters | Enter the following values and choose Delete All:Plan Category: Category you've created in step Copy Financial Plan DataLedger: 0LLedger Fiscal Year: Current fiscal yearFiscal Period: Enter fiscal periods such as between 1 and 12Company Code: 3310Timestamp: Use the selection help to find the timestamp of the data you wish to delete |  |  |
| 4 | Confirm deletion | You can confirm deletion of the plan data. |  |  |

#### Optional: Set Financial Plan Data to Zero

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can remove plan values without deleting them from the database. This process involves writing delta records and setting the corresponding values to zero. This feature allows you to adjust outdated data from past plan data imports, enhancing the consistency of your plan data. This could be beneficial, for instance, when you need to reduce costs due to cost-saving initiatives and want these changes to be reflected in your current plan data version.

|  |
| --- |
| Note This functionality is valid for plan category application type Periodic Planning and Consolidation. By Deleting Financial Plan Data checkbox is enabled and Availability Control option (Availability Control option is valid only for Usage 001 and 002) of the plan category are not selected in the configuration. Planning categories with the Availability Control option are not displayed in the application. |

|  |
| --- |
| Note To test this functionality, it's advisable to use a plan category created specifically for testing purposes without altering the default settings delivered by SAP. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Set Financial Plan Data to Zero (F4850). | The Set Financial Plan Data to Zero screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following values and choose Go:Plan Category: <Periodic plan category that is allowed for deletion>Ledger: 0LFiscal Year of Ledger: <Current year>Fiscal Period: <required period for which you want to set zero>Company Code: 3310 | Note You can use the Related Apps button to display financial plan data, open application logs and other activities. |  |
| 4 | Set All to Zero | Once you have analyzed the data, choose Set All to Zero. |  |  |

#### Optional: Delete Financial Plan Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this optional step, the selected data is permanently and irreversibly deleted. You can rectify errors in previous plan data imports to ensure the consistency of your plan data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Delete Financial Plan Data (F4851). | The Delete Financial Plan Data screen displays. |  |
| 3 | Enter Parameters | Enter the following values and choose Delete All:Plan Category: <Category you've created in step Copy Financial Plan Data>Ledger: 0LLedger Fiscal Year: <Current fiscal year>Fiscal Period: <Enter fiscal periods such as between 1 and 12>Company Code: 3310Timestamp: <Use the selection help to find the timestamp of the data you wish to delete> | Only plan category that are allowed for deletion will show up in Plan Category. |  |
| 4 | Confirm deletion | You can confirm deletion of the plan data. | Caution The selected data is permanently and irreversibly deleted. |  |

### Optional: Compress Financial Plan Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can compress financial plan data items. The app allows you to reduce the number of plan data items stored in planning table ACDOCP. Compressing plan data permanently and irrevocably erases the history of changes, retaining only the most recent snapshot of the plan data as of the current moment.Using this app to compress plan data can reduce the size of table ACDOCP, which can improve the overall performance of planning processes. For more details, refer [here](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1cbcff7ccd35405ab445b223c1ab1588/276a7cdff302443988368552aedc3fbe.html?state=TEST).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Compress Financial Plan Data (F6537). | The Compress Financial Plan Data screen displays. |  |
| 3 | Enter Parameters | Enter the following values and choose Compress All:Plan Category: <Category you've created in step Copy Financial Plan Data>Ledger: 0LLedger Fiscal Year: <Current fiscal year>Fiscal Period: <Enter fiscal periods such as between 1 and 12>Company Code: 3310 | Only plan category that are allowed for deletion will show up in Plan Category. |  |
| 4 | Confirm Compression | You can confirm compression of the plan data. | Caution Once you carry out the compression process, you cannot be able to restore the history of changes. |  |

### Cost Estimate Data Preparation for Transfer from SAP S/4HANA to SAP Analytics Cloud

#### Optional: Manage Cost Estimate Item Jobs for SAP Analytics Cloud Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To resolve performance issues when exporting cost estimates to SAP Analytics Cloud, you can set up a job to precalculate values and store them in an additional buffer table. In this step, you can define selection criteria for the precalculation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Cost Estimate Item Jobs - for SAP Analytics Cloud Integration (FCOMV_CEPRE_CONF). | The Configuration ID for Cost Estimate Item Jobs screen displays. |  |
| 3 | Create Entries | Choose the New Entries button and enter the following values:Configuration ID: <enter a configuration ID, for example PYC1_ENH>Description: <PYC1 Enhancement>Select the configuration ID row and double-click Filter Settings for Cost Estimate Item Jobs. | The Filter Settings for Cost Estimate Item Jobs screen displays. |  |
| 4 | Filter Settings | Choose New Entries. Add the following:1st row:SAP S/4HANA Field: PLANTInclude/Exclude: IncludeSelection Option: EQLow Value: 3310>2nd row:SAP S/4HANA Field: Costing VariantInclude/Exclude: IncludeSelection Option: EQLow Value: PYC1Save the entries. |  |  |

#### Optional: Schedule Cost Estimate Item Jobs for SAP Analytics Cloud Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can use the job template defined in the earlier step, and schedule regular jobs to mitigate performance issues during cost estimate exports to SAP Analytics Cloud.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Schedule Cost Estimate Item Jobs - for SAP Analytics Cloud Integration (F7750). | The Schedule Cost Estimate Job for Integration screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job view displays. |  |
| 4 | Enter Selection Criteria | In the Template Selection section, make the following entries:Job Template: Cost Estimate Job for Integration with SAP Analytics CloudJob Name: Cost Estimate Job for Integration with SAP Analytics CloudChoose Step 2. | The Scheduling Options view displays. |  |
| 5 | Scheduling Options | Select Start Immediately checkbox and choose Step 3. | The Parameters view display. |  |
| 6 | Parameters | Make the following entries:Configuration ID: <Use the dropdown to select the configuration ID PYC1_ENH created in previous step>Test: Deselect |  |  |
| 7 | Schedule Job | Choose the Schedule button. | Precalculated values are calculated and stored in buffer table. |  |

### Analytics

#### Commitments by Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report shows the plan, actual, and committed data to be viewed by cost center and cost elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open P&L - Plan/Actual/Committed (W0170). | The P&L - Plan/Actual/Committed screen displays. |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Key Date: <today's date>Ledger:0LPlan Category: PLNFiscal Year of Ledger: <Current fiscal year>G/L Account Hierarchy: 0102/YCOA/YBA000_CECompany Code: 3310Cost Center: <enter your desired cost center> | A report showing plan, actual, and commitments for the cost object displays. |  |

## Appendix

### Configure and Extract Financial Plan Data from SAP Analytics Cloud to SAP S/4HANA Cloud Public Edition Systems

Prerequisites

You must initially set up the integration and configure the OAuth client. To do so, see here:

[Integrating SAP Analytics Cloud with SAP S/4HANA Cloud Public Edition](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1cbcff7ccd35405ab445b223c1ab1588/2f610a5f08cb4142ac188c3e6a127b4e.html)

Procedure

To configure and extract plan data, follow the instructions provided in the links below:

- [Manage Financial Plan Data Jobs for SAP Anaytics Cloud Integration](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1cbcff7ccd35405ab445b223c1ab1588/c28c3b25b5af49649756fea55d408773.html)
- [Schedule Financial Plan Data Jobs for SAP Anaytics Cloud Integration](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1cbcff7ccd35405ab445b223c1ab1588/15739143dc4d40f88ae7ff5e71ee0417.html)

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
> Flagged while digesting this document, not verified: The Purpose note refers to Delete Financial Plan Data (F4074), but later sections name F4074 as Delete Financial Plan Data - with Timestamp and F4851 as Delete Financial Plan Data, so the app ID for the corrective-deletion app is inconsistent within the document.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Sample plan data years are inconsistent: the base cost center and market segment files use fiscal year 2022, while the follow-up update files and the statistical key figure table use 2017 and the statistical key figure CSV sample uses 2018 (with cost center 10101101 and company code 1010 versus 33101101 and 3310 in the table), although the verification steps use the current fiscal year.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/test-script-sap-s-4hana-cloud-public-edition-integrated-financial-plan]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1HB_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 68,366 chars in the whole document
