---
id: 03-financial-accounting-and-close/test-script-receivables-financing-with-taulia-7dx-ae-1214
title: "Test Script: Receivables Financing with Taulia (7DX_AE) (7DX_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script (7DX_AE, 2608) for Taulia receivables financing: prerequisites, config steps, Non-Dominion and Cash Dominion test procedures."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/receivables-financing-taulia]
aliases: [7DX_S4CLD2608_BPD_EN_AE]
keywords: [Receivables and Payables Financing with Taulia, receivables financing, taulia platform, non-dominion financing, cash dominion financing, financing agreements, financing documents, funder prepayment, bank statement reprocessing, number range intervals]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DX_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1214
topic: 03-financial-accounting-and-close/receivables-financing-taulia
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Receivables Financing with Taulia (7DX_AE) (7DX_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DX_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Receivables and Payables Financing with Taulia** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Receivables Financing with Taulia (7DX_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860242)

[2 Prerequisites 4](#_Toc232860243)

[2.1 System Access 4](#_Toc232860244)

[2.2 Roles 4](#_Toc232860245)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232860246)

[2.4 Business Conditions 7](#_Toc232860247)

[2.5 Additional Manual Configuration 8](#_Toc232860248)

[2.6 Preliminary Steps 8](#_Toc232860249)

[2.6.1 Define Number Range Intervals for Receivables Financing Agreements (Optional) 8](#_Toc232860250)

[2.6.2 Define Number Range Intervals for Receivables Financing Documents (Optional) 9](#_Toc232860251)

[2.6.3 Define Funder Account Assignment Groups (Optional) 10](#_Toc232860252)

[2.6.4 Define G/L Accounts for Offset Postings (Optional) 11](#_Toc232860253)

[2.6.5 Define G/L Accounts for Receivables Financing Documents (Optional) 12](#_Toc232860254)

[2.6.6 Define General Ledger Account for Payments in Transit (Optional) 13](#_Toc232860255)

[2.6.7 Bank Relationship Contract Types 14](#_Toc232860256)

[2.6.8 Create Bank and Bank Account 15](#_Toc232860257)

[3 Overview Table 17](#_Toc232860258)

[4 Test Procedures 19](#_Toc232860259)

[4.1 Non-Dominion Financing 19](#_Toc232860260)

[4.1.1 Create Financing Agreements 19](#_Toc232860261)

[4.1.2 Manage Receivable Financing Documents 20](#_Toc232860262)

[4.1.3 Prepayment from Funder to Financing Document 21](#_Toc232860263)

[4.1.4 Customer Incoming Payment for Receivable Items 22](#_Toc232860264)

[4.1.5 Check Settled Financing Document 23](#_Toc232860265)

[4.1.6 Repayment to Funder 24](#_Toc232860266)

[4.2 Cash Dominion Financing 24](#_Toc232860267)

[4.2.1 Create Financing Agreements 24](#_Toc232860268)

[4.2.2 Manage Receivables Financing Documents 26](#_Toc232860269)

[4.2.3 Prepayment from Funder to Financing Document 27](#_Toc232860270)

[4.2.4 Review or Reprocess Bank Statement for Receivables Invoice Clearing 28](#_Toc232860271)

[4.2.5 Check Settled Financing Document 28](#_Toc232860272)

[4.2.6 Post Incoming Payments 29](#_Toc232860273)

## Purpose

Overview

Taulia Receivables Financing gives you the ability to finance your receivable invoices with a diverse network of funders directly through the Taulia platform. You will gain unparalleled flexibility with the ability to finance individual invoices as needed. The delivered automated reconciliation will streamline your processes with the end-to-end automated process from financing, to repayment to the funder.

Financing of invoices requires an agreement with Taulia.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad and Taulia Network UI. Your system administrator provides you with the URL to access the various apps assigned to your role. |
| Taulia Platform | Set up and integrated with SAP S/4HANA Public Cloud systemContact the Taulia System Administrator to get logon credentials or create an internal incident for component BNS-TAU-WCM to request a user.Caution An additional license is required for Taulia Platform (Taulia Network UI). |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, see How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/87807ffd176c4dbca23d97ff1ec0705c.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable - Payables Financing Orders | SAP_FIN_BC_AP_PFO_DOC_PROC_PC |  |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Accounts Receivable Accountant | SAP_BR_AR_ACCOUNTANT | Accounts Receivable | SAP_BR_AR_ACCOUNTANT |  |
| Accounts Receivable Manager | SAP_BR_AR_MANAGER | Accounts Receivable | SAP_BR_AR_MANAGER |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

The business process is enabled with organization-specific master data. Examples are provided in the following table.

Operational Focus

SAP delivers standard values for more than one operational focus area, such as Services, Manufacturing, or Trade. You may find more than one master data table. Use the master data that matches the operational focus of your company (Services, Manufacturing, or Trade).

|  |
| --- |
| Note Additional Default ValuesYou can test the scenario with other SAP default values that have the same characteristics. |

Use the following master data in the process steps described in this document:

You've entered the master data required to go through the procedures of this scenario. Ensure that the following scenario-specific master data exists before you test this scenario.

Master Data

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Controlling Area | A000 |  |  |
| Cost Center | 33101101 |  |  |
| House Bank | AEBK1 (for Non-Dominion Financing)AERF1 (for Cash Dominion Financing) |  |  |
| Account ID | AEAC2 (for Non-Dominion Financing)AERFA (for Cash Dominion Financing) |  |  |
| Supplier | 33300026 Funder (for Non-Dominion Financing)33300027 Funder (for Cash Dominion Financing) |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

| Master Data ID | Description |
| --- | --- |
| BND | Create Customer Master - MDS |
| BNE | Create Supplier Master - MDS |
| BNF | Create Product Master of type "Trading Good" - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |

### Business Conditions

| Test Script/Scenario | Business Condition |
| --- | --- |
| BD9 - Sell from Stock | Run this scenario before this test script. |
| J59 - Accounts Receivable | Run this scenario before this test script. |
| BFA - Basic Bank Account Management | Bank account master data is processed. |
| BFB - Basic Cash Operations | Outgoing payment to vendors is integrated with a bank. |
| J77 - Advanced Bank Account Management | Bank accounts and approvers in banks are defined. |
| J78 - Advanced Cash Operations | Preliminary steps in the Prerequisites chapter are performed.Payment approvers are defined. Outgoing Payment with Bank Communication Management (BCM) process is performed. |
| J58 - Accounting and Financial Close | Posting periods are open. |
| J60 – Accounts Payable | Preliminary steps in the Prerequisites chapter are performed. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/0236bbe90c5fa6309c674654103bdea4)

### Preliminary Steps

#### Define Number Range Intervals for Receivables Financing Agreements (Optional)

Purpose

In this optional activity, you define number range intervals. We deliver number range 00 through 2035. If you wish to define your own number ranges, you can perform this activity.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Accounts Receivable

1. For the row with Item Name of Receivables Financing, choose Details (>).
2. For the Define Number Range Intervals for Receivables Financing Agreements row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Number Range Intervals for Receivables Financing Agreements.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Intervals | Choose Edit Intervals. |  |  |
| 2 | Make Changes | Make sure you are in change mode.To change the number ranges, update the values in the From Number and To Number fields.To change the number range status, choose the Change Number Range Status button, and make any necessary changes in the Number Range Status field.When you are done, choose Save. |  |  |

#### Define Number Range Intervals for Receivables Financing Documents (Optional)

Purpose

In this optional activity, you define number range intervals. We deliver number range 00 through 2035. If you wish to define your own number ranges, you can perform this activity.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Accounts Receivable

1. For the row with Item Name of Receivables Financing, choose Details (>).
2. For the Define Number Range Intervals for Receivables Financing Documents row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Number Range Intervals for Receivables Financing Documents.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Intervals | In the Company Code field, enter your company code.Choose Edit Intervals. |  |  |
| 2 | Make Changes | Make sure you are in change mode.To change the number ranges, update the values in the From Number and To Number fields.To change the number range status, choose the Change Number Range Status button, and make any necessary changes in the Number Range Status field.When you are done, choose Save. |  |  |

#### Define Funder Account Assignment Groups (Optional)

Purpose

In this optional activity, you define funder account assignment groups. We deliver a default funder group. You can use this activity to define your own.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Accounts Receivable

1. For the row with Item Name of Receivables Financing, choose Details (>).
2. For the Define Funder Account Assignment Groups row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Funder Account Assignment Groups.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 | Enter Details | Make the following entries and choose Save:Funder Account Assignment Group: <funder account assignment group>Funder Account Assignment Group Name: <name for group> |  |  |

#### Define G/L Accounts for Offset Postings (Optional)

Purpose

In this optional activity, you define the G/L accounts for offset postings. We deliver accounts, but you can perform this activity if you want to define your own.

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
2. For the Automatic Account Determination row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Automatic Account Determination.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Area Details | Make the following entries and choose Step 2:Area: Financial AccountingSubarea: Accounts Receivable and Accounts PayableProcess: Define Accounts for Receivables Financing |  |  |
| 2 | Define G/L Accounts for Offset Postings | Choose Define G/L Accounts for Offset Postings. |  |  |
| 3 | Enter Details | Make any changes to the accounts and choose Save. |  |  |

#### Define G/L Accounts for Receivables Financing Documents (Optional)

Purpose

In this optional activity, you define the general ledger accounts for receivables financing documents. We deliver accounts, but you can perform this activity if you want to define your own.

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
2. For the Automatic Account Determination row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Automatic Account Determination.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Area Details | Make the following entries and choose Step 2:Area: Financial AccountingSubarea: Accounts Receivable and Accounts PayableProcess: Define Accounts for Receivables Financing |  |  |
| 2 | Define G/L Accounts for Receivables Financing Documents | Choose Define G/L Accounts for Receivables Financing Documents. |  |  |
| 3 | Enter Details | Make any changes to the accounts and choose Save. |  |  |

#### Define General Ledger Account for Payments in Transit (Optional)

Purpose

In this activity, you define the general ledger account for payments in transit.

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
2. For the Automatic Account Determination row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Automatic Account Determination.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Area Details | Make the following entries and choose Step 2:Area: Financial AccountingSubarea: Accounts Receivable and Accounts PayableProcess: Define Accounts for Receivables Financing |  |  |
| 2 | Define G/L Accounts for Payments in Transit | Choose Define G/L Accounts for Payments in Transit. |  |  |
| 3 | Enter Details | Make any changes to the accounts and choose Save. |  |  |

#### Bank Relationship Contract Types

Purpose

In this activity, you define the bank relationship contract types.

|  |
| --- |
| Note This preliminary step is only for productive systems, not internal, demo, or starter systems. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Cash and Liquidity Management

1. For the row with Item Name of General Settings, choose Details (>).
2. For the Define Basic Settings row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Basic Settings.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Enter Details | Make the following entries and choose Save:Cash Scope: Full ScopeBank Relationship Management section:Enable Bank Account Contract Types: Selected |  |  |

#### Create Bank and Bank Account

Purpose

In this step, you create standard banks and internal bank master data with general information. You also create bank accounts.

|  |
| --- |
| Note This preliminary step is only for productive systems, not internal, demo, or starter systems. |

Procedure

For more information on setting up banks, see the Basic Bank Account Management (BFA) test script.

| Process Step | Fiori App | Values to Use | Comments |
| --- | --- | --- | --- |
| Test Procedures > Bank Account Master Data Processing with Basic Bank Account Management > Using Direct Revision Activate → Create Bank Account > Create Bank Master Data | Manage Banks - Master Data (F6437)Caution Choose Create Internal Bank. | Bank Key:<use your own bank key>Internal Bank Category: Technical Bank (9)Bank Name: <use your own bank name> |  |
| Test Procedures > Bank Account Master Data Processing with Basic Bank Account Management > Using Direct Revision Activate → Create Bank Account > Manage Banks Cash Management Data | Manage Banks - Cash Management (F1574A) | Use the Bank Key value above.Under House Banks, choose CreateCompany Code: <company code>House Bank: <house bank> |  |
| Test Procedures > Bank Account Master Data Processing with Basic Bank Account Management > Using Direct Revision Activate → Create Bank Account > Create Bank Account | Manage Bank Accounts (F1366A) | Choose Create. Enter your company code and Account Type: 21 (Working Capital Account) and choose Continue.Account Description: <account description>Use the Bank Key value above.Use a valid value for Account Number.Under House Bank Connectivity, choose Create.House Bank Account: <house bank account>G/L Account: <G/L account> |  |

## Overview Table

The Receivables Financing with Taulia scenario consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Non-Dominion Financing

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Financing Agreements](#unique_17) [page ] 19 | Accounts Receivable Manager | Manage Receivables Financing Agreements (F8158) | You created financing agreements. |
| [Manage Receivable Financing Documents](#unique_18) [page ] 20 | Accounts Receivable Accountant | Manage Receivables Financing Documents (F7983) | You checked the receivable financing documents. |
| [Prepayment from Funder to Financing Document](#unique_19) [page ] 21 | Perform the activities mentioned in the step from the Accounts Receivable (J59) test script, using the roles mentioned in that script. | Perform the activities mentioned in the step from the Accounts Receivable (J59) test script. | You handled the prepayment from the funder. |
| [Customer Incoming Payment for Receivable Items](#unique_20) [page ] 22 | Perform the activities mentioned in the step from the Accounts Receivable (J59) test script, using the roles mentioned in that script. | Perform the activities mentioned in the step from the Accounts Receivable (J59) test script. | You processed the customer incoming payment. |
| [Check Settled Financing Document](#unique_21) [page ] 23 | Accounts Receivable Accountant | Manage Receivables Financing Documents (F7983) | You checked the settled financing document. |
| [Repayment to Funder](#unique_22) [page ] 24 | Perform the activities mentioned in the step from the Accounts Payable (J60) test script, using the roles mentioned in that script. | Perform the activities mentioned in the step from the Accounts Payable (J60) test script. | You handled repayment to the funder. |

Table 2: Cash Dominion Financing

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Financing Agreements](#unique_23) [page ] 24 | Accounts Receivable Manager | Manage Receivables Financing Agreements (F8158) | You created financing agreements. |
| [Manage Receivables Financing Documents](#unique_24) [page ] 26 | Accounts Receivable Accountant | Manage Receivables Financing Documents (F7983) | You checked the receivable financing documents. |
| [Prepayment from Funder to Financing Document](#unique_25) [page ] 27 | Perform the activities mentioned in the step from the Accounts Receivable (J59) test script, using the roles mentioned in that script. | Perform the activities mentioned in the step from the Accounts Receivable (J59) test script. | You handled the prepayment from the funder. |
| [Review or Reprocess Bank Statement for Receivables Invoice Clearing](#unique_26) [page ] 28 |  | This is an automated process. | You reprocessed the bank statement. |
| [Check Settled Financing Document](#unique_27) [page ] 28 | Accounts Receivable Accountant | Manage Receivables Financing Documents (F7983) | You checked the settled financing document. |
| [Post Incoming Payments](#unique_28) [page ] 29 |  | This is an automated process. | You posted incoming payments. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Non-Dominion Financing

#### Create Financing Agreements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create financing agreements.

Prerequisites

Open invoices must be available in the system.

|  |
| --- |
| Note For more information, see the [Business Conditions](#unique_6) [page ] 7 topic. Open invoices are created as part of the Accounts Receivable (J59) or Sell from Stock (BD9) test scripts. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Receivables Financing Agreements (F8158). |  |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Details | Make the following entries:Funder: 33300026Valid From: <date>Valid To: <date>Journal Entry Type: <journal entry type>, for example, KAFunder Account Assignment Group: Default Funder GroupFinancing Type: Limited Recourse (True Sale), Non-Dominion, UndisclosedSale Posting Mode: Net (post prepayment deducted by financing fee)Select the VAT checkbox. |  |  |
| 5 | Company Code | In the Account Assignments pane, enter a company code in the Company Code column. |  |  |
| 6 | Create | Choose Create.Caution You can't have the same validity date range for more than one agreement. If an agreement exists with the same validity date range, the system displays an error message during creation. |  |  |
| 7 | Taulia System - Early Payment | To process the request for early payment, perform the steps for Requesting Early Payment on an AR Financing Invoice on the [Taulia Support](https://customersupport.taulia.com/articles/en_US/Agent_Knowledge_Base/AR-Financing-Receivables-Invoices/?q=rece&l=en_US&fs=Search&pn=1) site. When you are done, make a note of the Document Number (customer invoice) for later steps.Note The provided link also contains additional useful information that is not within the scope of this test script. |  |  |

#### Manage Receivable Financing Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the receivable financing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Receivables Financing Documents (F7983). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Company Code: 3310Funder: 33300026Document Status: PostedNote To view other statuses for troubleshooting, do not select any values in the Document Status field. | The Receivables Financing Documents pane shows a filtered list of documents. |  |
| 4 | Enter Details | For a document with the status Posted, choose Navigation (>) at the right of the row. | The document is displayed in a new view. |  |
| 5 | Review | Review the document. You can click the links for the Receivables Item or Receivables Financing Journal Entry to view more details on the related items. When you are done, choose Back. | Make a note of the Receivables Financing Journal Entry number for the next step: __________ |  |

#### Prepayment from Funder to Financing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you process the prepayment from the funder to the financing document.

Procedure

Perform only one of the following activities in the Accounts Receivable (J59) test script:

- Under Incoming Payments without Electronic Bank Statement, run Post Incoming Payments. This is the preferred method for testing.
    - Use Journal Entry Type of KZ (Vendor payment).
    - For Account Type/Account ID, use Supplier and 33300026 Funder.
    - In the Proposed ItemsReceivables Financing Journal Entry pane, clear and post field from the prior step.
- Optional: Under Incoming Payments with Electronic Bank Statement, run Daily Cash Operations - Bank Statement and pane, clear and post the proposed item that has the document number from the Cash Application Intelligence Integration.

#### Customer Incoming Payment for Receivable Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you process the customer incoming payment for the receivable items.

Procedure

Perform only one of the following activities in the Accounts Receivable (J59) test script:

- Under Incoming Payments without Electronic Bank Statement, run Post Incoming Payments. This is the preferred method for testing.
    - Use the full invoice amount.
    - In the Proposed Items pane, clear and post the proposed item that has the document number from the Document Number field from the Taulia interface (mentioned in the last procedure step in the [Create Financing Agreements](#unique_17) [page ] 19 topic). In the Taulia interface, if the Document Number column is not visible, you need to change the layout to make the column visible.
- Optional: Under Incoming Payments with Electronic Bank Statement, run Daily Cash Operations - Bank Statement and Cash Application Intelligence Integration.

#### Check Settled Financing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check for settled financing agreements.

Prerequisites

You have received the prepayment from the funder and the payment from the customer for the invoice amount.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Receivables Financing Documents (F7983). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Company Code: 3310Funder: 33300026Document Status: Funded, Completed | The Receivables Financing Documents pane shows a filtered list of documents.Rows with status of Funded are funded by the funder.Rows with a status of Completed are funded and the customer has paid the full invoice amount. |  |
| 4 | Details for Funded Document | For a document, choose Details (>) at the right of the row. | The document is displayed in a new view. |  |
| 5 | Settle Document | Review the document. You can click the links for the Receivables Item or Receivables Financing Journal Entry to view more details on the related items. When you are done, choose Back. | Make a note of the document number in the Postings pane with the Posting Category that contains Maturity: _________ This is used in the next step. |  |

#### Repayment to Funder

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you process the repayment to the funder .

Procedure

Perform only one of the following activities in the Accounts Payable (J60) test script:

- Under the Manual Payment Online section, perform the Post Outgoing Payment procedure. This is the preferred option for testing.
    - For the supplier, use 33300026 Funder.
    - In the Open AP/AR Items pane, clear and post the journal entry that has the document number that you wrote down in the prior step.
- Optional: Perform all steps under the Payment Run section.
- Optional: Perform all steps under the Single Outgoing Payment section.

### Cash Dominion Financing

#### Create Financing Agreements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create financing agreements.

Prerequisites

Open invoices must be available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Manager. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Receivables Financing Agreements (F8158). |  |  |
| 3 | Create | Choose Create. |  |  |
| 4 | Enter Details | Make the following entries:Funder: 33300027Valid From: <date>Valid To: <date>Journal Entry Type: <journal entry type>, for example, KAFunder Account Assignment Group: Default Funder GroupFinancing Type: Limited Recourse (True Sale), Cash Dominion, DisclosedSale Posting Mode: Net (post prepayment deducted by financing fee)VAT: Selected |  |  |
| 5 | Company Code | In the Account Assignments pane, enter a company code in the Company Code column. |  |  |
| 6 | Create | Choose Create.Caution You can't have the same validity date range for more than one agreement. If an agreement exists with the same validity date range, the system displays an error message during creation. |  |  |
| 7 | Taulia System - Early Payment | To process the request for early payment, perform the steps for Requesting Early Payment on an AR Financing Invoice on the [Taulia Support](https://customersupport.taulia.com/articles/en_US/Agent_Knowledge_Base/AR-Financing-Receivables-Invoices/?q=rece&l=en_US&fs=Search&pn=1) site. When you are done, make a note of the Document Number (customer invoice) for later steps.Note The provided link also contains additional useful information that is not within the scope of this test script. |  |  |

#### Manage Receivables Financing Documents

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the receivable financing documents.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
|  | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
|  | Access the SAP Fiori App | Open Manage Receivables Financing Documents (F7983). |  |  |
|  | Enter Details | Make the following entries and choose Go:Company Code: 3310Funder: 33300027Document Status: PostedNote To view other statuses for troubleshooting, don't select any values in the Document Status field. | The Receivables Financing Documents pane shows a filtered list of documents. |  |
|  | Enter Details | For a document with the status Posted, choose Navigation (>) at the right of the row. | The document is displayed in a new view. |  |
|  | Review | Review the document. You can click the links for the Receivables Item or Receivables Financing Journal Entry to view more details on the related items. When you are done, choose Back. | Make a note of the Receivables Financing Journal Entry number for the next step: __________ |  |

#### Prepayment from Funder to Financing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you process the prepayment from the funder to the financing document.

Procedure

Perform only one of the following activities in the Accounts Receivable (J59) test script:

- Under Incoming Payments without Electronic Bank Statement, run Post Incoming Payments. This is the preferred method for testing.
    - Use Journal Entry Type of KZ (Vendor payment).
    - For Account Type/Account ID, use Supplier and 33300027 Funder.
    - In the Proposed Items > Receivables Financing Journal Entry pane, clear and post the field from the prior step.
- Optional: Under Incoming Payments with Electronic Bank Statement, run Daily Cash Operations - Bank Statement and pane, clear and post the proposed item that has the document number from the Cash Application Intelligence Integration.

#### Review or Reprocess Bank Statement for Receivables Invoice Clearing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review or reprocess the clearing of the receivable item to the funds in transit account. This represents the customer payment to the funder.

Procedure

Once the House Bank and House Bank Account are properly set up, this is an automated process. Data comes from the Taulia platform and contains the reconciliation information.

|  |
| --- |
| Note You only need to perform manual reprocessing if there are errors. For troubleshooting/manual reprocessing, you can use the following apps:Reprocess Bank Statement Items (F1520)Manage Bank Statements (F1564) (to check bank statement status)For more information on these process steps, see Accounts Receivable (J59). |

#### Check Settled Financing Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check for settled financing agreements.

Prerequisites

You have received the prepayment from the funder and the payment from the customer for the invoice amount.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Receivable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Receivables Financing Documents (F7983). |  |  |
| 3 | Enter Details | Make the following entries and choose Go:Company Code: 3310Funder: 33300027Document Status: Funded, Completed | The Receivables Financing Documents pane shows a filtered list of documents.Rows with status of Funded are funded by the funder.Rows with a status of Completed are funded and the customer has paid the full invoice amount. |  |
| 4 | Details for Funded Document | For a document, choose Details (>) at the right of the row. | The document is displayed in a new view. |  |
| 5 | Settle Document | Review the document. You can click the links for the Receivables Item or Receivables Financing Journal Entry to view more details on the related items. When you are done, choose Back. | Make a note of the document number in the Postings pane with the Posting Category that contains Maturity: _________ This is used in the next step. |  |

#### Post Incoming Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post incoming payments.

Procedure

|  |
| --- |
| Note This is an automated process. In the event that you need to work with a retention posting, you can follow the Post Incoming Payments process (under Test Procedures > Incoming Payments > Incoming Payment without Bank Statement ) in Accounts Receivable (J59). |

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
- related-to :: [[03-financial-accounting-and-close/test-script-payables-financing-with-taulia-7mg-ae-1219]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7DX_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 51,704 chars in the whole document
