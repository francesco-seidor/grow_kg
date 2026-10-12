---
id: 04-tax-and-statutory-reporting/test-script-compliance-formats-support-preparation-1j2-ae-sap-s-4hana
title: "Test Script: Compliance Formats – Support Preparation (1J2_AE) – SAP S/4HANA Cloud Public Edition 2608 (1J2_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for UAE statutory reporting (scope 1J2_AE): config prerequisites, VAT return, FAF audit file, cash flow statement."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/uae-vat-return-and-statutory-reports]
aliases: [1J2_S4CLD2608_BPD_EN_AE]
keywords: [UAE VAT Return and Statutory Reports, uae statutory reporting, uae vat return, faf audit file, cash flow statement, document and reporting compliance, statutory reporting setup, scope item testing, financial statement hierarchy, reporting entity]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1J2_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-728
topic: 04-tax-and-statutory-reporting/uae-vat-return-and-statutory-reports
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Compliance Formats – Support Preparation (1J2_AE) – SAP S/4HANA Cloud Public Edition 2608 (1J2_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1J2_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **UAE VAT Return and Statutory Reports** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 28-08-26 |
| --- | --- |
|  | Compliance Formats – Support Preparation (1J2_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc239508747)

[2 Prerequisites 3](#_Toc239508748)

[2.1 System Access 3](#_Toc239508749)

[2.2 Roles 3](#_Toc239508750)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc239508751)

[2.4 Business Conditions 5](#_Toc239508752)

[2.5 Preliminary Steps 6](#_Toc239508753)

[2.5.1 Assign Organization Unit 6](#_Toc239508754)

[2.5.2 Import Report Hierarchies for Cash Flow Indirect Method 7](#_Toc239508755)

[2.5.3 Setting Up Your Statutory Reporting for UAE 10](#_Toc239508756)

[3 Overview Table 13](#_Toc239508757)

[4 Test Procedures 14](#_Toc239508758)

[4.1 Manage Document and Reporting 14](#_Toc239508759)

[4.2 Run Statutory Reports - UAE VAT Return 15](#_Toc239508760)

[4.3 Run Statutory Reports - UAE - VAT - FAF Audit File 18](#_Toc239508761)

[4.4 Run Statutory Reports – Utd.Arab Emir. Cash Flow Statement (Report) 21](#_Toc239508762)

## Purpose

Overview

SAP Document and Reporting Compliance for SAP S/4HANA Cloud Public Edition (formerly SAP S/4HANA Cloud for advanced compliance reporting) is SAP’s solution for the fulfillment of real-time and statutory reporting requirements including end-to-end processing of transaction controls, digital link, and online submission requirements. This scope item activates the display and output of the country content for manual submission processes.

Additional Information on the SAP Help Portal

For additional information, including descriptions of features for Compliance Formats - Support Preparation (formerly Advance Compliance Reporting), visit the SAP Help Portal ([https://help.sap.com](https://help.sap.com)). On the initial page, enter: Compliance Formats - Support Preparation in the Search field. The results provide additional documentation details about Compliance Formats - Support Preparation.

With the introduction of scope item Document and Reporting Compliance (5XU), this scope item has been restructured. It now only contains content that does not require an additional license. To use advanced features as specified in the feature and scope description of SAP S/4HANA Cloud Public Edition, an additional license of either SAP S/4HANA Cloud for Advanced Compliance Reporting (discontinued) or its successor SAP Document and Reporting Compliance for SAP S/4HANA Cloud Public Edition is required. To enable the advanced features, please activate scope item 5XU and follow the corresponding instructions.

|  |
| --- |
| Note If your instance was already live before CE2111, we ensure continuity. The advanced features are still visible. |

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/1J2_S4CLD2602_BPD_EN_AE.docx) ). |

### System Access

| System | Details |
| --- | --- |
| System | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

Table 1: United Arab Emirates

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| General Ledger Accountant for United Arab Emirates | SAP_BR_GL_ACCOUNTANT_AE |  |  |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Package, you can use the following Package scenario data: Accounting.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Controlling Area | A000 |  |  |
| Cost Center | 33101101 |  |  |
| VAT Code | Use a VAT code for example: S2/S4 for Output or V2/V4 for Input. |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 2: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Must be run before this test script. |
| J59 - Accounts Receivable | Must be run before this test script.Ensure that invoices for customers and payments for the invoices are created.Chapter Bad Debt Write-Off has been executed. |

### Preliminary Steps

#### Assign Organization Unit

Purpose

In this activity, you assign an Organizational Unit such as company code to your ACR reports.

Prerequisite

An Organizational Unit such as a company code has already been created.

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
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Setting Up Your Compliance Reporting.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select | Select your reporting entity, for example:Reporting entity: <Reporting Entity> |  |  |
| 2 | Validity | In the Dialog Structure pane, double-click Set Validity of Organization Unit and choose a Valid From date.Note If no date exists, a new Valid From date can be entered by choosing New Entries and entering the date. | The Change View "Set Validity of Organization Unit ": Overview view is displayed. |  |
| 3 | Assign | In the Dialog Structure pane, double-click Assign Org. Units to a Reporting Entity and enter the following:Organization UnitFor example: COMPANYCODEVALUE: <your COMPANY CODE>Leading: Selected (there can only be one leading company code) |  |  |
| 4 | Save | Choose Save and then Exit.Note If using an Organizational Unit other than a Company Code, follow the previous steps to assign the required unit for your country-specific report. | The Organizational Unit is assigned and saved. |  |

#### Import Report Hierarchies for Cash Flow Indirect Method

Purpose

In this activity, you import the report hierarchies for cash flow indirect method.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). | The app opens. |  |
| 3 | Set Local Version | Choose Set Local Version.On the Set Local Version dialog box, select Utd. Arab Emir from the dropdown list and choose Set Local Version. | The country/region version is set to United Arab Emirates. |  |
| 4 | Configure Solution | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 5 | Enter Details | Make the following entries:Application Area: FinanceSub Application Area: General LedgerOn the Configuration Items list, select the row of the Item Name: Chart of Accounts. | The Configure Your Solution – Chart of Accounts item details view displays. |  |
| 6 | Configure | On the Configuration Steps list, for the Define Financial Statement Versions in Global Hierarchies row, choose Configure. | The Change View "Manage Global Hierarchies": Overview view displays. |  |
| 7 | Import Hierarchy | Choose Import Hierarchy. | The Import Hierarchy dialog box displays. |  |
| 8 | Enter Version Criteria | Make the following entries and choose OK:Source: Maintain Financial Statement VersionsFinancial Statement Version ID: <see note>Note Choose the field. In the Select: Financial Statement Version ID dialog box, in the FS Version field, enter C1AE and choose Go. Select the row of the entry to enter the information in the Financial Statement Version ID field. | The Create a Hierarchy Based On <C1AE> dialog box displays. |  |
| 9 | Create a Hierarchy | Make the following entries and choose Create:Type: Financial Statement Version (selected)Hierarchy ID: CFAEHierarchy Description: For example, Indirect Cash Flow Statement UAEChart of Account: YCOA (selected)Valid From: <Current date>Valid To: For example, 12/31/9999 | The system displays the The Hierarchy ID CFAE was successfully notification. The Manage Global Accounting Hierarchies view displays. |  |
| 10 | Open Details | Double-click the new hierarchy on the Hierarchy List. | A CFAE - Financial Statement Version details view displays. |  |
| 11 | Activate | Choose Activate. | The CFAE hierarchy is activated. |  |

SAP Central Business Configuration:

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Chart of Accounts | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Chart of Accounts.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The app opens. |  |
| 3 | Configure | On the Configuration Steps list, for the Define Financial Statement Versions in Global Hierarchies row, choose Configure. | The Change View "Manage Global Hierarchies": Overview view displays. |  |
| 4 | Import Hierarchy | Choose Import Hierarchy. | The Import Hierarchy dialog box displays. |  |
| 5 | Enter Version Criteria | Make the following entries and choose OK:Source: Maintain Financial Statement VersionsFinancial Statement Version ID: <see note>Note Choose the field. In the Select: Financial Statement Version ID dialog box, in the FS Version field, enter C1AE and choose Go. Select the row of the entry to enter the information in the Financial Statement Version ID field. | The Create a Hierarchy Based On <C1AE> dialog box displays. |  |
| 6 | Create a Hierarchy | Make the following entries and choose Create:Type: Financial Statement Version (selected)Hierarchy ID: CFAEHierarchy Description: For example, Indirect Cash Flow Statement UAEChart of Account: YCOA (selected)Valid From: <Current date>Valid To: For example, 12/31/9999 | The system displays the The Hierarchy ID CFAE was successfully notification. The Manage Global Accounting Hierarchies view displays. |  |
| 7 | Open Details | Double-click the new hierarchy on the Hierarchy List. | A CFAE - Financial Statement Version details view displays. |  |
| 8 | Activate | Choose Activate. | The CFAE hierarchy is activated. |  |

#### Setting Up Your Statutory Reporting for UAE

Purpose

In this activity, you set up the parameters for the statutory report of the UAE.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Your Solution (F1241). |  |  |
| 3 | Set Local Version | Choose Set Local Version.On the Set Local Version dialog box, select United Arab Emirates from the dropdown list and choose Set Local Version. | The country/region version is set to UAE. |  |
| 4 | Configure | Choose Configure Your Solution. | The Configure Your Solution: Realize Phase view displays. |  |
| 5 | Search Criteria | Make the following entries:Application Area: FinanceSub Application Area: Statutory ReportingOn the Configuration Items list, select the row of the Item Name: Basic setting. | The Configure Your Solution - Cross Country item details view displays. |  |
| 6 | Configure | On the Configuration Steps list, Setting Up Your Statutory Reporting, choose Configure. | The Change View "Define Compliance Reporting Entities": Overview view displays. |  |
| 7 | Assign | On the Rep Entity column, select AE_REP_ENT.On the Dialog Structure column, choose Assign Report Categories to Reporting Entity.In the results that display, select the following:Report Category ID: AE_CASHFLOW | The Report Category ID can be selected. |  |
| 8 | Select Parameters | In the left column, choose Enter Parameters Specific to Report Category. | The parameters list displays to the right of the view. |  |
| 9 | Enter and Save | In the Parameter Name list, locate G_FIN_STMNT_HIER_ID and enter CFAE as the Parameter Value. Locate G_LEDGER and make the following entry:Parameter Value: 0L (or other ledger value)Choose Save. | The Parameter Values are saved. The parameter value CFAE is assigned to parameter name: G_FIN_STMNT_HIER_ID. |  |

SAP Central Business Configuration:

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Basic Setting | Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Basic Setting.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Configure Your Solution - Cross Country item details view displays. |  |
| 3 | Configure | On the Configuration Steps list, Setting Up Your Statutory Reporting, choose Configure. | The Change View "Define Compliance Reporting Entities": Overview view displays. |  |
| 4 | Assign | On the Rep Entity column, select AE_REP_ENT.On the Dialog Structure column, choose Assign Report Categories to Reporting Entity.In the results that display, select the following:Report Category ID: AE_CASHFLOW | The Report Category ID can be selected. |  |
| 5 | Select Parameters | In the left column, choose Enter Parameters Specific to Report Category. | The parameters list displays to the right of the view. |  |
| 6 | Enter and Save | In the Parameter Name list, locate G_FIN_STMNT_HIER_ID and enter CFAE as the Parameter Value. Locate G_LEDGER and make the following entry:Parameter Value: 0L (or other ledger value)Choose Save. | The Parameter Values are saved. The parameter value CFAE is assigned to parameter name: G_FIN_STMNT_HIER_ID. |  |

## Overview Table

The scope items consist of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 3: United Arab Emirates

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Document and Reporting](#unique_11) [page ] 14 | General Ledger Accountant for United Arab Emirates | Manage Document and Reporting Compliance (F5218) | Report and file generate. |
| [Run Statutory Reports - UAE VAT Return](#unique_12) [page ] 15 | General Ledger Accountant for United Arab Emirates | Run Statutory Reports - United Arab Emirates GL Reporting (F1515_AE) | The report and file are generated. |
| [Run Statutory Reports - UAE - VAT - FAF Audit File](#unique_13) [page ] 18 | General Ledger Accountant for United Arab Emirates | Run Statutory Reports - United Arab Emirates GL Reporting (F1515_AE) | The report and file are generated. |
| [Run Statutory Reports – Utd.Arab Emir. Cash Flow Statement (Report)](#unique_14) [page ] 21 | General Ledger Accountant for United Arab Emirates | Run Statutory Reports (F1515) | You generated and viewed the report. |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Open the SAP Fiori App | Open Manage Document and Reporting Compliance (F5218). |  |  |
| 3 | Selection | In the Filters section, enter the following:Country/Region: Any country(ies)Report Name: Any report(s)Report Due Date: Date rangeIf needed, use any other available filter. | Based on your filtering criteria, progress bars of selected reports display in section Reporting Progress and a list of report will display in section Reports – Immediate Attention Required. |  |
| 4 | Group / Sort | In section Reporting Progress, grouping display can be changed by choosing any other available option in the drill-down menu.In section Reports – Immediate Attention Required, sorting display can be changed by choosing any other available option in the drill-down menu. |  |  |
| 5 | Size | Size of each section box can be changed by dragging any of the border or corner boxes. |  |  |
| 6 | Navigation | The following selections will open app Run Statutory Reports (F1515):Choose the header of either section Reporting Progress or Reports – Immediate Attention Required and all reports based on the filtering criteria will be chosen.Choose a bar from the graphic displayed in Reporting Progress and it will choose the reports belonging to the specific bar.Choose a specific report by selecting it from section Reports – Immediate Attention Required. | The app Run Statutory Reports (F1515) is executed and opens in a new window with the reports according to your selection. |  |
| 7 | Report Execution | To generate a report, please follow the instructions in the following chapters. |  |  |

### Run Statutory Reports - UAE VAT Return

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you prepare Statutory Reporting Framework for a VAT returns declaration. These steps provide a detailed procedure for running reports, reflecting the predefined scope of the solution.

Prerequisite

The report can only be executed when data is available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports - United Arab Emirates GL Reporting (F1515_AE). | The Run Statutory Reports - United Arab Emirates GL Reporting (F1515_AE) view displays. |  |
| 3 | Enter Details | Make the following entries:Report Name: AE_VAT_DCLReporting Entity Name: AE_REP_ENT |  |  |
| 4 | Display Statutory Report | Choose Go. | A Statutory Reports table displays. |  |
| 5 | Select Report | Select an UAE VAT Declaration report to run. | The report details view displays. |  |
| 6 | Skip Activity for Manage Tax Item | Under the Activities section, select the checkbox for the row of Manage Tax Items and choose the Skip Activity button.Confirm the dialog box by choosing Yes. | The Due Date Status status changes to Completed and the Activity Status changes to Skipped. |  |
| 7 | Select Activity | Under the Activities section, double-click the Advance VAT Return for Sales and Purchasing Tax for UAE. | The UAE VAT Declaration report details view displays. |  |
| 8 | New Run | Choose the New Run button from the bottom of the view. | A selection criteria dialog box displays. |  |
| 9 | Enter Criteria | Enter or verify the following data:Documents for Generation:<Select or Deselect PDF generation>Company Code: 3310Reporting Date: <Date range of the selected report>Request Refund: NoRun Options: Start a Short Run Now (Less than 3 Minutes)Tip When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later.and choose Run at the bottom of the view.For Correction phase, two more additional parameters would be required:Correction Reason: <Select from dropdown>Correction Date:<Date for correction> | A Run started notification displays and a new report generates. |  |
| 10 | Refresh Report | If the generated report shows the In Process status, choose the Refresh icon at the top of the view to change to Generated Successfully status. | The report status is Generated Successfully. |  |
| 11 | Select Report | Double-click the report from the Generated area. | A view of the report run displays. |  |
| 12 | Review Data | Review the data for the reporting date.When the review is completed, return to the UAE VAT Declaration view. | The Legal Reporting view of the UAE VAT Declaration displays. |  |
| 13 | Download the VAT report | From the Legal Reporting section, select the row with the PDF format and JSON format, and choose the Download button. | A JSON and PDF version (if generated) of the VAT declaration downloads. |  |
| 14 | Submit the VAT report | Choose Submit from the bottom of the view.Confirm the Do you really want to submit the selected report run to the authority? notification by choosing Yes. | A Status on report submissionnotification displays and the status is changed to Submission Initiated. |  |
| 15 | Redirection | Choose the Redirect from the bottom of the view.(If external authorization is required, the status will change to Redirection Required and the Redirect button will appear.) | A status on redirecting will appear and the page will redirect to EMARA Tax portal login page. |  |
| 16 | Tax Portal Authorization | Enter User ID and password on the tax portal page and click on Login | The page will redirect back to the Run screen |  |
| 17 | Submission Status | Choose the refresh icon. | If the submission has been successful, the status changes to Submission Accepted by Authority.The log contains the updated VAT return data received from FTA.Note Once the status is changed to Submission accepted by the Authority, no further changes, including new runs, can be applied to the report. |  |
| 18 | Verify Status | Choose the < (Back) button to return to the previous view. Verify that the report now appears under the Submitted section with a Report Run Status of Submission Accepted by the Authority. | Declaration for the reporting period is completed. |  |
| 19 | Post Tax Payable Activity | Choose the < (Back) button to return to the previous view. Under the Activities section, double-click the Post Tax Payable activity.Confirm the Do you want to change the status of the activity to "In Process"? notification by choosing Yes. | The Post Tax Payables view displays. |  |
| 20 | Create New Posting | Create a posting, adding the correct values. When entries are completed, choose Post from the bottom of the view. | The amount is posted to the corresponding accounts. |  |
| 21 | Set Activity to Completed | Return to the UAE VAT Declaration view. Under the Activities section, select the checkbox for the Post Tax Payable activity and choose the Set Completed button.Confirm the Are you sure you want to set the selected activity to "Completed"? notification by choosing Yes. | The Activity Status changes to Completed. |  |

### Run Statutory Reports - UAE - VAT - FAF Audit File

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you prepare Statutory Reporting Framework for a Federal tax authority Audit File (FAF). These steps provide a detailed procedure for running reports, reflecting the predefined scope of the solution.

Prerequisite

The report can only be executed when data is available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports - United Arab Emirates GL Reporting (F1515_AE). | The Run Statutory Reports - United Arab Emirates GL Reporting (F1515_AE) view displays. |  |
| 3 | Enter Details | Make the following entries:Report Name: AE_FAF_DCLReport Entity name: AE_REP_ENT |  |  |
| 4 | Display Statutory Report | Choose Go. | A Statutory Reports table displays. |  |
| 5 | Create Ad Hoc Report Task (Optional) | Note When no list of reports displays after completing the previous step, follow these instructions to create an ad hoc report task. If a report does appear after the previous step, skip this step.When no report appears, create an ad hoc report.Choose the Create (New Ad-Hoc Reporting Task) button.On the New Ad-hoc Reporting Task dialog box, enter the following:Report Name: AE_FAF_DCLReporting Entity: AE_REP_ENTDue Date: for example, <today's date>Reporting Period: <date range>Choose OK. | A Statutory Reports table displays. |  |
| 6 | Select Report to Submit | Double-click the UAE FAF Return report name from the table. | The UAE FAF Return view displays. |  |
| 7 | New Run | Choose New Run from the bottom of the view. | A selection criteria dialog box displays. |  |
| 8 | Enter Criteria | Enter or verify the following data:Company Code: 3310Posting Date: <Date range of the selected report>Run Options: Start a Short Run Now (Less than 3 Minutes)Tip When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later.and choose Run at the bottom of the view. | A Run started notification displays and a new report generates. |  |
| 9 | Refresh Report | If the generated report shows the In Process status, choose the Refresh icon at the top of the view to change to Generated Successfully status. | The report status is Generated Successfully. |  |
| 10 | Select Report | Double-click the report from the Generated area. | A view of the report run displays. |  |
| 11 | Open Document | Under the Legal Reporting section, double-click the UAE FAF Audit File document name. | The document displays. |  |
| 12 | Review Report | Expand the headers to review the report data.Verify the entries:Company Information TablePurchase Listing TableSupply Listing TableGeneral Ledger Table |  |  |
| 13 | Back | Choose < (Back) to return to the previous view. | The UAE FAF Return reporting view displays. |  |
| 14 | Analyze Subreports | Under the Legal Reporting section, for the UAE FAF Audit File row, choose the Analyze Data - Design Studio icon from the Action column.When complete with your analysis, return to the previous view and repeat this step for the other two items. | A view displays to analyze data in table or chart formats. |  |
| 15 | Back | Return to the previous view. | The UAE FAF Return reporting view displays. |  |
| 16 | Download | Under the Legal Reporting section, select the checkbox for the UAE FAF Audit File document name and then choose Download. | A report downloads that include three subreports generated for the reporting date:Journal Entry DetailsPurchase Tax ItemsSales Tax Items |  |
| 17 | Review Report | Choose the successfully generated report.Verify that the header section includes the correct company information.Verify the mapping of the source data to the fields in the reports. | Document is generated and reviewed. |  |

### Run Statutory Reports – Utd.Arab Emir. Cash Flow Statement (Report)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you generate a cash flow statement in a PDF format. The form is submitted, as one of the UAE statutory reports.

Procedure

| Test Step | Test Step Name | Instruction | Expected Result | Pass/ Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Run Statutory Reports (F1515). |  |  |
|  |  | If a report does not appear, create an ad hoc report. To do so, choose Create (New Ad-Hoc Reporting Task). | The New Ad-hoc Reporting Task dialog box is displayed. |  |
| 3 | Select Report | Make the following entries and choose Go:Reporting Entity Name: AE_REP_ENTReport Name: AE_CASHFLOW | Items display in the report result list by period, according to configuration. |  |
| 4 | New Run | Choose the statutory report for the period of reporting and choose the New Run button at the bottom of the view. | A new run starts. A selection criteria dialog box displays. |  |
| 5 | Run Report | Make or verify the following entries and choose Run:Company Code: 3310Posting Date: <Date range>, for example, 1/1/2019 to 12/31/2019Note If you are an authorized user, to display an Individual Number, choose Display Individual Number.Run Options: Use the default setting.Tip When you have a limited number of documents, Start a Short Run Now is the best choice for running the file generation immediately. When a larger amount of input data is used for the report generation, choose Start a Long Run Now. And when your preference is setting up a one-time, background job to generate a report from a large dataset, select Schedule a Run Later. | A Run Started notification is displayed. A new report displays in the Generated section of the report details view. |  |
| 6 | Refresh Status | If the new report shows an In process status, choose Refresh. | The Report Run Status is Generated Successfully.Cash Flow Statement Indirect Method Generated |  |
| 7 | Select Report | Select the newly generated report. | A report details view displays. |  |
| 8 | Open Report | From the Legal Reporting section, on the row of the document name, select the document and choose the document name. | The report details are displayed. A Cash flow view displays. |  |
| 9 | Excel | Drill down on the item information. Choose Export to Excel. |  |  |
| 10 | Analyze Data | In the Action column, choose Analyze Data-Design Studio. | The Data Studio view is displayed. |  |

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
- see-also :: [[03-financial-accounting-and-close/bp-cld-entpr-2608-account-master-data-for-ycoa-132-part-01]]
- see-also :: [[04-tax-and-statutory-reporting/document-and-reporting-compliance-5xu-test-script-sap-s-4hana-cloud-pu]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1J2_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 41,339 chars in the whole document
