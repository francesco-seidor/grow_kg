---
id: 03-financial-accounting-and-close/accounting-and-financial-close-group-ledger-us-gaap-2va-ae-test-script
title: Accounting and Financial Close – Group Ledger US GAAP (2VA_AE) Test Script (2VA_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2VA_AE (UAE, company code 3310): ledger-group journal entries, clearing, FX valuation, trial balance."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/accounting-and-financial-close-us-gaap]
aliases: [2VA_S4CLD2608_BPD_EN_AE]
keywords: [Accounting and Financial Close with a Parallel Group…, journal entry verification, journal entry approval, journal entry posting, g/l account clearing, automatic clearing, foreign currency valuation, regroup receivables payables, trial balance, journal entry reversal]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VA_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-877
topic: 03-financial-accounting-and-close/accounting-and-financial-close-us-gaap
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Accounting and Financial Close – Group Ledger US GAAP (2VA_AE) Test Script (2VA_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VA_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Accounting and Financial Close with a Parallel Group Ledger (US GAAP or IFRS)** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Accounting and Financial Close – Group Ledger US GAAP (2VA_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Accounting and Financial Close – Group Ledger US GAAP (2VA_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850781)

[2 Prerequisites 4](#_Toc232850782)

[2.1 System Access 4](#_Toc232850783)

[2.2 Roles 4](#_Toc232850784)

[2.3 Master Data and Organizational Data 5](#_Toc232850785)

[2.4 Business Conditions 6](#_Toc232850786)

[2.5 Preliminary Steps 6](#_Toc232850787)

[2.5.1 Relevant Configuration Steps for Advanced Valuation Processes 6](#_Toc232850788)

[3 Overview Table 8](#_Toc232850789)

[4 Test Procedures 10](#_Toc232850790)

[4.1 Verify General Journal Entries for Ledger Group 10](#_Toc232850791)

[4.2 Approve Verify General Journal Entries (for Processor- Inbox) 13](#_Toc232850792)

[4.3 Reject Verify General Journal Entries (for Processor- Inbox) 15](#_Toc232850793)

[4.4 Edit a Rejected Verify General Journal Entry (Requester) 16](#_Toc232850794)

[4.5 Post General Journal Entries 17](#_Toc232850795)

[4.6 Manage Journal Entries 18](#_Toc232850796)

[4.7 Display G/L Account Balances 19](#_Toc232850797)

[4.8 Display Line Item Entry 20](#_Toc232850798)

[4.9 Display Line Items in General Ledger 21](#_Toc232850799)

[4.10 Audit Journal 22](#_Toc232850800)

[4.11 Journal Entry Analyzer 24](#_Toc232850801)

[4.12 Clear G/L Accounts - Manual Clearing with Ledger Group 25](#_Toc232850802)

[4.13 Clear Open Items Automatically for Ledger Group 28](#_Toc232850803)

[4.14 Reset Cleared Items 30](#_Toc232850804)

[4.15 Manage Journal Entries 31](#_Toc232850805)

[4.16 Perform Foreign Currency Valuation 32](#_Toc232850806)

[4.17 Post Currency Adjustments 35](#_Toc232850807)

[4.18 Regroup Receivables/Payables 37](#_Toc232850808)

[4.19 Perform Advanced Foreign Currency Valuation 39](#_Toc232850809)

[4.20 Credit-Risk-Based Impairment 39](#_Toc232850810)

[4.21 Post B/S Reclassification 39](#_Toc232850811)

[4.22 Trial Balance 40](#_Toc232850812)

[4.23 Trial Balance Comparison 41](#_Toc232850813)

[5 Appendix 42](#_Toc232850814)

[5.1 Balance Carryforward Status 42](#_Toc232850815)

## Purpose

Overview

The central tasks of General Ledger accounting are to provide a comprehensive picture of external accounting and accounts and to support parallel accounting.

General Ledger Accounting serves as a complete record of all business transactions providing a centralized, up-to-date reference for the rendering of accounts. Actual individual transactions can be checked at any time in real-time processing by displaying the original documents, line items, and transaction figures at various levels to support parallel accounting. These transactions include Manage Journal Entries, Post with Clearing for Ledger Group, Run Automatic Clearing Specific to Ledger Groups, Trial Balance Comparison, and Financial Statement Ledger Comparison.

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
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |
| General Ledger Accountant for United Arab Emirates | SAP_BR_GL_ACCOUNTANT_AE |  |  |  |

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

If you use parallel accounting and perform closing operations based on IFRS/US GAAP, before you perform advanced valuation processes, you must execute the following prerequisite steps from the Accounting and Financial Close (J58) test script using the master, organizational, or other data from this script:

|  |
| --- |
| Caution Ensure that you use 3L as ledger or USGP as accounting principle. |

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
| [Verify General Journal Entries for Ledger Group](#unique_9) [page ] 10 | General Ledger Accountant | Manage Workflows for Journal Entry Verification - In General Ledger (F2720) | The journal entry is checked. |
| [Approve Verify General Journal Entries (for Processor- Inbox)](#unique_10) [page ] 13 | General Ledger Accountant | Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728) | All documents received for approval are displayed. |
| [Reject Verify General Journal Entries (for Processor- Inbox)](#unique_11) [page ] 15 | General Ledger Accountant | Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728) | All documents checked by the user are displayed. |
| [Edit a Rejected Verify General Journal Entry (Requester)](#unique_12) [page ] 16 | General Ledger Accountant | Verify General Journal Entries - For Requester (F2547A) | All submitted documents are displayed. |
| [Post General Journal Entries](#unique_13) [page ] 17 | General Ledger Accountant | Post General Journal Entries (F0718) | The General Ledger Accountant Journal Entry is posted. The system has automatically added the Input tax amount. |
| [Manage Journal Entries](#unique_14) [page ] 18 | General Ledger Accountant | Manage Journal Entries (F0717A) | The Journal Entry has changed. |
| [Display G/L Account Balances](#unique_15) [page ] 19 | General Ledger Accountant | Display G/L Account Balances (F0707A) | The balances for every period in the year are displayed. |
| [Display Line Item Entry](#unique_16) [page ] 20 | General Ledger Accountant | Display Line Item Entry (F2218) | The G/L Account Line Items- G/L View screen displays. |
| [Display Line Items in General Ledger](#unique_17) [page ] 21 | General Ledger Accountant | Display Line Items in General Ledger (F2217) | A list of all relevant line items is displayed. |
| [Audit Journal](#unique_18) [page ] 22 | General Ledger Accountant | Audit Journal (F0997) | The correctness of the auditing reports is ensured. |
| [Journal Entry Analyzer](#unique_19) [page ] 24 | General Ledger Accountant | Journal Entry Analyzer (FIS_FPM_OVP_JEANA (FIS_FPM_OVP_JEANA)) | The Summation of amount and quantity of all selected journal entries according to various fields is displayed. Amounts are shown in different currencies (company code currency, document currency, global currency, and so on). |
| [Clear G/L Accounts - Manual Clearing with Ledger Group](#unique_20) [page ] 25 | General Ledger Accountant | Clear G/L Accounts - Manual Clearing (F1579) | The ledger-specific open items selected in the account have been cleared. If a difference is determined, a residual item or a new open item is created. |
| [Clear Open Items Automatically for Ledger Group](#unique_21) [page ] 28 | General Ledger Accountant | Post General Journal Entries (F0718) | The ledger-specific open items selected in the account have been cleared. |
| [Reset Cleared Items](#unique_22) [page ] 30 | General Ledger Accountant | Reset Cleared Items (F2223) |  |
| [Manage Journal Entries](#unique_23) [page ] 31 | General Ledger Accountant | Manage Journal Entries (F0717A) |  |
| [Perform Foreign Currency Valuation](#unique_24) [page ] 32 | General Ledger Accountant | Perform Foreign Currency Valuation (FAGL_FCV) | Foreign currency postings are represented with 'current date |
| [Post Currency Adjustments](#unique_25) [page ] 35 | General Ledger Accountant | Post Currency Adjustments (F1606) | You posted adjustments to account balances for foreign currencies. |
| [Regroup Receivables/Payables](#unique_26) [page ] 37 | General Ledger Accountant | Regroup Receivables / Payables (FAGLF101) |  |
| [Perform Advanced Foreign Currency Valuation](#unique_27) [page ] 39 |  | Execute the step of the same name in the Accounting and Financial Close (J58) test script. |  |
| [Credit-Risk-Based Impairment](#unique_28) [page ] 39 |  | Execute the step of the same name in the Accounting and Financial Close (J58) test script. |  |
| [Post B/S Reclassification](#unique_29) [page ] 39 |  | Execute the step of the same name in the Accounting and Financial Close (J58) test script. |  |
| [Trial Balance](#unique_30) [page ] 40 | General Ledger Accountant | Trial Balance (F0996) |  |
| [Trial Balance Comparison](#unique_31) [page ] 41 | General Ledger Accountant | Trial Balance Comparison (W0097) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Verify General Journal Entries for Ledger Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter a journal entry for review before final posting. You can check the status of your submitted journal entries in various tabs: All, Submitted, Rejected, and Others. If rejected, you can edit it and resubmit it for approval.

Journal entries in Submitted status aren't posted yet. Once the processor approves them, they're automatically posted. To view the postings, use the SAP Fiori App Manage Journal Entries (F0717A).

Prerequisites

You must activate approval workflows and define responsibility for rules used in workflow steps and assign users to responsibilities.

Prerequisite 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Workflows for Journal Entry Verification - In General Ledger (F2720). | The Manage Workflow view is displayed. |  |
| 3 | Create Workflow | Choose the Create button. | The new workflow view is displayed. |  |
| 4 | Enter Workflow Details | Make the following entries and choose Save:Header tab:Workflow Name: <workflow name>, for example, Journal Entry VerificationProperties tab:Description: for example, Company Code = 3310 Amount >=100 Account Group = FIN.Start Conditions tab: (add the following preconditions)Company Code: 3310Threshold Amount in Company Code Currency: <amount>, for example, 100Account Group: FIN.Steps tab:Under Workflow Steps, choose Create.Step Type: Verify Journal EntryChoose Create.Add a second Workflow Step.Step Type: Post General Journal EntryChoose Create. | You saved the workflow. |  |
| 5 | Activate Rule | Choose Save, then choose Activate. | The workflow journal entry verification is activated.Note You can create and activate multiple approval level workflows for G/L account groups, threshold amounts, and cost centers at the company code level. |  |

Prerequisite 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Manage Teams and Responsibilities For Journal Entry Verification - In General Ledger (F3932). |  |  |
| 3 | Create Team | Choose Create. | The Team view is displayed. |  |
| 4 | Enter Team Details | Make the following entries:Team Information tab:Name: for example, General Journal Entry VerifierStatus: EnabledType: FGLVG (FI general journal entry verification) |  |  |
| 5 | Enter Team Details | Choose the Team Members tab. |  |  |
| 6 | Enter Team Details | Choose the Create button. | A blank field displays below Business Partner. |  |
| 7 | Enter Team Details | Make the following entries and choose Save:Business Partner: For example, the local gl_accountant userFunction: FGJEV_L1 (Group 1 for Verifying G/L journal entries) | The Responsibility for the general journal entries approval workflow is defined |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access SAP Fiori App | Open Verify General Journal Entries - For Requester (F2547A). |  |  |
| 3 | Select Journal Entry | Make the following entry and choose Go.Company Code: 3310 | All company code journal entries are displayed under different tabs.Note Four tabs show journal entries in their various states: all, submitted, rejected, and others. |  |
| 4 | Access the Post General Journal Entries App | Choose Add. | The Post General Journal Entries (F0718) screen displays. |  |
| 5 | Enter Journal Entries Header Data | In the Header pane, make the following entries:Journal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: <Ledger Group number; for example, 3L for Group U.S. GAAP> |  |  |
| 6 | Enter Line Item Data | In the Line Items pane, make the following entries:G/L Account: for example, 63003000Debit: 100Tax Code: for example, <Input Tax Code> (if necessary for ledger group. Not required for 3L)Cost Center: for example, 33101101G/L Account: for example, 10010000Credit: <amount>Value Date: Today's date |  |  |
| 7 | Submit | Choose Submit. | The journal entry is submitted for verification. |  |
| 8 | Create a Second Document to be Verified | Repeat steps 4 to 7. | The journal entry is submitted for verification. |  |

### Approve Verify General Journal Entries (for Processor- Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive journal entries to be checked before final posting. After checking the journal entries, you can either approve or reject them with a comment or reason. Once a journal entry is selected and approved, it's removed from your list. If a journal entry is approved, posting of an FI journal entry is automatically triggered.

Prerequisites

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator. |  |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Users (F1303). |  |  |
| 3 | Search User | Make the following entry and choose GO.User name: GL_ACCOUNTANT_AE | The system displays a list of matching user names. |  |
| 4 | Choose User | Select the user name from the search result and choose Edit. | The Business User view is displayed. |  |
| 5 | Add Role to User | In the Assigned business roles section, choose Add. | The Add Business Roles view is displayed. |  |
| 6 | Choose Role to be Added | Search for and select the SAP_BR_GL_ACCOUNTANT role and choose OK. | The role is added in the Assigned Business Roles section. |  |
| 7 | Save | Save your entries. | The system confirms that the changes are saved. |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates . |  |  |
| 2 | Access the SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The My Inbox view is displayed. |  |
| 3 | Approve journal entries | Select the journal entry to be approved.Choose Approve. | The journal entry is approved and posted.Note All approved journal entries are displayed in the Verify General Journal Entry for Processor (Outbox) app as well as in the Verify Journal Entries app. |  |
| 4 | Display Posted journal entry | Access the Manage Journal Entries (F0717A) app, make the following selections, and choose Go:Company Code: 3310Ledger Group: <Ledger group number; for example, 3L for Group U.S. GAAP>Journal Entry Type (optional): for example, SAJournal Entry:Document Date: (optional): <date>Period (optional): <period>Fiscal Year: <year of posting document>Posting Date (optional): <date> | The approved journal entry is listed. |  |

### Reject Verify General Journal Entries (for Processor- Inbox)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You receive journal entries to be checked before final posting. After checking the journal entries, you can either approve or reject them with a comment or reason. Once a journal entry is selected and rejected, it's removed from your list and goes back to the requester.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant for United Arab Emirates |  |  |
| 2 | Access the SAP Fiori App | Open Verify Journal Entries in General Ledger - For Processor (Inbox) (F2728). | The My Inbox view is displayed. |  |
| 3 | Reject Journal Entries | Select the journal entry to be rejected and choose Reject. | The Submit Decision dialog box is displayed. |  |
| 4 | Reject Journal Entries | Make the following entries and choose Submit:Note: Change G/L 10010000 to 12540000 | The journal entry is rejected. |  |

### Edit a Rejected Verify General Journal Entry (Requester)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before you do the final posting, you must check the journal entries. The journal entry you submitted is rejected. To be approved and posted, you must make the changes requested by the approver.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Verify General Journal Entries - For Requester (F2547A). | The Verify Journal Entries view is displayed. |  |
| 3 | Select Journal Entry | Make the following entry and choose Go.Company Code: 3310Ledger Group: <Ledger group number> for example, 3L (Group U.S. GAAP)Status: Rejected (R)Note To see more fields to filter on, choose Adapt Filters and search for field names that are not displayed in the standard view. | The rejected journal entries are listed in the Journal Entries pane. |  |
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
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. | ad displays. |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries Header Data | In the Header pane, make the following entries:Journal Entry Date: <current date>Posting Date: <current date>Period: <period>Journal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: <Ledger group number> for example, 3L for Group U.S. GAAP | The General Ledger Accountant account document is posted. The system has automatically added the Input tax amount.Note Document Type AD can be used to enter accruals/deferrals into the system. |  |
| 4 | Enter Line Item Data | In the Line Items pane, make the following entries:G/L Account: for example, 63002000Debit: 100Cost Center: 33101101 |  |  |
| 5 | Add New Line Item | Choose the Plus + button to create a new line. |  |  |
| 6 | Enter Line Item Data | In the Line Items pane, make the following entries and choose Post:G/L Account: for example, 10010000Credit: <amount>. | The journal entries are posted. |  |

### Manage Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In G/L accounting. you can use this app to display, change, or reverse a document. In this activity, you use it to display a document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A). |  |  |
| 3 | Select Journal Entry | Make the following entries and choose Go:Company Code: 3310Ledger Group: <Ledger group ID, such as 3L for Group U.S. GAAP>Journal Entry Type (optional): for example, SAJournal Entry (optional):Journal Entry Date (optional): <date>Period (optional): <period>Fiscal Year: <year of posting document>Posting Date (optional): <date> | The selected documents are displayed in the Journal Entries list. |  |
| 4 | Select Option | In the Journal Entries list, click the journal entry number.Note Do not select the checkbox to the left of the journal entry number. Click the actual number. | The Journal Entry info box displays. |  |
| 5 | Display Document | Select an option from the displayed list.Caution Don't reverse or reset the posting as it is needed for the following steps. | The Journal Entry view displays the document details. |  |

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
| 3 | Enter Account Details | Make the following entries and choose Go:Ledger: <Ledger ID>, for example, 3L for Group U.S. GAAPCompany Code: 3310G/L Account: for example, 10010000Fiscal Year of Ledger: <year of posting document>From Period: <from date>To Period: <to date> | The account balances show in the Balances pane. If you want to change the currency used for the balances, select the desired currency from the Currency dropdown. |  |

### Display Line Item Entry

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display and change line items in a G/L account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Line Item Entry (F2218). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Company Code: 3310Account: <open item managed account>, for example, 11001010Status: Open itemsOpen on Key Date: <Current date>Chart of Accounts: for example, YCOANote You can't change accounts, amounts, tax amounts, or tax codes. If you receive an error regarding document contents after posting, you must reverse it. | A list of line items is displayed. You can choose any of the journal entry links to view or process the line item further. |  |

### Display Line Items in General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display line items of G/L accounts in reporting view.

You can display open, cleared, or all line items in the reporting view. The reporting view also offers the following functions:

- You can specify the ledger for which you want to display the line items. The line items displayed are combined from the documents in the entry view and the reporting view.
- With the custom selections, you can also make selections using general ledger account assignments (General Ledger Line Items).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Line Items in General Ledger (F2217). |  |  |
| 3 | Enter Search Criteria | Make the following entries and choose Go:Ledger: 3L for Group U.S. GAAPCompany Code: 3310G/L Account: <open item managed account>, for example, 11001010Status: <Open items>Open on Key Date: <Current date> | A list of line items is displayed. |  |

### Audit Journal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can run various auditing reports to ensure the correctness of your journal. This report has the following key features:

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
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Note Select the values using the appropriate checkbox. If the values aren't available, enter the value in the Key field.Company Code: 3310Fiscal Year: <Current fiscal year>Ledger: 3L for Group U.S. GAAP | The compact journal entries are displayed. |  |
| 4 | Display Changes to Journal Entries | Choose the Display Journal Entry Changes button.Review the report and go back. | The report shows logs for changes made to journal entries after initial posting. |  |
| 5 | Check Multireferenced Invoices | Choose the Check Multi-Referenced Invoices button.Review the report and go back | The report lists invoices when referenced in multiple journal entries. |  |
| 6 | Check Gaps in Journal Entry Numbering | Choose the Check Gaps Journal Entry Numbering button.Review the report. | The report displays all gaps that occur within a given time period. |  |
| 7 | Display Updated Terminations | Choose Display Updated Terminations.Note The button is only enabled if there are termination errors. |  |  |
| 8 | Display Updated Terminations | Make the following entries and choose Go:Creation date: Time periodCheck the report and go back. | The report displays all system terminations that occur within a given time period. |  |

### Journal Entry Analyzer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The journal entry analyzer gives an overview of cumulated amounts of selected journal entries on G/L accounts. This can be grouped by various fields from the header or line item segment, such as company code, fiscal year, posting date, business area, functional area, or profit center.

Prerequisite

Journal entries are posted to the G/L accounts and posting period selected in the report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Journal Entry Analyzer (FIS_FPM_OVP_JEANA (FIS_FPM_OVP_JEANA)). | The Prompts view is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Company Code: 3310Fiscal Year of Ledger: <Current year>Ledger: 3L (Group U.S. GAAP)Fiscal Period: for example, current period | The system displays cumulated amounts and quantity of selected journal entries grouped by company code, G/L account, and posting date. The amounts are listed in different currencies. |  |
| 4 | Add Field | From the Dimensions panel, drag and drop fields on both the row and column axis.For example, Cost Center. | The list is refreshed and the new field is shown. |  |

### Clear G/L Accounts - Manual Clearing with Ledger Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The transaction is used to manually clear ledger-specific open items. If the balance of the items to be cleared isn't 0, you can create a residual item for overpayments/ underpayments.

Prerequisites

You must post a Credit and Debit position to a G/L account where ledger-specific clearing is enabled.

For example, use account 24031100, Pension Provision ledger spec (which has ledger-specific OI management) and post:

1. Debit 61060000 (Payroll Exp. Pension) with cost center 33101101 to Credit 24031100 (Pension Provision ledger spec.)
2. Debit 24031100 (Pension Provision ledger spec.) to Credit 12550000 (Unbilled Revenue)

|  |
| --- |
| Caution Both postings must contain a specific ledger group! See Post General Journal Entries or a similar step. The amounts for both postings should match, so that a clearing is possible. |

Prerequisites

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries | Make the following entries:HeaderJournal Entry Date: current datePosting Date: current datePeriod: periodJournal Entry Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: 3LLine 1G/L Account: for example, 61060000Debit: <amount>, for example, 100Cost Center: 33101101Line 2G/L Account: for example, 24031100Credit: <amount>, for example 100 |  |  |
| 4 | Post | Choose Post. | The journal entries are posted. |  |
| 5 | Enter Second Document | Repeat Steps 3 and 4 for account 24031100 (debit) with amount, for example, 100 and account 12550000 (credit) with amount, for example, 100, the tax code A0 and item text, for example, Test. | The journal entries are posted. |  |

Procedure

Ensure that there's a posting to an account that is open item managed.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear G/L Accounts - Manual Clearing (F1579). |  |  |
| 3 | Enter Selection Details | Choose G/L Accounts with Ledger Groups.Make the following entries and choose Go:Company Code: 3310G/L Account: For example, 24031100Ledger Group: 3LPosted by: For example, today's dateand choose Clear G/L Accounts with ledger Groups. | The G/L account to be cleared displays. |  |
| 4 | Account Selection | Select the account to be cleared. | The Clear G/L Accounts - Manual Clearing (F1579) view is displayed. |  |
| 5 | Repeat | Repeat steps 2 to 4 for the following values, then choose Post.On the Post to G/L accounts tab:G/L Account: For example, 10010000Credit Amount: For example, 100On the Open Items tab:Ensure that the relevant open item is activated.In the Processing Status section, the Amount entered and Assigned must match, and the Not assigned amount must be zero. | A new document is posted and the open item selected in the account is cleared. |  |
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

In this activity, you clear ledger-specific open items automatically.

Prerequisites

You must post a Credit and Debit position to a G/L account for which the ledger-specific clearing is enabled. For example, use account 24031100 Pension Provision ledgerspec (which has ledger-specific open item management) and post:

a) Debit 61060000 (Payroll Exp. Pension) with cost center 33101101 to Credit 24031100 (Pension Provision ledgerspec.) and

b) Debit 24031100 (Pension Provision ledgerspec.) to Credit 12550000 (Unbilled Revenue)

|  |
| --- |
| Caution Both postings must contain a specific ledger group. See [Post General Journal Entries](#unique_13) [page ] 17 or a similar step. To ensure that clearing is possible, the amounts for both postings should be the same. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries (Test Run) | Make the following entries:HeaderJournal Entry Date: current datePosting Date: current datePeriod: periodDocument Type: SACompany Code: 3310Transaction Currency: AEDLedger Group: 3LLine 1G/L Account: for example, 61060000Debit: <amount>, for example, 100Cost Center: 33101101Line 2G/L Account: for example, 24031100Credit: <amount>, for example, 100 | In the test run, check for errors in the detail list of open and cleared items before starting in the next step the Production run. A log of the clearing run is provided. For the chosen General Ledger account, all open items that show the same amount in the debit and credit are cleared. |  |
| 4 | Post | Choose Post. | The journal entries are posted. |  |
| 5 | Enter Second Document | Repeat Steps 3-4 for account 24031100 (debit) with an amount, for example, 100For account 12550000 (credit) with an amount, for example, 100, the tax code AO and item text, for example, Test: | The journal entries are posted. |  |

Procedure

Ensure there is a posting to an account that is open item managed.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear Open Items Automatically - For Ledger Group (F13L). | The Automatic Clearing Specific to Ledger Groups view is displayed. |  |
| 3 | Enter Clearing Criteria | Make the following entries and choose Run:Fiscal Year: Current yearCompany Code: 3310G/L Account: 24031100Clearing Date: Current dateLedger Group: 3L | A log of the clearing run is provided. For the chosen General Ledger account, all open items that show the same amount in the debit and credit are cleared. |  |
| 4 | Enter Clearing Criteria (Production Run) | Rerun step 3, but ensure that Test run is not checked. Choose Run once the warning message for production run is issued. |  |  |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Reset Cleared Items (F2223). | The Reset Cleared Items (F2223) view is displayed. |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Clearing Entry: <document number>Company Code: 3310 | The system displays a list of clearing entries. |  |
| 4 | Reset Cleared Items | Choose the > button to the right of a row for an entry. | The Clearing Entry view is displayed. |  |
| 5 | Reset | Choose Reset. | You reset the document that shouldn't have been cleared. |  |

### Manage Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In G/L accounting, you can use this app to display, change, or reverse a document. In this activity, it is used to reverse a document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A). |  |  |
| 3 | Select Journal Entry | Make the following entries and choose Go:Company Code: 3310Ledger Group: <Ledger Group ID, such as 3L for Group U.S. GAAP>Journal Entry Type(optional): for example, SAJournal Entry:Document Date(optional): <date>Period (optional): <period>Fiscal Year: <year> of posting documentPosting Date (optional): <date> | The selected documents are displayed in the Journal Entries list. |  |
| 4 | Select Journal Entry | Select relevant document and choose Reverse. | The Reverse Journal Entries Details dialog box is displayed. |  |
| 5 | Enter Reversal Data | Make the following entries and choose OK:Reversal Reason for example, Wrong postingPosting Date (optional): <date> | The journal entry is reversed. |  |

### Perform Foreign Currency Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The total difference of all the open account items is posted to a balance sheet adjustment account, retaining the original account balance. The gains or losses from exchange rate fluctuations from the valuation are entered as offsetting entries in separate expense and revenue accounts for exchange rate differences. If you perform an update run and enter a session name for the batch input session, you can run the session after it is created.

You have two options for performing the foreign currency valuation: using Perform Foreign Currency Valuation (FAGL_FCV) or using Schedule General Ledger Accounting Jobs (F1927).

|  |
| --- |
| Note If Advanced Valuation is activated (the system displays an error message Advanced valuation active; you can no longer use the old report. Message no. FINS_FI_CLS023 is raised) and as long as there is no posting in the P system, you can deactivate this. To deactivate this, use the Activate Advanced Valuation configuration step (available in the Manage Your Solution (F1241) app (for more information on accessing the configuration step, see the Activate Advanced Valuation topic in Accounting and Financial Close (J58)). Now, you can run Perform Foreign Currency Valuation (FAGL_FCV). |

Prerequisite

You must post a Credit and Debit position, for example to a bank clearing account with different exchange rates. The prerequisite posting must not be a special ledger posting as described in the Post General Journal Entries (F0718) in this test script. It must be a posting according to the Post General Journal Entries (F0718) section in the Accounting and Financial Close (J58) test script without special ledger entry.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). |  |  |
| 3 | Enter Journal Entries Header Data | From Header, make the following entries:Journal Entry Date: <Date in the past period>Posting Date: <Date in past period>Period: <Period in the past>Journal Entry Type: SACompany Code: 3310Transaction Currency: a foreign currency, for example USD | The G/L account document is posted. The system has automatically added the Input tax amount. |  |
| 4 | Enter Line Item Data | From Line Items, make the following entries:G/L Account: for example, 63002000Debit: <amount>Tax Code: <Input Tax Code>Cost Center: for example,33101101G/L Account: for example,11001030Credit: <amount>Value date: a date in past periodHouse Bank: use F4 search help to select one available house bankHouse Bank Account: use F4 search help to select one available house bank account. |  |  |
| 5 | Post | Choose Post. | The journal entries are posted. |  |

Procedure - Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the Fiori App | Open Perform Foreign Currency Valuation (FAGL_FCV). | The Foreign Currency Valuation view is displayed. |  |
| 3 | Enter Data | Make the following entries and choose Run:General SelectionsCompany Code: 3310Valuation Key Date: <date>Valuation Area: UV for Group U.S. GAAPPosting ModeExecute Test Run: SelectedNote Use the radio button to choose whether to Execute a test run, (default selection) or to Post valuation immediately.Posting ParametersDetermine Automatically: SelectedOpen Items: SubledgerValuate Vendors: SelectedValuate Customers: SelectedOpen Items: G/L AccountsValuate G/L Accounts: Selected | Foreign currency postings in the system are represented in the financial statements with current date valuation.Two types of documents are posted:Reporting period documents to represent 'revaluation'.Next period documents to reverse the first postings.The system creates a Foreign Currency Valuation report showing the details of what accounts, by document, were revaluated. The document data includes:Amount in Foreign CurrencyAmount in Local CurrencyExchange ratePosting DateNew DifferenceThe Gain/Loss Unrealized Foreign Currency Revaluation account is or and credited based on gain or loss determination. The Adjustment accounts for A/R and A/P (Domestic, Foreign, and Intercompany) get the off-set amount posted to the Gain/ Loss account. |  |

Procedure - Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule General Ledger Jobs (F1927). | The Application Jobs view is displayed. |  |
| 3 | Create a new job | Choose Create. | The New Job: Advanced Foreign Currency Valuation view is displayed. |  |
| 4 | Enter Data | Make the following entries and choose Step 2:Template Selection:Job Template: for example, Foreign currency valuationJob Name: for example, Foreign currency valuation | The job is created and started immediately. |  |
| 5 | Enter Data | Make the following entries and choose Step 3:Scheduling OptionsStart immediately: Make the following entries and choose Selected |  |  |
| 6 | Enter Data | Make the following entries and choose Schedule:Parameters - General Selections:Company Code: 3310Valuation Key Date: <date>Valuation area:Postings area:Update Run: SelectedDetermine Automatically: SelectedOpen Items: Subledger area:Valuate Vendors: SelectedValuate Customers: SelectedOpen Items: G/L Accounts area:Valuate G/L Accounts: Selected |  |  |
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

You use this app to adjust account balances in foreign currencies. It can be useful in environments with volatile exchange rates, for example. To adjust the account balances, you enter amounts for specific currencies directly. This app is available for the General Ledger Accountant role.

Prerequisite

You've posted journal entries in foreign currency (for example, to the foreign currency bank account 10010000) in previous test steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the Fiori App | Open Post Currency Adjustments (F1606). |  |  |
| 3 | Enter Document Data | Make the following entries:HeaderJournal Entry Date: <Current date>Posting Date: <Current date>Company code: 3310Transaction Currency: a foreign currency, for example, USDJournal Entry Type: SALine items 1G/L account: <account number>, for example, 11001000Debit/Credit amount: <amount>, for example, Debit 10House Bank /House Bank Account: use search help to select a valid <house bank>, for example AEBK1/AEAC1and a <house bank account>Line items 2G/L account: <account number>, for example, 21720200Debit/Credit amount: <amount>, for example, credit 10Tax code (if necessary): <tax code>, for example, <Input Tax Code> |  |  |
| 4 | Post | Choose the Post button. | A log is displayed. |  |

### Regroup Receivables/Payables

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You must perform adjustment postings in these cases:

1. Sorted list according to remaining terms
2. Vendors with a debit balance and customers with a credit balance
3. Modified reconciliation accounts or partners (VBUND)

The system processes all accounts that are maintained with open item management. For each transfer posting created, a reset posting is also included in the session. For customer or vendor reconciliation accounts, the system posts to an adjustment account.

The report regroups the receivables and payables according to the required sort method (for example, 4th EU directive) and carries out transfer postings. You can define your own sort methods.

|  |
| --- |
| Note In the standard system, SAP ships the remaining terms of the 4th EU directive in sort method EG93. This directive supports the following sorted list:Receivables: less than 1 year and more than 1 yearPayables: less than 1 year, 1- 5 years, and more than 5 years |

A customer's credit balance must be displayed as a payable, while a vendor's debit balance must be displayed as a receivable (vendors with a debit balance and customers with a credit balance).

In these cases, the report performs the relevant adjustment postings. The report performs adjustment postings for modified reconciliation accounts or special G/L accounts. During this, the items in the old reconciliation accounts are assigned to the new accounts.

|  |
| --- |
| Note If Advanced Valuation is activated (the system displays an error message Advanced valuation active; you can no longer use the old report. Message no. FINS_FI_CLS023 is raised) and as long as there is no posting in the P system, you can deactivate this. To deactivate this, use the Activate Advanced Valuation configuration step (available in the Manage Your Solution (F1241) app (for more information on accessing the configuration step, see the Activate Advanced Valuation topic in Accounting and Financial Close (J58)). Now, you can run Regroup Receivables / Payables (FAGLF101). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Regroup Receivables / Payables (FAGLF101). | The Balance Sheet Supplement - OI - Analysis view is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries:Company Code: 3310Balance Sheet Key Date: <date in.CurrentFY>Sort Method: SAP (sorted list to 93 EU directive)Valuation Area: <value> for example, UV for Group U.S. GAAPPostingsGenerate Postings: SelectedBatch input instead of ECS: SelectedChoose Enter and fill in the Batch Input Session Name: FAGL_CL_REGRDocument Date: <date from.CurrentFY>Document Type: SAPosting Date: <date from CurrentFY>Posting Period: 12Reversal Posting Date: <date from.CurrentFY + 1>Reverse Posting Period: 01SelectionsAccount Type: D to KSupplier: Leave EmptyCustomer: Leave EmptyParametersChanged rec.acct: Selected |  |  |
| 4 | Execute | Choose Run. | The receivables and payables are regrouped.If a batch input session is created, then process it as described in the Process Batch Input Session section. |  |

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
| 3 | Enter Details | Make the following entries and choose OK:Ledger: <value> for example, 3L for Group U.S. GAAPCompany Code: 3310Posting date from: <date>Posting date to: <date>Note To display a readable amount of data in the chart, you can apply additional filters in the filter bar for G/L Account. This ensures that a reasonable data set is selected for graphical display. |  |  |
| 4 | Start Selection | You can drag criteria for the dimensions from the Dimensions panel to the Columns or Rows panels.Add criteria in the rows axis: for example, Company Code or G/L Account. | You can review the report findings. |  |

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
| 3 | Enter Details | Make the following entries and choose OK:Ledger: <value> for example, 3L for Group U.S. GAAPCompany Code: 3310Posting date from: <date>Posting date to: <date>Comparison Posting date from: <date>Comparison Posting date to: <date> |  |  |
| 4 | Display Statement | You can drag criteria for the dimensions from the Dimensions panel to the Columns or Rows panels.Add criteria in the rows axis: for example, Company Code or G/L Account. |  |  |

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
| 3 | Enter Selection Criteria | Make the following entries and choose Go:To Fiscal Year: <fiscal year to which balances are carried forward>Company Code: 3310Ledger: <value> for example, 3L for Group U.S. GAAP | The Balance Carryforward Status pane shows a list of results |  |
| 4 | Review Log | Analyze the Status column for the jobs. To view detailed status for a particular job, choose the status message for that job. | The Log Details view displays the detailed status for the selected job. |  |

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
- related-to :: [[03-financial-accounting-and-close/test-script-accounting-and-financial-close-group-ledger-ifrs-1ga-ae-sa]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2VA_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 67,171 chars in the whole document
