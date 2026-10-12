---
id: 05-treasury-and-cash-management/automatic-market-rates-management-1s4-ae-test-script-762
title: Automatic Market Rates Management (1S4_AE) - Test Script (1S4_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script (1S4_AE, UAE) for automatic market rates import via Refinitiv or BYOR: translation tables, retrieval, jobs, notifications."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/market-rates-management]
aliases: [1S4_S4CLD2608_BPD_EN_AE]
keywords: [Market Rates Management (Automatic Import and Manual Upload), market rates management, datafeed translation tables, currency spot rates, retrieve market data, bring your own rates, job scheduling, job notifications, date deviation check, message control]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1S4_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-762
topic: 05-treasury-and-cash-management/market-rates-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Automatic Market Rates Management (1S4_AE) - Test Script (1S4_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1S4_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Market Rates Management (Automatic Import and Manual Upload)** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Automatic Market Rates Management (1S4_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Automatic Market Rates Management (1S4_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232847572)

[2 Prerequisites 5](#_Toc232847573)

[2.1 System Access 5](#_Toc232847574)

[2.2 Roles 5](#_Toc232847575)

[2.3 Master Data, Organizational Data, and Other Data 6](#_Toc232847576)

[2.4 Additional Manual Configuration 6](#_Toc232847577)

[3 Overview Table 7](#_Toc232847578)

[4 Test Procedures 8](#_Toc232847579)

[4.1 Define Translation Table 8](#_Toc232847580)

[4.1.1 Define Currency Spot Rate for Datafeed 8](#_Toc232847581)

[4.1.2 Define Interest Rates for Datafeed 11](#_Toc232847582)

[4.1.3 Define Basis Spread for Datafeed 12](#_Toc232847583)

[4.1.4 Define Credit Spread for Datafeed 14](#_Toc232847584)

[4.1.5 Define FX Swap Rate for Datafeed 15](#_Toc232847585)

[4.1.6 Define Securities for Datafeed 17](#_Toc232847586)

[4.1.7 Define FX Volatility with Moneyness for Datafeed 18](#_Toc232847587)

[4.1.8 Define Exchange Rate Volatility for Datafeed 19](#_Toc232847588)

[4.2 Daily Task 20](#_Toc232847589)

[4.2.1 Retrieve Market Data 21](#_Toc232847590)

[5 Appendix 23](#_Toc232847591)

[5.1 App list for Defining Translation Table 23](#_Toc232847592)

[5.2 Job Scheduling 23](#_Toc232847593)

[5.2.1 Request Current Market Data 23](#_Toc232847594)

[5.3 BYOR Option 25](#_Toc232847595)

[5.3.1 Define Currency Spot Rate for Datafeed 26](#_Toc232847596)

[5.3.2 Retrieve Market Data 27](#_Toc232847597)

[5.4 Notification for Job Scheduling 28](#_Toc232847598)

[5.4.1 Create Teams and Responsibilities 29](#_Toc232847599)

[5.4.2 Enable Situation Types 30](#_Toc232847600)

[5.4.3 User Setting for Notification 32](#_Toc232847601)

[5.4.4 Schedule a Background Job to Trigger the Notifications 33](#_Toc232847602)

[5.4.5 Check the Notification in Fiori Launchpad and E-Mail 34](#_Toc232847603)

[5.5 Check Date Deviation 35](#_Toc232847604)

[5.5.1 Assign Currency Notations 35](#_Toc232847605)

[5.5.2 Change the Message Type via Configuration Activity 37](#_Toc232847606)

[5.5.3 Retrieve Market Data 38](#_Toc232847607)

## Purpose

Overview

In this process, market data is automatically imported from the currency service provided by the SAP Business Technology Platform. You can load market rates with either Refinitiv data option, or via Bring Your Own Rates (BYOR).

The Refinitiv data and BYOR options support eight different types market data, including Currency Spot Rate, Interest Rates, Forex Swap Rates, Basis Spreads, Credit Spread, FX Volatility with Moneyness, and Securities and Exchange Rate Volatilities.

You can schedule the request for current market data as a job to get the data when you need it and tailor the market data for importing to get only the market data you need.

You can also import historical market data into your system for comparison reasons.

Currently, both of the data options support the following eight market data types:

| Data class | Data description | Refinitiv data option | BYOR |
| --- | --- | --- | --- |
| 01 | Currency spot rate | ✓ | ✓ |
| 03 | Interest rates | ✓ | ✓ |
| 21 | Forex swap rates | ✓ | ✓ |
| 09 | Basis spreads | ✓ | ✓ |
| 10 | Credit spread | ✓ | ✓ |
| 30 | FX volatility with moneyness (implied FX volatility) | ✓ | ✓ |
| 02 | Securities | ✓ | ✓ |
| 31 | Exchange rate volatilities | ✓ | ✓ |

You can schedule the request for current market data through a background job. You can also tailor the market data import to get only the market data you need.

You can also import historical market data into your system for the comparison purpose.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| SAP S/4HANA system | Accessible via Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Currency | AED, USD |  |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/1fd57db5cad061a4224f248a71c82dc2)

## Overview Table

The Automatic Market Rates Management(1S4) scope item consists of process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Define Currency Spot Rate for Datafeed](#unique_8) [page ] 8 | Treasury Specialist - Back Office | Assign Currency Notations - Datafeed (DF_TT_CURR) | Translation table for currency spot rate datafeed defined. |
| [Define Interest Rates for Datafeed](#unique_9) [page ] 11 | Treasury Specialist - Back Office | Assign Interest Rate Notations - Datafeed (DF_TT_IRATE) | Translation table for interest rate datafeed defined. |
| [Define Basis Spread for Datafeed](#unique_10) [page ] 12 | Treasury Specialist - Back Office | Assign Basis Spread Notations - Datafeed (S_EIS_72000058) | Translation table for basis spread datafeed defined. |
| [Define Credit Spread for Datafeed](#unique_11) [page ] 14 | Treasury Specialist - Back Office | Assign Credit Spread Notations - Datafeed (S_EIS_72000129) | Translation table for credit spread datafeed defined. |
| [Define FX Swap Rate for Datafeed](#unique_12) [page ] 15 | Treasury Specialist - Back Office | Assign FX Swap Rate Notations - Datafeed (S_ALR_87007973) | Translation table for FX Swap rate datafeed defined. |
| [Define Securities for Datafeed](#unique_13) [page ] 17 | Treasury Specialist - Back Office | Assign Security Price Notations - Datafeed (S_ALR_87007819) | Translation table for securities datafeed defined. |
| [Define FX Volatility with Moneyness for Datafeed](#unique_14) [page ] 18 | Treasury Specialist - Back Office | Assign General Volatility Notations - Datafeed (S_KK4_13000258) | Translation table for FX volatility with moneyness datafeed defined. |
| [Define Exchange Rate Volatility for Datafeed](#unique_15) [page ] 19 | Treasury Specialist - Back Office | Assign Exchange Rate Volatility Notations - Datafeed (S_ALR_87009318) | Translation table for exchange rate volatility datafeed defined. |
| [Retrieve Market Data](#unique_16) [page ] 21 | Treasury Specialist - Back Office | Request Current Market Data - Datafeed (TBD4)Request Historical Market Data - Datafeed (TBDJ) | Selected Market Data is updated. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The main test procedures are based on Refinitiv option.

### Define Translation Table

Purpose

Before you import data from the market datafeeds, you need to first define translation table for every market data type. You only perform this once for each type of market data.

In this section, you maintain the translation table for each type of market data.

#### Define Currency Spot Rate for Datafeed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the datafeed translation table for currency exchange rates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Assign Currency Notations - Datafeed (DF_TT_CURR). | The Determine Work Area: Entry screen is displayed. |  |
| 3 | Change an Existing Record | Enter the following data and choose Continue.Data Provider: Y001 | The Display View "Datafeed: Translation Table Currencies": Details screen is displayed. |  |
| 4 | Add a New Record | Choose Edit. |  |  |
| 5 | Add a New Record | Choose New Entries. |  |  |
| 6 | Add a New Record | Make the following entries and choose Save:Currency Pair: for example, USDAEDRate Type: for example, MMax. Deviation in Percent: for example, 10Indirect Quotation: <select>Instrument: for example, USD~AED:01Data Source: for example, STProperty: for example, MIDExternal Datafeed: for example, 1: 1Check Date Deviation: <deselect>Ratio Must Match MRM: <deselect>Note You need to make sure the External Datafeed ratio is correct.The External Datafeed ratio of Refinitiv for a currency pair varies over time. Make sure you have adjusted this External Datafeed ratio of Refinitiv for the currency pair accordingly.Note In rate monitoring (Max. Deviation in Percent), you can enter the maximum deviation between the supplied rate and the latest read rate for the same instrument class that you can tolerate as a percentage. You enter an integer between 1 and 254. It is used to calculate the interval within which the rates are accepted. If the rate is not within the interval, a warning message will be displayed. If this message is displayed, you have to check the rate and change it manually in single rate maintenance.The message type can be changed to Error via the configuration activity Message Control for Treasury Risk Management (ID: 106916). If you change the message type to Error, the system will block the relevant data transfer when running the app Request Current Market Data - Datafeed (TBD4) or the relevant background jobs.For rate monitoring, please maintain a maximum acceptable derivation value in the Max. Deviation in Percent field.Note The exchange rates are used in many SAP S/4HANA Cloud Public Edition modules. If the wrong exchange rates are imported into SAP S/4HANA Cloud Public Edition, it might cause big impact. Thus please be careful about any warning messages or error messages issued in app Request Current Market Data - Datafeed (TBD4) or the background job.You need to do correction immediately if the exchange rates are not correct to avoid any negative impact to your daily transactional data.To better help you monitor any warning messages or error messages during market data importing, you may enable the notification for job scheduling. For more information, see the Notification for Job Scheduling section in the Appendix.Note Only one record can exist for each currency pair. If the currency pair you want to created has already been maintained, you can create another pair, or skip this step.Note The check box Check Date Deviation is to activate the validity check function of the exchange rate data for one currency pair. If you want to enable this function, please refer to the relevant chapter in the Appendix.Note To activate the check function of one currency pair's exchange ratio between MRM/Refinitiv and S4, you need to select the Ratio Must Match MRM checkbox. It’s controlled by the checkbox in Assign Currency Notations - Datafeed (DF_TT_CURR) App. Default value is blank.SAP system will always compare the exchange ratio which saved as from factor/to factor in MRM/Refinitiv and the external ratio in App Assign Currency Notations - Datafeed (DF_TT_CURR). For one currency pair, when running the App Request Current Market Data - Datafeed (TBD4) or the relevant background jobs, the system will give you a message if the exchange ratio is not consistent.Once you select this check box and the exchange ratio is different between MRM/Refinitiv and external ratio in App Assign Currency Notations - Datafeed (DF_TT_CURR), the system will send you the error message Currency ratio XX:X in MRM is different from ratio XX:X in S/4HANA and block the relevant data transfer.If this checkbox is deselected, it will send you the warning message Currency ratio XX:X in MRM is different from ratio XX:X in S/4HANA. The data will be transferred to S4 at the same time. | The data is saved without error. |  |

#### Define Interest Rates for Datafeed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the datafeed translation table for interest rates.

|  |
| --- |
| Note You can only create one record for one reference interest rate. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Assign Interest Rate Notations - Datafeed (DF_TT_IRATE). | The Determine Work Area: Entry dialog box is displayed. |  |
| 3 | Change an Existing Record | Enter the following data and choose Continue:Data Provider: Y001 | The Display View "Datafeed: Translation Table Reference Interest Rates": Details screen is displayed. |  |
| 4 | Add a New Record | Choose Edit .Choose New Entries, enter new data, and choose Save:Ref. Int. Rate: for example, EURM03EURInstrument: for example, EUR3MD:03Data Source: for example, STProperty: for example, MID | The data was saved without an error. |  |
| 5 | Create Another Record | Choose New Entries, maintain the following fields and choose Save:Ref. Int. Rate: for example, USDM03LIBInstrument: for example, EUR3MD:03Data Source: for example, STProperty: for example, MID | The data was saved without an error. |  |

#### Define Basis Spread for Datafeed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the datafeed translation table for basis spread.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Assign Basis Spread Notations - Datafeed (S_EIS_72000058) | The Determine Work Area: Entry dialog box is displayed. |  |
| 3 | Enter Parameters on the initial screen | In the Determine Work Area: Entry dialog box, make the following entry and choose Continue(Enter):Data Provider: Y001 | The Change View "Datafeed: Basis Spread Translation Table": Overview screen is displayed. |  |
| 4 | Add new entries | On the Change View "Datafeed: Basis Spread Translation Table": Overview screen, choose New Entries.On the New Entries: Details of Added Entries screen, make the following entries and choose Save:Basis Spread ID: for example, CEURUSD3M01YQuotation Type: for example, 1Save Market Data Permanently in System: <select this checkbox>Data Provider: Y001Instrument: EURCBS1Y:09Data Source: for example, STProperty: for example, 1Explan. : for example, Euro/US Dollar 1 Year Currency Basis SwapNote The checkbox of Save Market Data Permanently in System has to be selected if you want to store the data into the SAP S/4HANA Cloud Public Edition system. | The following message is displayed at the bottom of the screen:Data was saved. |  |
| 5 | Copy an entry | On the New Entries: Details of Added Entries screen, choose Back till the Change View "Datafeed: Basis Spread Translation Table": Overview screen is displayed.On the Change View "Datafeed: Basis Spread Translation Table": Overview screen, select the checkbox of the newly created entry: CEURUSD3M01YChoose Copy As…(F6) on the Change View "Datafeed: Basis Spread Translation Table": Details of Sel screen, enter the following data and then choose Copy:Basis Spread ID: for example, TEUR6M3M01YInstrument: EUR3E6E1Y:09Explan. : for example, for Euro 1 Year Basis SwapThe following message is displayed:Number of entries copied:1Choose Save.Note The checkbox of Save Market Data Permanently in System has to be selected if you want to store the data into the SAP S/4HANA Cloud Public Edition system. | The following message is displayed at the bottom of the screen:Data was saved. |  |

#### Define Credit Spread for Datafeed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the datafeed translation table for credit spread.

Prerequisite

You have created reference entities according to the following sections of the Market Rates Management – Manually via Upload(1XN) test script:

- Create Reference Entities for Business Partners
- Maintain Reference Entities

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Assign Credit Spread Notations - Datafeed (S_EIS_72000129) | The Determine Work Area: Entry screen is displayed. |  |
| 3 | Enter Parameters on the Initial Screen | In the Determine Work Area: Entry dialog box, make the following entry and choose Continue(Enter):Data Provider: Y001 | The Change View "Datafeed: Translation Table for Credit Spreads": Overview screen is displayed. |  |
| 4 | Add New Entries | On the Change View "Datafeed: Translation Table for Credit Spreads": Overview screen, choose New Entries.On the New Entries: Details of Added Entries screen, make the following entries and choose Save:Reference Entity: for example, BP_0033537001Credit Spread ID: for example, YEAR_01Quotation Type: for example, 1Data Provider: Y001Instrument: DNBA1YEUAM:10Data Source: for example, STProperty: for example, BIDExplan.: for example, Credit Spread 1 Year for example BP | The following message is displayed at the bottom of the screen:Data was saved.Note The instrument data here need to be entered base on the instrument data saved in MRM system. |  |
| 5 | Copy an Entry | On the New Entries: Details of Added Entries screen, choose Back till the Change View "Datafeed: Translation Table for Credit Spreads": Overview screen is displayed.On the Change View "Datafeed: Translation Table for Credit Spreads": Overview screen, select the checkbox of the newly created entry: BP_0033537001Choose Copy As…(F6) on the Change View "Datafeed: Translation Table for Credit Spreads": Details screen, and make the following changes:Reference Entity: for example, CC_3310Credit Spread ID: for example, MONTH_03Instrument: BNPP1YEUAM:10Data Source: for example, STProperty: for example, BIDExplan. : for example, Credit Spread for example companyThen choose Copy . The following message is displayed:Number of entries copied:1Choose Save. | The following message is displayed at the bottom of the screen:Data was saved.Note The instrument data here need to be entered base on the instrument data saved in MRM system. |  |

#### Define FX Swap Rate for Datafeed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the datafeed translation table for FX swap rate.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Assign FX Swap Rate Notations - Datafeed (S_ALR_87007973) | The Determine Work Area: Entry dialog box is displayed. |  |
| 3 | Enter Parameters on the initial screen | On the Determine Work Area: Entry screen, make the following entry and choose Continue(Enter):Data Provider: Y001 | The Change View "Datafeed: Translation Table for FX Swap Rates": Overview screen is displayed. |  |
| 4 | Add new entries | On the Change View "Datafeed: Translation Table for FX Swap Rates": Overview screen, choose New Entries.On the New Entries: Details of Added Entries screen, make the following entries and choose Save:Crcy Pair: for example, EUR USDRt.Type: for example, MTerm in Days: for example, 60Save Market Data Permanently in System: <select this checkbox>Data Provider: Y001Instrument: EUR~USD:21Data Source: for example, STProperty: for example, MID~2MExplan.: for example, FX swap rate EUR to USD 2 monthExternal Datafeed.: for example, 1:1Note The checkbox of Save Market Data Permanently in System has to be selected if you want to store the data into the SAP S/4HANA Cloud Public Edition system. | The following message is displayed at the bottom of the screen:Data was saved. |  |
| 5 | Copy an entry | On the New Entries: Details of Added Entries screen, choose Back till the Change View "Datafeed: Translation Table Securities": Overview screen is displayed.On the Change View "Datafeed: Translation Table for FX Swap Rates": Overview screen, select the checkbox of the newly created entry: EUR USD M 60Choose Copy As…(F6) on the Change View "Datafeed: Translation Table for Forwards": Details of Sel screen, make the following changes and choose Copy:Term in Days: for example, 120Property: for example, MID~4MExplan.: for example, FX Swap Rate EUR to USD 120 daysThe following message is displayed:Number of entries copied:1Choose Save.Note The checkbox of Save Market Data Permanently in System has to be selected if you want to store the data into the SAP S/4HANA Cloud Public Edition system. | The following message is displayed at the bottom of the screen:Data was saved. |  |

#### Define Securities for Datafeed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the datafeed translation table for security prices.

Prerequisite

You have created security classes ST_AE1, according to the procedures described in the Stock Management(5OD) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Assign Security Price Notations - Datafeed (S_ALR_87007819) | The Determine Work Area: Entry dialog box is displayed. |  |
| 3 | Enter Parameters on the initial screen | On the Determine Work Area: Entry screen, make the following entry and choose Continue(Enter):Data Provider: Y001 | The Change View "Datafeed: Translation Table Securities": Overview screen is displayed. |  |
| 4 | Add new entries | On the Change View "Datafeed: Translation Table Securities": Overview screen, choose New Entries.On the New Entries: Details of Added Entries screen, make the following entries and choose Save:Security: for example, ST_AE1Exchange: for example, EURONEXT PRateType: for example, 01Save Market Data Permanently in System: <select this checkbox>Data Provider: Y001Instrument: SAPG. AE 02Data Source : for example, STProperty: for example, 01Explan.: for example, Security price - spotThe checkbox of Save Market Data Permanently in System has to be selected if you want to store the data into the SAP S/4HANA Cloud Public Edition system. | The following message is displayed at the bottom of the screen:Data was saved.Note The instrument data here need to be entered base on the instrument data saved in MRM system. |  |

#### Define FX Volatility with Moneyness for Datafeed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define datafeed translation table for general volatilities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Assign General Volatility Notations - Datafeed (S_KK4_13000258) | The Determine Work Area: Entry dialog box is displayed. |  |
| 3 | Enter Parameters on the initial screen | In the Determine Work Area: Entry dialog box, make following entry and choose Continue(Enter):Data Provider: Y001 | The Change View "Datafeed: Translation Table Currency Volatilities": Overview screen is displayed. |  |
| 4 | Add new entries | On the Change View "Datafeed: Translation Table for Volatilities": Overview screen, choose New Entries.On the New Entries: Details of Added Entries screen, make the following entries and choose Save:Volatility Name: for example,Profile: for example, _10C_2WVolatility type: for example, 002Data Provider: Y001Instrument: EURISK25C2W:30Data Source: for example, STProperty: for example, MIDExplan.: for example, EUR USD Volatility with Refinitiv demo dataNote The checkbox of Save Market Data Permanently in System has to be selected if you want to store the data into the SAP S/4HANA Cloud Public Edition system. | The following message is displayed at the bottom of the screen:Data was saved.Note The instrument data here need to be entered base on the instrument data saved in MRM system. |  |

#### Define Exchange Rate Volatility for Datafeed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define datafeed translation table for currency volatility.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Assign Exchange Rate Volatility Notations - Datafeed (S_ALR_87009318) | The Determine Work Area: Entry screen is displayed. |  |
| 3 | Enter Parameters on the initial screen | On the Determine Work Area: Entry dialog box, make following entries and choose Continue(Enter):Data Provider: Y001 | The Change View "Datafeed: Translation Table Currency Volatilities": Overview screen is displayed. |  |
| 4 | Add new entries | On the Change View "Datafeed: Translation Table Currency Volatilities": Overview screen, choose New Entries.On the New Entries: Details of Added Entries screen, make the following entries and choose Save:Curr.pair: for example, EUR USDVolatility type: for example, 002Term in days: for example,30Save Market Data Permanently in System: <Select this checkbox>Data Provider: Y001Instrument: EUR~USD:31Data Source: for example, STProperty: for example, MID~1MExplan.: for example, Volatilities for EUR to USD with Refinitiv demo dataNote The checkbox of Save Market Data Permanently in System has to be selected if you want to store the data into the SAP S/4HANA Cloud Public Edition system. | The following message is displayed at the bottom of the screen:Data was saved.Note The instrument data here need to be entered base on the instrument data saved in MRM system. |  |

### Daily Task

Purpose

In this section, you update the market data through the datafeed.

#### Retrieve Market Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you request the market data through datafeed. You can retrieve both current and historical market data.

Prerequisite

If you've subscribed to type BYOR - Bring Your Own Rates, you need to upload all kind of rates via the uploading API provided by Market Rate Management of SAP BTP.

Procedure

Table 1: Request Current Market Data

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Request Current Market Data - Datafeed (TBD4). | The Datafeed: Request Current Market Data view is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Make the following entries and choose Execute:Market Data Class: for example, <select all the checkboxes>Datafeed Name: for example, Y001 | The result overview displays the data updates.For more information, see the Enter FX Spot Rates and Enter Interest Rates sections in the Market Rates Management – Manually via Upload(1XN) test script. |  |

Table 2: Request Historical Market Data

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Request Historical Market Data - Datafeed (TBDJ). | The Datafeed: Request Historical Market Data view is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Make the following entries and choose Execute:Market Data Class: for example, <select all the checkboxes>Period of History: for example, <1st day of last month – 7th day of last month>Datafeed Name: for example, Y001 | The result overview displays the data updates.For more information, please check the relevant sections in the Market Rates Management – Manually via Upload(1XN) test script. |  |

## Appendix

### App list for Defining Translation Table

- Assign Currency Notations - Datafeed (DF_TT_CURR)
- Assign Interest Rate Notations - Datafeed (DF_TT_IRATE)
- Assign Basis Spread Notations - Datafeed (S_EIS_72000058)
- Assign Credit Spread Notations - Datafeed (S_EIS_72000129)
- Assign FX Swap Rate Notations - Datafeed (S_ALR_87007973)
- Assign Security Price Notations - Datafeed (S_ALR_87007819)
- Assign General Volatility Notations - Datafeed (S_KK4_13000258)

### Job Scheduling

#### Request Current Market Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can schedule background job for Request Current Market Data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen is displayed. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose Create. | The New Job screen is displayed. |  |
| 4 | Enter General Information for New Job | On the New Job screen, enter the following data, and choose Step 2:Job Template: for example, <Request Current Market Data>Job Name: for example, <Request Current Market Data> | The Scheduling Information screen is displayed. |  |
| 5 | Enter Scheduling Options for New Job | In the Scheduling Options area, enter the following data, and choose Step 3:For Start Immediately case:Start Immediately: <select this checkbox>For Recurrence case:Choose Define Recurrence Pattern, and in the Scheduling Information dialog box, enter the following data and choose OK.Start Immediately: <deselect this checkbox>Job Start: for example, Current Date/Current Time + 5 minutesRecurrence Pattern: for example, DailyEvery: for example, 1End: for example, after 7 Occurrence(s)On Non-Working Day: <no restriction> | Back to New Job screen. |  |
| 6 | Enter Parameters for New Job | In the Parameters area, enter the following data:Market Data Class: for example, select CurrenciesDatafeed – Name: for example, Y001 |  |  |
| 7 | Schedule New Job | Choose Schedule. | Automatically go back to the initial screen of this app, the job you just scheduled displays in the result area. |  |
| 8 | Check Result | Choose the row of the job you just scheduled.Note Please enable the notification for job scheduling. For more information, see the Notification for Job Scheduling section in the Appendix. | The Job Details screen displays.If it is in status Finished (depends on parameters you entered for Scheduling Options), click the icon beside Results, a new window will open and you can check the result of this finished job. |  |

### BYOR Option

Purpose

If you've subscribed to type BYOR - Bring Your Own Rates, you need to upload all kind of rates via the uploading API provided by Market Rate Management of SAP BTP.

In this step, you can use BYOR option to get the market data from MRM system (Market Rate Management of SAP BTP).

Here provides an example of currency exchange rates.

Prerequisite

Before you run Request Current Market Data - Datafeed (TBD4) in this step, you need to complete all the relevant steps in MRM system and ensure that the market data is saved in the MRM system.

Besides, the market data key saved in the MRM system should match to the notation assignment.

For the detailed steps in MRM system, you could refer to the link: [https://help.sap.com/viewer/64e0eccf2d424543be76606dd5e5e460/LATEST/en-US/edfd50733e6240e9a51d08f51fbaf780.html](https://help.sap.com/viewer/64e0eccf2d424543be76606dd5e5e460/LATEST/en-US/edfd50733e6240e9a51d08f51fbaf780.html)

Please upload the sample upload rates in MRM.

| Data Provider | Data Source | Market Data Category | Key1 | Key2 | Property | Effective Date | Time | Market Data Value | Security Currency | From Factor | To Factor | Price Quotation | Additional Key | Status | Message |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Y001 | BYOR | 01 | EUR | USD | MID | 2022-09-12 | 00:00:00 | 0.975 |  |  |  |  |  |  |  |
| Y001 | BYOR | 01 | USD | AED | MID | 2022-09-12 | 00:00:00 | 1.05 |  |  |  |  |  |  |  |

#### Define Currency Spot Rate for Datafeed

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the datafeed translation table for currency exchange rates based on BYOR option.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Assign Currency Notations - Datafeed (DF_TT_CURR). | The Determine Work Area: Entry screen is displayed. |  |
| 3 | Change an Existing Record | Enter the following data and choose Continue.Data Provider: Y001 | The Display View "Datafeed: Translation Table Currencies": Details screen is displayed. |  |
| 4 | Add a New Record | Choose . |  |  |
| 5 | Add a New Record | Choose New Entries. |  |  |
| 6 | Add a New Record | Make the following entries and choose Save:Currency Pair: for example, USDAEDRate Type: for example, MIndirect Quotation: <select>Instrument: for example, USD~AED:01Data Source: for example, BYORProperty: for example, CMIDExternal Datafeed: for example, 1: 1Note Only one record can exist for each currency pair. If the currency pair you want to created has already been maintained, you can create another pair, or skip this step. | The data is saved without error.Note Make sure all the parameters can match to the key fields in MRM system accordingly. |  |

#### Retrieve Market Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you request the market data through datafeed. You can retrieve both current and historical market data.

Prerequisite

If you've subscribed to type BYOR - Bring Your Own Rates, you need to upload all kind of rates via the uploading API provided by Market Rate Management of SAP BTP.

Procedure

Table 3: Request Current Market Data

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Request Current Market Data - Datafeed (TBD4). | The Datafeed: Request Current Market Data view is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Make the following entries and choose Execute:Market Data Class: for example, <select all the checkboxes>Datafeed Name: for example, Y001 | The result overview displays the data updates.For more information, see the Enter FX Spot Rates and Enter Interest Rates sections in the Market Rates Management – Manually via Upload(1XN) test script. |  |

Table 4: Request Historical Market Data

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori app | Open Request Historical Market Data - Datafeed (TBDJ). | The Datafeed: Request Historical Market Data view is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Make the following entries and choose Execute:Market Data Class: for example, <select all the checkboxes>Period of History: for example, <1st day of last month – 7th day of last month>Datafeed Name: for example, Y001 | The result overview displays the data updates.For more information, please check the relevant sections in the Market Rates Management – Manually via Upload(1XN) test script. |  |

### Notification for Job Scheduling

Situation handling is a framework provided by SAP S/4HANA that could increase the quality and efficiency of business processes by signaling exceptional information. Notification for Job Scheduling of request market data is enabled in Treasury and Risk Management. For example, if you scheduled a background job to request current market data periodically, you could use the notification function to enable the system to send you a job log once the job run is completed. There are several channels for notification, including the notification area on the SAP Fiori launchpad and email.

|  |
| --- |
| Note Make sure scope item Situation Handling (31N) is activated in your system before you use this functionality. |

To integrate with situation handling, Treasury and Risk Management provides the following:

- Situation Template: FIN_TRM_REQUEST_MARKET_DATA
- Standard Team Category: FSCM_TRM

There are some customizing configurations needed. In SAP S/4HANA Cloud Public Edition, the following best practice customizing configurations are pre-delivered.

Table 5: Predefined Entities

| Entity | Definition | Description |
| --- | --- | --- |
| Functions | STRM_FT_MD | Administration Employee for Market Data |
| Function Profiles | STRM_FP | Function Profile for Treasury and Risk Management |
| Team Types | STRM_MD | Treasury Market Data Administration |

You need the following business roles to do the test.

| Business Role | Business Role ID | Application |
| --- | --- | --- |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Manage Situation Types - Extended (F5437) |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Manage Teams and Responsibilities (F2412)Manage Situation Types (F2947) |
| Treasury Specialist - Back Office | SAP_BR_TREASURY_SPECIALIST_BOE | My Situations (F4537) |

#### Create Teams and Responsibilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a team and maintain the general information and responsibility definitions for the team.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities screen displays. |  |
| 3 | Create Team | Choose Create. | The Team screen displays. |  |
| 4 | Maintain Team General Information | In the General Information section, enter the following data:Name: for example, Z_TEST_MD_01Type: for example, STRM_MDDescription: for example, <TRM Test Description for Situation Handling>Status: Enabled | The Global ID will be generated automatically. |  |
| 5 | Maintain Team Members | In the Team Members section, enter the following data and choose Create:Business Partner: <Choose the user you want to get the notification or email in F4 help>Note To get email notifications, you need to maintain the user's email correctly.Functions: STRM_MD_AD |  |  |
| 6 | Save the Team | Choose Save. | The Team is created successfully. |  |

#### Enable Situation Types

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the situation type for your teams.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Business Process Specialist. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types - Extended (F5437). | The Manage Situation Types screen displays. |  |
| 3 | Create New Situation Type | Click the Create button with the selection ‘Create Situation Type’.On the Create New Situation Type screen, select or enter the following data:ID: TEST_TRM_MD_ST01Name: Market Data RequestDescription: Market Data Request notificationSituation Scenario: FIN_TRM_MD_REQUEST_MSG_MONITORSituation Template: FIN_TRM_REQUEST_MARKET_DATAAfter input all above items, press Create button. | The Hander information for Situation Type screen displays. |  |
| 4 | Maintain the Status for the Situation Type | On the Hander information for Situation Type screen, select/enter the following data:Status: EnabledOn the Recipients area, select/enter following data:Filter by Member Function: Administration Employee for Market Data |  |  |
| 5 | Message-Based Triggers | In the Message-Based Triggers section, check the following data is in assigned:Item 1Name/Description: Market Data Request FailedItem 2Name/Description: Market Data Request SuccessfulItem 3Name/Description: Market Data Req. Successful with Warning |  |  |
| 6 | Maintain Situation Display | By selecting any items created in the Message-Based Triggers section, get into the Situation Display section, you can insert variables if you want to receive detailed information for the notification and email.Check and keep the default Situation Texts are assigned in Situation Display.Title: Notification for market data requestDescription: Notification for market data requestNotification Title: Error occurred during market data req.Notification Text: Error occurred during market data request.Public Text: Error occurred during market data request. You can find the detailed error messages in the Job Scheduling Framework in your SAP S/4HANA system. |  |  |
| 7 | Save the Situation Type | After you have done all above steps, choose Create. | The situation type is created. |  |

#### User Setting for Notification

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you enable the notifications for your user.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with your own user. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open profile of the logged-on user in the right corner. |  |  |
| 3 | Find the Notifications Setting | Choose Notifications in Settings. | The Notifications screen is displayed. |  |
| 4 | Enable the Email and Notification Alert in Launchpad | On the Notifications screen, enter the following data, and choose Save:Email: <select>High Priority: <check>Enable: Enabled | Note Please re-logon the current user if you cannot find the selections in the Notifications. |  |

#### Schedule a Background Job to Trigger the Notifications

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you can schedule a background job to request market data. You will receive a message in notification function once the job is completed.

Prerequisites

Please refer to [Define Currency Spot Rate for Datafeed](#unique_8) [page ] 8 to define the datafeed translation table for currency exchange rates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Treasury Back Office Jobs (F2771). | The Application Jobs screen displays. |  |
| 3 | Create A New Job | On the Application Jobs screen, choose New. | The New Job screen is displayed. |  |
| 4 | Enter General Infor-mation for New Job | On the New Job screen, enter the following data then choose Add More Scheduling Options:Job Template: for example, <Request Current Market Data>Job Name: for example, <Request Current Market Data>Market Data Class: for example, select CurrenciesDatafeed – Name: for example, Y001 | The Scheduling Information screen is displayed. |  |
| 5 | Enter Scheduling Options for New Job | On the Scheduling Information screen, enter the following data then choose OK:For Start Immediately case:Start Immediately: <select this checkbox>For Recurrence case:Start Immediately: <deselect this checkbox>Start: for example, <Current Date/Current Time>Recurrence Pattern: for example, DailyEvery: for example, 1End: for example, after 7 Occurrence(s)On Non-Working Day: <no restriction> | Back to New Job screen. |  |
| 6 | Schedule New Job | Choose Schedule. | Automatically go back to the initial screen of this app, the job you just scheduled displays in the result area. |  |
| 7 | Check Result | Choose the row of the job you just scheduled. | The Job Details screen displays.If it is in status Finished (depends on parameters you entered for Scheduling Options), click the icon beside Results, a new window will open and you can check the result of this finished job. |  |

#### Check the Notification in Fiori Launchpad and E-Mail

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you check the notification in Fiori Launchpad and email notification in Outlook.

Procedure

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Test Step # | Test Step Name | Instruction | Expected Result |  |
| 1 | Log On | Log on to the SAP Fiori launchpad with your own user. | The SAP Fiori launchpad displays. |  |
| 2 | Check Notification Area | Choose the red exclamation mark in the Notification Area. | You will see Notification Msg By Date, By Type, By Priority in the Notification Area. |  |
| 3 | Check Detail Message | Choose Show More. | Notification detail is displayed. |  |
| 4 | Check My Situations | Open My Situations (F4537). | Your open situations are displayed. |  |
| 5 | Check Email | Check email notifications in Outlook.Note The batch job will trigger when you define the Situation Type. | You will receive email notifications in the email address you maintained in your user account. |  |

### Check Date Deviation

#### Assign Currency Notations

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you define the datafeed translation table for currency exchange rates and enable the Check Date Deviation function.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Assign Currency Notations - Datafeed (DF_TT_CURR). | The Determine Work Area: Entry screen is displayed. |  |
| 3 | Change an Existing Record | Enter the following data and choose Continue:Data Provider: Y001 | The Display View "Datafeed: Translation Table Currencies": Details screen is displayed. |  |
| 4 | Add a New Record | Choose Edit. |  |  |
| 5 | Add a New Record | Choose New Entries. |  |  |
| 6 | Add a New Record | Make the following entries and choose Save:Currency Pair: for example, EURCHFRate Type: for example, MMax. Deviation in Percent: for example, 0Indirect Quotation: <deselect>Instrument: for example, EUR~CHF:01Data Source: for example, STProperty: for example, MIDExternal Datafeed: for example, 1:1Check Date Deviation: <select>Calendar: 01Max. Deviation in Days: 3Note The checkbox Check Date Deviation is to activate the validity check function of the exchange rate data for one currency pair.To enable this function, you need to input the Max. Deviation in Days field to define the maximum deviation between the system date and valid date of the market data. Please also select one calendar for it. The system can calculate the maximum deviation days with the consideration of weekends and public holidays.If the calculated deviation is larger than the defined maximum deviation days, the system will report a warning message.Effective date XXXX/XX/XX exceeds max. deviation in days from system date XXXX/XX/XX when running the App Request Current Market Data - Datafeed (TBD4) or the relevant background jobs to get the market data.The message type can be changed to Error via the Configuration Activity: Message Control for Treasury Risk Management (ID: 106916). If you change the message type to Error, the system will block the relevant data transfer when running the App Request Current Market Data - Datafeed (TBD4) or the relevant background jobs. | The data is saved without error. |  |

#### Change the Message Type via Configuration Activity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you change the message type via the configuration activity Message Control for Treasury Risk Management (ID: 106916) when the Date Deviation check is triggered.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Configuration Expert - Business Process Configuration. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Implementation Activities (SIMG). | The Display IMG: Authorized Activities screen is displayed. |  |
| 3 | Located the Configuration Activity and Enter It | Located the configuration activity Change Message Control - Treasury and Risk Management under menu Treasury Management > Common Settings (TRM) . | The Determine Work Area: Entry screen is displayed. |  |
| 4 | Enter Work Area | Make the following entries and choose Apply:Application Area: for example, FTDF | The Message Control for Treasury Risk Management view is displayed.Note Only Application Area FTDF/FTR_GUI/FTR_ASSIGNMENT is enabled the in this configuration activity. |  |
| 5 | Create a New Message Control Configuration Item | Make the following entries and choose Save:MsgNo: for example, 000Online: for example, EBatchl: for example, W | The new message control configuration item is saved.Note The message type maintained in the Online field will impact the Date Deviation Check result when retrieve market data via the front-end app or the background job.Note This configuration activity can support to change some message control type in different business scenarios. |  |

#### Retrieve Market Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you request the market data through datafeed. You can retrieve current market data.

Procedure

Table 6: Request Current Market Data

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Request Current Market Data - Datafeed (TBD4). | The Datafeed: Request Current Market Data view is displayed. |  |
| 3 | Enter Selection Criteria and Execute | Make the following entries and choose Execute:Market Data Class: for example, <select the checkbox: Currencies>Datafeed Name: for example, Y001 | The result overview displays the data updates.Warning message reported with the market data of currency pair EURCHF:Effective date XXXX/XX/XX exceeds max. deviation in days from system date XXXX/XX/XXNote The message type can be changed to Error via the Configuration Activity Message Control for Treasury Risk Management (ID: 106916). If you change the message type to Error, the system will block the relevant data transfer when running the App Request Current Market Data - Datafeed (TBD4) or the relevant background jobs. |  |

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
- related-to :: [[05-treasury-and-cash-management/test-script-market-rates-management-manually-via-upload-1xn-ae-782]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1S4_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 64,780 chars in the whole document
