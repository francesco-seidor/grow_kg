---
id: 05-treasury-and-cash-management/securities-option-management-group-ledger-us-gaap-6nf-ae-test-script-1
title: Securities Option Management – Group Ledger US GAAP (6NF_AE) Test Script (6NF_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script 6NF (AE) for posting flows, key date valuation and realized P&L in parallel valuation area 003 for US GAAP."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/securities-options]
aliases: [6NF_S4CLD2608_BPD_EN_AE]
keywords: [Securities Option Management, parallel valuation, group ledger us gaap, post flows to general ledger, key date valuation, realized profit and loss, business conditions, demo data, business roles, 6NF]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NF_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1183
topic: 05-treasury-and-cash-management/securities-options
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Securities Option Management – Group Ledger US GAAP (6NF_AE) Test Script (6NF_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NF_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Securities Option Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Securities Option Management – Group Ledger US GAAP (6NF_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Securities Option Management – Group Ledger US GAAP (6NF_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232859047)

[2 Prerequisites 3](#_Toc232859048)

[2.1 System Access 3](#_Toc232859049)

[2.2 Roles 3](#_Toc232859050)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232859051)

[2.4 Business Conditions 4](#_Toc232859052)

[3 Overview Table 5](#_Toc232859053)

[4 Test Procedures 6](#_Toc232859054)

[4.1 Post Flows to General Ledger (Parallel Valuation Area) 6](#_Toc232859055)

[4.2 Period-end Closing (Parallel Valuation) 7](#_Toc232859056)

[4.2.1 Perform Key Date Valuation (Parallel Valuation) 8](#_Toc232859057)

[4.3 Post Realized Profit and Loss (Parallel Valuation) 9](#_Toc232859058)

## Purpose

Overview

By activating parallel valuation for Securities Option Management – Group Ledger US GAAP, you can use an additional valuation area besides your operational valuation area according to US Generally Accepted Accounting Principles (US GAAP).

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

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

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

| Scope Item | Business Condition |
| --- | --- |
| 6ND - Securities Option Management | Must be run before this test script. |
| 2VA - Accounting and Financial Close – Group Ledger US GAAP | Must be in scope as prerequisite. |

## Overview Table

The Securities Option Management - Group Ledger US GAAP scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Post Flows to General Ledger (Parallel Valuation Area)](#unique_8) [page ] 6 | Treasury Accountant | Process Business Transactions (TPM10) | Flows are posted in valuation area 003 for ledger of US GAAP. |
| [Perform Key Date Valuation (Parallel Valuation)](#unique_9) [page ] 8 | Treasury Accountant | Run Valuation (TPM1) | Valuation is executed in valuation area 003 for ledger of US GAAP. |
| [Post Realized Profit and Loss (Parallel Valuation)](#unique_10) [page ] 9 | Treasury Accountant | Post Derived Business Transactions (TPM18) | Realized profit and loss are posted in valuation area 003 for ledger of US GAAP. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Post Flows to General Ledger (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the flows in parallel valuation area 003 for US GAAP. The flows are reflected in the corresponding ledger in Financial Accounting (FI). The flows include the premium or any fees of the securities options.

Prerequisites

The flows of deals are posted in operative valuation AE0 for local GAAP. For more information, ensure that you executed the following apps in the Securities Option Management (6ND) test script:

- Fix, Pay and Post Flows (TBB1): You used this app to generate a payment request for outgoing payment with the Pay Only option. You generated the posting for incoming payment (without payment request) in valuation area AE0 with the Post Operational Only option.
- Process Business Transactions (TPM10): You used this app to generate the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access Another SAP Fiori App | Open Process Business Transactions (TPM10). | The Fix, Post or Reverse Transactions view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Run:OTC Transactions: <select>Company code: for example, 3310Valuation Area: for example, 003Limit by Transaction Number: <deselect>Limiting by Subledger Positions: <select>Transaction: <transaction number(s) was created in test script 6ND, and flows have been posted in valuation area AE0>Test Run: <select> | The Test Run: Post/Reverse Business Transactions view displays.If the system displays the message You have not selected any business transactions, no posting is needed for your selection criteria. You can skip the current step. |  |
| 4 | Review Test Run Result | Choose Select All.Select Choose Those to Post and choose Run.On the Test Run: Display Posted/Reversed Business Transactions view, choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Check the simulated posting information for US GAAP (valuation area 003) on this view. No posting is created because it is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back.Change the following data and choose Run.Test Run: <deselect> | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 6 | Production Run | Choose Select All.Select Choose Those to Post and choose Run.On the Update Run: Display Posted/Reversed Business Transactions view, choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. An accounting document is created for US GAAP (valuation area 003). |  |

### Period-end Closing (Parallel Valuation)

Purpose

This section describes activities for period-end closing (usually executed at month end) using the 003 valuation area for US GAAP, including:

- Perform key date valuation

#### Perform Key Date Valuation (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to value the positions of financial instruments based on historical cost or fair value for a given key date in valuation area 003 for US GAAP, and transfer results to corresponding ledger for US GAAP in Financial Accounting (FI).

Prerequisites

Fair values (NPV) have been calculated or maintained for financial transactions which are evaluated at fair value (NPV) according to US GAAP, see step Calculate or Maintain Fair Value of Transaction in the Securities Option Management (6ND) test script .

Key date valuation has been executed in valuation area AE0 for local GAAP in test script Securities Option Management (6ND).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Execute Valuation view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select>Company code: for example, 3310Valuation Area: for example, 003Transaction: <transaction number(s) created in test script 6ND>Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, <Mid-year Valuation with Reset>Note When the Period end is also the Year end, use the Year-End Valuation Valuation Category.Test Run: <select>and choose Run. | The Display Positions to be Valued view displays. |  |
| 4 | Execute Valuation for Test Run | Choose Execute Valuation.If a Message dialog box displays, choose Continue. | The Valuation Log view displays.If you see a red traffic light icon, select it to review the error message. Solve the issue and perform another test run until there is no error.To review the simulated posting information for US GAAP (valuation area 003), choose Logs + Messages. No posting is created because it is a test run.Note If there is no simulated posting, your selected transaction may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial view of this app.Change the following data:Test Run: <deselect>and choose Run. | The Display Positions to be Valued view displays. |  |
| 6 | Execute Valuation for Production Run | Choose Execute Valuation. | The Valuation Log view displays. To check the posting information for US GAAP (valuation area 003), choose Logs + Messages. The accounting document is created in the corresponding ledger of US GAAP. |  |

### Post Realized Profit and Loss (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you fix and post derived business transactions (usually realized profit and loss when deal is mature) in valuation area 003 for US GAAP.

Prerequisites

The derived business transaction is fixed and posted in valuation area AE0 for local GAAP. For more information, see the Post Realized Profit and Loss procedure in the Securities Option Management (6ND) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select>Company code: for example, 3310Valuation Area: for example, 003OTC Transactions: <transaction number(s) created in test script 6ND>TRL Date: <maturity date of transaction>Test Run: <select>and choose Run.Confirm the message Are you sure that you want to select future business transactions by choosing Enter. | The Fix and Post Derived Business Transactions view displays.If the system displays the message No scheduled derived business transactions were found for the selection, no derived transaction is available for your selection. You can skip the current step. |  |
| 4 | Fix and Post for Test Run | Choose Fix. | The Posting Log: Posted Business Transactions view displays. Simulated posting information is shown for US GAAP (valuation area 003). No posting is created because it is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial view of this app.Change the following data and choose Run:Test Run: <deselect>Confirm the message Are you sure that you want to select future business transactions by choosing Enter. | The Fix and Post Derived Business Transactions view displays. |  |
| 6 | Fix and Post for Production Run | Choose Fix. | The Posting Log: Posted Business Transactions view displays. Posting information is shown for US GAAP (valuation area 003). The accounting document is created in the US GAAP ledger in financial accounting. |  |

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
- related-to :: [[05-treasury-and-cash-management/test-script-securities-option-management-6nd-ae-sap-s-4hana-cloud-publ]]
- related-to :: [[05-treasury-and-cash-management/test-script-securities-option-management-group-ledger-ifrs-6ne-ae-1182]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6NF_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 18,687 chars in the whole document
