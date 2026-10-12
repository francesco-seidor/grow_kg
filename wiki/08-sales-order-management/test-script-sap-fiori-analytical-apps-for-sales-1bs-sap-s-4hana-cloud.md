---
id: 08-sales-order-management/test-script-sap-fiori-analytical-apps-for-sales-1bs-sap-s-4hana-cloud
title: "Test Script: SAP Fiori Analytical Apps for Sales (1BS) - SAP S/4HANA Cloud Public Edition (1BS_S4CLD2608_BPD_EN_XX)"
description: "Test script for SAP scope item 1BS: Fiori test procedures for 18 sales analytical apps (overviews, quotations, orders, returns, sales volume, O2C)."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/sales-fulfillment-monitoring-and-analytics]
aliases: [1BS_S4CLD2608_BPD_EN_XX]
keywords: [Sales Order Fulfillment Monitoring and Sales Analytics, test scripts, sales analytical apps, sales overview pages, quotation conversion rates, sales contract fulfillment, incoming sales orders, sales order confirmation, delivery performance, customer returns analysis]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1BS_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-711
topic: 08-sales-order-management/sales-fulfillment-monitoring-and-analytics
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: SAP Fiori Analytical Apps for Sales (1BS) - SAP S/4HANA Cloud Public Edition (1BS_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1BS_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Sales Order Fulfillment Monitoring and Sales Analytics** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | SAP Fiori Analytical Apps for Sales (1BS) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852231)

[2 Prerequisites 4](#_Toc232852232)

[2.1 System Access 4](#_Toc232852233)

[2.2 Roles 4](#_Toc232852234)

[2.3 Business Conditions 5](#_Toc232852235)

[3 Overview Table 6](#_Toc232852236)

[4 Test Procedures 8](#_Toc232852237)

[4.1 My Sales Overview 8](#_Toc232852238)

[4.2 Sales Management Overview 10](#_Toc232852239)

[4.3 Sales Quotations - Flexible Analysis 12](#_Toc232852240)

[4.4 Quotation Conversion Rates 13](#_Toc232852241)

[4.5 Sales Contract Fulfillment Rates 14](#_Toc232852242)

[4.6 Incoming Sales Orders 15](#_Toc232852243)

[4.7 Analyze Confirmations of Sales Orders 17](#_Toc232852244)

[4.8 Delivery Performance 19](#_Toc232852245)

[4.9 Customer Returns - Flexible Analysis 20](#_Toc232852246)

[4.10 Customer Return Rate 21](#_Toc232852247)

[4.11 Sales Volume - Flexible Analysis 22](#_Toc232852248)

[4.12 Sales Volume - Detailed Analysis 24](#_Toc232852249)

[4.13 Sales Volume - Check Open Sales 25](#_Toc232852250)

[4.14 Sales Volume - Credit Memos 27](#_Toc232852251)

[4.15 Sales Volume - Profit Margin 28](#_Toc232852252)

[4.16 Sales Scheduling Agreements – Product Demand 30](#_Toc232852253)

[4.17 Customer Returns Overview 32](#_Toc232852254)

[4.18 Order to Cash Dashboard 33](#_Toc232852255)

## Purpose

Overview

For sales and distribution scenarios, this scope item provides key information required for a sales manager or internal sales representative about the different stages of a sales order. The analytical apps provided highlights back orders, demand fulfillment, sales order fulfillment and delivery performance in the sales process. An SAP Fiori overview page is also available that provides the different insight to actions about sales quotations, customer returns, sales order fulfillment and more.

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
| Internal Sales Representative | SAP_BR_INTERNAL_SALES_REP | Internal Sales / Customer Returns / Billing | SAP_BR_INTERNAL_SALES_REP / SAP_SD_SPT_RETURNS_INT_SALES_PC / SAP_SD_SPT_BILLING_INT_SALES_PC |  |
| Returns and Refund Clerk | SAP_BR_RETURNS_REFUND_CLERK | Customer Returns | SAP_BR_RETURNS_REFUND_CLERK |  |
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC |  |

### Business Conditions

Follow the procedures described in the following scope items to create the corresponding business data if needed.

| Scope Item | Business Condition |
| --- | --- |
| BD3 - Sales Processing using Third-Party with Shipping Notification | Follow the scope item to create the corresponding business data. |
| BD9 - Sell from Stock | Follow the scope item to create the corresponding business data. |
| BDD - Lean Customer Returns | Follow the scope item to create the corresponding business data. |
| BDG - Sales Quotation | Follow the scope item to create the corresponding business data. |
| BDH - Sales Order Entry with One-Time Customer | Follow the scope item to create the corresponding business data. |
| BDK -Sales Processing Using Third-Party Without Shipping Notification | Follow the scope item to create the corresponding business data. |
| BDN - Sales of Non-Stock Item with Order-Specific Procurement | Follow the scope item to create the corresponding business data. |
| BKJ - Sales Order Processing with Customer Down Payment | Follow the scope item to create the corresponding business data. |
| BDW - Returnables Processing | Follow the scope item to create the corresponding business data. |
| BKZ - Sales Order Processing with Invoice List and Collective Billing | Follow the scope item to create the corresponding business data. |
| 1EZ - Credit Memo Processing | Follow the scope item to create the corresponding business data. |
| 1F1 - Debit Memo Processing | Follow the scope item to create the corresponding business data. |
| BKP - Customer Returns | Follow the scope item to create the corresponding business data. |
| I9I - Sales Contract Management | Follow the scope item to create the corresponding business data. |
| 3D2 - Service Order Management and Monitoring | Follow the scope item to create the corresponding business data. |
| J58 - Accounting and Financial Close | Follow test procedure Currency Exchange Rates to maintain exchange rates if needed or issue met. |

## Overview Table

This scope item consists of several process steps provided in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App Name | Expected Results |
| --- | --- | --- | --- |
| [My Sales Overview](#unique_7) [page ] 8 | Internal Sales RepresentativeReturns and Refund ClerkSales Manager | My Sales Overview (F2200) | The SAP Fiori app is running correctly. |
| [Sales Management Overview](#unique_8) [page ] 10 | Sales Manager | Sales Management Overview - Track Execution (F2601) | The SAP Fiori app is running correctly. |
| [Sales Quotations - Flexible Analysis](#unique_9) [page ] 12 | Sales Manager | Sales Quotations - Flexible Analysis (W0140) | The SAP Fiori app is running correctly. |
| [Quotation Conversion Rates](#unique_10) [page ] 13 | Sales Manager | Quotation Conversion Rates - Valid/Not Completed (F1904) | The SAP Fiori app is running correctly. |
| [Sales Contract Fulfillment Rates](#unique_11) [page ] 14 | Sales Manager | Sales Contract Fulfillment Rates - Currently Valid (F1905) | The SAP Fiori app is running correctly. |
| [Incoming Sales Orders](#unique_12) [page ] 15 | Sales Manager | Incoming Sales Orders - Flexible Analysis (F1249) | The SAP Fiori app is running correctly. |
| [Analyze Confirmations of Sales Orders](#unique_13) [page ] 17 | Sales Manager | Sales Order Items - Confirmed as Requested (F5308)Sales Order Items - Backorders (F5307)Sales Orders - Demand Fulfillment (F2458) | The SAP Fiori app is running correctly. |
| [Delivery Performance](#unique_14) [page ] 19 | Sales Manager | Delivery Performance - Delivered as Requested (F2783) | The SAP Fiori app is running correctly. |
| [Customer Returns - Flexible Analysis](#unique_15) [page ] 20 | Sales ManagerReturns and Refund Clerk | Customer Returns (W0139) | The SAP Fiori app is running correctly. |
| [Customer Return Rate](#unique_16) [page ] 21 | Sales ManagerReturns and Refund Clerk | Customer Returns - Return Rate (F4092) | The SAP Fiori app is running correctly. |
| [Sales Volume - Flexible Analysis](#unique_17) [page ] 22 | Sales Manager | Sales Volume - Flexible Analysis (F1250) | The SAP Fiori app is running correctly. |
| [Sales Volume - Detailed Analysis](#unique_18) [page ] 24 | Sales Manager | Sales Volume - Detailed Analysis (F2235) | The SAP Fiori app is running correctly. |
| [Sales Volume - Check Open Sales](#unique_19) [page ] 25 | Sales ManagerInternal Sales Representative | Sales Volume (F2270) | The SAP Fiori app is running correctly. |
| [Sales Volume - Credit Memos](#unique_20) [page ] 27 | Sales Manager | Sales Volume (F5310) | The SAP Fiori app is running correctly. |
| [Sales Volume - Profit Margin](#unique_21) [page ] 28 | Sales Manager | Sales Volume - Profit Margin (F2271) | The SAP Fiori app is running correctly. |
| [Sales Scheduling Agreements – Product Demand](#unique_22) [page ] 30 | Internal Sales Representative | Sales Scheduling Agreements – Product Demand(F4508) | The SAP Fiori app is running correctly. |
| [Customer Returns Overview](#unique_23) [page ] 32 | Sales Manager | Customer Returns Overview (F4561) | The SAP Fiori app is running correctly. |
| [Order to Cash Dashboard](#unique_24) [page ] 33 | Sales Manager | Order to Cash Dashboard (F4663) | The SAP Fiori app is running correctly. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### My Sales Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The application allows you to view and create sales data in actionable cards, which you can see in a dashboard format. Sales data can include incoming sales orders, blocked credit memo requests, customer returns, and customer information.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Set User Default Values | Choose the user icon and choose Settings. On the Settings screen, choose Default Values. Maintain values for your user:For example, Exchange Rate Type Display Currency.Choose Save. | The user default values are set. |  |
| 3 | Access the App | Open My Sales Overview (F2200) | The overview page is launched successfully and the following cards are displayed (the exact names may vary):Blocked Credit Memo RequestsCustomer ReturnsOpen Sales QuotationsIncoming Sales OrdersOpen Sales OrdersSales Order FulfillmentSales Quotation PipelineQuick Actions |  |
| 4 | Set Global Filter | The global filters must be set in the global filter bar. If you enter values in the fields of the global filter, the overview page refreshes the content. | The global filter is applied to all cards on the overview page. |  |
| 5 | Navigate from Blocked Credit Memo Requests Card | Navigate from Blocked Credit Memo Requests and choose the header or line item level of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (or line item) information is carried over.If you choose the header, you are navigated to the Credit Memo Request worklist. If you choose a line item, you are directly navigated to the selected credit memo request. |  |
| 6 | Navigate from Customer Returns Card | Navigate from Customer Returns and choose the header or line item level of the card to get further information.Note The Returns & Refunds Clerk business role is required for navigation. | The overview page navigates you to the target apps. The global filter and header (or line item) information is carried over.If you choose the header or line item, you are navigated to the Manage Customer Returns app. |  |
| 7 | Navigate from Open Sales Quotations Card | Navigate from Open Sales Quotations and choose the header or line item level of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (or line item) information is carried over.If you choose the header, you are navigated to Sales Quotations worklist. Choosing one line item directly navigates you to the selected open sales quotation. |  |
| 8 | Navigate from Incoming Sales Orders Card | Navigate from Incoming Sales Orders and choose the header or line item level of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (or line item) information is carried over. If you choose the header, you are navigated to the Incoming Sales Orders application. |  |
| 9 | Navigate from Open Sales Orders Card | Navigate from Open Sales Orders and choose the header or line item level of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (or line item) information is carried over.If you choose the header, you are navigated to the Sales Orders worklist. Choosing one line item directly navigates you to the selected sales order. |  |
| 10 | Navigate from Sales Order Fulfillment Card | Navigate from Sales Order Fulfillment and choose the header or line item level of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (or line item) information is carried over.If you choose the header, you are navigated to Sales Order Fulfillment Issues worklist.If you choose the line item, you are navigated to the Sales Order Fulfillment Issues worklist with the sales orders of the selected issue category. |  |
| 11 | Navigate from Sales Quotation Pipeline Card | Navigate from Sales Quotation Pipeline and choose the header or line item level of the card to get further information. | The overview page navigates you to the target apps. The global filter and header (or line item) information is carried over.If you choose the header, you are navigated to the Manage Sales Quotations worklist. Choosing one line item navigates to the Manage Sales Quotations worklist with the sales quotations of the selected status. |  |
| 12 | Navigate from Quick Actions Card | Navigate from Quick Actions and choose the Action Links of the card for further action. | The overview page navigates to the selected Quick Action app. |  |

### Sales Management Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you as a sales manager can get a graphical overview of your various sales data on cards. You can further analyze the data by navigating to related analytical apps from the cards. Using this app, you can gain comprehensive insights into your current sales situation and respond quickly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager . | The SAP Fiori launchpad is displayed. |  |
| 2 | Set User Default Values | Choose the user icon and choose Settings. On the Settings screen, choose Default Values. Maintain values for your user. For example, Exchange Rate Type, Display Currency, and choose Save. | The user default values are set. |  |
| 3 | Access the App | Open Sales Management Overview - Track Execution (F2601). | The overview page has launched successfully and the following cards are displayed (the exact names may vary):Incoming Sales OrdersCustomer ReturnsIncomplete Sales DocumentsBackorder ItemsProfit MarginBlocked Sales OrdersOverdue Sales Orders |  |
| 4 | Set Global Filter | The global filters must be set in the global filter bar. Set values in the fields of the global filter and the overview page refreshes the content. | The global filter applies to all cards on the overview page. |  |
| 5 | Manage Cards | Cards on the overview page can be customized through Manage Cards. Choose the user icon on the screen, choose Manage Cards, make the settings of your choice, and then choose OK. | The cards on the overview page can be rearranged, hidden, and displayed again. |  |
| 6 | Switch KPI on Incoming Sales Orders Card | Select By Number from the dropdown list on the Incoming Sales Orders card. | The KPI changes. |  |
| 7 | Navigate from Incoming Sales Orders Card | Navigate from Incoming Sales Orders, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the Incoming Sales Orders – Flexible Analysis target app. The global filter and card information is carried over. |  |
| 8 | Navigate from Customer Returns Card | Navigate from Customer Returns, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the Customer Returns - Flexible Analysis target app. The global filter and card information is carried over. |  |
| 9 | Navigate from Incomplete Sales Documents Card | Navigate from Incomplete Sales Documents, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the List Incomplete Sales Documents target app. The global filter and card information is carried over. |  |
| 10 | Navigate from Backorder Items Card | Navigate from Backorder Items, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the Sales Order Items target app. The global filter and card information is carried over. |  |
| 11 | Navigate from Profit Margin Card | Navigate from Profit Margin, choose the header or chart of the card to get more detailed information. | The overview page navigates you to the Sales Volume – Profit Margin target app. The global filter and card information is carried over. |  |
| 12 | Navigate from Blocked Sales Orders Card | Navigate from Blocked Sales Orders and choose the header or line item level of the card to get more detailed information. | Overview page navigates you to the Sales Order Fulfillment Issues target app. The global filter and card information is carried over. |  |
| 13 | Navigate from Overdue Sales Orders Card | Navigate from Overdue Sales Orders, and choose the header or line item level of the card to get more detailed information. | The overview page navigates you to the Sales Order Fulfillment Issues target app. The global filter and card information is carried over. |  |

### Sales Quotations - Flexible Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this app is to gain an understanding of the sales quotations.

|  |
| --- |
| Note There’s another app Sales Quotations with the same functionality but for the accessibility purpose, you can access the app with same business roles. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Set User Default Values | Choose the user icon and select Settings. On the Settings screen, choose Default Values. Maintain values for your user. For example, Exchange Rate Type, Display Currency. Then choose Save. | TThe user default values are set. |  |
| 3 | Access the App | Open Sales Quotations - Flexible Analysis (W0140). Set the mandatory filters and choose GO. | The app is launched successfully. |  |
| 4 | Add Analysis Dimension | Open Navigation Panel, drag and drop the Available Fields to COLUMNS or ROWS for more analysis. | More analysis dimensions are added and the result is refreshed accordingly. |  |
| 5 | Target Navigation | Choose Navigate To to open the navigation list. Select one of them, for example, Sales Quotation for more analysis. | The target app is launched successfully. |  |

### Quotation Conversion Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This analytical app displays the Key Performance Indicator (KPI) Quotation Conversion Rates. It indicates the percentage of net value of orders that have been converted from a quotation, based on the total net value of the quotation. With Quotation Conversion Rates, you can track, in real time, to what extent your quotations are being referenced before expiring.

|  |
| --- |
| Note You may refer to 2YJ - Predictive Analytics Model Training – Sales for the predictive analytics of Quotation Conversion Rates. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Quotation Conversion Rates - Valid/Not Completed (F1904) . | The app launched successfully. |  |
| 3 | View by Customer | Open the view drilldown list and choose Customer. | The data displayed in the graph is changed accordingly. |  |
| 4 | Switch to Table View | Choose Tabular View on the screen. | The graphical view is replaced with the table view. |  |
| 5 | Drill Down to Further Dimension | On the Current Selection screen, choose one customer and drill down with another dimension. For example, on the Bottom 10 quotations by Conversion Rate. | The data displayed in the graph is changed accordingly. |  |
| 6 | Navigation to Jump To Target App | In Bottom 10 quotations by Conversion Rate, choose one customer and drill down with another dimension. For example, on the view, select one quotation and choose Jump To. Select one of them for further action, for example Sales Quotation. | The target app is opened. |  |

### Sales Contract Fulfillment Rates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This analytical app displays the Key Performance Indicator (KPI) Sales Contract Fulfillment Rates, which indicate the percentage of the target value that has been released in a sales contract. With Sales Contract Fulfillment Rates, you can analyze how well the contracts in the sales area you are responsible for being fulfilled. Using this KPI, you can quickly identify contracts that required to be renewed soon, as well as contracts that are not being fulfilled as expected.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Sales Contract Fulfillment Rates - Currently Valid (F1905). | The app launches successfully. |  |
| 3 | View by Customer | Open the drilldown list and choose Customer. | The data displayed in the graph is changed accordingly. |  |
| 4 | Switch to table view | Choose Tabular View on the screen. | The graphical view is replaced with the table view. |  |
| 5 | Drill Down to Further Dimension | Choose one customer and drill down to another dimension. For example, on the Current Selection screen, choose Product. | The data displayed in the graph is changed accordingly. |  |
| 6 | Reset Filter | Choose Reset Filter to clear all the filters. | The filters have been cleared. |  |
| 7 | View by Top 10 Contracts by Target Value | Open the view drilldown list and choose Top 10 Contracts by Target Value. | The data displayed in the graph is changed accordingly. |  |
| 8 | Navigation to Jump To Target App | Choose the Jump To menu and select the target app for further action, for example, Sales Contract. | The target app is opened. |  |

### Incoming Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of the app is to gain an understanding of the monthly rolling trend of incoming sales orders. You can

- View the monthly rolling trend for sales as a graphic or a table.
- Analyze the net amounts of aggregated sales order items with the display currency.
- Drill down to view detailed information for selected sales organizations, products, product groups, sold-to parties, sales document types, and so on.
- Filter the items according to various criteria, such as year, month, sales organization, product group, and sold-to party.
- Change the displayed ID or description.
- Save your selection as a variant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager . | The SAP Fiori launchpad is displayed. |  |
| 2 | Set User Default Values | Choose the user icon and select Settings. On the Settings screen, choose Default Values. Maintain values for your user. For example, Exchange Rate Type, Display Currency. Choose Save. | The user default values are set. |  |
| 3 | Access the App | Open Incoming Sales Orders - Flexible Analysis (F1249). | The app is launched successfully. |  |
| 4 | Run the Report | Choose Go. | The monthly net amount is displayed in the table and the available fields list is available on navigation panel. |  |
| 5 | Switch to Graphical Display | Choose Graphical Display.Note If there are "*" in the results in the data analysis, it indicates that the corresponding Key Figure has mixed units of measure which leads to the Chart cannot be rendered error. To solve the error, you can either remove the affected Key Figures or set the filter criteria to avoid mixed units of measure. | The graphical view is displayed. |  |
| 6 | Change Display Currency | Set Display Currency to another currency, then choose Go. | The data displayed in the graph is changed accordingly. |  |
| 7 | Switch Back to Data Analysis | Choose Data Analysis. | The view is switched back to the list view. |  |
| 8 | Add Drilldown | Choose Drilldown and choose Add Drilldown. On the Select Fields screen, choose, for example, Sold-To Party. | Sold-to Party information is added. |  |
| 9 | Remove Drilldown | Select the Sold-to Party dimension in the table, choose Drilldown, and choose Remove Drilldown. | The drilldown added in a previous step is removed. |  |
| 10 | Drag Available Fields to Rows | On the Navigation Panel, drag fields from Available Fields list to Rows, for example, Product Group. | Fields are added as rows to the table. |  |

### Analyze Confirmations of Sales Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With Sales Orders - Demand Fulfillment (F2458) you, as a sales manager are able to monitor your current sales confirmation situation and instantly recognize the potential for unconfirmed sales orders. It is important for you because only confirmed sales orders will create sales volume in the future. For unconfirmed orders, you can trigger actions for your sales team to take care of. KPIs, charts, and navigation capabilities support you to solve issues.

There are three tiles that focus on variants.

Sales Order Items - Confirmed as Requested (F5308) provides the following top N displays:

- This week Confirmed (ratio)
- Last week Confirmed (ratio)
- The week before Confirmed (ratio)

Sales Order Items - Backorders (F5307) provides the following KPIs:

- Delayed (number of)
- Partially Confirmed (number of)
- Unconfirmed (number of)

Sales Orders - Demand Fulfillment (F2458) provides the following KPIs:

- Confirmed (value)
- Delayed (value)
- Unconfirmed (value)

You can

- View the weekly ratio, number of, quantity, and value of the following KPIs as a graphic or a table:
    1. As requested in the sales order item, Confirmed (as Requested), Delayed, Partially Confirmed (as Requested), Not Confirmed.
    2. As overall confirmed in the sales order schedule line, Confirmed, Delayed, Not Confirmed.
- Extend further dimensions through the drilldown. For example, drill down by product, and discover a particular product has a high level of unconfirmed quantity.
- Select the relevant sales document for the product, and display the sales document schedule lines to see the detailed insights of the confirmations.
- Drill down to view detailed information for selected, sold-to parties, customer classification, productl, plant, and so on.
- Filter according to various criteria, such as week/year, sold-to party, productl, plant, delivery status, sales order type.
- Navigate directly to all the tiles of the current app and to the sales order fulfillment filtered by the issue Unconfirmed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Sales Order Items - Backorders (F5307). | The app is launched successfully. |  |
| 3 | Change Selection Criteria | Choose By Week to open the drilldown list, choose By Sold-To Party for example, and select a displayed sold-to party for a detailed analysis. For example, choose By Product from the Current Selection menu. | After choosing By Productl for a further customer analysis, the graph displayed changes and the Total Unconfirmed changes accordingly. |  |
| 4 | Change the View Settings | Choose Settings in the chart view.In View Settings screen, select the Sort tab to sort the table by Confirmed (descending). | The table is sorted by Confirmed (descending). |  |
| 5 | Switch to list view | Choose the tabular view on the screen. | The graphical view is replaced with the list view. |  |
| 6 | Switch Back to Graphical View | Choose the chart view on the screen. | The list view changes back to the graphical view. |  |
| 7 | Remove the Filter Condition Added Previously by Change Selection Criteria | Choose the Reset filter icon. Choose OK on the Reset Filters screen. | The data displayed in the graph is changed accordingly.The Total Unconfirmed is changed accordingly. |  |
| 8 | Display the Associated Tiles | Choose Show Mini Tiles on the screen. | Sales Order Items – Confirmed and Sales Orders – Unconfirmed Demand are displayed, and the measures are displayed on the tiles. |  |
| 9 | Change Selection Criteria | Select the By Sold-To Party drilldown.Choose Add Filter at the top left of the page. Choose Week of Order on the Filter screen. Set the filter to the current and previous week. | The data results are restricted to the current and previous month and to customer perspective.The values displayed in the associated tile are changed according to the filter settings. |  |
| 10 | Navigate to the Associated Tile | Choose Sales Orders – Unconfirmed Demand. | The app and the measures are displayed for the time period selected previously. |  |
| 11 | Navigate Back to Sales Order Items – Backorders App | Choose Back on Sales Orders – Unconfirmed Demand. | The Sales Order Items – Backorders app is displayed correctly with the latest filter settings. |  |
| 12 | Check Jump To Function | Choose the Jump To menu and select the target app for further action, for example, Sales Order. | The target app is opened. |  |
| 13 | Set App Filters | Choose the Expand Header on the screen. | The filter bar is displayed. You can change the filter settings including the default parameters. |  |

### Delivery Performance

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

A sales manager always wants to be up-to-date with the delivery performance of sales order fulfillment. Reliable, on-time delivery as requested by the customer, is key for customer satisfaction. In the case of poor delivery service or poor delivery reliability, you need a quick insight into the delivery performance details. It can optimize the delivery performance in your area of responsibility, in the best way possible.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Delivery Performance - Delivered as Requested (F2783) .(The Deliv. Fulfilment Status filter is set to D for completely shipped by default. It corresponds to the filter that is set for the display of the tile) | The app is launched successfully with visual filters, charts, and the table data. |  |
| 3 | Switch to Compact Filters | Choose Compact Filter at the top right of the screen. It is used to toggle the filter mode from Visual Filter to Compact Filter. | The filter mode changes to Compact Filter. |  |
| 4 | Apply Filter | Apply some filter criteria and check if the chart and list are filtered accordingly. For example: set a different Delivery Fulfillment Status: A (in order), B (partly in delivery), C (completely in Delivery), D (completely shipped). | The filter is applied to the app. |  |
| 5 | Verify Chart | Choose the nodes in the chart or on a key figure in the legend.Choose View By to analyze in more dimensions, for example select Bill-To Party. | The data displayed in the table changes accordingly. The chart changes accordingly. |  |
| 6 | Navigation from Table | Choose Sales Order Id, Sold to Party ID, or Product ID to get more detailed information and navigate to the smart links available. | The target links work correctly. |  |
| 7 | View Management | You can define, save, and share separate views for filter, chart, and table sections.To apply some filters in the section, choose the Select View icon. On the My Views screen, choose Save As. On the Save View screen, enter view name and mark the necessary checkbox, then choose Save. You can also manage the view by choosing Manage on the My Views screen. | The views can be defined, saved, shared, and managed. |  |
| 8 | Share the App | Choose the Share icon at the right top of the screen. It can share the app for quick and easy accessibility. The following options listed are possible:Send EmailSave as Tile | Tile sharing with an email, or as a tile on the SAP Fiori launchpad is possible. |  |

### Customer Returns - Flexible Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this app is to gain an understanding of the customer returns.

|  |
| --- |
| Note There’s another app Customer Returns with the same functionality but for the accessibility purpose, you can access the app with same business roles. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager or Returns and Refund Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Set User Default Values | Choose the user icon and select Settings. On the Settings screen, choose Default Values. Maintain values for your user. For example, Exchange Rate Type, Display Currency. Then choose Save. | The user default values are set. |  |
| 3 | Access the App | Open Customer Returns (W0139). | The app is launched successfully. |  |
| 4 | Add Analysis Dimension | Open Navigation Panel, drag and drop the Available Fields to COLUMNS or ROWS for more analysis. | More analysis dimensions are added and the result is refreshed accordingly. |  |
| 6 | Target Navigation | Choose Data Analysis, choose Navigate To to open the navigation list. Select one of them, for example, Customer Return for more analysis. | The target app is launched successfully. |  |

### Customer Return Rate

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Return Management is an important process in many of the business cases, when the received goods are broken or not satisfied by the customer, return business would happen. However, the return business should be monitored by return clerk or sales manager so that potential issue could be identified in time, then actions could be taken accordingly. With Customer Return Rate, you as a sales manager or a return clerk can analyze the return rate for products that you are responsible for. The analysis could be high-level overview for all the products, and it could be also individual customer return.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as Sales Manager or Returns and Refund Clerk. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Customer Returns - Return Rate (F4092) . | The app launched successfully. |  |
| 3 | View by Sales Organization | Open the view drilldown list and choose By Sales Organization. | The data displayed in the graph is changed accordingly. |  |
| 4 | Switch to table view | Choose Tabular View on the screen. | The graphical view is replaced with the table view. |  |
| 5 | Drill Down to Further Dimension | Choose one sales organization and drill down with another dimension. For example, on the By Customer Return Item. | The data displayed in the graph is changed accordingly. |  |
| 6 | Navigation to Jump To Target App | Select one customer return and choose Jump To. Select one of them for further action, for example Manage Customer Returns. | The target app is opened. |  |

### Sales Volume - Flexible Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this app is to gain an understanding of the monthly sales volume. You can

- View the monthly sales volume as a graphic or a table.
- Analyze aggregated billing document item net amounts with the display currency.
- Drill down to view detailed information for selected sales organizations, sold-to parties, bill-to parties, and so on.
- Filter the items according to various criteria, such as year/month, sales organization, sold-to party, and bill-to party.
- Change the displayed ID or description.
- Save your selection as a variant.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager . | The SAP Fiori launchpad is displayed. |  |
| 2 | Set User Default Values | Choose the user icon and select Settings. On the Settings screen, choose Default Values. Maintain values for your user. For example, Exchange Rate Type, Display Currency. Then choose Save. | The user default values are set. |  |
| 3 | Access the App | Open Sales Volume - Flexible Analysis (F1250). | The app is launched successfully. |  |
| 4 | Run the Report | Choose Go. | The monthly sales volume is displayed in the table and the fields list is available on the navigation panel. |  |
| 5 | Switch to Graphical Display | Choose Graphical Display. | The graphical view is displayed.Note if you get 'Chart cannot be rendered error' because of multiple units of measure, you can either remove the affected Key Figures or set the filter criteria to avoid it. |  |
| 6 | Change Display Currency | Set Display Currency to another currency, and then choose Go. | The data displayed in the graph is changed accordingly. |  |
| 7 | Switch Back to Data Analysis | Choose Data Analysis. | The view is switched back to the list view. |  |
| 8 | Add Drilldown | Choose Drilldown and choose Add Drilldown. On the Select Fields screen, choose the required option, for example Bill-To Party. | Bill-to Party information is added. |  |
| 9 | Remove Drilldown | Choose the Bill-to Party dimension in the table, choose Drilldown, and then choose Remove Drilldown. | The drilldown added in a previous step is removed. |  |
| 10 | Drag Available Fields to Rows | On the Navigation Panel, drag a field from the Available Fields list to Rows, for example, the Company Code field. | Fields are added as rows to the table. |  |

### Sales Volume - Detailed Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Sales Volume Analysis provides analyses and comparisons for sales volume over time and according to sales organization, distribution channel, division, customer group, customer, product group, and product. It enables sales analysis experts and sales managers to identify the root cause for sales volume increase or reduction, and to identify the most important sales volume contributors.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Sales Volume - Detailed Analysis (F2235). | The app is launched successfully. |  |
| 3 | Add Analysis Step | With Add Analysis Step on the left panel, customized analysis steps can be added if necessary.For example, choose Add Analysis Step, choose Time on the Category screen. Choose Sales Volume by Year and Line Chart. | The Sales Volume by Year analysis step is added. |  |
| 4 | Switch to List View | Choose List View in the right corner. | The chart is changed to the list view. |  |
| 5 | Add More Analysis Steps | Add more analysis steps for further analysis. | More analysis steps are added. |  |
| 6 | Delete Analysis Step | Choose Delete in the right corner of a particular analysis step. | That analysis step is deleted. |  |
| 7 | Save Analysis Path | Choose Related Options next to the analysis path, and then choose Save. On the Save Analysis Path screen, enter the name and choose OK. | The analysis path is saved. |  |

### Sales Volume - Check Open Sales

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app you, as a sales manager can check your sales volume in comparison to previous months, with the additional insight of open orders and open deliveries for the current month. It enables you to see at a glance how the sales volume of the current month relates to the sales volume of the previous month. It also shows you where you can still increase your sales volume in the current period, for example, open orders, open billing requests, open deliveries. You can:

- View the monthly sales volume as a graphic or a table
- Additionally analyze open orders and open deliveries, to identify where you can act in order to increase your sales volume
- Analyze aggregated billing document, sales document, and delivery document item net amounts with the display currency
- Drill down to view detailed information for selected sales organizations, sold-to parties, product, and so on
- Filter the items according to various criteria, such as year/month, sales organization, sold-to party, and product
- Navigate directly to the Sales Order Fulfillment app to either resolve the blocks or issues yourself, or you can collaborate with the shipping manager by email
- Navigate directly to the Sales Volume – Profit Margin analysis and Sales Volume – Credit Memos analysis

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Sales Volume - Check Open Sales (F2270) . | The app is launched successfully. |  |
| 3 | Change Selection Criteria | Choose By Month to open the drilldown list, for example choose By Sold-To Party.Select some of the displayed customers for a detailed analysis.For example, choose By Product from the Current Selection menu. | After choosing By Product for a further customers analysis, the displayed graph changes and the total sales amount changes accordingly. |  |
| 4 | Change the View Settings | Choose Settings in the chart view.On the View Settings screen, select the Sort tab to sort the table by Open Orders (descending). | The table is sorted by Open Orders (descending). |  |
| 5 | Switch to Table View | Choose the tabular view on the screen. | The graphical view is replaced with the table view. |  |
| 6 | Switch Back to Graphical View | Choose the chart view on the screen. | The table view changes back to the graphical view. |  |
| 7 | Remove the Filter Condition Added Previously by Change Selection Criteria | Choose the Reset filter icon and choose OK on the Reset Filters screen. | The data displayed in the graph is changed accordingly.The total sales net amount is changed accordingly. |  |
| 8 | Display the Associated Tiles | Choose Show Mini Tiles on the screen. | Sales Volume – Profit Margin, and Sales Volume – Credit Memo are displayed. |  |
| 9 | Change Selection Criteria | Select the By Sold-To Party drilldown.Choose Add Filter at the top left of the page, choose Month of Billing on the Filter screen, and set the filter to the current month. | The data results are restricted to the current month and to customer perspective. |  |
| 10 | Find Issue and Navigate to the Associated App for Further Analysis | For example, select the Sold-To Party that has the highest number of open deliveries, then choose Jump To, Analyze and Resolve Issues. | The Sales Order Fulfillment Issues app is displayed. |  |
| 11 | Solve the Issue | In the Sales Order Fulfillment Issues app, check the issue details. Navigating to Track Sales Order Details app by clicking on the Details icon in the table will display further details and help resolve the issues. | The issue is resolved. |  |
| 12 | Navigate Back to Sales Volume – Check Open Sales App | Choose Back in the Sales Order Fulfillment Issues app. | The Sales Volume - Check Open Sales is displayed.If the issues are successfully resolved, the data in the chart is changed accordingly. |  |
| 13 | Check Jump To Function | Choose Jump To and select the target app for further action, for example, Customer . | The target app is opened. |  |
| 14 | Set App Filters | Choose Expand Header on the screen. | The Filter Bar is displayed. You can change the filter settings including the default parameters. |  |

### Sales Volume - Credit Memos

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With Sales Volume – Credit Memo, you as a sales manager can gain insights into the number of credit memos resulting from returns, complaints, and cancellations, that are, invoices that have been canceled due to internal errors in your company. From here, you can investigate the reasons for returns and complaints.

The tile provides the following top N displays: sales volume, credit memos, and cancellations. You can:

- View the monthly sales volume and profit margin amount as a graphic or a table
- Extend further dimensions via the drilldown. For example, you drill down by product, and discover a particular product has a negative profit margin
- Select the relevant billing document for the product, and display the billing document conditions to see the reason for the product low profit margin
- Drill down to view detailed information for selected sales organizations, sold-to parties, product, and so on
- Filter the items according to various criteria, such as year/month, sales organization, sold-to party, productl.
- Navigate directly to the Sales Volume - Check Open Sales (F2270) analysis

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Sales Volume - Credit Memo (F5310). | The app is launched successfully. |  |
| 3 | Change Selection Criteria | Choose By Sales Organization to open the drilldown list, for example choose By Sold-To Party.Select some of the displayed customers for a detailed analysis. For example, choose By Product from the Current Selection menu. | After choosing By Product for a further customers analysis, the displayed graph and the total credit memos are changed accordingly. |  |
| 4 | Change the View Settings | Choose Settings in the chart view. On the View Settings screen, select the tab Sort to sort the table by Credit Memos (ascending). | The table is sorted by Credit Memos(ascending). |  |
| 5 | Switch to table view | Choose the tabular view on the screen. | The graphical view is replaced with the list view. |  |
| 6 | Switch Back to Graphical View | Choose the chart view on the screen. | The list view changes back to the graphical view. |  |
| 7 | Remove the Filter Condition Added previously by Change Selection Criteria | Choose the Reset icon and choose OK on the Reset Filters screen. | The data displayed in the graph is changed accordingly.The total Credit Memos amount is changed accordingly. |  |
| 8 | Display the Associated Tiles | Choose Show Mini Tiles on the screen. | Sales Volume – Check Sales Volume and Sales Volume – Profit Margin are displayed. |  |
| 9 | Change Selection Criteria and Check the Associated Tiles | Select the By Sold-To Party drilldown. Choose Add Filter at the top left of the page, choose Fiscal Year on the Filter screen, and set the filter to current year. | The data results are restricted to the current year and to customer perspective.Additionally, the values displayed in the associated tile change according to the filter settings. |  |
| 10 | Navigate to the associated tile | Choose Sales Volume – Profit Margin . | The app is displayed for the time period previously selected. |  |
| 11 | Navigate Back to Sales Volume – Credit Memos App | Choose Back on Sales Volume – Profit Margin app. | The Sales Volume – Credit Memos app is displayed correctly with the latest filter settings. |  |
| 12 | Check Jump To Function | Choose Jump To and select the target app for further action, for example, Customer. | The target app is opened. |  |
| 13 | Set App Filters | Choose the Expand Header on the screen. | The filter bar is displayed. You can change the filter settings including the default parameters. |  |

### Sales Volume - Profit Margin

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With Sales Volume – Profit Margin, you as a sales manager can check your sales volume against your profit margin for your sales organizations. The tile of the app displays the profit margin for the top three sales organizations as a percentage, but you can also use other selection criteria. It enables you to see at a glance whether your profit margin is low for a particular sales organization or, for example, for a particular product. The profit margin is an indicator of your company pricing strategies and how well you control costs. You can collaborate with your team by email, or with other sales managers, in order to gain further insights. For example, regarding prices or discounts, and to take the necessary action in order to increase your sales volume and, as a result, your profit margin.

The tile of the app displays the profit margin for the top three sales organizations as a percentage. More details are available:

- View the monthly sales volume and profit margin amount as a graphic or a table
- Extend further dimensions via the drilldown. For example, you drill down by product, and discover a particular product has a negative profit margin
- Select the relevant billing document for the product, and display the billing document conditions to see the reason for the low profit margin of the product
- Drill down to view detailed information for selected sales organizations, sold-to parties, product, and so on
- Filter the items according to various criteria, such as year/month, sales organization, sold-to party, product
- Navigate directly to the Sales Volume - Check Open Sales (F2270) analysis

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Sales Manager . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Sales Volume - Profit Margin (F2271) . | The app is launched successfully. |  |
| 3 | Change Selection Criteria | Choose By Sales Organization to open the drilldown list, for example choose By Sold-To Party.Select some of the customers displayed for a detailed analysis. For example, choose By Product from the Current Selection menu. | After choosing By Product for a further customer analysis, the displayed graph changes and the total profit margin percentage changes accordingly. |  |
| 4 | Change the View Settings | Choose Settings in the chart view. On the View Settings screen, go to the Sort tab and sort the table by Profit Margin, Ascending. | The table is sorted by Profit Margin (ascending). |  |
| 5 | Switch to table view | Choose Tabular View on the screen. | The graphical view is replaced with the list view. |  |
| 6 | Switch Back to Graphical View | Choose Chart View on the screen. | The list view changes back to the graphical view. |  |
| 7 | Remove the Filter Condition Added by Change Selection Criteria Previously | Choose the Reset icon and choose OK on the Reset Filters screen. | The data displayed in the graph is changed accordingly.The total profit margin amount is changed accordingly. |  |
| 8 | Display the Associated Tiles | Choose Show Mini Tiles on the screen. | Sales Volume – Check Sales Volume and Sales Volume – Credit Memo are displayed. |  |
| 9 | Change Selection Criteria and Check the Associated Tiles | Choose the By Sold-To Party drilldown. Select Add Filter at the top left of the page, choose Fiscal Year on the Filter screen, and set the filter to the current year. | The data results are restricted to the current year and to the customer perspective.The values that are displayed in the associated tile have been changed according to the filter settings. |  |
| 10 | Navigate to the Associated Tiles | Choose Sales Volume – Credit Memo. | The app is displayed for the time period previously selected. |  |
| 11 | Navigate Back to Sales Volume – Profit Margin App | Choose Back on the Sales Volume – Credit Memo app. | The Sales Volume – Profit Margin app is displayed correctly with the latest filter settings. |  |
| 12 | Check Jump To Function | Choose Jump To and select the target app for further action, for example, Customer. | The target app is opened. |  |
| 13 | Set App Filters | Choose the Expand Header on the screen. | The filter bar is displayed. You can change the filter settings including the default parameters. |  |

### Sales Scheduling Agreements – Product Demand

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

With this app, you as an internal sales representative can

Have an insight of customer demand on different delivery schedule versions. It helps user see customer demands are fluctuated in certain period.

Have an insight of customer demand for one product

Have an insight between demand and supplier for one product in certain period.

Have an insight of customer demand of different products for one customer

Have a possibility of navigating from high level demand view into detail level view as well as fulfillment overview

Have an insight of delivery reliability on sales scheduling agreement

Have an insight of open schedule lines for scheduling agreements and drill down to find issue

It is possible to drill down to the detail view to analyze the demand fluctuation on schedule line level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Internal Sales Representative. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Sales Scheduling Agreements – Product Demand (F4508) . | The app is opened. |  |
| 3 | Set Filters | Set filters for Release Type, Time Period, Delivery Date Range and other filters if necessary, and then choose Go. | The chart and table are shown according to the filters. |  |
| 4 | Check Visual Filter | Click Visual Filter to change the filter mode to visual filter. | The filter is changed to Visual Filter and it’s consistent with Compact Filter. |  |
| 5 | Drill Down in Chart and Table | Choose View By in the chart to analyze in more dimensions, for example select Sales Organization. | The data displayed in the chart and table changes accordingly. |  |
| 6 | View Settings | Choose Settings in chart view, more settings can be done for Chart, Sort and Filter.Choose Settings in table view, more settings can be done for Columns, Sort, Filter and Group. | The Chart and Table can be set as needed. |  |
| 7 | View Management | You can define, save, and share separate views for filter, chart, and table sections.To apply some filters in the section, choose the Select View icon. On the My Views screen, choose Save As. On the Save Viewscreen, enter view name and mark the necessary checkbox, then choose Save. You can also manage the view by choosing Manage on the My Views screen. | The views can be defined, saved, shared, and managed. |  |
| 8 | Share the App | Choose the Share icon at the right top of the screen. It can share the app for quick and easy accessibility. The following options listed are possible:• Send Email• Save as Tile | Tile sharing with an email, or as a tile on the SAP Fiori launchpad is possible. |  |

### Customer Returns Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This app provides real-time insights into customer returns KPIs including customer return value, no. of return items and return rate, and analyze across various dimensions such as sales area, sales office, sold-to party, customer group, product, product group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Customer Returns Overview (F4561) . | The app is opened.There are two pages in the story, Profile and Trend. |  |
| 3 | Set Prompt | Choose Edit Prompts on top right, and select a query to set the prompt. For example, change the Display Currency. | The prompt is set. |  |
|  | Page Profile |  |  |  |
| 4 | Filter Page Time Range | Click top left filter Created On to change the time range. | By default, the time range of the page is set to Current Month. You can change to Current Quarter or Current Year. The page will be refreshed. |  |
| 5 | Filter Dimensions | Click any dimension filter on the top to set filters. | The data displayed in the page changes accordingly. |  |
| 6 | Change Dimension Selection | Choose other option in Dimension on the left side of the page. | The analysis dimension is changed, the table and bar chart are refreshed. |  |
| 7 | Change Measure Selection | Choose other option in Measure on the left side of the page. | The analysis measure is changed, the donut and bar chart are refreshed. |  |
| 8 | Linked Analysis | Choose data point in table or donut chart. | The bar chart is filtered by the selected data point. |  |
| 9 | Explore the Charts | Choose Explorer Available on the charts, select measures or dimensions for further analysis, and then save as explorer view. The explorer view can be saved via variant management. | Customized explorer view are saved. |  |
|  | Page Trend |  |  |  |
| 10 | Filter Page Time Range | Click top left filter Created On to change the time range. | By default, the time range of the page is set to Last 6 months. You can change to other time range and the page will be refreshed. |  |
| 11 | Change Dimension Selection | Choose Month or Quarter in Granularity to change the time dimension of the upper 2 charts | The time dimension is changed, the upper charts are refreshed. |  |
| 12 | Change Measure Selection | Choose other option in Measure on the left of the lower chart. | The analysis measure is changed, the chart is refreshed. |  |
| 13 | Explore the Charts | Choose Explorer Available on the charts, select measures or dimensions for further analysis, and then save as explorer view. The explorer view can be saved via variant management. | Customized explorer view are saved. |  |

### Order to Cash Dashboard

Order to Cash Dashboard

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This app Identify the areas where corrective measures have to be taken for sales using the sales volume and profit margin dashboards. Identify such hotspots for sales & after-sales service in a single view of incoming orders and take action accordingly.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Sales Manager. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Order to Cash Dashboard (F4663) . | The app is opened. There are 3 pages in the story: Sales Volume, Profit Margin and Incoming Orders. |  |
| 3 | Set Prompt | Choose Edit Prompts on top right, and select a query to set the prompt. For example, change the Display Currency. | The prompt is set. For example, Display Currency is changed. |  |
|  | Page Sales Volume |  |  |  |
| 4 | Change Page Time Range | Click top left filter Billing Date to change the time range. | By default, the time range of the page is set to Current Month. You can change to Current Quarter or Current Year. The page will be refreshed. |  |
| 5 | Filter Dimensions | Click any dimension on the top to set filters. For example, Sales Organization. | The data displayed in the page changes accordingly. |  |
| 6 | Change time range for Time Trend Chart | Click on 1 Filter on the chart, change the time to another range. | By default, the chart is filtered by last 6 months. You can change as needed and the chart will be refreshed. |  |
| 7 | Change Dimension Selection | Choose other option in the Dimension on the left side of below 2 charts. | The dimension is changed, the charts are refreshed. |  |
| 8 | Explore the Charts | Choose Explorer Available on the charts, select measures or dimensions for further analysis, and then save as explorer view. | Explorer mode is on and explorer view can be saved. |  |
|  | Page Profit Margin |  |  |  |
| 9 | Change Page Time Range | Click top left filter Billing Date to change the time range. | By default, the time range of the page is set to Current Month. You can change to Current Quarter or Current Year. The page will be refreshed. |  |
| 10 | Change Dimension Selection | Choose Billing Month/Year or Billing Quarter/Year to change the time dimension of the upper left chart.Choose other option in the Dimension of the upper right chart. | The time dimension is changed, the upper charts are refreshed. |  |
| 11 | Change Top N Settings | Choose Top 5 in the chart, and change the Top N settings. For example, change to Top 10. | By default, we set Top 5 in charts. You can change as needed and the chart will be refreshed. |  |
|  | Page Incoming Orders | Note In order to display after-sales service data, business catalog SAP_S4CRM_BC_ANA_SLS_SRVC_PC need to be assigned to the role. |  |  |
| 12 | Change Page Time Range | Click top left filter Created on to change the time range. | By default, the time range of the page is set to Current Month. You can change to Current Quarter or Current Year. The page will be refreshed. |  |
| 13 | Change Time Range for Time Trend Chart | Click on 1 Filter on the chart, change the time to another range. | By default, the chart is filtered by last 6 months. You can change as needed and the chart will be refreshed. |  |
| 14 | Change Dimension Selection | Choose other option in the Dimension on the left side of bottom 2 charts | The dimension is changed, the charts are refreshed. |  |

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
- related-to :: [[08-sales-order-management/test-script-sales-order-fulfillment-monitoring-and-operations-bkk-ae-1]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/1BS_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 71,791 chars in the whole document
