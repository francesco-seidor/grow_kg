---
id: 16-two-tier-erp-and-central-finance/test-script-subsidiary-integration-of-sap-s-4hana-cloud-to-central-fin
title: "Test Script: Subsidiary Integration of SAP S/4HANA Cloud to Central Finance (1W4) (1W4_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1W4: replicating supplier invoices, payments and outgoing invoices to Central Finance (CFIN)."
cluster: 16-two-tier-erp-and-central-finance
tags: [kb/two-tier-erp-and-central-finance, topic/central-finance-replication]
aliases: [1W4_S4CLD2608_BPD_EN_XX]
keywords: [Central Finance Replication from Subsidiaries, central finance integration, financial data replication, supplier invoices, payment run, outgoing invoices, incoming payments, test scripts, business roles, master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1W4_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-766
topic: 16-two-tier-erp-and-central-finance/central-finance-replication
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Subsidiary Integration of SAP S/4HANA Cloud to Central Finance (1W4) (1W4_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1W4_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Central Finance Replication from Subsidiaries** in Two-Tier ERP and Central Finance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Subsidiary Integration of SAP S/4HANA Cloud to Central Finance (1W4) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232878122)

[2 Prerequisites 3](#_Toc232878123)

[2.1 System Access 3](#_Toc232878124)

[2.2 Roles 3](#_Toc232878125)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232878126)

[2.4 Additional Manual Configuration 4](#_Toc232878127)

[2.5 Preliminary Steps 4](#_Toc232878128)

[3 Overview Table 5](#_Toc232878129)

[4 Test Procedures 6](#_Toc232878130)

[4.1 Post Supplier Invoice 6](#_Toc232878131)

[4.2 Pay (via Payment Run) 8](#_Toc232878132)

[4.3 Create Outgoing Invoice 10](#_Toc232878133)

[4.4 Pay (via Incoming Payment) 12](#_Toc232878134)

## Purpose

Overview

This scope item establishes an integration between SAP S/4HANA Cloud Public Edition and Central Finance. The integration enables the replication of financial transaction data from SAP S/4HANA Cloud Public Edition to Central Finance. You can activate this data replication at the company code level within the SAP S/4HANA Cloud Public Edition system.

The integration uses Cloud Integration technologies (SAP Business Connector, Cloud Connector, WebSocket RFC). and the SAP Landscape Transformation Replication Server.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

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

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company was created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Use the following master data in the process steps described in this document:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | <company code> |  |  |
| Supplier | The supplier ID. For example, xx300001 (where xx is the first two digits of your company code) |  |  |
| Customer | The customer ID. For example, xx100001 (where xx is the first two digits of your company code) |  |  |
| Cost Center | For example, xx101101 (where xx is the first two digits of your company code) |  |  |
| Bank G/L Account | <account number> |  |  |
| House Bank | The bank ID. For example, xxBK1/xxAC1 (where xx is your ISO 3166 code) |  |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/3acdfe5858c184a3bfdd29e8c94a0378)

### Preliminary Steps

- The Integration Scenario SAP_COM_0083 is activated.
- SLT Connection is set up.
- CFIN Value- and Key-Mapping is maintained in the target system.
- CFIN Cost Object Mapping is activated in the target system.

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Post Supplier Invoice](#unique_9) [page ] 6 | Accounts Payable Accountant | Create Supplier Invoice (F0859) | The supplier invoice is reposted in the CFIN system. |
| [Pay (via Payment Run)](#unique_10) [page ] 8 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | The payment is reposted in the CFIN system with clearing. |
| [Create Outgoing Invoice](#unique_11) [page ] 10 | Accounts Receivable Accountant | Create Outgoing Invoices (FB70) | The outgoing invoice is reposted in the CFIN system. |
| [Pay (via Incoming Payment)](#unique_12) [page ] 12 | Accounts Receivable Accountant | Post Incoming Payments (F1345) | The payment is reposted in the CFIN system with clearing. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Post Supplier Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a supplier invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Payable Accountant in the subsidiary source system. |  |  |
| 2 | Access App | Open Create Supplier Invoice (F0859) | The Create Supplier Invoice screen displays. |  |
| 3 | Dialog Box | If the Data from Previous Invoice Entry Exist dialog box displays, choose No. |  |  |
| 4 | Enter Data | In the Basic Data section, make the following entries:Transaction: InvoiceCompany Code: <company code>Gross Invoice Amount: <amount>Currency: <currency>Invoice Date: <current date>Posting Date: <current date>Reference: <any>Invoicing Party: <supplier ID> |  |  |
| 5 | Add G/L Account Item | On the G/L Account Items tab, choose Add to add a new item.Enter the following data under G/L Account Items:Debit/Credit Indicator: DebitG/L Account: for example, 61400000Amount: <amount>Tax Code: <tax code>Cost Center: <cost center> |  |  |
| 6 | Post | Choose Post. | The Success dialog box displays, showing the document numbers created. Note down these document numbers. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the target Central Finance system. |  |  |
| 2 | Call Transaction | Call transaction FB03 and choose Document List. | The Document List screen displays. |  |
| 3 | Enter Data | Make the following entries, then choose Dynamic selections:Company Code: * (asterisk)Posting Date: <current date> |  |  |
| 4 | Add Dynamic Selections | Select Company Code in Sender System and Document No. in Sender System, then choose Copy Selected Items. |  |  |
| 5 | Display Replicated Documents | Make the following entries, then choose Execute:Company Code in Sender System: <company code>Document No. in Sender System: <document number> | The replicated document displays in the Document List. |  |

### Pay (via Payment Run)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you pay the supplier invoice via payment run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Accounts Payable Accountant in the subsidiary source system. |  |  |
| 2 | Access App | Open Manage Automatic Payments (F0770). | The Manage Automatic Payments screen displays. |  |
| 3 | Create Parameter | Choose Create Parameter. | The New Parameter dialog box displays. |  |
| 4 | Enter Data | Make the following entries and choose Create:Run Date: <current date>Identification: <any five character description, such as SPAY1> |  |  |
| 5 | Enter Data | Make the following entries:Basic section:Posting Date: <current date>Docs Entered Up To: <current date>Payment Controls section:Company Code: <company code>Next Payment Date: <current date + 5 days>Payment Method: <payment method>Open Item Selection section:Supplier:<supplier ID>Note For the Payment Method field, verify that the payment method is valid in the supplier master record. |  |  |
| 6 | Select Single Invoice | To execute a payment for a single invoice, make the following entries in the Open Item Selection by populating any of the Free Selection # fields available:Document Number (BKPF-BELNR): <document number from previous process step> |  |  |
| 7 | Save | Choose Save. | The system displays the message Parameter has been saved. The status changes to Parameter Created. |  |
| 8 | Schedule Proposal | Go back to the first view and choose Go.Select the row of your parameter and choose Schedule > Proposal. | The Schedule Proposal view is displayed. |  |
| 9 | Schedule Proposal | Make the following entries in the Schedule Proposal dialog box and choose Schedule:Start Date: <current date>Start immediately: Selected | The system displays the message Proposal is created.The status changes to Proposal Created. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the target Central Finance system. |  |  |
| 2 | Call Transaction | Call transaction FB03 and choose Document List. | The Document List screen displays. |  |
| 3 | Enter Data | Make the following entries, then choose Dynamic selections:Company Code: * (asterisk)Posting Date: <current date> |  |  |
| 4 | Add Dynamic Selections | Select Company Code in Sender System, then choose Copy Selected Items. |  |  |
| 5 | Display Replicated Documents | Make the following entries, then choose Execute:Company Code in Sender System: <company code> | The replicated document displays in the Document List. | The payment document is posted and the document header (F5) text contains the payment run information.The payment document line item is updated with the clearing document information. |

### Create Outgoing Invoice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an outgoing invoice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant in the subsidiary source system.. |  |  |
| 2 | Access App | Open Create Outgoing Invoices (FB70). | The Enter Customer Invoice: Company Code # view displays. |  |
| 3 | Enter Data | Choose the Company Code button and on the dialog box that displays, enter or verify your company code and choose Continue.Make the following entries:Customer: <customer ID>Invoice date: <current date>Reference: <any>Posting Date: <current date>Amount: <amount>Currency: <currency>Calculate Tax: <Selected> |  |  |
| 4 | Enter Data | Choose the Payment tab and enter the following:Bline Date : <current date>Pyt Terms: 0001Payt Meth. : <optional> |  |  |
| 5 | Maintain Line Items | In the line item table, make the following entries:G/L Account: for example, 41000400D/C: CreditAmount in doc.curr.: <amount>Tax Code : <tax code> |  |  |
| 6 | Assign Profitability Segment | If your account requires an assignenment to a controlling object, continue in the Items table and locate the Profit.segment column. Select the field button and an Assignment to a Profitability Segment dialog box displays.Make the following entries:Customer: <customer number>Profit Center: <any>Choose Derivation and then choose Continue to close the dialog box. |  |  |
| 6 | Post | Choose Post. | The journal entry is posted. Note down the document number. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the target Central Finance system. |  |  |
| 2 | Call Transaction | Call transaction FB03 and choose Document List. | The Document List screen displays. |  |
| 3 | Enter Data | Make the following entries, then choose Dynamic selections:Company Code: * (asterisk)Posting Date: <current date> |  |  |
| 4 | Add Dynamic Selections | Select Company Code in Sender System and Document No. in Sender System, then choose Copy Selected Items. |  |  |
| 5 | Display Replicated Documents | Make the following entries, then choose Execute:Company Code in Sender System: <company code>Document No. in Sender System: <document number> | The replicated document displays in the Document List. |  |

### Pay (via Incoming Payment)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you pay the supplier invoice via an incoming payment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant in the subsidiary source system.. |  |  |
| 2 | Access App | Open Post Incoming Payments (F1345). | The Post Incoming Payments screen appears. |  |
| 3 | Enter General Information | Make the following entries in the General Information area:Company Code : <company code>Posting Date : <current date>Journal Entry Date : <current date>Value Date : <current date>Journal Entry Type : DZ (Customer Payment) |  |  |
| 4 | Enter Bank Data | Make the following entries in the Bank Data area:G/L Account : for example 11001000House Bank/Account ID : <bank ID>Amount : <customer invoice amount>Currency : <currency> |  |  |
| 5 | Display Open Items | Make the following entries in the Open Item Selection and choose the Propose Items button:Account Type : CustomerAccount ID : <customer ID> | The open items are displayed in the bottom half of the view. |  |
| 6 | Pay Open Items | Find the journal entry created in the previous process step and choose Clear. | The selected item is transferred to view Items to Be Cleared. |  |
| 7 | Post Entries | Choose the Post button. | The Success dialog box displays details of the document number generated. Note down this document number. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the target Central Finance system. |  |  |
| 2 | Call Transaction | Call transaction FB03 and choose Document List. | The Document List screen displays. |  |
| 3 | Enter Data | Make the following entries, then choose Dynamic selections:Company Code: * (asterisk)Posting Date: <current date> |  |  |
| 4 | Add Dynamic Selections | Select Company Code in Sender System and Document No. in Sender System, then choose Copy Selected Items. |  |  |
| 5 | Display Replicated Documents | Make the following entries, then choose Execute:Company Code in Sender System: <company code>Document No. in Sender System: <document number> | The payment document is posted.The payment document line item is updated with the clearing document information. |  |

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
- related-to :: [[16-two-tier-erp-and-central-finance/test-script-process-integration-of-sap-s-4hana-finance-with-central-fi]]
- related-to :: [[16-two-tier-erp-and-central-finance/test-script-project-data-replication-to-central-finance-3w1-978]]
- related-to :: [[16-two-tier-erp-and-central-finance/two-tier-consolidation-of-autonomous-subsidiaries-via-central-finance]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1W4_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 20,655 chars in the whole document
