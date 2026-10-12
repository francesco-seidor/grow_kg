---
id: 09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo-part-01
title: Test Script SAP S/4HANA Cloud Public Edition - Contract Accounting – Customer Initiated Payments (2BI_AE) (2BI_S4CLD2608_BPD_EN_AE) — part 1 of 2
description: "Test script for scope item 2BI_AE (FI-CA customer-initiated payments, AED): payment cards, PSP, pay-by-link, payment/check lots, returns, workflows."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-payments]
aliases: []
keywords: [Contract Accounting Incoming and Outgoing Payments, fi-ca document posting, payment card processing, payment service provider, payment by link, payment lot processing, check lot processing, payment clarification, returns processing, bank statement import]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BI_S4CLD2608_BPD_EN_AE.docx#lines-1-2972"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-811
topic: 09-subscription-billing-and-contract-accounting/fi-ca-payments
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Contract Accounting – Customer Initiated Payments (2BI_AE) (2BI_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BI_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–2972 of the extracted text), extracted with `mammoth`. Grouped under **Contract Accounting Incoming and Outgoing Payments** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract Accounting – Customer Initiated Payments (2BI_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232849095)

[2 Prerequisites 6](#_Toc232849096)

[2.1 System Access 6](#_Toc232849097)

[2.2 Roles 6](#_Toc232849098)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232849099)

[2.4 Create Bank and Bank Account 7](#_Toc232849100)

[2.5 Business Conditions 8](#_Toc232849101)

[2.6 Additional Manual Configuration 9](#_Toc232849102)

[3 Overview Table 10](#_Toc232849103)

[4 Test Procedures 14](#_Toc232849104)

[4.1 Post Document with Payment Card Information 14](#_Toc232849105)

[4.1.1 Post Document 14](#_Toc232849106)

[4.1.2 Display Document 19](#_Toc232849107)

[4.2 Business Partner Accounts 20](#_Toc232849108)

[4.2.1 Display Account Balance 20](#_Toc232849109)

[4.2.2 Display Business Transactions 21](#_Toc232849110)

[4.3 Payment Card Processing 22](#_Toc232849111)

[4.3.1 Payment Cards: Process Payments Not Yet Captured by PSP 22](#_Toc232849112)

[4.3.2 Payment Cards: Process Payments Already Captured by PSP 28](#_Toc232849113)

[4.4 Post Document with External Digital Payment Service Provider 31](#_Toc232849114)

[4.4.1 Post Document 31](#_Toc232849115)

[4.4.2 Display Document 38](#_Toc232849116)

[4.5 External Digital Payment Processing 39](#_Toc232849117)

[4.5.1 Payment Service Provider Refund 39](#_Toc232849118)

[4.5.2 Process the Parked Payment Service Provider Advice 44](#_Toc232849119)

[4.5.3 Payment Service Provider Settlement 48](#_Toc232849120)

[4.6 Process Payments Paid via Link 50](#_Toc232849121)

[4.6.1 Import and Process Payment Advices 60](#_Toc232849122)

[4.6.2 Display Process Lot of Payments by Link 62](#_Toc232849123)

[4.6.3 Display Payment Forms 63](#_Toc232849124)

[4.7 Check Business Partner Account Balance 64](#_Toc232849125)

[4.8 Payment Lot Processing 65](#_Toc232849126)

[4.8.1 Payment Lot Creation from Bank Statement (FF_5) 65](#_Toc232849127)

[4.8.1.1 Import Bank Statement 65](#_Toc232849128)

[4.8.1.2 Import Payment Transaction 67](#_Toc232849129)

[4.8.2 Process Payment Lot 70](#_Toc232849130)

[4.8.3 Post Payment Lot 71](#_Toc232849131)

[4.8.4 Clarifications of Payment Lot 73](#_Toc232849132)

[4.8.4.1 Create Repayment 73](#_Toc232849133)

[4.8.4.2 Reverse Repayment Request 74](#_Toc232849134)

[4.8.4.3 Post on Account 75](#_Toc232849135)

[4.8.4.4 Return of Payment on Account to Clarification 76](#_Toc232849136)

[4.8.4.5 Post to G/L (Directly or KUKON) 77](#_Toc232849137)

[4.8.5 Search Payment Lots 80](#_Toc232849138)

[4.9 Check Lot Processing 81](#_Toc232849139)

[4.9.1 Create Check Lot Manually 81](#_Toc232849140)

[4.9.2 Post Check Lot 83](#_Toc232849141)

[4.9.3 Clarifications of Check Lot 84](#_Toc232849142)

[4.9.3.1 Create Repayment 84](#_Toc232849143)

[4.9.3.2 Reverse Repayment Request 86](#_Toc232849144)

[4.9.3.3 Post on Account 87](#_Toc232849145)

[4.9.3.4 Return of Payment on Account to Clarification 88](#_Toc232849146)

[4.9.3.5 Post to G/L Transferring 89](#_Toc232849147)

[4.9.4 Search Check Lots 92](#_Toc232849148)

[4.10 Returns 93](#_Toc232849149)

[4.10.1 Process Returns 94](#_Toc232849150)

[4.10.2 Display Returns 96](#_Toc232849151)

[4.10.3 Print Correspondence 97](#_Toc232849152)

[4.10.4 Display Correspondence 99](#_Toc232849153)

[5 Appendix 100](#_Toc232849154)

[5.1 Process Integration 100](#_Toc232849155)

[5.1.1 Change Document 100](#_Toc232849156)

[5.1.2 Display Document Changes 101](#_Toc232849157)

[5.1.3 Account Maintenance 101](#_Toc232849158)

[5.1.4 Process Receivables 103](#_Toc232849159)

[5.1.5 Manage Business Partner Items 103](#_Toc232849160)

[5.1.6 Business Partner Financial Overview 104](#_Toc232849161)

[5.1.7 Display Account Balance - New Version 105](#_Toc232849162)

[5.1.8 Reverse Document 105](#_Toc232849163)

[5.1.9 Reverse Document (Negative Postings) 106](#_Toc232849164)

[5.1.10 Reverse Documents 111](#_Toc232849165)

[5.1.11 Reverse Documents Run 111](#_Toc232849166)

[5.1.12 Write Off Items - Mass Run 113](#_Toc232849167)

[5.1.13 Manage Documents 114](#_Toc232849168)

[5.1.14 Clarification Returns 115](#_Toc232849169)

[5.1.15 Payment Cards: List of Card Data 116](#_Toc232849170)

[5.1.16 Assign New Reconciliation Key to Payment Lot 117](#_Toc232849171)

[5.1.17 Maintain Payment Advice Note 118](#_Toc232849172)

[5.1.18 Manage Payment Advices 119](#_Toc232849173)

[5.1.19 Takeover Bank Data from Clarification 122](#_Toc232849174)

[5.1.20 Write Off from Clarification 122](#_Toc232849175)

[5.1.21 Overview of Repayment Request 125](#_Toc232849176)

[5.1.22 Monitor Payment Cards 125](#_Toc232849177)

[5.1.23 Flexible Workflow for Document Posting 126](#_Toc232849178)

[5.1.23.1 Post Document 131](#_Toc232849179)

[5.1.23.2 Verify Document 131](#_Toc232849180)

[5.1.23.3 Approve Posted Document (for Processor- Inbox) 132](#_Toc232849181)

[5.1.23.4 Reject Posted Document (for Processor- Inbox) 133](#_Toc232849182)

[5.1.23.5 Reverse or Resent a Rejected Document (Requester) 134](#_Toc232849183)

[5.1.23.5.1 Reverse a Rejected Document (Requester) 135](#_Toc232849184)

[5.1.23.5.2 Resend a Rejected Document (Requester) 135](#_Toc232849185)

[5.1.24 Flexible Workflow for Document Changes 136](#_Toc232849186)

[5.1.24.1 Change Document 141](#_Toc232849187)

[5.1.24.2 Verify Document 141](#_Toc232849188)

[5.1.24.3 Approve Changed Document (for Processor- Inbox) 142](#_Toc232849189)

[5.1.24.4 Reject Document Changes (for Processor - Inbox) 143](#_Toc232849190)

[5.1.24.5 Close the Workflow (Requester) 144](#_Toc232849191)

[5.1.25 Flexible Workflow for Document Reverse 144](#_Toc232849192)

[5.1.25.1 Reverse Document 149](#_Toc232849193)

[5.1.25.2 Verify Document 149](#_Toc232849194)

[5.1.25.3 Approve Document Reversal 150](#_Toc232849195)

[5.1.25.4 Reject the Reversal of Document (for Processor - Inbox) 151](#_Toc232849196)

[5.1.25.5 Close the Workflow (Requester) 151](#_Toc232849197)

[5.2 External Cash Desk 152](#_Toc232849198)

[5.2.1 Create Payment 156](#_Toc232849199)

[5.2.2 Reverse Payment 156](#_Toc232849200)

[5.2.3 Cash Desk Payment Group Closing 157](#_Toc232849201)

[5.2.4 Cash Desk Payment Group Closing Reverse 158](#_Toc232849202)

[5.2.5 Open Item Summary 158](#_Toc232849203)

[5.3 Intraday Bank Statement Posting (Optional) 159](#_Toc232849204)

[5.3.1 Transfer Run for Bank Statements 160](#_Toc232849205)

[5.3.2 Payment Lot Creation from Intraday Bank Statements 161](#_Toc232849206)

[5.3.3 Display Payment Lot 162](#_Toc232849207)

## Purpose

Overview

Paid invoice processing allows you to post invoices that are already paid. You can also manage the payment card settlement process, ending in either a successful transfer to the General Ledger (FI-GL) or returns processing. The payment card process requires an integration of Contract Accounts Receivable and Payable (FI-CA) and Payment Hub (digital payments).

For open item, you can create payment lot to clarify the open item, similarly, check lot to clarify the open item with check. For the payment, you can also choose settlement through payment service provider.

- Post Documents with Payment Card
- Payment Lot Processing
- Payment Card Settlement
- Payment Service Provider Processing
- Check Lot Processing
- Process Returns

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
| Administrator - Accounts Payable and Receivable (FI-CA) | SAP_BR_ADMIN_APR_FICA | Contract Accounting - Jobs | SAP_BR_ADMIN_APR_FICA |  |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

Table 1: Organizational Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |

Table 2: Other Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Business Partner | BP_AE_99 |  |  |
| Contract Account | CA_AE_99 |  |  |

### Create Bank and Bank Account

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

### Business Conditions

Before this scope item can be tested, meet the following business conditions.

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Contract partner and contract account have been created for posting. |
| 2AR - Setting Up Contract Accounting - Master Data and Basic Functions | If you want to use Credit Card and Payment Service Provider functions, please refer to step Configuration Items for Digital Payments. |
| 2BG - Convergent Invoicing – Invoice Creation for Usage and Service | If you want to post payments in order to clear open invoicing documents, please refer to step Perform Invoicing Process. |

### Additional Manual Configuration

Regarding settings for tax date, you have the option to manually adjust the configurations for FI-CA. Please refer to the chapter Additional Manual Configuration in Contract Accounting – Company Initiated Payments (2DP).

## Overview Table

This scope item consists of several process steps listed in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 3: Post Document with Payment Card Information

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Document](#unique_10) [page ] 14 | Accounts Payable and Receivable Accountant (FI-CA) | Post Document (FPE1) | FI-CA document has been posted with Payment Card Information. |
| [Display Document](#unique_11) [page ] 19 | Accounts Payable and Receivable Accountant (FI-CA) | Display Document (FPE3) | FI-CA document detail information displayed. |

Table 4: Business Partner Accounts

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Display Account Balance](#unique_12) [page ] 20 | Accounts Payable and Receivable Accountant (FI-CA) | Display Account Balance (FPL9) | Business Partner open items and account balance displayed. |
| [Display Business Transactions](#unique_13) [page ] 21 | Accounts Payable and Receivable Accountant (FI-CA) | Display Business Transactions (F4294) |  |

Table 5: Payment Card Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Payment Cards: Process Payments Not Yet Captured by PSP](#unique_14) [page ] 22 | Administrator - Accounts Payable and Receivable (FI-CA) | Process Payment Cards (F3542) | Open items can be paid with payment cards. |
| [Payment Cards: Process Payments Already Captured by PSP](#unique_15) [page ] 28 | Administrator - Accounts Payable and Receivable (FI-CA) | Process Payment Cards (F3542) | Import Payment Advice Note Data from Digital Payments Add-On. |

Table 6: Post Document with Payment Service Provider

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post Document](#unique_16) [page ] 31 | Accounts Payable and Receivable Accountant (FI-CA) | Post Document (FPE1) | Open items can be paid with payment cards. |
| [Display Document](#unique_17) [page ] 38 | Accounts Payable and Receivable Accountant (FI-CA) | Display Document (FPE3) | Open item posted with payment cards displayed. |

Table 7: External Digital Payment Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Payment Service Provider Refund](#unique_18) [page ] 39 | Administrator - Accounts Payable and Receivable (FI-CA) | Process Payment Service Providers (F3771) | Get successful status from Payment Service Provider. |
| [Process the Parked Payment Service Provider Advice](#unique_19) [page ] 44 | Administrator - Accounts Payable and Receivable (FI-CA) | Process Payment Service Providers (F3771) | Park the early Advice from Payment Service Provider and get the matched FI-CA document later. |
| [Payment Service Provider Settlement](#unique_20) [page ] 48 | Administrator - Accounts Payable and Receivable (FI-CA) | Process Payment Service Providers (F3771) | Settlement document post successfully. |

Table 8: Process Payments Paid via Link

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Import and Process Payment Advices](#unique_21) [page ] 60 | Administrator - Accounts Payable and Receivable (FI-CA) | Import and Process Payment Advices - for Payments by Link (F6729) | Payment advices are imported and processed. |
| [Display Process Lot of Payments by Link](#unique_22) [page ] 62 | Accounts Payable and Receivable Accountant (FI-CA) | Process Lot (Payment by Link) (FP65) | Posted document is displayed. |
| [Display Payment Forms](#unique_23) [page ] 63 | Accounts Payable and Receivable Accountant (FI-CA) | Display Payment Forms - for Payments by Link (F7105) | Payment forms are displayed. |

Table 9: Check Business Partner Account Balance

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Check Business Partner Account Balance](#unique_24) [page ] 64 | Accounts Payable and Receivable Accountant (FI-CA) | Display Account Balance (FPL9) | Business partner account balance displayed. |

Table 10: Payment Lot Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Payment Lot Creation from Bank Statement (FF_5) |  |  |  |
| [Import Bank Statement](#unique_25) [page ] 65 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Incoming Payment Files (F1680) | Bank Statement import successfully. |
| [Import Payment Transaction](#unique_26) [page ] 67 | Administrator - Accounts Payable and Receivable (FI-CA) | Transfer Bank Statement (FPB7) | The import bank statement transform to payment lot successfully. |
| [Process Payment Lot](#unique_27) [page ] 70 | Accounts Payable and Receivable Accountant (FI-CA) | Process Payment Lot (FP05) | Update the payment lot successfully. |
| [Post Payment Lot](#unique_28) [page ] 71 | Accounts Payable and Receivable Accountant (FI-CA) | Process Payment Lot (FP05) | Close/Post the payment lot successfully. |
| Clarifications Payment Lot |  |  |  |
| [Create Repayment](#unique_29) [page ] 73 | Accounts Payable and Receivable Accountant (FI-CA) | Clarify Incoming Payments (FPCPL) | Repayment request create successfully. |
| [Reverse Repayment Request](#unique_30) [page ] 74 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Repayment Requests (F5754) | Repayment request reversed successfully. |
| [Post on Account](#unique_31) [page ] 75 | Accounts Payable and Receivable Accountant (FI-CA) | Clarify Incoming Payments (FPCPL) | Post on account successfully. |
| [Return of Payment on Account to Clarification](#unique_32) [page ] 76 | Accounts Payable and Receivable Accountant (FI-CA) | Post Payment on Account Back to Clarification Account (FP27) | Post to clarification successfully. |
| [Post to G/L (Directly or KUKON)](#unique_33) [page ] 77 | Accounts Payable and Receivable Accountant (FI-CA) | Clarify Incoming Payments (FPCPL) | Post to G/L account successfully. |
| [Search Payment Lots](#unique_34) [page ] 80 | Accounts Payable and Receivable Accountant (FI-CA) | Search Payments (F2588) | Payment detail information displayed. |

Table 11: Check Lot Processing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Check Lot Manually](#unique_35) [page ] 81 | Accounts Payable and Receivable Accountant (FI-CA) | Process Check Lot (FP25) | Create and save check lot successfully. |
| [Post Check Lot](#unique_36) [page ] 83 | Accounts Payable and Receivable Accountant (FI-CA) | Process Check Lot (FP25) | Post check lot successfully. |
| Clarifications of Check Lot |  |  |  |
| [Create Repayment](#unique_37) [page ] 84 | Accounts Payable and Receivable Accountant (FI-CA) | Process Check Lot (FP25) | Repayment request created successfully. |
| [Reverse Repayment Request](#unique_38) [page ] 86 | Accounts Payable and Receivable Accountant (FI-CA) | Manage Repayment Requests (F5754) | Repayment request reversed successfully. |
| [Post on Account](#unique_39) [page ] 87 | Accounts Payable and Receivable Accountant (FI-CA) | Process Check Lot (FP25) | Post on account successfully. |
| [Return of Payment on Account to Clarification](#unique_40) [page ] 88 | Accounts Payable and Receivable Accountant (FI-CA) | Post Payment on Account Back to Clarification Account (FP27) | Post to clarification successfully. |
| [Post to G/L Transferring](#unique_41) [page ] 89 | Accounts Payable and Receivable Accountant (FI-CA) | Process Check Lot (FP25) | Post to G/L successfully. |
| [Search Check Lots](#unique_42) [page ] 92 | Accounts Payable and Receivable Accountant (FI-CA) | Search Payments (F2588) | Check lots information displayed. |

Table 12: Returns

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Process Returns](#unique_43) [page ] 94 | Accounts Payable and Receivable Accountant (FI-CA) | Process Returns Lot (FP09) | Return lots have been posted. |
| [Display Returns](#unique_44) [page ] 96 | Accounts Payable and Receivable Accountant (FI-CA) | Display Returns (F3126) | The returns history is displayed. |
| [Print Correspondence](#unique_45) [page ] 97 | Administrator - Accounts Payable and Receivable (FI-CA) | Print Correspondence (F3537) | The return notification can be printed. |
| [Display Correspondence](#unique_46) [page ] 99 | Accounts Payable and Receivable Accountant (FI-CA) | Display Correspondences (F3693) | The return notification is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Post Document with Payment Card Information

#### Post Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

FI-CA document is posted with Payment Card Information.

For internal testing purpose, while creating the document, you can choose between two payment card processes: selecting card 'Authorize' only or selecting card 'Authorize + pay'. Depending on which process you select, it will determine the subsequent steps for the payment to be settled.

If you choose to select 'Authorize' when posting the document, you cannot fetch the payment advice from the PSP (payment service provider) directly. In this case, you need to send a request for the capturing of the payment to the PSP first. Only then can you fetch the payment advice and process the payment. In chapter [Payment Cards: Process Payments Not Yet Captured by PSP](#unique_14) [page ] 22, this scenario is referenced as 'payments not captured yet by PSP'.

If you choose to select 'Authorize + Pay' instead of 'Authorize' only, the PSP will automatically receive the request for capturing and does not need to be informed in a separate FI-CA activity. You can directly fetch the payment advice and process the payment. In chapter [Payment Cards: Process Payments Already Captured by PSP](#unique_15) [page ] 28, this scenario is referenced as 'payments captured by PSP'.

Hint for manually creating the FI-CA document with payment card:

You can register the payment card either by posting a document or by maintaining the business partner's master data.

If you haven't registered the payment card information in business partner's master data and want to register it in the document directly, please go to Procedure > Case 1 .

If you have registered the payment card information in the master data of business partner and it is a self-payer, please go to Procedure > Case 2 .

|  |
| --- |
| Note To check and confirm your payment card registration information, see 2AR - Contract Accounting – Master Data and Basic Functions - Create a Business Partner. |

Procedure

Case 1: You want to register the payment cards in the document.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen is displayed. |  |
| 3 | Enter Data | Make the following entries:Document Date: <today's date>Posting Date: <today's date>Document Type: YACurrency: AEDReconcil. Key: <reconciliation key generated by system>Clearing Reason: 01 Incoming PaymentBP Item: Y01G/L Item: Y01Calculate automatically: Select |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to Step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen is displayed. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section:Bus. Partner: <business partner number with MKK BP Role>Contract Acct: <contract account number related to the selected BP>Company Code: 3310Note For posting documents integrated with Provider Contract, you could enter the following information:Contract: <provider contract number>Subappl: PContract Item: <Item no. in provider contract>Transac.: Y600/0020In the Amounts and Due Dates section:Amount: <amount>Note The testing account of paymetric rejects all authorizations above 1,000 AED, so please choose an amount below 1,000.Processing: 9 |  |  |
| 8 | Maintain Card Data | Choose Card Data.If no payment card has been maintained, card registration could be processed as below:On the Enter Payment Data screen, choose Register Card.If your web browser IE encounters "session has expired" issue, use Google Chrome and try again.Make the following entries on the Credit Card Registration screen:Credit Card Type: <payment card type>Card Number: <card number>Name On Card: <owner's name>Valid To: <01/01/2025>CVC: <3-digital number>Choose Submit.Note In testing systems, to maintain Card Type and Card Number, see 2AR - Contract Accounting – Master Data and Basic Functions - Maintain Payment Data. | The Enter Data for Card Payment screen is displayed. |  |
| 9 | Continue | Choose Continue.If you choose Authorize, the payment card will be authorized online with the integrated payment hub. Data will be sent back to Authorization.If you use Payment Card Offline settlement, you should choose Authorize + Pay. | The Information that card data is previously not available appears. |  |
| 10 | Continue | Choose Continue. | The payment card is saved for settlement later in the Payment Card Settlement step.Check the following entry in the Amount and Due Dates section:Tax Code: <Output Tax Code>Net Due Date: <today's date> |  |
| 11 | Post | Choose Post. | The FI-CA document is posted with payment card information. |  |

Case 2: You have registered the payment card in the master data of business partner and it is a self-payer.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen is displayed. |  |
| 3 | Enter Data | Make the following entries:Document Date: <today's date>Posting Date: <today's date>Document Type: YACurrency: AEDReconcil. Key: <reconciliation key generated by system>Clearing Reason: 01 Incoming PaymentBP Item: Y01G/L Item: Y01Taxes Calculate Automatically: Select |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to Step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen is displayed. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section:Bus. Partner: <business partner number with MKK BP Role>Contract Acct: <contract account number related to the selected BP>Company Code: 3310Note For posting documents integrated with Provider Contract, you could enter the information below:Contract: <provider contract number>Subappl: PContract Item: <Item no. in provider contract>Transac.: Y600/0020In the Amounts and Due Dates section:Amount: <amount>Note Please enter an amount below 1,000.Processing: 9Tax Country: <tax country> |  |  |
| 8 | Maintain Alternative Business Partner for Payments Data | In the Alternative business partner for payments section, make the following entries:Partner: <the same business partner as above>Card ID: <select the credit card ID of the business partner>In the Amounts and Due Dates section, choose Card Data, check the credit card information and choose:If you choose Authorize, the payment card will be authorized online with the integrated payment hub. Data will be sent back to Authorization.If you use Payment Card Offline settlement, you should choose Authorize + Pay. | In the Enter Payment Data dialog box:If you choose Authorize, the Authorized Amt should contain the amount and is followed by a green square. On the Authorization tab, authorization data and expiration date information have been generated.If you choose Authorize + Pay, the Authorized Amt should still be 0 and is followed by a green square. On the Authorization tab, there is a Payment ID assigned. |  |
| 9 | Post Document | Choose Continue > Post to post the document. | The FI-CA document is posted with Payment Card Information. |  |

#### Display Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can view the details of previously posted FI-CA documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Document (FPE3). | The Display Document: Initial Screen displays. |  |
| 3 | Enter Data | Make the following entry:Document Number: <document number posted in the Post Document step> |  |  |
| 4 | Execute | Press Enter. | Details of the document are listed. |  |

### Business Partner Accounts

#### Display Account Balance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can view the account balance of a business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Account Balance (FPL9). | The Account Display: InitScrn screen displays. |  |
| 3 | Enter Required Parameters | Make the following entries:Business Partner: <business partner number created in 2AR - Contract Accounting – Master Data and Basic Functions>List Type: All ItemsSort Variant: Net Due Date - descendingLine Layout: Line Item Display with Main&Sub TraInitial Screen: Receivables |  |  |
| 4 | Continue | Choose Continue. |  |  |
| 5 | Check Items Details | Choose the Totals tab and double-click the line item. | The account balance of a business partner is displayed. |  |

#### Display Business Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can view business transactions of a business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Business Transactions (F4294). | The Display Business Transactions screen displays. |  |
| 3 | Enter Required Parameters | Make the following entries and choose Go:Business Partner: <business partner number with MKK BP Role>Contract Account: <contract account number related to the selected BP> | The list of business transactions is displayed. |  |
| 4 | Select Business Transaction | Select one business transaction from the list to check the information in detail. | Detailed information of this transaction is displayed on the right side of the screen and the overview list can still be found on the left side. |  |
| 5 | Select Business Partner | By choosing the Business Partner in one entry, you can see a dialog box that displays links to Business Partner Financial Overview, Display Account Balance and Manage Business Partner Items.Choose links in the dialog box to go to the relevant pages.Choose Back to return to the Display Business Transactions page. | Links to Business Partner Financial Overview, Display Account Balance and Manage Business Partner Items are displayed in the dialog box. Choose links to see more information. |  |
| 6 | Select Contract Account | By choosing the Contract Account in one entry, you can see a dialog box that displays links to Change Contract Account, Display Account Balance, Display Contract Account and Manage Contract Accounts.Choose links in the dialog box to go to the relevant pages.Choose Back to go back to the Display Business Transactions page. | Links to Change Contract Account, Display Account Balance, Display Contract Account and Manage Contract Accounts are displayed in the dialog box. Choose links to see more information. |  |
| 7 | Select Document | Choose the Original Reference Document in one entry, you can navigate to document relevant link pages to change document, display document, etc.Choose the link pops up, you can redirect to the relevant pages.Choose Back to go back to the Display Business Transactions page. | The navigation window of document pops up.Choose the link, you can go to the right page. |  |
| 8 | Display Document | Choose Display Document. | Details of the document are displayed on the Display Document: Overview screen. |  |

### Payment Card Processing

#### Payment Cards: Process Payments Not Yet Captured by PSP

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

As described in the Post Document with Payment Card Information section, there are two different scenarios for the processing of payment cards. In this subchapter, you can test the use case where a document has been posted with payment card action Authorize only. To process the payment in this case, a request for capture has to be sent to the payment service provider (PSP) first via FI-CA program FPCS (activity Send Payments for Settlement). Afterwards you fetch the digital payment advice with the PSP’s response. This allows you to process the payment in a final step via FI-CA program FPCS (activity Process Received Response).

Prerequisite

Make sure you have an already paid FI-CA document with credit card information and Authorize chosen. For detailed steps, please refer to Post Document with Payment Card Information.

|  |
| --- |
| Note If you have different kinds of charge/expense of payment card settlement and need to post the charge/expense to different accounts, then in addition to the settings of Define Specification for Charge Posting (Configuration Activity ID: 101959), please add extra accounts via Define Specifications for Additional Charge Postings (Configuration Activity ID: 106979). |

Procedure

1. Send payments for settlement:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Cards (F3542). | The Application Jobs view displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Settle PaymentsJob Name: FI-CA: Settle Payments |  |  |
| 5 | Enter Required Parameters | Make the following entries and choose Step 3:Start Immediately: SelectStart: <today's date> |  |  |
| 6 | Enter Required Parameters | Make the following entries:In the Run Settings section:Run ID Prefix: for example, ID0Simulation run: DeselectIn the Selection Criteria section:Company Code: 3310Items to Be Billed: SelectDocument Number: <document number posted in step Post Document>In the Further Settings section:Posting Date: <today's date>Document Date: <today's date>Value Date: <today's date>Send Payts for Settmt: SelectNote The Dynamic Date function is available for date parameters. You can also use the Dynamic Date function in combination with the Define Recurrence Pattern feature to schedule recurring mass activities according to your business requirements. For example, you can select the dynamic date function TODAY for testing purposes. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 9 | Display Job | To view the job details, find your run in the Jobs pane and choose the arrow button to the right of its row. | The Job Details screen displays.The Run Identification should combine Run ID Prefix + dynamic number (xx).Check the log and get the successful return code, for example, Code 100. Meanwhile, if you display the document to be settled, in More > Extras > Payment Data > Payment Card Supplement , you can find a green flag status showing with information Payment Service Provider was informed, and the running ID is displayed on the Settlement tab. |  |

In production environment, Import Payment Advice Note Data from Digital Payments Add-On function is enabled by Payment Service Provider.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Cards (F3542). | The Application Jobs view displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: Import Payment Advice Note Data from Digital Payments Add-OnJob Name: Import Payment Advice Note Data from Digital Payments Add-On |  |  |
| 5 | Enter Required Parameters | Make the following entries and choose Step 3:Start Immediately: SelectStart: <today's date> |  |  |
| 6 | Enter Required Parameters | Make the following entries:Run ID Prefix: for example, ID0Type of Digital Payment: Credit Card (CC)Note The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity according to your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 9 | Display Job | To view the job details, find your run in the Jobs pane and choose the arrow button to the right of its row. | The Job Log screen is displayed.The Run Identification should combine Run ID Prefix + dynamic number (xx).Check the log and get the successful return code, for example, Code 100. Meanwhile, if you display the document to be settled, in More > Extras > Payment Data > Payment Card Supplement , you can find a green flag status showing with information Payment Service Provider was informed, and the running ID is displayed on the Settlement tab. |  |

In testing environment, you can use an alternative way to process the step. Import Payment Advice Note Data from Digital Payments Add-On is replaced by means of an answer data program (RFKK_DPH_TEST_EXT_PAY_ADVICE with radio button: Credit Card) as the prerequisite to enable the credit card settlement function. (P_OPBEL: the FICA document you want to process; P_PM1 : Credit Card)

For testing purpose, you can contact the test script author to run this Add-On and obtain the digital payment answer. Then, you can proceed with the settlement steps as outlined below.

|  |
| --- |
| Note You also have a way to complete your payment data before settlement. To do so, you can access the Process Payment Cards (F3542) app using the role Administrator - Accounts Payable and Receivable (FI-CA) and choose the job template FI-CA: Complete Payment Data. SAP offers additional Cloud BAdIs if you need a more flexible way to handle your payment data. For more details, please refer to SAP Help Portal. |

1. Process received response for settlement:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Cards (F3542). | The Application Jobs view displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Settle PaymentsJob Name: FI-CA: Settle Payments |  |  |
| 5 | Enter Required Parameters | Make the following entries and choose Step 3:Start Immediately: SelectStart: <today's date> |  |  |
| 6 | Enter Required Parameters | Make the following entries:In the Run Settings section:Prefix of Run ID: for example, ID0Simulation run: DeselectIn the Selection Criteria section:Company Code: 3310Items to Be Billed: SelectDocument Number: <document number posted in step Post Document>In the Further Settings section:Posting Date: <today's date>Document Date: <today's date>Value Date: <today's date>Process Payt Advices: SelectNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity according to your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 9 | Display Job | To view the job details, find your run in the Jobs pane and choose the arrow button to the right of its row. | The Job Log screen displayed.The Run Identification should combine Run ID Prefix + dynamic number (xx).Check the log and get the clearing document number for credit card settlement. Meanwhile, if you display the document to be settled, in Payment data > Card Data , you can find a green square status showing with information Billing Executed. On the Response tab, the Processing Status is shown as X Processed, and the running ID and billing document are displayed on the Settlement tab. If you double-click the billing document number, you could navigate to display the document. |  |

#### Payment Cards: Process Payments Already Captured by PSP

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this subchapter, you can test the use case where a document has been posted with payment card action Authorize + Pay. It is the standard scenario for companies that already have an integration with a payment service provider. In that case, the PSP will directly receive the request to capture, which makes running FI-CA program FPCS activity Send Payments for Settlement redundant. You can immediately fetch the payment advice and process the payment in a final step via FPCS activity Process Received Response.

Prerequisite

- Make sure you have an already paid FI-CA document with credit card information and Authorize + Pay chosen. For detailed steps, please refer to Post Document with Payment Card Information section.
- In production environment, before you process the settlement, please refer to Import Payment Advice Note Data from Digital Payments Add-On in the step [Payment Cards: Process Payments Not Yet Captured by PSP](#unique_14) [page ] 22.
- For testing purpose, before you process the settlement, you can use the mock testing program (RFKK_DPH_TEST_EXT_PAY_ADVICE) to generate the answer for your digital payment advice.

|  |
| --- |
| NoteIf you have different kinds of charge/expense of payment card settlement and need to post the charge/expense to different accounts, then in addition to the settings of Define Specification for Charge Posting (Configuration Activity ID: 101959), please add extra accounts via Define Specifications for Additional Charge Postings (Configuration Activity ID: 106979).If you need to differentiate the document type among different card types, please display the keys via Menu > Goto > Select keys and choose Used of Payment card type. (via Define Specifications for Posting Settlement Document: 106981) |

|  |
| --- |
| Note You also have a way to complete your payment data before settlement. To do so, you can access the Process Payment Cards (F3542) app using the role Administrator - Accounts Payable and Receivable (FI-CA) and choose the job template FI-CA: Complete Payment Data. SAP offers additional Cloud BAdIs if you need a more flexible way to handle your payment data. For more details, please refer to SAP Help Portal. |

Procedure

In this activity, you process received response for settlement.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Cards (F3542). | The Application Jobs view displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Settle PaymentsJob Name: FI-CA: Settle Payments |  |  |
| 5 | Enter Required Parameters | Make the following entries and choose Step 3:Start Immediately: SelectStart: <today's date> |  |  |
| 6 | Enter Required Parameters | Make the following entries:In the Run Settings section:Run ID Prefix: for example, ID0Simulation Run: DeselectIn the Selection Criteria section:Company Code: 3310Items to Be Billed: SelectDocument Number: <document number posted in the Post Document step>In the Further Settings section:Document Date: <today's date>Posting Date: <today's date>Value Date: <today's date>Process Payt Advices: SelectNote The Dynamic Date function is available for date parameters. You can also use the Dynamic Date function in combination with the Define Recurrence Pattern feature to schedule recurring mass activities according to your business requirements. For example, you can select the dynamic date function TODAY for testing purposes. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 9 | Display Job | To view the job details, find your run in the Jobs pane and choose the arrow button to the right of its row. | The Job Log screen displayed.The Run Identification should combine Run ID Prefix + dynamic number (xx).Check the log and get the clearing document number for credit card settlement. Meanwhile, if you display the document to be settled, in Payment data > Card Data , you can find a green square status showing with information Billing Executed. On the Response tab, the Processing Status is shown as X Processed, and the running ID and billing document are displayed on the Settlement tab. If you double-click the billing document number, you could navigate to display the document. |  |

### Post Document with External Digital Payment Service Provider

#### Post Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

FI-CA documents can be posted with external digital Payment Service Provider information.

Prerequisite

Before you post FI-CA documents with external digital Payment Service Provider information, please check and define the configurations for the Payment Service Provider.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App to Define Account Determination for Payments via Payment Service Provider | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Payment Service Provider, choose Details (>).For the Define Account Determination for Payments via Payment Service Provider row, choose Configure. | The Change View "Payment Service Provider: Account Allocation: Overview” screen is displayed. |  |
| 4 | Add Entries to Define Account Determination for Payments via Payment Service Provider | Choose the chart of accounts:Chart of Accts: YCOAChoose Create and add an entry.Payt Service Prov: <the external digital payment service provider you’d like to use, e.g. DPPP>Company Code: 3310Pymt Serv. Prov. Acct: 12530300Clearing Account: 11001093Save the entry. | Check the entries by going back to the configuration activity. |  |
| 5 | Access App to Specify for Billing Document Posting | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Payment Service Provider, choose Details (>).For the Specification for Billing Document Posting row, choose Configure. | The Change View "Maintain Payment Service Provider: Speccific. Billing Document Posting” screen is displayed. |  |
| 6 | Add Entries to Specify for Billing Document Posting | Choose Create and add an entry.Payt Service Prov: <the external digital payment service provider you’d like to use, e.g. DPPP>Document Type: YASave the entry. | Check the entries by going back to the configuration activity. |  |
| 7 | Access App to Define Specifications for Charge Postings | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Payment Service Provider, choose Details (>).For the Define Specifications for Charge Postings row, choose Configure. | The Change View "Maintain Payment Service Provider: Specifications for Charge Posting" screen is displayed. |  |
| 8 | Add Entries to Define Specifications for Charge Postings | Choose the chart of accounts:Chart of Accts: YCOAChoose Create and add an entry.Payt Service Prov: <the external digital payment service provider you’d like to use, e.g. DPPP>Company Code: 3310Note To post documents integrated with Provider Contract, you could enter the information below:Contract: <provider contract number>Subappl: PContract Item: <Item no. in provider contract>Charges Account: 71000000Account Assgnmt Key: Y02Save the entry. | Check the entries by going back to the configuration activity. |  |
| 9 | Access App to Define Specifications for Automatic Returns Posting | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Payment Service Provider, choose Details (>).For the Define Specifications for Automatic Returns Posting row, choose Configure. | The Change View "Payment Service Provider: Specification for Automatic Returns" screen is displayed. |  |
| 10 | Add Entries to Payment Service Provider: Specification for Automatic Returns | Choose the chart of accounts:Chart of Accts: YCOAChoose Create and add an entry.Payt Service Prov: <the external digital payment service provider you’d like to use, e.g. DPPP>Company Code: 3310Payment Type: <*>Returns: XLot Prefix: P2Returns Reason: Y04Clearing Returns: 12530300Save the entry. | Check the entries by going back to the configuration activity. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Account Determination for Payments via Payment Service Provider | Go to the Business Processes Configuration app and search for the following activity: Define Account Determination for Payments via Payment Service Provider.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Payment Service Provider: Account Allocation: Overview" screen is displayed. |  |
| 3 | Input Parameters | Choose the chart of accounts:Chart of Accts: YCOAChoose Create and add an entry.Payt Service Prov: <the external digital payment service provider you’d like to use, e.g. DPPP>Company Code: 3310Pymt Serv. Prov. Acct: 12530300Clearing Account: 11001093Save the entry. | Entries to define account determination for payments via payment service provider are added. |  |
| 4 | Open Specifications for Billing Document Posting | Go to the Business Processes Configuration app and search for the following activity: Specifications for Billing Document Posting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Maintain Payment Service Provider: Speccific. Billing Document Posting" screen is displayed. |  |
| 5 | Input Parameters | Choose Create and add an entry.Payt Service Prov: <the external digital payment service provider you’d like to use, e.g. DPPP>Document Type: YASave the entry. | Entries to specify for billing document posting are added. |  |
| 6 | Open Define Specifications for Charge Postings | Go to the Business Processes Configuration app and search for the following activity: Define Specifications for Charge Postings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Maintain Payment Service Provider: Specifications for Charge Posting" screen is displayed. |  |
| 7 | Input Parameters | Choose the chart of accounts:Chart of Accts: YCOAChoose Create and add an entry.Payt Service Prov: <the external digital payment service provider you’d like to use, e.g. DPPP>Company Code: 3310Note To post documents integrated with Provider Contract, you could enter the information below:Contract: <provider contract number>Subappl: PContract Item: <Item no. in provider contract>Charges Account: 71000000Account Assgnmt Key: Y02Save the entry. | Entries to define specifications for charge postings are added. |  |
| 8 | Open Define Specifications for Automatic Returns Posting | Go to the Business Processes Configuration app and search for the following activity: Define Specifications for Automatic Returns Posting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Payment Service Provider: Specification for Automatic Returns" screen is displayed. |  |
| 9 | Input Parameters | Choose the chart of accounts:Chart of Accts: YCOAChoose Create and add an entry.Payt Service Prov: <the external digital payment service provider you’d like to use, e.g. DPPP>Company Code: 3310Payment Type: <*>Returns: XLot Prefix: P2Returns Reason: Y04Clearing Returns: 12530300Save the entry. | Entries to define specifications for charge postings are added. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen displays. |  |
| 3 | Enter Data | Make the following entries:Document Date: <today’s date>Posting Date: <today’s date>Document Type: YACurrency: AEDReconcil. Key: <reconciliation key generated by system>Clearing Reason: 01 Incoming PaymentBP Item: Y01G/L Item: Y01Taxes Calculate Automatically: Select |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.Note If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to Step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen is displayed. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section:Business Partner.: <business partner number with MKK BP Role>Contract Acct: <contract account number related to the selected BP>Company Code: 3310Transaction.: Y600/0020In the Amounts and Due Dates section:Amount: <Any amount>Processing: 9 |  |  |
| 8 | Maintain PSP Data | Choose PSP Data.Make the following entries under the Basic Data tab:Payment Service Providers: DPPPPayment Reference: <input reference number with maximum 35 characters>For example, timestamp DDMMYYYYHHMMSS.Choose Continue. |  |  |
| 9 | Post | Choose Post. | The FI-CA document is posted with PSP Information. |  |

#### Display Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, posted FI-CA documents can be displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Document (FPE3). | The Display Document: Initial Screen displays. |  |
| 3 | Select Document to Display | Make the following entry and press ENTER:Document Number: <document number posted in the Post Document step>BP Item: Y01G/L Item: Y01 | The Display Document: Overview screen displays.Details of the document are displayed. |  |

### External Digital Payment Processing

#### Payment Service Provider Refund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The following scenario requires a fully integrated external application, such as a webshop, that processes payments outside of Contract Accounting by sending a request to SAP Digital Payments. Payments must then be posted in Contract Accounting using the external payment reference included in the payment execution response. Typically, this posting step is handled by a billing system, such as Convergent Invoicing.

Buyers can return goods and initiate a refund request using an external payment reference provided by a Payment Service Provider, such as PayPal. In this activity, you can process refunds through the Payment Service Provider using a mass run.

Prerequisite

For testing purpose, you can reach out to the test script author to obtain a testing document. Follow the instructions provided to generate the digital payment Sale ID via a demo workshop page. Once you have the Sale ID, you can proceed with the steps outlined below.

Procedure

1. Post the debit FI-CA document using the Capture Sale Id generated in the prerequisite as the payment reference.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen displays. |  |
| 3 | Enter Data | Make the following entries:Document Date: <today’s date>Posting Date: <today’s date>Document Type: YACurrency: AEDReconcil. Key: <reconciliation key generated by system>BP Item: Y01G/L Item: Y01 |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen displays.If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen displays. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section:Business partner.: <business partner number with MKK BP Role>Contract Acct: <contract account number related to the selected BP>Company Code: 3310Transaction.: Y600/0020In the Amounts and Due Dates section:Amount: <the amount you entered in prerequisite step>Processing: 9 |  |  |
| 8 | Maintain PSP Data | Choose PSP Data.Make the following entries on the Basic Data tab:Payment Service Providers: DPPPPayment Reference: <the sale id you get in the createCharges_Tool.html>Choose Continue. |  |  |
| 9 | Post | Choose Post and record the document number. | The debit FI-CA document is posted with PSP Information. |  |

2. Post a credit FI-CA document to correct the debit document from Step 1.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen displays. |  |
| 3 | Enter Data | Make the following entries:Document Date: <today’s date>Posting Date: <today’s date>Document Type: YACurrency: AEDReconcil. Key: <reconciliation key generated by system>Correction For: <debit document number in prerequisite step>BP Item: Y01G/L Item: Y01Choose Yes in the dialog box. |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen is displayed. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section:Business partner.: <business partner number with MKK BP Role>Contract Acct: <contract account number related to the selected BP>Company Code: 3310Transaction.: Y600/0010In the Amounts and Due Dates section:Amount: <the amount you entered in prerequisite step>Processing: 9 |  |  |
| 8 | Check PSP Data | Choose PSP Data.Check the following entries on the Basic Data tab:Payment Service Providers: DPPPReference of Invoice: <the sale id you get in prerequisite step>Choose Continue. |  |  |
| 9 | Post | Choose Post and record the document number. | The credit FI-CA document is posted with PSP Information. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Service Providers (F3771). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: Request Refund of Credit MemosJob Name: Request Refund of Credit Memos |  |  |
| 5 | Enter Required Parameters | Make the following entries and choose Step 3:Start Immediately: SelectStart: <today's date> |  |  |
| 6 | Enter Required Parameters | Make the following entries:In the Run Settings section:Prefix of Run ID: for example, ID0Simulation run: DeselectIn the Selection Criteria section:Payment Service Providers: DPPPCompany Code: 3310Items to Be Billed: SelectDocument Number: <the document number of the credit FI-CA document>Note The Dynamic Date function is available for date parameters. You can also use the Dynamic Date function in combination with the Define Recurrence Pattern feature to schedule recurring mass activities according to your business requirements. For example, you can select the dynamic date function TODAY for testing purposes. |  |  |
| 7 | Check Job | Choose Check | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 9 | Display Job | To view the job details, find your run in the Jobs pane and choose the arrow button to the right of its row. | The Job Log screen displays.The Run Identification should combine Run ID Prefix + dynamic number (xx).Check the log and get the successful return code, for example, Code 100. Meanwhile, if you display the credit document, in Payment data > Card Data , you can find a green flag status showing with information Payment Service Provider was informed, and the running ID displays on the Settlement tab. |  |

#### Process the Parked Payment Service Provider Advice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

If you receive PSP advices before the document is generated, the system will temporarily hold these advices. Once the document is available in the system, you can proceed to process the parked advices.

Prerequisite

In the testing environment, a demo webshop page is utilized to simulate transactions with the Payment Service Provider (PSP). Please follow the steps below to obtain a Sale Id, retrieve the 'early' payment advice, and create an FI-CA document that corresponds to the payment advice.

1. Get the Sale ID for testing.

You can contact the test script author to obtain a testing document. Follow the provided instructions to generate the digital payment Sale Id using a demo workshop page, and allow at least one day for processing. After this period, you can proceed with the steps outlined below.

2. Fetch the payment advice.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA) role assigned. |  |  |
| 2 | Access App | Open Process Payment Service Providers (F3771) | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Required Parameters | Make the following entries:Job Template: Import Payment Advice Note Data from Digital Payments Add-OnStart Immediately: SelectDate ID: <today’s date>Identification: ID001Start Date: <today’s date>End Date: <today’s date>Type of Digital Payment: EPNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity according to your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 5 | Check Job | Choose Check | System message You can go ahead and schedule the job is displayed. |  |
| 6 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 7 | Display Job | Navigate to the new application job by choosing the information icon. | The Job Log screen displayed. |  |

3. Post one FI-CA document matching with the PSP advice fetched in step 2.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen is displayed. |  |
| 3 | Enter Data | Make the following entries:Document Date: <today’s date>Posting Date: <today’s date>Document Type: YACurrency: AEDReconcil. Key: <reconciliation key generated by system>BP Item: Y01G/L Item: Y01 |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be dispalyed. Please go to Step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen is displayed. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section:Business partner.: <business partner number with MKK BP Role>Contract Acct: <contract account number related to the selected BP>Company Code: 3310Transaction.: Y600/0020In the Amounts and due dates section:Amount: <the amount you entered in the createCharges_Tool.html>Processing: 9 |  |  |
| 8 | Maintain PSP Data | Choose PSP Data.Make the following entries on the Basic Data screen:Payment Service Providers: DPPPPayment Reference: <the Capture Id you get in the createCharges_Tool.html>Choose Continue. |  |  |
| 9 | Post | Choose Post and record the document number. | The debit FI-CA document is posted with PSP Information. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Service Providers (F3771). | The Application Jobs screen is displayed. |  |
| 3 | Create | Choose Create. | The New Job screen is displayed. |  |
| 4 | Enter Required Parameters | Make the following entries:Job Template: Process Parked AdvicesStart Immediately: SelectRun ID Prefix: for example, ID0Date ID: <date in prerequisite step 2 to fetch the PSP advice>Identification: <ID in prerequisite step 2 to fetch the PSP advice>Simulation Run: DeselectNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 5 | Check Job | Choose Check | System message You can go ahead and schedule the job is displayed. |  |
| 6 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 7 | Display Job | To view the job details, find your run in the Jobs pane and choose the arrow button to the right of its row | The Job Log screen displayed.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Payment Service Provider Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can settle documents with payment service provider by mass run.

Prerequisite

In production environment, Import Payment Advice Note Data from Digital Payments Add-On can be enabled by Digital Payments Service Provider.

In testing environment, this function is replaced by means of an answer data program (RFKK_DPH_TEST_EXT_PAY_ADVICE with radio button: Payment Service Providers chosen) as the prerequisite for the payment service provider settlement function (P_OPBEL: the FICA document you want to process; P_PM2: External Payment - PSP).

For testing purpose, you can contact the test script author to run this Add-On to obtain the digital payment answer. Without this, the payment service provider document cannot be settled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Service Providers (F3771). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job screen displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: Payment Service Provider SettlementJob Name: Payment Service Provider Settlement |  |  |
| 5 | Enter Required Parameters | Make the following entries and choose Step 3:Start Immediately: SelectStart: <today's date> |  |  |
| 6 | Enter Required Parameters | Make the following entries:In the Run Settings section:Prefix of Run ID: for example, ID0Simulation Run: DeselectIn the Selection Criteria section:Payment Service Providers: DPPPCompany Code: 3310Document Number: <the number of document that you want to settle>Note If you want to settle the credit memo, input the document number of the credit memo. If you want to settle the original customer invoice, input the document number of the original invoice.In the Further Settings section:Posting Date: <today's date>Document Date: <today's date>Value Date: <today's date>Date ID: <today's date> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.Choose the job finished and check the detailed results. |  |

### Process Payments Paid via Link

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

If you offer customers payment via a link with the invoice, you can either post the payment results with the lot processing manually or regularly request payment advice from the digital payments add-on and process the data.

Prerequisite

Before you start the Payment by Link process, please check and define the required G/L accounts and configurations for Payment by Link.

1. Prepare two G/L accounts with account type X (balance sheet account), one for bank clearing account, the other is for clarification account.

About how to create a new G/L account by copying an existing one, please refer to step Manage G/L Account Master Data in the test script of scope item J58 - Accounting and Financial Close.

1. Set Up Company Codes for Contract Accounts Receivable and Payable (Configuration Activity ID: 101239)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Open Set Up Company Codes for Contract Accounts Receivable and Payable | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingItem Name: OrganizationSearch for Set Up Company Codes for Contract Accounts Receivable and Payable and choose Configure. | The Change View "Company Codes in Contract Accounts Receivable and Payable": Overview screen is displayed. |  |
| 4 | Select Entries for Company Codes | Select an entry for company code 3310.In the Settings for Payment by Link section, make the following entry:For Invoices: <Select>Save the entry. | Check the entries by going again into the configuration activity. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Up Company Codes for Contract Accounts Receivable and Payable | Go to the Business Processes Configuration app and search for the following activity: Set Up Company Codes for Contract Accounts Receivable and Payable.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Company Codes in Contract Accounts Receivable and Payable": Overview screen is displayed. |  |
| 3 | Select Entries for Company Codes | Select an entry for company code 3310.For Invoices: <Select>Save the entry. | Check the entries by going again into the configuration activity. |  |

1. Define Bank Clearing Account (Configuration Activity ID: 102466)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App to Define Bank Clearing Account | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingItem Name: General Payment SettingsSearch for Define Bank Clearing Account and choose Configure. | The "Define Bank Clearing Account": Change screen is displayed. |  |
| 4 | Add New Entry | Choose Create and add an entry.Company Code: 3310Clearing Account: <your Bank clearing account prepared in Prerequisite>Payments by Link-bankclrAcctPaytLink: <Select>Save the entry. | Check the entries by going back to the configuration activity. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Bank Clearing Account | Go to the Business Processes Configuration app and search for the following activity: Define Bank Clearing Account.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The "Define Bank Clearing Account": Change screen is displayed. |  |
| 3 | Add New Entry | Choose Create and add an entry.Company Code: 3310Clearing Account: <your Bank clearing account prepared in Prerequisite>Payments by Link-bankclrAcctPaytLink: <Select>Save the entry. | Bank clearing account for Payment by Link is saved. |  |

1. Specifications for Posting Lots for Payments by Link (Configuration Activity ID: 105800)

|  |
| --- |
| Note The settings for Posting Lots for Payments by Link can vary according to your specific business requirements. The following procedure is provided as an example for your reference; you can adjust these settings to better suit your own business needs. |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App to Specifications for Posting Lots for Payments by Link | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingItem Name: Customer Initiated PaymentsSearch for Specifications for Posting Lots for Payments by Link and choose Configure. | The Maintain Lot for Payments by Link: Specifications for Posting screen is displayed. |  |
| 4 | Add New Entry | Choose the chart of accounts:Chart of Accts: <YCOA>Choose Create and add an entry.Company Code: 3310Payt Service Prov: <For example: *>Payment Type: <For example: *>Bank Clearing Account: <Your Bank clearing account prepared in Prerequisite>Charges Account: <for example: 71000000>Account Assignment Key: <for example: Y02>Tax code for Charge:<for example: A1>Tax Amount Tolerance: <for example: 2>Posting of tax: <for example: 2>Save the entry. | Check the entries by going back to the configuration activity. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Specifications for Posting Lots for Payments by Link | Go to the Business Processes Configuration app and search for the following activity: Specifications for Posting Lots for Payments by LinkChoose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Lot for Payments by Link: Specifications for Posting screen is displayed. |  |
| 3 | Add New Entry | Choose the chart of accounts:Chart of Accts: <YCOA>Choose Create and add an entry.Company Code: 3310Payt Service Prov: <For example: *>Payment Type: <For example: *>Bank Clearing Account: <Your Bank clearing account prepared in Prerequisite>Charges Account: <for example: 71000000>Account Assignment Key: <for example: Y02>Tax code for Charge:<for example: A1>Tax Amount Tolerance: <for example: 2>Posting of tax: <for example: 2>Save the entry. | The specification settings for Posting Lots for Payments by Link is saved. |  |

1. Define Clarification Account (Configuration Activity ID: 102267)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App to Define Clarification Account | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingItem Name: Customer Initiated PaymentsSearch for Define Clarification Account and choose Configure. | The Maintain Incoming Payment Interim Account: Overview screen is displayed. |  |
| 4 | Add New Entry | Choose the chart of accounts:Chart of Accts: <YCOA>Choose Create and add an entry.Company Code: 3310Currency: <for example: AED>Bank Clearing Account: <your Bank clearing account prepared in Prerequisite>Document Type: <for example: *>Clarif. Acct: <your clarification account prepared in Prerequisite>Save the entry. | Check the entries by going back to the configuration activity. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Clarification Account | Go to the Business Processes Configuration app and search for the following activity: Define Clarification Account.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain Incoming Payment Interim Account: Overview screen is displayed. |  |
| 3 | Add New Entry | Choose the chart of accounts:Chart of Accts: <YCOA>Choose Create and add an entry.Company Code: 3310Currency: <for example: AED>Bank Clearing Account: <your Bank clearing account prepared in Prerequisite>Document Type: <for example: *>Clarif. Acct: <your clarification account prepared in Prerequisite>Save the entry. | The clarification account of your bank clearing account is saved for your company code. |  |

1. Define Defaults for Incoming Payments (Configuration Activity: 102873)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App to define Defaults for Incoming Payments | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingItem Name: Clearing ControlSearch for Define Defaults for Incoming Payments and choose Configure. | The Define Defaults for Incoming Payments screen is displayed. |  |
| 4 | Add New Entry | Choose New entries.Clearing Type: <5P>General clearing variant: <014>Post on Acct: <2>No Payment: <Select>Save the entry. | The default value is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Defaults for Incoming Payments | Go to the Business Processes Configuration app and search for the following activity: Define Defaults for Incoming Payments.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Defaults for Incoming Payments screen is displayed. |  |
| 3 | Add New Entry | Choose New entries.Clearing Type: <5P>General clearing variant: <014>Post on Acct: <2>No Payment: <Select>Save the entry. | The default value is saved. |  |

1. Define Defaults for Payments by Link (Configuration Activity ID: 105901)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Defaults for Payments by Link | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingItem Name: Customer Initiated PaymentsSearch for Define Defaults for Payments by Link and choose Configure. | The Payments per Link: Derivation of Configuration of Web Page screen is displayed. |  |
| 4 | Add New Entry | Choose Create and add an entry.Company Code: <3310 or *>ID: <FICACONF01>Note The configuration ID should be defined and maintained in SAP digital payments add-on BTP app and FICACONF01 is only used for testing purpose.Restriction The value will be converted automatically as uppercase and it should not exceed 12 characters.Save the entry. | Default settings for Payment by Link are saved for your company codes. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Defaults for Payments by Link | Go to the Business Processes Configuration app and search for the following activity: Define Defaults for Payments by Link.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Payments per Link: Derivation of Configuration of Web Page screen is displayed. |  |
| 3 | Add New Entry | Choose Create and add an entry.Company Code: <3310 or *>ID: <FICACONF01>Note The configuration ID should be defined and maintained in SAP digital payments add-on BTP app and FICACONF01 is only used for testing purpose.Restriction The value will be converted automatically as uppercase and it should not exceed 12 characters.Save the entry. | Default settings for Payment by Link are saved for your company codes. |  |

1. (Optional) Specify ID for Configuration for Payment by Link (Configuration Activity ID: 105934)

|  |
| --- |
| Note This step is necessary only if the configuration ID has been defined as a mix of upper and lower case letters, or if it exceeds 12 characters in the SAP Digital Payments add-on. In this configuration, ensure that you define an ID consisting of no more than 12 upper-case characters to match the ID specified in the SAP Digital Payments add-on. |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Specify ID for Configuration for Payment by Link | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingItem Name: Customer Initiated PaymentsSearch for Specify ID for Configuration for Payment by Link and choose Configure. | The Specify ID for Configuration for Payment by: Change screen is displayed. |  |
| 4 | Add New Entry | Choose Create and add an entry.ID: <FICACONF01>Payment By Link Configuration ID: <FICACONF01>Note The configuration ID should be defined and maintained in SAP digital payments add-on BTP app. FICACONF01 is only used for testing purpose.Save the entry. | The Configuration ID is specified. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Specify ID for Configuration for Payment by Link | Go to the Business Processes Configuration app and search for the following activity: Specify ID for Configuration for Payment by Link.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Specify ID for Configuration for Payment by: Change screen is displayed. |  |
| 3 | Add New Entry | Choose Create and add an entry.ID: <FICACONF01>Payment By Link Configuration ID: <FICACONF01>Note The configuration ID should be defined and maintained in SAP digital payments add-on BTP app. FICACONF01 is only used for testing purpose.Save the entry. | The Configuration ID is specified. |  |

#### Import and Process Payment Advices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisite

You have integrated the SAP Digital Payments add-on to offer your customers the option to make payments via a link. Receivables paid through this link can be processed in separate payment lots.

Upon completing the convergent invoice posting, a QR code is printed on the convergent invoice document. For details on convergent invoice printing, please refer to scope item 2BG - Convergent Invoicing – Invoice Creation for Usage and Service. Customers can pay the invoice by scanning the QR code provided.

Context

In this activity, you can import and process your payment advices.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Import and Process Payment Advices - for Payments by Link (F6729). | The Application jobs screen is displayed. |  |
| 3 | Enter Basic Parameters | On the Application Jobs screen, choose Create. |  |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Import and Process Payment AdviceJob Name: FI-CA: Import and Process Payment Advice |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Basic Parameters | Make the following entries in the Date Selection section:Start Date: <for example, today’s date -3>End Date: <for example, today’s date> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show detailed post lot IDs and posted documents.Note down your payment lot IDs. |  |

#### Display Process Lot of Payments by Link

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Payment lots for Payments by Link are created after you import and process your payment advices. Payments initiated by business partners through Payment by Link can be processed within these payment lots to automatically clear the open invoices. If the payment lot is posted but the open invoice is not cleared, the items will be posted to an interim account as defined in the customization settings and will be included in a clarification worklist. You can then address the clarification worklist by correcting the payment items, creating repayment requests, posting on account, posting to the GL account, and more.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Lot (Payment by Link) (FP65). | Lot of Payments by Link: Initial Screen displays. |  |
| 3 | Display Payment Lot | Input your payment lot ID on the Lot of Payments by Link: Initial Screen.Lot: <Your payment lot ID>Press Enter.In the Status section, system shows the posting status.Note Posting made means payment is posted successfully.Postprocessing is required means the payment needs further clarification. Refer to the step Clarifications of Payment Lot to process the clarification for lot of Payment by Link.Choose List.On the Payment Lot: Payment Search dialog screen, choose your lot item and choose Payments. | Posted document displays. |  |

#### Display Payment Forms

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can display payment forms for Payments by Link.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Payment Forms - for Payments by Link (F7105). | The Display Payment Forms screen displays. |  |
| 3 | Enter Parameters | Make the following entries according to your business requirements:Payment Form Number: <optional>Business Partner: <optional>Contract Account: <optional>Payment Link Status: <optional>Status: <optional>Payment Form Reference: <optional>Created At: <optional>Choose Go. | Payment forms are listed. |  |
| 4 | Navigate to Detailed Information | Select one payment form from the list and navigate to the screen that displays the detailed information. | Detailed information of the payment form is displayed. |  |

### Check Business Partner Account Balance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can review the detailed account balance of the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Account Balance (FPL9). | The Account Display: InitScrn screen displays. |  |
| 3 | Enter Parameters | Make the following entries:Business Partner: <Business partner number>Contract Account: <Contract account number>Company Code: 3310List Type: All itemsLine Layout: Line Item Display with Main&Sub TransactionSort Variant: Net Due Date – descendingInitial screen: Receivables |  |  |
| 4 | Continue | Choose Continue. | The Account Display: Basic List screen is displayed. Detailed documents of the business partner are listed. |  |

### Payment Lot Processing

#### Payment Lot Creation from Bank Statement (FF_5)

##### Import Bank Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Bank statement file MT940 and CAMT.053 are uploaded.

|  |
| --- |
| Note You can choose either of the two methods to create your bank statement file for testing purpose:Refer to the sample code below and follow the procedure to modify the file during testing.Log onto the GUI system and run transaction code: FPBS1 to generate the sample bank statement automatically. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Incoming Payment Files (F1680) | The Manage Incoming Payment Files screen displays. |  |
| 3 | Maintain Payment Data | On the Incoming Payment Files tab, choose Import.In the Import File dialog box, select Bank Statement.In the Upload Files area, choose the Add button to upload a file.You can also change the format manually.The system will recognize the format according to your uploaded file. Then choose Process.Note Please check the format recognized by the system automatically and correct it if necessary. For FICA, the format description should always include text like 'for FI_CA'.The information screen shows the process status for uploading bank statement.The bank statement file is a text file. You can refer to the following sample example for quick testing.Sample Code{1:F01 0000000000}{2:O9401829041029LRLRXXXX4A0500004554351306031829N}{4: :20:20220518120500 :25:BOFAUS3M/0000000693123456 :28C:00006/1 :60F:C220518AED500,00 :61:220518C100,00NMSC900100000112 :86:051?00TestSAP?20BEL 900100000112?32BP_AE_99 :62F:C220518AED600,00 -}Also, you can refer to the following instructions to edit this file according to your own testing need.Tag:20: (Bank Statement Reference): Use current time as bank statement reference during testing, in format YYYYMMDDHHMMSS, for example 20220518120500.Tag:25: (Account Definition): SWIFT code of bank/account number, for example, BOFAUS3M / 0000000693123456. BOFAUS3M is the SWFIT code of AEBK1, 0000000693123456 is the account number of AEAC1.Tag:28C: Statement number/page number, for example, 00006/1, statement number should be incremented by 1 for a new bank statement.Tag:60F: The opening balance, you can replace 220518 with current date, and amount 500 with your own balance amount.Tag:61: In this example, 220518 is value date (format YYMMDD), you can replace it with current date; 100,00 is the amount of the incoming payment from customer. 900100000112 is the original customer invoice, you can replace it with your real invoice number.Tag:86: In this example, 900100000112 (after indicator ?20BEL ) is the reference of customer invoice (XBLNR), you can replace it with the reference of the customer invoice. BP_AE_Z1 is business partner, you can replace it with your own.Tag:62F: (Closing Balance Information): For example, C220518 AED600,00, you can replace 220518 with current date, in format YYMMDD; replace 600,00 with the calculated closing balance. Note that in the MT940 bank statement file, always use ‘,’ as decimal point (do not use ‘.’). And the date format should be YYMMDD.For more information on bank statement file, please refer to the test script of Bank Integration with File Interface (1EG). | Document xxx is posted in 3310. |  |

##### Import Payment Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

FI-CA document has been posted with customer invoice information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Transfer Bank Statement (FPB7) | The Data Transfer from Account Statement to Payment /Returns Lot screen displays. |  |
| 3 | Maintain Payment Data | Make the following entries on the Data Transfer from Account Statement to Payment/Returns Lot screen:Run Date: <Current date>Identification: <Name your ID>In the Processing mode section:Bank Statement Transfer: <Selected by default>In the Electronic Bank Statement Selection section, make the following entries according to your requirements:Company Code: 3310House Bank: AEBK1 / AEBK2House Bank Account: <optional>Statement Number: <optional>Statement Date: <optional>ID: <optional>In the Account Statement Transfer to Payment/Payment Order/Returns Lot/Check Encashment section, make the following entries according to your requirements:Create Lot: <optional>Close Lot: <optional>Post Lot: <optional>Note Choose one of them only.In the Schedule Transfer section:Start Immediately: SelectChoose Run. | Container is successfully stated. |  |

|  |
| --- |
| Note After you have created the communication scenario - General Ledger Hub Integration (SAP_COM_0696), you can read account statement and create payment lot in SAP S/4HANA Cloud Public Edition system. For more information, you can refer to Contract Accounting – Customer Initiated Payments (2BI) Set-Up Instruction.Before running the App Transfer Bank Statement (FPB7), make sure you have completed the following steps.Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Configure Your Solution:Test Step #Test Step NameInstructionExpected ResultPass / Fail / Comment1Log OnLog on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned.The SAP Fiori Launchpad is displayed.2Access App Manage Your SolutionOpen Manage Your Solution and choose Configure Your Solution.The Manage Your Solution screen is displayed.3Access App Make SpecificationsSearch with following criteria:Application Area: FinanceSub Application Area: Contract AccountingSearch for 105413 in the search help, choose the arrow button at the right end of the row Customer Initiated Payments.Search for the configuration step: Define Selections of Subscriber Account Items, and choose Configure.Add entry to Define the Subscriber Account Items:SrceObj.ID: <for example, Z01>Logical System: <for example, EMTCLNT100>Field Name Bank Statement Item: <optional>Field Value Bank Statement Items: <optional>Description: <optional>Choose Save.SAP Central Business Configuration:Test Step #Test Step NameInstructionExpected ResultPass / Fail / Comment1Log OnLog on to the project experience in SAP Central Business Configuration.The SAP Fiori Launchpad is displayed.2Open Activate Provider Contract Items for Revenue AccountingGo to the Business Processes Configuration app and search for the following activity: Define Selections of Subscriber Account Items.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.3Input ParametersAdd entry to Define the Subscriber Account Items:SrceObj.ID: <for example, Z01>Logical System: <for example, EMTCLNT100>Field Name Bank Statement Item: <optional>Field Value Bank Statement Items: <optional>Description: <optional>Choose Save.When you execute SAP Fiori app Transfer Bank Statement (FPB7), Source ID Bank Statement Item is enabled and you can process the bank statement to generate payment lot. |

#### Process Payment Lot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Payments initiated by business partners can be processed via a payment lot, enabling automatic clearance of open invoices. If a payment lot is posted but fails to clear the open invoice, the items will be posted to an interim account, as defined in the customization settings, and will be added to a clarification worklist. You can then manage the clarification worklist by correcting payment items, creating repayment requests, posting on account, posting to the GL account, and more.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot: Initial Screen displays. |  |
| 3 | Input Parameters for Payment Lot | Create your payment lot ID:Lot: <Your payment lot ID>Choose Create.Make the following entries on the Payment Lot Create: Default Entries and Status screen:In the Control Information section:Lot: <Your payment lot ID>Search Term: <Input your search information>Additional Info: <Input your specific information>In the Specifications for Posting Documents section:Document Type: <by default>Posting Date: <by default>Document Date: <by default>Reconciliation Key: <generated by the system>Currency: AEDIn the Specification for Posting Items on Bank Clearing Account section:Bank Clearing Account: 11001080Company Code: 3310Value Date: <Today's date>In the Selections for Selecting and Clearing Open Items section:Clearing Reason: <01, by default>Selection Category: <by default>Line Layout: SAPChoose New Items.On the Payment Lot Create: Payments screen, check and make the following entries:In the Default Value and Status section, values are maintained by default.In the Payments section:Payment Amount: <Input the amount>Selection Category: <Select G/K/B/P>Note G stands for Business Partner, K stands for Contract Account and B stands for Document.If the parameters you input match the open items, the payment lot can clear the open items for the specific business partner. If not, further clarification will be required.To create a payment lot using a payment advice note, you can either manually create the payment advice note or import payment advices to generate the note. During payment lot creation, you can directly input the payment advice note by selecting category P.Choose Save. | Payment lot is created. |  |

#### Post Payment Lot

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
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot: Initial Screen displays. |  |
| 3 | Post Payment Lot | Input your payment lot ID on the Payment Lot: Initial Screen.Lot: <Your payment lot ID>Choose Close.Note Payment lot must be closed before it can be posted.Choose Yes when message appears: All payment entered in full?Choose Post.Note Clearing variant 014 is delivered and set as default for incoming payment. From 2408 onward, clearing variants have been enhanced with new characteristics and sortings, such as 028 - Item is due (with Deferral), which is assigned to the enhanced clearing variants. You can make adjustment on that basis or create your own new clearing variants via Customizing Activity: 102871-Define Clearing Variants and change the default value for incoming payment via Customizing Activity: 102873-Define Defaults for Incoming Payments.In the Schedule Job dialog box, choose Start online and choose OK.Choose Continue when message appears: Posting run is complete, check status.In the Status section, system shows the posting status.Postprocessing is required means the payment needs further clarification. | Payment lot is closed and posted. |  |

#### Clarifications of Payment Lot

##### Create Repayment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

FI-CA document has been posted for clarification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Clarify Incoming Payments (FPCPL). | The Select. screen: Payment lot screen displays. |  |
| 3 | Input Parameters | Make the following entries on the Select. screen: Payment lot screen:Lot: <Input the payment lot ID>Other fields on the screen are optional, you can input parameters according to your detailed requirements. Also, you can choose the selection fields from the left window for further actions.Then choose Execute.Note Worklist can be displayed.Choose the clarification case and choose Clarify. If the Settings for Clarification Processing dialog box appears, select Continue.Make the following entries on the Item Clarify: Detail and Selections screen:In the Special usage section:Repayment: <Select>Refund method: <Select payment method T>Choose the Repayment Recipient button next to the Refund method field.Input following parameters in the Details of Recipient of Repayment dialog box:Name: <Input name1 and name2>Street address: <Input information for House/Street, Post code/City, District, Country, Region>PO Box address: <Input information for PO box, PO box post code, PO box city>Input following parameters in the Bank Details of Recipient section:For example,Bank Number: <Your bank number>Bank Country: AEBank Account: <Your Bank Account> for example, 12345Account Holder: JohnBIC: <Your BIC number>After checking the completeness of the recipient details, choose Post.Note With this step, a repayment of the payment lot has been created. For out payment, you can run payment program for payment. For more detailed procedure, you can refer to 2DP - Contract Accounting – Company Initiated Payments. | Document of repayment is generated. |  |

##### Reverse Repayment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In the step [Create Repayment](#unique_29) [page ] 73, the payment lot has been postprocessed by creating the repayment request. However, if you find the repayment request is not correct or it is better to clarify the payment lot in other ways afterward, you can reverse the repayment request and go back to clarify the payment again.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Repayment Requests (F5754). | The Manage Repayment Requests screen displays. |  |
| 3 | Reverse Repayment Request | Search for the repayment request:Repayment Request: <search for the repayment request generated in the previous step>Choose GO.Choose the repayment request from the list and choose Reverse.Reversal Date: <input current date>Document Type: <YA or General Document>Reconciliation Key: <by default>Choose Reverse. | Repayment request is reversed. |  |

##### Post on Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The FI-CA document has been posted for clarification. You may create an unclarified payment lot for posting on account once the existing payment lot has been clarified in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Clarify Incoming Payments (FPCPL). | The Select. screen: Payment lot screen displays. |  |
| 3 | Input Parameters | Make the following entry in the Select. screen: Payment lot section:Lot: <Input the payment lot ID>Other selection fields on the screen are optional, you can input the parameters according to your detailed requirements. Also, you can choose the field from left panel for selection.Then choose Execute.Note The incoming payment is automatically posted to a clarification account if the selection specifications in a payment lot are not sufficient.Note If you can't see the payment lot list by choosing Execute, try with the Administrator mode.The worklist is displayed.Choose clarification case and choose Clarify.The new screen Item Clarify: Details and Selections appears.In the Special usage section, select the Post on Acct checkbox.In the Selection proposal section, input your business partner and contract account.Choose Post. | Posting document is generated. |  |

##### Return of Payment on Account to Clarification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The post on account has been created for the clarification of the payment lot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Payment on Account Back to Clarification Account (FP27). |  |  |
| 3 | Input Parameters | Make the following entry on the Return of Payment on Account to Clarification screen:Document Number: <Document generated in the Post on Account step>In the Specification for Reset Posting section, maintain the following parameters:Reconciliation Key: <by default>Posting Date: <current date>Document Type: <YA by default>Choose Open Payment on Account Items.Open items are displayed. Select the item you want to proceed return to clarification and choose Activate item to activate it.Choose Post. | New document has been generated for return to post on account. |  |

##### Post to G/L (Directly or KUKON)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Payment lot clarification has been initiated and requires postprocessing for the G/L transfer. If possible, you may need to create an unclarified payment lot for this step.

Prerequisite

Before you postprocess the payment lot by transfering posting to G/L account, please check and define the configuration for short account assignment to transfer posting.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App to Define Short Account Assignment for Transfer Posting | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Postings and Documents, choose Details (>).For the Define Short Account Assignments for Transfer Postings row, choose Configure. | The Change View "Short Acct Assignment for Transfer Posting (Cloud)": Overview screen is displayed. |  |
| 4 | Add Entries to Define Short Account Assignment for Transfer Posting | Choose New Entries and add an entry:Short Acct Assgt: SAE1Description: Bank1_G/L Transfer Posting_AECompany Code: 3310G/L Account: 11001092Line Item: <Select>Period: 1Save the entry. | Check the entries by going back to the configuration step. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Short Account Assignments for Transfer Postings | Go to the Business Processes Configuration app and search for the following activity: Define Short Account Assignments for Transfer Postings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Short Acct Assignment for Transfer Posting (Cloud)": Overview screen is displayed. |  |
| 3 | Input Parameters | Choose New Entries and add an entry:Short Acct Assgt: SAE1Description: Bank1_G/L Transfer Posting_AECompany Code: 3310G/L Account: 11001092Line Item: <Select>Period: 1Save the entry. | Entries to define short account assignment for transfer posting are added. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Clarify Incoming Payments (FPCPL). | The Select. screen: Payment lot screen displays. |  |
| 3 | Input Parameters | Make the following entry on the Select. screen: Payment lot section:Lot: <Input the payment lot ID>The other selection fields on the screen are optional; you can input parameters according to your specific requirements. Additionally, you can choose fields from the left panel for selection.Then choose Execute.Note The incoming payment is automatically posted to a clarification account if the selection specifications in a payment lot are not sufficient.The worklist is displayed.Choose clarification case and choose Clarify.The new screen Item Clarify: Details and Selections appears.In the Special usage section, maintain the following parameters:TrPosting to: <F4 input your value and search, and choose the suitable one>Posting Text: <Input text>Assignment: <optional>Choose Post. | Document is posted. |  |

#### Search Payment Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can search for payment lots using the SAP Fiori app Search Payments (F2588) and obtain detailed information about the payment lot you want to review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Search Payments (F2588). | The Search Payments screen displays. |  |
| 3 | Enter Paramaters | Make the entries in the following fields:Creation Date: <Enter the creation date of the payment lot>Document Number: <Enter the document number posted in the payment lot>Choose Go. | The payment lots are listed. |  |
| 4 | Select Document | Choose the document number in the entry listed. | Available links for the document are listed. |  |
| 5 | Display Document | Choose Display Document. | Details of the document are displayed on the Display Document: Overview screen. |  |

### Check Lot Processing

#### Create Check Lot Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Similar to payment lot processing, payments initiated by business partners can be managed through a check lot, which automatically clears the open invoices. If a check lot is posted but fails to clear an open invoice, the items will be posted to an interim account defined in the customizing settings and added to a clarification worklist. You can then address the clarification worklist by correcting payment items, creating repayment requests, posting on account, posting to the GL account, and more.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Check Lot (FP25). | The Check Lot: Initial Screen screen is displayed. |  |
| 3 | Process Check Lot | Input your check lot ID and choose Create:Lot: <Your check lot ID>Make the following entries on the Check Lot Create: Default Entries and Status screen:In the Control Information section:Lot: <Your check lot ID>Search Term: <Input your information to search>Additional Info: <Input your specific information>In the Specifications for Posting Documents section:Document Type: <by default>Posting Date: <by default>Document Date: <by default>Reconciliation Key: <by default>Currency: AEDIn the Specification for Posting Items for Check Deposit and Check Clearing section:Check Clearing Account: 11001060Company Code: 3310House Bank: AEBK2Account ID: AEAC2Value Date: <Today's date>Note You can see the No Posting for Check Deposit checkbox, which means you can choose how the check is posted. If you want to make postings to the check deposit account, deselect the indicator. By default, the indicator is selected. You can proceed with both cases.In the Specifications for Selecting and Clearing Open Items section:Clearing Reason: <01, by default>Selection Category: <by default, or you can choose manually>Line Layout: SAPChoose New Items.On the Check Lot Create: Payments screen, check and make the following entries:In the Default Value and Status section, values are maintained by default.In the Payments section:Payment Amount: <Input the amount>Selection Category: <Select P/K/B>Selection Value: <Input the value according to the selection category>Check Number: <Input number as check number>Note In 1805, selection category C for check is not applicable. Here, you just need to input the check number.Choose Save. | Check lot is generated. |  |

#### Post Check Lot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Check lot is generated with ID and is posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Check Lot (FP25) | Check Lot: Initial Screen displays. |  |
| 3 | Process Check Lot | Input your check lot ID on the Check Lot: Initial Screen.Check Lot: <Input Check Lot ID from previous step>Choose Close.Choose Yes when message appears: All payment entered in full?Choose Post.In the Schedule Job dialog box, choose Start online and choose OK.Choose Continue when message appears: Posting run is complete, check status.In the Status section, system shows the posting status.Postprocessing is required means the check lot needs further clarification. | Check lot is posted. |  |

#### Clarifications of Check Lot

##### Create Repayment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Check lot of the FI-CA document has been posted for clarification. One line item has been selected for repayment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Check Lot (FP25). | Check Lot: Initial Screen displays. |  |
| 3 | Input Parameters | Note You can process check lot clarification either via payment lot clarification or via check lot postprocessing. Both methods can be used and option one is adopted here.Input your check lot ID on the Check lot: Initial Screen.Lot: <Input the check lot ID>Then choose Postprocess.Note To postprocess the payment lot, you first need to close it before it can be posted. Postprocessing is needed if the payment lot is not cleared with business partner.The worklist is displayed.Choose clarification case and choose Clarify.Make the following entries on the Item Clarify: Detail and Selections screen:In the Special usage section:Repayment: <Select>Refund Method: <Select payment method T>Choose the button Repayment Recipient next to the Refund method field, then the screen Details of recipient of repayment appears.Input following parameters:Name: <Input the name1 and name2>Street address: <Input information for House/Street, Post code/City, District, Country, Region>PO Box address: <Input information for PO box, PO box post code, PO box city>Input following parameters in the Bank details of recipient section:For example,Bank Number: <Your Bank Number>Bank Country: AEBank Account: <Your Bank Account> for example, 12345Account Holder: JohnBIC: <Your BIC number>After checking the completeness of the recipient details, choose Post.A document of repayment has been generated.Note With this step, a repayment of the payment lot has been created. To trigger the subsequent outgoing payment process, follow the steps detailed in test script 2DP - Contract Accounting – Company Initiated Payments. | Repayment request and document are generated. |  |

##### Reverse Repayment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In the step [Create Repayment](#unique_37) [page ] 84, the check lot has been postprocessed by creating the repayment request. However, if you find that the repayment request is incorrect or it would be better to address the check lot through other means, you have the option to reverse the repayment request and revisit the process to clarify the payment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Repayment Requests (F5754). | The Manage Repayment Requests screen displays. |  |
| 3 | Reverse Repayment Request | Search for the repayment request:Repayment Request: <search for the repayment request generated in the previous step>Choose GO.Choose the repayment request from the list and choose Reverse.Reversal Date: <input current date>Document Type: <YA or General Document>Reconciliation Key: <by default>Choose Reverse. | Repayment request is reversed. |  |

##### Post on Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The check lot for the FI-CA document has been posted for clarification. You may create an unclarified check lot to post on account once the existing check lot has been clarified in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Process Check Lot (FP25). | The Check Lot: Initial Screen is displayed. |  |
| 3 | Input Parameters | On the Check Lot: Initial Screen, maintain the following parameters:Lot: <input the check lot ID>Then choose Postprocess.Note To post-process a payment lot, you must first close and post the payment lot. This post-processing step is necessary if the payment lot is not cleared with the business partner's open items.The worklist is displayed.Choose the clarification case and choose Clarify.The new screen Item Clarify: Details and Selections appears.In the Special usage section, select the Post on Acct checkbox.In the Selection proposal section, input your business partner and contract account.Choose Post. | Document is generated for payment on account. |  |

##### Return of Payment on Account to Clarification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Post on account has been created for payment lot clarification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Payment on Account Back to Clarification Account (FP27). |  |  |
| 3 | Input Parameters | Make the following entry on the Return of Payment on Account to Clarification screen:Document Number: <Input the post on account document in previous step>In the Specification for Reset Posting section, maintain the following parameters:Reconciliation Key: <by default>Posting Date: <current date>Document Type: <YA by default>Choose Open Payment on Account Items.Choose Enter.Open item will be displayed. Select one and choose Activate item to activate it.Choose Post. | New document is generated for reset post on account. |  |

##### Post to G/L Transferring

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

A payment lot clarification has been created. In this activity, you can perform post-processing for the General Ledger (G/L) transfer. If necessary, you may need to create an unclarified check lot for this step.

Prerequisite

Before you postprocess the check lot by transferring posting to G/L account, please check and define the configuration for short account assignment to transfer posting.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App to Define Short Account Assignment for Transfer Posting | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Postings and Documents, choose Details (>).For the Define Short Account Assignments for Transfer Postings row, choose Configure. | The Change View "Short Acct Assignment for Transfer Posting (Cloud)": Overview screen is displayed. |  |
| 4 | Add Entries to Define Short Account Assignment for Transfer Posting | Choose New Entries and add an entry:Short Acct Assgt: S AE 1Description: Bank1_G/L Transfer Posting_ AECompany Code: 3310G/L Account: 11001092Line Item: <Select>Period: 1Save the entry. | Check the entries by going back to the configuration step. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Short Account Assignments for Transfer Postings | Go to the Business Processes Configuration app and search for the following activity: Define Short Account Assignments for Transfer Postings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Short Acct Assignment for Transfer Posting (Cloud)": Overview screen is displayed. |  |
| 3 | Input Parameters | Choose New Entries and add an entry:Short Acct Assgt: S AE 1Description: Bank1_G/L Transfer Posting_ AECompany Code: 3310G/L Account: 11001092Line Item: <Select>Period: 1Save the entry. | Entries to define short account assignment for transfer posting are added. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Check Lot (FP25). | The the Check Lot: Initial Screen view displays. |  |
| 3 | Input Parameters | Make the following entry:Lot: <Input the check lot ID>And then choose Postprocess.Select the item and choose Clarify.In the special usage section, make the following entries:TrPosting to: <F4 input the search value and choose a suitable one>Posting text: <Input text needed>Assignment: <optional>Choose Post. | Document is posted. |  |

#### Search Check Lots

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can use the SAP Fiori app Search Payments (F2588) to search for check lots and obtain detailed information for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Search Payments (F2588). | The Search Payments screen displays. |  |
| 3 | Enter Filters | Make the following entries:Creation Date: <Enter the creation date of the check lot>Document Number: <Enter the document number posted in the check lot>Choose Go. | Check lots are listed. |  |
| 4 | Select Document | Choose the document number in the entry listed. | Available links for the document are listed. |  |
| 5 | Display Document | Choose Display Document. | Details of the document are displayed on the Display Document: Overview screen. |  |

### Returns

Prerequisite

|  |
| --- |
| Note Activate return notification with QR code if you want to use this option, then business partner can pay inovice by scanning QR code. |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Selection Criteria for Credit Clarification | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Organization.Choose the configuration step Set Up Company Codes for Contract Accounts Receivable and Payable and choose Configure. | The Change View " Company Codes in Contract Accounts Receivable and Payable": Overview screen is displayed. |  |
| 4 | Select Entries for Company Codes | Select an entry for company code 3310For Returns: <Select>Save the entry. | Check the entries by accessing the configuration activity again. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Set Up Company Codes for Contract Accounts Receivable and Payable | Go to the Business Processes Configuration app and search for the following activity: Set Up Company Codes for Contract Accounts Receivable and Payable.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View " Company Codes in Contract Accounts Receivable and Payable": Overview screen is displayed. |  |
| 3 | Input Parameters | Select an entry for company code 3310For Returns: <Select>Save the entry. | Check the entries by accessing the configuration activity again. |  |

#### Process Returns

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

Your organization has been informed by its bank that it was unable to collect a payment from the business partner's bank. This could be due to reasons such as insufficient funds, an expired account, an invalid account, or other potential issues.

You can create a return lot either automatically or manually. The following is an example of how to manually create a return lot.

Purpose

In this activity, you can process payment returns.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Returns Lot (FP09). | Returns: Request Screen is displayed. |  |
| 3 | Enter Return Lot ID | Make the following entry:Returns Lot: <for example, RL001> |  |  |
| 4 | Create | Choose Create. | The Returns: Specification and Status Edit screen is displayed. |  |
| 5 | Enter Data | Choose the Specs for docs and processing tab and make the following entries:Company Code: 3310Document Type: YAReconcil. Key: <Enter or select an open reconciliation key>Currency: AEDType of posting: Cancel payment |  |  |
| 6 | Add New Items | Choose New Items. | The Returns: Record/process items screen is displayed. |  |
| 7 | Enter Items Details | Make the following entries:Selection Cat.: B DocumentSelection Value: <Payment document number to be returned>Note Payment document is generated through payment run. you need to first post document with credit memo, then create payment document through payment run. For detailed procedures, see test script of scope item 2DP - Contract Accounting – Company Initiated Payments - Payment Process.Returns Amount: <Amount to be returned>Return Reason: Y03Bank Clrg Acct: <Choose bank clearing account> |  |  |
| 8 | Save | Choose Save. | The entry is saved. |  |
| 9 | Close Returns Lot | Go back to Returns: Request Screen.Choose Close. | The Close lot screen is displayed. |  |
| 10 | Confirm | Choose Yes. | The return lot is closed.The Returns: Request Screen is displayed again. |  |
| 11 | Post Returns Lot | Choose Post. | The Schedule Job screen is displayed. |  |
| 12 | Start online | Choose Start online. | The return lot is posted successfully. |  |

#### Display Returns

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display the history of returns.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Display Returns (F3126). | The Display Returns screen is displayed. |  |
| 3 | Search Criteria | Enter required parameters. |  |  |
| 4 | Execute | Choose Go. | Details of the correspondence are listed. |  |

#### Print Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can print the return notification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Print Correspondence (F3537). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Required Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Print CorrespondenceJob Name: FI-CA: Print Correspondence |  |  |
| 5 | Enter Required Parameters | Make the following entry:Start Immediately: <Select>Choose Define Recurrence Pattern.Recurrence Pattern: <Select Single Run>Note For recurrence setting, select recurrence time cycle.Choose Step 3. |  |  |
| 6 | Enter Required Parameters | Make the following entries:In the Run Settings section:Run ID Prefix: For example, ID0In the Selection Criteria section:Business Partner: <Select business partner number>Contract Account: <Select contract account number>Company Code: 3310Correspondence Type: <Select 0001 Returns>In the Print Parameters section:Actual Print: <Select> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen displays.One new application job is created with a status. |  |
| 9 | Display Job Details | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen displays. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Display Correspondence

Purpose

In this activity, you can display return notification.

|  |
| --- |
| Note If the return notification with QR code is activated, the business partner can make a payment again by scanning the QR code on the return notification. For detailed procedures on how this process works, refer to the chapter Process Payments Paid via Link. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Display Correspondences (F3693). | The Display Correspondences screen displays. |  |
| 3 | Search Criteria | Enter required parameters for search criteria.Business Partner: <Select business partner number>Contract Account: <Select contract account number>Company Code: 3310Correspondence Type: <Select 0001 Returns> |  |  |
| 4 | Execute | Choose Go. | The correspondence details are listed. |  |
| 5 | Display | Select an entry to display. | The details of this entry are displayed, and you can view the QR code on the PDF file either by downloading it or in embedded mode. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Change Document

Context

After being posted, FI-CA documents can be changed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Change Document (FPE2). | The Change Document: Initial Screen is displayed. |  |
| 3 | Select Document | Make the following entry and press ENTER:Document Number: <Document Number Posted in chapterPost Document>BP Item: Y01G/L Item: Y01 | The Change Document: Overview screen is displayed. |  |
| 4 | Select Document Header | Choose menu More > Goto > Document Header. | The Change Document: Header screen is displayed. |  |
| 5 | Enter Change | Make the following entry:Reference: <Enter reference, for example, 910000000001> |  |  |
| 6 | Save | Choose Save. | The change is saved. |  |

#### Display Document Changes

Context

Changes to FI-CA documents can be displayed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Display Document Changes (FPE4). | The Display Document Changes: Initial Screen is displayed. |  |
| 3 | Select Document to Display | Make the following entry and press ENTER:Document Number: <Document number posted in chapterPost Document>ALV Grid: <Select> | The Change Documents: Display All Changes screen is displayed. The document changes are listed. |  |

#### Account Maintenance

Context

In this activity, you can maintain business partner account balance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Maintain Accounts (FP06). | The Account Maintenance: Select Account screen is displayed. |  |
| 3 | Enter Parameters | Make the following entries:Business Partner: <Business partner number>Contract Account: <Contract account number>Company Code: 3310Posting Date: <Today's date>Currency: AEDClearing Reason: 08Document Type: YAReconciliation Key: <Reconciliation key generated by system> |  |  |
| 4 | Select Open Items | Choose Open Items. | The Checking reconciliation key screen appears.If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new Reconciliation Key is created. |  |
| 6 | Continue | Choose Continue. | The Account maintenance: Process Open Items screen is displayed. |  |
| 7 | Activate Item | Select open items and choose Activate item. | The selected open items have been activated. The activated amount is displayed in Gross Clearing field. |  |
| 8 | Post | Choose Post.Note Clearing variant 001 is delivered and set as default for Account maintenance. From 2408 onward, clearing variants have been enhanced with new characteristics and sortings, such as 028 - Item is due (with Deferral), which is assigned to the enhanced clearing variants. You can make adjustment on that basis or create your own new clearing variants via Customizing Activity: 102871-Define Clearing Variants and change the default value for account maintenance via Customizing Activity: 102874-Define Defaults for Account Maintenance. | The open documents are posted.Note The maximum permitted difference is defined in the tolerance group of the contract account. |  |

#### Process Receivables

Context

With scope item 2KH - SAP Fiori Analytical Apps for Contract Accounting Manager being activated, the Accounts Payable and Receivable Manager (FI-CA) can create worklist by using different SAP Fiori apps. In this activity, you can display and process the work items via the app: Process Worklists from Analytical Apps (FPCKWL).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Process Worklists from Analytical Apps (FPCKWL). | The Worklist: Receivables Monitoring screen is displayed. |  |
| 3 | Select Document to Display | Double-click the work item listed in the left panel. | The details of the selected work item are displayed in the Overview panel. The work list is reserved for processing. |  |
| 4 | Clarify Work Item | Choose Clarif. Compltd. | Status of the work list is changed to Resolved. |  |

#### Manage Business Partner Items

Context

In this activity, you can check business partner documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Business Partner Items (F2562). | The Manage Business Partner Items screen is displayed. |  |
| 3 | Enter Filters | Make the following entry:Contract Account: <Select contract account number> |  |  |
| 4 | Execute | Choose Go. | The correspondent documents are listed. |  |
| 5 | Select Document | Choose document number. | The available options are listed for the document. |  |
| 6 | Display Document | Choose Display Document. | Details of the document are displayed on the Display Document: Overview screen. |  |

#### Business Partner Financial Overview

Context

In this activity, you can check business partner financial overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Business Partner Financial Overview (F2429). | The Business Partner Financial Overview screen is displayed. |  |
| 3 | Enter Filters | Make the following entries and choose Go:Business Partner: Business Partner NumberDisplay Currency: AED | Business partner line items are listed. |  |
| 4 | Display | Choose the business partner. | The detailed financial overview of the business partner is displayed. |  |

#### Display Account Balance - New Version

Context

With the SAP Fiori APP Display Account Balance - New Version (F8301), you can check the detailed information of account balance, payments, dunning and business transactions for selected objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Display Account Balance - New Version (F8301). | The Display Account Balance screen is displayed. |  |
| 3 | Enter Filters | Enter the following information on the displayed screen and choose Show Balance:Master Data:Business Partner: <business partner number>Contract Account: <contract account number>Contract: <provider contract number>Additional Data:Company Code: <optional> | The balance report for the selected objects is displayed.Navigate through the different tabs to view detailed information about the documents. |  |

#### Reverse Document

Context

In this activity, you can reverse a document, for example, open or cleared receivable/credits of a business partner, payment run document and payment lot document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Reverse Document - Old Version (FP08). | The Reverse Document screen is displayed. |  |
| 3 | Maintain Parameters to Select the Document | Make the following entry:Document Number: <Enter document number to be reversed>You can choose Adapt Filters to set the filter and then fill in the parameters to select the documents.Choose Go.In the document list, you can click the document number and navigate to relevant Fiori Apps, for example, Display Document.In the document list, you can double-click the document entry and navigate to see some detailed information about this document, for example, the clearing document.Note Reverse archived document by choosing Reverse Archived Document in the upper right corner. | Documents are listed.You can navigate to the Fiori App to display the document.You can navigate to the detailed information page showing the clearing document. |  |
| 4 | Post | Select the radio button in front of the document, choose Reverse.Enter the following parameters:Reversal Date: <Today’s date>Document Type: General DocumentReversal Method: Clear Business Partner ItemsReconciliation Key: <Reconciliation key> | The reversal document posts successfully and in the list of this Fiori App, you can see the reversal document as well. |  |
| 5 | Reverse | Choose Reverse. | The reversal document is posted. The document number is displayed in the Reversal Document column. |  |

#### Reverse Document (Negative Postings)

Context

The transaction figures of the account posted to are reduced by negative postings in the general ledger. Accordingly, a debit posting as a negative posting does not result in an increase of the transaction figures on the debit side, but in a reduction of the transaction figures on the credit side and vice versa. This enables an account with a posting error and respective adjustment (for example, with an invoice posting and reversal) to show transaction figures, which look as if both the incorrect posting and its adjustment never happened.

Prerequisite

Negative Postings are not by default enabled in all countries. Before starting, you firstly need to check whether the company code you plan to post documents allows negative postings.

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 3 | Access App to Check or Configure Company Code G/L Parameter | Search with following criteria:Application Area: FinanceSub Application Area: General LedgerChoose the group Company Codes.Choose the configuration step Company Code Master Data and choose Configure. | The Company Code Master Data screen is displayed. |  |
| 4 | Check and Enable the Negative Postings Indicator in Company Code | Make sure that the Negative Postings Permitted checkbox is selected.If the checkbox for negative postings is not selected and you want to enable it, please choose Edit. On the next screen, select Negative Postings Permitted and save. | The Negative Postings function is successfully enabled on company code level. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access Activity | Go to the Business Processes Configuration app and search for the following activity: Company Code Master Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Company Code Master Data screen is displayed. |  |
| 3 | Check Settings | Make sure that the Negative Postings Permitted checkbox is selected.If the checkbox for negative postings is not selected and you want to enable it, please chooseEdit. On the next screen, select Negative Postings Permitted and save. | The Negative Postings function is successfully enabled on company code level. |  |

Once confirmed that Negative Postings are allowed on company code level, you need to create a new FI-CA document type, which allows negative postings.

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Configure Your Solution screen is displayed. |  |
| 3 | Access App to Check or Configure Company Code G/L Parameter | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Postings and Documents.Choose the configuration step Maintain Document Types and Assign Number Ranges and choose Configure. | The Change View "Maintain Document Types": Overview screen is displayed. |  |
| 4 | Create a New FI-CA Document Type | Choose the New Entries button.Make the following entries:Document Type: N1Description: Negative Posting Document TypeNumber Range: 92Negative Posting: 1 Negative Posting |  |  |
| 5 | Save | Choose Save. | The new FI-CA document type is created, with negative postings indicator selected. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access Activity | Go to the Business Processes Configuration app and search for the following activity: Maintain Document Types and Assign Number Ranges.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Maintain Document Types": Overview screen is displayed. |  |
| 3 | Create a New FI-CA Document Type | Choose the New Entries button.Make the following entries:Document Type: N1Description: Negative Posting Document TypeNumber Range: 92Negative Posting: 1 Negative Posting |  |  |
| 4 | Save | Choose Save. | The new FI-CA document type is created, with negative postings indicator selected. |  |

After all the above prerequisites are completed, please check the account balance for the receivable account (the pre-delivered G/L account by SAP is 12100200) and note down the value. Let’s name it Value 1.

Then post an open invoice for a specific business partner/contract account. You need to transfer the FI-CA posting to G/L and note down the account balance for the receivable account (the pre-delivered G/L account by SAP is 12100200). Let’s name it Value 2.

About how to post open invoice in FI-CA, please refer to 2UJ - Contract Accounting – Open Item Management - Post Documents.

About how to transfer FI-CA posting to G/L, please refer to 2BK - Contract Accounting – Daily and Monthly Closing - Manage Reconciliation Key.

About how to check G/L account balances, please refer to J58 - Accounting and Financial Close - Display G/L Account Balances.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Reverse Document - Old Version (FP08). | The Reverse Document screen is displayed. |  |
| 3 | Maintain Parameters | Make the following entry:Document Number: <Enter document number to be reversed>You can choose Adapt Filters to set the filter and then fill in the parameters to select the documents.Choose Go.In the document list, you can click the document number and navigate to relevant Fiori Apps, for example, Display Document.In the document list, you can double-click the document entry and navigate to see some detailed information about this document, for example, the clearing document. | The documents are listed.You can navigate to the Fiori App to display the document.You can navigate to the detailed information page showing the clearing document. |  |
| 4 | Post | Select the radio button in front of the document, choose Reverse.Maintain the following parameters:Reversal Date: <Today’s date>Document Type: N1Reversal Method: Clear Business Partner ItemsReconciliation Key: <Reconciliation key> | The reversal document posts successfully and in the list of this Fiori App, you can see the reversal document as well. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue | Choose Continue. | The Reverse Document screen is displayed again. |  |
| 7 | Post | Choose Post. | The reversal document is posted. The document number is displayed in the Reversed By field of the Last reversal section. |  |

After successful reversal posting, you need to transfer the FICA document to G/L and note the account balance for the receivable account (the pre-delivered G/L account by SAP is 12100200). Let’s name it Value 3.

Now make the comparison among Value 1, Value 2 and Value 3. The expected result is: Value 1 = Value 3; Value 2 > Value 1.

Besides the reversal of manual receivables posting mentioned in this step, SAP also supports negative postings in the scenarios as returns, clearing reversals, manual credit memo postings and so on. To enable these postings, please check below prerequisites: (1). company code allows negative postings; (2). the document type of returns, clearing reversals and manual credit memos allow negative postings, too.

In the meantime, SAP provides another option for negative postings in the scenario of 2-steps clearing. In this scenario, open receivable is posted after payment on account for the same business partner/contract account, then account maintenance is conducted to clear the 2 open items (open receivable on debit side and payment on account on credit side). After the clearing document is transferred to G/L, the account balance of the receivable account (the pre-delivered G/L account by SAP is 12100200) keeps unchanged. To enable this scenarios, please check below prerequisites: (1). company code allows negative postings; (2). in configuration step 101245: Settings for Main and Sub Transaction, you set the Clearing Must Be Negative Posting indicator for the main and subtransaction that you use for posting payments on account (the pre-delivered main/sub transaction by SAP is 0060/0010).

#### Reverse Documents

Context

The SAP Fiori app Reverse Documents is used when there are many documents, for example, open or cleared receivable/credits of a business partner, payment run documents and payment lot documents you want to reverse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Document Reversal Run (FP08M). | The Mass Reversal view is displayed. |  |
| 3 | Enter Parameters | Make the following entries:Document Number: <Select document numbers to be reversed>Reverse Documents: <Select>Clearing Reason: 05Document Type: YAReversal Date: <Today's date>Simulation Run: <Unselect>ALV Grid Display: <Select> |  |  |
| 5 | Execute Job | Choose Execute.The Mass Reversal window is displayed. Choose Yes to execute the job. | You can see the documents to be reversed and their reversal documents on the screen. |  |

#### Reverse Documents Run

Context

The SAP Fiori app Reverse Documents Run is used when there are many documents, for example, open or cleared receivable/credits of a business partner, payment run documents and payment lot documents you want to reverse.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Reverse Documents Run (F3546) | The Application Jobs view is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job view is displayed. |  |
| 4 | Enter Parameters | Make the following entries:Start Immediately: <Select>Date ID: <Today's date>Run ID Prefix: For example, ID0Document Number: <Select document numbers to be reversed>Clearing Reason; 05Document Type: YAReversal Date: <Today's date>Simulation Run: <Unselect>Note The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the Recurring run for Mass activity for your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 5 | Check Job | Choose Check. | System message You can go ahead and schedule the job displays.Reconciliation key is generated by system. |  |
| 6 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status, you can see the posted documents. |  |

#### Write Off Items - Mass Run

Purpose

The mass run for Write Off items is used if there are many receivables that are uncollectible, or payables that cannot be disbursed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Write Off Run (F3540). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Enter Basic Parameters | Make the following entries:Start Immediately: <Select>Date ID: <Today's date>Identification: For example, ID001Simulation Run: <Unselect> |  |  |
| 5 | Enter Posting Parameters | Make the following entries:Posting Date: <Today's date>Company Code: 3310Clearing Reason: 14Write-Off Reason: Y1Document Type: YAReconciliation Key: <Reconciliation key generated by system>Currency: AED |  |  |
| 6 | Enter General Selections | Make the following entries:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310 |  |  |
| 7 | Enter Additional Selection | Make the following entries:Amount From…To: <Enter amount range>Currency: AED |  |  |
| 8 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 9 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |

#### Manage Documents

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Documents - for Contract Accounting (F6109). | The Manage Documents screen is displayed. |  |
| 3 | Adapt Filters | Choose Adapt Filters. Add and remove filters on the filter bar. | The filter bar is adjusted. |  |
| 4 | Enter Parameters | Enter selection filters and press GO. | Documents are listed. |  |
| 5 | Manage Documents | On the Manage Documents screen:Select the document you want to review and choose the navigation button (>) to the right of the row.On the Document page, you can review the detail information of document on different tabs or choose different options to manage your document. |  |  |
| 6 | Navigate to Different Options | Choose Edit.On the Change Document: Overview screen:Make and save the changes, and go back.Choose Display Document Flow.On the Document Flow page, you can see the connections between all objects that are linked to this document.Go back.Choose Reverse.Go back.Choose Write-Off.On the Write-Off Items page, you have the option to reverse document.Go back.Choose Create dispute case.On the Dispute case page, you have the option to create dispute case for your document.Then go back. |  |  |
| 7 | Navigate to Different Tabs | Header DataHeader information of documentBusiness Partner ItemsBusiness partner items listed of documentNote Select the business partner item you want to review and choose the navigation button (>) to the right of the row. On the Business partner Item page, you can see visualized clearing process of the business partner item by clearing status.G/L Line ItemsG/L line items listed.Tax ItemsTax items listed.Change DocumentsChange log of document.Linked Objects |  |  |

#### Clarification Returns

Context

In this activity, you can clarify open returns lot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Clarify Returns (FPCRL). | The Select screen: Returns lot screen is displayed. |  |
| 3 | Check Search Criteria | Check the following entry:Status≠: 03 |  |  |
| 4 | Execute | Choose Execute. | The Worklist: Return lot screen is displayed. The clarification cases are listed for processing. |  |
| 5 | Open Return Detail | Double-click on the clarification case line. | The Returns Detail screen is displayed. |  |
| 6 | Correct Data | Correct returns details and choose Save. | The correction is saved. |  |
| 7 | Post | Choose Post. | The return document is posted. The return lot is closed. |  |

#### Payment Cards: List of Card Data

Procedure

In this activity, you can check payment cards details.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Payment Card Details (FPPCBP). | The Payment Cards: List of Card Data screen is displayed. |  |
| 3 | Execute | Choose Execute. | All payment cards details are listed on the Payment Cards: List of Card Data screen. The Payment Card Number are encrypted. |  |

#### Assign New Reconciliation Key to Payment Lot

Context

Payment lot has been created and new reconciliation key needs to be assigned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned.Note Use Role ID RECONC_SPEC_APR_FICAReconciliation Specialist - Accounts Payable and Receivable (FI-CA) | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Assign New Reconciliation Key - Payment Lot. | The Assign New Reconciliation Key screen displays. |  |
| 3 | Assign New Reconciliation Key | Make the following entries on the Assign New Reconciliation Key to Payment Lot tab:Lot: <Input payment lot ID>Company Code: 3310Test Run: <optional>Choose Execute. | New reconciliation key for payment lot update run |  |

#### Maintain Payment Advice Note

Context

In this activity, you manually create incoming payment advice from customer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Maintain Payment Advice Note (FPAV). | The Payment Advice Note screen is displayed. |  |
| 3 | Enter Required Parameters | Make the following entry:Payment Note Advice: <Input you ID>Choose Create.On the next screen, input the following parameters:Business Partner: <Input the BP>Note You can use F4 to search for existing BP, or you can refer to the testing result in 2AR - Contract Accounting – Master Data and Basic Functions.Contract Account: <Input the CA>Note You can use F4 to search for existing CA, or you can refer to the testing result in 2AR - Contract Accounting – Master Data and Basic Functions.CoCd payment on acct: 3310Currency: AEDSelection Category: <Select the category, for example, B>In the Field Value column, input value according to selection category.Note The field value is in accordance with the selection category, for example, B stands for Document, K for Contract Account, V for Contract and X for Ref Document.Payment Advice Amount: <Input amount>Total Amount: <Input amount> |  |  |
| 4 | Check Job | Choose Save/Save and Close.Note Save and Close will close the payment advice note, and then you can use this payment advice note in payment lot. | Status is closed. |  |

#### Manage Payment Advices

Context

You can manually create or import payment advices from customer. In this activity, you manually create incoming payment advice from customer via app Manage Payment Advices - Deprecated (F2550).

Prerequisite

With these settings, you can alternatively process payment advice notes for Contract Accounts Receivable and Payable via the Manage Payment Advices app or the Maintain Payment Advice Note app.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App to Define Specifications for Management of Payment Advice Notes | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingItem Name: Customer Initiated PaymentsSearch for Define Specifications for Management of Payment Advice Notes and choose Configure. | The " Define Specifications for Management of Payment Advice Notes ": Change screen is displayed. |  |
| 4 | Add a New Entry | Choose New Entries and make following settings.Activation of Processing in Manage Payment Advices App.Processing in App Active: <Select>Active From: <lower or equal to today>Parallel Processing in Maintain Payment Advice Note App.Active Parallel Display: <Select>Save the settings. | Check the entries by going back to the configuration step. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access App to Define Specifications for Management of Payment Advice Notes | Go to the Business Processes Configuration app and search for the following activity: Define Specifications for Management of Payment Advice NotesChoose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The " Define Specifications for Management of Payment Advice Notes ": Change screen is displayed. |  |
| 3 | Add a New Entry | Choose New Entries and make following settings.Activation of Processing in Manage Payment Advices App.Processing in App Active: <Select>Active From: <lower or equal to today>Parallel Processing in Maintain Payment Advice Note App.Active Parallel Display: <Select>Save the settings. | Check the entries by going back to the configuration step. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Payment Advices - Deprecated (F2550). | The Manage Payment Advices screen displays. |  |
| 3 | Enter Filters | Make the following entries:Company Code: 3310Subledger: <Contract Accounts Receivable and Payable>Choose Go. | A payment advice is created manually. |  |
| 4 | Enter Parameters | Choose Add Manually in the Payment Advices section.Enter the following parameters:Subledger: <Contract Accounts Receivable and Payable>Business Partner : <BP_AE_99>Company Code: 3310Amount: <Total amount of payment advice>Choose the Payment Advice Items tab, and maintain the following parameter:Payment Advice Items: <FI-CA>Choose Create.Maintain the following parameters:Document Date: <For example, today’s date>Payment Amount: <Amount of the open invoice document>Field Value: <Invoice document>Selection category: <B: Document>Repeat steps above to add more documents in this payment advice.Save. |  |  |

#### Takeover Bank Data from Clarification

Context

Business Partner bank information could be changed during clarification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Copy Bank Data from Clarification Cases (FP05BNKD). | The Transfer Bank Details from Clarification Processing screen displays. |  |
| 3 | Input Parameters | Make the following entry on the Transfer Bank Details from Clarification Processing tab:Note This function is to transfer bank information you enter during the clarification process to the business partner master data. For instance, when clarifying, you can update or add a new IBAN and other bank details. After clarification, you can use this function to transfer the updated bank information to the business partner. For testing purposes, you can select a new business partner without existing bank details and create those bank details during clarification /check lot.)In the Parameters section, maintain the following parameters:Test Run: <optional>Transfer IBANS: <Select>List of Bank Details Transferred: <Select>List of Bank Det. Not Transferred: <Select>Choose Execute. | New bank details will be taken over to business partner master data. |  |

#### Write Off from Clarification

Context

Clarification has been generated which will be written off.

Prerequisite

Before you post processing the check lot by transfer posting to G/L account, please check and define the configuration for short account assignment for transfer posting.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App to Define Short Account Assignment for Transfer Posting | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Postings and Documents.Choose the configuration step Define Short Account Assignments for Transfer Postings and choose Configure. | The Change View "Short Acct Assignment for Transfer Posting (Cloud)": Overview screen is displayed. |  |
| 4 | Add Entries to Define Short Account Assignment for Transfer Posting | Choose New Entries and add an entry.Short Acct Assgt: SAE1Description: Bank1_G/L Transfer Posting_AECompany Code: 3310G/L Account: 11001092Line Item: <Select>Period: 1Save the entry. | Check the entries by going again into the configuration step. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Short Account Assignments for Transfer Postings | Go to the Business Processes Configuration app and search for the following activity: Define Short Account Assignments for Transfer Postings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Short Acct Assignment for Transfer Posting (Cloud)": Overview screen is displayed. |  |
| 3 | Input Parameters | Choose New Entries and add an entry.Short Acct Assgt: SAE1Description: Bank1_G/L Transfer Posting_AECompany Code: 3310G/L Account: 11001092Line Item: <Select>Period: 1Save the entry. | Entries to define short account assignment for transfer posting are added. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Write-Off from Clarification Worklist (FPCUM). | The Write-off from Clarification Worklist screen displays. |  |
| 3 | Input Parameters | Make the following entries on the Write-off from Clarification Worklist screen:In the Selection Parameters section:Company Code: 3310Bank Clearing Account: <Select bank clearing account, for example, 11001080>TrPosting to: SAE1/SAE2Other parameters are maintained by default.Choose Execute. | Document is posted. |  |

#### Overview of Repayment Request

Context

In chapters Create Repayment under Payment Lot Processing - Clarifications of Payment Lot and Create Repayment under Check Lot Processing - Clarifications of Check Lot, you can create repayment requests to clarify the payment lots and check lots. In this step, you can review the payment documents relevant to the repayment requests, change the requests, and reverse the requests.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Repayment Requests (F5754). | The Manage Repayment Requests screen displays. |  |
| 3 | Adapt Filters | Choose Adapt Filters to add or remove filters from the filter bar. | The filter bar is adjusted. |  |
| 4 | Enter Selection Filters | Enter selection filters and choose GO. | Repayment requests are listed. |  |
| 5 | Navigate to Detailed Information | Choose a repayment request form from the list and proceed to the screen that displays detailed information. | Detailed information of the repayment request is displayed. |  |

#### Monitor Payment Cards

Context

In this activity, you can monitor the payment card.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Payment Monitor - With Payment Card (FPCA_MON) | The Payment Cards: Monitor screen displays. |  |
| 3 | Input Parameters | Make the following entry on the Payment Monitor with payment card tab:Document Number: <optional>Card Type: <Select>Company Code: 3310Run Data: <Choose your Date ID and Identification>Click Enter | Select result show in half below screen, select each tab for monitoring. |  |

#### Flexible Workflow for Document Posting

Context

Workflow in Contract Accouting enables the approval processing of posting documents. If a document posted meets conditions set in the Manage Workflows for Contract Accounting (F5135) app, it is automatically blocked and routed to approver for action (release/rejection).

During the workflow:

- Approvers receive workflows in SAP inbox and can release/reject the documents.
- After the approver releases the workflow, the documents are unblocked and can go further processing.
- In case of rejection, the document goes back to the requestor’s Inbox. Requestor can reverse the document or resend it for approval.
- If the document is resent to approver, the approval cycle will restart.

It is important to know that the document will always be posted no matter whether a workflow is triggered or not. The only difference is that the document which has a workflow involved is currently ‘blocked’ for certain business process(es) according to the configuration step (103740-Define Check Reasons). In this test case, dummy check reason 01 with below settings will be used in this test script.

| Check Reason | No Payment | No Clearing | No Dunning | No Interest | No Changes |
| --- | --- | --- | --- | --- | --- |
| 01 | X | X | X | X | X |

Prerequisites

Make sure you have implemented scope item 2DP - Company initiated Payments and completed steps below to activate the Flexible Workflow for Document Posting in Contract Accounting.

1. Define Check Reason by configuration step (103740):

It is recommended to create your own check reason for your workflow. If you decide to use standard check reason 01, you could skip this step.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application: Contract AccountingItem Name: Postings and DocumentsChoose step Define Check Reasons and choose Configure.Choose the standard Check Reason 01 and copy it to create your check reason code and adapt the setting according to your business needs. | The Change View "Check Reasons for Dual Control Principle": Overview screen is displayed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Check Reasons | Go to the Business Processes Configuration app and search for the following activity: Define Check Reasons.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Check Reasons for Dual Control Principle": Overview screen is displayed. |  |
| 3 | Input Parameters | Choose the standard Check Reason 01 and copy it to create your check reason code and adapt the setting according to your business needs. |  |  |

1. Activate flexible workflow for posting document:

There are two ways to activate the flexible workflow in Cloud, you can choose either of them to activate your flexible workflow.

-
    1. Via configuration step (103769) - Define Default Check Reason for Workflow

It is recommended to create your own check reason for your workflow. If you decide to use standard Check Reason 01, you could skip this step.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solutionscreen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application: Contract AccountingItem Name: Postings and DocumentsChoose step Define Default Check Reason for Workflow and choose Configure.Choose Create and maintain:Scenario: WS02400073Check Reason: 01Save the entry. | The screen Maintain C003: Overview is displayed.The default check reason assigned to workflow scenario ID.The workflow for contract accounting document is enabled in this client. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Default Check Reason for Workflow | Go to the Business Processes Configuration app and search for the following activity: Define Default Check Reason for Workflow.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The screen Maintain C003: Overview is displayed. |  |
| 3 | Input Parameters | Choose Create and maintain:Scenario: WS02400073Check Reason: 01Save the entry. | The default check reason assigned to workflow scenario ID.The workflow for contract accounting document is enabled in this client. |  |

-
    1. Implement Cloud BAdI: FI-CA Dual Control Principle: New Document/Check (FKK_EVENT_5500) and assign the check reason into the BAdI:

If you need more conditions to trigger your workflow and configuration step could not meet your business requirement, you could implement Cloud BAdI: FI-CA Dual Control Principle: New Document/Check (FKK_EVENT_5500).

|  |
| --- |
| Note There is a certain priority for deriving the check reason. If you have implemented the check reason in the Cloud BAdI 5500, the configuration in the configuration step (103769) - Define Default Check Reason for Workflow can be ignored. |

1. Define and activate your approval workflows:

You can create a new workflow by copying the standard template or create a new entry directly. In this activity, you create the new workflow by copying standard template.

|  |
| --- |
| Note You can have multiple active workflows and could define or sort the order. The system will go through all the active workflows from the first order to the last until the workflow could be started. If the system could determine a workflow which could start a workflow process, the others will be ignored. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. |  |  |
| 2 | Access SAP Fiori App | Open Manage Workflows for Contract Accounting (F5135). | The Manage Workflows view displays. |  |
| 3 | Choose | Choose Workflow for Posting Documents and then choose Workflow Template. |  |  |
| 4 | Copy Workflow | Choose Copy. | The Copy of Workflow screen displays. |  |
| 5 | Enter Workflow Details | Make the following entries and choose Save:On the Header tab:Name: for example, Contract Document Posting WorkflowOn the Properties tab:Description: <Enter your description>Valid from: <Today's date for example>Valid to: <12/31/9999 for example>On the START CONDITIONS tab:Only start the workflow if all of the following preconditions are met:Main transaction is X and sub transaction is YMain transaction = Y600 sub transaction = 0010Choose Add to add another condition.On the Add Alternative Preconditions tab: (Optional)On the Step Sequence tab, choose the first sequence and modify:Step Name: for example, Contract Accounting Document approvalStep Type: Contract Accounting Document approvalOn the Recipients tab:Assignment By: RoleRole: Function for Approving-Level 1On the Step Conditions tab: (add the following as an example)Absolute credit amount in transaction currency of a business partner item is the same or greater than = 30000 AEDOn the EXCEPTION HANDLING tab:Name: Document Is to Be Sent for ReversalRequired Action: Posting reversalAction Result: Cancel workflow | The workflow is saved. |  |
| 6 | Activate Rule | Choose Apply, then choose Save and Activate.Note The template workflow is delivered by default as active with no preconditions defined, which means this workflow will always start, make sure you deactive the standard template if you don’t want to use it before you start your document postings. | The workflow Contract Document Posting Workflow is activated. |  |

1. Define responsibility for rules used in workflow steps and assign users to responsibilities.

|  |
| --- |
| Note The approver(s) and requester(s) must be different business users. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on on to the SAP Fiori launchpad as Business Process Specialist. |  |  |
| 2 | Access SAP Fiori App | Open Manage Teams and Responsibilities (F2412). |  |  |
| 3 | Create Team | Choose Create. | The Team view displays. |  |
| 4 | Enter Team Details | Make the following entries on the General Information tab:Name: for example, Contract Accounting approverStatus: Ready to useType: SFICAWF (Contract Accounting workflow team) |  |  |
| 5 | Enter Team Details | Choose the Team Members tab. |  |  |
| 6 | Enter Team Details | Choose Create. | A blank field displays under Business Partner. |  |
| 7 | Enter Team Details | Make the following entries and choose Save:Business Partner: For example, Example Accounts Payable and Receivable ManagerFunction: Function for Approving-Level 1 | The responsibility for the Contract Document Posting workflow is defined |  |

##### Post Document

Context

After you have completed all the prerequisite steps and set the start conditions with Main transaction Y600 and Subtransaction 0010 and set Amount > 30000 AED in step Define and Activate Your Approval Workflows, and you can post a document to start the workflow. Once the posting document meets the start conditions, the workflow starts, the system automatically sets the check reason in document header and a new item is sent to recipient’s Inbox as well as the notification list for actions. The document requires confirmation from approver for further processing (Automatic Payments, Dunning and so on) according to your check reason settings in configuration step (103740). If the document is released by approver, the check reason is automatically removed from the document header and the document can go for further processing.

In this activity, you post a document with Main transaction Y600 and Subtransaction 0010 and set Amount >30000 AED to trigger the workflow. For detailed procedure, see 2DP - Contract Accounting – Company Initiated Payments - Post Document.

##### Verify Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can verify a document blocked by workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Document (FPE3). | The Display Document: Initial screen is displayed. |  |
| 3 | Select Document to Display | Make the following entry and choose More > Goto > Document > Header :Document Number: <Document number posted in step Post Document>BP Item: Y01G/L Item: Y01 | The Display Document: Overview screen is displayed. The document details are displayed.On the Additional Data tab:The message Posting Must Be Confirmed with Check Reason is displayed. |  |
| 4 | Select Document to Change | Choose menu More > Document (Display->Change) . | The message Document cannot be changed until confirmed due to check reason Dummy Check Reason is displayed.Note You have this message as you've selected No Changes in your check reason. |  |

##### Approve Posted Document (for Processor- Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You receive contract accounting documents that need to be checked. After checking the documents, you can either release or reject with a comment or reason. Once a document has been selected and released, it disappears from the list. If a document is released, the released document can go for further processing.

|  |
| --- |
| Note You can set a substitute when you are absent and could not access your Inbox. To do so, go to My Inbox and access the Substitute function from your profile. |

Purpose

In this activity, you access Inbox as an approver and release the document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Inbox for FI-CA (F5136). | My Inbox view displays. |  |
| 3 | Approve Documents | Select the document to be released.Choose Release. | The document is released.Note All released documents are displayed in the My Outbox - Outbox items app.And the message Posting Must Be Confirmed with Check Reason Dummy Check Reason disappeared in the document header. |  |

##### Reject Posted Document (for Processor- Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You receive posted contract accounting documents that need to be checked. After checking the documents, you can either approve or reject with a comment or reason. Once a document has been selected and rejected, it disappears from the list and goes back to the requester.

Purpose

In this activity, you access Inbox as a approver and reject the document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Inbox for FI-CA (F5136). | The My Inbox view displays. |  |
| 3 | Reject Documents | Select the document to be rejected.Choose Reject and enter the reason for rejection.For example: The amount is not correct, please reverse the document. | The document is rejected. |  |

##### Reverse or Resent a Rejected Document (Requester)

Context

The posted contract accounting document must be checked before final release. The document you submitted is rejected. It can be reversed or sent back for repeated approval. You can choose one of the steps below to complete your workflow item.

###### Reverse a Rejected Document (Requester)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you access Inbox as a requestor and reverse the document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Inbox for Contract Accounting - All Items (F5136). | The My Inbox view displays. |  |
| 3 | Reverse the Document | Select the document entry to be reversed.Choose Open Task.In the Document view, choose Reverse.Reversal Date: <Today’s date>Document Type: General DocumentReverse Method: Clear Business Partner ItemsReconciliation Key: <generated by system automatically>Choose Reverse. | The rejected document is reversed. |  |

###### Resend a Rejected Document (Requester)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you access the Inbox as a requester, make a note, and send it back to the approver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Accounts Payable and Receivable Accountant (FI-CA). | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Inbox for FI-CA (F5136). | The My Inbox view displays. |  |
| 3 | Repeat Approval | Select the document entry to be resent.Choose Repeat Approval.In the Submit Decision view:Decision Note: <your reason for repeat approval>Choose Submit. | The document is submitted for approval.Note Once repeat approval is submitted, approval cycle will restart. |  |

#### Flexible Workflow for Document Changes

Context

Flexible Workflow for Document Changes in Contract Accounting enables the approval processing of changing documents. If changes in document meets conditions set in the Manage Workflows for Contract Accounting (F5135) app, it is automatically blocked and routed to approver for action (release/rejection).

During the workflow:

- Approvers receive workflows in SAP inbox and can release/reject the document changes, at this stage the document changes are not introduced to the document.
- After the approver releases, the documents are unblocked and can go further processing, The changes in the document are released.
- In case of rejection, the work items for the document goes back to the requestor’s Inbox. Requestor should accept the rejection. After that the document can be edited again, but the document changes are not stored in the document.

It is important to know that the document will always be posted no matter a workflow is triggered or not. The only difference is that the document which has a workflow involved is currently ‘blocked’ for certain business process(es) according to the configuration step (103740-Define Check Reasons). In this test case, check reason 02 for document change with below settings will be used in this test script.

| Check Reason | No Payment | No Clearing | No Dunning | No Interest | No Changes |
| --- | --- | --- | --- | --- | --- |
| 02 | X | X | X | X | X |

Prerequisites

Make sure you have completed below steps to activate the Flexible Workflow for Document Change in Contract Accounting.

1. Define Check Reason via configuration step (103740)

It is recommended to create your own check reason for your workflow, if you decide to use standard check reason 02, you could skip this step.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solutionscreen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application: Contract AccountingItem Name: Postings and DocumentsChoose stepDefine Check Reasons and choose Configure.Choose the standard Check Reason 02 and copy it to create your check reason code and adapt the setting according to your business needs. | The Change View "Check Reasons for Dual Control Principle": Overview screen is displayed. |  |

1. Activate Flexible Workflow for changing document:

There are two ways to activate the flexible workflow in Cloud, you can choose either of them to activate your flexible workflow.

-
    1. Via configuration step (103769) - Define Default Check Reason for Workflow

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application: Contract AccountingItem Name: Postings and DocumentsChoose step Define Default Check Reason for Workflow and choose Configure.Choose Create and maintain:Scenario: WS02400078Check Reason: 02Save the entry. | The screen Maintain C003: Overview is displayed.The default check reason is assigned to workflow scenario ID.The workflow for Installment Plan creation is enabled in this client. |  |

-
    1. Implement Cloud BAdI: FI-CA Dual Control Principle: Document Change (FKK_EVENT_5504) and assign the check reason into the BAdI.

If you need more conditions to trigger your workflow and configuration step could not meet your business requirement, you could implement Cloud BAdI: FI-CA Dual Control Principle: Document Change (FKK_EVENT_5504).

|  |
| --- |
| Note There is a certain priority for deriving the check reason. If you have implemented the check reason in the Cloud BAdI 5504, the configuration in the configuration step (103769) - Define Default Check Reason for Workflow can be ignored. |

1. Define responsibility for rules used in workflow steps and assign users to responsibilities:

|  |
| --- |
| Note The approver(s) and requester(s) must be different business users. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access SAP Fiori App | Open Manage Teams and Responsibilities for Contract Accounting (F5134). | The Manage Teams and Responsibilities view displays. |  |
| 3 | Create Team | Choose Create. | The Team view displays. |  |
| 4 | Enter Team Details | Make the following entries:On the General Information tab:Name: for example, Document change approverGlobal ID: for example, Document change approverType: SFICAWF (Contract Accounting Workflow)Description: (Optional)Status: Ready to use |  |  |
| 5 | Enter Team Details | Choose the Team Members tab. |  |  |
| 6 | Enter Team Details | Choose the Create button. | A blank field displays under Business Partner. |  |
| 7 | Enter Team Details | Make the following entries and choose Save:Business Partner: For example, Example Accounts Payable and Receivable ManagerFunction: Function for Approving-Level 1 | The responsibility for the contract document posting workflow is defined. |  |

1. Define and activate your approval workflows:

You can create a new workflow by copying the standard template or create a new entry directly. In this activity, you create the new workflow by copying standard template.

|  |
| --- |
| Note You can have multiple active workflows and could define or sort the order. The system will go through all the active workflows from the first order to the last until the workflow could be started. If the system could determine a workflow which could start a workflow process, the others will be ignored. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. |  |  |
| 2 | Access SAP Fiori App | Open Manage Workflows for Contract Accounting (F5135). | The Manage Workflows view displays. |  |
| 3 | Select | Select Workflow for Document Change. |  |  |
| 4 | Choose | Choose Workflow Template-Document Change. |  |  |
| 5 | Copy Workflow | Choose Copy. | The Copy of Workflow screen displays. |  |
| 6 | Enter Workflow Details | Make the following entries and choose Save:On the Header tab:Name: for example, Document change workflowOn the Properties tab:Description: for example Document change workflowValid from: <Today’s date>Valid to: 12/31/9999On the Start Conditions tab:Only start the workflow if all of the following preconditions are met:For example:Main and subtransaction = Y600/0020Choose Add to add another condition.Total amount should be greater than or equal to 3000 AED.On the Add Alternative Preconditions tab: (Optional)On the Step Sequence tab, choose the first sequence and modify:Step Name: for example: Approve document changeStep Type: Approve document changeOn the Recipients tab:Assignment By: Teams (For example)Team: <Select the team you create in previous step>On the Step Conditions tab: (Optional)On the EXCEPTION HANDLING tab:Name: The document should not be releasedRequired Action: Reject document changeAction result: Cancel workflow | You saved the workflow. |  |
| 5 | Activate Rule | Choose Apply, then choose Save and Activate.Note The template workflow is delivered default as active with no preconditions defined, which means this workflow will always start. Make sure you deactivate the standard template if you don’t want to use it before you start your document change workflows. | The workflow of document change is activated. |  |

##### Change Document

Context

You've completed all the prerequisite steps and set the start conditions with main transaction and subtransaction = Y600/0020 and set total amount as greater than or equal to 3000 AED in step Define and Activate Your Approval Workflows, and now you can change an document to start the workflow. Once the document change meets the start conditions, the work-flow starts, the system automatically set the check reason in document header and a new item is sent to recipient’s Inbox as well as the notification list for actions. The changes in document requires confirmation from approver for further processing (claring,payment ect) according to your check reason settings in configuration step (103740). If the workitem of changes in document is released by approver, the check reason is automatically removed from the document header and the document can go for further processing.

Purpose

In this activity, you change a document with main transaction and subtransaction = Y600/0020 and set total amount as greater than or equal to 3000 AED to trigger the workflow.

To do so, refer to step Change Document.

|  |
| --- |
| Note Once the change document workflow triggered, you could find the message Document Change must be Confirmed with Check Reason Document Change in the document header. |

##### Verify Document

Purpose

In this activity, you can verify a document blocked by document change workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |
| 2 | Access the SAP Fiori App | Open Display Document (FPE3). | The Display Document: Initial Screen is displayed. |
| 3 | Select Document to Display | Make the following entry and choose More > Document Header :Document Number: <Document Number changed in previous step>BP Item: Y01G/L Item: Y01 | The Display Document: Overview screen is displayed. The document details are displayed.In Additional Data tab:The message Document Change must be Confirmed with Check Reason Document Change is displayed. |
| 4 | Select Document to Change | Choose menu More > Document > (Display->Change) . | The message Document cannot be changed until confirmed due to check reason Document Change is displayed.Note You have this message because you've selected No Changes in your check reason. |

##### Approve Changed Document (for Processor- Inbox)

Context

You receive workitem of document changes that need to be checked. After checking the detailed information of the document change, you can either release release or reject with a comment or reason. Once the work item has been selected and released, it disappears from the list. If a document is released or approved, the released/apprvoved documents can go for further processing.

|  |
| --- |
| Note You can set a substitute when you are absent and could not access your Inbox, To do so, go to My Inbox and find the Substitute function from your profile. |

Purpose

In this activity, you access Inbox as a approver and release the document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. |  |  |
| 2 | Access the SAP Fiori App | Open My Inbox for FI-CA (F5136). |  |  |
| 3 | Approve Documents | Select the document to be released.Choose Release. | The document is released.Note All released documents are displayed in the My Outbox - Outbox items app.And the message Confirm Installment Plan with Check Reason Installment Plan approve disappeared. |  |

##### Reject Document Changes (for Processor - Inbox)

Context

You receive a work item of document changes that need to be checked. After checking the detailed information of the document changes, you can either approve or reject with a comment or reason. Once a workitem of document change has been selected and rejected, it disappears from the list and goes back to the requester.

Purpose

In this activity, you access Inbox as a approver and reject the document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. |  |  |
| 2 | Access the SAP Fiori App | Open My Inbox for Contract Accounting - All Items (F5136). | The My Inbox view displays. |  |
| 3 | Reject Installment Plan | Select the changed document item to be rejected.Choose Reject and enter the reason for rejection.For example: The changed information is not correct, please revert the changes. | The document change is rejected. |  |

##### Close the Workflow (Requester)

Context

The document changes must be approved before final release. If the document you submitted is rejected, you can close the workflow item to end the workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Inbox for Contract Accounting - All Items (F5136). | The My Inbox view displays. |  |
| 3 | Reverse the Document | Select the document entry to be closed.Choose CloseNote Then the workflow is ended and check reason is removed from the document header automatically. | The workflow of document change is closed. |  |

#### Flexible Workflow for Document Reverse

Context

Flexible Workflow for Document Reverse in Contract Accounting enables the approval processing of reversing the document. If a reversed document meets conditions set in the Manage Workflows for Contract Accounting (F5135) app, it is automatically blocked and routed to approver for action (release/rejection).

During the workflow:

- Approvers receive workflows in SAP inbox and can release/reject the document reverses. At that stage the document is not reversed and is blocked for editing.
- After the approver releases, the original documents are unblocked and reverse document posted.
- In case of rejection, the Document Reversal Rejection goes back to the requestor’s Inbox. Requestor accepts the workflow item. The document is not reversed but again available for editing.

It is important to know that the document will always be posted no matter a workflow is triggered or not. The only difference is that the document which has a workflow involved is currently ‘blocked’ for certain business process(es) according to the configuration step (103740-Define Check Reasons). In this test case, check reason 04 for Document Reversal with below settings will be used in this test script.

| Check Reason | No Payment | No Clearing | No Dunning | No Interest | No Changes |
| --- | --- | --- | --- | --- | --- |
| 04 | X | X | X | X | X |

Prerequisites

Make sure you have completed the following steps to activate the Flexible Workflow Document Reverse in Contract Accounting.

1. Define Check Reason by configuration step (103740)

It is recommended to create your own check reason for your workflow. If you decide to use standard check reason 04, you could skip this step.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solutionscreen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application: Contract AccountingItem Name: Postings and DocumentsChoose stepDefine Check Reasons and choose Configure.Choose the standard Check Reason 04 and copy it to create your check reason code and adapt the setting according to your business needs. | The Change View "Check Reasons for Dual Control Principle": Overview screen is displayed. |  |

2. Activate flexible workflow for posting document:

There are two ways to activate the flexible workflow in Cloud, you can choose either of them to activate your flexible workflow.

a. Via configuration step (103769) - Define Default Check Reason for Workflow

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solution and choose Configure Your Solution. | The Manage Your Solutionscreen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application: Contract AccountingItem Name: Postings and DocumentsChoose step Define Default Check Reason for Workflow and choose Configure.Choose Create and maintain:Scenario: WS02400079Check Reason: 04Save the entry. | The screen Maintain C003: Overview is displayed.The default check reason is assigned to workflow scenario ID.The workflow for document reverse is enabled in this client. |  |

b. Implement Cloud BAdI: FI-CA Dual Control Principle: Document Reversal (FKK_EVENT_5502) and assign the check reason into the BAdI

If you need more conditions to trigger your workflow and configuration step could not meet your business requirement, you could implement Cloud BAdI: FI-CA Dual Control Principle: Document Reversal (FKK_EVENT_5502).

|  |
| --- |
| Note There is a certain priority for deriving the check reason. If you have implemented the check reason in the Cloud BAdI 5502, the configuration in the configuration step (103769) - Define Default Check Reason for Workflow will be ignored. |

3. Define responsibility for rules used in workflow steps and assign users to responsibilities

|  |
| --- |
| Note The approver(s) and requester(s) must be different business users. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access SAP Fiori App | Open Manage Teams and Responsibilities for Contract Accounting (F5134). | The Manage Teams and Responsibilities view displays. |  |
| 3 | Create Team | Choose Create. | The Team view displays. |  |
| 4 | Enter Team Details | Make the following entries:On the General Information tab:Name: for example, Approver for document ReverseGlobal ID: for example, Approver for document ReverseType: SFICAWF (Contract Accounting Workflow Team)Description: (Optional)Status: Ready to use |  |  |
| 5 | Enter Team Details | Choose the Team Members tab. |  |  |
| 6 | Enter Team Details | Choose the Create button. | A blank field displays below Business Partner. |  |
| 7 | Enter Team Details | Make the following entries and choose Save:Business Partner: For example,Example Accounts Payable and Receivable ManagerFunction: Function for Approving-Level 1 | The responsibility for the Contract Document Reverse workflow is defined |  |

4. Define and activate your approval workflows;

You can create a new workflow by copying the standard template or create a new entry directly. In this activity, you create the new workflow by copying standard template.

|  |
| --- |
| Note You can have multiple active workflows and could define or sort the order. The system will go through all the active workflows from the first order to the last until the workflow could be started. If the system could determine a workflow which could start a workflow process, others will be ignored. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. |  |  |
| 2 | Access SAP Fiori App | Open Manage Workflows for Contract Accounting (F5135). | The Manage Workflows view displays. |  |
| 3 | Select | Select Workflow for Document reversal. |  |  |
| 4 | Choose | Choose Workflow Template-Document reversal. |  |  |
| 5 | Copy Workflow | Choose Copy. | The Copy of Workflow screen displays. |  |
| 6 | Enter Workflow Details | Make the following entries and choose Save:On the Header tab:Name: for example, Document reversal workflowOn the Properties tab:Description: for example Document reversal workflowValid from: <Today’s date>Valid to: 12/31/9999On the Start Conditions tab:Only start the workflow if all of the following preconditions are met:For example:Total amount is greater than or equal to 500 AEDChoose Add to add another condition if needed.On the Add Alternative Preconditions tab: (Optional)On the Step Sequence tab, choose the first sequence and modify:Step Name: for example, Approve reversalStep Type: Approve reversalOn the Recipients tab:Assignment By: Teams (For example)Team: <Select the team you created in previous step>On the Step Conditions tab: (Optional)On the EXCEPTION HANDLING tab:Name: The document should not be releasedRequired Action: Reject reversalAction result: Cancel workflow | You saved the workflow. |  |
| 5 | Activate Rule | Choose Apply, then choose Save and Activate.Note The template workflow is delivered default as active with no preconditions defined, which means this workflow will always start. Make sure you deactivate the standard template if you don’t want to use it before you start your document reversal postings. | The workflow of document reversal is activated. |  |

##### Reverse Document

Context

You completed all the prerequisite steps and set the start conditons with total amount as greater than or equal to 500 AED in step Define and Activate your Approval Workflows, and now you reverse a document to start the workflow. Once the reversed document meets the start conditions, the workflow starts, the system automatically set the check reason in orginal document header and a new item is sent to recipient’s Inbox as well as the notification list for actions. The creation of the reversed document requires confirmation from approver and the original document is blocked for further processing (for example, change) according to your check reason settings in configuration step (103740). If the work item of reverse document is released by approver, the check reason is automatically removed from the original document header and the reversal document is auto-generated .

Purpose

In this activity, you reverse a document which total amount that is greater than or equal to 500 AED to trigger the workflow.

To do so, refer to step Reverse Document.

##### Verify Document

Purpose

In this activity, you can verify a document blocked by installment plan workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |
| 2 | Access the SAP Fiori App | Open Display Document (FPE3). | The Display Document: Initial screen is displayed. |
| 3 | Select Document to Display | Make the following entry and choose More > Go to > Document Header :Document Number: <Document number you try to reverse in previous step>BP Item: Y01G/L Item: Y01 | The Display Document: Overview screen is displayed. The document details are displayed.On the Additional Data tab:The message Reversal Must Be Confirmed with Check Reason Document Reversal displayed. |
| 4 | Select Document to Change | Choose menu More > Document > (Display->Change). | The message Document cannot be changed until confirmed due to check reason Document Reversal displayed.Note You have this message because you've selected No Changes in your check reason. |

##### Approve Document Reversal

Context

You receive work item of document reversal that needs to be checked. After checking the detailed information of the document to be reversed, you can either release or reject it with a comment or reason. Once the work item has been selected and released, it disappears from the list. If a workitem is released or approved, the released/apprvoved document is auto-reversed.

|  |
| --- |
| Note You can set a substitute when you are absent and could not access your Inbox, To do so, go to My Inbox and find the Substitute function from your profile. |

Purpose

In this activity, you access Inbox as a approver and release the document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. |  |  |
| 2 | Access the SAP Fiori App | Open My Inbox for Contract Accounting - All Items (F5136). |  |  |
| 3 | Approve Documents | Select the document to be released.Choose Release.Note You can choose Open Task to check the detailed information of the document to be reversed. | The document is released.Note All released documents are displayed in the My Outbox - Outbox items app.And the message Reversal Must Be Confirmed with Check Reason Document Reversal disappeared in the document header after approver’s release. |  |

##### Reject the Reversal of Document (for Processor - Inbox)

Context

You receive a work item of document reversal that need to be checked. After checking the detailed information of the document, you can either approve or reject with a comment or reason. Once the workitem has been selected and rejected, it disappears from the list and goes back to the requester.

Purpose

In this activity, you access Inbox as a approver and reject the work item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. |  |  |
| 2 | Access the SAP Fiori App | Open My Inbox for Contract Accounting - All Items (F5136). | The My Inbox view displays. |  |
| 3 | Reject Installment Plan | Select the work item to be rejected.Choose Reject and enter the reason for rejection.For example: The amount is not correct. | The reversal of the document is rejected. |  |

##### Close the Workflow (Requester)

Context

The document changes must be approved before final release. If the document you submitted is rejected, you can close the workflow item to end the workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open My Inbox for Contract Accounting - All Items (F5136). | The My Inbox view displays. |  |
| 3 | Reverse the Document | Select the work item entry to be closed.Choose Close.Note Then the workflow is ended and check reason is removed from the document header automatically. | The workflow of document reversal is closed. |  |

### External Cash Desk

Prerequisite

Regarding External Cash Point Services, additional manual configuration is required.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the system with the role SAP_BR_BPC_EXPERT. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Start Customizing | Open Manage Your Solution. | The initial screen of the Manage Your Solution app is displayed. |  |
| 3 | Start Configuration | Choose Configure Your Solution. | A list of Solution is displayed on the screen. |  |
| 4 | Find the External Cash Desk Configuration | Search for External Cash. | The configuration item External Cash Desk is displayed. |  |
| 5 | Start the Configuration | Click on the displayed row to start the configuration. | The External Cash Desk configuration is displayed with a list of configuration steps. |  |
| 6 | Define Cash Desk Structure | Locate Step 2 and choose the Configure button. | The Define Branches overview is displayed. |  |
| 7 | Create a Cash Desk Structure | Choose New Entries.Enter:a 3 character ID for the Branchthe Branch nameselect a Branch Category from the drop-down listClick Save.Select the new entry and double-click the Define Cash Desks node.Choose New Entries.Enter a 2 character ID for the desk and a NameSave the changes. | A new branch and desk are stored. |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Document-change and document-reversal workflow sections contain wording copied from an Installment Plan workflow (e.g. 'workflow for Installment Plan creation is enabled', 'Confirm Installment Plan with Check Reason Installment Plan approve', 'Reject Installment Plan'), which does not match the document-change/reversal scenarios they describe.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Document-posting workflow threshold is stated as 'greater than or equal to = 30000 AED' in the step conditions but as 'Amount > 30000 AED' in the Post Document context.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-sap-s-4hana-cloud-public-edition-contract-accounting-custo-part-02]]
- related-to :: [[09-subscription-billing-and-contract-accounting/contract-accounting-company-initiated-payments-2dp-ae-test-script-813]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BI_S4CLD2608_BPD_EN_AE.docx` — lines 1–2972 of the extracted text · extracted with `mammoth` · 268,419 chars in the whole document
