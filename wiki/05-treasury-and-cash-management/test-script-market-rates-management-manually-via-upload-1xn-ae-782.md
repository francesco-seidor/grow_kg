---
id: 05-treasury-and-cash-management/test-script-market-rates-management-manually-via-upload-1xn-ae-782
title: "Test Script: Market Rates Management – Manually via Upload (1XN_AE) (1XN_S4CLD2608_BPD_EN_AE)"
description: SAP S/4HANA Cloud Public Edition 2608 test script (1XN_AE) for manually entering or uploading Treasury market data and checking the Market Data Overview.
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/market-rates-management]
aliases: [1XN_S4CLD2608_BPD_EN_AE]
keywords: [Market Rates Management (Automatic Import and Manual Upload), market data management, fx spot rates, fx swap rates, exchange rate volatilities, volatilities with moneyness, interest rates, credit spreads, basis spreads, securities prices]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XN_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-782
topic: 05-treasury-and-cash-management/market-rates-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Market Rates Management – Manually via Upload (1XN_AE) (1XN_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XN_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Market Rates Management (Automatic Import and Manual Upload)** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Market Rates Management – Manually via Upload (1XN_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232848299)

[2 Prerequisites 4](#_Toc232848300)

[2.1 System Access 4](#_Toc232848301)

[2.2 Roles 4](#_Toc232848302)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232848303)

[2.4 Business Conditions 5](#_Toc232848304)

[3 Overview Table 6](#_Toc232848305)

[4 Test Procedures 8](#_Toc232848306)

[4.1 Manually Input Market Data 8](#_Toc232848307)

[4.1.1 Enter FX Spot Rates 8](#_Toc232848308)

[4.1.2 Enter FX Swap Rates 9](#_Toc232848309)

[4.1.3 Enter Exchange Rate Volatilities 11](#_Toc232848310)

[4.1.4 Assign Currency Pairs for Volatilities with Moneyness for Foreign Exchange Rate 12](#_Toc232848311)

[4.1.5 Enter Values for Volatilities with Moneyness for Foreign Exchange Rate 14](#_Toc232848312)

[4.1.6 Assign Security Class for Volatilities with Moneyness for Securities Option 17](#_Toc232848313)

[4.1.7 Enter Values for Volatilities with Moneyness for Securities Option 19](#_Toc232848314)

[4.1.8 Enter Interest Rates 20](#_Toc232848315)

[4.1.9 Enter Price Index Values 25](#_Toc232848316)

[4.1.10 Check Yield Curves 26](#_Toc232848317)

[4.1.11 Create Reference Entities for Business Partners 27](#_Toc232848318)

[4.1.12 Assign Attributes to Evaluation Type 28](#_Toc232848319)

[4.1.13 Maintain Reference Entities 30](#_Toc232848320)

[4.1.14 Enter Credit Spreads 31](#_Toc232848321)

[4.1.15 Enter Basis Spreads 33](#_Toc232848322)

[4.1.16 Update Securities Price 35](#_Toc232848323)

[4.1.16.1 Update Securities Price - Money Market Mutual Fund Management 35](#_Toc232848324)

[4.1.16.2 Update Securities Price - Bond Management 37](#_Toc232848325)

[4.1.16.3 Update Securities Price - Stock Management 40](#_Toc232848326)

[4.1.16.4 Update Securities Price - Shareholding Management 41](#_Toc232848327)

[4.1.16.5 Update Security Price - ABS/MBS Management 42](#_Toc232848328)

[4.1.17 Enter Securities Factor Values 43](#_Toc232848329)

[4.2 Import Market Data via File Upload 47](#_Toc232848330)

[4.2.1 Import Market Data via File Upload 47](#_Toc232848331)

[4.3 Report 56](#_Toc232848332)

[4.3.1 Market Data Overview 56](#_Toc232848333)

## Purpose

Overview

With this process, you can manually enter the relevant market data or import market data from spreadsheets needed for the processes in Treasury and Risk Management.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites to conducting the test in terms of systems, users, master data, organizational data, and other test data and business conditions.

### System Access

The test is conducted in the following systems:

| System | Details |
| --- | --- |
| SAP S/4HANA system | Accessible via Fiori Launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | Description | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- | --- |
| Treasury Specialist - Back Office |  | SAP_BR_TREASURY_SPECIALIST_BOE | Treasury Back Office | SAP_BR_TREASURY_SPECIALIST_BOE |  |
| Treasury Risk Manager |  | SAP_BR_TREASURY_RISK_MANAGER | Treasury Analytics | SAP_BR_TREASURY_RISK_MANAGER |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | 3310 |  |  |
| Currency | AED, USD, BRL |  |  |
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
| 22G - Create Business Partner for Treasury and Risk Management - MDS | Perform scope item 22G to create business partner. |

## Overview Table

This scope item consists of several process steps that are listed in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/APP | Expected Results |
| --- | --- | --- | --- |
| [Enter FX Spot Rates](#unique_8) [page ] 8 | Treasury Specialist - Back Office | Currency Exchange Rates (F3616) | You enter the currency exchange spot rates |
| [Enter FX Swap Rates](#unique_9) [page ] 9 | Treasury Specialist - Back Office | Enter FX Swap Rates (TMDFXFP) | You enter the currency exchange swap rates |
| [Enter Exchange Rate Volatilities](#unique_10) [page ] 11 | Treasury Specialist - Back Office | Enter Exchange Rate Volatilities (JBVFX) | You enter the exchange rate volatility |
| [Assign Currency Pairs for Volatilities with Moneyness for Foreign Exchange Rate](#unique_11) [page ] 12 | Treasury Specialist - Back Office | Volatilities with Moneyness - Enter Values (TMDVOLANAME) Volatilities with Moneyness - Assign Currency Pairs (TMDAS_VOLANAME2FX) | You assign volatility name to currency pairs |
| [Enter Values for Volatilities with Moneyness for Foreign Exchange Rate](#unique_12) [page ] 14 | Treasury Specialist - Back Office | Volatilities with Moneyness - Enter Values (TMDVOLANAME) | You enter values for volatilities with moneyness |
| [Assign Security Class for Volatilities with Moneyness for Securities Option](#unique_13) [page ] 17 | Treasury Specialist - Back Office | Volatilities with Moneyness - Enter Values (TMDVOLANAME) | You create the volatility and volatility profile and assign them to the security class |
| [Enter Values for Volatilities with Moneyness for Securities Option](#unique_14) [page ] 19 | Treasury Specialist - Back Office | Volatilities with Moneyness - Enter Values (TMDVOLANAME) | You enter values for volatilities with moneyness for securities options |
| [Enter Interest Rates](#unique_15) [page ] 20 | Treasury Specialist - Back Office | Enter Interest Rates (JBIRMC) | You enter the reference interest rates. |
| [Check Yield Curves](#unique_16) [page ] 26 | Treasury Specialist - Back Office | Manage Yield Curves (JBYCN) | You review the yield curve for a certain currency. |
| [Create Reference Entities for Business Partners](#unique_17) [page ] 27 | Treasury Specialist - Back Office | Create Reference Entities - Business Partners (RMREBP) | You create the reference entity for a business partner |
| [Assign Attributes to Evaluation Type](#unique_18) [page ] 28 | Treasury Specialist - Back Office | Configuration Activity: Define and Set Up Evaluation Types | You assign attributes to the evaluation type. |
| [Maintain Reference Entities](#unique_19) [page ] 30 | Treasury Specialist - Back Office | Manage Reference Entities (RMRE) | You review the reference entities list and create a reference Entity for a Company Code |
| [Enter Credit Spreads](#unique_20) [page ] 31 | Treasury Specialist - Back Office | Enter Credit Spreads (RMCSM) | You enter credit spreads for a Business Partner or own Company Code |
| [Enter Basis Spreads](#unique_21) [page ] 33 | Treasury Specialist - Back Office | Enter Basis Spreads (RMBSM) | You enter the basis spreads. |
| [Update Securities Price - Money Market Mutual Fund Management](#unique_22) [page ] 35 | Treasury Specialist - Back Office | Enter Securities Prices (FW17) | Security prices are entered for money market mutual fund. |
| [Update Securities Price - Bond Management](#unique_23) [page ] 37 | Treasury Specialist - Back Office | Enter Securities Prices (FW17) | Security prices are entered for bond. |
| [Update Securities Price - Stock Management](#unique_24) [page ] 40 | Treasury Specialist - Back Office | Enter Securities Prices (FW17) | Security prices are entered for stock. |
| [Enter Securities Factor Values](#unique_25) [page ] 43 | Treasury Specialist - Back Office | Enter Factor Values (TMDFACTORVAL) | Security factor values are entered. |
| [Import Market Data via File Upload](#unique_26) [page ] 47 | Treasury Specialist - Back Office | Import Market Data (F2610) | The data was imported and saved |
| [Market Data Overview](#unique_27) [page ] 56 | Treasury Risk Manager | Market Data Overview (F3941) | An overview of master data is displayed. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

The test should take around <Enter a duration, e.g. 60 minutes>.

### Manually Input Market Data

Purpose

This section describes how a user can manually input market data through Fiori Apps.

#### Enter FX Spot Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you enter the currency exchange spot rates manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Currency Exchange Rates (F3616). | The Currency Exchange Rates screen is displayed. |  |
| 3 | Add a New Record | Choose Create to enter a new record.As an example, enter a record with the following conditions:Exchange Rate Type: MFrom Currency: USDNote For US, input EUR.To Currency: AEDValid From: <first day of last month>Quotation: <choose Direct or Indirect>Maintain one of the following quotations according to the FX quotation convention (for example, for EURO countries and GB, you should maintain Indirect quotation), and choose Save:Exchange Rate: <enter a proper direct or indirect quoted exchange rate> | A new FX Spot Rate has been created. |  |

For NDF Transactions, you may need to add the following currency pair.

| Exchange Rate Type | From Currency | To | Valid From | Quotation | Exchange Rate |
| --- | --- | --- | --- | --- | --- |
| M | BRL | AED | <first day of last month> | Indirect | <Enter a proper indirect quoted exchange rate> |

#### Enter FX Swap Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you enter the currency exchange swap rates manually.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Enter FX Swap Rates (TMDFXFP). | The Display View "View Table AT15 - Swap Rates" Overview screen is displayed. |  |
| 3 | Add a New Record | Choose New Entries. |  |  |
| 4 | Add Rate Criteria | Make the following entries, and choose Save:Effective From: <for example, the first day of last month>Exchange Rate Types: MFrom: USDNote For US, input EUR.To: AEDTerm (Days): for example, 365Swap Rate: for example, <enter a proper swap rate> | The data is saved without error. |  |

|  |
| --- |
| Note For example, if you want to use Par Method, you must enter swap rate within 90 days (public holidays and weekend days are included). |

For NDF Transactions, you may need to add the following currency pair.

| Eff. From | Exchange Rate Type | From | To | Term(Days) | Swap rate |
| --- | --- | --- | --- | --- | --- |
| <the first day of last month> | M | AED | BRL | 365 | <enter a proper swap rate> |

#### Enter Exchange Rate Volatilities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you enter the exchange rate volatilities manually, if you use historical volatilities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Enter Exchange Rate Volatilities (JBVFX). | The Change View "Exchange rate volatilities": Overview view displays. |  |
| 3 | Add a New Record | Select New Entries and enter the following data:From: for example, AEDTo: for example, USDVolatility Type: 002Date: for example, <Current date>Note The entered date is equivalent to effective from.Term: for example, 360Volatility: for example, 28and select Save. | The data saves without an error. |  |

#### Assign Currency Pairs for Volatilities with Moneyness for Foreign Exchange Rate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step you assign volatility name to currency pairs if you use volatilities with moneyness. If you don’t assign volatility name to currency pairs, the evaluation type will use historical volatilities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Volatilities with Moneyness - Enter Values (TMDVOLANAME). |  |  |
| 3 | Add a New Volatility Name | Choose New Entries and enter the following data, and choose Save:Volatility Name: for example, SFX_USD_AED |  |  |
| 4 | Enter the parameters for the volatility structure | Choose the volatility name and choose Profile of Volatilities.Select New Entries and enter the following data:Volatility Profile: for example, SUSDAED_ATM_2WOption Term: for example, 14Moneyness Factor: for example, 0,5Note Continue to input other volatility parameters as listed in the table at the end of this step and choose Save. |  |  |
| 5 | Access the SAP Fiori App | Open Volatilities with Moneyness - Assign Currency Pairs (TMDAS_VOLANAME2FX). | The "Assign Currency Pair": Change view displays. |  |
| 6 | Add a New Record | Choose New Entries and enter the following data:From Currency: for example, USDTo Currency: for example, AEDVolatility Name: for example, SFX_USD_AEDchoose Save.Note If you don’t assign volatility name to currency pairs, evaluation type will use historical volatilities. | The data saves without an error. |  |

| Volatility Name | Volitality Profile | Option Term | Moneyness Factor |
| --- | --- | --- | --- |
| SFX_USD_AED | SUSDAED_ATM_2W | 14 | 0,5 |
| SFX_USD_AED | SUSDAED_ATM_3M | 90 | 0,5 |
| SFX_USD_AED | SUSDAED_ATM_6M | 180 | 0,5 |
| SFX_USD_AED | SUSDAED_ATM_9M | 270 | 0,5 |
| SFX_USD_AED | SUSDAED_ATM_18M | 540 | 0,5 |
| SFX_USD_AED | SUSDAED_25P_2W | 14 | -0,25 |
| SFX_USD_AED | SUSDAED_25P_3M | 90 | -0,25 |
| SFX_USD_AED | SUSDAED_25P_6M | 180 | -0,25 |
| SFX_USD_AED | SUSDAED_25P_9M | 270 | -0,25 |
| SFX_USD_AED | SUSDAED_25P_18M | 540 | -0,25 |
| SFX_USD_AED | SUSDAED_10P_2W | 14 | -0,1 |
| SFX_USD_AED | SUSDAED_10P_3M | 90 | -0,1 |
| SFX_USD_AED | SUSDAED_10P_6M | 180 | -0,1 |
| SFX_USD_AED | SUSDAED_10P_9M | 270 | -0,1 |
| SFX_USD_AED | SUSDAED_10P_18M | 540 | -0,1 |
| SFX_USD_AED | SUSDAED_10C_2W | 14 | 0,1 |
| SFX_USD_AED | SUSDAED_10C_3M | 90 | 0,1 |
| SFX_USD_AED | SUSDAED_10C_6M | 180 | 0,1 |
| SFX_USD_AED | SUSDAED_10C_9M | 270 | 0,1 |
| SFX_USD_AED | SUSDAED_10C_18M | 540 | 0,1 |
| SFX_USD_AED | SUSDAED_25C_2W | 14 | 0,25 |
| SFX_USD_AED | SUSDAED_25C_3M | 90 | 0,25 |
| SFX_USD_AED | SUSDAED_25C_6M | 180 | 0,25 |
| SFX_USD_AED | SUSDAED_25C_9M | 270 | 0,25 |
| SFX_USD_AED | SUSDAED_25C_18M | 540 | 0,25 |

|  |
| --- |
| Note Change the decimal separator according to your system behavior, for example, from commas "," to dots ".". |

#### Enter Values for Volatilities with Moneyness for Foreign Exchange Rate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you enter values for volatilities with moneyness. If you don’t enter volatilities with moneyness, even if you have assigned a volatility name to the currency pairs in the previous step, the evaluation type will use historical volatilities.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Volatilities with Moneyness - Enter Values (TMDVOLANAME). | The "Master Data and Market Data for Volatilities": Change view displays. |  |
| 3 | Choose a Volatility Name | Choose the volatility name which has been assigned to a currency pair in the previous step.Volatility Name: for example, SFX_USD_AED |  |  |
| 4 | Add New Records | Double click on the Volatilities folder on the left pane, then choose New Entries and enter the following data, and choose Save:Volatility Type: for example, 002Volatility Profile: for example, SUSDAED_ATM_2WVolatility Effective Date: fo example, <the current date>Volatility: for example, 7.310 | The New Entries: Details of Added Entries screen is displayed. |  |
| 5 | Repeat | Repeat the above steps to maintain the values given in the following table.Note The data given in the following table is just an example. You are recommended to enter the latest market data.If no volatilities with moneyness is entered, the evaluation type will adopt the historical volatilities.By default, Vanna-Volga Approximation is set in the predelivered evaluation types. Please shift to Fixed Point Iteration via configuration step Define and Set Up Evaluation Types > Volatility Smile Construction Method. However, this method works best if market data is available at 5% delta intervals.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |  |  |

| Effective Date | Volatility Type | Volatility Profile | Volatility |
| --- | --- | --- | --- |
| <the first day of last month> | 002 | SUSDAED_ATM_2W | 7.310 |
| <the first day of last month> | 002 | SUSDAED_ATM_3M | 6.853 |
| <the first day of last month> | 002 | SUSDAED_ATM_6M | 6.955 |
| <the first day of last month> | 002 | SUSDAED_ATM_9M | 7.243 |
| <the first day of last month> | 002 | SUSDAED_ATM_18M | 7.803 |
| <the first day of last month> | 002 | SUSDAED_25P_2W | 7.289 |
| <the first day of last month> | 002 | SUSDAED_25P_3M | 7.093 |
| <the first day of last month> | 002 | SUSDAED_25P_6M | 7.400 |
| <the first day of last month> | 002 | SUSDAED_25P_9M | 7.858 |
| <the first day of last month> | 002 | SUSDAED_25P_18M | 8.445 |
| <the first day of last month> | 002 | SUSDAED_10P_2W | 7.515 |
| <the first day of last month> | 002 | SUSDAED_10P_3M | 7.545 |
| <the first day of last month> | 002 | SUSDAED_10P_6M | 8.098 |
| <the first day of last month> | 002 | SUSDAED_10P_9M | 8.730 |
| <the first day of last month> | 002 | SUSDAED_10P_18M | 9.428 |
| <the first day of last month> | 002 | SUSDAED_10C_2W | 8.175 |
| <the first day of last month> | 002 | SUSDAED_10C_3M | 7.540 |
| <the first day of last month> | 002 | SUSDAED_10C_6M | 7.498 |
| <the first day of last month> | 002 | SUSDAED_10C_9M | 7.650 |
| <the first day of last month> | 002 | SUSDAED_10C_18M | 8.273 |
| <the first day of last month> | 002 | SUSDAED_25C_2W | 7.707 |
| <the first day of last month> | 002 | SUSDAED_25C_3M | 7.088 |
| <the first day of last month> | 002 | SUSDAED_25C_6M | 7.065 |
| <the first day of last month> | 002 | SUSDAED_25C_9M | 7.238 |
| <the first day of last month> | 002 | SUSDAED_25C_18M | 7.800 |

|  |
| --- |
| Note the volatility for every profile is just a sample data for internal testing. |

#### Assign Security Class for Volatilities with Moneyness for Securities Option

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you create the volatility name and profile for the underlying security class of a securities option transaction. The step below shows you how to create the volatility and volatility profile and assign them to the security class ST_AE1.

Prerequisite

You have created security class according to the relevant step described in the Stock Management(5OD) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Volatilities with Moneyness - Enter Values (TMDVOLANAME). |  |  |
| 3 | Add a New Volatility Name | Choose New Entries and enter the following data, and choose Save:Volatility Name: for example, ST_AE1_VOLText Field for Volatility Name: for example, Volatilities with Moneyness S/X for Securities |  |  |
| 4 | Enter the parameters for the volatility structure | Choose the checkbox before the Volatility Name ST_AE1_VOL and double-click to choose Profile of Volatilities.Choose New Entries and enter the following data on the New Entries: Added Entries screen:Volatility Profile: for example, 075_1MOption Term: for example, 30Moneyness Factor: for example, 0,75Note Continue to input other volatility parameters as listed in the table at the end of this step and choose Save. |  |  |
| 5 | Access the SAP Fiori App | Open Volatilities with Moneyness - Assign Securities ID (TMDAS_VOLANAME2CLASS). | The "Assign Security ID Number": Change screen is displayed. |  |
| 6 | Add a New Record | Choose New Entries and enter the following data:Sec. Class: for example, ST_AE1Volatility Name: for example, ST_AE1_VOLChoose Save. | The data saves without an error. |  |

| Volatility Name | Volitality Profile | Option Term | Moneyness Factor |
| --- | --- | --- | --- |
| ST_AE1_VOL | 075_1M | 30 | 0,75 |
| ST_AE1_VOL | 075_2M | 60 | 0,75 |
| ST_AE1_VOL | 125_1M | 30 | 1,25 |
| ST_AE1_VOL | 125_2M | 60 | 1,25 |
| ST_AE1_VOL | ATM_1M | 30 | 1,00 |
| ST_AE1_VOL | ATM_2M | 60 | 1,00 |

#### Enter Values for Volatilities with Moneyness for Securities Option

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this process step, you enter values for volatilities with moneyness for securities options. The step below shows you how to enter the value of the volatility for the security class ST_AE1.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Volatilities with Moneyness - Enter Values (TMDVOLANAME). | The "Master Data and Market Data for Volatilities": Change screen is displayed. |  |
| 3 | Choose a Volatility Name | Choose the checkbox before the Volatility Name ST_AE1_VOL. Double click on the Volatilities folder on the left pane. | The "Master Data and Market Data for Volatilities": Change screen is displayed. |  |
| 4 | Add New Records | Choose New Entries and enter the following data, and choose Save:Volatility Type: for example, 004Volatility Profile: for example, 075_1MVolatility Effective Date: fo example, <the current date>Volatility: for example, 7.310 | The New Entries: Details of Added Entries screen is displayed. |  |
| 5 | Repeat | Repeat the above steps to maintain the values given in the following table. |  |  |

| Effective Date | Volatility Type | Volatility Profile | Volatility |
| --- | --- | --- | --- |
| <the key date> | 004 | 075_1M | 7.310 |
| <the key date> | 004 | 075_2M | 10.310 |
| <the key date> | 004 | 125_1M | 8.310 |
| <the key date> | 004 | 125_2M | 11.310 |
| <the key date> | 004 | ATM_1M | 4.310 |
| <the key date> | 004 | ATM_2M | 6.310 |

#### Enter Interest Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter the reference interest rates manually.

|  |
| --- |
| Note You may need to add your own reference interest rate or update current reference interest rate according to your specific requirement before you enter market data via configuration step Define Reference Interest Rates. |

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

Option 1: Enter IBOR rates

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Enter Interest Rates (JBIRMC). | The Field Selection dialog box displays. |  |
| 3 | Field Selection | Choose Ref. Interest Rate in the dialog box. |  |  |
| 4 | Input Criteria in Determine Work Area: Entry | Leave all fields blank and choose Continue. | The Change View "Reference Interest Rate Values": Overview view displays. |  |
| 5 | Add a New Record | Select New Entries. | The New Entries: Overview of Added Entries view displays. |  |
| 6 | Enter Record Data and Save | Enter the following new data, and choose Save:Reference: for example, AEDM03EIBValid From: for example, <the first day of last month>Int. Rate: <enter a proper interest rate> | New Reference Interest Rate Values of local currency are saved. |  |
| 7 | Repeat Step 6 to Enter Record Data of Foreign Currency and Save | Enter the following new data, and choose Save:Reference: for example, USDM03LIBValid From: for example, <the first day of last month>Int. Rate: <enter a proper interest rate> | New Reference Interest Rate Values of foreign currency are saved. |  |

Option 2: Enter alternative RFRs

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Enter Interest Rates (JBIRMC). | The Field Selection dialog box displays. |  |
| 3 | Field Selection | Choose Ref. Interest Rate in the dialog box. |  |  |
| 4 | Input Criteria in Determine Work Area: Entry | Leave all fields blank and choose Continue. | The Change View "Reference Interest Rate Values": Overview view displays. |  |
| 5 | Add a New Record | Select New Entries. | The New Entries: Overview of Added Entries view displays. |  |
| 6 | Enter Record Data and Save | Enter the following new data, and choose Save:Reference: for example, SOFRValid From: for example, <the first day of last month>Int. Rate: <enter a proper interest rate> | New Reference Interest Rate Values are saved. |  |

Example

The following table gives reference interest rates (alternative RFRs) as an example. In real case, there should be no market data for alternative RFRs on the weekends. Please also adapt the days of last month accordingly.

Table 2: Reference Interest Rates (alternative RFRs)

| Reference | Valid From | Int. Rate |
| --- | --- | --- |
| SOFR | the first day of last month | 0.0455 |
| SOFR | the second day of last month | 0.0455 |
| SOFR | the third day of last month | 0.0455 |
| SOFR | the fourth day of last month | 0.0455 |
| SOFR | the fifth day of last month | 0.0455 |
| SOFR | the sixth day of last month | 0.0455 |
| SOFR | the seventh day of last month | 0.0455 |
| SOFR | the eighth day of last month | 0.0455 |
| SOFR | the ninth day of last month | 0.0455 |
| SOFR | the tenth day of last month | 0.0455 |
| SOFR | the eleventh day of last month | 0.0455 |
| SOFR | the twelfth day of last month | 0.0455 |
| SOFR | the thirteenth day of last month | 0.0455 |
| SOFR | the fourteenth day of last month | 0.0455 |
| SOFR | the fifteenth day of last month | 0.0454 |
| SOFR | the sixteenth day of last month | 0.0454 |
| SOFR | the seventeenth day of last month | 0.0454 |
| SOFR | the eighteenth day of last month | 0.0454 |
| SOFR | the nineteenth day of last month | 0.0454 |
| SOFR | the twentieth day of last month | 0.0454 |
| SOFR | the twenty-first day of last month | 0.0454 |
| SOFR | the twenty-second day of last month | 0.0454 |
| SOFR | the twenty-third day of last month | 0.0454 |
| SOFR | the twenty-fourth day of last month | 0.0454 |
| SOFR | the twenty-fifth day of last month | 0.0454 |
| SOFR | the twenty-sixth day of last month | 0.0454 |
| SOFR | the twenty-seventh day of last month | 0.0454 |
| SOFR | the twenty-eighth day of last month | 0.0454 |
| SOFR | the twenty-ninth day of last month | 0.0454 |
| SOFR | the thirtieth day of last month | 0.0454 |
| SOFR | the thirty-first day of last month | 0.0454 |
| SOFR | the first day of current month | 0.0453 |
| SOFR | the second day of current month | 0.0453 |
| SOFR | the third day of current month | 0.0453 |
| SOFR | the fourth day of current month | 0.0453 |
| SOFR | the fifth day of current month | 0.0453 |
| SOFR | the sixth day of current month | 0.0453 |
| SOFR | the seventh day of current month | 0.0453 |
| SOFR | the eighth day of current month | 0.0453 |
| SOFR | the ninth day of current month | 0.0453 |
| SOFR | the tenth day of current month | 0.0453 |
| SOFR | the eleventh day of current month | 0.0453 |
| SOFR | the twelfth day of current month | 0.0453 |
| SOFR | the thirteenth day of current month | 0.0453 |
| SOFR | the fourteenth day of current month | 0.0453 |
| SOFR | the fifteenth day of current month | 0.0453 |
| SOFR | the sixteenth day of current month | 0.0453 |
| SOFR | the seventeenth day of current month | 0.0453 |
| SOFR | the eighteenth day of current month | 0.0453 |
| SOFR | the nineteenth day of current month | 0.0453 |
| SOFR | the twentieth day of current month | 0.0453 |
| SOFR | the twenty-first day of current month | 0.0453 |
| SOFR | the twenty-second day of current month | 0.0452 |
| SOFR | the twenty-third day of current month | 0.0452 |
| SOFR | the twenty-fourth day of current month | 0.0452 |
| SOFR | the twenty-fifth day of current month | 0.0452 |
| SOFR | the twenty-sixth day of current month | 0.0452 |
| SOFR | the twenty-seventh day of current month | 0.0452 |
| SOFR | the twenty-eighth day of current month | 0.0452 |
| SOFR | the twenty-ninth day of current month | 0.0452 |
| SOFR | the thirtieth day of current month | 0.0452 |
| SOFR | the thirty-first day of current month | 0.0452 |

#### Enter Price Index Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you enter the price index values manually.

|  |
| --- |
| Note A generic index name CPI is predefined. You may define your own price index according to your specific requirement before you enter price index value via configuration activity Define Price Index.Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or via the configuration activity in the project experience of SAP Central Business Configuration. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Enter Price Index Values (TMDPRICEIDX). | The Determine Work Area: Entry view displays. |  |
| 3 | Input Name of Price Index in Determine Work Area: Entry | Choose CPI and choose Continue. | The Change View "Enter Price Index Values": Overview view displays. |  |
| 4 | Add a New Record | Select New Entries. | The New Entries: Overview of Added Entries view displays. |  |
| 5 | Enter Record Data and Save | Enter the following new data, and choose Save:Trans. Date: for example, <the first day of last month>Index val.: <enter a proper price index value>Continue to enter proper price index values for the first day of this month and the first day of next month. | New Price Index Values are saved. |  |

#### Check Yield Curves

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you check yield curves.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Yield Curves (JBYCN). | The Enter and Evaluate Yield Curves view is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data, and choose Overview:Yield Curve Type: 0001Currency: for example, AEDDate: for example, <Current date>Note The pre-delivered yield curve 0001 is defined with reference rate IBOR. You can also check the pre-delivered yield curve 9001 that is defined with alternative RFRs SOFR and ESTER. | The Yield Curve Overview view is displayed. |  |
| 4. | Review Yield Curve Detail | Double-click on a line to check the yield curve for one specific currency. | The Yield Curve: Details view is displayed. |  |

#### Create Reference Entities for Business Partners

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to create the reference entity for a business partner.

Prerequisites

A Business Partner (BP) has been created and maintained as a counterpart.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Create Reference Entities - Business Partners (RMREBP). | The Create Reference Entities for Business Partners view displays. |  |
| 3 | Test Run | Enter the following data:Business Partner: for example, 33537001BP Role: for example, TR0151Prefix for Ref.Ent.ID: for example, BP_Use in Credit Spread Curve: for example, <select this indicator>Credit Spread Curve (Bid): for example, Y001Credit Spread Curve (Ask): for example, Y001Credit Spread Curve (Middle): for example, Y001and choose Execute.Choose Continue from the Information dialog box to return to the Create Reference Entities for Business Partners view. | An Information dialog box displays with a 1 new entries inserted, 0 existing entries updated notification.Note No entry will be created if a reference entry has been created before. |  |

#### Assign Attributes to Evaluation Type

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you assign company code for the Evaluation Type to retrieve credit spreads.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options

Configure Your Solution:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. |  |  |
| 2 | Access App | Open Manage Your Solution (F1241). |  |  |
| 3 | Go to Configure Your Solution | Choose Configure Your Solution. |  |  |
| 4 | Go to Define and Set Up Evaluation Types | On the Configure Your Solution screen, search for the following configuration step: Define and Set Up Evaluation Types. Choose Configure | The Define and Set Up Evaluation Types screen is displayed. |  |
| 5 | Enter Data and Save | From the Evaluation Type column, select rows Y002 and Y003 and enter the following data, and Save:Default Company Code: for example, 3310 | Data is saved. |  |

SAP Central Business Configuration:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the project experience in SAP Central Business Configuration. |  |  |
| 2 | Open Active Flexible Workflow | Go to the Business Processes Configuration app and search for the following activity: Define and Set Up Evaluation Types.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The <Title of configuration step (SSCUI)> screen is displayed |  |
| 3 | Enter Data and Save | From the Evaluation Type column, select rows Y002 and Y003 and enter the following data, and Save:Default Company Code: for example, 3310 | Data is saved. |  |

#### Maintain Reference Entities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the reference entities list and create a Reference Entity for a Company Code.

Prerequisites

Before creating reference entities for company codes, ensure that the relevant Default Company Code has been assigned to an Evaluation Type, which uses credit spread curve.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Manage Reference Entities (RMRE). | The Change View "Reference Entities": Overview view displays. |  |
| 3 | Choose New Entries | Choose New Entries. | The New Entries: Details of Added Entries view displays. |  |
| 4 | Enter Parameters and Save | Enter the following data:Reference Entity: for example, CC_3310Name: for example, Company Code3310Company Code: for example, 3310Use in Curve: SelectedCredit Spread Curve (Bid): for example, Y001Credit Spread Curve (Ask): for example, Y001Credit Spread Curve (Middle): for example, Y001and choose Save. | Reference entity for Company Code is created and data is saved. |  |

#### Enter Credit Spreads

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to enter credit spreads for a Business Partner or own Company Code.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Enter Credit Spreads (RMCSM). | The Maintain Credit Spreads: Initial Screen displays. |  |
| 3 | Change View | Choose Change. | The New Entries: Overview of Added "Credit Spread Values" screen is displayed. |  |
| 4 | Display | Choose the Display button. | The Display View "Credit Spread Values": Overview view displays. |  |
| 5 | Edit | Choose the Edit button at the top right of the view. | The Change View "Credit Spread Values": Overview view displays. |  |
| 6 | New Entry | Choose New Entries | The New Entries: Overview of Added "Credit Spread Values" displays. |  |
| 7 | Enter New Credit Spreads for counterparty | Enter following data and Save.Reference Entity: for example, BP_0033537001Credit Spread ID: for example, YEAR_01Quot. Type: for example, 1Date: for example, <Current Date>Credit Spread (BP): for example, 100Note For Credit Spread Value in Basis Points, one basis point corresponds to a hundredth of a percentage point.Repeat these steps, using the data in the following tables additional Credit Spreads for Counterparty and for Credit Spreads for Own Company. |  |  |
| 8 | Enter New Entries for own company | On the Change View "Credit Spread Values": Overview screen, choose New Entries, enter following data:Reference Entity: for example, CC_3310CreditSpread ID: for example, MONTH_03Quotation Type: for example, 1Date: for example, <the current date>Credit Spread (BP): for example, 50Note For Credit Spread Value in Basis Points (BP), one basis point corresponds to a hundredth of a percentage point.and then Save. |  |  |

Sample Data

- Credit Spreads for Counterparty

|  |
| --- |
| Note Please change the Valid From value to 1st day of current month to accommodate later use of the data. |

| Reference Entity | CreditSpread ID | Quot. Type | First Day of Current Month | CreditSprd(BP): |
| --- | --- | --- | --- | --- |
| BP_0033537001 | MONTH_03 | 1 | <the first day of current month> | 100 |
| BP_0033537001 | MONTH_06 | 1 | <the first day of current month> | 150 |
| BP_0033537001 | MONTH_09 | 1 | <the first day of current month> | 200 |
| BP_0033537001 | YEAR_02 | 1 | <the first day of current month> | 400 |
| BP_0033537001 | YEAR_03 | 1 | <the first day of current month> | 500 |

- Credit Spreads for Own Company

|  |
| --- |
| Note Please change the Valid From value to 1st day of current month to accommodate later use of the data. |

| Reference Entity | CreditSpread ID | Quot. Type | Date | CreditSprd(BP): |
| --- | --- | --- | --- | --- |
| CC_3310 | MONTH_06 | 1 | <the first day of current month> | 200 |
| CC_3310 | MONTH_09 | 1 | <the first day of current month> | 300 |
| CC_3310 | YEAR_01 | 1 | <the first day of current month> | 400 |
| CC_3310 | YEAR_02 | 1 | <the first day of current month> | 500 |
| CC_3310 | YEAR_03 | 1 | <the first day of current month> | 550 |

#### Enter Basis Spreads

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to enter basis spreads.

|  |
| --- |
| Note You may need to add your own basis spreads or update current basis spreads according to your specific requirement via configuration step Define Basis Spreads before you enter market data. |

|  |
| --- |
| Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Enter Basis Spreads (RMBSM). | The Maintain Basis Spreads: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data:Basis Spread ID: for example, CBRLUSD1M01YTo: for example, TUSD6M3M05Yand choose the Change button. | The Change View "Credit Spread Values": Overview view displays. |  |
| 4 | Enter New Basis Spreads | Choose New Input Line and then enter the following dataBasis Spread ID: for example, TUSD1M3M01YQuotation Type: for example, 1Quotation Date: for example, <Current Date>Basic Spread (BP): for example, 8Note For Basis Spread Value in Basis Points (BP), one basis point corresponds to a hundredth of a percentage point.and choose Save. | The data is saved |  |
| 5 | Repeat | Repeat the steps using the values in the following table. | Additional Basic Spread IDs are entered and saved. |  |

Sample Data

- Basis Spreads

| Basis Spread ID | Quot. | Quotation Date | BasSpread(BP) |
| --- | --- | --- | --- |
| CBRLUSD1M01Y | 1 | Current Date | 12 |
| CEURUSD3M01Y | 1 | Current Date | 15 |
| TEUR6M3M01Y | 1 | Current Date | -10 |
| TUSD1M3M01Y | 1 | Current Date | 8 |
| TUSD6M3M01Y | 1 | Current Date | -18 |

#### Update Securities Price

##### Update Securities Price - Money Market Mutual Fund Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter the securities price.

Prerequisite

Securities Class MMF_AE1, MMF_AE2 and MMF_AE3 have been created according to the procedures described in the Money Market Mutual Fund Management(2UN) test script .

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Enter Securities Prices (FW17). | The Securities Price Edit: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data:ID Number: for example, MMF_AE1Exchange: for example, SMMFand choose Change. | The Security Price Change view displays. |  |
| 4 | Enter Price Criteria | Enter the following data:Price Date: for example, <current date>Price Type: SpotPrice / Rate: for example, 1.0002and choose Save. | Data is saved. |  |
| 5 | Enter Selection Criteria | Enter the following data:ID Number: for example, MMF_AE2Exchange: for example, SMMFand choose Change. | The Security Price Change view displays. |  |
| 6 | Enter Price Criteria | Enter the following data:Price Date: for example, <current date>Price Type: SpotPrice / Rate: for example, 1.0002and choose Save. | Data is saved. |  |
| 7 | Enter Selection Criteria | Enter the following data:ID number: for example, MMF_AE3Exchange: for example, SMMFand choose Change. | The Security Price Change view displays. |  |
| 8 | Enter Price Criteria | Enter the following data:Price Date: for example, <current date>Price Type: SpotPrice / Rate: for example, 1.0002and choose Save. | Data is saved. |  |

##### Update Securities Price - Bond Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter the securities price.

Prerequisite

Securities Class BD_AE1, BD_AE2, BD_AE3, BD_AE4, BD_AE5, BD_AE6 and IL_BD_AE7 have been created according to the procedures described in the Bond Management(3WY) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Enter Securities Prices (FW17). | The Securities Price Edit: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data:ID Number: for example, BD_AE1Exchange: for example, EURONEXT Pand choose Change. | The Security Price Change view displays. |  |
| 4 | Enter Price Criteria | Enter the following data:Price Date: for example, last date of current monthPrice Type: SpotPrice / Rate: for example, 99and choose Save. | Data is saved. |  |
| 5 | Enter Selection Criteria | Enter the following data:ID Number: for example, BD_AE2Exchange: for example, EURONEXT Pand choose Change. | The Security Price Change view displays. |  |
| 6 | Enter Price Criteria | Enter the following data:Price Date: for example, last date of current monthPrice Type: SpotPrice / Rate: for example, 99and choose Save. | Data is saved. |  |
| 7 | Enter Selection Criteria | Enter the following data:ID Number: for example, BD_AE3Exchange: for example, EURONEXT Pand choose Change. | The Security Price Change view displays. |  |
| 8 | Enter Price Criteria | Enter the following data:Price Date: for example, last date of current monthPrice Type: SpotPrice / Rate: for example, 99and choose Save. | Data is saved. |  |
| 9 | Enter Selection Criteria | Enter the following data:ID Number: for example, BD_AE4Exchange: for example, EURONEXT Pand choose Change. | The Security Price Change view displays. |  |
| 10 | Enter Price Criteria | Enter the following data:Price Date: for example, last date of current monthPrice Type: SpotPrice / Rate: for example, 99and choose Save. | Data is saved. |  |
| 11 | Enter Selection Criteria | Enter the following data:ID Number: for example, BD_AE5Exchange: for example, EURONEXT Pand choose Change. | The Security Price Change view displays. |  |
| 12 | Enter Price Criteria | Enter the following data:Price Date: for example, last date of current monthPrice Type: SpotPrice / Rate: for example, 99and choose Save. | Data is saved. |  |
| 13 | Enter Selection Criteria | Enter the following data:ID Number: for example, BD_AE6Exchange: for example, EURONEXT Pand choose Change. | The Security Price Change view displays. |  |
| 14 | Enter Price Criteria | Enter the following data:Price Date: for example, last date of current monthPrice Type: SpotPrice / Rate: for example, 99and choose Save. | Data is saved. |  |
| 15 | Enter Selection Criteria | Enter the following data:ID Number: for example, IL_BD_AE7Exchange: for example, OTCand choose Change. | The Security Price Change view displays. |  |
| 16 | Enter Price Criteria | Enter the following data:Price Date: for example, last date of current monthPrice Type: SpotPrice / Rate: for example, 99and choose Save. | Data is saved. |  |

##### Update Securities Price - Stock Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter the securities price for stock.

Prerequisite

You have created security class according to the relevant step described in the Stock Management(5OD) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Enter Securities Prices (FW17). | The Securities Price Edit: Initial Screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data:ID Number: for example, ST_AE1Exchange: for example, DFMand choose Change. | The Security Price Change view is displayed. |  |
| 4 | Enter Price Criteria | Enter the following data, and choose Save:Price Date: for example, <the current date>Price Type: SpotPrice / Rate: for example, 102 | Data is saved. |  |

##### Update Securities Price - Shareholding Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter the securities price for the shareholding.

Prerequisite

You have created security class according to the relevant step described in the Shareholding Management (5WF) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Enter Securities Prices (FW17). | The Securities Price Edit: Initial Screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following data:ID Number: for example, SH_AE1Exchange: for example, OTCand choose Change. | The Security Price Change view is displayed. |  |
| 4 | Enter Price Criteria | Enter the following data, and choose Save:Price Date: for example, <the current date>Price Type: SpotPrice / Rate: for example, 102 | Data is saved. |  |

##### Update Security Price - ABS/MBS Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you enter the securities price.

Prerequisite

Securities Class MBS_AE1 has been created according to the procedures described in the Asset-Backed Securities Management(6B5) test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Enter Securities Prices (FW17). | The Securities Price Edit: Initial Screen displays. |  |
| 3 | Enter Selection Criteria | Enter the following data:ID Number: for example, MBS_AE1Exchange: for example, OTCand choose Change. | The Security Price Change view displays. |  |
| 4 | Enter Price Criteria | Enter the following data:Price Date: for example, last date of last monthPrice Type: SpotPrice / Rate: for example, 99 | Data is saved. |  |
| 5 | Enter Price Criteria | Enter the following data:Price Date: for example, <current date>Price Type: SpotPrice / Rate: for example, 99and choose Save. | Data is saved. |  |

#### Enter Securities Factor Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to enter securities factor values.

Prerequisite

Securities Class MMF_AE1 , MMF_AE2 and MMF_AE3 have been created according to the instructions in the Money Market Mutual Fund Management2UN test script.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Enter Factor Values (TMDFACTORVAL) | The "Enter Factor Values": Change screen is displayed. |  |
| 3 | Enter the New Factor Values and Save the Change | Choose New Entries and enter the following data:Record 1Security Class: for example, MMF_AE1Factor Type: for example, SM_FACTOREffective From: <last day of current month>Factor Values: for example, 0.001226122Record 2Security Class: for example, MMF_AE2Factor Type: for example,SD_FACTOREffective From: for example, <the current date>Factor Values: for example, 0.000040014Record 3Security Class: for example, MMF_AE3Factor Type: for example, SD_FACTOREffective From: for example, <the current date>Factor Values: for example, 0.000040014and choose Save. | The Security Price Change screen is displayed. |  |

Please create the Factor Values using the following table. You can also choose to import the market data by a file upload.

|  |
| --- |
| Note The Effective Date(YYYYMMDD) in following form is just an example. In order to make Capitalize Dividend Distribution work, the Effective Date should be same or from date of security purchase transaction. |

| Market Data Category | ID Number | Factor Type | Effective Date (YYYYMMDD) | Dividend Factor |
| --- | --- | --- | --- | --- |
| 41 | MMF_AE1 | SM_FACTOR | 20180331 | 0.001226122 |
| 41 | MMF_AE2 | SD_FACTOR | 20180301 | 0.000040014 |
| 41 | MMF_AE2 | SD_FACTOR | 20180302 | 0.000040196 |
| 41 | MMF_AE2 | SD_FACTOR | 20180303 | 0.000040177 |
| 41 | MMF_AE2 | SD_FACTOR | 20180304 | 0.000040188 |
| 41 | MMF_AE2 | SD_FACTOR | 20180305 | 0.000040188 |
| 41 | MMF_AE2 | SD_FACTOR | 20180306 | 0.000040187 |
| 41 | MMF_AE2 | SD_FACTOR | 20180307 | 0.000039978 |
| 41 | MMF_AE2 | SD_FACTOR | 20180308 | 0.000040168 |
| 41 | MMF_AE2 | SD_FACTOR | 20180309 | 0.000040137 |
| 41 | MMF_AE2 | SD_FACTOR | 20180310 | 0.00004009 |
| 41 | MMF_AE2 | SD_FACTOR | 20180311 | 0.000040077 |
| 41 | MMF_AE2 | SD_FACTOR | 20180312 | 0.000040077 |
| 41 | MMF_AE2 | SD_FACTOR | 20180313 | 0.000040076 |
| 41 | MMF_AE2 | SD_FACTOR | 20180314 | 0.000039783 |
| 41 | MMF_AE2 | SD_FACTOR | 20180315 | 0.000039772 |
| 41 | MMF_AE2 | SD_FACTOR | 20180316 | 0.000039803 |
| 41 | MMF_AE2 | SD_FACTOR | 20180317 | 0.000039331 |
| 41 | MMF_AE2 | SD_FACTOR | 20180318 | 0.000039331 |
| 41 | MMF_AE2 | SD_FACTOR | 20180319 | 0.000039331 |
| 41 | MMF_AE2 | SD_FACTOR | 20180320 | 0.000039331 |
| 41 | MMF_AE2 | SD_FACTOR | 20180321 | 0.000039243 |
| 41 | MMF_AE2 | SD_FACTOR | 20180322 | 0.000039167 |
| 41 | MMF_AE2 | SD_FACTOR | 20180323 | 0.000039083 |
| 41 | MMF_AE2 | SD_FACTOR | 20180324 | 0.000038902 |
| 41 | MMF_AE2 | SD_FACTOR | 20180325 | 0.000038657 |
| 41 | MMF_AE2 | SD_FACTOR | 20180326 | 0.000038656 |
| 41 | MMF_AE2 | SD_FACTOR | 20180327 | 0.000038656 |
| 41 | MMF_AE2 | SD_FACTOR | 20180328 | 0.000038539 |
| 41 | MMF_AE2 | SD_FACTOR | 20180329 | 0.000039237 |
| 41 | MMF_AE2 | SD_FACTOR | 20180330 | 0.000038784 |
| 41 | MMF_AE2 | SD_FACTOR | 20180331 | 0.000038963 |
| 41 | MMF_AE3 | SD_FACTOR | 20180301 | 0.000040014 |
| 41 | MMF_AE3 | SD_FACTOR | 20180302 | 0.000040196 |
| 41 | MMF_AE3 | SD_FACTOR | 20180303 | 0.000040177 |
| 41 | MMF_AE3 | SD_FACTOR | 20180304 | 0.000040188 |
| 41 | MMF_AE3 | SD_FACTOR | 20180305 | 0.000040188 |
| 41 | MMF_AE3 | SD_FACTOR | 20180306 | 0.000040187 |
| 41 | MMF_AE3 | SD_FACTOR | 20180307 | 0.000039978 |
| 41 | MMF_AE3 | SD_FACTOR | 20180308 | 0.000040168 |
| 41 | MMF_AE3 | SD_FACTOR | 20180309 | 0.000040137 |
| 41 | MMF_AE3 | SD_FACTOR | 20180310 | 0.00004009 |
| 41 | MMF_AE3 | SD_FACTOR | 20180311 | 0.000040077 |
| 41 | MMF_AE3 | SD_FACTOR | 20180312 | 0.000040077 |
| 41 | MMF_AE3 | SD_FACTOR | 20180313 | 0.000040076 |
| 41 | MMF_AE3 | SD_FACTOR | 20180314 | 0.000039783 |
| 41 | MMF_AE3 | SD_FACTOR | 20180315 | 0.000039772 |
| 41 | MMF_AE3 | SD_FACTOR | 20180316 | 0.000039803 |
| 41 | MMF_AE3 | SD_FACTOR | 20180317 | 0.000039331 |
| 41 | MMF_AE3 | SD_FACTOR | 20180318 | 0.000039331 |
| 41 | MMF_AE3 | SD_FACTOR | 20180319 | 0.000039331 |
| 41 | MMF_AE3 | SD_FACTOR | 20180320 | 0.000039331 |
| 41 | MMF_AE3 | SD_FACTOR | 20180321 | 0.000039243 |
| 41 | MMF_AE3 | SD_FACTOR | 20180322 | 0.000039167 |
| 41 | MMF_AE3 | SD_FACTOR | 20180323 | 0.000039083 |
| 41 | MMF_AE3 | SD_FACTOR | 20180324 | 0.000038902 |
| 41 | MMF_AE3 | SD_FACTOR | 20180325 | 0.000038657 |
| 41 | MMF_AE3 | SD_FACTOR | 20180326 | 0.000038656 |
| 41 | MMF_AE3 | SD_FACTOR | 20180327 | 0.000038656 |
| 41 | MMF_AE3 | SD_FACTOR | 20180328 | 0.000038539 |
| 41 | MMF_AE3 | SD_FACTOR | 20180329 | 0.000039237 |
| 41 | MMF_AE3 | SD_FACTOR | 20180330 | 0.000038784 |
| 41 | MMF_AE3 | SD_FACTOR | 20180331 | 0.000038963 |

### Import Market Data via File Upload

#### Import Market Data via File Upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you import market data via file upload.

Authorization control is allowed on exchange rate type when import exchange rates (category 01) or swap rates (category 21) into S/4HANA by using App Import Market Data (F2610). You can maintain restrictions by App Maintain Business Roles (F1492) with user ADMINISTRATOR.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Specialist - Back Office. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Import Market Data (F2610). | The Import Market Data screen is displayed. |  |
| 3 | Choose to Download a Template | Choose Download Template from the bottom of the view. | The Download Template dialog box is displayed. |  |
| 4 | Select Template to Download | Enter selection criteria and choose Download:Category Selection： Exchange RatesData Selection: for example, With Master DataFormat Selection: for example, Category-Specific FilesNote Repeat the step for other market data categories, for example Interest Rates, Credit Spreads, and so on, as described in the following table. | The template is downloaded. |  |
| 5 | Complete the Template and Upload | Fill in the required information for the template and then upload.Note You must provide Market Data Category in the first column in the template files. Refer to the Market Data Category List and Apps table below for the values to enter. | The Validation of Exchange Rates subarea displays. |  |
| 6 | Confirm Messages and Import | Confirm the messages, and if no further changes are required, select Import. | The rates import without error. |  |
| 7 | Confirm the Imported Data as Available | Open the manual input app to confirm that the correct data was imported.Refer to the Market Data Category List and Apps table below to find the corresponding apps. | The imported data can be found. |  |

Market Data Category List and Apps

| Name | Category | Apps |
| --- | --- | --- |
| Exchange Rates | 01 | Currency Exchange Rates (F3616) |
| Update Securities Price | 02 | Enter Securities Prices (FW17) |
| Interest Rates | 03 | Enter Interest Rates (JBIRMC) |
| Basis Spreads | 09 | Enter Basis Spreads (RMBSM) |
| Credit Spreads | 10 | Enter Credit Spreads (RMCSM) |
| Forex Swap Rates | 21 | Enter FX Swap Rates (TMDFXFP) |
| Implied Volatilities | 30 | Volatilities with Moneyness - Enter Values (TMDVOLANAME) |
| Exchange Rate Volatility | 31 | Enter Exchange Rate Volatilities (JBVFX) |
| Security Dividend Factors | 41 | Enter Factor Values (TMDFACTORVAL) |

Sample Data

For testing purposes, you can use the following data. Copy this test data into the downloaded template, adapt the data in accordance with your business requirements.

Exchange Rates

| Market Data Category | From Currency | To Currency | Exchange Rate Type | Date (YYYYMMDD) | Exchange Rate | From Factor | To Factor | Price Quotation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | USD | AED | M | <the fist day of last month> | <enter a proper rate> | 1 | 1 | X |
| 01 | BRL | AED | M | <the fist day of last month> | <enter a proper rate> | 1 | 1 | X |

|  |
| --- |
| Note For the Price Quotation field, input X to indicate indirect quotation, or leave it blank to indicate direct quotation. |

- Forex Swap Rates

| Market Data Category | From Currency | To Currency | Exchange Rate Type | Effective From Date (YYYYMMDD) | Term (Days) | Forex Swap Rate |
| --- | --- | --- | --- | --- | --- | --- |
| 21 | AED | USD | M | <the fist day of last month> | 360 | <enter a proper rate> |
| 21 | AED | BRL | M | <the fist day of last month> | 360 | <enter a proper rate> |

- Exchange Rate Volatilities

| Market Data Category | From Currency | To Currency | Volatility Type | Effective From Date (YYYYMMDD) | Term | Volatility |
| --- | --- | --- | --- | --- | --- | --- |
| 31 | AED | USD | 002 | <the fist day of last month> | 180 | 26 |
| 31 | AED | USD | 002 | <the fist day of last month> | 360 | 28 |

- Implied Volatilities

| Market Data Category | Volatility Name | Volatility Profile | VTyp | Effective Date | Volatility |
| --- | --- | --- | --- | --- | --- |
| 30 | SFX_USD_AED | SUSDAED_ATM_2W | 002 | <the fist day of last month> | 7.310 |
| 30 | SFX_USD_AED | SUSDAED_ATM_3M | 002 | <the fist day of last month> | 6.853 |
| 30 | SFX_USD_AED | SUSDAED_ATM_6M | 002 | <the fist day of last month> | 6.955 |
| 30 | SFX_USD_AED | SUSDAED_ATM_9M | 002 | <the fist day of last month> | 7.243 |
| 30 | SFX_USD_AED | SUSDAED_ATM_18M | 002 | <the fist day of last month> | 7.803 |
| 30 | SFX_USD_AED | SUSDAED_25P_2W | 002 | <the fist day of last month> | 7.289 |
| 30 | SFX_USD_AED | SUSDAED_25P_3M | 002 | <the fist day of last month> | 7.093 |
| 30 | SFX_USD_AED | SUSDAED_25P_6M | 002 | <the fist day of last month> | 7.400 |
| 30 | SFX_USD_AED | SUSDAED_25P_9M | 002 | <the fist day of last month> | 7.858 |
| 30 | SFX_USD_AED | SUSDAED_25P_18M | 002 | <the fist day of last month> | 8.445 |
| 30 | SFX_USD_AED | SUSDAED_10P_2W | 002 | <the fist day of last month> | 7.515 |
| 30 | SFX_USD_AED | SUSDAED_10P_3M | 002 | <the fist day of last month> | 7.545 |
| 30 | SFX_USD_AED | SUSDAED_10P_6M | 002 | <the fist day of last month> | 8.098 |
| 30 | SFX_USD_AED | SUSDAED_10P_9M | 002 | <the fist day of last month> | 8.730 |
| 30 | SFX_USD_AED | SUSDAED_10P_18M | 002 | <the fist day of last month> | 9.428 |
| 30 | SFX_USD_AED | SUSDAED_10C_2W | 002 | <the fist day of last month> | 8.175 |
| 30 | SFX_USD_AED | SUSDAED_10C_3M | 002 | <the fist day of last month> | 7.540 |
| 30 | SFX_USD_AED | SUSDAED_10C_6M | 002 | <the fist day of last month> | 7.498 |
| 30 | SFX_USD_AED | SUSDAED_10C_9M | 002 | <the fist day of last month> | 7.650 |
| 30 | SFX_USD_AED | SUSDAED_10C_18M | 002 | <the fist day of last month> | 8.273 |
| 30 | SFX_USD_AED | SUSDAED_25C_2W | 002 | <the fist day of last month> | 7.707 |
| 30 | SFX_USD_AED | SUSDAED_25C_3M | 002 | <the fist day of last month> | 7.088 |
| 30 | SFX_USD_AED | SUSDAED_25C_6M | 002 | <the fist day of last month> | 7.065 |
| 30 | SFX_USD_AED | SUSDAED_25C_9M | 002 | <the fist day of last month> | 7.238 |
| 30 | SFX_USD_AED | SUSDAED_25C_18M | 002 | <the fist day of last month> | 7.800 |

Interest Rates

| Market Data Category | Reference Interest Rate | Date (YYYYMMDD) | Interest Rate |
| --- | --- | --- | --- |
| 03 | EURD01EUR | <the fist day of last month> | -0.4240 |
| 03 | EURD07EUR | <the fist day of last month> | -0.2560 |
| 03 | EURD14EUR | <the fist day of last month> | -0.1660 |
| 03 | EURM01EUR | <the fist day of last month> | 0.0640 |
| 03 | EURM02EUR | <the fist day of last month> | 0.2240 |
| 03 | EURM03EUR | <the fist day of last month> | 0.4040 |
| 03 | EURM04EUR | <the fist day of last month> | 0.6640 |
| 03 | EURM05EUR | <the fist day of last month> | 0.8340 |
| 03 | EURM06EUR | <the fist day of last month> | 0.9940 |
| 03 | EURM07EUR | <the fist day of last month> | 0.3540 |
| 03 | EURM08EUR | <the fist day of last month> | 0.4240 |
| 03 | EURM09EUR | <the fist day of last month> | 0.5940 |
| 03 | EURM10EUR | <the fist day of last month> | 0.7840 |
| 03 | EURM11EUR | <the fist day of last month> | 0.9640 |
| 03 | EURM12EUR | <the fist day of last month> | 1.2440 |
| 03 | EURM18EUR | <the fist day of last month> | 1.3440 |
| 03 | EURY02S6E | <the fist day of last month> | 1.4340 |
| 03 | EURY03S6E | <the fist day of last month> | 1.7240 |
| 03 | EURY04S6E | <the fist day of last month> | 1.7440 |
| 03 | EURY05S6E | <the fist day of last month> | 1.9180 |
| 03 | EURY06S6E | <the fist day of last month> | 2.1100 |
| 03 | EURY07S6E | <the fist day of last month> | 2.3210 |
| 03 | EURY08S6E | <the fist day of last month> | 2.5530 |
| 03 | EURY09S6E | <the fist day of last month> | 2.8090 |
| 03 | EURY10S6E | <the fist day of last month> | 3.0900 |
| 03 | EURY11S6E | <the fist day of last month> | 3.3990 |
| 03 | EURY12S6E | <the fist day of last month> | 3.6990 |
| 03 | EURY15S6E | <the fist day of last month> | 3.9990 |
| 03 | EURY20S6E | <the fist day of last month> | 4.2990 |
| 03 | EURY25S6E | <the fist day of last month> | 4.5990 |
| 03 | EURY30S6E | <the fist day of last month> | 4.8990 |
| 03 | EURY35S6E | <the fist day of last month> | 5.1990 |
| 03 | EURY40S6E | <the fist day of last month> | 5.4990 |
| 03 | USDD01LIB | <the fist day of last month> | 0.9300 |
| 03 | USDD02DEP | <the fist day of last month> | 1.0200 |
| 03 | USDD07LIB | <the fist day of last month> | 1.0400 |
| 03 | USDD14LIB | <the fist day of last month> | 0.9800 |
| 03 | USDM01LIB | <the fist day of last month> | 1.1100 |
| 03 | USDM02LIB | <the fist day of last month> | 1.2600 |
| 03 | USDM03LIB | <the fist day of last month> | 1.3400 |
| 03 | USDM04LIB | <the fist day of last month> | 1.4100 |
| 03 | USDM05LIB | <the fist day of last month> | 1.4900 |
| 03 | USDM06LIB | <the fist day of last month> | 1.5400 |
| 03 | USDM07LIB | <the fist day of last month> | 1.5900 |
| 03 | USDM08LIB | <the fist day of last month> | 1.6500 |
| 03 | USDM09LIB | <the fist day of last month> | 1.7000 |
| 03 | USDM10LIB | <the fist day of last month> | 1.7500 |
| 03 | USDM11LIB | <the fist day of last month> | 1.8100 |
| 03 | USDM12USA | <the fist day of last month> | 1.4100 |
| 03 | USDY02USA | <the fist day of last month> | 1.5000 |
| 03 | USDY03USA | <the fist day of last month> | 1.6900 |
| 03 | USDY04USA | <the fist day of last month> | 1.9000 |
| 03 | USDY05USA | <the fist day of last month> | 2.1300 |
| 03 | USDY06USA | <the fist day of last month> | 2.3200 |
| 03 | USDY07USA | <the fist day of last month> | 2.4800 |
| 03 | USDY08USA | <the fist day of last month> | 2.6100 |
| 03 | USDY09USA | <the fist day of last month> | 2.7100 |
| 03 | USDY10USA | <the fist day of last month> | 3.0800 |
| 03 | USDY11USA | <the fist day of last month> | 3.2000 |
| 03 | BRLD01SWP | <the fist day of last month> | 9.3200 |
| 03 | BRLM01SWP | <the fist day of last month> | 9.4400 |
| 03 | BRLM02SWP | <the fist day of last month> | 9.4900 |
| 03 | BRLM03SWP | <the fist day of last month> | 9.5257 |
| 03 | BRLM04SWP | <the fist day of last month> | 10.0457 |
| 03 | BRLM06SWP | <the fist day of last month> | 10.4830 |
| 03 | BRLY01SWP | <the fist day of last month> | 10.8408 |
| 03 | BRLY02SWP | <the fist day of last month> | 11.7350 |
| 03 | BRLY03SWP | <the fist day of last month> | 12.1510 |
| 03 | BRLY04SWP | <the fist day of last month> | 12.3259 |
| 03 | BRLY05SWP | <the fist day of last month> | 12.4016 |

Security Prices

If you use 2UN, you may import security prices as in the following table.

As prerequisite, you should create security classes as described in the Money Market Mutual Fund Management(2UN) test script.

| Market Data Category | ID number | Exchange | Price Type | Price Date (YYYYMMDD) | Price of Unit | Quot.curr. |
| --- | --- | --- | --- | --- | --- | --- |
| 02 | MMF_AE1 | SMMF | 09 | <the fist day of last month> | 1 | AED |
| 02 | MMF_AE2 | SMMF | 09 | <the fist day of last month> | 1.0002 | AED |
| 02 | MMF_AE3 | SMMF | 09 | <the fist day of last month> | 1.0002 | AED |

If you use 3WY, you may import security prices as in the following table.

As prerequisite, you should create security classes as described in the Bond Management3WY test script.

| Market Data Category | ID number | Exchange | Price Type | Price Date (YYYYMMDD) | Price of Unit | Quot.curr. |
| --- | --- | --- | --- | --- | --- | --- |
| 02 | BD_AE1 | EURONEXT P | 01 | <the fist day of last month> | 99 | AED |
| 02 | BD_AE2 | EURONEXT P | 01 | <the fist day of last month> | 99 | AED |
| 02 | BD_AE3 | EURONEXT P | 01 | <the fist day of last month> | 99 | AED |
| 02 | BD_AE4 | EURONEXT P | 01 | <the fist day of last month> | 99 | AED |
| 02 | BD_AE5 | EURONEXT P | 01 | <the fist day of last month> | 99 | AED |

Security Dividends Factors

If you are managing money market fund in the system, to update the dividends, you may need to import the security dividends factors. Sample data is provided in the following table.

As the prerequisite, you should first create security classes as described in the 2UN test script.

| Market Data Category | ID Number | Factor Type | Effective Date (YYYYMMDD) | Dividend Factor |
| --- | --- | --- | --- | --- |
| 41 | MMF_AE1 | SM_FACTOR | <the fist day of last month> | 0.001226122 |
| 41 | MMF_AE2 | SD_FACTOR | <the fist day of last month> | 0.000040014 |

|  |
| --- |
| Note SM_FACTOR is the predefined monthly dividend factor, and SD_FACTOR is the predefined daily dividend factor.For SD_FACTOR, continue to maintain dividend factor for every single day of the last month. |

### Report

#### Market Data Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Display market data for review.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as Treasury Risk Manager. | The SAP Fiori Launchpad is displayed. |  |
| 2 | Access the SAP Fiori App | Open Market Data Overview (F3941). | The Market Data Overview screen is displayed. |  |
| 3 | Enter Selection Criteria | Enter the following selection criteria:Key Data: for example, <the current date>Exchange Rate Type: for example, MPrice Type: for example, 01Currency Pair: for example, AED/USDReference Interest Rate: for example, AEDM03EIB | The Cards of Historic FX Spot Rate, FX Spot Rate, FX Swap Rate, Historic Security Price, Current Security Price are displayed per the filter values. |  |

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
- related-to :: [[05-treasury-and-cash-management/automatic-market-rates-management-1s4-ae-test-script-762]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1XN_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 83,319 chars in the whole document
