---
id: 03-financial-accounting-and-close/sap-fiori-analytical-apps-for-asset-accounting-in-finance-2qy-853
title: SAP Fiori Analytical Apps for Asset Accounting in Finance (2QY) (2QY_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud 2608 test script for scope item 2QY: testing the Asset Accounting Overview (F3096) page, filters, cards and drill-down navigation."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/asset-accounting-ifrs-and-us-gaap]
aliases: [2QY_S4CLD2608_BPD_EN_XX]
keywords: [Asset Accounting with IFRS and US GAAP Group Ledgers, asset accounting overview, asset accounting analytics, overview page cards, global filters, business conditions, assets under construction, lease accounting, business roles, test procedures]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QY_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-853
topic: 03-financial-accounting-and-close/asset-accounting-ifrs-and-us-gaap
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# SAP Fiori Analytical Apps for Asset Accounting in Finance (2QY) (2QY_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QY_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Asset Accounting with IFRS and US GAAP Group Ledgers** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Fiori Analytical Apps for Asset Accounting in Finance (2QY) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232840852)

[2 Prerequisites 3](#_Toc232840853)

[2.1 System Access 3](#_Toc232840854)

[2.2 Roles 3](#_Toc232840855)

[2.3 Business Conditions 3](#_Toc232840856)

[3 Overview Table 5](#_Toc232840857)

[4 Test Procedures 6](#_Toc232840858)

[4.1 Asset Accounting Overview 6](#_Toc232840859)

## Purpose

Overview

This scope item provides overview pages for the Asset Accounting functionality, with a focus on assisting the Asset Accountant with high-level information about revenue, expense, journal entries, asset accounts balance, and more.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

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
| Asset Accountant | SAP_BR_AA_ACCOUNTANT | Fixed Assets | SAP_BR_AA_ACCOUNTANT |  |

### Business Conditions

Follow the procedures described in the following scope items for creating the corresponding business data if needed.

| Scope Item | Business Condition |
| --- | --- |
| J62 - Asset Accounting | Follow the scope item to create the corresponding business data. |
| BFH - Asset Under Construction | Follow the scope item to create the corresponding business data. |
| 1GB - Asset Accounting – Group Ledger IFRS | Follow the scope item to create the corresponding business data. |
| 1GF - Asset Under Construction – Group Ledger IFRS | Follow the scope item to create the corresponding business data. |
| 1T6 - Lease-In Accounting | Follow the scope item to create the corresponding business data. |
| 21P - Lease-In Accounting – Group Ledger IFRS | Follow the scope item to create the corresponding business data. |
| 2SB - Lease-Out for Sublease Accounting | Follow the scope item to create the corresponding business data. |
| 2SA - Lease-Out for Sublease Accounting – Group Ledger IFRS | Follow the scope item to create the corresponding business data. |
| 2O9 - Intercompany Process for Sublease Accounting | Follow the scope item to create the corresponding business data. |

## Overview Table

This scope item consists of several process steps, reports, items provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report, or Item | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [Asset Accounting Overview](#unique_7) [page ] 6 | Asset Accountant | Asset Accounting Overview (F3096) | The SAP Fiori overview page is running correctly. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Asset Accounting Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the Asset Accounting overview.

Prerequisite

You implemented the Asset Accounting Overview page.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Asset Accountant. |  |  |
| 2 | Set Default Value for SAP Fiori Launchpad User Setting (Optional) | On SAP Fiori launchpad, choose User > Settings > Default Values . |  |  |
| 3 | Change Defaults | Some input fields are available, such as:Company CodeLedgerCurrency TypeFisc. Year of LedgerFiscal Period (Balances)Depreciation AreaAsset ClassYou can enter and save the default values.Note Values set here are used to prepopulate the filter fields in later steps. |  |  |
| 4 | Access the App | Open Asset Accounting Overview (F3096). |  |  |
| 5 | Set Global Filters | Use the fields in the filter bar to filter the display. Fields such as the following are available:Company codeLedgerCurrency TypeFiscal YearFiscal Period (Balances)Depreciation AreaAsset ClassChoose Go. | The overview page and the following cards are displayed (the exact names may vary):Asset AcquisitionsAsset Balances - Chart ViewAsset BalancesAsset Depreciation ValuesManage Fixed AssetsAsset RetirementsAsset Transactions by TypeAsset TransactionsAssets Under Construction - AgingAssets Under ConstructionDepreciation to Be PostedOpen Purchase Orders with Account Assignment *A*Origin of AssetsOpen Purchase Orders with Account Assignment *A* - Chart ViewQuick Links |  |
| 6 | Manage Cards | To customize the cards, choose the user icon on the screen and choose Manage Cards. Make the settings of your choice and choose OK. | The cards on the overview page can be rearranged, hidden, and displayed again. |  |
| 7 | Navigate from Card Asset Acquisitions | Navigate from Asset Acquisitions, and choose the header or line item level of the card to get more detailed information. | The overview page navigates you to the Asset Transactions target app. The global filter and card information is carried over. |  |
| 8 | Navigate from Card Asset Balances. Chart View | Navigate from Asset Balances - Chart View, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the Asset Balances target app. The global filter and card information is carried over. |  |
| 9 | Navigate from Card Asset Balances | Navigate from Asset Balances, and choose the header or line item level of the card to get more detailed information. | The overview page navigates you to the Asset Balances target app. The global filter and card information is carried over. |  |
| 10 | Navigate from Card Asset Retirements | Navigate from Asset Retirements, and choose the header or line item level of the card to get more detailed information. | The overview page navigates you to the Asset Transactions target app. The global filter and card information is carried over. |  |
| 11 | Navigate from Card Depreciation to be Posted | Navigate from Depreciation to be Posted, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the Asset Balances target app. The global filter and card information is carried over. |  |
| 12 | Navigate from Card Manage Fixed Assets | Navigate from Manage Fixed Assets, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the Manage Fixed Assets target app. The global filter and card information is carried over. |  |
| 13 | Navigate from Card Asset Transactions by Type | Navigate from Asset Transactions by Type, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the Asset Transactions target app. The global filter and card information is carried over. |  |
| 14 | Navigate from Card Quick Links | Choose Quick Links on the card to get further information.Asset TransactionsAsset BalancesAsset History SheetManage Fixed Assets | The overview page navigates you to the target apps. |  |
| 15 | Navigate from Card Open Purchase Orders with Account Assignment *A* | Navigate from Open Purchase Orders with Account Assignment *A*, and choose the header or line item level of the card to get more detailed information. | The overview page navigates you to the Purchase Order Items by Account Assignment target app. The global filter and card information is carried over. |  |
| 16 | Navigate from Card Open Purchase Orders with Account Assignment *A* - Chart View | Navigate from Open Purchase Orders with Account Assignment *A* - Chart View, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the Purchase Order Items by Account Assignment target app. The global filter and card information is carried over. |  |
| 17 | Navigate from Card Asset Depreciation Values | Navigate from Asset Depreciation Values, and choose the header or line item level of the card to get more detailed information. | The overview page navigates you to the Asset Balances target app. The global filter and card information is carried over. |  |
| 18 | Navigate from Card Assets Under Construction | Navigate from Assets Under Construction, and choose the header or line item level of the card to get more detailed information. | The overview page navigates you to the Asset Balances target app. The global filter and card information is carried over. |  |
| 19 | Navigate from Card Origin of Assets | Navigate from Origin of Assets, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the Asset Balances target app. The global filter and card information is carried over. |  |
| 20 | Navigate from Card Assets Under Construction - Aging | Navigate from Assets Under Construction - Aging, and choose the header or line item level of the card to get more detailed information. | The overview page navigates you to the Asset Transactions target app. The global filter and card information is carried over. |  |
| 21 | Navigate from Card Asset Transactions | Navigate from Asset Transactions, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the Asset Transactions target app. The global filter and card information is carried over. |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-asset-accounting-group-ledger-ifrs-1gb-ae-719]]
- related-to :: [[03-financial-accounting-and-close/test-script-asset-accounting-group-ledger-us-gaap-33f-ae-898]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2QY_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 14,257 chars in the whole document
