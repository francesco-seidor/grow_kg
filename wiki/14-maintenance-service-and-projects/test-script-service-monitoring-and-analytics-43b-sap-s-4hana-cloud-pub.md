---
id: 14-maintenance-service-and-projects/test-script-service-monitoring-and-analytics-43b-sap-s-4hana-cloud-pub
title: "Test Script: Service Monitoring and Analytics (43B) - SAP S/4HANA Cloud Public Edition (43B_S4CLD2608_BPD_EN_XX)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 43B: service contract/order monitoring, issues, flexible analysis, solution order and O2C dashboards."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-monitoring-and-analytics]
aliases: [43B_S4CLD2608_BPD_EN_XX]
keywords: [Service Monitoring and Analytics, service management overview, service contract issues, service order issues, flexible analysis apps, solution orders, service contracts dashboard, order to cash dashboard, insights cards, situation handling]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/43B_S4CLD2608_BPD_EN_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-998
topic: 14-maintenance-service-and-projects/service-monitoring-and-analytics
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Service Monitoring and Analytics (43B) - SAP S/4HANA Cloud Public Edition (43B_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/43B_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Service Monitoring and Analytics** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Service Monitoring and Analytics (43B) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232841063)

[2 Prerequisites 4](#_Toc232841064)

[2.1 System Access 4](#_Toc232841065)

[2.2 Roles 4](#_Toc232841066)

[2.3 Settings for Situation Handling 5](#_Toc232841067)

[3 Overview Table 7](#_Toc232841068)

[4 Test Procedures 9](#_Toc232841069)

[4.1 Service Management Overview 9](#_Toc232841070)

[4.1.1 Review Service Contract Items for Expiry/Renewal 9](#_Toc232841071)

[4.1.2 Review Service Contracts by Total Contract Value/Profit Margin 10](#_Toc232841072)

[4.1.3 Review Overdue Service Orders 12](#_Toc232841073)

[4.1.4 Review Incomplete Service Orders 13](#_Toc232841074)

[4.1.5 Monitor Average Service Duration by Product 15](#_Toc232841075)

[4.1.6 Review Expired Service Contracts 16](#_Toc232841076)

[4.1.7 Review Service Contract Items 17](#_Toc232841077)

[4.1.8 Verify Quick Links 18](#_Toc232841078)

[4.2 Service Contracts 19](#_Toc232841079)

[4.2.1 Service Contract Issues 19](#_Toc232841080)

[4.2.1.1 Analyze Service Contract Issues - Graphical Overview 19](#_Toc232841081)

[4.2.1.2 Analyze Service Order Issues by Country and Region 20](#_Toc232841082)

[4.2.1.3 Analyze Service Contract Issues by Service Transactions 21](#_Toc232841083)

[4.2.1.4 Analyze Service Contract Issues by Sales Organization 22](#_Toc232841084)

[4.2.1.5 Analyze Service Contract Issues - Mini Tiles 22](#_Toc232841085)

[4.2.2 Service Contracts – Flexible Analysis 23](#_Toc232841086)

[4.2.3 Service Contract Items - Flexible Analysis 25](#_Toc232841087)

[4.2.4 Service Contracts Dashboard 26](#_Toc232841088)

[4.2.5 Insights Cards for Service Contracts (Optional) 27](#_Toc232841089)

[4.3 Solution Orders 28](#_Toc232841090)

[4.3.1 Solution Order Items - Flexible Analysis 28](#_Toc232841091)

[4.3.2 Journal Entries for Solution Orders - Flexible Analysis 29](#_Toc232841092)

[4.3.3 Solution Orders - Flexible Analysis 30](#_Toc232841093)

[4.3.4 Insights Cards for Solution Orders (Optional) 31](#_Toc232841094)

[4.4 Service Orders 32](#_Toc232841095)

[4.4.1 Service Order Issues 32](#_Toc232841096)

[4.4.1.1 Analyze Service Order Issues - Graphical Overview 32](#_Toc232841097)

[4.4.1.2 Analyze Service Order Issues by Country and Region 33](#_Toc232841098)

[4.4.1.3 Analyze Service Order Issues by Service Transactions 34](#_Toc232841099)

[4.4.1.4 Analyze Service Order Issues by Sales Organization 35](#_Toc232841100)

[4.4.1.5 Analyze Service Order Issues - Mini Tiles 35](#_Toc232841101)

[4.4.2 Service Orders – Flexible Analysis 37](#_Toc232841102)

[4.5 Order to Cash Manager Dashboard – Incoming Sales & Services 38](#_Toc232841103)

## Purpose

Overview

This scope item helps the customer service manager ensure on-time service delivery by monitoring incomplete or overdue service orders. This scope item also helps to compare the average repair time per product.

The customer service manager must also know how many service contracts will expire soon. The customer service manager can compare and view the service contracts from various dimensions, such as total contract value and profit margin. The customer service manager can also trigger actions to renew them.

This scope item helps to display and monitor a variety of issues in service contracts and service orders. It supports a detailed analysis of the issues by displaying the results by issue, service transaction, country, region, and sales organization. You can use various chart types, mini charts, and filters for analyzing, monitoring, and discovering additional information, and focusing on certain data, such as service transactions.

The manager can use the flexible analysis apps to analyze service orders and service-contract-related KPIs in multidimensional reports.

In addition, the service contracts dashboard helps the customer service manager to analyze the contracts in further detail.

As a sales manager, you can use the Order to Cash dashboard to analyze incoming and open service orders.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data, and business conditions.

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
| Customer Service Manager | SAP_BR_CUSTOMER_SRVC_MGR | Service Management / Service Management – SAP Field Service and Asset Management | SAP_BR_CUSTOMER_SRVC_MGR / SAP_S4CRM_SPT_FSM_PC | Your system administrator provides the user and password information. |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC | Your system administrator provides the user and password information. |
| Sales Manager | SAP_BR_SALES_MANAGER | Sales Management / Internal Sales / Billing for Sales Manager / Customer Returns for Sales Manager | SAP_BR_SALES_MANAGER / SAP_SD_SPT_INT_SALES_SALES_MGR_PC / SAP_SD_SPT_BILLING_SALES_MGR_PC / SAP_SD_SPT_RETURNS_SALES_MGR_PC | Your system administrator provides the user and password information. |

### Settings for Situation Handling

Purpose

Situation handling recognizes business situations by evaluating conditions (rules) on business facts. A business situation occurs when a business object changes a status relevant to a user, when critical deadlines are passed, or a KPI passes a threshold.

Prerequisite

Notifications are only created in the system once the required configurations in the situation template (including notification recipient settings) are set up.

This additional configuration steps should be carried out by customers to activate situation handling.

|  |
| --- |
| Note If you want to use situation handling with any of the service scope items, you have to implement the scope item 31N. |

If you want to use situation handling with any of the service scope items, you have to include also scope item Situation Handling (31N).

To set up situation handling, create your ready-to-use situation type, maintain the message to be displayed, define the conditions when the situation will be triggered, define recipient groups who will receive notifications, and monitor the instances. For more information, see the Set-Up Instructions for the scope item Situation Handling (31N).

For more information, see the Set-Up Instructions for the scope items [Situation Template in Service](https://help.sap.com/viewer/adbae5bcd5994f159bf2847a11397b61/latest/en-US/9d6cee508b2e44a39e93474ee68e6ba9.html).

The standard situation templates are defined and delivered by SAP :

- Solution Order
- Service Contract
- In-house Repair
- Service Order Management
- Service and Maintenance Plan

For each situation template, a corresponding responsibility rule is defined in which the responsible person to be notified can be assigned.

For more information and situation template details (default settings, conditions, notification recipients), see documentation :

- [Situation Template for Solution Orders](https://help.sap.com/viewer/a376cd9ea00d476b96f18dea1247e6a5/latest/en-US/40110bff6b874b1c8b2630b944b95a60.html).

|  |
| --- |
| Note If you want to test situation handling with various scope items, run the steps that are described in the Test Script of scope item .You can also refer to the Preliminary Steps in the following sope items for more information: |

- Solution Order Management (4GT)
- Service Contract Management (3MO)
- Inhouse Repair (3XK)
- Service Order Management (3D2)
- Service and Maintenance Plan (4X5)

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Topic | Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- | --- |
| Service Management Overview | [Review Service Contract Items for Expiry/Renewal](#unique_7) | Customer Service Manager | Expiring Service contracts | Expiring Service contracts based on profits are displayed |
| [Review Service Contracts by Total Contract Value/Profit Margin](#unique_8) | Customer Service Manager | Service Contract by Value/Profit | Service Contracts by Contract Value/Marginare displayed |  |
| [Review Overdue Service Orders](#unique_9) | Customer Service Manager | Overdue Service Orders | Overdue Service orders are displayed |  |
| [Review Incomplete Service Orders](#unique_10) [page ] 13 | Customer Service Manager | Incomplete Service orders | Incomplepte Service Orders are displayed |  |
| [Monitor Average Service Duration by Product](#unique_11) [page ] 15 | Customer Service Manager | Average Service Duration | Bar graph is displayed showing top 4 products with maximum Average Repair time |  |
| [Review Expired Service Contracts](#unique_12) | Customer Service Manager | Expired Service Contracts | Expired Service Contracts are displayed. |  |
| Service Contracts | [Analyze Service Contract Issues - Graphical Overview](#unique_13) | Customer Service Manager | Service Contract Issues > Issues | Issues are listed in categories |
| [Analyze Service Contract Issues by Country and Region](#unique_14) | Customer Service Manager | Service Contract Issues > Country and region | Issues are listed according to country and region |  |
| [Analyze Service Contract Issues by Service Transactions](#unique_15) | Customer Service Manager | Service Contract Issues > Service Contracts | Issues are listed based on service contracts |  |
| [Analyze Service Contract Issues by Sales Organization](#unique_16) | Customer Service Manager | Service Contract Issues > Sales Organization | Issues are listed based on sales organization |  |
| [Analyze Service Contract Issues - Mini Tiles](#unique_17) | Customer Service Manager | Service contract issues > Show Mini Tiles | Service contracts mini tiles are displayed |  |
| [Service Contracts – Flexible Analysis](#unique_18) [page ] 23 | Customer Service Manager | Service Contracts - Flexible Analysis | Data Analysis and Graphical Display are displayed. |  |
| Service Orders | [Analyze Service Order Issues - Graphical Overview](#unique_19) | Customer Service Manager | Service Order Issues Issues | Issues are listed in categories |
| [Analyze Service Order Issues by Country and Region](#unique_20) | Customer Service Manager | Service Order Issues Country and Region | Issues are listed according to country and region |  |
| [Analyze Service Order Issues by Service Transactions](#unique_21) | Customer Service Manager | Service Order Issues Service Orders | Issues are listed based on service orders |  |
| [Analyze Service Order Issues by Sales Organization](#unique_22) | Customer Service Manager | Service Order Issues Sales Organization | Issues are listed based on sales organization |  |
| [Analyze Service Order Issues - Mini Tiles](#unique_22) | Customer Service Manager | Service Order Issues Show Mini Tiles | Service order mini tiles are displayed |  |
| [Service Orders – Flexible Analysis](#unique_23) [page ] 37 | Customer Service Manager | Service orders- Flexible Analysis | Data Analysis and Graphical Display are displayed. |  |
|  | [Order to Cash Manager Dashboard – Incoming Sales & Services](#unique_24) [page ] 38 | Sales Manager | Sales Analytics for Sales & Service | Screen is Navigated Order to Cash dashboard page |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Service Management Overview

#### Review Service Contract Items for Expiry/Renewal

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To review the Expiring Service Contract card in Service Management overview that displays Service contract Items in Months.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Service Management Overview app is displayed under Service Management Analytics . | The Service Management Overview app is displayed. |  |
| 3 | View app | View Expiring Service Contract Items app, it has filter option to choose Service Contract either ‘By Contract Value’ or ‘By Number’. | The screen shows Expiring service contracts based on ‘By Contract value’ or ‘By Number’. |  |
| 4 | Choose Expiring Service Contract Items | Choose Expiring Service Contracts Items based on Contract value or Number. | The screen is navigated to Expiring Service Contract Analysis displaying the Expiry period of service contracts and details of the service contracts. |  |
| 5 | Choose Visual Filter | Choose Visual Filter to display the visual filter section. | The visual filter of Expiring Service Contracts by Sales Organization is shown. |  |
| 6 | Choose Filters on Standard tab | Choose Compact filter - Choose display currency for desired currency and select the contract end date.For desired Sales groupselect sales organization → distribution channel → division → sales office → sales group. (in a hierarchical order). | The content chart shows the service contracts expired Month wise for that sales organization and for the selected Contract end date range. |  |
| 7 | Adopt | Choose Sales organizations (from the different sales org number displayed).Service contracts due to expire in a Month/Months can be viewed by updating the Contract End Date in filters.Choose Go. | The content chart shows the service contracts expired Month wise default for that sales organization. |  |

#### Review Service Contracts by Total Contract Value/Profit Margin

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To review the service contracts by contract value / profit margin.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Service Management Overview app is displayed under Service Management Analytics . | The Service Management Overview app is displayed. |  |
| 3 | View Service contract by Contract value app | This app has a filter with an option 'Highest Value/Lowest Value' which helps to know which service contract has highest/lowest contract value. By default, the filter is set to ‘Highest Value’. | The Screen shows the app with Highest Contract Value Service contracts. |  |
| 4 | Review Service contract by contract value | Select Service Contracts by Contract Value.This card has a filter with an option ‘highest value/lowest value’ which helps to know which service contract has the highest/lowest value. (by default, highest value is displayed). | The Screen is navigated to service contract Analysis and table showing the Service contracts by contract value is displayed. |  |
| 5 | View Service contract by Profit Margin app | This card has a filter with an option ‘Most Profitable/Least Profitable’ which helps to know which service contract is most/least profitable.By default, the filter is set to ‘Most Profitable’. | The Screen shows the app with Highest contract value. |  |
| 6 | Review Service contract by Profit margin | Choose Service Contracts by Profit Margin. This card has a filter with an option ‘most profitable/least profitable’ which helps to know which service contract is the most/least profitable. (by default, most profitable is displayed). | The Screen is navigated to Service Contract Analysis and Table showing the Service contracts by contract value is displayed. |  |
| 7 | Choose Additional filters | Select one of the filters:By ContractBy region'By sales OrganizationYear to Date - By sales OrganizationRevenue , Cost and Profit Margin - By Month | The table is displayed based on contract, region, and sales organization. |  |
| 8 | Choose Filters on Standard tab | Select display currency for desired currency.For desired sales group:Select sales organization > distribution channel > division > sales office > sales group. (in a hierarchical order). | The number of figures in the cards will be displayed in the desired currency and for desired sales group.These filters help to view the information specific to sales organization. |  |

#### Review Overdue Service Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose is to review “Overdue Service Orders” Card in Service management overview page displaying service Orders with requested end date in past having Open ,In process and released status.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Choose the app Service Management Overview displayed under Service Management Analytics . | The Service Management Overview app is displayed. |  |
| 3 | Review Overdue Service Orders | Choose Overdue Service Orders. | The screen is navigated to overdue service orders analysis and Net Value by Service Order Type, Service Order Items by Life Cycle Status and Overdue Service Order Items are displayed in graph and tabular format. |  |
| 4 | Select Required Overdue Service Order | Choose required Overdue Service Orders based on priority from the Overdue service order Items table. | The screen is navigated to Manage service orders app. |  |
| 5 | Select Visual Filter | Select Net Value by Service Order Type and Service Order Items by Life Cycle Status.For example, select SV01 service order and Released Service order items by Life Cycle status. | The screen displays Service order SV01 and Released Service orders based on priority. |  |
| 6 | Compact Filter | Choose Compact Filter.Select display currency for desired currency.For desired sales groupselect sales organization → distribution channel → division → sales office → sales group. (in a hierarchical order). | The Screen displays all Overdue Service orders based on the filters selected.These filters help to view the information specific to sales organization. |  |
| 7 | Select Additional Filter | Select the Service Order Type filter. | The below mentioned Value help options are displayed.Fixed price Service OrderService Order |  |
| 9 | Select Different Value Help Options | Repeat the step 6. | The KPI’s related to Service order - Service Orders, Incomplete Service Orders, Overdue Service orders displays data according to value selected in value filter. |  |

#### Review Incomplete Service Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose is to review "Incomplete Service Orders” Card in Service management overview page displaying service Orders based on three filters. 1. Service confirmation existing 2. Doc Type 3. Priority.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Service Management Overview app is displayed under Service Management Analytics . | The Service Management Overview app is displayed. |  |
| 3 | Review Incomplete Service Orders | Choose Incomplete Service Orders. | The screen is navigated to Service Order Analysis and Net value by Service order Type, Service Order Items by Life Cycle Status and Service Orders by Requested End is displayed by default. |  |
| 4 | Choose Visual Filter | Choose visual filters such as Net Value by Service Order Type and Service Order Items by Life Cycle Status.For example, Choose Service order SVO1 under Net Value by Service Order Type and Released status (D) under Service Order Items by Life Cycle status. | The service orders are displayed as bar graph and as tabular form based on their priority. Select the desired service orders based on priority. |  |
| 5 | Verify Service Order by Requested End Date | Choose Visual filter Service Order by Requested End. | All incomplete service orders by its Requested End Date by week range is displayed. |  |
| 6 | Adapt Filter | Choose Adapt Filter - Choose More Filters.To see possible Date filters and select one as required . | The list is displayed showing different Date Filters such asService Orders by Requested StartService Orders by Planned StartService Orders by Planned EndService Orders by First Response ByService Orders by Due By |  |
| 7 | Cancel | Choose Cancel twice to go back to the main screen. |  |  |
| 8 | Choose required Date filter | Repeat step 5 if you want to select an additional filter. | Incomplete Service orders are displayed based on selected Date Filters. |  |
| 9 | Verify Service order by Requested End Date | Choose Compact Filter - Choose Requested End.Choose Go - Choose required Week Number. | All incomplete service orders by its Requested End Date by week range is displayed. |  |
| 10 | Adapt Filter | Choose Adapt Filter - Choose More Filters. | The list is displayed showing different Date Filters such asDue ByFirst Response ByPlanned EndPlanned StartPriorityRequested StartProductResponsible EmployeeService TeamShip-To PartySolution Order |  |
| 11 | Choose Required Date filter | Repeat step 8. | Incomplete Service orders are displayed based on selected Date Filters. |  |
| 12 | Select Filters on Standard tab | Select display currency for desired currency.For desired sales groupSelect sales organization -- distribution channel -- division - sales office - sales group. (in a hierarchical order). | The number of figures in the cards will be displayed in the desired currency and for desired sales group.These filters help to view the information specific to sales organization. |  |
| 13 | Select Additional filter | Select the Filter Service order type . | The below mentioned Value help options are displayed.Fixed price Service OrderService Order |  |

#### Monitor Average Service Duration by Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To Monitor the average repair time required for the service orders by top four products with maximum average repair time.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Service Management Overview app is displayed under Service Management Analytics . | The Service Management Overview app is displayed. |  |
| 3 | Monitor Average Service Duration | On Average Service Duration By Product/Equipment for Service order. | The Bar graph showing Top 4 Products with service Orders having maximum Average Service Duration is displayed. |  |

#### Review Expired Service Contracts

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To view the expired service contract by contract value.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Service Management Overview app is displayed under Service Management Analytics . | The Service Management Overview app is displayed. |  |
| 3 | View Expired Service Contracts app | This app has a filter with an option 'Highest Value/Lowest Value' which helps to know which Expired service contract has Highest/Lowest value. | The Screen shows the app with the Highest value for expired service contracts. |  |
| 4 | Open Expired Service Contracts app | Choose Expired Service contract app | The app is navigated to Manage Service Contracts app |  |
| 5 | Choose Service Contract | Choose Service Contract from the table | The app is navigated to selected Service Contract app which shows details of expired service contract. |  |

#### Review Service Contract Items

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To review the service contract items by Product or by Sold-To Party.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Service Management Overview app is displayed under Service Management Analytics. | The Service Management Overview app is displayed. |  |
| 3 | View Service Contract Items app | This app has a filter with an option 'By Product/By Sold-To Party' which helps to know filter service contract item by Products and Sold-To Party. | The Screen shows the app with Highest Contract Value Service contracts. |  |
| 4 | Review Service contract Items | Choose Service Contracts Items.This card has a filter with an option By Product/By Sold-To Party. | The Manage Service Contracts screen is displayed. |  |

#### Verify Quick Links

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

To verify Quick Links in Service Management Overview app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Service Management Overview app is displayed under Service Monitoring and Analytics. | The Service Management Overview app is displayed. |  |
| 3 | View Quick Links app | This app has quick links for apps such asService Orders - Flexible AnalysisService Contracts - Flexible AnalysisService Order IssuesService Contract Issues | The Screen shows the app with the Quick Links for different apps. |  |
| 4 | Open Service Orders - Flexible Analysis app | Choose Service Orders - Flexible Analysis app. | The app is navigated to Service Orders - Flexible Analysisapp. |  |
| 5 | Open Service Contracts - Flexible Analysis app | Choose Service Contracts - Flexible Analysis app. | The app is navigated to Service Contracts - Flexible Analysisapp. |  |
| 6 | Open Service Order Issues app | Choose Service Order Issues app. | The app is navigated to Service Order Issuesapp. |  |
| 7 | Open Service Contract Issues app | Choose Service Contract Issues app. | The app is navigated to Service Contract Issuesapp. |  |

### Service Contracts

#### Service Contract Issues

##### Analyze Service Contract Issues - Graphical Overview

Purpose

Analyze the list of released service contracts that includes various key performance indicators displayed as cards.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. | The Home screen is displayed. |  |
| 2 | View App | Service Contract Issues app is displayed under Service Monitoring and Analytics | Service Contract Issues app displays the total number of issues in Service Contracts |  |
| 3 | Access Service Contract Issues | Access Service Contract Issues app to View the different issue types represented in graphical format. | The Graph displays the number of issues for each of the issue type in service contracts. |  |
| 4 | Select Issue type in Service Contracts | Select an issue type to further filter on different criteria. | List of other filter criteria is displayed for the user when one of the issue types is selected. |  |
| 5 | Select Additional Filter Criteria | Select one of the Filter Criteria available to further filter out the issues. | Additional Filter criteria is applied, and the list is updated accordingly |  |

##### Analyze Service Order Issues by Country and Region

Purpose

Analyze the service orders and sort them by applying the filter on country and region. This helps in filtering out the issues specific to each of the country or region.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. | The Home screen is displayed. |  |
| 2. | View App | Service Order Issues app is displayed under Service Monitoring and Analytics | Service Order Issues app displays the total number of issues in service orders. |  |
| 3. | Access 'Service Orders Issues' | Access Service Orders Issues app to View the different issue types represented in graphical format. | The Graph displays the number of issues for each of the issue type in service orders. |  |
| 4. | Select Filter on Country and region | Select Country and Region option from the drop down menu to apply this filter. | The graph now displays the issues for each of country / region. |  |
| 5. | Select Issue for a Country / Region | Select an issue from the graph for a country or region to view details and option to further filter the results. | Details are displayed along with the available filter options. |  |
| 6. | Select Additional Filter Criteria | Select one of the filter criteria available to further filter out the issues. | Additional filter criteria is applied, and the list is updated accordingly. |  |

##### Analyze Service Contract Issues by Service Transactions

Purpose

Analyze the service contract issues by filtering on service transaction type and this will give a list of issues for each of the transaction types.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. | The Home screen is displayed. |  |
| 2 | View App | Service Contract Issues app is displayed under Service Monitoring and Analytics. | Service Contract Issues app displays the total number of issues in Service Orders |  |
| 3 | Access 'Service Contracts Issues' | Access Service Contract Issues app to view the different issue types represented in graphical format. | The graph displays the number of issues for each of the issue type in service contracts. |  |
| 4 | Select Filter on Service Contracts | Select Service Contracts option from the drop down menu to apply this filter. | Issues are displayed as a list based out of all the service contracts. |  |
| 5 | Select a Service Contract | Select an issue from the list of service contracts to view details and option to further filter the results. | Details are displayed along with the available filter options. |  |
| 6 | Select Additional Filter Criteria | Select one of the filter criteria available to further filter out the issues. | Additional filter criteria is applied, and the list is updated accordingly. |  |

##### Analyze Service Contract Issues by Sales Organization

Purpose

Analyze the service contract issues by filtering on sales organization and this will list out issues for each of the Service organization.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. | The Home screen is displayed. |  |
| 2 | View App | Service Contract Issues app is displayed under Service Monitoring and Analytics. | Service Contract Issues app displays the total number of issues in Service Contracts. |  |
| 3 | Access 'Service Contract Issues' | Access Service Contract Issues app to view the different issue types represented in graphical format. | The graph displays the number of issues for each of the issue type in service contracts. |  |
| 4 | Select Filter on Sales Organization | Select Sales Organization from the drop down menu to apply this filter. | Number of Issues for each of the sales organization is displayed in graphical format. |  |
| 5 | Select a Sales Organization | Select Sales Organization from the graph to View details with an option to further filter the results. | Details are displayed along with the available filter options. |  |
| 6 | Select Additional Filter Criteria | Select one of the filter criteria available to further filter out the issues. | Additional Filter criteria is applied, and the list is updated accordingly. |  |

##### Analyze Service Contract Issues - Mini Tiles

Purpose

Use the mini tiles feature to get an overview of service contract issues in different dimensions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. | The Home screen is displayed. |  |
| 2 | View App | Service Contract Issues app is displayed under Service Monitoring and Analytics | Service Contract Issues app displays the total number of issues in Service Contracts |  |
| 3 | Access 'Service Contract Issues' | Access Service Contract Issues app to View the different issue types represented in graphical format. | The Graph displays the number of issues for each of the issue type in service contracts. |  |
| 4 | Select Show Mini Tiles option | ChooseShow Mini Tiles option displayed at the top right corner of the screen. | The following mini tiles are displayed for Service Contract issues1. Billing Block2. Contains Error3. Rejected |  |
| 5 | Select Billing Block Mini Tile | Select Billing Block Mini Tile from the Mini Tiles view. | Issues related to billing block reason are displayed in the graph. |  |
| 6 | Select Contains Error Mini Tile | Select Contains Error Mini Tile from the Mini Tiles view. | Service Contracts containing errors are displayed in the graph. |  |
| 7 | Select Rejected Mini Tile | Select Rejected Mini Tile from the Mini Tiles view. | Contract issues which are rejected are displayed in the graph. |  |

#### Service Contracts – Flexible Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Purpose is to view the details of Service Contracts in Data Analysis and in Graphical display..

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Search Service Contracts Flexible Analysis app . | The Service Contracts Flexible Analysis app is displayed. |  |
| 3 | Review app | Choose the Service Contracts Flexible Analysis app. | The Screen is navigated to the Service Contracts -Flexible Analysis app showing Default filters as Display Currency , Earliest Contract Start, Latest Contract End, Life Cycle Status ,Sold to Party , Sales Organization.. |  |
| 4 | Click Navigation Panel | Choose navigation panel. | Different options such as Dimensions, Rows, Columns and Available Fields are displayed. |  |
| 5 | Add Filters | Chooses filtersCurrency – EUREarliest Contract Start: Earliest dateLatest Contract End:Latest dateLife Cycle Status: ReleasedSold to Party -17100001Sales Organization :1710Choose Go. | The results for Data Analysis and Graphical Display are displayed. |  |
| 6 | Jump to | Click on Jump to option. | You should be able to view & navigate below appsCreate Service ContractExpiring Contract DetailsManage Service contracts |  |

#### Service Contract Items - Flexible Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Purpose is to view the details of Service Contract Items - Fexible Analysis in Data Analysis and in Graphical display..

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Search Service Contract Items - Flexible Analysis app . | The Service Contracts Flexible Analysis app is displayed. |  |
| 3 | Review app | Choose the Service Contracts Flexible Analysis app. | The Screen is navigated to the Service ContractItems app showing Default filters as Display Currency , Posting Date, Service Contract, Item Life Cycle Status ,Sold to Party , Sales Organization, Distribution Channel and Division. |  |
| 4 | Click Navigation Panel | Choose navigation panel. | Different options such as Dimensions, Rows, Columns and Available Fields are displayed. |  |
| 5 | Add Filters | Chooses filtersDisplay Currency – EURPosting Date:Service Contract:Latest dateItem Life Cycle Status: ReleasedSold to Party -10100001Sales Organization :1010Distribution Channel : 10Division:00Choose Go. | The results for Data Analysis and Graphical Display are displayed. |  |
| 6 | Jump to | Click on Jump to option. | You should be able to view & navigate below appsService Contract – Flexible AnalysisExpiring Service Contract AnalysisManage Service contractsCreate Service ContractCreate Service Contract Template Follow upService Contracts Dashboard |  |

#### Service Contracts Dashboard

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

SAP Analytics Cloud (SAC) provides a comprehensive tool for strategic live-data analysis in solution business. The Purpose is to help the Sales Manager to review the Service Contract that are going to expire or Service contract that has maximum profitability.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the app | Choose app Service Contracts Dashboard | The Service Contracts Dashboard app is displayed. |  |
| 3 | Overview Page | Choose Overview from the dropdown. | The Overview page shows Net Value of Service Contracts and Net Value of Canceled Service Contracts. |  |
| 4 | Service Contract Item Details | Choose Service Contract Item Details from the dropdown. | The Service Contract Item Details page shows Net Value of Service Contract Items and Service Contract Item Details. |  |

#### Insights Cards for Service Contracts (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Purpose is to view the details of Insight Cards for Service Contracts which helps to view Service Contract by contract value by Sold-To Party and by Product.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Choose Service Contracts by Product app under InsightsDisplays the service contracts by Product. | The Manage Service Contracts app is displayed where additional details related to Service Contracts can be obtained. |  |
| 3 | Open app | Choose Service Contracts By Sold-To Party app under Insights.Displays the top five Service Contracts by sold-to party. | The Manage Service Contracts app is displayed where additional details related to Service Contracts can be obtained. |  |

### Solution Orders

#### Solution Order Items - Flexible Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Purpose is to view the details of Solution Order Items - Flexible Analysis in Data Analysis and in Graphical display..

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Sales Manager. | The Home screen is displayed. |  |
| 2 | Open app | Search Solution Order Items - Flexible Analysis app . | The Solution Order Items - Flexible Analysis app is displayed. |  |
| 3 | Review app | Choose the Solution Order Items- Flexible Analysis app. | The Screen is navigated to the Solution Orders app showing Default filters as Display Currency , Posting Date, Solution Order, Sales office , Sales Group , Sold to Party , Sales Organization, Distribution Channel Division and Item Life Cycle Status |  |
| 4 | Click Navigation Panel | Choose navigation panel. | Different options such as Dimensions, Rows, Columns and Available Fields are displayed. |  |
| 5 | Add Filters | Chooses filtersDisplay Currency – EURPosting Date:Solution order:Latest dateItem Life Cycle Status: ReleasedSold to Party -10100001Sales Organization :1010Distribution Channel : 10Division:00Choose Go. | The results for Data Analysis and Graphical Display are displayed. |  |

#### Journal Entries for Solution Orders - Flexible Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Purpose is to verify Query report for "Journal Entries for Solution Orders-Flexible Analysis".

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Sales Manager. | The Home screen is displayed. |  |
| 2 | Open app | Search Journal Entries for Solution Orders - Flexible Analysis app . | The Journal Entries for Solution Orders - Flexible Analysis app is displayed. |  |
| 3 | Review app | Choose the Journal Entries for Solution Orders - Flexible Analysis app. | The Screen is navigated to the Solution Orders app showing Default filters as Display Currency , Posting Date, Solution Order, Sales office , Sales Group , Sold to Party , Sales Organization, Distribution Channel Division and Solution Order Item Status |  |
| 4 | Click Navigation Panel | Choose navigation panel. | Different options such as Dimensions, Rows, Columns and Available Fields are displayed. |  |
| 5 | Add Filters | Chooses filtersDisplay Currency – EURPosting Date:Solution order:Latest dateSolution Ordrer Item Status: ReleasedSold to Party -10100001Sales Organization :1010Distribution Channel : 10Division:00Choose Go. | The results for Data Analysis and Graphical Display are displayed. |  |

#### Solution Orders - Flexible Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Purpose is to view the details of Solution Orders - Flexible Analysis in Data Analysis and in Graphical display..

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Sales Manager. | The Home screen is displayed. |  |
| 2 | Open app | Search Solution Orders - Flexible Analysis app . | The Solution Orders - Flexible Analysis app is displayed. |  |
| 3 | Review app | Choose the Solution Orders- Flexible Analysis app. | The Screen is navigated to the Solution Orders app showing Default filters as Display Currency , Posting Date, Solution Order, Sales office , Sales Group , Sold to Party , Sales Organization, Distribution Channel Division and Solution Order Status |  |
| 4 | Click Navigation Panel | Choose navigation panel. | Different options such as Dimensions, Rows, Columns and Available Fields are displayed. |  |
| 5 | Add Filters | Chooses filtersDisplay Currency – EURPosting Date:Solution Order:Latest dateSolution Order Life Cycle Status: ReleasedSold to Party -10100001Sales Organization :1010Distribution Channel : 10Division:00Choose Go. | The results for Data Analysis and Graphical Display are displayed. |  |

#### Insights Cards for Solution Orders (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Purpose is to view the details of Analytical Cards for Solution Orders which helps to view Solution orders by Product, Sold To Party and Net value.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad using the role Solution Order Specialist. | The Home screen is displayed. |  |
| 2 | Open app | Choose Solution Orders by Product app under Insights.Displays the top five solution orders by product. The result displayed is sorted in descending order by solution order net value. | The Manage Solution Orders app is displayed whereadditional details related to Solution Orders can be obtained. |  |
| 3 | Open app | Choose Solution Orders By Sold-To Party app under Insights.Displays the top five solution orders by sold-to party. The result displayed is sorted in descending order by solution order net value. | The Manage Solution Orders app is displayed whereadditional details related to Solution Orders can be obtained. |  |
| 4 | Open app | Choose Solution Order List app under Insights.Displays the top ten solution orders by net value. The result displayed is sorted in descending order by net value. | The Manage Solution Orders app is displayed where additional details related to Solution Orders can be obtained. |  |

### Service Orders

#### Service Order Issues

##### Analyze Service Order Issues - Graphical Overview

Purpose

Using the graphical representation of the service order issues, You can view the list of incomplete service orders. Incomplete service orders are orders for which no service confirmations exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. | The Home screen is displayed. |  |
| 2 | View App | Service Order Issues app is displayed under Service Monitoring and Analytics. | Service Order Issues app displays the total number of issues in Service Orders. |  |
| 3 | Access 'Service Orders Issues' | Access Service Orders Issues app to View the different issue types represented in graphical format. | The graph displays the number of issues for each of the issue type in service orders. |  |
| 4 | Select Issue type in Service Order | Select an issue type to further filter on different criteria. | List of other filter criteria is displayed for the user when one of the issue types is selected. |  |
| 5 | Select Additional Filter Criteria | Select one of the filter criteria available to further filter out the issues. | Additional filter criteria is applied, and the list is updated accordingly. |  |

##### Analyze Service Order Issues by Country and Region

Purpose

Analyze the service orders and sort them by applying the filter on country and region. This helps in filtering out the issues specific to each of the country or region.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. | The Home screen is displayed. |  |
| 2. | View App | Service Order Issues app is displayed under Service Monitoring and Analytics | Service Order Issues app displays the total number of issues in service orders. |  |
| 3. | Access 'Service Orders Issues' | Access Service Orders Issues app to View the different issue types represented in graphical format. | The Graph displays the number of issues for each of the issue type in service orders. |  |
| 4. | Select Filter on Country and region | Select Country and Region option from the drop down menu to apply this filter. | The graph now displays the issues for each of country / region. |  |
| 5. | Select Issue for a Country / Region | Select an issue from the graph for a country or region to view details and option to further filter the results. | Details are displayed along with the available filter options. |  |
| 6. | Select Additional Filter Criteria | Select one of the filter criteria available to further filter out the issues. | Additional filter criteria is applied, and the list is updated accordingly. |  |

##### Analyze Service Order Issues by Service Transactions

Purpose

Analyze the service order issues by filtering on all the service orders for which the issues are listed.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. | The Home screen is displayed. |  |
| 2 | View App | Service Order Issues app is displayed under Service Monitoring and Analytics. | Service Order Issues app displays the total number of issues in Service Orders. |  |
| 3 | Access 'Service Orders Issues' | Access Service Orders Issues app to View the different issue types represented in graphical format. | The Graph displays the number of issues for each of the issue type in service orders. |  |
| 4 | Select Filter on Service Orders | Select Service Orders option from the drop down menu to apply this filter. | Issues are displayed as a list based out of all the service orders. |  |
| 5 | Select a Service Order | Select an issue from the List of Service Orders to view details and option to further filter the results. | Details are displayed along with the available filter options. |  |
| 6 | Select Additional Filter Criteria | Select one of the filter criteria available to further filter out the issues. | Additional Filter criteria is applied, and the list is updated accordingly. |  |

##### Analyze Service Order Issues by Sales Organization

Purpose

Analyze the service order issues by filtering on sales organization and hence list the issues specific to each of the sales org issues are reported.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. | The Home screen is displayed. |  |
| 2 | View App | Service Order Issues app is displayed under Service Monitoring and Analytics. | Service Order Issues app displays the total number of issues in Service Orders. |  |
| 3 | Access 'Service Orders Issues' | Access Service Orders Issues app to view the different issue types represented in graphical format. | The Graph displays the number of issues for each of the issue type in service orders. |  |
| 4 | Select Filter on Sales Organization | Select Sales Organization option from the drop down menu to apply this filter. | Number of Issues for each of the Sales Organization is displayed in graphical format. |  |
| 5 | Select a Sales Organization | Select a sales organization from the fraph to View details with an option to further filter the results. | Details are displayed along with the available filter options. |  |
| 6 | Select Additional Filter Criteria | Select one of the filter criteria available to further filter out the issues. | Additional filter criteria is applied, and the list is updated accordingly. |  |

##### Analyze Service Order Issues - Mini Tiles

Purpose

Use the mini tiles feature to get an overview of service order Issues in different dimensions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Customer Service Manager. | The Home screen is displayed. |  |
| 2 | View App | Service Order Issues app is displayed under Service Monitoring and Analytics. | Service Order Issues app displays the total number of issues in service orders. |  |
| 3 | Access Service Orders Issues | Access Service Orders Issues app to view the different issue types represented in graphical format. | The graph displays the number of issues for each of the issue type in service orders. |  |
| 4 | Select Show Mini Tiles Option | Select Show Mini Tiles option displayed at the top right corner of the screen. | The following mini tiles are displayed for Service Order issues:Confirmation issuesErrorsBilling BlockNot Fully BilledSLA IssueRejectedNo Confirmations |  |
| 5 | Select Confirmation Issues Mini Tile | Select Confirmation Issues Mini Tile from the Mini Tiles view. | Confirmation issues types are displayed with the corresponding numbers as a graph. |  |
| 6 | Select Errors Mini Tile | Select Errors Mini Tile from the Mini Tiles view. | Service order errors are displayed as a graph. |  |
| 7 | Select Billing Block Mini Tile | Select Billing Block Mini Tile from the Mini Tiles view. | Issues related to blocked billing are displayed as a graph. |  |
| 8 | Select Not Fully Billed Mini Tile | Select Not Fully Billed Mini Tile from the Mini Tiles view. | Service Orders which are not fully billed are displayed in the graph. |  |
| 9 | Select SLA Issue Mini Tile | Select SLA Issue Mini Tile from the Mini Tiles view. | Service Orders with SLA issues are displayed in the graph. |  |
| 10 | Select Rejected Mini Tile | Select Rejected Mini Tile from the Mini Tiles view. | Service Orders which are rejected are displayed in the graph. |  |
| 11 | Select No Confirmations Mini Tile | Select Mini Tile from the Mini Tiles view. | Service Orders which do not have confirmations are displayed in the graph. |  |

#### Service Orders – Flexible Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The Purpose is to view the details of Service orders in Data Analysis and in Graphical display.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad using the role Customer Service Manager. | The Home screen is displayed. |  |
| 2 | Open app | Search Service Orders - Flexible Analysis app. | The service orders Flexible Analysis app is displayed |  |
| 3 | Review app | Choose the Service Orders - Flexible Analysis app. | The Screen is navigated to the Service Orders -Flexible Analysis app showing Default filters as Display Currency , Sold to Party , Sales Organization. |  |
| 4 | Click Navigation Panel | Choose navigation Panel. | Different options such as Dimensions, Rows, Columns and Available Fields are displayed. |  |
| 5 | Add Filters | Choose filtersCurrency: EURSold to Party: 17100001Sales Organization: 1710Click Go | The results for Data Analysis and Graphical Display are displayed. |  |
| 6 | Navigate to | Click on Navigate to option. | You should be able to view and navigate below appsCreate Service OrderDisplay Service OrderManage Service OrderOverdue Service Order AnalysisService ActualsService Management OverviewService Orders Analysis |  |

### Order to Cash Manager Dashboard – Incoming Sales & Services

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

SAP Analytics Cloud (SAC) provides a comprehensive tool for strategic live-data analysis in sales. The Purpose is to help the Sales Manager to compare the Incoming Order Value coming from Sales and Services and to identify top customers and trends by incoming sales and services.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad using the role Sales Manager. | The Home screen is displayed. |  |
| 2 | Open app | Choose Order to Cash Dashboard under Sales Analytics. | The Screen is Navigated to Order to Cash Dashboard page which displays Sales Volume, Profit Margin and Incoming orders. |  |
| 3 | Incoming orders | Select the Incoming orders tab. | The screen showing the following:Figures for Incoming service orders, Open Service orders and No. of Incoming Service orders.Incoming and Open Service Orders trend.Top customers - Incoming Service orders by Sold-To Party.No. of Open Service orders and No. of Incoming Service Orders by Sales Organization. |  |

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
- see-also :: [[14-maintenance-service-and-projects/test-script-service-quotation-4ga-ae-sap-s-4hana-cloud-public-edition]]
- see-also :: [[06-management-accounting/predictive-accounting-for-travel-and-expense-management-4q0-ae-1042]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/43B_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 65,768 chars in the whole document
