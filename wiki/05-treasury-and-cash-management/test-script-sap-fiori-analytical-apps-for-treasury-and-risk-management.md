---
id: 05-treasury-and-cash-management/test-script-sap-fiori-analytical-apps-for-treasury-and-risk-management
title: "Test Script: SAP Fiori Analytical Apps for Treasury and Risk Management (1MN) (1MN_S4CLD2608_BPD_EN_XX)"
description: "Test script for SAP S/4HANA Cloud scope item 1MN: Foreign Exchange Overview (F2331) and Treasury Executive Dashboard (F4316), eight tabstrips."
cluster: 05-treasury-and-cash-management
tags: [kb/treasury-and-cash-management, topic/treasury-analytics]
aliases: [1MN_S4CLD2608_BPD_EN_XX]
keywords: [Treasury Analytics and Executive Dashboard, test scripts, treasury analytics, foreign exchange overview, treasury executive dashboard, liquidity analytics, cash management, bank relationship, indebtedness, counterparty risk]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MN_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-737
topic: 05-treasury-and-cash-management/treasury-analytics
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP Fiori Analytical Apps for Treasury and Risk Management (1MN) (1MN_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MN_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Treasury Analytics and Executive Dashboard** in Treasury and Cash Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Fiori Analytical Apps for Treasury and Risk Management (1MN) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 2](#_Toc232849938)

[2 Prerequisites 3](#_Toc232849939)

[2.1 System Access 3](#_Toc232849940)

[2.2 Roles 3](#_Toc232849941)

[2.3 Business Conditions 3](#_Toc232849942)

[3 Overview Table 5](#_Toc232849943)

[4 Test Procedures 6](#_Toc232849944)

[4.1 Foreign Exchange Overview Page 6](#_Toc232849945)

[4.2 Treasury Executive Dashboard 8](#_Toc232849946)

[4.2.1 Story Tabstrip: Liquidity 9](#_Toc232849947)

[4.2.2 Story Tabstrip: Cash Management 11](#_Toc232849948)

[4.2.3 Story Tabstrip: Bank Relationship 13](#_Toc232849949)

[4.2.4 Story Tabstrip: Indebtedness 16](#_Toc232849950)

[4.2.5 Story Tabstrip: Counterparty Risk 18](#_Toc232849951)

[4.2.6 Story Tabstrip: Market Risk 20](#_Toc232849952)

[4.2.7 Story Tabstrip: Bank Guarantee 21](#_Toc232849953)

[4.2.8 Story Tabstrip: Market Overview 23](#_Toc232849954)

## Purpose

Overview

This scope item provides an overview page for the treasury and risk management related scenarios. The Foreign Exchange Overview page focuses on the financial status, foreign exchange rates, and so on, and how this can be visualized for to allow for better decision making by the treasury managers.

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
| Treasury Risk Manager | SAP_BR_TREASURY_RISK_MANAGER | Treasury Analytics | SAP_BR_TREASURY_RISK_MANAGER |  |

### Business Conditions

Follow the procedures described in the following scope items for creating the corresponding business data if needed.

| Scope Item ID | Business Condition |
| --- | --- |
| 1X1 - Foreign Currency Risk Management | Follow the scope item to create the corresponding business data. |
| 1X9 - Foreign Currency Risk Management – Group Ledger IFRS | Follow the scope item to create the corresponding business data. |
| 2F2 - Intercompany Foreign Exchange Management | Follow the scope item to create the corresponding business data. |
| 2HU - Intercompany Foreign Exchange – Group Ledger IFRS | Follow the scope item to create the corresponding business data. |
| 1XD - Hedge Accounting for FX Forward – Group Ledger IFRS | Follow the scope item to create the corresponding business data. |
| 1XN - Market Rates Management – Manually via Upload | Follow the scope item to create the corresponding business data. |
| 1S4 - Automatic Market Rates Management | Follow the scope item to create the corresponding business data. |
| 1WV - Debt and Investment Management | Follow the scope item to create the corresponding business data. |
| 1X1 - Foreign Currency Risk Management | Follow the scope item to create the corresponding business data. |
| 1X3 - Interest Rate Derivatives Management | Follow the scope item to create the corresponding business data. |
| 2NZ - Bank Guarantee Management | Follow the scope item to create the corresponding business data. |
| 3WY - Bond Management | Follow the scope item to create the corresponding business data. |
| BFB- Basic Cash Operations | Follow the scope item to create the corresponding business data. |
| J78 - Advanced Cash Operations | Follow the scope item to create the corresponding business data. |
| 2UN - Money Market Mutual Fund Management | Follow the scope item to create the corresponding business data. |
| 49D - Letter of Credit Management | Follow the scope item to create the corresponding business data. |

Follow the procedures described below for additional business configuration points if needed.

[Finance > Treasury Management > Treasury Analytics > Treasury Executive Dashboard > Configuration and Master Data for the Treasury Executive Dashboard](https://help.sap.com/s4_ce_fin)

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Foreign Exchange Overview Page](#unique_7) [page ] 6 | Treasury Risk Manager | Foreign Exchange Overview (F2331) | The SAP Fiori overview page is running correctly. |
| [Treasury Executive Dashboard](#unique_8) [page ] 8 | Treasury Risk Manager | Treasury Executive Dashboard (F4316) | The SAP Fiori overview page is running correctly. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Foreign Exchange Overview Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You have already implemented Foreign Exchange Overview. Please check if it is running correctly.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Risk Manager . | The SAP Fiori launchpad is displayed. |  |
| 2 | Set Default Value for SAP Fiori Launchpad User Setting (Optional) | On the SAP Fiori launchpad, choose User > Settings > Default Values . | The following input fields are available:Company CodeExchange Rate TypeDisplay CurrencyYou can enter and save default values. |  |
| 3 | Access the App | Open Foreign Exchange Overview (F2331) . Enter the following required information in the filter bar:Company CodeKey DateExchange Rate TypeDisplay CurrencyTransaction CurrencyAfterwards, choose Go.If a default value has been set in the SAP Fiori launchpad user settings, the filters have been automatically populated with the default values. | The overview page is launched successfully and the following cards are displayed (the exact names may vary):Credit line OverviewFX Instruments (FX Forwards)FX Instruments (FX Options)FX Instruments (FX Non Deliverable Forwards)Foreign Exchange RateLiquidity Forecast (with Drop Down List: Next 6 Months, Next 3 Months)Cash PositionAbsolute FX Net ExposureNote Financial Status (with Drop Down List: Book Value, Nominal Amount) is hidden by default, ask key user with role(SAP_UI_FLEX_KEY_USER) to add this card via "Adapt UI" function if there is need |  |
| 4 | Set Global Filters | The global filters can be changed in the global filter bar. Set the values in the fields of the global filter, choose Go, and the overview page refreshes content. | The global filter is applied to the results of the cards on the overview page. |  |
| 5 | Manage Cards | To customize the cards on the overview page, choose the user icon on the screen, choose Manage Cards, make the settings of your choice, and then choose OK. | The cards on the overview page can be rearranged, hidden, and displayed again. |  |
| 6 | Navigate from Card Financial Status (In case key user added card) | Navigate from Financial Status and choose the header (or chart data point) of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (and data point) information is carried over.If you select Book Value Amount from the dropdown list, the card navigates to the Financial Status – Book Value SAP Fiori app.If you select Nominal Amount from the dropdown list, the card navigates to the Financial Status – Nominal Amount SAP Fiori app. |  |
| 7 | Navigate from Card FX Instruments (FX Forwards) | Navigate from FX Instruments (FX Forwards).Choose the header (or line item) of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (and line item) information is carried over.The card navigates you to the Process Spots / Forwards Collective Processing SAP Fiori app. |  |
| 8 | Navigate from Card FX Instruments (FX Options) | Navigate from FX Instruments (FX Options).Choose the header (or line item) of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (and line item) information is carried over.The card navigates to the Process Spots / Forwards Collective Processing SAP Fiori app. |  |
| 9 | Navigate from Card FX Instruments (FX Non-Deliverable Forwards) | Navigate from FX Instruments (FX Non Deliverable Forwards).Choose the header (or line item) of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (and line item) information is carried over.The card navigates you to the Process Spots / Forwards Collective Processing SAP Fiori app. |  |
| 10 | Navigate from Card Foreign Exchange Rate | Navigate from Foreign Exchange Rate.Choose the header (or line item) of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (and line item) information is carried over.The card navigates you to the Currency Converter SAP Fiori app. |  |
| 11 | Navigate from Card Absolute FX Net Exposure | Navigate from Absolute FX Net Exposure.Choose the line item of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (and line item) information is carried over.The card navigates you to the Review Balance Sheet FX Risk SAP Fiori app. |  |

### Treasury Executive Dashboard

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You have already implemented Treasury Executive Dashboard. Please check if it is running correctly.

The SAP Treasury Executive Dashboard includes analytic tabs from different management perspectives.

Table 1:

| Tab# | Tab Name |
| --- | --- |
| 1 | Liquidity |
| 2 | Cash Management |
| 3 | Bank Relationship |
| 4 | Indebtedness |
| 5 | Counterparty Risk |
| 6 | Market Risk |
| 7 | Bank Guarantee |
| 8 | Market Overview |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Treasury Risk Manager or Cash Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Treasury Executive Dashboard (F4316). | The overview page is launched successfully and the SAP Treasury Executive Dashboard is displayed. |  |

#### Story Tabstrip: Liquidity

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Liquidity tabstrip

Table 2:

| Chart/Card# | Card Name | Card Detail | Formula or Calculated logic |
| --- | --- | --- | --- |
| 1 | Liquidity by Country | Chart 1 ~ Chart 7 will interact with each other (Except for chart 3) |  |
| 2 | Liquidity | Chart 1 ~ Chart 7 will interact with each other (Except for chart 3) |  |
| 3 | History of Liquidity | Chart 1 ~ Chart 7 will interact with each other (Except for chart 3) |  |
| 4 | Liquidity by Region | Chart 1 ~ Chart 7 will interact with each other (Except for chart 3) |  |
| 5 | Liquidity by Company Code (Top5) | Chart 1 ~ Chart 7 will interact with each other (Except for chart 3) |  |
| 6 | Liquidity by Financial Position Group | Chart 1 ~ Chart 7 will interact with each other (Except for chart 3) |  |
| 7 | Liquidity by Currency | Chart 1 ~ Chart 7 will interact with each other (Except for chart 3) |  |
| 8 | Liquidity by Treasury Center and Financial Positions |  | Gross Assets of Treasury Center:Assets/Liabilities = AssetsTreasury Center = Flag set. Event has occurred |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip |  | In the story, by default the Liquidity tab is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_FINANCIALSTATUSQUERY_2 .In the Set Variables for SAP Treasury Financial Position dialog box, enter the prompt values and choose Set.For example:Key Date*: Aug 19,2019Display Currency*: EURExchange Rate Type*: M | The charts will refresh with data you have selected. |  |
| 3 | Set prompt for the charts in this tab | Edit Story Prompts (story prompt icon {} from the toolbar area) > C_HISTFINANCIALSTATUSQUERY_2In the Set Variables for C_HISTFINANCIALSTATUSQUERY_2 dialog box, enter the prompt values and choose Set.For example:Key Date*: Aug 19,2019Display Currency*: EURExchange Rate Type*: MPeriod*: Last 4 Quarters | The charts will refresh with data you have selected. |  |
| 4 | Choose a region in Liquidity by Region | In the left-upper geo map, choose a bubble | Charts 2 and Charts 4-7 will refresh with data you have selected. |  |
| 5 | Test interactions among charts 1~7(except 3) | Repeat similar steps to view interactions among the charts 1~7 (except 3) | Data are reflected correctly. |  |

#### Story Tabstrip: Cash Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Cash Management tabstrip

Table 3:

| Chart/Card# | Card Name | Card Detail | Formula or Calculated logic |
| --- | --- | --- | --- |
| 1 | Region | Region filter for all the charts below |  |
| 2 | Cash Position |  | Filtered by Region Filter |
| 3 | Cash Position by Region |  | Filtered by Region Filter |
| 4 | Cash Position by Bank Account Currency |  | Filtered by Region Filter |
| 5 | Cash Position by Company Code |  | Filtered by Region Filter |
| 6 | Cash Position by Bank |  | Filtered by Region Filter |
| 7 | Cash Position by Bank Account |  | Filtered by Region Filter |
| 8 | Liquidity Forecast for Balances (For Future 90 Days) |  | Filtered by Region Filter |
| 9 | Liquidity Forecast by Liquidity Item | Display the detail of selected day (in left chart) | Filtered by Region FilterWhen you select one date (bar) in left table, the detail of selected date will be filtered out |
| 10 | Actual Cash Flows (For Past 90 Days) |  | Filtered by Region Filter |
| 11 | Actual Cash Flow by Liquidity Item | Display the detail of selected day (in left chart) | Filtered by Region FiltersWhen you select one date (bar) in left table, the detail of selected date will be filtered out |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip | In the story, choose the Cash Management tabstrip, | The Cash Management page is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_LIQUIDITYPOSITIONQUERY1In the Set Variables for SAP Treasury Liquidity Position dialog box, enter the prompt values and choose Set.For example:Key Date*: Aug 19,2019Display Currency*: EURExchange Rate Type*: MCashPool Prof Name*: CP_GENForecast Prof Name*: CP_GEN | The charts will refresh with data you have selected. |  |
| 3 | Adjust Input Control Regions | In the left-upper corner, choose several regions from the Regions hierarchy | Charts in this tabstrip will refresh with data you have selected. |  |

#### Story Tabstrip: Bank Relationship

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Bank Relationship tabstrip

Table 4:

| Chart/Card# | Card Name | Card Detail | Formula or Calculated logic |
| --- | --- | --- | --- |
| 1 | Total Incoming | Total incoming payment amount in selected time period |  |
| 2 | Total Outgoing | Total outgoing payment amount in selected time period |  |
| 3 | Average Incoming | Average incoming payment amount in selected time period | Total Incoming Payment Amount divided by number of banks |
| 4 | Average Outgoing | Average outgoing payment amount in selected time period | Total Outgoing Payment Amount divided by number of banks |
| 5 | Banks by Rating | Number and proportion of banks for each rating |  |
| 6 | Bank Accounts by Banks | Number of bank accounts under each bank | Top 5 of bank accounts by default |
| 7 | Company Codes by Banks | Number of company codes under each bank | Top 5 of company codes by default |
| 8 | Payment Amount by Banks | Payment amount (incoming/outgoing) for each bank in selected period | Dynamic reference line for average incoming/outgoing payment amount |
| 9 | Bank Accounts by Bank Groups | Number of bank accounts under each bank group | Top 5 of bank accounts by default |
| 10 | Company Codes by Bank Groups | Number of company codes under each bank group | Top 5 of company codes by default |
| 11 | Financial Status by Bank Groups | Book value of asset, liability and balance under each bank group |  |
| 12 | Assets and Liabilities by Bank Groups | The distribution of Assets and Liabilities by Bank Groups |  |
| 13 | Bank Fees by Bank Groups | The distribution of Bank Fees by Bank Groups | chart 16 will refresh each other when one of the chart stacks is chosen |
| 14 | Service Charge Amount by Bank Group | The distribution of service charge by bank group | Chart 16~18 will refresh each other when one of the chart stacks is chosen |
| 15 | Service Charge Amount by Service Common Code | The distribution of service charge by service common code and bank group | Chart 16~18 will refresh each other when one of the chart stacks is chosen |
| 16 | Service Charge Amount by Service Type | The distribution of service charge by charge type and bank group | Chart 16~18 will refresh each other when one of the chart stacks is chosen |
| 17 | Distribution of Product Group Amount by Bank Group |  |  |
| 18 | History of Product Group Amount by Bank Group |  |  |
| Fee of Financial Transactions |  |  |  |
| 19 | Paid Fees of Reporting Period – By Bank Group |  |  |
| 20 | Forecasted Fees – By Bank Group |  |  |
| 21 | Distribution of Paid Fees of Reporting Period – By Bank Group |  |  |
| 22 | Distribution of Forecasted Fees – By Bank Group |  |  |
| 23 | History of Paid Fees by Bank Group |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip | In the story, choose the Bank Relationship tabstrip. | The Bank Relationship page is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts{} > C_PAYMENTBYBANKKPI or C_PAYMENTBYBANKQUERY or C_BANKACCTANALYSISQUERY or C_HOUSEBANKACCTANLYSQRY or C_FINANCIALSTATUSQUERY or C_FINTRANSAMTQRY1 or C_FinTransSingleDayAmtQry or C_FinTransFcstHistlFeeQry .In the Set Variables for SAP Treasury Payment KPIs or Set Variables for SAP Treasury Payment by Bank dialog box, enter the prompt values and choose Set.For example:Exchange Rate Date*: Nov 6, 2019 or use Date Picker button to choose the dateExchange Rate Type*: MDisplay Currency*: EURFrom*: Aug 7, 2019 or use Date Picker button to choose the dateTo*: Nov 6, 2019 or use Date Picker button to choose the date.In the Set Variables for SAP Treasury Bank Group Liquidity Status or Set Variables for SAP Treasury Bank Fee for Bank Groups or Set Variables SAP Treasury Bank Account or Set Variables for SAP Treasury House Bank Account dialog box, enter the prompt values and choose Set.For example:Key Date*: Nov 6, 2019 or use Date Picker button to choose the dateDisplay Currency*: EURExchange Rate Type*: MIn the Set Variables for C_FINTRANSAMTQRY1 dialog box, enter the prompt values and choose Set.For example:Start Date*: Aug 19, 2020 or use Date Picker button to choose the dateEnd Date*: Aug 19, 2021 or use Date Picker button to choose the dateDisplay Currency*: EURExchange Rate Type*: MReporting Frequency*: DIn the Set Variables forC_FinTransFcstHistlFeeQry dialog box, enter the prompt values and choose Set.For example:Start Date*: Nov 12, 2019End Date*: Nov 12, 2020Start Date*: Nov 13, 2020End Date*: Nov 12, 2021Display Currency*: EURExchange Rate Type*: M | The charts in this page will refresh with data you have selected. |  |
| 3 | Adjust Input Control Company codes | In the left panel, choose several company codes from the hierarchy. | Charts on the right will refresh with data you have selected. |  |
| 4 | Link Analysis | Choose one row from table Bank Fees by Bank Groups. | Chart 15~18 is refreshed with criteria you have selected. |  |
|  |  | Choose one stack from charts 16~18. | Charts 16~18 is refreshed with criteria you have selected |  |

#### Story Tabstrip: Indebtedness

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Indebtedness tabstrip

Table 5:

| Chart/Card# | Card Name | Card Detail | Formula or Calculated logic |
| --- | --- | --- | --- |
| 1 | Total Amount of Debt | Region filter for all the charts below | Measure = Nominal Amount in Display Crcy;Debt/Investment = Debt;Product Category = 510,520,530,540,550,580,20,40,42,60,70 |
| 2 | Amount of Debt by Company Code |  |  |
| 3 | Amount of Debt by Product Type |  |  |
| 4 | Total Amount of Debt by Transaction Currency |  |  |
| 5 | Debt Maturity Profile |  |  |
| 6 | Without Swaps |  |  |
| 7 | Structure of Interest Rate Debt |  | Measure = Nominal Amount in Display Crcy;Debt/Investment = Debt;Product Category = 510,520,530,540,550,580,20,40,42,60,70 |
| 8 | Including Swaps |  |  |
| 9 | Structure of Interest Rate Debt Including Swaps |  | - (Debt Amount + Investment Amount-Swap) |
| 10 | Total Credit Line |  |  |
| 11 | Total Credit Line by Counterparty, Company Code, Transaction Currency |  |  |
| 12 | Forecast of Available Amount |  | Available Amount:Total Credit Line - Utilized Amount |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip | In the story, choose the Indebteness tabstrip | The Indebteness page is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_MATURITYPROFILEQUERYIn the Set Variables for SAP Treasury Maturity Profile dialog box, enter the prompt values and choose Set.For example:Key Date*: Aug 19,2019Display Currency*: EURExchange Rate Type*: MNumber of Years*: 3 | The charts 1–9 will refresh with data you have selected. |  |
| 3 | Set prompt | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_CREDITLINEUTILQRYIn the Set Variables for SAP Treasury Credit Line Utilization dialog box, enter the prompt values and choose Set.For example:Start Date*: Jul 19,2019End Date*: Aug 19,2019Exchange Rate Type*: MDisplay Currency*: EUR | The charts 10–12 will refresh with data you have selected. |  |

#### Story Tabstrip: Counterparty Risk

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Counterparty Risk tabstrip

Table 6:

| Chart/Card# | Card Name | Card Detail | Formula or Calculated logic |
| --- | --- | --- | --- |
| 1 | Free Limit by Counterparty |  | Bottom 5 of all counterparties by Default |
| 2 | Free Limit by Counterparty |  | Top 5 of all counterparties by Default |
| 3 | Limit Utilization by Counterparty |  | Top 5 of all counterparties by Default |
| 4 | Limit Utilization by Counterparty | Outlined bar shows the total limit and solid bar shows the actual utilization. | Select one Business Partner, chart 5–9 will be filtered accordingly |
| 5 | Limit Utilization by Product Group | Outlined bar shows the total limit and solid bar shows the actual utilization. | Filtered by selected Business Partner in chart 4 |
| 6 | Free Limit by Counterparty and Product Group | When utilization exceeds limit, the block is exceptional that formatted as red. | Filtered by selected Business Partner in chart 4 |
| 7 | Utilization Overview by Counterparty and Product Group |  | Filtered by selected Business Partner in chart 4When you select one business partner in left table, the rating of selected business partner will be filtered out |
| 8 | Counterparty Rating | Display the rating of selected business partner (in left table). | Filtered by selected Business Partner in chart 4 |
| 9 | History of Free Limits |  | Filtered by selected Business Partner in chart 4 |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip | In the story, choose the Counterparty Risk tabstrip. | The Counterparty Risk page is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_TRSYCTPTYLIMITOVERVIEWQ2 .In the Set Variables for SAP Treasury Counterparty Limit Overview dialog box, enter the prompt values and choose Set.For example:Display Currency*: EURExchange Rate Type*: MLimit Type*: Y13Limit Utilization Base*: 1 | The charts will refresh with data you have selected. |  |
| 3 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_TRSYCTPTYLMTBPRATINGQRY2 .In the Set Variables for SAP Treasury Counterparty Limit Business Partner Rating dialog box, enter the prompt values and choose Set.For example:Key Date*: Sep 16, 2019(By Default, current day is selected) | The charts will refresh with data you have selected. |  |
| 4 | Select specific Business Partner that you are interested in | Select a bar of your interested Business Partners from chart 4 Limit Utilization by Counterparty | Charts 5–9 will refresh with data of your selected business partners. |  |

#### Story Tabstrip: Market Risk

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Market Risk TabStrip

Table 7:

| Chart/Card# | Card Name | Card Detail | Formula or Calculated logic |
| --- | --- | --- | --- |
| Company Code |  |  |  |
|  | Company Code Input Control |  | Control the entire TabStrip |
| Net Present Value and Value at Risk by Different Attributes |  |  |  |
| 1 | Net Present Value (NPV) |  | Net Present Value: Get the Net Present Value of the first selected Key Figure Set (The same as below) |
| 2 | Value at Risk (VaR) |  | Value at Risk: Get the Value at Risk of the first selected Key Figure Set (The same as below) |
| 3 | Negative and Positive NPVs |  |  |
| 4 | Net Present Value by Product Category |  |  |
| 5 | Value at Risk by Product Category |  |  |
| 6 | Net Present Value by Key Figure Set and Product Category |  |  |
| 7 | Value at Risk by Company Code and Product Category |  |  |
| History of Net Present Value |  |  |  |
| 8 | Net Present Value by Date and Key Figure Set |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip | In the story, choose the Market Risk tabstrip. | The Market Risk page is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} > C_TrsyMktRskKeyFigValueQry .In the Set Variables for SAP Treasury Market Risk Key Figure Value dialog box, enter the prompt values and choose Set.For example:Display Currency*: EURExchange Rate Type*: MKey Date*: Nov 12,2019 - Feb 12,2020 | The charts will refresh with data you have selected. |  |
| 3 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} > C_TrsyValueAtRiskQuery .In the Set Variables for SAP Treasury Value At Risk dialog box, enter the prompt values and choose Set.For example:Confidence Level (%)* : 95Key Date*: (By Default, current day is selected)Display Currency*: EURExchange Rate Type*: M | Charts in this TabStrip will refresh with data of your selected company codes |  |
| 4 | Select specific Company Code that you are interested in | Select your interested company code from input control Company Code | Charts in this TabStrip will refresh with data of your selected company codes |  |

#### Story Tabstrip: Bank Guarantee

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Bank Guarantee tabstrip

Table 8:

| Chart/Card# | Card Name | Card Detail | Formula or Calculated logic |
| --- | --- | --- | --- |
| 1 | Total Volume, Number of Transactions | Total Volume of bank guaranteeNumber of financial transactions |  |
| 2 | Volume by Company Code | Volume of bank guarantee by company code | Top 5 of company code |
| 3 | Volume by Counterparty | Volume of bank guarantee by Counterparty | Top 5 of Counterparty |
| 4 | Volume by Currency | Volume of bank guarantee by nominal currency | Top 5 of all counterparties by Default |
| 5 | Average Fee Rate by Counterparty | Column bar shows fee rate | Top 5 of Fee rate based on Fee calculation type |
| 6 | Volume vs Fee Rate by Counterparty | X axis: Fee RateY axis: Total VolumeSize: Fee Amount | Top10 Fee Rate based on Fee calculation type compared by counterparty |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip | In the story, choose the Counterparty Risk tabstrip. | The Counterparty Risk page is displayed. |  |
| 2 | Set prompt for the charts in this tab | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_BANKGUARANTEEOVERVIEWQRY .In the Set Variables for SAP Treasury Bank Guarantee Overview dialog box, enter the prompt values and choose Set.For example:Product Type*: Bank GuaranteeTransaction Type*: IssueLKey Date*: Aug 27, 2019Display Currency*: EURExchange Rate Type*: M | The charts will refresh with data you have selected. |  |

#### Story Tabstrip: Market Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Overview

The Market Overview tabstrip

Table 9:

| Chart/Card# | Card Name | Card Detail | Formula or Calculated logic |
| --- | --- | --- | --- |
| 1 | Foreign Exchange Rate |  |  |
| 2 | Reference Interest Rate |  |  |
| 3 | Security Price |  |  |
| 4 | Implied Volatility |  |  |
| 5 | CDS Spread (Bank Description) |  |  |
| 6 | Basis Spread |  |  |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Tabstrip | In the story, choose the Market Overview tabstrip. | The Market Overview page is displayed. |  |
| 2 | Set prompt for the card Foreign Exchange Rate | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_MKTDATAFXRATEQUERY1 .In the Set Variables for SAP Treasury FX Rate dialog box, enter the prompt values and choose Set.For example:Exchange Rate Type*: MCurrency Pair*: EUR/USD;EUR/CAD;USD/CAD;USD/EURCalendar Date*: Jan 1, 2018 - Jul 9, 2019 | The chart 1 will refresh with data you have selected. |  |
| 3 | Set prompt for card Reference Interest Rate | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_MKTDATAREFINTRSTRATEQRY1 .In the Set Variables for SAP Treasury Reference Interest Rate dialog box, enter the prompt values and choose Set.For example:Exchange Rate Type*: MRef. Interest Rate*: EBONDYEUR02; EBONDYEUR03; EBONDYEUR05; EBONDYEUR07;DEPOBUSD01; DEPOBUSD03; DEPOBUSD06Calendar Date*: Jan 1, 2018 - Jul 9, 2019 | The chart 2 will refresh with data you have selected. |  |
| 4 | Set prompt for card Security Price | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_SECURITYPRICEQUERYIn the Set Variables for SAP Treasury Security Price dialog box, enter the prompt values and choose Set.For example:Security Price Type*: 01Security Class*: <ALL>Calendar Date*: Jan 1, 2015 - Jul 9, 2018 | The chart 3 will refresh with data you have selected. |  |
| 5 | Set prompt for card Implied Volatility | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_MKTDATAIMPVOLATILITYQRY3In the Set Variables for SAP Treasury Reference Interest Rate dialog box, enter the prompt values and choose Set.For example:Volatility Name*: ASD;FX_VOL_MNVolatility Profile*: FX_VOL_MNFX_120;FX_30;FX_60;FX_90Volatility Type*: <All>Calendar Date*: Jan 1, 2018 - Jul 9, 2019Adjust the value of input control Volatility Name to one of the values you have entered in prompt. | The chart 4 will refresh with data you have selected. |  |
| 6 | Set prompt for card Credit Spread (<Bank Description>) | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_MKTDATACREDITSPREADQRY2In the Set SAP Treasury Credit Spread Value dialog box, enter the prompt values and choose Set.For example:Reference Entity*: AREF_BBANK;REF_CC_0001Credit Spread ID*: <All>Quotation Type*: 1Calendar Date*: Jan 1, 2018 - Jul 9, 2019Adjust the value of input control Reference Entity to one of the values you have entered in prompt | The chart 5 will refresh with data you have selected. |  |
| 7 | Set prompt for card SAP Treasury Basis Spread | Edit Table Prompts (story prompt icon {} under the report title, not story prompt from the toolbar area) > C_MKTDATABASISSPREADQRYIn the Set SAP Treasury Basis Spread dialog box, enter the prompt values and choose Set.For example:Quotation Type*: 1Basis Spread ID*: <All>Calendar Date*: Jan 1, 2017 - Jul 9, 2019 | The chart 6 will refresh with data you have selected. |  |
| 8 | Adjust Input Controls | Adjust input controls from upper panel according to your own scenario. | Report values changed after input controls adjusted. |  |

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
- see-also :: [[05-treasury-and-cash-management/test-script-liquidity-planning-3l5-ae-953]]
- see-also :: [[05-treasury-and-cash-management/basic-cash-operations-bfb-ae-test-script-sap-s-4hana-cloud-public-edit]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1MN_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 40,763 chars in the whole document
