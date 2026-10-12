---
id: 04-tax-and-statutory-reporting/test-script-compliance-formats-support-preparation-for-germany-5o6-sap
title: "Test Script: Compliance Formats – Support Preparation for Germany (5O6), SAP S/4HANA Cloud Public Edition (5O6_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud test script for scope item 5O6: German statutory reporting (Audit Z3, EC Sales List, Advance VAT Return, extensions, euBP) via Advanced Compliance Reporting."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/germany-vat-and-intrastat]
aliases: [5O6_S4CLD2608_BPD_EN_XX]
keywords: [Germany VAT Returns and Intrastat, advanced compliance reporting, germany statutory reporting, advance vat return, ec sales list, audit z3 data extraction, electronic tax audit euBP, permanent vat extension, special advance payment, post tax payable]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5O6_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1110
topic: 04-tax-and-statutory-reporting/germany-vat-and-intrastat
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Compliance Formats – Support Preparation for Germany (5O6), SAP S/4HANA Cloud Public Edition (5O6_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5O6_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Germany VAT Returns and Intrastat** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Compliance Formats – Support Preparation for Germany (5O6) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232824879)

[2 Prerequisites 4](#_Toc232824880)

[2.1 System Access 4](#_Toc232824881)

[2.2 Roles 4](#_Toc232824882)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232824883)

[2.4 Business Conditions 6](#_Toc232824884)

[2.5 Preliminary Steps 6](#_Toc232824885)

[2.5.1 Assign Company Code 6](#_Toc232824886)

[2.5.2 Activate Registration for Indirect Taxation Abroad 8](#_Toc232824887)

[2.5.2.1 Activate Registration for Indirect Taxation Abroad (Optional) 8](#_Toc232824888)

[3 Overview Table 10](#_Toc232824889)

[4 Test Procedures 11](#_Toc232824890)

[4.1 Manage Document and Reporting 11](#_Toc232824891)

[4.2 Run Statutory Report - Audit 12](#_Toc232824892)

[4.3 Run Statutory Reports - EC Sales List 15](#_Toc232824893)

[4.4 Run Statutory Reports - Advanced VAT Return 16](#_Toc232824894)

[4.4.1 Advance VAT Return 16](#_Toc232824895)

[4.4.2 Post Tax Payable (Optional) 18](#_Toc232824896)

[4.4.3 Application for Permanent Extension (Dauerfristverlängerung) (Optional) 20](#_Toc232824897)

[4.4.4 Registration of Special Advance Payment (Sondervorauszahlung)(Optional) 22](#_Toc232824898)

[4.5 Electronically Supported Tax Audit euBP 24](#_Toc232824899)

[5 Appendix 28](#_Toc232824900)

[5.1 50A Withholding Tax Report (Optional) 28](#_Toc232824901)

## Purpose

Overview

SAP S/4HANA for advanced compliance reporting is a global legal reporting platform that caters to companies’ indirect tax reporting requirements. This solution enables the end-to-end process of legal reporting including multiple activities that may be necessary to complete the legal reporting. The solution offers a unified and harmonized user experience across countries/regions and reports, enabling a simplified view of the reporting status to the business users and the company's head of tax and compliance. It also provides a design environment to easily create and extend additional report requirements.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

Additional Information on the SAP Help Portal

For additional information, including descriptions of features for Advanced Compliance Reporting, visit the SAP Help Portal ([https://help.sap.com](https://help.sap.com)). On the initial page, enter: Advance Compliance Reporting in the Search field. The results provide additional documentation details about Advanced Compliance Reporting.

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

Table 1: Roles

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant for Germany | SAP_BR_GL_ACCOUNTANT_DE | General Ledger / General Ledger | SAP_FIN_SPT_GL_ACCOUNTING_GLO_PC / SAP_FIN_SPT_GL_ACCOUNTING_GLO_DE_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Package, you can use the following Package scenario data: Accounting.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 1010 |  |  |
| Controlling Area | A000 |  |  |
| Chart of Accounts | YCOA |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNH | Create Profit Center - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Must be run before this test script. |
| J59 - Accounts Receivable | Must be run before this test script.Ensure that invoices for vendors and payments for the invoices are created. |
| J60 - Accounts Payable | Must be run before this test script.Ensure that invoices for vendors and payments for the invoices are created. |
| 55U - VAT Tax Calculation and Reporting for Germany | Scope item is activated. |

### Preliminary Steps

#### Assign Company Code

Purpose

In this activity, you assign a company code to your ACR reports.

Prerequisite

Company code has already been created.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Statutory Reporting

1. For the row with Item Name of Basic Settings, choose Details (>).
2. For the Setting Up Your Statutory Reporting row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Setting Up Your Statutory Reporting.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select | Select your reporting entity, for example:Reporting entity: DE_VAT_ENT |  |  |
| 2 | Validity | In the Dialog Structure pane, double-click Set Validity of Organization Unit and choose a Valid From date.Note If no date exists, a new Valid From date can be entered by choosing New Entries and entering the date. | The Change View "Set Validity of Organization Unit ": Overview view is displayed. |  |
| 3 | Assign | In the Dialog Structure pane, double-click Assign Org. Units to a Reporting Entity and enter the following:Organization Unit: COMPANYCODEVALUE: <your COMPANY CODE>Leading: Selected (there can only be one leading company code) |  |  |
| 4 | Save | Choose Save and then Exit. | The company code is assigned and saved. |  |

#### Activate Registration for Indirect Taxation Abroad

Purpose

For global Advance Compliance Reporting scope items (such as Compliance Formats – Support Preparation for Belgium (5P9) or Compliance Formats – Support Preparation for Germany (5O6)), you must activate Registration for Indirect Taxation Abroad (RITA).

If the Compliance Formats – Support Preparation (1J2) scope item is activated for your country and is to be used in conjunction with another Advance Compliance Reporting scope item (such as (such as Compliance Formats – Support Preparation for Belgium (5P9) or Compliance Formats – Support Preparation for Germany (5O6)), the activation of RITA is required. Activating reports from different countries requires RITA functionality to allow them to work properly.

The activation of RITA is only optional if the Compliance Formats – Support Preparation (1J2) scope item is activated and used alone, not in conjucntion with another Advance Compliance Reporting scope item.

The following reports are RITA-enabled:

- EC Sales List
- Advance VAT Return

##### Activate Registration for Indirect Taxation Abroad (Optional)

Purpose

Companies that operate in multiple countries or regions need to comply with the tax and reporting regulations of each country/region they do business in. In some cases, you can register legal entities for indirect taxation abroad without having to create a separate company code for each country or region. Registration for Indirect Taxation Abroad (RITA) lets you maintain a tax registration country or region that's different from your company code’s country or region. This registration helps you link taxable transactions in foreign countries or regions for indirect tax reporting (like the EU Tax Return, Intrastat, or EC Sales List) and tax payments.

Currently, you can use RITA in Germany, Austria, Czechia, Belgium, Finland, France, the Netherlands, Ireland, Spain, Italy, the United Kingdom, South Africa, Switzerland, and Sweden. For example, companies in Germany can register the Netherlands as a tax registration country/region, and vice versa.

|  |
| --- |
| Note You can't use RITA where, for instance, you maintain an establishment in a foreign country/region and are required to create a company code for that permanent presence. You also can't use it in any instance when you're required to create a company code. Neither of these cautions refer to the default company code when you activate SAP S/4HANA Cloud Public Edition. It's your responsibility to verify whether your business activities are considered as a permanent establishment under the law of the respective country/region. In this case, a company code would be required. |

Procedure

A full discussion of setting up RITA is outside of the scope of this test script. For more information, see the topics under [Registration for Indirect Taxation Abroad (RITA) on the SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/baee0f4d00de4f1693be3f57fd49685a.html).

## Overview Table

The scope items consist of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Document and Reporting](#unique_11) [page ] 11 | General Ledger Accountant for Germany | Manage Document and Reporting Compliance (F5218) | You get an overview of the overall status, due dates, and pending activities of periodic reports. |
| [Run Statutory Report - Audit](#unique_12) [page ] 12 | General Ledger Accountant for Germany | Run Statutory Reports (F1515) | Report and file generate. |
| [Run Statutory Reports - EC Sales List](#unique_13) [page ] 15 | General Ledger Accountant for Germany | Run Statutory Reports - Germany Tax Reporting (F1515_DE_2) | Report and file generate. |
| Advanced VAT Return |  |  |  |
| [Advance VAT Return](#unique_14) [page ] 16 | General Ledger Accountant for Germany | Run Statutory Reports - Germany Tax Reporting (F1515_DE_2) | Report and file generate. |
| [Post Tax Payable (Optional)](#unique_15) [page ] 18 | General Ledger Accountant for Germany | Run Statutory Reports - Germany Tax Reporting (F1515_DE_2) | Report and file generate. |
| [Application for Permanent Extension (Dauerfristverlängerung) (Optional)](#unique_16) [page ] 20 | General Ledger Accountant for Germany | Run Statutory Reports (F1515) | Report and file generate. |
| [Registration of Special Advance Payment (Sondervorauszahlung)(Optional)](#unique_17) [page ] 22 | General Ledger Accountant for Germany | Run Statutory Reports - Germany Tax Reporting (F1515_DE_2) | Report and file generate. |
| [Electronically Supported Tax Audit euBP](#unique_18) [page ] 24 | General Ledger Accountant for Germany or Tax Accountant - Legal Reporting | Run Statutory Reports - Germany euBP Reporting (F1515_DE_4) | You submitted the euBP report. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage Document and Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use this app to get an overview of the overall status, due dates, and pending activities of periodic reports. You can also further navigate to the corresponding tasks and documents to process the details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Germany .Or as a Tax Accountant - Legal Reporting. |  |  |
| 2 | Open the SAP Fiori App | Open Manage Document and Reporting Compliance (F5218). |  |  |
| 3 | Selection | In the Filters section, enter the following:Country/Region: Any country(ies)Report Name: Any report(s)Report Due Date: Date rangeIf needed, use any other available filter. | Based on your filtering criteria, progress bars of selected reports display in section Reporting Progress and a list of report will display in section Reports – Immediate Attention Required. |  |
| 4 | Group / Sort | In section Reporting Progress, grouping display can be changed by choosing any other available option in the drill-down menu.In section Reports – Immediate Attention Required, sorting display can be changed by choosing any other available option in the drill-down menu. |  |  |
| 5 | Size | Size of each section box can be changed by dragging any of the border or corner boxes. |  |  |
| 6 | Navigation | The following selections will open app Run Statutory Reports (F1515):Choose the header of either section Reporting Progress or Reports – Immediate Attention Required and all reports based on the filtering criteria will be chosen.Choose a bar from the graphic displayed in Reporting Progress and it will choose the reports belonging to the specific bar.Choose a specific report by selecting it from section Reports – Immediate Attention Required. | The app Run Statutory Reports (F1515) is executed and opens in a new window with the reports according to your selection. |  |
| 7 | Report Execution | To generate a report, please follow the instructions in the following chapters. |  |  |

### Run Statutory Report - Audit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the statutory report for tax auditing purposes.

Prerequisite

You've executed the Business Conditions chapter.

Journal entries are posted.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as General Ledger Accountant for Germany or as a Tax Accountant - Legal Reporting. | . |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports (F1515). | The Run Statutory Reports view displays. |  |
| 3 | Enter Criteria | Make the following entries and choose Go:Submission Due Date: Leave blank or enter a <Date range>Report Name: DE_AUDIT_Z3 |  |  |
| 4 | Select Report to Submit | To create and choose a report to submit, choose Create. |  |  |
| 5 | Select Report to Submit | Select Report Name DE_AUDIT_Z3, make the following entries, and choose OK:Due Date: <Date>Reporting Period: <Date range>Reporting Year: <Year> |  |  |
| 6 | Select Report to Submit | Select the report you created with the following status:Reporting Status: Due LaterNote If the report to submit already exists in the Statutory Reports section, select it. | The relevant statutory report is displayed for selection in the Run Statutory Reports section. |  |
| 7 | New Run | Choose New Run.Caution If several reports exist in Activity Name column, select German Z3 Data Extraction Files (SAP Audit Format), and choose New Run in the new screen. | A dialog box displays. |  |
| 8 | Criteria | In the Standard section make the following entries and choose Run:Documents for Generation: <select documents via the dropdown>Company Code: 1010Ledger: <any>, for example, 0LFiscal Year: <Year>From Period: <any>, for example, 01To Period: <any>, for example, 12Run Options section:Start a Short Run Now (Less than 3 Minutes): SelectedTip When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. | In the Generated section, the report displays (verify the date and time). |  |
| 9 | Report | If the new report has an In Process status, choose the Refresh button from the top right of the view to update the status to Generated Successfully. |  |  |
| 10 | Report | Verify the date and time in the Action Taken On column, to ensure that you select the correct report. |  |  |
| 11 | Report | On the Generated tab, select the new report. | A report details view displays. |  |
| 12 | Navigation | Several sections are available to analyze your generated report:Legal ReportingSelection CriteriaLogAttachments |  |  |
| 13 | Download | Select the checkbox next to the document name and choose Download. |  |  |
| 14 | Attachments | In the Attachments section, drag and drop a file from your computer, or use the Upload button to select a location and file to attach. |  |  |

### Run Statutory Reports - EC Sales List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The tax authorities use the EC Sales List to provide information for other EU member states. All companies must send an EC Sales List to the tax authorities responsible. The EC Sales List provides information on the tax-exempt goods deliveries and movements to registered companies conducted within the EU during the reporting period.

Prerequisite

A foreign customer must exist.

You must post a credit or debit position (such as an invoice) to a foreign Customer within the EU with an EU relevant tax code (for example, A6 or A7).

The foreign customer within the EU must have the VAT registration number for their country stored in the master data record. If the revenue account for the account receivables posting is only a P&L account in FI, no additional co-object is required. Otherwise, if the revenue account is a primary cost or a revenue element, an additional co-object is required, such as a profitability segment or an internal order (or WBS element) with revenue postings allowed.

If you cannot find a proper existing customer, you must create a new foreign customer within EU with a VAT registration number first.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Germany or as a Tax Accountant - Legal Reporting. |  |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports - Germany Tax Reporting (F1515_DE_2). | The app opens. |  |
| 3 | Enter Criteria | Make the following entries and choose Go:Submission Due Date: <leave blank or enter a date range>Report Name: DE_ECSL_DCL |  |  |
| 4 | Select Report | Double-click an incomplete report. | The report details view displays. |  |
| 5 | New Run | In the Activities section, select Prepare EC Sales List and choose New Run. | The Selection Criteria for Germany EC Sales List dialog box is displayed. |  |
| 6 | Enter Details | Make the following entries and choose Run:Company Code: 1010Reporting Date: <date range>Run Options: Start a Short Run Now (Less than 3 Minutes) | In the Generated > Runs section, the report is displayed as In Process. |  |
| 7 | Details | In the Runs section, select the recently generated report and double-click the report. | The run details view displays. |  |
| 8 | Download | For the document, select the checkbox to the left and choose Download (above the pane). | The document is downloaded in CSV format. |  |

### Run Statutory Reports - Advanced VAT Return

The following steps cover the Statutory reports for Advanced VAT Return for Germany.

#### Advance VAT Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity deals with Statutory Reporting Framework Reports. These steps create the advance return for tax on sales and purchases.

Prerequisite

The report can only be executed when data is available.

|  |
| --- |
| Note If you want to submit a report, you must configure electronic communication with the government via the SAP Localization Hub, statutory reporting service. For more information about this service, go to the [Help Portal](https://help.sap.com/viewer/4de200b26d5d42bbacae69c6bf6b9923/latest/en-US/31d43577cebc45b991c74e854ef86573.html). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Germany or as a Tax Accountant - Legal Reporting. |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports - Germany Tax Reporting (F1515_DE_2). | The app opens. |  |
| 3 | Enter Details | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name: DE_VAT_ADV_RTN | A list of reports displays. |  |
| 4 | Select Report to Submit | In the Activities section, select Prepare Advance VAT Return, choose the arrow button at the right of the row. | The Germany Advance VAT Return view for the report displays. |  |
| 5 | New Run | Choose New Run. | A selection criteria dialog box displays. |  |
| 6 | Selection Criteria | Make the following entries and choose Run:Company Code: 1010Reporting Date: <period based on your selection>Run Options: Start a Short Run Now (Less than 3 Minutes)Note When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. | A Report started notification displays. The new report is generated and a new row displays in the Generated section. |  |
| 7 | Refresh Report | If the new report status remains In process, select the row of the generated report and choose Refresh. | The status changes to Generated Successfully. |  |
| 8 | Report Details | Choose the generated report. | Another detailed view displays. |  |
| 9 | Navigation | Several sections are available for your generated report:Legal ReportingSelection CriteriaLogAttachments |  |  |
| 10 | Download Report | For the document, select the checkbox to the left and choose Download. |  |  |
| 11 | Submit | When you complete your review of the downloaded file, return to the generated report view.Select the generated document, choose Submit, and choose Yes in the dialog box.Choose Log to review the status.Caution You can repeat a New Run for the report as many times required, if status of the Prepare Advance VAT Return activity is not completed. | The report is submitted and status is updated.Note Offline submission (manual upload) is not supported. |  |

#### Post Tax Payable (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity allows you to pay tax amounts by posting the balances of input and output tax accounts to a tax payable account after the VAT return has been generated.

The output tax account cannot normally be posted directly, which means that a transfer posting for the account balance cannot be made directly to the tax payable account, this activity helps you to post your documents directly.

Prerequisite

The report can only be executed when data is available.

The [Advance VAT Return](#unique_14) [page ] 16 activity must be completed, and the status of the activity set to Completed before executing this procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Germany or as a Tax Accountant - Legal Reporting. |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports - Germany Tax Reporting (F1515_DE_2). | The app opens. |  |
| 3 | Enter Details | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name: DE_VAT_ADV_RTN | A table of reports displays. |  |
| 4 | Select Report to Submit | For the report you want to submit, choose the arrow button at the right of the row. | The Germany Advance VAT Return view for the report displays. |  |
| 5 | Post Tax Payable | Note The Prepare Advance VAT Return activity must have Completed status before you can proceed.Select the Post Tax Payable activity and choose Reopen Activity to set the status to In Process.In the Reopen Activity dialog box, choose Yes to confirm the Are you sure you want to reopen the selected activity? message.Note If the user does not want to execute this activity, then can set the status to Skip or Completed. | A Post Tax Payables details view displays. |  |
| 6 | Post Tax Payable | Create a posting, enter any required or missing data and when the amount is correct, choose Post. | The amount is posted on the corresponding accounts. |  |

#### Application for Permanent Extension (Dauerfristverlängerung) (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request to postpone the deadline to report the Advance VAT return.

This procedure applies to businesses that file quarterly advance VAT returns. It only needs to be applied once (not to be repeated every year) until it is revoked.

Prerequisite

You have executed the Business Conditions chapter.

If you want to submit a report, you must configure electronic communication with the government via the SAP Localization Hub, statutory reporting service. For more information about this service, go to the [Help Portal](https://help.sap.com/viewer/4de200b26d5d42bbacae69c6bf6b9923/latest/en-US/31d43577cebc45b991c74e854ef86573.html).

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Germany or as a Tax Accountant - Legal Reporting. | . |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports (F1515). | The Run Statutory Reports view displays. |  |
| 3 | Enter Criteria | Make the following entries and choose Go:Submission Due Date: Leave blank or enter a <Date range>Report Name: DE_VAT_ADV_RTN |  |  |
| 4 | Select Report to Submit | To create and choose a report to submit, choose Reporting Tasks ->Create Ad hoc Reporting Tasks. | The Ad-hoc Reporting Task dialog box is displayed. |  |
| 5 | Select Report to Submit | Select Report Name DE_EXT_ADV_RTN, make the following entries, and choose OK:Due Date: <Date>Reporting Period: <Date range>Reporting Year: <Year> |  |  |
| 6 | Select Report to Submit | Select the report you created with the following status:Reporting Status: Due LaterNote If the report to submit already exists in the Run Statutory Reports view, select it. | The relevant statutory report is displayed for selection. |  |
| 7 | New Run | Choose New Run. | A dialog box displays. |  |
| 8 | Criteria | In the Standard section, make the following entries and choose Run:Company Code: 1010Fiscal Year: <Year>Run Options section:Start a Short Run Now (Less than 3 Minutes): SelectedNote When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. | In the Generated section, the report displays (verify the date and time). |  |
| 9 | Refresh Report | If the new report has an In Process status, choose Refresh to update the status to Generated Successfully. |  |  |
| 10 | Select | Use the date and time in the Generated On column to ensure that you select the correct report. Select the new report. | A report details view displays. |  |
| 11 | Navigation | Several sections are available to analyze your generated report:Legal ReportingSelection CriteriaLogAttachments |  |  |
| 12 | Download | For the document, select the checkbox to the left and choose Download. |  |  |
| 13 | Attachments | In the Attachments section, drag and drop a file from your computer, or choose the Upload button to select a location and file to attach. |  |  |
| 14 | Submit | When you complete your review of the downloaded file, return to the generated report view.Several option exist:Verify: (Optional) This is a test submission. It does not change the status at the tax authority.Submit: This is the actual submission. It changes the status at the tax authority. The activity is set to completed if the tax authority accepts the submission. If the tax authority declines, the activity remains open. The user can submit it again or create a new run.Update Submission Status: (Optional) This is a manual step that the user can do , which may be useful, for example, to re-open the activity.Choose the Submit button.Choose Yes in the dialog box.Navigate to the Log to review the status.Note You can repeat a New Run for the report as many times as required if the status of the Application for Permanent extension activity is not completed. | The report is submitted and status is updated.Note Offline submission (manual upload) is not supported. |  |

#### Registration of Special Advance Payment (Sondervorauszahlung)(Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request to postpone the deadline to report the Advance VAT return. This procedure applies to businesses that file monthly advance VAT returns. If the application is granted, the business automatically gets an extension.

Prerequisite

You've executed the Business Conditions chapter.

If you want to submit a report, you must configure electronic communication with the government via the SAP Localization Hub, statutory reporting service. For more information about this service, go to the [Help Portal](https://help.sap.com/viewer/4de200b26d5d42bbacae69c6bf6b9923/latest/en-US/31d43577cebc45b991c74e854ef86573.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Germany or as a Tax Accountant - Legal Reporting. |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports - Germany Tax Reporting (F1515_DE_2). | The app opens. |  |
| 3 | Enter Details | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name: DE_PAY_ADV_RTN | A list of reports displays. |  |
| 4 | Select Report to Submit | For the report you want to submit, choose the Details (>) button. | The Germany Registration of Special Advance Payment view for the report displays. |  |
| 5 | New Run | Choose New Run. | A selection criteria dialog box displays. |  |
| 6 | Run execution | Make the following entries and choose Run:Company Code: 1010Year: <leave default value>Special Advance Payment (EUR): <amount>Run Options: Start a Short Run Now (Less than 3 Minutes)Note When you've a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. | A Report started notification displays. The new report is generated and a new row displays in the Generated section. |  |
| 7 | Refresh Report | If the new report status remains In process, select the row of the generated report and choose Refresh. | The status changes to Generated Successfully. |  |
| 8 | Select | Choose the generated report. | Another detailed view displays. |  |
| 9 | Download Report | For the document, select the checkbox to the left and choose Download. |  |  |
| 10 | Attachments | In the Attachments section, drag and drop a file from your computer, or choose the Upload button to select a location and file to attach. |  |  |
| 11 | Submit | When you complete your review of the downloaded file, return to the generated report view.Several options exist:Verify: (Optional) This is a test submission. It won't change the status at the tax authority.Submit: This is the actual submission. It changes the status at the tax authority. The activity is set to completed if the tax authority accepts the submission. If the tax authority declines, the activity remains open. The user can submit it again or create a new run.Update Submission Status: (Optional) This is a manual step that the user can do that may be useful, for example, to reopen the activity.Choose Submit.Choose Yes in the dialog box to confirm submission of the selected report to the government.Navigate to the Log to review the status.Note You can repeat a New Run for the report as many times required, if status of the Registration of Special Advance Payment activity isn't completed. | The report is submitted and status is updated.Note Offline submission (manual upload) is not supported. |  |

### Electronically Supported Tax Audit euBP

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity deals with Statutory Reporting Framework Reports. These steps create the electronically supported tax audit euBP, which is a regular audit by the authority Deutsche Rentenversicherung.

Prerequisite

The report can only be executed if data is available.

For the Financial Statement Version (FSV), use the Manage Global Hierarchies (F2918) app to mark GL accounts that are euBP relevant. The accounts/FSV must be activated to use it.

The customer must request a certificate for encryption from company ITSG forSender Number and Company Number. The company ITSG serves as a mediator between the Deutsche Rentenversicherung authority and software providers like SAP. This company performs the certification of the software, meaning that it certifies that the data are correctly transmitted by the software to Deutsche Rentenversicherung. For more information, contact your system administrator.

|  |
| --- |
| Note Note: The technical communication with authorities is done in a separate component called DRC Cloud Edition (DRCC) which is an SAP BTP app. See SAP Help Documentation for DRC Cloud Edition. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Germany or as a Tax Accountant - Legal Reporting. |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports - Germany euBP Reporting (F1515_DE_4). |  |  |
| 3 | Ad hoc report | To create and choose a report to submit, choose Reporting Tasks > Create Ad hoc Reporting Tasks. | The Ad-hoc Reporting Task dialog box is displayed. |  |
| 4 | Ad hoc report | Select Report NameDE_AUDIT_EUBP.Make the following entries and choose OK:Due Date: <Date>Reporting Period: <Date range>Reporting Year: <Year> | In the Statutory Reporting Tasks section, a new report task is displayed. |  |
| 5 | Select | Select the previously created report to execute and choose Navigation ( > ).Note If the report to submit already exists in the Run Statutory Reports view, select it. |  |  |
| 6 | Select Report to Submit | In the Activities section, select German Audit euBP and choose Details ( > ). |  |  |
| 7 | New Run | Choose New Run. | A dialog box is displayed. |  |
| 8 | Selection Criteria | Make the following entries and choose Run:Financial Statement Version: <FSV version maintained in the Prerequisites)Company Code: 1010Ledger: 0LBalance Sheet Type: Trade LawFrom Fiscal Year: <year>, for example, 2021To Fiscal Year: <year>, for example, 2024Sender Number: <number requested from ITSG (see Prerequisites)>, for example, A0005140Company Number: <number requested from ITSG (see Prerequisites)>, for example, 63987777Company Name: <company name>Contact Person Name: <contact person name>Contact Person Gender: <gender>Contact Phone Number: <phone number>Contact Fax Number: <fax number>Contact E-Mail Address: <e-mail address>Company Number for Tax Consulting Agency: <company number> (Optional)Reason for the Transmission: Audit Announcement / Existing Audit DateLanguage Key: DEReversal Indicator: DeselectedRun Options: Start a Short Run Now (Less than 3 Minutes)Note When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. |  |  |
| 9 | Refresh Report | If the new report status remains In Process, select the row of the generated report and choose Refresh. |  |  |
| 10 | Navigation | Several sections are available for your generated report:Legal ReportingSelection CriteriaLogAttachments |  |  |
| 11 | Download Report | For the document, select the checkbox to the left and choose Download. |  |  |
| 12 | Submit | Choose Submit to send selected report run to the authority.In the dialog box, choose Yes. | Run status changes to Submission Initiated. |  |
| 13 | Rejected (Reversal Run) | If the report is rejected by the authorities (Run status is Rejected), execute a new run with the same parameters of the first run (point 8), ensuring that you select the Reversal Indicator checkbox. |  |  |
| 14 | Repeat run | After the reversal run is approved, execute a new run, but ensure that the Reversal Indicator checkbox is deselected to submit the corrected report. |  |  |

## Appendix

### 50A Withholding Tax Report (Optional)

Purpose

This activity deals with Statutory Reporting Framework reports.

Certain categories of income earned by foreign non-resident payees (Section 49 Income Tax Act [EStG]) are subject to the tax withholding procedure set out in Section 50a EStG. Payers of remuneration are required to withhold, pay, and report taxes.

|  |
| --- |
| Caution This report is only provided as demo data. If a customer is required to generate 50A reports, you must perform manual configuration in Production systems. |

Prerequisite

The report can only be executed when data is available.

If you want to use this in a Production system, the following is required:

- Create Withholding Tax configuration
- Configure 50A Withholding Tax Report

Procedure

For information on configuration and implementation, see the following Germany Withholding Tax Help pages in the SAP Help Portal:

- [Withholding Tax Configurations](https://help.sap.com/viewer/DRAFT/e2d057b7b4df44ba941a040d4dda2956/2208.500/en-US/73c183d00e4845e1908efc281bf002b9.html)
- [Configuration for Withholding Tax Report](https://help.sap.com/viewer/DRAFT/e2d057b7b4df44ba941a040d4dda2956/2208.500/en-US/465131647b07416d84091a5370338b09.html)
- [Generating Withholding Tax (50A) Report](https://help.sap.com/viewer/DRAFT/e2d057b7b4df44ba941a040d4dda2956/2208.500/en-US/6dc199215e024e9f8fd2bf2dc77c91c9.html)

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
- related-to :: [[04-tax-and-statutory-reporting/test-script-intrastat-processing-for-germany-5ol-sap-s-4hana-cloud-pub]]
- related-to :: [[04-tax-and-statutory-reporting/vat-tax-calculation-and-reporting-for-germany-55u-test-script-1071]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5O6_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 48,843 chars in the whole document
