---
id: 05-treasury-and-cash-management/shareholding-management-group-ledger-ifrs-5wg-ae-test-script-1127
title: Shareholding Management - Group Ledger IFRS (5WG_AE) Test Script (5WG_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5WG_AE: IFRS 9 parallel valuation postings for shareholdings, dividends, key date valuation, equity pickup (AE)."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/shareholding-management]
aliases: [5WG_S4CLD2608_BPD_EN_AE]
keywords: [Shareholding Management, group ledger ifrs, parallel valuation, cash dividend posting, key date valuation, equity pickup, general ledger posting, test scripts, period-end closing, securities redemption payment]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WG_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1127
topic: 05-treasury-and-cash-management/shareholding-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Shareholding Management - Group Ledger IFRS (5WG_AE) Test Script (5WG_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WG_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Shareholding Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Shareholding Management – Group Ledger IFRS (5WG_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232857908)

[2 Prerequisites 3](#_Toc232857909)

[2.1 System Access 3](#_Toc232857910)

[2.2 Roles 3](#_Toc232857911)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232857912)

[2.4 Business Conditions 5](#_Toc232857913)

[3 Overview Table 6](#_Toc232857914)

[4 Test Procedures 7](#_Toc232857915)

[4.1 Post to General Ledger 7](#_Toc232857916)

[4.2 Recognize Cash Dividend Income According to the Profit Distribution Plan 8](#_Toc232857917)

[4.2.1 Post the Cash Dividend - Associate or Joint Venture 8](#_Toc232857918)

[4.3 Period-end Closing 10](#_Toc232857919)

[4.3.1 Perform Key Date Valuation - Non-affiliated Company 10](#_Toc232857920)

[4.3.2 Equity Pickup - Associate or Joint Venture 12](#_Toc232857921)

[4.4 Payment from Sale 14](#_Toc232857922)

[4.4.1 Post to General Ledger 14](#_Toc232857923)

## Purpose

Overview

By activating parallel valuation for shareholding management – group ledger IFRS, you can use an additional valuation area other than your operational valuation area according to International Financial Reporting Standards (IFRS 9) phase I (Classification and Measurement).

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
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Treasury Specialist - Front Office | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |
| Treasury Specialist - Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE | Treasury Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE |  |
| Treasury Accountant | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |
| Treasury Risk Manager | SAP_BR_TREASURY_RISK_MANAGER | Treasury Analytics | SAP_BR_TREASURY_RISK_MANAGER |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Currency | AED |  |  |
| Business Partner | 33537001 |  |  |
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
| 5WF - Shareholding Management | Must be run before this test script. |
| 1GA - Accounting and Financial Close – Group Ledger IFRS | Must be in scope as prerequisite. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post to General Ledger](#unique_8) [page ] 7 | Treasury Accountant | Process Business Transactions (TPM10) | Flows are posted in valuation area 002 for ledger of IFRS |
| [Post the Cash Dividend - Associate or Joint Venture](#unique_9) [page ] 8 | Treasury Accountant | Create Manual Posting (FWBS) | Cash dividends are entered in the 002 for ledger of IFRS |
| [Perform Key Date Valuation - Non-affiliated Company](#unique_10) [page ] 10 | Treasury Accountant | Run Valuation (TPM1) | The key date valuation is performed. |
| [Equity Pickup - Associate or Joint Venture](#unique_11) [page ] 12 | Treasury Accountant | Create Manual Posting (FWBS) | Calculate the data of equity pick ups manually and enter the data. |
| [Post to General Ledger](#unique_12) [page ] 14 | Treasury Accountant | Process Business Transactions (TPM10) | The transaction is posted. |

## Test Procedures

### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the flows in valuation area 002 for ledger of IFRS. The flows are reflected in the corresponding ledger in Financial Accounting (FI). The flows include pur-chase.

Prerequisite

You have posted the flows in the operative valuation area under your company code by using the following apps mentioned in the Shareholding Management (5WF) test script:

- Fix, Pay and Post Flows (TBB1): You use this app to generate a payment request for outgoing payment with the Pay Only option.
- Process Business Transactions (TPM10): You used this app to generate the posting for outgoing payment (with payment request).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access Another SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: for example, 002Limit by Transaction Number: <select this checkbox>Transaction: <The Security ID you entered in previous step>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If message You have not selected any business transactions is displayed, that means there is no posting needed for your selection criteria, you can skip current step. |  |
| 4 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.The Test Run: Display Posted/Reversed Business Transactions screen is displayed. Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for local GAAP (valuation area 002) on this screen. Please note there is no posting created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 6 | Production Run | On the Update Run: Post/Reverse Business Transactions screen, choose Select All and choose Choose Those to Post, and then choose Execute.The Update Run: Display Posted/Reversed Business Transactions screen is displayed, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, and the accounting document has been created for outgoing payment in local GAAP (valuation area 002). |  |

### Recognize Cash Dividend Income According to the Profit Distribution Plan

If different valuation areas assigned to your company code adopt the same accounting method for cash dividends, you can follow the Enter Condition Items in Security ID and Post the Cash Dividend Income steps in the Shareholding Management (5WF) test script to post cash dividends in the system. Otherwise, you need to post the cash dividends manually by app Create Manual Posting (FWBS).

#### Post the Cash Dividend - Associate or Joint Venture

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post cash dividend income under equity method after you receive the cash dividend on the ex-dividend date.

Prerequisite

Currency exchange spot rates have been maintained if you receive the cash dividend of foreign currency.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Manual Posting (FWBS). | The Manual Posting: Initial Screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE2Security Account: for example, AE_SH | A list of positions is displayed. |  |
| 4 | Enter Details for Cash Dividend | On the Manual Posting screen, enter the following data of cash dividend income:Interest Value Date: for example, <the current date + 1 month>Due Date: for example, <the current date + 1 month>Value Date: for example, <the current date + 1 month>Position Value Date: for example, <the current date + 1 month>Value Date: for example, <the current date + 1 month>FI Posting Date: for example, <the current date + 1 month>Choose Insert Other Flow in the Flows area, insert flows as following data:Line 1:In the Manual Posting: Process Flow screen, select following data and choose Copy:Update Type: for example, SAM8132, Cash Dividend: Reduce equity method investment (VA 002)Payment Amount: for example, 50000 | The dividend flows to be posted or capitalized are maintaind. |  |
| 5 | Post | Confirm the data and choose Post. | The Posting Log: Posted Business Transaction screen is displayed. |  |

### Period-end Closing

Purpose

In this section, period-end closing has different steps if the shareholdings are measured by different accounting methods.

1. If shareholdings are measured as FVTPL/FVOCI in all the valuation area, you need to follow the Update Securities Price and Perform Key Date Valuation steps to complete the period-end closing.
2. If shareholdings are measured by different accounting methods in different valuation areas, you need to post the position changes manually via app Create Manual Posting (FWBS).

#### Perform Key Date Valuation - Non-affiliated Company

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you evaluate the positions of the stock transaction based on the latest price and foreign currency exchange rate where applicable.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Prerequisite

You have entered the spot price for the security class in the Update Securities Price section.

You have performed the following sections of this test script:

- Set Settlement Status
- Payment to Depository Bank
- Post the cash dividend if any during this period
- Post the corporate action if any during this period
- Maintained exchange rate in the valuation date if you have position measured by foreign currency

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Run Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run Valuation screen, enter the following data and choose Run:In the Product Groups area,Securities: <select this checkbox>In the General Selections area,Company Code: for example, 3310Valuation Area: for example, 002Product Type: for example, 16AIn the Securities area,Sec. Class ID Number: for example, SH_AE1Security Account: for example, AE_SHIn the Valuation Parameters area,Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation with ResetNote When the period end is also the year end, the Valuation Category Year End Valuation should be used.Test Run: <select this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation.If dialog box Message shows up, choose Continue. | The screen Valuation Log is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for local GAAP (valuation area 002) by choosing Logs + Messages. Please note there is no posting created because it is test run.Note Sometime there is no simulated posting because your selected security class position in security account may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the Run Valuation screen is displayed.On the Run Valuation screen, change the following data and choose Run:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation. | The Valuation Log screen is displayed, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Then, the accounting document has been created in local GAAP (valuation area 002). |  |

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

You have performed the following sections of this test script:

- Set Settlement Status
- Payment to Depository Bank
- Post the cash dividend if any during this period
- Post the corporate action if any during this period
- Maintained exchange rate in the valuation date if you have position measured by foreign currency

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Manual Posting (FWBS). | The Manual Posting: Initial Screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE2Security Account: for example, AE_SH | A list of positions is displayed. |  |
| 4 | Enter Details for Cash Dividend | On the Manual Posting screen, enter the following data of cash dividend income:Interest Value Date: for example, 3310Due Date: for example, <the current date + 2 month>Value Date: for example, <the current date + 2 month>Position Value Date: for example, <the current date + 2 month>Value Date: for example, <the current date + 2 month>FI Posting Date: for example, <the current date + 2 month>Choose Insert Other Flow in the Flows area, insert flows as following data:Line 1:In the Manual Posting: Process Flow screen, select following data and choose Copy:Update Type: for example, SAM9012, Equity Method: Income increase (VA 002)Payment Amount: for example, 100000 | The dividend flows to be posted or capitalized are maintaind. |  |
| 5 | Post | Confirm the data and choose Post. | The Posting Log: Posted Business Transaction screen is displayed. |  |

### Payment from Sale

Purpose

This section describes how to handle the payment for securities redemption transaction, and how to post it to G/L accounting.

Prerequisites

You have set the status of the transaction to Contract Settlement.

#### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. Two apps are available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this app to generate the posting for incoming payment. Note that it will not create postings for outgoing payment with the Pay Only option.
- Process Business Transactions (TPM10): Use this app to generate the posting for the outgoing payment with the Pay Only option.

|  |
| --- |
| Note You can also a schedule background job for this step. Please see the corresponding step in the Appendix. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Fix, Pay and Post Flows (TBB1). | The Treasury: Post Flows screen is displayed. |  |
| 3 | Test Run | On the Treasury: Post Flows screen, enter the following data and choose Execute:Securities: <select this checkbox>Company Code: for example 3310Transaction: <transaction number with inflow which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | The Posting Log: Posted Business Transactions screen is displayed. You can check the simulated posting information for local GAAP (valuation area 002) on this screen. Please note there is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria. You can skip current test step and continue with app Process Business Transactions (TPM10). |  |
| 4 | Production Run | Choose Back.On the Treasury: Post Flows screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Posting Log: Posted Business Transactions screen is displayed. An accounting document is created for the incoming payment in local GAAP (valuation area 002). |  |
| 5 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions screen displays. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>Company Code: for example, 3310Valuation Area: for example 002Limit by Transaction Number: <select this checkbox>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If the You have not selected any business transactions message is displayed, that means there is no posting needed for your selection criteria. You can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.The Test Run: Display Posted/Reversed Business Transactions screen is displayed, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed. You can check the simulated posting information for local GAAP (valuation area 002) on this screen. Please note there is no posting created because it is a test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 9 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.On the Update Run: Display Posted/Reversed Business Transactions screen, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, and an accounting document is created for the outgoing payment in local GAAP (valuation area 002). |  |

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
> Flagged while digesting this document, not verified: Key date valuation production-run result refers to 'valuation area AE0' while the rest of the script uses valuation area 002 for local GAAP

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-shareholding-management-5wf-ae-sap-s-4hana-cloud-public-ed]]
- related-to :: [[05-treasury-and-cash-management/test-script-shareholding-management-group-ledger-us-gaap-5wh-ae-1128]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WG_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 28,870 chars in the whole document
