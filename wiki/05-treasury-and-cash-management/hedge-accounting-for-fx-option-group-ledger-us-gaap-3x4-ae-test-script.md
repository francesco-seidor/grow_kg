---
id: 05-treasury-and-cash-management/hedge-accounting-for-fx-option-group-ledger-us-gaap-3x4-ae-test-script
title: Hedge Accounting for FX Option – Group Ledger US GAAP (3X4_AE) – Test Script (3X4_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 3X4: US GAAP cash flow hedge accounting with European FX options (vanilla and collar), incl. dedesignation, termination."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/hedge-accounting-fx]
aliases: [3X4_S4CLD2608_BPD_EN_AE]
keywords: [Hedge Accounting for FX Exposures, hedge accounting, fx options, hedging area, zero cost collar, hedging relationship, exposure management, period end closing, dedesignation, hedging instrument termination]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3X4_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-987
topic: 05-treasury-and-cash-management/hedge-accounting-fx
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Hedge Accounting for FX Option – Group Ledger US GAAP (3X4_AE) – Test Script (3X4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3X4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Hedge Accounting for FX Exposures** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Hedge Accounting for FX Option – Group Ledger US GAAP (3X4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232854155)

[2 Prerequisites 4](#_Toc232854156)

[2.1 System Access 4](#_Toc232854157)

[2.2 Roles 4](#_Toc232854158)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232854159)

[2.4 Business Conditions 5](#_Toc232854160)

[2.5 Premilinary Steps 6](#_Toc232854161)

[2.5.1 Create Market Data Set 6](#_Toc232854162)

[3 Overview Table 8](#_Toc232854163)

[4 Test Procedures 11](#_Toc232854164)

[4.1 FX Options as Hedging Instruments 11](#_Toc232854165)

[4.1.1 Define or Adjust Hedging Area 12](#_Toc232854166)

[4.1.2 Collect and Determine Exposure Data 18](#_Toc232854167)

[4.1.3 Create Raw Exposure 18](#_Toc232854168)

[4.1.4 Take Snapshot 20](#_Toc232854169)

[4.1.5 Review Net Open Exposure in Hedge Management Cockpit 21](#_Toc232854170)

[4.1.6 Agree on Hedging Instrument 21](#_Toc232854171)

[4.1.7 Check Limit Utilization Report (Optional) 22](#_Toc232854172)

[4.1.8 Create Foreign Exchange Contract with Hedging Classification 22](#_Toc232854173)

[4.1.8.1 Create Plain Vanilla FX Option 23](#_Toc232854174)

[4.1.8.2 Create Zero/Low Cost Collar FX Option (Cylinder Option) 25](#_Toc232854175)

[4.1.8.2.1 Option 1: Create Two Options Separately and Create Option Reference 25](#_Toc232854176)

[4.1.8.2.2 Option 2: Create Zero/Low Cost Collar FX Option in Single Step 29](#_Toc232854177)

[4.1.9 Automatic Designation (Planned) 32](#_Toc232854178)

[4.1.10 Set Contract Settlement Status with Incoming Confirmation 37](#_Toc232854179)

[4.1.11 Release Hedging Relationship 38](#_Toc232854180)

[4.1.12 Process Premium Payment 41](#_Toc232854181)

[4.1.13 Period End Closing 42](#_Toc232854182)

[4.1.13.1 Calculate NPV of Hedging Instrument and Hypothetical Derivative 42](#_Toc232854183)

[4.1.13.2 Run Key Date Valuation 44](#_Toc232854184)

[4.1.13.3 Run Classification 47](#_Toc232854185)

[4.1.14 Contract Maturity 50](#_Toc232854186)

[4.1.14.1 (1X1) – Foreign Currency Risk Management and (34D) – Foreign Currency Risk Management – Group Ledger US GAAP 50](#_Toc232854187)

[4.1.14.2 Process Dedesignation for Hedging Business Transaction at Maturity Date for Hedging Instrument 52](#_Toc232854188)

[4.1.15 Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date 54](#_Toc232854189)

[4.1.16 Reporting 56](#_Toc232854190)

[4.1.16.1 Display Treasury Position Flows 56](#_Toc232854191)

[4.1.16.2 Display Treasury Posting Journal 57](#_Toc232854192)

[4.1.16.3 Display Treasury Position Values 58](#_Toc232854193)

[5 Appendix 60](#_Toc232854194)

[5.1 Overhedge Processing - Dedesignation 60](#_Toc232854195)

[5.1.1 Create Raw Exposure 60](#_Toc232854196)

[5.1.2 Take Snapshot 62](#_Toc232854197)

[5.1.3 Create and Submit Dedesignation Request 62](#_Toc232854198)

[5.1.4 Release Dedesignation Request 64](#_Toc232854199)

[5.1.5 Process Dedesignation for Hedging Business Transaction 66](#_Toc232854200)

[5.2 Termination of Hedging Instrument 68](#_Toc232854201)

[5.2.1 Create, Submit and Release Termination Request for Hedging Instrument 68](#_Toc232854202)

[5.2.2 Terminate Hedging Instrument 69](#_Toc232854203)

[5.2.3 Set Termination Settlement Status for Hedging Instrument 71](#_Toc232854204)

[5.2.4 Process Dedesignation for Hedging Business Transaction at Termination Date 72](#_Toc232854205)

[5.2.5 Post Flows for Termination 73](#_Toc232854206)

[5.3 Simulated Valuation 74](#_Toc232854207)

[5.3.1 Run Simulated Valuation 74](#_Toc232854208)

[5.3.2 Delete Simulated Valuation 76](#_Toc232854209)

## Purpose

Overview

This process helps you to mitigate profit and loss volatility from the use of derivatives.

Currently, the scope item supports US GAAP as group ledger and covers Cash Flow Hedge using European Style FX Option as hedging instruments.

The functionality helps you to automate labor-intensive processes, such as calculating net open exposure amount, creating hedging relationship for hedge item and hedge instrument, determining the key figures calculation (NPV, Intrinsic Value, Time Value), performing the valuation of FX transaction, checking classification, dealing with the dedesignation, and generating posting journal reports.

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

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Valuation Area | 003 |  |  |
| Hedging Area | HAUS02 |  |  |
| Business Partner | 33537001 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

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
| 1X1 - Foreign Currency Risk Management | You may also need to maintain credit limits.Please refer to the Maintaining Credit Limit preliminary step in the Foreign Currency Risk Management (1X1) test script to maintain credit limits. |

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

The market data set is an entity referring to a set of different market data, each market data contributing to one data point for the linear regression used in effectiveness test.

Two market data set categories are available:

- From Market Data Scenarios: the market data set refers to list of market data scenarios which can be individually defined and thus may contain any artificial market data constellation.
- From Market Data Tables: the market data set refers to a list of historical market data selection dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Market Data Sets (TAN_MDS). | The Market Data Set Administration: Initial Screen displays. |  |
| 3 | Enter Basic Date for Market Date Set | On the Market Data Set Administration: Initial Screen, enter the following data:Market Data Set ID: for example, ET02Choose Create.In the Create New MDS with First Version dialog box, enter the following data:MDS Category: for example, from Market Data TablesTotal Number in MDS: for example, 3Valid From: for example, January 1st of last yearChoose Continue. | The Create Market Data Set <MDS ID> Version <Valid From Date> screen displays. |  |
| 4 | Create and Save Market Date Set | On the Create Market Data Set XXXX Version <Valid From Date> screen, enter the following data:Short Name: for example, MDS for ETLong Name: for example, MDS for Effectiveness TestTerm: for example, 1Time Unit: for example, MonthsChoose Save. | Message MDS <MDS ID> successfully saved displays. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

FX Options as Hedging Instruments:

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Define or Adjust Hedging Area](#unique_9) [page ] 12 | Treasury Specialist - Middle Office | Define Hedging Area (TOE_HEDGING_AREA) | Hedging Area is created or extended. |
| [Collect and Determine Exposure Data](#unique_10) [page ] 18 | Treasury Specialist - Middle Office | N/A | Exposure data is appropriately prepared outside of SAP system. |
| [Create Raw Exposure](#unique_11) [page ] 18 | Treasury Specialist - Middle Office | Process Raw Exposure (FTREX1) | Raw exposure is created and released. |
| [Take Snapshot](#unique_12) [page ] 20 | Treasury Specialist - Middle Office | Take Snapshot (TOESNAP) | Snapshot of exposures is created. |
| [Review Net Open Exposure in Hedge Management Cockpit](#unique_13) [page ] 21 | Treasury Specialist - Middle Office | Hedge Management Cockpit (TOENE) | Exposure, Net Exposure, and Net Open Exposure have been reviewed in app Hedge Management Cockpit (TOENE). |
| [Agree on Hedging Instrument](#unique_14) [page ] 21 | Treasury Specialist - Middle Office | N/A | Related teams and organizations have agreed on which financial instruments should be used as hedging instruments. |
| [Check Limit Utilization Report (Optional)](#unique_15) [page ] 22 | Treasury Specialist - Front Office | Review Limit Utilizations (TBLB) | Limit utilization has been checked. |
| [Create Foreign Exchange Contract with Hedging Classification](#unique_16) [page ] 22 | Treasury Specialist - Front Office | Create OTC Option (TI71) | FX transactions is created as hedging instruments. |
| [Automatic Designation (Planned)](#unique_17) [page ] 32 | Treasury Specialist - Back Office | Manage Hedging Relationships (TPM100);Process OTC Options - Collective Processing (TI91);Reprocess Transactions - Automated Designation (TPM104) | Automatic designation is created in status Designation Planned. |
| [Set Contract Settlement Status with Incoming Confirmation](#unique_18) [page ] 37 | Treasury Specialist - Back Office | Process OTC Options - Collective Processing (TI91) | Status of transaction becomes Contract Settlement. |
| [Release Hedging Relationship](#unique_19) [page ] 38 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120)Reverse Release of Hedging Business Transactions (TPM121) | Designation is released; hypothetical derivative is created; NPV and market value components are calculated at the designation date. |
| [Process Premium Payment](#unique_20) [page ] 41 | Treasury Specialist - Back Office;Treasury Accountant | Fix, Pay and Post Flows (TBB1);Automatic Payment Transactions for Payment Requests (F111);Process Business Transactions (TPM10) | Premium payment and posting are processed. |
| [Calculate NPV of Hedging Instrument and Hypothetical Derivative](#unique_21) [page ] 42 | Treasury Specialist - Back Office | Calculate Net Present Values - With CVA and DVA (TPM60CVA) | NPV and market value components are calculated at period end. |
| [Run Key Date Valuation](#unique_22) [page ] 44 | Treasury Accountant | Run Valuation (TPM1);Reverse Valuation (TPM2) | Valuation posting is created for FX transaction at period end. |
| [Run Classification](#unique_23) [page ] 47 | Treasury Accountant | Run Classification (TPM101);Reverse Classification (TPM102) | Classification posting is created on Exposure Subitem level at period end. |
| [(1X1) – Foreign Currency Risk Management and (34D) – Foreign Currency Risk Management – Group Ledger US GAAP](#unique_24) [page ] 50 | Treasury Specialist - Front Office;Treasury Specialist - Back Office;Treasury Accountant | Process OTC Options - Collective Processing (TI91);Post Derived Business Transactions (TPM18) | The FX option is exercised or expired.The postings for derived business transactions (if there are) at the end date of FX option are created in operative valuation area AE0 |
| [Process Dedesignation for Hedging Business Transaction at Maturity Date for Hedging Instrument](#unique_25) [page ] 52 | Treasury Specialist - Back Office | Release Hedging Business Transactions (TPM120) | Hedging Business Transaction is processed at the maturity date of hedging instrument. |
| [Reclassify Hedging Reserve and Cost of Hedging Reserve at Exposure Subitem End Date](#unique_26) [page ] 54 | Treasury Accountant | Post Derived Business Transactions (TPM18) | Reclassification postings are created and relevant flows have been fixed at the end date of exposure subitem. |
| [Display Treasury Position Flows](#unique_27) [page ] 56 | Treasury Accountant | Display Treasury Position Flows (F1754) | Position flows for FX transaction and exposure subitem are checked. |
| [Display Treasury Posting Journal](#unique_28) [page ] 57 | Treasury Accountant | Display Treasury Posting Journal (F1755) | Posting journals for FX transaction and exposure subitem are checked. |
| [Display Treasury Position Values](#unique_29) [page ] 58 | Treasury Accountant | Display Treasury Position Values (F1867) | Position values for FX transaction and exposure subitem are checked. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### FX Options as Hedging Instruments

Purpose

This section covers the Hedge Management and Hedge Accounting process for forecast cash flows in foreign currencies according to a company’s hedging policy, and the hedging instruments are FX option contracts.

The treasury department is responsible for executing a given hedging policy for hedging the risk of forecast cash flows in foreign currencies of future periods. The forecast itself is represented as exposures in the Hedge Management Cockpit. A snapshot is taken for the forecast exposures from Exposure Management. Based on the snapshot, net open exposure amount, risk currency and period are detailed in the Hedge Management Cockpit. Based on rules of the hedging policy, the net open exposures are reduced by trading financial instruments like a FX option. In case of expected inflows of a risk currency, the resulting exposure shall be closed by a plain vanilla FX option or zero/low cost collar FX option whose underlying spot transaction sells the inflow currency and buys the local currency of the company code; in case of expected outflows of risky currency, a plain vanilla FX option or zero/low cost collar FX option is traded whose underlying spot transaction buys the outflow currency and sells the local currency.

With the creating of the plain vanilla FX option contract or the reference of the two legs of zero/cost collar FX option, the financial transactions are automatically designated into a Hedging Relationship as Hedging Instrument together with the exposure item of the Hedge Management Cockpit as hedged item: The matching exposure item is determined based on characteristics of the hedging instrument, such as hedging classification, foreign currency of underlying FX spot transaction, and exercise of FX option. At the same time, the hypothetical derivative is created and all necessary mathematical evaluations necessary for the measurement of effectiveness are performed and stored.

At period end, the determination of NPVs including the decomposition of market values for hedging instrument and the hypothetical derivative is performed, and the key date valuation of the FX option transactions is executed. Meanwhile, the measurement and postings of the hedging reserve (OCI I), cost of hedging reserve (OCI II) and ineffectiveness are executed on exposure subitem level. The period end close can be executed using two different procedures: valuation and classification with Reset or without Reset. In case of zero/low cost collar FX option, the two legs which are designated into one hedging relationship are evaluated and posted separately as usual. The classification result of the hedging relationship is calculated as the sum of the component NPVs of the single leg according to the hedging relationship scenario of the hedging relationship.

At the expiry date of the FX option transaction, the FX option can be exercised or expired. The cumulated hedging reserve and cost of hedging reserve amounts are classified as frozen. At the end date of the exposure subitem, the cumulated hedging reserve and cost of hedging reserve amounts are to be reclassified to profit or loss as a reclassification adjustment.

This section can be executed using the following product type as hedging instrument:

- 76A: OTC Currency Option

|  |
| --- |
| Note Hedge accounting for FX option only supports European style FX option. |

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

In this section, as an example, one single Hedging Area HAUS02 for Hedge Accounting using FX Option is created. During testing, HAUS02 can be shared by different company codes from different countries with different local currencies.

|  |
| --- |
| Note Hedgeaing area HAUS02 is also used for testing Hedge Accounting for FX Option – Local GAAP (3X2) in US.You have the following two options to maintain hedgeing area HAUS02:Create a New Hedging Area: as the first tester to run 3X2 (US) and 3X4 test scripts, create new hedging area HAUS02;Extend an Existing Hedging Area: If you find out that the hedging area HAUS02 already exists in the system, you can create a new version of HAUS02 and extend it by entering specific parameters of your valuation area/company code/country. |

A company can have multiple Hedging Areas for Hedge Accounting according to its hedging policy. However, a hedge accounting relevant Hedging Classification can only be assigned to one Hedging Area for Hedge Accounting, therefore creating additional Hedging Area means the necessity of defining additional Hedging Classifications. Hedging Classification is a configuration which should be done via configuration step Define Hedging Classifications.

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Hedging Classifications are pre-defined for US GAAP Cash Flow Hedge of FX risk by FX Options,including plain vanilla FX option, zero/low cost collar FX option:

- YFC24: For plain vanilla FX option. Intrinsic Value of FX option is Hedging Reserve (OCI I), Time Value of FX option is Cost of Hedging Reserve (OCI II), and premium is amortized; No valuation will be carried out when releasing the designation. Prospective effectiveness test when designation is enabled. YFC24 should be always bundled with Hedging Profile S24 when maintaining the Hedge Accounting II tab of a Hedging Area.
- YFC34: For zero/low cost collar FX option (cylinder FX option). Intrinsic Value of FX option is Hedging Reserve (OCI I), Time Value of FX option is Cost of Hedging Reserve (OCI II), and premium is amortized; No valuation will be carried out when releasing the designation. Prospective effectiveness test when designation is enabled. YFC34 should be always bundled with Hedging Profile S34 when maintaining tab Hedge Accounting II of a Hedging Area.

Procedure

Option 1: Create a New Hedging Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Hedging Area (TOE_HEDGING_AREA). | The Display Hedging Area screen displays. |  |
| 3 | Enter Hedging Area ID | On the Display Hedging Area screen, enter the following data and choose the Create tab:Hedging Area: for example, HAUS02 | Dialog box Create Hedging Area displays.If message Hedging area HAUS02 already exists displays, please skip Option 1 and go to execute Option 2: Extend an Existing Hedging Area. If you find the parameters mentioned in Option 2 have been maintained, you can also skip Option 2. |  |
| 4 | Enter Data in Dialog Box Create Hedging Area | In the dialog box Create Hedging Area, enter the following data and choose the Create tab:Hedging Area: for example, HAUS02Description: for example, US GAAP Cash Flow Hedge using FX OptionAuthorization Group: for example, HAG01Valid From: for example, <first day of current year>US GAAP Cash Flow Hedge using FX Option>Without Template: <choose this radio button> | The Change Hedging Area screen displays. |  |
| 5 | Enter Data on Main Data Tab | Choose the tab Main Data, enter the following data:Local Currency: <choose this radio button>Calendar Related: <choose this radio button>Number of Periods: for example, 12Period Length: for example, MonthHedge Accounting: <choose this checkbox>Product Type for Exposure Subitems: 91ADate Exp.Itm FXOpt.: for example, US GAAP Cash Flow<Exercise Date of FX Option>Activate SAP Trading Platform Integ.: <Choose this checkbox>.You only choose this checkbox in case of testing integration with trading platform. | Data on tab Main Data has been maintained. |  |
| 6 | Enter Data on Tab General Settings | Choose the tab General Settings, and enter the following data:Company Code: for example, 3310In sub-area Differentiation Criteria: for example, select the checkbox of differentiation criterion Currency and Company CodeIn sub-area Hedging Classification:Choose Add Hedging Classification, and enter the following data:Hdg Class.DescriptionDue Date ShiftYFC24FX Risk; CFH; Vanilla; Intrinsic, Time, Amort.; w/o 1stDayReEOMN1YFC34FX Risk; CFH; Collar; Intrinsic, Time, Amort.; w/o 1stDayResEOMN1With the due date shift parameter EOMN1 (End of Next Month), the FX transaction mature in period X hedges an exposure due in period X+1, and the end date of hedged item will be the last date of period X+1. | Data on tab General Settings has been maintained. |  |
| 7 | Enter Data on Tab Currencies | Choose the Currencies tab.In the Hedging-Relevant Currencies sub-area, choose Add Currency, and enter the currencies which will be used as risk currencies in later steps in current test script. For example:USD | Data on tab Currencies has been maintained. |  |
| 8 | Enter Data on Tab Filters for Exposures | Choose the Filters for Exposures tab.In the Filter List for Exposures sub-area, choose Create Filter.In the New Filter for Exposures dialog box, enter the following data and choose Create Filter:Filter: for example, FLT_EXPFilter Description: for example, Filter for ExposuresSource: E_EM2In the Other Filter - Specific Selections sub-area, enter the following data:Exposure Position Type: YFXNoteYou may also use E_FXEM Foreign Exchange Exposure Management instead of E_EM2 Exposure Management 2.0 as the data source for exposures.If you use E_FXEM Foreign Exchange Exposure Management as the data source for exposures, you will have to use app Manage FX Exposures (F7990) instead of app Process Raw Exposure (FTREX1) to create and submit the FX Exposure. | Data on tab Filters for Exposures has been maintained. |  |
| 9 | Enter Data on Tab Filters for Hedges | Choose the Filters for Hedges tab.In the Filter List for Hedges sub-area, choose Create Filter.In the New Filter for Hedges dialog box, enter the following data and choose Create Filter:Filter: for example, FLT_HDGFilter Description: for example, Filter for HedgesSource: H_TMIn the Other Filter - Specific Selections sub-area, enter the following data:Product Type: 76A | Data on tab Filters for Hedges has been maintained. |  |
| 10 | Enter Data on Tab Hedge Accounting I | Choose the Hedge Accounting I tab.In the Designation Level sub-area, choose Insert, and enter the following data:CoCodeVADesig. LevelSplittingSequence3310003GBlank (Inactive)NIn the Designation Activation sub-area, choose Insert, and enter the following data:CoCodeVACurrencyDesig.3310003USD1(Active) | Data on tab Hedge Accounting I has been maintained. |  |
| 11 | Enter Data on Tab Hedge Accounting II | Choose the Hedge Accounting II tab.In the Designation Control sub-area， choose Insert, and enter the following data:CoCodeVAHdg Class.Des. TypePType ESIHdgProfileMDS ID3310003YFC24YFX1WS24ET023310003YFC34YFX2WS34ET02YFX1W and YFX2W are designation types that do not require counter-confirmation. There are another two designation types YFX1C and YFX2C that require counter-confirmation.When using YFX1C or YFX2C, hedging relationship can be released only after the corresponding hedging instrument is counter-confirmed, which requires Correspondence functionality. | Data on tab Hedge Accounting II has been maintained. |  |
| 12 | Save the Hedging Area | Choose Save (Ctrl+S). | Message Hedging area HAUS02 version 001 saved is displayed.The Hedging Area for Hedge Accounting has been created successfully. |  |

Option 2: Extend an Existing Hedging Area

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Define Hedging Area (TOE_HEDGING_AREA). | The Display Hedging Area screen displays. |  |
| 3 | Enter Hedging Area ID | On the Display Hedging Area screen, enter the following data and choose Display tab:Hedging Area: for example, HAUS02 | Hedging Area HAUS02 is displayed. |  |
| 4 | Create New Version | Choose New Version.In the dialog box Create New Version of Hedging Area HAUS02, enter the following data and choose Create:Valid From: for example, the given default date, or the current date | The Change Hedging Area screen displays. |  |
| 5 | Update Data on Tab General Settings | Choose the General Settings tab, choose the button Multiple selection of field Company Code.In the dialog box Multiple Selection for Company Code, add company code 1010 into the area Select Single Values, and choose Copy (F8). | Data on tab General Settings has been updated. |  |
| 6 | Update Data on Tab Currencies | Choose the tab Currencies.In sub-area Hedging-Relevant Currencies, choose Add Currency, and enter the currencies (if they have not been maintained) which will be used as risk currencies in later steps in current test script. For example:USD | Data on tab Currencies has been updated. |  |
| 7 | Update Data on Tab Hedge Accounting I | Choose the tab Hedge Accounting I.In sub-area Designation Level, choose Insert, and enter the following data:CoCodeVADesig. LevelSplittingSequence3310003GBlank (Inactive)NIn sub-area Designation Activation, choose Insert, and enter the following data:CoCodeVACurrencyDesig.3310003USD1 (Active) | Data on tab Hedge Accounting I has been updated. |  |
| 8 | Update Data on Tab Hedge Accounting II | Choose the tab Hedge Accounting II.In sub-area Designation Control, choose Insert, and enter the following data:CoCodeVAHdg Class.Des. TypePType ESIHdgProfileMDS ID3310003YFC24YFX1WS24ET023310003YFC34YFX2WS34ET02Note YFX1W and YFX2W are designation types that do not require counterconfirmation. There are another two designation types YFX1C and YFX2C that require counterconfirmation.When using YFX1C or YFX2C, hedging relationship can be released only after the corresponding hedging instrument has been successfully counterconfirmed, which requires correspondence functionality.PType ESI is to assign different product types for different exposure items classified by hedging classification. If you want to use just one product type maintained in the Main Data tab for all exposure items, please keep field PType ESI blank here. | Data on tab Hedge Accounting II has been updated. |  |
| 9 | Save the Hedging Area | Choose Save (Ctrl+S). | The Hedging area HAUS02 version XXX saved message displays.The Hedging Area for Hedge Accounting has been extended to support your company code/country testing successfully. |  |

#### Collect and Determine Exposure Data

Purpose

Middle office collects exposure data based on forecast cash flows in risk currencies from various sources, and consolidate the exposures data which should be ready to be entered SAP system as Raw Exposures. The exposure data should be aggregated in granularity which differentiates:

- Company code
- Risk currency
- The period in which exposure will be due

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

A derived exposure position is created and automatically released when a raw exposure is created and released.

This step give you an example of how to maintain raw exposure manually. You can also import Raw Exposures from spreadsheet. For details, please refer to Option 2: Import the raw exposures from spreadsheet of step Create Raw Exposure in the Foreign Currency Risk Management (1X1) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process Raw Exposure (FTREX1) | The Raw Exposure: Initial screen displays. |  |
| 3 | Enter Selection Criteria | On the Raw Exposure: Initial screen, enter the following data and choose the Create tab.Exposure Activity Type: for example, YFXIIf the direction of consolidated FX exposure is outgoing, use Exposure Activity Type YFXO. | The Raw Exposure Maintenance: Create screen displays. |  |
| 4 | Enter Header Data | On the Raw Exposure Maintenance: Create screen and under the tab Header Data, enter the following data:Default Exposure Category: for example, 01 (Forecasted Transaction)Company Code: for example, 3310Cirt4ExpPosType: FX (FX Exposure)Direction: for example, IN (Incoming Cash Flow)Cirt4ExpPosType is a criterion used to derive the Exposure Position Type YFX which you entered on tab Filters for Exposures of Hedging Area.If you use Exposure Activity Type YFXO on previous screen, please enter Direction OUT (Outgoing Cash Flow) on this screen. | Necessary header data is entered. |  |
| 5 | Enter Line Item Data | Choose the tab Line Item Data.In the sub-area Raw Exposure Line Item, choose the Create New Line Item button, and enter the following data:Exposure Due Date : for example, <Current date + 2 Months>Exposure Amount: for example, 20000000Exposure Amount Currency: for example, USDTarget Currency: for example, AED | Necessary line item data is entered. |  |
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

You take a snapshot of the exposure data belonging to specific hedging area. For the subsequent process of Hedge Management and Hedge Accounting, it is mandatory to rely on fully versioned data. This ensures that at all times an auditor can check which data served as the basis for a hedging decision.

The selected incoming or outgoing exposures and the exposure items are saved on the database, and can be reviewed in app Hedge Management Cockpit (TOENE) in next step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Take Snapshot (TOESNAP). | The Take Snapshot screen displays. |  |
| 3 | Enter General Selections | On the Take Snapshot screen, enter the following data and choose Run:Hedging Area: for example, HAUS02Description: for example, snapshot for hedge accounting using FX OptionDay Reference: <select this checkbox>Extraction Date: for example , <the current date> | The Display logs screen displays and the snapshot is created. |  |

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
| 2 | Access the SAP Fiori App | Open Hedge Management Cockpit (TOENE). | The Hedge Management Cockpit for Hedging Area screen displays. |  |
| 3 | Enter Selection Criteria | On the Hedge Management Cockpit for Hedging Area screen, enter the following data and choose Start:Hedging Area: for example, HAUS02Layout ID: for example, 1R_ALL_CHYou can also choose alternative layout IDs, or choose Manage Layouts to create new layout on next screen Layout Overview. | The Hedge Management Cockpit for Hedging Area HAUS02 displays.You can see the amounts of exposures have been reflected in specific cells for differentiation criteria of raw exposures you created previously (company code, risk currency, period of due date, incoming/outgoing indicator of Exposure Activity Type).Choose a cell, you can click Drilldown (cell) to display more detailed information of Exposure Item, Exposure Position, Raw Exposure. |  |

#### Agree on Hedging Instrument

Purpose

The middle office analyzes the exposure data for FX risk with relevant teams and organizations, and then agrees on which financial instruments should be used as hedging instruments. In the current section, plain vanilla FX option or zero/low cost collar (cylinder FX option) is used as hedging instrument.

Procedure

This step is done outside of the SAP system.

#### Check Limit Utilization Report (Optional)

Purpose

Before front office trade a financial instrument with counterparty, usually the middle office should check the limit utilization status to see if there is enough credit limit for trading new deals.

Prerequisites

Credit limits have been maintained, please see the [Business Conditions](#unique_6) [page ] 5.

Procedure

This step is optional since it is not a key process step of Hedge Accounting. For checking limit utilization, please see the step Check Limit Utilization Report in the Foreign Currency Risk Management (1X1) test script.

#### Create Foreign Exchange Contract with Hedging Classification

Purpose

In this step, you create FX option contract (plain vanilla FX option, or zero/low cost collar FX option) as hedging instruments.

The saving of the FX Transaction with a Hedge Accounting-specific Hedging Classification initiates the Hedge Accounting processing:

- According to the Contract Start Date and Hedging Classification, a valid Hedging Area is determined.
- According to the differentiating criteria (currency, company code, etc.) of the Hedging Area and by means of the Contract Start and Value Date, considering the due date shift setting, the Exposure Item of the Snapshot is determined.

Prerequisites

Business partner has been created, please refer to the [Business Conditions](#unique_6) [page ] 5 step for details.

If you used the Designation Type which requires counterconfirmation in step [Define or Adjust Hedging Area](#unique_9) [page ] 12, hedging relationship can be released only after the FX transaction has been successfully counterconfirmed, you need to run the correspondence process which will set the status of FX transaction to Counterconfirmed automatically after receiving the incoming confirmation from counterparty, and correspondence setting should be maintained for business partner before creating a FX transaction (please see the [Business Conditions](#unique_6) [page ] 5 section ).

##### Create Plain Vanilla FX Option

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create OTC Option (TI71). | The Create OTC Option: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Create OTC Option: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: 76ATransaction Type: 100Partner: for example, 33537001 | The OTC Option: Create Contract: Structure screen displays. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Sub-area Option:Expiry Date: for example, <Current date + 1 Month>Exercise Type: for example, EuropeanSettlement: for example, Physical ExerciseStrike: <Local Currency>/<Risk Currency Rate>, for example, AED/USDPut/Call: for example, PutTraded Amt: Risk Currency Amount, for example, USD 1000000Value Date: for example, <Expiry date + 1 Month + 2 Days>Spot Reference: for example,Sub-area Premium:Flow Type: for example, 1300 Option Premium - Profit/LossPayment Date: <Current date + 2 days>Amount: <local currency> <your option premium amount>, for example, AED 1000Contract Date: for example, <current date>, and must be equal to or later than the valid from date of latest version of hedging area.Because of due date shift setting in hedgeing area, the Expiry Date of FX option should be within the period before the period in which the raw exposure will due.You long put option if it is incoming exposure, you long call option if it is outgoing exposure.The currency of Traded Amt should be the risk currency. The amount of Traded Amt should be less or equal to the amount of Raw Exposure Line Item for this risk currency you created previously. | Data on tab Structure has been entered. |  |
| 5 | Enter Data in Administration tab | Choose tab Administr., and enter the following data:Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: for example, YFC24 (FX Risk; CFH; Vanilla; Intrinsic, Time, Amort.; w/o 1stDayRe)The appropriate General Valuation Class will derive the correct Position Management Procedure for Hedge Accounting in valuation area 003 for US GAAP. | Data on tab Administr. has been entered. |  |
| 6 | Save the OTC FX Option | Choose Save.The dialog box Check Run: Transaction: Display messages shows up.Please make sure the following message is displayed:Position Comp.Code:XXXX VA:XXX ValCls:0045 DN:\INTERN\XXXX has been included in valuation on key date XXXXXXXXIn the dialog box Check Run: Transaction: Display messages, choose Continue (Enter) to save the transaction.Note Note down the transaction number. |  |  |

After the plain vanilla FX option is saved, you can logon as Treasury Specialist - Middle Office and open app Hedge Management Cockpit (TOENE) to check the net open exposure again.

In app Hedge Management Cockpit (TOENE), the amounts of FX transactions will be reflected in corresponding cells for Key Figure Name Net Hedges and relevant company code, risk currency and period (e.g. next period of expiry date of option because of due date shift); Net Open Exposure should be reduced accordingly.

##### Create Zero/Low Cost Collar FX Option (Cylinder Option)

Purpose

In this step, you create a zero/low cost collar FX option (cylinder option).

There are two alternatives to manually create zero/low cost collar FX option:

- Option 1: Create Two Options Separately and Create Option Reference. You create a FX option (long leg), and create another FX option (short leg), and then create the reference for these two legs and become the zero/low cost collar FX option.
- Option 2: Create Zero/Low Cost Collar FX Option in Single Step. The two legs and the reference are saved at the same time.

No matter which option you choose, the following attributes are necessary to be identical in both FX option transactions (two legs):

- Company code
- Product type
- Business partner
- Expiry Date
- Risk currency, risk amount
- Premium payment date, premium currency
- Contract date
- Hedging classification

###### Option 1: Create Two Options Separately and Create Option Reference

Procedure

Table 1: Purchase a Put/Call FX Option (Long Leg)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create OTC Option (TI71). | The Create OTC Option: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Create OTC Option: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: 76ATransaction Type: 100Partner: for example, 33537001 | The OTC Option: Create Contract: Structure screen displays. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Sub-area Option:Expiry Date: for example, <Current date + 1 Month>Exercise Type: for example, EuropeanSettlement: for example, Physical ExerciseStrike: <Local Currency>/<Risk Currency Rate>, for example, AED/USDPut/Call: for example, PutTraded Amt: <Risk Currency><Amount>, for example, USD 2000000Value Date: for example, <Current date + 1 Month + 2 days>Spot Reference: for example,Sub-area Premium:Flow Type: for example, 1300 Option Premium - Profit/LossPayment Date: <Current date + 2 days>Amount: <local currency> <your option premium amount>, for example, AED 2000Sub-area Contract Conclusion:Contract Date: for example, <current date>, and must be equal to or later than the valid from date of latest version of hedging area.Because of due date shift setting in hedgeing area, the Expiry Date of FX option should be within the period before the period in which the raw exposure will due.You long call option in cylinder option if it is outgoing exposure.You long put option in cylinder option if it is incoming exposure.The currency of Traded Amt should be the risk currency. The amount of Traded Amt should be less or equal to the amount of Net Open Exposure. | Data on tab Structure has been entered. |  |
| 5 | Enter Data in Administration tab | Choose tab Administr., and enter the following data:Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: for example, YFC34 (FX Risk; CFH; Collar; Intrinsic, Time, Amort.; w/o 1stDayRes)The appropriate General Valuation Class will derive the correct Position Management Procedure for Hedge Accounting in valuation area 003 for US GAAP. | Data on tab Administr. has been entered. |  |
| 6 | Save the OTC FX Option (Long Leg) | Choose Save.The dialog box Check Run: Transaction: Display messages shows up.Please make sure the following message is displayed:Reprocessing of financial transaction required after saving. See longtextIn the dialog box Check Run: Transaction: Display messages, choose Continue (Enter) to save the transaction.Note Note down the transaction number. |  |  |

Table 2: Sell a Call/Put FX Option (Short Leg)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create OTC Option (TI71). | The Create OTC Option: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Create OTC Option: Initial Screen, enter the following data and choose Enter:Company Code: for example, 3310Product Type: 76ATransaction Type: 200Partner: for example, 33537001 | The OTC Option: Create Contract: Structure screen displays. |  |
| 4 | Enter Data on Tab Structure | On the tab Structure, enter the following data:Sub-area Option:Expiry Date: for example,<Current date + 1 Month>Exercise Type: for example, EuropeanSettlement: for example, Physical ExerciseStrike: Local Currency/Risk Currency Rate, for example, AED/USDPut/Call: for example, CallTraded Amt: <<Risk Currency> <Amount>, for example, USD 2000000Value Date: for example, <Current date + 1 Month + 2 days>Spot Reference: for example,Sub-area Premium:Flow Type: for example, 1300 Option Premium - Profit/LossPayment Date: <Current date + 2 days>Amount: <local currency> <your option premium amount>, for example, AED 2000Sub-area Contract Conclusion:Contract Date: for example, <current date>, and must be equal to or later than the valid from date of latest version of hedging area.Note Because of due date shift setting in hedgeing area, the Expiry Date of FX option should be within the period before the period in which the raw exposure will duYou short call option in cylinder option if it is incoming exposure.You short put option in cylinder option if it is outgoing exposure.The currency of Traded Amt should be the risk currency. The amount of Traded Amt should be less or equal to the amount of Net Open Exposure. | Data on tab Structure has been entered. |  |
| 5 | Enter Data in Administration tab | Choose tab Administr., and enter the following data:Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: for example, YFC34 (FX Risk; CFH; Collar; Intrinsic, Time, Amort.; w/o 1stDayRes)The appropriate General Valuation Class will derive the correct Position Management Procedure for Hedge Accounting in valuation area 003 for US GAAP. | Data on tab Administr. has been entered. |  |
| 6 | Save the OTC FX Option (Short Leg) | Choose Save.The dialog box Check Run: Transaction: Display messages shows up.Please make sure the following message is displayed:Reprocessing of financial transaction required after saving. See longtextIn the dialog box Check Run: Transaction: Display messages, choose Continue (Enter) to save the transaction.Note Note down the transaction number. |  |  |

Table 3: Create Option Reference

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create Reference (TBR6). | The Create Reference: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Create Reference: Initial Screen, enter the following data:Reference Category: OPTSub-area Object 1 to Be Linked:Company Code: for example, 3310Transaction: <The transaction number of the long leg>Sub-area Object 2 to Be Linked:Company Code: for example, 3310Transaction: <The transaction number of the short leg>Choose Enter. | The Create Reference: Data screen displays. |  |
| 4 | Save Reference | On the Create Reference: Data screen, choose Save, | Massage Reference number created displays. |  |

###### Option 2: Create Zero/Low Cost Collar FX Option in Single Step

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Front Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create Collar FX Option (TI4B). | The Create Option Entry - Spread: Initial Screen displays. |  |
| 3 | Enter Data on Initial Screen | On the Create Option Entry - Spread: Initial Screen, enter the following data:Company Code: for example, 3310Partner: for example, 33537001Sub-area First Transaction:Product Type: 76ATransaction: 100Sub-area Second Transaction:Product Type: 76ATransaction: 200Choose Enter. | The Currency Option Entry - Spread: Structure screen displays. |  |
| 4 | Enter Data for 1st Transaction (Long Leg) | On the Currency Option Entry - Spread: Structure screen, enter the following data in area 1st Transaction:Sub-area Option:Exercise Type: for example, EuropeanSettlement: for example, Physical ExerciseExpiry Date: for example, <Current date + 1 Month>Strike: <Local Currency>/<Risk Currency Rate>, for example, AED/USDPut/Call: for example, PutTraded Amt: <Risk Currency> <Amount>, for example, USD 2000000Value Date: for example, <Current date + 1 Month + 2 days>Spot Reference: for example,Sub-area Premium:Flow Type: for example, 1300 Option Premium - Profit/LossPayment Date: <Current date + 2 days>Amount: <local currency> <your option premium amount>, for example, AED 2000Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: for example, YFC34 (FX Risk; CFH; Collar; Intrinsic, Time, Amort.; w/o 1stDayRes)Choose Enter.Note Because of due date shift setting in hedgeing area, the Expiry Date of FX option should be within the period before the period in which the raw exposure will due.You long put option in cylinder option if it is incoming exposure,you long call option in cylinder option if it is outgoing exposure.Note The currency of Traded Amt should be the risk currency. The amount of Traded Amt should be less or equal to the amount of Net Open Exposure. | Data for 1st Transaction (long leg) has been entered. |  |
| 5 | Enter Data for 2nd Transaction (Short Leg) | Enter the following data in area 2nd Transaction:Sub-area Option:Exercise Type: <it is automatically copied from 1st transaction>Settlement: <it is automatically copied from 1st transaction>Expiry Date: <it is automatically copied from 1st transaction>Strike: currency pair is automatically copied from 1st transaction, only need to enter the exchange rate, for example,Put/Call: it is automatically derived from 1st transaction; if it is Call for 1st transaction, it should be Put for the 2nd transaction.Traded Amt: currency and amount are automatically copied from 1st transactionValue Date: <it is automatically copied from 1st transaction>Spot Reference: <it is automatically copied from 1st transaction>Sub-area Premium:Flow Type: for example, 1300 Option Premium - Profit/LossPayment Date: Current date + 2 daysAmount: <local currency> <your option premium amount>, for example, AED 2000Gen. Valn Class: for example, 45 Derivatives: Cash Flow HedgeHdg Classific.: for example, YFC34 (FX Risk; CFH; Collar; Intrinsic, Time, Amort.; w/o 1stDayRes)Choose Enter.You short call option in cylinder option if it is incoming exposure.you short put option in cylinder option if it is outgoing exposure.For both legs:The appropriate General Valuation Class will derive the correct Position Management Procedure for Hedge Accounting in valuation area 003 for US GAAP. | Data for 2nd Transaction (short leg) has been entered. |  |
| 6 | Enter Contract Conclusion Data | In sub-area Contract Conclusion, enter the following data:Contract Date: for example, <current date>, and must be equal to or later than the valid from date of latest version of hedging area. | Contract date has been entered. |  |
| 7 | Save the Cylinder Optin (Both Legs) | Choose Save. | If dialog box Document lines: Display messages displays, make sure no error message is there (otherwise please correct data and save again), and choose Continue (Enter).Message Options number 1 and number 2 created in company code company code displays.Two legs of cylinder option have been saved, the reference for them has been created.Note Note down the transaction numbers of these two legs for later use. |  |

After the zero/low cost collar FX option (cylinder FX option) is created, you can logon as Treasury Specialist - Middle Office and open app Hedge Management Cockpit (TOENE) to check the net open exposure again.

In app Hedge Management Cockpit (TOENE), the amount of long leg will be reflected in corresponding cells for Key Figure Name Net Hedges and relevant company code, risk currency and period (e.g. next period of expiry date of option because of due date shift); Net Open Exposure should be reduced accordingly.

#### Automatic Designation (Planned)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With saving the FX option transaction, the Exposure Item in a snapshot is found and the Hedging Relationship is automatically created in status Designation Planned, the Exposure Item is determined based on attributes of the relevant Snapshot and Hedging Area and FX Option transaction.

This step introduces how to check the automatically created Hedging Relationship.

For zero/low cost collar FX option (cylinder FX option), the attributes of the long leg are used for the determination of the Exposure Item of the relevant Exposure Snapshot of a valid Hedging Area version.

Procedure

Table 4: Option 1: via app Manage Hedging Relationships

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Hedging Relationships (TPM100). | The P-Hedge Accounting screen displays. |  |
| 3 | Enter Selection Criteria | On the P-Hedge Accounting screen, choose the Selection tab on the left side of screen, and enter the following data:Find: <All Hedging Relationships>By: <Hedging Instrument>Company Code: for example, 3310Valuation Area: 003Product Group: select the checkbox of OTC Trans., and choose OTC Transactions Selection beside OTC Trans.. In the OTC Transactions Selection dialog box, enter the transaction number(s) you noted down in the previous step, then choose Continue (Enter).Choose Start. | The list of Hedging Relationship Number(s) displays on bottom-left side of screen. You may need to zoom out the screen in web browser to see it.Note Note down the Hedging Relationship Number(s) |  |
| 4 | Display Header of Hedging Relationship | Double click a HR Number from bottom-left side of screen, the detailed information of Hedging Relationship will display on right side of screen.Check the data of Hedge Relationship Header. | The header of Hedging Relationship displays on upper-right side of screen, it provides details which are relevant for the Hedging Relationship as general entity.The Hedging Relationship Status should be Designation Planned since it has not been released.Choose Display All Flows, you can check the created flows resulting from the Designation.Choose Display H.Rel. Related Trans, in Hedge Related Transactions for Hedging Relationship dialog box, double click the row of Business Transaction Category Designation, then you can see the designation details in Designation of Hedging Relationship dialog box. |  |
| 5 | Display Tab Hedging Relationship Detail | Check the data of the Hedge Relationship Details tab. | The Hedging Relationship Detail tab contains information about:Risk Type and Risk Profile DetailsDate information on Hedging Relationship levelThe following fields are automatically populated:Risk Currency: your exposure currencyNote If you choose Currency Defined by the Source and exposure items are created based on the cross-currency exposures, the Target Currency is displayed in the Hedge Relationship Details.Profile: the Hedging Profile which is mapped (on tab Hedge Accounting II of Hedging Area) to the Hedging Classification you used when created FX transaction.Category: Cash Flow HedgeRisk Indicator: Currency RiskValid-From Date: contract date of FX OptionPlanned Designation Date: contract date of FX OptionPlanned Dedesign. Date: expiry date of FX OptionDesignation Type: the Designation Type which is mapped (on tab Hedge Accounting II of Hedging Area) to the Hedging Classification you used when created FX transaction |  |
| 6 | Display Tab Hedged Item | Choose tab Hedged Item, and check data of it. | The Hedged Item tab contains information about:Hedged Item DetailsPosition Management information of the Exposure SubitemThe following fields are automatically populated:Number: generated numberNote Note down this date.Start Date: contract date of FX OptionEnd Date: it is determined by the expiry date of FX option and settng of due date shift in hedging area.Note Note down this date.Category: Planned ForecastHypothetical Derivative: empty at this moment, it will be created after designation is released.Product Group: ExposuresValuation Class: determined from pre-defined configuration on Product Type levelExposure Item ID: generated number.Note Note down the Exposure Item.Exposure Subitem ID: generated number.Note Note down the Exposure Subitem ID. |  |
| 7 | Display Tab Hedging Instrument | Choose the Hedging Instrument tab, and check data of it. | The Hedging Instrument tab contains information about:Hedging Instrument DetailsPosition Management information of the Hedging InstrumentThe following fields are automatically populated:Number: generated numberNote Note down the Hedging Instrument Number.Product Group: OTC Transactions: Money Market, FX, DerivativesValuation Class: derived from pre-defined configuration and the General Valuation Class you chose when created FX transactions.Transaction Number: the FX option number you created in previous step.Start Date: Contract Date of FX OptionEnd Date: Expiry Date of FX OptionFor zero/low cost collar FX option (cylinder FX option), there are two hedging instruments, and each hedging instrument has its details. |  |

Table 5: Option 2: via app Process FX Option (Subtitle: Collective Processing)

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process OTC Options - Collective Processing (TI91). | The OTC Option: Collective Processing screen displays. |  |
| 3 | Enter Selection Criteria | On the OTC Option: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the FX Option number(s) you created in the previous step> | The list of FX transaction(s) displays in area OTC Option: Collective Processing. |  |
| 4 | Display Transaction | Select the checkbox of a transaction on OTC Option: Collective Processing, and choose Display. | The OTC Option: Display: Structure screen displays. |  |
| 5 | Display the Hedging Relationship | Choose tab Administr., choose Show Hedging Relationship.On the List of Hedging Relationships screen, select the checkbox of a Hedging Relationship, and then choose Display Hedging Rel.. | The P-Hedge Accounting screen displays, you can check detailed information of Hedging Relationship just like in app Manage Hedging Relationships (TPM100)(TPM100). |  |

If you cannot see the Hedging Relationship for your FX Option transaction via app Manage Hedging Relationships (TPM100) or Process Spots/Forwards - Collective Processing (TX06), or message Reprocessing of financial transaction required after save displays when you saved the FX Option transaction in step [Create Foreign Exchange Contract with Hedging Classification](#unique_16) [page ] 22, the system did not finish the automated designation of the financial transaction and exposure. To analyze the error situation and postprocess the financial transaction for the designation, use app Reprocess Transactions - Automated Designation (TPM104), for details please see the procedure as below:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reprocess Transactions - Automated Designation (TPM104). | The Reprocess Financial Transactions for Automated Designation screen displays. |  |
| 3 | Enter Selection Criteria | On the Reprocess Financial Transactions for Automated Designation screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 003Transaction: <the FX Option number(s) you created in the previous step> | The Transaction Numbers screen displays.If you cannot see any transaction on this screen, please skip current step because automated designation is created for the transaction(s) you selected on previous screen. |  |
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

Once a FX Option transaction is saved in system, the status of transaction needs to set as Contract Settlement before you could create postings for flows (e.g., for flow of premium), usually it is done after you receive the incoming confirmation from counterparty. You can settle the transaction via the following ways once you get counterparty confirmation:

- Option 1: Manual Settlement via app Process OTC Options - Collective Processing (TI91)
- Option 2: Automatic settlement via Correspondence Process

In this step, we only proceed Option 1 - Manual Settlement.

As described in section [Create Foreign Exchange Contract with Hedging Classification](#unique_16) [page ] 22: If you used the Designation Type which requires counterconfirmation, you need to run the correspondence process which will set the status of FX transaction to Counterconfirmed automatically after receiving the incoming confirmation from counterparty, and correspondence setting should be maintained for business partner before creating a FX transaction (please refer to the [Business Conditions](#unique_6) [page ] 5).

For details regarding how to do automatic settlement via Correspondence Process, please refer to steps described in the Correspondence with PDF Form section in the Foreign Currency Risk Management (1X1) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Process OTC Options - Collective Processing (TI91) | The OTC Options: Collective Processing screen displays. |  |
| 3 | Enter Selection Criteria | On the OTC Options: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the FX Option transaction number(s)> | The list of FX Option transaction(s) displays on OTC Options: Collective Processing screen. |  |
| 4 | Settle the Transaction | Select the checkbox of a transaction on OTC Options: Collective Processing screen, and choose Settle. | The OTC Option: Settle Contract: Structure screen displays. |  |
| 5 | Save the Change | On the OTC Option: Settle Contract: Structure screen, the value of field Activity in header is 2 - Contract Settlement.Choose Save.If dialog Document lines: Display messages displays, choose Continue (Enter). | The FX Option transaction is saved with status Contract Settlement.For zero/low cost collar FX option (cylinder FX option), please set the Contract Settlement status for both legs. |  |

#### Release Hedging Relationship

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the automated designation which is in status DesignationPlanned.. After release, the status will become Designated.

Prerequisite

Market data (FX spot rates, interest rates, FX Volatilities) for relevant currencies have been maintained in system, please see the [Business Conditions](#unique_6) [page ] 5 section. The prospective effectiveness test uses linear regression test which requires historical market data, so market data for previous periods (e.g. previous 3 months) should also be available.

If you used the Designation Type which requires counterconfirmation in the [Define or Adjust Hedging Area](#unique_9) [page ] 12 step, hedging relationship can be released only after the FX transaction has been successfully counterconfirmed. You need to run steps described in the Correspondence with PDF Form in the Foreign Currency Risk Management (1X1), the correspondence process in 1X1 will set the status of FX Option transaction to Counterconfirmed automatically after receiving the incoming confirmation from counterparty.

Note:

|  |
| --- |
| Note Open the configuration step Define Hedging Profiles, find out the hedging profiles you maintained in the Hedge Accounting II tab of hedging area HAUS02, and deselect the checkbox Documentation Optional (Yes/No) for each hedging profile, otherwise the Hedge Documentation cannot be displayed when releasing the hedging relationship. |

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

Release Hedging Relationship:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 003Up to Key Date: for example, <contract date of FX option>Transaction Selection: <select this radio button>Transaction Number:the FX Option transaction number(s)Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox>Test Run: <deselect this checkbox> | A new screen Release Hedging Business Transactions displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions screen, choose Execute. | The Hedging Relationships screen displays, and Hedging Relationship has been released without errors. |  |
| 5 | Check Market Data Calculation Details | Choose Display Market Value Calculation Details. | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays. You can see the details of the calculation of the full NPV as well as the Hedge Accounting Key Figures. The offered detail lists and analysis options are the same as the ones available in app Calculate Net Present Values (Subtitle: with CVA and DVA) which will be used when period end closing.Choose Hedge Accounting Key Figures, you can see the amounts of different components (Intrinsic Value, Time Value) of FX Option transaction and hypothetical derivative.Go back to the Hedging Relationships screen. |  |
| 6 | Check Hedging Relationship | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Hedging Relationships. | The screen P-Hedge Accounting display, and you can see Hedging Relationship Status is now Designated.Choose tab Hedged Item, you can see the field Hypothetical Derivative has been filled with a generated number. |  |
| 7 | Check Effective Test Result | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Effectiveness Test. | Details of prospective effectiveness test when designation shows up.The prospective effectiveness test may lead to some errors which stop releasing of hedging relationship:The effectiveness test has been executed, but it turned out that the hedging relationship is ineffective.Effectiveness could not be completely executed, e.g. due to missing historical market data for some of the market data selection dates derived from the market data set. In that case please choose Market Value Calculation Details to check the Error Log. |  |
| 8 | Display Hedge Documentation | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Hedge Documentation. | The Hedging Relationship Documentation in PDF format will be opened. |  |

Table 6: (Optional) Reverse Release of Hedging Relationship:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Release of Hedging Business Transactions (TPM121). | The Reverse Release of Hedging Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria | On the Reverse Release of Hedging Business Transactions screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 003Date to be Reversed: for example, <the contact date of transaction>Transaction Selection: <select this radio button>Transaction Number:the FX Option transaction number(s)Reversal Reason: for example, 04Enter Rev.Date: <select this checkbox>Test Run: <deselect this checkbox>On the next screen Reverse Hedging Business Transactions, choose Execute. | The Hedging Relationships screen displays, and Release of Hedging Relationship has been reversed without errors. |  |
| 4 | Check Hedging Relationship | Select the checkbox of a HR Number, and choose Display Hedging Relationship. | The screen P-Hedge Accounting display, and you can see Hedging Relationship Status is returned to Planned Designation. |  |
| 5 | Release Hedging Relationship Again | Open app Release Hedging Business Transactions (TPM120), and release the Hedging Relationship again (follow introductions in Release Hedging Relationship), otherwise you will not be able to continue the testing. | Hedging Relationship is released again. |  |

#### Process Premium Payment

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you run steps for premium payment and postings.

Procedure

Perform the following steps in the Foreign Currency Risk Management test script, under Foreign Currency Risk Management and Accounting - Vanilla Options > Premium Payment for the FX option transactions you created in step [Create Foreign Exchange Contract with Hedging Classification](#unique_16) [page ] 22

| Step Name in 1X1 | Mandatory/Optional for Continuing Testing 3X4 | Purpose |
| --- | --- | --- |
| Generate Payment Request for Mature Transaction | Mandatory | Generate payment request for payment of premium at its payment date via app Fix, Pay and Post Flows (TBB1). |
| Process Payment Request | Optional | Process the payment run procedure for payment request and create posting for premium payment via app Automatic Payment Transactions for Payment Requests (F111). |
| Post to General Ledger | Mandatory | Generate posting for premium payment (outgoing payment) in valuation area AE0 (local GAAP) via app Process Business Transactions (TPM10). |

Perform the following step in test script Foreign Currency Risk Management – Group Ledger US GAAP (34D) for the FX option transactions you created in step [Create Foreign Exchange Contract with Hedging Classification](#unique_16) [page ] 22:

| Step Name in 34D | Mandatory/Optional for Continuing Testing 3X4 | Purpose |
| --- | --- | --- |
| Post Flows to General Ledger (Parallel Valuation Area) | Mandatory | Generate posting for premium payment (outgoing payment) in valuation area 003 (US GAAP) via app Process Business Transactions (TPM10). |

|  |
| --- |
| Note If it is zero/low cost collar FX option (cylinder FX option), please perform steps mentioned above for both legs. |

#### Period End Closing

This test script only introduces the period end closing activities of valuation area 003 (US GAAP Hedge Accounting).

For period end closing activities for FX Option transactions in valuation area AE0 (local GAAP) without hedge accounting, please see test script Foreign Currency Risk Management under Foreign Currency Risk Management and Accounting - Vanilla Options > Period end has been reached .

##### Calculate NPV of Hedging Instrument and Hypothetical Derivative

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you calculate the Net Present Values (Fair Values) of FX Option transactions and corresponding Hypothetical Derivatives at period end, system also calculates market value components (Intrinsic Value, Time Value) for FX Option transactions and corresponding Hypothetical Derivatives.

Prerequisite

Market data (FX spot rates, interest rates, FX Volatilities) for relevant currencies have been maintained in system and valid at period end, please see section [Business Conditions](#unique_6) [page ] 5.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Calculate Net Present Values - With CVA and DVA (TPM60CVA). | The Determine NPVs Including Credit and Debit Value Adjustments screen displays. |  |
| 3 | Enter Selection Criteria and Execute | On the Determine NPVs Including Credit and Debit Value Adjustments screen, enter the following data:Sub-area Selection Mode:Evaluation Parameter Derivatn: <select this checkbox>Select OTC Transactions: <select this checkbox>Market Value Decomposition: <select this checkbox>Sub-area Common Selection Criteria:Company Code: for example, 3310Valuation Area: for example, 003Sub-area OTC Transaction Selection Criteria:Transaction: <the FX Option transaction number(s)>Note For zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs.Sub-area Evaluation Parameters:Evaluation Date: for example, last date of current monthSub-area Save Results:Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detail Log: <select this checkbox>Choose Execute. | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays.You can see the NPV of each transaction on this screen.You can also check different information by clicking on buttons:Single Transaction:Hedge Accounting Key FiguresDetailed LogCalculation BasesError LogHedge Accounting Key Figures provides a list showing the detailed amount information of market value components (Intrinsic Value, Time Value) for FX Option transactions and corresponding Hypothetical Derivatives. |  |

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
| 3 | Enter Selection Criteria for Test Run | On the Run valuation screen, enter the following data:Sub-area Product Groups:Securities: <unselect this checkbox>OTC Transactions: <select this checkbox>Sub-area General Selections:Company Code: for example, 3310Valuation Area: for example, 003Sub-area OTC Transactions:Transaction: <the FX Option transaction number(s)>Note For zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs.Sub-area Valuation Parameters:Key Date for Valuation: for example, last date of current monthValuation Category: for example, Mid-year Valuation without ResetNote You can also use Mid-year Valuation with Reset. In addition to the valuation flows, reset flows will be generated for the day following the valuation key date (usually reset flows will be posted at the first date of next month). You can therefore see the effects of the valuation only on the valuation key date.Sub-area Posting Control:Test Run: <select this checkbox>Choose Run. | The Display Selected Treasury Positions for Valuation screen displays. |  |
| 4 | Execute Valuation for Test Run | On the Display Selected Treasury Positions for Valuation screen, choose Run valuation.If dialog Message shows up, choose Continue. | The screen Valuation Log displays, if red traffic light exist, click on it and check the error message, solve the issue and perform test run again until there is no error.You can check the simulated Posting Log for US GAAP (valuation area 003) by choosing Logs + Messages, the offsetting account for fair value change of FX transaction is a Technical Clearing Account. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Run:Test Run: <deselect this checkbox> | The Display Selected Treasury Positions for Valuation screen displays. |  |
| 6 | Execute Valuation for Production Run | On the Display Selected Treasury Positions for Valuation screen, choose Run valuation. | The screen Valuation Log displays, you can check the Posting Log for US GAAP (valuation area 003) by choosing Logs + Messages, this time, accounting documents have been created for US GAAP (valuation area 003). |  |

(Optional) Reverse Valuation:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Valuation (TPM2). | The Reverse Valuation(TPM2) screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Reverse Valuation screen, enter the following data:Sub-area Product Groups:OTC Transactions: <select this checkbox>Sub-area General Selections:Company Code: for example, 3310Valuation Area: for example, 003Sub-area OTC Transactions:Transaction: <the FX Option transaction number(s)>Note For zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs.Sub-area Valuation Parameters:Key Date for Valuation: for example, last date of current month, same as the date you ran valuationSub-area Posting Control:Reason for Reversal: for example, 04Test Run: <select this checkbox>Update Derived Bus. Trans: Use System SettingsChoose Run. | The Display Positions to Be Reversed screen displays. |  |
| 4 | Execute Reversal for Test Run | On the Display Positions to Be Reversed screen, choose Reverse Valuation. | If dialog Information Overview shows up, choose Reversal Log.The screen Reversal Log: Reversed Business Transactions displays, you can check the simulated reversal valuation postings for US GAAP (valuation area 003). |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until initial screen of this app.On the initial screen, change the following data and choose Run:Test Run: <deselect this checkbox> | The Display Positions to Be Reversed screen displays. |  |
| 6 | Execute Reversal for Production Run | On the Display Positions to Be Reversed screen, choose Reverse Valuation. | If dialog Information Overview shows up, choose Reversal Log.The screen Reversal Log: Reversed Business Transactions displays, you can check the reversal valuation postings for US GAAP (valuation area 003), accounting document has been created. |  |
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

Prerequisite

Valuation for FX transactions (hedging instruments) has been executed at period end.

Procedure

Run Classification:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Classification (TPM101). | The Execute Classification screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Execute Classification screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 003Key Date for Classification: for example, <last date of current month>Transaction Selection: <select this radio button>Transaction Number:<the FX Option transaction number(s)>Note For zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs.Test Run: <select this checkbox> | Dialog box Information Overview displays. |  |
| 4 | Check Classification Log | In the dialog box Information Overview, choose Hedge Management. | The Information Overview screen displays, you can check the Classification Log on this screen. |  |
| 5 | Check Posting Log | Choose Back.In the dialog box Information Overview, choose Posting Log. | The Posting Log: Posted Business Transactions screen displays.You can check the simulated Classification postings for US GAAP (valuation area 003) on this screen, the offsetting account for OCI I, OCI II, P/L Ineffective is also the Technical Clearing Account. |  |
| 6 | Execute Valuation for Production Run | Choose Back, and choose Close in the dialog box Information Overview.On the initial screen of app Run Classification (TPM101), change the following data and choose Execute:Test Run: <deselect this checkbox> | The Information Overview screen displays again.The Classification postings have been created for US GAAP (valuation area 003), you can chick Posting Log to check the postings. |  |

(Optional) Reverse Classification:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Reverse Classification (TPM102). | The Reverse Classification(TPM102) screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Reverse Classification screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 003Key Date for Classification: for example, last date of current monthTransaction Selection: <select this radio button>Transaction Number:<the FX Option transaction number(s)>Note For zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs.Reason for Reversal: for example, 04Test Run: <select this checkbox> | Dialog box Information Overview displays. |  |
| 4 | Check Reversal Log | In the dialog box Information Overview, choose Reversal Log. | The screen Reversal Log: Reversed Business Transactions displays, you can check the simulated reversal postings of classification for US GAAP (valuation area 003). |  |
| 5 | Execute Reversal for Production Run | Choose Back, and choose Close in the dialog box Information Overview.On the initial screen of app Reverse Classification (TPM102), change the following data and choose Execute:Test Run: <deselect this checkbox> | The Information Overview screen displays again.The reversal postings of classification have been created for US GAAP (valuation area 003), you can chick Reversal Log to check the postings. |  |
| 6 | Run Classification Again | Open app Run Classification (TPM101), and create the postings for Classification again (follow introductions in Run Classification), otherwise you will not be able to continue the testing. | Classification is executed again. |  |

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

When the FX Option is reaching its expiry date, the exercising or expiration process steps for FX Option (which is a Hedging Instrument in Hedging Relationship) should be same as a normal FX Option (which is not in a Hedging Relationship), relevant process steps are described in test scripts (1X1) – Foreign Currency Risk Management and (34D) – Foreign Currency Risk Management – Group Ledger US GAAP.

Procedure

Perform the following steps in test script Foreign Currency Risk Management (1X1) under Foreign Currency Risk Management and Accounting - Vanilla Options > Transaction is Mature for the FX option transactions you created in step [Create Foreign Exchange Contract with Hedging Classification](#unique_16) [page ] 22:

| Step Name in 1X1 | Mandatory/Optional for Continuing Testing 3X4 | Purpose |
| --- | --- | --- |
| Check FX Options Collective Processing Report -> Decide to Exercise | Mandatory | You can choose to either excise or expire the FX option.If you decide to excise the FX option, run this step. |
| Check FX Options Collective Processing Report -> Create FX Spot Contract | Mandatory | You can choose to either excise or expire the FX option.If you decide to excise the FX option, run this step to create the underlying FX spot contract. |
| Check FX Options Collective Processing Report -> Decide to Expire | Mandatory | You can choose to either excise or expire the FX option.If you decide to expire the FX option, run this step. |
| Post Realized Profit and Loss | Optional | Post derived business transactions (if there are) for the OTC FX option at its Expiry Date in valuation area AE0 (local GAAP) via app Post Derived Business Transactions (TPM18). |

Perform the following step in test script Foreign Currency Risk Management – Group Ledger US GAAP (34D) for the FX option transactions you created in step [Create Foreign Exchange Contract with Hedging Classification](#unique_16) [page ] 22:

| Step Name in 34D | Mandatory/Optional for Continuing Testing 3X4 | Purpose |
| --- | --- | --- |
| Post Flows to General Ledger (Parallel Valuation Area) | Optional | Post derived business transactions (if there are) for the OTC FX option at its Expiry Date in valuation area 003 (US GAAP) via app Post Derived Business Transactions (TPM18). |

If it is zero/low cost collar FX option (cylinder FX option), please perform steps mentioned above for both legs.

If the long leg is in-the-money when maturity, usually the company will exercise the long leg and counterparty will expire the short leg.

If the long leg is out-of-the-money when maturity, usually the company will expire the long leg and counterparty will exercise the short leg.

##### Process Dedesignation for Hedging Business Transaction at Maturity Date for Hedging Instrument

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

At the maturity date (expiry date) of FX Option transaction, you run the app Release Hedging Business Transactions (TPM120), the following activities are done by this app:

- Calculation and saving of NPV of FX Transaction
- Calculation and saving of NPV component values for FX Transaction and Hypothetical Derivative
- Posting of key date valuation of the designated portion of the FX Transaction with actual NPV values
- Posting of classification of the selected Hedging Relationship with actual NPV component values
- Transfer Position Amounts from Designated to Free Standing Subposition
- Update amounts of Reclassification Update Types
- Fix scheduled Dedesignation Updated Types

Prerequisite

Market data (FX spot rates, interest rates, FX Volatilities) for relevant currencies have been maintained in system, please see section Business Conditions. And market date should be valid at the expiry date of FX Option transaction.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria | On the Release Hedging Business Transactions screen, enter the following data and choose Execute:Company Code: for example, 3310Valuation Area: for example, 003Up to Key Date: for example, <the Expiry Date of FX Option transaction(s)>Transaction Selection: <select this radio button>Transaction Number: the FX Option transaction number(s)Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions(TPM120) displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions(TPM120) screen, choose Execute. | The Hedging Relationships screen displays, and Hedging Relationship has been processed for designation without errors. |  |
| 5 | Display Log of Hedge Management | On the Hedging Relationships screen, select the checkbox of a HR Number, choose Display Log.In the Information Overview dialog box, choose Hedge Management. | The Information Overview screen displays, you can check the Classification Log on this screen. |  |
| 6 | Display Log of Posting | Choose Back.In the Information Overview dialog box, choose Posting Log. | The Posting Log: Posted Business Transactions screen displays, you can check the postings on this screen. |  |

Use app Post Derived Business Transactions (TPM18) to fix the derived business transactions for FX transaction at contract close date:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log on | Log onto the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2. | Access another SAP Fiori app | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3. | Enter Selection Criteria for Test Run | On the Fix and Post Derived Business Transactions screen, enter the following data:Sub-area Product Groups:OTC Transactions: <select this checkbox>Exposure Items: <deselect this checkbox>Sub-area General Selections:Company code: for example, 3310Valuation Area: for example, 003Sub-area Selections for Fixing Derived Business Transactions:TRL Date: <the Expiry Date of FX Option transaction(s)>For zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs.Sub-area Posting Control:Test Run: <select this checkbox>Choose Execute.If message No scheduled derived business transactions were found for the selection displays, then there is no derived transaction available for your selection, you can skip current step.If message Are you sure that you want to select future business transactions? displays, press Enter | The FX Transaction(s) to be fixed and posted (test run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 4. | Fix and Post for Test run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the simulated postings. |  |
| 5. | Enter Selection Criteria for Production Run | Choose Back until the initial screen of this app.Change the following data and choose Execute:Test Run: <deselect this checkbox>If message Are you sure that you want to select future business transactions? displays, press Enter | The FX Transaction(s) to be fixed and posted (production run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 6. | Fix and Post for Production run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the postings for US GAAP (valuation area 003), accounting document has been created in corresponding ledger in Financial Accounting. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post Derived Business Transactions (TPM18). | The Fix and Post Derived Business Transactions screen displays. |  |
| 3 | Enter Selection Criteria for Test Run | On the Fix and Post Derived Business Transactions screen, enter the following data:Sub-area Product Groups:OTC Transactions: <deselect this checkbox>Exposure Items: <select this checkbox>Sub-area General Selections:Company Code: for example, 3310Valuation Area: for example, 003Sub-area Selections for Fixing Derived Business Transactions:TRL Date: <the end date of hedged item which you noted down in step Automatic Designation (Planned)>Sub-area Exposure Items:Transaction Number: the FX Option transaction number(s)Note For zero/low cost collar FX option (cylinder FX option), enter the transaction numbers of both legs.Sub-area Posting Control:Test Run: <select this checkbox>Choose Execute.If message Are you sure that you want to select future business transactions? displays, press Enter | The Exposure Subitem(s) to be fixed and posted (test run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 4 | Fix and Post for Test Run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the simulated reclassification postings of Hedging Reserve and Cost of Hedging Reserve for US GAAP (valuation area 003). |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the initial screen of this app.Change the following data and choose Execute:Test Run: <deselect this checkbox>If message Are you sure that you want to select future business transactions? displays, press Enter | The Exposure Subitem(s) to be fixed and posted (production run) is displayed in area Positions with Derived Business Transactions to Be Fixed. |  |
| 6 | Fix and Post for Production Run | Choose Fix. | If dialog box Information Overview display, choose Posting Log.New screen Posting Log: Posted Business Transactions displays, you can see the postings for US GAAP (valuation area 003), accounting document has been created in corresponding ledger in Financial Accounting. |  |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Treasury Position Flows (F1754). | The Display Treasury Position Flows screen displays. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Position Flows screen, enter the following data and choose Go:Product Group: <select OTC Transactions> and Exposure ItemsCompany Code: for example, 3310Valuation Area: for example, 003For displaying position flows on OTC transaction level, enter:Transaction: <The FX Option transaction number(s)>For displaying position flows on Exposure Subitem level, enter:Exposure Item ID: <The Exposure Item ID you noted down in step Automatic Designation (Planned)>Exposure Subitem ID: <The Exposure Subitem ID you noted down in step Automatic Designation (Planned)>If the selection criteria Transaction, Exposure Item ID, Exposure Subitem ID do not exist on the screen, choose Adapt Filters, and then choose the fields Exposure Item ID, Exposure Subitem ID from the sub-area Exposure Items, and choose Transaction from the sub-area OTC Transactions in the Adapt Filters dialog box. | All relevant position flows of FX transaction and Exposure Subitems are displayed in area Position Flows.If you would like to see transaction ID, exposure item ID, exposure subitem ID in area Position Flows, please choose Settings to change the layout. |  |

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
| 2 | Access the SAP Fiori App | Open Display Treasury Posting Journal (F1755). | The Display Treasury Posting Journal screen displays. |  |
| 3 | Enter Selection Criteria | On the Display Treasury Posting Journal screen, enter the following data and choose Go:Product Group: <select OTC TransactionsExposure Items>Company Code: for example, 3310Valuation Area: for example, 003For displaying posting journal on OTC transaction level, enter:Transaction: <The FX Option transaction number(s)>Or for displaying posting journal on Exposure Subitem level, enter:Exposure Item ID: <The Exposure Item ID you noted down in step Automatic Designation (Planned)>Exposure Subitem ID: <The Exposure Subitem ID you noted down in step Automatic Designation (Planned)>If the selection criteria Transaction, Exposure Item ID, Exposure Subitem ID do not exist on the screen, choose Adapt Filters, and then choose the fields Exposure Item ID, Exposure Subitem ID from the sub-area Exposure Items, and choose Transaction from the sub-area OTC Transactions in the Adapt Filters dialog box. | All relevant posting journal line items are displayed in area Line Items, you can see the line items on FX transaction level or Exposure subitem level.If you would like to see transaction ID, exposure item ID, exposure subitem ID in area Position Flows, please choose Settings to change the layout. |  |

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

With the reduction of a planned cash flow of an exposure period an overhedge situation occurs (e.g. partial volume of the hedged item that is a forecast transaction is no longer highly probable). A Hedge Request type Dedesignation allows to dedesignate the Hedging Relationship to solve the overhedge situation.

Depending on the selected type of Reclassification Handling, the reclassification of the Hedging Reserve and Cost of Hedging Reserve amounts is posted immediately with the release of the Hedging Business Transaction or at the Exposure Item End Date.

Prerequisite

The following steps under section [FX Options as Hedging Instruments](#unique_31) [page ] 11 have been executed:

- [Define or Adjust Hedging Area](#unique_9) [page ] 12
- [Create Raw Exposure](#unique_11) [page ] 18
- [Take Snapshot](#unique_12) [page ] 20
- [Create Plain Vanilla FX Option](#unique_32) [page ] 23, or [Create Zero/Low Cost Collar FX Option (Cylinder Option)](#unique_33) [page ] 25

|  |
| --- |
| Note Note down the FX Option Transaction Number(s), and the Expiry Date of FX Option Transaction |

- [Automatic Designation (Planned)](#unique_17) [page ] 32

|  |
| --- |
| Note Note down the Hedging Relationship Number (HR Number). |

- [Set Contract Settlement Status with Incoming Confirmation](#unique_18) [page ] 37
- [Release Hedging Relationship](#unique_19) [page ] 38

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

A new Raw Exposure is created as an exposure position to simulate an over-hedge situation in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Middle Office | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Raw Exposure (FTREX1). | The Raw Exposure: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | On the Raw Exposure: Initial Screen, enter the following data and choose Create.Exposure Activity Type: for example, YFXI | The Raw Exposure Maintenance: Create screen displays. |  |
| 4 | Enter Header Data | On the Raw Exposure Maintenance: Create screen and tab Header Data, enter the following data:Default Exposure Category: for example, 01(Forecasted Transaction)Company Code: for example, 3310Cirt4ExpPosType: FX (FX Exposure)Direction: for example, IN(Incoming Cash Flow) | Necessary header data is entered. |  |
| 5 | Enter Line Item Data | Choose tab Line Item Data.In sub-area Raw Exposure Line Item, choose Create New Line Item, and enter the following data:Due Date: for example, <Current date + 2 Months>Exposure Amount: for example, -500000Exposure Amount Currency: for example, USDTarget Currency: for example, AED | Necessary line item data is entered. |  |
| 6 | Save Raw Exposure | Choose Save. | A dialog box displays, and states that:Raw exposure has been saved;Raw exposure has been released;Position IDs have been updated.You can check exposure position and exposure position flows via app Process Exposure Positions (FTREX12) and Display Exposure Position Flows (FTREX13)In the example, after the raw exposure is created, the incoming exposure in a specific period will be 500000 less than the initial estimated exposure data. |  |

#### Take Snapshot

Purpose

Take a new snapshot to reflect reduction of exposure for overhedge situation.

Procedure

Execute step [Take Snapshot](#unique_12) [page ] 20 under section [FX Options as Hedging Instruments](#unique_31) [page ] 11.

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
| 3. | Enter Selection Criteria | On the Hedge Management Cockpit for Hedging Area screen, enter the following data and choose Start:Hedging Area: for example: HAUS02Layout ID: for example, 1R_ALL_CH | The Hedge Management Cockpit for Hedging Area HAUS02 displays.You can see the amount of exposure have been reduced in the cell for relevant period (for example, current month + two months) and risk currency (for example, USD in accordance to the new raw exposure you just created. |  |
| 4. | Create Dedesignation Request | Choose a cell for relevant period and risk currency in accordance to the new raw exposure you just created.Choose Hedge Request > Dedesignation Request. | The Hedge Request screen displays. |  |
| 5. | Enter and Check Date for Dedesignation Request | On the Hedge Request screen, enter the following data:Header:Description (the field beside field Hedge Request ID): any textTab General:Hedge Req. Reason: S001Dedes.Date: <the date in the period targeting the adjusted exposure, and the due date shift should be considered as well; it must be earlier than the expiry date of the FX Option Transaction you created in the Prerequisites section of Overhedge Processing - Dedesignation>, for example, <10th of next month>Hedge Request Volume: <the reduced exposure amount>, for example, 500000Tab Hedging Relationships:Valuation Area: 003Reclass. Handling: for example, Immediate ReclassificationSelect the checkbox Requested for the row with the Transaction Number and HR Number you noted down when executing the steps mentioned in the Prerequisites section of Overhedge Processing - Dedesignation. For Cylinder FX Option, only the transaction number of this long leg can be selected.Request Volume (of the row you selected): <the reduced exposure amount>, for example,500000Sequence: for example, 1Choose Check.Two options of Reclass. Handling:Immediate Reclassification: the OCI I, OCI II of dedesignated portion is reclassified immediately with release of the Hedging Business Transaction.Planned Reclassification: the OCI I, OCI II of dedesignated portion will be reclassified at the end date of exposure subitem. | Message Hedge Request is consistent displays, means the data you entered is OK, otherwise please check your data until this message displays. |  |
| 6. | Submit Designation Request | Choose Submit. | Message Hedge Request number was saved displays.Note Note down the Hedge Request ID |  |

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
| 2. | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO). | The Process Hedge Requests screen displays. |  |
| 3. | Enter Selection Criteria and Start Search | On the Process Hedge Requests screen, enter the following data:Hedging Area: for example, HAUS02Submitted (in subarea Status): <make sure this checkbox has been selected>Choose Start. | A list of hedge requests displays, your dedesignation request is in this list, its status is Submitted. |  |
| 4. | Release Designation Request | Choose the Hedge Request ID of the dedesignation request you created, and choose Process > Release.If dialog box appears and stats that Data was Cahnged. Do you want to Save?, choose Yes. | The designation request's status becomes Released. |  |

A Released dedesignation request can be withdrawn. To withdraw a dedesignation request, please execute the following steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO). | The Process Hedge Requests screen displays. |  |
| 3 | Enter Selection Criteria and Start Search | On the Process Hedge Requests screen, enter the following data:Hedging Area: for example, HAUS02Released (in subarea Status): <make sure this checkbox has been selected>Choose Start. | A list of hedge requests displays, your dedesignation request is in this list, its status is Released. |  |
| 4 | Withdraw Dedesignation Request | Choose the Hedge Request ID of the dedesignation request you released, and choose Process > Withdraw. | Dialog box displays and states that Hedge Request withdrawn. |  |

|  |
| --- |
| Note A withdrawn dedesignation request cannot be released again, please recreate and resubmit a new designation to continue testing.If the dedesignation business transaction has been released (means next step [Process Dedesignation for Hedging Business Transaction](#unique_42) [page ] 66 has been executed), the dedesignation request cannot be withdrawn unless you reverse the release of the dedesignation business transaction via app Reverse Release of Hedging Business Transactions (TPM121) |

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

- Calculation and saving of NPV of FX Option transaction
- Calculation and saving of NPV component values (intrinsic value, time value) for FX Option transaction and hypothetical derivative
- Execution and posting of the key date valuation of the FX Option transaction to be dedesignated with actual NPV values
- Execution and posting of the classification of the selected Hedging Relationship with actual NPV component values
- Update amounts of flows of dedesignation update types
- Fix update types of planned dedesignation flows
- Fix and post update types of reclassification flows (if chose 'Immediate Reclassification' in hedge request)

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad displays. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions screen displays. |  |
| 3 | Release Hedging Business Transaction | On the Release Hedging Business Transactions screen, enter the following data:Company code: for example, 3310Valuation Area: for example, 003Up to Key Date: for example, <the dedesignation date you specified in the Dedesignation Request>Transaction Selection: <select this radio button>Transaction Number:<the FX Option transaction number>Note For Cylinder Option, you can enter transaction number of either long leg or short leg.Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox>Choose Execute. | A new screen Release Hedging Business Transactions displays. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions screen, choose Execute. | The Hedging Relationships screen displays, and Hedging Relationship has been processed without errors. |  |
| 5 | Check Market Data Calculation Details | Choose Display Market Value Calculation Details. | The NPVs including CVA/DVA from the Market Risk Analyzer screen displays. You can see the details of the calculation of the full NPV as well as the Hedge Accounting Key Figures.Go back to the Hedging Relationships screen. |  |
| 6 | Check Log and Message | On the Hedging Relationships screen, select the checkbox of a HR Number, and select Display Log. | Dialog box Information Overview displays, you can check:Hedge management logPosting logMessages |  |

|  |
| --- |
| Note If you check the relevant hedging relationship in app Manage Hedging Relationships (TPM100) and change the display date to the dedesigantion date, you will find the designated amount of Hedged Item and Hedging Instrument has been reduced. |

### Termination of Hedging Instrument

Purpose

The termination of hedging instrument (plain vanilla FX option, zero/low cost collar FX option) leads to the discontinuation of hedge accounting.

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

In some cases, for example, you may need to terminate a hedging instrument for some reason, for example, if a long-run plain vanilla FX option or zero/low cost collar FX option is over-hedged.

After aligning with your counterpart, you decide to terminate the hedging instrument. You start the termination process via termination request in hedge management cockpit. In this step, you select the hedging instrument in the hedge management cockpit to create and submit a termination request. The request needs to be released after it is submitted.

Prerequisites

1. You have created an FX option as hedging instrument, and its status is set to Contract Settlement.
2. You have created a hedging relationship and released the designation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Middle Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Hedge Management Cockpit (TOENE) |  |  |
| 3 | Enter Selection Criteria | Make the following entries, and choose Start:Hedging Area: For example, HAUS02Layout ID: 2R_TQ_CH | The Hedge Management Cockpit for Hedging Area HAUS02 is displayed with Net Hedges |  |
| 4 | Create Termination Request | Double click on key figure Net Hedges in the period of the value date of the forward transaction you just created as prerequisite.Select the transaction you just created, click Hedge Request and choose Termination Request in the dropdown list | The Create Hedge Request screen is displayed. |  |
| 5 | Submit Termination Request | Enter description for edge request: terminate forwardEnter the following data on the General tab, and choose Submit:Hedge Request Reason: Choose S003 Overhedge Processing - TerminationNote Overruling not allowed | Terminate Request is submitted with termination request ID.Remember Note down the ID. |  |
| 6 | Access the SAP Fiori app | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start:Hedging Area: for example, HAUS02 | Hedge requests that match the filter criteria are displayed. |  |
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

After the termination request released, you terminate a plain vanilla option, or one leg of the zero/low cost collar FX option. In case that both legs of a zero/low cost collar FX option should be terminated, terminate them one by one.

Once terminates the hedging instrument, the termination request is set to Completed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Front Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Process OTC Options - Collective Processing (TI91). | The OTC Options: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the OTC Options: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the FX option transaction number to be terminated> | The list of FX Option transaction(s) is displayed on the OTC Options: Collective Processing screen. |  |
| 4 | Terminate the Transaction | On the OTC Options: Collective Processing screen, select the checkbox of the transaction to be terminated, and then choose Give Notice. | The Terminate OTC Option: Structure screen is displayed. |  |
| 5 | Save the Termination | On the Terminate OTC Option: Structure screen, the value of the Activity field in header is 3 - Termination.Enter the following data in the Termination sub-area, and choose Save:Term.Date: <the termination data, it should be a date between contract date and Expiry date>Payment Date: for example, <termination data + 2 days>Amount: for example, -100If the Document lines: Display messages dialogue is displayed, choose Continue (Enter). | The transaction is saved with status Termination. |  |
| 6 | Access the SAP Fiori App | Open Process Hedge Requests (TOEHREQO) | The Process Hedge Requests screen is displayed. |  |
| 7 | Enter Selection Criteria | Enter the following data, and choose Start.:Hedging Area: for example, HAUS02 | hedge requests that match the filter criteria are displayed. |  |
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

After you terminate an FX option transaction, you need to set its status to Termination Settlement before you could create postings for termination flow. Usually it is done after you receive the incoming confirmation about termination from your counterparty.

In this step, you settle the termination for a plain vanilla option, or one leg of the zero/low cost collar FX option. In case that both legs of zero/low cost collar FX option should be terminated, settle their termination one by one.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. |  |  |
| 2 | Access the SAP Fiori app | Open Process OTC Options - Collective Processing (TI91). | The OTC Options: Collective Processing screen is displayed. |  |
| 3 | Enter Selection Criteria | On the OTC Options: Collective Processing screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the FX option transaction number in status Termination> | The list of FX Option transaction(s) is displayed on the OTC Options: Collective Processing screen. |  |
| 4 | Settle the Termination | On the OTC Options: Collective Processing screen, select the checkbox of the transaction to be settled, and then choose Settle. | The OTC Option: Settle Termination: Structure screen is displayed. |  |
| 5 | Save the Termination Settlement | On the OTC Option: Settle Termination: Structure screen, the value of field Activity in header is 4 - Termination Settlement.Choose Save.If the Document lines: Display messages dialogue is displayed, choose Continue (Enter). | The transaction is saved with status Termination Settlement. |  |

#### Process Dedesignation for Hedging Business Transaction at Termination Date

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you release the hedging business transaction on the termination date. During this process, the hedging relationship is dedesignated, and the following activities are done with the processing of hedging business transaction at the termination date:

- Calculation and saving of NPV of FX option transaction(s)
- Calculation and saving of NPV component values (Intrinsic Value, Time Value) for FX option transaction(s) and hypothetical derivative
- Execution and posting of the key date valuation of the FX option transaction(s) to be terminated with up-to-date NPV values
- Execution and posting of the classification of the Hedging Relationship with up-to-date NPV component values
- Fix and update other relevant position flows.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access another SAP Fiori app | Open Release Hedging Business Transactions (TPM120). | The Release Hedging Business Transactions screen is displayed. |  |
| 3 | Release Hedging Business Transaction | On the Release Hedging Business Transactions screen, enter the following data, and choose Execute:Company Code: for example, 3310Valuation Area: for example, 003Up to Key Date: for example, <the termination date>Transaction Selection: <select this radio button>Transaction Number: <the FX option transaction number(s) terminated>Test Run: <deselect this checkbox>Save Values with Warnings: <select this checkbox>Detailed Log (Market Val. Calc): <select this checkbox>Enter Posting Date: <select this checkbox> | A new screen Release Hedging Business Transactions is displayed. |  |
| 4 | Choose Hedging Relationship and Execute | On the Release Hedging Business Transactions screen, choose Execute. | The Hedging Relationships screen is displayed, and the Hedging Relationship has been processed for termination of hedging instrument without errors. |  |

|  |
| --- |
| Note If you check the relevant hedging relationship in the Manage Hedging Relationships (TPM100) app and change the display date to the termination date, you will find the status of this hedging relationship has become to. |

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
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Treasury Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Fix, Pay and Post Flows (TBB1) | The Treasury: Post Flows screen is displayed. |  |
| 3 | Enter Selection Criteria | On the Treasury: Post Flows screen, enter the following data and choose Execute:Company Code: for example, 3310Transaction: <the FX option transaction number(s) terminated>Up to and Including Due Date: <the payment date of termination>Test Run: for example, <deselect this checkbox>Post All Valuation Areas: <select this radio button> | The Information Overview dialog box is displayed. |  |
| 4 | Check Posting Log | In the Information Overview dialog box, choose Posting Log. | Posting journals are displayed. |  |

|  |
| --- |
| Note If termination results in outgoing payment with a payment request, please refer to the Foreign Currency Risk Management (1X1) test script for automatic payment of payment requests.Reclassification of Hedging Reserve and Cost of Hedging Reserve should be executed on the Exposure Subitem End Date, which is same as the normal hedge accounting process without termination of hedging instrument. |

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

For Hedge Accounting for FX Option, the following Simulated Valuation processes are supported:

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
| 3 | Enter Selection Criteria for Test Run | On the Simulate Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: for example, 003Product Type: for example, 76ATransaction Number: for example, < Transaction Number created in previous steps>Recalculate Outdated Sim.Val.: <deselect this checkbox>Note If you set this indicator, you can recalculate the outdated simulation results.Simulation Date: for example, <the current date>Key Date Valuation : <select this checkbox>Accrual/Deferral: <deselect this checkbox>Classification : <select this checkbox>Test Run: <select this checkbox> | The Messages dialog box is displayed and the following message is displayed:Processed xx positions; xx successful, 0 failedIf Recalculate Outdated Simulation Results has been executed, the following message is displayed:xx simulated results deleted for key date, Processed xx positions; xx successful, 0 failed. |  |
| 4 | Execute Simulated Valuation | The Message dialog box is displayed, and choose Continue. | The Simulate Period-End Closing screen is displayed.You can check the simulated valuation information for IFRS (valuation area 003). Please note there is no simulated valuation created because it is test run. |  |
| 5 | Enter Selection Criteria for Production Run | Choose Back until the initial screen of this app is displayed.On the initial screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The dialog Messages screen is displayed. |  |
| 6 | Execute Simulated Valuation for Production Run | The Message dialog box is displayed, choose Continue. | The Simulate Period-End Closing screen is displayed.You can check the simulated valuation information for IFRS (valuation area 003). |  |

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
| 2 | Access the SAP Fiori App | Open Delete Results of Simulated Period-End Closing (TPM_SIM_VAL_DEL). | The Delete Results of Simulated Period-End Closing screen is displayed. |  |
| 3 | Enter Selection Criteria for Test Run | On the Delete Results of Simulated Period-End Closing screen, enter the following data and choose Execute:Securities: <deselect this checkbox>OTC Transactions: <select this checkbox>Company Code: for example, 3310Valuation Area: <leave bank, or enter specific valuation are, for example, 003>Product Type: for example, 76ATransaction Number: for example, <the transaction number you noted down in the previous steps>Simulation Date: for example, <the date on which the reversal takes place>Test Run: <select this checkbox> | The Messages dialog box is displayed and the following message is displayed:xx simulated results deleted for key date (the date on which the reversal takes place). |  |
| 4 | Enter Selection Criteria for Production Run | Go back to the initial screen of this app.On the Delete Results of Simulated Period-End Closing screen, change the following data and choose Execute:Test Run: <deselect this checkbox> | The Messages dialog box is displayed and the following message is displayed:XX simulated results deleted for key date (the date on which the reversal takes place) |  |

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
> Flagged while digesting this document, not verified: Simulated Valuation steps say results can be checked for IFRS (valuation area 003), while elsewhere in the same script valuation area 003 is US GAAP.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-forward-group-ledger-us-gaap-3x3-ae-986]]
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-group-ledger-ifrs-2rw-ae-test-script-85]]
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-option-local-gaap-3x2-ae-985]]
- related-to :: [[05-treasury-and-cash-management/hedge-accounting-for-fx-swap-group-ledger-ifrs-2uf-ae-870]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3X4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 146,397 chars in the whole document
