---
id: 03-financial-accounting-and-close/test-script-account-reconciliation-sap-solution-extensions-by-blacklin
title: "Test Script: Account Reconciliation – SAP Solution Extensions by BlackLine (6IL) (6IL_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 6IL: BlackLine Cloud connector imports (currency, G/L, AP, AR, multi-currency, account analysis) and certification."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/account-reconciliation-blackline]
aliases: [6IL_S4CLD2608_BPD_EN_XX]
keywords: [Account Reconciliation and Transaction Matching with…, account reconciliation, blackline integration, currency rates import, g/l account balances, ap sub-ledger balances, ar sub-ledger balances, multi-currency balances, account analysis, reconciliation certification]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6IL_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1171
topic: 03-financial-accounting-and-close/account-reconciliation-blackline
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Account Reconciliation – SAP Solution Extensions by BlackLine (6IL) (6IL_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6IL_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Account Reconciliation and Transaction Matching with BlackLine** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Account Reconciliation – SAP Solution Extensions by BlackLine (6IL) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232826319)

[2 Prerequisites 3](#_Toc232826320)

[2.1 System Access 3](#_Toc232826321)

[2.2 Roles 3](#_Toc232826322)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232826323)

[2.4 Additional Manual Configuration 4](#_Toc232826324)

[2.5 Business Conditions 4](#_Toc232826325)

[3 Overview Table 5](#_Toc232826326)

[4 Test Procedures 6](#_Toc232826327)

[4.1 Import Currency Rates 6](#_Toc232826328)

[4.2 Import G/L Account Balances and Certify Account 8](#_Toc232826329)

[4.3 Import AP Sub-Ledger Balances and Certify Account 12](#_Toc232826330)

[4.4 Import AR Sub-Ledger Balances and Certify Account 16](#_Toc232826331)

[4.5 Import G/L Account Multi-Currencies and Certify Account 20](#_Toc232826332)

[4.6 Import Account Analysis Data and Certify Account 23](#_Toc232826333)

## Purpose

Overview

This service automates and standardizes the balance sheet account reconciliation process to produce high-quality and accurate financial statements. It drives accuracy in the financial close by providing accountants with a streamlined method to verify the correctness and appropriateness of their balance sheets.

Accountants can quickly compare general ledger, bank, and other data, at the balance or line-item level, investigate discrepancies, attach supporting documentation, and take required actions from an intuitive, unified workspace.

This scope item covers the integration to the BlackLine Cloud connector.

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
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | <company code> |  |  |
| Chart of Accounts | YCOA |  |  |
| G/L Account | 10010000 |  |  |
| Customer | For example, xx100001 (where xx is the value of the first two digits of your company code) |  |  |
| Vendor | For example, xx300001 (where xx is the value of the first two digits of your company code) |  |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/9d4df9c78372c27aaaebe5a3a829f6f7)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Must be run before this test script. |
| J59 - Accounts Receivable | Must be run before this test script. |
| J60 - Accounts Payable | Must be run before this test script. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Import Currency Rates](#unique_9) [page ] 6 | BlackLine System AdministratorGeneral Ledger Accountant | BlackLine CloudCurrency Exchange Rates (F3616) | A new integration has been created.Files with data extracted from the SAP S/4HANA Cloud Public Edition system are successfully imported into BlackLine Cloud. |
| [Import G/L Account Balances and Certify Account](#unique_10) [page ] 8 | BlackLine System Administrator, Preparer, and ApproverGeneral Ledger Accountant | BlackLine CloudDisplay G/L Account Balances (F0707A) | A new integration has been created.Files with data extracted from the SAP S/4HANA Cloud Public Edition system are successfully imported into BlackLine Cloud. The accounts are certified successfully. |
| [Import AP Sub-Ledger Balances and Certify Account](#unique_11) [page ] 12 | BlackLine System Administrator, Preparer, and ApproverAccounts Payable Accountant | BlackLine CloudManage Supplier Line Items (F0712) | A new integration has been created.Files with data extracted from the SAP S/4HANA Cloud Public Edition system are successfully imported into BlackLine Cloud. The accounts are certified successfully. |
| [Import AR Sub-Ledger Balances and Certify Account](#unique_12) [page ] 16 | BlackLine System Administrator, Preparer, and ApproverAccounts Receivable Accountant | BlackLine CloudManage Customer Line Items (F0711) | A new integration has been created.Files with data extracted from the SAP S/4HANA Cloud Public Edition system are successfully imported to BlackLine Cloud. The accounts are certified successfully. |
| [Import G/L Account Multi-Currencies and Certify Account](#unique_13) [page ] 20 | BlackLine System Administrator, Preparer, and ApproverGeneral Ledger Accountant | BlackLine CloudDisplay G/L Account Balances (F0707A) | A new integration has been created.Files with data extracted from the SAP S/4HANA Cloud Public Edition system are successfully imported into BlackLine Cloud. The accounts are certified successfully.. |
| [Import Account Analysis Data and Certify Account](#unique_14) [page ] 23 | BlackLine System Administrator, Preparer, and ApproverGeneral Ledger Accountant | BlackLine CloudDisplay G/L Account Balances (F0707A) Display Line Items in General Ledger (F2217) | A new integration has been created.Files with data extracted from the SAP S/4HANA Cloud Public Edition system are successfully imported into BlackLine Cloud. The accounts are certified successfully. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Import Currency Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The process extracts currency rates from the SAP S/4HANA Cloud Public Edition system and imports them into BlackLine Cloud.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the BlackLine Cloud system as a System Admin. |  |  |
| 2 | Access App | Navigate to the SAP Connector under System > Connectivity Center > SAP Connection. | The SAP Connector page displays. |  |
| 3 | Create New Integration | Choose New Integration to create a new integration. | The New Integration window displays. |  |
| 4 | Create New Integration | In the Type tab, make the following entries:Integration Name: for example, Curr_rates_test_01Type: Currency ratesSelect a valid existing connection profile from the Connection Profile drop down list. |  |  |
| 5 | Create New Integration | On the Selection tab, make the following entries:Exchange Rate Type: MKey Date: <key date>Company Code: <company code>Exchange Rate Currency: <currencies> |  |  |
| 6 | Create New Integration | On the Schedule tab, make the following entry:Don’t schedule automatically: Selected |  |  |
| 7 | Create New Integration | Choose Create and check if a new entry has been added to the Integration section. | A new integration has been created and added to list of integrations in the Integration section. |  |
| 8 | Validate Integration | Select the integration which you created and choose Validate.The files will be generated and saved on the workstation. | The integration is opened and editable.Once the validation is executed, the files are written to a local machine and the Test Complete message appears. Please check the downloaded files. |  |
| 9 | Run Integration with Scheduler | Choose Run Once to trigger the execution of the newly created integration record.Choose Refresh History in the Extract History section to check if the integration run is scheduled. | The integration run started and a record is available in the Extract History section. |  |
| 10 | Monitor Integration Run | Once the Integration Run status is Finished, choose the Show Log button in the Extract History section.Check the log records to verify that the output file has been stored on the FTP server and note down the file name from the log. | The Integration Run status is Finished.The output file is stored on the FTP server. |  |
| 11 | Import Extracted Data into BlackLine Cloud | Note If an automated FTP interface is created, the file will be imported automatically.To initiate a manual import, navigate to System > Jobs > Import Data.Select Cross Currency Rates from the drop down list.Locate your file and choose Import.Note More information about the data import functionality can be found on BlackLine Community:[https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ](https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ) | The file is imported with the following status:Import Status: FinishedSuccessful: Yes |  |
| 12 | Validate Import of Currency Rates | Navigate to System > Jobs > Currency Information.Make sure that the correct period is selected.Validate that the entries from the imported file have been added to the list. Verfiy that both sets of data match the output of the Currency Exchange Rates (F3616) app in SAP S/4HANA Cloud Public Edition.Note You can follow the instructions in the table below to generate output in the SAP S/4HANA Cloud Public Edition system. | The Currency Exchange Rates (F3616) app output matches the data in the output file generated by BlackLine Connector.The Currency Exchange Rates (F3616) app output matches the data imported into BlackLine Cloud. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP S/4HANA Cloud Public Edition system as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Currency Exchange Rates (F3616). | The Currency Exchange Rates screen displays. |  |
| 3 | Execute App | Make the following entries and choose Go:Exchange Rate Type: MValid From: <same value as BlackLine Cloud>Currency Pair: <same value as BlackLine Cloud> | Output is generated and ready to be used for comparison. You can compare the output against the data generated by BlackLine Connector and data imported to BlackLine Cloud. |  |

### Import G/L Account Balances and Certify Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The process extracts G/L balances from the SAP S/4HANA Cloud Public Edition system and imports them into the BlackLine Accounts Reconciliation application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the BlackLine Cloud system as a System Admin. |  |  |
| 2 | Access App | Navigate to the SAP Connector under System > Connectivity Center > SAP Connection. | The SAP Connector page displays. |  |
| 3 | Create New Integration | Choose New Integration to create a new integration. | The New Integration window displays. |  |
| 4 | Create New Integration | In the Type tab, make the following entries:Integration Name: for example, GL_Account_test_01Type: G/L Account BalancesSelect a valid existing connection profile from the Connection Profile drop down list. |  |  |
| 5 | Create New Integration | On the Segments tab, make the following entries:CompanyCode Segment Inclusions: <company code>GLAccount Segment Inclusions: for example, 10010000 |  |  |
| 6 | Create New Integration | On the Selection tab, make the following entries:Period Selection: CustomKey Date: <key date>Ledger: for example, 0LGL Account Balance: AmountInGlobalCurrencyGL Reporting Balance: AmountInCompanyCodeCurrencyGL Alternate Balance: AmountInCompanyCodeCurrency |  |  |
| 7 | Create New Integration | On the Schedule tab, make the following entry:Don’t schedule automatically: Selected |  |  |
| 8 | Create New Integration | Choose Create and check if a new entry has been added to the Integration section. | A new integration has been created and added to list of integrations in the Integration section. |  |
| 9 | Validate Integration | Select the integration which you created and choose Validate.The files will be generated and saved on the workstation. | The integration is opened and editable.Once the validation is executed, the files are written to a local machine and the Test Complete message appears. Please check the downloaded files. |  |
| 10 | Run Integration with Scheduler | Choose Run Once to trigger the execution of the newly created integration record.Choose Refresh History in the Extract History section to check if the integration run is scheduled. | The integration run started and a record is available in the Extract History section. |  |
| 11 | Monitor Integration Run | Once the Integration Run status is Finished, choose the Show Log button in the Extract History section.Check the log records to verify that the output file has been stored on the FTP server and note down the file name from the log. | The Integration Run status is Finished.The output file is stored on the FTP server. |  |
| 12 | Import Extracted Data into BlackLine Cloud | Note If an automated FTP interface is created, the file will be imported automatically.To initiate a manual import, navigate to System > Jobs > Import Data.Select Accounts from the drop down list.Locate your file and choose Import.Note More information about the data import functionality can be found on BlackLine Community:[https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ](https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ) | The file is imported with the following status:Import Status: FinishedSuccessful: Yes |  |
| 13 | Validate Import of Accounts | Navigate to Products > Accounts > View Reconciliations.Make sure that the correct period is selected.Validate that the entries from the imported file have been added to the list. Verfiy that both sets of data match the output of the Display G/L Account Balances (F0707A) app in SAP S/4HANA Cloud Public Edition.Note You can follow the instructions in the table below to generate output in the SAP S/4HANA Cloud Public Edition system. | The Display G/L Account Balances (F0707A) app output matches the data in the output file generated by BlackLine Connector.The Display G/L Account Balances (F0707A) app output matches the data imported into BlackLine Cloud. |  |
| 14 | Prepare Account Reconciliations for Certification | Log on as a Preparer.Navigate to Products > Accounts > View Reconciliation.Note Make sure that you selected the correct period.Choose Edit to open an imported account.Choose the Add Supporting Item link next to Supporting Items to add a supporting item to zero out the Unidentified Difference and make the reconciliation certifiable.Make the following entries to zero out the Unidentified Difference:Txn. Amount: <amount>Amount: <amount>Alternate Amount: <amount>Rpt. Amount: <amount>Choose List Component from the Item Class section.Make the following entries and choose Save:Description: <description> | The supporting item is created and the account reconciliation is certifiable. |  |
| 15 | Certify Account by Preparer | Choose Certify to start the reconciliation certification process.Once the Certification Statement page is loaded, choose Certify to certify the reconciliation. | The account reconciliation is certified to Prepared status. |  |
| 16 | Certify Account by Approver | Log on as an Approver.Navigate to Products > Accounts > View Reconciliation.Note Make sure that you selected the correct period.Choose the 'Cert' link.Choose Certify to start the reconciliation certification process.Once the Certification Statement page is loaded, choose Certify to certify the reconciliation. | The account has been certified successfully. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP S/4HANA Cloud Public Edition system as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Display G/L Account Balances (F0707A). | The Display G/L Account Balances screen displays. |  |
| 3 | Execute App | Make the following entries and choose Go:Ledger: <same value as BlackLine Cloud>Company Code : <same value as BlackLine Cloud>G/ LAccount: <same value as BlackLine Cloud>From Period: <same value as BlackLine Cloud>To Period: <same value as BlackLine Cloud>Fiscal Year of Ledger: <same value as BlackLine Cloud> | The output is generated and ready to be used for comparison against the data generated by BlackLine Connector and data imported into BlackLine Cloud. |  |

### Import AP Sub-Ledger Balances and Certify Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The process extracts AP sub-ledger balances from the SAP S/4HANA Cloud Public Edition system and imports them into the BlackLine Accounts Reconciliation application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the BlackLine Cloud system as System Admin. |  |  |
| 2 | Access App | Navigate to the SAP Connector under System > Connectivity Center > SAP Connection. | The SAP Connector page displays. |  |
| 3 | Create New Integration | Choose New Integration to create a new integration. | The New Integration window displays. |  |
| 4 | Create New Integration | In the Type tab, make the following entries:Integration Name: for example, APsubledgers_test_01Type: AP sub-ledger balancesSelect a valid existing connection profile from the Connection Profile drop down list. |  |  |
| 5 | Create New Integration | On the Segments tab, make the following entries:CompanyCode Segment Inclusions: <company code>GLAccount Segment Inclusions: for example, 217201111-217201120 |  |  |
| 6 | Create New Integration | On the Selection tab, make the following entries:Period Selection: CustomKey Date: <key date>Ledger: for example, 0LGL Account Balance: AmountInGlobalCurrencyGL Reporting Balance: AmountInCompanyCodeCurrencyGL Alternate Balance: AmountInCompanyCodeCurrency |  |  |
| 7 | Create New Integration | On the Schedule tab, make the following entry:Don’t schedule automatically: Selected |  |  |
| 8 | Create New Integration | Choose Create and check if a new entry has been added to the Integration section. | A new integration has been created and added to list of integrations in the Integration section. |  |
| 9 | Validate Integration | Select the integration which you created and choose Validate.The files will be generated and saved on the workstation. | The integration is opened and editable.Once the validation is executed, the files are written to a local machine and the Test Complete message appears. Please check the downloaded files. |  |
| 10 | Run Integration with Scheduler | Choose Run Once to trigger the execution of the newly created integration record.Choose Refresh History in the Extract History section to check if the integration run is scheduled. | The integration run started and a record is available in the Extract History section. |  |
| 11 | Monitor Integration Run | Once the Integration Run status is Finished, choose the Show Log button in the Extract History section.Check the log records to verify that the output file has been stored on the FTP server and note down the file name from the log. | The Integration Run status is Finished.The output file is stored on the FTP server. |  |
| 12 | Import Extracted Data into BlackLine Cloud | Note Before importing sub-ledger accounts, make sure that you have imported G/L account balances for these sub-ledger accounts. If you have not done this yet, please complete Import G/L Account Balances and Certify Account to import the G/L account balances.Note If an automated FTP interface is created, the file will be imported automatically.To initiate a manual import, navigate to System > Jobs > Import Data.Select Subledgers from the drop down list.Locate your file and choose Import.Note More information about the data import functionality can be found on BlackLine Community:[https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ](https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ) | The file is imported with the following status:Import Status: FinishedSuccessful: Yes |  |
| 13 | Validate Import of AP Sub-Ledger Balances | Navigate to Products > Accounts > View Reconciliations.Make sure that the correct period is selected and that GL Account Reconciliation Templates exist fo the imported sub-ledger accounts.Validate that the entries from the imported file have been added to the list. Verfiy that both sets of data match the output of the Manage Supplier Line Items (F0712) app in SAP S/4HANA Cloud Public Edition.Note You can follow the instructions in the table below to generate output in the SAP S/4HANA Cloud Public Edition system. | The Manage Supplier Line Items (F0712) app output matches the data in the output file generated by BlackLine Connector.The Manage Supplier Line Items (F0712) app output matches the data imported into BlackLine Cloud. |  |
| 14 | Prepare Account Reconciliations for Certification | Log on as a Preparer.Navigate to Products > Accounts > View Reconciliation.Note Make sure that you selected the correct period.Choose Edit to open an imported account.Choose the Add Supporting Item link next to Supporting Items to add a supporting item to zero out the Unidentified Difference and make the reconciliation certifiable.Make the following entries to zero out the Unidentified Difference:Txn. Amount: <amount>Amount: <amount>Alternate Amount: <amount>Rpt. Amount: <amount>Choose List Component from the Item Class section.Make the following entries and choose Save:Description: <description> | The supporting item is created and the account reconciliation is certifiable. |  |
| 15 | Certify Account by Preparer | Choose Certify to start the reconciliation certification process.Once the Certification Statement page is loaded, choose Certify to certify the reconciliation. | The account reconciliation is certified to Prepared status. |  |
| 16 | Certify Account by Approver | Log on as an Approver.Navigate to Products > Accounts > View Reconciliation.Note Make sure that you selected the correct period.Choose the 'Cert' link.Choose Certify to start the reconciliation certification process.Once the Certification Statement page is loaded, choose Certify to certify the reconciliation. | The account has been certified successfully. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP S/4HANA Cloud Public Edition system as a Accounts Payable Accountant. |  |  |
| 2 | Access App | Open Manage Supplier Line Items (F0712). | The Manage Supplier Line Items screen displays. |  |
| 3 | Execute App | Make the following entries and choose Go:Company Code : <same value as BlackLine Cloud>Status: <same value as BlackLine Cloud>Open on Key Date: <same value as BlackLine Cloud>Item Type: <same value as BlackLine Cloud>G/ LAccount: <same value as BlackLine Cloud> | The output is generated and ready to be used for comparison against the data generated by BlackLine Connector and data imported into BlackLine Cloud. |  |

### Import AR Sub-Ledger Balances and Certify Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The process extracts AR sub-ledger balances from the SAP S/4HANA Cloud Public Edition system and imports into the BlackLine Accounts Reconciliation application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the BlackLine Cloud system as System Admin. |  |  |
| 2 | Access App | Navigate to the SAP Connector under System > Connectivity Center > SAP Connection. | The SAP Connector page displays. |  |
| 3 | Create New Integration | Choose New Integration to create a new integration. | The New Integration window displays. |  |
| 4 | Create New Integration | In the Type tab, make the following entries:Integration Name: for example, ARsubledgers_test_01Type: AR sub-ledger balancesSelect a valid existing connection profile from the Connection Profile drop down list. |  |  |
| 5 | Create New Integration | On the Segments tab, make the following entries:CompanyCode Segment Inclusions: <company code>GLAccount Segment Inclusions: for example, 12199111-12199120 |  |  |
| 6 | Create New Integration | On the Selection tab, make the following entries:Period Selection: CustomKey Date: <key date>Ledger: for example, 0LGL Account Balance: AmountInGlobalCurrencyGL Reporting Balance: AmountInCompanyCodeCurrencyGL Alternate Balance: AmountInCompanyCodeCurrency |  |  |
| 7 | Create New Integration | On the Schedule tab, make the following entry:Don’t schedule automatically: Selected |  |  |
| 8 | Create New Integration | Choose Create and check if a new entry has been added to the Integration section. | A new integration has been created and added to list of integrations in the Integration section. |  |
| 9 | Validate Integration | Select the integration which you created and choose Validate.The files will be generated and saved on the workstation. | The integration is opened and editable.Once the validation is executed, the files are written to a local machine and the Test Complete message appears. Please check the downloaded files. |  |
| 10 | Run Integration with Scheduler | Choose Run Once to trigger the execution of the newly created integration record.Choose Refresh History in the Extract History section to check if the integration run is scheduled. | The integration run started and a record is available in the Extract History section. |  |
| 11 | Monitor Integration Run | Once the Integration Run status is Finished, choose the Show Log button in the Extract History section.Check the log records to verify that the output file has been stored on the FTP server and note down the file name from the log. | The Integration Run status is Finished.The output file is stored on the FTP server. |  |
| 12 | Import Extracted Data into BlackLine Cloud | Note Before importing sub-ledger accounts, make sure that you have imported G/L account balances for these sub-ledger accounts. If you have not done this yet, please complete Import G/L Account Balances and Certify Account to import the G/L account balances.Note If an automated FTP interface is created, the file will be imported automatically.To initiate a manual import, navigate to System > Jobs > Import Data.Select Subledgers from the drop down list.Locate your file and choose Import.Note More information about the data import functionality can be found on BlackLine Community:[https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ](https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ) | The file is imported with the following status:Import Status: FinishedSuccessful: Yes |  |
| 13 | Validate Import of AR Sub-Ledger Balances | Navigate to Products > Accounts > View Reconciliations.Make sure that the correct period is selected and that GL Account Reconciliation Templates exist fo the imported sub-ledger accounts.Validate that the entries from the imported file have been added to the list. Verfiy that both sets of data match the output of the Manage Customer Line Items (F0711) app in SAP S/4HANA Cloud Public Edition.Note You can follow the instructions in the table below to generate output in the SAP S/4HANA Cloud Public Edition system. | The Manage Customer Line Items (F0711) app output matches the data in the output file generated by BlackLine Connector.The Manage Customer Line Items (F0711) app output matches the data imported into BlackLine Cloud. |  |
| 14 | Prepare Account Reconciliations for Certification | Log on as a Preparer.Navigate to Products > Accounts > View Reconciliation.Note Make sure that you selected the correct period.Choose Edit to open an imported account.Choose the Add Supporting Item link next to Supporting Items to add a supporting item to zero out the Unidentified Difference and make the reconciliation certifiable.Make the following entries to zero out the Unidentified Difference:Txn. Amount: <amount>Amount: <amount>Alternate Amount: <amount>Rpt. Amount: <amount>Choose List Component from the Item Class section.Make the following entries and choose Save:Description: <description> | The supporting item is created and the account reconciliation is certifiable. |  |
| 15 | Certify Account by Preparer | Choose Certify to start the reconciliation certification process.Once the Certification Statement page is loaded, choose Certify to certify the reconciliation. | The account reconciliation is certified to Prepared status. |  |
| 16 | Certify Account by Approver | Log on as an Approver.Navigate to Products > Accounts > View Reconciliation.Note Make sure that you selected the correct period.Choose the 'Cert' link.Choose Certify to start the reconciliation certification process.Once the Certification Statement page is loaded, choose Certify to certify the reconciliation. | The account has been certified successfully. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP S/4HANA Cloud Public Edition system as a Accounts Receivable Accountant. |  |  |
| 2 | Access App | Open Manage Customer Line Items (F0711). | The Manage Customer Line Items screen displays. |  |
| 3 | Execute App | Make the following entries and choose Go:Company Code : <same value as BlackLine Cloud>Status: <same value as BlackLine Cloud>Open on Key Date: <same value as BlackLine Cloud>Item Type: <same value as BlackLine Cloud>G/ LAccount: <same value as BlackLine Cloud> | The output is generated and ready to be used for comparison against the data generated by BlackLine Connector and data imported into BlackLine Cloud. |  |

### Import G/L Account Multi-Currencies and Certify Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The process extracts G/L Account multi-currencies from the SAP S/4HANA Cloud Public Edition system and imports them into the BlackLine Accounts Reconciliation application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the BlackLine Cloud system as a System Admin. |  |  |
| 2 | Access App | Navigate to the SAP Connector under System > Connectivity Center > SAP Connection. | The SAP Connector page displays. |  |
| 3 | Create New Integration | Choose New Integration to create a new integration. | The New Integration window displays. |  |
| 4 | Create New Integration | In the Type tab, make the following entries:Integration Name: for example, GLaccountMC_test_01Type: G/L Account multi currenciesSelect a valid existing connection profile from the Connection Profile drop down list. |  |  |
| 5 | Create New Integration | On the Segments tab, make the following entries:CompanyCode Segment Inclusions: <company code>GLAccount Segment Inclusions: for example, 19990204-19990250 |  |  |
| 6 | Create New Integration | On the Selection tab, make the following entries:Period Selection: CustomKey Date: <key date>Ledger: 0LGL Account Balance: AmountInGlobalCurrencyGL Reporting Balance: AmountInCompanyCodeCurrencyGL Alternate Balance: AmountInCompanyCodeCurrency |  |  |
| 7 | Create New Integration | On the Schedule tab, make the following entry:Don’t schedule automatically: Selected |  |  |
| 8 | Create New Integration | Choose Create and check if a new entry has been added to the Integration section. | A new integration has been created and added to list of integrations in the Integration section. |  |
| 9 | Validate Integration | Select the integration which you created and choose Validate.The files will be generated and saved on the workstation. | The integration is opened and editable.Once the validation is executed, the files are written to a local machine and the Test Complete message appears. Please check the downloaded files. |  |
| 10 | Run Integration with Scheduler | Choose Run Once to trigger the execution of the newly created integration record.Choose Refresh History in the Extract History section to check if the integration run is scheduled. | The integration run started and a record is available in the Extract History section. |  |
| 11 | Monitor Integration Run | Once the Integration Run status is Finished, choose the Show Log button in the Extract History section.Check the log records to verify that the output file has been stored on the FTP server and note down the file name from the log. | The Integration Run status is Finished.The output file is stored on the FTP server. |  |
| 12 | Import Extracted Data into BlackLine Cloud | Note Before importing sub-ledger accounts, make sure that you have imported G/L account balances for these sub-ledger accounts. If you have not done this yet, please complete Import G/L Account Balances and Certify Account to import the G/L account balances.Note If an automated FTP interface is created, the file will be imported automatically.To initiate a manual import, navigate to System > Jobs > Import Data.Select Multi-Cncy Balances from the drop down list.Locate your file and choose Import.Note More information about the data import functionality can be found on BlackLine Community:[https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ](https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ) | The file is imported with the following status:Import Status: FinishedSuccessful: Yes |  |
| 13 | Validate Import of Accounts | Navigate to Products > Accounts > View Reconciliations.Make sure that the correct period is selected.Validate that the entries from the imported file have been added to the list. Verfiy that both sets of data match the output of the Display G/L Account Balances (F0707A) app in SAP S/4HANA Cloud Public Edition.Note You can follow the instructions in the table below to generate output in the SAP S/4HANA Cloud Public Edition system. | The Display G/L Account Balances (F0707A) app output matches the data in the output file generated by BlackLine Connector.The Display G/L Account Balances (F0707A) app output matches the data imported into BlackLine Cloud. |  |
| 14 | Prepare Account Reconciliations for Certification | Log on as a Preparer.Navigate to Products > Accounts > View Reconciliation.Note Make sure that you selected the correct period.Choose Edit to open an imported account.Choose the Add Supporting Item link next to Supporting Items to add a supporting item to zero out the Unidentified Difference and make the reconciliation certifiable.Make the following entries to zero out the Unidentified Difference:Txn. Amount: <amount>Amount: <amount>Alternate Amount: <amount>Rpt. Amount: <amount>Choose List Component from the Item Class section.Make the following entries and choose Save:Description: <description> | The supporting item is created and the account reconciliation is certifiable. |  |
| 15 | Certify Account by Preparer | Choose Certify to start the reconciliation certification process.Once the Certification Statement page is loaded, choose Certify to certify the reconciliation. | The account reconciliation is certified to Prepared status. |  |
| 16 | Certify Account by Approver | Log on as an Approver.Navigate to Products > Accounts > View Reconciliation.Note Make sure that you selected the correct period.Choose the 'Cert' link.Choose Certify to start the reconciliation certification process.Once the Certification Statement page is loaded, choose Certify to certify the reconciliation. | The account has been certified successfully. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP S/4HANA Cloud Public Edition system as a General Ledger Accountant. |  |  |
| 2 | Access App | Open Display G/L Account Balances (F0707A). | The Display G/L Account Balances screen displays. |  |
| 3 | Execute App | Make the following entries and choose Go:Ledger: <same value as BlackLine Cloud>Company Code : <same value as BlackLine Cloud>G/ LAccount: <same value as BlackLine Cloud>From Period: <same value as BlackLine Cloud>To Period: <same value as BlackLine Cloud>Fiscal Year of Ledger: <same value as BlackLine Cloud> | The output is generated and ready to be used for comparison against the data generated by BlackLine Connector and data imported into BlackLine Cloud. |  |

### Import Account Analysis Data and Certify Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The process extracts G/L Account balances and transaction level data and from the SAP S/4HANA Cloud Public Edition system and imports them into the BlackLine Accounts Reconciliation application.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the BlackLine Cloud system as System Admin. |  |  |
| 2 | Access App | Navigate to the SAP Connector under System > Connectivity Center > SAP Connection. | The SAP Connector page displays. |  |
| 3 | Create New Integration | Choose New Integration to create a new integration. | The New Integration window displays. |  |
| 4 | Create New Integration | In the Type tab, make the following entries:Integration Name: for example, ACCTAcubledgers_test_01Type: Account AnalysisSelect a valid existing connection profile from the Connection Profile drop down list. |  |  |
| 5 | Create New Integration | On the Segments tab, make the following entries:CompanyCode Segment Inclusions: <company code>GLAccount Segment Inclusions: for example, 19990103Profit Ceter Segment Inclusions: for example, YB101, YB102, YB103, YB111 (if applicable) |  |  |
| 6 | Create New Integration | On the Selection tab, make the following entries:Period Selection: CustomKey Date: <key date>Ledger: 0LGL Account Balance: AmountInGlobalCurrencyGL Reporting Balance: AmountInCompanyCodeCurrencyGL Alternate Balance: AmountInCompanyCodeCurrencyBase Date 1: Posting DateBase Date 2: Document DateBase Date 3: Value DateBase Date 4: Due Date |  |  |
| 7 | Create New Integration | On the Schedule tab, make the following entry:Don’t schedule automatically: Selected |  |  |
| 8 | Create New Integration | Choose Create and check if a new entry has been added to the Integration section. | A new integration has been created and added to list of integrations in the Integration section. |  |
| 9 | Validate Integration | Select the integration which you created and choose Validate.The files will be generated and saved on the workstation. | The integration is opened and editable.Once the validation is executed, the files are written to a local machine and the Test Complete message appears. Please check the downloaded files. |  |
| 10 | Run Integration with Scheduler | Choose Run Once to trigger the execution of the newly created integration record.Choose Refresh History in the Extract History section to check if the integration run is scheduled. | The integration run started and a record is available in the Extract History section. |  |
| 11 | Monitor Integration Run | Once the Integration Run status is Finished, choose the Show Log button in the Extract History section.Check the log records to verify that the output file has been stored on the FTP server and note down the file name from the log.Note Account Analysis Integration generates two data files, one for G/L balance data and one for transaction level data. | The Integration Run status is Finished.The output file is stored on the FTP server. |  |
| 12 | Import Extracted Data into BlackLine Cloud | Note If an automated FTP interface is created, the file will be imported automatically.To initiate a manual import, navigate to System > Jobs > Import Data.Select Accounts from the drop down list.Locate your file with G/L account balance data and choose Import .Note More information about the Data Import functionality can be found on BlackLine Community:[https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ](https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ) | The file is imported with the following status:Import Status: FinishedSuccessful: Yes |  |
| 13 | Validate Import of G/L Account Balances | Navigate to Products > Accounts > View Reconciliations.Note Make sure that the correct period is selected.Validate that the entries from the imported file have been added to the list. Verfiy that both sets of data match the output of the Display G/L Account Balances (F0707A) app in SAP S/4HANA Cloud Public Edition. | The Display G/L Account Balances (F0707A) app output matches the data in the output file generated by BlackLine Connector.The Display G/L Account Balances (F0707A) app output matches the data imported into BlackLine Cloud. |  |
| 14 | Set Reconciliation Template Type | Navigate to Products > Accounts > View Reconciliation.Choose Edit to open an imported account.In the Template Settings tab, make the following entries and choose Done:Reconciliation Template: Account Analysis | The Reconciliation Template is set to Account Analysis. |  |
| 15 | Import Extracted Data into BlackLine Cloud | Note Use the existing Import Definition<Acc_Analysis_import> and Data Source<Acc_Analysis_source> that were configured in cooperation with your BlackLine implementation consultant (or BlackLine partner) during the Account Analysis implementation process.Note If an automated FTP interface is created, the file will be imported automatically.To initiate a manual import, navigate to System > Jobs > Import Data.Make the following entries:Import type: <Acc_Analysis_import>Browse to your file with transactions and choose Import.Note More information about the data import functionality can be found on BlackLine Community:[https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ](https://myblackline.force.com/BlackLineCommunity/s/article/Data-Import-FAQ) | The file is imported with the following status:Import Status: FinishedSuccessful: Yes |  |
| 16 | Validate Import of Transactions | Navigate to Products > Match > Data sources.Select the Data Source<Acc_Analysis_source> and validate that the entries from the imported file have been added to the list. Verfiy that both sets of data match the output of the Display Line Items in General Ledger (F2217) app in the SAP S/4HANA Cloud Public Edition system.Note You can follow the instructions in the table below to generate output in the SAP S/4HANA Cloud Public Edition system. | The Display Line Items in General Ledger (F2217) app output matches the data in the output file generated by BlackLine Connector.The Display Line Items in General Ledger (F2217) app output matches the data imported into BlackLine Cloud. |  |
| 17 | Migrate Transactions to Account Analysis Template | Navigate to System > Jobs > Import Definitions.Choose Run Nowfor the existing Import Definition<Acc_Analysis_import>.To monitor the import status, navigate to System > Jobs > Job Status. | The file is imported with the following status:Import Status: FinishedSuccessful: Yes |  |
| 18 | Validate Migration of Transactions | Navigate to Products > Accounts > View Reconciliations.Make sure that the correct period is selected.Filter for the imported accounts and verify that the transactions were successfully migrated. | The transactions are successfully loaded into Account Analysis Templates. |  |
| 19 | Certify Account by Preparer | Log on as a Preparer.Navigate to Products > Accounts > View Reconciliation.Note Make sure that you selected the correct period.Choose Edit to open an imported account.Select all transactions on the Unanalyzed grid.Choose Take Action > Bulk Update.Assign transactions to the category and subcategory.Open the panel on the right and choose Certify. | The account reconciliation is certified to Prepared status. |  |
| 20 | Certify Account by Approver | Log on as an Approver.Navigate to Products > Accounts > View Reconciliation.Note Make sure that you selected the correct period.Choose the 'Cert' link.Choose Certify to start the reconciliation certification process.Once the Certification Statement page is loaded, choose Certify to certify the reconciliation. | The account has been certified successfully. |  |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment. |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP S/4HANA Cloud Public Edition system General Ledger Accountant. |  |  |
| 2 | Access App | Open Display G/L Account Balances (F0707A). | The Display G/L Account Balances screen displays. |  |
| 3 | Execute App | Make the following entries and choose Go:Ledger: <same value as BlackLine Cloud>Company Code : <same value as BlackLine Cloud>G/ LAccount: <same value as BlackLine Cloud>From Period: <same value as BlackLine Cloud>To Period: <same value as BlackLine Cloud>Fiscal Year of Ledger: <same value as BlackLine Cloud> | Th output is generated and ready to be used for comparison against the data generated by BlackLine Connector and data imported into BlackLine Cloud. |  |
| 4 | Access App | Open Display Line Items in General Ledger (F2217). | The Display Line Items in General Ledger screen displays. |  |
| 5 | Execute App | Make the following entries and choose Go:Company Code: <same value as BlackLine Cloud>G/L Account: <same value as BlackLine Cloud>Posting Date: <same value as BlackLine Cloud>Fiscal Year: <same value as BlackLine Cloud> | The output is generated and ready to be used for comparison against the data generated by BlackLine Connector and data imported into BlackLine Cloud. |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-transaction-matching-sap-solution-extensions-by-blackline]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6IL_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 53,463 chars in the whole document
