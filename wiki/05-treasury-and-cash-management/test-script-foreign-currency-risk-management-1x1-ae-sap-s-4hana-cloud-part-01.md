---
id: 05-treasury-and-cash-management/test-script-foreign-currency-risk-management-1x1-ae-sap-s-4hana-cloud-part-01
title: "Test Script: Foreign Currency Risk Management (1X1_AE) - SAP S/4HANA Cloud Public Edition 2608 (1X1_S4CLD2608_BPD_EN_AE) — part 1 of 2"
description: "SAP Best Practices test script for scope item 1X1 (UAE): FX risk management with exposure, hedging, FX forwards/swaps/NDFs/options, settlement, payment and posting."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/foreign-currency-risk-management]
aliases: []
keywords: [Foreign Currency Risk Management (FX Deals), foreign currency risk management, business partner master data, correspondence, limit management, hedge management, balance sheet fx risk, cash flow exposure, trade requests, fx transactions]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X1_S4CLD2608_BPD_EN_AE.docx#lines-1-3641"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-774
topic: 05-treasury-and-cash-management/foreign-currency-risk-management
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Foreign Currency Risk Management (1X1_AE) - SAP S/4HANA Cloud Public Edition 2608 (1X1_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X1_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–3641 of the extracted text), extracted with `mammoth`. Grouped under **Foreign Currency Risk Management (FX Deals)** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Foreign Currency Risk Management (1X1_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 8](#_Toc232848023)

[2 Prerequisites 9](#_Toc232848024)

[2.1 System Access 9](#_Toc232848025)

[2.2 Roles 9](#_Toc232848026)

[2.3 Master Data, Organizational Data, and Other Data 10](#_Toc232848027)

[2.4 Business Conditions 11](#_Toc232848028)

[2.5 Preliminary Steps 11](#_Toc232848029)

[2.5.1 Create Business Partner 11](#_Toc232848030)

[2.5.1.1 Maintain General Data for Business Partner 11](#_Toc232848031)

[2.5.1.2 Maintain Payment Details for Business Partner 14](#_Toc232848032)

[2.5.1.3 Maintain Authorizations for Business Partner 16](#_Toc232848033)

[2.5.1.4 Maintain Reporting Data in Company Code for Business Partner 17](#_Toc232848034)

[2.5.2 Correspondence 19](#_Toc232848035)

[2.5.2.1 Maintain Profile and BP Group Assignments to External Recipient 19](#_Toc232848036)

[2.5.2.2 Maintain Profile and BP Group Assignments to Internal Recipient 21](#_Toc232848037)

[2.5.3 Maintaining Credit Limit 24](#_Toc232848038)

[2.5.3.1 Maintain Limit with Limit Type Y01 24](#_Toc232848039)

[2.5.3.2 Maintain Limit with Limit Type Y07 25](#_Toc232848040)

[2.5.4 Maintain Trader and Trader Authorizations 26](#_Toc232848041)

[2.5.4.1 Define Traders 26](#_Toc232848042)

[2.5.4.2 Define User Data 27](#_Toc232848043)

[2.5.4.3 Maintain Trader Authorizations 28](#_Toc232848044)

[2.5.5 Exposure Management and Hedge Management 29](#_Toc232848045)

[2.5.5.1 Define Time Pattern 29](#_Toc232848046)

[2.5.5.2 Define Hedging Area 30](#_Toc232848047)

[2.5.5.3 Define Key Figures for Balance Sheet FX Risk 34](#_Toc232848048)

[2.5.5.4 Define Request Parameters for Balance Sheet FX Risk 36](#_Toc232848049)

[2.5.6 Define Fixing References 38](#_Toc232848050)

[2.5.7 Define Values for Expiry Time 40](#_Toc232848051)

[3 Overview Table 42](#_Toc232848052)

[4 Test Procedures 50](#_Toc232848053)

[4.1 Foreign Currency Risk Management and Accounting - Without Options 50](#_Toc232848054)

[4.1.1 (1XN) Market Rates Management – Manually via Upload 50](#_Toc232848055)

[4.1.2 (1S4) Automatic Market Rates Management 50](#_Toc232848056)

[4.1.3 Generate Limit Utilizations 51](#_Toc232848057)

[4.1.4 Analyze Cash Position 52](#_Toc232848058)

[4.1.5 Analyze Liquidity Forecast 52](#_Toc232848059)

[4.1.6 Balance Sheet Exposure Management 52](#_Toc232848060)

[4.1.6.1 Review Balance Sheet FX Risk 52](#_Toc232848061)

[4.1.6.2 Take Snapshot for Balance Sheet FX Risk 53](#_Toc232848062)

[4.1.6.3 Check and Process Snapshot Item 54](#_Toc232848063)

[4.1.6.4 Release Snapshot 56](#_Toc232848064)

[4.1.6.5 Review Balance Sheet FX Risk Based on Snapshot 56](#_Toc232848065)

[4.1.7 Cash Flow Exposure Management 57](#_Toc232848066)

[4.1.7.1 Collect Exposure Data 57](#_Toc232848067)

[4.1.7.2 Create Raw Exposure 58](#_Toc232848068)

[4.1.7.2.1 Create Raw Exposure using Exposure Management 2.0 58](#_Toc232848069)

[4.1.7.2.2 Create Raw Exposure using FX Exposure Management 61](#_Toc232848070)

[4.1.7.3 Take Snapshot for Cash Flow Exposure 62](#_Toc232848071)

[4.1.7.4 Review Cash Flow Net Exposure 64](#_Toc232848072)

[4.1.8 Analyze Exposure and Agree on Hedging Actions 65](#_Toc232848073)

[4.1.9 Create Trade Request 65](#_Toc232848074)

[4.1.9.1 Create Trade Request via Balance Sheet Exposure Hedge Request 65](#_Toc232848075)

[4.1.9.1.1 Generate Hedge Request 65](#_Toc232848076)

[4.1.9.1.2 Check and Process Hedge Request 67](#_Toc232848077)

[4.1.9.1.3 Release Hedge Request 68](#_Toc232848078)

[4.1.9.2 Create Trade Request via Cash Flow Exposure Hedge Request 69](#_Toc232848079)

[4.1.9.2.1 Generate Hedge Request 69](#_Toc232848080)

[4.1.9.2.2 Release Hedge Request 71](#_Toc232848081)

[4.1.9.3 Create Trade Request Manually 73](#_Toc232848082)

[4.1.10 Check Trade Request Status 74](#_Toc232848083)

[4.1.11 Check Limit Utilization Report 75](#_Toc232848084)

[4.1.12 Create Foreign Exchange Contract 76](#_Toc232848085)

[4.1.12.1 Create FX Spot/Forward 76](#_Toc232848086)

[4.1.12.2 Create FX Swap 78](#_Toc232848087)

[4.1.12.3 Create Non-Deliverable Forward 79](#_Toc232848088)

[4.1.13 (BFB) Basic Cash Operations 80](#_Toc232848089)

[4.1.14 (J78) Advanced Cash Operations 81](#_Toc232848090)

[4.1.15 Correspondence 82](#_Toc232848091)

[4.1.15.1 Set Settlement Status (Manual) 82](#_Toc232848092)

[4.1.15.2 Correspondence with PDF Form 83](#_Toc232848093)

[4.1.15.2.1 Send Confirmation Email / Print 84](#_Toc232848094)

[4.1.15.2.2 Check Correspondence Status 84](#_Toc232848095)

[4.1.15.2.3 Receive Incoming Confirmation 86](#_Toc232848096)

[4.1.15.2.4 Find Deal and Match Deal Details 86](#_Toc232848097)

[4.1.15.2.5 Set Settlement Status 88](#_Toc232848098)

[4.1.16 Period end has been reached 89](#_Toc232848099)

[4.1.16.1 Calculate or Maintain Fair Value of Transaction 89](#_Toc232848100)

[4.1.16.2 Perform Key Date Valuation 92](#_Toc232848101)

[4.1.17 Transaction is Mature 94](#_Toc232848102)

[4.1.17.1 For NDF 94](#_Toc232848103)

[4.1.17.1.1 Fix Rate for NDF 94](#_Toc232848104)

[4.1.17.1.2 Correspondence 95](#_Toc232848105)

[4.1.17.2 Payment for Mature Transaction 103](#_Toc232848106)

[4.1.17.2.1 Option 1: Generate and Automatically Process Payment Request 103](#_Toc232848107)

[4.1.17.2.2 Option 2: Generate and Process Payment Request 106](#_Toc232848108)

[4.1.17.2.3 Send Payment Medium File 111](#_Toc232848109)

[4.1.17.3 Bank-Initiated Payment 111](#_Toc232848110)

[4.1.17.4 Post to General Ledger 111](#_Toc232848111)

[4.1.17.5 Post Realized Profit and Loss 114](#_Toc232848112)

[4.2 Foreign Currency Risk Management and Accounting - With Options 116](#_Toc232848113)

[4.2.1 (1XN) Market Rates Management – Manually via Upload 116](#_Toc232848114)

[4.2.2 (1S4) Automatic Market Rates Management 116](#_Toc232848115)

[4.2.3 Generate Limit Utilizations 116](#_Toc232848116)

[4.2.4 Analyze Liquidity Forecast 117](#_Toc232848117)

[4.2.5 Balance Sheet Exposure Management 118](#_Toc232848118)

[4.2.5.1 Review Balance Sheet FX Risk 118](#_Toc232848119)

[4.2.5.2 Take Snapshot for Balance Sheet FX Risk 119](#_Toc232848120)

[4.2.5.3 Check and Process Snapshot Item 120](#_Toc232848121)

[4.2.5.4 Release Snapshot 121](#_Toc232848122)

[4.2.5.5 Review Balance Sheet FX Risk Based on Snapshot 122](#_Toc232848123)

[4.2.6 Cash Flow Exposure Management 123](#_Toc232848124)

[4.2.6.1 Collect Exposure Data 123](#_Toc232848125)

[4.2.6.2 Create Raw Exposure 123](#_Toc232848126)

[4.2.6.2.1 Create Raw Exposure using Exposure Management 2.0 124](#_Toc232848127)

[4.2.6.2.2 Create Raw Exposure using FX Exposure Management 127](#_Toc232848128)

[4.2.6.3 Take Snapshot for Cash Flow Exposure 128](#_Toc232848129)

[4.2.6.4 Review Cash Flow Net Exposure 130](#_Toc232848130)

[4.2.7 Analyze Exposure and Agree on Hedging Actions 131](#_Toc232848131)

[4.2.8 Create Trade Request 131](#_Toc232848132)

[4.2.8.1 Create Trade Request via Balance Sheet Exposure Hedge Request 131](#_Toc232848133)

[4.2.8.1.1 Generate Hedge Request 131](#_Toc232848134)

[4.2.8.1.2 Check and Process Hedge Request 133](#_Toc232848135)

[4.2.8.1.3 Release Hedge Request 134](#_Toc232848136)

[4.2.8.2 Create Trade Request via Cash Flow Exposure Hedge Request 135](#_Toc232848137)

[4.2.8.2.1 Generate Hedge Request 135](#_Toc232848138)

[4.2.8.2.2 Release Hedge Request 137](#_Toc232848139)

[4.2.8.3 Create Trade Request Manually 138](#_Toc232848140)

[4.2.9 Check Trade Request Status 140](#_Toc232848141)

[4.2.10 Check Limit Utilization Report 140](#_Toc232848142)

[4.2.11 Create FX Option Contract 141](#_Toc232848143)

[4.2.11.1 Create Plain Vanilla FX Option 142](#_Toc232848144)

[4.2.11.2 Create Zero/Low Cost Collar FX Option 143](#_Toc232848145)

[4.2.11.2.1 Option 1: Create Two Options Separately and Create Option Reference 144](#_Toc232848146)

[4.2.11.2.2 Option 2: Create Zero/Low Cost Collar FX Option in Single Step 148](#_Toc232848147)

[4.2.12 (BFB) Basic Cash Operations 151](#_Toc232848148)

[4.2.13 (J78) Advanced Cash Operations 151](#_Toc232848149)

[4.2.14 Correspondence 152](#_Toc232848150)

[4.2.14.1 Set Settlement Status (Manual) 152](#_Toc232848151)

[4.2.14.2 Correspondence with PDF Form 154](#_Toc232848152)

[4.2.14.2.1 Send Confirmation Email / Print 155](#_Toc232848153)

[4.2.14.2.2 Check Correspondence Status 155](#_Toc232848154)

[4.2.14.2.3 Receive Incoming Confirmation 157](#_Toc232848155)

[4.2.14.2.4 Find Deal and Match Deal Details 157](#_Toc232848156)

[4.2.14.2.5 Set Settlement Status 159](#_Toc232848157)

[4.2.15 Premium Payment 160](#_Toc232848158)

[4.2.15.1 Option 1: Generate and Automatically Process Payment Request 160](#_Toc232848159)

[4.2.15.2 Option 2: Generate and Process Payment Request 163](#_Toc232848160)

[4.2.15.2.1 Generate Payment Request 163](#_Toc232848161)

[4.2.15.2.2 Process Payment Request 165](#_Toc232848162)

[4.2.15.3 Send Payment Medium File 168](#_Toc232848163)

[4.2.15.4 Bank-Initiated Payment 168](#_Toc232848164)

[4.2.15.5 Post to General Ledger 168](#_Toc232848165)

[4.2.16 Period end has been reached 171](#_Toc232848166)

[4.2.16.1 Calculate or Maintain Fair Value of Transaction 171](#_Toc232848167)

[4.2.16.2 Perform Key Date Valuation 174](#_Toc232848168)

[4.2.17 Transaction is Mature 176](#_Toc232848169)

[4.2.17.1 Check the Manage Financial Transactions Report 176](#_Toc232848170)

[4.2.17.1.1 Decide to Exercise 177](#_Toc232848171)

[4.2.17.1.2 Create FX Spot Contract 178](#_Toc232848172)

[4.2.17.1.3 Decide to Expire 180](#_Toc232848173)

[4.2.17.2 Post Realized Profit and Loss 181](#_Toc232848174)

[4.3 Reporting 182](#_Toc232848175)

[4.3.1 Display Treasury Position Flows 182](#_Toc232848176)

[4.3.2 Display Treasury Alerts - Posting 183](#_Toc232848177)

[4.3.3 Display Treasury Alerts - Settlement, Release, Payment and Correspondence 184](#_Toc232848178)

[4.3.4 Display Payment Schedule 185](#_Toc232848179)

[4.3.5 Display Treasury Posting Journal 186](#_Toc232848180)

[4.3.6 Treasury Position Analysis 187](#_Toc232848181)

[4.3.7 Display Treasury Position Values 188](#_Toc232848182)

[4.3.8 Define Financial Positions 188](#_Toc232848183)

[4.3.9 Financial Status (Book Value) 190](#_Toc232848184)

[4.3.10 Display Treasury Payments 191](#_Toc232848185)

[4.3.11 Analyze NPV 191](#_Toc232848186)

[4.3.12 Calculate Market Risk Key Figures 192](#_Toc232848187)

[4.3.13 Sensitivity Key Figures 194](#_Toc232848188)

[4.3.14 Review Limit Utilization Report 195](#_Toc232848189)

[5 Appendix 196](#_Toc232848190)

[5.1 Exposure Management 196](#_Toc232848191)

[5.1.1 Overview of Raw Exposures 196](#_Toc232848192)

[5.1.2 Process Exposure Positions 197](#_Toc232848193)

[5.1.3 Display Exposure Position Flows 197](#_Toc232848194)

[5.1.4 Description on the Template for Import Raw Exposures 198](#_Toc232848195)

[5.1.5 Sample Data for Import Raw Exposures 201](#_Toc232848196)

[5.2 Job Scheduling 204](#_Toc232848197)

[5.2.1 Generate Limit Utilizations 204](#_Toc232848198)

[5.2.2 Send Correspondence 206](#_Toc232848199)

[5.2.3 Generate Payment Request 207](#_Toc232848200)

[5.2.4 Post Flows to General Ledger 210](#_Toc232848201)

[5.2.4.1 Template - Fix, Pay and Post Flows 210](#_Toc232848202)

[5.2.4.2 Template - Process Business Transactions 212](#_Toc232848203)

[5.2.5 Calculate Fair Value of Transaction 214](#_Toc232848204)

[5.2.6 Key Date Valuation 216](#_Toc232848205)

[5.2.7 Post Realized Profit and Loss 218](#_Toc232848206)

[5.2.8 Calculate Market Risk Key Figures 219](#_Toc232848207)

[5.3 Output Management 221](#_Toc232848208)

[5.3.1 Output Parameter Determination 221](#_Toc232848209)

[5.3.2 Manage Output Items 224](#_Toc232848210)

[5.3.3 Maintain Print Queues 225](#_Toc232848211)

[5.3.4 Display Email Transmissions 226](#_Toc232848212)

[5.3.5 Maintain Email Template 227](#_Toc232848213)

[5.3.6 Maintain Form Templates 229](#_Toc232848214)

[5.4 Accounting 230](#_Toc232848215)

[5.4.1 Reverse Valuation 230](#_Toc232848216)

[5.4.2 Account Assignment Reference Transfer 232](#_Toc232848217)

[5.4.3 Reverse Account Assignment Reference Transfer 233](#_Toc232848218)

[5.5 Interest Rate Adjustment 235](#_Toc232848219)

[5.5.1 Change Adjustment (Interest Rates/Prices) 235](#_Toc232848220)

[5.5.2 Display Adjustment (Interest Rates/Prices) 236](#_Toc232848221)

[5.5.3 Reverse Automatic Adjustments (Interest Rates/Prices) 236](#_Toc232848222)

[5.5.4 Reverse Adjustment (Interest Rates/Prices) 237](#_Toc232848223)

[5.6 Market Risk Analyzer 238](#_Toc232848224)

[5.6.1 Manage Market Data Shift 238](#_Toc232848225)

[5.6.2 Defining Report Layout for Calculate Market Risk Key Figures 239](#_Toc232848226)

[5.6.3 Defining Report Layout for Calculate Market Risk Key Figures 242](#_Toc232848227)

[5.6.4 Manage Market Risk Key Figure Sets 244](#_Toc232848228)

[5.7 Credit Risk Analyzer 247](#_Toc232848229)

[5.7.1 Display Limit Overview 247](#_Toc232848230)

[5.8 Change Counterparty 248](#_Toc232848231)

[5.8.1 Change Counterparty of Financial Transactions 248](#_Toc232848232)

[5.8.2 Display Financial Transactions With Changed Counterparty 249](#_Toc232848233)

[5.9 Analytical Apps 250](#_Toc232848234)

[5.9.1 Define Display Order 250](#_Toc232848235)

[5.9.2 Analytical Apps 251](#_Toc232848236)

[5.10 FX Netting 251](#_Toc232848237)

[5.10.1 Create a FX Forward Transaction 252](#_Toc232848238)

[5.10.2 Manual Settlement 252](#_Toc232848239)

[5.10.3 Roll Over the FX Transaction 252](#_Toc232848240)

[5.10.4 Edit Payment Details of the FX Transactions 254](#_Toc232848241)

[5.10.5 Propose Netting List 256](#_Toc232848242)

[5.10.6 Display Netting 257](#_Toc232848243)

[5.10.7 Generate Payment Request for the Netted Transactions 257](#_Toc232848244)

[5.10.8 Process Payment Request 259](#_Toc232848245)

[5.10.9 Send Payment Medium File 262](#_Toc232848246)

[5.11 Copy Existing Transaction 262](#_Toc232848247)

[5.11.1 Copy FX Spot/Forward 263](#_Toc232848248)

[5.11.2 Copy Nondeliverable Forward 264](#_Toc232848249)

[5.12 Termination of Foreign Exchange Transaction 265](#_Toc232848250)

[5.12.1 Create, Submit and Release Termination Request for a Forward 265](#_Toc232848251)

[5.12.2 Terminate Foreign Exchange Forward 267](#_Toc232848252)

[5.12.3 Set Termination Settlement Status for Foreign Exchange Forward 268](#_Toc232848253)

[5.12.4 Post Flows for Termination 269](#_Toc232848254)

[5.12.5 Create, Submit and Release Termination Request for Option 270](#_Toc232848255)

[5.12.6 Terminate Foreign Exchange Option 272](#_Toc232848256)

[5.12.7 Set Termination Settlement Status for Foreign Exchange Option 273](#_Toc232848257)

[5.12.8 Post Flows for Termination 274](#_Toc232848258)

[5.13 Simulated Valuation 275](#_Toc232848259)

[5.13.1 Run Simulated Valuation 275](#_Toc232848260)

[5.13.2 Delete Simulated Valuation 277](#_Toc232848261)

[5.14 Notification for Managing Financial Transactions 278](#_Toc232848262)

[5.14.1 Create Teams and Responsibilities 279](#_Toc232848263)

[5.14.2 Enable Situation Types 281](#_Toc232848264)

[5.14.3 Create a FX Option Contract 282](#_Toc232848265)

[5.14.4 Trigger and Schedule the Notifications 283](#_Toc232848266)

[5.14.5 User Setting for Notification 284](#_Toc232848267)

[5.14.6 Check the Notification in Fiori Launchpad and E-Mail 284](#_Toc232848268)

## Purpose

Overview

The foreign currency risk management enables you to gain an overview of the foreign exchange risk that your company is exposed to, as well as the hedging instruments that you used to mitigate that risk. You can review your balance sheet FX risk and determine your net open exposures (FX Risk).

Using the financial transactions provided for this process you can mitigate the FX risks.

The functionality helps you to automate labor-intensive processes, such as confirmation of financial transactions and accounting postings, giving you more time to focus on value-added activities. You can manage operational and accounting. The process includes the products FX spot transactions, FX Forward Transactions, swaps, nondeliverable forwards and FX options.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP S/4HANA system | Accessible via Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | Description | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- | --- |
| Treasury Specialist - Back Office |  | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Treasury Specialist - Front Office |  | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |
| Treasury Specialist - Middle Office |  | SAP_BR_TREASURY_SPECIALIST_MOE | Treasury Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE |  |
| Treasury Accountant |  | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |
| Treasury Risk Manager |  | SAP_BR_TREASURY_RISK_MANAGER | Treasury Analytics | SAP_BR_TREASURY_RISK_MANAGER |  |
| Cash Manager |  | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Administrator |  | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Master Data Specialist - Business Partner Data |  | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Currency | AED, USD and BRL |  |  |
| Business Partner | 33537001 and 33537002 |  |  |
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
| 1XN - Market Rates Management – Manually via Upload | Must be run before this test script, Market data must be created. |
| J60 - Accounts Payable | Execute the Prerequisites > Preliminary Steps > Define Payment Medium Format Variants topic to define the Payment Medium Format (PMF) variants. |

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

In this step, you maintain the general data for Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen displays. |  |
| 3 | Enter Data on Initial Screen | Choose Organization. | The Create Organization: screen displays. |  |
| 4 | Enter address data | Enter the following data and choose Save:Business Partner: for example, 33537001Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, <Bank 1 - SAMPLE BANK>Salutation: for example, <Bank 1>Search Term 1/2: for example, <Bank 1>Street/House number: for example,Postal Code/City: for example,Ctry/Reg.: select AELanguage: select ENE-Mail: for example, <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, <Dec 31 of the year 9999>Note Stay in the screen for subsequent steps. | The Business partner is created successfully.The Display Organization: 33537001 screen displays. |  |
| 5 | Switch to change mode | Choose Switch Between Display and Change.Make the following entries:Change in BP role: select TR0151 Counterparty | Additional tabs for counterparty (such as Legal Data or Rating) display.The Change Organization33537001, new role Counterparty screen displays. |  |
| 6 | Enter Legal data | Choose … > Legal Data.Note The … is the navigation menu.Make the following entries and choose Save:Country/Region: <select AE>Note Stay in the screen for subsequent steps. | The Legal data is entered and saved.The Change Organization: 33537001, new role Counterparty screen displays. |  |
| 7 | Enter Payment Transaction data | Choose ... > Payment Transactions.Make the following entries and choose Save:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, 18121976Bank acct: for example, <Bank account>IBAN: Choose the IBAN button and choose Continue in the IBAN view.Row 2:ID: for example, USD1C/R: for example, AEBank Key: for example, 18121976Bank acct: for example, <Bank account>IBAN: Choose the IBAN button and choose Continue in the IBAN dialog box.Note If an Information dialog box displays when you choose IBAN, choose Continue. | The Payment transaction data is entered and the Business Partner is saved. |  |

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
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen displays. |  |
| 3 | Switch to change mode | Choose Open BP, in the popup dialog box, enter following data:Business Partner:33537001Choose Enter and then choose Switch Between Display and Change.Enter the following data:Change in BP Role: <select TR0151 Counterparty> | The Change Organization: 3310, role Counterparty screen displays. |  |
| 4 | Enter SI: Payment Details data | Choose Company code.Enter the following data:Company Code: for example, 3310Choose Enter.Choose SI: Payment Details.Make the following entries:Row 1:Currency: for example, AEDPay.Det.ID: for example, AEDIHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: <Blank>Partner Bank: <Blank>Payment Request: <Deselect>Payment Methods: <Blank>Row 2:Currency: for example, AEDPay.Det.ID: for example, AEDOHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, 33537001Partner Bank: for example, AED1Payment Request: <select>Payment Methods: for example, TRow 3:Currency: for example, USDPay.Det.ID: for example, USDIHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/ee: <Blank>Partner Bank: <Blank>Payment Request: <Deselect>Payment Methods: <Blank>Row 4:Currency: for example, USDPay.Det.ID: for example, USDOHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/ee: for example, 33537001Partner Bank: for example, USD1Payment Request: <select>Payment Methods: for example, FNote Stay in this screen for subsequent steps.Note If a warning window with the following message displays, choose No.The business partner is proposed as payer/payee (see long text).Display this message for this business partner again? | The SI: Payment Details data is entered. |  |
| 5 | Assign Payment details | From the last screen of previous step:For AED, select the checkbox for AEDAEDI and choose Assign.On the Counterparty Change: Payment Details Assignment dialog box, choose Select All Incoming.Now AEDI displays under PmntID-Inc.Choose Continue.Select the checkbox for AEDAEDO and choose Assign.On the Counterparty Change: Payment Details Assignment dialog box, choose Select All Outgoing.Now AEDO displays under P-ID Outg.Choose Continue.Do the same for USD:USD I: PmntID-IncUSD O: P-ID Outg.On the Change Organization: 33537001, role Counterparty screen, choose Save. | Payment details and the assignments are saved. |  |

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
| 1 | Log on | Log onto the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen displays. |  |
| 3 | Switch to change mode | Choose Open BP, in the popup dialog box, enter following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change.Enter the following data:Change in BP Role: <select TR0151 Counterparty> | The Change Organization: 33537001, role Counterparty screen displays. |  |
| 4 | Enter SI: Authorizations data | Choose Company Code.Choose SI: Authorizations.Enter the following data and choose Save:Foreign Exchange: Auth.: <select>Derivatives: Auth.: <select>Note You can also give authorization to a specific product type and transaction type by expending the folders. For testing context, we give all authorizations to all kinds of product types and transaction types. | The authorizations data is saved. |  |

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen displays. |  |
| 3 | Switch to change mode | Enter the following data and choose Enter.Business Partner:33537001Choose Switch Between Display and Change.Enter the following data:Change in BP Role: TR0151 Counterparty | The Change Organization: 33537001 , role Counterparty screen displays. |  |
| 4 | Enter Reporting Data in Company Code | Choose Company Code.Choose Reporting Data in Company Code.Enter following data and choose Save.Comp. Rel.: 3 OtherNote If you cannot find Reporting Data in Company Code, then choose ... (the navigation menu) and choose it from the dropdown menu.Note Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itThey are used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

#### Correspondence

Purpose

SAP TRM provides the standard correspondence functionality. With this correspondence functionality, whenever a TRM transaction is saved, SAP either sends an email to the Business Partner, or automatically prints a form.

To use this correspondence functionality, the following data must be assigned to the Business Partner:

- Business Partner Profile
- Business Partner group
- Swift/BIC code

##### Maintain Profile and BP Group Assignments to External Recipient

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Business partner profiles and Business partner groups controls the correspondence activities in SAP Treasury and Risk Management.

SAP predefines the following business partner profiles:

- PR_EMAIL
- PR_PRINT

You can assign these predefined Business Partner profiles to your Business Partner. For example, if the communication with your Business Partner is via e-mail, you can assign PR_EMAIL to your Business Partner; If the communication is via Print, then you can assign PR_PRINT.

SAP has predefined following Business Partner groups:

- BPG_DEFAULT

You can assign this Business partner group to your Business Partner. You can also use SSCUIs Define Business Partner Group and Assign Attributes for Business Partner Groups to add your own Business partner group and assign appropriate attributes according to your specific requirement. Different business partner profiles and BP groups could be assigned to the same business partner.

This step describes how to assign Business partner profiles and BP groups to an external business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign Profile and BP Group - External Recipients (FTR_EXT_ASSIGN). | The Assignment of Profiles and BP Groups to External Recipients: screen displays. |  |
| 3 | Enter Business partner data on the screen | On the left side of the screen, choose Insert Row.Enter the following data and choose Enter:BusPartner: for example, 33537001CoCd: for example, 3310Recpt/Send Type: for example, COUNTERPARTYSelect the checkbox. | The Business Partner information is entered. |  |
| 4 | Assign Business profile and BP group to the Business Partner | On the top-right side of the screen,choose Expand Node.Expand BP:XXXXXXXX/CoCd:YYYY/Rec/SendType: COUNTERPARTY > Foreign Exchange > FX Transaction > 60A Foreign Exchange > 101 Spot Transaction > 20 Contract.On the bottom-right side of the screen, choose Insert Row and enter the following data:Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTChoose Insert Row again. Add another entry and choose Save:Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTNote Normally, you only assign one profile to a Product type/Transaction type/Activity Category. | Business partner profiles and BP groups are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat Prior Step | Select the item 33537001 in the left side view, and choose Modify Row.Repeat the above step for the values in the data table below. | For all the listed Product Types/Transaction Types/ Activity Categories, BP profiles and BP groups are assigned. |  |

Table 2: Business Partner Assignment Table

| Product Type | Transaction Type | Act. Category |
| --- | --- | --- |
| 60A | 101 | 20 |
| 60A | 102 | 20 |
| 60A | 103 | 20 |
| 60A | 104 | 20 |
| 60A | 105 | 20 |
| 60A | 107 | 20 |
| 60B | 103 | 20 |
| 60B | 103 | 55 |
| 60B | 104 | 20 |
| 60B | 104 | 55 |
| 60B | 105 | 20 |
| 60B | 105 | 55 |
| 60B | 110 | 20 |
| 60B | 110 | 55 |
| 76A | 100 | 20 |
| 76A | 200 | 20 |

##### Maintain Profile and BP Group Assignments to Internal Recipient

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The internal recipient ID is predefined by SAP, and it can be linked to SAP User IDs. When linked to a SAP user ID, whenever an internal correspondence object is generated, SAP Treasury and Risk Management attempts to send correspondence information to the address of the SAP User ID. Depending on the different profiles (PR_EMAIL /PR_PRINT), e-mail can be sent to the user's e-mail address, or a form is printed.

This step describes how to assign Business partner profiles and BP groups to an internal business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign Profile and BP Group - Internal Recipients (FTR_INT_ASSIGN). | The Assignment of Profiles and BP Groups to Internal Recipients screen displays. |  |
| 3 | Enter Business partner data on the screen | On the left side of the screen, choose Insert Row.Make the following entries and choose Enter.IntRec: for example, INT.RECPCoCd: for example, 3310Recpt/Send Type: for example, INTERNALCheckbox: Selected | The Business Partner information is entered. |  |
| 4 | Assign Business profile and BP group to the Business Partner | On the top-right side of the screen, expand the business partner: INT.RECP/CoCd XXXX > Rec/SendType: INTERNAL > Foreign Exchange > 60A Foreign Exchange > 101 Spot Transaction > 20 Contract.On the bottom-right side of the screen, choose Insert Row:Make the following entries and choose Save:Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTUser Name: <select a User ID>.Choose Insert Row again.Add another entry and choose Save:Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTUser Name: Select a <User ID>.Note The user ID is a backend user ID. | The business partner profile, BP group, and user ID are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat Prior Step | Select the item INT.RECP in the left side view, and choose Modify Row.Repeat the above step using data from the table below. | The BP profiles, BP groups, and user IDs are assigned to all the listed Product Types/Transaction Types/ Activity Categories. |  |

Table 3: Business Partner Assignment Table

| Product Type | Transaction Type | Act. Category |
| --- | --- | --- |
| 60A | 101 | 20 |
| 60A | 102 | 20 |
| 60A | 103 | 20 |
| 60A | 104 | 20 |
| 60A | 105 | 20 |
| 60A | 107 | 20 |
| 60B | 103 | 20 |
| 60B | 103 | 55 |
| 60B | 104 | 20 |
| 60B | 104 | 55 |
| 60B | 105 | 20 |
| 60B | 105 | 55 |
| 60B | 110 | 20 |
| 60B | 110 | 55 |
| 76A | 100 | 20 |
| 76A | 200 | 20 |

#### Maintaining Credit Limit

Purpose

A series of limit types have been created in system. You can maintain credit limits based on specified limit type according to business. In this test script, limit type Y01 and Y07 are maintained.

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

In this activity, you define traders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Define Traders (S_ALR_87009302). | The Determine Work Area: Entry dialog displays. |  |
| 3 | Enter Work Area | Enter the following data and choose ContinueCompany Code: for example, 3310 | The Change View "Treasury: Traders": Overview screen displays. |  |
| 4 | New Entries | Choose New Entries. |  |  |
| 5 | Create a New Record | Enter the following data and choose Save:Trader: for example, TRADER02 | The data is saved. |  |

##### Define User Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you map users with traders. This provides a default trader when creating a new transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Define User Data (S_ALR_87007933). | The Change View "Treasury: User master data supplements": Overview screen displays |  |
| 3 | Create a New Record | Choose New Entries. |  |  |
| 4 | Enter Data | Make the following entries and choose Save:User Name: for example, <Your user name>Trader: for example, TRADER02 | The data is saved. |  |

##### Maintain Trader Authorizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define authorization for traders.

Prerequisites

A trader must be defined before this step. For more information, see the Define Traders step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Trader Authorizations (TBT1). | The Create/Change Trans. Authorization for Trader: Init. Screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose EnterTrader: for example, TRADER02Company Code: for example, 3310 | The Create/Change Transaction Authorization for Traders screen displays. |  |
| 4 | Enter Authorization and Save | Select or deselect the Authorization column and choose Save.Note Authorize TRADER02 for the Foreign Exchange and Derivatives transactions. | The data is saved. The system displays a message Transaction authorizations for trader TRADER02 are being saved. |  |

#### Exposure Management and Hedge Management

##### Define Time Pattern

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define time pattern used for target quotas within a hedging area.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Define Time Pattern (TOE_TIME_PATTERN). | The Display Time Pattern screen displays. |  |
| 3 | Create a New Hedging Area | Make the following entries and choose Create:Time Pattern: for example, M12 | The Create Time Pattern dialog box displays. |  |
| 4 | Enter Details for the New Hedging Area | Make the following entries and choose Save:Time Pattern: for example, M12, Time Pattern - Calendar Month 12Time Pattern: for example, click Calendar-RelatedNumber of Periods: for example, 12Period Length: for example, MonthAbosolute Time Pattern: <unselect> | The data is saved. |  |

##### Define Hedging Area

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a hedging area to calculate and display the net open exposures in Hedge Management Cockpit (TOENE).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Hedging Area (TOE_HEDGING_AREA). | The Display Hedging Area screen displays. |  |
| 3 | Create a New Hedging Area | Make the following entries and choose Create:Hedging Area: for example, AE0001 | The Create Hedging Area dialog box displays. |  |
| 4 | Enter Details for the New Hedging Area | Make the following entries and choose Create:Description: for example, Hedging Area FXAuthorization Group: for example, HAG01Valid from: for example, <January 1st of current year> | The data is saved. The Change Hedging Area screen displays. |  |
| 5 | Define Main Data for Hedging Area | On the Main Data tab, make the following entries:Activate SAP Trading Platform Integ.: for example, <Select the checkbox>Risk Free Currency: for example, Local CurrencyNote If you want to enable extraction of cross-currency exposures, please choose Currency Defined by the Source. By doing so, the risk-free currency is derived from the currency pair of the exposure item. If the source is Exposure Management, the risk-free currency is the target currency. If the source is Cash Management, the risk-free currency is the company code currency.Choose Calendar-Related in section Reporting Time Pattern.Number of Period: for example, 12Period Length: for example, MonthTarget Quota: for example, select Target QuotaChoose Add Target Quota TypeTQ Type: for example, YLQTime Pattern ID: for example, M12 | The data is saved. |  |
| 6 | General Settings | Choose the General Settings tab. |  |  |
| 7 | Define General Settings for Hedging Area | Make the following entries:Company Code: for example,3310Differentiation Criteria: for example, select Currency/Currency Group and Company CodeRelevant for Target Quota: for example, select for Currency/Currency GroupChoose Add Hedging Classification.Add Y0 | The data is saved. |  |
| 8 | Currency | Choose the Currencies tab. |  |  |
| 9 | Currency | Choose Add Currency. |  |  |
| 10 | Define Currencies | In the Currency column, enter the risk currency other than local currency, for example, USD.In the Currency Group column, enter America.Repeat the step to add BRL and enter America in the Currency Group column. | The data is saved. |  |
| 11 | Exposure Filters | Choose the Filters for Exposure tab. |  |  |
| 12 | Create Filters for Exposures | Choose Create Filter. | The New Filter for Exposures dialog box displays. |  |
| 13 | Define Data for Filters for Exposures | Make the following entries and choose Create Filter:Filter: for example, EXP_FILTERFilter Description: for example, Exposure FilterSource: E_EM2Note You can also choose Source E_1EXP, which is One Exposure and/or Source E_FXEM, which is Foreign Exchange Exposure Management. | One record is created in the Filter List for Exposures. |  |
| 14 | Define Other Filter-Specific Selections | Scroll down to the Other Filter-Specific Selections section.Make the following entries:Exposure Position Type: YFXNote If you chose E_FXEM as data source in step 13, please scroll down to the Other Selections section and enter SFX in field FX Exposure Type.You can define additional FX Exposure Type via configuration step Define FX Exposure Types.Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | The data is saved. |  |
| 15 | Hedge Filters | Choose the Filters for Hedges tab. |  |  |
| 16 | Create Filters for Hedges | Choose Create Filter. | The New Filter for Hedges dialog box displays. |  |
| 17 | Define Data for Filters for Hedges | Make the following entries and choose Create Filter:Filter: for example, HDG_FILTERFilter Description: for example, Hedge FilterData Source: H_TM | One record is created in the Filter List for Hedges. |  |
| 18 | Define Other Filter-Specific Selections | Scroll down to the Other Filter-Specific Selections section. Make the following entries:Product type: 60A and 76A |  |  |
| 19 | Target Quotas | Choose Target Quotas. |  |  |
| 20 | Define Target Quota | Insert Quota and enter following data in the Enter Target Quota screen and choose Continue:Net/Gross : for example, NetCurrency Group: for example, AmericaTarget Quota: for example, <80 for Time Period 1,2,3,4,5,6 and 70 for Time Period 7,8,9,10,11,12> | Target Quotas is created. |  |
| 21 | FX Hedge Request | Choose the FX Hedge Request tab. |  |  |
| 22 | Define automation hedge request settings | Make the following entries:Target Status for Automation: for example, CreatedValue Date Definition: for example, <last Day of Period>Scroll down to the Hedge Request Settings section. Insert the following entries:Company: for example, 3310Risk Currency from Source: for example, USDNote If you chose Currency Defined by the Source in step 5, please also maintain Target Currency, which should be same as the target currency from the exposure item.Default Instrument Category: for example, FXFWHedging Classification: for example, Y0Minimum Amount: for example, 10000Repeat to insert another entry for currency BRL. | Automation of hedge request is set. |  |
| 23 | Save Data | Choose Save. | The new Hedging Area Version is saved. |  |

##### Define Key Figures for Balance Sheet FX Risk

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you define a set of key figures to be displayed on the Review Balance Sheet FX Risk screen.

|  |
| --- |
| Note The following procedure illustrates key figure creation. Define key figure groups and key figures per your company requirements. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Define Key Figures - Balance Sheet FX Risk (FXM_KF_DEF). | The Display View "Maintain Key Figure Groups": Overview screen displays. |  |
| 3 | New Entries | Choose New Entries. |  |  |
| 4 | Maintain Key Figure Groups | Make the following two entries and choose Save:Key Figure Group: for example, EXP_GRP1Key Figure Group Description: for example, All Accounts PayablesExposure/Hedge: for example, ExposureKey Figure Group: for example, HED_GRP1Key Figure Group Description: for example, All FX transactionsExposure/Hedge: for example, Hedge | The data is saved. |  |
| 5 | Maintain Key Figures | In the Dialog Structure pane, double-click Maintain Key Figures. |  |  |
| 6 | Maintain Key Figures | Choose New Entries. |  |  |
| 7 | Maintain Key Figures | Make the following entries and choose Save:Key Figure: for example, EG1K1Key Figure Description: for example, All Accounts PayablesKey Figure Group: for example, EXP_GRP1Data Source: for example, One ExposureKey Figure: for example, HG1K1Key Figure Description: for example, All FX transactionsKey Figure Group: for example, HED_GRP1Data Source: for example, Financial Transactions | The data is saved. |  |
| 8 | Maintain Selections | Select a key figure and choose Maintain Selections.Note You may need to choose the Back button if the Maintain Selections button does not display. |  |  |
| 9 | Maintain Selections | Select Key Figure: EG1K1 and make the following entries and press Enter:Certainty Level: for example, PAY_NSelect Key Figure: HG1K1 and make the following entries and press Enter:Product Type: for example, 60A to: for example 60B |  |  |
| 10 | Save | Choose Back.Choose Save. | The data is saved. |  |

##### Define Request Parameters for Balance Sheet FX Risk

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define a set of request parameters to filter your generation of hedge request.

|  |
| --- |
| Note The following procedure illustrates request parameters creation. Define request parameter group and request parameters according to your company requirements. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define Key Figures - Balance Sheet FX Risk (FXM_KF_DEF). | The Change View "Maintain Key Figure Groups": Overview screen is displayed. |  |
| 3 | Maintain Request Parameter Groups | On the Dialog Structure panel, double lick on Maintain Hedge Request Parameter Groups to open the folder. | The Maintain Hedge Request Parameter Groups folder is opened. |  |
| 4 | New Entries | Choose New Entries. |  |  |
| 5 | Maintain Request Parameter Groups | Maintain the following data and choose Save:B/S Hedge Request Parameter Group: for example, RP_GRP1Parameter Group Description: for example, Default Parameter Group for 3310Default: for example, Yes | The data is saved. |  |
| 6 | Maintain Request Parameters | In the Dialog Structure pane, double-click on Maintain Hedge Request Parameters. |  |  |
| 7 | Maintain Request Parameters | Choose New Entries. |  |  |
| 8 | Maintain Request Parameters | Maintain the following data and choose Save:B/S Hedge Request Parameter: for example, RP1Parameter Description: for example, USDB/S Hedge Request Parameter Group: for example, RP_GRP1B/S Hedge Request Parameter: for example, RP2Parameter Description: for example, BRLB/S Hedge Request Parameter Group: for example,RP_GRP1 | The data is saved. |  |
| 9 | Maintain Selections | Select a request parameter and choose Maintain Selections.Note You may need to choose Back if the Maintain Selections button does not display. |  |  |
| 10 | Maintain Selections | Select B/S Hedge Request Parameter: RP1 and make the following entries and choose Back:Company Code: for example, 3310Currency: for example, USDTime Period: for example, <select>Value Date Definition: for example, First Day of PeriodInstrument Category: for example, FX ForwardTarget Status: for example, CreatedSelect B/S Hedge Request Parameter: RP2, maintain the following data and choose Back:Company Code: for example, 3310Currency: for example, BRLTime Period: for example, <select>Value Date Definition: for example, First Day of PeriodInstrument Category: for example, FX ForwardTarget Status: for example, Created |  |  |
| 11 |  | Choose Back.Choose Save. | The data is saved. |  |
| 12 | Create Other Hedge Request Parameter Groups | Repeat step 3 to step 11 to add second B/S Hedge Request Parameter Group RP_GRP2 with B/S Hedge Request Parameter RP3 and RP4.Note The Instrument Category of RP3 and RP4 is FX Option. |  |  |

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

Table 4: Define General Fixing Reference and EMTA Fixing Reference

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Define Fixing Reference (FTR_FIX_DEF). | The Change View "Define Fixing References": Overview screen is displayed. |  |
| 3 | Create Fixing Reference IDs | Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Create Fixing Reference IDs | Make the entries from the Fixing Reference ID table below (each on a separate row) and choose Save. | On the New Entries: Overview of Added Entries screen, the system displays the message Data was saved. |  |

Table 5: Fixing Reference ID Table

| Fixing Reference ID | Fixing Reference Description | Leading Currency | Following Currency | Fixing Reference Category | Source | Location | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ECB37 AED / USD | ECB37 AED / USD | AED | USD | 1 General Fixing Reference | AED 1 | DECB | 14:15 |
| WM/REUTERS AED / USD 4 PM | WM/REUTERS AED / USD 4 PM | AED | USD | 1 General Fixing Reference | AED 2 | GBLO | 16:00 |
| KFTC18 ( KRW 02) | KFTC18 ( KRW 02) | USD | KRW | 2 EMTA Fixing Reference | Leave blank | Leave blank | Leave blank |
| PTAX ( BRL 09) | BRL PTAX ( BRL 09) | USD | BRL | 2 EMTA Fixing Reference | Leave blank | Leave blank | Leave blank |

Table 6: Define Compound Fixing Reference

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

For Swift format MT305, there is a mandatory field called 31G: Expiry Details. This field specifies the date, time and location at which the option expires. In this activity, you assign times to locations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Define Values for Expiry Time - OTC Option (FTR_EXPIRY_TIME_DEF). | The Change View "Assign Times to Locations": Overview screen is displayed. |  |
| 3 | Assign Expiry Times to Locations | Choose New Entries. | The New Entries: Overview of Added Entries screen displays. |  |
| 4 | Assign Expiry Times to Locations | Make the following entry and choose Save:Location: for example, DEFRTime: for example, 15:00Location: for example, DECBTime: for example, 16:00 | On the New Entries: Overview of Added Entries screen, the system displays the message Data was saved. |  |

## Overview Table

The scope item Foreign Currency Risk Management(1X1) consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Foreign Currency Risk Management and Accounting - Without Options

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [(1XN) Market Rates Management – Manually via Upload](#unique_27) [page ] 50 | - | - | The market data is prepared |
| [(1S4) Automatic Market Rates Management](#unique_28) [page ] 50 |  |  | The market data is prepared |
| [Generate Limit Utilizations](#unique_29) [page ] 51 | Treasury Specialist - Middle Office | End-of-Day Processing (KLNACHT) | The process completes successfully |
| [Analyze Cash Position](#unique_30) [page ] 52 | Cash Manager | - | Follow the two cash operations test scripts. |
| [Analyze Liquidity Forecast](#unique_31) [page ] 52 | Cash Manager | - | Follow the two cash operations test scripts. |
| [Review Balance Sheet FX Risk](#unique_32) [page ] 52 | Treasury Specialist - Middle Office | Review Balance Sheet FX Risk (F1588) | Review Balance Sheet FX Risk screen displays with correct data in it. |
| [Take Snapshot for Balance Sheet FX Risk](#unique_33) [page ] 53 | Treasury Specialist - Middle Office | Generate Hedge Request - Balance Sheet FX Risk (FXM_REQUEST) | A snapshot for balance sheet FX Risk is taken. |
| [Check and Process Snapshot Item](#unique_34) [page ] 54 | Treasury Specialist - Middle Office | Process Snapshots (F4763) | Your changes are saved. |
| [Release Snapshot](#unique_35) [page ] 56 | Treasury Specialist - Middle Office | Process Snapshots (F4763) | The snapshot is released. |
| [Collect Exposure Data](#unique_36) [page ] 123 | - | - | Summary of the raw exposures.This step is outside of SAP system. |
| [Create Raw Exposure](#unique_37) [page ] 58 | Treasury Specialist - Middle Office | Process Raw Exposure (FTREX1) Import Raw Exposures - Spreadsheet (FTREX_EXCEL_UPLOAD) | The exposures are created . |
| [Take Snapshot for Cash Flow Exposure](#unique_38) [page ] 62 | Treasury Specialist - Middle Office | Take Snapshot (TOESNAP) | A snapshot is taken for the cash flow exposure. |
| [Review Cash Flow Net Exposure](#unique_39) [page ] 64 | Treasury Specialist - Middle Office | Hedge Management Cockpit (TOENE) | The Hedge Management Cockpit displays with the exposure data in it. |
| [Generate Hedge Request](#unique_40) [page ] 65 | Treasury Specialist - Middle Office | Hedge Management Cockpit (TOENE) or Generate Hedge Request - Balance Sheet FX Risk (FXM_REQUEST) | A trade request via balance sheet exposure hedge request is created. |
| [Check and Process Hedge Request](#unique_41) [page ] 67 | Treasury Specialist - Middle Office | Process Hedge Requests – Balance Sheet FX Risk | Your changes are saved. |
| [Create FX Spot Contract](#unique_42) [page ] 178 | Treasury Specialist - Middle Office | Process Hedge Requests-Balance Sheet FX Risk (F4764) | The balance sheet exposure hedge request is released successfully. |
| [Generate Hedge Request](#unique_43) [page ] 69 | Treasury Specialist - Middle Office | Hedge Management Cockpit (TOENE) | Hedge Request is generated. |
| [Release Hedge Request](#unique_44) [page ] 71 | Treasury Specialist - Middle Office | Process Hedge Requests (TOEHREQO) | Hedge Request is synchronized. |
| [Check Trade Request Status](#unique_45) [page ] 74 | Treasury Specialist - Middle Office | Process Trade Requests (TPITRO) |  |
| [Analyze Exposure and Agree on Hedging Actions](#unique_46) [page ] 65 | - | - | Agreement on the hedging actions.This step is outside of SAP system. |
| [Check Limit Utilization Report](#unique_47) [page ] 75 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | The system displays an overview of the limit utilizations in accordance with your selection criteria. |
| [Create FX Spot/Forward](#unique_48) [page ] 76 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) | Transaction is saved and a transaction number is generated. |
| [Create FX Swap](#unique_49) [page ] 78 | Treasury Specialist - Front Office | Create FX Swap (TX10) | Transaction is saved and a transaction number is generated. |
| [Create Non-Deliverable Forward](#unique_50) [page ] 79 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) | Transaction is saved and a transaction number is generated. |
| [(BFB) Basic Cash Operations](#unique_51) [page ] 80 | Cash Manager | - | Follow the specified test script |
| [(J78) Advanced Cash Operations](#unique_52) [page ] 81 | Cash Manager | - | Follow the specified test script |
| [Set Settlement Status (Manual)](#unique_53) [page ] 82 | Treasury Specialist - Back Office | Manage Financial Transactions (F6157) | The transaction has been changed to Contract settlement status. |
| [Send Confirmation Email / Print](#unique_54) [page ] 84 | Treasury Specialist - Back Office | - | This step is outside of SAP system |
| [Check Correspondence Status](#unique_55) [page ] 84 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The form of the correspondence object displays |
| [Receive Incoming Confirmation](#unique_56) [page ] 157 | Treasury Specialist - Back Office | - | This step is outside of SAP system |
| [Find Deal and Match Deal Details](#unique_57) [page ] 86 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | Relevant outgoing COUNTERPARTY correspondence object(s) of the transactions are at status completed.Relevant INTERNAL outgoing correspondence object(s) have status Delivered. |
| [Set Settlement Status](#unique_58) [page ] 102 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The transaction has been updated to Activity 2 Contract Settlement. |
| [Calculate or Maintain Fair Value of Transaction](#unique_59) [page ] 89 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA) | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays, you can see the NPV, risk-free NPV, CVA, DVA of each transaction on the screen. |
| [Perform Key Date Valuation](#unique_60) [page ] 92 | Treasury Accountant | Run Valuation (TPM1) | The screen Valuation Log displays, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages.The accounting document has been created in local GAAP (valuation area AE0). |
| [Fix Rate for NDF](#unique_61) [page ] 94 | Treasury Specialist - Back Office | Fix FX Rates (TXV5) | The data is saved without error |
| [Set Settlement Status (Manual)](#unique_53) [page ] 82 | Treasury Specialist - Back Office | Manage Financial Transactions (F6157) | The transaction has been changed to Contract settlement status. |
| [Send Confirmation Email / Print](#unique_62) [page ] 98 | Treasury Specialist - Back Office | - | This step is outside of SAP system |
| [Check Correspondence Status](#unique_55) [page ] 84 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The form of the correspondence object displays |
| [Receive Incoming Confirmation](#unique_56) [page ] 157 | Treasury Specialist - Back Office | - | This step is outside of SAP system |
| [Find Deal and Match Deal Details](#unique_57) [page ] 86 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | Relevant outgoing COUNTERPARTY correspondence object(s) of the transactions are at status completed.Relevant INTERNAL outgoing correspondence object(s) have status Delivered. |
| [Set Settlement Status](#unique_58) [page ] 102 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The transaction has been updated to Activity 2 Contract Settlement. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_63) [page ] 103 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_64) [page ] 106 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Screen Payment Log displays, payment request has been generated, make a note of the key number displayed on this screen. |
| [Process Payment Request](#unique_65) [page ] 108 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | The payment document has been created.the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Cash Operations - Standard (BFB). |
| [Bank-Initiated Payment](#unique_66) [page ] 111 | Treasury Specialist - Back Office | - | This step is outside of SAP system |
| [Post to General Ledger](#unique_67) [page ] 111 | Treasury Accountant | Fix, Pay and Post Flows (TBB1) Process Business Transactions (TPM10) | Screen Posting Log: Posted Business Transactions displays, accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |
| [Post Realized Profit and Loss](#unique_68) [page ] 114 | Treasury Accountant | Post Derived Business Transactions (TPM18) | New screen Posting Log: Posted Business Transactions displays, you can see the posting information for local GAAP (valuation area AE0),The accounting document has been created in local GAAP (valuation area AE0). |

Foreign Currency Risk Management and Accounting - With Options

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [(1XN) Market Rates Management – Manually via Upload](#unique_27) [page ] 50 | - | - | The market data is prepared |
| [(1S4) Automatic Market Rates Management](#unique_69) [page ] 116 |  |  |  |
| [Generate Limit Utilizations](#unique_70) [page ] 116 | Treasury Specialist - Middle Office | End-of-Day Processing (KLNACHT) | The process completes successfully |
| [Analyze Liquidity Forecast](#unique_31) [page ] 52 | Cash Manager | - | Follow the two cash operations test scripts |
| [Review Balance Sheet FX Risk](#unique_32) [page ] 52 | Treasury Specialist - Middle Office | Review Balance Sheet FX Risk (F1588) | Review Balance Sheet FX Risk screen displays with correct data in it |
| [Take Snapshot for Balance Sheet FX Risk](#unique_33) [page ] 53 | Treasury Specialist - Middle Office | Take Snapshot - Balance Sheet FX Risk (FXM_SNAP) | A trade request via balance sheet exposure hedge request is created. |
| [Check and Process Snapshot Item](#unique_34) [page ] 54 | Treasury Specialist - Middle Office | Process Snapshots (F4763) | The snapshot status is Released |
| [Release Snapshot](#unique_35) [page ] 56 | Treasury Specialist - Middle Office | Process Snapshots (F4763) | Your changes are saved. |
| [Collect Exposure Data](#unique_36) [page ] 123 | - | - | Summary of the raw exposuresThis step is outside of SAP system |
| [Create Raw Exposure](#unique_71) [page ] 123 | Treasury Specialist - Middle Office | Process Raw Exposure (FTREX1) Import Raw Exposures - Spreadsheet (FTREX_EXCEL_UPLOAD) | The exposures are created |
| [Take Snapshot for Cash Flow Exposure](#unique_38) [page ] 62 | Treasury Specialist - Middle Office | Take Snapshot (TOESNAP) | A snapshot is taken for the cash flow exposure. |
| [Review Cash Flow Net Exposure](#unique_39) [page ] 64 | Treasury Specialist - Middle Office | Hedge Management Cockpit (TOENE) | The Hedge Management Cockpit displays with the exposure data in it. |
| [Analyze Exposure and Agree on Hedging Actions](#unique_46) [page ] 65 | - | - | Agreement on the hedging actionsThis step is outside of SAP system |
| [Generate Hedge Request](#unique_72) [page ] 131 | Treasury Specialist - Middle Office | Generate Hedge Request - Balance Sheet FX Risk (FXM_REQUEST) | A trade request via balance sheet exposure hedge request is created. |
| [Check and Process Hedge Request](#unique_41) [page ] 67 | Treasury Specialist - Middle Office | Process Hedge Requests – Balance Sheet FX Risk | Your changes are saved. |
| [Release Hedge Request](#unique_73) [page ] 68 | Treasury Specialist - Middle Office | Process Hedge Requests-Balance Sheet FX Risk (F4764) | The balance sheet exposure hedge request is released successfully. |
| [Generate Hedge Request](#unique_74) [page ] 135 | Treasury Specialist - Middle Office | Hedge Management Cockpit (TOENE) | A hedge request is created. |
| [Release Hedge Request](#unique_75) [page ] 137 | Treasury Specialist - Middle Office | Process Hedge Requests (TOEHREQO) | The hedge request is released. |
| [Create Trade Request Manually](#unique_76) [page ] 138 | Treasury Specialist - Middle Office | Process Trade Requests (TPITRO) | A trade request is created manually. |
| [Check Trade Request Status](#unique_77) [page ] 140 | Treasury Specialist - Middle Office | Process Trade Requests (TPITRO) |  |
| [Check Limit Utilization Report](#unique_47) [page ] 75 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | The system displays an overview of the limit utilizations in accordance with your selection criteria. |
| [Create Plain Vanilla FX Option](#unique_78) [page ] 142 | Treasury Specialist - Front Office | Create OTC Option (TI71) | Transaction is saved and a transaction number is generated. |
| [Option 1: Create Two Options Separately and Create Option Reference](#unique_79) [page ] 144 | Treasury Specialist - Front Office | Create OTC Option (TI71) |  |
| [Option 2: Create Zero/Low Cost Collar FX Option in Single Step](#unique_80) [page ] 148 | Treasury Specialist - Front Office | Create Collar FX Option (TI4B) |  |
| [(BFB) Basic Cash Operations](#unique_51) [page ] 80 | Cash Manager | - | Follow the specified test script |
| [(J78) Advanced Cash Operations](#unique_52) [page ] 81 | Cash Manager | - | Follow the specified test script |
| [Set Settlement Status (Manual)](#unique_81) [page ] 152 | Treasury Specialist - Back Office | Manage Financial Transactions (F6157) | The transaction has been changed to Contract settlement status. |
| [Send Confirmation Email / Print](#unique_54) [page ] 84 | Treasury Specialist - Back Office | - | This step is outside of SAP system |
| [Check Correspondence Status](#unique_55) [page ] 84 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The form of the correspondence object displays |
| [Receive Incoming Confirmation](#unique_56) [page ] 157 | Treasury Specialist - Back Office | - | This step is outside of SAP system |
| [Find Deal and Match Deal Details](#unique_57) [page ] 86 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | Relevant outgoing COUNTERPARTY correspondence object(s) of the transactions are at status completed.Relevant INTERNAL outgoing correspondence object(s) have status Delivered. |
| [Set Settlement Status](#unique_58) [page ] 102 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The transaction has been updated to Activity 2 Contract Settlement. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_82) [page ] 160 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘Auto. Payment Run’ function. |
| [Generate Payment Request](#unique_83) [page ] 163 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Screen Payment Log displays, payment request has been generated, make a note of the key number displayed on this screen. |
| [Process Payment Request](#unique_84) [page ] 165 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | The payment document has been created.the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Cash Operations - Standard (BFB). |
| [Bank-Initiated Payment](#unique_66) [page ] 111 | Treasury Specialist - Back Office | - | This step is outside of SAP system |
| [Post to General Ledger](#unique_67) [page ] 111 | Treasury Accountant | Fix, Pay and Post Flows (TBB1) Process Business Transactions (TPM10) | Screen Posting Log: Posted Business Transactions displays, accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |
| [Calculate or Maintain Fair Value of Transaction](#unique_59) [page ] 89 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA) | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays, you can see the NPV, risk-free NPV, CVA, DVA of each transaction on the screen. |
| [Perform Key Date Valuation](#unique_60) [page ] 92 | Treasury Accountant | Run Valuation (TPM1) | The screen Valuation Log displays, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages.The accounting document has been created in local GAAP (valuation area AE0). |
| [Decide to Exercise](#unique_85) [page ] 177 | Treasury Specialist - Front Office | Manage Financial Transactions (F6157) | The transaction is updated to Exercise and is saved without error |
| [Create FX Spot Contract](#unique_42) [page ] 178 | Treasury Specialist - Front Office | Manage Financial Transactions (F6157) | The data is saved and the new transaction number generated. |
| [Decide to Expire](#unique_86) [page ] 180 | Treasury Specialist - Front Office | Manage Financial Transactions (F6157) | The transaction is updated to Expiration and is saved without error |
| [Post Realized Profit and Loss](#unique_68) [page ] 114 | Treasury Accountant | Post Derived Business Transactions (TPM18) | New screen Posting Log: Posted Business Transactions displays, you can see the posting information for local GAAP (valuation area AE0),The accounting document has been created in local GAAP (valuation area AE0). |

Reporting

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Display Treasury Position Flows](#unique_87) [page ] 182 | Treasury Accountant | Display Treasury Position Flows (F1754) | The report displays with filtered data. |
| [Display Treasury Alerts - Posting](#unique_88) [page ] 183 | Treasury Accountant | Display Treasury Alerts (F4984) | The report displays with filtered data. |
| [Display Treasury Alerts - Settlement, Release, Payment and Correspondence](#unique_89) [page ] 184 | Treasury Specialist - Back Office | Display Treasury Alerts - Settlement (F4979) | The report displays with filtered data. |
| [Display Payment Schedule](#unique_90) [page ] 185 | Treasury Accountant | Display Payment Schedules (TJ04) | The report displays with filtered data. |
| [Display Treasury Posting Journal](#unique_91) [page ] 186 | Treasury Accountant | Display Treasury Posting Journal (F1755) | The report displays with filtered data. |
| [Treasury Position Analysis](#unique_92) [page ] 187 | Treasury Accountant | Treasury Position Analysis | The report displays with filtered data. |
| [Display Treasury Position Values](#unique_93) [page ] 188 | Treasury Accountant | Display Treasury Position Values (F1867) | The report displays with filtered data. |
| [Define Financial Positions](#unique_94) [page ] 188 | Treasury Risk Manager | Define Financial Positions (FTR_FP_DEF) | The report displays with filtered data. |
| [Financial Status (Book Value)](#unique_95) [page ] 190 | Treasury Risk Manager | Financial Status (F2136) | The report displays with filtered data. |
| [Display Treasury Payments](#unique_96) [page ] 191 | Treasury Specialist - Back Office | Display Treasury Payments (TPM20A) | The report displays with filtered data. |
| [Analyze NPV](#unique_97) [page ] 191 | Treasury Specialist - Middle Office | Analyze NPV (JBRX) | The report displays with filtered data. |
| [Calculate Market Risk Key Figures](#unique_98) [page ] 192 | Treasury Specialist - Middle Office | Calculate Market Risk Key Figures (AISGENKF) | The report displays with filtered data. |
| [Sensitivity Key Figures](#unique_99) [page ] 194 | Treasury Specialist - Middle Office | Sensitivity Key Figures - Single Analysis (AISS) | The report displays with filtered data. |
| [Review Limit Utilization Report](#unique_100) [page ] 195 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | The report displays with filtered data. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The test should take around <Enter a duration, e.g. 60 minutes>.

### Foreign Currency Risk Management and Accounting - Without Options

Purpose

In this section, you create foreign exchange (FX) transactions for hedging and non-hedging purposes. Additionally, you process subsequent steps to settle, fix and execute the contract to completion, either receiving or sending the payment. The FX transactions are tightly and automatically integrated with Cash Operations, General Ledger, and Correspondence. Daily reporting functionality is provided for the roles involved in the FX processes.

#### (1XN) Market Rates Management – Manually via Upload

Purpose

This step provides instructions to enter market data such as foreign currency exchange spot rates, swap rates, reference interest rates, and so on.

These data provide default values when creating new transactions, or calculating fair value for existing transactions.

Procedure

For more information, see the Market Rates Management – Manually via Upload (1XN) test script.

#### (1S4) Automatic Market Rates Management

Purpose

This step provides instructions to integrate market data with a data feed via SAP Business Technology Platform (SAP BTP), through manual operation or job scheduling. The Automatic Market Rates Management (1S4) scope item is optional for Foreign Currency Risk Management (1X1) to provide automatic update of the latest market data.

Procedure

For more information, see the Market Rates Management – Manually via Upload (1S4) test script.

#### Generate Limit Utilizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the end of the transaction day, the Treasury Specialist - Middle Office can execute the end-of-day process. The system determines and updates limit utilization based on the transactions and positions contained in the data pool, as well as the external transactions that were entered.

|  |
| --- |
| Note You can also schedule background job for this step. For more information, see the job scheduling step in the Appendix. |

Prerequisite

The market data is imported.

If security exists, the spot price needs to be maintained for current date. Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open End-of-Day Processing (KLNACHT). | The End-of-Day Processing (KLNACHT) screen displays. |  |
| 3 | Enter Criteria of End-of-Day Processing | Enter the following data and choose Execute:Valuation Date: for example, <Current Date>Determination Procedure: for example, <10 to 20>Company Code: for example 3310 | The system displays the message End-of-day processing was completed successfully. |  |

#### Analyze Cash Position

Purpose

At the start of the transaction day, the cash manager checks the cash position status, and makes decisions on the right financial instruments to use for short-term purpose based on analysis of cash position.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) app to analyze the cash position. For more information, see the Basic Cash Operations(BFB) test script.

#### Analyze Liquidity Forecast

Purpose

The cash manager checks the liquidity forecast regularly and makes decisions for medium-term or long-term financial instruments, such as investment, loan, or foreign exchange.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) app to analyze the liquidity forecast. For more information, see the Basic Cash Operations(BFB) test script.

#### Balance Sheet Exposure Management

Purpose

This section describes how to review the balance sheet exposures.

##### Review Balance Sheet FX Risk

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the Balance Sheet FX Risk to grasp the overview status of the balance sheet FX risks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Review Balance Sheet FX Risk (F1588). | The Review Balance Sheet FX Risk (F1588)screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Display Currency: For example, AEDExchange Rate Type: For example, MKey Date: <Current date> | The Standard sections displays data for all the company codes. |  |
| 4 | Drill Down to One Company Code | In the Company Code column, choose 3310. | The Balance Sheet FX Net Exposures list displays per the definition maintained in Define Key Figures for Balance Sheet FX Risk. |  |

##### Take Snapshot for Balance Sheet FX Risk

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you take snapshot for Balance Sheet FX risk on the Key Date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Take Snapshot - Balance Sheet FX Risk (FXM_SNAP) | The Take Snapshot-Balance Sheet FX Risk screen is displayed. |  |
| 3 | Entering General Information for take a snap shot | Make the following entries and choose Run:In the General area,Snapshot Description: for example: Take Snapshot-Balance Sheet FX RiskCreated in Status: CreatedKey Date Definition: Fixed DateKey Date: for example, <the current date>Reporting Currency: AEDExchange Rate Type: MIn the Filter area,Company Code: 3310Currency: <the risk currency, for example, USD for DE>In the Time Pattern area,Period Definition: for example, <select>Start Date: for example, <the first day of current year>End date: for example, <the last day of current year>Increment: for example, 1Unit: for example, MonthTest Run: <deselect> | The Snapshot Details screen is displayed.Please note down the Snapshot ID for follow-up steps. |  |

##### Check and Process Snapshot Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check and edit snapshot item for Balance Sheet FX risk

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Snapshots - Balance Sheet FX Risk(F4763) | The Process Snapshot - Balance Sheet FX Risk screen is displayed |  |
| 3 | Check Snapshot Item | Enter the snapshot ID you noted down in the field Snapshot ID and choose Go.Choose > at the end of the row for the snapshot you just created.In the Snapshot screen, choose > at the end of the row for the snapshot item you want to check the details.Check the snapshot item. | The Snapshot Item screen is displayed. |  |
| 4 | Create a New Snapshot Item (Optional) | Choose Back to go back to the Snapshot screen.Choose Create.In the New Snapshot Item screen, enter the following data and choose Create:Company Code: 3310Amount: for example, 1,000,000 <the risk currency, for example, USD for DE>Period Start: for example, <the first day of current month>Period End: for example, <the last day of current month> | A snapshot item is created, with the Manual flag. |  |
| 5 | Edit a Snapshot Item (Optional) | Choose Edit, change the data, for example change the Amount to 2,000,000 and choose Save. | Your changes are saved. |  |

##### Release Snapshot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release the updated snapshot for Balance Sheet FX risk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Snapshots - Balance Sheet FX Risk (F4763) | The Process Snapshot - Balance Sheet FX Risk screen is displayed. |  |
| 3 | Release a Snapshot | Select the snapshot you just edited and choose ReleaseChoose OK in the dialog box. | The snapshot is released. |  |

##### Review Balance Sheet FX Risk Based on Snapshot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can view the balance sheet FX Risk based on snapshot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Balance Sheet FX Risk Overview - Based on Snapshots (F4765). | The Balance Sheet FX Risk Overview-Based on Snapshots screen is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Display Currency: For example, AEDExchange Rate Type: For example, M | The Net Open Amount Overview chart is displayed as default. |  |
| 4 | Change View | Choose Chart and Table view | The Hedging Detail table displayed below the chart. |  |
| 5 | Drill Down to One Snapshot | In the Snapshot ID column, choose the snapshot ID you noted down | Hedging details of the snapshot is displayed.Because there is no hedge request from this snapshot ID yet, there is just Key Figure Type of Net Exposure of Snapshot. |  |

#### Cash Flow Exposure Management

Purpose

This section describes how to enter cash flow exposure based on some exposure data from an external system.

##### Collect Exposure Data

Purpose

Users collect exposure data from various teams and departments to generate a collection of exposures to enter into the SAP system.

This step is done outside of the SAP system.

##### Create Raw Exposure

Purpose

You have two options to create raw exposure depending on different Data Source of Filters for Exposures when define Hedging Area:

- Create Raw Exposure using Exposure Management 2.0.
- Create Raw Exposure using FX Exposure Management.

###### Create Raw Exposure using Exposure Management 2.0

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a raw exposure in the SAP system based on data obtained from external data source.

Prerequisites

A specific data format is required for Option 2: Import the raw exposures from spreadsheet. For more information on template file generation, see Description on the Template for Import Raw Exposures and Sample Data for Import Raw Exposures in the Appendix.

You have defined Raw Exposure for E_EM2 as data source (Exposure Management 2.0) when define hedging area.

Procedure

Option 1: Create the raw exposure manually.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Raw Exposure (FTREX1). | The Raw Exposure: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Create:Exposure Activity Type: For example, YFXO | The Raw Exposure Maintenance: Create screen displays. |  |
| 4 | Enter Header Data | On the Header Data tab, make the following entries:Ext. Doc. No.: For example, <Current date>001Default Exposure Category: For example, 01Company Code: 3310Crit4ExpPosType: FXDirection: For example, OUT | The screen switches to Line Item Data tab. |  |
| 5 | Line Item Data | Choose the Line Item Data tab. |  |  |
| 6 | New Line Item | Choose Create New Line Item. |  |  |
| 7 | Enter Line Item Data | Make the following entries and choose Save:Ext ItemNo: For example, 1001ExpDueDte: For example, <Current date + 3 Months>Exposure Amount: For example, 100,000,000.00ExpAmtCrcy: USDTargetCrcy: AEDNote If you chose Currency Defined by the Source in [Define Hedging Area](#unique_21) [page ] 30, you can maintain target currency as risk free currency other than company code currency. | The Messages dialog box displays messages indicating successful release, creation, and saving. |  |

Option 2: Import the raw exposures from spreadsheet.

|  |
| --- |
| Note You may encounter an issue if your browser is in private browsing mode. Switch to regular mode to execute following steps. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Import Raw Exposures - Spreadsheet (FTREX_EXCEL_UPLOAD). | The Excel Upload Raw Exposure screen displays. |  |
| 3 | Upload Local File to Device | Choose Local File for Upload/Download.Note If your browser displays the message Store files on this device, choose Allow to proceed. | The Select Exposure File screen displays. |  |
| 4 | Import from native file system | Choose Import from native file system. Select the template file from the local file system and choose Open.Note The template must be in a specific format. For more information on the file format, see the Description on the Template for Import Raw Exposures section in the Appendix.Note The file must have the .xlsx extension.Note Some sample data is provided in the Appendix in the Sample Data for Import Raw Exposures topic.The following steps assume you use the sample data provided in the Appendix. | After import, an Information dialog box displays the message Import finished. Number of imported files:1 |  |
| 5 | OK | Choose OK | The Select Exposure File dialog displays the exposure file. |  |
| 6 | Choose Exposure File to Import and Execute | Select the exposure file and choose the Choose button. | The file path in the File name field displays in the Excel Upload Raw Exposure screen. |  |
| 7 | Test Run the Import | Make the following entries and choose Execute:Display data before processing: SelectedTest Run: Selected | The Exposure Upload Data - Simulation screen displays. |  |
| 8 | Confirm Test Run Result | Review the exposure data. Once you confirm it, chooseExecute. | The Status column displays on the left. Successful records are marked with traffic light symbol. |  |
| 9 | Production Run the Import | Choose Exit. | The Select Exposure File screen displays. |  |
| 10 |  | Make the following entries and choose Execute:Test Run: Deselected | The Exposure Upload Data screen displays the imported data. |  |
| 11 | Production Run and Review the Import Result | Choose Execute. | The Exposure Upload screen displays with import results in it.Successfully imported records are indicated by green traffic light symbols and values in Raw Exposure ID. |  |

###### Create Raw Exposure using FX Exposure Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a raw exposure in the SAP system using FX Exposure Management. FX Exposure Management allows customers to intuitively administer FX Exposures tailored to Hedge Management Use Cases.

Prerequisites

You have defined E_FXEM as data source (FX Exposure Management) when define hedging area.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage FX Exposures (F7990). | The Manage FX Exposures screen displays. |  |
| 3 | Create FX Exposure | Choose Create. | The New: FX Exposure screen displays. |  |
| 4 | Enter Header Data | On the Header Data tab, make the following entries:FX Exposure Type: For example, SFXDue Date: For example, <Current date + 3 Months>Company Code: 3310 | The screen switches to FX Exposure Details tab. |  |
| 5 | Enter FX Exposure Details | On the FX Exposure Details tab, make the following entries:Direction: For example, IncomingTarget Currency: For example, <MD risk currency>Amount: For example, 100,000,000.00 <MD CC currency>Valid From: For example, <Current date>Choose Create. | The status change history displays status Created with date and time. |  |
| 6 | Submit FX Exposure | Choose Submit for Release. | The Messages dialog box displays messages indicating FX exposure submitted. |  |
| 7 | Sign Out |  |  |  |
| 8 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 9 | Access the SAP Fiori App | Open Manage FX Exposures (F7990). | The Manage FX Exposures screen displays. |  |
| 10 | Release FX Exposure | Choose Go to display all FX exposures.Choose the FX exposure created and submitted in previous steps and choose Release. | The Messages dialog box displays messages indicating FX exposure released. |  |

##### Take Snapshot for Cash Flow Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Take snapshot for cash flow exposure on the Key Date.

Prerequisites

A Hedging Area exists. To create a Hedging Area, see the previous Define Hedging Area procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Take a Snapshot | Open Take Snapshot (TOESNAP). | The Take Snapshot screen is displayed. |  |
| 3 | Enter General Selections | On the General Selections tab, make the following entries and choose Run:Hedging Area: For example, AE0001Description: For example, <Current date> snapshotExtraction Date: for example , <the current date>Note You can also take a snapshot with extraction date in the past when there is no snapshot taken for the hedge area. Please note that you can only take a snapshot with extraction date in the past for one time.Day Reference: <select this checkbox>Note The Day Reference checkbox must be selected if you want to perform the Generate Hedge Request operation.When you set Reset Target Quota indicator, manually overwritten target quotas in Hedge Management Cockpit are reset to the target quotas originally defined in your hedging area, which are used with the new snapshot date. | A log is displayed with a notification that the snapshot is successfully created. |  |

##### Review Cash Flow Net Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the cash flow net exposure in the Hedge Management Cockpit.

Prerequisites

A Hedging Area exists. To create a Hedging Area, see the previous Define Hedging Area procedure.

A snapshot on the Key Date exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Hedge Management Cockpit (TOENE). | The Hedge Management Cockpit view is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entry, and choose Start:Hedging Area: For example, AE0001Layout ID： 1R_ALL_CH | The Hedge Management Cockpit for Hedging AreaAE0001 displays with the exposure data.Note If you choose Currency Defined by the Source and exposure items are created based on the cross-currency exposures during snapshot, the hedge management cockpit displays the Target Currency, Risk Currency and Company Code Currency |  |

#### Analyze Exposure and Agree on Hedging Actions

Purpose

Analyze the exposure data with related teams and organizations and agree on hedging actions. This step is performed outside of the SAP system.

#### Create Trade Request

Purpose

You have three options to create trade requests:

- Create Trade Request via Balance Sheet Exposure Hedge Request
- Create Trade Request via Cash Flow Hedge Request
- [Create Trade Request Manually](#unique_110) [page ] 73

##### Create Trade Request via Balance Sheet Exposure Hedge Request

###### Generate Hedge Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you generate a balance sheet foreign exchange (FX) hedge request.

Prerequisites

You have taken and released a snapshot as described in the [Balance Sheet Exposure Management](#unique_103) [page ] 52 section.

Procedure

Option 1: Generate Hedge Request without Predefined Parameters

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Generate Hedge Request - Balance Sheet FX Risk (FXM_REQUEST). | The Generate Balance Sheet Exposure Hedge Requests screen is displayed. |  |
| 3 | Enter General Information for Generate Balance Sheet Exposure Hedge Requests | Make the following entries and choose Run:In the Snapshot area,Selection by Snapshot ID: for example, <select>Snapshot ID: for example, <the ID you noted down in step Take Snapshot for Balance Sheet FX Risk>Note Please make sure to use the same snapshot ID in taking snapshot.In the Filter for Snapshot areaCompany Code: 3310Currency: <the risk currency, for example, USD>In the Value Date area,Fixed Date: <select>Value Date Selection: Current Month EndIn the Main Parameter area,Instrument Category: FX ForwardTarget Status: CreatedTest Run: <deselect> | The Balance Sheet Exposure Hedge Request List is displayed. |  |

Option 2 Generate Hedge Request with Predefined Parameters

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Hedge Requests-Balance Sheet FX Risk (F4764). | The Balance Sheet Exposure Hedge Request screen is displayed. |  |
| 3 | Enter General Information for Generate Balance Sheet Exposure Hedge Requests | Choose CreateIn the dialog box, make the following entries and choose Create:Snapshot ID: for example, <the snapshot ID you noted down>Note Please make sure to use the same snapshot ID in taking snapshot.Request Parameter Group: for example, RP_GRP2 | The Balance Sheet Exposure Hedge Request List is displayed with new created hedge request(s). |  |

###### Check and Process Hedge Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check and process a balance sheet foreign exchange (FX) hedge request.

Prerequisite

A balance sheet foreign exchange (FX) hedge request is created and available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Hedge Requests-Balance Sheet FX Risk (F4764). | The Balance Sheet Exposure Hedge Request screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Go:Company Code: for example, 3310 | Balance sheet exposure hedge requests that match the filter criteria are displayed. |  |
| 4 | Check the Request | Select the row of the Hedge Request you just created and choose > at the end of the row. | The Hedge Request screen is displayed. |  |
| 5 | Edit the Request (Optional) | Choose Edit, change the data, for example, change the Amount to 80% of the original amount, and choose Save. | Your changes are saved. |  |

###### Release Hedge Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release a balance sheet foreign exchange (FX) hedge request.

Prerequisites

A balance sheet foreign exchange (FX) hedge request is created and available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Hedge Requests-Balance Sheet FX Risk (F4764). | The Balance Sheet Exposure Hedge Request screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Go:Company Code: for example, 3310 | Balance sheet exposure hedge requests that match the filter criteria are displayed. |  |
| 4 | Release the Request | Select the row of the Hedge Request you just edited and choose Release.Choose OK in the dialog box. | The balance sheet exposure hedge request is released successfully. |  |

##### Create Trade Request via Cash Flow Exposure Hedge Request

###### Generate Hedge Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you generate a cash flow foreign exchange hedge request.

Prerequisites

You have taken a snapshot with Day Reference as described in the [Take Snapshot for Cash Flow Exposure](#unique_38) [page ] 62 step.

Procedure

Table 7: Generate Hedge Request Manually

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Hedge Management Cockpit (TOENE). |  |  |
| 3 | Manage Layouts | Choose Manage Layouts. | The Layout Overview screen displayed. |  |
| 4 | Create Your Own Lay-out | Select a row of default Layout ID, for example, 1R_ALL_CH and choose Create with template | The New Layout ID screen is displayed |  |
| 5 | Enter Layout ID | Enter the following data and choose Enter:Layout ID: for example, 2R_TQ_CH | The Layout screen is displayed |  |
| 6 | Choose Key Figures for new Layout | Make the following entries, choose Save, and then choose Back.Description: for example, With Target Quota (Key Figures in Rows)Target Quota Type: for example, YLQOn the Key Figure tab, enter the following data and choose Save:Amount to Hedge: Display Level, for example, 1; Order, For example, 8Target Quota [%]: Display Level, For example, 1; Order, For example, 9Upper Target Quota [%]: Display Level, For example, 1; Order, For example, 10Lower Target Quota [%]: Display Level, For example, 1; Order, For example, 11 |  |  |
| 7 | Enter Selection Criteria | Make the following entries:Hedging Area: For example, AE0001Layout ID: 2R_TQ_CHand choose Start. | The Hedge Management Cockpit for Hedging Area AE0001 is displayed with the exposure data and target quota in it.Note You could overwrite target quota by selecting a target quota cell and clicking on Overwrite Target Quota.The overwritten target quota shall be applied to calculated key figures depending on the target quota, for example, Target Hdg Amt and Amount to Hedge. |  |
| 8 | Generate Hedge Request | Select a field that has Net Exposure value, for example, a field with Net Exposure value in the future three months, and choose Hedge Request > FX Hedge Request to create a hedge request.Note Select a field properly to create hedge request, otherwise you will get the Requirements for navigation to a hedge request not fulfilled error message. | The Hedge Request view is displayed.Note If the system displays the error message Select a currency for working day check, maintain the calendar assignment to currency via the Assign Calendars to Currencies configuration activity. |  |
| 9 | Save Hedge Request | Make the following entries:Hedge Request ID: For example, FX hedgeInstrument Cat.: For example, FX ForwardHedging Classificatn: For example, Y0Value Date: For example, <current date + 3 months>Hedge Request Amount: For example, + 1,000,000and choose Save. |  |  |

Table 8: Generate Hedge Request Automatically

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Generate Hedge Request Automatically | Choose Automated Request CreationCheck the row of Hedge request can be created and modify the following default entries if necessary and choose Save:AmountHedge Request Value DateInstrument Category.Note you must make the key figure Amount to Hedge available in your chosen layout. | The Hedge Request with group ID were saved message is displayed. |  |

###### Release Hedge Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to release an foreign exchange (FX) hedge request.

Prerequisites

An FX trade request is created and available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO). | The Process Hedge Requests (TOEHREQO) view displays. |  |
| 3 | Enter Selection Criteria | Enter the following data:Company Code: for example, 3310and choose Start. | The system displays the hedge requests that match the filter criteria. |  |
| 4 | Submit the Request | Select the row of the Hedge Request and choose Process and then select Submit from the dropdown list. | Log displays that the hedge request was submitted. |  |
| 5 | Release the Request | Select the row of the Hedge Request and choose Process and then select Release from the dropdown list. | Log displays that the hedge request was released. |  |
| 6 | Perform the Get Operation in the SAP Business Technology Platform (SAP BTP) App | Perform the Get operation in accordance with the instructions in the Treasury Trading via Trading Platforms(2F5) test script. | The Get operation completes successfully. |  |
| 7 | Confirm Update Status | Double-click the Hedge Request.Choose the Trade Request button.and confirm the Trade Req. Status in the Assigned Trade Request dialog box. | The status of the trade request changes to Transferred after you reload the page. |  |

##### Create Trade Request Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create trade request manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Requests (TPITRO). | The Process Trade Requests view displays. |  |
| 3 | Create Manual Trade Request | Choose Create Trade Request.In the General tab, enter the following data and Save:Company Code: for example,3310Instrument Cat.: for example, FX ForwardBuy/Sell: for example, BuyRequested Amount: for example, 10,000USDOpposite Currency: for example, AEDValue Date: for example, <current date 3 months> | The Trade Request - Display view displays. |  |
| 4 | Back to Previous Screen | Choose Back. |  |  |
| 5 | Submit the Request | Select the row of the Trade Request and choose Process and then select Submit from the dropdown list. |  |  |
| 6 | Release the Request | Select the row of the Trade Request and choose Process and then select Release from the dropdown list. | The status of the trade request changes to In Transfer |  |
| 7 | Confirm Update Status | Check the status of the trade request.Note A trade request with status In Transfer is automatically transferred to TPI and status changes to In Process once successfully receive the trade request. | The status of the trade request changes to In Process. |  |

#### Check Trade Request Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the status of all trade requests.

Prerequisites

There are foreign exchange trade requests created and released to make the trade requests available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Requests (TPITRO). | The Process Trade Requests view is displayed. |  |
| 3 | Enter Selection Criteria | Check the settings of the check boxes on the Selection screen and press Start. | The system displays the trade requests that match the filter criteria. |  |
| 4 | Check the Originating Request | Select the row of a Trade Request and choose Originating Request. | The Trade Request - Display view is displayed. |  |
| 5 | Check the Request | Choose Change and then choose Check. | Log displays that the trade request is consistent. |  |

#### Check Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to check the limit utilization report.

Prerequisites

The limit master records of your company are maintained in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Execute:Limit Type: for example, Y01 or Y07Limit Utilization Base: for example, 1Determination Date: for example, <the current date>Limits Valid From: for example, <the current date> | An overview of the limit utilization in accordance with your selection criteria is displayed. |  |

#### Create Foreign Exchange Contract

Purpose

In this section, you can create foreign exchange contracts for hedging or non-hedging purposes.

##### Create FX Spot/Forward

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Foreign Exchange Spot or Forward transaction for hedging or non-hedging purposes.

You can also create a Foreign Exchange Spot or Forward transaction by copying an existing FX Spot/Forward. For more information, see the [Copy Existing Transaction](#unique_112) [page ] 262 step in the Appendix.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Enter:Company Code: For example, 3310Product Type: 60ATransaction Type: For example, 101Partner: For example, 33537001Note Use Transaction Type 102 for forward transaction. | The Spot/Forward Transaction Entry: Structure screen displays. |  |
| 4 | Enter Data | Maintain the following fields and then choose the Administr. tab:Rate: For example, AED/USD <enter a proper rate>Buy/Sell: For example, B BuyTraded Amt: For example, USD 1MValue Date: +2Note You can enter a Value Date greater than +2 days for forward transactions.If the currency pair is not defined, you can define the currency pair via configuration step Define Leading Currency.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | The Administr. tab displays. |  |
| 5 | Enter Data in Administration Tab | Enter data and choose Save:Hdg Classific.: For example: Y0Risk Mitigation: <select> | Transaction is saved and a transaction number is generated. |  |

##### Create FX Swap

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Foreign Exchange Swap transaction for hedging or non-hedging purposes.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Swap (TX10). | The Create Forex Swap: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and press EnterCompany Code: For example, 3310Partner: For example,33537001First transactionProduct Type: 60ATransaction Type: For example, 101Second transactionProduct Type: 60ATransaction Type: For example, 102 | The Create Forex Swap: Structure screen displays. |  |
| 4 | Enter data | Enter data and choose Save:1st TransactionCurrencies: For example, EUR/USDRate: For example, 1.3Buy/Sell: For example, B BuyTraded Amt: For example, USD 1MValue Date: For example, +22nd TransactionRate: For example, 1.2Value Date: For example, ++6 | Two transactions are saved and two transaction numbers are generated. |  |

##### Create Non-Deliverable Forward

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a foreign exchange nondeliverable-forward transaction for hedging or non-hedging purposes.

You can also create a Foreign Exchange Nondeliverable Forward transaction by copying an existing NDF. For more information, see the [Copy Existing Transaction](#unique_112) [page ] 262 step in the Appendix.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose EnterCompany Code: For example, 3310Product Type: 60BTransaction Type: For example, 110Partner: For example,33537001 | The Spot/Forward Transaction Entry: Structure screen displays. |  |
| 4 | Enter data | Enter the following data and choose Administr.Rate: For example, AED/BRL <enter a proper rate>Buy/Sell: For example, B BuyTraded Amt: For example, BRL 50MValue Date: ++6+2Fixing Date: ++6Settlement Currency: AEDNote If the currency pair is not defined, you can define the currency pair via configuration activity Define Leading Currency. | The Administr. tab is displayed. |  |
| 5 | Enter Data in Administration tab | Enter data and choose Save:Hdg Classific.: For example, Y0Risk Mitigation: <select> | The transaction is saved and a transaction number is generated.Note If the system displays the error message No currency pair is defined for currencies, maintain the currency pair via the Define Leading Currency SSCUI. |  |

#### (BFB) Basic Cash Operations

Purpose

After the deal is created (in Contractstatus) but before payment is executed, the future cash flows of this deal is reflected in liquidity forecast reports. If basic cash management is implemented in your system, use the Cash Flow Analyzer (F2332) app to check the liquidity forecast.

|  |
| --- |
| Note This step can be executed during the whole lifecycle of the treasury deal. Different results under liquidity forecast reports are shown in the different processing phases of the transaction (for example, before transaction is created, after transaction is created, and after payment is posted). |

Procedure

If basic cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) app to check the liquidity forecast change. For more information, see the Basic Cash Operations (BFB) test script.

Treasury relevant cash flows are reflected in treasury specific planning levels. For example:

- MM - Money Market Deals
- NM - MM Deals (Bank unknown)
- FX - Foreign Exchange Deals
- FO - Foreign Exchange Options
- NF - Forex Deals (Bank unknown)
- DR - Derivative Deals
- ND - Derivative Deals(Bank unknown)

#### (J78) Advanced Cash Operations

Purpose

After the deal is created (in Contract status) but before payment is executed, the future cash flows of this deal is reflected in liquidity forecast reports. If full cash management is implemented in your system, use the Cash Flow Analyzer (F2332) or Check Cash Flow Items (F0735) apps to check the liquidity forecast.

|  |
| --- |
| Note This step can be executed during the whole lifecycle of the treasury deal. Different results under liquidity forecast reports are shown in the different processing phases of the transaction (for example, before transaction is created, after transaction is created, and after payment is posted). |

Procedure

If full cash management is implemented in your system, you can use the Cash Flow Analyzer or Cash Flow Analyzer (F2332) apps to check the liquidity forecast change. For more information, see the Advanced Cash Operations (J78) test script.

Treasury relevant cash flows are reflected in treasury specific planning levels. For example:

- MM - Money Market Deals
- NM - MM Deals (Bank unknown)
- FX - Foreign Exchange Deals
- FO - Foreign Exchange Options
- NF - Forex Deals (Bank unknown)
- DR - Derivative Deals
- ND - Derivative Deals(Bank unknown)

In addition, in full cash management apps, you can also select treasury specific cash flows by filtering certainty levels:

- TRM_D - Financial Instrument
- TRM_O - Optional Financial Instrument

#### Correspondence

Purpose

SAP TRM provides the standard correspondence functionality. With this correspondence functionality, whenever a TRM transaction is saved, SAP either sends an email to the Business Partner, or automatically prints a form.

To use this correspondence functionality, the following data must be assigned to the Business Partner:

- Business Partner Profile
- Business Partner group
- Swift/BIC code

In addition, SAP TRM provides Treasury Correspondence Integration with SWIFT Network via Multi-Bank Connectivity (MBC). The outgoing correspondence objects and relevant SWIFT messages can be generated automatically when you create OTC transactions; The SWIFT Message can be delivered to and sent back from the counterparty's SWIFT code via MBC. Then relevant incoming correspondence objects are generated automatically in the SAP client. Once the incoming correspondence object is matched with the outgoing correspondence object with confirmation, the OTC transaction is settled accordingly. For more information, refer to the Treasury Correspondence Integration with SWIFT Network(3QM)

##### Set Settlement Status (Manual)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a TRM transaction is recorded and saved in SAP, the transaction must be settled before you perform further activities. You can settle the transaction via one of two methods once you get counterparty confirmation:

- Manual settlement

For example, if you receive a counterparty confirmation e-mail, use following apps to settle the transaction manually:

-
    - Manage Financial Transactions
- Automatic settlement via correspondence process.

For example, for one transaction, once all the outgoing and incoming correspondence objects are matched and set to completed status, the financial transactions are automatically set to settlement status.

In this activity, you settle the TRM transaction manually.

Prerequisites

A TRM transaction is created successfully in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <Transaction Number created in previous step> | The transaction is displayed on the screen. |  |
| 4 | Settle the TRM Transaction | Select the checkbox at the beginning of the transaction line and choose Settle. | The Settle Forex Transaction: Structure screen displays with the transaction data. |  |
| 5 | Save Change | Choose Save. | The transaction is settled and saved. |  |
| 6 | TRM Transaction Status | Select the checkbox and choose Details at the end of the transaction line. | The Display Forex Transaction: Structure screen is displayed. |  |
| 7 | Check Status | Choose ... > Status.The Activity Cat field should be in Contract Settlement status. | The transaction is in Contract Settlement status. |  |

##### Correspondence with PDF Form

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

###### Send Confirmation Email / Print

Purpose

SAP provides Business partner group BPG_DEFAULT. By default, if any business partner is assigned to this group, correspondence objects are automatically sent when a financial transaction is saved. As described in the preliminary steps, the Business Partner 33537001 is assigned to BPG_DEFAULT, so the correspondence objects are sent automatically. However, if you create a new business partner group via configuration stepDefine Business Partner Group and do not assign the auto-send attribute, you may need to send those correspondence objects manually via the Send Correspondence (FTR_COSEND) app.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

This step does not require any operation in the system.

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

In the prior step, for Email channel, an outbound email is sent to the Business Partner. Normally, you receive counterparty confirmation from the Business Partner via Email, phone, and so on. This step is performed outside of the SAP system.

Procedure

This step does not require any operation in system.

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

In the prior step, all transaction correspondence objects are matched successfully. In standard functionality, the transaction is settled automatically.

In this step, you check if the transaction is automatically settled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor screen displays. |  |
| 3 | Enter selection criteria on the initial screen | Enter the following data and choose Execute:Correspondence tab:Company Code: For example, 3310Deal tab:Company Code: For example, 3310Deal Number: For example, <Transaction Number> | The Correspondence monitor - Standard View screen displays. |  |
| 4 | Display the transaction history | Select the checkbox for the incoming correspondence object and choose Show Underlying. | The Display Forex Transaction: Structure screen displays, with Activity 2 Contract Settlement on the second line. |  |

#### Period end has been reached

##### Calculate or Maintain Fair Value of Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you determine the fair values (NPV - net present values) of financial transactions.

The net present values can be calculated automatically by the Market Risk Analyzer (MRA) and saved to table VTVBAR. These values can then be used for the accounting valuation. In addition, you can also maintain the relevant net present value manually.

Predelivered configuration in MRA provides three options when calculating NPV automatically via app Calculate Net Present Values - With CVA and DVA (TPM60CVA)):

- Risk-free NPV: using the evaluation type that doesn't contain basis spread curve or credit spread curve, system only calculates the risk-free NPV.
- Risk-based NPV with credit spread curve: using the evaluation type that contains credit spread curve, system calculates risk-free NPV by using risk-free yield curve, and calculates the (risk-based) NPV, which also accounts for credit spreads.
- Risk-based NPV with basis spread curve and credit spread curve: using the evaluation type that contains basis spread curve and credit spread curve, system calculates risk-free NPV by using risk-free yield curve and basis spreads curve, and calculates the (risk-based) NPV, which also accounts for credit spreads.

There are two kinds of calculation method for CVA and DVA:

- Based on Expected Exposures
- Difference method

The formula for NPV is: NPV = risk-free NPV - CVA - DVA.

Prerequisites

Before calculating NPV via the Calculate Net Present Values - With CVA and DVA (TPM60CVA) app, ensure that relevant market data (interest rates, foreign exchange rates, credit spreads, and so on) are maintained for the evaluation date. For details of market data maintenance, see the Market Rates Management – Manually via Upload (1XN) test script.

If you want to use Par Method to calculate NPV for your FX foward transactions, please update the FX Valuation Method to Currency Conversion Before Discounting in relevant Evaluation Type via configuration step Define and Set Up Evaluation Types in advance.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

Option 1: Calculate NPV Automatically

|  |
| --- |
| Note You can also schedule the background job for the first option. For more information, see the corresponding step in the Appendix. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments screen displays. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute:Evaluation Parameter Derivatn: DeselectedSelect OTC Transaction: SelectedCompany Code: for example, 3310Transaction: <transaction number from previous steps>Evaluation Date: for example, <last date of current month>CVD/DVA Type: To calculate risk-free NPV, enter nothing. To calculate risk-based NPV and CVA/DVA, enter Y01.Evaluation Type: To calculate risk-free NPV, enter Y001. To calculate risk-based NPV and CVA/DVA, enter Y002.Test Run: DeselectedPrice/NPV Type: 001Save Values with Warnings: SelectedDetail Log (Other Calc. Steps):Selected | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays, the NPV, risk-free NPV, CVA, DVA of each transaction.To check other information, you can use the following buttons:Single Transaction:CVA/DVA Key FiguresDetailed LogCalculation BasesError Log |  |

Option 2: Maintain NPV Manually

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

You use the valuation function to value the positions of financial instruments based on historical cost or fair value for a given key date, and transfer results to financial accounting.

|  |
| --- |
| Note You can also schedule background job for this step. For more information, see the corresponding step in the Appendix section. |

Prerequisites

Fair values (NPV) are calculated or maintained for financial transactions, which are evaluated at fair value (NPV) according to accounting principles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Run Valuation screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:In the Product Groups area,OTC Transactions: <Select this checkbox>In the General Selections area,Company Code: for example, 3310Valuation Area: for example, AE0Transaction: <transaction number(s) created in previous steps, for zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs>In the Valuation Parameters area,Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation with ResetNote When the period end is also the year end, use the Valuation Category Year End Valuation.Test Run: <selected> | The Display Selected Treasury Positions for Valuation screen displays. |  |
| 4 | Execute Valuation for Test Run | Choose Run Valuation.If a Message dialog box displays, choose Continue. | The Valuation Log screen displays. If a red traffic light is shown, click it and check the error message. Solve the issue and perform a test run again until you resolve the error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. There is no posting created because it is a test run.Note Sometimes, there is no simulated posting because your selected transaction may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the Run Valuation screen.Change the following data and choose Execute:Test Run: <deselect> | The Display Selected Treasury Positions for Valuation screen displays. |  |
| 6 | Execute Valuation for Production Run | Choose Run Valuation. | The Valuation Log screen displays. Check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. The accounting document is created in the local GAAP (valuation area AE0). |  |

#### Transaction is Mature

Purpose

This section describes the required operations such as fixing an NDF transaction or payment when a transaction is mature.

##### For NDF

Purpose

The fixing rate is required for Non-Deliverable Forwards (NDFs).

###### Fix Rate for NDF

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you fix the rate for a NDF transaction.

Prerequisites

An NDF transaction exists and approaches maturity.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Fix FX Rates (TXV5). | The Execute Fixing Transaction: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and press EnterCompany Code: for example, 3310Transaction: <the number of maturing transaction> | The Execute Fixing Transaction: Structure screen displays.The Rate for Settlement is automatically suggested from currency table. |  |
| 4 | Confirm and Save Data | Review the Settlement section. When you are done with your review, choose Save. | The data is saved without error. |  |

###### Correspondence

Purpose

SAP TRM provides the standard correspondence functionality. With this correspondence functionality, whenever a TRM transaction is saved, SAP either sends an email to the Business Partner, or automatically prints a form.

To use this correspondence functionality, the following data must be assigned to the Business Partner:

- Business Partner Profile
- Business Partner group
- Swift/BIC code

###### Set Settlement Status (Manual)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a TRM transaction is recorded and saved in SAP, the transaction must be settled before you perform further activities. You can settle the transaction via one of two methods once you get counterparty confirmation:

- Manual settlement

For example, if you receive a counterparty confirmation e-mail, use following apps to settle the transaction manually:

-
    - Manage Financial Transactions
- Automatic settlement via correspondence process.

For example, for one transaction, once all the outgoing and incoming correspondence objects are matched and set to completed status, the financial transactions are automatically set to settlement status.

In this activity, you settle the TRM transaction manually.

Prerequisites

A TRM transaction is created successfully in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <Transaction Number created in previous step> | The transaction is displayed on the screen. |  |
| 4 | Settle the TRM Transaction | Select the checkbox at the beginning of the transaction line and choose Settle. | The Settle Forex Transaction: Structure screen displays with the transaction data. |  |
| 5 | Save Change | Choose Save. | The transaction is settled and saved. |  |
| 6 | TRM Transaction Status | Select the checkbox and choose Details at the end of the transaction line. | The Display Forex Transaction: Structure screen displays. |  |
| 7 | Status | Choose ... > Status.The Activity Cat field should be in Fixing Settlement status. | The transaction is in Fixing Settlement status. |  |

###### Correspondence with PDF Form

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

###### Send Confirmation Email / Print

Purpose

SAP provides Business partner group BPG_DEFAULT. By default, if any business partner is assigned to this group, correspondence objects are sent automatically when a financial transaction is saved. As described in the Preliminary steps section of this document, Business Partner 33537001 is assigned to BPG_DEFAULT, so the correspondence objects are sent automatically. However, if you create a new business partner group via SSCUIDefine Business Partner Group and do not assign the auto-send attribute, you may need to send those correspondence objects manually via the Send Correspondence app.

Procedure

This step does not require any operation in system.

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

In the prior step, for Email channel, an outbound email is sent to the Business Partner. Normally, you receive counterparty confirmation from the Business Partner via Email, phone, and so on. This step is performed outside of the SAP system.

Procedure

This step does not require any operation in system.

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

In the previous step, all correspondence objects of the transaction are matched successfully. As the standard functionality, the transaction is settled automatically.

In this step, you only check if the transaction has been settled automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor screen displays. |  |
| 3 | Enter selection criteria on the initial screen | Enter the following data and choose Execute:Correspondence tab:Company Code: for example, 3310Deal tab:Company Code: for example, 3310Deal Number: for example, <Transaction Number> | The Correspondence monitor - Standard View screen displays. |  |
| 4 | Display the transaction history | Select the checkbox of the incoming correspondence object and choose Show Underlying. | The OTC Option Display: Issue Structure screen displays. The second row shows Activity 2 Contract Settlement. |  |

For zero/low cost collar FX option (cylinder FX option), please check settlement status for both legs.

##### Payment for Mature Transaction

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
| 3 | Test Run | Enter the following data, and choose Run:Foreign Exchange: <select>Company Code: for example, 3310Transaction: <transaction number with outflows you created the in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Pay Only: <select this indicator>Test Run: <select>Pay Only: <select> | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable. |  |
| 4 | Back | Choose Back. | The Treasury: Post Flows view displays.The Fix, Pay and Post Flows view displays. |  |
| 5 | Production Run | Make the following change, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the check box Send for Approval will be uncheckable. |  |
| 6 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Foreign Exchange: <select>Company Code: for example, 3310Transaction: <transaction number with outflows you created the in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Test Run: <select>Pay Only: <select> | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable. |  |
| 4 | Back | Choose Back. | The Fix and Pay Flows view displays. |  |
| 5 | Production Run | Change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
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

Each financial transaction contains flows that must be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows that require payment request. It does not create postings in financial accounting.

If the payment is initiated by the financial partner, skip this procedure and the following [Process Payment Request](#unique_65) [page ] 108 procedure and continue with the [Bank-Initiated Payment](#unique_66) [page ] 111 procedure.

|  |
| --- |
| Note A background job can be scheduled for this step. For more information, see the Generate Payment Request procedure in the Job Scheduling section of the Appendix. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Run:Foreign Exchange: <select>Company code: for example, 3310Transaction: <transaction number with outflows you created the in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>Test Run: <select>Pay Only: <select> | The Payment Log - Test Run screen displays. Review the payment information on this view.If the system displays the No flows exist for processing notification, no payment with payment request is needed for your selection criteria. Go to the succeeding Post to General Ledger procedure. |  |
| 4 | Back | Choose Back. | The Treasury: Post Flows screen displays.The Fix, Pay and Post Flows screen displays. |  |
| 5 | Production Run | Change the following data, and choose Run:Test Run: <deselect> | The Payment Log screen displays. A payment request is generated.Make a note of the key number: __________ |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows screen displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Foreign Exchange: <select>Company Code: for example, 3310Transaction: <transaction number with outflows you created the in previous steps>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <current date>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Back | Choose Back: | The Fix and Pay Flows screen displays. |  |
| 5 | Production Run | Change the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. A payment request is generated.Make a note of the key number: __________ |  |

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
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen displays. |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: For example, <current date>Identification: For example,TRM01 | The Automatic Payment Transactions: Parameters screen displays. |  |
| 4 | Enter Parameters | Enter the following data and choose Dynamic selections:Posting Date: For example, <current date>Next payment run on: For example, <current date + 3 days>Company Code: For example, 3310Payment Methods: For example, TF | The Free Selection for payment run dialog box displays. |  |
| 5 | Key Number | Enter the following data and choose Save:Key Number: <the key number you noted down in previous step> | The Automatic Payment Transactions: Parameters screen displays. |  |
| 6 | Additional Log | Choose Additional Log. | The Additional Log dialog box displays. |  |
| 7 | Enter Parameters | Make the following entries and choose Continue:Payment method selection in all cases: <select>Line items of the payment documents: <select>Due date check: <select>If the system displays the message Log created for all accounts displays, choose Continue.Choose Save on the Automatic Payment Transactions: Parameters screen. | The system displays the message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 8 | Schedule Proposal | Choose Proposal. | The Schedule Proposal dialog box displays. |  |
| 9 | Schedule Job | Select Start Immediat. and choose Schedule Job. | The system displays the message Proposal is running with a yellow traffic light. |  |
| 10 | Update Status | Choose Status until the message Payment proposal has been created displays in the status bar with green traffic light. | The payment proposal is generated. |  |
| 11 | Schedule Payment | Choose Pmnt run. | The Schedule Payment dialog box displays. |  |
| 12 | Schedule Job | Select Start Immediat., select Create Payment Medium and choose Schedule Job. | The message Payment run is running displays in the status bar with a yellow traffic light. |  |
| 13 | Update Status | Choose Status until the message Payment run has been carried out displays with a green traffic light. | The Automatic Payment Transactions for Payment Requests screen displays.The payment document is created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium is created if it uses PMW format. You can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you see the message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media. A BCM batch is created after the payment run. For more information, see the next test step. |  |
| 14 | Cross-Payment Run Payment Media (Create BCM Batch) | Choose Menu > Environment > Payment Medium > Cross-Payment Run Payment Medium > Create Payment Medium . | The Creation of Cross-Payment Run Payment Media screen displays. |  |
| 15 | Enter Data | Enter the following data and choose Run:Run Date: For example, <Current date>Identification: For example, TRM01R | The Creation of Cross-Payment Run Payment Media dialog box displays with the message Collector XX/XX/20XX XXXXXX was created or updated. The BCM batch is created.A batch may need additional approvals before the payment medium is finally created. For more information, see the Advanced Cash Operations(J78) test script. |  |

###### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

##### Bank-Initiated Payment

Purpose

If the outgoing payment is initiated by bank, it is not necessary to run the previous steps Generate Payment Request and Process Payment Request, because the outgoing payment is initiated by the bank.

Procedure

This step does not require any steps in the SAP system.

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

- Fix, Pay and Post Flows (TBB1): This SAP Fiori app supports to generate posting for incoming payment and outgoing payment without payment request. You can not use this app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request for Mature Transaction step with the Pay Only option.
- Process Business Transactions (TPM10): You use this SAP Fiori app to generate postings for outgoing payments that have been processed in the previous Generate Payment Request for Mature Transaction step with the Pay Only option.

|  |
| --- |
| Note A background job can be scheduled for this procedure, please see the Job Scheduling section in the Appendix. |

Prerequisites

Outgoing payments handled using payment request were processed in the previous Generate Payment Request for Mature Transaction procedure with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data:Foreign Exchange: SelectedCompany Code: For example, 3310Transaction: <transaction number with inflow created in previous steps, for zero/low cost collar FX option (cylinder FX option), it is the short leg>Up to and Including Due Date: Enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: SelectedPost Operational Only: Selectedand choose Run: | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created during a test run.If the system displays the No flows exist for processing notification, no posting is needed for your selection criteria.You can skip the next steps and continue with step 6, using the Process Business Transactions (TPM10) app. |  |
| 4 | Back | Choose Back. | The Fix, Pay and Post Flows screen is displayed. |  |
| 5 | Production Run | Make the following entries and choose Execute:Test Run: Deselected | The Posting Log: Posted Business Transactions view displays. The accounting document is created for incoming payment in local GAAP (valuation area AE0). |  |
| 6 | Access Another SAP Fiori App | Return to the SAP Fiori launchpad and open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: SelectedCompany Code: For example, 3310Valuation Area: For example, AE0Limit by Transaction Number: Deselect this checkboxLimit by Subledger Pos.: SelectedTransaction: <transaction number with outflow and its payment request that you generated in the previous Generate Payment Request procedure, for zero/low cost collar FX option (cylinder FX option), it is the long leg>Test Run: Selectedand choose Run. | The Test Run: Post/Reverse Business Transactions view displays.If the system displays the You have not selected any business transactions notification, no postings are needed for your selection criteria. You can skip the current step. |  |
| 8 | Check Test Run Result | Choose Select All.Choose Choose Those to Post.Choose Run. | The Test Run: Display Posted/Reversed Business Transactions view displays. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created during a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions view displays. |  |
| 11 | Deselect Test Run | Make the following change:Test Run: Deselectedand choose Run. | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 12 | Production Run | Choose Select All.Choose Choose Those to Post.Choose Run. | The Update Run: Display Posted/Reversed Business Transactions view displays. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in local GAAP (valuation area AE0). |  |

##### Post Realized Profit and Loss

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you fix and post derived business transactions (usually realized profit and loss when a deal is mature).

|  |
| --- |
| Note You can also schedule a background job for this step. For more information, see the corresponding step in the Appendix. |

Prerequisites

The maturity date of transaction is reached.

The financial transaction is created, settled, and posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany Code: For example, 3310Valuation Area: For example, AE0OTC Transactions: <transaction number(s) that are mature, for zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs>TRL Date: <maturity date of transaction>Test Run: SelectedConfirm the message Are you sure that you want to select future business transactions by pressing Enter | The Fix and Post Derived Business Transactions screen displays.If the No scheduled derived business transactions were found for the selection message displays, no derived transaction is available for your selection. You can skip the current step. |  |
| 4 | Fix and Post for Test run | Choose Fix. | The Posting Log: Posted Business Transactions screen displays. You can see the simulated posting information for local GAAP (valuation area AE0). There is no posting created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: DeselectConfirm the message Are you sure that you want to select future business transactions by pressing Enter | The Fix and Post Derived Business Transactions screen displays. |  |
| 6 | Fix and Post for Production run | Choose Fix. | The Posting Log: Posted Business Transactions screen displays. You can see the posting information for local GAAP (valuation area AE0). An accounting document is created in the local GAAP (valuation area AE0). |  |

### Foreign Currency Risk Management and Accounting - With Options

Purpose

This section describes creation of a foreign exchange (FX) transactions for hedging and non-hedging purposes, as well as subsequent steps to settle, fix and execute the contract until complete (either receiving or sending the payment). The FX transactions are tightly and automatically integrated with Cash Operations, General Ledger, and Correspondence. Daily reporting functionality is provided for the roles involved in the FX processes.

#### (1XN) Market Rates Management – Manually via Upload

Purpose

This step provides instructions to enter market data such as foreign currency exchange spot rates, swap rates, reference interest rates, and so on.

These data provide default values when creating new transactions, or calculating fair value for existing transactions.

Procedure

For more information, see the Market Rates Management – Manually via Upload (1XN) test script.

#### (1S4) Automatic Market Rates Management

Purpose

This step provides instructions on integrating market data with the data feed via SAP Business Technology Platform (SAP BTP), through manual operation or job scheduling.

Procedure

For more information, see the Automatic Market Rates Management(1S4) test script.

#### Generate Limit Utilizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the end of the transaction day, the Treasury Specialist - Middle Office can run the end-of-day process. The system determines and updates limit utilizations based on the transactions and positions contained in the data pool, and the external transactions that were entered.

|  |
| --- |
| Note You can also schedule a background job for this step. For more information, see the job scheduling step in the Appendix. |

Prerequisite

The market data is imported.

If security exists, the spot price needs to be maintained for current date. Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Specialist - Middle Office | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open End-of-Day Processing (KLNACHT). | The End-of-Day Processing (KLNACHT) screen displays. |  |
| 3 | Enter Criteria of End-of-Day Processing | Enter the following data and choose Execute:Valuation Date: for example, <Current Date>Determination Procedure: for example, <10 to 20>Company Code: for example, 3310 | The system displays the message End-of-day processing was completed successfully. |  |

#### Analyze Liquidity Forecast

Purpose

The cash manager checks the liquidity forecast regularly and makes decisions for medium-term or long-term financial instruments, such as investment, loan, or foreign exchange.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) app to analyze the liquidity forecast. For more information, see the Basic Cash Operations(BFB) test script.

#### Balance Sheet Exposure Management

Purpose

This section describes how to review the balance sheet exposures.

##### Review Balance Sheet FX Risk

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the Balance Sheet FX Risk to grasp the overview status of the balance sheet FX risks.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Review Balance Sheet FX Risk (F1588). | The Review Balance Sheet FX Risk (F1588)screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Display Currency: For example, AEDExchange Rate Type: For example, MKey Date: <Current date> | The Standard sections displays data for all the company codes. |  |
| 4 | Drill Down to One Company Code | In the Company Code column, choose 3310. | The Balance Sheet FX Net Exposures list displays per the definition maintained in Define Key Figures for Balance Sheet FX Risk. |  |

##### Take Snapshot for Balance Sheet FX Risk

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you take snapshot for Balance Sheet FX risk on the Key Date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Take Snapshot - Balance Sheet FX Risk (FXM_SNAP) | The Take Snapshot-Balance Sheet FX Risk screen is displayed. |  |
| 3 | Entering General Information for take a snap shot | Make the following entries and choose Run:In the General area,Snapshot Description: for example: Take Snapshot-Balance Sheet FX RiskCreated in Status: CreatedKey Date Definition: Fixed DateKey Date: for example, <the current date>Reporting Currency: AEDExchange Rate Type: MIn the Filter area,Company Code: 3310Currency: <the risk currency, for example, USD for DE>In the Time Pattern area,Period Definition: for example, <select>Start Date: for example, <the first day of current year>End date: for example, <the last day of current year>Increment: for example, 1Unit: for example, MonthTest Run: <deselect> | The Snapshot Details screen is displayed.Please note down the Snapshot ID for follow-up steps. |  |

##### Check and Process Snapshot Item

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check and edit snapshot item for Balance Sheet FX risk

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Snapshots - Balance Sheet FX Risk(F4763) | The Process Snapshot - Balance Sheet FX Risk screen is displayed |  |
| 3 | Check Snapshot Item | Enter the snapshot ID you noted down in the field Snapshot ID and choose Go.Choose > at the end of the row for the snapshot you just created.In the Snapshot screen, choose > at the end of the row for the snapshot item you want to check the details.Check the snapshot item. | The Snapshot Item screen is displayed. |  |
| 4 | Create a New Snapshot Item (Optional) | Choose Back to go back to the Snapshot screen.Choose Create.In the New Snapshot Item screen, enter the following data and choose Create:Company Code: 3310Amount: for example, 1,000,000 <the risk currency, for example, USD for DE>Period Start: for example, <the first day of current month>Period End: for example, <the last day of current month> | A snapshot item is created, with the Manual flag. |  |
| 5 | Edit a Snapshot Item (Optional) | Choose Edit, change the data, for example change the Amount to 2,000,000 and choose Save. | Your changes are saved. |  |

##### Release Snapshot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you release the updated snapshot for Balance Sheet FX risk.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Snapshots - Balance Sheet FX Risk (F4763) | The Process Snapshot - Balance Sheet FX Risk screen is displayed. |  |
| 3 | Release a Snapshot | Select the snapshot you just edited and choose ReleaseChoose OK in the dialog box. | The snapshot is released. |  |

##### Review Balance Sheet FX Risk Based on Snapshot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can view the balance sheet FX Risk based on snapshot.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Balance Sheet FX Risk Overview - Based on Snapshots (F4765). | The Balance Sheet FX Risk Overview-Based on Snapshots screen is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Go:Display Currency: For example, AEDExchange Rate Type: For example, M | The Net Open Amount Overview chart is displayed as default. |  |
| 4 | Change View | Choose Chart and Table view | The Hedging Detail table displayed below the chart. |  |
| 5 | Drill Down to One Snapshot | In the Snapshot ID column, choose the snapshot ID you noted down | Hedging details of the snapshot is displayed.Because there is no hedge request from this snapshot ID yet, there is just Key Figure Type of Net Exposure of Snapshot. |  |

#### Cash Flow Exposure Management

Purpose

This section describes how to enter cash flow exposure based on some exposure data from an external system.

##### Collect Exposure Data

Purpose

Users collect exposure data from various teams and departments to generate a collection of exposures to enter into the SAP system.

This step is done outside of the SAP system.

##### Create Raw Exposure

Purpose

You have two options to create raw exposure depending on different Data Source of Filters for Exposures when define Hedging Area:

- Create Raw Exposure using Exposure Management 2.0.
- Create Raw Exposure using FX Exposure Management.

###### Create Raw Exposure using Exposure Management 2.0

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a raw exposure in the SAP system based on data obtained from external data source.

Prerequisites

A specific data format is required for Option 2: Import the raw exposures from spreadsheet. For more information on template file generation, see Description on the Template for Import Raw Exposures and Sample Data for Import Raw Exposures in the Appendix.

You have defined Raw Exposure for E_EM2 as data source (Exposure Management 2.0) when define hedging area.

Procedure

Option 1: Create the raw exposure manually.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Raw Exposure (FTREX1). | The Raw Exposure: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Create:Exposure Activity Type: For example, YFXO | The Raw Exposure Maintenance: Create screen displays. |  |
| 4 | Enter Header Data | On the Header Data tab, make the following entries:Ext. Doc. No.: For example, <Current date>001Default Exposure Category: For example, 01Company Code: 3310Crit4ExpPosType: FXDirection: For example, OUT | The screen switches to Line Item Data tab. |  |
| 5 | Line Item Data | Choose the Line Item Data tab. |  |  |
| 6 | New Line Item | Choose Create New Line Item. |  |  |
| 7 | Enter Line Item Data | Make the following entries and choose Save:Ext ItemNo: For example, 1001ExpDueDte: For example, <Current date + 3 Months>Exposure Amount: For example, 100,000,000.00ExpAmtCrcy: USDTargetCrcy: AEDNote If you chose Currency Defined by the Source in [Define Hedging Area](#unique_21) [page ] 30, you can maintain target currency as risk free currency other than company code currency. | The Messages dialog box displays messages indicating successful release, creation, and saving. |  |

Option 2: Import the raw exposures from spreadsheet.

|  |
| --- |
| Note You may encounter an issue if your browser is in private browsing mode. Switch to regular mode to execute following steps. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Import Raw Exposures - Spreadsheet (FTREX_EXCEL_UPLOAD). | The Excel Upload Raw Exposure screen displays. |  |
| 3 | Upload Local File to Device | Choose Local File for Upload/Download.Note If your browser displays the message Store files on this device, choose Allow to proceed. | The Select Exposure File screen displays. |  |
| 4 | Import from native file system | Choose Import from native file system. Select the template file from the local file system and choose Open.Note The template must be in a specific format. For more information on the file format, see the Description on the Template for Import Raw Exposures section in the Appendix.Note The file must have the .xlsx extension.Note Some sample data is provided in the Appendix in the Sample Data for Import Raw Exposures topic.The following steps assume you use the sample data provided in the Appendix. | After import, an Information dialog box displays the message Import finished. Number of imported files:1 |  |
| 5 | OK | Choose OK | The Select Exposure File dialog displays the exposure file. |  |
| 6 | Choose Exposure File to Import and Execute | Select the exposure file and choose the Choose button. | The file path in the File name field displays in the Excel Upload Raw Exposure screen. |  |
| 7 | Test Run the Import | Make the following entries and choose Execute:Display data before processing: SelectedTest Run: Selected | The Exposure Upload Data - Simulation screen displays. |  |
| 8 | Confirm Test Run Result | Review the exposure data. Once you confirm it, chooseExecute. | The Status column displays on the left. Successful records are marked with traffic light symbol. |  |
| 9 | Production Run the Import | Choose Exit. | The Select Exposure File screen displays. |  |
| 10 |  | Make the following entries and choose Execute:Test Run: Deselected | The Exposure Upload Data screen displays the imported data. |  |
| 11 | Production Run and Review the Import Result | Choose Execute. | The Exposure Upload screen displays with import results in it.Successfully imported records are indicated by green traffic light symbols and values in Raw Exposure ID. |  |

###### Create Raw Exposure using FX Exposure Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a raw exposure in the SAP system using FX Exposure Management. FX Exposure Management allows customers to intuitively administer FX Exposures tailored to Hedge Management Use Cases.

Prerequisites

You have defined E_FXEM as data source (FX Exposure Management) when define hedging area.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage FX Exposures (F7990). | The Manage FX Exposures screen displays. |  |
| 3 | Create FX Exposure | Choose Create. | The New: FX Exposure screen displays. |  |
| 4 | Enter Header Data | On the Header Data tab, make the following entries:FX Exposure Type: For example, SFXDue Date: For example, <Current date + 3 Months>Company Code: 3310 | The screen switches to FX Exposure Details tab. |  |
| 5 | Enter FX Exposure Details | On the FX Exposure Details tab, make the following entries:Direction: For example, IncomingTarget Currency: For example, <MD risk currency>Amount: For example, 100,000,000.00 <MD CC currency>Valid From: For example, <Current date>Choose Create. | The status change history displays status Created with date and time. |  |
| 6 | Submit FX Exposure | Choose Submit for Release. | The Messages dialog box displays messages indicating FX exposure submitted. |  |
| 7 | Sign Out |  |  |  |
| 8 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 9 | Access the SAP Fiori App | Open Manage FX Exposures (F7990). | The Manage FX Exposures screen displays. |  |
| 10 | Release FX Exposure | Choose Go to display all FX exposures.Choose the FX exposure created and submitted in previous steps and choose Release. | The Messages dialog box displays messages indicating FX exposure released. |  |

##### Take Snapshot for Cash Flow Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Take snapshot for cash flow exposure on the Key Date.

Prerequisites

A Hedging Area exists. To create a Hedging Area, see the previous Define Hedging Area procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Take a Snapshot | Open Take Snapshot (TOESNAP). | The Take Snapshot screen is displayed. |  |
| 3 | Enter General Selections | On the General Selections tab, make the following entries and choose Run:Hedging Area: For example, AE0001Description: For example, <Current date> snapshotExtraction Date: for example , <the current date>Note You can also take a snapshot with extraction date in the past when there is no snapshot taken for the hedge area. Please note that you can only take a snapshot with extraction date in the past for one time.Day Reference: <select this checkbox>Note The Day Reference checkbox must be selected if you want to perform the Generate Hedge Request operation.When you set Reset Target Quota indicator, manually overwritten target quotas in Hedge Management Cockpit are reset to the target quotas originally defined in your hedging area, which are used with the new snapshot date. | A log is displayed with a notification that the snapshot is successfully created. |  |

##### Review Cash Flow Net Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the cash flow net exposure in the Hedge Management Cockpit.

Prerequisites

A Hedging Area exists. To create a Hedging Area, see the previous Define Hedging Area procedure.

A snapshot on the Key Date exists.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Hedge Management Cockpit (TOENE). | The Hedge Management Cockpit view is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entry, and choose Start:Hedging Area: For example, AE0001Layout ID： 1R_ALL_CH | The Hedge Management Cockpit for Hedging AreaAE0001 displays with the exposure data.Note If you choose Currency Defined by the Source and exposure items are created based on the cross-currency exposures during snapshot, the hedge management cockpit displays the Target Currency, Risk Currency and Company Code Currency |  |

#### Analyze Exposure and Agree on Hedging Actions

Purpose

Analyze the exposure data with related teams and organizations and agree on hedging actions. This step is performed outside of the SAP system.

#### Create Trade Request

Purpose

You have three options to create trade requests:

- Create Trade Request via Balance Sheet Exposure Hedge Request
- Create Trade Request via Cash Flow Hedge Request
- [Create Trade Request Manually](#unique_76) [page ] 138

##### Create Trade Request via Balance Sheet Exposure Hedge Request

###### Generate Hedge Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you generate a balance sheet foreign exchange (FX) hedge request.

Prerequisites

You have taken and released a snapshot as described in the [Balance Sheet Exposure Management](#unique_129) [page ] 118 section.

Procedure

Option 1: Generate Hedge Request without Predefined Parameters

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Generate Hedge Request - Balance Sheet FX Risk (FXM_REQUEST). | The Generate Balance Sheet Exposure Hedge Requests screen is displayed. |  |
| 3 | Enter General Information for Generate Balance Sheet Exposure Hedge Requests | Make the following entries and choose Run:In the Snapshot area,Selection by Snapshot ID: for example, <select>Snapshot ID: for example, <the ID you noted down in step Take Snapshot for Balance Sheet FX Risk>Note Please make sure to use the same snapshot ID in taking snapshot.In the Filter for Snapshot areaCompany Code: 3310Currency: <the risk currency, for example, USD>In the Value Date area,Fixed Date: <select>Value Date Selection: Current Month EndIn the Main Parameter area,Instrument Category: FX OptionTarget Status: CreatedTest Run: <deselect> | The Balance Sheet Exposure Hedge Request List is displayed. |  |

Option 2 Generate Hedge Request with Predefined Parameters

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Hedge Requests-Balance Sheet FX Risk (F4764). | The Balance Sheet Exposure Hedge Request screen is displayed. |  |
| 3 | Enter General Information for Generate Balance Sheet Exposure Hedge Requests | Choose Create.In the dialog box, make the following entries and choose Create:Snapshot ID: for example, <the snapshot ID you noted down>Note Please make sure to use the same snapshot ID in taking snapshot.Request Parameter Group: for example, RP_GRP2 | The Balance Sheet Exposure Hedge Request List is displayed with new created hedge request(s). |  |

###### Check and Process Hedge Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check and process a balance sheet foreign exchange (FX) hedge request.

Prerequisite

A balance sheet foreign exchange (FX) hedge request is created and available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Hedge Requests-Balance Sheet FX Risk (F4764). | The Balance Sheet Exposure Hedge Request screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Go:Company Code: for example, 3310 | Balance sheet exposure hedge requests that match the filter criteria are displayed. |  |
| 4 | Check the Request | Select the row of the Hedge Request you just created and choose > at the end of the row. | The Hedge Request screen is displayed. |  |
| 5 | Edit the Request (Optional) | Choose Edit, change the data, for example, change the Amount to 80% of the original amount, and choose Save. | Your changes are saved. |  |

###### Release Hedge Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release a balance sheet foreign exchange (FX) hedge request.

Prerequisites

A balance sheet foreign exchange (FX) hedge request is created and available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Hedge Requests-Balance Sheet FX Risk (F4764). | The Balance Sheet Exposure Hedge Request screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Go:Company Code: for example, 3310 | Balance sheet exposure hedge requests that match the filter criteria are displayed. |  |
| 4 | Release the Request | Select the row of the Hedge Request you just edited and choose Release.Choose OK in the dialog box. | The balance sheet exposure hedge request is released successfully. |  |

##### Create Trade Request via Cash Flow Exposure Hedge Request

###### Generate Hedge Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you generate a cash flow foreign exchange hedge request.

Prerequisites

You have taken a snapshot with Day Reference as described in the [Take Snapshot for Cash Flow Exposure](#unique_38) [page ] 62 step.

Procedure

Table 9: Generate Hedge Request Manually

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Hedge Management Cockpit (TOENE). |  |  |
| 3 | Manage Layouts | Choose Manage Layouts. | The Layout Overview screen displayed. |  |
| 4 | Create Your Own Lay-out | Select a row of default Layout ID, for example, 1R_ALL_CH and choose Create with template | The New Layout ID screen is displayed |  |
| 5 | Enter Layout ID | Enter the following data and choose Enter:Layout ID: for example, 2R_TQ_CH | The Layout screen is displayed |  |
| 6 | Choose Key Figures for new Layout | Make the following entries, choose Save, and then choose Back.Description: for example, With Target Quota (Key Figures in Rows)Target Quota Type: for example, YLQOn the Key Figure tab, enter the following data and choose Save:Amount to Hedge: Display Level, for example, 1; Order, For example, 8Target Quota [%]: Display Level, For example, 1; Order, For example, 9Upper Target Quota [%]: Display Level, For example, 1; Order, For example, 10Lower Target Quota [%]: Display Level, For example, 1; Order, For example, 11 |  |  |
| 7 | Enter Selection Criteria | Make the following entries:Hedging Area: For example, AE0001Layout ID： 2R_TQ_CHand choose Start. | The Hedge Management Cockpit for Hedging Area AE0001 is displayed with the exposure data and target quota in it.Note You could overwrite target quota by selecting a target quota cell and clicking on Overwrite Target Quota.The overwritten target quota shall be applied to calculated key figures which are depending on the target quota, for example, Target Hdg Amt and Amount to Hedge. |  |
| 8 | Generate Hedge Request | Select a row.For example, select a row that includes Net Hedges in the Key Figure Name column with a current date value for + 3 months.Choose Hedge Request and then FX Hedge Request. | The Hedge Request view is displayed. |  |
| 9 | Save Hedge Request | Make the following entries:Hedge Request ID: For example, FX hedgeInstrument Cat.: For example, FX OptionHedging Classificatn: For example, Y0Value Date: For example, <current date + 3 months>Hedge Request Amount: For example, + 1,000,000and choose Save. |  |  |

Table 10: Generate Hedge Request Automatically

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Generate Hedge Request Automatically | Choose Automated Request CreationCheck the row of Hedge request can be created and modify the following default entries if necessary and choose Save:AmountHedge Request Value DateInstrument Category.Note you must make the key figure Amount to Hedge available in your chosen layout. | The Hedge Request with group ID were saved message is displayed. |  |

###### Release Hedge Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to release an foreign exchange (FX) hedge request.

Prerequisites

An FX trade request is created and available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO). | The Process Hedge Requests view is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data:Company Code: for example, 3310and choose Start. | The system displays the hedge requests that match the filter criteria. |  |
| 4 | Submit the Request | Select the row of the Hedge Request and choose Process and then select Submit from the dropdown list. | Log displays that the hedge request was submitted. |  |
| 5 | Release the Request | Select the row of the Hedge Request and choose Process and then select Release from the dropdown list. | Log displays that the hedge request was released. |  |
| 6 | Perform the Get Operation in the SAP Business Technology Platform (SAP BTP) App | Perform the Get operation in accordance with the instructions in the Treasury Trading via Trading Platforms(2F5) test script. | The Get operation completes successfully. |  |

##### Create Trade Request Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create trade request manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Trade Requests (TPITRO). | The Process Trade Requests view displays. |  |
| 3 | Create Manual Trade Request | Choose Create Trade Request.In the General tab, enter the following data and Save:Company Code: for example,3310Instrument Cat.: for example, FX OptionBuy/Sell: for example, BuyPut/Call: for example, CallRequested Amount: for example, 10,000USDOpposite Currency: for example, AEDValue Date: for example, <current date 3 months> | The Trade Request - Display view displays. |  |
| 4 | Submit the Request | Select the row of the Trade Request and choose Process and then select Submit from the dropdown list |  |  |
| 5 | Release the Request | Select the row of the Trade Request and choose Process and then select Release from the dropdown list. | The status of the trade request changes to In Transfer |  |
| 6 | Confirm Update Status | Check the status of the trade request.Note A trade request with status In Transfer is automatically transferred to TPI and status changes to In Process once successfully receive the trade request. | The status of the trade request changes to In Process. |  |

#### Check Trade Request Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the status of all trade requests.

Prerequisites

There are foreign exchange trade requests created and released to make the trade requests available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Requests (TPITRO). | The Process Trade Requests view is displayed. |  |
| 3 | Enter Selection Criteria | Check the settings of the check boxes on the Selection screen and press Start. | The system displays the trade requests that match the filter criteria. |  |
| 4 | Check the Originating Request | Select the row of a Trade Request and choose Originating Request. | The Trade Request - Display view is displayed. |  |
| 5 | Check the Request | Choose Change and then choose Check | Log displays that the trade request is consistent. |  |

#### Check Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes how to check the limit utilization report.

Prerequisites

The limit master records of your company are maintained in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Execute:Limit Type: for example, Y01 or Y07Limit Utilization Base: for example, 1Determination Date: for example, <the current date>Limits Valid From: for example, <the current date> | An overview of the limit utilization in accordance with your selection criteria is displayed. |  |

#### Create FX Option Contract

Purpose

In this step, you create FX option contract (plain vanilla FX option, or zero/low cost collar FX option) as hedging instruments.

##### Create Plain Vanilla FX Option

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the foreign exchange option contracts for those foreign exchange hedging activities. In addition, foreign exchange option contracts can also be created for non-hedging contexts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create OTC Option (TI71). | The Create OTC Option: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and press Enter:Company Code: for example, 3310Product Type: 76ATransaction Type: for example, 100Partner: for example,33537001 | The OTC Option: Create Contract: Structure screen displays. |  |
| 4 | Enter Structure | Enter the following data and choose the Administration tab.Expiry Date: for example, ++6 (6 months later)Exercise Type: for example, EuropeanSettlement: for example, Physical ExerciseStrike: for example, AED/USD<enter a proper rate>Put/Call: for example, CallTraded Amt: for example, USD 5MUnder the Premium section, enter the following data:Notation: for example, PercentagePercentage: for example, 8Flow Type: for example, 1300 Optional Premium - Profit/LossCurrency: for example, AEDNote You can define the currency pair not pre-delivered via configuration step Define Leading Currency.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |  |  |
| 5 | Enter Administration Data | Enter the following data and choose Save:Risk Mitigation: For example, <deselect>Hedging Classification: For example, Y0 | The data is saved and the transaction number is generated. |  |

##### Create Zero/Low Cost Collar FX Option

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a zero/low cost collar FX option (cylinder option).

There are two alternatives to manually create zero/low cost collar FX option:

Option 1: Create Two Options Separately and Create Option Reference. You create a FX option (long leg), and create another FX option (short leg), and then create the reference for these two legs and become the zero/low cost collar FX option.

- Option 2: Create Zero/Low Cost Collar FX Option in Single Step. The two legs and the reference are saved at the same time.

No matter which option you choose, the following attributes are necessary to be identical in both FX option transactions (two legs):

- Company code
- Product type
- Business partner
- Expiry Date
- Expiry Time
- Risk currency, risk amount
- Premium payment date, premium currency
- Contract date
- Hedging classification

###### Option 1: Create Two Options Separately and Create Option Reference

Procedure

Purchase a Call/Put FX Option (Long Leg):

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create OTC Option (TI71). | The Create OTC Option: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Create OTC Option: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: 76ATransaction Type: 100Partner: for example, 33537001 | The OTC Option: Create Contract: Structure screen displays. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Sub-area Option:Expiry Date: for example, <Current date + 2 Months>Exercise Type: for example, EuropeanSettlement: for example, Physical ExerciseStrike:Risk Currency/Local Currency Rate, for example, USD/AED<enter the strike rate>Put/Call: for example, CallTraded Amt: <Risk Currency><Amount>, for example, USD500000Value Date: for example, <Current date + 2 Months + 2 days>Sub-area Premium:Flow Type: for example, 1300 Option Premium - Profit/LossPayment Date: <Current date + 2 days>Amount: <local currency> <your option premium amount>, for example, AED500Sub-area Contract Conclusion:Contract Date: for example, <current date>Note The Expiry Date of FX option should be within the same period as the due date of exposure.you long call option in cylinder option if it is outgoing exposure.You long put option in cylinder option if it is incoming exposure,The currency of Traded Amt should be the risk currency. The amount of Traded Amt should be less or equal to the amount of Net Open Exposure.If the currency pair is not defined, you can define the currency pair via configuration step Define Leading Currency.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | Data on tab Structure has been entered. |  |
| 5 | Enter Data in Administration tab | Choose tab Administr., and enter the following data:Gen. Valn Class: for example, 43 DerivativesHdg Classific.: for example, Y0 | Data on tab Administr. has been entered. |  |
| 6 | Save the OTC FX Option (Long Leg) | Choose Save. | If dialog box Document lines: Display messages displays, make sure no error message is there (otherwise please correct data and save again), and choose Continue (Enter).Message Financial transaction saved under number displays.Note down the transaction number of this long leg. |  |

Sell a Put/Call FX Option (Short Leg):

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create OTC Option (TI71). | The Create OTC Option: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Create OTC Option: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: 76ATransaction Type: 200Partner: for example, 33537001 | The OTC Option: Create Contract: Structure screen displays. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Sub-area Option:Expiry Date: for example, <Current date + 2 Months>Exercise Type: for example, EuropeanSettlement: for example, Physical ExerciseStrike:Risk Currency/Local Currency Rate, for example, USD/AED<enter the strike rate>Put/Call: for example, PutTraded Amt: <Risk Currency> <Amount>, for example, USD500000Value Date: for example, <Current date + 2 Months + 2 days>Sub-area Premium:Flow Type: for example, 1300 Option Premium - Profit/LossPayment Date: <Current date + 2 days>Amount: <local currency> <your option premium amount>, for example, AED500Sub-area Contract Conclusion:Contract Date: for example, <current date>Note The Expiry Date of FX option should be within the same period as the due date of exposure.Note You short call option in cylinder option if it is incoming exposure.You short put option in cylinder option if it is outgoing exposure.Note The currency of Traded Amt should be the risk currency. The amount of Traded Amt should be less or equal to the amount of Net Open Exposure. | Data on tab Structure has been entered. |  |
| 5 | Enter Data in Administration tab | Choose tab Administr., and enter the following data:Gen. Valn Class: for example, 43 DerivativesHdg Classific.: for example, Y0 | Data on tab Administr. has been entered. |  |
| 6 | Save the OTC FX Option (Short Leg) | Choose Save. | If dialog box Document lines: Display messages displays, make sure no error message is there (otherwise please correct data and save again), and choose Continue (Enter).Message Financial transaction saved under number displays.Note down the transaction number of this short leg. |  |

Create Option Reference:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create Reference (TBR6). | The Create Reference: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Create Reference: Initial Screen, enter the following data:Reference Category: OPTSub-area Object 1 to Be Linked:Company Code: for example, 3310Transaction: <The transaction number of the long leg>Sub-area Object 2 to Be Linked:Company Code: for example, 3310Transaction: <The transaction number of the short leg>Choose Enter. | The Create Reference: Data screen displays. |  |
| 4 | Save Reference | On the Create Reference: Data screen, choose Save, | Massage Reference number created displays. |  |

###### Option 2: Create Zero/Low Cost Collar FX Option in Single Step

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Collar FX Option (TI4B). | The Create Option Entry - Spread: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Create Option Entry - Spread: Initial Screen, enter the following data:Company Code: for example, 3310Partner: for example, 33537001Sub-area First Transaction:Product Type: 76ATransaction Type: 100Sub-area Second Transaction:Product Type: 76ATransaction Type: 200Choose Enter. | The Currency Option Entry - Spread: Structure screen displays. |  |
| 4 | Enter Data for 1st Transaction (Long Leg) | On the Currency Option Entry - Spread: Structure screen, enter the following data in area 1st Transaction:Sub-area Option:Exercise Type: for example, EuropeanSettlement: for example, Physical ExerciseExpiry Date: for example, <Current date + 2 Months>Strike:Risk Currency/Local Currency Rate, for example, USD/AED<enter the strike rate>Put/Call: for example, CallTraded Amt: <Risk Currency> <Amount>, for example, USD500000Value Date: for example, <Current date + 2 Months + 2 days>Sub-area Premium:Flow Type: for example, 1300 Option Premium - Profit/LossPayment Date: <Current date + 2 days>Amount: <local currency> <your option premium amount>, for example, AED500Gen. Valn Class: for example, 43 DerivativesHdg Class.: for example, Y0Choose Enter.Note The Expiry Date of FX option should be within the same period as the due date of exposure.You long put option in cylinder option if it is incoming exposure,you long call option in cylinder option if it is outgoing exposure.The currency of Traded Amt should be the risk currency. The amount of Traded Amt should be less or equal to the amount of Net Open Exposure.If the currency pair is not defined, you can define the currency pair via configuration step Define Leading Currency.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | Data for 1st Transaction (long leg) has been entered. |  |
| 5 | Enter Data for 2nd Transaction (Short Leg) | Enter the following data in area 2nd Transaction:Sub-area Option:Exercise Type: <it is automatically copied from 1st transaction>Settlement: <it is automatically copied from 1st transaction>Expiry Date: <it is automatically copied from 1st transaction>Expiry Time: <it is automatically copied from 1st transaction>Strike: currency pair is automatically copied from 1st transaction. You only need to enter a proper exchange ratePut/Call: it is automatically derived from 1st transaction; if it is Call for 1st transaction, it should be Put for the 2nd transaction.Traded Amt: currency and amount are automatically copied from 1st transactionValue Date: <it is automatically copied from 1st transaction>Sub-area Premium:Flow Type: for example, 1300 Option Premium - Profit/LossPayment Date: Current date + 2 daysAmount: <local currency> <your option premium amount>, for example, AED500Gen. Valn Class: for example, 43 DerivativesHdg Class.: for example, Y0Choose Enter.Note You short call option in cylinder option if it is incoming exposure.You short put option in cylinder option if it is outgoing exposure. | Data for 2nd Transaction (short leg) has been entered. |  |
| 6 | Enter Contract Conclusion Data | In sub-area Contract Conclusion, enter the following data:Contract Date: for example, <current date> | Contract date has been entered. |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Table (Without Options) lists the app for Take Snapshot for Balance Sheet FX Risk as FXM_REQUEST, while the test procedure uses Take Snapshot - Balance Sheet FX Risk (FXM_SNAP).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-foreign-currency-risk-management-1x1-ae-sap-s-4hana-cloud-part-02]]
- related-to :: [[05-treasury-and-cash-management/foreign-currency-risk-management-group-ledger-ifrs-1x9-ae-777]]
- related-to :: [[05-treasury-and-cash-management/foreign-currency-risk-management-group-ledger-us-gaap-34d-ae-908]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1X1_S4CLD2608_BPD_EN_AE.docx` — lines 1–3641 of the extracted text · extracted with `mammoth` · 475,815 chars in the whole document
