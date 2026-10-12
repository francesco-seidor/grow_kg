---
id: 05-treasury-and-cash-management/test-script-asset-backed-securities-management-6b5-ae-sap-s-4hana-clou
title: "Test Script: Asset-Backed Securities Management (6B5_AE) - SAP S/4HANA Cloud Public Edition (6B5_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 6B5 (AE localization): ABS/MBS purchase, payment, valuation, repayment, sale, reports, plus appendix jobs, output and risk setup."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/asset-backed-securities]
aliases: [6B5_S4CLD2608_BPD_EN_AE]
keywords: [Asset-Backed Securities Management, asset-backed securities, business partner creation, securities accounts, security class, securities purchase, payment requests, general ledger posting, key date valuation, installment repayment]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6B5_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1158
topic: 05-treasury-and-cash-management/asset-backed-securities
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Asset-Backed Securities Management (6B5_AE) - SAP S/4HANA Cloud Public Edition (6B5_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6B5_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Asset-Backed Securities Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Asset-Backed Securities Management (6B5_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232858260)

[2 Prerequisite 6](#_Toc232858261)

[2.1 System Access 6](#_Toc232858262)

[2.2 Roles 6](#_Toc232858263)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232858264)

[2.4 Business Conditions 8](#_Toc232858265)

[3 Preliminary Steps 9](#_Toc232858266)

[3.1 Create Business Partner 9](#_Toc232858267)

[3.1.1 Create Business Partner - Counterpart/Depository Bank 9](#_Toc232858268)

[3.1.1.1 Maintain General Data for Business Partner 9](#_Toc232858269)

[3.1.1.2 Maintain Payment Details for Business Partner 11](#_Toc232858270)

[3.1.1.3 Maintain Authorizations for Business Partner 14](#_Toc232858271)

[3.1.1.4 Maintain Reporting Data in Company Code for Business Partner 15](#_Toc232858272)

[3.1.1.5 Maintain Additional Business Partner Roles 16](#_Toc232858273)

[3.1.2 Create Business Partner - ABS Issuer 17](#_Toc232858274)

[3.1.2.1 Maintain General Data for Business Partner 17](#_Toc232858275)

[3.1.2.2 Maintain Reporting Data in Company Code for Business Partner 19](#_Toc232858276)

[3.2 Maintaining Credit Limit 20](#_Toc232858277)

[3.2.1 Maintain Limit with Limit Type Y01 20](#_Toc232858278)

[3.2.2 Maintain Limit with Limit Type Y07 21](#_Toc232858279)

[3.3 Maintain Trader and Trader Authorizations 23](#_Toc232858280)

[3.3.1 Define Traders 23](#_Toc232858281)

[3.3.2 Define User Data 23](#_Toc232858282)

[3.3.3 Maintain Trader Authorizations 24](#_Toc232858283)

[4 Overview Table 26](#_Toc232858284)

[5 Test Procedures 29](#_Toc232858285)

[5.1 Open Security Account 29](#_Toc232858286)

[5.1.1 Create Security Account for Investment 29](#_Toc232858287)

[5.2 Create Security Class 30](#_Toc232858288)

[5.2.1 Create Security Class for Invested AMS/MBS 31](#_Toc232858289)

[5.3 Analyze Cash Position 33](#_Toc232858290)

[5.4 Analyze Liquidity Forecast 34](#_Toc232858291)

[5.5 Purchase ABS/MBS 34](#_Toc232858292)

[5.5.1 Import Securities Price 34](#_Toc232858293)

[5.5.2 Check Limit Utilization Report 34](#_Toc232858294)

[5.5.3 Create ABS/MBS Purchase Order 35](#_Toc232858295)

[5.5.4 Execute ABS/MBS Purchase Order 37](#_Toc232858296)

[5.5.5 Waiver ABS/MBS Purchase Order 39](#_Toc232858297)

[5.5.6 Create ABS/MBS Purchase Transaction 40](#_Toc232858298)

[5.5.7 Set Settlement Status (Manually) 41](#_Toc232858299)

[5.6 Corporate Initiated Payment 42](#_Toc232858300)

[5.6.1 Option 1: Generate and Automatically Process Payment Request 43](#_Toc232858301)

[5.6.1.1 Process the Payment with the ‘Auto. Payment Run’ Function 43](#_Toc232858302)

[5.6.2 Option 2: Generate and Process Payment Request 46](#_Toc232858303)

[5.6.2.1 Generate Payment Request 46](#_Toc232858304)

[5.6.2.2 Process Payment Request 49](#_Toc232858305)

[5.6.3 Send Payment Medium File 51](#_Toc232858306)

[5.7 Bank Initiated Payment 51](#_Toc232858307)

[5.8 Post to General Ledger 52](#_Toc232858308)

[5.9 Period-end Closing 54](#_Toc232858309)

[5.9.1 Import Securities Price 54](#_Toc232858310)

[5.9.2 Perform Key Date Valuation 54](#_Toc232858311)

[5.10 Installment Repayment 57](#_Toc232858312)

[5.10.1 Create/Adjust Redemption Schedule Version 57](#_Toc232858313)

[5.10.2 Post Installment Repayment 58](#_Toc232858314)

[5.10.3 Post Incoming Interest Payment 60](#_Toc232858315)

[5.11 Sell ABS/MBS before Maturity 62](#_Toc232858316)

[5.11.1 Create ABS/MBS Sale Transaction 62](#_Toc232858317)

[5.11.2 Set Settlement Status 64](#_Toc232858318)

[5.11.3 Bank Initiated Payment 65](#_Toc232858319)

[5.11.4 Post to General Ledger 65](#_Toc232858320)

[5.12 Reports 68](#_Toc232858321)

[5.12.1 Define Financial Positions 68](#_Toc232858322)

[5.12.2 Financial Status (Book Value) 69](#_Toc232858323)

[5.12.3 Financial Status (Nominal Amount) 70](#_Toc232858324)

[5.12.4 Display Treasury Alerts - Posting 71](#_Toc232858325)

[5.12.5 Display Treasury Alerts- Settlement, Release and Payment 72](#_Toc232858326)

[5.12.6 Display Treasury Posting Journal 73](#_Toc232858327)

[5.12.7 Display Treasury Position Flows 74](#_Toc232858328)

[5.12.8 Display Treasury Position Values 75](#_Toc232858329)

[5.12.9 Treasury Position Analysis 76](#_Toc232858330)

[5.12.10 Display Securities Account Class Positions 76](#_Toc232858331)

[5.12.11 Analyze NPV 77](#_Toc232858332)

[5.12.12 Calculate Market Risk Key Figures 78](#_Toc232858333)

[6 Appendix 80](#_Toc232858334)

[6.1 Reclassification 80](#_Toc232858335)

[6.1.1 Perform Valuation Class Transfer 80](#_Toc232858336)

[6.2 Position Indicator 81](#_Toc232858337)

[6.2.1 Change Position Indicator 81](#_Toc232858338)

[6.3 Job Scheduling 82](#_Toc232858339)

[6.3.1 Generate Limit Utilizations 82](#_Toc232858340)

[6.3.2 Generate Payment Request 84](#_Toc232858341)

[6.3.3 Post Flows to General Ledger 86](#_Toc232858342)

[6.3.3.1 Template - Fix, Pay and Post Flows 86](#_Toc232858343)

[6.3.3.2 Template - Process Business Transactions 88](#_Toc232858344)

[6.3.4 Key Date Valuation 90](#_Toc232858345)

[6.3.5 Update Security Cash Flow 92](#_Toc232858346)

[6.3.6 Post Debit Position 93](#_Toc232858347)

[6.3.7 Calculate Market Risk Key Figures 95](#_Toc232858348)

[6.4 Output Management 97](#_Toc232858349)

[6.4.1 Output Parameter Determination 97](#_Toc232858350)

[6.4.2 Manage Output Items 100](#_Toc232858351)

[6.4.3 Maintain Print Queues 101](#_Toc232858352)

[6.4.4 Display Email Transmissions 102](#_Toc232858353)

[6.4.5 Maintain Email Template 103](#_Toc232858354)

[6.4.6 Maintain Form Template 105](#_Toc232858355)

[6.5 Reconciliation of External Securities Account Statements 106](#_Toc232858356)

[6.5.1 Create the Statements of External Securities Account 106](#_Toc232858357)

[6.5.2 Reconciliation of External Securities Account Statements 108](#_Toc232858358)

[6.6 Accounting 109](#_Toc232858359)

[6.6.1 Reverse Valuation 109](#_Toc232858360)

[6.6.2 Reverse Debit Position 110](#_Toc232858361)

[6.7 Market Risk Analyzer 112](#_Toc232858362)

[6.7.1 Manage Market Data Shift 112](#_Toc232858363)

[6.7.2 Maintain Scenarios 113](#_Toc232858364)

[6.7.3 Defining Report Layout for Calculate Market Risk Key Figures 114](#_Toc232858365)

[6.7.4 Manage Market Risk Key Figure Sets 117](#_Toc232858366)

[6.8 Credit Risk Analyzer 120](#_Toc232858367)

[6.8.1 Display Limit Overview 120](#_Toc232858368)

[6.9 Simulated Valuation 121](#_Toc232858369)

[6.9.1 Run Simulated Valuation 121](#_Toc232858370)

[6.9.2 Delete Simulated Valuation 123](#_Toc232858371)

[6.10 Security Account Transfer 124](#_Toc232858372)

[6.10.1 Security Account Transfer 124](#_Toc232858373)

## Purpose

Overview

The scope item helps you to manage asset-backed securities investments. The functionality helps you to automate labor-intensive processes, such as payment handling and accounting postings, giving you more time to focus on value-added activities. You can manage operational and accounting requirements.

The current scope covers the asset-backed securities (ABS), such as mortgage-backed securities (MBS), collateralized debt obligation (CDO) and nonmortgage ABS.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisite

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/viewer/b249d650b15e4b3d9fc2077ee921abd0/latest/en-US/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version. |

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

## Preliminary Steps

### Create Business Partner

#### Create Business Partner - Counterpart/Depository Bank

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner screen, choose Organization. | The Create Organization screen is displayed. |  |
| 4 | Enter Address Data | On the Create Organization screen, enter the following data, and choose Save:Business Partner: for example, 33537001Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Bank 1 - SAMPLE BANKSalutation: for example, Bank 1Search Term 1/2: for example, Bank 1Street/House number: for example,Postal Code/City: for example,Ctry/Reg.: AELanguage: ENE-Mail: <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, <Dec 31 of the year 9999>Note Remain on this view for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to Change Mode | On the Display Organization33537001 details screen, choose Switch Between Display and Change, and enter the following data:Change in BP role: select TR0151 Counterparty | More counterparty related tabs, for example Legal Data, Rating display. |  |
| 6 | Enter Legal Data | On the Change Organization:33537001, new role Counterparty screen, from the Navigation Menu, choose Legal Data from the dropdown list and enter the following data:Country/Region: AEand choose Save.Note The navigation menu is on the right side of the view. It displays as … , and is next to the >),Note Remain in this view for subsequent steps. | The legal data is entered and saved.Change Organization: 33537001, new role Counterparty view is displayed. |  |
| 7 | Enter Payment Transaction Data | On Change Organization:33537001, new role Counterparty screen, from the Navigation Menu, select Payment Transactions from the dropdown list and enter the following two rows of data:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, <bank key>Bank acct: for example, <bank account>IBAN: choose the IBAN button and choose Continue in the IBAN dialog box.Row 2:ID: for example, USD1C/R: for example, AEBank Key: for example, <bank key>Bank acct: for example, <bank account>IBAN: choose the IBAN button and then choose Continue on the IBAN dialog box.Choose Save.Note If a dialog window of Information appears when you choose IBAN, choose Continue. | The Payment transaction data is entered and the Business Partner is saved. |  |

##### Maintain Payment Details for Business Partner

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
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter the following data:Business Partner: 33537001Choose Enter. Choose Switch Between Display and Change, and enter the following data:Change in BP Role: select TR0151 Counterpartyand choose Enter. | Change Organization: 33537001 , role Counterparty screen is displayed. |  |
| 4 | Enter SI: Payment Details Data | On Change Organization:33537001, role Counterparty, choose Company Code, and enter the following data:Company Code: for example, 3310Choose ENTER and choose SI: Payment Details and enter the following four rows of data:Row 1:Currency: for example, AEDPay.Det.ID: for example, AEDIHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, <leave blank>Partner Bank: for example, BlankPayment Request: for example, <deselect>Payment Methods: for example, BlankRow 2:Currency: for example, AEDPay.Det.ID: for example, AEDOHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, 33537001Partner Bank: for example, AED1Payment Request: for example, <select>Payment Methods: for example, TRow 3:Currency: for example, USDPay.Det.ID: for example, USDIHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/ee: for example, BlankPayment Request: for example, <deselect>Payment Methods: for example, <leave blank>Row 4:Currency: for example, USDPay.Det.ID: for example, USDOHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/Payee: for example, 33537001Partner Bank: for example, USD1Payment Request: for example, <select>Payment Methods: for example, FNote Remain in the view for subsequent steps.Note If a warning notification displays the following message: Business partner proposed as payer/payee (see long text). Display this message for this business partner again? choose No. | The SI: Payment Details data is entered. |  |
| 5 | Assign Payment Details | From the last view of previous step,For AED,select the checkbox for AEDAEDI. Choose Assign, in the Counterparty Change: Payment Details Assignment dialog box, and choose Select All Incoming.Now AEDI displays under PmntID-Inc. .Choose Continue to close the dialog box.Select the checkbox for AEDAEDO.Choose Assign, in the Counterparty Change: Payment Details Assignment dialog box and choose Select All Outgoing.Now AEDO displays under P-ID Outg.Choose Continue to close the dialog box.Repeat for USD:USD I: PmntID-IncUSD O: P-ID Outg.On the Change Organization:33537001, role Counterparty screen, choose Save. | Payment details and the assignments are saved. |  |

##### Maintain Authorizations for Business Partner

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
| 4 | Enter SI: Authorizations Data | On the Change Organization: 33537001, role Counterparty screen, choose Company Code, choose SI: Authorizations, enter the following data and choose Save.Securities: select the Auth. checkboxNote You can also give authorization to a specific product type and transaction type by expanding the folders. For testing purpose, we give all authorizations to all kinds of product types and transaction types. | The Authorizations data is saved. |  |

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
| 1 | Log On | Log onto the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter the following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter the following data:Change in BP Role: choose TR0151 Counteparty | Change Organization: 33537001 , role Counterparty screen is displayed. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization: 33537001, role Counterparty screen, choose Company Code, choose Reporting Data in Company Code, and enter the following data and choose save.Comp. Rel.: for example, 3 OtherNote If you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown list.Note Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itThey are used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

##### Maintain Additional Business Partner Roles

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

#### Create Business Partner - ABS Issuer

##### Maintain General Data for Business Partner

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
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner screen, choose Organization. | The Create Organization screen is displayed. |  |
| 4 | Enter Address Data | On the Create Organization screen, enter the following entries and choose Save:Business Partner: for example, 33537003Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Bank 2 - SAMPLE BANKSalutation: for example, Bank 2Search Term 1/2: for example, Bank 2Street/House number: for example,Postal Code/City: for example,Country: AELanguage: ENE-Mail: for example, <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, Dec 31 of the year 9999Note Remain on this view for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to Change Mode | On the Display Organization33537003 screen, choose Switch Between Display and Change, and enter the following data:Change in BP role: select TR0150 Issuer | More counterparty related tabs such as Legal Data, Rating show up. |  |
| 6 | Enter Legal Data | On the Change Organization:33537003 screen, choose Legal Data in the dropdown list of Navigation Menu, enter the following data and choose Save:Country: AENote The navigation menu is on the right side of the view. It displays as … , and is next to the >),Note Remain in this view for subsequent steps. | The Legal data is entered and saved.The Change Organization:33537003, role Counterparty screen is displayed. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Maintain Business Partner (BP). | The Maintain Business Partner(BP): screen is displayed. |  |
| 3 | Switch to Change Mode | On the Maintain Business Partner: screen, choose Open BP, in the popup dialog box, enter the following data:Business Partner: 33537003Choose Enter and then choose Switch Between Display and Change, and enter the following data:Change in BP Role: choose TR0150 Issuer(defined) | Change Organization: 33537003 , role Issuer screen is displayed. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization:33537003, role Counterparty screen, choose Company Code3310, choose Reporting Data in Company Code, and enter the following data and choose Save.Comp. Rel.: for example, 3 OtherIf you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown list.Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 unaffiliated4 Do not use itIt can be used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

### Maintaining Credit Limit

Purpose

A series of limit types have been created in system. You can maintain credit limit based on specific limit type according to business. In the following steps, you are going to maintain limit type Y01 and Y07.

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
| 2 | Access the SAP Fiori App | Open Manage Limits (TBL1). |  |  |
| 3 | Choose Limit Type | Select the Limit Type Y01 row and choose Create Limits. |  |  |
| 4 | Company Code | Enter the following entry and choose Continue:Company Code: for example, 3310 | The Edit Limits for Limit Type Y01: Create New Limit screen is displayed. |  |
| 5 | Create Internal Limit Amount and External Limit Amount | Enter the following data and choose Save:Valid From Date: for example, <the current date>Valid To (Internal): for example, 12/31/9999Valid To (External): for example, <the current date + 1 year>Limit Currency: for example, AEDInternal Limit Amnt: for example, 250,000,000External Limit Amnt: for example, 200,000,000Critical Limit Utilizat.: for example, 90%Max. Risk Commit Per. Mth: for example, 999Note The maximum period is set on monthly basis. A warning message is displayed if the period is exceeded.Limit: for example, Check |  |  |

#### Maintain Limit with Limit Type Y07

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
| 4 | Edit Limits | Make the following entries, and choose Continue:Company Code: for example, 3310BusPartner: for example,33537001 | The Edit Limits for Limit Type Y07: Create New Limit screen is displayed. |  |
| 5 | Create Internal Limit Amount and External Limit Amount | Enter the following data, and choose Save:Valid From Date: for example, <the current date>Valid To (Internal): for example, 12/31/9999Valid To (External): for example, <the current date + 1 year>Limit Currency: for example, AEDInternal Limit Amnt: for example, 250,000,000External Limit Amnt: for example, 200,000,000Critical Limit Utilizat.: for example, 90%Max. Risk Commit Per. Mth: for example, 999Limit: for example, Check |  |  |

### Maintain Trader and Trader Authorizations

#### Define Traders

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

#### Define User Data

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define User Data (S_ALR_87007933). | The Change View "Treasury: User master data supplements": Overview screen is displayed. |  |
| 3 | Create a New Record | Select New Entries, enter data and select Save.User name: for example: <Your user name>Trader: for example: TRADER02 | The data is saved. |  |

#### Maintain Trader Authorizations

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

A trader must be defined before this step. Refer to [Define Traders](#unique_17) [page ] 23 step for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Trader Authorizations (TBT1). | The Create/Change Trans. Authorization for Trader: Init. Screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter data and select Enter.Trader: for example: TRADER02Company Code: for example: 3310 | The Create/Change Transaction Authorization for Traders screen is displayed. |  |
| 4 | Enter Authorization and Save | Select or unselect on the Authorization column and select Save.Note Make sure to authorize TRADER02 for the Money Market transactions. | The data is saved as indicated by a message. For example: Transaction authorizations for trader TRADER02 are being saved. |  |

## Overview Table

The scope item consists of several process steps, reports, items provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Create Security Account for Investment](#unique_21) [page ] 29 | Treasury Specialist - Back Office | Manage Securities Accounts (TRS_SEC_ACC) | A security account for investment is created. |
| [Create Security Class for Invested AMS/MBS](#unique_22) [page ] 31 | Treasury Specialist - Back Office | Manage Securities Classes (FWZZ) | Security class for invested AMS/MBS is created. |
| [Analyze Cash Position](#unique_23) [page ] 33 | Cash Manager | Cash Flow Analyzer (F2332) | Cash manager check the cash position status, and make decisions of right financial instruments for short-term purpose based on analysis of cash position. |
| [Analyze Liquidity Forecast](#unique_24) [page ] 34 | Cash Manager | Cash Flow Analyzer (F2332) | The cash manager check the liquidity forecast regularly and make decisions regarding medium-term or long-term financial instruments. |
| [Import Securities Price](#unique_25) [page ] 34 | Treasury Specialist - Back Office | Enter Securities Prices (FW17) | New security price is maintained. |
| [Check Limit Utilization Report](#unique_26) [page ] 34 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | Limit utilization report displays. |
| [Create ABS/MBS Purchase Transaction](#unique_27) [page ] 40 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | ABS/MBS purchase ransaction is created. |
| [Set Settlement Status (Manually)](#unique_28) [page ] 41 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The transaction is settled manually. |
| [Process the Payment with the ‘Auto. Payment Run’ Function](#unique_29) [page ] 43 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_30) [page ] 46 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_31) [page ] 49 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Post to General Ledger](#unique_32) [page ] 52 | Treasury Accountant | Fix, Pay and Post Flows (TBB1); Process Business Transactions (TPM10) | Cash flows related FI document is posted. |
| [Import Securities Price](#unique_33) [page ] 54 | Treasury Specialist - Back Office | Enter Securities Prices (FW17) | New security price is maintained. |
| [Perform Key Date Valuation](#unique_34) [page ] 54 | Treasury Accountant | Run Valuation (TPM1) | The screen Valuation Log displays, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. The accounting document has been created in local GAAP (valuation area AE0). |
| [Create/Adjust Redemption Schedule Version](#unique_35) [page ] 57 | Treasury Specialist - Back Office | Manage Securities Classes (FWZZ) | Redemption schedule version is created/adjusted. |
| [Post Installment Repayment](#unique_36) [page ] 58 | Treasury Accountant | Execute Debit Position - Manual Debit Position (FWZE) | Installment repayment is posted. |
| [Post Incoming Interest Payment](#unique_37) [page ] 60 | Treasury Accountant | Execute Debit Position - Manual Debit Position (FWZE) | Incoming interest payment is posted. |
| [Create ABS/MBS Sale Transaction](#unique_38) [page ] 62 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | ABS/MBS sale transaction is created. |
| [Set Settlement Status](#unique_39) [page ] 64 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The transaction is settled manually. |
| [Bank Initiated Payment](#unique_40) [page ] 65 | N/A | N/A | This step is outside of SAP system |
| [Post to General Ledger](#unique_41) [page ] 65 | Treasury Accountant | Process Business Transactions (TPM10); | Cash flows related FI document is posted. |
| [Define Financial Positions](#unique_42) [page ] 68 | Treasury Accountant | Define Financial Positions (FTR_FP_DEF) | Financial Positions are defined. |
| [Financial Status (Book Value)](#unique_43) [page ] 69 | Treasury Accountant | Financial Status (F2136) | The financial status on book values displays. |
| [Financial Status (Nominal Amount)](#unique_44) [page ] 70 | Treasury Accountant | Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)) | The financial status on nominal amount displays. |
| [Display Treasury Alerts - Posting](#unique_45) [page ] 71 | Treasury Accountant | Display Treasury Alerts (F4984) | Treasury Alerts-Posting display. |
| [Display Treasury Alerts- Settlement, Release and Payment](#unique_46) [page ] 72 | Treasury Specialist - Back Office | Display Treasury Alerts - Settlement (F4979) | Treasury Alerts display. |
| [Display Treasury Posting Journal](#unique_47) [page ] 73 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Treasury posting journal displays. |
| [Display Treasury Position Flows](#unique_48) [page ] 74 | Treasury Specialist - Back Office | Display Treasury Position Flows (F1754) | Treasury posting flows display. |
| [Display Treasury Position Values](#unique_49) [page ] 75 | Treasury Accountant | Display Treasury Position Values (F1867) | Treasury position values display. |
| [Treasury Position Analysis](#unique_50) [page ] 76 | Treasury Accountant | Treasury Position Analysis | Treasury position analysis displays. |
| [Display Securities Account Class Positions](#unique_51) [page ] 76 | Treasury Accountant | Display Securities Account Class Positions (TPM40A) | Display Securities Account Class Positions display |
| [Analyze NPV](#unique_52) [page ] 77 | Treasury Specialist - Front Office | Analyze NPV (JBRX) | The NPV Result displays. |
| [Calculate Market Risk Key Figures](#unique_53) [page ] 78 | Treasury Specialist - Middle Office | Calculate Market Risk Key Figures (AISGENKF) | The single value analysis of assigned report layout displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Open Security Account

#### Create Security Account for Investment

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
| 3 | Enter Account Identifier | Enter a new unique identifier for the new Securities Account, and choose Create.Company Code: for example, 3310Securities Acct: for example, SEC_INVInfoChoose Create if a confirmation dialog pops up.If above account is already created, you can choose Display or Change to either view or edit the account. | A new account is created. |  |
| 4 | Enter General Data of the Account | Enter the following data and move to the next tab:Securities Account ID: for example, ABS33537001AE0Securities Account Type: for example, SAC Asset Securities Account | Move to the next tab. |  |
| 5 | Enter Bank Data | Enter the following data and choose Save:Depository Bank: for example, 33537001External Securities Account ID: for example, 123XXXX567Line 1:Payment Currency: AEDHouse Bank: AEBK1Account ID: AEAC1Line 2:Payment Currency: USDHouse Bank: AEBK1Account ID: USDAC | The data is saved. |  |

### Create Security Class

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The user needs to create a security class ID before creating any transaction on a security. This section introduces how to create a mortgage-backed security (MBS) class with fixed interest rate and maintain the corresponding redemption schedule.

The asset-backed security with floating interest rate can also be processed, you can refer to the Create Security Class for Invested Floating-Rate Bond and Interest Rate Fixing Date steps in 3WY - Bond Management test script.

#### Create Security Class for Invested AMS/MBS

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Securities Classes (FWZZ). | The Display Class screen is displayed. |  |
| 3 | Enter ID Number | Enter an ID Number for the New Class, and choose Create.ID Number: for example, MBS_AE1A dialog of Create Class pops up, enter the following data and choose Create:Prod. Type: 04M Asset-Backed SecuritiesShrt: for example, MBS Fixed-Rate1 | The Create Class screen displays with previously specified ID Number. |  |
| 4 | Enter Search Terms | On the Create Class - Product Type: ABS/MBS - ID Number:MBS_AE1 screen, enter the following data:Gen. Sec. Classification: for example, 06 Asset-Backed SecuritiesBond Classification: 915 Mortgage-Backed SecuritiesSecondary Indices: for example, CUSIP: XXXXQK3G1Please switch to the Basic Data tab, after entering Search Terms. | Basic Data tab is displayed. |  |
| 5 | Enter Basic Data | Switch to the Basic Data tab, and enter the following data:Tranche Classification: for example,001 Senior TrancheIssuer: for example, 33537003Issue Currency: for example, AEDIssue Start: for example,<the first day of current month – 3 months>Compatible End of Term for example, <The issue day + 5 years>Orig.Nominal for example, 109,000,000.00 |  |  |
| 6 | Enter Asset Pool Data | Switch to the Asset Pool Data tab, and enter the following data:Pool ID for example, Mortgage01Pool Class for example, 001 MortgagesNominal Amount for example, 109,000,000.00 |  |  |
| 7 | Switch to Conditions | Switch to the Conditions tab, enter the following data and choose Red.Schedules:Interest Calculation Method: for example, 360/360Eff.Int.Meth.: for example, ICMAChoose Yes if Document dialog box displays: Do you want to save the data first? |  |  |
| 8 | Enter the Details of Schedule - Redemption Schedule | The editable version 0 of security ID MBS_AE1 is generated by default. Select the version 0 in left-down box Version Overview.Then choose the Schedule tab, and enter the following data:Entry Type: for example, F Enter FactorRedemption Template: for example, 100 Int(perc.-quoted) |  |  |
| 9 | Enter Details of Conditions - Redemption Schedule | Switch to Conditions tab on the right side, choose Add Condition, and select condition 100 Int. (perc.-quoted) in the dialog box.In the record of Int. (perc.-quoted), enter the following entries:Entry eff. From: for example, <the first day of current month – 3 months>Percentage Rate: 3.0000000Double click to enter the following data on the Dates tab, and then go back.Calendar 1: 01In the Calculation Date area:The first line of the fields: for example, < 0 regular: 1 Months>1st Date: for example, <the first day of current month – 3 months>Month-End: <deselect this indicator>Inclusive: <deselect this indicator>In the Due Date area:1st Date: for example, <Date 25th in current month – 3 months>Month-End: <deselect this indicator> |  |  |
| 10 | Enter Details of Calculation Parameters – Redemption Schedule | Switch to the Calculation Parameters tab on the right side, enter the following data:Prepayment Calc. Method: for example, CPR MethodPrepayment Speed Interval: 1 MonthlyWAC Original: for example, 3.96Net Original: for example, 3.0WAM Original: for example, 60WAC: for example, 3.94Net Interest: for example, 3.0Age of the MBS: for example, 3WAM: for example, 57CPR 1 M.: for example, 35.2CPR Life: for example, 11.2Note If the original parameters are blank, and the fields WAM, WAC and Net Interest are promptly assigned, then those values would be copied to original parameters during saving. |  |  |
| 11 | Activate the Redemption Schedule – Redemption Schedule | Switch to the Schedule tab, choose Generate Schedule, the Redemption Factors are calculated in the table of Redemption Schedule, then change the value of column Stat.Fac. to Published from first line to the Calculat. Date is last month.Select the version 0 in left-down box Version Overview, choose Activate in left-top box to activate the version, then choose Back to return to the upper view. | Redemption Version is activated. |  |
| 12 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Save:Exchange: OTCFlat Price: <select this indicator> | Data is saved. |  |

### Analyze Cash Position

Purpose

At the end of the transaction day, the cash manager always reviews the cash position status for making decisions about the right financial instruments for short-term purposes, based on analysis of cash position.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) SAP Fiori app to analyze the cash position. For more information, please refer to the Basic Cash Operations(BFB) test script.

### Analyze Liquidity Forecast

Purpose

The cash manager reviews the liquidity forecast regularly and makes decisions regarding medium-term or long-term financial instruments, such as, investment, loan, or foreign exchange.

Procedure

If cash management is implemented in your system, you use the Cash Flow Analyzer (F2332) app to analyze the liquidity forecast. For more information, see the Basic Cash Operations(BFB) test script.

### Purchase ABS/MBS

#### Import Securities Price

Purpose

By entering the security price into SAP system, the system can recognize its latest fair value and update the credit limit utilization when purchasing transaction or running the end-of-day processing.

Procedure

Refer to the Update Security Price - ABS/MBS Management step of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Review Limit Utilizations (TBLB). | The Overview of Utilizations - Selection Using all Characteristics screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Execute:Limit Type: for example, Y01 or Y07Limit Utilization Base: for example, 1Determination Date: for example, <the current date>Limits Valid From: for example, <the current date> | An overview of the limit utilization in accordance with your selection criteria is displayed. |  |

#### Create ABS/MBS Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you enter the ABS/MBS purchase order information into the system. The order includes amount and order data and can be converted to the contact through order execution or obsoleted through expiration.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

Please create two purchase orders via below steps.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Securities Transaction: Entry Screen screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Securities Transaction: Entry Screen, enter the following data and choose Enter:Company Code: for example, 3310ID Number: the security class you created, for example, MBS_AE1Transaction Type: 100Partner: for example, 33537001In the Activity area,Order/Fixing: <select> | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:In the Position area,Securities Account: for example, SEC_INVIn the Amounts area,Original Nominal Amount: for example, 100,000,000.00 AEDIn the Order Data area,Limit Date: for example, <two days after current date>Limit Price: for example, 100 | All data is entered. |  |
| 5 | Save the Transaction | Choose Save.Note Write down the created security transaction ID for following step. |  |  |
| 6 | Create Position Indicator | Choose Create Automatically. | The transaction is created. |  |
| 7 | Create Another Order for Expiration | Repeat step 2-7 to create another order for expiration. |  |  |

#### Execute ABS/MBS Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You decide to purchase ABS/MBS based on the created order. After the execution, you enter the purchase contract information into the system. You can skip the step [Create ABS/MBS Purchase Transaction](#unique_27) [page ] 40 as the ABS/MBS purchase transaction is generated.

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
| 3 | Enter Data on Initial Screen | In the search term area, enter the following data and choose Go:Key Date: for example, TodayCompany Code: for example, 3310Transaction: <the order transaction number> | The ABS/MBS purchase order transaction screen is displayed. |  |
| 4 | Execute the Purchase Order | In the Transaction area, select the transaction and choose Execute Order in the toolbar via button …. | The details of the ABS/MBS purchase order transaction are displayed. |  |
| 5 | Add Relevant Information and Save the Transaction | On the tab Structure, enter the following data:Securities Account: for example, SEC_INVGeneral Valuation Class: <choose an appropriate GeneralValuation Class (GVC), for example, 11 Long term investment(non-current asset):Amorizated cost>Position Value Date: for example, <Current Date – 1 Month>Calculation Date: for example, <Current Date – 1 Month>Payment Date: for example, <Current Date – 1 Month>Original Nominal Amount: for example, 100,000,000.00 AEDPrice (%): for example, 99.8Coupon: 1 Next coupon will be delivered (plus accrued interest)Contract Date: for example, <Current Date – 1 Month> |  |  |
| 6 | Create Position Indicator | Choose Save. | If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a dialog box appears asking to Create Position Indicator.If the Position Indicator is already created, then you can ignore below step. The following message is displayed: Security transaction XXXXX created in company code YYYY |  |

#### Waiver ABS/MBS Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You decide to waiver the ABS/MBS purchase order. Once you set the order to expiration, you need to maintain the relevant information in the system.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.
- The relevant ABS/MBS purchase order is created in the above steps but not executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Data on Initial Screen | In the search term area, enter the following data and choose Go:Key Date: for example, TodayCompany Code: for example, 3310Transaction: <the transaction number> | The ABS/MBS purchase order transaction screen is displayed. |  |
| 4 | Waiver the ABS/MBS Purchase Order | In the Transaction area, select the transaction and choose Order Expiry in the toolbar via button …. | The details of the ABS/MBS purchase order transaction are displayed. |  |
| 5 | Waiver the ABS/MBS Purchase Order | On the initial screen, choose Save. | The status of ABS/MBS purchase order transaction is changed to Order Expiration. |  |

#### Create ABS/MBS Purchase Transaction

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
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Securities Transaction: Entry Screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Securities Transaction: Entry Screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, MBS_AE1Transaction Type: 100Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Securities Account: for example, SEC_INVGeneral Valuation Class: <choose an appropriate GeneralValuation Class (GVC), for example, 11 Long term investment(non-current asset):Amorizated cost>Position Value Date: for example, <Current Date – 1 Month>Calculation Date: for example, <Current Date – 1 Month>Payment Date: for example, <Current Date – 1 Month>Original Nominal: for example, 100,000,000.00 AEDPrice (%): 99.8Coupon : 1 Next coupon will be delivered(plus accrued interest)Contract Date: for example, <Current Date – 1 Month> | The Create Security Transaction: Other Flows screen is displayed. |  |
| 5 | Save the Transaction | Choose Save. | If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a prompt asking to Create Position Indicator. Please follow the following steps if so.If the Position Indicator is already created, then you can ignore below step, but expect a message stating Security transaction XXXXX created in company code YYYY |  |
| 6 | Create Position Indicator | Choose Create Automatically.Note Write down transaction number for following steps. | The transaction is created. |  |

#### Set Settlement Status (Manually)

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
| 3 | Enter Selection Criteria and Execute | Enter the following data, and choose Go:Key Date: <the current date - 1 month>Company Code: for example, 3310Transaction: <transaction you created in the previous step> | The transaction is displayed. |  |
| 4 | Settle the TRM Transaction | On the Manage Financial Transactions screen, select the checkbox at the head of the transaction line and choose Settle. | You are directed to the screen for settling the transaction.Note The view title will be different according to product type of transaction. |  |
| 5 | Save the Change | On the Settle Security Contract: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If the Document lines: Display messages dialog box displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

### Corporate Initiated Payment

Purpose

This section describes how to handle the payment for securities purchase transaction which are initiated by corporate via payment requests.

There are two options to process the payment for the purchase:

1. Process the payment with the ‘Auto. Payment Run’ function.
2. Process the payment without the ‘Auto. Payment Run’ function.

Prerequisites

You have settled the contract in the previous step.

#### Option 1: Generate and Automatically Process Payment Request

##### Process the Payment with the ‘Auto. Payment Run’ Function

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

#### Option 2: Generate and Process Payment Request

##### Generate Payment Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Each financial transaction contains flows that need to be paid. When creating the transaction, the payment request can be selected as required (usually only for outgoing payment in practice). Treasury back office uses the Pay Only functionality in the Fix, Pay and Post Flows (TBB1)/Fix and Pay Flows (TBB1_PAY) app to create the payment request for outflows which require payment requests. It will not create posting in financial accounting.

In the case that the payment is initiated by the financial partner, skip the current step and the next step [Process Payment Request](#unique_31) [page ] 49, and continue with the step [Post to General Ledger](#unique_32) [page ] 52.

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

##### Process Payment Request

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
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests view, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media view, enter the following data and choose Run:Run Date: for example <current date>Identification: for example TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations(J78). |  |

#### Send Payment Medium File

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Securities: <select this checkbox>Company Code: for example 3310Transaction: <The transaction number you created in previous step>Sec. Class ID Number: <The Sec. Class ID Number you entered in previous step,for example, MBS_ AE 1>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date – 1 month>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | Screen Posting Log: Posted Transactions is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria, you can skip the current test step and continue the test step with the Process Business Transactions app. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Execute:Test Run: <unselect this checkbox> | Screen Posting Log: Posted Transactions is displayed, and the accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access Another SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <unselect this checkbox>Company code: for example, 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>ID Number: <the Security ID you created in previous step,for example, MBS_ AE 1>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If message You have not selected any business transactions is displayed, that means there is no posting needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Test Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Transactions screen is displayed, you can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 9 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Update Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Transactions screen is displayed, and the accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |  |

### Period-end Closing

This section describes activities for period-end closing (usually executed at month end), including:

- [Import Securities Price](#unique_33) [page ] 54
- [Perform Key Date Valuation](#unique_34) [page ] 54

#### Import Securities Price

Purpose

By entering the latest price of ABS/MBS into SAP system as securities price, the system can recognize its latest position value and perform the relevant journal posting when running key date valuation.

Procedure

Refer to the Update Security Price - ABS/MBS Management step of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

|  |
| --- |
| Note Regarding the test purpose, please maintain the price of security in the end of last month for period valuation. |

#### Perform Key Date Valuation

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
| Note You can also schedule background job for this step. Please see corresponding step in the Appendix section. |

Prerequisite

You have entered latest security price for the security ID in section [Import Securities Price](#unique_33) [page ] 54.

You have performed following sections of this test script for ABS/MBS 04M:

- [Set Settlement Status (Manually)](#unique_28) [page ] 41
- [Corporate Initiated Payment](#unique_60) [page ] 42
- [Bank Initiated Payment](#unique_62) [page ] 51
- [Post to General Ledger](#unique_32) [page ] 52

If the installment repayment and incoming interest payment are scheduled before the key date, they need to be processed first. Otherwise, an error message Scheduled bus. trans. with posting date before key date might be reported. During valuation. you can refer to the following steps of this test script:

- [Create/Adjust Redemption Schedule Version](#unique_35) [page ] 57
- [Post Installment Repayment](#unique_36) [page ] 58
- [Post Incoming Interest Payment](#unique_37) [page ] 60

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Run Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run Valuation screen, enter the following data and choose Execute:In the Product Groups area,Securities: <select this checkbox>In the General Selections area,OTC Transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example, 04MSec. Class ID Number: for example, < Security Class ID Number(s) created in previous steps>, for example, MBS_AE1Security Account: for example, SEC_INVIn the Valuation Parameters area,Key Date for Valuation: for example, <the last day of last month>Valuation Category: for example, Mid-year Valuation with ResetWhen the Period End is also the Year End, the Valuation Category Year End Valuation should be used.Test Run: <select this checkbox>Amortization Log: <select this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Please note there is no posting created because it is test run.Note Sometime there is no simulated posting because your selected security class position in security account may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the Run Valuation screen is displayed.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation. | The Valuation Log screen is displayed, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Then, the accounting document has been created in local GAAP (valuation area AE0). |  |

### Installment Repayment

Purpose

The following steps in this section describes activities for the installment repayment and incoming interest payment of inversted ABS/MBS:

- [Create/Adjust Redemption Schedule Version](#unique_35) [page ] 57
- [Post Installment Repayment](#unique_36) [page ] 58
- [Post Incoming Interest Payment](#unique_37) [page ] 60

#### Create/Adjust Redemption Schedule Version

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can create a new version for the redemption schedule based with updated ABS/MBS information, the detail of installment repayment is based on the created version.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Securities Classes (FWZZ). | The Display Class screen is displayed. |  |
| 3 | Enter ID Number | Enter an ID Number, then , and choose Change.Securities Class: for example, MBS_AE1 | The Change Class screen displays with previously specified ID Number. |  |
| 4 | Switch to Conditions | Switch to Conditions tab. Then choose Red.Schedules. | The Edit detail screen displays with previously specified ID Number. |  |
| 5 | Enter the Details of Schedule - Redemption Schedule | Choose Create in left-top box Version.Then choose the Schedule tab on the right side, enter the following data on column Redemption Factor for the line Calculat. Date is <Current month>, then change the value of column Stat.Fac. to Published.Redemption Factor: for example, 0.650104033Choose Generate Schedule to regenerate the redemption schedule.Note Usually, the value of redemption factor is less than previous month and greater than next month. It’s allowed that input value is out of interval, leading to negative installment repayment. | Basic Data tab is displayed. |  |
| 6 | Enter Details of Calculation Parameters – Redemption Schedule | Switch to Calculation Parameters tab on the right side, update the following data:Age of the MBS: for example, 4WAM: for example, 56 |  |  |
| 7 | Activate the Redemption Schedule – Redemption Schedule | Switch to the Schedule tab, select the new created version in left-down box Version Overview, choose Save, and then choose the Activate left-top box to activate the version. | The following message occurs: Update was completed successfully |  |

#### Post Installment Repayment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can process installment repayment.

|  |
| --- |
| Note You can also schedule a background job for Automatic Debit Position. For more information, see the corresponding step in the Appendix. |

Procedure

Table 2: Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Debit Position - Manual Debit Position (FWZE) | The Manual Debit Position: Initial screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, MBS_AE1Security Account: for example, SEC_INV | A list of positions is displayed. |  |
| 4 | Select a Flow and Proceed | On the list of positions that displayed on the Manual Debit Position: Initial Screen, select the top flow with update type SAM1111 that you would like to capitalize and choose Post business transaction: | Manual Debit Position screen is displayed. |  |
| 5 | Enter Details for the Installment Payment | On the Manual Debit Position screen, double click on the record should be received:The Incoming Payments:Process Flow dialog box is displayed.Verify below data and choose Copy:Payment Amount: for example, <the total amount of the install repayment to be received>. | Flow has been processed in the Flows tab. |  |
| 6 | Post | Confirm the data and choose Post. | Screen with Posting Log displays. The install repayment has been generated. |  |
| 7 | Repeat | Repeat the above step 4 to 6 with update type SAM6111 to post incoming payments for installment Repayment. | Screen withPosting Log displays. The post for incoming payment has been generated. |  |

Table 3: Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Debit Position and Posting - Security Accounts (FWSO) | The Securities: Automatic Debit Position screen is displayed. |  |
| 3 | Enter Parameters and Test Run | On the Securities: Automatic Debit Position Screen, enter the following data and choose Execute:Company Code: for example, 3310Product Type: for example, 04MSecurity ID: for example, MBS_AE11Security Account: for example, SEC_INVUpdate Type: for example, SAM1111Note Update type SAM6111 can’t be processed as automatic, you need to follow the steps in option 1 to post.Up to an Including Pos. Date: for example, <date 25th of current month>Document Date: for example, <date 25th of current month>Test Run: for example, <select> | A list of messages indicating the flow were fixed. |  |
| 4 | Production Run | Confirm the messages and go back to previous screen, enter the following data and choose ExecuteTest Run: for example, <deselect> | A list of messages indicating the flow were fixed. |  |

#### Post Incoming Interest Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can post incoming interest payment.

|  |
| --- |
| Note You can also schedule a background job for Automatic Debit Position. For more information, see the corresponding step in the Appendix |

Procedure

Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Debit Position - Manual Debit Position (FWZE) | The Manual Debit Position: Initial screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, MBS_AE1Security Account: for example, SEC_INV | A list of positions is displayed. |  |
| 4 | Select a Flow and Proceed | On the list of positions that displayed on the Manual Debit Position: Initial Screen, select the top flow with update type SAM5000 that you would like to capitalize and choose Post business transaction: | Manual Debit Position screen is displayed. |  |
| 5 | Enter Details for the Interest Payment | On the Manual Debit Position screen, double click on the record should be received:The Incoming Payments:Process Flow popup window is displayed.Verify below data and choose Copy:Payment Amount: for example, the total amount of the interest to be received. | flow has been processed in the Flows tab. |  |
| 6 | Post | Confirm the data and choose Post. | Screen with Posting Log is displayed. The incoming interest payment has been generated.Note Make a note of the key number displayed on this screen. |  |
| 7 | Repeat | Repeat the above step 4 to 6 with update type SAM6000 to post incoming payments for installment Repayment | Screen with Posting Log is displayed. |  |

Table 4: Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Debit Position and Posting - Security Accounts (FWSO) | The Securities: Automatic Debit Position screen is displayed. |  |
| 3 | Enter Parameters and Test Run | On the Securities: Automatic Debit Position Screen, enter the following data and choose Execute:Company Code: for example, 3310Product Type: for example, 04MSecurity ID: for example, MBS_AE11Security Account: for example, SEC_INVUpdate Type: firstly, enter SAM5000, then choose Multiple selection of filed Update Type. In the Multiple Selection for Update Type dialog box, add another product type SAM6000, and choose Copy(F8).Up to an Including Pos. Date: for example, <date 25th of current month>Document Date: for example, <date 25th of current month>Test Run: for example, <select> | A list of messages indicating the flow were fixed. |  |
| 4 | Production Run | Confirm the messages and go back to previous screen, enter the following data and choose ExecuteTest Run: for example, <deselect> | A list of messages indicating the flow were fixed. |  |

|  |
| --- |
| Note You can use the transaction Post General Journal Entries (F0718) as described in General Ledger Accounting (058) script to move the security proceeds to Other Financiang Soures. Use the ledger group specific posting to post this for modified accrual ledger only. |

### Sell ABS/MBS before Maturity

#### Create ABS/MBS Sale Transaction

Purpose

After sale transaction has concluded in the real world, an entry into the system is required to update the securities position.

Prerequisite

The Securities position on hand must be greater than or equal to the position to be sold.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security ID: for example, MBS_AE1Transaction Type: 200Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Securities Account: for example, SEC_INVGeneral Valuation Class: click on Display Quantity Position to figure out the GVC should be used < for example, use the same General Valuation Class as purchase transaction for this security class ID>Position Value Date: for example, <End of current month>Calculation Date: for example, <End of current month>Payment Date: for example, <End of current month>Nominal Amount: for example, 100,000,000.00 AEDPrice (%): 100Coupon : 1 Next coupon will be delivered(plus accrued interest)Please switch to the Other flows tab | The Create Security Transaction: Other Flows screen is displayed.Note Make sure that there is no condition-based business transactions posted after position value date. |  |
| 5 | Enter Data on Other flows | On the tab Other flows, add a flow row by entering the following data:Flow type: 0315 Charge not capitalizedPayment Amount: 500.00Payment Currency: AED | All data are entered. |  |
| 6 | Save the Transaction | Choose Save.Note Write down transaction number for the following steps. | The data is saved. |  |

#### Set Settlement Status

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
| 3 | Enter Selection Criteria and Execute | Enter the following data and choose Go:Key Date: <the current date>Company Code: for example, 3310Transaction: <transaction you created in the previous step> | The transaction is displayed. |  |
| 4 | Settle the TRM Transaction | On the Manage Financial Transactions screen, select the checkbox at the head of the transaction line and choose Settle. | You are directed to the screen for settling the transaction.Note The view title will be different according to product type of transaction. |  |
| 5 | Save the Change | On the Settle Security Contract: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If dialog Document lines: Display messages displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

#### Bank Initiated Payment

Purpose

If the outgoing payment is initiated by bank, it is not necessary to run the previous steps Generate Payment Request and Process Payment Request, because the outgoing payment is initiated by bank.

Procedure

This step doesn't require any operation in system.

#### Post to General Ledger

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps available for posting flows:

- Fix, Pay and Post Flows (TBB1): you use this app to generate the posting for incoming payment.
- Process Business Transactions (TPM10) You use this app to generate the posting for outgoing payment.

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Securities: <select this checkbox>Company Code: for example 3310Transaction: <The transaction number you noted down in previous step>Sec. Class ID Number: <The Sec. Class ID Number you entered in previous step,for example, MBS_ AE1Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <End date of current month>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | Screen Posting Log: Posted Business Transactions is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria, you can skip the current test step and continue the test step with the Process Business Transactions app. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Execute:Test Run: <unselect this checkbox> | Screen Posting Log: Posted Business Transactions is displayed, and the accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access Another SAP Fiori App | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <unselect this checkbox>Company Code: for example, 3310Valuation Area: for example AE0Limit by Subledger Pos.: <select this checkbox>Transaction: <The transaction number you noted down in previous step>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If message You have not selected any business transactions is displayed, that means there is no posting needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Test Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 9 | Production Run | On the screen Update Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.Screen Update Run: Display Posted/Reversed Business Transactions displays, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, and the accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |  |

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

Define a set of key figures to be displayed in Financial Status - Book Value and Financial Status - Nominal Amount screens.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define Financial Positions (FTR_FP_DEF). | The "Maintain Financial Position Groups": Change screen is displayed. |  |
| 3 | Maintain Key Figure Groups | Select New Entries.Enter data for a record of new entry and select Save.Financial Position Group: for example, FPG_ABS_A0001Financial Position Group Description: for example, ABS InvestmentAssets/Liabilities: for example, Assets | The data is saved.Note If FPG_ABS_A0001 is already created for the same purpose, you can skip this step and use the existing record. |  |
| 4 | Maintain Key Figures | Switch to Maintain Financial Positions tab.Enter data and choose Save.Financial Position: for example, FP_ABS_A1001Financial Position Description: for example, ABS InvestmentFinancial Position Group: for example, FPG_ABS_A0001Data Source: for example, Treasury position management | The data is saved. |  |
| 5 | Maintain Selections | Choose Back to display all financial postions. Select one financial position and select Maintain Selections.Product Type: for example, 04MValuation Class: for example, 10 to 14 and 20 to 24Valuation Area: for example, AE0Posting Status: for example, 2Choose Back and choose Save. | The data is saved. |  |
| 6 | Enter More Data | Enter more financial positions data as below tables. |  |  |

Below are examples for financial position groups and financial positions. You can create your own financial position gourps and financial positions per your needs.

|  |
| --- |
| Note You may create your own Financial Position Groups and Financial Positions per your request. |

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

Refer to [Define Financial Positions](#unique_42) [page ] 68 for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Financial Status (F2136). | The Financial Status - Book Value screen is displayed. |  |
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

In this step, you display the financial status of the nominal amount.

Prerequisite

Financial positions are defined.

Refer to [Define Financial Positions](#unique_42) [page ] 68 for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)). | The Financial Status - Nominal Amount screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go:Key Date: for example, <Current Date>Display Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays per the filter values. |  |

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
| 3 | Enter Selection Criteria | On the Display Treasury Alerts screen, enter the following data and choose Go:Issue Message For: PostingCompany Code: for example, 3310 | Alerts data is displayed per the filter values |  |

#### Display Treasury Alerts- Settlement, Release and Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display treasury alerts for various type of transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Alerts - Settlement (F4979). | The Display Treasury Alerts - Settlement view displays with Issue Message For: Settlement. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Alerts - Posting screen, enter the following data:Issue Message For: SettlementCompany Code: for example, 3310and choose Go. | Alerts data displays per the filter values. |  |
| 4 | Confirm Alerts for Other Transactions | Select other values in the Issue MessageFor field.ReleasePaymentCorrespondenceInterest Rates |  |  |
| 5 | Select Display Treasury Alerts Tiles with Release | Return to the Home view and open Display Treasury Alerts - Release (F4980). | The Display Treasury Alerts - Release view displays, with Issue Message For:Release. |  |
| 6 | Select Display Treasury Alerts Tiles with Payment | Return to the Home view and open Display Treasury Alerts - Payment (F4981). | The Display Treasury Alerts - Payment view displays, with Issue Message For:Payment. |  |
| 7 | Select Display Treasury Alerts Tiles with Interest Rates | Return to the Home view and open Display Treasury Alerts - Interest Rates (F4982). | The Display Treasury Alerts - Interest Rates view displays, with Issue Message For:Interest Rates. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Product Group: for example, SecuritiesCompany Code: for example, 3310 | The posting journals display per the filter values. |  |

#### Display Treasury Position Flows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you display the position flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Position Flows screen, enter the following data and choose Go:Product Group: for example: SecuritiesCompany Code: for example, 3310 | Position Flow data is displayed according to the filter values. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Position Values (F1867). | The Display Treasury Position Values screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select GoKey Date: for example, <Current Date>Product Group: for example, SecuritiesNote You may have to adapt filter to make the Product Group filter available. The Product Group is in the Position Values filter group.Company Code: for example, 3310Valuation Area: for example, AE0 | The position values data displays per the filter values. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Treasury Position Analysis. | The Treasury Position Analysis screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go. Key Date: for example, <Current Date>Include Planned Data: for example, 1Valuation Area: for example, AE0Company Code: for example, 3310Product Type: for example, 04M | The position analysis data displays per the filter values. |  |

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
| 3 | Enter Selection Criteria | On the Display Securities Account Class Position List screen, enter the following data and choose Execute:Company Code: for example, 3310Sec. Class ID Number: for example, <Security class ID number(s) for which has been created>Securities Account: for example, <Security account for which has been created>Position Value Date: for example, <Current Date> | The position is displayed. |  |

#### Analyze NPV

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you calculate and display NPV result.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Analyze NPV (JBRX). | The NPV Analysis: Display of Single Values screen is displayed. |  |
| 3 | Enter Selection Criteria of Gen. Selection | On the NPV Analysis: Display of Single Values screen, enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <current date>Horizon: for example, <end date of current month>Portfolio Hierarchy: for example, 100 |  | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |
| 4 | Enter Selection Criteria of Characteristics | Choose the Characteristics tab, enter the following data then choose Execute:Company Code: for example, 3310Product Type: for example, 04M | The NPV Result displays based on Portfolio Hierarchy. |  |

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

Report Layout for key figure should be maintained. See [Defining Report Layout for Calculate Market Risk Key Figures](#unique_65) [page ] 114 in the Appendix of this document.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Calculate Market Risk Key Figures (AISGENKF). | The Single Value Analysis for Generic Key Figures screen is displayed. |  |
| 3 | Enter Selection Criteria of Gen. Selection | On the Single Value Analysis for Generic Key Figures screen, enter the following data:Evaluation Currency: for example, AEDEvaluation Type: for example, Y001Evaluation Date: for example, <current date>Horizon: for example, <end date of current month>Report Layout: for example, Y01 or other Report Layout you createdPortfolio Hierarchy: for example, 100 |  | The system calculates the net present value as on the horizon date, but selects the transaction data and market data for the evaluation date. |
| 4 | Enter Selection Criteria | Choose the Characteristics tab, enter the following data then choose Execute:Company Code: for example, 3310Product Type: for example, 04M | The Single Value Analysis for assigned Report Layout is displayed. |  |

## Appendix

### Reclassification

#### Perform Valuation Class Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, valuation class transfer are executed from long term to short term and reflected in financial accounting.

Prerequisite

The maturity date of transactions is within one year and the position values are not zero.

If the ABS/MBS is sold, the reclassification can’t be processed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Execute Valuation Class Transfer (TPM15M). | The Valuation Class Transfer screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Valuation Class Transfer screen, enter the following data:Securities: <select this checkbox>Company Code: for example, 3310Security ID: for example, MBS_AE1Security Account: for example, SEC_INVGeneral Valuation Class (in subarea Specific Selection for Outgoing Position): <select this indicator>Key Date: for example <last date of current month>Test Run: <select this checkbox>and choose Execute. | The Edit Selected Positions screen is displayed. |  |
| 4 | Execute Test Run and Check Result | On the Edit Selected Positions screen, select the transactions you want to transfer and enter the new General Valuation Class in field New Valuation Class.Rule of new General Valuation Class:switch the first digit of original General Valuation Class from 1 (long term) to 2 (short term) to change to the new General Valuation Class. For example, if the original General Valuation Class is 12, then the new General Valuation Class is 22.Choose Execute. | The Test Run: Transfer screen is displayed. |  |
| 5 | Review Logs | Choose Messages and Log.In the Information Overview dialog box, choose Posting Log.On the Posting Log: Posted Business Transactions screen, you review the simulated postings. | Logs are reviewed. |  |
| 6 | Production Run | Go back to the initial view of this app. Deselect the Test Run checkbox and repeat the previous steps for production run. | Production run successful, postings are created. |  |

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

This step describes how to change position indicator.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Position Indicator (TPM57A). | The Display Position Indicator screen is displayed. |  |
| 3 | Enter Parameters | On the Display Position Indicator screen, enter following data then choose Enter:Product Group: for example, SecuritiesCompany Code: for example, 3310ID Number: for example, <Security class ID number(s) you have created>Securities Account: for example, <Security account you have created> | The Securities Account Position Indicator and Subledger Position Indicator tabs are displayed.If you would like to make a change, please make the following operation at the Parameter screen.Click on More / Position Indicator / Change. |  |

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
| 2 | Access the SAP Fiori App | Open Schedule Treasury Middle Office Jobs (F2772). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information for New Job | On the Template Selection area, enter following data then choose Step 2:Job Template: for example, <End of Day Processing>Job Name: for example, <End of Day Processing> | You've chosen the job template, and are navigated to the Scheduling Options area. The New Job: Calculate Market Risk Key Figures screen is displayed. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, enter the following data then choose Step 3:For Start Immediately case:Start Immediately: <select>For Recurrence case:Start Immediately: <deselect>Choose Define Recurrence Pattern to define the recurrence pattern in the Scheduling Information dialog box.Start: for example, <Current Date/Current Time>Recurrence Pattern: for example, DailyEvery: for example, 1End: for example, after 7 Occurrence(s)On Non-Working Day: Run on next Working DayNote Schedule this job after back office's job for generating payment request by using the same job template. | You've entered the scheduling recurrence pattern, and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area, enter the following data and choose Schedule:Company Code: 3310Determination Procedure: <select 10 and 20 from the F4 help input> |  |  |
| 7 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The result is displayed on the Job Details screen. |  |

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
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Fix, Pay and Post FlowsJob Name: for example, <Generate Payment Request> | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and in the Scheduling Information dialog box, enter the following data:Start Immediately: <deselect>Job Start: for example, <current date and time default>Time Zone: <select a time zone or use default>Recurrence Pattern: for example, DailyEvery: for example, 1Day(s)End: for example, select After and then enter 7 occurrence(s)On Non-Working Days: for example No RestrictionChoose OK, and choose Step 3.Note If you would rather to start job at once, select Start Immediately checkbox. | You've defined the recurrence pattern and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area,In the Application sub-area, select one or more proper product group.In the General Selection sub-area, enter the following data:Company Code: for example, 3310Transaction: <enter transaction numbers if you'd like to limit transactions>Product Type: <enter product types if you'd like to limit product types>Due Date (Dynamic): for example, 0On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable.In the Posting Control sub-area,Test Run: <deselect>Note You can also choose the Post All Valuation Areas radio button, if you want to post to all valuation areas. |  |  |
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
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information dialog box :Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After 7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK, and choose Step 3.Note If you would like to start job at once, select the Start Immediately checkbox.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Application sub-area, select a proper Application.In the General Selection sub-area, enter the following data:Company Code: for example, 3310Transaction: <enter transaction numbers if you'd like to limit transactions>Product Type: <enter product types if you'd like to limit product types>Due Date (Dynamic): for example, 0In the Posting Control sub-area, make the following selections:Test Run: <deselect this checkbox>Post Operational Only: <Choose this radio button>Note You can also choose Post All Valuation Areas (instead of Post Operational Only) to post flows to all valuation areas. |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

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
| 3 | Create New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Process Business TransactionsJob Name: for example, Process Business Transactions |  |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After 7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Product Groups sub-area, select one or more product groups.Company Code: for example, 3310Valuation Area: for example, AE0, or leave it blank (run for all valuation areas)In the Limit by Transaction Number sub-area, make the following selection:Limit by Transaction Number: <deselect this checkbox>In the Limit by Subledger Positions sub-area, make the following selection:Limit by Subledger Pos.: <select this checkbox>Product Type: <enter product types if you'd like to limit product types>Transaction: <enter transaction numbers if you'd like to limit transactions>In the Limit by Business Transactions sub-area, make the following selection:Trans. to Be Fixed/Posted: <select this checkbox>In the Posting Control sub-area, make the following selection:Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

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
| 5 | Enter Scheduling Options | In the Scheduling Options area, enter the following data, and choose Step 3:Start Immediately: <unselect this checkbox>Start: for example, <first day of next month for this year and at time 03:00>Note Schedule your run time to be later than the Treasury - Calculate Net Present Value - With CVA and DVA job. | You've defined the scheduling option and are navigated to the Parameters area. |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:Company Code: for example 3310Valuation Area: for example, AE0,or leave it blank (run for all valuation areas)In the OTC Transactions sub-area, enter the following data:Transaction: <enter transaction numbers if you'd like to limit transactions>In the Valuation Parameters sub-area, enter the following data:Key Date for Val. (Dynamic): for example, <last date of current month>Valuation Category: for example, select <Mid-year Valuation with Reset>Note When the Period End is also the Year End, the Valuation Category Year End Valuation is used.In the Posting Control sub-area, make the following data:Test Run: <deselect this checkbox> |  |  |
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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Choose Job Template | In the Template Selection area, enter following data then choose Step 2:Job Template: for example, Update Securities Account Cash FlowJob Name: for example, Update Securities Account Cash Flow | The Scheduling Options area is displayed. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time Zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately. | You've defined the recurrence pattern and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area, enter the following data:Company Code: for example, 3310Product Type: for example, 04M |  |  |
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

In this step, you schedule a background job to post Debit Position.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The Template Selection area is displayed. |  |
| 4 | Choose Job Template | On the Template Selection area, enter following data and then choose Step 2:Job Template: for example, Post Debit PositionJob Name: for example, Post Debit Position | The Scheduling Options area is displayed. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After 7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately. | The Parameters area is displayed. |  |
| 6 | Enter Parameters | In the Parameters area, enter the following data:In the General Selection sub-area,Company Code: for example, 3310Product Type: for example, 04MSecurity Account: for example, <Security class ID number(s) you've created>Sec. Class ID Number: for example, <Security class ID number(s) you've created>Update Type: for example, SAM5000 and SAM1111In the Debit Position Parameter sub-area,Up to and Including Pos. Date: for example, <the end date of current month>In the Posting Control sub-area,Document Date: for example, <the end date of current month> |  |  |
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

Table 5: Determination Steps

| Step | Information | Comments about settings |
| --- | --- | --- |
| Output Type | SAP predelivers necessary configurations | Do not change this setting |
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
| 2 | Access the SAP Fiori App | Open Output Parameter Determination (APOC_WD_BRF_DEC_TAB_MAINTAIN). | The Output Parameter Determination screen is displayed. |  |
| 3 | Display Current Email Recipients | Enter the following data and press Enter:Show Rules for: Treasury and Risk Management CorrespondenceDetermination Step: Email RecipientNote By default, no e-mail recipients are maintained by SAP. | The default e-mail recipient rule displays. |  |
| 4 | Maintain Email Recipient for Internal Counterparty | In the Maintain Business Rules section, choose Edit. |  |  |
| 5 | Maintain Email Recipient for Internal Counterparty | Choose Insert New Row. |  |  |
| 6 | Maintain Email Recipient for Internal Counterparty | Make the following entries:Output Type: TRM_DEAL_SLIPNote To enter the value, from the dropdown list, choose Direct Value Input. In the field to the right of the is equal to value, enter TRM_DEAL_SLIP and choose OK. Use this method for the remaining field entries in this step.Role: INEmail Type Code: To, CC, or BCCE-Mail Address: for example, <Email address>Note To add more condition columns, choose Table Settings and make the necessary changes. For example, you can add another condition column (BusPartner) to maintain different e-mail recipients for different business partners. | The internal recipient e-mail address is maintained. |  |
| 7 | Maintain Email Recipient for External Counterparty | Repeat steps 5 to 6 with the following data:Output Type: TRM_TRANSACTION_CONFIRMATION (Transaction Confirmation)Role: INEmail Type Code: To, CC, or BCCE-Mail Address: for example, <Email address> | The external recipient Email address is maintained. |  |
| 8 | Activate Email Addresses | Choose Activate. | The Confirmation Activation dialog box displays. |  |
| 9 | Activate Email Addresses | Choose Yes. | The system displays the message Objects saved and activated. The e-mail addresses are saved and activated. |  |
| 10 | Display Email Settings for Sender Email Address and Email Template | Enter the following data and press Enter:Determination Step: Email Settings | The default e-mail settings are displayed. |  |
| 11 | Change Email Settings for Sender Email Address and Email Template | Choose Edit. |  |  |
| 12 | Change Email Settings for Sender Email Address and Email Template | Make the following entries:Sender Email: for example, <Email address>.Note To create a new e-mail template, use the Maintain Email Template app. | Email settings are changed. |  |
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
| 2 | Access the SAP Fiori App | Open Manage Output Items (F2279). | The Manage Output Items screen is displayed. |  |
| 3 | Enter Filter Criteria and Execute the Report | Make the following entries and choose Go:Application Object ID: <Transaction number>Application Object Type: TRM_CORRESPONDENCENote If the Application Object ID field is not displayed, choose Adapt Filters. Choose More Filters. Select Application Object ID and choose OK.Note When you enter the data in the input field, an input help automatically displays the possible entries for you. You can choose from the list instead of entering the whole words.Correspondence objects could have following status:In PreparationCompletedIn pendingErrorTo check the detailed log, select the correspondence and choose Show Application Log.To resend a correspondence object even it has completed status, you can select the correspondence object and choose Resend. | The status of the output correspondence objects is listed. You can search for your transaction and check the status. |  |

#### Maintain Print Queues

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the outgoing correspondence objects in the Print channel.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Print Queues (F1260). | The Maintain Print Queues screen is displayed. |  |
| 3 | Display TRM Print Queue Status | Scroll down and choose a TRM print queue (for example, Default). | The Print Queue screen is displayed. |  |
| 4 | Display TRM Print Queue Status | Select a line with the transaction number you noted in the prior step. Click the text of the print name to download a PDF file.Note By default, SAP provides the following print queue for TRM:DEFAULT | All the TRM outgoing correspondence objects in channel Print display with latest status. |  |

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

In this step, you create your own e-mail templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Email Templates - Deprecated (F1306). | The Maintain Email Template screen is displayed. |  |
| 3 | Copy a Predelivered Email Template to a Custom Email Template | Choose the Predelivered tab. | The predelivered e-mail templates are displayed. |  |
| 4 | Copy a Predelivered Email Template to a Custom Email Template | Use the Search field to find an email template to copy (for example, FTR_CORR_EMAIL_TEMPLATE_CNF), select the checkbox and choose Copy. | The Copy Template FTR_CORR_EMAIL_TEMPLATE_CNF dialog box displays. |  |
| 5 | Copy a Predelivered Email Template to a Custom Email Template | Make the following entries:Name: for example, TRM Transaction Confirmation Customer Email TemplateNote The new copied e-mail template is prefixed with YY1_. | The system displays the message Template has been copied. |  |
| 6 | Change Customer Email Template | Locate and choose your copied e-mail template within the Custom tab view, in this example: YY1_FTR_CORR_EMAIL_TEMPLATE_CN. |  |  |
| 7 | Change Customer Email Template | Choose Change Details. | The TRM Transaction Confirmation Default Email Template dialog box displays. |  |
| 8 | Change Customer Email Template | Make the following entries and choose Change Details:Description: TRM Transaction Confirmation Customer Email Template | The Email Template view displays. |  |
| 9 | Change Customer Email Template | In the Available Languages pane, select a language version, for example, English. Click the name itself. | The Email Template Content screen is displayed. |  |
| 10 | Change Customer Email Template | Adjust the e-mail subject and body as needed. When done, choose Save.Note SAP defines variables that you can use in e-mail templates. To view the variable list, choose Show Data Fields. | The custom e-mail template is adjusted successfully. |  |

#### Maintain Form Template

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create your own form templates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as Administrator. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Maintain Form Templates (F1434). | The Output Management Form Template screen is displayed. |  |
| 3 | Download a Predelivered Form Template | Choose the Predelivered Templates tab. All the pre-delivered form templates display. | Predelivered templates are displayed. |  |
| 4 | Download a Predelivered Form Template | Select a form template (for example, FDP_TRM_CONF_DE) | The details of the form template are displayed. |  |
| 5 | Download a Predelivered Form Template | Choose Download. | The Download Template dialog box displays. |  |
| 6 | Download a Predelivered Form Template | Choose OK. | The form template is downloaded successfully. |  |
| 7 | Change the customer Form Template File | Using Adobe LiveCycle Designer, adjust and save the form template.Note You must install Adobe LiveCycle Designer to edit the form template. |  |  |
| 8 | Upload Customer Form Template | Open Maintain Form Templates (F1434). | The Output Management Form Template screen is displayed. |  |
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
| 4 | Create New Statement | Choose Create external securities account statement screen, enter the following data and choose Save:Company Code: for example, 3310External Sec. Acct ID: for example, <External Securities Account ID you have created>, for example, MBS_AE1Key Date: for example, <Current Date>Date Category: for example, Position DateStatus: for example, SOPENDescription: for example, External Statement | New statement is created. |  |
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
| 3 | Enter Selection Criteria for Test Run | On the Reverse Valuation screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <unselect this checkbox>Company Code: for example, 3310Valuation Area: leave blank, or enter specific valuation are, for example, AE0Sec. Class ID Number: <Security class ID number(s) for which valuation has been executed>Securities Account: <Securities account(s) for which valuation has been executed>Key Date for Valuation: for example, <the date on which the reversal should take place>Reasons for Reversal: for example, 04 Other reasonsTest Run: <select this checkbox> | The Display Positions to be Reversed screen is displayed. |  |
| 4 | Reverse Valuation for Test Run | On the Display Positions to be Reversed screen, choose Reverse Valuation. | The screen Reversal Log: Reversed Business Transactions is displayed, and message Valuation (test run) has been successfully reversed shows up.Note You can check the simulated reversal posting information on this screen, please note there is no posting created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Display Positions to be Reversed screen is displayed. |  |
| 6 | Reverse Valuation for Production Run | On the Display Positions to be Reversed screen, choose Reverse Valuation (TPM2). | The screen Reversal Log: Reversed Business Transactions is displayed, and message Valuation has been successfully reversed shows up.Note You can check the posting on this screen, this time, accounting document for reversal has been created. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Reverse Debit Position (FWOEZ). | The Manual Posting / Debit Position: Reverse screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Manual Posting / Debit Position: Reverse screen, enter the following data and choose Enter:Company Code: for example, 3310ID Number: for example, <Security class ID number(s) for which debit position has been executed>Securities Account: for example, <Security account for which debit position has been executed> | A list of fixed debit positions is displayed. |  |
| 4 | Reverse Debit Position | On the Manual Posting / Debit Position: Reverse screen, select a record to reverse and choose Reverse business transaction. | The Reverse Business Transaction screen is displayed. |  |
| 5 | Process the Reversal | On the Reverse Business Transaction screen, enter the following data and choose Reverse:Reason for Reversal: for example, Process. errorFI Rversal Date: for example, <original posted date> |  |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Market Data Shift (JBR0). | The Edit Market Data Shifts screen is displayed. |  |
| 3 | Enter Market Data Shifts Name | On the Edit Market Data Shifts screen, enter the following data and choose Create:Market Data Shift: for example, 1 | The Define Market Data Shifts screen is displayed. |  |
| 4 | Define Market Data Shift | On the Edit Market Data Shifts screen, enter the following data:Short Name: for example, <Market Data Shift 0001> |  |  |
| 5 | Maintain Yield Curves of Market Data Shift | On the Edit Market Data Shifts screen, choose the Yield Curves tab, choose the Insert Row button, then enter the following data and choose Save:Short Name: for example, Euro Depo ShiftCurrency: for example, AEDYC. Type: for example, 0001Ref.Int.Rate: for example, AEDM03EIBPercentage: for example, 2 | Market Data Shift is saved |  |

#### Maintain Scenarios

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a scenario. A scenario is a market data record which can contain current market data, exchange rates, exchange rate volatilities, yield curves, interest rate volatilities, e.g., you can create scenarios, which represent market situations you consider possible or probable (for example, a high interest rate scenario with an inverted yield curve).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Scenarios (TV21). | The Scenario Admin: Initial Screen screen is displayed. |  |
| 3 | Enter Scenario Name | On the Scenario Admin: Initial Screen screen, enter the following data and choose Create:Scenario: for example, 1 | The Create Scenario 1 screen is displayed. |  |
| 4 | Maintain Scenario | On the Create Scenario 1 screen, enter the following data:Scenario: Full Name: for example, Scenario 1Scenario: Short Name: for example, Scenario 1 |  |  |
| 5 | Maintain Exch. Rates of Scenario | On the Create Scenario 1 screen, choose the Exchange Rates tab, then enter the following data:Reference Currency: for example, AEDIn the Other Currencies area, choose Insert Row, enter the following data:Currency: for example, USDBid Rate: for example, 1.2Ask Rate: for example, 1.2Then choose Save.Note Market Data Shift is parameter shifts based on market data imported; for scenario, you can maintain parameters without reference. | Scenario is saved |  |

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
| 3 | Access Report Layout Definition Screen | On the Calculate Market Risk Key Figures screen, enter the Evaluation Currency and Evaluation Type, and choose Define Report Layout. | The "Key Figure Layout": Change screen is displayed. | . |
| 4 | Create Layout-ID entries | On the "Key Figure Layout": Change screen, choose New Entries, then insert the following data in the Key Figure Layout form and Save:ROW1Layout-ID: for example, Y01Short Name: for example, NPV/BPV/DurationLong Name: for example, NPV/BPV/DurationROW2Layout-ID: for example, Y02Short Name: for example, NPV + Market Data shiftsLong Name: for example, NPV + Market Data shifts | Two new entries have been created. |  |
| 5 | Access Key Figures Maintain Screen | On the "Key Figure Layout": Change screen, select the checkbox of Layout-ID Y01, then double click Key Figures folder in the Dialog Structure panel. | The Change View "Key Figures": Overview screen is displayed in the main area. |  |
| 6 | Maintain Key Figures of Layout | On the "Key Figure Layout": Change screen, choose New Entries and then insert the following data in the Key Figures form:ROW1Key Figure Name: for example, BARWERTPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDec.Places: for example, 0ROW2Key Figure Name: for example, BPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_BASE_POINTShort Name: for example, BPVShift Rule: for example, 0Dec.Places: for example, 0ROW3Key Figure Name: for example, CRFNPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, RISK_FREE_NPVShort Name: for example, Current Risk Free NPVShift Rule: for example, 0Dec.Places: for example, 0ROW4Key Figure Name: for example, DURATION1Pos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_FWDURATIONShort Name: for example, Modified DurationShift Rule: for example, 0Dec.Places: for example, 0ROW5Key Figure Name: for example, DURATION2Pos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, SKF_MACAULAYShort Name: for example, Macaulay DurationShift Rule: for example, 0Dec.Places: for example, 0and Save. | The New Entries: Overview of Added Entries screen is displayed, allowing entry of the Key Figures name and configuration settings. |  |
| 7 | Access Key Figures Maintain Screen | Go back to the New Entries: Added Entries screen, select the checkbox of Layout-ID Y02, then double click on the Key Figures folder in the Dialog Structure panel. |  |  |
| 8 | Maintain Key Figures of Layout | On the "Key Figure Layout": Change screen, choose New Entries, then insert the following data in Key Figures form and Save:Key Figure Name: for example, NPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDecimal Places: for example, 0 |  |  |

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
| 2 | Access the SAP Fiori App | Open Manage Market Risk Key Figure Sets (AFWKF_SET). | The "Market Risk Key Figure Set": Change screen is displayed. |  |
| 3 | Define Risk Factor Set | On the "Market Risk Key Figure Set": Change screen, double click on the Risk Factor Set folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Factor Set form:RiskF. Set: for example, R01Description: for example, Risk Factor Set with FX Rate and Yld CurvesFX Risk: <select the checkbox>IR Risk: <select the checkbox>Then select the created entry, double click on the Risk Currency folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Risk Currency form:Row 1Currency: for example, USDlR Risk: <select the checkbox>Then double click on the Interest Rate Term folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Interest Rate Term form and choose Save:Row 1Term: for example, 1Time Unit: for example, MonthRow 2Term: for example, 3Time Unit: for example, MonthRow 3Term: for example, 6Time Unit: for example, MonthRow 4Term: for example, 1Time Unit: for example, Year | A new risk factor set is created. |  |
| 4 | Maintain Market Risk Key Set | Double click on the Market Risk Key Figure Set folder in the Dialog Structure panel on the left side. Choose New Entries, insert the following data in the Market Risk Key Figure Set form and choose Save:Row 1MR Key Figure Set: for example, MRK01Description: for example, Market Key Figure Set without VaREvaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <deselect>RT Update: <select>Note If the UpdUponChg checkbox is selected, once a new financial object is created or changed, an automatic calculation of the market risk key figure set is triggered. The calculation only covers the updated object. The adjustment run is based on the basic run of same date that is processed by scheduled job.Row 2MR Key Figure Set: for example, MRK02Description: for example, Market Key Figure Set (VaR Hist.Sim.)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV1RiskF. Set: for example, R01Row 3MR Key Figure Set: for example, MRK03Description: for example, Market Key Figure Set (VaR MonteCarloSim.)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV2RiskF. Set: for example, R01Row 4MR Key Figure Set: for example, MRK04Description: for example, Market Key Figure Set (VaR Variance/Covariance)Evaluation Currency: for example, AEDEval. Type: for example, Y001Calc. VaR: <select>VaRTyp: for example, SV3RiskF. Set: for example, R01Note If the Calc. VaR checkbox is selected, the parameters of the VaR type and the risk factor set need to be assigned; the market data scenario or market data shift should be blank. | Market Risk Key Set is savedThe VaR type SV1 is for the VaR calculation method as historical simulation;The VaR type SV2 is for the VaR calculation method as Monte Carlo simulation;The VaR type SV3 is for the VaR calculation method as variance-covariance approach. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Display Limit Overview (TBL3). | The Overview of Limits screen is displayed. |  |
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
- Accrual calculation of interest payables/receivables

Prerequisite

You have created a security transaction.

NPV values need to be stored in advance of the valuation of Treasury positions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Simulate Period-End Closing (TPM_SIM_VAL). | The Simulate Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Simulate Period-End Closing screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example,04MSecurity ID: for example, <Security Class ID Number(s) created in previous steps>, for example, MBS_AE3Security Account: for example, SEC_INVRecalculate Outdated Sim.Val.: <deselect this checkbox>Note If you set this indicator, you can recalculate the outdated simulation resultsSimulation Date: for example, <the current date>Key Date Valuation: <select this checkbox>Accrual/Deferral: <deselect this checkbox>Note If you set this indicator, the accrual/deferral of expenses and revenues for the selected treasury positions is simulated, and Accrual/Deferral Parameter is displayed.Test Run: <select this checkbox> | The following message is displayed:Processed xx positions; xx successful, 0 failed.If Recalculate Outdated Simulation Results has been executed, the following message is displayed:xx simulated results deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
| 4 | Execute Simulated Valuation | The dialog Message shows up, and choose Continue. | The screen Simulate Period-End Closing is displayed.You can check the simulated valuation information for local GAAP (valuation area AE0).Please note there is no simulated valuation created because it is test run. |  |
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
| 3 | Enter Selection Criteria for Test Run | On the Delete Results of Simulated Period-End Closing screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: leave blank, or enter specific valuation area, for example, AE0Product Type: for example, 04MSecurity ID: for example, <Security Class ID Number(s) created in previous steps>, for example, MBS_AE3Security Account: for example, SEC_INVSimulation Date: for example, <the date on which the reversal should take place>Test Run: <select this checkbox> | The following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |
| 4 | Enter Selection Criteria for Production Run | Go back to the initial screen of this app.On the Delete Results of Simulated Period-End Closing screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |

### Security Account Transfer

#### Security Account Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you transfer the security position to the new security account.

Prerequisite

You have a security purchase transaction.

You've created a new security account SEC_INV2 by referring to the Create Security Account for Issuance step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Securities Account Transfer (FWDU). | The Securities Account Transfer: Initial screen is displayed. |  |
| 3 | Enter Selection Criteria for Securities Account Transfer | On the Securities Account Transfer: Initial screen, enter the following data and choose Execute:Company Code: for example, 3310Security ID: for example, for example, MBS_AE1Source Sec. Account: for example, SEC_INVPos. Value Date: for example, <the current date> | The Securities Account Transfer: Edit screen is displayed. |  |
| 4 | Enter Detailed Data for Securities Account Transfer | On the Securities Account Transfer: Edit screen, enter the following data and choose Save:Target Sec.Acct: for example, SEC_INV2Nominal Amount: for example, 100000Pos. Value Date: for example, <the current date>Calc. Date: for example, <the current date>Document Date: for example, <the current date> | The screen Information Overview is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the posting information by choosing Logs + Messages. |  |
| 5 | Review Logs | Choose Messages and Log.On the Information Overview dialog box, choose Posting Log.On the Posting Log: Posted Business Transactions screen, you review the postings. | Logs are reviewed. |  |

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
- related-to :: [[05-treasury-and-cash-management/asset-backed-securities-management-group-ledger-us-gaap-6b7-ae-1160]]
- related-to :: [[05-treasury-and-cash-management/test-script-asset-backed-securities-management-group-ledger-ifrs-6b6-a]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6B5_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 205,817 chars in the whole document
