---
id: 06-management-accounting/margin-analysis-j55-ae-test-script-sap-s-4hana-cloud-public-edition-13
title: Margin Analysis (J55_AE) Test Script - SAP S/4HANA Cloud Public Edition (J55_S4CLD2608_BPD_EN_AE)
description: "SAP Best Practices test script for scope item J55 Margin Analysis (AE): prerequisites, CO-PA allocations, top-down distribution, realignment and profitability reports."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/margin-analysis]
aliases: [J55_S4CLD2608_BPD_EN_AE]
keywords: [Margin Analysis (CO-PA), margin analysis, test prerequisites, product profitability kpis, assessment cycle, top-down distribution, profitability realignment, project profitability, market segment reporting, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J55_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1303
topic: 06-management-accounting/margin-analysis
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Margin Analysis (J55_AE) Test Script - SAP S/4HANA Cloud Public Edition (J55_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J55_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Margin Analysis (CO-PA)** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Margin Analysis (J55_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Margin Analysis (J55_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232863079)

[2 Prerequisites 4](#_Toc232863080)

[2.1 System Access 4](#_Toc232863081)

[2.2 Roles 4](#_Toc232863082)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232863083)

[2.4 Business Conditions 5](#_Toc232863084)

[2.5 Preliminary Steps 6](#_Toc232863085)

[2.5.1 User Settings - Set Controlling Area 6](#_Toc232863086)

[2.5.2 Set Report Relevancy 7](#_Toc232863087)

[2.5.3 Replicate Runtime Hierarchy 8](#_Toc232863088)

[2.5.4 Product Profitability Report and Update of Financial Statement Version YPS2 9](#_Toc232863089)

[2.5.5 Optional: Manage Substitution/Validation Rules 10](#_Toc232863090)

[3 Overview Table 12](#_Toc232863091)

[4 Test Procedures 14](#_Toc232863092)

[4.1 Post Expenses to Central Cost Center 14](#_Toc232863093)

[4.2 Execute Assessment Cycle (CO-PA) 15](#_Toc232863094)

[4.3 Top-Down Distribution 17](#_Toc232863095)

[4.3.1 Create Top-Down Distribution Cycle 17](#_Toc232863096)

[4.3.2 Execute Top-Down Distribution 21](#_Toc232863097)

[4.3.3 Optional: Manage Allocation Changes 22](#_Toc232863098)

[4.4 Create Profitability Realignment Run 23](#_Toc232863099)

[4.4.1 Create Profitability Realignment Run 23](#_Toc232863100)

[4.4.2 Execute Profitability Realignment Run 24](#_Toc232863101)

[4.4.3 Analyze Realignment Results 25](#_Toc232863102)

[4.5 Analytics 26](#_Toc232863103)

[4.5.1 Project 26](#_Toc232863104)

[4.5.1.1 Project Profitability Overview 26](#_Toc232863105)

[4.5.1.2 Project Profitability 27](#_Toc232863106)

[4.5.1.3 Project Financial Booklet - Professional Services 28](#_Toc232863107)

[4.5.1.4 Project Financial Booklet - Enterprise Projects 29](#_Toc232863108)

[4.5.2 Product 31](#_Toc232863109)

[4.5.2.1 Product Profitability Review Booklet 31](#_Toc232863110)

[4.5.2.2 Product Profitability with Production Variances 32](#_Toc232863111)

[4.5.3 Service 33](#_Toc232863112)

[4.5.3.1 Solution Order Margins 33](#_Toc232863113)

[4.5.3.2 Service Profitability Review Booklet 34](#_Toc232863114)

[4.5.4 Market Segments 35](#_Toc232863115)

[4.5.4.1 Market Segments Actual Report 35](#_Toc232863116)

[4.5.4.2 Market Segments Actual vs Plan Report 36](#_Toc232863117)

[4.5.5 Cross-Object Margin Reporting 37](#_Toc232863118)

[4.5.5.1 Display Line Items - Margin Analysis 37](#_Toc232863119)

[4.5.5.2 Product and Service Margins 38](#_Toc232863120)

[4.5.5.3 Company Profitability Review Booklet 38](#_Toc232863121)

## Purpose

Overview

This scope item enables you to analyze profit and contribution margins by market segment or strategic business unit, such as a sales organization or business area. You can analyze contribution margins for individual products and services, and monitor the profitability of project-based services you provide to your clients. You can also see unbilled project costs and revenues.

The cost and revenue information is always current and fully reconciled with the income statement.

After performing allocations and top-down distributions, the application offers several reports to analyze the data.

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
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

Default Values

The organizational structure and master data of your company were created in your ERP system during implementation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

The business process is enabled with the organization-specific master data, examples are provided in the next section.

Operational Focus

SAP Best Practices delivers standard values for more than one operational focus area, such as Services, Manufacturing, or Trade. This means that you may find more than one master data in the following table. Use the master data that matches the operational focus of your company (Services, Manufacturing, or Trade).

|  |
| --- |
| Note Additional Default ValuesYou can test the scope item with other SAP Best Practices default values that have the same characteristics. Check your SAP ECC system to find out which other material master data exists. |

|  |
| --- |
| Note Using Your Own Master DataYou can also use customized values for any material or organizational data for which you have created master data. For more information about creating master data, see the Master Data Procedures documentation. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices Baseline Package, you can use the following Baseline Package scenario data:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Operating Concern | A000 |  |  |
| Controlling Area | A000 |  |  |
| Company Code | 3310 |  |  |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BND - Create Customer Master - MDS | Customer master data needs to be created. |
| BD9 - Sell from Stock | General postings for these customers must be done. |
| 1HB - Financial Plan Data Upload from File | Planning data must be added. |
| J11 - Customer Project Management – Project-Based Services or4I9 - Project Control – Sales or1NT - Project Control – Finance or1A8 - Internal Project Management – Project-Based Services or6GD - Engineer Products and Systems – Project with Production | Execute any of these scripts to run project reporting - [Project Profitability Overview](#unique_7) [page ] 26 and [Project Profitability](#unique_8) [page ] 27. |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing | Execute at least one production scope like Make-to-Stock Production – Discrete Manufacturing (BJ5) or any other production or process order manufacturing scope, and at least one sales scope like Sell from Stock (BD9) of these scripts to run product reporting - [Product Profitability with Production Variances](#unique_9) [page ] 32. |
| 3MO - Service Contract Management or3D2 - Service Order Management and Monitoring or4GT - Solution Order Management | Execute any of these scripts for service reporting - [Solution Order Margins](#unique_10) [page ] 33 and [Service Profitability Review Booklet](#unique_11) [page ] 34. |

|  |
| --- |
| Note Execute any of the above scripts (in the last three rows) for reporting of market segments and cross-object margins. |

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

#### Set Report Relevancy

Purpose

Report relevancy must be done when you execute any reports for the first time. If you make a subsequent change in cost center, profit center, or G/L hierarchy, perform this step again to get the latest information.

Also, you must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally, this would be created as a periodic job that would run in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Set Report Relevancy - Set-Based Hierarchies (F5295). | The Set Report Relevancy for Set-Based Hierarchies screen displays. |  |
| 3 | Enter Header Data | Make the following entries and choose Go:Set Class: For example,0101, for the cost center groupOrganizational Unit: A000Set Name: A000Include Subnodes: Yes |  |  |
| 4 | Mark as Report Relevant | In the Set Report Relevancy section, select the row and choose Edit. In the dialog box, make the following entries:Report Relevant: Yes |  |  |
| 5 | Save | Choose Save.Note If you are using the optional procedure Commitment Management and Cost Center Budgeting, repeat steps 1-5 with the following entries instead:Set Class: 0102Organizational Unit: YCOASet Name: YBA000_CEInclude Subnodes: <Select> | Set updated message displays. |  |

#### Replicate Runtime Hierarchy

Purpose

You must manually replicate set-based hierarchies (such as Cost Center Group or Profit Center Group) and financial statement hierarchies to the backend database hierarchy tables. Normally, this would be created as a periodic job that would run in the background.

Procedure

| Step # | Step Name | Instruction | Expected Result | Pass/Fail/Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access the SAP Fiori App | Open Schedule Overhead Accounting Jobs (F3767). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job: Replicate Runtime Hierarchy (SAP) view displays. |  |
| 4 | Header Data for Hierarchy ID 0101/A000/A000 | In the header area, make the following entries and choose Schedule:Job Template: Replicate Runtime Hierarchy (SAP)Job Name: <Enter a text>Choose the Step 2 button.Start Immediately: SelectChoose the Step 3 button.In the Create Hierarchy area, make the following entry:Hierarchy ID: 0101/A000/A000Note If you are using the optional procedure Commitment Management and Cost Center Budgeting, follow steps 1-4, but make the following entries instead:Job Template: Manually Replicate Runtime HierarchyHierarchy ID: 0102/YCOA/YBA000_CE |  |  |
| 5 | Hierarchy ID YPS2 | Repeat the above steps using hierarchy ID YPS2. |  |  |

#### Product Profitability Report and Update of Financial Statement Version YPS2

Purpose

The SAP Product Profitability report comes with predelivered KPIs (see table below). These KPIs are linked to the predelivered financial statement version YPS2 (GLs) via semantic tags.

| KPI | Associated Semantic Tag | Linked FSV node YPS2 |
| --- | --- | --- |
| Billed Revenue | BILL_REV | 23- Revenue |
| Sales Deduction | SALES_DED | 31-Discount |
| Revenue Adjustment | ADJ_REV | 25-Revenue Adjustments |
| Recognized Revenue | RECO_REV | 20- Net Sales/Revenue |
| COGS-Variable | RECO_COS | 38-Cost of Goods Sold |
| Contribution Margin-I | Calculated-N/A | Calculated |
| COGS-Fixed | RECO_COS | 38-Cost of Goods Sold |
| Price Differences | PRICE_DIF | 22-Variances |
| Contribution Margin-II | Calculated-N/A | Calculated |
| Billed Quantity |  |  |

|  |
| --- |
| Note If you want to add your own G/L or create additional nodes in FSV YPS2 that are relevant for the Product Profitability report, the new node or G/L must be under one of the existing nodes (non-calculated one). For example, if you want to add a freight cost G/L via new node, you would create the node under node number 38 to include it as part of cost of goods sold KPI in the report. The number mentioned in the table above can be viewed in FSV YPS2 (Manage Financial Statement Versions app > double-click on YPS2 > Financial Statement Items) via Menu > Settings > Change > Item keys visible . |

#### Optional: Manage Substitution/Validation Rules

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

With this app, you can display, change, and create substitution and validation rules for your selected business contexts and events. These rules can be used in the respective business processes to validate, derive, or replace values at the time of entry for the relevant fields.

|  |
| --- |
| Note You can create substitution rules, for example, for the following business processes when you select the Market Segment context in the Manage Substitution/Validation Rules app:Sales Order CreationPost Journal EntryGoods IssueEvent-Based Revenue RecognitionSales Invoice |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Substitution/Validation Rules (F4406). | The Manage Substitution and Validation Rules screen displays. |  |
| 3 | Create Rules | Enter the following as per your business needs and choose Create:Business Context: Market SegmentEvent: Market SegmentRule Type: Substitution Rule | The rules are defined. |  |
| 4 | New Substitution | Enter the following as per your business needs and choose Save:General Information:Rule Name: <any>Description: <any>PreconditionField/Function: <Select the field for which you want to set the substitution>Operator: <Equal To>Value: <enter the default value>SubstitutionTarget Field: <Select the field for which you want to set the substitution>Substitution Type: <Use the dropdown to select, for example, Substitute with Constant>Source: <enter the default value>Note The list of available fields that can be substituted depends on the context you select. |  |  |

## Overview Table

This scope item consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Post Expenses to Central Cost Center](#unique_18) [page ] 14 | General Ledger Accountant | Post General Journal Entries (F0718) | The accounting document is posted successfully. |
| [Execute Assessment Cycle (CO-PA)](#unique_19) [page ] 15 | Cost Accountant - Sales | Run Allocations (F3548) | Cost center costs have been transferred to CO-PA for Profitability Analysis. |
| [Create Top-Down Distribution Cycle](#unique_20) [page ] 17 | Cost Accountant - Sales | Manage Allocations (F3338A) | A top-down distribution cycle is created. |
| [Execute Top-Down Distribution](#unique_21) [page ] 21 | Cost Accountant - Sales | Manage Allocations (F3338A) | A top-down distribution cycle is executed. |
| [Optional: Manage Allocation Changes](#unique_22) [page ] 22 | Cost Accountant - Overhead | Manage Allocation Changes (F7272) | You can view the version history of a cycle. |
| [Create Profitability Realignment Run](#unique_23) [page ] 23 | Cost Accountant - Sales | Run Realignment - Profitability Analysis (KEND) | The newly created realignment request is listed underneath the realignment run. |
| [Execute Profitability Realignment Run](#unique_24) [page ] 24 | Cost Accountant - Sales | Run Realignment - Profitability Analysis (KEND) | The Realignment Run, from previous procedures, successfully executes. |
| [Analyze Realignment Results](#unique_25) [page ] 25 | Cost Accountant - Sales | Realignment Results - Profitability Analysis (F2549) | View the monetary amount of all realignments as well as all related journal entry items. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Project Profitability Overview](#unique_7) [page ] 26 | Cost Accountant - Sales | Project Profitability Overview (F2794) | You can monitor profitability information for your project-based services. |
| [Project Profitability](#unique_8) [page ] 27 | Cost Accountant - Sales | Project Profitability (W0052) | You can track the profitability of your project-based services. |
| [Project Financial Booklet - Professional Services](#unique_26) [page ] 28 | Cost Accountant - Sales | Project Financial Booklet - Professional Services (F7479) | An overview of different metrics related to the selection criteria displays. |
| [Project Financial Booklet - Enterprise Projects](#unique_27) [page ] 29 | Cost Accountant - Sales | Project Financial Booklet - Enterprise Projects (F8698) | An overview of different metrics related to the selection criteria displays. |
| [Product Profitability Review Booklet](#unique_28) [page ] 31 | Cost Accountant - Sales | Product Profitability Review Booklet (F8348) | You can analyze information such as contribution margins for individual products with related product information and profitability characteristics. |
| [Product Profitability with Production Variances](#unique_9) [page ] 32 | Cost Accountant - Sales | Product Profitability with Production Variances (W0182) | You can analyze information such as contribution margins for individual products with related product information and profitability characteristics. |
| [Solution Order Margins](#unique_10) [page ] 33 | Cost Accountant - Sales | Solution Order Margins (F6061) | You can analyze revenue, costs and contribution margins for individual solution orders across different installation services, or service and maintenance contracts within a region or channel. |
| [Service Profitability Review Booklet](#unique_11) [page ] 34 | Cost Accountant - Sales | Service Profitability Review Booklet (F6600) | The service margins overview displays. |
| [Market Segments Actual Report](#unique_29) [page ] 35 | Cost Accountant - Sales | Market Segments - Actuals (F0960) | The report displays. |
| [Market Segments Actual vs Plan Report](#unique_30) [page ] 36 | Cost Accountant - Sales | Market Segments - Plan/Actual (New Version) (F9103) | The report displays. |
| [Display Line Items - Margin Analysis](#unique_31) [page ] 37 | Cost Accountant - Sales | Display Line Items - Margin Analysis (F4818) | You can view line items that are relevant to margin analysis. |
| [Product and Service Margins](#unique_32) [page ] 38 | Cost Accountant - Sales | Product and Service Margins (New Version) (F9104) | You can analyze revenue, costs and contribution margins across multiple dimensions. |
| [Company Profitability Review Booklet](#unique_33) [page ] 38 | Cost Accountant - Sales | Company Profitability Review Booklet (Template) (F8300) | You can analyze profitability margins at the company code level . |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Post Expenses to Central Cost Center

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you post costs to be distributed later via top-down distribution.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a General Ledger Accountant. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Post General Journal Entries (F0718). | The Post General Journal Entries screen displays. |  |
| 3 | Enter Header Data | In the Header area, make the following entries:Journal Entry Date: <Current Date>Posting Date: <Current Date>Period: <current period>, for example, 05Journal Entry Type: SA (G/L Account Document)Company Code: 3310Transaction Currency: AED |  |  |
| 4 | Line Items | In Line Items, make the following entries and press Enter:Company Code: 3310G/L Account: 65400000Debit: 1000 |  |  |
| 5 | Enter Data | Expand the line item and enter the following:Tax Code: <Input Tax Code>Cost Center: 33101201Choose the Assign Profitability Segment button and then choose the Derive & Close button. |  |  |
| 6 | Enter Second Line Item Detail | In the second Line Item, make the following entries and press Enter:Company Code: 3310G/L Account: 10010000Credit: 1000 |  |  |
| 7 | Post | Choose the Post button. | The accounting document is posted successfully. |  |

### Execute Assessment Cycle (CO-PA)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this procedure, you execute an assessment cycle (CO-PA). For more details on allocation features and functions, see Universal Allocation (2QL).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Allocations (F3548). | The Run Allocations view displays. |  |
| 3 | Create a New Run | Choose Add. | The Select: Allocation Cycles for the Run view displays. |  |
| 4 | Input Initial Screen | Make the following entries and choose the Go button:Allocation Context: Margin AnalysisLedger: 0LCompany Code: 3310In the Items area:Allocation Cycle: YUA3310Select the line and choose OK. | Assessment of remaining cost center cost to CO-PA. |  |
| 5 | Execute | Choose the Run button. |  |  |
| 6 | Run Allocation - Live Run | On the Run Allocation(s) - Live Run screen, make the following entries and choose Validate.Test Run Name: <enter your desired value>Fiscal Period From: <current period and year>Fiscal Period To: <curent period and year> | A dialog box appears stating whether the run triggered successfully. |  |

|  |
| --- |
| Tip Allocation runs can be scheduled in advance or based on regular intervals. See the Schedule Allocation Run in Universal Allocation (2QL). |

### Top-Down Distribution

Purpose

In Profitability Analysis, sales revenues, sales deductions, and costs of goods manufactured are generally stored at the customer/product level. However, many business transactions - such as freight invoices, insurance expenses, or advertising - cannot easily be assigned to such a detailed level in CO-PA. Consequently, these need to be posted at a summarized level, such as the customer group, sales organization, or even company code level. Top-down distribution is a periodic function that lets you distribute this aggregated data to more detailed levels in CO-PA on the basis of reference information.

|  |
| --- |
| Note Top-down distribution supports situation handling via standard situation template FIN_ALLOCATION_RUN_WARNING_ERROR. For additional information, refer to scope itemSituation Handling (31N). |

Prerequisites

Generate sales order data using customers 33100001 and 33100003, and materials TG11 and FG126. For details on this process, refer to scope item Sell from Stock (BD9).

#### Create Top-Down Distribution Cycle

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you create a top-down distribution cycle.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori Launchpad as a Cost Accountant - Sales | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations screen displays. |  |
| 3 | Create Cycle Header | Choose the Create button and select Create a new cycle. | The Create a new cycle dialog box displays. |  |
| 4 | Enter Data | Make the following entries and choose the Create button:Allocation Cycle: <enter a cycle ID beginning with Z>Allocation Context: Margin AnalysisAllocation Type: Top Down DistributionLedger: 0LValid From:01/01/2021Valid To: 12/31/2021Top-Down Template: TDPRODUCT&CUSTOMERCycle Description: <enter a cycle description>Controlling Area:A000Actual/Plan: Actual | The Allocation: Create Plan Overhead Allocation Cycle: Header Data view displays.0L |  |
| 5 | Enter Segment Data | In the lower section of the New Allocation Cycle view under the Segments section, choose the Create button and make the following entries in the Create New Segment dialog box:Segment Name: <enter a segment beginning with Z>Segment Description: <enter a description>Note Only a single segment can be attached to each cycle. | The Create a new cycle view displays. |  |
| 6 | Enter Sender Details | Select the new segment in the left pane and choose the arrow on the right.In the Sender Details tab, make the following entries:For value RCNTR Cost Center, select Single Value from the dropdown box and in the Single Entry/From field, enter 33101201.For value RACCT Account Number, select Single Value from the dropdown box and in the Single Entry/From field, enter 65400000. |  |  |
| 7 | Enter Receiver Basis | On the Receiver Basis tab, make the following entries:Receiver Details:Scale Neg. Factors: No NormalizationVar. Portion Type: Actual Local Currency (HSL-0)Attributed Line Item: <Select to include interim postings where profitability segment is a derived attribute>Selection Criteria:For KDGRP Customer Group, select All values from the dropdown box.Choose the Reference base icon on the right and then the + (Add) button and enter the following values:In the Sender Data section:Value Type: All valuesIn the Reference Data section:Value Type: Single ValueSingle Entry/From: 01Choose OK and move on to the next selection criteria. |  |  |
| 8 | Enter Receiver Basis | For MATKL Product Sold Group, select All values from the dropdown box.Choose Reference base and then the + (Add) button and enter the following values:In the Sender Data section:Value Type: All valuesIn the Reference Data section:Value Type: Single ValueSingle Entry/From: L001Choose OK and move on to the next selection criteria. |  |  |
| 9 | Enter Receiver Basis | For value PRCTR Profit Center, select Single Value from the dropdown box and enter YB700.For value RACCT Account Number, select Single Value from the dropdown box and enter 41000000.Choose Reference base and then the + (Add) button and enter the following values:In the Sender Data section:Value Type: Single ValueSingle Entry/From: 65400000In the Reference Data section:Value Type: Single ValueSingle Entry/From: 41000000Choose OK and move on to the next selection criteria. |  |  |
| 10 | Enter Receiver Basis | For value RFAREA Functional Area, select Single Value from the dropdown box and enter YB10.Choose Reference base and then the + (Add) button and enter the following values:In the Sender Data section:Value Type: Single ValueSingle Entry/From: YB20In the Reference Data section:Value Type: All valuesChoose OK and move on to the next selection criteria. |  |  |
| 11 | Enter Receiver Basis | For value VKORG Sales Org., select All values from the dropdown box.Choose Reference base and then the + (Add) button and enter the following values:In the Sender Data section:Value Type: All valuesIn the Reference Data section:Value Type: Single ValueSingle Entry/From: 3310Choose OK and move on to the next selection criteria. |  |  |
| 12 | Enter Receiver Basis | For value WERKS Plant, select All values from the dropdown box.Choose Reference base and then the + (Add) button and enter the following values:In the Sender Data section:Value Type: All valuesIn the Reference Data section:Value Type: Single ValueSingle Entry/From: 3310Choose OK.Choose Save to save the segment. | The segment is saved. |  |

#### Execute Top-Down Distribution

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this step, you execute a top-down distribution cycle.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocations (F3338A). | The Manage Allocations view displays. |  |
| 3 | Input Initial Screen | Make the following entries and choose the Go button:Allocation Context: Margin AnalysisAllocation Type: Top Down DistributionLedger: 0L |  |  |
| 4 | Select Allocation Cycle | Select the allocation cycle row and choose the Run button. | The Run Allocations screen displays. |  |
| 5 | Test Run | Select the allocation cycle row and choose the Run button. | The Run Allocation(s) - Live Run screen displays. |  |
| 6 | Input Values | Make the following entries and choose OK.Run Name: <enter your desired value>Ledger: 0LRef. Period From: <period>Fiscal Period to: < period>Note If you have selected multiple cycles for processing that depend on each other, set the Sequential Processing option to Yes - Stop on Warning. |  |  |

#### Optional: Manage Allocation Changes

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

When cycles are initially created, the version is set. Versions are generated either through a live run (provided there have been changes made between live runs) or upon deletion of a cycle.

Prerequisite

Allocation cycles must exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Allocation Changes (F7272). | The Manage Allocation Changes view displays. |  |
| 3 | Enter Data | Make the following entry and choose Go:Company Code: 3310 | The list of allocation cycles display. |  |
| 4 | Select your Allocation Cycle | Select your allocation cycle, and choose the Select Version button. | You can view the version history of a cycle. |  |

### Create Profitability Realignment Run

#### Create Profitability Realignment Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this procedure, you create a profitability realignment run, consisting of one or more realignment requests.

Procedure - SAP Fiori

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Realignment - Profitability Analysis (KEND). | The overview screen for CO-PA: Maintain Realignments displays. |  |
| 3 | Create Realignment Run | Choose Realignment Run in the header area to create a new realignment run.Realignment Run Short Text: Enter a description clearly indicating what activities are included in the run.Choose the Accept button to continue. | The newly created run appears in the run hierarchy. |  |
| 4 | Create Realignment Request | Select the realignment run created in the previous step, and then choose the Request option from the header bar to create a new request. | The overview screen for Realignment Request displays, with the Selection Condition tab opened by default. |  |
| 5 | Input Realignment Request Selection Criteria | In Relign. request, enter a description clearly indicating what activities are included in the run.Select CO-PA characteristic Customer (field name KNDNR ) and select the Arrow Down icon to place it into the Selected characteristics table.Char. Value: 33100001 | The table for Selected characteristics displays the following:Fld Name: KNDNRCharac.: CustomerChar. Value: 33100001Name: Domestic UAE Customer 1 |  |
| 6 | Input Conversion Rule Criteria | Choose the ConversRule tab to open the dialog for maintaining the conversion rule for this request.In the Characteristics NOT to be change table, highlight characteristic Customer Group (Field name: KDGRP) and select the side arrow button pointing towards table characteristics to be derived again. | The characteristic Customer Group (Field name: KDGRP) is listed in table Characteristics to be derived again. |  |
| 7 | Save and Exit | Choose the Back button to ensure that the newly created request is listed under the realignment run you created in a previous procedure.Choose the Save button. | The newly created realignment request is listed underneath the realignment run. |  |

#### Execute Profitability Realignment Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this procedure, you execute the realignment run that was created in previous procedures.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Run Realignment - Profitability Analysis (KEND). | The overview for CO-PA: Maintain Realignments displays. |  |
| 3 | Execute Profitability Realignment Run | Select the realignment run created in the previous procedures and then choose Execute in the footer bar .Note The Customer Group of the customer master data must be modified in the Sales and Distribution view. For more information, see the Create Customer Master - MDS (BND) test script for more detailed instructions. | The CO-PA: Maintain Realignments job dialog box appears. |  |
| 4 | Execute Run | Ensure that the job name is correct. Deselect the Test Mode indicator. Choose Accept to execute the run. | The background job was scheduled.You can call up job management from the menu ( Goto > Job overview >).You can release the job to start immediately. To display its current status, choose Refresh status. |  |
| 5 | Verify Run Results | Double-click the executed profitability run to view the details of the run. | The status of the run displays Successful. |  |

#### Analyze Realignment Results

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You run this report to view both the monetary amount of all realignments and the associated journal entry items.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Realignment Results - Profitability Analysis (F2549). | The Realignment Results - Profitability Analysis screen displays. |  |
| 3 | Enter Filter Criteria | From the top of the view, choose the Compact Filter icon.Select the Ledger filter and enter 0L.Select the Realignment Date filter that opens the Define Conditions: Realignment Date dialog box.Choose the calendar icon and select the run date for your realignment and choose OK to close the dialog box.Choose Go to run the report. | The Realigned Journal Entry Items portion of the view is refreshed. |  |

### Analytics

#### Project

##### Project Profitability Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you can monitor profitability information for your project-based services.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Project Profitability Overview (F2794). | The Project Profitability Overview screen displays. |  |
| 3. | Enter Data | Make the following entries and choose Go:Ledger: 0LFinancial Statement Version: YPS2Fiscal Year : <current year>Company Code: 3310 | An overview of different metrics related to the selection criteria displays. |  |

##### Project Profitability

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you can track the profitability of your project-based services.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Project Profitability (W0052). | The Project Profitability screen displays. |  |
| 3. | Enter Data | Make the following entries and choose Go:Financial Statement Version: YPS2Company Code: 3310Ledger: 0LFiscal Year : <current year> | Data for all projects that meet the selection criteria displays |  |

##### Project Financial Booklet - Professional Services

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, the review booklet applications provide a guided margin analysis and various KPIs. You can explore and drill down into your financial data, as well as reveal and understand interdependencies in a conversational style. It combines various analytic views of the project into one report.

This report covers the following:

- Customer Projects (Customer Project Management – Project-Based Services - J11), Project Profile: P001-Customer Project
    - Project Margin Overview
    - Project Billing Element View
    - Project Hour Details
    - Profit Center View
- Internal Projects (Internal Project Management – Project-Based Services - 1A8), Project Profiles: P002-Internal Project
    - Project Actuals
    - Project Plan/Actuals
- Projects with Revenue (Project Control – Sales - 4I9), Project Profile: YP05-Project with Revenue
    - Project Margin Overview
    - Project Billing Element View
- Overhead/Statistical Projects (Project Control – Finance - 1NT), YP03-Overhead Project, YP04-Statistical Project
    - Project Actuals
    - Plan/Actual/Commitments
    - Project Budget/Commitments
- Investment Projects (Project Control – Capital Projects - 35F), YP02-Investment Project
    - Actuals
    - Plan/Actual/Commitments
    - Budget Availability Control

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Project Financial Booklet - Professional Services (F7479). | The Project Financial Booklet - Professional Services view is displayed. |  |
| 3 | Enter Data | Make the following entries and choose Go:Project: <Enter your desired project name>Company Code: 3310Fiscal Year : <current year>Fiscal Period : <current period> | An overview of various metrics related to the selection criteria displays. |  |
| 4 | Select Required Project Type | Based on the scope covered, select one of the following options:Customer Projects (CPM project)Internal ProjectsProject with Revenue (EPMM project)Overhead/Statistical ProjectsInvestment Projects |  |  |

##### Project Financial Booklet - Enterprise Projects

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, the review booklet applications provide a guided margin analysis and various KPIs. You can explore and drill down into your financial data, as well as reveal and understand interdependencies in a conversational style. It combines various analytic views of the project into one report.

This report covers the following:

- Enterprise Projects with Revenue (Project Control – Sales - 4I9), Project Profile: YP05-Project with Revenue
    - Project Margin Overview
    - Project Billing Element View
    - Project Assigned Orders
- Overhead/Statistical Projects (Project Control – Finance - 1NT), YP03-Overhead Project, YP04-Statistical Project
    - Project Actuals
    - Plan/Actual/Commitments
    - Project Budget/Commitments
- Investment Projects (Project Control – Capital Projects - 35F), YP02-Investment Project
    - Actuals
    - Plan/Actual/Commitments
    - Budget Availability Control

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Project Financial Booklet - Enterprise Projects (F8698). | The Project Financial Booklet - Professional Services view is displayed. |  |
| 3 | Enter Data | Make the following entries and choose Go:Project: <Enter your desired project name>Company Code: 3310Fiscal Year : <current year>Fiscal Period : <current period> | An overview of various metrics related to the selection criteria displays. |  |
| 4 | Select Required Project Type | Under Projects with Revenue, select one of the following options:Project Margin OverviewProject Billing Element ViewProject Budget AVCUnder the Overhead/Statistical Projects section, select one of the following options:Project ActualsPlan/Actual/CommitmentsProject Budget/CommitmentsUnder the Investment Projects section, select one of the following options:ActualsPlan/Actual/CommitmentsBudget Availability ControlNote The Project Budget AVC functionality is only available when using the Predictive Commitments Management (2I3). |  |  |

#### Product

##### Product Profitability Review Booklet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can analyze information such as contribution margins for individual products with UCB origin cost breakdown, related product information, and profitability characteristics.

Prerequisite

To view data in COGS Breakdown page scope, Product Cost Breakdown in Plan/Actual Value Flow (7NH) must be activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Product Profitability Review Booklet (F8348). | The Product Profitability Review booklet view displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Ledger: 0LCompany Code: 3310Currency Role Field: <Global Currency>Reporting Date: <current date>Product Sold: <optional>Product Sold Group: <optional>Sales Document: <optional>If these fields aren't visible, choose Adapt Filters and select those from the available options. | The booklet includes multiple pages:Margin Overview: Year-to-Date MarginCOGS Breakdown: Year-to-Date COGS BreakdownThe COGS breakdown is only accurate when using scope Product Cost Breakdown in Plan/Actual Value Flow (7NH). |  |

##### Product Profitability with Production Variances

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you can analyze information such as contribution margins for individual products with related product information and profitability characteristics.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Product Profitability with Production Variances (W0182). | The Product Profitability with Production Variances screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:FSV: YPS2Ledger: 0LCompany Code: 3310Fiscal Year: <current year> | Data for all product groups that meet the selection criteria displays. |  |

#### Service

##### Solution Order Margins

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you can analyze revenue, costs, and contribution margins for individual solution orders across different installation services, or service and maintenance contracts within a region or channel.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Solution Order Margins (F6061). | The Solution Order Margins screen displays. |  |
| 3. | Enter Data | Make the following entries and choose Go:Company Code: 3310Financial Statement Version: YPS2Ledger: 0L | Data for all product groups that meet the selection criteria displays. |  |

##### Service Profitability Review Booklet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

This booklet is designed for the service industry. It supports views of both margins and line items, including actual and plan data. The booklet provides an overview of the market segment, focusing on service orders and service contracts.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Service Profitability Review Booklet (F6600). | The Service Profitability Review Booklet screen displays. |  |
| 3. | Enter Data | Make the following entries and choose Go:Financial Statement Version: YPS2Ledger: 0LCompany Code: 3310 | The service margins overview displays. |  |

#### Market Segments

##### Market Segments Actual Report

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
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Market Segments - Actuals (F0960). | The selection view for Market Segments - Actuals displays. |  |
| 3 | Enter Data | Make the following entries and choose OK:Ledger: 0LLedger Fiscal Year: Current YearFiscal Period: Enter Current PeriodCompany Code: 3310G/L Account Hierarchy: YPS2Key Date: Enter Current Date | The actual figures for market segments display. Gross margin at different segment levels would be shown. |  |

##### Market Segments Actual vs Plan Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you run the market segments actual/plan data reporting.

Prerequisite

You must complete the procedures in Financial Plan Data Upload from File (1HB) test script, to include data in the plan column.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Market Segments - Plan/Actual (New Version) (F9103). | The Market Segment - Plan/Actual screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Ledger: 0LFiscal Year of Ledger: Current YearPlan Category: PLNCompany Code: 3310G/L Account Hierarchy: YPS2Key Date: Enter Current Date | The plan/actual figures for market segments display. |  |

#### Cross-Object Margin Reporting

##### Display Line Items - Margin Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you can view line items that are relevant to margin analysis, such as true account assignment to profitability segments.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Display Line Items - Margin Analysis (F4818). | The Display Line Items - Margin Analysis screen displays. |  |
| 3. | Enter Data | Make the following entries and choose Go:Ledger: 0LCompany Code: 3310Posting Date : <Year to Date>Account Assignment Type : EO | The line items that meet the selection criteria display. |  |

##### Product and Service Margins

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

In this activity, you can analyze revenue, costs, and contribution margins across multiple dimensions such as customer and projects.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Product and Service Margins (New Version) (F9104). | The Product and Service Margins screen displays. |  |
| 3. | Enter Data | Make the following entries and choose Go:Financial Statement Version: YPS2Ledger: 0LCompany Code: 3310Fiscal Year : <current year>Fiscal Period : <current year> | Data for all product groups that meet the selection criteria displays. |  |

##### Company Profitability Review Booklet

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Use

The contribution margin report must include all revenues and costs incurred from product sales, project and service sales.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1. | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2. | Access the SAP Fiori app | Open Company Profitability Review Booklet (Template) (F8300). | The Company Profitability Review Booklet screen displays. |  |
| 3. | Enter Data | Make the following entries and choose Go:Ledger: 0LReporting Date: <Enter current date>Company Code: 3310Financial Statement Version: YPS2If these fields aren't visible, choose Adapt Filters and select those from the available options. | The actual figures for market segments are displayed, showing the gross margin at various segment levels. |  |

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
- see-also :: [[06-management-accounting/2608-master-data-fi-en-xx-119]]
- see-also :: [[06-management-accounting/stammdatenskript-materialstamm-fur-universelle-erlosrealisierung-anleg]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/J55_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 61,652 chars in the whole document
