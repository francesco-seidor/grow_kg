---
id: 05-treasury-and-cash-management/stock-management-group-ledger-ifrs-5oe-ae-test-script-1112
title: Stock Management – Group Ledger IFRS (5OE_AE) Test Script (5OE_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5OE_AE: parallel valuation area 002 for IFRS in stock (securities) management, dated 19-06-26."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/stock-securities-management]
aliases: [5OE_S4CLD2608_BPD_EN_AE]
keywords: [Stock (Equity Securities) Management, parallel valuation, key date valuation, group ledger ifrs, stock management, subscription rights, period-end closing, business roles, business conditions, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OE_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1112
topic: 05-treasury-and-cash-management/stock-securities-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Stock Management – Group Ledger IFRS (5OE_AE) Test Script (5OE_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OE_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Stock (Equity Securities) Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Stock Management – Group Ledger IFRS (5OE_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232857470)

[2 Prerequisites 3](#_Toc232857471)

[2.1 System Access 3](#_Toc232857472)

[2.2 Roles 3](#_Toc232857473)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232857474)

[2.4 Business Conditions 4](#_Toc232857475)

[3 Overview Table 5](#_Toc232857476)

[4 Test Procedure 6](#_Toc232857477)

[4.1 Post to General Ledger (Parallel Valuation) 6](#_Toc232857478)

[4.2 Perform Key Date Valuation (Parallel Valuation) 7](#_Toc232857479)

[5 Appendix 9](#_Toc232857480)

[5.1 Subscription Rights 9](#_Toc232857481)

[5.1.1 Post to General Ledger 9](#_Toc232857482)

[5.1.2 Period-end Closing 10](#_Toc232857483)

[5.1.2.1 Perform Key Date Valuation 11](#_Toc232857484)

## Purpose

Overview

By activating parallel valuation for stock management – group ledger IFRS, you can use an additional valuation area other than your operational valuation area according to International Financial Reporting Standards (IFRS 9) phase I (Classification and Measurement).

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
| Treasury Accountant | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Valuation Area | 002 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

List conditions in the correct sequence. Specify the related scope item. The information is required to create the Test Cycle document which explains the dependencies between scope items and lists the requirements for testing a scope item.

| Scope Item ID | Business Condition |
| --- | --- |
| 5OD - Stock Management | Must be run before this test script. |
| 1GA - Accounting and Financial Close – Group Ledger IFRS | Must be in scope as prerequisite. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post to General Ledger (Parallel Valuation)](#unique_8) [page ] 6 | Treasury Accountant | Process Business Transactions (TPM10) | Flows are posted in valuation area 002 for ledger of IFRS |
| [Perform Key Date Valuation (Parallel Valuation)](#unique_9) [page ] 7 | Treasury Accountant | Run Valuation (TPM1) | Valuation is executed in valuation area 002 for ledger of IFRS |

## Test Procedure

This section describes test procedures for each process step that belongs to this scope item.

### Post to General Ledger (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the flows in parallel valuation area 002 for IFRS. The flows are reflected in the corresponding ledger in Financial Accounting (FI). The flows include purchase.

Prerequisite

The flows of deals are posted in operative valuation AE0 for local GAAP. For more information, ensure that you’ve completed the following apps in the Stock Management(5OD) test script:

- Fix, Pay and Post Flows (TBB1): You used this app to generate a payment request for outgoing payment with the Pay Only option.
- Process Business Transactions (TPM10): You used this app to generate the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Run:Securities: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, 002Limit by Transaction Number: <select this checkbox>Transaction: <transaction number with outflow, and its payment request has been generated in test script 5OD>Test Run: <select this checkbox> | Screen Test Run: Post/Reverse Business Transactions displays.If the You have not selected any business transactions message displays, it means that there is no posting needed for your selection criteria, you can skip the current step. |  |
| 4 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Run.Screen Test Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information on this screen, please note there is no posting created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Run:Test Run: <deselect this checkbox> | Screen Update Run: Post/Reverse Business Transactions is displayed.The following message should be displayed:Test run was successful. |  |
| 6 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Run.Screen Update Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | On the Update Run: Display Posted/Reversed Business Transactions screen, the following message should be displayed:Update was successfulThe Posting Log: Posted Business Transactions screen is displayed. The accounting document has been created for outgoing payment in IFRS (valuation area 002). |  |

### Perform Key Date Valuation (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you run the key date valuation to update the position of the stock transaction in valuation area 002.

Prerequisite

You have completed the key date valuation to update the postion of the stock transaction in local valuation area AE0 according to the relevant step in theStock Management (5OD) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Execute Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Execute Valuation screen, enter the following data and choose Run:Securities: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, 002Product Type: for example, 01ASecurity ID: for example, ST_AE1Security Account: for example, AE_STKey Date for Valuation: for example, <the last date of the current month>Valuation Category: for example, Mid-year Valuation with ResetWhen the Period End is also the Year End, the Valuation Category Year End Valuation should be used.Test Run: <select this checkbox> | The Display Positions to be Valued screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Positions to be Valued screen, choose Execute Valuation.If the Message dislog box shows up, choose Continue. | The Valuation Log screen is displayed.You can check the simulated posting information by choosing Logs + Messages. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back to return to the Execute Valuation screen.Change the following data and choose Run:Test Run: <deselect this checkbox> | The Display Positions to be Valued screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Positions to be Valued screen, choose Execute Valuation. | The Valuation Log screen is displayed. You can check the posting information by choosing Logs + Messages. |  |

## Appendix

### Subscription Rights

#### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the flows in parallel valuation area 002 for IFRS. The flows are posted to the corresponding ledger in Financial Accounting (FI).

Prerequisite

You have posted the old stock purchase transaction to the operative valuation AE0 for local GAAP according to relevant steps in the Subscription Rights part of the Stock Management(5OD) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, 002Limit by Transaction Number: <select this checkbox>Transaction: <the old stock purchase transaction number with outflow, and its payment request has been generated in test script 5OD>Test Run: <select this checkbox> | Screen Test Run: Post/Reverse Business Transactions displays.If the You have not selected any business transactions message displays, it means that there is no posting needed for your selection criteria, you can skip the current step. |  |
| 4 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.The Test Run: Display Posted/Reversed Business Transactions screen is displayed, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed. You can check the simulated postings on this screen. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <deselect this checkbox> |  |  |
| 6 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Update Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed. The accounting document has been created for outgoing payment in IFRS (valuation area 002). |  |

#### Period-end Closing

Purpose

In this section, you will update the period-end price of the subscription rights in your position and re-evaluate their fair value with the new price. You need to perform the following steps:

- Update Securities Price
- [Perform Key Date Valuation](#unique_13) [page ] 11

##### Perform Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you run valuation update the position of the subscription rights at the period end, which is posted to the valuation area 002 for IFRS.

Prerequisite

You have run the key date valuation in the local valuation area for the posting to the local GAAP according to the relevant step in the Stock Management (5OD) test script:

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Execute Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Execute Valuation screen, enter the following data and choose Execute:Securities: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, 002Product Type: for example, 03ASecurity ID: for example, SR_AE1Security Account: for example, AE_STKey Date for Valuation: for example, <the last date of the current month>Valuation Category: for example, Mid-year Valuation with ResetWhen the Period End is also the Year End, the Valuation Category Year End Valuation should be used.Test Run: <select this checkbox> | The Display Positions to be Valued screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Positions to be Valued screen, choose Execute Valuation. | The simulated postings are displayed.You can check the simulated posting information by choosing Logs + Messages. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back to return to the Execute Valuation screen.Change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Positions to be Valued screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Positions to be Valued screen, choose Execute Valuation. | The Valuation Log screen is displayed. You can check the posting information by choosing Logs + Messages. |  |

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
- related-to :: [[05-treasury-and-cash-management/stock-management-group-ledger-us-gaap-5of-ae-test-script-1113]]
- related-to :: [[05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-stock-management-5od-ae-1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5OE_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 20,991 chars in the whole document
