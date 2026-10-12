---
id: 03-financial-accounting-and-close/test-script-transaction-matching-sap-solution-extensions-by-blackline
title: "Test Script: Transaction Matching - SAP Solution Extensions by BlackLine (6IM) (6IM_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script (19-06-26) for BlackLine transaction matching: importing G/L and open item transactions via the BlackLine SAP Connector."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/account-reconciliation-blackline]
aliases: [6IM_S4CLD2608_BPD_EN_XX]
keywords: [Account Reconciliation and Transaction Matching with…, transaction matching, blackline integration, g/l transaction import, open item import, financial close, business roles, test scripts, additional manual configuration, 6IM]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6IM_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1172
topic: 03-financial-accounting-and-close/account-reconciliation-blackline
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Transaction Matching - SAP Solution Extensions by BlackLine (6IM) (6IM_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6IM_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Account Reconciliation and Transaction Matching with BlackLine** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Transaction Matching – SAP Solution Extensions by BlackLine (6IM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232826439)

[2 Prerequisites 3](#_Toc232826440)

[2.1 System Access 3](#_Toc232826441)

[2.2 Roles 3](#_Toc232826442)

[2.3 Master Data, Organizational Data, and Other Data 3](#_Toc232826443)

[2.4 Additional Manual Configuration 4](#_Toc232826444)

[2.5 Business Conditions 4](#_Toc232826445)

[3 Overview Table 5](#_Toc232826446)

[4 Test Procedures 6](#_Toc232826447)

[4.1 Import G/L Transactions 6](#_Toc232826448)

[4.2 Import Open Item Transactions 9](#_Toc232826449)

## Purpose

Overview

This solution extension supports the matching of data sets, usually done manually during the financial close.

This transaction matching service streamlines and automates detail-heavy reconciliations between key data sets, all in one centralized workspace.

This scope item covers the integration to the BlackLine Cloud Connector.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | <company code> |  |  |
| Chart of Accounts | YCOA |  |  |
| G/L Account | 10010000 |  |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/c8c8a8c569d8847eda65502ea1060183)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Must be run before this test script. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Import G/L Transactions](#unique_9) [page ] 6 | BlackLine System AdministratorGeneral Ledger Accountant | BlackLine CloudDisplay Line Items in General Ledger (F2217) | A new integration has been created.Files with data extracted from the SAP S/4HANA Cloud Public Edition system are successfully imported to BlackLine Cloud. The accounts are certified successfully. |
| [Import Open Item Transactions](#unique_10) [page ] 9 | BlackLine System AdministratorGeneral Ledger Accountant | BlackLine CloudDisplay Line Items in General Ledger (F2217) | A new integration has been created.Files with data extracted from the SAP S/4HANA Cloud Public Edition system are successfully imported into BlackLine Cloud. The accounts are certified successfully. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Import G/L Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The process extracts all G/L transactions from the SAP S/4HANA Cloud Public Edition system and imports them into the BlackLine Cloud application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the BlackLine Cloud system as a System Admin. |  |  |
| 2 | Access App | Navigate to the SAP Connector under System > Connectivity Center > SAP Connection. | The SAP Connector page displays. |  |
| 3 | Create New Integration | Choose New Integration to create a new integration. | The New Integration window displays. |  |
| 4 | Create New Integration | In the Type tab, make the following entries:Integration Name: for example, AllTrans_test_01Type: All transactionsSelect a valid existing connection profile from the Connection Profile drop down list. |  |  |
| 5 | Create New Integration | On the Segments tab, make the following entries:CompanyCode Segment Inclusions: <company code>GLAccount Segment Inclusions: for example, 61003000, 11002040, 12101000, 18100002, 19210000 |  |  |
| 6 | Create New Integration | On the Selection tab, make the following entries:Posting Date(s): <posting date>Fiscal Year(s): <fiscal year> |  |  |
| 7 | Create New Integration | On the Schedule tab, make the following entry:Don’t schedule automatically: Selected |  |  |
| 8 | Create New Integration | Choose Create and check if a new entry has been added to the Integration section. | A new integration has been created and added to the list of integrations in the Integration section. |  |
| 9 | Validate Integration | Select the integration which you created and choose Validate.The files will be generated and saved on the workstation. | The integration is opened and editable.Once the validation is executed, the files are written to a local machine and the Test Complete message appears. Please check the downloaded files. |  |
| 10 | Run Integration with Scheduler | Choose Run Once to trigger the execution of the newly created integration record.Choose Refresh History in the Extract History section to check if the integration run is scheduled.. | The integration run started and a record is available in the Extract History section. |  |
| 11 | Monitor Integration Run | Once the Integration Run status is Finished, choose the Show Log button in the Extract History section.Check the log records to verify that the output file has been stored on the FTP server and note down the file name from the log. | The Integration Run status is Finished.The output file is stored on the FTP server. |  |
| 12 | Import Extracted Data into BlackLine Cloud | Note If an automated FTP interface is created, the file will be imported automatically.To initiate a manual import for a file with transaction level data, navigate to System > Jobs > Import Data.Note Use the existing Import Definition<Transactions_import> and Data Source<SAP_Trxs_source> that were configured in cooperation with your BlackLine implementation consultant (or BlackLine partner) during the SAP Connector and matching module implementation process.Make the following entries:Import type: <Transactions_import>Browse to your file with transactions and choose Import.To monitor the import status, navigate to System > Jobs > Import Status.Note More information about the Matching Data Import Utility can be found on BlackLine Community:[https://myblackline.force.com/BlackLineCommunity/s/article/Matching-Data-Import-Utility-FAQ](https://myblackline.force.com/BlackLineCommunity/s/article/Matching-Data-Import-Utility-FAQ) | The file is imported with the following status:Import Status: FinishedSuccessful: Yes |  |
| 13 | Validate Import of Transactions | Navigate to Products > Match > Data sources.Select the Data Source<SAP_Trxs_source> and validate that the entries from the imported file have been added to the list. Verfiy that both sets of data match the output of the Display Line Items in General Ledger (F2217) app in the SAP S/4HANA Cloud Public Edition system.Note You can follow the instructions in the table below to generate output in the SAP S/4HANA Cloud Public Edition system. | The Display Line Items in General Ledger (F2217) app output matches the data in the output file generated by BlackLine Connector.The Display Line Items in General Ledger (F2217) app output matches the data imported into BlackLine Cloud. |  |
| 14 | Match Transactions | Navigate to Products > Match > Match sets.Note Use the existing Match Sets<Match_SAP_trxs> that was configured in cooperation with your BlackLine implementation consultant (or BlackLine partner) during the SAP Connector and matching module implementation process.Choose Run Now for the existing Match Set record <Match_SAP_trxs> to execute the Matching Engine.To monitor the import status, navigate to System > Jobs > Job Status.Navigate to Products > Match > Matched transactions.Select the link in the Suggested column for the Match Set record <Match_SAP_trxs>.On the Suggested Matches page, select the checkbox for transactions to match and choose Approve.Note More information about Transaction Matching can be found on BlackLine Community:[https://docs.blackline.com/bundle/blackline/page/transaction-matching/creating-a-match-set.html](https://docs.blackline.com/bundle/blackline/page/transaction-matching/creating-a-match-set.html)[https://docs.blackline.com/bundle/blackline/page/transaction-matching/running-the-matching-engine.html](https://docs.blackline.com/bundle/blackline/page/transaction-matching/running-the-matching-engine.html) | The transactions are matched successfully. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP S/4HANA Cloud Public Edition system as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Display Line Items in General Ledger (F2217). | The Display Line Items in General Ledger screen displays. |  |
| 3 | Execute App | Make the following entries and choose Go:Company Code: <same value as BlackLine Cloud>G/L Account: <same value as BlackLine Cloud>Posting Date: <same value as BlackLine Cloud>Fiscal Year: <same value as BlackLine Cloud> | Output is generated and ready to be used for comparison. You can compare the output against the data generated by BlackLine Connector and data imported into BlackLine Cloud. |  |

### Import Open Item Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process, you extract open item transactions from the SAP S/4HANA Cloud Public Edition system and import them into the BlackLine Cloud application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the BlackLine Cloud system as a System Admin. |  |  |
| 2 | Access App | Navigate to the SAP Connector under System > Connectivity Center > SAP Connection. | The SAP Connector page displays. |  |
| 3 | Create New Integration | Choose New Integration to create a new integration. | The New Integration window displays. |  |
| 4 | Create New Integration | In the Type tab, make the following entries:Integration Name: for example, OpenItems_test_01Type: Open ItemsSelect a valid existing connection profile from the Connection Profile drop down list. |  |  |
| 5 | Create New Integration | On the Segments tab, make the following entries:CompanyCode Segment Inclusions: <company code>GLAccount Segment Inclusions: for example, 61003000, 11002040, 12101000, 18100002,1 9210000 |  |  |
| 6 | Create New Integration | On the Selection tab, make the following entries:Period selection: CurrentInclude G/L Open Items: Selected |  |  |
| 7 | Create New Integration | On the Schedule tab, make the following entry:Don’t schedule automatically: Selected |  |  |
| 8 | Create New Integration | Choose Create and check if a new entry has been added to the Integration section. | A new integration has been created and added to list of integrations in the Integration section. |  |
| 9 | Validate Integration | Select the integration which you created and choose Validate.The files will be generated and saved on the workstation. | The integration is opened and editable.Once the validation is executed, the files are written to a local machine and the Test Complete message appears. Please check the downloaded files. |  |
| 10 | Run Integration with Scheduler | Choose Run Once to trigger the execution of the newly created integration record.Choose Refresh History in the Extract History section to check if the integration run is scheduled. | The integration run started and a record is available in the Extract History section. |  |
| 11 | Monitor Integration Run | Once the Integration Run status is Finished, choose the Show Log button in the Extract History section.Check the log records to verify that the output file has been stored on the FTP server and note down the file name from the log. | The Integration Run status is Finished.The output file is stored on the FTP server. |  |
| 12 | Import Extracted Data into BlackLine Cloud | Note If an automated FTP interface is created, the file will be imported automatically.To initiate a manual import for a file with transaction level data, navigate to System > Jobs > Import Data.Note Use the existing Import Definition<Transactions_import> and Data Source<SAP_Trxs_source> that were configured in cooperation with your BlackLine implementation consultant (or BlackLine partner) during the SAP Connector and matching module implementation process.Make the following entries:Import type: <Transactions_import>Browse to your file with transactions and choose Import.To monitor the import status, navigate to System > Jobs > Import Status.Note More information about the Matching Data Import Utility can be found on BlackLine Community:[https://myblackline.force.com/BlackLineCommunity/s/article/Matching-Data-Import-Utility-FAQ](https://myblackline.force.com/BlackLineCommunity/s/article/Matching-Data-Import-Utility-FAQ) | The file is imported with the following status:Import Status: FinishedSuccessful: Yes |  |
| 13 | Validate Import of Transactions | Navigate to Products > Match > Data sources.Select the Data Source<SAP_Trxs_source> and validate that the entries from the imported file have been added to the list. Verfiy that both sets of data match the output of the Display Line Items in General Ledger (F2217) app in the SAP S/4HANA Cloud Public Edition system.Note You can follow the instructions in the table below to generate output in the SAP S/4HANA Cloud Public Edition system. | The Display Line Items in General Ledger (F2217) app output matches the data in the output file generated by BlackLine Connector.The Display Line Items in General Ledger (F2217) app output matches the data imported into BlackLine Cloud. |  |
| 14 | Match Transactions | Navigate to Products > Match > Match sets.Note Use the existing Match Sets<Match_SAP_trxs> that was configured in cooperation with your BlackLine implementation consultant (or BlackLine partner) during the SAP Connector and matching module implementation process.Choose Run Now for the existing Match Set record <Match_SAP_trxs> to execute the Matching Engine.To monitor the import status, navigate to System > Jobs > Job Status.Navigate to Products > Match > Matched transactions.Select the link in the Suggested column for the Match Set record <Match_SAP_trxs>.On the Suggested Matches page, select the checkbox for transactions to match and choose Approve.Note More information about Transaction Matching can be found on BlackLine Community:[https://docs.blackline.com/bundle/blackline/page/transaction-matching/creating-a-match-set.html](https://docs.blackline.com/bundle/blackline/page/transaction-matching/creating-a-match-set.html)[https://docs.blackline.com/bundle/blackline/page/transaction-matching/running-the-matching-engine.html](https://docs.blackline.com/bundle/blackline/page/transaction-matching/running-the-matching-engine.html) | The transactions are matched successfully. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP S/4HANA Cloud Public Edition system as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Display Line Items in General Ledger (F2217). | The Display Line Items in General Ledger screen displays. |  |
| 3 | Execute App | Make the following entries and choose Go:Company Code: <same value as BlackLine Cloud>G/L Account: <same value as BlackLine Cloud>Status: <same value as BlackLine Cloud>Fiscal Year Period: <same value as BlackLine Cloud> | Output is generated and ready to be used for comparison. You can compare the output against the data generated by BlackLine Connector and data imported into BlackLine Cloud. |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-account-reconciliation-sap-solution-extensions-by-blacklin]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6IM_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 22,087 chars in the whole document
