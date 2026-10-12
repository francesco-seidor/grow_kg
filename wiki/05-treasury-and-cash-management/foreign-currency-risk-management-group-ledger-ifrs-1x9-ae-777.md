---
id: 05-treasury-and-cash-management/foreign-currency-risk-management-group-ledger-ifrs-1x9-ae-777
title: Foreign Currency Risk Management – Group Ledger IFRS (1X9_AE) (1X9_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud 2608 test script for parallel valuation (IFRS 9, valuation area 002) of foreign currency risk: flow posting, key date valuation, realized P&L."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/foreign-currency-risk-management]
aliases: [1X9_S4CLD2608_BPD_EN_AE]
keywords: [Foreign Currency Risk Management (FX Deals), foreign currency risk management, parallel valuation, ifrs ledger, key date valuation, flow posting, realized profit and loss, hedge accounting, demo data, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X9_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-777
topic: 05-treasury-and-cash-management/foreign-currency-risk-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Foreign Currency Risk Management – Group Ledger IFRS (1X9_AE) (1X9_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X9_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Foreign Currency Risk Management (FX Deals)** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Foreign Currency Risk Management – Group Ledger IFRS (1X9_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232848474)

[2 Prerequisites 3](#_Toc232848475)

[2.1 System Access 3](#_Toc232848476)

[2.2 Roles 3](#_Toc232848477)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232848478)

[2.4 Business Conditions 4](#_Toc232848479)

[3 Overview Table 5](#_Toc232848480)

[4 Test Procedures 6](#_Toc232848481)

[4.1 Post Flows to General Ledger (Parallel Valuation Area) 6](#_Toc232848482)

[4.2 Period-end Closing (Parallel Valuation) 7](#_Toc232848483)

[4.2.1 Perform Key Date Valuation (Parallel Valuation) 8](#_Toc232848484)

[4.3 Post Realized Profit and Loss (Parallel Valuation) 9](#_Toc232848485)

## Purpose

Overview

By activating parallel valuation for Foreign Currency Risk Management – Group Ledger IFRS, you can use an additional valuation area besides your operational valuation area according to International Financial Reporting Standards (IFRS 9) phase I (Classification and Measurement).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP S/4HANA system | Accessible via Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Treasury Accountant | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Valuation Area | 002 |  |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1X1 - Foreign Currency Risk Management. | Must be run before this test scriptMake sure you have created deal of foreign exchange with statusContract Settlement |
| 1GA - Accounting and Financial Close – Group Ledger IFRS | Must be in scope as prerequisite. |

## Overview Table

The scope item Foreign Currency Risk Management – Group Ledger IFRS consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Post Flows to General Ledger (Parallel Valuation Area)](#unique_8) [page ] 6 | Treasury Accountant | Process Business Transactions (TPM10) | Flows are posted in valuation area 002 for ledger of IFRS |
| [Perform Key Date Valuation (Parallel Valuation)](#unique_9) [page ] 8 | Treasury Accountant | Run Valuation (TPM1) | Valuation is executed in valuation area 002 for ledger of IFRS |
| [Post Realized Profit and Loss (Parallel Valuation)](#unique_10) [page ] 9 | Treasury Accountant | Post Derived Business Transactions (TPM18) | Realized profit and loss are posted in valuation area 002 for ledger of IFRS |

## Test Procedures

### Post Flows to General Ledger (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the flows in parallel valuation area 002 for IFRS. They are reflected in the corresponding ledger in Financial Accounting (FI). The flows include buying foreign exchange, selling foreign exchange, and premium of currency options.

Prerequisites

The flows of deals are posted in operative valuation AE0 for local GAAP. This is described in test script Foreign Currency Risk Management (1X1).

You executed the following activities in 1X1 with apps:

- Post Flows: You generated a payment request for outgoing payment with option Pay Only, and generated the posting for incoming payment (without payment request) in valuation area AE0 with option Post Operational Only.
- Process Business Transactions: You generated the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Run:OTC Transactions: SelectedCompany Code: for example 3310Valuation Area: for example, 002Limit by Transaction Number: DeselectedLimit by Subledger Pos.: SelectedTransaction: <transaction number(s) created in test script 1X1 with flows posted in valuation area AE0>Test Run: Selected | The Test Run: Post/Reverse Business Transactions screen displays.If the system displays the message You have not selected any business transactions, no posting is needed for your selection criteria. Skip this step. |  |
| 4 | Check Test Run Result | Choose Select All, choose Choose Those to Post, and choose Execute. | The Test Run: Display Posted/Reversed Business Transactions screen displays. |  |
| 5 | Logs and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen displays. Check the simulated posting information for IFRS (valuation area 002) on this screen. No posting is created because it is a test run. |  |
| 6 | Enter Selection Criteria for Production Run | Choose Back. | The Process Business Transactions screen displays. |  |
| 7 | Deselect Test Run | Change the following data and choose Run:Test Run: Deselected | The Update Run: Post/Reverse Business Transactions screen displays. |  |
| 8 | Production Run | Choose Select All, choose Choose Those to Post, and choose Execute. | The Update Run: Display Posted/Reversed Business Transactions screen displays. |  |
| 9 | Logs and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen displays. An accounting document is created for IFRS (valuation area 002) |  |

### Period-end Closing (Parallel Valuation)

Purpose

In this section, you perform key date valuation for period-end closing (usually executed at month end) in the parallel valuation area for IFRS.

#### Perform Key Date Valuation (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to:

- Value the positions of financial instruments based on historical cost or fair value for a given key date in valuation area 002 for IFRS
- Transfer results to the corresponding IFRS ledger in Financial Accounting (FI)

|  |
| --- |
| Note If the FX transaction is designated as a hedging instrument in a Hedging Relationship of IFRS9 Hedge Accounting for Parallel Valuation Area 002, skip this step. |

Prerequisites

Fair values (NPV) are calculated or maintained for financial transactions that are evaluated at fair value (NPV) according to IFRS. For more information, see the Calculate or Maintain Fair Value of Transaction step in test script Foreign Currency Risk Management(1X1).

Key date valuation is executed in valuation area AE0 for local GAAP in test script Foreign Currency Risk Management(1X1).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Execute Valuation screen displays. |  |
| 3. | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany code: for example 3310Valuation Area: for example, 002Transaction: <transaction number(s) created in test script 1X1>Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, <Mid-year Valuation with Reset>Note When the period end is also the year end, use the Valuation Category Year-End Valuation.Test Run: Selected | The Display Positions to be Valued screen displays. |  |
| 4. | Execute Valuation for Test Run | Choose Execute Valuation.If the Message dialog box displays, choose Continue. | The Valuation Log screen displays. If an entry has a red traffic light exist, click it and check the error message. Solve the issue and perform another test run until the error is cleared.To check the simulated posting information for IFRS (valuation area 002), choose Logs + Messages. No posting is created because it is a test run.Note Occasionally, no simulated postings are shown. Your selected transaction may not need valuation. |  |
| 5. | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: Deselected | The Display Positions to be Valued screen displays. |  |
| 6. | Execute Valuation for Production Run | Choose Execute Valuation. | The Valuation Log screen displays. To check the posting information for IFRS (valuation area 002), chose Logs + Messages. An accounting document is created in the corresponding IFRS ledger. |  |

### Post Realized Profit and Loss (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you fix and post derived business transactions (usually, realized profit and loss when deal is mature) in valuation area 002 for IFRS.

|  |
| --- |
| Note If the FX transaction is designated as a hedging instrument in a Hedging Relationship of IFRS9 Hedge Accounting for Parallel Valuation Area 002, please skip this step. |

Prerequisites

The derived business transaction is fixed and posted in valuation area AE0 for local GAAP. This is described in the Post Realized Profit and Loss step in test script Foreign Currency Risk Management(1X1).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3. | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany code: for example, 3310Valuation Area: for example, 002OTC Transactions: <transaction number(s) created in test script 1X1>TRL Date: <maturity date of transaction>Test Run: SelectedConfirm the message Are you sure that you want to select future business transactions by pressing Enter. | The Fix and Post Derived Business Transactions screen displays.If the system displays the message No scheduled derived business transactions were found for the selection, no derived transaction is available for your selection, You can skip this step. |  |
| 4. | Fix and Post for Test run | Choose Fix. | The Posting Log: Posted Business Transactions screen displays. The simulated posting information for IFRS (valuation area 002) is shown. No posting is created, because it is a test run. |  |
| 5. | Enter Selection Criteria for Production Run | Choose Back until you return to the the initial screen of this app.Change the following data and choose Execute:Test Run: DeselectedConfirm the message Are you sure that you want to select future business transactions by pressing Enter | The Fix and Post Derived Business Transactions screen displays. |  |
| 6. | Fix and Post for Production run | Choose Fix. | The Posting Log: Posted Business Transactions screen displays. The posting information for IFRS (valuation area 002) is shown. An accounting document is created in the IFRS ledger in financial accounting. |  |

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
- related-to :: [[05-treasury-and-cash-management/foreign-currency-risk-management-group-ledger-us-gaap-34d-ae-908]]
- related-to :: [[05-treasury-and-cash-management/test-script-foreign-currency-risk-management-1x1-ae-sap-s-4hana-cloud-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X9_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 18,864 chars in the whole document
