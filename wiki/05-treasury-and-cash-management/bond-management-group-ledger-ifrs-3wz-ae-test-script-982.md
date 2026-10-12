---
id: 05-treasury-and-cash-management/bond-management-group-ledger-ifrs-3wz-ae-test-script-982
title: Bond Management – Group Ledger IFRS (3WZ_AE) Test Script (3WZ_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3WZ: parallel valuation area 002 (IFRS) postings, key date valuation and class transfer for bond issuance/investment."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/bond-management]
aliases: [3WZ_S4CLD2608_BPD_EN_AE]
keywords: [Bond Management, group ledger ifrs, parallel valuation, key date valuation, bond investment, valuation class transfer, test scripts, business roles, demo data, period-end closing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3WZ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-982
topic: 05-treasury-and-cash-management/bond-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Bond Management – Group Ledger IFRS (3WZ_AE) Test Script (3WZ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3WZ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Bond Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Bond Management – Group Ledger IFRS (3WZ_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Bond Management – Group Ledger IFRS (3WZ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853951)

[2 Prerequisites 4](#_Toc232853952)

[2.1 System Access 4](#_Toc232853953)

[2.2 Roles 4](#_Toc232853954)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232853955)

[2.4 Business Conditions 5](#_Toc232853956)

[3 Overview Table 6](#_Toc232853957)

[4 Test Procedures 7](#_Toc232853958)

[4.1 Bond Issuance 7](#_Toc232853959)

[4.1.1 Post to General Ledger (Parallel Valuation Area) 7](#_Toc232853960)

[4.1.2 Period-end Closing (Parallel Valuation Area) 9](#_Toc232853961)

[4.1.2.1 Perform Key Date Valuation (Parallel Valuation) 9](#_Toc232853962)

[4.1.3 Reclassification (Parallel Valuation Area) 11](#_Toc232853963)

[4.1.3.1 Perform valuation class transfer (Parallel Valuation Area) 11](#_Toc232853964)

[4.2 Bond Investment 11](#_Toc232853965)

[4.2.1 Post to General Ledger (Parallel Valuation Area) 11](#_Toc232853966)

[4.2.2 Period-end Closing (Parallel Valuation Area) 13](#_Toc232853967)

[4.2.2.1 Perform Key Date Valuation (Parallel Valuation Area) 13](#_Toc232853968)

[4.2.3 Reclassification (Parallel Valuation Area) 15](#_Toc232853969)

[4.2.3.1 Perform valuation class transfer (Parallel Valuation Area) 15](#_Toc232853970)

## Purpose

Overview

By activating parallel valuation for bond management – group ledger , you can use an additional valuation area besides your operative valuation area to reflect financial positions, investment, and financing results in accordance with International Financial Reporting Standards (9) phase I (Classification and Measurement).

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

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

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

| Scope Item | Business Condition |
| --- | --- |
| 3WY - Bond Management | Must be run before this test script.Make sure you created the deal for bond issuance/investment with status Contract Settlement. |
| 1GA - Accounting and Financial Close – Group Ledger IFRS | Must be in scope as prerequisite. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Post to General Ledger (Parallel Valuation Area)](#unique_8) [page ] 7 | Treasury Accountant | Process Business Transactions (TPM10) | Cash flows related FI document is posted in valuation area 002 forledger of IFRS . |
| [Perform Key Date Valuation (Parallel Valuation)](#unique_9) [page ] 9 | Treasury Accountant | Run Valuation (TPM1) | Valuation is executed in valuation area 002 for ledger of IFRS. |
| [Perform valuation class transfer (Parallel Valuation Area)](#unique_10) [page ] 11 | Treasury Accountant | Execute Valuation Class Transfer (TPM15M) | Valuation class transfer is executed in all valuation areas, include parallel valuation area 002. |
| [Post to General Ledger (Parallel Valuation Area)](#unique_11) [page ] 11 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) | Cash flows related FI document is posted in valuation area 002 for ledger of IFRS . |
| [Perform Key Date Valuation (Parallel Valuation Area)](#unique_12) [page ] 13 | Treasury Accountant | Run Valuation (TPM1) | Valuation is executed in valuation area 002 for ledger of IFRS. |
| [Perform valuation class transfer (Parallel Valuation Area)](#unique_13) [page ] 15 | Treasury Accountant | Execute Valuation Class Transfer (TPM15M) | Valuation class transfer is executed in all valuation areas, include parallel valuation area 002. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Bond Issuance

#### Post to General Ledger (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the flows in parallel valuation area 002 for IFRS. They are reflected in the corresponding ledgerin Financial Accounting (FI). The flows include incoming or outgoing payment of placement or unscheduled redemption.

Prerequisite

You have already post flows of deals in operative valuation AE0 for local GAAP, as described in the Bond Management (3WY) test scrip by executing the following activities:

- Fix, Pay and Post Flows (TBB1): You generated a payment request for outgoing payment with option Pay Only, and generated the posting for incoming payment (without payment request) in valuation area AE0 with option Post Operational Only.
- Process Business Transactions (TPM10):You generated the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Exposure Items: <deselect this checkbox>Company Code: for example 3310Valuation Area: for example 002Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: <select this checkbox>Product Type: for example 04AID Number: <The Sec. Class ID Number created in test script 3WY, and the flows are posted in operative valuation AE0>FI Posting Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Trans. To Be Reversed: <deselect this checkbox>Test Run: <select this checkbox> | Screen Test Run : Posted /Reverse Business Transactions is displayed.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria, you can skip the current test step. |  |
| 4 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute. | Screen Test Run: Display Posted/Reversed Business Transactions displays. |  |
| 5 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for IFRS (valuation area 002) on this screen. Please note there is no posting created because it is test run. |  |
| 6 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 7 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute. | Screen Update Run: Display Posted/Reversed Business Transactions displays. |  |
| 8 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the posting information for IFRS (valuation area 002) on this screen. |  |

#### Period-end Closing (Parallel Valuation Area)

Purpose

This section describes activities for period-end closing (usually executed at month end) in parallel valuation area for IFRS, including:

- [Perform Key Date Valuation (Parallel Valuation)](#unique_9) [page ] 9

##### Perform Key Date Valuation (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

According to the classification of bond issuance, you can use the valuation function to value the positions of bond based on the amortized cost or market price for a given key date in valuation area 002 for IFRS, and transfer results to the corresponding ledger for IFRS in Financial Accounting (FI).

Prerequisite

Key date valuation is executed in valuation area AE0 for local GAAP in the Bond Management (3WY).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Execute Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Execute Valuation screen, enter the following data and choose Execute:Securities: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, 002Product Type: for example, 04ASecurity ID: for example, <The Sec. Class ID Number created in test script 3WY, and is valudated in operative valuation AE0>Security Account: for example, BOND_ISSUEKey Date for Valuation: for example, last date of current monthValuation Category: for example, Mid-year Valuation with ResetWhen the Period End is also the Year End, the Valuation Category Year End Valuation should be used.Test Run: <select this checkbox>Amortization Log: <select this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Positions to be Valued screen, choose Run Valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for IFRS (valuation area 002) by choosing Logs + Messages. Please note there is no posting created because it is test run.Note Sometime there is no simulated posting because your selected security class position in security account may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Positions to be Valued screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Positions to be Valued screen, choose Run Valuation. | The Valuation Log screen is displayed, you can check the posting information for IFRS (valuation area 002) by choosing Logs + Messages. Then, the accounting document has been created in the corresponding IFRS ledger. |  |

#### Reclassification (Parallel Valuation Area)

##### Perform valuation class transfer (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the valuation class transfer is executed from long term to short term in all valuation areas, and reflected in all ledgers in Financial Accounting (FI).

Procedure

Because the valuation class transfer should be executed for all valuation areas at the same time, see the Perform valuation class transfer step in the Bond Management (3WY) test script for executing valuation class transfer.

### Bond Investment

#### Post to General Ledger (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the flows in parallel valuation area 002 for IFRS. They are reflected in the corresponding ledger in Financial Accounting (FI). The flows include incoming or outgoing payment of sale transaction or purchase transation.

Prerequisite

You have posted the flows of deals in operative valuation AE0 for local GAAP, described in the Bond Management (3WY) test scrip, by executing the following activities:

- Fix, Pay and Post Flows (TBB1): You generated a payment request for outgoing payment with option Pay Only, andgenerated the posting for incoming payment (without payment request) in valuation area AE0 with option Post Operational Only.
- Process Business Transactions (TPM10): You generated the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Exposure Items: <deselect this checkbox>Company code: for example, 3310Valuation Area: for example 002Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: <select this checkbox>Product Type: for example 04AID Number: ID Number: <The Sec. Class ID Number created in test script 3WY, and the flows are posted in operative valuation AE0>FI Posting Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Trans. To Be Reversed: <deselect this checkbox>Test Run: <select this checkbox> | Screen Test Run: Posted/Reverse Business Transactions is displayed.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria, you can skip the current test step. |  |
| 4 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute. | Screen Test Run: Display Posted/Reversed Business Transactions displays. |  |
| 5 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for IFRS (valuation area 002) on this screen. Please note there is no posting created because it is test run. |  |
| 6 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 7 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute. | Screen Update Run: Display Posted/Reversed Business Transactions displays. |  |
| 8 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the posting information for IFRS (valuation area 002) on this screen. |  |

#### Period-end Closing (Parallel Valuation Area)

This section describes activities for period-end closing (usually executed at month end) in parallel valuation area for IFRS, including:

- [Perform Key Date Valuation (Parallel Valuation Area)](#unique_12) [page ] 13

##### Perform Key Date Valuation (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

According to the classification of bond investment, you can use the valuation function to value the positions of bond based on the amortized cost or market price for a given key date in valuation area 002 for IFRS, and transfer results to corresponding ledger for IFRS in Financial Accounting (FI).

Prerequisite

If the classification of bond investment is market price relevant, You should entere latest security price for the security ID via Update Securities Price section of the Market Rates Management – Manually via Upload (1XN).

Key date valuation is executed in valuation area AE0 for local GAAP in the Bond Management (3WY).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Execute Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Execute Valuation screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions:<unselect this checkbox>Company Code: for example, 3310Valuation Area: for example, 002Product Type: for example, 04ASecurity ID: for example, <The Sec. Class ID Number created in test script 3WY, and is valudated in operative valuation AE0>Security Account: for example, BOND_ISSUEKey Date for Valuation: for example, last date of current monthValuation Category: for example, Mid-year Valuation with ResetWhen the Period End is also the Year End, the Valuation Category Year End Valuation should be used.Test Run: <select this checkbox>Amortization Log: <select this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Positions to be Valued screen, choose Run Valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for IFRS (valuation area 002) by choosing Logs + Messages. Please note there is no posting created because it is test run.Note Sometime there is no simulated posting because your selected security class position in security account may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Positions to be Valued screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Positions to be Valued screen, choose Run Valuation. | The Valuation Log screen is displayed, you can check the posting information for IFRS (valuation area 002) by choosing Logs + Messages. Then, the accounting document has been created in the corresponding IFRS ledger. |  |

#### Reclassification (Parallel Valuation Area)

##### Perform valuation class transfer (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, the valuation class transfer is executed from long term to short term in all valuation areas, and reflectedin all ledgers in Financial Accounting (FI).

Procedure

Because the valuation class transfer should be executed for all valuation areas at the same time, please refer to the Perform valuation class transfer step in the Bond Management (3WY) test script for executing valuation class transfer.

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
- related-to :: [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-01]]
- related-to :: [[05-treasury-and-cash-management/test-script-bond-management-group-ledger-us-gaap-3x0-ae-983]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3WZ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 27,526 chars in the whole document
