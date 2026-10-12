---
id: 05-treasury-and-cash-management/test-script-letter-of-credit-management-49d-ae-sap-s-4hana-cloud-publi-part-01
title: "Test Script: Letter of Credit Management (49D_AE) - SAP S/4HANA Cloud Public Edition (49D_S4CLD2608_BPD_EN_AE) — part 1 of 2"
description: "SAP test script for scope item 49D (UAE): issuing, receiving, rolling over, presenting, paying and terminating normal and standby letters of credit."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/letters-of-credit]
aliases: []
keywords: [Letter of Credit Management, normal letter of credit, standby letter of credit, letter of credit rollover, letter of credit presentation, standby letter of credit termination, cash collateral and fees, payment requests, general ledger posting, key date valuation]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49D_S4CLD2608_BPD_EN_AE.docx#lines-1-2870"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1002
topic: 05-treasury-and-cash-management/letters-of-credit
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Letter of Credit Management (49D_AE) - SAP S/4HANA Cloud Public Edition (49D_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49D_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–2870 of the extracted text), extracted with `mammoth`. Grouped under **Letter of Credit Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Letter of Credit Management (49D_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232854576)

[2 Prerequisites 6](#_Toc232854577)

[2.1 System Access 6](#_Toc232854578)

[2.2 Roles 6](#_Toc232854579)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232854580)

[2.4 Business Conditions 8](#_Toc232854581)

[2.5 Preliminary Steps 8](#_Toc232854582)

[2.5.1 Create Business Partner 8](#_Toc232854583)

[2.5.1.1 Maintain General Data for Business Partner 8](#_Toc232854584)

[2.5.1.2 Maintain Payment Details for Business Partner 9](#_Toc232854585)

[2.5.1.3 Maintain Authorizations for Business Partner 9](#_Toc232854586)

[2.5.1.4 Maintain Reporting Data in Company Code for Business Partner 9](#_Toc232854587)

[2.5.1.5 Maintain Additional Role for Business Partner 9](#_Toc232854588)

[2.5.2 Maintain Limit with Limit Type Y01 10](#_Toc232854589)

[2.5.3 Maintain Trader and Trader Authorizations 11](#_Toc232854590)

[3 Overview Table 12](#_Toc232854591)

[4 Test Procedures 19](#_Toc232854592)

[4.1 Issue Normal Letter of Credit 19](#_Toc232854593)

[4.1.1 Issue Normal Letter of Credit 19](#_Toc232854594)

[4.1.1.1 (1XN) Market Rates Management – Manually via Upload 19](#_Toc232854595)

[4.1.1.2 Check Credit Line Limit (Optional) 19](#_Toc232854596)

[4.1.1.3 Create Facility (Optional) 20](#_Toc232854597)

[4.1.1.3.1 Create Facility (Optional) 20](#_Toc232854598)

[4.1.1.3.2 Settle Facility (Optional) 20](#_Toc232854599)

[4.1.1.4 Check Facilities Utilization (Optional) 21](#_Toc232854600)

[4.1.1.5 Issue Normal Letter of Credit 21](#_Toc232854601)

[4.1.1.6 Set Settlement Status 24](#_Toc232854602)

[4.1.1.7 Letter of Credit Fees and Cash Collateral Payment 25](#_Toc232854603)

[4.1.1.7.1 Option 1: Generate and Automatically Process Payment Request 25](#_Toc232854604)

[4.1.1.7.2 Option 2: Generate and Process Payment Request 29](#_Toc232854605)

[4.1.1.7.3 Send Payment Medium File 34](#_Toc232854606)

[4.1.1.8 Bank Initiated Payment 34](#_Toc232854607)

[4.1.1.9 Post to General Ledger 34](#_Toc232854608)

[4.1.2 Rollover Letter of Credit 37](#_Toc232854609)

[4.1.2.1 Rollover Letter of Credit 37](#_Toc232854610)

[4.1.2.2 Set Settlement Status 38](#_Toc232854611)

[4.1.2.3 Letter of Credit Fees and Cash Collateral Payment 39](#_Toc232854612)

[4.1.2.3.1 Option 1: Generate and Automatically Process Payment Request 39](#_Toc232854613)

[4.1.2.3.2 Option 2: Generate and Process Payment Request 43](#_Toc232854614)

[4.1.2.3.3 Send Payment Medium File 48](#_Toc232854615)

[4.1.2.4 Bank Initiated Payment 48](#_Toc232854616)

[4.1.2.5 Post to General Ledger 48](#_Toc232854617)

[4.1.3 Acceptance 50](#_Toc232854618)

[4.1.3.1 Exporter Presentation 50](#_Toc232854619)

[4.1.3.2 Accept Presentation 52](#_Toc232854620)

[4.1.3.2.1 Reject and Reverse 52](#_Toc232854621)

[4.1.3.2.2 Accept and Settle 54](#_Toc232854622)

[4.1.3.2.3 Processing for Import Bill Advance Loan (Optional) 55](#_Toc232854623)

[4.1.3.2.4 Post to General Ledger 57](#_Toc232854624)

[4.1.4 Period-end Closing 59](#_Toc232854625)

[4.1.4.1 Perform Key Date Valuation 59](#_Toc232854626)

[4.1.5 Payment for Letter of Credit 61](#_Toc232854627)

[4.1.5.1 Edit Payment Details 61](#_Toc232854628)

[4.1.5.2 Create Netting Group 62](#_Toc232854629)

[4.1.5.3 Letter of Credit Payment 64](#_Toc232854630)

[4.1.5.3.1 Option 1: Generate and Automatically Process Payment Request 64](#_Toc232854631)

[4.1.5.3.2 Option 2: Generate and Process Payment Request 67](#_Toc232854632)

[4.1.5.3.3 Send Payment Medium File 73](#_Toc232854633)

[4.1.5.4 Bank Initiated Payment 74](#_Toc232854634)

[4.1.5.5 Post to General Ledger 74](#_Toc232854635)

[4.2 Receive Normal Letter of Credit 76](#_Toc232854636)

[4.2.1 Receive Normal Letter of Credit 76](#_Toc232854637)

[4.2.1.1 Receive Normal Letter of Credit 76](#_Toc232854638)

[4.2.1.2 Set Settlement Status 78](#_Toc232854639)

[4.2.1.3 Processing for Packing Loan (Optional) 80](#_Toc232854640)

[4.2.1.3.1 1WV - Create Packing Loan 80](#_Toc232854641)

[4.2.1.3.2 Link Reference with LC 80](#_Toc232854642)

[4.2.1.3.3 1WV- Further processing for Packing Loan 81](#_Toc232854643)

[4.2.2 Rollover Normal Letter of Credit 82](#_Toc232854644)

[4.2.2.1 Rollover Letter of Credit 82](#_Toc232854645)

[4.2.2.2 Set Settlement Status 83](#_Toc232854646)

[4.2.3 Presentation 84](#_Toc232854647)

[4.2.3.1 Exporter Presentation 84](#_Toc232854648)

[4.2.3.2 Send to Bank 86](#_Toc232854649)

[4.2.3.3 Accept by Bank and Settle 87](#_Toc232854650)

[4.2.3.4 Processing for Export Bill Advance Loan (Optional) 88](#_Toc232854651)

[4.2.3.4.1 1WV - Create Export Bill Advance Loan 88](#_Toc232854652)

[4.2.3.4.2 Edit Payment Details 89](#_Toc232854653)

[4.2.3.4.3 Link Export Bill Advance Loan 90](#_Toc232854654)

[4.2.3.4.4 Further Processing for Export Bill Advance Loan 91](#_Toc232854655)

[4.2.3.5 Post to General Ledger 91](#_Toc232854656)

[4.2.4 Period-end Closing 93](#_Toc232854657)

[4.2.4.1 Perform Key Date Valuation 94](#_Toc232854658)

[4.2.5 Make Collections for Letter of Credit 95](#_Toc232854659)

[4.2.5.1 Post to General Ledger 95](#_Toc232854660)

[4.3 Issue Standby Letter of Credit 98](#_Toc232854661)

[4.3.1 Issue Standby Letter of Credit 98](#_Toc232854662)

[4.3.1.1 Check Credit Line Limit (Optional) 98](#_Toc232854663)

[4.3.1.2 Create Facility (Optional) 98](#_Toc232854664)

[4.3.1.3 Set Settlement status (Optional) 99](#_Toc232854665)

[4.3.1.4 Check Facilities Utilization (Optional) 99](#_Toc232854666)

[4.3.1.5 Issue Standby Letter of Credit 99](#_Toc232854667)

[4.3.1.6 Set Settlement Status 102](#_Toc232854668)

[4.3.1.7 Standby Letter of Credit Fees and Cash Collateral Payment 103](#_Toc232854669)

[4.3.1.7.1 Display Payment Schedule 104](#_Toc232854670)

[4.3.1.7.2 Corporate Initiated Payment 105](#_Toc232854671)

[4.3.1.8 Bank Initiated Payment 113](#_Toc232854672)

[4.3.1.9 Post to General Ledger 113](#_Toc232854673)

[4.3.2 Rollover Standby Letter of Credit 116](#_Toc232854674)

[4.3.2.1 Roll over Standby Letter of Credit 116](#_Toc232854675)

[4.3.2.2 Set Settlement Status 117](#_Toc232854676)

[4.3.2.3 Standby Letter of Credit Fees and Cash Collateral Payment 118](#_Toc232854677)

[4.3.2.3.1 Display Payment Schedule 118](#_Toc232854678)

[4.3.2.3.2 Corporate Initiated Payment 120](#_Toc232854679)

[4.3.2.4 Bank Initiated Payment 129](#_Toc232854680)

[4.3.2.5 Post to General Ledger 129](#_Toc232854681)

[4.3.3 Terminate Standby Letter of Credit 132](#_Toc232854682)

[4.3.3.1 Terminate Standby Letter of Credit and Confirm Cash Collateral 132](#_Toc232854683)

[4.3.3.2 Automatic Utilize Facility 133](#_Toc232854684)

[4.3.3.3 Set Settlement Status 133](#_Toc232854685)

[4.3.3.4 Standby Letter of Credit Fees and Cash Collateral Payment 135](#_Toc232854686)

[4.3.3.4.1 Display Payment Schedule 135](#_Toc232854687)

[4.3.3.4.2 Corporate Initiated Payment 136](#_Toc232854688)

[4.3.3.5 Bank Initiated Payment 146](#_Toc232854689)

[4.3.3.6 Post to General Ledger 146](#_Toc232854690)

[4.4 Receive Standby Letter of Credit 148](#_Toc232854691)

[4.4.1 Receive Standby Letter of Credit 148](#_Toc232854692)

[4.4.1.1 Generate Limit Utilization 149](#_Toc232854693)

[4.4.1.2 Check Limit Utilization Report(Optional) 149](#_Toc232854694)

[4.4.1.3 Receive Standby Letter of Credit 149](#_Toc232854695)

[4.4.1.4 Set Settlement Status 151](#_Toc232854696)

[4.4.2 Roll Over Standby Letter of Credit 152](#_Toc232854697)

[4.4.2.1 Rollover Standby Letter of Credit 152](#_Toc232854698)

[4.4.2.2 Set Settlement Status 153](#_Toc232854699)

[4.4.3 Terminate Standby Letter of Credit 154](#_Toc232854700)

[4.4.3.1 Terminate Standby Letter of Credit 155](#_Toc232854701)

[4.4.3.2 Set Settlement Status 156](#_Toc232854702)

[4.5 Reports 157](#_Toc232854703)

[4.5.1 Define Financial Positions 157](#_Toc232854704)

[4.5.2 Financial Status (Nominal Amount) 158](#_Toc232854705)

[4.5.3 Display Treasury Alerts - Settlement, Payment, Release, Correspondence and Interest Rates 159](#_Toc232854706)

[4.5.4 Display Treasury Payments 160](#_Toc232854707)

[4.5.5 Display Treasury Posting Journal 161](#_Toc232854708)

[4.5.6 Display Treasury Posting Flows 162](#_Toc232854709)

[4.5.7 Display Treasury Position Values 163](#_Toc232854710)

[4.5.8 Display Treasury Alerts - Posting 163](#_Toc232854711)

[5 Appendix 165](#_Toc232854712)

[5.1 Notification for Managing Financial Transactions 165](#_Toc232854713)

[5.1.1 Create Teams and Responsibilities 166](#_Toc232854714)

[5.1.2 Enable Situation Types 167](#_Toc232854715)

[5.1.3 Create a Normal Letter of Credit 169](#_Toc232854716)

[5.1.4 Trigger and Schedule the Notifications 169](#_Toc232854717)

[5.1.5 User Setting for Notification 170](#_Toc232854718)

[5.1.6 Check the Notification in Fiori Launchpad and E-Mail 171](#_Toc232854719)

## Purpose

Overview

This scope item supports common functionalities of letters of credit, including deal capture, rollover, acceptance and presentation, payment and collections. In addition, it also provides the functions for cash collateral and fee calculation.

Both normal and standby letters of credit are covered, and they are defined as different product types.

Presently, we only support letters of credit without integration to Sales functionality.

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| SAP S/4HANA Cloud Public Edition system | Accessible via SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Treasury Specialist - Front Office | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |
| Treasury Specialist - Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE | Treasury Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE |  |
| Treasury Accountant | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |
| Treasury Risk Manager | SAP_BR_TREASURY_RISK_MANAGER | Treasury Analytics | SAP_BR_TREASURY_RISK_MANAGER |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Currency | AED |  |  |
| Company Foreign Currency1 | USD |  |  |
| Business Partner | 33537001 |  |  |
| Valuation Area | AE0 |  |  |
| House Bank | AEBK1 |  |  |
| Account ID | AEAC1 |  |  |

You can find general information on how to create master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1XN - Market Rates Management – Manually via Upload | Import the Market Data for Treasury and Risk Management. For example, Reference interest rate and exchange rate for local and foreign currency. |
| 1WV - Debt and Investment Management | Create Facility. For example, If a Facility needs to be assigned to Letter of Credit and the Facilities Utilization needs to be checked for Letter of Credit. |

### Preliminary Steps

In this section, you can provide a detailed step-by-step description of technical or other prerequisites that are valid for all process step, report, or items.

#### Create Business Partner

##### Maintain General Data for Business Partner

Procedure

Please follow the following section in the Debt and Investment Management (1WV) to create the necessary business partners.

- Maintain General Data for Business Partner

##### Maintain Payment Details for Business Partner

Procedure

Please follow the following chapter in the Debt and Investment Management (1WV) test script to create the necessary business partners.

- Maintain General Data for Business Partner

##### Maintain Authorizations for Business Partner

Procedure

Please follow the following chapter in the Debt and Investment Management (1WV) to create the necessary business partners.

- Maintain Authorizations for Business Partner

|  |
| --- |
| Note Please choose the Trade Finance checkbox. |

##### Maintain Reporting Data in Company Code for Business Partner

Purpose

In this step, you maintain reporting data in company code for business partner.

Procedure

Perporm the following step in the Debt and Investment Management (1WV) to create the necessary business partners:

- Maintain Reporting Data in Company Code for Business Partner

##### Maintain Additional Role for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the detailed steps on how to maintain additional roles required for Letter of Credit Management process for Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP) | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP. In the dialog box, enter following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change. | Change Organization: 33537001 screen is displayed. |  |
| 4 | Add New Role of TR00703 Bank | Select Change in BP Role to: for example, TR00703 BankChoose Save. | Data is saved. |  |

#### Maintain Limit with Limit Type Y01

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can create characteristic values for each combination of limit characteristics defined in a limit type.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Limits (TBL1) |  |  |
| 3 | Choose Limit Type | On the Manage Limits screen, select the row of Limit type Y01, then choose Create Limits, enter the following data in the dialog box and choose Continue:Company Code: for example, 3310 | The Edit Limits for Limit Type Y01: Create New Limit screen appears |  |
| 4 | Create Internal Limit Amount and External Limit Amount | On the Edit Limits for Limit Type Y01: Create New Limit screen, enter the following data and choose Save:Valid From Date: for example, <current date>Valid To (Internal): for example, 12/31/9999Valid To (External): for example, <Current Date + 1 year>Limit Currency: for example, AEDInternal Limit Amnt: for example, 250,000,000External Limit Amnt: for example, 200,000,000Critical Limit Utilizat.: for example, 90%Max. Risk Commit Per. Mth: for example, 999Limit: for example, <check> | The Edit Limits for Limit Types: Overview screen displays |  |

#### Maintain Trader and Trader Authorizations

Purpose

In this step, you will create Traders and maintain Trader Authorizations.

Procedure

Please follow the following chapter in the Debt and Investment Management (1WV) to create traders.

- Maintain Trader and Trader Authorizations

|  |
| --- |
| Note Please choose the Trade Finance checkbox for Trader authorizations. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| Issue Normal Letter of Credit |  |  |  |
| [(1XN) Market Rates Management – Manually via Upload](#unique_16) [page ] 19 |  |  |  |
| [Check Credit Line Limit (Optional)](#unique_17) [page ] 19 | Treasury Specialist - Front Office | Credit Line Analysis (FTR_CREDIT_LINE_ANALYSIS (FTR_CREDIT_LINE_ANALYSIS)) |  |
| [Create Facility (Optional)](#unique_18) [page ] 20 | Treasury Specialist - Front Office | Create Facility (TM_61) |  |
| [Settle Facility (Optional)](#unique_19) [page ] 20 |  |  |  |
| [Check Facilities Utilization (Optional)](#unique_20) [page ] 21 | Treasury Specialist - Front Office | Credit Line Analysis (FTR_CREDIT_LINE_ANALYSIS (FTR_CREDIT_LINE_ANALYSIS)) |  |
| [Issue Normal Letter of Credit](#unique_21) [page ] 21 | Treasury Specialist - Front Office | Create Letter of Credit (FTRTLC01) | Letter of credit created. |
| [Set Settlement Status](#unique_22) [page ] 133 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | Letter of credit settled. |
| [Letter of Credit Fees and Cash Collateral Payment](#unique_23) [page ] 25 |  |  |  |
| [Option 1: Generate and Automatically Process Payment Request](#unique_24) [page ] 25 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_25) [page ] 29 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_26) [page ] 31 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Post to General Ledger](#unique_27) [page ] 34 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) | Fee and cash collateral posted to general ledger. |
| [Rollover Letter of Credit](#unique_28) [page ] 37 | Treasury Specialist - Front Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | Letter of credit rolled over. |
| [Set Settlement Status](#unique_29) [page ] 38 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The rolled over letter of credit settled. |
| [Letter of Credit Fees and Cash Collateral Payment](#unique_30) [page ] 39 |  |  |  |
| [Option 1: Generate and Automatically Process Payment Request](#unique_31) [page ] 39 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_32) [page ] 43 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_33) [page ] 45 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Post to General Ledger](#unique_34) [page ] 48 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) | Fees and cash collateral posted to the general ledger. |
| [Acceptance](#unique_35) [page ] 50 |  |  |  |
| [Exporter Presentation](#unique_36) [page ] 50 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | Documents attached for presentation. |
| [Reject and Reverse](#unique_37) [page ] 52 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The presentation is rejected.The rejection is reversed. |
| [Accept and Settle](#unique_38) [page ] 54 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The presentation is accepted and saved. |
| [Post to General Ledger](#unique_39) [page ] 57 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) | The presentation amount is posted. |
| [Perform Key Date Valuation](#unique_40) [page ] 59 | Treasury Accountant | Run Valuation (TPM1) | The positions of financial instruments is valued on the key date. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_41) [page ] 105 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_42) [page ] 108 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_43) [page ] 110 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_44) [page ] 113 |  |  |  |
| [Post to General Ledger](#unique_45) [page ] 74 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) |  |
| Receive Normal Letter of Credit |  |  |  |
| [Receive Normal Letter of Credit](#unique_46) [page ] 76 | Treasury Specialist - Front Office | Create Letter of Credit (FTRTLC01) | Letter of credit created in the system |
| [Set Settlement Status](#unique_47) [page ] 117 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | Letter of credit is settled. |
| [Processing for Packing Loan (Optional)](#unique_48) [page ] 80 |  |  |  |
| [Rollover Letter of Credit](#unique_49) [page ] 82 | Treasury Specialist - Front Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | Letter of credit is rolled-over |
| [Set Settlement Status](#unique_50) [page ] 24 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The rolled-over letter of credit is settled. |
| [Exporter Presentation](#unique_51) [page ] 84 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | Documents uploaded for presentation. |
| [Send to Bank](#unique_52) [page ] 86 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) |  |
| [Accept by Bank and Settle](#unique_53) [page ] 87 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) |  |
| [Post to General Ledger](#unique_54) [page ] 91 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) |  |
| [Perform Key Date Valuation](#unique_55) [page ] 94 | Treasury Accountant | Run Valuation (TPM1) | The positions of financial instruments is valued on the key date. |
| [Post to General Ledger](#unique_56) [page ] 95 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) |  |
| Issue Standby Letter of Credit |  |  |  |
| [Check Credit Line Limit (Optional)](#unique_57) [page ] 98 |  |  |  |
| [Create Facility (Optional)](#unique_58) [page ] 98 |  |  |  |
| [Set Settlement status (Optional)](#unique_59) [page ] 99 |  |  |  |
| [Check Facilities Utilization (Optional)](#unique_60) [page ] 99 |  |  |  |
| [Issue Standby Letter of Credit](#unique_61) [page ] 99 | Treasury Specialist - Front Office | Create Standby Letter of Credit | Standby letter of credit is created |
| [Set Settlement Status](#unique_62) [page ] 151 |  |  | The standby letter of credit is settled. |
| [Standby Letter of Credit Fees and Cash Collateral Payment](#unique_63) [page ] 103 |  |  |  |
| [Display Payment Schedule](#unique_64) [page ] 104 | Treasury Accountant | Display Payment Schedules (TJ04) | Payment schedule is displayed. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_41) [page ] 105 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_42) [page ] 108 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_43) [page ] 110 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_44) [page ] 113 |  |  |  |
| [Post to General Ledger](#unique_65) [page ] 113 | Treasury Accountant | Fix, Pay and Post Flows (TBB1)Process Business Transactions (TPM10) |  |
| [Roll over Standby Letter of Credit](#unique_66) [page ] 116 | Treasury Specialist - Front Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The standby letter of credit is rolled-over |
| [Set Settlement Status](#unique_67) [page ] 78 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The rolled-over standby letter of credit is settled. |
| [Standby Letter of Credit Fees and Cash Collateral Payment](#unique_68) [page ] 118 |  |  |  |
| [Display Payment Schedule](#unique_69) [page ] 118 | Treasury Accountant | Display Payment Schedules (TJ04) | Payment schedule is displayed. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_70) [page ] 120 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_71) [page ] 123 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_72) [page ] 126 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_73) [page ] 129 |  |  |  |
| [Post to General Ledger](#unique_74) [page ] 129 | Treasury Accountant | Fix, Pay and Post Flows (TBB1)Process Business Transactions (TPM10) |  |
| [Terminate Standby Letter of Credit and Confirm Cash Collateral](#unique_75) [page ] 132 | Treasury Specialist - Front Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) |  |
| [Automatic Utilize Facility](#unique_76) [page ] 133 |  |  |  |
| [Set Settlement Status](#unique_77) [page ] 83 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) |  |
| [Standby Letter of Credit Fees and Cash Collateral Payment](#unique_78) [page ] 135 |  |  |  |
| [Display Payment Schedule](#unique_79) [page ] 135 | Treasury Accountant | Display Payment Schedules (TJ04) | Payment schedule is displayed. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_80) [page ] 136 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_81) [page ] 140 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_82) [page ] 142 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_83) [page ] 146 |  |  |  |
| [Post to General Ledger](#unique_84) [page ] 146 | Treasury Accountant | Fix, Pay and Post Flows (TBB1)Process Business Transactions (TPM10) |  |
| Receive Standby Letter of Credit |  |  |  |
| [Receive Standby Letter of Credit](#unique_85) [page ] 148 |  |  |  |
| [Generate Limit Utilization](#unique_86) [page ] 149 |  |  |  |
| [Check Limit Utilization Report(Optional)](#unique_87) [page ] 149 |  |  |  |
| [Receive Standby Letter of Credit](#unique_88) [page ] 149 | Treasury Specialist - Front Office | Create Standby Letter of Credit | Standby letter of credit is created in the system |
| [Set Settlement Status](#unique_89) [page ] 153 | SAP_BR_TREASURY_SPECIALIST_BOE | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The standby letter of credit is settled. |
| [Rollover Standby Letter of Credit](#unique_90) [page ] 152 | Treasury Specialist - Front Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The standby letter of credit is rolled over |
| [Terminate Standby Letter of Credit](#unique_91) [page ] 155 | Treasury Specialist - Front Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The standby letter of credit transaction is terminated. |
| [Set Settlement Status](#unique_92) [page ] 156 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The transaction is settled. |
| Report |  |  |  |
| [Financial Status (Nominal Amount)](#unique_93) [page ] 158 | Treasury Risk Manager | Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)) | The report displays with filtered data. |
| [Display Treasury Alerts - Settlement, Payment, Release, Correspondence and Interest Rates](#unique_94) [page ] 159 | Treasury Specialist - Back Office | Display Treasury Alerts (F4979)Display Treasury Alerts (F4980)Display Treasury Alerts (F4981)Display Treasury Alerts (F4983) | The report displays with filtered data. |
| [Display Treasury Payments](#unique_95) [page ] 160 | Treasury Specialist - Back Office | Display Treasury Payments (TPM20A) | The report displays with filtered data. |
| [Display Treasury Posting Journal](#unique_96) [page ] 161 | Treasury Accountant | Display Treasury Posting Journal (F1755) | The report displays with filtered data. |
| [Display Treasury Posting Flows](#unique_97) [page ] 162 | Treasury Accountant | Display Treasury Position Flows (F1754) | The report displays with filtered data. |
| [Display Treasury Position Values](#unique_98) [page ] 163 | Treasury Accountant | Display Treasury Position Values (F1867) | The report displays with filtered data. |
| [Display Treasury Alerts - Posting](#unique_99) [page ] 163 | Treasury Accountant | Display Treasury Alerts (F4984) | The report displays with filtered data. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Issue Normal Letter of Credit

In this section, you manage Letter of Credit lifecycle from the importer perspective.

#### Issue Normal Letter of Credit

##### (1XN) Market Rates Management – Manually via Upload

Purpose

In this step, you enter market data such as foreign currency exchange spot rates, swap rates, reference interest rates, etc into the system

These data provides default values when creating new transactions or calculating fair value for existing transactions.

Procedure

Please refer to the Market Rates Management – Manually via Upload (1XN) test script to import following market rates in the system:

- FX Spot Rates
- FX Swap Rates
- Reference Interest Rates

##### Check Credit Line Limit (Optional)

Purpose

In this step, you check credit line limit of a certain currency.

Procedure

Perform the following step in test script Debt and Investment Management (1WV):

- Check Credit Line Limit (Optional)

##### Create Facility (Optional)

###### Create Facility (Optional)

Purpose

In this step, you create the facilities master records as part of the daily business. In this release, you can only create bilateral facilities.

Procedure

Perform the following step in test script Debt and Investment Management (1WV):

- Create Facility (Optional)

|  |
| --- |
| Note Write down the transaction number for later use. |

###### Settle Facility (Optional)

Purpose

In this step, you settle the facility you created.

Procedure

Perform the following step in test script Debt and Investment Management (1WV):

- Set Settlement Status (Manual)

##### Check Facilities Utilization (Optional)

Purpose

In this step, you check the utilization status of facilities.

Procedure

Perform the following step in test script Debt and Investment Management (1WV):

- Check Facilities Utilization (Optional)

##### Issue Normal Letter of Credit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you request a commercial bank to issue a Letter of Credit for your company's oversea trade, normally the commercial bank will require your company to either provide cash collateral or consume your company's credit line facility in the bank. The commercial bank will also charge a letter of credit fee for this service.

In this step, you create a transaction for issuing Letter of Credit, and maintain relevant fee in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create Letter of Credit (FTRTLC01) | The Create Letter of Credit: Initial Screen view is displayed. |  |
| 3 | Enter Data on Initial View | On the Create letter of Credit: Initial Screen View, enter the following data and choose Enter.Company code: for example, 3310Product Type: for example, 85ATransaction Type: for example, 100Partner: for example, 33537001Currency: AEDContract: <select> | The data is entered and the Create Letter of Credit: Structure view is displayed. |  |
| 4 | Enter Data on Structure tab | On the Create Letter of Credit: Structure, enter the following data:Flow Type: 1860Amount: for example, 1MStart: for example, <current date>End: for example, <current date + 3 months>L/C Number: <for example,NLC201909150001 which should be unique in the system>Confirm.Instr.: WITHOUTPlace of Expiry: ShanghaiBeneficiary: for example, <search for a supplier with BP role FLVN00>Advising Bank: for example, 33537001Shipment Period: for example, <current date > - <current date + 3 month>In the Document group:Template: <choose LC Creation from F4 input help>and choose the Collateral tab.Note If there is no vendor master data with BP role FLVN00, you can refer to master data script Create Supplier Master - MDS (BNE) to create a supplier. | The data is entered and the Create Letter of Credit: Cash Collateralview is displayed. |  |
| 5 | Enter Data on Collateral tab | On the Create Letter of Credit: Cash Collateral view, in the Facility Assignment group, choose Create. In the Assignment: Facility dialog box, enter the following data and choose Choose:Company Code: for example, 3310Transaction: for example, <Facility transaction number noted down in previous step>In the Cash Collateral group, enter the following data:Flow Type: 1991Direction: -Payment Amount: for example, 333 AEDPayment Date: for example, <Current Date>At the bottom of the screen, choose Generate Incoming Collateral, and choose the Other Flows tab. | The data is entered and the Create Letter of Credit : Other Flowsview is displayed. |  |
| 6 | Enter Data on Other Flow tab | On the Create Letter of Credit: Other Flows view, enter following data:Line 1:Flow Type: 1900Direction: -Payment Amount: for example, 350Payment Currency: for example, AEDPayment Date: for example, <Current Date>and choose the Payment Details tab. | The data is entered and the Create Letter of Credit : Payment Detailsview is displayed. |  |
| 7 | Enter Data on Payment Details tab | On the Create Letter of Credit: Payment Details view, add a line item as follows:Direction: +Currency: AEDFlow Type: 1840Select the row with the + sign and flow type 1840, choose Payment Details.Make the following entries:Posting: to customerPayment Request: WithoutHouse Bank: AEBK1Account ID: AEAC1Payer/payee: <Beneficiary you entered on Structure tab>and choose Fee Conditions from the tool bar. | The Overview of Conditions view is displayed. |  |
| 8 | Enter Condition data | On the Overview of Conditions view, choose Create Fee Cond.In the Overview of Condition dialog box, double click on one condition type, for example, 1204.Enter following data and choose Copy.Eff. from: for example, <the current date> | The Condition Details view is displayed |  |
| 9 | Input Condition Detail | On the Condition: Details view, enter the following data and choose Back twice.Percentage Rate: for example, 0.5 |  |  |
| 10 | Save the transaction | Save the transaction.Note If the following messages is displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | Transaction data is saved. The following message displays:Financial transaction saved under number XXXXXXXXX XXXX.Write down this transaction number. |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you settle the letter of credit you created before you can do further processing. Normally this needs to be done once you receive the Letter of Credit from the bank.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On theTrade Finance: Collective Processing view, enter the following data and choose Run.Company Code: for example, 3310Transaction: for example, <Letter of Credit Transaction number noted down in the previous step>Note Keep the default values for all the other fields. | The transaction is displayed on Trade Finance: Collective Processing view. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing view, select the checkbox before the transaction and chooseSettle. |  |  |
| 5 | Upload the Letter of Credit Creation Document | Find the Document Section in Structure Tab, select one Doc. Type in the Documents List view, for example, Application, and choose Attachment. |  |  |
| 6 | Update the attachment | Choose New > New AttachmentUpload the attachment, and chooseCopy . | Number of Attachment will increase. |  |
| 7 | Settle the Transaction | On the Settle Letter of Credit : Structure view, choose SaveNote If the following messages display, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Letter of Credit transaction is settled. |  |

##### Letter of Credit Fees and Cash Collateral Payment

This section describes payment steps involved in Letter of Credit transactions, including payment of bank fees and cash collateral. If you exclude the collateral from the payment process in the previous step, then only bank fees will be handled.

###### Option 1: Generate and Automatically Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows.

Within these two apps, if you select the ‘Schedule Auto Payment Run’ option, system will automatically process the automatic payment run for payment requests.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <first payment Date you noted in previous procedure or current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows screen, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <first payment Date you noted in previous procedure or current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

###### Option 2: Generate and Process Payment Request

###### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows that require payment request. It does not create postings in financial accounting.

If the payment is initiated by the financial partner, skip this procedure and the following Process Payment Request procedure and continue with the Bank Initiated Payment procedure.

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Run:Trade Finance: <select>Company code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <first payment Date you noted in previous procedure or current date>Test Run: <select>Pay Only: <select>Note The first payment date is normally the same as current date. | The Payment Log - Test Run view displays. Review the payment information on this view.If the system displays the No flows exist for processing notification, no payment with payment request is needed for your selection criteria. Go to the succeeding Process Payment Request procedure. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following change:Test Run: <deselect>and choose Run. | The Payment Log view displays. A payment request is generated.Make a note of the key number: __________ |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <first payment Date you noted in previous procedure or current date>Test Run: <select>Note The first payment date is normally the same as current date. | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Back | Choose Back. | The Fix and Pay Flows view displays. |  |
| 5 | Production Run | Enter the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. A payment request is generated.Make a note of the key number: __________ |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use Automatic Payment Transactions for Payment Requests (F111) to start the Payment Program for Payment Requests. The payment program for payment requests app provides another automatic payment option in the SAP system. Unlike the standard payment program, the payments are based on payment requests, not on open items (vendor/customer items).

Prerequisites

A payment request is generated in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen displays. |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: For example, <current date>Identification: For example,TRM01 | The Automatic Payment Transactions: Parameters screen displays. |  |
| 4 | Enter Parameters | Enter the following data and choose Dynamic selections:Posting Date: For example, <current date>Next payment run on: For example, <current date + 1 months>Company Code: For example, 3310Payment Methods: For example, TF | The Free Selection for payment run dialog box displays. |  |
| 5 | Key Number | Enter the following data and choose Save:Key Number: <the key number you noted down in previous step> | The Automatic Payment Transactions: Parameters screen displays. |  |
| 6 | Additional Log | Choose Additional Log. | The Additional Log dialog box displays. |  |
| 7 | Enter Parameters | Make the following entries and choose Continue:Payment method selection in all cases: <select>Line items of the payment documents: <select>Due date check: <select>If the system displays the message Log created for all accounts displays, choose Continue.Choose Save on the Automatic Payment Transactions: Parameters screen. | The system displays the message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 8 | Schedule Proposal | Choose Proposal. | The Schedule Proposal dialog box displays. |  |
| 9 | Schedule Job | Select Start Immediat. and choose Schedule Job. | The system displays the message Proposal is running with a yellow traffic light. |  |
| 10 | Update Status | Choose Status until the message Payment proposal has been created displays in the status bar with green traffic light. | The payment proposal is generated. |  |
| 11 | Schedule Payment | Choose Pmnt run. | The Schedule Payment dialog box displays. |  |
| 12 | Schedule Job | Select Start Immediat., select Create Payment Medium and choose Schedule Job. | The message Payment run is running displays in the status bar with a yellow traffic light. |  |
| 13 | Update Status | Choose Status until the message Payment run has been carried out displays with a green traffic light. | The Automatic Payment Transactions for Payment Requests screen displays.The payment document is created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium is created if it uses PMW format. You can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you see the message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media. A BCM batch is created after the payment run. For more information, see the next test step. |  |
| 14 | Cross-Payment Run Payment Media (Create BCM Batch) | Choose Environment > Payment Medium > Cross-Payment Run Payment Medium > Create Payment Medium . | The Creation of Cross-Payment Run Payment Media screen displays. |  |
| 15 | Enter Data | Enter the following data and choose Run:Run Date: For example, <current date>Identification: For example, TRM01R | The Creation of Cross-Payment Run Payment Media dialog box displays with the message Collector XX/XX/20XX XXXXXX was created or updated. The BCM batch is created.A batch may need additional approvals before the payment medium is finally created. For more information, see the Advanced Cash Operations (J78) test script. |  |

###### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

##### Bank Initiated Payment

Purpose

When the outgoing payment is initiated by the bank, skip the Generate Payment Request and Process Payment Request procedures because no requests are required.

Procedure

When the bank initiates payment, skip to the Post to General Ledger procedure.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two SAP Fiori apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): This SAP Fiori app supports to generate posting for incoming payment and outgoing payment without payment request. You can not use this app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.
- Process Business Transactions (TPM10): You use this SAP Fiori app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.

Prerequisites

Outgoing payments handled using payment request were processed in the previous Generate Payment Request procedure with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data:Trade Finance: <select>Company code: For example, 3310Transaction: <transaction number with inflow or outflow which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select>Post Operational Only: Selectedand choose Execute: | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created during a test run.If the system displays the No flows exist for processing notification, no posting is needed for your selection criteria.You can skip the next steps and continue with step 6, using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: <deselect> | The Posting Log: Posted Business Transactions view displays. The accounting document is created for incoming payment in the local GAAP (valuation area AE0). |  |
| 6 | Access another SAP Fiori app | Return to the SAP Fiori launchpad and open Process Business Transactions (TPM10). | The Process Business Transactions view is displayed. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select>Company Code: For example, 3310Valuation Area: For example, AE0Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: <select>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select>and choose Execute. | The Test Run: Post/Reverse Business Transactions view displays.If the system displays the You have not selected any business transactions notification, no postings are needed for your selection criteria. You can skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created during a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions view is displayed. |  |
| 11 | Deselect Test Run | Make the following change:Test Run: <deselect>and choose Execute. | The Update Run: Post/Reverse Business Transactions view is displayed. |  |
| 12 | Production Run | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in the local GAAP (valuation area AE0). |  |

#### Rollover Letter of Credit

After the Letter of Credit is issued by the bank, in case the amount or validity term of the Letter of Credit needs to be changed, you can negotiate with the bank to adjust the amount or term of Letter of Credit. Once the bank agrees to do the adjustment, you can roll over the Letter of Credit in the SAP S/4HANA Cloud Public Edition system by changing the Letter of Credit amount or end of term.

##### Rollover Letter of Credit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you roll over the Letter of Credit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company code: for example, 3310Transaction: for example, <transaction number you noted from the previous procedure>Term End: for example, <current date>Accept default values for other parameters and choose Run. | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Enter Rollover dates | On Trade Finance: Collective Processing view, select the checkbox before the transaction, and choose Roll Over.On Roll Over Letter of Credit: Structure view, enter following data:End: for example, <current date + 4 months>Choose Save. | The transaction has been rolled over successfully.The following message is displayed on Trade Finance: Collective Processing view:Financial transaction saved under number 100000000XXXX |  |
| 5 | Change the incoming Cash Collateral payment date | On the Roll Over Letter of Credit: Cash Collateral view, change the payment date of the second line as below, and choose Save:Payment date: <current date + 4 months>Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working dayTerm end changed; consider pymnt date of cash collateral incoming line | The transaction has been rolled over successfully.The following message is displayed on the Trade Finance: Collective Processing view:Financial transaction saved under number 100000000XXXX |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you roll over a Letter of Credit transaction, you need to settle it before you can proceed with further processes. Normally, you need to settle the transaction once you've received the updated Letter of Credit from the bank.

In this step, you settle the rolled-over Letter of Credit transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data and choose Run.Company Code: for example, 3310Transaction: for example, <Transaction number you noted down in previous step>Note Keep the default values for all the other fields. |  |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing view, choose the checkbox before the transaction created in previous step, and select Settle.On the Settle Letter of Credit: Structure view, choose Save.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Letter of Credit transaction is settled. The following message is displayed:Financial transaction saved under number 100000000XXXX.Note If you choose Display on the Trade Finance: Collective Processing view, you should see the transaction is now in the Rollover Settlement status. |  |

##### Letter of Credit Fees and Cash Collateral Payment

The updated Letter of Credit normally comes with the new Bank Fees and Collateral. The process of these payments is the same as the process in the [Letter of Credit Fees and Cash Collateral Payment](#unique_23) [page ] 25 step of the previous section.

###### Option 1: Generate and Automatically Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows.

Within these two apps, if you select the ‘Schedule Auto Payment Run’ option, system will automatically process the automatic payment run for payment requests.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <the current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows screen, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <the current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

###### Option 2: Generate and Process Payment Request

###### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows that require payment request. It does not create postings in financial accounting.

If the payment is initiated by the financial partner, skip this procedure and the following [Process Payment Request](#unique_33) [page ] 45 procedure and continue with the [Bank Initiated Payment](#unique_105) [page ] 48 procedure.

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <the current date>Test Run: <select>Pay Only: <select> | The Payment Log - Test Run view is displayed. Review the payment information on this view.If the No flows exist for processing message is displayed, no payment with payment request is needed for your selection criteria. Go to the succeeding [Post to General Ledger](#unique_34) [page ] 48 procedure. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following change:Test Run: <deselect>and choose Run. | The Payment Log view is displayed. A payment request is generated.Make a note of the key number: __________ |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <the current date>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Back | Choose Back. | The Fix and Pay Flows view displays. |  |
| 5 | Production Run | Enter the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. A payment request is generated.Make a note of the key number: __________ |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this app to start the Payment Program for Payment Requests. The payment program for payment requests app provides another automatic payment option in the SAP system. Unlike the standard payment program, the payments are based on payment requests, not on open items (vendor/customer items).

Prerequisites

A payment request is generated in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen displays. |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: For example, <current date>Identification: For example,TRM02 | The Automatic Payment Transactions: Parameters screen displays. |  |
| 4 | Enter Parameters | Enter the following data and choose Dynamic selections:Posting Date: For example, <current date>Next payment run on: For example, <current date + 4 months>Company Code: For example, 3310Payment Methods: For example, TF | The Free Selection for payment run dialog box displays. |  |
| 5 | Key Number | Enter the following data and choose Save:Key Number: <the key number you noted down in previous step> | The Automatic Payment Transactions: Parameters screen displays. |  |
| 6 | Additional Log | Choose Additional Log. | The Additional Log dialog box displays. |  |
| 7 | Enter Parameters | Make the following entries and choose Continue:Payment method selection in all cases: <select>Line items of the payment documents: <select>Due date check: <select>If the system displays the message Log created for all accounts displays, choose Continue.Choose Save on the Automatic Payment Transactions: Parameters screen. | The system displays the message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 8 | Schedule Proposal | Choose Proposal. | The Schedule Proposal dialog box displays. |  |
| 9 | Schedule Job | Select Start Immediat. and choose Schedule Job. | The system displays the message Proposal is running with a yellow traffic light. |  |
| 10 | Update Status | Choose Status until the message Payment proposal has been created displays in the status bar with green traffic light. | The payment proposal is generated. |  |
| 11 | Schedule Payment | Choose Pmnt run. | The Schedule Payment dialog box displays. |  |
| 12 | Schedule Job | Select Start Immediat., select Create Payment Medium and choose Schedule Job. | The message Payment run is running displays in the status bar with a yellow traffic light. |  |
| 13 | Update Status | Choose Status until the message Payment run has been carried out displays with a green traffic light. | The Automatic Payment Transactions for Payment Requests screen displays.The payment document is created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium is created if it uses PMW format. You can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you see the message Payment run XX/XX/20XX TRM02R is intended for cross-payment run payment media. A BCM batch is created after the payment run. For more information, see the next test step. |  |
| 14 | Cross-Payment Run Payment Media (Create BCM Batch) | Choose Environment > Payment Medium > Cross-Payment Run Payment Medium > Create Payment Medium . | The Creation of Cross-Payment Run Payment Media screen displays. |  |
| 15 | Enter Data | Enter the following data and choose Run:Run Date: For example, <current date>Identification: For example, TRM02R | The Creation of Cross-Payment Run Payment Media dialog box displays with the message Collector XX/XX/20XX XXXXXX was created or updated. The BCM batch is created.A batch may need additional approvals before the payment medium is finally created. For more information, see the Basic Cash Operations (BFB) test script. |  |

###### Send Payment Medium File

##### Bank Initiated Payment

Purpose

When the outgoing payment is initiated by the bank, skip the [Generate Payment Request](#unique_32) [page ] 43 and [Send Payment Medium File](#unique_106) [page ] 48 procedures because no requests are required.

Procedure

When the bank initiates payment skip to the [Post to General Ledger](#unique_34) [page ] 48 procedure.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two SAP Fiori apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): This SAP Fiori app supports to generate posting for incoming payment and outgoing payment without payment request. You can not use this app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.
- Process Business Transactions (TPM10): You use this SAP Fiori app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.

Prerequisites

Outgoing payments handled using payment request were processed in the previous Generate Payment Request procedure with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data:Trade Finance: <select>Company code: For example, 3310Transaction: <transaction number with inflow or outflow which was created in previous steps>Up to and Including Due Date: Enter date on which the flow of financial transaction should be posted, for example, <current date + 3 months>Test Run: <select>Post Operational Only: <select>and choose Execute: | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created during a test run.If the system displays the No flows exist for processing notification, no posting is needed for your selection criteria.You can skip the next steps and continue with step 6, using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: <deselect> | The Posting Log: Posted Business Transactions view displays. The accounting document is created for incoming payment in the local GAAP (valuation area AE0). |  |
| 6 | Access another SAP Fiori App | Return to the SAP Fiori launchpad and open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select>Company Code: For example, 3310Valuation Area: For example, AE0Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: <select>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select>and choose Execute. | The Test Run: Post/Reverse Business Transactions view displays.If the system displays the You have not selected any business transactions notification, no postings are needed for your selection criteria. You can skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view displays. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created during a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions view displays. |  |
| 11 | Deselect Test Run | Make the following change:Test Run: <deselect>and choose Execute. | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 12 | Production Run | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view displays. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in the local GAAP (valuation area AE0). |  |

#### Acceptance

In this section, you make payment upon notification from the issuing bank about the obligation to pay for the L/C.

##### Exporter Presentation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you upload L/C relevant documents presented by exporter into the system after the goods shipment.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <Letter of Credit Transaction number>Term End: for example, <current date>Accept default values for other parameters and choose Run. | The Letter of Credit transaction you created before is displayed. |  |
| 4 | Select the transaction for Presentation | On the Trade Finance: Collective Processing view, select the transaction, and choose Present. | The Change Letter of Credit: Presentation view is displayed. |  |
| 5 | Enter Presentation data | On the Presentation tab of the Change Letter of Credit: Presentationview, choose Insert Row, and enter the following data:Presentation Item: for example, 1Shipment Date: for example, <current date + 10 days>Presentation Date: for example, <current date + 10 days>Payment Date: for example, <current date + 1 month>Presentation Amount: 0.8MDouble click on the presentation itemNote Both presentation date and payment date should within the LC term and apply to the setting of presentation period/payment period defined in the Structure tab. Presentation date should be earlier than payment date and later than shipment date. | The Change Letter of Credit: Presentation detail view is displayed.Note Multiple presentations are allowed.There would be warning message if total net presentation amount exceeds the LC amount (with tolerance) |  |
| 6 | View Documents List | In the Documents section, select one Doc. Type in the Documents List view, for example, Beneficiary's statement.Choose the button under column Attachment. | The Attachment List view is displayed. |  |
| 7 | Added Attachments for Presentation | Choose New > Create Attachment .Upload the attachment, and choose Copy.Note You may encounter a File Upload window saying, The application wants to upload a file to the SAP system, choose OK to continue. |  |  |
| 8 | Added Attachments for Presentation | You can upload all the documents by above steps if it is need.Then choose Save. | Msg Financial Transcation saved under number XXXXX is displayed. |  |

##### Accept Presentation

In this section, you check the presentation documents, and accept or reject the presentation in the system. If you accept the presentation, you post it to general account. After posting, a financial document and an L/C payable open item are generated.

###### Reject and Reverse

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can reject the exporter presentation in case of missing documents required under the letter of credit or any other compliance issues.

Prerequisite

You have settled the Letter of Credit in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <transaction number you noted from the previous procedure>Term End: for example, <current date >Accept default values for other parameters and choose Run. | The Letter of Credit transaction you created before is displayed. |  |
| 4 | Select the Presentation | On Trade Finance: Collective Processing view, select the presentation entry of the transaction, and choose Reject. | The Change Letter of Credit: Presentation view displays.If you have several presentations for the same letter of credit, there may be multiple presentation entries show up. Select one you want to reject. |  |
| 5 | Input Reject Reason and save the rejection | In the Reject Reason screen, enter the reject reason, for example, 01 Document Issue, and choose Save twice to save the changes. | Msg Financial Transaction saved under number XXXXX is displayed. |  |
| 6 | Back to the original view | On the Trade Finance: Collective Process view, choose Back and then choose Run. |  |  |
| 7 | Reverse the Reject | In the Trade Finance: Collective Process view, select the presentation item you reject before, and choose Reverse. | The Reverse Confirmation screen is displayed. |  |
| 8 | Save the Reverse | In the Reverse Confirmation screen, enter the reverse reason, for example, 01 Reversal due to processing error by clerk, and choose Save twice to save the changes. | Msg Financial Transaction saved under number XXXXX is displayed. |  |

###### Accept and Settle

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you accept and settle the exporter presentation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <transaction number for Letter of Credit>Term End: for example, <current date >Accept default values for other parameters and choose Run. | The Letter of Credit transaction you created before is displayed. |  |
| 4 | Select and accept the transaction for Presentation | On the Trade Finance: Collective Processing view, select the presentation item of the transaction, and choose Accept. | The Change Letter of Credit: Presentation view is displayed.If you have several presentations for the same letter of credit, there may be multiple presentation entries shown up. Select one that you want to accept. |  |
| 5 | Settle the Presentation | On the Change Letter of Credit: Presentation view, check the details of the presentation, for example, the documents attached and presentation amount.Choose Settle.Note If the Not all documents are accepted message is displayed, just skip it. |  |  |
| 6 | Save the accept and Settle | Choose Save. | Msg Financial Transaction saved under number XXXXX is displayed. |  |

###### Processing for Import Bill Advance Loan (Optional)

|  |
| --- |
| Note Please use configuration activity Define Transaction Types - Trade Finance Transactions to maintain the product type 55A and transaction type 200 as the underlying of product type 85A and transaction type 100 before you perform the following steps. |

###### 1WV - Create Import Bill Advance Loan

Purpose

In this step, you create an import bill advance loan by creating an interest rate instrument according to relevant steps in the Debt and Investment Management (1WV) test script.

Procedure

Follow the Create IR Instrument and Set Settlement Status chapters in the Debt and Investment Management (1WV) test script to create and settle transaction with product type 55A and transaction type 200.

|  |
| --- |
| Note Note down the transaction number as loan number to be used in the next step.Make sure that the Amount is within presentation amount. And for netting purpose, make sure that the start date of import bill advance loan is as the same as Payment Date of issued L/C. |

###### Link Import Bill Advance Loan

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you link the interest rate instrument you created in the previous step as import bill advance loan to the letter of credit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <transaction number you noted from the previous procedure>Term End: for example, <current date>Accept default values for other parameters and choose Run. | The Letter of Credit transaction you created before is displayed. |  |
| 4 | Select and presentation | On the Trade Finance: Collective Processing view, select the presentation entry which you want to link the import advance loan, and choose Change. | The Change Letter of Credit: Presentation view is displayed.Note If you have several presentations for the same letter of credit, there may be multiple presentation entries shown up. Select one you want to apply for the import bill advance loan. |  |
| 5 | Link import bill advance loan for the presentation | On the Presentation tab of the Change Letter of Credit: Presentation view, double click on the presentation you accepted and settled before.Scroll down to the bottom, and choose Link Import Bill Advance Loan in the Financing section. | The Link Import Bill Advance Loan view is displayed. |  |
| 6 | Enter Data in Import Bill Advance Loan view | On the Link Import Bill Advance Loan view, enter the Transaction in Object to Be Linked section or enter the Loan Number you created in the previous step to link it to this presentation.Choose Save | Message Reference created is displayed. |  |
| 7 | Save the change | Choose Save to save the change. | Message Financial Transcation saved under number XXXXX is displayed. |  |

###### Loan Further Processing

Purpose

In this step, you further process the import bill advance loan in the system, for example, loan's Interest Payment, loan is Mature, loan's termination. Please refer to the Debt and Investment Management （1WV） test script for how to further process a loan.

###### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two SAP Fiori apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this SAP Fiori app to generate posting for incoming payment and outgoing payment without payment request.
- Process Business Transactions (TPM10): Use this SAP Fiori app to generate postings for outgoing payments that have been processed via app Fix, Pay and Post Flows (TBB1) with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data:Trade Finance: <select>Company code: For example, 3310Transaction: <transaction number for Letter of Credit you created in the previous step>Up to and Including Due Date: Enter date on which the flow of financial transaction should be posted, for example, <current date + 10 days>Test Run: <select>Post Operational Only: <select>and choose Execute: | The Posting Log: Posted Business Transactions view is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created during a test run.If the system displays the No flows exist for processing notification, no posting is needed for your selection criteria.You can skip the next steps and continue with step 6, using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: <deselect> | The Posting Log: Posted Business Transactions view is displayed. The accounting document is created for incoming payment in the local GAAP (valuation area AE0). |  |
| 6 | Access Another SAP Fiori App | Return to the SAP Fiori launchpad and open Process Business Transactions (TPM10). | The Process Business Transactions view is displayed. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select>Company Code: For example, 3310Valuation Area: For example, AE0Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: <select>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select>and choose Execute. | The Test Run: Post/Reverse Business Transactions view is displayed.If the You have not selected any business transactions message is displayed, no posting is needed for your selection criteria. You can skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created during a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions view is displayed. |  |
| 11 | Deselect Test Run | Make the following change:Test Run: <deselect>and choose Execute. | The Update Run: Post/Reverse Business Transactions view is displayed. |  |
| 12 | Production Run | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view is displayed. The accounting document is created for outgoing payment in the local GAAP (valuation area AE0). |  |

#### Period-end Closing

Purpose

In this section, you make period-end closing in the system, for example, month-end closing.

##### Perform Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you use the valuation function to value the positions of financial instruments based on historical cost or fair value for a given key date, and transfer the results to financial accounting.

Prerequisites

You have imported market data into the system, as described in the [Business Conditions](#unique_6) [page ] 8 chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Execute Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Transaction: <transaction number for Letter of Credit you created in previous steps>Key Date for Valuation: for example, <last date of current month>Note Make sure the Key Date for Valuation is between the Presentation Date and the Payment Date.Valuation Category: for example, Mid-year Valuation with ResetWhen the period end is also the year end, use the Valuation Category Year End Valuation.Test Run: <select> | The Display Positions to be Valued screen is displayed. |  |
| 4 | Execute Valuation for Test Run | Choose Run Valuation.If a Message dialog box displays, choose Continue. | The Valuation Log screen is displayed. If a red traffic light is shown, click on it and check the error message. Solve the issue and perform a test run again until you resolve the error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. There is no posting created because it is a test run.Note Sometimes, there is no simulated posting because your selected transaction may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: <deselect> | The Display Positions to be Valued screen is displayed. |  |
| 6 | Execute Valuation for Production Run | Choose Execute Valuation. | The Valuation Log screen is displayed. Check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. The accounting document is created in the local GAAP (valuation area AE0). |  |

#### Payment for Letter of Credit

##### Edit Payment Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

By default the loan you created will have payment request marked. You need change the default setting for Import Bill advance loan.

Prerequisite

A TRM transaction is created successfully in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process MM Transactions - Collective Processing (TM00). | The Money Market: Collective Processing view displays. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data:Company Code: for example, 3310Transaction: <Transaction Number for bill advance loan created in previous step>Accept default values for other parameters.and choose Execute. | The transaction is displayed in the next view. |  |
| 4 | Settle the TRM transaction | On the Money Market: Collective Processing view, select the checkbox at the head of the transaction line and choose Change. | Change Interest Rate Instrument view displays with the transaction data. |  |
| 5 | Switch to the payment details | On the Change Interest Rate Instrument view, choose Payment details tab. | The Payment details for the Import Bill Advance loan view displays |  |
| 6 | Change Payment Details for Export Bill Advance Loan Transaction | For netting purpose, select the row with the + sign and choose Payment Details. Make the following entries and choose Save:Payment Request: <select>Payer/Payee: 33537001Payment Methods: <Payment methods of outgoing flow which maintained in payment details of issued L/C that created in the previous steps, for example, T>Partner Bank: AED1 | The transaction has saved for the changes. |  |

##### Create Netting Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you net the import bill advance loan with the letter of credit to create a netting group.

You may use the following apps related with Netting:

- Create Netting (TBR1)
- Change Netting (TBR2)
- Display Netting (TBR3)
- Undo Netting (TBR4)
- Display Netting Proposals (TBR5)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Create Netting (TBR1). | The Create Netting: Initial screen is displayed. |  |
| 3 | Enter parameters in the initial view | Make the following entries and choose Enter:Company Code: 3310Payment Date: <Start date of import bill advance loan, or Payment Date of issued L/C which maintained in transactions that created in previous steps>1st Transaction: <transaction number of import bill advance loan created in the previous step>2nd transaction:< transaction number of issued L/C created in previous step> | The transaction is displayed in the Proposal List for Netting view. |  |
| 4 | Create the Netting Group | The two transaction with product type 85A and 55A are displayed.Choose Save. | The Netting created message shows up.Note Make a note of the Netting Number: __________ |  |

##### Letter of Credit Payment

In this section, you pay for the part of the presentation amount that hasn't been applied for loan.

###### Option 1: Generate and Automatically Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows.

Within these two apps, if you select the ‘Schedule Auto Payment Run’ option, system will automatically process the automatic payment run for payment requests.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number of Letter of Credit>Up to and Including Due Date: <Current Date + 4 months>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows screen, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number of Letter of Credit>Up to and Including Due Date: <Current Date + 4 months>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

###### Option 2: Generate and Process Payment Request

###### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request is selected as required (usually only for outgoing payment, in practice). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows that require payment request, which does not generate posting in financial accounting.

When payment is initiated by the financial partner, skip this procedure and the [Process Payment Request](#unique_118) [page ] 70 procedure and continue with the [Post to General Ledger](#unique_45) [page ] 74 procedure.

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number of Letter of Credit>Up to and Including Due Date: <Current Date + 4 months>Test Run: <select this checkbox>Pay Only: <select this indicator> | The Payment Log - Test Run screen is displayed. Review the payment information on this view.If the No flows exist for processing message is displayed, then there is no payment required for the payment request according to your selection criteria and you can skip to the [Post to General Ledger](#unique_45) [page ] 74 procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect this checkbox> | Payment log is displayed and payment requests are generated.The key is displayed in the Payment Log screen. Make a note of the payment request key numbers: __________ |  |
| 5 | Access the SAP Fiori App | Go back to the Fix, Pay and Post Flows view. | The Fix, Pay and Post Flows screen is displayed. |  |
| 6 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Money Market: <select this checkbox>Company code: for example, 3310Transaction: <transaction number of import bill advance loan created in previous steps>Up to and Including Due Date: enter date when the flow of financial transaction should be posted, for example, Treasury: Post Flows<Start date of import bill advance loan created in previous steps>Test Run: <select this checkbox>Pay Only: <select this indicator> |  |  |
| 7 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect this checkbox> | Payment log is displayed and payment requests are generated.The key is displayed in the Payment Log screen. Make a note of the payment request key numbers: __________ |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number of Letter of Credit>Up to and Including Due Date: <Current Date + 4 months>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, change the following data and choose Run:Test Run: <deselect> | The Payment Log view displays. A payment request is generated.Make a note of the key number: __________ |  |
| 5 | Access the SAP Fiori App | Go back to the Fix and Pay Flows view. | The Fix and Pay Flows view displays. |  |
| 6 | Test Run | On the Fix and Pay Flows view, enter the following data and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number of import bill advance loan created in previous steps>Up to and Including Due Date: enter date when the flow of financial transaction should be posted, for example, <Start date of import bill advance loan created in previous steps>Test Run: <select> |  |  |
| 7 | Production Run | Choose Back:On the Fix and Pay Flows view, change the following data, and choose Run:Test Run: <deselect> | Payment log is displayed and payment requests are generated.The key is displayed in the Payment Log screen. Make a note of the payment request key numbers: __________ |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you use the Automatic Payment Transactions for Payment Requests (F111) app to start the Payment Program for Payment Requests. The Payment Program for Payment Requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items), but on payment requests.

Prerequisite

Payment request is generated, from the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests view is displayed. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests view, enter the following data, and choose Maintain payment run parameters:Run Date: for example, <current date>Identification: for example, TRM02 | The Automatic Payment Transactions: Parameters view is displayed. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters view, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 3 months>Company Code: for example, 3310Payment Methods: for example TFChoose Dynamic selections, on the Free Selection for payment run dialog box, enter the following data, and choose Save:Key number: <the key numbers you noted from the issued L/C and import advance loan generated in the previous procedures>Choose Additional Log, on the Additional Log dialog box, enter the following data, and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select this checkbox>Due date check: <select this checkbox>Note If the Log created for all accounts message is displayed, choose Continue.Choose Save on the Automatic Payment Transactions: Parameters view. | The Parameters have been entered message is displayed on the Automatic Payment Transactions for Payment Requests view. |  |
| 5 | Schedule Proposal | Choose Schedule proposal..On the Schedule Proposal dialog box, choose Start Immediate and choose Schedule Job to confirm this dialog box.The Proposal is running message is displayed in the status bar with a yellow traffic light status.Choose Update status, until the Payment proposal has been created message is displayed in the status bar with green traffic light status.NoteIf you choose Edit Proposal, choose Continue on Accounting clerk view, the Edit Payment Proposal: Payments view is displayed.You should see one line with greenlight on the Edit Payment Proposal: Payments view.If there is only one line with red light or even other error messages is displayed, then the payment proposal is not successful. In this case, you need to check and correct the error so that you can continue to do the next step of this test. | Payment proposal is generated. |  |
| 6 | Schedule Payment | Choose Schedule payment.On the Schedule Payment dialog box, choose Start Immediat. and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.The Payment run is running message is displayed in the status bar with yellow traffic light status.Choose Update status, until the Payment run has been carried out message is displayed with green traffic light status. | The payment document is created.If SAP Bank Communication Management is not implemented in your system, the payment medium created uses the PMW format. To review the medium, select the Display payment log.If SAP Bank Communication Management is implemented in your system, in the Display payment log, the Payment run XX/XX/20XX, TRM02R is intended for cross-payment run payment media message is displayed, then a SAP Bank Communication Management batch is created after the payment run. Proceed to the following step. |  |
| 7 | Cross-Payment Run Payment Media (Create SAP Bank Communication Batch) | The following step only applies if SAP Bank Communication Management is implemented in your system,On the Automatic Payment Transactions for Payment Requests view, choose Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data, and choose Run:Run Date: for example <current date>Identification: for example TRM02R | The Creation of Cross-Payment Run Payment Media dialog box is displayed and states that Collector XX/XX/20XX XXXXXX was created or updated confirming that the SAP Bank Communication Management batch is created.Note A batch may require additional approvals before payment medium is finally created. For more information, see the Basic Cash Operations (BFB) test script. |  |

###### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

##### Bank Initiated Payment

Purpose

When the outgoing payment is initiated by the bank, skip the [Generate Payment Request](#unique_117) [page ] 67 and [Process Payment Request](#unique_118) [page ] 70 procedures because no requests are required.

Procedure

When the bank initiates payment, skip to the [Post to General Ledger](#unique_45) [page ] 74 procedure.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two SAP Fiori apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): This SAP Fiori app supports to generate posting for incoming payment and outgoing payment without payment request. You can not use this app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.
- Process Business Transactions (TPM10): You use this SAP Fiori app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.

Prerequisites

Outgoing payments handled using payment request were processed in the previous Generate Payment Request procedure with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data:Trade Finance: <select>Company code: For example, 3310Transaction: <transaction number with inflow or outflow which was created in previous steps>Up to and Including Due Date: Enter date on which the flow of financial transaction should be posted, for example, <current date date + 4 months>Test Run: <select>Post Operational Only: <select>and choose Execute: | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created during a test run.If the system displays the No flows exist for processing notification, no posting is needed for your selection criteria.You can skip the next steps and continue with step 6, using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: <deselect> | The Posting Log: Posted Business Transactions view displays. The accounting document is created for incoming payment in the local GAAP (valuation area AE0). |  |
| 6 | Access another SAP Fiori App | Return to the SAP Fiori launchpad and open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select>Company Code: For example, 3310Valuation Area: For example, AE0Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: <select>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select>and choose Execute. | The Test Run: Post/Reverse Business Transactions view displays.If the system displays the You have not selected any business transactions notification, no postings are needed for your selection criteria. You can skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view displays. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created during a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions view displays. |  |
| 11 | Deselect Test Run | Make the following change:Test Run: <deselect>and choose Execute. | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 12 | Production Run | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view displays. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in the local GAAP (valuation area AE0). |  |

### Receive Normal Letter of Credit

In this section, you manage Letter of Credit lifecycle from the exporter perspective.

#### Receive Normal Letter of Credit

##### Receive Normal Letter of Credit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you enter the information of letter of credit into the system after you are informed by the advising bank of the receipt of the letter of credit issued by the importer.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Letter of Credit (FTRTLC01). | The Create Letter of Credit: Initial view is displayed. |  |
| 3 | Enter Data on Initial View | On the Create letter of Credit: Initial view, enter the following data and choose Enter:Company code: for example, 3310Product Type: for example, 85ATransaction Type: for example, 200Partner: for example, 33537001Contract: <select> | The data is entered and Create Letter of Credit : Structure view is displayed. |  |
| 4 | Enter Data on Structure tab | On the Create Letter of Credit: Structure, enter the following data:Flow Type: 1860Amount: for example, 1MStart: for example, <Current Date>End: for example, <Current Date + 3 months>Confirm.Instr. : WITHOUTPlace of Expiry: ShanghaiApplicant: for example, <search for a customer with BP role FLCU00>Issuing Bank: for example, 33537001L/C Number: for example, NLC201909150002， which should be unique in the systemShipment Period: for example， <current date > - <current date + 1 month>In the Document section,Template： <select LC Creation from the value help>Note If there is no customer master data with BP role FLCU00, then you can either enter 33537001 or refer to the Create Customer Master - MDS (BND) master data script to create a customer. | The data is entered and the Create Letter of Credit: Cash Collateralview is displayed. |  |
| 5 | Enter Data on Payment Details tab | On the Create Letter of Credit : Payment Details view, add a line item as follows:Direction: -Currency: AEDFlow Type: 1840Select the row with the - sign and flow type 1840, choose Payment Details.Make the following entries:Posting: to customerPayment Request: WithoutHouse Bank: AEBK1Account ID: AEAC1Payer/payee: <the Applicant you entered on Structure tab> | The Overview of Payment Details view is displayed. |  |
| 6 | Save the transaction | Choose Back and Save the transaction.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | Transaction data is saved. The following message is displayed:Financial transaction saved under number XXXXXXXXX XXXX.Note Write down this transaction number. |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you settle the letter of credit you created before you can do further processing. Normally this needs to be done once you receive the Letter of Credit from the bank.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On theTrade Finance: Collective Processing view, enter the following data and choose Run.Company Code: for example, 3310Transaction: <Letter of Credit Transaction number you noted down in the previous step>Note Keep the default values for all the other fields | The transaction is displayed on Trade Finance: Collective Processing view. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing view, choose the checkbox before the transaction created, and choose Settle. |  |  |
| 5 | Upload the Letter of Credit Creation Document | In the Document section of the Structure tab,select one Doc. Type in the Documents List view, for example, Application.Double click on the selected attachment icon in the line. | The Attachment List view is displayed. |  |
| 6 | Update the attachment | Choose New > New Attachment .Upload the attachment.Choose Copy. | The number of Attachment increases. |  |
| 7 | Update the attachment | Repeat the above steps to attach all the document related for LC creation. | The number of Attachment increases. |  |
| 9 | Settle the Transaction | On the Settle Letter of Credit: Structure view, choose Save.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Letter of Credit transaction is settled. The following message is displayed: Financial transaction saved under number XXXXXXXXXXXXXX. |  |

##### Processing for Packing Loan (Optional)

Purpose

After you receive the letter of credit, you can apply the packing loan against the L/C.

###### 1WV - Create Packing Loan

Purpose

In this step, you create a packaging loan by creating an interest rate instrument with product 55A and transaction type 200 according to relevant steps in the Debt and Investment Management (1WV) test script.

|  |
| --- |
| Note Make sure that the Amount is no larger than the amount of the L/C, and the start date of the packing loan is before the shipment date of the received L/C. |

###### Link Reference with LC

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you link the packaging loan and the letter of credit by creating a reference between them.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create Reference (TBR6). | The Create Reference: Initial Screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Reference: Initial Screen, enter the following data, and choose Enter:Reference Category: LOCIn the Object 1 to Be Linked sub-area:Company Code: 3310Transaction: <the transaction number of the IR instrument you created in previous step>In the Object 2 to Be Linked sub-area:Company Code: 3310Transaction: <the transaction number of the Letter of Credit> | The Create Reference: Data screen is displayed. |  |
| 4 | Save Reference | On the Create Reference: Data screen, choose Save. | The Reference number created message is displayed. |  |

###### 1WV- Further processing for Packing Loan

Purpose

After you create a loan, you need to further process the loan in the system.

Procedure

You can refer to the Debt and Investment Management (1WV) test script for how to further processing the packing loan.

#### Rollover Normal Letter of Credit

After the Letter of Credit is issued by the bank, in case the amount or validity term of the Letter of Credit needs to be changed, you can negotiate with the bank to adjust the amount or term of Letter of Credit. Once the bank agrees to do the adjustment, you can roll over the Letter of Credit in the SAP S/4HANA Cloud Public Edition system by changing the Letter of Credit amount or end of term.

##### Rollover Letter of Credit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can roll over a Letter of Credit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company code: 3310Transaction: <transaction number you noted from the previous procedure>Term End:for example, <current date>Accept the default values for other parameters and choose Run. | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Enter Rollover dates | On theTrade Finance: Collective Processing view, select the checkbox before the transaction, and choose Roll Over.On the Roll Over Letter of Credit: Structure view, enter following data, and choose Save:Amount: for example, 2mEnd: for example, <current date + 4 months> | The following message is displayed on Trade Finance: Collective Processing view:Financial transaction saved under number 100000000XXXX |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you roll over a Letter of Credit transaction, you need to settle it before you can proceed with further processes. Normally, you need to settle the transaction once you've received the updated Letter of Credit from the bank.

In this step, you settle the rolled-over Letter of Credit transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data and choose Run:Company Code: for example, 3310Transaction: for example, <the transaction number you noted down in previous step> | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing view, choose the checkbox before the transaction created in previous step, and choose Settle.On the Settle Letter of Credit : Structure view, choose Save.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Letter of Credit transaction is settled. The following message is displayed:Financial transaction saved under number 100000000XXXX.Note If you choose Display on the Trade Finance: Collective Processing view, then the transaction is in the Rollover Settlement status. |  |

#### Presentation

##### Exporter Presentation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you upload L/C relevant documents present to the bank into the system after you ship the goods.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <transaction number you noted from the previous procedure>Term End: <current date >Accept default values for other parameters and choose Run. | The Letter of Credit transaction you created before is displayed. |  |
| 4 | Select the transaction for Presentation | OnTrade Finance: Collective Processing view, select the transaction, and choose Present. | The Change Letter of Credit: Presentation view is displayed. |  |
| 5 | Enter Presentation data | On the Presentation tab of the Change Letter of Credit: Presentation view, choose Insert Row.Enter the following data:Presentation Item: for example, 1Shipment Date: for example, <current date + 10 days>Presentation Date: for example, <current date + 10 days>Payment Date: for example, <current date + 1 month>Presentation Amount: 0.8MDouble click on the presentation itemNote Both presentation date and payment date should be within the LC term and apply to the setting of presentation period/payment period at in the Structure tab. Presentation date should be earlier than payment date and later than shipment date. | The Change Letter of Credit: Presentation Detail view is displayed.Note Multiple presentations are allowed. There would be warning to reminder user if total net presentation amount exceed LC amount (with tolerance) |  |
| 6 | Change the incoming Cash Collateral payment date | In the Documents section of the Change Letter of Credit: Presentation view, select one Doc. Type in the Documents List view, for example, Beneficiary's statement.Double Click on attachment.Note You can enter Discrepancy in the Presentation detail view. If you entered the discrepancy, then Net Presentation Amount = Presentation Amount - Decrease for Discrepancy | The Attachment List view is displayed. |  |
| 7 | Added Attachments for Presentation | Choose New > New Attachment .Upload the attachment, and choose Copy |  |  |
| 8 | Added Attachments for Presentation | Upload other documents by above steps if any, and then choose Save | Msg Financial Transcation saved under number XXXXX is displayed. |  |

##### Send to Bank

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you send the presentation item to Bank.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <transaction number you noted from the previous procedure>Term End:for example, <current date>Accept default values for other parameters and choose Run. | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Send to Bank | On the Trade Finance: Collective Processing view, select the checkbox before the Presentation Item, and choose Send to Bank. | The Change Letter of Credit: Structure view is displayed. |  |
| 5 | Save the change | Choose Save to save the change | The Financial transaction saved under number XXXXXXXXXXXX message is displayed. |  |

##### Accept by Bank and Settle

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you settle the presentation item(s) accepted by the Bank.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <transaction number you noted from the previous procedure>Term End: for example, <current date>Accept default values for other parameters and choose Run. | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Accept the presentation | On the Trade Finance: Collective Processing view, select the checkbox before the Presentation Item, and choose Accept. | The Change Letter of Credit: Presentation view is displayed. |  |
| 5 | Settle the presentation | On the Presentation tab of the Change Letter of Credit: Presentation view, choose SettleNote If there is message about document not accepted, skip it. |  |  |
| 6 | Save the change | Choose Save to save the change. | The Financial transaction saved under number XXXXXXXXXXXX message is displayed. |  |

##### Processing for Export Bill Advance Loan (Optional)

Purpose

In this section, you

There are two ways to create or link a export bill advance loan after the presentation of the Letter of Credit. You can choose one option to create Export Bill Advance Loan:

- Create Export Bill Advance Loan
- Link Export Bill Advance Loan

|  |
| --- |
| Note Please use configuration activity Define Transaction Types - Trade Finance Transactions to maintain the product type 55A and transaction type 200 as the underlying of product type 85A and transaction type 200 before you perform the following steps. |

###### 1WV - Create Export Bill Advance Loan

Purpose

In this step, you create an export bill advance loan by creating an interest rate instrument according to relevant steps in the Debt and Investment Management (1WV) test script.

Procedure

Follow the Create IR Instrument and Set Settlement Status chapters in the Debt and Investment Management (1WV) test script to create and settle transaction with product type 55A and transaction type 200.

|  |
| --- |
| Note Note down the transaction number as loan number to be used in the next step.Make sure that the End date is within presentation period and the Amount is within presentation amount. |

###### Edit Payment Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you change the payment details of the referenced export advance loan, to make sure that payment requests are not generated for outgoing payments.

Procedure

You can also refer the steps in the Debt and Investment Management (1WV) test script to edit payment details.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process MM Transactions - Collective Processing (TM00). | The Money Market: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | Enter the following data:Company Code: for example, 3310Transaction: <Transaction Number for Export Bill Advance Loan>Accept default values for other parameters, and choose Execute. | The transaction is displayed in the next view. |  |
| 4 | Select the Letter of Credit Transaction | On the Money Market: Collective Processing view, select the transaction, and choose Change. | The Change Interest Rate Instrument: view is displayed. |  |
| 5 | Check and Edit Payment Details | On the Payment Details tab, select the row with the - sign and choose Payment Details.:Make the following entries and choose Save:Payment Request: <deselect> |  |  |
| 6 | Save the Change | Save the change. | The Financial transaction saved under number XXXXX is displayed. |  |

###### Link Export Bill Advance Loan

Purpose

In this step, you link the interest rate instrument you created in the previous step as export bill advance loan to the letter of credit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <transaction number you noted from the previous procedure>Term End: for example, <current date>Accept default values for other parameters and choose Run. | The Letter of Credit transcation you created before is displayed. |  |
| 4 | Select and Presentation | On Trade Finance: Collective Processing view,Select the presentation entry which you want to link the import advance loan, and choose Change | The Change Letter of Credit: Presentation view is displayed.Note If you have several presentations for the same letter of credit, there may be multiple presentation entries shown up. Select one you want to apply for the import bill advance loan. |  |
| 5 | Link Export Bill Advance Loan for the Presentation | On the Presentation tab of the Change Letter of Credit: Presentation view, double click on the presentation you accepted and settled before.Scroll down to the bottom, and choose Link Export Bills Negotiation in the Financing section. | The Link Export Bill Advance Loan view is displayed. |  |
| 6 | Enter Data in Export Bill Advance Loan View | On the Link Export Bills Negotiation view, enter the Transaction in Object to Be Linked section or enter the Loan Number you created in the previous step to link it to this presentation.Choose Save | Message Reference created is displayed. |  |
| 7 | Save the Change | Choose Save to save the change. | Message Financial Transcation saved under number XXXXX is displayed. |  |

###### Further Processing for Export Bill Advance Loan

In this step, you further process the export bill advance loan in the system, for example, loan's Interest Payment, loan is Mature, loan's termination. Please refer to the Debt and Investment Management （1WV） test script for how to further process a loan.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two SAP Fiori apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this SAP Fiori app to generate posting for incoming payment and outgoing payment without payment request.
- Process Business Transactions (TPM10): Use this SAP Fiori app to generate postings for outgoing payments that have been processed via app Fix, Pay and Post Flows (TBB1) with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data:Trade Finance: <select>Company code: For example, 3310Transaction: <transaction number with inflow or outflow which was created in previous steps>Up to and Including Due Date: Enter date on which the flow of financial transaction should be posted, for example, <current date + 10 days>Test Run: <select>Post Operational Only: <select>and choose Execute: | The Posting Log: Posted Business Transactions view is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created during a test run.If the system displays the No flows exist for processing notification, no posting is needed for your selection criteria.You can skip the next steps and continue with step 6, using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: <deselect> | The Posting Log: Posted Business Transactions view displays. The accounting document is created for incoming payment in the local GAAP (valuation area AE0). |  |
| 6 | Access another SAP Fiori app | Return to the SAP Fiori launchpad and open Process Business Transactions (TPM10). | The Process Business Transactions view is displayed. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select>Company Code: For example, 3310Valuation Area: For example, AE0Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: <select>Transaction: <transaction number with outflow>Test Run: <select>and choose Execute. | The Test Run: Post/Reverse Business Transactions view is displayed.If the You have not selected any business transactions message is displayed, no postings are needed for your selection criteria. You can skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created during a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions view is displayed. |  |
| 11 | Deselect Test Run | Make the following change:Test Run: <deselect>and choose Execute. | The Update Run: Post/Reverse Business Transactions view is displayed. |  |
| 12 | Production Run | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in the local GAAP (valuation area AE0). |  |

#### Period-end Closing

Purpose

In this section, you make period-end closing in the system, for example, month-end closing.

##### Perform Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you use the valuation function to value the positions of financial instruments based on historical cost or fair value for a given key date, and transfer the results to financial accounting.

Prerequisites

You have imported market data into the system, as described in the [Business Conditions](#unique_6) [page ] 8 chapter.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Execute Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Transaction: <transaction number(s) created in previous steps >Key Date for Valuation: for example, <last date of current month>Note Make sure the Key Date for Valuation is between the Presentation Date and the Payment Date.Valuation Category: for example, Mid-year Valuation with ResetWhen the period end is also the year end, use the Valuation Category Year End Valuation.Test Run: <select> | The Display Positions to be Valued screen is displayed. |  |
| 4 | Execute Valuation for Test Run | Choose Execute Valuation.If a Message dialog box is displayed, choose Continue. | The Valuation Log screen is displayed. If a red traffic light is shown, click on it and check the error message. Solve the issue and perform a test run again until you resolve the error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. There is no posting created because it is a test run.Note Sometimes, there is no simulated posting because your selected transaction may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: <deselect> | The Display Positions to be Valued screen is displayed. |  |
| 6 | Execute Valuation for Production Run | Choose Execute Valuation. | The Valuation Log screen is displayed. Check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. The accounting document is created in the local GAAP (valuation area AE0). |  |

#### Make Collections for Letter of Credit

Purpose

In this step, you make the collection of the payment for the letter of Credit

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two SAP Fiori apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this SAP Fiori app to generate posting for incoming payment and outgoing payment without payment request.
- Process Business Transactions (TPM10): Use this SAP Fiori app to generate postings for outgoing payments that have been processed via app Fix, Pay and Post Flows (TBB1) with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data:Trade Finance: <select>Company code: For example, 3310Transaction: <transaction number with inflow or outflow which was created in previous steps>Up to and Including Due Date: Enter date on which the flow of financial transaction should be posted, for example, <current date + 4 months>Test Run: <select>Post Operational Only: <select>and choose Execute: | The Posting Log: Posted Business Transactions view is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created during a test run.If the system displays the No flows exist for processing notification, no posting is needed for your selection criteria.You can skip the next steps and continue with step 6, using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: <deselect> | The Posting Log: Posted Business Transactions view is displayed. The accounting document is created for incoming payment in the local GAAP (valuation area AE0). |  |
| 6 | Access another SAP Fiori App | Return to the SAP Fiori launchpad and open Process Business Transactions (TPM10). | The Process Business Transactions view is displayed. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions<select>:Company Code: For example, 3310Valuation Area: For example, AE0Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: <select>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select>and choose Execute. | The Test Run: Post/Reverse Business Transactions: view is displayed.If the system displays the You have not selected any business transactions notification, no postings are needed for your selection criteria. You can skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created during a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions view displays. |  |
| 11 | Deselect Test Run | Make the following change:Test Run: Deselectedand choose Execute. | The Update Run: Post/Reverse Business Transactions view is displayed. |  |
| 12 | Production Run | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view is displayed. The accounting document is created for outgoing payment in the local GAAP (valuation area AE0). |  |

### Issue Standby Letter of Credit

A standby letter of credit (SLOC) is a kind of letter of credit that guarantees a bank's commitment of payment to an exporter in the event that the importer, or the bank's client, defaults on the agreement.

In this section, you manage Standby Letter of Credit lifecycle from the importer perspective.

#### Issue Standby Letter of Credit

##### Check Credit Line Limit (Optional)

Purpose

In this step, you check credit line limit of a certain currency.

Procedure

Perform the following step in test script Debt and Investment Management (1WV):

- Check Credit Line Limit (Optional)

##### Create Facility (Optional)

Purpose

In this step, you create the facilities master records as part of the daily business. In this release, you can only create bilateral facilities.

Procedure

Perform the following step in test script Debt and Investment Management (1WV):

- Create Facility (Optional)

|  |
| --- |
| Note Write down the transaction number for later use. |

##### Set Settlement status (Optional)

Purpose

In this step, you settle the facility you created.

Procedure

Perform the following step in test script Debt and Investment Management (1WV):

- Set Settlement Status (Manual)

##### Check Facilities Utilization (Optional)

Purpose

In this step, you check the utilization status of facilities.

Procedure

Perform the following step in test script Debt and Investment Management (1WV):

- Check Facilities Utilization (Optional)

##### Issue Standby Letter of Credit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you request a commercial bank to issue a Standby Letter of Credit for your company, normally the commercial bank will require your company to either provide cash collateral or consume your company's credit line facility in the bank. And the commercial bank will also charge a small percentage of the entire guaranteed amount.

This section describes how to create a transaction for issuing Standby Letter of Credit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Letter of Credit (FTRTLC01). | The Create Letter of Credit: Initial Screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Create Letter of Credit: Initial Screen, enter the following data and choose Enter.Company Code: for example, 3310Product Type: for example, 85BTransaction Type: for example, 100Partner: for example, 33537001 | The data is entered and Create Letter of Credit: Structure screen is displayed. |  |
| 4 | Enter Data on Structure tab | On the Create Letter of Credit: Structure screen, enter the following data, and choose the Collateral tab:Flow Type: 1860Amount: for example, 1MStart: for example, <Current Date>End: for example, <Current Date + 1 year>L/C Number: for example, SLC201909150001, which should be unique in the systemBeneficiary: for example, <search for a supplier with BP role FLVN00>.Advising Bank: 33537001Note If there is no vendor master data with BP role FLVN00, then you can either enter 33537001 or refer to the Create Supplier Master - MDS (BNE) master data script to create a vendor. | The data is entered and Create Standby Letter of Credit : Cash Collateral screen is displayed. |  |
| 5 | Enter Data on Collateral tab | On the Create Standby Letter of Credit: Cash Collateral view, in Facility Assignment group, choose Create. In the Assignment: Facility dialog box, enter the following data and choose Choose:Company code: for example, 3310Transaction: for example, <Facility transaction number you noted down in the previous step>In Cash Collateral group, enter the following data:Line 1:Flow Type: 1991Direction: -Payment Amount: for example,0.2MPayment Date: for example, <Current Date>Line 2:Flow Type: 1991Direction: +Payment Amount: for example,0.2MPayment Date: for example, <Current Date + 1 year>and choose the Other Flows tab. | The data is entered and Create Standby Letter of Credit: Other Flows view is displayed. |  |
| 6 | Enter Data on Other Flow tab | On the Create Standby Letter of Credit : Other Flows view, enter following data, and choose Payment Details tab:Line 1:Flow Type: 1900Direction: -Payment Amount: for example, 350Paym.Crcy: for example, AEDPayment Date: for example, <current Date>Line 2:Flow Type: 1900Direction: -Payment Amount: for example, 250Paym.Crcy: for example, AEDPayment Date: for example, <current Date + 3 months> | The data is entered and Create Standby Letter of Credit : Payment Details view displays. |  |
| 7 | Enter Data on Payment Details tab | On the Create Standby Letter of Credit : Payment Details view, enter the following data:Add a new line:Direction: -Currency: for example, AEDFlow Type: 1991Select the checkbox in front of this new line, and scroll down to the bottom of the screen, choose Payment Details.On the Create Standby Letter of Credit : Payment Details view, enter following data:House Bank: AEBK1Account ID: AEAC1Posting: To G/L AcctsPayment Request: Withoutand choose Free Conditions from the tool bar.After entering Flow type 1991 without Payment request, the payment of Cash Collateral will not use payment request process.You can also skip this step to allow payment request process for Cash Collateral. | The Overview of Conditions view is displayed. |  |
| 8 | Enter Condition Data | On the Overview of Conditions screen, choose Create Fee Cond..In the Overview of Condition dialog box, enter following data and choose Copy: Eff. from: for example, <the current date>On the Condition Details view, enter the following data:On the Amounts tab:Percentage Rate: for example, 0.5On the Dates tab:In the Calculation Date area: input the values, for example, Regular 3 Months1st date: for example, <Current date>Group Due Date:1st date: for example, <Current date - 3 month>Choose Back twice and then choose Save.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | Transaction data is saved. The following message is displayed:Financial transaction saved under number 100000000XXXX.Write down this transaction number. |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you settle the standby letter of credit you created before you can do further processing. Normally this needs to be done once you receive the Standby Letter of Credit from the bank.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data and choose Run.Company Code: for example, 3310Transaction: for example, <Transaction number you noted down in previous step>Note Keep the default values for all the other fields. | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing view, choose the checkbox before the transaction, and select Settle.On the Settle Standby Letter of Credit: Structure view, choose Save.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Standby Letter of Credit transaction is settled. The following message is displayed:Financial transaction saved under number 100000000XXXX. |  |

##### Standby Letter of Credit Fees and Cash Collateral Payment

This section describes payment steps involved in Standby Letter of Credit transactions, including payment of bank fees and cash collateral. If you exclude the collateral from the payment process in the previous step, then only bank fees will be handled.

###### Display Payment Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to display the payments schedule for a Standby Letter of Credit transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules view is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Payment Schedules view, enter the following data, and choose Execute.:OTC Transactions: <select this checkbox>Company Code: for example, 3310End of Term in the Future: <select this checkbox>End of Term in Lapsed: <select this checkbox>Payment Period: for example, <current Date> to <current Date + 12 months>Payment Status: for example, 1Financial Transaction: <transaction number wrote down in previous step>Output Error Log: <select this checkbox> | The payment schedule report is displayed for your review.Note Make a note of the transaction number and payment date is displayed on this view for use in additional procedures, for example, process payment. |  |

###### Corporate Initiated Payment

###### Option 1: Generate and Automatically Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows.

Within these two apps, if you select the ‘Schedule Auto Payment Run’ option, system will automatically process the automatic payment run for payment requests.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number you noted down from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <first payment Date you noted in previous procedure or current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows screen, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number you noted down from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <first payment Date you noted in previous procedure or current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

###### Option 2: Generate and Process Payment Request

###### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request is selected as required (usually only for outgoing payment, in practice). The treasury back office uses the Pay Only functionality in the Post Flows/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows that require payment request,without creating posting in financial accounting.

When payment is initiated by the financial partner, skip this procedure and the [Process Payment Request](#unique_43) [page ] 110 procedure and continue with the [Bank Initiated Payment](#unique_44) [page ] 113 procedure.

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data:Trade Finance: <select this checkbox>Company code: for example, 3310Transaction: <transaction number you noted down from the previous procedure>Up to and Including Due Date: enter date when the flow of financial transaction should be posted, for example, <first payment Date you noted in previous procedure or current date>Test Run: <select this checkbox>Pay Only: <select this indicator>and choose Run.Note The first payment date is normally the same as current date. | The Payment Log - Test Run screen is displayed. Review the payment information on this view.If the No flows exist for processing message is displayed, then there is no payment required for the payment request according to your selection criteria and you can skip to the [Post to General Ledger](#unique_65) [page ] 113 procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect this checkbox> | The payment log is displayed, and a payment request is generated.Note Make a note of the key number displayed on this view to be used in other procedures. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Execute:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure>Up to and Including Due Date: enter date when the flow of financial transaction should be posted, for example, <first payment Date you noted in previous procedure or current date>Test Run: <select>Note The first payment date is normally the same as current date. | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, change the following data and choose Run:Test Run: <deselect> | The payment log is displayed, and a payment request is generated.Note Make a note of the key number displayed on this view to be used in other procedures. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this app to start the Payment Program for Payment Requests. The payment program for payment requests app provides another automatic payment option in the SAP system. Unlike the standard payment program, the payments are based on payment requests, not on open items (vendor/customer items).

Prerequisites

A payment request is generated in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: For example, <current date>Identification: For example,TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | Enter the following data and choose Dynamic selections:Posting Date: For example, <current date>Next payment run on: For example, <current date + 12 months>Company Code: For example, 3310Payment Methods: For example, TF | The Free Selection for payment run dialog box is displayed. |  |
| 5 | Key Number | Enter the following data and choose Save:Key Number: <the key number you noted down in previous step> | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 6 | Additional Log | Choose Additional Log. | The Additional Log dialog box is displayed. |  |
| 7 | Enter Parameters | Make the following entries and choose Continue:Payment method selection in all cases: <select>Line items of the payment documents: <select>Due date check: <select>If the Log created for all accounts message is displayed, choose Continue.Choose Save on the Automatic Payment Transactions: Parameters screen. | The Parameters have been entered message is displayed on the Automatic Payment Transactions for Payment Requests screen. |  |
| 8 | Schedule Proposal | Choose Proposal. | The Schedule Proposal dialog box is displayed. |  |
| 9 | Schedule Job | Select Start Immediat. and choose Schedule Job. | The Proposal is running message is displayed with a yellow traffic light. |  |
| 10 | Update Status | Choose Status until the Payment proposal has been created message is displayed in the status bar with green traffic light. | The payment proposal is generated. |  |
| 11 | Schedule Payment | Choose Pmnt run. | The Schedule Payment dialog box is displayed. |  |
| 12 | Schedule Job | Select Start Immediat., select Create Payment Medium and choose Schedule Job. | The Payment run is running message is displayed in the status bar with a yellow traffic light. |  |
| 13 | Update Status | Choose Status until the Payment run has been carried out message is displayed with a green traffic light. | The Automatic Payment Transactions for Payment Requests screen is displayed.The payment document is created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium is created if it uses PMW format. You can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you see the message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media. A BCM batch is created after the payment run. For more information, see the next test step. |  |
| 14 | Cross-Payment Run Payment Media (Create BCM Batch) | Choose Environment > Payment Medium > Cross-Payment Run Payment Medium > Create Payment Medium . | The Creation of Cross-Payment Run Payment Media screen is displayed. |  |
| 15 | Enter Data | Enter the following data and choose Run:Run Date: For example,Identification: For example, <current date>TRM01R | The Creation of Cross-Payment Run Payment Media dialog box is displayed with the Collector XX/XX/20XX XXXXXX was created or updated message. The BCM batch is created.A batch may need additional approvals before the payment medium is finally created. For more information, see the Advanced Cash Operations (J78) test script. |  |

###### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

##### Bank Initiated Payment

Purpose

When the outgoing payment is initiated by the bank, skip the Generate Payment Request and Process Payment Request procedures because no requests are required.

Procedure

When the bank initiates payment skips to the [Post to General Ledger](#unique_65) [page ] 113 procedure.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two SAP Fiori apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): This SAP Fiori app supports to generate posting for incoming payment and outgoing payment without payment request. You can not use this app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.
- Process Business Transactions (TPM10): You use this SAP Fiori app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.

Prerequisites

Outgoing payments handled using payment request were processed in the previous Generate Payment Request procedure with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data:Trade Finance: <select>Company code: For example, 3310Transaction: <transaction number with inflow or outflow which was created in previous steps>Up to and Including Due Date: Enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: SelectedPost Operational Only: Selectedand choose Execute: | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created during a test run.If the system displays the No flows exist for processing notification, no posting is needed for your selection criteria.You can skip the next steps and continue with step 6, using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: Deselected | The Posting Log: Posted Business Transactions view displays. The accounting document is created for incoming payment in the local GAAP (valuation area AE0). |  |
| 6 | Access another SAP Fiori App | Return to the SAP Fiori launchpad and open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select>Company Code: For example, 3310Valuation Area: For example, AE0Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: SelectedTransaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select>and choose Execute. | The Test Run: Post/Reverse Business Transactions view displays.If the system displays the You have not selected any business transactions notification, no postings are needed for your selection criteria. You can skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view displays. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created during a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions view displays. |  |
| 11 | Deselect Test Run | Make the following change:Test Run: Deselectedand choose Execute. | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 12 | Production Run | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view displays. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in the local GAAP (valuation area AE0). |  |

#### Rollover Standby Letter of Credit

After the Standby Letter of Credit is issued by the bank, in case the amount or validity term of the Standby Letter of Credit needs to be changed, you can negotiate with the bank to adjust the amount or term. Once the bank agrees to do the adjustment, you can roll over the Standby Letter of Credit in the SAP S/4HANA Cloud Public Edition system by changing the Standby Letter of Credit amount or end of term.

##### Roll over Standby Letter of Credit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to roll over a Standby Letter of Credit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <transaction number you noted from the previous procedure>Term End: for example, <current date>Accept default values for other parameters and choose Run. | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Enter Rollover dates | On the Trade Finance: Collective Processing view, select the checkbox before the transaction, and choose Roll Over.On the Roll Over Letter of Credit: Initial Screen view, enter following data, and choose Collateral:Amount: for example, 2MEnd: for example, <current date + 2 years> | The Roll Over Standby Letter of Credit : Cash Collateral is displayed. |  |
| 5 | Change the incoming Cash Collateral payment date | On the Roll Over Standby Letter of Credit: Cash Collateral view, change the payment date of the second line as below, and choose Save:Payment date: <current date + 2 years>Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working dayTerm end changed; consider pymnt date of cash collateral incoming line | The transaction has been rolled over successfully.The following message is displayed on the Trade Finance: Collective Processing view:Financial transaction saved under number 100000000XXXX |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you roll over a Standby Letter of Credit transaction, you need to settle it before you can proceed with further processes. Normally, you need to settle the transaction once you've received the updated Standby Letter of Credit from the bank.

In this step, you set the Settlement status for a rolled-over Standby Letter of Credit transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data and choose Run.Company code: for example, 3310Transaction: for example, <Transaction number wrote down in previous step>Note Keep the default values for all the other fields. | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing view, choose the checkbox before the transaction created in previous step, and choose Settle.On the Settle Standby Letter of Credit: Structure view, choose Save.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Standby Letter of Credit transaction is settled. The following message is displayed:Financial transaction saved under number 100000000XXXX.Note If you choose Display on the Trade Finance: Collective Processing view, you should see the transaction is now in the Rollover Settlement status. |  |

##### Standby Letter of Credit Fees and Cash Collateral Payment

The newly updated Standby Letter of Credit normally comes with the new Bank Fees and Collateral. The process of these payments is the same as the process in the [Issue Standby Letter of Credit](#unique_133) [page ] 98 step of the previous section.

###### Display Payment Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the payment schedule for a Standby Letter of Credit transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules view is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Payment Schedules view, enter the following data:OTC Transactions: <select this checkbox>Company Code: for example, 3310End of Term in the Future: <select this checkbox>End of Term in Lapsed: <select this checkbox>Payment Period: for example, <Current Date> to <Current Date + 2 years>Payment Status: for example, 1Financial Transaction: <transaction number wrote down in previous step>Output Error Log: <select this checkbox>and choose Run. | The payment schedule report appears for your review.Note Make a note of the transaction number and payment date displayed on this view for use in additional procedures, for example, process payment. |  |

###### Corporate Initiated Payment

###### Option 1: Generate and Automatically Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows.

Within these two apps, if you select the ‘Schedule Auto Payment Run’ option, system will automatically process the automatic payment run for payment requests.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number you noted down from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <the second payment date you noted down in previous procedure or current date + 3 months>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows screen, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <the second payment date you noted down in previous procedure or current date + 3 months>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

###### Option 2: Generate and Process Payment Request

###### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request is selected as required (usually only for outgoing payment, in practice). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows that require payment request, it does not create posting in financial accounting,

When payment is initiated by the financial partner, skip this procedure and the Process Payment Request procedure and continue with the Bank Initiated Payment procedure.

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select this checkbox>Company Code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: enter date when the flow of financial transaction should be posted, for example, <the second payment date you noted down in previous procedure or current date + 3 months>Test Run: <select this checkbox>Pay Only: <select this indicator>Note The first payment date is normally the same as current date. | The Payment Log - Test Run screen is displayed. Review the payment information on this view.If the No flows exist for processing message is displayed, then there is no payment required for the payment request according to your selection criteria and you can skip to the [Post to General Ledger](#unique_74) [page ] 129 procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect this checkbox> | The payment log is displayed and a payment request is generated.Note Make a note of the key number displayed on this view as the number is required for other procedures. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure>Up to and Including Due Date: enter date when the flow of financial transaction should be posted, for example, <the second payment date you noted down in previous procedure or current date + 3 months>Test Run: <select>Note The first payment date is normally the same as current date. | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, change the following data and choose Run:Test Run: <deselect> | Payment Log displays, and a payment request is generated.Note Make a note of the key number displayed on this view as the number is required for other procedures. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Use the Automatic Payment Transactions for Payment Requests (F111) app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items) but on payment requests.

Prerequisite

A payment request is generated in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Automatic Payment Transactions for Payment Requests (F111) | The Automatic Payment Transactions for Payment Requests view displays. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests view, enter the following data:Run Date: for example, <current date>Identification: for example, TRM02and choose Maintain payment run parameters. | The Automatic Payment Transactions: Parameters view displays. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters view, enter the following data, and choose Save:Posting Date: for example, <current date>Next payment run on: for example, <current date + 12 months>Company Code: for example 3310Payment Methods: for example, TFChoose Dynamic selections, on the Free Selection for payment run dialog box, enter the following data, and choose Continue:Key Number: <the key numbers you noted from the previous procedure>Choose Additional Log. On the Additional Log dialog box, enter the following data:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>Note If the Log created for all accounts message is displayed, choose Continue.Choose Save on the Automatic Payment Transactions: Parameters view. | Parameters have been entered message displays on Automatic Payment Transactions for Payment Requests view. |  |
| 5 | Schedule Proposal | Choose Schedule proposal..On the Schedule Proposal dialog box, choose Start Immediate and choose Schedule Job to confirm this dialog box.Proposal is runningmessage displays in the status bar with a yellow traffic light status.Choose Update status, until the Payment proposal has been created message appears in the status bar with green traffic light status.NoteIf you choose Edit Proposal, choose Continue on Accounting clerk view, the Edit Payment Proposal: Payments view should display.You should see one line with greenlight on Edit Payment Proposal: Payments view.If there is only one line with redlight or even other error messages display, then the payment proposal is not successful. In this case, you need to check and correct the error so that you can continue to do the next step of this test. | Payment proposal is generated. |  |
| 6 | Schedule Payment | Choose Schedule payment.On the Schedule Payment dialog box, choose Start Immediat. and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Payment run is running message displays in the status bar with yellow traffic light status.Choose Update status, until Payment run has been carried out message appears with green traffic light status. | The payment document is created.If SAP Bank Communication Management is not implemented in your system, the payment medium created uses the PMW format. To review, select the Display payment log.If SAP Bank Communication Management is implemented in your system, in the Display payment log and the Payment run XX/XX/20XX TRM02R is intended for cross-payment run payment media message appears, then a SAP Bank Communication Management batch must be created after the payment run. Proceed to the following step. |  |
| 7 | Cross-Payment Run Payment Media (Create SAP Bank Communication Batch) | The following step only applies if SAP Bank Communication Management is implemented in your system,On the Automatic Payment Transactions for Payment Requests view, choose Environment > Payment medium >Cross-Payment Run Payment Medium> C reate Payment Medium.On the Creation of Cross-Payment Run Payment Media view, enter the following data:Run Date: for example <current date>Identification: for example TRM02Rand choose Run. | The Creation of Cross-Payment Run Payment Media dialog box appears and states that Collector XX/XX/20XX XXXXXX was created or updated confirming the SAP Bank Communication Management batch is created.Note A batch may require additional approvals before payment medium is finally created. For more information, see theBasic Cash Operations (BFB) test script. |  |

###### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

##### Bank Initiated Payment

Purpose

When the outgoing payment is initiated by the bank, skip the [Generate Payment Request](#unique_71) [page ] 123 and [Process Payment Request](#unique_72) [page ] 126 procedures because no requests are required.

Procedure

When the bank initiates payment skip to the [Post to General Ledger](#unique_74) [page ] 129 procedure.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two SAP Fiori apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this SAP Fiori app supports to generate posting for incoming payment and outgoing payment without payment request. You can not use this app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.
- Process Business Transactions (TPM10): You use this SAP Fiori app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request step with the Pay Only option.

Prerequisites

Outgoing payments handled using payment request were processed in the previous Generate Payment Request procedure with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data, and choose Execute:Trade Finance: <select>Company Code: For example, 3310Transaction: <transaction number with inflow or outflow which was created in previous steps>Up to and Including Due Date: Enter date on which the flow of financial transaction should be posted, for example, <current date + 3 months>Test Run: <select>Post Operational Only: <select> | The Posting Log: Posted Business Transactions view is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created during a test run.If the No flows exist for processing message is displayed, no posting is needed for your selection criteria.You can skip the next steps and continue with step 6, using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: | The Posting Log: Posted Business Transactions view is displayed. The accounting document is created for incoming payment in the local GAAP (valuation area <deselect>AE0). |  |
| 6 | Access Another SAP Fiori App | Return to the SAP Fiori launchpad and open Process Business Transactions (TPM10). | The Process Business Transactions view is displayed. |  |
| <7 | Enter Selection Criteria for Test Run | Enter the following data, and choose Execute:OTC Transactions: <select>Company Code: For example, 3310Valuation Area: For example, AE0Limit by Transaction Number: <deselect this checkbox>Limit by Subledger Pos.: <select>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select> | The Test Run: Post/Reverse Business Transactions view is displayed.If the system displays the You have not selected any business transactions notification, no postings are needed for your selection criteria. You can skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created during a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions view is displayed. |  |
| 11 | Deselect Test Run | Make the following change, and choose Execute:Test Run: <deselect> | The Update Run: Post/Reverse Business Transactions view is displayed. |  |
| 12 | Production Run | Choose Select All.Choose Choose Those to Post.Choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view is displayed. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view is displayed. The accounting document is created for outgoing payment in the local GAAP (valuation area AE0). |  |

#### Terminate Standby Letter of Credit

During the validity period of a Standby Letter of Credit, if the Standby Letter of Credit is not needed or the related duties have been performed, then you need to terminate the Standby Letter of Credit.

##### Terminate Standby Letter of Credit and Confirm Cash Collateral

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you terminate a Standby Letter of Credit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <transaction number you noted from the previous procedure>Term End: for example, <current date>Accept default values for other parameters and choose Run. | The transaction is displayed on the Trade Finance: Collective Processing view. |  |
| 4 | Enter the Termination date | On the Trade Finance: Collective Processing view, select the checkbox before the transaction, and choose Terminate.On Terminate Standby Letter of Credit : Structure view, enter following data, and choose Collateral:Terminate: for example, <current date + 1 year and 6 months>Note If the following messages are displayed, choose Continue:No limits were exceededMM/DD/YYYY is not a working day | The Terminate Standby Letter of Credit : Cash Collateral screen is displayed. |  |
| 5 | Change the incoming Cash Collateral payment date | On the Terminate Standby Letter of Credit: Cash Collateral view, change the payment date of the second line as below, and choose Save:Payment date: <current date + 6 months>Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The transaction has been terminated successfully.The following message is displayed on the Trade Finance: Collective Processing view:Financial transaction saved under number 100000000XXXX |  |

##### Automatic Utilize Facility

Purpose

Once the Standby Letter of Credit is in the Termination status, the facility with the same amount of the transaction is utilized automatically.

Procedure

This step doesn't require any operation in system. You can check the facility utilization status in the following step of the Debt and Investment Management (1WV) test script:

- Check Facilities Utilization (Optional)

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a Standby Letter of Credit is terminated, then it needs to be settled before further process.

This section describes how to set the settlement status for a terminated Standby Letter of Credit transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data and choose Run.Company Code: for example, 3310Transaction: for example, <Transaction number you noted down in previous step>Note Keep the default values for all the other fields. |  |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing view, choose the checkbox before the transaction created in previous step, and choose Settle.On the Settle Letter of Credit: Structure view, you can see the status as below:Activity: Termination SettlementChoose Save.Note If the following messages displays, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Letter of Credit transaction is settled. The following message is displayed:Financial transaction saved under number 100000000XXXX.Note If you choose Display on the Trade Finance: Collective Processing view, you can see the transaction is now in the Termination Settlement status. |  |

##### Standby Letter of Credit Fees and Cash Collateral Payment

Once a Standby Letter of Credit is terminated, the Cash Collateral is returned by the bank and the Bank Fees should be calculated and paid to the bank. The process of these payments is the same as the process in the previous section.

###### Display Payment Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the payment schedule for a Standby Letter of Credit transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules view is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Payment Schedules view, enter the following data, and choose Execute:OTC Transactions: <select this checkbox>Company Code: for example, 3310End of Term in the Future: <select this checkbox>End of Term in Lapsed: <select this checkbox>Payment Period: for example, <current date> to <Current Date + 2 years>Payment Status: for example, 1Financial Transaction: <transaction number you noted down in previous step>Output Error Log: <select this checkbox> | The payment schedule report appears for your review.Note Make a note of the transaction number and payment date displayed on this view for use in additional procedures, for example, process payment. |  |

###### Corporate Initiated Payment

###### Option 1: Generate and Automatically Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows.

Within these two apps, if you select the ‘Schedule Auto Payment Run’ option, system will automatically process the automatic payment run for payment requests.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <latest payment Date you noted in previous procedure or current date + 2 years>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows screen, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <latest payment Date you noted in previous procedure or current date + 2 years>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

###### Option 2: Generate and Process Payment Request

###### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Process Payment Request steps send readers to the 'Advanced Cash Operations (J78)' test script for BCM batch approvals in the issue LC and standby LC sections, but to the 'Basic Cash Operations (BFB)' test script in the rollover LC and rollover standby LC sections.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-letter-of-credit-management-49d-ae-sap-s-4hana-cloud-publi-part-02]]
- related-to :: [[05-treasury-and-cash-management/letter-of-credit-management-group-ledger-ifrs-49e-ae-1003]]
- related-to :: [[05-treasury-and-cash-management/letter-of-credit-management-group-ledger-us-gaap-49f-ae-1004]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/49D_S4CLD2608_BPD_EN_AE.docx` — lines 1–2870 of the extracted text · extracted with `mammoth` · 304,091 chars in the whole document
