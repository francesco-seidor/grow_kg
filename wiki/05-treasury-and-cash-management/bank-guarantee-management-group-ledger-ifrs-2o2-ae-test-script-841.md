---
id: 05-treasury-and-cash-management/bank-guarantee-management-group-ledger-ifrs-2o2-ae-test-script-841
title: Bank Guarantee Management - Group Ledger IFRS (2O2_AE) - Test Script (2O2_S4CLD2608_BPD_EN_AE)
description: "SAP test script for scope item 2O2_AE: posting bank guarantee flows to the IFRS ledger in parallel valuation area 002 via TPM10, Treasury Accountant role."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/bank-guarantees]
aliases: [2O2_S4CLD2608_BPD_EN_AE]
keywords: [Bank Guarantee Management, parallel valuation, ifrs ledger, posting flows to general ledger, test script, treasury accounting, business conditions, master data scripts, demo data, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2O2_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-841
topic: 05-treasury-and-cash-management/bank-guarantees
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Bank Guarantee Management - Group Ledger IFRS (2O2_AE) - Test Script (2O2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2O2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Bank Guarantee Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Bank Guarantee Management – Group Ledger IFRS (2O2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232849801)

[2 Prerequisites 3](#_Toc232849802)

[2.1 System Access 3](#_Toc232849803)

[2.2 Roles 3](#_Toc232849804)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232849805)

[2.4 Business Conditions 4](#_Toc232849806)

[3 Overview Table 5](#_Toc232849807)

[4 Test Procedures 6](#_Toc232849808)

[4.1 Post Flows to General Ledger (Parallel Valuation Area) 6](#_Toc232849809)

## Purpose

Overview

By activating parallel valuation for bank guarantee management, you can use another valuation area in addition to your operational valuation area per International Financial Reporting Standards (IFRS 9) phase I (Classification and Measurement).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

### System Access

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

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 2NZ - Bank Guarantee Management | The TRM transaction has been created and with status Contract Settlement. To create a deal of Trade Finance transaction, please see test script Bank Guarantee Management (2NZ). |
| 1GA - Accounting and Financial Close – Group Ledger IFRS | Must be in scope as prerequisite. |

## Overview Table

The scope item Bank Guarantee Management – Group Ledger IFRS consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Post Flows to General Ledger (Parallel Valuation Area)](#unique_8) [page ] 6 | Treasury Accountant | Process Business Transactions (TPM10) | Flows are posted in valuation area 002 for ledger of IFRS. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The test should take around <Enter a duration, e.g. 60 minutes>.

### Post Flows to General Ledger (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The step describes how to post the flows in parallel valuation area 002 for IFRS. They will be reflected in corresponding ledger in Financial Accounting (FI). The flows include cash collateral and free condition fees, and other bank fees.

Prerequisites

The flows of deals have been posted in operative valuation AE0 for local GAAP, which are described in test script 2NZ: Bank Guarantee Management. You have executed the following activities in 2NZ with apps:

- Fix, Pay and Post Flows (TBB1): You have used this app to generate payment request for outgoing payment with option Pay Only, and generate the posting for incoming payment (without payment request) in valuation area AE0 with option Post Operational Only.
- Process Business Transactions (TPM10): You have used this app to generate the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Product Groups:OTC Transactions: <select this checkbox>General Selections:Company Code: for example 3310Valuation Area: for example 002Limit by Subledger Pos.: <select this checkbox>Transaction: <transaction number(s) was created in the test script 2NZ Bank Guarantee Management, and flows have been posted in valuation area AE0>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen displays.If the message You have not selected any business transactions. displays, it means there is no posting needed for your selection criteria in which case you can skip the current step. |  |
| 4 | Check Test Run Result | On the Test Run: Post/Reverse Business Transactions screen, choose Select All and choose Choose Those to Post, and then choose Save.The Test Run: Display Posted/Reversed Business Transactions screen displays, choose Logs and Messages. | The Information Overview dialog box displays. You can check the simulated posting information for IFRS (valuation area 002) on this screen. Note there is no posting created because it is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Close.On the Fix, Post or Reverse Transactions screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen displays. |  |
| 6 | Check Production Run Result | On the Update Run: Post/Reverse Business Transactions screen, choose Select All and choose Choose Those to Post, and then choose Save.The Update Run: Display Posted/Reversed Business Transactions screen displays, choose Logs and Messages. | The Information Overview dialog box displays. The accounting document has been created for IFRS (valuation area 002). |  |

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
- related-to :: [[05-treasury-and-cash-management/bank-guarantee-management-group-ledger-us-gaap-34f-ae-test-script-910]]
- related-to :: [[05-treasury-and-cash-management/test-script-bank-guarantee-management-2nz-ae-839]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2O2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 12,663 chars in the whole document
