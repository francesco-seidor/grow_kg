---
id: 05-treasury-and-cash-management/hedge-accounting-for-fx-forward-group-ledger-us-gaap-3x3-ae-986
title: Hedge Accounting for FX Forward – Group Ledger US GAAP (3X3_AE) (3X3_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3X3_AE: US GAAP cash flow hedge accounting with FX forwards/NDFs, from hedging area to reclassification."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/hedge-accounting-fx]
aliases: [3X3_S4CLD2608_BPD_EN_AE]
keywords: [Hedge Accounting for FX Exposures, hedge accounting, hedging area, raw exposure, hedge management cockpit, fx forward transactions, hedging relationship designation, hedging relationship release, period end closing, key date valuation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3X3_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-986
topic: 05-treasury-and-cash-management/hedge-accounting-fx
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Hedge Accounting for FX Forward – Group Ledger US GAAP (3X3_AE) (3X3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3X3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Hedge Accounting for FX Exposures** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Hedge Accounting for FX Forward – Group Ledger US GAAP (3X3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854104)

[2 Prerequisites 4](#_Toc232854105)

[2.1 System Access 4](#_Toc232854106)

[2.2 Roles 4](#_Toc232854107)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232854108)

[2.4 Business Conditions 5](#_Toc232854109)

[2.5 Premilinary Steps 6](#_Toc232854110)

[2.5.1 Create Market Data Set 6](#_Toc232854111)

[3 Overview Table 8](#_Toc232854112)

[4 Test Procedures 11](#_Toc232854113)

[4.1 FX Forwards as Hedging Instruments 11](#_Toc232854114)

[4.1.1 Define or Adjust Hedging Area 11](#_Toc232854115)

[4.1.2 Collect and Determine Exposure Data 18](#_Toc232854116)

[4.1.3 Create Raw Exposure 18](#_Toc232854117)

[4.1.4 Take Snapshot 20](#_Toc232854118)

[4.1.5 Review Net Open Exposure in Hedge Management Cockpit 21](#_Toc232854119)

[4.1.6 Agree on Hedging Instrument 22](#_Toc232854120)

[4.1.7 Check Limit Utilization Report (Optional) 22](#_Toc232854121)

[4.1.8 Create Foreign Exchange Contract with Hedging Classification 23](#_Toc232854122)

[4.1.8.1 Create Deliverable Forward Transaction 23](#_Toc232854123)

[4.1.8.2 Create Non-Deliverable Forward (NDF) Transaction 25](#_Toc232854124)

[4.1.9 Automatic Designation (Planned) 27](#_Toc232854125)

[4.1.10 Set Contract Settlement Status with Incoming Confirmation 31](#_Toc232854126)

[4.1.11 Release Hedging Relationship 33](#_Toc232854127)

[4.1.12 Fix Derived Business Transaction 36](#_Toc232854128)

[4.1.13 Period End Closing 37](#_Toc232854129)

[4.1.13.1 Calculate NPV of Hedging Instrument and Hypothetical Derivative 37](#_Toc232854130)

[4.1.13.2 Run Key Date Valuation 39](#_Toc232854131)

[4.1.13.3 Run Classification 42](#_Toc232854132)

[4.1.14 Contract Maturity 44](#_Toc232854133)

[4.1.14.1 (1X1) – Foreign Currency Risk Management and (34D) – Foreign Currency Risk Management – Group Ledger US GAAP 44](#_Toc232854134)

[4.1.14.2 Process Dedesignation for Hedging Business Transaction at Maturity Date for Hedging Instrument 46](#_Toc232854135)

[4.1.15 Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date 48](#_Toc232854136)

[4.1.16 Reporting 50](#_Toc232854137)

[4.1.16.1 Display Treasury Position Flows 50](#_Toc232854138)

[4.1.16.2 Display Treasury Posting Journal 51](#_Toc232854139)

[4.1.16.3 Display Treasury Position Values 52](#_Toc232854140)

[5 Appendix 54](#_Toc232854141)

[5.1 Overhedge Processing - Dedesignation 54](#_Toc232854142)

[5.1.1 Create Raw Exposure 54](#_Toc232854143)

[5.1.2 Take Snapshot 56](#_Toc232854144)

[5.1.3 Create and Submit Dedesignation Request 56](#_Toc232854145)

[5.1.4 Process Dedesignation for Hedging Business Transaction 58](#_Toc232854146)

[5.2 Termination of Hedging Instrument 60](#_Toc232854147)

[5.2.1 Create, Submit and Release Termination Request for a Forward 60](#_Toc232854148)

[5.2.2 Terminate Hedging Instrument 61](#_Toc232854149)

[5.2.3 Set Termination Settlement Status for Hedging Instrument 63](#_Toc232854150)

[5.2.4 Process Dedesignation for Hedging Business Transaction at Termination Date 64](#_Toc232854151)

[5.2.5 Post Flows for Termination 65](#_Toc232854152)

[5.3 Simulated Valuation 66](#_Toc232854153)

[5.3.1 Run Simulated Valuation 66](#_Toc232854154)

[5.3.2 Delete Simulated Valuation 68](#_Toc232854155)

## Purpose

Overview

This process helps you to mitigate profit and loss volatility from the use of derivatives.

Currently, the scope item supports US GAAP as group ledger and covers Cash Flow Hedge using FX Forwards (including NDF) as hedging instruments.

The functionality helps you to automate labor-intensive processes, such as calculating net open exposure amount, creating hedging relationship for hedge item and hedge instrument, determining the key figures calculation (NPV, Spot, Forward), performing the valuation of FX transaction, checking classification, dealing with the dedesignation, and generating posting journal reports.

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
| Treasury Specialist - Middle Office |  | SAP_BR_TREASURY_SPECIALIST_MOE | Treasury Middle Office | SAP_BR_TREASURY_SPECIALIST_MOE |  |
| Treasury Specialist - Front Office |  | SAP_BR_TREASURY_SPECIALIST_FOE | Treasury Front Office | SAP_BR_TREASURY_SPECIALIST_FOE |  |
| Treasury Specialist - Back Office |  | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Treasury Accountant |  | SAP_BR_TREASURY_ACCOUNTANT | Treasury Accounting | SAP_BR_TREASURY_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represent materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Master Data | Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Valuation Area | 003 |  |  |
| Hedging Area | HAUS01 |  |  |
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
| 1X1 - Foreign Currency Risk Management | Must be run before this test script to create a business partner (counterparty). Follow description in the Create Business Partner preliminary step in the Foreign Currency Risk Management (1X1) test script to create one. |
| 1XN - Market Rates Management – Manually via Upload | Must be run before this test script to make market data available. |
| 1X1 - Foreign Currency Risk Management | If you want to use Designation Type which requires counter confirmation, you need to first maintain correspondence settings for business partner.Please refer to the Maintain Profile and BP Group Assignments to External Recipient preliminary step in the Foreign Currency Risk Management (1X1) test script for correspondence settings. |
| 1X1 - Foreign Currency Risk Management. | You may also need to maintain credit limits.Please refer to the Maintaining Credit Limit preliminary step in the Foreign Currency Risk Management (1X1) test script to maintain credit limits. |

### Premilinary Steps

#### Create Market Data Set

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The market data set is an entity referring to a set of different market data, each market data contributing to one data point for the linear regression used in effectiveness testing.

Two market data set categories are available:

- From Market Data Scenarios: the market data set refers to list of market data scenarios that can be individually defined, and thus may contain any artificial market data constellation.
- From Market Data Tables: the market data set refers to a list of historical market data selection dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Market Data Sets (TAN_MDS). | The Market Data Set Administration: Initial Screen displays. |  |
| 3 | Enter Basic Date for Market Date Set | On the Market Data Set Administration: Intimal Screen, enter the following data:Market Data Set ID: for example, ET01Choose Create.In the Create New MDS with First Version dialog box, enter the following data:MDS Category: for example, from Market Data TablesTotal Number of Data: for example, 3Valid From: for example, January 1st of last yearchoose Continue: | The Create Market Data Set <MDS ID> Version <Valid From Date> screen displays. |  |
| 4 | Create and Save Market Date Set | On the Create Market Data Set XXXX Version <Valid From Date> screen, enter the following data:Short Name: for example, MDS for ETLong Name: for example, MDS for Effectiveness TestTerm: for example, 1Time Unit: for example, MonthsChoose Save. | Message MDS <MDS ID> successfully saved displays. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

FX Forwards as Hedging Instruments:

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Define or Adjust Hedging Area](#unique_9) [page ] 11 | Treasury Specialist - Middle Office | Define Hedging Area (TOE_HEDGING_AREA) | Hedging Area is created or extended. |
| [Collect and Determine Exposure Data](#unique_10) [page ] 18 | Treasury Specialist - Middle Office | N/A | Exposure data is appropriately prepared outside of SAP system. |
| [Create Raw Exposure](#unique_11) [page ] 18 | Treasury Specialist - Middle Office | Process Raw Exposure (FTREX1) | Raw exposure is created and released. |
| [Take Snapshot](#unique_12) [page ] 20 | Treasury Specialist - Middle Office | Take Snapshot (TOESNAP) | Snapshot of exposures is created. |
| [Review Net Open Exposure in Hedge Management Cockpit](#unique_13) [page ] 21 | Treasury Specialist - Middle Office | Hedge Management Cockpit (TOENE) | Exposure, Net Exposure, and Net Open Exposure have been reviewed in app Hedge Management Cockpit (TOENE). |
| [Agree on Hedging Instrument](#unique_14) [page ] 22 | Treasury Specialist - Middle Office | N/A | Related teams and organizations have agreed on which financial instruments should be used as hedging instruments. |
| [Check Limit Utilization Report (Optional)](#unique_15) [page ] 22 | Treasury Specialist - Middle Office | Review Limit Utilizations (TBLB) | Limit utilization has been checked. |
| [Create Deliverable Forward Transaction](#unique_16) [page ] 23 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) | Deliverable Forward Transaction created and saved. |
| [Create Non-Deliverable Forward (NDF) Transaction](#unique_17) [page ] 25 | Treasury Specialist - Front Office | Create FX Spot/Forward (TX01) | NDF transaction data entered and created |
| [Automatic Designation (Planned)](#unique_18) [page ] 27 | Treasury Specialist - Back Office | Manage Hedging Relationships (TPM100);Process Spots/Forwards - Collective Processing (TX06);Reprocess Transactions - Automated Designation (TPM104) | Automatic designation is created in status Designation Planned. |
| [Set Contract Settlement Status with Incoming Confirmation](#unique_19) [page ] 31 | Treasury Specialist - Back Office | Process Spots/Forwards - Collective Processing (TX06) | Status of transaction becomes Contract Settlement. |
| [Release Hedging Relationship](#unique_20) [page ] 33 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120)Reverse Release of Hedging Business Transactions (TPM121) | Designation is released; hypothetical derivative is created; NPV and market value components are calculated at the designation date. |
| [Fix Derived Business Transaction](#unique_21) [page ] 36 | Treasury Accountant | Post Derived Business Transactions (TPM18) |  |
| Period End Closing |  |  |  |
| [Calculate NPV of Hedging Instrument and Hypothetical Derivative](#unique_22) [page ] 37 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA) | NPV and market value components are calculated at period end. |
| [Run Key Date Valuation](#unique_23) [page ] 39 | Treasury Accountant | Run Valuation (TPM1);Reverse Valuation (TPM2) | Valuation posting is created for FX transaction at period end. |
| [Run Classification](#unique_24) [page ] 42 | Treasury Accountant | Run Classification (TPM101);Reverse Classification (TPM102) | Classification posting is created on Exposure Subitem level at period end. |
| Contract Maturity |  |  |  |
| [(1X1) – Foreign Currency Risk Management and (34D) – Foreign Currency Risk Management – Group Ledger US GAAP](#unique_25) [page ] 44 | Treasury Specialist - Front Office;Treasury Specialist - Back Office;Treasury Accountant | Fix, Pay and Post Flows (TBB1)Automatic Payment Transactions for Payment Requests (F111)Process Business Transactions (TPM10)Post Derived Business Transactions (TPM18) | The FX transaction is exercised or expired.The postings for derived business transactions (if there are) at the end date of FX transaction are created in operative valuation area AE0 |
| [Process Dedesignation for Hedging Business Transaction at Maturity Date for Hedging Instrument](#unique_26) [page ] 46 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120) | Hedging Business Transaction is processed at the maturity date of hedging instrument. |
| [Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date](#unique_27) [page ] 48 | Treasury Accountant | Post Derived Business Transactions (TPM18) | Reclassification postings are created and relevant flows have been fixed at the end date of exposure subitem. |
| Reporting |  |  |  |
| [Display Treasury Position Flows](#unique_28) [page ] 50 | Treasury Accountant | Display Treasury Position Flows (F1754) | Position flows for FX transaction and exposure subitem are checked. |
| [Display Treasury Posting Journal](#unique_29) [page ] 51 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Posting journals for FX transaction and exposure subitem are checked. |
| [Display Treasury Position Values](#unique_30) [page ] 52 | Treasury Accountant | Display Treasury Position Values (F1867) | Position values for FX transaction and exposure subitem are checked. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### FX Forwards as Hedging Instruments

Purpose

This section covers the Hedge Management and Hedge Accounting process for forecast cashflows in foreign currencies according to a company’s hedging policy. The hedging instruments are FX forward contracts.

The treasury department is responsible for executing a given hedging policy for hedging the risk of forecast cashflows in foreign currencies of future periods. The forecast itself is represented as exposures in the Hedge Management Cockpit. A snapshot is taken for the forecast exposures from Exposure Management. Based on the snapshot, net open exposure amount, risk currency, and period are detailed in the Hedge Management Cockpit. Based on the hedging policy rules, the net open exposures are reduced by trading financial instruments such as an FX forward transaction. For expected inflows of a risk currency, the resulting exposure are closed by a FX forward that sells the inflow currency and buys the local currency of the company code. For expected outflows, a FX forward transaction is traded that buys the outflow currency and sells the local currency.

With the creation of the FX forward transaction, the financial transaction is automatically designated into a Hedging Relationship as a Hedging Instrument together with the exposure item of the Hedge Management Cockpit as Hedged Item. The matching exposure item is determined based on characteristics of the Hedging Instrument (for example, hedging classification, position currency of financial transaction, or maturity of financial transaction). At the same time, the Hypothetical Derivative is created and all necessary mathematical evaluations necessary for the measurement of ineffectiveness are performed and stored. For changes to the FX forward transaction, the Hedging Relationships are updated accordingly.

At period end, the determination of NPVs including the decomposition of market values for Hedging Instrument and the Hypothetical Derivative is performed, and the key date valuation of the FX forward transactions is executed. Meanwhile, the measurement and postings of the Hedging Reserve (OCI I), Cost of Hedging Reserve (OCI II), and ineffectiveness are executed on exposure subitem level. The period-end close can be executed using two different procedures: valuation and classification with Reset or without Reset.

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

In this section, as an example, one single Hedging Area HAUS01 for Hedge Accounting is created. During testing, HAUS01 can be shared by different company codes from different countries with different local currencies.

|  |
| --- |
| Note Hedging area HAUS01 is also used for testing Hedge Accounting for FX Forward – Local GAAP (3X1). Hedge Accounting for FX Forward supporting Local GAAP for the US, because the local GAAP of US is US GAAP. |

- Create a New Hedging Area: as the first tester to run 3X3 and 3X1 test scripts, create new hedging area HAUS01;
- Extend an Existing Hedging Area: If you find out that the hedging area HAUS01 already exists in the system, you can create a new version of HAUS01 and extend it by entering specific parameters of your valuation area/company code/country.

A company can have multiple Hedging Areas for Hedge Accounting according to its hedging policy. However, a hedge accounting relevant Hedging Classification can only be assigned to one Hedging Area for Hedge Accounting, therefore creating additional Hedging Area means the necessity of defining additional Hedging Classifications. Hedging Classification is a configuration which should be done via configuration step Define Hedging Classifications.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Hedging Classifications are predefined for US GAAP Cash Flow Hedge of FX risk by using FX Forwards:

- YFC08: Spot Element of FX forward contract is Hedging Reserve (OCI I), Forward Element of FX forward contract is Cost of Hedging Reserve (OCI II); Valuation will be carried out when releasing the designation. YFC08 should be always bundled with Hedging Profile S08 when maintaining tab Hedge Accounting II of a Hedging Area.

Procedure

Option 1: Create a New Hedging Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access another SAP Fiori App | Open Define Hedging Area (TOE_HEDGING_AREA). | The Define Hedging Area (TOE_HEDGING_AREA) view displays. |  |
| 3 | Enter Hedging Area ID | On the Display Hedging Area view, enter the following data and choose Create:Hedging Area: for example, HAUS01Note If Hedging area HAUS01 already exists notification displays, skip these steps and proceed to Option 2: Extend an Existing Hedging Area. If you find the parameters mentioned in Option 2 have been maintained, you can also skip Option 2, | The Create Hedging Areadialog box displays. |  |
| 4 | Enter Data in Dialog Box Create Hedging Area | In the Create Hedging Area dialog box, enter the following data and choose Create:Hedging Area: for example, HAUS01Description: for example, Hedging Area for Hedge Accounting using FX ForwardAuthorization Group: for example, HAG01Valid From: for example, <first day of current year>Without Template: <Choose this radio button> | The Change Hedging Area view displays. |  |
| 5 | Enter Data on Tab Main Data | On the Main Data tab, enter the following data:In the Risk-Free Currency group:Local Currency: <Choose this radio button>Note If you want to enable extraction of cross-currency exposures, please choose Currency Defined by the Source. By doing so, the risk-free currency is derived from the currency pair of the exposure item. If the source is Exposure Management, the risk-free currency is the target currency. If the source is Cash Management, the risk-free currency is the company code currency.Calendar Related: <select>Number of Periods: for example, 12Period Length: for example, MonthHedge Accounting: <select>Product Type for Exposure Subitems: 91AActivate SAP Trading Platform Integ.: <select>.Note Only choose this checkbox when testing integration with a trading platform. | Data on tab Main Data has been maintained. |  |
| 6 | Enter Data on Tab General Settings | Choose the General Settings tab, and enter the following data:Company Code: for example, 3310In subarea Differentiation Criteria: for example, select the checkbox of differentiation criterion Currency and Company CodeIn subarea Hedging Classification:Choose Add Hedging Classification, and enter the following data:Hdg Class.DescriptionDue Date ShiftYFC08FX Risk; CFH; Spot, Fwd., Amort.; w/o 1st Day ResultEOMN1 | Data on tab General Settings has been maintained. |  |
| 7 | Enter Data on Tab Currencies | Choose the Currencies tab.In subarea Hedging-Relevant Currencies, choose Add Currency, and enter the currencies that will be used as risk currencies in later steps in current test script. For example:USDBRL | Data on tab Currencies has been maintained. |  |
| 8 | Enter Data on Tab Filters for Exposures | Choose the Filters for Exposures tab.In the subarea Filter List for Exposures, choose Create Filter.In the dialog box New Filter for Exposures, enter the following data and choose Create Filter:Filter: for example, FLT_EXPFilter Description: for example, Filter for ExposuresSource: E_EM2In the subarea Other Filter - Specific Selections, enter the following data:Exposure Position Type: YFXNoteYou may also use E_FXEM Foreign Exchange Exposure Management instead of E_EM2 Exposure Management 2.0 as the data source for exposures.If you use E_FXEM Foreign Exchange Exposure Management as the data source for exposures, you will have to use app Manage FX Exposures (F7990) instead of app Process Raw Exposure (FTREX1) to create and submit the FX Exposure. | Data on tab Filters for Exposures has been maintained. |  |
| 9 | Enter Data on Tab Filters for Hedges | Choose the Filters for Hedges tab.In the subarea Filter List for Hedges, choose Create Filter.In the dialog box New Filter for Hedges, enter the following data and choose Create Filter:Filter: for example, FLT_HDGFilter Description: for example, Filter for HedgesSource: H_TMIn the subarea Other Filter - Specific Selections, enter the following data:Product Type: firstly enter 60A, then choose Multiple selection button beside the Product Type. In the Multiple Selection for Product Type dialog box, add another product type 60B, and choose Copy (F8). | Data on tab Filters for Hedges has been maintained. |  |
| 10 | Enter Data on Tab Hedge Accounting I | Choose the Hedge Accounting I tab.In subarea Designation Level, choose Insert, and enter the following data:CoCodeVADesig. LevelSplittingSequence3310003GBlank (Inactive)NIn subarea Designation Activation, choose Insert, and enter the following data:CoCodeVACurrencyDesig.3310003USD1 (Active)3310003BRL1 (Active)Note If you choose Currency Defined by the Source on the Main Data tab, another column for Target Currency is displayed, then you can maintain target currency here. | Data on tab Hedge Accounting I has been maintained. |  |
| 11 | Enter Data on Tab Hedge Accounting II | Choose the Hedge Accounting II tab.In subarea Designation Control, choose Insert, and enter the following data:CoCodeVAHdg Class.Des. TypePType ESIHdgProfileMDS ID3310003YFC08YFX1WS08ET01Note YFX1W is a designation type doesn't require counterconfirmation. There is another designation type YFX1C which requires counterconfirmation.When using YFX1C, hedging relationship can be released only after the corresponding hedging instrument has been successfully counterconfirmed, which requires to use correspondence functionality.PType ESI is to assign different product types for different exposure items classified by hedging classification. If you want to use just one product type maintained in the Main Data tab for all exposure items, please keep field PType ESI blank here. | Data on tab Hedge Accounting II has been maintained. |  |
| 12 | Save the Hedging Area | Choose Save (Ctrl+S). | Hedging area HAUS01 version 001 saved notification displays.The Hedging Area for Hedge Accounting is created successfully. |  |

Option 2: Extend an Existing Hedging Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Hedging Area (TOE_HEDGING_AREA). | The Define Hedging Area (TOE_HEDGING_AREA) view displays. |  |
| 3 | Enter Hedging Area ID | On the Display Hedging Area view, enter the following data and choose Display:Hedging Area: for example, HAUS01 | Hedging Area HAUS01 is displayed. |  |
| 4 | Create New Version | Choose New Version.In the Create New Version of Hedging Area HAUS01 dialog box, enter the following data and choose Create:Valid From: for example, <current date> | The Change Hedging Area view displays. |  |
| 5 | Update Data on General Settings Tab | Choose the General Settings tab, choose the Multiple selection button for the Company Code field.In the dialog box Multiple Selection for Company Code, add company code 3310 into the Select Single Values area, and choose Copy (F8). | Data on General Settings tab is updated. |  |
| 6 | Update Data on Currencies Tab | Choose the Currencies tab.In subarea Hedging-Relevant Currencies, choose Add Currency, and enter the currencies (if they have not been maintained) which will be used as risk currencies in later steps in current test script. For example:USDBRL | Data on the Currencies tab is updated. |  |
| 7 | Update Data on Hedge Accounting I Tab | Choose the Hedge Accounting I tab.In subarea Designation Level, choose Insert, and enter the following data:CoCodeVADesig. LevelSplittingSequence3310003GBlank (Inactive)NIn subarea Designation Activation, choose Insert, and enter the following data:CoCodeVACurrencyDesig.3310003AED1 (Active)3310003BRL1 (Active) | Data on the Hedge Accounting I tab is updated. |  |
| 8 | Update Data on Tab Hedge Accounting II | Choose the Hedge Accounting II tab.In subarea Designation Control, choose Insert, and enter the following data:CoCodeVAHdg Class.Des. TypePType ESIHdgProfileMDS ID3310003YFC08YFX1WS08ET01YFX1W is a designation type doesn't require counterconfirmation. There is another designation type YFX1C which requires counterconfirmation.When using YFX1C, hedging relationship can be released only after the corresponding hedging instrument has been successfully counterconfirmed, which requires correspondence functionality. | Data on Hedge Accounting IItab is updated. |  |
| 9 | Save the Hedging Area | Choose Save (Ctrl+S). | The Hedging area HAUS01 version XXX saved notification displays.The Hedging Area for Hedge Accounting has been extended to support your company code/country testing successfully. |  |

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

This step give you an example of how to maintain raw exposure manually. You can also import Raw Exposures from spreadsheet. For details, please refer to Option 2: Import the raw exposures from spreadsheet of step Create Raw Exposure in the Foreign Currency Risk Management (1X1) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Raw Exposure (FTREX1). | The Raw Exposure: Initial screen displays. |  |
| 3 | Enter Selection Criteria | On the Raw Exposure: Initial screen, enter the following data and choose Create.Exposure Activity Type: for example, YFXIIf the direction of consolidated FX exposure is outgoing, use Exposure Activity Type YFXO. | The Raw Exposure Maintenance: Create screen displays. |  |
| 4 | Enter Header Data | On the Raw Exposure Maintenance: Create screen and tab Header Data, enter the following data:Default Exposure Category: for example, 01 (Forecasted Transaction)Company Code: for example, 3310Cirt4ExpPosType: FX (FX Exposure)Direction: for example, IN (Incoming Cash Flow)Cirt4ExpPosType is a criterion used to derive the Exposure Position Type YFX which you entered on tab Filters for Exposures of Hedging Area.If you use Exposure Activity Type YFXO on the previous screen, please enter Direction OUT (Outgoing Cash Flow) on this screen. | Necessary header data is entered. |  |
| 5 | Enter Line Item Data | Choose tab Line Item Data.In sub-area Raw Exposure Line Item, choose Create New Line Item, and enter the following data:Exposure Due Date : for example: <Current date + 2 Months>Exposure Amount: for example, 1000000Exposure Amount Currency: for example, USDTarget Currency: for example, AEDChoose Create New Line Item again, and create another raw exposure line item:Exposure Due Date : for example: <Current date + 2 Months>Exposure Amount: for example, 2000000Exposure Amount Currency: for example, BRLTarget Currency: for example, AED | Necessary line item data is entered. |  |
| 6 | Save Raw Exposure | Choose Save. | A dialog box displays, and states that:Raw exposure has been saved;Raw exposure has been released;Position IDs have been updated.You can check exposure position and exposure position flows via app Process Exposure Positions (FTREX12) and Display Exposure Position Flows (FTREX13) |  |

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
| 2 | Take a Snapshot | Open Take Snapshot (TOESNAP). | The Take Snapshot screen displays. |  |
| 3 | Enter General Selections | Enter the following data and choose Run:Hedging Area: for example, HAUS01Description: for example, Snapshot for hedge accounting using FX ForwardDay Reference: <select>Extraction Date: for example , <the current date> | The Display logs screen displays and the snapshot is created. |  |

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
| 3 | Enter Selection Criteria | Enter the following data and choose Start:Hedging Area: for example, HAUS01Layout ID: for example, 1R_ALL_CHYou can also choose alternative layout IDs, or choose Manage Layouts to create new layout on next screen Layout Overview. | The Hedge Management Cockpit for Hedging Area HAUS01 view displays.The amounts of exposures are reflected in specific cells for differentiation criteria of raw exposures you created previously (company code, risk currency, period of due date, incoming/outgoing indicator of Exposure Activity Type).Select a cell and choose Drilldown (cell) to display more detailed information for Exposure Item, Exposure Position, or Raw Exposure.Note If you choose Currency Defined by the Source and exposure items are created based on the cross-currency exposures during snapshot, the hedge management cockpit displays the Target Currency, Risk Currency and Company Code Currency |  |

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
- According to the differentiating criteria (currency, company code, etc.) of the Hedging Area and by means of the Contract Start and Value Date, considering the due date shift setting , the Exposure Item of the Snapshot is determined.

Prerequisites

Business partner has been created, please see section [Business Conditions](#unique_6) [page ] 5.

If you used the Designation Type which requires counterconfirmation in step [Define or Adjust Hedging Area](#unique_9) [page ] 11, hedging relationship can be released only after the FX transaction has been successfully counterconfirmed, you need to run the correspondence process which will set the status of FX transaction to Counterconfirmed automatically after receiving the incoming confirmation from counterparty, and correspondence setting should be maintained for business partner before creating a FX transaction (please see section [Business Conditions](#unique_6) [page ] 5).

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Spot/Forward Transaction Entry: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: 60ATransaction Type: 102Partner: for example, 33537001 | The Spot/Forward Transaction Entry: Structure screen displays. |  |
| 4 | Enter Data on Tab Structure | On the Structure tab, enter the following data:Rate: for example, AED/USD 1.15Buy/Sell: for example, SellTraded Amt: for example, USD 100000Value Date: for example, <Current date + 1 Months>Contract Date: for example, <Current date>Note The currency of Traded Amt should be the risk currency. The amount of Traded Amt should be less or equal to the amount of Raw Exposure Line Item for this risk currency you created previously.The Value Date of FX transaction should be within the same period as the due date of exposure.You Buy risk currency (Traded Amt) if it is outgoing exposure. | Data on the Structure tab has been entered. |  |
| 5 | Enter Data in Administration tab | Choose the Administr. tab, and enter the following data:Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: for example, YFC08 (FX Risk; CFH; Spot, Fwd., Amort.; w/o 1st Day Result)Note When a FX hedge request ID is entered in a deal the corresponding exposure item is automatically assigned in the FX Hedge Management tab.Note The appropriate General Valuation Class will derive the correct Position Management Procedure for Hedge Accounting in valuation area 003 for US GAAP. | Data on the Administr. tab has been entered. |  |
| 6 | Save the FX Transaction | Choose Save.The dialog box Check Run: Transaction: Display messages shows up.Please make sure the following message is displayed:Position Comp.Code:XXXX VA:XXX ValCls:0045 DN:\INTERN\XXXX has been included in valuation on key date XXXXXXXXIn the dialog box Check Run: Transaction: Display messages, choose Continue (Enter) to save the transaction.Note Note down the transaction number. |  |  |

##### Create Non-Deliverable Forward (NDF) Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create non-deliverable forward (NDF) transactions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Front Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create FX Spot/Forward (TX01). | The Spot/Forward Transaction Entry: Initial view displays. |  |
| 3 | Enter Data on Initial View | Enter the following data and choose Enter:Company Code: for example, 3310Product Type: 60BTransaction Type: 110Partner: for example, 33537001 | The Spot/Forward Transaction Entry: Structure view displays. |  |
| 4 | Enter Data on Structure Tab | On the Structure tab, enter the following data:Rate: for example, AED/USD 3.65Buy/Sell: for example, SellTraded Amt: for example, USD 1000000Value Date: for example, <Current date + 1 Months>Fixing Date: for example, <Current date + 1 Months - 2 Days>Contract Date: for example, <current date>, and must be equal to or later than the valid from date of latest version of hedging area.Because of due date shift setting in hedging area, the Expiry Date of FX option should be within the period before the period in which the raw exposure will due.Remember The currency of Traded Amt is the risk currency. The amount of Traded Amt is less than or equal to the amount of the Raw Exposure Line Item for the risk currency you created previously.Note The Value Date of FX transaction is within the same period as the due date of exposure.Tip You Buy risk currency (Traded Amt), if it is an outgoing exposure. | Data for Structure is entered. |  |
| 5 | Enter Data in Administration tab | Choose the Administr. tab, and enter the following data:Gen. Valn Class: for example, 45 Derivatives: Cash FlowHdg Classific.: for example, YFC08 (FX Risk; CFH; Spot, Fwd., Amort.; w/o 1st Day Result)Note When a FX hedge request ID is entered in a deal the corresponding exposure item is automatically assigned in the FX Hedge Management tab.The appropriate General Valuation Class derives the correct Position Management Procedure for Hedge Accounting in valuation area 003 for US GAAP. | Data on tab Administr. has been entered. |  |
| 6 | Save the FX Transaction | Choose Save.The dialog box Check Run: Transaction: Display messages shows up.Please make sure the following message is displayed:Position Comp.Code:XXXX VA:XXX ValCls:0045 DN:\INTERN\XXXX has been included in valuation on key date XXXXXXXXIn the dialog box Check Run: Transaction: Display messages, choose Continue (Enter) to save the transaction.Note Note down the transaction number. |  |  |

After the FX transaction is saved, you can log on as Treasury Specialist - Middle Office and open app Hedge Management Cockpit (TOENE) to check the net open exposure again.

In the Hedge Management Cockpit (TOENE) app, the amounts of FX transactions are reflected in corresponding cells for Key Figure Name Net Hedges, and relevant company code, risk currency, and period; Net Open Exposure should be reduced accordingly.

#### Automatic Designation (Planned)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With saving the FX forward transaction, the Exposure Item in a snapshot is found and the Hedging Relationship is automatically created in status Designation Planned. The Exposure Item is determined based on attributes of the relevant Snapshot and Hedging Area and FX forward transaction.

This step introduces how to check the automatically created Hedging Relationship.

Procedure

Table 1: Option 1: via app Manage Hedging Relationships

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Hedging Relationships (TPM100). | The Manage Hedging Relationships screen displays. |  |
| 3 | Enter Selection Criteria | On the Manage Hedging Relationships screen, choose the Selection tab on the left side of screen, and enter the following data:Find: <All Hedging Relationships>By: <Hedging Instrument>Company Code: for example, 3310Valuation Area: 003Product Group: select the checkbox of OTC Trans., and choose OTC Transactions Selection beside OTC Trans.. In the OTC Transactions Selection dialog box, enter the transaction number(s) you noted down in the previous step, then choose Continue (Enter).Choose Start. | The list of Hedging Relationship Number(s) displays on the bottom-left side of screen. You may need to zoom out the screen in web browser to see it.Note Note down the Hedging Relationship Number(s) |  |
| 4 | Display Header of Hedging Relationship | Double click on one HR number on the bottom-left side of the screen, and you will see the detailed information of the hedging relationship on the right side of the screen.Check the data of Hedge Relationship Header. | The header of Hedging Relationship is displayed on the upper-right side of screen. It provides details which are relevant for the Hedging Relationship as general entity.The Hedging Relationship Status should be Designation Planned since it has not been released.Choose Display All Flows, and you can check the created flows resulting from the Designation.Choose Display H.Rel. Related Trans, in the Hedge Related Transactions for Hedging Relationship dialog box, double click on the row of Business Transaction Category Designation, where you can see the designation details in the Designation of Hedging Relationship dialog box. |  |
| 5 | Display Tab Hedging Relationship Detail | Check the data of the Hedge Relationship Details tab. | The Hedging Relationship Detail tab contains information about:Risk Type and Risk Profile DetailsDate information on Hedging Relationship levelThe following fields are automatically populated:Risk Currency: your exposure currencyNote If you choose Currency Defined by the Source and exposure items are created based on the cross-currency exposures, the Target Currency is displayed in the Hedge Relationship Details.Profile: the Hedging Profile which is mapped (on the Hedge Accounting II tab of Hedging Area) to the Hedging Classification you used when created FX transaction.Category: Cash Flow HedgeRisk Indicator: Currency RiskValid-From Date: contract date of FX transactionPlanned Desig. Date: contract date of FX transactionPlanned Dedesign. Date: Value Date of FX TransactionDesignation Type: the Designation Type which is mapped (on tab Hedge Accounting II of Hedging Area) to the Hedging Classification you used when created FX transaction |  |
| 6 | Display Tab Hedged Item | Choose the Hedged Item tab, and check data of it. | The Hedged Item tab contains information about:Hedged Item DetailsPosition Management information of the Exposure SubitemThe following fields are automatically populated:Hedged Item Number: generated numberNote down the Hedged Item Number.Start Date: contract date of FX transactionEnd Date: it is determined by the valuation date of FX forward and settng of due date shift in hedging area.Note Note down this date.Category: Planned ForecastHypothetical Derivative: empty at this moment, it will be created after designation is released.Product Group: ExposuresValuation Class: determined from pre-defined configuration on Product Type levelExposure Item ID: generated number.Note Note down the Exposure Item.Exposure Subitem ID: generated number.Note Note down the Exposure Subitem ID. |  |
| 7 | Display Tab Hedging Instrument | Choose the Hedging Instrument tab, and check data of it. | The Hedging Instrument tab contains information about:Hedging Instrument DetailsPosition Management information of the Hedging InstrumentThe following fields are automatically populated:Number: generated numberNote Note down the Hedging Instrument Number.Product Group: OTC Transactions: Money Market, FX, DerivativesValuation Class: derived from pre-defined configuration and the General Valuation Class you chose when created FX transactions.Transaction Number: the FX transaction number you created in previous step.Start Date: Contract Date of FX transactionEnd Date: Expiry Date of FX transaction |  |

Table 2: Option 2: via app Process Spots/Forwards - Collective Processing (TX06)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Spots/Forwards - Collective Processing (TX06) | The Forex: Collective Processing screen displays |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the FX transaction number(s) you created in the previous step> | The list of FX transaction(s) displays in area Forex: Collective Pro-cessing - Results. |  |
| 4 | Display Transaction | Select the checkbox of a transaction on Forex: Collective Processing - Results, and choose Display. | The OTC Option: Display: Structure screen displays. |  |
| 5 | Display the Hedging Relationship | Choose theAdministr. tab, choose Show Hedging Relationship.On the List of Hedging Relationships screen, select the checkbox of a Hedging Relationship, and then choose Display Hedging Rel.. | The P-Hedge Accounting screen displays, you can check detailed information of Hedging Relationship just like in the Manage Hedging Relationships (TPM100). |  |

If you cannot see the Hedging Relationship for your FX transaction via app Manage Hedging Relationships (TPM100) or Process Spots/Forwards - Collective Processing (TX06), or message Reprocessing of financial transaction required after save displays when you saved the FX transaction in step [Create Foreign Exchange Contract with Hedging Classification](#unique_33) [page ] 23, the system did not finish the automated designation of the financial transaction and exposure. To analyze the error situation and postprocess the financial transaction for the designation, use the Reprocess Transactions - Automated Designation (TPM104), for details please see the procedure as below:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reprocess Transactions - Automated Designation (TPM104). | The Reprocess Financial Transactions for Automated Designation screen displays. |  |
| 3 | Enter Selection Criteria | On the Reprocess Financial Transactions for Automated Designation screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 003Transaction: <the FX transaction number(s) you created in the previous step> | The Transaction Numbers screen displays.If you cannot see any transaction on this screen, please skip the current step because automated designation is created for the transaction(s) you selected on the previous screen. |  |
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

Once an FX transaction is saved in system, it is necessary to set the status of transaction to Contract Settlement before you create postings for flows. Usually it is done after you receive the incoming confirmation from a counterparty. Once you receive the counterparty confirmation, you settle the transaction using the following options:

- Option 1: Manual Settlement using the Process Spots/Forwards (Subtitle: Collective Processing) app
- Option 2: Automatic settlement using a Correspondence Process

|  |
| --- |
| Note For this procedure, only Option 1 - Manual Settlement is described. |

As described in Prerequisites section of the [Create Foreign Exchange Contract with Hedging Classification](#unique_33) [page ] 23 procedure, when you used the Designation Type that requires counterconfirmation, you must run the correspondence process. That process will set the status of FX transaction to Counterconfirmed automatically after receiving the incoming confirmation from counterparty. The correspondence setting should be maintained for business partner before creating an FX transaction (for more information see [Business Conditions](#unique_6) [page ] 5 in the Prerequisites section).

For details regarding how to do Automatic Settlement via Correspondence Process, see the Correspondence with PDF Form procedure in the Foreign Currency Risk Management (1X1) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06) | The Forex: Collective Processing view displays. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing view, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the FX transaction number(s)> | The list of FX transaction(s) displays in the Forex: Collective Processing - Results area. |  |
| 4 | Settle the Transaction | Select the checkbox of a transaction in area Forex: Collective Processing - Results, and choose Settle. | The Settle forex transaction: Structure view displays. |  |
| 5 | Save the Change | On the Settle Forex Transaction: Structure view, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If the Document lines: Display messages dialogue displays, choose Continue (Enter). | The transaction saves with Contract Settlement status. |  |

#### Release Hedging Relationship

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the automated designation which is in status Designation Planned. After release, the status will becomeDesignated.

Prerequisites

Market data (FX spot rates, interest rates) for relevant currencies have been maintained in system, for more information, see [Business Conditions](#unique_6) [page ] 5 under Prerequisites. The prospective effectiveness test uses linear regression test, which requires historical market data. Market data for the previous periods (for example, the previous three months) must also be available in the system.

If you use the Designation Type YFX1C, which requires counterconfirmation as described in the previous [Define or Adjust Hedging Area](#unique_9) [page ] 11 procedure. The hedging relationship can be released only after the FX transaction has been successfully counterconfirmed. Ensure that you have run the Correspondence with PDF Form procedure from the Foreign Currency Risk Management (1X1) test script. The correspondence process in 1X1 sets the status of FX transaction to Counterconfirmed automatically after the incoming confirmation from counterparty is received.

|  |
| --- |
| Note Open the configuration step Define Hedging Profiles, find out the hedging profiles you maintained in the Hedge Accounting II tab of hedging area HAUS01, and deselect the checkbox Documentation Optional (Yes/No) for each hedging profile, otherwise the Hedge Documentation cannot be displayed when releasing the hedging relationship. |

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

Release Hedging Relationship:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions view displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions view, enter the following data:Company code: for example, 3310Valuation Area: for example, 003Up to Key Date: for example, <contract date of FX Forward>Transaction Selection: <select>Transaction Number: <the FX transaction number(s)>Test Run: <deselect>Save Values with Warnings: <select>Detailed Log (Market Val. Calc): <select>Enter Posting Date: <select> | A new view Release Hedging Business Transactions displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions view, choose Run. | The Hedging Relationships view is displayed, and Hedging Relationship has been released without errors. |  |
| 5 | Check Market Data Calculation Details | Choose Display Market Value Calculation Details. | The NPVs including CVA/DVA from the Market Risk Analyzer view displays. You can see the details of the calculation of the full NPV as well as the Hedge Accounting Key Figures. The offered detail lists and analysis options are the same as the ones available in the Calculate Net Present Values (Subtitle: with CVA and DVA) app.Choose Hedge Accounting Key Figures, you can see the amounts of different components (spot, forward, and other components) of FX transaction and hypothetical derivative.Go back to the Hedging Relationships view. |  |
| 6 | Check Hedging Relationship | On the Hedging Relationships view, select the checkbox of an HR Number, choose Display Hedging Relationships. | The view Manage Hedging Relationships displays, and you can see Hedging Relationship Status is now Designated.Choose the Hedged Item tab, you can see the Hypothetical Derivative field has been filled with a generated number. |  |
| 7 | Check Effective Test Result | On the Hedging Relationships view, select the checkbox of an HR Number, choose Display Effectiveness Test. | Details of prospective effectiveness test display when designation appears.The prospective effectiveness test may lead to some errors, which stop the releasing of the hedging relationship:The effectiveness test has been executed, but it turned out that the hedging relationship is ineffective.Effectiveness could not be completely executed, for example. due to missing historical market data for some of the market data selection dates derived from the market data set. If so, choose Market Value Calculation Details to review the Error Log. |  |
| 8 | Display Hedge Documentation | On the Hedging Relationships view, select the checkbox of an HR Number, and choose Display Hedge Documentation. | The Hedging Relationship Documentation in PDF format opens. |  |

(Optional) Reverse Release of Hedging Relationship:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Release of Hedging Business Transactions (TPM121). | The Reverse Release of Hedging Business Transactions view displays. |  |
| 3 | Enter Selection Criteria | On the Reverse Release of Hedging Business Transactions view, enter the following data:Company code: for example, 3310Valuation Area: for example, 003Date to be Reversed: for example, <the contact date of transaction>Transaction Selection:selectedTransaction Number: <the FX transaction number(s)>Reversal Reason: for example, 04Enter Rev.Date: selectedTest Run: deselectOn the next view, Reverse Hedging Business Transactions, choose Run. | The Hedging Relationships view displays, and Release of Hedging Relationship has been reversed without errors. |  |
| 4 | Check Hedging Relationship | Select the checkbox of an HR Number, and choose Display Hedging Rela tionship. | The Manage Hedging Relationships view is displayed, and you can see Hedging Rel a tionship Status is returned to Designation Planned. |  |
| 5 | Release Hedging Relationship Again | Open the Release Hedging Business Transactions (TPM120) app, and release the Hedging Relationship again repeating these steps, otherwise you will not be able to continue the testing. | The Hedging Relationship is released again. |  |

#### Fix Derived Business Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you fix relevant derived flows then you are able to proceed the period end closing activities for FX transaction in later steps.

To schedule a background job for this procedure, refer to the corresponding step in the Appendix of the Foreign Currency Risk Management (1X1) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions view displays. |  |
| 3 | Enter Selection Criteria | On the Fix and Post Derived Business Transactions view, enter the following data:Subarea Product Groups:OTC Transactions: <select this checkbox>Exposure Items: <select this checkbox>Subarea General Selections:Company code: for example, 3310Valuation Area: for example, 003Subarea OTC Transactions:OTC Transactions: <the FX transaction number(s)>Subarea Exposure Items:Select from OTC Transactions: selectedSubarea Selections for Fixing Derived Business Transactions:TRL Date: <the contract date of FX transaction(s)>Subarea Posting Control:Test Run: deselectChoose Run. | One or more transactions to be fixed are displayed in Positions with Derived Business Transactions to Be Fixed. |  |
| 4 | Fix Derived Business Transactions | Choose Fix. | The Messages dialog box displays with message Derived business transaction from <date> was fixed notification. |  |

#### Period End Closing

This test script only introduces the period end closing activities of valuation area 003 (US GAAP Hedge Accounting).

For period end closing activities of valuation area AE0 (local GAAP) without hedge accounting, refer to the Period end has been reached procedure, under the Foreign Currency Risk Management and Accounting - Without Options section of Foreign Currency Risk Management (1X1) test script.

##### Calculate NPV of Hedging Instrument and Hypothetical Derivative

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you calculate the Net Present Values (Fair Values) of FX Transactions and corresponding Hypothetical Derivatives at the month end. The system also calculates market value components (spot, forward, and other components) for FX Transactions and corresponding Hypothetical Derivatives,

Prerequisites

Market data (FX spot rates, interest rates) for relevant currencies have been maintained in the system. Ensure that the [Business Conditions](#unique_6) [page ] 5, under the Prerequisites section, have been met.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments view displays. |  |
| 3 | Enter Selection Criteria and Execute | Enter the following data:Sub-area Selection Mode:Evaluation Parameter Derivatn: <select this checkbox>Select OTC Transactions: <select this checkbox>Market Value Decomposition: <select this checkbox>Sub-area Common Selection Criteria:Company Code: for example, 3310Valuation Area: for example, 003Sub-area OTC Transaction Selection Crit e ria:Transaction: <the FX transaction number(s)>Sub-area Evaluation Parameters:Evaluation Date: for example, <last date of current month>Sub-area Save Results:Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detail Log: <select this checkbox>Choose Run. | The NPVs including CVA/DVA from the Market Risk Analyzer view displays.You can see the NPV of each transaction on this view.You can also check different information by selecting the following buttons:Single Transaction:Hedge Accounting Key FiguresDetailed LogCalculation BasesError LogHedge Accounting Key Figures provides a list showing the detailed amount information of market value components (spot, forward, others) for FX Transactions and corresponding Hypothetical Derivatives. |  |

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

Prerequisite

NPVs and market value components values have been calculated for FX transitions and Hypothetical Derivatives in valuation area 003 (US GAAP).

Procedure

Run Valuation:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Valuation (TPM1). | The Run valuation screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run valuation screen, enter the following data:Sub-area Product Groups:Securities: <unselect this checkbox>OTC Transactions: <select this checkbox>Sub-area General Selections:Company code: for example, 3310Valuation Area: for example, 003Sub-area OTC Transactions:Transaction: <the FX transaction number(s)>Sub-area Valuation Parameters:Key Date for Valuation: for example, <last date of current month>Valuation Category: for example, Mid-year Valuation without ResetNote You can also use Mid-year Valuation with Reset. In addition to the valuation flows, reset flows will be generated for the day following the valuation key date (usually reset flows will be posted at the first date of next month). You can therefore see the effects of the valuation only on the valuation key date.Sub-area Posting Control:Test Run: <select this checkbox>Choose Run. | The Display Selected Treasury Positions for Valuation screen displays. |  |
| 4 | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log displays, if red traffic light exist, check the error message, solve the issue and perform test run again until there is no error.You can check the simulated Posting Log in valuation area 003 by choosing Logs + Messages, the offsetting account for fair value change of FX transaction is a Technical Clearing Account. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Run:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation screen displays. |  |
| 6 | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation screen, choose Run valuation. | The screen Valuation Log displays, you can check the Posting Log in valuation area 003 by choosing Logs + Messages, this time, accounting documents have been created in valuation area 003. |  |

(Optional) Reverse Valuation:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Valuation (TPM2). | The Reverse Valuation screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Reverse Valuation(TPM2) screen, enter the following data:Sub-area Product Groups:OTC Transactions: <select this checkbox>Sub-area General Selections:Company Code: for example, 3310Valuation Area: for example, 003Sub-area OTC Transactions:Transaction: <the FX Option transaction number(s)>Sub-area Valuation Parameters:Key Date for Valuation: for example, last date of current month, same as the date you ran valuationSub-area Posting Control:Reason for Reversal: for example, 04Test Run: <select this checkbox>Update Derived Bus. Trans: Use System SettingsChoose Run. | The Display Positions to Be Reversed screen displays. |  |
| 4 | Execute Reversal for Test Run | On the Display Positions to Be Reversed screen, choose Reverse Valuation. | If dialog Information Overview shows up, choose Reversal Log.The screen Reversal Log: Reversed Business Transactions displays, you can check the simulated reversal valuation postings in valuation area 003. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Run:Test Run: <deselect this checkbox> | The Display Positions to Be Reversed screen displays. |  |
| 6 | Execute Reversal for Production Run | On the Display Positions to Be Reversed screen, choose Reverse Valuation. | If dialog Information Overview shows up, choose Reversal Log.The screen Reversal Log: Reversed Business Transactions displays, you can check the reversal valuation postings in valuation area 003, accounting document has been created. |  |
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

The Classification of FX Transactions which are designated Hedging Relationship is executed via app Run Classification (TPM101) at month end.

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

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Classification (TPM101). | The Execute Classification view displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Execute Classification view, enter the following data and choose Run:Company Code: for example, 3310Valuation Area: for example, 003Key Date for Classification: for example, <last date of current month>Transaction Selection: <select this radio button>Transaction Number: <the FX transaction number(s)>Test Run: <select this checkbox> | The Information Overview dialog box displays. |  |
| 4 | Check Classification Log | In the Information Overview dialog box, choose Hedge Management. | The Information Overview view displays, you can review the Classification Log on this view. |  |
| 5 | Check Posting Log | Choose Back.In the Information Overview dialog box, choose Posting Log. | The Posting Log: Posted Business Transactions view displays.You can verify the simulated Classification postings for US GAAP (valuation area 003) on this view. The offsetting account for OCI I, OCI II, P/L Ineffective is also the Technical Clearing Account. |  |
| 6 | Execute Valuation for Production Run | Choose Back, and choose Close in the dialog box Information Ove rview.On the initial view of the Process Business Transactions (TPM10) app, change the following data and choose Run:Test Run: <deselect this checkbox> | The Information Overview view displays again.The classification postings have been created for US GAAP (valuation area 003), you can choose Posting Log to review the postings. |  |

(Optional) Reverse Classification:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Classification (TPM102). | The Reverse Classification view displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Reverse Classification view, enter the following data and choose Run:Company Code: for example, 3310Valuation Area: for example, 003Key Date for Classification: for example, <last date of current month>Transaction Selection: <select this radio button>Transaction Number: <the FX transaction number(s)>Reason for Reversal: for example, 04Test Run: <select this checkbox> | The Information Overviewdialog box displays. |  |
| 4 | Check Reversal Log | In the Information Overview dialog box, choose Reversal Log. | The view Reversal Log: Reversed Business Transa c tions displays, you can review the simulated reversal postings of classification for US GAAP (valuation area 003). |  |
| 5 | Execute Reversal for Production Run | Choose Back, and choose Close in the Information Overviewdialog box.On the initial view of Reverse Classification app, change the following data and choose Run:Test Run: <deselect this checkbox> | The Information Overview view displays again.The reversal postings of classification have been created for US GAAP (valuation area 003), you can choose Reversal Log to review the postings. |  |
| 6 | Run Classification Again | Open Run Classification (TPM101), and create the postings for Classification again (follow introductions in Run Classification), otherwise you will not be able to continue the testing. | Classification is executed again. |  |

#### Contract Maturity

##### (1X1) – Foreign Currency Risk Management and (34D) – Foreign Currency Risk Management – Group Ledger US GAAP

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When the FX transaction is mature, the relevant posting and payment process steps for closing FX transaction (which is a Hedging Instrument in Hedging Relationship) should be same as a normal FX transaction (which is not in a Hedging Relationship), relevant process steps are described in the Foreign Currency Risk Management (1X1) and the Foreign Currency Risk Management – Group Ledger US GAAP (34D) test scripts.

Procedure

Perform the following procedures under the Foreign Currency Risk Management and Accounting - Without Options section of the Foreign Currency Risk Management (1X1) test script for the FX transactions you created in the previous [Create Foreign Exchange Contract with Hedging Classification](#unique_33) [page ] 23 section.

| Step Name in 1X1 | Mandatory/Optional for Continuing Testing 3X3 | Purpose |
| --- | --- | --- |
| Transaction is Mature -> For NDF -> Fix Rate for NDF | Mandatory (only for NDF) | Fix the rate for a NDF transaction at the Fixing Date you specified when created NDF transaction in step Create Non-Deliverable Forward (NDF) Transaction. |
| Transaction is Mature -> Correspondence -> Set Settlement Status (Manual) | Mandatory (only for NDF) | Set the status of NDF transaction to Fixing Settlement manually after getting incoming confirmation form counterparty.. |
| Generate Payment Request for Mature Transaction | Mandatory | Generate payment request for outgoing payment of FX transaction at its Value Date via app Fix, Pay and Post Flows (TBB1). |
| Process Payment Request | Optional | Process the payment run procedure for payment request and create posting for outgoing payment via app Automatic Payment Transactions for Payment Requests (F111). |
| Post to General Ledger | Mandatory | Post the relevant flows (incoming or outgoing payment) at value date of FX transaction in valuation area AE0 (local GAAP) via app Fix, Pay and Post Flows (TBB1) and Process Business Transactions (TPM10). |
| Post Realized Profit and Loss | Mandatory | Post realized profit or loss at value date of FX transaction in valuation area AE0 (local GAAP) via app Post Derived Business Transactions (TPM18). |

Perform the following step in test script Foreign Currency Risk Management – Group Ledger US GAAP (34D) for the FX transactions you created in step [Create Foreign Exchange Contract with Hedging Classification](#unique_33) [page ] 23:

| Step Name in 34D | Mandatory/Optional for Continuing Testing 3X3 | Purpose |
| --- | --- | --- |
| Post Flows to General Ledger (Parallel Valuation Area) | Mandatory | Post the relevant flows (incoming or outgoing payment) at value date of FX transaction in valuation area 003 (US GAAP) via app Process Business Transactions (TPM10). |

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

Market data (FX spot rates, interest rates, credit spreads, basis spreads) for relevant currencies and reference entities have been maintained in system, please see Business Conditions in the Prerequisites. The market date should be valid at the maturity date of FX the transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions view displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions (TPM120) view, enter the following data and choose Run:Company Code: for example, 3310Valuation Area: for example, 003Up to Key Date: for example, the maturity date of FX transaction(s)Transaction Selection: <select this radio button>Transaction Number:the FX transaction number(s)Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new view Release Hedging Business Transactions displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions view, choose Run. | The Hedging Relationships view displays, and Hedging Relationship is processed for balance sheet crossover without errors. |  |
| 5 | Display Log of Hedge Management | On the Hedging Relationships view, select the checkbox of an HR Number, choose Display Log.In the Information Overview dialog box, choose Hedge Management. | The Information Overview view displays, you can review the Classification Log on this view. |  |
| 6 | Display Log of Posting | Choose Back.In the Information Overview dialog box, choose Posting Log. | The Posting Log: Posted Business Transactions view displays, you can review the postings on this view. |  |

Use app Post Derived Business Transactions (TPM18) to fix the derived business transactions for FX transaction at contract close date:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions view displays. |  |
| 3 | Enter Selection Criteria for Test Run | Enter the following data:Subarea Product Groups:OTC Transactions: selectedSubarea General Selections:Company code: for example, 3310Valuation Area: for example, 003Subarea Selections for Fixing Derived Business Transactions:TRL Date: <the maturity date of FX transaction(s)>Subarea Posting Control:Test Run:selectedChoose Run.If No scheduled derived business transactions were found for the selecttion displays, then there is no derived transaction available for your selection, you can skip current step.If Are you sure that you want to select future business transactions? displays, choose Enter. | One or more FX Transactions to be fixed and posted (test run) is displayed in Positions with Derived Business Transactions to Be Fixed. |  |
| 4 | Fix and Post for Test run | Choose Fix. | If Information Overview dialog box displays, choose Posting Log.New view Posting Log: Posted Business Transactions displays, you can see the simulated postings. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until you return to the initial view of this app.Change the following data and choose Run:Test Run: deselectIf Are you sure that you want to select future business transactions? notification displays, choose Enter. | One or more FX Transactions to be fixed and posted (production run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 6 | Fix and Post for Production Run | Choose Fix. | If Information Overview dialog box displays, choose Posting Log.New view Posting Log: Posted Business Transactions displays, you can see the postings for US GAAP (valuation area 003), accounting document has been created in corresponding ledger in Financial Accounting. |  |

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

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions view displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Fix and Post Derived Business Transactions view, enter the following data:Subarea Product Groups:OTC Transactions: <deselect this checkbox>Exposure Items: <select this checkbox>Subarea General Selections:Company Code: for example, 3310Valuation Area: for example, 003Subarea Selections for Fixing Derived Business Transactions:TRL Date: <the end date of hedged item which you noted down in step Automatic Designation (Planned)>Subarea Exposure Items:Transaction Number: <the FX transaction number(s)>Subarea Posting Control:Test Run: <select this checkbox>Choose Execute.If message Are you sure that you want to select future business transactions? displays, press Enter | One or more Exposure Subitems to be fixed and posted (test run) is displayed in Positions with Derived Business Transactions to Be Fixed. |  |
| 4 | Fix and Post for Test run | Choose Fix. | If the Information Overview dialog box displays, choose Posting Log.New view Posting Log: Posted Business Transactions displays, you can see the simulated reclassification postings of Hedging Reserve and Cost of Hedging Reserve for valuation area 003. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the initial view of this app.Change the following data and choose Execute:Test Run: <deselect this checkbox>Note If a Are you sure that you want to select future business transactions? notification displays, choose Enter. | One or more Exposure Subitems to be fixed and posted (production run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 6 | Fix and Post for Production run | Choose Fix.Note If a Information Overview dialog box displays, choose Posting Log. | The Posting Log: Posted Business Transactions view displays with the postings for valuation area 003. An accounting document has been created in corresponding ledger in Financial Accounting. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows view displays. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Position Flows view, enter the following data and choose Go:Product Group: <select OTC Transactions and Exposure Items>Company code: for example, AEDValuation Area: for example, 003For displaying position flows on OTC transaction level, enter:Transaction: <The FX transaction number(s)>For displaying position flows on Exposure Subitem level, enter:Exposure Item ID: <The Exposure Item ID you noted down in step Automatic Designation (Planned)>Exposure Subitem ID: <The Exposure Subitem ID you noted down in step Automatic Designation (Planned)>If the selection criteria Transaction, Exposure Item ID, Exposure Subitem ID do not exist on the view, choose Adapt Filters, and then choose the fields Exposure Item ID, Exposure Subitem ID from the subarea Exposure Items, and choose Transaction from the subarea OTC Transactions in the Adapt Filters dialog box. | All relevant position flows of FX transaction and Exposure Subitems are displayed in area Position Flows.Note To see the transaction ID, exposure item ID, and exposure subitem ID in the Position Flows area, choose Settings to change the layout. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal view displays. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Posting Journal view, enter the following data and choose Go:Product Group: <select OTC Transactions and Exposure Items>Company code: for example, 3310Valuation Area: for example, 003For displaying posting journal on OTC transaction level, enter:Transaction: <The FX transaction number(s)>Or for displaying posting journal on Exposure Subitem level, enter:Exposure Item ID: <The Exposure Item ID you noted down in step Automatic Designation (Planned)>Exposure Subitem ID: <The Exposure Subitem ID you noted down in step Automatic Designation (Planned)>If the selection criteria Transaction, Exposure Item ID, Exposure Subitem ID do not exist on the view, choose Adapt Filters, and then choose the fields Exposure Item ID, Exposure Subitem ID from the subarea Exposure Items, and choose Transaction from the subarea OTC Transactions in the Adapt Filters dialog box. | All relevant posting journal line items are displayed in area Line Items, you can see the line items on FX transaction level or Exposure subitem level.Note To see the transaction ID, exposure item ID, and exposure subitem ID in the Position Flows area, choose Settings to change the layout. |  |

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

### Overhedge Processing - Dedesignation

Purpose

With the reduction of a planned cash flow of an exposure period, an overhedge situation occurs (that is, a partial volume of the hedged item that is a forecast transaction is no longer highly probable). A Hedge Request type Dedesignation allows to dedesignate the Hedging Relationship to solve the overhedge situation.

Depending on the selected type of Reclassification Handling, the reclassification of the Hedging Reserve and Cost of Hedging Reserve amounts is posted immediately with the release of the Hedging Business Transaction or at the Exposure Item End Date.

Prerequisites

The following steps under section [FX Forwards as Hedging Instruments](#unique_32) [page ] 11 have been executed:

- Define or Adjust Hedging Area
- Create Raw Exposure
- Take Snapshot
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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Raw Exposure (FTREX1). | The Raw Exposure: Initial view displays. |  |
| 3 | Enter Selection Criteria | On the Raw Exposure: Initial view, enter the following data and choose Create.Exposure Activity Type: for example, YFXI | The Raw Exposure Maintenance: Create view displays. |  |
| 4 | Enter Header Data | On the Raw Exposure Maintenance: Create view and tab Header Data, enter the following data:Default Exposure Category: for example, 01 (Forecasted Transaction)Company Code: for example, 3310Cirt4ExpPosType: FX (FX Exposure)Direction: for example, IN (Incoming Cash Flow) | Necessary header data is entered. |  |
| 5 | Enter Line Item Data | Choose tab Line Item Data.In sub-area Raw Exposure Line Item, choose Create New Line Item, and enter the following data:Due Date: for example, <Current date + 2 Months>Exposure Amount: for example, -500000Exposure Amount Currency: for example, USDTarget Currency: for example, EUR | Necessary line item data is entered. |  |
| 6 | Save Raw Exposure | Choose Save. | A dialog box displays, and states that:Raw exposure has been saved;Raw exposure has been released;Position IDs have been updated.You can check Exposure Position and Exposure Position Flows via app Process Exposure Positions (FTREX12) and Display Exposure Position Flows (FTREX13).In the example, after the raw exposure is created, the incoming exposure in a specific period will be 500000 less than the initial estimated exposure data. |  |

#### Take Snapshot

Purpose

Take a new snapshot to reflect reduction of exposure for an overhedge situation.

Procedure

Execute the [Take Snapshot](#unique_12) [page ] 20 procedure under the [FX Forwards as Hedging Instruments](#unique_32) [page ] 11 section of the Test Procedures.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Hedge Management Cockpit (TOENE). | The Hedge Management Cockpit for Hedging Area view displays. |  |
| 3 | Enter Selection Criteria | On the Hedge Management Cockpit for Hedging Area view, enter the following data and choose Start:Hedging Area: for example, HAUS01Layout ID: for example, 1R_ALL_CH | The Hedge Management Cockpit for Hedging Area HAUS01 displays.You can see the amount of exposure have been reduced in the cell for relevant period (for example, current month + two months) and risk currency (for example, USD) in accordance to the new raw exposure you just created. |  |
| 4 | Create Dedesignation Request | Choose a cell for relevant period and risk currency in accordance to the new raw exposure you just created.Choose Hedge Request > Dedesignation Request. | The Hedge Request view displays. |  |
| 5 | Enter and Check Date for Dedesignation Request | On the Hedge Request view, enter the following data:Header:Description (the field beside field Hedge Request ID): <any text>Tab General:Hedge Req. Reason: S001Dedes.Date: <the date in the period you reduce the exposure, which must be earlier than the value date of the FX Forward Transaction you created in the Prerequisites section of Overhedge Processing - Dedesignation, for example, <Current date + 15 days>Hedge Request Volume: <the reduced exposure amount>, for example, 500000Tab Hedging Relationships:Valuation Area: 003Reclass. Handling: for example, Immediate ReclassificationSelect the checkbox Requested for the row with the Transaction Number and HR Number you noted down when executing the steps mentioned in the Prerequisites section of [Overhedge Processing - Dedesignation](#unique_35) [page ] 54.Request Volume (of the row you selected): <the reduced exposure amount>, for example, 500000Sequence: for example, 1Choose Check.Two options of Reclass. Handling:Immediate Reclassification: the OCI I, OCI II of dedesignated portion is reclassified immediately with release of the Hedging Business Transaction.Planned Reclassification: the OCI I, OCI II of dedesignated portion will be reclassified at the end date of exposure subitem. | Message Hedge Request is consistent displays, means the data you entered is OK, otherwise please check your data until this message displays. |  |
| 6 | Submit Dedesignation Request | Choose Submit. | The Hedge Request number was saved notification displays.Note down the Hedge Request ID. |  |

#### Process Dedesignation for Hedging Business Transaction

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the hedging business transaction at dedesignation date.

The following activities are done with the release of hedging business transaction at the dedesignation date:

- Calculation and saving of NPV of FX forward transaction
- Calculation and saving of NPV component values (spot, forward, others) for FX forward transaction and hypothetical derivative
- Execution and posting of the key date valuation of the FX forward transaction to be dedesignated with actual NPV values
- Execution and posting of the classification of the selected Hedging Relationship with actual NPV component values
- Update amounts of flows of dedesignation update types
- Fix update types of planned dedesignation flows
- Fix and post update types of reclassification flows (if chose 'Immediate Reclassification' in hedge request)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions view displays. |  |
| 3 | Release Hedging Business Transaction | On the Release Hedging Business Transactions view, enter the following data:Company code: for example, 3310Valuation Area: for example, 003Up to Key Date: for example, <the dedesignation date you specified in the Dedesignation Request>Transaction Selection: <select this radio button>Transaction Number:<the FX Forward transaction number>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A Release Hedging Business Transactions view displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions view, choose Run. | The Hedging Relationships view displays, and Hedging Relationship has been processed for balance sheet crossover without errors. |  |
| 5 | Check Market Data Calculation Details | Choose Display Market Value Calculation Details. | The NPVs including CVA/DVA from the Market Risk Analyzer view displays. You can see the details of the calculation of the full NPV as well as the Hedge Accounting Key Figures.Go back to the Hedging Relationships view. |  |
| 6 | Check Log and Message | On the Hedging Relationships view, select the checkbox of an HR Number, and select Display Log. | Dialog box Information Overview displays, you can check:Hedge management logPosting logMessagesGo back to the Hedging Relationships view. |  |

|  |
| --- |
| Note To review the relevant hedging relationship, use the Manage Hedging Relationships (TPM100) SAP Fiori app. Change the display date to the dedesignation date, and the designated amount of Hedged Item and Hedging Instrument are reduced. |

### Termination of Hedging Instrument

Purpose

The termination of hedging instrument (FX forward or NDF) leads to the discontinuation of hedge accounting.

This section describes how to terminate hedging instrument and discontinue hedge accounting.

#### Create, Submit and Release Termination Request for a Forward

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In some cases, for example, you may need to terminate a hedging instrument for some reason, for example, if a long-run FX forward is over-hedged.

After aligning with your counterpart, you decide to terminate the hedging instrument. You start the termination process via termination request in hedge management cockpit. In this step, you select the hedging instrument in the hedge management cockpit to create and submit a termination request. The request needs to be released after it is submitted.

Prerequisites

You have created an FX forward as hedging instrument, and its status is set to Contract Settlement. You have created a hedging relationship and released the designation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Hedge Management Cockpit (TOENE) |  |  |
| 3 | Enter Selection Criteria | Make the following entries, and choose Start:Hedging Area: For example, HAUS01Layout ID: 2R_TQ_CH | The Hedge Management Cockpit for Hedging Area HAUS01 is displayed with Net Hedges |  |
| 4 | Create Termination Request | Double click on key figure Net Hedges in the period of the value date of the forward transaction you just created as prerequisite.Select the transaction you just created, click Hedge Request and choose Termination Request in the dropdown list | The Create Hedge Request screen is displayed. |  |
| 5 | Submit Termination Request | Enter description for edge request: terminate forwardEnter the following data on the General tab, and choose Submit:Hedge Request Reason: Choose S003 Overhedge Processing - TerminationNote Overruling not allowed | Terminate Request is submitted with termination request ID.Remember Note down the ID. |  |
| 6 | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start:Hedging Area: for example, HAUS01 | Hedge requests that match the filter criteria are displayed. |  |
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

In some cases, for example, if a long-run FX forward is over-hedged, you may need to terminate the transaction after aligning with your counterparty.

In this step, you terminate an FX forward transaction as a hedging instrument in system.

Prerequisites

- You have created the hedging relationship has been created, and has released the designation.
- You have created an FX forward transaction as hedging instrument, and its status has been changed to Contract Settlement

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06) | The Forex: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the FX transaction number to be terminated> | A list of FX transactions is displayed in the Forex: Collective Processing - Results area. |  |
| 4 | Terminate the Transaction | Select the checkbox of the transaction to be terminated in the Forex: Collective Processing - Results area, and choose Terminate. | The Terminate Forex Transaction: Structure screen is displayed. |  |
| 5 | Save the Termination | On the Terminate Forex Transaction: Structure screen, the value of field Activity in header is 3 - Termination.enter the following data in sub-area Termination:Date: <the termination data, it should be a date between contract date and value date>Payment Date: for example, <termination data + 2 days>Entry Type: for example, RateRate: for example, 1.16Choose Save.If the Document lines: Display messages dialogue is displayed, choose Continue (Enter). | The payment amount for termination is calculated and the transaction is saved with status Termination. |  |
| 6 | Access the SAP Fiori App | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start.:Hedging Area: for example, HAUS01 | hedge requests that match the filter criteria are displayed. |  |
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

After you terminate an FX forward transaction, you need to set its status to Termination Settlement before you could create postings for termination flow. Usually it is done after you receive the incoming confirmation about termination from your counterparty.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. |  |  |
| 2 | Access the SAP Fiori app | Open Process Spots/Forwards - Collective Processing (TX06) | The Forex: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Forex: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the FX transaction number in status Termination> | A list of FX transactions is displayed in the Forex: Collective Processing - Results area. |  |
| 4 | Settle the Termination | Select the checkbox of the transaction to be settled in the Forex: Collective Processing - Results area, and choose Settle. | The Settle Forex Transaction: Structure screen is displayed. |  |
| 5 | Save the Termination Settlement | On the Settle Forex Transaction: Structure screen, the value of field Activity in header is 4 - Termination Settlement.Choose Save.If the Document lines: Display messages dialogue displays, choose Continue (Enter). | The transaction is saved with status Termination Settlement. |  |

#### Process Dedesignation for Hedging Business Transaction at Termination Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the hedging business transaction at termination date. During this process, the hedging relationship is de-designated, and the following activities are done with the processing of hedging business transaction on the termination date:

- Calculation and saving of NPV of FX forward transaction
- Calculation and saving of NPV component values (spot, forward, others) for FX forward transaction and hypothetical derivative
- Execution and posting of the key date valuation of the FX forward transaction to be terminated with up-to-date NPV values
- Execution and posting of the classification of the Hedging Relationship with up-to-date NPV component values
- Fix and update other relevant position flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions screen is displayed. |  |
| 3 | Release Hedging Business Transaction | On the Release Hedging Business Transactions screen, enter the following data:Company code: for example, 3310Valuation Area: for example, 003Up to Key Date: for example, <the termination date>Transaction Selection: <select this radio button>Transaction Number: <the FX Forward transaction number terminated>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions is displayed. |  |
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

In this step, you post operative flows and derived flows at payment date of termination.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Accountant. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Fix, Pay and Post Flows (TBB1) | The Treasury: Post Flows screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Post Flows screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the FX transaction number terminated>Up to and Including Due Date: <the payment date of termination>Test Run: <deselect this checkbox>Post All Valuation Areas: <select this radio button》 | The Information Overview dialog box is displayed. |  |
| 4 | Check Posting Log | In the Information Overview dialog box, choose Posting Log. | Posting journals are displayed. |  |

|  |
| --- |
| Note If termination results in outgoing payment with a payment request, please refer to the Foreign Currency Risk Management (1X1) test script for automatic payment of payment requests.Reclassification of Hedging Reserve and Cost of Hedging Reserve should be executed on the Exposure Subitem End Date, which is the same as the normal hedge accounting process without termination of hedging instrument. |

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

You have performed following sections of this test script:

- [Create Foreign Exchange Contract with Hedging Classification](#unique_33) [page ] 23
- [Automatic Designation (Planned)](#unique_18) [page ] 27
- [Set Contract Settlement Status with Incoming Confirmation](#unique_19) [page ] 31

NPV values of the FX Transaction as well as the component NPV values need to be stored before the valuation and classification processing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Simulate Period-End Closing (TPM_SIM_VAL). | The Run Simulated Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Run Simulated Valuation screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, 003Product Type: for example,60ATransaction Number: for example, <the transaction number created in the previous steps>Recalculate Outdated Sim.Val.: <deselect this checkbox>Position Value Date: for example, <the current date>Test Run: <select this checkbox> | The following message is displayed:Processed xx positions; xx successful, 0 failed.If simulated valuation has been executed on key date, the following message is displayed:xx simulated valuation(s) deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
| 4 | Execute Simulated Valuation | The dialog Message shows up, and choose Continue. | The screen Simulated Valuation Result is displayed.You can check the simulated valuation information for local GAAP (valuation area 003). Please note there is no simulated valuation created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back to the initial screen of this app.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The dialog Messages screen is displayed. |  |
| 6 | Execute Simulated Valuation for Production Run | The dialog Message shows up, and choose Continue. | The screen Simulated Valuation Result is displayed.You can check the simulated valuation information for local GAAP (valuation area 003). |  |

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
| 2 | Access the SAP Fiori app | Open Delete Results of Simulated Period-End Closing (TPM_SIM_VAL_DEL). | The Delete Simulated Valuation screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Delete Simulated Valuation screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: leave bank, or enter specific valuation are, for example, 003Product Type: for example,60ATransaction Number: for example, <the transaction number created in the previous steps>Position Value Date: for example, <the date on which the reversal should takes place>Test Run: <select this checkbox> | The following message is displayed:xx simulated valuation(s) deleted for key date. |  |
| 4 | Enter Selection Criteria for Production Run | Go back to the initial screen of this app.On the Delete Simulated Valuation screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The following message is displayed:simulated valuation(s) deleted for key date. |  |

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
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-group-ledger-ifrs-2rw-ae-test-script-85]]
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-group-ledger-us-gaap-3x4-ae-test-script]]
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-local-gaap-3x2-ae-985]]
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-swap-group-ledger-ifrs-2uf-ae-870]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3X3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 129,700 chars in the whole document
