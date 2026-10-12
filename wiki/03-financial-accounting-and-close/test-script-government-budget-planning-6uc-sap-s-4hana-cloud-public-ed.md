---
id: 03-financial-accounting-and-close/test-script-government-budget-planning-6uc-sap-s-4hana-cloud-public-ed
title: "Test Script: Government Budget Planning (6UC) - SAP S/4HANA Cloud Public Edition (6UC_S4CLD2608_BPD_EN_XX)"
description: "SAP test script for scope item 6UC Government Budget Planning in SAP Analytics Cloud: data load, expense/revenue/project planning, reports, analytics (2608)."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/government-budget-planning-and-management]
aliases: [6UC_S4CLD2608_BPD_EN_XX]
keywords: [Government Budget Planning and Budget Management, government budget planning, operational expense planning, operational revenue planning, project planning, test procedures, backend data load, planning models, sample data creation, copy data action]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6UC_S4CLD2608_BPD_EN_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1189
topic: 03-financial-accounting-and-close/government-budget-planning-and-management
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Government Budget Planning (6UC) - SAP S/4HANA Cloud Public Edition (6UC_S4CLD2608_BPD_EN_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6UC_S4CLD2608_BPD_EN_XX.docx`, extracted with `mammoth`. Grouped under **Government Budget Planning and Budget Management** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Government Budget Planning (6UC) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232841816)

[2 Prerequisites 4](#_Toc232841817)

[2.1 System Access 4](#_Toc232841818)

[2.2 Roles 4](#_Toc232841819)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232841820)

[2.4 Additional Manual Configuration 5](#_Toc232841821)

[2.5 Business Conditions 5](#_Toc232841822)

[3 Overview Table 6](#_Toc232841823)

[4 Test Procedures 8](#_Toc232841824)

[4.1 Integration with SAP S/4HANA Cloud Public Edition 8](#_Toc232841825)

[4.1.1 Operational Expense Planning 8](#_Toc232841826)

[4.1.1.1 Load Master and Actual Data from SAP S/4HANA Cloud Public Edition 8](#_Toc232841827)

[4.1.2 Operational Revenue Planning 9](#_Toc232841828)

[4.1.2.1 Load Master and Actual Data from SAP S/4HANA Cloud Public Edition 9](#_Toc232841829)

[4.1.3 Project Planning 10](#_Toc232841830)

[4.1.3.1 Load Master and Actual Data from SAP S/4HANA Cloud Public Edition 10](#_Toc232841831)

[4.2 Operational Expense Planning 12](#_Toc232841832)

[4.2.1 Perform Operational Expense Admin Tasks 12](#_Toc232841833)

[4.2.2 Perform Operational Expense Planning 13](#_Toc232841834)

[4.2.3 Review Operational Expense Reports 14](#_Toc232841835)

[4.2.4 Review Operational Expense Analytics 15](#_Toc232841836)

[4.3 Operational Revenue Planning 16](#_Toc232841837)

[4.3.1 Perform Operational Revenue Admin Tasks 16](#_Toc232841838)

[4.3.2 Perform Operational Revenue Planning 17](#_Toc232841839)

[4.3.3 Review Operational Revenue Reports 19](#_Toc232841840)

[4.3.4 Review Operational Revenue Analytics 19](#_Toc232841841)

[4.4 Project Planning 21](#_Toc232841842)

[4.4.1 Perform Project Admin Tasks 21](#_Toc232841843)

[4.4.2 Perform Project Planning 22](#_Toc232841844)

[4.4.3 Review Project Reports 23](#_Toc232841845)

[4.4.4 Review Project Analytics 23](#_Toc232841846)

## Purpose

Overview

This process supports budget planning and analytics as a periodic activity, by setting expectations for the budgeting process of the upcoming fiscal years or periods.

Different planning activities would help to set operational targets for multiple elements of an organizational entity such as expenses, revenue, projects, and it includes:

- Operational Expense Planning to determine the expenses planned.
- Operational Revenue Planning to determine the incoming revenues.
- Project Planning for planning any implementation projects.

In general here, two aspects need to be tested:

- Backend Integration: data load from backend data sources into models in accordance with the documentation
- UI - Correctness of charts and calculations, navigation and adherence to the style guide

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

### System Access

| System | Details |
| --- | --- |
| System | Accessible from SAP Analytics Cloud. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Planning Modeler | Modeler | Modeling and Viewing Privileges | N/A | N/A |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data for your company have been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents funds, cost centers, projects and budget accounts, for example according to the operational focus of your company.

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Company Code | <company code, for example, 1710> |  |  |

You can find general information about creating master data objects in the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data) :

| MDS | Description |
| --- | --- |
| BNE | Create Supplier Master - MDS |
| BNG | Create G/L Account and Cost Element - MDS |
| BNH | Create Profit Center - MDS |
| 47C | Create Fund - MDS |
| 47D | Create Budget Period - MDS |
| 47E | Create Functional Area - MDS |

### Additional Manual Configuration

Before you can test this scope item, you must have completed the additional configuration steps that are described in the Set-Up Instructions for this scope item. These configuration steps are specific for your implementation and include mandatory settings that are not delivered by SAP and must be created by you. For more information, follow the link to the document:

[Link to Set-Up Instructions](https://help.sap.com/docs/SAP_S4HANA_BEST_PRACTICES/47b005e690a1b2bad59f332361976a4c)

### Business Conditions

Before you can test this scope item, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 3QE – Government Budget Management (US/CA) | The steps executed by the budget specialist to consume budget. |

## Overview Table

This scope item consists of several process steps provided in the following table.

All steps in this test script are performed in SAP Analytics Cloud.

Table 1: Operational Expense Planning

| Process Step | Business Role | Model |
| --- | --- | --- |
| Perform Operational Expense Planning | Planning Modeler | SAP_PSM_BP_IM_OPERATIONALEXPENSEPLANNING |

Table 2: Operational Revenue Planning

| Process Step | Business Role | Model |
| --- | --- | --- |
| Perform Operational Revenue Planning | Planning Modeler | SAP_PSM_BP_IM_OPERATIONALREVENUEPLANNING |

Table 3: Project Planning

| Process Step | Business Role | Model |
| --- | --- | --- |
| Perform Project Planning | Planning Modeler | SAP_PSM_BP_IM_PROJECTPLANNING |

Table 4: Integration with SAP S/4HANA Cloud Public Edition

| Process Step | Business Role | Transaction/App/Story |
| --- | --- | --- |
| Operational Expense Planning |  |  |
| Load Master Data from SAP S/4HANA Cloud Public Edition | Planning Modeler | SAP_ALL_FUNDSAP_ALL_COSTCENTERSAP_ALL_BUDGETPERIODSAP_ALL_FUNCTIONALAREASAP_ALL_BUDGETACCOUNTSAP_ALL_PROFITCENTER |
| Load Budget Data from SAP S/4HANA Cloud Public Edition | Planning Modeler | A_FinPlanningEntryItem |
| Load Actual Data from SAP S/4HANA Cloud Public Edition | Planning Modeler | PubSecCmtmtActlItem |
| Operational Revenue Planning |  |  |
| Load Master Data from SAP S/4HANA Cloud Public Edition | Planning Modeler | SAP_ALL_FUNDSAP_ALL_COSTCENTERSAP_ALL_BUDGETPERIODSAP_ALL_FUNCTIONALAREASAP_ALL_BUDGETACCOUNTSAP_ALL_PROFITCENTER |
| Load Budget Data from SAP S/4HANA Cloud Public Edition | Planning Modeler | A_FinPlanningEntryItem |
| Load Actual Data from SAP S/4HANA Cloud Public Edition | Planning Modeler | PubSecCmtmtActlItem |
| Project Planning |  |  |
| Load Master Data from SAP S/4HANA Cloud Public Edition | Planning Modeler | SAP_ALL_FUNDSAP_ALL_COSTCENTERSAP_ALL_BUDGETPERIODSAP_ALL_FUNCTIONALAREASAP_ALL_BUDGETACCOUNTSAP_ALL_PROFITCENTERSAP_ALL_PROJECT_WBSELEMENTSAP_ALL_GRANT |
| Load Budget Data from SAP S/4HANA Cloud Public Edition | Planning Modeler | A_FinPlanningEntryItem |
| Load Actual Data from SAP S/4HANA Cloud Public Edition | Planning Modeler | PubSecCmtmtActlItem |

## Test Procedures

### Integration with SAP S/4HANA Cloud Public Edition

#### Operational Expense Planning

##### Load Master and Actual Data from SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This procedure is only necessary for the SAP S/4HANA Cloud Public Edition integration test, and not for the standalone test with sample data.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator. | The Home - Welcome to SAP Analytics Cloud screen appears. |  |
| 2 | Operational Expense Planning Model | From the main menu, choose Browse > Files . Search for and open SAP_PSM_BP_IM_OPERATIONALEXPENSEPLANNING | The model SAP_PSM_BP_IM_OPERATIONALEXPENSEPLANNING appears. |  |
| 3 | Fund Dimension | Choose SAP_ALL_FUND |  |  |
| 4 | Data Management | Choose the Data Management tab. | The Data Management tab appears. |  |
| 5 | Refresh the Job | Choosehe Refresh to the right of the job. | The system displays a message showing the number of rows imported. |  |
| 6 | Repeat | Repeat steps 3 to 5 for the following dimensions:SAP_ALL_BUDGETPERIOD, SAP_ALL_FUNCTIONALAREA, SAP_ALL_BUDGETACCOUNT, SAP_ALL_PROFITCENTER, SAP_ALL_COSTCENTER | The system displays a message showing the number of rows imported. |  |
| 7 | Data Management | Choose the Data Management tab. | The Data Management tab appears. |  |
| 8 | Refresh the Job to Load Budget Data | Under Import Jobs, choose Refresh to the right of the job [Budget] A_FinPlanningEntryItemQuery | The system displays a message showing the number of rows imported. |  |
| 9 | Refresh the Job to Load Actual Data | Under Import Jobs, choose Refresh to the right of the job [Actuals] PubSecCmtmtActlItemQuery | The system displays a message showing the number of rows imported. |  |

#### Operational Revenue Planning

##### Load Master and Actual Data from SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This procedure is only necessary for the SAP S/4HANA Cloud Public Edition integration test, and not for the standalone test with sample data.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator. | The Home - Welcome to SAP Analytics Cloud screen appears. |  |
| 2 | Operational Revenue Planning Model | From the main menu, choose Browse > Files . Search for and open SAP_PSM_BP_IM_OPERATIONALREVENUEPLANNING | The model SAP_PSM_BP_IM_OPERATIONALREVENUEPLANNING appears. |  |
| 3 | Fund Dimension | Choose SAP_ALL_FUND |  |  |
| 4 | Data Management | Choose the Data Management tab. | The Data Management tab appears. |  |
| 5 | Refresh the Job | Choose Refresh to the right of the job. | The system displays a message showing the number of rows imported. |  |
| 6 | Repeat | Repeat steps 3 to 5 for the following dimensions:SAP_ALL_BUDGETPERIOD, SAP_ALL_FUNCTIONALAREA, SAP_ALL_BUDGETACCOUNT, SAP_ALL_PROFITCENTER, SAP_ALL_COSTCENTER | The system displays a message showing the number of rows imported. |  |
| 7 | Data Management | Choose the Data Management tab. | The Data Management tab is displayed. |  |
| 8 | Refresh the Job to Load Budget Data | Under Import Jobs, choose Refresh to the right of the job [Budget] A_FinPlanningEntryItemQuery | The system displays a message showing the number of rows imported. |  |
| 9 | Refresh the Job to Load Actual Data | Under Import Jobs, choose Refresh to the right of the job [Actuals] PubSecCmtmtActlItemQuery | The system displays a message showing the number of rows imported. |  |

#### Project Planning

##### Load Master and Actual Data from SAP S/4HANA Cloud Public Edition

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

This procedure is only necessary for the SAP S/4HANA Cloud Public Edition integration test, and not for the standalone test with sample data.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Open SAP Analytics Cloud | Use the URL and credentials provided by the system administrator. | The Home - Welcome to SAP Analytics Cloud screen appears. |  |
| 2 | Project Planning Model | From the main menu, choose Browse > Files . Search for and open SAP_PSM_BP_IM_PROJECTPLANNING | The model SAP_PSM_BP_IM_PROJECTPLANNING appears. |  |
| 3 | Fund Dimension | Choose SAP_ALL_FUND |  |  |
| 4 | Data Management | Choose the Data Management tab. | The Data Management tab appears. |  |
| 5 | Refresh the Job | Choose Refresh to the right of the job. | The system displays a message showing the number of rows imported. |  |
| 6 | Repeat | Repeat steps 3 to 5 for the following dimensions:SAP_ALL_BUDGETPERIOD, SAP_ALL_FUNCTIONALAREA, SAP_ALL_BUDGETACCOUNT, SAP_ALL_PROFITCENTER, SAP_ALL_COSTCENTER, SAP_ALL_PROJECT_WBSELEMENT | The system displays a message showing the number of rows imported. |  |
| 7 | Data Management | Choose the Data Management tab. | The Data Management tab appears. |  |
| 8 | Refresh the Job to Load Budget Data | Under Import Jobs, choose Refresh to the right of the job [Budget] A_FinPlanningEntryItemQuery | The system displays a message showing the number of rows imported. |  |
| 9 | Refresh the Job to Load Actual Revenue Data | Under Import Jobs, choose Refresh to the right of the job [Actuals Revenue] PubSecCmtmtActlItemQuery | The system displays a message showing the number of rows imported. |  |
| 10 | Refresh the Job to Load Actual Expense Data | Under Import Jobs, choose Refresh to the right of the job [Actuals Expense] PubSecCmtmtActlItemQuery | The system displays a message showing the number of rows imported. |  |

### Operational Expense Planning

#### Perform Operational Expense Admin Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

|  |
| --- |
| Note Create sample data (steps 4 and 6) in this procedure is only necessary for the standalone test with sample data, and not for the SAP S/4HANA Cloud Public Edition integration test. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Home Page | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the Home Page for Operational Expense Planning | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home appears. By default, Operational Expense Planning appears |  |
| 3 | Access the Admin Story | Click on the Create Actual Data tile to navigate to the Admin storyto create sample data for actuals | The story SAP_PSM_BP_Operational_Expense_Admin appears with the Actual tab selected |  |
| 4 | Create Actual Sample Data | On the Actual tab, use the data action Create Actual to create the sample data for actuals.If necessary, first delete the existing data using the other data action Clear Data. | Actual sample data is displayed. |  |
| 5 | Save Actuals Data | You can either choose Publish Data or leave the story. |  |  |
| 6 | Create Budget Sample Data | On the Budget tab, use the data actions Create Budget to Create Sample Data for Budget.If necessary, first delete the existing data using the other data action Clear Data. | Plan sample data is displayed. |  |
| 7 | Save Budget Data | You can either choose Publish Data or leave the story. |  |  |

#### Perform Operational Expense Planning

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
| 1 | Select File | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the home page | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home appears. By default Operational Expense Planning appears with the relevant tiles. |  |
| 3 | Access the Planning Story | Click on Plan Expense under Planning | The story SAP_PSM_BP_Operational_Expense_Planning appears with the Expense Planning tab selected. |  |
| 4 | Populate Budget Data by copying data | On the Expense Planning tab, use the data action Copy DataSelect the source version as BudgetSelect the target version as PlanEnter a growth factor (In percentage)Enter From Budget Period / Fiscal year (Prev. FY)Enter To Budget Period / Fiscal Year (Curr. FY) | The Copy Data dialog box appears.Budget data is copied to the Expense Plan planning form. |  |
| 5 | Populate Actual Data by copying data | On the Expense Planning tab, use the data action Copy DataSelect source version as ActualSelect target version as PlanEnter growth factor (In percentage)Enter From Budget Period / Fiscal year (Prev. FY)Enter To Budget Period / Fiscal Year (Curr. FY) | The Copy Data dialog box appears.Actual data is copied to the Expense Plan planning form. |  |
| 6 | Provide plan data values | On the Expense Plan table, Provide the plan data values. | Plan data is maintained for the fund, cost center and budget account combination |  |
| 7 | Publish Data | Publish Plan | Versions are published to the model |  |

#### Review Operational Expense Reports

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
| 1 | Access the Homepage | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the Homepage | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home is displayed. By default Operational Expense Planning appears with the relevant tiles. |  |
| 3 | Access the Reporting Planned Expense Data Story | Click on Expense Planning Report under Reports | The story SAP_PSM_BP_Operational_Expense_Planning appears with the Expense Planning Report tab selected. |  |
| 4 | Review Plan Data | Review the Expense Plan data planned for operational expenses | Expense plan data is displayed in a read-only format along with the total plan amount KPI, which can be filtered based on the company code, profit center, fund, cost center and budget account |  |

#### Review Operational Expense Analytics

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
| 1 | Access the Homepage | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the Homepage | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home appears. By default Operational Expense Planning appears with the relevant tiles. |  |
| 3 | Access the Operational Expense Planning Analytics Story | Click on Analyze Budget under Analytics | The story SAP_PSM_BP_Operational_Expense_Analytics appears with the Budget vs Actual tab selected. |  |
| 3 | Budget vs Actual | The total budget, actual amount and budget and actual amount based on each fiscal year are displayed. The budget and actual amount is displayed in terms of the budget account, cost center, fund and profit center. | Analyze the budget against the actual amount. |  |
| 4 | Choose the Budget vs Plan tab | The total budget, plan amount and budget and plan amount based on each fiscal year are displayed. The budget and plan amount is displayed in terms of the budget account, cost center, fund and profit center. | Analyze the budget against the plan amount. |  |
| 5 | Adjust Story Filters | Adjust the story filters for Company Code, Profit Center, Fund, Cost Center and Budget Account as required. | Displayed data is filtered. |  |

### Operational Revenue Planning

#### Perform Operational Revenue Admin Tasks

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Procedure

|  |
| --- |
| Note Create sample data (step 5 and 7) in this procedure is only required for the standalone test with sample data, and not for the SAP S/4HANA Cloud Public Edition integration test. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Homepage | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the Homepage | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home appears. By default Operational Expense Planning appears. |  |
| 3 | Access the Homepage for Operational Revenue Planning | Click on Operational Revenue Planning | The homepage for Operational Revenue Planning appears with the relevant tiles. |  |
| 4 | Access the Admin Story | Click on 'Create Actual Data' tile to navigate to the Admin story to create sample data for actuals | The story SAP_PSM_BP_Operational_Revenue_Admin appears with the Actual tab selected |  |
| 5 | Create Actual Sample Data | On the Actual tab, use the data action Create Actual to create the sample data for actuals.If necessary, first delete the existing data using the other data action Clear Data. | Actual sample data is displayed. |  |
| 6 | Save Actuals Data | You can either choose Publish Data or leave the story. |  |  |
| 7 | Create Budget Sample Data | On the Budget tab, use the data actions Create Budget to create Sample data for Budget.If necessary, first delete the existing data using the other data action Clear Data. | Plan sample data is displayed. |  |
| 8 | Save Plan Data | You can either choose Publish Data or leave the story. |  |  |

#### Perform Operational Revenue Planning

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
| 1 | Access the Homepage | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the Homepage | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home appears. By default Operational Expense Planning appears. |  |
| 3 | Access the Homepage for Operational Revenue Planning | Click on Operational Revenue Planning | The homepage for Operational Revenue Planning appears with the relevant tiles. |  |
| 4 | Access the Planning Story | Click on Plan Revenue under Planning | The story SAP_PSM_BP_Operational_Revenue_Planning appears with the Revenue Planning tab selected. |  |
| 5 | Perform the Copy Data Data Action to Populate Budget Data | On the Revenue Planning tab, use the data action Copy DataSelect the from version as BudgetSelect the target version as PlanEnter the growth factor (as a percentage)Enter the from budget period / fiscal year (Prev. FY)Enter the to budget period / fiscal year (Curr. FY) | The Copy Data dialog box appears.Budget data is copied to the Revenue Plan planning form |  |
| 6 | Perform the Copy Data Data Action to Populate Actual Data | On the Revenue Planning tab, use the data action Copy DataSelect the from version as ActualSelect target version as PlanEnter the growth factor (as a percentage)Enter the from budget period / fiscal year (Prev. FY)Enter the to budget period / fiscal year (Curr. FY) | The Copy Data dialog box appears.Actual data is copied to the Revenue Plan planning form |  |
| 7 | Provide Plan Data Values | On the Revenue Plan table, Provide the plan data values. | Plan data is maintained for the fund, cost center and budget account combination |  |
| 8 | Publish Data | Publish Plan | The version is published to the model |  |

#### Review Operational Revenue Reports

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
| 1 | Access the Homepage | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the Homepage | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home appears. By default Operational Expense Planning appears with the relevant tiles. |  |
| 3 | Access the Homepage for Operational Revenue Planning | Click on the Operational Revenue Planning tab | The homepage for Operational Revenue Planning appears with the relevant tiles. |  |
| 4 | Access the Reporting Planned Revenue Data Story | Click on Revenue Planning Report under Reports | The story SAP_PSM_BP_Operational_Revenue_Analytics appears with Budget vs Actual tab selected. |  |
| 5 | Review Plan Data | Review Revenue Plan data planned for operational revenue | Revenue plan data is displayed in a read-only format along with the total plan amount KPI which can be filtered based on the company code, profit center, fund, cost center and budget account |  |

#### Review Operational Revenue Analytics

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
| 1 | Access the Homepage | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the Homepage | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home appears. By default Operational Expense Planning appears with the relevant tiles. |  |
| 3 | Access the Homepage for Operational Revenue Planning | Click on Operational Revenue Planning tab | The homepage for Operational Revenue Planning appears with the relevant tiles. |  |
| 4 | Access the Operational Revenue Planning Analytics Story | Click on Analyze Budget under Analytics | The story SAP_PSM_BP_Operational_Revenue_Analytics appears with Budget vs Actual tab selected. |  |
| 5 | Budget vs Actual tab | The total budget, actual amount and budget and actual amount based on each fiscal year are displayed. The budget and actual amount is displayed in terms of the budget account, cost center, fund and profit center. | Analyze the budget against the actual amount. |  |
| 6 | Choose the Budget vs Plan tab | The total budget, plan amount and budget and plan amount based on each fiscal year are displayed. The budget and plan amount is displayed in terms of the budget account, cost center, fund and profit center. | Analyze the budget against the plan amount. |  |
| 7 | Adjust Story Filters | Adjust story filters for Company Code, Profit Center, Fund, Cost Center and Budget Account as required. | Displayed data is filtered. |  |

### Project Planning

#### Perform Project Admin Tasks

Procedure

|  |
| --- |
| Note Create sample data (steps 5 and 7) in this procedure is only required for the standalone test with sample data, and not for the SAP S/4HANA Cloud Public Edition integration test. |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Homepage | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the Homepage | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home appears. By default Operational Expense Planning appears. |  |
| 3 | Access the Homepage for Project Planning | Click on Project Planning | The homepage for Project Planning appears with the relevant tiles. |  |
| 4 | Access the Admin Story | Click on Create Actual Data tile to navigate to the Admin story to create sample data for actuals | The story SAP_PSM_BP_Project_Admin appears with the Actual tab selected |  |
| 5 | Create Actual Sample Data | On the Actual tab, use the data action Create Actual to create the sample data for actuals.If necessary, first delete the existing data using the other data action Clear Data. | Actual sample data is displayed. |  |
| 6 | Save Actuals Data | You can either choose Publish Data or leave the story. |  |  |
| 7 | Create Budget Sample Data | On the Budget tab, use the data action Create Budget to create Sample data for Budget.If necessary, first delete the existing data using the other data action Clear Data. | Budget sample data is displayed. |  |
| 8 | Save Budget Data | You can either choose Publish Data or leave the story. |  |  |

#### Perform Project Planning

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Access the Homepage | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the Homepage | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home appears. By default Operational Expense Planning appears. |  |
| 3 | Access the Homepage for Project Planning | Click on Project Planning | The homepage for Project Planning appears with the relevant tiles. |  |
| 4 | Access the Planning Story | Click on Plan Project under Planning | The story SAP_PSM_BP_Project_Planning appears with the Project Planning tab selected. |  |
| 5 | Perform the Copy Data Data Action to Populate Budget Data | On the Project Planning tab, use the data action Copy DataSelect the source version as BudgetSelect the target version as PlanEnter the growth factor (In percentage)Enter the from budget period / fiscal year (Prev. FY)Enter the to budget period / fiscal year (Curr. FY) | The Copy Data dialog box appears.Budget data is copied to the Project Plan planning form |  |
| 6 | Perform the Copy Data Data Action to Populate Actual Data | On the Project Planning tab, use the data action Copy DataSelect the source version as ActualSelect the target version as PlanEnter the growth factor (as a percentage)Enter the from budget period / fiscal year (prev. FY)Enter the to budget period / fiscal year (Curr. FY) | The Copy Data dialog box appears.Actual data is copied to the Project Plan planning form |  |
| 7 | Provide Plan Data Values | On the Project Plan table, Provide the plan data values. | Plan data is maintained for the fund, WBS element and budget account combination |  |
| 8 | Publish Data | Publish Plan | The version is published to the model |  |

#### Review Project Reports

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
| 1 | Access the Homepage | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the Homepage | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home appears. By default Operational Expense Planning appears with the relevant tiles. |  |
| 3 | Access the Homepage for Project Planning | Click on the Project Planning tab | The homepage for Project Planning appears with the relevant tiles. |  |
| 4 | Access the Reporting Planned Project Data Story | Click on Project Planning Report under Reports | The story SAP_PSM_BP_Project_Planning appears with the Project Planning Report tab selected. |  |
| 5 | Review Plan Data | Review Project Plan data is planned for projects | Project plan data is displayed in a read-only format along with the total plan amount KPI, which can be filtered based on the company code, profit center, fund, WBS element, cost center and budget account |  |

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
| 1 | Access the Homepage | From the main menu, choose Browse > Files. | The Files page appears. |  |
| 2 | Access the Homepage | Find and display the story SAP_PSM_BP_Planning_Home. | The story SAP_PSM_BP_Planning_Home appears. By default Operational Expense Planning appears with the relevant tiles. |  |
| 3 | Access the Homepage for Project Planning | Click on the Project Planning tab | The homepage for Project Planning appears with the relevant tiles. |  |
| 4 | Access the Project Planning Analytics Story | Click on Analyze Budget under Analytics | The story SAP_PSM_BP_Project_Analytics appears with Budget vs Actual tab selected. |  |
| 5 | Budget vs Actual | The total budget, actual amount and budget and actual amount is displayed for each fiscal year. The budget and actual amount is displayed in terms of the budget account, WBS element, fund and profit center. | Analyze the budget against the actual amount. |  |
| 6 | Choose the Budget vs Plan tab | The total budget, plan amount and budget and budget and plan amount is displayed for each fiscal year. The budget and plan amount is displayed in terms of the budget account, WBS element, fund and profit center. | Analyze the budget against the plan amount. |  |
| 7 | Adjust Story Filters | Adjust the story filters for Company Code, Profit Center, Fund, WBS Element and Budget Account as required. | The displayed data is filtered. |  |

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
> Flagged while digesting this document, not verified: The overview table lists SAP_ALL_GRANT among the Project Planning master data loads, but the Project Planning load procedure (step 6) repeats only SAP_ALL_BUDGETPERIOD, FUNCTIONALAREA, BUDGETACCOUNT, PROFITCENTER, COSTCENTER and PROJECT_WBSELEMENT, with no SAP_ALL_GRANT step.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[03-financial-accounting-and-close/government-budget-management-6yu-test-script-sap-s-4hana-cloud-public]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/6UC_S4CLD2608_BPD_EN_XX.docx` — full document · extracted with `mammoth` · 39,019 chars in the whole document
