---
id: 03-financial-accounting-and-close/test-script-intercompany-financial-posting-1gp-ae-722
title: "Test Script: Intercompany Financial Posting (1GP_AE) (1GP_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 1GP_AE: post, display, change and reverse cross-company-code journal entries, plus verification workflow appendix."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/intercompany-financial-posting]
aliases: [1GP_S4CLD2608_BPD_EN_AE]
keywords: [Cross-Company-Code Journal Postings, intercompany posting, cross-company journal entries, journal entry reversal, journal entry change, journal entry verification workflow, journal entry display, responsible team, journal entry approval, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GP_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-722
topic: 03-financial-accounting-and-close/intercompany-financial-posting
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Intercompany Financial Posting (1GP_AE) (1GP_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GP_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Cross-Company-Code Journal Postings** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Financial Posting (1GP_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232847085)

[2 Prerequisites 3](#_Toc232847086)

[2.1 Additional Manual Configuration 3](#_Toc232847087)

[2.2 System Access 3](#_Toc232847088)

[2.3 Roles 3](#_Toc232847089)

[2.4 Master Data, Organizational Data, and Other Data 4](#_Toc232847090)

[2.5 Business Conditions 4](#_Toc232847091)

[3 Overview Table 6](#_Toc232847092)

[4 Test Procedures 7](#_Toc232847093)

[4.1 Post General Journal Entry Between Two Company Codes 7](#_Toc232847094)

[4.2 Display Journal Entries Cross-Company Code 8](#_Toc232847095)

[4.3 Change Journal Entries Cross-Company Code 9](#_Toc232847096)

[4.4 Reverse Journal Entries Cross-Company Code 10](#_Toc232847097)

[5 Appendix 12](#_Toc232847098)

[5.1 Configure Responsible Team 12](#_Toc232847099)

[5.2 Configure Workflow Definition for Intercompany 13](#_Toc232847100)

[5.3 Submit Journal Entry to Be Verified (Intercompany) 15](#_Toc232847101)

[5.4 Approve Journal Entry by Different User (Intercompany) 16](#_Toc232847102)

[5.5 Check the Journal Entry Status (Intercompany) 17](#_Toc232847103)

## Purpose

Overview

In an intercompany posting across company codes, the system posts a separate document with its own document number in each of the company codes. Individual documents are linked by a common cross-company code number. The system generates line items to balance the debits and credits in each document.

The company codes involved must be part of a single legal entity for tax purposes if one of the following is true:

- The receivables or payables are posted in a different company code from the one in which the revenue or expenses (costs) are posted
- The business transaction is relevant to taxes

In addition, the customer can assign a paying company code to each company code. You can have a company code process the payment transactions centrally for several company codes. However, these company codes must be in the same country/region and have the same local currency and parallel currencies. They must have the same settings for enhanced withholding tax functions (active or inactive).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/1d27f8a26830d7ca14b5a4590a1454f2)

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
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Chart of Accounts | YCOA |  |  |
| Controlling Area | A000 |  |  |

You can find general information on how to create master data objects in the following Master Data Scripts (MDS):

| MDS | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |

### Business Conditions

The following business conditions must be met before this scope item can be tested,

| Scope Item ID | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Post General Journal Entry |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post General Journal Entry Between Two Company Codes](#unique_9) [page ] 7 | General Ledger Accountant | Post General Journal Entries (F0718) | The general ledger account document is posted. |
| [Display Journal Entries Cross-Company Code](#unique_10) [page ] 8 | General Ledger Accountant | Display Journal Entries - Cross-Company Code (FBU3) | The financial documents with the cross-company postings are displayed. |
| [Change Journal Entries Cross-Company Code](#unique_11) [page ] 9 | General Ledger Accountant | Change Journal Entries - Cross-Company Code (FBU2) | The cross-company document is changed. |
| [Reverse Journal Entries Cross-Company Code](#unique_12) [page ] 10 | General Ledger Accountant | Reverse Journal Entries - Cross-Company Code (FBU8) | The cross-company document is reversed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Post General Journal Entry Between Two Company Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post a general journal entry between two company codes.

Prerequisite

You must have more than one company code in one country.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entry Header Data | In the Header pane, make the following entries and press Enter:Journal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: <leave blank> |  |  |
| 4 | Enter Line Item Data | In the Line Items pane, make the following entries and press Enter:Company Code: 3310G/L Account: For example, 63002000Debit: 100Tax Code: For example, <Input Tax Code>Cost Center: for example, 33101101 |  |  |
| 5 | Enter Line Item Data | In the Line Items pane, make the following entries and press Enter:Company Code: <second company code>G/L Account: For example, 63002000Credit: 100Tax Code: For example, <Input Tax Code>Cost Center: For example, <second company cost center> |  |  |
| 6 | Post | Choose Post. | The general ledger account document is posted. The system displays the message Document XXXXXXXX (YYYY, ZZZZ) was posted successfully. |  |

### Display Journal Entries Cross-Company Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the journal entries for cross company codes (the journal entry you posted in the first step should be displayed).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Journal Entries - Cross-Company Code (FBU3). | The Display Journal Entries Cross-Company Code view is displayed. |  |
| 3 | Display CC Document List | Choose Document List. | The List of Cross-Company Code Transactions view is displayed. |  |
| 4 | Execute Document List | Caution If you run the app without entering a cross-company-code number, execution and display of results may take a long time.Enter a value or range in the Cross-Comp.Code No. fields and choose Execute. | The List of Cross-Company Code Transactions view is displayed. |  |
| 5 | Select Document | From the list, select the checkbox next to the document to display, and choose Choose . | The Display Transaction Overview view is displayed. |  |

### Change Journal Entries Cross-Company Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you change the journal entries for cross-company codes (the document you posted in the first step should be changed).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Change Journal Entries - Cross-Company Code (FBU2). | The Change Transaction: Initial view is displayed. |  |
| 3 | Select Document from List | Choose Document List. | The List of Cross-Company Code Transactions view is displayed. |  |
| 4 | Enter Selection Criteria | Make the following entries and choose Execute:Company code: 3310Fiscal Year: <current year> |  |  |
| 5 | Select Document | Select a document to change and choose Choose. | The Change Transaction: Overview view is displayed. |  |
| 6 | Select Document Header | Select a line in the document header area and choose Select Individual Object. | The Document Header: XXXX Company code view is displayed. |  |
| 7 | Change Journal Entry | Change the text in the Doc. Header Text and Reference fields, then choose Continue/Confirm. |  |  |
| 8 | Save Changes | Choose Save. | The document is changed and saved. |  |

### Reverse Journal Entries Cross-Company Code

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reverse the journal entry for cross-company codes (the document you posted in the first step should be reversed).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Reverse Journal Entries - Cross-Company Code (FBU8). | The Reverse Cross-Company Code Transaction: Header Data view is displayed. |  |
| 3 | Enter CC Document Number | Make the following entries and choose Post:Cross-co. code no: current posted CC document numberReversal Reason: 01 | The cross-company journal entry is reversed. |  |

## Appendix

### Configure Responsible Team

Purpose

In this activity, you configure the team responsible for the journal entry workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Manage Teams and Responsibilities For Journal Entry Verification - In General Ledger (F3932). | Ensure that FGJEV G/L Journal Entry Verification is chosen in the Category field. |  |
| 3 | Create Team | Choose Create. | The New Team view is displayed. |  |
| 4 | Enter Team Details | Make the following entries:General Information section:Name: RESPONSIBLE <first company code>Description: RESPONSIBLE <first company code>Type: FGLVGResponsibility Definitions section:Company Code: <first company code>Cost center: <leave blank>GL account Group: <leave blank>Team Owners section:Note The fields in this section are automatically populated with the details for the General Ledger Accountant. |  |  |
| 5 | Enter Team Members | In the Team Members section, choose Create. | The Select: Business Partner dialog box is displayed. |  |
| 6 | Enter Team Members | Search for the user for the General Ledger Accountant for the other country/region, then choose OK. |  |  |
| 7 | Enter Team Members | Make the following entries:Function: FGJEV_L1 (Group 1 for Verifying G/L Journal Entries) |  |  |
| 8 | Save | Choose Save. | The Team view is displayed. |  |
| 9 | Edit | Choose Edit. |  |  |
| 10 | Team Information | Choose the Team Information tab. |  |  |
| 11 | Change Status | Make the following entries and choose Save:Status: Ready to Use |  |  |
| 12 | Create Team for Another Company Code | Repeat steps 3-12 for the following information:Name: RESPONSIBLE <second company code>Type: FGLVGCompany Code: <second company code>User: GL_ACCOUNTANT role for second company code's country/region |  |  |

### Configure Workflow Definition for Intercompany

Purpose

In this activity, you configure the workflow for the intercompany process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Manage Workflows for Journal Entry Verification - In General Ledger (F2720). |  |  |
| 3 | Create Workflow | Choose Add. | The New Workflow view is displayed. |  |
| 4 | Enter Details | Make the following entries:Workflow Name: Intercompany GJE VerificationStep Properties section:Description: Intercompany GJE VerificationStart Conditions section:Only start the workflow if all of the following preconditions are met: (None) |  |  |
| 5 | Step Sequence | In the Step Sequence section, choose Add. |  |  |
| 6 | Enter Details | Make the following entries and choose Add:Step Name: IntercompanyStep Type: Verify Intercompany General Journal EntryRecipients section:Assignment By: RoleRole: Group 1 for Verifying G/L Journal EntriesStep to be completed by: All of the recipientsException Handling section:For Reject:Required Action: Redo General Journal EntryAction Result: Restart WorkflowFor Processing obsolete:Required Action: Do nothingAction Result: Cancel Workflow | The system returns to the prior screen. |  |
| 7 | Step Sequence | Repeat steps 5 and 6 with the following data:Name: PostType: Post General Journal EntryNote Don't make any other entries on this screen. | The system returns to the prior screen. |  |
| 8 | Save | Choose Save. |  |  |
| 9 | Activate | Choose Activate. | The workflow is activated. |  |

### Submit Journal Entry to Be Verified (Intercompany)

Purpose

In this activity, you submit the journal entry for intercompany verification.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Verify General Journal Entries - For Requester (F2547A). |  |  |
| 3 | Add Journal Entry | In the Journal Entries section, choose Create. |  |  |
| 4 | Enter Details | Make the following entries in the header:Journal Entry Date: <date of journal entry>Posting Date: <posting date>Journal Entry Type: <journal entry type>Company Code: 3310Transaction Currency: AEDMake the following entries for Line Item 1:Company Code: <first company code>G/L Account: 11001010Debit: 100.00Value Date: <today's date>Make the following entries for Line Item 2:Company Code: <second company code>G/L Account: 11001010Credit: 100.00Value Date: <today's date> |  |  |
| 5 | Submit | Choose Submit.Make a note of the journal entry number. | The system notifies you that the journal entry was submitted for verification in the company code from the first line item.The document is parked. |  |
| 6 | Back | Choose Back. |  |  |
| 7 | Review | In the Journal Entries section, locate your journal entry number. | The status is Submitted. |  |

### Approve Journal Entry by Different User (Intercompany)

Purpose

In this activity, the approvers in each company code approve the journal entry per the workflow setup.

Procedure - First Company Code

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for the country/region of the first company code. |  |  |
| 2 | Access SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The Verify General Journal Entry view displays. |  |
| 3 | Select Journal Entry | In the left pane, choose the journal entry to process. |  |  |
| 4 | Approve | Choose Approve. | The workflow is approved. |  |

Procedure – Second Company Code

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for the country/region of the second company code. |  |  |
| 2 | Access SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The Verify General Journal Entry view displays. |  |
| 3 | Select Journal Entry | In the left pane, choose the journal entry to process. |  |  |
| 4 | Approve | Choose Approve. | The workflow is approved. |  |

### Check the Journal Entry Status (Intercompany)

Purpose

In this activity, you verify the status of the journal entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Verify General Journal Entries - For Requester (F2547A). | The Verify General Journal Entries view displays. |  |
| 3 | Select Journal Entry | In the Journal Entries pane, find the journal entry from the prior steps. | The Status field for the journal entry is Posted. |  |

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
- see-also :: [[03-financial-accounting-and-close/2608-journal-entry-template-xxxx-pu1010-115]]
- see-also :: [[03-financial-accounting-and-close/intercompany-billing-for-cross-company-cost-accounting-postings-4an-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GP_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 24,445 chars in the whole document
