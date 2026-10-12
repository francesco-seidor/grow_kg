---
id: 03-financial-accounting-and-close/bill-of-exchange-1wq-ae-test-script-sap-s-4hana-cloud-public-edition-7
title: "Bill of Exchange (1WQ_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1WQ_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 1WQ_AE (UAE): bill of exchange / postdated check receivable processing in SAP S/4HANA Cloud Public Edition 2608, with prerequisites and 10 procedures."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/bills-of-exchange]
aliases: [1WQ_S4CLD2608_BPD_EN_AE]
keywords: [Bills of Exchange and Postdated Checks, bill of exchange, postdated checks, check presentation, bounced checks, bill of exchange portfolios, check reversal, bill of exchange list, bank account configuration, test prerequisites]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WQ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-772
topic: 03-financial-accounting-and-close/bills-of-exchange
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Bill of Exchange (1WQ_AE) - Test Script, SAP S/4HANA Cloud Public Edition (1WQ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WQ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Bills of Exchange and Postdated Checks** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Bill of Exchange (1WQ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847797)

[2 Prerequisites 4](#_Toc232847798)

[2.1 System Access 4](#_Toc232847799)

[2.2 Roles 4](#_Toc232847800)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232847801)

[2.4 Business Conditions 6](#_Toc232847802)

[2.5 Preliminary Steps 7](#_Toc232847803)

[2.5.1 Create Customer Invoices 7](#_Toc232847804)

[3 Overview Table 8](#_Toc232847805)

[4 Test Procedures 9](#_Toc232847806)

[4.1 Check for Banking Discounting/Collection G/L Accounts 9](#_Toc232847807)

[4.2 Post Incoming Payment with Check 10](#_Toc232847808)

[4.3 Present a Check to a Bank or Vendor 11](#_Toc232847809)

[4.4 Clear a Check Presented to a Bank or Vendor 13](#_Toc232847810)

[4.5 Bounced Check at a Bank or Vendor 14](#_Toc232847811)

[4.6 Bounced and Cleared 15](#_Toc232847812)

[4.7 Remove a Check from a Portfolio 17](#_Toc232847813)

[4.8 Add a Check to a Portfolio 18](#_Toc232847814)

[4.9 Reverse Check 19](#_Toc232847815)

[4.10 Create Check List 21](#_Toc232847816)

## Purpose

Overview

This scope item covers the use of bills of exchange for managing incoming or outgoing payments.

As a customer (debtor), you can pay your open invoices with a bill of exchange (payable). You create a bill of exchange (payable), sign it, and send it to your business partner. Alternately, your supplier can request a bill of exchange. Using SAP S/4HANA Cloud Public Edition, you can post your outgoing payments and clear your paid invoices.

If you are the supplier (creditor) and receive a bill of exchange, you can either collect the receivables at due date (collection) or cash the outstanding receivables before due date (discounting). The received bill of exchange is presented to your bank. Using SAP S/4HANA Cloud Public Edition, the respective G/L accounts are used to maintain your emerging liabilities. These liabilities are reversed after you received the payment from your bank.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Accounts Receivable Accountant for United Arab Emirates | SAP_BR_AR_ACCOUNTANT_AE | Accounts Receivable | SAP_FIN_SPT_AR_ACCOUNTING_GLO_PC |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| House Bank | AEBK2 |  | Bank for the test of bill of exchange receivable |
| Account ID | AEAC2 |  | Bank for the test of bill of exchange receivable |
| Bank – Bank (Main) Account | 11001000 |  | Note Use 11002000 if you are not using New Bank Ledger. |
| Bank – BoE Out | 11001055 |  | Note Use 11002055 if you are not using New Bank Ledger. |
| Bank – BoE Out (Balance Sheet) | 11009355 |  | Note Use 11002055 if you are not using New Bank Ledger. |
| Bank – BoE Collection | 11001065 |  | Note Use 11002065 if you are not using New Bank Ledger. |
| Bank – BoE Discounting | 11009366 |  | Note Use 11002066 if you are not using New Bank Ledger. |
| Bank – Forfeiting | 11009367 |  | Note Use 11002067 if you are not using New Bank Ledger. |
| Supplier | 33300001 for Company Code 3310 |  | Supplier for Present to Vendor step |
| Receivables Domestic G/L Account | 12100000 |  | Customer reconciliation account |
| Bill of Exchange Receivable G/L Account | 12510000 |  | Customer alternative reconciliation account, special G/L indicator W |
| Bounced Bill of Exchange Receivable Account | 12511000 |  | Customer alternative reconciliation account, Special G/L Indicator W, Portfolio 2 |
| Customer | 33100003 for Company Code 3310 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| Master Data Script | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J59 - Accounts Receivable | Must be run before this test script. Customer invoices are posted to accounting. |

### Preliminary Steps

#### Create Customer Invoices

Purpose

Customer invoices to be paid with bill of exchange receivable created in the system.

Procedure

In the Accounts Receivable (J59) test script, refer to the Enter Invoice without Sales Order process step.

Result

Customer Invoices are created.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Check for Banking Discounting/Collection G/L Accounts](#unique_9) [page ] 9 | Cash Manager | Manage Bank Accounts (F1366A) |  |
| [Post Incoming Payment with Check](#unique_10) [page ] 10 | Accounts Receivable Accountant for United Arab Emirates | Receive Bill of Exchange (F-36) |  |
| [Present a Check to a Bank or Vendor](#unique_11) [page ] 11 | Accounts Receivable Accountant for United Arab Emirates | Bill of Exchange Transactions (FTR03) |  |
| [Clear a Check Presented to a Bank or Vendor](#unique_12) [page ] 13 | Accounts Receivable Accountant for United Arab Emirates | Bill of Exchange Transactions (FTR03) |  |
| [Bounced Check at a Bank or Vendor](#unique_13) [page ] 14 | Accounts Receivable Accountant for United Arab Emirates | Bill of Exchange Transactions (FTR03) |  |
| [Bounced and Cleared](#unique_14) [page ] 15 | Accounts Receivable Accountant for United Arab Emirates | Bill of Exchange Transactions (FTR03) |  |
| [Remove a Check from a Portfolio](#unique_15) [page ] 17 | Accounts Receivable Accountant for United Arab Emirates | Bill of Exchange Transactions (FTR03) |  |
| [Add a Check to a Portfolio](#unique_16) [page ] 18 | Accounts Receivable Accountant for United Arab Emirates | Bill of Exchange Transactions (FTR03) |  |
| [Reverse Check](#unique_17) [page ] 19 | Accounts Receivable Accountant for United Arab Emirates | Reverse Bill of Exchange Transactions (FTR04) |  |
| [Create Check List](#unique_18) [page ] 21 | Accounts Receivable Accountant for United Arab Emirates | Bill of Exchange List (FTR02) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Check for Banking Discounting/Collection G/L Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you associate the Discounting/Collection G/L accounts to the House Bank and Account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cash Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Accounts (F1366A). | The Manage Bank Accounts view displays. |  |
| 3 | Data Entry | Make the following entries and choose Go:House Bank: AEBK2House Bank Account: AEAC2Company Code: 3310 | The Bank Accounts data displays. |  |
| 4 | Select | Select the bank account. | The system displays the bank account details. |  |
| 5 | Select | Select the connectivity path of the bank account. | The system displays the bank account details. |  |
| 6 | Data Entry | Check the following entries:Collection Account: 11001065Make the following entries:Discount account: 11009366 |  |  |

### Post Incoming Payment with Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter a postdated check (PDC) received from a customer as a customer payment in your system.

Prerequisite

You have already entered a customer invoice and received a postdated check by means of payment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant for United Arab Emirates . | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Receive Bill of Exchange (F-36). | The Bill of Exchange Payment: Header Data screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Choose Open Items:Document Date: <Today's date>Posting Date: <Today's date>Type: DZCompany Code: 3310Currency: AEDPeriod: <Current fiscal period>Transaction to Be Processed: Incoming paymentPstKy: 09Account: <Account number>, for example, 33100003SGL Ind: W |  |  |
| 4 | Bill of Exchange Portfolio Entry | Make the following entries and choose Continue.Bill Portfolio: 1 | The Bill of Exchange Payment Add Customer Item screen displays. |  |
| 5 | Add Customer Item | Make the following entries:Amount: <Enter amount>Due on: <Maturity date>Check No.: <Enter check No.>Bank / Acct No: 18121986 / 0000000693123456 |  |  |
| 6 | Process Open Items | Choose Process Open Items. | The Bill of Exchange Payment Select open items screen displays. |  |
| 7 | Open Item Selection | Make the following entries and choose Process Open Items.Company Code: 3310Account: <Account number>, for example, 0033100003Account Type: DNormal OI: <Select> | The Bill of Exchange Payment Process open items screen displays. |  |
| 8 | Post | Select your document items and choose Post. |  |  |

### Present a Check to a Bank or Vendor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can present the postdated checks (PDC) sent by your customer either to a bank or to a vendor.

Prerequisite

You received a PDC from a customer and entered it into the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant for United Arab Emirates . | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Bill of Exchange Transactions (FTR03). | The Bill of Exchange Transactions screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries:Company Code: 3310Document Date: <Today's date>Posting Date: <Today's date> |  |  |
| 4 | Transactions Tab | Go to the Transactions tab. |  |  |
| 5 | Data Entry | Make the following entries:Presented to Bank: <Select>Note Alternately, select Presented to Vendor. |  |  |
| 6 | Selection Criteria Tab | Go to the Selection Criteria tab. |  |  |
| 7 | Data Entry | Make the following entries and choose Execute:Bill of Exchange/Check Portf.: 1Currency: AED | The Presented to Bank screen displays. |  |
| 8 | Choose Document | Select the document created in the previous step and choose Execute. | The Posting Data screen displays. |  |
| 9 | Enter Interim Account | Make the following entries and choose Continue：Interim Account: 11001065 | The document is posted. |  |

### Clear a Check Presented to a Bank or Vendor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When a bank or a vendor clears your check, you must record it in your system.

Prerequisite

You have already entered the check in the system and have presented it to a bank or a vendor. Now you have received notification that your check is cleared.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant for United Arab Emirates . | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Bill of Exchange Transactions (FTR03). | The Bill of Exchange Transactions screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries:Company Code: 3310Document Date: <Today's date>Posting Date: <Today's date> |  |  |
| 4 | Transactions Tab | Select the Transactions tab. |  |  |
| 5 | Data Entry | Make the following entries:Cleared at Bank: <Select>Note Alternately, select Cleared at Vendor. |  |  |
| 6 | Selection Criteria Tab | Select the Selection Criteria tab. |  |  |
| 7 | Data Entry | Make the following entries and choose Execute:Bill of Exchange/Check Portf.: 1Currency: AEDSelect the already collected BoE and choose Execute. | The Bill of Exchange Transactions screen displays. |  |
| 8 | Posting Data | Make the following entries and choose Continue:Value Date: <Today's date> | The document is posted. |  |

### Bounced Check at a Bank or Vendor

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can record a check bounced at a bank or a vendor in your system.

Prerequisite

You have entered the check in the system and presented it to a bank or a vendor as described in the [Present a Check to a Bank or Vendor](#unique_11) [page ] section. The bank notified you that the check bounced. You can refer to [Post Incoming Payment with Check](#unique_10) [page ] for more information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant for United Arab Emirates . | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Bill of Exchange Transactions (FTR03). | The Bill of Exchange Transactions screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries:Company Code: 3310Document Date: <Today's date>Posting Date: <Today's date> |  |  |
| 4 | Transactions Tab | Select the Transactions tab. |  |  |
| 5 | Data Entry | Make the following entries:Bounced at Bank: <Select>Note Alternately, select Bounced at Vendor. |  |  |
| 6 | Selection Criteria Tab | Select the Selection Criteria tab. |  |  |
| 7 | Data Entry | Make the following entries and choose Execute:Bill of Exchange/Check Portf.: 1Currency: AED | The Bill of Exchange Transactions screen displays. |  |
| 8 | Choose Document | Select the document and choose Execute. | The Posting Data screen displays. |  |
| 9 | Posting Data | Make the following entries and choose Continue:Portfolio for bounced bills: 2Special G/L indicator: W | The document is posted. |  |

### Bounced and Cleared

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can clear a bounced check recorded in your system. The system clears the check from the portfolio for bounced checks.

Prerequisite

You have entered the check in the system and have recorded it as Bounced at Bank or Bounced at Vendor.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Receivable Accountant for United Arab Emirates . | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Bill of Exchange Transactions (FTR03). | The Bill of Exchange Transactions screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries:Company Code: 3310Document Date: <Today's date>Posting Date: <Today's date> |  |  |
| 4 | Transactions Tab | Select the Transactions tab. |  |  |
| 5 | Data Entry | Make the following entries:Bounced and Cleared: <Select> |  |  |
| 6 | Selection Criteria Tab | Select the Selection Criteria tab. |  |  |
| 7 | Data Entry | Make the following entries and choose Execute:Portfolio for Bounced Bills: 2Currency: AED | The Bill of Exchange Transactions screen displays. |  |
| 8 | Choose Document | Select the document and choose Execute. | The Confirmation screen displays. |  |
| 9 | Confirmation | In the Confirmation dialog box, choose Yes. | The document is posted. |  |

### Remove a Check from a Portfolio

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this procedure to remove a check from a portfolio. When you transfer a check between portfolios, you must first remove it from the existing portfolio using the following procedure, then add it to a new portfolio. For more information, refer to [Add a Check to a Portfolio](#unique_16) [page ] .

Prerequisite

A new check has been checked in portfolio 1. You can refer to [Post Incoming Payment with Check](#unique_10) [page ] .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant for United Arab Emirates . | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Bill of Exchange Transactions (FTR03). | The Bill of Exchange Transactions screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries:Company Code: 3310Document Date: <Today's date>Posting Date: <Today's date> |  |  |
| 4 | Transactions Tab | Select the Transactions tab. |  |  |
| 5 | Data Entry | Make the following entries:Removed from Portfolio: <Select> |  |  |
| 6 | Selection Criteria Tab | Select the Selection Criteria tab. |  |  |
| 7 | Data Entry | Make the following entries and choose Execute:Old Portfolio: 1Currency: AED |  |  |
| 8 | Choose Document | Select the document and choose Execute. | The Posting Data screen displays. |  |
| 9 | Posting Data | Make the following entries and choose Continue：New portfolio: 3 | The document is posted. |  |

### Add a Check to a Portfolio

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this procedure to add a check to a portfolio.

Prerequisite

When you transfer a check between portfolios, you must first remove it from the existing portfolio and then add it to a new portfolio using the following procedure. For more information, refer to [Remove a Check from a Portfolio](#unique_15) [page ] .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant for United Arab Emirates . | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Bill of Exchange Transactions (FTR03). | The Bill of Exchange Transactions screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries:Company Code: 3310Document Date: <Today's date>Posting Date: <Today's date> |  |  |
| 4 | Transactions Tab | Select the Transactions tab. |  |  |
| 5 | Data Entry | Make the following entries:Added to Portfolio: <Select> |  |  |
| 6 | Selection Criteria Tab | Select the Selection Criteria tab. |  |  |
| 7 | Data Entry | Make the following entries and choose Execute:Old Portfolio: 1New Portfolio: 3Currency: AED | You created a new portfolio, for example, Portfolio 1, with the GL account. |  |
| 8 | Choose Document | Select the document and choose Execute. | The Confirmation screen displays. |  |
| 9 | Confirmation | Choose Yes. | The document is posted. |  |

### Reverse Check

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this procedure to reverse a check.

Prerequisite

You have already executed some transactions for bill of exchange.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant for United Arab Emirates . | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Bill of Exchange Transactions (FTR04). | The Reversal of Bill of Exchange Transactions screen displays. |  |
| 3 | General Data | Make the following entries:Company Code: 3310Document Date: <Today's date>Posting Date: <Today's date> |  |  |
| 4 | Reverse Postings Tab | Select the Reverse Postings tab. |  |  |
| 5 | Data Entry | Select a transaction. Make the following entries:From "Bill of Exchange Portfolio": <Select> |  |  |
| 6 | Selection Criteria Tab | Select the Selection Criteria tab. |  |  |
| 7 | Data Entry | Make the following entries and choose Execute:Bill of Exchange Portfolio: 3Currency: AED | The Reversal of Bill of Exchange Transactions screen displays. |  |
| 8 | Choose Document | Select the document and choose Execute. |  |  |
| 9 | Confirmation | Choose Yes. | The document is posted. |  |

### Create Check List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this procedure to check bill of exchange list.

Prerequisite

You have created some bills of exchange in some portfolios.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant for United Arab Emirates . | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Bill of Exchange List (FTR02). | The Bill of Exchange List screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Run:Company Code: 3310Bill of Exchange Portfolio: 1 to 3Open Items at Key Date: <Today's date>Cleared Bills of Exchange: <Select> | The Extended Bill of Exchange List with ABAP List Viewer screen displays. |  |

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
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WQ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 31,096 chars in the whole document
