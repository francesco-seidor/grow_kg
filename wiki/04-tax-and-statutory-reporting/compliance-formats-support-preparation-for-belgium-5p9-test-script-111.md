---
id: 04-tax-and-statutory-reporting/compliance-formats-support-preparation-for-belgium-5p9-test-script-111
title: Compliance Formats – Support Preparation for Belgium (5P9) Test Script (5P9_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5P9: Belgium statutory reports (VAT return, VAT unit declaration, EC Sales List) for foreign company codes via RITA."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/belgium-vat-intrastat-and-compliance-formats]
aliases: [5P9_S4CLD2608_BPD_EN_XX]
keywords: ["Belgium VAT, Intrastat and Compliance Formats", belgium vat return, vat unit declaration, ec sales list, advanced compliance reporting, registration for indirect taxation abroad, statutory reports, company code assignment, non-deductible vat, tax balance grouping]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5P9_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1119
topic: 04-tax-and-statutory-reporting/belgium-vat-intrastat-and-compliance-formats
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Compliance Formats – Support Preparation for Belgium (5P9) Test Script (5P9_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5P9_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Belgium VAT, Intrastat and Compliance Formats** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Compliance Formats – Support Preparation for Belgium (5P9) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232825000)

[2 Prerequisites 3](#_Toc232825001)

[2.1 System Access 3](#_Toc232825002)

[2.2 Roles 3](#_Toc232825003)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232825004)

[2.4 Business Conditions 5](#_Toc232825005)

[2.5 Preliminary Steps 5](#_Toc232825006)

[2.5.1 Assign Company Code 5](#_Toc232825007)

[2.5.2 Activate Registration for Indirect Taxation Abroad 7](#_Toc232825008)

[2.5.2.1 Activate Registration for Indirect Taxation Abroad (Optional) 7](#_Toc232825009)

[3 Overview Table 9](#_Toc232825010)

[4 Test Procedures 10](#_Toc232825011)

[4.1 Run Statutory Reports - Belgium VAT Return 10](#_Toc232825012)

[4.2 Run Statutory Reports - Belgium Declaration for VAT Units 13](#_Toc232825013)

[4.3 Run Statutory Reports Framework for EC Sales List 15](#_Toc232825014)

## Purpose

Overview

SAP S/4HANA for advanced compliance reporting is a global legal reporting platform that caters to companies’ indirect tax reporting requirements. This scope item covers company codes outside of Belgium with tax registration in Belgium.

The solution enables the end-to-end process of legal reporting including multiple activities that may be necessary to complete the legal reporting.

The solution offers a unified and harmonized user experience across countries and reports, enabling a simplified view of the reporting status to the business users and the company’s head of tax and compliance. It also provides a design environment to easily create and extend additional report requirements.

For more information, we recommend to check the country roadmap for Registration for Indirect Taxation Abroad (RITA). Verify that the company code country and country of tax registration support the RITA solution.

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

Table 1: Belgium

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| General Ledger Accountant for Belgium | SAP_BR_GL_ACCOUNTANT_BE |  |  |  |
| Country/Region-specific subrole:Accounts Payable Manager for Belgium | SAP_BR_AP_MANAGER_BE |  |  |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Package, you can use the following Package scenario data: Accounting.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 2510 |  |  |
| Customer | 25100050 (US), 25100051 (FR) and 25100052 (HU) |  |  |
| Supplier | 25300030 for WHT 506125300031 for WHT 506025300032 for WHT 5060 natural person |  |  |
| House Bank | BEBK1/BEAC1 BEBK2/BEAC2 | BK1 is used for the Multi-Bank Connectivity (MBC) and BK2 is used for file download. |  |
| Bank G/L Account | 11001000,11002000 |  |  |
| Cost Center | 25101101 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Must be run before this test script. |
| J59 - Accounts Receivable | Must be run before this test script.Ensure that invoices for vendors and payments for the invoices are created. |
| BD9 - Sell from Stock | Must be run before this test script. |
| 5IS - VAT Tax Calculation and Reporting for Belgium | Scope item is activated. |

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
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Statutory Reporting

1. For the row with Item Name of Basic Settings, choose Details (>).
2. For the Setting Up Your Compliance Reporting row, choose Configure.
3. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Setting Up Your Compliance Reporting.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select | Select your reporting entity, for example:Reporting entity: BE_RPG_ENT |  |  |
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
| [Run Statutory Reports - Belgium VAT Return](#unique_11) [page ] 10 | General Ledger Accountant for Belgium | Run Statutory Reports - Belgium GL Reporting (F1515_BE_2) | Report is generated and tax items maintained. |
| [Run Statutory Reports - Belgium Declaration for VAT Units](#unique_12) [page ] 13 | General Ledger Accountant for Belgium | Run Statutory Reports - Belgium GL Reporting (F1515_BE_2) |  |
| [Run Statutory Reports Framework for EC Sales List](#unique_13) [page ] 15 | General Ledger Accountant for Belgium | Run Statutory Reports - Belgium GL Reporting (F1515_BE_2) | Report and file generate. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Run Statutory Reports - Belgium VAT Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity deals with Statutory Reporting Framework Reports. These steps provide a detailed procedure for running reports, reflecting the predefined scope of the solution.

Prerequisite

The report can only be executed when data is available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Belgium . |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports - Belgium GL Reporting (F1515_BE_2) . | The Run Statutory Reports view displays. |  |
| 3 | Enter Details | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name: BE_VAT_DCL | A list of Statutory Reports displays in a table. |  |
| 4 | Select Report to Submit | Select the report to submit by choosing > (arrow) on the right of the row. | The report details view displays. |  |
| 5 | Select Activity | Two activities are listed for the selected report:VAT Return (Belgium) - In this activity, you create a new run of the VAT report that you download for submission.To create a new report, follow steps 6 - 14.Post Tax Payable - In this activity, you post tax payable.To post, follow steps 15 and 16.Note The VAT Return (Belgium) activity must be completed and the status of the activity must be set to Completed before proceeding with the steps in the Post Tax Payable activity. | The Selection Criteria for VAT Return (Belgium) dialog box displays. |  |
| 6 | Activity 1: Run the VAT Return Statement | On the Activities list, double-click the VAT Return (Belgium) activity name. | The Belgium VAT Return details view displays. |  |
| 7 | New Run | Choose New Run. | A selection criteria dialog box displays. |  |
| 8 | Enter Details | Make or verify the following entries and choose Run:Company Code: <your company code>Reporting Date: <Period based on your selection>Request Restitution: leave blankOrder Payment Form: leave blankRun Options: Start a Short Run Now (Less than 3 Minutes)Tip When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, select Start a Long Run Now. When your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later and choose Run. | A Report started notification displays. The new report generates and a new row displays in the Generated section. |  |
| 9 | Refresh Report | If the new report status remains In Process, select the row of the generated report and choose Refresh. | The status changes to Generated Successfully. |  |
| 10 | Report Details | Double-click the generated report. | A run details view displays. |  |
| 11 | Download Report | After completing your review of the analysis, close the view and return to the previous details view.Under the Legal Reporting section, select the checkbox for the VAT Return (Belgium) document row and choose Download. | The report downloads in an XML file. |  |
| 12 | Analyze XML Report | Open the XML file from download location and verify that the content is correct. |  |  |
| 13 | Update Submission Status | When you complete your review of the downloaded file, return to the report details view.Choose Update Submission Status.Caution You can repeat a New Run for the report as many times as required until you change the status of the VAT Return (Belgium) activity to completed using Update Submission Status. After the status is changed to Completed, no further reports are run and you cannot revert the completed status.If the report is complete, confirm the This change cannot be reversed. Do you really want to change the status of this report run to "Accepted by Government"? notification. | The VAT Return (Belgium) activity displays a Completed status. |  |
| 14 | Return to Activities View | Choose < (Back) twice to return to the Activities view. | The report details view displays. |  |
| 15 | Activity 2: Post Tax Payable | Note The VAT Return (Belgium) activity must have a Completed status before you can proceed.Select the Post Tax Payable activity and confirm the Do you want to change the status of the activity to "In Process"? notification. | The Post Tax Payables details view displays. |  |
| 16 | Post Tax Payable | Create a posting and when the amount is correct, choose Post at the bottom of the view. | The amount is posted on the corresponding accounts. |  |

Country-specific logic for non-deductible taxes (transaction types NVV and NAV) for Belgium:

When documents contain (VST) deductible and (NVV, NAV) non-deductible VAT, the non-deductible tax amount is reported along with the tax base amount. This applies to tax boxes 81, 82 and 83.

The following settings are prerequisites for the correct XML output, (for example, for tax box 82):

Grouping of Tax Balances:

| Description | Transaction | Balance | Group Number |
| --- | --- | --- | --- |
| 21% input tax - 65% non-deductible | VST | H | 82 |
| 21% input tax - 65% non-deductible | VST | H | 85 |
| 21% input tax - 65% non-deductible | VST | S | 82 |

Grouping of Tax Balances:

| Description | Transaction | Balance | Group Number |
| --- | --- | --- | --- |
| 21% input tax - 65% non-deductible | NVV | H | 82 |
| 21% input tax - 65% non-deductible | NVV | S | 82 |
| 21% input tax - 65% non-deductible | VST | H | 63 |
| 21% input tax - 65% non-deductible | VST | S | 59 |

### Run Statutory Reports - Belgium Declaration for VAT Units

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Companies that form part of a VAT unit do their VAT returns collectively as one single entity subject to VAT. However, in the case of statistical declarations for the National Bank of Belgium (NBB), this advantage does not apply: each company that is selected is required to complete these declaration(s) on an individual basis.

This activity deals with Statutory Reporting Framework Reports. These steps provide a detailed procedure for running reports, reflecting the predefined scope of the solution.

Prerequisite

The report can only be executed when data is available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Belgium . |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports - Belgium GL Reporting (F1515_BE_2). | The Run Statutory Reports view displays. |  |
| 3 | Enter Details | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name: BE_VUNIT_DCL | A list of Statutory Reports displays in a table. |  |
| 4 | Select Report to Submit | Select the report to submit by choosing > (arrow) on the right of the row. | The report details view displays. |  |
| 5 | New Run | Choose New Run. | A selection criteria dialog box displays. |  |
| 6 | Enter Details | Make or verify the following entries and choose Run:Company Code: <your company code>Reporting Date: <Period based on your selection>Documents for Generation: Quarterly Declaration (or Annually Declaration, depending on the threshold amount to the VAT Unit)Run Options: Start a Short Run Now (Less than 3 Minutes)Tip When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, select Start a Long Run Now. When your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later and choose Run. | A Report started notification displays. The new report generates and a new row displays in the Generated section. |  |
| 7 | Refresh Report | If the new report status remains In Process, select the row of the generated report and choose Refresh. | The status changes to Generated Successfully. |  |
| 8 | Report Details | Double-click the generated report. | A run details view displays. |  |
| 9 | Download Report | After completing your review of the analysis, close the view and return to the previous details view.Under the Legal Reporting section, select the checkbox for the Quarterly Declaration document row and choose Download. | The report downloads in an XML file. |  |
| 10 | Analyze XML Report | Open the XML file from download location and verify that the content is correct. |  |  |
| 11 | Update Submission Status | When you complete your review of the downloaded file, return to the report details view.Choose Update Submission Status.Caution You can repeat a New Run for the report as many times as required until you change the status of the Belgium Declaration for VAT Units activity to completed using Update Submission Status. After the status is changed to Completed, no further reports are run and you cannot revert the completed status.If the report is complete, confirm the This change cannot be reversed. Do you really want to change the status of this report run to "Accepted by Government"? notification. | The Belgium Declaration for VAT Units activity displays a Completed status. |  |

### Run Statutory Reports Framework for EC Sales List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you execute the statutory reports for the EC Sales List.

Prerequisites

EC Sales list-relevant documents should be posted. To execute this activity, run the steps in Sell from Stock - BD9 using the master data that is valid for EC Sales list. You can use customers, for example, 25100051 or 25100052.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Belgium . |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports - Belgium GL Reporting (F1515_BE_2). | The Run Statutory Reports view displays. |  |
| 3 | Display Statutory Reports | Make the following entries and choose Go:Reporting Status: select Due Later, Due Soon, and OverdueReport Name: BE_ECSL_DCL | A list of Statutory Reports displays by Reporting Status. |  |
| 4 | Select Report to Submit | Select the following report to submit:Belgium EC Sales List | The report details view displays. |  |
| 5 | Select Declaration | In the Current Phases section, select the report and choose the EC Sales List with Call off Stock row. | A details view displays. |  |
| 6 | New Run | Choose New Run. | A Selection Criteria for BE EC Sales list v0_9 dialog box displays. |  |
| 7 | Enter or Verify Details | Make or verify the following entries and choose Run:Company Code: <your company code>Posting Date: <Date Range>Run Options: Use the default setting.Tip When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, select Start a Long Run Now. When your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later and choose Run. | A Run Started notification displays and a new report displays in the Generated section of the report details view. |  |
| 8 | Refresh Status | If the new report status remains In Process, select the row of the generated report and choose Refresh. | The status changes to Generated Successfully. |  |
| 9 | Select Report | Select the generated report. | The report details view displays. |  |
| 10 | Download Report | Under the Legal Reporting section, select the checkbox for the BE ECSL document row and choose Download. | The report downloads. |  |

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
- related-to :: [[04-tax-and-statutory-reporting/intrastat-processing-for-belgium-5pa-test-script-1120]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-vat-tax-calculation-and-reporting-for-belgium-5is-1105]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5P9_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 29,166 chars in the whole document
