---
id: 06-management-accounting/master-data-script-create-co-cost-rates-mds-3kw-353
title: "Master Data Script: Create CO Cost Rates - MDS (3KW) (3KW_S4CLD2608_Master_Data_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 master data script for creating CO cost rates (services, plan, actual) via Fiori apps F3161, F3162, F3422, plus display report."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-rates]
aliases: [3KW_S4CLD2608_Master_Data_EN_XX]
keywords: ["CO Cost Rates (Service, Plan and Actual)", cost rates, service cost rates, plan cost rates, actual cost rates, intercompany clearing accounts, intercompany margin accounts, display cost rates, business roles, activity allocation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-353
topic: 06-management-accounting/cost-rates
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Master Data Script: Create CO Cost Rates - MDS (3KW) (3KW_S4CLD2608_Master_Data_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_EN_XX.docx`, extracted with `mammoth`. Grouped under **CO Cost Rates (Service, Plan and Actual)** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Master Data ScriptSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Create CO Cost Rates - MDS (3KW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc233904646)

[2 Prerequisites 3](#_Toc233904647)

[2.1 System Access 3](#_Toc233904648)

[2.2 Roles 3](#_Toc233904649)

[2.3 Preliminary Steps 3](#_Toc233904650)

[2.3.1 Optional: Maintain Intercompany Clearing Accounts (only for intercompany postings) 3](#_Toc233904651)

[2.3.2 Optional: Maintain Margin Accounts (only for intercompany postings with intercompany rates) 5](#_Toc233904652)

[3 Overview Table 6](#_Toc233904653)

[4 Test Procedures 7](#_Toc233904654)

[4.1 Manage Cost Rates - Services 7](#_Toc233904655)

[4.2 Manage Cost Rates - Plan 10](#_Toc233904656)

[4.3 Manage Cost Rates - Actual 11](#_Toc233904657)

[5 Analytics 13](#_Toc233904658)

[5.1 Display Cost Rates 13](#_Toc233904659)

## Purpose

The following apps are available for maintaining cost rates (activity prices). Each app has a different purpose, depending on how the rates can be defined and which objects can receive activity allocations.

| App | Affected Scope Items | Comments |
| --- | --- | --- |
| Manage Cost Rates - Services (F3161) | Time Recording (1Q4)Overhead Cost Accounting (J54)Time Recording – Project-Based Services (J12)Service Order Management and Monitoring (3D2) | Time recording |
| Manage Cost Rates - Plan (F3162) | Standard Cost Calculation (BEG)Period-End Closing – Plant (BEI)Period-End Closing – Maintenance Orders (BF7) | Manufacturing confirmations, order plan and actual confirmations |
| Manage Cost Rates - Actual (F3422) | Actual Costing (33Q) | Used to enter actual cost rates for cost center activities.Actual cost rates are only required if a customer wants to use actual costing. |

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Preliminary Steps

#### Optional: Maintain Intercompany Clearing Accounts (only for intercompany postings)

Use

This activity lets you create and update clearing accounts for intercompany (ICO) postings. The ICO clearing accounts are derived from the G/L account of the activity.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, choose Set Local Version to change the country.
4. Choose Configure Your Solution.
5. In the Configuration Steps section, in the Name column, for the Automatic Account Determination (100297) row, choose Configure.
6. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Automatic Account Determination activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Area | For the displayed row, make the following entries and choose Step 2:Area: ControllingSubarea: Cost Center AccountingProcess: Assign Intercompany Clearing Account for Actual Postings |  |  |
| 2 | Select Parameters | Make the following entry and choose Step 3:Chart of Accounts: YCOA |  |  |
| 3 | Maintain Account Determination | Add an account that is relevant for ICO clearing.Note Default content is delivered with clearing G/L account 68888800 - ICO Clearing Account - Travel, and 99999900 - ICO Clearing Account - Consultancy. You can use this a reference to create your own accounts, if required (with G/L account type N-Non Operating Expense or Income). |  |  |

#### Optional: Maintain Margin Accounts (only for intercompany postings with intercompany rates)

Use

This activity lets you create and update margin accounts for intercompany (ICO) postings. This step is required if you maintain and post with ICO rates. The margin G/L clearing accounts are derived based on the activity allocation G/L account.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, choose Set Local Version to change the country.
4. Choose Configure Your Solution.
5. In the Configuration Steps section, in the Name column, for the Automatic Account Determination (100297) row, choose Configure.
6. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. To locate the activity in the tree view, search for the Automatic Account Determination activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Area | For the displayed row, make the following entries and choose Step 2:Area: ControllingSubarea: Cost Center AccountingProcess: Assign Intercompany Margin Accounts |  |  |
| 2 | Select Parameters | Make the following entry and choose Step 3:Chart of Accounts: YCOA |  |  |
| 3 | Maintain Account Determination | Add an account that is relevant for ICO margin for activity allocation G/L.Note Default content is delivered with margin account 97777700 - ICO Margin. You can use this as a reference to create your own margin account, if required (with G/L account P-Primary Cost and Revenue). |  |  |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Manage Cost Rates - Services](#unique_8) [page ] 7 | Cost Accountant - Overhead | Manage Cost Rates - Services (F3161) | Cost rates are maintained for services. |
| [Manage Cost Rates - Plan](#unique_9) [page ] 10 | Cost Accountant - Overhead | Manage Cost Rates - Plan (F3162) | Cost rates are maintained for plan. |
| [Manage Cost Rates - Actual](#unique_10) [page ] 11 | Cost Accountant - Overhead | Manage Cost Rates - Actual (F3422) | Cost rates are maintained for actuals. |

## Test Procedures

### Manage Cost Rates - Services

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Use this app to enter cost rates based on a variety of criteria. The cost rates are used in activity allocations to the following receiver objects via time recording or direct activity allocation:

- Cost centers
- Projects WBS elements
- Service orders

This app enables you to define cost rates for service cost levels and specific employees, so it is useful for professional services providers. However, it can also be used by manufacturing companies if there is a need for cost rates for service cost levels and employees.

The following fields are available for the price maintenance:

- Company Code (providing) always filled, thus not relevant for access sequence
- Company to be billed (receiving)
- ICO price (flag)
- Cost center (providing)
- Activity type (providing)
- Service cost level (providing)
- Personnel number (providing)
- Work item (New) (receiving)
- WBS element (receiving)

The ordering of the list shows the keys with the highest priority at the end of the list (WBS element).

The following rules are checked when updating the price table.

- Sending Company Code is required
- One or more of the following fields must be filled: Activity Type, Service Cost Level or Personnel Number (only cost center is not supported)
- The Personnel Number and Cost Center fields exclude each other as key fields for one price. Either the person has a specific cost rate or the average rate of the cost center is valid.
- The Personnel Number and Service Cost Level fields exclude each other as key fields for one price. Either the person has a specific cost rate or the average one of the service cost level is valid.
- Cost center and service cost level are an allowed key combination
- Cost center categories as defined in the activity type controls the allowed combinations of cost center and activity type.
- If an intracompany cost rate is entered, the receiving company shall be left blank
- WBS-specific cost rates can be used for cross- and intra-company activity allocations. If a receiving company and a WBS element are entered, the system checks if the WBS element is assigned to the receiving company (the system does not automatically derive the receiving company from the WBS element as this can lead to issues with migrated cost rates).
- Check and set the ICO flag
    - If the Receiving Company Code is empty, use the ICO flag from user input
    - If the Receiving Company Code does not equal the Sending Company Code, set the ICO flag to true
    - Otherwise, set the ICO Flag to false

| Cost Center | Activity Type | Service Cost Level | Personnel Number (Employee) | Work Item (Receiving) | WBS+Element (Receiving) | Company Code to be Billed (Receiving) | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sender | Receiver |  |  |  |  |  |  |
|  | X |  |  |  |  |  | At least one field (Activity Type, Service Cost Level, Personnel Number) must be filled |
|  |  | X |  |  |  |  |  |
| NEVER |  | NEVER | X |  |  |  |  |
| NEVER | X | NEVER | X |  |  |  | pers.no. w/o CCtr., w/o service cost level |
| X | X |  |  |  |  |  | CCtr. + act.type |
| X |  | X |  |  |  |  | CCtr. + service cost level |
| X | X | X |  |  |  |  | CCtr. + act.type + service cost level |
|  | X | X |  |  |  |  | act.type + service cost level |
|  | X |  |  | (X) | (X) |  | WBS or work item can be filled |
|  |  | X |  | (X) | (X) |  |  |
| NEVER |  | NEVER | X | (X) | (X) |  |  |
| NEVER | X | NEVER | X | (X) | (X) |  |  |
| X | X |  |  | (X) | (X) |  |  |
| X |  | X |  | (X) | (X) |  |  |
| X | X | X |  | (X) | (X) |  |  |
|  | X | X |  | (X) | (X) |  |  |
|  | X |  |  | (X) | (X) | X | ICO rates |
|  |  | X |  | (X) | (X) | X |  |
| NEVER |  | NEVER | X | (X) | (X) | X |  |
| NEVER | X | NEVER | X | (X) | (X) | X |  |
| X | X |  |  | (X) | (X) | X |  |
| X |  | X |  | (X) | (X) | X |  |
| X | X | X |  | (X) | (X) | X |  |
|  | X | X |  | (X) | (X) | X |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Rates - Services (F3161). | The Manage Cost Rates - Services screen displays. |  |
| 3 | Company Code | Make the following entry and choose Add:Company Code: <company code> |  |  |
| 4 | Maintain Service Cost Rates | Make the following entries and choose Save:Receiving Company: <leave blank>Note This field should only be used in the case of intercompany cost rates, else leave blank.Cost Center: <cost center>Activity Type: <activity type>WBS Element: <this is an optional field>From Fiscal Year: <current year>From Period: <current period>Rate: 100Note This rate is used for posting to all ledgers.Currency: <currency>Per: 1Activity Unit: H | Cost rates are created. |  |

### Manage Cost Rates - Plan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This activity is used to plan cost rates for cost center activities in a manufacturing environment. The rates are used in:

- Activity allocations to production orders and maintenance orders
- Material costing

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Rates - Plan (F3162). | The Manage Cost Rates - Plan screen displays. |  |
| 3 | Add | Choose Add. |  |  |
| 4 | Maintain Plan Cost Rates | Make the following entries and choose Save:Cost Center: <cost center>Activity Type: <activity type>From Fiscal Year: <current year>From Period: <current period>Currency: <currency>Fixed Rate: <amount>Variable Rate: <amount>Note This rate is used for posting to all ledgers. | Cost rates are maintained for plan. |  |

### Manage Cost Rates - Actual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This activity is used to enter actual cost rates for cost center activities used in actual costing. Actual cost rates can be maintained by ledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Rates - Actual (F3422). | The Manage Cost Rates - Actual screen displays. |  |
| 3 | Add | Choose Add. |  |  |
| 4 | Maintain Actual Cost Rates | Make the following entries and choose Save:Cost Center: <cost center>Activity Type: <activity type>Ledger: <for example, 0L or your lead ledger>NoteIf you use actual cost rate calculation, the system calculates actual cost rates per ledger. If you want to see or correct automatically calculated cost rates, you have to enter a ledger. Actual cost rates with ledger field blank are used for postings to all ledgers. If ledger-specific actual cost rates exist, the system uses the ledger-specific rates.To view the ledger column, adapt the settings in the cost rate list and select ledger.From Fiscal Year: <current year>From Period: <current period>Currency: <currency>Fixed Rate: <amount>Variable Rate: <amount>Note This rate is used for posting to all ledgers. | Cost rates are maintained for actuals. |  |

## Analytics

### Display Cost Rates

Purpose

This report allows you to select and view the various cost rate types.

Prerequisite

Cost rates must already exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Display Cost Rates (F5150). | The Display Cost Rates screen displays. |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Ledger: <keep this field empty>Note Leaving the selection field blank would display rates that are the same and apply to all ledgers (example plan rate). Specifying a ledger in the selection limits the cost rate display to the rates only maintained for the specific ledger(s) selected and applicable only to actual rates.Cost Center: <for example, 10101101>Activity Type: <for example, 11>From Fiscal Year Period: <current period>To Fiscal Year Period: <current period> |  |  |

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
- related-to :: [[06-management-accounting/co-mds-3kw-355]]
- related-to :: [[06-management-accounting/co-mds-3kw-357]]
- related-to :: [[06-management-accounting/crear-tasas-de-coste-co-mds-3kw-354]]
- related-to :: [[06-management-accounting/script-de-dados-mestre-criar-taxas-de-custo-co-mds-3kw-356]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3KW_S4CLD2608_Master_Data_EN_XX.docx` — full document · extracted with `mammoth` · 21,316 chars in the whole document
