---
id: 06-management-accounting/test-script-predictive-commitments-management-2i3-ae-sap-s-4hana-cloud
title: "Test Script: Predictive Commitments Management (2I3_AE) - SAP S/4HANA Cloud Public Edition (2I3_S4CLD2608_BPD_EN_AE)"
description: "SAP test script for scope item 2I3 Predictive Commitments Management (AE): commitment reporting, cost center and project budgeting, with prerequisites and step tables."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/budgets-and-commitments]
aliases: [2I3_S4CLD2608_BPD_EN_AE]
keywords: [Budgets and Commitment Management, commitment management, cost center budgeting, project budget report, budget availability control, purchase order commitments, budget transfer, financial plan import, currency exchange rates, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2I3_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-827
topic: 06-management-accounting/budgets-and-commitments
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Predictive Commitments Management (2I3_AE) - SAP S/4HANA Cloud Public Edition (2I3_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2I3_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Budgets and Commitment Management** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 02-08-26 |
| --- | --- |
|  | Predictive Commitments Management (2I3_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc237128597)

[2 Prerequisites 4](#_Toc237128598)

[2.1 System Access 4](#_Toc237128599)

[2.2 Roles 4](#_Toc237128600)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc237128601)

[2.4 Business Conditions 5](#_Toc237128602)

[2.5 Preliminary Steps 6](#_Toc237128603)

[2.5.1 User Settings - Set Controlling Area 6](#_Toc237128604)

[2.5.2 Maintain Currency Exchange Rate to Global Currency 6](#_Toc237128605)

[2.5.3 Optional: Updating Cost Center Budget Profiles (Only Required When Using Cost Center Budget Functionality) 7](#_Toc237128606)

[2.5.4 Optional: Updating Project Budget Profiles (Only Required When Using Project Budget Functionality) 9](#_Toc237128607)

[3 Overview Table 11](#_Toc237128608)

[4 Test Procedures 13](#_Toc237128609)

[4.1 Analytics 13](#_Toc237128610)

[4.1.1 Commitment Management by Cost Center 13](#_Toc237128611)

[4.1.2 Commitments by Cost Center 14](#_Toc237128612)

[4.1.3 Monitor Projects via Project Budget Report 15](#_Toc237128613)

[4.2 OPTIONAL: Commitment Management and Cost Center Budgeting 17](#_Toc237128614)

[4.2.1 Commitment Management Cost Centers Actual Data Reporting 17](#_Toc237128615)

[4.2.1.1 Exclude Cost Center Data for Commitment Management 17](#_Toc237128616)

[4.2.1.2 Create Purchase Order 18](#_Toc237128617)

[4.2.1.3 Commitment Management by Cost Center 20](#_Toc237128618)

[4.2.2 Cost Center Budgeting 20](#_Toc237128619)

[4.2.2.1 Set Cost Center Master Budgeting Parameters 21](#_Toc237128620)

[4.2.2.2 Upload Financial Data 22](#_Toc237128621)

[4.2.2.2.1 Template for File Upload 22](#_Toc237128622)

[4.2.2.2.2 Import Financial Data 24](#_Toc237128623)

[4.2.2.3 Create Purchase Order 25](#_Toc237128624)

[4.2.2.4 View Budget by Cost Center 27](#_Toc237128625)

[4.2.2.5 Cost Center Review Booklet with Budget 27](#_Toc237128626)

[4.2.2.6 Transfer Cost Center Budgets 28](#_Toc237128627)

[5 Appendix 31](#_Toc237128628)

[5.1 Process Integration 31](#_Toc237128629)

[5.1.1 Preceding Processes 31](#_Toc237128630)

[5.1.2 Succeeding Processes 31](#_Toc237128631)

## Purpose

Overview

Commitment management is part of the cost monitoring process. Commitment items for projects are triggered by material purchase requisitions and purchase orders and are reduced by various business transactions such as goods receipt. A project cost report shows commitments versus plan and actual costs.

If this scope item is activated and the prerequisite scope item of Project Financial Control (1NT) is performed, the Project Financial Controller can monitor purchase order commitments against plan and actual costs in a report.

If the scope item is activated, and the prerequisite scope item of Overhead Cost Accounting (J54) is performed, the Cost Accountant-Overhead can monitor purchase order commitments by cost center and cost element in a report.

This document provides a detailed procedure for testing this scope item after solution activation, reflecting the predefined scope of the solution. Each process step, report, or item is covered in its own section, providing the system interactions (test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly. Project-specific steps must be added.

|  |
| --- |
| Note Values in this test script (decimal notation, date formats, and so on) are presented in U.S. standard notation. If your test system is set up to use a different notation, enter values as appropriate. |

## Prerequisites

This section summarizes all prerequisites needed to conduct the test in terms of system, users, master data, organizational data, and other test data and business conditions.

### System Access

The test should be conducted with the following system:

| System | Details |
| --- | --- |
| System | Accessible via the SAP Fiori launchpad. Your system administrator provides you with the URL to access the various apps assigned to your role. |

### Roles

Create business roles using the following business role templates delivered by SAP and assign them to your individual test users.

Alternatively, if available, you can use the following spaces delivered by SAP. You create a space with pages containing predefined essential apps and assign it to the business role. You then assign this business role to your individual users.

For more information, refer to How to Create a Business Role from a Template in the [product assistance](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) for SAP S/4HANA Cloud Public Edition.

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Project Financial Controller | SAP_BR_PROJ_FIN_CONTROLLER | Project Control - Finance | SAP_BR_PROJ_FIN_CONTROLLER |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Controlling Area | A000 | A000 |  |
| Company Code | 3310 | 3310 |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| 1NT - Project Control – Finance orJ54 - Overhead Cost Accounting | At least one of these business conditions must be executed for this test script. |

### Preliminary Steps

#### User Settings - Set Controlling Area

Purpose

The controlling area must be set before you carry out the first steps in controlling.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Choose User Preferences | Choose the user icon on the top right corner of the screen, and choose Settings.Choose Default Values. | The Default Values dialog box displays. |  |
| 3 | Enter Data | On the CO Area field,enter the following value: A000.Choose Save. | Controlling area A000 is set for your user. |  |

#### Maintain Currency Exchange Rate to Global Currency

Use

In this activity, you can maintain currency exchange rate to global currency.

You can maintain currency exchange rates for the following:

- Primary Posting: From company code currencies to global currency (M rate)
- Secondary Posting: From global currency to company code currencies (P rate)

The M and P rates must be entered for the controlling area and all company codes' currency combinations. Note that any additional company currencies must also be maintained via the Currency Exchange Rate app.

Prerequisite

Ensure that exchange rates are maintained for both M and P rates for the controlling area and all company codes' currency combinations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Currency Exchange Rates (F3616). | The Currency Exchange Rates view displays. |  |
| 3 | Add an Exchange Rate Entry | Choose Create. | The right pane expands to show the entry fields. |  |
| 4 | Enter Data | Make the following entries and choose Create:Company Code: 3310Fiscal Year: <current fiscal year> | You entered a new exchange rate. |  |

|  |
| --- |
| Note Currency exchange rates can also be uploaded via the Import Foreign Exchange Rates (F2092). For more details, see the scope item Accounting and Financial Close (J58). |

#### Optional: Updating Cost Center Budget Profiles (Only Required When Using Cost Center Budget Functionality)

Purpose

- The default content comes with budget profile CC001- Cost Center Budget and mapped to sample groups for travel cost and material. The customer must either adopt this profile or create new as per your requirement.

|  |
| --- |
| Caution Adjustments to the budget profile CC001 has to be adapted for your specific company requirements prior to any budget-relevant postings. Retroactively capturing budget-relevant postings is not possible. |

1. Cost Center Budget availability control is at G/L account group (unlike Project this is not linked to FSV and semantic Tags)
2. G/L account group can be created either via the Edit Cost Element Groups app or the Manage Global Accounting Hierarchies - GL Account Hierarchy app.
3. All the G/L account group assigned to a particular budget profile should be part of same G/L account Hierarchy (top node of groups).
4. To actively use hierarchy created via Edit Cost Element Groups app in customizing, the prerequisites to set report relevancy via Set Report Relevancy - Set-Based Hierarchies (F5295) app (for example, for default content set class 0102, org YCOA, set name YBA000-CE and Include sub-node), and replicate runtime hierarchy (example for default content 0102/YCOA/YBA000_CE) must be carried out. The default content comes with GL Hierarchy YBA000_CE and customer can assign any groups to this as per their requirements and edit the predefined profile CC001- Cost Center Budget.

|  |
| --- |
| Note Make sure to always replicate runtime hierarchy after any change to the existing hierarchy to reflect the change and before mapping the groups in this step. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Overhead Cost Management

1. For the row with Item Name of Budget Management, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Maintain Budget Availability Control Profile for Cost Centers row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Maintain Budget Availability Control Profile for Cost Centers activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Change Entry of the Identified combination | Select the entry with profile CC001 and double-click Account Group. Go to New Entries on the top menu and add the cost element groups and hierarchy. | All the G/L account groups assigned to a particular budget profile should be part of the same G/L account hierarchy (top node of groups). |  |
| 2 | Change/Add Tolerance Limits for Each Group | Choose the G/L Account Hierarchy line and double-click Tolerance Limit and make the entry as per your requirements.You can delete the tolerance limits that you created. |  |  |
| 3 | Save | Save the entries. |  |  |

#### Optional: Updating Project Budget Profiles (Only Required When Using Project Budget Functionality)

Purpose

The default content for Project Budgeting uses the profile PS001. You can either update this profile or create your own via the configuration activity Maintain Budget Availability Control Profile for Projects.

Prerequisites

- Maintain Financial statement YPS2
- Tag ACT_COST which is mandatory for G/Ls relevant for Budget check. Commitment/Budget works for stock and non-stock purchase orders.
- Maintain Financial Statement Versions (FSV)
- Assign Semantic Tags for FSV
- Set Report Relevancy
- Replicate Runtime Hierarchy. Make sure G/Ls relevant for budget are part of this structure.

|  |
| --- |
| Note To update Project Q stock using SAP's predefined profile PSQ01 - Projct Bdgt Avail Prfl Q Std, which comes with default settings, ensure you follow the steps below to create your own profile: |

- For project budget associated with Project Q stock, the parent tag PSQBUDGET is mandatory for G/L accounts relevant to budget checks. Commitment and budget operations apply to all Q stock (balance sheet accounts) mapped to the child tag PRSLS_STCK, along with primary cost G/L accounts mapped to ACT_COST and possibly other G/L accounts mapped to your own semantic tags that have PSQBUDGET as their parent tag.
- Within the profile for project budget tied to Project Q stock, PSQBUDGET tag is recommended to ensure the effective functioning of the budget with the Q stock solution from end to end.
- Maintain FSVs for all required G/L accounts.
- Assign child semantic tags such as PRSLS_STCK and ACT_COST to FSV. You do not require to map the parent tag PSQBUDGET to FSV YPS2.
- Set Report Relevancy
- Replicate Runtime Hierarchy

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Overhead Cost Management

1. For the row with Item Name of Budget Management, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Maintain Budget Availability Control Profile for Cost Centers row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Maintain Budget Availability Control Profile for Projects activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Change Entry of the Identified combination | Select the entry with profile PS001 or PSQ01 and double-click Semantic Tags.Check the tag assigned and tolerance limits.For PS001, the semantic tag ACT_COST is used, whereas for PSQ01, the semantic tag PSQBUDGET is used.You can delete the tolerance limits that you created. |  |  |
| 2 | Save | Save the entries. |  |  |

## Overview Table

This scope item consists of several process steps provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Commitment Management by Cost Center](#unique_12) [page ] 13 | Cost Accountant - Overhead | Commitments by Cost Center (F3016) | A report showing commitments on the purchasing side for cost centers is displayed. |
| [Commitments by Cost Center](#unique_13) [page ] 14 | Cost Accountant - Overhead | P&L - Plan/Actual/Committed (W0170) | A report showing plan, actual, and commitments for the cost object is displayed. |
| [Monitor Projects via Project Budget Report](#unique_14) [page ] 15 | Project Financial Controller | Project Budget Report (F3378) | You can monitor projects and view the Project Budget report. |

Table 1: OPTIONAL: Commitment Management and Cost Centers Budgeting

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Exclude Cost Center Data for Commitment Management](#unique_15) [page ] 17 | Cost Accountant - Overhead | Manage Cost Centers - Old Version (F1443A) | Includes cost center data for commitment management reporting. |
| [Create Purchase Order](#unique_16) [page ] 18 | Purchaser | Create Purchase Order - Advanced (ME21N) | Creates the demo data to view the commitments in reporting. |
| [Commitment Management by Cost Center](#unique_17) [page ] 20 | Cost Accountant - Overhead | Commitments by Cost Center (F3016) | Allows visibility of purchase order commitments to be viewed by cost center and cost elements. |
| [Set Cost Center Master Budgeting Parameters](#unique_18) [page ] 21 | Cost Accountant - Overhead | Manage Cost Centers - Old Version (F1443A) | Includes cost center data for budgeting. |
| [Template for File Upload](#unique_19) [page ] 22 | Cost Accountant - Sales | Import Financial Plan Data (F1711) | Downloads the template and prepare your plan data for upload. |
| [Import Financial Data](#unique_20) [page ] 24 | Cost Accountant - Sales | Import Financial Plan Data (F1711) | Opens the Import P&L Plan Data app and select a source file. |
| [Create Purchase Order](#unique_21) [page ] 25 | Purchaser | Create Purchase Order - Advanced (ME21N) | Creates the demo data to view the commitments in reporting. |
| [View Budget by Cost Center](#unique_22) [page ] 27 | Cost Accountant - Overhead | Cost Center Budget Report (F3871) | Allows visibility of purchase order commitments to be viewed by cost center and cost elements. |
| [Cost Center Review Booklet with Budget](#unique_23) [page ] 27 | Cost Accountant - Overhead | Cost Centers - Review Booklet (F7763) | A report showing year-to-date comparison for selected company code, cost center hierarchy, and G/L account hierarchy combination displays. |
| [Transfer Cost Center Budgets](#unique_24) [page ] 28 | Cost Accountant - Overhead | Manage Cost Center Budgets (F4307) | Transfers cost center budget from one general ledger/cost center combination. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

|  |
| --- |
| Note Depending on the prerequisite scope item performed, different steps apply. If performing J54, proceed to step: [Commitment Management by Cost Center](#unique_12) [page ] 13. If performing 1NT proceed to step: [Monitor Projects via Project Budget Report](#unique_14) [page ] 15. |

### Analytics

#### Commitment Management by Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report allows visibility of purchase order commitments to be viewed by cost center and cost elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Commitments by Cost Center (F3016). | The Commitments by Cost Center (F3016) screen displays. |  |
| 3 | Selection Criteria | Make the following entries:Ledger: 0LPlan Category: PLNCompany Code: 3310Fiscal Year: <Current year> |  |  |
| 4 | Choose | Choose Go. | A report showing commitments on the purchasing side for the cost centers is displayed. |  |

#### Commitments by Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report shows the plan, actual, and committed data to be viewed by cost center and cost elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open P&L - Plan/Actual/Committed (W0170). | The P&L - Plan/Actual/Committed screen displays. |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Key Date: <today's date>Ledger:0LPlan Category: PLNFiscal Year of Ledger: <Current fiscal year>G/L Account Hierarchy: 0102/YCOA/YBA000_CECompany Code: 3310Cost Center: <enter your desired cost center> | A report showing plan, actual, and commitments for the cost object displays. |  |

#### Monitor Projects via Project Budget Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can analyze your project's cost structure and check the planned budget. Depending on the budget availability profile selected during the project creation, you can view the budget consumption report for a specific fiscal year or the overall project duration.

Prerequisites

If you plan to use Project Budget, make sure that you activate the non-standard scope item Predictive Commitments Management (2I3), as it is a prerequisite for budgeting. Once activated, the commitment management ledger 0E becomes active and applicable across all company codes and countries.

|  |
| --- |
| Note You can check, review, and update the project budget profiles as described in the section Optional: Updating Project Budget Profiles under the Preliminary Steps of Predictive Commitments Management (2I3). |

Procedure

|  |
| --- |
| Caution This Project Budget Report (F3377) app doesn’t display data associated with the semantic tag PSQBUDGET. To see data related to PSQBUDGET, use the Project Cost Report - Plan/Actual (F2513) which accurately displays the project budget, project stock, actual costs, and commitments in global currency. You can manually calculate the available budget using the formula: Available Budget = Project Budget - (Project Stock Costs + Actual Costs + Commitments). |

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Project Financial Controller . | The SAP Fiori Launchpad displays. |  |
| 2 | Access App | Open Project Budget Report (F3377). | The Project Budget Report - Overview screen displays. |  |
| 3 | Enter Selection Criteria | In the upper area, make the following entries and choose Go.Project : <Refer the respective project created in the Create Project section>Example O.000001 (for Overhead Project)I.000001 (for Investment Project)R.000001 (for Revenue Project)S.000001 (for Statistical Project)Planning Category: PlanFiscal Year: Current year | Details of the project structure and the corresponding planned budget display.Note The aggregated and non- aggregated costs of the selected project are displayed. In the budget report, you would see the assigned value (Commitment +Actual) and available budget (Budget-Assigned Value) based on which you can analyze the project. |  |
| 4 | Navigation to Project Budget Report - Line items; view details of different cost | Select the project in the table, and choose View Details.On the Project Budget Report - Line items screen, check the financials using drilldown and filter possibilities.Note In the Standard section, the information is shown in the Compact Filter view by default.You can also change it to Visual Filter view to get an easy understanding of overall costs of the project. This visual depiction helps the stakeholders to get an overview of the project. | All the plan, actual, and budget costs display. |  |
| 5 | Navigation to Project Budget Report- Line items: view graphical representation of different costs | In the Project Budget Report - Line items screen, once you ensure all required search fields are filled, you can see the different cost items recorded on the project as graphical representations, such as the bubble chart, bar graph and pie chart.Note You can see the details of the cost items by hovering the cursor on the graphs. | The cumulative actual costs, commitments and budget posted on the project display. |  |

### OPTIONAL: Commitment Management and Cost Center Budgeting

#### Commitment Management Cost Centers Actual Data Reporting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note This section is only applicable if you select the non-standard scope item 2I3 - Predictive Commitments Management. You have additional features in cost centers to view commitment which comes via purchasing.Commitment management is part of the cost monitoring process. Commitment management line items are triggered by stock and non-stock expense purchase requisitions and/or purchase orders that utilize cost centers. These commitments are updated in Extension Ledger 0E (predelivered) in ACDOCA table. Commitments are reduced by various business transactions such as goods receipt. |

Prerequisites

- To use commitment management functions, a nonstandard scope item 2I3 - Predictive Commitments Management must be selected and activated. Once activated, commitment management ledger 0E is active and applicable for all company codes and countries.
- Master Data requirement: Specific cost centers relevant for your commitment tracking must be unlocked. See the procedure on [Exclude Cost Center Data for Commitment Management](#unique_15) [page ] 17.
- To view commitments in the report, an open purchase order and/or requisition must exist. For details on creating purchase orders, refer to Consumable Purchasing (BNX).

##### Exclude Cost Center Data for Commitment Management

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to exclude cost center data from commitment management reporting. If you select the lock on the cost center master data, consumable purchases that utilize the cost center are excluded from the report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad with a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Open Manage Cost Centers | Open Manage Cost Centers - New Version (F1443B). | The Manage Cost Centers view displays. |  |
| 3 | Cost Center | Make the following entry and choose Go:Cost Center: 33101501Select the line item with Cost Center and choose the (>) Details button. |  |  |
| 4 | Lock Commitment Updates | Choose the Edit button on the top row. In the Control section, select the Lock Commitment Updates to see the ON sign.Choose the Save button on the bottom right of your view. | When the Lock Commitment Updates is set to On, no further updates for this cost center would be shown in the commitment report. |  |

##### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This prerequisite activity creates the demo data to view the commitments in reporting.

|  |
| --- |
| Note For details on consumable purchasing, refer to Consumable Purchasing (BNX), steps Create Purchase Requisition or Create Purchase Order. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order view displays. |  |
| 3 | Start Purchase Order creation | Make the following entries and choose Enter:Supplier : 33300001 | The Create Purchase Order view displays. |  |
| 4 | Enter Purchase Order data | Make the following entries and choose Enter.Org. Data:Purch. Org.:3310Purch. Group:001Company Code: 3310 | The Create Purchase Order view displays. |  |
| 5 | Enter Additional Details | Make the following entries and choose Enter:A: (Account Assessment Category): K (Cost center)Material: TG0011PO Quantity:1Net Price: 450Plnt: 3310Stor. Location: 331AIn the next section, enter the following and choose Enter:Cost Center:33101401 | The Create Purchase Order view displays. |  |
| 6 | Save the entries | Choose the Save button to save the purchase order. | The Purchase Order is created. |  |

##### Commitment Management by Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report allows visibility of purchase order commitments to be viewed by cost center and cost elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Commitments by Cost Center (F3016). | The Commitments by Cost Center (F3016) view displays. |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Ledger: 0LPlan Category: PLNCompany Code: 3310Fiscal Year: <Current year> | A report showing commitments on the purchasing side for the cost centers is displayed. |  |

#### Cost Center Budgeting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

|  |
| --- |
| Note This section is applicable only if you select non-standard scope item Predictive Commitments Management (2I3), which is also a prerequisite for budgeting. With this feature, you gain additional capabilities in cost centers for viewing commitments and budgets, allowing you to effectively monitor your expenses.Budgeting is a part of the cost monitoring process. Commitment management line items in SAP S/4HANA Cloud Public Edition are triggered by expense purchase requisitions and/or purchase orders that utilize cost centers and a material master. These commitments are updated in the Extension Ledger 0E (predelivered) in the ACDOCA table. Commitments are reduced by various business transactions, such as goods receipts.Cost Center Budget availability control is managed at the G/L account group level (unlike Projects, this is not linked to FSV and semantic tags). Cost Center Budgeting utilizes profile CC001, which allows you to assign a G/L account hierarchy and G/L account group to specify the general ledger accounts applicable for your cost center budgets. The default content utilizes G/L account hierarchy YBA000_CE and two G/L account groups: 1200_CE Production Costs Materials and 1900_CE Travel Costs.Once you create your G/L account hierarchy and G/L account groups, you must perform the Set Report Relevancy and Replicate Runtime Hierarchy steps as covered in the Preliminary Steps section of this document. |

Prerequisites

- To use cost center budgeting functions, you must select and activate the nonstandard scope item Predictive Commitments Management (2I3). Once activated, the commitment management ledger 0E becomes active and applicable for all company codes and countries.
- You must perform the Set Report Relevancy and Replicate Runtime Hierarchy steps as mentioned in the Preliminary Steps section of this document.
- To view commitments in the report, an open purchase order or requisition must exist. For details on creating purchase orders, refer to the Consumable Purchasing (BNX) test script.

##### Set Cost Center Master Budgeting Parameters

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity describes how to include cost center data for budgeting.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Centers - New Version (F1443B). | The Manage Cost Centers view displays. |  |
| 3 | Cost Center 33101601 | Make the following entry and choose Go:Cost Center: 33101601Select the line item with Cost Center and choose the (>) Details button. |  |  |
| 4 | Save the Entries | In the Control section, under Budget Availability Control, choose the Edit button and then make the following entries:Budget-Carrying Cost Center: 33101601Budget Availability Control Profile: CC001Budget Availability Control is Active: ONChoose the Save button on the bottom of the view. |  |  |
| 5 | Cost Center 33101202 | Repeat steps 3 and 4 using cost center 33101202. |  |  |

##### Upload Financial Data

###### Template for File Upload

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity helps you download the template and prepare your plan data for upload. Depending on the scope of your solution, the plan data you fill the template with will differ. You can use the sample data to populate the template. If you have plan data already in your system and would like to copy the data to a new Plan Category, application Copy Financial Plan Data (F3396) can achieve this without the need to manually upload the data.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data (F1711) view displays. |  |
| 3 | Select Template | Choose the Download Templates button.In the Download Templates view, select the comma as separator and then the Cost Center Budgeting template.Open the downloaded CSV template.Enter the field values as listed in the table below this table. |  |  |
| 4 | Save Template | Save the file in the CSV format. |  |  |

Field Value Table

| CATEGORY | RYEAR | POPER | RBUKRS | RCNTR | RACCT | HSL | RHCUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Category | General Ledger Fiscal Year | Posting Period | Company Code | Cost Center | Account Number | Amount in Local Currency | Local Currency |
| X | X |  | X | X |  |  |  |
| BUDGET02 | (Current Year) | 3 (Current Period) | 3310 | 33101601 | 61007000 | 1000 | AED |
| BUDGET02 | (Current Year) | 3 (Current Period) | 3310 | 33101601 | 65000500 | 1000 | AED |
| BUDGET02 | (Current Year) | 3 (Current Period) | 3310 | 33101202 | 51600000 | 500 | AED |

###### Import Financial Data

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

Once the plan data file is saved in the template, open the Import P&L Plan Data app and select a source file.

The app performs the following checks:

1. The app checks whether the values in the source file are valid. If required, it returns a list of error messages. You must correct the values in the source file until they are all valid before you can proceed.

2. If all values are valid, the app selects the distinct values for all characteristics of the plan data scope (as defined in the third row of the source file).

- If no plan data exists in the system for any combination of these characteristic values, you can directly import the plan data.
- If plan data exists in the system for any combination of these characteristic values, the app displays the affected values. It assumes that you want to completely replace the existing plan data by the new plan data import.

|  |
| --- |
| Note One source file must therefore always contain full plan data sets for a certain combination of the characteristics you specified in the third row (the plan data scope). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Import Financial Plan Data (F1711). | The Import Financial Plan Data (F1711) view displays. |  |
| 3 | Cost Center | Use the Browse button to select the CSV extension file you wish to upload and choose Enter.Make the following entry:Source File: Your .CSV file that contains your plan |  |  |
| 4 | File Check | The upload performs a check to ensure that the format is correct. Correct any error message that appears.To review the data, choose Preview List, and then choose Back. | You are going to see the messages in the upper part of your view. |  |
| 5 | Import Source File | Choose Import Source File. To view the data, choose Display Financial Plan Data. | Import successful message appears. |  |

##### Create Purchase Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This prerequisite activity creates the demo data to view the commitments in reporting.

|  |
| --- |
| Note For details on consumable purchasing, refer to Consumable Purchasing (BNX), steps Create Purchase Requisition or Create Purchase Order. |

|  |
| --- |
| Note Purchase line items without a material master using material group are currently not included in Commitments. But during actual posting (goods receipts) the amounts are checked and included in Bugeting. This is shown in the example below. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Purchaser role. | The SAP Fiori launchpad is displayed. |  |
| 2 | Open Manage Purchase Order | Open Create Purchase Order - Advanced (ME21N). | The Create Purchase Order view displays. |  |
| 3 | Start Purchase Order creation | Make the following entries and choose Enter:Supplier : 33300001 | The Create Purchase Order view displays. |  |
| 4 | Enter Purchase Order data | Make the following entries and choose Enter.Org. Data:Purch. Org.:3310Purch. Group:001Company Code: 3310 |  |  |
| 5 | Enter Additional Details | Make the following entries and choose Enter:A: (Account Assessment Category): K (Cost center)Material: TG0011PO Quantity:1Net Price: 450Plnt: 3310Stor. Location: 331AIn the next section, enter the following and choose Enter:Cost Center:33101601 |  |  |
| 6 | Enter Additional Details in the Next Line | Enter the following:A: (Account Assessment Category): K (Cost center)Description:Office EquipmentMaterial Group: L005OUn: EAPO Quantity:1Net Price: 1000Plnt: 3310Stor. Location: 331AIn the next section, make the following and choose Enter:G/L Account: 61007000Cost Center:33101202 |  |  |
| 7 | Save the entries | Choose the Save button. | The Purchase Order is created. |  |

##### View Budget by Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report allows visibility of purchase order commitments to be viewed by cost center and cost elements.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Cost Center Budget Report (F3871). | The Cost Center Budget Report (F3871) view displays. |  |
| 3 | Selection Criteria | Make the following entries:Plan Category: BUDGET02Company Code: 3310Fiscal Year: <Current year> |  |  |
| 4 | Commit for the Cost Centers | Choose Go. |  |  |

##### Cost Center Review Booklet with Budget

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can run reports to view year over year comparisons for selected company codes, cost center hierarchy, and G/L account hierarchy combinations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Cost Centers - Review Booklet (F7763). | The Cost Center - Review Booklet dialog box displays. |  |
| 3 | Selection Criteria | Make the following entries and choose Go:Ledger:<0L>Reporting Date: <today's date>Company Code: 3310Cost Center Hierarchy: <use the dropdown to select 0101/A000/A000>Tip To view both the key and description, select the dropdown menu in the field and change the Display setting to ID and Description.G/L Account Hierarchy: <use the dropdown to select 0102/YCOA/YBA000_CE> | A report showing year-to-date comparison for selected company code, cost center hierarchy, and G/L account hierarchy combination displays. |  |

##### Transfer Cost Center Budgets

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity transfers cost center budget from one general ledger/cost center combination.

Prerequisites

- Cost center must have a budgeting profile assigned.
- Cost center budgeting data must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Center Budgets (F4307). | The Manage Cost Center Budgets view displays. |  |
| 3 | Initial Entries | Choose Create and from the dropdown, select Budget Transfer.Note Budget Return option can decrease an existing budget and Budget Supplement option can increase an existing budget. | The Budget Document view displays. |  |
| 4 | Create Budget Transfer | Choose the Create button and make the following entries:Posting Date: <enter current date>Plan Category: BUDGET02Document Type: S_BTIn the Sender Items section, make the following entries:Cost Center: 33101601Account Number: 65000500Amount in Company Code Currency: 500In the Receiver Items section, make the following entries:Cost Center: 33101202Account Number: 51600000Amount in Company Code Currency: 500Choose Create. | The budget transfer has now been posted. Note your document number for the next step. |  |
| 5 | Reverse Posting | Go back to the Transfer Cost Center Budgets view. Make the following entry and choose Go:Document Number: <as created in the previous step>On the Budget Transfer Document view, choose Reverse and make the following entries:Document Description: <optional>Reversal Reason: <choose one, for example, wrong posting>Choose Create. | The reversal is successful. The status of the initial posting document changes to Reversed.Additionally, a new document is generated with the status Reversal.The two documents (Reversed and Reversal) should reference each other in the Reversal Reference Number field. |  |

## Appendix

### Process Integration

The process to be tested in this test script is part of a chain of integrated processes.

#### Preceding Processes

Complete the following processes and conditions before you start with the test steps:

| Process | Business Condition |
| --- | --- |
| 1NT | Project Financial Control |

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business process:

| Process | Business Condition |
| --- | --- |
| BNA | Period-End Closing - Projects |

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
> Flagged while digesting this document, not verified: Project Budget Report app is given as F3378 in the Overview Table but F3377 in the test procedure.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Table lists the Cost Accountant - Sales role for Import Financial Plan Data (F1711) steps while the template step uses Cost Accountant - Overhead; the exclude step names Manage Cost Centers - Old Version (F1443A) in overview but New Version (F1443B) in procedure.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[06-management-accounting/budgetupload-xx-3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2I3_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 52,017 chars in the whole document
