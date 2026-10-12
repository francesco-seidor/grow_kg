---
id: 03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounting-and-financial-part-01
title: Test Script SAP S/4HANA Cloud Public Edition - Accounting and Financial Close (J58_AE) (J58_S4CLD2608_BPD_EN_AE) — part 1 of 2
description: "SAP S/4HANA Cloud Public Edition 2608 (UAE) test script for Accounting and Financial Close (J58_AE): prerequisites, config steps and G/L test procedures."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/general-ledger-accounting-and-financial-close]
aliases: []
keywords: [General Ledger Accounting and Financial Close, financial close, g/l account master data, chart of accounts, financial statement versions, profit centers, journal entries, journal entry verification, recurring journal entries, open item clearing]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J58_S4CLD2608_BPD_EN_AE.docx#lines-1-3738"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1304
topic: 03-financial-accounting-and-close/general-ledger-accounting-and-financial-close
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Accounting and Financial Close (J58_AE) (J58_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J58_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–3738 of the extracted text), extracted with `mammoth`. Grouped under **General Ledger Accounting and Financial Close** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Accounting and Financial Close (J58_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232863122)

[2 Prerequisites 6](#_Toc232863123)

[2.1 System Access 6](#_Toc232863124)

[2.2 Roles 6](#_Toc232863125)

[2.3 Master Data and Organizational Data 7](#_Toc232863126)

[2.4 Business Conditions 8](#_Toc232863127)

[2.5 Preliminary Steps 9](#_Toc232863128)

[2.5.1 Define Reverse Document Type (Optional) 9](#_Toc232863129)

[2.5.2 Set Report Relevancy 10](#_Toc232863130)

[2.5.3 Activate Authorization Check for Approval 11](#_Toc232863131)

[2.5.4 Relevant Configuration Steps for Advanced Valuation in General Ledger Accounting 12](#_Toc232863132)

[2.5.4.1 Activate Advanced Valuation 12](#_Toc232863133)

[2.5.4.2 Assign Financial Statement Versions to Accounting Principles 14](#_Toc232863134)

[2.5.4.3 Define Rules for Determining Account Assignments in G/L Processes 15](#_Toc232863135)

[2.5.4.4 Assign Account Assignment Rule to Advanced Valuations 17](#_Toc232863136)

[2.5.5 Relevant Configuration Steps for Advanced Foreign Currency Valuation 18](#_Toc232863137)

[2.5.5.1 Define Financial Statement Versions 18](#_Toc232863138)

[2.5.5.2 Assign Semantic Tags to Financial Statement Versions 19](#_Toc232863139)

[2.5.5.3 Define Rules for Advanced Foreign Currency Valuation 20](#_Toc232863140)

[2.5.5.4 Assign Rules for Foreign Currency Valuation to Accounting Principles 23](#_Toc232863141)

[2.5.6 Relevant Configuration Steps for Credit-Risk Based Impairment 24](#_Toc232863142)

[2.5.6.1 Define Aging Increments for Advanced Valuation 24](#_Toc232863143)

[2.5.6.2 Assign Risk Class in Business Partner Master Data 25](#_Toc232863144)

[2.5.6.3 Assign Semantic Tags to Financial Statement Versions 26](#_Toc232863145)

[2.5.6.4 Define Rules for Impairment 27](#_Toc232863146)

[2.5.6.5 Assign Rules for Impairment to Accounting Principles 30](#_Toc232863147)

[2.5.7 Relevant Configuration Steps for Post Balance Sheet Reclassification by Master Data Change 31](#_Toc232863148)

[2.5.7.1 Define Aging Increments for Advanced Valuation 31](#_Toc232863149)

[2.5.7.2 Define Rules for Balance Sheet Reclassification by Maturity 33](#_Toc232863150)

[2.5.7.3 Define Rules for B/S Reclassification by Master Data Change 33](#_Toc232863151)

[2.5.7.4 Assign Semantic Tags to Financial Statement Versions 35](#_Toc232863152)

[2.5.7.5 Assign Rules for Balance Sheet Reclassification by Master Data Change to Accounting Principle 36](#_Toc232863153)

[2.5.8 Relevant Configuration Steps for Post Balance Sheet Reclassification by Maturity 37](#_Toc232863154)

[2.5.8.1 Define Aging Increments for Advanced Valuation 37](#_Toc232863155)

[2.5.8.2 Define Rules for Balance Sheet Reclassification by Maturity 39](#_Toc232863156)

[2.5.8.3 Assign Reclassification Rules to Accounting Principles 42](#_Toc232863157)

[2.5.9 Relevant Configuration Steps for Statement of Changes in General Ledger 43](#_Toc232863158)

[2.5.10 Add Multiple Accounts Using Expert Worklist 44](#_Toc232863159)

[2.5.11 Define Balance Validation Rules and Groups - Upload Rules 46](#_Toc232863160)

[2.5.12 Define Financial Statement Version in Global Hierarchies 47](#_Toc232863161)

[2.5.13 Migrate Financial Statement Versions to Global Hierarchies 49](#_Toc232863162)

[2.5.14 Replicate Runtime Hierarchy 51](#_Toc232863163)

[3 Overview Table 52](#_Toc232863164)

[4 Test Procedures 59](#_Toc232863165)

[4.1 Manage G/L Account Master Data 59](#_Toc232863166)

[4.2 Define Financial Statement Versions 63](#_Toc232863167)

[4.3 Manage Chart of Accounts 66](#_Toc232863168)

[4.4 Manage Operating Chart of Accounts 67](#_Toc232863169)

[4.5 Manage Operating G/L Account 69](#_Toc232863170)

[4.6 Manage Alternative Chart of Accounts 73](#_Toc232863171)

[4.7 Synchronize G/L Account Master Data 74](#_Toc232863172)

[4.8 G/L Account Changes 76](#_Toc232863173)

[4.9 Manage Profit Center Group 77](#_Toc232863174)

[4.10 Manage Profit Centers 78](#_Toc232863175)

[4.11 Edit Profit Centers Collective 79](#_Toc232863176)

[4.12 Edit Company Code Assignment Profit Centers 81](#_Toc232863177)

[4.13 Where-Used List - Profit Centers 82](#_Toc232863178)

[4.14 Change Log - Profit Centers 83](#_Toc232863179)

[4.15 Manage Journal Entry Template 84](#_Toc232863180)

[4.16 Post General Journal Entries 86](#_Toc232863181)

[4.16.1 Post with Auto-Reverse 89](#_Toc232863182)

[4.17 Upload General Journal Entries 92](#_Toc232863183)

[4.18 Verify General Journal Entries 93](#_Toc232863184)

[4.18.1 Verify General Journal Entries - with Auto-Reverse 97](#_Toc232863185)

[4.18.2 Withdraw Verify General Journal Entries 99](#_Toc232863186)

[4.19 Approve Verify General Journal Entries (for Processor - Inbox) 100](#_Toc232863187)

[4.20 Forward Verify General Journal Entries (for Processor - Inbox) 102](#_Toc232863188)

[4.21 Reject Verify General Journal Entries (for Processor - Inbox) 103](#_Toc232863189)

[4.22 Edit a Rejected Verify General Journal Entry (Requester) 104](#_Toc232863190)

[4.23 Manage Journal Entries 105](#_Toc232863191)

[4.23.1 Open Correspondence 106](#_Toc232863192)

[4.23.2 Reverse General Journal Entries 108](#_Toc232863193)

[4.24 Display Journal Entries 110](#_Toc232863194)

[4.25 Display Document Flow 111](#_Toc232863195)

[4.26 Display G/L Account Balances 112](#_Toc232863196)

[4.27 Display Line Items in General Ledger 113](#_Toc232863197)

[4.28 Display Line Item Entry 114](#_Toc232863198)

[4.29 Manage Recurring Journal Entries 115](#_Toc232863199)

[4.29.1 Create Recurring Journal Entry 116](#_Toc232863200)

[4.29.2 Display Recurring Journal Entry 117](#_Toc232863201)

[4.29.3 Edit Recurring Journal Entry 118](#_Toc232863202)

[4.29.4 Copy Recurring Journal Entry 119](#_Toc232863203)

[4.29.5 Post Recurring Journal Entry 119](#_Toc232863204)

[4.29.6 Delete Recurring Journal Entry 120](#_Toc232863205)

[4.30 Display Changes of Recurring Entry 121](#_Toc232863206)

[4.31 Audit Journal 122](#_Toc232863207)

[4.32 Journal Entry Analyzer 123](#_Toc232863208)

[4.33 Clear G/L Accounts - Manual Clearing 126](#_Toc232863209)

[4.34 Clear G/L Accounts 128](#_Toc232863210)

[4.35 Reset Cleared Items 130](#_Toc232863211)

[4.36 Schedule Jobs to Reset Cleared Items (Optional) 131](#_Toc232863212)

[4.37 Clear Open Items Automatically 133](#_Toc232863213)

[4.38 Currency Exchange Rates 134](#_Toc232863214)

[4.39 Import Foreign Exchange Rates 134](#_Toc232863215)

[4.40 Repost GR/IR Clearing 135](#_Toc232863216)

[4.41 Perform Foreign Currency Valuation 137](#_Toc232863217)

[4.42 Post Currency Adjustments 140](#_Toc232863218)

[4.43 Verify Currency Adjustments 141](#_Toc232863219)

[4.43.1 Withdraw Verify Currency Adjustments 144](#_Toc232863220)

[4.44 Approve Verify Currency Adjustments (for Processor- Inbox) 145](#_Toc232863221)

[4.45 Forward Verify Currency Adjustments (for Processor- Inbox) 147](#_Toc232863222)

[4.46 Reject Verify Currency Adjustments (for Processor- Inbox) 148](#_Toc232863223)

[4.47 Edit a Rejected Verify Currency Adjustment (Requester) 149](#_Toc232863224)

[4.48 Verify Data Flow 150](#_Toc232863225)

[4.49 Perform Advanced Foreign Currency Valuation 151](#_Toc232863226)

[4.50 Analyze Closing Run Results 153](#_Toc232863227)

[4.51 Credit-Risk-Based Impairment 154](#_Toc232863228)

[4.52 Balance Sheet Reclassification 156](#_Toc232863229)

[4.52.1 Post B/S Reclassification - Master Data Change 156](#_Toc232863230)

[4.52.2 Post B/S Reclassification - Maturity 158](#_Toc232863231)

[4.53 Manage Posting Periods 161](#_Toc232863232)

[4.54 Post Tax Payables 162](#_Toc232863233)

[4.55 General Ledger - Periodic Activities 164](#_Toc232863234)

[4.55.1 Tax Reconciliation Account Balance 164](#_Toc232863235)

[4.55.2 Tax Declaration Reconciliation 165](#_Toc232863236)

[4.56 Withholding Tax Calculation Analysis Report (Optional) 166](#_Toc232863237)

[4.57 Regroup Receivables/Payables 169](#_Toc232863238)

[4.58 Process Batch Input Session 170](#_Toc232863239)

[4.59 Import Financial Plan Data 171](#_Toc232863240)

[4.60 Balance Sheet / Income Statement 173](#_Toc232863241)

[4.60.1 Financial Statement Download and Printing 174](#_Toc232863242)

[4.60.2 Financial Statements Review Booklet 175](#_Toc232863243)

[4.61 Trial Balance 177](#_Toc232863244)

[4.62 Year-to-Date Balances 178](#_Toc232863245)

[4.63 Balance Carryforward Status 179](#_Toc232863246)

[4.64 Display Journal Entries - in T-Account View 180](#_Toc232863247)

[4.65 Statement of Changes in General Ledger 180](#_Toc232863248)

[4.66 General Ledger Overview 182](#_Toc232863249)

[4.67 Balance Validation 185](#_Toc232863250)

[4.67.1 Schedule Balance Validation Jobs 185](#_Toc232863251)

[4.67.2 View Balance Validation Results 186](#_Toc232863252)

[5 Appendix 188](#_Toc232863253)

[5.1 Display Tax Information Per Country/Region 188](#_Toc232863254)

[5.2 User Specific Settings for Alternative Chart of Account 189](#_Toc232863255)

[5.3 Schedule General Ledger Jobs - Carry Forward Balances 189](#_Toc232863256)

[5.4 Review Verify General Journal Entries (Optional) 191](#_Toc232863257)

[5.5 Manage Finance Notifications 193](#_Toc232863258)

## Purpose

Overview

The central task of general ledger accounting is to provide a comprehensive overview of external accounting and accounts. By recording all business transactions, including primary postings and settlements from internal accounting, in a system that is fully integrated with all the other operational areas of a company, you ensure accuracy and completeness for accounting data.

General ledger accounting serves as a complete record of all business transactions, providing a centralized, current reference for the rendering of accounts. Actual individual transactions are reviewed with real-time processing, displaying the original documents, line items, and transaction figures at various levels (such as account information, journals, totals, transaction figures, and balance sheets).

This process describes all required period end-closing steps, related to performing local period-end closing and steps that are identical for local and parallel ledgers.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/J58_S4CLD2602_BPD_EN_AE.docx) ). |

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
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Divisional Accountant | SAP_BR_DIVISION_ACCOUNTANT | Divisional Accounting | SAP_BR_DIVISION_ACCOUNTANT |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data and Organizational Data

Default Values

The organizational structure and master data of your company was created in your SAP S/4HANA Cloud Public Edition system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Additional Default Values

You can test the scope item with other SAP Best Practices default values that have the same characteristics.

Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Master Data | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Chart of Accounts | YCOA |  |  |
| Controlling Area | A000 |  |  |
| Cost Center | 33101001 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) .

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |

### Business Conditions

Activate Features

In a software update, SAP delivers certain features that could have an impact on your implemented solution initially in an inactive state. You can choose to already activate these features before they become available by default in a later release.

The test procedures in this document describe the software behavior when all features have been activated. It is a prerequisite for testing that you have activated all of the following features in each of your systems using the configuration activity Activate Features. For more information about this activity, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/3e94fcc37b42433b97d6aef0c830dc52.html) for SAP S/4HANA Cloud Public Edition.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

- Configure Your Solution:

Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

Navigate to Manage your Solution > Configure Your Solution. Search for Activate Features. In the search result, select the configuration activity and go to the next screen. Select the configuration step and choose Configure.

- SAP Central Business Configuration:

Log on to the project experience in SAP Central Business Configuration.

Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Features. Choose the link to navigate directly to the target system of SAP S/4HANA Cloud Public Edition. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration (SAP_BR_BPC_EXPERT).

| Feature ID | Feature Title |
| --- | --- |
| FIN_GL_FS_REVIEW_BOOKLET | Financial Statements Review Booklet |

### Preliminary Steps

#### Define Reverse Document Type (Optional)

Purpose

In this activity, you define the reverse document type for a document type. Document types (Journal Entry Types) categorize business transactions and manage how documents are stored. The document number range is assigned to the document type, and document splitting is controlled by the document type. A reverse document type is used to reverse a document. If you don't specify a reverse document type, the reversal document is automatically posted with the same document type and number range as the original document.

|  |
| --- |
| Caution This step is only required if your country or your specific business process requires reverse documents to be posted with a different document type or different number range than the original document type. If you do not require reverse documents, skip this step. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Settings

1. For the row with Item Name of Journal Entries, choose Details (>).
2. For the Define Document Types row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Document Types.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Document Type | Select the checkbox for the document type (for example, SA), and choose Details.Note The document type mentioned in this row and the following row are examples only. Use document types appropriate to your situation. | The Change View "Document Types": Details view displays. |  |
| 2 | Reverse Document Type | Make the following entries and choose Save:Reverse Document Type: <reversal document type> for example, AB | The reverse document type is assigned. |  |

#### Set Report Relevancy

Purpose

When you run Design Studio reports for the first time, you need to set the report relevancy. If you later change the cost center, profit center, or G/L hierarchy, you must update the report relevancy to reflect the latest information.

Additionally, you need to manually replicate set-based hierarchies (like Cost Center Group or Profit Center Group) and financial statement hierarchies to the back-end database hierarchy tables. This process is typically automated as a periodic background job.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Set Report Relevancy - Set-Based Hierarchies (F5295). | The Set Report Relevancy view is displayed. |  |
| 3 | Enter Header Data | In the header area, make the following entries and choose Go:Set Class: <cost center group>, for example, 0101Organizational Unit: A000Set Name: A000 |  |  |
| 4 | Edit | In the Set Report Relevancy pane, select the checkbox for the set to edit and choose Edit. | The Edit dialog box is displayed. |  |
| 5 | Mark as Report Relevant | Make the following entries and choose Save:Report Relevant: Yes |  |  |

#### Activate Authorization Check for Approval

Purpose

In this activity, you enable the authorization check on the processor when you perform the verification workflows in the following Test Procedure steps:

- [Approve Verify General Journal Entries (for Processor - Inbox)](#unique_10) [page ] 100
- [Approve Verify Currency Adjustments (for Processor- Inbox)](#unique_11) [page ] 145

If checking is enabled, when you approve a journal entry or currency adjustment, the system checks if you are authorized to do the posting.

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

1. For the row with Item Name of Journal Entries, choose Details (>).
2. For the Activate Authorization Check for Approval row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Authorization Check for Approval.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Authorization Check | Select the appropriate scenario for your business:General Journal Entry VerificationCurrency Adjustment Verification |  |  |
| 3 | Save | Choose Save. |  |  |

#### Relevant Configuration Steps for Advanced Valuation in General Ledger Accounting

##### Activate Advanced Valuation

Purpose

In this activity, you activate the advanced valuation.

Procedure

To run [Perform Advanced Foreign Currency Valuation](#unique_13) [page ] 151, you must activate Advanced Foreign Currency Valuation.

|  |
| --- |
| Caution To activate advanced valuation, activate the relevant content for SAP S/4HANA Cloud Public Edition. Once Advanced Valuation is activated, the following apps can't be used:Perform Foreign Currency Valuation (FAGL_FCV)Regroup Receivables / Payables (FAGLF101)Perform Further Valuations (F107)If there are no postings in the productive system, Advanced Valuation can be deactivated. |

|  |
| --- |
| Caution If you're an existing customer using the Central Business Configuration environment to configure your system and you want to add a new country/region version anytime after the upgrade to SAP S/4HANA Cloud Public Edition 2202, Advanced Valuation is automatically activated for the newly added country/region. If you want to use Classic Valuation instead and if you haven't yet made any postings in the productive system for the new country/region, you can deactivate Advanced Valuation using the Activate Advanced Valuation configuration step. For more information, see SAP Note [3139304](https://me.sap.com/notes/3139304). |

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Activate Advanced Valuation row, choose Configure.
3. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Activate Advanced Valuation.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step# | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Activate Advanced Valuation | Make the following entries:Accounting Principle: AEAPActivate Advanced Valuation: Selected |  |  |
| 3 | Maintain Fiscal Year and Period | Select the row you created and in the Dialog Structure pane, double-click Maintain Fiscal Year and Period. |  |  |
| 4 | Maintain Fiscal Year and Period | Make the following entries and choose Save:Ledger: 0L<defaulted from the accounting principle used>Company Code: 3310Fiscal Year: <current fiscal year>Activation from Period: <current period>Note The activation period should be considered during testing. The date of the job run should be the last day of the current period. |  |  |

##### Assign Financial Statement Versions to Accounting Principles

Purpose

In this activity, you assign the financial statement versions to the accounting principle. Customers must assign their own FSV (based on YCOA) here. In addition, only the operative chart of accounts (such as YCOA) can be selected here. For more information, see [Define Financial Statement Versions](#unique_15) [page ] 18.

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
2. For the Assign Financial Statement Version to Accounting Principles row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Financial Statement Version to Accounting Principles.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step# | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Required Data for FSV Assignment | Make the following entries and choose Save:Accounting Principle: AEAPChart of Accounts: YCOAFinancial Statement Version Financials: <customer's FSV> |  |  |

##### Define Rules for Determining Account Assignments in G/L Processes

Purpose

In this activity, you create rules that determine account assignment in G/L accounting processes. The rules are used, for example, when you perform jobs using the following job templates in the Schedule General Ledger Jobs (F1927) app:

- Advanced Foreign Currency Valuation
- Post Credit-Risk-Based Impairment
- Post Discounting of Long-Term Assets and Liabilities

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

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Define Rules for Determining Account Assignments in G/L Processes row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Rules for Determining Account Assignments in G/L Processes.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step# | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Make the following entries:Assignment Rule: four-digit ID starting with ZDescription of Assignment Rule: descriptionControlling Object Inheritance Option: see noteNote Determine how the account assignment is derived when this rule is used: The following options are available:From Original Object: The controlling object is derived from the dependent object (source document).From Default Configuration: The controlling object is derived from the default configuration, from the Automatic Account Assignment activity.No Assignment: The controlling object is empty in the financial document.Reporting Field Inheritance Option: <Value is preset (Standard Derivation); cannot be changed>Default: <Value is preset (VALV, selected); cannot be changed> |  |  |
| 2 | Adjust Inheritance Option for Assignment Field | Make the following entries and choose Save:Fields: <see note>Note For each field in the list, you can set how the account assignment is determined by the system when this rule is applied. The following options are available:Inherited from Global Rule Setting: The option defined in the assignment rule is used.Always from Original Object: The field is always derived from a dependent object.Always from Default Configuration: The field is always derived from the default configuration.Always No Assignment: The field isn't used for account assignment determination; it's left empty in the created document.Not Relevant: Each process handles this field with its own logic. |  |  |

##### Assign Account Assignment Rule to Advanced Valuations

Purpose

In this activity, you assign an account assignment rule to the process where you want to use it.

The SAP standard delivery contains the valuation rule VALN. This rule is assigned to the following business transaction types and job templates:

- RFCV Foreign Currency Valuation (Advanced Foreign Currency Valuation job template)
- RFDI Discounting (Post Discounting of Long-Term Assets and Liabilities job template)
- RFIM Credit Risk Based Impairment (Post Credit-Risk Based Impairment job template)

If you defined a new valuation rule in the prior step, follow the procedure below.

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

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Assign Account Assignment Rules to Advanced Valuations row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Account Assignment Rules to Advanced Valuations.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step# | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Entry Details | Make the following entries and choose Save:Business Transaction Type.Business Transaction Item CategoryAssignment Rule |  |  |

#### Relevant Configuration Steps for Advanced Foreign Currency Valuation

The financial statement version XX99 is delivered as demo data and is assigned to the local accounting principle.

In addition to the configuration activities in this section, you can also perform revaluation of parallel currencies using an optional configuration activity titled Maintain Settings for Revaluation of Parallel Currency. You can use the Manage Your Solution (F1241) app or the SAP Central Business Configuration Experience to access the activity. For more information, see [this page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/431fffe8557d464ba4afdf5087c4b83a-582.html?version=LATEST) on the SAP Help Portal.

##### Define Financial Statement Versions

To perform the necessary steps for Advanced Valuation in General Ledger Accounting, perform the steps in the [Define Financial Statement Versions](#unique_19) [page ] 63 topic.

##### Assign Semantic Tags to Financial Statement Versions

Purpose

In this activity, you assign semantic tags to the financial statement versions.

|  |
| --- |
| Note Only G/L accounts with the semantic tag FX are considered for an Advanced Foreign Currency Valuation run.If you maintain the financial statement version (FSV) in the configuration step, you can search for Assign Semantic Tags to Financial Statement Versions in either the Manage Your Solution (F1241) app or the SAP CBC project experience, as mentioned below. The G/L account should be assigned to the FSV.If you maintain the FSV using the new Global Hierarchy tool, you don't need to perform the configuration below. Semantic tag functionality is already included into Global Hierarchy. Semantic Tag should be entered for required G/L accounts. |

This is required for the following test procedures:

- [Perform Advanced Foreign Currency Valuation](#unique_13) [page ] 151

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
2. For the Assign Semantic Tags to Financial Statement Versions row, choose Configure.
3. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Semantic Tags to Financial Statement Versions.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step# | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries.In the New Entry dialog box, select Assign Semantic Tag to G/L Account and choose Continue. |  |  |
| 2 | Map FSV to Semantic Tag | Make the following entries and choose Save:FS Vers: <FSV from prior step>Account From: <G/L account>Semantic Tag: FX |  |  |

##### Define Rules for Advanced Foreign Currency Valuation

Purpose

In this activity, you define the foreign currency valuation rules. The following rule is delivered for foreign currency valuation:

| Valuation Rule | Description | Accounting Principle Assignment |
| --- | --- | --- |
| SKDV | Key Date Foreign Currency Valuation | IFRS, USGP |

|  |
| --- |
| Note Optionally, you can create a rule for advanced foreign currency valuation, depending on your local requirements. |

Prerequisite

Before you start the Advanced Foreign Currency Valuation process, you must assign the G/L accounts.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Define Rules for Advanced Foreign Currency Valuation row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Rules for Advanced Foreign Currency Valuation.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Define Rules for Advanced Foreign Currency Valuation | Select Valuation Rule SKDV (Key Date Foreign Currency Valuation, and from the left pane, double-click Assign GL Accounts for FCV. | The Determine Work Area: Entry dialog box is displayed. |  |
| 2 | Confirm | Verify the Rules and Rule Step and choose Continue. | The Change View "Define Rules for Advanced Foreign Currency...: Overview view is displayed. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Assign G/L Accounts for FCV | Make the following entries and choose Save:Chart of Accounts: YCOAReset FX Unrealized Gain Account: 72510000Reset FX Unrealized Loss Account: 72010000FX Gain Unrealized Account: 72540000FX Loss Unrealized Account: 72040000 |  |  |

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

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Define Rules for Advanced Foreign Currency Valuation row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Rules for Advanced Foreign Currency Valuation.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Define Rules for Advanced Foreign Currency Valuation | Select the entry:SKDV (Key Date Foreign Currency Valuation)Choose Copy as.Enter a new ID in the customer namespace.Choose Save.Note Optionally, you can create a rule for advanced foreign currency valuation as New Entry. The new rule you create must be given an ID compatible with the customer name space. |  |  |
| 2 | Define Steps of FCV Rule | Copy an existing valuation rule step or create an entry. In the step, you can assign a different FCV valuation method. The following methods are available:ALWAYS_VALUATION (Always Valuate)DE_BILMOG_VALUATE (German Accounting Modernization Act)GAIN_ONLY (Highest Value Principle)LOWEST_VALUE (Lowest Value Principle)STRICT_LOWEST_VALUE (Strictly Lowest Value Principle)Note For new steps, you should select a value with the interval 1000 to 4999. Values starting with 00 can't be included in entries created in the customer namespace. |  |  |
| 3 | Assign Semantic Tag to FCV Rule | You must define a semantic tag as a filter value. You should assign the semantic tag FX to all G/L accounts to be considered in the valuation run. |  |  |
| 4 | Assign G/L Accounts for FCV | Assign the G/L accounts before you start Advanced Foreign Currency Valuation. For more information on the test data, see the section in this step. |  |  |

##### Assign Rules for Foreign Currency Valuation to Accounting Principles

Purpose

If you create a customer-specific rule for advanced foreign currency valuation in the prior [Define Rules for Advanced Foreign Currency Valuation](#unique_21) [page ] 20 step, you must assign it to an accounting principle.

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

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Assign Rules for Foreign Currency Valuation to Accounting Principles row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Rules for Foreign Currency Valuation to Accounting Principles.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Assign Rules for Foreign Currency Valuation to Accounting Principles | Make the following entries and choose Save:Accounting Principle: AEAPValuation Rule: <new valuation rule> |  |  |

#### Relevant Configuration Steps for Credit-Risk Based Impairment

##### Define Aging Increments for Advanced Valuation

Purpose

In this activity, you define the aging increments for advanced valuation.

The following aging with aging increments is delivered for the [Credit-Risk-Based Impairment](#unique_25) [page ] 154 topic:

- IMPAIRMENT (Aging for Impairment)
    - I - 12 (Due < 1 Year)
    - I – 36 (Due < 3 Year)
    - I0 (Overdue < 30 Days)
    - I30 (Overdue > 30 Days)
    - I60 (Overdue > 60 Days)
    - I90 (Overdue > 90 Days)

|  |
| --- |
| Note If needed, you can create additional aging or aging increments with this procedure. |

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

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Define Aging Increments for Advanced Valuation row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Aging Increments for Advanced Valuation.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step# | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Define New Aging for Impairment | Make the following entries and choose Save:Aging: <new aging codification>Description: <new aging description>Aging Category: IMP Impairment |  |  |

##### Assign Risk Class in Business Partner Master Data

Purpose

In this activity, you assign the risk class to the customer business partner master data.

Procedure

| Step # | Test Step name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). |  |  |
| 3 | Select Customer | Make the following entries and press Enter:Business Partner: 33100001 | The Display Organization view is displayed for the business partner. |  |
| 4 | Change Role | Make the following entries:Change in BP Role: Customer (Fin.Accounting)Note If the field is Display in BP Role, choose Switch between Display and Change to go into change mode. | The Display Organization XXXXXXXX: Role FI Customer view is displayed for the business partner. |  |
| 5 | Credit Profile | Choose the Credit Profile tab. |  |  |
| 6 | Risk Class | In the Risk Class field, select a risk class from the list. | The risk class is assigned to the customer. |  |
| 7 | Save | Choose Save. |  |  |

##### Assign Semantic Tags to Financial Statement Versions

Purpose

In this activity, you assign semantic tags to the financial statement versions.

|  |
| --- |
| Note Only G/L accounts assigned to the Semantic Tag ACCREC/ ACCREC_OTH are considered for a Credit-Risk-Based Impairment run.If you maintain the financial statement version (FSV) via configuration step, you can search for Assign Semantic Tags to Financial Statement Versions in either the Manage Your Solution (F1241) app or the SAP CBC project experience, as mentioned below. The GL Account should be assigned to the FSV.If you maintain the FSV using the new Global Hierarchy tool, there is no need to perform the configuration below. Semantic tag functionality is already included into Global Hierarchy. Semantic Tag should be entered for required GL Accounts. |

This is required for the following test procedures:

- [Credit-Risk-Based Impairment](#unique_25) [page ] 154

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
2. For the Assign Semantic Tags to Financial Statement Versions row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Semantic Tags to Financial Statement Versions.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step# | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries.In the New Entry dialog box, select Assign Semantic Tag to G/L Account and choose Continue. |  |  |
| 2 | Map FSV to Semantic Tag | Make the following entries and choose Save:FS Vers: <FSV from prior step>Account From: <G/L account>Semantic Tag: ACCREC/ ACCREC OTH |  |  |

##### Define Rules for Impairment

Purpose

In this activity, you define the impairment rules. The following rules are delivered for impairment:

| Valuation Rule | Description |
| --- | --- |
| SCRI | Credit-Risk-Based Impairment |

Prerequisite

Before you start the Credit-Risk-Based Impairment process, you must assign the G/L accounts and probability of default.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Define Rules for Impairment row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Rules for Impairment.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Define Rules for Impairment | Select Valuation Rule SCRI (Credit-Risk-Based Impairment), and from the left pane, double-click Define Steps of an Impairment Rule. | The right pane shows the Define Rules for Impairment pane. |  |
| 2 | Define Steps of Impairment Rule | Select Valuation Rule Step – 0010 (Impairment of Receivables), and from the left pane, double-click Assign Semantic Tag to Impairment Rule. |  |  |
| 3 | Assign Semantic Tag to Impairment Rule | Select the checkbox for the FINS_SEM_TAG row, and from the left pane, double-click Assign Probability of Default to Aging Increment. |  |  |
| 4 | Assign Probability of Default to Aging Increment | For each Aging Increment and Risk Class, you must enter a Probability of Default. For example, you can use the following data for testing processes (the last number in each bullet below is the suggested probability of default value):A, I-12, 12/31/9999, 0.0500A, I-36, 12/31/9999, 0.5000A, I0, 12/31/9999, 1.0000A, I30, 12/31/9999, 2.0000A, I60, 12/31/9999, 5.0000A, I90, 12/31/9999, 10.0000 |  |  |
| 5 | Assign G/L Accounts for Impairment | In the left pane, double-click Assign G/L Accounts for Impairment. Make the following entries and choose Save:New/Change: 62020000Release: 62020000 |  |  |

|  |
| --- |
| Note If the customer is using the VALN account assignment rule, for controlling account assignment fields, the customer should maintain the P&L accounts of advanced valuation in the Manage Default Account Assignments configuration activity and assign them respectively to the default profit center or cost center.The customer can verify which account assignment rule he is using in the Assign Account Assignment Rules to Advanced Valuations configuration activity. |

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

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Define Rules for Impairment row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Rules for Impairment.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Define Rules for Impairment | Select this entry:SCRI (Credit-Risk-Based Impairment)Choose Copy as.Choose Save.Note Optionally, you can create an impairment rule as New Entry. |  |  |
| 2 | Define Steps of Impairment Rule | Copy an existing valuation rule step or create an entry:Business Transaction Type: RFIMAging: ImpairmentNote For new steps, you should select a value with the interval 1000 to 4999. Values starting with 00 cannot be included in entries created in the customer namespace. |  |  |
| 3 | Assign Semantic Tag to Impairment Rule | You need to define the semantic tags ACCREC and ACCREC OTH as filter values. You should assign one of these semantic tags to all G/L accounts to be considered in the impairment run. |  |  |
| 4 | Assign Probability of Default to Aging Increment | For each combination of aging increments and risk classes, you should specify a value for Probability of Default. |  |  |
| 5 | Assign G/L Accounts for Impairment | Assign the G/L accounts before you start the impairment process. For more information on the test data, see the section in this step. |  |  |

##### Assign Rules for Impairment to Accounting Principles

Purpose

If you create a customer-specific rule for credit-risk-based impairment in the prior [Define Rules for Impairment](#unique_28) [page ] 27 step, you must assign it to an accounting principle.

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

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Assign Rules for Impairment to Accounting Principles row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign Rules for Impairment to Accounting Principles.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Assign Rules for Impairment to Accounting Principles | Make the following entries and choose Save:Accounting Principle: AEAPValuation Rule: <new valuation rule> |  |  |

#### Relevant Configuration Steps for Post Balance Sheet Reclassification by Master Data Change

##### Define Aging Increments for Advanced Valuation

Purpose

In this activity, you define the aging increments for balance sheet reclassification of receivables and payables.

We deliver the following aging (with aging increments) for the balance sheet reclassification of receivables and payables:

Table 2: S3IRCL (Aging for Reclassification (3 increments))

| Aging Increment | Months | Days | Aging Increment Description | Text |
| --- | --- | --- | --- | --- |
| LONGTERM | 999 |  | Long-term more than 5 Years | Due >5Y |
| MIDTERM | 60 |  | Mid-term between 1 and 5 Years | 1Y<Due=<5Y |
| SHORTTERM | 12 |  | Short-term up to 12 Months | Due =<12M |

Table 3: SGLOBRCL (Aging for Global AP Reclassification (IFRS, USGAAP))

| Aging Increment | Months | Days | Aging Increment Description | Text |
| --- | --- | --- | --- | --- |
| CURRENT | 1 |  | Current up to 12 Months | Due =<12M |
| NONCURRENT | 2 |  | Non-current more than 12 Months | Due >12M |

|  |
| --- |
| Note If needed, you can create additional aging or aging increments with this procedure. |

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

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Define Aging Increments for Advanced Valuation row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Aging Increments for Advanced Valuation.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step | Test Step Name | Instructions | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Define New Aging for Reclassification | Make the following entries and choose Save:Aging: <new aging codification>Description: <new aging description>Aging Category: REC Reclassification |  |  |

##### Define Rules for Balance Sheet Reclassification by Maturity

Purpose

In this activity, you define the rules for balance sheet reclassification by maturity and select the Master Data Changed checkbox for valuation rules to recognize changed master data for posting.

Procedure

For more information, see the [Define Rules for Balance Sheet Reclassification by Maturity](#unique_32) [page ] 39 topic in the next section. For valuation rules that need to recognize changed master data for posting, ensure you select the Master Data Changed checkbox for those rules.

##### Define Rules for B/S Reclassification by Master Data Change

Purpose

In this activity, you define the rules for balance sheet reclassification by master data change.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Define Rules for B/S Reclassification by Master Data Change row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Rules for B/S Reclassification by Master Data Change.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Copy | Select a valuation rule.Choose Copy as.Choose Copy. |  |  |
| 2 | Define Steps | Select the checkbox for your copied rule and in the Dialog Structure pane, double-click Define Steps of a Reclassification by MDS Rule. |  |  |
| 3 | Enter Details | Make the following entries:Valuation Rule Step: <step number>Val Rule Step Description: <description>Business Transaction Type: <transaction type>Business Transaction Type Description: <description> |  |  |
| 4 | Save | Save your entries. |  |  |

##### Assign Semantic Tags to Financial Statement Versions

Purpose

In this activity, you assign semantic tags to the financial statement versions.

|  |
| --- |
| Note Only G/L accounts assigned to the semantic tag ACCPAY/ ACCREC are considered for a Balance Sheet Reclassification by Master Data Change run.If you maintain the financial statement version (FSV) via configuration step, you can search for Assign Semantic Tags to Financial Statement Versions in either the Manage Your Solution (F1241) app or the SAP CBC project experience, as mentioned below. The GL Account should be assigned to the FSV.If you maintain the FSV using the new Global Hierarchy tool, you don't need to perform the following configuration. Semantic tag functionality is already included in the Global Hierarchy. Semantic Tag should be entered for required GL Accounts.This is required for the following test procedures:[Post B/S Reclassification - Master Data Change](#unique_35) [page ] 156 |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Chart of Accounts, choose Details (>).
2. For the Assign Semantic Tags to Financial Statement Versions row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Assign Semantic Tags to Financial Statement Versions.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. | The New Entry dialog box is displayed. |  |
| 2 | Assign Semantic Tag to G/L Account | Select Assign Semantic Tag to G/L Account and choose Continue. |  |  |
| 3 | Map FSV to Semantic Tag | Make the following entries and choose Save:FS Vers: <FSV from prior step>Account From: <G/L account>Semantic Tag: ACCREC/ACCPAY |  |  |

##### Assign Rules for Balance Sheet Reclassification by Master Data Change to Accounting Principle

Purpose

In this activity, you assign the rules for balance sheet reclassification by master data change to the accounting principle.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Assign Rules for B/S Reclassifctn by Master Data Change to Acctg Principle row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Assign Rules for B/S Reclassifctn by Master Data Change to Acctg Principle.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Enter Details | Make the following entries and choose Save:Accounting Principle: <accounting principle>Ledger: <ledger>Valuation Rule: <rule defined in prior step> |  |  |

#### Relevant Configuration Steps for Post Balance Sheet Reclassification by Maturity

##### Define Aging Increments for Advanced Valuation

Purpose

In this activity, you define the aging increments for balance sheet reclassification of receivables and payables.

We deliver the following aging (with aging increments) for the balance sheet reclassification of receivables and payables:

Table 4: S3IRCL (Aging for Reclassification (3 increments))

| Aging Increment | Months | Days | Aging Increment Description | Text |
| --- | --- | --- | --- | --- |
| LONGTERM | 999 |  | Long-term more than 5 Years | Due >5Y |
| MIDTERM | 60 |  | Mid-term between 1 and 5 Years | 1Y<Due=<5Y |
| SHORTTERM | 12 |  | Short-term up to 12 Months | Due =<12M |

Table 5: SGLOBRCL (Aging for Global AP Reclassification (IFRS, USGAAP))

| Aging Increment | Months | Days | Aging Increment Description | Text |
| --- | --- | --- | --- | --- |
| CURRENT | 1 |  | Current up to 12 Months | Due =<12M |
| NONCURRENT | 2 |  | Non-current more than 12 Months | Due >12M |

|  |
| --- |
| Note If needed, you can create additional aging or aging increments with this procedure. |

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

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Define Aging Increments for Advanced Valuation row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Aging Increments for Advanced Valuation.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step | Test Step Name | Instructions | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Define New Aging for Reclassification | Make the following entries and choose Save:Aging: <new aging codification>Description: <new aging description>Aging Category: REC Reclassification |  |  |

##### Define Rules for Balance Sheet Reclassification by Maturity

Purpose

In this activity, you define reclassification rules. We deliver the following rules for reclassification.

| Valuation Rule | Valuation Rule Description |
| --- | --- |
| SBSR | B/S Reclassification (Global AP) |
| SLBS | B/S Reclassification (3 increments) |

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

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Define Rules for B/S Reclassification by Maturity row, choose Configure.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Rules for B/S Reclassification by Maturity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step# | Test Step Name | Instructions | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Define Rules for Reclassification | Select one of the following entries:SBSR (B/S Reclassification (Global AP))SLBS (B/S Reclassification (3 increments))Choose Copy as.Choose Copy.Note There's also an option to create a reclassification rule as a new entry. |  |  |
| 2 | Define Reclassification Rule Steps | Copy an existing valuation rule step or create an entry.Caution We recommend that customers leave the Grouping Rule field empty. By doing so, the system automatically uses a reasonable fallback rule.For customers using in-house banking, we recommend creating a separate rule step for IHB accounts in addition to the predelivered 0010 rule. For the new rule, assign SIHB Reclassification Grouping Rule for In-House Banking.We also recommend that customers with in-house banking complete customizing steps mentioned in the Relevant Configuration Steps for Post Balance Sheet Reclassification section of the Prerequisites section in the In-House Banking (6BP) test script. See that scope item's test script for more information.Note For B/S Reclassification - Maturity to recognize changed master data and post accordingly, you must select the Master Data Changed checkbox.When you run [Post B/S Reclassification - Master Data Change](#unique_35) [page ] 156, then run [Post B/S Reclassification - Maturity](#unique_38) [page ] 158 after, the system recognizes postings done based on changed master data and uses them in the Maturity step.If you copied an existing rule in the prior step, select the checkbox for the rule and in the Dialog Structure pane, double-click Define Steps of a Reclassification Rule.Make the following entries:Aging for Liabilities: <aging>; see following noteNote You can assign a different aging (Aging for Assets and Aging for Liabilities): SGLOBRCL, S3IRCL, or one created as a customer entry. |  |  |
| 3 | Assign G/L Accounts for Reclassification | Define the G/L accounts and reclassification method to run the Reclassification process.For each of the rules you created and its corresponding step, assign accounts according the tables in the Valuation Rules section below. |  |  |

Valuation Rules

Table 6: Valuation Rule SBSR (B/S Reclassification (Global AP))

| Chart of Accounts | Target Account | Aging | Aging Increment | Source Account | Reclassification Method | Explanation |
| --- | --- | --- | --- | --- | --- | --- |
| YCOA | 12100000 | SGLOBRCL | CURRENT | 12101000 | Debit balance | Reclassification of debit balance from long-term Receivable account to short-term Receivable account |
| YCOA | 12100000 | SGLOBRCL | CURRENT | 21100000 | Debit balance | Reclassification of debit balance from short-term Payable account to short-term Receivable account |
| YCOA | 12101000 | SGLOBRCL | NONCURRENT | 12100000 | Debit balance | Reclassification of debit balance from short-term Receivable account to long-term Receivable account |
| YCOA | 12101000 | SGLOBRCL | NONCURRENT | 21100000 | Debit balance | Reclassification of debit balance from short-term Payable account to long-term Receivable account |
| YCOA | 21100000 | SGLOBRCL | CURRENT | 12100000 | Credit balance | Reclassification of credit balance from short-term Receivable account to short-term Payable account |
| YCOA | 21100200 | SGLOBRCL | NONCURRENT | 12100000 | Credit balance | Reclassification of credit balance from short-term Receivable account to long-term Payable account |
| YCOA | 21100200 | SGLOBRCL | NONCURRENT | 21100000 | Credit balance | Reclassification of credit balance from short-term Payable account to long-term Payable account |

Table 7: Valuation Rule SLBS (B/S Reclassification (3 increments))

| Chart of Accounts | Target Account | Aging | Aging Increment | Source Account | Reclassification Method | Explanation |
| --- | --- | --- | --- | --- | --- | --- |
| YCOA | 12100000 | SGLOBRCL | CURRENT | 12101000 | Debit balance | Reclassification of debit balance from long-term Receivable account to short-term Receivable account |
| YCOA | 12100000 | SGLOBRCL | CURRENT | 21100000 | Debit balance | Reclassification of debit balance from short-term Payable account to short-term Receivable account |
| YCOA | 12100000 | SGLOBRCL | CURRENT | 21100200 | Debit balance | Reclassification of debit balance from mid-term Payable account to short-term Receivable account |
| YCOA | 12100000 | SGLOBRCL | CURRENT | 21100300 | Debit balance | Reclassification of debit balance from log-term Payable account to short-term Receivable account |
| YCOA | 12101000 | SGLOBRCL | NONCURRENT | 12100000 | Debit balance | Reclassification of debit balance from short-term Receivable account to long-term Receivable account |
| YCOA | 12101000 | SGLOBRCL | NONCURRENT | 21100000 | Debit balance | Reclassification of debit balance from short-term Payable account to long-term Receivable account |
| YCOA | 12101000 | SGLOBRCL | NONCURRENT | 21100200 | Debit balance | Reclassification of debit balance from mid-term Payable account to long-term Receivable account |
| YCOA | 12101000 | SGLOBRCL | NONCURRENT | 21100300 | Debit balance | Reclassification of debit balance from long-term Payable account to long-term Receivable account |
| YCOA | 21100000 | S3IRCL | SHORTTERM | 12100000 | Credit balance | Reclassification of credit balance from short-term Receivable account to short-term Payable account |
| YCOA | 21100200 | S3IRCL | MIDTERM | 12100000 | Credit balance | Reclassification of credit balance from short-term Receivable account to mid-term Payable account |
| YCOA | 21100300 | S3IRCL | LONGTERM | 12100000 | Credit balance | Reclassification of credit balance from short-term Receivable account to long-term Payable account |
| YCOA | 21100200 | S3IRCL | MIDTERM | 21100000 | Credit balance | Reclassification of credit balance from short-term Payable account to mid-term Payable account |
| YCOA | 21100300 | S3IRCL | LONGTERM | 21100000 | Credit balance | Reclassification of credit balance from short-term Payable account to long-term Payable account |
| YCOA | 21100000 | S3IRCL | SHORTTERM | 21100200 | Credit balance | Reclassification of credit balance from mid-term Payable account to short-term Payable account |
| YCOA | 21100300 | S3IRCL | LONGTERM | 21100200 | Credit balance | Reclassification of credit balance from mid-term Payable account to long-term Payable account |
| YCOA | 21100200 | S3IRCL | MIDTERM | 21100300 | Credit balance | Reclassification of credit balance from long-term Payable account to mid-term Payable account |
| YCOA | 21100000 | S3IRCL | SHORTTERM | 21100300 | Credit balance | Reclassification of credit balance from long-term Payable account to short-term Payable account |
| YCOA | 21100200 | S3IRCL | MIDTERM | 12101000 | Credit balance | Reclassification of credit balance from long-term Receivable account to mid-term Payable account |
| YCOA | 21100000 | S3IRCL | SHORTTERM | 12101000 | Credit balance | Reclassification of credit balance from long-term Receivable account to short-term Payable account |
| YCOA | 21100300 | S3IRCL | LONGTERM | 12101000 | Credit balance | Reclassification of credit balance from long-term Receivable account to long-term Payable account |

##### Assign Reclassification Rules to Accounting Principles

Purpose

If you created a customer-specific reclassification rule in the prior step, you must assign it to an accounting principle.

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

1. For the row with Item Name of Ledgers and Valuation, choose Details (>).
2. For the Assign B/S Reclassification Rules to Accounting Principles row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Assign B/S Reclassification Rules to Accounting Principles.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step# | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Assign Reclassification Rules to Accounting Principle | Make the following entries and choose Save:Accounting Principle: AEAPReclassification Rule: <new valuation rule> |  |  |

#### Relevant Configuration Steps for Statement of Changes in General Ledger

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
2. For the Define Structure for Statement of Changes in General Ledger row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Structure for Statement of Changes in General Ledger.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step# | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Statement of Changes (SOC) Type | Make the following entries and choose Save:SOC Type: <new SOC type codification>Description: <new SOC type description> |  |  |

|  |
| --- |
| Note To assign the semantic tags and the transaction types to the statement of changes (SOC), select the SOC type you previously defined, then in the Dialog Structure pane, double-click Assign Semantic Tags to SOC Type and then double-click Assign Transaction Types to SOC Type. |

#### Add Multiple Accounts Using Expert Worklist

Purpose

In this activity, you manage the operating chart of accounts using Expert Worklist functionality. This lets you add multiple accounts using a spreadsheet template.

|  |
| --- |
| Note If you only want to add an individual account, you can use the [Manage Operating Chart of Accounts](#unique_42) [page ] 67 step in the Test Procedures section instead. |

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
2. For the Manage Operating Chart of Accounts row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Manage Operating Chart of Accounts.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step Number | Test Step Name | Instructions | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Enable Expert Worklist | At the top right, toggle the Expert Worklist to the right to turn it on. | New actions are visible in the List View table. |  |
| 2 | Enter Details | Make the following entries and choose Go:Chart of Accounts: <chart of accounts>, for example, YCOAFinancial Statement Version: <financial statement version> | The list of G/L accounts is displayed. |  |
| 3 | Download Template | Choose Change Worklist > Download Template . | The template is downloaded to your local system. |  |
| 4 | Update Template | In your spreadsheet program, update the file.Note For specifics on how to work with the template, see the [How to Create Multiple G/L Accounts Using a Spreadsheet](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/c79e0a33980144e7b83b09aef89302d2.html) page on the Help Portal. |  |  |
| 5 | Upload Template | In the app, choose Change Worklist > Upload Spreadsheet . | The Upload Spreadsheet dialog box is displayed. |  |
| 6 | Upload Template | Browse for your file, then choose Upload.Confirm the informational dialog box. | The spreadsheet is uploaded. Your new accounts are shown in the List View. |  |
| 7 | Change Assigned Company Codes | If you want to change the company codes assigned to a new account, select the checkbox for one or more new accounts and choose Assign Company Codes. | The Company Code Assignment dialog box is displayed. |  |
| 8 | Change Assigned Company Codes | Select or deselect the company codes you want to assign to the accounts. Once done, choose Apply.Confirm the informational dialog box. | The Company Code column is updated to show the assigned company codes. |  |
| 9 | Complete Action | Once you have updated the company code assignment, select the checkboxes for the new G/L accounts and choose Complete Action. | The system displays an informational dialog box to notify you that the job to create the G/L accounts is started. |  |
| 10 | Confirm | Confirm the informational dialog box. To view the log for the job status, choose View Logs. | The Application Logs view is displayed. Review the logs to see the status of the account creation job. |  |

#### Define Balance Validation Rules and Groups - Upload Rules

Purpose

Balance validation ensures data quality during period-end close of a business entity. It checks that balance sheet and P&L account data is complete, correct, and compliant with user-defined rules. These validation rules can be based on legislation, best practices, or company policies.

|  |
| --- |
| Caution Sample rules and groups using Financial Statement Version (FSV) 1799 are defined and attached to SAP Note [3322100](https://me.sap.com/notes/3322100). If you are using that FSV, you can download the file from the note and upload it using this procedure. If you use a different FSV for your country/region, you can either import the rules and change the values before you activate, or create your own testing rules from scratch using the guidance in the next note. |

|  |
| --- |
| Note For more information, see the [Balance Validation](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/8c1fce9f709f482cb890bc440fbb79bd.html) pages on the SAP Help Portal.To create basic rules, see this [page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/b3b203c626304229aef1bbd74324ec0b.html).To create compound rules, see this [page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/994c8a4b5fe64b9d8849628ea6d82910.html).To assign rules to groups, see this [page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/f2555238929a47b7bc7577e96f3c8bc4.html).To activate or deactivate rules and groups, see this [page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/de84984a8f244a7391cc0ee22264c8fd.html). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Balance Validation Rules and Groups (F6386). |  |  |
| 3 | Import Groups and Rules | At the top right corner of the table, choose Export Table > Import . | The Open dialog box is displayed. |  |
| 4 | Browse and Open File | Locate and select the XLSX file that you downloaded from the SAP Note. Choose Open. | The Import/Export Validation Settings view is displayed. |  |
| 5 | Review Your Rules | Your rules are shown on the New for Import tab. If there are any duplicated rules or rules where the import failed, they're shown on the relevant tab. Once you review your rules, choose Import.Note You can click on the rule ID number (blue text) to see the details of the rule. | The Imported tab shows a count of the rules and groups that were imported. The rules are activated by default.Note You can choose the Imported tab to view a list of the imported rules and groups. |  |
| 6 | Back | Choose Back. |  |  |
| 7 | View Groups | In the Groups pane, locate your imported group and choose > (Details). | The right pane expands and displays a list of rules in the group. |  |
| 8 | View Rules | Click one of the rule ID numbers (blue text) to see a dialog box with a summary of the rule. Choose View Rule to see more information. Choose Back when done. |  |  |
| 9 | Close Right Pane | Close the right pane. |  |  |
| 10 | Rules | Choose the Rules tab. | A list of rules are displayed. |  |
| 11 | View Rule | For one of the rules, choose > (Details) at the right of the row.Note If you click the Rule ID number (blue text), a summary is shown in a modal dialog box. If you choose View Rule in this dialog box, the same result occurs as if you chose > (Details). | The Define Validation Rules view is displayed. Information about the rule is shown on this view. |  |
| 12 | Back | Choose Back. |  |  |

#### Define Financial Statement Version in Global Hierarchies

Purpose

In this activity, you define the financial statement version.

|  |
| --- |
| Note Only relevant for access via Manage Your Solution > Configure Your Solution : If you can’t use the Define Financial Statement Versions in Global Hierarchies configuration step, you can log in as a General Ledger Accountant and use the Manage Global Hierarchies (F2918) app. |

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
2. For the Define Financial Statement Versions in Global Hierarchies row, choose Configure.
3. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Financial Statement Versions in Global Hierarchies.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Process Step# | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add Selection Criteria | Choose Import Hierarchy. | The Import Hierarchy view is displayed. |  |
| 2 | Add Selection Criteria | Make the following entries and choose OK:Source: Maintain Financial Statement VersionsFinancial Statement Version ID: 3310 | The Create a Hierarchy Based On view is displayed. |  |
| 3 | Add Selection Criteria | Make the following entries and choose Create:Type: Financial Statement VersionHierarchy ID: <Hierarchy ID>Hierarchy Description: <description>Chart of Accounts: YCOAValid From: <beginning of year>Valid To: 12/31/9999 | The FSV is created as a draft. The Manage Global Hierarchy view is displayed. |  |
| 4 | Add Selection Criteria | For the draft FSV you created, choose Details (>). | The right pane is displayed. |  |
| 5 | Edit | Choose Edit. |  |  |
| 6 | Timeframe | Choose the Timeframe tab. |  |  |
| 7 | Choose Node | Expand the relevant node. |  |  |
| 8 | Add Details | Assign the semantic tag.When done, choose OK. |  |  |
| 9 | Save | Choose Save and Activate. |  |  |

#### Migrate Financial Statement Versions to Global Hierarchies

Purpose

This activity lets you migrate financial statement versions (FSV) to the global hierarchy.

|  |
| --- |
| Note You can also use this app to set FSVs as not migration-relevant, or undo a migration if you encountered an error. |

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
2. For the Migrate Financial Statement Versions to Global Hierarchies row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Migrate Financial Statement Versions to Global Hierarchies.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail /Comment |
| --- | --- | --- | --- | --- |
| 1 | FSV Details | On the Hierarchy Types tab, for the Financial Statement Version hierarchy type, choose Details (>). | The view changes to display the financial statement version and the hierarchy items. |  |
| 2 | Item Details | For one of the items in the Items pane, choose Details(>). | The details for the selected hierarchy item are displayed in a new view. |  |
| 3 | Back | Choose Back. |  |  |
| 4 | Show Not Started | Above the list of items in the Items pane, choose Not Started from the dropdown.Note You can also filter by In Progress, Migrated, or Not Relevant. | The list is filtered to only show the hierarchy items that haven't started migration. |  |
| 5 | Migrate FSVs | Select the checkbox for an item and choose Migrate. | A new view is displayed. The item is migrated. The system displays the list of hierarchy items, excluding the one you just migrated. |  |
| 6 | Show Migrated | Above the list of items in the Items pane, choose Migrated from the dropdown. | The item you migrated is shown in the filtered list along with other migrated items.Note To check this, you can use the Manage Global Hierarchies (F2918) app to search for the hierarchy item you migrated. |  |

#### Replicate Runtime Hierarchy

Purpose

You must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the back-end database hierarchy tables. Normally, this would be created as a periodic job that would run in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Replicate Runtime Hierarchy (F1478). | The Application Jobs view is displayed. |  |
| 3 | Create | Choose the Create button. | The New Job: Replicate Runtime Hierarchy (SAP) view is displayed. |  |
| 4 | Enter Header Data | In the header area, make the following entries and choose Step 2:Job Template: Replicate Runtime HierarchyJob Name: Manual test |  |  |
| 5 | Start | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Hierarchy ID | Make the following entries and choose Schedule:Hierarchy ID: YPS2By Date: <Select>Version Older than: 1 dayNote If you are using the optional procedure Commitment Management and Cost Center Budgeting, follow steps 1-4, but make the following entries instead:Job Template: Manually Replicate Runtime HierarchyHierarchy ID: 0102/YCOA/YBA000_CE |  |  |

## Overview Table

The Accounting and Financial Close scope item consists of several process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage G/L Account Master Data](#unique_48) [page ] 59 | Configuration Expert - Business Process ConfigurationorGeneral Ledger Accountant | Manage Your Solution (F1241) or Manage G/L Account Master Data (F0731A) | The G/L Account is created in the chart of accounts and company code. The G/L Account can be created, changed, copied in the chart of account and company code. Multiple G/L accounts can be maintained through Mass Change. |
| [Define Financial Statement Versions](#unique_19) [page ] 63 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | You maintained the financial statement version. |
| [Manage Chart of Accounts](#unique_49) [page ] 66 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) | You managed the chart of accounts. |
| [Manage Operating Chart of Accounts](#unique_42) [page ] 67 | General Ledger Accountant | Manage Operating Chart of Accounts (F0763B) | You managed the chart of accounts. |
| [Manage Operating G/L Account](#unique_50) [page ] 69 | Configuration Expert - Business Process Configuration | Manage Your Solution (F1241) or Manage Operating G/L Accounts (F0731B) | You managed the operating G/L account. |
| [Manage Alternative Chart of Accounts](#unique_51) [page ] 73 | General Ledger Accountant | Manage Alternative Chart of Accounts (F8390) | You created an alternative chart of accounts. |
| [Synchronize G/L Account Master Data](#unique_52) [page ] 74 | General Ledger Accountant | Synchronize G/L Account Master Data (OB_GLACC71) | You downloaded the changed master data into a text file. |
| [G/L Account Changes](#unique_53) [page ] 76 | General Ledger Accountant | G/L Account Changes - Central View (FS04) | Display the changes to a G/L account master record. |
| [Manage Profit Center Group](#unique_54) [page ] 77 | Divisional Accountant | Manage Profit Center Groups (F0764) | The Profit Center Group is maintained. |
| [Manage Profit Centers](#unique_55) [page ] 78 | General Ledger Accountant or Divisional Accountant | Manage Profit Centers - New Version (F3516A) | The Profit Center Master is maintained. |
| [Edit Profit Centers Collective](#unique_56) [page ] 79 | Divisional Accountant | Edit Profit Centers - Collective (KE55) | Make changes to large quantities of profit center master data without having to change the master data for each single profit center. |
| [Edit Company Code Assignment Profit Centers](#unique_57) [page ] 81 | Divisional Accountant | Edit Company Code Assignment Profit Centers - Old Version (KE56) | Make changes to the company code assignments of a larger number of profit centers without having to change the master data for each single profit center. |
| [Where-Used List - Profit Centers](#unique_58) [page ] 82 | Divisional Accountant | Where-Used List - Profit Centers (F3751) |  |
| [Change Log - Profit Centers](#unique_59) [page ] 83 | General Ledger Accountant or Divisional Accountant | Change Log - Profit Centers (F3810) |  |
| [Manage Journal Entry Template](#unique_60) [page ] 84 | General Ledger Accountant | Manage Journal Entry Templates (F3803) | You created a template for general journal entries. |
| [Post General Journal Entries](#unique_61) [page ] 86 | General Ledger Accountant | Post General Journal Entries (F0718) | The General Ledger journal entry is posted. The system has automatically added the Input tax amount. |
| [Post with Auto-Reverse](#unique_62) [page ] 89 | General Ledger Accountant | Post General Journal Entries (F0718) | You posted the journal entry with automatic reversal. |
| [Upload General Journal Entries](#unique_63) [page ] 92 | General Ledger Accountant | Upload General Journal Entries (F2548) | The G/L journal entries are posted. |
| [Verify General Journal Entries](#unique_64) [page ] 93 | General Ledger Accountant | Verify General Journal Entries - For Requester (F2547A) | All journal entries submitted for checking are displayed. |
| [Verify General Journal Entries - with Auto-Reverse](#unique_65) [page ] 97 | General Ledger Accountant | Verify General Journal Entries - For Requester (F2547A) | Journal entries are submitted for auto-reversal. |
| [Withdraw Verify General Journal Entries](#unique_66) [page ] 99 | General Ledger Accountant | Verify General Journal Entries - For Requester (F2547A) | The journal entry is withdrawn. |
| [Approve Verify General Journal Entries (for Processor - Inbox)](#unique_10) [page ] 100 | General Ledger Accountant for United Arab Emirates | Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728) | All journal entries received for approval are displayed. |
| [Forward Verify General Journal Entries (for Processor - Inbox)](#unique_67) [page ] 102 | General Ledger Accountant for United Arab Emirates | Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728) | All journal entries checked by the user are displayed. |
| [Reject Verify General Journal Entries (for Processor - Inbox)](#unique_68) [page ] 103 | General Ledger Accountant for United Arab Emirates | Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728) | All journal entries checked by the user are displayed. |
| [Edit a Rejected Verify General Journal Entry (Requester)](#unique_69) [page ] 104 | General Ledger Accountant | Verify General Journal Entries - For Requester (F2547A) | All submitted journal entries are displayed. |
| [Manage Journal Entries](#unique_70) [page ] 105 | General Ledger Accountant | Manage Journal Entries (F0717A) | You displayed the journal entries. |
| [Open Correspondence](#unique_71) [page ] 106 | General Ledger Accountant | Manage Journal Entries (F0717A) | Correspondence is created according to the selected criteria. |
| [Reverse General Journal Entries](#unique_72) [page ] 108 | General Ledger Accountant | Post General Journal Entries (F0718) | You reversed the journal entries. |
| [Display Journal Entries](#unique_73) [page ] 110 | General Ledger Accountant | Display Journal Entries (F7697) | You displayed the journal entries. |
| [Display Document Flow](#unique_74) [page ] 111 | General Ledger Accountant | Display Document Flow (F3665) | You displayed the document flow. |
| [Display G/L Account Balances](#unique_75) [page ] 112 | General Ledger Accountant | Display G/L Account Balances (F0707A) | The G/L Account Balances view is displayed. |
| [Display Line Items in General Ledger](#unique_76) [page ] 113 | General Ledger Accountant | Display Line Items in General Ledger (F2217) | A list of all relevant line items is displayed. |
| [Display Line Item Entry](#unique_77) [page ] 114 | General Ledger Accountant | Display Line Item Entry (F2218) | A list of all relevant line items is displayed. |

[Manage Recurring Journal Entries](#unique_78) [page ] 115

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Recurring Journal Entry](#unique_79) [page ] 116 | General Ledger Accountant | Manage Recurring Journal Entries (F1598) | The Manage Recurring Journal Entries: Header Data view is displayed. |
| [Display Recurring Journal Entry](#unique_80) [page ] 117 | General Ledger Accountant | Manage Recurring Journal Entries (F1598) | The Manage Recurring Journal Entries: Header Data view is displayed. |
| [Edit Recurring Journal Entry](#unique_81) [page ] 118 | General Ledger Accountant | Manage Recurring Journal Entries (F1598) | The Manage Recurring Journal Entries: Header Data view is displayed. |
| [Copy Recurring Journal Entry](#unique_82) [page ] 119 | General Ledger Accountant | Manage Recurring Journal Entries (F1598) | The Manage Recurring Journal Entries: Header Data view is displayed. |
| [Post Recurring Journal Entry](#unique_83) [page ] 119 | General Ledger Accountant | Manage Recurring Journal Entries (F1598) | The Manage Recurring Journal Entries: Header Data view is displayed. |
| [Delete Recurring Journal Entry](#unique_84) [page ] 120 | General Ledger Accountant | Manage Recurring Journal Entries (F1598) | The Manage Recurring Journal Entries: Header Data view is displayed. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Display Changes of Recurring Entry](#unique_85) [page ] 121 | General Ledger Accountant | Display Changes of Recurring Entry (FBD4) | The G/L Account Line Items - G/L View screen displays. |
| [Audit Journal](#unique_86) [page ] 122 | General Ledger Accountant | Audit Journal (F0997) |  |
| [Journal Entry Analyzer](#unique_87) [page ] 123 | General Ledger Accountant | Journal Entry Analyzer (F0956A)Journal Entry Analyzer - New Version (F0956B) |  |
| [Clear G/L Accounts - Manual Clearing](#unique_88) [page ] 126 | General Ledger Accountant | Clear G/L Accounts - Manual Clearing (F1579) | The Clear G/L Accounts (F1579) view is displayed. |
| [Clear G/L Accounts](#unique_89) [page ] 128 | General Ledger Accountant | Clear G/L Accounts - Manual Clearing (F1579) | The Post General Journal Entries (F0718) view is displayed. |
| [Reset Cleared Items](#unique_90) [page ] 130 | General Ledger Accountant | Reset Cleared Items (F2223) |  |
| [Schedule Jobs to Reset Cleared Items (Optional)](#unique_91) [page ] 131 | General Ledger Accountant | Schedule Jobs to Reset Cleared Items (F9296) | You scheduled jobs to reset cleared items. |
| [Clear Open Items Automatically](#unique_92) [page ] 133 | General Ledger Accountant | Clear Open Items Automatically (F.13) | The Post General Journal Entries (F0718) view is displayed. |
| [Currency Exchange Rates](#unique_93) [page ] 134 | General Ledger Accountant | Currency Exchange Rates (F3616) | The Change View "Currency Exchange Rates"; Overview view is displayed. |
| [Import Foreign Exchange Rates](#unique_94) [page ] 134 | General Ledger Accountant | Import Foreign Exchange Rates (F2092) | The Import Foreign Exchange Rates (F2092) view is displayed. |
| [Repost GR/IR Clearing](#unique_95) [page ] 135 | General Ledger Accountant | Repost GR/IR Clearing (F.19) | The Analyze GR/IR Clearing Accounts and Display Acquisition Tax view is displayed. |
| [Perform Foreign Currency Valuation](#unique_96) [page ] 137 | General Ledger Accountant | Perform Foreign Currency Valuation (FAGL_FCV) | The Foreign Currency Valuation view is displayed. |
| [Post Currency Adjustments](#unique_97) [page ] 140 | General Ledger Accountant | Post Currency Adjustments (F1606) | Currency adjustments are posted. |
| [Verify Currency Adjustments](#unique_98) [page ] 141 | General Ledger Accountant | Verify Currency Adjustments - For Requester (F4670A) | You verified a currency adjustment. |
| [Withdraw Verify Currency Adjustments](#unique_99) [page ] 144 | General Ledger Accountant | Verify Currency Adjustments - For Requester (F4670A) | The currency adjustment is withdrawn. |
| [Approve Verify Currency Adjustments (for Processor- Inbox)](#unique_11) [page ] 145 | General Ledger Accountant for United Arab Emirates | Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728) | You approved a currency adjustment. |
| [Forward Verify Currency Adjustments (for Processor- Inbox)](#unique_100) [page ] 147 | General Ledger Accountant for United Arab Emirates | Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728) | You forwarded a currency adjustment. |
| [Reject Verify Currency Adjustments (for Processor- Inbox)](#unique_101) [page ] 148 | General Ledger Accountant for United Arab Emirates | Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728) | You rejected a currency adjustment. |
| [Edit a Rejected Verify Currency Adjustment (Requester)](#unique_102) [page ] 149 | General Ledger Accountant | Verify Currency Adjustments - For Requester (F4670A) | You edited a rejected currency adjustment. |
| [Verify Data Flow](#unique_103) [page ] 150 | General Ledger Accountant | Verify Data Flow (ACC_ECS_MAINTAIN) |  |
| [Perform Advanced Foreign Currency Valuation](#unique_13) [page ] 151 | General Ledger Accountant | Schedule General Ledger Jobs (F1927) | You performed the valuation run. |
| [Analyze Closing Run Results](#unique_104) [page ] 153 | General Ledger Accountant | Analyze Closing Run Results (F3753) | You analyzed the results of the closing run. |
| [Credit-Risk-Based Impairment](#unique_25) [page ] 154 | General Ledger Accountant | Schedule General Ledger Jobs (F1927) | You performed the impairment run. |
| [Post B/S Reclassification - Master Data Change](#unique_35) [page ] 156 | General Ledger Accountant | Schedule General Ledger Jobs (F1927) | The reclassification is posted. |
| [Post B/S Reclassification - Maturity](#unique_38) [page ] 158 | General Ledger Accountant | Schedule General Ledger Jobs (F1927) | The reclassification is posted. |
| [Manage Posting Periods](#unique_105) [page ] 161 | General Ledger Accountant | Manage Posting Periods - Cost Accounting (F4684) or Manage Posting Periods (F2293) | The Manage Posting Periods (F2293) view is displayed. |
| [Post Tax Payables](#unique_106) [page ] 162 | General Ledger Accountant | Post Tax Payables (F1597) | The Post Tax Payables: Header Data screen displays. |

General Ledger - Periodic Activities

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Tax Reconciliation Account Balance](#unique_107) [page ] 164 | General Ledger Accountant | Tax Reconciliation Account Balance (F2095) | The Tax Reconciliation Account Balance (F2095) view is displayed. |
| [Tax Declaration Reconciliation](#unique_108) [page ] 165 | General Ledger Accountant | Tax Declaration Reconciliation (F2096) | The Tax Declaration Reconciliation (F2096) view is displayed. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Withholding Tax Calculation Analysis Report (Optional)](#unique_109) [page ] 166 | General Ledger Accountant | Withholding Tax Calculation Analysis (F7977) | You performed the report. |
| [Regroup Receivables/Payables](#unique_110) [page ] 169 | General Ledger Accountant | Regroup Receivables / Payables (FAGLF101) | The receivables and payables are regrouped, and transfer postings are performed. |
| [Process Batch Input Session](#unique_111) [page ] 170 | General Ledger Accountant | Batch Input Sessions in My Area (SM35SA) | Journal entries are posted and recurring documents are updated with processing data. |
| [Import Financial Plan Data](#unique_112) [page ] 171 | General Ledger Accountant | Import Financial Plan Data (F1711) | The balance sheet and P&amp;L accounts are planned. |
| [Balance Sheet / Income Statement](#unique_113) [page ] 173 | General Ledger Accountant | Balance Sheet/Income Statement (F0708) | The financial statement is displayed. |
| [Financial Statement Download and Printing](#unique_114) [page ] 174 | General Ledger Accountant | Balance Sheet/Income Statement - Multidimensional (W0161) | The financial statement is downloaded in Excel format. |
| [Financial Statements Review Booklet](#unique_115) [page ] 175 | General Ledger Accountant | Financial Statements - Review Booklet (F8587) | You reviewed the financial statements. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Trial Balance](#unique_116) [page ] 177 | General Ledger Accountant | Trial Balance (F0996) | The trial balance displays. |
| [Year-to-Date Balances](#unique_117) [page ] 178 | General Ledger Accountant | Year-to-Date Balances (W0177) | You displayed the year-to-date balances. |
| [Balance Carryforward Status](#unique_118) [page ] 179 | General Ledger Accountant | Balance Carryforward Status (F4683) | You reviewed the status of the balance carryforward jobs. |

| Process Step | Business Role | Transaction / App | Expected Results |
| --- | --- | --- | --- |
| [Display Journal Entries - in T-Account View](#unique_119) [page ] 180 | General Ledger Accountant | Display Journal Entries - In T-Account View (F3664) | You viewed the accounting impact of the document. |
| [Statement of Changes in General Ledger](#unique_120) [page ] 180 | General Ledger Accountant | Statement of Changes in General Ledger (W0162) | You reviewed the statement of changes. |
| [General Ledger Overview](#unique_121) [page ] 182 | General Ledger Accountant | General Ledger Overview (F2445) | You reviewed the general ledger overview. |

Balance Validation

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Schedule Balance Validation Jobs](#unique_122) [page ] 185 | General Ledger Accountant | Schedule Balance Validation Jobs - Accounting (F7470) | You scheduled the balance validation jobs. |
| [View Balance Validation Results](#unique_123) [page ] 186 | General Ledger Accountant | View Balance Validation Results (F6387) | You viewed the balance validation results. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Manage G/L Account Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a new G/L account by copying an existing one from the chart of accounts view or the company code view. You can also use the Mass Change function to modify one or more attributes of multiple G/L accounts.

|  |
| --- |
| Note Previously, you could only edit/mass change master data up to a maximum of 50 G/L accounts. This limit is now extended up to 5000 G/L accounts at a time. |

|  |
| --- |
| Note The Manage G/L Account Master Data (F0731A) app can be executed by either the Configuration Expert - Business Process Configuration role or the General Ledger Accountant role (the General Ledger Accountant role must be set up by the administrator as an expert GL_ACCOUNTANT to perform configuration activities). You can only make changes in the Q system or the customizing system in a three-system landscape (3SL). In the P system, you can only display content. |

|  |
| --- |
| Caution If the configuration activity in the Manage Your Solution (F1241) app is only accessible in Display mode, you can still use the Manage G/L Account Master Data (F0731A) app with the General Ledger Accountant role to maintain master data. |

|  |
| --- |
| Note When GL accounts are created via content activation, such as initial implementation, country/region activation, or scope item activation, by default, they're set with implementation status I (In process). If you copy a G/L account, the implementation status is inherited from the source accounts (for example, if the source account is set as P (Productive), the copy is also set to P (Productive)). You can change the implementation status to N (Not used), or P (Productive). For more information on Implementation Status (including which accounts are available in your quality and development systems), see [this page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/35e42fcad6e644c5b51f563da6dc190d.html?locale=en-US&version=LATEST) on the SAP Help Portal. |

Procedure

You can access the Manage G/L Account Master Data feature via one of the following procedures:

- Manage G/L Account Master Data Configuration Activity - Procedure
- Manage G/L Account Master Data (F0731A) Fiori App - Procedure

Manage G/L Account Master Data Configuration Activity - Procedure

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
2. For the Manage G/L Account Master Data row, choose Configure.
3. Continue with the procedure in the Procedure Table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Manage G/L Account Master Data.
3. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
4. Continue with the procedure in the Procedure Table below.

Manage G/L Account Master Data (F0731A) Fiori App - Procedure

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage G/L Account Master Data (F0731A). (You can use the search function to find this if there isn't a tile shown.)
3. Continue with the procedure in the Procedure Table below.

Procedure Table

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Search for Your Account | Make the following entries and choose Go:Chart of Accounts: YCOAG/L Account: For example, 12562000View: Chart of Accounts View | The system displays a list of matching G/L accounts. |  |
| 2 | Choose G/L Account | For the G/L account you want to select, choose Details (>). | The G/L Account Master Data view is displayed. |  |
| 3 | Copy Account | Choose Copy. | The Copy of <G/L account number> screen displays. |  |
| 4 | Create Account | Make the following entries and choose OK:Account Number: For example, 12562003Description in Maintenance Language (EN): Deferred Income Oth.Company Code Assignment: For example, 3310 | Data entered on the screen G/L Account Master Data displays. |  |
| 5 | Save | Make the following entries:Group Account Number: <account number>Note This field is visible only when Consolidation is in the scope.Choose Save. | A success message is displayed. The account is shown in display mode. |  |
| 6 | Edit | Choose Edit. |  |  |
| 7 | Change Account to Productive Status | Make the following entry and choose Save:Implement Status: <implementation status>, for example, P (Productive Use)Note For more information on Implementation Status, see the link in the note above. | Note The G/L account is blocked for posting until transported changes arrive in the P system. |  |
| 8 | Back to the Entry View | Choose Back twice. | The Manage G/L Account Master Data screen displays. |  |
| 9 | Multiple Copies | Select the checkbox for the G/L Account (for example, 12562000) and choose Copy (above the table). | The Copies of <account> view is displayed. |  |
| 10 | Multiple Copies | Make the following entries and choose Copy:Account Number: for example, 12562090Description in Maintenance Language (EN): for example, Deferred Income Oth.Company Code Assignment: 3310 | An Information dialog box is displayed. When the job is complete, the system displays a notification. You can view the access logs. Additionally, you can check the copy status using View Logs. |  |
| 11 | Mass Copy | On the Manage G/L Account Master Data screen, make the following entries and choose Go:Chart of Accounts: YCOAG/L Account: For example, 12562000View: Company Code ViewCompany Code: 3310 |  |  |
| 12 | Mass Copy | Select the G/L Account and choose Copy to Company Code.Enter another country/region's Company Code and choose Copy. | The Copy Accounts to Company Code screen displays.An Information box displays. |  |
| 13 | View Application Logs | Choose View Logs to see the Applications Logs. When you're done viewing the logs, choose Back. |  |  |
| 14 | Search Multiple G/L Accounts | In the G/L Account field, make the following entries, and then choose Go:G/L Account: For example, 1256*Chart of Accounts: YCOAAfterwards, select the relevant G/L Accounts. | The search result of multiple G/L accounts can be seen in the field G/L Account. |  |
| 15 | Select View for Chart of Account | From the View dropdown list, select Chart of Accounts View. | The selected view displays. |  |
| 16 | Select Multiple G/L Accounts | Choose Go and select multiple G/L Accounts to change. | Multiple G/L Accounts are selected on the screen. |  |
| 17 | Start Mass Change | Choose Mass Change > Description Only . | The Mass Change in Chart of Accounts View - Description view is displayed. |  |
| 18 | Make Mass Change | In the Replace column, enter the short and long text to be replaced. In the By column, enter the new descriptions and choose Apply. You can also change the descriptions directly in the Items table. | Old values are updated with new descriptions for all displayed G/L accounts. |  |
| 19 | Save the Changes | Choose Save. Go back to the search screen. | The system confirms that G/L accounts are changed. |  |
| 20 | Select View for Company Code | From the View dropdown menu, choose the entry Company Code View.Make the following entries and choose Go:Company Code: 3310 |  |  |
| 21 | Open Settings for Mass Change | Choose Settings. | The View Settings view is displayed. |  |
| 22 | Change Settings for Mass Change | Select one or multiple fields from the Settings list (for example: Sort Key) and choose OK. | The screen is refreshed and the selected fields display. For example: Sort Key is visible. |  |
| 23 | Select Multiple G/L Accounts | Choose Go and select multiple G/L Accounts to change. | Multiple G/L accounts are selected on the screen. |  |
| 24 | Start Mass Change | Choose Mass Change and select Other Attributes from the dropdown list. | The Mass Change in Company Code View screen is displayed. |  |
| 25 | Make Mass Change | In the Replace column, enter the old value to be replaced. In the By column, enter a new value (for example, 012 for Sort Key) and choose Apply. | The old values are replaced by new values for all displayed G/L accounts. |  |
| 26 | Save the Changes | Choose Save. | The system confirms that <X> G/L accounts are changed. |  |

### Define Financial Statement Versions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage the financial statement version.

|  |
| --- |
| Note The P&L section for some Financial Statement Versions is maintained for functional areas. In this case, you cannot assign accounts in the P&L, only for balance sheet accounts for Asset and Liabilities. |

|  |
| --- |
| Note If you log on to the Q system as a General Ledger Accountant, you can use Manage Financial Statement Versions (OB58) to execute changes in financial statement version data. If you use that app, execute the steps in the table below starting with step 3. In the P system, you can only display financial statement version data. |

|  |
| --- |
| Caution If Q2P is turned off, the configuration step is still available in the Manage Your Solution (F1241) app, but stays in Display mode. |

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
| 1 | Select Financial Statement Version | Select the following financial statement version and choose Copy As.Financial Statement Version Name: 3310 | The Change View "Financial Statement Versions": Overview view is displayed. |  |
| 2 | Copy Financial Statement Version | Make the following entries and choose Copy:FS Version: for example, AE99Name: for example, Financial Statement Version AE99Chart of Accounts: YCOASave your entries. | The template financial statement version is copied. |  |
| 3 | Select Financial Statement Version | Select the following financial statement version and choose the Financial Statement Items button.Financial Statement Version Name: for example, AE99 | The Change Financial Statement Version view displays. |  |
| 4 | Delete Accounts | Expand to the item that needs to be maintained, select the account and choose the Delete button. | The account is deleted from the Financial Statement. |  |
| 5 | Save | Save your entries. | The Financial Statement Version: Save & Activate dialog box is displayed. |  |
| 6 | Replicate FSV Hierarchy | Choose Activate. | The replication of the FSV hierarchy starts. |  |
| 7 | Replicate FSV Hierarchy | Choose Continue. | The FSV hierarchy is replicated. |  |
| 8 | Replicate FSV Hierarchy | Choose Continue. | Data is saved. |  |
| 9 | Assign Accounts | Select the item where the account should be added and choose the Assign Accounts button.The account can't be in multiple items. | The Change Accounts entry view displays |  |
| 10 | Enter Account | Make the following entries and choose Continue.The account can't be in multiple rows.From Acct : <your account>To Acct : <your account>D: SelectedC: Selected | The account is assigned to the Financial Statement. |  |
| 11 | Save | Save your entries. | The Financial Statement Version: Save & Activate dialog box is displayed. |  |
| 12 | Replicate FSV Hierarchy | Choose Activate. | The replication of the FSV hierarchy starts. |  |
| 13 | Replicate FSV Hierarchy | Choose Continue. | The FSV hierarchy is replicated. |  |
| 14 | Replicate FSV Hierarchy | Choose Continue. | Data is saved. |  |

### Manage Chart of Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the general ledger accounts for a chart of accounts in either hierarchical or flat list form.

|  |
| --- |
| Note If you're logged on as a General Ledger Accountant in the Q system, you can perform the steps in the table below by using the Manage Chart of Accounts (F0763A) app. When you launch the app, execute the steps in the table below starting with step 3. You must use the Configuration version of the app. If you're logged on to the P system, you can launch the Manage Chart of Accounts (F0763A) app, but you can only display content and can't make changes. |

|  |
| --- |
| Caution If Q2P is turned off, the SSCUI is still available in the Manage Your Solution (F1241) app, but stays in Display mode. |

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
2. For the Manage Chart of Accounts row, choose Configure.
3. Continue with the procedure in the table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Manage Chart of Accounts.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Chart of Accounts | Choose the Chart of Accounts tab. |  |  |
| 2 | Select Chart of Accounts | For the chart of accounts to display (for example YCOA), choose Details (>). | The list of G/L accounts in the selected chart of account displays. |  |
| 3 | Manage Chart of Accounts in Company Code View | Choose Company Code View. |  |  |
| 4 | Enter Company Code | Make the following entries and press Enter:Company Code: 3310 | The system displays a list of G/L accounts that are available in the selected company code. |  |

### Manage Operating Chart of Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage the operating chart of accounts. You have two options:

- Add an individual account: Use the procedure below.
- Add multiple accounts using Expert Worklist functionality: See the [Add Multiple Accounts Using Expert Worklist](#unique_41) [page ] 44 preliminary step

Procedure

You have two choices to access Manage Operating Chart of Accounts:

- Manage Operating Chart of Accounts - Configuration Activity
- Manage Operating Chart of Accounts (F0763B) - Procedure

Manage Operating Chart of Accounts - Configuration Activity

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: General Ledger

1. For the row with Item Name of Chart of Accounts, choose Details (>).
2. For the Manage Operating Chart of Accounts row, choose Configure.
3. Perform steps 3 to 6 in the Manage Operating Chart of Accounts (F0763B) - Procedure table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Manage Operating Chart of Accounts.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Perform steps 3 to 6 in the Manage Operating Chart of Accounts (F0763B) - Procedure table.

Manage Operating Chart of Accounts (F0763B) - Procedure

| Test Step Number | Test Step Name | Instructions | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Operating Chart of Accounts (F0763B). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Chart of Accounts: YCOA (Standard Chart of Accounts)Financial Statement Version: <financial statement version> | The system displays the general ledger accounts in the Hierarchy View pane. You can view account information in the table. You can also click the account number link to perform additional actions. |  |
| 4 | Copy | Expand the hierarchy to find an account you want to copy (for example, a petty cash account). Select the row for the account and choose Copy Account. | A Copy G/L Account dialog box is displayed. |  |
| 5 | Enter Details | Make the following entries:Target G/L Account area:Account: <target account number>Short Text: <short text description>Account Long Text: <long text description>In the Company Code Assignment area, select the company codes to which you want to assign the copied G/L account and choose Copy Account. | The system displays a dialog box with the message No errors found. Job to create G/L accounts started. See Log. |  |
| 6 | Close Message Box | Choose OK. |  |  |

### Manage Operating G/L Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an operating G/L account by copying an existing one from the Chart of Accounts view. You can also use the Mass Change function to modify one or more attributes of multiple operating G/L accounts.

|  |
| --- |
| Note Previously, you could only edit or mass change master data up to a maximum of 50 G/L accounts. This limit is now extended up to 200 G/L accounts. |

|  |
| --- |
| Note The Manage Operating G/L Accounts (F0731B) app can be run by either the Configuration Expert - Business Process Configuration role or the General Ledger Accountant role (the General Ledger Accountant role must be set up by the administrator as an expert GL_ACCOUNTANT to perform configuration activities). You can only make changes in the Q system or the customizing system in a three-system landscape (3SL). In the P system, you can only display content. |

|  |
| --- |
| Caution If the configuration activity in the Manage Your Solution (F1241) app is only accessible in Display mode, you can still use the Manage Operating G/L Accounts (F0731B) app with the General Ledger Accountant role to maintain master data. |

|  |
| --- |
| Note When GL accounts are created via content activation, such as initial implementation, country/region activation, or scope item activation, by default, they're set with implementation status I (In process). If you copy a G/L account, the implementation status is inherited from the source accounts (for example, if the source account is set as P (Productive), the copy is also set to P (Productive)). You can change the implementation status to N (Not used), or P (Productive). For more information on Implementation Status (including which accounts are available in your quality and development systems), see [this page](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/35e42fcad6e644c5b51f563da6dc190d.html?locale=en-US&version=LATEST) on the SAP Help Portal. |

Procedure

You can access the Manage G/L Account Master Data feature via one of the following procedures:

- Manage Operating G/L Account Configuration Activity - Procedure
- Manage Operating G/L Accounts Fiori App (F0731B) Fiori App - Procedure

Manage Operating G/L Account Configuration Activity - Procedure

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
2. For the Manage Operating G/L Account row, choose Configure.
3. Continue with the procedure in the Procedure Table below.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Open the Business Process Configuration app. Go to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Manage Operating G/L Account.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the Procedure Table below.

Manage Operating G/L Accounts (F0731B) Fiori App - Procedure

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Operating G/L Accounts (F0731B). (You can use the search function to find this if there isn't a tile shown.)
3. Continue with the procedure in the Procedure Table below.

Procedure Table

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Search Multiple Operating G/L Accounts | Make the following entries and choose Go:Operating Chart of Accounts: YCOAG/L Account: For example, 1256*View: Chart of Accounts View | The matching operating G/L accounts are shown in the list. |  |
| 2 | Copy Account | Select the checkbox for the account and choose Copy Account. | The Copy of <G/L account number> view is displayed. |  |
| 3 | Copy Account | Make the following entries and choose Copy Account:Account Number: For example, 12562003Short Text and long text: Deferred Income Oth.Company Code Assignment: For example, 3310 | The system displays a Success dialog box. |  |
| 4 | Copy | Choose Close. | The Copy of <G/L account number> view is closed. The Manage Operating G/L Account view is displayed. |  |
| 5 | View Application Logs | Choose View Logs to see the Applications Logs. When you're done viewing the logs, choose Back. |  |  |
| 6 | Select Account | Search for the account you just created.Select the checkbox for the account and choose Details (>). | An information pane opens on the right. |  |
| 7 | Edit | Choose Edit. |  |  |
| 8 | Change Account to Productive Status | Make the following entry and choose Save:Impl. Status in Chart of Accts: <implementation status>, for example, P (Productive Use)Note For more information on Implementation Status, see the link in the note above. | Note The G/L account is blocked for posting until transported changes arrive in the P system. |  |
| 9 | Back | Choose Back. |  |  |
| 10 | Select Multiple G/L Accounts for Mass Change | Choose Go.Select multiple Operating G/L Accounts to change. |  |  |
| 11 | Start Mass Change | Choose Mass Change. | The Mass Change in Chart of Accounts View is displayed. |  |
| 12 | Make Mass Change | In the Replace column, enter the values to be replaced. In the By column, enter the new values and choose Apply. | Old values are updated with new values for attributes to be changed in the G/L accounts. |  |
| 13 | Save the Changes | Choose Save. Go back to the search screen. | The system confirms that G/L accounts are changed. |  |
| 14 | Copy to Company Code | Navigate into one operating G/L account and go to the Company Code Assignment section.Select a company code as the source and choose the Copy to Company Code button. | The Copy from <XX> to Company Codes view is displayed. |  |
| 15 | Navigate to Company Code Specific Settings | In the details of one operating G/L account, in the Company Code Assignment section, for one company code, choose Details (>). | Company code specific settings of the operating G/L account are displayed. |  |
| 16 | Select View for Company Code | Choose the Chart of Accounts View to Company Code View tab. |  |  |
| 17 | Select View for Company Code | Make the following entries and choose Go:Company Code: 3310 |  |  |
| 18 | Select Multiple G/L Accounts in Company Code for Mass Change | For the selected company code, select multiple G/L Accounts to change. |  |  |
| 19 | Start Mass Change | Choose Mass Change. | The Mass Change in Company Code View is displayed. |  |
| 20 | Make Mass Change | In the Replace column, enter the old value to be replaced. In the By column, enter a new value (for example, 012 for Sort Key) and choose Apply. | The old values are replaced by new values for all attributes to be changed in the G/L accounts. |  |
| 21 | Save the Changes | Choose Save. | The system confirms that <X> G/L accounts are changed. |  |

### Manage Alternative Chart of Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage an alternative chart of accounts. This alternative chart of accounts (CoA) can help to fulfill your reporting requirements. The alternative CoA is specific to a country/region, and contains G/L accounts to meet specific legal reporting requirements for that country/region.

|  |
| --- |
| Note Alternative G/L accounts can be created by the Configuration Expert - Business Process Configuration role or the expert General Ledger Accountant role. |

|  |
| --- |
| Caution If this does not apply to your country or region, skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant.Note You can also access this via SAP Fiori launchpad by logging in as a Configuration Expert - Business Process Configuration using Manage Your Solution (F1241), then searching for Manage Alternative Chart of Accounts. You can also access this via SAP Central Business Configuration in the Business Processes Configuration app.. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Alternative Chart of Accounts (F8390). | The Migration: Mass Create dialog box is displayed. |  |
| 3 | Mass Migration | If you want to perform a mass creation migration, enter a value in the Alternative Chart of Accounts field and choose Trigger Migration. Otherwise, choose Cancel.Note For the purposes of this test script, choose Cancel. |  |  |
| 4 | Create Alternative G/L Account | To create an alternative G/L account, choose Create. | The right pane is displayed. A New Object dialog box is displayed. |  |
| 5 | Enter Details | Make the following entries and choose Continue:Chart of Accounts: <chart of accounts>, for example, YIKRAlternative G/L Account: <alternative G/L account> | The right pane is populated with some basic information. |  |
| 6 | Enter Details | Make the following entries and choose Create:Alternative G/L Account Type: <account type>Alternative G/L Implementation Status: <status>, for example, P (Productive Use)Short Text in Maint Language: <short text>, for example, Test AcctLong Text in Maint Language: <long text>, for example, Test AccountOperating G/L Account: <G/L account> | The system displays the Unaccepted Recommendations dialog box. |  |
| 7 | Activate | To activate the assignment of the alternative account to the operative account, choose Activate. |  |  |

### Synchronize G/L Account Master Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

New G/L accounts, financial statement versions (FSV), or changes to G/L account master data are normally transported from your quality system to the production system with the currently open business change project (BCP). However,if you urgently need a new or changed object in your production system and can't wait for that BCP to be released and transported, you can use the Synchronize G/L Account Master Data (OB_GLACC71) app to copy these changes into your production system earlier.

This topic includes procedures for the Q system and the P system.

Procedure - Q System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad for your Q system as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Synchronize G/L Account Master Data (OB_GLACC71). | The G/L Account Synchronization view is displayed. |  |
| 3 | Enter Details | Make the following entries and choose Execute:Process G/L Accounts: SelectedChart of Accounts: YCOAG/L Account: <range of G/L accounts> (optional)Test Run: Selected | You executed a test run of the G/L account synchronization. This is useful to see what changes are transferred to the P system. |  |
| 4 | Update Run | Repeat step 3 but change the following value:Update Run: Selected | The system transfers the data to the P system. |  |

Procedure - P System

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad for your P system as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Synchronize G/L Account Master Data (OB_GLACC71). | The G/L Account Synchronization view is displayed. |  |
| 3 | Enter Details | In the Processing Area section, make the following entries and choose Execute:Process G/L Accounts: SelectedSelect the proper radio button for the task you wish to accomplish (for example, Initial Load or one of the Newly created since options; for the latter options, you need to indicate a date in the field next to the radio button).Processing Mode section:Test Run: Selected | The system displays the Display Logs dialog box. Various messages indicate the accounts and other data that are to be transferred. |  |
| 4 | Upload File | Choose Continue. | The G/L Account Synchronization view shows the details for the account synchronization. |  |
| 5 | Back | Choose Back. |  |  |
| 6 | Update Run | Repeat steps 3 to 5 but change the following value:Update Run: Selected | The system updates the data in the P system.Note If you want to verify that your changes are accepted, use the Manage G/L Account Master Data (F0731A) app. |  |

### G/L Account Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The system records modifications made to G/L master records, such as the time of change, the user's name, and the current and previous field contents. This process step is used to display the changes done to the master data of G/L accounts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the App | Open G/L Account Changes (S_ALR_87012308). | The Display Changes to G/L Accounts view is displayed. |  |
| 3 | Display Changes | Make the following entries in the Further Selections area and choose Execute:Chart of accounts data: YCOAAll G/L Accounts: SelectCompany code data: Select | The system displays the changes for the selected G/L accounts. |  |

### Manage Profit Center Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage the profit center group. You have the choice of creating one, or copying an existing one.

Procedure - Create Profit Center Group

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Profit Center Groups (F0764). | The Search: Profit Center Groups view is displayed. |  |
| 3 | Create New Profit Center Group | In the Result List: Profit Center Group pane, choose the New button. | The Profit Center Group: New view is displayed. |  |
| 4 | Group Details | Make the following entries and choose Continue.Controlling Area: A000To create a Profit Center Group that doesn't exist, make the following entries:Name: <name>, for example, YBH125 | The profit center group is created. |  |
| 5 | Continue | Choose Continue. |  |  |
| 6 | Save | Enter a name for the profit center group, then choose Save. | Your group is saved. |  |

Procedure - Create Profit Center Group by Copy

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the SAP Fiori App | Perform steps 1 and 2 above to access the SAP Fiori app. | The Search: Profit Center Groups view is displayed. |  |
| 2 | Enter Selection Criteria | Using the Search Criteria fields, enter an existing profit center group and choose Go. | The Result List: Profit Center Group pane displays any relevant groups. |  |
| 3 | Copy Group | Select a group, choose the Copy button, then choose Copy. |  |  |
| 4 | Enter Group Details | Perform steps 4 to 5 from the procedure table above. |  |  |

### Manage Profit Centers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage the profit center master data.

Prerequisites

On the Home page, choose User > Settings > Default values . Set CO Area to A000. Choose Save.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant.Note You can also use the Divisional Accountant role. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Profit Centers - New Version (F3516A). |  |  |
| 3 | Search Profit Center | In the Search fields, make the following entries and choose Go:Profit Center: For example, YB900 |  |  |
| 4 | Copy Profit Center | Select the row for the profit center and choose Copy. | The right pane expands to show the data entry area. |  |
| 5 | Enter Profit Center | Make the following entries and choose Create:Profit Center: For example, YB901Profit Center Name: <name>Valid From: For example, <Current date>Valid To: For example, 12/31/9999 | You copied a profit center and changed its data. |  |

### Edit Profit Centers Collective

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you make changes to large quantities of profit center master data without having to change the master data for each single profit center.

Prerequisite

Create at least two new profit centers, for which you can change the master data.

From the SAP Fiori launchpad home page, choose User > Settings > Default Values . Set the CO Area field to A000 and choose Save.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access the App | Open Manage Profit Centers - New Version (F3516A). |  |  |
| 3 | Search Profit Center | In the Search fields, make the following entries and choose Go.Profit Center: For example, YB900 |  |  |
| 4 | Copy Profit Center | Select the row for the profit center and choose Copy. | The right pane expands to show the data entry fields. |  |
| 5 | Enter Profit Center Details | Make the following entries and choose Create:Profit Center: For example, YB902Profit Center Name: <name>Valid From: For example, <Current date>Valid To: For example, 12/31/9999 | The YB902 view is displayed. |  |
| 6 | Create Another Profit Center | Repeat these steps to create another profit center (for example, YB903). |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access the App | Open Edit Profit Centers - Collective (KE55). | The Mass Maintenance Profit Center view is displayed. |  |
| 3 | Choose Profit Center to be Edited | Make the following entries and choose Execute:Controlling Area: For example, A000Profit Center: For example, YB902 to YB903 | The system displays a list of matching profit centers. |  |
| 4 | Add Field to be Changed | Choose the Profit Center Master Data Table tab. |  |  |
| 5 | Add Field to be Changed | Choose the Select fields button. |  |  |
| 6 | Add Field to be Changed | Select Lock indicator and add it to the selection criteria, then choose Continue. | The Lock Indicator column is added to the selection criteria in the upper table. |  |
| 7 | Change Master Data of Profit Centers | Make the following entry in the upper table, select the column, and choose Perform Mass Change:Lock indicator: X | The Lock Indicator indicator is set for the selected profit centers. |  |
| 8 | Save | Save your entries. | The changes are saved. |  |

### Edit Company Code Assignment Profit Centers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you change the company code assignments of a larger number of profit centers without having to change the master data for each single profit center.

Prerequisite

This test step is only applicable if more than one company code is activated in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Edit Company Code Assignment Profit Centers - Old Version (KE56). | The Assignment of Profit Centers to Company Codes - Change view is displayed. |  |
| 3 | Search Profit Center | To display the profit center assignment for a company code, drill down to the profit center to be assigned to the company code.Caution When you test in your Starter or Demo system, don't deselect or remove the company code assignment for the SAP predelivered profit centers that start with YB***.For example, select or deselect the checkbox for assignment of your profit centers to your company code (for example, 3310). Choose Activate. | The company code assignment is changed accordingly. |  |
| 4 | Save | Save your entries. |  |  |

### Where-Used List - Profit Centers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you view information on profit center usage.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Where-Used List - Profit Centers (F3751). |  |  |
| 3 | Enter Data | Make the following entries and choose Go:Profit Center: <profit center>, for example, YB101Valid On: <date>, for example, Today | The system displays object types that use the profit center. |  |
| 4 | Select Object Type | Choose the arrow at the right side of a row for one of the object types (for example, Cost Centers). | The right pane expands, showing profit center details for the selected object type. |  |
| 5 | Manage Profit Centers | In the right pane, choose the hyperlink for the profit center you entered above. From the dialog box, choose Manage Profit Centers (New Version).Note You can also choose Manage Profit Centers (Old Version). If you use this one instead, ignore the next instruction. Instead, on the view that displays, choose the Change Log tab, then refer to the topic mentioned in the note below. | The Manage Profit Centers view displays. |  |
| 6 | More Links | Select the checkbox for the row, then choose Change Log. | The Change Log - Profit Centers view is displayed.Note For more information on the Change Log activity, see the [Change Log - Profit Centers](#unique_59) [page ] 83 topic. |  |

### Change Log - Profit Centers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you view a list of changes for a profit center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Divisional Accountant.Note You can also use the General Ledger Accountant role. |  |  |
| 2 | Access the SAP Fiori App | Open Change Log - Profit Centers (F3810). |  |  |
| 3 | Enter Data | Make the following entries and choose Go:Profit Center: <profit center>, for example, YB101Note You can also use other fields to filter on specific change types, the date of change, or who made the change. | The Items pane shows a list of changes for the selected profit center. |  |

### Manage Journal Entry Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you manage templates for general journal entries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entry Templates (F3803).Note If the app isn't shown in the launchpad, you can either launch it from the Search field, or add it to your launchpad via the App finder. | The Manage Journal Entry Templates view is displayed. A list of available templates is shown. |  |
| 3 | Create Template | Choose Create. | The Create Template dialog box is displayed. |  |
| 4 | Create Template | Make the following entry and choose Create:Apply Template In: for example, Post General Journal EntriesNote To create your own template to post with auto-reverse, choose Post General Journal Entries with Auto-reverse. | The Manage Journal Entry Templates view displays. |  |
| 5 | Enter Details - Step 1 | Make the following entries and choose Step 2:Template ID: for example, BANK_INT_ADJDescription: for example, Bank interest adjustmentAccess Level: for example, User Level (30) | The Journal Entry Header: Select Fields view is displayed. |  |
| 6 | Enter Details - Step 2 | Select the following fields (as either Mandatory or Read Only) and choose Step 3:Header TextIntercompany TransactionLedger GroupNet EntryPosting DateNote Ensure that you select the checkbox to the left of the field name, as well as the Mandatory or Read-Only checkbox as needed. | The Journal Entry Header: Enter Values view is displayed. |  |
| 7 | Enter Details - Step 3 | For the fields you selected in step 3, enter values for the fields, then choose Step 4. | The Journal Entry Line Items: Select Fields view is displayed. |  |
| 8 | Enter Details - Step 4 | Select the following fields (as either Mandatory or Read Only) and choose Step 5:Company CodeG/L AccountTextHouse BankHouse Bank AccountCost CenterProfit Center | The Journal Entry Line Items: Enter Values view is displayed. |  |
| 9 | Enter Details - Step 5 | For the fields you selected in step 4, enter values for the fields, then choose Review. | The Manage Journal Entry Templates view is displayed. |  |
| 10 | Save Template | Review your entries. When you are done, choose Save. | The General Journal entry template is saved |  |
| 11 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 12 | Select Template | Choose the Select Templates button. | A dialog box is displayed. |  |
| 13 | Template Use | Select the template to use for posting (such as Bank interest adjustment). | The general journal entry is posted using the selected template. |  |

### Post General Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive G/L journal entries that must be posted manually in the system.

Prerequisite

A global chart of accounts is assigned to all company codes. If a company code has an assigned country chart of accounts, you can use alternative (local) accounts in journal entries. Unless there's a special note, we always use global accounts in the test scripts. To make sure that you have the correct setting, open the Edit Options for Journal Entries - My Settings (F2130) app and deselect the Use Alternative Acct. checkbox.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries Header Data | In the Header pane, make the following entries:Journal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: <empty> |  |  |
| 4 | Enter the Line Item Data | In the Line Items pane, make the following entries:Line item 1:G/L Account: For example, 63002000Debit: 100Tax Code: <Input Tax Code>Cost Center: 33101101Line item 2:G/L Account: For example, 10010000Credit: <amount>Note To see some of the fields, you may need to choose Details (>) at the left of the row. |  |  |
| 5 | Post | Choose Post. | The journal entry is posted. The system automatically adds the input tax amount. |  |
| 6 | Restart the SAP Fiori App | Go back to the SAP Fiori launchpad.Open Post General Journal Entries (F0718). |  |  |
| 7 | Start Journal Entry Excel Upload | Choose Upload New Entry at the bottom of the screen. | The Upload General Journal Entries (F2548) view displays. |  |
| 8 | Download Template | In Destination, select Local, then choose Download Template.Make the following entries and choose Download:Template Language: EnglishFormat: Spreadsheet (*.xlsx) | The Excel template file is downloaded. |  |
| 9 | Prepare the Template | Make the following entries in the template file for all G/L account journal entries to be posted and save it locally:Header:Company Code: 3310Journal Entry Type: <journal entry type>, for example, SAJournal Entry Date: <current date>Posting Date: <current date>Transaction Currency: For example, AEDLine items - Line 1:Company Code: 3310G/L Account: For example, 63003000Debit: <amount>Tax Code: <Input Tax Code>Cost Center: For example, 33101101Line items - Line 2:Company Code: 3310G/L Account: for example, 10010000Credit: <amount> |  |  |
| 10 | Upload Excel File | Choose the Browse button at top of the screen, select the prepared Excel file, and choose Open. | The Excel file is uploaded and you can see new held journal entries in the worklist.If the uploaded file contains errors, choose Show log to view details. |  |
| 11 | Post | Select the held journal entries and choose Post. | The journal entries are posted. |  |

#### Post with Auto-Reverse

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post general journal entries with automatic reversal. This activity also applies for manual accruals and deferrals posting.

Prerequisite (Optional)

If your country/region or your specific business process requires reverse documents to be posted with a different document type or different number range than the original document type, see the [Define Reverse Document Type (Optional)](#unique_7) [page ] 9 step in the Preliminary Steps section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Select Templates | Choose Select Templates. | The Templates dialog box is displayed. |  |
| 4 | Locate Template | In the search field, search for Post General Journal Entries with Auto-reverse. When you locate the template in the search results, choose the template. | The screen updates with the template. |  |
| 5 | Enter Journal Entries Header Data | In the Header pane, make the following entries:Journal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: <empty>Choose the Auto-Reverse tab.Reversal Reason: <reversal reason>, for example, 05Plnd Reversal Date: <last day of next period> |  |  |
| 6 | Enter Line Item Data | In the Line Items pane, make the following entries:Line item 1:G/L Account: For example, 63002000Debit: 100Tax Code: <Input Tax Code>Cost Center: 33101101Line item 2:G/L Account: For example, 10010000Credit: <amount> |  |  |
| 7 | Post | Choose Post. | The journal entry is posted. |  |
| 8 | Access the SAP Fiori App | Go back to the SAP Fiori launchpad.Open Schedule General Ledger Jobs (F1927). | The Application Jobs view is displayed. |  |
| 9 | Reversal Reason | Choose Create.Make the following entries and choose Step 2:Job Template: Post General Journal Entries with Auto-reverseJob Name: Post General Journal Entries with Auto-reverseMake the following entries and choose Step 3:Start Immediately: SelectedMake the following entries and choose Schedule:Company Code: 3310Plnd Reversal Date: date of reversalNote The Inverse Posting checkbox is deselected by default. This means that the exchange rate for the reversal document currency is based on the original document's posting date. If you select the checkbox, the exchange rate is based on the Planned Reversal Date job.Note To do a productive run, deselect the Test run checkbox. | The job is scheduled. |  |
| 10 | Access the SAP Fiori App | Go back to the SAP Fiori launchpad.Open Manage Journal Entries (F0717A). |  |  |
| 11 | Adapt Filters | Choose the Adapt Filters button. | The Adapt Filters dialog box is displayed. |  |
| 12 | Adapt Filters | Select Reversal Reason and choose OK. |  |  |
| 13 | Adapt Filters | Choose Go. |  |  |
| 14 | Adapt Filters | In the Journal Entries pane, choose Settings. | The View Settings dialog box is displayed. |  |
| 15 | Adapt Filters | Select Reversal Reason and choose OK. | The journal entries with Reversal Reason are displayed in the Journal Entries list. |  |
| 16 | Display Journal Entry | Select your journal entry and choose Details. | The Journal Entry - Entry View screen displays the document details. |  |
| 17 | Related Documents | Choose the Related Documents tab. | A reversal document should be displayed in the Items pane. |  |

### Upload General Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive G/L account documents that must be posted manually in the SAP system. When posting to the balance sheet accounts only, you only need to make an entry in the Segment field. If the field is left blank, segment 1000_C is defaulted and must be reconciled.

The app allows for multiple G/L account documents to be uploaded using a single upload file.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Upload General Journal Entries (F2548). |  |  |
| 3 | Download Template | Choose Download Template. In the Template Download dialog box, select the language and format Excel Workbook and then choose Download. | The Template Download dialog box is displayed. |  |
| 4 | Download Template | Make the following entries and choose Download:Template Language: <template language>Format: Spreadsheet (*.xlsx) | The spreadsheet template file is downloaded. |  |
| 5 | Prepare the Template | Make following entries in the template file for all G/L account documents to be posted and save it locally:Note If you want to use Upload General Entries for Post with Auto-reverse, manually add the STODT and STGRD fields at the end of the header column. STODT is Reverse Date, and STGRD is Reverse Reason 05.HeaderCompany Code: 3310Journal Entry Type: <Journal Entry Type>, for example, SAJournal Entry Date: <current date>Posting Date: <current date>Transaction Currency: <currency>, for example AEDLine items - Line 1:Company Code: 3310G/L Account: for example, 63002000Debit: <amount>Tax Code: <Input Tax Code>Cost Center: For example, 33101101Line items - Line 2:Company Code: 3310G/L Account: for example, 10010000Credit: <amount> |  |  |
| 6 | Upload Excel File | Choose the Browse button at the top of the screen and select the prepared Excel file, then choose Open. | The Excel file is uploaded and you can see data entered in the app. |  |
| 7 | Post | Choose Post. | The journal entries are posted. |  |

### Verify General Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can enter a journal entry to be checked before final posting.

You can check the status of the documents submitted for verification in various tabs: All, Submitted, Rejected, and Others. For the rejected documents, you can edit and submit again for approval to the processor.

Documents with status Submitted aren't posted yet. Once approved by the processor, the document is posted automatically and can be seen in the Manage Journal Entries (F0717A) app.

Prerequisites

You must activate approval workflows, define responsibility for rules used in workflow steps, and assign users to responsibilities.

Prerequisite 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Workflows for Journal Entry Verification - In General Ledger (F2720). | The Manage Workflow view displays. |  |
| 3 | Choose Workflow Type | In the Workflows field, select General Journal Entry Verification. |  |  |
| 4 | Create Workflow | Choose Create. | The New Workflow view displays. |  |
| 5 | Enter Workflow Details | Make the following entries and choose Save:Header tab:Workflow Name: for example, Journal entry verificationProperties tab:Description: for example, Company code = 3310 Amount >=100 Account Group = FINStart Conditions tab: (add the following preconditions)Company Code: 3310Threshold Amount in Company Code Currency: for example, 100Account Group: FINJournal Entry Type: for example, SASteps tab: (choose Create to add the first sequence step)Step Type: Verify General Journal EntryRecipients tab:Role: Group 1 for Verifying G/L Journal EntriesTo complete the first sequence step, choose Create.To add a second sequence step, choose Create.Step Type: Post General Journal EntryTo complete the second sequence step, choose Create. | You saved the workflow. |  |
| 6 | Activate Rule | Choose Save, then choose Activate. | The workflow journal entry verification is activated.Note You can create and activate multiple approval level workflows for G/L account groups, threshold amounts, and cost centers at the company code level. |  |

Prerequisite 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Manage Teams and Responsibilities For Journal Entry Verification - In General Ledger (F3932). | The Manage Teams and Responsibilities view is displayed. |  |
| 3 | Create Team | Choose Create. | The Team view displays. |  |
| 4 | Enter Team Details | Make the following entries:Team Information tab:Name: for example, General Journal Entry VerifierGlobal ID: <global identifier>Type: FGLVG (FI general journal entry verification)Status: Enabled |  |  |
| 5 | Team Owner | In the Team Owners area, the Business Partner field should already be prepopulated for you. |  |  |
| 6 | Enter Team Details | Choose the Team Members tab. |  |  |
| 7 | Enter Team Details | Choose the Create button (located above the Team Members area). | The Select: Business User dialog box is displayed. |  |
| 8 | Enter Team Details | Make the following entries and choose OK:Business Partner: for example, the local gl_accountant userFunctions: FGJEV_L1 (Group 1 for Verifying G/L journal entries) |  |  |
| 9 | Create Team | At the bottom of the view, choose Create. | The responsibility for the general journal entries approval workflow is defined. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Verify General Journal Entries - For Requester (F2547A). | The Verify General Journal Entries view is displayed. |  |
| 3 | Select Journal Entry | Make the following entry and choose Go:Company Code: 3310 | All company code documents are displayed.Note You can use the dropdown field above the table to filter the view to show documents for each status type. |  |
| 4 | Access the Post General Journal Entries App | Choose the Create button. | The Post General Journal Entries (F0718) view is displayed. |  |
| 5 | Enter Journal Entries Header Data | In the Header pane, make the following entries:Journal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: <empty> |  |  |
| 6 | Enter Line Item Data | In the Line Items pane, make the following entries:Line item 1:G/L Account: for example, 63003000Debit: 100Note You may need to expand the line item to view the following fields.Tax Code: for example, <Input Tax Code>Account Assignment area:Cost Center: for example, 33101101Line item 2G/L Account: for example, 10010000Credit: <amount>Value Date: Today's date |  |  |
| 7 | Submit | Choose Submit. | The journal entry is submitted for verification. A confirmation dialog box confirms the submission. |  |
| 8 | Confirm | Choose OK. | The dialog box is closed. |  |
| 9 | Back | Choose Back. |  |  |
| 10 | Display Submitted Entry | Choose the submitted document. | The document is displayed. |  |
| 11 | Create a Second Document to be Verified | Repeat steps 4 to 10. | The journal entry is submitted for verification. |  |

#### Verify General Journal Entries - with Auto-Reverse

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can enter a journal entry with automatic reversal to be checked before final posting.

You can check the status of the documents submitted for verification in various tabs: All, Submitted, Rejected, and Others. For those rejected, you can edit and submit again for approval to the processor.

Documents with status Submitted aren't posted yet. Once approved by the processor, the document is posted automatically and can be seen in the Manage Journal Entries (F0717A) app.

Prerequisites

You must activate approval workflows and define responsibility for rules used in workflow steps and assign users to responsibilities. For more information, execute the two prerequisites in the [Verify General Journal Entries](#unique_64) [page ] 93 topic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Verify General Journal Entries - For Requester (F2547A). | The Verify General Journal Entries view is displayed. |  |
| 3 | Select Journal Entry | Make the following entry and choose Go:Company Code: 3310 | All company code documents are displayed under different tabs.Note There are four tabs displaying documents in their various states: all, submitted, rejected, and others. |  |
| 4 | Access the Post General Journal Entries App | Choose Create. | The Post General Journal Entries (F0718) view is displayed. |  |
| 5 | Select Templates | Choose Select Templates. | The Templates dialog box is displayed. |  |
| 6 | Select Template | Search for or scroll down to locate the Post General Journal Entries with Auto-reverse template. Select the template. | The dialog box closes. The Post General Journal Entries view displays with the Posting Template heading. |  |
| 7 | Auto-Reverse Reason | In the Auto-Reverse pane, make the following entries:Reversal Reason: <reversal reason>Plnd Reversal Date: <planned date for reversal> |  |  |
| 8 | Enter Journal Entries Header Data | Choose the Header tab.Make the following entries:Journal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: <empty> |  |  |
| 9 | Enter Line Item Data | In the Line Items pane, make the following entries:Line item 1:G/L Account: for example, 63003000Debit: 100Note You may need to expand the line item to see the following fields.Tax Code: <Input Tax Code>Account Assignment area:Cost Center: for example, 33101101Line item 2G/L Account: for example, 10010000Credit: <amount>Value Date: Today's date |  |  |
| 10 | Submit | Choose Submit. | The auto-reversal is submitted. |  |

#### Withdraw Verify General Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can withdraw the general journal entries with Submitted and Approved status. You only can withdraw the entries that you submitted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Verify General Journal Entries - For Requester (F2547A). | The Verify General Journal Entries view is displayed. |  |
| 3 | Select Journal Entry | Make the following entry and choose Go:Company Code: 3310 | All documents for the company code are displayed.Note You can use the dropdown field above the table to filter the view to show documents for each status type. |  |
| 4 | Select and Withdraw | In the Journal Entries table, for the document you want to withdraw, select the empty cell to the left of the row and choose Withdraw. | The system displays a Confirmation dialog box. |  |
| 5 | Confirm Withdrawal | To withdraw your document, choose OK. | The document is withdrawn. The status changes to Withdrawn. |  |

### Approve Verify General Journal Entries (for Processor - Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive G/L account documents that require review before final posting. After checking the documents, you can either approve or reject with a comment/reason. Once a document has been selected and approved, it's removed from the list. If a document is approved, posting of FI document is automatically triggered.

|  |
| --- |
| Note You can enable the approval authorization check with the [Activate Authorization Check for Approval](#unique_9) [page ] 11 configuration step (in the Preliminary Steps section of this document). Once this is activated, the system has the posting authorization check for the processor to approve the document.. |

Prerequisites

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the Administrator role. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Users (F1303). |  |  |
| 3 | Search User | Make the following entry and choose Go:User name: GL_ACCOUNTANT_AE | The system displays a list of matching user names. |  |
| 4 | Choose User | Select the checkbox next to the user name from the search result and choose Edit. | The Business User view is displayed. |  |
| 5 | Add Role to User | In the Assigned Business Roles section, choose Add. | The Add Business Roles view is displayed. |  |
| 6 | Choose Role to be Added | On the Add Business Roles dialog box, search for the local SAP_BR_GL_ACCOUNTANT role, select it and then choose OK.Caution After you complete this section, unassign the SAP_BR_GL_ACCOUNTANT role from the user you chose in this step. | The role is added in the Assigned Business Roles section. |  |
| 7 | Save | Save your entries. |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The My Inbox view is displayed. |  |
| 3 | Approve Documents | Select the document to be approved and choose Approve.On the Submit Decision dialog box, choose Submit. | The document is approved and posted.Note All approved documents are displayed in the My Inbox - All Items (F0862) app as well as in the Verify Journal Entries app. |  |
| 4 | Display Posted Document | Access the Manage Journal Entries (F0717A) app, make the following selections and choose Go:Company Code: 3310Ledger Group: <leave blank>Journal Entry Type (optional): for example, SAJournal Entry: <leave blank>Document Date: (optional): <date>Fiscal Period (optional): <period>Fiscal Year: <year of posting document>Posting Date (optional): <date> | The approved document is listed. |  |

### Forward Verify General Journal Entries (for Processor - Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive G/L account documents that need to be checked before final posting. After checking, you can forward the documents to another processor to approve with a comment. The system checks the new processor posting authorization for the company code. Once a document has been forwarded, it's removed from the list and goes to the new processor's inbox.

Prerequisite

To ensure that you have documents available for the procedure below, execute steps 1 to 8 in the Procedure table of the [Verify General Journal Entries](#unique_64) [page ] 93 topic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The My Inbox view displays. |  |
| 3 | Forward Documents | Select the document to be forwarded and choose Forward. | The Forward dialog box is displayed. |  |
| 4 | Add Recipient | Enter the name of the recipient and choose Search. | The dialog box shows a list of matching names. |  |
| 5 | Select Recipient | Choose the name of the recipient. | The Forward dialog box changes to show the recipient name and a new field. |  |
| 6 | Add Reason | Make the following entries and choose Forward:Forward Note: <reason for forwarding, such as changing a G/L account> | The document is forwarded. |  |

### Reject Verify General Journal Entries (for Processor - Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive G/L account documents that need to be checked before final posting. After checking the documents you can either approve or reject with a comment/reason. Once a document is selected and rejected, it's removed from the list and goes back to the requester.

Prerequisite

To ensure that you have documents available for the procedure below, execute steps 1 to 8 in the Procedure table of the [Verify General Journal Entries](#unique_64) [page ] 93 topic.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The My Inbox view displays. |  |
| 3 | Reject Documents | Select the document to be rejected.Choose Reject and enter the reason for rejection, for example,change G/L 10010000 to 12540000 | The document is rejected. |  |

### Edit a Rejected Verify General Journal Entry (Requester)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The G/L journal entries must be checked before final posting. The journal entry you submitted is rejected. For it to be approved and posted, you must make the changes requested by the approver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Verify General Journal Entries - For Requester (F2547A). | The Verify Journal Entries view is displayed. |  |
| 3 | Select Journal Entry | Make the following entry and choose Go.Company Code: 3310 | The journal entries are listed. |  |
| 4 | Edit Rejected Journal Entry | Find a journal entry with a value of Rejected in the Status column.For the journal entry, choose the History button. Check the comments to see the reason for rejection.Click outside of the dialog box to dismiss it.Click the journal entry number hyperlink in the Journal Entry column.Choose Edit.Change the journal entry based on the comments entered, for example, change G/L account 10010000 to 12540000.Choose Submit. | The changed journal entry is resubmitted for approval. |  |

### Manage Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display, change, or reverse a journal entry. In the following procedure, it’s used to display a journal entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A). |  |  |
| 3 | Select Journal Entry | Make the following entries and choose Go:Company Code: 3310Journal Entry Date: (optional) <date>Posting Date (optional): <date>Fiscal Year: <year of posting document>Fiscal Period: (optional) <period>Journal Entry Type: (optional) For example, SA | Selected journal entries are displayed in the Journal Entries list. |  |
| 4 | Display Journal Entry | In the row for one of the entries, choose > (Details). | The Display Journal Entries view is displayed. |  |
| 5 | Review | Review the journal entries and choose Back. |  |  |
| 6 | Manage Journal Entry | For one of the journal entries, choose Details (>).Choose Edit to edit a journal entry or choose New to create a journal entry. | The right pane displays details for the journal entry. |  |
| 7 | Edit | If you want to edit the journal entry, choose Edit. Since you're only displaying the journal entry, close the right pane. |  |  |

#### Open Correspondence

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create open items correspondence.

Prerequisite

Invoices and payments are posted. The Business Partner (BP) master data (such as email address, and so on) is updated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant . |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A). | The Manage Journal Entries view displays. |  |
| 3 | Select Journal Entry | Make the following entries and choose Go.Company Code: 3310Ledger Group: emptyJournal Entry Type: (optional) For example, SAJournal Entry: <empty>Journal Entry Date: (optional) <date>Fiscal Period: (optional) <period>Fiscal Year: <year of posting document>Posting Date (optional): <date> | Selected journal entries are displayed in the Journal Entries list. |  |
| 4 | Manage Journal Entry | Select the checkbox for a journal entry number and choose Create Correspondence. | The Create Correspondence view displays. |  |
| 5 | Entry View | Make the following entries:Correspondence: SAP09 (Internal Document - Entry View) | Available fields display and are populated automatically. |  |
| 6 | Actions | Use the buttons to:PreviewSend EmailPrint | Correspondence is created according to the selected criteria. |  |
| 7 | Exit | Choose Home to exit. | The SAP Fiori launchpad displays. |  |
| 8 | Ledger View | Repeat steps 1–6 and select:Correspondence: SAP09 (Internal Document - Ledger View)In the Advanced Parameters section, make the following entry:Ledger: <ledger> | Available fields display and are populated automatically. |  |

#### Reverse General Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display, change, or reverse a document. Here, it's used to reverse a document.

Prerequisite (Optional)

If your country/region or your specific business process requires reverse documents to be posted with a different document type or different number range than the original document type, see the [Define Reverse Document Type (Optional)](#unique_7) [page ] 9 step in the Preliminary Steps section.

Prerequisite

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries Header Data | Make the following entries in the Header pane:General Journal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: <empty> |  |  |
| 4 | Enter Line Item Data | In the Line Items pane, make the following entries:G/L Account: For example: 63003000Debit: amountTax Code:Tax Code: <Input Tax Code>Cost Center: For example: 33101101 |  |  |
| 5 | Enter Line Item Data | In the Line Items pane, make the following entries:G/L Account: For example, 10010000Credit: <amount> |  |  |
| 6 | Post | Choose Post. | The journal entries are posted. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A). |  |  |
| 3 | Select Journal Entry | Make the following entries and choose Go.Company Code: 3310Ledger Group: <empty>Journal Entry Type (optional): For example, SAJournal Entry: <journal entry>Document Date (optional): <date>Fiscal Period (optional): <period>Fiscal Year: <year of posting document>Posting Date (optional): <date> |  |  |
| 4 | Select Journal Entry | Select a relevant document and choose Reverse > Reverse Selected . | The Reverse Journal Entries Details dialog box displays. |  |
| 5 | Enter Reversal Data | Make the following entries and choose OK:Reversal Reason: for example, Wrong postingPosting Date: <date after posting date of document to reverse> | The journal entry is reversed. |  |

### Display Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display journal entries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Journal Entries (F7697). |  |  |
| 3 | Select Journal Entry | Make the following entries and choose Go:Company Code: 3310Journal Entry Date: (optional) <date>Posting Date (optional): <date>Fiscal Year: <year of posting document>Fiscal Period: (optional) <period>Journal Entry Type: (optional) For example, SANote Leave other fields empty. | Selected journal entries are displayed in the Journal Entries list. |  |
| 4 | Display Journal Entry | For the journal entry you want to review, choose the Details (>) button at the right of the row. | A right pane opens with details of the journal entry. |  |
| 5 | Review | Review the journal entry. When done, choose the Close (x) button at the top of the right pane. |  |  |

### Display Document Flow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity displays all documents related to a business transaction, starting from a single document. It shows both the operational and accounting document flows originating from that document. The application's goal is to provide a comprehensive view of the business transaction. It does this by displaying all operational and accounting documents, such as sales, delivery logistics, and billing, that precede and follow the starting document. Additionally, journal entries are shown in chronological order and can be filtered by ledgers, fiscal years, and company codes. You can also drill down into the posting details.

This app shows the relationships between various operational documents and lets you view the linked accounting documents. The operational flow lets you hide or show documents by expanding or collapsing categories, such as sales. The accounting flow displays all accounting documents before and after the starting document in chronological order. You can display and filter these documents by ledger, company code, and fiscal year.

You can view the accounting impact of the documents with the Display as T-accounts option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Display Document Flow (F3665). | The Display Document Flow view is displayed. |  |
| 3 | Select the Starting Document | Make the following entries and choose Go:Document Type: for example, All Document TypesDocument Number: for example, <10001010>Note The starting document selection can be restricted by selecting one of the following document types: Sales document, Billing document, Journal entry, or Delivery. If you select a different value in the Document Type field, the label of the second field also changes. Depending on the document type selection, additional fields may also display.Note If you select Purchasing Document in the Document Type field, the Item field is displayed. You can enter a value in this field to search for a flow for a specific PO item only instead of the entire PO. | The Operational and G/L document flows are displayed.Note The documents are split and displayed in two flows: Operational Document flow and G/L Document flow. |  |
| 5 | Display as T-accounts | Select a document from the G/L document flow, select the checkbox and choose Display as T-accounts. | The accounting document is displayed in T-account view |  |

### Display G/L Account Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you report the general ledger account balances.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display G/L Account Balances (F0707A). |  |  |
| 3 | Enter Account Details | Make the following entries and choose Go:Ledger: 0L for leading ledger with local GAAP or 2L Ledger IFRSCompany Code: 3310Account: for example, 10010000 (use the account from prior steps)Fiscal Year of Ledger: <year of posting document>Period From: <from date>Period To: <to date> | The account balances show in the Balances pane.To change the currency used for the balances, select the desired currency from the Currency dropdown. |  |

### Display Line Items in General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display open, cleared, or all line items of G/L accounts in reporting view.

Additionally, the reporting view offers the following functions:

- Specify the ledger from which to display the line items. The line items displayed are combined from the documents in the entry view and the reporting view.
- With the custom selections, you can also make selections using general ledger account assignments (General Ledger Line Items).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Line Items in General Ledger (F2217). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Ledger: 2L for IFRS ledgerCompany Code: 3310G/L Account: for example, an open-item-managed account, for example, 11001010 (use the same account you used in prior steps)Status: <Open Items>Open on Key Date: <Current date> | A list of line items displays. |  |

### Display Line Item Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display and change line items in a general ledger account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Line Item Entry (F2218). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Company Code: 3310G/L Account: <account>, for example, 11001010Item Type: Normal itemsStatus: <open items>Open on Key Date: <current date>Note You can't change accounts, amounts, tax amounts, or tax codes. If you receive an error regarding these document contents after posting the document, you must reverse it. | A list of line items displays. You can select any of the journal entry links to view or further process the line item. |  |

### Manage Recurring Journal Entries

Purpose

This functionality supports the creation of recurring postings. Recurring entries are similar to standing orders with banks for debiting rent, contribution payments, or loan repayments directly. The postings are done by the recurring entry program on the basis of the recurring entry documents.

In the G/L accounting area, you can use recurring entries to post fixed amounts (such as periodic posting of deferrals and accruals).

The following data in a recurring entry document remains unchanged:

- Posting Key
- Account
- Amounts

You only need to enter the data that changes occasionally in a recurring entry document. This document doesn’t result in transaction figures being updated. The recurring entry program uses this document to create a journal entry.

#### Create Recurring Journal Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Recurring Journal Entries (F1598). |  |  |
| 3 | Create Recurring Journal Entry | Choose Create New Recurring Journal Entry. |  |  |
| 4 | Manage Recurring Journal Entries | Make the following entries and press Enter.Note The Document Header Information pane contains the individual data for the document to be posted. The data for a lease installment payment is defined as an example.Document Header InformationJournal Entry Type: SACompany Code: 3310Transaction Currency: AEDConversion Rule for Foreign Currency Amounts: Use Current Exchange RateReference: <reference text> for example, AccrualsFirst Line ItemG/L Account: For example, 63003000Debit/Credit: <amount>Tax Code: <Input Tax Code>Cost Center: For example, 33101101Item Text: For example, Monthly accrualNext Line ItemG/L Account: <G/L account> for example, 21720000Debit/Credit: <amount>Recurrence RuleStart Date: <date of the first run>Recurrence Pattern: For example, MonthlyEvery: For example, 1End: For example, AfterOccurrence(s): For example, 3Tax Items:Note If the section for tax items isn't visible yet, choose Enter. | A recurring document is processed. The document is entered as a recurring entry document, but isn't yet posted to the accounts.The Enter Recurring Entry Add G/L Account Item view is displayed. |  |
| 5 | Save | Save your entries. | A recurring entry is saved. |  |

#### Display Recurring Journal Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Recurring Journal Entries (F1598). |  |  |
|  |  | Make the following entries and choose Go:Company Code: 3310 |  |  |
| 3 | Select Recurring Journal Entry | Select a line for a recurring entry to display and choose Display. | The Display Recurring Journal Entries view is displayed. |  |

#### Edit Recurring Journal Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Recurring Journal Entries (F1598) |  |  |
| 3 | Company Code | Make the following entries and choose Go:Company Code: 3310 |  |  |
| 4 | Select a Recurring Journal Entry | Select the line for the recurring entry to edit and choose Edit. | The Edit Recurring Journal Entry view is displayed. |  |
| 5 | Edit Recurring Journal Entry | Change the value of any field. When you are done, choose Save. | A success message is displayed. |  |

#### Copy Recurring Journal Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Recurring Journal Entries (F1598). |  |  |
| 3 | Company Code | Make the following entries and choose Go:Company Code: For example, 3310 |  |  |
| 4 | Select a Recurring Journal Entry | Select the line for the recurring entry and choose Copy. | The Copy Recurring Journal Entries view is displayed. |  |
| 5 | Copy Recurring Journal Entry | Change the value of any fields and choose Save. | A confirmation message is displayed. A new recurring journal entry is created. |  |

#### Post Recurring Journal Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Recurring Journal Entries (F1598). |  |  |
| 3 | Company Code | Make the following entries and choose Go:Company Code: For example, 3310 |  |  |
| 4 | Select a Recurring Journal Entry | Mark the line of the recurring entry and choose Post. | The Posting Confirmation dialog box displays. |  |
| 5 | Post Recurring Journal Entry | Choose Post. | A posting confirmation is displayed. The posting status of the corresponding recurring journal entry is marked as successful. |  |

#### Delete Recurring Journal Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you delete a recurring journal entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Recurring Journal Entries (F1598) |  |  |
| 3 | Company Code | Make the following entries and choose Go:Company Code: For example, 3310 |  |  |
| 4 | Select a Recurring Journal Entry | Mark the line of the recurring entry to delete and choose Delete. | The Confirmation dialog box displays. |  |
| 5 | Post Recurring Journal Entry | Choose OK. | A deletion confirmation displays. The corresponding recurring journal entry is removed. |  |

### Display Changes of Recurring Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display changes made to a recurring entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Changes of Recurring Entry (FBD4). | The Recurring Document Changes: Initial Screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Continue:Company Code: 3310Document Number: 91XXXXXXXXFrom Change Date: Optional <date of change>Changed by: Optional |  |  |
| 4 | Select Changes | Choose All Changes. | The changes are displayed. |  |

### Audit Journal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run various auditing reports to verify your journal's accuracy.

Prerequisite

Key features for this report:

- Run the Compact Journal report to provide an overview of journal entries that are entered within a given time period.
- Run the Journal report to list all journal entries that are entered within a given time period, and navigate to the Manage Journal Entries (F0717A) app.
- Run the Display Journal Entry Changes report to show logs for changes that are made to journal entries since they're posted.
- Run the Check Multi-referenced Invoices report to list invoices if they're referenced in multiple journal entries.
- Run the Check Gaps in Document Numbers report to display all gaps that occur within a given time period.
- Run the Display Update Terminations report to display all system terminations that occur within a given time period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Audit Journal (F0997). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Company Code: 3310Fiscal Year: <Current fiscal year>Ledger: 0L for leading ledger with local GAAP | The Compact Journal report is displayed.Note You can switch to the Journal report to see the documents per posting date. |  |
| 4 | Display Changes to Journal Entries | Choose Display Journal Entry Changes.Check the report and go back. | The report shows logs for changes that are made to journal entries since they're posted |  |
| 5 | Check Multireferenced Invoices | Choose Check Multi-Referenced Invoices.Check the report and go back. | The report lists all documents in which the same reference was maintained. |  |
| 6 | Check Gaps in Journal Entry Numbering | Choose Check Gaps in Journal Entry Numbering.Check the report and go back. | The report displays all gaps that occur within a given time period |  |
| 7 | Display Updated Terminations | Choose Check Gaps in Journal Entry Numbering.On the next page, choose Display Update Terminations.Make the following entries:Creation Date:Creation dateCheck the report and go back. | The report displays all system terminations that occur within a given time period.Note The Display Update Terminations button is enabled only if there are termination errors. |  |

### Journal Entry Analyzer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The journal entry analyzer shows the total amounts of selected journal entries on G/L accounts. You can group these fields from the header or line item segment, such as company code, fiscal year, posting date, business area, functional area, or profit center.

Two apps are available: the original app Journal Entry Analyzer (F0956A) and the new app Journal Entry Analyzer - New Version (F0956B). Procedures for both apps are below.

Prerequisite

Journal entries are posted to the G/L accounts and the posting period selected in the report.

Procedure - Original App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Journal Entry Analyzer (F0956A). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Ledger: 0L for leading ledger or 2L for IFRSCompany Code: 3310Key Date: <key date>Ledger Fiscal Year: <Current year>Fiscal Period: for example, <current period> | In the Data Analysis pane, the system displays cumulated amounts and quantity of selected journal entries grouped by company code, G/L account, and posting date. The amounts are listed in different currencies. |  |
| 4 | Drilldown | Choose Drilldown > Add Drilldown . | A dialog box is displayed. |  |
| 5 | Select Fields | Select a specific dimension from the Available Fields list (for example, Cost Center), and choose OK. | The list is refreshed and the new field is shown in the Data Analysis pane. |  |

Procedure - New App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Journal Entry Analyzer - New Version (F0956B). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Ledger: 0L for leading ledger or 2L for IFRSCompany Code: 3310 (you can select multiple company codes if needed)Posting Date: <posting date>Key Date: <key date>Fiscal Year of Ledger: <Current year>Fiscal Period: for example, <current period> | The system displays the list of accounts, names, and amounts grouped by company code and G/L account. |  |
| 4 | Filter | In the right panel, choose Filters. |  |  |
| 5 | Filter | In the right panel, choose Add. | The Select Dimension dialog box is displayed. |  |
| 6 | Filter | Select one or more dimensions from the list, then choose Select. |  |  |
| 7 | Filter | For the selected filters, enter a value to filter the list of accounts, then press Enter. | The list of accounts is filtered. |  |
| 8 | Layout | In the right panel, choose Layout. |  |  |
| 9 | Layout | Select one or more checkboxes for Measures to add the measure value to the Columns pane.In the Dimensions pane, choose the Rows or Columns button for a Dimension to add it to the Rows or Columns pane. | As you select measures or dimensions, the accounts list is updated with the select parameters. |  |
| 10 | Chart | In the right panel, choose Chart Settings.Note Some charts have specific requirements for displaying data. For example, in Pie and Donut charts, cell values must either be all positive or all negative. |  |  |
| 11 | Chart | Choose Table and Chart. | The left display area changes to include a chart alongside the table. |  |
| 12 | Chart | You can modify the chart display by changing the Chart Type, Series Axis, and so on.Note To display a chart with no table, choose Chart. You can also change the display of the chart. |  |  |
| 13 | Formatting | In the right panel, choose Formatting. |  |  |
| 14 | Formatting | You can choose the formatting template (for example, Financials, Report, or Basic), shade alternate rows, wrap text, change number format and so on. | The data in the left pane changes as you update formatting settings. |  |
| 15 | Context Information | In the right panel, choose Context Information. | The system displays contextual and technical information for the data. |  |
| 16 | Export | In the right panel, choose Export. |  |  |
| 17 |  | You can export to Excel or PDF. Choosing either button displays a dialog box where you can change export settings. Once you make your choices, choose Export. | The data is exported in the chosen format. |  |

### Clear G/L Accounts - Manual Clearing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The transaction is used to post with clearing for open items.

Prerequisites

You must post a credit and debit position to the account that you want to clear. For example, use open-item-managed account 15200000 and post:

- Debit 61100000 (Payroll Exp. Salaries) with cost center 33101101 to Credit 15200000 (Salary and Wages Advances)

|  |
| --- |
| Caution Both postings must not contain a specific ledger group. See Post General Journal Entries (F0718) or a similar step. |

|  |
| --- |
| Note The amounts for both postings should be the same, so that a clearing is possible. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori Launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries | Make the following entries:HeaderJournal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: Must be empty!Line 1G/L Account: For example, 61100000Currency: AEDDebit: <amount>, for example, 100Cost Center: 33101101Line 2G/L Account: for example, 15200000Credit: <amount>, for example 100 |  |  |
| 4 | Post | Choose Post. | The journal entries are posted. |  |

Procedure

Make sure there's a posting to an open-item-managed account.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the Fiori App | Open Clear G/L Accounts - Manual Clearing (F1579). |  |  |
| 3 | Enter Selection Details | Make the following entries and choose Go:Clear G/L Accounts: Without Ledger GroupsCompany Code: 3310G/L Account: For example, 15200000Posted by: For example, today's date | The selected G/L account displays. |  |
| 4 | Account Selection | Select the account to be cleared. | The Clear G/L Accounts - Manual Clearing (F1579) view is displayed. |  |
| 5 | Enter Posting Details | Choose the Post to G/L Accounts tab.Make the following entries:G/L Account: For example, 10010000Credit Amount: For example, 100 |  |  |
| 6 | Process Open Items | Choose the Open Items tab.Ensure that the relevant open item is activated.In the Processing Status section, the Amount entered and Assigned must match, and the Not assigned amount must be zero. | Items net to zero so that the document can be posted with clearing. |  |
| 7 | Save | Choose Post. | A new document is posted and the open item selected in the account is cleared. |  |

### Clear G/L Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The transaction is used to manually clear open items. If the balance of the items to be cleared isn't zero, you can create a residual item for overpayments/underpayments.

Prerequisites

You must post a Credit and Debit position to the account you want to clear. For example, use open item-managed account 15200000 and post:

a) Debit 61100000 (Payroll Exp Salaries) with cost center 33101101 to Credit 15200000 (Salary and Wages Advances) and

b) Debit 15200000 (Salary and Wages Advances) to Credit 10010000 (Petty Cash)

|  |
| --- |
| Caution Both postings must not contain a specific ledger group. See Post General Journal Entries (F0718) or a similar step. |

|  |
| --- |
| Note The amounts for both postings should be the same, so that a clearing is possible. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries | Make the following entries:HeaderJournal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transactions Currency: AEDLedger Group: Must be empty!Line 1G/L Account: 61100000Debit: <amount>, for example, 100Cost Center: 33101101Line 2G/L Account: for example, 15200000Credit: <amount>, for example, 100 |  |  |
| 4 | Post |  | The journal entries are posted. |  |
| 5 | Enter Second Document | Repeat Steps 3–4 for debit account 15200000 and credit account 10010000 | The journal entries are posted. |  |

Procedure

Make sure that there's a posting to an open-item-managed account.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear G/L Accounts - Manual Clearing (F1579). |  |  |
| 3 | Account Information | Enter the G/L account to clear and choose the Go button.G/L Account: For example, 15200000Company Code: 3310 |  |  |
| 4 | Clear Account | To clear an account, in the Accounts (x) section, choose the Clear (>) button for the account. |  |  |
| 5 | Select Open Items | In the Header section, enter the Document Currency AED. In the Open Items section, select items to be cleared by choosing the Clear button. | In the Items to Be Cleared section, the selected items are displayed. |  |
| 6 | Save | Choose Post. | The open items selected in the account are cleared. Make a note of the cleared document number for later use in resetting the cleared item: ______ |  |

### Reset Cleared Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reset a document that was mistakenly cleared.

|  |
| --- |
| Caution Resetting a large number of cleared documents can cause system performance issues. If you have more than 1000 items to process, the system automatically creates a scheduled job using Schedule Jobs to Reset Cleared Items (F9296). For more information, see [Schedule Jobs to Reset Cleared Items (Optional)](#unique_91) [page ] 131. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Reset Cleared Items (F2223). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Clearing Entry: <document number>Company Code: 3310 |  |  |
| 4 | Reset Cleared Item | On the row for the cleared item, choose the > button at the right of the row. | The Clearing Entry view is displayed. |  |
| 5 | Reset | Choose Reset. | The document is reset. |  |

### Schedule Jobs to Reset Cleared Items (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you schedule jobs to reset cleared items. This activity can be run manually, if needed. If you have run Reset Cleared Items (F2223) and have more than 1000 items to clear, this transaction is automatically executed to prevent performance issues.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Schedule Jobs to Reset Cleared Items (F9296). | The Schedule Jobs to Reset Cleared Items view is displayed. |  |
| 3 | Create | Choose Create. | The New Job: Reset Cleared Items view is displayed. |  |
| 4 | Enter Job Details | Make the following entries and choose Step 2:Job Template: Reset Cleared ItemsJob Name: Reset Cleared Items |  |  |
| 5 | Enter Job Details | Make the following entries and choose Step 3:Start Immediately: Selected |  |  |
| 6 | Enter Job Details | Make the following entries and choose Schedule:Clearing entry: <entry number>Company Code: 3310Fiscal Year: <fiscal year>, for example, 2026Note If you are performing a reversal along with the reset, enter additional information into the fields in the Reversal Parameters pane. | The Application Jobs view is displayed. |  |
| 7 |  | To refresh the review, choose the Go button. When the report status is Finished, choose the document button in the Results column for the job you scheduled. | Review the log results. |  |

### Clear Open Items Automatically

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you periodically clear open G/L account items. The open items are posted as a result of normal postings to open-item-managed G/L accounts and reset clearings. If the items have the same assignment and amount, they're cleared based on the G/L account. The clearing is posted on the clearing date entered in the clearing run or on the date of the most recent document if selected.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear Open Items Automatically (F.13) . | The Automatic Clearing view is displayed. |  |
| 3 | Clearing Data | Make the following entries and choose Execute:Company Code: 3310Fiscal Year: <fiscal year>Posting date: for example, from <one day in current month to end of the month>Select one of the following checkboxes:Select SupplierSelect CustomerSelect G/L AccountsClearing date: for example, <last day of current month>Test Run: Deselect | A clearing document is generated for each pair of open items cleared based on account, amount, and assignment. |  |

### Currency Exchange Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you update exchange rates. The exchange rates can be maintained daily or, at least, the end of the month.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Currency Exchange Rates (F3616). |  |  |
| 3 | Add an Exchange Rate Entry | Choose Create. | The right pane expands to show the entry fields. |  |
| 4 | Enter Data | Make the following entries and choose Create:Exchange Rate Type: MFrom Currency: <foreign currency>, for example, USDTo Currency: <group currency>, for example, AEDQuotation: Direct/IndirectExchange Rate : <exchange rate>Valid From: <validity date> | You entered a new exchange rate. |  |

### Import Foreign Exchange Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can import foreign exchange rates directly from a spreadsheet file and transfer the data.

Prerequisite

A spreadsheet program that supports .xlsx format (for example, Microsoft Excel) is installed on your computer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Import Foreign Exchange Rates (F2092). |  |  |
| 3 | Download Template | Choose Download Template and choose OK. | An XLSX file is downloaded. |  |
| 4 | Prepare the Import File | Open the XLSX file, modify it as needed, and save the file for upload. |  |  |
| 5 | Select File to Import | Choose Browse… and select the upload file (in .xlsx format) | Data from the test load file and a statistic of the records are displayed.The Status column displays any error or success symbols. |  |
| 6 | Start Import | Choose Import. | The system displays the message X entries have been imported successfully. |  |

### Repost GR/IR Clearing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This app analyzes goods receipt/invoice receipt (GR/IR) clearing accounts at a specified key date and creates adjustment postings if needed. These adjustments help to accurately show the following business transactions in the balance sheet:

- Goods delivered but not invoiced
- Goods invoiced but not delivered

Prerequisite

Data is created by running the listed steps in either of these scripts:

- Procurement of Direct Materials (J45)
    - Post Goods Receipt for Purchase Order
    - Create Supplier Invoice with PO/GR Relation
- Requisitioning (18J)
    - Confirm Receipt of Goods
    - One of the Create Supplier Invoice steps

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Repost GR/IR Clearing (F.19). | The Analyze GR/IR Clearing Accounts and Display Acquisition Tax view is displayed. |  |
| 3 | Enter Account Selection | Make the following entries and choose Execute:G/L account: For example, 21120000Company Code: 3310Parameters tab:Key Date: <end of period>GR/IR clearing: selectedPostings tab:Create Posting: selectedName of batch input session: <name>Document date: <end of period>Document type: for example SAPosting date: <end of period>Reversal posting date: <beginning of the next period> | A report with line item information is displayed.If a batch input session is created, process it as described in the Process Batch Input Session section. |  |

### Perform Foreign Currency Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The total difference of all the open account items is posted to a balance sheet adjustment account, retaining the original account balance. The gains or losses from exchange rate fluctuations from the valuation are entered as offsetting entries in separate expense and revenue accounts for exchange rate differences. If you perform an update run and enter a session name for the batch input session, you can run the session after it's created.

You have two options for performing the foreign currency valuation: using Perform Foreign Currency Valuation (FAGL_FCV) or using Schedule General Ledger Jobs (F1927).

|  |
| --- |
| Note If Advanced Valuation is activated (the system displays an error message Advanced valuation active; you can no longer use the old report. Message no. FINS_FI_CLS023 is raised) and as long as there is no posting in the P system, you can deactivate this. To deactivate this, use the Activate Advanced Valuation configuration step (available in the Manage Your Solution (F1241) app (for more information on accessing the configuration step, see the [Activate Advanced Valuation](#unique_12) [page ] 12 topic. Now, you can run Perform Foreign Currency Valuation (FAGL_FCV). |

Prerequisites

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Aging SGLOBRCL is listed with Months values 1 (CURRENT) and 2 (NONCURRENT) but descriptions 'Current up to 12 Months' and 'Non-current more than 12 Months'; the Months column and the descriptions do not match.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/test-script-sap-s-4hana-cloud-public-edition-accounting-and-financial-part-02]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J58_S4CLD2608_BPD_EN_AE.docx` — lines 1–3738 of the extracted text · extracted with `mammoth` · 345,315 chars in the whole document
