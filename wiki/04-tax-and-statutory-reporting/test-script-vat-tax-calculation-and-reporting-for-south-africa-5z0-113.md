---
id: 04-tax-and-statutory-reporting/test-script-vat-tax-calculation-and-reporting-for-south-africa-5z0-113
title: "Test Script: VAT Tax Calculation and Reporting for South Africa (5Z0) (5Z0_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5Z0: South Africa VAT calculation and reporting, covering prerequisites, journal entries, advance return and electronic tax return."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/south-africa-vat]
aliases: [5Z0_S4CLD2608_BPD_EN_XX]
keywords: [South Africa VAT Calculation and Reporting, south africa vat, tax code assignment, general journal entries, advance return sales/purchase tax, electronic tax return, registration for indirect taxation abroad, default tax rate per contract type, business roles, demo data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z0_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1131
topic: 04-tax-and-statutory-reporting/south-africa-vat
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: VAT Tax Calculation and Reporting for South Africa (5Z0) (5Z0_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z0_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **South Africa VAT Calculation and Reporting** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | VAT Tax Calculation and Reporting for South Africa (5Z0) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232825398)

[2 Prerequisites 3](#_Toc232825399)

[2.1 System Access 3](#_Toc232825400)

[2.2 Roles 3](#_Toc232825401)

[2.3 Master Data and Organizational Data 3](#_Toc232825402)

[2.4 Preliminary Steps 4](#_Toc232825403)

[2.4.1 Default Value for Tax Rate per Contract Type (Optional) 4](#_Toc232825404)

[2.4.2 Assign Tax Codes 6](#_Toc232825405)

[2.4.3 Assign Tax Code (for FI Document) 8](#_Toc232825406)

[2.4.4 Activate Registration for Indirect Taxation Abroad (Optional) 10](#_Toc232825407)

[3 Overview Table 11](#_Toc232825408)

[4 Test Procedures 12](#_Toc232825409)

[4.1 Post General Journal Entries 12](#_Toc232825410)

[4.2 Create Advanced Return on Sales/Purchase Tax 15](#_Toc232825411)

[4.3 Prepare Electronic Tax Return 17](#_Toc232825412)

## Purpose

Overview

This scope item provides information on calculating and reporting taxes in South Africa. This covers South Africa-based companies and foreign companies that do business in South Africa.

This scope item is required for South Africa VAT reporting in two situations: you have a company code within South Africa, or you have a company code outside of South Africa with tax registration in South Africa.

For more information, we recommend that you check the country roadmap for Registration for Indirect Taxation Abroad (RITA). Verify that the company code country and country of tax registration support the RITA solution.

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

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

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | <Company Code> |  |  |
| Cost Center | For example, xx101101 (where xx is the first two digits of your company code) |  |  |

### Preliminary Steps

#### Default Value for Tax Rate per Contract Type (Optional)

Purpose

For each contract type, you specify here which tax group and which tax type is proposed by the system when a contract is created. For contract types that are not relevant for tax (internal contracts, G/L account contracts), you can also specify that these contract types are treated as tax exempt.

If you set the Tax Exempt indicator, then the tax type and tax group are not entered during the processing of contracts with this contract type. In that case, leave the Tax Type and Tax Group fields blank in this view, otherwise the cash flow generation would incorrectly use the tax type and tax group entered here.

|  |
| --- |
| Note This activity is only applicable when at least one of Contract and Lease Management scope items (1T6, 21P, 21Q, 21R, 2SB, 2SA, 23N, 34O, 7EZ, 7G4 or 7G5) is activated. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: FinanceSub Application Area: Contract and Lease Management |  |  |
| 5 | Open | Open Accounting Integration. |  |  |
| 6 | Select Configuration Step | For the Default Value for Tax Rate per Contract Type step, choose Configure. | The "Default Value for Tax Rate per Contract Type": Change screen displays. |  |
| 7 | Assign Tax Type and Tax Group | Make the following entries and choose Save:TType: <Tax Type>Default Tax Group : <Tax Group>Note To change the Default Tax Group, choose the Display/Edit button, then select the magnifying glass in the field you wish to change. | The Tax Type and Tax Group are saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Default Value for Tax Rate per Contract Type.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Default Value for Tax Rate per Contract Type screen is displayed. |  |
| 3 | Assign Tax Type and Tax Group | Make the following entries and choose Save:TType: <Tax Type>Default Tax Group : <Tax Group>Note To change the Default Tax Group, choose the Display/Edit button, then select the magnifying glass in the field you wish to change. | The Tax Type and Tax Group are saved. |  |

#### Assign Tax Codes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You assign a tax code in your accounting system to the tax types and tax groups that you defined in Flexible Real Estate Management. The tax code is needed for calculating tax on sales/purchases. The tax code assignment is both country/region-dependent and time-dependent.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: FinanceSub Application Area: Contract and Lease Management |  |  |
| 5 | Open | Open Accounting Integration. |  |  |
| 6 | Select Configuration Step | For the Tax Code Assignment step, choose Configure. | The Change View "Tax Code Assignment": Overview screen displays. |  |
| 7 | Assign Tax Codes | Make the following entries and choose Save:C/RTtypTaxGroupValid FromTax CodeZAY1Y-FULL01.01.1900W1ZAY1Y-NONE01.01.1900V5ZAY2Y-FULL01.01.1900B1ZAY2Y-NONE01.01.1900A5Note To change the Default Tax Group, choose Display/Edit, then select the magnifying glass in the field you wish to change. | The tax code assignments are saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app and search for the following activity: Assign Tax Codes.Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Assign Tax Codes | Make the following entries and choose Save:C/RTtypTaxGroupValid FromTax CodeZAY1Y-FULL01.01.1900W1ZAY1Y-NONE01.01.1900V5ZAY2Y-FULL01.01.1900B1ZAY2Y-NONE01.01.1900A5Note To change the Default Tax Group, choose Display/Edit, then select the magnifying glass in the field you wish to change. | The tax code assignments are saved. |  |

#### Assign Tax Code (for FI Document)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You assign a tax code in your accounting system to the tax types and tax groups that you defined in Flexible Real Estate Management. The tax code is needed for calculating tax on sales/purchases. The tax code assignment is both country/region-dependent and time-dependent.

You must make this assignment in order for FI documents to be read correctly in RE. This assignment is relevant for service charge settlement and input tax distribution.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Access Configuration | Open Configure Your Solution. | The Configure Your Solution: Realize Phase screen displays. |  |
| 4 | Access Configuration | Make the following entries:Application Area: FinanceSub Application Area: Contract and Lease Management |  |  |
| 5 | Open | Open Accounting Integration. |  |  |
| 6 | Select Configuration Step | For the Assign Tax Code (for FI Document) step, choose Configure. | The Change View "Assignment of Tax Code to RE Tax Type and Group": Overview screen displays. |  |
| 7 | Assign Tax Types and Tax Groups | Make the following entries and choose Save:C/RTax CodeValid FromValid ToTtypTaxGroupZAB101.01.1900Y2Y-FULLZAA501.01.1900Y2Y-NONEZAW101.01.1900Y1Y-FULLZAV501.01.1900Y1Y-NONE | The tax code assignments are saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Access Configuration | Go to the Business Processes Configuration app and search for the following activity: Assign Tax Code (for FI Document).Choose the line item in the search result to see more details about this configuration activity.Choose the Go to Activity button to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Assign Tax Types and Tax Groups | Make the following entries and choose Save:C/RTax CodeValid FromValid ToTtypTaxGroupZAB101.01.1900Y2Y-FULLZAA501.01.1900Y2Y-NONEZAW101.01.1900Y1Y-FULLZAV501.01.1900Y1Y-NONE | The tax code assignments are saved. |  |

#### Activate Registration for Indirect Taxation Abroad (Optional)

Purpose

Companies operating in multiple countries must satisfy the tax and reporting regulations of the countries in which they do business. Under some circumstances, you’re permitted to register legal entities for indirect taxation abroad without having to create a company code for that country. Registration for Indirect Taxation Abroad (RITA) allows you to maintain a tax registration country that is different from the company code country This registration helps you link taxable transactions in foreign countries for indirect tax reporting (such as the EU Tax Return, Intrastat, or EC Sales List) and tax payments.

|  |
| --- |
| Note You can't use RITA where, for instance, you maintain an establishment in a foreign country and are required to create a company code for that permanent presence. You also can't use it in any instance when you're required to create a company code. Neither of these cautions refer to the default company code when you activate SAP S/4HANA Cloud Public Edition. It's your responsibility to verify whether your business activities are considered as a permanent establishment under the law of the respective country. In this case, a company code would be required. |

Procedure

A full discussion of setting up RITA is outside of the scope of this test script. For more information, see the topics under [Registration for Indirect Taxation Abroad (RITA) on the SAP Help Portal](https://help.sap.com/viewer/0fa84c9d9c634132b7c4abb9ffdd8f06/latest/en-US/baee0f4d00de4f1693be3f57fd49685a.html).

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Post General Journal Entries](#unique_11) [page ] 12 | General Ledger Accountant | Post General Journal Entries (F0718) | The General Ledger journal entry is posted. The system has automatically added the Input tax amount. |
| [Create Advanced Return on Sales/Purchase Tax](#unique_12) [page ] 15 | General Ledger Accountant | Create Advance Return on Sales/Purchase Tax (S_ALR_87012357) | The report creates the advance return for tax on sales and purchases. |
| [Prepare Electronic Tax Return](#unique_13) [page ] 17 | General Ledger Accountant | Prepare Electronic Tax Return (FOTV) | The administrative report is created. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Post General Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive G/L journal entries that must be posted manually in the SAP system.

Prerequisite

A global chart of accounts is assigned to all company codes. If a company code has an assigned local chart of accounts, you can use alternative (local) accounts in journal entries. Unless there is a special note, we always use global accounts in the test scripts. To make sure that you have the correct setting, open the Edit Options for Journal Entries - My Settings (F2130) app and deselect the Use Alternative Acct. checkbox.

|  |
| --- |
| Note You can execute the test steps for the following scenarios:Without Registration for Indirect Taxation Abroad (RITA)You execute the test steps for company code 6410.With Registration for Indirect Taxation Abroad (RITA)If you have activated RITA in your system, the field Tax Ctry/Reg. will be visible.You execute the test steps for your company code and tax reporting country/region ZA. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries Header Data | In the Header pane, make the following entries:Journal Entry Date: <Today's Date>Posting Date: <Today's Date>Period: <Period>Journal Entry Type: SACompany Code: <Company Code>Document Currency: <Currency>Ledger Group: <Empty> |  |  |
| 4 | Enter Line Item Data | In the Line Items pane, make the following entries:Line Items - Line 1:G/L Account: for example, 63002000Debit: <Amount>Tax Code: <Tax Code>Tax Ctry/Reg.: ZANote This field is only visible if you have activated RITA.Tax Date: for example, <Today's Date>Cost Center: <Cost Center>Line Items - Line 2:G/L Account: for example, 10010000Credit: <Amount>. |  |  |
| 5 | Post | Choose Post. | The journal entry is posted. The system automatically adds the input tax amount. |  |
| 6 | Restart the SAP Fiori App | Go back to the SAP Fiori launchpad.Open Post General Journal Entries (F0718). |  |  |
| 7 | Start Journal Entry Excel Upload | Choose Upload New Entry at the bottom of the screen. | The Upload General Journal Entries (F2548) view displays. |  |
| 8 | Download Template | Choose Download Template.Make the following entries and choose Download.Template Language for example, EnglishFormat: Spreadsheet (*.xlsx) | The Excel template file is downloaded. |  |
| 9 | Prepare the Template | Make the following entries in the template file for all G/L account journal entries to be posted and save it locally:Header:Company Code: <Company Code>Journal Entry Type: <Journal Entry Type>, for example, SAJournal Entry Date: <Today's Date>Posting Date: <Today's Date>Transaction Currency: for example, <Currency>Line Items - Line 1:Company Code: <Company Code>G/L Account: for example, 63003000Debit: <Amount>Tax Code: <Tax Code>Tax Ctry/Reg.: ZANote You can disregard this field if you have not activated RITA.Tax Date: for example, <Today's Date>Cost Center: <Cost Center>Line Items - Line 2:Company Code: <Company Code>G/L Account: for example, 10010000Credit: <Amount> |  |  |
| 10 | Upload Excel File | Choose the Browse button at top of the screen, select the prepared Excel file, and choose Open. | The Excel file is uploaded and you can see new held journal entries in the worklist.If the uploaded file contains errors, choose Show log to view details. |  |
| 11 | Post | Select the held journal entries and choose Post. | The journal entries are posted. |  |

### Create Advanced Return on Sales/Purchase Tax

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Posting via report (RFUMSV00): (as recommended by SAP)

The report creates the advance return for tax on sales and purchases and, if required, a batch input session for making an automatic transfer posting for the tax payable.

When the system creates a batch input session for the tax payable transfer posting, a document is prepared for each company code selected. In this document, one item for posting to the tax account and one item for posting to the tax payable account is created for each tax account.

If required, the report starts filling in the form for advance return for tax on sales and purchases (function not covered/delta Customizing). It provides the tax balances for each company code, the tax on sales/purchases code, transaction key, total/debit or credit indicators, and the selected period in tabular form. The subsequent print report uses these tables to determine the data required for the printout.

You can set the output lists to suit your requirements. You can use the ABAP List Viewer function to arrange the lists accordingly.

|  |
| --- |
| Note If necessary, changes to the assignment of tax groups to company codes can be carried out with the Assign Company Codes to Tax on Sales/Purchases Groups configuration step.Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Configure Your Solution:Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.Open Manage Your Solution (F1241).Choose Configure Your Solution.On the Configure Your Solution screen, search for the following configuration step: Assign Company Codes to Tax on Sales/Purchases Groups. Choose Go.In the search result, select the configuration activity and go to the next screen.On the Assign Company Codes to Tax on Sales/Purchases Groups screen, go to the configuration step Assign Company Codes to Tax on Sales/Purchases Groups and choose Configure.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Company Codes to Tax on Sales/Purchases Groups.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |

|  |
| --- |
| Note You can execute the test steps for the following scenarios:Without Registration for Indirect Taxation Abroad (RITA)You execute the test steps for your tax group or company code 6410.With Registration for Indirect Taxation Abroad (RITA)If you have activated RITA in your system, the field Tax Reporting Country/Region will be visible.You execute the test steps for your company code and tax reporting country/region ZA. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Create Advance Return on Sales/Purchase Tax (S_ALR_87012357). | The Advance Return for Tax on Sales/Purchases screen displays. |  |
| 3 | Maintain Selections | Make the following entries:Fiscal Year: <Current Fiscal Year>Posting Date: <Date Range of One Month> |  |  |
| 4 | Maintain Further Selections | Choose the Further Selections button and make the following entries:Taxes on sales/purchases group: <Tax Group>Note If you do not have a tax group assigned to your company code, enter your company code in the Company Code field.Tax Reporting Country/Region: ZANote This field is only visible if you have activated RITA. |  |  |
| 5 | Tax Payable Posting: Batch Input Session Required | Choose Tax Payable Posting.Make the following entries:Batch Input Session Required: SelectedPostings Document type: SAPosting Date: <Today's Date>Due Date of the Tax Payable: <Date After Fiscal Period End>Folder Name: RFUMSV00Hold processed session: SelectedNote To process the session with Display errors only, you can use the Batch Input Sessions in My Area (SM35SA) or My Batch Input Sessions (SM35SM) apps. |  |  |
| 6 | Posting Parameters | Choose Posting parameters.Make the following entries and choose Run:Update documents: Update run: SelectedElectronic Advance Return: SelectedReporting Year: <Fiscal Year>Reporting Period: <Month to Create Tax Return>Prepare Printing of Forms: SelectedProgram Run Date: <Today's Date>Identification: GAB01 | The system creates a list in both the test run and update run. |  |

### Prepare Electronic Tax Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the administration report for the electronic data transmission to the authorities.

Prerequisite

You successfully executed the Create Advance Return on Sales/Purchase Tax (S_ALR_87012357) app with Electronic Advance Return selected.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Prepare Electronic Tax Return (FOTV). |  |  |
| 3 | Enter Data | Make the following entries and choose Run:Dominant Enterprise/Comp. Code: <Company Code>Return Type: 0001Reporting Country/Region: <XX>Reporting Period: for example, 1Rep. Year: for example, <Current Year> | The Administration Report Electronic Data Transmission to Authorities view displays. The report is generated. |  |
| 4 | Download File | After running the report, choose Menu > SAP GUI HTML File Browser . | The SAP GUI for HTML File Browser dialog box displays. |  |
| 5 | Export File | A file with the AWVZ4 prefix displays in the Z:\ directory. To download the file to your PC, select the file and choose Export. | The reporting data is downloaded to your PC. |  |

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
- related-to :: [[04-tax-and-statutory-reporting/compliance-formats-support-preparation-for-south-africa-5z5-test-scrip]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z0_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 31,942 chars in the whole document
