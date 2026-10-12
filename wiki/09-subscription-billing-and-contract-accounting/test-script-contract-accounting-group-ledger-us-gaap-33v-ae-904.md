---
id: 09-subscription-billing-and-contract-accounting/test-script-contract-accounting-group-ledger-us-gaap-33v-ae-904
title: "Test Script: Contract Accounting – Group Ledger US GAAP (33V_AE) (33V_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud test script (33V_AE, company code 3310): US GAAP ledger FI-CA steps for doubtful receivables, FX valuation, reclassification, closing."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/fi-ca-closing-and-valuation]
aliases: [33V_S4CLD2608_BPD_EN_AE]
keywords: [Contract Accounting Closing and Valuation, doubtful receivables, value adjustments, credit loss allowances, foreign currency valuation, deferred inverse posting, reclassifications, group ledger us gaap, contract accounting, day-end closing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33V_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-904
topic: 09-subscription-billing-and-contract-accounting/fi-ca-closing-and-valuation
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Contract Accounting – Group Ledger US GAAP (33V_AE) (33V_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33V_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Contract Accounting Closing and Valuation** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Contract Accounting – Group Ledger US GAAP (33V_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851601)

[2 Prerequisites 4](#_Toc232851602)

[2.1 System Access 4](#_Toc232851603)

[2.2 Roles 4](#_Toc232851604)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232851605)

[2.4 Business Conditions 6](#_Toc232851606)

[2.5 Preliminary Step 6](#_Toc232851607)

[2.5.1 Post Documents 6](#_Toc232851608)

[3 Overview Table 9](#_Toc232851609)

[4 Test Procedures 11](#_Toc232851610)

[4.1 Doubtful Receivables 11](#_Toc232851611)

[4.1.1 Create Flat-Rate Value Adjustments According to Expected Credit Loss Rates 11](#_Toc232851612)

[4.1.2 Create Doubtful Receivables and Individual Value Adjustments 16](#_Toc232851613)

[4.1.3 Create Doubtful Receivables and Individual Value Adjustments according to Age 17](#_Toc232851614)

[4.1.4 Post Value Adjustments 19](#_Toc232851615)

[4.1.5 Display Value Adjustments 21](#_Toc232851616)

[4.1.6 Transfer Value Adjustments 22](#_Toc232851617)

[4.1.7 Analyze Credit Loss Allowances 24](#_Toc232851618)

[4.2 Foreign Currency Valuation 25](#_Toc232851619)

[4.2.1 Foreign Currency Valuation 25](#_Toc232851620)

[4.2.2 Display Foreign Currency Valuation 26](#_Toc232851621)

[4.2.3 Deferred Inverse Posting for Foreign Currency Valuation 27](#_Toc232851622)

[4.2.4 Clear Foreign Currency Document (Optional) 32](#_Toc232851623)

[4.2.5 Clear Foreign Currency Document in Value Adjustment (Optional) 34](#_Toc232851624)

[4.3 Reclassifications 36](#_Toc232851625)

[4.3.1 Create Open Item Lists for Reclassifications 36](#_Toc232851626)

[4.3.2 Post Reclassifications 38](#_Toc232851627)

[4.3.3 Create Open Item Lists for Reclassifications by Due Date 38](#_Toc232851628)

[4.3.4 Post Reclassifications by Due Date 40](#_Toc232851629)

[4.4 Day-End Closing 41](#_Toc232851630)

[4.4.1 Close Reconciliation Keys 41](#_Toc232851631)

[4.4.2 Transfer FI-CA Total Records to General Ledger 42](#_Toc232851632)

[4.5 Month-End Closing 42](#_Toc232851633)

[4.5.1 Close Previous Accounting Period 42](#_Toc232851634)

[4.5.2 Reconcile Open Items with G/L 42](#_Toc232851635)

## Purpose

Overview

In this process, you handle ledger-specific transactions and reports for US GAAP within contract accounting. This includes transactions such as Doubtful Receivables, Foreign Currency Valuation, Day-End Closing, and Month-End Closing.

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
| (Optional) Configuration Expert - Business Process Configuration(Only required when modifying SSCUI to add a new Valuation Adjustment Variant Key with specific Age Grids, for example) | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Accounts Payable and Receivable Accountant (FI-CA) | SAP_BR_APR_ACCOUNTANT_FICA | Contract Accounting | SAP_BR_APR_ACCOUNTANT_FICA |  |
| Administrator - Accounts Payable and Receivable (FI-CA) | SAP_BR_ADMIN_APR_FICA | Contract Accounting - Jobs | SAP_BR_ADMIN_APR_FICA |  |
| Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | SAP_BR_RECONC_SPEC_APR_FICA | Contract Accounting - Reconciliation | SAP_BR_RECONC_SPEC_APR_FICA |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

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
| 2BK - Contract Accounting – Daily and Monthly Closing | Perform Doubtful Receivables; Foreign Currency Valuation procedure; Transfer FI-CA Total Records to the Leading Ledger are executed. |
| 2VA - Accounting and Financial Close – Group Ledger US GAAP | Must be in scope as prerequisite. |

### Preliminary Step

#### Post Documents

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Post Document (FPE1). | The Post Document: Initial Screen is displayed. |  |
| 3 | Enter Data | Make the following entries:Document Date: <today’s date>Posting Date: <today’s date>Document Type: YACurrency: AEDReconcil. Key: <Reconciliation Key generated by system>BP Item: Y01G/L Item: Y01Taxes Calculate Automatically: SelectTax Jurisdiction: Select |  |  |
| 4 | Enter BP Item | Choose New BP Itm. | The Checking reconciliation key screen appears.If Reconcil. Key has already been created, the Checking reconciliation key screen won’t be displayed. Please go to Step 7 directly. |  |
| 5 | Create Reconciliation Key | Choose Yes. | A new Reconciliation Key is created. |  |
| 6 | Continue to Enter BP Item | Choose Continue. | The Post Document: Enter Item screen is displayed. |  |
| 7 | Enter Item Data | Make the following entries:In the Account Assignment section,Business partn.: <Business Partner number with MKK BP Role>Contract Acct: <Contract Account number related to the selected BP>Contract: <fill in Provider Contract number, which is optional>If the document has contract, you also need to fill in Contract Item.Company Code: 3310Transac.: Y600/0020Note Use Transaction: Y600/0010 to post credit open items.In the Amounts and Due Date section:Net Due Date: <input net due date>Amount: <input amount> |  |  |
| 8 | Post | Choose Post. | The FI-CA document is posted. |  |

## Overview Table

This Monthly and Daily Closing scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 2: Doubtful Receivables

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Flat-Rate Value Adjustments According to Expected Credit Loss Rates](#unique_9) [page ] 11 | Administrator - Accounts Payable and Receivable (FI-CA) | Adjust Receivables According To Age (F3535) | Receivables are automatically set to doubtful and flat rate value adjustments are made on the basis of their age. |
| [Create Doubtful Receivables and Individual Value Adjustments](#unique_10) [page ] 16 | Accounts Payable and Receivable Accountant (FI-CA) | Adjust Receivables (FPZW) | The selected receivables are marked as doubtful and individual value adjustments are done. |
| [Create Doubtful Receivables and Individual Value Adjustments according to Age](#unique_11) [page ] 17 | Administrator - Accounts Payable and Receivable (FI-CA) | Adjust Receivables According To Age (F3535) | Receivables are automatically set to doubtful and individual value adjustments are made on the basis of their age. |
| [Post Value Adjustments](#unique_12) [page ] 19 | Administrator - Accounts Payable and Receivable (FI-CA) | Post Value Adjustments (F3539) | Adjusted and doubtful receivables are transferred cumulative in the general ledger. |
| [Display Value Adjustments](#unique_13) [page ] 21 | Accounts Payable and Receivable Accountant (FI-CA) | Display Posted Value Adjustments (F4824) | The transferred receivables adjustments can be displayed. |
| [Transfer Value Adjustments](#unique_14) [page ] 22 | Administrator - Accounts Payable and Receivable (FI-CA) | Prepare Value Adjustment Analysis (F3843) | Transfer Value Adjustments from Contract Accounting to General Ledger for the Credit Loss Allowance Analysis preparation. |
| [Analyze Credit Loss Allowances](#unique_15) [page ] 24 | General Ledger Accountant | Analyze Credit Loss Allowances (F3752) | Analyze credit loss allowances. |

Table 3: Foreign Currency Valuation

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Foreign Currency Valuation](#unique_16) [page ] 25 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Execute Foreign Currency Valuation (FPW1) | Valuate foreign currencies in contract accounts with the aim of adjusting the receivable and payable accounts as part of balance sheet preparations |
| [Display Foreign Currency Valuation](#unique_17) [page ] 26 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Display Foreign Currency Valuations (FPW2) | Display foreign currency valuations that have been carried out or reversed. |
| [Deferred Inverse Posting for Foreign Currency Valuation](#unique_18) [page ] 27 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Deferred Inverse Posting (FPW3) | Deferred inverse posting for Foreign Currency Valuation. |
| [Clear Foreign Currency Document (Optional)](#unique_19) [page ] 32 |  |  |  |
| [Clear Foreign Currency Document in Value Adjustment (Optional)](#unique_20) [page ] 34 |  |  |  |

Table 4: Reclassifications

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Open Item Lists for Reclassifications](#unique_21) [page ] 36 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Creation Run Open Item List for Key Date (F3538) | Closing balance of selected open items has to be reclassified. |
| [Post Reclassifications](#unique_22) [page ] 38 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Post Reclassifications (FPRECL) | Display reclassification document. |
| [Create Open Item Lists for Reclassifications by Due Date](#unique_23) [page ] 38 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Creation Run Open Item List for Key Date (F3538) | Closing balance of selected open items has to be reclassified by due dates. |
| [Post Reclassifications by Due Date](#unique_24) [page ] 40 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Post Reclassifications by Due Date (FPRECL_DUEGRID) | Display reclassification document generated by due date. |

Table 5: Day-End Closing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Close Reconciliation Keys](#unique_25) [page ] 41 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Delete and Close Reconciliation Key (FPG4) | The selected reconciliation keys are closed |
| [Transfer FI-CA Total Records to General Ledger](#unique_26) [page ] 42 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Transfer Total Records to G/L (FPG1) | FI-CA total records are transferred to the General Ledger |

Table 6: Month-End Closing

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Close Previous Accounting Period](#unique_27) [page ] 42 | General Ledger Accountant | Manage Posting Periods (F2293) | The previous accounting period is closed |
| [Reconcile Open Items with G/L](#unique_28) [page ] 42 | Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) | Reconcile Open Items with G/L (FPO2) | Contract Accounts Receivable and Payable are reconciled with the General Ledger |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Doubtful Receivables

Prerequisite

Transfer value adjustments from Contract Accounting to General Ledger for the Credit Loss Allowance Analysis (step Transfer Value Adjustment and Analyze Credit Loss Allowances), calculation type needs to be set as 09 for specific valuation area via SSCUI: Define Valuation Areas for Receivables Adjustments (102194).

#### Create Flat-Rate Value Adjustments According to Expected Credit Loss Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can make a flat-rate value adjustment of all receivables due and not yet due depending on the risk class and age grid of the receivables through mass run.

|  |
| --- |
| Note You have to maintain risk class for business partner. |

Prerequisites

1. To maintain Risk Class (for example, C) for business partner, refer to the test script of scope item 2ARContract Accounting – Master Data and Basic Functions, chapter Create a Business Partner.
2. To note down the Semantic Tag, access SSCUI via: Finance > General Ledger > Ledgers and Valuation > Define Rules for Impairment (105452).

Select the Valuation Rule under Define Rules for Impairment, double-click the folder Define Steps of an Impairment Rule and then select the Valuation Rule Step. Next, double-click the folder Assign Semantic Tag to Impairment Rule and note down the Semantic Tag in the Filter Condition column.

1. To maintain the Probability of Default, access SSCUI via: Finance > General Ledger > Ledgers and Valuation > Define Rules for Impairment (105452).

Select the Valuation Rule under Define Rules for Impairment, double-click the folder Define Steps of an Impairment Rule and then select the Valuation Rule Step. Next, double-click the folder Assign Probability of Default to Aging Increment and maintain the Probability of Default.

1. To note down Financial Statement Versions (for example, corresponding financial statement version) with corresponding Accounting Principle (for example, USGP), access SSCUI via: Finance > General Ledger > Ledgers and Valuation > Assign Financial Statement Versions to Accounting Principles (103215).
2. To assign Valuation Rule (for example, SCRI) to the corresponding Accounting Principle, access configuration activity via: Finance > General Ledger > Assign Rules for Impairment to Accounting Principles (105453) .
3. To assign Account (for example, 12100200) under Semantic Tag (for example, ACCREC), access SSCUI via: Finance > General Ledger > Ledgers and Valuation > Assign Semantic Tags to Financial Statement Versions (102659).

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Rules for Impairment | Search with following criteria:Application Area: FinanceSub Application Area: General LedgerFor the row with Item Name of Ledgers and Valuation, choose Details (>).For the Define Rules for Impairment row, choose Configure. | The Change View "Define Rules for Impairment": Overview screen is displayed. |  |
| 4 |  | Select the Valuation Rule and Double-click the folder Define Steps of an Impairement Rule.Make the following entries:Valuation Rule: SCRIValuation Rule Step: 0010 |  |  |
| 5 | Maintain Entries on Assign Probability of Default to Aging Increment | Maintain the probability of default.Double-click the folder Assign Probability of Default to Aging Increment.Maintain entries on Probability of Default to Aging Increment for each combination of aging increment and risk class.(For example, Overdue < 30 Days, Risk class C, Probability of Default 5%).Save the entry. | The Change View "Assign Probability of Default to Aging Increment": Overview screen is displayed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Define Rules for Impairment | Go to the Business Processes Configuration app and search for the following activity: Define Rules for Impairment.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Define Rules for Impairment": Overview screen is displayed. |  |
| 3 | Input Parameters | Make the following entries:Valuation Rule: SCRIValuation Rule Step: 0010 |  |  |
| 4 | Maintain Entries on Assign Probability of Default to Aging Increment | Double click on folder Assign Probability of Default to Aging Increment.Maintain entries on Assign Probability of Default to Aging Increment for each combination of risk class and aging increment.(For example, Overdue < 30 Days, Risk class C, Probability of Default 5%).Save the entry. |  |  |

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access SSCUI Assign Semantic Tags to Financial Statement Versions | Search with following criteria:Application Area: FinanceSub Application Area: General LedgerFor the row with Item Name of Ledgers and Valuation, choose Details (>).For the Assign Semantic Tags to Financial Statement Versions row, choose Configure. | The Change View "Mapping of Financial Statement Version to S..": Overview screen is displayed. |  |
| 4 | Add New Entries | Choose New Entries and select Assign Semantic Tags to G/L account.FS Version: <Corresponding financial statement version>Account From: 12100200Semantic Tag: ACCRECSave the entry. |  |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Assign Semantic Tags to Financial Statement Versions | Go to the Business Processes Configuration app and search for the following activity: Assign Semantic Tags to Financial Statement Versions.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The Change View "Mapping of Financial Statement Version to S..": Overview screen is displayed. |  |
| 3 | Add New Entries | Choose New Entries and select Assign Semantic Tags for G/L account.Choose an assignment type.FS Version: <Corresponding financial statement version>Account From: 12100200Semantic Tag: ACCRECSave the entry. |  |  |

1. Before executing the procedures below, make sure open item is overdue < 30 days (see Preliminary Step > Post Document).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Administrator - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Adjust Receivables According To Age (F3535). | The Application Jobs screen is displayed. |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Adjust Receivables by AgeJob Name: FI-CA: Adjust Receivables by Age |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Basic Parameters | Make the following entries:Run Identification:Prefix of Run ID: For example, ID0Simulation: UnselectGeneral Selections:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310Selection type:Open Items: SelectDate:Selection Date: <last day of the month>Posting Date: <last day of the month>Note If Transfer Value Adjustment will be executed, set Posting Date as the last day of fiscal period.Value Adjustment Reason:Adjustment Reason: 01Valuation Area: SUVFlat-Rate Value Ajust.: SelectNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
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

In this activity, you can mark receivables as doubtful or make individual value adjustments.

You can adjust the value in one of the following ways:

- Using a percentage rate that you can define as needed
- Using a specified adjustment amount

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Adjust Receivables (FPZW). | The Adjust Receivables: Initial Screen is displayed. |  |
| 3 | Enter Selection Details | Business Partner: <Business Partner number with open items>Contract Account: <Contract Account number with open items>Currency: AED |  |  |
| 4 | Enter Valuation Area | Valuation Area: SUV |  |  |
| 5 | Make Correction | Choose Make Correction. | The Adjust Receivables: Execute screen is displayed. |  |
| 6 | Select Open Items | Select the open item in the Open Items section. |  |  |
| 7 | Execute | Execute Individual Value Adjustment. | The Adjust Receivables: Execute screen is displayed. |  |
| 8 | Maintain Value | Modify Reason or IVA Percentage Rate as required. |  |  |
| 9 | Save | Execute Save. |  |  |

#### Create Doubtful Receivables and Individual Value Adjustments according to Age

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, receivables can be set to doubtful automatically and individual value adjustments can be made on the basis of their age through mass run.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Adjust Receivables According To Age (F3535). | The Application Jobs screen is displayed. |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Adjust Receivables by AgeJob Name: FI-CA: Adjust Receivables by Age |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Basic Parameters | Make the following entries:Run Identification:Run ID Prefix: For example, ID0Simulation: UnselectGeneral Selections:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: 3310Date:Selection Date: <last day of the month>Posting Date: <last day of the month>Note If Transfer Value Adjustment will be executed, set Posting Date as the last day of fiscal period.Value Adjustment Reasons:Adjustment reason: 01Value adj. vari: S001Valuation Area: SUVStatic Individual Value Ajust.: SelectNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
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

You can use this mass activity to post cumulative adjusted and doubtful receivables.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Value Adjustments (F3539). | The Application Jobs screen is displayed. |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: FI-CA: Repost Corrected ReceivablesJob Name: FI-CA: Repost Corrected Receivables |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Basic Parameters | Make the following entries:Run Identification:Run ID Prefix: For example, ID0Simulation: UnselectGeneral Selections:Business Partner: <Business Partner number>Contract Account: <Contract Account number>Company Code: <Company Code>Valuation Area: SUVPosting and Selection Date: <last day of the month>Note In this activity, you analyze reconciliation of the loss allowance for receivables for Contract Accounting (from opening to closing balances).A table shows the changes during the period using a simplified Expected Credit Loss model.Document Date: <last day of the month>Create Transfer Posting Docs for Section:Doubtful Entry: SelectIndividual Value Adjustment : SelectNote The Dynamic Date Function is available for parameters of date, you can also use the Dynamic Date Function with the Define Recurrence Pattern to set up the recurring run for mass activity to meet your business needs. For example, you can choose the dynamic date function TODAY for testing purpose. |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors.The Run Identification should combine Run ID Prefix + dynamic number (xx). |  |

#### Display Value Adjustments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can display the adjusted receivables.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Accounts Payable and Receivable Accountant (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Posted Value Adjustments (F4824). | The screen Display Receivables Adjustments Transferred is displayed. |  |
| 3 | Enter Search Criteria | Make the following entries:Key Date : <Select a Date>Valuation Area: SUV |  |  |
| 4 | Execute | Choose Execute. | The screen Display Receivables Adjustments Transferred is displayed. The adjusted receivables are listed. |  |

#### Transfer Value Adjustments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can transfer Value Adjustments from Contract Accounting to General Ledger for the Credit Loss Allowance Analysis preparation.

|  |
| --- |
| Note Calculation type needs set to 09 for specific valuation area via SSCUI Define Valuation Areas for Receivables Adjustments (102194) to transfer Individual Value Adjustments. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Administrator - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Prepare Value Adjustment Analysis (F3843). |  |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Basic Parameters | Make the following entries and choose Step 2:Job Template: Transfer Value AdjustmentJob Name: Transfer Value Adjustment |  |  |
| 5 | Enter Basic Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Basic Parameters | Make the following entries:Run Identification:Run ID Prefix: For example, ID0Simulation: UnselectGeneral Selections:Business Partner: <Business Partner number>Company Code: <Company Code>Key Date: <for example, last day of current month>Valuation Area: SUV |  |  |
| 7 | Check Job | Choose Check. | System message You can go ahead and schedule the job is displayed. Recon. Key is generated by system automatically. |  |
| 8 | Execute Job | Choose Schedule. | The Application Jobs screen is displayed.One new application job is created with a status. |  |
| 9 | Check Job Status | After the job has been finished, choose the arrow button at the end of the entry to navigate to the job details. | The Job Log screen is displayed. The log should show no errors. |  |

#### Analyze Credit Loss Allowances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you analyze reconciliation of the loss allowance for receivables for Contract Accounting (from opening to closing balances).

The procedure below shows the changes during the period using a simplified Expected Credit Loss model.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as General Ledger Accountant role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Analyze Credit Loss Allowances (W0134). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Ledger: 3L for leading ledger with US GAAPCompany Code: 3310Fiscal Year: <select fiscal year>To Period: <select period>Currency Type: <select currency type> | The credit loss allowance is shown. |  |

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

In this activity, you can valuate foreign currencies in contract accounts to adjust the receivable and payable accounts as part of balance sheet preparations.

The valuation posting is automatically reset one day after the financial statement key date.

Prerequisites

You must post open document using a foreign currency when the exchange rate at the time of the posting is different from the exchange rate at the month end (when you execute the foreign currency valuation). Open items must be available in a foreign currency and posted with a higher or lower exchange rate that is currently applicable. To post document in a foreign currency, you can use SAP Fiori app Post Document (FPE1) to change the exchange rate in detail.

To see the exchange rates, you can either useSAP Fiori app Maintain Exchange Rates (OB08) or enter the exchange rate manually in the document you are posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Execute Foreign Currency Valuation (FPW1).Note Use SAP Fiori app Execute Foreign Currency Valuation (FPW1) for a small number of open receivables in foreign currencies.Use SAP Fiori app Foreign Currency Valuation Run (F5985) and select job template Foreign Currency Valuation Run for a large number of open receivables in foreign currencies.If error occurs when you use SAP Fiori app Foreign Currency Valuation Run (F5985), access SAP Fiori app Foreign Currency Valuation Run (F5985) and select job template Repeat Posting of Foreign Currency Valuation Run.Lock exists if you run FPW1/FPW1M/FPW1P in parallel, as parallel posting runs are not allowed. |  |  |
| 3 | Enter General Selections | Make the following entry:Balance sheet key date: <last date of current quarter>Ledger: 3LCompany Code: <select specific company code>, for example 3310Note Please don't leave this field blank. |  |  |
| 4 | Further Selections | Valuation Variant: <for example, SUV> |  |  |
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

In this activity, you can display foreign currency valuations that have been carried out or reversed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Display Foreign Currency Valuations (FPW2). |  |  |
| 3 | Enter Selection Criteria | Make the following entry:Company Code: 3310Ledger: <Ledger group number, 3L for US GAAP Ledger only>Flag one of the following 3 options, for example, No Reversed Valuations.No Reversed ValuationsWith Reversed ValuationsOnly Reversed Valuations |  |  |
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

As alternative way for foreign currency valuation, deferred inverse posting can be triggered by one of the following events:

- Clearing
- Reversal
- Clearing Reset

Prerequisite

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

1. Maintain Key Date for Valuation Plan Variant

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Configuration Expert - Business Process Configuration role assigned. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Define Valuation Plan Variants | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Foreign Currency Valuation, choose Details (>).For the Define Valuation Plan Variants row, choose Configure.Valuation Plan Variant: S1Key Date: <last date of the current month and last date of the next month> | The Change View screen is displayed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Basic Settings | Go to the Business Processes Configuration app and search for the following activity: Define Valuation Plan Variants.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Maintain Key Dates for Valuation Plan Variants | Valuation Plan Variant: S1Key Date: <last date of the current month and last date of the next month> | The Change View screen is displayed. |  |

1. Maintain Valuation Plan Variant to Company Code

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

1. Deferred Inverse Posting Setting

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

1. Execute foreign currency valuation on key date 1, for example, end of January (refer to the step [Foreign Currency Valuation](#unique_16) [page ] 25).
2. One of valuated documents is cleared/opened by the following events which is later than key date 1:
    - Reversal (refer to scope item 2BIContract Accounting – Customer Initiated Payments, Appendix > Reverse Document)
    - Clearing Reset (refer to scope item 2UJContract Accounting – Open Item Management, Appendix > Reset Cleared Items)
    - Clearing (refer to scope item 2DPContract Accounting – Company Initiated Payments, step Execute Payment Run)
3. Execute deferred inverse posting:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Deferred Inverse Posting (FPW3). |  |  |
| 3 | Enter General Selections | Make the following entry:Company Code: 3310Ledger: 3L |  |  |
| 4 | Posting Parameters | Simulation Mode: not selected |  |  |
| 5 | Execute | Choose Execute. | The List of Inverse Postings screen is displayed. |  |

1. Execute foreign currency valuation on key date 2, for example, end of February (refer to the step [Foreign Currency Valuation](#unique_16) [page ] 25).

#### Clear Foreign Currency Document (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

When a document in foreign currency is cleared by payment, write-offs or reversal, system posts realized gains or losses from exchange rate differences.

Procedure

1. To post document in a foreign currency, you can use SAP Fiori app Post Document (FPE1) to change the exchange rate in the item detail. Please refer to Preliminary Step - Post Documents.
2. To clear foreign currency document (for example, cleared by payment), follow the steps below.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable and Receivable Accountant (FI-CA). |  |  |
| 2 | Access App | Open Process Payment Lot (FP05). | Payment Lot: Initial Screen displays. |  |
| 3 | Input Parameters for Payment Lot | Choose Create.Lot: <your payment lot ID>Make the following entries on the Payment Lot Create: Default Entries and Status screen:Control Information:Lot: <your payment lot ID>Search Term: <input your search information>Additional Info: <input your specific information>Specifications for Posting Documents:Document Type: <by default>Posting Date: <by default>Document Date: <by default>Reconciliation Key: <generated by the system>Currency: AEDSpecification for Posting Items on Bank Clearing Account:Bank Clearing Account: 11001080Company Code: 3310Value Date: <today's date>Selections for Selecting and Clearing Open Items:Clearing Reason: <01, by default>Selection Category: <by default>Line Layout: SAPChoose New Items.On the Payment Lot Create: Payments screen, check and make the following entries:In the Default Value and Status section: <values are maintained by default>In the Payments section:Payment Amount: <input the amount>Selection Category: BNote Category B stands for Document.If parameters you input are in accordance with the open items, the payment lot can clear open items of specific business partner, otherwise, it needs further clarification.Selection Value 1: <input your document generated in the Create Cash Deposit Request step>Click Save. | Payment lot is created. |  |
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

When a document in foreign currency are posted value adjustments (refer to step [Create Doubtful Receivables and Individual Value Adjustments according to Age](#unique_11) [page ] 17/[Post Value Adjustments](#unique_12) [page ] 19) and then cleared, system resets the value adjustment amount and posts the exchange rate differences due to fluctuations.

Activate the function of clearing foreign currency invoice in value adjustment, you have to maintain the prerequisite below:

Prerequisite

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

Define Valuation Areas for Receivables Adjustments (SSCUI: 102194)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App Manage Your Solution | Open Manage Your Solution and then choose Configure Your Solution. | The Manage Your Solution screen is displayed. |  |
| 3 | Access App Configure Basic Settings | Search with following criteria:Application Area: FinanceSub Application Area: Contract AccountingFor the row with Item Name of Doubtful Receivables and Value Adjustments, choose Details (>).For the Define Valuation Areas for Receivables Adjustments row, choose Configure.Company Code: 3310Valuation Area: SUVExchange Rate: Choose Yes | The Change View screen is displayed. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Configure Define Valuation Areas for Receivables Adjustments | Go to the Business Processes Configuration app and search for the following activity: Define Valuation Areas for Receivables Adjustments.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 3 | Maintain Define Valuation Areas for Receivables Adjustments | Company Code: 3310Valuation Area: SUVExchange Rate: Choose Yes |  |  |

Procedure

1. To post document in a foreign currency, you can use SAP Fiori app Post Document (FPE1) to change the exchange rate in the item detail. Please refer to Preliminary Step - [Post Documents](#unique_7) [page ] 6.
2. You can post individual value adjustments by following the step [Create Doubtful Receivables and Individual Value Adjustments according to Age](#unique_11) [page ] 17/[Post Value Adjustments](#unique_12) [page ] 19 .
3. You can clear foreign currency document (for example, cleared by write-offs) by following step Write Off Items or Write Off Items - Mass Run in test script of scope item 2BIContract Accounting – Customer Initiated Payments.
4. You can reset value adjustment when a document in foreign currency is cleared by following the step [Create Doubtful Receivables and Individual Value Adjustments according to Age](#unique_11) [page ] 17/[Post Value Adjustments](#unique_12) [page ] 19).

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

In this activity, system checks the balance of open items for a business partner per company code and reclassify account receivable with credit balance and account payable with debit balance.

Prerequisites

To reclassify accounts receivable with a credit balance, you need to carry out two prerequisite steps as below:

1. Access SSCUI (102513): Define Receivables and Payables Accounts - maintain G/L account 12100200, select Debit (pre-delivered content).
2. Make the balance of opens items for a business partner result in a credit balance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Creation Run Open Item List for Key Date (F3538). |  |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: Open Item List for Key DateJob Name: Open Item List for Key Date |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Setting section:Run ID Prefix: <for example, ID0>Ignore Clearing History: UnselectIn the General Selections section:Key Date: <last date of current month>Ledger: 3LNote Don't leave the Ledger field blank.In the Grouping and Total Levels section:Grouping at Level 1:2: Partner:-Totals at Level 1:2: Company Code:-In the Output Options - Due Dates section:Statement Due Date Grid: UnselectIn the Output Options - Reclassification section:Regrouping statement: SelectName for Export: <give any name> |  |  |
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

In this activity, you can make automatic adjustment postings for account receivable with credit balances and account payable with debit balances in Contract Accounts Receivable and Payable.

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

In this activity, system checks the balance of open items which have due date more than 1 year for a business partner per company code and reclassify account receivable with credit balance and account payable with debit balance.

Prerequisites

To reclassify accounts receivable with a credit balance, you need to carry out the following prerequisite steps:

1. Access SSCUI (102513): Define Receivables and Payables Accounts - maintain G/L account 12100200, select Debit (pre-delivered content).
2. Make the balance of opens items which have due date more than 1 year for a business partner result in a credit balance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA). |  |  |
| 2 | Access App | Open Creation Run Open Item List for Key Date (F3538). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job view displays. |  |
| 4 | Enter Posting Parameters | Make the following entries and choose Step 2:Job Template: Open Item List for Key DateJob Name: Open Item List for Key Date |  |  |
| 5 | Enter Posting Parameters | Make the following entry and choose Step 3:Start Immediately: Select |  |  |
| 6 | Enter Posting Parameters | Make the following entries:In the Run Setting section:Prefix of Run ID For example, ID0Ignore Clearing History: UnselectIn the General selections:Key date: <last date of current month>Ledger: 3LNote Don't leave the Ledger field blank.In the Grouping and Total Levels sections:Grouping at Level 1:2: Partner:-Totals at Level 1:2: Company Code:-In the Output Options - Due Dates section:Statement Due Date Grid: SelectGrid Interval in days: -365Name for Export: <give any name> |  |  |
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

According to some accounting principles, you are required to display receivables separately if they have a due date longer than one year in the future. You can create and post the adjustments that are necessary for open items as part of closing operations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your user credentials as Reconciliation Specialist - Accounts Payable and Receivable (FI-CA) role assigned. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Post Reclassifications by Due Date (FPRECL_DUEGRID). | The Post Reclassifications by Due Date screen is displayed. |  |
| 3 | Select Posting | In the left panel structure, expand the target folders and double-click the posting document. | On the right side of the screen, you can see status and other details of the export data.If the posting has already been executed, you can see data of the posted document.If the posting has not been executed yet, system generates a posting proposal, provided no errors are determined during the export. If an error sign displays, you cannot execute the posting. |  |
| 4 | Execute | Choose Save. | Two documents are created: one for reclassification and the other for reversal on the day after the key date. |  |

### Day-End Closing

#### Close Reconciliation Keys

Context

In previous steps, you have completed postings to Reconciliation Key. In this activity, you close the Reconciliation Keys so that the total records can be transferred to General Ledger. To do so, refer to the test script of scope item 2BK Contract Accounting – Daily and Monthly Closing, chapter Close Reconciliation Keys.

#### Transfer FI-CA Total Records to General Ledger

Context

In previous step, you have closed the Reconciliation Keys. In this activity, you transfer the total records in Contract Accounts Receivable and Payable to General Ledger. To do so, refer to the test script of scope item 2BK Contract Accounting – Daily and Monthly Closing, chapter Transfer FI-CA Total Records to General Ledger.

### Month-End Closing

#### Close Previous Accounting Period

Context

In this activity, you can close previous posting period. To do so, refer to the test script of scope item 2BK Contract Accounting – Daily and Monthly Closing, chapter Close Previous Accounting Period.

#### Reconcile Open Items with G/L

Context

In this activity, you can check the reconciliation between open items and General Ledger. To do so, refer to the test script of scope item 2BK Contract Accounting – Daily and Monthly Closing, chapter Reconcile Open Items with G/L.

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
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-daily-and-monthly-closing-2bk-ae-812]]
- related-to :: [[09-subscription-billing-and-contract-accounting/test-script-contract-accounting-group-ledger-ifrs-33x-ae-905]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33V_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 69,649 chars in the whole document
