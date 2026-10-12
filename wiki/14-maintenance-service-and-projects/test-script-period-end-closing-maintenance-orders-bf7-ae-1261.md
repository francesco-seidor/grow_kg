---
id: 14-maintenance-service-and-projects/test-script-period-end-closing-maintenance-orders-bf7-ae-1261
title: "Test Script: Period-End Closing – Maintenance Orders (BF7_AE) (BF7_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud 2608 test script (BF7, AE) for settling, closing and analyzing maintenance service orders YA01-YA05 at period end."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/maintenance-order-period-end-closing]
aliases: [BF7_S4CLD2608_BPD_EN_AE]
keywords: [Period-End Closing for Maintenance Orders, period-end closing, maintenance orders, order settlement, settlement profiles, closing service orders, maintenance order analysis, controlling area settings, cost accounting periods, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BF7_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1261
topic: 14-maintenance-service-and-projects/maintenance-order-period-end-closing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Period-End Closing – Maintenance Orders (BF7_AE) (BF7_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BF7_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Period-End Closing for Maintenance Orders** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 02-08-26 |
| --- | --- |
|  | Period-End Closing – Maintenance Orders (BF7_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc237361485)

[2 Prerequisites 3](#_Toc237361486)

[2.1 System Access 3](#_Toc237361487)

[2.2 Roles 3](#_Toc237361488)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc237361489)

[2.4 Business Conditions 5](#_Toc237361490)

[2.5 Preliminary Steps 5](#_Toc237361491)

[2.5.1 User Settings - Set Controlling Area 5](#_Toc237361492)

[2.5.2 Update Settlement Profile 6](#_Toc237361493)

[2.5.3 Order Type to Settlement Profile Mapping 7](#_Toc237361494)

[2.5.4 Open Cost Accounting Period 7](#_Toc237361495)

[3 Overview Table 9](#_Toc237361496)

[4 Test Procedures 10](#_Toc237361497)

[4.1 Run Settlement for Service Order 10](#_Toc237361498)

[4.2 Close Completed Service Order 12](#_Toc237361499)

[4.3 Analyze Order 12](#_Toc237361500)

## Purpose

Overview

This scope item supports activities required for Reactive Maintenance (4HH) and Proactive Maintenance (4HI) scope items. Once the cost is recorded in order types YA01 (Reactive Maintenance), YA02 (Proactive Maintenance), YA03 (Improvement Maintenance), YA04 (Operational Maintenance), and YA05 (Overhead Maintenance), this scope item is executed as a follow-up for settlement, closing, and reporting.

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
| Maintenance Planner | SAP_BR_MAINTENANCE_PLANNER | Maintenance Planning | SAP_BR_MAINTENANCE_PLANNER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company.

The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| OPERATING CONCERN | A000 |  |  |
| CONTROLLING AREA | A000 |  |  |
| COMPANY CODE | 3310 |  |  |
| G/L ACCOUNT |  |  | G/L account for posting |
| COST CENTER | 33101301 |  | Manufacturing 1 (AE) |
| SERVICE ORDER TYPE |  | YA01: Reactive MaintenanceYA02: Proactive MaintenanceYA03: Improvement MaintenanceYA04: Operational MaintenanceYA05: Overhead Maintenance |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| 3KW | Create CO Cost Rates - MDS |

### Business Conditions

Before this scope item can be tested, the following business condition must be met.

| Scope Items | Business Condition |
| --- | --- |
| 4HH - Reactive Maintenance or4HI - Proactive Maintenance or4VT - Improvement Maintenance or4WM - Operational and Overhead Maintenance | At least one of these scripts must be executed for this test. |

### Preliminary Steps

#### User Settings - Set Controlling Area

Purpose

The controlling area must be set before you carry out the first steps in controlling.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Choose User Preferences | Choose the user icon on the top right corner of the screen, and choose Settings.Choose Default Values. | The Default Values dialog box displays. |  |
| 3 | Enter Data | On the CO Area field,enter the following value: A000.Choose Save. | Controlling area A000 is set for your user. |  |

#### Update Settlement Profile

Purpose

This activity lets you update settlement profile.

|  |
| --- |
| Note The following settlement profiles are not editable as they are for specific scope: YB00AI-Settlement asset under construction (for deprecated internal order), YBMF99-REWORK-VIA NOTIFICATION, YBMFP1-PP Valuated to COPA, and YNS-No Settlement. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Create Settlement Profile (105768).
6. For the displayed row, choose Details (>).
7. For the Create Settlement Profile: Change row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Create Settlement Profile activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Allowed Settlement Profile for Edit | Select the settlement profile and double-click on the Dialog Structure pane to view the detail.You can now update the predelivered settlement profile based on your requirements. | Updates the settlement profile.Note Deletion of predelivered settlement profile is not allowed. Only update is possible. |  |

#### Order Type to Settlement Profile Mapping

This section describes the assignment design flow of each order type to its respective settlement/allocation.

|  |
| --- |
| Note You can settle all settlements by ledger. For more information, see SAP Note [3066714](https://me.sap.com/notes/3066714). |

| Order Type | Settlement Profile | Allocation Structure | Line ID | Cost Element Group of Line ID | Receivers |
| --- | --- | --- | --- | --- | --- |
| Order types YA01, YA02, YA03, YA04 and YA05 | YEAM02-EAM -Reactive-CTR, YEAM04-EAM-Proactive-CTR, YEAM03-EAM-Improvement-WBS, YEAM05-EAM-Operational-CTR and YEAM06-EAM-Overhead-CTR respectively | YE | 10 - Personnel Cost | YBMF_001 | CTR and WBS to secondary G/L 92105100-Personnel costs |
| Order types YA01, YA02, YA03, YA04 and YA05 | YEAM02-EAM -Reactive-CTR, YEAM04-EAM-Proactive-CTR, YEAM03-EAM-Improvement-WBS, YEAM05-EAM-Operational-CTR and YEAM06-EAM-Overhead-CTR respectively | YE | 20 -Spare/Service/Ext material | YBMF_002 | CTR and WBS to secondary G/L 92105200-Sp/Serv/Ext Mat con |
| Order types YA01, YA02, YA03, YA04 and YA05 | YEAM02-EAM -Reactive-CTR, YEAM04-EAM-Proactive-CTR, YEAM03-EAM-Improvement-WBS, YEAM05-EAM-Operational-CTR and YEAM06-EAM-Overhead-CTR respectively | YE | 30 - Other Costs | YBMF_003 | CTR and WBS to secondary G/L 92105300- Other Costs |
| Order types YA01, YA02, YA03, YA04 and YA05 | YEAM02-EAM -Reactive-CTR, YEAM04-EAM-Proactive-CTR, YEAM03-EAM-Improvement-WBS, YEAM05-EAM-Operational-CTR and YEAM06-EAM-Overhead-CTR respectively | YE | 40 - Secondary Costs | YBMF_004 | CTR and WBS to secondary G/L 92105400- Secondary costs |

|  |
| --- |
| Note You can update the cost element grouping for any missing G/L via the Manage Cost Element Groups app and don't need to update the allocation structure. Updating the predelivered cost element groups is sufficient to avoid any errors. You can use the Edit Cost Element Groups app for updates to cost element assignments. |

#### Open Cost Accounting Period

Use

The posting period for cost accounting must be open.

Prerequisites

Check and ensure that the cost accounting period is open for the period you are working.

|  |
| --- |
| Note For more details on this step, see the Manage Posting Periods step in Accounting and Financial Close (J58) script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Posting Periods - Cost Accounting (F4684). | The Manage Posting Periods - Cost Accounting view displays. |  |
| 3 | Check/Open Period | Make the following entries and choose Go:Company Code: 3310Fiscal Year: <current fiscal year> | Controlling posting period is now open. |  |

## Overview Table

This scope item consists of several process steps, reports, and items provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Run Settlement for Service Order](#unique_13) [page ] 10 | Cost Accountant - Overhead | Schedule Overhead Accounting Jobs (F3767) | Costs are settled to cost center (overhead cost orders only). |
| [Close Completed Service Order](#unique_14) [page ] 12 | Cost Accountant - Overhead | Set Status to Closed - Orders - Collective (CO99) | The completed service orders are closed. |
| [Analyze Order](#unique_15) [page ] 12 | Maintenance Planner | Maintenance Order Costs - Plan / Actual (F4603) | Actual figures for orders can be displayed in the reporting with different dimensions for navigation. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Run Settlement for Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the settlement. Service orders that have a maintenance order type are settled to the responsible cost center.

|  |
| --- |
| Note For the assignment design flow of each order type to its respective settlement/allocation, see the [Order Type to Settlement Profile Mapping](#unique_10) [page ] 7 section. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Overhead Accounting Jobs (F3767). | The Application Jobs screen showing the history of application jobs displays. |  |
| 3 | Create Settlement Job | To define a new job, choose Create. | The New Job screen displays. |  |
| 4 | Job Template | In the Job Template field, choose the input help. In the Template Selection dialog box, clear the search field and select Actual Settlement: Orders (SAP). | The job template defaults as Actual Settlement Orders (SAP). |  |
| 5 | Job Parameters | In the Scheduling Options section, make the following entry:Start Immediately: SelectIn the Parameters section, enter the following:Settlement Period: <Current period>Fiscal Year: <Current year>Processing Type: AutomaticLedger: <0L or your lead ledger)>Note Settlement with Lead Ledger ensures all orders (old and new) are settled. For orders created before the 2105 release, the app settled the same values to all ledgers as the older order settlement rule wasn't configured for settlement with parallel ledger. For new orders with parallel settlement rule, the lead ledger ONLY settles to the lead ledger; you would require additional jobs for ledgers 2L or 3L.For orders created after the 2105 release, create settlement job for any additional ledgers 2L or 3L. Otherwise, balances remain in the Ledger and aren't specifically settled. Each ledger must be settled separately.Under Orders, enter the following:Order Type: <Use the input help to select types YA01, YA02, YA03, YA04 and YA05>Released: SelectTechnically Completed: SelectUnder Processing options, make the following entries:Actual Settlement: SelectTest Run: Deselect | Note The order type depends on maintenance scope. |  |
| 6 | Schedule | Choose Schedule. | A delivery creation job is scheduled. The Application Jobs view is displayed. |  |
| 7 | Check Actual Cost Rate Calculation Job Log | After the status of the jobs changes to Finished, in the Log column, choose the Status symbol.Note To refresh the job list, choose Go. | The job log details display. |  |

|  |
| --- |
| Note To perform a single settlement, use the Run Settlement - Actual (F4568) app. |

### Close Completed Service Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you close the completed service orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Status to Closed - Orders - Collective (CO99). | The Collective Processing: Set Status "Closed" view displays |  |
| 3 | Enter Actual Data | Make the following entries:Plant: 3310Order Type: <Use the input help to select types YA01, YA02, YA03, YA04 and YA05>Test Run: <Deselected> |  |  |
| 4 | Execute | Choose Execute. |  |  |

### Analyze Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity allows you to view service orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Maintenance Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintenance Order Costs - Plan / Actual (F4603). | The Maintenance Order Costs view displays. |  |
| 3 | Enter Details | Enter the following details:Relative Date Function: Previous 30 daysG/L Account Hierarchy: YPS2Ledger: 0LCompany Code: 3310Equipment: 233100091Choose Go.Note If data is not displayed, it can be because the Relative Date Function field is set to a past date. | Based on the values, different types of maintenance costs are analyzed and reviewed. |  |

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
- see-also :: [[14-maintenance-service-and-projects/reactive-maintenance-4hh-ae-test-script-sap-s-4hana-cloud-public-editi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BF7_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 21,211 chars in the whole document
