---
id: 03-financial-accounting-and-close/test-script-payables-financing-with-taulia-7mg-ae-1219
title: "Test Script: Payables Financing with Taulia (7MG_AE) (7MG_S4CLD2608_BPD_EN_AE)"
description: "S/4HANA Cloud Public Edition 2608 (AE) test script, scope item 7MG: Taulia Dynamic Discounting, Supply Chain Finance, Virtual Card; prerequisites and steps."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/receivables-financing-taulia]
aliases: [7MG_S4CLD2608_BPD_EN_AE]
keywords: [Receivables and Payables Financing with Taulia, payables financing, taulia integration, dynamic discounting, supply chain finance, virtual card, early payment requests, financing orders, payment run, business partner master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MG_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1219
topic: 03-financial-accounting-and-close/receivables-financing-taulia
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Payables Financing with Taulia (7MG_AE) (7MG_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MG_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Receivables and Payables Financing with Taulia** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Payables Financing with Taulia (7MG_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860515)

[2 Prerequisites 4](#_Toc232860516)

[2.1 System Access 4](#_Toc232860517)

[2.2 Roles 4](#_Toc232860518)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232860519)

[2.4 Business Conditions 7](#_Toc232860520)

[2.5 Additional Manual Configuration 8](#_Toc232860521)

[2.6 Preliminary Steps 8](#_Toc232860522)

[2.6.1 Activate Transfer of Recievable/Payable Items 8](#_Toc232860523)

[2.6.2 Review Taulia Supplier State 10](#_Toc232860524)

[2.6.3 Define Settings for Dynamic Discount Credit Memos (Optional) 11](#_Toc232860525)

[2.6.4 Activate Credit Memo Attachment for Dynamic Discount 12](#_Toc232860526)

[3 Overview Table 14](#_Toc232860527)

[4 Test Procedures 17](#_Toc232860528)

[4.1 Invoice Entry Without Purchase Order 17](#_Toc232860529)

[4.2 Dynamic Discounting 19](#_Toc232860530)

[4.2.1 Maintain Business Partner for Dynamic Discounting 19](#_Toc232860531)

[4.2.2 Create Early Payment Request for Dynamic Discounting 20](#_Toc232860532)

[4.2.3 Financing Order for Dynamic Discounting 22](#_Toc232860533)

[4.2.3.1 Display Financing Order 22](#_Toc232860534)

[4.2.3.2 Cancel Financing Order 23](#_Toc232860535)

[4.2.4 Payment Run for Dynamic Discounting 24](#_Toc232860536)

[4.2.4.1 Schedule Payment Proposals 24](#_Toc232860537)

[4.2.4.2 Revise Payment Proposal 26](#_Toc232860538)

[4.2.4.3 Release Payment Proposal 28](#_Toc232860539)

[4.2.4.4 Next Steps (Optional) 29](#_Toc232860540)

[4.3 Supply Chain Finance 30](#_Toc232860541)

[4.3.1 Maintain Business Partner for Supply Chain Finance 30](#_Toc232860542)

[4.3.2 Create Early Payment Request for Supply Chain Finance 32](#_Toc232860543)

[4.3.3 Financing Order for Supply Chain Finance 33](#_Toc232860544)

[4.3.3.1 Display Financing Order 33](#_Toc232860545)

[4.3.3.2 Cancel Financing Order 34](#_Toc232860546)

[4.3.4 Payment Run for Supply Chain Finance 35](#_Toc232860547)

[4.3.4.1 Schedule Payment Proposals 35](#_Toc232860548)

[4.3.4.2 Revise Payment Proposal 37](#_Toc232860549)

[4.3.4.3 Release Payment Proposal 39](#_Toc232860550)

[4.3.4.4 Next Steps (Optional) 40](#_Toc232860551)

[4.4 Virtual Card 41](#_Toc232860552)

[4.4.1 Maintain Business Partner 41](#_Toc232860553)

[4.4.1.1 Maintain Business Partner for Virtual Card 41](#_Toc232860554)

[4.4.1.2 Maintain Business Partner for Card Provider 42](#_Toc232860555)

[4.4.2 Create Early Payment Request for Virtual Card 44](#_Toc232860556)

[4.4.3 Financing Order for Virtual Card Supplier 45](#_Toc232860557)

[4.4.3.1 Display Financing Order 45](#_Toc232860558)

[4.4.3.2 Cancel Financing Order 46](#_Toc232860559)

[4.4.4 Payment Run for Virtual Card Supplier 47](#_Toc232860560)

[4.4.4.1 Schedule Payment Proposals 47](#_Toc232860561)

[4.4.4.2 Revise Payment Proposal 49](#_Toc232860562)

[4.4.4.3 Release Payment Proposal 51](#_Toc232860563)

[4.4.5 Invoice Entry Without Purchase Order for Card Provider 52](#_Toc232860564)

[4.4.6 Payment Run for Card Provider 54](#_Toc232860565)

[4.4.6.1 Schedule Payment Proposals 54](#_Toc232860566)

[4.4.6.2 Revise Payment Proposal 56](#_Toc232860567)

[4.4.6.3 Release Payment Proposal 58](#_Toc232860568)

[4.4.6.4 Next Steps (Optional) 59](#_Toc232860569)

[4.4.7 Clear Virtual Card Clearing Account 60](#_Toc232860570)

## Purpose

Overview

Taulia's Payables Financing offers three powerful tools to optimize your working capital and cash flow:

- Dynamic Discounting: Offer early payments to suppliers in exchange for discounts on individual invoices
- Supply Chain Financing: Provide early payments to suppliers using third-party funds, preserving your cash reserves
- Virtual Cards: Simplify supplier payments, reduce fraud risk, and extend your working capital

You can flexibly combine Dynamic Discounting and Supply Chain Financing to control when you use your own cash for discounts versus third-party funds to manage cash flow. This versatile approach allows you to tailor your payment strategy to your current financial needs and goals.

|  |
| --- |
| Caution Credit Memo functionality is not yet available for some countries. The system will issue an error message as intended until the Credit Memo functionality is available. |

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
| Taulia Platform | Set up and integrated with SAP S/4HANA Public Cloud system |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

For more information, see How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/87807ffd176c4dbca23d97ff1ec0705c.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable - Payables Financing Orders | SAP_FIN_BC_AP_PFO_DOC_PROC_PC |  |
| Accounts Payable Accountant | SAP_BR_AP_ACCOUNTANT | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Accounts Payable Manager | SAP_BR_AP_MANAGER | Accounts Payable / Central Invoice Management - Supplier Invoices / Central Invoicing - Supplier Invoice | SAP_BR_AP_ACCOUNTANT / SAP_MM_SPT_CIM_INV_PC / SAP_MM_SPT_CNTRL_INVOICING_PC |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Cash Management Specialist | SAP_BR_CASH_SPECIALIST | Cash Management | SAP_BR_CASH_SPECIALIST |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Manager | SAP_BR_MANAGER | My Inbox | SAP_CORE_SPT_MYINBOX_PC |  |
| Extensibility Specialist | SAP_BR_EXTENSIBILITY_SPEC | Extensibility / Extensibility | SAP_BR_EXTENSIBILITY_SPEC / SAP_CA_SPT_EXT_PC |  |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company was created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

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
| Cost Center | 33101301 |  |  |
| Material Master | * | Material type DIEN, SEMI, HAWA |  |
| House Bank | AEBK1AEBK2 | The AEBK2 value is used for non-MBC payments. Make sure that the solution is installed with demo data if you want to test both banks. |  |
|  | AEVC1 | The AEVC1 value is used for non-MBC payments. Make sure that the solution is installed with demo data if you want to test both banks. |  |
| Account ID | AEAC1 AEAC2USDAC(only for AEBK1) |  |  |
|  | AEVV1 | Account ID for Virtual Card |  |
| VC Clearing G/L Account | 21901000 | Virtual Card Clearing for Accounts Payable Financing |  |
| Supplier | 33300022 SCF33300023 Funder33300024 V.Card33300025 Card Provider |  |  |
| Payment Methods | $ (VCard Payable Financing)T (Bank Transfer)F (Foreign Bank Transfer (DTAZV)) |  |  |

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

Invoices to be paid must be available. You can enter new invoices by performing the purchase process in Material Management.

| Test Script/Scenario | Business Condition |
| --- | --- |
| J45 - Procurement of Direct Materials | Run this scenario before this test script. Invoices are created and posted to accounting. |
| J13 - Service and Material Procurement – Project-Based Services | Run this scenario before this test script. Invoices are created and posted to accounting. |
| BFA - Basic Bank Account Management | Bank account master data is processed. |
| BFB - Basic Cash Operations | Outgoing payment to vendors is integrated with a bank. |
| J77 - Advanced Bank Account Management | Bank accounts and approvers in banks are defined. |
| J78 - Advanced Cash Operations | Preliminary steps in the Prerequisites chapter are performed.Payment approvers are defined. Outgoing Payment with Bank Communication Management (BCM) process is performed. |
| J58 - Accounting and Financial Close | Posting periods are open. |
| J60 – Accounts Payable | Preliminary steps in the Prerequisites chapter are performed. |
| BNZ - Create New Open MM Posting Period - MDS | MM posting periods are open. |
| BNX - Consumable Purchasing | Perform the Activate Flexible Workflow for Supplier Invoice preliminary step. |
| 1LQ - Output Management | Ensure that you set up printers, create a print queue, and/or set up e-mail. These activities are in the Setup Instructions document. |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/077478bc9150c41dd7fd5c19e9df1460)

### Preliminary Steps

#### Activate Transfer of Recievable/Payable Items

Purpose

In this activity, you activate the replication of Accounts Payable and Accounts Receivable items for the Taulia platform.

Prerequisites

The company code is created.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Accounts Payable

1. For the row with Item Name of Payables Financing, choose Details (>).
2. For the Define Company Codes for Receivable Items/Payable Items row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Company Codes for Receivable Items/Payable Items.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Change | Choose Display -> Change to go into change mode. |  |  |
| 2 | New Entries | Choose New Entries. |  |  |
| 3 | Enter Details | Make the following entries and choose Save:Appl: FI-APARCoCd: <company code> | Company code is activated to transfer Receivable/Payable Items. |  |

#### Review Taulia Supplier State

Use

In this activity, you review that suppliers are onboarded and ready for financing.

Prerequisite

Suppliers are onboarded and have enrolled status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log into Taulia Network UI as Buyer, for example:admin@sap-<system>-<client>.comNote:Contact Taulia System Administrator to get logon credentials or create an internal incident for component BNS-TAU-WCM to request a user. |  |  |
| 2 | Supplier Center | Choose Home > Supplier Center . | List of suppliers are displayed. |  |
| 3 | Enrollment State | Look for the suppliers used for testing and check that the column Enrollment State is Enrolled.Click on the supplier’s name to see more details. | Suppliers with Enrollment State of Enrolled are ready to use financing options. |  |
| 4 | Invoices | Choose Payables > Invoices and filter by:Supplier: <Supplier> | A list of invoices of the selected suppliers are displayed showing information such as status, payment, and so on. |  |
| 5 | Data Entry and Search | Make the following entries and choose Go:Paying Company Code: 3310Supplier: <any> | A list of Financing Order IDs is displayed according to your search criteria. |  |
| 6 | Log out | Go to your profile and choose Log out. |  |  |

#### Define Settings for Dynamic Discount Credit Memos (Optional)

Purpose

In this activity, you configure settings for credit memos in dynamic discounting, including defining document types.

|  |
| --- |
| Note This topic is only valid for Germany, and those countries/regions that use the Germany solution. If this does not apply to you, skip this step. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Accounts Payable

1. For the row with Item Name of Payables Financing, choose Details (>).
2. For the Define Settings for Dynamic Discount Credit Memos row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Define Settings for Dynamic Discount Credit Memos.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | New Entries | Choose New Entries. |  |  |
| 2 |  | Make the following entries and choose Save:CoCd: <company code>Type: <document type> |  |  |

#### Activate Credit Memo Attachment for Dynamic Discount

Purpose

In this activity, you configure the settings to activate and enable receipt of attachments of credit memos for Dynamic Discounting.

|  |
| --- |
| Caution This preliminary step only applies for countries/regions that use credit memos in their solution. If your country/region doesn't use credit memos, skip this step. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country or region by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: R&D/Engineering

Sub Application Area: Project Control and Product Development

1. For the row with Item Name of Product Development Foundation, choose Details (>).
2. For the Activate HDM for Attachment Object Type row, choose Configure.
3. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. In the Product-Specific Configuration phase, navigate to the Configuration Activities tab. To locate the activity in the tree view, search for the following activity: Activate HDM for Attachment Object Type.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Activate | In the Dialog Structure, double-click Activate HDM for Attachment Object Type. |  |  |
| 2 | Save | In the right pane, under Activate HDM for Attachment Object Type, make the following entries:Activate HDM for Attachment Object Types column: Journal EntryActivate column: Selected |  |  |
| 3 | Save | Save your entries. |  |  |

## Overview Table

The Payables Financing with Taulia scenario consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Table 1: Invoice Entry Without Purchase Order

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Invoice Entry Without Purchase Order](#unique_13) [page ] 17 | Personalized role based on SAP_BR_AR_ACCOUNTANT | Create Supplier Invoice (F0859) | You entered a supplier invoice. |

Table 2: Dynamic Discounting

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain Business Partner for Dynamic Discounting](#unique_14) [page ] 19 | Master Data Specialist - Business Partner Data | Manage Supplier Master Data (F1053A) | You assigned a default payment method for the dynamic discounting supplier. |
| [Create Early Payment Request for Dynamic Discounting](#unique_15) [page ] 20 | Taulia - Dynamic Discounting Supplier | Invoices > My Invoices | The supplier created an early payment. |
| [Display Financing Order](#unique_16) [page ] 22 | Accounts Payable Accountant | Display Payables Financing Orders (F8343) | You displayed the financing order. |
| [Cancel Financing Order](#unique_17) [page ] 23 | See step details | See step details. | The financing order is canceled. |
| [Schedule Payment Proposals](#unique_18) [page ] 24 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | You selected the invoices to be paid. |
| [Revise Payment Proposal](#unique_19) [page ] 26 | Accounts Payable Accountant | Revise Payment Proposals (F0771) | You reviewed the invoices to be paid. |
| [Release Payment Proposal](#unique_20) [page ] 28 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | You released the payment proposal. |
| [Next Steps (Optional)](#unique_21) [page ] 29 |  | In the topic, perform the steps mentioned from the Accounts Payable (J60) test script. |  |

Table 3: Supply Chain Finance

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain Business Partner for Supply Chain Finance](#unique_22) [page ] 30 | Master Data Specialist - Business Partner Data | Manage Supplier Master Data (F1053A) | You assigned a default payment method for the supply chain finance. |
| [Create Early Payment Request for Supply Chain Finance](#unique_23) [page ] 32 | Taulia - Supply Chain Finance Supplier | Invoices > My Invoices | The supplier created an early payment. |
| [Display Financing Order](#unique_24) [page ] 33 | Accounts Payable Accountant | Display Payables Financing Orders (F8343) | You displayed the financing order. |
| [Cancel Financing Order](#unique_25) [page ] 34 | See step details | See step details. | The financing order is canceled. |
| [Schedule Payment Proposals](#unique_26) [page ] 35 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | You selected the invoices to be paid. |
| [Revise Payment Proposal](#unique_27) [page ] 37 | Accounts Payable Accountant | Revise Payment Proposals (F0771) | You reviewed the invoices to be paid. |
| [Release Payment Proposal](#unique_28) [page ] 39 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | You released the payment proposal. |
| [Next Steps (Optional)](#unique_29) [page ] 40 |  | In the topic, perform the steps mentioned from the Accounts Payable (J60) test script. |  |

Table 4: Virtual Card

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Maintain Business Partner for Virtual Card](#unique_30) [page ] 41 | Master Data Specialist - Business Partner Data | Manage Supplier Master Data (F1053A) | You assigned a default payment method for the virtual card supplier. |
| [Maintain Business Partner for Card Provider](#unique_31) [page ] 42 | Master Data Specialist - Business Partner Data | Manage Supplier Master Data (F1053A) | You assigned a default payment method for the card provider supplier. |
| [Create Early Payment Request for Virtual Card](#unique_32) [page ] 44 | Taulia - Virtual Card Supplier | Invoices > My Invoices | The supplier created an early payment. |
| [Display Financing Order](#unique_33) [page ] 45 | Accounts Payable Accountant | Display Payables Financing Orders (F8343) | You displayed the financing order. |
| [Cancel Financing Order](#unique_34) [page ] 46 | See step details | See step details. | The financing order is canceled. |
| [Schedule Payment Proposals](#unique_35) [page ] 47 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | You selected the invoices to be paid. |
| [Release Payment Proposal](#unique_36) [page ] 51 | Accounts Payable Accountant | Revise Payment Proposals (F0771) | You reviewed the invoices to be paid. |
| [Release Payment Proposal](#unique_36) [page ] 51 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | You released the payment proposal. |
| [Invoice Entry Without Purchase Order for Card Provider](#unique_37) [page ] 52 | Personalized role based on SAP_BR_AR_ACCOUNTANT | Create Supplier Invoice (F0859) | You entered a supplier invoice. |
| [Schedule Payment Proposals](#unique_38) [page ] 54 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | You selected the invoices to be paid. |
| [Revise Payment Proposal](#unique_39) [page ] 56 | Accounts Payable Accountant | Revise Payment Proposals (F0771) | You reviewed the invoices to be paid. |
| [Release Payment Proposal](#unique_40) [page ] 58 | Accounts Payable Accountant | Manage Automatic Payments (F0770) | You released the payment proposal. |
| [Next Steps (Optional)](#unique_41) [page ] 59 |  | In the topic, perform the steps mentioned from the Accounts Payable (J60) test script. |  |
| [Clear Virtual Card Clearing Account](#unique_42) [page ] 60 | General Ledger Accountant | Clear G/L Accounts - Manual Clearing (F1579) | You cleared the open items. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Invoice Entry Without Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter a supplier invoice without reference to a purchase order. Payment is made in local currency or you can pay invoices in foreign currency. For example, for a German company, you can pay invoices in USD, and for the U.S., you can pay invoices in EUR.

|  |
| --- |
| Note Create an invoice for each supplier listed in the [Master Data, Organizational Data, and Other Data](#unique_5) [page ] 5 section, except for the following suppliers:33300023 (funder)33300025 (card provider) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using a personalized user.Note Don't use the generic Accounts Payable Accountant user. Create a personalized user based on the business role IDSAP_BR_AP_ACCOUNTANT. |  |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). | The Manage Supplier Invoices (F0859) view displays. |  |
| 3 | Dialog Box | If the Data from Previous Invoice Entry Exist dialog box displays, choose No. |  |  |
| 4 | General Information | In the Basic Data section, enter the following data:Transaction: InvoiceInvoicing Party: <supplier>Company Code: 3310Gross Invoice Amount: 1000Note If the entry is tax relevant, change the amount according to the tax rate from step 6.Currency: For example, AEDInvoice Date: <Today's date>Posting Date: <Today's date>Reference: <any>Business Place: DXBNote After choosing the selection box, enter the company code, 3310, and choose Go. Then select the business place. |  |  |
| 5 | G/L Account Items | In the G/L Account Items section, choose Add.Make the following entries:Debit/Credit: DebitG/L Account: For example,61061000Amount 1000Item text: <any text> |  |  |
| 6 | Account Assignment | In the G/L Account Items, choose Add. Choose Show Details to expand the selection.Make the following entries:Cost Center: <Any cost center>If the General Ledger account is tax relevant, in the Tax section, enter Tax Date and any other mandatory fields.Payment section:Tax Date: <enter today's date>Note The Tax Date field is only visible in countries/regions where it is needed. |  |  |
| 7 | Post | Choose Post.Note The supplier invoice number generated is a logistics document number. To find or review the finance document number (Journal Entry), see the Invoice Payment Preparation > View Supplier Line Items task. | The Success dialog box displays, showing the document numbers created. |  |
| 8 | Exit | Choose No. |  |  |

### Dynamic Discounting

#### Maintain Business Partner for Dynamic Discounting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you assign a default payment method for the dynamic discounting supplier.

Prerequisite

Business partners are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Supplier Master Data (F1053A). | The Supplier Master view is displayed. |  |
| 3 | Select Roles and Supplier | Make the following entries and choose Go:Roles: Supplier (Fin.Accounting), SupplierBusiness Partner: 33300021 | The selected Business Partner displays in the worklist. |  |
| 4 | Choose Business Partner | For the selected business partner row, choose Details (>). |  |  |
| 5 | Edit Supplier | Choose Edit. | The Business Partner Master Data can now be edited. |  |
| 6 | Company Code Data | Choose the Company Codes tab. |  |  |
| 7 | Company Code | Select the radio button for a company code and choose Details (>). | Company code data is displayed. |  |
| 8 | Finance | Choose the Finance tab. |  |  |
| 9 | Payment Methods | In the Automatic Payment Transactions section, select one or more of the following Payment Methods:T | You've chosen payment methods. |  |
| 10 | Apply Changes | Choose Apply. |  |  |
| 11 | Save | Choose Save. |  |  |

#### Create Early Payment Request for Dynamic Discounting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, the supplier creates an early payment request for dynamic discounting.

|  |
| --- |
| Caution An additional license is required for Taulia Platform (Taulia Network UI). |

Prerequisite

All Preliminary Steps and previous procedures are performed.

Supplier invoices are posted.

Suppliers are onboarded and have enrolled status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log into the Taulia Network UI as a Dynamic Discounting Supplier, for example:<name>+<systemclient>_dd@taulia.comNote Contact the Taulia System Administrator to get logon credentials or create an internal incident for component BNS-TAU-WCM to request a user. | You are logged into the Taulia Supplier UI. |  |
| 2 | Invoices | Choose Invoices > My Invoices. | A list of invoices is displayed. |  |
| 3 | Early payment | For any invoice, in the Payment column choose Pay Me Early. | The Early Payment Offer dialog box is displayed. |  |
| 4 | Early Payment | Review the offer details and select an early payment date from the calendar. Choose Submit. | A dialog box is displayed. |  |
| 5 | No Thanks | Choose No Thanks. | An early payment is created. The Payment column changes to Requested and then to Agreed . A Financing Order is created in SAP S/4HANA Cloud Public Edition.Note The Cash discount amount and Payment Terms fields for the selected invoice document are updated. |  |
| 6 | Log out | Go to your profile and choose Log out. |  |  |

#### Financing Order for Dynamic Discounting

##### Display Financing Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

A financing order is automatically created after an early payment request is created. The financing order locks some fields in the original invoice and prevents running of some transactions such as clearing and manual payment.

Prerequisite

An early payment request is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Payables Financing Orders (F8343). |  |  |
| 3 | Data Entry and Search | Make the following entries and choose Go:Financing Type: <Any>Paying Company Code: 3310Supplier: <any> | A list of financing order IDs is displayed. |  |
| 4 | Selection | Choose a financing order ID and choose Details (>). | The Payables Financing view is displayed. |  |
| 5 | Navigation | Review the detailed information:General information - Review Cash discount amount and Payment Terms fields updated in creation of early payment requestFinancing order items- financed journal entries are displayed showing clearing status. To navigate to the journal entry, choose the journal entry number and then choose an option from the dialog box.Credit memo - (only generated if system is set up accordingly) discount is captured for the same amount as the cash discount amount. The credit is posted to the configured cash discount account. This is also created in the Taulia platform.You can view credit memo PDFs in the Attachment section of the journal entry. The attachment is also available in the Taulia platform so that the supplier can also view it.Administrative data |  |  |
| 6 | Done | When you're done reviewing the financing order, choose Back (<) as many times as needed to return to the previous screens. |  |  |

##### Cancel Financing Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, the Financing Order is canceled. The fields in the original invoice (and other transactions such as clearing and manual pay) are unlocked.

Prerequisite

A Financing Order exists with status Created.

Procedure

In a productive environment, cancellations are triggered by the Financial Operations team as the result of a funding issue (for example, in SCF) or by the Taulia Support team at the request of a buyer. Because a cancellation can never be triggered by the supplier, there is no user interface or application for it.

#### Payment Run for Dynamic Discounting

##### Schedule Payment Proposals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity selects the invoices to be paid.

Prerequisites

- The financing order is created.
- Business partners are maintained.
- Invoices are posted and open for payment. For more information, see the Accounts Payable (J60) test script (the Manage Supplier Line Items (F0712) app).
- Invoices are past due.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Automatic Payments (F0770). | The Manage Automatic Payments (F0770) view displays. |  |
| 3 | Create View | Choose Create Parameter. | The New Parameter dialog box is displayed. |  |
| 4 | Data Entry | Make the following entries and choose Create Parameter:Run Date: <today's date>Identification: <any five character description, such as SPAY1> | The Automatic Payment Parameters view is displayed. |  |
| 5 | Data Entry | Make the following entries:Basic section:Posting Date: <today's date>Docs entered up to: <today's date>Additional Log: ONPayment Controls section:Company Code: 3310Next payment date: <today's date + 5 days>Tip This is only recommended for testing purposes.If an invoice isn't overdue, but needs to be included in the payment run, choose a date that is after the invoice's due date.Payment method: for example, DOpen Item Selection section:Supplier: <supplier>Note For the Payment Method field, verify that the payment method is valid in the supplier master record.If it is necessary to post a down payment request, add a Free Selection and then enter the following:Special G/L ind. (BSEG-UMSKZ): F |  |  |
| 6 | Single Invoice (Optional) | To execute a payment for a single invoice, make the following entries in the Open Item Selection by populating any of the Free Selection # fields available:Document Number (BKPF-BELNR): <Document Number> |  |  |
| 7 | Save the Parameters | Choose Save. | The system displays the message Parameter has been saved. The status changes to Parameter Created. |  |
| 8 | Schedule Proposal | Choose Schedule > Proposal . | The Schedule Proposal dialog box is displayed. |  |
| 9 | Data Entry | Make the following entries and choose Schedule:Start Date: today's dateStart immediately: Select | The system displays the message Proposal has been scheduled.The status changes to Proposal Created. |  |
| 10 | View the Proposal | Choose the Proposal Processed tab. |  |  |
| 11 | Display | Choose the Go button. | The proposal is displayed in the list. |  |

##### Revise Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review invoices to be paid.

|  |
| --- |
| Caution Make sure that there are no other Payment Run Identification Proposals pending to be executed which might be using the same supplier as proposal created in previous step. If payment proposals exist, they must be processed or deleted, otherwise no payment proposal is generated for your proposal. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Revise Payment Proposals (F0771) app. | The Revise Payment Proposals screen is displayed. |  |
| 3 | Go | Choose Go. | A list of all proposals is displayed. |  |
| 4 | Select Identification | Choose Details (>) for the proposal you want to edit (for example, SPAY1 ). | The view Schedule Payment Proposal of the selected Identification is displayed. |  |
| 5 | Edit Payment (Optional) | In the Payments tab, select the rows to edit, and choose Edit Payment. | The Edit Payment dialog box is displayed. |  |
| 6 | Make Entries (Optional) | Change desired options and choose OK to continue.Payment method: <payment method>House Bank: <house bank>Account ID: <account>Payee Bank: <payee bank>Due Date: <date> |  |  |
| 7 | Payment List | Choose Export to PDF. | A new view displays the payment list. You can download or print the form from here. |  |
| 8 | Exceptions | If some payments are blocked, you can find them on the Exceptions tab. You may unblock or reallocate and pay them by using the buttons in the view.Note A Sanctioned Party List screening happens if the Compliance Management with SAP Global Trade Services (24J) was activated. If the screening blocks a payment as a result of this SAP GTS check, contact your GTS team to take the proper actions. |  |  |

##### Release Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to release the payment proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Manage Automatic Payments (F0770) app. | The Manage Automatic Payments screen is displayed. |  |
| 3 | Go | Choose Go. | A list of all payment runs is displayed. |  |
| 4 | Proposal Processing | Choose the Proposal Processed tab. |  |  |
| 5 | Select Proposal | Select the line of the previously created proposal (for example, SPAY1 ) and choose Schedule Payment. | The Schedule Payment dialog box is displayed. |  |
| 6 | Schedule Payment | Make the following entries:Start Date: <Today's date>Start immediately: Selectand choose Schedule. | The system message Payment has been scheduled is displayed. The status changes to Payment Posted. The log shows how many postings or payments were generated. |  |
| 7 | View the payment | Choose the Payments Processed tab. | The status changes to Payment posted.Note If the status is Payment finished, review if the chosen documents can be paid (execute the steps starting with the Payment and Exceptions header. |  |
| 8 | View Log postings | Select the line of your payment run Identification and in the Log column, choose Log Details.Note If the Log column doesn't show, choose the Settings button. Select the Log field and choose OK. | The log shows how many postings were generated. |  |
| 9 | Close Dialog | Choose OK. | The Log Details dialog box closes. |  |
| 10 | Payments and Exceptions | Choose Details (>) . | The view displays a summary of payments and exceptions for the payment run. |  |
| 11 | Navigation | You can sort the information by payment method, country/region, and so on. Select the view to display in the field below Summary. | Amounts are sorted by your selection. |  |
| 12 | Payments | Choose Payments or Exceptions. | Details are displayed for payments or exceptions generated (such as payment document, payment order, included items, and so on). |  |
| 13 | Payment List | On the Payments tab, choose Export to PDF. | A view displays the payment list. From here, you can preview, print, or download the list. |  |
| 14 | Payments Navigation | On the Payments tab, for the desired item, choose Details (>).When you're done, choose Back at the top to exit this view. | Payment item details are displayed. |  |

##### Next Steps (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform any optional follow-on steps.

Prerequisite

The payment proposal was released successfully.

From the Accounts Payable (J60) test script, you performed all steps in Prerequisites > Preliminary Steps .

Procedure

Review and perform steps described in the following chapters of the Accounts Payable (J60) test script:

- Payment Approval
- Payment Media

### Supply Chain Finance

#### Maintain Business Partner for Supply Chain Finance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you assign a default payment method and alternative payee for supply chain finance.

|  |
| --- |
| Note During Taulia platform setup, the Permitted Alternative Payee can be configured; however, you must coordinate this with the Taulia FinOps team. In this case, the manual assignment of Permitted Alternative Payee is optional. The Business Partner Master Data is automatically updated when you create the first Early Payment Request. |

Prerequisite

Business Partners are created.

Payment methods exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Supplier Master Data (F1053A). | The Supplier Master view is displayed. |  |
| 3 | Select Roles and Supplier | Select the following and choose Go:Roles: Supplier (Fin.Accounting), SupplierBusiness Partner: 33300022 | The selected Business Partner displays in the worklist. |  |
| 4 | Choose BP | For the Business Partner row, choose Details (>). | Details of the Business Partner are displayed. |  |
| 5 | Edit Supplier | Choose Edit. | The Business Partner Master Data can now be edited. |  |
| 6 | Company Code Data | Choose the Company Codes tab. |  |  |
| 7 | Company Code | Select the radio button for a company code and choose Details (>). | Company code data is displayed. |  |
| 8 | Finance | Choose the Finance tab. |  |  |
| 9 | Alternative Payee | In the Basic Data section, in the Supplier information area, make the following entry:Alternative Payee: 33300023 (Funder) |  |  |
| 10 | Payment Methods | In the Automatic Payment Transactions section, select one or more of the following Payment Methods:FTNote For payments in USD, use F. | You've chosen payment methods. |  |
| 11 | Apply Changes | Choose Apply. |  |  |
| 12 | Save | Choose Save. |  |  |
| 13 | Repeat for Alternative Payee | Repeat these steps to set up a payment method to the Alternative Payee. |  |  |

#### Create Early Payment Request for Supply Chain Finance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, the supplier creates an early payment request for supply chain finance.

|  |
| --- |
| Caution An additional license is required for Taulia Platform (Taulia Network UI). |

Prerequisite

Supplier invoices are posted.

Suppliers are onboarded with enrolled status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log into the Taulia Network UI as a Supply Chain Finance Supplier, for example:<name>+<systemclient>_scf@taulia.comNote Contact Taulia System Administrator to get logon credentials or create an internal incident for component BNS-TAU-WCM to request a user. | Taulia Supplier UI is accessed. |  |
| 2 | Invoices | Choose Invoices > My Invoices. | A list of invoices is displayed. |  |
| 3 | Early Payment | For any invoice, in the Payment column choose the button Pay Me Early. |  |  |
| 4 | Early Payment | In the Early Payment Offer dialog box, details of the offer are displayed. Select the available date from the calendar and choose Submit. | A dialog box appears asking to get paid early on all invoices. |  |
| 5 | Early Payment | Choose No Thanks. | Early payment is created. The Payment column changes to Requested and then to Agreed. A Financing Order is created in SAP S/4HANA Cloud Public Edition. |  |
| 6 | Log out | Go to your profile and choose Log out. |  |  |

#### Financing Order for Supply Chain Finance

##### Display Financing Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

After an Early Payment Request has been created, a Financing Order is created automatically.

The Financing Order locks some fields of the original invoice and prevents some transaction such as clearing, or manual pay to be performed.

Prerequisite

An Early Payment Request is created.

Use data created in previous chapters.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Payables Financing Orders (F8343). |  |  |
| 3 | Data Entry and Search | Make the following entries and choose Go:Financing Type: <Any>Paying Company Code: 3310Supplier: <any> | A list of financing order IDs is displayed according to your search criteria. |  |
| 4 | Selection | Choose a financing order ID and choose Details (>). | The Payables Financing view is displayed. |  |
| 5 | Navigation | Review the detailed information:General Information - Funder and Funder Bank Type are displayed.Financing order items – financed journal entries are displayed, showing clearing status. To navigate to the journal entry, choose the journal entry number and choose an option from the dialog box.Administrative Data |  |  |
| 6 | Done | When you’re done reviewing the financing order, choose Back (<) as many times as needed to return to the previous screens. |  |  |

##### Cancel Financing Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, the financing order is canceled. When canceled, it unlocks the fields in the original invoice and unlocks other transaction such as clearing and manual payment.

Prerequisite

A financing order exists with status Created.

Procedure

In a productive environment, cancellations are triggered by the Financial Operations team as the result of a funding issue (for example, in SCF) or by the Taulia Support team at the request of a buyer. Because a cancellation can never be triggered by the supplier, there is no user interface or application for it.

#### Payment Run for Supply Chain Finance

##### Schedule Payment Proposals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity selects the invoices to be paid.

Prerequisites

- The financing order is created.
- Business partners are maintained.
- Invoices are posted and open for payment. For more information, see the Accounts Payable (J60) test script (the Manage Supplier Line Items (F0712) app).
- Invoices are past due.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Automatic Payments (F0770). | The Manage Automatic Payments (F0770) view displays. |  |
| 3 | Create View | Choose Create Parameter. | The New Parameter dialog box is displayed. |  |
| 4 | Data Entry | Make the following entries and choose Create Parameter:Run Date: <today's date>Identification: <any five character description, such as SPAY1> | The Automatic Payment Parameters view is displayed. |  |
| 5 | Data Entry | Make the following entries:Basic section:Posting Date: <today's date>Docs entered up to: <today's date>Additional Log: ONPayment Controls section:Company Code: 3310Next payment date: <today's date + 5 days>Tip This is only recommended for testing purposes.If an invoice isn't overdue, but needs to be included in the payment run, choose a date that is after the invoice's due date.Payment method: for example, DOpen Item Selection section:Supplier: <supplier>Note For the Payment Method field, verify that the payment method is valid in the supplier master record.If it is necessary to post a down payment request, add a Free Selection and then enter the following:Special G/L ind. (BSEG-UMSKZ): F |  |  |
| 6 | Single Invoice (Optional) | To execute a payment for a single invoice, make the following entries in the Open Item Selection by populating any of the Free Selection # fields available:Document Number (BKPF-BELNR): <Document Number> |  |  |
| 7 | Save the Parameters | Choose Save. | The system displays the message Parameter has been saved. The status changes to Parameter Created. |  |
| 8 | Schedule Proposal | Choose Schedule > Proposal . | The Schedule Proposal dialog box is displayed. |  |
| 9 | Data Entry | Make the following entries and choose Schedule:Start Date: today's dateStart immediately: Select | The system displays the message Proposal has been scheduled.The status changes to Proposal Created. |  |
| 10 | View the Proposal | Choose the Proposal Processed tab. |  |  |
| 11 | Display | Choose the Go button. | The proposal is displayed in the list. |  |

##### Revise Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review invoices to be paid.

|  |
| --- |
| Caution Make sure that there are no other Payment Run Identification Proposals pending to be executed which might be using the same supplier as proposal created in previous step. If payment proposals exist, they must be processed or deleted, otherwise no payment proposal is generated for your proposal. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Revise Payment Proposals (F0771) app. | The Revise Payment Proposals screen is displayed. |  |
| 3 | Go | Choose Go. | A list of all proposals is displayed. |  |
| 4 | Select Identification | Choose Details (>) for the proposal you want to edit (for example, SPAY1 ). | The view Schedule Payment Proposal of the selected Identification is displayed. |  |
| 5 | Edit Payment (Optional) | In the Payments tab, select the rows to edit, and choose Edit Payment. | The Edit Payment dialog box is displayed. |  |
| 6 | Make Entries (Optional) | Change desired options and choose OK to continue.Payment method: <payment method>House Bank: <house bank>Account ID: <account>Payee Bank: <payee bank>Due Date: <date> |  |  |
| 7 | Payment List | Choose Export to PDF. | A new view displays the payment list. You can download or print the form from here. |  |
| 8 | Exceptions | If some payments are blocked, you can find them on the Exceptions tab. You may unblock or reallocate and pay them by using the buttons in the view.Note A Sanctioned Party List screening happens if the Compliance Management with SAP Global Trade Services (24J) was activated. If the screening blocks a payment as a result of this SAP GTS check, contact your GTS team to take the proper actions. |  |  |

##### Release Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to release the payment proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Manage Automatic Payments (F0770) app. | The Manage Automatic Payments screen is displayed. |  |
| 3 | Go | Choose Go. | A list of all payment runs is displayed. |  |
| 4 | Proposal Processing | Choose the Proposal Processed tab. |  |  |
| 5 | Select Proposal | Select the line of the previously created proposal (for example, SPAY1 ) and choose Schedule Payment. | The Schedule Payment dialog box is displayed. |  |
| 6 | Schedule Payment | Make the following entries:Start Date: <Today's date>Start immediately: Selectand choose Schedule. | The system message Payment has been scheduled is displayed. The status changes to Payment Posted. The log shows how many postings or payments were generated. |  |
| 7 | View the payment | Choose the Payments Processed tab. | The status changes to Payment posted.Note If the status is Payment finished, review if the chosen documents can be paid (execute the steps starting with the Payment and Exceptions header. |  |
| 8 | View Log postings | Select the line of your payment run Identification and in the Log column, choose Log Details.Note If the Log column doesn't show, choose the Settings button. Select the Log field and choose OK. | The log shows how many postings were generated. |  |
| 9 | Close Dialog | Choose OK. | The Log Details dialog box closes. |  |
| 10 | Payments and Exceptions | Choose Details (>) . | The view displays a summary of payments and exceptions for the payment run. |  |
| 11 | Navigation | You can sort the information by payment method, country/region, and so on. Select the view to display in the field below Summary. | Amounts are sorted by your selection. |  |
| 12 | Payments | Choose Payments or Exceptions. | Details are displayed for payments or exceptions generated (such as payment document, payment order, included items, and so on). |  |
| 13 | Payment List | On the Payments tab, choose Export to PDF. | A view displays the payment list. From here, you can preview, print, or download the list. |  |
| 14 | Payments Navigation | On the Payments tab, for the desired item, choose Details (>).When you're done, choose Back at the top to exit this view. | Payment item details are displayed. |  |

##### Next Steps (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform any optional follow-on steps.

Prerequisite

The payment proposal was released successfully.

In the Accounts Payable (J60) test script, you performed all steps from the Prerequisites > Preliminary Steps section.

Procedure

Review and perform steps described in the following chapters of the Accounts Payable (J60) test script:

- Payment Approval
- Payment Media

### Virtual Card

#### Maintain Business Partner

##### Maintain Business Partner for Virtual Card

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you assign a default Taulia payment method for virtual card supplier.

Prerequisite

Business partners are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Supplier Master Data (F1053A). | The Supplier Master view displays. |  |
| 3 | Select Roles and Supplier | Select the following and choose Go:Roles: Supplier (Fin.Accounting), SupplierBusiness Partner: 33300024 | The selected Business Partner displays in the worklist. |  |
| 4 | Choose BP | For the Business Partner row, choose Details (>). |  |  |
| 5 | Edit Supplier | Choose Edit. |  |  |
| 6 | Company Code Data | Choose the Company Codes tab. |  |  |
| 7 | Company Code | Select the radio button for a company code and choose Details (>). |  |  |
| 8 | Finance | Choose the Finance tab. |  |  |
| 9 | Payment Methods | In the Automatic Payment Transactions section, select the following Payment Method:$ | You've chosen the payment method. |  |
| 10 | Apply Changes | Choose Apply. |  |  |
| 11 | Save | Choose Save. |  |  |

##### Maintain Business Partner for Card Provider

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you assign a default payment method for card provider supplier.

Prerequisite

Business Partners are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Supplier Master Data (F1053A). | The Supplier Master view is displayed. |  |
| 3 | Select Roles and Supplier | Select the following and choose Go:Roles: Supplier (Fin.Accounting), SupplierBusiness Partner: 33300025 | The selected Business Partner displays in the worklist. |  |
| 4 | Choose BP | Choose the Navigation (>) button (last column) of the Business Partner row. |  |  |
| 5 | Edit Supplier | Choose Edit. |  |  |
| 6 | Company Code Data | Choose the Company Codes tab. |  |  |
| 7 | Company Code | Select the radio button for a company code and choose Details (>). | Company code data is displayed. |  |
| 8 | Finance | Choose the Finance tab. |  |  |
| 9 | Payment Methods | In the Automatic Payment Transactions section, select one or more of the following Payment Methods:TNote For payments in EUR, use I. | You've chosen payment methods. |  |
| 10 | Apply Changes | Choose Apply. |  |  |
| 11 | Save | Choose Save. | The changes to Business Partner Master Data are saved. |  |

#### Create Early Payment Request for Virtual Card

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

When a supplier agrees to be financed via Virtual Cards, the early payment request is automatically created.

|  |
| --- |
| Caution An additional license is required for Taulia Platform (Taulia Network UI). |

Prerequisite

Supplier invoices are posted.

Suppliers are onboarded with enrolled status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log into Taulia Network UI as a Virtual Card Supplier, for example:<name>+<systemclient>_vc@taulia.comNote Contact the Taulia System Administrator to get logon credentials or create an internal incident for component BNS-TAU-WCM to request a user. | Taulia Supplier UI is accessed. |  |
| 2 | Invoices | Choose Invoices > My Invoices. | A list of invoices are displayed. |  |
| 3 | Early payment | Since the early payment request is automatically created, only status updates are displayed in the Payment column:Card Issued: This is automatically set when invoices are created and transferred from SAP S/4HANA Cloud Public Edition to the Taulia platform The Payment Method field for the invoice documents is updated, and Virtual Card is sent to the Supplier via e-mail.Card Charged: communication via email happens before the card is charged. When the Supplier charges the card, the Card Provider updates status to Paid.All of this is an automatic background process that has no user intervention. | Early payment is automatically created, and a Financing Order is created in SAP S/4HANA Cloud Public Edition.Note The Payment Method field of the invoice documents are updated. |  |
| 4 | Log out | Go to your profile and choose Log out. |  |  |

#### Financing Order for Virtual Card Supplier

##### Display Financing Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

A financing order is automatically created after an early payment request is created. The financing order locks some fields of the original invoice and prevents the performance of some transactions such as clearing and manual payment.

Prerequisite

An early payment request is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Payables Financing Orders (F8343). |  |  |
| 3 | Data Entry and Search | Make the following entries and choose Go:Financing Type: <Any>Paying Company Code: 3310Supplier: <any> | A list of Financing Order IDs is displayed according to your search criteria. |  |
| 4 | Selection | Choose a financing order ID and choose Details (>). | The Payables Financing view is displayed. |  |
| 5 | Navigation | Review the detailed information:General information - Review the Payment Method field updated in creation of early payment requestFinancing order items: Financed journal entries are displayed showing clearing status. To navigate to the journal entry, choose the journal entry number and choose an option from the dialog box.Administrative Data |  |  |
| 6 | Done | When you are done reviewing the financing order, choose Back (<) as many times as needed to return to the previous screens. |  |  |

##### Cancel Financing Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, the financing order is canceled. It unlocks the fields in the original invoice and unlocks other transaction such as clearing and manual pay.

Prerequisite

A Financing Order exists with status Created.

Procedure

In a productive environment, cancellations are triggered by the Financial Operations team as the result of a funding issue (for example, in SCF) or by the Taulia Support team at the request of a buyer. Because a cancellation can never be triggered by the supplier, there is no user interface or application for it.

#### Payment Run for Virtual Card Supplier

Purpose

In this activity, payment is performed for a Virtual Card Supplier.

Prerequisites

Invoices are posted and are open for payment. For more information, see the Accounts Payable (J60) test script; see the Manage Supplier Line Items (F0712) app.

Payment methods are defined in the Maintain Business Partner procedure.

The financing order is created.

##### Schedule Payment Proposals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity selects the invoices to be paid for the Supply Chain Finance supplier that are posted against a Virtual Card Clearing Account using a Taulia payment method.

|  |
| --- |
| Caution In the Procedure table below, in step 5 (Data Entry), use Payment Method $. |

Prerequisites

- The financing order is created.
- Payment methods and Alternative Payee are defined in the Maintain Business Partner procedure.
- Invoices are posted and open for payment. For more information, see the Accounts Payable (J60) test script (the Manage Supplier Line Items (F0712) app).
- Invoices are past due.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Automatic Payments (F0770). | The Manage Automatic Payments (F0770) view displays. |  |
| 3 | Create View | Choose Create Parameter. | The New Parameter dialog box is displayed. |  |
| 4 | Data Entry | Make the following entries and choose Create Parameter:Run Date: <today's date>Identification: <any five character description, such as SPAY1> | The Automatic Payment Parameters view is displayed. |  |
| 5 | Data Entry | Make the following entries:Basic section:Posting Date: <today's date>Docs entered up to: <today's date>Additional Log: ONPayment Controls section:Company Code: 3310Next payment date: <today's date + 5 days>Tip This is only recommended for testing purposes.If an invoice isn't overdue, but needs to be included in the payment run, choose a date that is after the invoice's due date.Payment method: for example, DOpen Item Selection section:Supplier: <supplier>Note For the Payment Method field, verify that the payment method is valid in the supplier master record.If it is necessary to post a down payment request, add a Free Selection and then enter the following:Special G/L ind. (BSEG-UMSKZ): F |  |  |
| 6 | Single Invoice (Optional) | To execute a payment for a single invoice, make the following entries in the Open Item Selection by populating any of the Free Selection # fields available:Document Number (BKPF-BELNR): <Document Number> |  |  |
| 7 | Save the Parameters | Choose Save. | The system displays the message Parameter has been saved. The status changes to Parameter Created. |  |
| 8 | Schedule Proposal | Choose Schedule > Proposal . | The Schedule Proposal dialog box is displayed. |  |
| 9 | Data Entry | Make the following entries and choose Schedule:Start Date: today's dateStart immediately: Select | The system displays the message Proposal has been scheduled.The status changes to Proposal Created. |  |
| 10 | View the Proposal | Choose the Proposal Processed tab. |  |  |
| 11 | Display | Choose the Go button. | The proposal is displayed in the list. |  |

##### Revise Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review invoices to be paid.

|  |
| --- |
| Caution Make sure that there are no other Payment Run Identification Proposals pending to be executed which might be using the same supplier as proposal created in previous step. If payment proposals exist, they must be processed or deleted, otherwise no payment proposal is generated for your proposal. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Revise Payment Proposals (F0771) app. | The Revise Payment Proposals screen is displayed. |  |
| 3 | Go | Choose Go. | A list of all proposals is displayed. |  |
| 4 | Select Identification | Choose Details (>) for the proposal you want to edit (for example, SPAY1 ). | The view Schedule Payment Proposal of the selected Identification is displayed. |  |
| 5 | Edit Payment (Optional) | In the Payments tab, select the rows to edit, and choose Edit Payment. | The Edit Payment dialog box is displayed. |  |
| 6 | Make Entries (Optional) | Change desired options and choose OK to continue.Payment method: <payment method>House Bank: <house bank>Account ID: <account>Payee Bank: <payee bank>Due Date: <date> |  |  |
| 7 | Payment List | Choose Export to PDF. | A new view displays the payment list. You can download or print the form from here. |  |
| 8 | Exceptions | If some payments are blocked, you can find them on the Exceptions tab. You may unblock or reallocate and pay them by using the buttons in the view.Note A Sanctioned Party List screening happens if the Compliance Management with SAP Global Trade Services (24J) was activated. If the screening blocks a payment as a result of this SAP GTS check, contact your GTS team to take the proper actions. |  |  |

##### Release Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to release the payment proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Manage Automatic Payments (F0770) app. | The Manage Automatic Payments screen is displayed. |  |
| 3 | Go | Choose Go. | A list of all payment runs is displayed. |  |
| 4 | Proposal Processing | Choose the Proposal Processed tab. |  |  |
| 5 | Select Proposal | Select the line of the previously created proposal (for example, SPAY1 ) and choose Schedule Payment. | The Schedule Payment dialog box is displayed. |  |
| 6 | Schedule Payment | Make the following entries:Start Date: <Today's date>Start immediately: Selectand choose Schedule. | The system message Payment has been scheduled is displayed. The status changes to Payment Posted. The log shows how many postings or payments were generated. |  |
| 7 | View the payment | Choose the Payments Processed tab. | The status changes to Payment posted.Note If the status is Payment finished, review if the chosen documents can be paid (execute the steps starting with the Payment and Exceptions header. |  |
| 8 | View Log postings | Select the line of your payment run Identification and in the Log column, choose Log Details.Note If the Log column doesn't show, choose the Settings button. Select the Log field and choose OK. | The log shows how many postings were generated. |  |
| 9 | Close Dialog | Choose OK. | The Log Details dialog box closes. |  |
| 10 | Payments and Exceptions | Choose Details (>) . | The view displays a summary of payments and exceptions for the payment run. |  |
| 11 | Navigation | You can sort the information by payment method, country/region, and so on. Select the view to display in the field below Summary. | Amounts are sorted by your selection. |  |
| 12 | Payments | Choose Payments or Exceptions. | Details are displayed for payments or exceptions generated (such as payment document, payment order, included items, and so on). |  |
| 13 | Payment List | On the Payments tab, choose Export to PDF. | A view displays the payment list. From here, you can preview, print, or download the list. |  |
| 14 | Payments Navigation | On the Payments tab, for the desired item, choose Details (>).When you're done, choose Back at the top to exit this view. | Payment item details are displayed. |  |

#### Invoice Entry Without Purchase Order for Card Provider

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you enter a supplier invoice for the card provider without reference to a purchase order.

Prerequisite

A vCard statement from the Bank is received.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad using a personalized user.Note Note Don't use the generic Accounts Payable Accountant user. Create a personalized user based on the business role ID: SAP_BR_AP_ACCOUNTANT |  |  |
| 2 | Access the SAP Fiori App | Open Create Supplier Invoice (F0859). |  |  |
| 3 | Dialog Box | If the Data from Previous Invoice Entry Exist dialog box displays, choose No. |  |  |
| 4 | General Information | In the Basic Data section, enter the following data:Transaction: InvoiceInvoicing Party: 33300025Company Code: 3310Gross Invoice Amount: <amount from Financing Order >Note If the entry is tax relevant, change the amount according to the tax rate from step 6.Currency: For example, AEDInvoice Date: <Today's date>Posting Date: <Today's date>Reference: <any> |  |  |
| 5 | G/L Account Items | In the G/L Account Items section, choose Add.Make the following entries:Debit/Credit: DebitG/L Account: 21901000Amount: <amount from Financing Order>Item text: <any text> |  |  |
| 6 | More Details | In the G/L Account Items, choose Show Details to expand the selection and enter any other required entry. |  |  |
| 7 | Post | Choose Post.Note The supplier invoice number generated is a logistics document number. To find or review the finance document number (Journal Entry), from the Accounts Payable (J60) test script, review the chapter Invoice Payment Preparation > View Supplier Line Items task. |  |  |
| 8 | Exit | Choose No. |  |  |

#### Payment Run for Card Provider

##### Schedule Payment Proposals

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity selects the invoices to be paid.

Prerequisites

- The financing order is created.
- Business partners are maintained.
- Invoices are posted and open for payment. For more information, see the Accounts Payable (J60) test script (the Manage Supplier Line Items (F0712) app).
- Invoices are past due.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Automatic Payments (F0770). | The Manage Automatic Payments (F0770) view displays. |  |
| 3 | Create View | Choose Create Parameter. | The New Parameter dialog box is displayed. |  |
| 4 | Data Entry | Make the following entries and choose Create Parameter:Run Date: <today's date>Identification: <any five character description, such as SPAY1> | The Automatic Payment Parameters view is displayed. |  |
| 5 | Data Entry | Make the following entries:Basic section:Posting Date: <today's date>Docs entered up to: <today's date>Additional Log: ONPayment Controls section:Company Code: 3310Next payment date: <today's date + 5 days>Tip This is only recommended for testing purposes.If an invoice isn't overdue, but needs to be included in the payment run, choose a date that is after the invoice's due date.Payment method: for example, DOpen Item Selection section:Supplier: <supplier>Note For the Payment Method field, verify that the payment method is valid in the supplier master record.If it is necessary to post a down payment request, add a Free Selection and then enter the following:Special G/L ind. (BSEG-UMSKZ): F |  |  |
| 6 | Single Invoice (Optional) | To execute a payment for a single invoice, make the following entries in the Open Item Selection by populating any of the Free Selection # fields available:Document Number (BKPF-BELNR): <Document Number> |  |  |
| 7 | Save the Parameters | Choose Save. | The system displays the message Parameter has been saved. The status changes to Parameter Created. |  |
| 8 | Schedule Proposal | Choose Schedule > Proposal . | The Schedule Proposal dialog box is displayed. |  |
| 9 | Data Entry | Make the following entries and choose Schedule:Start Date: today's dateStart immediately: Select | The system displays the message Proposal has been scheduled.The status changes to Proposal Created. |  |
| 10 | View the Proposal | Choose the Proposal Processed tab. |  |  |
| 11 | Display | Choose the Go button. | The proposal is displayed in the list. |  |

##### Revise Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review invoices to be paid.

|  |
| --- |
| Caution Make sure that there are no other Payment Run Identification Proposals pending to be executed which might be using the same supplier as proposal created in previous step. If payment proposals exist, they must be processed or deleted, otherwise no payment proposal is generated for your proposal. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Revise Payment Proposals (F0771) app. | The Revise Payment Proposals screen is displayed. |  |
| 3 | Go | Choose Go. | A list of all proposals is displayed. |  |
| 4 | Select Identification | Choose Details (>) for the proposal you want to edit (for example, SPAY1 ). | The view Schedule Payment Proposal of the selected Identification is displayed. |  |
| 5 | Edit Payment (Optional) | In the Payments tab, select the rows to edit, and choose Edit Payment. | The Edit Payment dialog box is displayed. |  |
| 6 | Make Entries (Optional) | Change desired options and choose OK to continue.Payment method: <payment method>House Bank: <house bank>Account ID: <account>Payee Bank: <payee bank>Due Date: <date> |  |  |
| 7 | Payment List | Choose Export to PDF. | A new view displays the payment list. You can download or print the form from here. |  |
| 8 | Exceptions | If some payments are blocked, you can find them on the Exceptions tab. You may unblock or reallocate and pay them by using the buttons in the view.Note A Sanctioned Party List screening happens if the Compliance Management with SAP Global Trade Services (24J) was activated. If the screening blocks a payment as a result of this SAP GTS check, contact your GTS team to take the proper actions. |  |  |

##### Release Payment Proposal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to release the payment proposal.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Accounts Payable Accountant. |  |  |
| 2 | Access App | Open the Manage Automatic Payments (F0770) app. | The Manage Automatic Payments screen is displayed. |  |
| 3 | Go | Choose Go. | A list of all payment runs is displayed. |  |
| 4 | Proposal Processing | Choose the Proposal Processed tab. |  |  |
| 5 | Select Proposal | Select the line of the previously created proposal (for example, SPAY1 ) and choose Schedule Payment. | The Schedule Payment dialog box is displayed. |  |
| 6 | Schedule Payment | Make the following entries:Start Date: <Today's date>Start immediately: Selectand choose Schedule. | The system message Payment has been scheduled is displayed. The status changes to Payment Posted. The log shows how many postings or payments were generated. |  |
| 7 | View the payment | Choose the Payments Processed tab. | The status changes to Payment posted.Note If the status is Payment finished, review if the chosen documents can be paid (execute the steps starting with the Payment and Exceptions header. |  |
| 8 | View Log postings | Select the line of your payment run Identification and in the Log column, choose Log Details.Note If the Log column doesn't show, choose the Settings button. Select the Log field and choose OK. | The log shows how many postings were generated. |  |
| 9 | Close Dialog | Choose OK. | The Log Details dialog box closes. |  |
| 10 | Payments and Exceptions | Choose Details (>) . | The view displays a summary of payments and exceptions for the payment run. |  |
| 11 | Navigation | You can sort the information by payment method, country/region, and so on. Select the view to display in the field below Summary. | Amounts are sorted by your selection. |  |
| 12 | Payments | Choose Payments or Exceptions. | Details are displayed for payments or exceptions generated (such as payment document, payment order, included items, and so on). |  |
| 13 | Payment List | On the Payments tab, choose Export to PDF. | A view displays the payment list. From here, you can preview, print, or download the list. |  |
| 14 | Payments Navigation | On the Payments tab, for the desired item, choose Details (>).When you're done, choose Back at the top to exit this view. | Payment item details are displayed. |  |

##### Next Steps (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform any optional follow-on steps.

Prerequisite

The payment proposal is successfully released.

You performed the activities for all steps from the Prerequisites > Preliminary Steps section in from the Accounts Payable (J60) test script.

Procedure

Review and perform steps described in the following chapters of the Accounts Payable (J60) test script:

- Payment Approval
- Payment Media

#### Clear Virtual Card Clearing Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you clear open items manually. If the balance of the items to be cleared isn't 0, you can create a residual item for overpayments/underpayments.

Prerequisites

You performed the payment run for the virtual card supplier successfully.

You created the invoice entry without purchase order for the card provider and performed the payment run.

Ensure that there’s a posting to an open-item-managed account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Clear G/L Accounts - Manual Clearing (F1579). |  |  |
| 3 | Account Information | Enter the G/L account to clear and choose Go:G/L Account: 21901000Company Code: 3310 |  |  |
| 4 | Clear Account | To clear an account, in the Accounts (x) section, choose Clear (>). |  |  |
| 5 | Select Open Items | In the Header section, enter the Transaction Currency AED.In the Open Items section, select items to be cleared by choosing the Clear button. | In the Items to Be Cleared section, the selected items are displayed. |  |
| 6 | Save | Choose Post. | The open items selected in the account are cleared. Make a note of the cleared document number for later use in resetting the cleared item: ______ |  |

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
> Flagged while digesting this document, not verified: The Overview Table names the business role for Create Supplier Invoice (F0859) as a personalized role based on SAP_BR_AR_ACCOUNTANT, while the procedure steps say to create a personalized user based on SAP_BR_AP_ACCOUNTANT.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/test-script-receivables-financing-with-taulia-7dx-ae-1214]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7MG_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 96,162 chars in the whole document
