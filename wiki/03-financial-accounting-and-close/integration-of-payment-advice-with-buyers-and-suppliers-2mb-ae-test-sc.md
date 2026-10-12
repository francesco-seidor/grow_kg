---
id: 03-financial-accounting-and-close/integration-of-payment-advice-with-buyers-and-suppliers-2mb-ae-test-sc
title: Integration of Payment Advice with Buyers and Suppliers (2MB_AE) - Test Script (2MB_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2MB_AE: payment runs, SOAP payment advice and cancellation exchange between buyer and supplier systems."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/payment-advice-exchange]
aliases: [2MB_S4CLD2608_BPD_EN_AE]
keywords: [Payment Advice Exchange with Buyers and Suppliers, payment advice, payment proposals, payment cancellation, edi integration, supplier invoices, automatic payments, aif message monitoring, cleared documents, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2MB_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-834
topic: 03-financial-accounting-and-close/payment-advice-exchange
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Integration of Payment Advice with Buyers and Suppliers (2MB_AE) - Test Script (2MB_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2MB_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Payment Advice Exchange with Buyers and Suppliers** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Integration of Payment Advice with Buyers and Suppliers (2MB_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232849501)

[2 Prerequisites 3](#_Toc232849502)

[2.1 Additional Manual Configuration 3](#_Toc232849503)

[2.2 System Access 3](#_Toc232849504)

[2.3 Roles 3](#_Toc232849505)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232849506)

[2.5 Business Conditions 5](#_Toc232849507)

[3 Overview Table 6](#_Toc232849508)

[4 Test Procedures 7](#_Toc232849509)

[4.1 Invoice Entry Without Purchase Order (Optional) 7](#_Toc232849510)

[4.2 Pay Single Invoice 8](#_Toc232849511)

[4.2.1 Schedule Payment Proposals 9](#_Toc232849512)

[4.2.2 Revise Payment Proposal 11](#_Toc232849513)

[4.2.3 Release Payment Proposal 12](#_Toc232849514)

[4.3 Receive Payment Advice 13](#_Toc232849515)

[4.4 Cancel Payment 14](#_Toc232849516)

[4.4.1 Send Payment Advice Cancellation 15](#_Toc232849517)

[4.5 Delete Payment Advice 16](#_Toc232849518)

[4.6 Display Cleared Document 16](#_Toc232849519)

[4.7 Check Messages in AIF (Optional) 17](#_Toc232849520)

## Purpose

Overview

For organizations whose suppliers or buyers use traditional data exchange protocols like electronic data interchange (EDI), this scope item provides robust application programming interfaces (APIs) to simplify and automate exchanging procurement documents.

The following documents are supported via the Simple Object Access Protocol (SOAP) messaging protocol:

- Payment Advice Notification (Trigger Outbound message)

- Payment Advice Notification (Receive Inbound message)

- Payment Advice Cancellation Notification (Trigger Outbound message)

- Payment Advice Cancellation Notification (Receive Inbound message)

You can benefit from intercompany integration by enabling this scope item.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/4f46877a2d6db2bbe4a897fa0d7df3ac)

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
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Configuration Expert - Business Network Integration | SAP_BR_CONF_EXPERT_BUS_NET_INT |  |  |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Accounting

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Supplier | 33300084 (where the two digits in the beginning are the first two digits of your company code) |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |

### Business Conditions

The following business condition must be met before proceeding with this test script:

| Scope Item | Business Condition |
| --- | --- |
| J60 – Accounts Payable | Update BP master data with the payment method T.Review and execute the Invoice Payment Preparation section. |

## Overview Table

This scope item consists of several process steps provided in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Invoice Entry Without Purchase Order (Optional)](#unique_9) [page ] 7 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | Invoice is entered without a purchase order (PO). |
| [Pay Single Invoice](#unique_10) [page ] 8 | Accounts Payable Accountant |  |  |
| [Schedule Payment Proposals](#unique_11) [page ] 9 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | Payment Proposal is created. |
| [Revise Payment Proposal](#unique_12) [page ] 11 | Accounts Payable Accountant | Revise Payment Proposals (F0771) | Payment Proposal is revised. |
| [Release Payment Proposal](#unique_13) [page ] 12 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | Payment Proposal is released and Payment Advice is created. |
| [Receive Payment Advice](#unique_14) [page ] 13 | Accounts Receivable Accountant |  | Payment advice is received in the Receiver system |
| [Cancel Payment](#unique_15) [page ] 14 | Accounts Payable Accountant | Reset Cleared Items (F2223) | Payment Advice cancellation (Cleared Document) has been created. |
| [Send Payment Advice Cancellation](#unique_16) [page ] 15 | Accounts Payable Accountant |  | Cancellation is sent out. |
| [Delete Payment Advice](#unique_17) [page ] 16 | Accounts Payable Accountant |  |  |
| [Display Cleared Document](#unique_18) [page ] 16 | General Ledger Accountant | Manage Journal Entries (F0717A) | Cleared Document/Payment Advice Cancellation can be seen and sent again. |
| [Check Messages in AIF (Optional)](#unique_19) [page ] 17 | Configuration Expert - Business Network Integration | Message Dashboard (/AIFX/WDA_MSG_MONITOR) | Messages can be seen by Administrator. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Invoice Entry Without Purchase Order (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter a supplier invoice without reference to a purchase order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant.Don't use the generic Accounts Payable Accountant user. Create a personalized user based on the business role ID. |  |  |
| 2 | Access App | Open Create Supplier Invoice (F0859). |  |  |
| 3 | Dialog Box | If the Data from Previous Invoice Entry Exist dialog box appears, choose No. |  |  |
| 4 | General Data | In the General Information section, enter the following data:Transaction: InvoiceCompany Code: 3310Gross Invoice Amount: , for example<11,900>Invoice Date: <<Today's date>Posting Date: <Today's date>Reference: <Enter the NF number>Use - (dash) to enter NF Series, if applicable (for example, 12345-001).Invoicing Party: 33300084Use the invoicing party/supplier provided to you by your administrator. |  |  |
| 5 | G/L Account Items | In the G/L Account Items section, make the following entries:Debit/Credit: DebitG/L Account: 61061000Amount: <100>, for example |  |  |
| 6 | More Details: Account Assignment | Choose > next to the Debit/Credit field.Make the following entries:Cost Center: 33101201 |  |  |
| 7 | Payment | Payment Terms: NT30/NT45/ |  |  |
| 8 | Post | Choose Post. | A dialog box is displayed showing the invoice number posted. Make a note of the MM invoice number.If you need the FI invoice number, use the Display Supplier Invoice Advanced app. Open the invoice. Choose the Follow-on Documents button to get the FI invoice number. |  |
| 9 | Exit | Choose OK and then choose Back to exit. |  |  |

### Pay Single Invoice

Purpose

This section describes how to post payment using the automatic payment program.

Prerequisites

- Invoices have been posted and are open for payment.
- Payment methods to use have been defined in Business Partner Master Data. (See the chapter Complete Supplier Master Data in Accounts Payable.

#### Schedule Payment Proposals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Prerequisites

An open invoice must be available. For more information, see [Business Conditions](#unique_7) [page ] 5.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. |  |  |
| 2 | Access App | Open Manage Automatic Payments (F0770). |  |  |
| 3 | Create Screen | Choose Add. | The New Parameter screen is displayed. |  |
| 4 | Data Entry | Enter the following details and choose Add:Run Date: <Today's date>Identification: <Any five character description, such as SPAY1> | An entry input screen is displayed. |  |
| 5 | Data Entry | Enter the following details:Posting Date: <Today's date>Docs Entered Up To: <Today's date>Next Payment Date: <Today's date + 6 months>Company Code: 3310Payment Method: <T or F>For invoices in EUR, use F.Supplier: 33300084Enable Additional Log (CE only).In the Additional Log section (OP only), enter as required.Required supplier: 33300084Note For the Payment Method field, verify that the payment method is valid in the supplier master record. |  |  |
| 6 | Single Invoice (Optional) | If you want to execute a payment for a single invoice, make the following entries in the Free Selection section:Accounting Document Number (BKPF-BELNR): <Document Number> |  |  |
| 7 | Save the Parameters | Choose Save. | The system displays a success message. The status changes to Parameter Created. |  |
| 8 | Schedule Proposal | Choose the Schedule button. Choose Proposal. | The Schedule Proposal screen is displayed. |  |
| 9 | Data Entry | Enter the following in the Schedule Proposal pane and choose Schedule:Start Date: <Today's date>Select the Start Immediately checkbox. | The system displays a message mentioning that a proposal is created.The status changes to Proposal Created. |  |
| 10 | View the Proposal | Choose the Proposal Processed tab. |  |  |
| 11 | Display Program Selection | Choose Go. | The program's selection is displayed in the log. |  |
| 12 | View Log for Outgoing Payment | Select the row of your payment run ID (Identification column), and in the Log column, choose Notes.Note If the Log column is not displayed, choose the Settings button. Select the Log field and choose OK. | The log displays the program's selection. The SAP system is updated with information about the outgoing payment. |  |

#### Revise Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the invoices to be paid.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. |  |  |
| 2 | Access App | Open Revise Payment Proposals (F0771). |  |  |
| 3 | Go | Choose Go. | A list of all proposals is displayed. |  |
| 4 | Select | Choose the > button in the Open column in the proposal you want to edit (for example SPAY1). | The Schedule Payment Proposal screen of the selected Identification is displayed. |  |
| 5 | Edit Payment | In the Payments tab, select the row and choose Edit Payment. |  |  |
| 6 | Enter Details | You can change the details according your needs. |  |  |
| 7 | Exceptions | If some payments are blocked, you can find them on the Exceptions tab. You may unblock or reallocate and pay them by using the buttons in the screen. |  |  |

#### Release Payment Proposal

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant. |  |  |
| 2 | Access App | Open Manage Automatic Payments (F0770). |  |  |
| 3 | Go | Choose Go. | A list of all payment runs is displayed |  |
| 4 | Proposal Processing | Choose the Proposal Processed tab. |  |  |
| 5 | Select Proposal | Select the line of the previously created proposal (for example SPAY1) and choose Schedule. | The Schedule Payment screen is displayed. |  |
| 6 | Schedule Payment | Enter the following details and choose Schedule:Start Date: <Today's date>Select the Start Immediately checkbox. | The system displays a message mentioning that payment has been scheduled. The status changes to Payment Posted. The log shows how many postings were generated. |  |
| 7 | View the Payment | Choose the Payment Processed tab. | The status changes to Payment posted. |  |
| 8 | View Log Postings | Select the line of your payment run Identification and in the Log column, choose Notes.If the Log column is not displayed, choose the Settings button. Select the Log field and choose OK. | The log shows how many postings were generated. |  |
| 9 | Close Dialog | Choose OK. | The Log Details dialog box is closed. |  |
| 10 | Payments and Exceptions | In the Open column, choose the right arrow (navigation). | The screen displays a summary of payments and exceptions for the payment run. |  |
| 11 | Navigation | You can sort the information by payment method, country, and so on. Select the view to display in the field below Summary. | Amounts are sorted by your selection. |  |
| 12 | Payments | Choose Payments or Exceptions. | Details are displayed for the payments or exceptions generated (such as payment document, included items, and so on).If you have to cancel the payment, note down Payment Document No. and use this as a clearing document number. |  |
| 13 | Payments Navigation | In the Open column, choose the right arrow (navigation) to display the line item details of payment. | Payment item details are displayed. |  |
| 14 | Output Items | Choose Output Items. |  |  |
| 15 | Review | In the Output Items section, check that status of Output Type PAYM_ADV_EDI . Choose the item and then choose Show Application Log. | Application Log shows all the processing details of the message. |  |
| 16 | Close | Close the application. |  |  |

### Receive Payment Advice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can see the payment advice in Receiver system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Receivable Accountant.Do not use the generic Accounts Receivable Accountant user. Create a personalized user based on the business role ID. |  |  |
| 2 | Access App | Open Manage Payment Advices - Deprecated (F2550). |  |  |
| 3 | Enter Details | Company Code: 1710Created On: <Payment posting date>Choose Go. | A list of entries with Payment Advices is displayed. |  |
| 4 | View Results | Choose the Payment Advice number that you have noted in the previous step. | Payment Advice is displayed with all the details. |  |
| 6 | Exit | Choose Exit. | Home page is displayed. |  |

### Cancel Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you cancel the already created payment advice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant.Do not use the generic Accounts Payable Accountant user. Create a personalized user based on the business role ID. |  |  |
| 2 | Access App | Open Reset Cleared Items (F2223). |  |  |
| 3 | Enter Details | Enter the following details:Clearing Entry: <Enter the Clearing Document Number got from the Release Payment Proposal step>Company Code: 3310Fiscal Year: 2017, for example |  |  |
| 4 | Reset Cleared Items | Choose the > icon on the right side of the entry. Choose Reset or Reset and Reverse as required. | The details screen is displayed. Enter the reason for reversal. |  |
| 5 | Enter Details | Enter Reversal Reason and choose Continue | A message is displayed mentioning that clearing has been reset.A message is displayed mentioning that the respective document has been posted in company code 3310. |  |
| 6 | Exit | Choose Exit. | Home page is displayed. |  |

#### Send Payment Advice Cancellation

Purpose

Payment Cancellation is automatically sent to the other system.

Prerequisites

Payment advice must be already available and canceled by the user.

Procedure

This step is automatically generated.

### Delete Payment Advice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can recheck whether the previously created payment advice in the Receiver system is deleted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Receivable Accountant.Do not use the generic Accounts Receivable Accountant user. Create a personalized user based on the business role ID. |  |  |
| 2 | Access App | Open Manage Payment Advices - Deprecated (F2550). |  |  |
| 3 | Enter Details | Enter the required details:Company Code: 3310Created On: <Payment posting date>Choose Go. | The previously created Payment Advices should not exist. The entries should not appear. |  |
| 4 | Exit | Choose Exit. | Home page is displayed. |  |

### Display Cleared Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the canceled payment advice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Accountant.Do not use the generic Accounts Payable Accountant user. Create a personalized user based on the business role ID. |  |  |
| 2 | Access App | Open Manage Journal Entries (F0717A). |  |  |
| 3 | Enter Details | Journal Entry:<XXXXXXXXXX> (enter the journal entry of the payment created in the Pay Single Invoice chapter) |  |  |
| 4 | Go | Choose Go | Journal entry is displayed |  |
| 5 | Manage Journal Entry | Choose the document displayed under Journal Entry and choose Manage Journal Entry. | The details of the journal entry are displayed. |  |
| 6 | Choose Line Items | Choose Posting View Item. | Output details are displayed informing whether PAYM_ADV_CANCELLATION is successfully sent or not. |  |
| 7 | Show Application Log | Choose the entry and then choose Show Application Log. | Application log displays all the processing details of the message. |  |

### Check Messages in AIF (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In message monitoring, you can check the messages related to Payment Advice and Payment Advice Cancellation.

Prerequisites

Using the Assign Recipients application, the Administrator user must be assigned to the /FIEDI namespace and the corresponding Recipient for Alert.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP S/4HANA system as Configuration Expert - Business Network Integration. | The Home page is displayed. |  |
| 2 | Display Messages | Choose Message Dashboard (/AIFX/WDA_MSG_MONITOR). | All the messages related to Payment advice and Payment Advice Cancellation are displayed. |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Receive Payment Advice step uses company code 1710 for the receiver system, while other steps use company code 3310; the Delete Payment Advice step checks company code 3310 for receiver entries.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[03-financial-accounting-and-close/test-script-accounts-payable-j60-ae-sap-s-4hana-cloud-public-edition-2]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2MB_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 28,171 chars in the whole document
