---
id: 16-two-tier-erp-and-central-finance/two-tier-subsidiary-as-financial-planning-and-upload-of-plan-data-from
title: Two-Tier – Subsidiary as Financial Planning and Upload of Plan data from Headquarters (1HB) (S4CLD2608_2T_Financial Plng_upload_plan)
description: SAP Cloud ERP Customer Guide and test script for uploading HQ plan data via CSV into a subsidiary (Import Financial Plan Data) and comparing P&L actual vs plan.
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/financial-planning-hq-and-subsidiary]
aliases: [S4CLD2608_2T_Financial Plng_upload_plan]
keywords: [Two-Tier Financial Planning, financial plan upload, two-tier erp, csv file format, plan data scope, p&l actual versus plan, cost center planning, market segment planning, report relevancy, runtime hierarchy replication]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T_Financial Plng_upload_plan.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-226
topic: 16-two-tier-erp-and-central-finance/financial-planning-hq-and-subsidiary
language: ""
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Two-Tier – Subsidiary as Financial Planning and Upload of Plan data from Headquarters (1HB) (S4CLD2608_2T_Financial Plng_upload_plan)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T_Financial Plng_upload_plan.docx`, extracted with `mammoth`. Grouped under **Two-Tier Financial Planning** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| SAP Cloud ERP June 2026English |  |
|  | Two-Tier – Subsidiary as Financial Planning and Upload of Plan data from Headquarters (1HB) |
|  | Customer Guide |

Copyright

© 2020 SAP SE or an SAP affiliate company. All rights reserved.

No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE. The information contained herein may be changed without prior notice.

Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors.

National product specifications may vary.

These materials are provided by SAP SE and its affiliated companies ("SAP Group") for informational purposes only, without representation or warranty of any kind, and SAP Group shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP Group products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE in Germany and other countries. Please see http://www.sap.com/corporate-en/legal/copyright/index.epx#trademark for additional trademark information and notices.

| Revision | Change Date | Description |
| --- | --- | --- |
| 0 | 01.09.2017 | Initial version of document |
|  |  |  |

Only add a revision when corrections are made to a published document. Do not change the original published date. Set back to revision 0 after a full upgrade of the Customer Guide.

Icons

| Icon | Meaning |
| --- | --- |
| <!-- image omitted: unnamed --> | Caution |
| <!-- image omitted: unnamed --> | Example |
| <!-- image omitted: unnamed --> | Note |
| <!-- image omitted: unnamed --> | Recommendation |
| <!-- image omitted: unnamed --> | Syntax |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example text | Words or characters that appear on the screen. These include field names, screen titles, pushbuttons as well as menu names, paths and options.Cross-references to other documentation. |
| Example text | Emphasized words or phrases in body text, titles of graphics and tables. |
| EXAMPLE TEXT | Names of elements in the system. These include report names, program names, transaction codes, table names, and individual key words of a programming language, when surrounded by body text, for example, SELECT and INCLUDE. |
| Example text | Screen output. This includes file and directory names and their paths, messages, source code, names of variables and parameters as well as names of installation, upgrade and database tools. |
| EXAMPLE TEXT | Keys on the keyboard, for example, function keys (such as F2) or the ENTER key. |
| Example text | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example text> | Variable user entry. Pointed brackets indicate that you replace these words and characters with appropriate entries. |

**Contents**

[1 Purpose 6](#_Toc494191139)

[2 Value Proposition 6](#_Toc494191140)

[2.1 Business Requirements 6](#_Toc494191141)

[2.2 Two--Tier Solution 6](#_Toc494191142)

[3 Business Process Details 7](#_Toc494191143)

[3.1 Prerequisites 7](#_Toc494191144)

[3.2 Process Flow with Technical Details 7](#_Toc494191145)

[4 Technical Requirement 8](#_Toc494191146)

[4.1 Integration Requirements by using API 8](#_Toc494191147)

[4.2 Integration Requirements by using EDI/IDOC 8](#_Toc494191148)

[4.3 Reporting Requirements by using Analytical CDS Views 8](#_Toc494191149)

[4.4 Reporting Requirements by using Analytical API 8](#_Toc494191150)

[5 Test Script 8](#_Toc494191151)

[1 Purpose 9](#_Toc494191152)

[2 Prerequisites 10](#_Toc494191153)

[2.1 System Access 10](#_Toc494191154)

[2.2 Roles 10](#_Toc494191155)

[2.3 Master Data, Organizational Data, and Other Data 10](#_Toc494191156)

[2.4 File Format Requirements 10](#_Toc494191157)

[2.5 Preliminary Steps 12](#_Toc494191158)

[2.5.1 User Settings - Set Controlling Area in subsidiary SAP S/4HANA cloud system. 12](#_Toc494191159)

[2.5.2 Setting Report Relevancy in subsidiary SAP S/4HANA cloud system. 13](#_Toc494191160)

[2.5.3 Replicate Runtime Hierarchy in subsidiary SAP S/4HANA cloud system. 14](#_Toc494191161)

[3 Overview Table 15](#_Toc494191162)

[4 Test Procedures 16](#_Toc494191163)

[4.1 Create P&L Actual Data (optional) 16](#_Toc494191164)

[4.2 View P&L Actuals 16](#_Toc494191165)

[4.3 Profit and Loss File Upload 18](#_Toc494191166)

[4.3.1 Template for file upload 18](#_Toc494191167)

[4.3.2 Prepare the file for Cost Center Plan upload 19](#_Toc494191168)

[4.3.3 Prepare the file for Market Segment Plan upload 21](#_Toc494191169)

[4.3.4 Importing the P&L File 22](#_Toc494191170)

[4.4 P&L Actual versus Plan 24](#_Toc494191171)

[4.5 Updating Plan Data 26](#_Toc494191172)

[4.5.1 Prepare file for additional Cost Center plan data import 26](#_Toc494191173)

[4.5.2 Importing the P&L File 28](#_Toc494191174)

[4.5.3 P&L Actuals versus Plan 29](#_Toc494191175)

[4.5.4 Prepare file with changes to the characteristics of the plan data scope 31](#_Toc494191176)

[4.5.5 Importing the P&L File 33](#_Toc494191177)

[4.5.6 P&L Actuals versus Plan 34](#_Toc494191178)

[6 Appendix 38](#_Toc494191179)

[6.1 Relevant Scope ID’s / Test Scripts 38](#_Toc494191180)

**Subsidiary as Financial Planning and Upload of Plan data from Head Quarters**

## Purpose

This document will provide the detailed process on Two-Tier approach where “Subsidiary as Financial Planning and Plan data upload from Headquarters” with process flow, technical requirements and followed with testing procedure.

## Value Proposition

In a Two-Tier scenario where the headquarter is running OP and the subsidiary is running on SAP S/4HANA Cloud Public Edition, headquarter can trigger the group level planning and import the planning data into the subsidiary.

### Business Requirements

Headquarter needs to share the planning data to the subsidiaries to perform the group level financial planning.

### Two--Tier Solution

With Two-Tier approach SAP Cloud ERP solution will be deployed on subsidiary and integrates with Headquarters which runs on S/4HANA OP / SAP Cloud ERP Private/ECC solutions.

The following business benefits will be achieved with Two-Tier approach.

- Standardization of Financial planning across HQ and subsidiaries.
- Subsidiary can report Plan versus Actual report based on the imported plan data.
- Enable load from any source system that can produce a flat file.
- Access an SAP Fiori interface as a user with an authorized profile.

## Business Process Details

This scope item simulates a Two-Tier scenario where the headquarter is running OP and the subsidiary is running on SAP Cloud ERP, headquarter can trigger the group level planning and import the planning data into the subsidiary.

Using the Import P&L Data Fiori application, you can load a semicolon separated file for PLAN data into the SAP Cloud ERP application. Once uploaded, the user can open the Actual versus Plan P&L application to see the results.

**Key Process Steps Covered**

- Load data in SAP Cloud ERP
- Run report P&L Plan/Actual
- Load revised or additional plan data

### Prerequisites

The following list of prerequisites are to be in place to realize the business process

- Connection/Integration between Headquarter and Subsidiary system
- Master data synchronization between Headquarter and Subsidiary

### Process Flow with Technical Details

<!-- image omitted: unnamed -->

## Technical Requirement

### Integration Requirements by using API

N/A

### Integration Requirements by using EDI/IDOC

N/A

### Reporting Requirements by using Analytical CDS Views

N/A

### Reporting Requirements by using Analytical API

N/A

## Test Script

## Purpose

This scope item enabales using Import P&L Data Fiori application acting as a subsidiary SAP Cloud ERP system. User can load a semicolon separated file for PLAN data into the SAP Cloud ERP application. A template (data from Headquarters) is provided to ensure that the file is successfully loaded into the SAP Cloud ERP application. Once uploaded, the user can open the Actual versus Plan P&L application to see the results.

This document provides a detailed procedure for testing the scope item after solution deployment, reflecting the predefined scope of the solution. Each process step is covered in its own section, providing the system interactions (that is, test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly (see the Test Step column).

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| System | On-Premise SAP S/4HANA |

### Roles

Use the following standard test users or assign roles to testers, respectively:

| Business Role Name | Business Role ID | LogOn |
| --- | --- | --- |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT |  |

For details about the business role content, refer to the Maintenance of SAP Fiori Artefacts for SAP S/4HANA section in the Check S/4HANA Technical Settings (BG0) configuration guide.

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure.

Note All organizational units and all master data for which you want to plan must exist in the system in order to perform the upload successfully.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1710 |  |  |
| G/L Account | any applicable G/L Account |  |  |

### File Format Requirements

Format Values:

Plan data must be formatted as a comma separated values file (CSV file).

All organizational units and all master data for which you want to plan must exist in the system.

For the time-dependent organizational units or master data, the following applies:

- It must exist in the period specified in the same data row
- If period 0 is specified, the master data must exist in period 1
- If a special period is specified, the master data must exist in the last normal period of the fiscal year
- If only the fiscal year is provided, the master data must exist at some time during the fiscal year

The source files in this example should use the following values:

- Category, as default, use the category PLN
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

Decimal Digits:

The amounts may have a currency sign (for example, €). The import cuts it off and reads the currency code from the next column.

The upload accepts only two decimal digits.

The following decimal marks or thousands indicators may be used:

European format:

- Comma (,) as decimal mark
- Point (.) as thousands indicator

For example, 1.234.567,89

US format:

- Point (.) as decimal mark
- Comma (,) as thousands indicator

For example, 1,234,567.89

No decimal mark and no thousands indicator (for example, 12345)

Currency As used by the system, for example, EUR instead of €

CSV Files:

The csv-upload supports the following separators:

- , (comma)
- ; (semi colon)
- . (period)
- | (pipe)

If you use Microsoft Excel to create the CSV file, you can specify the separator in your Microsoft Windows control panel by choosing Region and Language Formats.

The source CSV files must have the following structure:

1. Row: The technical name of the field for which you want to import data.
2. Row: Any explanatory text, for example, the field description.
3. Row: The characteristics defining the plan data scope of the source file flagged by an X (capitalized or non capitalized). For the values of these characteristics, the plan data from the source file overwrites the existing plan data.

To prevent the plan data scope of a source file becomes too big, the app expects a minimal set of characteristics defining the plan data scope.

You must at least flag the following characteristics:

-
    - Category (CATEGORY)
    - Company Code (RBUKRS) or Controlling Area (KOKRS)
    - Fiscal year (RYEAR)
    - Ledger (RLDNR)

The app reads the plan data starting from the fourth line.

If the third row contains other characters than X, the system assumes that the third row contains plan data and starts reading from there. In this case, the system uses the following default set of characteristics defining the plan data scope:

- Category (CATEGORY)
- Company Code (RBUKRS)
- Fiscal year (RYEAR)
- Ledger (RLDNR)

### Preliminary Steps

Assuming for Two-Tier scenario Headquarters is running on On-Premise/ SAP Cloud ERP Private and subsidiary on SAP Cloud ERP System.

#### User Settings - Set Controlling Area in subsidiary SAP S/4HANA Cloud Public Edition system.

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon to SAP Fiori launchpad | Logon to the SAP Fiori launchpad as a Cost Accountant - Overhead . | The SAP Fiori launchpad displays. |  |
| 2 | Choose User Preferences | Choose User Cost Accountant - Overhead (to the right of the screen), and choose Settings.Choose Default Values. | The Default Values screen displays. |  |
| 3 | Enter Data | On the CO Area field,enter the following value: A000.Choose Save. | Controlling area A000 is set for your user. |  |

#### Setting Report Relevancy in subsidiary SAP Cloud ERP.

Report relevancy must be done when you execute any design studio reports for first time. If you make a subsequent change in cost center, profit center, or GL hierarchy, perform this step again to get the latest information.

Also, you must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally this would be created as a periodic job that would run in the background.

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon to SAP Fiori launchpad | Logon to the SAP Fiori launchpad as a Overhead Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Set Report Relevancy. | The Application Jobs screen displays. |  |
| 3 | Enter Header Data | In the header area, make the following entries :Set Class: For example, 0101 cost center groupOrganizational Unit: A000Set Name: A000 |  |  |
| 4 | Execute | Choose Execute. |  |  |
| 5 | Mark as report relevant | In the header Set Report Relevancy for Set-Based Hierarchies, make the following entries :Set Name: A000Report Relevant: Select |  |  |
| 6 | Save | Choose Save. |  |  |

#### Replicate Runtime Hierarchy in subsidiary SAP Cloud Public Edition system.

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log onto SAP Fiori launchpad | Log onto the SAP Fiori launchpad as a Overhead Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Replicate Runtime Hierarchy. | The Replicate Runtime Hierarchy screen displays. |  |
| 3 | Select | Choose New. |  |  |
| 4 | Enter Header Data | In the header area, make the following entries:Job Template: Manually replicater Runtime hierarchyJob Name: Manual testStart Immediately: SelectHierarchy ID: YCOAValid From: Enter current date |  |  |
| 5 | Select | Choose Schedule. |  |  |

## Overview Table

The scope item Profit and Loss Plan Data Load from File consists of several process steps provided in the following table:

Master Data

| Process Step | Source | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- | --- |
| Profit and Loss data | Headquarters | Accountant | S_ALR_87012270 |  |
| Create P&L Actual Data (optional) | Subsidiary | Internal Sales Representative |  |  |
| View P&L Actual | Subsidiary | Cost Accountant - OVERHEAD_ACCOUNTANT | P&L Plan Actuals |  |
| Profit and Loss File Upload | Subsidiary | Cost Accountant - OVERHEAD_ACCOUNTANT | Import Financial Plan Data |  |
| P&L Actual versus Plan | Subsidiary | Cost Accountant - OVERHEAD_ACCOUNTANT | P&L Plan Actual |  |
| Updating Plan Data | Subsidiary | Cost Accountant - OVERHEAD_ACCOUNTANT |  |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create P&L Actual Data (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

For the upload of planning data, creating sales information allows you to see both actual and plan data at the end of the upload process (optional step).

Procedure

Create and process sales orders: To execute this activity, run the processes such as Sales Order Processing with Customer Down Payment(BKJ).

### View P&L Actuals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you can view your current actuals in the SAP S/4HANA Cloud Public Edition system and view if there is any plan data previously uploaded in the system.

Note P&L actual data is only available if there are processed sales orders in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Overhead Accountant.. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open P&L Plan/Actual. |  |  |
| 3 | Enter Information | Make the following entries :Fiscal Year : Current fiscal yearCategory: PLNFiscal Period : 005Company Code : 1710G/L Account (Hierarchy):YCOA (Sample Grouping of P&L)Note The G/L Account Hierarchy YCOA is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement.Choose Go. |  |  |
| 4 | Review | Note, overall values and if any plan data is entered. |  |  |

### Profit and Loss File Upload

#### Template for file upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you download the pre-delivered template and prepare your plan data for upload. Depending on the scope of your solution the actual data you fill the template will differ. In this script you download two templates: Cost Center Planning Data and Market Segment Planning Data. Use the sample data in the preceding labeled sections to populate the template.

Note Planning for Cost Centers, Internal Orders, and WBS elements automatically derive the Profit Center and Segment organizational fields that are reflected in the corresponding Plan/Actual report.

Cost center Plan upload template in csv format:

<!-- image omitted: unnamed -->

Market segment Plan upload template in csv format:

<!-- image omitted: unnamed -->

Procedure

Headquarters plan data upload is uploaded and user can review the actual vs plan data in subsidiary SAP S/4HANA Cloud Public Edition system.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Overhead Accountant.. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori app | Open Import Financial Plan Data . |  |  |
| 3 | Select Template. | Select the Download Templates button. In the Download Templates window select the template file by placing the cursor direction the line Cost Centers and choose Close.A CVS template is downloaded in the lower left corner of the page. Open the template by placing the cursor and selecting.Enter the following Field Values as listed in the step Prepare the file for Cost Center Plan upload. |  |  |
| 4 | Save Template | Save the file in the CSV format. |  |  |
|  |  | Repeat all steps in this section and download template Market Segment and enter the following Field Values as listed in the step Prepare the file for Market Segment Plan upload. |  |  |

#### Prepare the file for Cost Center Plan upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, you prepare your plan data from an external system for upload. Fill in the downloaded template Cost Center Planning with the following data listed below. The exact same data is presented in two ways: Table and CSV format.

- The table format is for clarity of what data is being entered.
- The CSV format is how the exact data must be entered in the CSV file in order for the upload to be successful.

The file must use one of the four acceptable separators listed in section 2.4 and be saved as a CSV file. In our example, we use a semi colon as the separator.

Note The data field KSL (Amount) is represented as a positive (debit) or negative (credit) value dependent on the Accounting view of the G/L account being planned. For example, revenue G/L account plan data would be entered as a negative (credit) in the KSL column. Similarly, expense and asset GL accounts are planned as positive (debit).

Caution The following sample is provided as an example only and this may differ from country to country. Contact your Test administrator for country-specific data.

Procedure

Review the following cost center plan data:

| CATEGORY | RYEAR | POPER | RBUKRS | RCNTR | RACCT | KSL | RKCUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | ar | Pos | Compan | Cost | Acc | cy |  |
| X | X | X | X | X |  |  |  |
| PLN | 2017 | 5 | 1710 | 17101101 | 61003000 | 1000 | USD |
| PLN | 2017 | 5 | 1710 | 17101101 | 65008300 | 2000 | USD |
| PLN | 2017 | 5 | 1710 | 17101101 | 94308000 | 3000 | USD |
| PLN | 2017 | 5 | 1710 | 17101101 | 61007000 | 4000 | USD |

CSV

Enter the cost center plan data in the template:

The CSV file of the same data must appear in this format.

CATEGORY; RLDNR; RYEAR;POPER;RBUKRS;RCNTR;RACCT;KSL;RKCUR

Category; Ledger in General Ledger Accounting; General Ledger Fiscal Year; Posting Period; Company Code; Cost Center; Account Number; Amount in Global Currency;Global Currency

X; X; X; X; X; X;;;

PLN;2017;5;1710;17101101;61003000;1000; USD

PLN;2017;5;1710;17101101;65008300;2000; USD

PLN;2017;5;1710;17101101;94308000;3000; USD

PLN;2017;5;1710;17101101;61007000;4000; USD

Caution The sample is provided as an example only. This is the view from a CSV perspective.

| CATEGORY | RYEAR | POPER | RBUKRS | RCNTR | RACCT | KSL | RKCUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Plan Category | General Ledger Fiscal Year | Posting Period | Company Code | Cost Center | Account Number | Amount in Global Currency | Global Currency |
| X | X | X | X | X |  |  |  |
| PLN | 2017 | 6 | 1710 | 17101101 | 61003000 | 1000 | USD |
| PLN | 2017 | 6 | 1710 | 17101101 | 65008300 | 2000 | USD |
| PLN | 2017 | 6 | 1710 | 17101101 | 94308000 | 3000 | USD |
| PLN | 2017 | 6 | 1710 | 17101101 | 61007000 | 4000 | USD |

#### Prepare the file for Market Segment Plan upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this activity, you prepare your plan data from an external system for upload. Fill in the downloaded template Market Segment Planning with the following data listed below. The exact same data is presented two ways: Table and CSV format. The table format is for clarity of what data is being entered. The CSV format is how the exact data must be entered in the CSV file in order for the upload to be successful. The file must use one of the four acceptable separators listed in section 2.4 and be saved as a CSV file. In our example, we use a semi colon as the separator.

Note The data field KSL (Amount) is represented as a positive (debit) or negative (credit) value dependent on the Accounting view of the G/L account being planned. For example, revenue G/L account plan data would be entered as a negative (credit) in the KSL column. Similarly expense and asset GL accounts are planned as positive (debit).

Caution The following sample is provided as an example only and this may differ from country to country. Contact your Test administrator for country-specific data.

Procedure

Review the following market segment plan data:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | RYEAR | POPER | RBUKRS | MATKL | KDGRP | RACCT | KSL | RKCUR |
|  |  |  |  |  |  |  |  |  |
|  | X | X | X | X | X | X |  |  |
| PLN | 2017 | 5 | 1710 |  | 01 | 41000000 | -90000 | USD |
| PLN | 2017 | 5 | 1710 |  | 02 | 41001000 | -50000 | USD |

CSV

Enter the market segment plan data in the template:

The CSV file of the same data must appear in this format.

CATEGORY; RLDNR; RYEAR; POPER;RBUKRS;MATKL;KDGRP;RACCT;KSL;RKCUR

Category; Ledger in General Ledger Accounting; General Ledger Fiscal Year;Posting Period;Company Code;Material Group;Customer Group;Account Number;Amount in Global Currency;Global Currency

X;X;X;X;X;X;X;;;

PLN;2017;5;1710;;01;41000000;-90000;USD

PLN;2017;5;1710;;02;41000000;-50000;USD

Caution The sample is provided as an example only.This is the view from a CSV perspective.

<!-- image omitted: unnamed -->

#### Importing the P&L File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

Once the plan data file is saved in the template, open the Import P&L Plan Data app and select a source file.

The app performs the following checks:

1.The app checks whether the values in the source file are valid. If required, it returns a list of error messages.

You must correct the values in the source file until they are all valid before you can proceed.

2. If all values are valid, the app checks all versions, fiscal years, posting periods, and company codes that are contained in the source file.

- If no plan data exists in the system for any combination of these four characteristics, you can directly import the plan data.
- If plan data exists in the system for any combination of these four characteristics, the app displays the affected values. It assumes that you want to completely replace the existing plan data by the new plan data import.

Note One source file should therefore always contain full plan data sets for a certain combination of version, company code, and fiscal year (including all posting periods).

<!-- image omitted: unnamed -->

Procedure

Headquarters plan data upload is uploaded and user can review the actual vs plan data in subsidiary SAP Cloud ERP system.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as Overhead Accountant.. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori app | Open Import Financial Plan Data . |  |  |
| 3 | Enter Source File | Use the Browse button to select the CSV extension file you wish to upload following entries and choose Enter.Enter the following Field Value :Source File:Your .CSV file that contains your plan | The Block Asset Processing screen displays. |  |
| 4 | File check | The upload performs a check to ensure that the format is correct.Correct any error message that appears. | The selected file contains data that replaces or deletes the following data message appears. |  |
| 5 | Review | Once successfully uploaded the messageThe selected file has the following plan data scope.appears.Note the two informational messages in the upper left of the screen.On the messageYour plan data import will upload X plan items,select the Show Detail, review the data and then select the back icon.On the messageYour plan data import will overwrite x items,select the Show Detail, review the data and then select the back icon proceed to the next step Import. | The list of the data uploaded appears. |  |
| 6 | Import | Choose Import. | Import successfulmessage appears. |  |

### P&L Actual versus Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you view your current actuals and plan in the system. The P&L Actual versus Plan report shows a consolidated view of planning from both the Cost Center and Market Segment level. Specific reports for Cost Center and Market Segment Actual versus Plan are also available.

Note P&L actual data is only available if there are processed sales orders in the system.

Cost center plan data in csv format:<!-- image omitted: unnamed -->

Market segment plan data in csv format:

<!-- image omitted: unnamed -->

Procedure

Headquarters plan data upload is uploaded and user can review the actual vs plan data in subsidiary SAP Cloud ERP system.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Overhead Accountant.. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open P&L Plan/Actual. |  |  |
| 3 | Enter Information | Make the following entries :Enter the following Field Values :Category : PLNFiscal Year : Current fiscal yearFiscal Period : 005Company Code : 1710G/L Account (Hierarchy) :YCOA ( Sample Grouping of P&L)Note The G/L Account Hierarchy YCOA is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement.Choose Go. |  |  |
| 4 | Review | View Actual versus Plan. |  |  |

### Updating Plan Data

Context

As previously explained, the third row of the file format defines the characteristics of the plan data scope and are file flagged by an X. The more characteristics flagged with an X, the more-specific target plan data is overwritten. Correspondingly, the fewer characteristics flagged the broader the population of the target data is overwritten.

This example illustrates the effects of changes to the characteristics of the plan data scope.

#### Prepare file for additional Cost Center plan data import

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this step, you load additional plan data needed for comparison.

Procedure

Prepare a plan csv data file that is similar to the one created in the step Prepare file for Cost Center plan data upload.

For this data file, the column POPER (Fiscal Period), has the value 6. Save the CSV file.

Note The sample is provided as an example only.

| CATEGORY | RYEAR | POPER | RBUKRS | RCNTR | RACCT | KSL | RKCUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Category |  |  |  |  |  |  |  |
| X | X | X | X | X |  |  |  |
| PLN | 2017 | 6 | 1710 | 17101101 | 61003000 | 1000 | USD |
| PLN | 2017 | 6 | 1710 | 17101101 | 65008300 | 2000 | USD |
| PLN | 2017 | 6 | 1710 | 17101101 | 94308000 | 3000 | USD |
| PLN | 2017 | 6 | 1710 | 17101101 | 61007000 | 4000 | USD |

CSV

Enter the cost center plan data in the template:

The CSV file of the same data must appear in this format.

CATEGORY;RLDNR;RYEAR;POPER;RBUKRS;RCNTR;RACCT;KSL;RKCUR

Category;Ledger in General Ledger Accounting;General Ledger Fiscal Year;Posting Period;Company Code;Cost Center;Account Number;Amount in Global Currency;Global Currency

X;X;X;X;X;X;;;

PLN;2017;6;1710;17101101;61003000;1000;USD

PLN;2017;6;1710;17101101;65008300;2000;USD

PLN;2017;6;1710;17101101;94308000;3000;USD

PLN;2017;6;1710;17101101;61007000;4000;USD

Caution The sample is provided as an example only. This is the view from a CSV perspective.

<!-- image omitted: unnamed -->

#### Importing the P&L File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Overhead Accountant.. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori app | Open Import Financial Plan Data. |  |  |
| 3 | Enter Source File | Use the Browse button to select the CSV extension file you wish to upload the following entries.Enter the following Field Value :Source File:Your .CSV file that contains your planChoose Enter. | The Block Asset Processing screen displays. |  |
| 4 | File check | The upload performs a check to ensure that the format is correct.Correct any error message that appears. | The selected file contains data that replaces or deletes the following data message appears. |  |
| 5 | Import | Choose Import. | Import successfulmessage appears. |  |

#### P&L Actuals versus Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

In this activity, you can view both the previously imported plan data for month 5 and the newly imported plan data for month 6.

Procedure

Headquarters plan data upload is uploaded and user can review the actual vs plan data in subsidiary SAP Cloud ERP system.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Overhead Accountant.. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open P&L Plan/Actual. |  |  |
| 3 | Enter Information | Make the following entries :Enter the following Field Values :Category : PLNFiscal Year : Current fiscal yearFiscal Period : 005 and 006Company Code : 1710G/L Account (Hierarchy) :YCOA ( Sample Grouping of P&L)Note The G/L Account Hierarchy YCOA is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement.Choose Go. |  |  |
| 4 | Review | View Actual versus Plan. | Note The period 5 plan data remains unchanged. |  |
| 5 | Repeat steps 1-4 | Make the following new entries and select Go:Enter the following Field Values:Category: PLNFiscal Year: Current fiscal yearFiscal Period: 006Company Code: 1710G/L Account (Hierarchy):YCOA ( Sample Grouping of P&L)Note The G/L Account Hierarchy YCOA is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement. | <!-- image omitted: unnamed --><!-- image omitted: unnamed --> |  |
| 6 | Review | View Actual versus Plan. | Note the plan data in period 6. |  |

#### Prepare file with changes to the characteristics of the plan data scope

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Purpose

In this step, change the csv file by deselecting the characteristic POPER (Fiscal Period) by removing the X from the third row. Because this file has fewer selection criteria, more data will be overwritten and removed. Specifically, both Period 5 & Period 6 are removed and replaced by this new plan data that only has period 6 data.

Procedure

Prepare a plan csv data file identical to the one created in step Prepare file for additional service plan data import.

Note the change to the table for the value POPER (Posting Period), in the row 3, the value from X was changed to blank. Save the csv file.

Caution The sample is provided as an example only.

| CATEGORY | RYEAR | POPER | RBUKRS | RCNTR | RACCT | KSL | RKCUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
| X | X |  | X | X |  |  |  |
| PLN | 2017 | 6 | 1710 | 17101101 | 61003000 | 1000 | USD |
| PLN | 2017 | 6 | 1710 | 17101101 | 65008300 | 2000 | USD |
| PLN | 2017 | 6 | 1710 | 17101101 | 94308000 | 3000 | USD |
| PLN | 2017 | 6 | 1710 | 17101101 | 61007000 | 4000 | USD |

CSV

Enter the cost center plan data in the template:

The csv file of the same data must appear in this format.

CATEGORY;RLDNR;RYEAR;POPER;RBUKRS;RCNTR;RACCT;KSL;RKCUR

Category;Ledger in General Ledger Accounting;General Ledger Fiscal Year;Posting Period;Company Code;Cost Center;Account Number;Amount in Global Currency;Global Currency

X;X;X;;X;X;;;

PLN;2017;6;1710;17101101;61003000;1000;USD

PLN;2017;6;1710;17101101;65008300;2000;USD

PLN;2017;6;1710;17101101;94308000;3000;USD

PLN;2017;6;1710;17101101;61007000;4000;USD

Caution The sample is provided as an example only.This is the view from a CSV perspective.

Template in csv format:

<!-- image omitted: unnamed -->

#### Importing the P&L File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Procedure

Import the financial plan data from the Headquarters in csv format.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Overhead Accountant.. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Fiori app | Open Import Financial Plan Data . |  |  |
| 3 | Enter Source File | Use the Browse button to select the CSV extension file you wish to upload following entries and choose Enter.Enter the following Field Value:Source File :Your .CSV file that contains your plan |  |  |
| 4 | File check | The upload performs a check to ensure that the format is correct.Correct any error message that appears. | The selected file contains data that replaces or deletes the following data message appears. |  |
| 5 | Import | Choose Import. | Import successfully message appears. |  |

#### P&L Actuals versus Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Test Case ID | <X.XX> | Tester Name |  | Testing Date | Enter a test date. |
| Business Role(s) |  |  |  |  |  |
| Responsibility | <State Service Provider, Customer or Joint Service Provider and Customer> | Duration | Enter a duration. |  |  |

Context

View the results of removing the update characteristic POPER.

As a result of the removing the flag (X) from the characteristic POPER (Fiscal Period) the applicable records updated are no longer limited to a specific fiscal period. Thus, the plan updated all Plan, Company Code, Cost Center, Customer, GL, Year matches. Since, the field provided data no data from period 5, the previous values are removed. Only period 6 data was in this file and therefore only plan data 6 is available for all period that match the selection criteria.

The more specific characteristics chosen through the flag with an X in the 3rd row, the more targeted and narrow plan data population will be updated.

Template in csv format of headquarters data:

<!-- image omitted: unnamed -->

Headquarters plan data upload is uploaded and user can review the actual vs plan data in subsidiary SAP Cloud ERP system.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Logon | Logon to the SAP Fiori launchpad as a Overhead Accountant.. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open P&L Plan/Actual. |  |  |
| 3 | Enter Information | Make the following entries and select Go :Enter the following Field Values :Category : PLNFiscal Year : Current fiscal yearFiscal Period : 005Company Code : 1710G/L Account (Hierarchy) :YCOA ( Sample Grouping of P&L)Note The G/L Account Hierarchy YCOA is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement.Choose Go. |  |  |
| 4 | Review | View Actual versus Plan. | Note the changes in period 5 plan data. |  |
| 5 | Repeat steps 1-4 | Make the following new entries:Enter the following Field Values:Category: PLNFiscal Year: Current fiscal yearFiscal Period: 006Company Code: 1710G/L Account (Hierarchy):YCOA ( Sample Grouping of P&L)Note The G/L Account Hierarchy YCOA is a sample grouping of P&L accounts. You can use any G/L hierarchy as per your requirement.Choose Go . | <!-- image omitted: unnamed --><!-- image omitted: unnamed --> |  |
| 6 | Review | View Actual versus Plan. | Note the plan data in period 6. |  |

## Appendix

### Relevant Scope ID’s / Test Scripts

None

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Guide says plan file is 'semicolon separated' in one place and 'comma separated values (CSV)' in another, while listing four supported separators.

> [!warning] Conflict
> Flagged while digesting this document, not verified: System access table lists both Fiori launchpad and 'On-Premise SAP S/4HANA' for a Cloud Public Edition subsidiary scenario.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-erp-integrated-financial-planning-with-sap-analytics-cloud-22]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/General/Two-Tier_ERP_Assets_User_Guides/Two-Tier_ERP_Assets_User_Guides/Finance/S4CLD2608_2T_Financial Plng_upload_plan.docx` — full document · extracted with `mammoth` · 44,443 chars in the whole document
