---
id: 04-tax-and-statutory-reporting/test-script-compliance-formats-support-preparation-for-sweden-5z6-1137
title: "Test Script: Compliance Formats – Support Preparation for Sweden (5Z6) (5Z6_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition test script (5Z6) for Sweden advanced compliance reporting: setup, RITA, running the EC Sales List and VAT Return via Run Statutory Reports (F1515)."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/sweden-vat-intrastat-and-compliance-formats]
aliases: [5Z6_S4CLD2608_BPD_EN_XX]
keywords: ["Sweden VAT, Intrastat and Compliance Formats", advanced compliance reporting, sweden vat return, ec sales list, registration for indirect taxation abroad, reporting entity setup, business role templates, business conditions, master data scripts, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z6_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1137
topic: 04-tax-and-statutory-reporting/sweden-vat-intrastat-and-compliance-formats
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Compliance Formats – Support Preparation for Sweden (5Z6) (5Z6_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z6_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Sweden VAT, Intrastat and Compliance Formats** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Compliance Formats – Support Preparation for Sweden (5Z6) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232825437)

[2 Prerequisites 3](#_Toc232825438)

[2.1 System Access 3](#_Toc232825439)

[2.2 Roles 3](#_Toc232825440)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232825441)

[2.4 Business Conditions 5](#_Toc232825442)

[2.5 Preliminary Steps 5](#_Toc232825443)

[2.5.1 Assign Company Code 5](#_Toc232825444)

[2.5.2 Activate Registration for Indirect Taxation Abroad 6](#_Toc232825445)

[2.5.2.1 Activate Registration for Indirect Taxation Abroad (Optional) 7](#_Toc232825446)

[3 Overview Table 8](#_Toc232825447)

[4 Test Procedures 9](#_Toc232825448)

[4.1 Run Compliance Reports - Sweden EC Sales List 9](#_Toc232825449)

[4.2 Run Compliance Reports - Sweden VAT Return 11](#_Toc232825450)

## Purpose

Overview

SAP S/4HANA for advanced compliance reporting is a global legal reporting platform that caters to companies’ indirect tax reporting requirements. This solution enables the end-to-end process of legal reporting including multiple activities that may be necessary to complete the legal reporting. The solution offers a unified and harmonized user experience across countries and reports, enabling a simplified view of the reporting status to the business users and the company's head of tax and compliance. It also provides a design environment to easily create and extend additional report requirements.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

Additional Information on the SAP Help Portal

For additional information, including descriptions of features for Advanced Compliance Reporting, visit the SAP Help Portal ([https://help.sap.com](https://help.sap.com)). On the initial page, enter: Advance Compliance Reporting in the Search field. The results provide additional documentation details about Advanced Compliance Reporting.

With the introduction of scope item Document and Reporting Compliance (5XU), this scope item has been restructured. It now only contains content that does not require an additional license. To use advanced features as specified in the feature and scope description of SAP S/4HANA Cloud Public Edition, an additional license of either SAP S/4HANA Cloud for Advanced Compliance Reporting (discontinued) or its successor SAP Document and Reporting Compliance for SAP S/4HANA Cloud Public Edition is required. To enable the advanced features, please activate scope item 5XU and follow the corresponding instructions.

|  |
| --- |
| Note If your instance was already live before CE2111, we ensure continuity. The advanced features are still visible. |

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| General Ledger Accountant for Sweden | SAP_BR_GL_ACCOUNTANT_SE | General Ledger | SAP_FIN_SPT_GL_ACCOUNTING_GLO_SE_PC |  |
|  |  |  |  |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedures. If you have installed an SAP Best Practices package, you can use the following package scenario data: Accounting.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | <your company code> |  |  |
| Customer | 19100051 |  |  |
| Controlling Area | A000 |  |  |
| Supplier | 17100030 for 1099 Withholding tax 17300031 for 1042 Withholding tax |  |  |
| Cost Center | 19101101 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Must be run before this test script. |
| J59 - Accounts Receivable | Must be run before this test script.Ensure that invoices for customers and payments for the invoices are created. |

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
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Setting Up Your Compliance Reporting .
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select | Select your reporting entity, for example:Reporting entity: SE_RPG_ENT |  |  |
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

Table 2: Sweden

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Run Compliance Reports - Sweden EC Sales List](#unique_11) [page ] 9 | General Ledger Accountant for Sweden | Run Statutory Reports (F1515) | Report and file generate. |
| [Run Compliance Reports - Sweden VAT Return](#unique_12) [page ] 11 | General Ledger Accountant for Sweden | Run Statutory Reports (F1515) | Report and file generate. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Run Compliance Reports - Sweden EC Sales List

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

EC Sales list-relevant documents should be posted. To execute this activity run the processes in Sell from Stock (BD9) using the master data that is valid for EC Sales list. You can use customers, for example, 19100051 or 19100052.

Sales order billings to EU customers are posted.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Sweden . |  |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports (F1515). |  |  |
| 3 | Add Ad-Hoc Reporting Task | If a report does not appear, create an ad-hoc report. To do so, choose + (Add Ad-Hoc Reporting Task). | The Add Ad-Hoc Reporting Task dialog box is displayed. |  |
| 4 | Enter Criteria | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name: SE_ECSL_DCL | The Advanced Compliance Reports table displays SE EC Sales List reports listed by Reporting Status. |  |
| 5 | Select Report to Submit | Select the report to generate. | The SE EC Sales List view displays. |  |
| 6 | Create New Run | Choose New Run. | A selection criteria dialog box displays. |  |
| 7 | Execute | Make or verify the following entries and choose Run:Company Code: <your company code>Reporting Date: <date range>Run Options: Start a Short Run Now (Less than 3 Minutes)Note When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. | A Run started notification appears and the report generates. A new report displays in the Generated area. |  |
| 8 | Select Report | If the generated report has a In Process status, choose the Refresh button from the top right of the view to change status to Generated Successfully.On the Generated tab, double-click the report that generated. | A Run details view displays. |  |
| 9 | Analyze Data | On the Legal Reporting tab, on the EC Sales List row, choose the Analyze Data - Design Studio button in the Action column.On the Tax Item [Reporting Date <date range> view that displays, analyze the data in table or chart form.When finished with analysis, return to the previous view. | Data analyzed. |  |
| 10 | Preview Report | In the Legal Reporting section, double-click the EC Sales List document name to preview the report.In the view that displays, expand all nodes to preview the report.When finished with the preview, return to the previous view. |  |  |
| 11 | Download File | On the Legal Reporting tab, select the checkbox for the row for EC Sales List - Service and choose Download. | A TXT file downloads that you can review and then upload for the government. |  |

### Run Compliance Reports - Sweden VAT Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the Sweden VAT return report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for Sweden . |  |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports (F1515). |  |  |
| 3 | Add Ad-Hoc Reporting Task | If a report does not appear, create an ad-hoc report. To do so, choose + (Add Ad-Hoc Reporting Task). | The Add Ad-Hoc Reporting Task dialog box is displayed. |  |
| 4 | Enter Criteria | Make the following entries and choose Go:Report Name: SE_VAT_DCL |  |  |
| 5 | Select Report to Submit | Select the report to submit. | The details view of the relevant compliance report displays. |  |
| 6 | New Run | Select the row with the activity name of Generate VAT Return and choose New Run. | The Selection Criteria for Generate VAT Return dialog box displays. |  |
| 7 | Enter Details | Make or verify the following entries and choose Run:Company Code: <your company code>Reporting Date: <Date range>Run Options: Start a Short Run Now (Less than 3 Minutes)Note When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. | A Run started notification displays. The new report generates and a new row displays in the Generated section. |  |
| 8 | Select Report | If the new report status is still In process, choose Refresh. Select the generated report. | A detailed view of the selected report displays. |  |
| 9 | Analyze Data | In the Legal Reporting section, choose the Sweden VAT Return document link. | The system displays a preview. |  |
| 10 | Verify Data | Check that the content is correct and that all tax items are displayed.Note The reported amounts are displayed without decimal places. There is no rounding in Sweden. The report first sums all line items and then cuts off the decimal places for all tax boxes except 49. The calculation box 49 (VAT to pay or recover) is the result of output VAT - input VAT. |  |  |
| 11 | Edit Data | Choose Edit. |  |  |
| 12 | Edit Data | Make some changes (such as entering text in the Text Information field).Choose Save and Regenerate. | The system displays an Information dialog box with the message Changes have been saved and regeneration is in process. |  |
| 13 | Confirm | Choose OK. |  |  |
| 14 | Download | Select the checkbox for the Sweden VAT Return document and choose Download. |  |  |
| 15 | Verify Data | Open the downloaded file to ensure the data is correct. |  |  |
| 16 | Analyze Data | For the Sweden VAT Return document row, choose the Analyze Data button in the Action column. |  |  |
| 17 | Analyze Data | Check that the data is correctly displayed. If needed, you can add more dimensions to the rows to provide additional analysis. |  |  |

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
- related-to :: [[04-tax-and-statutory-reporting/test-script-intrastat-processing-for-sweden-5z3-1134]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-vat-tax-calculation-and-reporting-for-sweden-5z1-1132]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z6_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 23,430 chars in the whole document
