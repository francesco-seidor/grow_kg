---
id: 05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-money-market-mutual-fund-part-01
title: Test Script SAP S/4HANA Cloud Public Edition - Money Market Mutual Fund Management (2UN_AE) (2UN_S4CLD2608_BPD_EN_AE) — part 1 of 2
description: "Part 1 of 2: Step-by-step test script for scope item 2UN_AE (Money Market Mutual Fund Management, release 2608, AE localisation): prerequisites, test procedures, job scheduling appendix."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/money-market-mutual-funds]
aliases: []
keywords: [Money Market Mutual Fund Management, money market mutual fund, security class creation, fund purchase transaction, fund redemption, dividend distribution, dividend capitalization, period-end closing, treasury correspondence, payment processing]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UN_S4CLD2608_BPD_EN_AE.docx#lines-1-3335"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-873
topic: 05-treasury-and-cash-management/money-market-mutual-funds
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Money Market Mutual Fund Management (2UN_AE) (2UN_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UN_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–3335 of the extracted text), extracted with `mammoth`. Grouped under **Money Market Mutual Fund Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Money Market Mutual Fund Management (2UN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232850595)

[2 Prerequisites 6](#_Toc232850596)

[2.1 System Access 6](#_Toc232850597)

[2.2 Roles 6](#_Toc232850598)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232850599)

[2.4 Business Conditions 8](#_Toc232850600)

[2.5 Preliminary Steps 9](#_Toc232850601)

[2.5.1 Create Business Partner 9](#_Toc232850602)

[2.5.1.1 Maintain General Data for Business Partner 9](#_Toc232850603)

[2.5.1.2 Maintain Payment Details for Business Partner 11](#_Toc232850604)

[2.5.1.3 Maintain Authorizations for Business Partner 13](#_Toc232850605)

[2.5.1.4 Maintain Reporting Data in Company Code for Business Partner 14](#_Toc232850606)

[2.5.1.5 Maintain Additional Business Partner Roles 16](#_Toc232850607)

[2.5.2 Correspondence 17](#_Toc232850608)

[2.5.2.1 Maintain Profile and BP Group Assignments to Internal Recipient 17](#_Toc232850609)

[2.5.2.2 Maintain Profile and BP Group Assignments to External Recipient 18](#_Toc232850610)

[2.5.3 Maintaining Credit Limit 20](#_Toc232850611)

[2.5.3.1 Maintain Limit with Limit Type Y01 20](#_Toc232850612)

[2.5.3.2 Maintain Limit with Limit Type Y07 21](#_Toc232850613)

[2.5.4 Maintain Trader and Trader Authorizations 23](#_Toc232850614)

[2.5.4.1 Define Traders 23](#_Toc232850615)

[2.5.4.2 Define User Data 24](#_Toc232850616)

[2.5.4.3 Maintain Trader Authorizations 24](#_Toc232850617)

[3 Overview Table 26](#_Toc232850618)

[4 Test Procedures 30](#_Toc232850619)

[4.1 Create Security Account 30](#_Toc232850620)

[4.2 Create Security Class 31](#_Toc232850621)

[4.2.1 Create Security Class for Money Market Fund 32](#_Toc232850622)

[4.2.2 Create Security Class for MMF Accrued + Accum. Dividend 34](#_Toc232850623)

[4.2.3 Create Security Class for MMF Accum. Dividend 36](#_Toc232850624)

[4.3 (1XN) Market Rates Management – Manually via Upload 38](#_Toc232850625)

[4.4 Generate Limit Utilizations 39](#_Toc232850626)

[4.5 Analyze Cash Position 40](#_Toc232850627)

[4.6 Analyze Liquidity Forecast 40](#_Toc232850628)

[4.7 Check Limit Utilization Report 40](#_Toc232850629)

[4.8 Create Fund Purchase Transaction 41](#_Toc232850630)

[4.8.1 Create Fund Purchase Transaction for Money Market Fund 41](#_Toc232850631)

[4.8.1.1 Create Fund Purchase Transaction for Money Market Fund with Known Quantity and Price 42](#_Toc232850632)

[4.8.1.1.1 Create Fund Purchase Order 42](#_Toc232850633)

[4.8.1.1.2 Execute Fund Purchase Order 43](#_Toc232850634)

[4.8.1.1.3 Waiver Fund Purchase Order 45](#_Toc232850635)

[4.8.1.1.4 Create Fund Purchase Contract 46](#_Toc232850636)

[4.8.1.2 Create Fund Purchase Transaction for Money Market Fund Priced Later (optional) 48](#_Toc232850637)

[4.8.2 Create Fund Purchase Transaction for MMF Accrued + Accum. Dividend 50](#_Toc232850638)

[4.8.3 Create Fund Purchase Transaction for MMF Accum. Dividend 51](#_Toc232850639)

[4.9 Correspondence 53](#_Toc232850640)

[4.9.1 Set Settlement Status (Manual) 53](#_Toc232850641)

[4.9.2 Correspondence with PDF Form 54](#_Toc232850642)

[4.9.2.1 Set Settlement Status 55](#_Toc232850643)

[4.9.2.2 Send Confirmation Email/Print 56](#_Toc232850644)

[4.9.2.3 Check Correspondence Status 56](#_Toc232850645)

[4.9.2.4 Receive Incoming Confirmation 58](#_Toc232850646)

[4.9.2.5 Find Deal and Match Deal Details 58](#_Toc232850647)

[4.10 Payment for Purchase 60](#_Toc232850648)

[4.10.1 Corporate Initiated Payment 60](#_Toc232850649)

[4.10.1.1 Option 1: Generate and Automatically Process Payment Request 61](#_Toc232850650)

[4.10.1.2 Option 2: Generate and Process Payment Request 64](#_Toc232850651)

[4.10.1.2.1 Generate Payment Request 64](#_Toc232850652)

[4.10.1.2.2 Process Payment Request 66](#_Toc232850653)

[4.10.1.3 Send Payment Medium File 68](#_Toc232850654)

[4.11 Bank Initiated Payment 69](#_Toc232850655)

[4.12 Post to General Ledger 69](#_Toc232850656)

[4.12.1 Fix Price (optional) 69](#_Toc232850657)

[4.12.2 Fix Price Settlement (optional) 71](#_Toc232850658)

[4.12.3 Post to General Ledger 72](#_Toc232850659)

[4.13 Recognize Dividend Distribution 74](#_Toc232850660)

[4.13.1 Enter Dividend Factor 74](#_Toc232850661)

[4.13.2 Update Planned Records for Securities 75](#_Toc232850662)

[4.13.3 Accrue Dividend 75](#_Toc232850663)

[4.14 Capitalize Dividend Distribution 77](#_Toc232850664)

[4.14.1 Capitalize Dividend Distribution for Money Market Fund 77](#_Toc232850665)

[4.14.2 Capitalize Dividend Distribution for MMF Accrued + Accum. Dividend 78](#_Toc232850666)

[4.14.3 Capitalize Dividend Distribution for MMF Accum. Dividend 80](#_Toc232850667)

[4.15 Period-end Closing 81](#_Toc232850668)

[4.15.1 Update Securities Price (optional) 82](#_Toc232850669)

[4.15.2 Perform Key Date Valuation 82](#_Toc232850670)

[4.16 Redeem Fund Instrument 84](#_Toc232850671)

[4.16.1 Review Funds Position 84](#_Toc232850672)

[4.16.2 Create Fund Redemption Transaction 85](#_Toc232850673)

[4.17 Set Settlement Status 86](#_Toc232850674)

[4.18 Payment from Sale 87](#_Toc232850675)

[4.18.1 Bank Initiated Payment 88](#_Toc232850676)

[4.18.2 Post to General Ledger 88](#_Toc232850677)

[4.19 Reports 90](#_Toc232850678)

[4.19.1 Display Treasury Posting Journal 90](#_Toc232850679)

[4.19.2 Treasury Position Analysis 91](#_Toc232850680)

[4.19.3 Display Treasury Position Values 92](#_Toc232850681)

[4.19.4 Define Financial Positions 93](#_Toc232850682)

[4.19.5 Financial Status - Book Value 95](#_Toc232850683)

[4.19.6 Financial Status - Nominal Amount 95](#_Toc232850684)

[4.19.7 Display Treasury Payments 96](#_Toc232850685)

[4.19.8 Display Treasury Position Flows 97](#_Toc232850686)

[4.19.9 Display Treasury Alerts - Posting 98](#_Toc232850687)

[4.19.10 Display Treasury Alerts- Settlement, Release and Payment 99](#_Toc232850688)

[4.19.11 Display Payment Schedules 100](#_Toc232850689)

[4.19.12 Display Securities Account Class Positions 101](#_Toc232850690)

[4.19.13 Analyze NPV 102](#_Toc232850691)

[4.19.14 Calculate Market Risk Key Figures 103](#_Toc232850692)

[4.19.15 Sensitivity Key Figures 104](#_Toc232850693)

[4.19.16 Review Limit Utilization Report 105](#_Toc232850694)

[5 Appendix 107](#_Toc232850695)

[5.1 Position Indicator 107](#_Toc232850696)

[5.1.1 Change Position Indicator 107](#_Toc232850697)

[5.2 Job Scheduling 108](#_Toc232850698)

[5.2.1 Generate Limit Utilizations 108](#_Toc232850699)

[5.2.2 Generate Payment Request 109](#_Toc232850700)

[5.2.3 Post Flows to General Ledger 111](#_Toc232850701)

[5.2.3.1 Template - Fix, Pay and Post Flows 111](#_Toc232850702)

[5.2.3.2 Template - Process Business Transactions 113](#_Toc232850703)

[5.2.4 Key Date Valuation 115](#_Toc232850704)

[5.2.5 Update Security Cash Flow 117](#_Toc232850705)

[5.2.6 Post Debit Position 119](#_Toc232850706)

[5.2.7 Calculate Market Risk Key Figures 120](#_Toc232850707)

[5.3 Output Management 122](#_Toc232850708)

[5.3.1 Output Parameter Determination 123](#_Toc232850709)

[5.3.2 Manage Output Items 125](#_Toc232850710)

[5.3.3 Maintain Print Queues 127](#_Toc232850711)

[5.3.4 Display Email Transmissions 127](#_Toc232850712)

[5.3.5 Maintain Email Template 128](#_Toc232850713)

[5.3.6 Maintain Form Template 130](#_Toc232850714)

[5.4 Reconciliation of External Securities Account Statements 131](#_Toc232850715)

[5.4.1 Create the Statements of External Securities Account 131](#_Toc232850716)

[5.4.2 Reconciliation of External Securities Account Statements 133](#_Toc232850717)

[5.5 Accounting 134](#_Toc232850718)

[5.5.1 Reverse Accrual 134](#_Toc232850719)

[5.5.2 Reverse Valuation 135](#_Toc232850720)

[5.5.3 Reverse Debit Position 137](#_Toc232850721)

[5.6 Market Risk Analyzer 138](#_Toc232850722)

[5.6.1 Manage Market Data Shift 138](#_Toc232850723)

[5.6.2 Maintain Scenarios 139](#_Toc232850724)

[5.6.3 Defining Report Layout for Calculate Market Risk Key Figures 140](#_Toc232850725)

[5.6.4 Manage Market Risk Key Figure Sets 143](#_Toc232850726)

[5.7 Credit Risk Analyzer 146](#_Toc232850727)

[5.7.1 Display Limit Overview 146](#_Toc232850728)

[5.8 Simulated Valuation 147](#_Toc232850729)

[5.8.1 Run Simulated Valuation 147](#_Toc232850730)

[5.8.2 Delete Simulated Valuation 149](#_Toc232850731)

[5.9 Rebate Reinvestment 150](#_Toc232850732)

[5.10 Security Account Transfer 152](#_Toc232850733)

## Purpose

Overview

The scope item helps you to better manage your Money Market Mutual Fund instruments.

The Money Market Mutual Funds (MMMF) are traditionally traded at a stable 1.00 Currency Unit. An SEC rule in the U.S. for investment companies requires the MMMFs to declare their Net Asset Value (NAV) to be floating on a daily basis. This scope item incorporates the processes to manage both traditional and floating NAV MMMFs.

The scope item covers the processes to create a securities class, and to purchase, bookkeep, and receive dividends of and sale of a money market mutual fund.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/2UN_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Treasury Specialist - Front Office | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |
| Treasury Specialist - Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE | Treasury Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE |  |
| Treasury Accountant | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |
| Treasury Risk Manager | SAP_BR_TREASURY_RISK_MANAGER | Treasury Analytics | SAP_BR_TREASURY_RISK_MANAGER |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Currency | AED |  |  |
| Business Partner | 33537001 |  |  |
| Valuation Area | AE 0 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| J60 - Accounts Payable | Define payment medium format following the steps described under Prerequisites > Preliminary Steps > Define Payment Medium Format Variants (Optional) in the test script of J60. |

### Preliminary Steps

#### Create Business Partner

##### Maintain General Data for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the general data for the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner screen, choose Organization. | The Create Organization: screen is displayed. |  |
| 4 | Enter Address Data | On the Create Organization screen, enter the following entries and choose Save:Business Partner: for example, 33537001Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Bank 1 - SAMPLE BANKSalutation: for example, Bank 1Search Term 1/2: for example, Bank 1Street/House number: for example,Postal Code/City: for example,Ctry/Reg.: AELanguage: ENE-Mail: for example, <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, Dec 31 of the year 9999Note Stay in the screen for subsequent steps. | The business partner is created successfully. |  |
| 5 | Switch to Change Mode | On the Display Organization33537001 screen, choose Switch Between Display and Change, and enter following data:Change in BP role: select TR0151 Counterparty | More counterparty related tabs such as Legal Data, Rating are displayed. |  |
| 6 | Enter Legal Data | On the Change Organization:33537001 screen, choose Legal Data in the dropdown list of Navigation Menu, enter the following data and choose Save:Country/Region: AENote Navigation Menu is on the very right side of the screen. It's displayed as  , which is right next to the symbol .Stay in the screen for subsequent steps. | The legal data is entered and saved.The Change Organization:33537001, role Counterparty screen is displayed. |  |
| 7 | Enter Payment Transaction Data | On the Change Organization:33537001 screen, choose Payment Transactions in the dropdown menu of Navigation Menu, and enter the following 2 rows of data:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, 18121976Bank Acct: for example, Bank accountIBAN: choose IBAN button and choose Continue in the popup IBAN screen.Row 2:ID: for example, USD1C/R: for example, AEBank Key: for example, 18121976Bank Acct: for example, Bank accountIBAN: choose IBAN button and choose Continue in the popup IBAN screen.Now choose Save.If the Information dialog box appears when you choose IBAN, please choose Continue. | The payment transaction data is entered and the business partner is saved. |  |

##### Maintain Payment Details for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the payment details of the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP. In the popup dialog box, enter the following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter the following data:Change in BP Role: TR0151 Counterparty(defined) | Change Organization: 33537001, new role Counterparty screen is displayed. |  |
| 4 | Enter SI: Payment Details data | On the Change Organization:33537001, role Counterparty) screen, choose Company Code, enter the following data and choose Enter:Company Code: for example, 3310Choose SI: Payment Details and enter the following four rows:Row 1:Currency: for example, AEDPay.Det.ID: for example, AEDIHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: <leave blank>Partner Bank: <leave blank>Payment Request: <deselect>Payment Methods: <leave blank>Row 2:Currency: for example, AEDPay.Det.ID: for example, AEDOHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, 33537001Partner Bank: for example, AED1Payment Request: <select>Payment Methods: TRow 3:Currency: USDPay.Det.ID: for example, USDIHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/ee: for example, <leave blank>Payment Request: <deselect>Payment Methods: <leave blank>Row 4:Currency: for example, USDPay.Det.ID: for example, USDOHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/Payee: for example, 33537001Partner Bank: for example, USD1Payment request: <select>Payment methods: FStay in this screen for subsequent steps.Note If the following message displays, choose No.Business partner proposed as payer/payee (see long text) Display this message for this business partner again? | The SI: Payment Details data is entered. |  |
| 5 | Assign Payment details | From the last screen of previous step,For AED,select the Checkbox for AEDAEDI. Choose Assign. In the Counterparty Change: Payment Details Assignment dialog box, choose Select All Incoming. Now AEDI is displayed under PmntID-Inc, choose Continue to close the dialog box.Select the checkbox for AEDAEDO. Choose Assign. In the Counterparty Change: Payment Details Assignment dialog box, choose Select All Outgoing. Now AEDO is displayed under P-ID Outg. Choose Continue to close the dialog box.Do the same for USD:USD I: PmntID-IncUSD O: P-ID Outg.On the Change Organization:33537001, role Counterparty screen, choose Save. | Payment details and the assignments are saved. |  |

##### Maintain Authorizations for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the authorization data of the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP. In the Open business partner dialog box, enter the following data, and choose Enter:Business Partner: 33537001Choose Switch Between Display and Change, and enter the following data:Change in BP Role: <select TR0151 Counterparty(defined)> | The Change Organization:33537001, role Counterparty screen is displayed. |  |
| 4 | Enter SI: Authorizations Data | On the Change Organization:33537001, role Counterparty screen, choose Company Code. On the SI: Authorizations tab, maintain the following data and choose Save:Securities: <select>Note You can also give authorization to a specific product type and transaction type. For testing purpose, we give authorizations to all transactions. | The authorizations are maintained. |  |

##### Maintain Reporting Data in Company Code for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the company relationship of the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP. In the Open Business Partner dialog box, enter the following data, and choose Enter:Business Partner: 33537001Choose Switch Between Display and Change, and enter the following data:Change in BP Role: choose TR0151 Counterparty (defined) | Change Organization: 33537001 , role Counterparty screen is displayed. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization:33537001, role Counterparty screen, choose Company Code. On the Reporting Data in Company Code tab, enter the following data and choose Save:Comp. Rel.: for example, 3 OtherNote You may need to choose the Reporting Data in Company Code tab in Navigation Menu.Comp.Rel. reflects your relationship with the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itIt is considered when deriving the G/L account. | The reporting data is entered and saved. |  |

##### Maintain Additional Business Partner Roles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain additional roles of the business partner required for securities transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP. In the Open business partner dialog box, enter the following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change. | Change Organization: 33537001 screen is displayed. |  |
| 4 | Add New Role of TR0150 Issuer | Change in BP Role: <select TR0150 Issuer>Choose Save. | Data is saved. |  |
| 5 | Add New Role of TR0152 Depository Bank | Change in BP Role to: for example, <select TR0152 Depository Bank>Choose Save. | Data is saved. |  |

#### Correspondence

Purpose

SAP TRM provides the standard correspondence functionality. With this correspondence functionality, whenever a TRM transaction is saved, SAP could either send an Email to the Business Partner, or automatically print out a form in Print machine.

To use this correspondence functionality, the following data needs to be assigned to Business Partner:

- Business Partner Profile
- Business Partner group

##### Maintain Profile and BP Group Assignments to Internal Recipient

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Recipient ID is predefined by SAP, and can be linked to SAP User ID(s). Once it's linked to an SAP user ID, whenever an internal correspondence object is generated, the system sends correspondence information to the address of the SAP User ID. Depending on the profiles (PR_EMAIL /PR_PRINT) maintained, email is sent to the user's email address or a form is print out.

In this step, you assign business partner profiles and BP groups to an internal business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Assign Profile and BP Group - Internal Recipients (FTR_INT_ASSIGN). | The Assignment of Profiles and BP Groups to Internal Recipients: screen is displayed. |  |
| 3 | Enter Business Partner Data on the View | On the left side of Assignment of Profiles and BP Groups to Internal Recipients screen, choose Insert Row, and enter the following data:IntRec: for example, INT.RECPCoCd: for example, 3310Recpt/Send Type: for example, INTERNALCheckbox: <select> | The business partner information is entered. |  |
| 4 | Assign Business profile and BP Group to the Business Partner | Select the INT.RECP row.On the upper right side of the Assignment of Profiles and BP Groups to Internal Recipients view, expend the node, and choose one item to maintain the business partner profile and business partner group, for example, Securities > Investment Fund > 02A Money Market Fund > 100 Purchase > 20 ContractThen on the bottom right side of the screen, choose Insert Row. Enter the following data, and choose Save:Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTUser Name: <select a User ID>.Choose Insert Row again and add another entry as follows and choose Save:Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTUser Name: <select a User ID>.Note The user ID is a backend user ID. | User ID with business partner profile and business partner group is assigned to the activity category level. |  |
| 5 | Repeat the previous step to assign BP profile and BP group to the rest of Product type/Transaction Type/Activity category | Select the item INT.RECP in the left side view, and choose Modify Row.Repeat the above step to maintain other items under the Securities > Investment Fund folder. | Other items are maintained fo rthe correspondence. |  |

##### Maintain Profile and BP Group Assignments to External Recipient

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you set up correspondence activities by maintaining Business Partner Profiles and Business Partner Groups.

SAP has predefined following business partner profiles:

- PR_EMAIL
- PR_PRINT

You can assign these predefined business partner profiles to your business partner. For example, if you communicate with your business partner via Email, you can assign PR_EMAIL to your business partner; if you communicate with your business partner via printed file, you can assign PR_PRINT to your business partner.

SAP has predefined following Business Partner Group:

- BPG_DEFAULT

You can assign this Business partner group to your Business Partner. You can also use SSCUIs Define Business Partner Group and Assign Attributes for Business Partner Groups to add your own Business partner group and assign appropriate attributes according to your specific requirement. Different business partner profiles and BP groups could be assigned to the same business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign Profile and BP Group - External Recipients (FTR_EXT_ASSIGN). | The Assignment of Profiles and BP Groups to External Recipients: view displays. |  |
| 3 | Enter Business partner data on the view | On the left side of Assignment of Profiles and BP Groups to External Recipients: view, choose Insert Row and enter the following data, and then select the business partner by ticking the checkbox before the business partner:BusPartner: for example, 33537001CoCd: for example, 3310Recpt/Send Type: for example, COUNTERPARTY | The Business Partner information is entered. |  |
| 4 | Assign Business profile and BP group to the Business Partner | On the top right side of the Assignment of Profiles and BP Groups to External Recipients screen, expand the node, and choose one item to maintain the business partner profile and business partner group, for example, Securities > Investment Fund > 02A Money Market Fund > 100 Purchase > 20 ContractThen on the bottom-right side of the screen, choose Insert Row and enter the following data:Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTChoose Insert Row again and add another entry as following data：Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTNote Normally you only assign one profile to a Product type/Transaction type/Activity Category. | Business partner profiles and BP groups are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat the previous step to assign BP profiles and BP groups to the rest of Product type/Transaction Type/Activity category | Select the item 33537001 in the left side view, and choose Modify Row.Repeat the above step to maintain other items under the Securities > >Investment Fund folder. | For all the listed Product Types/Transaction Types/ Activity Categories, BP profiles and BP groups are assigned. |  |

#### Maintaining Credit Limit

Purpose

A series of limit types have been created in system. You can maintain credit limit based on specific limit type according to business. In the following steps, you are going to maintain limit type Y01 and Y07.

##### Maintain Limit with Limit Type Y01

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
| 2 | Access the SAP Fiori app | Open Manage Limits (TBL1) | The Limits: Choose Limit Types view displays. |  |
| 3 | Choose Limit Type | On the The Limits: Choose Limit Types screen, select the row of Limit type Y01, then choose Create Limits, enter the following data in the Create Limits: Define Characteristics dialog and choose Continue:Company Code: for example, 3310 | The Edit Limits for Limit Type Y01: Create New Limit screen appears |  |
| 4 | Create Internal Limit Amount and External Limit Amount | On the Edit Limits for Limit Type Y01: Create New Limit screen, enter the following data and choose Save:Valid From Date: for example, Current DateValid To (Internal): for example, 12/31/9999Valid To (External): for example, <Current Date + 1 year>Limit Currency: for example, AEDInternal Limit Amnt: for example, 250,000,000External Limit Amnt: for example, 200,000,000Critical Limit Utilizat.: for example, 90Max. Risk Commit Per. Mth: for example, 999Limit: for example, Check | The Edit Limits for Limit Types: Overview screen displays |  |

##### Maintain Limit with Limit Type Y07

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Limits (TBL1). | The Limits: Choose Limit Types screen is displayed. |  |
| 3 | Choose Limit Type | On the Limits: Choose Limit Types screen, select the row of Limit type Y07, then choose Create Limits, enter the following data in the Create Limits: Define Characteristics dialog box and choose Continue:In the Characteristics area:Company Code: for example, 3310BusPartner: for example, 33537001 | The Edit Limits for Limit Type Y07: Create New Limit screen is displayed. |  |
| 4 | Create Internal Limit Amount and External Limit Amount | On the Edit Limits for Limit Type Y07: Create New Limit screen, enter the following data in the Limits area and choose Save:Valid From Date: <Current Date>Valid To (Internal): for example, 12/31/9999Valid To (External): for example, <Current Date + 1 year>Limit Currency: for example, AEDInternal Limit Amnt: for example, 250,000,000External Limit Amnt: for example, 200,000,000Critical Limit Utilizat.: for example, 90%Max. Risk Commit Per. Mth: for example, 999Limit: for example, Check | The Edit Limits for Limit Types: Overview screen is displayed. |  |

#### Maintain Trader and Trader Authorizations

##### Define Traders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Define traders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Define Traders (S_ALR_87009302). | The Determine Work Area: Entry dialog box is displayed. |  |
| 3 | Enter Work Area | In the Determine Work Area: Entry dialog box, enter the following data and choose Continue:Company Code: for example, 3310 | The Change View "Treasury: Traders": Overview screen is displayed. |  |
| 4 | Create a New Record | Select New Entries, enter the following data and choose Save:Trader: for example, TRADER02 | The Treasury: Traders is saved. The New Entries: Overview of Added Entries screen is displayed. |  |

##### Define User Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Map users with traders. This will provide a default trader when creating a new transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Define User Data (S_ALR_87007933). | The Change View "Treasury: User master data supplements": Overview screen is displayed |  |
| 3 | Create a New Record | Select New Entries, enter the following data and choose Save:User Name: for example, Your user nameTrader: for example, TRADER02 | The data is saved. |  |

##### Maintain Trader Authorizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Define authorization for traders.

Prerequisite

A trader must be defined before this step. Refer to Define Traders step for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Trader Authorizations (TBT1). | The Create/Change Trans. Authorization for Trader: Init. Screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter data and select Enter.Trader: TRADER02Company Code: for example, 3310 | The Create/Change Transaction Authorization for Traders screen is displayed. |  |
| 4 | Enter Authorization and Save | Select or unselect on the Authorization column and choose Save.Note Make sure to authorize TRADER02 for the Investment Certificate transactions under Securities. | The data is saved as indicated by a message. For example: Transaction authorizations for trader TRADER02 are being saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [(1XN) Market Rates Management – Manually via Upload](#unique_22) [page ] 38 | - |  | Maintain FX Spot rates |
| [Create Security Account](#unique_23) [page ] 30 | Treasury Specialist - Back Office | Manage Securities Accounts (TRS_SEC_ACC) | Security Account is created. |
| [Create Security Class for Money Market Fund](#unique_24) [page ] 32 | Treasury Specialist - Back Office | Manage Security Classes (F8717) | Security Class for Product Type 02A is created. |
| [Create Security Class for MMF Accrued + Accum. Dividend](#unique_25) [page ] 34 | Treasury Specialist - Back Office | Manage Security Classes (F8717) | Security Class for Product Type 02B is created. |
| [Create Security Class for MMF Accum. Dividend](#unique_26) [page ] 36 | Treasury Specialist - Back Office | Manage Security Classes (F8717) | Security Class for Product Type 02C is created. |
| [Generate Limit Utilizations](#unique_27) [page ] 39 | Treasury Specialist - Middle Office | End-of-Day Processing (KLNACHT) | Limit utilizations was determinate and updated. |
| [Analyze Cash Position](#unique_28) [page ] 40 | Cash Manager | Cash Flow Analyzer (F2332) | Cash manager check the cash position status, and make decisions of right financial instruments for short-term purpose based on analysis of cash position. |
| [Analyze Liquidity Forecast](#unique_29) [page ] 40 | Cash Manager | Cash Flow Analyzer (F2332) | The cash manager check the liquidity forecast regularly and make decisions regarding medium-term or long-term financial instruments. |
| [Check Limit Utilization Report](#unique_30) [page ] 40 | Treasury Specialist - Middle Office | Review Limit Utilizations (TBLB) | Limit utilization report displays. |
| [Create Fund Purchase Transaction for Money Market Fund](#unique_31) [page ] 41 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A purchase for a security class of the product type 02A is created. |
| [Create Fund Purchase Transaction for MMF Accrued + Accum. Dividend](#unique_32) [page ] 50 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A purchase for a security class of the product type 02B is created. |
| [Create Fund Purchase Transaction for MMF Accum. Dividend](#unique_33) [page ] 51 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A purchase for a security class of the product type 02C is created. |
| [Set Settlement Status (Manual)](#unique_34) [page ] 53 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The transaction is settled manually. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_35) [page ] 61 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_36) [page ] 64 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_37) [page ] 66 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_38) [page ] 69 | N/A | N/A |  |
| [Fix Price (optional)](#unique_39) [page ] 69 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The price of the transaction is fixed. |
| [Fix Price Settlement (optional)](#unique_40) [page ] 71 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The priced transaction is settled. |
| [Post to General Ledger](#unique_41) [page ] 72 | Treasury Accountant | Fix, Pay and Post Flows (TBB1) | The transaction is posted to the general ledger. |
| [Enter Dividend Factor](#unique_42) [page ] 74 | Treasury Specialist - Back Office | Enter Factor Values (TMDFACTORVAL) | This step is outside of SAP system |
| [Update Planned Records for Securities](#unique_43) [page ] 75 | Treasury Specialist - Back Office | Update Planned Records for Securities (FWUP) |  |
| [Accrue Dividend](#unique_44) [page ] 75 | Treasury Accountant | Run Accrual/Deferral (TPM44); Automatic Debit Position and Posting - Security Accounts (FWSO) |  |
| [Capitalize Dividend Distribution for Money Market Fund](#unique_45) [page ] 77 | Treasury Accountant | Execute Debit Position - Manual Debit Position (FWZE) |  |
| [Capitalize Dividend Distribution for MMF Accrued + Accum. Dividend](#unique_46) [page ] 78 | Treasury Accountant | Execute Debit Position - Manual Debit Position (FWZE) |  |
| [Capitalize Dividend Distribution for MMF Accum. Dividend](#unique_47) [page ] 80 | Treasury Accountant | Automatic Debit Position and Posting - Security Accounts (FWSO) |  |
| [Update Securities Price (optional)](#unique_48) [page ] 82 | Treasury Specialist - Back Office | Enter Securities Prices (FW17) | New security price is maintained. |
| [Perform Key Date Valuation](#unique_49) [page ] 82 | Treasury Accountant | Run Valuation (TPM1) | The screen Valuation Log displays, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. The accounting document has been created in local GAAP (valuation area AE0). |
| [Review Funds Position](#unique_50) [page ] 84 | Treasury Specialist - Front Office | Display Securities Account Class Positions (TPM40A) | The report displays with filtered data. |
| [Create Fund Redemption Transaction](#unique_51) [page ] 85 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A sale transaction is created. |
| [Set Settlement Status](#unique_52) [page ] 86 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The transaction is settled manually. |
| [Bank Initiated Payment](#unique_53) [page ] 88 | N/A | N/A | This step is outside of SAP system. |
| [Post to General Ledger](#unique_54) [page ] 88 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) | Cash flows related FI document is posted. |
| [Display Treasury Posting Journal](#unique_55) [page ] 90 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Treasury posting journal displays. |
| [Treasury Position Analysis](#unique_56) [page ] 91 | Treasury Accountant | Treasury Position Analysis | Treasury position analysis displays. |
| [Display Treasury Position Values](#unique_57) [page ] 92 | Treasury Accountant | Display Treasury Position Values (F1867) | Treasury position values display. |
| [Define Financial Positions](#unique_58) [page ] 93 | Treasury Risk Manager | Define Financial Positions (FTR_FP_DEF) | Financial Positions are defined. |
| [Financial Status - Book Value](#unique_59) [page ] 95 | Treasury Risk Manager | Financial Status (F2136) | The financial status on book values displays. |
| [Financial Status - Nominal Amount](#unique_60) [page ] 95 | Treasury Risk Manager | Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)) | The financial status on nominal amount displays. |
| [Display Treasury Payments](#unique_61) [page ] 96 | Treasury Specialist - Back Office | Display Treasury Payments (TPM20A) | Treasury Payment displays. |
| [Display Treasury Position Flows](#unique_62) [page ] 97 | Treasury Specialist - Back Office | Display Treasury Position Flows (F1754) | Treasury posting flows display. |
| [Display Treasury Alerts - Posting](#unique_63) [page ] 98 | Treasury Accountant | Display Treasury Alerts - Posting (F4984) | Treasury Alerts-Posting display. |
| [Display Treasury Alerts- Settlement, Release and Payment](#unique_64) [page ] 99 | Treasury Specialist - Back Office | Display Treasury Alerts - Settlement (F4979) | Treasury Alerts display. |
| [Display Payment Schedules](#unique_65) [page ] 100 | Treasury Accountant | Display Payment Schedules (TJ04) | Payment schedules displays. |
| [Display Securities Account Class Positions](#unique_66) [page ] 101 | Treasury Accountant | Display Securities Account Class Positions (TPM40A) | Display Securities Account Class Positions display |
| [Analyze NPV](#unique_67) [page ] 102 | Treasury Specialist - Middle Office | Analyze NPV (JBRX) | The NPV Result displays. |
| [Calculate Market Risk Key Figures](#unique_68) [page ] 103 | Treasury Specialist - Middle Office | Calculate Market Risk Key Figures (AISGENKF) | The single value analysis of assigned report layout displays. |
| [Sensitivity Key Figures](#unique_69) [page ] 104 | Treasury Specialist - Middle Office | Sensitivity Key Figures - Single Analysis (AISS) | The sensitivity key figures display. |
| [Review Limit Utilization Report](#unique_70) [page ] 105 | Treasury Specialist - Middle Office | Review Limit Utilizations (TBLB) | Limit utilizations display. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Create Security Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The money market funds, or more broadly, a security in general, is usually purchased and maintained by a broker such as a bank or a securities company. The transactions involve opening a security account with the broker. The broker maintains positions by each of the securities account. In the system, the securities positions are also maintained on an account level. This procedure details out the steps of creating a security account.

Prerequisite

A Business Partner with TR0152 Depository Bank is created with ID 33537001.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Securities Accounts (TRS_SEC_ACC). | The Choose Securities Account and Company Code screen is displayed. |  |
| 3 | Enter Account Identifier | Enter a new unique identifier for the new Securities Account, and choose Create.Company Code: for example, 3310Securities Account: for example, AE_MMFInfoChoose Create if a confirmation dialog pops up.if above account is already created, you can choose Display or Change to either view or edit the account. | A new account is created. |  |
| 4 | Enter General Data of the Account | Enter below data and move to next tabSecurities Account ID: for example, 33537001AE0Securities Account Type: for example, SAC Asset Securities Account |  |  |
| 5 | Enter Bank Data | Enter the following data and choose Save:Depository Bank: for example, 33537001External Securities Account ID: for example, 123XXXX567Line 1:Payment Currency: AEDHouse Bank: AEBK1Account ID: AEAC1Line 2:Payment Currency: USDHouse Bank: AEBK1Account ID: USDAC | The data is saved |  |

### Create Security Class

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You need to create a security class ID before creating any securities transaction.

Currently, securities class ID of the following three product types are supported in the system:

- 02A Money Market Fund: to recognize position and revenue based on the monthly distribution of dividends of the money market fund.
- 02B MMF Accrued + Accum. Dividend: to accrue dividend revenue on a daily basis, and accumulate and recognize the actual position change on a monthly basis.
- 02C MMF Accum. Dividend: to update the dividend daily, and accumulate and recognize the position change on a monthly basis.

#### Create Security Class for Money Market Fund

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.Security Class ID: for example, MMF_AE1Product Type: 02A Money Market Fund | The New Object screen displays with previously specified Class ID. |  |
| 4 | Enter Header | On the Header tab, enter the following data:Security Class Name: for example, Mny Mkt Fund #1Gen. Sec. Classification: for example, Money market fundPlease switch to the Basic Data tab. | The Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | Under the Basic Data tab, enter the following data and choose Save:In the Issue area,Issuer: for example, 33537001Nominal Value: for example, 1.00Issue Currency: for example, AEDIssue Price: for example, 1.00In the Fund area,Fund Type: for example, Money mkt fund (1)In the Additional Identification Number table, you can choose to enter some actual index values. |  |  |
| 6 | Switch to Conditions | Switch to the Conditions tab.Note You can maintain dividend reinvestment by pre-delivered transaction type for 02A as described in [Create Fund Purchase Transaction for Money Market Fund with Known Quantity and Price](#unique_73) [page ] 42. If you choose this option, you can skip the maintenance of Conditions and continue with step 9. |  |  |
| 7 | Enter Details of Conditions - Dividend Adj. | Choose Create in the table header of Condition Items.In the pop-up dialog New Object, enter the following data, then choose Continue:Condition Type: for example, 112(Dividend Adj.)Effective From: for example, <the current date>Make the following entries and choose Apply.On the Dates tab,Adjustment Date Update Rule: for example, 0 At start of periodReference Date of Rate Fixing Date: for example, 1 Period End |  |  |
| 8 | Enter Details of Conditions - Dividend | Choose Create in the table header of Condition Items.In the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 116 (Dividend)Effective From: for example, <the current date>On the Amounts tab, enter the following data:Factor Type: for example, SM_FACTOROn the Dates tab, enter the following data, and choose Apply.Calculation Date Frequency: for example, 1Calculation Date Frequency Unit: for example, (Months)Calculation Date: for example, <end date of current month>Due Date Update Rule: for example, (Regular)Due Date: for example, <end date of current month> |  |  |
| 9 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: SMMFCurrency Unit: for example, AED | Data is saved. |  |
| 10 | Repeat | Repeat Step 1 - 9 to create another two security classes for Money Market Fund.Security Class ID: for example, MMF_AE4 or MMF_AE5 |  |  |

#### Create Security Class for MMF Accrued + Accum. Dividend

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a security class ID and product type in the pop-up dialog​ New Object, then choose Continue.Security Class ID: for example, MMF_AE2Product Type: 02B MMF Accrued + Accum. Dividend | The New Object screen displays with previously specified Class ID. |  |
| 4 | Enter Header | On the Header tab, enter the following data:Security Class Name: for example, Mny Mkt Fund #2Gen. Sec. Classification: for example, Money market fundPlease switch to the Basic Data tab. | The Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | On the Basic Data tab, enter the following data:In the Issue area:Issuer: for example, 33537001Nominal Value: for example, 1.00Issue Currency: for example, AEDIssue Price: for example, 1.00In the Fund area:Fund Type: for example, 2 MMF-Float. NAV |  |  |
| 6 | Switch to Conditions | Switch to the Conditions tab. |  |  |
| 7 | Enter Details of Conditions - Accrued Divid. Adj. | Choose Create in the table header of Condition Items.In the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 113 (Accrued Divid.Adj.)Effective From: for example, <the current date>Make the following entries and choose Apply.On the Dates tab, enter the following data:Adjustment Date Update Rule: for example, RegularInterest Rate Adjustment Frequency: 1Interest Rate Adjustment Unit: 1(Calendar Days)Interest Rate Adjustment Date: for example, <current date>Fixing Date Update Rule: for example, 1 (Relative) |  |  |
| 8 | Enter Details of Conditions - Accrued Dividend | Choose Create in the table header of Condition Items.In the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 114 (Accrued Dividend)Effective From: for example, <the current date>On the Amounts tab, enter the following data:Factor Type: for example, SD_FACTOROn the Dates tab, enter the following data, and choose Apply.Calculation Date Frequency: for example, 1Calculation Date Frequency Unit: (Calendar Days)Calculation Date: for example, <the current date>, and select the Calculation Date Included indicator.Due Date Update Rule: for example, (Regular)Due Date Frequency: 1Due Date Frequency Unit: 1 (Calendar Days)Due Date: for example, <the current date> |  |  |
| 9 | Enter Details of Conditions - Accum. Dividend 1 | Choose Create in the table header of Condition Items.In the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 115 (Accum.Dividend 1)Effective From: for example, <the current date>On the Dates tab, enter the following data, and choose Apply:Calculation Date Frequency: for example, 1Calculation Date Frequency Unit: (Months)Calculation Date: for example, <the end date of the current month>, and select the Calculation Date Included indicator.Due Date Frequency: for example, 1Due Date Frequency Unit: (Month)Due Date: for example, <the end date of the current month> |  |  |
| 10 | Enter Exchanges | Switch to Exchanges tab, enter below data and choose Create:Exchange: SMMFCurrency Unit: for example, AED |  |  |

#### Create Security Class for MMF Accum. Dividend

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.Security Class ID: for example, MMF_AE3Product Type: 02C (MMF Accum. Dividend) | The New Object screen displays with previously specified ID Number. |  |
| 4 | Enter Header | On the Header tab, enter the following data:Security Class Name: for example, Mny Mkt Fund #3Gen. Sec. Classification: for example, Money market fundPlease switch to the Basic Data tab. | The Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | On the Basic Data tab, enter the following data:In the Issue area,Issuer: for example, 33537001Nominal Value: for example, 1.00Issue Currency: for example, AEDIssue Price: for example, 1.00In the Fund area,Fund Type: for example, 2 MMF-Float. NAV | A confirmation appears. Data is saved. |  |
| 6 | Switch to Conditions | Switch to the Conditions tab. |  |  |
| 7 | Enter Details of Conditions - Accrued Divid. Adj. | Choose Create in the table header of Condition Items.In the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 113 (Accrued Divid.Adj.)Effective From: for example, <the current date>Make the following entries and choose Apply.On the Dates tab, enter the following data:Adjustment Date Update Rule: for example, (At start of period)Fixing Date Update Rule: for example, 1 (Relative)Reference Date of Rate Fixing Date: for example, Period End (1) |  |  |
| 8 | Enter Details of Conditions - Accrued Dividend | Choose Create in the table header of Condition Items.In the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 114 (Accrued Dividend)Effective From: for example, <the current date>On the Amounts tab, enter the following data:Factor Type: for example, SD_FACTOROn the Dates tab, enter the following data, and choose Apply:Calculation Date Frequency: for example, 1Calculation Date Frequency Unit: (Calendar Days)Calculation Date: for example, <the current date>Due Date Update Rule: for example, (Regular)Due Date Frequency: 1Due Date Frequency Unit: 1 (Calendar Days)Due Date: for example, <the current date> | A confirmation appears. The Class has been saved. |  |
| 9 | Enter Details of Conditions - Accum. Dividend 2 | Choose Create in the table header of Condition Items.In the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 117 (Accum. Dividend)Effective From: for example, <the current date>Make the following entries and choose Apply.On the Dates tab, enter the following data, and choose Apply.Calculation Date Frequency: for example, 1Calculation Date Frequency Unit: (Months)Calculation Date: for example, <the end date of the current month>Due Date Frequency: 1Due Date Frequency Unit: (Months)Due Date: for example, <the end date of the current month> |  |  |
| 10 | Enter Exchanges | Switch to the Exchanges tab, enter below data and choose Create.Exchange: SMMFCurrency Unit: for example, AED |  |  |

### (1XN) Market Rates Management – Manually via Upload

Purpose

This step provides instructions on how to enter market data such as foreign currency exchange spot rates etc.

Money market funds are quoted usually in the local currency. When the corporate is purchasing a money market fund from an overseas market, it may need to translate foreign currency into local currency for valuation purpose. The foreign currency exchange spot rates will be used for this purpose.

Procedure

Please refer to the test script Market Rates Management – Manually via Upload (1XN) for detail instructions.

### Generate Limit Utilizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the End of the transaction day, the Treasury Specialist - Middle Office can process End-of-Day process, the system determines and updates limit utilizations based on the transactions and positions contained in the data pool.

|  |
| --- |
| Note You can also schedule background job for this step, please see job scheduling step in Appendix. |

Prerequisite

The market data has been imported.

If security exists, the spot price needs to be maintained for current date. Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open End-of-Day Processing (KLNACHT). | The End-of-Day Processing screen is displayed. |  |
| 3 | Enter Criteria of End-of-Day Processing | On the End-of-Day Processing screen, enter the following data and choose Execute:Valuation Date: <Current Date>Determination Procedure: 10 to 20Company code: for example, 3310 | You should get a message End-of-day processing was completed successfully. |  |

### Analyze Cash Position

Purpose

At the End of the transaction day, the Cash Manager will always check the cash position status, and make decisions of the right financial instruments for short-term purpose based on the analysis of cash position.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) app to analyze the cash position. For detailed information, please refer to the Basic Cash Operations test script.

### Analyze Liquidity Forecast

Purpose

The cash manager will check the liquidity forecast regularly and make decisions regarding medium-term or long-term financial instruments, such as, investment, loan, or foreign exchange.

Procedure

If cash management is implemented in your system, you can use app Cash Flow Analyzer (F2332) to analyze the liquidity forecast, for details please refer to the Basic Cash Operations(BFB) test script.

### Check Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to check Limit Utilization Report.

Prerequisite

The Limit master records of your company was maintained in the system, the step [Generate Limit Utilizations](#unique_27) [page ] 39 was processed already.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Overview of Utilizations - Selection Using all Characteristics screen, enter the following data and choose Execute:In the General Access Options area,Limit type: for example, Y01 or Y07In the Selection of Utilizations area,Limit Utilization Base: for example, 1Determination Date: for example, <Current Date>In the Selection of Limits area,Limits Valid From: for example, <Current Date> | The system displays an overview of the limit utilizations in accordance with your selection criteria.Note No utilizations selected -> see long text message is displayed while there is not any transaction created in system yet. |  |

### Create Fund Purchase Transaction

#### Create Fund Purchase Transaction for Money Market Fund

Purpose

When money market funds are traded with fixed amount and known quantity and price, please follow step [Create Fund Purchase Transaction for Money Market Fund with Known Quantity and Price](#unique_73) [page ] 42

When money market funds are traded via a clearing house (for example ICD portal), the payment amount is fixed and has directly to be paid before the quantity and price are known. The quantity and price are calculated later and provided by the counterparty. In this case, please follow the [Create Fund Purchase Transaction for Money Market Fund Priced Later (optional)](#unique_74) [page ] 48 step.

##### Create Fund Purchase Transaction for Money Market Fund with Known Quantity and Price

###### Create Fund Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you place an order of fund, you enter the purchase order information into the system.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

Please create two purchase orders via below steps.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Securities Transaction: Entry Screen screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Entry Screen, enter the following data and choose Enter:Company Code: for example, 3310ID Number: for example, MMF_AE4Transaction Type: 100Partner: for example, 33537001In the Activity area,Order/Fixing: <select> | The Create Securities Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:In the Position area,Securities Account: for example, AE_MMFIn the Amounts area,Amounts of Units: for example, 1MIn the Order Data area,Limit Date: for example, <the current date>Limit Price: for example, 1 AED | All data is entered. |  |
| 5 | Save the Transaction | Choose Save. |  |  |
| 6 | Repeat | Repeat step 1-5 with security class ID MMF_AE5 to create another order. | Financial transaction is saved. |  |

###### Execute Fund Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You decide to purchase fund with the created order. After the purchase, you enter the purchase contract information into the system.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.
- The relevant fund purchase order is created in the [Create Fund Purchase Order](#unique_75) [page ] 42 step.

Procedure

|  |
| --- |
| Note Please use first order created in the [Create Fund Purchase Order](#unique_75) [page ] 42 step to execute. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Data on Initial Screen | In the search term area, enter the following data and choose Go:Key Date: for example, TodayCompany Code: for example, 3310Transaction: <the order transaction number(s) of the first order created in the Create Fund Purchase Order step> | The fund purchase order transaction screen is displayed. |  |
| 4 | Execute the Purchase Order | In the Transaction area, select the transaction and choose Execute Order in the toolbar via button …. | The Process Financial Transaction screen is displayed. |  |
| 5 | Add Relevant Information and Save the Transaction | On the tab Structure, enter the following data:In the Position area,General Valuation Class: for example, choose an appropriate GeneralValuation Class (GVC), for example, 30 Cash equivalentsIf it is stable-NAV MMF, choose a GVC only with FX Valuation; If it is floating-NAV MMF, choose a GVC with FVTPL or FVOCI, because floating-NAV MMF needs to mark to latest floating NAV (security price), so it is evaluated at fair value through P/L or OCI from the accounting perspective.In the Amounts area,Price (Unit-Quoted): 1 AEDThen choose Save.Note If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a dialog box appears asking to Create Position Indicator.If the Position Indicator is already created, then you can ignore below step. The following message is displayed: Security transaction XXXXX created in company code YYYY |  |  |
| 6 | Create Position Indicator | Choose Create Automatically. | The fund purchase order is executed, the relevant fund purchase transaction is created. |  |

###### Waiver Fund Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You decide to waiver a fund purchase order. Once you cancel the order, you maintain the relevant information in the system.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.
- The relevant fund purchase order is created in the [Create Fund Purchase Order](#unique_75) [page ] 42 step and has not been executed.

Procedure

|  |
| --- |
| Note Please use second order created in the [Create Fund Purchase Order](#unique_75) [page ] 42 step to waiver a fund purchase order. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Data on Initial Screen | In the search term area, enter the following data and choose Go:Key Date: for example, TodayCompany Code: for example, 3310Transaction: <the transaction number(s) of the second order created in the Create Fund Purchase Order step> | The fund purchase order transaction is displayed. |  |
| 4 | Waiver the Fund Purchase Order | In the Transaction area, select the transaction and choose Order Expiry in the toolbar via button …. | The Process Financial Transaction screen is displayed. |  |
| 5 | Waiver the Fund Purchase Order | On the initial screen, choose Save. | The status of fund purchase order transaction is changed to Order Expiration. |  |

###### Create Fund Purchase Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After purchase transaction has concluded in the real world, an entry into the system is required to update the securities position. This section is about money market funds traded with fixed amount and known quantity and price.

If you don't maintain condition of security class, you can use transaction type 500 to update the position from dividend reinvestment or transaction type 600 to reverse the position from dividend reinvestment.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Securities Transaction: Entry Screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Entry Screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, MMF_AE1Transaction Type: 100Partner: for example, 33537001 | The Create Securities Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the Structure tab, enter the following data:In the Position area,Securities Account: for example, AE_MMFGeneral Valuation Class: choose an appropriate GeneralValuation Class (GVC), for example, 30 Cash equivalentsIf it is stable-NAV MMF, choose a GVC only with FX Valuation; If it is floating-NAV MMF, choose a GVC with FVTPL or FVOCI, because floating-NAV MMF needs to mark to latest floating NAV (security price), so it is evaluated at fair value through P/L or OCI from the accounting perspective.Position Value Date: for example, <Current Date>Calculation Date: for example, <Current Date>Payment Date: for example, <Current Date>In the Amounts area,Number of Units: for example, 1MPrice (Unit Quoted): for example, 1 | All data is entered. |  |
| 5 | Save the Transaction | Choose Save.If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a prompt asking to Create Position Indicator. Please follow below step if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |  |  |
| 6 | Create Position Indicator | Choose Create Automatically . | The transaction is created. |  |

##### Create Fund Purchase Transaction for Money Market Fund Priced Later (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After purchase transaction has concluded in the real world, an entry into the system is required to update the securities position.

The section covers the case when payment amount is fix and has directly to be paid before the quantity and price are known. The quantity and price are calculated later and provided by counterparty.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, MMF_AE1Transaction Type: 101Partner: for example, 33537001 | The Create Investment Fund: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the Structure tab, enter the following data:In the Payment area,Payment Amount: for example, 1MAEDIn the Position area,Securities Account: for example, AE_MMFGeneral Valuation Class: choose an appropriate GeneralValuation Class (GVC), for example, 30 Cash equivalentsIf it is stable-NAV MMF, choose a GVC only with FX Valuation; If it is floating-NAV MMF, choose a GVC with FVTPL or FVOCI, because floating-NAV MMF needs to mark to latest floating NAV (security price), so it is evaluated at fair value through P/L or OCI from the accounting perspective.Position Value Date: for example, <Current Date>Calculation Date: for example, <Current Date>In the Amounts area,Price (Unit Quoted): for example, 1 | All data is entered. |  |
| 5 | Save the Transaction | Choose Save.If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a prompt asking to Create Position Indicator. Please follow below step if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |  |  |
| 6 | Create Position Indicator | Choose Create Automatically . | The transaction is created. |  |

#### Create Fund Purchase Transaction for MMF Accrued + Accum. Dividend

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After purchase transaction has concluded in the real world, an entry into the system is required to update the securities position.

|  |
| --- |
| Note For MMF with Accrued and Accumulated Dividend, we also support the option when payment amount is fixed and has directly to be paid before the quantity and price are known. The transaction type is 101. You can refer to [Create Fund Purchase Transaction for Money Market Fund Priced Later (optional)](#unique_74) [page ] 48 to cover the case when payment amount is fixed and has directly to be paid before the quantity and price are known. |

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, MMF_AE2Transaction Type: 100Partner: for example, 33537001 | The Create Investment Fund: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:In the Position area,Securities Account: for example, AE_MMFGeneral Valuation Class: for example, 23 Short term investment (current asset): Fair value throu. P/LNote If it is stable-NAV MMF, choose a GVC only with FX Valuation; If it is floating-NAV MMF, choose a GVC with FVTPL or FVOCI, because floating-NAV MMF needs to mark to latest floating NAV (security price), so it is evaluated at fair value thru P/L or OCI from accounting perspective.Position Value Date: for example, <Current Date>Calculation Date: for example, <Current Date - 1>Payment Date: for example, <Current Date>Number of Units: for example, 1MPrice (Unit Quoted): for example, 1 | All data are entered. |  |
| 5 | Save the Transaction | Choose Save.If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a prompt asking to Create Position Indicator. Please follow below step if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |  |  |
| 6 | Create Position Indicator | Choose Create Automatically | The transaction is created. |  |

#### Create Fund Purchase Transaction for MMF Accum. Dividend

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After purchase transaction has concluded in the real world, an entry into the system is required to update the securities position.

|  |
| --- |
| Note For MMF with Accumulated Dividend, we also support the option when payment amount is fixed and has directly to be paid before the quantity and price are known. The transaction type is 101. You can refer to [Create Fund Purchase Transaction for Money Market Fund Priced Later (optional)](#unique_74) [page ] 48 to cover the case when payment amount is fixed and has directly to be paid before the quantity and price are known. |

Prerequisite

The relevant Securities ID is created.

The relevant Securities Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, MMF_AE3Transaction Type: 100Partner: for example, 33537001 | The Create Investment Fund: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the Structure tab, enter the following data:In the Position area,Securities Account: for example, AE_MMFGeneral Valuation Class: for example, 23 Short term investment (current asset): Fair value throu. P/L.Note If it is stable-NAV MMF, choose a GVC only with FX Valuation; If it is floating-NAV MMF, choose a GVC with FVTPL or FVOCI, because floating-NAV MMF needs to mark to latest floating NAV (security price), so it is evaluated at fair value thru P/L or OCI from accounting perspective.Position Value Date: for example, <Current Date>Calculation Date: for example, <Current Date - 1>Payment Date: for example, <Current Date>In the Amount area,Number of Units: for example, 1MPrice (Un. Quot): for example, 1 | All data are entered. |  |
| 5 | Save the Transaction | Choose Save.If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a prompt asking to Create Position Indicator. Please follow below step if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |  |  |
| 6 | Create Position Indicator | Choose Create Automatically | The transaction is created. |  |

### Correspondence

Purpose

TRM transaction related information is transferred between you and your Business Partner. SAP Treasury and Risk Management (SAP TRM) provides standard correspondence functionalities with which you can communicate with Business Partner with a printout form via email.

This section describes the standard correspondence functionality that SAP TRM provides.

#### Set Settlement Status (Manual)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a Securities transaction is recorded and saved in SAP, the transaction must be settled before you perform further activities. This section describes how to set the settlement status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Securities Transactions - Collective Processing (TS00) | The Securities: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Securities: Collective Processing screen, enter the following data and choose Execute:In the General Selections area,Company Code: for example, 3310Transaction: the transaction number(s) | The list of transaction(s) is displayed on Securities: Collective Processing screen. |  |
| 4 | Settle the Transaction | Select the checkbox of a transaction on Securities: Collective Processing screen, and choose Settle.Note Please make sure to settle all the relevant transactions. | The Investment Fund: Structure screen is displayed. |  |
| 5 | Save the Change | On the Investment Fund: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If dialog Document lines: Display messages displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

#### Correspondence with PDF Form

Purpose

Email/Print are all PDF form-related output. By default, SAP provides business profiles for several PDF forms (for example, PR_PRINT and PR_EMAIL).

- For any Business Partner assigned to profile PR_PRINT, when a financial transaction is created, a PDF form is sent to a predefined print queue. To view and print the PDF file, use the SAP Fiori app Maintain Print Queues (F1260). Once you check and confirm that the transaction information on the form is correct, you may then send the paper copy of the form to the Business Partner.
- For any Business Partner assigned profile PR_EMAIL, when a transaction is created, SAP automatically sends emails to the Business Partner.

Once you receive the counterparty confirmation about the transaction from your Business Partner, you can settle all the correspondence objects of the transaction. Once all the correspondence objects are settled, the transaction status changes to Contract Settlement status.

|  |
| --- |
| NoteYou can use the following apps to maintain your own settings for output:Output Parameter DeterminationYou maintain your own rules for the output. For example, you can maintain email addresses of recipients. This rule overwrites the email address of the Business Partner for an external counterparty, or it overwrites the email address of User IDs for an internal counterparty.Maintain Email Templates - Deprecated (F1306). You maintain your own email template with this app.Maintain Form Templates (F1434). You maintain your own form template with this app.In this step, you settle the TRM transaction via the correspondence processing automatically. |

Prerequisites

You've created a TRM transaction which has not been settled.

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the previous procedure, all of the correspondence objects of the transaction were matched successfully. As standard functionality, the transaction is settled automatically.

In this activity, you verify that the transaction has been settled automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor view displays. |  |
| 3 | Enter Selection Criteria | On the Correspondence Monitor view, enter following data, and choose Execute:In the Correspondence area,Company Code: for example, 3310On the Financial transaction tab,Company Code: for example, 3310Transaction number: for example, <Transaction Number> | The Correspondence monitor - Standard View view displays. |  |
| 4 | Display Transaction History | On the Correspondence monitor - Standard View screen, select the checkbox of the incoming correspondence object, choose Show Underlying and the details of transaction view displays. | Activity 2 Contract Settlement displays in the second line. |  |

##### Send Confirmation Email/Print

Purpose

SAP provides the BP_DEFAULT business partner group. By default, if any business partner is assigned to this group, correspondence objects will be sent automatically when a financial transaction is saved. As described in the preliminary steps, 33537001 is assigned to BP_GROUP, so the correspondence objects have been sent automatically. If you create a new business partner group and don't assign the auto-send attribute, you can send correspondence objects manually using the Send Correspondence (FTR_COSEND) app.

Procedure

This step doesn’t require any operation in system.

##### Check Correspondence Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you verify the status of the correspondence objects for a transaction.

|  |
| --- |
| Note For zero/low cost collar FX option (cylinder FX option), please check the status for both legs. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor screen is displayed. |  |
| 3 | Enter Selection Criteria on the Initial Screen | Make the following entries and choose Execute:Correspondence tab:Company Code: for example, 3310In the Financial Transaction subarea,Company Code: for example, 3310Deal Number: for example, <Transaction Number> | The Correspondence monitor - Standard View screen is displayed. |  |
| 4 | Check the Correspondence Status | All correspondence objects are displayed.Note One financial transaction can have one or more correspondence objects depending on the BP profiles and BP groups assignment.In the status column:If the channel is Email, Delivered status, the system sent an email to the email address maintained in the business partner master data. However, this email address could also be overwritten if you maintained an Email Recipient rule with the Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN) app. Use the Monitor Email Transmissions (F5442) app to verify the actual email status.If the channel is Print, the form is sent to the print queue. You can also print out the form with the Maintain Print Queues (F1260) app.Maintain your own email template with the Maintain Email Templates - Deprecated (F1306) app.Maintain your own form template with the Maintain Form Templates (F1434) app. | Correspondence objects are in Delivered status. |  |
| 5 | Display the Transaction Details | Select the checkbox for COUNTERPARTY EMAIL and choose Show Underlying.Verify the following values:Recpt/Send Type: COUNTERPARTYChannel: EMAILChoose Back. | The transaction details are displayed.The Correspondence monitor - Standard View screen is displayed. |  |
| 6 | Display the Form of the Correspondence Object | Select the checkbox for the line with the following data, then choose View Message:Recpt/Send Type: COUNTERPARTYChannel: EMAILA dialog box displays the form of the correspondence object. Choose Continue. | The form of the correspondence object displays. |  |

##### Receive Incoming Confirmation

Purpose

In previous step, for the email channel, an outbound email is sent to the Business Partner. Normally, you will receive a counterparty confirmation from the Business Partner via email, phone, etc. This step is outside of SAP,

Procedure

This step doesn’t require any operation in the system.

##### Find Deal and Match Deal Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You have received counterparty confirmation in the previous procedure. In this procedure, you create an inbound correspondence object and match it with all the outgoing correspondence objects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor view displays. |  |
| 3 | Enter Selection Criteria on the Initial View | Enter the following data and choose Execute:Correspondence group:Company Code: for example, 3310Financial Transaction group:Company Code: for example, 3310Transaction Number: for example, <Transaction Number>Note Make a note of the correspondence key for a COUNTERPARTY correspondence object. | Please note down the correspondence key numbers for COUNTERPARTY PRINT and COUNTERPARTY EMAIL. |  |
| 4 | Create | Choose Create. | The Options for Creating Correspondence Objects view displays. |  |
| 5 | Create an Incoming Correspondence Object Referring to the Outgoing Correspondence Object | Enter the following data for groups and press Enter:Display Options group:Corresp. Category: 01 Transaction ActivitiesTransaction Details group:Company Code: for example, 3310Product Type: for example, <Product type you entered in the transaction>Incoming/Outgoing: I IncomingEntry Options: 05 Correspondence object as templateTemplate for Correspondence Object Data group:Correspondence Key: for example, <Enter the correspondence key number for COUNTERPARTY PRINT from the previous step> |  |  |
| 6 | Save | Choose Save.Note If the Automatic matching proposal view displays, choose Cancel. | The incoming correspondence object is created successfully and displayed on Correspondence monitor - Standard View view. |  |
| 7 | Match the Incoming Correspondence Object with the Outgoing Correspondence Objects for channel PRINT | Select the checkbox for the incoming correspondence object and choose Status Functions > Automatic Match. | The Automatic matching proposal view displays. |  |
| 8 | Outgoing Correspondence | On the left-side of the view, expand the incoming correspondence key. All outgoing correspondence objects of the transaction are displayed.Select all the checkboxes of the outgoing correspondence objects and choose Enter. | All the outgoing COUNTERPARTY PRINT correspondence objects of the transaction now have status completed.All the INTERNAL outgoing correspondence objects remain in Delivered status. |  |
| 9 | Match the Incoming Correspondence Object with the Outgoing Correspondence Objects for channel EMAIL | Repeat the above steps to create an incoming correspondence object for COUNTERPARTY EMAIL and match it with outgoing correspondence for channel EMAIL. |  |  |

### Payment for Purchase

#### Corporate Initiated Payment

Purpose

In this step, you process the payment flows of the transaction. You have two options:

1. Process the payment with the ‘Auto. Payment Run’ function.
2. Process the payment without the ‘Auto. Payment Run’ function.

Prerequisites

You have settled the transaction.

##### Option 1: Generate and Automatically Process Payment Request

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

##### Option 2: Generate and Process Payment Request

###### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows which require payment requests. It will not create posting in financial accounting.

In the case that the payment is initiated by the financial partner, skip the current step and the next step Process Payment Request, and continue with the step Bank Initiated Payment.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>Test Run: <select>Pay Only: <select this indicator>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Payment Log - Test Run displays, you can check the payment information on this screen. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Payment Log displays, payment request has been generated, make a note of the key number displayed on this screen. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | The Payment Log - Test Run view displays. Review the payment information on this view. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, enter the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. A payment request is generated.Make a note of the key number: __________ |  |

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
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters screen, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 3 days>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free selection for payment run, enter the following data and choose Save:Key number: <the key number you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>If information Log created for all accounts displays, choose Continue.Choose Save on screen Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat, and choose Schedule Job to confirm this dialog box.Message Proposal is running is displayed in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests screen, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media screen, enter the following data and choose Run:Run Date: for example, <current date>Identification: for example, TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

##### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by bank, it is not necessary to run previous steps Generate Payment Request and Process Payment Request, because the outgoing payment is initiated by bank.

Procedure

This step doesn‘t require any operation in system.

### Post to General Ledger

#### Fix Price (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section is only relevant with the case that the payment amount is fixed and has directly to be paid before the quantity and price are known.

Once the quantity and price are calculated and provided by the counterparty, you need to fix the price of the transaction before you perform further activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Securities Transactions - Collective Processing (TS00) | The Securities: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Securities: Collective Processing screen, enter the following data and choose Execute:In the General Selections area,Company Code: for example, 3310Transaction: the transaction number(s) | The list of transaction(s) is displayed on Securities: Collective Processing screen. |  |
| 4 | Settle the Transaction | Select the checkbox of a transaction on Securities: Collective Processing screen, and choose Fixing.Note Please choose the transaction you created in the section [Create Fund Purchase Transaction for Money Market Fund Priced Later (optional)](#unique_74) [page ] 48 and settled. | The Settle Security Contract: Structure screen displays. |  |
| 5 | Enter Data on Tab Structure | On the Structure tab, enter the following data:In the Position area,Position Value Date: for example, <2 days after Current Date>Calculation Date: for example, <2 days after Current Date>In the Amounts area,Number of Units: for example, 999,900.01Price (Unit Quoted): for example, 1.0001 | All data is entered. |  |
| 6 | Save the Change | Choose Save. | The transaction is Contract Priced. |  |

#### Fix Price Settlement (optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section is only relevant the case the payment amount is fixed and has directly to be paid before the quantity and price are known. The quantity and price are calculated later and provided by the counterparty.

Once a securities transaction is recorded and saved, the transaction must be settled before you perform further activities. In this step, you settle a transaction after its price is fixed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Securities Transactions - Collective Processing (TS00) | The Securities: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Securities: Collective Processing screen, enter the following data and choose Execute:In the General Selections area,Company Code: for example, 3310Transaction: the transaction number(s) | The list of transaction(s) is displayed on Securities: Collective Processing screen. |  |
| 4 | Settle the Transaction | Select the checkbox of a transaction on the Securities: Collective Processing screen, and choose Settle.Note Please make sure to settle all the relevant transactions. | The Settle Security Contract: Structure screen is displayed. |  |
| 5 | Save the Change | On the Settle Security Contract: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If the Document lines: Display message displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

#### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps are available for posting flows:

- Fix, Pay and Post Flows (TBB1): you use this app to generate the posting for incoming payment. Please note that when using this app in the current step, it will not create posting for outgoing payment which has been processed in previous step Generate Payment Request with the Pay Only option.
- Process Business Transactions (TPM10): You use this app to generate the posting for outgoing payment which has been processed in previous step Generate Payment Request with the Pay Only option.

|  |
| --- |
| Note You can also schedule a background job for this step, please see corresponding step in Appendix. |

Prerequisite

The outgoing payment which should be handled via payment request (if any) for this transaction has been processed in the previous step Generate Payment Request with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Securities: <select this checkbox>Company code: for example 3310Sec. Class ID Number: <transaction number with inflow which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | Screen Posting Log: Posted Business Transactions is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria, you can skip the current test step and continue the test step with the Process Business Transactionsapp. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Execute:Test Run: <deselect this checkbox> | Screen Posting Log: Posted Business Transactions is displayed, and the accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Fix, Post or Reverse Transactions screen is displayed. |  |
| 6 | Enter Selection Criteria for Test Run | On the Fix, Post or Reverse Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <unselect this checkbox>Company code: for example, 3310Valuation Area: for example AE0Limit by Transaction Number: <select this checkbox>Transaction: <The Security ID you entered in previous step>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If message You have not selected any business transactions is displayed, that means there is no posting needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Test Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Fix, Post or Reverse Transactions screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 9 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Update Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, and the accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |  |

### Recognize Dividend Distribution

Purpose

- It is common for Money Market Funds to declare their earned profit at a frequency that is different than actually distributing them. For example, a Money Market Fund can declare their profit on a daily basis at their website, but make such distribution at a monthly basis, usually at the last business day of a month.
- The declaration does not change the Net Asset Value (NAV, the unit price of the fund) or units held, whereas, the actual distribution usually takes the form of increased units held by an account.
- Some companies would recognize the profit as soon as they see the declaration depending on their accounting policy. A user can achieve frequent accrual of dividend by entering and accounting for the daily factor, and capitalize the factor at end of a month. We provide separate processes for the accrual and capitalize of the dividend to achieve such a flexibility.
- The user has to run dividend accrual at least once before capitalizing it.

#### Enter Dividend Factor

Purpose

This step provides instructions on how to enter a dividend factor.

Procedure

Follow the instructions in the Enter Securities Factor Values step of Market Rates Management – Manually via Upload(1XN) test script.

#### Update Planned Records for Securities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step provides instructions on how to update planned records for securities.

Prerequisite

The dividend factors are already entered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2. | Access the SAP Fiori app | Open Update Planned Records for Securities (FWUP). | The Securities: Update Planned Records screen is displayed. |  |
| 3. | Enter Selection Criteria | On the Securities: Update Planned Records screen, enter the following data and choose Execute:Company Code: for example, 3310Security ID: for example, MMF_AE2 | Update was completed successfully. |  |

#### Accrue Dividend

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step provides instructions on how to accrue profit distribution based on the dividend factors.

This step is only applicable for Product type 02B: MMF Accrued + Accum. Dividend

|  |
| --- |
| Note You can also schedule a background job for Automatic Debit Position. For more information, see the corresponding step in the Appendix |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Debit Position and Posting - Security Accounts (FWSO) | The Securities: Automatic Debit Position screen is displayed. |  |
| 3 | Enter Parameters and Test Run | On the Securities: Automatic Debit Position Screen, enter the following data and choose Execute:Company Code: for example, 3310Product Type: for example, 02BSec. Class ID Number: for example, MMF_AE2Security Account: for example, AE_MMFUpdate Type: for example, SAM5020Up to an Including Pos. Date: for example, <end date of current month>Document Date: for example, <end date of current month>Test Run: for example, <select> | A list of messages indicating the flow has been fixed. |  |
| 4 | Production Run | Confirm the messages and go back to previous screen, enter the following data and choose ExecuteTest Run: for example, <deselect> | A list of messages indicating the flow has been fixed. |  |
| 5 | Access the SAP Fiori app | Open Run Accrual/Deferral (TPM44). | The Execute Accrual/Deferral of Expenses and Revenues screen is displayed. |  |
| 6 | Enter Selection Criteria and Test Run | On the Execute Accrual/Deferral of Expenses and Revenues screen, enter the following data and choose Execute:Securities: <Select>OTC Transactions: <unselect>Company Code: 3310Valuation Area: AE0Sec. Class ID Number: for example, MMF_AE2Security Account: for example, AE_MMFAccrual / Deferral Key Date: for example, <end date of current month> | A list of accrual details displays. |  |
| 7 | Production Run | After confirming the accrual details, go back to previous screen, enter the following data and choose Execute:Test Run: for example, <unselect> | A list of accrual details is displayed.You can click on the Logs and Messages for further details. |  |

### Capitalize Dividend Distribution

#### Capitalize Dividend Distribution for Money Market Fund

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step provides instructions on how to capitalize the dividend to increase the units held.

Prerequisite

This section is relevant for the dividend to be capitalized without accrual. The latest (monthly) dividend factor has been entered or updated, and the Update Planned Records for Securities app has been executed to update the amount.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Execute Debit Position - Manual Debit Position (FWZE). | The Manual Debit Position: Initial Screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, MMF_AE1Security Account: for example, AE_MMF | A list of positions is displayed. |  |
| 4 | Select a Flow and Proceed | On the list of positions that displayed on the Manual Debit Position: Initial screen, select the top flow that you would like to capitalize and choose Post business transaction: | Manual Debit Position screen is displayed. |  |
| 5 | Enter Details for the Capitalization | On the Manual Debit Position screen, select the record to be capitalized, and choose Capitalize:Capitalize popup window is displayed.Enter below data and choose Copy:Amount to be capitalized: for example, the total amount of the dividend for the month.Units to be received: for example, the units that equal to the total amount of the dividend for the month. | 2 new flows are created in the Flows tab. |  |
| 6 | Post | Confirm the data and choose Post. | The Posting Log: Posted Business Transaction screen is displayed. |  |

#### Capitalize Dividend Distribution for MMF Accrued + Accum. Dividend

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step provides instructions on how to capitalize the accrued dividend to increase the units held.

Prerequisite

You have accrued the profit dividend.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Execute Debit Position - Manual Debit Position (FWZE) | The Manual Debit Position: Initial screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, MMF_AE2Security Account: for example, AE_MMF | A list of positions is displayed. |  |
| 4 | Select a Flow and Proceed | On the list of positions that displayed on the Manual Debit Position: Initial Screen, select the top flow with update type SAM5021 that you would like to capitalize and choose Post business transaction: | Manual Debit Position screen is displayed. |  |
| 5 | Enter Details for the Capitalization | On the Manual Debit Position screen, select the record to be capitalized, and choose Capitalize:The Capitalize popup window is displayed.Enter below data and choose Copy:Amount to be capitalized: for example, the total amount of the dividend for the month.Units to be received: for example, the units that equal to the total amount of the dividend for the month. | 2 new flows are created in the Flows tab. |  |
| 6 | Post | Confirm the data and choose Post. | Posting Log: Posted Business Transaction screen is displayed. |  |

#### Capitalize Dividend Distribution for MMF Accum. Dividend

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step provides instructions on how to capitalize the dividend to increase the units held. This section is relevant for the dividend with daily declaration but to be capitalized without accrual.

|  |
| --- |
| Note You can also schedule a background job for Automatic Debit Position. For more information, see the corresponding step in the Appendix. |

Prerequisite

The daily dividend factor has been entered or updated, and the Update Planned Records for Securities app has been executed to update the amount.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Debit Position and Posting - Security Accounts (FWSO) | The Securities: Automatic Debit Position screen is displayed. |  |
| 3 | Enter Parameters and Test Run | On the Securities: Automatic Debit Position screen, enter the following data and choose Execute:Company Code: for example, 3310Product Type: for example, 02CSec. Class ID Number: for example, MMF_AE3Security Account: for example, AE_MMFUpdate Type: for example, SAM5020Up to an Including Pos. Date: for example, <end date of current month>Document Date: for example, <end date of current month>Test Run: for example, <select> | A list of messages indicating the flow were fixed. |  |
| 4 | Production Run | Confirm the messages and go back to previous screen, enter the following data and choose ExecuteTest Run: for example, <deselect> | A list of messages indicating the flow were fixed. |  |
| 5 | Access the SAP Fiori app | Open Execute Debit Position - Manual Debit Position (FWZE) | The Manual Debit Position: Initial screen is displayed. |  |
| 6 | Enter Parameters | On the Manual Debit Position: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, MMF_AE3Security Account: for example, AE_MMF | A list of positions is displayed. |  |
| 7 | Select a Flow and Proceed | On the list of positions that displayed on the Manual Debit Position: Initial screen, select the top flow with update type SAM5031 that you would like to capitalize and choose Post business transaction: | The Manual Debit Position screen is displayed. |  |
| 8 | Enter Details for the Capitalization | On the Manual Debit Position screen, select the record to be capitalized, and choose Capitalize:The Capitalize popup window is displayed.Enter below data and choose Copy:Amount to be capitalized: for example, <the total amount of the dividend for the month>Units to be received: for example, <the units that equal to the total amount of the dividend for the month> | 2 new flows are created in the Flows tab. |  |
| 9 | Post | Confirm the data and choose Post. | The Posting Log: Posted Business Transaction screen is displayed. |  |

### Period-end Closing

Purpose

This step is required if you have not done so for a Floating Net Asset Value type of Money Market Fund.

- Update Securities Price.

The unit price does not change for the money market funds for the ones that employ Fixed Nat Asset Value, and hence above step is not required.

This section describes activities for period-end closing (usually executed at month end), including:

- Perform Key Date Valuation

#### Update Securities Price (optional)

Purpose

A certain class of Money Market Funds in the US market is required to disclose its floating Net Asset Value (NAV) using four decimal significant figures, for example, USD 1.0002 per unit. The Money Market Funds at other markets are usually quoted at a stable NAV at 1.00 currency unit.

By entering the latest floating NAV of a MMF into SAP system as securities price, the system can recognize its latest position value and perform the relevant journal posting when running key date valuation. The Stable NAV MMFs may not require this step to enter the latest securities price.

Procedure

Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

#### Perform Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to value the positions of securities based on Floating Net Asset Value, as well as to reflect the latest foreign currency exchange rate for the investments other than the company reporting currency.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Prerequisite

You have entered the spot price for the security ID in the Update Securities Price section (optional).

You have performed following sections of this test script for floating NAV MMF, for example, 02B and 02C:

- Set Settlement Status
- Payment to Depository Bank
- Recognize Dividend Distribution
- Capitalize Dividend Distribution

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Run Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run Valuation screen, enter the following data and choose Execute:In the Product Groups area,Securities: <select this checkbox>In the General Selections area,Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example, 02BIn the Securities area,Sec. Class ID Number: for example, MMF_AE2Security Account: for example, AE_MMFIn the Valuation Parameters area,Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation with ResetNote When the Period End is also the Year End, the Valuation Category Year End Valuation should be used.Test Run: <select this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Please note there is no posting created because it is test run.Note Sometime there is no simulated posting because your selected security class position in security account may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the Run Valuation screen is displayed.On the Run Valuation screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation. | The Valuation Log screen is displayed, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Then, the accounting document has been created in local GAAP (valuation area AE0). |  |

### Redeem Fund Instrument

#### Review Funds Position

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the position of the security class in the security account before redemption.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Securities Account Class Positions (TPM40A). | The Display Securities Account Class Position List screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Securities Account Class Position List screen, enter the following data and choose Execute:Company code: for example, 3310Sec. Class ID Number: for example, MMF_AE1Securities Account: for example, AE_MMF | The Display Securities Account Class Position List is displayed according to the filter values. |  |

#### Create Fund Redemption Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a sale transaction has concluded in the real world, you need to enter the deal information into the system to update the securities position. In this step, you update the position sold.

|  |
| --- |
| Note The securities position on hand must be greater than or equal to the position to be sold.We also support the option when sale amount is fix before the quantity and price are known. The transaction type is 201. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, MMF_AE1Transaction Type: 200Partner: for example, 33537001 | The Create Investment Fund: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:In the Position area,Securities Account: for example, AE_MMFGeneral Valuation Class: <use the same General Valuation Class as purchase transaction for this security class ID>Position Value Date: for example, <the current date>Calculation Date: for example, <the current date>Payment Date: for example, <the current date>In the Amount area,Number of Units: for example, 1,000Price (Unit Quoted): for example, 1 | All data are entered. |  |
| 5 | Save the Transaction | Choose Save. | The data is saved |  |

### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a securities transaction is recorded and saved in SAP, the transaction must be settled before you perform further activities. This section describes how to set the settlement status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Securities Transactions - Collective Processing (TS00) | The Securities: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Securities: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the transaction number(s)> | The list of transaction(s) is displayed on Securities: Collective Processing screen. |  |
| 4 | Settle the Transaction | Select the checkbox of a transaction on Securities: Collective Processing screen, and choose Settle. | The Settle Security Contract: Structure screen is displayed. |  |
| 5 | Save the Change | On the Settle Security Contract: Structure screen, the value of the Activity field in header is 2 - Contract Settlement.Choose Save.If the Document lines: Display messages dialog displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

### Payment from Sale

Purpose

This section describes how to handle the payment for securities redemption transaction, and how to post it to G/L accounting.

Prerequisites

You have set the status of the transaction to Contract Settlement.

#### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by a bank, it is not necessary to run previous steps Generate Payment Request and Process Payment Request, because the outgoing payment is initiated by the bank.

Procedure

This step doesn't require any operation in the system.

#### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. Two apps are available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this app to generate the posting for incoming payment. Note that it will not create postings for outgoing payment processed in the previous Generate Payment Request step with the Pay Only option.
- Process Business Transactions (TPM10): Use this app to generate the posting for the outgoing payment processed in the previous Generate Payment Request step with the Pay Only option.

|  |
| --- |
| Note You can also a schedule background job for this step. Please see the corresponding step in the Appendix. |

Prerequisite

The outgoing payment which should be handled via payment request (if there is) for this transaction has been processed in previous step Generate Payment Request with the Pay Only option.

|  |
| --- |
| Note If the sale amount is fixed before the quantity and price are known, which means you use the transaction type 201 for the fund redemption transaction, please fix the price of the transaction and settle the priced transaction before posting it to the general ledger. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Securities: <select this checkbox>Company code: for example 3310Transaction: <transaction number with inflow which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | The Posting Log: Posted Business Transactions screen is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria. You can skip current test step and continue with app Process Business Transactions (TPM10). |  |
| 4 | Production Run | Choose Back.On the Treasury: Post Flows screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Posting Log: Posted Business Transactions screen is displayed. An accounting document is created for the incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Fix, Post or Reverse Transactions screen displays. |  |
| 6 | Enter Selection Criteria for Test Run | On the Fix, Post or Reverse Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>Company code: for example, 3310Valuation Area: for example AE0Limit by Transaction Number: <select this checkbox>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If the You have not selected any business transactions message is displayed, that means there is no posting needed for your selection criteria. You can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.The Test Run: Display Posted/Reversed Business Transactions screen is displayed, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is a test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Fix, Post or Reverse Transactions screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 9 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.On the Update Run: Display Posted/Reversed Business Transactions screen, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, and an accounting document is created for the outgoing payment in local GAAP (valuation area AE0). |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Product Group: for example, SecuritiesCompany Code: for example, 3310 | The posting journals display per the filter values. |  |

#### Treasury Position Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display treasury position analysis for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Treasury Position Analysis. | The Treasury Position Analysis screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, Current DateInclude Planned Data: for example, 1Valuation Area: for example, AE0Company Code: for example, 3310Product Type: for example, 02A and 02B | The position analysis data displays per the filter values. |  |

#### Display Treasury Position Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display treasury position values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Display Treasury Position Values (F1867) . | The Display Treasury Position Values screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select GoKey Date: for example, Current DateProduct Group: for example, SecuritiesNote You may need to adapt the filters to make the OpenProduct Group filter display.Company Code: for example, 3310Valuation Area: for example, AE0 | The position values data displays per the filter values. |  |

#### Define Financial Positions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define a set of key figures to be displayed in the Financial Status - Book Value and Financial Status - Nominal Amount screens.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define Financial Positions (FTR_FP_DEF). | The "Maintain Financial Position Groups": Change screen is displayed. |  |
| 3 | Maintain Key Figure Groups | Choose New Entries.Enter the data below and choose Save.Financial Position Group: for example, FPG_MMF_A0001Financial Position Group Description: for example, Bank accounts and MMFAssets/Liabilities: for example, Assets | The data is saved.Note if FPG_MMF_A0001 is already created for the same purpose, you can skip this step and use the existing record. |  |
| 4 | Maintain Key Figures | In the Dialog Structure area, double-click on the Maintain Financial Positions folder, and choose New Entries.Enter data and choose Save.Financial Position: for example, FP_MMF_A0002Financial Position Description: for example, Money Market Fund AccountFinancial Position Group: for example, FPG_MMF_A0001Data Source: for example, Treasury Position Management | The New Entries: Overview of Added Entries screen displays to allow you to enter and save the Key Figures.. |  |
| 5 | Maintain Selections | Select financial position Short term investments-MMF, choose Back, and select Maintain Selections.Product Type = 02A to 02CTransaction Type = 100 to 600Valuation Class = 20 to 30Valuation Area = AE0Posting Status = 2Choose Back and choose Save. | The data is saved. |  |

| Financial Position Group | Financial Position Group Description | Assets/Liabilities |
| --- | --- | --- |
| FPG_MMF_A0001 | Bank accounts and MMF | Assets |

| Financial Position | Financial Position Description | Financial Position Group | Data Source | Maintain Selection |
| --- | --- | --- | --- | --- |
| FP_MMF_A0001 | Bank accounts | FPG_MMF_A0001 | One exposure | House Bank = A* to Z* |
| FP_MMF_A0002 | Money Market Fund Account | FPG_MMF_A0001 | Treasury position management | Product Type = 02A to 02CTransaction Type = 100 to 600Valuation Class = 20 to 30Valuation Area = AE0Posting Status = 2 |

#### Financial Status - Book Value

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

Refer to Define Financial Position for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Financial Status (F2136). | The Financial Status - Book Value screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, Current DateReporting Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays per the filter values. |  |

#### Financial Status - Nominal Amount

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the financial status of the nominal amount.

Prerequisite

You have already defined the financial positions. Please refer to the [Define Financial Positions](#unique_58) [page ] 93 step to define financial positions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)). | The Financial Status - Nominal Amount screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go.Key Date: for example, Current DateReporting Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays per the filter values. |  |

#### Display Treasury Payments

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review all payment journals.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Payments (TPM20A). | The Payment Journal screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Execute.Company Code: for example: 3310Product Type: 02A, 02B | The payment journals are displayed. |  |
| 4 | Review data | Review the data displayed on the screen. You can also select on Original business transaction or Details to drill down for more details. |  |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows (F1754) screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Position Flows (F1754) screen, enter following data and choose Go:Product Group: for example: SecuritiesCompany code: for example, 3310 | Position Flow data is displays according to the filter values. |  |

#### Display Treasury Alerts - Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to display treasury alerts for posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Alerts - Posting (F4984). | The Display Treasury Alerts screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Alerts screen, enter following data and choose Go:Issue Message For: PostingCompany Code: for example, 3310 | Alerts data is displayed per the filter values |  |

#### Display Treasury Alerts- Settlement, Release and Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to display treasury alerts for various type of transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Alerts - Settlement (F4979). | The Display Treasury Alerts - Settlement screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Alerts screen, enter following data and choose Go:Issue Message For: SettlementCompany code: for example, 3310 | Alerts data displays per the filter values. |  |
| 4 | Confirm Alerts for Other Transactions | Select other values in the Issue Message For field.Release / Payment / Correspondence / Interest Rates |  |  |
| 5 | Select Display Treasury Alerts Tiles with Release | Open Display Treasury Alerts - Release (F4980). | The Display Treasury Alerts - Release screen is displayed, with Issue Message For = Release. |  |
| 6 | Select Display Treasury Alerts Tiles with Payment | Open Display Treasury Alerts - Payment (F4981). | The Display Treasury Alerts - Payment screen is displayed, with Issue Message For = Payment. |  |
| 7 | Select Display Treasury Alerts Tiles with Interest Rates | Display Treasury Alerts - Interest Rates (F4982) | The Display Treasury Alerts - Interest Rates screen displays, with Issue Message For = Interest Rates. |  |

#### Display Payment Schedules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to display the payment schedule for interest flows due.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedule screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Payment Schedule screen, enter the following data and choose Execute:Securities: select this checkboxCompany code: for example, 3310End of Term in the Future: <select this checkbox>End of Term in Lapsed: <select this checkbox>Payment Period: for example, <Current Date to Current Date + 5 days>Payment Status: for example, 1Output Error Log: <select this checkbox> | You can check payment schedule report. |  |

#### Display Securities Account Class Positions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the securities account class position list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Securities Account Class Positions (TPM40A). | The Display Securities Account Class Position List screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Securities Account Class Position List screen, enter the following data and choose Execute:Company Code: for example, 3310Sec. Class ID Number: for example, MMF_AE2Securities account: for example, AE_MMFPosition Value Date: for example, <Current date> | The position is displayed. |  |

#### Analyze NPV

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you calculate and display the NPV result.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Analyze NPV (JBRX). | The NPV Analysis: Display of Single Values screen is displayed. |  |
| 3 | Enter Selection Criteria of Gen. Selection | On the NPV Analysis: Display of Single Values screen, enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <current date>Horizon: for example, <end date of current month>Portfolio Hierarchy: for example, 100 |  |  |
| 4 | Enter Selection Criteria of Characteristics | Choose the Characteristics tap, enter the following data then choose Execute:Company Code: for example, 3310Product Type: for example, 02A | The NPV Result displays based on Portfolio Hierarchy. |  |

#### Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you calculate and display online market risk key figures, such as NPV and sensitivity key figures for the selected financial transactions.

Prerequisite

You have maintained the report layout for key figure as described in the [Defining Report Layout for Calculate Market Risk Key Figures](#unique_91) [page ] 140 step of the Appendix section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Calculate Market Risk Key Figures (AISGENKF). | The Calculate Market Risk Key Figures screen is displayed. |  |
| 3 | Enter Selection Criteria of Gen. Selection | On the Calculate Market Risk Key Figures screen, enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <the current date>Horizon: for example, <the end date of current month>Report Layout: for example, <Y01 or other Report Layout you created>Portfolio Hierarchy: for example, 100 | The system calculates the net present value on the horizon date, using the transaction data and market data on the evaluation date. |  |
| 4 | Enter Selection Criteria | Choose the Characteristics tab, enter the following data then choose Execute:Company Code: for example, 3310Product Type: for example, 02A | The Single Value Analysis for assigned Report Layout is displayed. |  |

#### Sensitivity Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can check sensitivity key figures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Sensitivity Key Figures - Single Analysis (AISS). | The Sensitivity Key Figures - Single Analysis screen is displayed. |  |
| 3 | Enter Selection Criteria of Gen. Selection | On the Sensitivity Key Figures - Single Analysis screen, enter the following data:Display Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <the current date>Horizon: for example, <the end date of current month>Portfolio Hierarchy: for example, 100 | The system calculates the net present value on the horizon date, using the transaction data and market data on the evaluation date. |  |
| 4 | Enter Selection Criteria | Choose the Chars tab, enter the following data then choose Execute:Company Code: for example, 3310Product Type: for example, 02A | The Sensitivity Key Figures report is displayed based on Portfolio Hierarchy. |  |

#### Review Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the limit utilization report.

Prerequisite

You have maintained the limit master records of your company, and processed the [Generate Limit Utilizations](#unique_27) [page ] 39 step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Overview of Utilizations - Selection Using all Characteristics screen, enter the following data and choose Execute:Limit Type: for example, Y01Limit Utilization Base: for example, 1Determination Date:<the current date>Limits Valid From: <the current date> | The system displays an overview of the limit utilization in accordance with your selection criteria. |  |

## Appendix

### Position Indicator

#### Change Position Indicator

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check and change the position indicator.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Position Indicator (TPM57A). | The Display Position Indicator screen is displayed. |  |
| 3 | Enter Parameters | On the Display Position Indicator screen, enter following data and press Enter:Product Group: select SecuritiesCompany Code: for example, 3310ID Number: for example, MMF_AE1Securities Account: for example, AE_MMF | The Securities Account Position Indicator and Subledger Position Indicator sections are displayed.Note If you want to change position indicators, go back to the opening screen, input the position indicator information, and choose More > Position Indicator > Change. |  |

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

If security exists, the spot price needs to be maintained for current date. Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Middle Office Jobs (F2772). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information for New Job | On the Template Selection area, enter following data then choose Step 2:Job Template: for example, <End of Day Processing>Job Name: for example, <End of Day Processing> | You've chosen the job template, and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Information area, enter following data then choose Step 3:For Start Immediately case:Start Immediately: <select>For Recurrence case:Start Immediately: <deselect>Choose Define Recurrence Pattern to define recurrence patternStart: for example, <Current Date/Current Time>Recurrence Pattern: for example, DailyEvery: for example, 1End: for example, after 7 Occurrence(s)On Non-Working Day: No restrictionNote Schedule this job after back office's job for generating payment request by using the same job template. | You've enter the scheduling recurrence pattern, and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameter Section area, enter the following data and choose Schedule:Company Code: 3310Determination Procedure: <select 10 and 20 from the F4 help input> |  |  |
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
| 1 | Log On | Log on to the SAP Fiori launchpad a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs view, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Fix, Pay and Post FlowsJob Name: for example, <Generate Payment Request> | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and in the Scheduling Information dialog box, enter the following data:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time default>Time Zone: <select a time zone or use default>Recurrence Pattern: for example, DailyEvery: for example, 1Day(s)End: for example, select After and then enter 7 occurrence(s)On Non-Working Days: for example No RestrictionChoose OK, and choose Step 3.Note If you would rather to start job at once, select Start Immediately checkbox. | You've defined the recurrence pattern and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area,In the Application sub-area, select one or more proper product groupIn the General Selection sub-area, enter the following data:Company Code: for example, 3310Transaction: <enter transaction numbers if you'd like to limit transactions>Product Type: <enter product types if you'd like to limit product types>Due Date Period: for example, 0On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.In the Posting Control sub-area,Test Run: <deselect this checkbox>Pay Only: <choose this radio button>Note You can also choose the Post All Valuation Areas radio button, if you want to post to all valuation areas |  |  |
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
| 4 | Enter General Information for New Job | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Fix, Pay and Post FlowsJob Name: Post Flows |  |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information dialog box :Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day:for example, Run on next Working DayChoose OK, and choose Step 3.Note If you would like to start job at once, select the Start Immediately checkbox.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Application sub-area, select a proper Application.In the General Selection sub-area, enter the following data:Company Code: for example, 3310Transaction: <enter transaction numbers if you'd like to limit transactions>Product Type: <enter product types if you'd like to limit product types>Due Date Period: for example, 0In the Posting Control sub-area, make the following selections:Test Run: <deselect this checkbox>Post Operational Only: <Choose this indicator>Note You can also choose Post All Valuation Areas (instead of Post Operational Only) to post flows to all valuation areas. |  |  |
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

In this step, you schedule a background job to fix and post the outgoing payment, which were processed in the previous Generate Payment Request step with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs view, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the General Information area, enter the following data, and choose Step 2:Job Template: Process Business TransactionsJob Name: for example, Process Business Transactions |  |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box :Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Product Groups sub-area, select one or more product groups.Company Code: for example, 3310Valuation Area: for example, AE0, or leave it blank (run for all valuation areas)In the Limit by Transaction Number sub-area, make the following selection:Limit by Transaction Number: <deselect this checkbox>In the Limit by Subledger Positions sub-area, make the following selection:Limit by Subledger Pos.: <select this checkbox>Product Type: <enter product types if you'd like to limit product types>Transaction: <enter transaction numbers if you'd like to limit transactions>Trans. to Be Fixed/Posted: <select this checkbox>In the Posting Control sub-area, make the following selection:Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details view displays. |  |

#### Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to value the positions of financial instruments, based on historical cost or fair value for a given key date, and transfer results to financial accounting.

Prerequisite

Fair values using Net Present Value (NPV) have been calculated or maintained for financial transactions which are evaluated at fair value (NPV) according to accounting principles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Enter General Information | In the Template Selections area, enter the following data, and choose Step 2:Job Template: Run ValuationJob Name: for example, Run Valuation | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, enter the following data, and choose Step 3:Start Immediately: <unselect this checkbox>Start: for example, <first day of next month for this year and at time 03:00>Note Schedule your run time to be later than the Treasury - Calculate Net Present Value - With CVA and DVA job. | You've defined the scheduling option and are navigated to the Parameters area. |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:Company Code: for example 3310Valuation Area: for example, AE0, or leave it blank (run for all valuation areas)In the Loans sub-area, enter the following data:Transaction: <enter transaction numbers if you'd like to limit transactions>In the Valuation Parameters sub-area, enter the following data:Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, select Mid-year Valuation with ResetNote When the Period End is also the Year End, the Valuation Category Year End Valuation is used.In the Posting Control sub-area, make the following data:Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

#### Update Security Cash Flow

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to update security cash flow on a regular basis.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information for New Job | In the Template Selection area, enter following data then choose Step 2:Job Template: for example, Update Securities Account Cash FlowJob Name: for example, Update Securities Account Cash Flow | The Scheduling Options area is displayed |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately. | You've defined the recurrence pattern and are navigated to the Parameters area。 |  |
| 6 | Enter Parameters | In the Parameters area, enter the following data:Company Code: for example, 3310Product Type: for example, 02A and 02B |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

#### Post Debit Position

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you schedule a background job to post debit position.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information for New Job | In the Template Selection area, enter following data then choose Step 2:Job Template: for example, Post Debit PositionJob Name: for example, Post Debit Position | The Scheduling Options area is displayed. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately. | The Parameters area is displayed. |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the General Selection sub-area,Company Code: for example, 3310Product Type: for example, 02BSecurity Account: for example, AE_MMFSec. Class ID Number: for example, MMF_AE2Update Type: for example, SAM5020In the Debit Position Parameter sub-area,Up to an Including Pos. Date: for example, <end date of current month>In the Posting Control sub-area,Document Date: for example, <end date of current month> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
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

In this step, you schedule a background job to calculate market risk key figures, including the key figure Value at Risk; the result of calculation is persisted in the database for analysis with the SAP Analytics Cloud. The calculation risk keys are defined in the market risk key figure set.

This step is different from the Calculate Market Risk Key Figures step in the Reports section, which is a real-time calculation for the risk keys in the defined report layout.

|  |
| --- |
| Note There are three methods to calculate the Value at Risk key figure, the historical simulation, the Monte Carlo simulation and a parametric method (variance-covariance approach).For the historical simulation, the daily market data of past 250 days needs to be maintained.For the Monte Carlo simulation and the variance-covariance approach, the statistical data of volatility or correlation is required. The calculation is based on the historical daily market data. You need to maintain the daily market data of past 113 days. |

Prerequisites

You have maintained the market risk key figure set, as described in the [Manage Market Risk Key Figure Sets](#unique_101) [page ] 143 step in the Appendix section.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Middle Office Jobs (F2772). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The New Job screen is displayed. |  |
| 4 | Enter General Information for New Job | In the General Information subarea, enter the following data, and choose:Job Template: Calculate Market Risk Key FiguresJob Name: for example, Calculate Market Risk Key FiguresNote You can delete the existing market risk key figure values on the specified evaluation date by the Delete Market Risk Key Figures job template. |  |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options subarea, enter the following data:Start Immediately: <select this checkbox> |  |  |
| 6 | Enter Selection Data for New Job | On the General tab, enter the following data:Basic Run: <select this checkbox>Adjustment Run: <deselect this checkbox>Note The adjustment run processes new financial objects and financial objects for which errors have occurred in the base run.Market Risk Key Figure Set: for example, <MRK01, and MRK02, the key figure set you maintained>Evaluation Date (Dynamic): for example, <the current date, or enter the evaluation date>Calculate Statistical Data: <deselect this checkbox, determine whether calculate statistical figure as volatilities or correlations> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are back to the initial screen, and the job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose  at the end of the row for the job you just scheduled. | The Job Details screen is displayed.If it is in status Finished (depends on parameters you entered for Scheduling Options), click on the icon beside Results, a new window will open and you can check the result of this finished job. |  |

### Output Management

SAP S/4HANA introduces a new output management approach. This new output management includes cloud qualities, such as:

- Extensibility enablement
- Multi-tenancy enablement
- Modification-free configuration

The complete configuration differs from the configuration that is used when output management is based on NAST. The configuration is based on BRF+, which is accessible for customers. In SAP S/4HANA, the target architecture is based only on Adobe Document Server and Adobe Forms. BRF+ functionality (in this case, in combination with message determination) is used for the form determination rules (along with other output parameters). For TRM, we deliver an application object type Treasury and Risk Management. All the predelivered output determination rules are maintained under this application object type. We provide several apps to let you easily manage your output.

#### Output Parameter Determination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Output Parameter Determination app to manage the determination rules for the output. The following determination steps are under Treasury and Risk Management:

Table 2: Determination Steps

| Step | Information | Comments about settings |
| --- | --- | --- |
| Output type | SAP predelivers necessary configurations | Do not change this setting |
| Receiver | SAP predelivers necessary configurations | Do not change this setting |
| Channel | SAP predelivers necessary configurations | Do not change this setting |
| Printer Settings | SAP predelivers necessary configurations | You can change this setting |
| Email Recipient | Maintain e-mail recipients for outgoing correspondence objects in the e-mail channel | This setting overwrites the e-mail address in Business partner master data |
| Email Settings | Specify the e-mail template and sender e-mail address. SAP predelivers PDF form templates. | Create your own forms with the Maintain Email Template app |
| Form Template | Specify the PDF form template and number of copies. SAP predelivers PDF form templates. | Create your own forms with the Maintain Form Template app |
| Output Relevance | SAP sets all output types as output relevant | Do not change this setting |

|  |
| --- |
| Note The operations to change these settings are similar. This section describes the steps to change the e-mail recipients and sender's e-mail address as an example. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination view displays. |  |
| 3 | Display current Email recipients | Enter the following data and press Enter:Show Rules for: Treasury and Risk Management CorrespondenceDetermination Step: Email RecipientNote By default, no e-mail recipients are maintained by SAP. | The default e-mail recipient rule displays. |  |
| 4 | Maintain Email recipient for Internal Counterparty | In the Maintain Business Rules section, choose Edit. |  |  |
| 5 | Maintain Email recipient for Internal Counterparty | Choose Insert New Row. |  |  |
| 6 | Maintain Email recipient for Internal Counterparty | Make the following entries:Output Type: TRM_DEAL_SLIPNote To enter the value, from the dropdown list, choose Direct Value Input. In the field to the right of the is equal to value, enter TRM_DEAL_SLIP and choose OK. Use this method for the remaining field entries in this step.Role: INEmail Type Code: To, CC, or BCCE-Mail Address: for example, <Email address>Note To add more condition columns, choose Table Settings and make the necessary changes. For example, you can add another condition column (BusPartner) to maintain different e-mail recipients for different business partners. | The internal recipient e-mail address is maintained. |  |
| 7 | Maintain Email recipient for external counterparty | Repeat steps 5 to 6 with the following data:Output Type: TRM_TRANSACTION_CONFIRMATION (Transaction Confirmation)Role: INEmail Type Code: To, CC, or BCCE-Mail Address: for example, <Email address> | The external recipient Email address is maintained. |  |
| 8 | Activate Email Addresses | Choose Activate. | The Confirmation Activation dialog box displays. |  |
| 9 | Activate Email Addresses | Choose Yes. | The system displays the message Objects saved and activated. The e-mail addresses are saved and activated. |  |
| 10 | Display Email settings for Sender Email address and Email template | Enter the following data and press Enter:Determination Step: Email Settings | The default e-mail settings are displayed. |  |
| 11 | Change Email settings for Sender Email address and Email template | Choose Edit. |  |  |
| 12 | Change Email settings for Sender Email address and Email template | Make the following entries:Sender Email: for example, <Email address>.Note To create a new e-mail template, use the Maintain Email Template app. | Email settings are changed. |  |
| 13 | Activate Email Settings | Choose Activate. | The Confirmation Activation dialog box displays. |  |
| 14 | Activate Email Settings | Choose Yes. | The system displays the message Objects saved and activated. The e-mail settings are saved and activated. |  |

#### Manage Output Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the output correspondence objects are generated, you can use this app to track the status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Output Items (F2279). | The Manage Output Items view displays. |  |
| 3 | Enter filter criteria and execute the report | Make the following entries and choose Go:Application Object ID: <Transaction number>Application Object Type: TRM_CORRESPONDENCENote If the Application Object ID field is not displayed, choose Adapt Filters. Choose More Filters. Select Application Object ID and choose OK.Note When you enter the data in the input field, an input help automatically displays the possible entries for you. You can choose from the list instead of enter the whole words.Correspondence objects could have following status:In PreparationCompletedIn pendingErrorTo check the detailed log, select the correspondence and choose Show Application Log.To resend a correspondence object even it has completed status, you can select the correspondence object and choose Resend. | The status of the output correspondence objects is listed. You can search for your transaction and check the status. |  |

#### Maintain Print Queues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the outgoing correspondence objects in the Print channel.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Print Queues (F1260). | The Maintain Print Queues view displays. |  |
| 3 | Display TRM Print Queue Status | Scroll down and choose a TRM print queue (for example, Default). | The Print Queue view displays. |  |
| 4 | Display TRM Print Queue Status | Select a line with the transaction number you noted in a prior step. Click the text of the print name to download a PDF file.Note By default, SAP provides the following print queue for TRM:DEFAULT | All the TRM outgoing correspondence objects in channel Print display with latest status. |  |

#### Display Email Transmissions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For the e-mail channel, you can check if the e-mail is successfully sent.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Monitor Email Transmissions (F5442). | The Monitor Email Transmissions view displays. |  |
| 3 | Display Email Transmission Status | Use the Status dropdown list to filter for Error, Sent or Waiting.Use the Created At field to search within a specific date range and choose Go.Note If an e-mail status is Transmitted, the e-mail is sent out to the recipient.If an e-mail status is Sent, the system tried to send the e-mail. However, the user is not guaranteed to receive the e-mail. | All the outgoing e-mails for selected correspondences are displayed. |  |

#### Maintain Email Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create your own e-mail templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Email Templates - Deprecated (F1306). | The Maintain Email Template view displays. |  |
| 3 | Copy a Predelivered Email Template to a Custom Email Template | Choose the Predelivered tab. | The predelivered e-mail templates are displayed. |  |
| 4 | Copy a Predelivered Email Template to a Custom Email Template | Use the Search field to find an email template to copy (for example, FTR_CORR_EMAIL_TEMPLATE_CNF), select the checkbox and choose Copy. | The Copy Template FTR_CORR_EMAIL_TEMPLATE_CNF dialog box displays. |  |
| 5 | Copy a Predelivered Email Template to a Custom Email Template | Make the following entries:Name: for example, TRM Transaction Confirmation Customer Email TemplateNote The new copied e-mail template is prefixed with YY1_. | The system displays the message Template has been copied. |  |
| 6 | Change Customer Email template | Locate and choose your copied e-mail template within the Custom tab view, in this example: YY1_FTR_CORR_EMAIL_TEMPLATE_CN. |  |  |
| 7 | Change Customer Email template | Choose Change Details. | The TRM Transaction Confirmation Default Email Template dialog box displays. |  |
| 8 | Change Customer Email template | Make the following entries and choose Change Details:Description: TRM Transaction Confirmation Customer Email Template | The Email Template view displays. |  |
| 9 | Change Customer Email template | In the Available Languages pane, select a language version, for example, English. Click the name itself. | The Email Template Content view displays. |  |
| 10 | Change Customer Email template | Adjust the e-mail subject and body as needed. When done, choose Save.Note SAP defines variables that you can use in e-mail templates. To view the variable list, choose Show Data Fields. | The custom e-mail template is adjusted successfully. |  |

#### Maintain Form Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create your own form templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Form Templates (F1434). | The Output Management Form Template view displays. |  |
| 3 | Download a Predelivered Form Template | Choose the Predelivered Templates tab. All the pre-delivered form templates display. | Predelivered templates are displayed. |  |
| 4 | Download a Predelivered Form Template | Select a form template (for example, FDP_TRM_CONF_DE) | The details of the form template are displayed. |  |
| 5 | Download a Predelivered Form Template | Choose Download. | The Download Template dialog box displays. |  |
| 6 | Download a Predelivered Form Template | Choose OK. | The form template is downloaded successfully. |  |
| 7 | Change the customer Form template file | Using Adobe LiveCycle Designer, adjust and save the form template.Note You must install Adobe LiveCycle Designer to edit the form template. |  |  |
| 8 | Upload Customer Form Template | Open Maintain Form Templates (F1434). | The Output Management Form Template view displays. |  |
| 9 | Upload Customer Form Template | Choose the Custom Templates tab. |  |  |
| 10 | Upload Customer Form Template | Choose New. | The Create Form Template dialog box displays. |  |
| 11 | Upload Customer Form Template | Make the following entries and choose OK:Form Template Name: for example, CUST_TRM_CONF_DELanguage: for example, EnglishSelect Form Template File: select Browse and choose the file.Data Source: for example, FDP_TR_CORR_SRVForm Type:Content | The customer form template is created successfully. |  |

### Reconciliation of External Securities Account Statements

Purpose

This section described the reconciliation of external securities account statements activities which are not described in the Test Procedures section.

#### Create the Statements of External Securities Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the statement of external securities account manually.

If the treasury correspondence integration with SWIFT Network is set up, and the statement is generated from the incoming MT535 message automatically, the step can be skipped. Refer to the test script Treasury Correspondence Integration with SWIFT Network3QM for details.

Prerequisite

The External Securities Account ID is maintained for the security account.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Statements - External Securities Account (RECON4). | The Select External Securities Account Statement of Processing screen is displayed. |  |
| 3 | Enter Parameters | On the Select External Securities Account Statement of Processing screen, enter the following data and choose Enter:Company Code: for example, 3310Securities Account ID: for example, <External Securities Account ID you have created>, for example, 123XXXX567 | The External Securities Account Statements: Display screen is displayed. |  |
| 4 | Create New Statement | Choose Create external securities account statement screen, enter the following data and choose Save:Company Code: for example, 3310External Sec. Acct ID: for example, <External Securities Account ID you have created>, for example, BD_AE3Key Date: for example, <Current Date>Date Category: for example, Position DateStatus: for example, SOPENDescription: for example, External Statement | New statement is created. |  |
| 5 | Create External Position | On the tab Pos., choose Create Position. New screen External Position : Create is displayed. Enter the following data, and choose Save:ID Number: for example, <the security class you have created> , for example, BD_04External Nominal Amount: for example, 100,000,000.00 | New external position is created. |  |

#### Reconciliation of External Securities Account Statements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reconcile the statement of external securities account with internal position.

Prerequisite

The statement of external securities is uploaded.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Reconcile Statement - External Securities Account (RECON5). | The Reconciliation of External Securities Account Statements Using Sec. Acct ID screen is displayed. |  |
| 3 | Enter Parameters | On the Reconciliation of External Securities Account Statements Sec. Acct ID screen, enter the following data and choose Execute:Company Code: for example, 3310Securities Account ID: for example, <External Securities Account ID you have created>, for example, 123XXXX567Key Date: for example, <Current Date>Status: for example, SOPEN | The Reconciliation of External Securities Account Statements Using Sec. Acct ID screen is displayed. |  |
| 4 | Check the Reconciliation Report | On the Reconciliation of External Securities Account Statements Using Sec. Acct ID screen, check the reconciliation report. | If there is a difference between the internal and external nominal, an error message will occur. |  |

### Accounting

Purpose

This section describes some accounting relevant activities which are not described in the Test Procedures section.

#### Reverse Accrual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reverse accrual posted for the deal.

For example, you executed the accrual on an incorrect date, you would like to reverse it.

Prerequisite

The accrual of the position has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Reverse Accrual/Deferral (TPM45). | The Reverse Accrual/Deferral of Expenses and Revenues screen is displayed. |  |
| 3 | Test Run | On the Reverse Accrual/Deferral of Expenses and Revenues screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: <leave blank, or enter a specific valuation area, for example, AE0>Sec. Class ID Number: <Security class ID number(s) for which accrual has been executed>Securities Account: <Securities account(s) for which accrual has been executed>Accrual/Deferral Key Date: for example, <date on which the reversal of accrual should take place>Test Run: <select this checkbox>Reasons for Reversal: for example, 04 Other reasonsImmediate Posting: <select this checkbox>Note Choose Logs and Messages, you can see the simulated reversal posting information. Please note there is no posting created because it is test run. | New screen Reverse Accrual/Deferral of Expenses and Revenues is displayed. |  |
| 4 | Production Run | Choose Back until the initial screen of this app, change the following data and choose Execute:Test Run: <unselect this checkbox>Note Choose Logs and Messages, you can see the posting information for reversal. This time, an accounting document has been created. | New screen Execute Accrual/Deferral of Expenses and Revenues is displayed. |  |

#### Reverse Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reverse the period end valuation posting.

For example, if you have done the period end valuation with incorrect currency rate or incorrect evaluation type, you may need to reverse the valuation.

Prerequisite

The period end valuation of the deal has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Reverse Valuation (TPM2). | The Reverse Valuation (TPM2) screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Reverse Valuation (TPM2) screen, enter the following data and choose Execute:Securities: <select this checkbox>Company code: for example, 3310Valuation Area: leave blank, or enter specific valuation are, for example AE0Sec. Class ID Number: <Security class ID number(s) for which valuation has been executed>Securities Account: <Securities account(s) for which valuation has been executed>Key Date for Valuation: for example, <the date on which the reversal should take place>Reasons for Reversal: for example, 04 Other reasonsTest Run: <select this checkbox> | The Display Positions to be Reversed screen is displayed. |  |
| 4 | Reverse Valuation for Test Run | On the Display Positions to be Reversed screen, choose Reverse Valuation (TPM2). | The screen Reversal Log: Reversed Business Transactions is displayed, and message Valuation (test run) has been successfully reversed shows up.You can check the simulated reversal posting information on this screen, please note there is no posting created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Display Positions to be Reversed screen is displayed. |  |
| 6 | Reverse Valuation for Production Run | On the Display Positions to be Reversed screen, choose Reverse Valuation (TPM2).Check the posting on the screen, and accounting document for reversal has been created. | The screen Reversal Log: Reversed Business Transactions is displayed, and the Valuation has been successfully reversed is displayed. |  |

#### Reverse Debit Position

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you need to reverse the debit position after posting, you can use the app Reverse Debit Position (FWOEZ).

Prerequisite

A previous debit position has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Reverse Debit Position (FWOEZ). | The Manual Posting / Debit Position: Reverse screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Manual Posting / Debit Position: Reverse screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class: for example, MMF_AE1Securities Account: for example, AE_MMF | A list of fixed debit positions is displayed. |  |
| 4 | Reverse Debit Position (FWOEZ) | On the Manual Posting / Debit Position: Reverse screen, select a record to reverse and choose Reverse business transaction: | The Reverse Business Transaction screen is displayed. |  |
| 5 | Process the Reversal | On the Reverse Business Transaction screen, enter the following data and choose Reverse:Reason for Reversal: for example, Process. errorFI Reversal Date: for example, <original posted date> |  |  |

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

The objective of this step is to create market data shifts to be able to analyze key figures with modified market data. It will be used in the [Defining Report Layout for Calculate Market Risk Key Figures](#unique_91) [page ] 140 step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Market Data Shift (JBR0) | The Edit Market Data Shifts screen is displayed. |  |
| 3 | Enter Market Data Shifts Name | On the Edit Market Data Shifts screen, enter the following data and choose Create:Market Data Shift: for example, 1 | The Define Market Data Shifts screen is displayed. |  |
| 4 | Define Market Data Shift | On the Define Market Data Shifts screen, enter the following dataShort Name: for example, <Market Data Shift 0001> |  |  |
| 5 | Maintain Yield Curves of Market Data Shift | On the Define Market Data Shifts screen, choose the Yield Curves tab, choose the Insert Row button, then enter the following data and choose SaveShort Name: for example, Euro Depo ShiftCurrency: for example, AEDYC. Type: for example, 0001Ref.Int.Rate: for example, AEDM03AEDPercentage: for example, 2 | Market Data Shift is saved |  |

#### Maintain Scenarios

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this step is to create scenarios. A scenario is a market data record which can contain current market data, exchange rates, exchange rate volatilities, yield curves, interest rate volatilities, e.g. you can create scenarios, which represent market situations you consider possible or probable (for example, a high interest rate scenario with an inverted yield curve).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Scenarios (TV21) | The Scenario Admin: Initial Screen screen is displayed. |  |
| 3 | Enter Scenario Name | On the Scenario Admin: Initial Screen screen, enter the following data and choose Create:Scenario: for example, 1 | The Create Scenario 1 screen is displayed. |  |
| 4 | Maintain Scenario | On the Create Scenario 1 screen, enter the following dataScenario: Full Name: for example, Scenario 1Scenario: Short Name: for example, Scenario 1 |  |  |
| 5 | Maintain Exch. Rates of Scenario | On the Create Scenario 1 screen, choose Exchange Rates tap, then enter the following data:Reference Currency: for example, AEDIn the Other Currencies area, choose Insert Row, enter the following data:Currency: for example, USDBid Rate: for example, 1.2Ask Rate: for example, 1.2Then choose Save.Note Market Data Shift is parameter shifts based on market data imported; for scenario, you can maintain parameters without reference. | Scenario is saved |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Calculate Market Risk Key Figures (AISGENKF). | The Calculate Market Risk Key Figures screen is displayed. |  |
| 3 | Access Report Layout Definition screen | On the Calculate Market Risk Key Figures screen, enter the Evaluation Currency and Evaluation Type, and choose Define Report Layout. | The Change View "Key Figure Layout": Overview screen is displayed. | . |
| 4 | Create Layout-ID entries | On the Change View "Key Figures Layout": Overview screen, Choose New Entries, then insert the following data in the Key Figure Layout form and Save:ROW1Layout-ID: for example, Y01Short Name: for example, NPV/BPV/DurationLong Name: for example, NPV/BPV/DurationROW2Layout-ID: for example, Y02Short Name: for example, NPV + Market Data shiftsLong Name: for example, NPV + Market Data shifts | Two new entries have been created. |  |
| 5 | Access Key Figures Maintain screen | On the Change View "Key Figures": Overview screen, select the checkbox of Layout-ID Y01, then double click Key Figures folder in the Dialog Structure panel. | The Change View "Key Figures": Overview screen is displayed in the main area. |  |
| 6 | Maintain Key Figures of Layout | On the Change View "Key Figures": Overview screen, choose New Entries and then insert the following data in the Key Figures form:ROW1Key Figure Name: for example, BARWERTPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDec.Places: for example, 0ROW2Key Figure Name: for example, BPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_BASE_POINTShort Name: for example, BPVShift Rule: for example, 0Dec.Places: for example, 0ROW3Key Figure Name: for example, CRFNPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, RISK_FREE_NPVShort Name: for example, Current Risk Free NPVShift Rule: for example, 0Dec.Places: for example, 0ROW4Key Figure Name: for example, DURATION1Pos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_FWDURATIONShort Name: for example, Modified DurationShift Rule: for example, 0Dec.Places: for example, 0ROW5Key Figure Name: for example, DURATION2Pos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_MACAULAYShort Name: for example, Macaulay DurationShift Rule: for example, 0Dec.Places: for example, 0and Save. | The New Entries: Overview of Added Entries screen displays allowing entry of the Key Figures name and configuration settings. |  |
| 7 | Access Key Figures Maintain screen | Go back to the Change View "Key Figure Layout": Overview screen, select the checkbox of Layout-ID Y02, then double click on the Key Figures folder in the Dialog Structure panel. |  |  |
| 8 | Maintain Key Figures of Layout | On the Change View "Key Figure Layout": Overview screen, Choose New Entries, then insert the following data in Key Figures form and Save:Key Figure Name: for example, NPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDecimal Places: for example, 0 |  |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Market Risk Key Figure Sets (AFWKF_SET) | The Change View "Market Risk Key Figure Set": Overview screen is displayed. |  |
| 3 | Define Risk Factor Set | On the Change View "Market Risk Key Figure Set": Overview screen, double click on the Risk Factor Set folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Factor Set form:RiskF. Set: for example, R01Description: for example, Risk Factor Set with FX Rate and Yld CurvesFX Risk: <select the checkbox>IR Risk: <select the checkbox>Then select the created entry, double click on the Risk Currency folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Currency form:Row 1Currency: for example, USDlR Risk: <select the checkbox>Then double click on the Interest Rate Term folder in the Dialog Structure panel on the left side. Choose New Entries,insert the following data in the Interest Rate Term form and choose Save:Row 1Term: for example, 1Time Unit: for example, MonthRow 2Term: for example, 3Time Unit: for example, MonthRow 3Term: for example, 6Time Unit: for example, MonthRow 4Term: for example, 1Time Unit: for example, Year | A new risk factor set is created. |  |
| 4 | Maintain Market Risk Key Set | Double click on the Market Risk Key Figure Set folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Market Risk Key Figure Set form and choose Save:row 1MR Key Figure Set: for example, MRK01Description: for example, Market Key Figure Set without VaREvaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <deselect>UpdUponChg: <select>Note If the UpdUponChg checkbox is selected, once a new financial object is created or changed, an automatic calculation of the market risk key figure set is triggered. The calculation only covers the updated object. The adjustment run is based on the basic run of same date that is processed by scheduled job.Row 2MR Key Figure Set: for example, MRK02Description: for example, Market Key Figure Set (VaR Hist.Sim.)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV1RiskF. Set: for example, R01Row 3MR Key Figure Set: for example, MRK03Description: for example, Market Key Figure Set (VaR MonteCarloSim.)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV2RiskF. Set: for example, R01Row 4MR Key Figure Set: for example, MRK04Description: for example, Market Key Figure Set (VaR Variance/Covariance)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV3RiskF. Set: for example, R01Note If the Calc. VaR checkbox is selected, the parameters of the VaR type and the risk factor set need to be assigned; the market data scenario or market data shift should be blank. | Market Risk Key Set is savedThe VaR type SV1 is for the VaR calculation method as historical simulation;The VaR type SV2 is for the VaR calculation method as Monte Carlo simulation;The VaR type SV3 is for the VaR calculation method as variance-covariance approach. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Limit Overview (TBL3). | The Overview of Limits screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Overview of Limits screen, enter the following data and choose Execute:Limit Type: for example, Y01 to Y09Company Code: for example, 3310 | The Display Limits for Limit Types: Overview screen is displayed. |  |

### Simulated Valuation

#### Run Simulated Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Simulated valuation key figures are used to verify how balance and P&L figures have been developing since last period end.

The simulated key figures cover all relevant valuation figures which are usually generated within the period end closing process.

Simulated valuation processing covers:

- Valuation of Treasury Positions
- Accrual calculation of dividends for relevant product type (for example, 02B MMF Accrued + Accum. Dividend)

Prerequisite

You have created a MMF transaction.

NPV values need to be stored in advance of the valuation of Treasury positions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Simulate Period-End Closing (TPM_SIM_VAL). | The Simulate Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Simulate Period-End Closing screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example,02ASecurity ID: for example, <Security Class ID Number(s) created in previous steps>, for example, MMF_AE1Security Account: for example, DE_MMFRecalculate Outdated Sim.Val.: <deselect this checkbox>Note If you set this indicator, you can recalculate the outdated simulation results.Simulation Date: for example, <the current date>Key Date Valuation: <select this checkbox>Accrual/Deferral: <deselect this checkbox>Note If you set this indicator, the accrual/deferral of expenses and revenues for the selected treasury positions is simulated, and Accrual/Deferral Parameter is displayed.Test Run: <select this checkbox> | The following message is displayed:Processed xx positions; xx successful, 0 failed.If Recalculate Outdated Simulation Results has been executed, the following message is displayed:xx simulated results deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
| 4 | Execute Simulated Valuation | The dialog Message shows up, and choose Continue. | The Simulate Period-End Closing screen is displayed.You can check the simulated valuation information for local GAAP (valuation area AE0). Please note there is no simulated valuation created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back to the initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Messages dialog box is displayed. |  |
| 6 | Execute Simulated Valuation for Production Run | The dialog Message shows up, and choose Continue. | The Simulate Period-End Closing screen is displayed.You can check the simulated valuation information for local GAAP (valuation area AE0). |  |

#### Delete Simulated Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reverse the simulated valuation you've just run.

Prerequisite

You've executed the simulated valuation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Delete Results of Simulated Period-End Closing (TPM_SIM_VAL_DEL). | The Delete Results of Simulated Period-End Closing screen is displayed. |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Recognize Dividend Distribution states the user has to run dividend accrual at least once before capitalizing it, but Accrue Dividend is stated as only applicable to product type 02B and the 02A and 02C capitalization sections are described as dividend capitalized 'without accrual'.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Table says Enter Dividend Factor 'is outside of SAP system', whereas the Enter Dividend Factor procedure directs the tester to the Enter Securities Factor Values step of test script 1XN (app Enter Factor Values TMDFACTORVAL).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-sap-s-4hana-cloud-public-edition-money-market-mutual-fund-part-02]]
- related-to :: [[05-treasury-and-cash-management/money-market-mutual-fund-management-group-ledger-ifrs-2uo-ae-874]]
- related-to :: [[05-treasury-and-cash-management/money-market-mutual-fund-management-group-ledger-us-gaap-34g-ae-911]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UN_S4CLD2608_BPD_EN_AE.docx` — lines 1–3335 of the extracted text · extracted with `mammoth` · 257,646 chars in the whole document
