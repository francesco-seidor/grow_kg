---
id: 05-treasury-and-cash-management/test-script-hedge-accounting-for-fx-forward-group-ledger-ifrs-1xd-ae-7
title: "Test Script: Hedge Accounting for FX Forward – Group Ledger IFRS (1XD_AE) (1XD_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script (scope item 1XD, AE) for IFRS 9 cash flow hedge accounting with FX forwards/NDF, from hedging area to reporting."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/hedge-accounting-fx]
aliases: [1XD_S4CLD2608_BPD_EN_AE]
keywords: [Hedge Accounting for FX Exposures, hedge accounting, hedging area, hedging classification, raw exposure, hedge management cockpit, fx forward transactions, hedging relationship designation, period end closing, balance sheet reclassification]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XD_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-779
topic: 05-treasury-and-cash-management/hedge-accounting-fx
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Hedge Accounting for FX Forward – Group Ledger IFRS (1XD_AE) (1XD_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XD_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Hedge Accounting for FX Exposures** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Hedge Accounting for FX Forward – Group Ledger IFRS (1XD_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848372)

[2 Prerequisites 4](#_Toc232848373)

[2.1 System Access 4](#_Toc232848374)

[2.2 Roles 4](#_Toc232848375)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232848376)

[2.4 Business Conditions 5](#_Toc232848377)

[3 Overview Table 7](#_Toc232848378)

[4 Test Procedures 10](#_Toc232848379)

[4.1 FX Forwards as Hedging Instruments 10](#_Toc232848380)

[4.1.1 Define or Adjust Hedging Area 11](#_Toc232848381)

[4.1.2 Collect and Determine Exposure Data 22](#_Toc232848382)

[4.1.3 Create Raw Exposure 22](#_Toc232848383)

[4.1.4 Take Snapshot 24](#_Toc232848384)

[4.1.5 Review Net Open Exposure in Hedge Management Cockpit 25](#_Toc232848385)

[4.1.6 Agree on Hedging Instrument 26](#_Toc232848386)

[4.1.7 Check Limit Utilization Report (Optional) 26](#_Toc232848387)

[4.1.8 Create Foreign Exchange Contract with Hedging Classification 27](#_Toc232848388)

[4.1.8.1 Create Deliverable Forward Transaction 27](#_Toc232848389)

[4.1.8.2 Create Non-Deliverable Forward (NDF) Transaction 29](#_Toc232848390)

[4.1.9 Automatic Designation (Planned) 31](#_Toc232848391)

[4.1.10 Set Contract Settlement Status with Incoming Confirmation 36](#_Toc232848392)

[4.1.11 Release Hedging Relationship 37](#_Toc232848393)

[4.1.12 Period End Closing 40](#_Toc232848394)

[4.1.12.1 Calculate NPV of Hedging Instrument and Hypothetical Derivative 40](#_Toc232848395)

[4.1.12.2 Run Key Date Valuation 42](#_Toc232848396)

[4.1.12.3 Run Classification 45](#_Toc232848397)

[4.1.13 Process Reclassification for Hedging Business Transaction at Balance Sheet Recognition Date 48](#_Toc232848398)

[4.1.14 Contract Maturity 50](#_Toc232848399)

[4.1.14.1 (1X1) Foreign Currency Risk Management and (1X9) Foreign Currency Risk Management – Group Ledger IFRS 50](#_Toc232848400)

[4.1.14.2 Process Dedesignation for Hedging Business Transaction at Maturity Date for Hedging Instrument 51](#_Toc232848401)

[4.1.15 Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date 54](#_Toc232848402)

[4.1.16 Reporting 56](#_Toc232848403)

[4.1.16.1 Display Treasury Position Flows 56](#_Toc232848404)

[4.1.16.2 Display Treasury Posting Journal 57](#_Toc232848405)

[4.1.16.3 Display Treasury Position Values 58](#_Toc232848406)

[5 Appendix 60](#_Toc232848407)

[5.1 Process Integration 60](#_Toc232848408)

[5.1.1 Preceding Processes 60](#_Toc232848409)

[5.2 Overhedge Processing - Dedesignation 61](#_Toc232848410)

[5.2.1 Create Raw Exposure 61](#_Toc232848411)

[5.2.2 Take Snapshot 63](#_Toc232848412)

[5.2.3 Create and Submit Dedesignation Request 63](#_Toc232848413)

[5.2.4 Release Dedesignation Request 65](#_Toc232848414)

[5.2.5 Process Dedesignation for Hedging Business Transaction 67](#_Toc232848415)

[5.3 Effectiveness Test 68](#_Toc232848416)

[5.3.1 Create Market Data Set 69](#_Toc232848417)

[5.3.2 Adjust Hedging Area 70](#_Toc232848418)

[5.3.3 Create Foreign Exchange Contract with Hedging Classification 71](#_Toc232848419)

[5.3.4 Automatic Designation (Planned) 72](#_Toc232848420)

[5.3.5 Release Hedging Relationship with Prospective Effectiveness Test 72](#_Toc232848421)

[5.4 Termination of Hedging Instrument 74](#_Toc232848422)

[5.4.1 Create, Submit and Release Termination Request for Hedging Instrument 74](#_Toc232848423)

[5.4.2 Terminate Hedging Instrument 75](#_Toc232848424)

[5.4.3 Set Termination Settlement Status for Hedging Instrument 77](#_Toc232848425)

[5.4.4 Process Dedesignation for Hedging Business Transaction at Termination Date 78](#_Toc232848426)

[5.4.5 Post Flows for Termination 79](#_Toc232848427)

[5.5 Simulated Valuation 80](#_Toc232848428)

[5.5.1 Run Simulated Valuation 80](#_Toc232848429)

[5.5.2 Delete Simulated Valuation 82](#_Toc232848430)

## Purpose

Overview

The Hedge Management and Hedge Accounting process helps you to mitigate profit and loss volatility from the use of derivatives.

Currently, the scope item supports IFRS 9 and covers Cash Flow Hedge using FX Forwards (including NDF) as Hedging Instruments.

The functionality helps you to automate labor-intensive processes, such as calculating net open exposure amount, creating hedging relationship for hedge item and hedge instrument, determining the key figures calculation (NPV, Forward, CCBS, CVA/DVA), performing the valuation of FX transaction, checking classification, dealing with the dedesignation, and generating posting journal reports.

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

Use your own master data or the following sample data to go through the test procedure.

| Master Data | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Valuation Area | 002 |  |  |
| Hedging Area | HA0001 |  |  |
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
| 1XN - Market Rates Management – Manually via Upload | Market data has been maintained. As a prerequisite for running the current test script, execute the following steps in test script 1XN - Market Rates Management – Manually via Upload to maintain the necessary market data manually for hedge accounting:Enter FX Spot RatesEnter Interest RatesCreate Reference Entities for Business PartnersAssign Attributes to Evaluation TypeMaintain Reference EntitiesEnter Credit SpreadsEnter Basis Spreads |
| 1X1 - Foreign Currency Risk Management | (Optional) Correspondence setting has been maintained for business partner. As a prerequisite for running the current test script when using Designation Type which requires counterconfirmation, correspondence process should be proceeded. Therefore correspondence setting should be maintained for business partner in advance. See preliminary step Maintain Profile and BP Group Assignments to External Recipient in test script 1X1 - Foreign Currency Risk Management for correspondence setting. |
| 1X1 - Foreign Currency Risk Management | (Optional) Credit limits have been maintained. Please follow preliminary step Maintaining Credit Limit in test script 1X1 - Foreign Currency Risk Management to maintain credit limits, this is optional. |

## Overview Table

The scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

FX Forwards as Hedging Instruments:

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Define or Adjust Hedging Area](#unique_8) [page ] 11 | Treasury Specialist - Middle Office | Define Hedging Area (TOE_HEDGING_AREA) | Hedging Area is created or extended. |
| [Collect and Determine Exposure Data](#unique_9) [page ] 22 | Treasury Specialist - Middle Office | N/A | Exposure data has been appropriately prepared outside of SAP system. |
| [Create Raw Exposure](#unique_10) [page ] 22 | Treasury Specialist - Middle Office | Process Raw Exposure (FTREX1) | Raw exposure has been created and released. |
| [Take Snapshot](#unique_11) [page ] 24 | Treasury Specialist - Middle Office | Take Snapshot (TOESNAP) | Snapshot of exposures has been created. |
| [Review Net Open Exposure in Hedge Management Cockpit](#unique_12) [page ] 25 | Treasury Specialist - Middle Office | Hedge Management Cockpit (TOENE) | Exposure, net exposure, net open exposure has been reviewed in app Hedge Management Cockpit. |
| [Agree on Hedging Instrument](#unique_13) [page ] 26 | Treasury Specialist - Middle Office | N/A | Related teams and organizations have agreed on which financial instruments should be used as hedging instruments. |
| [Check Limit Utilization Report (Optional)](#unique_14) [page ] 26 | Treasury Specialist - Middle Office | Review Limit Utilizations (TBLB) | Limit utilization has been checked. |
| [Create Foreign Exchange Contract with Hedging Classification](#unique_15) [page ] 27 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) | FX transactions have been created. |
| [Create Deliverable Forward Transaction](#unique_16) [page ] 27 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) | Deliverable Forward Transaction created and saved. |
| [Create Non-Deliverable Forward (NDF) Transaction](#unique_17) [page ] 29 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) | NDF transaction data entered and created |
| [Automatic Designation (Planned)](#unique_18) [page ] 31 | Treasury Specialist - Back Office | Manage Hedging Relationships (TPM100) Process Spots/Forwards - Collective Processing (TX06) Reprocess Transactions - Automated Designation (TPM104) | Automatic designation has been created in status 'Planned Designation'. |
| [Set Contract Settlement Status with Incoming Confirmation](#unique_19) [page ] 36 | Treasury Specialist - Back Office | Process Spots/Forwards - Collective Processing (TX06) | Status of transaction becomes 'Contract Settlement'. |
| [Release Hedging Relationship](#unique_20) [page ] 37 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120) Reverse Release of Hedging Business Transactions (TPM121) | Designation has been released, hypothetical derivative has been created, NPV and market value components have been calculated at the designation date. |
| [Period End Closing](#unique_21) [page ] 40 |  |  |  |
| [Calculate NPV of Hedging Instrument and Hypothetical Derivative](#unique_22) [page ] 40 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA) | NPV and market value components have been calculated at period end. |
| [Run Key Date Valuation](#unique_23) [page ] 42 | Treasury Accountant | Run Valuation (TPM1) Reverse Valuation (TPM2) | Valuation posting has been created for FX transaction at period end. |
| [Run Classification](#unique_24) [page ] 45 | Treasury Accountant | Run Classification (TPM101) Reverse Classification (TPM102) | Classification posting has been created on Exposure Subitem level at period end. |
| [Process Reclassification for Hedging Business Transaction at Balance Sheet Recognition Date](#unique_25) [page ] 48 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120) | Hedging Business Transaction has been processed at the balance sheet recognition date for crossover. |
| Contract Maturity |  |  |  |
| [(1X1) Foreign Currency Risk Management and (1X9) Foreign Currency Risk Management – Group Ledger IFRS](#unique_26) [page ] 50 | Treasury Specialist - Back Office Treasury Accountant | Fix, Pay and Post Flows (TBB1) Automatic Payment Transactions for Payment Requests (F111) Process Business Transactions (TPM10) Post Derived Business Transactions (TPM18) | The postings for closing FX transactions in operative valuation area AE0 and parallel valuation area 002 have been created. |
| [Process Dedesignation for Hedging Business Transaction at Maturity Date for Hedging Instrument](#unique_27) [page ] 51 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120) | Hedging Business Transaction has been processed at the maturity date of hedging instrument. |
| [Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date](#unique_28) [page ] 54 | Treasury Accountant | Post Derived Business Transactions (TPM18) | Reclassification postings have been created and relevant flows have been fixed at the end date of exposure subitem. |
| Reporting |  |  |  |
| [Display Treasury Position Flows](#unique_29) [page ] 56 | Treasury Accountant | Display Treasury Position Flows (F1754) | Position flows for FX transaction and exposure subitem are checked. |
| [Display Treasury Posting Journal](#unique_30) [page ] 57 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Posting journals for FX transaction and exposure subitem are checked. |
| [Display Treasury Position Values](#unique_31) [page ] 58 | Treasury Accountant | Display Treasury Position Values (F1867) | Position values for FX transaction and exposure subitem are checked. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### FX Forwards as Hedging Instruments

Purpose

This section covers the Hedge Management and Hedge Accounting process for forecast cashflows in foreign currencies according to a company’s hedging policy. The hedging instruments are FX forward contracts.

The treasury department is responsible for executing a given hedging policy for hedging the risk of forecast cashflows in foreign currencies of future periods. The forecast itself is represented as exposures in the Hedge Management Cockpit. A snapshot is taken for the forecast exposures from Exposure Management. Based on the snapshot, net open exposure amount, risk currency, and period are detailed in the Hedge Management Cockpit. Based on the hedging policy rules, the net open exposures are reduced by trading financial instruments such as an FX forward transaction. For expected inflows of a risk currency, the resulting exposure are closed by a FX forward that sells the inflow currency and buys the local currency of the company code. For expected outflows, a FX forward transaction is traded that buys the outflow currency and sells the local currency.

With the creation of the FX forward transaction, the financial transaction is automatically designated into a Hedging Relationship as a Hedging Instrument together with the exposure item of the Hedge Management Cockpit as Hedged Item. The matching exposure item is determined based on characteristics of the Hedging Instrument (for example, hedging classification, position currency of financial transaction, or maturity of financial transaction). At the same time, the Hypothetical Derivative is created and all necessary mathematical evaluations necessary for the measurement of ineffectiveness are performed and stored. For changes to the FX forward transaction, the Hedging Relationships are updated accordingly.

At period end, the determination of NPVs including the decomposition of market values for Hedging Instrument and the Hypothetical Derivative is performed, and the key date valuation of the FX forward transactions is executed. Meanwhile, the measurement and postings of the Hedging Reserve (OCI I), Cost of Hedging Reserve (OCI II), and ineffectiveness are executed on exposure subitem level. The period-end close can be executed using two different procedures: valuation and classification with Reset or without Reset.

At the Balance Sheet Recognition Date, the Reclassification Flows are automatically created. Depending on the rule that was set in the Hedging Area Definition, the Reclassification Flows are posted immediately or at the Exposure Subitem End Date or at a Deviant Reclassification Data.

With the maturity of the FX forward transaction, the cumulated Hedging Reserve and Cost of Hedging Reserve amounts are classified as frozen. At the end date of the Exposure Subitem, the cumulated Hedging Reserve and Cost of Hedging Reserve amounts are to be reclassified to profit or loss as a reclassification adjustment.

This section can be executed using different product types as Hedging Instruments:

- 60A: FX forward transaction which is Deliverable
- 60B: FX forward transaction which is Non-deliverable

#### Define or Adjust Hedging Area

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The hedging area is an entity that represents a section of hedging policy of the company. The creation of a Hedging Area is a necessary requirement to start the process of Hedge Management and Hedge Accounting. It is the central steering entity that contains all relevant settings for this process.

|  |
| --- |
| Note In this section, as an example, one single Hedging Area HA0001 for Hedge Accounting is created. During testing, HA0001 can be shared by different company codes from different countries with different local currencies. |

- As the first tester to run this test script in system, please create new Hedging Area HA0001 by following Option 1: Create a New Hedging Area.
- If you find out that the Hedging Area HA0001 already exists in the system, you create a new version for HA0001 and extend it by entering specific parameters of your company code/country, that is Option 2: Extend an Existing Hedging Area.

A company can have multiple Hedging Areas for Hedge Accounting according to its hedging policy. However, a hedge accounting relevant Hedging Classification can only be assigned to one Hedging Area for Hedge Accounting, therefore creating additional Hedging Area means the necessity of defining additional Hedging Classifications. Hedging Classification is a configuration which should be done via configuration step Define Hedging Classifications.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

|  |
| --- |
| Note 8 Hedging Classifications are pre-defined for IFRS 9 Cash Flow Hedge of FX risk by using FX Forwards: |

- YFC00: Spot Element of FX forward contract is Hedging Reserve (OCI I), Forward Element and Cross Currency Basis Spread of FX forward contract is Cost of Hedging Reserve (OCI II); Valuation will be carried out when releasing the designation. YFC00 should be always bundled with Hedging Profile F00 when maintaining tab Hedge Accounting II of a Hedging Area.
- YFC01: Spot Element of FX forward contract is Hedging Reserve (OCI I), Forward Element and Cross Currency Basis Spread of FX forward contract is Cost of Hedging Reserve (OCI II): No valuation will be carried out when releasing the designation. YFC01 should be always bundled with Hedging Profile F01 when maintaining tab Hedge Accounting II of a Hedging Area.
- YFC02: Spot Element and Forward Element of FX forward contract is Hedging Reserve (OCI I), Cross Currency Basis Spread of FX forward contract is Cost of Hedging Reserve (OCI II); Valuation will be carried out when releasing the designation. YFC02 should be always bundled with Hedging Profile F02 when maintaining tab Hedge Accounting II of a Hedging Area.
- YFC03: Spot Element and Forward Element of FX forward contract is Hedging Reserve (OCI I), Cross Currency Basis Spread of FX forward contract is Cost of Hedging Reserve (OCI II); No valuation will be carried out when releasing the designation. YFC03 should be always bundled with Hedging Profile F03 when maintaining tab Hedge Accounting II of a Hedging Area.
- YFC04: Spot Element of FX forward contract is Hedging Reserve (OCI I), Forward Element, Cross Currency Basis Spread and Others Element of FX forward contract is Cost of Hedging Reserve (OCI II); Valuation will be carried out when releasing the designation. YFC04 should be always bundled with Hedging Profile F04 when maintaining tab Hedge Accounting II of a Hedging Area.
- YFC05: Spot Element of FX forward contract is Hedging Reserve (OCI I), Forward Element, Cross Currency Basis Spread and Others Element of FX forward contract is Cost of Hedging Reserve (OCI II): No valuation will be carried out when releasing the designation. YFC05 should be always bundled with Hedging Profile F05 when maintaining tab Hedge Accounting II of a Hedging Area.
- YFC06: Spot Element and Forward Element of FX forward contract is Hedging Reserve (OCI I), Cross Currency Basis Spread and Others Element of FX forward contract is Cost of Hedging Reserve (OCI II); Valuation will be carried out when releasing the designation. YFC06 should be always bundled with Hedging Profile F06 when maintaining tab Hedge Accounting II of a Hedging Area.
- YFC07: Spot Element and Forward Element of FX forward contract is Hedging Reserve (OCI I), Cross Currency Basis Spread and Others Element of FX forward contract is Cost of Hedging Reserve (OCI II); No valuation will be carried out when releasing the designation. YFC07 should be always bundled with Hedging Profile F07 when maintaining tab Hedge Accounting II of a Hedging Area.

|  |
| --- |
| Note Please note that only hedging classifications YFC00 - YFC03 will be used in hedging area HA0001; YFC04 - YFC07 will be assigned to another hedging area HA0003 which is described in test script Hedge Accounting for FX Swap – Group Ledger IFRS(2UF) supporting IFRS 9. In real business environment, YFC00 - YFC07 can be assigned to single hedging area. |

Procedure

Option 1: Create a New Hedging Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Define Hedging Area (TOE_HEDGING_AREA). | The Define Hedging Area (TOE_HEDGING_AREA) screen displays. |  |
| 3 | Enter Hedging Area ID | On the Display Hedging Area screen, enter the following data and choose Create:Hedging Area: for example, HA0001 | Dialog box Create Hedging Area displays.If message Hedging area HA0001 already existsdisplays, please skip Option 1 and go to execute Option 2: Extend an Existing Hedging Area. If you find the parameters mentioned in Option 2 have been maintained, you can also skip Option 2, |  |
| 4 | Enter Data in Dialog Box Create Hedging Area | In the dialog box Create Hedging Area, enter the following data and choose Create:Hedging Area: for example, HA0001Description: for example, Hedging Area for Hedge Accounting using FX ForwardAuthorization Group: for example, HAG01Valid From: for example, <first day of current year>Without Template: <Choose this radio button> | The Change Hedging Area screen displays. |  |
| 5 | Enter Data on Tab Main Data | On the tab Main Data, enter the following data:Local Currency: <Choose this radio button>Note If you want to enable extraction of cross-currency exposures, please choose Currency Defined by the Source. By doing so, the risk-free currency is derived from the currency pair of the exposure item. If the source is Exposure Management, the risk-free currency is the target currency. If the source is Cash Management, the risk-free currency is the company code currency.Calendar Related: <choose this radio button>Number of Periods: for example, 12Period Length: for example, <Month>Hedge Accounting: <Choose this checkbox>Product Type for Exposure Subitems: 91AActivate SAP Trading Platform Integ.: <choose this checkbox>.You only choose this checkbox in case of testing integration with trading platform. | Data on tab Main Data has been maintained. |  |
| 6 | Enter Data on Tab General Settings | Choose the tab General Settings, and enter the following data:Company Code: for example, 3310In sub-area Differentiation Criteria: for example, select the checkbox of differentiation criterion Currency and Company CodeIn sub-area Hedging Classification:Choose Add Hedging Classification, and enter the following data:Hdg Class.DescriptionYFC00FX Risk; CFH; Spot, Forward + CCBS; with 1st Day ResultYFC01FX Risk; CFH; Spot, Forward + CCBS; w/o 1st Day ResultYFC02FX Risk; CFH; Forward + Spot, CCBS; with 1st Day ResultYFC03FX Risk; CFH; Forward + Spot, CCBS; w/o 1st Day Result | Data on tab General Settings has been maintained. |  |
| 7 | Enter Data on Tab Currencies | Choose the Currencies tab.In sub-area Hedging-Relevant Currencies, choose Add Currency, and enter the currencies which will be used as risk currencies in later steps in current test script. For example:USDBRL | Data on tab Currencies has been maintained. |  |
| 8 | Enter Data on Tab Filters for Exposures | Choose the Filters for Exposures tab.In the sub-area Filter List for Exposures, choose Create Filter.In the dialog box New Filter for Exposures, enter the following data and choose Create Filter:Filter: for example, FLT_EXPFilter Description: for example, <Filter for Exposures>Source: E_EM2In the sub-area Other Filter - Specific Selections , enter the following data:Exposure Position Type: YFXNoteYou may also use E_FXEM Foreign Exchange Exposure Management instead of E_EM2 Exposure Management 2.0 as the data source for exposures.If you use E_FXEM Foreign Exchange Exposure Management as the data source for exposures, you will have to use app Manage FX Exposures (F7990) instead of app Process Raw Exposure (FTREX1) to create and submit the FX Exposure. | Data on tab Filters for Exposures has been maintained. |  |
| 9 | Enter Data on Tab Filters for Hedges | Choose the Filters for Hedges tab.In the sub-area Filter List for Hedges, choose Create Filter.In the dialog box New Filter for Hedges, enter the following data and choose Create Filter:Filter: for example, FLT_HDGFilter Description: for example, <Filter for Hedges>Source: H_TMIn the sub-area Other Filter - Specific Selections, enter the following data:Product Type: firstly enter 60A, then choose Multiple selection of filed Product Type. In the Multiple Selection for Product Type dialog box, add another product type 60B, and choose Copy (F8). | Data on tab Filters for Hedges has been maintained. |  |
| 10 | Enter Data on Tab Hedge Accounting I | Choose the Hedge Accounting I tab.In sub-area Designation Level, choose Insert, and enter the following data:Company Code: for example, 3310Valuation Area: 002Designation Level: Choose G (Gross Exposure Item with Larger Absolute Value) if it is not selected by defaultSplitting: for example, 1 (Active)Sequence: for example, N (No Consumption Sequence)In sub-area Designation Activation, choose Insert, and enter the following data:CoCodeVACurrencyDesig.3310002USD1 (Active)3310002BRL1 (Active)Note If you choose Currency Defined by the Source on the Main Data tab, another column for Target Currency is displayed, then you can maintain target currency here.In sub-area Designation Splitting, choose Insert, and enter the following data:Company Code: for example, 3310Valuation Area: 002Risk Currency: for example, USDNote If you choose Currency Defined by the Source on the Main Data tab, another column for Target Currency is displayed, then you can maintain target currency here.Direction: for example, I (Incoming)Split ID: for example, 1Splitting Ratio: for example, 100Reclassification Offset Category: for example, 4 (Due Date HInst + PT)Balance Sheet Recognition: 1 (Immediate Reclassification at Balance Sheet Recognition Date)Extend Hypothetical Derivative Period: for example, 1 (Yes)Payment Term (Days): for example, 10Enter another row in sub-area Designation Splitting:Company Code: for example, 3310Valuation Area: 002Risk Currency: for example, BRLDirection: for example, I (Incoming)Split ID: for example, 1Splitting Ratio: for example, 100Reclassification Offset Category: for example, 4 (Due Date HInst + PT)Balance Sheet Recognition: <Keep blank>Extend Hypothetical Derivative Period: for example, 1 (Yes)Payment Term (Days): for example, 15Note Split ID is the numerical identifier that is used to number the different designation splits: 1, 2, 3, etc.The sum of the splitting ratios of corresponding Split IDs for a specific combination of Company Code, Valuation Area, Risk Currency, and Direction should be 100.Note With the Reclassification Offset Category, you define the date on which the reclassification of Hedging Reserve and Cost of Hedging Reserve, for example, when 4 (Due Date HInst + PT) is selected, reclassification date = maturity date of hedging instrument + payment term.Note Only enter a value for Balance Sheet Recognition when your scenario is balance sheet crossover (from Cash Flow Hedge to Fair Value Hedge), The Balance Sheet Recognition Date = Maturity Date of Hedging Instrument - Payment Term.The different types of reclassification depend on the company code and distinguish the reclassification of Hedging Reserve and Cost of Hedging Reserve amounts which were classified for the Hedging Relationship up to and equal to the Balance Sheet Recognition Date:• 1 - Immediate Reclassification at Balance Sheet Recognition Date• 2 - Reclassification at the End Date of the Exposure Subitem: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until end date of the Exposure Subitem.• 3 - Reclassification at Deviant Reclassification Date: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until the Deviant Reclassification Date = Due Date of Hedging Instrument + DIO (Days Inventory Outstanding) - Payment Term..Note When you choose to extend the period of the hypothetical derivative (value for field Extend Hypothetical Derivative Period is 1 - Yes), the due date of the hypothetical derivative = maturity date of the hedging instrument + payment term. If you do not want to extend the hypothetical derivative period, the due date of the hypothetical derivative = maturity date of the hedging instrument. | Data on tab Hedge Accounting I has been maintained. |  |
| 11 | Enter Data on Tab Hedge Accounting II | Choose the Hedge Accounting II tab.In sub-area Designation Control, choose Insert, and enter the following data:CoCodeVAHdg Class.Des. TypePType ESIHdgProfileMDS ID3310002YFC00YFX1WF003310002YFC01YFX1WF013310002YFC02YFX1WF023310002YFC03YFX1WF03Note YFX1W is a designation type that doesn't require counterconfirmation. There is another designation type YFX1C that requires counterconfirmation.When using YFX1C, hedging relationship can be released only after the corresponding hedging instrument has been successfully counterconfirmed, which requires to use correspondence functionality.PType ESI is to assign different product types for different exposure items classified by hedging classification. If you want to use just one product type maintained in the Main Data tab for all exposure items, please keep field PType ESI blank here.MDS ID (Market Data Set ID) is used for Effectiveness Test. Leave the column MDS ID blank since Test Procedures do not include process steps of Effectiveness Test. Furthermore, special hedging profile should be used for Effectiveness Test, You can find more details regarding Effectiveness Test in Appendix – Effectiveness Test. | Data on tab Hedge Accounting II has been maintained. |  |
| 12 | Save the Hedging Area | Choose Save (Ctrl+S). | Message Hedging area HA0001 version 001 saved displayed.The Hedging Area for Hedge Accounting has been created successfully. |  |

Option 2: Extend an Existing Hedging Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Define Hedging Area (TOE_HEDGING_AREA). | The Define Hedging Area (TOE_HEDGING_AREA) screen displays. |  |
| 3 | Enter Hedging Area ID | On the Display Hedging Area screen, enter the following data and choose Display:Hedging Area: for example, HA0001 | Hedging Area HA0001 is displayed. |  |
| 4 | Create New Version | Choose New Version.In the dialog box Create New Version of Hedging Area HA0001, enter the following data and choose Create:Valid From: for example, <current date> | The Change Hedging Area screen displays. |  |
| 5 | Update Data on Tab General Settings | Choose the tab General Settings, choose the button Multiple selection of field Company Code.In the dialog box Multiple Selection for Company Code, add company code 3310 into the area Select Single Values, and choose Copy (F8). | Data on tab General Settings has been updated. |  |
| 6 | Update Data on Tab Currencies | Choose the tab Currencies.In sub-area Hedging-Relevant Currencies, choose Add Currency, and enter the currencies (if they have not been maintained) which will be used as risk currencies in later steps in current test script. For example:USDBRL | Data on tab Currencies has been updated. |  |
| 7 | Update Data on Tab Hedge Accounting I | Choose the Hedge Accounting I tab.In sub-area Designation Level, choose Insert, and enter the following data:Company Code: for example, 3310Valuation Area: 002Designation Level: Choose G (Gross Exposure Item with Larger Absolute Value) if it is not selected by defaultSplitting: for example, 1 (Active)Sequence: for example, N (No Consumption Sequence)In sub-area Designation Activation, choose Insert, and enter the following data:CoCodeVACurrencyDesig.3310002USD1 (Active)3310002BRL1 (Active)In sub-area Designation Splitting, choose Insert, and enter the following data:Company Code: for example, 3310Valuation Area: 002Currency: for example, USDDirection: for example, I (Incoming)Split ID: for example, 1Ratio: for example, 100Reclassification Offset Category: for example, 4 (Due Date HInst + PT)Balance Sheet Recognition: 1 (Immediate Reclassification at Balance Sheet Recognition Date)Extend Hypothetical Derivative Period: for example, 1 (Yes)Payment Term (Days): for example, 10Enter another row in sub-area Designation Splitting:Company Code: for example, 3310Valuation Area: 002Currency: for example, BRLDirection: for example, I (Incoming)Split ID: for example, 1Ratio: for example, 100Reclassification Offset Category: for example, 4 (Due Date HInst + PT)Balance Sheet Recognition: <Keep blank>Extend Hypothetical Derivative Period: for example, 1 (Yes)Payment Term (Days): for example, 15Note Split ID is the numerical identifier that is used to number the different designation splits: 1, 2, 3, etc.The sum of the splitting ratios of corresponding Split IDs for a specific combination of Company Code, Valuation Area, Risk Currency, and Direction should be 100.Note With the Reclassification Offset Category, you define the date on which the reclassification of Hedging Reserve and Cost of Hedging Reserve, for example, when 4 (Due Date HInst + PT) is selected, reclassification date = maturity date of hedging instrument + payment term.Note Only enter a value for Balance Sheet Recognition when your scenario is balance sheet crossover (from Cash Flow Hedge to Fair Value Hedge), The Balance Sheet Recognition Date = Maturity Date of Hedging Instrument - Payment Term.The different types of reclassification depend on the company code and distinguish the reclassification of Hedging Reserve and Cost of Hedging Reserve amounts which were classified for the Hedging Relationship up to and equal to the Balance Sheet Recognition Date:• 1- Immediate Reclassification at Balance Sheet Recognition Date• 2- Reclassification at the End Date of the Exposure Subitem: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until end date of the Exposure Subitem.• 3 - Reclassification at Deviant Reclassification Date: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until the Deviant Reclassification Date = Due Date of Hedging Instrument + DIO (Days Inventory Outstanding) - Payment Term..Note When you choose to extend the period of the hypothetical derivative (value for field Extend Hypothetical Derivative Period is 1 - Yes), the due date of the hypothetical derivative = maturity date of the hedging instrument + payment term. If you do not want to extend the hypothetical derivative period, the due date of the hypothetical derivative = maturity date of the hedging instrument. | Data on tab Hedge Accounting I has been updated. |  |
| 8 | Update Data on Tab Hedge Accounting II | Choose the Hedge Accounting II tab.In sub-area Designation Control, choose Insert, and enter the following data:CoCodeVAHdg Class.Des. TypePType ESIHdgProfileMDS ID3310002YFC00YFX1WF003310002YFC01YFX1WF013310002YFC02YFX1WF023310002YFC03YFX1WF03Note YFX1W is a designation type doesn't require counterconfirmation. There is another designation type YFX1C which requires counterconfirmation.When using YFX1C, hedging relationship can be released only after the corresponding hedging instrument has been successfully counterconfirmed, which requires correspondence functionality.MDS ID (Market Data Set ID) is used for Effectiveness Test. Leave the column MDS ID blank since Test Procedures do not include process steps of Effectiveness Test. Furthermore, special hedging profile should be used for Effectiveness Test, You can find more details regarding Effectiveness Test in Appendix – Effectiveness Test. | Data on tab Hedge Accounting II has been updated. |  |
| 9 | Save the Hedging Area | Choose Save (Ctrl+S). | Message Hedging area HA0001 version XXX saved displayed.The Hedging Area for Hedge Accounting has been extended to support your company code/country testing successfully. |  |

#### Collect and Determine Exposure Data

Purpose

The middle office collects exposure data based on forecast cash flows in risk currencies from various sources. They consolidate the exposure data to enter it into the SAP system as Raw Exposures. The exposure data should be aggregated in granularity which differentiates:

- Company code
- Risk currency
- The period when the exposure is due

Procedure

This step is done outside of the SAP system.

#### Create Raw Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The creation and subsequent release of a Raw Exposure leads to the creation of a derived Exposure Position (automatic released).

|  |
| --- |
| Note As an example, how to manually key in Raw Exposure is introduced in current step. Besides manually key in Raw Exposure, you can also import Raw Exposures from spreadsheet, for details please see Option 2: Import the raw exposures from spreadsheet of step Create Raw Exposure in test script Foreign Currency Risk Management (1X1). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Raw Exposure (FTREX1). | The Raw Exposure: Initial screen displays. |  |
| 3 | Enter Selection Criteria | On the Raw Exposure: Initial screen, enter the following data and choose Create.Exposure Activity Type: for example, YFXINote If the direction of consolidated FX exposure is outgoing, use Exposure Activity Type YFXO. | The Raw Exposure Maintenance: Create screen displays. |  |
| 4 | Enter Header Data | On the Raw Exposure Maintenance: Create screen and tab Header Data, enter the following data:Default Exposure Category: for example, 01 (Forecasted Transaction)Company Code: for example, 3310Cirt4ExpPosType: FX (FX Exposure)Direction: for example, IN (Incoming Cash Flow)Note Cirt4ExpPosType is a criterion used to derive the Exposure Position Type YFX which you entered on tab Filters for Exposures of Hedging Area.Note If you use Exposure Activity Type YFXO on previous screen, please enter Direction OUT (Outgoing Cash Flow) on this screen. | Necessary header data is entered. |  |
| 5 | Enter Line Item Data | Choose tab Line Item Data.In sub-area Raw Exposure Line Item, choose Create New Line Item, and enter the following data:Exposure Due Date : for example: <Current date + 2 Months>Exposure Amount: for example, 1000000Exposure Amount Currency: for example, USDTarget Currency: for example, AEDChoose Create New Line Item again, and create another raw exposure line item:Exposure Due Date : for example: <Current date + 2 Months>Exposure Amount: for example, 2000000Exposure Amount Currency: for example, BRLTarget Currency: for example, AED | Necessary line item data is entered. |  |
| 6 | Save Raw Exposure | Choose Save. | A dialog box displays, and states that:Raw exposure has been saved;Raw exposure has been released;Position IDs have been updated.You can check Exposure Position and Exposure Position Flows via app Process Exposure Positions and Display Exposure Position Flows. |  |

#### Take Snapshot

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You take a snapshot of the exposure data belonging to specific hedging area. For further processing of Hedge Management and Hedge Accounting, it is mandatory to rely on fully versioned data. This ensures that an auditor can check at all times the data that served as the basis for a hedging decision.

The selected incoming or outgoing exposures and the exposure items are saved in the database, and can be reviewed via the Hedge Management Cockpit (TOENE) app in the next step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Take a Snapshot | Open Take Snapshot (TOESNAP). | The Take Snapshot (TOESNAP)screen displays. |  |
| 3 | Enter General Selections | Enter the following data and choose Run:Hedging Area: for example, HA0001Description: for example, Snapshot for hedge accounting using FX ForwardDay Reference: <select>Extraction Date: for example , <the current date> | The Display logs screen displays and the snapshot is created. |  |

#### Review Net Open Exposure in Hedge Management Cockpit

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the exposure data based on the snapshot from the prior step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Hedge Management Cockpit (TOENE). | The Hedge Management Cockpit for Hedging Area view displays. |  |
| 3 | Enter Selection Criteria | Enter the following data and choose Start:Hedging Area: for example, HA0001Layout ID: for example, 1R_ALL_CHNote You can also choose alternative layout ID 1C_CURR_OV - Currency Pairs Overview (Key Figures in Columns) or 1C_ALL_CH - All Characteristics (Key Figures in Columns).Choose Manage Layouts. Create a layout on the Layout Overview view. | The Hedge Management Cockpit for Hedging Area HA0001 view displays.The amounts of exposures are reflected in specific cells for differentiation criteria of raw exposures you created previously (company code, risk currency, period of due date, incoming/outgoing indicator of Exposure Activity Type).Select a cell and choose Drilldown (cell) to display more detailed information for Exposure Item, Exposure Position, or Raw Exposure.Note If you choose Currency Defined by the Source and exposure items are created based on the cross-currency exposures during snapshot, the hedge management cockpit displays the Target Currency, Risk Currency and Company Code Currency |  |

#### Agree on Hedging Instrument

Purpose

The middle office analyzes the exposure data for FX risk with related teams and organizations. The middle office and related teams agree on the financial instruments to use as hedging instruments. In this section, FX forward transactions are used as hedging instruments.

Procedure

This step is done outside of the SAP system.

#### Check Limit Utilization Report (Optional)

Purpose

Before the front office trades a financial instrument with counterparty, the middle office usually checks the limit utilization status to see if there is enough credit limit for trading new deals.

Prerequisites

Credit limits are maintained. For more information, see the [Business Conditions](#unique_6) [page ] 5 section.

Procedure

Because this step is not a key process in Hedge Accounting, this step is optional. To check limit utilization, see the Check Limit Utilization Report step in the Foreign Currency Risk Management (1X1) test script.

#### Create Foreign Exchange Contract with Hedging Classification

Purpose

In this step, you create FX Forward transactions as hedging instruments.

The saving of the FX Transaction with a Hedge Accounting-specific Hedging Classification initiates the Hedge Accounting processing:

- According to the Contract Start Date and Hedging Classification, a valid Hedging Area is determined.
- According to the differentiating criteria (currency, company code, etc.) of the Hedging Area and by means of the Contract Start and Value Date, the Exposure Item of the Snapshot is determined.
- According to the settings of the Designation Splitting of the Hedging Area, one Hedging Relationship or multiple Hedging Relationships are created.

Prerequisites

Business partner has been created, please see section [Business Conditions](#unique_6) [page ] 5.

If you used the Designation Type which requires counterconfirmation in step [Define or Adjust Hedging Area](#unique_8) [page ] 11, hedging relationship can be released only after the FX transaction has been successfully counterconfirmed, you need to run the correspondence process which will set the status of FX transaction to 'Counterconfirmed' automatically after receiving the incoming confirmation from counterparty, and correspondence setting should be maintained for business partner before creating a FX transaction (please see section [Business Conditions](#unique_6) [page ] 5).

##### Create Deliverable Forward Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Spot/Forward Transaction Entry: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: 60ATransaction Type: 102Partner: for example, 33537001 | The Spot/Forward Transaction Entry: Structure screen displays. |  |
| 4 | Enter Data on Tab Structure | On the Structure tab, enter the following data:Rate: for example, AED/USD1.15Buy/Sell: for example, SellTraded Amt: for example, USD800000Value Date: for example, <Current date + 2 Months>Contract Date: for example, <Current date>Note The currency of Traded Amt should be the risk currency. The amount of Traded Amt should be less or equal to the amount of Raw Exposure Line Item for this risk currency you created previously.Note The Value Date of FX transaction should be within the same period as the due date of exposure.Note You Buy risk currency (Traded Amt) if it is outgoing exposure. | Data on the Structure tab has been entered. |  |
| 5 | Enter Data in Administration tab | Choose the Administr. tab, and enter the following data:Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: for example, YFC01 (FX Risk; CFH; Spot, Forward + CCBS; w/o 1st Day Result)Note When a FX hedge request ID is entered in a deal the corresponding exposure item is automatically assigned in the FX Hedge Management tab.Note The appropriate General Valuation Class will derive the correct Position Management Procedure for Hedge Accounting in valuation area 002 for IFRS.In operative valuation area AE0, a Position Management Procedure for non-Hedge Accounting is determined. | Data on the Administr. tab has been entered. |  |
| 6 | Save the FX Transaction | Choose Save. | Dialog box Document lines: Display messages displays, and shows no warning message Reprocessing of financial transaction required after save about auto designation could not be finished.Choose Continue (Enter), message Financial transaction saved under number XXXXXXXXXXXXX displays.Note down the transaction number. |  |

##### Create Non-Deliverable Forward (NDF) Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can create non-deliverable forward (NDF) transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Spot/Forward Transaction Entry: Initial screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: 60BTransaction Type: 110Partner: for example, 33537001 | The Spot/Forward Transaction Entry: Structure screen displays. |  |
| 4 | Enter Data on Tab Structure | On the Structure tab, enter the following data:Rate: for example, AED/BRL 3.65Buy/Sell: for example, SellTraded Amt: for example, BRL 1500000Value Date: for example, <Current date + 2 Months>Fixing Date: for example, <Current date + 2 Months - 2 Days>Contract Date: for example, <Current date>Note The currency of Traded Amt should be the risk currency. The amount of Traded Amt should be less or equal to the amount of Raw Exposure Line Item for this risk currency you created previously.Note The Value Date of FX transaction should be within the same period as the due date of exposure.Note You Buy risk currency (Traded Amt) if it is outgoing exposure. | Data on tab Structure has been entered. |  |
| 5 | Enter Data in Administration tab | Choose the Administr. tab, and enter the following data:Gen. Valn Class: for example, 45 Derivatives: Cash FlowHdg Classific.: for example, YFC02 (FX Risk; CFH; Forward + Spot, CCBS; with 1st Day Result)The appropriate General Valuation Class will derive the correct Position Management Procedure for Hedge Accounting in valuation area 002 for IFRS.In operative valuation area AE0, a Position Management Procedure for non-Hedge Accounting is determined.Note When a FX hedge request ID is entered in a deal the corresponding exposure item is automatically assigned in the FX Hedge Management tab. | Data on tab Administr. has been entered. |  |
| 6 | Save the FX Transaction | Choose Save.Note If below error message occurs, please use configuration activity Define leading currency (101026) to maintain the currency pair.No currency pair is defined for currencies XXX BRL | Dialog box Document lines: Display messages displays, and shows no warning message Reprocessing of financial transaction required after save about auto designation could not be finished.Choose Continue (Enter), message Financial transaction saved under number XXXXXXXXXXXXX displays.Note down the transaction number. |  |

|  |
| --- |
| Note After the FX transaction is saved, you can logon as Treasury Specialist - Middle Office and open app Hedge Management Cockpit (TOENE) to check the net open exposure again.In app Hedge Management Cockpit (TOENE), the amounts of FX transactions will be reflected in corresponding cells for Key Figure Name Net Hedges and relevant company code, risk currency and period; Net Open Exposure should be reduced accordingly. |

#### Automatic Designation (Planned)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With saving the FX forward transaction, the Exposure Item in a snapshot is found and the Hedging Relationship is automatically created in status Planned Designation, the Exposure Item is determined based on attributes of the relevant Snapshot and Hedging Area and FX forward transaction.

This step introduces how to check the automatically created Hedging Relationship.

|  |
| --- |
| Note The automated designation of a FX transaction into a hedging relationship is prevented if the calculated Balance Sheet Recognition Date is earlier than or on the same date as the Designation Date (Contract Date), and the portion of the FX Transaction is processed as freestanding position. |

Procedure

Option 1: via app Manage Hedging Relationships

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Manage Hedging Relationships (TPM100). | The Manage Hedging Relationships screen displays. |  |
| 3 | Enter Selection Criteria | On the Manage Hedging Relationships screen, choose the Selection tab on the left side of screen, and enter the following data:Find: All Hedging RelationshipsBy: Hedging InstrumentCompany Code: for example, 3310Valuation Area: 002Product Group: select the checkbox of OTC Trans., and choose OTC Transactions Selection beside OTC Trans.. In the OTC Transactions Selection dialog box, enter the transaction number(s) you noted down in the previous step, then choose Continue (Enter).Choose Start. | The list of Hedging Relationship Number(s) displays on bottom-left side of screen. You may need to zoom out the screen in web browser to see it.Note down the Hedging Relationship Number(s). |  |
| 4 | Display Header of Hedging Relationship | Double click a HR Number from bottom-left side of screen, the detailed information of Hedging Relationship will display on right side of screen.Check the data of Hedge Relationship Header. | The header of Hedging Relationship displays on upper-right side of screen, it provides details which are relevant for the Hedging Relationship as general entity.The Hedging Relationship Status should be Planned Designation since it has not been released.Choose Display All Flows, you can check the created flows resulting from the Designation.Choose Display H.Rel. Related Trans, in Hedge Related Transactions for Hedging Relationship dialog box, double click the row of Business Transaction Category Designation, then you can see the designation details in Designation of Hedging Relationship dialog box. |  |
| 5 | Display Tab Hedging Relationship Detail | Check the data of the Hedge Relationship Details tab. | The Hedging Relationship Detail tab contains information about:Risk Type and Risk Profile DetailsDate information on Hedging Relationship levelThe following fields are automatically populated:Risk Currency: your exposure currencyNote If you choose Currency Defined by the Source and exposure items are created based on the cross-currency exposures, the Target Currency is displayed in the Hedge Relationship Details.Profile: the Hedging Profile which is mapped (on tab Hedge Accounting II of Hedging Area) to the Hedging Classification you used when created FX transaction.Category: Cash Flow HedgeRisk Indicator: Currency RiskValid-From Date: contract date of FX TransactionPlanned Designation Date: contract date of FX TransactionPlanned Dedesign. Date: Value Date of FX TransactionBal.Sheet Rec.Date: the Balance Sheet Recognition Date of crossoverNote down the Balance Sheet Recognition Date.Reclassification Date: the Deviant Reclassification Date other than the Balance Sheet Recognition Date and the End Date of the Exposure Subitem, the Deviant Reclassification Date = Due Date of Hedging Instrument + DIO (Days Inventory Outstanding) - Payment Term.Designation Type: the Designation Type which is mapped (on tab Hedge Accounting II of Hedging Area) to the Hedging Classification you used when created FX transactionNote The Balance Sheet Recognition Date is only available when you gave value 1 or 2 or 3 for the field Balance Sheet Recognition in sub-area Designation Splitting on tab Hedge Accounting I of the Hedging Area.The Reclassification Date is only available when you gave value 3 for the field Balance Sheet Recognition in sub-area Designation Splitting on tab Hedge Accounting I of the Hedging Area. |  |
| 6 | Display Tab Hedged Item | Choose tab Hedged Item, and check data of it. | The Hedged Item tab contains information about:Hedged Item DetailsPosition Management information of the Exposure SubitemThe following fields are automatically populated:Number: generated numberNote down the Hedged Item Number.Start Date: contract date of FX TransactionEnd Date: it is determined by the parameters you entered in sub-area Designation Splitting on the Hedge Accounting I tab of the Hedging Area, it is the date on which reclassification of OCI I and OCI II should carry out (except the case that Immediate Reclassification at Balance Sheet Recognition Date, or Reclassification at Deviant Reclassification Date). Note down this date.Category: Planned ForecastHypothetical Derivative: empty at this moment, it will be created after designation is released.Product Group: ExposuresValuation Class: determined from pre-defined configuration on Product Type levelExposure Item ID: generated number. Note down the Exposure Item ID.Exposure Subitem ID: generated number. Note down the Exposure Subitem ID. |  |
| 7 | Display Tab Hedging Instrument | Choose the Hedging Instrument tab, and check data of it. | The Hedging Instrument tab contains information about:Hedging Instrument DetailsPosition Management information of the Hedging InstrumentThe following fields are automatically populated:Number: generated numberNote down the Hedging Instrument Number.Product Group: OTC Transactions: Money Market, FX, DerivativesValuation Class: derived from pre-defined configuration and the General Valuation Class you chose when created FX transactions.Transaction Number: the FX transaction number you created in previous step.Start Date: Contract Date of FX transactionEnd Date: Value Date of FX Transaction |  |

Option 2: via app Process Spots/Forwards (Subtitle: Collective Processing)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06). | The Forex: Collective Processing screen displays. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the FX transaction number(s) you created in previous step> | The list of FX transaction(s) displays in area Forex: Collective Processing - Results. |  |
| 4 | Display Transaction | Select the checkbox of a transaction in area Forex: Collective Processing - Results, and choose Display. | The Display Forex Transaction: Structure screen displays. |  |
| 5 | Display the Hedging Relationship | Choose tab Administr., choose Show Hedging Relationship.On the List of Hedging Relationships screen, select the checkbox of a Hedging Relationship, and then choose Display Hedging Rel.. | The P-Hedge Accounting screen displays, you can check detailed information of Hedging Relationship just like in app Manage Hedging Relationships (TPM100). |  |

|  |
| --- |
| Note If you cannot see the Hedging Relationship for your FX transaction via app Manage Hedging Relationships (TPM100) or Process Spots/Forwards (Subtitle: Collective Processing), or message Reprocessing of financial transaction required after save displays when you saved the FX transaction in step [Create Foreign Exchange Contract with Hedging Classification](#unique_15) [page ] 27, the system did not finish the automated designation of the financial transaction and exposure. To analyze the error situation and postprocess the financial transaction for the designation, use app Reprocess Transactions (Subtitle: Automated Designation), for details please see the procedure as below: |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Reprocess Transactions - Automated Designation (TPM104). | The Reprocess Financial Transactions for Automated Designation screen displays. |  |
| 3 | Enter Selection Criteria | On the Reprocess Financial Transactions for Automated Designation screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 002Transaction: <the FX transaction number(s) you created in previous step> | The Transaction Numbers screen displays.If you cannot see any transaction on this screen, please skip current step because automated designation is created for the transaction(s) you selected on previous screen. |  |
| 4 | Display Log | Select the checkbox of a transaction, and choose Display Log. | The Messages dialogue displays, and you can see the relevant message and figure out why automated designation failed. |  |

#### Set Contract Settlement Status with Incoming Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once an FX transaction is saved in the system, the status of transaction needs to be set to Contract Settlement before you could create postings for flow. Usually it is done after you receive the incoming confirmation from counterparty. You can settle the transaction via the following ways once you get counterparty confirmation:

- Option 1: Manual Settlement via app Process Spots/Forwards (Subtitle: Collective Processing)
- Option 2: Automatic settlement via Correspondence Process

In this step, we only proceed Option 1 - Manual Settlement.

As described in section Prerequisites of step [Create Foreign Exchange Contract with Hedging Classification](#unique_15) [page ] 27: If you used the Designation Type which requires counterconfirmation, you need to run the correspondence process which will set the status of FX transaction to Counterconfirmed automatically after receiving the incoming confirmation from counterparty. The correspondence setting should be maintained for business partner before creating a FX transaction (please see section [Business Conditions](#unique_6) [page ] 5).

For details regarding how to do Automatic Settlement via Correspondence Process, please see the Correspondence with PDF Form chapter in the Foreign Currency Risk Management(1X1) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. |  |  |
| 2 | Access the SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06) | The Forex: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data and choose Run:Company Code: for example, 3310Transaction: <the FX transaction number(s)> | A list of FX transactions is displayed in the Forex: Collective Processing - Resultsarea. |  |
| 4 | Settle the Transaction | Select the checkbox of a transaction in area Forex: Collective Processing - Results, and choose Settle. | The Settle forex transaction: Structure screen is displayed. |  |
| 5 | Save the Change | On the Settle Forex Transaction: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If the Document lines: Display messages dialogue displays, choose Continue (Enter). | The transaction is saved with status Contract Settlement. |  |

#### Release Hedging Relationship

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the automated designation which is in status Planned Designated. After release, the status will become Designated.

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system. Please see the [Business Conditions](#unique_6) [page ] 5 section.

If you use the Designation Type which requires counter-confirmation in step [Define or Adjust Hedging Area](#unique_8) [page ] 11, hedging relationship can be released only after the FX transaction has been successfully counterconfirmed. You need to run step Correspondence with PDF Form in test script Foreign Currency Risk Management(1X1), the correspondence process in 1X1 will set the status of FX transaction to Counterconfirmed automatically after receiving the incoming confirmation from counterparty.

|  |
| --- |
|  |

|  |
| --- |
| Note Open the configuration step Define Hedging Profiles, find out the hedging profiles you maintained in the tab of hedging area HA0001, and deselect the checkbox Documentation Optional (Yes/No) for each hedging profile, otherwise the Hedge Documentation cannot be displayed when releasing the hedging relationship. |

Procedure

Release Hedging Relationship:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions (TPM120) screen, enter the following data:Company code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, <current date>Transaction Selection: <select this radio button>Transaction Number: the FX transaction number(s)Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new Release Hedging Business Transactions screen is displayed. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions screen, choose Run. | The Hedging Relationships screen displays, and Hedging Relationship has been released without errors. |  |
| 5 | Check Market Data Calculation Details | Choose Display Market Value Calculation Details. | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays. You can see the details of the calculation of the full NPV as well as the Hedge Accounting Key Figures. The offered detail lists and analysis options are the same as the ones available in app Calculate Net Present Values (Subtitle: with CVA and DVA).Choose Hedge Accounting Key Figures, you can see the amounts of different components (spot, forward, CCBS, and other components) of FX transaction and hypothetical derivative.Go back to the Hedging Relationships screen. |  |
| 6 | Check Hedging Relationship | On the Hedging Relationships screen, select the checkbox of a HR Number, choose DisplayHedging Relationships. | The screen Manage Hedging Relationships displays, and you can see Hedging Relationship Status is now Designated.Choose the Hedged Item tab, you can see the field Hypothetical Derivative has been filled with a generated number. |  |
| 7 | Display Hedge Documentation | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Hedge Documentation. | The Hedging Relationship Documentation in PDF format will be opened. |  |

(Optional) Reverse Release of Hedging Relationship:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Reverse Release of Hedging Business Transactions (TPM121). | The Reverse Release of Hedging Business Transactions (TPM121) screen displays. |  |
| 3 | Enter Selection Criteria | On the Reverse Release of Hedging Business Transactions screen, enter the following data:Company code: for example, 3310Valuation Area: for example, 002Date to be Reversed: for example, <the contact date of transaction>Transaction Selection:<select this radio button>Transaction Number: <the FX transaction number(s)>Reversal Reason: for example, 04Enter Rev.Date: <select this checkbox>Test Run: <deselect this checkbox>On the next screen Reverse Hedging Business Transactions, choose Run. | The Hedging Relationships screen displays, and Release of Hedging Relationship has been reversed without errors. |  |
| 4 | Check Hedging Relationship | Select the checkbox of a HR Number, and choose Display Hedging Relationship. | The screen P-Hedge Accounting displays, and you can see Hedging Relationship Status is returned to Planned Designation. |  |
| 5 | Release Hedging Relationship Again | Open the Release Hedging Business Transactions (TPM120) app, and release the Hedging Relationship again (follow introductions in Release Hedging Relationship), otherwise you will not be able to continue the testing. | Hedging Relationship is released again. |  |

#### Period End Closing

|  |
| --- |
| Note This test script only introduces the period end closing activities of valuation area 002 (IFRS 9 Hedge Accounting).For period end closing activities of valuation area AE0 (local GAAP, non-Hedge Accounting), please see steps under node Period end has been reached in Foreign Currency Risk Management and Accounting - Without Options of test script SAP Fiori Analytical Apps for Treasury and Risk Management(1X1). |

##### Calculate NPV of Hedging Instrument and Hypothetical Derivative

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you calculate the Net Present Values (Fair Values) of FX Transactions and corresponding Hypothetical Derivatives at the month end. The system also calculates market value components (spot, forward, CCBS, and other components) for FX Transactions and corresponding Hypothetical Derivatives, Credit Value Adjustment/Debit Value Adjustment of FX transactions are decomposed as well.

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in the system. Please see section [Business Conditions](#unique_6) [page ] 5.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments screen is displayed. |  |
| 3 | Enter Selection Criteria and Execute | On the Determine NPVs Including Credit and Debit Value Adjustments screen, enter the following data:Sub-area Selection Mode:Evaluation Parameter Derivatn: <select this checkbox>Select OTC Transactions: <select this checkbox>Market Value Decomposition: <select this checkbox>Sub-area Common Selection Criteria:Company Code: for example, 3310Valuation Area: for example, 002Sub-area OTC Transaction Selection Criteria:Transaction: <the FX transaction number(s)>Sub-area Evaluation Parameters:Evaluation Date: for example, <last date of current month>Sub-area Save Results:Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detail Log: <select this checkbox>Choose Run. | The NPVs including CVA/DVA from the Market Risk Analyzerscreen is displayed.You can see the NPV, risk-free NPV, CVA/DVA of each transaction on this screen.You can also check different information by clicking on buttons:Single Transaction:CVA/DVA Key FiguresHedge Accounting Key FiguresDetailed LogCalculation BasesError LogHedge Accounting Key Figures provides a list showing the detailed amount information of market value components (spot, forward, CCBS, others) for FX Transactions and corresponding Hypothetical Derivatives. |  |

##### Run Key Date Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You use the valuation function to evaluate the positions of FX transactions based on the previously calculated NPVs, and transfer results to financial accounting.

Prerequisites

NPVs and market value components values have been calculated for FX transitions and Hypothetical Derivatives in valuation area 002 (IFRS).

Procedure

Run Valuation:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Run valuation screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run Valuation screen, enter the following data:Sub-area Product Groups:OTC Transactions: <select this checkbox>Sub-area General Selections:Company code: for example, 3310Valuation Area: for example, 002Sub-area OTC Transactions:Transaction: <the FX transaction number(s)>Sub-area Valuation Parameters:Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation without ResetNote You can also use Mid-year Valuation with Reset. In addition to the valuation flows, reset flows will be generated for the day following the valuation key date (usually reset flows will be posted at the first date of next month). You can therefore see the effects of the valuation only on the valuation key date.Sub-area Posting Control:Test Run: <select this checkbox>Choose Run. | The Display Positions to be Valued screen displays. |  |
|  | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation.If the Message dialog shows up, choose Continue. | The Valuation Log screen displays. If red traffic light exists, click on it and check the error message, solve the issue and perform test run again until there is no error.You can check the simulated Posting Log for IFRS (valuation area 002) by choosing Logs + Messages. The offsetting account for fair value change of FX transaction is a Technical Clearing Account. |  |
|  | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Run:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation screen displays. |  |
|  | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation screen, choose Run Valuation. | The Valuation Log screen displays, you can check the Posting Log for IFRS (valuation area 002) by choosing Logs + Messages, this time, accounting documents have been created for IFRS (valuation area 002). |  |

(Optional) Reverse Valuation:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Valuation (TPM2). | The Reverse Valuation (TPM2)screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Reverse Valuation (TPM2) screen, enter the following data:Sub-area Product Groups:OTC Transactions: <select this checkbox>Sub-area General Selections:Company code: for example, 3310Valuation Area: for example, 002Sub-area OTC Transactions:Transaction: <the FX transaction number(s)>Sub-area Valuation Parameters:Key Date for Valuation: for example, <last date of current month, same as the date you ran valuation>Sub-area Posting Control:Reason for Reversal: for example, 04Test Run: <select this checkbox>Update Derived Bus. Trans: Use System SettingsChoose Run. | The Display Positions to Be Reversed screen displays. |  |
| 4 | Execute Reversal for Test Run | On the Display Positions to Be Reversed screen, choose Reverse Valuation (TPM2). | If dialog Information Overview shows up, choose Reversal Log.The screen Reversal Log: Reversed Business Transactions displays, you can check the simulated reversal valuation postings for IFRS (valuation area 002). |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Run:Test Run: <deselect this checkbox> | The Display Positions to Be Reversed screen displays. |  |
| 6 | Execute Reversal for Production Run | On the Display Positions to Be Reversed screen, choose Reverse Valuation (TPM2). | If dialog Information Overview shows up, choose Reversal Log.The screen Reversal Log: Reversed Business Transactions displays, you can check the reversal valuation postings for IFRS (valuation area 002), accounting document has been created. |  |
| 7 | Run Valuation Again | Open app Run Valuation (TPM1), and create the postings for valuation again (follow introductions in Run Valuation), otherwise you will not be able to continue the testing. | Valuation is executed again. |  |

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

Valuation for FX transactions (hedging instruments) has been executed at period end.

Procedure

Run Classification:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Run Classification (TPM101). | The Execute Classification screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Execute Classification screen, enter the following data and choose Run:Company Code: for example, 3310Valuation Area: for example, 002Key Date for Classification: for example, <the last date of current month>Transaction Selection: <select this radio button>Transaction Number: <the FX transaction number(s)>Test Run: <select this checkbox> | The Information Overview dialog box displays. |  |
| 4 | Check Classification Log | In the Information Overview dialog box, choose Hedge Management. | The Information Overview screen is displayed. You can check the Classification Log on this screen. |  |
| 5 | Check Posting Log | Choose Back.In the Information Overview dialog box, choose Posting Log. | The Posting Log: Posted Business Transactions screen is displayed.You can check the simulated Classification postings for IFRS (valuation area 002) on this screen, the offsetting account for OCI I, OCI II, P/L Ineffective is also the Technical Clearing Account. |  |
| 6 | Execute Valuation for Production Run | Choose Back, and choose Close in the dialog box Information Overview.On the initial screen of app Run Classification (TPM101), change the following data and choose Run:Test Run: <deselect this checkbox> | The Information Overview screen displays again.The Classification postings have been created for IFRS (valuation area 002), you can chick Posting Log to check the postings. |  |

(Optional) Reverse Classification:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Reverse Classification (TPM102). | The Reverse Classification (TPM102) screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Reverse Classification (TPM102) screen, enter the following data and choose Run:Company Code: for example, 3310Valuation Area: for example, 002Key Date for Classification: for example, <last date of current month>Transaction Selection: <select this radio button>Transaction Number: <the FX transaction number(s)>Reason for Reversal: for example, 04Test Run: <select this checkbox> | Dialog box Information Overview displays. |  |
| 4 | Check Reversal Log | In the Information Overview dialog box, choose Reversal Log. | The screen Reversal Log: Reversed Business Transactions displays, you can check the simulated reversal postings of classification for IFRS (valuation area 002). |  |
| 5 | Execute Reversal for Production Run | Choose Back, and choose Close in the Information Overviewdialog box.On the initial screen of app Reverse Classification (TPM102), change the following data and choose Run:Test Run: <deselect this checkbox> | The Information Overview screen displays again.The reversal postings of classification have been created for IFRS (valuation area 002), you can chick Reversal Log to check the postings. |  |
| 6 | Run Classification Again | Open app Run Classification (TPM101), and create the postings for Classification again (follow introductions in Run Classification), otherwise you will not be able to continue the testing. | Classification is executed again. |  |

#### Process Reclassification for Hedging Business Transaction at Balance Sheet Recognition Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the Balance Sheet Recognition date, you run the app Release Hedging Business Transactions (TPM120), the following activities are done by this app:

- Calculation and saving of NPV of FX Transaction
- Calculation and saving of NPV component values for FX Transaction and Hypothetical Derivative
- Posting of key date valuation of the designated portion of the FX Transaction with actual NPV values
- Posting of classification of the selected Hedging Relationship with actual NPV component values
- Update amounts of Reclassification Update Types
- Fix scheduled Reclassification Updated Types

Three options are provided for the reclassification of Balance Sheet Crossover, they are maintained in field Balance Sheet Recognition in sub-area Designation Splitting on tab Hedge Accounting I of the Hedging Area:

- 1 - Immediate Reclassification at Balance Sheet Recognition Date
- 2 - Reclassification at the End Date of the Exposure Subitem: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until end date of the Exposure Subitem.
- 3 - Reclassification at Deviant Reclassification Date: the classification result between Designation Date and Balance Sheet Recognition Date is frozen until the Deviant Reclassification Date = Due Date of Hedging Instrument + DIO (Days Inventory Outstanding) - Payment Term.

|  |
| --- |
| Note This step is only necessary when you do Balance Sheet Crossover, that means, you gave value 1, 2 or 3 for the field Balance Sheet Recognition in sub-area Designation Splitting on tab Hedge Accounting I of the Hedging Area, and you can see the Bal.Sheet Rec.Date on tab Hedging Relationship Detail of the Hedging Relationship as described in step [Automatic Designation (Planned)](#unique_18) [page ] 31. |

Prerequisite

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see section [Business Conditions](#unique_6) [page ] 5. And market date should be valid at the Balance Sheet Recognition Date.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions (TPM120) screen displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions (TPM120) screen, enter the following data:Company Code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, Balance Sheet Recognition Date you noted down in step Automatic Designation (Planned)Transaction Selection: <select this radio button>Transaction Number:the FX transaction number(s)Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions (TPM120) screen, choose Run. | The Hedging Relationships screen displays, and Hedging Relationship has been processed for balance sheet crossover without errors. |  |
| 5 | Display Log of Hedge Management | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Log.In the Information Overview dialog box, choose Hedge Management. | The Information Overview screen displays, you can check the Classification Log on this screen. |  |
| 6 | Display Log of Posting | Choose Back.In the Information Overview dialog box, choose Posting Log. | The Posting Log: Posted Business Transactions screen displays, you can check the following postings on this screen:ValuationClassificationReclassification (depend on the setting of field Balance Sheet Recognition on tab Hedge Accounting I of the Hedging Area and when you run Release Hedging Business Transactions (TPM120)) |  |

#### Contract Maturity

##### (1X1) Foreign Currency Risk Management and (1X9) Foreign Currency Risk Management – Group Ledger IFRS

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the FX transaction is mature, the relevant posting and payment process steps for closing FX transaction (which is a Hedging Instrument in Hedging Relationship) should be same as a normal FX transaction (which is not in a Hedging Relationship), relevant process steps are described in test scripts Foreign Currency Risk Management(1X1) and Foreign Currency Risk Management – Group Ledger IFRS(1X9).

Procedure

Perform the following steps in section Foreign Currency Risk Management and Accounting - Without Options of test script Foreign Currency Risk Management(1X1) for the FX transactions you created in step Create Foreign Exchange Contract with Hedging Classification:

| Step Name in 1X1 | Mandatory/Optional for Continuing Testing 1XD | Purpose |
| --- | --- | --- |
| Transaction is Mature -> For NDF -> Fix Rate for NDF | Mandatory (only for NDF) | Fix the rate for a NDF transaction at the Fixing Date you specified when created NDF transaction in step Create Non-Deliverable Forward (NDF) Transaction. |
| Transaction is Mature -> Correspondence -> Set Settlement Status (Manual) | Mandatory (only for NDF) | Set the status of NDF transaction to Fixing Settlement manually after getting incoming confirmation form counterparty.. |
| Generate Payment Request for Mature Transaction | Mandatory | Generate payment request for outgoing payment of FX transaction at its Value Date via app Fix, Pay and Post Flows (TBB1). |
| Process Payment Request | Optional | Process the payment run procedure for payment request and create posting for outgoing payment via app Automatic Payment Transactions for Payment Requests (F111). |
| Post to General Ledger | Mandatory | Post the relevant flows (incoming or outgoing payment) at value date of FX transaction in valuation area AE0 (local GAAP) via app Fix, Pay and Post Flows (TBB1) and Process Business Transactions (TPM10). |
| Post Realized Profit and Loss | Mandatory | Post realized profit or loss at value date of FX transaction in valuation area AE0 (local GAAP) via app Post Derived Business Transactions (TPM18). |

Perform the following step in test script Foreign Currency Risk Management – Group Ledger IFRS(1X9) for the FX transactions you created in step Create Foreign Exchange Contract with Hedging Classification:

| Step Name in 1X9 | Mandatory/Optional for Continuing Testing 1XD | Purpose |
| --- | --- | --- |
| Post Flows to General Ledger (Parallel Valuation Area) | Mandatory | Post the relevant flows (incoming or outgoing payment) at value date of FX transaction in valuation area 002 (IFRS) via app Process Business Transactions (TPM10). |

##### Process Dedesignation for Hedging Business Transaction at Maturity Date for Hedging Instrument

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the maturity date (value date) of FX forward transaction, you run the app Release Hedging Business Transactions (TPM120), the following activities are done by this app:

- Calculation and saving of NPV of FX Transaction
- Calculation and saving of NPV component values for FX Transaction and Hypothetical Derivative
- Posting of key date valuation of the designated portion of the FX Transaction with actual NPV values
- Posting of classification of the selected Hedging Relationship with actual NPV component values
- Transfer Position Amounts from Designated to Free Standing Subposition
- Update amounts of Reclassification Update Types
- Fix scheduled Dedesignation Updated Types

Prerequisite

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see section Business Conditions. And market date should be valid at the maturity date of FX transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions (TPM120) screen displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions (TPM120) screen, enter the following data:Company Code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, the maturity date of FX transaction(s)Transaction Selection: <select this radio button>Transaction Number:the FX transaction number(s)Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions (TPM120) displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions (TPM120) screen, choose Run. | The Hedging Relationships screen displays, and Hedging Relationship has been processed for balance sheet crossover without errors. |  |
| 5 | Display Log of Hedge Management | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Log.In the Information Overview dialog box, choose Hedge Management. | The Information Overview screen displays, you can check the Classification Log on this screen. |  |
| 6 | Display Log of Posting | Choose Back.In the Information Overview dialog box, choose Posting Log. | The Posting Log: Posted Business Transactions screen displays, you can check the postings on this screen. |  |

Use app Post Derived Business Transactions (TPM18) to fix the derived business transactions for FX transaction at contract close date:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Fix and Post Derived Business Transactions screen, enter the following data:Sub-area Product Groups:OTC Transactions: <select this checkbox>Sub-area General Selections:Company code: for example, 3310Valuation Area: for example, 002Sub-area Selections for Fixing Derived Business Transactions:TRL Date: <the maturity date of FX transaction(s)>Sub-area Posting Control:Test Run:<select this checkbox>Choose Run.If message No scheduled derived business transactions were found for the selection displays, then there is no derived transaction available for your selection, you can skip current step.If message Are you sure that you want to select future business transactions? displays, press Enter | The FX Transaction(s) to be fixed and posted (test run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 4 | Fix and Post for Test run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the simulated postings. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the initial screen of this app.Change the following data and choose Run:Test Run: <deselect this checkbox>If message Are you sure that you want to select future business transactions? displays, press Enter | The FX Transaction(s) to be fixed and posted (production run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 6 | Fix and Post for Production run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the postings for IFRS (valuation area 002), accounting document has been created in corresponding ledger in Financial Accounting. |  |

#### Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Reclassification of the Hedging Reserve and Cost of Hedging Reserve position amounts is executed at the end date of the Exposure Subitem within the Derived Business Transaction Framework: the app Post Derived Business Transactions (TPM18) for the fixation and posting of Derived Business Transactions selects the Exposure Subitem position flows to be reclassified.

Postings are created for reclassification of Hedging Reserve and Cost of Hedging Reserve position amounts; P/L ineffective position amounts are fixed only.

|  |
| --- |
| Note This step creates postings only when the relevant Split ID on tab Hedge Accounting I of the Hedging Area uses the following parameters for the field Balance Sheet Recognition:• 0 or Blank - None: the accumulated Hedging Reserve and Cost of Hedging Reserve between Designation Date and Dedesignation Date are reclassified at the end date of Exposure Subitem.• 2 - Reclassification at the End Date of the Exposure Subitem: the accumulated Hedging Reserve and Cost of Hedging Reserve between Designation Date and Balance Sheet Recognition Date are reclassified at the end date of Exposure Subitem.If 1 - Immediate Reclassification at Balance Sheet Recognition Date is given for field Balance Sheet Recognition, reclassification has been done at the Balance Sheet Recognition Date by using app Release Hedging Business Transactions.If 3 - Reclassification at Deviant Reclassification Date is given for field Balance Sheet Recognition, reclassification should be done at the Deviant Reclassification Date by using app Release Hedging Business Transactions. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Fix and Post Derived Business Transactions screen, enter the following data:Sub-area Product Groups:OTC Transactions: <deselect this checkbox>Exposure Items: <select this checkbox>Sub-area General Selections:Company code: for example, 3310Valuation Area: for example, 002Sub-area Selections for Fixing Derived Business Transactions:TRL Date: <the end date of hedged item which you noted down in step Automatic Designation (Planned)>Sub-area Exposure Items:Transaction Number: <the FX transaction number(s)>Sub-area Posting Control:Test Run: <select this checkbox>Choose Execute.If message Are you sure that you want to select future business transactions? displays, press Enter | The Exposure Subitem(s) to be fixed and posted (test run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 4 | Fix and Post for Test run | Choose Fix. | If the Information Overview dialog box displays, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the simulated reclassification postings of Hedging Reserve and Cost of Hedging Reserve for IFRS (valuation area 002). |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the initial screen of this app.Change the following data and choose Execute:Test Run: <deselect this checkbox>If message Are you sure that you want to select future business transactions? displays, press Enter | The Exposure Subitem(s) to be fixed and posted (production run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 6 | Fix and Post for Production run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the postings for IFRS (valuation area 002), accounting document has been created in corresponding ledger in Financial Accounting. |  |

#### Reporting

##### Display Treasury Position Flows

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the position flows of FX transactions and exposure subitems.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows (F1754) screen displays. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Position Flows (F1754) screen, enter the following data and choose Go:Product Group: <select OTC Transactions and Exposure Items>Company code: for example, 3310Valuation Area: for example, 002For displaying position flows on OTC transaction level, enter:Transaction: <The FX transaction number(s)>For displaying position flows on Exposure Subitem level, enter:Exposure Item ID: <The Exposure Item ID you noted down in step Automatic Designation (Planned)>Exposure Subitem ID: <The Exposure Subitem ID you noted down in step Automatic Designation (Planned)>Note If the selection criteria Transaction, Exposure Item ID, Exposure Subitem ID do not exist on the screen, choose Adapt Filters, and then choose the fields Exposure Item ID, Exposure Subitem ID from the sub-area Exposure Items, and choose Transaction from the sub-area OTC Transactions in the Adapt Filters dialog box. | All relevant position flows of FX transaction and Exposure Subitems are displayed in area Position Flows.If you would like to see transaction ID, exposure item ID, exposure subitem ID in area Position Flows, please choose Settings to change the layout. |  |

##### Display Treasury Posting Journal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the posting journals of FX transactions and exposure subitems.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal (F1755) screen displays. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Posting Journal (F1755) screen, enter the following data and choose Go:Product Group: <select OTC Transactions and Exposure Items>Company code: for example, 3310Valuation Area: for example, 002For displaying posting journal on OTC transaction level, enter:Transaction: <The FX transaction number(s)>Or for displaying posting journal on Exposure Subitem level, enter:Exposure Item ID: <The Exposure Item ID you noted down in step Automatic Designation (Planned)>Exposure Subitem ID: <The Exposure Subitem ID you noted down in step Automatic Designation (Planned)>If the selection criteria Transaction, Exposure Item ID, Exposure Subitem ID do not exist on the screen, choose Adapt Filters, and then choose the fields Exposure Item ID, Exposure Subitem ID from the sub-area Exposure Items, and choose Transaction from the sub-area OTC Transactions in the Adapt Filters dialog box. | All relevant posting journal line items are displayed in area Line Items, you can see the line items on FX transaction level or Exposure subitem level.If you would like to see transaction ID, exposure item ID, exposure subitem ID in area Position Flows, please choose Settings to change the layout. |  |

##### Display Treasury Position Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

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

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

You may first have completed the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| (1X1) Foreign Currency Risk Management | As a prerequisite for running current test script, an appropriate business partner (counterparty) must exist, please follow preliminary step Create Business Partner in test script Foreign Currency Risk Management (1X1) to create a business partner.Optional: as a prerequisite for running current test script when using Designation Type which requires counterconfirmation, correspondence process should be proceeded, therefore correspondence setting should be maintained for business partner in advance, please see preliminary step Maintain Profile and BP Group Assignments to External Recipient in test script Foreign Currency Risk Management(1X1) for correspondence setting. This is optional.Optional: please follow preliminary step Maintaining Credit Limit in test script Foreign Currency Risk Management(1X1) to maintain credit limits. This is optional. |
| (1XN) Market Rates Management – Manually via Upload | As perquisites for running current test script, execute the following steps in test script Market Rates Management – Manually via Upload (1XN) to maintain the necessary market data manually for hedge accounting:Enter FX Spot RatesEnter Interest RatesCreate Reference Entities for Business PartnersAssign Attributes to Evaluation TypeMaintain Reference EntitiesEnter Credit SpreadsEnter Basis Spreads |

### Overhedge Processing - Dedesignation

Purpose

With the reduction of a planned cash flow of an exposure period an overhedge situation occurs (e.g. partial volume of the hedged item that is a forecast transaction is no longer highly probable). A Hedge Request type Dedesignation allows to dedesignate the Hedging Relationship to solve the overhedge situation.

Depending on the selected type of Reclassification Handling, the reclassification of the Hedging Reserve and Cost of Hedging Reserve amounts is posted immediately with the release of the Hedging Business Transaction or at the Exposure Item End Date.

Prerequisites

The following steps under section [FX Forwards as Hedging Instruments](#unique_33) [page ] 10 have been executed:

- Define or Adjust Hedging Area
- Create Raw Exposure
- Take Snapshot (TOESNAP)
- Create Foreign Exchange Contract with Hedging Classification - Create Deliverable Forward Transaction

Note down the FX Forward Transaction Number, and the Value Date of this FX Forward Transaction.

- Automatic Designation (Planned)

Note down the Hedging Relationship Number (HR Number).

- Set Contract Settlement Status with Incoming Confirmation
- Release Hedging Relationship

After the steps above are done, there is already a released hedging relationship.

The follow-on steps introduce how to simulate a overhedge situation for this released hedging relationship and how to dedesignate the overhedged portion in system.

#### Create Raw Exposure

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A new Raw Exposure is created as an exposure position to simulate an overhedge situation in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Raw Exposure (FTREX1). | The Raw Exposure: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | On the Raw Exposure: Initial Screen, enter the following data and choose Create.Exposure Activity Type: for example, YFXI | The Raw Exposure Maintenance: Create screen displays. |  |
| 4 | Enter Header Data | On the Raw Exposure Maintenance: Create screen and tab Header Data, enter the following data:Default Exposure Category: for example, 01(Forecasted Transaction)Company Code: for example, 3310Cirt4ExpPosType: FX (FX Exposure)Direction: for example, IN(Incoming Cash Flow) | Necessary header data is entered. |  |
| 5 | Enter Line Item Data | Choose tab Line Item Data.In sub-area Raw Exposure Line Item, choose Create New Line Item, and enter the following data:Due Date: for example, Current date + 2 MonthsExposure Amount: for example, -300000Exposure Amount Currency: for example, USDTarget Currency: for example, AED | Necessary line item data is entered. |  |
| 6 | Save Raw Exposure | Choose Save. | A dialog box displays, and states that:Raw exposure has been saved;Raw exposure has been released;Position IDs have been updated.You can check Exposure Position and Exposure Position Flows via app Process Exposure Positions (FTREX12) and Display Exposure Position Flows (FTREX13).In the example, after the raw exposure is created, the incoming exposure in a specific period will be 300000 less than the initial estimated exposure data. |  |

#### Take Snapshot

Purpose

Take a new snapshot to reflect reduction of exposure for overhedge situation.

Procedure

Execute step [Take Snapshot](#unique_11) [page ] 24 under section [FX Forwards as Hedging Instruments](#unique_33) [page ] 10.

#### Create and Submit Dedesignation Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Create a dedesignation request in Hedge Management Cockpit (TOENE) and submit it.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Hedge Management Cockpit (TOENE). | The Hedge Management Cockpit for Hedging Area screen displays. |  |
| 3. | Enter Selection Criteria | On the Hedge Management Cockpit for Hedging Area screen, enter the following data and choose Start:Hedging Area: for example, HA0001Layout ID: for example, 1R_ALL_CH | The Hedge Management Cockpit for Hedging Area HA0001 displays.You can see the amount of exposure have been reduced in the cell for relevant period (for example, current month + two months) and risk currency (for example, USD) in accordance to the new raw exposure you just created. |  |
| 4. | Create Dedesignation Request | Choose a cell for relevant period and risk currency in accordance to the new raw exposure you just created.Choose Hedge Request > Dedesignation Request. | The Hedge Request screen displays. |  |
| 5. | Enter and Check Date for Dedesignation Request | On the Hedge Request screen, enter the following data:Header:Description (the field beside field Hedge Request ID): <any text>Tab General:Hedge Req. Reason: S001Dedes.Date: <the date in the period you reduce the exposure, which must be earlier than the value date of the FX Forward Transaction you created in the Prerequisites section of Overhedge Processing - Dedesignation, for example, <Current date + 1 Months>Hedge Request Volume: <the reduced exposure amount>, for example, 300000Tab Hedging Relationships:Valuation Area: 002Reclass. Handling: for example, Immediate ReclassificationSelect the checkbox Requested for the row with the Transaction Number and HR Number you noted down when executing the steps mentioned in the Prerequisites section of [Overhedge Processing - Dedesignation](#unique_36) [page ] 61.Request Volume (of the row you selected): <the reduced exposure amount>, for example, 300000Sequence: for example, 1Choose Check.Note Two options of Reclass. Handling:Immediate Reclassification: the OCI I, OCI II of dedesignated portion is reclassified immediately with release of the Hedging Business Transaction.Planned Reclassification: the OCI I, OCI II of dedesignated portion will be reclassified at the end date of exposure subitem. | Message Hedge Request is consistent displays, means the data you entered is OK, otherwise please check your data until this message displays. |  |
| 6. | Submit Dedesignation Request | Choose Submit. | Message Hedge Request number was saved displays.Note down the Hedge Request ID. |  |

#### Release Dedesignation Request

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the dedesignation request.

With the release of the dedesignation request, position flows with update types THX003 or THX004 are automatically created for relevant Hedging Relationships in status Scheduled.

Additional position flows are created to transfer position values of Hedging Reserve, Cost of Hedging Reserve and P/L portions from the designated subposition to the free standing subposition of the Exposure Subitems.

If you chose Immediate Reclassificatin in the dedesignation request, the position flows for reclassifying Hedging Reserve, Cost of Hedging Reserve of the dedesignated portion are created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO). | The Process Hedge Requests (TOEHREQO) screen displays. |  |
| 3. | Enter Selection Criteria and Start Search | On the Process Hedge Requests (TOEHREQO) screen, enter the following data:Hedging Area: for example, HA0001Submitted (in subarea Status):<make sure this checkbox has been selected>Choose Start. | A list of hedge requests displays, your dedesignation request is in this list, its status is Submitted. |  |
| 4. | Release Dedesignation Request | Choose the Hedge Request ID of the dedesignation request you created, and choose Process > Release.If dialog box appears and states that Data was Changed. Do you want to Save?, choose Yes. | The dedesignation request's status becomes Released. |  |

A Released dedesignation request can be withdrawn. To withdraw a dedesignation request, please execute the following steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO). | The Process Hedge Requests (TOEHREQO) screen displays. |  |
| 3 | Enter Selection Criteria and Start Search | On the Process Hedge Requests (TOEHREQO) screen, enter the following data:Hedging Area: for example, HA0001Released (in subarea Status): <make sure this checkbox has been selected>Choose Start. | A list of hedge requests displays, your dedesignation request is in this list, its status is Released. |  |
| 4 | Withdraw Dedesignation Request | Choose the Hedge Request ID of the dedesignation request you released, and choose Process > Withdraw. | Dialog box displays and states that Hedge Request withdrawn. |  |

|  |
| --- |
| Note A withdrawn dedesignation request cannot be released again, please recreate and resubmit a new designation to continue testing.If the dedesignation business transaction has been released (means next step Process Dedesignation for Hedging Business Transaction has been executed), the dedesignation request cannot be withdrawn unless you reverse the release of the dedesignation business transaction via app Reverse Release of Hedging Business Transactions (TPM121). |

#### Process Dedesignation for Hedging Business Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purppose

In this step, you release the hedging business transaction at dedesignation date.

The following activities are done with the release of hedging business transaction at the dedesignation date:

- Calculation and saving of NPV of FX forward transaction
- Calculation and saving of NPV component values (spot, forward, CCBS, others) for FX forward transaction and hypothetical derivative
- Execution and posting of the key date valuation of the FX forward transaction to be dedesignated with actual NPV values
- Execution and posting of the classification of the selected Hedging Relationship with actual NPV component values
- Update amounts of flows of dedesignation update types
- Fix update types of planned dedesignation flows
- Fix and post update types of reclassification flows (if chose 'Immediate Reclassification' in hedge request)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2. | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions (TPM120) screen displays. |  |
| 3. | Release Hedging Business Transaction | On the Release Hedging Business Transactions (TPM120) screen, enter the following data:Company code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, <the dedesignation date you specified in the Dedesignation Request>Transaction Selection: <select this radio button>Transaction Number:<the FX Forward transaction number>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions (TPM120) screen, choose Run. | The Hedging Relationships screen displays, and Hedging Relationship has been processed for balance sheet crossover without errors. |  |
| 5 | Check Market Data Calculation Details | Choose Display Market Value Calculation Details. | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays. You can see the details of the calculation of the full NPV as well as the Hedge Accounting Key Figures.Go back to the Hedging Relationships screen. |  |
| 6 | Check Log and Message | On the Hedging Relationships screen, select the checkbox of a HR Number, and select Display Log. | Dialog box Information Overview displays, you can check:Hedge management logPosting logMessagesGo back to the Hedging Relationships screen. |  |

|  |
| --- |
| Note If you check the relevant hedging relationship in app Manage Hedging Relationships (TPM100) and change the display date to the dedesigantion date, you will find the designated amount of Hedged Item and Hedging Instrument has been reduced. |

### Effectiveness Test

Purpose

When effectiveness test is enabled in hedge accounting process, some process steps will be different from Test Procedure because Test Procedure describes the hedge accounting process without effectiveness test .

This section describes what are the differences if effectiveness test is enabled.

#### Create Market Data Set

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The market data set is an entity referring to a set of different market data, each market data contributing to one data point for the linear regression used in effectiveness test.

Two market data set categories are available:

- From Market Data Scenarios: the market data set refers to list of market data scenarios which can be individually defined and thus may contain any artificial market data constellation.
- From Market Data Tables: the market data set refers to a list of historical market data selection dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Market Data Sets (TAN_MDS). | The Market Data Set Administration: Initial Screen displays. |  |
| 3 | Enter Basic Date for Market Date Set | On the Market Data Set Administration: Intimal Screen, enter the following data:Market Data Set ID: for example, ET01Choose Create.In the Create New MDS with First Version dialog box, enter the following data:MDS Category: for example, from Market Data TablesTotal Number of Data: for example, 3Valid From: for example, January 1st of last yearchoose Continue: | The Create Market Data Set <MDS ID> Version <Valid From Date> screen displays. |  |
| 4 | Create and Save Market Date Set | On the Create Market Data Set XXXX Version <Valid From Date> screen, enter the following data:Short Name: for example, MDS for ETLong Name: for example, MDS for Effectiveness TestTerm: for example, 1Time Unit: for example, MonthsChoose Save. | Message MDS <MDS ID> successfully saved displays. |  |

#### Adjust Hedging Area

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This section describes that the data in Hedge Accounting II tab of the hedging area should be adjusted for effectiveness test.

Prerequisites

The hedging area already exists.

A market date set has been created.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Define Hedging Area (TOE_HEDGING_AREA). | The Display Hedging Area screen displays. |  |
| 3 | Enter Hedging Area ID | On the Display Hedging Area screen, enter the following data, and choose Display:Hedging Area: for example, HA0001 | Hedging Area HA0001 is displayed. |  |
| 4 | Create New Version | Choose New Version.In the Create New Version of Hedging Area HA0001 dialog box, enter the following data, and choose Create:Valid From: for example, <current date>. If current date cannot be entered, please enter the earliest date system allows. | The Change Hedging Area screen displays. |  |
| 5 | Update Data on Tab Hedge Accounting II | Choose the Hedge Accounting II tab.In sub-area Designation Control, chose a row and change its Hedging Profile and enter a MDS ID. For example, change the row with Hedging Classification YFC00 according to the following data:CoCodeVAHdg Class.Des. TypePType ESIHdgProfileMDS ID1010002YFC00YFX1WS00ET01Note S00 is a SAP pre-delivered Hedging Profile in which effectiveness test is enabled. If you need more Hedging Profiles for FX forwards with effectiveness test , please use configuration step Define Hedging Profiles.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. | Data on tab Hedge Accounting II has been updated. |  |
| 6 | Save the Hedging Area | Choose Save (Ctrl+S). | Message Hedging area HA0001 version XXX saved displayed.The Hedging Area for Hedge Accounting has been extended for effectiveness test. | 9 |

#### Create Foreign Exchange Contract with Hedging Classification

Procedure

Please follow the step [Create Foreign Exchange Contract with Hedging Classification](#unique_15) [page ] 27 in Test Procedure to create a Foreign Exchange Contract (hedging instrument) and pay attention to fields:

- Contract Date: must enter a date which is equal to or later than the Valid From date of the new version of Hedging Area.
- Hdg Classific.(Hedging Classification): must enter a hedging classification which is assigned with an effectiveness test-enabled Hedging Profile and a MDS ID in Hedge Accounting II tab of hedging area, that is YFC00 in this example.

#### Automatic Designation (Planned)

After saving the Foreign Exchange Contract, a Hedging Relationship will be automatically created with status ‘Planned Designation’ just like description in step [Automatic Designation (Planned)](#unique_18) [page ] 31 of Test Procedure.

The only difference is Effectiveness Test tab on which you can see information about effectiveness test for this hedging relationship. The Test Plan sub-tab contains the market data set derived from the hedging area settings, the first record is the basis for the prospective effectiveness test (PET) performed at designation.

#### Release Hedging Relationship with Prospective Effectiveness Test

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the automated designation which is in status Planned Designation. The prospective effectiveness test is also executed during release.

Prerequisites

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system and should be valid at the designation date and the dates derived from market data set.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions screen, enter the following data and choose Run:Company code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, <contract date of FX transaction>Transaction Selection: <select this radio button>Transaction Number: the FX transaction number(s)Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Post Date: <select this checkbox>Test Run: <deselect this checkbox> | A new screen Release Hedging Business Transactions displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions screen, choose Run. | The Hedging Relationships screen displays.A list shows the processed hedging relationship(s) along with processing status indicated by a green or red status icon.The prospective effectiveness test may lead to some errors which stop releasing of hedging relationship:The effectiveness test has been executed, but it turned out that the hedging relationship is ineffective. In that case you can choose Display Log to check the message, and choose Display Effectiveness Test to check details.Effectiveness could not be completely executed, e.g. due to missing historical market data for some of the market data selection dates derived from the market data set. In that case please choose Market Value Calculation Details to check the Error Log. |  |

### Termination of Hedging Instrument

Purpose

The termination of hedging instrument (FX forward or NDF) leads to the discontinuation of hedge accounting.

This section describes how to terminate hedging instrument and discontinue hedge accounting.

#### Create, Submit and Release Termination Request for Hedging Instrument

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In some cases, for example, when a long FX forward transaction (or FX spot, FX Swap, NDF) is over-hedged, you may need to terminate the transaction after aligning with your counterparty.

After aligning with your counterpart, you decide to terminate the hedging instrument. You start the termination process via termination request in hedge management cockpit. In this step, you select the hedging instrument in the hedge management cockpit to create and submit a termination request. The request needs to be released after it is submitted.

Prerequisites

1. You have created an FX forward transaction (or FX spot, FX Swap, NDF) as hedging instrument, and its status is set to Contract Settlement.
2. You have created a hedging relationship and released the designation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Hedge Management Cockpit (TOENE) |  |  |
| 3 | Enter Selection Criteria | Make the following entries, and choose Start:Hedging Area: For example, HA0001Layout ID: 2R_TQ_CH | The Hedge Management Cockpit for Hedging Area HA0001 is displayed with Net Hedges |  |
| 4 | Create Termination Request | Double click on key figure Net Hedges in the period of the value date of the forward transaction you just created as prerequisite.Select the transaction you just created, click Hedge Request and choose Termination Request in the dropdown list | The Create Hedge Request screen is displayed. |  |
| 5 | Submit Termination Request | Enter description for edge request: terminate forwardEnter the following data on the General tab, and choose Submit:Hedge Request Reason: Choose S003 Overhedge Processing - TerminationNote Overruling not allowed | Terminate Request is submitted with termination request ID.Remember Note down the ID. |  |
| 6 | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start:Hedging Area: for example, HA0001 | Hedge requests that match the filter criteria are displayed. |  |
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

In this step, you terminate an FX forward transaction as a hedging instrument in the system, after the termination request released. Once the hedging instrument is terminated, the termination request is set to Completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06) | The Forex: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data and choose Run:Company Code: for example, 3310Transaction: <the FX transaction number to be terminated> | A list of FX transactions is displayed in the Forex: Collective Processing - Results area. |  |
| 4 | Terminate the Transaction | Select the checkbox of the transaction to be terminated in the Forex: Collective Processing - Results area, and choose Terminate. | The Terminate Forex Transaction: Structure screen is displayed. |  |
| 5 | Save the Termination | On the Terminate Forex Transaction: Structure screen, the value of field Activity in header is 3 - Termination.Enter the following data in the Termination area, and choose Save:Date: <the termination data, it should be a date between contract date and value date>Payment Date: for example, <termination data + 2 days>Entry Type: for example, RateRate: for example, 1.16If the Document lines: Display message dialog box is displayed, choose Continue. | The payment amount for termination is calculated and the transaction is saved with status Termination. |  |
| 6 | Access the SAP Fiori App | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start.:Hedging Area: for example, HA0001 | hedge requests that match the filter criteria are displayed. |  |
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

After terminating an FX forward transaction in the system, you need to set the status of transaction to Termination Settlement before you can create postings for termination flow. Usually it is done after you receive the incoming confirmation about termination from counterparty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. |  |  |
| 2 | Access the SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06) | The Forex: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data, and choose Run:Company Code: for example, 3310Transaction: <the FX transaction number in status Termination> | A list of FX transactions is displayed in the Forex: Collective Processing - Results area. |  |
| 4 | Settle the Termination | Select the checkbox of the transaction to be settled in the Forex: Collective Processing - Results area, and choose Settle. | The Settle Forex Transaction: Structure screen is displayed. |  |
| 5 | Save the Termination Settlement | On the Settle Forex Transaction: Structure screen, the value of the Activity field in header is 4 - Termination Settlement.Choose Save.If the Document lines: Display messages dialogue box is displayed, choose Continue (Enter). | The transaction is saved with status Termination Settlement. |  |

#### Process Dedesignation for Hedging Business Transaction at Termination Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the hedging business transaction on the termination date. During this process, the hedging relationship is dedesignated, and the following activities are done:

- Calculation and saving of NPV of FX forward transaction;
- Calculation and saving of NPV component values (spot, forward, CCBS, others) for FX forward transaction and hypothetical derivative;
- Execution and posting of the key date valuation of the FX forward transaction to be terminated with up-to-date NPV values;
- Execution and posting of the classification of the Hedging Relationship with up-to-date NPV component values;
- Fix and update other relevant position flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions screen is displayed. |  |
| 3 | Release Hedging Business Transaction | On the Release Hedging Business Transactions screen, enter the following data:Company Code: for example, 3310Valuation Area: for example, 002Up to Key Date: for example, <the termination date>Transaction Selection: <select this radio button>Transaction Number: <the FX Forward transaction number terminated>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new Release Hedging Business Transactions screen is displayed. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions screen, choose Run. | The Hedging Relationships screen is displayed, and Hedging Relationship has been processed for termination of hedging instrument without errors. |  |

|  |
| --- |
| Note If you check the relevant hedging relationship in the Manage Hedging Relationships (TPM100) app and change the display date to the termination date, you will find the status of this hedging relationship becomes Dedesignated |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Fix, Pay and Post Flows (TBB1). | The Treasury: Post Flows screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Post Flows screen, enter the following data, and choose Run:Company Code: for example, 3310Transaction: <the FX transaction number terminated>Up to and Including Due Date: <the payment date of termination>Test Run: for example, <deselect this checkbox>Post All Valuation Areas: for example, <select this radio button> | The Information Overview dialog box is displayed. |  |
| 4 | Check Posting Log | In the Information Overview dialog box, choose Posting Log. | Posting journals are displayed. |  |

|  |
| --- |
| NoteIf termination results in outgoing payment with a payment request, please refer to the Foreign Currency Risk Management (1X1) test script for automatic payment of payment requests.Reclassification of Hedging Reserve and Cost of Hedging Reserve should be executed on the Exposure Subitem End Date, which is the same as the normal hedge accounting process without termination of hedging instrument. |

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

For Hedge Accounting for FX Forward, the following Simulated Valuation processes are supported:

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
| 3 | Enter Selection Criteria for Test Run | On the Simulate Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, 002Product Type: for example, 60ATransaction Number: for example, < Transaction Number created in previous steps>Recalculate Outdated Sim.Val.: <deselect this checkbox>Note If you set this indicator, you can recalculate the outdated simulation resultsSimulation Date: for example, <the current date>Key Date Valuation : <select this checkbox>Accrual/Deferral: <deselect this checkbox>Classification : <select this checkbox>Test Run: <select this checkbox> | The Messages dialog box is displayed and the following message is displayed:Processed xx positions; xx successful, 0 failedIf Recalculate Outdated Simulation Results has been executed, the following message is displayed:xx simulated results deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
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
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XD_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 158,235 chars in the whole document
