---
id: 03-financial-accounting-and-close/provisioning-of-overdue-receivables-2pd-ae-test-script-847
title: Provisioning of Overdue Receivables (2PD_AE) - Test Script (2PD_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script (2PD, AE) for IFRS 9 provisioning of overdue receivables: valuation run, doubtful debts analysis, bad debt write-off."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/overdue-receivables-provisioning]
aliases: [2PD_S4CLD2608_BPD_EN_AE]
keywords: [Provisioning of Overdue Receivables (IFRS 9), overdue receivables provisioning, valuation run, doubtful debts analysis, bad debt write-off, expected credit losses, value adjustment key, customer master data, business roles, advanced foreign currency valuation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2PD_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-847
topic: 03-financial-accounting-and-close/overdue-receivables-provisioning
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Provisioning of Overdue Receivables (2PD_AE) - Test Script (2PD_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2PD_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Provisioning of Overdue Receivables (IFRS 9)** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Provisioning of Overdue Receivables (2PD_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232849865)

[2 Prerequisites 3](#_Toc232849866)

[2.1 System Access 3](#_Toc232849867)

[2.2 Roles 3](#_Toc232849868)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232849869)

[2.4 Business Conditions 4](#_Toc232849870)

[2.5 Preliminary Steps 5](#_Toc232849871)

[2.5.1 (Optional) Create New Valuation Adjustment Key 5](#_Toc232849872)

[2.5.2 Complete Customer Master Data 6](#_Toc232849873)

[3 Overview Table 8](#_Toc232849874)

[4 Test Procedures 9](#_Toc232849875)

[4.1 Valuation Run 9](#_Toc232849876)

[4.2 Analyze Doubtful Debts 12](#_Toc232849877)

[4.3 Bad Debt Write-Off 13](#_Toc232849878)

## Purpose

Overview

Due to the new impairment model of IFRS 9, Expected Credit Losses (ECL) on Trade Receivables are calculated using a provision matrix, where fixed provision rates apply depending on the number of days that trade receivable is outstanding. For the calculation of the provisioned amounts, you can periodically perform a valuation run to calculate the bad debt expense posting for overdue items. If you agree with the proposal of the valuation run, you can transfer the valuation to the general ledger to generate the postings. The system makes the adjustment posting for the relevant key date and reversal postings for the date after the key date.

|  |
| --- |
| Note If Advanced Foreign Currency Valuation is activated, the SAP Fiori apps in the test script are not functional. For more information about Advanced Foreign Currency Valuation, see the Accounting and Financial Close (J58) test script. |

|  |
| --- |
| Restriction Advanced Foreign Currency Valuation is not set to active by default. If it is set active, classical reclassification does not work. |

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
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| (Optional)Configuration Expert - Business Process Configuration(Only required when modifying SSCUI to add a new valuation adjustment key) | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Customer | 3310000133100002 |  |  |
| Value Adjustment | R1 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J14 - Sales Order Processing – Project-Based Services | Must be run before this test script. Invoices have been created and posted to accounting. |
| BD9 - Sell from Stock | Must be run before this test script. Invoices have been created and posted to accounting.Caution Not valid for SAP S/4HANA Professional Services Cloud. |
| BDN - Sales of Non-Stock Item with Order-Specific Procurement | Must be run before this test script. Invoices have been created and posted to accounting. |
| J59 - Accounts Receivable | Must be run before this test script. Invoices have been created and posted to accounting. |
| J58- Accounting and Financial Close | Perform Foreign Currency Valuation procedure is executed. |

### Preliminary Steps

#### (Optional) Create New Valuation Adjustment Key

Context

As an option, you can create a value adjustment key.

|  |
| --- |
| Posting Instructions Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Configure Your Solution:Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Open Manage Your Solution (F1241).If necessary, change the country or region by choosing Set Local Version.Choose Configure Your Solution.Make the following entries:Application Area: FinanceSub Application Area: Accounts ReceivableFor the row with Item Name of Valuations, choose Details (>).For the Define Value Adjustment Key row, choose Configure.Create the value adjustment key and save your entries.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Value Adjustment Key.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Create the value adjustment key and save your entries. |

#### Complete Customer Master Data

Purpose

In this activity, you execute the allowance for doubtful debt step. You must assign a value adjustment to a customer.

Prerequisites

- The customer master record is created.
- Value adjustment keys are defined.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner (BP) view is displayed. |  |
| 3 | Select Customer | Make the following entry and choose Enter:Business Partner : 33100001 | The Display Organization : 33100001 view is displayed. |  |
| 4 | Change Role | Make the following entry :Display in BP role : Customer(Fin. Accounting) | The Display Organization : 33100001, role FI Customer view is displayed. |  |
| 5 | Edit Customer | Choose the Switch between Display and Change button to change the data to update. |  |  |
| 6 | Company Code data | Choose the Company Code button.Choose the Customer: Account Management tab. |  |  |
| 7 | Value Adjustment | In the Account Management section, make the following entry and choose Save:Value Adjustment: R1 | The value adjustment is assigned to the customer. |  |

## Overview Table

The scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Valuation Run](#unique_10) [page ] 9 | General Ledger Accountant | Perform Further Valuations (F107) | The valuation run is completed. |
| [Analyze Doubtful Debts](#unique_11) [page ] 12 | Accounts Receivable Accountant | Doubtful Accounts Valuation (F3246) | Doubtful accounts are displayed. |
| [Bad Debt Write-Off](#unique_12) [page ] 13 | Accounts Receivable Accountant | Clear Incoming Payments - Manual Clearing (F0773) | Bad debt is written off. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Valuation Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you make allowance for doubtful receivables valuation postings.

|  |
| --- |
| Caution If Advanced Foreign Currency Valuation is activated, the Perform Further Valuations (F107) app and process doesn’t work. For more information about Advanced Foreign Currency Valuation, see the Accounting and Financial Close (J58) test script. |

Prerequisites

- Execute the Perform Foreign Currency Valuation test procedure from the Accounting and Financial Close (J58) scope item. Posting Date and Reversal Posting Date used for the Perform Further Valuations (F107) app must be the same values used in Perform Foreign Currency Valuation.
- Open receivables exist in the system that satisfy the valuation adjustment key requirements, based on number of days overdue. The creation of the valuation adjustment key is maintained in the [(Optional) Create New Valuation Adjustment Key](#unique_7) [page ] 5 step (in Prerequisites > Preliminary Steps).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Perform Further Valuations (F107). | The Valuation Run: Initial Screen view displays. |  |
| 3 | Initial Data Entry | Make the following entries and choose Maintain:Run Date: <today's date>Identification: For example, any five character description, such as SAPY1 | The Valuation: Parameters view displays. |  |
| 4 | Parameters Data Entry | Make the following entries:Key Date: <key date>Val. Method: 3Currency Type: 10Valuation Area: For example, AEPostings: SelectedPosting Date: <today's date>JE Type: SARev.Post.Date: <today's date + 1>JE Type: SAValuation for Each Line Item: Selected |  |  |
| 5 | Selection Options | Choose the Selection options button. | The FI Valuation Program (Individual Value Adjustment Discounting) view is displayed. |  |
| 6 | Customer | Make the following entries and choose Execute:Customers: Select the checkbox and enter 33100001 |  |  |
| 7 | Save | Choose Save. | The Valuation Run: Initial Screen view displays with Status as Parameters entered. |  |
| 8 | (Optional) Delete Parameters | Caution Once postings are made, parameters can’t be deleted.This step is optional.Before posting, if the parameters must be deleted, choose Menu > Edit > Parameters > Delete. The system displays a dialog box with the notification Do you want to delete all the parameters?.Choose Yes.After parameters are deleted, return to the previous Initial Data Entry step to create a new valuation run. | Parameters are deleted for the valuation run and a confirmation notification displays.The Status changes to No parameters entered as yet. |  |
| 9 | Dispatch Valuation Run | Choose Dispatch. | The Valuation selection has been scheduled notification displays at the bottom of the view and the Status changes to:Val.run scheduled for <Run date and Time>Val.running |  |
| 10 | Complete Valuation Run | To change Status to Val.run Finished and complete the valuation run, choose Enter. | Status changes to Val.run Finished. |  |
| 11 | Display Valuation Run | Choose Display to review the valuation run. When your review is complete, choose the Exit button to return to the Valuation Run: Initial Screen. | The FI Valuation Lists view displays with details of the invoice documents selected in the run. |  |
| 12 | (Optional) View Sample Posting | Choose Menu > Edit > Valuation Transfer > Sample Posting to view a simulation of the posting. | Posting Documents (Simulations) view displays. |  |
| 13 | (Optional) Delete Valuation Run | Caution Once postings are made, the valuation run can’t be deleted.Before posting, if any changes are required for the valuation run, you must delete the executed run and start over.From the Valuation Run: Initial Screen, choose Delete Run.A Do you want to delete selection valuation balance? dialog box appears.Choose Yes.The valuation run you created is deleted.Return to the previous Valuations Data Entry step to begin a new valuation run. | The valuation run data is deleted for Run Data and an identification notification displays.The Status changes to Parameters entered. |  |
| 14 | Post Valuation Run | Caution This step posts the accounting entries. After you execute this step, no changes can be made to the parameters nor can the valuation run be deleted.To post the valuation run, choose Forward and a dialog box appears. Check the box for Start Immediately and choose the Dispatch button. | The Valuation transfer has been scheduled notification displays.The Status changes to:Transfer scheduled for Run data at TimeTransfer running |  |
| 15 | Complete Posting | To complete the posting, choose Enter. | The Status changes to Transfer finished. |  |
| 16 | (Optional) View the Log | To review the Valuation Transfer Log, choose Menu > Edit > Valuation Transfer > Display Log | The job log entries for the valuation run display. |  |

### Analyze Doubtful Debts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the overdue receivables and their associated allowances, and you can drill down for details of individual customer accounts at journal entry level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Doubtful Accounts Valuation (F3246). | The Doubtful Accounts Valuation (F3246) view is displayed. |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Key Date: For example, <Current date>Net Due Interval 1: For example, 30Net Due Interval 2: For example, 60Net Due Interval 3: For example, 90Display Currency: AEDValuation Area: IFCompany Code: 3310 | A chart and table for Coverage displays with your search criteria. |  |
| 4 | Explore Doubtful Accounts | To explore your options, use the dropdown menu and select one of the following for viewing a graph:By CustomerBy Country/RegionBy Credit Risk ClassBy Dunning BlockOther buttons allow different options around how the data is visualized in charts or tables. | A graph or list is displayed according to your selections. |  |
| 5 | Drill Down | The Customers table provides a list of customers. By selecting a customer from the Customer column, a dialog box appears with customer details. Links are provided to drill down and either review or execute further activities for this customer, for example:Clear Incoming PaymentsCustomer MasterDisplay Customer BalancesManage Customer Line ItemsPost Incoming PaymentsProcess Receivables by CustomerIf you select one of those links, a new view displays allowing additional activities. Choose the < (Back) button to return to the list.Note By choosing the More Links, you can customize the Link List to add or remove activities that display in the dialog box. | Additional review or activities are completed. |  |

### Bad Debt Write-Off

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Bad debt is a loss that a company incurs when credit that has been extended to customers becomes worthless, either because the debtor is bankrupt, has financial problems, or because it cannot be collected. It is expensed on the income statement. Recognizing bad debt leads to an offsetting reduction to accounts receivable on the balance sheet – though businesses retain the right to collect funds should the circumstances change.

In this activity, you select customer invoices that are unrecoverable and post financial entries.

Prerequisites

Invoices are created but are not recoverable.

You must have customers in financial trouble with debit balances that have to be zeroed out on the balance sheet.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear Incoming Payments - Manual Clearing (F0773). |  |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Company Code: 3310Posted By: <date>Note The default posting/journal entry date is taken from the original document. If the fiscal period of the original posting date is closed, the current date is displayed by default. This behavior is intentional, and is aligned with the principle of posting the document in time with the business related event.Line Item Type: Normal Open ItemsNote Deselect any other checkboxes in the Line Item Type dropdown. The Normal Open Items selection must be used to write off the receivable for a bad debt invoice. | The Standard pane displays a list of matching items. |  |
| 4 | Details | Toggle the Transfer Posting to ON, then choose Details (>) for one of the rows. | The Open Item XXXXXXXXXX view is displayed. |  |
| 5 | Enter Data | Make the following entries:Journal Entry: DANote The Transfer Posting toggle must be set to on to process the bad debt write-off. |  |  |
| 6 | Post to G/L Account | Choose the Post to G/L Account tab. |  |  |
| 7 | Enter Data and Simulate | Make the following entries and choose Simulate:G/L Account: <account>, for example, 62000000Debit Amount: <debit amount>Tax Code: <relevant tax code>Account Assignment area:Cost Center: <cost center> | The system displays the simulated posting. The bad debt write-off is indicated with posting key 17 (clearing). |  |
| 8 | Post | Once you review and confirm the journal entry, choose Post. |  |  |

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
- see-also :: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounts-receivable-j59-a]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2PD_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 24,727 chars in the whole document
