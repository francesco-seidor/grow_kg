---
id: 05-treasury-and-cash-management/test-script-intercompany-foreign-exchange-group-ledger-us-gaap-34m-ae
title: "Test Script: Intercompany Foreign Exchange – Group Ledger US GAAP (34M_AE) (34M_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 34M: intercompany FX deals, mirror deals and US GAAP parallel valuation postings (area 003)."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/intercompany-fx-deals]
aliases: [34M_S4CLD2608_BPD_EN_AE]
keywords: [Intercompany Foreign Exchange Deals, intercompany foreign exchange, group ledger us gaap, parallel valuation, fx spot forward, fx swap, non-deliverable forward, mirror deal, key date valuation, general ledger posting]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34M_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-913
topic: 05-treasury-and-cash-management/intercompany-fx-deals
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Intercompany Foreign Exchange – Group Ledger US GAAP (34M_AE) (34M_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34M_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Intercompany Foreign Exchange Deals** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Intercompany Foreign Exchange – Group Ledger US GAAP (34M_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851818)

[2 Prerequisites 4](#_Toc232851819)

[2.1 System Access 4](#_Toc232851820)

[2.2 Roles 4](#_Toc232851821)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232851822)

[2.4 Business Conditions 5](#_Toc232851823)

[2.5 Preliminary Steps 6](#_Toc232851824)

[2.5.1 Maintain Data for Intercompany Business Partner 6](#_Toc232851825)

[3 Overview Table 7](#_Toc232851826)

[4 Test Procedures 8](#_Toc232851827)

[4.1 Negotiate Process for Intercompany Foreign Exchange Contract 8](#_Toc232851828)

[4.1.1 Analyze Cash Position 8](#_Toc232851829)

[4.1.2 Determine Foreign Exchange Rates 8](#_Toc232851830)

[4.1.3 Agreement on Internal Foreign Exchange Contract by Receiving Company 9](#_Toc232851831)

[4.1.4 Agreement on Internal Foreign Exchange Contract by Issuing Company 9](#_Toc232851832)

[4.2 Create Foreign Exchange Contract - Intercompany Transaction 9](#_Toc232851833)

[4.2.1 Create Foreign Exchange Spot/Forward - Intercompany Transaction 9](#_Toc232851834)

[4.2.2 Create Foreign Exchange Swap - Intercompany Transaction 11](#_Toc232851835)

[4.2.3 Create Non-deliverable Forward - Intercompany Transaction 13](#_Toc232851836)

[4.3 Check Mirror Deal 14](#_Toc232851837)

[4.4 Period-end Closing (Parallel Valuation) 15](#_Toc232851838)

[4.4.1 Perform Key Date Valuation (Parallel Valuation) 16](#_Toc232851839)

[4.5 Post Flows to General Ledger (Parallel Valuation Area) 18](#_Toc232851840)

[4.6 Post Realized Profit and Loss (Parallel Valuation) 19](#_Toc232851841)

## Purpose

Overview

This scope item allows the company to exchange the foreign currency with the affiliate companies and post the transactions with Group Ledger US GAAP. It helps the customer to execute the posting for the parallel valuation area separately from the operative valuation area. In practice, the customer can also do postings for all valuation areas at the same time.

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

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data reflect materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

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

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 2F2 - Intercompany Foreign Exchange Management | Must be run before this test script. |
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

The scope item 34MIntercompany Foreign Exchange – Group Ledger US GAAP consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Analyze Cash Position](#unique_9) [page ] 8 | Cash Manager | Cash Flow Analyzer (F2332) | - |
| [Determine Foreign Exchange Rates](#unique_10) [page ] 8 | Treasury Specialist - Front Office | - | - |
| [Agreement on Internal Foreign Exchange Contract by Receiving Company](#unique_11) [page ] 9 | Treasury Specialist - Front Office | - | - |
| [Agreement on Internal Foreign Exchange Contract by Issuing Company](#unique_12) [page ] 9 | Treasury Specialist - Front Office | - | - |
| [Create Foreign Exchange Spot/Forward - Intercompany Transaction](#unique_13) [page ] 9 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) |  |
| [Create Foreign Exchange Swap - Intercompany Transaction](#unique_14) [page ] 11 | Treasury Specialist - Front Office | Create FX Swap (TX10) |  |
| [Create Non-deliverable Forward - Intercompany Transaction](#unique_15) [page ] 13 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) |  |
| [Check Mirror Deal](#unique_16) [page ] 14 | Treasury Specialist - Front Office | Process Spots/Forwards - Collective Processing (TX06) |  |
| [Post Flows to General Ledger (Parallel Valuation Area)](#unique_17) [page ] 18 | Treasury Accountant | Process Business Transactions (TPM10) |  |
| [Perform Key Date Valuation (Parallel Valuation)](#unique_18) [page ] 16 | Treasury Accountant | Run Valuation (TPM1) |  |
| [Post Realized Profit and Loss (Parallel Valuation)](#unique_19) [page ] 19 | Treasury Accountant | Post Derived Business Transactions (TPM18) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Negotiate Process for Intercompany Foreign Exchange Contract

Purpose

This following step are about the negotiation process for intercompany foreign exchange agreements.

Procedure

The negotiation process takes place outside of the system.

#### Analyze Cash Position

Purpose

The Cash Manager from central group verifies the cash position status and determines that a specific foreign currency is required for a subsidiary company based on analysis of foreign currency cash position. The Cash Manager enables the intercompany foreign currency exchange transactions.

Procedure

If full cash management is implemented in your system, use the Cash Flow Analyzer (F2332) app to analyze the cash position. For more information about procedures, see Advanced Cash Operations (J78).

#### Determine Foreign Exchange Rates

Purpose

In this activity, you determine the foreign exchange (FX) rates in Intercompany Foreign Currency Exchange Deals.

Procedure

The Treasury Specialist - Front Office from the central group determines the foreign exchange (FX) rates based on internal guidelines and external market environment. This activity takes places outside of the system.

#### Agreement on Internal Foreign Exchange Contract by Receiving Company

Purpose

In this activity, an agreement is reached on the internal foreign exchange (FX) contract by the receiving company.

Procedure

The Treasury Specialist - Front Office of the receiving company agrees on the internal FX contract details. This activity occurs outside of the system.

#### Agreement on Internal Foreign Exchange Contract by Issuing Company

Purpose

In this activity, an agreement is reached on the internal foreign exchange (FX) contract by the issuing company.

Procedure

The Treasury Specialist - Front Office of the issuing company agrees on the internal foreign exchange (FX) contract. This activity occurs outside of the system.

### Create Foreign Exchange Contract - Intercompany Transaction

Purpose

In the following procedures, you create the Foreign Exchange contracts as an Intercompany transaction.

Prerequisites

The prerequisites for intercompany transaction creation are in accordance to the foreign exchange (FX) transactions, which are described in the Foreign Currency Risk Management (1X1) test script. Complete the prerequisites of the Foreign Exchange Creation procedure using the affiliate company before proceeding.

#### Create Foreign Exchange Spot/Forward - Intercompany Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Foreign Exchange Spot or Forward transaction, for hedging or non-hedging purposes, with an affiliate company. The mirror transaction generates automatically in the affiliate company.

You can create a new transaction through the Copy Existing Transaction function. For detail steps, please refer to the Appendix section in the Foreign Currency Risk Management (1X1)

|  |
| --- |
| Remember Sample values for master data values are country-specific. Substitute the country-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter the selection criteria:Company Code: For example, 3310 for AEProduct Type: 60ITransaction Type: For example, 101Partner: For example, 17401710and choose EnterNote Use Transaction Type102 for forward transaction. | The Spot/Forward Transaction Entry: Structure view displays. |  |
| 4 | Enter Initial Data | Enter the following data:Rate: For example, EUR/USD 1.3Buy/Sell: For example, B BuyTraded Amt: For example, USD 1MValue Date: +2Note For Value Date, you can add more than +2 days for forward transaction.and select the Administr. tab. | The Administr. tab displays. |  |
| 5 | Enter Administr. Data | Enter the following data:Hdg Classific.: For example, Y0Risk Mitigation: For example, CheckNote If this transaction is intended for risk mitigation purposes, then check the Risk Mitigation box. When the box is checked, this excludes the transaction from Clearing Threshold Report (FTR_THRESHOLD_DISP) calculation.and choose Save. | The transaction saves and a transaction number generates.Note the transaction number for use in the mirror transaction query step. |  |

#### Create Foreign Exchange Swap - Intercompany Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a foreign exchange swap transaction, for hedging or non-hedging purposes, with an affiliate company. The mirror transaction generates automatically in the affiliate company.

|  |
| --- |
| Remember Sample values for master data values are country-specific. Substitute the country-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Swap (TX10). | The Create Forex Swap: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteriaCompany Code: For example, 3310 for AEPartner: For example, 17401710First transactionProduct Type: 60ITransaction Type: For example, 101Second transactionProduct Type: 60ITransaction Type: For example, 102and choose Enter. | The Create Forex Swap: Structure view displays. |  |
| 4 | Enter Data | Enter the following data:First TransactionCurrencies: For example, EUR/USDRate: For example, 1.3Buy/Sell: For example, B BuyTraded Amt: For example, USD 1MValue Date: For example, +22nd TransactionRate: For example, 1.2Value Date: For example, ++6and choose Save. | Two transactions save and two transaction numbers generate.Note both transaction numbers for use with the mirror transaction query step. |  |

#### Create Non-deliverable Forward - Intercompany Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create a Foreign Exchange Non-Deliverable-Forward transaction, for hedging or non-hedging purposes, with an affiliate company. The mirror transaction generates automatically in the affiliate company.

You can create a new transaction through the Copy Existing Transaction function. For detail steps, please refer to the Appendix section in the Foreign Currency Risk Management (1X1).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter selection criteriaCompany Code: For example, 3310 for AEProduct Type: 60JTransaction Type: For example, 110Partner: For example, 17401710and choose Enter. | The Spot/Forward Transaction Entry: Structure view displays. |  |
| 4 | Enter Data | Enter the following data:Rate: For example, AED/BRL 3.3220Buy/Sell: For example, B BuyTraded Amt: For example, BRL 50MValue Date: ++6+2Fixing Date: ++6Settlement Currency: For example, AED | The Spot/Forward Transaction Entry: Structure view displays. |  |
| 5 | Enter Data in Administration Tab | Enter the following data:Hdg Classific: For example, Y0Risk Mitigation: For example, CheckNote If this transaction is intended for risk mitigation purposes, then check the Risk Mitigation box. When the box is checked, this excludes the transaction from the Clearing Threshold Report (FTR_THRESHOLD_DISP) calculation..and choose Save. | Transaction saves and a transaction number generates.Note the transaction number for use with the mirror transaction query. |  |

### Check Mirror Deal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

An FX mirror deal is created automatically with the same status as the issuing deal. This activity describes how to review the mirror deal details.

|  |
| --- |
| Remember Sample values for master data values are country-specific. Substitute the country-specific values provided by Best Practices for SAP S/4HANA or use master data values you have created for this purpose. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Spots/Forwards - Collective Processing (TX06). | The Forex: Collective Processing view displays. |  |
| 3 | Enter Selection Criteria | Enter the following dataCompany Code: For example, 3310 for AETransaction: <Issuing Transaction Number(s) created in previous steps>Accept default values for other parameters.Choose Execute. | The transaction is displays in the next view. |  |
| 4 | Display Issuing Deal | On the Forex: Collective Processingview, select the checkbox for the transaction line and choose Display | Display Forex Transaction: view displays with the transaction data.Mirror transaction 1000XXXXXXX is available in company code XXXX message displays.Note down the mirror transaction number for use with the query. |  |
| 5 | Query Mirror Transaction | Return to Forex: Collective Processing view, enter the following data:Company Code: for example, 1020 or 3310 for custom company code or AETransaction: <Enter Mirror Transaction Number(s) created in previous steps>Accept default values for the other parameters.Choose Execute. | Mirror Transaction lists on the Forex: Collective Processing view. For additional details, choose Display. |  |

### Period-end Closing (Parallel Valuation)

Purpose

In this section if the maturity date of transactions is in next periods, you perform key date valuation for period-end closing (usually executed at month end) in the parallel valuation area for US GAAP if maturity date is in same period, you can skip the step.

|  |
| --- |
| Remember Process this step for both the issuing company and the receiving company. |

#### Perform Key Date Valuation (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to:

- Value the positions of financial instruments based on historical cost or fair value for a given key date in valuation area 003 for US GAAP
- Transfer results to the corresponding US GAAP ledger in Financial Accounting (FI)

|  |
| --- |
| Remember Process this step for both the issuing company and the receiving company. |

Prerequisites

Both issuing deal and mirror deal should be settled first. Fair values (NPV) are calculated or maintained for financial transactions that are evaluated at fair value (NPV) according to US GAAP. For more information, see the Calculate or Maintain Fair Value of Transaction step in test script Foreign Currency Risk Management(1X1).

Key date valuation is executed in valuation area AE0 for local GAAP in test script Foreign Currency Risk Management(1X1).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Execute Valuation screen displays. |  |
| 3. | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select>Company code: for example 3310Valuation Area: for example, 003Transaction: <transaction number(s) created>Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, <Mid-year Valuation with Reset>Note When the period end is also the year end, use the Valuation Category Year-End Valuation.Test Run: <select> | The Display Positions to be Valued screen displays. |  |
| 4. | Execute Valuation for Test Run | Choose Execute Valuation.If the Message dialog box displays, choose Continue. | The Valuation Log screen displays. If an entry has a red traffic light exist, click it and check the error message. Solve the issue and perform another test run until the error is cleared.To check the simulated posting information for US GAAP (valuation area 003), choose Logs + Messages. No posting is created because it is a test run.Note Occasionally, no simulated postings are shown. Your selected transaction may not need valuation. |  |
| 5. | Enter Selection Criteria for Production Run | Choose Back until you return to the initial screen of this app.Change the following data and choose Execute:Test Run: <deselect> | The Display Positions to be Valued screen displays. |  |
| 6. | Execute Valuation for Production Run | Choose Execute Valuation. | The Valuation Log screen displays. To check the posting information for US GAAP (valuation area 003), chose Logs + Messages. An accounting document is created in the corresponding US GAAP ledger. |  |

### Post Flows to General Ledger (Parallel Valuation Area)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you post the flows in parallel valuation area 003 for US GAAP. They are reflected in the corresponding ledger in Financial Accounting (FI). The flows include buying foreign exchange, selling foreign exchange, or flow for cash settlement.

|  |
| --- |
| Remember Process this step for both the issuing company and the receiving company. |

Prerequisites

The flows of deals are posted in operative valuation AE0 for local GAAP. This is described in test script Foreign Currency Risk Management (1X1).

You executed the following activities in 1X1 with apps:

- Fix, Pay and Post Flows (TBB1): You generated a payment request for outgoing payment with option Pay Only, and generated the posting for incoming payment (without payment request) in valuation area AE0 with option Post Operational Only.
- Process Business Transactions (TPM10): You generated the posting for outgoing payment (with payment request) in valuation area AE0.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Process Business Transactions (TPM10). | The Process Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select>Company Code: for example 3310Valuation Area: for example, 003Limit by Transaction Number: <deselect>Limit by Subledger Pos.: <select>Transaction: <transaction number(s) created with flows posted in valuation area AE0>Test Run: <select> | The Test Run: Post/Reverse Business Transactions screen displays.If the system displays the message You have not selected any business transactions, no posting is needed for your selection criteria. Skip this step. |  |
| 4 | Check Test Run Result | Choose Select All, choose Choose Those to Post, and choose Execute. | The Test Run: Display Posted/Reversed Business Transactions screen displays. |  |
| 5 | Logs and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen displays. Check the simulated posting information for US GAAP (valuation area 003) on this screen. No posting is created because it is a test run. |  |
| 6 | Enter Selection Criteria for Production Run | Choose Back. | The Process Business Transactions screen displays. |  |
| 7 | Deselect Test Run | Change the following data and choose Execute:Test Run: <deselect> | The Update Run: Post/Reverse Business Transactions screen displays. |  |
| 8 | Production Run | Choose Select All, choose Choose Those to Post, and choose Execute. | The Update Run: Display Posted/Reversed Business Transactions screen displays. |  |
| 9 | Logs and Messages | Choose Log and Messages. | The Posting Log: Posted Business Transactions screen displays. An accounting document is created for US GAAP (valuation area 003) |  |

### Post Realized Profit and Loss (Parallel Valuation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you fix and post derived business transactions (usually, realized profit and loss when deal is mature) in valuation area 003 for US GAAP.

|  |
| --- |
| Remember Process this step for both the issuing company and the receiving company. |

Prerequisites

The derived business transaction is fixed and posted in valuation area AE0 for local GAAP. This is described in the Post Realized Profit and Loss step in test script Foreign Currency Risk Management(1X1).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3. | Enter Selection Criteria for Test Run | Enter the following data and choose Execute:OTC Transactions: <select>Company code: for example, 3310Valuation Area: for example, 003OTC Transactions: <transaction number(s) created>TRL Date: <maturity date of transaction>Test Run: <select>Confirm the message Are you sure that you want to select future business transactions by pressing Enter. | The Fix and Post Derived Business Transactions screen displays.If the system displays the message No scheduled derived business transactions were found for the selection, no derived transaction is available for your selection, You can skip this step. |  |
| 4. | Fix and Post for Test run | Choose Fix. | The Posting Log: Posted Business Transactions screen displays. The simulated posting information for US GAAP (valuation area 003) is shown. No posting is created, because it is a test run. |  |
| 5. | Enter Selection Criteria for Production Run | Choose Back until you return to the the initial screen of this app.Change the following data and choose Execute:Test Run: <deselect>Confirm the message Are you sure that you want to select future business transactions by pressing Enter | The Fix and Post Derived Business Transactions screen displays. |  |
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
- related-to :: [[05-treasury-and-cash-management/intercompany-foreign-exchange-group-ledger-ifrs-2hu-ae-test-script-826]]
- related-to :: [[05-treasury-and-cash-management/intercompany-foreign-exchange-management-2f2-ae-test-script-819]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/34M_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 33,447 chars in the whole document
