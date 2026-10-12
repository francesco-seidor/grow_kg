---
id: 08-sales-order-management/external-digital-payments-2lz-ae-test-script-833
title: External Digital Payments (2LZ_AE) Test Script (2LZ_S4CLD2608_BPD_EN_AE)
description: "Test script for scope item 2LZ_AE External Digital Payments in SAP S/4HANA Cloud Public Edition: prerequisites, AR/GL jobs, advice processing, card data."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/digital-payments]
aliases: [2LZ_S4CLD2608_BPD_EN_AE]
keywords: [Digital Payments and Card Payments in Sales, external digital payments, sap digital payments, advice processing, payment card settlement, automatic clearing, payment card data, test prerequisites, business roles, sample master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LZ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-833
topic: 08-sales-order-management/digital-payments
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# External Digital Payments (2LZ_AE) Test Script (2LZ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LZ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Digital Payments and Card Payments in Sales** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| External Digital Payments (2LZ_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | External Digital Payments (2LZ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232849598)

[2 Prerequisites 3](#_Toc232849599)

[2.1 System Access 3](#_Toc232849600)

[2.2 Roles 3](#_Toc232849601)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232849602)

[2.4 Business Conditions 5](#_Toc232849603)

[2.5 Preliminary Steps 5](#_Toc232849604)

[2.5.1 Create Invoices Manually 5](#_Toc232849605)

[2.5.2 Display Open Invoices 6](#_Toc232849606)

[2.5.3 Create Bank and Bank Account 7](#_Toc232849607)

[3 Overview Table 9](#_Toc232849608)

[4 Test Procedures 10](#_Toc232849609)

[4.1 Schedule Accounts Receivable Jobs – Settlement External Payment 10](#_Toc232849610)

[4.2 Schedule Accounts Receivable Jobs - External Payment Method 11](#_Toc232849611)

[4.3 Schedule General Ledger Jobs - Automatic Clearing 13](#_Toc232849612)

[4.4 Display Payment Card Data 14](#_Toc232849613)

[5 Appendix 16](#_Toc232849614)

[5.1 Succeeding Processes 16](#_Toc232849615)

## Purpose

Overview

SAP digital payments is a payment hub that connects payment service providers (PSP) and SAP components, solutions, or applications that need to process incoming credit card or external payments.

The scope item enables the integration between SAP S/4HANA Cloud Public Edition and SAP digital payments. With this, you can use external payment methods in SAP S/4HANA Cloud Public Edition for incoming payments.

The entire process from payment advice processing via the SAP digital payments application jobs to automatic clearing and the final bank statement upload is covered and automated.

Various payment service providers are supported.

|  |
| --- |
| Caution The test procedure steps in this test script are only for productive customers with upstream systems for external payments, not for internal, demo, or starter systems. |

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
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Customer | 33100010 |  |  |
| G/L Accounts | 1253010012530110 |  |  |
| Bank | Use an External Payment bank |  |  |
| House Bank | AEEP1 |  |  |
| House Bank Account | AEEPA |  |  |
| Payment Method | L (External Payments) |  |  |
| Currency | AED |  |  |
| Payment Method | L when using external payment |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNG | Create G/L Account and Cost Element - MDS |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Business Condition | Comment |
| --- | --- |
| Digital Payments (1S2) | Required integration must be enabled using the Setting Up Digital Payments (1S2) setup instructions guide. Follow the activities in the guide before proceeding with this test script. |
| Sell from Stock (BD9) | A customer invoice must be available for the test procedures. When there are no existing open customer items, you must create a billing document. Follow the procedures in either of these test scripts to create a customer invoice.When creating a customer invoice, note the amount and Reference Document Number (XBLNR in the header). The information is required when simulating a manual bank statement. In the bank statement, a credit item can be reconciled with the customer invoice. |
| Accounts Receivable (J59) | Perform the Enter Invoice without Sales Order procedure and the Invoice Collection Preparation procedure in the test script to create outgoing invoices, import manually, and display invoices. |

### Preliminary Steps

#### Create Invoices Manually

Purpose

In this activity, you post customer invoices in accounting. Journal entries are created.

Prerequisites

A customer master record has been entered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Outgoing Invoices (FB70). | The Enter Customer Invoice view displays. |  |
| 3 | Company Code | Choose the Company Code button. On the dialog box, enter your company code and choose Continue. |  |  |
| 4 | Basic Data | Choose the Basic Data tab.Make the following entries:Customer: 33100010Invoice date: <Today’s date>Posting date: Today’s dateReference: <any>Amount: <any>Document Currency : <co.code currency>Calculate Tax : Selected |  |  |
| 5 | Payment | Choose the Payment tab.Make the following entries:Bline Date : <Today’s date>Payt Terms: 0001 |  |  |
| 6 | Line Items | In the Items table at the bottom of the screen, make the following entries:G/L Acct : 41000400D/C : CreditAmount in Document Currency: <any>Tax Code : <Output/Sales tax code> |  |  |
| 7 | Profitability Segment | In the Profit.segment column, select the button and enter:Customer: <customer number>Profit Center: <any>Choose Derivation and then choose Continue. |  |  |
| 8 | Post | Choose Post to save. | The journal entry is posted. |  |

#### Display Open Invoices

Purpose

In this activity, you display line items for a customer account.

Prerequisite

Invoices are available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Line Items (F0711). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Customer: 33100010Company Code: 3310Status: <see note>Note If you choose All Items, the system displays all the account items.To see a lsit of open invoices, choose Open items.Open on Key Date: <Today’s date>Item Type: Normal Items | The customer line items display according to your search criteria. |  |

#### Create Bank and Bank Account

Purpose

In this step, you create standard banks and internal bank master data with general information. You also create bank accounts.

|  |
| --- |
| Note This preliminary step is only for productive systems, not internal, demo, or starter systems. |

Procedure

For more information on setting up banks, see the Basic Bank Account Management (BFA) test script.

| Process Step | Fiori App | Values to Use | Comments |
| --- | --- | --- | --- |
| Test Procedures > Bank Account Master Data Processing with Basic Bank Account Management > Using Direct Revision Activate → Create Bank Account > Create Bank Master Data | Manage Banks - Master Data (F6437)Caution Choose Create Internal Bank. | Bank Key: <use your own bank key>Bank Number: <use your own bank number>Internal Bank Category: Payment Service Provider (3)Bank Name: <use your own bank name> |  |
| Test Procedures > Bank Account Master Data Processing with Basic Bank Account Management > Using Direct Revision Activate → Create Bank Account > Manage Banks Cash Management Data | Manage Banks - Cash Management (F1574A) | Use the Bank Key value above.Under House Banks, choose CreateCompany Code: <company code>House Bank: <use your own house bank> |  |
| Test Procedures > Bank Account Master Data Processing with Basic Bank Account Management > Using Direct Revision Activate → Create Bank Account > Create Bank Account | Manage Bank Accounts (F1366A) | Choose Create. Enter your company code and Account Type: 20 (PSP Account Type) and choose Continue.Account Description: <account description>Use the Bank Key value above.Use a valid value for Account Number.Under House Bank Connectivity, choose Create.House Bank Account: <house bank account>G/L Account: <G/L account>On the Bank Relationship tab, make the following entry:Pmnt Tran Type Group: CAMT053 |  |

## Overview Table

The External Digital Payments (2LZ) test script consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2:

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Schedule Accounts Receivable Jobs – Settlement External Payment](#unique_11) [page ] 10 | Accounts Receivable Accountant | Schedule Accounts Receivable Jobs (F2366) | You scheduled the credit card payments. |
| [Schedule Accounts Receivable Jobs - External Payment Method](#unique_12) [page ] 11 | Accounts Receivable Accountant | Schedule Accounts Receivable Jobs (F2366) | You scheduled the advice processing. |
| [Schedule General Ledger Jobs - Automatic Clearing](#unique_13) [page ] 13 | General Ledger Accountant | Schedule General Ledger Accounting Jobs (F1927) | You scheduled the automatic clearing job. |
| [Display Payment Card Data](#unique_14) [page ] 14 | Accounts Receivable Accountant | Display Payment Card Data (F2935) | You displayed the payment card data. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Caution The following test procedure steps are only for productive customers with upstream systems for external payments, not for internal, demo, or starter systems. |

### Schedule Accounts Receivable Jobs – Settlement External Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you schedule the settlement of external payments.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Schedule Accounts Receivable Jobs (F2366). |  |  |
| 3 | Create a New Job | Choose Create. | The New Job view displays. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Payment Card SettlementJob Name: Payment Card Settlement |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Parameters | Make the following entries and choose Schedule:Company Code: 3310G/L Account: 12530110Journal Entry Type: SAJournal Entry Date: <current date>Posting Date: <current date>Update Run: Selected | The job is created and starts immediately. |  |
| 7 | Review Job Status | When the job is complete, the Application Jobs view displays. Review the job log.Note The job log only displays when there is a credit card settlement. |  |  |

### Schedule Accounts Receivable Jobs - External Payment Method

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The following procedure provides a description for scheduling accounts receivable jobs for external payment methods.

Prerequisites

The external electronic fund transfer system is configured to integrate with SAP S/4HANA.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accounts Receivable Jobs (F2366). | The Application Jobs view displays. |  |
| 3 | Create a New Job | Choose Create. | The New Job view displays. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: SAP Digital Payments: Advice ProcessingJob Name: SAP Digital Payments: Advice Processing |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Parameters | Make the following entries and choose Schedule:Bank Country/Region: for example AEBank Key:18121996Transactions From: for example, <current date>Transactions To: for example, <current date>Note For the dates in the two fields above, use the date of the payment.Digital Payment Method: EPPayment Service Provider: For example, DPPPMerchant Alias: Use the value help to choose, for example, 18121996Reconciliation: DeselectedNote Reconciliation means that the advice data is only returned once. If you create another run for the same time frame and no additional data is provided by the payment service providers, no advice data is returned. In a situation where data is necessary for SAP S/4HANA (for example, when postings of the advice were wrong and have been reversed), the reconciliation flag is set so all advice data for the date / payment service provider / merchant selection is returned. | A list of Jobs displays. |  |
| 7 | Review Job Status | Double-click the icon in the Log column. Review the log details in the view that displays.Note An icon in the Log column only displays if there is incoming advice. |  |  |

### Schedule General Ledger Jobs - Automatic Clearing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule general ledger jobs for automatic clearing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Schedule General Ledger Accounting Jobs (F1927). | The Application Jobs view displays. |  |
| 3 | Create a New Job | Choose Create. | The New Job view displays. |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: Automatic ClearingJob Name: Automatic Clearing |  |  |
| 5 | Scheduling Options | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Parameters | Make the following entries and choose Schedule:General Selections section:Company Code: 3310G/L Selections section:Select G/L Accounts: SelectedG/L Account: 12530100Posting Parameters section:Clearing Date: <current date> | The job is created and started immediately. After the job completes, the Application Jobs view displays. |  |
| 7 | Review Job Status | Review the job log.Note The job log displays only when there are documents available for automatic clearing. |  |  |

### Display Payment Card Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display payment card data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Payment Card Data (F2935). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Authorization Date and Time: For example, choose the field help, and from the Time Period dialog box, select Date Range.Enter: 01/07/2019 - 01/11/2019Customer: For example, 33100010Company Code: For example, 3310 | The list of Card Payments displays. |  |
| 4 | Drilldown Display | Choose a row of a journal entry to display detailed payment card data. You can drilldown into the data in the entry details view. | The detailed payment card data for the selected row is displayed on the right side of the view.Note If there is no settlement for the payment, the Settlement section and Settlement Run section aren't displayed. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Basic Cash Operations (BFB) | Follow the procedures for Bank Statements, including the sub-steps, to upload incoming bank statements. |
| Accounting and Financial Close (J58) | Follow the procedures for the Clear G/L Accounts - Manual Clearing (F1579) app |

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
- related-to :: [[08-sales-order-management/test-script-digital-payments-foundation-53v-1062]]
- related-to :: [[08-sales-order-management/test-script-digital-payments-sales-1z1-ae-sap-s-4hana-cloud-public-edi]]
- related-to :: [[08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-digital-payments-1s2-ae-7]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2LZ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 23,884 chars in the whole document
