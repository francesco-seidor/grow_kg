---
id: 08-sales-order-management/test-script-sap-s-4hana-cloud-public-edition-digital-payments-1s2-ae-7
title: "Test Script: SAP S/4HANA Cloud Public Edition - Digital Payments (1S2_AE) (1S2_S4CLD2608_BPD_EN_AE)"
description: "SAP test script (release 2608, AE) for scope item 1S2 Digital Payments: card authorization, payment run, settlement, advice, clearing, refunds."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/digital-payments]
aliases: [1S2_S4CLD2608_BPD_EN_AE]
keywords: [Digital Payments and Card Payments in Sales, digital payments, payment card authorizations, credit card settlement, advice processing, payment run, automatic clearing, payment card data, payment card refunds, authorization cancellation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1S2_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-761
topic: 08-sales-order-management/digital-payments
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP S/4HANA Cloud Public Edition - Digital Payments (1S2_AE) (1S2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1S2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Digital Payments and Card Payments in Sales** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Digital Payments (1S2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847624)

[2 Prerequisites 4](#_Toc232847625)

[2.1 Additional Manual Configuration 4](#_Toc232847626)

[2.2 System Access 4](#_Toc232847627)

[2.3 Roles 4](#_Toc232847628)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232847629)

[2.5 Business Conditions 6](#_Toc232847630)

[2.6 Preliminary Steps 7](#_Toc232847631)

[2.6.1 Manage Payment Card Data 7](#_Toc232847632)

[2.6.2 Create Invoices Manually 8](#_Toc232847633)

[2.6.3 Bank Relationship Contract Types 10](#_Toc232847634)

[2.6.4 Create Bank and Bank Account 11](#_Toc232847635)

[3 Overview Table 12](#_Toc232847636)

[4 Test Procedures 13](#_Toc232847637)

[4.1 Digital Payments 13](#_Toc232847638)

[4.1.1 Schedule Accounts Receivable Jobs - Payment Card Authorizations 13](#_Toc232847639)

[4.1.2 Payment Run 15](#_Toc232847640)

[4.1.2.1 Schedule Payment Proposals 15](#_Toc232847641)

[4.1.2.2 Release Payment Proposal 17](#_Toc232847642)

[4.1.3 Schedule Accounts Receivable Jobs - Credit Card Settlement 18](#_Toc232847643)

[4.1.4 Schedule Accounts Receivable Jobs - SAP Digital Payments: Advice Processing 20](#_Toc232847644)

[4.1.5 Schedule General Ledger Jobs - Automatic Clearing 21](#_Toc232847645)

[4.1.6 Display Payment Card Data 22](#_Toc232847646)

[4.1.7 Create Refunds for Digital Payments (Optional) 23](#_Toc232847647)

[4.1.8 Cancel Payment Card Authorizations (Optional) 24](#_Toc232847648)

[5 Appendix 26](#_Toc232847649)

[5.1 Succeeding Processes 26](#_Toc232847650)

## Purpose

Overview

SAP digital payments is a payment hub between payment service providers and SAP components, solutions, or applications that process incoming credit card payments.

The scope item enables the integration between SAP S/4HANA Cloud Public Edition and SAP digital payments, allowing you to use credit card payment methods in SAP S/4HANA Cloud Public Edition for incoming payments.

The complete process — from settlement using secure tokens via payment service provider advice to final bank statement — is covered and automated.

Various payment service providers are supported.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/1S2_S4CLD2602_BPD_EN_AE.docx) ). |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/cd93e472e990f680c155022fc586c7d6)

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
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

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
| G/L Accounts | 1253000011008070 |  |  |
| House Bank | AEDP1 |  |  |
| House Bank Account | AEDPA |  |  |
| Payment Method | N (Credit Card Payments) |  |  |
| Bank | Use a Digital Payments bank |  | If you create your own bank, the bank type must be Payment Service Provider. |
| Bank Account | Use a digital payment account |  | If you create your own bank account, the account type must be PSP Account Type. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNG | Create G/L Account and Cost Element - MDS |

### Business Conditions

Before this test script can be tested, the following business conditions must be met.

| Business Condition | Comment |
| --- | --- |
| Sell from Stock (BD9) | A customer invoice must be available for the test procedures. When there are no existing open customer items, you must create a billing document. Follow the procedures in either of these test scripts to create a customer invoice.When creating a customer invoice, note the amount and Reference Document Number (XBLNR in the header). The information is required when simulating a manual bank statement. In the bank statement, a credit item can be reconciled with the customer invoice. |
| Accounts Receivable (J59) | Perform the Enter Invoice without Sales Order procedure and the Invoice Collection Preparation procedure in the test script to create outgoing invoices, import manually, and display invoices. |

### Preliminary Steps

#### Manage Payment Card Data

Purpose

In this activity, you update the business partner master data for the customer to add payment card information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Customer Master Data (F0850A). | The Manage Customer Master view is displayed. |  |
| 3 | Enter Business Partner | Make the following entries and choose Go:Business Partner: 33100010 | The customer/business partner is displayed in the Customers pane. |  |
| 4 | Details | Choose the Details (>) button for the customer. |  |  |
| 5 | Edit | Choose Edit. |  |  |
| 6 | Payment Cards | Choose the Payment Cards tab. |  |  |
| 7 | Register Payment Card | In the Payment Cards pane, choose Create. | The Register New Payment Card dialog box is displayed. |  |
| 8 | Register Payment Card | Make the following entry and choose Register:Card ID: <unique card identification description (six-character limit)> | The system displays a new Payment Page window or tab. |  |
| 9 | Register Payment Card | Make the following entries and choose Submit:Credit Card Type: <type of card>Card Number: <credit card number>Name On Card: <name on credit card>Valid To: <month and year of validity>CVC: <card validation code> | The system displays a message Your payment card was successfully registered.Note Once the message is displayed, you can choose Close.The new payment card is listed in the Payment Cards pane. |  |
| 10 | Save | Choose Save. | The customer master data record is updated with the payment card. |  |

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

#### Bank Relationship Contract Types

Purpose

In this activity, you define the bank relationship contract types.

|  |
| --- |
| Note This preliminary step is only for productive systems, not internal, demo, or starter systems. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Cash and Liquidity Management

1. For the row with Item Name of General Settings, choose Details (>).
2. For the Define Basic Settings row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Basic Settings.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Details | Make the following entries and choose Save:Cash Scope: Full ScopeBank Relationship Management section:Enable Bank Account Contract Types: Selected |  |  |

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
| Test Procedures > Bank Account Master Data Processing with Basic Bank Account Management > Using Direct Revision Activate → Create Bank Account > Create Bank Account | Manage Bank Accounts (F1366A) | Choose Create. Enter your company code and Account Type: 20 (PSP Account Type) and choose Continue.Account Description: <account description>Use the Bank Key value above.Use a valid value for Account Number.Under House Bank Connectivity, choose Create.House Bank Account: <use your own house bank account>G/L Account: <G/L account>Under the Bank Relationship tab, make the following entry:Pmnt Tran Type Group: CAMT053 |  |

## Overview Table

The Digital Payments (1S2) test script consists of several process steps and reports provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Schedule Accounts Receivable Jobs - Payment Card Authorizations](#unique_13) [page ] 13 | Accounts Receivable Accountant | Schedule Accounts Receivable Jobs (F2366) | You scheduled jobs for payment card authorizations. |
| [Schedule Payment Proposals](#unique_14) [page ] 15 | Accounts Receivable Accountant | Manage Automatic Payments (F0770) | You schedule payment proposals. |
| [Release Payment Proposal](#unique_15) [page ] 17 | Accounts Receivable Accountant | Manage Automatic Payments (F0770) | You released the payment proposals. |
| [Schedule Accounts Receivable Jobs - Credit Card Settlement](#unique_16) [page ] 18 | Accounts Receivable Accountant | Schedule Accounts Receivable Jobs (F2366) | You scheduled jobs for credit card settlement. |
| [Schedule Accounts Receivable Jobs - SAP Digital Payments: Advice Processing](#unique_17) [page ] 20 | Accounts Receivable Accountant | Schedule Accounts Receivable Jobs (F2366) | You scheduled jobs for advice processing. |
| [Schedule General Ledger Jobs - Automatic Clearing](#unique_18) [page ] 21 | General Ledger Accountant | Schedule General Ledger Accounting Jobs (F1927) | You scheduled jobs for automatic clearing. |
| [Display Payment Card Data](#unique_19) [page ] 22 | Accounts Receivable Accountant | Display Payment Card Data (F2935) | You displayed payment card data. |
| [Create Refunds for Digital Payments (Optional)](#unique_20) [page ] 23 | Accounts Receivable Accountant | Create Refunds for Digital Payments (F7326) | You created refunds for digital payments. |
| [Cancel Payment Card Authorizations (Optional)](#unique_21) [page ] 24 | Accounts Receivable Accountant | Cancel Payment Card Authorization - in Open Items (FCC_DP_AUTH_CANCEL) | You canceled the payment card authorization for an open item. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Digital Payments

#### Schedule Accounts Receivable Jobs - Payment Card Authorizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you make ad hoc payment card authorizations.

Prerequisites

In the procedure below, if you are running a job for normal items, open invoices must exist.

In the procedure below, if you are running a job for down payment requests, down payments must exist.

A credit card must be assigned to the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access App | Open Schedule Accounts Receivable Jobs (F2366). |  |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Job Template | Make the following entries and choose Step 2:Job Template: Payment Card Authorizations for Customer Line ItemsJob Name: Payment Card Authorizations for Customer Line ItemsNote Depending on the card type, you have two options for the Job Template/Job Name fields:Payment Card Authorizations for Customer Line Items with Collection AdministrationPayment Card Authorizations for Customer Line Items with Standard Card |  |  |
| 5 | Start Immediately | Select Start Immediately and choose Step 3. |  |  |
| 6 | Customer Details | Make the following entries and choose Schedule:Company Code: 3310Customer: 33100010Select one of the following (depending on your needs):Select Normal ItemsSelect Down Payment Requests | The Application Log view is displayed. The job you scheduled displays Finished status. |  |
| 7 | View Log | In the Log column for the job, choose the Log button. | The log is displayed. |  |
| 8 | Review Log | Review the log. When done, choose Back. |  |  |
| 9 | Copy Job | Select the job and choose Copy. |  |  |
| 10 | Job Template | Keep the current values. Choose Step 2. |  |  |
| 11 | Start Immediately | Keep the current values. Choose Step 3. |  |  |
| 12 | Customer Details | Select Update Run and choose Schedule. |  |  |
| 13 | View Log | For the copied job, choose the Log button in the Log column. |  |  |
| 14 | Review Log | Review the log. | Authorizations for line items are displayed, as are messages stating that line items are updated with those authorizations. |  |
| 15 | Back | When done, choose Back. |  |  |

#### Payment Run

Use

This section describes how to post payment using the automatic payment program.

Invoices and down payment requests are posted and are open for payment.

Prerequisites

The [Schedule Accounts Receivable Jobs - Payment Card Authorizations](#unique_13) [page ] 13 step has been executed.

##### Schedule Payment Proposals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you select the invoices to be paid.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Automatic Payments (F0770). |  |  |
| 3 | Create | Choose + (Add). | The New Parameter dialog box displays. |  |
| 4 | Data Entry | Make the following entries:Run Date: <Today's date>Identification: Any five character description, for example, <SPAY1>and choose Create. | An entry input view displays. |  |
| 5 | Data Entry | Make the following entries:Basic section:Posting Date: <Today's date>Docs Entered Up To: <Today's date>Customer Items Due By: For example, <Today's date + 10 >Additional Log: YESPayment Controls section:Company Code: 3310Next Payment Date: <Today's date + 5 days>Payment Method: For example, NOpen Item Selection section:Customer: 33100010 |  |  |
| 6 | Save the Parameters | At the top of the view, choose Save. | The system displays the Parameter has been saved notification. The status changes to Parameter Created. |  |
| 7 | Schedule Proposal | Choose Schedule > Proposal. | The Schedule Proposal dialog box displays. |  |
| 8 | Data Entry | Make the following entries:Start Date: <Today's date>Start immediately: Selectedand choose Schedule. | The Manage Automatic Payments view displays. |  |
| 9 | View the Proposal | Choose the Proposal Processed tab. | The proposal displays in the Items list with a Proposal Created status. |  |

##### Release Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release the payment proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Automatic Payments (F0770). |  |  |
| 3 | Go | Choose the Go button. | A list of all payment runs is displayed |  |
| 4 | Proposal Processing | Choose the Proposal Processed tab. |  |  |
| 5 | Select Proposal | Select the line of the previously created proposal (for example, SPAY1) and choose Schedule. | The Schedule Payment view is displayed. |  |
| 6 | Schedule Payment | Make the following entries and choose Schedule:Start Date: Today's dateStart immediately: Select | The system displays the message Payment has been scheduled. The status changes to Payment Posted. The log shows how many postings were generated. |  |
| 7 | View the payment | Choose the Payment Processed tab. | The status changes to Payment posted. |  |
| 8 | View Log postings | Select the line of your payment run and in the Log column, choose Notes.Note If the Log column does not show, choose the gear (Settings) icon. Select the Log field and choose OK to add the column to the view. | The log shows how many postings were generated. |  |
| 9 | Close Log Details | Choose OK. | The Log Details dialog box closes. |  |
| 10 | Payments and Exceptions | In the Open column of your payment run, choose > (Open).Note If the Open column does not show, choose the gear (Settings) icon. Select the Open field and choose OK to add the column to the view. | The view displays a summary of payments and exceptions for the payment run. |  |
| 11 | Navigation | You sort the information by payment method, country, business area, and so on. Make your selection to filter the results in the Summary table. | Amounts are sorted by your selection. |  |
| 12 | Payments | Choose Payments or Exceptions. | Details are displayed for payments or exceptions generated (such as payment document, included items, and so on). |  |
| 13 | Payments Navigation | In the Open column, choose > (Open) to display line item details of the payment.When you are done, choose Back at the top, to exit this view. | Payment item details are displayed. |  |

#### Schedule Accounts Receivable Jobs - Credit Card Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule accounts receivable jobs for credit card settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori app | Open Schedule Accounts Receivable Jobs (F2366). |  |  |
| 3 | Create a New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Job Data | In the New Jobs view, make the following entries:General Information section:Job Template: Payment Card SettlementScheduling Option section:Start Immediately: SelectedParameter Section:Company Code: 3310G/L Accounts: 12530000Data for Clearing Entry section:Journal Entry Type: SAJournal Entry Date: <current date>Posting Date: <current date>Processing Parameters section:Update Run: selectedAnd choose Schedule from the lower right of the view. | Your job is created and starts immediately. |  |
| 5 | Review Job Status | Once jobs complete, the Application Jobs (F4519) view displays. Review the job log.Note Job log only displays when there is a credit card settlement. |  |  |

#### Schedule Accounts Receivable Jobs - SAP Digital Payments: Advice Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule accounts receivable jobs for SAP Digital Payments, Advice Processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Accounts Receivable Jobs (F2366). |  |  |
| 3 | Create a New Job | Choose the Create button. | The New Job view displays. |  |
| 4 | Enter Job Data | In the New Jobs view, make the following entries:General Information section:Job Template: SAP Digital Payments: Advice ProcessingScheduling Options section:Start Immediately: selectedParameters Section:Bank Key: 88800011Bank Country: for example AETransactions from: for example, current date - 2Transactions to: for example, current date -1Digital Payment Type: CCPayment Service Provider Selections sectionPayment Service Provider: For example, DPSTMerchant Alias: Use the value help to enter or select the appropriate merchant alias valueReconciliation: unselectedNote Reconciliation means that the Advice data is only returned once. If you create another run for the same time frame and no additional data was provided by the payment service providers, no advice data is returned. In a situation where data is necessary for SAP S/4HANA (for example, when postings of the advice were wrong and have been reversed), then the reconciliation flag is set so all advice data for the date / payment service provider / merchant selection is returned.And choose Schedule from the lower right of the view. | The job is created and starts immediately. |  |
| 5 | Review Job Status | After the job completes, the Application Job view displays. Review the job log.Note The job log only displays when there is an incoming advice. |  |  |

#### Schedule General Ledger Jobs - Automatic Clearing

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
| 4 | Enter Job Data | Make the following entries and choose Schedule:General Information sectionJob Template: Automatic ClearingScheduling Options section:Start Immediately: selectedParameters section:General SelectionsSelect G/L Accounts: selectedG/L Account: 11008070Company Code: 3310Clearing date: <current date> | The job is created and started immediately. After the job completes, the Application Jobs view displays. |  |
| 5 | Review Job Status | Review the job log.Note The job log displays only when there are documents available for automatic clearing. |  |  |

#### Display Payment Card Data

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Receivable Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Payment Card Data (F2935). | The Display Payment Card Data (F2935) view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Authorization Date: Choose the field help, and from the Time Period dialog box, select Date Range. Enter a range from today's date through to 10 days after today's dateCustomer: For example, 33100010Company Code: For example, 3310 | The list of Card Payments displays. |  |
| 4 | Drilldown Display | Choose a row of a journal entry to display detailed payment card data. You can drilldown into the data in the entry details view. | The detailed payment card data for the selected row is displayed on the right side of the view.Note If there is no settlement for the payment, the Settlement section and Settlement Run section will not be displayed. |  |

#### Create Refunds for Digital Payments (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a refund of a payment card payment initiated from the [Schedule Accounts Receivable Jobs - Payment Card Authorizations](#unique_13) [page ] 13 step and charged from the customer the [Schedule Accounts Receivable Jobs - Credit Card Settlement](#unique_16) [page ] 18 step. The refund amount is credited to the customer account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Refunds for Digital Payments (F7326). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Company Code: <company code>, for example, 3310Customer: <customer>, for example, 33100010Payment Document Number: <document number from the Payment Run topic> | A payment is displayed. |  |
| 4 | Select Payment | For the entry, choose > (Details) at the right end of the row. | The detailed payment view is displayed. |  |
| 5 | Create Refund | Choose Create Refund. | A dialog box is displayed. |  |
| 6 | Refund | Make the following entry and choose Create:Refund Amount: <amount that is lower or equal to the original payment amount>Document Type: AB | The updated detailed payment is displayed with a new refund in the document flow in pending status. |  |
| 7 | Settle Refund | You must settle the refund. To do this, perform the [Schedule Accounts Receivable Jobs - Credit Card Settlement](#unique_16) [page ] 18procedure in this test script, then return to the next step in this procedure. | The refund is settled.Note If you want to validate the refund, run steps 2 to 4 in this procedure. |  |

#### Cancel Payment Card Authorizations (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you cancel a credit card authorization for customer line items. The open line item has a payment card authorization that must not be charged.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Cancel Payment Card Authorization - in Open Items (FCC_DP_AUTH_CANCEL). | The Cancel Payment Card Authorization in Open Items view is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Company Code: <company code>, for example, 3310Document Number: <document number of authorized open item>Fiscal Year: <fiscal year for the open item>Payment Card Item: 1 | The Display Logs view is displayed. The payment card authorization is canceled. The system shows messages stating that the payment card authorization is removed, that the authorization is canceled and that the payment card authorization is successfully canceled at PSP.Note If you execute a cancelation for a document that is already canceled, the system displays the message No line items found for this selection. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Basic Cash Operations (BFB) | Follow the procedures for Bank Statements, including the sub-steps, to upload incoming bank statements. |
| Accounting and Financial Close(J58) | Follow the procedures for the Clear G/L Accounts - Manual Clearing app |

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
- related-to :: [[08-sales-order-management/external-digital-payments-2lz-ae-test-script-833]]
- related-to :: [[08-sales-order-management/test-script-digital-payments-foundation-53v-1062]]
- related-to :: [[08-sales-order-management/test-script-digital-payments-sales-1z1-ae-sap-s-4hana-cloud-public-edi]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1S2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 41,134 chars in the whole document
