---
id: 06-management-accounting/test-script-event-based-revenue-recognition-subscription-billing-ifrs
title: "Test Script: Event-Based Revenue Recognition – Subscription Billing – IFRS (5DR_AE) (5DR_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 5DR: event-based revenue recognition of subscription provider contracts under IFRS, with prerequisites and steps."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/event-based-revenue-recognition-subscriptions]
aliases: [5DR_S4CLD2608_BPD_EN_AE]
keywords: [Event-Based Revenue Recognition for Subscriptions, event-based revenue recognition, provider contracts, subscription billing, recognition key derivation, period-end revenue recognition, revenue recognition issues, revenue recognition reversal, product and service margins, report relevancy]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5DR_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1076
topic: 06-management-accounting/event-based-revenue-recognition-subscriptions
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Event-Based Revenue Recognition – Subscription Billing – IFRS (5DR_AE) (5DR_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5DR_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Event-Based Revenue Recognition for Subscriptions** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Event-Based Revenue Recognition – Subscription Billing – IFRS (5DR_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232856372)

[2 Prerequisites 4](#_Toc232856373)

[2.1 System Access 4](#_Toc232856374)

[2.2 Roles 4](#_Toc232856375)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232856376)

[2.4 Business Conditions 5](#_Toc232856377)

[2.5 Preliminary Steps 5](#_Toc232856378)

[2.5.1 Set Report Relevancy 5](#_Toc232856379)

[2.5.2 Replicate Runtime Hierarchy 6](#_Toc232856380)

[2.5.3 Check and Update Derivation of Recognition Key for Provider Contract Item 7](#_Toc232856381)

[2.5.4 Maintain Settings for Event-Based Revenue Recognition 9](#_Toc232856382)

[3 Overview Table 11](#_Toc232856383)

[4 Test Procedures 12](#_Toc232856384)

[4.1 Monitor Revenue Recognition (Event-Based): Provider Contracts 12](#_Toc232856385)

[4.2 Manage Real-Time Revenue Recognition Issues 13](#_Toc232856386)

[4.3 Run Revenue Recognition: Provider Contracts (Period-End Activity) 14](#_Toc232856387)

[4.4 Manage Revenue Recognition Issues – Provider Contracts 15](#_Toc232856388)

[4.5 Review Product and Service Margins 16](#_Toc232856389)

[4.6 Optional: Revenue Recognition Reversal 17](#_Toc232856390)

[5 Appendix 18](#_Toc232856391)

[5.1 Reverse Month-End Revenue Recognition Postings 18](#_Toc232856392)

## Purpose

Overview

Subscriptions created in SAP Subscription Billing are stored as provider contract items in SAP S/4HANA Cloud Public Edition. Event-Based Revenue Recognition lets you manage revenue recognition for provider contracts using group ledger IFRS functionality. For a provider contract item, revenue is recognized over time, based on the billing plan associated with the provider contract item. Revenue posted because of the invoicing document in Sales Billing is deferred. Manual adjustments to revenue are possible. If necessary, period-end closing corrects real-time revenue recognition postings.

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
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Controlling area | A000 | Controlling Area A000 |  |
| Company code | 3310 | Company Code 3310 |  |
| Service Organization | 3310 | Service Org 3310 |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met. These steps below provide the source of the revenue recognition.

| Scope Item | Business Condition |
| --- | --- |
| 57Z - Subscription Management with Sales Billing | Subscriptions are created via API or as part of an SAP S/4HANA Cloud Public Edition solution order in SAP Subscription Billing. |
| 1GA - Accounting and Financial Close – Group Ledger IFRS | You must select and activate this scope item. |
| 5DQ - Event-Based Revenue Recognition – Subscription Billing | You must select and activate this scope item. |

### Preliminary Steps

#### Set Report Relevancy

Purpose

Report relevancy must be done when you execute any reports for the first time. If you make a subsequent change in cost center, profit center, or G/L hierarchy, perform this step again to get the latest information.

Also, you must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally, this would be created as a periodic job that would run in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Report Relevancy - Set-Based Hierarchies (F5295). | The Set Report Relevancy for Set-Based Hierarchies screen displays. |  |
| 3 | Enter Header Data | Make the following entries and choose Go:Set Class: For example,0101, for the cost center groupOrganizational Unit: A000Set Name: A000Include Subnodes: Yes |  |  |
| 4 | Mark as Report Relevant | In the Set Report Relevancy section, select the row and choose Edit. In the dialog box, make the following entries:Report Relevant: Yes |  |  |
| 5 | Save | Choose Save.Note If you are using the optional procedure Commitment Management and Cost Center Budgeting, repeat steps 1-5 with the following entries instead:Set Class: 0102Organizational Unit: YCOASet Name: YBA000_CEInclude Subnodes: <Select> | Set updated message displays. |  |

#### Replicate Runtime Hierarchy

Purpose

You must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally, this would be created as a periodic job that would run in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Overhead Accounting Jobs (F3767). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job: Replicate Runtime Hierarchy (SAP) view displays. |  |
| 4 | Header Data for Hierarchy ID 0101/A000/A000 | In the header area, make the following entries and choose Schedule:Job Template: Replicate Runtime Hierarchy (SAP)Job Name: <Enter a text>Choose the Step 2 button.Start Immediately: SelectChoose the Step 3 button.In the Create Hierarchy area, make the following entry:Hierarchy ID: 0101/A000/A000Note If you are using the optional procedure Commitment Management and Cost Center Budgeting, follow steps 1-4, but make the following entries instead:Job Template: Manually Replicate Runtime HierarchyHierarchy ID: 0102/YCOA/YBA000_CE |  |  |
| 5 | Hierarchy ID YPS2 | Repeat the above steps using hierarchy ID YPS2. |  |  |

#### Check and Update Derivation of Recognition Key for Provider Contract Item

Purpose

In the activity, you can check and update derivation of recognition key for provider contracts.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Profitability Analysis

1. For the row with Item Name of Revenue Recognition, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Derivation of Recognition Key for Provider Contracts (105138) row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Derivation of Recognition Key for Provider Contracts activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add/Change Entry for Required Charge Type | Choose the New Entries button and make the following entries:Company Code: <enter your company code>Contract Category: <Defaulted to Sales Billing Provider Contract>Charge Type: < One-Time or Recurring>Material: <for example, *>Note Keep material as * if the same RA key is valid for all the materials.Recognition Key: <PPCA for time-based revenue recognition, and PPCN for no revenue recongition>Save the entries. | The following contract category and charge type are supported in event-based revenue recognition, and based on your business requirements, you must ensure that the derivation is set for all used combinations.Contract Category: Sales Billing Provider ContractCharge Type: 01 One-Time and 02-Recurring.Note Provider Contract RA key is represented by RecKeyArea 600.Note The recognition key NONREV - Universal No Rev Rec is available for use across the RA key area. This generic non-revenue recognition key represents method 2 for all scenarios supported by Event-Based Revenue Recognition.Note The recognition key PPCF - Provider Contract with Financing Component is allowed only when used with Universal Revenue Recognition and requires the prerequisite scopes Contract-Based Revenue Recognition – IFRS (3KK) and Contract-Based Revenue Recognition – US GAAP (3VS). |  |

#### Maintain Settings for Event-Based Revenue Recognition

Purpose

In the activity, you can check and update configuration of recognition key for project-based sales documents.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Profitability Analysis

1. For the row with Item Name of Revenue Recognition, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Maintain Settings for Event-Based Revenue Recognition row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration (CBC).
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Maintain Settings for Event-Based Revenue Recognition activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add/Change Entry for Recognition Key | In this configuration step, you can add G/L to predelivered sources based on your business needs.You can also update the assignment rule with the necessary G/L.For more information, see the notes below. |  |  |

|  |
| --- |
| Note The assignment rule PPCF - Provider Contract with Financing Component is allowed only when used with Universal Revenue Recognition and requires the prerequisite scopes Contract-Based Revenue Recognition – IFRS (3KK) and Contract-Based Revenue Recognition – US GAAP (3VS).Table 1:Settings for PPC: Periodic Provider Contract and PPCF: Provider Contract Revenue with Financing ComponentDetailsUsage 110Interest Income in Finance AgreementRequired ActionMap a separate G/L account to distinctly capture the Interest Income portion, differentiating it from finance income (Usage 100) within total revenue.HintYou can copy G/L accounts 44401100, 13811100, and 13711100 to create a dedicated account for interest income. Make sure you update FSV YPS2 with the additional G/L accounts you create so that reporting is complete.Usage 111Price Allocation DifferenceFunctionCaptures the revenue allocation difference between interest and finance revenue based on the allocation ratio.HintReplicate G/L accounts 44401100, 13811100, and 13711100 to create a dedicated account for interest income. Make sure you update FSV YPS2 with the additional G/L accounts you create so that reporting is complete. |

## Overview Table

The scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | App Name | Expected Results |
| --- | --- | --- | --- |
| [Monitor Revenue Recognition (Event-Based): Provider Contracts](#unique_12) [page ] 12 | Cost Accountant - Sales | Event-Based Revenue Recognition - Provider Contracts (F5406) | Contract documents are reviewed. |
| [Manage Real-Time Revenue Recognition Issues](#unique_13) [page ] 13 | Cost Accountant - Sales | Manage Real-Time Revenue Recognition Issues (F4101) | Issue such as cost/revenue posting with no real time posting are reviewed. |
| [Run Revenue Recognition: Provider Contracts (Period-End Activity)](#unique_14) [page ] 14 | Cost Accountant - Sales | Run Revenue Recognition - Provider Contracts (F5405) | Values for real-time revenue for service contracts are posted. |
| [Manage Revenue Recognition Issues – Provider Contracts](#unique_15) [page ] 15 | Cost Accountant - Sales | Manage Revenue Recognition Issues - Provider Contracts (F5407) | Revenue recognition posting issues are reviewed and corrected. |
| [Review Product and Service Margins](#unique_16) [page ] 16 | Cost Accountant - Sales | Product and Service Margins (FIS_FPM_OVP_PROSRVMGN (FIS_FPM_OVP_PROSRVMGN)). | You can view actual figures based on your selection criteria. |
| [Optional: Revenue Recognition Reversal](#unique_17) [page ] 17 | Cost Accountant - Sales | Revenue Recognition Reversal (F4869) | The document is reversed. |

## Test Procedures

### Monitor Revenue Recognition (Event-Based): Provider Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The provider contract revenue can be reviewed.

|  |
| --- |
| Note RA key assigned to provider contract for charge type recurring is PPCA-Provider Contracts 365 Days Calendar Yr-No cost deferred. So to view any data in this app, there must either be billing done for the contract and that would post deferred revenue, or execute the Run Revenue Recognition: Provider Contracts (Period-End Activity) step to accrue revenue if no billing is done. For charge type One time with RA key PPCN, there is no rev recognition. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Event-Based Revenue Recognition - Provider Contracts (F5406). | The Event Based Rev. Rec.-Provider Contract view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries :Company Code: 3310Provider Contract: <Created in scope items Solution Order Management (4GT) and Subscription Management with Sales Billing (57Z)>Contract Item: <leave this field blank>Recognition Key: PPCA |  |  |
| 4 | Execute | Choose Go. |  |  |

### Manage Real-Time Revenue Recognition Issues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

During cost or revenue posting on the cost object, errors that stop real time revenue postings can occur. This activity allows you to review these posting entries where no corresponding real time revenue recognition posting exists and make the necessary corrections. All errors must be addressed prior to the month end revenue recognition month end process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. |  |  |
| 2 | Access the App | Open Manage Real-Time Revenue Recognition Issues (F4101). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:To Fiscal Period/Year: <mm.yyyy>Company Code: 3310 | No data found indicates that there are no issues. If issues are shown, review and process corrections.Tip To download the issue list, make your filter selections and select Show Error Summary. From the list, you can choose the Download button. |  |

### Run Revenue Recognition: Provider Contracts (Period-End Activity)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the event-based revenue recognition for provider contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Revenue Recognition - Provider Contracts (F5405). | The Application Jobs view displays. |  |
| 3 | New Job | Choose the Create button. | The New Job view displays. |  |
| 4 | Enter Selection Criteria | Make the following entries and choose the Schedule button:Job Template: Run Revenue Recognition – Provider ContractsJob Name: <Enter a description or leave the default description>Choose Step 2.Start Immediately: <checked>Choose Step 3.Fixed Period: <mm/yyyy>ORDynamic Period: <use the dropdown to select, for example, Current Fiscal Period>Company Code: 3310Ledger: 2LProvider Contract: <Created in scope items Solution Order Management (4GT) and Subscription Management with Sales Billing (57Z)>Contract Item: <leave this field blank>Sales Organization: 3310Division: <leave this field blank>Distribution Channel: <leave this field blank>Simulation: <deselect the checkbox> | The new job is executed. |  |

### Manage Revenue Recognition Issues – Provider Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Errors in the revenue recognition must be corrected.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. |  |  |
| 2 | Access the App | Open Manage Revenue Recognition Issues - Provider Contracts (F5407) . |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Reprocess to correct and/or skip errors.Fiscal Year Period: <MM/YYYY>Company Code: 3310Ledger: 2LProvider Contract: <Created in scope items Solution Order Management (4GT) and Subscription Management with Sales Billing (57Z)>Provider Contract Item: <leave this field blank> | No data found indicates that there are no issues. If issues are shown, review and process corrections.Tip To download the issue list, make your filter selections and select Show Error Summary. From the list, you can choose the Download button. |  |

### Review Product and Service Margins

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the provider contract actual data report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Product and Service Margins (FIS_FPM_OVP_PROSRVMGN (FIS_FPM_OVP_PROSRVMGN)). | The Product and Service Margins view displays. |  |
| 3 | Enter Report Criteria | Make the following entries and choose Go:Financial Statement version: YPS2Ledger Fiscal Year: <enter a fiscal year>Ledger: 2LProvider Contract: <Created in scope items Solution Order Management (4GT) and Subscription Management with Sales Billing (57Z)>Provider Contract Item: <leave this field blank> | The actual figures for product and service margins display. |  |

### Optional: Revenue Recognition Reversal

You could reverse revenue recognition if you made an error. For information on revenue recognition reversal, see the [Reverse Month-End Revenue Recognition Postings](#unique_19) step in the Appendix section.

## Appendix

### Reverse Month-End Revenue Recognition Postings

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Occasionally, you may be required to reverse revenue recognition posts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Revenue Recognition (F4869). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job: Reverse Revenue Recognition view displays. |  |
| 4 | Enter Selection Criteria | In the Template Selection section, make the following entries:Job Template: Reverse Revenue RecognitionJob Name: Reverse Revenue RecognitionChoose Step 2. | The Scheduling Options view display. |  |
| 5 | Scheduling Options | Select Start Immediately checkbox and choose Step 3. | The Parameters view display. |  |
| 6 | Parameters | Make the following entries:Posting Date: <Enter a desired date>Note This must be a month-end date. Otherwise, no selection will be returned.Company Code: 3310Ledger: <enter a ledger>Journal Entry: <Enter the document you want to reverse> | The figures for projects display. |  |
| 7 | Schedule Job | Choose the Schedule button. | The document is reversed. |  |

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
- related-to :: [[06-management-accounting/event-based-revenue-recognition-subscription-billing-5dq-ae-test-scrip]]
- related-to :: [[06-management-accounting/event-based-revenue-recognition-subscription-billing-us-gaap-5ds-ae-te]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5DR_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 29,571 chars in the whole document
