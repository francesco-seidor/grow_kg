---
id: 04-tax-and-statutory-reporting/test-script-contract-accounting-external-tax-audit-and-compliance-repo
title: "Test Script: Contract Accounting – External Tax Audit and Compliance Reporting (2SJ_AE) (2SJ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 2SJ_AE: FI-CA external auditor access (direct, indirect, file), data extracts, and tax report steps."
cluster: 04-tax-and-statutory-reporting
tags: [kb/tax-and-statutory-reporting, topic/external-tax-audit-and-auditor-access]
aliases: [2SJ_S4CLD2608_BPD_EN_AE]
keywords: [External Tax Audit and Auditor Access, external tax audit, auditor system access, data extracts, tax reporting, contract accounting, test scripts, general ledger reconciliation, business roles, test prerequisites]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2SJ_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-860
topic: 04-tax-and-statutory-reporting/external-tax-audit-and-auditor-access
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Contract Accounting – External Tax Audit and Compliance Reporting (2SJ_AE) (2SJ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2SJ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **External Tax Audit and Auditor Access** in Tax and Statutory Reporting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Contract Accounting – External Tax Audit and Compliance Reporting (2SJ_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Contract Accounting – External Tax Audit and Compliance Reporting (2SJ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850214)

[2 Prerequisites 4](#_Toc232850215)

[2.1 System Access 4](#_Toc232850216)

[2.2 Roles 4](#_Toc232850217)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232850218)

[2.4 Business Conditions 5](#_Toc232850219)

[3 Overview Table 7](#_Toc232850220)

[4 Test Procedures 11](#_Toc232850221)

[4.1 Access Type: Direct System Access 11](#_Toc232850222)

[4.1.1 Display for General Ledger Transfer 11](#_Toc232850223)

[4.1.2 Itemization for General Ledger Documents 11](#_Toc232850224)

[4.1.3 Display Posting Totals 12](#_Toc232850225)

[4.1.4 Display Itemization for Posting Totals 12](#_Toc232850226)

[4.1.5 Display Account Assignment for Single Documents 12](#_Toc232850227)

[4.1.6 Check Transfer Status of Reconciliation Key 12](#_Toc232850228)

[4.1.7 Check Totals Records 13](#_Toc232850229)

[4.1.8 Check General Ledger Documents 13](#_Toc232850230)

[4.1.9 Determine Gaps in Document Number Range 13](#_Toc232850231)

[4.1.10 Display Receivables Adjustments Transferred 14](#_Toc232850232)

[4.1.11 Display Foreign Currency Valuation 14](#_Toc232850233)

[4.1.12 Itemization of Clarification Accounts - Returns 14](#_Toc232850234)

[4.1.13 Itemization of Clarification Accounts - Payments 14](#_Toc232850235)

[4.1.14 Document Journal 15](#_Toc232850236)

[4.1.15 Evaluate Open Items 15](#_Toc232850237)

[4.1.16 Business Partner Financial Overview 15](#_Toc232850238)

[4.1.17 Display Contract Account 16](#_Toc232850239)

[4.1.18 Display Account Balance 16](#_Toc232850240)

[4.1.19 Display Document 17](#_Toc232850241)

[4.1.20 Display Document Changes 17](#_Toc232850242)

[4.1.21 Display Installment Plan 18](#_Toc232850243)

[4.1.22 Display Reconciliation Key 18](#_Toc232850244)

[4.1.23 Display Write-Offs 19](#_Toc232850245)

[4.1.24 Display Returns 19](#_Toc232850246)

[4.1.25 Display Dunning History 20](#_Toc232850247)

[4.1.26 Display Dunning Exceptions 20](#_Toc232850248)

[4.1.27 Display Interest Calculation 20](#_Toc232850249)

[4.1.28 Display Installment Plan History 21](#_Toc232850250)

[4.1.29 Display Correspondence History 21](#_Toc232850251)

[4.1.30 Monitor Payments with Payment Card 22](#_Toc232850252)

[4.1.31 Display Payment Card Details 22](#_Toc232850253)

[4.1.32 Display Repayment Requests 22](#_Toc232850254)

[4.1.33 Invoicing Overview for Contract Accounts 23](#_Toc232850255)

[4.1.34 Display Invoicing Documents 23](#_Toc232850256)

[4.1.35 Display Billing Documents 24](#_Toc232850257)

[4.1.36 Display Billable Items 25](#_Toc232850258)

[4.2 Access Type: Indirect System Access 26](#_Toc232850259)

[4.3 Access Type: File Access 26](#_Toc232850260)

[4.3.1 Export Customizing Extracts 26](#_Toc232850261)

[4.3.2 Import Customizing Extracts 27](#_Toc232850262)

[4.3.3 Export Partner Extracts 28](#_Toc232850263)

[4.3.4 Import Partner Extracts 30](#_Toc232850264)

[4.3.5 Export Documents Extracts 31](#_Toc232850265)

[4.3.6 Import Documents Extracts 32](#_Toc232850266)

[4.3.7 Manage Extracts 34](#_Toc232850267)

[4.3.8 Delete Customizing Extracts 35](#_Toc232850268)

[4.3.9 Delete Document Extracts 36](#_Toc232850269)

[4.3.10 Delete Partner Extracts 37](#_Toc232850270)

[4.3.11 Evaluate Extracted Data 38](#_Toc232850271)

[4.4 Tax Report 39](#_Toc232850272)

[4.4.1 Display Tax Data for Tax Report 42](#_Toc232850273)

[4.4.2 Transfer Tax Data for Tax Report 43](#_Toc232850274)

## Purpose

Overview

This process allows internal and external auditors to view, analyze, and extract accounting-relevant data from Contract Accounts Receivable and Payable (FI-CA). Accounting data covers the relevant customizing extracts, business partner extracts, and FI-CA documents. Extracts are exported by the Administrator – Accounts Payable and Receivable (FI-CA) and are analyzed by the External Auditor – Accounts Payable and Receivable (FI-CA). Extracts can also be imported into standard tax auditor software. This scope item supports the three legally required access types: direct system access, indirect system access, and file access.

- Direct System Access: The external auditor is allowed to use the normal accountant functionality with read-only access. The auditor has direct system access to posting data and master data to enable the review of single cases in the system. The external auditor can also verify the reconciliation of the subledger FI-CA with the G/L.
- Indirect System Access: Most important system data is extracted and imported into FI-CA database tables with reduced fields (so called short-tables). The external auditor is only authorized to display the data in the short-tables with the reduced field sets. The administrator must prepare the system before the audit and exports the data from productive tables and imports it into the short-tables.
- File Access: The external auditor has no authorization to the system at all. The auditor is only provided extracted data in files, which is possible by importing into an audit software designed especially for audit use cases.

This scope item also provides the solution for the fulfillment of real-time and statutory reporting requirements. This solution enables the end-to-end process of legal reporting and includes multiple activities that may be necessary to complete the legal reporting. The solution offers a unified and harmonized user experience across countries and reports, enabling a simplified view of the reporting status for the business users and the company's head of tax and compliance. It also provides a design environment to easily create and extend additional report requirements.

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
| Administrator - Accounts Payable and Receivable (FI-CA) | SAP_BR_ADMIN_APR_FICA | Contract Accounting - Jobs | SAP_BR_ADMIN_APR_FICA |  |
| External Auditor - Accounts Payable and Receivable (FI-CA) | SAP_BR_EXT_AUDITOR_APR_FICA | Contract Accounting - Auditing | SAP_BR_EXT_AUDITOR_APR_FICA |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comment |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Company Code Group | 3310 |  |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Business Partner and Contract Account Master Data must be created. |
| 2BI - Contract Accounting – Customer Initiated Payments | Transaction documents for contract accounting must be created. |
| 2BK - Contract Accounting – Daily and Monthly Closing | Transaction documents for contract accounting must be created. |
| 2DP - Contract Accounting – Company Initiated Payments | Transaction documents for contract receivable and contracts payable must be created. |
| 2UJ - Contract Accounting – Open Item Management | Installment Plans have been posted, invoices have been dunned, credit had been clarified and interests have been posted. |
| 2BG - Convergent Invoicing – Invoice Creation for Usage and Service | Invoices must be posted. |

## Overview Table

Contract Accounting – External Tax Audit and Compliance Reporting consists of process steps for the three levels of access for auditing, as described in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Access Type: Direct System Access

For this first access type, the external auditor is allowed to use the normal accountant functionality with read-only access. The external auditor has direct system access for posting data and master data, allowing the audit of single cases in the system. The external auditor also can review the reconciliation of the subledger FI-CA with the G/L.

External Auditor – Accounts Payable and Receivable (FI-CA): Transactions for Reconciliation

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Display for General Ledger Transfer](#unique_8) [page ] 11 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display for General Ledger Transfer (FPT3) |  |
| [Itemization for General Ledger Documents](#unique_9) [page ] 11 | External Auditor - Accounts Payable and Receivable (FI-CA) | Itemization for G/L Documents (FPG5) |  |
| [Display Posting Totals](#unique_10) [page ] 12 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display for Posting Totals (FPT7) |  |
| [Display Itemization for Posting Totals](#unique_11) [page ] 12 | External Auditor - Accounts Payable and Receivable (FI-CA) | Itemization for Posting Totals (FPT5) |  |
| [Display Account Assignment for Single Documents](#unique_12) [page ] 12 | External Auditor - Accounts Payable and Receivable (FI-CA) | Acct Assignment Details for Single Docs (FPT8) |  |
| [Check Transfer Status of Reconciliation Key](#unique_13) [page ] 12 | External Auditor - Accounts Payable and Receivable (FI-CA) | Check Transfer Status of Reconciliation Key (FPT4) |  |
| [Check Totals Records](#unique_14) [page ] 13 | External Auditor - Accounts Payable and Receivable (FI-CA) | Check Totals Records (FPT1) |  |
| [Check General Ledger Documents](#unique_15) [page ] 13 |  | Check General Ledger Documents (FPG2) |  |
| [Determine Gaps in Document Number Range](#unique_16) [page ] 13 | External Auditor - Accounts Payable and Receivable (FI-CA) | Determine Gaps in Document Number Ranges (FPDOC) |  |
| [Display Receivables Adjustments Transferred](#unique_17) [page ] 14 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Posted Value Adjustments (F4824) |  |
| [Display Foreign Currency Valuation](#unique_18) [page ] 14 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Foreign Currency Valuations (FPW2) |  |
| [Itemization of Clarification Accounts - Returns](#unique_19) [page ] 14 | External Auditor - Accounts Payable and Receivable (FI-CA) | Itemization of Clarification Accounts - Returns (FPR_RLCL) |  |
| [Itemization of Clarification Accounts - Payments](#unique_20) [page ] 14 | External Auditor - Accounts Payable and Receivable (FI-CA) | Itemization of Clarification Accounts - Returns (FPR_RLCL) |  |

External Auditor – Accounts Payable and Receivable (FI-CA): Transactions to Check Single Cases

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Business Partner Financial Overview](#unique_21) [page ] 15 | External Auditor - Accounts Payable and Receivable (FI-CA) | Business Partner Financial Overview (F2429) |  |
| [Display Contract Account](#unique_22) [page ] 16 | External Auditor - Accounts Payable and Receivable (FI-CA) | Maintain Contract Account (CAA3) |  |
| [Display Account Balance](#unique_23) [page ] 16 | External Auditor - Accounts Payable and Receivable (FI-CA) |  |  |
| [Display Document](#unique_24) [page ] 17 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Document (FPE3) |  |
| [Display Document Changes](#unique_25) [page ] 17 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Document Changes (FPE4) |  |
| [Display Installment Plan](#unique_26) [page ] 18 | External Auditor - Accounts Payable and Receivable (FI-CA) | Maintain Installment Plan (FPR3) |  |
| [Display Reconciliation Key](#unique_27) [page ] 18 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Reconciliation Key (FPF3) |  |
| [Display Write-Offs](#unique_28) [page ] 19 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Write-Offs (F3125) |  |
| [Display Returns](#unique_29) [page ] 19 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Returns (F3126) |  |
| [Display Dunning History](#unique_30) [page ] 20 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Dunning History (FPM3) |  |
| [Display Dunning Exceptions](#unique_31) [page ] 20 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Dunning Run Exceptions (F7575) |  |
| [Display Interest Calculation](#unique_32) [page ] 20 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Interest Calculations (F4761) |  |
| [Display Installment Plan History](#unique_33) [page ] 21 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Installment Plan History (FPRH) |  |
| [Display Correspondence History](#unique_34) [page ] 21 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Correspondences (F3693) |  |
| [Monitor Payments with Payment Card](#unique_35) [page ] 22 | External Auditor - Accounts Payable and Receivable (FI-CA) | Payment Monitor - With Payment Card (FPCA_MON) |  |
| [Display Payment Card Details](#unique_36) [page ] 22 | External Auditor - Accounts Payable and Receivable (FI-CA) | Display Payment Card Details (FPPCBP) |  |
| [Display Repayment Requests](#unique_37) [page ] 22 | External Auditor - Accounts Payable and Receivable (FI-CA) | Manage Repayment Requests (F5754) |  |
| [Invoicing Overview for Contract Accounts](#unique_38) [page ] 23 | External Auditor - Accounts Payable and Receivable (FI-CA) | Invoicing Overview for Contract Accounts (F2473) |  |
| [Display Invoicing Documents](#unique_39) [page ] 23 | External Auditor - Accounts Payable and Receivable (FI-CA) | Manage Invoicing Documents (F2048) |  |
| [Display Billing Documents](#unique_40) [page ] 24 | External Auditor - Accounts Payable and Receivable (FI-CA) | Manage Billing Documents (F2250) |  |
| [Display Billable Items](#unique_41) [page ] 25 | External Auditor - Accounts Payable and Receivable (FI-CA) | Manage Billable Items (F2621) |  |

Access Type: Indirect System Access

Auditors can also request data analyses from the taxpayer or from third parties according to their legal constraints. In this case, the data is made available by an employee of the company. This can only be done using analysis functions that are already available in the IT system.

Access Type: File Access

In this third type of access, the auditor has no authorization to the system at all. The auditor only receives extracted data in files, which is possible by importing into an audit software designed especially for this audit use cases.

Administrator – Transactions to Extract Documents

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Export Customizing Extracts](#unique_42) [page ] 26 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Extracts (FPDE) |  |
| [Import Customizing Extracts](#unique_43) [page ] 27 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Extracts (FPDE) |  |
| [Export Partner Extracts](#unique_44) [page ] 28 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Extracts (FPDE) |  |
| [Import Partner Extracts](#unique_45) [page ] 30 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Extracts (FPDE) |  |
| [Export Documents Extracts](#unique_46) [page ] 31 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Extracts (FPDE) |  |
| [Import Documents Extracts](#unique_47) [page ] 32 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Extracts (FPDE) |  |
| [Manage Extracts](#unique_48) [page ] 34 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Extracts (FPDE) |  |
| [Delete Customizing Extracts](#unique_49) [page ] 35 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Extracts (FPDE) |  |
| [Delete Document Extracts](#unique_50) [page ] 36 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Extracts (FPDE) |  |
| [Delete Partner Extracts](#unique_51) [page ] 37 | Administrator - Accounts Payable and Receivable (FI-CA) | Manage Extracts (FPDE) |  |
| [Evaluate Extracted Data](#unique_52) [page ] 38 | Administrator - Accounts Payable and Receivable (FI-CA) | Evaluate Exported Extracts (FPDE_EXTR) |  |

Tax Report

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Display Tax Data for Tax Report](#unique_53) [page ] 42 | Accounts Payable and Receivable Accountant (FI-CA) | Display Tax Data for Tax Report (FPTREP1) | Tax data for tax report is displayed. |
| [Transfer Tax Data for Tax Report](#unique_54) [page ] 43 | Administrator - Accounts Payable and Receivable (FI-CA) | Transfer Tax Data for Tax Report (F6189) | Tax records can be transferred. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Access Type: Direct System Access

In this type of direct access, an auditor reviews a particular company code and data the past fiscal year. In following procedures, only the company code is used as selection criteria, since no data may be present in the system for the past year.

#### Display for General Ledger Transfer

Context

In this activity, you display a list with the details for the transfer to General Ledger (G/L).

Procedure

Refer to chapter Display for General Ledger Transfer scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Itemization for General Ledger Documents

Context

In this activity, you display the documents from FI-CA that were transferred to the General Ledger (G/L) as totals records.

Procedure

Refer to chapter Itemization for General Ledger Documents scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Display Posting Totals

Context

In this activity, you display the total records recorded to a reconciliation key.

Procedure

Refer to chapter Display Posting Totals scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Display Itemization for Posting Totals

Context

In this activity, you will display itemization for posting totals.

Procedure

Refer to chapter Display Receivables Adjustments Transferred scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Display Account Assignment for Single Documents

Context

In this activity, you evaluate FI-CA documents posted to a specific object, for example, CO account assignment or commitment item.

Procedure

Refer to chapter Display before Account Assignment scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Check Transfer Status of Reconciliation Key

Context

In this activity, you verify the transfer status of a reconciliation key.

Procedure

Refer to chapter Check Transfer Status of Reconciliation Key scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Check Totals Records

Context

In this activity, you verify that the FI-CA posting totals agree with the totals of the relevant FI-CA documents.

Procedure

Refer to chapter Check Total Records scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Check General Ledger Documents

Context

In this activity, you reconcile G/L and FI-CA by comparing the transferred FI-CA totals records with the documents posted in the general ledger during the transfer.

Procedure

Refer to chapter Check General Ledger Documents scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Determine Gaps in Document Number Range

Context

In this activity, you create a list of all missing document numbers in a company code, resulting from postings to other company codes.

Procedure

Refer to chapter Determine Gaps in Document Number Ranges scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Display Receivables Adjustments Transferred

Context

In this activity, you can display the adjusted receivables for the selection criteria entered.

Procedure

Refer to chapter Display Receivables Adjustments Transferred scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Display Foreign Currency Valuation

Context

In this activity, you can display foreign currency valuations that have been carried out or reversed.

Procedure

Refer to chapter Display Foreign Currency Valuation scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Itemization of Clarification Accounts - Returns

Context

In this process, you can explain the balance of a clarification account on any specific key date by the returns lot items to be clarified. For the test, you need a returns lot with the status Postings Incomplete.

Procedure

Refer to chapter Itemization of Clarification Accounts - Returns scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Itemization of Clarification Accounts - Payments

Context

In this process, you can explain the balance of a clarification account on any specific key date by the returns lot items to be clarified. For the test, you need a returns lot with the status Postings Incomplete.

Procedure

Refer to chapter Itemization of Clarification Accounts - Payments scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Document Journal

Context

In this activity, you create a document journal that contains data from the document headers and items of the documents selected. For each item category, it also automatically creates totals per company code and local currency.

Procedure

Refer to chapter Document Journal scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Evaluate Open Items

Context

In this activity, you evaluate open items.

Procedure

Refer to chapter Evaluate Open Items scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Business Partner Financial Overview

Context

In this activity, you evaluate open items.

Procedure

Refer to chapter Business Partner Financial Overview scope item 2BI: Contract Accounting – Customer Initiated Payments.

#### Display Contract Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display a contract account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Contract Account (CAA3). | The Contract Account Display: Initial View displays. |  |
| 3 | Maintain Selection Parameters | Make the following entry:Contract Account: <Contract Account number>Note To display Contract Account based on the Business Partner, also enter: Business Partner: <Business Partner number>. |  |  |
| 4 | Execute | Choose Continue. | Contract Account master data is displayed. |  |

#### Display Account Balance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display an Account Balance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Account Balance (FPL9). | The Account Display: InitScrn view displays. |  |
| 3 | Maintain Selection Parameters | Make the following entries:Business Partner: <Business Partner number>Contract Account: <Contract Account number> |  |  |
| 4 | Execute | Choose Continue. | Account Balance is displayed. |  |

#### Display Document

Context

In this activity, you display a FI-CA document.

Procedure

Refer to chapter Display Document scope item 2BI: Contract Accounting – Customer Initiated Payments.

#### Display Document Changes

Context

In this activity, you display document changes.

Procedure

Refer to chapter Display Document Changes scope item 2BI: Contract Accounting – Customer Initiated Payments.

#### Display Installment Plan

Context

In this activity, you display document changes.

Procedure

Refer to chapter Display Installment Plan scope item 2UJ: Contract Accounting – Open Item Management.

#### Display Reconciliation Key

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display a reconciliation key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Reconciliation Key (FPF3) | The Display Reconciliation Key: InitView view displays. |  |
| 3 | Enter Reconciliation Key | Choose the value help of the Reconciliation Key.Make the following entry:Entered by: keyand choose Start Search. | Details for the reconciliation key display. |  |
| 4 | Execute | Select one and choose Enter. | Details for the reconciliation key are displayed. |  |

#### Display Write-Offs

Context

In this activity, you display Write-Offs.

Procedure

Refer to chapter Display Write-Offs scope item 2BK: Contract Accounting – Daily and Monthly Closing.

#### Display Returns

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display returns.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Returns (F3126) | The Display Returns view displays. |  |
| 3 | Enter Selection Criteria | Enter required parameters for search criteria. |  |  |
| 4 | Execute | Choose Go. | Write-offs are displayed. |  |

#### Display Dunning History

Context

In this activity, you display document changes.

Procedure

Refer to chapter Display Dunning History scope item 2UJ: Contract Accounting – Open Item Management.

#### Display Dunning Exceptions

Context

In this activity, you display document changes.

Procedure

Refer to chapter Display Dunning Exceptions scope item 2UJ: Contract Accounting – Open Item Management.

#### Display Interest Calculation

Context

In this activity, you display document changes.

Procedure

Refer to chapter Display Interest Calculation scope item 2UJ: Contract Accounting – Open Item Management.

#### Display Installment Plan History

Context

In this activity, you display document changes.

Procedure

Refer to chapter Display Installment Plan History scope item 2UJ: Contract Accounting – Open Item Management.

#### Display Correspondence History

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display correspondence history details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Correspondences (F3693). | The Display Correspondence view displays. |  |
| 3 | Search Criteria | Enter required parameters for search criteria. |  |  |
| 4 | Execute | Choose Execute. | The Display Correspondence view displays. The correspondence history details are listed. |  |

#### Monitor Payments with Payment Card

Context

In this activity, payments cards are monitored.

Procedure

Refer to chapter Monitor Payment Cards scope item 2BI: Contract Accounting – Customer Initiated Payments.

#### Display Payment Card Details

Context

In this activity, you display document changes.

Procedure

Refer to chapter Payment Cards: List of Card Data scope item 2BI: Contract Accounting – Customer Initiated Payments.

#### Display Repayment Requests

Context

In this activity, you display document changes.

Procedure

Refer to chapter Overview of Repayment Request scope item 2BI: Contract Accounting – Customer Initiated Payments.

#### Invoicing Overview for Contract Accounts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display an invoicing overview for a contract account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Invoicing Overview for Contract Accounts (F2473). | The Invoicing Overview for Contract Accounts view is displayed. |  |
| 3 | Search Criteria | Enter required parameters for search criteria. |  |  |
| 4 | Execute | Choose Go. | Invoicing documents are listed. |  |
| 5 | Display Overview | Choose the > at the end of a row. | The invoicing overview for the contract account is displayed. |  |

#### Display Invoicing Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display an invoicing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Invoicing Documents (F2048). | The Display Invoicing Documents view is displayed. |  |
| 3 | Search Criteria | Enter required parameters for search criteria. |  |  |
| 4 | Execute | Choose Go. | Invoicing documents are listed. |  |
| 5 | Display Invoicing Document | Choose the > at the end of a row. | The details for the invoice document are displayed. |  |

#### Display Billing Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display a billing document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Billing Documents (F2250). | The Display Billing Documents view displays. |  |
| 3 | Search Criteria | Enter required parameters for search criteria. |  |  |
| 4 | Execute | Choose Go. | Billing documents are listed. |  |
| 5 | Display Billing Document | Choose the > at the end of a row. | The details for the billing document display. |  |

#### Display Billable Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you display billable items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an External Auditor - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Billable Items (F2621). | The Display Billable Items view displays. |  |
| 3 | Search Criteria | Enter required parameters for search criteria. |  |  |
| 4 | Execute | Choose Go. | Billable items are listed. |  |
| 5 | Display Billable Item | Choose the > at the end of a row. | The details for the billable item display. |  |

### Access Type: Indirect System Access

In this type of indirect access, an auditor can request data analyses from the taxpayer or from third parties according to their legal constraints. In this case, the data is made available by an employee of the company. The data is provided to the auditor as a file or a paper.

### Access Type: File Access

#### Export Customizing Extracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note In indirect system access, you may face message as: Period is not closed yet. you can align with G/L account or you can use role General Ledger Accountant to close period. In real business scenarios, customer won’t face such issue. |

Context

In this activity, you export data extracts of customizing data for auditing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Extracts (FPDE). | The view Data Extracts: Overview displays. |  |
| 3 | Choose transaction | Make the following entries:Extract Type: Select FI-CA CustomizingChoose the Export Extract button. | The view Customizing Data Extraction displays. |  |
| 4 | Enter Data | Make the following entries and choose Execute:Extraction ID: <create your own ID>Fiscal Year: <Fiscal Year>Language Key: For example, ENName of file: <name your export file>Check box: Overwrite file.Note The Overwrite file choice means an existing file is deleted and new export file generated. It is optional.Output format: Select the check box for either CSV for SAP import or SAP audit format.Note Only one output format is chosen. CSV includes all data in one file. Audit format generates separate files on customizing, business partner, contact account, and so on. | CSV/Audit file can be generated, you need further down from the browser to your local PC. |  |
| 5 | Execute | Review the output logs and files in a GUI browser.You can download files from the GUI browser to your local PC. | Files are generated. |  |

#### Import Customizing Extracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you import extraction of customizing data for auditing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Extracts (FPDE). | The view Data Extracts: Overview displays. |  |
| 3 | Choose transaction | Make the following entries:Extract Type: Select FI-CA CustomizingChoose button Import Extract | The view Customizing Data Import displays. |  |
| 4 | Enter Data | Make the following entries:Name of the file: < name of the CVS file>Note The file name is the CVS file you created and downloaded in the previous procedure.Unicode Format: optionalImport control: Choose one of the following:New extract: When importing a new file, choose to create the extract.Overwrite: Overwrite when there is an existing file to create new extract.Add: When there is an existing file and you are adding additional entries to import into the existing file. | The view Customizing Data Import displays. |  |
| 5 | Execute | Upload your file by choosing Execute. | File imports and displays log. |  |

#### Export Partner Extracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you export data extracts of a business partner for auditing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Manage Extracts (FPDE). | The view Data Extracts: Overview displays. |  |
| 3 | Choose transaction | Make the following entries:Extract Type: Select FI-CA Business PartnerChoose button Export Extract | The view Business Partner Data Extraction displays. |  |
| 4 | Enter Data | Make the following entries:Extract ID: <Your Extract ID>Fiscal Year: <fiscal year>Business Partner: <Business ID/Interval>Name of file: <Name of extracted file>Overwrite file: Selected by defaultKeep leading zero: OptionalOutput format: Only one choiceCSV for SAP import: <file format>Number of objects: <limit of file size>SAP Audit Format: File from external Audit system, for example, IDEA | Local file generated on you PC local file folder,Or display log show successful. |  |
| 5 | Execute | Review the logs and file. To download file your PC, choose Execute. |  |  |

#### Import Partner Extracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you import an extraction of business partner data for auditing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Extracts (FPDE). | The view Data Extracts: Overview displays. |  |
| 3 | Choose transaction | Make the following entries:Extract Type: Select FI-CA Business PartnerChoose button Import Extract | The view Business Partner Data Import displays. |  |
| 4 | Enter Data | Make the following entries:Name of file: <file name>Note This is the file you created in the previous procedure.Unicode Format: SelectImport Control: Choose one of the following:New extract: When importing a new file, choose to create the extract.Overwrite: Overwrite when there is an existing file to create new extract.Add: When there is an existing file and you are adding additional entries to import into the existing file. |  |  |
| 5 | Execution | You make final changes to the file in your PC and upload to the GUI browser and choose Execute. | File imports and logs display. |  |

#### Export Documents Extracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you export data extracts of documents for auditing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Extracts (FPDE). | The view Data Extracts: Overview displays. |  |
| 3 | Choose transaction | Make the following entries:Extract Type: FI-CA DocumentChoose button Export Extract | The view FI-CA Documents Data Extraction displays. |  |
| 4 | Enter Data | Make the following entries:Extract ID: Your extract IDDocument selection:Posting date: From toNote The To date is earlier than today.Company code: <your company code>Checkbox: optionalAlso, select SD document: optionalAlso, select Industry Data: optionalName of file: <name of file to be exported>Overwrite file: <select>Keep leading zeros: optionalOutput format: Choose only one, either CSV or audit format.CSV for SAP import: CSV file downloadNumber of object: optional, size of fileSAP audit format: optional | Local file generated to your local file folder or success message displays for log. |  |
| 5 | Execute | Local file imports from local PC, logs display. | Review logs and file in GUI browser. |  |
| 6 | Choose Back | If you want to import invoicing document, choose Back twice. | The view Data Extracts: Overview displays. |  |
| 7 | Choose transaction | Make the following entries:Extract Type: FI-CA-INV Invoicing DocumentChoose Import Extract. | The view Data Import Invoicing Documents Extract displays. |  |
| 8 | Enter Data | Make the following entries:Extract ID: Your extract IDDocument selection:Invoicing Document: <your document number>Name of file: <name of file to be exported>Overwrite file: selectKeep leading zeros: optionalOutput format: Choose only one, either File of SAP Import or SAP Audit Format. | Local file generated to your local file folder or success message displays for log. |  |
| 9 | Execute | Choose Execute (F8). Local file exports to local PC, logs display. | Review logs and file in GUI browser. |  |

#### Import Documents Extracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you import extractions of documents for auditing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Extracts (FPDE). | The view Data Extracts: Overview displays. |  |
| 3 | Choose transaction | Make the following entries:Extract Type: Select FI-CA DocumentChoose button Import Extract | The view FI-CA Documents Data Import displays. |  |
| 4 | Enter Data | Make the following entries:Name of the file: <file name>Note The file name is the file you created in the previous procedure.Unicode Format: No to the checkboxImport control: Choose one of the following:New extract: When importing a new file, choose to create the extract.Overwrite: Overwrite when there is an existing file to create new extract.Add: When there is an existing file and you are adding additional entries to import into the existing file.Update clearing data: optional |  |  |
| 5 | Execution | Choose Execute. | Local file imports from local PC and logs display success. |  |
| 6 | Choose Back | If you want to import invoicing document, choose Back twice. | The view Data Extracts: Overview displays. |  |
| 7 | Choose transaction | Make the following entries:Extract Type: FI-CA-INV Invoicing DocumentChoose Import Extract. | The view Data Import Invoicing Documents Extract displays. |  |
| 8 | Enter Data | Make the following entries:Name of file: <name of file to be imported>Note The file name is the file you created in the previous procedure.Unicode Format: No to the checkboxImport control: Choose one of the following:New extract: When importing a new file, choose to create the extract.Overwrite: Overwrite when there is an existing file to create new extract.Add: When there is an existing file and you are adding additional entries to import into the existing file. | Local file generated to your local file folder or success message displays for log. |  |
| 9 | Execute | Choose Execute (F8). | Local file imports from local PC and logs display success. |  |

#### Manage Extracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display an overviews of extract IDs and logs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Manage Extracts (FPDE). | The Data Extracts Overview: Initial Screen displays. |  |
| 3 | Enter Data | Make the following entries:Extract type: Select one of the following:FI-CA Business partnerFI-CA CustomizingFI-CA DocumentFI-CA-INV Invoicing Document | After execution, result will show log with your Extract ID |  |
| 4 | Review and Export | After selecting the Extract type, the Extract ID displays with information on posting date, company code, currency logical system, and so on. | The Extract ID displays. |  |

#### Delete Customizing Extracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you delete the extract for customizing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Manage Extracts (FPDE). | The view Business Partner Data Import displays. |  |
| 3 | Choose transaction | Make the following entries:Extract Type: Select FI-CA CustomizingChoose button Delete Extract | The view Deletion of Partner Extract from Database displays. |  |
| 4 | Enter Data | Make the following entry:Extract ID: <ID for customizing extract> | After execution, result displays log with Extract ID. |  |
| 5 | Execute | Choose Execute. | Customizing data for Extract ID deleted. |  |

#### Delete Document Extracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you delete document extracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Manage Extracts (FPDE). | The view Data Extracts: Overview displays. |  |
| 3 | Choose transaction | Make the following entries:Extract Type: Select FI-CA DocumentsChoose button Delete Extract | The view Deletion of Partner Extract from Database displays. |  |
| 4 | Enter Data | Make the following entries:Extract ID: <ID for customizing extract> | After execution, result displays log with Extract ID. |  |
| 5 | Execute | Choose Execute. | Customizing data for Extract ID deleted. |  |
| 6 | Choose transaction | To delete extract type FI-CA-INV Invoicing Document, repeat steps 3 – 5 with Extract Type FI-CA-INV Invoicing Document. | Invoicing document for Extract ID is deleted. |  |

#### Delete Partner Extracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you delete data extracts for partners.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Manage Extracts (FPDE). | The view Data Extracts: Overview displays. |  |
| 3 | Choose transaction | Make the following entries:Extract Type: Select FI-CA Business PartnerChoose button Delete Extract | The view Deletion of Partner Extract from Database displays. |  |
| 4 | Enter Data | Make the following entry:Extract ID: <Enter the ID for partner data> | After execution, result displays log with your Extract ID. |  |
| 5 | Execute | Choose Execute. | Partner data for Extract ID deleted. |  |

#### Evaluate Extracted Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you export the data you have extracted to a file for the external auditor. He can then importing this into an audit software designed especially for audit use cases.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Evaluate Exported Extracts (FPDE_EXTR). | The FI-CA Data Extracts: Export of Extract Entries: Initial Screen displays. |  |
| 3 | Enter Data | Make the following entries:Fiscal Year: <fiscal year>Business Partner: <Business ID/Interval>Company code: <your company code>Posting date: From toNote The To date is earlier than today.Object Key: choose on after the otherFI-CA Business partnerFI-CA CustomizingFI-CA DocumentOutput format: Choose File (SAP Audit Format)Output to File:Name of file: <name of file to be exported>Local file: <select>Overwrite file: <select> | Local file generated to your local file folder or success message displays for log. |  |
| 4 | Execute | Local files are created. | Review logs and file in GUI browser. |  |

### Tax Report

Prerequisite

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

1. Active Recording of Tax Data

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Configure Basic Settings | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Tax Reporting.Choose the configuration step Activate Recording of Tax Data.Choose Activate Recording of Tax Data.Choose New Entries.Choose Use Shadow Table. | The Change View screen is displayed. |  |

SAP Central Business Configuration:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Assign Semantic Tags to Financial Statement Versions | Go to the Business Processes Configuration app and search for the following activity: Activate Recording of Tax Data.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Activate Recording of Tax Data": screen is displayed. |  |
| 3 | Choose Entries | Choose Activate Recording of Tax Data.Choose New Entries.Choose Use Shadow Table.Save the entry. |  |  |

1. Define Report Times for Sales/Purchase Tax

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Configure Basic Settings | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingChoose the group Tax Reporting.Choose the configuration step Define Report Times for Sales/Purchase Tax.Company Code: 3310Tax code: <Select tax code>Tax Item Type: *Report Time: Report for Clearing dateData scope: Proportional Report with Partial PaymentSingle Record: <Checked>Rule: <blank>Details: Business partner level | The Change View screen is displayed. |  |

SAP Central Business Configuration:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Assign Semantic Tags to Financial Statement Versions | Go to the Business Processes Configuration app and search for the following activity: Define Report Times for Sales/Purchase Tax.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Define Report Times for Sales/Purchase Tax": screen is displayed. |  |
| 3 | Input Entries | Company Code: 3310Tax code: <Select tax code>Tax Item Type: *Report Time: Report for Clearing dateData scope: Proportional Report with Partial PaymentSingle Record: <Checked>Rule: <blank>Details: Business partner levelSave the entry. |  |  |

#### Display Tax Data for Tax Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In some countries, there is a legal requirement for tax reporting that tax returns must contain detailed information at document level. The relevant tax authority determines what document information a company has to display in its tax return.

Prerequisite

1. Post a document.
2. Clear this document with total amount or partially using app Payment Run (refer to the chapter Execute Payment Run in 2BI Contract Accounting – Customer Initiated Payments) or Process Payment Lot (refer to the chapter Payment Lot in 2DP Contract Accounting – Company Initiated Payments).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Tax Data for Tax Report (FPTREP1). | The Display Data of Generic Tax Reporting screen is displayed. |  |
| 3 | Input Parameters | Make the following entries:Reporting period: <Choose period>Company Code: 3310 |  |  |
| 4 | Execute | Choose Execute. | The Display Data of Generic Tax Reporting screen is displayed. The tax history details are listed. |  |

#### Transfer Tax Data for Tax Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this step, you transfer tax records by using the generic tax reporting tool.

Prerequisite

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. In SSCUI (105595) Define Report Times for Sales/Purchase Tax, change Report Time: Report for clearing date, for the due date at the latest.
2. Post a document with net due data in the past.
3. Clear this document with total amount or partially using app Payment Run (refer to the chapter Execute Payment Run in 2BI Contract Accounting – Customer Initiated Payments) or Process Payment Lot (refer to the chapter Payment Lot in 2DP Contract Accounting – Company Initiated Payments).

Procedure

After implementing this procedure, you can view tax report via app Display Tax Data for Tax Report (FPTREP1).

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Transfer Tax Data for Tax Report (F6189). | The Application Jobs screen is displayed. |  |
| 3 | Choose Create | On the Application Jobs screen, choose Create. | Screen 1. Template Selection displays. |  |
| 4 | Choose Step 2 | ChooseJob Template: Transfer Tax Data for Tax ReportJob Name: Transfer Tax Data for Tax ReportChoose Step 2. | Screen 2. Scheduling Options displays. |  |
| 5 | Choose Step 3 | Start Immediately: <Selected>Choose Step 3. | Screen 3. Steps displays. |  |
| 6 | Enter Basic Parameters | Make the following entries:Reporting Date: <Choose a date>Company Code: 3310Update run: <Selected> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Indirect system access is described inconsistently: Purpose says the administrator exports productive data into reduced-field short-tables that the auditor displays, while Overview Table and Test Procedures say the auditor requests analyses and an employee provides data as a file or paper; no test steps are given for it.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[04-tax-and-statutory-reporting/test-script-external-tax-audit-2oo-ae-sap-s-4hana-cloud-public-edition]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2SJ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 68,019 chars in the whole document
