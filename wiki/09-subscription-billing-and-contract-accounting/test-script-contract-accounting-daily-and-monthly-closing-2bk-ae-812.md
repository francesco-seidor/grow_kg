---
id: 09-subscription-billing-and-contract-accounting/test-script-contract-accounting-daily-and-monthly-closing-2bk-ae-812
title: "Test Script: Contract Accounting – Daily and Monthly Closing (2BK_AE) (2BK_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (scope item 2BK, UAE/AED) for FI-CA day-end and month-end closing: value adjustments, write-offs, FX valuation, reclassification, G/L reconciliation."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-closing-and-valuation]
aliases: [2BK_S4CLD2608_BPD_EN_AE]
keywords: [Contract Accounting Closing and Valuation, doubtful receivables, value adjustments, write-offs, foreign currency valuation, reclassifications, day-end closing, month-end closing, reconciliation keys, general ledger transfer]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BK_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-812
topic: 09-subscription-billing-and-contract-accounting/fi-ca-closing-and-valuation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Contract Accounting – Daily and Monthly Closing (2BK_AE) (2BK_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BK_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Contract Accounting Closing and Valuation** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract Accounting – Daily and Monthly Closing (2BK_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232849135)

[2 Prerequisites 5](#_Toc232849136)

[2.1 System Access 5](#_Toc232849137)

[2.2 Roles 5](#_Toc232849138)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232849139)

[2.4 Business Conditions 7](#_Toc232849140)

[2.5 Preliminary Step 7](#_Toc232849141)

[2.5.1 Post Documents 7](#_Toc232849142)

[3 Overview Table 10](#_Toc232849143)

[4 Test Procedures 13](#_Toc232849144)

[4.1 Doubtful Receivables 13](#_Toc232849145)

[4.1.1 Create Flat-Rate Value Adjustments According to Expected Credit Loss Rates 13](#_Toc232849146)

[4.1.2 Create Doubtful Receivables and Individual Value Adjustments 18](#_Toc232849147)

[4.1.3 Create Doubtful Receivables and Individual Value Adjustments According to Age 20](#_Toc232849148)

[4.1.4 Post Value Adjustments 22](#_Toc232849149)

[4.1.5 Display Value Adjustments 23](#_Toc232849150)

[4.1.6 Transfer Value Adjustments 24](#_Toc232849151)

[4.1.7 Analyze Credit Loss Allowances 26](#_Toc232849152)

[4.2 Write-Offs 27](#_Toc232849153)

[4.2.1 Write Off Items 27](#_Toc232849154)

[4.2.2 Write Off Items - Mass Run 28](#_Toc232849155)

[4.2.3 Display Write-Offs 30](#_Toc232849156)

[4.3 Foreign Currency Valuation 31](#_Toc232849157)

[4.3.1 Foreign Currency Valuation 31](#_Toc232849158)

[4.3.2 Display Foreign Currency Valuation 33](#_Toc232849159)

[4.3.3 Deferred Inverse Posting for Foreign Currency Valuation 34](#_Toc232849160)

[4.3.4 Clear Foreign Currency Document (Optional) 38](#_Toc232849161)

[4.3.5 Clear Foreign Currency Document in Value Adjustment (Optional) 40](#_Toc232849162)

[4.4 Reclassifications 42](#_Toc232849163)

[4.4.1 Create Open Item Lists for Reclassifications 42](#_Toc232849164)

[4.4.2 Post Reclassifications 44](#_Toc232849165)

[4.4.3 Create Open Item Lists for Reclassifications by Due Date 45](#_Toc232849166)

[4.4.4 Post Reclassifications by Due Date 47](#_Toc232849167)

[4.5 Day-End Closing 48](#_Toc232849168)

[4.5.1 Close Reconciliation Keys 48](#_Toc232849169)

[4.5.2 Transfer FI-CA Total Records to General Ledger 49](#_Toc232849170)

[4.6 Month-End Closing 50](#_Toc232849171)

[4.6.1 Close Previous Accounting Period 50](#_Toc232849172)

[4.6.2 Reconcile Open Items with G/L 51](#_Toc232849173)

[5 Appendix 53](#_Toc232849174)

[5.1 Process Integration 53](#_Toc232849175)

[5.1.1 Preparation and Execution 53](#_Toc232849176)

[5.1.1.1 Change Reconciliation Key 53](#_Toc232849177)

[5.1.1.2 Manage Reconciliation Key 54](#_Toc232849178)

[5.1.1.3 Display Itemization for Posting Totals 55](#_Toc232849179)

[5.1.1.4 Display Posting Totals 56](#_Toc232849180)

[5.1.2 Forward Postings 56](#_Toc232849181)

[5.1.2.1 Preparation and Execution 56](#_Toc232849182)

[5.1.2.1.1 Assign New Reconciliation Key to Returns Lot 56](#_Toc232849183)

[5.1.2.1.2 Assign New Reconciliation Key for Payment Lot 57](#_Toc232849184)

[5.1.2.1.3 Maintain Alternative Posting Date 58](#_Toc232849185)

[5.1.2.1.4 Transfer to General Ledger - Mass Run 58](#_Toc232849186)

[5.1.2.1.5 Reverse General Ledger Transfer 60](#_Toc232849187)

[5.1.2.2 Direct Posting to General Ledger 60](#_Toc232849188)

[5.1.2.2.1 Post Document 62](#_Toc232849189)

[5.1.2.2.2 Display Document 63](#_Toc232849190)

[5.1.2.3 Reconciliation 64](#_Toc232849191)

[5.1.2.3.1 Display General Ledger Transfer 64](#_Toc232849192)

[5.1.2.3.2 Itemization for General Ledger Documents 65](#_Toc232849193)

[5.1.2.3.3 Display Account Assignment for Single Documents 65](#_Toc232849194)

[5.1.2.4 Checks 66](#_Toc232849195)

[5.1.2.4.1 Check Transfer Status of Reconciliation Key 66](#_Toc232849196)

[5.1.2.4.2 Check Totals Records 67](#_Toc232849197)

[5.1.2.4.3 Check General Ledger Documents 68](#_Toc232849198)

[5.1.2.4.4 Determine Gaps in Document Number Ranges 68](#_Toc232849199)

[5.1.2.4.5 Reconcile Postings - Mass Runs 69](#_Toc232849200)

[5.1.3 Closing Preparation 71](#_Toc232849201)

[5.1.3.1 Evaluate Installment Plans for Key Date 71](#_Toc232849202)

[5.1.3.2 Create Open Item List for Key Date 72](#_Toc232849203)

[5.1.3.3 Display Saved Open Item List 77](#_Toc232849204)

[5.1.3.4 Itemization of Clarification Accounts - Returns 78](#_Toc232849205)

[5.1.3.5 Itemization of Clarification Accounts - Payments 78](#_Toc232849206)

[5.1.3.6 Document Journal 79](#_Toc232849207)

[5.1.3.7 Display G/L Line Items 79](#_Toc232849208)

[5.1.3.8 Evaluate Open Item 80](#_Toc232849209)

[5.1.3.9 Display Installment Plan Evaluation for Key Date 81](#_Toc232849210)

[5.1.3.10 Delete Installment Plan Evaluation for Key Date 81](#_Toc232849211)

[5.1.4 Flexible Workflow for Document Write-Off 82](#_Toc232849212)

[5.1.4.1 Write Off Open Items 87](#_Toc232849213)

[5.1.4.2 Verify Document 87](#_Toc232849214)

[5.1.4.3 Approve Document Write Off (for Processor - Inbox) 88](#_Toc232849215)

[5.1.4.4 Reject Document Write Off (for Processor - Inbox) 89](#_Toc232849216)

## Purpose

Overview

Daily and monthly closing allows you to prepare and carry out the activities required for day-end and month-end closing for Contract Accounts Receivable and Payable (FI-CA). The major activity for closing is the reconciliation between Contract Accounts Receivable and Payable and General Ledger (FI-GL). In addition, you can write off uncollectible receivables in Contract Accounts Receivable and Payable (FI-CA).

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |
| Administrator - Accounts Payable and Receivable (FI-CA) | SAP_BR_ADMIN_APR_FICA | Contract Accounting - Jobs | SAP_BR_ADMIN_APR_FICA |  |
| Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | SAP_BR_RECONC_SPEC_APR_FICA | Contract Accounting - Reconciliation | SAP_BR_RECONC_SPEC_APR_FICA |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  | Company code |
| Posting Period Variant | 3310 |  |  |
| Fiscal Year Variant | K4 |  |  |
| Account Type | V (Contract accounts) |  |  |

Table 1: Other Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Business Partner | BP_AE_99 |  |  |
| Contract Account | CA_AE_99 |  |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2AR - Contract Accounting – Master Data and Basic Functions | Must be run before this test script. Contract partner and contract account have been created for posting. |
| 2BI - Contract Accounting – Customer Initiated Payments | Invoices have been created for posting. |
| 2DP - Contract Accounting – Company Initiated Payments | Credit Memos have been created for posting. |

### Preliminary Step

#### Post Documents

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen is displayed. |  |
| 3 | Enter Data | Make the following entries:Document Date: <today’s date>Posting Date: <today’s date>Document Type: YACurrency: AEDReconcil. Key: <reconciliation key generated by system>BP Item: Y01G/L Item: Y01Taxes Calculate Automatically: SelectTax Jurisdiction: Select |  |  |
| 4 | Enter BP Item | Choose New BP Item. | The Checking reconciliation key screen appears.If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to Step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen is displayed. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section:Bus. Partner: <Business Partner number with MKK BP Role>Contract Acct: <Contract Account number related to the selected BP>Contract: <fill in Provider Contract number, which is optional>If the document has contract, you also need to fill in the Contract Item field.Company Code: 3310Transac.: Y600/0020Note Use Transaction: Y600/0010 to post credit open items.In the Amounts and Due Date section:Net Due Date: <input net due date>Amount: <input amount> |  |  |
| 8 | Post | Choose Post. | The FI-CA document is posted. |  |

## Overview Table

This Monthly and Daily Closing scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Doubtful Receivables

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Flat-Rate Value Adjustments According to Expected Credit Loss Rates](#unique_10) [page ] 13 | Administrator - Accounts Payable and Receivable (FI-CA) | Adjust Receivables According To Age (F3535) | Receivables are automatically set to doubtful and flat rate value adjustments are made on the basis of their age. |
| [Create Doubtful Receivables and Individual Value Adjustments](#unique_11) [page ] 18 | Accounts Payable and Receivable Accountant (FI-CA) | Adjust Receivables (FPZW) | The selected receivables are marked as doubtful and individual value adjustments are done. |
| [Create Doubtful Receivables and Individual Value Adjustments According to Age](#unique_12) [page ] 20 | Administrator - Accounts Payable and Receivable (FI-CA) | Adjust Receivables According To Age (F3535) | Receivables are automatically set to doubtful and individual value adjustments are made on the basis of their age. |
| [Post Value Adjustments](#unique_13) [page ] 22 | Administrator - Accounts Payable and Receivable (FI-CA) | Post Value Adjustments (F3539) | Adjusted and doubtful receivables are transferred cumulative in the general ledger. |
| [Display Value Adjustments](#unique_14) [page ] 23 | Accounts Payable and Receivable Accountant (FI-CA) | Display Posted Value Adjustments (F4824) | The transferred receivables adjustments can be displayed. |
| [Transfer Value Adjustments](#unique_15) [page ] 24 | Administrator - Accounts Payable and Receivable (FI-CA) | Prepare Value Adjustment Analysis (FPRT) | Transfer Value Adjustments from Contract Accounting to General Ledger for the Credit Loss Allowance Analysis preparation. |
| [Analyze Credit Loss Allowances](#unique_16) [page ] 26 | General Ledger Accountant | Analyze Credit Loss Allowances (W0134) | Analyze credit loss allowances. |

Table 3: Write-Off

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Write Off Items](#unique_17) [page ] 27 | Accounts Payable and Receivable Accountant (FI-CA) | Write Off Items (FP04) | The selected documents are written off. |
| [Write Off Items - Mass Run](#unique_18) [page ] 28 | Administrator - Accounts Payable and Receivable (FI-CA) | Write Off Run (F3540) | The selected documents are written off using the mass run. |
| [Display Write-Offs](#unique_19) [page ] 30 | Accounts Payable and Receivable Accountant (FI-CA) | Display Write-Offs (F3125) | The written off documents can be displayed. |

Table 4: Foreign Currency Valuation

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Foreign Currency Valuation](#unique_20) [page ] 31 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Execute Foreign Currency Valuation (FPW1) | Valuate foreign currencies in contract accounts with the aim of adjusting the receivable and payable accounts as part of balance sheet preparations |
| [Display Foreign Currency Valuation](#unique_21) [page ] 33 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Display Foreign Currency Valuations (FPW2) | Display foreign currency valuations that have been carried out or reversed. |
| [Deferred Inverse Posting for Foreign Currency Valuation](#unique_22) [page ] 34 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Deferred Inverse Posting (FPW3) | Deferred inverse posting for Foreign Currency Valuation. |
| [Clear Foreign Currency Document (Optional)](#unique_23) [page ] 38 |  |  |  |
| [Clear Foreign Currency Document in Value Adjustment (Optional)](#unique_24) [page ] 40 |  |  |  |

Table 5: Reclassifications

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Open Item Lists for Reclassifications](#unique_25) [page ] 42 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Creation Run Open Item List for Key Date (F3538) | Closing balance of selected open items are reclassified. |
| [Post Reclassifications](#unique_26) [page ] 44 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Post Reclassifications (FPRECL) | Display reclassification document. |
| [Create Open Item Lists for Reclassifications by Due Date](#unique_27) [page ] 45 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Creation Run Open Item List for Key Date (F3538) | Closing balance of selected open items are reclassified by due dates. |
| [Post Reclassifications by Due Date](#unique_28) [page ] 47 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Post Reclassifications by Due Date (FPRECL_DUEGRID) | Display reclassification document generated by due date. |

Table 6: Day-End Closing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Close Reconciliation Keys](#unique_29) [page ] 48 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Delete and Close Reconciliation Key (FPG4) | The selected reconciliation keys are closed. |
| [Transfer FI-CA Total Records to General Ledger](#unique_30) [page ] 49 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Transfer Total Records to G/L (FPG1) | FI-CA total records are transferred to the General Ledger. |

Table 7: Month-End Closing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Close Previous Accounting Period](#unique_31) [page ] 50 | General Ledger Accountant | Manage Posting Periods (F2293) | The previous accounting period is closed. |
| [Reconcile Open Items with G/L](#unique_32) [page ] 51 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Reconcile Open Items with G/L (FPO2) | Contract Accounts Receivable and Payable are reconciled with the General Ledger. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Doubtful Receivables

Prerequisite

Transfer value adjustments from Contract Accounting to General Ledger for the Credit Loss Allowance Analysis (step Transfer Value Adjustment and Analyze Credit Loss Allowances), calculation type needs to be set as 09 for specific valuation area via configuration activity: Define Valuation Areas for Receivables Adjustments (102194).

#### Create Flat-Rate Value Adjustments According to Expected Credit Loss Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can perform a flat-rate value adjustment on all receivables — both due and not yet due — based on their risk class and age grid through a mass processing run.

|  |
| --- |
| Note You have to maintain risk class for business partner. |

Prerequisites

1. To maintain Risk Class (for example, C Medium Default Risk) for business partner, refer to test script of scope item 2AR Contract Accounting – Master Data and Basic Functions, chapter Create a Business Partner.
2. To note down the Semantic Tag, access configuration activity via: Finance > General Ledger > Ledgers and Valuation > Define Rules for Impairment (105452).

Select the Valuation Rule under Define Rules for Impairment, double-click the folder Define Steps of an Impairment Rule and then select the Valuation Rule Step. Next, double-click the folder Assign Semantic Tag to Impairment Rule and note down the Semantic Tag in the Filter Condition column.

1. To maintain the Probability of Default, access configuration activity via: Finance > General Ledger > Ledgers and Valuation > Define Rules for Impairment (105452).

Select the Valuation Rule under Define Rules for Impairment, double-click the folder Define Steps of an Impairment Rule and then select the Valuation Rule Step. Next, double-click the folder Assign Probability of Default to Aging Increment and maintain the Probability of Default.

1. To note down Financial Statement Versions (for example, corresponding financial statement version) with corresponding Accounting Principle (for example, corresponding accounting principle), access configuration activity via: Finance > General Ledger > Chart of Accounts > Assign Financial Statement Versions to Accounting Principles (103215) .
2. To assign Valuation Rule (for example, SCRI) to the corresponding Accounting Principle, access configuration activity via: Finance > General Ledger > Assign Rules for Impairment to Accounting Principles (105453) .
3. To assign GL account to Financial Statement Version, access configuration activity via: Finance > General Ledger > Chart of Accounts > Define Financial Statement Versions (102669) .
4. To assign Account (for example, 12100200) under Semantic Tag (for example, ACCREC), access configuration activity via: Finance > General Ledger > Chart of Accounts > Assign Semantic Tags to Financial Statement Versions (102659) .

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Rules for Impairment | Search with following criteria:Application Area: FinanceSub Application Area: General LedgerFor the row with Item Name of Ledgers and Valuation, choose Details (>).For the Define Rules for Impairment row, choose Configure. | The Change View "Define Rules for Impairment": Overview screen is displayed. |  |
| 4 |  | Select the Valuation Rule and double-click the folder Define Steps of an Impairement Rule.Make the following entries:Valuation Rule: SCRIValuation Rule Step: 0010 |  |  |
| 5 | Maintain Entries on Assign Probability of Default to Aging Increment | Maintain the Probability of Default.Double-click the folder Assign Probability of Default to Aging Increment.Maintain entries in the Probability of Default to Aging Increment section for each combination of aging increment and risk class.For example,Aging Increment: Overdue < 30 DaysRisk Class: C Medium Default RiskProbability of Default 5%Save the entry. | The Change View "Assign Probability of Default to Aging Increment": Overview screen is displayed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Rules for Impairment | Go to the Business Processes Configuration app and search for the following activity: Define Rules for Impairment.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Define Rules for Impairment": Overview screen is displayed. |  |
| 3 | Input Parameters | Make the following entries:Valuation Rule: SCRIValuation Rule Step: 0010 |  |  |
| 4 | Maintain Entries on Assign Probability of Default to Aging Increment | Double-click the folder Assign Probability of Default to Aging Increment.Maintain entries in the Assign Probability of Default to Aging Increment section for each combination of risk class and aging increment.For example,Aging Increment: Overdue < 30 DaysRisk Class: C Medium Default RiskProbability of Default 5%Save the entry. |  |  |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access SSCUI Assign Semantic Tags to Financial Statement Versions | Search with following criteria:Application Area: FinanceSub Application Area: General LedgerFor the row with Item Name of Chart of Accounts, choose Details (>).For the Assign Semantic Tags to Financial Statement Versions row, choose Configure. | The Change View "Mapping of Financial Statement Version to S..": Overview screen is displayed. |  |
| 4 | Add New Entries | Choose New Entries and select Assign Semantic Tags to G/L account.FS Version: <Corresponding financial statement version>Account From: 12100200Semantic Tag: ACCRECSave the entry. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Semantic Tags to Financial Statement Versions | Go to the Business Processes Configuration app and search for the following activity: Assign Semantic Tags to Financial Statement Versions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Mapping of Financial Statement Version to S..": Overview screen is displayed. |  |
| 3 | Add New Entries | Choose New Entries and select Assign Semantic Tags for G/L account.Choose an assignment type.FS Version: <Corresponding financial statement version>Account From: 12100200Semantic Tag: ACCRECSave the entry. |  |  |

1. Before executing the procedure below, make sure the open item is overdue < 30 days (see Preliminary Step > [Post Documents](#unique_8) [page ] 7).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Adjust Receivables According To Age (F3535). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Adjust Receivables by AgeJob Name: FI-CA: Adjust Receivables by Age |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Basic Parameters | Make the following entries:In the Run Identification section:Prefix of Run ID: For example, ID0Simulation Run: UnselectIn the General Selections section:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310In the Selection type section:Open Items: SelectIn the Date section:Selection Date: <last day of the month>Posting Date: <last day of the month>Note If Transfer Value Adjustment will be executed, set Posting Date as the last day of fiscal period.In the Value Adjustment Reason section:Adjustment reason: 01In the Value Adjustment Variant section:Valuation Area: SAEFlat-Rate Value Adjustment: SelectNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Create Doubtful Receivables and Individual Value Adjustments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can classify receivables as doubtful or make individual value adjustments.

You can adjust the value in one of the following ways:

- Using a percentage rate that you can define as needed
- Using a specified adjustment amount

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Adjust Receivables (FPZW). | Adjust Receivables: Initial Screen is displayed. |  |
| 3 | Enter Selection Details | Business Partner: <Business Partner number with open items>Contract Account: <Contract Account number with open items>Currency: AED |  |  |
| 4 | Enter Valuation Area | Valuation Area: SAE |  |  |
| 5 | Make Correction | Choose Make Correction. | The Adjust Receivables: Execute screen is displayed. |  |
| 6 | Select Open Items | Select the open item in the Open Items section. |  |  |
| 7 | Execute | Execute Individual Value Adjustment. | The Adjust Receivables: Execute screen is displayed. |  |
| 8 | Maintain Value | Modify Reason or IVA Percentage Rate as required. |  |  |
| 9 | Save | Execute Save |  |  |

#### Create Doubtful Receivables and Individual Value Adjustments According to Age

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, receivables can be automatically marked as doubtful, and individual value adjustments can be applied based on their age through a mass processing run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Adjust Receivables According To Age (F3535). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Adjust Receivables by AgeJob Name: FI-CA: Adjust Receivables by Age |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Identification section:Run ID Prefix: <for example, ID0>Simulation: UnselectIn the General Selections section:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310In the Selection type section, for example, select Open Items.In the Date section:Selection Date: <last day of the month>Posting Date: <last day of the month>Note If Transfer Value Adjustment will be executed, set Posting Date as the last day of fiscal period.In the Value Adjustment Reasons section:Adjustment reason: 01In the Value Adjustment Variant section:Value adj. vari: S001Valuation Area: SAEChoose the Ind.Val.Adj.Var radio button.Note The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Post Value Adjustments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This mass activity enables you to post cumulative adjusted and doubtful receivables.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Post Value Adjustments (F3539). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Repost Corrected ReceivablesJob Name: FI-CA: Repost Corrected Receivables |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Basic Parameters | Make the following entries:In the Run Identification section:Prefix of Run ID: <for example, ID0>Simulation Run: UnselectIn the General Selections section:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: <Company Code>Valuation Area: SAEPosting and Selection Date: <last day of the month>Note If Transfer Value Adjustment will be executed, set the last day of fiscal period as Posting Date.Document Date: <last day of the month>In the Create Transfer Posting Docs for section:Doubtful Entry: SelectIndividual Value Adjustment: UnselectFlat-Rate Value Adjustment: SelectNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the Recurring run for Mass activity for your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, navigate to the new application job by choosing the information icon. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Display Value Adjustments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can view the receivables that have been adjusted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access App | Open Display Posted Value Adjustments (F4824). | The screen Display Receivables Adjustments Transferred is displayed. |  |
| 3 | Enter Search Criteria | Make the following entry:Key Date: <select a date>Valuation Area: SAE |  |  |
| 4 | Display | Choose Go. | The screen Display Receivables Adjustments Transferred is displayed. The adjusted receivables are listed. |  |

#### Transfer Value Adjustments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can transfer value adjustments from Contract Accounting to the General Ledger to prepare for the Credit Loss Allowance Analysis.

|  |
| --- |
| Note To transfer Individual Value Adjustments, the calculation type should be set to 09 for the specific valuation area. This can be done through the configuration activity: Define Valuation Areas for Receivables Adjustments (102194). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Prepare Value Adjustment Analysis (FPRT). |  |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Transfer Value AdjustmentJob Name: FI-CA: Transfer Value Adjustment |  |  |
| 5 | Enter Basic Parameters | Start Immediately: SelectChoose Step 3. |  |  |
| 6 | Enter Basic Parameters | Make the following entries:In the Run Identification section:Prefix of Run ID: For example, ID0Simulation Run: UnselectIn the General Selections section:Business Partner: <Business Partner number>Company Code: <Company Code>Key Date: <for example, last day of current month>Valuation Area: SAE |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, navigate to the new application job by choosing the information icon. | The Job Log screen is displayed. The log should show no errors. |  |

#### Analyze Credit Loss Allowances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can analyze the reconciliation of loss allowance for receivables in Contract Accounting, tracking changes from opening to closing balances. The following procedure outlines the period's changes using a simplified Expected Credit Loss model.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as General Ledger Accountant role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Analyze Credit Loss Allowances (W0134). | The Application Jobs screen is displayed. |  |
| 3 | Enter Details | Make the following entries and choose Go:Ledger: 0L for leading ledger with local GAAPCompany Code: 3310Fiscal Year: <select fiscal year>To Period: <select period>Currency Type: <select currency type> | The credit loss allowance is shown. |  |

### Write-Offs

#### Write Off Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can write off open receivables and credits of a business partner.

Prerequisite

Before executing this step, you need to create open document first (refer to Preliminary Step - [Post Documents](#unique_8) [page ] 7).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Write Off Items (FP04). | The Write Off Items screen is displayed. |  |
| 3 | Enter Selection details | Make the following entry:Business Partner: <business partner number with open items>Contract Account: <contract account number with open items>Document Number: <document with open items> |  |  |
| 4 | Enter Specifications for Write-Off | Make the following entry:Document Date: <today's date>Posting Date: <today's date>Currency: AEDClearing Reason: 04Write-Off Reason: Y1Document Type: YAReconciliation Key: <reconciliation key generated by system> |  |  |
| 5 | Select Open Items | Choose Select Online. | The Checking reconciliation key screen appears. |  |
| 6 | Create Reconciliation Key | Choose Yes. | A new reconciliation key is created. |  |
| 7 | Continue to Write Off | Choose Continue. | The Write Off: Process Open Items screen is displayed. |  |
| 8 | Activate Items | Select open items to write off by choosing the Activate item button.Alternatively, double-click the gross amount to activate a specific item for write-off. | The selected open items have been activated. The activated write-off amount is displayed in the Gross Clearing field. |  |
| 9 | Post | Choose Post. | The write-off documents are posted. |  |

#### Write Off Items - Mass Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can perform a mass run to write off items when there are many uncollectible receivables or undisbursable payables.

Prerequisite

Before executing this step, you need to create open document first (refer to Preliminary Step - [Post Documents](#unique_8) [page ] 7).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Write Off Run (F3540). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Write-Off RunJob Name: FI-CA: Write-Off Run |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Basic Parameters | Make the following entries:In the Run Identification section:Prefix of Run ID: For example, ID0Simulation Run: UnselectIn the General Selections section:Business Partner: <business partner number>Contract Account: <contract account number>Company Code: <company code>Document Number: <document number>In the Additional Selections section:Amount From…To: <define amount range>Currency: AEDIn the Posting Parameters section:Posting Date: <today's date>Clearing Reason: 14-Mass Write-OffWrite-Off Reason: Y1Document Type: YA-General Document |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Display Job | Navigate to the new application job by choosing the information icon. | The Job Log screen is displayed.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Display Write-Offs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can efficiently access and display write-off data for a business partner or contract account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Write-Offs (F3125). | The Display Write-Off screen is displayed. |  |
| 3 | Enter Search Criteria | Make the following entry:Business Partner: <Business Partner number> |  |  |
| 4 | Execute | Choose Go. | The Write-Offs screen is displayed. Details of write-off history are listed. |  |

### Foreign Currency Valuation

#### Foreign Currency Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can valuate foreign currencies in contract accounts to adjust receivable and payable accounts as part of balance sheet preparation. The valuation posting is automatically reversed the day following the financial statement key date.

Prerequisites

You must post open document using a foreign currency when the exchange rate at the time of the posting is different from the exchange rate at the month-end, while executing foreign currency valuation. Open items should be available in a foreign currency and posted with a higher or lower current exchange rate. To post document in a foreign currency, you can use SAP Fiori app Post Document (FPE1) to adjust the exchange rate in detail.

To view exchange rates, you can either use the SAP Fiori app Currency Exchange Rates (F3616) with the GL Accountant role or manually enter the exchange rate in the document you are posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Execute Foreign Currency Valuation (FPW1).Note Use SAP Fiori app Execute Foreign Currency Valuation (FPW1) for a small number of open receivables in foreign currencies.Use SAP Fiori app Foreign Currency Valuation Run (F5985) and select job template Foreign Currency Valuation Run for a large number of open receivables in foreign currencies.If error occurs when you use SAP Fiori app Foreign Currency Valuation Run (F5985), access SAP Fiori app Foreign Currency Valuation Run (F5985) and select job template Repeat Posting of Foreign Currency Valuation Run.Lock exists if you run FPW1/FPW1M/FPW1P in parallel, as parallel posting runs are not allowed. |  |  |
| 3 | Enter General Selections | Make the following entry:Balance sheet key date: <last date of current quarter>Ledger: 0LCompany Code: <select specific company code> for example, 3310Note Please don't leave this field blank. |  |  |
| 4 | Further Selections | Valuation Variant: <for example, SAE> |  |  |
| 5 | Posting Parameters | Posting requested: selectReconciliation Key: <Reconciliation Key generated by system> |  |  |
| 6 | Execute | Choose Execute.Select No if comparison date is not used for valuation. Otherwise, select Yes and enter the comparison date. | The Valuation of Open Items for MM/DD/YYYY: screen is displayed. The valuation items with details are listed. |  |

#### Display Foreign Currency Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can display foreign currency valuations that have been executed or reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Foreign Currency Valuations (FPW2). |  |  |
| 3 | Enter Selection Criteria | Make the following entry:Company Code: 3310Ledger: 0LFlag one of the following 3 options, for example: No Reversed Valuations.No Reversed ValuationsWith Reversed ValuationsOnly Reversed Valuations |  |  |
| 4 | Execute | Choose Execute.It is also possible to reverse by selecting one or more log records and choosing the Reverse button. | The Foreign Currency Valuations Executed: screen is displayed. Details are listed. |  |

#### Deferred Inverse Posting for Foreign Currency Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

As an alternative method for foreign currency valuation, deferred inverse posting can be initiated by one of the following events:

- Clearing
- Reversal
- Clearing Reset

Prerequisite

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

1. Maintain key date for valuation plan variant:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Valuation Plan Variants | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Foreign Currency Valuation, choose Details (>).For the Define Valuation Plan Variants row, choose Configure.Valuation Plan Variant: S1Key Date: <last date of the previous month, last date of the current month and last date of the next month> | The Change View screen is displayed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Basic Settings | Go to the Business Processes Configuration app and search for the following activity: Define Valuation Plan Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Maintain Key Dates for Valuation Plan Variants | Valuation Plan Variant: S1Key Date: <last date of the previous month, last date of the current month and last date of the next month> | The Change View screen is displayed. |  |

1. Maintain valuation plan variant to company code:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Set Up Company Codes for Contract Accounts Receivable and Payable | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Organization, choose Details (>).For the Set Up Company Codes for Contract Accounts Receivable and Payable row, choose Configure.Valuation Plan Variant: S1 | The Change View screen is displayed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Basic Settings | Go to the Business Processes Configuration app and search for the following activity: Set Up Company Codes for Contract Accounts Receivable and Payable.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Maintain Valuation Plan Variant | Valuation Plan Variant: S1 | The Change View screen is displayed. |  |

1. Deferred inverse posting setting:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Configure Basic Settings | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Foreign Currency Valuation, choose Details (>).For the Basic Settings row, choose Configure.Valuation Based On: <Choose 2 Several Account Balancing Views with Deferred Inverse Pstg> | The Change View "Basic Settings: Change": Details screen is displayed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Basic Settings | Go to the Business Processes Configuration app and search for the following activity: Basic Settings.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Maintain Basic Settings | Valuation Based On: <Choose 2 Several Account Balancing Views with Deferred Inverse Pstg> | The Change View "Basic Settings: Change": Details screen is displayed. |  |

Procedure

1. Execute foreign currency valuation on key date 1, for example, end of January (refer to the step [Foreign Currency Valuation](#unique_20) [page ] 31).
2. One of valuated documents is cleared/opened by the following events which is later than key date 1:
    - Reversal (refer to scope item 2BI Contract Accounting – Customer Initiated Payments, Appendix > Reverse Document )
    - Clearing Reset (refer to scope item 2UJ Contract Accounting – Open Item Management, Appendix > Reset Cleared Items )
    - Clearing (refer to scope item 2DP Contract Accounting – Company Initiated Payments, step Execute Payment Run)
3. Execute deferred inverse posting:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Deferred Inverse Posting (FPW3). |  |  |
| 3 | Enter General Selections | Make the following entry:Company Code: 3310Ledger: 0L |  |  |
| 4 | Posting Parameters | Simulation Mode: Unselect |  |  |
| 5 | Execute | Choose Execute. | The List of Inverse Postings screen is displayed. |  |

1. Execute foreign currency valuation on key date 2, for example, end of February (refer to the step [Foreign Currency Valuation](#unique_20) [page ] 31).

#### Clear Foreign Currency Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

When a foreign currency document is cleared through payment, the system automatically posts any realized gains or losses resulting from exchange rate differences.

Procedure

1. To post document in a foreign currency, you can use SAP Fiori app Post Document (FPE1) to change the exchange rate in the item detail. Please refer to Preliminary Step - [Post Documents](#unique_8) [page ] 7.
2. To clear foreign currency document (for example, cleared by payment), follow the steps below.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot: Initial Screen displays. |  |
| 3 | Input Parameters for Payment Lot | Choose Create.Lot: <your payment lot ID>Make the following entries on the Payment Lot Create: Default Entries and Status screen:Control Information:Lot: <your payment lot ID>Search Term: <input your search information>Additional Info: <input your specific information>Specifications for Posting Documents:Document Type: <by default>Posting Date: <by default>Document Date: <by default>Reconciliation Key: <generated by the system>Currency: AEDSpecification for Posting Items on Bank Clearing Account:Bank Clearing Account: 11001080Company Code: 3310Value Date: <today's date>Selections for Selecting and Clearing Open Items:Clearing Reason: <01, by default>Selection Category: <by default>Line Layout: SAPChoose New Items.On the Payment Lot Create: Payments screen, check and make the following entries:In the Default Value and Status section: <values are maintained by default>In the Payments section:Payment Amount: <input the amount>Selection Category: Select G/K/B/PNote G stands for Business Partner, K stands for Contract Account and B stands for Document.If parameters you input are in accordance with the open items, the payment lot can clear open items of specific business partner, otherwise, it needs further clarification.If you want to create payment lot through payment advice note, you can create payment advice note manually or import the payment advices to create payment advice note, then you can directly input payment advice note with selection category P during the payment lot creation.Click Save. | Payment lot is created. |  |
| 4 | Post Payment Lot | Input your payment lot ID on the Payment Lot: Initial Screen.Lot: <your payment lot ID>Choose Close.Note Payment lot must be closed before it can be posted.Choose Yes when message appears: All payment entered in full?Choose Post.In the Schedule Job dialog box, choose Start online and choose OK.Choose Continue when message appears: Posting run is complete, check status.In the Status section, system shows the posting status.Postprocessing is required means the payment needs further clarification. | Payment lot is closed and posted. |  |

#### Clear Foreign Currency Document in Value Adjustment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

When a document in foreign currency is posted value adjustments (refer to step [Create Doubtful Receivables and Individual Value Adjustments According to Age](#unique_12) [page ] 20 / [Post Value Adjustments](#unique_13) [page ] 22) and is subsequently cleared, the system resets the value adjustment amount and posts exchange rate differences resulting from fluctuations.

To activate the function for clearing foreign currency invoices within value adjustments, you need to ensure the following prerequisite is maintained:

Prerequisite

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Access configuration activity: Define Valuation Areas for Receivables Adjustments (102194).

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Valuation Areas for Receivables Adjustments | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Doubtful Receivables and Value Adjustments, choose Details (>).For the Define Valuation Areas for Receivables Adjustments row, choose Configure.Company Code: 3310Valuation Area: SAEExchange Rate: Choose Yes | The Change View screen is displayed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Define Valuation Areas for Receivables Adjustments | Go to the Business Processes Configuration app and search for the following activity: Define Valuation Areas for Receivables Adjustments.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Maintain Define Valuation Areas for Receivables Adjustments | Company Code: 3310Valuation Area: SAEExchange Rate: Choose Yes | The Change View screen is displayed. |  |

Procedure

1. To post document in a foreign currency, you can use SAP Fiori app Post Document (FPE1) to change the exchange rate in the item detail. Please refer to Preliminary Step - [Post Documents](#unique_8) [page ] 7.
2. You can post individual value adjustments by following the step [Create Doubtful Receivables and Individual Value Adjustments According to Age](#unique_12) [page ] 20 / [Post Value Adjustments](#unique_13) [page ] 22.
3. You can clear foreign currency document (for example, cleared by write-offs) by following the step [Write Off Items](#unique_17) [page ] 27 or [Write Off Items - Mass Run](#unique_18) [page ] 28.
4. You can reset value adjustment when a document in foreign currency is cleared by following the step [Create Doubtful Receivables and Individual Value Adjustments According to Age](#unique_12) [page ] 20 / [Post Value Adjustments](#unique_13) [page ] 22).

### Reclassifications

#### Create Open Item Lists for Reclassifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, the system reviews the balance of open items for a business partner by company code, and reclassifies accounts where receivables have a credit balance and payables have a debit balance.

Prerequisites

To reclassify accounts receivable with a credit balance, you'll need to complete the following two prerequisite steps:

1. Access configuration activity: Define Receivables and Payables Accounts (102513) to maintain G/L account 12100200 and select the checkbox under Debit column (pre-delivered content).
2. Make the balance of opens items for a business partner result in a credit balance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Creation Run Open Item List for Key Date (F3538). |  |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Open Item List for Key DateJob Name: FI-CA: Open Item List for Key Date |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Setting section:Run ID Prefix: <for example, ID0>Ignore Clearing History: UnselectIn the General Selections section:Key Date: <last date of current month>Ledger: 0LNote Don't leave the Ledger field blank.In the Grouping and Total Levels section:Grouping at Level 1:2: Partner:-Totals at Level 1:2: Company Code:-In the Output Options - Due Dates section:Statement Due Date Grid: UnselectIn the Output Options - Reclassification section:Regrouping statement: SelectName for Export: <give any name> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, navigate to the new application job by choosing the information icon. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Post Reclassifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can make automatic adjustment postings for accounts receivable with credit balances and accounts payable with debit balances within Contract Accounts Receivable and Payable.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Reclassifications (FPRECL). | The Post Reclassifications screen is displayed. |  |
| 3 | Select Posting | In the left panel structure, expand the target folders and double-click the posting document. | On the right side of the screen, you can see status and other details of the export data.If the posting has already been executed, you can see data of the posted document.If the posting has not been executed yet, system generates a posting proposal, provided no errors are determined during the export. If an error sign displays, you cannot execute the posting. |  |
| 4 | Execute | Choose Save. | Two documents are created: one for reclassification and the other for reversal on the day after the key date. |  |

#### Create Open Item Lists for Reclassifications by Due Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, the system checks the balance of open items for a business partner, focusing on those with a due date exceeding one year, across each company code. It then reclassifies account receivable with a credit balance and account payable with a debit balance.

Prerequisites

To reclassify accounts receivable with a credit balance, you need to carry out the following prerequisite steps:

1. Access configuration activity: Define Receivables and Payables Accounts (102513) to maintain G/L account 12100200 and select the checkbox under Debit column (pre-delivered content).
2. Make the balance of opens items which have due date more than 1 year for a business partner result in a credit balance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Creation Run Open Item List for Key Date (F3538). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: Open Item List for Key DateJob Name: Open Item List for Key Date |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Setting section:Run ID Prefix: For example, ID0Ignore Clearing History: UnselectIn the General selections:Key date: <last date of current month>Ledger: 0LNote Don't leave the Ledger field blank.In the Grouping and Total Levels sections:Grouping at Level 1:2: Partner:-Totals at Level 1:2: Company Code:-In the Output Options - Due Dates section:Statement Due Date Grid: SelectGrid Interval in days: -365Name for Export: <give any name> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, navigate to the new application job by choosing the information icon. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Post Reclassifications by Due Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In accordance with certain accounting principles, it is necessary to separately display receivables with a due date extending more than one year into the future. As part of closing operations, you can create and post the necessary adjustments for such open items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Reclassifications by Due Date (FPRECL_DUEGRID). | The Post Reclassifications by Due Date screen is displayed. |  |
| 3 | Select Posting | In the left panel structure, expand the target folders and double-click the posting document. | On the right side of the screen, you can see status and other details of the export data.If the posting has already been executed, you can see data of the posted document.If the posting has not been executed yet, system generates a posting proposal, provided no errors are determined during the export. If an error sign displays, you cannot execute the posting. |  |
| 4 | Execute | Choose Save. | Two documents are created: one for reclassification and the other for reversal on the day after the key date. |  |

### Day-End Closing

#### Close Reconciliation Keys

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In earlier steps, you have successfully completed postings to the Reconciliation Key. In this activity, you will close the Reconciliation Keys to enable the transfer of total records to the General Ledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Delete and Close Reconciliation Key (FPG4). | The Automatic Reconciliation Key Closing screen is displayed. |  |
| 3 | Enter Selection | Make the following entry:Entered by: <name of the user who created the reconciliation key> |  |  |
| 4 | Enter Processing Options | Make the following entries:Close Used Keys: SelectDelete Unused Open Keys: SelectDelete Unused Closed Keys: SelectTest Run: Unselect |  |  |
| 5 | Execute | Choose Execute. | Selected reconciliation keys are closed. |  |

#### Transfer FI-CA Total Records to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In the previous step, you closed the Reconciliation Keys. Now, in this activity, you will transfer the total records from Contract Accounts Receivable and Payable to the General Ledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Transfer Total Records to G/L (FPG1). | The Transfer of FI-CA Totals Records to General Ledger screen is displayed. |  |
| 3 | Maintain Parameters | Make the following entries:Reconciliation Key: <select reconciliation key>Company Code: 3310Test Run/Update Run: <select 2>List of Documents Created: <select the checkbox if you want to have a list of transferred line items> |  |  |
| 4 | Execute Job | Choose Execute. | Total records are posted in General Ledger. |  |

### Month-End Closing

#### Close Previous Accounting Period

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can close previous posting period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as General Ledger Accountant role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Posting Periods (F2293). | The Manage Posting Periods screen is displayed. |  |
| 3 | Enter Parameters | Make the following entries and choose Go:Posting Period Variant: 3310Fiscal Year Variant: K4Account Type: V(Contract accounts) | The posting period line for FI-CA is listed. |  |
| 4 | Select Period | Select the line from the Posting Periods pane and choose Set Posting Periods. Then choose Open Periods. | The Set Posting Periods – Open Periods screen is displayed. |  |
| 5 | Set Period | Make the following entries:On the Normal Periods tab:From Year/Period: <fiscal year for first period allowed/the beginning of the allowed posting period for contract accounts receivable and payable> for example, 2017/001To Year/Period: <fiscal year for last period allowed/the end of the allowed posting period for contract accounts receivable and payable> for example, 2017/012On the Adjustment Periods tab:From Year/Period: <the beginning of the year for special period 013/013> for example, 2017/013To Year/Period: <the end of the year for special period 016/016> for example, 2017/016 |  |  |
| 6 | Save | Choose OK. | No more posting in Contract Accounts Receivable and Payable are allowed in the previous period. |  |

#### Reconcile Open Items with G/L

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can verify the reconciliation between open items and the General Ledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Reconcile Open Items with G/L (FPO2). | The Reconciliation Between Open Items and G/L screen is displayed. |  |
| 3 | Enter General Selections | Make the following entry:Company Code: 3310 |  |  |
| 4 | Execute | Choose Execute. | A list is displayed on the Reconciliation Between Open Items and G/L screen.The report reconciles Contract Accounts Receivable and Payable with relevant General Ledger. |  |

## Appendix

### Process Integration

The processes to be tested in this test script are part of a chain of integrated processes.

#### Preparation and Execution

##### Change Reconciliation Key

Purpose

In this activity, you have the option to manually delete or close Reconciliation Keys.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Change Reconciliation Key (FPF2). | The Change Reconciliation Key: InitScreen screen is displayed. |  |
| 3 | Enter Reconciliation Key | Search with the value help of Reconciliation Key.Make the following entry:Entered by: <name of the user who created the Reconciliation Key, for example, your user>Choose Start Search. |  |  |
| 4 | Select | Select one Reconciliation Key that has not been closed yet and choose Enter. | Details of the Reconciliation Key are shown. |  |
| 5 | Execute | Choose Close and confirm the dialog box. | The Reconciliation Key will be closed for further postings. |  |

##### Manage Reconciliation Key

Purpose

In this activity, you can create, modify, and close Reconciliation Keys, as well as transfer the associated records to General Ledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Manage Reconciliation Key (F4531). | The Manage Reconciliation Key: InitScreen screen is displayed. |  |
| 3 | Enter Reconciliation Key | Search with the value help of Reconciliation Key.Make the following entry:Entered by: <name of the user who created the Reconciliation Key, for example, your user>Choose Start Search. | Details of the Reconciliation Key are shown. |  |
| 4 | Select | Select one Reconciliation Key that you want to close. |  |  |
| 5 | Execute | Choose Close and confirm the dialog box. | The Reconciliation Key is processed accordingly. |  |

You could transfer the FI-CA total records to General Ledger via the same SAP Fiori app with the Reconciliation Specialist role.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Manage Reconciliation Key (F4531). | The Manage Reconciliation Key: InitScreen screen is displayed. |  |
| 3 | Enter Reconciliation Key | Search with the value help of Reconciliation Key.Make the following entry:Entered by: <name of the user who created the Reconciliation Key, for example, your user>Choose Start Search. | Details of the Reconciliation Key are shown. |  |
| 4 | Select | Select one Reconciliation Key that you want to edit. | Details of the Reconciliation Key are displayed. |  |
| 5 | Execute | Choose Transfer to General Ledger. | Total records are posted in General Ledger. |  |

##### Display Itemization for Posting Totals

Purpose

In this activity, you can view the detailed itemization of documents that have been recorded under a Reconciliation Key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Itemization for Posting Totals (FPT5). | The Itemization for Posting Totals screen is displayed. |  |
| 3 | Enter Reconciliation Key | Search with the value help of the Reconciliation Key.Make the following entry:Entered by: <name of the user who created the Reconciliation Key, for example, your user>Choose Start Search. | A list of Reconciliation Keys is shown. |  |
| 4 | Execute | Select one entry and choose Execute. | Details of the selected Reconciliation Key is shown. |  |

##### Display Posting Totals

Purpose

In this activity, you can view the total records associated with a Reconciliation Key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Display for Posting Totals (FPT7). | The Display for Posting Totals screen is displayed. |  |
| 3 | Enter Reconciliation Key | Search with the value help of the Reconciliation Key.Make the following entry:Entered by: <name of the user who created the Reconciliation Key, for example, your user>Choose Start Search. | A list of Reconciliation Keys is shown. |  |
| 4 | Execute | Select one entry and choose Execute. | Details of the selected Reconciliation Key is shown. |  |

#### Forward Postings

##### Preparation and Execution

###### Assign New Reconciliation Key to Returns Lot

Purpose

In this activity, you can assign a new reconciliation key to the list of outstanding clarification process. For testing purpose, you need a returns lot with the status Postings Incomplete.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Assign new Reconciliation Key- Returns Lot. | The Assign New Reconciliation Key to Returns Lot screen is displayed. |  |
| 3 | Select Data | Search with the value help of Returns Lot and select one entry. Unflag the field Test Run. |  |  |
| 4 | Execute | Choose Execute. | A list of old and new Reconciliation Keys are displayed. The old reconciliation key is closed. |  |

###### Assign New Reconciliation Key for Payment Lot

Purpose

In this activity, you can assign a new reconciliation key to the list of outstanding clarification process. For testing purpose, you need a payment lot with the status Postings Incomplete.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Assign new Reconciliation Key - Payment Lot. | The Assign New Reconciliation Key to Payment Lot screen is displayed. |  |
| 3 | Select Data | Search with the value help of Payment Lot and select one entry. Unflag the field Test Run. |  |  |
| 4 | Execute | Choose Execute. | A list of old and new Reconciliation Keys are displayed. The old reconciliation key is closed. |  |

###### Maintain Alternative Posting Date

Purpose

In this activity, you can enter alternative posting dates. You need this, if you want to transfer totals records with a posting date in the past for which the posting period is closed in General Ledger and cannot be opened.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Maintain Alternative Posting Dates (FPG0C). | The Change View "Alternative Posting Data fpr G/L Transfer": Overview screen is displayed. |  |
| 3 | Enable New Entries | Choose New Entries. |  |  |
| 4 | Make a New Entry | Make the following entries:Company Code: 3310To PostDte: Current DateAlt Pst Dt: Current Date plus one monthChoose Save. | The alternative posting date will be stored. To check this, you can post a document with the current posting data, transfer the data to G/L and check the posting date of the G/L document. |  |

###### Transfer to General Ledger - Mass Run

Purpose

In previous steps, Reconciliation Keys are closed. In this activity, you can transfer the total records in Contract Accounts Receivable and Payable to General Ledger through mass run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Transfer Run Total Records to G/L (F3536). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. |  |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: Transfer of Totals Records to General LedgerJob Name: Transfer of Totals Records to General Ledger |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Identification section:Run ID Prefix: For example, ID0Simulation: UnselectIn the Selection Criteria section:Reconciliation Key: <select Reconciliation Keys to be transferred> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

###### Reverse General Ledger Transfer

Purpose

In this process, you can reverse the documents that were posted during the transfer of total records to the General Ledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Reverse G/L Transfer (FPG8). | The Reverse General Ledger Transfer screen is displayed. |  |
| 3 | Enter Selection Data | Search with the value help of Reconciliation Key.Make the following entry:Entered by: <name of the user who created the Reconciliation Key, for example, your user>Choose Start Search.Select one Reconciliation Key that has already been transferred to General Ledger.Unflag the field Test Run. |  |  |
| 4 | Execute | Choose Execute. | Transfer to General Ledger for this Reconciliation Key is reversed. |  |

##### Direct Posting to General Ledger

Prerequisite Steps

Before activating direct posting to the General Ledger, ensure that Origin Keys 01 and 02 are configured by following the steps outlined below.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Make Specifications | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of General Ledger Integration, choose Details (>).For the Define Direct G/L Transfer for Document Origins row, choose Configure. | The Define Direct G/L Transfer for Document Origins screen is displayed. |  |
| 4 | Add New Entries | Make the following entries:4 4Save the entries. | New entries are added. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Direct G/L Transfer for Document Origins | Go to the Business Processes Configuration app and search for the following activity: Define Direct G/L Transfer for Document Origins.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Define Direct G/L Transfer for Document Origins screen is displayed. |  |
| 3 | Input Parameters | Make the following entries:3 3Save the entries. | New entries are added. |  |

###### Post Document

Context

The FI-CA document is posted using Direct Transfer to the General Ledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen is displayed. |  |
| 3 | Enter Data | Make the following entries:Document Date: <today's date>Posting Date: <today's date>Document Type: YACurrency: AEDDirect Transfer: SelectReconcil. Key: <Reconciliation Key generated by system>Clearing Reason: 01 Incoming PaymentBP Item: Y01G/L Item: Y01Taxes Calculate Automatically: Select |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to Step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new Reconciliation key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen is displayed. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section,Business partn.: : <Business Partner number with MKK BP Role>Contract Acct: <Contract Account number related to the selected BP>Company Code: 3310Transac.: Y600/0020Note Use Transaction: Y600/0010 to post credit open items.In the Amounts and Due Date section:Net Due Date: <today's date>Amount: <input amount> |  |  |
| 8 | Post | Choose Post. | FI-CA document and accounting documents are posted. |  |

###### Display Document

Context

In this activity, you can view the details of the FI-CA document and the related accounting documents that were posted in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Document (FPE3). | The display Document: Initial Screen is displayed. |  |
| 3 | Enter Data | Make the following entry:Document Number: <document number posted in step Post Document> |  |  |
| 4 | Execute | Choose Enter. | Details of document are listed. |  |
| 5 | Check Accounting Documents | Choose G/L Documents. | Related accounting documents are listed. |  |

##### Reconciliation

###### Display General Ledger Transfer

Purpose

In this activity, you can view the details of the transfers made to the General Ledger.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Display for General Ledger Transfer (FPT3). | The Display for General Ledger Transfer screen is displayed. |  |
| 3 | Enter Selection Data | Make the following entry:Posting Date: current dateChoose Run. | Details of today’s transfer to General Ledger are displayed. |  |

###### Itemization for General Ledger Documents

Purpose

In this activity, you can view the documents that have been transferred from FI-CA to the General Ledger as total records.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Itemization for G/L Documents (FPG5). | The Itemization for G/L documents from FI-CA screen is displayed. |  |
| 3 | Enter Selection Data | Search with the value help of Reconciliation Key.Make the following entry:Entered by: <name of the user who created the Reconciliation Key, for example, your user>Choose Start Search.Select one Reconciliation Key which has already been transferred to General Ledger and choose Execute. | Total records of the selected General Ledger documents are displayed. |  |

###### Display Account Assignment for Single Documents

Context

In this activity, you can evaluate FI-CA documents that are posted to a specific object, such as a CO account assignment or a commitment item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Acct Assignment Details for Single Docs (FPT8). | The Acct Assignment Details: Single Docs screen is displayed. |  |
| 3 | Enter Selection Data | Search with the value help of Reconciliation Key.Make the following entry:Entered by: <name of the user who created the Reconciliation Key, for example, your user>Choose Start Search.Select one Reconciliation Key which has already been transferred to General Ledger and choose Execute. | For each document selected, data from totals records, document header, business partner and General Ledger items are displayed. |  |

##### Checks

###### Check Transfer Status of Reconciliation Key

Purpose

In this activity, you can verify the transfer status of a Reconciliation Key.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Check Transfer Status of Reconciliation Key (FPT4). | The Check Transfer Status of Reconciliation Key screen is displayed. |  |
| 3 | Enter Selection Data | Search with the value help of Reconciliation Key.Make the following entry:Entered by: <name of the user who created the Reconciliation Key, for example, your user>Choose Start Search.Select one Reconciliation Key which has already been transferred to General Ledger.Flag the field Transfer to General Ledger.Select All Selected Reconciliation Keys. |  |  |
| 4 | Execute | Choose Execute. | List of Reconciliation Keys is displayed and grouped by the status of the transfer. |  |

###### Check Totals Records

Purpose

In this activity, you can verify that the FI-CA posting totals align with the totals of the corresponding FI-CA documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Check Totals Records (FPT1). | The Check Totals Records screen is displayed. |  |
| 3 | Enter Selection Data | Search with the value help of Reconciliation Key.Make the following entry:Entered by: <name of the user who created the Reconciliation Key, for example, your user>Choose Start Search.Select one Reconciliation Key which has already been transferred to General Ledger.Extended Processing Log: Select |  |  |
| 4 | Execute | Choose Execute. | A list showing the differences between posting totals and FI-CA documents is displayed. |  |

###### Check General Ledger Documents

Purpose

In this activity, you can reconcile FI-CA with the General Ledger by comparing the FI-CA totals records that were transferred with the documents posted in the General Ledger during the transfer process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Check General Ledger Documents (FPG2). | The Check General Ledger Documents screen is displayed. |  |
| 3 | Enter Selection Data | Make the following entry:Company Code: 3310Choose Execute. | A list showing the determined differences during the reconciliation is displayed. |  |

###### Determine Gaps in Document Number Ranges

Purpose

In this activity, you generate a list of all missing document numbers within a company code, which have resulted from postings made to other company codes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Determine Gaps in Document Number Ranges (FPDOC). | The Display Missing FI-CA Documents in Company Code screen is displayed. |  |
| 3 | Enter Selection Data | Make the following entries:Company Code: 3310Posting Data: period to checkChoose Execute. | A list of missing FI-CA documents is displayed. |  |

###### Reconcile Postings - Mass Runs

Purpose

In this activity, you can perform the following procedures using a mass run:

- Check Totals Records (check whether FI-CA posting totals are in accordance with the totals of the relevant FI-CA documents)
- Check General Ledger Documents (reconcile FI-CA and General Ledger by comparing the transferred FI-CA totals records with the documents posted in General Ledger during the transfer)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Reconcile Postings (F3533). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: Check Totals RecordsJob Name: Check Totals Records |  |  |
| 5 | Enter Posting Parameters | Make the following entries and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Setting section:Run ID Prefix: for example, ID0In the General Selections section:Reconciliation Key: <select Reconciliation Keys to be checked> |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, navigate to the new application job by choosing the information icon. | The Job Log screen is displayed. The log should show no errors. |  |
| 10 | Choose Create | On the Application Jobs screen, choose Create. |  |  |
| 11 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: Check General Ledger DocumentsJob Name: Check General Ledger Documents |  |  |
| 12 | Enter Posting Parameters | Make the following entries and choose Step 3:Start Immediately: select |  |  |
| 13 | Enter Posting Parameters | Make the following entries:In the Run Setting section:Run ID Prefix: for example, ID0In the General Selections section:Reconciliation Key: <select Reconciliation Keys to be checked> |  |  |
| 14 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 15 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 16 | Check Job Status | After the job has been finished, navigate to the new application job by choosing the information icon. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Closing Preparation

##### Evaluate Installment Plans for Key Date

Purpose

Installment plans allow you to distribute original receivables across a series of installments with future due dates. It's important to separately display receivables with due dates extending more than one year into the future on the balance sheet.

In this activity, you can create a snapshot of the installment plan due dates as of the key date, along with the assignment of these due dates to the original items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Evaluate Installment Plans for Key Date (F3532). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create.Select Job Template: FI-CA: Evaluate Installment Plans for Key Date | The New Job screen is displayed. |  |
| 4 | Enter Basic Parameters | Make the following entry:Run ID Prefix: for example, ID0Simulation Run: Unselect |  |  |
| 5 | Enter Posting Parameters | Make the following entry:Company Code: 3310Key Date: <today's date>Note The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 6 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 7 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 8 | Check Job Status | After the job has been finished, navigate to the new application job by choosing the information icon. | The Job Log screen is displayed. The log should show no errors.Note The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

##### Create Open Item List for Key Date

Purpose

In this activity, you can display the open item list based on the selected key date.

You can create the open item list for key date either via SAP Fiori app Create Open Item List for Key Date or Evaluate Open Items. In the Evaluate Open Items app, you can use the predefined selection function.

Procedure

Method 1. Using SAP Fiori app Create Open Item List for Key Date.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Open Item List for Key Date (FPO1). | The FI-CA:Key Date-Based Open Item List screen is displayed. |  |
| 3 | Enter General Selections | Make the following entry in selection of number of open items:Key Date: <input date>Ledger: <select 0L, other ledgers are optional>Company Code: 3310Output Control: <by default>Business Partner: <select business partners for Z5a report> | The New Job screen is displayed. |  |
| 4 | Enter Additional Output | Make the following entry in the Additional Output section:Save Data: selectName: <description of the open item list> |  |  |
| 5 | Execute Job | Choose Execute. | A list is shown on the FI-CA: Key Date-Based Open Item List screen.The report displays a list of open items based on the key date you've selected. |  |

Method 2. Using SAP Fiori app Evaluate Open Items.

a. Create a pre-selection object.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Define Preselection (FPSELP). | The Preparations for Evaluations screen is displayed. |  |
| 3 | Select Object Type from the Object Name Menu | From the Object Name menu:Select Selections > Master Data > Business Partner. | The Business Partner folder is selected and the existing business partner objects are listed. |  |
| 4 | Create New Object | Choose Create New Object.Object type: Business PartnerObject name: <name of the object, for example, ZZ01>Choose Enter.Description: <input description of this object>In the Selections tab:Choose Create.Business Partner: <select business partners for this object>Choose Save.Go back to the Preparations for Evaluations screen.To save the object, choose Save. | The New Job screen is displayed. |  |

b. Create a pre-selection layout.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Define Layout for Evaluations (FPSELP1). | The Preparations for Evaluations screen is displayed. |  |
| 3 | Select Object Type from the Object Name Menu | From the Object Name menu:Select Layouts > Open Items Line Layout . | The Business Partner folder selected and the existing business partner objects listed. |  |
| 4 | Create New Object | Choose Create.Object type: Open Items Line LayoutObject name: <name of the layout, for example, Layout01>Choose Continue.Description: <input description of this layout>In the Select Fields tab, the following fields are selected for example:FieldRequired fieldField NameDocument numberXOPBEL[FKKOP]Repetition itemXOPUPW[FKKOP]ItemXOPUPK[FKKOP]Sub-itemXOPUPZ[FKKOP]Local currency amountXBETRH[FKKOP]CurrencyXWAERS[T00Business partnerGPART[FKKOP]In the Define Layout tab, the layout is defined as follows:FieldHiddenTotals fieldSortSubtotalDocument numberRepetition itemXItemXSub-itemXLocal currency amountX TotalCurrencyBusiness partner1H With headerChoose Save. | The New Job screen is displayed. |  |

c. Generate the pre-selection object.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Regenerate Preselections (F3787). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Generate Preselection Object | Job Template: Business Partner PreselectionStart Immediately: SelectPrefix of Run ID: ID0Object Name: SelectObject name: <select name of the preselection object> | A new preselection object of Business Partner type is created, and the object is displayed in the tree menu in the Business Partner folder. |  |
| 5 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. |  |
| 6 | Execute Job | Choose Schedule. | The Application Jobs view is displayed.One new application job is created with a status. |  |
| 7 | Display Job | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen displayed.The Run Identification should combine Run ID Prefix + dynamic number (xx).View generated. |  |

d. Create the open item list.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Evaluate Open Items (FPO4). | The FI-CA:Key Date-Based Open Item List screen is displayed. |  |
| 3 | Enter General Selections | Make the following entry in the Selection of number of open items section:Open Items Only: SelectKey Date: <input date>Master Data Selection:Predefined Selection: <preselection object defined in step a. Create a preselection object> | The Business Partner folder selected and the existing business partner objects listed. |  |
| 4 | Enter Additional Output | In the Output Control tab:Save Data: SelectLine Layout: <preselection object defined in step b. Create a preselection layout>Export to Table:Save Data: SelectName: <description of the open item list> | The New Job screen is displayed. |  |
| 5 | Execute Job | Choose Execute. | A list is shown on the Item List screen.The report displays a list of open items. |  |

##### Display Saved Open Item List

Purpose

In this activity, you can view the open item list as of the key date according to your selection criteria.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Saved Open Item Lists (F3638). | The screen Display Saved Open Item List is displayed. |  |
| 3 | Enter Parameter | To display saved open items, make sure you've made selection as described in step [Create Open Item List for Key Date](#unique_57) [page ] 72.Enter the following parameter:Key Date: <key date of the open item list>Description: <description of the open item list>Choose Go | A list of saved open item lists is shown. |  |
| 4 | Choose | Choose one item from Saved open item lists. | Details of saved open item is displayed. |  |

##### Itemization of Clarification Accounts - Returns

Purpose

In this activity, you can display the balance of a clarification account on a specific key date by examining the returns lot items that need clarification. For testing purposes, ensure you have a returns lot with the status Postings Incomplete.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Itemization of Clarification Accounts - Returns (FPR_RLCL). | The Application Jobs screen is displayed. |  |
| 3 | Enter Selection Data | Make the following entry:Key Date: <return lot postdate>Choose Execute. | A list of the clarification cases by company code and clarification account from Returns Lots is shown. |  |

##### Itemization of Clarification Accounts - Payments

Purpose

In this activity, you can display the balance of a clarification account for any specific key date by the payments lot items that need clarification. For testing purposes, ensure that you have a payments lot with the status Postings Incomplete.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Itemization of Clarification Accounts - Payments (FPR_PLCL). | The Itemization of Clarification Worklist from Payments Lot screen is displayed. |  |
| 3 | Enter Selection Data | Make the following entry:Key Date: <payment lot post date>Choose Execute. | A list of the clarification cases by company code and clarification account from Payment Lots is shown. |  |

##### Document Journal

Purpose

In this process, you can generate a document journal that includes data from the document headers and items of the selected documents. For each item category, the system automatically creates totals for each company code and local currency.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Document Journal (FPS_RFKKBELJ00). | The Document Journal screen is displayed. |  |
| 3 | Enter Selection Data | Make the following entry:Posting Date: beginning of the year until todayChoose Execute. | A list with the data from the document header and the business partner and general ledger items is displayed. |  |

##### Display G/L Line Items

Purpose

In this process, G/L line items are displayed with comprehensive details, including document number, G/L account, segment, amount, and other relevant information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Display G/L Line Items - for Contract Accounting (F9342). | The Display G/L Line Items screen is displayed |  |
| 3 | Enter Selection Data | Make the following entry:Posting Date: <any date>Choose Go. | G/L line items are displayed in a list view. |  |

##### Evaluate Open Item

Purpose

In this activity, you can obtain an overview of the outstanding receivables from your business partners.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access SAP Fiori App | Open Evaluate Open Items (FPO4). | The Item List screen is displayed |  |
| 3 | Enter Selection Data | Make the following entries:Key Date: <today's date>Installment Plan has Priority: SelectConsider Installment Plan for Key Date: SelectChoose Execute. | A list of all open items for this key date in local currency is displayed. |  |

##### Display Installment Plan Evaluation for Key Date

Purpose

In this activity, you can view a snapshot of the installment plan due dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Display Installment Plan Evaluation for Key Date (FPIPKEY_LIST). | The screen Deletion of Installment Plan Report for Key Date is displayed. |  |
| 3 | Enter Parameter | Enter the following parameter:Date ID: <required date>Run ID: <required Identification> |  |  |
| 4 | Execute | Choose Execute. | Reports are displayed. |  |

##### Delete Installment Plan Evaluation for Key Date

Purpose

In this activity, you can delete the snapshot of the installment plan due dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Delete Installment Plan Evaluation for Key Date (FPIPKEY_DEL). | The screen Deletion of Installment Plan Report for Key Date is displayed. |  |
| 3 | Enter Parameter | Enter the following parameter:Date ID: <required date>Run ID: <required Identification> |  |  |
| 4 | Execute | Choose Execute. | Reports are deleted. |  |

#### Flexible Workflow for Document Write-Off

Context

Flexible Workflow for Document Write-Off in Contract Accouting implements the dual control principle for writing-off of open items. If a writen-off run meets conditions set in Manage Workflows for Contract Accounting (F5135), a write-off document will not be created immediately. Rather a workitem will be routed to an approver for further action (release/rejection).

During the workflow:

- Approvers receive workflows in SAP inbox and can release/reject the write-off run.
- If approved, the original documents in the write-off run are automatically writen-off, for example, and the initiator will not be involved again.
- In case of rejection, the documents are not get written-off.

Note that the Requestor will not get any notification of the rejection from the approver. The Requestor needs to restart another workflow to approver.

Prerequisites

Make sure you have completed the following steps to activate the Flexible Workflow to write off open items in Contract Accounting.

1. Define Check Reason via SSCUI(103740)

It is recommended to create your own check reason for your workflow. If you decide to use standard check reason 07, you could skip this step.

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solutionand choose Configure Your Solution. | The Manage Your Solutionscreen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application: Contract AccountingItem Name: Postings and DocumentsSelect configuration and choose step Define Check Reasons.Choose the standard check reason 07 and copy it to create your Check Reason Code and adapt the setting according to your business needs. | The Change View "Check Reasons for Dual Control Principle": Overview screen is displayed. |  |

SAP Central Business Configuration:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Define Check Reasons | Go to the Business Processes Configuration app and search for the following activity: Define Check Reasons.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Manage Your Solutionscreen is displayed. |  |
| 3 | Input Parameters | Choose the standard check reason 07 and copy it to create your Check Reason Code, and adapt the setting according to your business needs. |  |  |

1. Activate Flexible Workflow for Posting Document

Access SSCUI - Define Default Check Reason for Workflow (103769)

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Your Solutionand choose Configure Your Solution. | The Manage Your Solutionscreen is displayed. |  |
| 3 | Input Parameters | Application Area: FinanceSub Application: Contract AccountingItem Name: Postings and DocumentsSelect configuration and choose step Define Default Check Reason for Workflow.Choose Create.Scrnario: WS02400082Check Reason: 07Save. | The screen Maintain C003:Overview is displayed.The Default Check reason assigned to workflow scenario ID.The workflow for document write-off posting is enabled in this client. |  |

SAP Central Business Configuration:

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Define Default Check Reason for Workflow | Go to the Business Processes Configuration app and search for the following activity: Define Default Check Reason for Workflow.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Maintain C003:Overviewscreen is displayed. |  |
| 3 | Input Parameters | Choose Create.Scenario: WS02400082Check Reason: 07Save. | The Default Check reason assigned to workflow scenario ID.The workflow for document write-off posting is enabled in this client. |  |

1. Define responsibility for rules used in workflow steps and assign users to responsibilities.

|  |
| --- |
| Note The approver(s) and requester(s) should be different business users. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration . |  |  |
| 2 | Access SAP Fiori App | Open Manage Teams and Responsibilities - Contract Accounting (F5134). | The Manage Teams and Responsibilities view displays. |  |
| 3 | Create Team | Choose Create. | The Team view displays. |  |
| 4 | Enter Team Details | Make the following entries:In the General Information tab:Name: for example, Approver for document Write-off postingGlobal ID: for example. Approver for document Write-off postingType: SFICAWF (Contract Accounting Workflow Team)Description: (Optional)Status: Ready to use |  |  |
| 5 | Enter Team Details | Choose the Team Members tab. |  |  |
| 6 | Enter Team Details | Choose the Create button. | A blank field displays under Business Partner. |  |
| 7 | Enter Team Details | Make the following entries and choose Save:Business Partner: For example,Example Accounts Payable and Receivable ManagerFunction: Function for Approving - Level 1 | The responsibility for the Contract Document Write-off posting workflow is defined. |  |

1. Define and activate your approval workflows

You can create a new workflow by copying the standard template or create a new entry directly. In this activity,you create the new workflow by copying standard template.

|  |
| --- |
| Note You can have multiple active workflows and could define or sort the order. The system will go through all the active workflows from the first order to the last until the workflow could be started. If the system could determine a workflow which could start a workflow process, the others will be ignored! |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. |  |  |
| 2 | Access SAP Fiori App | Open Manage Workflows for Contract Accounting (F5135). | The Manage Workflows view displays. |  |
| 3 | Select | Select Contract Accounting Write-Off Run |  |  |
| 4 | Choose | Choose Workflow Template . |  |  |
| 5 | Copy Workflow | Choose Copy. | The Copy of Workflow screen displays. |  |
| 6 | Enter Workflow Details | Make the following entries and choose Save:Header tab:Name: for example, workflow for Document Write-OffProperties tab:Description: for example workflow for Document Write-OffValid from: Today’s dateValid to: 12/31/9999Start Conditions tab:Only start the workflow if all of the following preconditions are met:For example:Write-Off balance Amount is greater or equal 2000 AED.Choose Add to add another condition if needed.Add Alternative Preconditions tab: (Option)Step Sequence tab: Choose the first sequence and modify:Step Name:for example: Approve Write-Off RunStep Type: Approve Write-Off RunRecipients tab:Assignment By: Teams (For example)Team: Select the team you create in last stepStep Conditions tab: (Option)EXCEPTION HANDLING tab:Name: The document should not be releasedRequired Action: Do nothingAction result: Cancel workflow | You saved the workflow template. |  |
| 7 | Activate Rule | Choose Apply, then choose Save and Activate.Note The template workflow is delivered default as active with no preconditions defined, which means this workflow will always start. Make sure you deactive the standard template if you don’t want to use it before you start your document reversal postings. | The workflow of document Write-off is activated. |  |

##### Write Off Open Items

Context

Having completed all prerequisite steps and established the start conditions — specifically a write-off balance amount greater than or equal to 2,000 AED — in the Define and Activate your Approval Workflows step, you are now ready to initiate a write-off posting for a document to trigger the workflow. Once the write-off posting meets the conditions, the workflow will start.

The original document is blocked for write-off posting until the approver has approved the work items.

In this activity, you perform a write-off posting for a document where the total amount is equal to or greater than 3,000 AED to initiate the workflow.

To do so, refer to chapter Write Off Items.

|  |
| --- |
| Note Message appears: Write-off is being checked - check reason 07 was set. |

##### Verify Document

Purpose

In this activity, you can verify a document that has been blocked by the write-off workflow.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |
| 2 | Access SAP Fiori App | Open Display Document (FPE3). | The Display Document: Initial Screen is displayed. |
| 3 | Select Document to Display | Make the following entry and choose More > Goto > Document Header :Document Number: <document number you try to reverse in previous step>BP Item: Y01G/L Item: Y01 | The Display Document: Overview screen is displayed. The document details are displayed.In the Additional Data tab:Message Document cannot be changed until confirmed due to check reason Write-off approval is displayed. |
| 4 | Select Document to Change | Choose menu Document > More > (Display->Change) . | Message Document cannot be changed until confirmed due to check reason Document write-off is displayed.Note You have this message based on your selected No Changes in your check reason. |

##### Approve Document Write Off (for Processor - Inbox)

Context

You receive work item of a document from write-off posting that needs to be checked. After checking the detailed information of the document(s) to be reversed, you can either release or reject it with a comment/ reason. Once the work item has been selected and released, it disappears from the list. If a workitem is released/approved, the write-off posting starts.

|  |
| --- |
| Note You can set substitute when you are absent and could not access your Inbox. To do so, go to My Inbox and find the Substitute function from your profile. |

In this activity, you access Inbox as an approver and release the document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. |  |  |
| 2 | Access SAP Fiori App | Open My Inbox for Contract Accounting - All Items (F5136). |  |  |
| 3 | Approve Documents | Select the document to be released.Choose Release.Decision Note: <your note>Choose Submit. | The work item is released and the write-off posting is completed.Note All released documents are displayed in the My Outbox - Outbox items app. |  |

##### Reject Document Write Off (for Processor - Inbox)

Context

You receive a work item of a document from write off posting that needs to be checked. After checking the detailed information of the document, you can either approve or reject with a comment/ reason. Once the work item has been selected and rejected, the orginal document could not be written-off.

In this activity, you access Inbox as an approver and reject the work item.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Manager (FI-CA) role assigned. |  |  |
| 2 | Access SAP Fiori App | Open My Inbox for Contract Accounting - All Items (F5136). | The My Inbox view displays. |  |
| 3 | Reject Installment Plan | Select the work item to be rejected.Choose Reject and enter the reason for rejection. For example: The amount is not correct.Choose Submit. | The write off posting is rejected. |  |

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
> Flagged while digesting this document, not verified: Write-off workflow start condition is stated as write-off balance >= 2,000 AED, but the test activity says to post a write-off of a document total >= 3,000 AED to trigger it.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-group-ledger-ifrs-33x-ae-905]]
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-group-ledger-us-gaap-33v-ae-904]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2BK_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 141,267 chars in the whole document
