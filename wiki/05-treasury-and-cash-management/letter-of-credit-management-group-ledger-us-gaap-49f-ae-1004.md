---
id: 05-treasury-and-cash-management/letter-of-credit-management-group-ledger-us-gaap-49f-ae-1004
title: Letter of Credit Management – Group Ledger US GAAP (49F_AE) (49F_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script 49F_AE: parallel valuation area postings and key date valuation for letter of credit management under US GAAP group ledger."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/letters-of-credit, topic/treasury-parallel-valuation-areas]
aliases: [49F_S4CLD2608_BPD_EN_AE]
keywords: [Letter of Credit Management, parallel valuation, general ledger posting, key date valuation, group ledger us gaap, period-end closing, treasury accountant role, business conditions, demo data, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49F_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1004
topic: 05-treasury-and-cash-management/letters-of-credit
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Letter of Credit Management – Group Ledger US GAAP (49F_AE) (49F_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49F_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Letter of Credit Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Letter of Credit Management – Group Ledger US GAAP (49F_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232854681)

[2 Prerequisites 3](#_Toc232854682)

[2.1 System Access 3](#_Toc232854683)

[2.2 Roles 3](#_Toc232854684)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232854685)

[2.4 Business Conditions 4](#_Toc232854686)

[3 Overview Table 5](#_Toc232854687)

[4 Test Procedures 6](#_Toc232854688)

[4.1 Post Flows 6](#_Toc232854689)

[4.1.1 Post to General Ledger (Parallel Valuation Area) 6](#_Toc232854690)

[4.2 Acceptance or Presentation 8](#_Toc232854691)

[4.2.1 Post to General Ledger (Parallel Valuation Area) 8](#_Toc232854692)

[4.3 Period-end Closing (Parallel Valuation) 9](#_Toc232854693)

[4.3.1 Perform Key Date Valuation (Parallel Valuation) 10](#_Toc232854694)

## Purpose

Overview

By activating parallel valuation for letter of credit management, you can use another valuation area in addition to your operational valuation area per US GAAP.

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

| Name (Role Template) | Description | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- | --- |
| Treasury Accountant |  | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

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
| 49D - Letter of Credit Management | Must be run before this test script.Make sure you created the deal of Letter of Credit with status Contract Settlement. |
| 2VA - Accounting and Financial Close – Group Ledger US GAAP | Must be in scope as prerequisite. |

## Overview Table

This scope item consists of several process steps that are listed in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Post to General Ledger (Parallel Valuation Area)](#unique_8) [page ] 6 | Treasury Accountant | Process Business Transactions (TPM10) | Flows are posted in valuation area 002 for ledger of IFRS. |
| [Post to General Ledger (Parallel Valuation Area)](#unique_9) [page ] 8 | Treasury Accountant | Process Business Transactions (TPM10) | Flows are posted in valuation area 002 for ledger of IFRS. |
| [Perform Key Date Valuation (Parallel Valuation)](#unique_10) [page ] 10 | Treasury Accountant | Run Valuation (TPM1) | Valuation is executed in valuation area 002 for ledg-er of IFRS. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The test should take around <Enter a duration, e.g. 60 minutes>.

### Post Flows

Purpose

This section describes activities for post flows in parallel valuation area for IFRS, including:

- [Post to General Ledger (Parallel Valuation Area)](#unique_8) [page ] 6

#### Post to General Ledger (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the flows in parallel valuation area 003 for US GAAP. The flows are reflected in the corresponding ledger in Financial Accounting (FI). The flows include incoming or outgoing payment of charges and cash collateral.

Prerequisites

The flows of deals are posted in operative valuation AE0 for local GAAP. For more information, ensure that you executed the following apps in the Letter of Credit Management (49D) test script:

- Fix, Pay and Post Flows (TBB1): You used this app to generate a payment request for outgoing payment with the Pay Only option. You generated the posting for incoming payment (without payment request) in valuation area AE0 with the Post Operational Only option.
- Process Business Transactions (TPM10): You used this app to generate the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Run:OTC Transactions: <select>Company Code: for example, 3310Valuation Area: for example, 003Limit by Transaction Number: <deselect>Limit by Subledger Pos.: <select>Transaction: <transaction number(s) was created in test script 49D.Make sure the flows have been posted in valuation area AE0>Test Run: <select> | The Test Run: Post/Reverse Business Transactions view displays.If the system displays the message You have not selected any business transactions, no posting is needed for your selection criteria. You can skip the current step. |  |
| 4 | Review Test Run Result | Choose Select All.Select Choose Those to Post and choose Run.On the Test Run: Display Posted/Reversed Business Transactions view, choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Check the simulated posting information for US GAAP (valuation area 003) on this view. No posting is created because it is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back.Change the following data and choose Run.Test Run: <deselect> | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 6 | Production Run | Choose Select All.Select Choose Those to Post and choose Run.On the Update Run: Display Posted/Reversed Business Transactions view, choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. An accounting document is created for US GAAP (valuation area 003). |  |

### Acceptance or Presentation

Purpose

This section describes activities for post flows in parallel valuation area for IFRS, including:

- [Post to General Ledger (Parallel Valuation Area)](#unique_9) [page ] 8

#### Post to General Ledger (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the flows in parallel valuation area 003 for US GAAP. The flows are reflected in the corresponding ledger in Financial Accounting (FI). The flows include incoming or outgoing payment of letter of credit receivables or payables.

Prerequisites

The flows of deals are posted in operative valuation AE0 for local GAAP. For more information, ensure that you executed the following apps in the Letter of Credit Management (49D) test script:

- Fix, Pay and Post Flows (TBB1): You used this app to generate a payment request for outgoing payment with the Pay Only option. You generated the posting for incoming payment (without payment request) in valuation area AE0 with the Post Operational Only option.
- Process Business Transactions (TPM10): You used this app to generate the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Run:OTC Transactions: <select>Company Code: for example, 3310Valuation Area: for example, 003Limit by Transaction Number: <deselect>Limit by Subledger Pos.: <select>Transaction: <transaction number(s) you created in test script 49D. Make sure the flows have been posted in valuation area AE0>Test Run: <select> | The Test Run: Post/Reverse Business Transactions view displays.If the system displays the message You have not selected any business transactions, no posting is needed for your selection criteria. You can skip the current step. |  |
| 4 | Review Test Run Result | Choose Select All.Select Choose Those to Post and choose Run.On the Test Run: Display Posted/Reversed Business Transactions view, choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Check the simulated posting information for US GAAP (valuation area 003) on this view. No posting is created because it is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back.Change the following data and choose Run.Test Run: <deselect> | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 6 | Production Run | Choose Select All.Select Choose Those to Post and choose Run.On the Update Run: Display Posted/Reversed Business Transactions view, choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. An accounting document is created for US GAAP (valuation area 003). |  |

### Period-end Closing (Parallel Valuation)

Purpose

This section describes activities for period-end closing (usually executed at month end) in parallel valuation area for IFRS, including:

- [Perform Key Date Valuation (Parallel Valuation)](#unique_10) [page ] 10

#### Perform Key Date Valuation (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to execute foreign currency valuation in valuation area 002 for IFRS, and transfer results to corresponding ledger for IFRS in Financial Accounting (FI).

Prerequisites

Key date valuation is executed in valuation area AE0 for local GAAP in test script Letter of Credit Management (49D).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Execute Valuation screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select>Company code: for example 3310Valuation Area: for example 002Transaction: <transaction number(s) you created in test script 49D>Key Date for Valuation: for example, <last date of current month>Note Make sure the Key Date for Valuation is between the Presentation Date and the Payment Date.Valuation Category: for example Mid-year Valuation with ResetWhen the Period End is also the Year End, use the Valuation Category Year-End Valuation should be usedTest Run: <select> | The Display Positions to be Valued screen displays. |  |
| 4 | Execute Valuation for Test Run | Choose Execute Valuation.If the Message dialog box displays, choose Continue. | The Valuation Log screen displays. If an entry has a red traffic light, click it and check the error message. Perform the test run again until the error is resolved.To check the simulated posting information for IFRS (valuation area 002), choose Logs + Messages. No posting is created because it is a test run.Note Occasionally, if your selected transaction does not need valuation, there is no simulated posting. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: <deselect> | The Display Positions to be Valued screen displays. |  |
| 6 | Execute Valuation for Production Run | Choose Execute Valuation. | The Valuation Log screen displays. To check the posting information for IFRS (valuation area 002), choose Logs + Messages. An accounting document is created in the corresponding IFRS ledger. |  |

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
> Flagged while digesting this document, not verified: Internal inconsistency: procedure sections say flows are posted in valuation area 003 for US GAAP, while the overview table and some section purposes say area 002 for the IFRS ledger (sample data lists 002); area/GAAP naming is unclear.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/letter-of-credit-management-group-ledger-ifrs-49e-ae-1003]]
- related-to :: [[05-treasury-and-cash-management/test-script-letter-of-credit-management-49d-ae-sap-s-4hana-cloud-publi-part-01]]
- see-also :: [[05-treasury-and-cash-management/test-script-debt-and-investment-management-group-ledger-ifrs-1x7-ae-77]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49F_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 19,164 chars in the whole document
