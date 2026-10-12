---
id: 05-treasury-and-cash-management/test-script-interest-rate-derivatives-management-1x3-ae-sap-s-4hana-cl-part-01
title: "Test Script: Interest Rate Derivatives Management (1X3_AE) - SAP S/4HANA Cloud Public Edition (1X3_S4CLD2608_BPD_EN_AE) — part 1 of 2"
description: "Test script for scope item 1X3_AE (S/4HANA Cloud Public Edition 2608, AE): interest rate swaps, cross-currency swaps, swaptions; prerequisites and step tables."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/interest-rate-derivatives]
aliases: []
keywords: [Interest Rate Derivatives Management, interest rate swap, cross-currency interest rate swap, business partner master data, correspondence, credit limits, payment requests, general ledger posting, period-end closing, net present value]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X3_S4CLD2608_BPD_EN_AE.docx#lines-1-3127"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-775
topic: 05-treasury-and-cash-management/interest-rate-derivatives
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Interest Rate Derivatives Management (1X3_AE) - SAP S/4HANA Cloud Public Edition (1X3_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X3_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–3127 of the extracted text), extracted with `mammoth`. Grouped under **Interest Rate Derivatives Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Interest Rate Derivatives Management (1X3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 7](#_Toc232848013)

[2 Prerequisites 8](#_Toc232848014)

[2.1 System Access 8](#_Toc232848015)

[2.2 Roles 8](#_Toc232848016)

[2.3 Master Data, Organizational Data, and Other Data 9](#_Toc232848017)

[2.4 Business Conditions 10](#_Toc232848018)

[2.5 Preliminary Steps 10](#_Toc232848019)

[2.5.1 Create Business Partner 10](#_Toc232848020)

[2.5.1.1 Maintain General Data for Business Partner 10](#_Toc232848021)

[2.5.1.2 Maintain Payment Details for Business Partner 13](#_Toc232848022)

[2.5.1.3 Maintain Authorizations for Business Partner 15](#_Toc232848023)

[2.5.1.4 Maintain Derived Flows for Business Partner (Optional) 16](#_Toc232848024)

[2.5.1.5 Maintain Reporting Data in Company Code for Business Partner 17](#_Toc232848025)

[2.5.2 Correspondence 18](#_Toc232848026)

[2.5.2.1 Maintain Profile and BP Group Assignments to External Recipient 18](#_Toc232848027)

[2.5.2.2 Maintain Profile and BP Group Assignments to Internal Recipient 20](#_Toc232848028)

[2.5.3 Maintaining Credit Limit 22](#_Toc232848029)

[2.5.3.1 Maintain Limit with Limit Type Y01 22](#_Toc232848030)

[2.5.3.2 Maintain Limit with Limit Type Y07 24](#_Toc232848031)

[2.5.4 Maintain Trader and Trader Authorizations 25](#_Toc232848032)

[2.5.4.1 Define Traders 25](#_Toc232848033)

[2.5.4.2 Define User Data 26](#_Toc232848034)

[2.5.4.3 Maintain Trader Authorizations 26](#_Toc232848035)

[2.5.5 Define Fixing References 27](#_Toc232848036)

[2.5.6 Define Values for Expiry Time 30](#_Toc232848037)

[3 Overview Table 31](#_Toc232848038)

[4 Test Procedures 38](#_Toc232848039)

[4.1 Interest Rate Swap 38](#_Toc232848040)

[4.1.1 Market Data 38](#_Toc232848041)

[4.1.2 Automatic Market Rates Management (1S4) (Optional) 38](#_Toc232848042)

[4.1.3 Generate Limit Utilizations 39](#_Toc232848043)

[4.1.4 Calculate Market Risk Key Figures 40](#_Toc232848044)

[4.1.5 Check Limit Utilization Report 41](#_Toc232848045)

[4.1.5.1 Create Interest Rate Swap Contract 42](#_Toc232848046)

[4.1.6 Correspondence 47](#_Toc232848047)

[4.1.6.1 Settle Statement Status (Manual) 48](#_Toc232848048)

[4.1.6.2 Correspondence with PDF Form 49](#_Toc232848049)

[4.1.6.2.1 Send Confirmation Email/Print 50](#_Toc232848050)

[4.1.6.2.2 Check Correspondence Status 50](#_Toc232848051)

[4.1.6.2.3 Receive Incoming Confirmation 52](#_Toc232848052)

[4.1.6.2.4 Find Deal and Match Deal Details 52](#_Toc232848053)

[4.1.6.2.5 Set Settlement Status 54](#_Toc232848054)

[4.1.7 Period-End Closing 55](#_Toc232848055)

[4.1.7.1 Run Accrual 55](#_Toc232848056)

[4.1.7.2 Calculate or Maintain Fair Value of Transaction 57](#_Toc232848057)

[4.1.7.3 Perform Key Date Valuation 59](#_Toc232848058)

[4.1.8 Interest Rate Adjustment 61](#_Toc232848059)

[4.1.8.1 Interest Rate Adjustment Schedule Report 61](#_Toc232848060)

[4.1.8.2 Adjust Interest Rate 62](#_Toc232848061)

[4.1.9 Interest Payment 64](#_Toc232848062)

[4.1.9.1 Display Payment Schedule 64](#_Toc232848063)

[4.1.9.2 Interest Payment 65](#_Toc232848064)

[4.1.9.2.1 Option 1: Generate and Automatically Process Payment Request 65](#_Toc232848065)

[4.1.9.2.2 Option 2: Generate and Process Payment Request 68](#_Toc232848066)

[4.1.9.2.3 Send Payment Medium File 73](#_Toc232848067)

[4.1.9.3 Bank Initiated Payment 74](#_Toc232848068)

[4.1.9.4 Post to General Ledger 74](#_Toc232848069)

[4.1.10 Post Realized Profit and Loss 76](#_Toc232848070)

[4.2 Cross-Currency Interest Rate Swap 78](#_Toc232848071)

[4.2.1 Market Data 78](#_Toc232848072)

[4.2.2 Automatic Market Rates Management (1S4)(Optional) 78](#_Toc232848073)

[4.2.3 Generate Limit Utilizations 78](#_Toc232848074)

[4.2.4 Calculate Market Risk Key Figures 80](#_Toc232848075)

[4.2.5 Check Limit Utilization Report 81](#_Toc232848076)

[4.2.6 Create Cross-Currency Interest Rate Swap Contract 82](#_Toc232848077)

[4.2.7 Correspondence 91](#_Toc232848078)

[4.2.7.1 Set Settlement Status (Manual) 92](#_Toc232848079)

[4.2.7.2 Correspondence with PDF Form 93](#_Toc232848080)

[4.2.7.2.1 Send Confirmation Email/Print 94](#_Toc232848081)

[4.2.7.2.2 Check Correspondence Status 94](#_Toc232848082)

[4.2.7.2.3 Receive Incoming Confirmation 96](#_Toc232848083)

[4.2.7.2.4 Find Deal and Match Deal Details 96](#_Toc232848084)

[4.2.7.2.5 Set Settlement Status 98](#_Toc232848085)

[4.2.8 Principal Payment 99](#_Toc232848086)

[4.2.8.1 Fix FX Rate for Principal Payment (Optional) 99](#_Toc232848087)

[4.2.8.2 Corporate Initial Payment 100](#_Toc232848088)

[4.2.8.2.1 Option 1: Generate and Automatically Process Payment Request 100](#_Toc232848089)

[4.2.8.2.2 Option 2: Generate and Process Payment Request 104](#_Toc232848090)

[4.2.8.2.3 Send Payment Medium File 109](#_Toc232848091)

[4.2.8.3 Bank Initiated Payment 109](#_Toc232848092)

[4.2.8.4 Post to General Ledger 109](#_Toc232848093)

[4.2.9 Period-End Closing 111](#_Toc232848094)

[4.2.9.1 Run Accrual 111](#_Toc232848095)

[4.2.9.2 Calculate or Maintain Fair Value of Transaction 113](#_Toc232848096)

[4.2.9.3 Perform Key Date Valuation 115](#_Toc232848097)

[4.2.10 Interest Rate Adjustment 117](#_Toc232848098)

[4.2.10.1 Interest Rate Adjustment Schedule Report 117](#_Toc232848099)

[4.2.10.2 Adjust Interest Rate 118](#_Toc232848100)

[4.2.11 Interest Payment 120](#_Toc232848101)

[4.2.11.1 Fix FX Rate for Interest Payment (Optional) 120](#_Toc232848102)

[4.2.11.2 Display Payment Schedule 121](#_Toc232848103)

[4.2.11.3 Corporate Initial Payment 122](#_Toc232848104)

[4.2.11.3.1 Option1: Generate and Automatically Process Payment Request 122](#_Toc232848105)

[4.2.11.3.2 Option2: Generate and Process Payment Request 126](#_Toc232848106)

[4.2.11.3.3 Send Payment Medium File 130](#_Toc232848107)

[4.2.11.4 Bank Initiated Payment 131](#_Toc232848108)

[4.2.11.5 Post to General Ledger 131](#_Toc232848109)

[4.2.12 Final Repayment 133](#_Toc232848110)

[4.2.12.1 Fix FX Rate for Final Repayment (Optional) 134](#_Toc232848111)

[4.2.12.2 Display Payment Schedule 135](#_Toc232848112)

[4.2.12.3 Corporate Initial Payment 136](#_Toc232848113)

[4.2.12.3.1 Option 1: Generate and Automatically Process Payment Request 136](#_Toc232848114)

[4.2.12.3.2 Option 2: Generate and Process Payment Request 139](#_Toc232848115)

[4.2.12.3.3 Send Payment Medium File 144](#_Toc232848116)

[4.2.12.4 Bank Initiated Payment 144](#_Toc232848117)

[4.2.12.5 Post to General Ledger 144](#_Toc232848118)

[4.2.13 Post Realized Profit and Loss 146](#_Toc232848119)

[4.3 Swaption 148](#_Toc232848120)

[4.3.1 Market Data 148](#_Toc232848121)

[4.3.2 Check Limit Utilization Report 149](#_Toc232848122)

[4.3.3 Create Swaption Contract 150](#_Toc232848123)

[4.3.3.1 Create Interest Rate Swaption 150](#_Toc232848124)

[4.3.3.2 Create Cross-Currency Interest Rate Swaption 153](#_Toc232848125)

[4.3.4 Correspondence 156](#_Toc232848126)

[4.3.4.1 Set Settlement Status (Manual) 156](#_Toc232848127)

[4.3.4.2 Correspondence with PDF Form 158](#_Toc232848128)

[4.3.4.2.1 Send Confirmation Email/Print 158](#_Toc232848129)

[4.3.4.2.2 Check Correspondence Status 159](#_Toc232848130)

[4.3.4.2.3 Receive Incoming Confirmation 160](#_Toc232848131)

[4.3.4.2.4 Find Deal and Match Deal Details 161](#_Toc232848132)

[4.3.4.2.5 Set Settlement Status 162](#_Toc232848133)

[4.3.5 Premium Payment 163](#_Toc232848134)

[4.3.5.1 Option 1: Generate and Automatically Process Payment Request 163](#_Toc232848135)

[4.3.5.2 Option 2 : Generate and Process Payment Request 167](#_Toc232848136)

[4.3.5.2.1 Generate Payment Request 167](#_Toc232848137)

[4.3.5.2.2 Process Payment Request 169](#_Toc232848138)

[4.3.5.3 Send Payment Medium File 172](#_Toc232848139)

[4.3.5.4 Bank-Initiated Payment 172](#_Toc232848140)

[4.3.5.5 Post to General Ledger 173](#_Toc232848141)

[4.3.6 Period-End Closing 175](#_Toc232848142)

[4.3.6.1 Maintain Fair Value of Transaction 175](#_Toc232848143)

[4.3.6.2 Perform Key Date Valuation 177](#_Toc232848144)

[4.3.7 Transaction is Mature 178](#_Toc232848145)

[4.3.7.1 Review Swaption Status 179](#_Toc232848146)

[4.3.7.1.1 Decide to Exercise 179](#_Toc232848147)

[4.3.7.1.2 Create Interest Rate Swap Contract 180](#_Toc232848148)

[4.3.7.1.3 Decide to Expire 182](#_Toc232848149)

[4.3.7.2 Post Realized Profit and Loss 183](#_Toc232848150)

[4.4 Reports 185](#_Toc232848151)

[4.4.1 Display Treasury Posting Journal 185](#_Toc232848152)

[4.4.2 Treasury Position Analysis 185](#_Toc232848153)

[4.4.3 Display Treasury Position Values 186](#_Toc232848154)

[4.4.4 Define Financial Positions 187](#_Toc232848155)

[4.4.5 Financial Status (Book Value) 189](#_Toc232848156)

[4.4.6 Financial Status (Nominal Amount) 189](#_Toc232848157)

[4.4.7 Display Treasury Payments 190](#_Toc232848158)

[4.4.8 Display Treasury Position Flows 191](#_Toc232848159)

[4.4.9 Display Treasury Alerts - Posting 192](#_Toc232848160)

[4.4.10 Display Treasury Alerts - Settlement, Release, Correspondence, and Interest Rates 193](#_Toc232848161)

[4.4.11 Display Payment Schedule 194](#_Toc232848162)

[4.4.12 Analyze NPV 195](#_Toc232848163)

[4.4.13 Calculate Market Risk Key Figures 196](#_Toc232848164)

[4.4.14 Sensitivity Key Figures 197](#_Toc232848165)

[4.4.15 Review Limit Utilization Report 198](#_Toc232848166)

[4.4.16 Review Interest Rate Overview 199](#_Toc232848167)

[5 Appendix 201](#_Toc232848168)

[5.1 Job Scheduling 201](#_Toc232848169)

[5.1.1 Generate Limit Utilizations 201](#_Toc232848170)

[5.1.2 Send Correspondence 203](#_Toc232848171)

[5.1.3 Adjust Interest Rate 204](#_Toc232848172)

[5.1.4 Update Planned Records 206](#_Toc232848173)

[5.1.5 Generate Payment Request 208](#_Toc232848174)

[5.1.6 Post Flows to General Ledger 210](#_Toc232848175)

[5.1.6.1 Template - Fix, Pay and Post Flows 210](#_Toc232848176)

[5.1.6.2 Template - Process Business Transactions 212](#_Toc232848177)

[5.1.7 Run Accrual 214](#_Toc232848178)

[5.1.8 Calculate Fair Value of Transaction 216](#_Toc232848179)

[5.1.9 Key Date Valuation 218](#_Toc232848180)

[5.1.10 Post Realized Profit and Loss 220](#_Toc232848181)

[5.1.11 Calculate Market Risk Key Figures 222](#_Toc232848182)

[5.2 Output Management 224](#_Toc232848183)

[5.2.1 Output Parameter Determination 224](#_Toc232848184)

[5.2.2 Manage Output Items 227](#_Toc232848185)

[5.2.3 Maintain Print Queues 228](#_Toc232848186)

[5.2.4 Display Email Transmissions 229](#_Toc232848187)

[5.2.5 Maintain Email Template 230](#_Toc232848188)

[5.2.6 Maintain Form Template 231](#_Toc232848189)

[5.3 Accounting 233](#_Toc232848190)

[5.3.1 Reverse Accrual 233](#_Toc232848191)

[5.3.2 Reverse Valuation 234](#_Toc232848192)

[5.3.3 Account Assignment Reference Transfer 236](#_Toc232848193)

[5.3.4 Reverse Account Assignment Reference Transfer 237](#_Toc232848194)

[5.4 Interest Rate Adjustment 239](#_Toc232848195)

[5.4.1 Change Adjustment (Interest Rates/Prices) 239](#_Toc232848196)

[5.4.2 Display Adjustment (Interest Rates/Prices) 240](#_Toc232848197)

[5.4.3 Reverse Automatic Adjustmests (Interest Rates/Prices) 240](#_Toc232848198)

[5.4.4 Reverse Adjustment (Interest Rates/Prices) 241](#_Toc232848199)

[5.5 Market Risk Analyzer 242](#_Toc232848200)

[5.5.1 Manage Market Data Shift 242](#_Toc232848201)

[5.5.2 Maintain Scenarios 243](#_Toc232848202)

[5.5.3 Defining Report Layout for Calculate Market Risk Key Figures 244](#_Toc232848203)

[5.5.4 Manage Market Risk Key Figure Sets 247](#_Toc232848204)

[5.6 Credit Risk Analyzer 250](#_Toc232848205)

[5.6.1 Display Limit Overview 250](#_Toc232848206)

[5.7 Change Counterparty 251](#_Toc232848207)

[5.7.1 Change Counterparty of Financial Transaction 251](#_Toc232848208)

[5.7.2 Display Financial Transactions with Changed Counterparty 252](#_Toc232848209)

[5.8 Simulated Valuation 253](#_Toc232848210)

[5.8.1 Run Simulated Valuation 253](#_Toc232848211)

[5.8.2 Delete Simulated Valuation 255](#_Toc232848212)

## Purpose

Overview

The interest rate derivatives management process helps you to manage your interest rate risks. The functionality helps you to automate labor-intensive processes, such as confirmation of financial transactions and accounting postings, giving you more time to focus on value-added activities.

The process includes the products interest rate swaps (payer, receiver, and basis), and cross-currency interest rate swaps (payer, receiver, and basis).

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
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Treasury Specialist - Front Office | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |
| Treasury Specialist - Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE | Treasury Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE |  |
| Treasury Accountant | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |
| Treasury Risk Manager | SAP_BR_TREASURY_RISK_MANAGER | Treasury Analytics | SAP_BR_TREASURY_RISK_MANAGER |  |
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| COMPANY CODE | 3310 |  |  |
| CURRENCY | AED |  |  |
| FOREIGN CURRENCY 1 | USD |  |  |
| BUSINESS PARTNER | 33537001 |  |  |
| VALUATION AREA | AE 0 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) Script

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1XN - Market Rates Management – Manually via Upload | Market data must be created. |
| J60 - Accounts Payable | Execute Prerequisites in J60 to define the Payment Medium Format (PMF) variants. Prerequisites > Preliminary Steps > Define Payment Medium Format Variants |

### Preliminary Steps

Use

The following procedures maintain the necessary data for business partners and must be completed before you can run the subsequent test steps.

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

In this step, you maintain the general data for a business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Enter Data on Initial View | Choose Organization. | The Create Organization view displays. |  |
| 4 | Enter address data | Enter the following data:Business Partner: for example, 33537001Grouping: select Treasury partner (external)Create in BP role: select Business Partner (Gen.)Title: select CompanyName: for example, Bank 1 - SAMPLE BANKSalutation: for example, Bank 1Search Term 1/2: for example, Bank 1Street/House number: for example, <Street, House number>Postal Code/City: for example, <Postal Code, City>Ctry/Reg.: AELanguage: ArabicE-Mail: for example, <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, <Dec 31 of the year 9999>and choose Save.Stay in the view for subsequent steps. | The business partner is created successfully. |  |
| 5 | Switch to Change Mode | Choose Switch Between Display and Change, and enter following data:Change in BP role: Counterparty | More counterparty related tabs such as Legal Data, Rating appear. |  |
| 6 | Enter Legal Data | Choose Navigation Menu > Legal Data. Enter the following data and choose Save:Country/Region: AENote The navigation menu is on the right side of the view. It displays as …, which is right next to the symbol >Stay in the view for subsequent steps. | The legal data is entered and saved.Change Organization: 33537001 , new role Counterparty view displays. |  |
| 7 | Enter Payment Transaction Data | Choose Navigation Menu > Payment Transactions. Enter following data for each row:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, 18121976Bank acct: <Bank account>IBAN: Choose the IBAN button and choose Continue in the IBAN dialog box.Row 2:ID: for example, USD1C/R: for example, AEBank Key: for example, 18121976Bank account: for example, <Bank account>IBAN: choose IBAN button and choose Continue in the IBAN dialog box.Note If an Information dialog box appears when you choose IBAN, please choose ContinueNow choose Save. | The payment transaction data is entered and the business partner is saved. |  |

##### Maintain Payment Details for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the payment details for a business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: view is displayed. |  |
| 3 | Choose Business Partner | Choose Open BP. In the dialog box, enter the following data, and choose Enter:Business Partner: 33537001 |  |  |
| 4 | Change Mode | Choose Switch Between Display and Change. | The Change Organization:33537001, role Counterparty view displays. |  |
| 5 | Change BP Role | Make the following entries, and choose Enter:Change in BP Role: Counterparty |  |  |
| 6 | Choose Company Code | Choose Company Code.Note You may have to use the More dropdown list to see more options, such as the Company Code. |  |  |
| 7 | Enter Criteria | Make the following entries, and choose Enter:Company Code: for example, 3310 |  |  |
| 8 | Enter SI: Payment Details | On the SI: Payment Details tab, use the information in the Payment Details Data table to make four rows of entries.Note If the system displays a dialog box with the following message: Business partner proposed as payer/payee (see long text)Display this message for this business partner again? choose No.Stay in this view for subsequent steps. | The SI: payment details are entered. |  |
| 9 | Assign Payment details | To assign payment details, for example, select the checkbox for the first row (for example, AED, AEDI) and choose Assign. | The Counterparty Change: Payment Details Assignment dialog box displays. |  |
| 10 | Assign Payment details | Choose Select All Incoming. | The AEDI value displays under PmntID-Inc. |  |
| 11 | Assign Payment details | Choose Continue to close the dialog box. | The Change Organization:33537001, role Counterparty view displays. |  |
| 12 | Assign Payment details | Select the checkbox for the second row (for example, AED, AEDO) and choose Assign. | The Counterparty Change: Payment Details Assignment dialog box displays. |  |
| 13 | Assign Payment details | Choose Select All Outgoing. | The AEDO value displays under P-ID Outg. |  |
| 14 | Assign Payment details | Choose Continue to close the dialog box. | The Change Organization:33537001, role Counterparty view displays. |  |
| 15 | Assign Payment details | Repeat the prior six steps for the remaining two rows, then choose Save. | Payment details and the assignments are saved. |  |

Table 2: Payment Details Data

| Currency | Pay.Det.ID | House Bank | Account ID | Payer/ee | Partner Bank | Payment request | Payment methods |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AED | AED I | AEBK1 | AEAC1 | <leave blank> | <leave blank> | <deselect> | <leave blank> |
| AED | AED O | AEBK1 | AEAC1 | 33537001 | AED 1 | <select> | T |
| USD | USD I | AEBK1 | USDAC | <leave blank> | <leave blank> | <deselect> | <leave blank> |
| USD | USD O | AEBK1 | USDAC | 33537001 | USD 1 | <select> | F |

##### Maintain Authorizations for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the authorization data for a business partner for SAP Treasury Risk Management.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: view, choose Open BP, in the Open business partner dialog box, enter following data:Business Partner: 33537001and choose Enter.Choose Switch Between Display and Change, and enter the following data:Change in BP Role: select TR0151 Counterparty | Change Organization: 33537001 , role Counterparty view is displayed. |  |
| 4 | Enter SI: Authorizations Data | On the Change Organization:33537001, role Counterparty view, choose Company Code, choose SI: Authorizations, enter the following:Derivatives: select the Auth. checkboxand choose Save.Note You can provide authorization to a specific product type and transaction type by expanding the folders. For testing purpose, all authorizations are given to all product types and transaction types. | The authorizations data is saved. |  |

##### Maintain Derived Flows for Business Partner (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain derived flow data for Business Partner. You set a specific derived procedure for a product type and transaction type combination.

You need to run this step first if you want to test single currency payment for cross-currency interest rate swap.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: view is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: view, choose Open BP. In the Open business partner dialog box, enter following data, and choose Enter:Business Partner: 33537001Choose Switch Between Display and Change, and enter following data:Change in BP Role: TR0151 Counterparty | The Change Organization:33537001, role Counterparty view is displayed. |  |
| 4 | Enter Procedure | On the Change Organization:33537001, role Counterparty view, choose Company Code, and choose the SI:Derived Flows tabOn the SI: Derived Flows tab, in the Trans. Hierarchy column, choose the Derivatives folder and expand it. Make the assignment in the following path:Derivatives > Swap > 62B Cross-curr.Int.Rate Swap (CCS) > 300 Payer: NTALL “Swap: Net Int.and Nom.”Save the change. | The procedure is entered and saved. |  |

##### Maintain Reporting Data in Company Code for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure describes the steps to maintain company relationships for a business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: view displays. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: view, choose Open BP, in the popup dialog box, enter following data:Business Partner: 33537001and choose Enter.Choose Switch Between Display and Change, and enter following data:Change in BP Role: choose TR0151 Counterparty | Change Organization: 33537001 , role Counterparty view displays. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization:33537001, role Counterparty view, choose Company Code, choose Reporting Data in Company Code, and enter following data:Comp. Rel.: for example, 3 Otherand choose Save.Note When you don't find Reporting Data in Company Code on the view, choose Navigation Menu and select it from the dropdown menu.Note Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itThese are used to derive the correct G/L accounts. | The reporting data is entered and saved. |  |

#### Correspondence

Purpose

SAP Treasury Risk Management provides standard correspondence functionality. With this correspondence functionality, whenever a treasury risk management transaction is saved, you designate whether the system sends an e-mail to the business partner or automatically prints out a form to a printer.

To use this correspondence functionality, the following data must be assigned to business partner:

- Business Partner Profile
- Business Partner group

##### Maintain Profile and BP Group Assignments to External Recipient

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Business partner profiles and business partner groups controls the correspondence activities in SAP Treasury Risk Management.

SAP has predefined following business partner profiles:

PR_EMAIL

PR_PRINT

You assign these predefined business partner profiles to your business partner. For example, if the communication with your business partner is via e-mail, you assign PR_EMAIL to your business partner. When the communication is made using a printed document, then you assign PR_PRINT.

SAP has predefined following Business Partner groups:

BPG_DEFAULT

You can assign this Business partner group to your Business Partner. You can also use SSCUIs Define Business Partner Group and Assign Attributes for Business Partner Groups to add your own Business partner group and assign appropriate attributes according to your specific requirement. Different business partner profiles and BP groups could be assigned to the same business partner.

In this step, you assign business partner profiles and BP groups to an external business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign Profile and BP Group - External Recipients (FTR_EXT_ASSIGN). | The Assignment of Profiles and BP Groups to External Recipients: view displays. |  |
| 3 | Enter Business Partner Data on the View | On the left side of Assignment of Profiles and BP Groups to External Recipients: view, choose Insert Row and enter the following data, and press Enter:BusPartner: for example, 33537001CoCd: for example, 3310Recpt/Send Type: for example, COUNTERPARTY. | The business partner information is entered. |  |
| 4 | Assign Business Profile and BP Group to the Business Partner | On the top-right of the Assignment of Profiles and BP Groups to External Recipients view, choose Expand Node to expand BP:0033537001 /CoCd:3310/ Rec/SendType: COUNTERPARTY > Derivatives > SWAP > 62A Interest Rate Swap(IRS) > 300 Payer, and select 20 Contract.On the bottom-right side of the Assignment of Profiles and BP Groups to Internal Recipients: view,choose Insert Row and enter the following data:Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTChoose Insert Row again and add another entry as follows:Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTand choose Save.Remember Typically, you only assign one profile to a Product type/Transaction type/Activity Category. | Business partner profiles and BP groups are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat Process for Additional Types and Categories | Select the item 33537001 in the left side view, and choose Modify Row.Repeat the previous steps for the following items:62A/300/2062A/301/2062A/302/2062A/303/2062B/300/2062B/301/2062B/302/2062B/303/2076T/100/2076T/200/2076V/100/2076V/200/20 | For all the listed Product Types/Transaction Types/Activity Categories, BP profiles and BP groups are assigned. |  |

##### Maintain Profile and BP Group Assignments to Internal Recipient

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Internal Recipient ID is predefined by SAP. It could be linked to SAP User ID(s). Once it's linked to an SAP user ID, whenever an internal correspondence object is generated, SAP Treasury Risk Management sends correspondence information to the address of the SAP User ID. Depending on the different profiles (PR_EMAIL /PR_PRINT), E-mail is sent to the user's email address or a form is printed out.

This procedure describes assigning business partner profiles and BP groups to an internal business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign Profile and BP Group - Internal Recipients (FTR_INT_ASSIGN). | The Assignment of Profiles and BP Groups to Internal Recipients: view displays. |  |
| 3 | Enter Business partner data on the view | On the left side of Assignment of Profiles and BP Groups to Internal Recipients view, choose Insert Row and enter the following data:IntRec: for example, INT.RECPCoCd: for example, 3310Recpt/Send Type: for example, INTERNAL | The Business Partner information is entered. |  |
| 4 | Assign Business profile and BP group to the Business Partner | Double click on the row newly inserted.On the top-right side of the Assignment of Profiles and BP Groups to Internal Recipients view, expand BP:INT. RECP /CoCd: <Company Code> / Rec/SendType: INTERNAL > Derivatives > SWAP > 62A Interest Rate Swap (IRS) > 300 Payer , and select 20 Contract.On the bottom-right side of theAssignment of Profiles and BP Groups to Internal Recipients view, choose Insert Row, and enter the following data:Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTUser Name: select a <User ID>.Choose Save.Choose Insert Row again and add another entry as follows:Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTUser Name: select a User IDChoose Save.Note The <User ID> is a backend user ID. | Business partner profile and BP group and user ID are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat for Additional Types and Categories | Select the item INT.RECP in the left side view, and choose Modify Row.Repeat the previous step for following items:Product TypesTransaction TypesActivity Categories62A3002062A3012062A3022062A3032062B3002062B3012062B3022062B3032076T1002076T2002076V1002076V20020 | BP profiles and BP groups and user IDs are assigned to all the listed Product Types/Transaction Types/ Activity Categories. |  |

>

#### Maintaining Credit Limit

Purpose

A serial of limit types has been created in system, you maintain credit limit based on specified limit type according to business. In following procedures, limit type Y01 and Y07 are maintained.

##### Maintain Limit with Limit Type Y01

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

##### Maintain Limit with Limit Type Y07

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the limit characteristics for limit type Y07.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Limits (TBL1). | The view is displayed. |  |
| 3 | Choose Limit Type | Select the Limit type Y07 row and choose Create Limits. |  |  |
| 4 | Edit Limits | Make the following entries, and choose Continue:Company Code: for example, 3310BusPartner: for example,33537001 | The Edit Limits for Limit Type Y07: Create New Limit view is displayed. |  |
| 5 | Create Internal Limit Amount and External Limit Amount | Enter the following data, and choose Save:Valid From Date: for example, <the current date>Valid To (Internal): for example, 12/31/9999Valid To (External): for example, <the current date + 1 year>Limit Currency: for example, AEDInternal Limit Amnt: for example, 250,000,000External Limit Amnt: for example, 200,000,000Critical Limit Utilizat.: for example, 90%Max. Risk Commit Per. Mth: for example, 999Limit: for example, Check |  |  |

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

In this step, you define traders for treasury transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Risk Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define Traders (S_ALR_87009302). | The Determine Work Area: Entry dialog box is displayed. |  |
| 3 | Enter Work Area | Enter the following data, and choose Continue:Company Code: for example, 3310 | The Change View "Treasury: Traders": Overview view is displayed. |  |
| 4 | Create a New Record | Choose New Entries, enter the following data, and choose Save.Trader: for example: TRADER02 | The data is saved. |  |

##### Define User Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you map users with traders, providing a default trader when creating a new transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Risk Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define User Data (S_ALR_87007933). | The Change View "Treasury: User master data supplements": Overview view is displayed. |  |
| 3 | Create a New Record | Choose New Entries, enter the following data, and choose Save:User ID: for example: <User ID>Trader: for example: TRADER02 | The data is saved. |  |

##### Maintain Trader Authorizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once traders are defined, the procedure allows you to define authorization for those traders.

Prerequisite

A trader must be defined before this step. The previous procedure, [Define Traders](#unique_19) [page ] 25, provides the steps to define a trader.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Trader Authorizations (TBT1). | The Create/Change Trans. Authorization for Trader: Init. screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Enter:Trader: for example: TRADER02Company Code: for example: 3310 | The Create/Change Transaction Authorization for Traders view displays. |  |
| 4 | Enter Authorization and Save | Select or deselect within the Authorization column and choose Save.Note Ensure to authorize TRADER02 for the Derivativestransactions. | The data is saved as indicated by a message. For example: Transaction authorizations for trader TRADER02 are being saved |  |

#### Define Fixing References

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For Swift format MT300, there is a new mandatory field called 14S: Settlement Rate Source. This field entry describes whether the fixing exchange rate is:

- Governed by EMTA template (For example, :14S:EMT00), or
- Negotiated with the counterparty and explicitly described (For example,:14S:EUR2/1600/GBLO)

To derive this field, you must define fixing references. Enter the fixing references in each NDF transaction. SAP delivers three fixing reference categories:

- 1: General Fixing Reference
- 2: EMTA Fixing Reference
- 3: Compound Fixing Reference

The first two fixing reference categories are the basic fixing reference categories, which can be used when defining fixing reference IDs for the third category. You can define fixing reference IDs for categories 1 and 2 directly. However, to define the fixing reference ID for category 3, you must define the basic fixing reference IDs. You can then use those basic fixing reference IDs to define the compound fixing reference ID.

Procedure

Table 3: Define General Fixing Reference and EMTA Fixing Reference

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Define Fixing Reference (FTR_FIX_DEF). | The Change View "Define Fixing References": Overview screen is displayed. |  |
| 3 | Create Fixing Reference IDs | Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Create Fixing Reference IDs | Make the entries from the Fixing Reference ID table below (each on a separate row) and choose Save. | On the New Entries: Overview of Added Entries screen, the system displays the message Data was saved. |  |

Table 4: Fixing Reference ID Table

| Fixing Reference ID | Fixing Reference Description | Leading Currency | Following Currency | Fixing Reference Category | Source | Location | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ECB37 AED / USD | ECB37 AED / USD | AED | USD | 1 General Fixing Reference | AED 1 | DECB | 14:15 |
| WM/REUTERS AED / USD 4 PM | WM/REUTERS AED / USD 4 PM | AED | USD | 1 General Fixing Reference | AED 2 | GBLO | 16:00 |
| KFTC18 ( KRW 02) | KFTC18 ( KRW 02) | USD | KRW | 2 EMTA Fixing Reference | Leave blank | Leave blank | Leave blank |
| PTAX ( BRL 09) | BRL PTAX ( BRL 09) | USD | BRL | 2 EMTA Fixing Reference | Leave blank | Leave blank | Leave blank |

Table 5: Define Compound Fixing Reference

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Define Fixing Reference (FTR_FIX_DEF). | The Change View "Define Fixing References": Overview screen is displayed. |  |
| 3 | Create Fixing Reference IDs | Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Create Fixing Reference IDs | Make the following entries:First Row:Fixing Reference ID: PTAX( BRL 09) -WM/REUTERS AED / USDFixing Reference Description: BRL PTAX (BRL09) - WM/REUTERS AED/USD 4 PMLeading Currency: AEDFollowing Currency: BRLFixing Reference Category: 3 Compound Fixing ReferenceSource: <leave blank>Location: <leave blank>Time: <leave blank> |  |  |
| 5 | Create Fixing Reference IDs | Select the checkbox at the beginning of this row and double click on Specify Compound Fixing Reference Details folder in the left pane.Note Compound Fixing Reference Details can only be specified for a Fixing Reference ID of category 3 (Compound Fixing Reference). |  |  |
| 6 | Create Fixing Reference IDs | Make the following entries and choose Save:Row 1:Fixing Reference ID: PTAX ( BRL 09)Sequence Number: 1Row2:Fixing Reference ID: WM/REUTERS AED / USD 4 PMSequence Number: 2 | On the New Entries: Overview of Added Entries screen, the system displays the message Data was saved.You defined the necessary fixing reference IDs. |  |

#### Define Values for Expiry Time

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

For Swift format MT305, there is a mandatory field called 31G: Expiry Details. This field specifies the date, time and location at which the option expires. In this step, you assign times to locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Define Values for Expiry Time - OTC Option (FTR_EXPIRY_TIME_DEF). | The "Assign Times to Locations": Change screen is displayed. |  |
| 3 | Assign Expiry Times to Locations | Choose New Entries. | The New Entries: Added Entries screen is displayed. |  |
| 4 | Assign Expiry Times to Locations | Make the following entries and choose Save:Location: for example, DEFRTime: for example, 15:00Location: for example, DECBTime: for example, 16:00 | On the New Entries: Added Entries screen, the system displays the message Data already saved. |  |

## Overview Table

This scope item consists of process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Interest Rate Swap

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Market Data](#unique_25) [page ] 38 |  | Execute all procedures in the Market Rates Management – Manually via Upload (1XN) test script. | Market data is maintained, such as foreign currency exchange spot rates, swap rates, reference interest rates, and so on. |
| [Automatic Market Rates Management (1S4) (Optional)](#unique_26) [page ] 38 |  | Execute all procedures in the Automatic Market Rates Management (1S4) test script. | Market data is prepared. |
| [Generate Limit Utilizations](#unique_27) [page ] 39 | Treasury Specialist - Middle Office | End-of-Day Processing (KLNACHT) | Limit utilizations was determinate and updated based on daily transactions and positions contained in the data pool. |
| [Calculate Market Risk Key Figures](#unique_28) [page ] 40 | Treasury Specialist - Middle Office | Calculate Market Risk Key Figures (AISGENKF) | The single value analysis of assigned report layout displays. |
| [Check Limit Utilization Report](#unique_29) [page ] 41 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | Limit utilizations display. |
| [Create Interest Rate Swap Contract](#unique_30) [page ] 42 | Treasury Specialist - Front Office | Create IR Derivative (TO01) | Interest rate swap contract is created. |
| [Settle Statement Status (Manual)](#unique_31) [page ] 48 | Treasury Specialist - Back Office | Process IR Derivatives - Collective Processing (TI92) | The TRM transaction is settled. |
| Send Confirmation Email / Print / FAX[Send Confirmation Email/Print](#unique_32) [page ] 50 |  |  | Confirmation correspondences are in delivered status |
| [Check Correspondence Status](#unique_33) [page ] 50 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The status of correspondence objects displays. |
| [Receive Incoming Confirmation](#unique_34) [page ] 52 | Treasury Specialist - Back Office |  |  |
| [Find Deal and Match Deal Details](#unique_35) [page ] 52 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | An incoming correspondence is created. |
| [Set Settlement Status](#unique_36) [page ] 54 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The TRM transaction is settled. |
| [Run Accrual](#unique_37) [page ] 55 | Treasury Accountant | Run Accrual/Deferral (TPM44) | Interest expenses and interest income are accrued and posted based on assigned time period. |
| [Calculate or Maintain Fair Value of Transaction](#unique_38) [page ] 57 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA) | The fair value of transaction is calculated automatically, or maintained manually. |
| [Perform Key Date Valuation](#unique_39) [page ] 59 | Treasury Accountant | Run Valuation (TPM1) | The financial instrument is valued, related FI document is posted. |
| Interest Rate Adjustment Schedule Report[Perform Key Date Valuation](#unique_39) [page ] 59 | Treasury Specialist - Back Office | Adjustment Schedule - Rates/Prices (TJ07) | The interest rate adjustment schedule displays |
| [Adjust Interest Rate](#unique_40) [page ] 62 | Treasury Specialist - Back Office | Run Automatic Adjustments - Rates/Prices (TJ05)/ Create Adjustment - Rates/Prices (TI10) | The interest rate of transaction is changed automatically or manually. |
| [Display Payment Schedule](#unique_41) [page ] 64 | Treasury Accountant | Display Payment Schedules (TJ04) | Payment Schedule displays |
| [Option 1: Generate and Automatically Process Payment Request](#unique_42) [page ] 65 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_43) [page ] 68 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_44) [page ] 70 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Post to General Ledger](#unique_45) [page ] 74 | Treasury Accountant | Fix, Pay and Post Flows (TBB1) | FI document is posted. |
| [Post Realized Profit and Loss](#unique_46) [page ] 76 | Treasury Accountant | Post Derived Business Transactions (TPM18) | Accounting document has been created in local GAAP (valuation area AE0) |

Cross Currency Interest Rate Swap

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Market Data](#unique_47) [page ] 78 |  | Execute all procedures in the Market Rates Management – Manually via Upload (1XN) test script. | Market data is maintained, such as foreign currency exchange spot rates, swap rates, reference interest rates, and so on. |
| [Automatic Market Rates Management (1S4)(Optional)](#unique_48) [page ] 78 |  | Execute all procedures in the Automatic Market Rates Management (1S4) test script. | Market data is prepared. |
| [Generate Limit Utilizations](#unique_49) [page ] 78 | Treasury Specialist - Middle Office | End-of-Day Processing (KLNACHT) | Limit utilizations was determinate and updated based on daily transactions and positions contained in the data pool. |
| [Calculate Market Risk Key Figures](#unique_50) [page ] 80 | Treasury Specialist - Middle Office | Calculate Market Risk Key Figures (AISGENKF) | The single value analysis of assigned report layout displays. |
| [Check Limit Utilization Report](#unique_51) [page ] 81 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | Limit utilizations display. |
| [Create Cross-Currency Interest Rate Swap Contract](#unique_52) [page ] 82 | Treasury Specialist - Front Office | Create IR Derivative (TO01) | Cross currency interest rate swap contract is created. |
| [Set Settlement Status (Manual)](#unique_53) [page ] 92 | Treasury Specialist - Back Office | Process IR Derivatives - Collective Processing (TI92) | The TRM transaction is settled. |
| [Send Confirmation Email/Print](#unique_54) [page ] 94 |  |  | Confirmation correspondences are in delivered status |
| [Check Correspondence Status](#unique_33) [page ] 50 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The status of correspondence objects displays. |
| [Receive Incoming Confirmation](#unique_55) [page ] 96 | Treasury Specialist - Back Office |  |  |
| [Find Deal and Match Deal Details](#unique_56) [page ] 96 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | An incoming correspondence is created. |
| [Set Settlement Status](#unique_57) [page ] 98 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The TRM transaction is settled. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_58) [page ] 100 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_59) [page ] 104 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_60) [page ] 106 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_61) [page ] 109 |  |  |  |
| [Post to General Ledger](#unique_62) [page ] 109 | Treasury Accountant | Fix, Pay and Post Flows (TBB1)/ Process Business Transactions (TPM10) | FI document is posted. |
| [Run Accrual](#unique_63) [page ] 111 | Treasury Accountant | Run Accrual/Deferral (TPM44) | Interest expenses and interest income are accrued and posted based on assigned time period. |
| [Calculate or Maintain Fair Value of Transaction](#unique_64) [page ] 113 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA) | The fair value of transaction is calculated automatically, or maintained manually. |
| [Perform Key Date Valuation](#unique_65) [page ] 115 | Treasury Accountant | Run Valuation (TPM1) | The financial instrument is valued, related FI document is posted. |
| [Interest Rate Adjustment Schedule Report](#unique_66) [page ] 117 | Treasury Specialist - Back Office | Adjustment Schedule - Rates/Prices (TJ07) | The interest rate adjustment schedule displays |
| [Adjust Interest Rate](#unique_67) [page ] 118 | Treasury Specialist - Back Office | Run Automatic Adjustments - Rates/Prices (TJ05)/ Create Adjustment - Rates/Prices (TI10) | The interest rate of transaction is changed automatically or manually. |
| [Display Payment Schedule](#unique_68) [page ] 121 | Treasury Accountant | Display Payment Schedules (TJ04) | Payment Schedule displays |
| [Option1: Generate and Automatically Process Payment Request](#unique_69) [page ] 122 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_70) [page ] 126 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_71) [page ] 128 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_72) [page ] 131 |  |  |  |
| [Post to General Ledger](#unique_73) [page ] 131 | Treasury Accountant | Fix, Pay and Post Flows (TBB1) / Process Business Transactions (TPM10) | FI document is posted. |
| Display Payment Schedule (Final repayment)[Display Payment Schedule](#unique_74) [page ] 135 | Treasury Accountant | Display Payment Schedules (TJ04) | Payment Schedule displays |
| [Option 1: Generate and Automatically Process Payment Request](#unique_75) [page ] 136 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_76) [page ] 139 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_77) [page ] 141 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Automatic Payment Transactions for Payment Requests (F111) |
| [Bank Initiated Payment](#unique_78) [page ] 144 |  |  |  |
| [Post to General Ledger](#unique_79) [page ] 144 | Treasury Accountant | Fix, Pay and Post Flows (TBB1) / Process Business Transactions (TPM10) | FI document is posted. |
| [Post Realized Profit and Loss](#unique_80) [page ] 146 | Treasury Accountant | Post Derived Business Transactions (TPM18) | Accounting document has been created in local GAAP (valuation area AE0) |

Swaption

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Market Data](#unique_81) [page ] 148 |  | Execute all procedures in the Market Rates Management – Manually via Upload (1XN) test script. | Market data is maintained, such as foreign currency exchange spot rates, swap rates, reference interest rates, and so on. |
| [Check Limit Utilization Report](#unique_82) [page ] 149 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | Limit utilizations display. |
| [Create Interest Rate Swaption](#unique_83) [page ] 150 | Treasury Specialist - Front Office | Create OTC Option (TI71) | Interest rate swaption contract is created. |
| [Create Cross-Currency Interest Rate Swaption](#unique_84) [page ] 153 | Treasury Specialist - Front Office | Create OTC Option (TI71) | Cross currency interest rate swaption contract is created. |
| [Set Settlement Status (Manual)](#unique_85) [page ] 156 | Treasury Specialist - Back Office | Process IR Derivatives - Collective Processing (TI92) | The TRM transaction is settled. |
| [Send Confirmation Email/Print](#unique_86) [page ] 158 |  |  | Confirmation correspondences are in delivered status. |
| [Check Correspondence Status](#unique_33) [page ] 50 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The status of correspondence objects displays. |
| [Receive Incoming Confirmation](#unique_87) [page ] 160 | Treasury Specialist - Back Office |  |  |
| [Find Deal and Match Deal Details](#unique_88) [page ] 161 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | An incoming correspondence is created. |
| [Set Settlement Status](#unique_89) [page ] 162 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The TRM transaction is settled. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_90) [page ] 163 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_91) [page ] 167 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_92) [page ] 169 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank-Initiated Payment](#unique_93) [page ] 172 |  |  |  |
| [Post to General Ledger](#unique_94) [page ] 173 | Treasury Accountant | Fix, Pay and Post Flows (TBB1)/ Process Business Transactions (TPM10) | FI document is posted. |
| [Maintain Fair Value of Transaction](#unique_95) [page ] 175 | Treasury Specialist - Back Office | Manage Net Present Values (F7601) | The fair value of transaction is maintained manually. |
| [Perform Key Date Valuation](#unique_96) [page ] 177 | Treasury Accountant | Run Valuation (TPM1) | The financial instrument is valued, related FI document is posted. |
| [Decide to Exercise](#unique_97) [page ] 179 | Treasury Specialist - Front Office | Manage Financial Transactions (F6157) | The transaction is updated to Exercise and is saved without error. |
| [Create Interest Rate Swap Contract](#unique_98) [page ] 180 | Treasury Specialist - Front Office | Manage Financial Transactions (F6157) | The data is saved and the new transaction number generated. |
| [Decide to Expire](#unique_99) [page ] 182 | Treasury Specialist - Front Office | Manage Financial Transactions (F6157) | The transaction is updated to Expiration and is saved without error. |
| [Post Realized Profit and Loss](#unique_100) [page ] 183 | Treasury Accountant | Post Derived Business Transactions (TPM18) | Accounting document has been created in local GAAP (valuation area AE0). |

Report

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Display Treasury Posting Journal](#unique_101) [page ] 185 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Posting journals display. |
| [Treasury Position Analysis](#unique_102) [page ] 185 | Treasury Accountant | Treasury Position Analysis | Position analysis data displays. |
| [Display Treasury Position Values](#unique_103) [page ] 186 | Treasury Accountant | Display Treasury Position Values (F1867) | The position values data displays. |
| [Define Financial Positions](#unique_104) [page ] 187 | Treasury Risk Manager | Define Financial Positions (FTR_FP_DEF) | A set of key figures is defined. |
| [Financial Status (Book Value)](#unique_105) [page ] 189 | Treasury Risk Manager | Financial Status (F2136) | Financial status on book values displays. |
| [Financial Status (Nominal Amount)](#unique_106) [page ] 189 | Treasury Risk Manager | Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)) | Financial status on nominal amount displays. |
| [Display Treasury Payments](#unique_107) [page ] 190 | Treasury Specialist - Back Office | Display Treasury Payments (TPM20A) | All payment journals are displayed. |
| [Display Treasury Position Flows](#unique_108) [page ] 191 | Treasury Accountant | Display Treasury Position Flows (F1754) | Position Flow data displays. |
| [Display Treasury Alerts - Posting](#unique_109) [page ] 192 | Treasury Accountant | Display Treasury Alerts - Posting (F4984) | Treasury alerts for posting display. |
| [Display Treasury Alerts - Settlement, Release, Correspondence, and Interest Rates](#unique_110) [page ] 193 | Treasury Specialist - Back Office | Display Treasury Alerts - Settlement (F4979) | Treasury alerts for various type of transactions display. |
| [Display Payment Schedule](#unique_111) [page ] 194 | Treasury Accountant | Display Payment Schedules (TJ04) | The payment schedule displays. |
| [Analyze NPV](#unique_112) [page ] 195 | Treasury Specialist - Middle Office | Analyze NPV (JBRX) | calculate and display NPV result |
| [Calculate Market Risk Key Figures](#unique_113) [page ] 196 | Treasury Specialist - Middle Office | Calculate Market Risk Key Figures (AISGENKF) | The NPV Result displays based on Portfolio Hierarchy. |
| [Sensitivity Key Figures](#unique_114) [page ] 197 | Treasury Specialist - Middle Office | Sensitivity Key Figures - Single Analysis (AISS) | The Sensitivity Key Figures displays based on Portfolio Hierarchy |
| [Review Limit Utilization Report](#unique_115) [page ] 198 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | The system displays an overview of the limit utilizations in accordance with your selection criteria. |
| [Review Interest Rate Overview](#unique_116) [page ] 199 | Treasury Specialist - Front Office | Interest Rate Overview (F3098) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Interest Rate Swap

Purpose

An interest rate swap is a derivative in which a party exchanges a stream of interest payments for another party's stream of cash flows. Interest rate swaps can be used by hedgers to manage their fixed or floating assets and liabilities. They can also be used by speculators to replicate unfunded bond exposures to profit from changes in interest rates.

Interest rate swaps are swap transactions that usually have a term of over a year. They are affected based on different interest rates in the same currency or cross-currency. You can represent the most common variants such as the swap of fixed interest rates against variable interest rates or variable interest rates against each other in the SAP system.

The following procedures describe the functionality of the interest rate swap (in same currency).

#### Market Data

Purpose

In this activity, you enter market data (such as foreign currency exchange spot rates, swap rates, reference interest rates, and so on). The data provides default values when creating new transactions, or calculating fair value for existing transactions.

Procedure

Execute all procedures in the Market Rates Management – Manually via Upload (1XN) test script, before proceeding with the steps in this test script.

|  |
| --- |
| Note The example data in 1XN might not contain the necessary interest rates for your test. If you are using SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA, please make sure that you've entered interest from current date to current date of next month when you are doing test for this test script. |

#### Automatic Market Rates Management (1S4) (Optional)

Purpose

As an option, you can integrate market data with the data feed via SAP Cloud Platform, through manual operation or job scheduling.

Procedure

If you implement this option, complete the steps provided in the Automatic Market Rates Management (1S4) test script before proceeding with this test script.

#### Generate Limit Utilizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the end of the transaction day, the Treasury Specialist - Middle Office processes the end-of-day activities. The system determines and updates limit utilizations based on the transactions and positions contained in the data pool, as well as the external transactions that were entered.

|  |
| --- |
| Note A background job can be scheduled for this procedure. For more information about job scheduling, see the topic in the Appendix. |

Prerequisite

The market data is imported.

If security exists, the spot price needs to be maintained for the current date. Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open End-of-Day Processing (KLNACHT). | The End-of-Day Processing view displays. |  |
| 3 | Enter Criteria of End-of-Day Processing | Make the following entries and choose Execute:Valuation Date: for example, <Current Date>Determination Procedure: for example, 10 to 20Company code: for example, 3310 | The system displays the message End-of-day processing was completed successfully. |  |

#### Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This function calculates online and displays the key figures for Net Present Value (NPV) analysis and Sensitivity key figures for a selection of transactions. You use calculated key figures as the basis for defining formula-based key figures, and display them with the NPV and Sensitivity key figures.

Prerequisite

You maintained a report layout for key figures. For more information, see the [Defining Report Layout for Calculate Market Risk Key Figures](#unique_119) [page ] 244 procedure under the Market Risk Analyzer topic in the Appendix.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Calculate Market Risk Key Figures (AISGENKF). | The Calculate Market Risk Key Figures view is displayed. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <Current Date>Report Layout: for example, Y01 or other Report Layout you createdPortfolio Hierarchy: for example, 100 | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |  |
| 4 | Characteristics | Choose the Characteristics tab. |  |  |
| 5 | Enter Selection Criteria | Make the following entries and choose Run:Company Code: for example, 3310Product Type: for example, 62A | The net present value (NPV) displays based on portfolio hierarchy. |  |

#### Check Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check the limit utilization report.

Prerequisite

The limit master records of your company are maintained in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics view displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Execute:Limit type: for example, Y01 or Y07Limit Utilization Base: for example, 1Determination Date: for example, <Current Date>Limits Valid From: for example, <Current Date> | The system displays an overview of the limit utilizations. |  |

##### Create Interest Rate Swap Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create an interest rate swap transaction.

Procedure

Option 1: IBOR is in use

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create IR Derivative (TO01). | The Create Interest Rate Derivative: Initial Screen is displayed. |  |
| 3 | Enter Data | Enter the following data and press Enter:Company code: for example, 3310Product Type: for example, 62ATransaction Type: for example, 300Partner: for example, 33537001 | The Create Swap: Structure view is displayed. |  |
| 4 | Enter Data | Enter data in the following groups, and choose Save:Term group:Start: for example, Current DateEnd: for example, Current Date next yearOutgoing Interest group:Nominal amount: for example, 2,000,000.00 AEDNote The nominal amount is only for testing purpose. You can change it according to your real business transaction.Effective From: for example, <Current Date>1st Due Date: for example, <First day of (Current month + 3 months)>Freq.Month: for example, 3Fix.Rate: for example, 3.5Int. Calc.Method: for example, selectBusiness Calendar group:Calendar 2: for example, leave blankIncoming Interest group:Nominal amount: for example, 2000,000.00Effective From: for example, <Current Date>1st Due Date: for example, <First day of (Current month + 3 months)>Freq.Month: for example, 3Var.Interest: for example, AEDM03EIBInt. Calc.Method: for example, 2 act/360Contract Conclusion group:Contract Date: for example, <Current Date>Stay in this view for the following step. | The Interest Rate Swap's data on the Structure tab is entered. |  |
| 5 | Enter First Period Interest Rate for Variable Leg | Choose Condition – Incoming Side. | The Overview of Conditions view is displayed. |  |
| 6 | Interest Rate | Double click on CTyp 1200 Interest.Make the following entries:First Int Rate: for example, 3.2Choose Back twice to return to the Create Swap: Structure view. | The first period initial interest rate is entered. The Create Swap: Structure view is displayed. |  |
| 7 | Check Outgoing Interest Flows | Choose the Outgoing tab, and review the outgoing interest flows. | The outgoing interest flows are reviewed. |  |
| 8 | Check Incoming Interest Flows | Choose the Incoming tab, and review the incoming interest flows. | The incoming interest flows are reviewed. |  |
| 9 | Validate the General Valuation Class | Choose the Administration tab to review the general valuation class to ensure the class is correct. Stay in this view for the following step. | The correct general valuation class is selected. |  |
| 10 | Create Payment Request for Outgoing Interest Flows | Choose Payment Details.Double-click Direction - to display the Create Swap: Payment Details view.Make the following entries and choose Save:Payment Request: for example, WithHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment methods: for example,Note If the Check Run: Trans.: Display messages dialog box displays, choose Continue. | The following message is displayed:The financial transaction saved under number.Make a note of the transaction number: __________. |  |

Option 2: If you want to use SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create IR Derivative (TO01). | The Create Interest Rate Derivative: Initial Screen displays. |  |
| 3 | Enter Data | Enter the following data, and choose Enter:Company Code: for example, 3310Product Type: for example, 62ATransaction Type: for example, 300Partner: for example, 33537001 | The Create Swap: Structure view displays. |  |
| 4 | Enter Data | Enter data in the following groups:In the Term group:Start: for example, <the current date>End: for example, <the current date of next month>In the Outgoing Interest group:Nominal Amount: for example, 2,000,000.00 USDThe nominal amount is only for testing purpose. You can change it according to your real business transaction.Effective From: for example, <the current date>1st Due Date: for example, <the current date of next month>Freq.Month: for example, 1Fix.Rate: for example, 3.5Int. Calc.Method: for example, select 2 act/360In the Business Calendar group:Calendar 1: for example, EUCalendar 2: for example, <leave blank>In the Incoming Interest group:Nominal amount: for example, 2000,000.00Effective From: for example, <the current date>1st Due Date: for example, <the current date of next month>Freq.Month: for example, 1Var.Interest: for example, SOFRInt. Calc.Method: for example, 2 act/360In the Contract Conclusion group:Contract Date: for example, <the current date>Stay in this view for the following step. | The Interest Rate Swap's data on Structure tab is entered. |  |
| 5 | Enter First Period Interest Rate for Variable Leg | Choose Condition - Incoming Side. | The Overview of Conditions view displays. |  |
| 6 | Interest Rate | Double-click on the condition type 1200.Make the following entries:Int calc.type: 5 Compound Interest CalculationInt.Calc. Method: 2 act/360Ref.Int.Rate: + SOFRPercentage Rate: 3.2Note If 6 Average Compound Interest Calculation is selected, the following fields under Average Interest Rate are displayed: and should maintained for example as following:Weighting: for example, L Based on Interest Rate Adjustment DateRounding: Round to the NearestDecimal Places: 4Spread: 1Choose Back to go back to the Overview of Conditions view. | The first period initial interest rate is entered. The Create Swap: Structure view displays. |  |
| 7 | Interest Rate Adjustment | Double-click on condition type 1210 Interest rate adjustment in the Condition View.Make the following entries:Interest Rate Adjustment: 1 Regular 1 Calendar DaysIR Adj.Date: <effective date>, for example, <current date>Calendar rule: 3 Previous Working DayInterest Rate Fixing Date: for example, Relative, - 1 Working daysLockout Period: 2 Working DaysChoose Back to go back to the Overview of Conditions view. | The Interest Rate Adjustments Tab under Condition Type 1210 displayed. |  |
| 8 | Maintain Accumulating Condition | On the Overview of Conditions view, select the condition type 1200 Interest, then choose Create Accumulating Condition from the toolbar.In the pop up dialog box of Possible condition types, double click on condition type 1201 - Interest (accumulated).Eff.From: <the current date>Choose Back twice to return to the Create Swap: Structure view. | The condition type Interest (accumulated) is maintained. |  |
| 9 | Check Outgoing Interest Flows | Choose the Outgoing tab, and review the outgoing interest flows. | The outgoing interest flows are reviewed. |  |
| 10 | Check Incoming Interest Flows | Choose the Incoming tab, and review the incoming interest flows.Choose Show/Hide Single Flows to show or hide the single interest flows 1200 - Interest. | The incoming interest flows are reviewed. |  |
| 11 | Validate the General Valuation Class | Choose Administration to review the general valuation class to ensure the class is correct. Stay in this view for the following step. | The correct general valuation class is selected. |  |
| 12 | Create Payment Request for Outgoing Interest Flows | Choose Payment Details.Double-click Direction - to display the Create Swap: Payment Details view.Make the following entries and choose Save:Payment Request: for example, WithHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, TFNote If the Check Run: Trans.: Display message dialog box is displayed, choose Continue. | The system displays the message The financial transaction saved under number. Make a note of the transaction number: __________. |  |

#### Correspondence

Purpose

Information for SAP Treasury Risk Management transactions is transferred between you and your business partner. SAP Treasury Risk Management provides standard correspondence functionalities to use for communicating with a business partner via e-mail or printed forms.

Prerequisites

The Preliminary Step section outlines the initial steps for setting up correspondence. Complete those procedures before continuing.

Procedure

The procedures in this section describe additional steps required for interest rate swap.

##### Settle Statement Status (Manual)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a treasury risk management transaction is recorded and saved, the transaction must be settled before further activities. After you get counterparty confirmation, you can settle the transaction in one of two ways:

- Manual settlement: For example, if you receive counterparty confirmation email, then you can use following app to settle the transaction manually:
    - Process IR Derivatives (Subtitle: Collective Process)
- Automatic settlement via correspondence process: For example, when a transaction has all the outgoing correspondence objects and incoming correspondence objects matched and set to completed status, the financial transactions will be set to settlement status automatically.

The following procedure describes settling the treasury risk management transaction manually.

Prerequisite

A treasury risk management transaction is created and available for this procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process IR Derivatives - Collective Processing (TI92). | The Collective Processing: Interest Rate Derivatives view displays. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute:Company Code: for example, 3310Transaction: <Transaction Number created previously> | The Collective Processing: Interest Rate Derivatives view displays. |  |
| 4 | Settle the Transaction | Select the checkbox at the beginning of the transaction line and choose Settle. | The Settle OTC Interest Rate Instrument: Initial Screen view displays the transaction data. |  |
| 5 | Save the Change | Choose Save.Note If the Check Run: Trans.:Display messages dialog box displays, choose Continue (Enter). | The transaction is settled and saved.The Collective Processing: Interest Rate Derivatives view displays. |  |
| 6 | Check the Status of the Transaction | Select the checkbox and choose Display. | The Display Swap, Structure view displays. |  |
| 7 | Check the Status of the Transaction | Choose the Status tab.Verify that the Activity Cat field is in Contract settlement status. | The transaction has contract settlement status. |  |

##### Correspondence with PDF Form

Purpose

E-mail and print are both PDF-related outputs. By default, SAP provides several business profiles for PDF forms, such as PR_PRINT and PR_EMAIL.

- For any business partner assigned to the PR_PRINT profile, when a financial transaction is created, a PDF form is sent to a predefined print queue. You can view and print the PDF file via the Maintain Print Queues (F1260) app. Once you verify that the transaction information on the form is correct, you can send the paper copy of the form to the business partner.
- For any business partner assigned to the PR_EMAIL profile, when a transaction is created, SAP automatically sends e-mails to the Business Partner.
- Once you receive the counterparty confirmation about the transaction from your Business Partner, you can settle all the correspondence objects of the transaction. Once all the correspondence objects are settled, the transaction status changes to Contract Settlement status.

Use the following apps to maintain your own settings for output:

- Output Parameter Determination. You maintain your own rules for the output. For example, you can maintain e-mail address of recipients. This rule overwrites the e-mail address of the Business Partner for an external counterparty, or overwrites the e-mail address of User IDs for an internal counterparty.
- Maintain Email Templates - Deprecated (F1306). You maintain your own e-mail template with this app.
- Maintain Form Templates (F1434). You maintain your own form template with this app.

In the following procedures in this section, you settle the treasury risk management transaction via the correspondence processing automatically.

Prerequisite

A new treasury risk management transaction must be created (as described in the prior step), since the transaction is manually settled.

###### Send Confirmation Email/Print

Purpose

SAP provides the best practices business partner group, BPG_DEFAULT. By default, if any business partner is assigned to this group, correspondence objects are automatically sent when a financial transaction is saved. As described in the Preliminary Steps section, the best practices business partner, 33537001, is assigned to BPG_GROUP, so the correspondence objects are sent automatically. However, if you use the configuration step Define Business Partner Group to create new business partner groups and then do not assign the auto-send attribute, you must send those correspondence objects manually using the Send Correspondence (FTR_COSEND) app.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

The automated procedure does not require you to do any operation in-system.

###### Check Correspondence Status

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

###### Receive Incoming Confirmation

Purpose

In the prior procedure, an outbound email is sent to the business partner. Typically, you receive counterparty confirmation from the business partner via email, phone, or other channels. This procedure takes place outside of the system.

Procedure

This procedure does not require any operation from the system.

###### Find Deal and Match Deal Details

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
| 4 | Create | Choose Create. | The Options for Creating Correspondence Objects dialog box displays. |  |
| 5 | Create an Incoming Correspondence Object Referring to the Outgoing Correspondence Object | Enter the following data for groups and press Enter:Display Options group:Corresp. Categ: 01 Transaction ActivitiesTransaction Details group:Company Code: for example, 3310Product Type: for example, <Product type you entered in the transaction>Incoming/Outgoing: I IncomingEntry Options: 05 Correspondence Object as TemplateTemplate for Correspondence Object Data group:Correspondence Key: for example, <Enter the correspondence key number for COUNTERPARTY PRINT from the previous step> |  |  |
| 6 | Save | Choose Save.Note If the Automatic matching proposal view displays, choose Cancel. | The incoming correspondence object is created successfully and displayed on Correspondence monitor - Standard View view. |  |
| 7 | Match the Incoming Correspondence Object with the Outgoing Correspondence Objects for channel PRINT | Select the checkbox for the incoming correspondence object and choose Status Functions > Automatic Match. | The Automatic matching proposal view displays. |  |
| 8 | Outgoing Correspondence | On the left-side of the view, expand the incoming correspondence key. All outgoing correspondence objects of the transaction are displayed.Select all the checkboxes of the outgoing correspondence objects and choose Enter. | All the outgoing COUNTERPARTY PRINT correspondence objects of the transaction now have status completed.All the INTERNAL outgoing correspondence objects remain in Delivered status. |  |
| 9 | Match the Incoming Correspondence Object with the Outgoing Correspondence Objects for channel EMAIL | Repeat the above steps to create an incoming correspondence object for COUNTERPARTY EMAIL and match it with outgoing correspondence for channel EMAIL. |  |  |

###### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the previous procedure, all the correspondence objects of the transaction are successfully matched. The standard functionality provides that the transaction is settled automatically. In this procedure, you verify that the transaction settled automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor view displays. |  |
| 3 | Enter Selection Criteria on the Initial View | Enter the following data and choose Execute:Correspondence group:Company Code: for example, 3310Deal tab:Company Code: for example, 3310Deal Number: for example, <Transaction Number> | The Correspondence monitor - Standard View displays. |  |
| 4 | Display the Transaction History | Select the checkbox for the incoming correspondence object and choose Show Underlying. | The History of OTC Interest Rate Instrument: Activity Sequence view displays, with Activity 2 Contract Settlement in the second line. |  |

#### Period-End Closing

Purpose

This section describes activities for period-end closing (usually executed at month end), including:

- Accrue interest income/expenses
- Calculate or maintain fair value of transactions
- Perform key date valuation

##### Run Accrual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this function to accrue interest expenses and interest income based on existing financial instruments and reflect results correctly in the general ledger. The function distributes the amount correctly, based on the time period from flow start date to the key date, irrespective of when they are due for payment or received.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Accrual/Deferral (TPM44). | The Execute Accrual/Deferral of Expenses and Revenues view displays. |  |
| 3 | Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany code: for example, 3310Valuation Area: for example, AE0Transaction: <Transaction numbers created in previous procedures>Accrual/Deferral Key Date: for example, <last date of current month>Include key date: SelectedTest Run: Selected | The Execute Accrual/Deferral of Expenses and Revenues view displays. Review the accrual information on this view.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Note No posting is created because it is a test run. |  |
| 4 | Production Run | Choose Back to return to the initial view of the app.Change the following data and choose Execute:Test Run: Deselected | The Execute Accrual/Deferral of Expenses and Revenues view displays. Review the accrual information on this view.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Because this is a production run, the accounting document is created in local GAAP (valuation area AE0). |  |

##### Calculate or Maintain Fair Value of Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you determine the fair value (net present value (NPV)) of financial transactions.

The NPV can be calculated automatically by the Market Risk Analyzer (MRA) and saved to table VTVBAR. These values can then be used for the accounting valuation. In addition, you can also maintain the relevant net present value manually.

Predelivered configuration in the MRA component of SAP Treasury and Risk Management provides two options when calculating NPV automatically by the Calculate Net Present Values (Subtitle: with CVA and DVA)app:

- Risk-free NPV: using the evaluation type that does not contain a credit spread curve, the system only calculates the risk-free NPV.
- Risk-based NPV: using the evaluation type that contains the credit spread curve, the system calculates risk-free NPV by using risk-free yield curve, and calculates the (risk-based) NPV, also accounting for credit spreads.

The CVA (credit value adjustment) or DVA (debit value adjustment) is the difference between the risk-free NPV and the (risk-based) NPV. This is called difference method.

NPV = risk-free NPV - CVA - DVA.

Prerequisite

Before calculating NPV via the Calculate Net Present Values (Subtitle: with CVA and DVA) app, ensure relevant market data (interest rates, foreign exchange rates, credit spreads, and so on) is maintained for the evaluation date. For more information about market data maintenance, see the Market Rates Management – Manually via Upload (1XN) test script.

Procedure - Option 1: Calculate NPV Automatically

|  |
| --- |
| Note By default, Yield Curve Type 9001 is defined with reference rate SOFR/ESTER; Yield Curve Type 0001 is defined with reference rate IBOR; Evaluation Type is defined with Yield Curve Type 0001 only. If you want to use SOFR, ESTER, SONIA, SARON, TONAR, CORRA, SORA, HONIA, you can choose to use SAP pre-delivered content, or set up your own yield curves, evaluation type, basis spreads and basis spread curves via relevant SSCUIs based on these reference rates. |

|  |
| --- |
| Note To schedule a background job for option 1, see the corresponding step in the Appendix. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments view displays. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute:Evaluation Parameter Derivatn: DeselectedSelect OTC Transactions: SelectedCompany Code: for example, 3310Transaction: <Transaction numbers created in previous procedures>Evaluation Date: for example, <last date of current month>CVD/DVA Type: To calculate risk-free NPV, leave blank. To calculate risk-based NPV and CVA/DVA, enter Y01.Evaluation Type: To calculate risk-free NPV, enter Y001. To calculate risk-based NPV and CVA/DVA, enter Y002Test Run: DeselectedPrice/NPV Type: 001Save Values with Warnings: SelectedDetail Log (Other Calc. Steps): Selected | The NPVs including CVA/DVA from the Market Risk Analyzer view displays with the NPV, risk-free NPV, CVA, DVA of each transaction on this view.You can also review different information by selecting additional buttons on this view:Single Transaction:CVA/DVA Key FiguresDetailed LogCalculation BasesError Log |  |

Procedure - Option 2: Maintain NPV Manually

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Net Present Values (F7601). | The Manage Net Present Values screen displays. |  |
| 3 |  | Choose Create. | The Net Present Value Data screen displays. |  |
| 4 | Enter Header | Make the following entries:Transaction: <transaction numbers created in previous steps>Company Code: for example, 3310Price / NPV Type: 001Effective from: for example, <last date of current month> |  |  |
| 5 | Enter Net Present Value Details | Make the following entries and choose Create:NPV Currency: for example, AEDNet Present Value: <the value of (risk-based) NPV>Risk-Free Net Present Value: <the value of risk-free NPV>CVA: <the value of CVA>DVA: <the value of DVA>Note To reflect credit spreads for accounting valuation, maintain the risk-based NPV in the Net Present Value field, then enter CVA/DVA, which is the difference between risk-free NPV and risk-based NPV, Net Present Value (NPV) = risk-free NPV - CVA - DVA. Otherwise, also enter the value of risk-free NPV in the Net Present Value field, and leave fields CVA and DVA blank. | Manually maintained NPV is saved. |  |

|  |
| --- |
| Note You can also use SAP Fiori app Enter Net Present Values (JBNPV) to maintain NPV manually. |

##### Perform Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The valuation function values the positions of financial instruments, based on historical cost or fair value for a given key date, and transfer results to financial accounting.

|  |
| --- |
| Note To schedule a background job for this step, see the corresponding step in the Appendix section. |

Prerequisite

Fair values (net present values (NPV)) are calculated or maintained for financial transactions that are evaluated at fair value (NPV) according to accounting principles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Run Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | Make the following entries and choose Execute:In the Product Groups area,OTC Transactions: <select>In the General Selections area,Company Code: for example, 3310Valuation Area: for example, AE0Transaction: <Transaction numbers created in previous procedures>In the Valuation Parameters area,Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation with ResetNote When the period end is also the year end, use the Valuation Category of Year End Valuation.Test Run: <select> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | Choose Run Valuation.Note If the Message dialog box displays, choose Continue. | The Valuation Log view displays.If a red traffic light status is shown, select and review the error message. Correct the issue and perform test run again, until the error is resolved.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Note If there is no simulated posting, your selected transaction does not require valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the Run Valuation screen is displayed.On the Run Valuation screen, change the following data and choose Execute:Test Run: <deselect> | The Display Selected Treasury Positions for Valuation view is displayed. |  |
| 6 | Execute Valuation for Production Run | Choose Run Valuation. | The Valuation Log view displays.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Because this is a production run, the accounting document is created in local GAAP (valuation area AE0). |  |

#### Interest Rate Adjustment

Purpose

This section covers the activities for Interest Rate Adjustment, including:

- Interest Rate Adjustment Schedule Report
- Adjust Interest Rate

##### Interest Rate Adjustment Schedule Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you get an overview of interest rate adjustment schedule.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Adjustment Schedule - Rates/Prices (TJ07). | The Rate/Price Adjustment Schedule screen is displayed |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Execute:Interest Rate Adjustment: <select>Company Code: for example, 3310Product Type: for example, 62A | The overview of the rate or price adjustment schedule is displayed. |  |

##### Adjust Interest Rate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you adjust the interest rate for the reference interest rate.

Prerequisite

You have maintained the reference interest rate on the fixing date, according to the Enter Interest Rates step in the Market Rates Management – Manually via Upload(1XN) test script.

|  |
| --- |
| Note The example data in 1XN might not contain the necessary interest rates for your test. If you are using SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA, please make sure that you've entered interest from current date to current date of next month when you are doing test for this test script. |

.

Procedure - Option 1: Interest Rate Adjustment (Automatically)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Automatic Adjustments - Rates/Prices (TJ05). | The Run Automatic Interest Rate or Price Adjustment screen is displayed. |  |
| 3 | Enter Parameter of Adjustment | Make the following entries, and choose Execute:Interest Rate Adjustment: <select>Company Code: for example, 3310Fixing Date: for example, <the fixing date you noted down from the previous procedure>All Transactions: <deselect>Single Transactions: <transaction number you noted from previous procedure>Test Run: <deselect> | The interest rate adjustment of fixing date processes automatically runs. |  |

Procedure - Option 2: Interest Rate Adjustment (Manually)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Adjustment - Rates/Prices (TI10) | The Create Rate/Price Adjustment screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and press Enter:Interest Rate Adjustment: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure> |  |  |
| 4 | Enter Interest Rate | Enter the following data, and choose Save:Interest Rate: for example, 7 | The manual interest rate adjustment is created. |  |

#### Interest Payment

Purpose

This section describes handling the payment for interest of the Interest Rate Swap transaction and posting it to G/L accounting.

Prerequisites

You can only trigger the payment and posting of flows for a transaction that is in Contract Settlement status.

##### Display Payment Schedule

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
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:OTC Transactions: <select>Company Code: for example, 3310End of Term in the Future: <select>End of Term in Lapsed: <select>Payment Period: for example, <Current Date> to <Current Date + 12 months>Payment Status: for example, 1Output Error Log: <select> | The payment schedule report displays for your review.Note Make a note of the transaction number and payment date displayed on this view for use in additional procedures (for example, process payment). |  |

##### Interest Payment

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <Payment Date you noted in previous procedure>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Pay Only: <select> | Screen Logs and Messages displays, you can check the payment information via the Payment Log.If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following change, and choose Run:Test Run: <deselect> |  |  |
| 6 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <Payment Date you noted down in the previous procedure>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select> | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back. | The Fix and Pay Flows view displays. |  |
| 5 | Production Run | Enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 6 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

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

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request is selected as required (usually only for outgoing payment, in practice). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows that require payment request. It does not create posting in financial accounting.

When payment is initiated by the financial partner, skip this procedure and the Process Payment Request procedure and continue with the Bank Initiated Payment procedure.

|  |
| --- |
| Note To schedule a background job for this step, see the corresponding step in the Appendix. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <Payment Date you noted in previous procedure>Test Run: <select>Pay Only: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the [Post to General Ledger](#unique_45) [page ] 74 procedure. |  |
| 4 | Production Run | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Run:Test Run: <deselect> | The Payment Log view displays and a payment request is generated.Note Make note of the key number displayed on this view as the number is required for other procedures. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <the transaction number you noted down from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <Payment Date you noted down in the previous procedure>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back. | The Fix and Pay Flows view displays. |  |
| 5 | Production Run | Enter the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays and a payment request is generated.Note Make note of the key number displayed on this view as the number is required for other procedures. |  |

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

A payment request is generated from the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests view displays. |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters view displays. |  |
| 4 | Enter Parameters | Enter the following data and choose Dynamic selections:Posting Date: for example, <current date>Next payment run on: for example, <current date + 12 Months>Company Code: for example 3310Payment Methods: for example, TF | The Free Selection for payment run dialog box displays. |  |
| 5 | Enter Parameters | Make the following entries and choose Save:Key number: <the key number you noted from the previous procedure> |  |  |
| 6 | Enter Parameters | Choose Additional Log. | The Additional Log dialog box displays. |  |
| 7 | Enter Parameters | Make the following entries and choose Continue:Payment method selection in all cases: <select>Line items of the payment documents: <select>Due date check: <select>Note If the message Log created for all accounts displays, choose Continue. | The Automatic Payment Transactions: Parameters view displays. |  |
| 8 | Enter Parameters | Choose Save. | The Automatic Payment Transactions for Payment Requests view displays.The message Parameters have been entered displays. |  |
| 9 | Schedule Proposal | Choose Proposal. | The Schedule Proposal dialog box displays. |  |
| 10 | Schedule Proposal | Select Start Immediate and choose Schedule Job. | The system displays the message Proposal is running in the status bar with a yellow traffic light status. |  |
| 11 | Schedule Proposal | Choose Status, until the Payment proposal has been created message displays in the status bar with green traffic light status. | Payment proposal is generated. |  |
| 12 | Schedule Payment | Choose Pmnt run. | The Schedule Payment dialog box displays. |  |
| 13 |  | Select Start Immediat., choose Create Payment Medium, and choose Schedule Job. | The system displays the message Payment run is running in the status bar with yellow traffic light status. |  |
| 14 |  | Choose Status, until the message Payment run has been carried out displays with green traffic light status. | The payment document is created.If SAP Bank Communication Management is not implemented in your system, the payment medium created uses the PMW format. To review, choose Display payment log.If SAP Bank Communication Management is implemented in your system, in the Display payment log, the message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media displays. Create a SAP Bank Communication Management batch after the payment run. Proceed to the following step. |  |
| 15 | Cross-Payment Run Payment Media (Create SAP Bank Communication Batch) | Caution This step only applies if SAP Bank Communication Management is implemented in your system.On the Automatic Payment Transactions for Payment Requests view, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium . | The Creation of Cross-Payment Run Payment Media view displays. |  |
| 16 | Cross-Payment Run Payment Media (Create SAP Bank Communication Batch) | Caution This step only applies if SAP Bank Communication Management is implemented in your system.Enter the following data and choose Run:Run Date: for example <current date>Identification: for example, TRM01R | The Creation of Cross-Payment Run Payment Media dialog box displays the message Collector XX/XX/20XX XXXXXX was created or updated confirming that the SAP Bank Communication Management batch is created.Note A batch may require additional approvals before payment medium is finally created. For more information, see the Advanced Cash Operations(J78) scope item. |  |

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

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this app to generate the posting for incoming payment. When using this app for this procedure, it does not create posting for outgoing payment that you processed in the Generate Payment Request procedure using the Pay Only option.
- Process Business Transactions: Use this app to generate the posting for outgoing payment that you processed in previous Generate Payment Request procedure using the Pay Only option.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Prerequisite

The outgoing payment handled by the payment request for this transaction was processed in the Generate Payment Request procedure using the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Execute:Derivatives: SelectedCompany code: for example, 3310Transaction: <transaction number with inflow created in previous procedure>Up to and Including Due Date: enter date the flow of the financial transaction is posted, for example, <current date + 1 Year>Test Run: SelectedPost Operational Only: Selected | Note The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run.If the No flows exist for processing message displays, no posting is required for your selection criteria. Skip the Production Run step and continue the test step using the Process Business Transactions (TPM10) app. |  |
| 4 | Production Run | Choose Back.Change the following data and choose Execute:Test Run: Deselected | The Posting Log: Posted Business Transactions view displays. An accounting document is created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 6 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select>Company Code: for example 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select>Transaction: <transaction number with outflow, and its payment request has been generated with the Generate Payment Request procedure>Test Run: <select> | The Test Run: Post/Reverse Business Transactions view displays.Note If the You have not selected any business transactions message displays, no postings are required for your selection criteria. Skip this step. |  |
| 7 | Check Test Run Result | Choose Select All, choose Choose Those to Post, and choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view displays. |  |
| 8 | Logs and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.Change the following data and choose Execute:Test Run: Deselected | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 9 | Production Run | Choose Select All, choose Choose Those to Post, and choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view displays. |  |
|  | Logs and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Post Realized Profit and Loss

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you fix and post derived business transactions. Usually this occurs for realized profit and loss when a deal is mature.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Prerequisite

The maturity date of transaction is reached.

The financial transaction is created, settled, and posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Post Derived Business Transactions view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany Code: for example, 3310Valuation Area: for example, AE0OTC Transactions: <transaction numbers which are mature>TRL Date: <maturity date of transaction>Test Run: <select>If the system displays the message Are you sure that you want to select future business transactions, choose Enter. | The Fix and Post Derived Business Transactions view displays.Note If the No scheduled derived business transactions were found for the selection message displays, no derived transaction is available for your selection. You can skip this step. |  |
| 4 | Fix and Post for Test run | Choose Fix. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0).Note No posting is created since this is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial view of this app. Change the following data and choose Execute:Test Run: <deselect>If the system displays the message Are you sure that you want to select future business transactions, choose Enter. | The Fix and Post Derived Business Transactions view displays. |  |
| 6 | Fix and Post for Production Run | Choose Fix. | The Posting Log: Posted Business Transactions view displays. The posting information for local GAAP (valuation area AE0) and the accounting document are created in local GAAP (valuation area AE0). |  |

### Cross-Currency Interest Rate Swap

Purpose

This section describes the functionality of Cross-Currency Interest Rate Swap.

An interest rate swap is a derivative in which one party exchanges a stream of interest payments for another party's stream of cash flows. Interest rate swaps are used by traders, investors, or hedgers to manage their fixed or floating assets and liabilities. They can also be used by speculators to replicate unfunded bond exposures to profit from changes in interest rates.

Interest rate swaps are swap transactions that usually have a term of over a year. They are affected on the basis of different interest rates in the same currency or cross-currency. You represent the most common variants such as the swap of fixed interest rates against variable interest rates or variable interest rates against each other in the SAP system.

#### Market Data

Purpose

This procedure provides instructions on how to enter market data such as foreign currency exchange spot rates, swap rates, reference interest rates, and so on.

The data provides default values when creating new transactions, or calculating fair value for existing transactions.

Procedure

Complete all steps in the Market Rates Management – Manually via Upload (1XN) scope item before proceeding.

#### Automatic Market Rates Management (1S4)(Optional)

Purpose

Optionally, you can integrate market data with the data feed via SAP Cloud Platform, through manual operation or job scheduling.

Procedure

If you implement this option, complete the steps in the Automatic Market Rates Management (1S4) scope item before proceeding.

#### Generate Limit Utilizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the end of the transaction day, the Treasury Specialist - Middle Office role processes End-of-Day activity. The system determines and updates limit utilizations based on the transactions and positions contained in the data pool, as well as the external transactions that were entered.

|  |
| --- |
| Note A background job can be scheduled for this procedure. For more information about job scheduling, see the topic in the Appendix. |

Prerequisite

The market data is imported.

If security exists, the spot price needs to be maintained for current date. Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open End-of-Day Processing (KLNACHT). | The End-of-Day Processing view displays. |  |
| 3 | Enter Criteria of End-of-Day Processing | Enter the following data and choose Execute:Valuation Date: for example, <Current Date>Determination Procedure: for example, 10 to 20Company code: for example, 3310 | The system displays the message End-of-day processing was completed successfully. |  |

#### Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This function calculates online and displays the key figures for Net Present Value (NPV) analysis and sensitivity key figures for a selection of transactions. You use calculated key figures as the basis for defining formula-based key figures, and display them with the NPV and sensitivity key figures.

Prerequisite

A report layout for key figures is maintained. For more information, see the [Defining Report Layout for Calculate Market Risk Key Figures](#unique_119) [page ] 244 procedure under the Market Risk Analyzer topic in the Appendix.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Calculate Market Risk Key Figures (AISGENKF). | The Calculate Market Risk Key Figures view displays. |  |
| 3 | Enter Selection Criteria of Gen. Selection | Enter the following data and choose the Characteristics tab:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <Current Date>Horizon: for example, <Current Date>Report Layout: for example, Y01 or other Report Layout you createdPortfolio Hierarchy: for example, 100 | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |  |
| 4 | Enter Selection Criteria | Make the following entries and choose Run:Company Code: for example, 3310Product Type: For example, 62A | The net present value (NPV) displays based on portfolio hierarchy. |  |

#### Check Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Limit master records of your company was maintained in the system, the step [Generate Limit Utilizations](#unique_27) [page ] 39 was processed already

Prerequisite

'The Limit master records of your company was maintained in the system, the step [Generate Limit Utilizations](#unique_49) [page ] 78 was processed already.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics view displays. |  |
| 3 | Enter Selection Criteria | On the Overview of Utilizations - Selection Using all Characteristics view, enter the following data:Limit type: for example, Y01 or Y09Limit Utilization Base: for example, 1Determination Date: for example, <Current Date>Limits Valid From: for example, <Current Date> and choose Execute. | The system displays an overview of the limit utilizations in accordance with your selection criteria. |  |

#### Create Cross-Currency Interest Rate Swap Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you create an interest rate swap transaction.

Prerequisite

To test Option 2, make sure you have run the [Maintain Derived Flows for Business Partner (Optional)](#unique_11) [page ] 16 step.

Procedure

Option 1: Payment with Cross-Currency for IBOR

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create IR Derivative (TO01). | The Create Interest Rate Derivative: Initial Screen displays. |  |
| 3 | Enter Data on the Initial View | On the Create Interest Rate Derivative: Initial Screen view, enter the following data:Company Code: for example, 3310Product Type: for example, 62BTransaction Type: for example, 300Partner: for example, 33537001and choose Enter. | The Create Swap: Structure view displays. |  |
| 4 | Enter data on Create Swap: Structure view | On Create Swap: Structure view, enter data in the following groups:Term group:Start: for example, Current DateEnd: for example, Current Date next yearOutgoing Interest group:Nominal amount: for example, 2000,000.00AEDEffective From: for example, <Current Date>1st Due Date: for example, <First day of (Current month + 3 months)>Freq.Month: for example, 3Fix.Rate: for example, 3.5Int. Calc.Method: for example, select 2 act/360Business Calendar group:Calendar 2: for example, leave blankIncoming Interest group:Nominal amount: for example, 2000,000.00USDNote The amount is for testing purpose. You can change the account according to the real business.Effective From: for example, <Current Date>1st Due Date: for example, <First day of (Current month + 3 months)>Freq.Month: for example, 3Var. Interest: for example, USDM03LIBInt. Calc.Method: for example, 2 act/360Contract Conclusion group:Contract Date: for example, <Current Date>Stay in this view for the following step. | The Interest Rate Swap's data on Structure tab is entered. |  |
| 5 | Enter First Period Interest Rate for Variable Leg | Choose Condition – Incoming Side,On the Overview of Conditions view, double-click CTyp 1200 Interest and enter the following data:First Int Rate: for example, 3.2Choose Back twice to return to the Create Swap: Structure view | First period initial interest rate is entered. |  |
| 6 | Check Outgoing Interest Flows | On the Create Swap: Structure view, choose the Conditions - Outgoing Side, and the outgoing interest flows display. | The outgoing interest flows are reviewed. |  |
| 7 | Check Incoming Interest Flows | Choose the Incoming tab, the incoming interest flows display. | The Incoming interest flows are reviewed. |  |
| 8 | Validate the General Valuation Class | Choose the Administr. tab to review the general valuation class to ensure the class is correct. Stay in this view for the following step. | Correct general valuation class is selected. |  |
| 9 | Create Payment Request for Outgoing Interest Flows | Choose the Payment Details tab and double click on the currency line with currency AED.The Create Swap: Payment Details view displays.Ensure the following data is correctly entered:Payment Request: for example, select WithHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, TAt the bottom of the view, choose Payment details overview.Double-click the currency line with the currency value USDPayment Request: for example, select WithHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/Payee: for example, 33537001Partner Bank: for example, USD1Payment Methods: for example, TFand choose Save.Note If a window of Check Run: Trans.: Display messages appears, choose Continue (Enter). | Financial transaction saved under number …. message is displayed. Note down the transaction No.. |  |

Option 2: Payment with Cross-Currency if you want to use SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create IR Derivative (TO01). | The Create Interest Rate Derivative: Initial Screen displays. |  |
| 3 | Enter Data on the Initial View | On the Create Interest Rate Derivative: Initial Screen view, enter the following data:Company Code: for example, 3310Product Type: for example, 62BTransaction Type: for example, 300Partner: for example, 33537001and choose Enter. | The Create Swap: Structure view displays. |  |
| 4 | Enter data on Create Swap: Structure view | On Create Swap: Structure view, enter data in the following groups:Term group:Start: for example, <Current Date>End: for example, <the current date of next month>Outgoing Interest group:Nominal amount: for example, 2000,000.00 AEDEffective From: for example, <Current Date>1st Due Date: for example, <the current date of next month>Freq.Month: for example, 1Fix.Rate: for example, 3.5Int. Calc.Method: for example, select 2 act/360Business Calendar group:Calendar 2: for example, leave blankIncoming Interest group:Nominal amount: for example, 2000,000.00 USDNote The amount is for testing purpose. You can change the account according to the real business.Effective From: for example, <Current Date>1st Due Date: for example, <the current date of next month>Freq.Month: for example, 1Var. Interest: for example, SOFRInt. Calc.Method: for example, 2 act/360Contract Conclusion group:Contract Date: for example, <Current Date>Stay in this view for the following step. | The Interest Rate Swap's data on Structure tab is entered. |  |
| 5 | Interest Rate | Choose Condition – Incoming Side.On the Overview of Conditions view, double-click CTyp 1200 Interest and enter the following data:Int calc.type: 5 Compound Interest CalculationInt.Calc. Method: 2 act/360Percentage Rate: 3.2Note If 6 Average Compound Interest Calculation is selected, the following fields under Average Interest Rate are displayed: and should maintained for example as following:Weighting: for example, L Based on Interest Rate Adjustment DateRounding: Round to the NearestDecimal Places: 4Spread: 1Choose Back to go back to the Overview of Conditions view. | First period initial interest rate is entered. |  |
| 6 | Interest Rate Adjustment | Double-click on condition type 1210 Interest rate adjustment in the Condition View.Make the following entries:Interest Rate Adjustment: 1 Regular 1 Calendar DaysIR Adj.Date: <effective date> for example, <current date>Calendar rule: 3 Previous Working DayInterest Rate Fixing Date: for example, Relative, - 1 Working daysLockout Period: 2 Working DaysChoose Back to go back to the Overview of Conditions view. | The condition type Interest rate adjustment is maintained. |  |
| 7 | Maintain Accumulating Condition | On the Overview of Conditions view, select the condition type 1200 Interest, then choose Create Accumulating Condition from the toolbar.In the pop up dialog box of Possible condition types, double click on condition type 1201 - Interest (accumulated).Eff.From: <the current date>Choose Back twice to return to the Create Swap: Structure view. | The condition type Interest (accumulated) is maintained. |  |
| 8 | Check Outgoing Interest Flows | On the Create Swap: Structure view, choose the Outgoing tab, and the outgoing interest flows display. | The outgoing interest flows are reviewed. |  |
| 9 | Check Incoming Interest Flows | Choose the Incoming tab, the incoming interest flows display.Choose Show/Hide Single Flows to show or hide the single interest flows 1200 - Interest. | The incoming interest flows are reviewed. |  |
| 10 | Validate the General Valuation Class | Choose the Administr. tab to review the general valuation class to ensure the class is correct. Stay in this view for the following step. | Correct general valuation class is selected. |  |
| 11 | Create Payment Request for Outgoing Interest Flows | Choose the Payment Details tab and double click on the currency line with currency AED.The Create Swap: Payment Details view displays.Ensure the following data is correctly entered:Payment Request: for example, select WithHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, TAt the bottom of the view, choose Payment details overview.Double-click the currency line with the currency value USDPayment Request: for example, select WithHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/Payee: for example, 33537001Partner Bank: for example, USD1Payment Methods: for example, Fand choose Save.Note If a window of Check Run: Trans.: Display messages appears, choose Continue (Enter). | Financial transaction saved under number …. message is displayed. Note down the transaction No.. |  |

Option 3: Payment With Single Settlement Currency if you want to use SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create IR Derivative (TO01). | The Create Interest Rate Derivative: Initial Screen is displayed. |  |
| 3 | Enter Data | Enter the following data, and choose Enter:Company Code: for example, 3310Product Type: for example, 62BTransaction Type: for example, 300Partner: for example, 33537001 | The Create Swap: Structure view is displayed. |  |
| 4 | Enter Data | Enter data in the following groups:In the Term group:Start: for example, <the current date>End: for example, <the current date of next month>In the Outgoing Interest group:Nominal Amount: for example, 2,000,000.00 AEDEffective From: for example, <the current date>1st Due Date: for example, <the current date of next month>Freq.Month: for example, 1Fix.Rate: for example, 3.5Int. Calc.Method: for example, 2 act/360In the Business Calendar group:Calendar 2: for example, <leave blank>In the Incoming Interest group:Nominal amount: for example, 2000,000.00 USDEffective From: for example, <the current date>1st Due Date: for example, <the current date of next month>Freq.Month: for example, 1Var.Interest: for example, SOFRInt. Calc.Method: for example, 2 act/360In the Contract Conclusion group:Contract Date: for example, <the current date>Stay in this view for the following step. | The Interest Rate Swap's data on Structure tab is entered. |  |
| 5 | Enter Settlement Currency | Enter Settlement Currency:Settlement Crcy: for example, AED |  |  |
| 6 | Enter Working Days Shift | In the Settlement section, enter following data:Fix Reference ID: <select a proper fix reference ID>Fix Rel.to: Due DateDir.: -Working Days: 2Cal.1: EU |  |  |
| 7 | Create Nominal Changes for Outgoing Side | In the Outgoing Interest section, choose Create Nominal Changes. In the Nominal Amounts dialog box, change Flow Type from 1100 to 1105.Choose Adopt data. |  |  |
| 8 | Create Nominal Changes for Incoming Side | In the Incoming Interest section, choose Create Nominal Changes. In the Nominal Amounts dialog box, change Flow Type from 1100 to 1105.Choose Adopt data. |  |  |
| 9 | Check and Enter Incoming Interest Flows | Choose Condition - Incoming Side.On the Overview of Conditions view, double-click on condition type 1200 Interest and change it to 1205. Enter the following data:Int calc.type: 5 Compound Interest CalculationInt.Calc. Method: 2 act/360Percentage Rate: 3.2Choose Back.In the Overview of Conditions view, double-click on condition type 1120, and change it to 1125Choose Back. | First period initial interest rate is entered. |  |
| 10 | Interest Rate Adjustment | Double-click on condition type 1210 Interest rate adjustment in the Condition View.Make the following entries:Interest Rate Adjustment: 1 Regular 1 Calendar DaysIR Adj.Date: <effective date>, for example, <current date>Calendar rule: 3 Previous Working DayInterest Rate Fixing Date: for example, Relative, - 1 Working daysLockout Period: 2 Working DaysChoose Back to go back to the Overview of Conditions view. | The condition type Interest rate adjustment is maintained. |  |
| 11 | Maintain Accumulating Condition | On the Overview of Conditions view, select the condition type 1205 Interest (to be netted), then choose Create Accumulating Condition from the toolbar.In the pop up dialog box of Possible condition types, double click on condition type 1206 - Interest Accum (to be netted).Eff.From: <the current date>Choose Back twice to return to the Create Swap: Structure view. | The condition type Interest Accum (to be netted) is maintained. |  |
| 12 | Check and Enter Outgoing Interest Flows | On the Create Swap: Structure view, choose the Conditions- Outgoing side.On the Overview of Conditions view, double-click on condition type 1200, and change it to 1205.Choose Back.On the Overview of Conditions view, double-click on condition type 1120, and change it to 1125.Choose Back twice to go back to the Create Swap: Structure screen.On the Create Swap: Structure view, choose the Outgoing tab, and the outgoing interest flows are displayed. | The outgoing interest flows are reviewed. |  |
| 13 | Check Cash Flow | Switch to the Cash Flow tab.Make sure the derived flow 1107 for nominal netting and 1250 for interest netting are generated automatically.Choose Show/Hide Single Flows to show or hide the single interest flows 1205 Interest (to be netted). | 1107 for payment net and 1250 for interest net are generated. |  |
| 14 | Validate the General Valuation Class | Choose Administr. tab to review the general valuation class to ensure the class is correct. Stay in this view for the following step. | Correct general valuation class is selected. |  |
| 15 | Create Payment Request for Outgoing Interest Flows | Choose Payment Details tab, and double-click on the outgoing AED row with direction -.Ensure the following data is correctly entered:Payment Request: WithHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, TFAt the bottom of the view, choose Payment details overview.Double-click on the outgoing USD row with direction -Payment Request: for example, select WithHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/Payee: for example, 33537001Partner Bank: for example, USD1Payment Methods: for example, TFChoose Save. | Financial transaction saved under number XXXX message is displayed. Note down the transaction number. |  |

#### Correspondence

Purpose

Information related to SAP Treasury Risk Management transactions transferred between you and your business partner. SAP Treasury Risk Management provides standard correspondence functionalities to use for communicating with a business partner by email or through a printout form.

Prerequisites

The Preliminary Step section outlines the initial steps for setting up correspondence. Complete those procedures before continuing.

Procedure

This section describes the standard correspondence functionality that SAP Treasury Risk Management provides.

##### Set Settlement Status (Manual)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a treasury risk management transaction is recorded and saved, the transaction must be settled before further activities. Once you get counterparty confirmation, you can settle the transaction in one of two ways:

- Manual settlement

For example, if you receive counterparty confirmation e-mail, you can use the Process IR Derivatives (Subtitle: Collective Process) app to settle the transaction manually.

- Automatic settlement via correspondence process

For example, when a transaction has all the outgoing correspondence objects and incoming correspondence objects matched and set to completed status, the financial transactions is automatically set to settlement status.

This procedure describes settling the treasury risk management transaction manually.

Prerequisite

A treasury risk management transaction is created and available for this procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process IR Derivatives - Collective Processing (TI92). | The Collective Processing: Interest Rate Derivatives view displays. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute:Company Code: for example, 3310Transaction: <Transaction Number created previously> | The transaction is displayed in the Collective Processing: Interest Rate Derivatives view. |  |
| 4 | Settle the Transaction | Select the checkbox at the beginning of the transaction line and choose Settle. | The Settle OTC Interest Rate Instrument: Initial Screen view displays with the transaction data. |  |
| 5 | Save the Change | Choose Save.Note If the Check Run: Trans.:Display messages dialog box displays, choose Continue (Enter). | The transaction is settled and saved.The Collective Processing: Interest Rate Derivatives view displays. |  |
| 6 | Check the Status of the Transaction | Select the checkbox and choose Display. | The Display Swap, Structure view displays. |  |
| 7 | Check the Status of the Transaction | Choose Navigation Menu and choose Status. The Activity Cat field should have the following status: Contract settlement. | The Display Swap: Status view displays the transaction that has a Contract settlement status. |  |

##### Correspondence with PDF Form

Purpose

E-mail and print are both PDF form-related outputs. By default, SAP provides business profiles for several PDF forms (for example, PR_PRINT and PR_EMAIL).

- For any business partner assigned the profile PR_PRINT, when a financial transaction is created, a PDF form is sent to predefined print queue. You can view and print the PDF file via the Maintain Print Queues (F1260) SAP Fiori app. Once you verify that the transaction information on the form is correct, you can send the paper copy of the form to the business partner.
- For any business partner assigned profile PR_EMAIL, when a transaction is created, SAP automatically sends e-mails to the Business Partner.
- Once you receive the counterparty confirmation about the transaction from your Business Partner, you can settle all the correspondence objects of the transaction. Once all the correspondence objects are settled, the transaction status changes to Contract Settlement status.

Use the following apps to maintain your own settings for output:

- Output Parameter Determination. You maintain your own rules for the output. For example, you can maintain e-mail address of recipients. This rule overwrites the e-mail address of the Business Partner for an external counterparty, or it overwrites the e-mail address of User IDs for an internal counterparty.
- Maintain Email Templates - Deprecated (F1306). You maintain your own e-mail template with this app.
- Maintain Form Templates (F1434). You maintain your own form template with this app.

In the procedures in this section, you settle the treasury risk management transaction via the correspondence processing automatically.

Prerequisites

A new treasury risk management transaction must be created, as described in the previous step, since the transaction is manually settled.

###### Send Confirmation Email/Print

Purpose

SAP provides the best practices business partner group, BPG_DEFAULT. By default, if any business partner is assigned to this group, correspondence objects are automatically sent when a financial transaction is saved. As described in the Preliminary Steps section, the best practices business partner, 33537001, is assigned to BPG_GROUP, so the correspondence objects are sent automatically. However, if you use configuration step Define Business Partner Group to create new business partner groups and then do not assign the auto-send attribute, you must send those correspondence objects manually using the Send Correspondence (FTR_COSEND) app.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

The automated procedure does not require you to do any operation in-system.

###### Check Correspondence Status

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

###### Receive Incoming Confirmation

Purpose

In the prior procedure, an outbound email is sent to the business partner. Typically, you receive counterparty confirmation from the business partner via email, phone, or other channels. This procedure takes place outside of the system.

Procedure

This procedure does not require any operation from the system.

###### Find Deal and Match Deal Details

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
| 3 | Enter Selection Criteria on the Initial View | Enter the following data and choose Execute:Correspondence group:Company Code: for example, 3310Deal group:Company Code: for example, 3310Deal Number: for example, <Transaction Number>Note Make a note of the correspondence key for a COUNTERPARTY correspondence object. | Please note down the correspondence key numbers for COUNTERPARTY PRINT and COUNTERPARTY EMAIL. |  |
| 4 | Create | Choose Create. | The Options for Creating Correspondence Objects view displays. |  |
| 5 | Create an Incoming Correspondence Object Referring to the Outgoing Correspondence Object | Enter the following data for groups and press Enter:Display Options group:Corresp. Category: 01 Transaction ActivitiesTransaction Details group:Company Code: for example, 3310Product Type: for example, <Product type you entered in the transaction>Incoming/Outgoing: I IncomingEntry Options: 05 Correspondence object as templateTemplate for Correspondence Object Data group:Correspondence Key: for example, <Enter the correspondence key number for COUNTERPARTY PRINT from the previous step> |  |  |
| 6 | Save | Choose Save.Note If the Automatic matching proposal view displays, choose Cancel. | The incoming correspondence object is created successfully and displayed on Correspondence monitor - Standard View view. |  |
| 7 | Match the Incoming Correspondence Object with the Outgoing Correspondence Objects for channel PRINT | Select the checkbox for the incoming correspondence object and choose Status Functions > Automatic Match. | The Automatic matching proposal view displays. |  |
| 8 | Outgoing Correspondence | On the left-side of the view, expand the incoming correspondence key. All outgoing correspondence objects of the transaction are displayed.Select all the checkboxes of the outgoing correspondence objects and choose Enter. | All the outgoing COUNTERPARTY PRINT correspondence objects of the transaction now have status completed.All the INTERNAL outgoing correspondence objects remain in Delivered status. |  |
| 9 | Match the Incoming Correspondence Object with the Outgoing Correspondence Objects for channel EMAIL | Repeat the above steps to create an incoming correspondence object for COUNTERPARTY EMAIL and match it with outgoing correspondence for channel EMAIL. |  |  |

###### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the previous procedure, all the correspondence objects of the transaction are successfully matched. The standard functionality provides that the transaction is settled automatically.

In this procedure, you verify that the transaction settled automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Correspondence group:Company Code: for example, 3310Deal tab:Company Code: for example, 3310Deal Number: for example, <Transaction Number> | The Correspondence monitor - Standard View displays. |  |
| 4 | Display Transaction History | Select the checkbox of the incoming correspondence object and choose Show Underlying. | The History of OTC Interest Rate Instrument: Activity Sequence view displays. The second line shows Activity 2 Contract Settlement. |  |

#### Principal Payment

Purpose

The procedures in this section describe payment handling for a principal amount of cross-currency interest rate swap transaction, and posting to G/L accounting.

##### Fix FX Rate for Principal Payment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you adjust the foreign exchange rate for principal payment.

|  |
| --- |
| Note This step is only relevant if you need to create a CCS payment with the single settlement currency option. Otherwise you can skip this step. |

Prerequisite

You've settled the transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Adjustment - Rates/Prices (TI10) | The Create Rate/Price Adjustment view is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Enter:Foreign Exchange Rate Adjustment: <select>Company Code: for example, 3310Transaction: <transaction number from the previous procedure> | The Create Rate/Price Adjustment view is displayed. |  |
| 4 | Enter Foreign Exchange Rate | Choose and double click on the Principal Payment flow.Enter the following data and choose Save:EUR/USD =: for example, 1.2 | The rate/price is adjusted. |  |

##### Corporate Initial Payment

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows screen, enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
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

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request is selected as required (usually only for outgoing payment). The treasury back office uses the Pay Only functionality in from the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows requiring a payment request. The request does not create a posting in financial accounting.

If the payment is initiated by the financial partner, skip this procedure and begin the Process Payment Request procedure that follows the Bank Initiated Payment procedure.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding procedure in Appendix. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted, for example, <current date>Test Run: <Select>Pay Only:<Select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the system displays the message No flows exist for processing, no payment with payment request is required for your selection criteria. Skip to the [Post to General Ledger](#unique_62) [page ] 109 procedure. |  |
| 4 | Production Run | Choose Back.Change the following data and choose Run:Test Run: <Deselect> | The Payment Log view displays. The payment request is generated.Note Make note of the key number displayed on this view for use in the following procedures. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <current date>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back. | The Fix and Pay Flows view displays. |  |
| 5 | Production Run | Enter the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays and a payment request is generated.Note Make note of the key number displayed on this view as the number is required for other procedures. |  |

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

A payment request was generated in previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests view displays. |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters view displays. |  |
| 4 | Enter Parameters | Enter the following data and choose Dynamic selections:Posting Date: for example, <current date>Next payment run on: for example, <current date + 12 Months>Company Code: for example, 3310Payment Methods: for example, TF | The Free Selection for payment run dialog box displays. |  |
| 5 | Key Number | Make the following entries and choose Save:Key number: <the key number you noted from the previous procedure> |  |  |
| 6 | Additional Log | Choose Additional Log. | The Additional Log dialog box displays. |  |
| 7 | Enter Criteria | Make the following entries and choose Continue:Payment method selection in all cases: <select>Line items of the payment documents: <select>Due date check: <select>Note If the system displays the message Log created for all accounts, choose Continue. | The Automatic Payment Transactions: Parameters view displays. |  |
| 8 | Save | Choose Save. | The Automatic Payment Transactions for Payment Requests view displays the message Parameters have been entered. |  |
| 9 | Schedule Proposal | Choose Proposal. | The Schedule Proposal dialog box displays. |  |
| 10 | Schedule Proposal | Select Start Immediat. and choose Schedule Job. | The system displays the message Proposal is running with yellow traffic light status. |  |
| 11 | Schedule Proposal | Choose Status until the system displays the message Payment proposal has been created with green traffic light status. | The payment proposal is generated. |  |
| 12 | Schedule Payment | Choose Pmnt run. | The Schedule Payment dialog box displays. |  |
| 13 | Schedule Payment | Select Start Immediat., choose Create Payment Medium, and choose Schedule Job. | The system displays the message Payment run is running with yellow traffic light status. |  |
| 14 | Schedule Payment | Choose Status until the system displays the message Payment run has been carried out with green traffic light status. | The payment document is created.If SAP Bank Communication Management is not implemented in your system, the payment medium is created with a PMW format. Review the log by choosing Display payment log.If SAP Bank Communication Management is implemented in your system, the Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media message displays by choosing the Display payment log, indicating that a bank communication management batch must be created after the payment run. Proceed to the next test step. |  |
| 15 | Cross-Payment Run Payment Media (Create Bank Communication Management Batch) | Note This step (and the next step) is only necessary if SAP Bank Communication Management is implemented on your system. Otherwise, skip these steps.On the Automatic Payment Transactions for Payment Requests view, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium . | The Creation of Cross-Payment Run Payment Media view displays. |  |
| 16 | Cross-Payment Run Payment Media (Create Bank Communication Management Batch) | Make the following entries and choose Run:Run Date: for example, <current date>Identification: for example, TRM01R | When a Creation of Cross-Payment Run Payment Media dialog box appears with a Collector XX/XX/20XX XXXXXX was created or updated message, the bank communication batch is created.Note A batch may require additional approvals before payment medium is finally created. For more information, see the Advanced Cash Operations(J78)scope item. |  |

###### Send Payment Medium File

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

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this app to generate the posting for incoming payment. In this procedure, it does not create a posting for outgoing payment that you processed in previous Generate Payment Request procedure using the Pay Only option.
- Process Business Transactions: Use this app to generate the posting for outgoing payment that you processed in previous Generate Payment Request procedure using the Pay Only option.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Prerequisite

The outgoing payment handled by the payment request for this transaction was processed in the previous Generate Payment Request procedure using the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Execute:Derivatives: SelectedCompany Code: for example, 3310Transaction: <transaction number with inflow created in previous procedure>Up to and Including Due Date: enter date the flow of the financial transaction is posted, for example, <current date>Test Run: SelectedPost Operational Only: Selected | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run.If the system displays the message No flows exist for processing, no posting is required for your selection criteria. Skip the Production Run step and continue the test step using theProcess Business Transactions app. |  |
| 4 | Production Run | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: Deselected | The Posting Log: Posted Business Transactions view displays. An accounting document is created for incoming payment in local GAAP (valuation area AE0). |  |
| 6 | Access the SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany Code: for example 3310Valuation Area: for example, AE0Limit by Subledger Pos.: SelectedTransaction: <transaction number with outflow, and its payment request has been generated with the Generate Payment Request procedure>Test Run: Selected | The Test Run: Post/Reverse Business Transactions view displays.Note If the You have not selected any business transactions message displays, no posting is required for your selection criteria. Skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All, choose Choose Those to Post, and choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view displays. |  |
| 9 | Check Test Run Result | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run. |  |
| 10 | Enter Selection Criteria for Production Run | Choose Back.Change the following data and choose Execute:Test Run: Deselected | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 11 | Production Run | Choose Select All, choose Choose Those to Post, and choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view displays. |  |
| 12 | Production Run | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Period-End Closing

Purpose

The procedures in this section describe activities for period-end closing (usually executed at month-end), including:

- Accrue interest income or expenses
- Calculate or maintain fair value of transactions
- Perform key date valuation

##### Run Accrual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this function to accrue interest expenses and interest income based on existing financial instruments and reflect results correctly in the general ledger. The function distributes the amount correctly, based on the time period from flow start date to the key date, irrespective of when they are due for payment or received.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log n | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Accrual/Deferral (TPM44). | The Execute Accrual/Deferral of Expenses and Revenues view displays. |  |
| 3 | Test Run | Make the following entries and choose Execute:OTC Transactions: <select>Company code: for example, 3310Valuation Area: for example, AE0Transaction: <Transaction numbers created in previous procedures>Accrual/Deferral Key Date: for example, <the last date of current month>Include Key Date: <select>Test Run: <select> | The Execute Accrual/Deferral of Expenses and Revenues view displays. Review the accrual information.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Note No posting is created because it is a test run. |  |
| 4 | Production Run | Choose Back to return to the initial view of the app.Change the following data and choose Execute:Test Run: <deselect> | The Execute Accrual/Deferral of Expenses and Revenues view displays. Review the accrual information.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Because this is a production run, the accounting document is created in local GAAP (valuation area AE0).. |  |

##### Calculate or Maintain Fair Value of Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you determine the fair values, net present value (NPV) of financial transactions.

The net present values can be calculated automatically by the Market Risk Analyzer (MRA) and saved to VTVBAR table. These values can then be used for the accounting valuation. In addition, you can also maintain the relevant net present value manually.

Predelivered configuration in the Market Risk Analyzer (MRA) component of SAP Treasury Risk Management provides three options when calculating NPV automatically by the Calculate Net Present Values (Subtitle: with CVA and DVA)app:

- Risk-free NPV: Uses the evaluation type that does not contain basis spread curve or credit spread curve as the system only calculates the risk-free NPV.
- Risk-based NPV with Credit Spread Curve: Uses the evaluation type that contains credit spread curve. The system calculates risk-free NPV by using risk-free yield curve, and calculates the (risk-based) NPV, also accounting for credit spreads.
- Risk-based NPV with Basis Spread Curve and Credit Spread Curve: Uses the evaluation type that contains basis spread curve and credit spread curve. The system calculates risk-free NPV by using risk-free yield curve and basis spreads curve, and calculates the (risk-based) NPV that also accounts for credit spreads.

There are two types of calculation methods for CVA (credit value adjustment) and DVA (debit value adjustment). The first calculation method is Based on Expected Exposures and the second calculation method is called the Difference method.

NPV = risk-free NPV - CVA - DVA.

Prerequisite

Before calculating NPV with the Calculate Net Present Values - with CVA and DVA app, ensure relevant market data (interest rates, foreign exchange rates, credit spreads, and so on) are maintained for the evaluation date. For more information about market data maintenance, see the Market Rates Management – Manually via Upload (1XN) test script.

Procedure - Option 1: Calculate NPV Automatically

|  |
| --- |
| Note By default, Yield Curve Type 9001 is defined with reference rate SOFR/ESTER; Yield Curve Type 0001 is defined with reference rate IBOR; Evaluation Type is defined with Yield Curve Type 0001 only. If you want to use SOFR, ESTER, SONIA, SARON, TONAR, CORRA, you can choose to use SAP pre-delivered content, or set up your own yield curves, evaluation type, basis spreads and basis spread curves via relevant SSCUIs based on these reference rates. |

|  |
| --- |
| Note To schedule a background job for option 1, see the corresponding step in the Appendix. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments view displays. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute:Evaluation Parameter Derivatn: DeselectedSelect OTC Transactions: SelectedCompany Code: for example, 3310Transaction: <Transaction numbers created in previous procedures>Evaluation Date: for example, <last date of current month>CVD/DVA Type:To calculate risk-free NPV, leave blank.To calculate risk-based NPV and CVA/DVA, enter Y01.Evaluation Type:To calculate risk-free NPV, enter Y001Determine NPVs Including Credit and Debit Value To calculate risk-based NPV and CVA/DVA, enter Y002Test Run: DeselectedPrice/NPV Type: 001Save Values with Warnings: SelectedDetail Log: Selected | The NPVs including CVA/DVA from the Market Risk Analyzer view displays with the NPV, risk-free NPV, CVA, DVA of each transaction on this view.You can also review different information by selecting additional buttons on this view:Single Transaction:CVA/DVA Key FiguresDetailed LogCalculation BasesError Log |  |

Procedure - Option 2: Maintain NPV Manually

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Net Present Values (F7601). | The Manage Net Present Values screen displays. |  |
| 3 |  | Choose Create. | The Net Present Value Data screen displays. |  |
| 4 | Enter Header | Make the following entries:Transaction: <transaction numbers created in previous steps>Company Code: for example, 3310Price / NPV Type: 001Effective from: for example, <last date of current month> |  |  |
| 5 | Enter Net Present Value Details | Make the following entries and choose Create:NPV Currency: for example, AEDNet Present Value: <the value of (risk-based) NPV>Risk-Free Net Present Value: <the value of risk-free NPV>CVA: <the value of CVA>DVA: <the value of DVA>Note To reflect credit spreads for accounting valuation, maintain the risk-based NPV in the Net Present Value field, then enter CVA/DVA, which is the difference between risk-free NPV and risk-based NPV, Net Present Value (NPV) = risk-free NPV - CVA - DVA. Otherwise, also enter the value of risk-free NPV in the Net Present Value field, and leave fields CVA and DVA blank. | Manually maintained NPV is saved. |  |

|  |
| --- |
| Note You can also use SAP Fiori app Enter Net Present Values (JBNPV) to maintain NPV manually. |

##### Perform Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The valuation function values the positions of financial instruments - based on historical cost or fair value for a given key date - and transfers results to financial accounting.

|  |
| --- |
| Note To schedule a background job for this step, see the corresponding step in the Appendix section. |

Prerequisite

Fair values (Net Present Values (NPV)) are calculated or maintained for financial transactions that are evaluated at fair value (NPV) according to accounting principles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Run Valuation view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:In the Product Groups area,OTC Transactions: <select>In the General Selections area,Company code: for example, 3310Valuation Area: for example, AE0Transaction: <Transaction numbers created in previous procedures>In the Valuation Parameters area,Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation with ResetNote When the Period End is also the Year End, use the Valuation Category of Year End ValuationTest Run: <select> | The Display Selected Treasury Positions for Valuation view displays. |  |
| 4 | Execute Test Run Valuation | Choose Run Valuation.Note If the Message dialog box displays, choose Continue. | The Valuation Log view displays.If an entry has a red traffic light status, select and review the error message. Correct the issue and perform test run again, until the error is resolved.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Note If there is no simulated posting, your selected transaction does not require valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until your return to the Run Valuation area is displayed.Change the following data and choose Execute:Test Run: <deselect> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 6 | Execute Valuation for Production Run | Choose Run Valuation. | The Valuation Log view displays.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Because this is a production run, the accounting document is created in local GAAP (valuation area AE0). |  |

#### Interest Rate Adjustment

Purpose

The procedures under this section describe activities for interest rate adjustment, including:

- Interest Rate Adjustment Schedule Report
- Adjust Interest Rate

##### Interest Rate Adjustment Schedule Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you get an overview of interest rate adjustments.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Adjustment Schedule - Rates/Prices (TJ07). | The Rate/Price Adjustment Schedule screen is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Select Interest Rate Adjustment: <select this checkbox>Company code: for example, 3310Product Type: for example, 62B | The overview of rate or price adjustment is displayed. |  |

##### Adjust Interest Rate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you adjust the interest rate for the reference interest rate.

Prerequisite

You have maintained the reference interest rate, according to the Enter Interest Rates step in the Market Rates Management – Manually via Upload test script is maintained on the fixing date.

Procedure - Option 1: Interest Rate Adjustment (Automatically)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Automatic Adjustments - Rates/Prices (TJ05). | The Run Automatic Rate/Price Adjustment screen is displayed. |  |
| 3 | Enter Parameter of Adjustment | Enter the following data and choose Execute:Select Interest Rate Adjustment: <select>Company Code: for example, 3310Fixing Date: for example, <the fixing date you noted down from the previous procedure>All Transactions: <deselect>Single Transactions: <the transaction number noted down from the previous procedure>Test Run: <deselect> | The interest rate adjustment of fixing date process automatically runs. |  |

Procedure - Option 2: Interest Rate Adjustment (Manually)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Adjustment - Rates/Prices (TI10) | The Create Rate/Price Adjustment screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Enter:Select Interest Rate Adjustment: <select>Company Code: for example, 3310Transaction: <the transaction number from the previous procedure> |  |  |
| 4 | Enter Interest Rate | Enter the following data, and choose Save:Interest Rate: for example, 7 | The manual interest rate adjustment is created. |  |

#### Interest Payment

Purpose

The procedures in this section describe handling the payment for interest of the Interest Rate Swap transaction and posting it to G/L accounting.

Prerequisites

You can only trigger the payment and posting of flows for a transaction in Contract Settlement status.

##### Fix FX Rate for Interest Payment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you adjust the foreign exchange rate for interest payment.

|  |
| --- |
| Note This step is only relevant if you need to create a CCS payment with the single settlement currency option. Otherwise you can skip this step. |

Prerequisite

You have settled the transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Adjustment - Rates/Prices (TI10) | The Create Rate/Price Adjustment view is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Enter:Foreign Exchange Rate Adjustment: <select>Company Code: for example, 3310Transaction: <transaction number from the previous procedure> | The Create Rate/Price Adjustment view is displayed. |  |
| 4 | Enter Foreign Exchange Rate | Choose and double click on one Interest flow.Enter the following data and choose Save:EUR/USD =: for example 1.2 | The rate/price is adjusted. |  |
| 5 | Enter Foreign Exchange Rate | Maintain and save foreign exchange rate for all other interest flows. | The rate/price is adjusted. |  |

##### Display Payment Schedule

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules view displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Execute:OTC Transactions: SelectedCompany code: for example, 3310End of Term in the Future: SelectedEnd of Term in Lapsed: SelectedPayment Period: for example, <Current Date>to <Current Date + 12 months>Payment Status: for example, 1Output Error Log: Selected | The payment schedule report appears for your review.Note Make a note of the transaction number and payment date displayed on this view for use in additional procedures, for example, process payment. |  |

##### Corporate Initial Payment

###### Option1: Generate and Automatically Process Payment Request

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <Payment Date you noted in previous procedure>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows screen, enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <Payment Date you noted in previous procedure>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

###### Option2: Generate and Process Payment Request

###### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request is selected as required (usually only for outgoing payment, in practice). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows that require payment request. It does not create a posting in financial accounting,

When payment is initiated by the financial partner, skip this procedure and the Process Payment Request procedure and continue with the Bank Initiated Payment procedure.

|  |
| --- |
| Note To schedule a background job for this step, see the corresponding step in the Appendix. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Run:Derivatives: SelectedCompany Code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <Payment Date you noted in previous procedure>Test Run: <select>Pay Only: <select> | The Payment Log - Test Run displays. Review the payment information on this view.If the No flows exist for processing message displays, no payment is required for the payment request according to your selection criteria. Skip to the [Post to General Ledger](#unique_73) [page ] 131 procedure. |  |
| 4 | Production Run | Choose Back.Change the following data and choose Run:Test Run: <deselect> | The Payment Log view displays and a payment request is generated.Note Make note of the key number displayed on this view as the number is required for other procedures. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number you noted from the previous procedure>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <Payment Date you noted in previous procedure>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back. | The Fix and Pay Flows view displays. |  |
| 5 | Production Run | Enter the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays and a payment request is generated.Note Make note of the key number displayed on this view as the number is required for other procedures. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items) but on payment requests.

Prerequisite

The payment request is generated in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests view displays. |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters view displays. |  |
| 4 | Enter Parameters | Enter the following data and choose Dynamic Selections:Posting Date: for example, <current date>Next payment run on: for example, <current date + 12 Months>Company Code: for example, 3310Payment Methods: for example, TF | The Free Selection for payment run dialog box displays. |  |
| 5 | Enter Parameters | Enter the following data and choose Save:Key number: <the key number you noted from the previous procedure> |  |  |
| 6 | Enter Parameters | Choose Additional Log. | The Additional Log dialog box displays. |  |
| 7 | Enter Parameters | Make the following entries and choose Continue:Payment method selection in all cases: <select>Line items of the payment documents: <select>Due date check: <select>Note If the Log created for all accounts message displays, choose Continue. | The Automatic Payment Transactions: Parameters view displays. |  |
| 8 | Enter Parameters | Choose Save. | The Automatic Payment Transactions for Payment Requests view displays the message Parameters have been entered. |  |
| 9 | Schedule Proposal | Choose Proposal. | The Schedule Proposal dialog box displays. |  |
| 10 | Schedule Proposal | Select Start Immediate and choose Schedule Job. | The system displays the message Proposal is running with a yellow traffic light status. |  |
| 11 | Schedule Proposal | Choose Status, until the system displays the message Payment proposal has been created with green traffic light status. | The payment proposal is generated. |  |
| 12 | Schedule Payment | Choose Pmnt run. | The Schedule Payment dialog box displays. |  |
|  |  | Select Start Immediat., select Create Payment Medium, and choose Schedule Job. | The system displays the message Payment run is running with yellow traffic light status. |  |
|  |  | Choose Status, until Payment run has been carried out message appears with green traffic light status. | The payment document is created.If SAP Bank Communication Management is not implemented in your system, the payment medium created uses the PMW format. To review, select the Display payment log.If SAP Bank Communication Management is implemented in your system, in the Display payment log, the Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media message displays. A bank communication management batch must be created after the payment run. Proceed to the following step. |  |
| 13 | Cross-Payment Run Payment Media (Create Bank Communication Batch) | The following step only applies if SAP Bank Communication Management is implemented in your system,On the Automatic Payment Transactions for Payment Requests view, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .Enter the following data and choose Run:Run Date: for example <current date>Identification: for example TRM01R | The Creation of Cross-Payment Run Payment Media dialog box appears and states that Collector XX/XX/20XX XXXXXX was created or updated confirming the bank communication management batch is created.Note A batch may require additional approvals before payment medium is finally created. For more information, see the Advanced Cash Operations(J78) scope item. |  |

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

When the outgoing payment is initiated by the bank, skip the Generate Payment Request and Process Payment Request procedures. No requests are required.

Procedure

When the bank initiates payment skip to the Post to General Ledger procedure.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): Use this app to generate the posting for incoming payment. When using this app for this procedure, it does not create posting for outgoing payment that you processed in previous Generate Payment Request procedure using the Pay Only option.
- Process Business Transactions (TPM10): Use this app to generate the posting for outgoing payment that you processed in previous Generate Payment Request procedure using the Pay Only option.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Prerequisite

The outgoing payment handled by the payment request for this transaction was processed in the previous Generate Payment Request procedure using the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Execute:Derivatives: SelectedCompany Code: for example, 3310Transaction: <transaction number with inflow created in previous procedure>Up to and Including Due Date: enter date the flow of the financial transaction is posted, for example, <current date + 1 Year>Test Run: SelectedPost Operational Only: Selected | Note The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created since this is a test run.If the No flows exist for processing message displays, no posting is required for your selection criteria. Skip the Production Run step and continue the test step using the Process Business Transactions (TPM10) app. |  |
| 4 | Production Run | Choose Back.Change the following data and choose Execute:Test Run: Deselected | The Posting Log: Posted Business Transactions view displays. An accounting document is created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 6 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany Code: for example, 3310Valuation Area: for example, AE0Limit by Subledger Pos.: SelectedTransaction: <transaction number with outflow and payment request generated with Generate Payment Request procedure>Test Run: Selected | The Test Run: Post/Reverse Business Transactions view displays.Note If the You have not selected any business transactions message displays, no posting is required for your selection criteria. Skip the current step. |  |
| 7 | Check Test Run Result | Select Select All, select Choose Those to Post, and choose Execute. | The Test Run: Display Posted/Reversed Business Transactions view displays. |  |
| 8 | Check Test Run Result | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created since this is a test run. |  |
| 9 | Enter Selection Criteria for Production Run | Choose Back.Change the following data and choose Execute:Test Run: Deselected | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 10 | Production Run | Select Select All, select Choose Those to Post, and choose Execute. | The Update Run: Display Posted/Reversed Business Transactions view displays. |  |
| 11 | Production Run | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Final Repayment

Purpose

Once the cross-currency interest rate swap transaction is matured, the final repayment is necessary. Possible payments include principle conclusion flows and interest flows.

The procedures in this section describe how to handle the final payment for cross-currency interest rate swap transactions and how to post it to G/L accounting.

Prerequisites

You can only trigger the payment and posting of flows for a transaction that is in the Contract Settlement status.

##### Fix FX Rate for Final Repayment (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you adjust the foreign exchange rate for final payment.

|  |
| --- |
| Note This step is only relevant if you need to create a CCS payment with the single settlement currency option. Otherwise you can skip this step. |

Prerequisite

You have settled the transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Adjustment - Rates/Prices (TI10) | The Create Rate/Price Adjustment view is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Enter:Foreign Exchange Rate Adjustment: <select>Company Code: for example, 3310Transaction: <transaction number from the previous procedure> | The Create Rate/Price Adjustment view is displayed. |  |
| 4 | Enter Foreign Exchange Rate | Choose and double click on the Final Repayment flow.Enter the following data and choose Save:EUR/USD =: for example 1.2 | The rate/price is adjusted. |  |

##### Display Payment Schedule

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules view displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:OTC Transactions: SelectedCompany code: for example, 3310End of Term in the Future: SelectedEnd of Term in Lapsed: SelectedPayment Period: for example, <Current Date> to <Current Date + 12 Months>Payment Status: for example, 1Output Error Log: Selected | You can check payment schedule report. Make a note of the transaction number and payment date displayed on this view you want to process payment: _________ __________ |  |

##### Corporate Initial Payment

###### Option 1: Generate and Automatically Process Payment Request

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <Payment Date you noted in previous procedure>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows screen, enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <Payment Date you noted in previous procedure>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, no payment is required for the payment request per your selection criteria and you can skip to the Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

###### Option 2: Generate and Process Payment Request

###### Generate Payment Request

Purpose

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Prerequisites maintain credit limit types Y01 and Y07 only, but the CCS Check Limit Utilization Report step selects limit type 'Y01 or Y09' (the IRS version says 'Y01 or Y07').

> [!warning] Conflict
> Flagged while digesting this document, not verified: Fair-value description differs between sections: IRS describes two NPV options and only the difference method for CVA/DVA, while the CCS section describes three options (adds basis spread curve) and two CVA/DVA methods (Based on Expected Exposures and Difference); the reference-rate list also differs (IRS lists SORA and HONIA, CCS stops at CORRA).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-interest-rate-derivatives-management-1x3-ae-sap-s-4hana-cl-part-02]]
- related-to :: [[05-treasury-and-cash-management/interest-rate-derivatives-management-group-ledger-ifrs-1xb-ae-test-scr]]
- related-to :: [[05-treasury-and-cash-management/interest-rate-derivatives-management-group-ledger-us-gaap-34e-ae-test]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X3_S4CLD2608_BPD_EN_AE.docx` — lines 1–3127 of the extracted text · extracted with `mammoth` · 440,263 chars in the whole document
