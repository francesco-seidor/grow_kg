---
id: 05-treasury-and-cash-management/test-script-bank-guarantee-management-2nz-ae-839
title: "Test Script: Bank Guarantee Management (2NZ_AE) (2NZ_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 2NZ (UAE, company code 3310): issuing/receiving bank guarantees, rollover, termination, fees, collateral, reports."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/bank-guarantees]
aliases: [2NZ_S4CLD2608_BPD_EN_AE]
keywords: [Bank Guarantee Management, issue bank guarantee, receive bank guarantee, bank guarantee rollover, bank guarantee termination, cash collateral, payment requests, facility management, treasury posting, limit utilization]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NZ_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-839
topic: 05-treasury-and-cash-management/bank-guarantees
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Bank Guarantee Management (2NZ_AE) (2NZ_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NZ_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Bank Guarantee Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Bank Guarantee Management (2NZ_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232849721)

[2 Prerequisites 5](#_Toc232849722)

[2.1 System Access 5](#_Toc232849723)

[2.2 Roles 5](#_Toc232849724)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232849725)

[2.4 Business Conditions 7](#_Toc232849726)

[2.5 Preliminary Steps 7](#_Toc232849727)

[2.5.1 Create Business partner 7](#_Toc232849728)

[2.5.1.1 Maintain General Data for Business Partner 7](#_Toc232849729)

[2.5.1.2 Maintain Payment Details for Business Partner 9](#_Toc232849730)

[2.5.1.3 Maintain Authorizations for Business Partner 12](#_Toc232849731)

[2.5.1.4 Maintain Reporting Data in Company Code for Business Partner 13](#_Toc232849732)

[2.5.2 Maintain Limit with Limit Type Y01 14](#_Toc232849733)

[2.5.3 Maintain Trader and Trader Authorizations 15](#_Toc232849734)

[3 Overview Table 18](#_Toc232849735)

[4 Test Procedures 22](#_Toc232849736)

[4.1 Issue Bank Guarantee 22](#_Toc232849737)

[4.1.1 Issue Bank Guarantee 22](#_Toc232849738)

[4.1.1.1 Check Credit Line Limit (Optional) 22](#_Toc232849739)

[4.1.1.2 Create and Settle Facility 23](#_Toc232849740)

[4.1.1.3 Check Facilities Utilization (Optional) 26](#_Toc232849741)

[4.1.1.4 Issue Bank Guarantee 27](#_Toc232849742)

[4.1.1.5 Set Settlement Status 30](#_Toc232849743)

[4.1.1.6 Bank Guarantee Fees and Cash Collateral Payment 31](#_Toc232849744)

[4.1.1.6.1 Display Payment Schedule 31](#_Toc232849745)

[4.1.1.6.2 Corporate Initiated Payments 32](#_Toc232849746)

[4.1.1.6.3 Bank Initiated Payment 42](#_Toc232849747)

[4.1.1.6.4 Post to General Ledger 42](#_Toc232849748)

[4.1.2 Roll Over Bank Guarantee 44](#_Toc232849749)

[4.1.2.1 Roll Over Bank Guarantee 44](#_Toc232849750)

[4.1.2.2 Set Settlement Status 46](#_Toc232849751)

[4.1.2.3 Bank Guarantee Fees and Cash Collateral Payment 47](#_Toc232849752)

[4.1.2.3.1 Display Payment Schedule 47](#_Toc232849753)

[4.1.2.3.2 Corporate Initiated Payments 48](#_Toc232849754)

[4.1.2.3.3 Bank Initiated Payment 58](#_Toc232849755)

[4.1.2.3.4 Post to General Ledger 58](#_Toc232849756)

[4.1.3 Terminate Bank Guarantee 61](#_Toc232849757)

[4.1.3.1 Terminate Bank Guarantee and Confirm Cash Collateral 61](#_Toc232849758)

[4.1.3.2 Automatic Release Facility 62](#_Toc232849759)

[4.1.3.3 Set Settlement Status 63](#_Toc232849760)

[4.1.3.4 Bank Guarantee Fees and Cash Collateral Payment 64](#_Toc232849761)

[4.1.3.4.1 Display Payment Schedule 64](#_Toc232849762)

[4.1.3.4.2 Corporate Initiated Payments 65](#_Toc232849763)

[4.1.3.4.3 Bank Initiated Payment 74](#_Toc232849764)

[4.1.3.4.4 Post to General Ledger 75](#_Toc232849765)

[4.2 Receive Bank Guarantee 77](#_Toc232849766)

[4.2.1 Receive Bank Guarantee 77](#_Toc232849767)

[4.2.1.1 Generate Limit Utilizations 77](#_Toc232849768)

[4.2.1.2 Check Limit Utilization Report (Optional) 78](#_Toc232849769)

[4.2.1.3 Receive Bank Guarantee 79](#_Toc232849770)

[4.2.1.4 Set Settlement Status 81](#_Toc232849771)

[4.2.2 Roll Over Bank Guarantee 82](#_Toc232849772)

[4.2.2.1 Rollover Bank Guarantee 82](#_Toc232849773)

[4.2.2.2 Set Settlement Status 84](#_Toc232849774)

[4.2.3 Terminate Bank Guarantee 85](#_Toc232849775)

[4.2.3.1 Terminate Bank Guarantee 85](#_Toc232849776)

[4.2.3.2 Set Settlement Status 86](#_Toc232849777)

[4.3 Reports 88](#_Toc232849778)

[4.3.1 Display Treasury Posting Journal 88](#_Toc232849779)

[4.3.2 Treasury Position Analysis 88](#_Toc232849780)

[4.3.3 Treasury Position History 89](#_Toc232849781)

[4.3.4 Display Treasury Position Values 90](#_Toc232849782)

[4.3.5 Define Financial Positions 91](#_Toc232849783)

[4.3.6 Financial Status (Book Value) 94](#_Toc232849784)

[4.3.7 Financial Status (Nominal Amount) 95](#_Toc232849785)

[4.3.8 Display Treasury Payments 96](#_Toc232849786)

[4.3.9 Display Treasury Position Flows 96](#_Toc232849787)

[4.3.10 Display Treasury Alerts - Posting 97](#_Toc232849788)

[4.3.11 Display Treasury Alerts- Settlement, Release, Payment, Correspondence and Interest Rates 98](#_Toc232849789)

[4.3.12 Display Payment Schedules 99](#_Toc232849790)

[4.3.13 Analyze Net Present Value (NPV) 100](#_Toc232849791)

[4.3.14 Calculate Market Risk Key Figures 101](#_Toc232849792)

[4.3.15 Sensitivity Key Figures 102](#_Toc232849793)

[4.3.16 Review Limit Utilization Report 103](#_Toc232849794)

[5 Appendix 105](#_Toc232849795)

[5.1 Job Scheduling 105](#_Toc232849796)

[5.1.1 Generate Limit Utilizations 105](#_Toc232849797)

[5.1.2 Generate Payment Request 107](#_Toc232849798)

[5.1.3 Post Flows to General Ledger 109](#_Toc232849799)

[5.1.3.1 Template - Fix, Pay and Post Flows 109](#_Toc232849800)

[5.1.3.2 Template - Process Business Transactions 111](#_Toc232849801)

[5.1.4 Post Realized Profit and Loss 113](#_Toc232849802)

[5.1.5 Calculate Market Risk Key Figures 114](#_Toc232849803)

[5.2 Market Risk Analyzer 116](#_Toc232849804)

[5.2.1 Manage Market Data Shift 116](#_Toc232849805)

[5.2.2 Defining Report Layout for Calculate Market Risk Key Figures 117](#_Toc232849806)

[5.2.3 Manage Market Risk Key Figure Sets 120](#_Toc232849807)

[5.2.4 Manage Market Risk Key Figure Sets 123](#_Toc232849808)

[5.3 Credit Risk Analyzer 126](#_Toc232849809)

[5.3.1 Display Limit Overview 126](#_Toc232849810)

## Purpose

Overview

This scope item helps you to better manage your bank guarantee instruments. It supports common functionalities of bank guarantees without integration with sales functionality. Bank guarantee issuing and receiving are covered. In addition to functions for creating and changing bank guarantees, the system also supports functions for rollover, contract settlement, and contract termination. Cash collateral and bank guarantee fees are also covered.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

|  |  |
| --- | --- |
|  | Details |
| SAP S/4HANA system | Accessible via Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

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

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Currency | AED |  |  |
| Foreign Currency 1 | USD |  |  |
| Business Partner | 33537001 |  |  |
| Valuation Area | AE 0 |  |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1XN - Market Rates Management – Manually via Upload | Create necessary market data before you run this scope item. |
| 1WV - Debt and Investment Management | Create Facility. For example, If a Facility needs to be assigned to Bank Guarantee and the Facilities Utilization needs to be checked for Bank Guarantee. |
| J60 - Accounts Payable | In the script, execute the Prerequisites > Preliminary Steps > Define Payment Medium Format Variants step to define the Payment Medium Format (PMF) variants. |

### Preliminary Steps

#### Create Business partner

##### Maintain General Data for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the general data for Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: view displays. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner view, choose Organization. | The Create Organization view displays. |  |
| 4 | Enter address data | On the Create Organization view, enter the following data, and choose Save:Business Partner: for example, 33537001Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Bank 1 - SAMPLE BANKSalutation: for example, Bank 1Search Term 1/2: for example, Bank 1Street/House Number: <street/house number of the business partner>Postal Code/City: <postal code/city of the business partner>Country/Reg.: AELanguage: EnglishE-Mail: <E-mail>Address Valid From: for example, <the current date in the previous year>Address Valid To: for example, <Dec 31 of the year 9999>Note Remain on this view for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to change mode | On the Display Organization33537001 details view, choose Switch Between Display and Change, and enter following data:Change in BP role: select TR0151 Counterparty | More counterparty related tabs, for example Legal Data, Rating display. |  |
| 6 | Enter Legal data | On the Change Organization: 33537001 view, choose Legal Data from the dropdown menu and enter the following data:Country/Region: AEand choose Save.Note The navigation menu is on the right side of the view. It displays as … , and is next to the >),Note Remain in this view for subsequent steps. | The legal data is entered and saved.Change Organization: 33537001 , new role Counterparty view displays. |  |
| 7 | Enter Payment Transaction data | On Change Organization:33537001, new role Counterparty view, select Payment Transactions from the dropdown menu and enter following two rows of data:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, 18121976Bank acct: <bank account>IBAN: choose the IBAN button and choose <Bank account>Continue in the IBAN dialog box.Row 2:ID: for example, USD1C/R: for example, AEBank Key: for example,Bank acct: for example, <bank account>IBAN: choose the IBAN button and then choose Continue on the IBAN dialog box.Now choose Save.Note If a dialog window of Information appears when you choose IBAN, choose Continue. | The Payment transaction data is entered and the Business Partner is saved. |  |

##### Maintain Payment Details for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the detailed steps on how to maintain payment details data for Business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: view displays. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: view, choose Open BP, in the Open business partner dialog box, enter the following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: select TR0151 Counterparty (defined)and choose Enter. | Change Organization: 33537001 , new role Counterparty view displays. |  |
| 4 | Enter SI: Payment Details data | On Change Organization:33537001, new role Counterparty screen, choose Company code, and enter the following data:Company code: for example, 3310Choose ENTER and choose SI: Payment Details and enter the following four rows of data:Row 1:Currency: for example, AEDPay.Det.ID: for example, AEDIHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, BlankPartner Bank: for example, BlankPayment Request: for example, DeselectPayment methods: for example, BlankRow 2:Currency: for example, AEDPay.Det.ID: for example, AEDOHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, 33537001Partner Bank: for example, AED1Payment Request: for example, selectPayment methods: for example, TRow 3:Currency: for example, USDPay.Det.ID: for example, USDIHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/ee: for example, BlankPayment Request: for example, DeselectPayment methods: for example, BlankRow 4:Currency: for example, USDPay.Det.ID: for example, USDOHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/Payee: for example, 33537001Partner Bank: for example, USD1Payment request: for example, <select>Payment methods: for example, FNote Remain in the view for subsequent steps.Note If a warning notification displays the following message:Business partner proposed as payer/payee (see long text). Display this message for this business partner again? choose No. | The SI: Payment Details data is entered. |  |
| 5 | Assign Payment details | From the last view of the previous step,For AED, select the Checkbox for AEDAEDI. Choose Assign. In the Counterparty Change: Payment Details Assignment dialog box, choose Select All Incoming.Now AEDI displays under PmntID-Inc. .Choose Continue to close the dialog box.Select the Checkbox for AEDAEDO.Choose Assign. In the Counterparty Change: Payment Details Assignment dialog box, choose Select All Outgoing.Now AEDO displays under P-ID Outg.Choose Continue to close the dialog box.Repeat for USD:USD I: PmntID-IncUSD O: P-ID Outg.On Change Organization:33537001, role Counterparty view, choose Save. | Payment details and the assignments are saved. |  |

##### Maintain Authorizations for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the detailed steps on how to maintain the authorization data for Business Partner for SAP TRM.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen displays. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP, in the Open business partner dialog box, enter following data:Business Partner: 33537001Choose Enter and choose Switch Between Display and Change, and enter the following data:Change in BP Role: select TR0151 Counterparty (defined) | Change Organization: 33537001 , role Counterparty screen displays. |  |
| 4 | Enter SI: Authorizations data | On the Change Organization: 33537001, role Counterparty screen, choose Company Code, choose SI: Authorizations, enter the following data and choose Save.In the Trans. Hierarchy column, find Trade Finance, then in the Auth. column, select the checkbox representing Trade Finance.Note You can also give authorization to a specific product type and transaction type by expending the folders. For testing purpose, we give all authorizations to all kinds of product types and transaction types. | The Authorizations data is saved. |  |

##### Maintain Reporting Data in Company Code for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the detailed steps on how to maintain company relationship for Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen displays. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP, in the Open business partner popup dialog box, enter following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: choose TR0151 Counterparty (defined) | Change Organization: 33537001 , role Counterparty screen displays. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization: 33537001, role Counterparty screen, choose Company Code, choose the Reporting Data in Company Code subtab, and enter the following data and choose save.Comp. Rel.: for example, 3 OtherNote If you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown Menu.Note Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itThey are used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

#### Maintain Limit with Limit Type Y01

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can maintain the limit for limit type Y01.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Limits (TBL1). | The Limits: Choose Limit Types screen is displayed. |  |
| 3 | Choose Limit Type | Select the Limit Type Y01 row and choose Create Limits. | The Create Limits: Define Characteristics dialog box appears. |  |
| 4 | Company Code | Enter the following entry and choose Continue:Company Code: for example, 3310 | The Edit Limits for Limit Type Y01: Create New Limit screen is displayed. |  |
| 5 | Create Internal Limit Amount and External Limit Amount | Enter the following data and choose Save:Valid From Date: for example, <the current date>Valid To (Internal): for example, 12/31/9999Valid To (External): for example, <the current date + 1 year>Limit Currency: for example, AEDInternal Limit Amnt: for example, 250,000,000External Limit Amnt: for example, 200,000,000Critical Limit Utilizat.: for example, 90%Max. Risk Commit Per. Mth: for example, 999Note The maximum period is set on monthly basis. A warning message is displayed if the period is exceeded.Limit: for example, Check |  |  |

#### Maintain Trader and Trader Authorizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create traders and maintain authorizations for the traders in the system.

Procedure

1. Define Traders

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Traders (S_ALR_87009302). | The Determine Work Area: Entry dialog displays |  |
| 3 | Enter Work Area | Enter data and select Apply (Enter).Company Code: for example: 3310 | The Define Traders: Change screen displays. |  |
| 4 | Create a New Record | Select New Entries, enter data and select Save:Trader: for example: TRADER02 | The data is saved. |  |

2. Define User Data

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define User Data (S_ALR_87007933). | The Define User Data: Change screen is displayed. |  |
| 3 | Create a New Record | Select New Entries, enter the following data and push enter then choose Save:User ID: for example: <Your user name>Trader: for example, TRADER02 | The data is saved. |  |

3. Maintain Authorizations for Trader

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Trader Authorizations (TBT1). | The Create/Change Trans. Authorization for Trader: Init. Screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Enter:Trader: for example, TRADER02Company Code: for example, 3310 | The Create/Change Transaction Authorization for Traders screen is displayed. |  |
| 4 | Enter Authorization and Save | Select or deselect the entries on the Auth. column and choose Save.Note Make sure to authorize TRADER02 for the Trade Finance transactions. | The data is saved as indicated by a message. For example: Transaction authorizations for trader TRADER02 are being saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Issue Bank Guarantee

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Check Credit Line Limit (Optional)](#unique_14) [page ] 22 | Treasury Specialist - Front Office | Credit Line Analysis (FTR_CREDIT_LINE_ANALYSIS (FTR_CREDIT_LINE_ANALYSIS)) | Credit line limits displays. |
| [Create and Settle Facility](#unique_15) [page ] 23 | Treasury Specialist - Front Office | Create Facility (TM_61) | A facilities master record is created. |
| [Check Facilities Utilization (Optional)](#unique_16) [page ] 26 | Treasury Specialist - Front Office | Credit Line Analysis (FTR_CREDIT_LINE_ANALYSIS (FTR_CREDIT_LINE_ANALYSIS)) | The utilization of facility displays. |
| [Issue Bank Guarantee](#unique_17) [page ] 27 | Treasury Specialist - Front Office | Create Bank Guarantee (FTRTBG01) | Bank Guarantee Transaction data is saved. |
| [Set Settlement Status](#unique_18) [page ] 30 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The Bank Guarantee transaction is settled. |
| [Display Payment Schedule](#unique_19) [page ] 31 | Treasury Accountant | Display Payment Schedules (TJ04) | The payment schedule report appears. |
| [Process the Payment with the ‘Auto. Payment Run’ Function](#unique_20) [page ] 33 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment requests keys are generated and automatic payment run is completed. |
| [Generate Payment Request](#unique_21) [page ] 36 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_22) [page ] 39 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_23) [page ] 42 |  |  |  |
| [Post to General Ledger](#unique_24) [page ] 42 | Treasury Accountant | Fix, Pay and Post Flows (TBB1)/ Process Business Transactions (TPM10) | FI document is posted. |
| [Roll Over Bank Guarantee](#unique_25) [page ] 44 | Treasury Specialist - Front Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The transaction has been rolled over successfully. |
| [Set Settlement Status](#unique_26) [page ] 46 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The Bank Guarantee transaction is settled. |
| [Display Payment Schedule](#unique_27) [page ] 47 | Treasury Accountant | Display Payment Schedules (TJ04) | The payment schedule report appears. |
| [Process the Payment with the ‘Auto. Payment Run’ Function](#unique_28) [page ] 49 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment requests keys are generated and automatic payment run is completed. |
| [Generate Payment Request](#unique_29) [page ] 52 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_30) [page ] 55 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Post to General Ledger](#unique_31) [page ] 58 | Treasury Accountant | Fix, Pay and Post Flows (TBB1) Process Business Transactions (TPM10) | FI document is posted. |
| [Terminate Bank Guarantee and Confirm Cash Collateral](#unique_32) [page ] 61 | Treasury Specialist - Front Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The transaction has been terminated successfully. |
| [Automatic Release Facility](#unique_33) [page ] 62 | Treasury Specialist - Front Office | Credit Line Analysis | The utilization of facility displays. |
| [Set Settlement Status](#unique_34) [page ] 63 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The Bank Guarantee transaction is settled. |
| [Display Payment Schedule](#unique_35) [page ] 64 | Treasury Accountant | Display Payment Schedules (TJ04) | The payment schedule report appears. |
| [Process the Payment with the ‘Auto. Payment Run’ Function](#unique_36) [page ] 66 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment requests keys are generated and automatic payment run is completed. |
| [Bank Initiated Payment](#unique_37) [page ] 74 |  |  |  |
| [Generate Payment Request](#unique_21) [page ] 36 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_22) [page ] 39 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Post to General Ledger](#unique_38) [page ] 75 | Treasury Accountant | Fix, Pay and Post Flows (TBB1) Process Business Transactions | FI document is posted. |

Receive Bank Guarantee

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Generate Limit Utilizations](#unique_39) [page ] 77 | Treasury Specialist - Middle Office | End-of-Day Processing (KLNACHT) | Limit utilizations was determinate and updated. |
| [Check Limit Utilization Report (Optional)](#unique_40) [page ] 78 | Treasury Specialist - Middle Office | Review Limit Utilizations (TBLB) | Limit utilization report displays. |
| [Receive Bank Guarantee](#unique_41) [page ] 79 | Treasury Specialist - Front Office | Create Bank Guarantee (FTRTBG01) | Bank Guarantee Transaction data is saved. |
| [Set Settlement Status](#unique_42) [page ] 81 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The Bank Guarantee transaction is settled. |
| [Rollover Bank Guarantee](#unique_43) [page ] 82 | Treasury Specialist - Front Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The transaction has been rolled over successfully. |
| [Set Settlement Status](#unique_44) [page ] 84 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The Bank Guarantee transaction is settled. |
| [Terminate Bank Guarantee](#unique_45) [page ] 85 | Treasury Specialist - Front Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The transaction has been terminated successfully. |
| [Set Settlement Status](#unique_46) [page ] 86 | Treasury Specialist - Back Office | Process Trade Finance Transactions - Collective Processing (FTRTLC00) | The Bank Guarantee transaction is settled. |

Reports

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Display Treasury Posting Journal](#unique_47) [page ] 88 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Treasury posting journal displays. |
| [Treasury Position Analysis](#unique_48) [page ] 88 | Treasury Accountant | Treasury Position Analysis | Treasury position analysis displays. |
| [Display Treasury Position Values](#unique_49) [page ] 90 | Treasury Accountant | Display Treasury Position Values (F1867) | Treasury position values display. |
| [Define Financial Positions](#unique_50) [page ] 91 | Treasury Accountant | Define Financial Positions (FTR_FP_DEF) | Financial Positions are defined. |
| [Financial Status (Book Value)](#unique_51) [page ] 94 | Treasury Accountant | Financial Status (F2136) | The financial status on book values displays. |
| [Financial Status (Nominal Amount)](#unique_52) [page ] 95 | Treasury Accountant | Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)) | The financial status on nominal amount displays. |
| [Display Treasury Payments](#unique_53) [page ] 96 | Treasury Accountant | Display Treasury Payments (TPM20A) | Treasury Payment displays. |
| [Display Treasury Position Flows](#unique_54) [page ] 96 | Treasury Accountant | Display Treasury Position Flows (F1754) | Treasury posting flows display. |
| [Display Treasury Alerts - Posting](#unique_55) [page ] 97 | Treasury Accountant | Display Treasury Alerts (F4984) | Treasury Alerts-Posting display. |
| [Display Treasury Alerts- Settlement, Release, Payment, Correspondence and Interest Rates](#unique_56) [page ] 98 | Treasury Specialist - Back Office | Display Treasury Alerts - Settlement (F4979) | Treasury Alerts display. |
| [Display Payment Schedules](#unique_57) [page ] 99 | Treasury Accountant | Display Payment Schedules (TJ04) | Payment schedules displays. |
| [Analyze Net Present Value (NPV)](#unique_58) [page ] 100 | Treasury Specialist - Middle Office | Analyze NPV (JBRX) | The NPV Result displays. |
| [Calculate Market Risk Key Figures](#unique_59) [page ] 101 | Treasury Specialist - Middle Office | Calculate Market Risk Key Figures (AISGENKF) | The single value analysis of assigned report layout displays. |
| [Sensitivity Key Figures](#unique_60) [page ] 102 | Treasury Specialist - Middle Office | Sensitivity Key Figures - Single Analysis (AISS) | The sensitivity key figures display. |
| [Review Limit Utilization Report](#unique_61) [page ] 103 | Treasury Specialist - Middle Office | Review Limit Utilizations (TBLB) | Limit utilizations display. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Issue Bank Guarantee

A bank guarantee is a written promise from a bank or financial institution to take responsibility for the applicant's financial obligation if that applicant cannot meet its obligation.

To issue a Bank Guarantee, you need to contact a bank or financial institution to start the application process.

#### Issue Bank Guarantee

##### Check Credit Line Limit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check credit line limit.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Credit Line Analysis (FTR_CREDIT_LINE_ANALYSIS (FTR_CREDIT_LINE_ANALYSIS)). | The Credit Line Analysis screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Credit Line Analysis screen, enter the following data,and choose Go:Start Date: for example, <Current Date>End Date: for example, <Current Date>Reporting Frequency: for example, DDisplay Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The Credit limit screen is displayed.Note If the following error message is displayed, it means no credit line available yet. You may ignore this error message and continue with the following step.Result set for query XXXXXXXXXXXXXXXXX is empty |  |

##### Create and Settle Facility

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and settle the facilities. In this release, you can only create bilateral facilities.

Procedure

1. Create Facility

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Facility (TM_61). | The Create Facility: Initial Screen view displays. |  |
| 3 | Create A New Facility | On the Create Facility: Initial Screen view, enter the following data, and choose Enter:Company Code: for example, 3310Product Type: 56ATransaction Type: for example, 200Partner: for example, 33537001 | The Create Facility: Structure view appears. |  |
| 4 | Maintain Structure of New Facility | On the Create Facility: Structure screen, enter the following data:Start of Term: for example, <the current date>End of Term: for example, <the current date + 3 years>Inclusive: for example, Start Included |  |  |
| 5 | Maintain Conditions | Choose Conditions, then choose Create Fee Condition from the dropdown list.In the Possible condition types (1) dialog box, choose 1240 Facility fee: Not Utilized and choose OK.In the Overview of Conditions dialog box, enter the following data and choose Copy:Eff. From: for example, <the current date> | The Overview of Conditions view is displayed. |  |
| 5 | Maintain Conditions | On the Amounts tab, enter the following data:Int. Calc. Type: for example, <select a proper interest calculation type>Int.Calc.Method: for example, <select a proper interest calculation method>Percentage Rate: for example, 3 | The Condition Details view is displayed. |  |
| 5 | Maintain Conditions | On the Dates tab, enter the following data, and choose back twice:1st date: for example, <the current date + 3 years> | The condition type 1240 is created.The Create Facility: Structure view is displayed. |  |
| 6 | Maintain Profiles of New Facility | On the Profiles tab, in the Credit Line area, choose Create, enter the following data, and choose Copy entries:Credit Line Amount: for example, 20MValid Frm: for example, <the current date> |  |  |
| 7 | Maintain Administration of New Facility | On the Administr. tab, enter the following data, and choose Save:Gen. Valn Class: for example, Short term debt (current liability): Nominal/Facilities | Facility created successfully. Make a note of the facility number for following procedures. |  |

2. Settle the Facility

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process MM Transactions - Collective Processing (TM00). | The Money Market: Collective Processing screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Money Market: Collective Processing screen, enter the following data and choose Run:Company Code: for example, 3310Transaction: for example, <the facility number you noted down in the previous step>Note Keep the default values for all the other fields. | The transaction is displayed on Trade Finance: Collective Processing screen. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing screen, choose the checkbox before the transaction created, and choose Settle.On the Settle Interest Rate Instrument: Structure view, choose Save.Note If the following messages displays, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Bank Guarantee transaction is settled. The following message is displayed:Financial transaction saved under number 100000000XXXX. |  |

##### Check Facilities Utilization (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the facility utilization.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Credit Line Analysis (FTR_CREDIT_LINE_ANALYSIS (FTR_CREDIT_LINE_ANALYSIS)). | The Prompts dialog box is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Go:Company Code: for example, 3310Transaction Number: <facility transaction number which was created in the previous steps, or leave blank for all facilities transactions>Start Date: for example, <Current Date>End Date: for example, <Current Date>Reporting Frequency: for example, DDisplay Currency: for example, AEDExchange Rate Type: for example, M | The Credit Line Analysis screen is displayed. |  |
| 4 | Displays by Transaction Number | On the Dimensions panel, choose the Transaction Number dimension and drag it to the Columns or the Rows panel to display the results by Transaction Number.Note The utilization of facility is displayed in the Utilized Amt in DC field. | The facilities by transaction number are displayed. |  |

##### Issue Bank Guarantee

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you request a commercial bank to issue a Bank Guarantee for your company, normally the commercial bank will require your company to either provide cash collateral or consume your company's credit line facility in the bank. And the commercial bank will also charge a small percentage of the entire guaranteed amount.

In this step, create a transaction for issued Bank Guarantee.

Prerequisite

You have run Generate Limit Utilizations of Debt and Investment Management(1WV).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Create Bank Guarantee (FTRTBG01). | The Create Bank Guarantee: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | Enter the following data, and choose Enter:Company Code: for example, 3310Product Type: for example, 86ATransaction Type: for example, 100Partner: for example, 33537001. | The data is entered and Create Bank Guarantee: Structure view displays. |  |
| 4 | Enter Data on Structure tab | On the Create Bank Guarantee: Structure screen, enter the following data:Flow Type: 1860Amount: for example, 1mStart: for example, <Current Date>End: for example, <Current Date + 1 year>BankGuarantee No.: for example, 201710BG001BankGuarantee Ty.:: for example, PAYM Payment GuaranteeBeneficiary: for example, search for a vendor with BP role FLVN00 or FLVN01.Note If there is no vendor master data with the FLVN00 or FLVN01 BP role, you can refer to following master data script to create a vendor:Create Supplier Master - MDS (BNE)You may also manually enter the Beneficiary data: Manual Input Beneficiary: Select this checkbox and more fields show up on the screen.Company Name: for example, <your vendor's name>Company Name Ext:for example, <your vendor's name>Contact Person: for example, <enter your vendor's sales person's name>Company Address: for example, <your vendor's address>Company Addr Ext: for example, <your vendor's address>Note You can create your own Bank Guarantee Types via configuration step Define Bank Guarantee Types.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | The data is entered and Create Bank Guarantee: Cash Collateral view displays. |  |
| 5 | Enter Data on Collateral tab | Choose the Collateral tab. On the Create Bank Guarantee: Cash Collateral screen, in Facility Assignment group, Choose Create. In the Assignment: Facility dialog box, enter the following data and choose Choose:Company Code: for example, 3310Transaction: for example, Facility transaction number you noted down in previous stepIn the Cash Collateral area, enter the following data:Flow Type: 1991Direction: -Payment Amount: for example,0.2mPayment Date: for example, <Current Date>At the bottom of the area, choose Generate Incoming Collateral button, to automatically generate the incoming collateral. | The data is entered and Create Bank Guarantee: Other Flows view displays. |  |
| 6 | Enter Data on Other Flow tab | Choose Other Flows. On the Create Bank Guarantee: Other Flows screen, enter following data:Line 1:Flow Type: 1900Direction: -Payment Amount: for example,350Paym.Crcy: for example, AEDPayment Date: for example, <Current Date>Line 2:Flow Type: 1900Direction: -Payment Amount: for example,250Paym.Crcy: for example, AEDPayment Date: for example, <current Date + 3 months> | The data is entered and Create Bank Guarantee: Payment Details view displays. |  |
| 7 | Enter Data on Payment Details tab | Choose Payment Details tab. On the Create Bank Guarantee: Payment Details view, enter the following data:Add a new line:Direction: OutflowCurrency: for example, AEDFlow Type: 1991House Bank: AEBK1Account ID: AEAC1Payment Request: <Select Without>NoteAfter entering Flow type 1991 without Payment request, the payment of Cash Collateral will not use payment request process.You can also skip this step to allow payment request process for Cash Collateral. | Overview of Conditions view displays. |  |
| 8 | Enter Condition data | Choose Fee Conditions in the tool bar.On the Overview of Conditions screen, choose Create Fee Cond..In the Overview of Condition dialog box, enter following data and choose Copy: Eff. from: for example, <the current date>On the Condition Details view, enter the following data:On the Amounts tab:Percentage Rate: for example, 0.5On the Dates tab:In the Calculation Date area: input the values, for example, Regular 3 Months1st date: for example, <Current date>Group Due Date:1st date: for example, <Current date - 3 month>Choose Back twice and then choose Save.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | Transaction data is saved. The following message displays:Financial transaction saved under number 100000000XXXX.Write down this transaction number. |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a Bank Guarantee transaction is recorded and saved, it needs to be settled before further processing. Normally this needs to be done once you receive the Bank Guarantee from the bank. This section describes how to set the settlement status for a Bank Guarantee transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing view displays. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data and choose Run.Company Code: for example, 3310Transaction: for example, Transaction number wrote down in previous stepNoteKeep the default values for all the other fields. | The transaction is displayed on Trade Finance: Collective Processing view. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing view, choose the checkbox before the transaction created, and select Settle.On the Settle Bank Guarantee: Structure view, choose Save.Note If the following messages displays, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Bank Guarantee transaction is settled. The following message displays:Financial transaction saved under number 100000000XXXX. |  |

##### Bank Guarantee Fees and Cash Collateral Payment

In this section, you pay for the Bank Guarantee transaction, for example, the bank fee and cash collateral.

###### Display Payment Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the payments schedule for a Bank Guarantee transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Payment Schedules screen, enter the following data, and choose Run:OTC Transactions: <select this checkbox>Company Code: for example, 3310End of Term in the Future: <select this checkbox>End of Term in Lapsed: <select this checkbox>Payment Period: for example, <current date to current date + 1 yearPayment Status: for example, 1Financial Transaction: <transaction number you noted down in the previous step>Output Error Log: <select this checkbox> | The payment schedule report is displayed for your review.Note Make a note of the transaction number and payment date displayed on this view for use in additional procedures, for example, process payment. |  |

###### Corporate Initiated Payments

Purpose

This section describes how to handle the corporate initiated outgoing payments via payment requests.

There are two options to process the outgoing payments:

1. Process the payment with the ‘Auto. Payment Run’ function.
2. Process the payment without the ‘Auto. Payment Run’ function.

If the payment is initiated by the bank without using payment request, skip the current step, and continue with the step [Post to General Ledger](#unique_24) [page ] 42.

Prerequisites

You have settled the contract in the previous step.

###### Option 1: Generate and Automatically Process Payment Request

###### Process the Payment with the ‘Auto. Payment Run’ Function

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.If scope item (3NA) Treasury Workstation Payment Integration is activated and the certain communication arrangement with communication scenario - Finance - Treasury Payment Request Integration (SAP_COM_0442) is also activated in your system, the Payment Control area will not appear in the selection screen. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
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

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment requests for outflows, which does not create posting in financial accounting.

If payment is initiated by the financial partner, skip this procedure and the [Process Payment Request](#unique_22) [page ] 39 procedure and continue with the [Bank Initiated Payment](#unique_23) [page ] 42 procedure.

|  |
| --- |
| Note To schedule a background job for this step, see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted in the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <first payment Date you noted in the previous procedure or current date>Test Run: <select>Pay Only: <select this indicator>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Payment Log - Test Run displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | The Information Overview dialog is displayed with following 2 lines:Payment LogMessages |  |
| 5 | Get Payment Request Key | On the Information Overview screen, double click on Payment Log to check the payment log. | On the Payment Log screen, the key numbers of the payment request are displayed.Note Write down the key numbers of the payment requests to be processed in the next step. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down in the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <first payment date you noted down in the previous procedure or current date>Test Run: <select> | You may choose Payment Log to review the payment information on view Payment Log - Test Run.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, enter the following data, and choose Run:Test Run: <deselect> | The Information Overview dialog is displayed with following 2 lines:Payment LogMessages |  |
| 5 | Get Payment Request Key | On the Information Overview screen, double click on Payment Log to check the payment log. | On the Payment Log screen, the key numbers of the payment request are displayed.Note Write down the key numbers of the payment requests to be processed in the next step. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the app Automatic Payment Transactions for Payment Requests (F111) to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items) but on payment requests.

Prerequisite

Payment request has been generated in previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests screen, enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters screen, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 12 months>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free selection for payment run, enter the following data and choose Save:Key number: <the key numbers you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>Note If Log created for all accounts displays, choose Continue.Choose Save on screen Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 5 | Schedule Proposal | Choose Schedule proposal.On the dialog box Schedule Proposal, choose Start Immediat and choose Schedule Job to confirm this dialog box.The Proposal is running message is displayed in the status bar with a yellow traffic light.Choose Update Status, until message Payment proposal has been created appears in the status bar with green traffic light.NoteIf you choose Edit Proposal, choose Continue on Accounting clerk view, the Edit Payment Proposal: Payments view should display.You should see one line with greenlight on Edit Payment Proposal: Payments view.If there is only one line with redlight or even other error messages display, then the payment proposal is not successful. In this case, you need to check and correct the error so that you can continue to do the next step of this test. | Payment proposal is generated. |  |
| 6 | Schedule Payment | Choose Schedule payment.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create SAP Bank Communication Batch) | The following step only applies if SAP Bank Communication Management is implemented in your system.On the Automatic Payment Transactions for Payment Requests screen, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium.On the Creation of Cross-Payment Run Payment Media screen, enter the following data and choose Run:Run Date: for example, <current date>Identification: for example, TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations (J78). |  |

###### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

###### Bank Initiated Payment

Purpose

When the outgoing payment is initiated by the bank, skip the Generate Payment Request and Process Payment Request procedures because no requests are required.

Procedure

When the bank initiates payment skip to the Post to General Ledger procedure.

###### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post related cash flows to the FI interface that generates the relevant postings in financial accounting. There are two apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this app to generate the posting for incoming or outgoing payment that you haven't processed in the previous Generate Payment Request procedure with the Pay Only option.
- Process Business Transactions (TPM10): Use this app to generate the posting for outgoing payment that you have processed in previous Generate Payment Request procedure with the Pay Only option.

|  |
| --- |
| Note You can schedule a background job for this procedure by referring to the corresponding step in the Appendix. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows screen, enter the following data, and choose Execute:Trade Finance: <select this checkbox>Company Code: for example 3310Transaction: <transaction number with inflow or outflow you created in the previous steps>Up to and Including Due Date: enter the date on which the flow of financial transaction should be posted, for example, <the current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | Posting Log: Posted Business Transactions view is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run.If No flows exist for processing message is displayed, then there is no posting required for your selection criteria. Skip the Production Run step and continue the test step using the Process Business Transactions app. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows screen, change the following data, and choose Execute:Test Run: <deselect this checkbox> | The Posting Log: Posted Business Transactions view displays. Accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access Another SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen displays. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data, and choose Execute:OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions view displays.Note If message You have not selected any business transactions displays, that means there is no posting are needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the Test Run: Post/Reverse Business Transactions screen, choose Select All and choose Choose Those to Post, and then choose Save.The Test Run: Display Posted/Reversed Business Transactions screen is displayed, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this screen.Note There is no posting created since this is a test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 9 | Production Run | On Update Run: Post/Reverse Business Transactions screen, choose Select All and choose Choose Those to Post, and then choose Save.The Update Run: Display Posted/Reversed Business Transactions screen is displayed. Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Roll Over Bank Guarantee

In this section, you roll over the bank guarantee. You may need to adjust some of the transaction conditions after negotiating with the bank, for example, the amount or the validity term of the bank guarantee.

##### Roll Over Bank Guarantee

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you roll over a Bank Guarantee.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing screen, enter the following data:Company Code: for example, 3310Transaction: for example, <transaction number you noted down from the previous procedure>Term End: for example, <the current date>Accept default values for the other parameters and choose Run. | The transaction is displayed on the Trade Finance: Collective Processing screen. |  |
| 4 | Enter Rollover dates | On Trade Finance: Collective Processing screen, select the checkbox before the transaction, and choose Roll Over.On the Roll Over Bank Guarantee: Structure screen enter following data, and choose Collateral:Amount: for example, 2MRollover: for example, <the current date + 1 year>End: for example, <the current date + 2 years> | The Roll Over Bank Guarantee: Cash Collateral screen is displayed. |  |
| 5 | Change the incoming Cash Collateral payment date | On the Roll Over Bank Guarantee: Cash Collateral screen, change the payment date of the second line as below:Payment Date: <current date + 2 years>Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The cash collateral payment date is changed. |  |
| 5 | Change the Fee Conditions | Choose Fee Conditions in the tool bar. Double click on the second row of fee condition which is newly created.On the Amounts tab:Percentage Rate: for example, 0.5On the Dates tab:In the Calculation Date area: input the values, for example, Regular 3 Months1st date: for example, <the current date + 1 year>In the Due Date area:1st date: for example, <the current date + 9 months>Choose Back twice and then choose Save. | The transaction has been rolled over successfully.The following message is displayed on Trade Finance: Collective Processing screen:Financial transaction saved under number 100000000XXXX |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you roll over a bank guarantee, you need to settle the rolled over transaction before you can do further process. Normally this needs to be done once you receive the updated Bank Guarantee from the bank.

In this step, you set the settlement status for a rolled over Bank Guarantee transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing screen, enter the following data and choose Run:Company code: for example, 3310Transaction: for example, <Transaction number wrote down in previous step>NoteKeep the default values for all the other fields. | The transaction is displayed on the Trade Finance: Collective Processing screen. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing screen, select the checkbox before the transaction created in previous step, and choose Settle.On the Settle Bank Guarantee: Structure screen choose Save.Note If the following messages displays, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Bank Guarantee transaction is settled. The following message displays:Financial transaction saved under number 100000000XXXX.Note If you choose Display on Trade Finance: Collective Processing view, you should see the Transaction is now in the Rollover Settlement status. |  |

##### Bank Guarantee Fees and Cash Collateral Payment

The rolled over transaction may bring additional bank fee and cash collateral. In this section, you make the additional payment.

###### Display Payment Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the payments schedule for the rolled over the Bank Guarantee transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Payment Schedules screen, enter the following data, and choose Run:OTC Transactions: <select this checkbox>Company Code: for example, 3310End of Term in the Future: <select this checkbox>End of Term in Lapsed: <select this checkbox>Payment Period: for example, <the current date to the current date + 2 years>Payment Status: for example, 1Financial Transaction: <transaction number wrote down in previous step>Output Error Log: <select this checkbox> | The payment schedule report appears for your review.Note Make a note of the transaction number and payment date displayed on this view. |  |

###### Corporate Initiated Payments

Purpose

This section describes how to handle the corporate initiated outgoing payments via payment requests.

There are two options to process the outgoing payments:

1. Process the payment with the ‘Auto. Payment Run’ function.
2. Process the payment without the ‘Auto. Payment Run’ function.

If the payment is initiated by the bank without using payment request, skip the current step, and continue with the step [Post to General Ledger](#unique_31) [page ] 58.

Prerequisites

You have settled the contract in the previous step.

###### Option 1: Generate and Automatically Process Payment Request

###### Process the Payment with the ‘Auto. Payment Run’ Function

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <the latest payment date you noted down in the previous procedure or current date + 1 years>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <the latest payment date you noted down in the previous procedure or current date + 1 years>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.If scope item (3NA) Treasury Workstation Payment Integration is activated and the certain communication arrangement with communication scenario - Finance - Treasury Payment Request Integration (SAP_COM_0442) is also activated in your system, the Payment Control area will not appear in the selection screen. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
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

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment requests for outflows, which does not create posting in financial accounting.

If payment is initiated by the financial partner, skip this procedure and the [Process Payment Request](#unique_22) [page ] 39 procedure and continue with the [Bank Initiated Payment](#unique_23) [page ] 42 procedure.

|  |
| --- |
| Note To schedule a background job for this step, see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted in the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <the latest payment date you noted down in the previous procedure or current date + 1 years>Test Run: <select>Pay Only: <select this indicator>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | The Payment Log - Test Run displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | The Information Overview dialog is displayed with following 2 lines:Payment LogMessages |  |
| 5 | Get Payment Request Key | On the Information Overview screen, double click on Payment Log to check the payment log. | On the Payment Log screen, the key numbers of the payment request are displayed.Note Write down the key numbers of the payment requests to be processed in the next step. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down in the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <the latest payment date you noted down in the previous procedure or current date + 1 years>Test Run: <select> | You may choose Payment Log to review the payment information on view Payment Log - Test Run.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, enter the following data, and choose Run:Test Run: <deselect> | The Information Overview dialog is displayed with following 2 lines:Payment LogMessages |  |
| 5 | Get Payment Request Key | On the Information Overview screen, double click on Payment Log to check the payment log. | On the Payment Log screen, the key numbers of the payment request are displayed.Note Write down the key numbers of the payment requests to be processed in the next step. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the app Automatic Payment Transactions for Payment Requests (F111) to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items) but on payment requests.

Prerequisite

Payment request has been generated in previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests screen, enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters screen, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 12 months>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free selection for payment run, enter the following data and choose Save:Key number: <the key numbers you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>If Log created for all accounts displays, choose Continue.Choose Save on screen Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 5 | Schedule Proposal | Choose Schedule proposal.On the dialog box Schedule Proposal, choose Start Immediat and choose Schedule Job to confirm this dialog box.The Proposal is running message is displayed in the status bar with a yellow traffic light.Choose Update Status, until message Payment proposal has been created appears in the status bar with green traffic light.NoteIf you choose Edit Proposal, choose Continue on Accounting clerk view, the Edit Payment Proposal: Payments view should display.You should see one line with greenlight on Edit Payment Proposal: Payments view.If there is only one line with redlight or even other error messages display, then the payment proposal is not successful. In this case, you need to check and correct the error so that you can continue to do the next step of this test. | Payment proposal is generated. |  |
| 6 | Schedule Payment | Choose Schedule payment.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create SAP Bank Communication Batch) | The following step only applies if SAP Bank Communication Management is implemented in your system.On the Automatic Payment Transactions for Payment Requests screen, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium.On the Creation of Cross-Payment Run Payment Media screen, enter the following data and choose Run:Run Date: for example, <current date>Identification: for example, TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations (J78). |  |

###### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

###### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by the bank, skip the Generate Payment Request and Process Payment Request procedures because no requests are required.

Procedure

After the bank is done with the payment, you can directly post the outflows by referring to the Post to General Ledger procedure.

###### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this app to generate the posting for incoming or outgoing payment that you haven't processed in previous Generate Payment Request procedure. When using this app for this procedure, it will not create posting for outgoing payment that you processed in previous Generate Payment Request procedure using the Pay Only option.
- Process Business Transactions (TPM10): Use this app to generate the posting for outgoing payment that you processed in previous Generate Payment Request procedure using the Pay Only option.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Prerequisite

The outgoing payment handled by the payment request for this transaction was processed in previous Generate Payment Request procedure using the Pay Only option

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen displays. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows screen, enter the following data:Derivatives: <select this checkbox>Company Code: for example 3310Transaction: <transaction number with inflow or outflow which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date + 3 months>Test Run: <select this checkbox>Post Operational Only: <select this indicator>Choose Execute. | Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run.If No flows exist for processing message displays, then there is no posting required for your selection criteria. Skip the Production Run step and continue the test step using the Process Business Transactions app. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data:Test Run: <unselect this checkbox>Choose Execute: | The Posting Log: Posted Business Transactions view displays. Accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen displays. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:OTC Transactions: <select this checkbox>Company code: for example 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions view displays.Note If message You have not selected any business transactions displays, that means there is no posting are needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the Test Run: Post/Reverse Business Transactions view, choose Select All and choose Choose Those to Post, and then choose Save.The Test Run: Display Posted/Reversed Business Transactions view displays, choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions view, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 9 | Production Run | On Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Save.The Update Run: Display Posted/Reversed Business Transactions view displays, choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Terminate Bank Guarantee

During the validity period of a Bank Guarantee, if the Bank Guarantee is not needed or the related duties have been performed, then you can terminate the Bank Guarantee. In this step, you terminate the bank guarantee in the system.

##### Terminate Bank Guarantee and Confirm Cash Collateral

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you terminate a Bank Guarantee.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing view, enter the following data:Company Code: for example, 3310Transaction: for example, <the transaction number you noted down from the previous procedure>Term End: for example, <the current date>Accept the default values for other parameters and choose Run. | The transaction is displayed on Trade Finance: Collective Processing screen. |  |
| 4 | Enter the Termination date | On Trade Finance: Collective Processing screen, select the checkbox before the transaction, and choose Terminate.On Terminate Bank Guarantee: Structure screen, enter following data, and choose the Collateral tab:Terminate: for example, <the current date + 15 months>Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Terminate Bank Guarantee: Cash Collateral screen is displayed. |  |
| 5 | Change the incoming Cash Collateral payment date | On the Terminate Bank Guarantee: Cash Collateral screen, change the payment date of the second line as below, and choose Save:Payment Date: <the current date + 15 months>Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The transaction is terminated successfully.The following message is displayed on Trade Finance: Collective Processing screen.Financial transaction saved under number 100000000XXXX |  |

##### Automatic Release Facility

Purpose

Once the Bank Guarantee is in Termination status, the facility used in the transaction is released automatically.

Procedure

This step doesn't require any operation in system. If you want to review the facilities utilization, refer to the following procedure in the Debt and Investment Management(1WV) test script:

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

After you terminate the bank guarantee, you need to settle the termination before you do the further process.

In this step, you set the settlement status for a terminated Bank Guarantee transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing screen, enter the following data and choose Run.Company Code: for example, 3310Transaction: for example, <Transaction number wrote down in previous step>NoteKeep the default values for all the other fields. | The transaction is displayed on the Trade Finance: Collective Processing screen. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing screen, select the checkbox before the transaction you created in the previous step, and choose Settle.On the Settle Bank Guarantee: Structure screen, you can see the status as below:Activity: Termination SettlementChoose Save.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The Bank Guarantee transaction is settled. The following message is displayed:Financial transaction saved under number 100000000XXXX.Note If you choose Display on the Trade Finance: Collective Processing screen, you can see the transaction is now in the Termination Settlement status. |  |

##### Bank Guarantee Fees and Cash Collateral Payment

Once a Bank Guarantee is terminated, the Cash Collateral is returned by the bank.

###### Display Payment Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the payment schedule after you terminate the Bank Guarantee transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Payment Schedules screen, enter the following data, and choose Run:OTC Transactions: <select this checkbox>Company Code: for example, 3310End of Term in the Future: <select this checkbox>End of Term in Lapsed: <select this checkbox>Payment Period: for example, <the current date to the current date + 2 years>Payment Status: for example, 1Financial Transaction: <the transaction number you noted down in the previous step>Output Error Log: <select this checkbox> | The payment schedule report is displayed for your review.Note Make a note of the transaction number and payment date. |  |

###### Corporate Initiated Payments

Purpose

This section describes how to handle the corporate initiated outgoing payments via payment requests.

There are two options to process the outgoing payments:

1. Process the payment with the ‘Auto. Payment Run’ function.
2. Process the payment without the ‘Auto. Payment Run’ function.

If the payment is initiated by the bank without using payment request, skip the current step, and continue with the step [Post to General Ledger](#unique_38) [page ] 75.

Prerequisites

You have settled the contract in the previous step.

###### Option 1: Generate and Automatically Process Payment Request

###### Process the Payment with the ‘Auto. Payment Run’ Function

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows. Within these two apps, if you select the ‘Schedule Auto Payment Run’ option, system will automatically process the automatic payment run for payment requests.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <the latest payment date you noted down in the previous procedure or current date + 2 years>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <the latest payment date you noted down in the previous procedure or current date + 2 years>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the check box Send for Approval will be uncheckable.If scope item (3NA) Treasury Workstation Payment Integration is activated and the certain communication arrangement with communication scenario - Finance - Treasury Payment Request Integration (SAP_COM_0442) is also activated in your system, the Payment Control area will not appear in the selection screen. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
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

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment requests for outflows, which does not create posting in financial accounting.

If payment is initiated by the financial partner, skip this procedure and the Process Payment Request procedure and continue with the Bank Initiated Payment procedure.

|  |
| --- |
| Note To schedule a background job for this step, see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted in the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <the latest payment date you noted down in the previous procedure or current date + 2 years>Test Run: <select>Pay Only: <select this indicator> | The Payment Log - Test Run displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | The Information Overview dialog is displayed with following 2 lines:Payment LogMessages |  |
| 5 | Get Payment Request Key | On the Information Overview screen, double click on Payment Log to check the payment log. | On the Payment Log screen, the key numbers of the payment request are displayed.Note Write down the key numbers of the payment requests to be processed in the next step. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Trade Finance: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down in the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <the latest payment date you noted down in the previous procedure or current date + 2 years>Test Run: <select> | You may choose Payment Log to review the payment information on view Payment Log - Test Run.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, enter the following data, and choose Run:Test Run: <deselect> | The Information Overview dialog is displayed with following 2 lines:Payment LogMessages |  |
| 5 | Get Payment Request Key | On the Information Overview screen, double click on Payment Log to check the payment log. | On the Payment Log screen, the key numbers of the payment request are displayed.Note Write down the key numbers of the payment requests to be processed in the next step. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the app Automatic Payment Transactions for Payment Requests (F111) to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items) but on payment requests.

Prerequisite

Payment request has been generated in previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests screen, enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters screen, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 12 months>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free selection for payment run, enter the following data and choose Save:Key number: <the key numbers you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>If Log created for all accounts displays, choose Continue.Choose Save on screen Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 5 | Schedule Proposal | Choose Schedule proposal.On the dialog box Schedule Proposal, choose Start Immediat and choose Schedule Job to confirm this dialog box.The Proposal is running message is displayed in the status bar with a yellow traffic light.Choose Update Status, until message Payment proposal has been created appears in the status bar with green traffic light.NoteIf you choose Edit Proposal, choose Continue on Accounting clerk view, the Edit Payment Proposal: Payments view should display.You should see one line with greenlight on Edit Payment Proposal: Payments view.If there is only one line with redlight or even other error messages display, then the payment proposal is not successful. In this case, you need to check and correct the error so that you can continue to do the next step of this test. | Payment proposal is generated. |  |
| 6 | Schedule Payment | Choose Schedule payment.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create SAP Bank Communication Batch) | The following step only applies if SAP Bank Communication Management is implemented in your system.On the Automatic Payment Transactions for Payment Requests screen, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media screen, enter the following data and choose Run:Run Date: for example, <current date>Identification: for example, TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations (J78). |  |

###### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

###### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by the bank, skip the Generate Payment Request and Process Payment Request procedures because no requests are required.

Procedure

After the bank is done with the payment, post the outflows directly by referring to the Post to General Ledger procedure.

###### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this app to generate the posting for incoming or outgoing payment that you haven't processed in previous Generate Payment Request procedure. When using this app for this procedure, it will not create posting for outgoing payment that you processed in previous Generate Payment Request procedure using the Pay Only option.
- Process Business Transactions (TPM10): Use this app to generate the posting for outgoing payment that you processed in previous Generate Payment Request procedure using the Pay Only option.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Prerequisite

The outgoing payment handled by the payment request for this transaction was processed in previous Generate Payment Request procedure using the Pay Only option

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen displays. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows screen, enter the following data:Derivatives: <select this checkbox>Company Code: for example 3310Transaction: <transaction number with inflow or outflow which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date + 2 years>Test Run: <select this checkbox>Post Operational Only: <select this indicator>Choose Execute. | Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run.If No flows exist for processing message displays, then there is no posting required for your selection criteria. Skip the Production Run step and continue the test step using the Process Business Transactions app. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data:Test Run: <unselect this checkbox>Choose Execute. | The Posting Log: Posted Business Transactions view displays. Accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen displays. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:OTC Transactions: <select this checkbox>Company code: for example 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions view displays.Note If message You have not selected any business transactions displays, that means there is no posting are needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the Test Run: Post/Reverse Business Transactions view, choose Select All and choose Choose Those to Post, and then choose Save.The Test Run: Display Posted/Reversed Business Transactions view displays, choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions view, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 9 | Production Run | On Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Save.The Update Run: Display Posted/Reversed Business Transactions view displays, choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in local GAAP (valuation area AE0). |  |

### Receive Bank Guarantee

#### Receive Bank Guarantee

In this section, you maintained the Bank Guarantees received from your business counterparties.

##### Generate Limit Utilizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the end of the transaction day, you execute the End-of-Day Processing (KLNACHT) app to complete necessary end of day processes. The system determines and updates limit utilization based on the transactions and positions contained in the data pool, as well as the external transactions that were entered.

|  |
| --- |
| Note You can schedule a background job for this step. For more information. Refer to the Job Scheduling section in the Appendix for detail. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open End-of-Day Processing (KLNACHT). | The End-of-Day Processing screen is displayed. |  |
| 3 | Enter Criteria of End-of-Day Processing | On the End-of-Day Processing view, enter the following data, and choose Run:Valuation Date: for example, <Current Date>Determination Procedure: for example, 10 to 20Company code: for example, 3310 | The End-of-day processing was completed successfully message is displayed. |  |

##### Check Limit Utilization Report (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the Limit Utilization Report.

Prerequisite

The limit master records of your company are maintained in the system.

You have completed the previous [Generate Limit Utilizations](#unique_39) [page ] 77 procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Run:Limit Type: for example, Y01 or Y07Limit Utilization Base: for example, 1Determination Date: for example, <the current date>Limits Valid From: for example, <the current date> | An overview of the limit utilization in accordance with your selection criteria is displayed. |  |

##### Receive Bank Guarantee

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once you receive a Bank Guarantee, enter the Bank Guarantee information into the system. Normally, as the receiver or beneficiary of a Bank Guarantee, you don't pay any cash collateral. Also, the issuing bank won't charge you. So normally there won't be any outgoing or incoming payments. However, in some special cases, for example back to back Bank Guarantees, there could be payments coming with receiving Bank Guarantees.

In this step, you maintain the received bank guarantee information in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Create Bank Guarantee (FTRTBG01). | The Create Bank Guarantee: Initial Screen screen is displayed. |  |
| 3 | Enter Data on Initial Screen | Enter the following data, and choose Enter:Company Code: for example, 3310Product Type: for example, 86ATransaction Type: for example, 200Partner: for example, 33537001 | The data is entered and Create Bank Guarantee: Structure screen is displayed. |  |
| 4 | Enter Data on Structure tab | On the Create Bank Guarantee: Structure screen, enter the following data, and choose Save:Flow Type: 1860Amount: for example, 1mStart: for example, <the current date>End: for example, <the current date + 1 year>Bank Guar. Number: for example, 201710BG002Bank Guar. Type: for example, PAYMApplicant: for example, search for a customer with BP role FLCU00 or FLCU01.Note If there is no customer master data with the FLCU00 or FLCU01 BP role, you can refer to following master data script to create a customer:Create Customer Master - MDS (BND)You may also manually enter the Applicant data:Applicant Entered Manually: <select this checkbox and more fields show up on the screen>Company Name: for example, <your customer's name>Company Name Ext:for example, <your customer's name>Contact Person: for example, <enter your customer's sales person's name>Company Address: for example, <your customer's address>Company Addr Ext: for example, <your customer's address>Note If the following message are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working dayIf there are incoming or outgoing payments coming with the Bank Guarantee, you can also enter those fees in Free Conditions or on the Other Flows tabs. In this case, you can refer to Issue Bank Guarantee section to enter the data. | The Bank Guarantee is saved.The following message is displayed:Financial transaction saved under number 100000000XXXX.Write down this transaction number. |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you settle the received bank guarantee you created in the previous step, before you can do further processes. Normally this needs to be done once you receive the Bank Guarantee from the bank.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing screen, enter the following data and choose Run.Company Code: for example, 3310Transaction: for example, <the transaction number you noted down in the previous step>Note Keep the default values for all the other fields. | The transaction is displayed on the Trade Finance: Collective Processing screen. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing screen, select the checkbox before the transaction, and choose Settle.On the Settle Bank Guarantee: Structure screen, and choose Save.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working dayNote For receiving Bank Guarantees without incoming or outgoing payments, once the transaction is settled, the whole process is done.Note If you've already entered incoming or outgoing payments in the previous step, then you need also to finish the whole payment process by referring to the whole Bank Guarantee Fees and Cash Collateral payment process under Issue Bank Guarantee. | The Bank Guarantee transaction is settled. The following message is displayed:Financial transaction saved under number 100000000XXXX. |  |

#### Roll Over Bank Guarantee

##### Rollover Bank Guarantee

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you roll over the received bank guarantee transaction once you receive a renewed bank guarantee. You may change some conditions, for example, the amount or validity term of the bank guarantee.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing screen, enter the following data:Company Code: for example, 3310Transaction: for example, <the transaction number you noted down in the previous procedure>Term End: for example, <the current date>Accept the default values for the other parameters and choose Run. | The transaction is displayed on the Trade Finance: Collective Processing screen. |  |
| 4 | Roll Over the Transaction | On the Trade Finance: Collective Processing screen, select the checkbox before the transaction, and choose Roll Over.On the Roll Over Bank Guarantee: Structure screen, enter following data, and choose Save:Amount: for example, 2MRollover: for example, <the current date + 3 months>End: for example, <the current date + 2 years>Note If the following messages are displaysed choose Continue.No limits were exceededMM/DD/YYYY is not a working dayTerm end changed; consider pymnt date of cash collateral incoming line | The transaction is rolled over successfully.The following message is displayed on the Trade Finance: Collective Processing screen:Financial transaction saved under number 100000000XXXX |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set the Settlement status for rolled-over bank guarantee transaction before you conduct further process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing screen, enter the following data and choose Run.Company Code: for example, 3310Transaction: for example, <the transaction number you noted down in the previous step>NoteKeep the default values for all the other fields. | The transaction is displayed on the Trade Finance: Collective Processing screen. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing screen, select the checkbox before the transaction created in previous step, and choose Settle.On the Settle Bank Guarantee: Structure screen, choose Save.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working dayNote For receiving Bank Guarantees without incoming or outgoing payments, once the transaction is settled, the whole process is done.Note If you've already entered incoming or outgoing payments in previous step, then you need also to finish the whole payment process by referring to the whole Bank Guarantee Fees and Cash Collateral payment process under Issue Bank Guarantee. | The Bank Guarantee transaction is settled. The following message is displayed:Financial transaction saved under number 100000000XXXXNote If you choose Display on the Trade Finance: Collective Processing screen, you can see the Transaction is now in the Rollover Settlement status. |  |

#### Terminate Bank Guarantee

During the validity period of a Bank Guarantee, if the Bank Guarantee is not required, then you terminate the Bank Guarantee.

##### Terminate Bank Guarantee

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you terminate the received Bank Guarantee.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing screen, enter the following data:Company Code: for example, 3310Transaction: for example, <the transaction number you noted down in the previous procedure>Term End: for example, <the current date>Accept default values for other parameters and choose Run. | The transaction is displayed on the Trade Finance: Collective Processing screen. |  |
| 4 | Terminate the Transaction | On the Trade Finance: Collective Processing screen, select the checkbox before the transaction, and choose Terminate.On the Terminate Bank Guarantee: Structure screen, enter following data, and choose Save:Terminate: for example, <current date + 6 months>Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working day | The transaction is rolled over successfully.The following message is displayed on Trade Finance: Collective Processing screen:Financial transaction saved under number 100000000XXXX |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a Bank Guarantee is terminated, you need to settle before further process.

In this step, you set the settlement status for a terminated Bank Guarantee transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Finance Transactions - Collective Processing (FTRTLC00). | The Trade Finance: Collective Processing screen is displayed. |  |
| 3 | Enter Data on Initial View | On the Trade Finance: Collective Processing screen, enter the following data and choose Run.Company Code: for example, 3310Transaction: for example, <the transaction number you noted down in the previous step>Note Keep the default values for all the other fields. | The transaction is displayed on the Trade Finance: Collective Processing screen. |  |
| 4 | Settle the Transaction | On the Trade Finance: Collective Processing screen, select the checkbox before the transaction created in previous step, and choose Settle.On the Settle Bank Guarantee: Structure screen, you can see the status as below:Activity: Termination SettlementChoose Save.Note If the following messages are displayed, choose Continue.No limits were exceededMM/DD/YYYY is not a working dayNote For receiving Bank Guarantees without incoming or outgoing payments, once the transaction is settled, the whole process is done.Note If you've already entered incoming or outgoing payments in previous step, then you need also to finish the whole payment process by referring to the whole Bank Guarantee Fees and Cash Collateral payment process under Issue Bank Guarantee. | The Bank Guarantee transaction is settled. The following message is displayed:Financial transaction saved under number 100000000XXXX.Note If you choose Display on Trade Finance: Collective Processing view, you can see the Transaction is now in the Termination Settlement status. |  |

### Reports

#### Display Treasury Posting Journal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display posting journals for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as aTreasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal (F1755) screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Product Group: for example, OTC TransactionsCompany Code: for example, 3310 | The posting journals display per the filter values. |  |

#### Treasury Position Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the treasury position analysis report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Treasury Position Analysis (W0049). | The Treasury Position Analysis screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, <the current date>Include Planned Data: for example, 1Valuation Area: for example, AE0Company Code: for example, 3310Product Type: for example, <choose the proper product type(s)>Note You can enter multiple product types by pressing Enter in between. | The position analysis data displays per the filter values. |  |

#### Treasury Position History

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the treasury position history.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Treasury Position History (F3966) | The Treasury Position History screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, <the current date>Period: for example, <Year to Date>Display Currency: for example, AEDExchange Rate Type: for example, MValuation Area: for example, AE0Company Code: for example, 3310. | The data is displayed per the filter values. |  |

#### Display Treasury Position Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the treasury position values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Values (F1867). | The Display Treasury Position Values screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, <the current date>Product Group: for example, OTC TransactionsCompany Code: for example, 3310Note You may need to make filters available by adapting filters, for example, enable the Product Group filter in the Position Values filter group. | The position values data is displayed per the filter values. |  |

#### Define Financial Positions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define a set of key figures to be displayed in Financial Status - Book Value and Financial Status - Nominal Amount screens.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Financial Positions (FTR_FP_DEF). | The "Maintain Financial Position Groups": Change screen displays. |  |
| 3 | Maintain Key Figure Groups | Select New Entries.Enter data for a record of new entry and select Save.Financial Position Group: for example, FPG_MM_A0001Financial Position Group Description: for example, <Bank accounts and Short term invest>Assets/Liabilities: for example, Assets | The data is saved. |  |
| 4 | Maintain Key Figures | Switch to Maintain Financial Positions tab.Enter data and choose Save.Financial Position: for example, FP_MM_A0001Financial Position Description: for example, Bank accountsFinancial Position Group: for example, FPG_MM_A0001Data Source: for example, One Exposure | The data is saved. |  |
| 5 | Maintain Selections | Choose Back to display all financial postions. Select one financial position and select Maintain Selections.House Bank: for example, AEBK1Choose Back and choose Save. | The data is saved. |  |
| 6 | Enter More Data | Enter more financial positions data as below tables. |  |  |

| Financial Position Group | Financial Position Group Description | Assets/Liabilities |
| --- | --- | --- |
| FPG_MM_A0001 | Bank accounts and short term invest. | Assets |
| FPG_MM_A0002 | Long term invest. and other assets | Assets |
| FPG_MM_L0001 | Short term debt | Liabilities |
| FPG_MM_L0002 | Long term debt and other liabilities | Liabilities |

| Financial Position | Financial Position Description | Financial Position Group | Data Source | Maintain Selection |
| --- | --- | --- | --- | --- |
| FP_MM_A0001 | Bank accounts | FPG_MM_A0001 | One exposure | House Bank: for example, AEBK1 |
| FP_MM_A0002 | short term investments | FPG_MM_A0001 | Treasury position management | Product Type = 51A to 55ATransaction Type = 100 to 199Valuation Class = 20 to 29Valuation Area = AE0Posting Status = 2 |
| FP_MM_A0003 | g term investments | FPG_MM_A0002 | Treasury position management | Product Type = 51A to 55ATransaction Type = 100 to 199Valuation Class = 10 to 19Valuation Area = AE0Posting Status = 2 |
| FP_MM_A0004 | Other assets | FPG_MM_A0002 | One document balances | Account Number = 12041000 to 1204199912042000 to 1204299912701000 to 12701999Chart of Account = YCOALedger = 0L |
| FP_MM_L0001 | Short term debt | FPG_MM_L0001 | Treasury position management | Product Type = 51A to 55ATransaction Type = 200 to 299Valuation Class = 20 to 29Valuation Area = AE0Posting Status = 2 |
| FP_MM_L0002 | Long term debt | FPG_MM_L0002 | Treasury position management | Product Type = 51A to 55ATransaction Type = 200 to 299Valuation Class = 10 to 19Valuation Area = AE0Posting Status = 2 |
| FP_MM_L0003 | Other liabilities | FPG_MM_L0002 | One document balances | Account Number = 22541000 to 2254199922542000 to 22542999Chart of Account = YCOALedger = 0L |

#### Financial Status (Book Value)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display financial status on book values.

Prerequisite

Financial positions are already defined.

Refer to [Define Financial Positions](#unique_50) [page ] 91 for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Financial Status (F2136). | The Financial Status - Book Value screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, <Current Date>Display Currency : for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays per the filter values. |  |

#### Financial Status (Nominal Amount)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the financial status of the nominal amount.

Prerequisite

Financial positions are defined.

Refer to [Define Financial Positions](#unique_50) [page ] 91 for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)). | The Financial Status - Nominal Amount screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Key Date: for example, <Current Date>Display Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays per the filter values. |  |

#### Display Treasury Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can display all payment journals for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Payments (TPM20A). | The Payment Journal screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Run.Company Code: for example: 3310Product Type: 51A,53A,54A and 55A | The payment journals display. |  |
| 4 | Review data | Review the data displayed on the screen. You can also choose Original business transaction or Details to drill down for more details. |  |  |

#### Display Treasury Position Flows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to display the position flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows view displays. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Position Flows view, enter following data:Product Group: for example: OTC TransactionsCompany code: for example, 3310and choose Go. | Position Flow data displays according to the filter values. |  |

#### Display Treasury Alerts - Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display treasury alerts for posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Alerts - Posting (F4984). | The Display Treasury Alerts - Posting screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Alerts screen, enter following data, and choose Go:Issue Message For: PostingCompany Code: for example, 3310 | Alerts data is displayed per the filter values. |  |

#### Display Treasury Alerts- Settlement, Release, Payment, Correspondence and Interest Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the treasury alerts for various types of transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Alerts - Settlement (F4979). | The Display Treasury Alerts - Settlement view displays with Issue Message For: Settlement. |  |
| 3 | Enter Selection Criteria | Enter following data, and choose Go:Issue Message For: SettlementCompany Code: for example, 3310 | Alerts data displays per the filter values. |  |
| 4 | Confirm Alerts for Other Transactions | In the following steps, you display treasury alert results by selecting other SAP Fiori apps:ReleasePaymentCorrespondenceInterest Rates |  |  |
| 5 | Select Display Treasury Alerts Tiles with Release | Return to the Home view and open Display Treasury Alerts - Release (F4980). | The Display Treasury Alerts view is displayed, with Issue Message For:Release. |  |
| 6 | Select Display Treasury Alerts Tiles with Payment | Return to the Home view and open Display Treasury Alerts - Payment (F4981). | The Display Treasury Alerts view is displayed, with Issue Message For:Payment. |  |
| 7 | Select Display Treasury Alerts Tiles with Correspondence | Return to the Home view and open Display Treasury Alerts - Correspondence (F4983). | The Display Treasury Alerts view is displayed, with Issue Message For:Correspondence. |  |
| 8 | Select Display Treasury Alerts Tiles with Interest Rates | Return to the Home view and open Display Treasury Alerts - Interest Rates (F4982). | The Display Treasury Alerts view is displayed, with Issue Message For:Interest Rates. |  |

#### Display Payment Schedules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the payment schedule for interest flows due.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules view displays. |  |
| 3 | Enter Selection Criteria | Enter the following data:OTC Transactions: <select this checkbox>Company code: for example, 3310End of Term in the Future: <select this checkbox>End of Term Lapsed: <select this checkbox>Payment Period: for example, <Current Date to Current Date + 5 days>Payment Status: for example, 1Output Error Log: <select this checkbox>and choose Run. | Review the check payment schedule report. |  |

#### Analyze Net Present Value (NPV)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you calculate and display Net Present Value (NPV) result.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Analyze NPV (JBRX). | The NPV Analysis: Display of Single Values view displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <Current Date>Portfolio Hierarchy: for example, 100 | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date.Note If transaction end date is before evaluation date, there is no output. |  |
| 4 | Enter Selection Criteria of Characteristics | Choose the Characteristics tab and enter the following data, and then choose Run:Company Code: for example, 3310Product Type: for example, <product type of the transaction number you noted down in the previous procedure>and then choose Run. | The NPV Result displays based on the portfolio hierarchy. |  |

#### Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you calculate and display the key figures for the Net Present Value (NPV) analysis and the sensitivity key figures for selected transactions. You can use the key figures as the basis for defining formula-based key figures and display them with the NPV and sensitivity key figures.

Prerequisite

Report Layout for key figure should be maintained. For more information, see the [Defining Report Layout for Calculate Market Risk Key Figures](#unique_81) [page ] 117 in the Appendix.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Calculate Market Risk Key Figures (AISGENKF). | The Single Value Analysis for Generic Key Figures view displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <Current Date>Report Layout: for example, <Y01 or any other Report Layout you created>Portfolio Hierarchy: for example, 100 | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date.Note If transaction end date is before/on evaluation date, there is no output. |  |
| 4 | Enter Selection Criteria | Choose the Characteristics tab and enter the following data and then choose Run:Company Code: for example, 3310Product Type: for example, 86A | The Single Value Analysis for the assigned report layout displays. |  |

#### Sensitivity Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you process sensitivity key figures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Sensitivity Key Figures - Single Analysis (AISS). | The Sensitivity Key Figures - Single Analysis (AISS) view displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Enter the following data:Display Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <End Date of Current Month>Portfolio Hierarchy: for example, 100 | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date.Note If transaction end date is before/on evaluation date, there is no output. |  |
| 4 | Enter Selection Criteria | Choose the Characteristics tab, enter the following data:Company Code: for example, 3310Product Type: for example, 86Aand then choose Run. | The Sensitivity Key Figures - Single Analysis (AISS) report displays based on the portfolio hierarchy. |  |

#### Review Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to Review Limit Utilization Report.

Prerequisite

The limit master records of your company is maintained in the system.

You successfully completed the processing in the previous test procedure Generate Limit Utilizations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Run:Limit Type: for example, Y01 or Y07Limit Utilization Base: for example, 1Determination Date: for example, <the current date>Limits Valid From: for example, <the current date> | An overview of the limit utilization in accordance with your selection criteria is displayed. |  |

## Appendix

### Job Scheduling

#### Generate Limit Utilizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to generate limit utilizations.

Prerequisite

You have imported the market data.

If security exists, the spot price needs to be maintained for the current date. Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Middle Office Jobs (F2772). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information for New Job | On the Template Selection area, enter following data then choose Step 2:Job Template: for example, <End of Day Processing>Job Name: for example, <End of Day Processing> | You've chosen the job template, and are navigated to the Scheduling Options area. The New Job: Calculate Market Risk Key Figures view displays. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, enter the following data then choose Step 3:For Start Immediately case:Start Immediately: <select>For Recurrence case:Start Immediately: <deselect>Choose Define Recurrence Pattern to define the recurrence pattern in the Scheduling Information dialog box.Start: for example, <Current Date/Current Time>Recurrence Pattern: for example, DailyEvery: for example, 1End: for example, after 7 Occurrence(s)On Non-Working Day: Run on next Working DayNote Schedule this job after back office's job for generating payment request by using the same job template. | You've enter the scheduling recurrence pattern, and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area, enter the following data and choose Schedule:Company Code: 3310Determination Procedure: <select 10 and 20 from the F4 help input> |  |  |
| 7 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The result is displayed in the Job Details screen. |  |

#### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a background job to generate the payment requests for flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs view, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Fix, Pay and Post FlowsJob Name: for example, <Generate Payment Request> | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and in the Scheduling Information dialog box, enter the following data:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time default>Time Zone: <select a time zone or use default>Recurrence Pattern: for example, DailyEvery: for example, 1Day(s)End: for example, select After and then enter 7 occurrence(s)On Non-Working Days: for example No RestrictionChoose OK, and choose Step 3.Note If you would rather to start job at once, select Start Immediately checkbox. | You've defined the recurrence pattern and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area,In the Application sub-area, select one or more proper product groupIn the General Selection sub-area, enter the following data:Company Code: for example, 3310Transaction: <enter transaction numbers if you'd like to limit transactions>Product Type: <enter product types if you'd like to limit product types>Due Date (Dynamic): for example, 0On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.In the Posting Control sub-area,Test Run: <deselect>Pay Only: <select>Note You can also choose the Post All Valuation Areas radio button, if you want to post to all valuation areas |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details view displays. |  |

#### Post Flows to General Ledger

##### Template - Fix, Pay and Post Flows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to generate the posting for incoming payment without a payment request.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information for New Job | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Fix, Pay and Post FlowsJob Name: Post Flows | The New Job: Post Flows screen is displayed. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information dialog box :Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day:for example, Run on next Working DayChoose OK, and choose Step 3.Note If you would like to start job at once, select the Start Immediately checkbox.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Application sub-area, select a proper Application.In the General Selection sub-area, enter the following data:Company Code: for example, 3310Transaction: <enter transaction numbers if you'd like to limit transactions>Product Type: <enter product types if you'd like to limit product types>Due Date (Dynamic): for example, 0In the Posting Control sub-area, make the following selections:Test Run: <deselect this checkbox>Post Operational Only: <Choose this radio button>Note You can also choose Post All Valuation Areas (instead of Post Operational Only) to post flows to all valuation areas. |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details view displays. |  |

##### Template - Process Business Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to fix and post the outgoing payment, which was processed in the previous Generate Payment Request step with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs view, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Process Business TransactionsJob Name: for example, Process Business Transactions |  |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Product Groups sub-area, select one or more product groups.Company Code: for example, 3310Valuation Area: for example, AE0, or leave it blank (run for all valuation areas)In the Limit by Transaction Number sub-area, make the following selection:Limit by Transaction Number: <deselect this checkbox>In the Limit by Subledger Positions sub-area, make the following selection:Limit by Subledger Pos.: <select this checkbox>Product Type: <enter product types if you'd like to limit product types>Transaction: <enter transaction numbers if you'd like to limit transactions>In the Limit by Business Transactions sub-area, make the following selection:Trans. to Be Fixed/Posted: <select this checkbox>In the Posting Control sub-area, make the following selection:Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

#### Post Realized Profit and Loss

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to fix and post derived business transactions (usually for realized profit and loss when deal is mature).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Post Derived Business TransactionsJob Name: for example, Post Derived Business Transactions |  |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, enter the following data, and choose Step 3:Start Immediately: <select this checkbox>Note You can define recurrence pattern by choosing Define Recurrence Pattern, if you don't want to start the job immediately. | You've defined the scheduling option and are navigated to the Parameters area |  |
| 6 | Enter Parameters for New Job | In the Parameters areas, enter the following data:Company Code: for example 3310Valuation Area: for example, AE0,or leave it blank (run for all valuation areas)In the OTC Transactions sub-area, enter the following data:OTC Transactions: <enter transaction numbers if you'd like to limit transactions>In the Selections for Fixing Derived Business Transactions sub-area, enter the following data:TRL Date: for example, <current date>In the Posting Control subarea, make the following selection:Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule the New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

#### Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to calculate market risk key figures, including the key figure Value at Risk. The result of calculation is persisted in the database for analysis with the SAP Analytics Cloud. The calculation risk keys are defined in the market risk key figure set.

This step is different from the Calculate Market Risk Key Figures step in the Reports section, which is a real-time calculation for the risk keys in the defined report layout.

|  |
| --- |
| Note There are three methods to calculate the Value at Risk key figure, the historical simulation, the Monte Carlo simulation and a parametric method (variance-covariance approach).For the historical simulation, the daily market data of past 250 days needs to be maintained.For the Monte Carlo simulation and the variance-covariance approach, the statistical data of volatility or correlation is required. The calculation is based on the historical daily market data. You need to maintain the daily market data of past 113 days. |

Prerequisites

You have maintained the market risk key figure set, as described in the Manage Market Risk Key Figure Sets step in the Appendix section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Middle Office Jobs (F2772). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The New Job screen is displayed. |  |
| 4 | Enter General Information for New Job | In the Template Selection sub-area, enter the following data, and choose Step 2:Job Template: Calculate Market Risk Key FiguresJob Name: for example, Calculate Market Risk Key FiguresNote You can delete the existing market risk key figure values on the specified evaluation date by the Delete Market Risk Key Figures job template. |  |  |
| 5 | Enter Parameters for New Job | In the Scheduling Options area, enter the following data, and choose Step 3:Start Immediately: <select this checkbox> |  |  |
| 6 | Enter Selection Data for New Job | In the General sub-area, enter the following data:Basic Run: <select this checkbox>Adjustment Run: <deselect this checkbox>Note The adjustment run processes new financial objects and financial objects for which errors have occurred in the base run.In the Evaluation Parameters sub-area, enter the following data:Market Risk Key Figure Set: for example, <MRK01, and MRK02, the key figure set you maintained>Evaluation Date (Dynamic): for example, <the current date, or enter the evaluation date>Volas + Correlations: <deselect this checkbox, determine whether calculate statistical figure as volatilities or correlations> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are back to the initial screen, and the job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose  at the end of the row for the job you just scheduled. | The Job Details screen is displayed.If it is in status Finished (depends on parameters you entered for Scheduling Options), click on the icon beside Results, a new window will open and you can check the result of this finished job. |  |

### Market Risk Analyzer

#### Manage Market Data Shift

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The objective of this step is to create market data shifts to be able to analyze key figures with modified market data, and it will be used in the step Defining Report Layout for Calculate Market Risk Key Figures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Middle Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Market Data Shift (JBR0) | The Edit Market Data Shifts screen displays. |  |
| 3 | Enter Market Data Shifts Name | On the Edit Market Data Shifts screen, enter the following data and choose Create:Market Data Shift: for example, 1 | The Define Market Data Shifts screen displays. |  |
| 4 | Define Market Data Shift | On the Edit Market Data Shifts screen, enter the following dataShort Name: for example, Market Data Shift 0001 |  |  |
| 5 | Maintain Yield Curves of Market Data Shift | On the Edit Market Data Shifts screen, choose Yield Curves tap, choose Insert Row button, then enter the following data and choose SaveShort Name: for example, Euro Depo ShiftCurrency: for example, EURYC. Type: for example, 0001Ref.Int.Rate: for example, EURM01EURPercentage: for example, 2 | Market Data Shift is saved |  |

#### Defining Report Layout for Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the report layout for market risk key figures report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Calculate Market Risk Key Figures (AISGENKF). | The Calculate Market Risk Key Figures screen is displayed. |  |
| 3 | Access Report Layout Definition screen | On the Calculate Market Risk Key Figures screen, enter the Evaluation Currency and Evaluation Type, and choose Define Report Layout. | The "Key Figure Layout": Change screen is displayed. | . |
| 4 | Create Layout-ID entries | On the "Key Figure Layout": Change screen, Choose New Entries, then insert the following data in the Key Figure Layout form and Save:ROW1Layout-ID: for example, Y01Short Name: for example, NPV/BPV/DurationLong Name: for example, NPV/BPV/DurationROW2Layout-ID: for example, Y02Short Name: for example, NPV + Market Data shiftsLong Name: for example, NPV + Market Data shifts | Two new entries have been created. |  |
| 5 | Access Key Figures Maintain screen | On the "Key Figure Layout": Change screen, select the checkbox of Layout-ID Y01, then double click Key Figures folder in the Dialog Structure panel. | The Change View "Key Figures": Overview screen is displayed in the main area. |  |
| 6 | Maintain Key Figures of Layout | On the "Key Figure Layout": Change screen, choose New Entries and then insert the following data in the Key Figures form:ROW1Key Figure Name: for example, BARWERTPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDec.Places: for example, 0ROW2Key Figure Name: for example, BPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_BASE_POINTShort Name: for example, BPVShift Rule: for example, 0Dec.Places: for example, 0ROW3Key Figure Name: for example, CRFNPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, RISK_FREE_NPVShort Name: for example, Current Risk Free NPVShift Rule: for example, 0Dec.Places: for example, 0ROW4Key Figure Name: for example, DURATION1Pos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_FWDURATIONShort Name: for example, Modified DurationShift Rule: for example, 0Dec.Places: for example, 0ROW5Key Figure Name: for example, DURATION2Pos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_MACAULAYShort Name: for example, Macaulay DurationShift Rule: for example, 0Dec.Places: for example, 0and Save. | The New Entries: Overview of Added Entries screen displays allowing entry of the Key Figures name and configuration settings. |  |
| 7 | Access Key Figures Maintain screen | Go back to the New Entries: Added Entries screen, select the checkbox of Layout-ID Y02, then double click on the Key Figures folder in the Dialog Structure panel. |  |  |
| 8 | Maintain Key Figures of Layout | On the "Key Figure Layout": Change screen, Choose New Entries, then insert the following data in Key Figures form and Save:Key Figure Name: for example, NPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDecimal Places: for example, 0 |  |  |

#### Manage Market Risk Key Figure Sets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the parameters for the market risk key figures calculation, including evaluation currency, evaluation type, scenario, and market data shift rule.

The market risk key figures calculation is processed as a scheduled background job, the result of which is recorded in the database for analysis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Market Risk Key Figure Sets (AFWKF_SET) | The "Market Risk Key Figure Set": Change screen is displayed. |  |
| 3 | Define Risk Factor Set | On the "Market Risk Key Figure Set": Changescreen, double click on the Risk Factor Set folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Factor Setform:RiskF. Set: for example, R01Description: for example, Risk Factor Set with FX Rate and Yld CurvesFX Risk: <select the checkbox>IR Risk: <select the checkbox>Then select the created entry, double click on the Risk Currency folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Currency form:Row 1Currency: for example, USDlR Risk: <select the checkbox>Then double click on the Interest Rate Term folder in the Dialog Structure panel on the left side. Choose New Entries,insert the following data in the Interest Rate Term form and choose Save:Row 1Term: for example, 1Time Unit: for example, MonthRow 2Term: for example, 3Time Unit: for example, MonthRow 3Term: for example, 6Time Unit: for example, MonthRow 4Term: for example, 1Time Unit: for example, Year | A new risk factor set is created. |  |
| 4 | Maintain Market Risk Key Set | Double click on the Market Risk Key Figure Set folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Market Risk Key Figure Set form and choose Save:row 1MR Key Figure Set: for example, MRK01Description: for example, Market Key Figure Set without VaREvaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <deselect>RT Update: <select>Note If the UpdUponChg checkbox is selected, once a new financial object is created or changed, an automatic calculation of the market risk key figure set is triggered. The calculation only covers the updated object. The adjustment run is based on the basic run of same date that is processed by scheduled job.Row 2MR Key Figure Set: for example, MRK02Description: for example, Market Key Figure Set (VaR Hist.Sim.)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV1RiskF. Set: for example, R01Row 3MR Key Figure Set: for example, MRK03Description: for example, Market Key Figure Set (VaR MonteCarloSim.)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV2RiskF. Set: for example, R01Row 4MR Key Figure Set: for example, MRK04Description: for example, Market Key Figure Set (VaR Variance/Covariance)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV3RiskF. Set: for example, R01Note If the Calc. VaR checkbox is selected, the parameters of the VaR type and the risk factor set need to be assigned; the market data scenario or market data shift should be blank. | Market Risk Key Set is savedThe VaR type SV1 is for the VaR calculation method as historical simulation;The VaR type SV2 is for the VaR calculation method as Monte Carlo simulation;The VaR type SV3 is for the VaR calculation method as variance-covariance approach. |  |

#### Manage Market Risk Key Figure Sets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the parameters for the market risk key figures calculation, including evaluation currency, evaluation type, scenario, and market data shift rule.

The market risk key figures calculation is processed as a scheduled background job, the result of which is recorded in the database for analysis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Market Risk Key Figure Sets (AFWKF_SET) | The "Market Risk Key Figure Set": Change screen is displayed. |  |
| 3 | Define Risk Factor Set | On the "Market Risk Key Figure Set": Changescreen, double click on the Risk Factor Set folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Factor Setform:RiskF. Set: for example, R01Description: for example, Risk Factor Set with FX Rate and Yld CurvesFX Risk: <select the checkbox>IR Risk: <select the checkbox>Then select the created entry, double click on the Risk Currency folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Currency form:Row 1Currency: for example, USDlR Risk: <select the checkbox>Then double click on the Interest Rate Term folder in the Dialog Structure panel on the left side. Choose New Entries,insert the following data in the Interest Rate Term form and choose Save:Row 1Term: for example, 1Time Unit: for example, MonthRow 2Term: for example, 3Time Unit: for example, MonthRow 3Term: for example, 6Time Unit: for example, MonthRow 4Term: for example, 1Time Unit: for example, Year | A new risk factor set is created. |  |
| 4 | Maintain Market Risk Key Set | Double click on the Market Risk Key Figure Set folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Market Risk Key Figure Set form and choose Save:row 1MR Key Figure Set: for example, MRK01Description: for example, Market Key Figure Set without VaREvaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <deselect>RT Update: <select>Note If the UpdUponChg checkbox is selected, once a new financial object is created or changed, an automatic calculation of the market risk key figure set is triggered. The calculation only covers the updated object. The adjustment run is based on the basic run of same date that is processed by scheduled job.Row 2MR Key Figure Set: for example, MRK02Description: for example, Market Key Figure Set (VaR Hist.Sim.)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV1RiskF. Set: for example, R01Row 3MR Key Figure Set: for example, MRK03Description: for example, Market Key Figure Set (VaR MonteCarloSim.)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV2RiskF. Set: for example, R01Row 4MR Key Figure Set: for example, MRK04Description: for example, Market Key Figure Set (VaR Variance/Covariance)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV3RiskF. Set: for example, R01Note If the Calc. VaR checkbox is selected, the parameters of the VaR type and the risk factor set need to be assigned; the market data scenario or market data shift should be blank. | Market Risk Key Set is savedThe VaR type SV1 is for the VaR calculation method as historical simulation;The VaR type SV2 is for the VaR calculation method as Monte Carlo simulation;The VaR type SV3 is for the VaR calculation method as variance-covariance approach. |  |

### Credit Risk Analyzer

#### Display Limit Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to display limit overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Limit Overview (TBL3). | The Overview of Limits screen displays. |  |
| 3 | Enter Selection Criteria | On the Overview of Limits screen, enter the following data and choose Run:Limit Type: for example, Y01 to Y09Company Code: for example, 3310 | The Display Limits for Limit Types: Overview screen displays. |  |

Change Counterparty - Financial Transaction (TRTM_CHG_PARTNER)

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
- related-to :: [[05-treasury-and-cash-management/bank-guarantee-management-group-ledger-ifrs-2o2-ae-test-script-841]]
- related-to :: [[05-treasury-and-cash-management/bank-guarantee-management-group-ledger-us-gaap-34f-ae-test-script-910]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2NZ_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 217,044 chars in the whole document
