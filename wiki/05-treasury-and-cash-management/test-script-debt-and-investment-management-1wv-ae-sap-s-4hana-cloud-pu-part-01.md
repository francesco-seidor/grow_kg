---
id: 05-treasury-and-cash-management/test-script-debt-and-investment-management-1wv-ae-sap-s-4hana-cloud-pu-part-01
title: "Test Script: Debt and Investment Management (1WV_AE) - SAP S/4HANA Cloud Public Edition (1WV_S4CLD2608_BPD_EN_AE) — part 1 of 2"
description: "Test script for SAP S/4HANA Cloud Public Edition 2608 (AE) scope item 1WV Debt and Investment Management: prerequisites, test steps, reports, jobs."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/debt-and-investment-management]
aliases: []
keywords: [Debt and Investment Management, counterparty business partner, correspondence, credit limits, credit facilities, money market transactions, interest rate instruments, payment requests, general ledger posting, period-end closing]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WV_S4CLD2608_BPD_EN_AE.docx#lines-1-3001"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-773
topic: 05-treasury-and-cash-management/debt-and-investment-management
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Debt and Investment Management (1WV_AE) - SAP S/4HANA Cloud Public Edition (1WV_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WV_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–3001 of the extracted text), extracted with `mammoth`. Grouped under **Debt and Investment Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Debt and Investment Management (1WV_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 7](#_Toc232847903)

[2 Prerequisites 8](#_Toc232847904)

[2.1 System Access 8](#_Toc232847905)

[2.2 Roles 8](#_Toc232847906)

[2.3 Master Data, Organizational Data, and Other Data 9](#_Toc232847907)

[2.4 Business Conditions 10](#_Toc232847908)

[2.5 Preliminary Steps 11](#_Toc232847909)

[2.5.1 Create Business Partner 11](#_Toc232847910)

[2.5.1.1 Maintain General Data for Business Partner 11](#_Toc232847911)

[2.5.1.2 Maintain Payment Details for Business Partner 13](#_Toc232847912)

[2.5.1.3 Maintain Authorizations for Business Partner 16](#_Toc232847913)

[2.5.1.4 Maintain Reporting Data in Company Code for Business Partner 17](#_Toc232847914)

[2.5.1.5 Maintain Derived Flows for Business Partner (Optional) 18](#_Toc232847915)

[2.5.2 Correspondence 19](#_Toc232847916)

[2.5.2.1 Maintain Profile and BP Group Assignments to External Recipient 20](#_Toc232847917)

[2.5.2.2 Maintain Profile and BP Group Assignments to Internal Recipient 21](#_Toc232847918)

[2.5.3 Maintaining Credit Limit 23](#_Toc232847919)

[2.5.3.1 Maintain Limit with Limit Type Y01 23](#_Toc232847920)

[2.5.3.2 Maintain Limit with Limit Type Y07 24](#_Toc232847921)

[2.5.4 Maintain Trader and Trader Authorizations 25](#_Toc232847922)

[2.5.4.1 Define Traders 25](#_Toc232847923)

[2.5.4.2 Define User Data 26](#_Toc232847924)

[2.5.4.3 Maintain Trader Authorizations 27](#_Toc232847925)

[3 Overview Table 29](#_Toc232847926)

[4 Test Procedures 35](#_Toc232847927)

[4.1 (1XN) Market Rates Management – Manually via Upload 35](#_Toc232847928)

[4.2 Generate Limit Utilization 35](#_Toc232847929)

[4.3 Analyze Cash Position 36](#_Toc232847930)

[4.4 Analyze Liquidity Forecast 37](#_Toc232847931)

[4.5 Check Credit Line Limit (Optional) 37](#_Toc232847932)

[4.6 Create Facility (Optional) 38](#_Toc232847933)

[4.7 Settle Facility (Optional) 42](#_Toc232847934)

[4.8 Check Facilities Utilization (Optional) 43](#_Toc232847935)

[4.9 Check Limit Utilization Report 44](#_Toc232847936)

[4.10 Review Money Market Trade Request Status 45](#_Toc232847937)

[4.11 Create Debt or Investment Contract 46](#_Toc232847938)

[4.11.1 Create Fixed Term Deposit 46](#_Toc232847939)

[4.11.2 Create Deposit at Notice 48](#_Toc232847940)

[4.11.3 Create Commercial Paper 49](#_Toc232847941)

[4.11.4 Create Cash Flow Transaction 51](#_Toc232847942)

[4.11.5 Create IR Instrument 53](#_Toc232847943)

[4.11.6 Drawdown on Facilities 59](#_Toc232847944)

[4.11.7 Create Current Acct-Style Instrument 61](#_Toc232847945)

[4.12 (BFB) Basic Cash Operations 63](#_Toc232847946)

[4.13 (J78) Advanced Cash Operations 64](#_Toc232847947)

[4.14 Correspondence 64](#_Toc232847948)

[4.14.1 Set Settlement Status (Manual) 65](#_Toc232847949)

[4.14.2 Correspondence with PDF Form 66](#_Toc232847950)

[4.14.2.1 Send Confirmation Email/Print 67](#_Toc232847951)

[4.14.2.2 Check Correspondence Status 67](#_Toc232847952)

[4.14.2.3 Receive Incoming Confirmation 69](#_Toc232847953)

[4.14.2.4 Find Deal and Match Deal Details 69](#_Toc232847954)

[4.14.2.5 Set Settlement Status 71](#_Toc232847955)

[4.15 Principal Payment 72](#_Toc232847956)

[4.15.1 Corporate Initiated Payment 72](#_Toc232847957)

[4.15.1.1 Option 1: Generate and Automatically Process Payment Request 72](#_Toc232847958)

[4.15.1.2 Option 2: Generate and Process Payment Request 76](#_Toc232847959)

[4.15.1.2.1 Generate Payment Request 76](#_Toc232847960)

[4.15.1.2.2 Process Payment Request 78](#_Toc232847961)

[4.15.1.3 Send Payment Medium File 80](#_Toc232847962)

[4.15.2 Bank Initiated Payment 81](#_Toc232847963)

[4.15.3 Post to General Ledger 81](#_Toc232847964)

[4.16 Period-end Closing 83](#_Toc232847965)

[4.16.1 Run Accrual 84](#_Toc232847966)

[4.16.2 Calculate or Maintain Fair Value of Transaction 85](#_Toc232847967)

[4.16.3 Perform Key Date Valuation 88](#_Toc232847968)

[4.17 Interest Rate Adjustment 90](#_Toc232847969)

[4.17.1 Interest Rate Adjustment Schedule Report 90](#_Toc232847970)

[4.17.2 Adjust Interest Rate 91](#_Toc232847971)

[4.18 Update Price Index Value 93](#_Toc232847972)

[4.19 Interest Payment 94](#_Toc232847973)

[4.19.1 Display Payment Schedule 94](#_Toc232847974)

[4.19.2 Corporate Initiated Payment 95](#_Toc232847975)

[4.19.2.1 Option 1: Generate and Automatically Process Payment Request 95](#_Toc232847976)

[4.19.2.2 Option 2: Generate and Process Payment Request 99](#_Toc232847977)

[4.19.2.2.1 Generate Payment Request 99](#_Toc232847978)

[4.19.2.2.2 Process Payment Request 101](#_Toc232847979)

[4.19.2.3 Send Payment Medium File 103](#_Toc232847980)

[4.19.3 Bank Initiated Payment 104](#_Toc232847981)

[4.19.4 Post to General Ledger 104](#_Toc232847982)

[4.20 Nominal Amount Adjustment 106](#_Toc232847983)

[4.20.1 Adjust Nominal Amount 106](#_Toc232847984)

[4.20.2 Corporate Initiated Payment 108](#_Toc232847985)

[4.20.2.1 Option 1: Generate and Automatically Process Payment Request 108](#_Toc232847986)

[4.20.2.2 Option 2: Generate and Process Payment Request 112](#_Toc232847987)

[4.20.2.2.1 Generate Payment Request 112](#_Toc232847988)

[4.20.2.2.2 Process Payment Request 112](#_Toc232847989)

[4.20.2.3 Send Payment Medium File 112](#_Toc232847990)

[4.20.3 Bank Initiated Payment 113](#_Toc232847991)

[4.20.4 Post to General Ledger 113](#_Toc232847992)

[4.21 Reclassification 114](#_Toc232847993)

[4.21.1 Display Maturity Statistics 114](#_Toc232847994)

[4.21.2 Reclassify from Long Term to Short Term (Valuation Class Transfer) 115](#_Toc232847995)

[4.22 Terminate Deposit at Notice 116](#_Toc232847996)

[4.22.1 Give Notice to Deposit at Notice 116](#_Toc232847997)

[4.23 Transaction is Premature 117](#_Toc232847998)

[4.23.1 Maintain Early Repayment for Premature Transaction 118](#_Toc232847999)

[4.23.2 Corporate Initiated Payment 119](#_Toc232848000)

[4.23.2.1 Option 1: Generate and Automatically Process Payment Request 119](#_Toc232848001)

[4.23.2.2 Option 2: Generate and Process Payment Request 123](#_Toc232848002)

[4.23.2.2.1 Generate Payment Request 123](#_Toc232848003)

[4.23.2.2.2 Process Payment Request 125](#_Toc232848004)

[4.23.2.3 Send Payment Medium File 127](#_Toc232848005)

[4.23.3 Bank Initiated Payment 128](#_Toc232848006)

[4.23.4 Post to General Ledger 128](#_Toc232848007)

[4.23.5 Post Realized Profit and Loss 130](#_Toc232848008)

[4.24 Transaction is Mature 132](#_Toc232848009)

[4.24.1 Corporate Initiated Payment 132](#_Toc232848010)

[4.24.1.1 Option 1: Generate and Automatically Process Payment Request 132](#_Toc232848011)

[4.24.1.2 Option 2: Generate and Process Payment Request 136](#_Toc232848012)

[4.24.1.2.1 Generate Payment Request 136](#_Toc232848013)

[4.24.1.2.2 Process Payment Request 138](#_Toc232848014)

[4.24.1.3 Send Payment Medium File 140](#_Toc232848015)

[4.24.2 Bank Initiated Payment 141](#_Toc232848016)

[4.24.3 Post to General Ledger 141](#_Toc232848017)

[4.24.4 Post Realized Profit and Loss 143](#_Toc232848018)

[4.25 Reports 145](#_Toc232848019)

[4.25.1 Display Treasury Posting Journal 145](#_Toc232848020)

[4.25.2 Treasury Position Analysis 145](#_Toc232848021)

[4.25.3 Treasury Position History 146](#_Toc232848022)

[4.25.4 Display Treasury Position Values 147](#_Toc232848023)

[4.25.5 Define Financial Positions 148](#_Toc232848024)

[4.25.6 Financial Status (Book Value) 151](#_Toc232848025)

[4.25.7 Financial Status (Nominal Amount) 152](#_Toc232848026)

[4.25.8 Display Treasury Payments 153](#_Toc232848027)

[4.25.9 Display Treasury Position Flows 153](#_Toc232848028)

[4.25.10 Display Treasury Alerts - Posting 154](#_Toc232848029)

[4.25.11 Display Treasury Alerts- Settlement, Release, Payment, Correspondence and Interest Rates 155](#_Toc232848030)

[4.25.12 Display Payment Schedules 156](#_Toc232848031)

[4.25.13 Analyze Net Present Value (NPV) 157](#_Toc232848032)

[4.25.14 Calculate Market Risk Key Figures 158](#_Toc232848033)

[4.25.15 Sensitivity Key Figures 159](#_Toc232848034)

[4.25.16 Review Limit Utilization Report 160](#_Toc232848035)

[4.25.17 Review Maturity Profile 161](#_Toc232848036)

[4.25.18 Review Interest Rate Overview 162](#_Toc232848037)

[4.25.19 Debt and Investment Analysis 163](#_Toc232848038)

[5 Appendix 165](#_Toc232848039)

[5.1 Job Scheduling 165](#_Toc232848040)

[5.1.1 Generate Limit Utilizations 165](#_Toc232848041)

[5.1.2 Send Correspondence 167](#_Toc232848042)

[5.1.3 Adjust Interest Rate 168](#_Toc232848043)

[5.1.4 Update Planned Records 170](#_Toc232848044)

[5.1.5 Generate Cash Flow – Money Market 172](#_Toc232848045)

[5.1.6 Generate Payment Request 174](#_Toc232848046)

[5.1.7 Post Flows to General Ledger 176](#_Toc232848047)

[5.1.7.1 Template - Fix, Pay and Post Flows 176](#_Toc232848048)

[5.1.7.2 Template - Process Business Transactions 178](#_Toc232848049)

[5.1.8 Run Accrual 180](#_Toc232848050)

[5.1.9 Calculate Fair Value of Transaction 182](#_Toc232848051)

[5.1.10 Key Date Valuation 184](#_Toc232848052)

[5.1.11 Post Realized Profit and Loss 186](#_Toc232848053)

[5.1.12 Calculate Market Risk Key Figures 188](#_Toc232848054)

[5.2 Output Management 190](#_Toc232848055)

[5.2.1 Output Parameter Determination 190](#_Toc232848056)

[5.2.2 Manage Output Items 192](#_Toc232848057)

[5.2.3 Maintain Print Queues 194](#_Toc232848058)

[5.2.4 Display Email Transmissions 194](#_Toc232848059)

[5.2.5 Maintain Email Template 195](#_Toc232848060)

[5.2.6 Maintain Form Templates 196](#_Toc232848061)

[5.3 Accounting 197](#_Toc232848062)

[5.3.1 Reverse Accrual 197](#_Toc232848063)

[5.3.2 Reverse Valuation 199](#_Toc232848064)

[5.3.3 Reversal Valuation Class Transfer 200](#_Toc232848065)

[5.3.4 Account Assignment Reference Transfer 201](#_Toc232848066)

[5.3.5 Reverse Account Assignment Reference Transfer 203](#_Toc232848067)

[5.4 Cash Flow 205](#_Toc232848068)

[5.4.1 Update Cash Flow for Deposit at Notice 205](#_Toc232848069)

[5.5 Interest Rate Adjustment 206](#_Toc232848070)

[5.5.1 Change Adjustment (Interest Rates/Prices) 206](#_Toc232848071)

[5.5.2 Display Adjustment (Interest Rates/Prices) 207](#_Toc232848072)

[5.5.3 Reverse Automatic Adjustments (Interest Rates/Prices) 208](#_Toc232848073)

[5.5.4 Reverse Adjustment (Interest Rates/Prices) 209](#_Toc232848074)

[5.6 Market Risk Analyzer 210](#_Toc232848075)

[5.6.1 Manage Market Data Shift 210](#_Toc232848076)

[5.6.2 Maintain Scenarios 211](#_Toc232848077)

[5.6.3 Defining Report Layout for Calculate Market Risk Key Figures 212](#_Toc232848078)

[5.6.4 Manage Market Risk Key Figure Sets 215](#_Toc232848079)

[5.7 Credit Risk Analyzer 218](#_Toc232848080)

[5.7.1 Display Limit Overview 218](#_Toc232848081)

[5.8 Change Counterparty 219](#_Toc232848082)

[5.8.1 Change Counterparty of Financial Transactions 219](#_Toc232848083)

[5.8.2 Display Financial Transactions with Changed Counterparty 220](#_Toc232848084)

[5.9 Copy Existing Transaction 221](#_Toc232848085)

[5.9.1 Copy Debt/Investment Contract 221](#_Toc232848086)

[5.10 Simulated Valuation 223](#_Toc232848087)

[5.10.1 Run Simulated Valuation 223](#_Toc232848088)

[5.10.2 Delete Simulated Valuation 225](#_Toc232848089)

[5.11 Notification for Managing Financial Transactions 226](#_Toc232848090)

[5.11.1 Create Teams and Responsibilities 227](#_Toc232848091)

[5.11.2 Enable Situation Types 229](#_Toc232848092)

[5.11.3 Create Fixed Term Deposit 231](#_Toc232848093)

[5.11.4 Trigger and Schedule the Notifications 231](#_Toc232848094)

[5.11.5 User Setting for Notification 232](#_Toc232848095)

[5.11.6 Check the Notification in Fiori Launchpad and E-Mail 233](#_Toc232848096)

## Purpose

Overview

The debt and investment management process helps you to secure short-term liquidity at optimal interest rates while effectively managing medium- to long-term debt and investments. This functionality automates labor-intensive tasks like confirming financial transactions and accounting postings, allowing you to focus on more strategic activities. It supports both operational and accounting needs and includes products such as fixed-interest and variable-interest investments and borrowing, commercial paper transactions, and deposit facilities.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/1WV_S4CLD2602_BPD_EN_AE.docx) ). |

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
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
| Cash Manager | SAP_BR_CASH_MANAGER | Cash Management | SAP_BR_CASH_MANAGER |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |
| Master Data Specialist - Business Partner Data | SAP_BR_BUPA_MASTER_SPECIALIST | Master Data - Business Partners / Business Partner Governance / Business Partner Governance / Business Partner Governance | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

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

| Master Data ID | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Business Condition | Comment |
| --- | --- |
| 1XN - Market Rates Management – Manually via Upload | Must be run before this test script, Market data must be created. |
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

In this step, you maintain general data for Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner view, choose Organization. | The Create Organization view displays. |  |
| 4 | Enter address data | On the Create Organization view, enter the following data, and choose Save:Business Partner: for example, 33537001Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Bank 1 - SAMPLE BANKSalutation: for example, Bank 1Search Term 1/2: for example, Bank 1Street/House number: <street/house number of the business partner>Postal Code/City: <postal code/city of the business partner>Ctry/Reg.: AELanguage: ENE-Mail: <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, <Dec 31 of the year 9999>Note Remain on this view for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to change mode | On the Display Organization33537001 details view, choose Switch Between Display and Change, and enter following data:Change in BP role: select TR0151 Counterparty | More counterparty related tabs, for example Legal Data, Rating display. |  |
| 6 | Enter Legal data | On the Change Organization: 33537001 view, choose the new role Counterparty view, and then from the Navigation Menu, choose Legal Data from the dropdown menu and enter the following data:Country/Region: AENote The navigation menu is on the right side of the view. It displays as … , and is next to the >),Note Remain in this view for subsequent steps. | The legal data is entered and saved.Change Organization: 33537001 , new role Counterparty view displays. |  |
| 7 | Enter Payment Transaction data | On Change Organization:33537001, new role Counterparty view, select Payment Transactions from the dropdown menu and enter following two rows of data, and choose Save:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, 18121976Bank acct: <bank account>IBAN: choose the IBAN button and choose <Bank account>Continue in the IBAN dialog box.Row 2:ID: for example, USD1C/R: for example, AEBank Key: for example, 18121976Bank acct: for example, <bank account>IBAN: choose the IBAN button and then choose Continue on the IBAN dialog box.Note If a dialog window of Information appears when you choose IBAN, choose Continue. | The Payment transaction data is entered and the Business Partner is saved. |  |

##### Maintain Payment Details for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the payment details data for the counterparty role of the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: view is displayed. |  |
| 3 | Switch to Change Mode | In the Maintain Business Partner: view, choose Open BP. In the dialog box, enter the following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter the following data:Change in BP Role: select TR0151 CounterpartyChoose Enter. | The Change Organization:33537001, new role Counterparty view is displayed. |  |
| 4 | Enter SI: Payment Details Data | On the Change Organization:33537001, new role Counterparty screen, choose Company Code, and enter the following data:Company Code: for example, 3310Choose ENTER and choose SI: Payment Details and enter the following data:Row 1:Currency: for example, AEDPay.Det.ID: for example, AEDIHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, <leave blank>Partner Bank: for example, <leave blank>Payment Request: for example, <deselect>Payment methods: for example, <leave blank>Row 2:Currency: for example, AEDPay.Det.ID: for example, AEDOHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, 33537001Partner Bank: for example, AED1Payment Request: for example, <select>Payment Methods: for example, TRow 3:Currency: for example, USDPay.Det.ID: for example, USDIHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/ee: for example, <leave blank>Payment Request: for example, <deselect>Payment Methods: for example, <leave blank>Row 4:Currency: for example, USDPay.Det.ID: for example, USDOHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/Payee: for example, 33537001Partner Bank: for example, USD1Payment Request: for example, <select>Payment Methods: FNote Remain in the view for subsequent steps.Note If the following warning message is displayed, choose No:Business partner proposed as payer/payee (see long text). Display this message for this business partner again? | The SI: Payment Details data is entered. |  |
| 5 | Assign Payment Details | In the view of the previous step, for AED, select the checkbox of AEDAEDI. Choose Assign. In the Counterparty Change: Payment Details Assignment dialog box, choose Select All Incoming.Now AEDI is displayed under PmntID-Inc. .Choose Continue to close the dialog box.Select the checkbox of AEDAEDO.Choose Assign. In the Counterparty Change: Payment Details Assignment dialog box, choose Select All Outgoing.Now AEDO is displayed under P-ID Outg.Choose Continue to close the dialog box.Repeat for USD:USDI: PmntID-IncUSD O: P-ID Outg.In the Change Organization:33537001, role Counterparty view, choose Save. | Payment details and the assignments are saved. |  |

##### Maintain Authorizations for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the authorization of the Counterparty role of the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP. In the dialog box, enter the following data:Business Partner: 33537001Choose Enter and choose Switch Between Display and Change, and enter the following data:Change in BP Role: select TR0151 Counterparty | The Change Organization: 33537001, role Counterparty screen is displaysed. |  |
| 4 | Enter SI: Authorizations Data | On the Change Organization: 33537001 screen, choose Company Code, select the Counterparty role. ChooseSI: Authorizations,, enter the following data and choose Save.In the Trans. Hierarchy column, find Money Market, then in the Auth. column, select the checkbox representing Money Market.Note You can also give authorization to a specific product type and transaction type by expending the folders. For testing purpose, you may give authorizations to all kinds of product types and transaction types. | The Authorization data is saved. |  |

##### Maintain Reporting Data in Company Code for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the company relationship for the Counterparty role of the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter following data:Business Partner: 33537001Choose Enter, choose Switch Between Display and Change, and enter the following data:Change in BP Role: select TR0151 Counterparty | The Change Organization: 33537001, role Counterparty screen is displayed. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization: 33537001, role Counterparty screen, choose Company Code, choose Reporting Data in Company Code, and enter the following data and choose Save.Comp. Rel.: for example, 3 OtherNote If you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown menu.Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itThey are used to derive the correct G/L accounts. | The reporting data is entered and saved. |  |

##### Maintain Derived Flows for Business Partner (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain derived flow data for the Counterparty role of the business partner. In some countries, for interest rate income, a special kind of tax is required. In this step, you set a country specific Interest Income Tax procedure for product type and transaction type. This step is optional.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP. In the dialog box, enter the following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change , and enter the following data:Change in BP Role: select TR0151 Counterparty | Change Organization: 33537001 , role Counterparty screen is displayed. |  |
| 4 | Enter SI: Derived Flows Data | On the Change Organization: 33537001, role Counterparty screen, choose Company Code, choose SI: Derived Flows, and enter the following data:Choose Money Market > Interest rate instrument > 51A Fixed-Term Deposit/Borrowing > 100 Investment, choose Select/Deselect Incoming line, in the Procedure for Generating Derived Flows 1 Entry dialog box, choose INTAE, and choose OK. Now INTAE is displayed in the Procedure column.Choose Save.Do the same for the following product type and transaction type combinations:Product TypeTransaction Type53A10053A10153A10254A10055A10058A300 | The Derived Flows data is entered and saved. |  |

#### Correspondence

Purpose

SAP TRM provides the standard correspondence functionality. When a TRM transaction is saved, the system either sends an email to the business partner, or automatically prints out a form.

To use the correspondence functionality, the following data needs to be assigned to the business partner:

- Business Partner Profile
- Business Partner Group

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

SAP has predefined the following business partner profiles:

- PR_EMAIL
- PR_PRINT

You can assign these predefined business partner profiles to your business partner. For example, if you communicate with your business partner via email, you can assign PR_EMAIL to your business partner; if you communicate with your business partner via printed file, you can assign PR_PRINT to your business partner.

SAP has predefined the following business partner group:

- BPG_DEFAULT

You can assign this business partner group to your business partner. You can also use SSCUIsDefine Business Partner Group and Assign Attributes for Business Partner Groups to add your own business partner group and assign appropriate attributes according to your specific requirement. Different business partner profiles and BP groups could be assigned to the same business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Assign Profile and BP Group - External Recipients (FTR_EXT_ASSIGN). | The Assignment of Profiles and BP Groups to External Recipients: view is displayed. |  |
| 3 | Enter Business Partner Data on the View | On the left side of the Assignment of Profiles and BP Groups to External Recipients: screen, choose Insert Row and enter the following data, and then select the business partner by ticking the checkbox before the business partner:BusPartner: for example, 33537001CoCd: for example, 3310Recpt/Send Type: for example, COUNTERPARTY | The Business Partner information is entered. |  |
| 4 | Assign Business Profile and BP Group to the Business Partner | On the top right side of the Assignment of Profiles and BP Groups to External Recipients screen, expand the node, and choose one item to maintain the business partner profile and business partner group, for example, Money Market > Interest rate instrument > 51A Fixed-Term Deposit/Borrowing > 100 Investment > 10 ContractThen on the bottom-right side of the screen, choose Insert Row, and enter the following data:Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTChoose Insert Row again and add another entry as follows：Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTNote Normally you only assign one profile to one combination of Product type/Transaction type/Activity Category. | Business partner profiles and BP groups are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat to Maintain More Entries | Select the item 33537001 on the left part of the screen, and choose Modify Row.Repeat the above step to maintain other items under the Money Market folder. | For all the listed Product Types/Transaction Types/ Activity Categories, BP profiles and BP groups are assigned. |  |

##### Maintain Profile and BP Group Assignments to Internal Recipient

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Internal Recipient ID is predefined and can be linked to SAP User ID(s). Once it's linked to an SAP user ID, whenever an internal correspondence object is generated, SAP TRM will send correspondence information to the address of the SAP User ID. Depending on the different profiles (PR_EMAIL /PR_PRINT), email is sent to the user's email address or a form is printed out.

In this step, you assign business partner profiles and BP groups to an internal business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Assign Profile and BP Group - Internal Recipients (FTR_INT_ASSIGN). | The Assignment of Profiles and BP Groups to Internal Recipients: view is displayed. |  |
| 3 | Enter Business Partner Data in the View | On the left side of Assignment of Profiles and BP Groups to Internal Recipients screen, choose Insert Row and enter the following data, and then select the item by ticking the checkbox before:IntRec: for example, INT.RECPCoCd: for example, 3310Recpt/Send Type: for example, INTERNALCheckbox: <select> | The Business Partner information is entered. |  |
| 4 | Assign Business Profile and BP Group to Business Partner | On the upper right part of the Assignment of Profiles and BP Groups to Internal Recipients screen, expend the node, and choose one item to maintain the business partner profile and business partner group, for example, Money Market > Interest rate instrument > 51A Fixed-Term Deposit/Borrowing > 100 Investment > 10 ContractThen on the lower right part of the screen, choose Insert Row, enter the following data, and choose SaveProfile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTUser Name: <select a User ID>.Choose Insert Row again and add another entry as following and choose Save:Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTUser Name: <select a User ID>.Note The user ID is a backend user ID. | User ID with business partner profile and BP group is assigned to the activity category. |  |
| 5 | Repeat to Maintain More Entries | Select the item INT.RECP in the left side view, and choose Modify Row.Repeat the above step to maintain other items under the Money Market folder. | User ID with business partner profile and BP group are assigned to all the listed Product Types/Transaction Types/Activity Categories. |  |

#### Maintaining Credit Limit

Purpose

A series of limit types are predefined. You can maintain credit limit of specific limit type according to the business needs. In this section, limit types Y01 and Y07 are maintained as an example.

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

In this step, you define traders in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Define Traders (S_ALR_87009302). | The Determine Work Area: Entry dialog box is displayed |  |
| 3 | Enter Work Area | Enter the following data and choose ContinueCompany Code: for example: 3310 | The Change View "Treasury: Traders": Overview screen is displayed. |  |
| 4 | Create a New Record | Select New Entries, enter the following data and choose Save:Trader: for example, TRADER02 | The data is saved. |  |

##### Define User Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you map the trader to your user, then it will be the default trader when you create new transactions in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Risk Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define User Data (S_ALR_87007933). | The Change View "Treasury: User master data supplements": Overview screen is displayed. |  |
| 3 | Create a New Record | Select New Entries, enter the following data and choose Save:User Name: for example: <Your user name>Trader: for example, TRADER02 | The data is saved. |  |

##### Maintain Trader Authorizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define authorization for traders.

Prerequisite

You have defined a trader in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Risk Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Trader Authorizations (TBT1). | The Create/Change Trans. Authorization for Trader: Init. screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Enter:Trader: for example, TRADER02Company Code: for example, 3310 | The Create/Change Transaction Authorization for Traders screen is displayed. |  |
| 4 | Enter Authorization and Save | Select or deselect the entries on the Authorization column and choose Save.Note Make sure to authorize TRADER02 for the Money Market transactions. | The data is saved with the following message: Transaction authorizations for trader TRADER02 are being saved. |  |

## Overview Table

The Debt and Investment Management(1WV) scope item consists of several process steps and reports, provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [(1XN) Market Rates Management – Manually via Upload](#unique_22) [page ] 35 | Treasury Risk Manager |  | Market data is maintained. |
| [Generate Limit Utilization](#unique_23) [page ] 35 | Treasury Specialist - Middle Office | End-of-Day Processing (KLNACHT) | Limit utilizations was determinate and updated. |
| [Analyze Cash Position](#unique_24) [page ] 36 | Cash Manager | Cash Flow Analyzer (F2332) | Cash manager check the cash position status, and make decisions of right financial instruments for short-term purpose based on analysis of cash position. |
| [Analyze Liquidity Forecast](#unique_25) [page ] 37 | Cash Manager | Cash Flow Analyzer (F2332) | The cash manager check the liquidity forecast regularly and make decisions regarding medium-term or long-term financial instruments. |
| [Check Credit Line Limit (Optional)](#unique_26) [page ] 37 | Treasury Specialist - Front Office | Credit Line Analysis- Review Booklet (F9064) | Credit line limits displays. |
| [Create Facility (Optional)](#unique_27) [page ] 38 | Treasury Specialist - Front Office | Create Facility (TM_61) | A facilities master record is created. |
| [Check Facilities Utilization (Optional)](#unique_28) [page ] 43 | Treasury Specialist - Front Office | Credit Line Analysis (FTR_CREDIT_LINE_ANALYSIS (FTR_CREDIT_LINE_ANALYSIS)) | The utilization of facility displays. |
| [Check Limit Utilization Report](#unique_29) [page ] 44 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | Limit utilization report displays. |
| [Review Money Market Trade Request Status](#unique_30) [page ] 45 | Treasury Specialist - Middle Office | Process Trade Requests (TPITRO) | The MM Trade requests are in the Released status. |
| [Create Fixed Term Deposit](#unique_31) [page ] 46 | Treasury Specialist - Front Office | Create IR Instrument (TM_51) | A fixed term deposit is created. |
| [Create Deposit at Notice](#unique_32) [page ] 48 | Treasury Specialist - Front Office | Create Deposit at Notice (TM11) | A deposit at notice is created. |
| [Create Commercial Paper](#unique_33) [page ] 49 | Treasury Specialist - Front Office | Create Commercial Paper (TM31) | A commercial paper is created. |
| [Create Cash Flow Transaction](#unique_34) [page ] 51 | Treasury Specialist - Front Office | Create Cash Flow Transaction (TM41) | Cash Flow is created. |
| [Create IR Instrument](#unique_35) [page ] 53 | Treasury Specialist - Front Office | Create IR Instrument (TM_51) | An interest rate instrument is created. |
| [Drawdown on Facilities](#unique_36) [page ] 59 | Treasury Specialist - Front Office | Create IR Instrument (TM_51) | Drawdown on Facilities through IR instrument. |
| [Create Current Acct-Style Instrument](#unique_37) [page ] 61 | Treasury Specialist - Front Office | Create CA Style Instrument (FTRCAI01) | Current Acct-Style Instrument is created. |
| [(BFB) Basic Cash Operations](#unique_38) [page ] 63 | Cash Manager | Cash Flow Analyzer (F2332) | Liquidity forecast reports is shown in the different processing phases of the transaction, |
| [(J78) Advanced Cash Operations](#unique_39) [page ] 64 | Cash Manager | Cash Flow Analyzer (F2332) or Check Cash Flow Items (F0735) | Liquidity forecast reports is shown in the different processing phases of the transaction, |
| [Set Settlement Status (Manual)](#unique_40) [page ] 65 | Treasury Specialist - Back Office | Process MM Transactions - Collective Processing (TM00) | TRM transaction is settled manually. |
| [Send Confirmation Email/Print](#unique_41) [page ] 67 |  |  |  |
| [Check Correspondence Status](#unique_42) [page ] 67 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The status of correspondence object displays. |
| [Receive Incoming Confirmation](#unique_43) [page ] 69 | N/A |  |  |
| [Find Deal and Match Deal Details](#unique_44) [page ] 69 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | An inbound correspondence object is crated and matched with outgoing correspondence object. |
| [Set Settlement Status](#unique_45) [page ] 71 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The settled transaction displays. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_46) [page ] 72 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_47) [page ] 76 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_48) [page ] 78 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_49) [page ] 81 | N/A |  |  |
| [Post to General Ledger](#unique_50) [page ] 81 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) | Cash flows related FI document is posted. |
| [Run Accrual](#unique_51) [page ] 84 | Treasury Accountant | Run Accrual/Deferral (TPM44) | Interest expenses and interest income are accrued and posted based on assigned time period. |
| [Calculate or Maintain Fair Value of Transaction](#unique_52) [page ] 85 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA); Enter Net Present Values (JBNPV) | The fair value of transaction is calculated automatically, or maintained manually. |
| [Perform Key Date Valuation](#unique_53) [page ] 88 | Treasury Accountant | Run Valuation (TPM1) | The financial instrument is valued, related FI document is posted. |
| [Interest Rate Adjustment Schedule Report](#unique_54) [page ] 90 | Treasury Specialist - Back Office | Adjustment Schedule - Rates/Prices (TJ07) | The interest rate adjustment schedule displays |
| [Adjust Interest Rate](#unique_55) [page ] 91 | Treasury Specialist - Back Office | Run Automatic Adjustments - Rates/Prices (TJ05); Create Adjustment - Rates/Prices (TI10) | The interest rate of transaction is changed automatically or manually. |
| [Display Payment Schedule](#unique_56) [page ] 94 | Treasury Accountant | Display Payment Schedules (TJ04) | Payment Schedules displays |
| [Option 1: Generate and Automatically Process Payment Request](#unique_57) [page ] 95 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_58) [page ] 99 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_59) [page ] 101 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_49) [page ] 81 | N/A |  |  |
| [Post to General Ledger](#unique_60) [page ] 104 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) | Cash flows related FI document is posted. |
| [Adjust Nominal Amount](#unique_61) [page ] 106 | Treasury Specialist - Front Office | Process MM Transactions - Collective Processing (TM00) | Increase or decrease nominal amount |
| [Option 1: Generate and Automatically Process Payment Request](#unique_62) [page ] 108 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_63) [page ] 112 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_64) [page ] 112 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_65) [page ] 113 | N/A |  |  |
| [Post to General Ledger](#unique_66) [page ] 113 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) | Cash flows related FI document is posted. |
| [Display Maturity Statistics](#unique_67) [page ] 114 | Treasury Specialist - Back Office | Manage Financial Transactions (F6157) | Maturity Statistics display. |
| [Reclassify from Long Term to Short Term (Valuation Class Transfer)](#unique_68) [page ] 115 | Treasury Accountant | Execute Valuation Class Transfer (TPM15M) | Valuation class transfer is executed from long term to short term, and reflected in financial accounting. |
| [Give Notice to Deposit at Notice](#unique_69) [page ] 116 | Treasury Specialist - Back Office | Process MM Transactions - Collective Processing (TM00) | The Deposit at Notice is terminated. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_70) [page ] 119 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_71) [page ] 123 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_72) [page ] 125 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Post to General Ledger](#unique_73) [page ] 141 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) | Cash flows related FI document is posted. |
| [Post Realized Profit and Loss](#unique_74) [page ] 143 | Treasury Accountant | Post Derived Business Transactions (TPM18) | The derived business transaction is fixed and posted. |
| [Display Treasury Posting Journal](#unique_75) [page ] 145 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Treasury posting journal displays. |
| [Treasury Position Analysis](#unique_76) [page ] 145 | Treasury Accountant | Treasury Position Analysis | Treasury position analysis displays. |
| [Display Treasury Position Values](#unique_77) [page ] 147 | Treasury Accountant | Display Treasury Position Values (F1867) | Treasury position values display. |
| [Define Financial Positions](#unique_78) [page ] 148 | Treasury Accountant | Define Financial Positions (FTR_FP_DEF) | Financial Positions are defined. |
| [Financial Status (Book Value)](#unique_79) [page ] 151 | Treasury Accountant | Financial Status (F2136) | The financial status on book values displays. |
| [Financial Status (Nominal Amount)](#unique_80) [page ] 152 | Treasury Accountant | Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)) | The financial status on nominal amount displays. |
| [Display Treasury Payments](#unique_81) [page ] 153 | Treasury Accountant | Display Treasury Payments (TPM20A) | Treasury Payment displays. |
| [Display Treasury Position Flows](#unique_82) [page ] 153 | Treasury Specialist - Back Office | Display Treasury Position Flows (F1754) | Treasury posting flows display. |
| [Display Treasury Alerts - Posting](#unique_83) [page ] 154 | Treasury Accountant | Display Treasury Alerts (F4984) | Treasury Alerts-Posting display. |
| [Display Treasury Alerts- Settlement, Release, Payment, Correspondence and Interest Rates](#unique_84) [page ] 155 | Treasury Specialist - Back Office | Display Treasury Alerts - Settlement (F4979) | Treasury Alerts display. |
| [Display Payment Schedules](#unique_85) [page ] 156 | Treasury Accountant | Display Payment Schedules (TJ04) | Payment schedules displays. |
| [Analyze Net Present Value (NPV)](#unique_86) [page ] 157 | Treasury Specialist - Middle Office | Analyze NPV (JBRX) | The NPV Result displays. |
| [Calculate Market Risk Key Figures](#unique_87) [page ] 158 | Treasury Specialist - Middle Office | Calculate Market Risk Key Figures (AISGENKF) | The single value analysis of assigned report layout displays. |
| [Sensitivity Key Figures](#unique_88) [page ] 159 | Treasury Specialist - Middle Office | Sensitivity Key Figures - Single Analysis (AISS) | The sensitivity key figures display. |
| [Review Limit Utilization Report](#unique_89) [page ] 160 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | Limit utilizations display. |
| [Review Maturity Profile](#unique_90) [page ] 161 | Treasury Specialist - Front Office | Debt and Investment Maturity Profile (F3130) | Maturity Profile display. |
| [Review Interest Rate Overview](#unique_91) [page ] 162 | Treasury Specialist - Front Office | Interest Rate Overview (F3098) | Interest Rate Overview displays. |
| [Debt and Investment Analysis](#unique_92) [page ] 163 | Treasury Specialist - Front Office | Debt and Investment Analysis (F3450) | Debt and Investment Analysis displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The test should take around Enter a duration, e.g. 60 minutes.

### (1XN) Market Rates Management – Manually via Upload

Purpose

In this step, you enter market data such as foreign currency exchange spot rates, swap rates, reference interest rates into the system.

These data provide default values when creating new transactions, or calculating fair value for existing transactions.

Procedure

Please refer to the Market Rates Management – Manually via Upload (1XN) test script for complete instructions.

|  |
| --- |
| Note The example data in 1XN might not contain the necessary interest rates for your test. If you are using SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA, please make sure that you've entered interest from current date to current date of next month when you are doing test for this test script. |

### Generate Limit Utilization

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the end of the transaction day, you run the end-of-day process to update limit utilization based on the latest market data.

|  |
| --- |
| Note You can schedule a background job for this step. For more information, see the Job Scheduling section in the Appendix. |

Prerequisite

The market data have been imported.

In the case of securities transactions, you need to maintain the spot price. You can refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed instructions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open End-of-Day Processing (KLNACHT). | The End-of-Day Processing screen is displayed. |  |
| 3 | Enter Criteria of End-of-Day Processing | On the End-of-Day Processing screen, enter the following data, and choose Execute:Valuation Date: for example, <the current date>Determination Procedure: for example, 10 to 20Company Code: for example, 3310 | The End-of-day processing was completed successfully message is displayed. |  |

### Analyze Cash Position

Purpose

At the end of the transaction day, the cash manager may review the cash position.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) SAP Fiori app to analyze the cash position. For more information, please refer to the Basic Cash Operations(BFB) test script.

### Analyze Liquidity Forecast

Purpose

In this step, you review the liquidity forecast to analyze medium-term or long-term financial status.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) app to analyze the liquidity forecast. For more information, refer to the Basic Cash Operations(BFB) test script.

### Check Credit Line Limit (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the total credit line, available amounts, overdraft amounts and amounts consumed as a review booklet. Review booklets are the latest format for multidimensional analytics apps with AI capability.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Credit Line Analysis - Review Booklet (F9064). | The Credit Line Analysis view is displayed. |  |
| 3 | Enter Selection Criteria | On the Credit Line Analysis screen, enter the following data, and choose Go:Start Date: for example, <the current date>End Date: for example, <the current date>Reporting Frequency: for example, DDisplay Currency: for example, AEDExchange Rate Type: for example, MAuthorized Company Code: for example, 3310 | The Credit limit view is displayed with four different tabs: Amount Overview, Utilization Overview, Transaction Overview and Amount Timeline.Note If the following error message is displayed, it means there is no credit line available yet. You may ignore this error message and continue with the next step.Result set for query XXXXXXXXXXXXXXXXX is empty |  |

### Create Facility (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the facility transaction in the system. For the current release, you can only create bilateral facilities or syndicated facilities.

Procedure

Option 1: Create bilateral facilities

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Facility (TM_61). | The Create Facility: Initial Screen view is displayed. |  |
| 3 | Create A New Facility | On the Create Facility: Initial Screen, enter the following data, and choose Enter:Company Code: for example, 3310Product Type: 56ATransaction Type: for example, 200Partner: for example, 33537001 | The Create Facility: Structure view is displayed. |  |
| 4 | Maintain Structure of New Facility | On the Create Facility: Structure screen, enter the following data:Start of Term: for example, <the current date>End of Term: for example, <the current date + 3 years>Inclusive: for example, Start IncludedExceedance of End of Term: for example, Not AllowedNote If you want to allow utilization of the facility after its end term, you can select Allowed. |  |  |
| 5 | Maintain Conditions | Choose Conditions, then choose Create Fee Condition from the dropdown list.In the popup dialog box, choose 1240 Facility fee: Not utilized.In the popup dialog box, enter the following data:Item eff. from: for example, <the current date> | The Overview of Conditions view is displayed. |  |
| 5 | Maintain Conditions | On the Amounts tab, enter the following data:Int.Calc.Type: for example, <select a proper interest calculation type>Int. Calc. Method: for example, <select a proper interest calculation method>Percentage Rate: for example, 3 | The Condition Details view is displayed. |  |
| 5 | Maintain Conditions | On the Dates tab, enter the following data, and choose back twice:Due Date: for example, <the current date + 3 years> | The condition type 1240 is created.The Create Facility: Structure view is displayed. |  |
| 6 | Maintain Profiles of New Facility | Choose the Profiles tab and choose Create, then enter the following data, and choose Copy entries.:Credit Line Amount: for example, 20MValid Frm: for example, <the current date> |  |  |
| 7 | Maintain Administration of New Facility | Choose the Administration tab, enter the following data, and choose Save:Gen. Valn Class: for example, Short term debt (current liability): Nominal/Facilities | Facility is created successfully. Make a note of the facility number for further procedures. |  |

Option 2: Create syndicated facilities

In this section, there are two main steps:

1. Define Sub Credit Lines – Syndicated Facilities

2. Create Syndicated Facility

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define Sub Credit Lines - Syndicated Facilities (TCL1). | The Definition of Credit Lines view is displayed. |  |
| 3 | Maintain the Definition of Credit Lines | Choose New Entries. In the Definition of Credit Lines section, enter the following data and choose Save:Row 1:Credit: for example, 2Currency: for example, AEDDraw: for example, <Selected>Line of Credit (Descript): for example, Subline for Bank LoanRow 2:Credit: for example, 3Currency: for example, AEDDraw: for example, <Selected>Line of Credit (Descript): for example, Subline for Bank Guarantee | The two credit lines are saved successfully. |  |
| 4 | Access the SAP Fiori App | Open Create Facility (TM_61). | The Create Facility: Initial Screen view is displayed. |  |
| 5 | Create A New Facility | On the Create Facility: Initial Screen, enter the following data, and choose Enter:Company Code: for example, 3310Product Type: 56BTransaction Type: for example, 200Partner: for example, 33537001 | The Create Facility: Structure view is displayed. |  |
| 6 | Maintain Structure of New Facility | On the Create Facility: Structure screen, enter the following data and choose Other Lines:Start of Term: for example, <the current date>End of Term: for example, <the current date + 3 years>Inclusive: for example, Start InclusiveExceedance of End of Term: for example, Not AllowedNote If you want to allow utilization of the facility after its end term, you can select Allowed.Start Date: for example, <the current date>End Date: for example, <the current date + 3 years>Rank: for example, S002 Syndicate BankPartner: for example, 33537001 | The Create Facility: Structure popup screen for Lines of Credit is displayed. |  |
|  |  | On the Create Facility: Structure pop up screen for Lines of Credit, add two additional rows as below, and choose Save:Row 1:Credit Line: for example, 2 Subline for Bankloan (AED)Subline of Cred.fr.: for example, 1 Prim.Credit Line (AED)Row 2:Credit Line: for example, 3 Subline for Bank Guarantee (AED)Subline of Cred.fr.: for example, 1 Prim.Credit Line (AED) | The Lines of Credit are saved successfully. |  |
| 7 | Maintain Conditions | Choose Conditions, then choose Create Fee Condition from the dropdown list.In the popup dialog box, choose 1240 Facility fee: Not utilized.In the popup dialog box, enter the following data and choose Copy.Item eff. from: for example, <the current date> | The Overview of Conditions view is displayed. |  |
| 8 | Maintain Conditions | On the Amounts tab, enter the following data:Int.Calc.Type: for example, <select a proper interest calculation type>Int. Calc. Method: for example, <select a proper interest calculation method>Percentage Rate: for example, 3 | The Condition Details view is displayed. |  |
| 9 | Maintain Conditions | On the Dates tab, enter the following data, and choose back twice:Due Date: for example, <the current date + 3 years>Note If you want to calculate the condition based on sub line, you can change the selected dropdown value of Credit Line, by default, it is based on Prim. Credit Line. | The condition type 1240 is created.The Create Facility: Structure view is displayed. |  |
| 10 | Maintain Profiles of New Facility | On the Profiles tab, choose 3 Profile:Total Credit Line from the Overview dropdown list and Prim.Credit Line from the Credit Line dropdown list.Choose Create, enter the following data, and choose Copy entries.Credit Line Amount: for example, 20MValid Frm: for example, <the current date> | The Profile for total credit line is added in the List. |  |
| 11 | Maintain Profiles of New Facility | Choose 3 Profile:Total Credit Line from the Overview dropdown list and S2 Subline for BankLoan from the Credit Line dropdown list.Choose Create, enter the following data, and choose Copy entries.Credit Line Amount: for example, 15MValid Frm: for example, <the current date>Then choose Syndication. | The popup screen for Change Facility: Profiles is displayed. |  |
| 12 | Maintain Profiles of New Facility | On the Change Facility: Profiles screen, in the Commitment section, enter the following data, and choose Save:Partner: for example, 33537001New commitment : for example, 15M | The Syndication is created successfully. |  |
| 13 | Maintain Rules | On the Rules Tab, Choose 3 TranscationType from the Ruleset Entity dropdown list, enter the following data as a new line in the Rule Maintenance section.ProdType: for example, 55ATransTy. : for example, 200Maximum Term: for example, 1095 | The rules are saved successfully. |  |
| 14 | Maintain Administration of New Facility | Choose the Administration tab, enter the following data, and choose Save:Gen. Valn Class: for example, Short term debt (current liability): Nominal/Facilities | Facility is created successfully. Make a note of the facility number for further procedures. |  |

### Settle Facility (Optional)

Purpose

In this step, you settle the facility you created. You can only drawdown facilities that are settled.

Procedure

Refer to the [Correspondence](#unique_95) [page ] 64 section for how to settle the facility.

### Check Facilities Utilization (Optional)

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
| 2 | Access the SAP Fiori App | Open Credit Line Analysis (FTR_CREDIT_LINE_ANALYSIS (FTR_CREDIT_LINE_ANALYSIS)). | The Prompts dialog box is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Go:Company Code: for example, 3310Transaction Number: <facility transaction number which was created in previous steps, or leave blank for all facilities transactions>Start Date: for example, <the current date>End Date: for example, <the current date>Reporting Frequency: for example, DDisplay Currency: for example, AEDExchange Rate Type: for example, M | The Credit Line Analysis view is displayed. |  |
| 4 | Display by Transaction Number | On the Dimensions panel, choose the Transaction Number dimension and drag it to the Columns or the Rows panel to display the results by Transaction Number.Note The utilization of facility is in the Utilized Amt in DC field. | The facilities utilization is displayed by transaction number. |  |

### Check Limit Utilization Report

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

You have maintained the limit types in the system.

You have run the [Generate Limit Utilization](#unique_23) [page ] 35 step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Execute:Limit Type: for example, Y01 or Y07Limit Utilization Base: for example, 1Determination Date: for example, <the current date>Limits Valid From: for example, <the current date> | An overview of the limit utilization in accordance with your selection criteria is displayed. |  |

### Review Money Market Trade Request Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step is optional. In the money markert trading platform integration scenario, you can create money market transactions through cash trade request in cash management. Then you need to check the status of trade requests for money market transactions that are created when cash trade requests are released.

Prerequisite

You have created and released cash trade requests by performing the following sections in the Advanced Cash Operations(J78) test script.

- Cash Trade Request
    - Create and Submit Cash Trade Request for Money Market
    - Release Cash Trade Request

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Process Trade Requests (TPITRO). | The Process Trade Requests screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Start:Trade Request Category: CashNote The Instrument Group of MM trade requests is Money Market. | MM trade requests that match the filter criteria are displayed. |  |
| 4 | Go to Detailed Page | Select the checkbox before an MM trade request, and choose Display Trade Request.Confirm the following on the General tab:Trade Request Status: ReleasedInstrument Category: not defined | The Money Market Trade Request screen is displayed.The MM trade requests are in the Released status. |  |

### Create Debt or Investment Contract

Purpose

In this section, you create money market transactions with predefined product types.

#### Create Fixed Term Deposit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a fixed term deposit transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create IR Instrument (TM_51). | The Create Interest Rate Instrument screen is displayed. |  |
| 3 | Create New Deal | Enter the following data, and choose Enter:Company Code: for example, 3310Product Type: 51ATransaction Type: for example, 100Partner: for example, 33537001 | The Create Interest Rate Instrument: Structure screen is displayed. |  |
| 4 | Maintain Structure of New Deal | Enter the following data:Amount: for example, 1MStart: for example, <the current date>End: for example, <the current date + 1 year>Percentage Rate: for example, 3.0000000Int. Calc. Method: for example, <select a proper interest calculation method>Frequency: for example, MonthlyContract Date: for example, <the current date/current time> |  |  |
| 5 | Maintain Administration of New Deal | On the Administr. tab, choose a proper Gen. Valn Class:Gen. Valn Class: <select proper Gen. Valn Class for transaction, for example,Short term investment (current asset): Amortized cost>Enter the following data for SPPI Classification (Optional):Valid From: <the current date/current time>SPPI Criteria: for example, Passed |  |  |
| 6 | Maintain Payment Details of New Deal | Choose the Payment Details. Double click on the outgoing row, confirm the following data:Payment Request: <select this checkbox>House Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, T |  |  |
| 7 | Save the New Deal | Choose Check to verify the input data. If no error message appears, choose Save. | An interest rate instrument is created. |  |

#### Create Deposit at Notice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A deposit at notice is an investment or borrowing without defined due date.

In this step, you create deposit at notice transactions with product type 52B through the Create IR Instrument (TM_51) app.

|  |
| --- |
| Note Product type 52B is based on product category 550 Interest Rate Instrument, which has the term category At Notice and supports fixed, variable, scaled (incremental), and scaled (interval) interest conditions. |

Procedure

Creating a deposit at notice transaction with variable interest rate.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create IR Instrument (TM_51). | The Create Interest Rate Instrument screen is displayed. |  |
| 3 | Create A New Deal | On the Create Interest Rate Instrument view, enter the following data, and choose Enter:Company Code: for example, 3310Product Type: 52BTransaction Type: for example, 100Partner: for example, 33537001 | The Create Interest Rate Instrument: Structure screen is displayed. |  |
| 4 | Maintain Structure of New Deal | On the Create Interest Rate Instrument: Structure screen, enter the following data:Amount: for example, 1MStart: for example, <the current date>Interest Cat.: for example, VariableRef.Int.Rate: for example, AEDM03EIB+/- 11st Int. Rate: for example, 3.0000000Int. Calc. Method: for example, act/360Frequency: for example, MonthlyContract Date: for example, <the current datecurrent time> |  |  |
| 5 | Maintain Administration of New Deal | Choose the Administr. tab, and choose a proper Gen. Valn Class:Gen. Valn Class: for example, Short term investment (current asset): Amortized cost |  |  |
| 6 | Maintain Payment Details of New Deal | Choose the Payment Details tab. On the Payment Details tab, double-click on the outgoing row, confirm the following data:Payment Request, With: <select this checkbox>House Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, T |  |  |
| 7 | Save the New Deal | Choose Check to verify the input data. If no error message appears, choose Save. | Variable rate deposit at notice is created. Make a note of the transaction number displayed for the notice process. |  |

#### Create Commercial Paper

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a commercial paper.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Commercial Paper (TM31). | The Create Commercial Paper screen is displayed. |  |
| 3 | Create A New Deal | Enter the following data, and choose Enter:Company Code: for example, 3310Product Type: 53ATransaction Type: for example, 102Partner: for example, 33537001 | The Create Commercial Paper: Structure screen is displayed. |  |
| 4 | Maintain Structure of New Deal | Enter the following data, and choose Enter:Nominal Amount: for example, 10MStart: for example, <the current date>End: for example, <the current date + 6 months>Int. Calc. Method: for example, <select a proper interest calculation method>Contract Date: for example, <the current date/current time>Trader: for example, TRADER02Choose the Detail view: Main flow button on the right side of the Flow Type field, enter the following data in the Principal Increase - Change dialog box, and then choose Copy.Pmnt Amount: for example, 9.6MNote If the following error message appears, the trader authorizations must be maintained. For more information, see the previous Maintain Trader Authorization procedure in the Preliminary Steps section of the Prerequisites.Trader TRADER02 has no authorization for transaction type selected |  |  |
| 5 | Maintain Administration of New Deal | On the Administration tab,Gen. Valn Class: <select a proper Gen. Valn Class for transaction, for example, Short term investment (current asset): Amortized cost>Enter the following data for SPPI Classification (Optional):Valid From: <the current date/current time>SPPI Criteria: for example, Passed |  |  |
| 6 | Maintain Payment Details of New Deal | On the Payment Details tab, double click on the outgoing row, confirm the following data:Payment Request: <select this checkbox>House Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, T |  |  |
| 7 | Save the New Deal | Choose Check to verify the input data. If no error message appears, choose Save. | Commercial Paper is created. |  |

#### Create Cash Flow Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a cash flow transaction with predefined product type 54A. For cash flow transactions, you can manage transactions whose structural characteristics cannot be mapped by the standard product categories. You can map your financial transactions flexibly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Cash Flow Transaction (TM41). | The Create Cash Flow Transaction screen is displayed. |  |
| 3 | Create New Deal | On the Create Cash Flow Transaction (TM41) view, enter the following data, and choose Enter:Company Code: for example, 3310Product Type: 54ATransaction Type: for example, 200Partner: for example, 33537001 | The Create Cash Flow Transaction: Structure screen is displayed. |  |
| 4 | Maintain Structure of New Deal | Enter the following data:Start: for example, <the current date>End: for example, <the current date + 6 months>Contract Date: for example, <the current date/current time> |  |  |
| 5 | Maintain Flow in Structure | On the Flows tab of the Create Cash Flow Transaction: Structure screen, enter the following data:ROW 1Flow Type: For example, 1100Payment Amount: for example, 1MPayment Date: for example, <the current date>ROW 2Flow Type: For example, 1120Payment Amt: for example, 1MPayment Date: for example, <the current date + 6 Months> |  |  |
| 6 | Maintain Administration of New Deal | On the Administration tab, enter the following data:Gen. Valn Class: <select proper Gen. Valn Class for transaction, for example,Short term debt (current liability)>Enter the following data for SPPI Classification (Optional):Valid From: <the current date/current time>SPPI Criteria: for example, Passed |  |  |
| 7 | Maintain Account Assignment Reference | Choose Menu-> Environment-> Position Indicator. Enter the following data, and choose Transfer Data:Record 1:AcctAssRef: For example, 101200000000If Record 2 exists, when parallel valuation is activated, then enter the following data:AcctAssRef: For example, 101200000000 | Account assignment reference is maintained. |  |
| 8 | Maintain Payment Details of New Deal | On the Payment Details tab, double click on the outgoing row, confirm the following data:Payment Request, With: <select this checkbox>House Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, T |  |  |
| 9 | Save the New Deal | Choose Check to verify the input data. If no error message appears, choose Save. | Cash flow transaction is created. |  |

#### Create IR Instrument

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create an interest rate instrument.

For the variable interest rate instrument, you can choose to use Interbank Offered Rate (IBOR) as reference interest rate, or the predefined overnight rates: SOFR, ESTER, SONIA, SARON, TONAR, CORRA, SORA, HONIA.

|  |
| --- |
| Note If you choose to use SOFR, ESTER, SONIA, SARON, TONAR, CORRA, SORA, HONIA, you need to set up your own yield curves, basis spreads and basis spread curves via relevant SSCUIs based on these reference interest rates. |

You can also create price index based interest rate instrument. Following product types are predefined:

- 55P: Interest rate instrument price index on interest
- 55Q: Interest rate instrument price index on interest and repayment

Procedure

1. Variable interest rate instrument with IBOR as the reference interest rate

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create IR Instrument (TM_51). | The Create Interest Rate Instrument screen is displayed. |  |
| 3 | Create A New Deal | On the Create Interest Rate Instrument view, enter the following data:Company Code: for example, 3310Product Type: 55ATransaction Type: for example, 100Partner: for example, 33537001and choose Enter. | The Create Interest Rate Instrument: Structure screen is displayed. |  |
| 4 | Maintain Structure of New Deal | On the Create Interest Rate Instrument: Structure screen, enter the following data:Amount: for example, 10MStart: for example, <the current date>End: for example, <the current date + 3 years>Interest Cat.: for example, VariableRef.Int.Rate: for example, AEDM03EIB +/- 11st Int. Rate: for example, 3.0000000Int. Calc. Method: for example, <select a proper interest calculation method>Frequency: for example, MonthlyContract Date: for example, <the current date/current time>. |  |  |
| 5 | Maintain Administration of New Deal | On the Administr. tab, enter the following data:Portfolio: for example, Y000Gen. Valn Class: <select proper Gen. Valn Class for transaction, for example, Long term debt (non-current liability)Enter the following data for SPPI Classification (Optional):Valid From: <the current date/current time>SPPI Criteria: for example, Passed |  |  |
| 6 | Maintain Payment Details of New Deal | On the Payment Details tab, double-click on the outgoing row, confirm the following data:Payment Request, With: <select this checkbox>House Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, T. |  |  |
| 7 | Save the New Deal | Choose Check verify the input data. If no error message, choose Save. | Interest rate instrument is created. |  |

2. Variable interest rate instrument with overnight rates as the reference interest rate (SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create IR Instrument (TM_51). | The Create Interest Rate Instrument screen is displayed. |  |
| 3 | Create New Deal | On the Create Interest Rate Instrument view, enter the following data, and choose Enter:Company Code: for example, 3310Product Type: 55ATransaction Type: for example, 100Partner: for example, 33537001Currency: for example, USD | The Create Interest Rate Instrument: Structure screen is displayed. |  |
| 4 | Maintain Structure of New Deal | On the Create Interest Rate Instrument: Structure screen, enter the following data:Amount: for example, 10MStart: for example, <the current date>End: for example, <the current date + 1 month>Interest Cat.: for example, VariableRef. Int. Rate: for example, SOFRInt.Calc.Method: for example, act/360Contract Date: for example, <the current date/current time>. |  |  |
| 5 | Check Conditions | Choose Conditions on the menu bar to review the condition details. | Three conditions are displayed:Nominal interestInterest rate adjustmentFinal repayment |  |
| 6 | Enter Nominal Interest | Double click on the Nominal interest condition type, make the following entries and then choose Back.On the Amounts tab, enter the following data:Int. Calc. Type: for example, Compound Interest CalculationInt.Calc.Method: for example, 2 act/360Note If Compound Interest Calculation is selected, you want a reference rate plus a spread, you should input value in following field:Percentage Rate: for example, 1If Average Compound Interest Calculation is selected, the following fields under Average Interest Rate are displayed.Weighting: for example, L Based on Interest Rate Adjustment DateRounding: for example, Round to the NearestDecimal Places : for example, 4Spread: for example, 1Upper Limit: <select, and enter value, for example, 2>Lower Limit: <select and enter value, for example, 0.5>On the Dates tab, enter the following data:Calculation Date: for example, Regular 7 Calendar Days1st date: for example, <the current date + 7 days>Due date: for example, Regular 7 Calendar Days1st date: for example, <the current date + 7 days> |  |  |
| 7 | Maintain Interest Rate Adjustment | Double click on the Interest rate adjustment condition type, make the following entries and then choose Back:Interest Rate Adjustment: for example, Regular 1 Calendar DaysIR Adj. Date: for example, <the current date>Calendar Rule: Previous Working DayInterest Rate Fixing Date: for example, Relative, - 1 Working days,Lockout Period: 1 Working days |  |  |
| 8 | Maintain Accumulating Condition | In the overview of Condition view, select condition type 1200-Nominal Interest, then choose Create Accumulating Condition.In the pop up dialog box, double click on condition type 1205-Nominal interest (accumulated).Eff.From: <the current date>then choose Back. |  |  |
| 9 | Check Accumulated Flows | On the Cash Flow tab, choose Show/Hide Single Flows. | The 1200 Normnial interests flow will show up. |  |
| 10 | Maintain Administration of New Deal | On the Create Interest Rate Instrument: Structure screen, choose the Administr. tab, and enter the following data:Portfolio: for example, Y000Gen. Valn Class: <select proper Gen. Valn Class for transaction, for example, Short term debt (current liability)>Enter the following data for SPPI Classification (Optional):Valid From: <the current date/current time>SPPI Criteria: for example, Passed |  |  |
| 11 | Maintain Payment Details of New Deal | On the Payment Details tab, double-click on the outgoing row, and enter the following data:Payment Request, With: <select this checkbox>House Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, T |  |  |
| 12 | Save the New Deal | Choose Check to verify the input data. If no error message, choose Save. | Interest rate instrument is created. |  |

3. Price index based interest rate instrument

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create IR Instrument (TM_51). | The Create Interest Rate Instrument screen is displayed. |  |
| 3 | Create New Deal | On the Create Interest Rate Instrument screen, enter the following data, and choose Enter:Company Code: for example, 3310Product Type: for example, 55PTransaction Type: for example, 100Partner: for example, 33537001 | The Create Interest Rate Instrument: Structure screen is displayed. |  |
| 4 | Maintain Structure of New Deal | On the Create Interest Rate Instrument: Structure screen, enter the following data:Amount: for example, 10MStart: for example, <the current date>End: for example, <the current date + 3 years>In the Index Adjustment section,Index Name: for example, CPIBase Date: <the current date>IdxInterpolate: for example, Without InterpolationPriceIdxApply: for example, BASE Price Index Applied on Base AmountIdxRelDate: for example, Calculation DateCalculation Dt.: for example, <the current date + 1 month>, and select the Inclusive indicator.Every: 1 MonthsIdxFixDateLow: for example, <the first date of the current month>In the Interest Structure section,Interest Cat.: for example, FixedPercentage Rate: for example, 12Int. Calc. Method: for example, 360/360Frequency: for example, MonthlyEvery: 1 MonthsIn the Contract Conclusion section,Contract Date: for example, <the current date/current time>. |  |  |
| 5 | Maintain Administration of New Deal | On the Administr. tab, enter the following data:Portfolio: for example, Y000Gen. Valn Class: <select proper Gen. Valn Class for transaction, , for example, Long term investment (non-current asset): Amortized cost>Enter the following data for SPPI Classification (Optional):Valid From: <the current date/current time>SPPI Criteria: for example, Passed |  |  |
| 6 | Maintain Payment Details of New Deal | On the Payment Details tab, double click on the outgoing row, and confirm the following data:Payment Request, With: <select this checkbox>House Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, T. |  |  |
| 7 | Save the New Deal | Choose Check verify the input data. If no error message, choose Save. | Interest rate instrument is created. |  |

#### Drawdown on Facilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can draw varying amounts at any time up to the total approved credit line of a facility.

In this step, you draw the line of credit by assigning facility to IR instrument as an example.

Prerequisite

You've created and settled a facility.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create IR Instrument (TM_51). | The Create Interest Rate Instrument screen is displayed. |  |
| 3 | Create A New Deal | On the Create Interest Rate Instrument view, enter the following data, and choose Enter:Company Code: for example, 3310Product Type: 55ATransaction Type: for example, 200Partner: for example, 33537001 | The Create Interest Rate Instrument: Structure view is displayed. |  |
| 4 | Maintain Structure of New Deal | On the Create Interest Rate Instrument: Structure view, enter the following data:Payment Amount: for example, 10MStart: for example, <the current date>End: for example, <the current date + 6 months>Interest Cat.: for example, VariableRef.Int.Rate: for example, <choose a proper reference interest rate>1st Int. Rate: for example, 3.0000000Int. Calc. Method: for example, <select a proper interest calculation method>Frequency: for example, MonthlyContract Date: for example, <the current date/current time> |  |  |
| 5 | Maintain Administration of New Deal | On the Administr. tab, enter following data:Gen. Valn Class: for example, Short term debt (current liability) |  |  |
| 6 | Maintain Facilities in Administration | On the Create Interest Rate Instrument: Administr. screen, choose Create beside facilities, and enter the following data in the dialog box, and choose Choose:Company Code: for example, 3310Transaction: <facilities you created in the previous step>Note If you choose a syndicated facility, you need to select subline for Bank loan from the credit line dropdown list. |  |  |
| 7 | Maintain Payment Details of New Deal | On the Payment Details tab, double click on the outgoing row, and confirm the following data:Payment Request: <select this checkbox>House Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, T |  |  |
| 8 | Save the New Deal | Choose Check to verify the input data. If no error message displays, choose Save. | Interest rate instrument is created. |  |

#### Create Current Acct-Style Instrument

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a Current Acct-Style instrument, which has similar functionality with Interest Rate Instrument. A specific feature of Current Acct-Style Instrument is that the nominal amount can be changed through additional cash flows, even from positive to negative (Asset/Liability position switch).

|  |
| --- |
| Note For the nominal amount increase or decrease process, refer to the [Nominal Amount Adjustment](#unique_97) [page ] 106 section. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create CA Style Instrument (FTRCAI01). | The Create Current Acct-Style Instrument screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following selection criteria, and choose Enter:Company Code: for example, 3310Product Type: 58ATransaction Type: for example, 300Partner: for example, 33537001 | The Create Current Acct-Style Instrument: Structure screen is displayed. |  |
| 4 | Enter Data | Enter the following data:Flow Type: for example, 1101 for Nominal Amount Increase or 1111 for Nominal Amount DecreaseAmount: for example, 10MStart: for example, <the current date - 7 days>End: for example, <the current date + 3 years>Interest Cat.: for example, FixedPercentage Rate: for example, 3.0000000Int. Calc. Method: for example, <select a proper interest calculation method>Frequency: for example, MonthlyContract Date: for example, <the current date - 7 days> | The Create Current Acct-Style Instrument: Structure screen is displayed. |  |
| 5 | Maintain Administration of New Deal | On the Administr. tab, enter following data:Gen. Valn Class: <select proper Gen. Valn Class for transaction, for example,Long term investment (non-current asset): Amortized cost>Enter the following data for SPPI Classification (Optional):Valid From: <the current date/current time>SPPI Criteria: for example, Passed |  |  |
| 6 | Maintain Payment Details of New Deal | On the Payment Details tab, double click on the outgoing row, and confirm the following data:Payment Request, With: <select this checkbox>House Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, T |  |  |
| 7 | Save the New Deal | Choose Check to verify the input data. If no error message, choose Save. | A current acct-style instrument is created. Note down the transaction number for further step. |  |

### (BFB) Basic Cash Operations

Purpose

After the deal is created (in status Contract) and before the payment is executed, the future cash flows of this deal will be reflected in liquidity forecast reports. If basic cash management is implemented in your system, please use the Cash Flow Analyzer (F2332) app to check the liquidity forecast.

|  |
| --- |
| Note This step can be executed the whole lifecycle of the treasury deal and different result under liquidity forecast reports will be shown in the different processing phases of the transaction, for example, before transaction is created, after transaction is created, or after the payment is posted. |

Procedure

If basic cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) app to check the liquidity forecast change. For details, please refer to the Basic Cash Operations (BFB) test script.

Treasury relevant cash flows are reflected in treasury specific planning levels, for example:

- MM - Money Market Deals
- NM - MM Deals (Bank unknown)
- FX - Foreign Exchange Deals
- FO - Foreign Exchange Options
- NF - Forex Deals (Bank unknown)
- DR - Derivative Deals
- ND - Derivative Deals(Bank unknown)

### (J78) Advanced Cash Operations

Purpose

After the deal is created (in status Contract) and before payment is executed, the future cash flows of this deal will be reflected in liquidity forecast reports. If full cash management is implemented in your system, use the Cash Flow Analyzer (F2332) app or the Check Cash Flow Items (F0735) app to check the liquidity forecast.

|  |
| --- |
| Note You can execute this step at any time during the lifecycle of the treasury deal. In the liquidity forecast reports, different results are shown during different processing phases of the transaction (for example, before creation of the transaction, after creation of the transaction, and after posting of the payment). |

Procedure

If full cash management is implemented in your system, you can use the Cash Flow Analyzer app or the Check Cash Flow Items (F0735) app to check the liquidity forecast change. For details, please refer to the Advanced Cash Operations(J78) test script.

Treasury relevant cash flows are reflected in treasury specific planning levels, for example:

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

Once a Treasury Risk Management (TRM) transaction is recorded and saved, the transaction must be settled before continuing with further activities. You can settle the transaction in two ways, once you get counterparty confirmation:

- Manual Settlement

For example, if you receive counterparty confirmation email, then you can use the Manage Financial Transactions app to settle the transaction manually.

- Automatic Settlement via Correspondence Process

For example, for one transaction, once all of the outgoing correspondence objects and incoming correspondence objects are matched and set to completed status, the financial transactions are set to settlement status automatically.

In this activity, you settle the TRM transaction manually.

Prerequisite

A TRM transaction is created successfully in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data, and choose Go:Key Date: <the current date>Company Code: for example, 3310Transaction: <the money market transaction you created in the previous step>Term End: <delete the default value> | The transaction is displayed. |  |
| 4 | Settle the TRM Transaction | On the Manage Financial Transactions screen, select the checkbox at the head of the transaction line and choose Settle. | You are directed to the screen for settling the transaction.Note The view title will be different according to product type of transaction. |  |
| 5 | Save the Change | Check the transaction details. If no problem, choose Save. | The transaction is settled and saved. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor view displays. |  |
| 3 | Enter Selection Criteria | On the Correspondence Monitor view, enter following data, and choose Execute:In the Correspondence area,Company Code: for example, 3310On the deal tab,Company Code: for example, 3310Deal Number: for example, <Transaction Number> | The Correspondence monitor - Standard View view displays. |  |
| 4 | Display Transaction History | On the Correspondence monitor - Standard View screen, select the checkbox of the incoming correspondence object, choose Show Underlying and the details of transaction view displays. | Activity 2 Contract Settlement displays in the second line. |  |

### Principal Payment

#### Corporate Initiated Payment

Purpose

In this step, you process the payment flows of the transaction. You have two options:

1. Process the payment with the ‘Auto. Payment Run’ function.
2. Process the payment without the ‘Auto. Payment Run’ function.

Prerequisites

You have settled the Contract.

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
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

Each financial transaction contains flows that require payment. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows requiring a payment request. It does not create a posting in financial accounting,

When the payment is initiated by the financial partner, skip this procedure and next procedure Process Payment Request, and continue with the Bank Initiated Payment procedure.

|  |
| --- |
| Note A background job can be scheduled for this procedure. Please see the corresponding step in the Appendix. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data:Money Market: <select>Company Code: for example 3310Transaction: <transaction number with outflows which you created in the previous procedures>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>Test Run: <select>Pay Only: <select this indicator>and choose Run. | The Payment Log - Test Run view displays, you review the payment information on this view.If message No flows exist for processing displays, then no payment with payment request are required for your selection criteria. When no flows exist, you can skip to next several procedures and go directly to the Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data:Test Run: <deselect>and choose Run. | The Payment Log screen is displayed. The payment request is generated.Make a note of the key number displayed on this view. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous procedure>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <current date>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, change the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. A payment request is generated.Note Make note of the key number displayed on this view for use in the following procedures. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Automatic Payment Transactions for Payment Requests (F111) SAP Fiori app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items), but on payment requests.

Prerequisite

Payment request has been generated in the previous procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests view displays. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests view, enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters view displays. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters view, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 3 days>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free Selection for payment run, enter the following data and choose Save:Key number: <the key number you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>If information Log created for all accounts displays, choose Continue.Choose Save on view Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on view Automatic Payment Transactions for Payment Requests. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat, and choose Schedule Job to confirm this dialog box.Message Proposal is running displays in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests view, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data and choose Run:Run Date: for example <current date>Identification: for example TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

##### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

#### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by a bank, you can skip the previous Generate Payment Request and Process Payment Request procedures.

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

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps are available for posting flows:

- Fix, Pay and Post Flows (TBB1): you use this app to generate the posting for incoming payment. Please note that when using this app in the current step, it will not create posting for the outgoing payment which has been processed in the Generate Payment Request step with the Pay Only option.
- Process Business Transactions (TPM10): You use this app to generate the posting for outgoing payment which has been processed in the previous step Generate Payment Request with the Pay Only option.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix. |

Prerequisite

The outgoing payment which should be handled via payment request for this transaction has been processed in the previous step Generate Payment Request with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Money Market: <select this checkbox>Company Code: for example 3310Transaction: <transaction number with inflow which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | Posting Log: Posted Business Transactions view is displayed. Review the simulated posting information for local GAAP (valuation area AE0) on this view.No posting is created because it is a test run.If message No flows exist for processing displays, there is no posting required for your selection criteria, you can skip current test step and continue to the test step 5 with app Process Business Transactions. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Execute:Test Run: <deselect this checkbox> | The Posting Log: Posted Business Transactions screen is displayed. An accounting document has been created for the incoming payment in the local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori app | Return to Home and open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 6 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>Under the OTC Transactions area:Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select this checkbox>and choose Execute. | Test Run: Post/Reverse Business Transactions view displays.If message You have not selected any business transactions is displayed, then there is no posting required for your selection criteria, you can skip this current step. |  |
| 7 | Check Test Run Result | On the Test Run: Post/Reverse Business Transactions view , choose Select All and choose Choose Those to Post, and then choose Execute.view Test Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0) on this view.There is no posting created because this is a test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions view, change the following data:Test Run: <deselect>and choose Execute. | Update Run: Post/Reverse Business Transactions view displays. |  |
| 9 | Production Run | Choose Select All and choose Choose Those to Post, and then choose Execute.Update Run: Display Posted/Reversed Business Transactions view displays. Choose Log and Messages. | Posting Log: Posted Business Transactions view displays, accounting document are created for outgoing payment in local GAAP (valuation area AE0). |  |

### Period-end Closing

Purpose

This section describes activities for period-end closing (usually executed at month end) and includes:

- Accrue interest income/expenses
- Calculate or maintain fair value of transactions
- Perform key date valuation

#### Run Accrual

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this function to accrue interest expenses and interest income based on existing financial instruments and reflect results correctly in the general ledger. The function distributes the amount correctly based on the time period from flow start date to the key date, irrespective of when they are due for payment or received.

You can also use SSCUI Assign Update Types for Accrual/Deferral to define your own accrual/deferral postings, such as aggregated accrual/deferral flow or not. In the case of a compound interest calculation, a grouping term has to be defined.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

|  |
| --- |
| Note You can schedule a background job for this step, please see the corresponding step in the Appendix. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Accrual/Deferral (TPM44). | The Execute Accrual/Deferral of Expenses and Revenues view displays. |  |
| 3 | Test Run | On the Execute Accrual/Deferral of Expenses and Revenues view, enter the following data:OTC Transactions: <select this checkbox>Company Code: for example 3310Valuation Area: for example, AE0Transaction: <transaction number(s) created in previous steps>Accrual/Deferral Key Date: for example, <last date of current month>Include key date: for example, <select this indicator>Test Run: <select this checkbox>and choose Execute. | A new Execute Accrual/Deferral of Expenses and Revenues view displays. Review accrual information in this view.Choose Logs and Messages to review the simulated posting information for local GAAP (valuation area AE0).There is no posting created because this is a test run. |  |
| 4 | Production Run | Choose Back until you return to the initial view of this app.Change the following data:Test Run: <deselect this checkbox>and choose Execute. | A new Execute Accrual/Deferral of Expenses and Revenues view displays. You review the accrual information on this view.Choose Logs and Messages to view the posting information for local GAAP (valuation area AE0).An accounting document has been created in local GAAP (valuation area AE0). |  |

#### Calculate or Maintain Fair Value of Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you determine the fair values, or net present value (NPV) of financial transactions.

The net present values can be calculated automatically by the Market Risk Analyzer (MRA) and saved to table VTVBAR. These values can then be used for the accounting valuation. In addition, you can also maintain the relevant net present value manually.

Pre-delivered configuration in MRA provides three options when calculating NPV automatically via app Calculate Net Present Values - With CVA and DVA (TPM60CVA):

- Risk-free NPV: using the evaluation type that doesn't contain basis spread curve or credit spread curve, the system only calculates the risk-free NPV.
- Risk-based NPV with credit spread curve: using the evaluation type that contains credit spread curve, the system calculates the risk-free NPV by using risk-free yield curve, and calculates the (risk-based) NPV which takes credit spreads into account.
- Risk-based NPV with basis spread curve and credit spread curve: the system calculates the risk-free NPV by using risk-free yield curve and basis spreads curve, and calculates the risk-based NPV that takes basis spreads and credit spreads into account.

There are two kinds of calculation method for CVA and DVA, one is based on Expected Exposures, the other is called difference method.

NPV = risk-free NPV – CVA – DVA.

Prerequisite

Before calculating NPV using the Calculate Net Present Values (Subtitle: with CVA and DVA) SAP Fiori app, ensure that the relevant market data (interest rates, foreign exchange rates, credit spreads, and so on) is maintained for the evaluation date. For details of market data maintenance, see the Market Rates Management – Manually via Upload (1XN) test script.

Procedure

Option 1: Calculate NPV Automatically

|  |
| --- |
| Note By default, Yield Curve Type 9001 is predefined with reference rate SOFR/ESTER; Yield Curve Type 0001 is defined with reference rate IBOR; Evaluation Type is defined with Yield Curve Type 0001 only. If you want to use SOFR, ESTER, SONIA, SARON, TONAR, CORRA, SORA, HONIA, you can choose to use SAP pre-delivered content, or set up your own yield curves, evaluation type, basis spreads and basis spread curves via relevant SSCUIs based on these reference rates. |

|  |
| --- |
| Note A background job can be scheduled for this procedure, please see the corresponding step in the Appendix. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments view displays. |  |
| 3 | Enter Selection Criteria and Execute | On the Determine NPVs Including Credit and Debit Value Adjustments view, enter the following dataEvaluation Parameter Derivatn: <do not select this checkbox>Select OTC Transactions: <select this checkbox>Company Code: for example 3310Transaction: <transaction number(s) created in previous steps>Evaluation Date: for example <last date of current month>Clean Price Calculation: <select>CVD/DVA Type: If you would like to calculate risk-free NPV, enter nothing; if you would like to calculate risk-based NPV and CVA/DVA, you can enter Y01 for CVA/DVA calculation via Difference Method, or you can enter Y02 or Y03 for CVA/DVA calculation based on expected exposures with the Variable or Constant approachEvaluation Type: If you would like to calculate risk-free NPV, enter Y001; if you would like to calculate risk-based NPV with Credit Spread Curve, enter Y002, if you would like to calculate risk-based NPV with Basis spread Curve and Credit Spread Curve, enter Y003Test Run: <do not select this checkbox>Price/NPV Type: 001Save Values with Warnings: <select this checkbox>Detail Log: <select this checkbox>and choose Execute. | The NPVs including CVA/DVA from the Market Risk Analyzer view displays, you can see the NPV, risk-free NPV, CVA, DVA of each transaction on this view.You can also check different information by clicking on buttons on this view:Single Transaction:CVA/DVA Key FiguresDetailed LogCalculation BasesError Log |  |

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

#### Perform Key Date Valuation

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
| Note By default, Yield Curve Type 9001 is defined with reference rate SOFR/ESTER; Yield Curve Type 0001 is defined with reference rate IBOR; Evaluation Type is defined with Yield Curve Type 0001 only. If you want to use SOFR, ESTER, SONIA, SARON, TONAR, CORRA, SORA, HONIA, you can choose to use SAP pre-delivered content, or set up your own yield curves, evaluation type, basis spreads and basis spread curves via relevant configuration steps or activities based on these reference rates. |

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

You can also use SSCUI Assign Update Types for Accrual/Deferral to define your own accrual/deferral postings, such as aggregated accrual/deferral flow or not. In the case of a compound interest calculation, a grouping term has to be defined.

|  |
| --- |
| Note A background job can be scheduled for this procedure, please see the corresponding step in the Appendix section. |

Prerequisite

Fair values (NPV) have been calculated or maintained for financial transactions which are evaluated at fair value (NPV) according to accounting principles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Run Valuation view is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run Valuation view, enter the following data and choose Execute:In the Product Groups area,OTC Transactions: <select this checkbox>In the General Selections area,Company Code: for example, 3310Valuation Area: for example AE0Transaction: <transaction number(s) created in previous steps>Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation with ResetNote When the Period End is also the Year End, use the Year End Valuation Valuation Category.Test Run: <select this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation.If dialog Message shows up, choose Continue. | The Valuation Log view displays.If a red traffic light displays, select it to review the error message. Resolve the issue and repeat the test run until there is no error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages.No posting is created because this is a test run.Note Sometimes there is no simulated posting because your selected transaction did not require valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the Run Valuation screen is displayed.On the Run Valuation screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation view, choose Run Valuation. | The view Valuation Log displays, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. The accounting document has been created in the local GAAP (valuation area AE0). |  |

### Interest Rate Adjustment

Purpose

This section describes activities for Interest Rate Adjustment and includes:

- Interest Rate Adjustment Schedule Report
- Adjust Interest Rate

#### Interest Rate Adjustment Schedule Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The interest rate adjustment schedule gives you an overview of interest rate adjustments that have already been made and the related interest rate and reference interest rate adjustment. It also tells you when the next interest rate adjustment for a particular transaction is scheduled.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Adjustment Schedule - Rates/Prices (TJ07). | The Rate/Price Adjustment Schedule screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Execute:Interest Rate Adjustment: <select this radio button>Company Code: for example, 3310Product Type: for example, 55A | The rate/price adjustment schedule report is displayed. |  |

#### Adjust Interest Rate

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

The reference interest rate has been maintained on the fixing date. Please refer to the Market Rates Management – Manually via Upload(1XN) test script for how to maintain reference interest rates.

|  |
| --- |
| Note The example data in 1XN might not contain the necessary interest rates for your test. If you are using SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA, please make sure that you've entered interest from current date to current date of next month when you are doing test for this test script. |

You have settled the contract.

Procedure

Option 1: Interest Rate Adjustment (Automatically)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Automatic Adjustments - Rates/Prices (TJ05). | The Run Automatic Rate or Price Adjustment screen is displayed. |  |
| 3 | Enter Parameter of Adjustment | Enter the following data, and choose Execute:Interest Rate Adjustment: <select this checkbox>Company Code: for example, 3310Fixing Date: for example, <Fixing Date you noted down in previous step>All Transactions: <deselect this checkbox>Single Transactions: <transaction number you noted down in previous procedure>Test Run: <deselect this checkbox> | The interest rate is adjusted automatically. |  |

Option 2: Interest Rate Adjustment (Manually)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Adjustment - Rates/Prices (TI10). | The Create Rate/Price Adjustment screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Enter:Company code: for example, 3310Transaction: <transaction number you noted down in previous procedure> |  |  |
| 4 | Enter Interest Rate | Enter the following data, and choose Save:Interest Rate Adjustment: <select this checkbox>Interest Rate: for example, 7 | A manual interest rate adjustment is created. |  |

### Update Price Index Value

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you update the price index value.

|  |
| --- |
| Note This step only applies to price-indexed interest rate instruments created as described in the third option in the Create IR Instrument step. |

Prerequisite

You've enter the latest price index value by following the Enter Price Index Values step in the Market Rates Management – Manually via Upload (1XN) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Automatic Adjustments - Rates/Prices (TJ05). | The Run Automatic Rate/Price Adjustment view is displayed. |  |
| 3 | Enter Parameter of Adjustment | Enter the following data:Price Index Adjustment: <select this checkbox>Company Code: for example, 3310Fixing Date: for example, <the date of interest payment>All Transactions: <deselect this checkbox>Single Transactions: <transaction number you noted down in previous procedure>Test Run: <select this checkbox>Check out the message. If no error, choose Back.Test Run: <deselect this checkbox>Choose Execute. | The price index values are updated automatically. |  |

### Interest Payment

Purpose

This section describes activities for interest payment, which includes payment schedules report display and the payment process.

#### Display Payment Schedule

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
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data:OTC Transactions: <select this checkbox>Company code: for example, 3310End of Term in the Future: <select this checkbox>End of Term Lapsed: <select this checkbox>Payment Period: for example, <Current Date to Current Date + 5 days>Payment Status: for example, 1Output Error Log: <select this checkbox>and choose Execute. | Review the payment schedules report.Make a note of the transaction number and payment date displayed for use in succeeding procedures. |  |

#### Corporate Initiated Payment

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
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

Each financial transaction contains flows that require payment. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows requiring a payment request. It does not create a posting in financial accounting,

When the payment is initiated by the financial partner, skip this procedure and next procedure Process Payment Request, and continue with the Bank Initiated Payment procedure.

|  |
| --- |
| Note A background job can be scheduled for this procedure. Please see the corresponding step in the Appendix. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Money Market: <select>Company code: for example 3310Transaction: <transaction number you noted down in previous step>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <Payment Date you noted down in previous procedure>Test Run: <select>Pay Only: <select this indicator> | The Payment Log - Test Run view displays, you review the payment information on this view.If message No flows exist for processing displays, then no payment with payment request are required for your selection criteria. When no flows exist, you can skip to next several procedures and go directly to the Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data:Test Run: <deselect>and choose Run. | The Payment Log screen is displayed. The payment request has been generated.Make a note of the key number displayed for use in succeeding procedures. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous procedure>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <Payment Date you noted down in previous procedure>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, change the following data, and choose Run:Test Run: <deselect> | The Payment Log screen is displayed. The payment request is generated.Note Make note of the key number displayed on this view for use in the following procedures. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests view displays. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests (F111) view, enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters view displays. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters view, enter the following data:Posting Date: for example, <current date>Next payment run on: for example <current date + 3 days>Company Code: for example 3310Payment Methods: <payment method for your country/region, for example,TF>Choose Dynamic selections, on the dialog box Free Selection for payment run, enter the following data and choose Save:Key number: <the key number you noted down in previous step>Choose Additional Log. On the Additional Log dialog box, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>If an Information dialog box displays Log created for all accounts, choose Continue.Choose Save on view Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests view. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediate. Choose Schedule Job to confirm this dialog box.Message Proposal is running displays in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, select Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests (F111) view, choose Menu > Environment > Payment Medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data and choose Run:Run Date: for example, <current date>Identification: for example TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

##### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

#### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by a bank, it is not necessary to run the previous Generate Payment Request and Process Payment Request steps.

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

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps that are available for posting flows:

- Fix, Pay and Post Flows (TBB1): You use this app to generate the posting for incoming payment.

|  |
| --- |
| Caution When using Fix, Pay and Post Flows (TBB1) for this procedure, no posting for outgoing payment is created for any if the payment was processed in the previous Generate Payment Request step with the Pay Only option. |

- Process Business Transactions: You use this app to generate the posting for outgoing payment that you processed in the previous Generate Payment Request step with the Pay Only option.

|  |
| --- |
| Note You can schedule a background job for this step, please see the corresponding step in the Appendix. |

Prerequisite

The outgoing payment which should be handled via payment request for this transaction has been processed in the previous Generate Payment Request step with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data:Money Market: <select this checkbox>Company code: for example, 3310Transaction: <transaction number you noted down in previous step>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, Payment Date you noted down in previous stepTest Run: <select this checkbox>Post Operational Only: <select this indicator>and choose Execute. | The Posting Log: Posted Business Transactions view displays,.Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting is created because this is test run.If No flows exist for processing notification displays, then there is no posting required for your selection criteria. Skip the following step and continue with the test step 5, using the Process Business Transactions app. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data:Test Run: <deselect this checkbox>and choose Execute | The Posting Log: Posted Business Transactions view displays. The accounting document is created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori App | Return Home and open Process Business Transactions (TPM10). | The Process Business Transactions view displays. |  |
| 6 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select this checkbox>Company Code: for example 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>Under the OTC Transactions screen group:Transaction: <transaction number you noted down in previous procedureTest Run: <select this checkbox>and choose Execute. | The Test Run: Post/Reverse Business Transactions view displays.If You have not selected any business transactions notification displays, then there is no posting required for your selection criteria and you can skip the current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Test Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions view displaysReview the simulated posting information for local GAAP (valuation area AE0) on this view.Note No posting created because this is a test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions view, change the following data:Test Run: <deselect this checkbox>and choose Execute. | The Update Run: Post/Reverse Business Transactions view displays. |  |
| 9 | Production Run | Choose Select All and choose Choose Those to Post, and then choose Execute.When the Update Run: Display Posted/Reversed Business Transactions view displays, choose Log and Messages. | The Posting Log: Posted Business Transactions view displays. The accounting document is created for outgoing payment in local GAAP (valuation area AE0). |  |

### Nominal Amount Adjustment

Purpose

This section describes the process of nominal amount adjustment for the Current Account-Style Instrument as an example.

#### Adjust Nominal Amount

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you adjust the nominal amount of a Current Acct-Style Instrument transaction as an example.

|  |
| --- |
| Note The nominal amount adjustment function is applicable to product type 51A (Fixed-Term Deposit), 55A (Interest Rate Instrument) and 58A (Current Acct-Style Instrument). For 51A and 55A, the balance of the transaction must be positive after the new nominal flow is added. For 58A, the balance of the transaction could be changed to the opposite after the new nominal flow is added. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Go:Key Date: <the current date>Company Code: for example, 3310Transaction: <the money market transaction you want to change the nominal amount>Term End: <delete the default value> | The transactions you selected are displayed. |  |
| 4 | Change the transaction | Select the transaction that you want to adjust the nominal amount and choose Edit. | The Change Current Acct-Style Instrument: Structure view displays. |  |
| 5 | Add new flow | Select the Other Changes in Cap.Struct. button, beside the Amount field, and insert the following data in dialog box:Flow Type: for example, for 58A, 1101 for Nominal Amount Increase or 1111 for Nominal Amount Decrease; for 51A or 55A, 1100 for Nominal Amount Increase or 1110 for Nominal Amount DecreasePayment Amount: for example, 11MPayment Date: for example, <Current Date + 1 Month>Calculation Date: for example, <Current Date + 1 Month>choose Copy and then choose Save.Caution Only one nominal change per day. | Current acct-style instrument was changed, new cash flow was added.Note If the additional flow direction is opposite and the Payment Amount is greater than original amount, the position will be switched from Asset to Liability. |  |

#### Corporate Initiated Payment

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

##### Option 2: Generate and Process Payment Request

###### Generate Payment Request

Purpose

In the case of nominal amount increase, you can use the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create payment request for the outflow which requires payment request. It will not create a posting in financial accounting.

In the case of nominal amount decrease where no payment request is needed, you can skip the current step and the next step, and continue from the Bank Initiated Payment step.

|  |
| --- |
| Note You can also schedule a background job for this procedure. Please see the corresponding step in the Appendix section. |

Procedure

Please refer to the Generate Payment Request procedure in the Principal Payment section.

###### Process Payment Request

Purpose

In this step, you use the Automatic Payment Transactions for Payment Requests (F111) app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items), but on payment requests.

Prerequisites

A payment request has been generated in the previous step.

Procedure

Please refer to the Process Payment Request step in the Principal Payment section.

##### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

#### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by the bank, it is not necessary to run the previous steps Generate Payment Request and Process Payment Request.

Procedure

This step doesn't require any operation in the system.

#### Post to General Ledger

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps are available for posting flows:

- Fix, Pay and Post Flows (TBB1): you use this app to generate the posting for incoming payment. Please note, this app will not create posting for outgoing payment which has been processed in the previous Generate Payment Request step with the Pay Only option.
- Process Business Transactions (TPM10): You use this app to generate the posting for outgoing payment which has been processed in the previous step Generate Payment Request with the Pay Only option.

|  |
| --- |
| Note You can schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Please refer to the Post to General Ledger procedure in the Principal Payment section.

### Reclassification

#### Display Maturity Statistics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the remaining term of debt or investment deals. You can find transactions with maturity less than one year, before you reclassify them from long term to short term in the next step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | On the Manage Financial Transactions screen, enter the following data, and choose Go:Key Date: for example, <last date of the current month>Company Code: for example, 3310Product Type: <enter a money market product type, for example, 55A> | The transactions falling in the selection criteria are displayed. |  |
| 4 | Note Down the Transactions Number | Go to the Term End field, and check for transactions that mature within one year. | Make a note of the transaction numbers to reclassify them from long term to short term. |  |

#### Reclassify from Long Term to Short Term (Valuation Class Transfer)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you transfer the valuation class of a transaction with maturity less than one year from long term to short term, which is reflected in financial accounting.

Prerequisite

The transaction matures within one year, and still has positive position value.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Execute Valuation Class Transfer (TPM15M). | The Valuation Class Transfer screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Valuation Class Transfer view, enter the following data, and choose Execute:OTC Transactions: <select this checkbox>Company Code: for example 3310Transaction: <transactions noted in previous procedure>General Valuation Class (in subarea Specific Selection for Outgoing Position): <select this indicator>Key Date: for example <last date of next month>Test Run: <select this checkbox> | The Edit Selected Positions screen is displayed. |  |
| 4 | Execute Test Run and Check Result | On the Edit Selected Positions view, select the transactions you want to transfer and enter the new General Valuation Class in the New Valuation Class field.Note Rule of new General Valuation Class:Switch the first digit of original General Valuation Class from 1 (long term) to 2 (short term), for example, if the original General Valuation Class is 11, then the new General Valuation Class is 21.Choose Execute. | The Test Run: Transfer view displays, |  |
| 5 | Review Logs | Choose Messages and Log.In the Information Overview dialog box, choose Posting Log.In the Posting Log: Posted Business Transactions view, review the simulated postings. | Logs are reviewed. |  |
| 6 | Production Run | Go back to the initial view of this app. Deselect the Test Run checkbox and repeat the previous steps for production run. | Production run succeeds, postings are created. |  |

### Terminate Deposit at Notice

Purpose

This section describes activities for deposit at notice termination.

#### Give Notice to Deposit at Notice

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you give notice to Deposit at Notice.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Manage Financial Transactions screen, enter the following data, and choose Go:Key Date: <the current date>Company Code: for example, 3310Transaction: <the deposit at notice transaction you created and what to give notice>Term End: <delete the default value> | The Deposit at Notice you select is displayed. |  |
| 4 | Set to Terminate Status | Select the Deposit at Notice to terminate and then choose Give Notice. | The Give Notice on Deposit at Notice screen is displayed. |  |
| 5 | Set Notice Date | On the Give Notice on Interest Rate Instr. screen, enter the following data, and choose Save:Notice: for example, <the current date> | The deposit at notice changed notification displays. |  |

### Transaction is Premature

Purpose

This section describes activities when Transaction is set to Premature.

#### Maintain Early Repayment for Premature Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

According to your business requirements, you may need to conclude a transaction before the agreed end date. In this step, you end a transaction before the end date specified in the contract, by modifying the end date of the transaction, maintaining accrued interest rate that is aligned with your counterparty, and create an early repayment for the new end date.

|  |
| --- |
| Note Currently, only transaction of Interest Rate Instrument can be premature, and the interest payment frequency of the transaction should be At End of Term. |

Prerequisites

You have already settled the transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Manage Financial Transactions screen, enter the following data, and choose Go:Key Date: <the current date>Company Code: for example, 3310Transaction: <the transaction you want to premature>Term End: <delete the default value> | The transaction you selected displays. |  |
| 4 | Change the Transaction | Select the transaction to set to premature and choose Edit. | The Change Interest Rate Instrument: Structure screen is displayed. |  |
| 5 | Add Accrued Interest | On the Change Interest Rate Instrument: Structure view, choose Conditions in menu barOn the new Overview of Conditions view, first select the line item of Nominal interest. From the drop-down list of Create icon (next to the Delete icon), choose Create Accrued Int. Cond..Enter the following data in Condition Details view:Percentage Rate: for example, 6and choose Back twice.Note During early repayment, all unpaid interest is recalculated based on the accrued interest rate. |  |  |
| 6 | Add New Flow | On the Change Interest Rate Instrument: Structure view, select the Other Changes in Cap.Struct. button, which is beside the Amount field.In the Change Interest Rate Instrument: Other Changes in Cap. Struct screen, enter the following data in the dialog box:Flow Type: for example, 1112 for Accrued DecreasePayment Amt: for example, <Same amount of Principal Increase>Payment Date: for example, <same as the new end date>Calculation Date: for example, <Same as the new end date>and choose Copy and then choose Save. | The Interest Rate Instrument is changed, and a new cash flow is added. |  |

#### Corporate Initiated Payment

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Money Market: <select this checkbox>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Money Market: <select this checkbox>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
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

Premature Transaction contains early repayment flows requiring payment. When creating the transaction, the payment request is selected as required (usually only for outgoing payments). The treasury back office uses the Pay Only functionality in the Post Flows/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows requiring a payment request. The request does not create posting in financial accounting,

When the payment is initiated by the financial partner, skip this procedure and next procedure Process Payment Request, and continue with the Bank Initiated Payment procedure.

|  |
| --- |
| Note A background job can be scheduled for this procedure. Please see the corresponding step in the Appendix. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data:Money Market: <select>Company code: for example 3310Transaction: <transaction number with outflows which you created in the previous procedures>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>Test Run: <select>Pay Only: <select this indicator>and choose Run. | The Payment Log - Test Run view displays, you review the payment information on this view.If message No flows exist for processing displays, then no payment with payment request are required for your selection criteria. When no flows exist, you can skip to next several procedures and go directly to the Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data:Test Run: <deselect>and choose Run. | The Payment Log screen is displayed. The payment request is generated.Make a note of the key number displayed on this view. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous procedure>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <current date>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, change the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. A payment request is generated.Note Make note of the key number displayed on this view for use in the following procedures. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Automatic Payment Transactions for Payment Requests (F111) SAP Fiori app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items), but on payment requests.

Prerequisite

Payment request has been generated in the previous procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests view displays. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests view, enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters view displays. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters view, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 3 days>Company Code: for example, 3310Payment Methods: for example, TChoose Dynamic selections, on the dialog box Free Selection for payment run, enter the following data and choose Save:Key number: <the key number you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>If information Log created for all accounts displays, choose Continue.Choose Save on view Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on view Automatic Payment Transactions for Payment Requests. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat, and choose Schedule Job to confirm this dialog box.Message Proposal is running displays in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests (F111) view, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data and choose Run:Run Date: for example <current date>Identification: for example TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78) . |  |

##### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

#### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by bank, it is not necessary to run the previous Generate Payment Request for Premature Transaction procedure.

Procedure

This step doesn't require any system operation.

#### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionality, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): You use this app to generate the posting for incoming payment. When using this app in the current step, it will not create posting for outgoing payments which have been processed in the previous Generate Payment Request for Premature Transaction procedure with the Pay Only option.
- Fix, Post, Reverse Business Transactions: You use this app to generate the posting for outgoing payments that have been processed in the previous Generate Payment Request for Premature Transaction procedure with the Pay Only option.

|  |
| --- |
| Note A background job can be scheduled for this step. Please see the corresponding step in the Appendix. |

Prerequisites

If there is an outgoing payment request for the transaction, it was previously processed in the Generate Payment Request for Premature Transaction procedure with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data:Money Market: <select this checkbox>Company Code: for example 3310Transaction: transaction number with inflow which was created in previous stepsUp to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, prematurity dateTest Run: <select this checkbox>Post Operational Only: <select this indicator>and choose Execute. | The Posting Log: Posted Business Transactions view is displayed.You review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created with a test run.If No flows exist for processing notification displays, no posting is required for your selection criteria. Skip the current test step and continue with the step 5 that uses the Fix, Post, Reverse Business Transactions SAP Fiori app. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data:Test Run: <deselect this checkbox>and choose Execute. | The Posting Log: Posted Business Transactions view is displayed. The accounting document is created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access Another SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions view is displayed. |  |
| 6 | Enter Selection Criteria for Test Run | Enter the following data:OTC Transactions: <select this checkbox>Company Code: for example 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>Under the OTC Transactions screen group:Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select this checkbox>and choose Execute. | The Test Run: Post/Reverse Business Transactions view is displayed.If the You have not selected any business transactions notification displays, no posting is required for your selection criteria and you can skip the current step. |  |
| 7 | Check Test Run Result | Choose Select All and choose Choose Those to Post, and then choose Execute.In theTest Run: Display Posted/Reversed Business Transactions view, choose Log and Messages. | ThePosting Log: Posted Business Transactions view displays.Review the simulated posting information for local GAAP (valuation area AE0) on this view.Note There is no posting created during a test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions view, change the following data:Test Run: <deselect this checkbox>and choose Execute. | The Update Run: Post/Reverse Business Transactions view is displayed. |  |
| 9 | Production Run | Choose Select All and choose Choose Those to Post, and then choose Execute.In the Update Run: Display Posted/Reversed Business Transactions view, choose Log and Messages. | The Posting Log: Posted Business Transactions view is displayed.An accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Post Realized Profit and Loss

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you fix and post derived business transactions (usually, realized profit and loss when the deal is mature).

|  |
| --- |
| Note A background job can be scheduled for this step. Please see the corresponding step in the Appendix. |

Prerequisites

The maturity date of transaction has been reached, and the financial transaction has been created, settled, and posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions view is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data:OTC Transactions: <select this checkbox>Company Code: for example 3310Valuation Area: for example AE0OTC Transactions: transaction numbers that are prematureTRL Date: prematurity date of transactionTest Run: <select this checkbox>and choose Execute.Confirm the Are you sure that you want to select future business transactions notification by choosing Enter. | New view Fix and Post Derived Business Transactions is displayed.If the No scheduled derived business transactions were found for the selection notification displays, there is no derived transaction available for your selection and you can skip the current step. |  |
| 4 | Fix and Post for Test Run | On the Fix and Post Derived Business Transactions view, choose Fix. | The Posting Log: Posted Business Transactions view is displayed.Review the simulated posting information for local GAAP (valuation area AE0).Note No posting created for a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back to return to the initial view of this app. Enter the following data:Test Run: <deselect this checkbox>and then choose Execute.Confirm the Are you sure that you want to select future business transactions notification by choosing Enter. | The Fix and Post Derived Business Transactions view is displayed. |  |
| 6 | Fix and Post for Production Run | On the Fix and Post Derived Business Transactions view, choose Fix. | The Posting Log: Posted Business Transactions view displays.Review the posting information for local GAAP (valuation area AE0) in this view.An accounting document has been created in local GAAP (valuation area AE0). |  |

### Transaction is Mature

Purpose

This section describes activities when Transaction is Mature.

#### Corporate Initiated Payment

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, enter the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item: Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by choosing Display payment log. |  |

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

Each financial transaction contains flows that require payment. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment). The treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows requiring a payment request. It does not create a posting in financial accounting.

When the payment is initiated by the financial partner, skip this procedure and next procedure Process Payment Request, and continue with the Bank Initiated Payment procedure.

|  |
| --- |
| Note A background job can be scheduled for this procedure. Please see the corresponding step in the Appendix. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Money Market: <select>Company code: for example 3310Transaction: <transaction number with outflows which you created in the previous procedures>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>Test Run: <select>Pay Only: <select this indicator> | The Payment Log - Test Run view displays, you review the payment information on this view.If message No flows exist for processing displays, then no payment with payment request are required for your selection criteria. When no flows exist, you can skip to next several procedures and go directly to the Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run :Test Run: <deselect> | The Payment Log screen is displayed. The payment request has been generated.Make a note of the key number displayed on this view. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Money Market: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous procedure>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date when the flow of financial transaction should be posted>, for example, <current date>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, change the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. The payment request is generated.Note Make note of the key number displayed on this view for use in the following procedures. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Automatic Payment Transactions for Payment Requests (F111) SAP Fiori app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items), but on payment requests.

Prerequisite

Payment request has been generated in the previous procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests view displays. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests view, enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters view displays. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters view, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 3 days>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free Selection for payment run, enter the following data and choose Save:Key number: <the key number you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select this checkbox>Due date check: <select>If information Log created for all accounts displays, choose Continue.Choose Save on view Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on view Automatic Payment Transactions for Payment Requests. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat, and choose Schedule Job to confirm this dialog box.Message Proposal is running displays in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests view, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data and choose Run:Run Date: for example <Current date>Identification: for example TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

##### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Table assigns Give Notice to Deposit at Notice to Treasury Specialist - Back Office and Adjust Nominal Amount to Front Office, both via Process MM Transactions - Collective Processing (TM00); the test procedures use Front Office for Give Notice, Back Office for Adjust Nominal Amount, and Manage Financial Transactions (F6157) as the app. Manual settlement likewise lists TM00 in the table but F6157 in the procedure.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/test-script-debt-and-investment-management-1wv-ae-sap-s-4hana-cloud-pu-part-02]]
- related-to :: [[05-treasury-and-cash-management/test-script-debt-and-investment-management-group-ledger-ifrs-1x7-ae-77]]
- related-to :: [[05-treasury-and-cash-management/test-script-debt-and-investment-management-group-ledger-us-gaap-34c-ae]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1WV_S4CLD2608_BPD_EN_AE.docx` — lines 1–3001 of the extracted text · extracted with `mammoth` · 396,646 chars in the whole document
