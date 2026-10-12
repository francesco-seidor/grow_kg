---
id: 03-financial-accounting-and-close/test-script-cash-journal-1go-ae-721
title: "Test Script: Cash Journal (1GO_AE) (1GO_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 1GO_AE (Cash Journal): posting entries, printing receipts and displaying the cash journal, company code 3310."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/cash-journal]
aliases: [1GO_S4CLD2608_BPD_EN_AE]
keywords: [Cash Journal, cash journal postings, cash receipt printing, cash journal display, test scripts, business roles, master data, output parameter determination, demo data, 1GO]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GO_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-721
topic: 03-financial-accounting-and-close/cash-journal
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Cash Journal (1GO_AE) (1GO_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GO_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Cash Journal** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Cash Journal (1GO_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232847075)

[2 Prerequisites 3](#_Toc232847076)

[2.1 System Access 3](#_Toc232847077)

[2.2 Roles 3](#_Toc232847078)

[2.3 Master Data and Organizational Data 4](#_Toc232847079)

[3 Overview Table 5](#_Toc232847080)

[4 Test Procedures 6](#_Toc232847081)

[4.1 Post Cash Journal Entries 6](#_Toc232847082)

[4.2 Print Cash Receipt 9](#_Toc232847083)

[4.3 Cash Journal 10](#_Toc232847084)

## Purpose

Overview

The cash journal is a subledger of Financial Accounting. It is used to manage a company's cash transactions. The system automatically calculates and displays the opening and closing balances and the receipts and payments totals. You can run several cash journals for each company code, and you can run a separate cash journal for each currency. You can also carry out postings to G/L accounts, supplier accounts, and customer accounts.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conduct the test in terms of system, user, master data, organizational data, and other test data and business conditions.

- Vendor master data has been created.
- Invoices have been posted to accounting.
- Complete Business Conditions.
- Execute Preliminary Steps.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data and Organizational Data

Default Values

The organizational structure and master data of your company was created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Master Data | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Chart of Accounts | YCOA |  |  |
| Controlling Area | A000 |  |  |
| Cost Center | 33101001 |  |  |

For more information about creating master data objects, see the following Master Data Scripts (MDS):

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Post Cash Journal Entries](#unique_7) [page ] 6 | General Ledger Accountant | Post Cash Journal Entries (FBCJ) | Cash Journal entries are posted. |
| [Print Cash Receipt](#unique_8) [page ] 9 | General Ledger Accountant | Post Cash Journal Entries (FBCJ) | The cash receipt is printed. |
| [Cash Journal](#unique_9) [page ] 10 | General Ledger Accountant | Cash Journal (S_P6B_12000118) | Cash Journal entries are displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Post Cash Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter cash-related journal entries. You use the cash journal to record bank transfers, customer receipts, supplier payments, and expenses like office supplies.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Cash Journal Entries (FBCJ) | The Cash Journal view displays. |  |
| 3 | Cash Journal | Choose the Change cash journal button. | The Cash Journal: Initial Data dialog box displays. |  |
| 4 | Company Code | Make the following entries and choose Continue:Company Code: 3310Cash Journal: for example, 0001 | The Company Code entered in the Enter Company Code selection screen is transferred into the Basic Data tab. |  |
| 5 | Select Display Period | In the Data selection area, make the following entries:Display period: for example, <current period>Note You can choose from three predefined display periods: Today, This Week, Current period |  |  |
| 6 | Cash Receipts | Choose the Cash receipts tab. |  |  |
| 7 | Post Bank Transfer to Journal | Make the following entries, then press Enter:Business transaction: Transfer Bank to JournalAmount: 1000Note The fields House Bank and Account ID are mandatory if the G/L account type is Cash Account.House Bank: for example, AEBK1/AEAC1Account ID: for example, AEAC1Posting Date: for example, <current date>Document Date: for example, <current date> | The bank transfer is entered into the cash journal. |  |
| 8 | Post Customer Receipt | On a new row, make the following entries and press Enter:Business transaction: CustomerAmount: 100Customer: for example, 33100050Posting Date: for example, <current date>Document Date: for example, <current date> | The customer receipt is entered into the cash journal. |  |
| 9 | Save Selection | Select the entries and choose Save Sel. | The selected entries are saved. |  |
| 10 | Post | Choose Post Sel. | Your cash journal entries are posted. |  |
| 11 | Cash Payments | Choose the Cash payments tab. |  |  |
| 12 | Post Supplier Payment | Make the following entries and press Enter:Business transaction: VendorAmount: 300Supplier: for example, 33300001Posting Date: for example, <current date>Document Date: for example, <current date> | The supplier payment is entered into the cash journal. |  |
| 13 | Post Office Supplies Expenses | On the new row, make the following entries and press Enter:Business transaction: Office SuppliesAmount: 150Tax Code: <Input Tax Code>Posting Date: for example, <current date>Document Date: for example, <current date>Cost Center: 33101101 | The office supplies expense is entered into the cash journal. |  |
| 14 | Post Journal Transfer to Bank | On the new row, make the following entries and press Enter:Business transaction: Transfer Journal to BankAmount: 500Note The fields House Bank and Account ID are mandatory if the G/L account type is Cash Account.House Bank: for example, AEBK1/AEAC1Account ID: for example, AEAC1Posting Date: for example, <current date>Document Date: for example, <current date> | The journal to bank transfer is entered into the cash journal. |  |
| 15 | Save | Select the cash journal entries and choose Save Sel. | Your cash journal entries are saved.Note When cash journal documents are saved, the system data is not updated. Data is only updated after posting. |  |
| 16 | Post | Choose Post Sel. | Your cash journal entries are posted. |  |
| 17 | Reverse Journal Entry (Original) | Select the cash journal entry to be deleted. Choose Menu > Edit > Delete entry .In the dialog box, make the following entries before the journal entry is reversed and choose Continue:Reversal reason: for example, 01 wrong postingPosting Date: for example, the wrong postings’ date | The cash journal entry is reversed. |  |

### Print Cash Receipt

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you print a cash journal receipt.

Prerequisite

| Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator |  |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). |  |  |
| 3 | Select Business Rule | Make the following entries:Show Rules for: Cash Journal ReceiptDetermination Step: Form Template |  |  |
| 4 | Maintain Business Rule | In the Maintain Business Rules section, choose the Edit button.Ensure that no value is maintained in the Recipient column. If a value exists, choose ∨ > Remove Cell Value to the right of the value in the cell. |  |  |
| 5 | Activate Business Rule | Choose Activate and confirm the Confirm Activation dialog box by selecting Yes. | The business rule is activated. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an General Ledger Accountant. |  |  |
| 2 | Access App | Open Post Cash Journal Entries (FBCJ). |  |  |
| 3 | Change Cash Journal | Choose Change Cash Journal. | A dialog box displays. |  |
| 4 | Cash Journal Details | Make the following entries and choose Continue:Company code: 3310Cash Journal: 0001 |  |  |
| 5 | Select Entry | Select a cash journal entry and choose Print Receipt. |  |  |
| 6 | Display Receipt | Choose Display Document. | The receipt is generated. |  |
| 7 | Check/Review Data | Check the PDF file against the data of cash journal entries, company code data, and business partner data. |  |  |
| 8 | Print/Save Receipt | Choose Print.To save the report, choose Download > Save . | The receipt is printed. |  |

### Cash Journal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the cash journal entries by company code, cash journal, and date interval.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Cash Journal (S_P6B_12000118). | The Cash Journal screen displays. |  |
| 3 | Select Cash journal to be displayed | Make the following entries and choose Execute:Company Code:3310Cash Journal: 0001Date interval: for example, <current period>Note G/L account 10010000 is not set to Post Automatically Only. If you plan to use an account only for automatic postings, you can use, for example, G/L account 10020000. | The Cash Journal for the selected interval is displayed |  |
| 4 | Export Cash Journal | From the menu, choose List > Export > Local file ( Ctrl Shift F9 ). | The Save list in file dialog box displays. |  |
| 5 | HTML Format | Select HTML Format and choose Continue. | A dialog box displays export file location details. |  |
| 6 | Export Cash Journal | Make the following entries:File name: for example, Cash JournalNote The Cash Journal export file can be downloaded locally by choosing Save a copy to the native file system in the directory selection. | The Cash Journal export file is generated |  |
| 7 | Print Cash Journal | Open the exported file in your Web browser. Print the file from your browser. | The Cash Journal is printed. |  |

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
- see-also :: [[03-financial-accounting-and-close/test-script-accounts-payable-j60-ae-sap-s-4hana-cloud-public-edition-2]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GO_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 18,018 chars in the whole document
