---
id: 04-tax-and-statutory-reporting/compliance-formats-support-preparation-for-czech-republic-5z7-test-scr
title: Compliance Formats – Support Preparation for Czech Republic (5Z7) Test Script (5Z7_S4CLD2608_BPD_EN_XX)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 5Z7: Czech Republic statutory reports (VAT return, EC Sales List, financial statement, cash flow) via F1515_CZ."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/czech-vat-intrastat-and-compliance-formats]
aliases: [5Z7_S4CLD2608_BPD_EN_XX]
keywords: ["Czech Republic VAT, Intrastat and Compliance Formats", czech republic vat return, ec sales list, financial statement, cash flow statement, advanced compliance reporting, statutory reporting, registration for indirect taxation abroad, company code assignment, financial statement versions]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z7_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1138
topic: 04-tax-and-statutory-reporting/czech-vat-intrastat-and-compliance-formats
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Compliance Formats – Support Preparation for Czech Republic (5Z7) Test Script (5Z7_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z7_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Czech Republic VAT, Intrastat and Compliance Formats** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Compliance Formats – Support Preparation for Czech Republic (5Z7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232825164)

[2 Prerequisites 3](#_Toc232825165)

[2.1 System Access 3](#_Toc232825166)

[2.2 Roles 3](#_Toc232825167)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232825168)

[2.4 Business Conditions 4](#_Toc232825169)

[2.5 Preliminary Steps 5](#_Toc232825170)

[2.5.1 Check Activated Financial Statement Versions 5](#_Toc232825171)

[2.5.2 Assign Company Code 6](#_Toc232825172)

[2.5.3 Activate Registration for Indirect Taxation Abroad 7](#_Toc232825173)

[2.5.3.1 Activate Registration for Indirect Taxation Abroad (Optional) 8](#_Toc232825174)

[3 Overview Table 9](#_Toc232825175)

[4 Test Procedures 10](#_Toc232825176)

[4.1 Run Statutory Reports - Czech Republic VAT Return 10](#_Toc232825177)

[4.2 EC Sales List - Czech Republic 11](#_Toc232825178)

[4.3 Financial Statement - Czech Republic 13](#_Toc232825179)

[4.4 Cash Flow Statement - Czech Republic 15](#_Toc232825180)

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
|  |  |  |  |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data to go through the test procedures. If you have installed an SAP Best Practices package, you can use the following package scenario data: Accounting.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | <your company code> |  |  |
| Controlling Area | A000 |  |  |
| Cost Center | 20101101 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

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
| J59 - Accounts Receivable | Must be run before this test script.Ensure that invoices for customers and payments for the invoices are created. |

### Preliminary Steps

#### Check Activated Financial Statement Versions

Use

In this activity, you check that the financial statement versions are activated.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Chart of Accounts, choose Details (>).
2. For the Define Financial Statement Versions row, choose Configure.
3. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Financial Statement Versions.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select Financial Statement Version | Select the following financial statement version and choose Financial Statement Items:Financial Statement Version: 2010,2020,2030,2040 | The Change Financial Statement Version view displays. |  |
| 2 | Save and Activate | Save and activate your entries. | Data is saved and activated. |  |

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
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Setting Up Your Compliance Reporting.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select | Select your reporting entity, for example:Reporting entity: CZ_RPG_ENT |  |  |
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

Table 2: Czech Republic

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Run Statutory Reports - Czech Republic VAT Return](#unique_12) [page ] 10 |  | Run Statutory Reports - Czech Republic GL Reporting (F1515_CZ) | The report is generated. |
| [EC Sales List - Czech Republic](#unique_13) [page ] 11 |  | Run Statutory Reports - Czech Republic GL Reporting (F1515_CZ) | The report is generated. |
| [Financial Statement - Czech Republic](#unique_14) [page ] 13 |  | Run Statutory Reports - Czech Republic GL Reporting (F1515_CZ) | The report is generated. |
| [Cash Flow Statement - Czech Republic](#unique_15) [page ] 15 |  | Run Statutory Reports - Czech Republic GL Reporting (F1515_CZ) | The report is generated. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Run Statutory Reports - Czech Republic VAT Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity deals with Statutory Reporting for Czech Republic VAT. These steps provide a detailed procedure for running reports, reflecting the predefined scope of the solution.

|  |
| --- |
| Note The Czech Republic VAT Return procedure assists with the completion of the VAT Declaration, which is submitted to the tax office. The VAT Declaration is not in-scope for this solution. |

Prerequisite

The report can only be executed when data is available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a . |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports - Czech Republic GL Reporting (F1515_CZ). | The app opens. |  |
| 3 | Enter Criteria | Make the following entries for the Czech Republic VAT Declaration report and choose Go:Reporting Status: Due LaterReport Name: CZ_VAT_DCL | A table of reports displays. |  |
| 4 | Select a Report | Select a Czech Republic VAT Declaration report for the time period to submit. | A details page for the selected report displays. |  |
| 5 | Select the VAT Return Activity | Select the CZ VAT Control Statement row in the Activities list. | The details page of the Czech Republic VAT Return displays. |  |
| 6 | New Run | Choose the New Run button. | A Selection Criteria for CZ VAT Control Statement dialog box is displayed. |  |
| 7 | Default Settings | Keep the default settings for Company Code, Reporting Date, and Run Options, then choose Run. | The Generated section shows an In Process run. |  |
| 8 | In Process | Choose the right arrow button at the end of the In Process run. | The report detail view is displayed. |  |
| 9 | Refresh View | Choose Refresh until the Run Status field changes from In Process. |  |  |
| 10 | Select Log | Choose the Log tab and review Message Text to verify that documents are created.Choose the (!) icon, if visible, for details of missing or incorrect data when the report status of the run isGenerated with errors. | Verify that report published or provides details when generated with errors. |  |
| 11 | View Document | In the Legal Reporting pane, double-click the CZ_VAT_RETURN document. | The report displays in a new screen. |  |
| 12 | View Document | Choose Back. |  |  |
| 13 | View Document | Repeat steps 10 to 12 for the CZ_VAT_CONTROL document. |  |  |
| 14 | Download Files | To download the files, select the checkboxes for the files and choose the Download button. |  |  |
| 15 | Go Back | Choose Back. | The Report Run Status changes to Submission Accepted by Authority. |  |

### EC Sales List - Czech Republic

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

All Czech Republic taxpayers having EU VAT registration number (the one starting with CZ) are obliged to deliver monthly statements, called EC Sales List (VAT-UE, VAT-UEK), to Czech Republic Tax Authorities.

Prerequisite

The VAT registration number (NIP) must be assigned in the Customer and Vendor master data settings.

Goods and Services tax codes are maintained.

The report can only be executed when data is available. The EC Sales report is generated only if there are postings made against foreign customers/vendors.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a . |  |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports - Czech Republic GL Reporting (F1515_CZ). | The app opens. |  |
| 3 | Enter Criteria | Make the following entries and choose Go:Reporting Status: OverdueReport Name: CZ_ECSL | A table displays with Czech Republic EC Sales List reports. |  |
| 4 | Select Report to Submit | Select a report to generate for the Submission Due Date by choosing the > (Arrow) button at the right of the row . | The details view of the selected report displays. |  |
| 5 | Select an Activity | In the Current Phases section, select EC Sales List (Czech Republic) activity by choosing the > (Arrow) button at left of the row . | A details view of the selected activity displays. |  |
| 6 | Create New Run | Choose New Run. | A selection criteria dialog box displays. |  |
| 7 | Enter Criteria and Run | Verify or make the following entries and choose Run:Company Code: 2010Reporting Date: <date range> (refers to the Tax Reporting Date)Run Options: Start a Short Run Now (Less than 3 Minutes)Tip When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. | A Run started notification displays and the report generates. |  |
| 8 | Select Report | If the report has an In Process status, choose the Refresh button from the top right of the view to change status to Generated Successfully.Under the Generated tab, double-click the generated report. | A Run details view displays. |  |
| 9 | Select Log | Choose the Log tab and review Message Text to verify that documents are created.Choose the (!) icon, if visible, for details of missing or incorrect data when the report status of the run is Generated with errors. | Verify that report published or provides details when generated with errors. |  |
| 10 | Review Data | From this view, you can review the data used to generate the file. You can download the analysis as an XML file. When the analysis is completed, close the view to return to the details view. |  |  |
| 11 | Download File | Choose the Legal Reporting tab and select the checkbox for the row of the document and choose Download. | File in XML format downloads and ready to be sent. |  |
| 12 | Change Submission Status | Choose Update Submission Status from the bottom of the view. Choose Yes to confirm the This change cannot be reversed. Do you really want to change the status of this report to "Accepted by Authority"? notification. | A Status of report run updated notification displays. |  |
| 13 | Verify Status | Choose the < (Back) icon to return to the Czech Republic EC Sales List report details view. From the Submitted tab, your report displays with a Submission Accepted by Authority report run status. |  |  |

### Financial Statement - Czech Republic

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can create Balance Sheet and Profit and Loss Statement report and submit it as an XML file.

Prerequisite

The report can only be executed when data is available.

You must ensure that your financial statement versions are activated. For more information, see [Check Activated Financial Statement Versions](#unique_7) [page ] 5 in the Preliminary Steps section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a . |  |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports - Czech Republic GL Reporting (F1515_CZ). | The app opens. |  |
| 3 | Enter Details | Make the following entries:Reporting Status: DefaultSubmission Due Date: <Date range> or use defaultReport Name: CZ_FINSTATEMENTEach report name represents a different reporting period: monthly, quarterly, or yearly.Reporting Year: <year of reported period>Country: CZand choose Go. | A list of reports displays. |  |
| 4 | Select Report | Select a report. | A details view of the selected report displays. |  |
| 5 | New Run | Choose New Run from the bottom of the view. | A selection criteria dialog box displays. |  |
| 6 | Enter Criteria and Run | Verify or enter the following data:Company Code: 2010Ledger: 0LReporting Date: <period>Comparison From Period: <period>Comparison To Period: <period>Comparison Fiscal Year: <period>DIsplay Alternative Accounts: <flagged>Run Options: Start a Short Run Now (Less than 3 Minutes)and choose Run. | A Run started notification displays. The new report generates and a new row displays in the Generated section. |  |
| 7 | Select Report | Note If the report has In Process status, choose the Refresh icon from the top right of the view to change status to Generated Successfully.Under the Generated tab, double-click the report that generated. | A Run details view displays. |  |
| 8 | Display Report | In the Legal Reporting pane, double-click theFinancial Statement XML File document. | The report displays in a new screen. |  |
| 9 | Download | To download the files, select the checkboxes for the files and choose Download. |  |  |
| 10 | Change Submission Status | Choose Update Submission Status from the bottom of the view.A dialog box displays a This change cannot be reversed. Do you really want to change the status of this report run to "Accepted by Authority?" notification. Choose Yes. | The status changes to Submission Completed and the report details view moves the report to the Submitted section with Submission Accepted by Authority report run status. |  |

### Cash Flow Statement - Czech Republic

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you can create Cash Flow Statement report via application Run Statutory Reports.

Prerequisite

The report can be executed when the data is available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a . |  |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports - Czech Republic GL Reporting (F1515_CZ). | The app opens. |  |
| 3 | Enter Details | Make the following entries:Reporting Status: defaultSubmission Due Date: <Date range> or use defaultReport Name: CZ_CASHFLOWEach report name represents a different reporting period: monthly, quarterly, or yearly.Reporting Year: <year of reported period>Country: CZand choose Go. | A list of reports displays. |  |
| 4 | Select Report | Select a report. | A details view of the selected report displays. |  |
| 5 | New Run | Choose New Run from the bottom of the view. | A selection criteria dialog box displays. |  |
| 6 | Enter Criteria and Run | Verify or enter the following data:Company Code: 2010Reporting Date: <period>Comparision Reporting Date: <period>Ledger: 0LDIsplay Alternative Accounts: <flagged>Run Options: Start a Short Run Now (Less than 3 Minutes)and choose Run. | A Run started notification displays. The new report generates and a new row displays in the Generated section. |  |
| 7 | Select Report | Note If the report has In Process status, choose the Refresh icon from the top right of the view to change status to Generated Successfully.Under the Generated tab, double-click the report that generated. | A Run details view displays. |  |
| 8 | Display Report | In the Legal Reporting section, double-click the Cash Flow Statement Indirect Method document. | The report displays on a new screen. |  |
| 9 | Change Submission Status | Choose Update Submission Status from the bottom of the view.A dialog box displays a This change cannot be reversed. Do you really want to change the status of this report run to "Accepted by Authority?" notification. Choose Yes. | The status changes to Submission Completed and the report details view moves the report to the Submitted section with Submission Accepted by Authority report run status. |  |

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
- related-to :: [[04-tax-and-statutory-reporting/test-script-intrastat-processing-for-czech-republic-5z4-1135]]
- related-to :: [[04-tax-and-statutory-reporting/vat-tax-calculation-and-reporting-for-czech-republic-5z2-test-script-1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5Z7_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 31,526 chars in the whole document
