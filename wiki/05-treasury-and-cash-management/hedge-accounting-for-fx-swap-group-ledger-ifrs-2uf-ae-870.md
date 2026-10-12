---
id: 05-treasury-and-cash-management/hedge-accounting-for-fx-swap-group-ledger-ifrs-2uf-ae-870
title: Hedge Accounting for FX Swap – Group Ledger IFRS (2UF_AE) (2UF_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script 2UF (AE): IFRS 9 cash flow hedge accounting with FX swap overhedge processing, from hedging area to period-end, maturity and termination."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/hedge-accounting-fx]
aliases: [2UF_S4CLD2608_BPD_EN_AE]
keywords: [Hedge Accounting for FX Exposures, hedge accounting, overhedge processing, fx swap transactions, hedging area, hedging relationships, period-end closing, hedging reserve reclassification, hedging classifications, raw exposure]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UF_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-870
topic: 05-treasury-and-cash-management/hedge-accounting-fx
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Hedge Accounting for FX Swap – Group Ledger IFRS (2UF_AE) (2UF_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UF_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Hedge Accounting for FX Exposures** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Hedge Accounting for FX Swap – Group Ledger IFRS (2UF_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232850502)

[2 Prerequisites 5](#_Toc232850503)

[2.1 System Access 5](#_Toc232850504)

[2.2 Roles 5](#_Toc232850505)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232850506)

[2.4 Business Conditions 6](#_Toc232850507)

[3 Overview Table 8](#_Toc232850508)

[4 Test Procedures 12](#_Toc232850509)

[4.1 Overhedge Processing - FX Swap 12](#_Toc232850510)

[4.1.1 Define or Adjust Hedging Area 12](#_Toc232850511)

[4.1.2 Create Raw Exposure 22](#_Toc232850512)

[4.1.3 Take Snapshot 24](#_Toc232850513)

[4.1.4 Review Net Open Exposure in Hedge Management Cockpit 25](#_Toc232850514)

[4.1.5 Create Original Foreign Exchange Contract with Hedging Classification 26](#_Toc232850515)

[4.1.6 Automatically Create Original Hedging Relationship (Planned Designation) 28](#_Toc232850516)

[4.1.7 Set Contract Settlement Status with Incoming Confirmation 33](#_Toc232850517)

[4.1.8 Release Original Hedging Relationship 34](#_Toc232850518)

[4.1.9 Period End Closing Before Swap 36](#_Toc232850519)

[4.1.9.1 Calculate NPV of Hedging Instrument and Hypothetical Derivative 36](#_Toc232850520)

[4.1.9.2 Run Key Date Valuation 38](#_Toc232850521)

[4.1.9.3 Run Classification 39](#_Toc232850522)

[4.1.10 Create Raw Exposure for Overhedge Situation 41](#_Toc232850523)

[4.1.11 Take Snapshot 43](#_Toc232850524)

[4.1.12 Create and Submit Swap Request in Hedge Management Cockpit 43](#_Toc232850525)

[4.1.13 Release Swap Request 44](#_Toc232850526)

[4.1.14 Create FX Swap Transactions 45](#_Toc232850527)

[4.1.14.1 Option 1: Create FX Swap Transactions in Single Step 46](#_Toc232850528)

[4.1.14.2 Option 2: Create Two Legs of FX Swap Separately and Create Swap Reference 48](#_Toc232850529)

[4.1.15 Automatically Update Original Hedging Relationship and Create New Hedging Relationship (Planned Designation) 51](#_Toc232850530)

[4.1.16 Set Contract Settlement Status for FX Swap Transactions with Incoming Confirmations 56](#_Toc232850531)

[4.1.17 Process Hedging Relationships at Swap Date 57](#_Toc232850532)

[4.1.18 Period end Closing between Swap Date and Maturity of Original FX Transaction 59](#_Toc232850533)

[4.1.18.1 Calculate NPV of Hedging Instruments and Hypothetical Derivatives 60](#_Toc232850534)

[4.1.18.2 Run Key Date Valuation 61](#_Toc232850535)

[4.1.18.3 Run Classification 63](#_Toc232850536)

[4.1.19 Process Reclassification for Original Hedging Relationship at Balance Sheet Recognition Date 64](#_Toc232850537)

[4.1.20 Contract Maturity for Original FX Transaction and Offsetting FX Transaction 67](#_Toc232850538)

[4.1.20.1 (1X1) Foreign Currency Risk Management and (1X9) Foreign Currency Risk Management – Group Ledger IFRS 67](#_Toc232850539)

[4.1.20.2 Process Hedging Relationships at Maturity Date of Original FX Transaction and Offsetting FX Transaction 68](#_Toc232850540)

[4.1.21 Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date of Original Hedging Relationship 71](#_Toc232850541)

[4.1.22 Period end Closing after Maturity of Original and Offsetting FX Transactions 73](#_Toc232850542)

[4.1.22.1 Calculate NPV of Hedging Instrument and Hypothetical Derivative 73](#_Toc232850543)

[4.1.22.2 Run Key Date Valuation 75](#_Toc232850544)

[4.1.22.3 Run Classification 76](#_Toc232850545)

[4.1.23 Process Reclassification for New Hedging Relationship at Balance Sheet Recognition Date 78](#_Toc232850546)

[4.1.24 Contract Maturity for Securing FX Transaction 80](#_Toc232850547)

[4.1.24.1 (1X1) Foreign Currency Risk Management and (1X9) Foreign Currency Risk Management – Group Ledger IFRS 80](#_Toc232850548)

[4.1.24.2 Process Dedesignation for New Hedging Relationship at Maturity Date of Securing FX Transaction 81](#_Toc232850549)

[4.1.25 Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date of New Hedging Relationship 84](#_Toc232850550)

[4.1.26 Reporting 86](#_Toc232850551)

[4.1.26.1 Display Treasury Position Flows 86](#_Toc232850552)

[4.1.26.2 Display Treasury Posting Journal 86](#_Toc232850553)

[4.1.26.3 Display Treasury Position Values 87](#_Toc232850554)

[5 Appendix 88](#_Toc232850555)

[5.1 Process Integration 88](#_Toc232850556)

[5.1.1 Preceding Processes 88](#_Toc232850557)

[5.2 Termination of Hedging Instrument 89](#_Toc232850558)

[5.2.1 Create, Submit and Release Termination Request for Hedging Instrument 89](#_Toc232850559)

[5.2.2 Terminate Hedging Instrument 90](#_Toc232850560)

[5.2.3 Set Termination Settlement Status for Hedging Instrument 92](#_Toc232850561)

[5.2.4 Process Dedesignation for Hedging Business Transaction at Termination Date 93](#_Toc232850562)

[5.2.5 Post Flows for Termination 94](#_Toc232850563)

[5.3 Simulated Valuation 95](#_Toc232850564)

[5.3.1 Run Simulated Valuation 95](#_Toc232850565)

[5.3.2 Delete Simulated Valuation 97](#_Toc232850566)

## Purpose

Overview

This process helps you to mitigate profit and loss volatility from the use of derivatives.

Currently, the scope item supports IFRS 9 and covers cash flow hedge using FX forwards (including NDF) as hedging instruments, and using FX Swap as to transfer hedging instruments from the original exposure period to a new exposure period if an overhedge situation occurs in the original exposure period.

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
| Treasury Specialist - Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE | Treasury Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE |  |
| Treasury Specialist - Front Office | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Treasury Accountant | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Master Data | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Valuation Area | 002 |  |  |
| Hedging Area | HA0003 |  |  |
| Business Partner | 33537001 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| MDS | Description |
| --- | --- |
| 22G | Create Business Partner for Treasury and Risk Management - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 1X1 - Foreign Currency Risk Management | Business partner has been created. As a prerequisite for running current test script, an appropriate business partner (counterparty) must exist. Follow preliminary step Create Business Partner in test script 1X1 - Foreign Currency Risk Management to create a business partner. |
| 1XN - Market Rates Management – Manually via Upload | Market data has been maintained. As perquisites for running current test script, execute the following steps in test script 1XN - Market Rates Management – Manually via Upload to maintain the necessary market data manually for hedge accounting:Enter FX Spot RatesEnter Interest RatesCreate Reference Entities for Business PartnersAssign Attributes to Evaluation TypeMaintain Reference EntitiesEnter Credit SpreadsEnter Basis Spreads |
| 1X1 - Foreign Currency Risk Management | (Optional) Correspondence setting has been maintained for business partner. As a prerequisite for running current test script when using Designation Type which requires counterconfirmation, correspondence process should be proceeded, therefore correspondence setting should be maintained for business partner in advance. See preliminary step Maintain Profile and BP Group Assignments to External Recipient in test script 1X1 - Foreign Currency Risk Management for correspondence setting. |
| 1X1 - Foreign Currency Risk Management | (Optional) Credit limits have been maintained. Please follow preliminary step Maintaining Credit Limit in test script 1X1 - Foreign Currency Risk Management to maintain credit limits. |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

Overhedge Processing - FX Swap:

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Define or Adjust Hedging Area](#unique_8) [page ] 12 | Treasury Specialist - Middle Office | Define Hedging Area (TOE_HEDGING_AREA) | Hedging Area is created or extended. |
| [Create Raw Exposure](#unique_9) [page ] 22 | Treasury Specialist - Middle Office | Process Raw Exposure (FTREX1) | Raw exposure has been created and released. |
| [Take Snapshot](#unique_10) [page ] 24 | Treasury Specialist - Middle Office | Take Snapshot (TOESNAP) | Snapshot of exposures has been created. |
| [Review Net Open Exposure in Hedge Management Cockpit](#unique_11) [page ] 25 | Treasury Specialist - Middle Office | Hedge Management Cockpit (TOENE) | Exposure, net exposure, net open exposure has been reviewed in app Hedge Management Cockpit. |
| [Create Original Foreign Exchange Contract with Hedging Classification](#unique_12) [page ] 26 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) | The original FX forward transaction has been created. |
| [Automatically Create Original Hedging Relationship (Planned Designation)](#unique_13) [page ] 28 | Treasury Specialist - Back Office | Manage Hedging Relationships (TPM100) Process Spots/Forwards - Collective Processing (TX06) Reprocess Transactions - Automated Designation (TPM104) | The original hedging relationship (contains original FX forward transaction) has been created in status 'Planned Designation'. |
| [Set Contract Settlement Status with Incoming Confirmation](#unique_14) [page ] 33 | Treasury Specialist - Back Office | Process Spots/Forwards - Collective Processing (TX06) | Status of the original FX forward transaction becomes 'Contract Settlement'. |
| [Release Original Hedging Relationship](#unique_15) [page ] 34 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120) | The original hedging relationship has been released. |
| [Period End Closing Before Swap](#unique_16) [page ] 36 |  |  |  |
| [Calculate NPV of Hedging Instrument and Hypothetical Derivative](#unique_17) [page ] 36 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA) | NPV and market value components have been calculated at period end for original FX transaction and relevant hypothetical derivative. |
| [Run Key Date Valuation](#unique_18) [page ] 38 | Treasury Accountant | Run Valuation (TPM1) Reverse Valuation (TPM2) | Valuation posting has been created for original FX transaction at period end. |
| [Run Classification](#unique_19) [page ] 39 | Treasury Accountant | Run Classification (TPM101) | Classification postings have been created on Exposure Subitem level of original hedging relationship at period end. |
| [Create Raw Exposure for Overhedge Situation](#unique_20) [page ] 41 | Treasury Specialist - Middle Office | Process Raw Exposure (FTREX1) | New raw exposure has been created to transfer the exposure position from original period to a new period. |
| [Take Snapshot](#unique_21) [page ] 43 | Treasury Specialist - Middle Office | Take Snapshot (TOESNAP) | Snapshot has been created to reflect the transfer of exposure from original period to new period. |
| [Create and Submit Swap Request in Hedge Management Cockpit](#unique_22) [page ] 43 | Treasury Specialist - Middle Office | Hedge Management Cockpit (TOENE) | A swap request has been created and submitted. |
| [Release Swap Request](#unique_23) [page ] 44 | Treasury Specialist - Middle Office | Process Hedge Requests (TOEHREQO) | Swap request has been released. |
| [Create FX Swap Transactions](#unique_24) [page ] 45 | Treasury Specialist - Front OfficeTreasury Specialist - Back Office | Create FX Spot/Forward (TX01) Create Reference (TBR6) Create FX Swap (TX10) | Two legs of FX swap have been created, swap reference for them has been saved. |
| [Automatically Update Original Hedging Relationship and Create New Hedging Relationship (Planned Designation)](#unique_25) [page ] 51 | Treasury Specialist - Back Office | Manage Hedging Relationships (TPM100) | The original hedging relationship has been updated; the new hedging relationship has been created. |
| [Set Contract Settlement Status for FX Swap Transactions with Incoming Confirmations](#unique_26) [page ] 56 | Treasury Specialist - Back Office | Process Spots/Forwards - Collective Processing (TX06) | Status of two legs of FX swap transaction becomes 'Contract Settlement'. |
| [Process Hedging Relationships at Swap Date](#unique_27) [page ] 57 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120) | The original and new hedging relationships have been processed properly at the swap date. |
| [Period end Closing between Swap Date and Maturity of Original FX Transaction](#unique_28) [page ] 59 |  |  |  |
| [Calculate NPV of Hedging Instruments and Hypothetical Derivatives](#unique_29) [page ] 60 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA) | NPVs and market value components have been calculated at period end for all transactions and hypothetical derivatives in original and new hedging relationships. |
| [Run Key Date Valuation](#unique_30) [page ] 61 | Treasury Accountant | Run Valuation (TPM1) Reverse Valuation (TPM2) | Valuation postings have been created for original FX transaction and two legs of FX swap transaction. |
| [Run Classification](#unique_31) [page ] 63 | Treasury Accountant | Run Classification (TPM101) | Classification postings have been created on Exposure Subitem level of original and new hedging relationships at period end. |
| [Process Reclassification for Original Hedging Relationship at Balance Sheet Recognition Date](#unique_32) [page ] 64 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120) | Original hedging relationship has been processed at its balance sheet recognition date for crossover. |
| Contract Maturity for Original FX Transaction and Offsetting FX Transaction: |  |  |  |
| [(1X1) Foreign Currency Risk Management and (1X9) Foreign Currency Risk Management – Group Ledger IFRS](#unique_33) [page ] 67 | Treasury Specialist - Back Office;Treasury Accountant | Fix, Pay and Post Flows (TBB1) Automatic Payment Transactions for Payment Requests (F111) Process Business Transactions (TPM10) Post Derived Business Transactions (TPM18) | The postings for closing original FX transaction and offsetting leg of FX swap have been created in operative valuation area AE0 and parallel valuation area 002. |
| [Process Hedging Relationships at Maturity Date of Original FX Transaction and Offsetting FX Transaction](#unique_34) [page ] 68 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120) | Hedging Business Transactions have been processed at the maturity date of hedging instruments. |
| [Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date of Original Hedging Relationship](#unique_35) [page ] 71 | Treasury Accountant | Post Derived Business Transactions (TPM18) | Reclassification postings have been created and relevant flows have been fixed at the end date of exposure subitem of original hedging relationship. |
| [Period end Closing after Maturity of Original and Offsetting FX Transactions](#unique_36) [page ] 73 |  |  |  |
| [Calculate NPV of Hedging Instrument and Hypothetical Derivative](#unique_17) [page ] 36 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA) | NPV and market value components have been calculated at period end for securing leg in new hedging relationships. |
| [Run Key Date Valuation](#unique_37) [page ] 75 | Treasury Accountant | Run Valuation (TPM1) Reverse Valuation (TPM2) | Valuation posting has been created for securing leg in new hedging relationships. |
| [Run Classification](#unique_38) [page ] 76 | Treasury Accountant | Run Classification (TPM101) | Classification postings have been created on Exposure Subitem level of new hedging relationships at period end. |
| [Process Reclassification for New Hedging Relationship at Balance Sheet Recognition Date](#unique_39) [page ] 78 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120) | New hedging relationship has been processed at its balance sheet recognition date for crossover. |
| Contract Maturity for Securing FX Transaction: |  |  |  |
| [(1X1) Foreign Currency Risk Management and (1X9) Foreign Currency Risk Management – Group Ledger IFRS](#unique_40) [page ] 80 | Treasury Specialist - Back Office;Treasury Accountant | Fix, Pay and Post Flows (TBB1) Automatic Payment Transactions for Payment Requests (F111) Reprocess Transactions - Automated Designation (TPM104) Post Derived Business Transactions (TPM18) | The postings for closing of securing leg of FX swap have been created in operative valuation area AE0 and parallel valuation area 002. |
| [Process Dedesignation for New Hedging Relationship at Maturity Date of Securing FX Transaction](#unique_41) [page ] 81 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120) | Hedging Business Transaction has been processed at the maturity date of securing leg of FX swap. |
| [Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date of New Hedging Relationship](#unique_42) [page ] 84 | Treasury Accountant | Post Derived Business Transactions (TPM18) | Reclassification postings have been created and relevant flows have been fixed at the end date of exposure subitem of new hedging relationship. |
| [Display Treasury Position Flows](#unique_43) [page ] 86 | Treasury Accountant | Display Treasury Position Flows (F1754) | Position flows for FX transaction and exposure subitem are checked. |
| [Display Treasury Posting Journal](#unique_44) [page ] 86 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Posting journals for FX transaction and exposure subitem are checked. |
| [Display Treasury Position Values](#unique_45) [page ] 87 | Treasury Accountant | Display Treasury Position Values (F1867) | Position values for FX transaction and exposure subitem are checked. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Overhedge Processing - FX Swap

Purpose

This section covers the Hedge Management and Hedge Accounting process for forecast cashflows in foreign currencies according to a company’s hedging policy, and the hedging instruments are FX forward contracts, and near and far legs in FX swap transactions.

The treasury department is responsible for executing a given hedging policy for hedging the risk of forecast cashflows in foreign currencies of future periods. The forecast itself is represented as exposures in the Hedge Management Cockpit. A snapshot is taken for the forecast exposures from Exposure Management. Based on the snapshot, net open exposure amount, risk currency and period are detailed in the Hedge Management Cockpit. Based on rules of the hedging policy, the net open exposures are reduced by trading financial instruments like a FX forward transaction. In case of expected inflows of a risk currency, the resulting exposure shall be closed by a FX forward that sells the inflow currency and buys the local currency of the company code; in case of expected outflows, a FX forward transaction is traded that buys the outflow currency and sells the local currency.

With the creating of the FX forward transaction, the financial transaction is automatically designated into a Hedging Relationship as Hedging Instrument together with the exposure item of the Hedge Management Cockpit as Hedged Item: The matching exposure item is determined based on characteristics of the Hedging Instrument, e.g. hedging classification, position currency of financial transaction, maturity of financial transaction. At the same time, the Hypothetical Derivative is created and all necessary mathematical evaluations necessary for the measurement of ineffectiveness are performed and stored.

At period end, the determination of NPVs including the decomposition of market values for Hedging Instrument and the Hypothetical Derivative is performed, and the key date valuation of the FX forward transactions is executed, meanwhile the measurement and postings of the Hedging Reserve (OCI I), Cost of Hedging Reserve (OCI II) and ineffectiveness are executed on exposure subItem level. The period end close can be executed using two different procedures: valuation and classification with Reset or without Reset.

With the transfer of forecast cashflow from one exposure period to another exposure period an overhedge situation occurs for the original exposure period. A FX Swap Transaction is created based on the information of a Swap Request to transfer the Hedging Instrument from the original exposure period to the new exposure period. As a result, the overhedge situation is solved with a FX Swap Transaction which is processed in the following Period End Close.

At the Balance Sheet Recognition Date, the Reclassification Flows are automatically created; depending on the rule which was set in the Hedging Area Definition, the Reclassification Flows are posted immediately or at the Exposure Subitem End Date or at a Deviant Reclassification Date.

With the maturity of the FX forward transaction, the cumulated Hedging Reserve and Cost of Hedging Reserve amounts are classified as frozen. At the end date of the Exposure Subitem, the cumulated Hedging Reserve and Cost of Hedging Reserve amounts are to be reclassified to profit or loss as a reclassification adjustment.

#### Define or Adjust Hedging Area

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The hedging area is an entity that represents a section of hedging policy of the company. The creation of a hedging area is required to start the process of Hedge Management and Hedge Accounting. It is the central steering entity that contains all relevant settings for this process.

|  |
| --- |
| Note In this section, as an example, one single Hedging Area HA0003 for Hedge Accounting is created. During testing, HA0003 can be shared by different company codes from different countries with different local currencies.As the first tester to run this test script in system, create a Hedging Area HA001 by following Option 1: Create a New Hedging Area.If you find out that the Hedging Area HA0003 already exists in the system, create a new version for HA0003 and extend it by entering specific parameters of your company code/country, using Option 2: Extend an Existing Hedging Area.A company can have multiple hedging areas for Hedge Accounting according to its hedging policy. However, a hedge-accounting-relevant Hedging Classification can only be assigned to one Hedging Area for Hedge Accounting. Creating additional Hedging Area means the necessity of defining additional Hedging Classifications. Hedging Classification is a configuration that should be done via configuration step Define Hedging ClassificationsNote Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

|  |
| --- |
| Note Eight Hedging Classifications are predefined for IFRS 9 Cash Flow Hedge of FX risk by using FX Forwards:YFC00: Spot Element of FX forward contract is Hedging Reserve (OCI I), Forward Element and Cross Currency Basis Spread of FX forward contract is Cost of Hedging Reserve (OCI II); Valuation will be carried out when releasing the designation. YFC00 should be always bundled with Hedging Profile F00 when maintaining tab Hedge Accounting II of a Hedging Area.YFC01: Spot Element of FX forward contract is Hedging Reserve (OCI I), Forward Element and Cross Currency Basis Spread of FX forward contract is Cost of Hedging Reserve (OCI II): No valuation will be carried out when releasing the designation. YFC01 should be always bundled with Hedging Profile F01 when maintaining tab Hedge Accounting II of a Hedging Area.YFC02: Spot Element and Forward Element of FX forward contract is Hedging Reserve (OCI I), Cross Currency Basis Spread of FX forward contract is Cost of Hedging Reserve (OCI II); Valuation will be carried out when releasing the designation. YFC02 should be always bundled with Hedging Profile F02 when maintaining tab Hedge Accounting II of a Hedging Area.YFC03: Spot Element and Forward Element of FX forward contract is Hedging Reserve (OCI I), Cross Currency Basis Spread of FX forward contract is Cost of Hedging Reserve (OCI II); No valuation will be carried out when releasing the designation. YFC03 should be always bundled with Hedging Profile F03 when maintaining tab Hedge Accounting II of a Hedging Area.YFC04: Spot Element of FX forward contract is Hedging Reserve (OCI I), Forward Element, Cross Currency Basis Spread and Others Element of FX forward contract is Cost of Hedging Reserve (OCI II); Valuation will be carried out when releasing the designation. YFC04 should be always bundled with Hedging Profile F04 when maintaining tab Hedge Accounting II of a Hedging Area.YFC05: Spot Element of FX forward contract is Hedging Reserve (OCI I), Forward Element, Cross Currency Basis Spread and Others Element of FX forward contract is Cost of Hedging Reserve (OCI II): No valuation will be carried out when releasing the designation. YFC05 should be always bundled with Hedging Profile F05 when maintaining tab Hedge Accounting II of a Hedging Area.YFC06: Spot Element and Forward Element of FX forward contract is Hedging Reserve (OCI I), Cross Currency Basis Spread and Others Element of FX forward contract is Cost of Hedging Reserve (OCI II); Valuation will be carried out when releasing the designation. YFC06 should be always bundled with Hedging Profile F06 when maintaining tab Hedge Accounting II of a Hedging Area.YFC07: Spot Element and Forward Element of FX forward contract is Hedging Reserve (OCI I), Cross Currency Basis Spread and Others Element of FX forward contract is Cost of Hedging Reserve (OCI II); No valuation will be carried out when releasing the designation. YFC07 should be always bundled with Hedging Profile F07 when maintaining tab Hedge Accounting II of a Hedging Area.Only hedging classifications YFC04 - YFC07 are used in hedging area HA0003; YFC00 - YFC03 is assigned to another hedging area HA0001 that is described in test script Hedge Accounting for FX Forward – Group Ledger IFRS. In a real business environment, YFC00 - YFC07 can be assigned to single hedging area. |

|  |
| --- |
| Note 1 Hedging Classifications is predefined for handling the overhedge situation by using FX swap:YFC40: the hedging profile of the new hedging relationship (containing FX swap transactions) is copied from the original hedging relationship, so the YFC40 doesn't specify components splitting between Hedging Reserve (OCI I) and Cost of Hedging Reserve (OCI II). |

Procedure

Option 1: Create a New Hedging Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Define Hedging Area (TOE_HEDGING_AREA). | The Display Hedging Area view displays. |  |
| 3 | Enter Hedging Area ID | Enter the following data and choose Create:Hedging Area: for example, HA0003 | The Create Hedging Area dialog box displays.If the system displays the message Hedging area HA0003 already exists, skip Option 1 and execute Option 2: Extend an Existing Hedging Area. If you find the parameters mentioned in Option 2 are maintained, you can also skip Option 2. |  |
| 4 | Enter Data in Dialog Box Create Hedging Area | Enter the following data and choose Create:Hedging Area: for example, HA0003Description: <for example, Hedging Area for Hedge Accounting using FX Forward and Swap>Authorization Group: for example, HAG01Valid From: for example, <first day of current year>Without Template: Selected | The Change Hedging Area view displays. |  |
| 5 | Enter Data on Tab Main Data | On the Main Data tab, enter the following data:Local Currency: <choose this radio button>Calendar Related: SelectedNumber of Periods: for example, 12Period Length: for example, MonthHedge Accounting: <choose this checkbox>Product Type for Exposure Subitems: 91AActivate SAP Trading Platform Integ.: <Choose this checkbox>.You only choose this checkbox in case of testing integration with trading platform. | You maintained the data. |  |
| 6 | Enter Data on Tab General Settings | Choose the General Settings tab.Enter the following data:Company Code: for example, 3310In the Differentiation Criteria area: for example, select the checkbox of differentiation criteria Currency and Company CodeIn the Hedging Classification area:Choose Add Hedging Classification.Enter the following data:Hdg Class.DescriptionYFC04FX Risk; CFH; Spot, Forward+CCBS+Others; with 1st Day ResultYFC05FX Risk; CFH; Spot, Forward+CCBS+Others; w/o 1st Day ResultYFC06FX Risk; CFH; Forward+Spot, CCBS+Others; with 1st Day ResultYFC07FX Risk; CFH; Forward+Spot, CCBS+Others; w/o 1st Day ResultYFC40FX Risk; CFH; Overhedge Processing - FX Swap | You maintained the data. |  |
| 7 | Enter Data on Tab Currencies | Choose the Currencies tab.In the Hedging-Relevant Currencies pane, choose Add Currency.Enter the currencies to be used as risk currencies in later steps in current test script (for example,USD) | You maintained the data. |  |
| 8 | Enter Data on Tab Filters for Exposures | Choose the tab Filters for Exposures.in the sub-area Filter List for Exposures, choose Create Filter.In the dialog box New Filter for Exposures, enter the following data and choose Create Filter:Filter: for example, FLT_EXPFilter Description: for example, Filter for ExposuresSource: E_EM2In the sub-area Other Filter - Specific Selections , enter the following data:Exposure Position Type: YFXNoteYou may also use E_FXEM Foreign Exchange Exposure Management instead of E_EM2 Exposure Management 2.0 as the data source for exposures.If you use E_FXEM Foreign Exchange Exposure Management as the data source for exposures, you will have to use app Manage FX Exposures (F7990) instead of app Process Raw Exposure (FTREX1) to create and submit the FX Exposure. | You maintained the data. |  |
| 9 | Enter Data on Tab Filters for Hedges | Choose the tab Filters for Hedges.In the sub-area Filter List for Hedges, choose Create Filter.In the dialog box New Filter for Hedges, enter the following data and choose Create Filter:Filter: for example, FLT_HDGFilter Description: for example, Filter for HedgesSource: H_TMIn the sub-area Other Filter - Specific Selections, enter the following data:Product Type: firstly enter 60A, then choose button Multiple selection of filed Product Type. In the dialog box Multiple Selection for Product Type, add another product type 60B, and choose Copy (F8). | You maintained the data. |  |
| 10 | Enter Data on Tab Hedge Accounting I | Choose the tab Hedge Accounting I.In sub-area Designation Level, choose Insert, and enter the following data:Company Code: for example, 3310Valuation Area: 002Designation Level: choose G (Gross Exposure Item with Larger Absolute Value) if it is not selected by defaultSplitting: for example, 1 (Active)Sequence: for example, N (No Consumption Sequence)In sub-area Designation Activation, choose Insert, and enter the following data:CoCodeVAR-CurrencyDesig.3310002USD1 (Active)In sub-area Designation Splitting, choose Insert, and enter the following data:Company Code: for example, 3310Valuation Area: 002Risk Currency: for example, USDDirection: for example, I (Incoming)Split ID: for example, 1Splitting Ratio: for example, 100Reclassification Offset Category: for example, 4 (Due Date HInst + PT)Balance Sheet Recognition: 2 (Reclassification at the End Date of the Exposure Subitem)Extend Hypothetical Derivative Period: for example, 1 (Yes)Payment Term (Days): for example, 5Note Split ID is the numerical identifier that is used to number the different designation splits: 1, 2, 3, etc.The sum of the splitting ratios of corresponding Split IDs for a specific combination of Company Code, Valuation Area, Risk Currency, and Direction should be 100.Note With the Reclassification Offset Category, you define the date on which the reclassification of Hedging Reserve and Cost of Hedging Reserve, for example, when 4 (Due Date HInst + PT) is selected, reclassification date = maturity date of hedging instrument + payment term.Note Only enter a value for Balance Sheet Recognition when your scenario is balance sheet crossover (from Cash Flow Hedge to Fair Value Hedge), The Balance Sheet Recognition Date = Maturity Date of Hedging Instrument - Payment Term.The different types of reclassification depend on the company code and distinguish the reclassification of Hedging Reserve and Cost of Hedging Reserve amounts which were classified for the Hedging Relationship up to and equal to the Balance Sheet Recognition Date:1 - Immediate Reclassification at Balance Sheet Recognition Date2 - Reclassification at the End Date of the Exposure Subitem: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until end date of the Exposure Subitem.3 - Reclassification at Deviant Reclassification Date: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until the Deviant Reclassification Date = Due Date of Hedging Instrument + DIO (Days Inventory Outstanding) - Payment Term.Note When you choose to extend the period of the hypothetical derivative (value for field Extend Hypothetical Derivative Period is 1 - Yes), the due date of the hypothetical derivative = maturity date of the hedging instrument + payment term. If you do not want to extend the hypothetical derivative period, the due date of the hypothetical derivative = maturity date of the hedging instrument. | You maintained the data. |  |
| 11 | Enter Data on Tab Hedge Accounting II | Choose the tab Hedge Accounting II.In sub-area Designation Control, choose Insert, and enter the following data:CoCodeVAHdg Class.Des. TypePType ESIHdgProfileMDS ID3310002YFC04YFX1WF043310002YFC05YFX1WF053310002YFC06YFX1WF063310002YFC07YFX1WF073310002YFC40YFXSWF05Note YFX1W, YFXSW are designation types don't require counterconfirmation. There are other designation types YFX1C, YFXSC which require counterconfirmation.When using YFX1C or YFXSC, hedging relationship can be released only after the corresponding hedging instrument has been successfully counterconfirmed, which requires to use correspondence functionality.PType ESI is to assign different product types for different exposure items classified by hedging classification. If you want to use just one product type maintained in the Main Data tab for all exposure items, please keep field PType ESI blank here.MDS ID (Market Data Set ID) is used for Effectiveness Test, leave the column MDS ID blank since Test Procedures do not include process steps of Effectiveness Test. Furthermore, special hedging profile should be used for Effective Test, You can find more details regarding Effective Test for FX forward as hedging instrument in Appendix – Effectiveness Test of test script 1XD. SAP only pre-delivers S00 as a Hedging Profile for FX forward in which effectiveness test is enabled, if you need more Hedging Profiles with effectiveness test, use the SSCUI Define Hedging Profiles. | You maintained the data. |  |
| 12 | Save the Hedging Area | Choose Save (Ctrl+S). | The system displays the message Hedging area HA0003 version 001 saved.The Hedging Area for Hedge Accounting is created successfully. |  |

Option 2: Extend an Existing Hedging Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Define Hedging Area (TOE_HEDGING_AREA). | The Display Hedging Area view displays. |  |
| 3 | Enter Hedging Area ID | On the Display Hedging Area view, enter the following data and choose Display:Hedging Area: for example, HA0003 | Hedging Area HA0003 is displayed. |  |
| 4 | Create New Version | Choose New Version.In the dialog box Create New Version of Hedging Area HA0003, enter the following data and choose Create:Valid From: for example, <current date> | The Change Hedging Area view displays. |  |
| 5 | Update Data on Tab General Settings | Choose the tab General Settings, choose the button Multiple selection of field Company Code.In the dialog box Multiple Selection for Company Code, add company code 3310 into the area Select Single Values, and choose Copy (F8). | Data on tab General Settings has been updated. |  |
| 6 | Update Data on Tab Currencies | Choose the tab Currencies.In sub-area Hedging-Relevant Currencies, choose Add Currency, and enter the currencies (if they have not been maintained) which will be used as risk currencies in later steps in current test script. For example:USD | Data on tab Currencies has been updated. |  |
| 7 | Update Data on Tab Hedge Accounting I | Choose the tab Hedge Accounting I.In sub-area Designation Level, choose Insert, and enter the following data:Company Code: for example, 3310Valuation Area: 002Designation Level: choose G (Gross Exposure Item with Larger Absolute Value) if it is not selected by defaultSplitting: for example, 1 (Active)Sequence: for example, N (No Consumption Sequence)In sub-area Designation Activation, choose Insert, and enter the following data:CoCodeVACurrencyDesig.3310002USD1 (Active)In sub-area Designation Splitting, choose Insert, and enter the following data:Company Code: for example, 3310Valuation Area: 002Currency: for example, USDDirection: for example, I (Incoming)Split ID: for example, 1Ratio: for example, 100Reclassification Offset Category: for example, 4 (Due Date HInst + PT)Balance Sheet Recognition: 2 (Reclassification at the End Date of the Exposure Subitem)Extend Hypothetical Derivative Period: for example, 1 (Yes)Payment Term (Days): for example, 5Note Split ID is the numerical identifier that is used to number the different designation splits: 1, 2, 3, etc.The sum of the splitting ratios of corresponding Split IDs for a specific combination of Company Code, Valuation Area, Risk Currency, and Direction should be 100.Note With the Reclassification Offset Category, you define the date on which the reclassification of Hedging Reserve and Cost of Hedging Reserve, for example, when 4 (Due Date HInst + PT) is selected, reclassification date = maturity date of hedging instrument + payment term.Note Only enter a value for Balance Sheet Recognition when your scenario is balance sheet crossover (from Cash Flow Hedge to Fair Value Hedge), The Balance Sheet Recognition Date = Maturity Date of Hedging Instrument - Payment Term.The different types of reclassification depend on the company code and distinguish the reclassification of Hedging Reserve and Cost of Hedging Reserve amounts which were classified for the Hedging Relationship up to and equal to the Balance Sheet Recognition Date:1 - Immediate Reclassification at Balance Sheet Recognition Date2 - Reclassification at the End Date of the Exposure Subitem: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until end date of the Exposure Subitem.3 - Reclassification at Deviant Reclassification Date: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until the Deviant Reclassification Date = Due Date of Hedging Instrument + DIO (Days Inventory Outstanding) - Payment Term.Note When you choose to extend the period of the hypothetical derivative (value for field Extend Hypothetical Derivative Period is 1 - Yes), the due date of the hypothetical derivative = maturity date of the hedging instrument + payment term. If you do not want to extend the hypothetical derivative period, the due date of the hypothetical derivative = maturity date of the hedging instrument. | Data on tab Hedge Accounting I has been updated. |  |
| 8 | Update Data on Tab Hedge Accounting II | Choose the tab Hedge Accounting II.In sub-area Designation Control, choose Insert, and enter the following data:CoCodeVAHdg Class.Des. TypePType ESIHdgProfileMDS ID3310002YFC04YFX1WF043310002YFC05YFX1WF053310002YFC06YFX1WF063310002YFC07YFX1WF073310002YFC40YFXSWF05Note YFX1W, YFXSW are designation types don't require counterconfirmation. There are other designation types YFX1C, YFXSC which require counterconfirmation.When using YFX1C or YFXSC, hedging relationship can be released only after the corresponding hedging instrument has been successfully counterconfirmed, which requires to use correspondence functionality.MDS ID (Market Data Set ID) is used for Effectiveness Test, leave the column MDS ID blank since Test Procedures do not include process steps of Effectiveness Test. Furthermore, special hedging profile should be used for Effective Test, You can find more details regarding Effective Test for FX forward as hedging instrument in Appendix – Effectiveness Test of test script 1XD. SAP only pre-delivers S00 as a Hedging Profile for FX forward in which effectiveness test is enabled, if you need more Hedging Profiles with effectiveness test, use the SSCUI Define Hedging Profiles. | Data on tab Hedge Accounting II has been updated. |  |
| 9 | Save the Hedging Area | Choose Save (Ctrl+S). | Message Hedging area HA0003 version XXX saved displayed.The Hedging Area for Hedge Accounting has been extended to support your company code/country testing successfully. |  |

#### Create Raw Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Middle office collects exposure data based on forecast cash flows in risk currencies from various sources, and consolidate the exposures data which should be ready to be entered SAP system as Raw Exposures. The exposure data should be aggregated in granularity which differentiates:

- Company code
- Risk currency
- The period in which exposure will due

The creation and subsequent release of a Raw Exposure leads to the creation of a derived Exposure Position (automatic released).

|  |
| --- |
| Note As an example, how to manually key in Raw Exposure is introduced in current step. Besides manually key in Raw Exposure, you can also import Raw Exposures from spreadsheet, for details please see Option 2: Import the raw exposures from spreadsheet of step Create Raw Exposure in test script Foreign Currency Risk Management. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Raw Exposure (FTREX1). | The Raw Exposure: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | On the Raw Exposure: Initial Screen, enter the following data and choose Create.Exposure Activity Type: for example: YFXIIf the direction of consolidated FX exposure is outgoing, use Exposure Activity Type YFXO. | The Raw Exposure Maintenance: Create screen displays. |  |
| 4 | Enter Header Data | On the Raw Exposure Maintenance: Create screen and tab Header Data, enter the following data:Default Exposure Category: for example, 01 (Forecasted Transaction)Company Code: for example, 3310Cirt4ExpPosType: FX (FX Exposure)Direction: for example, IN (Incoming Cash Flow)Cirt4ExpPosType is a criterion used to derive the Exposure Position Type YFX which you entered on tab Filters for Exposures of Hedging Area.If you use Exposure Activity Type YFXO on previous screen, please enter Direction OUT (Outgoing Cash Flow) on this screen. | Necessary header data is entered. |  |
| 5 | Enter Line Item Data | Choose tab Line Item Data.In sub-area Raw Exposure Line Item, choose Create New Line Item, and enter the following data:Exposure Due Date: for example: <Current date + 2 Months>Exposure Amount: for example, 1000000Exposure Amount Currency: for example, USDTarget Currency: for example, AED | Necessary line item data is entered. |  |
| 6 | Save Raw Exposure | Choose Save. | A dialog box displays, and states that:Raw exposure has been saved;Raw exposure has been released;Position IDs have been updated.You can check Exposure Position and Exposure Position Flows via app Process Exposure Positions (FTREX12) and Display Exposure Position Flows. |  |

#### Take Snapshot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You take a snapshot of the exposure data belonging to specific hedging area. For the subsequent process of Hedge Management and Hedge Accounting, it is mandatory to rely on fully versioned data. This ensures that at all times an auditor can check which data served as the basis for a hedging decision.

The selected incoming or outgoing exposures and the exposure items are saved on the database, and can be review in app Hedge Management Cockpit (TOENE) in next step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Take a Snapshot | Open Take Snapshot (TOESNAP). | The Take Snapshot screen is displayed. |  |
| 3 | Enter General Selections | On the Take Snapshot (TOESNAP)screen, enter the following data and choose Run:Hedging Area: for example, HA0003Description: for example, snapshot for hedge accounting using FX forwardDay Reference: <select this checkbox> | The Display logs screen is displayed and the snapshot is created. |  |

#### Review Net Open Exposure in Hedge Management Cockpit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Review the exposure data in the app Hedge Management Cockpit (TOENE) based on the snapshot you took in previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Hedge Management Cockpit (TOENE). | The Hedge Management Cockpit for Hedging Area screen displays. |  |
| 3 | Enter Selection Criteria | On the Hedge Management Cockpit for Hedging Area screen, enter the following data and choose Start:Hedging Area: for example: HA0003Layout ID: for example, 1R_ALL_CHYou can also choose alternative layout ID 1C_CURR_OV - Currency Pairs Overview (Key Figures in Columns) or 1C_ALL_CH - All Characteristics (Key Figures in Columns).Choose Manage Layouts, you can create new layout on next screen Layout Overview, | The Hedge Management Cockpit for Hedging Area HA0003 displays.You can see the amounts of exposures have been reflected in specific cells for differentiation criteria of raw exposures you created previously (company code, risk currency, period of due date, incoming/outgoing indicator of Exposure Activity Type).Choose a cell, you can click Drilldown (cell) to display more detailed information of Exposure Item, Exposure Position, Raw Exposure. |  |

#### Create Original Foreign Exchange Contract with Hedging Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a FX forward transaction which is the original hedging instrument before occurrence of overhedge.

The saving of the FX Transaction with a Hedge Accounting-specific Hedging Classification initiates the Hedge Accounting processing:

- According to the Contract Start Date and Hedging Classification, a valid Hedging Area is determined.
- According to the differentiating criteria (currency, company code, etc.) of the Hedging Area and by means of the Contract Start and Value Date, the Exposure Item of the Snapshot is determined.
- According to the settings of the Designation Splitting of the Hedging Area, one Hedging Relationship or multiple Hedging Relationships are created.

Prerequisites

Business partner has been created, please see section [Business Conditions](#unique_6) [page ] 6.

If you used the Designation Type which requires counterconfirmation in step [Define or Adjust Hedging Area](#unique_8) [page ] 12, hedging relationship can be released only after the FX transaction has been successfully counterconfirmed, you need to run the correspondence process which will set the status of FX transaction to 'Counterconfirmed' automatically after receiving the incoming confirmation from counterparty, and correspondence setting should be maintained for business partner before creating a FX transaction (please see section [Business Conditions](#unique_6) [page ] 6).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Spot/Forward Transaction Entry: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: 60ATransaction Type: 102Partner: for example, 33537001 | The Spot/Forward Transaction Entry: Structure screen displays. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Rate: for example, AED/USD1.15Buy/Sell: for example, SellTraded Amt: for example, USD800000Value Date: for example, <Current date + 2 Months>Contract Date: for example, <Current date>The currency of Traded Amt should be the risk currency. The amount of Traded Amt should be less or equal to the amount of Raw Exposure Line Item for this risk currency you created previously.The Value Date of FX transaction should be within the same period as the due date of exposure.You Buy risk currency (Traded Amt) if it is outgoing exposure. | Data on tab Structure has been entered. |  |
| 5 | Enter Data in Administration tab | Choose tab Administr., and enter the following data:Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: for example, YFC05 (FX Risk; CFH; Spot, Forward+CCBS+Others; w/o 1st Day Result)Note The appropriate General Valuation Class will derive the correct Position Management Procedure for Hedge Accounting in valuation area 002 for IFRS.In operative valuation area AE0, a Position Management Procedure for non-Hedge Accounting is determined. | Data on tab Administr. has been entered. |  |
| 6 | Save the FX Transaction | Choose Save. | Dialog box Document lines: Display messages displays, and shows NO warning message Reprocessing of financial transaction required after save about auto designation could not be finished.Choose Continue (Enter), message Financial transaction saved under number XXXXXXXXXXXXX displays.Note down the transaction number of this original FX Forward Transaction. |  |

|  |
| --- |
| Note After the FX transaction is saved, you can logon as Treasury Specialist - Middle Office and open app Hedge Management Cockpit to check the net open exposure again.In app Hedge Management Cockpit (TOENE), the amounts of FX transactions will be reflected in corresponding cells for Key Figure Name Net Hedges and relevant company code, risk currency and period; Net Open Exposure should be reduced accordingly. |

#### Automatically Create Original Hedging Relationship (Planned Designation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With saving the FX forward transaction, the Exposure Item in a snapshot is found and the Hedging Relationship is automatically created in status ‘Planned Designation’, the Exposure Item is determined based on attributes of the relevant Snapshot and Hedging Area and FX forward transaction.

This step introduces how to check the automatically created Hedging Relationship.

|  |
| --- |
| Note The automated designation of a FX transaction into a hedging relationship is prevented if the calculated Balance Sheet Recognition Date is earlier than or on the same date as the Designation Date (Contract Date), and the portion of the FX Transaction is processed as freestanding position. |

Procedure

Option 1: via app Manage Hedging Relationships

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as aTreasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Manage Hedging Relationships (TPM100). | The P-Hedge Accounting screen displays. |  |
| 3 | Enter Selection Criteria | On the P-Hedge Accounting screen, choose tab Selection on the left side of screen, and enter the following data:Find: All Hedging RelationshipsBy: Hedging InstrumentCompany Code: for example, 3310Valuation Area: 002Product Group: select the checkbox of OTC Trans., and choose the button OTC Transactions Selection beside OTC Trans.. In the dialog box OTC Transactions Selection, enter the transaction number of the Original FX Forward Transaction you noted down in previous step, then choose Continue (Enter).Choose Start. | The list of Hedging Relationship Number(s) displays on bottom-left side of screen. You may need to zoom out the screen in web browser to see it.Note down the Hedging Relationship Number of this Original Hedging Relationship. |  |
| 4 | Display Header of Hedging Relationship | Double click a HR Number from bottom-left side of screen, the detailed information of Hedging Relationship will display on right side of screen.Check the data of Hedge Relationship Header. | The header of Hedging Relationship displays on upper-right side of screen, it provides details which are relevant for the Hedging Relationship as general entity.The Hedging Relationship Status should be ‘Planned Designation’ since it has not been released.Choose Display All Flows, you can check the created flows resulting from the Designation.Choose Display H.Rel. Related Trans, in Hedge Related Transactions for Hedging Relationship dialog box, double click the row of Business Transaction Category Designation, then you can see the designation details in Designation of Hedging Relationship dialog box. |  |
| 5 | Display Tab Hedging Relationship Detail | Check the data of tab Hedge Relationship Details. | Tab Hedging Relationship Detail contains information about:Risk Type and Risk Profile DetailsDate information on Hedging Relationship levelThe following fields are automatically populated:Risk Currency: your exposure currencyProfile: the Hedging Profile which is mapped (on tab Hedge Accounting II of Hedging Area) to the Hedging Classification you used when created FX transaction.Category: Cash Flow HedgeRisk Indicator: Currency RiskValid-From Date: contract date of FX TransactionPlanned Designation Date: contract date of FX TransactionPlanned Dedesign. Date: Value Date of FX TransactionBal.Sheet Rec.Date: the Balance Sheet Recognition Date of crossoverReclassification Date: the Deviant Reclassification Date other than the Balance Sheet Recognition Date and the End Date of the Exposure Subitem, the Deviant Reclassification Date = Due Date of Hedging Instrument + DIO (Days Inventory Outstanding) - Payment Term.Note down the Balance Sheet Recognition Date.Designation Type: the Designation Type which is mapped (on tab Hedge Accounting II of Hedging Area) to the Hedging Classification you used when created FX transactionNote The Balance Sheet Recognition Date is only available when you gave value 1, 2 or 3 for the field Balance Sheet Recognition in sub-area Designation Splitting on tab Hedge Accounting I of the Hedging Area.The Reclassification Date is only available when you gave value 3 for the field Balance Sheet Recognition in sub-area Designation Splitting on tab Hedge Accounting I of the Hedging Area. |  |
| 6 | Display Tab Hedged Item | Choose tab Hedged Item, and check data of it. | Tab Hedged Item contains information about:Hedged Item DetailsPosition Management information of the Exposure SubitemThe following fields are automatically populated:Number: generated number. Note down the Hedged Item Number.Start Date: contract date of FX TransactionEnd Date: it is determined by the parameters you entered in sub-area Designation Splitting on tab Hedge Accounting I of the Hedging Area, it is the date on which reclassification of OCI I and OCI II should carry out (except the case that Immediate Reclassification at Balance Sheet Recognition Date, or Reclassification at Deviant Reclassification Date). Note down this Exposure Subitem End date of original Hedging Relationship.Category: Planned ForecastHypothetical Derivative: empty at this moment, it will be created after designation is released.Product Group: ExposuresValuation Class: determined from pre-defined configuration on Product Type levelExposure Item ID: generated number.Note down the Exposure Item of original Hedging Relationship.Exposure Subitem ID: generated number. Note down the Exposure Subitem ID of original Hedging Relationship. |  |
| 7 | Display Tab Hedging Instrument | Choose tab Hedging Instrument, and check data of it. | Tab Hedging Instrument contains information about:Hedging Instrument DetailsPosition Management information of the Hedging InstrumentThe following fields are automatically populated:Number: generated number. Note down the Hedging Instrument Number.Product Group: OTC Transactions: Money Market, FX, DerivativesValuation Class: derived from pre-defined configuration and the General Valuation Class you chose when created FX transactions.Transaction Number: the FX transaction number you created in previous step.Start Date: Contract Date of FX transactionEnd Date: Value Date of FX Transaction |  |

Option 2: via app Process Spots/Forwards (Subtitle: Collective Processing)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06). | The Forex: Collective Processing screen displays. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: the transaction number of original FX Forward Transaction | The list of FX transaction(s) displays in area Forex: Collective Processing - Results. |  |
| 4 | Display Transaction | Select the checkbox of a transaction in area Forex: Collective Processing - Results, and choose Display, | The Display Forex Transaction: Structure screen displays. |  |
| 5 | Display the Hedging Relationship | Choose tab Administr., choose the button Show Hedging Relationship.On List of Hedging Relationships screen, select the checkbox of a Hedging Relationship, and then choose Display Hedging Rel.. | The P-Hedge Accounting screen displays, you can check detailed information of Hedging Relationship just like in app Manage Hedging Relationships (TPM100). |  |

|  |
| --- |
|  |

If you cannot see the Hedging Relationship for your FX transaction via app Manage Hedging Relationships (TPM100) or Process Spots/Forwards (Subtitle: Collective Processing), or you already saw message Reprocessing of financial transaction required after save when you saved the FX transaction in step Create Foreign Exchange Contract with Hedging Classification, the system did not finish the automated designation of the financial transaction and exposure.

To analyze the error situation and postprocess the financial transaction for the designation, use app Reprocess Transactions (Subtitle: Automated Designation), for details please see the procedure as below:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reprocess Transactions - Automated Designation (TPM104). | The Reprocess Financial Transactions for Automated Designation screen displays. |  |
| 3 | Enter Selection Criteria | On the Reprocess Financial Transactions for Automated Designation screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 002Transaction: <the transaction number of original FX Forward Transaction> | The Transaction Numbers screen displays.If you cannot see any transaction on this screen, please skip current step because automated designation is created for the transaction you selected on previous screen, |  |
| 4 | Display Log | Select the checkbox of a transaction, and choose Display Log. | Dialog Messages displays, and you can see the relevant message and figure out why automated designation failed. |  |

#### Set Contract Settlement Status with Incoming Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once a FX transaction is saved in system, the status of transaction needs to set as 'Contract Settlement' before you could create postings for flows, usually it is done after you receive the incoming confirmation from counterparty. You can settle the transaction via the following ways once you get counterparty confirmation:

- Option 1: Manual Settlement via app Process Spots/Forwards (Subtitle: Collective Processing)
- Option 2: Automatic settlement via Correspondence Process
- In this step, we only proceed Option 1 - Manual Settlement.

|  |
| --- |
| Note As described in section Prerequisites of step Create Foreign Exchange Contract with Hedging Classification: If you used the Designation Type which requires counterconfirmation, you need to run the correspondence process which will set the status of FX transaction to 'Counterconfirmed' automatically after receiving the incoming confirmation from counterparty, and correspondence setting should be maintained for business partner before creating a FX transaction (please see section [Business Conditions](#unique_6) [page ] 6).For details regarding how to do Automatic Settlement via Correspondence Process, please see the step Correspondence with PDF Form in test script Foreign Currency Risk Management (1X1). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06) | The Forex: Collective Processing screen displays. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the transaction number of original FX Forward Transaction> | The list of FX transaction(s) displays in area Forex: Collective Processing - Results. |  |
| 4 | Settle the Transaction | Select the checkbox of a transaction in area Forex: Collective Processing - Results, and choose Settle. | The Settle forex transaction: Structure screen displays. |  |
| 5 | Save the Change | On the Settle Forex Transaction: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If dialog Document lines: Display messages displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

#### Release Original Hedging Relationship

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the automated designation (for the original FX forward transaction) which is in status Planned Designation. After release, the status will become Designated.

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see section Business Conditions.

If you used the Designation Type which requires counter-confirmation in step Define or Adjust Hedging Area, hedging relationship can be released only after the FX transaction has been successfully counterconfirmed. You need to run step Correspondence with PDF Form in test script Foreign Currency Risk Management(1X1), the correspondence process in 1X1 will set the status of FX transaction to Counterconfirmed automatically after receiving the incoming confirmation from counterparty.

Open the configuration step Define Hedging Profiles, find out the hedging profiles you maintained in the Hedge Accounting II tab of hedging area HA0003, and deselect the checkbox Documentation Optional (Yes/No) for each hedging profile, otherwise the Hedge Documentation cannot be displayed when releasing the hedging relationship.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions (TPM120) screen displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions (TPM120) screen, enter the following data and choose Execute:Company code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, <current date>Transaction Selection: <select this radio button>Transaction Number: <the transaction number of original FX Forward Transaction>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions (TPM120) displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions (TPM120) screen, choose Execute. | The Hedging Relationships screen displays, and Hedging Relationship has been released without errors. |  |
| 5 | Check Market Data Calculation Details | Choose Display Market Value Calculation Details. | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays. You can see the details of the calculation of the full NPV as well as the Hedge Accounting Key Figures. The offered detail lists and analysis options are the same as the ones available in app Calculate Net Present Values (Subtitle: with CVA and DVA).Choose Hedge Accounting Key Figures, you can see the amounts of different components (spot, forward, CCBS, and other components) of FX transaction and hypothetical derivative.Go back to the Hedging Relationships screen. |  |
| 6 | Check Hedging Relationship | On the Hedging Relationships screen, select the checkbox of a HR Number, choose DisplayHedging Relationships. | The screen P-Hedge Accounting display, and you can see Hedging Relationship Status is now 'Designated'.Choose tab Hedged Item, you can see the field Hypothetical Derivative has been filled with a generated number. |  |
| 7 | Display Hedge Documentation | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Hedge Documentation. | The Hedging Relationship Documentation in PDF format will be opened. |  |

#### Period End Closing Before Swap

|  |
| --- |
| Note This section introduces the period end closing activities of valuation area 002 (IFRS 9 Hedge Accounting) for the original Hedging Relationship before swap for overhedge.For period end closing activities of valuation area AE0 (local GAAP, non-Hedge Accounting), please see test script Foreign Currency Risk Management(1X1) -> section Foreign Currency Risk Management and Accounting - Without Options -> steps under node Period end has been reached. |

##### Calculate NPV of Hedging Instrument and Hypothetical Derivative

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you calculate the Net Present Value (Fair Value) of the Securing FX Transaction and corresponding Hypothetical Derivative at month end, system also calculates market value components (spot, forward, CCBS, and other components) for FX Transaction and Hypothetical Derivative, Credit Value Adjustment/Debit Value Adjustment of FX transactions are decomposed as well.

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see section [Business Conditions](#unique_6) [page ] 6. And market data should be valid at period end.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments screen displays. |  |
| 3 | Enter Selection Criteria and Execute | On the Determine NPVs Including Credit and Debit Value Adjustments screen, enter the following data:Sub-area Selection Mode:Evaluation Parameter Derivatn: <select this checkbox>Select OTC Transactions: <select this checkbox>Market Value Decomposition: <select this checkbox>Sub-area Common Selection Criteria:Company Code: for example, 3310Valuation Area: for example, 002Sub-area OTC Transaction Selection Criteria:Transaction: <the transaction number of original FX Forward Transaction>Sub-area Evaluation Parameters:Evaluation Date: for example, <last date of current month>Sub-area Save Results:Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detail Log: <select this checkbox>Choose Execute. | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays.You can see the NPV, risk-free NPV, CVA/DVA of each transaction on this screen.You can also check different information by clicking on buttons:Single Transaction:CVA/DVA Key FiguresHedge Accounting Key FiguresDetailed LogCalculation BasesError LogHedge Accounting Key Figures provides a list showing the detailed amount information of market value components (spot, forward, CCBS, others) for FX Transaction and corresponding Hypothetical Derivative. |  |

##### Run Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to evaluate the position of FX transaction based on the previously calculated NPV, and transfer results to financial accounting.

Prerequisites

NPV and market value components values have been calculated for FX transition and Hypothetical Derivative in valuation area 002 (IFRS).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Run valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run valuation screen, enter the following data:Sub-area Product Groups:OTC Transactions: <select this checkbox>Sub-area General Selections:Company Code: for example, 3310Valuation Area: for example, 002Sub-area OTC Transactions:Transaction: <the transaction number of original FX Forward Transaction>Sub-area Valuation Parameters:Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation without ResetYou can also use Mid-year Valuation with Reset. In addition to the valuation flows, reset flows will be generated for the day following the valuation key date (usually reset flows will be posted at the first date of next month). You can therefore see the effects of the valuation only on the valuation key date.Sub-area Posting Control:Test Run: <select this checkbox>Choose Execute. | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 4 | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log displays, if red traffic light exist, click on it and check the error message, solve the issue and perform test run again until there is no error.You can check the simulated Posting Log for IFRS (valuation area 002) by choosing Logs + Messages, the offsetting account for fair value change of FX transaction is a Technical Clearing Account. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation screen is displayed. |  |
| 6 | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation screen, choose Run valuation. | The screen Valuation Log displays, you can check the Posting Log for IFRS (valuation area 002) by choosing Logs + Messages, this time, accounting documents have been created for IFRS (valuation area 002). |  |

##### Run Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Classification of FX Transactions which are designated into one or several Hedging Relationships is executed via app Run Classification (TPM101) at month end.

With the execution of Classification, the designated Exposure Subitem Positions of the Hedging Relationship are selected and relevant classification amounts are calculated according to settings of the Hedge Accounting Rule:

- Hedging Reserve (OCI I)
- P/L ineffective of Hedging Reserve
- Cost of Hedging Reserve (OCI II)
- P/L ineffective of Cost of Hedging Reserve
- P/L ineffective

Postings to Financial Accounting are created on Exposure Subitem level.

Prerequisites

Valuation for FX transaction (hedging instrument) has been executed at period end.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Run Classification (TPM101). | The Execute Classification screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Execute Classification screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 002Key Date for Classification: for example, <last date of current month>Transaction Selection: <select this radio button>Transaction Number: <the transaction number of original FX Forward Transaction>Test Run:<select this checkbox> | Dialog box Information Overview displays. |  |
| 4 | Check Classification Log | In the dialog box Information Overview, choose Hedge Management. | The Information Overview screen displays, you can check the Classification Log on this screen. |  |
| 5 | Check Posting Log | Choose Back.In the dialog box Information Overview, choose Posting Log. | The Posting Log: Posted Business Transactions screen displays.You can check the simulated Classification postings for IFRS (valuation area 002) on this screen, the offsetting account for OCI I, OCI II, P/L Ineffective is also the Technical Clearing Account. |  |
| 6 | Execute Valuation for Production Run | Choose Back, and choose Close in the dialog box Information Overview.On the initial screen of app Run Classification (TPM101), change the following data and choose Execute:Test Run: <deselect this checkbox> | The Information Overview screen displays again.The classification postings have been created for IFRS (valuation area 002), you can click Posting Log to check the postings. |  |

#### Create Raw Exposure for Overhedge Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Assume that after the first period end closing, Middle Office realizes full or partial of the original forecasted cash flow in the original period should be postponed to another later period, that means, an overhedge situation occurs for the original period.

During this step, Middle Office will create new Raw Exposure to transfer the exposure position from original period to a new period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Raw Exposure (FTREX1). | The Raw Exposure: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | On the Raw Exposure: Initial Screen, enter the following data and choose Create.Exposure Activity Type: for example, YFXI | The Raw Exposure Maintenance: Create screen displays. |  |
| 4 | Enter Header Data | On the Raw Exposure Maintenance: Create screen and tab Header Data, enter the following data:Default Exposure Category: for example, 01 (Forecasted Transaction)Company Code: for example, 3310Cirt4ExpPosType: FX (FX Exposure)Direction: for example, IN (Incoming Cash Flow) | Necessary header data is entered. |  |
| 5 | Enter Line Item Data | Choose tab Line Item Data.In sub-area Raw Exposure Line Item, choose Create New Line Item, and enter the following data:Exposure Due Date : the date in original period the exposure will be swapped from, for example, <Current date + 2 Months>Exposure Amount: for example, -300000Exposure Amount Currency: for example, USDTarget Currency: for example, AEDChoose Create New Line Item again and enter the following data:Exposure Due Date: the date in new period the exposure will be swapped to, for example, <Current date + 4 Months>Exposure Amount: for example, 300000Exposure Amount Currency: for example, USDTarget Currency: for example, AED | Necessary line item data is entered. |  |
| 6 | Save Raw Exposure | Choose Save. | A dialog box displays, and states that:Raw exposure has been saved;Raw exposure has been released;Position IDs have been updated.You can check Exposure Position and Exposure Position Flows via app Process Exposure Positions (FTREX12) and Display Exposure Position Flows.In the example, after the raw exposure is created, the incoming exposure in original period is partially transferred to the new period. |  |

#### Take Snapshot

Purpose

Take a new snapshot to reflect the transfer of exposure from original period to new period.

Procedure

Execute step [Take Snapshot](#unique_10) [page ] 24 which has been described previously.

|  |
| --- |
| Note You may encounter the error message Day reference snapshot for same day already exists and is used when taking snapshot, the reason is that you already took a snapshot for hedge accounting purpose (check box Day Reference is selected) at current system date. In this case, you can just skip current step. |

#### Create and Submit Swap Request in Hedge Management Cockpit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create and submit a hedge request (Swap category) to transfer hedging relationship from the original period to a new period in Hedge Management Cockpit.

The hedge request contains information about the Hedging Relationship to be swapped to a new period.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Hedge Management Cockpit (TOENE). | The Hedge Management Cockpit for Hedging Area screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Start:Hedging Area: for example, HA0003Layout ID: for example, 1R_ALL_CH | The Hedge Management Cockpit for Hedging Area HA0003 displays. |  |
| 4 | Create Swap Request | Choose a cell for original period (for example, current period + 2 months) and risk currency (for example, USD) in accordance to the new raw exposure you just created.Choose Hedge Request > FX Swap Request . | The Hedge Request screen displays. |  |
| 5 | Enter and Check Date for Swap Request | Enter the following data and choose Check:Header:Description (the field beside field Hedge Request ID): <any text>General tab:Hedge Req. Reason: S002 Overhedge Processing - SwapInitial Value Date: <the value date of original FX forward transaction>Target Value Date: a date in the new period the exposure is swapped to, for example, <Current date + 4 Months>Hedging Classificatn: YFC40Hedge Request Amount: the swapped exposure amount, for example, 300000Hedging Relationships tab:Valuation Area: 002Select the checkbox Requested for the row with the Transaction Number of the Original FX Forward Transaction and HR Number you noted down when executing step Automatically Create Original Hedging Relationship (Planned Designation).Request Amount (for the selected row): <swapped exposure amount>, for example, 300000Sequence: for example, 1 | The system displays the message Hedge Request is consistent. The data you entered is OK. Otherwise, check your data until you see this message. |  |
| 6 | Submit Swap Request | Choose Submit. | The system displays the message Hedge Request <number> was saved. Make a note of the Hedge Request ID: __________ |  |

#### Release Swap Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the Hedge Request (category 'Swap').

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO). | The Process Hedge Requests (TOEHREQO) screen displays. |  |
| 3 | Enter Selection Criteria and Start Search | On the Process Hedge Requests (TOEHREQO)screen, enter the following data:Hedging Area: for example, HA0003Company Code: for example, 3310Swap (in subarea Category): <make sure this checkbox has been selected>Submitted (in subarea Status): <make sure this checkbox has been selected>Choose Start. | A list of hedge request(s) displays, your swap request is in this list, its status is Submitted. |  |
| 4 | Release Swap Request | Choose the Hedge Request ID of the swap request you created and submitted, and choose Process -> Release.If a dialog box appears and states that Data was Changed. Do you want to Save?, choose Yes. | The swap request's status becomes Released. |  |

#### Create FX Swap Transactions

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The swap request has been created and released in previous step, it will be forwarded to front office who close the FX transactions at the market.

In this step, FX swap transactions will be created manually based on the information of the swap request to transfer the hedging relationship from the original period to the new period, as a result the overhedge situation will be solved.

There are two alternatives to create FX swap transactions, you choose one of them during testing:

- Option 1: Create FX Swap Transactions in Single Step. The two legs and the reference are saved at the same time.
- Option 2: Create Offsetting Leg (Near Leg) and Securing Leg (Far Leg) of FX Swap separately and Create Swap Reference.

No matter which option you choose, the following criteria should be fulfilled:

- Offsetting leg (of FX Swap transactions) has opposite currency pair than original FX forward transaction (of the original hedging relationship to be swapped)
- Securing leg (of FX Swap transactions) has identical currency pair than original FX forward transaction (of the original hedging relationship to be swapped)
- Absolute nominal amounts of offsetting and securing leg are identical with the swapped portion of the original FX forward transaction
- Offsetting leg and original FX forward transaction have identical value date
- Securing leg's value date is identical to the Target Value Date in Hedge Request
- Securing leg and offsetting leg have identical contract date
- Securing leg and offsetting leg have identical Hedging Classification
- Securing leg and offsetting leg have identical Hedge Request ID

##### Option 1: Create FX Swap Transactions in Single Step

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create FX Swap (TX10). | The Create FX Swap: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Create FX Swap: Initial Screen, enter the following data:Company Code: for example, 3310Partner: for example, 33537001Sub-area First Transaction:Product Type: 60ATransaction: 102Sub-area Second Transaction:Product Type: 60ATransaction: 102Choose Enter. | The Create Forex Swap: Structure screen displays. |  |
| 4 | Enter Data for 1st Transaction (Offsetting Leg) | On the Create Forex Swap: Structure screen, enter the following data in area 1st Transaction:Currencies: for example, AED/USDRate: for example,1.14Buy/Sell: <it should be opposite direction than original FX forward transaction>, for example, BuyTraded Amt: the Hedge Request Volume entered in the swap request, for example, USD300000Value Date: it should identical to the value date of original FX forward transaction, for example, <Current date + 2 Months>Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: YFC40 (FX Risk; CFH; Overhedge Processing - FX Swap)HReq.ID: <the Hedge Request ID you noted down in step Create and Submit Swap Request in Hedge Management Cockpit>Choose Enter. | Data for 1st Transaction (offsetting leg) has been entered. |  |
| 5 | Enter Data for 2nd Transaction (Securing Leg) | Enter the following data in area 2nd Transaction:Rate: for example, 1.16Buy/Sell: it is automatically populated based on the Buy/Sell indicator of 1st transactionTraded Amt: the Hedge Request Volume entered in the swap request, for example, USD300000Value Date: it should identical to the Target Value Date in the Hedge Request, for example, <Current date + 4 Months>Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: YFC40 (FX Risk; CFH; Overhedge Processing - FX Swap)HReq.ID: <the Hedge Request ID you noted down in step Create and Submit Swap Request in Hedge Management Cockpit>Choose Enter. | Data for 2nd Transaction (securing leg) has been entered. |  |
| 6 | Enter Contract Conclusion Data | In area Contract Conclusion, enter the following data:Contract Date: it is the Swap Date, for example, <Current date + 1 month> | Contract date has been entered. |  |
| 7 | Save the FX Swap Transactions (Both Legs) | Choose Save. | Message Forex transactions <number 1> and <number 2> saved in company code <company code> displays.Two legs of FX swap have been saved, the swap reference for them has been created.Note down the transaction numbers of these two legs. |  |

##### Option 2: Create Two Legs of FX Swap Separately and Create Swap Reference

Procedure

Create Offsetting Leg (Near Leg):

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Spot/Forward Transaction Entry: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: 60ATransaction Type: 102Partner: for example, 33537001 | The Spot/Forward Transaction Entry: Structure screen displays. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Rate: for example, AED/USD1.14Buy/Sell: <it should be opposite direction than original FX forward transaction>, for example, BuyTraded Amt:<the Hedge Request Volume entered in the swap request>, for example, USD300000Value Date: <it should identical to the value date of original FX forward transaction>, for example, Current date + 2 MonthsContract Date: it is the Swap Date, for example, <Current date + 1 month> | Data on tab Structure has been entered. |  |
| 5 | Enter Data in Administration tab | Choose tab Administr., and enter the following data:Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: YFC40 (FX Risk; CFH; Overhedge Processing - FX Swap)HReq.ID: <the Hedge Request ID you noted down in step Create and Submit Swap Request in Hedge Management Cockpit> | Data on tab Administr. has been entered. |  |
| 6 | Save the Offsetting Leg of FX Swap Transactions | Choose Save. | If dialog box Document lines: Display messages displays, make sure no error message is there (otherwise please correct data and save again), and choose Continue (Enter).Message Financial transaction saved under number number displays.Note down the transaction number of this Offsetting leg. |  |

Create Securing Leg (Far Leg):

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Spot/Forward Transaction Entry: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: 60ATransaction Type: 102Partner: for example, 33537001 | The Spot/Forward Transaction Entry: Structure screen displays. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Rate: for example, AED/USD1.16Buy/Sell: it should be identical to the direction of original FX forward transaction, for example, SellTraded Amt: the Hedge Request Volume entered in the swap request, for example, USD300000Value Date: it should identical to the Target Value Date in the Hedge Request, for example, <Current date + 4 Months>Contract Date: it is the Swap Date and identical to the Contract Date of Offsetting leg, for example, <Current date + 1 month> | Data on tab Structure has been entered. |  |
| 5 | Enter Data in Administration tab | Choose tab Administr., and enter the following data:Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: YFC40 (FX Risk; CFH; Overhedge Processing - FX Swap)HReq.ID: <the Hedge Request ID you noted down in step Create and Submit Swap Request in Hedge Management Cockpit> | Data on tab Administr. has been entered. |  |
| 6 | Save the Securing Leg of FX Swap Transactions | Choose Save. | If dialog box Document lines: Display messages displays, make sure no error message is there (otherwise please correct data and save again), and choose Continue (Enter).Message Financial transaction saved under number number displays.Note down the transaction number of this Offsetting leg. |  |

Create Swap Reference:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create Reference (TBR6). | The Create Reference: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Create Reference: Initial Screen, enter the following data:Reference Category: SWPSub-area Object 1 to Be Linked:Company Code: for example, 3310Transaction: <The transaction number of the offsetting leg>Sub-area Object 2 to Be Linked:Company Code: for example, 3310Transaction: <The transaction number of the securing leg>Choose Enter. | The Create Reference: Data screen displays. |  |
| 4 | Save Reference | On the Create Reference: Data screen, choose Save, | Massage Reference number created displays. |  |

#### Automatically Update Original Hedging Relationship and Create New Hedging Relationship (Planned Designation)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The creation of the Swap Reference generates a Hedging Business Transaction type ‘Hedging Relationship Swap Transfer‘ which is relevant for the original Hedging Relationship:

- Nominal Amounts of Hedged Item (Exposure Subitem) and Hedging Instrument (FX Forward Transaction) as well as pro rata amounts of Hedging Reserve and Cost of Hedging Reserve are transferred out at Swap Date.
- In case of partial swap, the remaining portions of the amounts are processed within the original hedging relationship according to the settings at Designation Date.

A new Hedging Relationship is created in status ‘Planned Designation’ with Designation Date = Swap Date:

- The Hedging Profile is copied from the original Hedging Relationship to the new Hedging Relationship.
- Splitting information for the creation of multiple Hedging Relationships is not considered for the creation of the new Hedging Relationship.
- (Planned) Dedesignation Date is newly determined for the new Hedging Relationship from the settings of the Hedging Area version valid at the designation date of the original Hedging Relationship.
- If the Balance Sheet Recognition Date of the original Hedging Relationship is later than/equal to the designation date (swap date) of the new Hedging Relationship, the date is newly determined for the new Hedging Relationship from the settings of the Hedging Area version valid at the designation date of the original Hedging Relationship. In case of the Balance Sheet Recognition Date was passed at swap date, the Balance Sheet Recognition Date is copied from the original Hedging Relationship to the new Hedging Relationship.
- A new Designation Type for Hedging Relationships with FX Swap Transactions is assigned
- The Swap Reference can be accessed from the new Hedging Relationship.
- The Hedged Item is created the same way as for regular Hedging Relationships: Payment Term and Days Inventory Outstanding determination for the creation of the end date of the new Exposure Subitem or the Hypothetical Derivative is used from the settings of the Hedging Area version valid at the designation date of the original Hedging Relationship.
- Multiple Hedging Instruments are listed and can be accessed within the new Hedging Relationship: the original FX Transaction can be accessed, the two legs of FX Swap Transactions can be accessed.

This step introduces how to check original and new Hedging Relationships in app Manage Hedging Relationships (TPM100).

Procedure

Check Original Hedging Relationship:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Manage Hedging Relationships (TPM100). | The P-Hedge Accounting screen displays. |  |
| 3 | Enter Selection Criteria | On the P-Hedge Accounting screen, choose tab Selection on the left side of screen, and enter the following data:Find: All Hedging RelationshipsBy: Hedging InstrumentCompany Code: for example, 3310Valuation Area: 002Product Group: select the checkbox of OTC Trans., and choose the button OTC Transactions Selection beside OTC Trans.. In the dialog box OTC Transactions Selection, enter the transaction number of the original FX forward transaction, then choose Continue (Enter).Choose Start. | The original Hedging Relationship Number displays on bottom-left side of screen. You may need to zoom out the screen in web browser to see it. |  |
| 4 | Change Display Date | Choose Change Display Date.In dialog box Change Display Date, enter the following data:Display Date: the swap date, for example, current date + 1 month | Data for this hedging relationship at the swap date is displayed. |  |
| 5 | Display Tab Hedged Item | Choose tab Hedged Item, and check data of it. | The Designated Amount of Hedged Item is reduced because originally designated amount has been fully or partially swapped out. |  |
| 6 | Display Tab Hedging Instrument | Choose tab Hedging Instrument, and check data of it. | The Designated Amount of Hedging Instrument is reduced because originally designated amount has been fully or partially swapped out. |  |

Check New Hedging Relationship:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Manage Hedging Relationships (TPM100). | The P-Hedge Accounting screen displays. |  |
| 3 | Enter Selection Criteria | On the P-Hedge Accounting screen, choose tab Selection on the left side of screen, and enter the following data:Find: All Hedging RelationshipsBy: Hedging InstrumentCompany Code: for example, 3310Valuation Area: 002Product Group: select the checkbox of OTC Trans., and choose the button OTC Transactions Selection beside OTC Trans.. In the dialog box OTC Transactions Selection, enter the transaction numbers of the two legs of FX Swap Transaction, then choose Continue (Enter).Choose Start. | The new Hedging Relationship Number displays on bottom-left side of screen. You may need to zoom out the screen in web browser to see it.Note down the Hedging Relationship Number of this new Hedging Relationship. |  |
| 4 | Display Header of Hedging Relationship | Double click a HR Number from bottom-left side of screen, the detailed information of Hedging Relationship will display on right side of screen.Check the data of Hedge Relationship Header. | The header of Hedging Relationship displays on upper-right side of screen, it provides details which are relevant for the Hedging Relationship as general entity.The Hedging Relationship Status should be ‘Planned Designation’ since it has not been released.Choose Display All Flows, you can check the relevant flows of this new Hedging Relationship.Choose Display H.Rel. Related Trans, in Hedge Related Transactions for Hedging Relationship dialog box, double click the row of Business Transaction Category Hedging Relationship Swap Transfer, then you can see the details in Swap Transfer of Hedging Relationship dialog box. |  |
| 5 | Display Tab Hedging Relationship Detail | Check the data of tab Hedge Relationship Details. | Tab Hedging Relationship Detail contains information about:Risk Type and Risk Profile DetailsDate information on Hedging Relationship levelThe following fields are automatically populated:Risk Currency: your exposure currencyProfile: is copied from original Hedging Relationship.Category: Cash Flow HedgeRisk Indicator: Currency RiskValid-From Date: contract date of FX Swap TransactionsPlanned Designation Date: contract date of FX Swap TransactionsPlanned Dedesign. Date: is newly determined for the new Hedging Relationship from the settings of the Hedging Area version valid at the designation date of the original Hedging Relationship.Bal.Sheet Rec.Date: the Balance Sheet Recognition Date of crossover for new Hedging RelationshipNote down the Balance Sheet Recognition Date.Reclassification Date: the Deviant Reclassification Date, it is only available when you gave value 3 for the field Balance Sheet Recognition in sub-area Designation Splitting on tab Hedge Accounting I of the Hedging Area.Designation Type: the Designation Type which is mapped (on tab Hedge Accounting II of Hedging Area) to the Hedging Classification you used when created FX Swap TransactionsCategory: SWPReference: the ID of Swap Reference |  |
| 6 | Display Tab Hedged Item | Choose tab Hedged Item, and check data of it. | Tab Hedged Item contains information about:Hedged Item DetailsPosition Management information of the Exposure SubitemThe following fields are automatically populated:Number: generated number. Note down the Hedged Item Number of New Hedging Relationship.Start Date: contract date of FX Swap TransactionsEnd Date: it is determined by the parameters of the Hedging Area version valid at the designation date of the original Hedging Relationship. It is the date on which reclassification of OCI I and OCI II should carry out (except the case without Balance Sheet Crossover). Note down this Exposure Subitem End date of new Hedging Relationship.Category: Planned ForecastHypothetical Derivative: empty at this moment, it will be created after designation is released.Product Group: ExposuresValuation Class: determined from pre-defined configuration on Product Type levelExposure Item ID: generated number.Note down the Exposure Item of new Hedging Relationship.Exposure Subitem ID: generated number. Note down the Exposure Subitem ID of new Hedging Relationship. |  |
| 7 | Display Tab Hedging Instrument | Choose tab Hedging Instrument, and check data of it. | Tab Hedging Instrument contains information about:Hedging Instrument DetailsPosition Management information of the Hedging InstrumentThe new Hedging Relationship contains 3 Hedging Instruments:Original FX Forward TransactionOffsetting Leg of FX Swap TransactionsSecuring Leg of FX Swap TransactionsThe following fields are automatically populated for each Hedging Instrument:Number: generated number. Note down the Hedging Instrument Numbers.Product Group: OTC Transactions: Money Market, FX, DerivativesValuation Class: derived from pre-defined configuration and the General Valuation Class you chose when created relevant FX transactions.Transaction Number: the FX transaction number of each FX transactionStart Date: Contract Date of each FX transactionEnd Date: Value Date of each FX Transaction |  |

#### Set Contract Settlement Status for FX Swap Transactions with Incoming Confirmations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the Offsetting and Securing FX Forward Transactions are saved in system, the status of transactions needs to set as 'Contract Settlement' before you could create postings for flows, usually it is done after you receive the incoming confirmation from counterparty. You can settle the transactions via the following ways once you get counterparty confirmation:

- Option 1: Manual Settlement via app Process Spots/Forwards (Subtitle: Collective Processing)
- Option 2: Automatic settlement via Correspondence Process
- In this step, we only proceed Option 1 - Manual Settlement.

|  |
| --- |
| Note As described in section Prerequisites of step Create Foreign Exchange Contract with Hedging Classification: If you used the Designation Type which requires counterconfirmation, you need to run the correspondence process which will set the status of FX transaction to 'Counterconfirmed' automatically after receiving the incoming confirmation from counterparty, and correspondence setting should be maintained for business partner before creating a FX transaction (please see section Business Conditions).For details regarding how to do Automatic Settlement via Correspondence Process, please see the step Correspondence with PDF Form in test script Foreign Currency Risk Management. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06) | The Forex: Collective Processing screen displays. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the transaction numbers for two legs of FX Swap Transactions> | The list of FX transaction(s) displays in area Forex: Collective Processing - Results. |  |
| 4 | Settle the Offsetting FX Forward Transaction | Select the checkbox of the Offsetting FX Forward Transaction in area Forex: Collective Processing - Results, and choose Settle. | The Settle forex transaction: Structure screen displays. |  |
| 5 | Save the Change | On the Settle Forex Transaction: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If dialog Document lines: Display messages displays, choose Continue (Enter). | The Offsetting FX Forward Transaction is saved with status Contract Settlement. |  |
| 6 | Settle the Securing FX Forward Transaction | Repeat the steps above to settle the Securing FX Forward Transaction. | The Offsetting FX Forward Transaction is saved with status Contract Settlement. |  |

#### Process Hedging Relationships at Swap Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you process the original and new Hedging Relationships at the Swap Date via app Release Hedging Business Transactions (TPM120).

With the release of hedging relationships at Swap Date, the following activities are executed:

- The status of new Hedging Relationship is changed to Designated.
- The Aligned Value Check Result of the original Hedging Relationship was copied to the new Hedging Relationship.
- A new Hypothetical Derivative for new Hedging Relationship is created with Start Date of original Hedging Relationship and End Date according to setting of Hedging Area Version of original Hedging Relationship.
- Copy of Market Data Container Values of the swapped portion of the original Hedging Instrument to the new Hedging Relationship.
- Calculation of Market Data Container Values of FX Swap Transactions.
- Calculation and posting of First Day Result of the new Hedging Relationship according to setting of Hedging Relationship Profile.
- Calculation and posting of valuation and classification flows of the original Hedging Relationship.
- Calculation and update of amounts of Exposure Subitem position transfer flows.
- Change status of nominal amount transfer flows to Fixed.

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see section [Business Conditions](#unique_6) [page ] 6. And market date should be valid at the Swap Date.

If you used the Designation Type which requires counterconfirmation in step [Define or Adjust Hedging Area](#unique_8) [page ] 12, the new Hedging Relationship can be released only after the FX Swap Transactions has been successfully counterconfirmed. You need to run step Correspondence with PDF Form in test script Foreign Currency Risk Management, the correspondence process in 1X1 will set the status of FX transaction to 'Counterconfirmed' automatically after receiving the incoming confirmation from counterparty.

Open the configuration step Define Hedging Profiles, find out the hedging profiles you maintained in the Hedge Accounting II tab of hedging area HA0003, and deselect the checkbox Documentation Optional (Yes/No) for each hedging profile, otherwise the Hedge Documentation cannot be displayed when releasing the hedging relationship.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions (TPM120) screen displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions (TPM120) screen, enter the following data and choose Execute:Company code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, <the Swap Date, which is also the Contract Date of FX Swap Transactions>Transaction Selection: <select this radio button>Transaction Number: <the FX transaction numbers: original FX Forward Transaction, and the two legs of FX Swap Transactions>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions (TPM120) displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions (TPM120) screen, choose Execute. | The Hedging Relationships screen displays, and Hedging Relationship has been released without errors. |  |
| 5 | Check Market Data Calculation Details | Choose Display Market Value Calculation Details. | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays. You can see the details of the calculation of the full NPV as well as the Hedge Accounting Key Figures for the original FX Forward Transaction and FX Swap Transactions.Go back to the Hedging Relationships screen. |  |
| 6 | Check Hedging Relationship | On the Hedging Relationships screen, select the checkbox of the new Hedging Relationship Number, choose DisplayHedging Relationships. | The screen P-Hedge Accounting display, and you can see Hedging Relationship Status is now 'Designated'.Choose tab Hedged Item, you can see the field Hypothetical Derivative has been filled with a generated number.Go back to the Hedging Relationships screen. |  |
| 7 | Check Log and Message | On the Hedging Relationships screen, select the checkbox of the new Hedging Relationship Number, and select Display Log. | Dialog box Information Overview displays, you can check:Posting logHedge management logMessagesGo back to the Hedging Relationships screen. |  |
| 8 | Display Hedge Documentation | On the Hedging Relationships screen, select the checkbox of the new Hedging Relationship Number, choose Display Hedge Documentation. | The Hedging Relationship Documentation in PDF format will be opened. |  |

#### Period end Closing between Swap Date and Maturity of Original FX Transaction

|  |
| --- |
| Note This section introduces the period end closing activities of valuation area 002 (IFRS 9 Hedge Accounting) for the original and new Hedging Relationships at end of the period in which the Swap Date is, and this period end should be earlier than maturity of original FX Forward Transaction.For period end closing activities of valuation area AE0 (local GAAP, non-Hedge Accounting), please see test script Foreign Currency Risk Management (1X1) -> section Foreign Currency Risk Management and Accounting - Without Options -> steps under node Period end has been reached. |

##### Calculate NPV of Hedging Instruments and Hypothetical Derivatives

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you calculate the Net Present Values (Fair Values) of FX Transactions and corresponding Hypothetical Derivatives at month end, system also calculates market value components (spot, forward, CCBS, and other components) for FX Transactions and Hypothetical Derivatives, Credit Value Adjustment/Debit Value Adjustment of FX transactions are decomposed as well.

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see section [Business Conditions](#unique_6) [page ] 6. And market data should be valid at period end.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments screen displays. |  |
| 3 | Enter Selection Criteria and Execute | On the Determine NPVs Including Credit and Debit Value Adjustments screen, enter the following data:Sub-area Selection Mode:Evaluation Parameter Derivatn: <select this checkbox>Select OTC Transactions: <select this checkbox>Market Value Decomposition: <select this checkbox>Sub-area Common Selection Criteria:Company Code: for example, 3310Valuation Area: for example, 002Sub-area OTC Transaction Selection Criteria:Transaction: <the transaction numbers of original FX Forward Transaction and two legs of FX Swap Transactions>Sub-area Evaluation Parameters:Evaluation Date: for example, <last date of the month in which the Swap Date is>Sub-area Save Results:Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detail Log: <select this checkbox>Choose Execute. | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays.You can see the NPV, risk-free NPV, CVA/DVA of each transaction on this screen.You can also check different information by clicking on buttons:Single Transaction:CVA/DVA Key FiguresHedge Accounting Key FiguresDetailed LogCalculation BasesError LogHedge Accounting Key Figures provides a list showing the detailed amount information of market value components (spot, forward, CCBS, others) for FX Transaction and corresponding Hypothetical Derivative. |  |

##### Run Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to evaluate the position of FX transaction based on the previously calculated NPV, and transfer results to financial accounting.

For original Hedging Relationship: the remaining portion of the original Hedging Relationship is processed as usual.

For new Hedging Relationship: the designated portion of the FX Transaction as well as each leg of the FX Swap Transactions which are designated into the new Hedging Relationship are evaluated and posted separately as usual.

Prerequisites

NPV and market value components values have been calculated for FX transitions and Hypothetical Derivatives in valuation area 002 (IFRS).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Run valuation screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run valuation screen, enter the following data:Sub-area Product Groups:OTC Transactions: <select this checkbox>Sub-area General Selections:Company Code: for example, 3310Valuation Area: for example, 002Sub-area OTC Transactions:Transaction: <the transaction numbers of original FX Forward Transaction and two legs of FX Swap Transactions>Sub-area Valuation Parameters:Key Date for Valuation: for example, <last date of the month in which the Swap Date is>Valuation Category: for example, Mid-year Valuation without ResetSub-area Posting Control:Test Run: <select this checkbox>Choose Execute. | The Display Selected Treasury Positions for Valuation screen displays.You can see original FX Forward Transaction, two legs of FX Swap Transactions here. |  |
| 4 | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log displays, if red traffic light exist, click on it and check the error message, solve the issue and perform test run again until there is no error.You can check the simulated Posting Log for IFRS (valuation area 002) by choosing Logs + Messages, the offsetting account for fair value change of FX transactions is a Technical Clearing Account. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation screen displays. |  |
| 6 | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation screen, choose Run valuation. | The screen Valuation Log displays, you can check the Posting Log for IFRS (valuation area 002) by choosing Logs + Messages, this time, accounting documents have been created for IFRS (valuation area 002). |  |

##### Run Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Classification of FX Transactions which are designated into one or several Hedging Relationships is executed via app Run Classification (TPM101) at month end.

For original Hedging Relationship: the remaining portion of the original Hedging Relationship is processed as usual.

For new Hedging Relationship: the classification result of the new Hedging Relationship is calculated as the sum of the component NPVs of the single FX Transaction according to the Hedging Relationship Scenario of the Hedging Relationship:

- The original FX Forward Transaction is taken into consideration with its portion designated into the new Hedging Relationship.
- The FX Swap Transactions are considered with 100 % of their designated amount.

The postings are created for the Exposure Subitem of the new Hedging Relationship using the same posting logic and posting specifications as for usual Hedging Relationships.

Prerequisites

Valuation for FX transactions (hedging instruments) has been executed at period end.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Run Classification (TPM101). | The Execute Classification screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Execute Classification screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 002Key Date for Classification: for example, <last date of the month in which the Swap Date is>Transaction Selection: <select this radio button>Transaction Number: <the transaction numbers of original FX Forward Transaction and two legs of FX Swap Transactions>Test Run: <select this checkbox> | Dialog box Information Overview displays. |  |
| 4 | Check Classification Log | In the dialog box Information Overview, choose Hedge Management. | The Information Overview screen displays, you can check the Classification Log of original and new Hedging Relationship on this screen. |  |
| 5 | Check Posting Log | Choose Back.In the dialog box Information Overview, choose Posting Log. | The Posting Log: Posted Business Transactions screen displays.You can check the simulated Classification postings for IFRS (valuation area 002) on this screen, the offsetting account for OCI I, OCI II, P/L Ineffective is also the Technical Clearing Account. |  |
| 6 | Execute Valuation for Production Run | Choose Back, and choose Close in the dialog box Information Overview.On the initial screen of app Run Classification (TPM101), change the following data and choose Execute:Test Run: <deselect this checkbox> | The Information Overview screen displays again.The classification postings have been created for IFRS (valuation area 002), you can click Posting Log to check the postings. |  |

#### Process Reclassification for Original Hedging Relationship at Balance Sheet Recognition Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the Balance Sheet Recognition date of the original Hedging Relationship, you run the app Release Hedging Business Transactions (TPM120), the following activities are done by this app:

- Calculation and saving of NPV of FX Transaction
- Calculation and saving of NPV component values for FX Transaction and Hypothetical Derivative
- Posting of key date valuation of the designated portion of the FX Transaction with actual NPV values
- Posting of classification of the selected Hedging Relationship with designated portion of actual NPV component values
- Update amounts of Reclassification Update Types
- Fix scheduled Reclassification Updated Types

Three options are provided for the reclassification of Balance Sheet Crossover, they are maintained in field Balance Sheet Recognition in sub-area Designation Splitting on tab Hedge Accounting I of the Hedging Area:

- 1 - Immediate Reclassification at Balance Sheet Recognition Date
- 2 - Reclassification at the End Date of the Exposure Subitem: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until end date of the Exposure Subitem.
- 3 - Reclassification at Deviant Reclassification Date: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until the Deviant Reclassification Date = Due Date of Hedging Instrument + DIO (Days Inventory Outstanding) - Payment Term.

|  |
| --- |
| Note This step is only necessary when you do Balance Sheet Crossover, that means, you gave value 1, 2 or 3 for the field Balance Sheet Recognition in sub-area Designation Splitting on tab Hedge Accounting I of the Hedging Area, and you can see the Bal.Sheet Rec.Date on tab Hedging Relationship Detail of the original Hedging Relationship as described in step Automatically Create Original Hedging Relationship (Planned Designation). |

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see section [Business Conditions](#unique_6) [page ] 6. And market date should be valid at the Balance Sheet Recognition Date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions (TPM120) screen displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions (TPM120) screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, <Balance Sheet Recognition Date of original Hedging Relationship you noted down in step Automatically Create Original Hedging Relationship (Planned Designation)>Transaction Selection: <select this radio button>Transaction Number: <the transaction number of original FX Forward Transaction>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions (TPM120) screen displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions (TPM120) screen, choose Execute. | The Hedging Relationships screen displays, and Hedging Relationships have been processed without errors. |  |
| 5 | Display Log of Hedge Management | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Log.In the Information Overview dialog box, choose Hedge Management. | The Information Overview screen displays, you can check the Classification Log on this screen.You will find only the remaining portion of Hedging Instrument and Hedged Item are considered in original Hedging Relationship. |  |
| 6 | Display Log of Posting | Choose Back.In the Information Overview dialog box, choose Posting Log. | The Posting Log: Posted Business Transactions screen displays, you can check the following postings on this screen:ValuationClassificationReclassification (depend on the setting of field Balance Sheet Recognition on tab Hedge Accounting I of the Hedging Area) |  |

#### Contract Maturity for Original FX Transaction and Offsetting FX Transaction

##### (1X1) Foreign Currency Risk Management and (1X9) Foreign Currency Risk Management – Group Ledger IFRS

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the Original FX Forward Transaction and the Offsetting FX Forward Transaction are mature (they have identical Value Date), the relevant posting and payment process steps for closing these two FX transactions (which are Hedging Instruments in Hedging Relationships) should be same as a normal FX transaction (which is not in a Hedging Relationship), relevant process steps are described in test scripts Foreign Currency Risk Management(1X1) and Foreign Currency Risk Management – Group Ledger IFRS(1X9).

Procedure

Perform the following steps in section Foreign Currency Risk Management and Accounting - Without Options of test script Foreign Currency Risk Management(1X1) for the Original FX Forward Transaction and the Offsetting FX Forward Transaction:

| Step Name in 1X1 | Mandatory/Optional for Continuing Testing 2UF | Purpose |
| --- | --- | --- |
| Generate Payment Request for Mature Transaction | Mandatory | Generate payment request for outgoing payment of FX transactions at Value Date via app Fix, Pay and Post Flows (TBB1). |
| Process Payment Request | Optional | Process the payment run procedure for payment requests and create posting for outgoing payments via app Automatic Payment Transactions for Payment Requests (F111). |
| Post to General Ledger | Mandatory | Post the flows of incoming payments at value date of FX transactions in valuation area AE0 (local GAAP) via app Fix, Pay and Post Flows (TBB1);Post the flows of outgoing payments at value date of FX transactions in valuation area AE0 (local GAAP) via app Process Business Transactions (TPM10). |
| Post Realized Profit and Loss | Mandatory | Post realized profit or loss at value date of FX transactions in valuation area AE0 (local GAAP) via app Post Derived Business Transactions (TPM18). |

Perform the following step in test script Foreign Currency Risk Management – Group Ledger IFRS(1X9) for the Original FX Forward Transaction and the Offsetting FX Forward Transaction:

| Step Name in 1X9 | Mandatory/Optional for Continuing Testing 2UF | Purpose |
| --- | --- | --- |
| Post Flows to General Ledger (Parallel Valuation Area) | Mandatory | Post the relevant flows (incoming and outgoing payment) at value date of FX transactions in valuation area 002 (IFRS) via app Process Business Transactions (TPM10). |

##### Process Hedging Relationships at Maturity Date of Original FX Transaction and Offsetting FX Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the maturity date (value date) of Original FX Forward Transaction and the Offsetting FX Forward Transaction, you run the app Release Hedging Business Transactions (TPM120), the following activities are done by this app:

- Calculation and saving of NPV for all FX Transactions in original and new Hedging Relationships.
- Calculation and saving of NPV component values for all FX Transactions and Hypothetical Derivatives in original and new Hedging Relationships.
- Posting of key date valuation of Original FX Forward Transaction and the Offsetting FX Forward Transaction with actual NPV values.
- Posting of classification of the original and new Hedging Relationships with designated portion of actual NPV component values.
- Transfer Position Amounts from Designated to Free Standing Subposition.
- Update amounts of Reclassification Update Types.
- Fix scheduled Dedesignation Updated Types.

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see section [Business Conditions](#unique_6) [page ] 6. And market date should be valid at the maturity date of FX transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions (TPM120) screen displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions (TPM120) screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, <the maturity date of Original FX Forward Transaction and Offsetting FX Forward Transaction>Transaction Selection: <select this radio button>Transaction Number: <the FX transaction numbers of Original FX Forward Transaction and Offsetting FX Forward Transaction>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions (TPM120) screen displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions (TPM120) screen, choose Execute. | The Hedging Relationships screen displays, and Hedging Relationship has been processed without errors. |  |
| 5 | Display Log of Hedge Management | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Log.In the Information Overview dialog box, choose Hedge Management. | The Information Overview screen displays, you can check the Classification Log on this screen. |  |
| 6 | Display Log of Posting | Choose Back.In the Information Overview dialog box, choose Posting Log. | The Posting Log: Posted Business Transactions screen displays, you can check the postings on this screen. |  |

Use app Post Derived Business Transactions (TPM18) to fix the derived business transactions for FX transactions at contract close date:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Fix and Post Derived Business Transactions screen, enter the following data:Sub-area Product Groups:OTC Transactions: <select this checkbox>Sub-area General Selections:Company Code: for example, 3310Valuation Area: for example, 002Sub-area OTC Transactions:OTC Transactions: <the FX transaction numbers of Original FX Forward Transaction and Offsetting FX Forward Transaction>Sub-area Selections for Fixing Derived Business Transactions:TRL Date: <the maturity date of Original FX Forward Transaction and Offsetting FX Forward Transaction>Sub-area Posting Control:Test Run: <select this checkbox>Choose Execute.If message No scheduled derived business transactions were found for the selection displays, then there is no derived transaction available for your selection, you can skip current step.If message Are you sure that you want to select future business transactions? displays, press Enter | The FX Transactions to be fixed and posted (test run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 4 | Fix and Post for Test run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the simulated postings. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the initial screen of this app.Change the following data and choose Execute:Test Run: <deselect this checkbox>If message Are you sure that you want to select future business transactions? displays, press Enter | The FX Transactions to be fixed and posted (production run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 6 | Fix and Post for Production run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the postings for IFRS (valuation area 002), accounting document has been created in corresponding ledger in Financial Accounting. |  |

#### Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date of Original Hedging Relationship

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Reclassification of the Hedging Reserve and Cost of Hedging Reserve position amounts for the original Hedging Relationship is executed at the end date of its Exposure Subitem within the Derived Business Transaction Framework: the app Post Derived Business Transactions (TPM18) for the fixation and posting of Derived Business Transactions selects the Exposure Subitem position flows to be reclassified.

Postings are created for reclassification of Hedging Reserve and Cost of Hedging Reserve position amounts; P/L ineffective position amounts are fixed only.

|  |
| --- |
| Note This step creates postings only when the relevant Split ID on tab Hedge Accounting I of the Hedging Area uses the following parameters for the field Balance Sheet Recognition:0 or Blank - None: the accumulated Hedging Reserve and Cost of Hedging Reserve between Designation Date and Dedesignation Date are reclassified at the end date of Exposure Subitem.2 - Reclassification at the End Date of the Exposure Subitem: the accumulated Hedging Reserve and Cost of Hedging Reserve between Designation Date and Balance Sheet Recognition Date are reclassified at the end date of Exposure Subitem.If 1 - Immediate Reclassification at Balance Sheet Recognition Date is given for field Balance Sheet Recognition, reclassification has been done at the Balance Sheet Recognition Date by using app Release Hedging Business Transactions (TPM120).If 3 - Reclassification at Deviant Reclassification Date is given for field Balance Sheet Recognition, reclassification should be done at the Deviant Reclassification Date by using app Release Hedging Business Transactions. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Fix and Post Derived Business Transactions screen, enter the following data:Sub-area Product Groups:OTC Transactions: <deselect this checkbox>Exposure Items:<select this checkbox>Sub-area General Selections:Company Code: for example, 3310Valuation Area: for example, 002Sub-area Selections for Fixing Derived Business Transactions:TRL Date: <the Exposure Subitem End date of original Hedging Relationship you noted down in step Automatically Create Original Hedging Relationship (Planned Designation)>Sub-area Exposure Items -> Additional Selections:Transaction Number: <the FX transaction number of original FX Forward Transaction>Sub-area Posting Control:Test Run: <select this checkbox>Choose Execute.If message Are you sure that you want to select future business transactions? displays, press Enter | The Exposure Subitem to be fixed and posted (test run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 4 | Fix and Post for Test run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the simulated reclassification postings of Hedging Reserve and Cost of Hedging Reserve for IFRS (valuation area 002). |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the initial screen of this app.Change the following data and choose Execute:Test Run:<deselect this checkbox>If message Are you sure that you want to select future business transactions? displays, press Enter | The Exposure Subitem to be fixed and posted (production run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 6 | Fix and Post for Production run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the postings for IFRS (valuation area 002), accounting document has been created in corresponding ledger in Financial Accounting. |  |

#### Period end Closing after Maturity of Original and Offsetting FX Transactions

|  |
| --- |
| Note This section introduces the period end closing activities of valuation area 002 (IFRS 9 Hedge Accounting) for the New Hedging Relationships at end the period in which Original and Offsetting FX Transactions mature, and this period end should be earlier than maturity of securing FX Transaction.For period end closing activities of valuation area AE0 (local GAAP, non-Hedge Accounting), please see test script Foreign Currency Risk Management (1X1) -> section Foreign Currency Risk Management and Accounting - Without Options -> steps under node Period end has been reached. |

##### Calculate NPV of Hedging Instrument and Hypothetical Derivative

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you calculate the Net Present Value (Fair Value) of the Securing FX Transaction and corresponding Hypothetical Derivative at month end, system also calculates market value components (spot, forward, CCBS, and other components) for FX Transaction and Hypothetical Derivative, Credit Value Adjustment/Debit Value Adjustment of FX transactions are decomposed as well.

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see section [Business Conditions](#unique_6) [page ] 6. And market data should be valid at period end.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments screen displays. |  |
| 3 | Enter Selection Criteria and Execute | On the Determine NPVs Including Credit and Debit Value Adjustments screen, enter the following data:Sub-area Selection Mode:Evaluation Parameter Derivatn: <select this checkbox>Select OTC Transactions: <select this checkbox>Market Value Decomposition: <select this checkbox>Sub-area Common Selection Criteria:Company Code: for example, 3310Valuation Area: for example, 002Sub-area OTC Transaction Selection Criteria:Transaction: <transaction number of the Securing leg of FX Swap Transactions>Sub-area Evaluation Parameters:Evaluation Date: for example, <last date of the month in which the Original/Offsetting FX Transaction mature>Sub-area Save Results:Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detail Log: <select this checkbox>Choose Execute. | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays.You can see the NPV, risk-free NPV, CVA/DVA of each transaction on this screen.You can also check different information by clicking on buttons:Single Transaction:CVA/DVA Key FiguresHedge Accounting Key FiguresDetailed LogCalculation BasesError LogHedge Accounting Key Figures provides a list showing the detailed amount information of market value components (spot, forward, CCBS, others) for FX Transaction and corresponding Hypothetical Derivative. |  |

##### Run Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to evaluate the position of securing FX transaction based on the previously calculated NPV, and transfer results to financial accounting.

Prerequisites

NPV and market value components values have been calculated for FX transition and Hypothetical Derivative in valuation area 002 (IFRS).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Valuation (TPM1). | The Run valuation screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run valuation screen, enter the following data:Sub-area Product Groups:OTC Transactions: <select this checkbox>Sub-area General Selections:Company Code: for example, 3310Valuation Area: for example, 002Sub-area OTC Transactions:Transaction: <transaction number of the Securing leg of FX Swap Transactions>Sub-area Valuation Parameters:Key Date for Valuation: for example, <last date of the month in which the Original/Offsetting FX Transaction mature>Valuation Category: for example, Mid-year Valuation without ResetSub-area Posting Control:Test Run: <select this checkbox>Choose Execute. | The Display Selected Treasury Positions for Valuation screen displays.You can see the securing FX Forward Transaction here. |  |
| 4 | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log displays, if red traffic light exist, click on it and check the error message, solve the issue and perform test run again until there is no error.You can check the simulated Posting Log for IFRS (valuation area 002) by choosing Logs + Messages, the offsetting account for fair value change of FX transactions is a Technical Clearing Account. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation screen displays. |  |
| 6 | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation screen, choose Run valuation. | The screen Valuation Log displays, you can check the Posting Log for IFRS (valuation area 002) by choosing Logs + Messages, this time, accounting documents have been created for IFRS (valuation area 002). |  |

##### Run Classification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Classification of FX Transactions which are designated into one or several Hedging Relationships is executed via app Run Classification (TPM101) at month end.

For the new Hedging Relationship, the classification result is calculated as the sum of the component NPVs of the single FX Transaction according to the Hedging Relationship Scenario of the Hedging Relationship. The postings are created for the Exposure Subitem of the new Hedging Relationship using the same posting logic and posting specifications as for usual Hedging Relationships.

Prerequisites

Valuation for FX transaction (hedging instrument) has been executed at period end.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Run Classification (TPM101). | The Execute Classification screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Execute Classification screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 002Key Date for Classification: for example, <last date of the month in which the Original/Offsetting FX Transaction mature>Transaction Selection: <select this radio button>Transaction Number: <transaction number of the Securing leg of FX Swap Transactions>Test Run: <select this checkbox> | Dialog box Information Overview displays. |  |
| 4 | Check Classification Log | In the dialog box Information Overview, choose Hedge Management. | The Information Overview screen displays, you can check the Classification Log of new Hedging Relationship on this screen. |  |
| 5 | Check Posting Log | Choose Back.In the dialog box Information Overview, choose Posting Log. | The Posting Log: Posted Business Transactions screen displays.You can check the simulated Classification postings for IFRS (valuation area 002) on this screen, the offsetting account for OCI I, OCI II, P/L Ineffective is also the Technical Clearing Account. |  |
| 6 | Execute Valuation for Production Run | Choose Back, and choose Close in the dialog box Information Overview.On the initial screen of app Run Classification (TPM101), change the following data and choose Execute:Test Run:<deselect this checkbox> | The Information Overview screen displays again.The classification postings have been created for IFRS (valuation area 002), you can click Posting Log to check the postings. |  |

#### Process Reclassification for New Hedging Relationship at Balance Sheet Recognition Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the Balance Sheet Recognition date of the new Hedging Relationship, you run the app Release Hedging Business Transactions (TPM120), the following activities are done by this app:

- Calculation and saving of NPV of FX Transaction
- Calculation and saving of NPV component values for FX Transaction and Hypothetical Derivative
- Posting of key date valuation of the designated portion of the FX Transaction with actual NPV values
- Posting of classification of the selected Hedging Relationship with actual NPV component values
- Update amounts of Reclassification Update Types
- Fix scheduled Reclassification Updated Types

|  |
| --- |
| Note This step is only necessary when you can see the Bal.Sheet Recognition Date for new Hedging Relationship in step Automatically Update Original Hedging Relationship and Create New Hedging Relationship (Planned Designation), and this Bal.Sheet Recognition Date is between previous period end closing and maturity date of Securing FX Transaction. |

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see section [Business Conditions](#unique_6) [page ] 6. And market date should be valid at the Balance Sheet Recognition Date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions (TPM120) screen displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions (TPM120) screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, <Balance Sheet Recognition Date of new Hedging Relationship you noted down in step Automatically Update Original Hedging Relationship and Create New Hedging Relationship (Planned Designation)>Transaction Selection: <select this radio button>Transaction Number: <the transaction number of Securing FX Forward Transaction>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions (TPM120) screen displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions (TPM120) screen, choose Execute. | The Hedging Relationships screen displays, and Hedging Relationships have been processed without errors. |  |
| 5 | Display Log of Hedge Management | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Log.In the Information Overview dialog box, choose Hedge Management. | The Information Overview screen displays, you can check the Classification Log on this screen. |  |
| 6 | Display Log of Posting | Choose Back.In the Information Overview dialog box, choose Posting Log. | The Posting Log: Posted Business Transactions screen displays, you can check the following postings on this screen:ValuationClassificationReclassification (depend on the setting of field Balance Sheet Recognition on tab Hedge Accounting I of the Hedging Area) |  |

#### Contract Maturity for Securing FX Transaction

##### (1X1) Foreign Currency Risk Management and (1X9) Foreign Currency Risk Management – Group Ledger IFRS

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the Securing FX Forward Transaction is mature, the relevant posting and payment process steps for closing this FX transaction (which is Hedging Instruments in Hedging Relationship) should be same as a normal FX transaction (which is not in a Hedging Relationship), relevant process steps are described in test scripts Foreign Currency Risk Management(1X1) and Foreign Currency Risk Management – Group Ledger IFRS(1X9).

Procedure

Perform the following steps in section Foreign Currency Risk Management and Accounting - Without Options of test script Foreign Currency Risk Management(1X1) for the Securing FX Forward Transaction:

| Step Name in 1X1 | Mandatory/Optional for Continuing Testing 2UF | Purpose |
| --- | --- | --- |
| Generate Payment Request for Mature Transaction | Mandatory | Generate payment request for outgoing payment of FX transactions at Value Date via app Fix, Pay and Post Flows (TBB1). |
| Process Payment Request | Optional | Process the payment run procedure for payment request and create posting for outgoing payment via app Automatic Payment Transactions for Payment Requests (F111). |
| Post to General Ledger | Mandatory | Post the flow of incoming payment at value date of FX transaction in valuation area AE0 (local GAAP) via app Fix, Pay and Post Flows (TBB1);Post the flow of outgoing payment at value date of FX transaction in valuation area AE0 (local GAAP) via app Process Business Transactions (TPM10). |
| Post Realized Profit and Loss | Mandatory | Post realized profit or loss at value date of FX transaction in valuation area AE0 (local GAAP) via app Post Derived Business Transactions (TPM18). |

Perform the following step in test script Foreign Currency Risk Management – Group Ledger IFRS(1X9) for the Original FX Forward Transaction and the Securing FX Forward Transaction:

| Step Name in 1X9 | Mandatory/Optional for Continuing Testing 2UF | Purpose |
| --- | --- | --- |
| Post Flows to General Ledger (Parallel Valuation Area) | Mandatory | Post the relevant flows (incoming and outgoing payment) at value date of FX transactions in valuation area 002 (IFRS) via app Process Business Transactions (TPM10). |

##### Process Dedesignation for New Hedging Relationship at Maturity Date of Securing FX Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the maturity date (value date) of Securing FX Forward Transaction, you run the app Release Hedging Business Transactions (TPM120), the following activities are done by this app:

- Calculation and saving of NPV for FX Transaction in new Hedging Relationship.
- Calculation and saving of NPV component values for FX Transaction and Hypothetical Derivative in new Hedging Relationship.
- Posting of key date valuation of Securing FX Forward Transaction with actual NPV values.
- Posting of classification of the new Hedging Relationships with designated portion of actual NPV component values.
- Transfer Position Amounts from Designated to Free Standing Subposition.
- Update amounts of Reclassification Update Types.
- Fix scheduled Dedesignation Updated Types.

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see section [Business Conditions](#unique_6) [page ] 6. And market date should be valid at the maturity date of FX transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions (TPM120) screen displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions (TPM120) screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, <the maturity date of Securing FX Forward Transaction>Transaction Selection: <select this radio button>Transaction Number: <the transaction numbers of Securing FX Forward Transaction>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions (TPM120) screen displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions (TPM120) screen, choose Execute. | The Hedging Relationships screen displays, and Hedging Relationship has been processed without errors. |  |
| 5 | Display Log of Hedge Management | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Log.In the Information Overview dialog box, choose Hedge Management. | The Information Overview screen displays, you can check the Classification Log on this screen. |  |
| 6 | Display Log of Posting | Choose Back.In the Information Overview dialog box, choose Posting Log. | The Posting Log: Posted Business Transactions screen displays, you can check the postings on this screen. |  |

Use app Post Derived Business Transactions (TPM18) to fix the derived business transactions for FX transaction at contract close date:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Fix and Post Derived Business Transactions screen, enter the following data:Sub-area Product Groups:OTC Transactions: <select this checkbox>Sub-area General Selections:Company Code: for example, 3310Valuation Area: for example, 002Sub-area OTC Transactions:OTC Transactions: <the transaction numbers of Securing FX Forward Transaction>Sub-area Selections for Fixing Derived Business Transactions:TRL Date: <the maturity date of Securing FX Forward Transaction>Sub-area Posting Control:Test Run: <select this checkbox>Choose Execute.If message No scheduled derived business transactions were found for the selection displays, then there is no derived transaction available for your selection, you can skip current step.If message Are you sure that you want to select future business transactions? displays, press Enter | The FX Transaction to be fixed and posted (test run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 4 | Fix and Post for Test run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the simulated postings. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the initial screen of this app.Change the following data and choose Execute:Test Run: <deselect this checkbox>If message Are you sure that you want to select future business transactions? displays, press Enter | The FX Transaction to be fixed and posted (production run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 6 | Fix and Post for Production run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the postings for IFRS (valuation area 002), accounting document has been created in corresponding ledger in Financial Accounting. |  |

#### Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date of New Hedging Relationship

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Reclassification of the Hedging Reserve and Cost of Hedging Reserve position amounts for the new Hedging Relationship is executed at the end date of its Exposure Subitem within the Derived Business Transaction Framework: the app Post Derived Business Transactions (TPM18) for the fixation and posting of Derived Business Transactions selects the Exposure Subitem position flows to be reclassified.

Postings are created for reclassification of Hedging Reserve and Cost of Hedging Reserve position amounts; P/L ineffective position amounts are fixed only.

|  |
| --- |
| Note This step creates postings only when the relevant Split ID on tab Hedge Accounting I of the Hedging Area uses the following parameters for the field Balance Sheet Recognition:0 or Blank - None: the accumulated Hedging Reserve and Cost of Hedging Reserve between Designation Date and Dedesignation Date are reclassified at the end date of Exposure Subitem.2 - Reclassification at the End Date of the Exposure Subitem: the accumulated Hedging Reserve and Cost of Hedging Reserve between Designation Date and Balance Sheet Recognition Date are reclassified at the end date of Exposure Subitem.If 1 - Immediate Reclassification at Balance Sheet Recognition Date is given for field Balance Sheet Recognition, reclassification has been done at the Balance Sheet Recognition Date by using app Release Hedging Business Transactions (TPM120).If 3 - Reclassification at Deviant Reclassification Date is given for field Balance Sheet Recognition, reclassification should be done at the Deviant Reclassification Date by using app Release Hedging Business Transactions. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Fix and Post Derived Business Transactions screen, enter the following data:Sub-area Product Groups:OTC Transactions: <deselect this checkbox>Exposure Items: <select this checkbox>Sub-area General Selections:Company Code: for example, 3310Valuation Area: for example, 002Sub-area Selections for Fixing Derived Business Transactions:TRL Date: <the Exposure Subitem End date of new Hedging Relationship you noted down in step Automatically Update Original Hedging Relationship and Create New Hedging Relationship (Planned Designation)>Sub-area Exposure Items -> Additional Selections:Transaction Number: <the transaction number of securing FX Forward Transaction>Sub-area Posting Control:Test Run: <select this checkbox>Choose Execute.If message Are you sure that you want to select future business transactions? displays, press Enter | The Exposure Subitem to be fixed and posted (test run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 4 | Fix and Post for Test run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the simulated reclassification postings of Hedging Reserve and Cost of Hedging Reserve for IFRS (valuation area 002). |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the initial screen of this app.Change the following data and choose Execute:Test Run: <deselect this checkbox>If message Are you sure that you want to select future business transactions? displays, press Enter | The Exposure Subitem to be fixed and posted (production run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 6 | Fix and Post for Production run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the postings for IFRS (valuation area 002), accounting document has been created in corresponding ledger in Financial Accounting. |  |

#### Reporting

##### Display Treasury Position Flows

Purpose

In this step, you check the position flows of FX transactions and exposure subitems.

Procedure

For details please see the same step in test script Hedge Accounting for FX Forward – Group Ledger IFRS(1XD).

##### Display Treasury Posting Journal

Purpose

In this step, you check the posting journals of FX transactions and exposure subitems.

Procedure

For details please see the same step in test script Hedge Accounting for FX Forward – Group Ledger IFRS(1XD)

##### Display Treasury Position Values

Purpose

In this step, you check the position values of FX transactions and exposure subitems.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Treasury Position Values - Classic (TPM12). | The Treasury Position Values - classic screen displays. |  |
| 3 | Enter Selection Criteria | On the Treasury Position Values - classic screen, enter the following data and choose Execute:Product Group: <select OTC Transactions and Exposure Items>Company Code: for example, 3310Valuation Area: for example, AE0In the OTC transactions area, enter the following data:Transaction: <The transaction number(s)>In the Exposure Items area, enter the following data:Select From OTC Transactions: <select>In the Control Parameters area, enter the following data:Key Date: for example, <last date of current month>No Zero Positions: <select>Included Planned Data: <select> | Position values of FX transaction and Exposure Subitems are displayed in area List of Position Values for Key Date.If you would like to see Hedging Instrument number, Hedged Item number and other amount relevant fields, please find the field Subpositions, you can kick in the button Display Subpositions to check the detailed information. |  |

## Appendix

### Process Integration

Purpose

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

Purpose

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| (1X1) Foreign Currency Risk Management | As a prerequisite for running current test script, an appropriate business partner (counterparty) must exist, please follow preliminary step Create Business Partner in test script Foreign Currency Risk Management (1X1) to create a business partner.Optional: as a prerequisite for running current test script when using Designation Type which requires counterconfirmation, correspondence process should be proceeded, therefore correspondence setting should be maintained for business partner in advance, please see preliminary step Maintain Profile and BP Group Assignments to External Recipient in test script Foreign Currency Risk Management (1X1) for correspondence setting. This is optional.Optional: please follow preliminary step Maintaining Credit Limit in test script Foreign Currency Risk Management (1X1) to maintain credit limits. This is optional. |
| (1XN) Market Rates Management – Manually via Upload | As perquisites for running current test script, execute the following steps in test script Market Rates Management – Manually via Upload (1XN) to maintain the necessary market data manually for hedge accounting:Enter FX Spot RatesEnter Interest RatesCreate Reference Entities for Business PartnersAssign Attributes to Evaluation TypeMaintain Reference EntitiesEnter Credit SpreadsEnter Basis Spreads |

### Termination of Hedging Instrument

Purpose

In FX swap scenario, if the hedging instrument is terminated, the hedging accounting is discontinued.

Basically, there are two cases:

- One leg or both legs of the FX swap are terminated, then the new hedging relationship will be discontinued.
- The original FX forward transaction is terminated, then the original hedging relationship and the new hedging relationship will be discontinued.

In this section, you terminate the original FX forward transaction and discontinue original and new hedging relationships. In case that one leg or both legs of the FX swap are terminated, you can also refer to the steps in this section.

#### Create, Submit and Release Termination Request for Hedging Instrument

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In some cases, you may need to terminate a hedging instrument for some reason, for example, if a long-run plain vanilla FX option or zero/low cost collar FX option is over-hedged.

After aligning with your counterpart, you decide to terminate the hedging instrument. You start the termination process via termination request in hedge management cockpit. In this step, you select the hedging instrument in the hedge management cockpit to create and submit a termination request. The request needs to be released after it is submitted.

Prerequisites

1. You have created an original FX forward transaction has been created, and its status has been set to Contract Settlement.
2. You have created the original hedging relationship containing the original FX forward transaction, and released the designation.
3. You have submitted and released the FX swap request, and have created the FX swap, and both of its legs have been set to the Contract Settlement status.
4. You have created the new hedging relationship containing the original FX forward transaction and FX swap, and has released the designation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Hedge Management Cockpit (TOENE) |  |  |
| 3 | Enter Selection Criteria | Make the following entries, and choose Start:Hedging Area: For example, HA0003Layout ID: 2R_TQ_CH | The Hedge Management Cockpit for Hedging Area HA0003 is displayed with Net Hedges |  |
| 4 | Create Termination Request | Double click on key figure Net Hedges in the period of the value date of the forward transaction you just created as prerequisite.Select the transaction you just created, click Hedge Request and choose Termination Request in the dropdown list | The Create Hedge Request screen is displayed. |  |
| 5 | Submit Termination Request | Enter description for edge request: terminate forwardEnter the following data on the General tab, and choose Submit:Hedge Request Reason: Choose S003 Overhedge Processing - TerminationNote Overruling not allowed | Terminate Request is submitted with termination request ID.Remember Note down the ID. |  |
| 6 | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start:Hedging Area: for example, HA0003 | Hedge requests that match the filter criteria are displayed. |  |
| 8 | Release Termination Request | Select the row of the Termination Request you just submitted and choose Process and then select Release from the dropdown list. | Log is displayed that the termination request was released. |  |

#### Terminate Hedging Instrument

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you terminate the original FX forward transaction before its maturity.

Once hedging instrument is terminated, the termination request is set to completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06) | The Forex: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the original FX transaction number> | A list of FX transactions is displayed in the Forex: Collective Processing - Results area. |  |
| 4 | Terminate the Transaction | Select the checkbox of the transaction to be terminated in the Forex: Collective Processing - Results area, and choose Terminate. | The Terminate Forex Transaction: Structure screen is displayed. |  |
| 5 | Save the Termination | On the Terminate Forex Transaction: Structure screen, the value of field Activity in header is 3 - Termination.Enter the following data in the Termination sub-area, and choose Save:Date: <the termination data, it should be a date between swap date and value date of original FX forward transaction>Payment Date: for example, <termination data + 2 days>Entry Type: for example, RateRate: for example, 1.16If the Document lines: Display messages dialogue box is displayed, choose Continue (Enter). | The payment amount for termination is calculated and the transaction is saved with status Termination. |  |
| 6 | Access the SAP Fiori App | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start.:Hedging Area: for example, HA0003 | hedge requests that match the filter criteria are displayed. |  |
| 8 | Check Termination Request Status | Status of the termination request is Completed. |  |  |

#### Set Termination Settlement Status for Hedging Instrument

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the original FX forward transaction is terminated in the system, the status of transaction needs to be set to Termination Settlement before you could create postings for termination flow. Usually it is done after back office receive the incoming confirmation about termination from counterparty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. |  |  |
| 2 | Access the SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06) | The Forex: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the original FX transaction number> | A list of FX transactions is displayed in the Forex: Collective Processing - Results area. |  |
| 4 | Settle the Termination | Select the checkbox of the transaction to be settled in the Forex: Collective Processing - Results area, and choose Settle. | The Settle Forex Transaction: Structure screen is displayed. |  |
| 5 | Save the Termination Settlement | On the Settle Forex Transaction: Structure screen, the value of field Activity in header is 4 - Termination Settlement.Choose Save.If the Document lines: Display messages dialogue box is displayed, choose Continue (Enter). | The transaction is saved with status Termination Settlement. |  |

#### Process Dedesignation for Hedging Business Transaction at Termination Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the hedging business transactions on the termination date, and the hedging relationships are then dedesignated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions screen is displayed. |  |
| 3 | Release Hedging Business Transaction | On the Release Hedging Business Transactions screen, enter the following data, and choose Execute:Company code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, <the termination date>Transaction Selection: <select this radio button>Transaction Number: <transaction numbers of the original FX Forward transaction and two legs of FX swap>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions is displayed. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions screen, choose Execute. | The Hedging Relationships screen is displayed, and hedging relationships have been processed for termination of hedging instrument without errors. |  |

|  |
| --- |
| Note If you check the relevant hedging relationships in the Manage Hedging Relationships (TPM100) and change the display date to the termination date, you will find the status of these hedging relationships becomes Dedesignated.If you terminate one leg or both legs of FX swap, then only the new hedging relationship is dedesignated. |

#### Post Flows for Termination

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post operative flows and derived flows on the payment date of termination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Fix, Pay and Post Flows (TBB1) | The Treasury: Post Flows screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Post Flows screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the original FX transaction number terminated>Up to and Including Due Date: <the payment date of termination>Test Run: for example, <deselect this checkbox>Post All Valuation Areas: for example, <select this radio button> | The Information Overview dialog box is displayed. |  |
| 4 | Check Posting Log | In the Information Overview dialog box, choose Posting Log. | Posting journals are displayed. |  |

|  |
| --- |
| Note If termination results in outgoing payment with a payment request, please refer to the Foreign Currency Risk Management (1X1) test script for automatic payment of payment requests.Reclassification of Hedging Reserve and Cost of Hedging Reserve should be executed on the Exposure Subitem End Date, which is same with the normal hedge accounting process without termination of hedging instrument. |

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

In this step, you run simulated valuation to check the balance sheet and P&L figures between two period-end closings.

For Hedge Accounting for FX Swap, the following Simulated Valuation processes are supported:

- Valuation of Treasury Positions
- Classification of Hedging Relationships

|  |
| --- |
| Note You need to run the simulated valuation of the FX Transaction before or together with the simulated classification of the Hedging Relationship, otherwise an error message will be displayed indicating the simulated valuation is not available. |

Prerequisite

NPV values of the FX Transaction as well as the component NPV values need to be stored before the valuation and classification processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Simulate Period-End Closing (TPM_SIM_VAL). | The Simulate Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Simulate Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, 002Product Type: for example, 60ATransaction Number: for example, < Transaction Number created in previous steps>Recalculate Outdated Sim.Val.: <deselect this checkbox>Note If you set this indicator, you can recalculate the outdated simulation results.Simulation Date: for example, <the current date>Key Date Valuation : <select this checkbox>Accrual/Deferral: <deselect this checkbox>Classification : <select this checkbox>Test Run: <select this checkbox> | The Messages dialog box is displayed and the following message is displayed:Processed xx positions; xx successful, 0 failedIf Recalculate Outdated Simulation Results has been executed, the following message is displayed:xx simulated results deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
| 4 | Execute Simulated Valuation | The Message dialog box is displayed, and choose Continue. | The Simulate Period-End Closing screen is displayed.You can check the simulated valuation information for IFRS (valuation area 002). Please note there is no simulated valuation created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the initial screen of this app is displayed.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The dialog Messages screen is displayed. |  |
| 6 | Execute Simulated Valuation for Production Run | The Message dialog box is displayed, choose Continue. | The Simulate Period-End Closing screen is displayed.You can check the simulated valuation information for IFRS (valuation area 002). |  |

#### Delete Simulated Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you reverse the simulated valuation.

Prerequisite

The simulated valuation has been executed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Delete Results of Simulated Period-End Closing (TPM_SIM_VAL_DEL). | The Delete Results of Simulated Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Delete Results of Simulated Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: <leave bank, or enter specific valuation are, for example, 002>Product Type: for example, 60ATransaction Number: for example, < the transaction number you noted down in the previous steps>Simulation Date: for example, <the date on which the reversal takes place>Test Run: <select this checkbox> | The Messages dialog box is displayed and the following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |
| 4 | Enter Selection Criteria for Production Run | Go back to the initial screen of this app.On the Delete Results of Simulated Period-End Closing screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Messages dialog box is displayed and the following message is displayed:XX simulated results deleted forkey date (the date on which the reversal takes place) |  |

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
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-forward-group-ledger-us-gaap-3x3-ae-986]]
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-group-ledger-ifrs-2rw-ae-test-script-85]]
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-group-ledger-us-gaap-3x4-ae-test-script]]
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-local-gaap-3x2-ae-985]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UF_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 200,364 chars in the whole document
