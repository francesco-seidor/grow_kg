---
id: 03-financial-accounting-and-close/customer-payments-1s0-ae-test-script-760
title: Customer Payments (1S0_AE) Test Script (1S0_S4CLD2608_BPD_EN_AE)
description: "S/4HANA Cloud test script for Customer Payments (1S0, UAE, company code 3310): sample invoice and bank statement setup, and displaying open invoices."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/accounts-receivable]
aliases: [1S0_S4CLD2608_BPD_EN_AE]
keywords: [Accounts Receivable, customer payments, open invoices, customer invoices, manual bank statement, customer payment api, master data, business conditions, business roles, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1S0_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-760
topic: 03-financial-accounting-and-close/accounts-receivable
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Customer Payments (1S0_AE) Test Script (1S0_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1S0_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Accounts Receivable** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Customer Payments (1S0_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Customer Payments (1S0_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232847484)

[2 Prerequisites 3](#_Toc232847485)

[2.1 Additional Manual Configuration 3](#_Toc232847486)

[2.2 System Access 3](#_Toc232847487)

[2.3 Roles 3](#_Toc232847488)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232847489)

[2.5 Business Conditions 5](#_Toc232847490)

[2.6 Preliminary Steps 5](#_Toc232847491)

[2.6.1 Create Invoices Manually 5](#_Toc232847492)

[2.6.2 Create a Manual Input Bank Statement (Optional) 7](#_Toc232847493)

[3 Overview Table 10](#_Toc232847494)

[4 Test Procedures 11](#_Toc232847495)

[4.1 Display Open Invoices 11](#_Toc232847496)

## Purpose

Overview

The customer payments scope item is a public cloud API solution delivered on the SAP S/4HANA Public Cloud edition for electronic bill presentment and payment.

With the new SAP S/4HANA APIs, SAP enables customers and partners to build modern customer-facing portals. These portals accelerate the invoice-to-cash process and support automated cash collection, and empower end customers with self-service capabilities, reducing manual workload while improving the customer experience.

Using the APIs available businesses can:

- Pay and manage bills: Select open items, create payments, view or cancel payments in process
- Display account statements: View and download all items for a specific time period

|  |
| --- |
| Note For more information on the API for testing purposes, see [this page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/d33c074cc9b94242a8146c313ac66889/d92bab44637343d98ef490af5c41bb75.html?version=latest) on the SAP Help Portal. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/f0f5c8b72f1d3327ca62f4ea342ebd4e)

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
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |

|  |
| --- |
| Remember Some of the procedures described are performed by the customer. Ensure you have the appropriate access, with username and password, created and in place for your customer usage of the system. |

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
| Currency | AED |  |  |
| G/L Account | 41000400 |  |  |
| House Bank | AEBK1 |  |  |
| House Bank Account ID | AEAC1 |  |  |
| Cash Management Account | AE-BK1-AC1 |  |  |
| Payment Method | M (Direct Debit Payments) |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Business Condition | Comment |
| --- | --- |
| Sell from Stock (BD9) | A customer invoice must be available for the test procedures. When there are no existing open customer items, you must create a billing document. Follow the procedures in either of these test scripts to create a customer invoice.When creating a customer invoice, note the amount and Reference Document Number (XBLNR in the header). The information is required when simulating a manual bank statement. In the bank statement, a credit item can be reconciled with the customer invoice. |
| Accounts Receivable (J59) | Perform the Enter Invoice without Sales Order procedure and the Invoice Collection Preparation procedure in the test script to create outgoing invoices, import manually, and display invoices. |

### Preliminary Steps

#### Create Invoices Manually

Purpose

In this activity, you post customer invoices in accounting. Journal entries are created.

Prerequisites

A customer master record is entered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Outgoing Invoices (FB70). | The Enter Customer Invoice view is displayed. |  |
| 3 | Company Code | Choose the Company Code tab. |  |  |
| 4 | Company Code | Make the following entries and press Enter:Company Code: 3310 |  |  |
| 5 | Basic Data | Make the following entries:Customer: 33100010Invoice date: <Today’s date>Posting date: Today’s dateReference: <any>Amount: <any>Note There's an upper limit for payment via credit card. For testing purposes, keep the invoice amount below 500.Document Currency : <co.code currency>Calculate Tax : Selected |  |  |
| 6 | Payment | Choose the Payment tab.Make the following entries:Bline Date : <Today’s date>Payt Terms: 0001Payt Meth. : <optional> |  |  |
| 7 | Line Items | In the Items table, make the following entries:G/L Acct : 41000400D/C : CreditAmount in Document Currency: <any>Note There's an upper limit for payment via credit card. For testing purposes, keep the invoice amount below 500.Tax Code : <Output/Sales tax code> |  |  |
| 8 | Profitability Segment | In the Profit.segment column, select the button and enter:Customer: <customer number>Profit Center: <any>Choose Derivation and choose Continue. |  |  |
| 9 | Post | Choose Post. | The journal entry is posted. |  |

#### Create a Manual Input Bank Statement (Optional)

Purpose

In this activity you can create a credit balance if it isn't available in the system. Complete the steps before assigning the payment method of matching payment to invoices.

Prerequisite

When you create an incoming payment item in a manual bank statement, enter the customer number and text in the memo line that is displayed in the Match Payments app, with invoices (in our example, manual transaction F001 with interpretation algorithm 001).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Management Specialist. |  |  |
| 2 | Access the SAP Fiori app | Open Manage Bank Statements (F1564). |  |  |
| 3 | Get Latest Bank Statement Number | To get the latest imported bank statement number, make the following entries and choose Go:Editing Status: AllLatest Statements: SelectedLatest OnlyCompany Code: 3310House Bank: AEBK1House Bank Account: AEAC1Note If any selection criterion is invisible, choose Adapt Filter to add it to filter bar. | The latest bank statement number of the specified bank account displays.Note The next bank statement number is one greater than the latest bank statement number. For example, if the latest bank statement number is 5, the next number is 6. If no latest bank statement found, the next number should be 1. |  |
| 4 | Note Closing Balance | Make note of the closing balance of the specified bank account, found on the Manage Bank Statements view. | The closing balance of the latest bank statement should be the opening balance of the next bank statement. Get Closing Balance of Latest Bank StatementIf no latest bank statement is found, the opening balance of the next bank statement should be zero. |  |
| 5 | Create New Bank Statement | Choose the + button to Create Bank Statement.On the Bank Statement view, make the following entries:House Bank Account: AEAC1House Bank: AEBK1Company Code: 3310Bank Statement No.: Enter the next Bank Statement Number, for example, 6Bank Statement Date: For example, <Current Date>Choose Enter to determine the currency of this house bank before entering opening or closing balances.Opening Balance: For example, 5002.00Closing Balance: For example, 4019.00 | The data of bank statement header is entered.The opening balance is the closing balance of latest imported bank statement, for example, 5002.00.Remember Get Closing Balance of Latest Bank. The closing balance = opening balance - debit amount + credit amount, for example, 4019.00 = 5002.00 + 208.00 - 1191.00. |  |
| 6 | Create First Bank Statement Item | On the Bank Statement view, choose the + button in the Bank Statement Items area to create the first item.On the New Object 1 view, make the following entries:Manual Transaction: F001Value Date: For example, <current date>Amount: Enter the receivable amount of customer invoice as described in Prerequisites, for example, 208.00Customer: 33100010Memo: Enter descriptive text in the memo line, for example, payment for multiple invoices .Choose the Apply button. | The first bank statement item is entered and you automatically return to the previous Bank Statement view. |  |
| 7 | Save the Bank Statement | On the Bank Statement view, choose Save.An Information dialog box displays the message Bank Statement 6 for bank account ... at bank ... created successfully. Choose Close. | The statement status is Saved. |  |
| 8 | Post the Bank Statement | On the Bank Statement view, choose Post.The Information dialog box displays the message Statement posted: all items completed. Choose Close. | The statement status changes from Saved to Not Completed.Journal Entry is:Posting Area 1 - Bank Accounting:Dr: Bank main accountCr: Bank subaccountPosting Area 2 - Sub ledger Accounting:Dr: Bank subaccountCr: Accounts receivable - customer (with clearing). |  |

## Overview Table

This test script consists of several process steps and reports provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report, or Item | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Display Open Invoices](#unique_11) [page ] 11 | Accounts Receivable Accountant | Manage Customer Line Items (F0711) | You displayed open invoices. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Display Open Invoices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display line items for a customer account.

Prerequisite

Invoices are available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Line Items (F0711). |  |  |
| 3 | Enter Search Criteria | Make the following entries:Customer: 33100010Company Code: 3310 |  |  |
| 4 | Status | Choose your status.If you choose All Items, the system displays all the account items.Choose Open items for a list of open invoices. |  |  |
| 5 | Date and Item Type | Make the following entries:Open at key date: <Today’s date>Item type: Normal Items |  |  |
| 6 | Execute Search | Choose Go. | The customer line items display according to your search criteria. |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounts-receivable-j59-a]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1S0_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 18,310 chars in the whole document
