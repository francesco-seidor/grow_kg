---
id: 05-treasury-and-cash-management/asset-backed-securities-management-group-ledger-us-gaap-6b7-ae-1160
title: Asset-Backed Securities Management – Group Ledger US GAAP (6B7_AE) (6B7_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud 2608 test script 6B7: posting ABS investment flows and key date valuation in parallel valuation area 003 for the US GAAP ledger."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/asset-backed-securities]
aliases: [6B7_S4CLD2608_BPD_EN_AE]
keywords: [Asset-Backed Securities Management, asset-backed securities, parallel valuation, us gaap ledger, general ledger posting, key date valuation, period-end closing, treasury accounting, business conditions, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6B7_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1160
topic: 05-treasury-and-cash-management/asset-backed-securities
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Asset-Backed Securities Management – Group Ledger US GAAP (6B7_AE) (6B7_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6B7_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Asset-Backed Securities Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Asset-Backed Securities Management – Group Ledger US GAAP (6B7_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232858385)

[2 Prerequisites 3](#_Toc232858386)

[2.1 System Access 3](#_Toc232858387)

[2.2 Roles 3](#_Toc232858388)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232858389)

[2.4 Business Conditions 4](#_Toc232858390)

[3 Overview Table 6](#_Toc232858391)

[4 Test Procedures 7](#_Toc232858392)

[4.1 ABS Investment 7](#_Toc232858393)

[4.1.1 Post to General Ledger (Parallel Valuation Area) 7](#_Toc232858394)

[4.1.2 Period-end Closing (Parallel Valuation Area) 9](#_Toc232858395)

[4.1.2.1 Perform Key Date Valuation (Parallel Valuation Area) 9](#_Toc232858396)

## Purpose

Overview

By activating parallel valuation for asset-backed securities management group ledger US GAAP, you can use an additional valuation area besides your operative valuation area to reflect financial positions and investment and financing results in accordance with US Generally Accepted Accounting Principles (US GAAP).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/viewer/b249d650b15e4b3d9fc2077ee921abd0/latest/en-US/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version. |

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
| 6B5 - Asset-Backed Securities Management | Must be run before this test script.Make sure you created the deal for ABS issuance/investment with status Contract Settlement. |
| 2VA - Accounting and Financial Close – Group Ledger US GAAP | Must be in scope as prerequisite. |

## Overview Table

The scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Post to General Ledger (Parallel Valuation Area)](#unique_8) [page ] 7 | Treasury Accountant | Process Business Transactions (TPM10) | Cash flows related FI document is posted in valuation area 003 forledger of US GAAP. |
| [Perform Key Date Valuation (Parallel Valuation Area)](#unique_9) [page ] 9 | Treasury Accountant | Run Valuation (TPM1) | Valuation is executed in valuation area 003 for ledger of US GAAP. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### ABS Investment

#### Post to General Ledger (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post the flows in valuation area 003 for ledger of US GAAP. They are reflected in the corresponding ledger in Financial Accounting (FI). The flows include incoming or outgoing payment of sale transaction or purchase transation.

Prerequisite

The flows of deals have been posted in operative valuation AE0 for local GAAP, as described in the Asset-Backed Securities Management(6B5) test script. You should have executed the following activities in 6B5:

- Fix, Pay and Post Flows (TBB1): You generated a payment request for outgoing payment with option Pay Only, and generated the posting for incoming payment (without payment request) in valuation area AE0 with option Post Operational Only.
- Process Business Transactions (TPM10):You generated the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Run:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Exposure Items: <deselect this checkbox>Company Code: for example, 3310Valuation Area: for example, 003Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: <select this checkbox>Product Type: for example, 04MID Number: <The Sec. Class ID Number created in test script 6B5, and the flows are posted in oper-ative valuation AE0>FI Posting Date: enter date on which the flow of financial transaction should be posted, for example, <the current date>Trans. To Be Reversed: <deselect this checkbox>Test Run: <select this checkbox> | The Test Run : Posted/Reverse Business Transactions screen is displayed.Note If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria. You can skip the current test step. |  |
| 4 | Check Test Run Result | On the Test Run: Post/Reverse Business Transactions screen, choose Select All and choose Choose Those to Post, and then choose Run. | The Test Run: Display Posted/Reversed Business Transactions screen is displayed. |  |
| 5 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for US GAAP (valuation area 003) on this screen. Please note there is no posting created because it is test run. |  |
| 6 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Run:Test Run: <deselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 7 | Production Run | On the Update Run: Post/Reverse Business Transactions screen, choose Select All and choose Choose Those to Post, and then choose Run. | The Update Run: Display Posted/Reversed Business Transactions screen is displayed. |  |
| 8 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the posting information for US GAAP (valuation area 003) on this screen. |  |

#### Period-end Closing (Parallel Valuation Area)

Purpose

This section describes activities for period-end closing (usually executed at month end) in parallel valuation area for US GAAP, including:

- [Perform Key Date Valuation (Parallel Valuation Area)](#unique_9) [page ] 9

##### Perform Key Date Valuation (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

According to the classification of ABS investment, you can use the valuation function to value the positions of ABS based on the amortized cost or market price for a given key date in valuation area 003 for US GAAP, and transfer results to corresponding ledger for US GAAP in Financial Accounting (FI).

Prerequisite

If the classification of ABS investment is market price relevant, you should enter the latest security price for the security ID via the Update Securities Price section of the Market Rates Management – Manually via Upload (1XN).

Key date valuation is executed in valuation area AE0 for local GAAP in the Asset-Backed Securities Management(6B5) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Execute Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Execute Valuation screen, enter the following data and choose Run:Securities: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, 003Product Type: for example, 04MSecurity ID: for example, <The Sec. Class ID Number created in test script 6B5, and is valudated in operative valuation AE0>Security Account: for example, SEC_INVSTKey Date for Valuation: for example, last date of current monthValuation Category: for example, Mid-year Valuation with ResetWhen the Period End is also the Year End, the Valuation Category Year End Valuation should be used.Test Run: <select this checkbox>Amortization Log: <select this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Positions to be Valued screen, choose Run Valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for US GAAP (valuation area 003) by choosing Logs + Messages. Please note there is no posting created because it is test run.Note Sometime there is no simulated posting because your selected security class position in security account may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back to return to the initial screen of this app.On the initial screen, change the following data and choose Run:Test Run: deselect this checkbox | The Display Positions to be Valued screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Positions to be Valued screen, choose Run Valuation. | The Valuation Log screen is displayed, you can check the posting information for US GAAP (valuation area 003) by choosing Logs + Messages. Then, the accounting document has been created in the corresponding US GAAP ledger. |  |

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
- related-to :: [[05-treasury-and-cash-management/test-script-asset-backed-securities-management-6b5-ae-sap-s-4hana-clou]]
- related-to :: [[05-treasury-and-cash-management/test-script-asset-backed-securities-management-group-ledger-ifrs-6b6-a]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6B7_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 18,339 chars in the whole document
