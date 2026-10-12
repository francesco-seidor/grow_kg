---
id: 06-management-accounting/test-script-sap-s-4hana-cloud-public-edition-integrated-financial-plan
title: Test Script SAP S/4HANA Cloud Public Edition - Integrated Financial Planning (4RC) (4RC_S4CLD2608_BPD_EN_XX)
description: "Test script for scope item 4RC Integrated Financial Planning in SAP Analytics Cloud: OPEX, product cost, profitability, CAPEX, financial statement, GHG, add-ons, S/4HANA integration."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/financial-plan-data-and-integrated-planning, topic/group-financial-planning]
aliases: [4RC_S4CLD2608_BPD_EN_XX]
keywords: [Financial Plan Data Upload and Integrated Financial Planning, integrated financial planning, operating expense planning, product cost planning, sales and profitability planning, capital expense planning, financial statement planning, simulation cockpit, greenhouse gas emission planning, ifp add-on package]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4RC_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1048
topic: 06-management-accounting/financial-plan-data-and-integrated-planning
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script SAP S/4HANA Cloud Public Edition - Integrated Financial Planning (4RC) (4RC_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4RC_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Financial Plan Data Upload and Integrated Financial Planning** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Integrated Financial Planning (4RC) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 4](#_Toc232833397)

[2 Prerequisites 5](#_Toc232833398)

[2.1 Business Content Activation and Integration Setup 5](#_Toc232833399)

[2.2 System Access 5](#_Toc232833400)

[2.3 Roles 5](#_Toc232833401)

[2.4 Master Data, Organizational Data, and Other Data 5](#_Toc232833402)

[2.5 Additional Manual Configuration 6](#_Toc232833403)

[3 Overview Table 7](#_Toc232833404)

[4 Test Procedures 9](#_Toc232833405)

[4.1 Landing Page 9](#_Toc232833406)

[4.2 Operating Expense Planning 12](#_Toc232833407)

[4.2.1 Perform Planning Admin Tasks 12](#_Toc232833408)

[4.2.2 Perform Cost Center Expense Planning 13](#_Toc232833409)

[4.2.3 Perform Cost Center Activity Cost Rate Planning 14](#_Toc232833410)

[4.2.4 Perform Cost Center Activity Cost Rate Calculation 16](#_Toc232833411)

[4.2.5 Perform Project Expense Planning 17](#_Toc232833412)

[4.2.6 Review Cost Center Reports 18](#_Toc232833413)

[4.2.7 Review Project Reports 19](#_Toc232833414)

[4.2.8 Review Cost Center Analytics 20](#_Toc232833415)

[4.2.9 Review Project Analytics 21](#_Toc232833416)

[4.3 Product Cost Planning 22](#_Toc232833417)

[4.3.1 Perform Planning Admin Tasks 22](#_Toc232833418)

[4.3.2 Perform Product Cost Rate Calculation 23](#_Toc232833419)

[4.3.3 Perform Product Cost Resource Planning 24](#_Toc232833420)

[4.3.4 Review Product Cost Reports 25](#_Toc232833421)

[4.3.5 Review Product Cost Analytics 25](#_Toc232833422)

[4.4 Sales and Profitability Planning 26](#_Toc232833423)

[4.4.1 Perform Planning Admin Tasks 26](#_Toc232833424)

[4.4.2 Perform Sales and Profitability Planning 27](#_Toc232833425)

[4.4.3 Allocate Sales and Admin Costs 28](#_Toc232833426)

[4.4.4 Review Sales and Profitability Reports 29](#_Toc232833427)

[4.4.5 Review Sales and Profitability Analytics 30](#_Toc232833428)

[4.5 Capital Expense Planning 31](#_Toc232833429)

[4.5.1 Perform Planning Admin Tasks 31](#_Toc232833430)

[4.5.2 Perform Capital Expense Planning 32](#_Toc232833431)

[4.5.3 Perform Capital Asset Request Planning 33](#_Toc232833432)

[4.5.4 Perform Capital Expense Reporting 35](#_Toc232833433)

[4.5.5 Perform Portfolio Planning Integration Reporting 36](#_Toc232833434)

[4.6 Financial Statement Planning 36](#_Toc232833435)

[4.6.1 Perform Planning Admin Tasks 36](#_Toc232833436)

[4.6.2 Perform Financial Statement Target Planning 37](#_Toc232833437)

[4.6.3 Perform Financial Statement Planning 39](#_Toc232833438)

[4.6.4 Review Financial Statement Target Reports 41](#_Toc232833439)

[4.6.5 Review Financial Statement Reports 42](#_Toc232833440)

[4.6.6 Review Financial Statement Target Analytics 43](#_Toc232833441)

[4.6.7 Review Financial Statement Analytics 43](#_Toc232833442)

[4.7 Product Unit Conversion 45](#_Toc232833443)

[4.7.1 Perform Admin Tasks 45](#_Toc232833444)

[4.8 Cross Automated Planning 45](#_Toc232833445)

[4.9 Cross-Simulation Cockpit 47](#_Toc232833446)

[4.9.1 Prerequisites 47](#_Toc232833447)

[4.9.2 Perform Cross-Model Simulation 49](#_Toc232833448)

[4.10 Cross-Model Parameter Setting 52](#_Toc232833449)

[4.10.1 Plan Sales Quantities 52](#_Toc232833450)

[4.10.2 Plan Operating Expenses 53](#_Toc232833451)

[4.10.3 Plan Profit and Loss 54](#_Toc232833452)

[4.11 Cross Greenhouse Gas Emission Planning 54](#_Toc232833453)

[4.11.1 Prerequisites 54](#_Toc232833454)

[4.11.2 Perform Cross Model Greenhouse Gas Emission Factor Planning and Valuation 58](#_Toc232833455)

[4.11.3 Perform Cross Model Greenhouse Gas Emission Allocation to Cost Center and Product 59](#_Toc232833456)

[4.11.4 Perform Cross Model Greenhouse Gas Emission Variance Analysis 61](#_Toc232833457)

[4.12 Cross End-to-End Planning Process 62](#_Toc232833458)

[4.13 Add-On Package for IFP 63](#_Toc232833459)

[4.13.1 Landing Page 63](#_Toc232833460)

[4.13.2 Perform Employee Expenses Transfer 64](#_Toc232833461)

[4.13.3 Perform IBP Consensus Demand Transfer 65](#_Toc232833462)

[4.13.4 Perform CP Sales Planning Integration 66](#_Toc232833463)

[4.13.5 Perform Commercial Planning Integration 67](#_Toc232833464)

[4.13.6 Perform Sustainability Footprint Management Integration 69](#_Toc232833465)

[4.13.7 Perform Portfolio Financial Planning Integration 70](#_Toc232833466)

[4.14 Integration with SAP S/4HANA 71](#_Toc232833467)

[4.14.1 Operating Expense Planning and Budgeting 71](#_Toc232833468)

[4.14.1.1 Load Master and Actual Data from SAP S/4HANA 71](#_Toc232833469)

[4.14.1.2 Export Plan Data to SAP S/4HANA 72](#_Toc232833470)

[4.14.2 Product Cost Planning 73](#_Toc232833471)

[4.14.2.1 Load Master and Actual Data from SAP S/4HANA 73](#_Toc232833472)

[4.14.3 Sales and Profitability Planning 75](#_Toc232833473)

[4.14.3.1 Load Master and Actual Data from SAP S/4HANA 75](#_Toc232833474)

[4.14.3.2 Export Plan Data to SAP S/4HANA 76](#_Toc232833475)

[4.14.4 Capital Expense Planning 77](#_Toc232833476)

[4.14.4.1 Load Master Data from SAP S/4HANA 77](#_Toc232833477)

[4.14.5 Financial Statement Planning 78](#_Toc232833478)

[4.14.5.1 Load Master and Actual Data from SAP S/4HANA 78](#_Toc232833479)

[4.14.5.2 Export Plan Data to SAP S/4HANA 79](#_Toc232833480)

[4.14.6 Add-On Package for IFP 80](#_Toc232833481)

[4.14.6.1 Load Demand Data from SAP IBP 80](#_Toc232833482)

[4.14.6.2 Load Master and Actual Data from SAP S/4HANA Cloud Public Edition 81](#_Toc232833483)

## Purpose

Overview

This process supports detailed financial planning to set operational targets and to provide a baseline for the valuation of operational processes. It includes:

- Cost and activity planning to determine cost flows and activity rates
- Sales and profitability planning to determine volume and price targets, expected discounts, and cost of goods sold
- Product cost simulation to determine raw material prices and activity usage
- Project planning to provide a baseline for revenue recognition and for capital expense projects
- Financial statement planning, including profit and loss, balance sheet, and cash flow

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all the prerequisites for conducting the test in terms of systems, users, master data, organizational data, other test data and business conditions.

### Business Content Activation and Integration Setup

You must perform the following Getting Started activities for SAP Analytics Cloud:

- For SAP S/4HANA Cloud Public Edition: [Getting Started with SAP Analytics Cloud](https://help.sap.com/viewer/1cbcff7ccd35405ab445b223c1ab1588/latest/en-US/74b2bfa963214757b0746993603762be.html)
- For SAP S/4HANA Cloud Private Edition: [Getting Started with SAP Analytics Cloud](https://help.sap.com/viewer/48f4b4785b8e45938ac44a67be8032d9/latest/en-US/74b2bfa963214757b0746993603762be.html)

|  |
| --- |
| Note For purposes of completing the test procedures, it isn't necessary to perform the activities Getting Started Activities - Importing Your Master and Transaction Data to SAP Analytics Cloud and Adapting SAP Analytics Cloud Planning Content to Customer-Specific G/L Account Master Data in the linked content. |

### System Access

|  |  |
| --- | --- |
|  | Details |
| System | Accessible via SAP Analytics Cloud. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Planning Modeler | Modeler | Modeling and Viewing Privileges | N/A | N/A |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and suppliers, for example, depending on the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | xx10 (with xx being the two-digit prefix for your country/region (10 for DE, 17 for U.S., and so on)) |  |  |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/2f26796826a1d63499ac1a577de6901c)

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note All steps in this test script are performed in SAP Analytics Cloud. |

| Process Step | Business Role | Transaction/App/Story | Expected Results |
| --- | --- | --- | --- |
| [Landing Page](#unique_9) [page ] 9 | Planning Modeler | SAP Analytics Cloud | The landing page offers the user the possibility to directly access any of the IFP planning stories and thus ease navigation within the planning. |
| [Operating Expense Planning](#unique_10) [page ] 12 | Planning Modeler | SAP Analytics Cloud | Operating expense planning, allocations, activity quantity planning, activity cost rate planning, and activity cost rate calculations for cost centers and planning of costs associated with a project and allocation to cost centers |
| [Product Cost Planning](#unique_11) [page ] 22 | Planning Modeler | SAP Analytics Cloud | Calculation and simulation of product costs based on raw material prices and activity cost rates. |
| [Sales and Profitability Planning](#unique_12) [page ] 26 | Planning Modeler | SAP Analytics Cloud | Sales and quantity planning and simulation, revenue, deductions, and cost of goods sold calculations. |
| [Capital Expense Planning](#unique_13) [page ] 31 | Planning Modeler | SAP Analytics Cloud | Profit center expenses for acquiring, maintaining, or improving fixed assets such as buildings, vehicles, equipment, or land. |
| [Financial Statement Planning](#unique_14) [page ] 36 | Planning Modeler | SAP Analytics Cloud | Profit and loss planning with trading partner allocation and balance sheet planning. |
| [Product Unit Conversion](#unique_15) | Planning Modeler | SAP Analytics Cloud | You viewed product-dependent and product-independent conversion factors |
| [Cross Simulation Cockpit](#unique_16) | Planning Modeler | SAP Analytics Cloud | Perform what-if simulations for sample processes based on changes to drivers, such as sales quantity or personnel expenses. |
| [Cross-Model Parameter Setting](#unique_17) | Planning Modeler | SAP Analytics Cloud | You planned control parameters for sales quantities, operating expenses, and profit and loss. |
| [Cross Greenhouse Gas Emission Planning](#unique_18) | Planning Modeler | SAP Analytics Cloud | You performed planning for cross model greenhouse gas emissions. |
| [Cross End-to-End Planning Process](#unique_19) [page ] 62 | Planning Modeler | SAP Analytics Cloud | You prepared the end-to-end sample process. |
| [Add-On Package for IFP](#unique_20) | Planning Modeler | SAP Analytics Cloud | Load transaction data from optional sources. |
| [Integration with SAP S/4HANA](#unique_21) [page ] 71 | Planning Modeler | SAP Analytics Cloud | Load master and transaction data from SAP S/4HANA. |

## Test Procedures

### Landing Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you navigate the landing page.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | Open the Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_LandingPage | The Story SAP_FI_IFP_IM_LandingPage is displayed. |  |
| 3 | Operating Expense Planning | Choose Operating Expense Planning. |  |  |
| 4 | Operating Expense Planning | The Operating Expense tab shows information for the Cost Center planning. |  |  |
| 5 | Navigate | Use the links in the lower section to open any of the Operating Expense stories and show the named tab. | The named story and tab are opened in a new browser tab. |  |
| 6 | Product Cost Planning | Choose Product Cost Planning. |  |  |
| 7 | Product Cost Planning | The Product Cost tab shows information for the Product Cost planning. |  |  |
| 8 | Navigate | Use the links in the lower section to open any of the Product Cost stories and show the named tab. | The named story and tab are opened in a new browser tab. |  |
| 9 | Sales and Profitability Planning | Choose Sales and Profitability Planning. |  |  |
| 10 | Sales and Profitability Planning | The Sales & Profitability tab shows information for the Profitability planning. |  |  |
| 11 | Navigate | Use the links in the lower section to open any of the Profitability stories and show the named tab. | The named story and tab are opened in a new browser tab. |  |
| 12 | Capital Expense Planning | Choose Capital Expense Planning. |  |  |
| 13 | Capital Expense Planning | The Capital Expense tab shows information for the Capital Expense planning. |  |  |
| 14 | Navigate | Use the links in the lower section to open any of the Capital Expense stories and show the named tab. | The named story and tab are opened in a new browser tab. |  |
| 15 | Financial Statement Planning | Choose Financial Statement Planning. |  |  |
| 16 | Financial Statement Planning | The Financial Statement tab shows information for Financial Statement planning. |  |  |
| 17 | Navigate | Use the links in the lower section to open any of the Financial Statement stories and show the named tab. | The named story and tab are opened in a new browser tab. |  |
| 18 | Greenhouse Gas Emission Planning | Choose Greenhouse Gas Emission Planning. | The tab shows information for greenhouse gas planning. |  |
| 19 | Navigate | Use the links in the lower section to open any of the Greenhouse Gas Emission Planning stories. | The named story and tab are opened in a new browser tab. |  |
| 20 | Financial Planning Administration | Choose Financial Planning Administration. |  |  |
| 21 | Financial Planning Administration | The Admin tab shows information for Administration. |  |  |
| 22 | Navigate | Use the links in the lower section to open any of the Admin stories and show the named tab. | The named story and tab are opened in a new browser tab. |  |
| 23 | Planning Process Support | Choose Planning Process Support. | The tab shows information on preparing for the planning process. |  |
| 24 | Navigate | Use the multi action starters to import IFP related master and transaction data and copy previous years actuals and plan parameters into current year plan version.Use links to access the admin stories | The multi action starters successfully run.The named story and tab are opened in a new browser tab. |  |
| 25 | System Access and Monitoring | Choose System Access & Monitoring. | The tab contains links to models, files, and system tables in the planning system. |  |
| 26 | Navigate | Use the links in the lower section to open any of the folders and see the related files. | The named story and tab are opened in a new browser tab. |  |
| 27 | Simulation Cockpit | Choose Simulation Cockpit. | The Simulation Cockpit is opened in a new browser tab.The Simulation Cockpit story contains step by step processes for Sales Simulation, Expense Simulation, and Raw Material Price Simulation. |  |
| 28 | End-to-End Planning | Choose End-to-End Planning Process. | The End-to-End Planning Process is opened in a new browser tab.The End-to-End Planning Process story contains step by step planning processes across the IFP models. |  |
| 29 | Financial Data Flow | Choose Financial Data Flow. |  |  |
| 30 | Financial Data Flow | The Financial Data Flow tab displays the data flow diagram. |  |  |
| 31 | Greenhouse Gas Data Flow | Choose Greenhouse Gas Data Flow. | The tab displays the data flow. |  |
| 32 | Navigate | Use the link in the upper right corner to go back to the General tab. | The General tab is displayed. |  |

### Operating Expense Planning

#### Perform Planning Admin Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Step 3 Create sample data of this procedure is only necessary for the stand-alone test with sample data, not for the SAP S/4HANA integration test.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access Story | Find and display the story SAP_FI_IFP_IM_OPEX_PlanAdmin. | The Story SAP_FI_IFP_IM_OPEX_PlanAdmin is displayed. |  |
| 3 | Create Plan Sample Data | On the Create 'Plan' Sample Data tab, use data actions Create Sample Data for Actuals and Create Sample Data for Plan.If necessary, first delete the existing data with the other data actions. | Plan sample data are displayed. |  |
| 4 | Maintain Drivers for Planning | Maintain values on the following tabs:CCtr Distribution WeightsCCtr Allocation WeightsProject Allocation WeightsCCtr Splitting WeightsCCtr Fix/Var WeightsCCtr Activity Allocation WeightsCCtr Activity Relation |  |  |
| 5 | Optional: Execute Planning Functions | Choose the 'Plan' Planning Functions tab.Execute the data actions. | Resulting Plan data is displayed. |  |
| 6 | Save Plan Data | You can either choose Publish Data or leave the story and choose Publish All. |  |  |
| 7 | Optional: Plan Parameter Setting | On the 'Plan' Parameter Setting tab, select a base level account and enter a simulation variant and parameter for first open period of the plan. | Control parameters and parameter values entered. |  |
| 8 | Optional: Execute Plan Parameter Setting | On the 'Plan' Parameter Setting tab, use data action Apply Control Parameters to Cost Center Expenses. | You checked the Plan data values and calculations. |  |
| 9 | Create 'Budget' Sample Data | On the Create 'Budget' Sample Data tab, use data action Create Sample Data for CCtr Budget and Create Sample Data for Project Budget.If necessary, first delete the existing data with the other data action. | CCtr Budget and Project Budget sample data are displayed |  |
| 10 | Optional: Execute Planning Functions | Choose the 'Budget' Planning Functions tab.Execute the data actions. | Resulting budget data are displayed. |  |
| 11 | Save Budget Data | You can either choose Publish Data or leave the story and choose Publish All. |  |  |

#### Perform Cost Center Expense Planning

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
| 1 | Access the Story Page | From the main menu, choose Files . | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_OPEX_CCtrExpenses | The Story SAP_FI_IFP_IM_OPEX_CCtrExpenses is displayed. |  |
| 3 | Copy Actual Expenses | On the Expenses tab, use data action Copy Cost Center Expenses from Actuals. | Plan data is displayed. |  |
| 4 | Populate Expenses Using Control Parameters | On the Expenses tab, use data action Apply Control Parameters to Cost Center Expenses. | Plan data is displayed. |  |
| 5 | Maintain Expenses | Change the expense values. |  |  |
| 6 | Run Allocation with Account Split | On the Allocations tab, use data action Allocate CCtr Expenses with Account Split. | Plan data values are distributed between cost centers according to the cost center allocation weights maintained in the Admin story. Additionally plan data values are split between accounts which are mapped to the original expense G/L account by the Allocation Account column in dimension SAP_FI_IFP_GLACCOUNT. |  |
| 7 | Run Allocation | On the Allocations tab, use the Allocate CCtr Expenses data action. | Results from the prior step are undone. Plan data are distributed between cost centers according to the cost center allocation weights maintained in the Admin story. Plan data values are posted to the Secondary costs account. |  |
| 8 | Run Allocation with Account Split | On the Allocations tab, use data action Allocate CCtr Expenses. | Result from previous step is undone and result from step 6 restored. |  |

#### Perform Cost Center Activity Cost Rate Planning

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_OPEX_ActivityCostRatePlanning. | The Story SAP_FI_IFP_IM_OPEX_ActivityCostRatePlanning is displayed. |  |
| 3 | Copy Actuals | On the Cost Rates tab, use data action Derive Activity Cost Rates from Actuals. | Activity cost rates are displayed. |  |
| 4 | Maintain Cost Rates | Change the cost rate values. |  |  |
| 5 | Copy Actual Activity Quantities | Choose the Total Activity Output tab. Use the Copy CCtr Activity Quantities from Actuals data action. | Activity quantities are displayed. |  |
| 6 | Maintain Capacities and Activity Quantities | Change the capacities and activity quantities. | Check the result on the Activity Output to Partner tab. |  |
| 7 | Run Cost Calculation | On the Total Activity Output tab, use data action Calculate Cost Center Costs. | Check calculated amounts . |  |
| 8 | Maintain Activity Quantities | Choose the Activity Output to Partner tab.Maintain the activity quantities | Check the result on Total Activity Output tab. |  |
| 9 | Indirect Activity Allocation | On the Activity Output to Partner tab, use the Allocate CCtr Activity Quantities data action. | Total activity output of a sender cost center is allocated to the receiving cost centers according to the cost center activity allocation weights maintained in the Admin story. |  |
| 10 | Inverse Calculation of Activity Quantities | On the Activity Output Detail tab, use data action Calc. CCtr Activity Quantities Inversely. | Activity output of a sender cost center is calculated from the total activity output of the receiving cost centers according to the activity relation factors maintained in the Admin story |  |
| 11 | Run Cost Calculation | On the Activity Output to Partner tab, use data action Calculate Cost Center Costs. | Check calculated amounts. |  |
| 12 | Reporting | Choose the Reporting tab. Check the plan data. | You checked the plan data. |  |
| 13 | Exploration | From the table, navigate to Explore. | Check the two exploration view. |  |

#### Perform Cost Center Activity Cost Rate Calculation

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_OPEX_ActivityCostRateCalculation | The Story SAP_FI_IFP_IM_OPEX_ActivityCostRateCalculation is displayed. |  |
| 3 | Copy Actual Expenses | Choose the Expenses tab.Either use the expenses from the expense planning or use data action Copy Cost Center Expenses from Actuals. | Plan data is displayed. |  |
| 4 | Check Expenses | Check the expense values.Note Expenses are maintained in the story SAP_FI_IFP_IM_OPEX_CCtrExpenses |  |  |
| 5 | Split Expenses to Activity Types | On the Expenses ActDep tab, use the Split CCtr Expenses by Activity Type data action. | Cost Center Expenses are allocated to activity types according to the splitting weights maintained in the Admin story. |  |
| 6 | Activity Quantities | On the Total Activity Output use data action Copy CCtr Activity Quantities from Actuals or Copy CCtr Activity Quantities from Product Cost Plan. | Activity quantities are displayed. |  |
| 7 | Maintain Activity Quantities | Change activity quantity values |  |  |
| 8 | Run Price Calculation with Account Split | On the Cost Rates tab, use data action Calc. CCtr Activity Cost Rates with Account Split. | The results from the prior step are undone. Activity cost rates are displayed. |  |
| 9 | Run Price Calculation | On the Cost Rates tab, use data action Calc. CCtr Activity Cost Rates. | Activity prices are displayed. |  |
| 10 | Run Price Calculation with Account Split | On the Cost Rates tab, use data action Calc. CCtr Activity Cost Rates with Account Split. | The previous step's result is undone. The result from step 8 is restored. |  |
| 11 | Split Fix/Variable | On the Expenses ActDep Fix/Var tab, use the Split CCtr Expenses by Fix/Variable Code data action. | Activity quantities are displayed split by fix and variable according to the fix/var weights maintained in the Admin story. |  |
| 12 | Run Price Calculation with Account Split | On the Cost Rates Fix/Var tab, use data action Calc. CCtr Activity Cost Rates with Account Split. | Activity cost rates are displayed. |  |
| 13 | Calculate Variable Costs | On the Total Activity Output tab, change the activity quantity for Manufacturing 1/Manufacturing2.On the Expenses ActDep Fix/Var tab, run data action Calculate Variable Costs by Variable Expense Relation. | Variable costs change according to the changed activity quantities and the variable expense relation factor. |  |
| 14 | Run Price Calculation with Account Split | On the Cost Rates Fix/Var tab, use data action Calc. CCtr Activity Cost Rates with Account Split. | Fixed portion of the activity cost rates are changed |  |
| 15 | Reporting | Choose the Reporting tab. Check the plan data. | You checked the plan data. |  |

#### Perform Project Expense Planning

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_OPEX_ProjExpenses | The Story SAP_FI_IFP_IM_OPEX_ProjExpenses is displayed. |  |
| 3 | View Actual Expenses | On the Actuals tab, view actual project expenses | Actual data are displayed |  |
| 4 | Copy Actual Expenses | On the Expenses tab, use data action Copy Project Expenses from Actuals | Plan data are displayed |  |
| 5 | Maintain Project Expenses | Change project expense values. |  |  |
| 6 | Plan Project Activity Input | On the Activity Input tab, use data action Copy Proj. Activity Quantities from Actuals. | Plan data are displayed |  |
| 7 | Maintain Activity Quantities | Change activity quantity values. |  |  |
| 8 | Calculate Project Costs | On the Activity Input tab, use data action Calculate Project Costs.(As a prerequisite, SAP_FI_IFP_IM_OPEX_ActivityCostRatePlanning ([Perform Cost Center Activity Cost Rate Planning](#unique_25) [page ] 14, step 3) needs to be performed). | Costs are displayed. |  |
| 9 | Run Allocation | On the Allocation tab, use data action Allocate Project Expenses | Plan data are distributed between cost centers according to the project allocation weights maintained in the Admin story |  |

#### Review Cost Center Reports

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
| 1 | Access the Story Page | In the Main Menu, choose Files . | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_OPEX_CCtrReports | The story SAP_FI_IFP_IM_OPEX_CCtrReports is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year, Company Code, and Cost Center as necessary. | Displayed data are filtered. |  |
| 4 | Review Plan Data | On each tab, review the plan data. | Plan data are displayed. |  |

#### Review Project Reports

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the project reports.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | In the Main Menu, choose Files. |  |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_OPEX_ProjReports. | The SAP_FI_IFP_IM_OPEX_ProjReports story is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year, Company Code, and WBS Element as needed. | The displayed data is filtered. |  |
| 4 | Review Plan Data | Review the plan data. | The plan data is displayed. |  |

#### Review Cost Center Analytics

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
| 1 | Access the Story Page | In the Main Menu, choose Files . | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_OPEX_CCtrAnalytics | The story SAP_FI_IFP_IM_OPEX_CCtrAnalytics is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year, Company Code and Cost Center as necessary. | Displayed data are filtered. |  |
| 4 | Select Cost Center Overview tab | Review the plan data. | Plan data are displayed. |  |
| 5 | Select Cost Center Details tab | Review the plan data. Adjust the Select G/L Account and Select Controlling Debit Credit Code input controls. | Plan data are displayed. |  |

#### Review Project Analytics

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
| 1 | Access the Story Page | In the Main Menu, choose Files . | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_OPEX_ProjAnalytics | The story SAP_FI_IFP_IM_OPEX_ProjAnalytics is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year, Company Code and WBS Element (Project) as necessary. | Displayed data are filtered. |  |
| 4 | Project Overview | Choose the Project Overview tab. |  |  |
| 5 | Project Overview | Review the plan data. | Plan data are displayed. |  |
| 6 | Project Details | Choose the Project Details tab. |  |  |
| 7 | Project Details | Review the plan data. Adjust the Select G/L Account and Select Controlling Debit Credit Code input controls. | Plan data are displayed. |  |

### Product Cost Planning

#### Perform Planning Admin Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Step 3 Create sample data of this procedure only is necessary for the stand-alone test with sample data, not for the SAP S/4HANA integration test.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_ProductCost_PlanAdmin. | The Story SAP_FI_IFP_IM_ProductCost_PlanAdmin is displayed. |  |
| 3 | Create Sample Data | Choose the Create Sample Data tab.Use data actions Create Sample Data for Cost Estimate.If necessary, first delete the existing data with the other data actions. | Sample data are displayed |  |
| 4 | Optional: Execute Planning Functions | Choose the Planning Functions tab.Execute the data actions. | Resulting Plan data is displayed. |  |
| 5 | Save Plan Data | Either choose Publish Data or leave the story and choose Publish All. |  |  |

#### Perform Product Cost Rate Calculation

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_ProductCost_RateCalculation. | The Story SAP_FI_IFP_IM_ProductCost_RateCalculation is displayed. |  |
| 3 | Check Initial Data | If you executed the planning functions already within the Admin story, check the data on the Lot Size, Quantity Structure, Raw Material Prices, Activity Cost Rates , and Manufacturing Overhead tabs. | Check the data on the first five tabs. |  |
| 4 | Prepare Initial Data | If you didn’t execute the planning function already within the Admin story, execute the data actions on the first five tabs.On the Activity Cost Rates tab, you must decide if you want to copy the activity cost rates from the actuals (Derive Activity Cost Rates from Cost Estimate) or from the cost center plan (Copy Activity Cost Rates from Cost Center Plan). | Check the data on the first five tabs |  |
| 5 | Maintain Driver | Maintain raw material prices and overhead costs on the respective tabs. |  |  |
| 6 | Calculate Product Costs | On the COGS per Lot tab, use data action Calculate Product Costs.Also, check the result on the Calculate Product Cost Rates tab. | New product costs are displayed. |  |
| 7 | Check Data | Raw material RAW20 has a raw material costing. For example, it consists of two components with different G/L accounts. | Check raw material RAW20 on the Raw Material Prices, COGS per Lot and Calculate Product Costs tab |  |

#### Perform Product Cost Resource Planning

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_ProductCost_ResourcePlanning. | The Story SAP_FI_IFP_IM_ProductCost_Resource Planning is displayed. |  |
| 3 | Create Data | If you didn’t execute the planning functions already within the SAP_FI_IFP_IM_ProductCost_RateCalculation story, perform the data actions on the first two tabs. | Check the data on the two tabs. |  |
| 4 | Prepare Sales Quantities | If you did not perform Sales & Profitability planning, switch to the SAP_FI_IFP_IM_Profitability_Planning story on the Plan Quantity tab and perform data action Copy Quantities from Actuals. | Sales quantities in sales & profitability planning are displayed. |  |
| 5 | Copy Sales Quantities | On the Sales Quantities tab, use data action Copy Quantities from Profitability Plan. | Check the data in the table. |  |
| 6 | Calculate Cost Center Resources | On the Cost Center Resources tab, use data action Calc. Cost Center Resources to calculate the cost center resource consumption. | Total credit activity quantity per cost center is displayed. |  |
| 7 | Calculate Raw Material Resources | On the Raw Material Resources tab, use data action Calc. Material Resources to calculate the raw material resource consumption. | Total debit and credit raw material quantity per plant and material is displayed. |  |
| 8 | Calculate Inventory Changes | On the Raw Material Inventory tab, use data action Calc. Material Inv. Changes. | Debit and credit amounts are displayed with an inventory G/L account. |  |
| 9 | Calculate Overheads | On the Manufacturing Overhead tab, use data action Calculate Manufacturing Overhead. | Total overhead costs are displayed. |  |

#### Review Product Cost Reports

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_ProductCost_Reports. | The Story SAP_FI_IFP_IM_ProductCost_Reports is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year, Company Code, Plant, and Product as necessary. | The displayed data is filtered. |  |
| 4 | Select Product | Select a product from the table on the left side. | The displayed data is filtered. |  |
| 5 | Review Plan Data | Review the play data. | Plan data is displayed. |  |

#### Review Product Cost Analytics

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_ProductCost_Analytics. | The Story SAP_FI_IFP_IM_ProductCost_Analytics is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year, Company Code, Plant, and Product as necessary. | The displayed data is filtered. |  |
| 4 | Review Plan Data | Review the plan data. | Plan data are displayed. |  |
| 5 | Select Drill-Through Page | On the Drill-through page, review the charts. | Displayed data are filtered |  |
| 6 | Review Plan Data | Review the plan data. | Plan data are displayed. |  |

### Sales and Profitability Planning

#### Perform Planning Admin Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Step 3 Create sample data of this procedure only is necessary for the stand-alone test with sample data, not for the SAP S/4HANA integration test.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, choose Files . | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Profitability_PlanAdmin. | The story SAP_FI_IFP_IM_Profitability_PlanAdmin is displayed. |  |
| 3 | Create Sample Data | On the Create Sample Data tab, run data actions Create Sample Data for Actuals and Convert Units for Actuals. | Sample Actuals data are displayed |  |
| 4 | Optional: Execute Planning Functions | Choose the Planning Functions tab.Execute the data actions. | Resulting Plan data is displayed. |  |
| 5 | Publish Actual and Plan data | Choose Publish Data and choose Publish All. | Success message is displayed. |  |

#### Perform Sales and Profitability Planning

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Profitability_Planning. | The story SAP_FI_IFP_IM_Profitability_Planning is displayed. |  |
| 3 | Copy Actual Data to Plan | On the Plan Quantity tab, use data action Copy Quantities from Actuals. | Resulting Plan data is displayed. |  |
| 4 | Review and Adjust Quantities | On the Plan Quantity tab, expand the date selection to show the plan periods and adjust the quantities. | Entered quantities are accepted. |  |
| 5 | Enter Control Parameters | Select a base level account on the Quantity Parameter Setting tab and enter a control parameter for first open period of Plan. | Control parameter values are accepted. |  |
| 6 | Run Control Parameters | On the Quantity Parameter Setting tab, use data action Apply Control Parameters to Sales Quantities. | Quantity values are calculated based upon control parameters selected. Check Budget data values and calculations |  |
| 7 | Run Sales Prices | On the Sales Price tab, use data action Derive Sales Prices from Actuals | Resulting plan data are displayed. |  |
| 8 | Review and Adjust Prices | On the Sales Price tab, expand the date selection to show the plan periods and adjust the prices. | Entered prices are accepted. |  |
| 9 | Run Sales Deductions | On the Sales Deductions % tab, use data action Derive Deductions from Actuals | Resulting plan data are displayed. |  |
| 10 | Adjust Sales Deduction % | On the Sales Deductions % tab, expand the date selection to show the plan periods and adjust the deduction percentages. | The percentages are accepted. |  |
| 11 | Run Product Cost Rates | On the Product Cost Rates tab, run the data action Derive Product Cost Rates from Actuals. | The resulting plan data is displayed. |  |
| 12 | Calculate Profitability | On the Product Profitability tab, run the data action Calculate Profitability. | The system displays a success message. Confirm the gross revenue, sales deductions, and COGS amounts. |  |

#### Allocate Sales and Admin Costs

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
| 1 | Access the file menu | Open the Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the story | Find and display the story SAP_FI_IFP_IM_Cross_AllocateSales&AdminCosts | The story SAP_FI_IFP_IM_Cross_AllocateSales&AdminCosts is displayed. |  |
| 3 | Review Sales and Admin Costs | On the Allocate Sales & Admin Costs tab, review the table at the left. | The table displays the cost center debits and credits in the OPEX model. The difference between the debits and credits is considered sales and admin costs. |  |
| 4 | Allocate Sales and Admin Costs to Plant and Product | On the Allocate Sales & Admin Costs tab, use the data action Allocate Sales & Admin Costs from Cost Center | In the table on the right, the sales and admin costs are allocated to the Plant and Product dimensions in the Profitability model. In the table on the left, a credit in the OPEX model is posted, resulting in the sum of debits and credits being zero.Note Not all cost centers appearing in the table are subject to this process. The data action parameter specifies the selected cost centers. The allocation is based on the plan gross revenue for the plant and product dimensions. If plan gross revenue isn't present in the profitability model, the process posts the debit to the unassigned member of plant and product. |  |

#### Review Sales and Profitability Reports

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the sales and profitability reports.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, choose Files . | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Profitability_Reports. | The story SAP_FI_IFP_IM_Profitability_Reports is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year, Company Code, Profit Center, Customer, Product, and Plant as necessary. | Displayed data are filtered. |  |
| 4 | Review Plan Data | On each tab, review the plan data. | Plan data are displayed. |  |

#### Review Sales and Profitability Analytics

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you review the analytics for sales and profitability.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, choose Files . | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Profitability_Analytics. | The story SAP_FI_IFP_IM_Profitability_Analytics is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year and Company Code as necessary. | Displayed data are filtered. |  |
| 4 | Profitability Overview | Review the plan data. | Plan data are displayed. |  |
| 5 | Customer View | Adjust the Customer input control selections.Review the plan data. | Plan data are displayed and filtered. |  |
| 6 | Product and Plant View | Toggle the Select Dimension radio button. Adjust the Product and Plant input control selections.Review the plan data. | Plan data are displayed and filtered. |  |

### Capital Expense Planning

#### Perform Planning Admin Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Step 3 Create sample data of this procedure only is necessary for the stand-alone test with sample data, not for the SAP S/4HANA integration test.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, open Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_CAPEX_PlanAdmin. | The StorySAP_FI_IFP_IM_CAPEX_PlanAdmin is displayed. |  |
| 3 | Create sample data | On the Create Sample Data tab, use data actions Create Sample Data for Actuals and Create Sample Data for Plan.If necessary, first delete the existing data with the other data actions. | Sample data for actuals and for plan depreciation parameter settings are displayed. |  |
| 4 | Optional: Execute planning functions | Choose the Planning Functions tab.Execute the data action Copy Capital Expenses from Actuals and Calculate Depreciation. | Resulting plan data is displayed. |  |
| 5 | Save plan data | Either choose Publish Data or leave the story and choose Publish All. |  |  |

#### Perform Capital Expense Planning

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_CAPEX_Planning. | The Story SAP_FI_IFP_IM_CAPEX_Planning is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Profit Center as necessary. | Displayed data are filtered. |  |
| 4 | Maintain Parameter Settings | On the Parameter Settings tab, enter data. | Plan data is displayed. |  |
| 5 | Maintain Plan Data | On the Capital Expenses tab, enter data. | Plan data is displayed. |  |
| 6 | Execute Planning Function | On the Capital Expenses tab, execute the data action Calculate Depreciation. | You calculated the depreciation. |  |

#### Perform Capital Asset Request Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform planning for capital asset requests.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, open Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_CAPEX_CAR_Planning. | The story is displayed. |  |
| 3 | Create CAR | Select the Create CAR data action. | The Create Capital Asset Request form is displayed. |  |
| 4 | Enter Details | Make the following entries and choose Save:Capital Asset Request Description: <any description>In Service Period: <service period>, for example, 202606Cost Center: <cost center>, for example, xx101301 (where xx is your two-digit company code prefix)PFP Project: I.0000007Asset Type: 16002000Depr./ Amort Method: Straight-LineUseful Life (Yrs): 3Salvage Value % (Amort N/A): 10 | The system displays a message that the CAR is being created. |  |
| 5 | Add Investment | Select the Add Investment data action.Select the CAR you just created under the ALL_CAR hierarchy.Select any G/L account under 018 Operating Expenses (for example, 61002000).Choose Run. | A new row is added in the table for your CAR and G/L account. |  |
| 6 | Add Investment Data | In a period or periods before or including the In Service Date, enter your amounts. For example, if P6 2026 is the in-service date, enter data in P1 to P6 2026 only. |  |  |
| 7 | Calculate In Service | Perform the Calculate In Service data action. | Credits for the selected G/L account and debits for Assets under Construction are created in the periods data was entered. Debits for the selected Asset Type and credits for Assets under Construction are created in the In Service Date period. |  |
| 8 | Asset Purchase | Choose the Asset Purchase tab.Perform the Create CAR data action. | The Create Capital Asset Request form is displayed. |  |
| 9 | Enter Details | Make the following entries and choose Save:Capital Asset Request Description: <any description>Purchase Date: <purchase date>, for example, 202607Cost Center: <cost center>, for example, xx101301 (where xx is your two-digit company code prefix)PFP Project: I.0000007Asset Type: 16005000Depr./ Amort Method: Declining BalanceUseful Life (Yrs): 3Salvage Value % (Amort N/A): 10 | The system displays a message that the CAR is being created. A new row is added in the table for the CAR and G/L account, displaying the purchase amount in the purchase period. |  |
| 10 | Calculate Depreciation and Amortization | Choose the Calculate Depr & Amort tab.Perform the Calculate Depr & Amort data action. | The calculation is displayed. |  |
| 11 | Reporting | Choose the Reporting tab.Review the data. |  |  |

#### Perform Capital Expense Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity you perform reporting for capital expenses.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, open Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_CAPEX_Reports. | The story is displayed. |  |
| 3 | CAPEX | Choose the CAPEX tab. | Data is displayed. |  |
| 4 | CAPEX by CAR | Choose the CAPEX by CAR tab. | Data is displayed. |  |
| 5 | CAR Depreciation and Amortization | Choose the CAR Depr & Amort tab. | Data is displayed. |  |

#### Perform Portfolio Planning Integration Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform portfolio planning integration reporting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Results | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, open Files. | The Files page is displayed. |  |
| 2 | Access the STory | Find and display the story SAP_FI_IFP_IM_CAPEX_PFP_Reports | The story is displayed. |  |
| 3 | PFP Overview | Choose the PFP Overview tab. | Data is displayed. |  |
| 4 | PFP Integration | Choose the PFP Integration tab.In the table to the left, set the filter to I.0000007.In the table to the right, ensure the Entry Year is set as 2026. | Filtered data is displayed. |  |

### Financial Statement Planning

#### Perform Planning Admin Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

Step 3 "Create sample data" of this procedure only is necessary for the stand-alone test with sample data, not for the SAP S/4HANA integration test.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_FinancialStatement_PlanAdmin. | The story SAP_FI_IFP_IM_ FinancialStatement_PlanAdmin is displayed. |  |
| 3 | Create Sample Data | On the Create Sample Data tab, run data action Create Sample Data for Actuals. | Sample Actuals data are displayed |  |
| 4 | Perform Entering FTE | Choose the Enter FTE tab.Enter data for actual and planned period. | Entered amounts are accepted. |  |
| 5 | Optional: Execute Planning Functions | Choose the Planning Functions tab.Execute the data actions. | Resulting Plan data is displayed. |  |
| 6 | Optional: Execute Planning Functions | Choose the Trading Partner tab.Execute the data action. | Resulting Plan data is displayed. |  |
| 7 | Optional: Execute Plan Parameter Setting | Choose the Parameter Setting tab. Select a base level account. Enter a control parameter for the first open period plan.Run the Apply Control Parameters to Profit and Loss data action. | Control parameters and values are entered. Check the plan data values and calculations. |  |
| 8 | Publish Actual and Plan Data | Choose Publish Data and choose Publish All. | Success message is displayed. |  |

#### Perform Financial Statement Target Planning

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
| 1 | Access the Story Page | Open the Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP _IM_ FinancialStatement _TargetPlanning | The story SAP_FI_IFP _IM _ FinancialStatement _TargetPlanning is displayed. |  |
| 3 | Copy Net Income Actual Data to Target | On the Profit and Loss tab, use the data action Copy P&L and Balance Sheet from Actual s | Resulting target data are displayed. |  |
| 4 | Review and Adjust Profit and Loss Amounts | On the P&L by PC tab, adjust the net income amounts. | Entered amounts are accepted. |  |
| 5 | Review and Adjust Profit and Loss Amounts | On the PC by P&L Acct tab, select G/L accounts and adjust the Profit Center amounts. | Entered amounts are accepted. |  |
| 6 | Plan Balance Sheet Changing Balance | On the Balance Sheet - Changing tab, adjust the changing amounts and first period opening amount. | Entered amounts are accepted. |  |
| 7 | Plan Balance Sheet Closing Balance | On the Balance Sheet - Closing tab, adjust the closing amounts and first period opening amount. | Entered amounts are accepted. |  |
| 8 | Carryforward Balance Amounts | On the Balance Sheet - Closing tab, use the data action Calculate Balance Sheet | Resulting target data is adjusted. |  |
| 9 | Review Balance Sheet Plan | On the Balance Sheet Report tab, review the resulting target data. | Resulting target data are displayed. |  |
| 10 | Calculate Cash Flow | On the Cash Flow tab, use the data action Calculate Cash Flow for Target | Resulting target data are displayed. |  |
| 11 | Review Cash Flow | On the Cash Flow tab, review the resulting plan data. | Validation Balance row is zero for all target periods. |  |
| 12 | Review Version Comparison P&L/BS | On the Version Comparison P&L/BS tab, review the plan vs target version comparison for profit & loss and balance sheet accounts. | Resulting plan and target data are displayed. |  |
| 13 | Review Version Comparison CF | On the Version Comparison CF tab, review the plan vs target comparison version for cash flow accounts. | Resulting plan and target data are displayed. |  |

#### Perform Financial Statement Planning

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_FinancialStatement_Planning. | The story SAP_FI_IFP_IM_FinancialStatement_Planning is displayed. |  |
| 3 | Copy Net Income Actual Data to Plan | On the Profit and Loss tab, use data action Copy P&L and Balance Sheet from Actuals. | Resulting Plan data is displayed. |  |
| 4 | Transfer Plan Data from Sales and Profitability model | On the Profit and Loss tab, use data action Copy Gross Margin from Profitability Plan. | Resulting Plan data is displayed. |  |
| 5 | Transfer Plan Data from Cost Center model | On the Profit and Loss tab, use data action Copy Operating Expense from Cost Center Plan. | Resulting Plan data is displayed. |  |
| 7 | Review and Adjust Profit and Loss Amounts | On the Profit and Loss tab, adjust the net income amounts. | Entered amounts are accepted. |  |
| 8 | Split Profit and Loss by Trading Partner | On the Profit and Loss tab, use data action Split Profit and Loss by Trading Partner. In the story SAP_FI_IFP_IM_FinancialStatement_Reports (described in the next section), on the P&L by Trading Partner tab, check that the amounts split by trading partners are correct - see the Plan Weights for Trading Partner Splitting from the Trading Partner tab in the admin story for reference. | Allocated amounts are correct. |  |
| 9 | Calculate Drivers | On the Balance Sheet – Driver-based tab, use data action Calculate Drivers. | Resulting drivers for plan are displayed in top table. |  |
| 10 | Plan Driver Inputs | On the Balance Sheet – Driver-based tab, adjust the drivers in the top table. | Entered amounts are accepted. |  |
| 11 | Calculate Closing Amounts | On the Balance Sheet – Driver-based tab, use data action Calculate Closing Amounts. | Resulting plan data are displayed. |  |
| 12 | Carry Forward Balance Amounts | On the Balance Sheet – Driver-based tab, use data action Calculate Balance Sheet. | Resulting plan data are displayed. |  |
| 13 | Transfer Plan Data from Capital Expense Planning model | On the Balance Sheet - Changing tab, use data action Copy Asset Acquisition from Capital Expense Plan. | Resulting plan data are displayed. |  |
| 14 | Transfer Plan Data from Product Cost Model | On the Balance Sheet - Changing tab, use data action Copy Raw Material from Product Cost Plan. | Resulting plan data are displayed. |  |
| 15 | Plan Balance Sheet Changing Balance | On the Balance Sheet - Changing tab, adjust the changing amounts and first period opening amount. | Entered amounts are accepted. |  |
| 16 | Plan Balance Sheet Closing Balance | On the Balance Sheet - Closing tab, adjust the closing amounts and first period opening amount. | Entered amounts are accepted. |  |
| 17 | Carryforward Balance Amounts | On the Balance Sheet - Closing tab, use data action Calculate Balance Sheet. | Resulting plan data is adjusted. |  |
| 18 | Review Balance Sheet Plan | On the Balance Sheet Report tab, review the resulting plan data. | Resulting Plan data is displayed. |  |
| 19 | Calculate Cash Flow | On the Cash Flow tab, use data action Calculate Cash Flow for Plan. | Resulting Plan data is displayed. |  |
| 20 | Review Cash Flow | On the Cash Flow tab, use data, review resulting plan data. | Validation Balance row is zero for all plan periods. |  |

#### Review Financial Statement Target Reports

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
| 1 | Access the Story Page | Open the Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP _IM_ FinancialStatement _Reports | The story SAP_FI_IFP _IM_ FinancialStatement _Reports is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year, Company Code, Profit Center, Functional Area, and Trading Partner as necessary. | Displayed data are filtered. |  |
| 4 | Review Plan Data | On each tab, review the plan data. | Plan data are displayed. |  |

#### Review Financial Statement Reports

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_FinancialStatement_Reports. | The story SAP_FI_IFP_IM_FinancialStatement_Reports is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year, Company Code, Profit Center, Functional Area, and Trading Partner as necessary. | Displayed data are filtered. |  |
| 4 | Review Plan Data | On each tab, review the plan data. | Plan data is displayed. |  |
| 5 | Drill-Through via Profitability Dimensions | Select any cell in the table on the top of the page. | Plan data from the Sales & Profitability model are displayed in the table at the bottom of the page.Note Amounts between the Financial Statement and Sales & Profitability models only match if the Copy Gross Margin from Profitability data action has been run. |  |
| 6 | Drill-Through via Cost Center Dimensions | Select any cell in the table on the top of the page. | Plan data from the OPEX model are displayed in the table at the bottom of the page.Note Amounts between the Financial Statement and OPEX models only match if the Copy Operating Expense from Cost Center Plan data action has been run. |  |

#### Review Financial Statement Target Analytics

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
| 1 | Access the Story Page | Open the Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP _IM_ FinancialStatement _TargetAnalytics | The story SAP_FI_IFP _IM_ FinancialStatement _TargetAnalytics is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year, Company Code, and Profit Center as necessary. | Displayed data are filtered. |  |
| 4 | Select Target P&L Overview tab | Review the plan and target data. Adjust the Select KPI input control. | Plan and Target data are displayed. |  |
| 5 | Select Target Balance Sheet Overview tab | Review the plan and target data. | Plan and Target data are displayed. |  |

#### Review Financial Statement Analytics

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
| 1 | Access the Story Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_FinancialStatement_Analytics. | The story SAP_FI_IFP_IM_FinancialStatement_Analytics is displayed. |  |
| 3 | Adjust Story Filters | Adjust story filters for Plan Year and Company Code as necessary. | Displayed data are filtered. |  |
| 4 | Select P&L Overview tab | Choose the P&L Overview tab.Review the plan data. Adjust the Select KPI input control. | Plan data is displayed. |  |
| 5 | Balance Sheet Overview | Choose the Balance Sheet Overview tab.Review the plan data. | Plan data is displayed. |  |
| 6 | Drill-Through by Profitability Dimensions | On the Drill-through tab, select a cell in the table on the top of the page. | Plan data from the Sales & Profitability model are displayed in the charts (By Customer, By Product, By Plant).Note Amounts between the Financial Statementand Sales & Profitability models match only if the Copy Gross Margin from Profitability Plan step is completed. |  |
| 7 | Drill-Through by Cost Center Dimensions | On the Drill-through tab, select a cell in the table on the top of the page. | Plan data from the OPEX model are displayed in the chart (By Cost Center).Note Amounts between the Financial Statement and OPEX models only match if the Copy Operating Expense from Cost Center Plan step is completed. |  |

### Product Unit Conversion

#### Perform Admin Tasks

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
| 1 | Access the Story Page | Open Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP _IM_ ProductUnits _PlanAdmin | The story SAP_FI_IFP _IM_ ProductUnits_PlanAdmin is displayed. |  |
| 3 | Create sample data | On the Create Sample Data tab, run data action Create Sample Data for Product Units | Sample product-dependent conversion factors (numerator and denominator) are displayed. |  |
| 4 | Derive Product Quantity Units | On the Product Units tab, run data action Derive Product Quantity Units | Product-independent conversion factors (for example, mass, volume, or time) are displayed in addition to the existing product-dependent conversion factors. |  |
| 5 | Publish Actual data | Choose Publish Data and choose Publish All | Success message is displayed. |  |

### Cross Automated Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform cross automated planning.

Prerequisite

Actuals data must be available in the system.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the LandingPage story | Access the LandingPage story as described in [Landing Page](#unique_9) [page ] 9. | The LandingPage story is displayed. |  |
| 2 | Access the story | Choose the General tab.Access the Automated Planning story. | The story SAP_FI_IFP_IM_Cross_AutomatedPlanning is displayed. |  |
| 3 | Growth rates tab | The Plan Growth Rates tab shows products, materials, and G/L accounts with actual data. |  |  |
| 4 | Create consistent sample plan version | To create a consistent sample plan version, ensure growth rates are zero or blank. Choose the Review Financial Statement tab, then perform Calculate Plan Version. | A consistent sample plan version is created.To validate the results you can compare your data with the screen shots below this procedure table. |  |
| 5 | Enter growth rates | On the Plan Growth Rates tab, enter growth rates for sales quantities and sales price on product, expenses on G/L account, material price on the material level, and asset and depreciation on the asset level.Enter growth rate on the node level. | Data is distributed to all available objects (master data driven). |  |
| 6 | Calculate plan version | On the Review Financial Statement tab, perform Calculate Plan Version. | A plan version is calculated based on the actuals of the previous year multiplied with the respective growth rates.% YoY growth is visible in all tables for comparison. |  |

### Cross-Simulation Cockpit

#### Prerequisites

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform a full planning cycle to create the necessary transaction data. Trigger the following data actions in the given order to run a complete planning cycle and generate consistent plan data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | Iin the Main Menu, choose Files. | The Files page is displayed.. |  |
| 2 | Open Story | Find and display the story:SAP_FI_IFP_IM_Cross_SimulationCockpit | The story is displayed. |  |
| 3 | Application Menu | To open the application menu, choose the menu icon in the upper left corner.. |  |  |
| 4 | Prepare Demo Data | Acces the Prepare Demo Data functionality. | The dialog box offers two options:Create Sample Reference DataCreate Consistent Sample Plan Version |  |
| 5 | Create Consistent Plan version | Select Create Consistent Sample Plan Version and choose Perform. | A consistent sample plan version is created. To validate the results, compare your data in the Financial Overview section with the screenshots below this table. |  |
| 6 | Publish the data | Choose Publish Data. Choose Publish All. | The system displays a success message. |  |

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

<!-- image omitted: unnamed -->

#### Perform Cross-Model Simulation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the cross-model simulation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the file menu | From the Main Menu, choose Files . | The Files page is displayed. |  |
| 2 | Access the application | Find and display the app:SAP_FI_IFP_IM_Cross_SimulationCockpit | The story SAP_FI_IFP_IM_ Cross_SimulationCockpit is displayed. |  |
| 3 | Test Header Functions | On the landing page, test all buttons in the header area:MenuExitFilterVersion ManagementSave a CopyResume existing simulationDeleteBookmarkData FlowUser SettingsHelp | You shouldn’t receive any error messages. You can switch between the simulation scenarios. |  |
| 4 | Access Available Simulation Scenarios | To access any of the simulation scenarios, choose either the menu or the boxes at the bottom of the landing page. | The system displays a planning layout that contains different tabs with tables and data actions depending on the selected simulation scenario. |  |
| 5 | Save Copy of Version Plan for Reference | After creating a consistent sample plan version as described in the Prerequisites section, choose Save a Copy to create a backup or reference version of the plan (for example, name it Plan Secured). | Your new version is shown in all tables. |  |
| 6 | Test Data Integrity | Without changing any drivers, run all planning functions of the scenario in the given order or choose the One-Click-Button (Trigger All Data Actions for this Simulation) in the upper right corner. | No data should change. |  |
| 7 | Change Data Entries and Trigger Planning Functions | On the Adjust… tabs, change some drivers in your chosen simulation scenario.Use the One-Click-Button in the upper right corner to trigger all planning functions of the selected simulation process with one click or trigger all planning functions in the given order to see the effect of the changed data on your product profitability and P&L.Additionally, check the data in the Financial Overview. | Depending on your changes, you should see an increase or decrease of your product profitability and P&L compared with your reference version (created in step 5). |  |
| 8 | Test Button Functions | Test the functionality of the following buttons:HeaderInfo AreaCollapse / expand data action areaWhere possible, switch to the table view. | You shouldn’t receive any error messages. You can switch between views, as well as expand and collapse data action area. |  |
| 9 | Save Copy of Version Plan for Reference | Use Save a Copy to create a copy (for example, name it Best Scenario). | Your copied version is shown in all tables. |  |
| 10 | Test bookmark functionality | Change the drill setting of tables, change filter settings, user settings, collapse data action area, and create a bookmark within any of the simulation processes.Use Bookmark Current State and enter a name for your bookmark.Choose if you want to save the bookmark as a Personal or Global bookmark.Save the bookmark and leave the app. | The new bookmark displays in the list, with the info if it's a personal or global bookmark |  |
| 11 | Open bookmark | Open the bookmark eithervia the main menu Analytic Applications > Bookmarks tab and search for your bookmarkopen the simulation cockpit and click on the bookmark icon in the header Manage Bookmarks, select your bookmark and choose Open. | the app should open with the saved settings, drill-state, etc. |  |
| 12 | Share personal bookmark | Use Manage Bookmarks to share a personal bookmark with another user | Other users can access your bookmark. |  |
| 13 | Delete bookmark | Delete the bookmark you've created. | The bookmark is removed from the list. The bookmark is also not visible in the Analytic Applications > Bookmarks tab |  |
| 14 | Resume Simulation | Use Resume existing Simulation to copy the version you created in step 5 back to the Plan version. | The Plan version should show the same data as the version created in step 5. |  |
| 15 | Delete Version | Delete all versions you created. | The versions should be removed from the filter line and all tables. |  |
| 16 | Revert Version | Choose Revert Plan version. | No unpublished data is available for your user. |  |

### Cross-Model Parameter Setting

#### Plan Sales Quantities

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
| 1 | Access the file menu | Open the Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the application | Find and display the app SAP_FI_ IFP _IM_ Cross_ParameterSetting | The SAP_FI_ IFP _IM_ Cross_ParameterSetting is displayed. |  |
| 3 | Access the story | On the homepage, select the Plan Sales Quantities link | The parameter setting table is displayed. |  |
| 4 | Enter Control Parameters | Select a Control Parameter cell and use the Select Control Parameter drop-down menu to populate the first open period of plan with a control parameter. | Control parameter values are accepted. |  |
| 5 | Run Control Parameters | Use the data action Apply Control Parameters to Sales Quantities. | Quantity values are calculated based upon control parameters selected. Check plan data values and calculations. |  |
| 6 | Return to Home Page | Choose Home. | The home page is displayed. |  |

#### Plan Operating Expenses

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
| 1 | Access the story | On the homepage, select the Plan Operating Expenses link | The parameter setting table is displayed. |  |
| 2 | Enter Control Parameters | Select a Control Parameter cell and use the Select Control Parameter drop-down menu to populate the first open period of plan with a control parameter. | Control parameter values are accepted. |  |
| 3 | Run Control Parameters | Use the data action Apply Control Parameters to Cost Center Expenses. | Cost center expense values are calculated based upon control parameters selected. Check plan data values and calculations. |  |
| 4 | Return to Home Page | Choose Home. | The home page is displayed |  |

#### Plan Profit and Loss

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
| 1 | Access the story | On the homepage, choose Plan Profit and loss. | The parameter setting table is displayed. |  |
| 2 | Enter Control Parameters | Select a Control Parameter cell and use the Select Control Parameter drop-down menu to populate the first open period of plan with a control parameter. | Control parameter values are accepted. |  |
| 3 | Run Control Parameters | Use the data action Apply Control Parameters to Profit and Loss | Profit and Loss values are calculated based upon control parameters selected. Check plan data values and calculations. |  |
| 4 | Return to Home Page | Choose Home. | The home page is displayed |  |

### Cross Greenhouse Gas Emission Planning

#### Prerequisites

Purpose

You must perform a full planning cycle to create the necessary transaction data.

Perform all planning steps in the [Operating Expense Planning](#unique_10) [page ] 12, [Product Cost Planning](#unique_11) [page ] 22, [Sales and Profitability Planning](#unique_12) [page ] 26, [Capital Expense Planning](#unique_13) [page ] 31, and [Financial Statement Planning](#unique_14) [page ] 36 sections, or perform the procedure below to run a complete planning cycle and generate consistent plan data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the file menu | Open the Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the application | Find and display the app SAP_FI_ IFP _IM_ Cross_SimulationCockpit. | The story SAP_FI_ IFP _IM_ Cross_SimulationCockpit is displayed. |  |
| 3 | Open the application menu | Open the application menu with the menu icon in the upper left corner. |  |  |
| 4 | Prepare demo data | Access the Prepare Demo Data functionality. | The dialog box offers two options:Create Sample Reference DataCreate Consistent Sample Plan Version |  |
| 5 | Create Consistent Sample Plan Version | Select Create Consistent Sample Plan Version and choose Perform. | A consistent sample plan version is created.To validate the results, you can compare your data in the Financial Overview section with the following screen shots:<!-- image omitted: unnamed --><!-- image omitted: unnamed --><!-- image omitted: unnamed --> |  |
| 6 | Publish the data | Choose Publish Data . Choose Publish All . | The system displays a success message. |  |

#### Perform Cross Model Greenhouse Gas Emission Factor Planning and Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the factor planning and valuation for cross model greenhouse gas emissions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | Open the Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Cross_CO2E_FactorPlanningAndValuation. | The Story SAP_FI_IFP_IM_Cross_CO2E_FactorPlanningAndValuation is displayed. |  |
| 3 | Maintain raw material factors | Maintain factors for raw material CO2e per component unit. |  |  |
| 4 | Run raw material CO2e calculation | Choose the Raw Material CO2 tab.Use data action Calculate Raw Material CO2e. | CO2e per material and quantity unit is displayed. |  |
| 5 | Maintain cost center spend-based factors | Choose the CCtr Factors Spend-Based tab.Maintain the factors. |  |  |
| 6 | Maintain cost center activity-based factors | Choose the CCtr Factors Activity-Based tab.Maintain the factors. |  |  |
| 7 | Run cost center CO2e calculation | Choose the Cost Center CO2 tab.Use data action Calculate Cost Center CO2e. | CO2e per cost center and activity type is displayed. |  |
| 8 | View total CO2e | Choose the Total CO2 tab.Use data action Copy CO2e from Underlying Plans. | CO2e data per GHG category is displayed. |  |

#### Perform Cross Model Greenhouse Gas Emission Allocation to Cost Center and Product

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform the allocation to cost center and product for cross model greenhouse gas emissions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | Open the Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Cross_CO2E_AllocationToCCtrAndProduct. | The Story SAP_FI_IFP_IM_Cross_CO2E_AllocationToCCtrAndProduct is displayed. |  |
| 3 | Run cost center CO2e to cost center allocation | Choose the Allocations tab. Use data action Allocate Cost Center CO2e to Cost Center. | CO2e data are distributed between cost centers according to the cost center allocation weights maintained in the Admin story. CO2e data values are posted to Account Secondary costs. |  |
| 4 | Split cost center CO2e to activity types | Choose the CO2e Activity Dependent tab. Use data action Split Cost Center CO2e by Activity Type. | Cost Center CO2e are allocated to activity types according to the splitting weights maintained in the Admin story. |  |
| 5 | View actual activity quantities | Choose the Total Activity Output tab. | Activity quantities are displayed. |  |
| 6 | Run CO2e activity rate calculation | Choose the CO 2e Activity Rate tab.Use data action Calculate CO2e Activity Rate. | CO2e activity rates are displayed. |  |
| 7 | Run CO2e product rate calculation | Choose the CO 2e Product Rate tab.Use data action Calcu late CO2e P roduct Rate. | CO2e product rates are displayed. |  |
| 8 | Calculate CO2e for manufacturing overheads | Choose the Manufacturing Overhead tab.Use data action Calculate CO2e for Manufacturing Overheads. | Total overhead CO2e are displayed. |  |
| 9 | Copy CO2e overheads to cost center | Use data action Copy CO2e Overheads to Cost Center Plan. | Overhead CO2e data is copied to cost center plan. |  |
| 10 | Allocate sales and admin CO2e to plant and product | Choose the Allocate Sales & Admin CO2e tab.Use data action Allocate Sales & Admin CO2e. | In the right-hand table, the sales and admin costs are allocated to the Plant and Product dimensions in the Profitability model. In the left-hand table, a Credit in the OPEX model is posted resulting in the sum of debits and credits being zero.Note: Not all cost centers appearing in the table are subject to this process. The data action parameter specifies the selected cost centers. The allocation is based on the plan gross revenue for the plant and product dimensions. If plan gross revenue is not present in the profitability model, the process will post the debit to the unassigned member of plant and product. |  |
| 11 | Run raw material CO2e credit calculation | Choose the Raw Material CO2 tab. Use data action Calculate Raw Material CO2e Credit. | CO2e credits per material is displayed. |  |
| 12 | Run product CO2e calculation | Choose the Product CO2 tab. Use data action Calculate Product CO2e. | CO2e per product is displayed. |  |
| 13 | View cost center CO2e | Choose the Cost Center CO2 tab. Review the CO2e per cost center. | CO2e per cost center is displayed. |  |
| 14 | View total CO2e | Choose the Financial Statement tab. Use data action Copy CO2e from Underlying Plans. | CO2e data per GHG category, in financial statement, and CO2e-flow statement is displayed. |  |
| 15 | Drill-through to underlying plans | Choose the Financial Statement Drill-through tab.Select any bar in the Corporate CO2e by GHG Category bar chart. | Underlying plan data from the Sales & Profitability, Product Cost and Operating Expense plans are displayed in the three tables. |  |
| 16 | View KPIs | Choose the KPIs tab. | KPIs for Corporate CO2e and Product CO2e are displayed. |  |

#### Perform Cross Model Greenhouse Gas Emission Variance Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you perform cross model greenhouse gas emission variance analysis.

Prerequisites

Perform Greenhouse Gas Emission Factor Planning and Valuation story.

Perform Greenhouse Gas Emission Allocation to Cost Center and Product story, without performing Allocate Sales & Admin CO2e from Cost Center data action

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the LandingPage story | Access the LandingPage story as described in [Landing Page](#unique_9) [page ] 9. | The LandingPage story is displayed. |  |
| 2 | Access the Story | Choose the Greenhouse Gas tab.Access the GHG Emission Variance Analysis story. | The Story SAP_FI_IFP_IM_Cross_CO2E_VarianceAnalysis is displayed. |  |
| 3 | Run variance calculation | On the Total CO2e tab, use data action Calculate Variances. | Target1 and Target2 versions are calculated, and the variances are shown. |  |
| 4 | Review raw material data | Choose the Raw Material Overview tab.See target1 and target2 details and the corresponding variances. | Plan data is displayed. |  |
| 5 | Review cost center data | Choose the Cost Center Overview tab.See target1 details and the corresponding sales quantity variance. | Plan data is displayed. |  |
| 6 | Review product data | Choose the Product Variances tab.See target1 and target2 details and the corresponding variances. | Plan data is displayed. |  |
| 7 | Review target1 resource data | Choose the Target1 Resources Overview tab.See target1 details for raw material and cost center. | Plan data is displayed. |  |
| 8 | Review base data | Choose the Financial Base Data tab.See plan and actual data used to calculate target1, target2 and corresponding variances. | Plan data is displayed. |  |

### Cross End-to-End Planning Process

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
| 1 | Access the Story Page | Open the Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Cross_LandingPage | The Story SAP_FI_IFP_IM_Cross_LandingPage is displayed. |  |
| 3 | Sample Process Story | On the General tab, choose Information: End-to-End Sample Process Story. |  |  |
| 4 | Story Details | On the End-to-End Start Page tab, see some details regarding the story. |  |  |
| 5 | See data flow for sample planning process | Choose Data flow for sample planning process to see the data flow. | Data flow tab is displayed. |  |
| 6 | Navigate back to start page | Choose Home to return to the End-to-End Start Page. |  |  |
| 7 | Create Sample Data | Perform Create Sample Data to clean up the models' versions and create the sample data you need. | A Multi-Action is triggered to create the sample data you need. |  |
| 8 | Prepare End-to-End Sample Process | Perform Prepare End-to-End Sample Process to copy actuals into the plan version as a basis on which to start this demo. | A Multi-Action is triggered to copy actuals into the plan version. |  |
| 9 | Start the End-to-End story | On the End-to-End Start Page, choose Start to start the end-to-end planning. | The first planning tab of the story is displayed. |  |
| 10 | Perform End-to-End planning | Follow the instructions on each tab and use the navigation buttons to move back and forth and to perform selected planning activities. | Perform a complete planning process from sales quantity to cash flow planning. |  |

### Add-On Package for IFP

#### Landing Page

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you navigate to the landing page for the Add-On Package for IFP.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | In the Main Menu, open Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Addon_LandingPage. | The Story SAP_FI_IFP_IM_Addon_LandingPage is displayed. |  |
| 3 | Use Navigation | Use the links in the lower section to open any of the stories and show the named tab. | The named story and tab are opened in a new browser tab. |  |

#### Perform Employee Expenses Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Employee expenses data is transferred from SAP__HR_BPL_IM_WORKFORCE model to the SAP_FI_IFP_IM_OPEX model.. This procedure can only be run if the SAP__HR_BPL_IM_WORKFORCE model is implemented. The SAP__HR_BPL_IM_WORKFORCE model isn't part of the Integrated Financial Planning package.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | In the main menu, choose Files . | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Addon_WFPIntegration. | The StorySAP_FI_IFP_IM_Addon_WFPIntegration is displayed. |  |
| 3 | Set the Plan Year and Company Code | In the story filters, set the Company Code. | The story filter is set and the table on the left displays the data from the source model SAP__HR_BPL_IM_WORKFORCE. |  |
| 4 | Transfer Data to Cost Center Model | On the Cross Model Copy tab, use the Copy Employee Expenses from Workforce Planning data action. | Plan data from SAP__HR_BPL_IM_WORKFORCE source model is transferred to the target model SAP_FI_IFP_IM_OPEX and displays in the table on the right. |  |
| 5 | Transfer Data to Financial Statement Model | On the Copy FTE tab, use data actions Copy Actual FTE – from Workforce Planning and Copy Plan FTE – from Workforce Planning. | Actual and Plan data from SAP__HR_BPL_IM_WORKFORCE source model is transferred to the target model SAP_FI_IFP_IM_FinancialStatement and appears in the table on the right. |  |
| 6 | Save plan data | You can either choose Publish Data or leave the story and choose Publish All. |  |  |

#### Perform IBP Consensus Demand Transfer

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Sales quantity data from Integrated Business Planning (IBP) is loaded in the IBP version of the SAP Analytics Cloud model SAP_FI_IFP_IM_Profitability. Step 3 Create sample data of this procedure only is necessary for the stand-alone test with sample data, not for the integration test.

|  |
| --- |
| Caution SAP Integrated Business Planning is a separate product and not part of the Integrated Financial Planning SAP Analytics Cloud content. This add-on package is not applicable to SAP S/4HANA Cloud Public Edition source systems. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | In the main menu, choose Files . | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Addon_IBPIntegration. | The StorySAP_FI_IFP_IM_Addon_IBPIntegration is displayed. |  |
| 3 | Create Sample Data | On the Create Sample Data tab, use the Create Sample Data for IBP and Create Sample Data for PlantProduct data actions.If necessary, first delete the existing data with the Clear IBP Data and Clear PlantProduct Data actions. | Sample data for IBP and PlantProduct are displayed. |  |
| 4 | Set the Plan Year and Plant | In the story filters, set the Plant. | The story filter is set and the table on the left displays the data from the source. |  |
| 5 | Transfer Data to Plan version | On the Copy Demand tab, use the Copy Quantities from IBP data action. | IBP quantity data from SAP_FI_IFP_IM_Profitability is transferred to the plan quantity of SAP_FI_IFP_IM_Profitability and is displayed in the table on the right. |  |
| 6 | Save Plan Data | You can either choose Publish Data or leave the story and choose Publish All. |  |  |

#### Perform CP Sales Planning Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Sales quantities are transferred from SAP_CP_BPL_IM_TargetSetting model to the SAP_FI_IFP_IM_Profitability model within the Integrated Financial Planning for SAP S/4HANA content. The Profit Center is derived using reference data from the SAP_FI_IFP_IM_Addon_PlantProduct model.

|  |
| --- |
| Caution This procedure can only be run if the SAP_CP_BPL_IM_TargetSetting model is implemented. The SAP_CP_BPL_IM_TargetSetting model isn’t part of the Integrated Financial Planning package. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass /Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | In the Main Menu, open Browse > Files. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Addon_ CPS PIntegration | The StorySAP_FI_IFP_IM_Addon_ CPS PIntegration is displayed. |  |
| 3 | Create sample data | On the Create Sample Data tab, run data action Create Sample Data for PlantProduct | Sample data are displayed. |  |
| 4 | Set the Plant | Choose the Copy Quantities tab.In the story filters, set the Company Code and Plant. | The story filters are set. The table at the left displays the data from the source. |  |
| 5 | Transfer Data to Sales and Profitability Model | On the C opy Quantities tab, use the data action Copy Quantities – from CP Sales Planning. | Plan data from SAP_ CP _ BPL _IM_ TargetSetting sourcemodel is transferred to the target model SAP_FI_ IFP _IM_ Profitability and appears in the table on the right.Additionally, Profit Center is derived using the combinations displayed on the Derivation Rule tab and appears in the table on the right. |  |
| 6 | Convert Units | On the C opy Quantities tab, use the data action Convert Units – for Plan | Quantity units are converted to the product’s base unit of measure and displayed in the table on the right. |  |
| 7 | Save plan data | Either choose Publish Data or leave the story and choose Publish All. | The system displays a success message. |  |

#### Perform Commercial Planning Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Sales quantities and Net Revenue (including Gross Revenue and Sales Deductions) are transferred from the SAP_SD_IM_SalesPlanning model to the SAP_FI_IFP_IM_Profitability model within the Integrated Financial Planning for SAP S/4HANA content. The Profit Center is derived using reference data from the SAP_FI_IFP_IM_Addon_PlantProduct model.

|  |
| --- |
| Caution This procedure requires the SAP_SD_IM_SalesPlanning model, which is not included in the Integrated Financial Planning package. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Story Page | Open the Browse ® Files in the Main Menu. | The Files page is displayed. |  |
| 2 | Access the Story | Find and display the story SAP_FI_IFP_IM_Addon_CXCPIntegration | The StorySAP_FI_IFP_IM_Addon_CXCPIntegration is displayed. |  |
| 3 | Create sample data | On the Create Sample Data tab, run data action Create Sample Data for PlantProduct | Sample data are displayed. |  |
| 4 | Set the Plant | Choose the Copy Quantities tab. In the story filters, set the Company Code and Plant. | The Story filters are set and the table on the left-hand side displays the data from the source |  |
| 5 | Transfer Quantity Data to Sales and Profitability Model | On the Copy Quantities tab, use data action Copy Quantities – from Commercial Planning. | Plan data from SAP_SD_IM_SalesPlanning sourcemodel is transferred to the target model SAP_FI_IFP_IM_Profitability and appears in the table on the right-hand side.Additionally, Profit Center is derived using the combinations displayed on the Derivation Rule tab and appears in the table on the right-hand side. |  |
| 6 | Transfer Net Revenue Data to Sales and Profitability Model | Choose the Copy Net Revenue tab. Use data action Copy Net Revenue – from Commercial Planning. | Plan data from SAP_SD_IM_SalesPlanning sourcemodel is transferred to the target model SAP_FI_IFP_IM_Profitability and appears in the table on the right-hand side.Additionally, Profit Center is derived using the combinations displayed on the Derivation Rule tab and appears in the table on the right-hand side. |  |
| 7 | Save plan data | Either choose Publish Data or leave the story and choose Publish All. | Success message is displayed. |  |

#### Perform Sustainability Footprint Management Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Raw Material Factors (CO2e per Component Unit) in the SAP Sustainability Footprint Management (SFM) version of SAP_FI_ IFP _IM_ ProductCost are transferred to the Plan version and have the Company Code dimension derived.

|  |
| --- |
| Caution SAP Sustainability Footprint Management is a separate product and not part of the Integrated Financial Planning SAP Analytics Cloud content. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the LandingPage story | Access the LandingPage story as described in [Landing Page](#unique_61) [page ] 63. | The LandingPage story is displayed. |  |
| 2 | Access the Story | Find the Sustainability Footprint Management section and choose the Create Sample Data link. | The StorySAP_FI_IFP_IM_Addon_SFMIntegration is displayed. |  |
| 3 | Create sample data | On the Create Sample Data tab, run data action Create Sample Data for SFM. | Sample Plan data are displayed. |  |
| 4 | Transfer Data to Plan version | On the Copy Factors from SFM tab use data action Copy Raw Material Factors – from SFM. | CO2e per Component Unit data is transferred from the SFM version to the Plan version of SAP_FI_ IFP _IM_ ProductCost and shows in the table on the bottom.Additionally, the company code is derived using the dimension attribute in the Component Plant dimension. |  |
| 5 | Save plan data | Choose Publish Data or leave the story and choose Publish All. | A success message is displayed. |  |

#### Perform Portfolio Financial Planning Integration

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Project data is transferred from the SAP_ PPM _IM_ Portfolio or SAP_PPM_IM_Portfolio_OP model to the SAP_FI_ IFP _IM_ OPEX model. This procedure can only be run if the SAP_ PPM _IM_ Portfolio or SAP_PPM_IM_Portfolio_OP model is implemented. The  SAP_ PPM _IM_ Portfolio or the SAP_PPM_IM_Portfolio_OP model isn't part of the Integrated Financial Planning package.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the LandingPage story | Access the LandingPage story as described in [Landing Page](#unique_61) [page ] 63. | The LandingPage story is displayed. |  |
| 2 | Access the Story | Find the Portfolio Financial Planning section and select the Copy Projects link.Ensure that you have selected the relvant SAP S/4HANA version. | One of the following stories is displayed:SAP_FI_IFP_IM_Addon_PFP IntegrationSAP_FI_IFP_IM_Addon_PFPIntegration_OP |  |
| 3 | Set the Company Code and Portfolio Hierarchy | On the Copy Projects from PFP tab, in the story filters, set the Company Code and Portfolio Hierarchy. | The story filters are set and the table on the left-hand side displays the data from the source model. |  |
| 4 | Transfer Data to OPEX Model | On the Copy Projects from PFP tab, use data action Copy Projects – from PFP. | Plan data from the SAP_ PPM _IM_ Portfolio or SAP_FI_IFP_IM_Addon_PFPIntegration_OP source model is transferred to the target model SAP_FI_ IFP _IM_ OPEX and appears in the table on the right-hand side.Note: The Approved Budget (Project) data is published in the SAP_PPM_BucketFinPlan story on the Budget Allocation tab. A currency conversion data action is run to create the data in Company Code currency for transfer to Integrated Financial Planning. |  |
| 5 | Save plan data | Choose Publish Data or leave the story and choose Publish All. | A success message is displayed. |  |

### Integration with SAP S/4HANA

#### Operating Expense Planning and Budgeting

##### Load Master and Actual Data from SAP S/4HANA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This procedure only is necessary for the SAP S/4HANA integration test, not for the stand-alone test with sample data.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator. | The Home - Welcome to SAP Analytics Cloud screen is displayed. |  |
| 2 | Cost Center Planning Model | From the main menu, choose Files . Search for and open SAP_FI_IFP_IM_OPEX. | The model SAP_FI_IFP_IM_OPEX is displayed. |  |
| 3 | G/L Account Dimension | Choose SAP_FI_IM_GLACCOUNT. |  |  |
| 4 | Data Management | Choose the Data Management tab. | The Data Management tab is displayed. |  |
| 5 | Refresh the Job | Choose the Refresh button to the right of the job. | The system displays a message stating number of rows imported. |  |
| 6 | Repeat | Repeat steps 3 to 5 for the following dimensions:SAP_ALL_COSTCENTERSAP_FI_IFP_CCACTIVITYTYPESAP_ALL_PROJECT_WBSELEMENTSAP_FI_IFP_PRTNRCOSTCENTERSAP_FI_IFP_PRTNRCCACTIVITYTYPESAP_FI_IFP_PRTNRWBSELEMENTSAP_ALL_PROFITCENTERSAP_ALL_FUNCTIONALAREASAP_ALL_COMPANY_CODE | The system displays a message stating number of rows imported. |  |
| 7 | Go back to the OPEX planning model | From the main menu, choose Files . Search for and open SAP_FI_IFP_IM_OPEX. | The model SAP_FI_IFP_IM_OPEX is displayed. |  |
| 8 | Data Management | Choose the Data Management tab. | The Data Management tab is displayed. |  |
| 9 | Refresh Import Jobs to Load Transaction Data | Under Import Jobs, choose Refresh to the right of the job. | The system displays a message stating number of rows imported. |  |

##### Export Plan Data to SAP S/4HANA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can now export the plan and budget data that you’ve created in the steps before to SAP S/4HANA.

For more information on the export to SAP S/4HANA functionality, see the [documentation](https://help.sap.com/doc/00f68c2e08b941f081002fd3691d86a7/release/en-US/dbf37c1a62e6403a840f8fa026669ee9.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Model Page | From the main menu, open Files . | The Files page is displayed. |  |
| 2 | Access the Model | Find and display the model SAP_FI_IFP_IM_OPEX. | The Model SAP_FI_IFP_IM_OPEX is displayed. |  |
| 3 | Open Data Management | Choose Data Management. | Import and Export jobs are displayed |  |
| 4 | Create Export | On the Export Jobs section, choose Export Data to SAP S/4HANA. | Follow the wizard as described in the documentation |  |

#### Product Cost Planning

##### Load Master and Actual Data from SAP S/4HANA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This procedure only is necessary for the SAP S/4HANA integration test, not for the stand-alone test with sample data.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator | The Home - Welcome to SAP Analytics Cloud screen is displayed. |  |
| 2 | Choose the product cost planning model | From the main menu, choose Files. Search for and open SAP_FI_IFP_IM_ProductCost | The model SAP_FI_IFP_IM_ProductCost is displayed |  |
| 3 | Go to the G/L Account dimension | Choose SAP_FI_IFP_GLACCOUNT. |  |  |
| 4 | Choose the Data Management tab | Choose the Data Management tab. | The Data Management tab is displayed. |  |
| 5 | Refresh the Job | Choose the Refresh button at the right-hand side of the job. | The system displays a message stating number of rows imported. |  |
| 6 | Repeat | Repeat steps 3 to 5 for the following values:SAP_ALL_PLANTSAP_ALL_PRODUCTSAP_FI_IFP_COMPONENTPLANTSAP_ALL_MATERIALSAP_ALL_COSTCENTERSAP_FI_IFP_CCACTIVITYTYPESAP_FI_IFP_FIXVARIABLESAP_FI_IFP_COMPQUANTITY_UNITSAP_FI_IFP_LOTSIZE_UNITSAP_FI_IFP_SALESQUANTITY_UNITSAP_FI_IFP_QUANTITY_UNITSAP_ALL_COMPANY_CODE | The system displays a message stating number of rows imported. |  |
| 7 | Go back to the Product Cost model | From the main menu, choose Files. Search for and open SAP_FI_IFP_IM_ProductCost | The model SAP_FI_IFP_IM_ProductCost is displayed |  |
| 8 | Choose the Data Management tab | Choose the Data Management tab. | The Data Management tab is displayed. |  |
| 9 | Refresh Import Jobs to Load Transaction Data | Under Import Jobs, choose Refresh at the right of the job. | The system displays a message stating number of rows imported. |  |

#### Sales and Profitability Planning

##### Load Master and Actual Data from SAP S/4HANA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This procedure only is necessary for the SAP S/4HANA integration test, not for the stand-alone test with sample data.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator | The Home - Welcome to SAP Analytics Cloud screen is displayed. |  |
| 2 | Go to the sales and profitability planning model | From the main menu, choose Files. Search for and open SAP_FI_IFP_IM_Profitability | The model SAP_FI_IFP_IM_Profitability is displayed |  |
| 3 | Go to the Company Code dimension | Choose SAP_ALL_COMPANY_CODE. | The public dimension is displayed. |  |
| 4 | Choose the Data Management tab | Choose the Data Management tab. | The Data Management tab is displayed. |  |
| 5 | Refresh the Job | Choose the Refresh button at the right-hand side of the job. | The system displays a message stating number of rows imported. |  |
| 6 | Repeat | Repeat steps 3 to 5 for the following dimensions:SAP_FI_IFP_GLACCOUNTSAP_ALL_PLANTSAP_ALL_PRODUCTSAP_ALL_CUSTOMERSAP_ALL_PROFITCENTERSAP_ALL_FUNCTIONALAREASAP_FI_IFP_QUANTITY_UNIT | The system displays a message stating number of rows imported. |  |
| 7 | Go to the profitability model | From the main menu, choose Files . Search for and open SAP_FI_IFP_IM_PROFITABILITY. | The model SAP_FI_IFP_IM_PROFITABILITY is displayed. |  |
| 8 | Choose the Data Management tab | Choose the Data Management tab. | The Data Management tab is displayed. |  |
| 9 | Refresh Import Jobs to Load Transaction Data | Under Import Jobs, choose Refresh at the right-hand side of the job. | The system displays a message stating number of rows imported. |  |

##### Export Plan Data to SAP S/4HANA

Purpose

You can now export the plan and budget data that you’ve created in the steps before to SAP S/4HANA.

For details on the export to SAP S/4HANA functionality, check out the [documentation](https://help.sap.com/doc/00f68c2e08b941f081002fd3691d86a7/release/en-US/dbf37c1a62e6403a840f8fa026669ee9.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Model Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Model | Find and display the model SAP_FI_IFP_IM_Profitability. | The Model SAP_FI_IFP_IM_Profitability is displayed. |  |
| 3 | Open Data Management | Choose Data Management. | Import and Export jobs are displayed |  |
| 4 | Create new export | On the Export Jobs section, choose Export Data to SAP S/4HANA. | Follow the wizard as described in the documentation |  |

#### Capital Expense Planning

##### Load Master Data from SAP S/4HANA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This procedure only is necessary for the SAP S/4HANA integration test, not for the stand-alone test with sample data.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator | The Home - Welcome to SAP Analytics Cloud screen is displayed. |  |
| 2 | Go to the CAPEX model | From the main menu, choose Files. Search for and open SAP_FI_IFP_IM_CAPEX | The model SAP_FI_IFP_IM_ CAPEX is displayed |  |
| 3 | Go to the G/L Account dimension | Choose SAP_FI_IFP_GLACCOUNT. |  |  |
| 4 | Choose the Data Management tab | Choose the Data Management tab. | The Data Management tab is displayed |  |
| 5 | Refresh the Job | Choose the Refresh button at the right-hand side of the job | The system displays a message stating number of rows imported. |  |
| 6 | Repeat | Repeat steps 3 to 5 for the following dimensions:SAP_ALL_PROFITCENTERSAP_ALL_COMPANY_CODE | The system displays a message stating number of rows imported. |  |
| 7 | Go to the CAPEX Model | From the main menu, choose Files. Search for and open SAP_FI_IFP_IM_CAPEX | The model SAP_FI_IFP_IM_ CAPEX is displayed |  |
| 8 | Data Management | Choose the Data Management tab. |  |  |
| 9 | Refresh Import Jobs to Load Transaction Data | Under Import Jobs, choose Refresh to the right of the job. | The system displays a message stating the number of imported rows. |  |

#### Financial Statement Planning

##### Load Master and Actual Data from SAP S/4HANA

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This procedure only is necessary for the SAP S/4HANA integration test, not for the stand-alone test with sample data.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator | The Home - Welcome to SAP Analytics Cloud screen is displayed. |  |
| 2 | Go to the financial statement planning model | From the main menu, choose Files. Search for and open SAP_FI_IFP_IM_FinancialStatement | The model SAP_FI_IFP_IM_FinancialStatement is displayed |  |
| 3 | Go to the Company Code dimension | Choose SAP_ALL_COMPANY_CODE. | The public dimension is displayed. |  |
| 4 | Choose the Data Management tab | Choose the Data Management tab. | The Data Management tab is displayed |  |
| 5 | Refresh the Job | Choose the Refresh button at the right-hand side of the job. | The system displays a message stating number of rows imported. |  |
| 6 | Repeat | Repeat steps 3 to 5 for the following dimensions:SAP_FI_IFP_GLACCOUNTSAP_ALL_FUNCTIONALAREASAP_ALL_PROFITCENTERSAP_ALL_TRADINGPARTNER | The system displays a message stating number of rows imported. |  |
| 7 | Go to the financial statement model | From the main menu, choose Files. Search for and open SAP_FI_IFP_IM_FinancialStatement | The model SAP_FI_IFP_IM_FinancialStatement is displayed |  |
| 8 | Choose the Data Management tab | Choose the Data Management tab. | The Data Management tab is displayed |  |
| 9 | Refresh Import Jobs to Load Transaction Data | Under Import Jobs, choose Refresh at the right-hand side of the job. | The system displays a message stating number of rows imported. |  |

##### Export Plan Data to SAP S/4HANA

Use

You can now export the plan and budget data that you’ve created in the steps before to SAP S/4HANA.

For more information on the export to SAP S/4HANA functionality, see the [documentation](https://help.sap.com/docs/SAP_S4HANA_CLOUD/1cbcff7ccd35405ab445b223c1ab1588/15447e5bda934be28f3b16cfb456fb23.html).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Model Page | From the main menu, choose Files. | The Files page is displayed. |  |
| 2 | Access the Model | Find and display the model SAP_FI_IFP_IM_FinancialStatement. | The Model SAP_FI_IFP_IM_FinancialStatement is displayed. |  |
| 3 | Open Data Management | Choose Data Management. | Import and Export jobs are displayed. |  |
| 4 | Create new export | On the Export Jobs section, choose Export Data to SAP S/4HANA. | Follow the wizard as described in the documentation. |  |

#### Add-On Package for IFP

##### Load Demand Data from SAP IBP

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure only is necessary for the SAP IBP integration test, not for the stand-alone test with sample data.

|  |
| --- |
| Caution This add-on package is not applicable to SAP S/4HANA Cloud Public Edition source systems. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator | The Home - Welcome to SAP Analytics Cloud screen is displayed. |  |
| 2 | Go to the Profitability Model | From the main menu, choose Files .Search for and open SAP_FI_IFP_IM_Profitability. | The model SAP_FI_IFP_IM_Profitability is displayed. |  |
| 3 | Data Management | Choose the Data Management tab. |  |  |
| 4 | Refresh the Job for Loading IBP Demand | Under Import Jobs, choose Refresh at the right-hand side of the job [IBP Demand] UNIPA. | The system displays a message stating number of rows imported. |  |

##### Load Master and Actual Data from SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This procedure only is necessary for the SAP S/4HANA Cloud Public Edition integration test, not for the stand-alone test with sample data.

|  |
| --- |
| Caution This add-on package is not applicable for SAP S/4HANA Cloud Public Edition source systems. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator | The Home - Welcome to SAP Analytics Cloud screen is displayed. |  |
| 2 | Plant Dimension | From the main menu, choose Modeler > Dimensions .Search for and open SAP_ALL_PLANT. | The public dimension is displayed. |  |
| 3 | Data Management | Choose the Data Management tab. |  |  |
| 4 | Refresh the Job | Choose the Refresh button at the right-hand side of the job. | The system displays a message stating number of rows imported. |  |
| 5 | Repeat | Repeat steps 2 to 4 for the following dimensions:SAP_ALL_PRODUCTSAP_ALL_PROFITCENTER | The system displays a message stating number of rows imported. |  |
| 6 | PlantProduct Model | From the main menu, choose Files. Search for and open SAP_FI_IFP_IM_Addon_PlantProduct. | The SAP_FI_IFP_IM_Addon_PlantProduct model is displayed. |  |
| 7 | Data Management | Choose the Data Management tab. |  |  |
| 8 | Refresh the Job for Loading Actual Data | Under Import Jobs, choose Refresh at the right-hand side of the job [DRIVER] A_ProductPlant. | The system displays a message stating number of rows imported. |  |

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
> Flagged while digesting this document, not verified: The final section 'Load Master and Actual Data from SAP S/4HANA Cloud Public Edition' carries a Caution that the add-on package is not applicable for SAP S/4HANA Cloud Public Edition source systems, contradicting its own title and purpose.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/test-script-financial-plan-data-upload-from-file-1hb-ae-sap-s-4hana-cl]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/4RC_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 132,380 chars in the whole document
