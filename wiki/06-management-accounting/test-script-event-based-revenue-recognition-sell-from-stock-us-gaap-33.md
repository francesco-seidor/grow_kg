---
id: 06-management-accounting/test-script-event-based-revenue-recognition-sell-from-stock-us-gaap-33
title: "Test Script: Event-Based Revenue Recognition – Sell from Stock – US GAAP (33J_AE) (33J_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for event-based revenue recognition, sell from stock, US GAAP (33J_AE): prerequisites, config and test steps."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/event-based-revenue-recognition-sell-from-stock]
aliases: [33J_S4CLD2608_BPD_EN_AE]
keywords: [Event-Based Revenue Recognition for Sell from Stock, event-based revenue recognition, sell from stock, recognition key derivation, revenue recognition settings, test procedures, revenue recognition issues, business roles, business conditions, report relevancy]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33J_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-900
topic: 06-management-accounting/event-based-revenue-recognition-sell-from-stock
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Event-Based Revenue Recognition – Sell from Stock – US GAAP (33J_AE) (33J_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33J_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Event-Based Revenue Recognition for Sell from Stock** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Event-Based Revenue Recognition – Sell from Stock – US GAAP (33J_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851487)

[2 Prerequisites 4](#_Toc232851488)

[2.1 System Access 4](#_Toc232851489)

[2.2 Roles 4](#_Toc232851490)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232851491)

[2.4 Business Conditions 5](#_Toc232851492)

[2.5 Preliminary Steps 6](#_Toc232851493)

[2.5.1 Set Report Relevancy 6](#_Toc232851494)

[2.5.2 Replicate Runtime Hierarchy 7](#_Toc232851495)

[2.5.3 Maintain Settings for Event-Based Revenue Recognition 8](#_Toc232851496)

[2.5.4 Check and Update Derivation of Recognition Key for Sell from Stock 9](#_Toc232851497)

[3 Overview Table 12](#_Toc232851498)

[4 Test Procedures 13](#_Toc232851499)

[4.1 Monitor Revenue Recognition (Event-Based): Sales Order 13](#_Toc232851500)

[4.2 Review Allocated Revenue (optional) 14](#_Toc232851501)

[4.3 Manage Real-Time Revenue Recognition Issues 15](#_Toc232851502)

[4.4 Run Revenue Recognition: Sales Orders 15](#_Toc232851503)

[4.5 Manage Revenue Recognition Issues – Sales Orders 17](#_Toc232851504)

[4.6 Optional: Revenue Recognition Reversal 17](#_Toc232851505)

[4.7 Sales Order Actual Data Reporting 18](#_Toc232851506)

[5 Appendix 19](#_Toc232851507)

[5.1 Reverse Month-End Revenue Recognition Postings 19](#_Toc232851508)

## Purpose

Overview

Event-based Revenue Recognition calculates and posts real-time revenue and cost adjustment for sales orders, using US GAAP ledger functionality. When a goods issue is posted for sale from stock, revenue is calculated based on quantity, accrued revenue is posted, and costs are matched with revenues.

Processes that do not write a source document do not result in real-time revenue recognition postings. For example, changes of plan data do not directly result in revenue recognition postings. Period-end closing postings (periodic revenue recognition) correct the event-based revenue postings. After period-end closing, the posted values are fully correct and separate settlement is no longer required.

Event-based Revenue Recognition also supports bundling, revenue calculation, and posting in the context of ASC 606. For more information, see SAP Note 2524569.

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
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Controlling area | A000 | Controlling AreaA000 |  |
| Company code | 3310 | Company Code3310 |  |
| Sales Organization | 3310 | Sales Org3310 |  |

### Business Conditions

Event-based revenue recognition is valid for the following scenarios:

- BD3 - Sales Processing using Third-Party with Shipping Notification
- BD9 - Sell from Stock
- BDA - Free of Charge Delivery
- BDH - Sales Order Entry with One-Time Customer
- BDK - Sales Processing Using Third-Party Without Shipping Notification
- BDW - Returnables Processing
- BKZ - Sales Order Processing with Invoice List and Collective Billing
- BKA - Free Goods Processing
- BKX - Sales Order Processing – SEPA Direct Debit Handling
- 1JW - Advanced Available-to-Promise Processing
- 1YT - Make-to-Order Production with Variant Configuration
- 4R6 - Sales Processing using Third-Party with Variant Configuration
- 31Q - Sales Order Processing for Sales Kits

Before this scope item can be tested, one of the following business conditions must be met:

| Scope Item | Business Condition |
| --- | --- |
| BD3 - Sales Processing using Third-Party with Shipping Notification orBD9 - Sell from Stock orBDH - Sales Order Entry with One-Time Customer orBDK - Sales Processing Using Third-Party Without Shipping Notification orBKA - Free Goods Processing orBKZ - Sales Order Processing with Invoice List and Collective Billing orBKX - Sales Order Processing – SEPA Direct Debit Handling or1JW - Advanced Available-to-Promise Processing or1YT - Make-to-Order Production with Variant Configuration or4R6 - Sales Processing using Third-Party with Variant Configuration or31Q - Sales Order Processing for Sales Kits | At least one of the revenue applicable scripts must be executed for this test. |
| 2VA - Accounting and Financial Close – Group Ledger US GAAP | You must select and activate this scope item. |
| 1K2 - Event-Based Revenue Recognition – Sell from Stock | You must select and activate this scope item. |

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
| Note CBC only: You can create your own revenue sources with names starting with Z and assign them to the provided assignment rules using customer sequence numbers that start with 1000. Additionally, you can configure the extra P&L and Balance Sheet accounts for revenue/cost adjustments and accrued/deferred revenue. Ensure that the custom source is only assigned to usage 100: Revenue for Revenue Recognition Processing. You must also add usage 400: Currency Result and usage 401: Currency Valuation to the custom source, as well as usage 103 if the default revenue source is assigned with these usages. |

|  |
| --- |
| Note CBC only: Avoid assigning the same G/L account to two source lines. When assigning a source to the assignment rule, the system ensures that no other source is already assigned that would derive the same G/L account. If this condition is met, the assignment is forbidden. During transaction processing, the assignment rule evaluates each source sequence sequentially, regardless of the source's nature (for example, revenue versus cost). Once a G/L account is determined, the process stops and proceeds with the identified source. |

#### Check and Update Derivation of Recognition Key for Sell from Stock

Purpose

In the activity, you can check and update derivation of recognition key for sell from stock.

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
3. For the Derivation of Recognition Key for Sell from Stock row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Derivation of Recognition Key for Sell from Stock activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add/Change Entry for Required Item Category | Choose the New Entries button and make the following entries:Company Code: <enter your company code>Item Category: <for example, CB1C and CB2C>Material : <for example, *>Note Keep material as * if the same RA key is valid for all the materials.Recognition Key: <for example, SFSEP>Save the entries. | The following item categories are supported in event-based revenue recognition and based on your sales scope activated and business requirements, you must ensure that the derivation is set for all used item categories:Table 1:Item Category SupportedSuggested RA Keys defaultsCB1, CB2,CB1C, CB2CSFSEPCBXN, TAQ,TAN, TANN, CBTC, FPHD and FBHDSFSCPHDSFSCCMNote Example item categories added in this step are only valid if you have activated the scope item Sales Processing using Third-Party with Variant Configuration (4R6) and want to use this scope item with Event-based Revenue Recognition.Note If you do not want to use the event-based revenue recognition functionality and the item category is added already by default content, you must keep the Recognition key field blank and not delete the default predelivered content. Deleting predelivered content would lead to errors later.Note We predeliver various RA keys such as SFS, SFSCCM, SFSEP, SFSN, SFSR and SFSSM. All recognition keys have different posting logic and you must review and implement the RA key that works for your business and update accordingly. For example, keys to use for third-party item categories such as CB1,CB2, CB1C, and CB2C are SFSCCM and SFSEP.Note The new key NONREV - Universal No Rev Rec is now available for use across the RA key area. This generic non-revenue recognition key represents method 2 for all scenarios supported by Event-Based Revenue Recognition. |  |

## Overview Table

This scope item consists of several process steps as provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | App Name | Expected Results |
| --- | --- | --- | --- |
| [Monitor Revenue Recognition (Event-Based): Sales Order](#unique_12) [page ] 13 | Cost Accountant - Sales | Event-Based Revenue Recognition - Sales Orders (F2441A) | Sales documents are reviewed. |
| [Review Allocated Revenue (optional)](#unique_13) [page ] 14 | Cost Accountant - Sales | Display Allocated Revenue (F3039) | Allocated revenue vs standalone revenue and transaction revenue is displayed. |
| [Manage Real-Time Revenue Recognition Issues](#unique_14) [page ] 15 | Cost Accountant - Sales | Manage Real-Time Revenue Recognition Issues (F4101) | Cost/revenue posting issues with no real time posting are reviewed. |
| [Run Revenue Recognition: Sales Orders](#unique_15) [page ] 15 | Cost Accountant - Sales | Run Revenue Recognition - Sales Orders (F4276). | Real time revenue for sales orders are posted. |
| [Manage Revenue Recognition Issues – Sales Orders](#unique_16) [page ] 17 | Cost Accountant - Sales | Manage Revenue Recognition Issues - Sales Orders (F4185) . | Revenue recognition posting issues are reviewed and corrected. |
| [Optional: Revenue Recognition Reversal](#unique_17) [page ] 17 | Cost Accountant - Sales | Revenue Recognition Reversal (F4869) | The document is reversed. |
| [Sales Order Actual Data Reporting](#unique_18) [page ] 18 | Cost Accountant - Sales | Sales Orders - Actuals (F1582A). | You can view actual figures based on your selection criteria. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Monitor Revenue Recognition (Event-Based): Sales Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Event-based Revenue Recognition calculates and posts real time revenue and cost adjustment for sales orders. Processes that do not write a prima nota don't result in any real-time revenue recognition postings. For example, changes of plan data do not directly result in revenue recognition postings. Period-end-closing postings (periodic revenue recognition) correct the event-based postings. After period-end-closing, posted values are updated and a separate settlement is no longer required.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Event-Based Revenue Recognition - Sales Orders (F2441A). | The Event Based Revenue Recognition: Sales Orders screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Sales Document: <Your sales order number>Note The sales document and sales document items are generated after running the prerequisite business conditions.Company Code: 3310Revenue Recognition Key: <for example, SFS> | The sales orders with derived revenue recognition key are displayed. |  |
| 4 | Sales Order | Select the sales order to view the details. In this view, you can set Parameters, Revaluate, Enter temporary adjustment or change RA key if required. |  |  |

### Review Allocated Revenue (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report is only relevant for IFRS Bundling. This report will show allocated revenue based on standalone selling price ratio (transaction price/sale price is divided based on standalone selling price ratio). For further information regarding bundling functionality in context of IFRS 15 and ASC 606, see SAP Note [2524569](https://me.sap.com/notes/2524569).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Allocated Revenue (F3039). | The Display Allocated Revenue (F3039) screen displays. |  |
| 3 | Enter Report Criteria | Make the following entries and choose Go:Sales Document: <enter your sales order> | Allocated revenue vs standalone selling price and transaction price displays. |  |

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

### Run Revenue Recognition: Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the event-based revenue recognition for sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Revenue Recognition - Sales Orders (F4276). | The Application Jobsview displays. |  |
| 3 | New Job | Choose the Create button. | The New Job: Run Revenue Recognition - Sales Orders view displays. |  |
| 4 | Enter Selection Criteria | Make the following entries and choose the Schedule button:Job Template: Run Revenue Recognition – Sales OrdersJob Name: <Enter a description or leave the default description>Choose the Step 2 button.Start Immediately: <checked>Choose the Step 3 button.Fixed Period: <mm/yyyy>ORDynamic Period: <use the dropdown to select, for example, Current Fiscal Period>Company Code: 3310Ledger: 3LSales Document: <your created sales document> | The new job is executed. |  |

### Manage Revenue Recognition Issues – Sales Orders

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
| 2 | Access the App | Open Manage Revenue Recognition Issues - Sales Orders (F4185) . | The Manage Revenue RecognitionIssues - Sales Orders view displays. |  |
| 3 | Enter Processing Data | Make the following entries and choose Go:Fiscal Year Period: <MM/YYYY>Company Code: 3310Ledger: 3L | No data found indicates that there are no issues. If issues are shown, review and process corrections.Tip To download the issue list, make your filter selections and select Show Error Summary. From the list, you can choose the Download button. |  |

### Optional: Revenue Recognition Reversal

You could reverse revenue recognition if you made an error. For information on revenue recognition reversal, see the [Reverse Month-End Revenue Recognition Postings](#unique_20) step in the Appendix section.

### Sales Order Actual Data Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the Sales Order Actual Data report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Sales Orders - Actuals (F1582A). | The Prompts dialog box appears on top of the Sales Orders - Actuals screen. |  |
| 3 | Enter Report Criteria | Make the following entries:Ledger: 0LLedger Fiscal Year: 2023Fiscal Period: <enter period, for example, the current period>Company Code: 3310Sales Order: sales order numberG/L Account (Hierarchy): YPS2Key Date: enter a date | The actual figures for sales order - actuals display. |  |
| 4 | Accept | Choose OK. |  |  |

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
- related-to :: [[06-management-accounting/7r8-537]]
- related-to :: [[06-management-accounting/event-based-revenue-recognition-sell-from-stock-1k2-ae-test-script-731]]
- related-to :: [[06-management-accounting/master-data-script-create-material-master-for-universal-revenue-recogn]]
- related-to :: [[06-management-accounting/master-data-script-item-master-for-universal-revenue-recognition-7r8-j]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33J_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 32,743 chars in the whole document
