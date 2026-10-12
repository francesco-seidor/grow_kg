---
id: 03-financial-accounting-and-close/test-script-accounting-and-financial-close-group-ledger-ifrs-1ga-ae-sa
title: "Test Script: Accounting and Financial Close - Group Ledger IFRS (1GA_AE) - SAP S/4HANA Cloud Public Edition (1GA_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for Group Ledger IFRS (1GA_AE, UAE): journal entries, clearing, FX valuation, reports; company code 3310."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/accounting-and-financial-close-us-gaap]
aliases: [1GA_S4CLD2608_BPD_EN_AE]
keywords: [Accounting and Financial Close with a Parallel Group…, group ledger ifrs, parallel accounting, journal entry verification, journal entry posting, open item clearing, reset cleared items, foreign currency valuation, currency adjustments, regroup receivables payables]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GA_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-718
topic: 03-financial-accounting-and-close/accounting-and-financial-close-us-gaap
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Accounting and Financial Close - Group Ledger IFRS (1GA_AE) - SAP S/4HANA Cloud Public Edition (1GA_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GA_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Accounting and Financial Close with a Parallel Group Ledger (US GAAP or IFRS)** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Accounting and Financial Close – Group Ledger IFRS (1GA_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232846986)

[2 Prerequisites 4](#_Toc232846987)

[2.1 System Access 4](#_Toc232846988)

[2.2 Roles 4](#_Toc232846989)

[2.3 Master Data and Organizational Data 5](#_Toc232846990)

[2.4 Business Conditions 6](#_Toc232846991)

[2.5 Preliminary Steps 7](#_Toc232846992)

[2.5.1 Relevant Configuration Steps for Advanced Valuation Processes 7](#_Toc232846993)

[3 Overview Table 8](#_Toc232846994)

[4 Test Procedure 11](#_Toc232846995)

[4.1 Verify General Journal Entries for Requester 11](#_Toc232846996)

[4.2 Approve Verify General Journal Entries (for Processor- Inbox) 15](#_Toc232846997)

[4.3 Reject Verify General Journal Entries (for Processor- Inbox) 16](#_Toc232846998)

[4.4 Edit a Rejected Verify General Journal Entry (Requester) 17](#_Toc232846999)

[4.5 Post General Journal Entries 18](#_Toc232847000)

[4.6 Manage Journal Entries 20](#_Toc232847001)

[4.7 Display G/L Account Balances 21](#_Toc232847002)

[4.8 Display Line Item Entry 22](#_Toc232847003)

[4.9 Display Line Items in General Ledger 23](#_Toc232847004)

[4.10 Audit Journal 24](#_Toc232847005)

[4.11 Journal Entry Analyzer 26](#_Toc232847006)

[4.12 Clear G/L Accounts - Manual Clearing with Ledger Group 27](#_Toc232847007)

[4.13 Clear Open Items Automatically for Ledger Group 29](#_Toc232847008)

[4.14 Reset Cleared Items 32](#_Toc232847009)

[4.15 Schedule Jobs to Reset Cleared Items (Optional) 32](#_Toc232847010)

[4.16 Manage Journal Entries 34](#_Toc232847011)

[4.17 Perform Foreign Currency Valuation 35](#_Toc232847012)

[4.18 Post Currency Adjustments 38](#_Toc232847013)

[4.19 Regroup Receivables/Payables 40](#_Toc232847014)

[4.20 Perform Advanced Foreign Currency Valuation 42](#_Toc232847015)

[4.21 Credit-Risk-Based Impairment 42](#_Toc232847016)

[4.22 Post B/S Reclassification 42](#_Toc232847017)

[4.23 Cash Flow Statement 43](#_Toc232847018)

[4.24 Trial Balance 44](#_Toc232847019)

[4.25 Trial Balance Comparison 45](#_Toc232847020)

[5 Appendix 46](#_Toc232847021)

[5.1 Balance Carryforward Status 46](#_Toc232847022)

## Purpose

Overview

General Ledger Accounting provides a comprehensive overview of external accounting and accounts and supports parallel accounting.

General Ledger Accounting serves as a complete record of all business transactions, providing a centralized, up-to-date reference for the rendering of accounts. Actual individual transactions can be checked at any time in real-time processing by displaying the original documents, line items, and transaction figures at various levels to support parallel accounting. These transactions include:

- Manage Journal Entries
- Post with Clearing for Ledger Group
- Run Automatic Clearing Specific to Ledger Groups
- Trial Balance Comparison
- Financial Statement Ledger Comparison

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/1GA_S4CLD2602_BPD_EN_AE.docx) ). |

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
| General Ledger Accountant for United Arab Emirates | SAP_BR_GL_ACCOUNTANT_AE |  |  |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data and Organizational Data

Default Values

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

The business process is enabled with this organization-specific master data, examples are provided in the next section.

Additional Default Values

You can test the scope item with other SAP Best Practices default values that have the same characteristics.

Check your SAP system to find out which other material master data exists.

Using Your Own Master Data

You can also use customized values for any material or organizational data for which you have created master data. For more information on how to create master data, see the Master Data Procedures documentation.

Use the following master data in the process steps described in this document:

| Master Data | Sample Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Chart of Accounts | YCOA |  |  |
| Controlling Area | A000 |  |  |
| Cost Center | 33101001 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Items | Business Condition |
| --- | --- |
| J58 - Accounting and Financial Close | You must complete the test procedures in the J58 test script. |

### Preliminary Steps

#### Relevant Configuration Steps for Advanced Valuation Processes

Purpose

If you're using parallel accounting and perform closing operations based on IFRS, before you perform advanced valuation processes, you must execute the following prerequisite steps as they are referenced in the Accounting and Financial Close (J58) test script using the master, organizational, or other data from this script:

|  |
| --- |
| Caution Ensure that you use 2L as ledger or IFRS as accounting principle. |

|  |
| --- |
| Note To comply with IFRS18, SAP delivers standard content for an additional rule: SIFR Key Date Foreign Currency Valuation for IFRS. This rule presents exchange gains and losses in different categories (financing, operating, investing) based on the nature of the items from which the gain or loss arises.Use the Manage Operating G/L Accounts (F0731B) app to create dedicated P&L accounts for each category: financing, operating, and investing. Maintain the required account assignments in the Manage Default Account Assignments configuration activity”. For more information, see [3694359](https://me.sap.com/notes/3694359). |

- Relevant Configuration Steps for Advanced Valuation in General Ledger Accounting
- Relevant Configuration Steps for Discounting of Long-Term Assets and Liabilities
- Relevant Configuration Steps for Advanced Foreign Currency Valuation
- Relevant Configuration Steps for Credit-Risk Based Impairment
- Migrate Financial Statement Versions to Global Hierarchies
- Replicate Runtime Hierarchy

## Overview Table

This scope item consists of several process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Verify General Journal Entries for Requester](#unique_9) [page ] 11 | General Ledger Accountant | Verify General Journal Entries - For Requester (F2547A) | The journal entry is checked. |
| [Approve Verify General Journal Entries (for Processor- Inbox)](#unique_10) [page ] 15 | General Ledger Accountant for United Arab Emirates | Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728) and Manage Journal Entries (F0717A) | All documents received for approval are displayed. |
| [Reject Verify General Journal Entries (for Processor- Inbox)](#unique_11) [page ] 16 | General Ledger Accountant for United Arab Emirates | Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728) | All documents checked by the user are displayed. |
| [Edit a Rejected Verify General Journal Entry (Requester)](#unique_12) [page ] 17 | General Ledger Accountant for United Arab Emirates | Verify General Journal Entries - For Requester (F2547A) | All submitted documents are displayed. |
| [Post General Journal Entries](#unique_13) [page ] 18 | General Ledger Accountant | Post General Journal Entries (F0718) | The General Ledger Accountant Journal Entry is posted. The system has automatically added the Input tax amount. |
| [Manage Journal Entries](#unique_14) [page ] 20 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Journal Entry has changed. |
| [Display G/L Account Balances](#unique_15) [page ] 21 | General Ledger Accountant | Display G/L Account Balances (F0707A) | The balances for every period in the year are displayed. |
| [Display Line Item Entry](#unique_16) [page ] 22 | General Ledger Accountant | Display Line Item Entry (F2218) | The G/L Account Line Items- G/L View screen displays. |
| [Display Line Items in General Ledger](#unique_17) [page ] 23 | General Ledger Accountant | Display Line Items in General Ledger (F2217) | A list of all relevant line items is displayed. |
| [Audit Journal](#unique_18) [page ] 24 | General Ledger Accountant | Audit Journal (F0997) | The correctness of the auditing reports is ensured. |
| [Journal Entry Analyzer](#unique_19) [page ] 26 | General Ledger Accountant | Journal Entry Analyzer (F0956) | The summation of amount and quantity of all selected journal entries according to various fields is displayed. Amounts are shown in different currencies (company code currency, document currency, global currency, and so on). |
| [Clear G/L Accounts - Manual Clearing with Ledger Group](#unique_20) [page ] 27 | General Ledger Accountant | Clear G/L Accounts - Manual Clearing (F1579) | The ledger-specific open items selected in the account have been cleared. If a difference is determined, a residual item or a new open item is created. |
| [Clear Open Items Automatically for Ledger Group](#unique_21) [page ] 29 | General Ledger Accountant | Clear Open Items Automatically - For Ledger Group (F13L) | The ledger-specific open items selected in the account have been cleared. |
| [Reset Cleared Items](#unique_22) [page ] 32 | General Ledger Accountant | Reset Cleared Items (F2223) | You reset cleared items. |
| [Schedule Jobs to Reset Cleared Items (Optional)](#unique_23) [page ] 32 | General Ledger Accountant | Schedule Jobs to Reset Cleared Items (F9296) | You scheduled jobs to reset cleared items. |
| [Manage Journal Entries](#unique_24) [page ] 34 | General Ledger Accountant | Manage Journal Entries (F0717A) |  |
| [Perform Foreign Currency Valuation](#unique_25) [page ] 35 | General Ledger Accountant | Perform Foreign Currency Valuation (FAGL_FCV) or Schedule General Ledger Jobs (F1927) | Foreign currency postings are represented with current date. |
| [Post Currency Adjustments](#unique_26) [page ] 38 | General Ledger Accountant | Post Currency Adjustments (F1606) | You posted adjustments to account balances for foreign currencies. |
| [Regroup Receivables/Payables](#unique_27) [page ] 40 | General Ledger Accountant | Regroup Receivables / Payables (FAGLF101) |  |
| [Perform Advanced Foreign Currency Valuation](#unique_28) [page ] 42 |  | Execute the step of the same name in the Accounting and Financial Close (J58) test script. |  |
| [Credit-Risk-Based Impairment](#unique_29) [page ] 42 |  | Execute the step of the same name in the Accounting and Financial Close (J58) test script. |  |
| [Post B/S Reclassification](#unique_30) [page ] 42 |  | Execute the step of the same name in the Accounting and Financial Close (J58) test script. |  |
| [Cash Flow Statement](#unique_31) [page ] 43 | General Ledger Accountant | Cash Flow Statement - Indirect Method (W0054) |  |
| [Trial Balance](#unique_32) [page ] 44 | General Ledger Accountant | Trial Balance (F0996) |  |
| [Trial Balance Comparison](#unique_33) [page ] 45 | General Ledger Accountant | Trial Balance Comparison (W0097) |  |

## Test Procedure

This section describes test procedures for each process step that belongs to this scope item.

### Verify General Journal Entries for Requester

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this task, you enter a journal entry to be checked before final posting. You can check the status of the journal entries submitted for verification in various tabs: All, Submitted, Rejected, and Others. If an entry is rejected, you can edit and resubmit it for approval.

Journal entries with status Submitted aren't posted yet. Once approved, the journal entry is posted automatically. To view the posting, use the SAP Fiori App Manage Journal Entries (F0717A).

Prerequisites

You must activate approval workflows and define responsibility for rules used in workflow steps and assign users to responsibilities.

Prerequisite 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Manage Workflows for Journal Entry Verification - In General Ledger (F2720). | The Manage Workflows view displays. |  |
| 3 | Create Workflow | To the right of the Workflows title, select General Journal Entry Verification from the dropdown.Choose Create. | The New Workflow view displays. |  |
| 4 | Enter Workflow Details | Make the following entries and choose Save:Header tab:Workflow Name: for example, Journal entry verificationProperties tab:Description: for example, Company code = 3310 Amount >=100 Account Group = FINStart Conditions tab: (add the following preconditions)Company code: 3310Threshold amount in company code currency: for example, 100Account group: FINSteps tab: (choose Create to add the first sequence step)Step Type: Verify General Journal EntryChoose Create.Add a second sequence step.Step Type: Post General Journal EntryChoose Create. | You saved the workflow. |  |
| 5 | Activate Workflow | Choose Save, then choose Activate. | The workflow journal entry verification is activated.Note You can create and activate multiple approval level workflows for G/L account groups, threshold amounts, and cost centers at the company code level. |  |

Prerequisite 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Manage Teams and Responsibilities For Journal Entry Verification - In General Ledger (F3932). | The Manage Teams and Responsibilities view displays. |  |
| 3 | Create Team | Choose Create. | The Team view displays. |  |
| 4 | Enter Team Details | Make the following entries:General Information pane:Name: for example, General Journal Entry VerifierGlobal ID: <defaults to the same value as the Name field>Type: FGLVG (FI General Journal Entry Verification Default Team)Status: Enabled |  |  |
| 5 | Enter Team Details | Choose the Team Members tab. |  |  |
| 6 | Enter Team Details | In the Team Members pane, choose Create. | The Select: Business User dialog box is displayed. |  |
| 7 | Enter Team Details | Select the Business Partner/Full Name (such as GL_ACCOUNTANT_AE) and choose OK. |  |  |
| 8 | Enter Team Details | Make the following entries:Functions: FGJEV_L1 (Group 1 for Verifying G/L Journal Entries) |  |  |
| 9 | Create | At the bottom of the view, choose Create. | The responsibility for the general journal entries approval workflow is defined. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Verify General Journal Entries - For Requester (F2547A). |  |  |
| 3 | Select Journal Entry | Make the following entry and choose Go.Company Code: 3310 | All company code journal entries are displayed under different tabs.Note There are four tabs displaying journal entries in their various states: all, submitted, rejected, and others. |  |
| 4 | Access the Post General Journal Entries App | Choose Create. | The Post General Journal Entries (F0718) screen displays. |  |
| 5 | Enter Journal Entries Header Data | In the Header pane, make the following entries:Journal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: <Ledger Group number; for example, 2L for IFRS> |  |  |
| 6 | Enter Line Item Data | Note You may need to expand the line item row to see more fields.In the Line Items pane, make the following entries:G/L Account: for example, 63003000Debit: 100Tax Code: <Input Tax Code> (if required for ledger group; not required for ledger 2L)Account Assignment area:Cost Center: for example, 33101101For the next line item:G/L Account: for example, 10010000Credit: <amount>Value Date: Today's date |  |  |
| 7 | Submit | Choose Submit. | The journal entry is submitted for verification. |  |
| 8 | Create a Second Document to be Verified | Repeat steps 4 to 7. |  |  |

### Approve Verify General Journal Entries (for Processor- Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive journal entries to be checked before final posting. After checking these entries, you can either approve or reject them with a comment or reason. Once a journal entry has been selected and approved, it's removed from your list. If a journal entry is approved, posting of an FI journal entry is automatically triggered.

Prerequisites

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Users (F1303). | The Maintain Business Users (F1303) screen displays. |  |
| 3 | Search User | Make the following entry and choose Go:User name: GL_ACCOUNTANT_AE | The system displays a list of matching user names. |  |
| 4 | Choose User | Select the checkbox for the user name from the search results and choose Edit. | The Business User screen displays. |  |
| 5 | Add Role to User | In the Assigned business roles section, choose Add. | The Add Business Roles screen displays. |  |
| 6 | Choose Role to be Added | On the Add Business Roles screen, search for the SAP_BR_GL_ACCOUNTANT role, select it and then choose OK. | The role is added in the Assigned Business Roles section. |  |
| 7 | Save | Save your entries. |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The My Inbox view displays. |  |
| 3 | Approve Journal Entries | Select the journal entry to be approved and choose Approve.In the Submit Decision dialog box, choose Submit. | The journal entry is approved and posted.Note All approved journal entries are displayed in the Verify General Journal Entries For Processor (Outbox) (F2729) app as well as in the Verify Journal Entries in General Ledger (F2728) app. |  |
| 4 | Home | To return to the SAP Fiori launchpad, choose Home. |  |  |
| 5 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A). |  |  |
| 6 | Display Posted Journal Entry | Make the following selections, and choose Go:Company Code: 3310Ledger Group: <Ledger group number; for example, 2L for IFRS>Journal Entry Type (optional): for example, SAJournal Entry:Document Date: (optional): <date>Period (optional): <period>Fiscal Year: <year of posting document>Posting Date (optional): <date> | The approved journal entry is listed. |  |

### Reject Verify General Journal Entries (for Processor- Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive journal entries to be checked before final posting. After checking these entries, you can either approve or reject them, adding a comment or reason if needed. When a journal entry is rejected, it's removed from your list and sent back to the requester.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The My Inbox view is displayed. |  |
| 3 | Reject Journal Entries | Select the journal entry to be rejected and choose Reject. | The Submit Decision dialog box is displayed. |  |
| 4 | Reject Journal Entries | Make the following entries and choose Submit:Decision Note: <decision note, for example, Change G/L 63003000 to 63000000 | The journal entry is rejected. |  |

### Edit a Rejected Verify General Journal Entry (Requester)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The journal entries must be verified prior to final posting. Your submitted journal entry is rejected. To gain approval and proceed with posting, make the requested changes as specified by the approver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Verify General Journal Entries - For Requester (F2547A). | The Verify Journal Entries view is displayed. |  |
| 3 | Select Journal Entry | Make the following entry and choose Go:Company Code: 3310Ledger Group: <Ledger group number>, for example, 2L for IFRSStatus: Rejected (R)Note If a filter field isn't displayed, choose Adapt Filters and search for field names that are not displayed in the standard view. | The rejected journal entries are listed in the Journal Entries pane. |  |
| 4 | Edit Rejected Journal Entry | Select the journal entry to be edited and choose Edit. |  |  |
| 5 | Edit Rejected Journal Entry | Change the journal entry based on the comments entered (for example, change G/L account 10010000 to 12540000) and choose Submit. | The changed journal entry is resubmitted for approval. |  |

### Post General Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive G/L account documents that must be posted manually in the system.

When posting to the balance sheet accounts only, make an entry in the Segment field. If the field is left blank, segment 1000_C is defaulted and must be reconciled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries Header Data | In the Header pane, make the following entries:Journal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: <Ledger group number> for example, 2L for IFRS | Note Document Type AD can be used to enter accruals/deferrals into the system. |  |
| 4 | Enter Line Item Data | In the Line Items pane, make the following entries:Note You may need to expand Line Item to view more fields.G/L Account: for example, 63002000Debit: 100Cost Center: for example, 33101101 |  |  |
| 5 | Enter Line Item Data | In the Line Items pane, make the following entries:G/L Account: for example, 10010000Credit: <amount>. |  |  |
| 6 | Post | Choose Post. | The General Ledger Accountant account document is posted. The system has automatically added the Input tax amount. |  |

### Manage Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In General Ledger Accounting, you can use this app to display, change, or reverse a document. In this activity, you use it to display a document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A). |  |  |
| 3 | Select Journal Entry | Make the following entries and choose Go:Company Code: 3310Ledger Group: <Ledger group ID, such as 2L for IFRS Ledger Only>Journal Entry Type (optional): for example, SAJournal Entry (optional):Journal Entry Date (optional): <date>Period (optional): <period>Fiscal Year: <year of posting document>Posting Date (optional): <date> | The selected documents are displayed in the Journal Entries list. |  |
| 4 | Select Option | In the Journal Entries list, choose the journal entry number.Caution Don't select the checkbox to the left of the journal entry number. Choose the actual number. | The Journal Entry info box displays. |  |
| 5 | Display Document | Select an option from the displayed list.Caution Don't reverse or reset the posting as it's needed for the following steps. | The Journal Entry view displays the document details. |  |

### Display G/L Account Balances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you view the general ledger account balances.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display G/L Account Balances (F0707A). | The G/L Account Balances view is displayed. |  |
| 3 | Enter Account Details | Make the following entries and choose Go:Ledger: <Ledger ID, such as 2L for IFRS>Company Code: 3310G/L Account: for example, 10010000Fiscal Year of Ledger: <year of posting document>Period From: <from date>Period To: <to date> | The account balances show in the Balances pane. If you want to change the currency used for the balances, select the desired currency from the Currency dropdown. |  |

### Display Line Item Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display line items in a general ledger account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Line Item Entry (F2218). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Company Code: 3310Account: <open item managed account>, for example, 11001010Status: Open itemsOpen on Key Date: <current date>Chart of Accounts: for example, YCOANote You can't change accounts, amounts, tax amounts, or tax codes. If you receive an error regarding document contents after posting, you must reverse it. | A list of line items is displayed. You can choose any of the journal entries links to view or further process the line item. |  |

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

### Audit Journal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you can run various auditing reports to ensure the correctness of your journal. This report has the following key features:

| Feature/Report | Description |
| --- | --- |
| Compact Journal | Provide an overview of journal entries that are entered within a given time period |
| Journal | List all journal entries that are entered within a given time period, and navigate to the Manage Journal Entries (F0717A) app |
| Display Document Changes | Show logs for changes that are made to journal entries since they're posted |
| Check Multireferenced Invoices | List invoices if they're referenced in multiple journal entries |
| Check Gaps in Document Numbers | Display all gaps that occur within a given time period |
| Display Update Terminations | Display all system terminations that occur within a given time period |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Audit Journal (F0997). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Note To select values, select the appropriate checkbox. If the values aren't available, enter the value in the Key field.Company Code: 3310Fiscal Year: <Current fiscal year>Ledger: 2L for IFRS Ledger | The compact journal entries are displayed. |  |
| 4 | Display Changes to Journal Entries | Choose the Display Journal Entry Changes button.Review the report, and go back. | The report shows logs for changes made to journal entries after initial posting. |  |
| 5 | Check Multireferenced Invoices | Choose the Check Multi-Referenced Invoices button.Review the report, and go back. | The report lists invoices when referenced in multiple journal entries. |  |
| 6 | Check Gaps in Journal Entry Numbering | Choose the Check Gaps Journal Entry Numbering button.Review the report, and go back. | The report displays all gaps that occur within a given time period. |  |
| 7 | Display Updated Terminations | Choose Display Updated Terminations.Note The button is only enabled if there are termination errors. |  |  |
| 8 | Display Updated Terminations | Make the following entries and choose Go:Note If the Creation Date field is not visible, choose Adapt Filters.Creation Date: Time periodCheck the report and go back. | The report displays all system terminations that occur within a given time period. |  |

### Journal Entry Analyzer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The journal entry analyzer provides an overview of cumulated amounts of selected journal entries on G/L accounts. This can be grouped by various fields from the header or line item segment, such as company code, fiscal year, posting date, business area, functional area, or profit center.

Prerequisite

Journal entries are posted to the G/L accounts and within the selected posting period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Journal Entry Analyzer (F0956). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Ledger: 2L (for IFRS)Company Code: 3310Key Date: <key date>Fiscal Year of Ledger: <Current year>Fiscal Period: for example, the current period | The system displays cumulated amounts and quantity of selected journal entries grouped by company code, G/L account, and posting date. The amounts are listed in different currencies. |  |
| 4 | Add Field | From the Navigation panel, in the Available Fields area, drag and drop fields into either the row area, column area, or both.For example, Cost Center. | The list is refreshed and the new field is shown. |  |

### Clear G/L Accounts - Manual Clearing with Ledger Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The transaction is used to manually clear ledger-specific open items. If the balance of the items to be cleared isn't 0, you can create a residual item for overpayments/underpayments.

Prerequisites

You must post a Credit and Debit position to a G/L account where ledger-specific clearing is enabled.

For example, use account 24031100, Pension Provision ledgerspec (which has ledger-specific OI management) and post:

1. Debit 61060000 (Payroll Exp. Pension) with cost center 33101101 to Credit 24031100 (Pension Provision ledgerspec.)
2. Debit 24031100 (Pension Provision ledgerspec.) to Credit 12550000 (Unbilled Revenue)

|  |
| --- |
| Caution Both postings must contain a specific ledger group! See Post General Journal Entries or a similar step. Note that the amounts for both postings should be the same, so that a clearing is possible. |

Prerequisites

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries | Make the following entries:HeaderJournal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: 2LLine Items area:Note Expand the lines to show additional fields.Line 1G/L Account: for example, 61060000Debit: <amount>, for example, 100Cost Center: 33101101Line 2G/L Account: for example, 24031100Credit: <amount>, for example 100 |  |  |
| 4 | Post | Choose Post. | The journal entries are posted. |  |
| 5 | Enter Second Document | Repeat Steps 3 and 4 for account 24031100 (debit) with amount, for example, 100 and account 12550000 (credit) with amount, for example, 100, a tax code, and item text, for example, Test. |  |  |

Procedure

Ensure there's a posting to an account that is open item managed.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear G/L Accounts - Manual Clearing (F1579). | The Clear G/L Accounts view is displayed. |  |
| 3 | Enter Selection Details | Choose Clear G/L Accounts > With Ledger Groups .Make the following entries and choose Go:Company Code: 3310G/L Account: For example, 24031100Posted by: For example, <today's date>Ledger Group: 2L | The G/L account to be cleared displays. |  |
| 4 | Account Selection | Select the account to be cleared. | The Clear G/L Accounts - Manual Clearing (F1579) view is displayed. |  |
| 5 | Repeat Process | Repeat steps 3 to 4 for the following values, then choose Post.On the Post to G/L accounts tab:G/L Account: For example, 10010000Credit Amount: For example, 100On the Open Items tab:Ensure that the relevant open item is activated.In the Processing Status section, the Amount entered and Assigned must match, and the Not assigned amount must be zero. | A new document is posted and the open item selected in the account is cleared. |  |
| 6 | Enter Details | Select or deselect the items to be cleared. |  |  |
| 7 | Save | Choose Post. | The open items selected in the account are cleared. If a difference is determined, a residual item or a new open item is created. |  |

### Clear Open Items Automatically for Ledger Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The transaction is used to automatically clear ledger-specific open items.

Prerequisites

You must post a Credit and Debit position to a G/L account that has ledger-specific clearing enabled. For example, use account 24031100 Pension Provision ledgerspec (which has ledger-specific open item management) and post:

a) Debit 61060000 (Payroll Exp. Pension) with cost center 33101101 to Credit 24031100 (Pension Provision ledgerspec.) and

b) Debit 24031100 (Pension Provision ledgerspec.) to Credit 12550000 (Unbilled Revenue)

|  |
| --- |
| Caution Both postings must contain a specific ledger group. See Post General Journal Entries or a similar step. To ensure that clearing is possible, the amounts for both postings should be the same. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries (Test Run) | Make the following entries:Note Expand the line to view more fields.HeaderJournal Entry Date: current datePosting Date: current datePeriod: periodDocument Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: 2LLine 1G/L Account: for example, 61060000Debit: <amount>, for example, 100Cost Center: 33101101Line 2G/L Account: for example, 24031100Credit: <amount>, for example, 100 | In the test run, check for errors in the detail list of open and cleared items before you perform the production run. A log of the clearing run is provided. For the chosen General Ledger account, all open items that show the same amount in the debit and credit are cleared. |  |
| 4 | Post | Choose Post. | The journal entries are posted. |  |
| 5 | Enter Second Document | Repeat Steps 3–4 for account 24031100 (debit) with an amount, for example, 100For account 12550000 (credit) with an amount, for example, 100 and item text, for example, Test. |  |  |

Procedure

Ensure there is a posting to an account that is open item managed.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear Open Items Automatically - For Ledger Group (F13L). | The Automatic Clearing view is displayed. |  |
| 3 | Enter Clearing Criteria | Make the following entries:Company Code: 3310Fiscal Year: Current yearG/L Account: 24031100Posting Parameters area:Clearing Date: Current dateLedger Group: 2Land choose Run. | A log of the clearing run is provided. For the chosen G/L account, all open items that show the same amount in the debit and credit are cleared. |  |
| 4 | Enter Clearing Criteria (Production Run) | Rerun step 3, but ensure that Test run isn't checked. Press Enter and choose Run once the warning message for production run is issued. |  |  |

### Reset Cleared Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you reset a document that shouldn't have been cleared.

|  |
| --- |
| Caution Resetting a large number of cleared documents can cause system performance issues. If you have more than 1000 items to process, the system automatically creates a scheduled job using Schedule Jobs to Reset Cleared Items (F9296). For more information, see [Schedule Jobs to Reset Cleared Items (Optional)](#unique_23) [page ] 32. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Reset Cleared Items (F2223). |  |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Clearing Journal Entry: <document number>Company Code: 3310 | The system displays a list of clearing entries. |  |
| 4 | Reset Cleared Items | For the item you want to reset, choose Details (>). | The Clearing Entry view is displayed. |  |
| 5 | Reset | Choose the Reset button. | The entry is reset. |  |

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

### Manage Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In General Ledger Accounting, you can use this app to display, change, or reverse a document. In this activity, it's used to reverse a document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A). |  |  |
| 3 | Select Journal Entry | Make the following entries and choose Go:Company Code: 3310Ledger Group: <Ledger Group ID, such as 2L for IFRS>Journal Entry Type (optional): for example, SADocument Number:Journal Entry Date (optional): <date>Period (optional): <period>Fiscal Year: <year> of posting documentPosting Date (optional): <date> | The system displays the selected documents in the Journal Entries list. |  |
| 4 | Select Journal Entry | Select relevant document and choose Reverse. | The Reverse Journal Entries dialog box is displayed. |  |
| 5 | Enter Reversal Data | Make the following entries and choose OK:Reversal Reason: for example, Wrong postingPosting Date (optional): <date> | The journal entry is reversed. |  |

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

You have two options for performing the foreign currency valuation: using Perform Foreign Currency Valuation (FAGL_FCV) or using Schedule General Ledger Accounting Jobs (F1927).

|  |
| --- |
| Note If Advanced Valuation is activated (the system displays an error message Advanced valuation active; you can no longer use the old report. Message no. FINS_FI_CLS023 is raised) and as long as there is no posting in the P system, you can deactivate this. To deactivate this, use the Activate Advanced Valuation configuration step (available in the Manage Your Solution (F1241) app (for more information on accessing the configuration step, see the Activate Advanced Valuation topic in Accounting and Financial Close (J58)). Now, you can run Perform Foreign Currency Valuation (FAGL_FCV). |

Prerequisite

You must post a Credit and Debit position, for example, to a bank clearing account with different exchange rates. The prerequisite posting must not be a special ledger posting as described in Post General Journal Entries (F0718) in this test script. It must be a posting according to the Post General Journal Entries (F0718) section in the Accounting and Financial Close (J58) test script without special ledger entry.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries Header Data | From Header, make the following entries:Journal Entry Date: <Date in the past period>Posting Date: <Date in past period>Period: <Period in the past>Journal Entry Type: SACompany Code: 3310Transaction Currency: a foreign currency, for example USD | The General Ledger Accountant account document is posted. The system has automatically added the Input tax amount. |  |
| 4 | Enter Line Item Data | From Line Items, make the following entries:G/L Account: for example, 63002000Debit: <amount>Tax Code: <Input Tax Code>Cost Center: for example, 33101101Line 2G/L Account: for example,11001030Credit: <amount>Value date: a date in past periodHouse Bank: use F4 search help to select one available house bankHouse Bank Account: use F4 search help to select one available house bank account. |  |  |
| 5 | Post | Choose Post. | The journal entries are posted. |  |

Procedure - Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the Fiori App | Open Perform Foreign Currency Valuation (FAGL_FCV). | The Foreign Currency Valuation view displays. |  |
| 3 | Enter Data | Make the following entries and choose Run:General SelectionsCompany Code: 3310Valuation Key Date: <date>Valuation Area: IFRSPosting ModeTest Run (No Database Update): SelectedNote Use the radio button to choose whether to Execute a test run, (default selection) or to Post valuation immediately.Posting ParametersDetermine Automatically: SelectedOpen Items: Subledger tab:Valuate Vendors: SelectedValuate Customers: SelectedOpen Items: G/L Accounts tab:Valuate G/L Accounts: Selected | Foreign currency postings in the system are represented in the financial statements with current date valuation.Two types of documents are posted:Reporting period documents to represent revaluation.Next period documents to reverse the first postings.The system generates a Foreign Currency Valuation report showing the details of what accounts, by document, were revaluated. The document data includes:Amount in Foreign CurrencyAmount in Local CurrencyExchange ratePosting DateNew DifferenceThe Gain/Loss Unrealized Foreign Currency Revaluation account gets debits and credits based on gain or loss determination. The Adjustment accounts for A/R and A/P (Domestic, Foreign, and Intercompany) get the off-set amount posted to the Gain/ Loss account. |  |

Procedure - Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule General Ledger Jobs (F1927). | The Application Jobs view is displayed. |  |
| 3 | Create a new job | Choose Create. | The New Job view is displayed. |  |
| 4 | Enter Data | Make the following entries and choose Step 2:Template Selection:Job Template: Foreign currency valuationJob Name: Foreign currency valuation | The job is created and started immediately. |  |
| 5 | Enter Data | Make the following entries and choose Step 3:Scheduling OptionsStart immediately: Selected |  |  |
| 6 | Enter Data | Make the following entries and choose Schedule:Parameters - General Selections:Company Code: 3310Valuation Key Date: <date>Valuation area:Postings area:Update Run: SelectedDetermine Automatically: SelectedOpen Items: Subledger area:Valuate Vendors: SelectedValuate Customers: SelectedOpen Items: G/L Accounts area:Valuate G/L Accounts: Selected Choose Schedule. |  |  |
| 7 | Check Job Status | After the job is finished, choose Details (>) for the row of your completed job. | The job log is displayed. |  |

### Post Currency Adjustments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you adjust account balances in foreign currencies. The app is useful in environments with volatile exchange rates, for example. You adjust the account balances by entering amounts for each currency directly.

|  |
| --- |
| Note If needed, you can find a parallel workflow for currency adjustments in the Appendix. For more information, see the subtopics there under Parallel Workflow - Currency Adjustment. |

Prerequisite

You posted journal entries in foreign currency (for example, to the foreign currency bank account 10010000) previously.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post Currency Adjustments (F1606). |  |  |
| 3 | Enter Document Data | Make the following entries and choose Post:HeaderJournal Entry Date: <Current date>Company Code: 3310Posting Date: <Current date>Transaction Currency: a foreign currency, for example, USDJournal Entry Type: SADebits/Credits Cur.: Company Code Currency (10)Line items 1G/L Account: <account number>, for example, 11001000Debit/Credit amount (Company Code Currency): <amount>, for example, 10 in the Debit fieldCaution You may need to press Enter after entering a value in the Debit or Credit fields to access the remaining fields.House Bank /House Bank Account: <house bank> and <house bank account>, for example, AEBK1 / USDACLine items 2G/L account: <account number>, for example, 21720200Debit/Credit amount (Company Code Currency): <amount>, for example, credit 10Tax code (If required): <tax code> for example, <Input Tax Code> | The document shows a zero amount in foreign currency and your entered amount in local currency. |  |

### Regroup Receivables/Payables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You must perform adjustment postings in the following cases:

- Sorted list according to remaining terms
- Vendors with a debit balance and customers with a credit balance
- Modified reconciliation accounts or partners (VBUND)

The system processes all accounts that use open item management. For each transfer posting created, a reset posting is also included. For customer or vendor reconciliation accounts, the system posts to an adjustment account.

The report regroups receivables and payables based on the required sort method (for example, 4th EU directive) and makes transfer postings. You can define your own sort methods.

|  |
| --- |
| Note In the standard system, SAP ships the remaining terms of the 4th EU directive in sort method EG93. This directive supports the following sorted list: |

- Receivables - less than 1 year and more than 1 year
- Payables - less than 1 year, 1- 5 years, and more than 5 years

A customer account's credit balance must be displayed as a payable, while the debit balance of a vendor account must be displayed as a receivable (vendors with a debit balance and customers with a credit balance).

In these cases, the report performs the relevant adjustment postings. The report carries out adjustment postings for modified reconciliation accounts or special G/L accounts. During this, the items in the old reconciliation accounts are assigned to the new accounts.

|  |
| --- |
| Note If Advanced Valuation is activated (the system displays an error message Advanced valuation active; you can no longer use the old report. Message no. FINS_FI_CLS023 is raised) and as long as there is no posting in the P system, you can deactivate this. To deactivate this, use the Activate Advanced Valuation configuration step (available in the Manage Your Solution (F1241) app (for more information on accessing the configuration step, see the Activate Advanced Valuation topic in Accounting and Financial Close (J58)). Now, you can run Regroup Receivables / Payables (FAGLF101). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Regroup Receivables / Payables (FAGLF101) | The Balance Sheet Supplement - OI - Analysis screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Run:Company Code: 3310Balance Sheet Key Date: <date in.CurrentFY>Sort method: SAP (EU 93 fin.stat.guidelines)Valuation Area: <value> for example, IF for year-end closingPostings tab:Generate postings: SelectedUse Batch input instead of ECS: Selected |  |  |
| 4 | Back | Choose Back. |  |  |
| 5 | Enter Selection Criteria | Make the following entries and choose Run:Batch Input Session Name: FAGL_CL_REGR (system defaults this value)Document Date: <date from.CurrentFY> (date of the first current year run)Journal Entry Type: SAPosting Date: <date from CurrentFY>Posting Period: <posting period, for example, 12>Reversal Posting Date: <date from.CurrentFY + 1>Reverse Posting Period: <reverse posting period, for example, 01>Selections tab:Account Type (D/K/S): D to KSupplier: Leave EmptyCustomer: Leave EmptyParameters tab; Other Parameters area:Changed rec.acct: Selected | The receivables and payables are regrouped.If a batch input session is created, process it as described in the Process Batch Input Session section. |  |

### Perform Advanced Foreign Currency Valuation

Purpose

In this activity, you perform advanced foreign currency valuation.

Procedure

Execute the test procedure step (including any prerequisites) of the same name in the Accounting and Financial Close (J58) test script, using the master, organizational, or other data from this test script.

### Credit-Risk-Based Impairment

Purpose

The new impairment model of IFRS 9, corresponding to the Current Expected Credit Loss (CECL) impairment model (ASC 326-20) use in US GAAP for financial assets appraised at amortized cost, requires calculating the Expected Credit Losses (ECL) on Trade Receivables. This calculation is done using a provision matrix, where rates change based on how long a trade receivable is outstanding. To estimate the provisioned sums, a routine valuation run can be performed to determine the bad debt expense posting for any overdue items.

Procedure

Execute the test procedure step (including any prerequisites) of the same name in the Accounting and Financial Close (J58) test script, using the master, organizational, or other data from this test script.

### Post B/S Reclassification

Purpose

In this activity, you post the balance sheet reclassification.

Procedure

Execute the test procedure step of the same name in the Accounting and Financial Close (J58) test script, using the master, organizational, or other data from this test script.

### Cash Flow Statement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the cash flow statement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Cash Flow Statement - Indirect Method (W0054). | The Display Cash Flow Statement - Indirect Method view is displayed. |  |
| 3 | Enter Details | Make the following entries and choose Go:From Fiscal Period: for example, 1To Fiscal Period: for example, 12Financial Statement Version: for example, CFG0Company Code: 3310Ledger fiscal year: <current year>Ledger: 2L for IFRS | The system displays the cash flow statement. |  |
| 4 | Change Layout | To add more criteria, choose Drilldown > Add Attribute . Select the attribute from the dialog box and choose OK. |  |  |

### Trial Balance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the trial balance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Trial Balance (F0996). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Ledger: <value> for example, 2L for IFRSCompany Code: 3310Posting Date From: <date>Posting Date To: <date>Note To display a readable amount of data in the chart, you can apply additional filters in the filter bar for G/L Account. This ensures that a reasonable data set is selected for graphical display. |  |  |
| 4 | Start Selection | To add more criteria, choose Drilldown > Add Attribute . Select the attribute from the dialog box and choose OK. | You can review the report findings. |  |

### Trial Balance Comparison

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report compares the trial balances of two different posting periods.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Trial Balance Comparison (W0097). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Ledger: <value> for example, 2L for IFRS LedgerCompany Code: 3310Posting Date From: <date>Posting Date To: <date>Comparison Posting Date From: <date>Comparison Posting Date To: <date> |  |  |
| 4 | Display Statement | To add more criteria, on the Data Analysis tab, choose Drilldown > Add Attribute . Select the attribute from the Select Attributes - G/L Account dialog box and choose OK. | You can review the report findings. |  |

## Appendix

### Balance Carryforward Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can view the status of the balance carryforward jobs.

The balance carryforward run (which carries forward account balances for all currencies into the new fiscal year) is automatically scheduled two weeks before the start of a new fiscal year and opening balance for a fiscal year are made available. Balances are also automatically updated whenever postings are made to the previous fiscal year. To handle postings that are made while a balance carryforward run is in process, balances are carried forward one day after the automatic balance carryforward is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Balance Carryforward Status (F4683). |  |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:To Fiscal Year: <fiscal year to which balances are carried forward>Company Code: 3310Ledger: <value> for example, 2L for IFRS | The Balance Carryforward Status pane shows a list of results. |  |
| 4 | Review Log | Analyze the Status column for the jobs. To view detailed status for a particular job, click the status message for that job. | The Log Details view displays the detailed status for the selected job. |  |

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
- related-to :: [[03-financial-accounting-and-close/accounting-and-financial-close-group-ledger-us-gaap-2va-ae-test-script]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1GA_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 74,415 chars in the whole document
