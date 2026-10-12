---
id: 09-subscription-billing-and-contract-accounting/contract-accounting-company-initiated-payments-2dp-ae-test-script-813
title: Contract Accounting – Company Initiated Payments (2DP_AE) Test Script (2DP_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 2DP_AE (UAE): FI-CA company-initiated payments, payment runs, card orders, returns, revenue distribution."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-payments]
aliases: [2DP_S4CLD2608_BPD_EN_AE]
keywords: [Contract Accounting Incoming and Outgoing Payments, company initiated payments, payment run, payment order with credit card, returns lot processing, outgoing payment processing, revenue distribution, payment media, manual returns lot, payment advice notes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2DP_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-813
topic: 09-subscription-billing-and-contract-accounting/fi-ca-payments
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Contract Accounting – Company Initiated Payments (2DP_AE) Test Script (2DP_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2DP_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Contract Accounting Incoming and Outgoing Payments** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Contract Accounting – Company Initiated Payments (2DP_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Contract Accounting – Company Initiated Payments (2DP_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232849076)

[2 Prerequisites 5](#_Toc232849077)

[2.1 System Access 5](#_Toc232849078)

[2.2 Roles 5](#_Toc232849079)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232849080)

[2.4 Business Conditions 6](#_Toc232849081)

[2.5 Additional Manual Configuration 6](#_Toc232849082)

[3 Overview Table 8](#_Toc232849083)

[4 Test Procedures 11](#_Toc232849084)

[4.1 Complete Master Data 11](#_Toc232849085)

[4.1.1 Maintain Business Partner 11](#_Toc232849086)

[4.1.2 Maintain Contract Account 12](#_Toc232849087)

[4.2 Post Document 14](#_Toc232849088)

[4.2.1 Post Document 14](#_Toc232849089)

[4.2.2 Display Document 16](#_Toc232849090)

[4.3 Payment Process 17](#_Toc232849091)

[4.3.1 Execute Payment Run 22](#_Toc232849092)

[4.3.2 Check Payment Documents 26](#_Toc232849093)

[4.3.3 Print Payment Advice Note (Optional) 27](#_Toc232849094)

[4.3.4 Payment Card Settlement (Optional) 30](#_Toc232849095)

[4.3.5 Manage Payment Media 31](#_Toc232849096)

[4.3.6 Upload Bank Statement 32](#_Toc232849097)

[4.4 Payment Order with Credit Card 32](#_Toc232849098)

[4.4.1 Post Document 40](#_Toc232849099)

[4.4.2 Execute Payment Run 41](#_Toc232849100)

[4.4.3 Send Payment for Settlement 41](#_Toc232849101)

[4.4.4 Process Received Response from Payment Service Provider 43](#_Toc232849102)

[4.4.5 Post Payment Card Order Lots 45](#_Toc232849103)

[4.4.6 Display Payment Card Order Lot 46](#_Toc232849104)

[4.5 Return Lot Processing from Bank Statement 47](#_Toc232849105)

[4.5.1 Upload Bank Statement 47](#_Toc232849106)

[4.5.1.1 camt.053 Format 47](#_Toc232849107)

[4.5.2 Returns Lot Creation from Bank Statement 49](#_Toc232849108)

[4.5.3 Display Returns 51](#_Toc232849109)

[4.6 Return Lot Processing by Manual Creation 51](#_Toc232849110)

[4.6.1 Manual Returns Lot Creation 51](#_Toc232849111)

[4.6.2 Clarifications of Returns Lot 53](#_Toc232849112)

[4.7 Outgoing Payment Processing 54](#_Toc232849113)

[4.7.1 Post Outgoing Payment Request Document 54](#_Toc232849114)

[4.7.2 Display Outgoing Payment Request Document 56](#_Toc232849115)

[4.7.3 Post Outgoing Payment Document 57](#_Toc232849116)

[4.7.4 Post Credit Memo Document 57](#_Toc232849117)

[4.7.5 Clear Outgoing Payment documents with Credit Memo 57](#_Toc232849118)

[4.8 Revenue Distribution 58](#_Toc232849119)

[4.8.1 Post Document 60](#_Toc232849120)

[4.8.2 Process Payment Lot 62](#_Toc232849121)

[4.8.3 Distribute Revenue 62](#_Toc232849122)

[4.8.4 Post Distribute Revenue 63](#_Toc232849123)

[4.8.5 Analyze Revenue Distribution 65](#_Toc232849124)

[4.8.6 Reverse Distribute Revenue 66](#_Toc232849125)

[5 Appendix 68](#_Toc232849126)

[5.1 Process Integration 68](#_Toc232849127)

[5.1.1 Change Document 68](#_Toc232849128)

[5.1.2 Display Document Changes 68](#_Toc232849129)

[5.1.3 Maintain Accounts 68](#_Toc232849130)

[5.1.4 Display Account Balance 69](#_Toc232849131)

[5.1.5 Business Partner Financial Overview 69](#_Toc232849132)

[5.1.6 Reverse Document 69](#_Toc232849133)

[5.1.7 Reverse Documents 69](#_Toc232849134)

[5.1.8 Reverse Documents - Mass Run 70](#_Toc232849135)

[5.1.9 Write - Off Items 70](#_Toc232849136)

[5.1.10 Write-Off Items - Mass Run 70](#_Toc232849137)

[5.1.11 Display Write-Offs 71](#_Toc232849138)

[5.1.12 Manage Documents 71](#_Toc232849139)

[5.1.13 Search Payment 72](#_Toc232849140)

[5.1.14 Create Payment Media Manually 72](#_Toc232849141)

[5.1.15 Clarify Exceptions from Payment Run 74](#_Toc232849142)

[5.1.16 Sample Bank Statement for Payment Order Lot 76](#_Toc232849143)

[5.1.16.1 camt.053 Format 77](#_Toc232849144)

[5.1.17 Manage Payment Orders 82](#_Toc232849145)

## Purpose

Overview

This process allows you to start the collect payment procedure from the company perspective. Using different methods, the company can receive the customer’s payment and perform further processing.

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
| Administrator - Accounts Payable and Receivable (FI-CA) | SAP_BR_ADMIN_APR_FICA | Contract Accounting - Jobs | SAP_BR_ADMIN_APR_FICA |  |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Table 1: Organizational Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| House Bank Account | AEAC1 AEAC2 |  |  |
| House Bank | AEBK1 AEBK2 |  |  |

Table 2: Other Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Business Partner | BP_AE_99 |  |  |
| Contract Account | CA_AE_99 |  |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met .

| Scope Item ID | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Contract partner and contract account have been created for posting. |

### Additional Manual Configuration

Regarding Tax Date settings, you can manually modify the following configurations for FI-CA:

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:
    1. Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned.
    2. Choose Manage Your Solution APP, search for Set Up Company Codes for Contract Accounts Receivable and Payable, or Configuration Activity ID: 101239. Choose Configure.
    3. Select the company code and choose details.
    4. In the Settings for Tax Date section, you could modify relevant configuration. By default, Default Tax Date is selected to align with the General Ledger FI. This means that in postings, the default tax date should correspond to the one specified in table T001 at the company code level.
    5. You can adjust relevant configuration for Tax Date from Statistical Receivable according to your business needs. By default, it is left blank.
- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. You can search for Set Up Company Codes for Contract Accounts Receivable and Payable to locate it in the tree view. Choose Open Documentation for the found line item to see more details. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Select the company code and choose details.

In the Settings for Tax Date section, you could modify relevant configuration. By default, Default Tax Date is selected to align with the General Ledger FI. This means that in postings, the default tax date should correspond to the one specified in table T001 at the company code level.

You can adjust relevant configuration for Tax Date from Statistical Receivable according to your business needs. By default, it is left blank.

## Overview Table

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Complete Master Data

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Maintain Business Partner](#unique_9) [page ] 11 | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Business Partner (BP) | Business Partner master data is completed for succeeding process. |
| [Maintain Contract Account](#unique_10) [page ] 12 | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Contract Account (CAA3) | Contract Account master data is completed for succeeding process. |

Post Document

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Document](#unique_11) [page ] 14 | Accounts Payable and Receivable Accountant (FI-CA) | Post Document (FPE1) | Credit documents are posted. |
| [Display Document](#unique_12) [page ] 16 | Accounts Payable and Receivable Accountant (FI-CA) | Display Document (FPE3) |  |

Payment Process

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Execute Payment Run](#unique_13) [page ] 22 | Administrator - Accounts Payable and Receivable (FI-CA) | Payment Run / Debit Memo Run (F3529) | Open credit items can be cleared by payment run. Payment media are created automatically. |
| [Check Payment Documents](#unique_14) [page ] 26 | Accounts Payable and Receivable Accountant (FI-CA) | Display Payment Lists (F3917) | Check business partner payment documents created by payment run. |
| [Print Payment Advice Note (Optional)](#unique_15) [page ] 27 | Accounts Payable and Receivable Accountant (FI-CA) | Display Correspondences (F3693) | Correspondence of payment advice note can be displayed and printed. |
| [Manage Payment Media](#unique_16) [page ] 31 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Payment Media (F1868) | Check payment media which are created automatically. |
| [Upload Bank Statement](#unique_17) [page ] 32 | Administrator - Accounts Payable and Receivable (FI-CA) | Management Incoming Payment Files | Bank statement upload successfully. |

Payment Order with Credit Card

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Document](#unique_18) [page ] 40 | Accounts Payable and Receivable Accountant (FI-CA) | Post Document (FPE1) | Credit document is posted. |
| [Execute Payment Run](#unique_19) [page ] 41 | Administrator - Accounts Payable and Receivable (FI-CA) | Payment Run / Debit Memo Run (F3529) | Payment order is created and card account is posted to payment order clearing account. |
| [Send Payment for Settlement](#unique_20) [page ] 41 | Administrator - Accounts Payable and Receivable (FI-CA) | Process Payment Cards (F3542) | Payments are sent to PSP. |
| [Process Received Response from Payment Service Provider](#unique_21) [page ] 43 | Administrator - Accounts Payable and Receivable (FI-CA) | Process Payment Cards (F3542) | Answer from PSP is processed and clearing document is created. |
| [Post Payment Card Order Lots](#unique_22) [page ] 45 | Administrator - Accounts Payable and Receivable (FI-CA) | Post Payment Card Order Lot (F7118) | Payment order is executed and open receviables is cleared. |
| [Display Payment Card Order Lot](#unique_23) [page ] 46 | Accounts Payable and Receivable Accountant (FI-CA) | Process Payment Card Order Lots (FP45CC) | Payment card order lot is displayed. |

Return Lot Processing from Bank Statement

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Upload Bank Statement (For Returns) |  |  |  |
| [camt.053 Format](#unique_24) [page ] 47 | Administrator - Accounts Payable and Receivable (FI-CA) | Management Incoming Payment Files | A camt.053 format electronic bank statement is uploaded. |
| [Returns Lot Creation from Bank Statement](#unique_25) [page ] 49 | Administrator - Accounts Payable and Receivable (FI-CA) | Transfer Bank Statement (FPB7) | The Returns Lot key is displayed in log for further step. |
| [Display Returns](#unique_26) [page ] 51 | Accounts Payable and Receivable Accountant (FI-CA) | Display Returns (F3126) | Return lots history can be displayed. |

Return Lot Processing by Manual Creation

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Manual Returns Lot Creation](#unique_27) [page ] 51 | Accounts Payable and Receivable Accountant (FI-CA) | Process Returns Lot (FP09) | The return lot is created successfully. |
| [Clarifications of Returns Lot](#unique_28) [page ] 53 | Accounts Payable and Receivable Accountant (FI-CA) | Clarify Returns (FPCRL) | The clarification of returns lot display. |

Outgoing Payment Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Outgoing Payment Request Document](#unique_29) [page ] 54 | Accounts Payable and Receivable Accountant (FI-CA) | Post Document (FPE1) | Outgoing Payment request document has been posted. |
| [Display Outgoing Payment Request Document](#unique_30) [page ] 56 | Accounts Payable and Receivable Accountant (FI-CA) | Display Document (FPE3) | The Outgoing Payment request document is displayed. |
| [Post Outgoing Payment Document](#unique_31) [page ] 57 | Administrator - Accounts Payable and Receivable (FI-CA) | Payment Run / Debit Memo Run (F3529) | The Outgoing payment document is posted. |
| [Post Credit Memo Document](#unique_32) [page ] 57 | Accounts Payable and Receivable Accountant (FI-CA) |  | The Credit Memo document is posted. |
| [Clear Outgoing Payment documents with Credit Memo](#unique_33) [page ] 57 | Accounts Payable and Receivable Accountant (FI-CA) | Maintain Accounts (FP06) | The Outgoing payment document is cleared with Credit Memo. |

Revenue Distribution

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Document](#unique_34) [page ] 60 | Accounts Payable and Receivable Accountant (FI-CA) | Post Document (FPE1) | Document has been posted. |
| [Process Payment Lot](#unique_35) [page ] 62 |  | Process Payment Lot (FP05) | Payment lot processed successfully. |
| [Distribute Revenue](#unique_36) [page ] 62 | Administrator - Accounts Payable and Receivable (FI-CA) | Distribute Revenues (FP60M) | Revenue distribution was executed without error. |
| [Post Distribute Revenue](#unique_37) [page ] 63 | Administrator - Accounts Payable and Receivable (FI-CA) | Post Revenue Distribution Documents (F5056) | Revenue Distribution document is posted. |
| [Analyze Revenue Distribution](#unique_38) [page ] 65 | Accounts Payable and Receivable Accountant (FI-CA) | Analyze Revenue Distribution - Based on Original Documents (FP60R_NEW) | The Revenue Distribution documents of the business partner is displayed. |
| [Reverse Distribute Revenue](#unique_39) [page ] 66 | Accounts Payable and Receivable Accountant (FI-CA) | Reverse Distribution Documents (F5054) Reversal of Distribution Documents |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Complete Master Data

#### Maintain Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can complete the Business Partner master data to create outgoing payments.

Procedures

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Select Business Partner | Make the following entry:Business Partner: <Select Business Partner Number with MKK BP Role> |  |  |
| 4 | Open Business Partner | Choose Enter. | The Display Person: Business Partner Number screen is displayed. |  |
| 5 | Switch to Change Mode | Choose Switch Between Display and Change. | The business partner fields are editable. |  |
| 6 | Maintain Payment Data | Make the following entries on the Payment Transactions tab:ID: 01C/R: AEBank Key : 18121976Bank Account : <Bank Account> |  |  |
| 7 | Save | Choose Save. | Changes are saved for the Business Partner. |  |

#### Maintain Contract Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you complete Contract Account master data to create outgoing payments.

Procedures

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Maintain Contract Account (CAA3). | The Contract Account Display: Initial Screen is displayed. |  |
| 3 | Select Change Mode | Choose Change. | The Contract Account Change: Initial Screen is displayed. |  |
| 4 | Select Contract Account | Make the following entry:Contract Acct: <Select Contract Account related to Business Partner in step [Maintain Business Partner](#unique_9) [page ] 11> |  |  |
| 5 | Open Contract Account | Choose Continue. | The Contract Account Display: General Data screen is displayed. |  |
| 6 | Maintain Payment Data | Make the following entries in the Payments/Taxes section:Outg.Payt Meth: TBank ID – Outg.: 01CardID Outgoing: <Your Card ID>Note For credit card registration, please refer to 2AR - Contract Accounting – Master Data and Basic Functions, step Create a Business Partner.Note Inc.Payt Method: EBank Det. Inc.: 01CardID Incoming: 0001 |  |  |
| 7 | Save | Choose Save. | Changes are saved for the Contract Account. |  |

### Post Document

#### Post Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can post credit documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Post Document (FPE1). | The Post Document: Initial Screen is displayed. |  |
| 3 | Enter Data | Make the following entries:Document Date: <Today's Date>Posting Date: <Today's Date>Document Type: YACurrency: AEDReconcil. Key: <Reconciliation Key generated by system>Clearing Reason: 02 Outgoing PaymentBP Item: Y01G/L Item: Y01Taxes Calculate Automatically : <Selected> |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.Note If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new Reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen is displayed. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section,Bus. Partner: <Business Partner Number with MKK BP Role>Contract Acct: <Contract Account Number Related to the Selected BP>Company Code: 3310Transac: Y600/0010In the Amounts and Due Dates section,Amount: <Any>Tax Code: <Output Tax Code>In the Dunning Data/Payment Data section,Payment Method: TNote For Credit Card for Outgoing Payment:Transaction: Y600/0010, Payment method: 3For Credit Transfer with Payment Order:Transaction: Y600/0010, Payment method: 5For Direct Debit via Payment Order:Transaction: Y600/0020, Payment method: 4If your country solution does not include the above mentioned payment methods, you have the option to create it yourself via configuration activities 101952 and 101251.Note For post documents integrated with Provider Contract, you could enter below information:Contract: <Provider Contract number>Subappl: PContract Item: <item no. in Provider Contract> |  |  |
| 8 | Post | Choose Post. | The credit document is posted. |  |

#### Display Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can display the FI-CA documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Document (FPE3). | The Display Document: Initial screen is displayed. |  |
| 3 | Select Document to Display | Make the following entries and choose ENTER:Document Number: <Document Number Posted in step [Post Document](#unique_11) [page ] 14>BP Item: Y01G/L Item: Y01 | The Display Document: Overview screen is displayed. Details of the document are displayed. |  |

### Payment Process

Context

In this section, you can process the payment.

Prerequisite

1. You can set up self-customized payment medium format in FI-CA according to the following steps:

(Optional) Define Payment Medium Formats via configuration activity: 106730

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access Define Payment Medium Formats | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Payment Medium Formats.Choose Configure in the Define Payment Medium Formats row. | The Define Payment Medium Formats: Change screen is displayed. |  |
| 4 | Input Parameters | Choose an existing payment medium format, for example, AE_CGI_XML_DD.Choose Copy As, and make the following entries to create a new payment medium format:Payment Medium (DME) Without Documents: <Checked>Type: for example, 04 XMLFormat: <Input the payment medium format and the description> for example, / AE_CGI_XML_DD and ISO20022 Automatic Debit, United Arab EmiratesNote Please set a format ID starting with '/'.Country/Region Key: AEExt. Format Name: for example, PAIN.008.001.02Format Short Name: for example, /AE_CGI_DDNote Please set a Name starting with '/'.Deviating Format Tree: AE_CGI_XML_DDDocumentation Module: for example, FPM_DOCU_CGI_XML_DDCode Page: for example, 4110Company Code: <Checked>House Bank: <Checked>Check and modify the other data if required, then press Enter.Choose copy all in the dialog box appears.Choose Continue, and choose Save.Save the entry.Choose the newly created payment medium format, and double-click the sub folder Text Fields for Reference Information.Choose New Entries and make the following entries:Suppl.: for example, <blank>Notif. Type: for example, Note to payeeLength: for example, 035Number: for example, 004Save the entry.Note You can also double-click the sub folder Supplements for Payment Medium Formats, and choose New Entries to add new entries if required. | Settings for the new Payment Medium Format are saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Payment Medium Formats | Go to the Business Processes Configuration app and search for the following activity: Define Payment Medium Formats.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Variants for Payment Medium Program: Change screen is displayed. |  |
| 3 | Input Parameters | Choose an existing payment medium format, for example, AE_CGI_XML_DD.Choose Copy As, and make the following entries to create a new payment medium format:Payment Medium (DME) Without Documents: <Checked>Type: for example, 04 XMLFormat: <Input the payment medium format and the description> for example, / AE_CGI_XML_DD and ISO20022 Automatic Debit, United Arab EmiratesNote Please set a format ID starting with '/'.Country/Region Key: AEExt. Format Name: for example, PAIN.008.001.02Format Short Name: for example, /AE_CGI_DDNote Please set a Name starting with '/'.Deviating Format Tree: AE_CGI_XML_DDDocumentation Module: for example, FPM_DOCU_CGI_XML_DDCode Page: for example, 4110Company Code: <Checked>House Bank: <Checked>Check and modify the other data if required, then press Enter.Choose copy all in the dialog box appears.Choose Continue, and choose Save.Save the entry.Choose the newly created payment medium format, and double-click the sub folder Text Fields for Reference Information.Choose New Entries and make the following entries:Suppl.: for example, <blank>Notif. Type: for example, Note to payeeLength: for example, 035Number: for example, 004Save the entry.Note You can also double-click the sub folder Supplements for Payment Medium Formats, and choose New Entries to add new entries if required. | Settings for Variants for Payment Medium Program are saved successfully. |  |

|  |
| --- |
| Note After creating the new payment medium format, complete the following settings via relevant configuration activity if required.Define Variants for Payment Medium Program via configuration activity: 101276This step is to add the variant name for the new payment short name which you assigned to the new payment medium format via above step.Choose New Entries to add the payment medium variant, and save the entry.Define Variant Determination for Payment Medium Program via configuration activity: 102207This step is to maintain the variant determination for the new payment short name which you assigned to the new payment medium format via above step.Choose Create to add the determination data, assign the same variant ID which you have added via configuration activity: 101276, and save the entry.Define Specifications for Paying Company Code via configuration activity: 101251This step is to assign the new payment medium format to your company code.Choose your company code, double-click the sub folder Payment Medium Formats in Company Code on the left column, and choose the original format ID which you copied to create the new format.Choose Copy As…, enter new format ID, and save the entry.Define Payment Methods via configuration activity: 101952This step is to assign the new payment medium format to your payment method.Choose your country, double-click the sub folder Payment Methods on the left column, double-click your payment method (for example, T).Enter your new format ID into Format under the tab Payment medium format and save the entry. |

1. If you want to use the Multi-bank Connectivity function in FI-CA, please make sure you have chosen scope item 16R: Bank Integration with SAP Multi-Bank Connectivity and completed the following mandatory configuration steps:

(Optional) Define Variants for Payment Medium Program via configuration activity: 101276

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access Define Variants for Payment Medium Program | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Payment Medium Formats.Choose Configure in the Define Variants for Payment Medium Program row. | The Define Variants for Payment Medium Program: Change screen is displayed. |  |
| 4 | Input Parameters | Input the Format Short Name of the Payment Medium Format you want to use Multi-bank Connectivity in FI-CA and choose Apply.Select the Payment Medium Format with your Format Short Name and Payment Medium Variant, and choose the Details button.If you're directed to the Define Variants for Payment Medium Program: Change: Details screen, select the Send Message checkbox on the Parameters Independent of Format tab.Save the entry. | Settings for Variants for Payment Medium Program are saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Variants for Payment Medium Program | Go to the Business Processes Configuration app and search for the following activity: Define Variants for Payment Medium Program.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Variants for Payment Medium Program: Change screen is displayed. |  |
| 3 | Input Parameters | Input the Format Short Name of the Payment Medium Format you want to use Multi-bank Connectivity in FI-CA and choose Apply.Select the Payment Medium Format with your Format Short Name and Payment Medium Variant, and choose the Details button.If you're directed to the Define Variants for Payment Medium Program: Change: Details screen, select the Send Message checkbox on the Parameters Independent of Format tab.Save the entry. | Settings for Variants for Payment Medium Program are saved successfully. |  |

#### Execute Payment Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can create payment documents by mass run.

Prerequisite

Before you execute payment run, make sure account determination is set up correctly via SSCUI as below.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Accounts for Payment Program | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Company Initiated Payments.Choose Configure in the Define Accounts for Payment Program row. | The Maintain Payment Program Bank Accounts: Overview screen is displayed. |  |
| 4 | Check or Add Entries for Account Determination | Choose Create and add an entry for company code.Paying Company code: <For example, 3310. Do not enter * in this field.>House Bank: <For example, AEBK1. Do not enter * in this field.>Payment Method: <For example, T. Do not enter * in this field.>Currency: <For example, AED. Do not enter * in this field.>Account ID: <For example, AEAC1>Tax: <Make sure * is maintained. Only input blank or X for Romania VAT split purpose>Save the entry. | Account determination entries are saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Selection Criteria for Credit Clarification | Go to the Business Processes Configuration app and search for the following activity: Define Accounts for Payment Program.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Credit Processing: Customizing ID Credit ": Overview screen is displayed. |  |
| 3 | Input Parameters | Choose Create and add an entry for company code.Paying Company code: <For example, 3310. Do not enter * in this field.>House Bank: <For example, AEBK1. Do not enter * in this field.>Payment Method: <For example, T. Do not enter * in this field.>Currency: <For example, AED. Do not enter * in this field.>Account ID: <For example, AEAC1>Tax: <Make sure * is maintained. Only input blank or X for Romania VAT split purpose>Save the entry. | Account determination entries are saved successfully. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Payment Run / Debit Memo Run (F3529). | The Application Jobs screen is displayed. |  |
| 3 | Create | Choose Create. | The New Job screen is displayed. |  |
| 4 | Maintain Parameters | Make the following entries and choose Step 2:Job Template: FI-CA Payment RunJob Name: FI-CA Payment Run |  |  |
| 5 | Maintain Parameters | Make the following entry and choose Step 3:Start Immediately: <Selected> |  |  |
| 6 | Maintain Parameters | Make the following entries:Run SettingsPrefix of Run ID: For example, ID0Simulation run: <Unselected>Selection CriteriaOpen Items: <Selected>Note Please select Pre-notified Items if you have executed Advance Notice for Direct Debits.Business Partner: <Select Business Partner number in step Post Document>Contract Account: <Select Contract Account number in step Post Document>Company Code: 3310Due by: <Today's Date + 1 Year>Payment Method List: 3310Country/Region Key: AEFurther SettingsSelection ID: 3310Note The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function LASTDAYOFCURRENTMONTH for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. For credit card outgoing payment, after execute payment run generated clearing document, please follow/refer to step: Payment Card Settlement in 2BI - Contract Accounting – Customer Initiated Payments. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. One new application job is created with a status. Payment documents are created from job log details. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Check Payment Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can check business partner payment documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Payment Lists (F3917). | The Display Payment Lists screen is displayed. |  |
| 3 | Enter Filters | Make the following entries:Payment Run Date: <Input payment run date in the [Execute Payment Run](#unique_13) [page ] 22 step>Or Payment Run ID: <Input payment run date in the [Execute Payment Run](#unique_13) [page ] 22 step> |  |  |
| 4 | Execute | Choose Go.Select the payment run line item you want to display. | The correspondent payment run items are listed. |  |
| 5 | Check Payment Document | Click the payment document number. Scroll down to the Payments for Business Partner Items tab.Note Write down the payment document number. | The payment clearing document number is displayed on the Payments for Business Partner Items tab. |  |
| 6 | Display Document | Choose Display Document. | Details of the payment document are displayed on the Display Document: Overview screen. |  |

#### Print Payment Advice Note (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display correspondence of payment advice note then print it or send it via email in SAP S/4HANA Cloud Public Edition.

Prerequisite

|  |
| --- |
| Note The procedures outlined in this section require that the prerequisite customizing activities be completed before you execute the payment run. |

1. Define Specifications for Paying Company Code via configuration activity: 101251

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Specifications for Paying Company Code | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Company Initiated Payments.Choose Configure in the Define Specifications for Paying Company Code row. | The "Define Specifications for Paying Company Code": Change screen is displayed. |  |
| 4 | Input Parameters | Choose your company code and double-click the Payment Medium Formats in Company Code folder in the Dialog Structure.Company Code: <3310>Double-click the format, for example, AE_CGI_XML_CTNote Please make sure the format you select has already been assigned to the payment method of your posted document or contract account via configuration activity Define Payment Methods (101952).Then make the following criteria for your payment medium format:Always output payment advice: <Checked>Note For the CGI format, you can choose to select Payment Advice if Info Lines Overflow instead of Always Output Payment Advice, or opt for both.Save the entry. | Settings for Define Specifications for Paying Company Code are saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Define Specifications for Paying Company Code | Go to the Business Processes Configuration app and search for the following activity: Define Specifications for Paying Company Code.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Specifications for Paying Company Code": Change screen is displayed. |  |
| 3 | Input Parameters | Choose your company code and double-click the Payment Medium Formats in Company Code folder in the Dialog Structure.Company Code: <3310>Double-click the format, for example, AE_CGI_XML_CTNote Please make sure the format you select has already been assigned to the payment method of your posted document or contract account via configuration activity Define Payment Methods (101952).Then make the following criteria for your payment medium format:Always output payment advice: <Checked>Note For the CGI format, you can choose to select Payment Advice if Info Lines Overflow instead of Always Output Payment Advice, or opt for both.Save the entry. | Settings for Define Specifications for Paying Company Code are saved successfully. |  |

1. Maintain the email for your business partner via APP Manage Business Partner.

|  |
| --- |
| Note If an Alternative Correspondence Recipient (Corresp. Recip.) is specified in contract account, you need to maintain the email for Alternative Correspondence Recipient. |

1. You have posted document via step [Post Document](#unique_11) [page ] 14 and executed payment run via step [Check Payment Documents](#unique_14) [page ] 26.

|  |
| --- |
| Note If you only select Payment advice if info lines overflow for your payment medium format via configuration activity: Define Specifications for Paying Company Code (101251), please check the number of notification type 1 Note to Payee, which is maintained in the Text Fields for Reference information folder in the Dialog Structure via configuration activity: Define Payment Medium Formats (106730). Ensure that the receivable/payable line items in your posted document exceed this number; otherwise, no new correspondence will be generated. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Correspondences (F3693). | The Display Correspondence screen is displayed. |  |
| 3 | Search Criteria | Enter the following parameters.Correspondence Type: <Payment Advice Notes (0006)> |  |  |
| 4 | Execute | Choose Go. | A new correspondence is displayed in the list. |  |
| 5 | Print Correspondence | Select the item and choose the arrow button >.Choose Print.In the Print Correspondence dialog box, make the following criteria:Output Mode: Real print (X)Channel: Print | The Payment Advice Notes PDF file is displayed. Verify the accuracy of values, such as the header, payment information, and other related details.Note SAP provides pre-delivered form templates, and you can design your own templates according to your specific needs. |  |
| 6 | Repeat Print | Choose Print.In the Print Correspondence dialog box, make the following criteria:Output Mode: Repeat print (R)Send Control: Only emailChannel: Email | An email is sent to the address specified in the master data records.Note If an Alternative Correspondence Recipient is designated in the contract account, the email address will be utilized for the email channel. If no alternative correspondence recipient is specified, the email address of the Business Partner (BP) noted in the document will be used. |  |

#### Payment Card Settlement (Optional)

Context

In this activity, you can process the payment card settlement after payment run.

Prerequisite

Make sure you have already posted a FI-CA document with credit card information and 'Authorize' chosen, or a FI-CA document with credit card information 'Authorize + Pay' chosen, and have completed the payment run of this FI-CA document.

Procedure

If you choose 'Authorize', please refer to the test script of the scope item 2BIContract Accounting – Customer Initiated Payments, chapter Payment Cards: Process Payments Not Yet Captured by PSP.

If you choose 'Authorize + Pay', please refer to the test script of the scope item 2BI Contract Accounting – Customer Initiated Payments, chapter Payment Cards: Process Payments Already Captured by PSP.

#### Manage Payment Media

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can check the payment media that is created automatically after payment run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Payment Media (F1868). | The Manage Payment Media screen is displayed. |  |
| 3 | Open Detailed Filters | Choose Filters. | The Filters screen is displayed. |  |
| 4 | Enter Filters | Make the following entries:Run Date: <Input the Payment Run Date in the [Execute Payment Run](#unique_13) [page ] 22 step> |  |  |
| 5 | Execute | Choose Go. | The corresponding payment media file is listed with New status. |  |
| 6 | Download Payment Files | Select the payment media file and choose Download. | The Download Success window appears. |  |
| 7 | Check Payment Files | Choose OK.Open the downloaded payment media file. | Payment media files are displayed for checking. |  |

#### Upload Bank Statement

Context

In this process step, you upload an electronic bank statement in SAP S/4HANA Cloud Public Edition system.

Procedure

Please refer to the Upload Bank Statement step in scope item 1EG - Bank Integration with File Interface.

|  |
| --- |
| Note For payment order lot bank statement, please refer to the samples listed in Appendix. SAP GUI also provides the function (Tcode: FPBS1) to generate the bank statement automatically. A payment order can be created if a payment (incoming as well as outgoing) has been generated through payment run and payment media transferred to the bank. The open item can be cleared in FICA after the actual payment is confirmed through the incoming bank statement. Once the bank statement has been imported and the bank posting transferred to FICA, the payment order can be posted or closed in the payment order lot. Only now will the open items be cleared. The underlying payment methods are 4 for direct debit payments via payment order, and 5 for credit transfers via payment order. |

### Payment Order with Credit Card

Context

In this activity, you can process the open receivable with payment run using the payment method payment order with credit card.

Prerequisite

Before you execute payment order with credit card, make sure you've completed the following steps via customizing activities.

1. Prepare two G/L accounts with account type X (balance sheet account), one is for payment card clearing account, the other is for payment order clearing account.

About how to create a new G/L account by copying an existing one, please refer to step Manage G/L Account Master Data in the test script of scope item J58 - Accounting and Financial Close.

1. Define Payment Methods (via SSCUI: 101952)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Payment Methods | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Company Initiated Payments.Choose Configure in the Define Payment Methods row. | The "Define Payment Methods": Display screen is displayed. |  |
| 4 | Input Parameters | Choose your country ID, for example, AE.Double-click the Payment Methods folder in the Dialog Structure.Choose New Entries and make the following entries to create a new payment method:Payment Method: <For example, $>Discription: <For example, Payment Order with Credit Card>Payment Method for Incoming Pmnts: <Selected>Payment card: <Selected>Payment order only: <Selected>Double-click the Additional Details folder in the Dialog Structure.Choose Continue in the Information dialog box, then choose New Entries and make the following entries:Application area: <Convergent FI-CA>Document Type: <YA>Double-click the Payment Method Lists folder in the Dialog Structure, and assign your created new payment method to your payment method list.Payment Method List: <For example, Z001>Payment Methods List : <For example, ET$>Save the entry. | Settings for payment method are saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access App Manage Your Solution | Go to the Business Processes Configuration app and search for the following activity: Define Payment Methods.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Payment Methods": Display screen is displayed. |  |
| 3 | Input Parameters | Choose your country ID, for example, AE.Double-click the Payment Methods folder in the Dialog Structure.Choose New Entries and make the following entries to create a new payment method.Payment Method : <For example, $>Discription: <For example, Payment Order with Credit Card>Payment Method for Incoming Pmnts: <Selected>Payment card: <Selected>Payment order only: <Selected>Double-click the Additional Details folder in the Dialog Structure.Choose Continue in the Information dialog box, then choose New Entries and make the following entries:Application area: <Convergent FI-CA>Document Type: <YA>Double-click the Payment Method Lists folder in the Dialog Structure, and assign your created new payment method to your payment method list.Payment Method List: <For example, Z001>Payment Methods List : <For example, ET$>Save the entry. | Settings for payment method are saved successfully. |  |

1. Define Specifications for Paying Company Code (via SSCUI: 101251)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Specifications for Paying Company Code | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Company Initiated Payments.Choose Configure in the Define Specifications for Paying Company Code row. | The "Define Specifications for Paying Company Code": Change screen is displayed. |  |
| 4 | Input Parameters | Choose your company code and double-click the Payment Methods in Company Code folder in the Dialog Structure.Company Code: <3310>Choose New Entries and make the following critieria for your company code:Payment Method: <Your newly created payment method>Country/Reg: <AE>Maximum Amount: <For example, 9.999.999.999,00>Save the entry. | Settings for Define Specifications for Paying Company Code are saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access App Define Specifications for Paying Company Code | Go to the Business Processes Configuration app and search for the following activity: Define Specifications for Paying Company Code.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Specifications for Paying Company Code": Change screen is displayed. |  |
| 3 | Input Parameters | Choose your company code and double-click the Payment Methods in Company Code folder in the Dialog Structure.Company Code: <3310>Choose New Entries and make the following critieria for your company code:Payment Method: <Your newly created payment method>Country/Reg: <AE>Maximum Amount: <For example, 9.999.999.999,00>Save the entry. | Settings for Define Specifications for Paying Company Code are saved successfully. |  |

1. Define Account Determination for Card Payment Order Lot (via SSCUI: 106193)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Account Determination for Card Payment Order Lot | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Company Initiated Payments.Choose Configure in the Define Account Determination for Card Payment Order Lot row.Choose the Chart of Accounts.Chart of Accts: <YCOA> | The Maintain 1128: Overview screen is displayed. |  |
| 4 | Input Parameters | Make the following entries for your paying company code:Payment Card Type: <For example, *>Company Code: <For example, *>Merchant ID: <For example, *>Account ID: < Your payment order clearing account prepared in Prerequisite>Save the entry. | Settings for account determination are saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Open Define Account Determination for Card Payment Order Lot | Go to the Business Processes Configuration app and search for the following activity: Define Account Determination for Card Payment Order Lot.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Choose the Chart of Accounts.Chart of Accts: <YCOA> | The Maintain 1128: Overview screen is displayed. |  |
| 3 | Input Parameters | Make the following entries for your paying company code:Payment Card Type: <For example, *>Company Code: <For example, *>Merchant ID: <For example, *>Account ID: < Your payment order clearing account prepared in Prerequisite>Save the entry. | Settings for account determination are saved successfully. |  |

1. Define Bank Clearing Account (via SSCUI: 102466)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Bank Clearing Account | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose General Payment Settings.Choose Configure in the Define Bank Clearing Account row. | The "Define Bank Clearing Account": Change screen is displayed. |  |
| 4 | Input Parameters | Make the following entries for your company code:Company Code: <3310>Bank clearing acct: <Your payment order clearing account prepared in Prerequisite>Card Payment Orders - Card Payt Order Lot Bank Clearing Acct: <Selected>Save the entry. | Bank Clearing Account for Payment Order with Credit Card is saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Open Define Bank Clearing Account | Go to the Business Processes Configuration app and search for the following activity: Define Bank Clearing Account.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Bank Clearing Account": Change screen is displayed. |  |
| 3 | Input Parameters | Make the following entries for your company code:Company Code: <3310>Bank clearing acct: <Your payment order clearing account prepared in Prerequisite>Card Payment Orders - Card Payt Order Lot Bank Clearing Acct: <Selected>Save the entry. | Bank Clearing Account for Payment Order with Credit Card is saved successfully. |  |

1. Define Accounts for Payment Card Institute (via SSCUI: 101957)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Accounts for Payment Card Institute | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Payment Cards.Choose Configure in the Define Accounts for Payment Card Institute row.Choose the Chart of Accounts.Chart of Accts: <YCOA> | The Maintian Payment Cards: Account Assignment: Overview screen is displayed. |  |
| 4 | Input Parameters | Make the following entries for your company code:Payment Card Type: <For example, DPVI>Company Code: <3310>Merchant ID: <*>Card Account: <0012530200>Clearing Account: <Your card clearing account created in Prerequisite>No Validity: <Selected>No Cardholder: <Selected>Save the entry. | Accounts for Payment Card Institute saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access App Define Accounts for Payment Card Institute | Go to the Business Processes Configuration app and search for the following activity: Define Accounts for Payment Card Institute.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Choose the Chart of Accounts.Chart of Accts: <YCOA> | The Maintian Payment Cards: Account Assignment: Overview screen is displayed. |  |
| 3 | Input Parameters | Make the following entries for your company code:Payment Card Type: <For example, DPVI>Company Code: <3310>Merchant ID: <*>Card Account: <0012530200>Clearing Account: <Your card clearing account created in Prerequisite>No Validity: <Selected>No Cardholder: <Selected>Save the entry. | Accounts for Payment Card Institute saved successfully. |  |

1. Maintian the payment card data for your business partner. Please refer to step Create a Business Partner in the test script of scope item 2AR - Contract Accounting – Master Data and Basic Functions.

|  |
| --- |
| Note The payment card type maintained in business partner needs to be in accordance with the type maintained in Define Accounts for Payment Card Institute (via SSCUI: 101957). |

1. Assign the new payment method "Payment Order with Credit Card" as Incoming Payment Method and assign Incoming Card ID to the contract account of your business partner. Please refer to step Create a Contract Account in the test script of scope item 2AR - Contract Accounting – Master Data and Basic Functions.

#### Post Document

Context

In this activity, you post an open receivable.

Procedure

Please refer to the Post Document step to create a invoice with Transaction Code: Y600/0020 and Payment Method: Payment Order with Credit Card in your company code.

#### Execute Payment Run

Context

In this activity, you execute payment run to post card account to payment order clearing account and create payment order.

Procedure

Please refer to the Execute Payment Run step to post card account to payment order clearing account and create payment order.

|  |
| --- |
| Note For the payment method of payment order with credit card, there is no need to enter the bank selection ID. |

#### Send Payment for Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you send the payment to payment service provider for settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Cards (F3542). | The Application Jobs view displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Settle PaymentsJob Name: FI-CA: Settle Payments |  |  |
| 5 | Enter Required Parameters | Make the following entries and choose Step 3:Start Immediately: <Selected>Start: <Today's date> |  |  |
| 6 | Enter Required Parameters | Make the following entries:Run Settings:Prefix of Run ID: For example, ID0Simulation Run: <Unselect>Selection Criteria:Company Code: <3310>Items to Be Billed: <Selected>Document Number: <Clearing Document Number posted in the Exectue Payment Run step>Further Settings:Document Date: <Today's Date>Posting Date: <Today's Date>Value Date: <Today's Date>Send Payts for Settmt: <Selected> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 9 | Display Job | To view the job details, find your run in the Jobs pane and choose the arrow button to the right of its row. | The Job Log screen displayed.The Run Identification should combine Run ID Prefix + dynamic number (xx).Check the log and get the send status of credit card settlement. |  |

#### Process Received Response from Payment Service Provider

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You can import payment advice note data from Digital Payments Add-On. This procedure is only a mandatory requirement in production environment and the Digital Payment Add-On can only be enabled in production environment as well. If you want to go through this procedure, make sure you have mock report authorization of the back-end system.

Prerequisite

- The answer from PSP should be received. For internal testing purpose, you can use the mock testing program (RFKK_DPH_TEST_EXT_PAY_ADVICE) to generate the answer.
- In production environment, Import Payment Advice Note Data from Digital Payments Add-On function is enabled by Digital Payments Service Provider.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Cards (F3542). | The Application Jobs view displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Settle PaymentsJob Name: FI-CA: Settle Payments |  |  |
| 5 | Enter Required Parameters | Make the following entries and choose Step 3:Start Immediately: <Selected>Start: <Today's date> |  |  |
| 6 | Enter Required Parameters | Make the following entries:Run Settings:Run ID Prefix: For example, ID0Simulation Run: <Unselect>Selection Criteria:Company Code: <3310>Items to Be Billed: <Selected>Document Number: <Clearing Document Number posted in the Execute Payment Run step>Further Settings:Document Date: <Today's Date>Posting Date: <Today's Date>Value Date: <Today's Date>Process Payt Advices: <Selected> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 9 | Display Job | To view the job details, find your run in the Jobs pane and choose the arrow button to the right of its row. | The Job Log screen displayed.The Run Identification should combine Run ID Prefix + dynamic number (xx).Check the log and get the clearing document number for credit card settlement. |  |

#### Post Payment Card Order Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you process the payment card order lot and clear the receivables.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Payment Card Order Lot (F7118). | The Application Jobs screen is displayed. |  |
| 3 | Create | Choose Create. | The New Job screen is displayed. |  |
| 4 | Maintain Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Post Payment Card Order LotsJob Name: FI-CA: Post Payment Card Order Lots |  |  |
| 5 | Maintain Parameters | Make the following entry and choose Step 3:Start Immediately: <Selected> |  |  |
| 6 | Maintain Parameters | Make the following entries:Run Identification:Prefix of Run ID: For example, ID0Simulation run: <Unselect>General Selections:CoCd: <3310>Payment Order: <Payment Order created in the Execute Payment Run step>Data for Posting:Posting Date: <Today's Date>Document Date: <Today's Date>Value Date: <Today's Date> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx).Check the log and get payment card order lot number and the clearing document number for receviable. |  |

#### Display Payment Card Order Lot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display the payment card order lot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Payment Card Order Lots (FP45CC). | The Payment Card Order Lot: Initial Screen is displayed. |  |
| 3 | Maintain Parameters | Enter the following criteria:Lot: <Your payment order lot ID>Choose Display. | Details of payment card order lot are displayed. |  |

### Return Lot Processing from Bank Statement

#### Upload Bank Statement

Context

This section describes the scenario in which money was debited from the company's account following an outgoing payment. Subsequently, customer receives a bank statement confirming that the outgoing payment could not be processed, resulting in the return of the money. In this process step, you upload camt.053 format electronic bank statement in SAP S/4HANA Cloud Public Edition system.

##### camt.053 Format

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This section describes the situation in which the money was debited to the company's account after outgoing payment and customer receives the bank statement, which confirms that the outgoing payment could not be done and the money returns back. In this process step, you upload a camt.053 format electronic bank statement in SAP S/4HANA Cloud Public Edition system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Bank Statements (F1564). | The screen Manage Bank Statements displays. |  |
| 3 | Get Latest Bank Statement Number | To get the latest imported bank statement number, choose Show Filter Bar if search criteria are hidden, and make the following entries:Company Code: 3310House Bank: AEBK2House Bank Account: AEAC2Latest Statement: Latest onlyand choose Go. | The latest bank statement number of the specified bank account displays on the screen Manage Bank Statements.The next bank statement number is one greater than the latest bank statement number. For example, if the latest bank statement number is 00005, the next number is 00006. If no latest bank statement was found, the next number should be 00001. |  |
| 4 | Get Closing Balance of Latest Bank Statement | Make a note of the closing balance of the specified bank account. It can be found on the Manage Bank Statements screen. | The closing balance of the latest bank statement should be the opening balance of the next bank statement. If no latest bank statement was found, the opening balance of the next bank statement should be zero. |  |
| 5 | Open XML File on Your PC | In a text editor, open camt.053_ AEBK2_00006.xml, the text file you previously created in the Prerequisites section. |  |  |
| 6 | Edit XML File | Edit the following values in camt.053 file:<MsgId>20220613104957</MsgId>: Replace 20220613104957 with current time (format YYYYMMDDHHMMSS).<ElctrncSeqNb>34</ElctrncSeqNb>: In this example, 34 is the bank statement number, replace it with the right bank statement number.<Id>0000000693123456</Id>: In this example, 0000000693123456 is the bank account number of house bank/account ID AEBK2/AEAC2. Edit this element if you are not using AEBK2/AEAC2 during testing.<BIC></BIC>: In this example, is the bank key of AEBK2, edit this element if you are not using AEBK2 during testing.<Dt>2022-06-13</Dt>: Replace 2022-06-13 with current date, the format is YYYY-MM-DD. Dt2014-12-22/Dt appears several times in this xml file, replace them all.<Amt Ccy="AED<Amt Ccy="<"> 13875.24 </Amt>: In this example, 13875.24 is the opening balance that is also the closing balance of latest imported bank statement, replace 13875.24 with the real opening balance.<Amt Ccy="AED"> 14875.24 </Amt>: In this example, 14875.24 is the closing balance.<Amt Ccy="AED"> 1000.00 </Amt> In the first <Ntry></ Ntry>: In this example, 1000.00 is the amount of the incoming payment from customer.<CdtDbtInd> DBIT <CdtDbtInd>: DBIT means the value is on credit side.<CdtDbtInd> CRDT <CdtDbtInd>: CRDT means the value is on debit side<ChqNb> 920000032220 </ChqNb>: 920000032220 is the clearing document generated via payment run. Replace document number here with your posted document number.<AddtlNtryInf> DOCUMENT 920000032220 </AddtlNtryInf>: Replace document number here with your posted document number. This ensures the open accounts can be recognized in the original document and cleared without payment lot clarification. |  |  |
| 7 | Access the SAP Fiori App | Open Manage Incoming Payment Files . |  |  |
| 8 | Upload Bank Statement | On the Management Incoming Payment Files screen, choose the Import button, in the Import File dialog box, make the following entries:Incoming File Type: Bank Statement FileFormat: ISO XML Format CAMT.053 for FI-CAUpload Files: choose the plus "+" button and a new dialog box displays. Choose the electronic bank statement file (for example, camt.053_AEBK2_00006.xml) and choose Open. The result is the electronic bank statement file is selected and displays in the Import File dialog box. Choose Process. | File imported: 1 displays. Choose OK, then choose Go on Management Incoming Payment Files screen, the latest imported file is displayed on the first row. You can select the imported file and review the log on the next screen. |  |

#### Returns Lot Creation from Bank Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can create Returns Lot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Transfer Bank Statement (FPB7). | The Data Transfer from Account Statement to Payment/Returns Lot screen is displayed. |  |
| 3 | Enter Required Parameters | Make the following entry:Run Date: <Today's Date>Identification: <For example, ID001>Bank statement transfer: <Selected>Company Code: 3310House Bank: AEBK2House Bank Account: AEAC2Bank Statement Number: <Select Statement Number for Returns lot.>Do not execute allocation in multiple lots: <Selected>Post Lot: <Selected>Lot Key: <For example, RL001>Start immediat.: <Selected>Start Date: <Today's Date> | The corresponding Statement Date and ID are displayed accordingly. |  |
| 4 | Execute | Choose Run. | The Returns Lot is created. |  |
| 5 | Check Result | Choose Job overview. | The Parallel Job - Individual Display screen is displayed. |  |
| 6 | Check Detailed Log | Select the job line. Choose the Show Individual Log button. | The Job Log Entries screen is displayed. The detailed job logs are listed. The Returns Lot key is displayed in log for further step. |  |

#### Display Returns

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Returns history can be listed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Returns (F3126). | The Display Returns screen is displayed. |  |
| 3 | Search Criteria | Enter required parameters for search criteria. |  |  |
| 4 | Execute | Choose Go. | Details of returns are listed. |  |

### Return Lot Processing by Manual Creation

#### Manual Returns Lot Creation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can create payment returns.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Returns Lot (FP09). | Returns: Request Screen is displayed. |  |
| 3 | Enter Return Lot ID | Make the following entry:Returns Lot: <Example: ReturnLot001> |  |  |
| 4 | Create | Choose Create. | The Returns: Specification and Status Display screen is displayed. |  |
| 5 | Maintain Specifications and Status | Company Code: 3310Currency: AEDChoose New Items. |  |  |
| 6 | Input Items | Selection Value: <Input the payment document number generated in payment run and check the returns amount with the payment document>Return reason: Y02Returns Clearing Account: <Choose bank clearing account>House Bank: <For example, AEBK1>Account ID: <For example, AEAC1>Choose Save.Note if you want to check the Clarifications of Returns Lot, you could input * in the Selection Value field. | The Returns: Display line items screen is displayed. |  |
| 7 | Close Returns Lot | Go back to Return Lot: Specification and Status display screen.Choose Close. | The Close lot screen appears. |  |
| 8 | Confirm | Choose Yes. | The return lot is closed.The Returns: Request Screen is displayed again. |  |
| 9 | Post Returns Lot | Choose Post. | The Schedule Job screen is displayed. |  |
| 10 | Start online | Choose Start online. | The return lot is posted successfully. |  |

#### Clarifications of Returns Lot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can clarify open returns lot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Clarify Returns (FPCRL). | The Select screen: Returns lot screen is displayed. |  |
| 3 | Check Search Criteria | Check the following entry:Status≠: 03 |  |  |
| 4 | Execute | Choose Execute. | The Worklist: Return lot screen is displayed. The clarification cases are listed for processing. |  |
| 5 | Open Return Detail | Double-click the clarification case line. | The Returns Detail screen is displayed. |  |
| 6 | Correct Data | Correct returns detail and choose Save. | The correction is saved. |  |
| 7 | Post | Choose Post. | The return document is posted. The return lot is closed. |  |

### Outgoing Payment Processing

#### Post Outgoing Payment Request Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can process outgoing payment to customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen is displayed. |  |
| 3 | Enter Data | Make the following entry:Document Date: <Today's Date>Posting Date: <Today's Date>Document Type: YACurrency: AEDReconcil. Key: <Reconciliation Key generated by system>BP Item: Y01G/L Item: Y01Taxes Calculate Automatically: <Selected> |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to Step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen is displayed. |  |
| 7 | Enter Item Data | Make the following entry:In the Account Assignment section,Business partn.: <Business Partner Number with MKK BP Role>Contract Acct: <Contract Account Number related to the selected BP>Company Code: 3310Transac.: 0750/0010In the Amounts and due dates section,Amount: <Any> | The Statistical Key Z is defaulted. Down Payment is checked. |  |
| 8. | Post | Choose Post. | The Outgoing Payment Request Document is posted . |  |

#### Display Outgoing Payment Request Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, details of previously posted FI-CA document are displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Document (FPE3). | The display Document: Initial Screen is displayed. |  |
| 3 | Enter Data | Make the following entry:Document Number: <Document Number Posted in the Post Document step> |  |  |
| 4 | Execute | Press Enter. | Details of the document are listed. |  |

#### Post Outgoing Payment Document

Context

In this activity, you create outgoing payment document base on outgoing payment request document. To do so, refer to the test script of the scope item 2DP - Contract Accounting – Company Initiated Payments, from chapter Execute Payment Run to chapter Check Payment Documents.

#### Post Credit Memo Document

Context

In this activity, you create credit memo document. To do so, refer to the test script of the scope item 2DP - Contract Accounting – Company Initiated Payments, chapter Post Document.

#### Clear Outgoing Payment documents with Credit Memo

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you clear the outgoing payment document with credit memo for business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Maintain Accounts (FP06). | The Application Jobs screen is displayed. |  |
| 3 | Enter Basic Parameters | Make the following entry:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310Currency: AEDChoose open items.Note |  |  |
| 4 | Choose Items to be Cleared | Choose the open items of the business partner to be cleared.For example,A receivable in the amount of 100 AEDA payable in the amount of 100 AEDClick activate item, check and make sure the difference amount is 0 AED.Choose post.Note Note down the clearing document. |  |  |

### Revenue Distribution

Prerequisite

Before you execute revenue distribution, make sure you've completed the following steps via customizing activities.

1. Maintain the Acct Determ. ID (for example Y1) to contract account APP Change Contract Account (CAA2).
2. Define Specifications for Deriving Final Recipient (via SSCUI: 103640)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Specifications for Deriving Final Recipient | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Define Specifications for Deriving Final Recipient. | The Define Specifications for Deriving Final Recipient: Overview screen is displayed. |  |
| 4 | Input Parameters | Choose Create and make the following criteria for your company code:Company Code: 3310Main Transaction: <For example, *>Sub Transaction: <For example, *>Account Determine. ID: <For example, *>Period Key: <For example, *>Division: <For example, *>Final Recipient: <Contract Account number>Note The contract account assigned to Final Recipient should be different from the contract account of your AR document.Save the entry. | Settings are saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Define Specifications for Deriving Final Recipient | Go to the Business Processes Configuration app and search for the following activity: Define Specifications for Deriving Final Recipient.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Specifications for Deriving Final Recipient: Overview screen is displayed. |  |
| 3 | Input Parameters | Choose Create and make the following criteria for your company code:Company Code: 3310Main Transaction: <For example, *>Sub Transaction: <For example, *>Account Determine. ID: <For example, *>Period Key: <For example, *>Division: <For example, *>Final Recipient: <Contract Account number>Note The contract account assigned to Final Recipient should be different from the contract account of your AR document.Save the entry. | Settings are saved successfully. |  |

#### Post Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In addition to managing your own receivables, you can use the FI-CA component Revenue Distribution to manage receivables for other parties.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen is displayed. |  |
| 3 | Enter Data | Make the following entry:Document Date: <Today's Date>Posting Date: <Today's Date>Document Type: YACurrency: AEDReconcil. Key: <Reconciliation Key generated by system>BP Item: Y01G/L Item: Y01Taxes Calculate Automatically: <Selected> |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to Step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen is displayed |  |
| 7 | Enter Item Data | Make the following entry:In the Account Assignment section,Business partn.: <Business Partner Number with MKK BP Role>Contract Acct: <Contract Account Number related to the selected BP>Company Code: 3310Transac.: Y600/0020In the Amounts and due dates section,Amount: <Any>In the Data for Revenue Distribution section,Final Recipient： <Contract Account Number which you maintain as final recipient in prerequisite step> |  |  |
| 8 | Post | Choose Post. | Document is created. |  |

#### Process Payment Lot

Context

For how to process payment lot to post the payment, please refer to the test script of the scope item 2BI - Contract Accounting – Customer Initiated Payments, chapter Process Payment Lot.

#### Distribute Revenue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Distribute Revenues (FP60M). | The Application Jobs screen is displayed. |  |
| 3 | Choose Create | Choose Create. | The New Job screen is displayed. |  |
| 4 | Maintain Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Distribute RevenuesJob Name: FI-CA: Distribute Revenues |  |  |
| 5 | Maintain Parameters | Make the following entry and choose Step 3:Start Immediately: <Selected> |  |  |
| 6 | Maintain Parameters | Make the following entries:Prefix of Run ID: For example, ID0Posting Date: <Today's Date>Company Code: 3310Business Partner: <Business Partner used in chapter Post Document>Contract Account: <Contract Account used in chapter Post Document>Simulation run.: <Unselected>Problem Class: Additional information |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Post Distribute Revenue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Post Revenue Distribution Documents (F5056). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Post Revenue DistributionJob Name: FI-CA: Post Revenue Distribution |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Posting Parameters | Make the following entries:Posting Date: <Today's Date>Date ID: <Same as the value in Distribute Revenue run>Run ID: <Same as the value in Distribute Revenue run>Simulation run.: UnselectedProblem Class: Additional information |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. One new application job is created with a status. Documents are created from job log details. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Analyze Revenue Distribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Analyze Revenue Distribution - Based on Original Documents (FP60R_NEW). | The Application Jobs screen is displayed. |  |
| 3 | Maintain Parameters | Make the following entry:Business Partner: <Business Partner used in the Post Document step>Company Code: 3310Payment information: <Selected>Simulated Assigned Payment: <Selected> |  |  |
| 4 | Execute | Choose Run. | The Revenue Distribution documents of the business partner is displayed.Note If you see the yellow status which means the distribution item has not been cleared, you could refer to step: Payment Process - Execute Payment Run to do the clearing. After that, you could process step: Reverse Distribute Revenue. |  |

#### Reverse Distribute Revenue

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Reverse Distribution Documents (F5054). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Reversal of Distribution DocumentsJob Name: FI-CA: Reversal of Distribution Documents |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Posting Parameters | Make the following entries:Date ID: <Same as the value in Distribute Revenue run>Run ID: <Same as the value in Distribute Revenue run>Simulation run.: <Unselected> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.Click Results, you could see the details about the reverse information. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Change Document

Context

After posted, FI-CA documents can be changed.

Procedure

Refer to chapter Change Documents of scope item 2BI: Contract Accounting – Customer Initiated Payments.

#### Display Document Changes

Context

FI-CA documents changes can be displayed.

Procedure

Refer to chapter Display Document Changes of scope item 2BI: Contract Accounting – Customer Initiated Payments

#### Maintain Accounts

Context

In this activity, you can maintain business partner account balance.

Procedure

Refer to chapter Account Maintenance of scope item 2BI: Contract Accounting – Customer Initiated Payments.

#### Display Account Balance

Context

Business partner account balanced can be checked with detail documents in this activity.

Procedure

Refer to chapter Check Business Partner Account Balance scope item 2BI: Contract Accounting – Customer Initiated Payments.

#### Business Partner Financial Overview

Context

Business partner financial overview can be checked in this activity.

Procedure

Refer to chapter Business Partner Financial Overview of scope item 2BI: Contract Accounting – Customer Initiated Payments .

#### Reverse Document

Context

In this activity, you can reverse the open receivables and credits of a business partner.

Procedure

Refer to chapter Reverse Document of scope item 2BI: Contract Accounting – Customer Initiated Payments .

#### Reverse Documents

Context

In this activity, you can reverse the open receivables and credits of business partners in batch.

Procedure

Refer to chapter Reverse Documents of scope item 2BI: Contract Accounting – Customer Initiated Payments.

#### Reverse Documents - Mass Run

Context

The mass run for Reverse Documents is used if there are many open receivables and credits of business partners.

Procedure

Refer to chapter Reverse Documents Run scope item 2BI:Contract Accounting – Customer Initiated Payments .

#### Write - Off Items

Context

In this activity, you can write off the open receivables and credits of a business partner.

Procedure

Refer to chapter Write - Off Items of scope item 2BI: Contract Accounting – Customer Initiated Payments.

#### Write-Off Items - Mass Run

Context

The mass run for write off items is used if there are many receivables that are uncollectible, or payables that cannot be disbursed.

Procedure

Refer to chapter Write-Off Items – Mass Run of scope item 2BI: Contract Accounting – Customer Initiated Payments .

#### Display Write-Offs

Context

In this activity, you can quickly and easily access the write-off data for a business partner or contract account.

Procedure

Refer to chapter Display Write-Offs of scope item 2BI: Contract Accounting – Customer Initiated Payments .

#### Manage Documents

Purpose

With the Fiori application Manage Documents(F6109), you can review the status of Contract Account documents. Additionally, you could also create, edit, reverse or write-off documents in this app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Documents(F6109). | The Manage Documents screen is displayed. |  |
| 3 | Adapt Filters | Choose Adapt Filters. Add and remove filters on the filter bar. | The filter bar is adjusted. |  |
| 4 | Enter Parameters | Enter selection filters and press GO. | Documents are listed. |  |
| 5 | Navigate to Detailed Information | Select one document from the list and navigate to the screen that displays the detailed information. | Detailed information of the document is displayed.You could also navigate to Edit,Reverse or Write-Off functions from this screen. |  |

#### Search Payment

Context

Payment overview can be checked in this activity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Search Payments (F2588). | The Search Payments screen is displayed. |  |
| 3 | Enter Filters | Make the following entry and choose Go:Creation Date: <Enter Creation Date of Payment Run to be searched> | The payment lines are listed. |  |
| 4 | Select Document | Click on document number. | The available options are listed for the document. |  |
| 5 | Display Document | Choose Display Document. | Details of the document are displayed in Display Document: Overview screen. |  |

#### Create Payment Media Manually

Context

Payment media can be created manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Payment Media (F3013). | The Create Payment Media screen is displayed. |  |
| 3 | Enter Filters | Make the following entry and choose Go:Run Date: <Enter Run Date of Payment Run to be searched>Run ID: <Enter Run ID of Payment Run to be searched> | The payment groups are listed. |  |
| 4 | Select Payment Groups | Select payment groups. | The available options are activated for the payment group.Note Create Payment Media option is only available when the data of column Number of Payments is not 0. |  |
| 5 | Create Payment Media | Choose Create Payment Media. | Note The Confirmation screen pops up.The Existence Check for Payment Data screen pops up if payment data already exists. |  |
| 6 | Confirm | Choose OK. | System information indicates that a job is scheduled for the payment media creation. |  |
| 7 | Check Notifications | Open Notifications. | The Notifications list is displayed as A payment medium has been created for payment group. |  |
| 8 | Refresh Payment Groups | Choose Go again. | The payment groups are listed. Number of Payments in File of selected payment group is updated. |  |
| 9 | Manage Payment Media | Choose Manage Payment Media. | The Manage Payment Media window is displayed. Check the following entry:Run Date: Date Range Payment Run DateIdentification: Payment Run ID |  |
| 10 | Check Payment Files | Choose Go. | The payment file is listed for further actions. |  |

#### Clarify Exceptions from Payment Run

Context

Payment run exception list is shown.

Prerequisite

Before proceeding with App: Clarify Exceptions from Payment Run, you need to have completed these mandatory configuration steps:

Define Payment Lock Reasons via SSCUI: 102545

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Define Payment Lock Reasons | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose Company Initiated Payments.Choose Configure in the Define Payment Lock Reasons row. | The Define Payment Lock Reasons: Change screen is displayed. |  |
| 4 | Input Parameters | Add an entry:Payment Lock Reason: <for example, A>Name: <for example, Payment Lock>Include in Clarif. Worklist: SelectedValid: Valid Without RestrictionsSave the entry. | Settings for Define Payment Lock Reasons are saved successfully. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Payment Lock Reasons | Go to the Business Processes Configuration app and search for the following activity: Define Payment Lock Reasons.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Payment Lock Reasons: Change screen is displayed. |  |
| 3 | Input Parameters | Add an entry:Payment Lock Reason: <for example, A>Name: <for example, Payment Lock>Include in Clarif. Worklist: SelectedValid: Valid Without RestrictionsSave the entry. | Settings for Define Payment Lock Reasons are saved successfully. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Clarify Exceptions from Payment Run (FPCPR). | The Clarify Exceptions from payment run screen is displayed. |  |
| 3 | Enter Filters | Click Restrict List.In the Clarification Worklist: Payment Program, please double-click Business partner.And enter the Business partner as the filter.Then, choose ExecuteThe clarification worklist appears on the left side of the screen. By switching between the different tab pages, you can choose individual views. You can display all clarification cases in the list, or only those that you are processing.On the right hand side of the screen, tab pages offer you a detailed display of the payment exceptions requiring clarification. | The payment exception list are listed. |  |

#### Sample Bank Statement for Payment Order Lot

|  |
| --- |
| Note For payment order, the External Transactions for FICA are as follows: |

| Format | FICA Transaction Type | External Transaction | Description |
| --- | --- | --- | --- |
| MT940 | 10MTCA | 171 | SEPA DD Payment Orders Incoming (+) |
| MT940 | 10MTCA | 174 | SEPA DD B2B Payment Orders Incoming (+) |
| MT940 | 10MTCA | 177 | SEPA DD B2B Payment Orders Outgoing (-) |
| CAMT.53 | C053CA | PMNTIDDTBBDD | B2B Payment Orders Incoming (+) |
| CAMT.53 | C053CA | PMNTIDDTESDD | Payment Orders Incoming (+) |
| CAMT.53 | C053CA | PMNTICDTESCT- | Payment Orders Outgoing (-) |

##### camt.053 Format

|  |
| --- |
| Sample Code<?xml version="1.0" encoding="UTF-8"?> <Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.053.001.02" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:iso:std:iso:20022:tech:xsd:camt.053.001.02 camt.053.001.02.xsd"> <BkToCstmrStmt> <GrpHdr> <MsgId>20180726040405</MsgId> <CreDtTm>2017-08-25T19:30:47.0+01:00</CreDtTm> <MsgRcpt> <Id> <OrgId> <Othr> <Id>BCS45678</Id> </Othr> </OrgId> </Id> </MsgRcpt> <MsgPgntn> <PgNb>1</PgNb> <LastPgInd>true</LastPgInd> </MsgPgntn> </GrpHdr> <Stmt> <Id>2736482736482</Id> <ElctrncSeqNb>8032 </ElctrncSeqNb> <LglSeqNb>32</LglSeqNb> <CreDtTm>2017-08-25T19:30:47.0+01:00</CreDtTm> <Acct> <Id> <Othr> <Id>2580061</Id> </Othr> </Id> <Ccy>AED</Ccy> <Ownr> <Nm>Name Kontoinhaber</Nm> </Ownr> <Svcr> <FinInstnId> <BIC>82080000</BIC> <Othr> <Id>123456790</Id> <Issr>UmsStId</Issr> </Othr> </FinInstnId> </Svcr> </Acct> <Bal> <Tp> <CdOrPrtry> <Cd>PRCD</Cd> </CdOrPrtry> </Tp> <Amt Ccy="AED">300.00 </Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Dt> <Dt>2018-07-26</Dt> </Dt> </Bal> <Bal> <Tp> <CdOrPrtry> <Cd>CLBD</Cd> </CdOrPrtry> </Tp> <Amt Ccy="AED">400.00 </Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Dt> <Dt>2018-07-26</Dt> </Dt> </Bal> <Ntry> <Amt Ccy="AED">100.00 </Amt> <CdtDbtInd>CRDT</CdtDbtInd> <Sts>BOOK</Sts> <BookgDt> <Dt>2018-07-26</Dt> </BookgDt> <ValDt> <Dt>2018-07-26</Dt> </ValDt> <AcctSvcrRef>Bankreferenz</AcctSvcrRef> <BkTxCd> <Prtry> <Cd>PMNTIDDTBBDD</Cd> </Prtry> </BkTxCd> <NtryDtls> <TxDtls> <Refs> <ChqNb>1000000071</ChqNb> </Refs> <AddtlTxInf>4712</AddtlTxInf> </TxDtls> </NtryDtls> <AddtlNtryInf>4712</AddtlNtryInf> </Ntry> <AddtlStmtInf>FSN Test AddtlStmtInf</AddtlStmtInf> </Stmt> </BkToCstmrStmt> </Document> |

|  |
| --- |
| Note Please replace the transaction on the line <Cd>PMNTIDDTBBDD</Cd>, and the payment order number on the line <ChqNb>1000000071</ChqNb>. For more information, please refer to <camt.053. Format>. |

#### Manage Payment Orders

Context

In this activity, you can display, change, and reverse payment orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Payment Orders(F7651). | The Manage Payment Orders screen is displayed. |  |
| 3 | Maintain Parameters | Make the following entry, and choose Go:Business Partner: <Your Business Partner ID>Status: Open |  |  |
| 4 | Display Payment Order | Choose your item.Note You can choose Reverse to reverse your payment order. | Your payment order document is displayed. |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo-part-01]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2DP_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 121,566 chars in the whole document
