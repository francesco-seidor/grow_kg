---
id: 03-financial-accounting-and-close/average-daily-balances-for-banking-649-test-script-1148
title: Average Daily Balances for Banking (649) - Test Script (649_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 649: analysing average daily balances via Trial Balance apps W0166 (deprecated) and F9114."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/average-daily-balances]
aliases: [649_S4CLD2608_BPD_EN_XX]
keywords: [Average Daily Balances for Banking, average daily balances, trial balance, test scripts, key figure calculation, deprecated apps, business roles, banking accounting, business conditions, comments and export]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/649_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1148
topic: 03-financial-accounting-and-close/average-daily-balances
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Average Daily Balances for Banking (649) - Test Script (649_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/649_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Average Daily Balances for Banking** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Average Daily Balances for Banking (649)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Average Daily Balances for Banking (649) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232841365)

[2 Prerequisites 3](#_Toc232841366)

[2.1 System Access 3](#_Toc232841367)

[2.2 Roles 3](#_Toc232841368)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232841369)

[2.4 Business Conditions 4](#_Toc232841370)

[3 Overview Table 5](#_Toc232841371)

[4 Test Procedures 6](#_Toc232841372)

[4.1 Trial Balance - Average Daily Balances (Deprecated) 6](#_Toc232841373)

[4.2 Trial Balance - Average Daily Balances 9](#_Toc232841374)

## Purpose

Overview

With this scope item, you can analyze the average daily balances (ADB) and spot balances in real-time. You can also get a multidimensional view of your key figures.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| General Ledger Accountant - Banks | SAP_BR_GL_ACCOUNTANT_BANKS | General Ledger | SAP_FIN_SPT_GL_ACCOUNTING_BNK_PC |  |

The General Ledger Accountant - Banks (SAP_BR_GL_ACCOUNTANT_BANKS) role template will only be accessible if you have activated the Accounting Enhancements for Banking (5NU) scope item. If 5NU is not active for your account, please use the GL Enhancements: Average Daily Balance (SAP_FS_BC_GLE_ADB_PC) catalog when creating roles.

### Master Data, Organizational Data, and Other Data

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | For example, 1710 for US |  |  |
| Ledger | Any value |  |  |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Execute to create open posting periods. |

## Overview Table

This scope item consists of a process step provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | App/Transaction | Expected Results |
| --- | --- | --- |
| [Trial Balance - Average Daily Balances (Deprecated)](#unique_8) [page ] 6 | Trial Balance: Average Daily Balances (Deprecated) (W0166) | Analyze trial balance key-figures |
| [Trial Balance - Average Daily Balances](#unique_9) [page ] 9 | Trial Balance: Average Daily Balances (F9114) | Analyze trial balance key-figures |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Trial Balance - Average Daily Balances (Deprecated)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can analyze the average daily balance (ADB) of an account at any point during a year. You can view ADBs for intra-month dates based on the posting date of FI documents and also several other key figures such as quarter-to-date average balance and year-to-date average balance.

Prerequisite

Ensure that postings are available in the universal journal for the specified company code and fiscal year.

Example

|  |
| --- |
| Note In all the following examples, the number of decimal places is set to 2. You make this settings under Measures → Number Format → Decimal Place in the Trial Balance: Average Daily Balance (Deprecated) (W0166) app. |

Month-to-Date Average Balance (MTD)

Formula:

Opening balance of the period + SUM (posting amount*(key date -posting date + 1)/(number of days between the key date and the beginning of the period +1))

Note that the sum includes all postings between the beginning of the period and the key date.

Example:

| Activity | Amount |
| --- | --- |
| Opening Balance - Current Year | 150.00 USD |
| Amount Posted – 15th Jan | 200.00 USD |
| Amount Posted – February 5th, 2022 | 150.00 USD |
| Amount Posted – February 10th, 2022 | 250.00 USD |
| Opening Balance - February 2022 | 150.00 USD + 200.00 USD = 350.00 USD |
| Key Date | February 15th, 2022 |
| MTD Average Balance for the Key Date | 350 + SUM ((150 * 11 )/ 15 , ( 250 * 6 ) / 15 )350 + 110 + 100 = 560.00 USD |

Quarter-to-Date Average Balance (QTD)

Formula:

Opening balance of the quarter + SUM (posting amount*(key date -posting date + 1)/(number of days between the key date and the beginning of the quarter +1))

Note that the sum includes all postings between the beginning of the quarter and the key date.

Example:

| Activity | Amount |
| --- | --- |
| Opening Balance – 2nd Quarter | 200.00 USD |
| Amount Posted – April 5th 2022 | 100.00 USD |
| Amount Posted – May 15th 2022 | 400.00 USD |
| Key Date | June 15th, 2022 |
| QTD Average Balance for the Key Date: | 200 + SUM ((100*72)/76, (400*32)/76)200 + 94.74+168.42 = 463.16 USD |

Year-to-Date Average Balance (YTD)

Formula:

Opening balance of the year + SUM (posting amount*(key date -posting date + 1)/number of days between the key date and the beginning of the year +1))

Note that the sum includes all postings between the beginning of the year and the key date.

Example:

| Activity | Amount |
| --- | --- |
| Opening Balance – January 2022 | 200.00 USD |
| Amount Posted – June 5th 2022 | 600.00 USD |
| Amount Posted – July 15th 2022 | 200.00 USD |
| Key Date | August 15th, 2022 |
| YTD Average Balance for the Key Date | 200 + SUM ((600*72)/227 (200*32)/227)200 + 190.31 + 28.19 = 418.50 USD |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | If 5NU is activated, then, log on to the SAP Fiori launchpad as a General Ledger Accountant - Banks.If 5NU is not activated, then proceed as follows:Create a business role with the GL Enhancements - Average Daily Balance (SAP_FS_BC_GLE_ADB_PC business catalog (see How to Create a New Business Role topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Create a business user (see How to Maintain Business Users topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Log on to the SAP Fiori launchpad with the user you created in the previous step |  |  |
| 2 | Access App | Open Trial Balance: Average Daily Balances (Deprecated) (W0166). |  |  |
| 3 | Start Selection | On the entry screen, make the following entries and choose Go:Ledger:for example,0LCompany Code: enter a company code, for example, 1710Key Date: enter the key date | The app, by default, displays the following ADB key figures (in company code currency) for all GL accounts linked to the specified company code, in the Data Analysis tab:MTD Average Daily BalanceQTD Average Daily BalanceYTD Average Daily BalanceIn addition, you can also view the following key figures:Month-to-Date Average ActivityQuarter-to-Date ActivityNoteYou can add additional fields using the Adapt Filters button to narrow down your search results. For example, if you want to analyze the ADB balances for specific G/L accounts, then you can add GL Account as an additional search field from the list of fields available under Adapt Filters.From the Navigation Panel (on the top), you can do the following:Add additional measures that you want to analyze. To do this, choose Columns -> Measures. The newly added measures will be displayed as columns in the result table.Group the ADB key figures based on fields, for example like profit center, cost center, and G/L account. To do so, choose the fields from the list of Available Fields and add them to the row axis |  |

### Trial Balance - Average Daily Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can analyze a wide range of key financial figures—primarily Average Daily Balances (ADB)—at any point throughout the year. The app enables you to view metrics such as month-to-date (MTD), quarter-to-date (QTD), and year-to-date (YTD) average daily balances, including intra-month ADBs based on the posting dates of Financial Accounting (FI) documents. In addition to ADBs, the app offers a comprehensive suite of account performance indicators, including daily and monthly transaction activity, cumulative balances, and average balances across multiple currency types such as company code currency, global currency, and freely defined currencies. With the commenting capability, you can collaborate better. You can add, edit, reply, view, delete, copy, paste, filter, and search comments directly within the app.

Prerequisite

Ensure that postings are available in the universal journal for the specified company code and fiscal year.

Example

|  |
| --- |
| Note In all the following examples, the number of decimal places is set to 2. |

MTD Average Daily Balance

Formula:

Opening balance of the period + SUM (posting amount*(key date -posting date + 1)/(number of days between the key date and the beginning of the period +1))

Note that the sum includes all postings between the beginning of the period and the key date.

Example:

| Activity | Amount |
| --- | --- |
| Opening Balance - Current Year | 150.00 USD |
| Amount Posted – 15th Jan | 200.00 USD |
| Amount Posted – February 5th, 2022 | 150.00 USD |
| Amount Posted – February 10th, 2022 | 250.00 USD |
| Opening Balance - February 2022 | 150.00 USD + 200.00 USD = 350.00 USD |
| Key Date | February 15th, 2022 |
| MTD ADB for the Key Date | 350 + SUM ((150 * 11 )/ 15 , ( 250 * 6 ) / 15 )350 + 110 + 100 = 560.00 USD |

QTD Average Daily Balance

Formula:

Opening balance of the quarter + SUM (posting amount*(key date -posting date + 1)/(number of days between the key date and the beginning of the quarter +1))

Note that the sum includes all postings between the beginning of the quarter and the key date.

Example:

| Activity | Amount |
| --- | --- |
| Opening Balance – 2nd Quarter | 200.00 USD |
| Amount Posted – April 5th 2022 | 100.00 USD |
| Amount Posted – May 15th 2022 | 400.00 USD |
| Key Date | June 15th, 2022 |
| QTD ADB for the Key Date: | 200 + SUM ((100*72)/76, (400*32)/76)200 + 94.74+168.42 = 463.16 USD |

YTD Average Daily Balance

Formula:

Opening balance of the year + SUM (posting amount*(key date -posting date + 1)/number of days between the key date and the beginning of the year +1))

Note that the sum includes all postings between the beginning of the year and the key date.

Example:

| Activity | Amount |
| --- | --- |
| Opening Balance – January 2022 | 200.00 USD |
| Amount Posted – June 5th 2022 | 600.00 USD |
| Amount Posted – July 15th 2022 | 200.00 USD |
| Key Date | August 15th, 2022 |
| YTD Average Balance for the Key Date | 200 + SUM ((600*72)/227 (200*32)/227)200 + 190.31 + 28.19 = 418.50 USD |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | If 5NU is activated, then, log on to the SAP Fiori launchpad as a General Ledger Accountant - Banks.If 5NU is not activated, then proceed as follows:Create a business role with the GL Enhancements - Average Daily Balance (SAP_FS_BC_GLE_ADB_PC) business catalog with dependencies. For more details, see How to Create a New Business Role topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Create a business user (see How to Maintain Business Users topic in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html))Log on to the SAP Fiori launchpad with the user you created in the previous step |  |  |
| 2 | Access App | Open Trial Balance: Average Daily Balances (F9114). |  |  |
| 3 | Start Selection | On the entry screen, make the following entries and choose Go:Ledger:for example,0LCompany Code: enter a company code, for example, 1710Key Date: enter the key dateCreated Until (Date): enter the journal entry creation cutoff dateCreated Until (Time): enter the journal entry creation cutoff time | The app, by default, displays the following ADB key figures for all GL accounts linked to the specified company code:MTD Average Daily Balance (Company Code Currency)QTD Average Daily Balance (Company code currency)YTD Average Daily Balance (Company Code Currency) |  |
| 4 | View Additional Key Figures | On the side panel, choose Layout and specify the additional key figures that you want to analyze. To do so, select these fields from the list of Measures (in the Available Objects section). On selecting, these key figures get added to the Columns list. | The app displays the additional measures that you selected in the output list table.The available list of measures that you can analyze using this app are listed below:MTD Average Daily Balance (Balance Transaction Currency)MTD Average Daily Balance (Global Currency)MTD Average Daily Balance (Functional Currency)MTD Average Daily Balance (Freely Defined Currency 1)MTD Average Daily Balance (Freely Defined Currency 2)MTD Average Activity (Company Code Currency)MTD Average Activity (Balance Transaction Currency)MTD Average Activity (Global Currency)MTD Average Activity (Functional Currency)MTD Average Activity (Freely Defined Currency 1)MTD Average Activity (Freely Defined Currency 2)QTD Average Daily Balance (Balance Transaction Currency)QTD Average Daily Balance (Global Currency)QTD Average Daily Balance (Functional Currency)QTD Average Daily Balance (Freely Defined Currency 1)QTD Average Daily Balance (Freely Defined Currency 2)QTD Activity (Company Code Currency)QTD Activity (Balance Transaction Currency)QTD Activity (Global Currency)QTD Activity (Functional Currency)QTD Activity (Freely Defined Currency 1)QTD Activity (Freely Defined Currency 2)YTD Average Daily Balance (Balance Transaction Currency)YTD Average Daily Balance (Global Currency)YTD Average Daily Balance (Functional Currency)YTD Average Daily Balance (Freely Defined Currency 1)YTD Average Daily Balance (Freely Defined Currency 2)YTD Balance (Company Code Currency)YTD Balance (Balance Transaction Currency)YTD Balance (Global Currency)YTD Balance (Functional Currency)YTD Balance (Freely Defined Currency 1)YTD Balance (Freely Defined Currency 2)Prior Day Balance (Company Code Currency)Prior Day Balance (Balance Transaction Currency)Prior Day Balance (Global Currency)Prior Day Balance (Functional Currency)Prior Day Balance (Freely Defined Currency 1)Prior Day Balance (Freely Defined Currency 2)Prior Month Balance (Company Code Currency)Prior Month Balance (Balance Transaction Currency)Prior Month Balance (Global Currency)Prior Month Balance (Functional Currency)Prior Month Balance (Freely Defined Currency 1)Prior Month Balance (Freely Defined Currency 2)Current Day Activity (Company Code Currency)Current Day Activity (Balance Transaction Currency)Current Day Activity (Global Currency)Current Day Activity (Functional Currency)Current Day Activity (Freely Defined Currency 1)Current Day Activity (Freely Defined Currency 2)Current Month Activity (Company Code Currency)Current Month Activity (Balance Transaction Currency)Current Month Activity (Global Currency)Current Month Activity (Functional Currency)Current Month Activity (Freely Defined Currency 1)Current Month Activity (Freely Defined Currency 2)Amount (Company Code Currency)Amount (Balance Transaction Currency)Amount (Global Currency)Amount (Functional Currency)Amount (Freely Defined Currency 1)Amount (Freely Defined Currency 2 |  |
| 5 | Apply Dimensions | On the side panel, choose Layout and specify the fields based on which you want to group the measures that you added. To do so, select these fields from the list of Dimensions (in the Available Objects section) and choose Rows. | The app groups the measures that you selected based on the dimensions that you specify.The available list of dimensions based on which you can group the measures are:If 5NU is Not ActiveChart of AccountsCompany CodeControlling AreaCost CenterFiscal YearFiscal Year VariantFiscal Year of LedgerGL AccountLedgerPartner Functional AreaPartner Profit CenterPartner SegmentPosting DateProfit CenterSegmentTrading PartnerIf 5NU is ActiveBranch (FS)Chart of AccountsCompany CodeControlling AreaCost CenterCustomer GroupCustomer/Supplier IndustryCustomer/Supplier CountryData SourceFiscal YearFiscal Year VariantFiscal Year of LedgerGL AccountLedgerPartner Functional AreaPartner Profit CenterPartner SegmentPosting DateProduct GroupProfit CenterSegmentTrading Partner |  |
| 6 | Filtering Output Values | On the side panel, choose Filters and specify filter values for dimensions to further zoom in on the data displayed in the output table. | The app filters the key figures based on the filter dimensions you specify. |  |
| 7 | Display Options | On the side panel, choose Chart Settings and switch between Table, Table and Chart, and Chart views. Also, select a chart type and apply the settings. | The app displays the output in the selected view and renders the chart based on the applied settings. |  |
| 8 | Add Comments | On the side panel, choose Comments. | The app displays the Comments section, where you can do the following:Add commentsEdit commentsReply to commentsView commentsDelete commentsNote You can add, view, copy, and paste comments directly from the output list table by right‑clicking on a cell. |  |
| 9 | Export Data | On the side panel, choose Export and use the options to export data to a spreadsheet and to PDF. | The app generates and downloads the exported file in the selected format. |  |

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
- see-also :: [[03-financial-accounting-and-close/test-script-accounting-and-financial-close-group-ledger-ifrs-1ga-ae-sa]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/649_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 23,044 chars in the whole document
