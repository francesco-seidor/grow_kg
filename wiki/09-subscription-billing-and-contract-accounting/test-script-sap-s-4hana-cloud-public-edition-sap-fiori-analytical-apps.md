---
id: 09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-sap-fiori-analytical-apps
title: Test Script SAP S/4HANA Cloud Public Edition - SAP Fiori Analytical Apps for Contract Accounting Manager (2KH) (2KH_S4CLD2608_BPD_EN_XX)
description: "Test script for scope item 2KH: Fiori analytical apps for FI-CA (overdue items, locks, dunning, collections, returns, incoming payments) and My Open Worklists, release 2608."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-open-item-management]
aliases: [2KH_S4CLD2608_BPD_EN_XX]
keywords: [Contract Accounting Open Item Management and Collections, contract accounting analytics, overdue items analysis, open credits, write-offs, clearing reasons, payment run exceptions, returns analysis, dunning analysis, dunning run exceptions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2KH_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-829
topic: 09-subscription-billing-and-contract-accounting/fi-ca-open-item-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - SAP Fiori Analytical Apps for Contract Accounting Manager (2KH) (2KH_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2KH_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Contract Accounting Open Item Management and Collections** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Fiori Analytical Apps for Contract Accounting Manager (2KH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232843176)

[2 Prerequisites 4](#_Toc232843177)

[2.1 System Access 4](#_Toc232843178)

[2.2 Roles 4](#_Toc232843179)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232843180)

[2.4 Business Conditions 5](#_Toc232843181)

[2.5 Preliminary Steps 5](#_Toc232843182)

[3 Overview Table 7](#_Toc232843183)

[4 Test Procedures 9](#_Toc232843184)

[4.1 Analyze Data 9](#_Toc232843185)

[4.1.1 Analyze Overdue Items 9](#_Toc232843186)

[4.1.2 Analyze Open Credit Items 12](#_Toc232843187)

[4.1.3 Analyze Write-Offs 14](#_Toc232843188)

[4.1.4 Analyze Clearing Reasons 17](#_Toc232843189)

[4.1.5 Analyze Payment Run Exceptions 20](#_Toc232843190)

[4.1.6 Analyze Returns 23](#_Toc232843191)

[4.1.7 Analyze Dunning Volume 26](#_Toc232843192)

[4.1.8 Analyze Dunning Success 29](#_Toc232843193)

[4.1.9 Analyze Dunning Run Exceptions 31](#_Toc232843194)

[4.1.10 Create a Snapshot of Locked Open Items 34](#_Toc232843195)

[4.1.11 Analyze Dunning Locks 36](#_Toc232843196)

[4.1.12 Analyze Payment Locks 38](#_Toc232843197)

[4.1.13 Analyze Clearing Locks 40](#_Toc232843198)

[4.1.14 Analyze Posting Locks 42](#_Toc232843199)

[4.1.15 Analyze Installment Plans 44](#_Toc232843200)

[4.1.16 Analyze External Collections Volume 47](#_Toc232843201)

[4.1.17 Analyze Collections Volume 49](#_Toc232843202)

[4.1.18 Analyze Incoming Payments 52](#_Toc232843203)

[4.2 Track Worklists 54](#_Toc232843204)

[4.2.1 My Open Worklists 54](#_Toc232843205)

[5 Appendix 56](#_Toc232843206)

[5.1 Process Integration 56](#_Toc232843207)

[5.1.1 Preceding Processes 56](#_Toc232843208)

[5.1.2 Succeeding Processes 56](#_Toc232843209)

[5.2 Analyze Collections Success 57](#_Toc232843210)

## Purpose

Overview

This process allows you to analyze data in Contract Accounts Receivable and Payable (FI-CA) according to different business perspectives.

- Analyze Overdue Items
- Analyze Open Credit Items
- Analyze Write-Offs
- Analyze Clearing Reasons
- Analyze Payment Run Exceptions
- Analyze Returns
- Analyze Dunning Volume
- Analyze Dunning Success
- Analyze Dunning Run Exceptions
- Analyze Dunning Locks
- Analyze Payment Locks
- Analyze Posting Locks
- Analyze Clearing Locks
- Analyze Installment Plans
- Analyze External Collections Volume
- Analyze Collections Volume
- Analyze Collections Success
- Analyze Incoming Payments

Within these apps you can create worklists for your colleagues to perform further checks and resolve the detected problems. With the app My Open Worklists you can track the status of the processing of these worklists.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Accounts Payable and Receivable Manager (FI-CA) | SAP_BR_APR_MANAGER_FICA | Contract Accounting - Analytics | SAP_BR_APR_MANAGER_FICA |  |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |
| Administrator - Accounts Payable and Receivable (FI-CA) | SAP_BR_ADMIN_APR_FICA | Contract Accounting - Jobs | SAP_BR_ADMIN_APR_FICA |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Contract partner and contract account have been created for posting. |
| 2BI - Contract Accounting – Customer Initiated Payments | Invoices have been created for posting and the payment run has collected the open items. Also for returns which have also been posted. Payment Lots or Check Lots have been posted. |
| 2DP - Contract Accounting – Company Initiated Payments | Credits have been created and paid out to the customers. Also for returns which have also been posted. |
| 2BK - Contract Accounting – Daily and Monthly Closing | Noncollectable Receivables are written off. As well the monthly and daily closing is done (not necessary for this test script). |
| 2UJ - Contract Accounting – Open Item Management | Dunning notices are created. Installment plans exist as well. Collection Agency Postings exist. Valuating the Success of Dunning/Collections were executed and determined successfully. |
| 47I - Contract Accounting – Cash Application | Only to test if the company code is active for machine learning support and suitable trained ML model exits.Payment lot's clearing control is being processed considering with the machine learning proposals. |

### Preliminary Steps

Make sure you have the following data available in your system:

- Overdue Items
- Open Credits
- Write-Offs
- Cleared Items
- Payment Run Exceptions
- Returns
- Dunning Notices
- Installment Plan
- Collection Agency Postings
- Payment Lots or Check Lots are created and posted
- Dunning Locks
- Payment Locks
- Clearing Locks
- Posting Locks

To create locks, you have to log on with the Role Accounts Payable and Receivable Accountant (FI-CA):

- Dunning Locks:

Choose transaction Change Document to create locks on document level. The dunning lock can be set on the tab Dunn. Data.

Choose transaction Maintain Contract Account to create locks on contract account level. The dunning lock can be set on the tab Dunning/Correspondence.

- Payment Locks:

Choose transaction Change Document to create locks on document level. The payment lock can be set on the tab Payt Data. Make sure you create payment locks for payables and receivables.

Choose transaction Maintain Contract Account to create locks on contract account level. The payment lock can be set on the tab Payment/Taxes. Make sure you create payment locks for outgoing and incoming payments.

- Clearing Locks:

Choose transaction Change Document to create locks on document level. The clearing lock can be set on the tab Payt Data. Make sure you create clearing locks for payables and receivables.

- Posting Locks:

Choose transaction Maintain Contract Account to create locks on contract account level. The posting lock can be set on the tab General Data.

Usually the locks are set automatically by the system.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Analyze Data

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Analyze Overdue Items](#unique_9) [page ] 9 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Overdue Items (F0860A) | Open Items are visualized in a chart and worklists can be created. |
| [Analyze Open Credit Items](#unique_10) [page ] 12 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Open Credits (F2364A) | Open Credits are visualized in a chart and worklists can be created. |
| [Analyze Write-Offs](#unique_11) [page ] 14 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Write-Offs (F0861A) | Write-Offs are visualized in a chart. |
| [Analyze Clearing Reasons](#unique_12) [page ] 17 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Clearing Reasons (F2125A) | Clearing reasons are visualized in a chart. |
| [Analyze Payment Run Exceptions](#unique_13) [page ] 20 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Payment Run Exceptions (F2124A) | Payment run exceptions are visualized in a chart and worklists can be created. |
| [Analyze Returns](#unique_14) [page ] 23 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Returns (F2600A) | Returns are visualized in a chart and worklists can be created. A list with the returns is also available. |
| [Analyze Dunning Volume](#unique_15) [page ] 26 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Dunning Volume (F2122A) | Dunning volume is visualized in a chart. A list with the dunning notices is also available. |
| [Analyze Dunning Success](#unique_16) [page ] 29 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Dunning Success (F2123A) | Dunning success is visualized in a chart. |
| [Analyze Dunning Run Exceptions](#unique_17) [page ] 31 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Dunning Run Exceptions (F2596A) | Dunning run exceptions are visualized in a chart and worklists can be created. A list with the exceptions is also available. |
| [Create a Snapshot of Locked Open Items](#unique_18) [page ] 34 | Administrator - Accounts Payable and Receivable (FI-CA) | Create Snapshot of Locked Open Items - for Contract Accounting (F6214) | The job for creating a snapshot of locked open items is excuted. It is a prerequisite for the analytical apps for business locks, i.e. Analyze Dunning Locks (F1655A), Analyze Payment Locks (F6134), Analyze Clearing Locks (F1653A). |
| [Analyze Dunning Locks](#unique_19) [page ] 36 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Dunning Locks (F1655A) | Dunning locks are visualized in a chart and worklists can be created. |
| [Analyze Payment Locks](#unique_20) [page ] 38 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Payment Locks - Receivables (F6134) | Payment locks are visualized in a chart and worklists can be created. |
| [Analyze Clearing Locks](#unique_21) [page ] 40 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Clearing Locks - Receivables (F1653A) | Clearing locks are visualized in a chart and worklists can be created. |
| [Analyze Posting Locks](#unique_22) [page ] 42 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Posting Locks (F1652A) | Posting locks are visualized in a chart and worklists can be created. |
| [Analyze Installment Plans](#unique_23) [page ] 44 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Installment Plans (F2363A) | Installment Plans are visualized in a chart and worklists can be created. |
| [Analyze External Collections Volume](#unique_24) [page ] 47 | Accounts Payable and Receivable Manager (FI-CA) | Analyze External Collections Volume (F2402A) | External collections volume are visualized in a chart. |
| [Analyze Collections Volume](#unique_25) [page ] 49 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Collections Volume (F2208A) | Collections volume is visualized in a chart. A list with the dunning notices by collection strategy is also available. |
| [Analyze Incoming Payments](#unique_26) [page ] 52 | Accounts Payable and Receivable Manager (FI-CA) | Analyze Incoming Payments (F5588) | Incoming Payments is visualized in a chart. |

Check Worklists

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [My Open Worklists](#unique_27) [page ] 54 | Accounts Payable and Receivable Manager (FI-CA) | My Open Worklists (F1611A) | The worklists and their processing progress are shown in this app. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Analyze Data

#### Analyze Overdue Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Overdue Items, an Accounts Payable and Receivable Manager (FI-CA) can display the number and value of items which are overdue in Contract Accounts Receivable and Payable. The value and number of overdue items can be filtered by various criteria. Any irregularities detected during the analysis can be collected into a worklist and transmitted to a processor responsible for follow-up activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Overdue Items (F0860A). | The screen Analyze Overdue Items is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select a special main transaction from the value help of the filter Main Transaction, and then choose OK. Choose Go to enable the selection. | The chart will only display overdue items for the selected main transaction. |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, a filter chart will be shown. It is:Number of Items by Company Code |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. For example, choose the Measure icon to the right of the Number of Items by Company Code field, and select Amount from the list. Choose OK. | The filter chart for Amount by Company Code will show the amount by company code accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the Overdue Items chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, add dimension Segment and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the segments. |  |
| 10 | Change Time Frame | In the case where a date has been selected as grouping criteria, the time frame for the chart displayed can be changed. For example, choose an item like Calendar Quarter or Calendar Week as dimension. | The unit description of the x-axis will be changed and the chart will be adjusted. |  |
| 11 | Change Measure | In the View Settings dialog box, one or more measures can be used for the chart. For example, you can select Amount and Number of Items as measures. | The chart will be adjusted. |  |
| 12 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Dunning Procedure. | The dimension Dunning Procedure with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 13 | Restrict the View | Choose one or more bars or columns from the chart. | The detailed information will be shown in dialog box appears.The chart and table view will display only those bar(s) or column(s) selected. |  |
| 14 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Column Chart. | The chart type will be changed. |  |
| 15 | Change Settings of Table | Choose the Settings icon to the right of the Overdue Items table. Under the Columns tab in the View Settings dialog box, you can select Last Worklist Item Created At and Last Worklist Item Status as additional columns. Then choose OK. | The table settings will be changed. |  |
| 16 | Navigate to Other Apps for a Specific Business Partner | Choose a business partner ID from the table and navigate to a business-partner-specific app, for example, choose Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |
| 17 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Overdue Items screen. |  |
| 18 | Navigate to Other Analytical Apps | Select the line item from the table and navigate to another analytical app, for example, Write Offs. | The Fiori app Write Offs opens and the Write-Offs items for the selected business partners are shown. |  |
| 19 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Overdue Items screen. |  |
| 20 | Create a Worklist | Select the line item from the table and choose Create Worklist. Enter your values in the dialog box appears, select the Create Email checkbox and choose Create. | A message is displayed that a worklist has been created. A mail is created which also displays the worklist number.This worklist can now be processed by a responsible person. |  |
| 21 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Overdue Items screen. |  |
| 22 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter data required in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Analyze Open Credit Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Open Credit, an Accounts Payable and Receivable Manager (FI-CA) can display the number or value of open credits in Contract Accounts Receivable and Payable. The value and number of open credits can be filtered by various criteria. Any irregularities detected during the analysis can be collected into a worklist and transmitted to a processor responsible for follow-up activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Open Credits (F2364A). | The screen Analyze Open Credit Items is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select a special main transaction from the value help of the filter Main Transaction, and then choose OK. Choose Go to enable the selection. | The chart will only display open credits for the selected main transaction. |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, a filter chart will be shown. It is:Amount by Company Code |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. For example, choose the Measure icon to the right of the Amount by Company Code field, and select Number of Items from the list. Choose OK. | The filter chart for Number of Items by Company Code will show the number of items by company code accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the Open Credits chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, add dimension Segment and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the segments. |  |
| 10 | Change Time Frame | In the case where a date has been selected as grouping criteria, the time frame for the chart displayed can be changed. For example, choose an item like Quarter of Due Date or Week of Due Date as dimension. | The unit description of the x-axis will be changed and the chart will be adjusted. |  |
| 11 | Change Measure | In the View Settings dialog box, one or more measures can be used for the chart. For example, you can select Amount and Number of Items as measures. | The chart will be adjusted. |  |
| 12 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Segment. | The dimension Segment with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 13 | Restrict the View | Choose one or more bars or columns from the chart. | The detailed information will be shown in dialog box appears.The chart and table view will display only those bar(s) or column(s) selected. |  |
| 14 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Column Chart. | The chart type will be changed. |  |
| 15 | Change Settings of Table | Choose the Settings icon to the right of the Open Credits table. Under the Columns tab in the View Settings dialog box, you can select Last Worklist Item Created At and Last Worklist Item Status as additional columns. Then choose OK. | The table settings will be changed. |  |
| 16 | Navigate to Other Apps for a Specific Business Partner | Choose a business partner ID from the table and navigate to a business-partner-specific app, for example, choose Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |
| 17 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Open Credit Items screen. |  |
| 18 | Navigate to Other Analytical Apps | Select the line item from the table and navigate to another analytical app, for example, Analyze Overdue Items. | The Fiori app Analyze Overdue Items opens and the overdue items for the selected business partners are shown. |  |
| 19 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Open Credit Items screen. |  |
| 20 | Create a Worklist | Select the line item from the table and choose Create Worklist. Enter your values in the dialog box appears, select the Create Email checkbox and choose Create. | A message is displayed that a worklist has been created. A mail is created which also displays the worklist number.This worklist can now be processed by a responsible person. |  |
| 21 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Open Credit Items screen. |  |
| 22 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter data required in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Analyze Write-Offs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Write-Offs an Accounts Payable and Receivable Manager (FI-CA) can display the number and value of write-offs made in Contract Accounts Receivable and Payable. The value and number can be filtered by various criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Write-Offs (F0861A). | The screen Analyze Write-Offs is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select a special company code from the value help of the filter Company Code and then choose OK. Choose Go to enable the selection. | The chart and table will only show write-offs for the selected company code. |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, 3 filter charts will be shown. They are:Amount by Company CodeAmount by Contract Account CategoryAmount by Write-Off Reason |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. For example, choose the Measure icon to the right of the Amount by Company Code field, and select Number of Write-Offs from the list. Choose OK. | The filter chart for Number of Write-Offs by Company Code will show the number of write-offs by company code accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the Write-Offs chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, add dimension Write-Off Reason and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the write-off reason. |  |
| 10 | Change Measure | In the View Settings dialog box, one or more measures can be used for the chart. For example, you can select Amount and Number of Write-Offs as measures. Then choose OK. | The chart will be adjusted. |  |
| 11 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Quarter of Write-Off. | The dimension Quarter of Write-Off with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 12 | Restrict the View | Choose one or more bars or columns from the chart. | The detailed information will be shown in dialog box appears.The chart and table view will display only those bar(s) or column(s) selected. |  |
| 13 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Column Chart. | The chart type will be changed. |  |
| 14 | Change Settings of Table | Choose the Settings icon to the right of the Write-Offs table. Under the Columns tab in the View Settings dialog box, you can select Run ID and Run Date as additional columns. Then choose OK. | The table settings will be changed. |  |
| 15 | Navigate to App Display Write-Offs | Select the line item from the table and choose Display Write-Offs. | A list with Write-Off document(s) will be displayed. The filter criteria and filters can also be adapted here. |  |
| 16 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Write-Offs screen. |  |
| 17 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter data required in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Analyze Clearing Reasons

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Clearing Reasons an Accounts Payable and Receivable Manager can track clearing reasons for receivables for a certain time period. It can be determined which receivables have already been cleared and how they were cleared. Additionally, the open amount of the analyzed receivables can be displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Clearing Reasons (F2125A). | The screen Analyze Clearing Reasons is displayed.The number and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, choose Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select a special main transaction from the value help of the filter Main Transaction, and then choose OK. Choose Go to enable the selection. | The chart and table view will only show cleared receivables for the selected main transaction. |  |
| 5 | Adapt Filters | Choose Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, a filter chart will be shown. It is:Number of Items by Main Transaction |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type for the filter charts. | The filter chart will be adjusted accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the Receivables chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions for the chart. For example, add dimension Net Due Date in Months and choose Category for layout option. | The columns in the chart will show the currently selected entries, for example, Net Due Date in Months.You can configure the group via SSCUI: Group Clearing Reasons for Evaluation with ID 106363.With the group configuration, items can be displayed grouped together based on their clearing reason(s). For example, it is desired to display all the items that have a clearing reason related to any type of reversal. In such a case a new group can be created and the clearing reasons 'Reversal', 'Statistic Item reset' and 'Reset Cleared items' assigned.NoteAs soon as you create customized groups, you override the delivered preset groups.Clearing reasons that you do not assign to a group are not evaluated by the app and also do not display the cleared receivable.You can assign a clearing reason to multiple groups. Note that this can distort the total sum total of the clearings displayed in the app.Clearing Reason Group can also be defined through the menu App Settings from the icon Profile of User.It is only user-specific and will override the groups via SSCUI 106363: Group Clearing Reasons for Evaluation. |  |
| 10 | Change Measure | In the View Settings dialog box, one or more measures can be used for the chart. For example, you can select Amount and Number of Items as measures. | The chart will be adjusted. |  |
| 11 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Document Type. | The dimension Document Type with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 12 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Column Chart. | The chart type will be changed. |  |
| 13 | Restrict the View | Choose one or more bars or columns from the chart. | The chart and table view will display only those bar(s) or column(s) selected. |  |
| 14 | Change Settings of Table | Choose the Settings icon to the right of the Receivables table. Under the Columns tab in the View Settings dialog box, you can one or more available columns. For example: Business Partner. You can also configure sort, filter and group for the table, and then choose OK. | The table settings will be changed. |  |
| 15 | Navigate to Other Apps for a Specific Business Partner | Choose a business partner ID from the table and navigate to a business-partner-specific app, for example, choose Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |
| 16 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Clearing Reasons screen. |  |
| 17 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter data required in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Analyze Payment Run Exceptions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Payment Run Exceptions, an Accounts Payable and Receivable Manager can analyze the number and amount of payment run exceptions dependent on various grouping and filter criteria. Any irregularities detected during the analysis can be collected into a worklist and transmitted to a processor responsible for follow-up activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as role Accounts Payable and Receivable Manager (FI-CA) assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Payment Run Exceptions (F2124A). | The screen Analyze Payment Run Exceptions is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, choose Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select Receivable or Payable from the value help of the mandatory filter Variant. | The chart will only show payment run exceptions for the selected variant. |  |
| 5 | Adapt Filters | Choose Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, two filter charts will be shown. They are:Amount by Exception ReasonNumber of Exceptions by Payment Status |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. For example, choose the Measure icon to the right of the Amount by Exception Reason field, and select Number of Exceptions from the list. Choose OK. | The filter chart for Number of Exceptions by Exception Reason will show the number of exceptions accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the Payment Run Exceptions chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, add dimension Exception Reason and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the exception reason.User-specific exceptions groups can be defined through the menu App Settings from the icon Profile of User. |  |
| 10 | Change Time Frame | In the case where a date has been selected as grouping criteria, the time frame for the chart displayed can be changed. For example, choose an item like Quarter of Payment Run or Week of Payment Run as dimension. | The unit description of the x-axis will be changed and the chart will be adjusted. |  |
| 11 | Change Measure | In the View Settings dialog box, one or more measures can be used for the chart. For example, you can select Amount and Number of Exceptions as measures. | The chart will be adjusted. |  |
| 12 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list. | The chart will be adjusted. |  |
| 13 | Restrict the View | Choose one or more bars or columns from the chart. | The detailed information will be shown in dialog box appears.The chart and table view will display only those bar(s) or column(s) selected. |  |
| 14 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Column Chart. | The chart type will be changed. |  |
| 15 | Change Settings of Table | Choose the Settings icon to the right of the Payment Run Excpetions table. Under the Columns tab in the View Settings dialog box, you can select Last Worklist Item Created At and Last Worklist Item Status as additional columns. Then choose OK. | The table settings will be changed. |  |
| 16 | Navigate to Other Apps for a Specific Business Partner | Choose a business partner ID from the table and navigate to a business-partner-specific app, for example, choose Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |
| 17 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Payment Run Exceptions screen. |  |
| 18 | Navigate to Other Analytical Apps | Select the line item from the table and navigate to another analytical app, for example, Anaylze Payment Locks. | The Fiori app Analyze Payment Locks opens and the Payment Locks for the selected business partners are shown. |  |
| 19 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Payment Run Exceptions screen. |  |
| 20 | Create a Worklist | Select the line item from the table and choose Create Worklist. Enter your values in the dialog box appears, select the Create Email checkbox and choose Create. | A message is displayed that a worklist has been created. A mail is created which also displays the worklist number.This worklist can now be processed by a responsible person. |  |
| 21 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Payment Run Exceptions screen. |  |
| 22 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter data required in the dialog box appears and choose OK. | A new tile will be created on the launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Analyze Returns

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Returns an Accounts Payable and Receivable Manager can analyze the number and value of returns dependent on various grouping and filter criteria. Any irregularities detected during the analysis can be collected into a worklist and transmitted to a processor responsible for follow-up activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Returns(F2600A). | The screen Analyze Returns is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, choose Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select Incoming Payment or Outgoing Payment from the value help of the mandatory filter Variants and then choose OK. Choose Go to enable the selection. | The chart will only show returns for the selected variant. |  |
| 5 | Adapt Filters | Choose Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, three filter charts will be shown. They are:Returns Amount by Returns ReasonCharge (Own Company) by Returns TypeReturns Amount by House Bank Key |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. For example, choose the Measure icon to the right of the Returns Amount by Returns Reason field, and select Number of Returns from the list. Choose OK. | The filter chart for Number of Returns by Returns Reason will show the number of returns by returns reason accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the Analyze Returns chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, add dimension House Bank and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the house banks. |  |
| 10 | Change Time Frame | In the case where a date has been selected as grouping criteria, the time frame for the chart displayed can be changed. For example, choose an item like Value date in Quarters or Value Date in Weeks as dimension. | The unit description of the x-axis will be changed and the chart will be adjusted. |  |
| 11 | Change Measure | In the View Settings dialog box, one or more measures can be used for the chart. For example, you can select Returns Amount and Number of Returns as measures. | The chart will be adjusted. |  |
| 12 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Returns Reason. | The dimension Returns Reason with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 13 | Restrict the View | Choose one or more bars or columns from the chart. | The detailed information will be shown in dialog box appears.The chart and table view will display only those bar(s) or column(s) selected. |  |
| 14 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Column Chart. | The chart type will be changed. |  |
| 15 | Change Settings of Table | Choose the Settings icon to the right of the A nalyze Returns table. Under the Columns tab in the View Settings dialog box, you can select Last Worklist Item Created At and Last Worklist Item Status as additional columns. Then choose OK. | The table settings will be changed. |  |
| 16 | Navigate to Other Apps for a Specific Business Partner | Choose a business partner ID from the table and navigate to a business-partner-specific app, for example, choose Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |
| 17 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Returns screen. |  |
| 18 | Navigate to Other Analytical Apps | Select the line item from the table and navigate to another analytical app, for example, Anaylze Payment Locks. | The Fiori app Analyze Payment Locks opens and the Payment Locks for the selected business partners are shown. |  |
| 19 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Returns screen. |  |
| 20 | Create a Worklist | Select the line item from the table and choose Create Worklist. Enter your values in the dialog box appears, select the Create Email checkbox and choose Create. | A message is displayed that a worklist has been created. A mail is created which also displays the worklist number.This worklist can now be processed by a responsible person. |  |
| 21 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Returns screen. |  |
| 22 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter data required in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Analyze Dunning Volume

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Dunning Volume an Accounts Payable and Receivable Manager can display the number of items and total amount based on the dunning procedure that has been dunned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Dunning Volume (F2122A). | The screen Analyze Dunning Volume is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select a special dunning level from the value help of the filter Dunning Level and then choose OK. Choose Go to enable the selection. | The chart and table view will only show dunning data for the selected dunning level. |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, 3 filter charts will be shown. They are:Dunning Volume by Company CodeDunning Volume by Dunning ProcedureDunning Volume by Dunning Level |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. For example, choose the Measure icon to the right of the Dunning Volume by Company Code field, and select Number of Dunning Notices from the list. | The filter chart for Dunning Volume by Company Code will show the number of dunning notices accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the Dunning Volume chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, remove existing dimension, add dimension Dunning Procedure and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the dunning procedure. |  |
| 10 | Change Measure | In the View Settings dialog box, one or more measures can be used for the chart. For example, you can select Dunning Volume and Number of Dunning Notices as measures. | The chart will be adjusted. |  |
| 11 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Quarter of Issue. | The dimension Quarter of Issue with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 12 | Display Details | Select one or more columns and choose the Details icon on the top right of the chart. | The detailed information will be shown in the dialog box appears.The chart and table view will display only the column(s) selected. |  |
| 13 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Column Chart. | The chart type will be changed. |  |
| 14 | Change Settings of Table | Choose the Settings icon to the right of the Dunning Volume table. Under the Columns tab in the View Settings dialog box, you can select Run ID and Run Date as additional columns. Then choose OK. | The table settings will be changed. |  |
| 15 | View Dunning Notices | Choose the line item in the table and choose the Details(>) icon to the right of its row. | List of dunning notices is displayed. The filter criteria and filters can also be adapted here. |  |
| 16 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Dunning Volume screen. |  |
| 17 | Navigate to Other Analytical Apps | Choose the line item from the table and navigate to another analytical app, for example, choose Analyze Overdue Items. | The Fiori app Analyze Overdue Items opens and the overdue items for the selected business partners are shown. |  |
| 18 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Dunning Volume screen. |  |
| 19 | Navigate to Other Apps for a Specific Business Partner | Choose the business partner ID in one line item and navigate to a business-partner-specific app, for example, choose the link Business Partner Financial Overview. | The Fiori app Business Partner Financial Overview opens for the selected business partner. |  |
| 20 | Navigate Back | Choose the Back button again. | You can get back to the Analyze Dunning Volume screen. |  |
| 21 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter some data in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Analyze Dunning Success

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Dunning Success an Accounts Payable and Receivable Manager can display an overview of the dunning success (in percentage) within a certain time frame or related to various dunning procedures and dunning activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Dunning Success (F2123A). | The screen Analyze Dunning Success is displayed.The percentage and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select a special dunning level from the value help of the filter Dunning Level and then choose OK. Choose Go to enable the selection. | The chart will only show dunning data for the selected dunning level. |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, 2 filter charts will be shown. They are:Success Rate by Company CodeSuccess Rate by Segment |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. | The filter chart will be changed accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the Dunning Success chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, remove existing dimension, add dimension Segment and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the segment. |  |
| 10 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Quarter of Issue. | The dimension Quarter of Issue with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 11 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Bar Chart. | The chart type will be changed. |  |
| 12 | Change Settings of Table | If the Dunning Success table is hidden, choose the Chart and Table View icon to the right of the Dunning Success chart.Choose the Settings icon to the right of the Dunning Success table. Under the Columns tab in the View Settings dialog box, you can choose other available columns. You can also configure sort and group for the table Dunning Success. Then choose OK. | Data of the table will be adjusted and displayed. |  |
| 13 | Restrict the View | Select one or more bars or columns from the chart. | Data of the table will be adjusted. It will only display those dunning success that the bar(s) or column(s) selected. |  |
| 14 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter some data in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Analyze Dunning Run Exceptions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Dunning Run Exceptions an Accounts Payable and Receivable Manager can analyze the number and amount of dunning run exceptions dependent on various grouping and filter criteria. Any irregularities detected during the analysis can be collected into a worklist and transmitted to a responsible processor for follow-up activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Dunning Run Exceptions (F2596A). | The screen Analyze Dunning Run Exceptions is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select a special exception reason from the value help of the filter Exception Reason and then choose OK. Choose Go to enable the selection. | The chart will only show exceptions for the selected exception reason. |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, two filter charts will be shown. They are:Amount by Exception ReasonAmount by Dunning Lock Reason |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. For example, choose the Measure icon to the right of the Amount by Exception Reason field, and select Number of Exceptions from the list. Choose OK. | The filter chart for Number of Exceptions by Exception Reason will show the number of exceptions accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the Dunning Run Excepts chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, add dimension Segment and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the segments.User-specific exceptions groups can be defined through the menu App Settings from the icon Profile of User. |  |
| 10 | Change Time Frame | In the case where a date has been selected as grouping criteria, the time frame for the chart displayed can be changed. For example, choose an item like Quarter of Issue or Week of Issue as dimension. | The unit description of the x-axis will be changed and the chart will be adjusted. |  |
| 11 | Change Measure | In the View Settings dialog box, one or more measures can be used for the chart. For example, you can select Amount and Number of Exceptions as measures. | The chart will be adjusted. |  |
| 12 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Dunning Lock Reason. | The dimension Dunning Lock Reason with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 13 | Restrict the View | Choose one or more bars or columns from the chart. | The detailed information will be shown in dialog box appears.The chart and table view will display only those bar(s) or column(s) selected. |  |
| 14 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Column Chart. | The chart type will be changed. |  |
| 15 | Change Settings of Table | Choose the Settings icon to the right of the Dunning Run Excpetions table. Under the Columns tab in the View Settings dialog box, you can select Last Worklist Item Created At and Last Worklist Item Status as additional columns. Then choose OK. | The table settings will be changed. |  |
| 16 | Navigate to Other Apps for a Specific Business Partner | Choose a business partner ID from the table and navigate to a business-partner-specific app, for example, choose Business Partner Financial Overview. | The Fiori app Business Partner Financial Overview opens for the selected business partner. |  |
| 17 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Dunning Run Exceptions screen. |  |
| 18 | Navigate to Other Analytical Apps | Select the line item from the table and navigate to another analytical app, for example, Display Dunning Exceptions. | The Fiori app Display Dunning Exceptions opens and the Dunning Exception items for the selected business partners are shown. |  |
| 19 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Dunning Run Exceptions screen. |  |
| 20 | Create a Worklist | Select the line item from the table and choose Create Worklist. Enter your values in the dialog box appears, select the Create Email checkbox and choose Create. | A message is displayed that a worklist has been created. A mail is created which also displays the worklist number.This worklist can now be processed by a responsible person. |  |
| 21 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Dunning Run Exceptions screen. |  |
| 22 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter data required in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Create a Snapshot of Locked Open Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Create Snapshot of Locked Open Items, an Administrator - Accounts Payable and Receivable (FI-CA) can schedule job with a predefined template to create Snapshot for locked open items automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Create Snapshot of Locked Open Items - for Contract Accounting (F6214). | The Create Snapshot of Locked Open Items - for Contract Accounting screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Create Snapshot of Locked Open ItemsJob Name: FI-CA: Create Snapshot of Locked Open Items |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: <Select> |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Identification section:Prefix of Run ID: <For example, ID0>In the Type of Run section:Simulation Run: <Deselect>In the Selection Criteria section:Create Snapshot for Apps: <Lock Apps> for example, keep it as blank if no dedicated app is chosen, the snapshot is created for all of them.Note The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, navigate to the new application job by choosing the information icon.Note You can also delete a snapshot by repeating Test Steps 1 to 6 of the prior test.In the Selection Criteria section:Select the Only Delete Existing Snapshot checkbox.Schedule the run and wait until it is finished. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Analyze Dunning Locks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Dunning Locks, an Accounts Payable and Receivable Manager can analyze the number and value of dunning locks. Any irregularities detected during the analysis can be collected into a worklist and transmitted to a responsible processor for follow-up activities.

Prerequisites

The step Create Snapshot for Locked Open Items has been executed and a Snapshot for Dunning Locks exists.

You can also use the navigation from the KPI tag Snapshot Age in the Analytical app to create a new snapshot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Dunning Locks (F1655A). | The screen Analyze Dunning Locks is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The filter bar with several filter criteria is shown. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example:Select Currency from the value help of the mandatory filter Display Currency.Select one or more Lock Object Categories from the value help of the filter Lock Object Category and then choose OK. Choose Go to enable the selection. | The chart will only show locked amounts for the selected lock object categories. |  |
| 5 | Adapt Filters | Choose the Adapt Filters button. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Show or Hide Legend | Choose the Show Legend button. Show or hide the legend of the chart. | The legend will be shown or hidden. |  |
| 7 | Change the Settings | Above the chart on the right-hand side are several icons. Choose the button Settings to change the dimension or measure in the chart. Modify the settings; for example, select the Dimension Lock Reasons, and select the Measure Number of Business Partner Items, and then choose OK. | The chart will be adjusted. |  |
| 8 | Change View By | Choose the drop-down list of View By above the chart on the right-hand side and select an item, for example, Created On in Months. | The columns in the chart will add additional dimension, for example, the Created On in Months. |  |
| 9 | Change the Chart Type | Choose the various chart types on the upper right-hand side of the chart. | The chart type will change. |  |
| 10 | Maximize the Chart | Above the chart on the right-hand side are several icons can adjust size of chart, for example. Choose the button Maximize . | The chart will be maximized. |  |
| 11 | Minimize the Chart | Choose the Minimize button. | The chart will be minimized. |  |
| 12 | Navigate to Other Apps for a Specific Business Partner | Select a business partner ID in one row and then navigate to a business-partner-specific app, for example, the Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |
| 13 | Navigate Back | Choose the back button again. | The view returns to the business partner list. |  |
| 14 | Create a Worklist | Choose one or more columns from the chart. Select some of the business partners in the list and click the button Create Worklist. On the screen appears enter some acceptable values, mark the checkbox Email and choose OK. | A message is displayed that a worklist has been created. A mail is created which also displays the worklist number.This worklist can now be processed by a responsible person. |  |
| 15 | Navigate Back | Choose the back button again. | The view returns to the chart. |  |
| 16 | Create a New Snapshot | In the upper left part, click on KPI tag Snapshot Age and then choose Create Snapshot.Navigation to Create a Snapshot of Locked Open Items. Follow up the steps of process of Create a Snapshot of Locked Open items. | After a successful run, the timestamp in the KPI details will be changed. |  |
| 17 | Navigate Back | Choose the back button again. | The view returns to the chart. |  |
| 18 | Save a New Tile | Enter some data in the filter bar and choose the buttons Share and Save as tile in the upper right part. Enter some acceptable data in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. This tile enables the analysis to be made with the settings made at the time the tile was created. |  |

#### Analyze Payment Locks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Payment Locks, an Accounts Payable and Receivable Manager can analyze the number and value of payment locks. Any irregularities detected during the analysis can be collected into a worklist and transmitted to a responsible processor for follow-up activities.

Prerequisites

The step Create Snapshot for Locked Open Items has been executed and a Snapshot for Payment Locks exists.

You can also use the navigation from the KPI tag Snapshot Age in the Analytical app to create a new snapshot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Payment Locks - Receivables (F6134). | The screen Analyze Payment Locks is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The filter bar with several filter criteria is shown. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example:Select Currency from the value help of the mandatory filter Display Currency.Select Receivable or Payable from the value help of the mandatory filter Variant.Select one or more Lock Object Categories from the value help of the filter Lock Object Category and then choose OK. Choose Go to enable the selection. | The chart will only show locked amounts for the selected lock object categories. |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Show or Hide Legend | Choose the button Show Legend. Show or hide the legend of the chart. | The legend will be shown or hidden. |  |
| 7 | Change the Settings | Above the chart on the right-hand side are several icons. Choose the button Settings to change the dimension or measure in the chart. Modify the settings; for example, select the Dimension Lock Reasons, and select the Measure Number of Business Partner Items, and then choose OK. | The chart will be adjusted. |  |
| 8 | Change View By | Choose the drop-down list of View By above the chart on the right-hand side and select an item, for example, Created On in Months. | The columns in the chart will add additional dimension, for example, the Created On in Months. |  |
| 9 | Change the Chart Type | Choose the various chart types on the upper right-hand side of the chart. | The chart type will change. |  |
| 10 | Maximize the Chart | Above the chart on the right-hand side are several icons can adjust size of chart, for example. Choose the button Maximize . | The chart will be maximized. |  |
| 11 | Minimize the Chart | Choose the button Minimize. | The chart will be minimized. |  |
| 12 | Navigate to Other Apps for a Specific Business Partner | Select a business partner ID in one row and then navigate to a business-partner-specific app, for example, the Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |
| 13 | Navigate Back | Choose the back button again. | The view returns to the business partner list. |  |
| 14 | Create a Worklist | Choose one or more columns from the chart. Select some of the business partners in the list and click the button Create Worklist. On the screen appears enter some acceptable values, mark the checkbox Email and choose OK. | A message is displayed that a worklist has been created. A mail is created which also displays the worklist number.This worklist can now be processed by a responsible person. |  |
| 15 | Navigate Back | Choose the back button again. | The view returns to the chart. |  |
| 16 | Create a New Snapshot | In the upper left part, click on KPI tag Snapshot Age and then choose Create Snapshot.Navigation to Create a Snapshot of Locked Open Items. Follow up the steps of process of Create a Snapshot of Locked Open items. | After a successful run, the timestamp in the KPI details will be changed. |  |
| 17 | Navigate Back | Choose the back button again. | The view returns to the chart. |  |
| 18 | Save a New Tile | Enter some data in the filter bar and choose the buttons Share and Save as tile in the upper right part. Enter some acceptable data in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. This tile enables the analysis to be made with the settings made at the time the tile was created. |  |

#### Analyze Clearing Locks

Context

With SAP Fiori App Analyze Clearing Locks, an Accounts Payable and Receivable Manager can analyze the number and value of clearing locks. Any irregularities detected during the analysis can be collected into a worklist and transmitted to a responsible processor for follow-up activities.

Prerequisites

The step Create Snapshot for Locked Open Items has been executed and a Snapshot for Clearing Locks exists.

You can also use the navigation from the KPI tag Snapshot Age in the Analytical app to create a new snapshot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Clearing Locks - Receivables (F1653A). | The screen Analyze Clearing Locks is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The filter bar with several filter criteria is shown. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example:Select Currency from the value help of the mandatory filter Display Currency.Select Receivable or Payable from the value help of the mandatory filter Variant .Select one or more Lock Object Categories from the value help of the filter Lock Object Category and then choose OK. Choose Go to enable the selection. | The chart will only show locked amounts for the selected lock object categories. |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Show or Hide Legend | Choose the button Show Legend. Show or hide the legend of the chart. | The legend will be shown or hidden. |  |
| 7 | Change the Settings | Above the chart on the right-hand side are several icons. Choose the button Settings to change the dimension or measure in the chart. Modify the settings; for example, select the Dimension Lock Reasons, and select the Measure Number of Business Partner Items, and then choose OK. | The chart will be adjusted. |  |
| 8 | Change View By | Choose the drop-down list of View By above the chart on the right-hand side and select an item, for example, Created On in Months. | The columns in the chart will add additional dimension, for example, the Created On in Months. |  |
| 9 | Change the Chart Type | Choose the various chart types on the upper right-hand side of the chart. | The chart type will change. |  |
| 10 | Maximize the Chart | Above the chart on the right-hand side are several icons can adjust size of chart, for example. Choose the button Maximize . | The chart will be maximized. |  |
| 11 | Minimize the Chart | Choose the button Minimize. | The chart will be minimized. |  |
| 12 | Navigate to Other Apps for a Specific Business Partner | Select a business partner ID in one row and then navigate to a business-partner-specific app, for example, the Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |
| 13 | Navigate Back | Choose the back button again. | The view returns to the business partner list. |  |
| 14 | Create a Worklist | Choose one or more columns from the chart. Select some of the business partners in the list and click the button Create Worklist. On the screen appears enter some acceptable values, mark the checkbox Email and choose OK. | A message is displayed that a worklist has been created. A mail is created which also displays the worklist number.This worklist can now be processed by a responsible person. |  |
| 15 | Navigate Back | Choose the back button again. | The view returns to the chart. |  |
| 16 | Create a New Snapshot | In the upper left part, click on KPI tag Snapshot Age and then choose Create Snapshot.Navigation to Create a Snapshot of Locked Open Items. Follow up the steps of process of Create a Snapshot of Locked Open items. | After a successful run, the timestamp in the KPI details will be changed. |  |
| 17 | Navigate Back | Choose the back button again. | The view returns to the chart. |  |
| 18 | Save a New Tile | Enter some data in the filter bar and choose the buttons Share and Save as tile in the upper right part. Enter some acceptable data in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. This tile enables the analysis to be made with the settings made at the time the tile was created. |  |

#### Analyze Posting Locks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Posting Locks, an Accounts Payable and Receivable Manager can analyze the number of posting locks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Posting Locks (F1652A) . | The screen Analyze Posting Locks is displayed.The number and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The filter bar with several filter criteria is shown. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select one or more Lock Object Categories from the value help of the filter Lock Object Category and then choose OK. Choose Go to enable the selection. | The chart will only show number of locks for the selected lock object categories. |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Show or Hide Legend | Choose the button Show Legend. Show or hide the legend of the chart. | The legend will be shown or hidden. |  |
| 7 | Change the Settings | Above the chart on the right-hand side are several icons. Choose the button Settings to change the dimension or measure in the chart. Modify the settings; for example, select the Dimension Lock Reasons, and then choose OK. | The chart will be adjusted. |  |
| 8 | Change View By | Choose the drop-down list of View By above the chart on the right-hand side and select an item, for example, Created On in Months. | The columns in the chart will add additional dimension, for example, the Created On in Months. |  |
| 9 | Change the Chart Type | Choose the various chart types on the upper right-hand side of the chart. | The chart type will change. |  |
| 10 | Maximize the Chart | Above the chart on the right-hand side are several icons that can adjust size of chart, for example, choose the button Maximize. | The chart will be maximized. |  |
| 11 | Minimize the Chart | Above the chart on the right-hand side are several icons that can adjust size of chart, for example, choose the button Maximize. | The chart will be minimized. |  |
| 12 | Navigate to Other Apps for a Specific Business Partner | Select a business partner ID in one row and then navigate to a business-partner-specific app, for example, the Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |
| 13 | Navigate Back | Choose the back button again. | The view returns to the business partner list. |  |
| 14 | Save a New Tile | Enter some data in the filter bar and choose the buttons Share and Save as tile in the upper right part. Enter some acceptable data in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. This tile enables the analysis to be made with the settings made at the time the tile was created. |  |

#### Analyze Installment Plans

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Installment Plans an Accounts Payable and Receivable Manager can number of installment plans that have been created and the total amount that has been paid into the original receivables in the installment plans. Any irregularities detected during the analysis can be collected into a worklist and transmitted to a processor responsible for follow-up activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Installment Plans (F2363A) . | Analyze Installment Plans is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select a special main transaction from the value help of the filter Category, and then choose OK. Choose Go to enable the selection. | The chart and table view will only show installments for the selected category. |  |
| 5 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, 3 filter charts will be shown. They are:Amount by Installment Plan StatusAmount by Status of InstallmentsAmount by Category |  |
| 6 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 7 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. For example, choose the Measure icon to the right of the Amount by Installment Plan Status field, and select Number of Installment Plans from the list. Choose OK. | The filter chart for Number of Installment Plans by Installment Plan Status will show the number of installment plans accordingly. |  |
| 8 | Change Grouping Criteria | Choose the Settings icon to the right of the Installment Plans chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, add dimension Status of Installments and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the status of installments. |  |
| 9 | Change Measure | In the View Settings dialog box, one or more measures can be used for the chart. For example, you can select Amount and Number of Installment Plans as measures. | The chart will be adjusted. |  |
| 10 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Category. | The dimension Category with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 11 | Restrict the View | Choose one or more bars or columns from the chart. | The detailed information will be shown in dialog box appears.The chart and table view will display only those bar(s) or column(s) selected. |  |
| 12 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Column Chart. | The chart type will be changed. |  |
| 13 | Change Settings of Table | Choose the Settings icon to the right of the Installment Plans table. Under the Columns tab in the View Settings dialog box, you can select Last Worklist Item Created At and Last Worklist Item Status as additional columns. Then choose OK. | The table settings will be changed. |  |
| 14 | Navigate to Other Apps for a Specific Business Partner | Choose a business partner ID from the table and navigate to a business-partner-specific app, for example, choose Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |
| 15 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Installment Plans screen. |  |
| 16 | Create a Worklist | Select the line item from the table and choose Create Worklist. Enter your values in the dialog box appears, select the Create Email checkbox and choose Create. | A message is displayed that a worklist has been created. A mail is created which also displays the worklist number.This worklist can now be processed by a responsible person. |  |
| 17 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Installment Plans screen. |  |
| 18 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter data required in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Analyze External Collections Volume

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze External Collections Volume an Accounts Payable and Receivable Manager can display the number of items or total amount of collections made by collection Agencies in Contract Accounts Receivable and Payable dependent on various grouping and filter criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze External Collections Volume (F2402A). | The screen Analyze External Collections Volume is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select a special submission status from the value help of the filter Submission status and then choose OK. Choose Go to enable the selection. | The chart and table view will only show collections data for the selected submission status. |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, 2 filter charts will be shown. They are:Amount by Collection AgencyAmount by Submission Reason |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. For example, choose the Measure icon to the right of the Amount by Collection Agency field, and select Number of Items from the list. Choose OK. | The filter chart for Collections Volume by Company Code will show the number of items by collection agency accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the External Collections Volume chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, add dimension Collection Agency and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the clooection agency. |  |
| 10 | Change Measure | In the View Settings dialog box, one or more measures can be used for the chart. For example, you can select Amount and Number of Items as measures. | The chart will be adjusted. |  |
| 11 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Submission Reason. | The dimension Submission Reason with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 12 | Change Settings of Table | Choose the Settings icon to the right of the External Collections Volume table. Under the Columns tab in the View Settings dialog box, you can select one or more columns for the table. You can also configure sort and group for the table. Then choose OK. | The table settings will be changed. |  |
| 13 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Column Chart. | The chart type will be changed. |  |
| 14 | Restrict the View | Choose one or more bars or columns from the chart. | The detailed information will be shown in dialog box appears.The chart and table view will display only those bar(s) or column(s) selected. |  |
| 15 | Navigate to Other Analytical Apps | Select the line item from the table and navigate to another analytical app, for example, Analyze Overdue Items. | The Fiori app Analyze Overdue Items opens and the overdue items for the selected business partners are shown. |  |
| 16 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze External Collections Volume screen. |  |
| 17 | Navigate to Other Apps for a Specific Business Partner | Choose a business partner ID from the table and navigate to a business-partner-specific app, for example, choose Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |
| 18 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze External Collections Volume screen. |  |
| 19 | Create a Worklist | Select the line item from the table and choose Create Worklist. Enter your values in the dialog box appears, select the Create Email checkbox and choose Create. | A message is displayed that a worklist has been created. A mail is created which also displays the worklist number.This worklist can now be processed by a responsible person. |  |
| 20 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze External Collections Volume screen. |  |
| 21 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter data required in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Analyze Collections Volume

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Collection Volume an Accounts Payable and Receivable Manager can display the number of items or total amount of dunning made with Collection Strategies in Contract Accounts Receivable and Payable dependent on various grouping and filter criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Collections Volume (F2208A). | The screen Analyze Collections Volume is displayed.The amount and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.Display Currency is the default user setting. For example, set EUR as Display Currency. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select a special collection step from the value help of the filter Collection Step and then choose OK. Choose Go to enable the selection. | The chart and table view will only show collections data for the selected collection step(s). |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, 3 filter charts will be shown. They are:Collections Volume by Company CodeCollections Volume by Collection StrategyCollections Volume by Collection Step |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. For example, choose the Measure icon via the Additional Options icon to the right of the Collections Volume by Company Code field, and select Number of Dunning Notices from the list. | The filter chart for Collections Volume by Company Code will show the number of dunning notices accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the Collections Volume chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, remove existing dimension, add dimension Collection Strategy and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the collection strategy. |  |
| 10 | Change Measure | In the View Settings dialog box, one or more measures can be used for the chart. For example, you can select Collections Volume and Number of Dunning Notice as measures. | The chart will be adjusted. |  |
| 11 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Quarter of Issue. | The dimension Quarter of Issue with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 12 | Display Details | Select one or more columns and choose the Details icon on the top right of the chart. | The detailed information will be shown in the dialog box appears.The chart and table view will display only the column(s) selected. |  |
| 13 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Column Chart. | The chart type will be changed. |  |
| 14 | Change Settings of Table | Choose the Settings icon to the right of the Collections Volume table. Under the Columns tab in the View Settings dialog box, you can also configure sort and group for the table Collections Volume. Then choose OK. | Data of the table will be adjusted. |  |
| 15 | View Dunning Notices | Choose the line item in the table and choose the Details(>) icon to the right of its row. | List of dunning notices is displayed. The filter criteria and filters can also be adapted here. |  |
| 16 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Collections Volume screen. |  |
| 17 | Navigate to Other Analytical Apps | Choose the line item from the table and navigate to another analytical app, for example, choose Analyze Overdue Items. | The Fiori app Analyze Overdue Items opens and the overdue items for the selected business partners are shown. |  |
| 18 | Navigate Back | Choose the Back button on the top left of the screen. | You can get back to the Analyze Collections Volume screen. |  |
| 19 | Navigate to Other Apps for a Specific Business Partner | Choose the business partner ID in one line item and navigate to a business-partner-specific app, for example, choose the link Business Partner Financial Overview. | The Fiori app Business Partner Financial Overview opens for the selected business partner. |  |
| 20 | Navigate Back | Choose the Back button again. | You can get back to the Analyze Collections Volume screen. |  |
| 21 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter some acceptable data in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

#### Analyze Incoming Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With SAP Fiori App Analyze Incoming Payments an Accounts Payable and Receivable Manager can display an overview of number of items within a payment lot or check lot have been cleared automatically, manually or, if active, with machine learning (Cash Application) dependent on various grouping and filter criteria. A list of payment lots or check lots with detailed information is also available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Incoming Payments (F5588). | The screen Analyze Incoming Payments is displayed.The number of items and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show Filter Bar | Above the chart, a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The filter bar with several filter criteria is shown. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select one or more Company Codes from the value help of the mandatory filter Company Code and then choose OK. Choose Go to enable the selection. | The chart and table will only show Lots data for the selected company code(s).The chart’s default dimension is Lot and the default measure is Payments in Clarification, Payments Posted Automatically, Payments Posted Manually and Payments Posted using Cash App.You could put your mouse on the bar in the chart, then the relevant number of payments will show up in the dialog. |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Show or Hide Legend | Choose the button Show Legend. Show or hide the legend of the chart. | The legend will be shown or hidden. |  |
| 7 | Change Settings | Above the chart on the right-hand side are several icons. Choose the button Settings to change the dimension or measure in the chart. Modify the settings; for example, select the Dimension House Bank with Role Category, and choose OK. | The chart will be adjusted. |  |
| 8 | Change View By | Choose the drop-down list of View By above the chart on the right-hand side and select an item, for example, Status. | The columns in the chart will add additional dimension, for example, the Status. |  |
| 9 | Change Chart Type | Choose the various chart types on the upper right-hand side of the chart. | The chart type will change. |  |
| 10 | Maximize the Chart | Above the chart on the right-hand side are several icons can adjust size of chart, for example. Choose the button Maximize . | The chart will be maximized. |  |
| 11 | Minimize the Chart | Choose the button Minimize. | The chart will be minimized. |  |
| 12 | Navigate to Object Page | Choose the button Details of one row in the table. | The next view displays the lot’s details information.You could display the result of clearing statistics and cash app statistics from the header information. The cash app statistics group will be invisible if the cash app process is not enabled in the system.You could also display the donut chart for Payment Usage and the chart for Clarification Progress. |  |
| 13 | Navigate Back | Choose the back button on the very upper part of the screen. | The view returns to the chart. |  |
| 14 | Save View | Choose the Select View button on the upper left-hand side. Choose Save As. Enter name like Z001 for the view and some acceptable data in the dialog box appears. Choose Save. | A new view will be created. |  |
| 15 | Save New Tile | Enter some data in the filter bar and choose the button Share and Save as tile in the upper right part. Enter some acceptable data in the dialog box and choose OK. | A new tile will be created on the Launchpad. This tile enables the analysis to be made with the settings made at the time the tile was created. |  |

### Track Worklists

#### My Open Worklists

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With the FIORI application My Open Worklists an Accounts Payable and Receivable Manager can display the results of all open worklists and their corresponding items, which have been created in the following apps:

- Analyze Overdue Items
- Analyze Open Credit Items
- Analyze Payment Run Exceptions
- Analyze Returns
- Analyze External Collections Volume

Using this app, the working status can be easily monitored, and the status of worklists and their items set to obsolete as required.

Procedure

Before worklists created in previous tests can be tracked, it is acceptable to change the process of the work items. It is therefore necessary to ensure that the user has the role SAP_BR_APR_ACCOUNTANT_FICA (Accounts Payable and Receivable Accountant (FI-CA)) assigned. Open the app Process Worklists from Analytical Apps and change some of the work items which have just been created.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open My Open Worklists (F1611A). | The screen My Open Worklists is displayed.The table shows the worklists which have been created. |  |
| 3 | Set worklists to obsolete | Select some worklists and choose Set to obsolete. | If none of the work items is in process, the whole worklist will be set to obsolete. |  |
| 4 | Display details of a worklist | Choose the title of a worklist in one row. | The items of the worklist are displayed. The last processor and the status can be seen. If the item is closed, it can be found in the list Completed. |  |
| 5 | Set items to obsolete | Select some work items and choose Set to obsolete. | The system will set the work items to obsolete, if they are not yet in process. |  |
| 6 | Navigate to other apps for a specific business partner | Select a business partner ID in one row and then navigate to a business-partner-specific app, for example, the Business Partner Financial Overview. | The Fiori App Business Partner Financial Overview opens for the selected business partner. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Contract partner and contract account have been created for posting. |
| 2BI - Contract Accounting – Customer Initiated Payments | Invoices have been created for posting and the payment run has collected the open items. Also for returns which have also been posted. |
| 2DP - Contract Accounting – Company Initiated Payments | Credits have been created and paid out to the customers. Also for returns which have also been posted. |
| 2BK - Contract Accounting – Daily and Monthly Closing | Uncollectible Receivables are written off. As well the monthly and daily closing is done (not necessary for this test script). |
| 2UJ - Contract Accounting – Open Item Management | Dunning notices are created. As well installment plans are existing. |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Scope Item | Business Condition |
| --- | --- |
|  |  |

### Analyze Collections Success

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With the FIORI application Analyze Collections Success an Accounts Payable and Receivable Manager can display an overview of the collections success (in percentage) within a certain time frame based on different kind of grouping criteria (like date of issue, collection activity, collection strategy).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze Collections Success (F2209A) . | The screen Analyze Collections Success is displayed.The percentage and the information displayed on the tile on the Launchpad home screen is consistent with the information displayed upon entering the app. |  |
| 3 | Show the Filter Bar | Above the chart a filter bar with several filter criteria is displayed. If the filter bar is hidden, click the button Expand Header above the chart. | The Compact Filter mode is selected by default.The filter bar with several filter criteria is shown.EUR is set for Display Currency by default. |  |
| 4 | Change Filter Criteria | Change the filter criteria, for example, select a special collection step from the value help of the filter Collection Step and then choose OK. Choose Go to enable the selection. | The chart and table view will only show collections data for the selected collection step(s). |  |
| 5 | Adapt Filters | Choose the button Adapt Filters. Add and remove filters on the filter bar. | The filter bar will be adjusted. |  |
| 6 | Change the Filter Mode to Visual Filter from Compact Filter | Above the filter bar on the right-hand side are several icons. Choose the second icon Visual Filter. | With the Visual Filter mode chosen, 2 filter charts will be shown. They are:Success Rate by Company CodeSuccess Rate by Segment |  |
| 7 | Adapt Filter Criteria by Using Filter Chart | Choose the value help on the top right of each filter chart, check and change the filter criteria. Choose OK after changing. | Filter criteria for each filter chart will show. The chart and table view will only show data according to the settings of filter criteria. |  |
| 8 | Configure Filter Chart by Using Adapt Filters | Choose the Adapt Filters button under the filter bar. You can choose to show and hide filter charts on the filter bar. You can also configure the sort order, chart type and measure for the filter charts. | The filter chart will be changed accordingly. |  |
| 9 | Change Grouping Criteria | Choose the Settings icon to the right of the Collections Success chart. Under the Chart tab in the View Settings dialog box, you can configure dimensions and measures for the chart. For example, remove existing dimension, add dimension Segment and choose Category for layout option. | Currently selected entries will be shown in the chart, for example, the segment. |  |
| 10 | Add Another Dimension via View By | Choose the View By icon on the top right of the chart. You can select a dimension from the drop-down list, for example, Quarter of Issue. | The dimension Quarter of Issue with Categroy chosen as the layout option is added.The chart will be adjusted. |  |
| 11 | Change Chart Type | Choose the Chart Type icon on the top right of the chart and select various chart types from the list.When you place the cursor over the button, your selected chart type will be displayed, for example, Selected Chart Type: Bar Chart. | The chart type will be changed. |  |
| 12 | Change Settings of Table | If the Collections Success table is hidden, choose the Chart and Table View icon to the right of the Collections Success chart.Choose the Settings icon to the right of the Collections Success table. Under the Columns tab in the View Settings dialog box, you can choose other available columns. You can also configure sort and group for the table Collections Success. Then choose OK. | Data of the table will be adjusted. |  |
| 13 | Restrict the View | Select one or more bars or columns from the chart. | Data of the table will be adjusted. It will only display those collections success that the bar(s) or column(s) selected. |  |
| 14 | Save a New Tile | Enter some data on the filter bar and choose the buttons Share and Save as Tile in the upper right corner. Enter some acceptable data in the dialog box appears and choose OK. | A new tile will be created on the Launchpad. It enables the analysis with the settings made when the tile was created. |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-open-item-management-2uj-ae-872-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2KH_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 129,919 chars in the whole document
