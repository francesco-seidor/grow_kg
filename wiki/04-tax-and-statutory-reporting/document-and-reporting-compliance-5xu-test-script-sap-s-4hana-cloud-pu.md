---
id: 04-tax-and-statutory-reporting/document-and-reporting-compliance-5xu-test-script-sap-s-4hana-cloud-pu
title: "Document and Reporting Compliance (5XU) - Test Script, SAP S/4HANA Cloud Public Edition (5XU_S4CLD2608_BPD_EN_XX)"
description: "Test script for scope item 5XU Document and Reporting Compliance (S/4HANA Cloud 2608): eDocuments, statutory reports, email, approval workflow, consistency."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/document-and-reporting-compliance-framework]
aliases: [5XU_S4CLD2608_BPD_EN_XX]
keywords: [Document and Reporting Compliance Framework, document and reporting compliance, electronic documents, edocument cockpit, statutory reports, tax items, business partner email, approval workflow, draft report reconciliation, electronic document consistency]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5XU_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1130
topic: 04-tax-and-statutory-reporting/document-and-reporting-compliance-framework
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Document and Reporting Compliance (5XU) - Test Script, SAP S/4HANA Cloud Public Edition (5XU_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5XU_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Document and Reporting Compliance Framework** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Document and Reporting Compliance (5XU)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Document and Reporting Compliance (5XU) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232841268)

[2 Prerequisites 4](#_Toc232841269)

[2.1 System Access 4](#_Toc232841270)

[2.2 Roles 4](#_Toc232841271)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232841272)

[2.4 Business Conditions 6](#_Toc232841273)

[2.5 Preliminary Steps 7](#_Toc232841274)

[2.5.1 Activate Document and Reporting Compliance Features 7](#_Toc232841275)

[2.5.2 Maintain Business Users 8](#_Toc232841276)

[2.5.3 Activate Routine Checks and Detect Document Inconsistencies 9](#_Toc232841277)

[3 Overview Table 11](#_Toc232841278)

[4 Test Procedures 13](#_Toc232841279)

[4.1 Electronic Documents 13](#_Toc232841280)

[4.1.1 Manage Electronic Documents 13](#_Toc232841281)

[4.1.2 eDocument Cockpit 15](#_Toc232841282)

[4.2 Analyze, Preview, and Edit a Report 17](#_Toc232841283)

[4.3 Manage Tax Items for VAT and Withholding Taxes (Optional) 19](#_Toc232841284)

[4.4 Email for Business Partner Correspondence 22](#_Toc232841285)

[4.4.1 BRF+ Settings for Email Functionality 23](#_Toc232841286)

[4.4.2 Maintain Business Partner 27](#_Toc232841287)

[4.4.3 Generate Email 28](#_Toc232841288)

[4.5 Workflow 30](#_Toc232841289)

[4.5.1 Create Team 30](#_Toc232841290)

[4.5.2 Create Workflow 32](#_Toc232841291)

[4.5.3 Execute Workflow 34](#_Toc232841292)

[4.5.3.1 Request Approval 34](#_Toc232841293)

[4.5.3.2 Request Clarification 36](#_Toc232841294)

[4.5.3.3 First Approval 38](#_Toc232841295)

[4.5.3.4 Second Approval 40](#_Toc232841296)

[4.6 Reconcile Draft Reports 41](#_Toc232841297)

[4.7 Electronic Document Consistency 43](#_Toc232841298)

[4.7.1 Responsibility Management Functions 43](#_Toc232841299)

[4.7.2 Team Category Assignment 45](#_Toc232841300)

[4.7.3 Team Type 46](#_Toc232841301)

[4.7.4 Create Team 48](#_Toc232841302)

[4.7.5 Create Workflow 49](#_Toc232841303)

[4.7.6 Schedule Jobs for Electronic Document Consistency 51](#_Toc232841304)

[4.7.7 Electronic Document Consistency Validation Report 52](#_Toc232841305)

[4.7.8 Notification Processing 53](#_Toc232841306)

## Purpose

Overview

SAP Document and Reporting Compliance (formerly SAP S/4HANA Cloud for Advanced Compliance Reporting & SAP Document Compliance) allows a customer to comply with electronic invoicing (e-invoicing), electronic reporting (e-reporting), and statutory reporting obligations. With the activation of this scope item, you can enable and control the visibility of advanced features on a country or region level. To see a full list of the advanced features, check the latest version of the SAP S/4HANA Cloud Public Edition feature and scope description.

|  |
| --- |
| Note Some test procedure steps in local versions of Compliance Formats – Support Preparation (1J2) require activation of this scope item for full functionality. |

Additional Information on the SAP Help Portal

For more information, including descriptions of features for Document and Reporting Compliance for each country/region, see the [Local Versions](https://help.sap.com/viewer/60a09f68f2444ceca31dcac2e7017945/latest/en-US/546e6657290ba57ae10000000a4450e5.html) content on the [SAP Help Portal](https://help.sap.com). From there, navigate to Country/Region-Specific Functions > <country/region> > General Functions > Document and Reporting Compliance .

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| General Ledger Accountant(local) | SAP_BR_GL_ACCOUNTANT_<country>Note Replace <country> with your two-letter country code. | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Manager | SAP_BR_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable | SAP_BR_AP_MANAGER |  |
| Accounts Payable Manager for USA (or your country/region) | SAP_BR_AP_MANAGER for USA (or your country/region) | Accounts Payable | SAP_BR_AP_MANAGER |  |
| Billing Clerk | SAP_BR_BILLING_CLERK | Billing | SAP_BR_BILLING_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you've installed an SAP Best Practices Package, you can use the following Package scenario data: Accounting.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Country | <country> (for example, DE, US, or another country/region) |  | Use any country that is installed |
| Company Code | <company code> (for example, 1010, 1710, or another country/region company code) |  | Use any company code that is installed |
| Controlling Area | A000 |  |  |
| Chart of Accounts | YCOA |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master |
| BNE | Create Supplier Master |
| BNG | Create G/L Account and Cost Element |
| BNM | Create Cost Center and Cost Center Group |
| BNH | Create Profit Center |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | Must be run before this test script. |
| J59 - Accounts Receivable | Must be run before this test script. |
| J60 - Accounts Payable | Must be run before this test script.Ensure that invoices for vendors and payments for the invoices are created. |
| 1J2 - Compliance Formats – Support Preparation | Generate compliance reports.Note Some test procedure steps in local versions of Compliance Formats – Support Preparation (1J2) require activation of this scope item for full functionality. |

### Preliminary Steps

#### Activate Document and Reporting Compliance Features

Use

In this activity, you activate the document and reporting compliance features for your country/region.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Application Platform and Infrastructure

Sub Application Area: Legal Compliance

1. For the row with Item Name of General Settings for Document and Reporting Compliance, choose Details (>).
2. For the Activate Document and Reporting Compliance Features row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Document and Reporting Compliance Features.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Enter Details | Make the following entry and press Enter:Country/Region Key: <two-letter country/region key>Note The Country/Region Name field is populated when you press Enter. | The country/region information is entered. |  |
| 3 | Save | Choose Save. | The document and reporting compliance features are activated for your selected country. |  |

#### Maintain Business Users

Purpose

In this activity, you assign the SAP_BR_MANAGER business role ID to a business user to be able to use and display the My Inbox - All Items (F0862) app.

Prerequisite

You created business users.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Users (F1303). | The Maintain Business Users view displays. |  |
| 3 | Search | Make the follwing entries and choose Go :User Name: GL_ACCOUNTANT_<country>Note Replace <country> with your two-letter country code. | Your selection is displayed. |  |
| 4 | Select | Choose the displayed entry. | Details of the user are displayed. |  |
| 5 | Person ID | In the General > Personal Data section, make a note of the Person ID. This value is used later in the [Create Team](#unique_9) [page ] 30 process step (in the Team Owners and Team Members rows). |  |  |
| 6 | Assign | In the Assigned Business Roles section, choose Add. | The business role is assigned. |  |
| 7 | Assign | Search for and select SAP_BR_MANAGER and choose OK. |  |  |
| 8 | Repeat | Repeat steps 3 to 6 for other users, such as:AP_MANAGERGL_ACCOUNTANTNote Any available user can be used. |  |  |
| 9 | Save | Choose Save. |  |  |

#### Activate Routine Checks and Detect Document Inconsistencies

Purpose

To execute the Electronic Document Consistency Validation Report, you must configure your system for a specific country/region/region to perform routine checks and detect document inconsistencies.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Application Platform and Infrastructure

Sub Application Area: Legal Compliance

1. For the row with Item Name of General Settings for Consistency Check, choose Details (>).
2. For each of the following steps, choose Configure.
    - Enable Consistency Checks for Company Codes
    - Assign Journal Entry Types to Comparison Types
    - Define Tolerance Limits for Amount Mismatch
3. Continue with the procedure in the note at the bottom of this topic.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activities:
    - Enable Consistency Checks for Company Codes
    - Assign Journal Entry Types to Comparison Types
    - Define Tolerance Limits for Amount Mismatch
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following note.

|  |
| --- |
| Note Follow the procedures outlined in the [Configuration Options](https://help.sap.com/docs/SAP_S4HANA_CLOUD/71af4585db6d4904b1724730f3776c9b/dbf19e07cddf4a5d93e60c47d0b6ab28.html?version=LATEST) topic on the SAP Help Portal. |

## Overview Table

The scope item consists of several process steps provided in the following table.

Table 1: Electronic Documents

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Electronic Documents](#unique_12) [page ] 13 | Billing Clerk | Manage Electronic Documents (F4306) | You monitored and processed eDocuments. |
| [eDocument Cockpit](#unique_13) [page ] 15 | Billing Clerk | eDocument Cockpit (EDOC_COCKPIT) | You created, displayed, submittted, or monitored eDocuments. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Analyze, Preview, and Edit a Report](#unique_14) [page ] 17 | General Ledger Accountant for your country/region | Run Statutory Reports (F1515) | You previewed or edited a report. |
| [Manage Tax Items for VAT and Withholding Taxes (Optional)](#unique_15) [page ] 19 | General Ledger Accountant for your country/region | Run Statutory Reports (F1515) | You moved tax items between reporting periods. |

Table 2: Email for Business Parter Correspondence

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [BRF+ Settings for Email Functionality](#unique_16) [page ] 23 | Administrator | Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) | You set up the BRF+ settings for email functionality. |
| [Maintain Business Partner](#unique_17) [page ] 27 | Master Data Specialist - Business Partner Data | Manage Supplier Master Data (F1053A) | You maintained the business partner. |
| [Generate Email](#unique_18) [page ] 28 | Accounts Payable Manager for USA (or for your country/region) | Run Statutory Reports (F1515) | You generated the email. |

Table 3: Workflow

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Team](#unique_9) [page ] 30 | Business Process Specialist | Manage Teams and Responsibilities (F2412) | You created the team. |
| [Create Workflow](#unique_19) [page ] 32 | Configuration Expert - Business Process Configuration | Manage Workflows - Statutory Reporting (F5110) | You created the workflow. |
| Execute Workflow |  |  |  |
| [Request Approval](#unique_20) [page ] 34 | General Ledger Accountant role for your country/region | Run Statutory Reports (F1515) | You sent the request for approval. |
| [Request Clarification](#unique_21) [page ] 36 | General Ledger Accountant | My Inbox - All Items (F0862) | Clarification is answered and sent for approval. |
| [First Approval](#unique_22) [page ] 38 | General Ledger Accountant | My Inbox - All Items (F0862) | The first approver approves the report. |
| [Second Approval](#unique_23) [page ] 40 | Accounts Payable Manager | My Inbox - All Items (F0862) | The second approver approves the report. |

Table 4: Reconcile Draft Reports

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Reconcile Draft Reports](#unique_24) [page ] 41 | General Ledger Accountant for your country/region | Run Statutory Reports (F1515) | You reconciled the draft report. |

Table 5: Electronic Document Consistency

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Responsibility Management Functions](#unique_25) [page ] 43 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | You define the responsibility management functions . |
| [Team Category Assignment](#unique_26) [page ] 45 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | You assigned a team category to a function profile. |
| [Team Type](#unique_27) [page ] 46 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | You defined a team type associated with a team category. |
| [Create Team](#unique_28) [page ] 48 | Business Process Specialist. | Manage Teams and Responsibilities (F2412) | You defined a team member as a notification recipient. |
| [Create Workflow](#unique_29) [page ] 49 | Configuration Expert - Business Process Configuration | Manage Workflows (F8647) | You defined and activated a workflow. |
| [Schedule Jobs for Electronic Document Consistency](#unique_30) [page ] 51 | Billing Clerk | Schedule Jobs for Electronic Document Consistency (F7494) | You scheduled a job to execute the validation report. |
| [Electronic Document Consistency Validation Report](#unique_31) [page ] 52 | Billing Clerk | Resolve Electronic Document Inconsistencies (F7043) | You reviewed the report. |
| [Notification Processing](#unique_32) [page ] 53 | Billing Clerk | My Inbox - All Items (F0862) | You processed the notifications. |

|  |
| --- |
| Note The activation of SAP Document and Reporting Compliance also enables a list of value-added features that support, streamline, and automate the end-to-end process from e-documents to statutory reporting (for example, monitoring and correction of e-documents, manual adjustments for statutory reports via Manage Tax Items, embedded analytics, and so on).These can be tested upon activation of the corresponding country/region configurations. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Electronic Documents

For more information, including descriptions of features for Document and Reporting Compliance for each country, see the [Local Versions](https://help.sap.com/viewer/60a09f68f2444ceca31dcac2e7017945/latest/en-US/546e6657290ba57ae10000000a4450e5.html) > <country/region> > General Functions > Document and Reporting Compliance .

#### Manage Electronic Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can monitor and process electronic documents in a simple and user-friendly way.

For information about features for the Manage Electronic Documents (F4306) app and the supported countries and processes, see the [SAP Help Portal](https://help.sap.com/viewer/ae0b823738ee4227b7ec12cc4fbf1b4c/latest/en-US/054224c8887b459ca1adf2b8b67d9154.html) and review chapters Supported Tasks by Country/Region and Frequently Asked Questions.

|  |
| --- |
| Note If your country/region process is not supported, use the procedure in the eDocument Cockpit section. |

Prerequisites

You executed the preliminary steps in this test script.

You execute the preliminary steps for Electronic Invoicing from the Accounts Receivable (J59) test script for your country. This procedure may differ for each country/region and may only be applicable to some countries/regions. If your country/region doesn’t have electronic invoicing steps in the Accounts Receivable (J59) test script, ignore this specific prerequisite.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open Manage Electronic Documents (F4306). | The Processes section displays a list of processes per country/region with statistical information such as number of documents and status overview. |  |
| 3 | Filter | In the Filters section, make entries to finetune your selection, for example:Company Code: <Company Code>eDocument Type: <eDocument Type>Creation Date: <Choose any value>Posting Date: <Choose any date(s)>Note To display only the processes of a particular status, choose any of the status buttons. | Results are displayed based on filtering criteria. |  |
| 4 | Selection | In the Processes section, choose a process. | A new Document List section displays showing a list of eDocuments with status. |  |
| 5 | Navigation | Note The statuses are displayed in two location on the view. One location is next to the view’s title. The other location is below that, just above the data table.To get more information, choose a Status tag (next to the view’s title). A small dialog displays the bar charts with each status subtype.To filter the results in the data table, select a status from the options just above the data table. You can also use the dropdowns for each status to filter to a specific status subtype.Choose All Documents to display all results again.Choose Chart View or Table View to change how the data is displayed. | The Document List section is updated. |  |
| 6 | Error Analysis | From the status tags next to the view’s title, choose Error Go to Error Analysis.Note You can choose from several actions. | Information for analyzing errors with electronic documents is displayed. |  |
| 7 | Back | Choose Back. |  |  |
| 8 | Details | For an eDocument, choose Details (>).Several tabs are available with details.From the Logs tab, you can also choose Go to Error Analysis to analyze the errors. | Document details are displayed in a new window. |  |
| 9 | Back | Choose Back. |  |  |
| 10 | Actions | Select the checkbox for a document row.Depending on the eDocument type and status, different actions are available.Note For a Created status, you can Submit, Cancel, Export File, or Display File. For an Accepted status, you can Export File or Display File.Check the available actions for other statuses. | Different actions are available depending on each eDocument type and status.Actions are executed according to chosen action. |  |

#### eDocument Cockpit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you use the eDocument Cockpit to do the following:

- Display eDocuments that are created when the source documents are created in their source applications
- Submit eDocuments in the required XML format to the tax authorities or to your business partners
- Create and submit eDocuments that for any reason couldn't be created upon source document creation
- Monitor the status of the eDocuments and perform subsequent actions on them

|  |
| --- |
| Note For more information about features, see the application help for eDocuments (go to the SAP Help Portal and search for eDocument for your country or region). |

Prerequisites

You executed the preliminary steps in this test script.

You executed the preliminary Steps for Electronic Invoicing from the Accounts Receivable (J59) test script for your country/region. This procedure may differ for each country/region and may only be applicable to some countries/regions. If your country/region doesn’t have electronic invoicing steps in the Accounts Receivable (J59) test script, ignore this specific prerequisite.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the App | Open eDocument Cockpit (EDOC_COCKPIT). |  |  |
| 3 | Select eInvoice Document | Make the following entries:Source Document: <Invoice or Document number>Note You can also search for your invoice. In the Results Overview section, expand your country/region to display your country's/region's eInvoice or eDocument. |  |  |
| 4 | Submit eInvoice | Select the row and choose Submit.Note The submission of the eDocument requires a connection to SAP BTP. | The eDocument status displays the message Action successfully executed: SUBMIT. |  |
| 5 | Review status | Review the eDocument status. | The possible statuses of submitted eDocuments are:Accepted by receiving Access PointReceived by Access PointError at Sending Access PointSending RequestedReceived by Access PointError at Receiving Access Point |  |
| 6 | Display eDocument | Select the row for an eDocument with Accepted by receiving Access Point status.Choose Display > Display/Preview XML . | The eDocument is shown in XML format. |  |
| 7 | Display Source Document | Select the row of an eDocument and choose Go to > Source Document . | A view displays the original transaction that generated the eDocument (source document). |  |
| 8 | Back | Choose Exit. |  |  |
| 9 | Review History of eDocument | To review the eDocument history, choose Go to > History . | The view displays the last process steps and statuses from selected eDocument. |  |
| 10 | Back | Choose Back at the bottom of the view to return to the previous view. |  |  |
| 11 | Review Application Log | Choose Go to > Application Log . | If there are no errors, a No Application Log found for the selected eDocument notification displays at the bottom of the view.If there are errors, an Application Log dialog box displays with information about the error. Review the message and choose Continue (Enter) to close the dialog box. |  |
| 12 | Review Interface Log | Choose Go to > Interface Log . | If you encounter errors, a dialog box displays information about the error. Review the message and choose Continue to close the dialog box. |  |
| 13 | Cancel eDocument | To cancel an eDocument, select the row of an eDocument with Created status and choose More > Cancel eDocument . | The status of eDocument changes to eDocument Cancelled and the status icon turns green. |  |
| 14 | Delete eDocument | To delete an eDocument, choose a row from the list with a Created status.Select an eDocument with Created status and choose More > Delete eDocument . | The system displays a Number of eDocuments that have been deleted: 1 notification. |  |

### Analyze, Preview, and Edit a Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, after a report is successfully generated, you can:

- Preview - Preview a report in human-readable format
- Edit - Make manual changes to the document data after the document has been generated, and before you submit it to the tax authorities

|  |
| --- |
| Note This procedure is written with the assumption that you're working with an Advance VAT Return report for Germany (DE_VAT_ADV_RTN). If you're using a different report for a different country/region, the steps may be different.For more information, including descriptions of features for Document and Reporting Compliance for each country, see the [Local Versions](https://help.sap.com/viewer/60a09f68f2444ceca31dcac2e7017945/latest/en-US/546e6657290ba57ae10000000a4450e5.html) → <geographical region> → <country/region> → Cross-Application Functions → Document and Reporting Compliance. |

Prerequisite

You executed the preliminary steps in this test script.

You executed prerequisites and successfully generated a report from the Compliance Formats – Support Preparation (1J2) test script (for example, an Advanced VAT return report or another report for your country/region).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a local General Ledger Accountant. |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports (F1515). | The Run Compliance Reports view is displayed. |  |
| 3 | Filter | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name: <Any previously generated report> (for example, an Advanced VAT Return report or another report for your country/region)Note Follow instructions from the Compliance Formats – Support Preparation (1J2) test script if you haven't executed and generated a report yet. | A list of Reports display. |  |
| 4 | Selection | In the Activities section, choose the Prepare Advance VAT Return (Germany).Note This procedure is written with the assumption that you're working with an Advance VAT Return report for Germany (DE_VAT_ADV_RTN). If you're using a different report, the steps may be different. |  |  |
| 5 | Choose report | In the Runs section, choose a successfully generated report.Note For some countries/regions, the Preview pane may show results that require you to click a link to view. Click the link to open a pane to the right with more details. |  |  |
| 6 | Analysis | In the Preview report, on the Legal Reporting tab, in the Document Name column, choose Analyze Data.You can drag and drop Dimensions into the Columns or Rows panes to customize the displayed data. |  |  |
| 7 | Back | Go back to the generated report. |  |  |
| 8 | Preview | On the Legal Reporting tab, in the Document Name column, choose the document name. | A detailed preview of the report is displayed. You can expand or collapse different part of the report. |  |
| 9 | Edit | In the Preview report, choose Edit to make changes.After finishing, choose Save and Regenerate.To undo changes, choose Reset. | Changes are saved and report regenerated.When you regenerate a document, associated documents are regenerated at the same time. |  |

### Manage Tax Items for VAT and Withholding Taxes (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can move tax items between reporting periods by changing the tax reporting date. The system retrieves the documents based on the parameters from the reporting task of advanced compliance reporting or based on the filter values provided in the Manage Tax Items view. The selection of the tax items is based on the tax reporting date field. However, if the tax reporting date isn't available, the system considers the posting date.

|  |
| --- |
| Caution Values given below are only examples. Use values appropriate for your country or region.This activity may not be available for all reports and countries. |

Prerequisite

The report can only be executed when data is available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | For VAT, log on to the SAP Fiori launchpad as a General Ledger Accountant for your country/region.For withholding taxes, use Accounts Payable Manager for your country/region. |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports (F1515). | The Run Advanced Compliance Reports view displays. |  |
| 3 | Enter Details | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name:<report for your country>, for example, an Advance VAT Return or Withholding Tax report for your country or region | A list of Advanced Compliance Reportsdisplay. |  |
| 4 | Select Report to Submit | For the report you want to submit, choose Details (>). | The Advance VAT Return view for the compliance report is displayed. |  |
| 5 | Manage Tax Items (optional) | In the Activities section, depending on the report you want to execute, double-click Manage Tax Items or Manage Withholding Tax Items. | The Confirmation dialog box is displayed. |  |
| 6 | Confirm Status Change | For the Do you want to change the status of the activity to "In Process" notification, choose Yes.Note If all tax items are included in the report, the following steps for managing tax items are optional.If you don't want to execute this activity, you can set the status to Skip or Completed. | The Manage Tax Items for Legal Reporting view displays. |  |
| 7 | Display Tax Items List | Verify the following entries:Company Code: <company code>Reporting Date: <reporting date range for selected period>, for example, 01/01/2021 - 05/31/2021If the tax items table isn't automatically loaded, choose Go. | A list of tax items displays for the selected period.Three tabs display next to Tax Items:All: All tax items in the current reporting period are displayed.Included: Any items included for the current period are displayed.Excluded: Any items excluded from the current period are displayed.By default, the All tab is selected. |  |
| 8 | Personalize Settings (optional) | Choose the Gear button. | The Define Column Properties dialog box is displayed. |  |
| 9 |  | Select or deselect your required columns and choose OK to confirm the selection. | The view displays only the columns you selected. |  |
| 10 | Display Tax Item Details (optional) | From the Tax Items list, select any tax item. | A Display Document: Data Entry View displays with details about the corresponding accounting document. |  |
| 11 | Exclude a Tax Item | When you complete your review, return to the Manage Tax Items for Legal Reporting or the Manage Withholding Tax Items view.With the All tab selected, exclude a Tax Item by choosing the switch in the Document Status column. | An Exclude Document dialog box displays. |  |
| 12 | Define Exclusion | Enter the tax reporting date for excluding the item.Note The date entered must be outside the selected reporting period. | The Document Status for the tax item changes to Excluded (Red). |  |
| 13 | Save | Choose Save. | The Warning dialog box displays the Changing the tax reporting date will impact reporting of the tax item in all associated reports. Are you sure you want to continue? Notification. |  |
| 14 | Confirm | Choose Yes to confirm. | The excluded document is saved. |  |
| 15 | Verify the Exclusion | Choose the Excluded tab to verify that the excluded item displays the correct exclusion date in the Tax Reporting column. | The recently excluded tax item has the correct exclusion date. |  |
| 16 | Repeat (optional) | Choose the All tab and repeat steps 8–15 to exclude additional tax items. | Additional tax items are excluded. |  |
| 17 | Case 1: Revert Excluded Tax Items | Choose the All tab.In the Tax Items list, choose the Excluded (Red) document status switch to revert the status to Included. | The Include document dialog box displays. |  |
| 18 | Revert to Current Period | Choose the Tax Reporting date for the current period. Choose Continue to close the dialog box.Choose Save.Choose Yes when the system displays the Changing the tax reporting date will impact the reporting of the tax items in all associated reports. Do you wish to Continue? notification. | The selected tax item is included in the current list and moves from the Excluded to the Included list. |  |
| 19 | Verify the Inclusion | Choose the Included tab to verify that the item displays the correct inclusion date in the Tax Reporting Date column. | The tax items have the correct inclusion date. |  |
| 20 | Case 2: Include Tax Items from Another Reporting Period | From the All tab, choose the + (Add) button.On the Warning dialog box, choose Yes. | The Select Document for inclusion dialog box displays. |  |
| 21 | Choose the Reporting Period | Make the following entries and choose Go:Company Code: <company code>Reporting Date: <date range> | A list of tax items displays. A green box displays next to tax items to include. Any items displaying a red box are already excluded. Any items displaying a white box are already reported. |  |
| 22 | Select Items to Include | Select the items to add and choose Save and Include. | A confirmation dialog box displays. |  |
| 23 | Include Items in Current Period | Choose Yes to confirm.In the Include document dialog box, enter the Tax Reporting date for the current period and choose Continue. | A dialog box displays. |  |
| 24 | Confirm the Selection | Choose Save.Choose Yes to The item(s) should be included in the current list notification. | The Tax Items list is updated. The additional list is added to the Included tab. |  |
| 25 | Select Activity | Return to the Advance VAT Return or Withholding Tax view.In the Activities section, select the checkbox for the Manage Tax Items or the Manage Withholding Tax Items row and choose Set Completed. | The Set Completed dialog box displays. |  |
| 26 | Set Completed | Confirm the Are you sure you want to set the selected activity to "Completed" notification by choosing Yes. | The Manage Tax Items or the Manage Withholding Tax Items activity displays a Completed status. |  |

### Email for Business Partner Correspondence

Purpose

In this section, you make the necessary settings to trigger an email directly to a business partner when a report file is created per instructions in the Compliance Formats – Support Preparation (1J2) test script.

#### BRF+ Settings for Email Functionality

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you configure the BRF+ settings for email functionality.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination view is displayed. |  |
| 3 | Output TYpe | In the Select Business Rules section, choose:Show Rules for: Advanced Compliance ReportingDetermination Step: Output Type | Details are displayed in the Maintain Business Rules section. |  |
| 3 | Edit | Choose Edit. |  |  |
| 4 | Insert New Row | Under Table Contents, choose + (Insert New Row). |  |  |
| 5 | Add Rules | Make the following entries and choose OK:Output type: ACCT_WHTDispatch Time: 1 (immediately)Note To make these entries, choose ... or choose Direct Value Input from the dropdown in each field. |  |  |
| 6 | Activate | Choose Activate. | Rules are activated. |  |
| 7 | Receiver | In the Select Business Rules section, choose:Show Rules for: Advanced Compliance ReportingDetermination Step: Receiver | Details are displayed in the Maintain Business Rules section. |  |
| 8 | Edit | Choose Edit. |  |  |
| 9 | Insert New Row | Under Table Contents, choose + (Insert New Row). |  |  |
| 10 | Add Rules | Make the following entries and choose OK:Output type: ACCT_WHTReport ID: <enter the report ID for which you want to enable correspondence>, for example, US_WHT_1099_MISCNote The report ID value is provided only as an example. Your actual report ID can be different.Role: <enter the role per the report documentation (for example, BP)>Exclusive Indicator: X (True)Note To make these entries, choose ... or choose Direct Value Input from the dropdown in each field. |  |  |
| 11 | Activate | Choose Activate. | Rules are activated. |  |
| 12 | Channel | In the Select Business Rules section, choose:Show Rules for: Advanced Compliance ReportingDetermination Step: Channel | Details are displayed in the Maintain Business Rules section. |  |
| 13 | Edit | Choose Edit. |  |  |
| 14 | Remove Existing Row and Insert New Row | Under Table Contents, since the output channel does not need be Print, delete the row. To do so, select the entry with the following values and choose Remove Row:Output type: ACCT_WHTChannel: PRINT (Printout)Exclusive Indicator: - (true)Choose Insert New Row. |  |  |
| 15 | Add Rules | Make the following entries and choose OK:Output Type: ACCT_WHTRole: BP (after adding BP, add new entries for T1, T3, and UT)Channel: choose the expression Channel_determination()Note To find the expression easily using search, use Application Name of OPD_SRF_REPRUN.Exclusive Indicator: X (True)Note To make these entries, choose ... or choose Direct Value Input from the dropdown in each field. |  |  |
| 16 | Activate | Choose Activate. | Rules are activated. |  |
| 17 | Printer Settings | In the Select Business Rules section, choose:Show Rules for: Advanced Compliance ReportingDetermination Step: Printer Settings | Details are displayed in the Maintain Business Rules section. |  |
| 18 | Edit | Choose Edit. |  |  |
| 19 | Insert New Row | Under Table Contents, choose + (Insert New Row). |  |  |
| 20 | Add Rules | Make the following entries and choose OK:Output type: ACCT_WHTPrint Queue: <print queue defined in your system>, for example, QUEUE_PAYM_ADVNumber of Copies: 1Note To make these entries, choose ... or choose Direct Value Input from the dropdown in each field. |  |  |
| 21 | Activate | Choose Activate. | Rules are activated. |  |
| 22 | Email Settings | In the Select Business Rules section, choose:Show Rules for: Advanced Compliance ReportingDetermination Step: Email settings | Details are displayed in the Maintain Business Rules section. |  |
| 23 | Edit | Choose Edit. |  |  |
| 24 | Insert New Row | Under Table Contents, choose + (Insert New Row). |  |  |
| 25 | Add Rules | Make the following entries and choose OK:Output type: ACCT_WHTSender Email: <sender email address>Email Template: SRF_DEF_CORRSP_EMAIL_TEMPLATENote To make these entries, choose ... or choose Direct Value Input from the dropdown in each field. |  |  |
| 26 | Activate | Choose Activate. | Rules are activated. |  |
| 27 | Output Relevance | In the Select Business Rules section, choose:Show Rules for: Advanced Compliance ReportingDetermination Step: Output Relevance | Details are displayed in the Maintain Business Rules section. |  |
| 28 | Edit | Choose Edit. |  |  |
| 29 | Insert New Row | Under Table Contents, choose + (Insert New Row). |  |  |
| 30 | Add Rules | Make the following entries and choose OK:Output type: ACCT_WHTRelevance Indicator: X(True)Note To make these entries, choose ... or choose Direct Value Input from the dropdown in each field. |  |  |
| 31 | Activate | Choose Activate. | Rules are activated. |  |
| 32 | Form Template | In the Select Business Rules section, choose:Show Rules for: Advanced Compliance ReportingDetermination Step: Form Template | Details are displayed in the Maintain Business Rules section. |  |
| 33 | Edit | Choose Edit. |  |  |
| 34 | Insert New Row | Under Table Contents, choose + (Insert New Row). |  |  |
| 35 | Add Rules | Make the following entries and choose OK:Output type: ACCT_WHTForm Template: <from the dropdown, select context. From context, select Form>Form Language: <language>, for example, E (English)Note To make these entries, choose ... or choose Direct Value Input from the dropdown in each field. |  |  |
| 36 | Activate | Choose Activate. | Rules are activated. |  |

#### Maintain Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

Vendor master records are used in the Accounting and Purchasing components.

In this activity, you maintain the address for email usage.

Prerequisites

The BRF+ settings for email functionality are defined.

The business partner exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Supplier Master Data (F1053A). | The Supplier Master view displays. |  |
| 3 | Select Roles and Supplier | Select the following and choose Go:Roles: Supplier (Fin.Accounting), SupplierBusiness Partner: <business partner number> | The Business Partner displays in the worklist. |  |
| 4 | Choose BP | For the business partner you want to update, choose Details (>). | The business partner details are displayed. |  |
| 5 | Edit Supplier | Choose Edit. |  |  |
| 6 | Address | Choose the Address > Address Details tab. |  |  |
| 7 | Address Details | Select an existing address, then choose Details (>). |  |  |
| 8 | Email | Choose the Communication tab.Make the following entry and choose Apply:Preferred Communication: E-MailChoose the Communication > Email tab.Choose Create.Make the following entries and choose Apply:Email: <email address> |  |  |
| 9 | Address Usages | Choose the Address Usages tab.Choose Create.Make the following entries and choose Apply:Valid From: <first day of reporting year>, for example, 01/01/2022Valid To: <end of year date> (the validity of the address must be for the full duration of the reporting period)Address Type: GCO_TAX (Document & Reporting Compliance Address) |  |  |
| 10 | Save | Choose Save. | Changes are saved. |  |

#### Generate Email

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you send a successfully generated report via email.

This procedure is written with the assumption that you are working with a USA Withholding Tax - 1099 MISC (US_WHT_1099MISC). If you are using a different report for a different country, some steps may be different so review the corresponding country test script.

|  |
| --- |
| Note The Business Partner email correspondence functionality is required when there is a need to provide details to the Business Partner about the details of the transaction with them (such as Withholding Taxes). On the other hand, in VAT reports, there is no such requirement. |

Prerequisites

You executed the preliminary steps.

You executed the BRF+ Settings for Email Functionality.

You maintained the Business Partner.

You have executed prerequisites and successfully generated a report from the Compliance Formats – Support Preparation (1J2) for USA test script (for example, US_WHT_1099MISC report or Withholding Tax report for your country).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Manager for USA (or the country/region report to be generated).Note If you are using a different country/region than USA, the steps in this procedure will be different. |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports (F1515). | The Run Advanced Compliance Reports view displays. |  |
| 3 | Enter Details | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name: <Any previously generated report> (for example, US_WHT_1099MISC or another Withholding Tax report for your country).Note Follow instructions from the Compliance Formats – Support Preparation (1J2) test script if you haven't executed and generated a report yet. | A list of Advanced Compliance Reports display. |  |
| 4 | Select Report | Choose a report (for example, USA Withholding Tax - 1099 MISC). |  |  |
| 5 | Generated Report | In the Runs section, choose and review the details of a Generated Successfully report. |  |  |
| 6 | Correspondence | In Business Partner Reporting > Partner Correspondence, choose a form to see the details. |  |  |
| 7 | Email | Choose Show More per Row to display more details about output details and look for Channel Email. |  |  |
| 8 | Options | Choose the output with Channel email. Depending on the Status, there are options available to choose from, such as Send Output, Duplicate, Retry, or Set to Complete.To display the form, choose:Display: < PDF >To view email sender, receiver and others choose:Details: < Output Details > |  |  |

### Workflow

Purpose

The workflow is a general function that allows you to define condition-based workflows for approval processes. The workflow for advanced compliance reporting allows you to define one-step or multistep approval processes for your reporting scenarios. Approvers can then approve or reject corresponding work items in the My Inbox - All Items (F0862) app.

For more information, see the help documentation for [workflow](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4de200b26d5d42bbacae69c6bf6b9923/6eeb8b57e2fe41a2993c0761a0a1d5fe.html) in Advance Compliance Reporting.

Prerequisite

You've executed the [Business Conditions](#unique_6) [page ] 6 and Preliminary Steps.

#### Create Team

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a team that uniquely identifies the approvers in runtime based on predelivered conditions.

Prerequisites

You've executed the [Business Conditions](#unique_6) [page ] 6 and Preliminary Steps.

Business users are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Open the SAP Fiori App | Open Manage Teams and Responsibilities (F2412).Note If you see several apps with different subtitles (such as Procurement), you can open any of them. When it opens, change the Category field to SRF (Advance Compliance Reporting) and choose Go to display the available teams for the SRF category. |  |  |
| 3 | Create | Choose Create. | The Team view displays. |  |
| 4 | General Information | In section General Information make the following entries:Name: <Any name>Global ID: <Keep same as Name field>Description: <Any description>Type: SRFTTStatus: Enabled |  |  |
| 5 | Responsibility Definitions | In the Responsibility Definitions section, make the following entry:Country: <Any country> (for example, DE, US, or another country/region) |  |  |
| 6 | Team Owners | In the Team Owners section, choose Create.Select a user:Business Partner: <person ID> (see note)Note For example, if you want to use GL_ACCOUNTANT_DE, enter the Person ID from the [Maintain Business Users](#unique_8) [page ] 8 preliminary step (Person ID row). For other countries/regions, follow that process for your desired role. |  |  |
| 7 | Team Members | In the Team Members, section, choose Create. Select the users who are the approvers and choose OK:Business Partner: <person ID> (see note)Note For example, if you want to use GL_ACCOUNTANT, enter the Person ID from the [Maintain Business Users](#unique_8) [page ] 8 preliminary step (Person ID row). For other countries/regions, follow that process for your desired role.Business Partner: <person ID> (see note)Note For example, if you want to use AP_MANAGER, enter the Person ID from the [Maintain Business Users](#unique_8) [page ] 8 preliminary step (Person ID row). For other countries/regions, follow that process for your desired role.In the Functions column, assign a function for each approver (BP):BP GLAccountant: General Ledger AccountantBP ApManager: Compliance Manager |  |  |
| 8 | Save | Choose Save. | The team is created. |  |

#### Create Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define and activate a workflow for approval processes of your reporting scenarios.

Prerequisite

A team has been created and responsibilities assigned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Open the SAP Fiori App | Open Manage Workflows - Statutory Reporting (F5110). | The Manage Workflows view displays. |  |
| 3 | Create | Choose Create. | The New Workflow view displays. |  |
| 4 | Header | In section Header make the following entry:Workflow Name: <Any name> |  |  |
| 5 | Properties | In the Properties section, make the following entries:Description: <Any description>Valid from: <Any date, for example 01/01/2020>Valid To: <Any date + 2 year> |  |  |
| 6 | Start Conditions | In the Start Conditions section, make the following entries:Country: <two-letter country/region code> (for example, DE, US, or another country/region) |  |  |
| 7 | Steps | In the Steps section, choose Create.In the Header section, enter the following:Step Name: <Any description>Step Name: Approve ReportIn Recipients, enter the following:Role: General Ledger AccountantStep to be completed by : One of the recipientsIn Step Conditions enter the following:Country: <two-letter country/region code> (for example, DE, US, or another country/region)In Exception Handling, enter the following:RejectedRequired Action: Do nothingAction Result: Cancel WorkflowSent for ClarificationRequired Action: Provide More InformationRecipients: Determined automaticallyAction Result : Repeat stepChoose Create.Repeat this step for Recipient:Role: Compliance Manager |  |  |
| 8 | Create | Choose Create. | Workflow has been created. |  |
| 9 | Activate | Choose Activate | Workflow has been activated. |  |

#### Execute Workflow

Purpose

When a report run is generated, the app displays bubbles that indicate the number of levels of approval configured for the report.

Prerequisites

Preliminary steps are executed.

Business users are assigned the SAP_BR_MANAGER role.

A team is created and responsibilities assigned.

A workflow is created and activated.

You've executed prerequisites and successfully generated a report from the Compliance Formats – Support Preparation (1J2) test script (for example, an Advanced VAT return report or another report for your country).

##### Request Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you send a successfully generated report for approval.

|  |
| --- |
| Caution This procedure is written with the assumption that you're working with an Advance VAT Return report for Germany (DE_VAT_ADV_RTN). If you're using a different report for a different country/region, the steps for rows 4 and 5 may be different. |

Prerequisite

Preliminary steps are executed.

Business Users are assigned the SAP_BR_MANAGER role.

A team is created and responsibilities assigned.

A workflow is created and activated.

You've executed prerequisites and successfully generated a report from the Compliance Formats – Support Preparation (1J2) test script (for example, an Advanced VAT return report or another report for your country/region).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for your country/region. |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports (F1515). | The Run Advanced Compliance Reports view displays. |  |
| 3 | Enter Details | Make the following entries and choose Go:Submission Due Date: <Date range>Report Name: <Any previously generated report> (for example, an Advanced VAT Return report or another report for your country/region)Note Follow instructions from the Compliance Formats – Support Preparation (1J2) test script if you haven't executed and generated a report yet. | A list of Advanced Compliance Reports display. |  |
| 4 | Selection | In the Activities section, choose the Prepare Advance VAT Return (Germany).Caution This procedure is written with the assumption that you're working with an Advance VAT Return report for Germany (DE_VAT_ADV_RTN). If you're using a different report, the steps for rows 4 and 5 may be different. | A detailed view is displayed. |  |
| 5 | Workflow information | In the Runs section, in the Approval Status column, there are bubbles that represent each approval step. In this case, there are two levels. Hover over (or choose) a bubble to see more details. |  |  |
| 6 | Workflow Execution | In the Report Run Status column, select a successfully generated report and choose Send for Approval. | The system displays a dialog box. |  |
| 7 | Send | Optionally, you can add a note.Choose Send. | Request for approval has been sent and first bubble status changes.Also, overall Approval Status changes to Sent for Approval. |  |

##### Request Clarification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you request a clarification so a report can be approved.

|  |
| --- |
| Caution This procedure is written with the assumption that you are processing an Advance VAT Return for Germany (DE_VAT_ADV_RTN). If you are using a different report for a different country, the procedure in step 3 in each procedure table in this topic may be different. |

Prerequisite

Preliminary steps are executed.

Business users are assigned the SAP_BR_MANAGER role.

All steps in the [Request Approval](#unique_20) [page ] 34 topic are successfully executed.

Procedure - Request Clarification

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Open the SAP Fiori App | Open My Inbox - All Items (F0862). |  |  |
| 3 | Selection | In the All tasks pane, select the report item that was sent for clarification (for example, Advanced Compliance Reporting: Germany Advance VAT Return (DE_VAT_ADV_RTN) due on <date> is sent for clarification).Caution This procedure is written with the assumption that you are processing an Advance VAT Return for Germany (DE_VAT_ADV_RTN). If you are using a different report for a different country, this step may be different. | Details of the task display in the right pane. |  |
| 4 | Report | Choose Open Tasks to open the report for approval. When you are finished, go back to the My Inbox view. | The Run Compliance Reports view is displayed in a new window. |  |
| 5 | Information | Choose Comments to add a comment, or choose Attachment to add a file. |  |  |
| 6 | Clarification | Choose Send for Clarification. | A dialog box is displayed. |  |
| 7 | Submit | Add a note and choose Submit. | A request for clarification is sent.For the corresponding report, open the Run Statutory Reports (F1515) app. In the Generated section, the overall Approval Status changes to Sent for Clarification. You can hover over (or choose) the bubble for more information. |  |

Procedure - Clarification

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for your country/region. |  |  |
| 2 | Open the SAP Fiori App | Open My Inbox - All Items (F0862). |  |  |
| 3 | Selection | In the All tasks pane, select the report item that was sent for clarification (for example, Advanced Compliance Reporting: Germany Advance VAT Return (DE_VAT_ADV_RTN) due on <date> is sent for clarification).Caution This procedure is written with the assumption that you are processing an Advance VAT Return for Germany (DE_VAT_ADV_RTN). If you are using a different report for a different country, this step may be different. | Details of the task display in the right pane. |  |
| 4 | Clarification | Choose Comments to add any clarification comment or choose Attachment to add a file to support the clarification. |  |  |
| 5 | Complete Clarification | Choose Complete Clarification. | The system displays a dialog box. |  |
| 6 | Submit | Optionally, you can add a note.Choose Submit. | Clarification has been answered and sent for approval. |  |

##### First Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the first approver approves a report.

|  |
| --- |
| Caution This procedure is written with the assumption that you are processing an Advance VAT Return for Germany (DE_VAT_ADV_RTN). If you are using a different report for a different country, this procedure may be different. |

Prerequisite

Preliminary steps are executed.

Business Users are assigned the SAP_BR_MANAGER role.

If clarification was requested, all steps in the Request Clarification topic are successfully executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Open the SAP Fiori App | Open My Inbox - All Items (F0862). |  |  |
| 3 | Selection | In the All tasks pane, select the report item that was sent for clarification (for example, Advanced Compliance Reporting: Germany Advance VAT Return (DE_VAT_ADV_RTN) due on <date> is sent for Approval).Caution This procedure is written with the assumption that you are processing an Advance VAT Return for Germany (DE_VAT_ADV_RTN). If you are using a different report for a different country, this step may be different. | Details of the task display in the right pane. |  |
| 4 | Log | Choose Show log to see log details. | You can review the Workflow log and Task log. |  |
| 5 | Other (Optional) | Choose Comments to see previous comments or add a new comment.Choose Attachment to add a file to support the approval or provide extra information. |  |  |
| 6 | Approve | Choose Approve. | The system displays a dialog box. |  |
| 7 | Submit | Optionally, you can add a note.Choose Submit. | Task is processed successfully and no longer appears in the left pane All tasks and the request for approval is sent automatically to second approver. |  |
|  | Review First Approval |  |  |  |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for your country/region. |  |  |
| 2 | Status | In the [Request Approval](#unique_20) [page ] 34 topic, execute steps 2 to 5. | In the Generated section, the Approval Status column shows that the first bubble status is changed.Approval status can be reviewed with latest information. |  |

##### Second Approval

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the second approver approves a report.

|  |
| --- |
| Caution This procedure is written with the assumption that you are processing an Advance VAT Return for Germany (DE_VAT_ADV_RTN). If you are using a different report for a different country, this procedure may be different. |

Prerequisite

Preliminary steps are executed.

Business users are assigned the SAP_BR_MANAGER role.

All steps in the First Approval topic are successfully executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Accounts Payable Manager. |  |  |
| 2 | Open the SAP Fiori App | Open My Inbox - All Items (F0862). |  |  |
| 3 | Selection | In the All tasks pane, select the report item that was sent for clarification (for example, Advanced Compliance Reporting: Germany Advance VAT Return (DE_VAT_ADV_RTN) due on <date> is sent for Approval).Caution This procedure is written with the assumption that you are processing an Advance VAT Return for Germany (DE_VAT_ADV_RTN). If you are using a different report for a different country, this step may be different. | Details of the task display in the right pane. |  |
| 4 | Log | Choose Show log to see log details. | You can review the Workflow log and Task log. |  |
| 5 | Other (Optional) | Choose Comments to see previous comments or add a new comment.Choose Attachment to add a file to support the approval or provide extra information. |  |  |
| 6 | Approve | Choose Approve. | The system displays a dialog box. |  |
| 7 | Submit | Optionally, you can add a note.Choose Submit. | The task is processed successfully and no longer appears in the left pane All tasks. |  |
|  | Review Second Approval |  |  |  |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for your country/region. |  |  |
| 2 | Status | In the [Request Approval](#unique_20) [page ] 34 topic, execute steps 2 to 5. | In the Generated section, the Approval Status column shows that the second bubble status is changed.Approval status can be reviewed with the latest information.Also, overall Approval Status changes to Approved. |  |
| 3 | Submit | After approvals are completed, the report can be submitted.Note For more information on report submission, see the Compliance Formats – Support Preparation (1J2) test script. |  |  |

### Reconcile Draft Reports

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can request draft reports from the authority electronically and compare with report generated from the business system and identify any inconsistencies between the reports. When both the source reports are available, you can run a comparison and check the inconsistencies/mismatches. The comparison is always executed on the latest draft reports. After the validation, you can proceed to submission which would conclude the activity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for your country/region. |  |  |
| 2 | Open the SAP Fiori App | Open Run Statutory Reports (F1515). | The Run Advanced Compliance Reports view is displayed. |  |
| 3 | Enter Details | Make the following entries and choose Go:Submission Due Date: <date range>Report Name: <report for your country/region> | A list of reports is displayed. |  |
| 4 | Select Report | For the report you want to submit, choose Navigation (>). | The detailed view for your report is displayed. |  |
| 5 | Reconcile Draft Reports | In the Activities pane, double-click the report you want to execute.Note The activity to reconcile draft reports may have a different name depending on the country/region process. | A Confirmation dialog box is displayed. |  |
| 6 | Confirm Status Change | For the Do you want to change the status of the activity to "In Process" notification, chooseYes. | The Reconcile Draft Reports app is displayed. |  |
| 7 | Request Data from Authority | On the Reconciliation tab, choose From Authority > Request Data . | The file from the authority is electronically retrieved on successful request. The File Name and Requested On is updated and the Request Status is updated to Success. |  |
| 8 | Generate Data from Business System | Choose From Source Application > Generate Data . | On successful file generation, the File Name and Generated On is successfully updated and the Generation Status is updated to Generated Successfully. |  |
| 9 | Run Comparison | Choose Run Comparison. | The Reconciliation Status shows the status as either Content Mismatch or Content Match. |  |
| 10 | Verify Mismatches | If there are mismatches, choose the Mismatch tab. | Mismatches are displayed. |  |
| 11 | Logs | Choose the Logs tab. | All of the logs are displayed. |  |
| 12 | Full Result | Choose Full Result. | The full version of both reports, along with mismatches, are displayed. |  |
| 13 | Submit | Choose Proceed to Submission.Caution Before you submit, ensure that you have resolved any mismatches. | The submission is completed. Once the activity is complete, the Activity Status changes to Completed. |  |

### Electronic Document Consistency

Purpose

Electronic Document Consistency checks are used to ensure that different representations of your business documents remain uniform across your SAP system and your tax authority's system.

|  |
| --- |
| Note Review the SAP Help Portal to check the[Country/Region Specific Scenarios that Support Electronic Document Consistency Checks](https://help.sap.com/docs/SAP_S4HANA_CLOUD/71af4585db6d4904b1724730f3776c9b/1a99505af4bd445c9f80c9f316894ce3.html?version=LATEST) page. |

#### Responsibility Management Functions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step creates functions to perform tasks that are a part of a business process. Functions can be assigned to team members or agents to enable them to perform various tasks.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Application Platform and Infrastructure

Sub Application Area: Responsibility Management

1. For the row with Item Name of Functions, choose Details (>).
2. For the Define Functions row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Functions.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Editiond system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Enter Details | Make the following entries and press Enter:Function: <function>, for example, EDCBILLFunction Description: <description>, for example, Billing ClerkAdd another entry:Function: <function>, for example, EDCTAXOFunction Description: <description>, for example, Tax Officer |  |  |
| 3 | Save and Go Back | Save your entries.Choose Back until you return to the Functions, Configuration Steps view |  |  |

1. For the Define Function Profiles row, choose Configure.
2. Continue with the procedure in the following table.

|  |
| --- |
| Note For SAP Central Business Configuration, follow the instructions above for the Define Function Profiles activity. |

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Enter Details | Make the following entries and press Enter:Profile: <profile>, for example, EDCFPFunction Profile Description: <description>, for example, EDC Function ProfileSelect the added entry and choose Function Profile to Function Mapping. Enter the following in two separate rows:Function: <functions from procedure table above>, for example, EDCBILL and EDCTAXO |  |  |
| 3 | Save | Save your entries. |  |  |

#### Team Category Assignment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you assign a team category to a function profile.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Application Platform and Infrastructure

Sub Application Area: Responsibility Management

1. For the row with Item Name of Teams, choose Details (>).
2. For the Assign Function Profiles to Team Category row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Assign Function Profiles to Team Category.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Enter Details | Make the following entries and press Enter:Team Category: <team category>, for example, EDCProfile: <profile created in prior topic>, for example, EDCFP |  |  |
| 3 | Save | Save your entries. |  |  |

#### Team Type

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define team type which is associated with a team category and inherits its functions and responsibility definitions.

Prerequisites

A team category is assigned to a function profile.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Application Platform and Infrastructure

Sub Application Area: Responsibility Management

1. For the row with Item Name of Teams, choose Details (>).
2. For the Define Team Types row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Team Types.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Enter Details | Make the following entries and press Enter:Team Type: <team type>, for example, EDC_<ctry>_CUST_INV (replace <ctry> with your country or region)Team Category: <team category>, for example, EDCTeam Type Description: <description> |  |  |
| 3 | Exclude Functions (Optional) | Optional Step: Select a team type. From the side menu, choose Exclude Functions and add an entry from the [Responsibility Management Functions](#unique_25) [page ] 43 topic. |  |  |
| 4 | Save | Save your entries. |  |  |

#### Create Team

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a team member that identifies as the notification recipient.

Prerequisites

Employees are created as business partners.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Open the SAP Fiori App | Open Manage Teams and Responsibilities (F2412). |  |  |
| 3 | Create | Choose Create. | The Team view displays. |  |
| 4 | General Information | In section General Information make the following entries:Name: <Any name> (Recommended to add country initials in name)Global ID: <Same as Name field>Description: <any description>Type: <team type from the Team Type topic>, for example, EDC_<Ctry>_CUST_INV >Status: Enabled |  |  |
| 5 | Responsibility Definitions | In the Responsibility Definitions section, make the following entry:Company Code: <company code>EDC type (Consistency scenario): <select one for country to be tested (first 2 characters identify the country)>, for example, ESSIIOUT |  |  |
| 6 | Team Owners (Optional) | Optional step: In the Team Owners section, either keep the default entry or choose Create.Select a user:Business Partners: <business partner> |  |  |
| 7 | Team Members | In the Team Members, section, choose Create.Select the users who will be the workflow notification recipient and choose OK:Business Partners: <business partner>, for example; BillingClerk.To find the business partner number, search by last name.In the Functions column, assign a function:BillingClerk: <choose a function created in the Responsibility Management Functions topic>, for example, EDCBILL |  |  |
| 8 | Save | Save your entries. | The team is created. |  |

#### Create Workflow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define and activate a workflow for electronic document consistency for your reporting scenarios.

Prerequisite

A team has been created and responsibilities assigned.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Open the SAP Fiori App | Open Manage Workflows (F8647). |  |  |
| 3 | Create | Choose Create. | The New Workflow view displays. |  |
| 4 | Header | In section Header make the following entry:Workflow Name: <Any name> |  |  |
| 5 | Start Conditions | In the Start Conditions section, make the following entries:Company Code: <company code>Consistency Scenario: <country scenario>, for example, ESSIIOUTNote Each country has its own unique situation, so ensure the appropriate country-specific scenario is being applied. |  |  |
| 6 | Steps | In the Steps section, choose Create.In the Header section, enter the following:Step Name: <Any description>Step Type: Resolve InconsistenciesIn Recipients, enter the following:Role: Billing ClerkThe team member assigned in the [Create Team](#unique_28) [page ] 48 topic receives a notification in their Inbox.Step to be completed by: One of the recipientsIn Exception Handling, enter the following:Required Action: Send for ClarificationRecipients: Workflow InitiatorAction Result: Repeat step |  |  |
| 7 | Create | Choose Create. | Workflow is created. |  |
| 8 | Activate | Choose Activate | Workflow is activated. |  |

#### Schedule Jobs for Electronic Document Consistency

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to schedule an application job to execute the validation report for eDocument consistencies.

Prerequisite

Invoices are posted.

The eDocument is sent to the Tax Authority Portal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Jobs for Electronic Document Consistency (F7494). | The Application Jobs view displays. |  |
| 3 | Create Job | Choose Create. |  |  |
| 4 | Template Selection | Make the following entries and choose Step 2:Job Template: eDocument Consistency: Validation ReportJob Name: eDocument Consistency: Validation Report |  |  |
| 5 | Scheduling | Make the following entries and choose Step 3:Start immediately: Selected |  |  |
| 6 | Parameters | Make the following entries:General Selection Criteria section:Company Code: <company code>Consistency Scenario: <Select one that is specific to your country>, for example, ESSIIOUT |  |  |
| 7 | Schedule | Choose Schedule. | You scheduled the job. |  |

#### Electronic Document Consistency Validation Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to execute the Resolve Electronic Document Inconsistencies report to review the content mismatch of documents sent to a Portal Authority and initiate a workflow notification to review them.

|  |
| --- |
| Note Review SAP Help Portal to check [Country/Region-Specific Scenarios that Support Electronic Document Consistency Checks](https://help.sap.com/docs/SAP_S4HANA_CLOUD/71af4585db6d4904b1724730f3776c9b/1a99505af4bd445c9f80c9f316894ce3.html?version=LATEST). |

Prerequisite

The eDocument Consistency: Validation Report scheduled job ran successfully.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk.Note This role is the Initiator of the workflow notification. For testing purposes, we use the same generic user (Billing Clerk) as both the notification initiator and recipient. In a productive environment, assign the billing clerk role to different users to ensure that the initiator and recipient are not the same person.Note Users with the Billing Clerk role assigned to them have access to this report. |  |  |
| 2 | Access the SAP Fiori App | Open Resolve Electronic Document Inconsistencies (F7043). |  |  |
| 3 | Selection | Make the following entry and choose Go:Company Code: <company code> | The Summary of Electronic Document Consistency Checks view displays. |  |
| 4 | List | Select an entry with Category Content Mismatch from the Invoice Count column.Note Depending on the country standard delivery, other categories might be enabled. |  |  |
| 5 | Details | Choose > (Details) to view all the information of the content mismatch. |  |  |
| 6 | Notification | After reviewing the inconsistency, initiate a workflow to report it by choosing Report inconsistency.In the dialog box, add a comment with instructions to check the content mismatch and choose Save. | The system displays a message indicating that the workflow notification was sent successfully.A user with the Billing Clerk role receives the notification. |  |

#### Notification Processing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you access a workflow notification. This workflow notification informs the recipient of an inconsistency found so it can be analyzed and solved.

Prerequisite

The Validation Report and Notification procedure was executed successfully.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Billing Clerk.Note This role is defined as the Recipient of workflow notification. |  |  |
| 2 | Access the SAP Fiori App | Open My Inbox - All Items (F0862). |  |  |
| 3 | Notification | Select a task that has Inconsistencies detected in document ID. | The recipient should take action to resolve the inconsistency, such as checking documents, reports, and other tools to identify the cause of the inconsistency to solve it.The recipient should have access to the app Resolve Electronic Document Inconsistencies (F7043) to see the inconsistency details. |  |
| 4 | Clarification | If the recipient needs more information, choose Send for Clarification to add a comment to request information, then choose Submit. | A notification is sent back to the notification initiator. |  |
| 5 | Answer | The initiator checks their inbox (in this example the Billing Clerk). After reading the notification, they choose Resubmit to answer to the recipient. | A notification is sent back to the recipient. |  |
| 6 | Resolve | Once the clarifications are processed and inconsistencies resolved, choose Resolve to inform that the job is done | The resolution can be different on a case-by-case basis. |  |
| 7 | Check | Once the inconsistency is resolved, the initiator must run the prior two topics to review and ensure that the inconsistency is gone. |  |  |

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
- see-also :: [[04-tax-and-statutory-reporting/test-script-invoice-correction-process-with-debit-memo-bdq-ae-1257]]
- see-also :: [[04-tax-and-statutory-reporting/test-script-compliance-formats-support-preparation-1j2-ae-sap-s-4hana]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5XU_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 95,579 chars in the whole document
