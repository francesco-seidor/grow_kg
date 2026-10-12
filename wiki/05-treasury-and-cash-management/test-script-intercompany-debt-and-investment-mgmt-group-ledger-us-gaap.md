---
id: 05-treasury-and-cash-management/test-script-intercompany-debt-and-investment-mgmt-group-ledger-us-gaap
title: "Test Script: Intercompany Debt and Investment Mgmt – Group Ledger US GAAP (34L_AE) (34L_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud test script for scope item 34L_AE: intercompany loans posted to US GAAP parallel valuation area 003, from deal creation to period-end."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/intercompany-debt-and-investment]
aliases: [34L_S4CLD2608_BPD_EN_AE]
keywords: [Intercompany Debt and Investment (Mirror Loans), intercompany debt and investment, parallel valuation, us gaap ledger, mirror deals, interest rate instrument, current account-style instrument, period-end closing, interest accrual, key date valuation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34L_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-912
topic: 05-treasury-and-cash-management/intercompany-debt-and-investment
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Intercompany Debt and Investment Mgmt – Group Ledger US GAAP (34L_AE) (34L_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34L_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Intercompany Debt and Investment (Mirror Loans)** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Debt and Investment Mgmt – Group Ledger US GAAP (34L_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851794)

[2 Prerequisites 4](#_Toc232851795)

[2.1 System Access 4](#_Toc232851796)

[2.2 Roles 4](#_Toc232851797)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232851798)

[2.4 Business Conditions 5](#_Toc232851799)

[2.5 Preliminary Steps 6](#_Toc232851800)

[2.5.1 Maintain Data for Intercompany Business Partner 6](#_Toc232851801)

[3 Overview Table 7](#_Toc232851802)

[4 Test Procedures 8](#_Toc232851803)

[4.1 Negotiation Process for Intercompany Foreign Exchange Contact 8](#_Toc232851804)

[4.1.1 Analyze Cash Position 8](#_Toc232851805)

[4.1.2 Determine Interest Rates 8](#_Toc232851806)

[4.1.3 Agree on Internal Contract by Receiving Company 9](#_Toc232851807)

[4.1.4 Agree on Internal Contract by Issuing Company 9](#_Toc232851808)

[4.2 Create Debt and Investment Contract - Intercompany Transaction 9](#_Toc232851809)

[4.2.1 Create Interest Rate Instrument - Intercompany Transaction 9](#_Toc232851810)

[4.2.2 Create Current Acct-Style Instrument - Intercompany Transaction 11](#_Toc232851811)

[4.3 Check Mirror Deal 13](#_Toc232851812)

[4.4 Post Flows to General Ledger (Parallel Valuation Area) 14](#_Toc232851813)

[4.5 Period-end Closing (Parallel Valuation) 16](#_Toc232851814)

[4.5.1 Run Accrual (Parallel Valuation) 16](#_Toc232851815)

[4.5.2 Perform Key Date Valuation (Parallel Valuation) 18](#_Toc232851816)

[4.6 Post Realized Profit and Loss (Parallel Valuation) 19](#_Toc232851817)

## Purpose

Overview

This scope item allows the company to post the accounting in a parallel valuation area when it handles loans with an affiliate company.

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

| Name (Role Template) | Description | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- | --- |
| Treasury Accountant |  | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |
| Treasury Specialist - Front Office |  | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Valuation Area | 003 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| 1YI - Intercompany Process for Debt and Investment Mgmt | Must be run before this test script. |
| 2VA - Accounting and Financial Close – Group Ledger US GAAP | Must be in scope as prerequisite. |

### Preliminary Steps

#### Maintain Data for Intercompany Business Partner

Purpose

To maintain intercompany business process such as mirror deals in the system, you need to create intercompany business partners first to make the functionality work.

To maintain business partner for TRM, refer to Setting Up Intercompany Foreign Exchange Management (2F2) for details. Make sure you go through all steps in the following sections for both Issuing Company and Receiving Company:

- Maintain General Data for Intercompany Business Partner
- Maintain Company Code Data for Intercompany Business Partner
- Correspondence
- Maintain Relevant Settings for Intercompany Transaction

## Overview Table

The scope item Intercompany Debt and Investment Mgmt – Group Ledger US GAAP consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Analyze Cash Position](#unique_9) [page ] 8 | Cash Manager | Cash Flow Analyzer (F2332) | - |
| [Determine Interest Rates](#unique_10) [page ] 8 | Treasury Specialist - Front Office | - | - |
| [Agree on Internal Contract by Receiving Company](#unique_11) [page ] 9 | Treasury Specialist - Front Office | - | - |
| [Agree on Internal Contract by Issuing Company](#unique_12) [page ] 9 | Treasury Specialist - Front Office | - | - |
| [Create Interest Rate Instrument - Intercompany Transaction](#unique_13) [page ] 9 | Treasury Specialist - Front Office | Create IR Instrument (TM_51) |  |
| [Create Current Acct-Style Instrument - Intercompany Transaction](#unique_14) [page ] 11 | Treasury Specialist - Front Office | Create CA Style Instrument (FTRCAI01) |  |
| [Check Mirror Deal](#unique_15) [page ] 13 | Treasury Specialist - Front Office | Process MM Transactions - Collective Processing (TM00) |  |
| [Post Flows to General Ledger (Parallel Valuation Area)](#unique_16) [page ] 14 | Treasury Accountant | Process Business Transactions (TPM10) |  |
| [Run Accrual (Parallel Valuation)](#unique_17) [page ] 16 | Treasury Accountant | Run Accrual/Deferral (TPM44) |  |
| [Perform Key Date Valuation (Parallel Valuation)](#unique_18) [page ] 18 | Treasury Accountant | Run Valuation (TPM1) |  |
| [Post Realized Profit and Loss (Parallel Valuation)](#unique_19) [page ] 19 | Treasury Accountant | Post Derived Business Transactions (TPM18) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Negotiation Process for Intercompany Foreign Exchange Contact

Context

In this activity, the negotiation process for intercompany contact agreement takes place. The negotiation process occurs and completes outside of the system.

#### Analyze Cash Position

Purpose

The Cash Manager from the central group reviews the cash position status. If a need of liquidity for a subsidiary company based on analysis of cash position is identified, then it initiates the intercompany debt and investment deal.

Procedure

When full cash management is implemented for your system, use the Cash Flow Analyzer (F2332) app for analyzing the cash position. For more information about this procedure, see Advanced Cash Operations (J78).

#### Determine Interest Rates

Purpose

In this activity, you determine the interest rates in intercompany debt or investment deals.

Procedure

For this procedure, a Treasury Specialist - Front Office, from the central group, determines interest based on internal guidelines and external market environment. This activity occurs outside of the system.

#### Agree on Internal Contract by Receiving Company

Purpose

In this activity, agreement is reached on internal intercompany debt or an investment contract by the receiving company.

Procedure

A Treasury Specialist - Front Office of the receiving company agrees on internal intercompany debt or an investment contract detail. This activity occurs outside of the system.

#### Agree on Internal Contract by Issuing Company

Purpose

In this activity, an agreement is reached on internal intercompany debt or an investment contract by the issuing company.

Procedure

In this procedure, the Treasury Specialist - Front Office of the issuing company agrees to the internal intercompany debt or an investment contract. This activity occurs outside of the system.

### Create Debt and Investment Contract - Intercompany Transaction

Context

In this activity, you create the debt or investment contracts as an intercompany transaction.

Prerequisites

The prerequisites of intercompany deals creation that are in accordance to debt or investment deals with external business partner are described in Debt and Investment Management (1WV). For this procedure, you follow those prerequisites of the debt or investment creation using the affiliate company information.

#### Create Interest Rate Instrument - Intercompany Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create an interest rate instrument transaction with an affiliate company. The mirror transaction generates automatically in the affiliate company.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. |  |  |
| 2 | Access the SAP Fiori App | Open Create IR Instrument (TM_51). | The Create Interest Rate Instrument view displays. |  |
| 3 | Create A New Deal | On the Create Interest Rate Instrument view, enter the following data:Company Code: for example, 3310Product Type: 55ITransaction Type: for example, 200Partner: for example, 17401710and choose Enter. | The Create Interest Rate Instrument: Structure view displays. |  |
| 4 | Maintain Structure of New Deal | Enter the following data:Amount: For example, 10MStart: For example, <Current Date>End: For example, <Current Date + 3 years>Interest Cat.: For example, VariableRef,Int.Rate: For example, EURM03EUR +/- 11st Int. Rate: For example, 3.0000000Int. Calc. Method: For example, Act/360Frequency: For example, MonthlyContract Date: For example, <Current Date/Current Time>. |  |  |
| 5 | Maintain Administration | Choose the Administr. view and enter following data:Portfolio: For example, Y000Gen. Valn Class: For example, Short term debt (current liability). |  |  |
| 6 | Maintain Payment Details | Choose the Payment Details tab and find the incoming line with the direction of flow "+" and outgoing row with the direction of flow "-". Double-click the outgoing row and confirm the assignments or enter the following data:Payment Request, With: <select this checkbox>House Bank: For example, AEBK1Account ID: For example, AEAC1Payer/Payee: For example,Partner Bank: For example, AED1Payment methods: For example, T. |  |  |
| 7 | Save | Choose Check to verify the input data. If no error notification appears, choose Save. | Transaction saves and a transaction number generates. Note the transaction number for the mirror transaction query. |  |

#### Create Current Acct-Style Instrument - Intercompany Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a current acct-style instrument. The mirror transaction generates automatically for an affiliate company.

|  |
| --- |
| Note After a contact settles, the issuing company can increase or decrease the nominal amount of the current acct-style instrument transaction according to business requirement. For internal cash flow balance, the receiving company consequently updates the mirror transaction. The update to the mirror transaction is a manual process. For more information, see the Nominal Amount Adjustment procedure in the Debt and Investment Management (1WV) test script. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. |  |  |
| 2 | Access the SAP Fiori App | Open Create CA Style Instrument (FTRCAI01). | The Create Current Acct-Style Instrument view displays. |  |
| 3 | Enter Selection Criteria | Enter the following selection criteria:Company Code: For example, 3310Product Type: 58ITransaction Type: For example, 300Partner: For eample, 17401710and choose Enter. | The Create Current Acct-Style Instrument: Structure view displays. |  |
| 4 | Enter data | Enter the following data:Flow Type: For example, 1101 or 1111Amount: For example, 10MStart: For example, <Current Date - 7 days>End: For example, <Current Date + 3 years>Interest Category: For example, FixedPercentage Rate: For example, 3.0000000Int. Calc. Method: For example, Act/360Frequency: For example, MonthlyContract Date: For example, <Current Date - 7 days> | The Administr. tab displays. |  |
| 5 | Maintain Administration of New Deal | Choose Administr. view and enter the following data:Gen. Valn Class: For example, Short term investment (current asset): Amortized cost |  |  |
| 6 | Maintain Payment Details of New Deal | Choose the Payment Details tab. In the Payment Details tab, you see the incoming line with Direction of flow "+" and outgoing row with Direction of flow "-". Double-click the outgoing row. Confirm the assignments or enter following data:Payment Request, With: <select this checkbox>House Bank: For example, AEBK1Account ID: For example, AEAC1Payer/Payee: For example, 33403310Partner Bank: For example, AED1Payment methods: For example, T |  |  |
| 7 | Save the New Deal | Choose Check to verify the input data. If no error notification displays, choose Save. | The transaction saves and a transaction number generates. Note the transaction number for use with the mirror transaction query. |  |

### Check Mirror Deal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A debt and investment mirror deal is created automatically with the same status as the issuing deal. In this activity, you review the mirror deal details.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. |  |  |
| 2 | Access the SAP Fiori App | Open Process MM Transactions - Collective Processing (TM00). | The Money Market: Collective Processing view displays. |  |
| 3 | Enter Selection Criteria | On the Money Market: Collective Processing view, enter the following data:Company Code: For example, 3310Transaction: <Issuing Transaction Numbers created in previous step>Accept default values for other parameters.and choose Execute. | The transaction displays in the next view. |  |
| 4 | Change the Transaction | On the Money Market: Collective Processing view, select the checkbox for the transaction line and choose Display. | Display CAI Transaction: Structure view displays with the transaction data.The Mirror transaction 1000XXXXXXX is available in company code XXXX notification displays.Note the Mirror transaction number for use with the following step. |  |
| 5 | Query Mirror Transaction | Return to the Money Market: Collective Processing view and enter the following data:Company Code: For example, 1020 or 3310Transaction: < The Mirror Transaction Numbers created in previous step>Accept default values for other parameters and choose Execute. | A Mirror Transaction appears on the Money Market: Collective Processing view, choose Display for details. |  |

### Post Flows to General Ledger (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the flows in parallel valuation area 003 for ledger of US GAAP. They are reflected in the corresponding ledger in Financial Accounting (FI). The flows include incoming or outgoing payment of increasing or decreasing nominal , interest, repayment of debt, or investment instruments.

|  |
| --- |
| Remember Process this step for both the issuing company and the receiving company. |

Prerequisites

The flows of deals are posted in operative valuation AE0 for local GAAP, described in the Debt and Investment Management (1WV) test script. You executed the following activities in 1WV with apps:

- Manage Financial Transactions (F6157): Once a Treasury Risk Management (TRM) transaction is recorded and saved, the transaction must be settled before continuing with further activities. You can settle the transaction in two ways: Manual Settlement or Automatic Settlement via Correspondence Process.
- Fix, Pay and Post Flows (TBB1): You generated a payment request for outgoing payment with option Pay Only, and generated the posting for incoming payment (without payment request) in valuation area AE0 with option Post Operational Only.
- Process Business Transactions (TPM10): You generated the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Fix, Post or Reverse Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany code: for example, 3310Valuation Area: for example, 003Limit by Transaction Number: DeselectedLimiting by Subledger Positions: SelectedTransaction: <transaction number(s) was created, and flows have been posted in valuation area AE0>Test Run: Selected | The Test Run: Post/Reverse Business Transactions screen displays.If the system displays the message You have not selected any business transactions, no posting is needed for your selection criteria. Skip this step. |  |
| 4 | Check Test Run Result | Choose Select All, choose Choose Those to Post, and choose Execute. | The Test Run: Display Posted/Reversed Business Transactions screen displays. |  |
| 5 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen displays. Check the simulated posting information for US GAAP (valuation area 003) on this screen. No posting is created because it is a test run. |  |
| 6 | Enter Selection Criteria for Production Run | Choose Back.On the Fix, Post or Reverse Transactions screen, change the following data and choose Execute:Test Run: Deselected | The Update Run: Post/Reverse Business Transactions screen displays. |  |
| 7 | Production Run | Choose Select All, choose Choose Those to Post, and choose Execute. | The Update Run: Display Posted/Reversed Business Transactions screen displays. |  |
| 8 | Log and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen displays. An accounting document is created for US GAAP (valuation area 003). |  |

### Period-end Closing (Parallel Valuation)

Purpose

This section describes activities for period-end closing (usually executed at month end) in parallel valuation area for US GAAP, including:

- Accrue interest income/expenses
- Perform key date valuation

#### Run Accrual (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use this function to accrue interest expenses and interest income in valuation area 003 for US GAAP, and reflect results correctly in the corresponding ledger in Financial Accounting (FI).

|  |
| --- |
| Remember Process this step for both the issuing company and the receiving company. |

Prerequisites

Accruals are executed in valuation area AE0 for local GAAP, described in the Run Accrual step in the Debt and Investment Management (1WV) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Accrual/Deferral (TPM44). | The Execute Accrual/Deferral of Expenses and Revenues screen displays. |  |
| 3 | Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany code: for example 3310Valuation Area: for example 003Transaction: <transaction number(s) created>Accrual/Deferral Key Date: for example <last date of current month>Include key date: for example, SelectedTest Run: Selected | The Execute Accrual/Deferral of Expenses and Revenues screen displays. Check accrual information on this screen. |  |
| 4 | Logs and Messages | Choose Logs and Messages. | The simulated posting information for US GAAP (valuation area 003) is shown. No posting is created because it is a test run. |  |
| 5 | Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: Deselected | The Execute Accrual/Deferral of Expenses and Revenues screen displays. Check accrual information on this screen. |  |
| 6 | Logs and Messages | Choose Logs and Messages | The posting information for US GAAP (valuation area 003) is shown. An accounting document is created in the corresponding US GAAP ledger. |  |

#### Perform Key Date Valuation (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to value the positions of financial instruments based on historical cost or fair value for a given key date in valuation area 003 for US GAAP, and transfer results to corresponding ledger for US GAAP in Financial Accounting (FI).

|  |
| --- |
| Remember Process this step for both the issuing company and the receiving company. |

Prerequisites

Fair values (NPV) are calculated or maintained for financial transactions that are evaluated at fair value (NPV) according to US GAAP. For more information, see the Calculate or Maintain Fair Value of Transaction step in test script Debt and Investment Management(1WV).

Key date valuation is executed in valuation area AE0 for local GAAP in test script Debt and Investment Management(1WV).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Execute Valuation view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany code: for example 3310Valuation Area: for example 003Transaction: <transaction number(s) created>Key Date for Valuation: for example <last date of current month>Valuation Category: for example Mid-year Valuation with ResetNote When the Period End is also the Year End, use the Valuation Category Year-End Valuation should be usedTest Run: Selected | The Display Positions to be Valued view displays. |  |
| 4 | Execute Valuation for Test Run | Choose Execute Valuation.If the Message dialog box displays, choose Continue. | The Valuation Log view displays. If an entry has a red traffic light, click it and check the error message. Perform the test run again until the error is resolved.To check the simulated posting information for US GAAP (valuation area 003), choose Logs + Messages. No posting is created because it is a test run.Note Occasionally, if your selected transaction does not need valuation, there is no simulated posting. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial view of this app.Change the following data and choose Execute:Test Run: Deselected | The Position Valued view displays. |  |
| 6 | Execute Valuation for Production Run | Choose Run Valuation. | The Valuation Log view displays. To check the posting information for US GAAP (valuation area 003), choose Logs + Messages. An accounting document is created in the corresponding US GAAP ledger. |  |

### Post Realized Profit and Loss (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you fix and post derived business transactions (usually realized profit and loss when deal is mature) in valuation area 003 for US GAAP.

|  |
| --- |
| Remember Process this step for both the issuing company and the receiving company. |

Prerequisites

The derived business transaction is fixed and posted in valuation area AE0 for local GAAP. This is described in the Post Realized Profit and Loss step in test script Debt and Investment Management(1WV).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3. | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: SelectedCompany code: for example 3310Valuation Area: for example 003OTC Transactions: <transaction number(s) created>TRL Date: <maturity date of transaction>Test Run: SelectedConfirm the message Are you sure that you want to select future business transactions by pressing Enter. | The Fix and Post Derived Business Transactions screen displays.If the system displays the message No scheduled derived business transactions were found for the selection, no derived transaction is available for your selection. Skip this step. |  |
| 4. | Fix and Post for Test run | Choose Fix. | The Posting Log: Posted Business Transactions screen displays. Simulated posting information for US GAAP (valuation area 003) is shown. No posting is created because it is a test run. |  |
| 5. | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: DeselectedConfirm the message Are you sure that you want to select future business transactions by pressing Enter. | The Fix and Post Derived Business Transactions screen displays. |  |
| 6. | Fix and Post for Production run | Choose Fix. | The Posting Log: Posted Business Transactions screen displays. The posting information for US GAAP (valuation area 003) is shown. An accounting document is created in the US GAAP ledger in financial accounting. |  |

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
- related-to :: [[05-treasury-and-cash-management/test-script-intercompany-debt-and-investment-mgmt-group-ledger-ifrs-2o]]
- related-to :: [[05-treasury-and-cash-management/test-script-intercompany-process-for-debt-and-investment-mgmt-1yi-ae-7]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34L_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 33,786 chars in the whole document
