---
id: 05-treasury-and-cash-management/test-script-shareholding-management-group-ledger-us-gaap-5wh-ae-1128
title: "Test Script: Shareholding Management – Group Ledger US GAAP (5WH_AE) (5WH_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5WH: parallel US GAAP valuation area postings for shareholdings (dividends, equity pickup, reclassification)."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/shareholding-management]
aliases: [5WH_S4CLD2608_BPD_EN_AE]
keywords: [Shareholding Management, parallel valuation area, us gaap ledger, cash dividend posting, equity pickup, equity item reclassification, test scripts, business roles, master data scripts, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WH_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1128
topic: 05-treasury-and-cash-management/shareholding-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Shareholding Management – Group Ledger US GAAP (5WH_AE) (5WH_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WH_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Shareholding Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Shareholding Management – Group Ledger US GAAP (5WH_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232857874)

[2 Prerequisites 3](#_Toc232857875)

[2.1 System Access 3](#_Toc232857876)

[2.2 Roles 3](#_Toc232857877)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232857878)

[2.4 Business Conditions 4](#_Toc232857879)

[3 Overview Table 5](#_Toc232857880)

[4 Test Procedures 6](#_Toc232857881)

[4.1 Post to General Ledger (Parallel Valuation Area) 6](#_Toc232857882)

[4.2 Recognize Cash Dividend Income According to the Profit Distribution Plan 7](#_Toc232857883)

[4.2.1 Post the Cash Dividend - Associate or Joint Venture 7](#_Toc232857884)

[4.3 Period-end Closing 9](#_Toc232857885)

[4.3.1 Equity Pickup - Associate or Joint Venture 9](#_Toc232857886)

[4.4 Payment from Sale 11](#_Toc232857887)

[4.4.1 Reclassify the Recognized Equity Item 11](#_Toc232857888)

## Purpose

Overview

By activating parallel valuation for Shareholding Management – Group Ledger US GAAP, you can use an additional valuation area besides your operational valuation area according to US Generally Accepted Accounting Principles (US GAAP).

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
| Valuation Area | 003 |  |  |

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
| 5WF - Shareholding Management | Must be run before this test script. |
| 2VA - Accounting and Financial Close – Group Ledger US GAAP | Must be in scope as prerequisite. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post to General Ledger (Parallel Valuation Area)](#unique_8) [page ] 6 | Treasury Accountant | Process Business Transactions (TPM10) | Flows are posted in valuation area 002 for ledger of IFRS |
| [Post the Cash Dividend - Associate or Joint Venture](#unique_9) [page ] 7 | Treasury Accountant | Create Manual Posting (FWBS) | Cash dividends are entered in the 002 for ledger of IFRS |
| [Equity Pickup - Associate or Joint Venture](#unique_10) [page ] 9 | Treasury Accountant | Create Manual Posting (FWBS) | Calculate the data of equity pick ups manually and enter the data. |
| [Reclassify the Recognized Equity Item](#unique_11) [page ] 11 | Treasury Accountant | Create Manual Posting (FWBS) | The equity items are reclassfied. |

## Test Procedures

### Post to General Ledger (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the flows in valuation area 003 for ledger of US GAAP. The flows are reflected in the corresponding ledger in Financial Accounting (FI).

Prerequisite

The flows of deals are posted in operative valuation AE0 for local GAAP by using the following apps:

- Fix, Pay and Post Flows (TBB1): You used this app to generate a payment request for outgoing payment with the Pay Only option.
- Process Business Transactions (TPM10): You used this app to generate the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Run:Securities: <select this checkbox>Company Code: for example, 3310Valuation Area: for example 003Limit by Transaction Number: <select this checkbox>Transaction: <transaction number with outflow, and its payment request has been generated in test script 5WF>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If the You have not selected any business transactions message is displayed, that means there is no posting needed for your selection criteria. You can skip current step. |  |
| 4 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Run.The Test Run: Display Posted/Reversed Business Transactions screen is displayed, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed. You can check the simulated posting information for local GAAP (valuation area 002) on this screen. Please note there is no posting created because it is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Run:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 6 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Run.On the Update Run: Display Posted/Reversed Business Transactions screen, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, and an accounting document is created for the outgoing payment in local GAAP (valuation area 003). |  |

### Recognize Cash Dividend Income According to the Profit Distribution Plan

For the shareholding of shareholding types Non-Affiliated and Subsidiary, you can refer to the step Enter Condition Items in Security ID and Post the Cash Dividend Income in the test script Shareholding Management (5WF) to post the cash dividend in all valuation areas together.

If the shareholding type is Associate or Joint venture, you should execute the following step to post the cash dividend in valuation area 003 for ledger of US GAAP individually.

#### Post the Cash Dividend - Associate or Joint Venture

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, for the shareholding type is Associate or Joint venture, you post cash dividend income for ledger of US GAAP, after you receive the cash dividend on the ex-dividend date.

Prerequisite

Currency exchange spot rates have been maintained if you receive the cash dividend of foreign currency.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Manual Posting (FWBS). | The Manual Posting: Initial Screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE2Security Account: for example, AE_SH | A list of positions is displayed. |  |
| 4 | Enter Details for Cash Dividend | On the Manual Posting screen, enter the following data of cash dividend income:Interest Value Date: for example, <the current date + 1 month>Due Date: for example, <the current date + 1 month>Value Date: for example, <the current date + 1 month>Position Value Date: for example, <the current date + 1 month>Value Date: for example, <the current date + 1 month>FI Posting Date: for example, <the current date + 1 month>Choose Insert Other Flow in the Flows area, insert flows as following data:Line 1:in the Manual Posting: Process Flow screen, select following data and choose Copy:Update Type: for example, SAM8133 Cash Dividend: Reduce equity method in-vestment (VA 003)Payment Amount: for example, 50000 | The dividend flows to be posted or capitalized are maintaind. |  |
| 5 | Post | Confirm the data and choose Post. | The Posting Log: Posted Business Transaction screen is displayed. |  |

### Period-end Closing

Purpose

For the shareholding of non-affiliated type, you can refer to the Update Securities Price - Non-affiliated Company and Perform Key Date Valuation - Non-affiliated Company steps in the test script Shareholding Management (5WF) to process period-end valuation in all valuation areas together.

For the shareholding type of associate or joint venture, you need to post position changes manually.

For the shareholding type of subsidiary, no procedure is needed in the TRM component.

#### Equity Pickup - Associate or Joint Venture

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you do the equity pickup based on the latest financial information from the associate or joint venture companies.

You need to calculate the data of equity pickup manually and enter the data by Create Manual Posting (FWBS).

Prerequisite

For the relevant shareholding, you have performed the following sections of the test script Shareholding Management (5WF):

- Sell Shareholdings
- Set Settlement Status
- Payment from Sale: for the step Post to General Ledger, the valuation area 003 should be assigned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Manual Posting (FWBS). | The Manual Posting: Initial Screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE2Security Account: for example, AE_SH | A list of positions is displayed. |  |
| 4 | Enter Details for Cash Dividend | On the Manual Posting screen, enter the following data of cash dividend income:Interest Value Date: for example, <the current date + 3 month>Due Date: for example, <the current date + 3 month>Value Date: for example, <the current date + 3 month>Position Value Date: for example, <the current date + 3 month>Value Date: for example, <the current date + 3 month>FI Posting Date: for example, <the current date + 3 month>Choose Insert Other Flow in the Flows area, insert flows as following data:Line 1:In the Manual Posting: Process Flow screen, select following data and choose Copy:Update Type: for example, SAM9043, Equity Method: OCI decrease (VA 003)Payment Amount: for example, 5000Line 2:In the Manual Posting: Process Flow screen, select following data and choose Copy:Update Type: for example, SAM9053, Equity Method: APIC increase (VA 003)Payment Amount: for example, 8000 | The valuation flows to be posted. |  |
| 5 | Post | Confirm the data and choose Post. | The Posting Log: Posted Business Transaction screen is displayed. |  |

### Payment from Sale

Purpose

This section describes how to handle the payment for securities redemption transaction, and how to post it to G/L accounting.

Prerequisites

You have set the status of the transaction to Contract Settlement.

#### Reclassify the Recognized Equity Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For the sold portion of associate or joint venture type, if the Equity Pickup is processed during the period-end closing, you need to calculate the recognized equity items of the sold share, then reclassify to corresponding financial accounts manually for the ledger of US GAAP by APP: Create Manual Posting (FWBS).

Prerequisites

For the relevant shareholding, you have performed the following sections of the test script Shareholding Management (5WF):

- Sell Shareholdings
- Set Settlement Status
- Payment from Sale: for the step Post to General Ledger, the valuation area 003 should be assigned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Manual Posting (FWBS). | The Manual Posting: Initial Screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE2Security Account: for example, AE_SH | A list of positions is displayed. |  |
| 4 | Enter Details for Cash Dividend | On the Manual Posting screen, enter the following data of cash dividend income:Interest Value Date: for example, <the current date + 3 month>Due Date: for example, <the current date + 3 month>Value Date: for example, <the current date + 3 month>Position Value Date: for example, <the current date + 3 month>Value Date: for example, <the current date + 3 month>FI Posting Date: for example, <the current date + 3 month>Choose Insert Other Flow in the Flows area, insert flows as following data:Line 1:In the Manual Posting: Process Flow screen, select following data and choose Copy:Update Type: for example, SAM9143, Equity Method: Clear OCI (negative) (VA 003)Payment Amount: for example, 5000Line 2:In the Manual Posting: Process Flow screen, select following data and choose Copy:Update Type: for example, SAM9153, Equity Method: Clear APIC (positive) (VA 003)Payment Amount: for example, 8000 | The valuation flows to be posted. |  |
| 5 | Post | Confirm the data and choose Post. | The Posting Log: Posted Business Transaction screen is displayed. |  |

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
> Flagged while digesting this document, not verified: Valuation area references are inconsistent within the script: the Overview Table says flows post in valuation area 002 for ledger of IFRS and step text mentions local GAAP as 002 or 003, while Purpose states 003 for US GAAP and the prerequisite names operative valuation AE0 for local GAAP.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/shareholding-management-group-ledger-ifrs-5wg-ae-test-script-1127]]
- related-to :: [[05-treasury-and-cash-management/test-script-shareholding-management-5wf-ae-sap-s-4hana-cloud-public-ed]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WH_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 21,928 chars in the whole document
