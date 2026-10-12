---
id: 05-treasury-and-cash-management/test-script-shareholding-management-5wf-ae-sap-s-4hana-cloud-public-ed
title: "Test Script: Shareholding Management (5WF_AE) - SAP S/4HANA Cloud Public Edition (5WF_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 (AE) test script for scope item 5WF Shareholding Management: BP setup, security classes, purchase, dividends, valuation, sale, reports."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/shareholding-management]
aliases: [5WF_S4CLD2608_BPD_EN_AE]
keywords: [Shareholding Management, business partner setup, security class, securities account, shareholding purchase, shareholding sale, cash dividend, period-end closing, payment processing, treasury correspondence]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WF_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1126
topic: 05-treasury-and-cash-management/shareholding-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Shareholding Management (5WF_AE) - SAP S/4HANA Cloud Public Edition (5WF_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WF_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Shareholding Management** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Shareholding Management (5WF_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 5](#_Toc232857138)

[2 Prerequisites 6](#_Toc232857139)

[2.1 System Access 6](#_Toc232857140)

[2.2 Roles 6](#_Toc232857141)

[2.3 Master Data, Organizational Data, and Other Data 7](#_Toc232857142)

[2.4 Business Conditions 8](#_Toc232857143)

[2.5 Preliminary Steps 9](#_Toc232857144)

[2.5.1 Create Business Partner 9](#_Toc232857145)

[2.5.1.1 Create Business Partner - Counterpart/Depository Bank 9](#_Toc232857146)

[2.5.1.1.1 Maintain General Data for Business Partner 9](#_Toc232857147)

[2.5.1.1.2 Maintain Payment Details for Business Partner 11](#_Toc232857148)

[2.5.1.1.3 Maintain Authorizations for Business Partner 14](#_Toc232857149)

[2.5.1.1.4 Maintain Reporting Data in Company Code for Business Partner 15](#_Toc232857150)

[2.5.1.1.5 Maintain Additional Business Partner Roles 16](#_Toc232857151)

[2.5.1.2 Create Business Partner – Shareholding Issuer 17](#_Toc232857152)

[2.5.1.2.1 Maintain General Data for Business Partner 17](#_Toc232857153)

[2.5.1.2.2 Maintain Reporting Data in Company Code for Business Partner 24](#_Toc232857154)

[2.5.2 Correspondence 27](#_Toc232857155)

[2.5.2.1 Maintain Profile and BP Group Assignments to Internal Recipient 27](#_Toc232857156)

[2.5.2.2 Maintain Profile and BP Group Assignments to External Recipient 29](#_Toc232857157)

[2.5.3 Maintaining Credit Limit 31](#_Toc232857158)

[2.5.3.1 Maintain Limit with Limit Type Y01 31](#_Toc232857159)

[2.5.3.2 Maintain Limit with Limit Type Y07 32](#_Toc232857160)

[2.5.4 Maintain Trader and Trader Authorizations 33](#_Toc232857161)

[2.5.4.1 Define Traders 33](#_Toc232857162)

[2.5.4.2 Define User Data 34](#_Toc232857163)

[2.5.4.3 Maintain Trader Authorizations 35](#_Toc232857164)

[3 Overview Table 37](#_Toc232857165)

[4 Test Procedures 40](#_Toc232857166)

[4.1 Create Security Account 40](#_Toc232857167)

[4.2 Create Security Class for Shareholding 41](#_Toc232857168)

[4.2.1 Create Security Class for Shareholding - Non-affiliated Company 42](#_Toc232857169)

[4.2.2 Create Security Class for Shareholding - Associate or Joint Venture 43](#_Toc232857170)

[4.2.3 Create Security Class for Shareholding - Subsidiary 44](#_Toc232857171)

[4.3 (1XN) Market Rates Management – Manually via Upload 46](#_Toc232857172)

[4.4 Generate Limit Utilizations 46](#_Toc232857173)

[4.5 Analyze Cash Position 47](#_Toc232857174)

[4.6 Analyze Liquidity Forecast 47](#_Toc232857175)

[4.7 Create Shareholding Purchase Transaction 48](#_Toc232857176)

[4.7.1 Create Shareholding Purchase Transaction - Non-affiliated Company 48](#_Toc232857177)

[4.7.1.1 Create Shareholding Purchase Transaction - Non-affiliated Company via Purchase Order 48](#_Toc232857178)

[4.7.1.2 Execute Shareholding Purchase Order 50](#_Toc232857179)

[4.7.1.3 Waiver the Shareholding Order 51](#_Toc232857180)

[4.7.1.4 Create Shareholding Purchase Transaction - Non-affiliated Company via Contract 52](#_Toc232857181)

[4.7.2 Create Shareholding Purchase Transaction - Associate or Joint Venture 54](#_Toc232857182)

[4.7.3 Create Shareholding Purchase Transaction - Subsidiary 56](#_Toc232857183)

[4.8 Correspondence 58](#_Toc232857184)

[4.8.1 Set Settlement Status (Manual) 58](#_Toc232857185)

[4.8.2 Correspondence with PDF Form 59](#_Toc232857186)

[4.8.2.1 Send Confirmation Email/Print 60](#_Toc232857187)

[4.8.2.2 Check Correspondence Status 60](#_Toc232857188)

[4.8.2.3 Receive Incoming Confirmation 62](#_Toc232857189)

[4.8.2.4 Find Deal and Match Deal Details 62](#_Toc232857190)

[4.8.2.5 Set Settlement Status 64](#_Toc232857191)

[4.9 Payment for Purchase 65](#_Toc232857192)

[4.9.1 Option 1: Generate and Automatically Process Payment Request 66](#_Toc232857193)

[4.9.1.1 Process the Payment with the ‘Auto. Payment Run’ Function 66](#_Toc232857194)

[4.9.2 Option 2: Generate and Process Payment Request 69](#_Toc232857195)

[4.9.2.1 Generate Payment Request 69](#_Toc232857196)

[4.9.2.2 Process Payment Request 71](#_Toc232857197)

[4.9.3 Send Payment Medium File 73](#_Toc232857198)

[4.10 Bank Initiated Payment 74](#_Toc232857199)

[4.11 Post to General Ledger 74](#_Toc232857200)

[4.12 Recognize Cash Dividend Income According to the Profit Distribution Plan 76](#_Toc232857201)

[4.12.1 Enter Condition Items in Security ID 76](#_Toc232857202)

[4.12.2 Post the Cash Dividend Income - Non-affiliated Company/Subsidiary 78](#_Toc232857203)

[4.12.3 Post the Cash Dividend - Associate or Joint Venture 79](#_Toc232857204)

[4.13 Corporate Actions for Specific Business Scenario 81](#_Toc232857205)

[4.13.1 Shareholding Split 81](#_Toc232857206)

[4.14 Period-end Closing 83](#_Toc232857207)

[4.14.1 Update Securities Price - Non-affiliated Company 83](#_Toc232857208)

[4.14.2 Perform Key Date Valuation - Non-affiliated Company 83](#_Toc232857209)

[4.14.3 Equity Pickup - Associate or Joint Venture 86](#_Toc232857210)

[4.15 Sell Shareholdings 87](#_Toc232857211)

[4.15.1 Review Shareholding Position 87](#_Toc232857212)

[4.15.2 Create Shareholding Sale Transaction 88](#_Toc232857213)

[4.16 Set Settlement Status 90](#_Toc232857214)

[4.17 Payment from Sale 91](#_Toc232857215)

[4.17.1 Bank Initiated Payment 91](#_Toc232857216)

[4.17.2 Post to General Ledger 92](#_Toc232857217)

[4.18 Reports 94](#_Toc232857218)

[4.18.1 Display Treasury Posting Journal 94](#_Toc232857219)

[4.18.2 Treasury Position Analysis 95](#_Toc232857220)

[4.18.3 Display Treasury Position Values 95](#_Toc232857221)

[4.18.4 Define Financial Positions 96](#_Toc232857222)

[4.18.5 Financial Status - Book Value 99](#_Toc232857223)

[4.18.6 Financial Status - Nominal Amount 99](#_Toc232857224)

[4.18.7 Display Treasury Payments 100](#_Toc232857225)

[4.18.8 Display Treasury Position Flows 101](#_Toc232857226)

[4.18.9 Display Treasury Alerts - Posting 102](#_Toc232857227)

[4.18.10 Display Treasury Alerts- Settlement, Release and Payment 103](#_Toc232857228)

[4.18.11 Display Payment Schedules 104](#_Toc232857229)

[4.18.12 Display Securities Account Class Positions 104](#_Toc232857230)

[4.18.13 Analyze NPV 105](#_Toc232857231)

[4.18.14 Review Limit Utilization Report 106](#_Toc232857232)

[5 Appendix 108](#_Toc232857233)

[5.1 Position Indicator 108](#_Toc232857234)

[5.1.1 Change Position Indicator 108](#_Toc232857235)

[5.2 Job Scheduling 109](#_Toc232857236)

[5.2.1 Generate Limit Utilizations 109](#_Toc232857237)

[5.2.2 Generate Payment Request 110](#_Toc232857238)

[5.2.3 Post Flows to General Ledger 112](#_Toc232857239)

[5.2.3.1 Template - Fix, Pay and Post Flows 112](#_Toc232857240)

[5.2.3.2 Template - Process Business Transactions 114](#_Toc232857241)

[5.2.4 Update Security Cash Flow 116](#_Toc232857242)

[5.2.5 Key Date Valuation 118](#_Toc232857243)

[5.2.6 Post Debit Position 119](#_Toc232857244)

[5.3 Reconciliation of External Securities Account Statements 121](#_Toc232857245)

[5.3.1 Create the Statements of External Securities Account 121](#_Toc232857246)

[5.3.2 Reconciliation of External Securities Account Statements 123](#_Toc232857247)

[5.4 Accounting 124](#_Toc232857248)

[5.4.1 Reverse Accrual 124](#_Toc232857249)

[5.4.2 Reverse Valuation 125](#_Toc232857250)

[5.4.3 Reverse Debit Position 127](#_Toc232857251)

[5.4.4 Reverse Corporate Action 128](#_Toc232857252)

[5.4.5 Manual Posting 129](#_Toc232857253)

[5.5 Market Risk Analyzer 130](#_Toc232857254)

[5.5.1 Manage Market Data Shift 130](#_Toc232857255)

[5.5.2 Maintain Scenarios 131](#_Toc232857256)

[5.5.3 Defining Report Layout for Calculate Market Risk Key Figures 132](#_Toc232857257)

[5.6 Credit Risk Analyzer 135](#_Toc232857258)

[5.6.1 Display Limit Overview 135](#_Toc232857259)

[5.7 Simulated Valuation 136](#_Toc232857260)

[5.7.1 Run Simulated Valuation 136](#_Toc232857261)

[5.7.2 Delete Simulated Valuation 138](#_Toc232857262)

[5.8 Security Account Transfer 139](#_Toc232857263)

[5.8.1 Security Account Transfer 139](#_Toc232857264)

[5.9 Transfer Valuation Class 140](#_Toc232857265)

[5.9.1 Evaluated the Fair Value of Original Position at Transfer Date 141](#_Toc232857266)

[5.9.1.1 Perform Key Date Valuation by Manual Posting 141](#_Toc232857267)

[5.9.2 Reclassify the Shareholding Position and Adjust Relevant Postings 142](#_Toc232857268)

[5.9.2.1 Create Shareholding Purchase Transaction - Associate or Joint venture 142](#_Toc232857269)

[5.9.2.2 Set Settlement Status 144](#_Toc232857270)

[5.9.2.3 Payment for Purchase 145](#_Toc232857271)

[5.9.2.4 Change the Reporting Data in Company Code in Business Partner 146](#_Toc232857272)

[5.9.2.5 Transfer the Current Position of the Shareholding to the New Valuation Class 147](#_Toc232857273)

## Purpose

Overview

The scope item helps you to better manage your shareholding instruments. You can automate labor-intensive processes, such as payment handling and accounting postings, giving you more time to focus on value-added activities. You can manage operational and accounting requirements.

The current scope covers the processes to create securities account and security class, and to purchase, bookkeep, and recognize dividends of and sell a shareholding transaction.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

|  |
| --- |
| Caution Testing in a 3-System LandscapeIn a 3-system landscape (with SAP Central Business Configuration as your configuration environment), changes to software and business configuration are applied to your systems independently of one another. It is therefore your responsibility to manage the active business configuration in your systems and synchronize configuration data in your SAP S/4HANA Cloud Public Edition system landscape. A synchronization is required, for example, after you've enhanced the scope, extended configuration, or adopted new or changed content from content updates or upgrades. For more information, refer to the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b249d650b15e4b3d9fc2077ee921abd0/6c398c4ae7364af69d3edffe7fdc39f2.html) in the SAP Help Portal.Before testing, if you want to use all software features described for the process steps, reports, or items in this document, we recommend the Business Process Configuration Expert in your organization has upgraded the configuration content and deployed the configuration data to your system landscape.If the decision is not to upgrade the configuration content in your test or production system, you can run regression tests of software changes using the procedures in the previous test script version (see the following [link](https://support.sap.com/content/dam/SAAP/Sol_Pack/S4C/Library/TestScripts/5WF_S4CLD2602_BPD_EN_AE.docx) ). |

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
| Valuation Area | AE0 |  |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner screen, choose Organization. | The Create Organization: screen is displayed. |  |
| 4 | Enter address data | On the Create Organization screen, enter the following entries and choose Save:Business Partner: for example, 33537001Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Bank 1 - SAMPLE BANKSalutation: for example, Bank 1Search Term 1/2: for example, Bank 1Street/House number: <Street/House number>Postal Code/City: <Postal Code/City>Ctry/Reg.: AELanguage: ENE-Mail: for example, <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, Dec 31 of the year 9999Note Stay in the screen for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to change mode | On the Display Organization33537001 screen, choose Switch Between Display and Change, and enter following data:Change in BP role: select TR0151 Counterparty | More counterparty related tabs such as Legal Data, Rating show up. |  |
| 6 | Enter Legal data | On the Change Organization:33537001 screen, choose Legal Data in the dropdown list of Navigation Menu, enter the following data and choose Save:Country/Region: AENote Navigation Menu is on the very right side of the screen. It's displayed as  , which is right next to the symbol .Stay in the screen for subsequent steps. | The Legal data is entered and saved.The Change Organization:33537001, role Counterparty screen is displayed. |  |
| 7 | Enter Payment Transaction data | On Change Organization:33537001 screen, choose Payment Transactions of the dropdown menu of Navigation Menu, and enter the following 2 rows of data:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, 18121976Bank Acct: for example, Bank accountIBAN: choose IBAN button and choose Continue in the popup IBAN screenRow 2:ID: for example, USD1C/R: for example, AEBank Key: for example, 18121976Bank Acct: for example, Bank accountIBAN: choose IBAN button and choose Continue in the popup IBAN screen.Now choose Save.If the Information dialog box appears when you choose IBAN, please choose Continue. | The Payment transaction data is entered and the Business Partner is saved. |  |

###### Maintain Payment Details for Business Partner

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen displays. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP. In the popup dialog box, enter following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: select TR0151 Counterparty(defined) | Change Organization: 33537001, new role Counterparty screen displays. |  |
| 4 | Enter SI: Payment Details data | On the Change Organization:33537001, Role Counterparty screen, choose Company Code, and enter following data and choose Enter:Company Code: for example, 3310Choose SI: Payment Details and make the following four rows of entries:Row 1:Currency: for example, AEDPay.Det.ID: for example, AEDIHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: <leave blank>Partner Bank: <Leave blank>Payment Request: <Deselect>Payment Methods: <Leave blank>Row 2:Currency: for example, AEDPay.Det.ID: for example, AEDOHouse Bank: for example, AEBK1Account ID: for example, AEAC1Payer/ee: for example, 33537001Partner Bank: for example, AED1Payment Methods: TPayment Request: <select>Row 3:Currency: USDPay.Det.ID: for example, USDIHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/ee: for example, <leave blank>Payment Request: <Deselect>Payment Methods: <leave blank>Row 4:Currency: for example, USDPay.Det.ID: for example, USDOHouse Bank: for example, AEBK1Account ID: for example, USDACPayer/Payee: for example, 33537001Partner Bank: for example, USD1Payment Request: <select>Payment Methods: FStay in this screen for subsequent steps.Note If the following message displays, choose No.Business partner proposed as payer/payee (see long text) Display this message for this business partner again? | The SI: Payment Details data is entered. |  |
| 5 | Assign Payment details | From the last screen of previous step,For AED, select the Checkbox for AEDAEDI. Choose Assign. In the Counterparty Change: Payment Details Assignment dialog box, choose Select All Incoming. Now AEDI displays under PmntID-Inc, choose Continue to close the dialog box.Select the Checkbox for AEDAEDO. Choose Assign, in the dialog box Counterparty Change: Payment Details Assignment, choose Select All Outgoing. Now AEDO is displayed under P-ID Outg. Choose Continue to close the dialog box.Do the same for USD:USD I: PmntID-IncUSD O: P-ID Outg.On the Change Organization:33537001, Role Counterparty screen, choose Save. | Payment details and the assignments are saved. |  |

###### Maintain Authorizations for Business Partner

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP. In the Open business partner dialog box, enter following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter the following data:Change in BP Role: select select TR0151 Counterparty(defined) | Change Organization: 33537001 , role Counterparty screen is displayed. |  |
| 4 | Enter SI: Authorizations data | On the Change Organization:33537001, role Counterparty screen, choose Company Code, choose SI: Authorizations, enter the following data and choose Save.Securities: select the Auth. checkboxYou can also give authorization to a specific product type and transaction type by expending the folders. For testing purpose, we give all authorizations to all kinds of product types and transaction types. | The Authorizations data is saved. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP, in the Open business partner dialog box, enter following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: choose TR0151 Counterparty(defined) | Change Organization: 33537001 , role Counterparty screen displays. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization:33537001, role Counterparty screen, choose Company Code, choose Reporting Data in Company Code, and enter following data and choose Save.Comp. Rel.: for example, 3 OtherIf you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown menu.Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 Other4 Do not use itIt can be used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

###### Maintain Additional Business Partner Roles

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes the detailed steps on how to maintain additional roles required for Securities for Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP, in the Open business partner dialog box, enter following data:Business Partner: 33537001Choose Enter and then choose Switch Between Display and Change. | Change Organization: 33537001 screen is displayed. |  |
| 4 | Add New Role of TR0150 Issuer | Select Change in BP Role to: for example, TR0150 IssuerChoose Save. | Data is saved. |  |
| 5 | Add New Role of TR0152 Depository Bank | Select Change in BP Role to: for example, TR0152 Depository BankChoose Save. | Data is saved. |  |

##### Create Business Partner – Shareholding Issuer

###### Maintain General Data for Business Partner

###### Maintain General Data for Business Partner - Non-affiliated Company

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner screen, choose Organization. | The Create Organization: screen is displayed. |  |
| 4 | Enter address data | On the Create Organization screen, enter the following entries and choose Save:Business Partner: for example, 33537005Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Non-affiliated companySalutation: for example, Non-affiliated companySearch Term 1/2: for example, Non-affiliated companyStreet/House Number: for example,Postal Code/City: for example,Ctry/Reg.: AELanguage: ENE-Mail: for example, <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, Dec 31 of the year 9999Note Stay in the screen for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to change mode | On the Display Organization33537005 screen, choose Switch Between Display and Change, and enter following data:Change in BP role: select TR0151 Counterparty | More counterparty related tabs such as Legal Data, Rating show up. |  |
| 6 | Enter Legal data | On the Change Organization:33537005 screen, choose Legal Data in the dropdown list of Navigation Menu, enter the following data and choose Save:Country: AENote Navigation Menu is on the very right side of the screen. It's displayed as  , which is right next to the symbol .Stay in the screen for subsequent steps. | The Legal data is entered and saved.The Change Organization:33537005, role Counterparty screen is displayed. |  |
| 7 | Enter Payment Transaction data | On Change Organization:33537005 screen, choose Payment Transactions of the dropdown menu of Navigation Menu, and enter the following 2 rows of data:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, 18121976Bank Acct: for example, Bank accountRow 2:ID: for example, USD1C/R: for example, AEBank Key: for example, 18121976Bank Acct: for example, Bank accountNow choose Save. | The Payment transaction data is entered and the Business Partner is saved. |  |
| 8 | Add New Role of TR0150 Issuer | On the Maintain Business Partner: screen, enter the following data: Select Change in BP Role to: for example, TR0150 IssuerChoose Save. | Data is saved. |  |

###### Maintain General Data for Business Partner - Associate or Joint Venture

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner screen, choose Organization. | The Create Organization: screen is displayed. |  |
| 4 | Enter address data | On the Create Organization screen, enter the following entries and choose Save:Business Partner: for example, 33537006Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, Associate or Joint ventureSalutation: for example, Associate or Joint ventureSearch Term 1/2: for example, Associate/Joint vent.Street/House number: for example,Postal Code/City: for example,Ctry/Reg.: AELanguage: ENE-Mail: for example, <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, Dec 31 of the year 9999Note Stay in the screen for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to change mode | On the Display Organization33537006 screen, choose Switch Between Display and Change, and enter following data:Change in BP role: select TR0151 Counterparty | More counterparty related tabs such as Legal Data, Rating show up. |  |
| 6 | Enter Legal data | On the Change Organization:33537006 screen, choose Legal Data in the dropdown list of Navigation Menu, enter the following data and choose Save:Country: AENote Navigation Menu is on the very right side of the screen. It's displayed as  , which is right next to the symbol .Stay in the screen for subsequent steps. | The Legal data is entered and saved.The Change Organization:33537001, role Counterparty screen is displayed. |  |
| 7 | Enter Payment Transaction data | On Change Organization:33537006 screen, choose Payment Transactions of the dropdown menu of Navigation Menu, and enter the following 2 rows of data:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, 18121976Bank Acct: for example, Bank accountRow 2:ID: for example, USD1C/R: for example, AEBank Key: for example, 18121976Bank Acct: for example, Bank accountNow choose Save. | The Payment transaction data is entered and the Business Partner is saved. |  |
| 8 | Add New Role of TR0150 Issuer | On the Maintain Business Partner: screen, enter the following data: Select Change in BP Role to: for example, TR0150 IssuerChoose Save. | Data is saved. |  |

###### Maintain General Data for Business Partner - Subsidiary

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP). | The Maintain Business Partner: screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Maintain Business Partner screen, choose Organization. | The Create Organization: screen is displayed. |  |
| 4 | Enter address data | On the Create Organization screen, enter the following entries and choose Save:Business Partner: for example, 33537007Grouping: <select TR02 Treasury partner (external)>Create in BP role: <select 000000 Business Partner (Gen.)>Title: <select 0003 Company>Name: for example, SubsidiarySalutation: for example, SubsidiarySearch Term 1/2: for example, SubsidiaryStreet/House number: for example,Postal Code/City: for example,Ctry/Reg.: AELanguage: ENE-Mail: for example, <E-mail>Address Valid From: for example, <Current date in previous year>Address Valid To: for example, Dec 31 of the year 9999Note Stay in the screen for subsequent steps. | The Business partner is created successfully. |  |
| 5 | Switch to change mode | On the Display Organization33537007 screen, choose Switch Between Display and Change, and enter following data:Change in BP role: select TR0151 Counterparty | More counterparty related tabs such as Legal Data, Rating show up. |  |
| 6 | Enter Legal data | On the Change Organization:33537007 screen, choose Legal Data in the dropdown list of Navigation Menu, enter the following data and choose Save:Country: AENote Navigation Menu is on the very right side of the screen. It's displayed as  , which is right next to the symbol .Stay in the screen for subsequent steps. | The Legal data is entered and saved.The Change Organization:33537001, role Counterparty screen is displayed. |  |
| 7 | Enter Payment Transaction data | On Change Organization:33537007 screen, choose Payment Transactions of the dropdown menu of Navigation Menu, and enter the following 2 rows of data:Row 1:ID: for example, AED1C/R: for example, AEBank Key: for example, 18121976Bank Acct: for example, Bank accountRow 2:ID: for example, USD1C/R: for example, AEBank Key: for example, 18121976Bank Acct: for example, Bank accountNow choose Save. | The Payment transaction data is entered and the Business Partner is saved. |  |
| 8 | Add New Role of TR0150 Issuer | On the Maintain Business Partner: screen, enter the following data: Select Change in BP Role to: for example, TR0150 IssuerChoose Save. | Data is saved. |  |

###### Maintain Reporting Data in Company Code for Business Partner

###### Maintain Reporting Data in Company Code for Business Partner - Non-affiliated Company

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain company relationship for Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP) | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP, in the Open business partner dialog box, enter following data:Business Partner: 33537005Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: choose TR0151 Counterparty(defined) | Change Organization: 33537005 , role Counterparty screen displays. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization:33537005, role Counterparty screen, choose Company Code, choose Reporting Data in Company Code, and enter following data and choose Save.Comp. Rel.: for example, 3 OtherIf you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown menu.Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 OtherIt can be used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

###### Maintain Reporting Data in Company Code for Business Partner - Associate or Joint Venture

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain company relationship for Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP) | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP, in the Open business partner dialog box, enter following data:Business Partner: 33537006Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: choose TR0151 Counterparty(defined) | Change Organization: 33537006 , role Counterparty screen displays. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization:33537006, role Counterparty screen, choose Company Code, choose Reporting Data in Company Code, and enter following data and choose Save.Comp. Rel.: for example, 2 ShareholdingIf you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown menu.Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 OtherIt can be used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

###### Maintain Reporting Data in Company Code for Business Partner - Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you maintain company relationship for Business Partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP) | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP, in the Open Business Partner dialog box, enter following data:Business Partner: 33537007Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: choose TR0151 Counterparty(defined) | Change Organization: 33537007 , role Counterparty screen displays. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization:33537007, role Counterparty screen, choose Company Code, choose Reporting Data in Company Code, and enter following data and choose Save.Comp. Rel.: for example, 1 Affiliated CompanyIf you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown menu.Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 OtherIt can be used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

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
| 2 | Access the SAP Fiori App | Open Assign Profile and BP Group - Internal Recipients (FTR_INT_ASSIGN). | The Assignment of Profiles and BP Groups to Internal Recipients: view displays. |  |
| 3 | Enter Business partner data on the view | On the left side of Assignment of Profiles and BP Groups to Internal Recipients view, choose Insert Row and enter the following data, and then select the item by ticking the checkbox before:IntRec: for example, INT.RECPCoCd: for example, 3310Recipient/SenderType: for example, INTERNALCheckbox: <select> | The Business Partner information is entered. |  |
| 4 | Assign Business profile and BP group to the Business Partner | On the top-right side of Assignment of Profiles and BP Groups to Internal Recipients view, expend the node, and choose one item to maintain the business partner profile and business partner group, for example, Shareholding > 16A Shareholding > 100 purchase > 20 ContractThen on the bottom-right side of the screen,choose Insert Row, enter the following data, and choose SaveProfile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTUser Name: <select a User ID>.Choose Insert Row again and add another entry as following and choose Save:Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTUser Name: <select a User ID>.Note The user ID is a backend user ID. | Business partner profile and BP group and user ID are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat the previous step to assign BP profile and BP group to the rest of Product type/Transaction Type/Activity category | Check the item INT.RECP in the left side view, and choose Modify Row.Repeat the above step to maintain other items under the Shareholding folder:16A – 200 – 20 | BP profiles and BP groups and user IDs are assigned to all the listed Product Types/Transaction Types/ Activity Categories. |  |

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

You can assign this Business partner group to your Business Partner. You can also use configuration activities Define Business Partner Group and Assign Attributes for Business Partner Groups to add your own Business partner group and assign appropriate attributes according to your specific requirement. Different business partner profiles and BP groups could be assigned to the same business partner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Assign Profile and BP Group - External Recipients (FTR_EXT_ASSIGN). | The Assignment of Profiles and BP Groups to External Recipients: view displays. |  |
| 3 | Enter Business partner data on the view | On the left side of Assignment of Profiles and BP Groups to External Recipients: view, choose Insert Row and enter the following data, and then select the business partner by ticking the checkbox before the business partner:BusPartner: for example, 33537001CoCd: for example, 3310Recipient/SenderType: for example, COUNTERPARTY | The Business Partner information is entered. |  |
| 4 | Assign Business profile and BP group to the Business Partner | On the top right side of the Assignment of Profiles and BP Groups to External Recipients screen, expand the node, and choose one item to maintain the business partner profile and business partner group, for example, Shareholding > 16A Shareholding > 100 purchase > 20 ContractThen on the bottom-right side of the screen, choose Insert Row and enter the following data:Profile: for example, PR_EMAILBP Group: for example, BPG_DEFAULTChoose Insert Row again and add another entry as following data：Profile: for example, PR_PRINTBP Group: for example, BPG_DEFAULTNote Normally you only assign one profile to a Product type/Transaction type/Activity Category. | Business partner profiles and BP groups are assigned for the Product type/Transaction type/Activity category. |  |
| 5 | Repeat the previous step to assign BP profiles and BP groups to the rest of Product type/Transaction Type/Activity category | Check the item 33537001 in the left side view, and choose Modify Row.Repeat the above step to maintain other items under the Shareholding folder:16A – 200 – 20 | For all the listed Product Types/Transaction Types/ Activity Categories, BP profiles and BP groups are assigned. |  |

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
| 4 | Create a New Record | Select New Entries, enter the following data and choose Save:Trader: for example, TRADER2 | The Treasury: Traders is saved. The New Entries: Overview of Added Entries screen is displayed. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Define User Data (S_ALR_87007933). | The Change View "Treasury: User master data supplements": Overview screen is displayed |  |
| 3 | Create a New Record | Select New Entries, enter the following data and choose Save:User Name: for example, <Your user name>Trader: for example, TRADER2 | The data is saved. |  |

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

A trader must be defined before this step. Refer to the [Define Traders](#unique_25) [page ] 33 step for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Trader Authorizations (TBT1). | The Create/Change Trans. Authorization for Trader: Init. Screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter data and select Enter.Trader: TRADER2Company Code: for example, 3310 | The Create/Change Transaction Authorization for Traders screen is displayed. |  |
| 4 | Enter Authorization and Save | Select or unselect on the Authorization column and choose Save.Note Make sure to authorize TRADER2 for the Shareholding transactions under Securities. | The data is saved as indicated by a message. For example: Transaction authorizations for trader TRADER2 are being saved. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Create Security Account](#unique_29) [page ] 40 | Treasury Specialist - Back Office | Manage Securities Accounts (TRS_SEC_ACC) | Maintain FX Spot rates |
| [Create Security Class for Shareholding](#unique_30) [page ] 41 | Treasury Specialist - Back Office | Manage Security Classes (F8717) | Security Account is created. |
| [(1XN) Market Rates Management – Manually via Upload](#unique_31) [page ] 46 |  |  | Maintain FX Spot rates |
| [Generate Limit Utilizations](#unique_32) [page ] 46 | Treasury Specialist - Middle Office | End-of-Day Processing (KLNACHT) | Limit utilizations was determinate and updated. |
| [Analyze Cash Position](#unique_33) [page ] 47 | Cash Manager | Cash Flow Analyzer (F2332) | Cash manager check the cash position status, and make decisions of right financial instruments for short-term purpose based on analysis of cash position. |
| [Analyze Liquidity Forecast](#unique_34) [page ] 47 | Cash Manager | Cash Flow Analyzer (F2332) | The cash manager check the liquidity forecast regularly and make decisions regarding medium-term or long-term financial instruments. |
| [Create Shareholding Purchase Transaction](#unique_35) [page ] 48 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | A stock transaction is created. |
| [Set Settlement Status (Manual)](#unique_36) [page ] 58 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The transaction is settled manually. |
| [Correspondence with PDF Form](#unique_37) [page ] 59 | Treasury Specialist - Back Office | Process Correspondence - Monitor (FTR_COMONI) |  |
| [Process the Payment with the ‘Auto. Payment Run’ Function](#unique_38) [page ] 66 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Process the payment with the ‘automatic payment run’ function. |
| [Generate Payment Request](#unique_39) [page ] 69 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1)Fix and Pay Flows (TBB1_PAY) | Payment request is generated. |
| [Process Payment Request](#unique_40) [page ] 71 | Treasury Specialist - Back Office | Automatic Payment Transactions for Payment Requests (F111) | Payment program for payment request processes. |
| [Bank Initiated Payment](#unique_41) [page ] 74 | N/A | N/A |  |
| [Post to General Ledger](#unique_42) [page ] 74 | Treasury Specialist - Back Office | Fix, Pay and Post Flows (TBB1) | The transaction is posted. |
| [Enter Condition Items in Security ID](#unique_43) [page ] 76 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The condition item for cash dividend income is maintained in the security class. |
| [Post the Cash Dividend Income - Non-affiliated Company/Subsidiary](#unique_44) [page ] 78 | Treasury Accountant | Execute Debit Position - Manual Debit Position (FWZE) | The cash dividend is posted. |
| [Post the Cash Dividend - Associate or Joint Venture](#unique_45) [page ] 79 | Treasury Accountant | Create Manual Posting (FWBS) | The cash dividend is posted. |
| [Shareholding Split](#unique_46) [page ] 81 | Treasury Specialist - Back Office | Manage Corporate Actions (FWK0) | The stock units position have updated. |
| [Update Securities Price - Non-affiliated Company](#unique_47) [page ] 83 | Treasury Specialist - Back Office | Enter Securities Prices (FW17) | Stock price is updated. |
| [Perform Key Date Valuation - Non-affiliated Company](#unique_48) [page ] 83 | Treasury Accountant | Run Valuation (TPM1) | The key date valuation is performed. |
| [Review Shareholding Position](#unique_49) [page ] 87 | Treasury Specialist - Front Office | Display Securities Account Class Positions (TPM40A) | You review the account class positions. |
| [Create Shareholding Sale Transaction](#unique_50) [page ] 88 | Treasury Specialist - Front Office | Create Securities Transaction (TS01) | The sale transaction is created. |
| [Set Settlement Status](#unique_51) [page ] 90 | Treasury Specialist - Back Office | Process Securities Transactions - Collective Processing (TS00) | The transaction is settled manually. |
| [Bank Initiated Payment](#unique_52) [page ] 91 | n/a | n/a |  |
| [Post to General Ledger](#unique_53) [page ] 92 | Treasury Accountant | Fix, Pay and Post Flows (TBB1) | The transaction is posted. |
| [Display Treasury Posting Journal](#unique_54) [page ] 94 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Treasury posting journal is displayed. |
| [Treasury Position Analysis](#unique_55) [page ] 95 | Treasury Accountant | Treasury Position Analysis | Treasury position analysis is displayed. |
| [Display Treasury Position Values](#unique_56) [page ] 95 | Treasury Accountant | Display Treasury Position Values (F1867) | Treasury position values are displayed. |
| [Define Financial Positions](#unique_57) [page ] 96 | Treasury Risk Manager | Define Financial Positions (FTR_FP_DEF) | Financial Positions are defined. |
| [Financial Status - Book Value](#unique_58) [page ] 99 | Treasury Risk Manager | Financial Status (F2136) | The financial status on book values is displayed. |
| [Financial Status - Nominal Amount](#unique_59) [page ] 99 | Treasury Risk Manager | Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)) | The financial status on nominal amount is displayed. |
| [Display Treasury Payments](#unique_60) [page ] 100 | Treasury Specialist - Back Office | Display Treasury Payments (TPM20A) | Treasury Payment displays. |
| [Display Treasury Position Flows](#unique_61) [page ] 101 | Treasury Specialist - Back Office | Display Treasury Position Flows (F1754) | Treasury posting flows display. |
| [Display Treasury Alerts - Posting](#unique_62) [page ] 102 | Treasury Accountant | Display Treasury Alerts - Posting (F4984) | Treasury Alerts-Posting display. |
| [Display Treasury Alerts- Settlement, Release and Payment](#unique_63) [page ] 103 | Treasury Specialist - Back Office | Display Treasury Alerts - Settlement (F4979) | Treasury Alerts display. |
| [Display Payment Schedules](#unique_64) [page ] 104 | Treasury Accountant | Display Payment Schedules (TJ04) | Payment schedules displays. |
| [Display Securities Account Class Positions](#unique_65) [page ] 104 | Treasury Accountant | Display Securities Account Class Positions (TPM40A) | Display Securities Account Class Positions display |
| [Analyze NPV](#unique_66) [page ] 105 | Treasury Specialist - Middle Office | Analyze NPV (JBRX) | The NPV Result displays. |
| [Review Limit Utilization Report](#unique_67) [page ] 106 | Treasury Specialist - Middle Office | Review Limit Utilizations (TBLB) | Limit utilizations display. |

## Test Procedures

### Create Security Account

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The stock, or more broadly, a security in general, is usually purchased and maintained by a broker such as a bank or a securities company. The transactions involve opening a security account with the broker. The broker maintains positions by each of the securities account. In the system, the securities positions are also maintained on an account level. This procedure details out the steps of creating a security account.

Prerequisite

A Business Partner with TR0152 Depository Bank is created with ID 33537001.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Securities Accounts (TRS_SEC_ACC). | The Choose Securities Account and Company Code screen is displayed. |  |
| 3 | Enter Account Identifier | Enter a new unique identifier for the new Securities Account, and choose Create.Company Code: for example, 3310Securities Account: for example, AE_SHNoteChoose Create if a confirmation dialog pops up.if above account is already created, you can choose Display or Change to either view or edit the account. | A new account is created. |  |
| 4 | Enter General Data of the Account | Enter the following data and move to the next tab:Securities Account ID: for example, 33537001AE0Securities Account Type: for example, SAC Asset Securities Account |  |  |
| 5 | Enter Bank Data | Enter the following data and choose Save:Depository Bank: for example, 33537001External Securities Account ID: for example, 123XXXX567Line 1:Payment Currency: AEDHouse Bank: AEBK1Account ID: AEAC1Line 2:Payment Currency: USDHouse Bank: AEBK1Account ID: USDAC | The data is saved |  |

### Create Security Class for Shareholding

According to the different position of shareholding, the underlying company of the shareholdings could be divided into three types:

1. Non-affiliated company - holding ratio < 20%
2. Associate or Joint venture - holding ratio during 20% to 50%
3. Subsidiary - holding ratio > 50%

Eash type of shareholding should be designated an accounting method.

In the following test case, we suppose there are three different shareholdings with different holding ratios. Each shareholding was designated a different accounting measure method.

#### Create Security Class for Shareholding - Non-affiliated Company

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The user needs to create a security class ID before creating any transaction on a security. This section introduces how to create a security class under product type 16A - Shareholding.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.ID Number: for example, SH_AE1Product Type: 16A Shareholding | The New Object screen displays with previously specified ID Number. |  |
| 4 | Enter Header | On the tab Header, enter the following data:Security Class Name: for example, Shareholding #1Gen. Sec. Classification: 04 ShareholdingsStatus: for example, ActivePlease switch to the Basic Data tab. | The general data is entered. |  |
| 5 | Enter Basic Data | Under the Basic Data tab, enter the following data :Issuer: for example, 33537005Nominal Value: for example, 1.00Issue Currency: for example, AEDIssue Price: for example, 1.00Quotation: for example, 2 Unit-quotedSharehoiding Type: for example, 91 Non-affiliatedShareholding Structure: for example, 91 Holding structure |  |  |
| 6 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: for example, DFMCurrency: for example, AED | Security class is created. |  |

#### Create Security Class for Shareholding - Associate or Joint Venture

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The user needs to create a security class ID before creating any transaction on a security. This section introduces how to create a security class under product type 16A - Shareholding.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.ID Number: for example, SH_AE2Product Type: 16A Shareholding | The New Object screen displays with previously specified ID Number. |  |
| 4 | Enter Header | On the tab Header, enter the following data:Security Class Name: for example, Shareholding #2Gen. Sec. Classification: 04 ShareholdingsStatus: for example, ActivePlease switch to the Basic Data tab. | The general data is entered. |  |
| 5 | Enter Basic Data | Under the Basic Data tab, enter the following data:Issuer: for example, 33537006Nominal Value: for example, 1.00Issue Currency: for example, AEDIssue Price: for example, 1.00Quotation: for example, 2 Unit-quotedSharehoiding Type: for example, 92 AssociateShareholding Structure: for example, 91 Holding structure |  |  |
| 6 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: for example, DFMCurrency: for example, AED | Security class is created. |  |

#### Create Security Class for Shareholding - Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The user needs to create a security class ID before creating any transaction on a security. This section introduces how to create a security class under product type 16A - Shareholding.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Choose Create, enter a Security Class ID and Product Type in the pop-up dialog​ New Object, then choose Continue.ID Number: for example, SH_AE3Product Type: 16A Shareholding | The New Object screen displays with previously specified ID Number. |  |
| 4 | Enter Header | On the tab Header, enter the following data:Security Class Name: for example, Shareholding #3Gen. Sec. Classification: 04 ShareholdingsStatus: for example, ActivePlease switch to the Basic Data tab. | The general data is entered. |  |
| 5 | Enter Basic Data | Under the Basic Data tab, enter the following data :Issuer: for example, 33537007Nominal Value: for example, 1.00Issue Currency: for example, AEDIssue Price: for example, 1.00Quotation: for example, 2 Unit-quotedSharehoiding Type: for example, 94 SubsidiaryShareholding Structure: for example, 91 Holding structure |  |  |
| 6 | Enter Exchanges | Switch to the Exchanges tab, enter the following data and choose Create:Exchange: for example, FSXCurrency: for example, AED | Security class is created. |  |

### (1XN) Market Rates Management – Manually via Upload

Purpose

This step provides instructions on how to enter market data such as foreign currency exchange spot rates, etc.

Shareholding is quoted usually in the exchange’s currency. When the corporate is purchasing Shareholding from an overseas market, the foreign currency exchange spot rates will be used for this purpose.

Procedure

Please refer to the test script Market Rates Management – Manually via Upload (1XN) for more instructions.

### Generate Limit Utilizations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the End of the transaction day, the middle officier can trigger the end-of-day processes.

|  |
| --- |
| Note You can also schedule background job for this step, please see job scheduling step in Appendix. |

Prerequisite

The market data has been imported.

If security exists, the spot price needs to be maintained for the current date. Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload (1XN) test script for detailed procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open End-of-Day Processing (KLNACHT). | The End-of-Day Processing screen is displayed. |  |
| 3 | Enter Criteria of End-of-Day Processing | On the End-of-Day Processing screen, enter the following data and choose Execute:Valuation Date: <the current Date>Determination Procedure: 10 to 20Company Code: for example, 3310 | The End-of-day processing was completed successfully message is displayed. |  |

### Analyze Cash Position

Purpose

At the end of the transaction day, the Cash Manager will always check the cash position status, and make investment or financial decisions based on the analysis of cash position.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) app to analyze the cash position. For detailed information, please refer to the Basic Cash Operations(BFB) test script.

### Analyze Liquidity Forecast

Purpose

At the end of the transaction day, the Cash Manager will always check the cash position status, and make investment or financial decisions based on the analysis of cash position.

Procedure

If cash management is implemented in your system, you can use the Cash Flow Analyzer (F2332) app to analyze the cash position. For detailed information, please refer to the Basic Cash Operations(BFB) test script.

### Create Shareholding Purchase Transaction

According to the created security class IDs for the three different shareholdings in previous steps, each shareholding would be designated an accounting method.

In transaction, if you select General Valuation Classes 62, 63, 61 and 60, you designate the accounting methods FVTPL, FVOCI, Equity Method, At Cost respectively.

- Shareholding #1 - Meassure as Financial Instruments
- Shareholding #2 - Equity Method
- Shareholding #3 - At Cost Method

#### Create Shareholding Purchase Transaction - Non-affiliated Company

##### Create Shareholding Purchase Transaction - Non-affiliated Company via Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you purchase a shareholding and the purchased ratio is under 20%, you enter the purchase order information into the system.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.

Procedure

Please create two purchase orders via below steps.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Securities Transaction: Entry Screen screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Entry Screen, enter the following data and choose Enter:Company Code: for example, 3310ID Number: for example, SH_AE1Transaction Type: 100Partner: for example, 33537001In the Activity area,Order/Fixing: <select> | The Create Securities Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Flow Type: for example, 0100 Purchase (transaction)In the Position area,Securities Account: for example, AE_SHIn the Amounts area,Amounts of Units: for example, 10000In the Order Data area,Limit Date: for example, <the current date>Limit Price: for example, 100 | All data is entered.Note You can select the below flow types as desired:0100 Purchase (transaction), means shareholding is purchased by cash.0105 Purchase (other consid-er.), means shareholding is purchased by other considerations (for example, fixed asset), you need to clear the balance of technical clearing account manually. |  |
| 5 | Enter Data on Tab Other Flows | On the tab Structure, you can record the transaction fee relevant information by enter the following data:In the Other Flows area,Flow Type: for example, 0315 Brokerage not capitalized(tr.)Payment Amount: for example, 100Payment Currency: for example, AED |  |  |
| 6 | Save the Transaction | Choose Save.Note If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a dialog box appears asking to Create Position Indicator.If the Position Indicator is already created, then you can ignore below step. The following message is displayed: Security transaction XXXXX created in company code YYYY |  |  |
| 7 | Create Position Indicator | Choose Create Automatically. | The transaction is created. |  |

##### Execute Shareholding Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You decide to purchase a shareholding with the created order. After the purchase, you enter the purchase contract information into the system.

|  |
| --- |
| Note You can skip the step [Create Shareholding Purchase Transaction - Non-affiliated Company via Contract](#unique_75) [page ] 52 as the shareholding purchase transaction is generated. |

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
| 3 | Enter Data on Initial Screen | In the search term area, enter the following data and choose Go:Key Date: for example, TodayCompany Code: for example, 3310Transaction: <the transaction number(s)> | The shareholding purchase order transaction is displayed. |  |
| 4 | Execute the Purchase Order | In the Transaction area, select the transaction and choose Execute Order in the toolbar via button …. | The details of the shareholding purchase order transaction are displayed. |  |
| 5 | Add Relevant Information and Save the Transaction | On the tab Structure, enter the following data:In the Position area,General Valuation Class: for example, Equity: Fair value th. OCIIn the Amount area,Price (Unit Quoted): for example, 100Then choose Save.Note If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a dialog box appears asking to Create Position Indicator.If the Position Indicator is already created, then you can ignore below step. The following message is displayed: Security transaction XXXXX created in company code YYYY |  |  |
| 6 | Create Position Indicator | Choose Create Automatically. | The shareholding purchase order is executed, the relevant shareholding purchase transaction is created. |  |

##### Waiver the Shareholding Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You decide to waiver a shareholding purchase order. Once you cancel the order, you need to maintain the relevant information in the system.

Prerequisite

- The relevant Securities ID is created.
- The relevant Securities Account is created.
- The relevant shareholding purchase order is created in the above steps and has not been executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Financial Transactions (F6157). | The Manage Financial Transactions screen is displayed. |  |
| 3 | Enter Data on Initial Screen | In the search term area, enter the following data and choose Go:Key Date: for example, TodayCompany Code: for example, 3310Transaction: the transaction number(s) | The shareholding purchase order transaction is displayed. |  |
| 4 | Waiver the Shareholding Purchase Order | In the Transaction area, select the transaction and choose Order Expiry in the toolbar via button …. | The details of the shareholding purchase order transaction are displayed. |  |
| 5 | Waiver the Stock Purchase Order | On the initial screen, choose Save. | The status of shareholding purchase order transaction is changed to Order Expiration. |  |

##### Create Shareholding Purchase Transaction - Non-affiliated Company via Contract

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you purchase a shareholding and the purchased ratio is under 20%, you enter the purchase transaction information into the system.

Prerequisite

- The relevant Security ID is created.
- The relevant Security Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Securities Transaction: Entry Screen screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Securities Transaction: Entry Screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE1Transaction Type: 100Partner: for example, 33537001 | The Create Securities Transaction: Structure is displayed. |  |
| 4 | Enter Data on Tab Structure | On the Structure tab, enter the following data:Flow Type: for example, 0100 Purchase (transaction)In the Position area,Securities Account: for example, AE_SHGeneral Valuation Class: choose an appropriate General Valuation Class (GVC), for example, 63 Equity: Fair value th. P/LNote You can also choose General Valuation Class (GVC) 62: Equity: Fair value th. OCI. The selection of GVC 62/63 represents this shareholding would be designated as Financial InstrumentsPosition Value Date: for example, <the current date>Calculation Date: for example, <the current date>Payment Date: for example, <the current date>In the Amounts area,Number of Units: for example, 10000Price (Unit Quoted): for example, 100 | All data is entered.Note You can select the below flow types as desired:0100 Purchase (transaction), means shareholding is purchased by cash.0105 Purchase (other consid-er.), means shareholding is purchased by other considerations (for example, fixed asset), you need to clear the balance of technical clearing account manually. |  |
| 5 | Enter Data on Tab Other Flows | On the Structure tab, you can record the transaction fee relevant information.Enter the following data:In the Other Flows area,Flow Type: for example, 0315 Brokerage not capitalized(tr.)Payment Amount: for example, 100Payment Currency: for example, AED |  |  |
| 6 | Save the Transaction | Choose Save.Note If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a dialog boxt is displayed asking you to create Position Indicator.If the Position Indicator is already created, then you can ignore below step. The following message is displayed: Security transaction XXXXX created in company code YYYY |  |  |
| 7 | Create Position Indicator | Choose Create Automatically. | The transaction is created. |  |

#### Create Shareholding Purchase Transaction - Associate or Joint Venture

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you purchase a shareholding and the purchased ratio is under 20%, you enter the purchase transaction information into the system.

Prerequisite

- The relevant Security ID is created.
- The relevant Security Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Create Securities Transaction (TS01). | The Create Security Transaction: Structure screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE2Transaction Type: 100Partner: for example, 33537001 | The Create Security Transaction: Initial screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the Structure tab, enter the following data:Flow Type: for example, 0100 Purchase (transaction)In the Position area,Securities Account: for example, AE_SHGeneral Valuation Class: choose an appropriate GeneralValuation Class (GVC), for example, 61 Equity: Equity MethodNote The selection of GVC 61 represents this shareholding would be measured by Equity Method under IFRS/US GAAP. But under DE GAAP, the accounting method is Moderate lower of cost or fair value.Position Value Date: for example, <the current date>Calculation Date: for example, <the current date>Payment Date: for example, <the current date>In the Amounts area,Number of Units: for example, 30000Price (Unit Quoted): for example, 100 | All data is entered. |  |
| 5 | Enter Data on Tab Other Flows | On the Structure tab, you can record the transaction fee relevant information.Enter the following data:In the Other Flows area,Flow Type: for example, 0315 Charge not capitalized (tran.)Payment Amount: for example, 100Payment Currency: for example, AED |  |  |
| 6 | Save the Transaction | Choose Save.Note If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a dialog boxt is displayed asking you to create Position Indicator.If the Position Indicator is already created, then you can ignore below step. The following message is displayed: Security transaction XXXXX created in company code YYYY |  |  |
| 7 | Create Position Indicator | Choose Create Automatically . | The transaction is created. |  |

#### Create Shareholding Purchase Transaction - Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you purchase a shareholding and the purchased ratio is more than 50%, you enter the purchase transaction information into the system.

Prerequisite

- The relevant Security ID is created.
- The relevant Security Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Create Securities Transaction (TS01). | The Create Security Transaction: Structure screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE3Transaction Type: 100Partner: for example, 33537001 | The Create Security Transaction: Initial screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the Structure tab, enter the following data:Flow Type: for example, 0100 Purchase (transaction)In the Position area,Securities Account: for example, AE_SHGeneral Valuation Class: choose an appropriate GeneralValuation Class (GVC), for example, 60 Equity: Cost MethodNote The selection of GVC 60 represents this shareholding would be measured by At Cost Method.Position Value Date: for example, <the current date>Calculation Date: for example, <the current date>Payment Date: for example, <the current date>In the Amounts area,Number of Units: for example, 60000Price (Unit Quoted): for example, 100 | All data is entered. |  |
| 5 | Enter Data on Tab Other Flows | On the Structure tab, you can record the transaction fee relevant information.Enter the following data:In the Other Flows area,Flow Type: for example, 0315 Charge not capitalized (tran.)Payment Amount: for example, 100Payment Currency: for example, AED |  |  |
| 6 | Save the Transaction | Choose Save.Note If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a dialog boxt is displayed asking you to create Position Indicator.If the Position Indicator is already created, then you can ignore below step. The following message is displayed: Security transaction XXXXX created in company code YYYY |  |  |
| 7 | Create Position Indicator | Choose Create Automatically . | The transaction is created. |  |

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

Once a securities transaction is recorded and saved, you need to settle it before you perform further activities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Securities Transactions - Collective Processing (TS00) | The Securities: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Securities: Collective Processing screen, enter the following data and choose Execute:In the General Selections area,Company Code: for example, 3310Transaction: the transaction number(s) | The list of transaction(s) is displayed on Securities: Collective Processing screen. |  |
| 4 | Settle the Transaction | Select the checkbox of a transaction on Securities: Collective Processing screen, and choose Settle.Note Please make sure to settle all the relevant transactions. | The Settle Security Contract: Structure screen displays. |  |
| 5 | Save the Change | On the Settle Security Contract: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If dialog Document lines: Display messages displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

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
| 7 | Match the Incoming Correspondence Object with the Outgoing Correspondence Objects for channel PRINT | Select the checkbox for the incoming correspondence object and choose Status Functions > Automatic Match . | The Automatic matching proposal view displays. |  |
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

### Payment for Purchase

Purpose

This section describes how to handle the payment for securities purchase transaction which are initiated by corporate via payment requests.

There are two options to process the payment for the purchase:

1. Process the payment with the ‘Auto. Payment Run’ function.
2. Process the payment without the ‘Auto. Payment Run’ function.

If the payment is initiated by the bank without using payment request, skip the current step, and continue with the step Post to General Ledger.

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
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Pay Only: <select this indicator>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
| 5 | Check the Log for Automatic Payment Run | On the log list screen, please choose the item Log for Automatic Payment Run.On the Log for Automatic Payment Runs screen, select one item of the payment log, choose Display Payment Run.Then, in the Automatic Payment Transactions for Payment Requests screen, choose Display payment log. | The payment document has been created.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX XXXXR has been processed. Batches are created for Collector XX/XX/XXXX XXXXXB.Please save a note for the Run date and ID in the output screen of Log for Automatic Payment Runs.A batch may need additional approvals before payment medium is finally created. For details, refer to test script (J78) Advanced Cash Operations.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>On the Payment Control area:Schedule Auto Payment Run: <select this indicator>Send for Approval: <select this indicator>Test Run: <select>Note If the No flows exist for processing message displays, then there is no payment required for the payment request according to your selection criteria and you can skip to Post to General Ledger procedure. | Screen Logs and Messages displays, you can check the payment information via the Payment Log.Note If scope item (J78) Advanced Cash Operations is not activated in your system, the checkbox Send for Approval will be uncheckable. |  |
| 4 | Production Run | Choose Back.On the Fix and Pay Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Logs and Messages displays, payment request has been generated. Check the Payment Log and make a note of the key number displayed on this screen.Note Please keep Test Run deselected, otherwise the autopayment run logs won’t be generated. |  |
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

In the case that the payment is initiated by the financial partner, skip the current step and the next step Process Payment Request, and continue with the step Post to General Ledger.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Procedure

Option 1: Generate Payment Request with Fix, Pay and Post Flows (TBB1) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>On the Payment Control area:Schedule Auto Payment Run: <deselect this indicator>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select>Pay Only: <select this indicator>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | Screen Payment Log - Test Run displays, you can check the payment information on this screen. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Run:Test Run: <deselect> | Screen Payment Log displays, payment request has been generated, make a note of the key number displayed on this screen. |  |

Option 2: Generate Payment Request with Fix and Pay Flows (TBB1_PAY) App

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Fix and Pay Flows (TBB1_PAY). | The Fix and Pay Flows view displays. |  |
| 3 | Test Run | On the Fix and Pay Flows view, enter the following data, and choose Run:Securities: <select>Company Code: for example, 3310Transaction: <transaction number with outflows which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select>Note If message No flows exist for processing displays, that means there is no payment with payment request are needed for your selection criteria, you can skip to step Post to General Ledger. | The Payment Log - Test Run view displays. Review the payment information on this view. |  |
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

You use the app Automatic Payment Transactions for Payment Requests (F111) to start the Payment Program for Payment Requests. The payment program for payment requests is an additional automatic payment option in the SAP system. Unlike the standard payment program, the payments are not based on open items (vendor/customer items) but on payment requests.

Prerequisite

Payment request has been generated in previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Automatic Payment Transactions for Payment Requests (F111). | The Automatic Payment Transactions for Payment Requests screen is displayed. |  |
| 3 | Enter Run Date and Identification | On the Automatic Payment Transactions for Payment Requests screen, enter the following data and choose Parameters:Run Date: for example, <Current date>Identification: for example, TRM01 | The Automatic Payment Transactions: Parameters screen is displayed. |  |
| 4 | Enter Parameters | On the Automatic Payment Transactions: Parameters screen, enter the following data:Posting Date: for example, <Current date>Next payment run on: for example, <Current date + 3 days>Company Code: for example, 3310Payment Methods: for example, TFChoose Dynamic selections, on the dialog box Free selection for payment run, enter the following data and choose Save:Key number: <the key number you noted down in previous step>Choose Additional Log, on the dialog box Additional Log, enter the following data and choose Continue:Payment method selection in all cases: <select this indicator>Line items of the payment documents: <select>Due date check: <select>If information Log created for all accounts displays, choose Continue.Choose Save on screen Automatic Payment Transactions: Parameters. | Message Parameters have been entered displays on the Automatic Payment Transactions for Payment Requests screen. |  |
| 5 | Schedule Proposal | Choose Proposal.On the dialog box Schedule Proposal, choose Start Immediat, and choose Schedule Job to confirm this dialog box.Message Proposal is running is displayed in the status bar with yellow traffic light.Choose Status, until message Payment proposal has been created appears in the status bar with green traffic light. | Payment proposal has been generated. |  |
| 6 | Schedule Payment | Choose Pmnt run.On the dialog box Schedule Payment, choose Start Immediat., and choose Create Payment Medium, then choose Schedule Job to confirm the dialog box.Message Payment run is running displays in the status bar with yellow traffic light.Choose Status, until message Payment run has been carried out appears with green traffic light. | The payment document has been created.If Bank Communication Management (BCM) is not implemented in your system, the payment medium will be created if it uses PMW format, you can check log by clicking Display payment log.If BCM is implemented in your system, in Display payment log, you can see message Payment run XX/XX/20XX TRM01R is intended for cross-payment run payment media, then a BCM batch is supposed to be created after payment run, please see next test step. |  |
| 7 | Cross-Payment Run Payment Media (Create BCM Batch) | On the Automatic Payment Transactions for Payment Requests screen, choose Menu > Environment > Payment medium > Cross-Payment Run Payment Medium > Create Payment Medium .On the Creation of Cross-Payment Run Payment Media screen, enter the following data and choose Execute:Run Date: for example, <Current date>Identification: for example, TRM01R | Dialog box Creation of Cross-Payment Run Payment Media appears, and states that Collector XX/XX/20XX XXXXXX was created or updated, that means, the BCM batch has been created.A batch may need additional approvals before payment medium is finally created. For details refer to test script Advanced Cash Operations (J78). |  |

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

With the posting functionalities, the posting related cash flows are transferred to the FI interface that generates the relevant postings in financial accounting. There are two apps for posting flows:

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
| 3 | Test Run | On the Treasury: Post Flows screen, enter the following data and choose Execute:Securities: <select this checkbox>Company Code: for example 3310Sec. Class ID Number: <The security class number>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | Screen Posting Log: Posted Business Transactions is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria, you can skip the current test step and continue the test step with the Process Business Transactions app. |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Execute:Test Run: <deselect this checkbox> | Screen Posting Log: Posted Business Transactions is displayed, and the accounting document has been created for incoming payment in local GAAP (valuation area AE0). |  |
| 5 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions screen is displayed. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Company code: for example, 3310Valuation Area: for example AE0Limit by Transaction Number: <select this checkbox>Transaction: <The Security ID you entered in previous step>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If message You have not selected any business transactions is displayed, that means there is no posting needed for your selection criteria, you can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.The Test Run: Display Posted/Reversed Business Transactions screen is displayed. Choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, you can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
| 9 | Production Run | On the Update Run: Post/Reverse Business Transactions screen, choose Select All and choose Choose Those to Post, and then choose Execute.The Update Run: Display Posted/Reversed Business Transactions screen is displayed, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed, and the accounting document has been created for outgoing payment in local GAAP (valuation area AE0). |  |

### Recognize Cash Dividend Income According to the Profit Distribution Plan

#### Enter Condition Items in Security ID

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

It is a common practice for corporates to declare profit distribution plan on a yearly basis. The cash dividend is the main approach for corporates to share retained earnings with shareholders. A distribution plan usually includes the following information: record date, ex-dividend date, and terms of distribution, for example, every 10 shares eligible for 0.5 EUR cash dividend.

In this step, you maintain the cash dividend after the profit distribution plan is declared and cash dividend process is triggered.

Prerequisite

You've created a security class ID.

Procedure

Please repeat this step for security class SH_AE2.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Manage Security Classes (F8717). | The Manage Security Classes screen is displayed. |  |
| 3 | Enter ID Number | Enter an ID Number, and choose Go.Securities Class: for example, SH_AE1Choose Details to display the Security class. | The Display Security Class screen is displayed with previously specified ID Number. |  |
| 4 | Create New Conditions Items | Choose Edit and switch to the Conditions tab, and choose Create to create new condition Item.Choose the condition type for cash dividend in the New Object screen.Condition Type: for example, 122 Cash Dividend - SHDEff. From: for example, <the current date>Choose in the condition details screen, enter the following data and choose Apply.Calculate Date: for example, <the current date + 5 days>Due Date: for example, <the current date + 1 month>Amount: for example, 0,5000000000Note Due Date is the ex-dividend date.The Amount means the cash dividend amount per unit according to the profit distribution plan. | Generated the condition item for cash dividend. |  |

#### Post the Cash Dividend Income - Non-affiliated Company/Subsidiary

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post cash dividend income based on the cash dividend information maintained in the Security Class, after you receive the cash dividend on the ex-dividend date.

Prerequisite

You've created condition items of cash dividend in the Security Class in the previous step.

Currency exchange spot rates have been maintained if you receive the cash dividend of foreign currency.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Execute Debit Position - Manual Debit Position (FWZE). | The Manual Debit Position: Initial Screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE1Security Account: for example, AE_SH | A list of positions is displayed. |  |
| 4 | Select a Flow and Proceed | On the list of positions displayed on the Manual Debit Position: Initial screen, select the top flow that you would like to capitalize and choose Post Business Transaction: | The Manual Debit Position screen is displayed. |  |
| 5 | Enter Details for the Capitalization | On the Manual Debit Position screen, confirm the following information of cash dividend income and choose Post:Payment amount of cash dividendCapital Gains Tax amount derived by the cash dividend amountSolidarity Surcharge amount derived by the Capital Gains Tax amountNet Payment AmountFI Posting DateNote You can choose Capitalize if you need to reinvest the cash dividend.The tax amount was derived by the predefined tax rate in configuration activity Define Derivation Rules for Tax Flows.You can change the tax amount manually.Also, you can add other flows manually if needed.. | The dividend flows to be posted or capitalized are maintaind. |  |
| 6 | Post | Confirm the data and choose Post. | The Posting Log: Posted Business Transaction screen is displayed. |  |

#### Post the Cash Dividend - Associate or Joint Venture

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post cash dividend income under equity method after you receive the cash dividend on the ex-dividend date.

Prerequisite

Currency exchange spot rates have been maintained if you receive the cash dividend of foreign currency.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Manual Posting (FWBS). | The Manual Posting: Initial Screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE2Security Account: for example, AE_SH | A list of positions is displayed. |  |
| 4 | Enter Details for Cash Dividend | On the Manual Posting screen, enter the following data of cash dividend income:Interest Value Date: for example, <the current date + 1 month>Due Date: for example, <the current date + 1 month>Value Date: for example, <the current date + 1 month>Position Value Date: for example, <the current date + 1 month>Value Date: for example, <the current date + 1 month>FI Posting Date: for example, <the current date + 1 month>Choose Insert Other Flow in the Flows area, insert flows as following data:Line 1:In the Manual Posting: Process Flow screen, select following data and choose Copy:Update Type: for example, SAM8131Payment Amount: for example, 50000Line 2:In the Manual Posting: Process Flow screen, select following data and choose Copy:Update Type: for example, SAM8110, Cash Dividend: Receive payment (All VAs)Payment Amount: for example, 50000Note The update type in Line 2 is posted for cash side. | The dividend flows to be posted or capitalized are maintaind. |  |
| 5 | Post | Confirm the data and choose Post. | The Posting Log: Posted Business Transaction screen is displayed. |  |

### Corporate Actions for Specific Business Scenario

Purpose

The following business scenarios can be processed by Corporate Action:

- Stock split
- Receive stock dividend
- Stock swap
- Capital reduction
- Issue currency change over
- Transfer new stock to old stock
- Transaction currency change over

#### Shareholding Split

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create the corporate action to update the shareholding units according to the shareholding split declaration.

Prerequisite

You’ve created the Security Class.

Procedure

1. Create a Corporate Action

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Manage Corporate Actions (FWK0). | The Manage Corporate Action: Initial Screen view is displayed. |  |
| 3 | Enter corporate action data | On the Manage Corporate Action: Initial Screen view, enter the following data and choose Create:CA Cat.: for example, 01 Stock SplitCA Type: for example, 1 Stock split(std) | The Corporate Action is saved with a CA number displayed in the header. |  |
| 4 | Enter corporate action data for stock split | On the Create Corporate Action: Stock split screen, enter the following data and choose Activate:Key Date: for example, <the current date + 2 month>Description: for example, shareholding split testSecurity Class: for example, SH_AE1Split Ratio: for example, 1 / 2 |  |  |

2. Post the Corporate Action

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Post Corporate Actions (FWKB). | The Post Corporate Action screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Post Corporate Action screen, enter the following data and choose Execute:Corporate Action Number: for example, <the CA number you have created in the previous step>Company Code: for example, 3310Test Run: <select this checkbox> | The Post Corporate Action screen is displayed.The Status of the corporate action is changed to Simulate Success.If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Cash Flow. New flows have been generated according to the corporate action. Please note there is no posting created because it is test run. |  |
| 4 | Enter Selection Criteria for Production Run | Choose Back until the Post Corporate Action screen is displayed.On the Post Corporate Action screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Post Corporate Action screen is displayed.The status of the Corporate Action is changed to Post Success.You can check the posting information for local GAAP (valuation area AE0) by choosing Cash Flow. New flows have been generated according to the corporate action.Note The value of the shareholding will keep unchanged in this step. Only the shareholding units is updated. |  |

### Period-end Closing

Purpose

In this section, you perform the period-end closing activities. For shareholding of different ratio under different accounting principles, you need to perfom different steps under this section.

For shareholding of a non-affiliated company, you need to perform the Update Securities Price and Perform Key Date Valuation steps.

For shareholding of an associate or joint venture company, different accounting methods may be used in different valuation areas. For example, a shareholding investment with 30% holding ratio is measured by equity method under IFRS/US GAAP, but by Moderate lower of cost or fair value method under HGB. Therefore you need to run the Equity Pickup - Associate or Joint Venture step for shareholding measured by equity method, but run the Update Securities Price and Perform Key Date Valuation steps for shareholding measured by Moderate lower of cost or fair value.

#### Update Securities Price - Non-affiliated Company

Purpose

By entering the latest price of a stock into SAP system as securities price, the system can recognize its latest position value and perform the relevant journal posting when running key date valuation.

Procedure

Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload(1XN) for detailed procedures.

#### Perform Key Date Valuation - Non-affiliated Company

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you evaluate the positions of the stock transaction based on the latest price and foreign currency exchange rate where applicable.

|  |
| --- |
| Note You can also schedule a background job for this step. Please see the corresponding step in the Appendix section. |

Prerequisite

You have entered the spot price for the security class in the Update Securities Price section.

You have performed the following sections of this test script:

- Set Settlement Status
- Payment to Depository Bank
- Post the cash dividend if any during this period
- Post the corporate action if any during this period
- Maintained exchange rate in the valuation date if you have position measured by foreign currency

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Run Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run Valuation screen, enter the following data and choose Execute:In the Product Groups area,Securities: <select this checkbox>In the General Selections area,Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example, 16AIn the Securities area,Sec. Class ID Number: for example, SH_AE1Security Account: for example, AE_SHIn the Valuation Parameters area,Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation with ResetNote When the period end is also the year end, the Valuation Category Year End Valuation should be used.Test Run: <select this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation.If dialog box Message shows up, choose Continue. | The screen Valuation Log is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Please note there is no posting created because it is test run.Note Sometime there is no simulated posting because your selected security class position in security account may not need valuation. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the Run Valuation screen is displayed.On the Run Valuation screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation. | The Valuation Log screen is displayed, you can check the posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Then, the accounting document has been created in local GAAP (valuation area AE0). |  |

#### Equity Pickup - Associate or Joint Venture

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you do the equity pickup based on the latest financial information from the associate or joint venture companies.

You need to calculate the data of equity pickup manually and enter the data by Create Manual Posting (FWBS).

Prerequisite

You have performed the following sections of this test script:

- Set Settlement Status
- Payment to Depository Bank
- Post the cash dividend if any during this period
- Post the corporate action if any during this period
- Maintained exchange rate in the valuation date if you have position measured by foreign currency

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Manual Posting (FWBS). | The Manual Debit Position: Initial Screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Debit Position: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE2Security Account: for example, AE_SH | A list of positions is displayed. |  |
| 4 | Enter Details for Cash Dividend | On the Manual Posting screen, enter the following data of cash dividend income:Interest Value Date: for example, 3310Due Date: for example, <the current date + 2 month>Value Date: for example, <the current date + 2 month>Position Value Date: for example, <the current date + 2 month>Value Date: for example, <the current date + 2 month>FI Posting Date: for example, <the current date + 2 month>Choose Insert Other Flow in the Flows area, insert flows as following data:Line 1:In the Manual Posting: Process Flow screen, select following data and choose Copy:Update Type: for example, SAM9011, Equity Method: Income increase (local VA)Payment Amount: for example, 100000 | The dividend flows to be posted or capitalized are maintaind. |  |
| 5 | Post | Confirm the data and choose Post. | The Posting Log: Posted Business Transaction screen is displayed. |  |

### Sell Shareholdings

#### Review Shareholding Position

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you review the position of the security class in the security account before selling.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Securities Account Class Positions (TPM40A). | The Display Securities Account Class Position List screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Securities Account Class Position List screen, enter the following data and choose Execute:Company Code: for example, 3310Sec. Class ID Number: for example, SH_AE1; SH_AE2; SH_AE3Securities Account: for example, AE_SH | The Display Securities Account Class Position List is displayed according to the filter values. |  |

#### Create Shareholding Sale Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you sell the whole or a portion of the Shareholding, you need to enter the deal information into the system to update the securities position. In this step, you update the position sold. The sale transaction should take place after the cash dividends are recorded in the system.

|  |
| --- |
| Note The securities position on hand must be greater than or equal to the position to be sold. |

Procedure

1. Non-affiliated Company

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE1Transaction Type: 200Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:In the Position area,Securities Account: for example, AE_SHGeneral Valuation Class: <use the same General Valuation Class as purchase transaction for this security class ID>Position Value Date: for example, <the current date + 3 months>Calculation Date: for example, <the current date + 3 months>Payment Date: for example, <the current date + 3 months>In the Amount area,Number of Units: for example, 1,000Price (Unit Quoted): for example, 110 | All data are entered. |  |
| 5 | Save the Transaction | Choose Save. | The data is saved |  |

2. Associate or Joint Venture

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE3Transaction Type: 200Partner: for example, 33537001 | The Create Security Transaction: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:In the Position area,Securities Account: for example, AE_SHGeneral Valuation Class: <use the same General Valuation Class as purchase transaction for this security class ID>Position Value Date: for example, <the current date + 3 months>Calculation Date: for example, <the current date + 3 months>Payment Date: for example, <the current date + 3 months>In the Amount area,Number of Units: for example, 1,000Price (Unit Quoted): for example, 110 | All data are entered. |  |
| 5 | Save the Transaction | Choose Save. | The data is saved. |  |

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

If the outgoing payment is initiated by a bank, it is not necessary to create and process payment requests, because the outgoing payment is initiated by the bank.

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

- Fix, Pay and Post Flows (TBB1): Use this app to generate the posting for incoming payment. Note that it will not create postings for outgoing payment with the Pay Only option.
- Process Business Transactions (TPM10): Use this app to generate the posting for the outgoing payment with the Pay Only option.

|  |
| --- |
| Note You can also a schedule background job for this step. Please see the corresponding step in the Appendix. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Fix, Pay and Post Flows (TBB1). | The Fix, Pay and Post Flows screen is displayed. |  |
| 3 | Test Run | On the Fix, Pay and Post Flows view, enter the following data, and choose Execute:Securities: <select this checkbox>Company Code: for example 3310Transaction: <transaction number with inflow which was created in previous steps>Up to and Including Due Date: enter date on which the flow of financial transaction should be posted, for example, <current date>Test Run: <select this checkbox>Post Operational Only: <select this indicator> | The Posting Log: Posted Business Transactions screen is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is test run.If message No flows exist for processing is displayed, that means there is no posting needed for your selection criteria. You can skip current test step and continue with app Process Business Transactions (TPM10). |  |
| 4 | Production Run | Choose Back.On the Fix, Pay and Post Flows view, change the following data, and choose Execute:Test Run: <deselect this checkbox> | Process Business Transactions |  |
| 5 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions screen displays. |  |
| 6 | Enter Selection Criteria for Test Run | On the Process Business Transactions screen, enter the following data and choose Execute:Securities: <select this checkbox>Company Code: for example, 3310Valuation Area: for example AE0Limit by Transaction Number: <select this checkbox>Transaction: <transaction number with outflow, and its payment request has been generated in step Generate Payment Request>Test Run: <select this checkbox> | The Test Run: Post/Reverse Business Transactions screen is displayed.If the You have not selected any business transactions message is displayed, that means there is no posting needed for your selection criteria. You can skip current step. |  |
| 7 | Check Test Run Result | On the screen Test Run: Post/Reverse Business Transactions, choose Select All and choose Choose Those to Post, and then choose Execute.The Test Run: Display Posted/Reversed Business Transactions screen is displayed, choose Log and Messages. | The Posting Log: Posted Business Transactions screen is displayed. You can check the simulated posting information for local GAAP (valuation area AE0) on this screen. Please note there is no posting created because it is a test run. |  |
| 8 | Enter Selection Criteria for Production Run | Choose Back.On the Process Business Transactions screen, change the following data and choose Execute:Test Run: <unselect this checkbox> | The Update Run: Post/Reverse Business Transactions screen is displayed. |  |
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

In this step, you check the posting journals.

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

In this step, you check the treasury position analysis view.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Treasury Position Analysis. | The Treasury Position Analysis screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, Current DateInclude Planned Data: for example, 1Valuation Area: for example, AE0Company Code: for example, 3310Product Type: for example, 16A | The position analysis data displays per the filter values. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Display Treasury Position Values (F1867). | The Display Treasury Position Values screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select GoKey Date: for example, <the current date>Product Group: for example, SecuritiesNote You may need to adapt the filters to make the OpenProduct Group filter display.Company Code: for example, 3310Valuation Area: for example, AE0 | The position values data displays per the filter values. |  |

#### Define Financial Positions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define a set of key figures to be displayed in the Financial Status - Book Value and Financial Status - Nominal Amount apps.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Define Financial Positions (FTR_FP_DEF). | The "Maintain Financial Position Groups": Change screen is displayed. |  |
| 3 | Maintain Key Figure Groups | Choose New Entries.Enter the data below and choose Save.Financial Position Group: for example, FPG_A0001Financial Position Group Description: for example, Bank accounts and Short term investAssets/Liabilities: for example, Assets | The data is saved.Note if FPG_A0001 is already created for the same purpose, you can skip this step and use the existing record. |  |
| 4 | Maintain Key Figures | In the Dialog Structure area, double-click on the Maintain Financial Positions folder, and choose New Entries.Enter data and choose Save.Financial Position: for example, FP_A1001Financial Position Description: for example, Shareholding AccountFinancial Position Group: for example, FPG_A0001Data Source: for example, One Document Balances | The New Entries: Overview of Added Entries screen is displayed to allow you to enter and save the Key Figures. |  |
| 5 | Maintain Selections | Select one financial position and select Maintain Selections.G/L Account: for example, 19999000Chart of Accounts: for example, YCOALedger: for example, 0LChoose Back and choose Save. | The data is saved. |  |
| 6 | Enter More Data | Enter more financial positions data as below tables. |  |  |

| Financial Position Group | Financial Position Group Description | Assets/Liabilities |
| --- | --- | --- |
| FPG_A0001 | Bank accounts and Short term invest. | Assets |
| FPG_A0002 | Long term invest. and other assets | Assets |
| FPG_L0001 | Short term debt | Liabilities |
| FPG_L0002 | Long term debt and other liabilities | Liabilities |

| Financial Position | Financial Position Description | Financial Position Group | Data Source | Maintain Selection |
| --- | --- | --- | --- | --- |
| FP_A0001 | Bank accounts | FPG_A0001 | One exposure | House bank |
| FP_A0002 | Short term investments | FPG_A0001 | Treasury position management | Product Type = 16ATransaction Type = 100 to 199Valuation Class = 62 to 63Valuation Area = AE0Posting Status = 2 |
| FP_A0003 | Long term investments | FPG_A0002 | Treasury position management | Product Type = 16ATransaction Type = 100 to 199Valuation Class = 60 to 61Valuation Area = AE0Posting Status = 2 |
| FP_A0004 | Other assets | FPG_A0002 | One document balances | Account Number = 12041000 to 1204199912042000 to 1204299912701000 to 12701999Chart of Account = YCOALedger = 0L |
| FP_L0003 | Other liabilities | FPG_L0002 | One document balances | Account Number = 22541000 to 2254199922542000 to 22542999Chart of Account = YCOALedger = 0L |

#### Financial Status - Book Value

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

Financial positions are already defined.

Refer to Define Financial Position for more details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Financial Status (F2136). | The Financial Status - Book Value screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and select Go.Key Date: for example, <the current date>Reporting Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays per the filter values. |  |

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

You have already defined the financial positions. Please refer to the Define Financial Positions step to define financial positions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Risk Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Financial Status (FTR_FPM_FINANCIAL_STATUS (FTR_FPM_FS_NOMAMT)). | The Financial Status - Nominal Amount screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Go.Key Date: for example, <the current date>Reporting Currency: for example, AEDExchange Rate Type: for example, MCompany Code: for example, 3310 | The data displays per the filter values. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Payments (TPM20A). | The Payment Journal screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter selection criteria and choose Execute.Company Code: for example: 3310Product Type: 16A | The payment journals are displayed. |  |
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

In this step, you check the position flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows screen is displayed. |  |
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

In this step, you check treasury alerts for posting.

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

In this step, you check treasury alerts for various type of transactions.

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

In this step, you check the payment schedule for interest flows due.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Payment Schedules (TJ04). | The Treasury: Payment Schedule screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Payment Schedule screen, enter the following data and choose Execute:Securities: <select this checkbox>Company Code: for example, 3310End of Term in the Future: <select this checkbox>End of Term in Lapsed: <select this checkbox>Payment Period: for example, <the current date to the current date + 5 days>Payment Status: for example, 1Output Error Log: <select this checkbox> | You can check payment schedule report. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Display Securities Account Class Positions (TPM40A). | The Display Securities Account Class Position List screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Display Securities Account Class Position List screen, enter the following data and choose Execute:Company Code: for example, 3310Sec. Class ID Number: for example, SH_AE1Securities Account: for example, AE_SHPosition Value Date: for example, <the current date> | The position is displayed. |  |

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
| 4 | Enter Selection Criteria of Characteristics | Choose the Characteristics tap, enter the following data then choose Execute:Company Code: for example, 3310Product Type: for example, 16A | The NPV Result displays based on Portfolio Hierarchy. |  |

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

You have maintained the limit master records of your company, and processed the Generate Limit Utilizations step.

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
| 3 | Enter Parameters | On the Display Position Indicator screen, enter following data and press Enter:Product Group: select SecuritiesCompany Code: for example, 3310ID Number: for example, SH_AE1Securities Account: for example, AE_SH | The Securities Account Position Indicator and Subledger Position Indicator sections are displayed.Note If you want to change position indicators, go back to the opening screen, input the position indicator information, and choose More > Position Indicator > Change . |  |

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

If security exists, the spot price needs to be maintained for current date. Refer to the Update Securities Price section of the Market Rates Management – Manually via Upload (1XN) for detailed procedures.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs view, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the Template Selection area, enter the following data, and choose Step 2:Job Template: Fix, Pay and Post FlowsJob Name: for example, <Generate Payment Request> | You've chosen the template and are navigated to the Scheduling Options area. |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and in the Scheduling Information dialog box, enter the following data:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time default>Time Zone: <select a time zone or use default>Recurrence Pattern: for example, DailyEvery: for example, 1Day(s)End: for example, select After and then enter 7 occurrence(s)On Non-Working Days: for example No RestrictionChoose OK, and choose Step 3.Note If you would rather to start job at once, select Start Immediately checkbox. | You've defined the recurrence pattern and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area,In the Application sub-area, select one or more proper product groupIn the General Selection sub-area, enter the following data:Company Code: for example, 3310Transaction: <enter transaction numbers if you'd like to limit transactions>Product Type: <enter product types if you'd like to limit product types>Due Date Period: for example, 0On the Payment Control area:Schedule Auto. Payment Run: <select this indicator>Send for Approval: <select this indicator>In the Posting Control sub-area,Test Run: <deselect>Pay Only: <choose this radio button>Note You can also choose the Post All Valuation Areas radio button, if you want to post to all valuation areas. | Note If scope item (J78) Advanced Cash Operations is not activated in your system, the check box Send for Approval will be uncheckable. |  |
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
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information dialog box :Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After 7 Occurrence(s)On Non-Working Day:for example, Run on next Working DayChoose OK, and choose Step 3.Note If you would like to start job at once, select the Start Immediately checkbox.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
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
| 2 | Access the SAP Fiori app | Open Schedule Treasury Accountant Jobs (F2770). | The Application Jobs screen is displayed. |  |
| 3 | Create New Job | On the Application Jobs view, choose Create. | The Template Selection area is displayed. |  |
| 4 | Enter General Information | In the General Information area, enter the following data, and choose Step 2:Job Template: Process Business TransactionsJob Name: for example, Process Business Transactions |  |  |
| 5 | Enter Scheduling Options | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box :Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After 7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately.Remember Schedule this job after the back office job for generating payment request by using the same job template. |  |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:In the Product Groups sub-area, select one or more product groups.Company Code: for example, 3310Valuation Area: for example, AE0, or leave it blank (run for all valuation areas)In the Limit by Transaction Number sub-area, make the following selection:Limit by Transaction Number: <deselect this checkbox>In the Limit by Subledger Positions sub-area, make the following selection:Limit by Subledger Pos.: <select this checkbox>Product Type: <enter product types if you'd like to limit product types>Transaction: <enter transaction numbers if you'd like to limit transactions>Trans. to Be Fixed/Posted: <select this checkbox>In the Posting Control sub-area, make the following selection:Test Run: <deselect this checkbox> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Review Results | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details view displays. |  |

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
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After 7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately. | You've defined the recurrence pattern and are navigated to the Parameters area. |  |
| 6 | Enter Parameters | In the Parameters area, enter the following data:Company Code: for example, 3310Product Type: for example, 16A |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

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
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, choose Define Recurrence Pattern, and enter the following data in the Scheduling Information the dialog box:Start Immediately: <deselect this checkbox>Job Start: for example, <current date and time 11:00>Time zone: <choose a time zone>Recurrence Pattern: for example, DailyEvery: for example, 1 Day(s)End: for example, After 7 Occurrence(s)On Non-Working Day: for example, Run on next Working DayChoose OK and choose Step 3.Note If you would like to start job at once, select checkbox Start Immediately. | The Parameters area is displayed. |  |
| 6 | Enter Parameters for New Job | n the Parameters area, enter the following data:In the General Selection sub-area,Company Code: for example, 3310Product Type: for example, 16ASecurity Account: for example, AE_SHSec. Class ID Number: for example, SH_AE1Update Type: for example, SAM5020In the Debit Position Parameter sub-area,Up to an Including Pos. Date: for example, <end date of current month>In the Posting Control sub-area,Document Date: for example, <end date of current month> |  |  |
| 7 | Schedule New Job | Choose Schedule. | You are automatically navigated back to the initial screen of this app. The job you just scheduled is displayed in the result area. |  |
| 8 | Check Result | Choose the  on the right side of the job to review the job details.Note You may need to refresh the screen to see the latest status of the job. | The Job Details screen is displayed. |  |

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
| 3 | Enter Selection Criteria for Test Run | On the Manual Posting / Debit Position: Reverse screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class: for example, SH_AE1Securities Account: for example, AE_SH | A list of fixed debit positions is displayed. |  |
| 4 | Reverse Debit Position | On the Manual Posting / Debit Position: Reverse screen, select a record to reverse and choose Reverse business transaction: | The Reverse Business Transaction screen is displayed. |  |
| 5 | Process the Reversal | On the Reverse Business Transaction screen, enter the following data and choose Reverse:Reason for Reversal: for example, Process. errorFI Reversal Date: for example, <original posted date> |  |  |

#### Reverse Corporate Action

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you need to reverse the debit position after posting, you can use the app Reverse Posting of Corporate Actions (FWKS).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Reverse Posting of Corporate Actions (FWKS). | The Reverse Corporate Action screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Reverse Corporate Action screen, enter the following data and choose Enter:Corporate Action Number:: for example, <the CA number you have posted in the previous step>Company Code: for example, 3310TR Reversal Reason: for example, 01 Process. ErrorTest Run: <select this checkbox> | A list of posted corporate actions is displayed.If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error. |  |
| 4 | Enter Selection Criteria for Production Run | On the Reverse Corporate Action Test Run screen, review the reverse test run result and choose Back until the Reverse Corporate Action screen is displayed.On the Reverse Corporate Action screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Reverse Business Transaction screen is displayed. |  |
| 5 | Check the Reverse Result | On the Reverse Corporate Action screen, review the reverse production run result. | The reverse post succussed. |  |

#### Manual Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

If you need to add some tax flow, for example Capital Gains Tax, to the security Class ID, you can use the app Create Manual Posting (FWBS).

Prerequisite

You've created a security class.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Manual Posting (FWBS). | The Manual Posting: Initial screen is displayed. |  |
| 3 | Enter Selection Criteria for Manual Posting | On the Manual Posting: Initial Screen, screen, enter the following data and choose Enter:Security ID: for example, SH_AE1Securities Account: for example, AE_SH | A list of fixed debit positions is displayed. |  |
| 4 | Enter Detailed Information of the New Flows for Manual Posting | On the Manual Posting screen, choose Insert Other Flow, enter the following data and choose Copy:Update Type: for example, TAX0006 Capital Gains TaxPayment Amount: for example, 10000 | The Manual Posting: Process screen is displayed. |  |
| 5 | Post | Confirm the data and choose Post | The Posting Log: Posted Business Transaction screen is displayed. |  |

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

The objective of this step is to create market data shifts to be able to analyze key figures with modified market data. It will be used in the [Defining Report Layout for Calculate Market Risk Key Figures](#unique_109) [page ] 132 step.

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
| 6 | Maintain Key Figures of Layout | On the Change View "Key Figures": Overview screen, choose New Entries and then insert the following data in the Key Figures form:ROW 1Key Figure Name: for example, BARWERTPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDec.Places: for example, 0ROW 2Key Figure Name: for example, CRFNPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, RISK_FREE_NPVShort Name: for example, Current Risk Free NPVShift Rule: for example, 0Dec.Places: for example, 0and Save. | The New Entries: Overview of Added Entries screen displays allowing entry of the Key Figures name and configuration settings. |  |
| 7 | Access Key Figures Maintain screen | Go back to the Change View "Key Figure Layout": Overview screen, select the checkbox of Layout-ID Y02, then double click on the Key Figures folder in the Dialog Structure panel. |  |  |
| 8 | Maintain Key Figures of Layout | On the Change View "Key Figure Layout": Overview screen, Choose New Entries, then insert the following data in Key Figures form and Save:Key Figure Name: for example, NPVPos. Area: for example, <select this checkbox>PH-Area: for example, <select this checkbox>Key Figure Category: for example, NPVShort Name: for example, NPVShift Rule: for example, 1 or Market Data Shift Rule you createdDecimal Places: for example, 0 |  |  |

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

Prerequisite

You have created a stock transaction.

NPV values need to be stored in advance of the valuation of Treasury positions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Simulate Period-End Closing (TPM_SIM_VAL). | The Simulate Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Simulate Period-End Closing screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: for example, AE0Product Type: for example,16ASecurity ID: for example, <Security Class ID Number(s) created in previous steps>, for example, SH_AE1Security Account: for example, AE_SHRecalculate Outdated Sim.Val.: <deselect this checkbox>Note If you set this indicator, you can recalculate the outdated simulation results.Simulation Date: for example, <the current date>Key Date Valuation: <select this checkbox>Accrual/Deferral: <deselect this checkbox>Note If you set this indicator, the accrual/deferral of expenses and revenues for the selected treasury positions is simulated, and Accrual/Deferral Parameter is displayed.Test Run: <select this checkbox> | The following message is displayed:Processed xx positions; xx successful, 0 failed.If Recalculate Outdated Simulation Results has been executed, the following message is displayed:xx simulated results deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
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
| 3 | Enter Selection Criteria for Test Run | On the Delete Results of Simulated Period-End Closing screen, enter the following data and choose Execute:Securities: <select this checkbox>OTC Transactions: <deselect this checkbox>Company Code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example, AE0Product Type: for example,16ASec. Class ID Number: for example, for example, SH_AE1Security Account: for example, <Securities account(s) for which valuation has been executed, for example, AE_SH>Simulation Date: for example, <the date on which the reversal should takes place>Test Run: <select this checkbox> | The following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |
| 4 | Enter Selection Criteria for Production Run | Go back to the initial screen of this app.On the Delete Results of Simulated Period-End Closing screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The following message is displayed:simulated results deleted for key date (the date on which the reversal takes place). |  |

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

Transfer the shareholding position to the new security account.

Prerequisite

You have purchased a Shareholding transaction.

A new security account has created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Securities Account Transfer (FWDU). | The Securities Account Transfer: Initial screen is displayed. |  |
| 3 | Enter Selection Criteria for Securities Account Transfer | On the Securities Account Transfer: Initial screen, enter the following data and choose Execute:Company Code: for example, 3310Security ID: for example, for example, SH_AE1Source Sec. Account: for example, for example, AE_SHPos. Value Date: for example, <the current date> | The Securities Account Transfer: Edit screen is displayed. |  |
| 4 | Enter Detailed Data for Securities Account Transfer | On the Securities Account Transfer: Edit screen, enter the following data and choose Save:Target Sec.Acct: for example, AE_SH2Nominal Amount: for example, 100000Pos. Value Date: for example, <the cur-rent date>Calc. Date: for example, <the current date>Document Date: for example, <the current date> | The screen Information Overview is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the posting information by choosing Logs + Messages. |  |
| 5 | Review logs | Choose Messages and Log.On Information Overview dialog box, choose Posting Log.On Posting Log: Posted Business Transactions view, you review the postings. | Logs are reviewed. |  |

### Transfer Valuation Class

If the position of shareholding is increased or decreased, the change in the holding ratio could lead to the accounting method change in some cases. Then, you need to transfer the accounting balance and post the relevant adjustments. The process transfer valuation class is to deal with this situation.

There are six possible scenarios of valuation class transfer according to the holding ratio change:

1. non-affiliated company transfer to associate or joint venture
2. non-affiliated company transfer to subsidiary
3. associate or joint venture transfer to non-affiliated company
4. associate or joint venture transfer to subsidiary
5. subsidiary transfer to non-affiliated company
6. subsidiary transfer to joint venture to subsidiary

Here we take the example of transfer from non-affiliate company to associate or joint venture.

#### Evaluated the Fair Value of Original Position at Transfer Date

##### Perform Key Date Valuation by Manual Posting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you evaluate the fair value of the shareholdings at transfer date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Manual Posting (FWBS). | The Manual Debit Position: Initial Screen screen is displayed. |  |
| 3 | Enter Parameters | On the Manual Posting: Initial Screen screen, enter the following data and choose Enter:Company Code: for example, 3310Security Class ID: for example, SH_AE1Security Account: for example, AE_SH | A list of positions is displayed. |  |
| 4 | Enter Details for Cash dividend | On the Manual Posting screen, enter the following data of cash dividend income:Interest Value Date: for example, 1010Due Date: for example, <the current date>Value Date: for example, <the current date>Position Value Date: for example, <the current date>Value Date: for example, <the current date>FI Posting Date: for example, <the current date>Choose the button Insert other flow in the Flows area, insert flows as following data:Line 1:In the Manual Posting: Process Flow screen, select following data and choose Copy:Update Type: for example, SAM9210, Revaluate at fair value, realized gains (All VAs)Payment Amount: for example, 50000 | The screen Valuation Log is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Please note there is no posting created because it is test run.Note Sometime there is no simulated posting because your selected security class position in security account may not need valuation. |  |
| 5 | Post | Confirm the data and choose Post. | The Display Selected Treasury Positions for Valuation screen is displayed. |  |

#### Reclassify the Shareholding Position and Adjust Relevant Postings

##### Create Shareholding Purchase Transaction - Associate or Joint venture

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you purchase a shareholding and the total holding ratio is between 20% to 50%, you enter the purchase transaction information into the system.

Prerequisite

- The relevant Security ID is created.
- The relevant Security Account is created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Create Securities Transaction (TS01). | The Create Security Transaction: Structure screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Create Security Transaction: Initial screen, enter the following data and choose Execute:Company Code: for example, 3310Security Class ID: for example, for example, SH_AE1Transaction Type: 100Partner: for example, 33537001 | The Create Investment Fund: Structure screen is displayed. |  |
| 4 | Enter Data on Tab Structure | On the Structure tab, enter the following data:Flow Type: for example, 0100 Purchase (transaction)In the Position area,Securities Account: for example, AE_SHGeneral Valuation Class: choose an appropriate General Valuation Class (GVC), for example, 61 Equity: Equity MethodThe selection of GVC 61 represents this shareholding would be measured by Equity MethodPosition Value Date: for example, <the current date>Calculation Date: for example, <the current date>Payment Date: for example, <the current date>In the Amounts area,Number of Units: for example, 10000Price (Unit Quoted): for example, 100 | All data is entered. |  |
| 5 | Enter Data on Tab Other Flows | On the Structure tab, you can record the transaction fee relevant information.Enter the following data:In the Other Flows area,Flow Type: for example, 0315 Charge not capitalized (tran.)Payment Amount: for example, 100Payment Currency: for example, AED |  |  |
| 6 | Save the Transaction | Choose Save.If this transaction is the first transaction for the combination of Securities Account and Securities ID, then a dialog boxt is displayed asking you to create Position Indicator.If the Position Indicator is already created, then you can ignore below step. The following message is displayed: Security transaction XXXXX created in company code YYYY |  |  |
| 7 | Create Position Indicator | Choose Create Automatically. | The transaction is created. |  |

##### Set Settlement Status

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a securities transaction is recorded and saved in SAP, the transaction must be settled before you perform further activities. This section describes how to set the set-tlement status.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Securities Transactions - Collective Processing (TS00) | The Securities: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Securities: Collective Processing screen, enter the following data and choose Execute:In the General Selections area,Company Code: for example, 3310Transaction: the transaction number(s) | The list of transaction(s) is displayed on Securities: Collective Processing screen. |  |
| 4 | Settle the Transaction | Select the checkbox of a transaction on Securities: Collective Processing screen, and choose Settle.Note Please make sure to settle all the relevant transactions. | The Settle Security Contract: Structure screen displays. |  |
| 5 | Save the Change | On the Settle Security Contract: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If dialog Document lines: Display messages displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

##### Payment for Purchase

Purpose

In this step, you maintain the payment for the purchase transaction.

Procedure

You may refer to the Payment for Purchase section.

##### Change the Reporting Data in Company Code in Business Partner

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you update the company relationship in Business Partner after the holding ratio is changed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Master Data Specialist - Business Partner Data. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Maintain Business Partner (BP) | The Maintain Business Partner: screen is displayed. |  |
| 3 | Switch to change mode | On the Maintain Business Partner: screen, choose Open BP, in the Open business partner dialog box, enter following data:Business Partner: 33537006Choose Enter and then choose Switch Between Display and Change, and enter following data:Change in BP Role: choose TR0150 Issuer | Change Organization: 33537006 , role Counterparty screen displays. |  |
| 4 | Enter Reporting Data in Company Code | On the Change Organization:33537006, role Counterparty screen, choose Company Code, choose Reporting Data in Company Code, and enter following data and choose Save.Comp. Rel.: for example, 2 ShareholdingIf you couldn't find Reporting Data in Company Code on the screen, then you can choose Navigation Menu and choose it from the dropdown menu.Comp.Rel. reflects your relationship to the counterparty:1 affiliated and consolidated2 affiliated but not consolidated3 OtherIt can be used to derive the correct G/L accounts. | The Reporting data is entered and saved. |  |

##### Transfer the Current Position of the Shareholding to the New Valuation Class

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After you purchase a shareholding and the purchased ratio is between 20% to 50%, you transfer the current position to the new valuation class: associate or joint venture.

Prerequisite

The relationship to the issuer is updated in business paterner.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Execute Valuation Class Transfer (TPM15M). | The Securities Account Transfer: Initial screen is displayed. |  |
| 3 | Enter Data on Initial Screen | On the Valuation Class Transfer screen screen, enter the following data and choose Execute:Company Code: for example, 3310Security ID: for example, for example, SH_AE1Source Sec. Account: for example, for example, AE_SHIn the Specific Selections for Outgoing Position area,Choose General Valuation Class.General Valuation Class: for example, 63 Equi-ty: Fair value th. P/LIn the Transfer Posting Parameters area,Target Valuation Class: for example, 61 Equity: Equity MethodKey Date: for example, <last date of cur-rent month>In the Posting Data area,Test Run: <select this checkbox> | The Securities Account Transfer: Edit screen is displayed. |  |
| 4 | Confirm the Data for Valuation Class Transfer | On the Edit Selected Positions screen, you check/adjust/confirm the data for valuation class tranfer and choose Exexcute. | The screen Valuation Log is displayed. If red traffic light exists, click on it and check the error message. Solve the issue and perform test run again until there is no error.You can check the simulated posting information for local GAAP (valuation area AE0) by choosing Logs + Messages. Please note there is no posting created because it is test run. |  |
| 5 | Review logs | Choose Messages and Log.On Information Overview dialog box, choose Posting Log.On Posting Log: Posted Business Transactions view, you review the postings. | Logs are reviewed. |  |
| 6 | Production Run | Go back to the initial view of this app. Unselect the Test Run checkbox and repeat the previous steps for production run. | Production run succeeds, postings are created. |  |

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
> Flagged while digesting this document, not verified: Associate or Joint Venture purchase section purpose says purchased ratio is under 20%, while the document defines associate/JV as 20% to 50%.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Correspondence section refers to BP group BP_DEFAULT / BP_GROUP, whereas elsewhere the predefined group is BPG_DEFAULT.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/shareholding-management-group-ledger-ifrs-5wg-ae-test-script-1127]]
- related-to :: [[05-treasury-and-cash-management/test-script-shareholding-management-group-ledger-us-gaap-5wh-ae-1128]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/5WF_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 247,061 chars in the whole document
