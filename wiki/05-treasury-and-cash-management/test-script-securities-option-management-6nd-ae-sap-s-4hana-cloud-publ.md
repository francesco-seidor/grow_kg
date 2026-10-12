---
id: 05-treasury-and-cash-management/test-script-securities-option-management-6nd-ae-sap-s-4hana-cloud-publ
title: "Test Script: Securities Option Management (6ND_AE) - SAP S/4HANA Cloud Public Edition (6ND_S4CLD2608_BPD_EN_AE)"
description: "Test script for scope item 6ND (AE localization): securities option lifecycle in Treasury, from setup to payment, valuation, exercise/expiry, accounting and reports."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/securities-options]
aliases: [6ND_S4CLD2608_BPD_EN_AE]
keywords: [Securities Option Management, test scripts, business partner setup, correspondence, premium payment, period-end closing, net present value, option exercise and expiry, credit limits, trader authorizations]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6ND_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1181
topic: 05-treasury-and-cash-management/securities-options
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Securities Option Management (6ND_AE) - SAP S/4HANA Cloud Public Edition (6ND_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6ND_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Securities Option Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Securities Option Management (6ND_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232859236)

[2 Prerequisites 6](#_Toc232859237)

[2.1 System Access 6](#_Toc232859238)

[2.2 Roles 6](#_Toc232859239)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232859240)

[2.4 Business Conditions 8](#_Toc232859241)

[2.5 Preliminary Steps 9](#_Toc232859242)

[2.5.1 Create Business Partner 9](#_Toc232859243)

[2.5.1.1 Create Business Partner - Counterpart/Depository Bank 9](#_Toc232859244)

[2.5.1.1.1 Maintain General Data for Business Partner 9](#_Toc232859245)

[2.5.1.1.2 Maintain Payment Details for Business Partner 11](#_Toc232859246)

[2.5.1.1.3 Maintain Authorizations for Business Partner 14](#_Toc232859247)

[2.5.1.1.4 Maintain Reporting Data in Company Code for Business Partner 15](#_Toc232859248)

[2.5.1.1.5 Maintain Additional Business Partner Roles 16](#_Toc232859249)

[2.5.1.2 Create Business Partner - Issuer 17](#_Toc232859250)

[2.5.1.2.1 Maintain General Data for Business Partner 17](#_Toc232859251)

[2.5.1.2.2 Maintain Reporting Data in Company Code for Business Partner 19](#_Toc232859252)

[2.5.2 Correspondence 20](#_Toc232859253)

[2.5.2.1 Maintain Profile and BP Group Assignments to Internal Recipient 20](#_Toc232859254)

[2.5.2.2 Maintain Profile and BP Group Assignments to External Recipient 22](#_Toc232859255)

[2.5.3 Maintaining Credit Limit 24](#_Toc232859256)

[2.5.3.1 Maintain Limit with Limit Type Y01 24](#_Toc232859257)

[2.5.3.2 Maintain Limit with Limit Type Y07 25](#_Toc232859258)

[2.5.4 Maintain Trader and Trader Authorizations 26](#_Toc232859259)

[2.5.4.1 Define Traders 26](#_Toc232859260)

[2.5.4.2 Define User Data 27](#_Toc232859261)

[2.5.4.3 Maintain Trader Authorizations 28](#_Toc232859262)

[3 Overview Table 30](#_Toc232859263)

[4 Test Procedures 33](#_Toc232859264)

[4.1 Open Security Account 33](#_Toc232859265)

[4.2 Create Security Class 34](#_Toc232859266)

[4.3 Import Market Data 36](#_Toc232859267)

[4.4 Generate Limit Utilizations 36](#_Toc232859268)

[4.5 Check Limit Utilization Report 37](#_Toc232859269)

[4.6 Create Securities Option Contract 38](#_Toc232859270)

[4.7 Correspondence 41](#_Toc232859271)

[4.7.1 Set Settlement Status (Manually) 41](#_Toc232859272)

[4.7.2 Correspondence with PDF Form 42](#_Toc232859273)

[4.7.2.1 Send Confirmation Email/Print 43](#_Toc232859274)

[4.7.2.2 Check Correspondence Status 43](#_Toc232859275)

[4.7.2.3 Receive Incoming Confirmation 45](#_Toc232859276)

[4.7.2.4 Find Deal and Match Deal Details 45](#_Toc232859277)

[4.7.2.5 Set Settlement Status 47](#_Toc232859278)

[4.8 Premium Payment 47](#_Toc232859279)

[4.8.1 Corporate Initiated Payment 47](#_Toc232859280)

[4.8.1.1 Option 1: Generate and Automatically Process Payment Request 48](#_Toc232859281)

[4.8.1.2 Option 2: Generate and Process Payment Request 51](#_Toc232859282)

[4.8.1.2.1 Generate Payment Request 51](#_Toc232859283)

[4.8.1.2.2 Process Payment Request 53](#_Toc232859284)

[4.8.1.3 Send Payment Medium File 56](#_Toc232859285)

[4.8.2 Bank-Initiated Payment 56](#_Toc232859286)

[4.8.3 Post to General Ledger 56](#_Toc232859287)

[4.9 Period-end Closing 59](#_Toc232859288)

[4.9.1 Import Market Data 59](#_Toc232859289)

[4.9.2 Calculate or Maintain Fair Value of Transaction 60](#_Toc232859290)

[4.9.3 Perform Key Date Valuation 62](#_Toc232859291)

[4.10 Transaction is Mature 64](#_Toc232859292)

[4.10.1 Import Market Data 64](#_Toc232859293)

[4.10.2 Calculate or Maintain Fair Value of Transaction 65](#_Toc232859294)

[4.10.3 Review Securities Option Status 68](#_Toc232859295)

[4.10.3.1 Decide to Exercise 69](#_Toc232859296)

[4.10.3.2 Create Securities Contract 70](#_Toc232859297)

[4.10.3.3 Decide to Expire 71](#_Toc232859298)

[4.11 Post Derived Business Transactions 72](#_Toc232859299)

[4.12 Reports 74](#_Toc232859300)

[4.12.1 Define Financial Positions 74](#_Toc232859301)

[4.12.2 Financial Status (Book Value) 75](#_Toc232859302)

[4.12.3 Display Treasury Alerts - Posting 76](#_Toc232859303)

[4.12.4 Display Treasury Alerts- Settlement, Release and Payment 77](#_Toc232859304)

[4.12.5 Display Treasury Payments 78](#_Toc232859305)

[4.12.6 Display Payment Schedule 79](#_Toc232859306)

[4.12.7 Analyze NPV 80](#_Toc232859307)

[4.12.8 Display Treasury Posting Journal 81](#_Toc232859308)

[4.12.9 Display Treasury Position Flows 82](#_Toc232859309)

[4.12.10 Display Treasury Position Values 83](#_Toc232859310)

[4.12.11 Treasury Position Analysis 84](#_Toc232859311)

[4.12.12 Display Securities Account Class Positions 84](#_Toc232859312)

[4.12.13 Calculate Market Risk Key Figures 85](#_Toc232859313)

[5 Appendix 87](#_Toc232859314)

[5.1 Position Indicator 87](#_Toc232859315)

[5.1.1 Change Position Indicator 87](#_Toc232859316)

[5.2 Job Scheduling 88](#_Toc232859317)

[5.2.1 Generate Limit Utilizations 88](#_Toc232859318)

[5.2.2 Generate Payment Request 89](#_Toc232859319)

[5.2.3 Post Flows to General Ledger 92](#_Toc232859320)

[5.2.3.1 Template - Fix, Pay and Post Flows 92](#_Toc232859321)

[5.2.3.2 Template - Process Business Transactions 94](#_Toc232859322)

[5.2.4 Calculate Market Risk Key Figures 96](#_Toc232859323)

[5.2.5 Key Date Valuation 98](#_Toc232859324)

[5.3 Accounting 99](#_Toc232859325)

[5.3.1 Reverse Valuation 100](#_Toc232859326)

[5.4 Market Risk Analyzer 101](#_Toc232859327)

[5.4.1 Manage Market Data Shift 101](#_Toc232859328)

[5.4.2 Maintain Scenarios 102](#_Toc232859329)

[5.4.3 Defining Report Layout for Calculate Market Risk Key Figures 103](#_Toc232859330)

[5.4.4 Manage Market Risk Key Figure Sets 106](#_Toc232859331)

[5.5 Credit Risk Analyzer 109](#_Toc232859332)

[5.5.1 Display Limit Overview 109](#_Toc232859333)

[5.6 Change Counterparty 110](#_Toc232859334)

[5.6.1 Change Counterparty of Financial Transaction 110](#_Toc232859335)

[5.6.2 Display Financial Transactions with Changed Counterparty 111](#_Toc232859336)

[5.7 Simulated Valuation 112](#_Toc232859337)

[5.7.1 Run Simulated Valuation 112](#_Toc232859338)

[5.7.2 Delete Simulated Valuation 114](#_Toc232859339)

## Purpose

Overview

The scope item helps you to better manage your Securities Option instruments.

It helps you to automate labor-intensive processes, such as payment handling and accounting postings, giving you more time to focus on value-added activities. You can manage operational and accounting requirements.

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
| 5OD - Stock Management or3WY - Bond Management or2UN - Money Market Mutual Fund Management or5WF - Shareholding Management | At least one of the securities related scope items is required depending on your business requirements.Note As an example, this test script describes the process of securities option for stock as the underlying transaction. Therefore, for the testing purpose, you need to activate scope item Stock Management (5OD). |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner view, choose Organization. | The Create Organization screen is displayed. |  |
| 4 | Enter Address Data | On the Create Organization view, enter the following data:Business Partner: for example, 33537001Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Bank 1 - SAMPLE BANKSalutation: for example, Bank 1Search Term 1/2: for example, Bank 1Street/House number: for example,Postal Code/City: for example,Ctry/Reg.: AELanguage: ENE-Mail: <E-mail>Address Valid From: for example, <the current date in previous year>Address Valid To: for example, <Dec 31 of the year 9999>and Save.Note Remain on this screen for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to Change Mode | On the Display Organization33537001 details screen, choose Switch Between Display and Change, and enter the following data:Change in BP role: select TR0151 Counterparty | More counterparty related tabs, for example Legal Data, Rating display. |  |
| 6 | Enter Legal Data | On the Change Organization:33537001, new role Counterparty view, from the Navigation Menu, choose Legal Data from the dropdown list and enter the following data:Country/Region: AEand choose Save.Note The navigation menu is on the right side of the view. It displays as … , and is next to the >),Note Remain in this view for subsequent steps. | The legal data is entered and saved.Change Organization: 33537001, new role Counterparty screen is displayed. |  |
| 7 | Enter Payment Transaction Data | On the Change Organization:33537001, new role Counterparty screen, from the Navigation Menu, select Payment Transactions from the dropdown list and enter the following two rows of data:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, <bank key>Bank acct: for example, <bank account>IBAN: choose the IBAN button and choose Continue in the IBAN dialog box.Row 2:ID: for example, USD1C/R: for example, AEBank Key: for example, <bank key>Bank acct: for example, <bank account>IBAN: choose the IBAN button and then choose Continue on the IBAN dialog box.Now choose Save.Note If a dialog window of Information appears when you choose IBAN, choose Continue. | The Payment transaction data is entered and the Business Partner is saved. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter the following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter the following data:Change in BP Role: select TR0151 Counterpartyand choose Enter. | Change Organization: 33537001 , role Counterparty screen is displayed. |  |
| 4 | Enter SI: Payment Details Data | On the Change Organization:33537001, role Counterparty screen, choose Company Code, and enter the following data:Company Code: for example, 3310Choose ENTER and choose SI: Payment Details and enter the following four rows of data:Row 1:Currency: for example, AEDPay.Det.ID: for example, AEDIHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, <leave blank>Partner Bank: for example, BlankPayment Request: for example, <deselect>Payment Methods: for example, BlankRow 2:Currency: for example, AEDPay.Det.ID: for example, AEDOHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, 33537001Partner Bank: for example, AED1Payment Request: for example, <select>Payment Methods: for example, TRow 3:Currency: for example, USDPay.Det.ID: for example, USDIHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/ee: for example, BlankPayment Request: for example, <deselect>Payment Methods: for example, <leave blank>Row 4:Currency: for example, USDPay.Det.ID: for example, USDOHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/Payee: for example, 33537001Partner Bank: for example, USD1Payment Request: for example, <select>Payment Methods: for example, FNote Remain in the view for subsequent steps.Note If a warning notification displays the following message:Business partner proposed as payer/payee (see long text). Display this message for this business partner again? choose No. | The SI: Payment Details data is entered. |  |
| 5 | Assign Payment Details | From the last view of previous step,For AED,select the Checkbox for AEDAEDI. Choose Assign, in the Counterparty Change: Payment Details Assignment dialog box, and choose Select All Incoming.Now AEDI displays under PmntID-Inc. .Choose Continue to close the dialog box.Select the Checkbox for AEDAEDO.Choose Assign, in the Counterparty Change: Payment Details Assignment dialog box and choose Select All Outgoing.Now AEDO displays under P-ID Outg.Choose Continue to close the dialog box.Repeat for USD:USD I: PmntID-IncUSD O: P-ID Outg.On Change Organization:33537001, role Counterparty view, choose Save. | Payment details and the assignments are saved. |  |

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter the following data:Business Partner: 33537001Choose Enter and choose Switch Between Display and Change, and enter the following data:Change in BP Role: select TR0151 Counterparty | Change Organization: 33537001 , role Counterparty screen is displayed. |  |
| 4 | Enter SI: Authorizations data | On the Change Organization: 33537001, role Counterparty screen, choose Company Code, choose SI: Authorizations, enter the following data and choose Save.Derivatives: select the Auth. checkboxSecurities: select the Auth. checkboxNote You can also give authorization to a specific product type and transaction type by expending the folders. For testing purpose, we give all authorizations to all kinds of product types and transaction types. | The Authorizations data is saved. |  |

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter the following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: choose TR0151 Counteparty | Change Organization: 33537001 , role Counterparty screen is displayed. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization: 33537001, role Counterparty screen, choose Company Code, choose Reporting Data in Company Code, and enter the following data and choose save.Comp. Rel.: for example, 3 OtherNote If you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown list.Note Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itThey are used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter the following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change. | Change Organization: 33537001 screen is displayed. |  |
| 5 | Add New Role of TR0152 Depository Bank | Select Change in BP Role to: for example, TR0152 Depository BankChoose Save. | Data is saved. |  |

##### Create Business Partner - Issuer

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner screen, choose Organization. | The Create Organization: screen is displayed. |  |
| 4 | Enter Address Data | On the Create Organization screen, enter the following entries and choose Save:Business Partner: for example, 33537003Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Bank 2 - SAMPLE BANKSalutation: for example, Bank 2Search Term 1/2: for example, Bank 2Street/House number: for example,Postal Code/City: for example,Country: AELanguage: ENE-Mail: for example, <E-mail>Address Valid From: for example, <the current date in previous year>Address Valid To: for example, Dec 31 of the year 9999Note Remain on this view for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to Change Mode | On the Display Organization33537003 screen, choose Switch Between Display and Change, and enter the following data:Change in BP role: select TR0150 Issuer | More counterparty related tabs such as Legal Data, Rating show up. |  |
| 6 | Enter Legal Data | On the Change Organization:33537003 screen, choose Legal Data from the dropdown list of Navigation Menu, enter the following data and choose Save:Country/Region: AENote The navigation menu is on the right side of the view. It displays as … , and is next to the >),Note Remain in this view for subsequent steps. | The Legal data is entered and saved.The Change Organization:33537003, role Counterparty screen is displayed. |  |

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
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter the following data:Business Partner: 33537003Choose Enter and then choose Switch Between Display and Change, and enter the following data:Change in BP Role: choose TR0150 Issuer(defined) | Change Organization: 33537003 , role Issuer screen is displayed. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization:33537003, role Issuer screen, choose Company Code, and enter the following data:Company Code: for example, 3310Choose ENTER and choose Reporting Data in Company Code, and enter the following data and choose Save.Comp. Rel.: for example, 3 OtherIf you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown list.Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itIt can be used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Assign Profile and BP Group - Internal Recipients (FTR_INT_ASSIGN). | The Assignment of Profiles and BP Groups to Internal Recipients: screen is displayed. |  |
| 3 | Enter Business Partner Data on the View | On the left side of Assignment of Profiles and BP Groups to Internal Recipients view, choose Insert Row and enter the following data, and then select the item by ticking the checkbox before:IntRec: for example, INT.RECPCoCd: for example, 3310Recpt/Send Type: for example, INTERNALCheckbox: <select> | The Business Partner information is entered. |  |
| 4 | Assign Business Profile and BP Group to the Business Partner | On the top-right side of Assignment of Profiles and BP Groups to Internal Recipients view, expend the node, and choose one item to maintain the business partner profile and business partner group, for example, Derivatives > OTC Options > 76J OTC Securities Option > 100 Investment > 20 ContractThen on the bottom-right side of the screen, choose Insert Row, enter the following data, and choose Save.Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTUser Name: <select a User ID>Choose Insert Row again and add another entry as following and choose Save:Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTUser Name: <select a User ID>.Note The user ID is a backend user ID. | Business partner profile and BP group and user ID are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat the previous step to assign BP profile and BP group to the rest of Product type/Transaction Type/Activity category | Check the item INT.RECP in the left side view, and choose Modify Row.Repeat the above step to maintain other items under the OTC Securities Option folder.Product TypeTransaction TypeActivity Category76J20020 | BP profiles and BP groups and user IDs are assigned to all the listed Product Types/Transaction Types/ Activity Categories. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Assign Profile and BP Group - External Recipients (FTR_EXT_ASSIGN). | The Assignment of Profiles and BP Groups to External Recipients: screen is displayed. |  |
| 3 | Enter Business Partner Data on the View | On the left side of Assignment of Profiles and BP Groups to External Recipients: view, choose Insert Row and enter the following data, and then select the business partner by ticking the checkbox before the business partner:BusPartner: for example, 33537001CoCd: for example, 3310Recpt/Send Type: for example, COUNTERPARTY | The Business Partner information is entered. |  |
| 4 | Assign Business Profile and BP Group to the Business Partner | On the top right side of the Assignment of Profiles and BP Groups to External Recipients screen, expand the node, and choose one item to maintain the business partner profile and business partner group, for example, Derivatives > OTC Options > 76J OTC Securities Option > 100 Investment > 20 ContractThen on the bottom-right side of the screen, choose Insert Row and enter the following data:Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTChoose Insert Row again and add another entry as following data：Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTNote Normally you only assign one profile to a Product type/Transaction type/Activity Category. | Business partner profiles and BP groups are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat the previous step to assign BP profiles and BP groups to the rest of Product type/Transaction Type/Activity category | Check the item 33537001 in the left side view, and choose Modify Row.Repeat the above step to maintain other items under the OTC Securities Option folder.Product TypeTransaction TypeActivity Category76J20020 | For all the listed Product Types/Transaction Types/Activity Categories, BP profiles and BP groups are assigned. |  |

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
| 2 | Access the SAP Fiori App | Open Manage Limits (TBL1). |  |  |
| 3 | Choose Limit Type | Select the Limit Type Y01 row and choose Create Limits. |  |  |
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
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Limits (TBL1). | The view is displayed. |  |
| 3 | Choose Limit Type | Select the Limit type Y07 row and choose Create Limits. |  |  |
| 4 | Edit Limits | Make the following entries, and choose Continue:Company Code: for example, 3310BusPartner: for example, 33537001 | The Edit Limits for Limit Type Y07: Create New Limit screen is displayed. |  |
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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Traders (S_ALR_87009302). | The Determine Work Area: Entry dialog displays. |  |
| 3 | Enter Work Area | Enter data and select Continue.Company Code: for example: 3310 | The Change View "Treasury: Traders": Overview screen is displayed. |  |
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

In this step, you map users with traders, providing a default trader when creating a new transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Risk Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define User Data (S_ALR_87007933). | The Change View "Treasury: User master data supplements": Overview screen is displayed. |  |
| 3 | Create a New Record | Choose New Entries, enter the following data, and choose Save:User name: for example: <Your user name>Trader: for example: TRADER02 | The data is saved. |  |

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

A trader must be defined before this step. Refer to [Define Traders](#unique_21) [page ] 26 step for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Trader Authorizations (TBT1). | The Create/Change Trans. Authorization for Trader: Init. Screen screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter data and select Enter.Trader: for example: TRADER02Company Code: for example: 3310 | The Create/Change Transaction Authorization for Traders screen is displayed. |  |
| 4 | Enter Authorization and Save | Select or unselect on the Authorization column and select Save.Note Make sure to authorize TRADER02 for the Derivatives and Securities transactions. | The data is saved as indicated by a message. For example: Transaction authorizations for trader TRADER02 are being saved. |  |

## Overview Table

This scope item consists of process steps provided in the following tables.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Open Security Account](#unique_25) [page ] 33 | Treasury Specialist - Back Office | Manage Securities Accounts (TRS_SEC_ACC) | The security account information is maintained. |
| [Create Security Class](#unique_26) [page ] 34 | Treasury Specialist - Back Office | Manage Security Classes (F8717) | The security class of the underlying securities transaction is maintained. |
| [Import Market Data](#unique_27) [page ] 36 | N/A |  | Market data is imported. |
| [Generate Limit Utilizations](#unique_28) [page ] 36 | Treasury Specialist - Middle Office | End-of-Day Processing (KLNACHT) | Limit utilization is determined and updated based on daily transactions and positions contained in the data pool. |
| [Check Limit Utilization Report](#unique_29) [page ] 37 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | Limit utilizations display. |
| [Create Securities Option Contract](#unique_30) [page ] 38 | Treasury Specialist - Front Office | Create OTC Option (TI71) | A securities option transaction is created. |
| [Set Settlement Status (Manually)](#unique_31) [page ] 41 | Treasury Specialist - Back Office | Process IR Derivatives - Collective Processing (TI92) | The TRM transaction is settled. |
| [Send Confirmation Email/Print](#unique_32) [page ] 43 | N/A |  | Confirmation correspondences are in delivered status. |
| [Check Correspondence Status](#unique_33) [page ] 43 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The status of correspondence objects displays. |
| [Receive Incoming Confirmation](#unique_34) [page ] 45 | Treasury Specialist - Back Office |  |  |
| [Find Deal and Match Deal Details](#unique_35) [page ] 45 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | An incoming correspondence is created. |
| [Set Settlement Status](#unique_36) [page ] 47 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) | The TRM transaction is settled. |
| [Option 1: Generate and Automatically Process Payment Request](#unique_37) [page ] 48 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_38) [page ] 51 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_39) [page ] 53 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank-Initiated Payment](#unique_40) [page ] 56 | N/A |  |  |
| [Post to General Ledger](#unique_41) [page ] 56 | Treasury Accountant | Process Business Transactions (TPM10);Fix, Pay and Post Flows (TBB1) | Cash flows related FI document is posted. |
| [Import Market Data](#unique_42) [page ] 59 | N/A |  | Market data is imported. |
| [Calculate or Maintain Fair Value of Transaction](#unique_43) [page ] 60 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA) | The fair value of transaction is calculated automatically, or maintained manually. |
| [Perform Key Date Valuation](#unique_44) [page ] 62 | Treasury Accountant | Run Valuation (TPM1) | The financial instrument is valued, related FI document is posted. |
| [Review Securities Option Status](#unique_45) [page ] 68 | Treasury Specialist - Front Office | Manage Financial Transactions (F6157) | The status of the transactions and conduct operations is reviewed. |
| [Post Derived Business Transactions](#unique_46) [page ] 72 | Treasury Accountant | Post Derived Business Transactions (TPM18) | Accounting document has been created in local GAAP (valuation area AE0). |
| [Define Financial Positions](#unique_47) [page ] 74 | Treasury Risk Manager | Define Financial Positions (FTR_FP_DEF) | A set of key figures is defined. |
| [Financial Status (Book Value)](#unique_48) [page ] 75 | Treasury Risk Manager | Financial Status (F2136) | Financial status on book values displays. |
| [Display Treasury Alerts - Posting](#unique_49) [page ] 76 | Treasury Accountant | Display Treasury Alerts - Posting (F4984) | Treasury alerts for posting display. |
| [Display Treasury Alerts- Settlement, Release and Payment](#unique_50) [page ] 77 | Treasury Specialist - Back Office | Display Treasury Alerts - Settlement (F4979) | Treasury alerts for various type of transactions display. |
| [Display Payment Schedule](#unique_51) [page ] 79 | Treasury Accountant | Display Payment Schedules (TJ04) | The payment schedule displays. |
| [Analyze NPV](#unique_52) [page ] 80 | Treasury Specialist - Middle Office | Analyze NPV (JBRX) | Calculate and display NPV result. |
| [Display Treasury Posting Journal](#unique_53) [page ] 81 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Posting journals display. |
| [Display Treasury Position Flows](#unique_54) [page ] 82 | Treasury Accountant | Display Treasury Position Flows (F1754) | Position Flow data displays. |
| [Display Treasury Position Values](#unique_55) [page ] 83 | Treasury Accountant | Display Treasury Position Values (F1867) | The position values data displays. |
| [Treasury Position Analysis](#unique_56) [page ] 84 | Treasury Accountant | Treasury Position Analysis | Position analysis data displays. |
| [Display Securities Account Class Positions](#unique_57) [page ] 84 | Treasury Accountant | Display Securities Account Class Positions (TPM40A) | Securities account class position list displays. |
| [Calculate Market Risk Key Figures](#unique_58) [page ] 85 | Treasury Specialist - Middle Office | Calculate Market Risk Key Figures (AISGENKF) | The NPV Result displays based on Portfolio Hierarchy. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Open Security Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before you create securities option transactions in the system, you need to maintain the security account information.

The following procedure describes the maintenance of security account for stock as an example.

Prerequisite

You have created the business partner 33537001 with the role of TR0152 Depository Bank.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Securities Accounts (TRS_SEC_ACC). | The Choose Securities Account and Company Code screen is displayed. |  |
| 3 | Enter Account Identifier | Enter a new unique identifier for the new Securities Account, and choose Create. Choose Create again on the popup screen of Create New Securities Account.Company Code: for example, 3310Securities Account: for example, STOCK_INVInfoChoose Create if a confirmation dialog pops up.If above account has been already created, you can choose Display or Change to either check or edit the account. | A new account is created. |  |
| 4 | Enter General Data of the Account | Enter the following data and move to the next tab:Securities Account ID: for example, STK33537001AE0Securities Account Type: for example, SAC Asset Securities Account | Move to the next tab. |  |
| 5 | Enter Bank Data | Enter the following data and choose Save:Depository Bank: for example, 33537001Line 1:Payment Currency: AEDHouse Bank: AEBK1Account ID: AEAC1Line 2:Payment Currency: USDHouse Bank: AEBK1Account ID: USDAC | The data is saved. |  |

### Create Security Class

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Before you create securities option transactions in the system, you need to maintain the security class of the underlying securities transaction.

The following procedure describes the maintenance of security class for stock as an example.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog New Object, then choose Continue.Securities Class ID: for example, ST_AE1Product Type: 01A stockNote You may have already created the above security class when running the Stock Management (5OD) test script. In this case, you can skip this step and use this existing security class for the underlying securities. | The New Object screen displays with previously specified Class ID. |  |
| 4 | Enter Header | On the Header tab, enter the following data:Security Class Name: for example, Stock #1Gen. Sec. Classification: for example, StockPlease switch to the Basic Data tab.A list of Secondary Indices is displayed under the Search Terms tab, where you can choose to enter some actual index values. | Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | On the Basic Data tab, enter the following data:In the Issue area,Issuer: for example, 33537003Nominal Value: for example, 1.00Issue Currency: for example, AEDSecurity Type: for example, Regist.security (2)Quotation: for example, Unit-quoted (2)Stock Category: for example, Common Stock (1) |  |  |
| 6 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: DFMCurrency Unit: for example, AED | Data is saved. |  |

### Import Market Data

Purpose

In this step, you import market data (securities price, security price volatility, reference interest rates, foreign exchange rates, credit spread, and so on) before the system can recognize its latest fair value and update the credit limit utilization when you enter a purchase transaction or run the end-of-day processing.

Prerequisite

You need to assign volatilities with moneyness to the underlying security class and enter values of volatilities with moneyness. Refer to the following step of the Market Rates Management – Manually via Upload(1XN).

- Assign Security Class for Volatilities with Moneyness for Securities Option

Procedure

Volatility with moneyness, securities price, and reference interest rate are mandatory market data for calculating risk-free NPV of the securities option. Enter these data by referring to the following sections of the Market Rates Management – Manually via Upload(1XN).

- Enter Values for Volatilities with Moneyness for Securities Option
- Enter Interest Rates
- Update Securities Price - Stock Management

If you need to get NPV with CVA and DVA, also run the following steps of the Market Rates Management – Manually via Upload(1XN) test script:

- Create Reference Entities for Business Partners
- Maintain Reference Entities
- Enter Credit Spreads

### Generate Limit Utilizations

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

You have imported the market data.

If security exists, the spot price needs to be maintained for the current date. Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open End-of-Day Processing (KLNACHT). | The End-of-Day Processing screen is displayed. |  |
| 3 | Enter Criteria of End-of-Day Processing | Make the following entries and choose Execute:Valuation Date: for example, <the current date>Determination Procedure: 10 to 20Company Code: 3310 | The system displays the message End-of-day processing was completed successfully. |  |

### Check Limit Utilization Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the limit utilization report.

Prerequisite

The Limit master records of your company was maintained in the system according to the Maintaining Credit Limit section in the Preliminary Steps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Execute:Limit Type: for example, Y01 or Y07Limit Utilization Base: for example, 1Determination Date: for example, <the current date>Limits Valid From: for example, <the current date> | An overview of the limit utilization in accordance with your selection criteria is displayed. |  |

### Create Securities Option Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a securities option transaction.

This step describes the creation of securities option for stock as an example.

Prerequisite

- The relevant Securities ID for the underlying securities transaction is created.
- The relevant Securities Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create OTC Option (TI71). | The Create OTC Option: Initial Screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and press Enter:Company Code: for example, 3310Product Type: for example, 76JTransaction Type: for example, 100Partner: for example, 33537001Security Class: for example, ST_AE1 | The OTC Option: Create Contract: Structure screen is displayed. |  |
| 4 | Enter Structure | On the OTC Option: Create Contract: Structure screen, enter the following data:In the Option group:Expiry Date: for example, ++2 (two months later)Exercise Type: for example, EuropeanSettlement: for example, Physical ExerciseTransactn Type: for example, 100Flow Type: for example, 0100In the Position group:Securities Account: for example, STOCK_INVIn the Date Details group:Position Value Date: for example, +2 (2 days after the Expiry DateIn the Amounts group:Number of Units: for example, 1000Price (Unit-Quoted): 80 AEDIn the Trading Data group:Exchange: for example, DFMIn the Premium group:Flow Type: for example, 1300Payment Date: for example, <the current date>Amount: for example, AED 100In the Contract Conclusion group:Contract Date: for example, <the current date> |  |  |
| 5 | Maintain Administration of New Deal | On the Administr. tab, enter the following data:Portfolio: for example, Y000Gen.Valn Class: for example, <select a proper Gen. Valn Class for transaction, for example, 43 Derivatives> | The Overview of Conditions screen is displayed. |  |
| 6 | Maintain Payment Details of New Deal | On the Payment Details tab, double-click on the outgoing row, and enter the following data:Payment Request, With: <select this checkbox>House Bank: for example, AEBK1Account ID: for example, AEAC1Payer/Payee: for example, 33537001Partner Bank: for example, AED1Payment Methods: for example, T |  |  |
| 7 | Save the New Deal | Choose Check to verify the input data. If no error message, choose Save.Note Write down the transaction number. | The securities option transaction is created. |  |

### Correspondence

Purpose

TRM transaction related information is transferred between you and your Business Partner. SAP Treasury and Risk Management (SAP TRM) provides standard correspondence functionalities with which you can communicate with Business Partner with a printout form via email.

This section describes the standard correspondence functionality that SAP TRM provides.

#### Set Settlement Status (Manually)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a securities option transaction is recorded and saved, it must be settled before you can perform further activities. After you get counterparty confirmation, you can settle the transaction via:

- Manual settlement: For example, if you receive counterparty confirmation e-mail, then you can use the following app to settle the transaction manually:
    - Manage Financial Transactions (F6157)

The following procedure describes the manual settlement process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the transaction number of the securities option you created previously> | The transaction is displayed on the screen. |  |
| 4 | Settle the Transaction | Select the transaction line and choose Settle. | The transaction data is displayed on the OTC Option: Settle Contract: Structure screen. |  |
| 5 | Save the Change | Choose Save. | The transaction is settled and saved. |  |
| 6 | Check the Status of the Transaction | Select the checkbox and choose Details at the end of the transaction line. | The OTC Option Display: Structure screen is displayed. |  |
| 7 | Check Status | Verify that the Activity field is in the Contract Settlement status. | The transaction has the Contract Settlement status. |  |

#### Correspondence with PDF Form

Purpose

Email/Print are all PDF form-related output. By default, SAP provides business profiles for several PDF forms (for example, PR_PRINT and PR_EMAIL).

- For any Business Partner assigned to profile PR_PRINT, when a financial transaction is created, a PDF form is sent to a predefined print queue. To view and print the PDF file, use the SAP Fiori app Maintain Print Queues (F1260). Once you check and confirm that the transaction information on the form is correct, you may then send the paper copy of the form to the Business Partner.
- For any Business Partner assigned profile PR_EMAIL, when a transaction is created, SAP automatically sends emails to the Business Partner.

Once you receive the counterparty confirmation about the transaction from your Business Partner, you can settle all the correspondence objects of the transaction.

- You can use the following apps to maintain your own settings for output:
    - Output Parameter Determination. You maintain your own rules for the output. For example, you can maintain email addresses of recipients. This rule overwrites the email address of the Business Partner for an external counterparty, or it overwrites the email address of User IDs for an internal counterparty.
    - Maintain Email Templates - Deprecated (F1306). You maintain your own email template with this app.
    - Maintain Form Templates (F1434). You maintain your own form template with this app.

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

In previous step, for the email channel, an outbound email is sent to the Business Partner. Normally, you will receive a counterparty confirmation from the Business Partner via email, phone, etc. This step is outside of SAP.

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
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Correspondence - Monitor (FTR_COMONI). | The Correspondence Monitor screen is displayed. |  |
| 3 | Enter Selection Criteria on the Initial View | Enter the following data and choose Execute:Correspondence group:Company Code: for example, 3310Financial Transaction group:Company Code: for example, 3310Transaction Number: for example, <the transaction number of the securities option you created previously>Note Make a note of the correspondence key for a COUNTERPARTY correspondence object. | Please note down the correspondence key numbers for COUNTERPARTY PRINT and COUNTERPARTY EMAIL. |  |
| 4 | Create | Choose Create. | The Options for Creating Correspondence Objects screen is displayed. |  |
| 5 | Create an Incoming Correspondence Object Referring to the Outgoing Correspondence Object | Enter the following data for groups and press Enter:Display Options group:Corresp. Category: 01 Transaction ActivitiesTransaction Details group:Company Code: for example, 3310Product Type: for example, <Product type you entered in the transaction>Incoming/Outgoing: I IncomingEntry Options: 05 Correspondence object as templateTemplate for Correspondence Object Data group:Correspondence Key: for example, <Enter the correspondence key number for COUNTERPARTY PRINT from the previous step> |  |  |
| 6 | Save | Choose Save.Note If the Automatic matching proposal view displays, choose Cancel. | The incoming correspondence object is created successfully and displayed on Correspondence monitor - Standard View view. |  |
| 7 | Match the Incoming Correspondence Object with the Outgoing Correspondence Objects for channel PRINT | Select the checkbox for the incoming correspondence object and choose Status Functions > Automatic Match . | The Automatic matching proposal screen is displayed. |  |
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

In the previous procedure, all of the correspondence objects of the transaction were matched successfully.

In this activity, you settle the transaction manually.

Procedure

Please refer to the following section of this test script to settle the contract:

- [Set Settlement Status (Manually)](#unique_31) [page ] 41

### Premium Payment

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log. |  |
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

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <the current date>Test Run: <select>Pay Only: <select this indicator> | Screen Payment Log - Test Run displays, you can check the payment information on this screen.If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect>Note Make a note of the key number displayed on this screen. | Screen Payment Log displays, payment request has been generated. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | Enter the following data, and choose Run:Derivatives: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous procedure>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.Up to and Including Due Date: <enter date on which the flow of financial transaction should be posted>, for example, <the current date>Test Run: <select> | The Payment Log - Test Run view displays. Review the payment information on this view.If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows screen, enter the following data, and choose Run:Test Run: <deselect> | The Payment Log view displays. A payment request is generated.Make note of the key number displayed on this view for use in the following procedures. |  |

###### Process Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the Automatic Payment Transactions for Payment Requests (F111) app to start the payment program for payment requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items), but on payment requests.

Prerequisite

A payment request has been generated in the previous procedure.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. |  |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). |  |  |
| 3 | Enter Run Date and Identification | Enter the following data and choose Parameters:Run Date: for example, <the current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | Enter the following data:Posting Date: for example, <the current date>Next payment run on: for example, <the current date + 3 days>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free Selection for payment run, enter the following data and choose Save:Key number: <the key number you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment Method Selection in All Cases: <select this indicator>Line Items of the Payment Documents: <select>Due Date Check: <select>If information Log created for all accounts displays, choose Continue.Choose Save on view Automatic Payment Transactions: Parameters. | The system displays the message Parameters have been entered. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat, and choose Schedule Job to confirm this dialog box.Message Proposal is running displays in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, choose Payments to check the payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests view, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data and choose Run:Run Date: for example, <the current date>Identification: for example, TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

##### Send Payment Medium File

Purpose

In this activity, you send the payment medium file to your house bank to facilitate the payment.

Procedure

If Bank Communication Management (BCM) is not implemented in your system, the payment medium file will be generated upon completion of the payment run in the previous step, provided that the relevant payment method uses the PMW format.

If BCM is implemented in your system, additional approvals may be required for a BCM batch before the payment medium file can be generated. For the approval process, please refer to the section Outgoing Payment with BCM Approval Process in the test script Advanced Cash Operations ([J78](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/J78)).

After payment medium file is created, there are two ways for sending the payment medium file to your house bank:

- If Multi-Bank Connectivity (MBC) is not enabled, please use app Manage Payment Media (F1868) to check and download the payment medium file, and send the file to the bank via the previously agreed-upon method. Further details are provided in test script Bank Integration with File Interface ([1EG](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/1EG)).
- If MBC is enabled and the relevant PMW format uses the alternative format type designated for MBC, then the payment medium file can be automatically sent to MBC. Bank will then retrieve the payment medium file from MBC and execute the payment. Further details are provided in test script Bank Integration with SAP Multi-Bank Connectivity ([16R](https://me.sap.com/processnavigator/SolS/BP_CLD_ENTPR/latest/SolP/16R)).

#### Bank-Initiated Payment

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

Prerequisite

The outgoing payment which should be handled via payment request (if there is) for this transaction has been processed in previous step Generate Payment Request with the Pay Only option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | Enter the following data and choose Execute:Derivatives: <select>Company Code: for example 3310Transaction: <the securities option transaction number>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <the current date>Test Run: <select>Post Operational Only: <select> | Note Screen Posting Log: Posted Business Transactions is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen.Note There is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria, you can skip the current test step and continue the test step with the Process Business Transactions app. |  |
| 4 | Back | Choose Back. | The Treasury: Post Flows screen is displayed. |  |
| 5 | Production Run | Enter the following data and choose Execute:Test Run: <deselect> | Screen Posting Log: Posted Business Transactions is displayed, and the accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 6 | Access Another SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 7 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select>Company code: for example, 3310Valuation Area: for example AE0Limiting by Transaction Number: <deselect>Limit by Subledger Pos.: <select>Transaction: <the securities option transaction number>Test Run: <select> | The Test Run: Post/Reverse Business Transactions screen is displayed.If message You have not selected any business transactions is displayed, that means there is no posting needed for your selection criteria, you can skip current step. |  |
| 8 | Check Test Run Result | Choose Select All and choose Choose Those to Post, and choose Execute. | The Test Run: Display Posted/Reversed Business Transactionsscreen is displayed. |  |
| 9 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for local GAAP (valuation area AE0) on this screen.Note No posting is created since this is a test run. |  |
| 10 | Back | Choose Back. | The Process Business Transactions screen is displayed. |  |
| 11 | Deselect Test Run | Enter the following data and choose Execute:Test Run: <deselect> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 12 | Production Run | Choose Select All and choose Choose Those to Post, and choose Execute. | The Update Run: Display Posted/Reversed Business Transactions screen is displayed. |  |
| 13 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed. The accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |  |

### Period-end Closing

This section describes activities for period-end closing (usually executed at month end), including:

- [Import Market Data](#unique_42) [page ] 59
- [Calculate or Maintain Fair Value of Transaction](#unique_43) [page ] 60
- [Perform Key Date Valuation](#unique_44) [page ] 62

#### Import Market Data

Purpose

In this step, you import market data (securities price, security price volatility, reference interest rates, foreign exchange rates, credit spread, and so on) for the evaluation date into the system before the net present value (NPV) of the securities option transaction can be calculated via the Calculate Net Present Values - With CVA and DVA (TPM60CVA) app.

Prerequisite

You need to assign volatilities with moneyness to the underlying security class and enter values of volatilities with moneyness. Refer to the following step of the Market Rates Management – Manually via Upload(1XN).

- Assign Security Class for Volatilities with Moneyness for Securities Option

Procedure

Volatility with moneyness, securities price, and reference interest rate are mandatory market data for calculating risk-free NPV of the securities option. Enter these data by referring to the following sections of the Market Rates Management – Manually via Upload(1XN).

- Enter Values for Volatilities with Moneyness for Securities Option
- Enter Interest Rates
- Update Securities Price - Stock Management

If you need to get NPV with CVA and DVA, also run the following steps of the (1XN) test script:

- Create Reference Entities for Business Partners
- Maintain Reference Entities
- Enter Credit Spreads

|  |
| --- |
| Note You need to enter value for the period end, for example, the end of the current month. |

#### Calculate or Maintain Fair Value of Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you calculate via app Calculate Net Present Values - With CVA and DVA (TPM60CVA) or maintain manually the NPV of the securities option at the period end. The net present values can be calculated automatically by the Market Risk Analyzer (MRA) and saved to table VTVBAR. These values can then be used for the accounting valuation. In addition, you can also maintain the relevant net present value manually.

Predelivered configuration in MRA provides three options when calculating NPV automatically via app Calculate Net Present Values - With CVA and DVA (TPM60CVA):

- Risk-free NPV: using the evaluation type that does not contain a credit spread curve, the system only calculates the risk-free NPV.
- Risk-based NPV with credit spread curve: using the evaluation type that contains credit spread curve, system calculates risk-free NPV by using risk-free yield curve, and calculates the (risk-based) NPV, which also accounts for credit spreads.
- Risk-based NPV with basis spread curve and credit spread curve: using the evaluation type that contains basis spread curve and credit spread curve, system calculates risk-free NPV by using risk-free yield curve and basis spreads curve, and calculates the (risk-based) NPV, which also accounts for credit spreads.

There are two kinds of calculation method for CVA and DVA:

- Based on Expected Exposures
- Difference method

NPV = risk-free NPV - CVA - DVA.

|  |
| --- |
| Note Currently, the TPM60CVA only supports the NPV calculation for securities option of stock (both European and American styles) and bond (only European style). The NPV calculation of other securities type as underlying, such as money market fund (MMF), subscription right and shareholding are not supported yet.The Calculate Net Present Values - With CVA and DVA (TPM60CVA) can only calculates NPV of securities options with implied volatilities. NPV calculation with historical volatility is not supported yet. |

Prerequisite

You have maintained the market data for the evaluation date in the previous step.

Procedure

Option 1: Calculate NPV Automatically

|  |
| --- |
| Note To schedule a background job for option 1, see the corresponding step in the Appendix. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute:Evaluation Parameter Derivatn: <deselect>Select OTC Transactions: <select>Company Code: for example, 3310Transaction: <the securities option transaction number>Evaluation Date: for example, <last date of the current month>CVD/DVA Type: To calculate risk-free NPV, leave blank. To calculate risk-based NPV and CVA/DVA, enter Y01.Evaluation Type: To calculate risk-free NPV, enter Y001. To calculate risk-based NPV and CVA/DVA, enter Y002Test Run: <deselect>Price/NPV Type: 001Save Values with Warnings: <select>Detail Log: <select> | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays with the NPV, risk-free NPV, CVA, DVA of each transaction.You can also review different information by selecting additional buttons on this view:Single Transaction:CVA/DVA Key FiguresDetailed LogCalculation BasesError Log |  |

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

In this step, you run valuation for the securities option to update its position based on the net present value calculated or manually maintained in the previous step, and post the result to financial accounting.

|  |
| --- |
| Note To schedule a background job for this step, see the corresponding step in the Appendix section. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Run Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | Make the following entries and choose Execute:In the Product Groups area,OTC Transactions: <select>In the General Selections area,Company Code: for example, 3310Valuation Area: for example, AE0In the OTC Transactions area,Transaction: <the securities option transaction number>In the Valuation Parameters area,Key Date for Valuation: for example, <the last date of the current month>Valuation Category: for example, Mid-year Valuation with ResetNote When the period end is also the year end, use the Valuation Category of Year End Valuation.Test Run: <select> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Test Run Valuation | Choose Run Valuation.Note If the Message dialog box displays, choose Continue. | The Valuation Log screen is displayed.If a red traffic light status is shown, select and review the error message. Correct the issue and perform test run again, until the error is resolved.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Note If there is no simulated posting, your selected transaction does not require valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the Run Valuation screen is displayed.Change the following data and choose Execute:Test Run: <deselect> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 6 | Execute Valuation for Production Run | Choose Run Valuation. | The Valuation Log screen is displayed.To review the simulated posting information for local GAAP (valuation area AE0), choose Logs + Messages. No posting is created because this is a test run.Because this is a production run, the accounting document is created in local GAAP (valuation area AE0). |  |

### Transaction is Mature

Purpose

This section describes the required operations when the option transaction is mature. You may decide whether to exercise or expire the option and conduct the following operations.

#### Import Market Data

Purpose

In this step, you import market data (securities price, security price volatility, reference interest rates, foreign exchange rates, credit spread, and so on) for the maturity date (the date on which you exercise or expire the option) into the system before the net present value (NPV) of the securities option transaction can be calculated via the Calculate Net Present Values - With CVA and DVA (TPM60CVA) app.

Prerequisite

You need to assign volatilities with moneyness to the underlying security class and enter values of volatilities with moneyness. Refer to the following step of the Market Rates Management – Manually via Upload(1XN).

- Assign Security Class for Volatilities with Moneyness for Securities Option

Procedure

Volatility with moneyness, securities price, and reference interest rate are mandatory market data for calculating risk-free NPV of the securities option. Enter these data by referring to the following sections of the Market Rates Management – Manually via Upload(1XN).

- Enter Values for Volatilities with Moneyness for Securities Option
- Enter Interest Rates
- Update Securities Price - Stock Management

If you need to get NPV with CVA and DVA, also run the following steps of the (1XN) test script:

- Create Reference Entities for Business Partners
- Maintain Reference Entities
- Enter Credit Spreads

#### Calculate or Maintain Fair Value of Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you calculate via app Calculate Net Present Values - With CVA and DVA (TPM60CVA) or maintain manually the NPV of the securities option on the maturity date. The net present values can be calculated automatically by the Market Risk Analyzer (MRA) and saved to table VTVBAR. These values can then be used for the accounting valuation. In addition, you can also maintain the relevant net present value manually.

Predelivered configuration in MRA provides three options when calculating NPV automatically via app Calculate Net Present Values - With CVA and DVA (TPM60CVA):

- Risk-free NPV: using the evaluation type that does not contain a credit spread curve, the system only calculates the risk-free NPV.
- Risk-based NPV with credit spread curve: using the evaluation type that contains credit spread curve, system calculates risk-free NPV by using risk-free yield curve, and calculates the (risk-based) NPV, which also accounts for credit spreads.
- Risk-based NPV with basis spread curve and credit spread curve: using the evaluation type that contains basis spread curve and credit spread curve, system calculates risk-free NPV by using risk-free yield curve and basis spreads curve, and calculates the (risk-based) NPV, which also accounts for credit spreads.

There are two kinds of calculation method for CVA and DVA:

- Based on Expected Exposures
- Difference method

NPV = risk-free NPV - CVA - DVA.

|  |
| --- |
| Note Currently, the TPM60CVA only supports the NPV calculation for securities option of stock (both European and American styles) and bond (only European style). The NPV calculation of other securities type as underlying, such as money market fund (MMF), subscription right and shareholding are not supported yet.The Calculate Net Present Values - With CVA and DVA (TPM60CVA) can only calculates NPV of securities options with implied volatilities. NPV calculation with historical volatility is not supported yet. |

Prerequisite

You have maintained the market data for the evaluation date in the previous step.

Procedure

Option 1: Calculate NPV Automatically

|  |
| --- |
| Note To schedule a background job for option 1, see the corresponding step in the Appendix. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Execute:Evaluation Parameter Derivatn: <deselect>Select OTC Transactions: <select>Company Code: for example, 3310Transaction: <the securities option transaction number>Evaluation Date: for example, <the maturity date>CVD/DVA Type: To calculate risk-free NPV, leave blank. To calculate risk-based NPV and CVA/DVA, enter Y01.Evaluation Type: To calculate risk-free NPV, enter Y001. To calculate risk-based NPV and CVA/DVA, enter Y002Test Run: <deselect>Price/NPV Type: 001Save Values with Warnings: <select>Detail Log: <select> | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays with the NPV, risk-free NPV, CVA, DVA of each transaction.You can also review different information by selecting additional buttons on this view:Single Transaction:CVA/DVA Key FiguresDetailed LogCalculation BasesError Log |  |

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

#### Review Securities Option Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the status of the transactions and conduct operations accordingly.

You can either exercise or expire the securities option transaction with status Contract Settlement.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <Numbers of Maturing transactions> | The transaction is displayed on the screen. |  |

##### Decide to Exercise

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you exercise the securities option.

Prerequisites

A securities option transaction exists and is updated to the Contract Settlement status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the number of securities option transaction you want to exercise> | The transaction is displayed on the screen. |  |
| 4 | Select a Transaction and Exercise | Select a transaction with the following criteria and choose Exercise:Activity: Contract Settlement | The Exercise OTC Option: Structure screen is displayed. |  |
| 5 | Enter Data and Save | Enter the following criteria and choose Save:Confirm the Exercise Date:If Exercise Type is European, the Exercise Date should be equal to Exercise Period.If Exercise Type is American, the Exercise Date should be earlier than or equal to Exercise Period.Note Make sure the Contract Date is earlier than the Exercise Period. | The data is saved without error. |  |

##### Create Securities Contract

Purpose

In this step, you create the underlying securities transaction in the system after you exercise the securities option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the number of the securities option transaction> | The transaction is displayed on the screen. |  |
| 4 | Select a Transaction and Settle | Choose a transaction that meets the following criteria and choose Settle:Activity: Exercise Settlement | The OTC Option: Settle Exercise: Structure screen is displayed. |  |
| 5 | Choose Save to Create Securities Transaction | Choose Save. | The Create Stock: Structure screen is displayed. |  |
| 6 | Confirm Data and Save | Review the automatically generated securities transaction details and choose Save. | The data is saved and the new transaction number is generated. |  |

##### Decide to Expire

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step describes the process for the other operation option to expire a securities option.

Prerequisites

A securities option transaction exists, with the Contract Settlement status.

|  |
| --- |
| Note If you have already exercised the securities option, you may need to create and settle a new one to expire for the testing purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Go:Company Code: for example, 3310Transaction: <the number of the securities option transaction you want to expire> | The transaction is displayed on the screen. |  |
| 4 | Select a Transaction and Exercise | Choose a transaction that meets the following criteria and choose Expiration:Activity Cat. Name: Contract Settlement | The Exercise OTC Option: Structure screen is displayed. |  |
| 5 | Enter Data and Save | Enter data and choose Save.Note Make sure the Contract Date is earlier than the Exercise Period. | The data is saved without error. |  |

### Post Derived Business Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you fix and post derived business transactions. Usually this occurs for realized profit and loss when a deal is mature.

|  |
| --- |
| Note To schedule a background job for this procedure, see the corresponding step in the Appendix. |

Prerequisite

The maturity date of transaction is reached.

The financial transaction is created, settled, and posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Derived Business Transactions (TPM18). | The Post Derived Business Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select>Company Code: for example, 3310Valuation Area: for example, AE0OTC Transactions: <the securities option transaction number>TRL Date: <maturity date of transaction>Test Run: <select>If the system displays the message Are you sure that you want to select future business transactions, choose Enter. | The Fix and Post Derived Business Transactions screen is displayed.Note If the No scheduled derived business transactions were found for the selection message displays, no derived transaction is available for your selection. You can skip this step. |  |
| 4 | Fix and Post for Test Run | Choose Fix. | The Posting Log: Posted Business Transactions view displays. Review the simulated posting information for local GAAP (valuation area AE0).Note No posting is created since this is a test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial view of this app. Change the following data and choose Execute:Test Run: <deselect>If the system displays the message Are you sure that you want to select future business transactions, choose Enter. | The Fix and Post Derived Business Transactions screen is displayed. |  |
| 6 | Fix and Post for Production Run | Choose Fix. | The Posting Log: Posted Business Transactions view displays. The posting information for local GAAP (valuation area US0) and the accounting document are created in local GAAP (valuation area AE0). |  |

### Reports

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define Financial Positions (FTR_FP_DEF). | The "Maintain Financial Position Groups": Change screen is displayed. |  |
| 3 | Maintain Key Figure Groups | Select New Entries.Enter data for a record of new entry and select Save.Financial Position Group: for example, FPG_SOFinancial Position Group Description: for example, Securities option positionAssets/Liabilities: for example, Assets | The data is saved.Note If FPG_SO is already created for the same purpose, you can skip this step and use the existing record. |  |
| 4 | Maintain Key Figures | Switch to Maintain Financial Positions tab.Enter data and choose Save.Financial Position: for example, FPG_SOFinancial Position Description: for example, Securities option positionFinancial Position Group: for example, FPG_SOData Source: for example, Treasury Position Management | The data is saved. |  |
| 5 | Maintain Selections | Select one financial position and select Maintain Selections, and make the following entries:Product Type = 76JTransaction Type = 100 to 200Posting Status = 2Choose Back and choose Save. | The data is saved. |  |

#### Financial Status (Book Value)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the financial status of book values.

Prerequisite

You have defined the financial position group and the financial position as described in the [Define Financial Positions](#unique_47) [page ] 74 step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Financial Status (F2136). | The Financial Status - Book Value screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, <the current date>Display Currency : for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays per the filter values. |  |

#### Display Treasury Alerts - Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the treasury alerts for posting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Alerts - Posting (F4984). | The Display Treasury Alerts - Posting screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Alerts screen, enter the following data and choose Go:Issue Message For: PostingCompany Code: for example, 3310 | Alerts data is displayed per the filter values. |  |

#### Display Treasury Alerts- Settlement, Release and Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display treasury alerts for various type of transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Alerts - Settlement (F4979). | The Display Treasury Alerts - Settlement view displays with Issue Message For: Settlement. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Alerts - Posting screen and enter following data:Issue Message For: SettlementCompany Code: for example, 3310and choose Go. | Alerts data displays per the filter values. |  |
| 4 | Confirm Alerts for Other Transactions | Select other values in the Issue MessageFor field.ReleasePaymentCorrespondenceInterest Rates |  |  |
| 5 | Select Display Treasury Alerts Tiles with Release | Return to the Home view and open Display Treasury Alerts - Release (F4980). | The Display Treasury Alerts - Release view displays, with Issue Message For:Release. |  |
| 6 | Select Display Treasury Alerts Tiles with Payment | Return to the Home view and open Display Treasury Alerts - Payment (F4981). | The Display Treasury Alerts - Payment view displays, with Issue Message For:Payment. |  |
| 7 | Select Display Treasury Alerts Tiles with Interest Rates | Return to the Home view and open Display Treasury Alerts - Interest Rates (F4982). | The Display Treasury Alerts - Interest Rates view displays, with Issue Message For:Interest Rates. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Payments (TPM20A). | The Payment Journal screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Execute.Company Code: for example, 3310Product Type: 76J | The payment journals display. |  |
| 4 | Review Data | Review the data displayed on the screen. You can also choose Original business transaction or Details to drill down for more details. |  |  |

#### Display Payment Schedule

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the payment schedule for securities option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedules screen is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:OTC Transactions: <select>Company Code: for example, 3310End of Term in the Future: <select>End of Term in Lapsed: <select>Payment Period: for example, <the current date> to <the current date + 12 months>Payment Status: for example, 1Output Error Log: <select> | You can check the payment schedule report. |  |

#### Analyze NPV

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you calculate and display the Net Present Value (NPV) result.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze NPV (JBRX). | The NPV Analysis: Display of Single Values screen is displayed. |  |
| 3 | Enter Selection Criteria of Gen. Selection | On the NPV Analysis: Display of Single Values screen, enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <the current date>Horizon: for example, <the end date of the current month>Portfolio Hierarchy: for example, 100 |  | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |
| 4 | Enter Selection Criteria of Characteristics | Choose the Characteristics tap, enter the following data then choose Execute:Company Code: for example, 3310Product Type: for example, 76J | The NPV Result displays based on Portfolio Hierarchy. |  |

#### Display Treasury Posting Journal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the posting journals of securities option transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Product Group: for example, OTC TransactionsCompany Code: for example, 3310 | The posting journals display per the filter values. |  |

#### Display Treasury Position Flows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the treasury position flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Position Flows screen, enter following data and choose Go:Product Group: for example: OTC TransactionsCompany code: for example, 3310 | Position Flow data is displays according to the filter values. |  |

#### Display Treasury Position Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the treasury position values.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Position Values (F1867). | The Display Treasury Position Values screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, <the current date>Product Group: for example, OTC TransactionsNote You may have to adapt filter to make the Product Group filter available. The Product Group is in the Position Values filter group.Company Code: for example, 3310Valuation Area: for example, AE0 | The position values data displays per the filter values. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Treasury Position Analysis. | The Treasury Position Analysis screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following selection criteria and choose Go.Key Date: for example, <the current date>Include Planned Data: for example, 1Valuation Area: for example, AE0Company Code: for example, 3310Product Type: for example, 76J | The position analysis data displays per the filter values. |  |

#### Display Securities Account Class Positions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display securities account class position list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Securities Account Class Positions (TPM40A). | The Display Securities Account Class Position List screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Securities Account Class Position List screen, enter the following data and choose Execute:Company Code: for example, 3310Sec. Class ID Number: for example, <Security class ID number(s) for which has been created>Securities account: for example, <Security account for which has been created>Position Value Date: for example, <the current date> | The position is displayed. |  |

#### Calculate Market Risk Key Figures

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can use this function to calculate online and display the key figures for NPV analysis and sensitivity key figures for a selection of transactions. You can also use the key figures that have been calculated as the basis for defining formula-based key figures, and display them with the NPV and sensitivity key figures.

Prerequisite

You have maintained the report layout for key figures. See [Defining Report Layout for Calculate Market Risk Key Figures](#unique_72) [page ] 103 in the Appendix.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Calculate Market Risk Key Figures (AISGENKF). | The Single Value Analysis for Generic Key Figures screen is displayed. |  |
| 3 | Enter Selection Criteria of Gen. Selection | On the Single Value Analysis for Generic Key Figures screen, enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <the current date>Horizon: for example, <end date of the current month>Report Layout: for example, Y01 or other Report Layout you createdPortfolio Hierarchy: for example, 100 |  | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |
| 4 | Enter Selection Criteria | Choose the Characteristics tab, enter the following data and choose Execute:Company Code: for example, 3310Product Type: for example, 76J | The Single Value Analysis for assigned Report Layout is displayed. |  |

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

In this step, you change position indicator.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Position Indicator (TPM57A). | The Display Position Indicator screen is displayed. |  |
| 3 | Enter Parameters | On the Display Position Indicator screen, enter the following data then choose Enter:Product Group: for example, OTC TransactionsCompany Code: for example, 3310General Valuation Class: for example, 43Transaction: <the securities option transaction number> | The Subledger Position Indicator table is displayed.If you would like to make a change, please make following operation on the initial screen.Click on Menu > Position Indicator > Change . |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Schedule Treasury Middle Office Jobs (F2772). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information for New Job | On the Template Selection area, enter following data then choose Step 2:Job Template: for example, <End of Day Processing>Job Name: for example, <End of Day Processing> | You've chosen the job template, and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, enter the following data then choose Step 3:For Start Immediately case:Start Immediately: <select>For Recurrence case:Start Immediately: <deselect>Choose Define Recurrence Pattern to define the recurrence pattern in the Scheduling Information dialog box.Start: for example, <the current date/the current time>Recurrence Pattern: for example, DailyEvery: for example, 1End: for example, after 7 Occurrence(s)On Non-Working Day: Run on next Working DayNote Schedule this job after back office's job for generating payment request by using the same job template. | You've enter the scheduling recurrence pattern, and are navigated to the Parameters area. |  |
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
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and in the Scheduling Information dialog box, enter the following data:Start Immediately: <deselect this checkbox>Job Start: for example, <the current date and time default>Time Zone: <select a time zone or use default>Recurrence Pattern: for example, DailyEvery: for example, 1Day(s)End: for example, select After and then enter 7 occurrence(s)On Non-Working Days: for example, No RestrictionChoose OK, and choose Step 3.Note If you would rather to start job at once, select Start Immediately checkbox. | You've defined the recurrence pattern and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area,In the Application sub-area, select one or more proper product groupIn the General Selection sub-area, enter the following data:Company Code: for example, 3310Transaction: <enter transaction numbers if you'd like to limit transactions>Product Type: <enter product types if you'd like to limit product types>Due Date (Dynamic): for example, 0On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.In the Posting Control sub-area,Test Run: <deselect this checkbox>Pay Only: <choose this radio button>Note You can also choose the Post All Valuation Areas radio button, if you want to post to all valuation areas |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

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
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information dialog box :Start Immediately: <deselect this checkbox>Job Start: for example, <the current date and time>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day:for example, Run on next Working DayChoose OK, and choose Step 3.Note If you would like to start job at once, select the Start Immediately checkbox.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
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
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <the current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Product Groups sub-area, select one or more product groups.Company Code: for example, 3310Valuation Area: for example, AE0, or leave it blank (run for all valuation areas)In the Limit by Transaction Number sub-area, make the following selection:Limit by Transaction Number: <deselect this checkbox>In the Limit by Subledger Positions sub-area, make the following selection:Limit by Subledger Pos.: <select this checkbox>Product Type: <enter product types if you'd like to limit product types>Transaction: <enter transaction numbers if you'd like to limit transactions>In the Limit by Business Transactions sub-area, make the following selection:Trans. to Be Fixed/Posted: <select this checkbox>In the Posting Control sub-area, make the following selection:Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

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
| 4 | Enter General Information for New Job | In the General Information sub-area, enter the following data, and choose Step 2:Job Template: Calculate Market Risk Key FiguresJob Name: for example, Calculate Market Risk Key FiguresNote You can delete the existing market risk key figure values on the specified evaluation date by the Delete Market Risk Key Figures job template. |  |  |
| 5 | Enter Parameters for New Job | In the Parameters area, enter the following data, and choose Step 3:Start Immediately: <select this checkbox> |  |  |
| 6 | Enter Selection Data for New Job | On the General tab, enter the following data:Basic Run: <select this checkbox>Adjustment Run: <deselect this checkbox>Note The adjustment run processes new financial objects and financial objects for which errors have occurred in the base run.Market Risk Key Figure Set: for example, <MRK01, and MRK02, the key figure set you maintained>Evaluation Date (Dynamic): for example, <the current date, or enter the evaluation date>Volas + Correlations: <deselect this checkbox, determine whether calculate statistical figure as volatilities or correlations> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are back to the initial screen, and the job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose  at the end of the row for the job you just scheduled. | The Job Details screen is displayed.If it is in status Finished (depends on parameters you entered for Scheduling Options), click on the icon beside Results, a new window will open and you can check the result of this finished job. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | Choose Create. | The New Job screen is displayed. |  |
| 4 | Enter General Information | In the Template Selections area, enter the following data, and choose Step 2:Job Template: Run ValuationJob Name: for example, Run Valuation | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, enter the following data, and choose Step 3:Start Immediately: <deselect this checkbox>Start: for example, <first day of next month for this year and at time 03:00>Note Schedule your run time to be later than the Treasury - Calculate Net Present Value - With CVA and DVA job. | You've defined the scheduling option and are navigated to the Parameters area. |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:Company Code: for example, 3310Valuation Area: for example, AE0,or leave it blank (run for all valuation areas)In the OTC Transactions sub-area, enter the following data:Transaction: <enter transaction numbers if you'd like to limit transactions>In the Valuation Parameters sub-area, enter the following data:Key Date for Val. (Dynamic): for example, <last date of current month>Valuation Category: for example, select <Mid-year Valuation with Reset>Note When the Period End is also the Year End, the Valuation Category Year End Valuation is used.In the Posting Control sub-area, make the following data:Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

### Accounting

Purpose

This section described some accounting relevant activities which are not described in the Test Procedures section.

#### Reverse Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This step allows you to reverse posted period end valuation for the deal.

For example, if you have done the period end valuation with incorrect currency rates or incorrect evaluation type. This would lead to wrong accounting results which need to be reversed.

Prerequisite

The period end valuation of the deal has been posted.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Reverse Valuation (TPM2). | The Reverse Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Reverse Valuation screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Company code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example, AE0Sec. Class ID Number: <Security class ID number(s) for which valuation has been executed>Securities Account: <Securities account(s) for which valuation has been executed>Key Date for Valuation: for example, <the date on which the reversal should take place>Reasons for Reversal: for example, 04 Other reasonsTest Run: <select this checkbox> | The Display Positions to be Reversed screen is displayed. |  |
| 4 | Reverse Valuation for Test Run | On the Display Positions to be Reversed screen, choose Reverse Valuation. | The screen Reversal Log: Reversed Business Transactions is displayed, and message Valuation (test run) has been successfully reversed shows up.Note You can check the simulated reversal posting information on this screen, please note there is no posting created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Positions to be Reversed screen is displayed. |  |
| 6 | Reverse Valuation for Production Run | On the Display Positions to be Reversed screen, choose Reverse Valuation (TPM2). | The screen Reversal Log: Reversed Business Transactions is displayed, and message Valuation has been successfully reversed shows up.Note You can check the posting on this screen, this time, accounting document for reversal has been created. |  |

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

In this step, you can create market data shifts to analyze key figures with modified market data, which will be used in the Defining Report Layout for Calculate Market Risk Key Figures step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Market Data Shift (JBR0) | The Edit Market Data Shifts screen is displayed. |  |
| 3 | Enter Market Data Shifts Name | On the Edit Market Data Shifts screen, enter the following data and choose Create:Market Data Shift: for example, 1 | The Define Market Data Shifts screen is displayed. |  |
| 4 | Define Market Data Shift | On the Edit Market Data Shifts screen, enter the following data.Short Name: for example, <Market Data Shift 0001> |  |  |
| 5 | Maintain Yield Curves of Market Data Shift | On the Edit Market Data Shifts screen, choose the Yield Curves tab, choose the Insert Row button, then enter the following data and choose Save.Short Name: for example, Euro Depo ShiftCurrency: for example, AEDYC. Type: for example, 0001Ref.Int.Rate: for example, AEDM03EIBPercentage: for example, 2 | Market Data Shift is saved. |  |

#### Maintain Scenarios

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a scenario. A scenario is a market data record which can contain current market data, exchange rates, exchange rate volatilities, yield curves, interest rate volatilities, e.g. you can create scenarios, which represent market situations you consider possible or probable (for example, a high interest rate scenario with an inverted yield curve).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Scenarios (TV21). | The Scenario Admin: Initial Screen screen is displayed. |  |
| 3 | Enter Scenario Name | On the Scenario Admin: Initial Screen screen, enter the following data and choose Create:Scenario: for example, 1 | The Create Scenario 1 screen is displayed. |  |
| 4 | Maintain Scenario | On the Create Scenario 1 screen, enter the following data:Scenario: Full Name: for example, Scenario 1Scenario: Short Name: for example, Scenario 1 |  |  |
| 5 | Maintain Exch. Rates of Scenario | On the Create Scenario 1 screen, choose the Exchange Rates tab, then enter the following data:Reference Currency: for example, AEDIn the Other Currencies area, choose Insert Row, enter the following data:Currency: for example, USDBid Rate: for example, 1.2Ask Rate: for example, 1.2Then choose Save.Note Market Data Shift is parameter shifts based on market data imported; for scenario, you can maintain parameters without reference. | Scenario is saved. |  |

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
| 3 | Access Report Layout Definition Screen | On the Calculate Market Risk Key Figures screen, enter the Evaluation Currency and Evaluation Type, and choose Define Report Layout. | The "Key Figure Layout": Change screen is displayed. |  |
| 4 | Create Layout-ID Entries | On the Change View "Key Figures Layout": Overview screen, Choose New Entries, then insert the following data in the Key Figure Layout form and Save:ROW1Layout-ID: for example, Y01Short Name: for example, NPV/BPV/DurationLong Name: for example, NPV/BPV/DurationROW2Layout-ID: for example, Y02Short Name: for example, NPV + Market Data shiftsLong Name: for example, NPV + Market Data shifts | Two new entries have been created. |  |
| 5 | Access Key Figures Maintain Screen | On the Change View "Key Figures": Overview screen, select the checkbox of Layout-ID Y01, then double click on the Key Figures folder in the Dialog Structure panel. | The Change View "Key Figures": Overview screen is displayed in the main area. |  |
| 6 | Maintain Key Figures of Layout | On the Change View "Key Figures": Overview screen, choose New Entries and then insert the following data in the Key Figures form:ROW1Key Figure Name: for example, BARWERTPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDec.Places: for example, 0ROW2Key Figure Name: for example, BPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_BASE_POINTShort Name: for example, BPVShift Rule: for example, 0Dec.Places: for example, 0ROW3Key Figure Name: for example, CRFNPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, RISK_FREE_NPVShort Name: for example, Current Risk Free NPVShift Rule: for example, 0Dec.Places: for example, 0ROW4Key Figure Name: for example, DURATION1Pos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_FWDURATIONShort Name: for example, Modified DurationShift Rule: for example, 0Dec.Places: for example, 0ROW5Key Figure Name: for example, DURATION2Pos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_MACAULAYShort Name: for example, Macaulay DurationShift Rule: for example, 0Dec.Places: for example, 0and Save. | The New Entries: Overview of Added Entries screen displays allowing entry of the Key Figures name and configuration settings. |  |
| 7 | Access Key Figures Maintain Screen | Go back to the Change View "Key Figure Layout": Overview screen, select the checkbox of Layout-ID Y02, then double click on the Key Figures folder in the Dialog Structure panel. |  |  |
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
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Market Risk Key Figure Sets (AFWKF_SET). | The Change View "Market Risk Key Figure Set": Overview screen is displayed. |  |
| 3 | Define Risk Factor Set | On the Change View "Market Risk Key Figure Set": Overview screen, double click on the Risk Factor Set folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Factor Set form:RiskF. Set: for example, R01Description: for example, Risk Factor Set with FX Rate and Yld CurvesFX Risk: <select the checkbox>IR Risk: <select the checkbox>Then select the created entry, double click on the Risk Currency folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Currency form:Row 1Currency: for example, USDlR Risk: <select the checkbox>Then double click on the Interest Rate Term folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Interest Rate Term form and choose Save:Row 1Term: for example, 1Time Unit: for example, MonthRow 2Term: for example, 3Time Unit: for example, MonthRow 3Term: for example, 6Time Unit: for example, MonthRow 4Term: for example, 1Time Unit: for example, Year | A new risk factor set is created. |  |
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

In this activity, you display the limit overview.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Limit Overview (TBL3). | The Overview of Limits screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Overview of Limits screen, enter the following data and choose Execute:Limit Type: for example, Y01 to Y09Company Code: for example, 3310 | The Display Limits for Limit Types: Overview screen is displayed. |  |

### Change Counterparty

#### Change Counterparty of Financial Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you change the counterparty of financial transactions.

Prerequisite

Ensure that the 33537001 partner is created. For more information, see the Create Business Partner for Treasury and Risk Management - MDS (22G) master data script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Change Counterparty - Financial Transaction (TRTM_CHG_PARTNER). | The Change Counterparty of a Financial Transaction screen is displayed. |  |
| 3 | Test Run | Make the following entries and choose Execute:Company Code: for example, 3310New Partner: for example, 33537001Change Effective From: enter the date from which the change will be effective. For example, <the current date>Test Run: <select> | The Change Counterparty of a Financial Transaction view displays with Test Run: List of Successfully Changed Financial TransactionsNote If the period specified included a non-working day, a message displays indicating that. |  |
| 4 | Production Run | Choose Exit.Make the following entries and choose Execute:Test Run: <deselect> | The Change Counterparty of a Financial Transaction view displays with List of Successfully Changed Financial Transactions. |  |

#### Display Financial Transactions with Changed Counterparty

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display the list of financial transactions for the changed counterparty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Transactions - Changed Counterparty (TRTM_CHG_PARTNER_DIS). | The Display Financial Transactions With Changed Counterparty screen is displayed. |  |
| 3 | Enter Selection Criteria | Make the following entries and choose Execute:Company Code: 3310 | The Display Financial Transactions With Changed Counterparty view displays a list of financial transactions with changed partner. |  |

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

Prerequisite

You have created a securities option transaction.

NPV values need to be stored in advance of the valuation of treasury positions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Simulate Period-End Closing (TPM_SIM_VAL). | The Simulate Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Simulate Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example, 76JTransaction Number: for example, <the transaction number of the securities option you created in the previous step>Recalculate Outdated Sim.Val.: <deselect this checkbox>Note If you set this indicator, you can recalculate the outdated simulation resultsSimulation Date: for example, <the current date>Key Date Valuation: <select this checkbox>Accrual/Deferral: <deselect this checkbox>Test Run: <select this checkbox> | The following message is displayed:Processed xx positions; xx successful, 0 failed.If Recalculate Outdated Simulation Results has been executed, the following message is displayed:xx simulated results deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
| 4 | Execute Simulated Valuation | The dialog Message shows up, and choose Continue. | The screen Simulate Period-End Closing is displayed.You can check the simulated valuation information for local GAAP (valuation area AE0). Please note there is no simulated valuation created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back to the initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The dialog Messages screen is displayed. |  |
| 6 | Execute Simulated Valuation for Production Run | The dialog Message shows up, and choose Continue. | The screen Simulate Period-End Closing is displayed.You can check the simulated valuation information for local GAAP (valuation area AE0). |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Delete Results of Simulated Period-End Closing (TPM_SIM_VAL_DEL). | The Delete Results of Simulated Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Delete Results of Simulated Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example, AE0Product Type: for example, 76JTransaction Number: for example, <the transaction number of the securities option you created in the previous step>Simulation Date: for example, <the date on which the reversal should take place>Test Run: <select this checkbox> | The following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |
| 4 | Enter Selection Criteria for Production Run | Go back to the initial screen of this app.On the Delete Results of Simulated Period-End Closing screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |

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
> Flagged while digesting this document, not verified: Post Derived Business Transactions production run expected result mentions posting information for valuation area US0 while creating the accounting document in AE0 (all other steps use AE0 only).

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/securities-option-management-group-ledger-us-gaap-6nf-ae-test-script-1]]
- related-to :: [[05-treasury-and-cash-management/test-script-securities-option-management-group-ledger-ifrs-6ne-ae-1182]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6ND_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 186,246 chars in the whole document
