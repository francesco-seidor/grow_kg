---
id: 05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-01
title: Bond Management (3WY_AE) Test Script - SAP S/4HANA Cloud Public Edition 2608 (3WY_S4CLD2608_BPD_EN_AE) — part 1 of 2
description: "SAP test script for Bond Management (3WY_AE, UAE/AED, company code 3310): bond issuance and investment, payments, correspondence, postings, period-end, in Fiori apps."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/bond-management]
aliases: []
keywords: [Bond Management, bond issuance, bond investment, security classes, securities accounts, securities transactions, business partner setup, correspondence processing, payment requests, general ledger posting]
sources: ["raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3WY_S4CLD2608_BPD_EN_AE.docx#lines-1-2911"]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-981
topic: 05-treasury-and-cash-management/bond-management
language: EN
part: 1/2
created: 2026-10-12
updated: 2026-10-12
---

# Bond Management (3WY_AE) Test Script - SAP S/4HANA Cloud Public Edition 2608 (3WY_S4CLD2608_BPD_EN_AE) — part 1 of 2

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3WY_S4CLD2608_BPD_EN_AE.docx`, part 1 of 2 (lines 1–2911 of the extracted text), extracted with `mammoth`. Grouped under **Bond Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Bond Management (3WY_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Bond Management (3WY_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 7](#_Toc232853813)

[2 Prerequisites 8](#_Toc232853814)

[2.1 System Access 8](#_Toc232853815)

[2.2 Roles 8](#_Toc232853816)

[2.3 Master Data, Organizational Data, and Other Data 9](#_Toc232853817)

[2.4 Business Conditions 10](#_Toc232853818)

[2.5 Preliminary Steps 11](#_Toc232853819)

[2.5.1 Create Business Partner 11](#_Toc232853820)

[2.5.1.1 Create Business Partner - Counterpart/Depository Bank 11](#_Toc232853821)

[2.5.1.1.1 Maintain General Data for Business Partner 11](#_Toc232853822)

[2.5.1.1.2 Maintain Payment Details for Business Partner 13](#_Toc232853823)

[2.5.1.1.3 Maintain Authorizations for Business Partner 16](#_Toc232853824)

[2.5.1.1.4 Maintain Reporting Data in Company Code for Business Partner 17](#_Toc232853825)

[2.5.1.1.5 Maintain Additional Business Partner Roles 18](#_Toc232853826)

[2.5.1.2 Create Business Partner - Bond Issuer 19](#_Toc232853827)

[2.5.1.2.1 Maintain General Data for Business Partner 19](#_Toc232853828)

[2.5.1.2.2 Maintain Reporting Data in Company Code for Business Partner 21](#_Toc232853829)

[2.5.2 Correspondence 22](#_Toc232853830)

[2.5.2.1 Maintain Profile and BP Group Assignments to Internal Recipient 22](#_Toc232853831)

[2.5.2.2 Maintain Profile and BP Group Assignments to External Recipient 24](#_Toc232853832)

[2.5.3 Maintaining Credit Limit 26](#_Toc232853833)

[2.5.3.1 Maintain Limit with Limit Type Y01 26](#_Toc232853834)

[2.5.3.2 Maintain Limit with Limit Type Y07 27](#_Toc232853835)

[2.5.4 Maintain Trader and Trader Authorizations 29](#_Toc232853836)

[2.5.4.1 Define Traders 29](#_Toc232853837)

[2.5.4.2 Define User Data 29](#_Toc232853838)

[2.5.4.3 Maintain Trader Authorizations 30](#_Toc232853839)

[3 Overview Table 32](#_Toc232853840)

[4 Test Procedures 39](#_Toc232853841)

[4.1 Bond Issuance 39](#_Toc232853842)

[4.1.1 Analyze Cash Position 39](#_Toc232853843)

[4.1.2 Analyze Liquidity Forecast 39](#_Toc232853844)

[4.1.3 Start Public Offering or Private Placement Process 40](#_Toc232853845)

[4.1.4 Create Security Account for Issuance 40](#_Toc232853846)

[4.1.5 Create Security Class for Issued Bond 42](#_Toc232853847)

[4.1.5.1 Create Security Class for Issued Fixed-Rate Bond 42](#_Toc232853848)

[4.1.5.2 Create Security Class for Issued Floating-Rate Bond 44](#_Toc232853849)

[4.1.6 Create Placement Transaction 51](#_Toc232853850)

[4.1.6.1 Create Placement Transaction for Fixed-Rate Bond 51](#_Toc232853851)

[4.1.6.2 Create Placement Transaction for Floating-Rate Bond 53](#_Toc232853852)

[4.1.7 Correspondence 55](#_Toc232853853)

[4.1.7.1 Set Settlement Status (Manually) 55](#_Toc232853854)

[4.1.7.2 Correspondence with PDF Form 56](#_Toc232853855)

[4.1.7.2.1 Send Confirmation Email/Print 57](#_Toc232853856)

[4.1.7.2.2 Check Correspondence Status 57](#_Toc232853857)

[4.1.7.2.3 Receive Incoming Confirmation 59](#_Toc232853858)

[4.1.7.2.4 Find Deal and Match Deal Details 59](#_Toc232853859)

[4.1.7.2.5 Set Settlement Status 61](#_Toc232853860)

[4.1.8 Corporate Initiated Payment 62](#_Toc232853861)

[4.1.8.1 Option 1: Generate and Automatically Process Payment Request 62](#_Toc232853862)

[4.1.8.1.1 Process the Payment with the ‘Auto. Payment Run’ Function 62](#_Toc232853863)

[4.1.8.2 Option 2: Generate and Process Payment Request 66](#_Toc232853864)

[4.1.8.2.1 Generate Payment Request 66](#_Toc232853865)

[4.1.8.2.2 Process Payment Request 68](#_Toc232853866)

[4.1.8.3 Send Payment Medium File 70](#_Toc232853867)

[4.1.9 Bank Initiated Payment 71](#_Toc232853868)

[4.1.10 Post to General Ledger 71](#_Toc232853869)

[4.1.11 Post Issuance Cost Manually 73](#_Toc232853870)

[4.1.12 Period-end Closing 75](#_Toc232853871)

[4.1.12.1 Import Securities Price 75](#_Toc232853872)

[4.1.12.2 Import Reference Interest Rate 75](#_Toc232853873)

[4.1.12.3 Perform Key Date Valuation 76](#_Toc232853874)

[4.1.13 Interest rate fixing date 78](#_Toc232853875)

[4.1.13.1 Import Reference Interest Rate 78](#_Toc232853876)

[4.1.13.2 Update Planned Records for Securities 78](#_Toc232853877)

[4.1.14 Coupon Date 79](#_Toc232853878)

[4.1.14.1 Post Outgoing Interest Payment 79](#_Toc232853879)

[4.1.14.2 Process Payment Request 81](#_Toc232853880)

[4.1.14.3 Send Payment Medium File 83](#_Toc232853881)

[4.1.15 Reclassification 84](#_Toc232853882)

[4.1.15.1 Perform Valuation Class Transfer 84](#_Toc232853883)

[4.1.16 Unscheduled Redemption 86](#_Toc232853884)

[4.1.16.1 Create Redemption Transaction 86](#_Toc232853885)

[4.1.16.2 Set Settlement Status 87](#_Toc232853886)

[4.1.16.3 Corporate Initiated Payment 88](#_Toc232853887)

[4.1.16.3.1 Option 1: Generate and Automatically Process Payment Request 89](#_Toc232853888)

[4.1.16.3.2 Option 2: Generate and Process Payment Request 92](#_Toc232853889)

[4.1.16.3.3 Send Payment Medium File 96](#_Toc232853890)

[4.1.16.4 Bank Initiated Payment 97](#_Toc232853891)

[4.1.16.5 Post to General Ledger 97](#_Toc232853892)

[4.1.17 Scheduled Repayment Date 100](#_Toc232853893)

[4.1.17.1 Post Scheduled Principal Repayment 100](#_Toc232853894)

[4.1.17.2 Process Payment Request 101](#_Toc232853895)

[4.1.17.3 Send Payment Medium File 103](#_Toc232853896)

[4.2 Bond Investment 104](#_Toc232853897)

[4.2.1 Open Security Account 104](#_Toc232853898)

[4.2.1.1 Create Security Account for Investment 104](#_Toc232853899)

[4.2.2 Create Security Class 106](#_Toc232853900)

[4.2.2.1 Create Security Class for Invested Fixed-Rate Bond 106](#_Toc232853901)

[4.2.2.2 Create Security Class for Invested Floating-Rate Bond 108](#_Toc232853902)

[4.2.2.3 Create Security Class for Invested Zero-Coupon Bond 115](#_Toc232853903)

[4.2.2.4 Create Security Class for Invested Unit-Quoted Bond 117](#_Toc232853904)

[4.2.2.5 Create Security Class for Invested Index-Linked Bond 119](#_Toc232853905)

[4.2.3 Import Securities Price 121](#_Toc232853906)

[4.2.4 Analyze Cash Position 122](#_Toc232853907)

[4.2.5 Analyze Liquidity Forecast 122](#_Toc232853908)

[4.2.6 Check Limit Utilization Report 122](#_Toc232853909)

[4.2.7 Create Bond Purchase Transaction 123](#_Toc232853910)

[4.2.7.1 Create Bond Purchase Order 123](#_Toc232853911)

[4.2.7.2 Execute Bond Purchase Order 125](#_Toc232853912)

[4.2.7.3 Waiver Bond Purchase Order 126](#_Toc232853913)

[4.2.7.4 Create Fixed-Rate Bond Purchase Transaction 128](#_Toc232853914)

[4.2.7.5 Create Floating-Rate Bond Purchase Transaction 129](#_Toc232853915)

[4.2.7.6 Create Zero-Coupon Bond Purchase Transaction 131](#_Toc232853916)

[4.2.7.7 Create Unit-Quoted Bond Purchase Transaction 133](#_Toc232853917)

[4.2.7.8 Create Index-Linked Bond Purchase Transaction 134](#_Toc232853918)

[4.2.8 Correspondence 136](#_Toc232853919)

[4.2.8.1 Set Settlement Status (Manually) 136](#_Toc232853920)

[4.2.8.2 Correspondence with PDF Form 137](#_Toc232853921)

[4.2.8.2.1 Send Confirmation Email/Print 138](#_Toc232853922)

[4.2.8.2.2 Check Correspondence Status 138](#_Toc232853923)

[4.2.8.2.3 Receive Incoming Confirmation 140](#_Toc232853924)

[4.2.8.2.4 Find Deal and Match Deal Details 140](#_Toc232853925)

[4.2.8.2.5 Set Settlement Status 142](#_Toc232853926)

[4.2.9 Corporate Initiated Payment 143](#_Toc232853927)

[4.2.9.1 Option 1: Generate and Automatically Process Payment Request 144](#_Toc232853928)

[4.2.9.1.1 Process the Payment with the ‘Auto. Payment Run’ Function 144](#_Toc232853929)

[4.2.9.2 Option 2: Generate and Process Payment Request 147](#_Toc232853930)

[4.2.9.2.1 Generate Payment Request 147](#_Toc232853931)

[4.2.9.2.2 Process Payment Request 149](#_Toc232853932)

[4.2.9.3 Send Payment Medium File 151](#_Toc232853933)

[4.2.10 Bank Initiated Payment 152](#_Toc232853934)

[4.2.11 Post to General Ledger 152](#_Toc232853935)

[4.2.12 Period-end Closing 154](#_Toc232853936)

[4.2.12.1 Import Securities Price 155](#_Toc232853937)

[4.2.12.2 Import Reference Interest Rate 155](#_Toc232853938)

[4.2.12.3 Perform Key Date Valuation 155](#_Toc232853939)

[4.2.13 Interest Rate/Index Value Fixing Date 157](#_Toc232853940)

[4.2.13.1 Import Reference Interest Rate 158](#_Toc232853941)

[4.2.13.2 Import Price Index Values 158](#_Toc232853942)

[4.2.13.3 Update Planned Records for Securities 159](#_Toc232853943)

[4.2.14 Coupon Date 159](#_Toc232853944)

[4.2.14.1 Recognize Interest Receivable 160](#_Toc232853945)

[4.2.14.2 Post Incoming Interest Payment 162](#_Toc232853946)

[4.2.15 Reclassification 164](#_Toc232853947)

[4.2.15.1 Perform Valuation Class Transfer 164](#_Toc232853948)

[4.2.16 Sell Bond before Maturity 165](#_Toc232853949)

[4.2.16.1 Create Bond Sale Transaction 165](#_Toc232853950)

[4.2.16.2 Set Settlement Status 167](#_Toc232853951)

[4.2.16.3 Corporate Initiated Payment 168](#_Toc232853952)

[4.2.16.3.1 Option 1: Generate and automatically process payment request 169](#_Toc232853953)

[4.2.16.3.2 Option 2: Generate and Process Payment Request 172](#_Toc232853954)

[4.2.16.3.3 Send Payment Medium File 176](#_Toc232853955)

[4.2.16.4 Bank Initiated Payment 177](#_Toc232853956)

[4.2.16.5 Post to General Ledger 177](#_Toc232853957)

[4.2.17 Repayment Date 179](#_Toc232853958)

[4.2.17.1 Recognize Redemption Receivable 180](#_Toc232853959)

[4.2.17.2 Post Incoming Principal Repayment 182](#_Toc232853960)

[4.3 Reports 183](#_Toc232853961)

[4.3.1 Define Financial Positions 183](#_Toc232853962)

[4.3.2 Financial Status (Book Value) 185](#_Toc232853963)

[4.3.3 Financial Status (Nominal Amount) 186](#_Toc232853964)

[4.3.4 Display Treasury Alerts - Posting 187](#_Toc232853965)

[4.3.5 Display Treasury Alerts- Settlement, Release and Payment 188](#_Toc232853966)

[4.3.6 Display Treasury Posting Journal 189](#_Toc232853967)

[4.3.7 Display Treasury Position Flows 190](#_Toc232853968)

[4.3.8 Display Treasury Position Values 191](#_Toc232853969)

[4.3.9 Treasury Position Analysis 192](#_Toc232853970)

[4.3.10 Display Securities Account Class Positions 192](#_Toc232853971)

[4.3.11 Analyze NPV 193](#_Toc232853972)

[4.3.12 Calculate Market Risk Key Figures 194](#_Toc232853973)

[5 Appendix 196](#_Toc232853974)

[5.1 Position Indicator 196](#_Toc232853975)

[5.1.1 Change Position Indicator 196](#_Toc232853976)

[5.2 Job Scheduling 197](#_Toc232853977)

[5.2.1 Generate Limit Utilizations 197](#_Toc232853978)

[5.2.2 Generate Payment Request 198](#_Toc232853979)

[5.2.3 Post Flows to General Ledger 201](#_Toc232853980)

[5.2.3.1 Template - Fix, Pay and Post Flows 201](#_Toc232853981)

[5.2.3.2 Template - Process Business Transactions 203](#_Toc232853982)

[5.2.4 Key Date Valuation 205](#_Toc232853983)

[5.2.5 Update Security Cash Flow 206](#_Toc232853984)

[5.2.6 Post Debit Position 208](#_Toc232853985)

[5.2.7 Calculate Market Risk Key Figures 210](#_Toc232853986)

[5.3 Output Management 212](#_Toc232853987)

[5.3.1 Output Parameter Determination 212](#_Toc232853988)

[5.3.2 Manage Output Items 215](#_Toc232853989)

[5.3.3 Maintain Print Queues 216](#_Toc232853990)

[5.3.4 Display Email Transmissions 217](#_Toc232853991)

[5.3.5 Maintain Email Template 218](#_Toc232853992)

[5.3.6 Maintain Form Template 219](#_Toc232853993)

[5.4 Reconciliation of External Securities Account Statements 221](#_Toc232853994)

[5.4.1 Create the Statements of External Securities Account 221](#_Toc232853995)

[5.4.2 Reconciliation of External Securities Account Statements 222](#_Toc232853996)

[5.5 Accounting 223](#_Toc232853997)

[5.5.1 Reverse Accrual 224](#_Toc232853998)

[5.5.2 Reverse Valuation 225](#_Toc232853999)

[5.5.3 Reverse Debit Position 227](#_Toc232854000)

[5.6 Market Risk Analyzer 228](#_Toc232854001)

[5.6.1 Manage Market Data Shift 228](#_Toc232854002)

[5.6.2 Maintain Scenarios 229](#_Toc232854003)

[5.6.3 Defining Report Layout for Calculate Market Risk Key Figures 230](#_Toc232854004)

[5.6.4 Manage Market Risk Key Figure Sets 233](#_Toc232854005)

[5.7 Credit Risk Analyzer 236](#_Toc232854006)

[5.7.1 Display Limit Overview 236](#_Toc232854007)

[5.8 Simulated Valuation 237](#_Toc232854008)

[5.8.1 Run Simulated Valuation 237](#_Toc232854009)

[5.8.2 Delete Simulated Valuation 239](#_Toc232854010)

[5.9 Security Account Transfer 240](#_Toc232854011)

[5.9.1 Security Account Transfer 240](#_Toc232854012)

## Purpose

Overview

The Bond Management process helps you to manage issued bonds and bond investments. You can automate labor-intensive processes, such as payment handling and accounting postings, giving you more time to focus on value-added activities. You can manage operational and accounting requirements. The process covers fixed-rate, floating-rate, and zero-coupon bonds.

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

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Currency | AED |  |  |
| Business Partner | 33537001 |  | Counterparty/Depository Bank |
| Business Partner | 33537003 |  | Issuer |
| Valuation Area | AE0 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Comment |
| --- | --- |
| 1XN - Market Rates Management – Manually via Upload | Must be run before this test script. Market data must be created. |
| J60 - Accounts Payable | Define payment medium format following the steps described under Prerequisites > Preliminary Steps > Define Payment Medium Format Variants (Optional) in the test script of J60. |

### Preliminary Steps

#### Create Business Partner

##### Create Business Partner - Counterpart/Depository Bank

###### Maintain General Data for Business Partner

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner view, choose Organization. | The Create Organization screen is displayed. |  |
| 4 | Enter Address Data | On the Create Organization view, enter the following data:Business Partner: for example, 33537001Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Bank 1 - SAMPLE BANKSalutation: for example, Bank 1Search Term 1/2: for example, Bank 1Street/House number: for example,Postal Code/City: for example,Ctry/Reg.: AELanguage: ENE-Mail: <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, <Dec 31 of the year 9999>and Save.Note Remain on this view for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to Change Mode | On the Display Organization33537001 details view, choose Switch Between Display and Change, and enter following data:Change in BP role: select TR0151 Counterparty | More counterparty related tabs, for example Legal Data, Rating display. |  |
| 6 | Enter Legal Data | On the Change Organization:33537001, new role Counterparty view, from the Navigation Menu, choose Legal Data from the dropdown menu and enter the following data:Country/Region: AEand choose Save.Note The navigation menu is on the right side of the view. It displays as … , and is next to the >),Note Remain in this view for subsequent steps. | The legal data is entered and saved.Change Organization: 33537001, new role Counterparty view displays. |  |
| 7 | Enter Payment Transaction Data | On Change Organization:33537001, new role Counterparty view, from the Navigation Menu, select Payment Transactions from the dropdown menu and enter following two rows of data:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, <bank key>Bank acct: for example, <bank account>IBAN: choose the IBAN button and choose Continue in the IBAN dialog box.Row 2:ID: for example, USD1C/R: for example, AEBank Key: for example, <bank key>Bank acct: for example, <bank account>IBAN: choose the IBAN button and then choose Continue on the IBAN dialog box.Now choose Save.Note If a dialog window of Information appears when you choose IBAN, choose Continue. | The Payment transaction data is entered and the Business Partner is saved. |  |

###### Maintain Payment Details for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the payment details for the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner view displays. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: view, choose Open BP, in the popup dialog box, enter following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: select TR0151 Counterpartyand choose Enter. | Change Organization: 33537001 , role Counterparty view displays. |  |
| 4 | Enter SI: Payment Details data | On Change Organization:33537001, role Counterparty, choose Company Code, and enter following data:Company Code: for example, 3310Choose ENTER and choose SI: Payment Details and enter the following four rows of data:Row 1:Currency: for example, AEDPay.Det.ID: for example, AEDIHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, <leave blank>Partner Bank: for example, BlankPayment Request: for example, <deselect>Payment Methods: for example, BlankRow 2:Currency: for example, AEDPay.Det.ID: for example, AEDOHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, 33537001Partner Bank: for example, AED1Payment Request: for example, <select>Payment Methods: for example, TRow 3:Currency: for example, USDPay.Det.ID: for example, USDIHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/ee: for example, BlankPayment Request: for example, DeselectPayment Methods: for example, <leave blank>Row 4:Currency: for example, USDPay.Det.ID: for example, USDOHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/Payee: for example, 33537001Partner Bank: for example, USD1Payment Request: for example, <select>Payment Methods: for example, FNote Remain in the view for subsequent steps.Note If a warning notification displays the following message:Business partner proposed as payer/payee (see long text). Display this message for this business partner again? choose No. | The SI: Payment Details data is entered. |  |
| 5 | Assign Payment details | From the last view of previous step,For AED,select the Checkbox for AEDAEDI. Choose Assign, in the Counterparty Change: Payment Details Assignment dialog box, and choose Select All Incoming.Now AEDI displays under PmntID-Inc. .Choose Continue to close the dialog box.Select the Checkbox for AEDAEDO.Choose Assign, in the Counterparty Change: Payment Details Assignment dialog box and choose Select All Outgoing.Now AEDO displays under P-ID Outg.Choose Continue to close the dialog box.Repeat for USD:USD I: PmntID-IncUSD O: P-ID Outg.On Change Organization:33537001, role Counterparty view, choose Save. | Payment details and the assignments are saved. |  |

###### Maintain Authorizations for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain the authorization data for the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen displays. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter following data:Business Partner: 33537001Choose Enter and choose Switch Between Display and Change, and enter the following data:Change in BP Role: select TR0151 Counterparty | Change Organization: 33537001 , role Counterparty screen displays. |  |
| 4 | Enter SI: Authorizations data | On the Change Organization: 33537001, role Counterparty screen, choose Company Code, choose SI: Authorizations, enter the following data and choose Save.Securities: select the Auth. checkboxNote You can also give authorization to a specific product type and transaction type by expending the folders. For testing purpose, we give all authorizations to all kinds of product types and transaction types. | The Authorizations data is saved. |  |

###### Maintain Reporting Data in Company Code for Business Partner

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
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen displays. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: choose TR0151 Counteparty | Change Organization: 33537001 , role Counterparty screen displays. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization: 33537001, role Counterparty screen, choose Company Code, choose Reporting Data in Company Code, and enter following data and choose save.Comp. Rel.: for example, 3 OtherNote If you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown Menu.Note Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itThey are used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

###### Maintain Additional Business Partner Roles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain an additional role for the business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change. | Change Organization: 33537001 screen is displayed. |  |
| 5 | Add New Role of TR0152 Depository Bank | Select Change in BP Role to: for example, TR0152 Depository BankChoose Save. | Data is saved. |  |

##### Create Business Partner - Bond Issuer

###### Maintain General Data for Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the process to maintain general data for Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner screen, choose Organization. | The Create Organization: screen is displayed. |  |
| 4 | Enter address data | On the Create Organization screen, enter the following entries and choose Save:Business Partner: for example, 33537003Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Bank 2 - SAMPLE BANKSalutation: for example, Bank 2Search Term 1/2: for example, Bank 2Street/House number: for example,Postal Code/City: for example,Country: AELanguage: ENE-Mail: for example, <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, Dec 31 of the year 9999Note Remain on this view for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to change mode | On the Display Organization33537003 screen, choose Switch Between Display and Change, and enter following data:Change in BP role: select TR0150 Issuer | More counterparty related tabs such as Legal Data, Rating show up. |  |
| 6 | Enter Legal data | On the Change Organization:33537003 screen, choose Legal Data in the dropdown list of Navigation Menu, enter the following data and choose Save:Country/Region: AENote The navigation menu is on the right side of the view. It displays as … , and is next to the >),Note Remain in this view for subsequent steps. | The Legal data is entered and saved.The Change Organization:33537003, role Counterparty screen is displayed. |  |

###### Maintain Reporting Data in Company Code for Business Partner

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner(BP): screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter following data:Business Partner: 33537003Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: choose TR0150 Issuer(defined) | Change Organization: 33537003 , role Issuer screen displays. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization:33537003, role Issuer screen, choose Company Code, and enter the following data:Company Code: for example, 3310Choose ENTER and choose Reporting Data in Company Code, and enter the following data and choose Save.Comp. Rel.: for example, 3 OtherIf you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown menu.Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itIt can be used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

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

The Internal Recipient ID is predefined by SAP. It could be linked to SAP User ID(s). Once it's linked to an SAP user ID, whenever an internal correspondence object is generated, SAP TRM will send correspondence information to the address of the SAP User ID. Depending on the different profiles (PR_EMAIL /PR_PRINT), email is sent to the user's email address or a form is printout.

This activity describes how to assign business partner profiles and BP groups to an internal business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign Profile and BP Group - Internal Recipients (FTR_INT_ASSIGN). | The Assignment of Profiles and BP Groups to Internal Recipients: view displays. |  |
| 3 | Enter Business partner data on the view | On the left side of Assignment of Profiles and BP Groups to Internal Recipients view, choose Insert Row and enter the following data, and then select the item by ticking the checkbox before:IntRec: for example, INT.RECPCoCd: for example, 3310Recpt/Send Type: for example, INTERNALCheckbox: <select> | The Business Partner information is entered. |  |
| 4 | Assign Business profile and BP group to the Business Partner | On the top-right side of Assignment of Profiles and BP Groups to Internal Recipients view, expend the node, and choose one item to maintain the business partner profile and business partner group, for example, Securities > Bond > 04A Bond > 100 Investment > 20 ContractThen on the bottom-right side of the screen,choose Insert Row, enter the following data, and choose SaveProfile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTUser Name: <select a User ID>.Choose Insert Row again and add another entry as following and choose Save:Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTUser Name: <select a User ID>.Note The user ID is a backend user ID. | Business partner profile and BP group and user ID are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat the previous step to assign BP profile and BP group to the rest of Product type/Transaction Type/Activity category | Check the item INT.RECP in the left side view, and choose Modify Row.Repeat the above step to maintain other items under the Bond folder.Product TypeTransaction TypeActivity Category04A1002004A2002004A3002004A40020 | BP profiles and BP groups and user IDs are assigned to all the listed Product Types/Transaction Types/ Activity Categories, |  |

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
| 4 | Assign Business profile and BP group to the Business Partner | On the top right side of the Assignment of Profiles and BP Groups to External Recipients screen, expand the node, and choose one item to maintain the business partner profile and business partner group, for example, Securities > Bond > 04A Bond > 100 Investment > 20 ContractThen on the bottom-right side of the screen, choose Insert Row and enter the following data:Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTChoose Insert Row again and add another entry as following data：Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTNote Normally you only assign one profile to a Product type/Transaction type/Activity Category. | Business partner profiles and BP groups are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat the previous step to assign BP profiles and BP groups to the rest of Product type/Transaction Type/Activity category | Check the item 33537001 in the left side view, and choose Modify Row.Repeat the above step to maintain other items under the Bond folder.04A1002004A2002004A3002004A40020 | For all the listed Product Types/Transaction Types/ Activity Categories, BP profiles and BP groups are assigned. |  |

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

In this step, you can define traders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Define Traders (S_ALR_87009302). | The Determine Work Area: Entry dialog displays |  |
| 3 | Enter Work Area | Enter data and select ContinueCompany Code: for example: 3310 | The Change View "Treasury: Traders": Overview screen displays. |  |
| 4 | Create a New Record | Select New Entries, enter data and select Save.Trader: for example: TRADER02 | The data is saved. |  |

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Define User Data (S_ALR_87007933). | The Change View "Treasury: User master data supplements": Overview screen displays |  |
| 3 | Create a New Record | Select New Entries, enter data and select Save.User name: for example: <Your user name>Trader: for example: TRADER02 | The data is saved. |  |

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
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Trader Authorizations (TBT1). | The Create/Change Trans. Authorization for Trader: Init. Screen displays. |  |
| 3 | Enter Selection Criteria | Enter data and select Enter.Trader: for example: TRADER02Company Code: for example: 3310 | The Create/Change Transaction Authorization for Traders screen displays. |  |
| 4 | Enter Authorization and Save | Select or unselect on the Authorization column and select Save.Note Make sure to authorize TRADER02 for the Securities transactions. | The data is saved as indicated by a message. For example: Transaction authorizations for trader TRADER02 are being saved. |  |

## Overview Table

The scope item consists of several process steps, reports, items provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Analyze Cash Position](#unique_24) [page ] 39 | Cash Manager | Cash Flow Analyzer (F2332) | Cash manager check the cash position status, and make decisions of right financial instruments for short-term purpose based on analysis of cash position. |
| [Analyze Liquidity Forecast](#unique_25) [page ] 39 | Cash Manager | Cash Flow Analyzer (F2332) | The cash manager check the liquidity forecast regularly and make decisions regarding medium-term or long-term financial instruments. |
| [Start Public Offering or Private Placement Process](#unique_26) [page ] 40 | N/A | N/A | This step is outside of SAP system |
| [Create Security Account for Issuance](#unique_27) [page ] 40 | Treasury Specialist - Back Office | Manage Securities Accounts (TRS_SEC_ACC) | Security Account is created. |
| [Create Security Class for Issued Fixed-Rate Bond](#unique_28) [page ] 42 | Treasury Specialist - Back Office | Manage Security Classes (F8717) | Security Class for Product Type 04A is created. |
| [Create Security Class for Issued Floating-Rate Bond](#unique_29) [page ] 44 | Treasury Specialist - Back Office | Manage Security Classes (F8717) | Security Class for Product Type 04A is created. |
| [Create Placement Transaction for Fixed-Rate Bond](#unique_30) [page ] 51 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A placement transaction is created. |
| [Create Placement Transaction for Floating-Rate Bond](#unique_31) [page ] 53 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A placement transaction is created. |
| [Set Settlement Status (Manually)](#unique_32) [page ] 55 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The transaction is settled manually. |
| [Process the Payment with the ‘Auto. Payment Run’ Function](#unique_33) [page ] 62 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_34) [page ] 66 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Post Issuance Cost Manually](#unique_35) [page ] 73 | Treasury Accountant | Create Manual Posting (FWBS) | Manual posting is generated. |
| [Process Payment Request](#unique_36) [page ] 68 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_37) [page ] 71 | N/A | N/A | This step is outside of SAP system |
| [Post to General Ledger](#unique_38) [page ] 71 | Treasury Accountant | Process Business Transactions (TPM10);Fix, Pay and Post Flows (TBB1) | Cash flows related FI document is posted. |
| [Import Securities Price](#unique_39) [page ] 75 | Treasury Specialist - Back Office |  | New security price is maintained. |
| [Perform Key Date Valuation](#unique_40) [page ] 76 | Treasury Accountant | Run Valuation (TPM1) | The screen Valuation Log displays, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. The accounting document has been created in local GAAP (valuation area AE0). |
| [Import Reference Interest Rate](#unique_41) [page ] 78 | Treasury Specialist - Back Office | Enter Interest Rates (JBIRMC) | This step is mentioned in Market Rates Management – Manually via Upload (1XN) test script. Reference interest rate is updated. |
| [Update Planned Records for Securities](#unique_42) [page ] 78 | Treasury Specialist - Back Office | Update Planned Records for Securities (FWUP) | Update was completed. |
| [Post Outgoing Interest Payment](#unique_43) [page ] 79 | Treasury Accountant | Execute Debit Position - Manual Debit Position (FWZE) | Payment request is generated. |
| [Process Payment Request](#unique_44) [page ] 81 | Treasury Accountant | Execute Debit Position - Manual Debit Position (FWZE) | Payment program for payment request processes. |
| [Perform Valuation Class Transfer](#unique_45) [page ] 84 | Treasury Accountant | Execute Valuation Class Transfer (TPM15M) | Valuation class transfer is executed from long term to short term, and reflected in financial accounting. |
| [Create Redemption Transaction](#unique_46) [page ] 86 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A redemption transaction is created. |
| [Set Settlement Status](#unique_47) [page ] 87 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The transaction is settled manually. |
| [Process the Payment with the ‘Auto. Payment Run’ Function](#unique_48) [page ] 89 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_49) [page ] 92 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_50) [page ] 94 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_51) [page ] 97 | N/A | N/A | This step is outside of SAP system |
| [Post to General Ledger](#unique_52) [page ] 97 | Treasury Accountant | Process Business Transactions (TPM10) | Cash flows related FI document is posted. |
| [Post Scheduled Principal Repayment](#unique_53) [page ] 100 | Treasury Accountant | Execute Debit Position - Manual Debit Position (FWZE) | Payment receivable is generated. |
| [Process Payment Request](#unique_54) [page ] 101 | Treasury Accountant | Automatic Payment Transactions for Payment Requests (F111) | Payment is generated. |
| [Create Security Account for Investment](#unique_55) [page ] 104 | Treasury Specialist - Back Office | Manage Securities Accounts (TRS_SEC_ACC) | Security Account is created. |
| [Create Security Class for Invested Fixed-Rate Bond](#unique_56) [page ] 106 | Treasury Specialist - Back Office | Manage Security Classes (F8717) | Security Class for Product Type 04A is created. |
| [Create Security Class for Invested Floating-Rate Bond](#unique_57) [page ] 108 | Treasury Specialist - Back Office | Manage Security Classes (F8717) | Security Class for Product Type 04A is created. |
| [Create Security Class for Invested Zero-Coupon Bond](#unique_58) [page ] 115 | Treasury Specialist - Back Office | Manage Security Classes (F8717) | Security Class for Product Type 04A is created. |
| [Create Security Class for Invested Unit-Quoted Bond](#unique_59) [page ] 117 | Treasury Specialist - Back Office | Manage Security Classes (F8717) | Security Class for Product Type 04A is created. |
| [Create Security Class for Invested Index-Linked Bond](#unique_60) [page ] 119 | Treasury Specialist - Back Office | Manage Securities Classes (FWZZ) | Security Class for Product Type 04A is created. |
| [Import Securities Price](#unique_61) [page ] 121 | Treasury Specialist - Back Office | Enter Securities Prices (FW17) | New security price is maintained. |
| [Analyze Cash Position](#unique_62) [page ] 122 | Cash Manager | Cash Flow Analyzer (F2332) | Cash manager check the cash position status, and make decisions of right financial instruments for short-term purpose based on analysis of cash position. |
| [Analyze Liquidity Forecast](#unique_63) [page ] 122 | Cash Manager | Cash Flow Analyzer (F2332) | The cash manager check the liquidity forecast regularly and make decisions regarding medium-term or long-term financial instruments. |
| [Check Limit Utilization Report](#unique_64) [page ] 122 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | Limit utilization report displays. |
| [Create Fixed-Rate Bond Purchase Transaction](#unique_65) [page ] 128 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A purchase transaction is created. |
| [Create Floating-Rate Bond Purchase Transaction](#unique_66) [page ] 129 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A purchase transaction is created. |
| [Create Zero-Coupon Bond Purchase Transaction](#unique_67) [page ] 131 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A purchase transaction is created. |
| [Set Settlement Status (Manually)](#unique_68) [page ] 136 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The transaction is settled manually. |
| [Process the Payment with the ‘Auto. Payment Run’ Function](#unique_69) [page ] 144 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_70) [page ] 147 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_71) [page ] 149 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_72) [page ] 152 | N/A | N/A | This step is outside of SAP system. |
| [Post to General Ledger](#unique_73) [page ] 152 | Treasury Accountant | Process Business Transactions (TPM10);Fix, Pay and Post Flows (TBB1) | Cash flows related FI document is posted. |
| [Import Securities Price](#unique_74) [page ] 155 | Treasury Specialist - Back Office | Enter Securities Prices (FW17) | New security price is maintained. |
| [Perform Key Date Valuation](#unique_75) [page ] 155 | Treasury Accountant | Run Valuation (TPM1) | The screen Valuation Log displays, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. The accounting document has been created in local GAAP (valuation area AE0). |
| [Import Reference Interest Rate](#unique_76) [page ] 158 | Treasury Specialist - Back Office | Enter Interest Rates (JBIRMC) | This step is mentioned in Market Rates Management - Manually via Upload(1XN) test script. Reference interest rate is updated. |
| [Update Planned Records for Securities](#unique_77) [page ] 159 | Treasury Specialist - Back Office | Update Planned Records for Securities (FWUP) | Update was completed. |
| [Recognize Interest Receivable](#unique_78) [page ] 160 | Treasury Accountant | Automatic Debit Position and Posting - Security Accounts (FWSO);Execute Debit Position - Manual Debit Position (FWZE) | Payment receivable is generated. |
| [Post Incoming Interest Payment](#unique_79) [page ] 162 | Treasury Accountant | Execute Debit Position - Manual Debit Position (FWZE) | Payment is generated. |
| [Perform Valuation Class Transfer](#unique_80) [page ] 164 | Treasury Accountant | Execute Valuation Class Transfer (TPM15M) | Valuation class transfer is executed from long term to short term, and reflected in financial accounting. |
| [Create Bond Sale Transaction](#unique_81) [page ] 165 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A sale transaction is created. |
| [Set Settlement Status](#unique_82) [page ] 167 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The transaction is settled manually. |
| [Process the Payment with the ‘Auto. Payment Run’ Function](#unique_83) [page ] 169 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_84) [page ] 172 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_85) [page ] 174 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_86) [page ] 177 | N/A | N/A | This step is outside of SAP system |
| [Post to General Ledger](#unique_87) [page ] 177 | Treasury Accountant | Process Business Transactions (TPM10);Fix, Pay and Post Flows (TBB1) | Cash flows related FI document is posted. |
| [Recognize Redemption Receivable](#unique_88) [page ] 180 | Treasury Accountant | Automatic Debit Position and Posting - Security Accounts (FWSO);Execute Debit Position - Manual Debit Position (FWZE) | Payment receivable is generated. |
| [Post Incoming Principal Repayment](#unique_89) [page ] 182 | Treasury Accountant | Execute Debit Position - Manual Debit Position (FWZE) | Payment is generated. |
| [Define Financial Positions](#unique_90) [page ] 183 | Treasury Accountant | Define Financial Positions (FTR_FP_DEF) | Financial Positions are defined. |
| [Financial Status (Book Value)](#unique_91) [page ] 185 | Treasury Accountant | Financial Status (F2136) | The financial status on book values displays. |
| [Financial Status (Nominal Amount)](#unique_92) [page ] 186 | Treasury Accountant | Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)) | The financial status on nominal amount displays. |
| [Display Treasury Alerts - Posting](#unique_93) [page ] 187 | Treasury Accountant | Display Treasury Alerts (F4984) | Treasury Alerts-Posting display. |
| [Display Treasury Alerts- Settlement, Release and Payment](#unique_94) [page ] 188 | Treasury Specialist - Back Office | Display Treasury Alerts - Settlement (F4979) | Treasury Alerts display. |
| [Display Treasury Posting Journal](#unique_95) [page ] 189 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Treasury posting journal displays. |
| [Display Treasury Position Flows](#unique_96) [page ] 190 | Treasury Specialist - Back Office | Display Treasury Position Flows (F1754) | Treasury posting flows display. |
| [Display Treasury Position Values](#unique_97) [page ] 191 | Treasury Accountant | Display Treasury Position Values (F1867) | Treasury position values display. |
| [Treasury Position Analysis](#unique_98) [page ] 192 | Treasury Accountant | Treasury Position Analysis | Treasury position analysis displays. |
| [Display Securities Account Class Positions](#unique_99) [page ] 192 | Treasury Accountant | Display Securities Account Class Positions (TPM40A) | Display Securities Account Class Positions display |
| [Analyze NPV](#unique_100) [page ] 193 | Treasury Specialist - Middle Office | Analyze NPV (JBRX) | The NPV Result displays. |
| [Calculate Market Risk Key Figures](#unique_101) [page ] 194 | Treasury Specialist - Middle Office | Calculate Market Risk Key Figures (AISGENKF) | The single value analysis of assigned report layout displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Bond Issuance

#### Analyze Cash Position

Purpose

At the end of the transaction day, the cash manager always reviews the cash position status for making decisions about the right financial instruments for short-term purposes, based on analysis of cash position.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) SAP Fiori app to analyze the cash position. For more information, please refer to the Basic Cash Operations(BFB) test script.

#### Analyze Liquidity Forecast

Purpose

The cash manager reviews the liquidity forecast regularly and makes decisions regarding medium-term or long-term financial instruments, such as, investment, loan, or foreign exchange.

Procedure

If cash management is implemented in your system, you use the Cash Flow Analyzer (F2332) app to analyze the liquidity forecast. For more information, see the Basic Cash Operations(BFB) test script.

#### Start Public Offering or Private Placement Process

Purpose

Bond can be issued in primary markets via a public offering or via private placement.

Procedure

You don't need to do any operation in system in this step.

#### Create Security Account for Issuance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A security in general, is usually purchased and maintained by a broker such as a bank or a securities company. The transactions involve opening a security account with the broker. The broker maintains positions by each of the securities account. In the system, the securities positions are also maintained on an account level. This procedure gives you detailed steps of how to create a security account.

Prerequisite

A Business Partner with TR0152 Depository Bank is created with ID 33537001.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Securities Accounts (TRS_SEC_ACC). | The Choose Securities Account and Company Code screen is displayed. |  |
| 3 | Enter Account Identifier | Enter a new unique identifier for the new Securities Account, and choose Create.Company Code: for example, 3310Securities Acct: for example, BOND_ISSUEInfoChoose Create if a confirmation dialog pops up.if above account is already created, you can choose Display or Change to either view or edit the account. | A new account is created. |  |
| 4 | Enter General Data of the Account | Enter the following data and move to the next tabSecurities Account ID: for example, BOND33537001AE0Securities Account Type: for example, SLC Issuance Securities Account | Move to next tab |  |
| 5 | Enter Bank Data | Enter below data and choose SaveDepository Bank: for example, 33537001Line 1:Payment Currency: AEDHouse Bank: AEBK1Account ID: AEAC1Payer: for example, 33537001Partner Bank: AED1Payment Request: <select>Payment Methods: TLine 2:Payment Currency: USDHouse Bank: AEBK1Account ID: USDACPayer: for example, 33537001Partner Bank: USD1Payment Request: <select>Payment Methods: T | The data is saved |  |

#### Create Security Class for Issued Bond

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The user needs to create a security class ID before creating any transaction on a security. This section introduces how to create a security class depending on different product types.

##### Create Security Class for Issued Fixed-Rate Bond

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.ID Number: for example, BD_AE1Product Type: for example, 04A | The New Object screen displays with previously specified ID Number. |  |
| 4 | Enter Header | On the tab Header, enter the following data:Security Class Name: for example, Fixed-Rate #1Gen. Sec. Classification: for example, BondBond Classification: for example, Senior SecuredStatus: for example, ActivePlease switch to the Basic Data tab. | The Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | On the tab Basic Data, enter the following data:Issuer: for example, 33537003Issue Currency: for example, AEDIssue Start: for example, <the first day of current month>Calculation: for example, <the first day of current month>Final Due Date: for example, <the first day of current month + 3 year>Quotation: for example, 1In the table Additional Identification Number, enter the following data:Secondary Index Number: for example, ISINSecondary Index Value: for example, XX0000000XX00Please switch to the Ratings tab. | The Ratings tab is displayed. |  |
| 6 | Enter Rating | On the tab Ratings, enter the following data:Rating Procedure: for example, 1_MoodyRating: for example, 1_A1Trend: for example, +Valid From Date: for example, <the first day of current month>Valid To Date: for example, <the first day of current month + 1 year>Please switch to the Condition tab. | The Condition tab is displayed. |  |
| 7 | Enter Condition | On the tab Condition, enter the following data:Interest Calculation Method: for example, 360/360Effective Interest Method: for example, 2Repayment Type: for example, Full repayment on maturityChoose Create in the table header of Condition Items. | The dialog​ New Object pops up. |  |
| 8 | Create Condition Items | On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 100Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 9 | Enter Details of Conditions - Int. (perc.-quoted) | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Interest Calculation Type: for example, Linear Interest CalculationPercentage Rate: for example, 3.0000000On the tab Dates, enter the following data:Calendar 1: for example, 01Calculation Date Frequency: for example, 1Calculation Date: for example, <the first day of next month>Calculation Date Included: for example, <deselected>Calculation Date Is Month-End Indicator: for example, <deselected>Due Date: for example, <the first day of next month>Due Date Is Month-End Indicator: for example, <deselected> |  |  |
| 10 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 263Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 11 | Enter Details of Conditions - Final repayment | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Currency: for example, AEDOn the tab Dates, enter the following data:Calendar 1: for example, 01Calculation date: for example, <the first day of current month + 3 years>Due date: for example, <the first day of current month + 3 years> |  |  |
| 12 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: for example, DFMCurrency: for example, AEDFlat Price: for example, <selected> | Security class is created. |  |

##### Create Security Class for Issued Floating-Rate Bond

Procedure

Option 1: IBOR is in use

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.ID Number: for example, BD_AE2Product Type: for example, 04A | The New Object screen displays with previously specified ID Number. |  |
| 4 | Enter Header | On the tab Header, enter the following data:Security Class Name: for example, Floating-Rate#2Gen. Sec. Classification: for example, BondBond Classification: for example, Senior SecuredStatus: for example, ActivePlease switch to the Basic Data tab. | The Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | On the tab Basic Data, enter the following data:Issuer: for example, 33537003Issue Currency: for example, AEDIssue Start: for example, <the first day of current month>Calculation: for example, <the first day of current month>Final Due Date: for example, <the first day of current month + 3 years>Quotation: for example, 1In the table Additional Identification Number, enter the following data:Secondary Index Number: for example, ISINSecondary Index Value: for example, XX0000000XX00Please switch to the Ratings tab. | The Ratings tab is displayed. |  |
| 6 | Enter Rating | On tab Ratings, enter the following data:Rating Procedure: for example, 1_MoodyRating: for example, 1_A1Trend: for example, +Valid From Date: for example, <the first day of current month>Valid To Date: for example, <the first day of current month + 1 year>Please switch to the Condition tab. | The Condition tab is displayed. |  |
| 7 | Enter Condition | On tab Condition, enter the following data:Interest Calculation Method: for example, 360/360Effective Interest Method: for example, 2Repayment Type: for example, Full repayment on maturityChoose Create in the table header of Condition Items. | The dialog​ New Object pops up. |  |
| 8 | Create Condition Items | On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 101Effective From: for example, <the first day of current month> | The Condition screen displays. |  |
| 9 | Enter Details of Conditions - Int. (perc.-quoted) | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Interest Calculation Type: for example, Linear Interest CalculationReference Interest Rate: for example, AEDM03EIBReference Interest Rate Operator: for example, +Percentage Rate: for example, 3.0000000On the tab Dates, enter the following data:Calendar 1: for example, 01Calculation Date Frequency: for example, 1Calculation Date: for example, <the first day of next month>Calculation Date Included: for example, <deselected>Calculation Date Is Month-End Indicator: for example, <deselected>Due Date: for example, <the first day of next month>Due Date Is Month-End Indicator: for example, <deselected> |  |  |
| 10 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 209Effective From: for example, <the first day of current month>Choose Apply in the Condition screen, and go back to main screen. |  |  |
| 11 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 263Effective From: for example, <the first day of current month> | The Condition screen displays. |  |
| 12 | Enter Details of Conditions - Final repayment | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Currency: for example, AEDOn the tab Dates, enter the following data:Calendar 1: for example, 01Calculation date: for example, <the first day of current month + 3 years>Due date: for example, <the first day of current month + 3 years> |  |  |
| 13 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: for example, DFMCurrency: for example, AEDFlat Price: for example, <selected> | Security class is created. |  |

Option 2: If you want to use SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.ID Number: for example, BD_AE2Product Type: for example, 04A | The New Object screen displays with previously specified Class ID. |  |
| 4 | Enter Header | On the tab Header, enter the following data:Security Class Name: for example, Floating-Rate#2Gen. Sec. Classification: for example, BondBond Classification: for example, Senior SecuredPlease switch to the Basic Data tab. | The Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | On tab Basic Data, enter the following data:Issuer: for example, 33537003Issue Currency: for example, AEDIssue Start: for example, <the first day of current month>Calculation: for example, <the first day of current month>Final Due Date: for example, <the first day of current month + 1 year>Quotation: for example, 1In the table Additional Identification Number, enter the following data:Secondary Index Number: for example, ISINSecondary Index Value: for example, XX0000000XX00Please switch to the Ratings tab. | The Ratings tab is displayed. |  |
| 6 | Enter Rating | On the tab Ratings, enter the following data:Rating Procedure: for example, 1_MoodyRating: for example, 1_A1Trend: for example, +Valid From Date: for example, <the first day of current month>Valid To Date: for example, <the first day of current month + 1 year>Please switch to the Condition tab. |  |  |
| 7 | Enter Condition | On the tab Condition, enter the following data:Interest Calculation Method: for example, act/360Effective Interest Method: for example, 2Repayment Type: for example, Full repayment on maturityChoose Create in the table header of Condition Items. | The dialog​ New Object pops up. |  |
| 8 | Enter Condition Items | On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 101Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 9 | Enter Details of Condition - Variable Interest | Make the following entries in screen Condition, then choose Apply:On the tab Amounts, enter the following data:Interest Calculation Type: for example, Compound Interest CalculationInterest Calculation Method: for example, act/360Reference Interest Rate: for example, SOFRNote If Compound Interest Calculation is selected, and you want a reference rate plus a spread, you should input value in following field:Reference Interest Rate Operator: for example, +Percentage Rate: for example, 1.0000000If Average Compound Interest Calculation is selected in field Interest Calculation Type, the following fields under group Average Interest Rate are displayed.Weighting: for example, LAvg. Interest Rate Rounding Decimal: for example, 4Spread: for example, 1.0000000000Set Upper Limit: for example, <selected>Upper Limit: for example, 2.0000000000Set Lower Limit: for example, <selected>Lower Limit: for example, 0.5000000000On the tab Dates, enter the following data:Calendar 1: for example, 01Calculation Date Frequency: for example, 1Calculation Date: for example, <the first day of next month>Calculation Date Included: for example, <deselected>Calculation Date Is Month-End Indicator: for example, <deselected>Due Date: for example, <the first day of next month>Due Date Is Month-End Indicator: for example, <deselected> |  |  |
| 10 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 209Effective From: for example, <the first day of current month> | The screen condition displays. |  |
| 11 | Enter Details of Condition - Int. Rate Adjustment | Make the following entries in screen Condition, then choose Apply:On the tab Dates, enter the following data:Adjustment Date Update Rule: for example, 1Interest Rate Adjustment Date: for example, <the first day of current month>Adjustment Date Working Day Shift: for example, 3Note If 3 (Previous Working Day) is selected in field Interest Rate Adjustment Date, the following fields under group Calendar are displayed.Calendar 1: for example, 01Fixing Date Update Rule: for example, 1Fixing Date Shift Direction: for example, -Fixing Date Shift Days: for example, 1Lockout Period in Days: for example, 1 |  |  |
| 12 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 104Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 13 | Enter Details of Condition - Var. int. (accum.) | Make the following entries in screen Condition and choose Apply:On the tab Dates, enter the following data:Calendar 1: for example, 01Calculation Date Frequency: for example, 1Calculation Date: for example, <the first day of next month>Calculation Date Included: for example, <deselected>Calculation Date Is Month-End Indicator: for example, <deselected>Due Date: for example, <the first day of next month>Due Date Is Month-End Indicator: for example, <deselected> |  |  |
| 14 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 263Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 15 | Enter Details of Condition - Final Repayment | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Currency: for example, AEDOn the tab Dates, enter the following data:Calendar 1: for example, 01Due date: for example, <the first day of current month + 1 year> |  |  |
| 16 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: for example, DFMCurrency: for example, AEDFlat Price: for example, <selected> | Security class is created. |  |

#### Create Placement Transaction

##### Create Placement Transaction for Fixed-Rate Bond

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After a placement transaction is concluded in the real world, an entry into the system is required to update the securities position.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, BD_AE1Transaction Type: 300Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Securities Account: for example, BOND_ISSUEGeneral Valuation Class: <choose an appropriate General Valuation Class (GVC), for example, 16 Long term debt(non-current liability)>Position Value Date: for example, <Current Date>Calculation Date: for example, <Current Date>Payment Date: for example, <Current Date>Nominal Amount: for example, 100,000,000.00AEDPrice (%): 99.8Coupon : 1 Next coupon will be delivered(plus accrued interest)Please switch to the Other flows tab | The Create Security Transaction: Other Flows screen is displayed. |  |
| 5 | Enter Data on Other flows | On the tab Other flows, add a row as follows:Flow type : 0321 Issue costPayment Amount: 500.00Payment Currency: AED | All data are entered. |  |
| 6 | Save the Transaction | Choose Save. | If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a prompt asking to Create Position Indicator. Please follow below step if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |  |
| 7 | Create Position Indicator | Choose Create Automatically | The transaction is created. |  |

##### Create Placement Transaction for Floating-Rate Bond

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After placement transaction has concluded in the real world, an entry into the system is required to update the securities position.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.
- You've run the Enter Interest Rates step of the Market Rates Management – Manually via Upload(1XN) test script.

|  |
| --- |
| Note The example data in 1XN might not contain the necessary interest rates for your test. If you are using SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA, please make sure that you've entered interest from 1st day to end date of current month when you are doing test for this test script. |

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result |  |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, BD_AE2 or BD_AE02Transaction Type: 300Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Securities Account: for example, BOND_ISSUEGeneral Valuation Class: <choose an appropriate GeneralValuation Class (GVC), for example, 26 short term debt(current liability)>Position Value Date: for example, <Current Date>Calculation Date: for example, <Current Date>Payment Date: for example, <Current Date>Nominal Amount: for example, 100,000,000.00AEDPrice (%): 99.8Coupon : 1 Next coupon will be delivered(plus accrued interest)Please switch to the Other flows tab | The Create Security Transaction: Other Flows screen is displayed. |  |
| 5 | Enter Data on Other flows | On the tab Other flows, add a row as follows:Flow type : 0321 Issue costPayment Amount: 500.00Payment Currency: AED | All data are entered. |  |
| 6 | Save the Transaction | Choose Save. | If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a prompt asking to Create Position Indicator. Please follow below step if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |  |
| 7 | Create Position Indicator | Choose Create Automatically | The transaction is created. |  |

#### Correspondence

Purpose

TRM transaction related information is transferred between you and your Business Partner. SAP Treasury and Risk Management (SAP TRM) provides standard correspondence functionalities with which you can communicate with Business Partner with a printout form via email.

This section describes the standard correspondence functionality that SAP TRM provides.

##### Set Settlement Status (Manually)

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
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data, and choose Go:Key Date: <the current date>Company Code: for example, 3310Transaction: <transaction you created in the previous step> | The transaction is displayed. |  |
| 4 | Settle the TRM Transaction | On the Manage Financial Transactions screen, select the checkbox at the head of the transaction line and choose Settle. | You are directed to the screen for settling the transaction.Note The view title will be different according to product type of transaction. |  |
| 5 | Save the Change | On the Settle Security Contract: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If the Document lines: Display messages dialog box displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

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

###### Send Confirmation Email/Print

Purpose

SAP provides the BP_DEFAULT business partner group. By default, if any business partner is assigned to this group, correspondence objects will be sent automatically when a financial transaction is saved. As described in the preliminary steps, 33537001 is assigned to BP_GROUP, so the correspondence objects have been sent automatically. If you create a new business partner group and don't assign the auto-send attribute, you can send correspondence objects manually using the Send Correspondence (FTR_COSEND) app.

Procedure

This step doesn’t require any operation in system.

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

In previous step, for the email channel, an outbound email is sent to the Business Partner. Normally, you will receive a counterparty confirmation from the Business Partner via email, phone, etc. This step is outside of SAP,

Procedure

This step doesn’t require any operation in the system.

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

In the previous procedure, all of the correspondence objects of the transaction were matched successfully. As standard functionality, the transaction is settled automatically.

In this activity, you verify that the transaction has been settled automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor view displays. |  |
| 3 | Enter Selection Criteria | On the Correspondence Monitor view, enter following data, and choose Execute:In the Correspondence area,Company Code: for example, 3310On the Finacial Transaction tab,Company Code: for example, 3310Transaction Number: for example, <Transaction Number> | The Correspondence monitor - Standard View view displays. |  |
| 4 | Display Transaction History | On the Correspondence monitor - Standard View screen, select the checkbox of the incoming correspondence object, choose Show Underlying and the details of transaction view displays. | Activity 2 Contract Settlement displays in the second line. |  |

#### Corporate Initiated Payment

Purpose

This section describes how to handle the payment for securities purchase transaction which are initiated by corporate via payment requests.

There are two options to process the payment for the purchase:

1. Process the payment with the ‘Auto. Payment Run’ function.
2. Process the payment without the ‘Auto. Payment Run’ function.

Prerequisites

You have settled the contract in the previous step.

##### Option 1: Generate and Automatically Process Payment Request

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Send for Approval: <select this indicator>Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Send for Approval: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
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

In the case that the payment is initiated by the financial partner, skip the current step and the next step [Process Payment Request](#unique_36) [page ] 68, and continue with the step [Post to General Ledger](#unique_38) [page ] 71.

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

You use the Automatic Payment Transactions for Payment Requests (F111) app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items), but on payment requests.

Prerequisite

Payment request has been generated in the previous procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters screen, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 3 days>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free Selection for payment run, enter the following data and choose Save:Key Number: <the key numbers you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>If information Log created for all accounts displays, choose Continue.Choose Save on screen Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat., and choose Schedule Job to confirm this dialog box.Message Proposal is running displays in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, choose Payments to check the payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests screen, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data and choose Execute:Run Date: for example <current date>Identification: for example TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

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

If the outgoing payment is initiated by bank, it is not necessary to run previous steps Generate Payment Request and Process Payment Request, because the outgoing payment is initiated by bank.

Procedure

This step doesn‘t require any operation in system.

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

- Fix, Pay and Post Flows (TBB1): you use this app to generate the posting for incoming payment. Please note that when using this app in current step, it will not create posting for outgoing payment which has been processed in previous step Generate Payment Request with the Pay Only option.
- Process Business Transactions (TPM10): You use this app to generate the posting for outgoing payment which has been processed in previous step Generate Payment Request with the Pay Only option.

|  |
| --- |
| Note You can also schedule background job for this step, please see corresponding step in Appendix. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Securities: <select this checkbox>Company code: for example 3310Product Type: for example 04ATransaction: <the transaction number you created in previous step>Sec. Class ID Number: <The Sec. Class ID Number you entered in previous step,for example, BD_AE1 or BD_2 or BD_AE02>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | Screen Posting Log: Posted Business Transactions is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria, you can skip the current test step and continue the test step with the Process Business Transactions (TPM10) app. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Execute:Test Run: <unselect this checkbox> | Screen Posting Log: Posted Business Transactions is displayed, and the accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <unselect this checkbox>Company code: for example, 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>ID Number: <The Security ID you created in previous step, for example, BD_AE1 or BD_2 or BD_AE02>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If message You have not selected any business transactions is displayed, that means there is no posting needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Test Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 9 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Update Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, and the accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |  |

#### Post Issuance Cost Manually

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When bonds are issued, bond issuance cost are incurred. Bond issuance cost are presented on the balance sheet as a direct reduction to the carrying amount of the bond, similar to bond discounts. This session is describe to record this kind of transaction cost during bond issuance.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Create Manual Posting (FWBS). | The Manual Posting: Initial Screen screen is displayed. |  |
| 3 | Enter Security Class ID and Security Account | On the Manual Posting: Initial screen, enter the following data and choose Execute:Company code: for example, 3310Security Class ID: for example, BD_AE1 or BD_AE2 or BD_AE02Security Account: for example, BOND_ISSUEChoose Enter. | Screen Manual Postingis displayed. |  |
| 4 | Enter Parameters | On the Manual Posting screen, enter the following data:Interest Value Date: for example, <Current Date>Due Date: for example, <Current Date>Value Date: for example, <Current Date>Position Value Date: for example, <Current Date>FI Posting Date: for example, <Current Date>On the Flows tab, choose insert other flow, on the Manual Posting:Process Flow dialog box, enter the following data, and then choose Copy to confirm the dialog box.Update type: for example, SE3021 Issue costPayment Amount: for example, 500 AED | Update Type is added. |  |
| 5 | Save the Transaction | On the Manual Posting screen, choose Post. | Screen with Payment Log and Posting log displays, payment request has been generated. Make a note of the key number displayed on this screen. Flows were posted successfully. |  |

#### Period-end Closing

Purpose

This section describes activities for period-end closing (usually executed at month end).

##### Import Securities Price

Purpose

By entering the latest price of a bond into SAP system as securities price, the system can recognize its latest position value and perform the relevant journal posting when running key date valuation.

Procedure

Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

##### Import Reference Interest Rate

Purpose

In this step, you adjust the interest rate for the reference interest rate.

Prerequisite

Reference interest rate has been maintained on the fixing date.

Procedure

Follow instructions in the Enter Interest Rates step of the Market Rates Management – Manually via Upload(1XN) test script.

|  |
| --- |
| Note The example data in 1XN might not contain the necessary interest rates for your test. If you are using SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA, please make sure that you've entered interest from 1st day to end date of current month when you are doing test for this test script. |

##### Perform Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to value the positions of securities based on amortized cost or security price imported via Update Securities Price section of the Market Rates Management – Manually via Upload(1XN), as well as to reflect latest foreign currency exchange rate for the investments other than the company reporting currency.

You can also use configuration step Assign Update Types for Accrual/Deferral to define your own accrual/deferral postings, such as aggregated accrual/deferral flow or not. In the case of a compound interest calculation, a grouping term has to be defined.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

|  |
| --- |
| Note You can also schedule background job for this step. Please see corresponding step in Appendix. |

Prerequisite

You have entered latest security price for the security ID in section [Import Securities Price](#unique_39) [page ] 75.

You have performed following sections of this test script for bond 04A:

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Execute Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run Valuation screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions:<unselect this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example, 04ASecurity ID: for example, < Security Class ID Number(s) created in previous steps>, for example, BD_AE1 or BD_AE2 or BD_AE02Security Account: for example, BOND_ISSUEKey Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation with ResetWhen the Period End is also the Year End, the Valuation Category Year End Valuation should be used.Test Run: <select this checkbox>Amortization Log: <select this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Positions to be Valued screen, choose Run Valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Please note there is no posting created because it is test run.Note Sometime there is no simulated posting because your selected security class position in security account may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Display Positions to be Valued screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Positions to be Valued screen, choose Run Valuation. | The Valuation Log screen is displayed, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Then, the accounting document has been created in local GAAP (valuation area AE). |  |

#### Interest rate fixing date

Purpose

This section describes activities for Interest Rate Adjustment and includes:

- [Import Reference Interest Rate](#unique_41) [page ] 78
- [Update Planned Records for Securities](#unique_42) [page ] 78

##### Import Reference Interest Rate

Purpose

In this step, you adjust the interest rate for the reference interest rate.

Prerequisite

Reference interest rate has been maintained on the fixing date.

Procedure

Follow instructions in the Enter Interest Rates step of the Market Rates Management – Manually via Upload(1XN) test script.

|  |
| --- |
| Note The example data in 1XN might not contain the necessary interest rates for your test. If you are using SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA, please make sure that you've entered interest from 1st day to end date of current month when you are doing test for this test script. |

##### Update Planned Records for Securities

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Update Planned Records for Securities (FWUP) | The Update Planned Records for Securitiesscreen is displayed. |  |
| 3 | Enter Selection Criteria | On the Update Planned Records for Securities screen, enter the following data and choose Execute:Company Code: for example, 3310Security ID: for example, BD_AE2 or BD_AE02 | Update was completed successfully. |  |

#### Coupon Date

Purpose

The following steps in this section describes activities for interest payable of issued bond:

- [Post Outgoing Interest Payment](#unique_43) [page ] 79
- [Process Payment Request](#unique_44) [page ] 81

##### Post Outgoing Interest Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can generate interest payment request.

Procedure

Table 2: Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Debit Position - Manual Debit Position (FWZE). | The Manual Debit Position: Initial screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, BD_AE2 or BD_AE02Security Account: for example, BOND_ISSUE | A list of positions is displayed. |  |
| 4 | Select a Flow and Proceed | On the list of positions that displayed on the Manual Debit Position screen, select the top flow with update type SAM7000 and choose Post business transaction. | Manual Debit Position screen is displayed. |  |
| 5 | Enter Details for the Interest Payment | On the Manual Debit Position screen, double click on the record should be paid:The Incoming Payments:Process Flow dialog box is displayed.Verify below data and choose Copy:Payment Amount: for example, the total amount of the interest to be paid. | The flow has been processed in the Flows tab. |  |
| 6 | Post | Confirm the data and choose Post. | Screen with Posting Log and Payment Log displays, payment request has been generated. Make a note of the key number displayed on this screen. |  |

Table 3: Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Automatic Debit Position and Posting - Security Accounts (FWSO) | The Securities: Automatic Debit Position screen is displayed. |  |
| 3 | Enter Parameters and Test Run | On the Securities: Automatic Debit Position Screen, enter the following data and choose Execute:Company Code: for example, 3310Product Type: for example, 04ASecurity ID: for example, BD_AEBD_2 or AE02Security Account: for example, BOND_ISSUEUpdate Type: for example, SAM7000Up to an Including Pos. Date: for example, <end date of current month>Document Date: for example, <end date of current month>Up to an Including Pos. Date: for example, end of term you entered in step Create Security ClassDocument Date: for example, end of term you entered in step Create Security ClassTest Run: for example, <select> | A list of messages indicating the flow is fixed. |  |
| 4 | Production Run | Confirm the messages and go back to previous screen, enter the following data and choose ExecuteTest Run: for example, <deselect> | A list of messages indicating the flow is fixed. |  |

##### Process Payment Request

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests screen, enter the following data and choose Parameters:Run Date: for example, <Current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters screen, enter the following data:Posting Date: for example, <Current date>Next payment run on: for example, <Current date+3 days>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free Selection for payment run, enter the following data and choose Save:Key Number: <the key number you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select this checkbox>Due date check: <select this checkbox>If information Log created for all accounts displays, choose Continue.Choose Save on screen Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat, and choose Schedule Job to confirm this dialog box.Message Proposal is running is displayed in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests screen, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media screen, enter the following data and choose Execute:Run Date: for example <Current date>Identification: for example TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

##### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

#### Reclassification

##### Perform Valuation Class Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, valuation class transfer are executed from long term to short term and reflected in financial accounting.

Prerequisite

The maturity dates of transactions are below one year and the position values are not zero.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Execute Valuation Class Transfer (TPM15M). | The Valuation Class Transfer view displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Valuation Class Transfer view, enter the following data:Securities: <select this checkbox>OTC Transactions: <unselect this checkbox>Company Code: for example, 3310Security ID: for example, BD_AE1Security Account: for example, BOND_ISSUEGeneral Valuation Class (in subarea Specific Selection for Outgoing Position): <select this indicator>Key Date: for example <last date of current month>Test Run: <select this checkbox>and choose Execute. | The Edit Selected Positions view displays. |  |
| 4 | Execute Test Run and Check Result | On the Edit Selected Positions view, select the transactions you want to transfer and enter the new General Valuation Class in field New Valuation Class.Rule of new General Valuation Class:switch the first digit of original General Valuation Class from 1 (long term) to 2 (short term) to change to the new General Valuation Class. For example, if the original General Valuation Class is 16, then the new General Valuation Class is 26.Choose Execute. | The Test Run: Transfer view displays, |  |
| 5 | Review Logs | Choose Messages and Log.On Information Overview dialog box, choose Posting Log.On Posting Log: Posted Business Transactions view, you review the simulated postings. | Logs are reviewed. |  |
| 6 | Production Run | Go back to the initial view of this app. Unselect the Test Run checkbox and repeat the previous steps for production run. | Production run succeeds, postings are created. |  |

#### Unscheduled Redemption

##### Create Redemption Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After redemption transaction has been concluded in the real world, you need to enter the transaction into the system to update the securities position.

Prerequisite

The securities position on hand must be greater than or equal to the position to be sold.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, BD_AE2 or BD_AE02Transaction Type: 400Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Securities Account: for example, BOND_ISSUEGeneral Valuation Class: click on Display Quantity Position to figure out the GVC that should be used, for example, <the same General Valuation Class as purchase transaction for this security class ID>Note If you have performed Valuation Class Transfer step, use the new GVC transferred.Position Value Date: for example, <The second day of next month>Calculation Date: for example, <The second day of next month>Payment Date: for example, <The second day of next month>Incl.: <deselected>Nominal Amount: for example, 100,000,000.00 AEDPrice (%): 100Coupon: 1 Next coupon will be delivered(plus accrued interest) | All data are entered.Note Make sure that there is no condition-based business transactions posted after position value date. |  |
| 5 | Save the Transaction | Choose Save. | The data is saved |  |

##### Set Settlement Status

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data, and choose Go:Key Date: <the current date>Company Code: for example, 3310Transaction: <transaction you created in the previous step> | The transaction is displayed. |  |
| 4 | Settle the TRM Transaction | On the Manage Financial Transactions screen, select the checkbox at the head of the transaction line and choose Settle. | You are directed to the screen for settling the transaction.Note The view title will be different according to product type of transaction. |  |
| 5 | Save the Change | On the Settle Security Contract: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If dialog Document lines: Display messages displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

##### Corporate Initiated Payment

Purpose

This section describes how to handle the payment for securities purchase transaction which are initiated by corporate via payment requests.

There are two options to process the payment for the purchase:

1. Process the payment with the ‘Auto. Payment Run’ function.
2. Process the payment without the ‘Auto. Payment Run’ function.

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Send for Approval: <select this indicator>Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Send for Approval: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
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

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows which require payment requests. It will not create posting in financial accounting.

In the case that the payment is initiated by the financial partner, skip the current step and the next step [Process Payment Request](#unique_50) [page ] 94, and continue with the step [Post to General Ledger](#unique_52) [page ] 97.

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

You use the Automatic Payment Transactions for Payment Requests (F111) app to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items), but on payment requests.

Prerequisite

Payment request has been generated in the previous procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests screen, enter the following data and choose Parameters:Run Date: for example, <current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters screen, enter the following data:Posting Date: for example, <current date>Next payment run on: for example, <current date + 3 days>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free Selection for payment run, enter the following data and choose Save:Key Number: <the key numbers you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>If information Log created for all accounts displays, choose Continue.Choose Save on screen Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat., and choose Schedule Job to confirm this dialog box.Message Proposal is running displays in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, choose Payments to check the payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests screen, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data and choose Run:Run Date: for example <current date>Identification: for example TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

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

If the outgoing payment is initiated by bank, it is not necessary to run the previous steps Generate Payment Request and Process Payment Request, because the outgoing payment is initiated by bank.

Procedure

This step doesn't require any operation in system.

##### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps are available for posting flows:

- Fix, Pay and Post Flows (TBB1): you use this app to generate the posting for incoming payment. Please note that when using this app in current step, it will not create posting for outgoing payment which has been processed in previous step Generate Payment Request with the Pay Only option.
- Process Business Transactions (TPM10): You use this app to generate the posting for outgoing payment which has been processed in previous step Generate Payment Request with the Pay Only option.

|  |
| --- |
| Note You can also schedule background job for this step, please see corresponding step in Appendix. |

Prerequisite

The outgoing payment which should be handled via payment request (if there is) for this transaction has been processed in previous step Generate Payment Request with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Securities: <select this checkbox>Company Code: for example 3310Transaction: <The transaction number you cre-ated in previous step>Sec. Class ID Number: <the Sec. Class ID Num-ber you entered in previous step,for example, BD_AE2 or BD_AE02>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | Screen Posting Log: Posted Business Transactions is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria, you can skip the current test step and continue the test step with the Process Business Transactionsapp. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Execute:Test Run: <unselect this checkbox> | Screen Posting Log: Posted Business Transactions is displayed, and the accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <unselect this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Limit by Subledger Pos.: <select this checkbox>ID Number: <The Security ID you created in previous step>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If message You have not selected any business transactions is displayed, that means there is no posting needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Test Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 9 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.The Update Run: Display Posted/Reversed Business Transactions screen displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, and the accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |  |

|  |
| --- |
| Note You can use the transaction Post General Journal Entries (F0718) as described in General Ledger Accounting (058) script to move the bond proceeds to Other Financiang Soures. Use the ledger group specific posting to post this for modified accrual ledger only. If you are using the WBS element as an account assignment, make sure you adjusted the field status group as described in the preliminary steps. |

#### Scheduled Repayment Date

Purpose

This section describes activities for Interest Rate Adjustment and is composed of the following steps:

- [Post Scheduled Principal Repayment](#unique_53) [page ] 100
- [Process Payment Request](#unique_54) [page ] 101

##### Post Scheduled Principal Repayment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step provides instructions on how to post principal repayment at maturity date of issued bond.

Prerequisite

You have executed all the steps and performed all the transactions which should be occurred and posted before scheduled repayment date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Debit Position - Manual Debit Position (FWZE). | The Manual Debit Position: Initial screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, BD_AE1Security Account: for example, BOND_ISSUE | A list of positions is displayed. |  |
| 4 | Select a Flow and Proceed | On the list of positions that displayed on the Manual Debit Position: Initial Screen, select the top flow with update type SAM7100 and choose Post business transaction: | Manual Debit Position screen is displayed. |  |
| 5 | Enter Details for the Interest Payment | On the Manual Debit Position screen, double click on the record should be paid:The Incoming Payments:Process Flow dialog box is displayed.Verify below data and choose Copy:Payment Amount: for example, the total amount of the principal to be repaid. | flow has been processed in the Flows tab. |  |
| 6 | Post | Confirm the data and choose Post. | Screen with Posting Log and Payment Log displays, payment request has been generated.Note Make a note of the key number displayed on this screen. |  |

|  |
| --- |
| Note you can use the transaction Post General Journal Entries (F0718) as described in the General Ledger Accounting (058) test script to move the bond proceeds to Other Financiang Soures. Use the ledger group specific posting to post this for modified accrual ledger only. |

##### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Automatic Payment Transactions for Payment Requests (F111) to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items) but on payment requests.

Prerequisite

Payment request has been generated in previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests screen, enter the following data and choose Parameters:Run Date: for example, <Current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters screen, enter the following data:Posting Date: for example, <Current date>Next payment run on: for example, <Current date+3 days>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free Selection for payment run, enter the following data and choose Save:Key number: <the key number you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select this checkbox>Due date check: <select this checkbox>If information Log created for all accounts displays, choose Continue.Choose Save on screen Automatic Payment Transactions: Parameters. | The Parameters have been entered message displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat, and choose Schedule Job to confirm this dialog box.Message Proposal is running is displayed in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests screen, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media screen, enter the following data and choose Execute:Run Date: for example <Current date>Identification: for example TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

##### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

### Bond Investment

#### Open Security Account

##### Create Security Account for Investment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A security in general, is usually purchased and maintained by a broker such as a bank or a securities company. The transactions involve opening a security account with the broker. The broker maintains positions by each of the securities account. In the system, the securities positions are also maintained on an account level. This procedure details out the steps of creating a security account.

Prerequisite

A Business Partner with TR0152 Depository Bank is created with ID 33537001.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Securities Accounts (TRS_SEC_ACC). | The Choose Securities Account and Company Code screen is displayed. |  |
| 3 | Enter Account Identifier | Enter a new unique identifier for the new Securities Account, and choose Create.Company Code: for example, 3310Securities Acct: for example, BOND_INVSTInfoChoose Create if a confirmation dialog pops up.if above account is already created, you can choose Display or Change to either view or edit the account. | A new account is created. |  |
| 4 | Enter General Data of the Account | Enter below data and move to next tabSecurities Account ID: for example, BOND33537001AE0Securities Account Type: for example, SAC Asset Securities Account | Move to next tab |  |
| 5 | Enter Bank Data | Enter below data and choose Save:Depository Bank: for example, 33537001External Securities Account ID: for example, 123XXXX567Line 1:Payment Currency: AEDHouse Bank: AEBK1Account ID: AEAC1Line 2:Payment Currency: USDHouse Bank: AEBK1Account ID: USDAC | The data is saved |  |

#### Create Security Class

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The user needs to create a security class ID before creating any transaction on a security. This section introduces how to create a security class depending on different coupon payment structure.

##### Create Security Class for Invested Fixed-Rate Bond

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.ID Number: for example, BD_AE3Product Type: for example, 04A | The New Object screen displays with previously specified ID Number. |  |
| 4 | Enter Header | On the tab Header, enter the following data:Security Class Name: for example, Fixed-Rate #3Gen. Sec. Classification: for example, BondBond Classification: for example, Non-financial company bondsStatus: for example, ActivePlease switch to the Basic Data tab. | The Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | On the tab Basic Data, enter the following data:Issuer: for example, 33537003Issue Currency: for example, AEDIssue Start: for example, <the first day of current month>Calculation: for example, <the first day of current month>Final Due Date: for example, <the first day of current month + 3 years>Quotation: for example, 1In the table Additional Identification Number, enter the following data:Secondary Index Number: for example, ISINSecondary Index Value: for example, XX0000000XX00Please switch to the Ratings tab. | The Ratings tab is displayed. |  |
| 6 | Enter Rating | On the tab Ratings, enter the following data:Rating Procedure: for example, 1_MoodyRating: for example, 1_A1Trend: for example, +Valid From Date: for example, <the first day of current month>Valid To Date: for example, <the first day of current month + 1 year>Please switch to the Condition tab. | The Condition tab is displayed. |  |
| 7 | Enter Condition | On the tab Condition, enter the following data:Interest Calculation Method: for example, 360/360Effective Interest Method: for example, 2Repayment Type: for example, Full repayment on maturityChoose Create in the table header of Condition Items. | The dialog​ New Object pops up. |  |
| 8 | Create Condition Items | On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 100Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 9 | Enter Details of Conditions - Int. (perc.-quoted) | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Interest Calculation Type: for example, Linear Interest CalculationPercentage Rate: for example, 3.0000000On the tab Dates, enter the following data:Calendar 1: for example, 01Calculation Date Frequency: for example, 1Calculation Date: for example, <the first day of next month>Calculation Date Included: for example, <deselected>Calculation Date Is Month-End Indicator: for example, <deselected>Due Date: for example, <the first day of next month>Due Date Is Month-End Indicator: for example, <deselected> |  |  |
| 10 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 263Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 11 | Enter Details of Conditions - Final repayment | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Currency: for example, AEDOn the tab Dates, enter the following data:Calendar 1: for example, 01Calculation date: for example, <the first day of current month + 3 years>Due date: for example, <the first day of current month + 3 years> |  |  |
| 12 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: for example, DFMCurrency: for example, AEDFlat Price: for example, <selected> | Security class is created. |  |

##### Create Security Class for Invested Floating-Rate Bond

Procedure

Option 1: IBOR is in use

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.ID Number: for example, BD_AE4Product Type: for example, 04A | The New Object screen displays with previously specified ID Number. |  |
| 4 | Enter Header | On the tab Header, enter the following data:Security Class Name: for example, Floating-Rate#4Gen. Sec. Classification: for example, BondBond Classification: for example, Non-financial company bondsStatus: for example, ActivePlease switch to the Basic Data tab. | Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | On the tab Basic Data, enter the following data:Issuer: for example, 33537003Issue Currency: for example, AEDIssue Start: for example, <the first day of current month>Calculation: for example, <the first day of current month>Final Due Date: for example, <the first day of current month + 3 years>Quotation: for example, 1In the table Additional Identification Number, enter the following data:Secondary Index Number: for example, ISINSecondary Index Value: for example, XX0000000XX00Please switch to the Ratings tab. | The Ratings tab is displayed. |  |
| 6 | Enter Rating | On tab Ratings, enter the following data:Rating Procedure: for example, 1_MoodyRating: for example, 1_A1Trend: for example, +Valid From Date: for example, <the first day of current month>Valid To Date: for example, <the first day of current month + 1 year>Please switch to the Condition tab. | Condition tab is displayed. |  |
| 7 | Enter Condition | On the tab Condition, enter the following data:Interest Calculation Method: for example, 360/360Effective Interest Method: for example, 2Repayment Type: for example, Full repayment on maturityChoose Create in the table header of Condition Items. | The dialog​ New Object pops up. |  |
| 8 | Create Condition Items | On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 101Effective From: for example, <the first day of current month> | The Condition screen displays. |  |
| 9 | Enter Details of Conditions - Int. (perc.-quoted) | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Interest Calculation Type: for example, Linear Interest CalculationPercentage Rate: for example, AEDM03AEDReference Interest Rate Operator: for example, +Percentage Rate: for example, 3.0000000On the tab Dates, enter the following data:Calendar 1: for example, 01Calculation Date Frequency: for example, 1Calculation Date: for example, <the first day of next month>Calculation Date Included: for example, <deselected>Calculation Date Is Month-End Indicator: for example, <deselected>Due Date: for example, <the first day of next month>Due Date Is Month-End Indicator: for example, <deselected> |  |  |
| 10 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 209Effective From: for example, <the first day of current month>Choose Apply in the Condition screen, and go back to main screen. |  |  |
| 11 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 263Effective From: for example, <the first day of current month> | The Condition screen displays. |  |
| 12 | Enter Details of Conditions - Final repayment | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Currency: for example, AEDOn the tab Dates, enter the following data:Calendar 1: for example, 01Calculation date: for example, <the first day of current month + 3 years>Due date: for example, <the first day of current month + 3 years> |  |  |
| 13 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: for example, DFMCurrency: for example, AEDFlat Price: for example, <selected> | Security class is created. |  |

Option 2: If you want to use SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.ID Number: for example, BD_AE4Product Type: for example, 04A | The New Object screen displays with previously specified Class ID. |  |
| 4 | Enter Header | On the tab Header, enter the following data:Security Class Name: for example, Floating-Rate#4Gen. Sec. Classification: for example, BondBond Classification: for example, Non-financial company bondsPlease switch to the Basic Data tab. | The Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | On tab Basic Data, enter the following data:Issuer: for example, 33537003Issue Currency: for example, AEDIssue Start: for example, <the first day of current month>Calculation: for example, <the first day of current month>Final Due Date: for example, <the first day of current month + 1 year>Quotation: for example, 1In the table Additional Identification Number, enter the following data:Secondary Index Number: for example, ISINSecondary Index Value: for example, XX0000000XX00Please switch to the Ratings tab. | The Ratings tab is displayed. |  |
| 6 | Enter Rating | On the tab Ratings, enter the following data:Rating Procedure: for example, 1_MoodyRating: for example, 1_A1Trend: for example, +Valid From Date: for example, <the first day of current month>Valid To Date: for example, <the first day of current month + 1 year>Please switch to the Condition tab. |  |  |
| 7 | Enter Condition | On the tab Condition, enter the following data:Interest Calculation Method: for example, act/360Effective Interest Method: for example, 2Repayment Type: for example, Full repayment on maturityChoose Create in the table header of Condition Items. | The dialog​ New Object pops up. |  |
| 8 | Enter Condition Items | On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 101Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 9 | Enter Details of Condition - Variable Interest | Make the following entries in screen Condition, then choose Apply:On the tab Amounts, enter the following data:Interest Calculation Type: for example, Compound Interest CalculationInterest Calculation Method: for example, act/360Reference Interest Rate: for example, SOFRNote If Compound Interest Calculation is selected, and you want a reference rate plus a spread, you should input value in following field:Reference Interest Rate Operator: for example, +Percentage Rate: for example, 1.0000000If Average Compound Interest Calculation is selected in field Interest Calculation Type, the following fields under group Average Interest Rate are displayed.Weighting: for example, LAvg. Interest Rate Rounding Decimal: for example, 4Spread: for example, 1.0000000000Set Upper Limit: for example, <selected>Upper Limit: for example, 2.0000000000Set Lower Limit: for example, <selected>Lower Limit: for example, 0.5000000000On the tab Dates, enter the following data:Calendar 1: for example, 01Calculation Date Frequency: for example, 1Calculation Date: for example, <the first day of next month>Calculation Date Included: for example, <deselected>Calculation Date Is Month-End Indicator: for example, <deselected>Due Date: for example, <the first day of next month>Due Date Is Month-End Indicator: for example, <deselected> |  |  |
| 10 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 209Effective From: for example, <the first day of current month> | The screen condition displays. |  |
| 11 | Enter Details of Condition - Int. Rate Adjustment | Make the following entries in screen Condition, then choose Apply:On the tab Dates, enter the following data:Adjustment Date Update Rule: for example, 1Interest Rate Adjustment Date: for example, <the first day of current month>Adjustment Date Working Day Shift: for example, 3Note If 3 (Previous Working Day) is selected in field Interest Rate Adjustment Date, the following fields under group Calendar are displayed.Calendar 1: for example, 01Fixing Date Update Rule: for example, 1Fixing Date Shift Direction: for example, -Fixing Date Shift Days: for example, 1Lockout Period in Days: for example, 1 |  |  |
| 12 | Enter Condition Items | Choose Create button in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 104Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 13 | Enter Details of Condition - Var. int. (accum.) | Make the following entries in screen Condition and choose Apply:On the tab Dates, enter the following data:Calendar 1: for example, 01Calculation Date Frequency: for example, 1Calculation Date: for example, <the first day of next month>Calculation Date Included: for example, <deselected>Calculation Date Is Month-End Indicator: for example, <deselected>Due Date: for example, <the first day of next month>Due Date Is Month-End Indicator: for example, <deselected> |  |  |
| 14 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 263Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 15 | Enter Details of Condition - Final Repayment | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Currency: for example, AEDOn the tab Dates, enter the following data:Calendar 1: for example, 01Due date: for example, <the first day of current month + 1 year> |  |  |
| 16 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: for example, DFMCurrency: for example, AEDFlat Price: for example, <selected> | Security class is created. |  |

##### Create Security Class for Invested Zero-Coupon Bond

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.ID Number: for example, BD_AE5Product Type: for example, 04A | The New Object screen displays with previously specified ID Number. |  |
| 4 | Enter Header | On the tab Header, enter the following data:Security Class Name: for example, Zero-coupon#5Gen. Sec. Classification: for example, BondBond Classification: for example, Non-financial company bondsStatus: for example, ActivePlease switch to the Basic Data tab. | The Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | On tab Basic Data, enter the following data:Issuer: for example, 33537003Issue Currency: for example, AEDIssue Start: for example, <the first day of current month>Calculation: for example, <the first day of current month>Final Due Date: for example, <the first day of current month + 3 years>Quotation: for example, 1In the table Additional Identification Number, enter the following data:Secondary Index Number: for example, ISINSecondary Index Value: for example, XX0000000XX00Please switch to the Ratings tab. | The Ratings tab is displayed. |  |
| 6 | Enter Rating | On the tab Ratings, enter the following data:Rating Procedure: for example, 1_MoodyRating: for example, 1_A1Trend: for example, +Valid From Date: for example, <the first day of current month>Valid To Date: for example, <the first day of current month + 1 year>Please switch to the Condition tab. | The Condition tab is displayed. |  |
| 7 | Enter Condition | On the tab Condition, enter the following data:Discounted: for example, <selected>Repayment Type: for example, Full repayment on maturityChoose Create in the table header of Condition Items. | The dialog​ New Object pops up. |  |
| 8 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 263Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 9 | Enter Details of Conditions - Final repayment | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Currency: for example, AEDOn the tab Dates, enter the following data:Calendar 1: for example, 01Due date: for example, <the first day of current month + 3 years> |  |  |
| 10 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: for example, DFMCurrency: for example, AEDFlat Price: for example, <selected> | Security class is created. |  |

##### Create Security Class for Invested Unit-Quoted Bond

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.ID Number: for example, BD_AE6Product Type: for example, 04A | The New Object screen displays with previously specified ID Number. |  |
| 4 | Enter Header | On the tab Header, enter the following data:Security Class Name: for example, Unit Quote #6Gen. Sec. Classification: for example, BondBond Classification: for example, Non-financial company bondsStatus: for example, ActivePlease switch to the Basic Data tab. | Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | On tab Basic Data, enter the following data:Issuer: for example, 33537003Issue Currency: for example, AEDIssue Start: for example, <the first day of current month>Calculation: for example, <the first day of current month>Final Due Date: for example, <the first day of current month + 3 years>Quotation: for example, 2Nominal Amount: for example, 100.00AEDIn the table Additional Identification Number, enter the following data:Secondary Index Number: for example, ISINSecondary Index Value: for example, XX0000000XX00Please switch to the Ratings tab. | The Ratings tab is displayed. |  |
| 6 | Enter Rating | On the tab Ratings, enter the following data:Rating Procedure: for example, 1_MoodyRating: for example, 1_A1Trend: for example, +Valid From Date: for example, <the first day of current month>Valid To Date: for example, <the first day of current month + 1 year>Please switch to the Condition tab. | The Condition tab is displayed. |  |
| 7 | Enter Condition | On tab Condition, enter the following data:Interest Calculation Method: for example, 360/360Effective Interest Method: for example, 2Repayment Type: for example, Full repayment on maturityChoose Create in the table header of Condition Items. | The dialog​ New Object pops up. |  |
| 8 | Create Condition Items | On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 100Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 9 | Enter Details of Conditions - Int. (perc.-quoted) | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Interest Calculation Type: for example, Linear Interest CalculationPercentage Rate: for example, 3.0000000On the tab Dates, enter the following data:Calendar 1: for example, 01Calculation Date Frequency: for example, 1Calculation Date: for example, <the first day of next month>Calculation Date Included: for example, <deselected>Calculation Date Is Month-End Indicator: for example, <deselected>Due Date: for example, <the first day of next month>Due Date Is Month-End Indicator: for example, <deselected> |  |  |
| 10 | Enter Condition Items | Choose Create in the table header of Condition Items.On the pop-up dialog New Object, enter the following data, then choose Continue.Condition Type: for example, 263Effective From: for example, <the first day of current month> | The screen Condition displays. |  |
| 11 | Enter Details of Conditions - Final repayment | Make the following entries in screen Condition and choose Apply:On the tab Amounts, enter the following data:Currency: for example, AEDOn the tab Dates, enter the following data:Calendar 1: for example, 01Due date: for example, <the first day of current month + 3 years> |  |  |
| 12 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: for example, DFMCurrency: for example, AEDFlat Price: for example, <selected> | Security class is created. |  |

##### Create Security Class for Invested Index-Linked Bond

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Securities Classes (FWZZ). | The Display Class screen is displayed. |  |
| 3 | Enter ID Number | Enter an ID Number for the new Securities Class, and choose Create.Securities Class: for example, IL_BD_AE7A dialog of Create Class pops up, enter the following data and choose Create:Product Type: 04L Index-linked BondShrt: for example, Index-Linked #7 | The Create Class screen displays with previously specified ID Number. |  |
| 4 | Enter Search Terms | On the Create Class - Product Type: Bond - ID Number: IL_BD_AE7 screen, enter the following data:Gen. Sec. Classification: for example, 02 BondBond Classification: 906 Non-financial company bondsSecondary Indices: for example, ISIN XX0000000XX16Please switch to the Basic Data tab, after entering Search Terms. | Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | Enter the following data:Issuer: for example, 33537003Issue Currency: for example, AEDPrice Index: for example, CPINominal Value: for example, 100.00Price Index Base Date: for example, <The first day of the current month>Issue Start: for example,<The first day of the current month>End of Term: for example, <The first day of the current month + 3 year>Quotation for example, Unit-Quoted |  |  |
| 6 | Switch to Conditions | Switch to Conditions tab, and enter the following data:Interest Calculation Method: for example, 360/360Eff.Int.Meth.: for example, ICMARepayment Type: for example, 1 Maturity | Three records of conditions1. Interest with PIDX2. Price index adj.3. Final repayment |  |
| 7 | Enter Details of Conditions - Interest with PIDX | Make the following entries:For the record of Interest with PIDX,Eff. From: for example, <The first day of the current month>Percentage Rate: 3.0000000Double click to enter below data on the Dates tab, and then go back:Calendar 1: 01Calculation date: for example, 1 Months1st date: for example, <the first day of next month>Month-end: <deselected>Include: <deselected> |  |  |
| 8 | Enter Details of Conditions - Price index adj. | For the record of Price index adj.,Calculation Dt.: for example, <end date of the current month>Month-end: <select this indicator>Include: <select this indicator>Frequency: for example, 1 MonthsIdxFixDateLow: for example, <The first day of last month> |  |  |
| 9 | Enter Details of Conditions - Final repaym. PIDX | For the record of Final repaym. PIDX,Eff. From: for example, <The first day of the current month>Double click and switch to the Dates tab, enter the following data, and choose back:Calendar 1: 01Calculation date: for example, <default value>Due date: for example, <default value> |  |  |
| 10 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Save:Exchange: OTCFlat Price: <select this indicator> | Data is saved. |  |

#### Import Securities Price

Purpose

In this step, you enter the security price before the system can recognize its latest fair value and update the credit limit utilization when you enter a purchase transaction or run the end-of-day processing.

Procedure

Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

#### Analyze Cash Position

Purpose

At the end of the transaction day, the cash manager always reviews the cash position status for making decisions about the right financial instruments for short-term purposes, based on analysis of cash position.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) SAP Fiori app to analyze the cash position. For more information, please refer to the Basic Cash Operations(BFB) test script.

#### Analyze Liquidity Forecast

Purpose

The cash manager reviews the liquidity forecast regularly and makes decisions regarding medium-term or long-term financial instruments, such as, investment, loan, or foreign exchange.

Procedure

If cash management is implemented in your system, you use the Cash Flow Analyzer (F2332) app to analyze the liquidity forecast For more information, see the Basic Cash Operations(BFB) test script.

#### Check Limit Utilization Report

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

The Limit master records of your company was maintained in the system, Maintaining Credit Limit in the Preliminary Steps is completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Execute:Limit Type: for example, Y01 or Y07Limit Utilization Base: for example, 1Determination Date: for example, <the current date>Limits Valid From: for example, <the current date> | An overview of the limit utilization in accordance with your selection criteria is displayed. |  |

#### Create Bond Purchase Transaction

##### Create Bond Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you enter the purchase order information into the system. The order includes amount and order data and can be converted to the contract through order execution or obsoleted through expiration.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

Please create two purchase orders via below steps.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Securities Transaction: Entry Screen screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Securities Transaction: Entry Screen, enter the following data and choose Enter:Company Code: for example, 3310ID Number: the security class you created, for example, BD_AE3Transaction Type: 100Partner: for example, 33537001In the Activity area,Order/Fixing: <select> | The Create Securities Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:In the Position area,Securities Account: for example, BOND_INVSTIn the Amounts area,Nominal Amount: for example, 100,000,000.00 AEDIn the Order Data area,Limit Date: for example, <two days after current date>Limit Price: for example, 100 | All data is entered. |  |
| 5 | Save the Transaction | Choose Save.Note Write down the created security transaction ID for following step. |  |  |
| 6 | Create Position Indicator | Choose Create Automatically. | The transaction is created. |  |
| 7 | Create Another Order for Expiration | Repeat step 2-7 to create another order for expiration. |  |  |

##### Execute Bond Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You decide to purchase a bond based on the created order. After the execution, you enter the purchase contract information into the system. You can skip the step [Create Fixed-Rate Bond Purchase Transaction](#unique_65) [page ] 128 as the fixed-rate bond purchase transaction is generated from bond.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

|  |
| --- |
| Note Please only use one order created in the above step to create the purchase contract. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Data on Initial Screen | In the search term area, enter the following data and choose Go:Key Date: for example, TodayCompany Code: for example, 3310Transaction: <the order transaction number> | The bond purchase order transaction screen is displayed. |  |
| 4 | Execute the Purchase Order | In the Transaction area, select the transaction and choose Execute Order in the toolbar via button …. | The details of the bond purchase order transaction are displayed. |  |
| 5 | Add Relevant Information and Save the Transaction | On the tab Structure, enter the following data:In the Position area,General Valuation Class: for example, choose an appropriate GeneralValuation Class (GVC), for example, 11 Long term investment(non-current asset):Amorizated costPrice(%): for example, 99.8Choose Save.Note If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a dialog box appears asking to Create Position Indicator.If the Position Indicator is already created, then you can ignore below step. The following message is displayed: Security transaction XXXXX created in company code YYYY |  |  |
| 6 | Create Position Indicator | Choose Create Automatically. | The bond purchase order is executed, the relevant bond purchase transaction is created.Note Note down the transaction ID for following step. |  |

##### Waiver Bond Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You decide to waiver the purchase order. Once you set the order to expiration, you need to maintain the relevant information in the system.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.
- The relevant bond purchase order is created in the above steps but not executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Data on Initial Screen | In the search term area, enter the following data and choose Go:Key Date: for example, TodayCompany Code: for example, 3310Transaction: <the transaction number> | The bond purchase order transaction screen is displayed. |  |
| 4 | Waiver the Bond Purchase Order | In the Transaction area, select the transaction and choose Order Expiry in the toolbar via button …. | The details of the bond purchase order transaction are displayed. |  |
| 5 | Waiver the Bond Purchase Order | On the initial screen, choose Save. | The status of bond purchase order transaction is changed to Order Expiration. |  |

##### Create Fixed-Rate Bond Purchase Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After purchase transaction has concluded in the real world, an entry into the system is required to update the securities position.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01) . | The Create Securities Transaction: Entry Screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Securities Transaction: Entry Screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, BD_AE3Transaction Type: 100Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Securities Account: for example, BOND_INVSTGeneral Valuation Class: choose an appropriate GeneralValuation Class (GVC), for example, 11 Long term investment(non-current asset):Amorizated costPosition Value Date: for example, <Current Date>Calculation Date: for example, <Current Date>Payment Date: for example, <Current Date>Nominal Amount: for example, 100,000,000.00 AEDPrice (%): 99.8Coupon : 1 Next coupon will be delivered(plus accrued interest) | The Create Security Transaction: Other Flows screen is displayed. |  |
| 5 | Save the Transaction | Choose Save. | If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a dialog box appears asking to Create Position Indicator. Please follow below step if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |  |
| 6 | Create Position Indicator | Choose Create Automatically. | The transaction is created. |  |

##### Create Floating-Rate Bond Purchase Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After purchase transaction has concluded in the real world, an entry into the system is required to update the securities position.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.
- You've run the Enter Interest Rates step of the Market Rates Management – Manually via Upload(1XN) test script.

|  |
| --- |
| Note The example data in 1XN might not contain the necessary interest rates for your test. If you are using SOFR / ESTER / SONIA / SARON / TONAR / CORRA / SORA / HONIA, please make sure that you've entered interest from 1st day to end date of current month when you are doing test for this test script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result |
| --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, BD_AE4 or BD_AE04Transaction Type: 100Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Securities Account: for example, BOND_INVSTGeneral Valuation Class: <choose an appropriate General Valuation Class (GVC), for example, 12 Long term investment (non-current asset): Fair value th. OCI>Position Value Date: for example, <Current Date>Calculation Date: for example, <Current Date>Payment Date: for example, <Current Date>Nominal Amount: for example, 100,000,000.00 AEDPrice (%): 98Coupon : 1 Next coupon will be delivered (plus accrued interest) | The Create Security Transaction: Other Flows screen is displayed. |
| 5 | Check Cash Flow | If you are using security ID BD_AE04, then you may choose tab Cash Flow, and choose Show/Hide Single Flows to show the single flows.Depending on the date you are doing this test, the following cash flows might show up:0100 Purchase (transaction)0871 Accrued interest (accumulated)0870 Accrued interest (transaction)Choose Choose Layout, in the Choose Layout dialog box, choose 1SAP07 Interest rate adjustment view.Note Please make sure that the column Posting status of all the flow type 0870 are Activity does not allow posting.If some of the flow type 0870 features posting status Rate/Price not adjusted for flow, you need to maintain the relevant interest rate on the fixing date. Please refer to the Enter Interest Rates step of the Market Rates Management – Manually via Upload(1XN) test script. | All cash flows have posting status Activity does not allow posting. |
| 6 | Save the Transaction | Choose Save. | If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a prompt asking to Create Position Indicator. Please follow below step if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |
| 7 | Create Position Indicator | Choose Create Automatically. | The transaction is created. |

##### Create Zero-Coupon Bond Purchase Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After purchase transaction has concluded in the real world, an entry into the system is required to update the securities position.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, BD_AE5Transaction Type: 100Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Securities Account: for example, BOND_INVSTGeneral Valuation Class: choose an appropriate GeneralValuation Class (GVC), for example, 13 Long term investment(non-current asset):Fair value th. P/LPosition Value Date: for example, <Current Date>Calculation Date: for example, <Current Date>Payment Date: for example, <Current Date>Nominal Amount: for example, 100,000,000.00 AEDPrice (%): 99.8 | The Create Security Transaction: Other Flows screen is displayed. |  |
| 5 | Save the Transaction | Choose Save. | If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a prompt asking to Create Position Indicator. Please follow below step if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |  |
| 6 | Create Position Indicator | Choose Create Automatically | The transaction is created. |  |

##### Create Unit-Quoted Bond Purchase Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After purchase transaction has concluded in the real world, an entry into the system is required to update the securities position.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, BD_AE6Transaction Type: 100Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Securities Account: for example, BOND_INVSTGeneral Valuation Class: choose an appropriate GeneralValuation Class (GVC), for example, 11 Long term investment(non-current asset):Amorizated costPosition Value Date: for example, <Current Date>Calculation Date: for example, <Current Date>Payment Date: for example, <Current Date>Number of Units: for example, 100,000Price (Unit-Quoted): 100.00AEDCoupon: 1 Next coupon will be delivered(plus accrued interest) | The Create Security Transaction: Other Flows screen is displayed. |  |
| 5 | Save the Transaction | Choose Save. | If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a prompt asking to Create Position Indicator. Please follow below step if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |  |
| 6 | Create Position Indicator | Choose Create Automatically. | The transaction is created. |  |

##### Create Index-Linked Bond Purchase Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After purchase transaction has concluded in the real world, an entry into the system is required to update the securities position.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.
- The relevant Index value is maintained. Refer to the Enter Price Index Values step of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, IL_BD_AE7Transaction Type: 100Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Securities Account: for example, BOND_INVSTGeneral Valuation Class: choose an appropriate GeneralValuation Class (GVC), for example, 11 Long term investment(non-current asset):Amorizated costPosition Value Date: for example, <the current date>Calculation Date: for example, <the current date>Payment Date: for example, <the current date>Number of Units: for example, 100,000Price (Unit-Quoted): 98.00 AEDCoupon: 1 Next coupon will be delivered(plus accrued interest) | The Create Security Transaction: Other Flows screen is displayed. |  |
| 5 | Save the Transaction | Choose Save. | If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a prompt asking to Create Position Indicator. Please follow below step if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |  |
| 6 | Create Position Indicator | Choose Create Automatically. | The transaction is created. |  |

#### Correspondence

Purpose

TRM transaction related information is transferred between you and your Business Partner. SAP Treasury and Risk Management (SAP TRM) provides standard correspondence functionalities with which you can communicate with Business Partner with a printout form via email.

This section describes the standard correspondence functionality that SAP TRM provides.

##### Set Settlement Status (Manually)

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data, and choose Go:Key Date: <the current date>Company Code: for example, 3310Transaction: <transaction you created in the previous step> | The transaction is displayed. |  |
| 4 | Settle the TRM Transaction | On the Manage Financial Transactions screen, select the checkbox at the head of the transaction line and choose Settle. | You are directed to the screen for settling the transaction.Note The view title will be different according to product type of transaction. |  |
| 5 | Save the Change | On the Settle Security Contract: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If the Document lines: Display messages dialog box displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

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

###### Send Confirmation Email/Print

Purpose

SAP provides the BP_DEFAULT business partner group. By default, if any business partner is assigned to this group, correspondence objects will be sent automatically when a financial transaction is saved. As described in the preliminary steps, 33537001 is assigned to BP_GROUP, so the correspondence objects have been sent automatically. If you create a new business partner group and don't assign the auto-send attribute, you can send correspondence objects manually using the Send Correspondence (FTR_COSEND) app.

Procedure

This step doesn’t require any operation in system.

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

In previous step, for the email channel, an outbound email is sent to the Business Partner. Normally, you will receive a counterparty confirmation from the Business Partner via email, phone, etc. This step is outside of SAP,

Procedure

This step doesn’t require any operation in the system.

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

In the previous procedure, all of the correspondence objects of the transaction were matched successfully. As standard functionality, the transaction is settled automatically.

In this activity, you verify that the transaction has been settled automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor view displays. |  |
| 3 | Enter Selection Criteria | On the Correspondence Monitor view, enter following data, and choose Execute:In the Correspondence area,Company Code: for example, 3310On the Finacial Transaction tab,Company Code: for example, 3310Transaction Number: for example, <Transaction Number> | The Correspondence monitor - Standard View view displays. |  |
| 4 | Display Transaction History | On the Correspondence monitor - Standard View screen, select the checkbox of the incoming correspondence object, choose Show Underlying and the details of transaction view displays. | Activity 2 Contract Settlement displays in the second line. |  |

#### Corporate Initiated Payment

Purpose

This section describes how to handle the payment for securities purchase transaction which are initiated by corporate via payment requests.

There are two options to process the payment for the purchase:

1. Process the payment with the ‘Auto. Payment Run’ function.
2. Process the payment without the ‘Auto. Payment Run’ function.

Prerequisites

You have settled the contract in the previous step.

##### Option 1: Generate and Automatically Process Payment Request

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Send for Approval: <select this indicator>Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview table lists Create Security Class for Invested Index-Linked Bond using Manage Securities Classes (FWZZ), while other classes use Manage Security Classes (F8717) - app naming differs by section.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Intro says process covers fixed-rate, floating-rate and zero-coupon bonds, but the script also tests unit-quoted and index-linked bonds.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Correspondence section refers to BP_DEFAULT/BP_GROUP while elsewhere the group is named BPG_DEFAULT.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Section 'Scheduled Repayment Date' purpose text says it describes Interest Rate Adjustment, apparently copied from another section.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/bond-management-3wy-ae-test-script-sap-s-4hana-cloud-public-edition-26-part-02]]
- related-to :: [[05-treasury-and-cash-management/bond-management-group-ledger-ifrs-3wz-ae-test-script-982]]
- related-to :: [[05-treasury-and-cash-management/test-script-bond-management-group-ledger-us-gaap-3x0-ae-983]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3WY_S4CLD2608_BPD_EN_AE.docx` — lines 1–2911 of the extracted text · extracted with `mammoth` · 413,538 chars in the whole document
