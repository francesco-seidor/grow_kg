---
id: 06-management-accounting/test-script-event-based-production-cost-posting-3f0-ae-sap-s-4hana-clo
title: "Test Script: Event-Based Production Cost Posting (3F0_AE) - SAP S/4HANA Cloud Public Edition (3F0_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud test script for scope item 3F0_AE: set up and test event-based WIP, variance and overhead posting, manual settlement and cost analytics."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/event-based-production-cost-posting]
aliases: [3F0_S4CLD2608_BPD_EN_AE]
keywords: [Event-Based Production Cost Posting, event-based wip and variance, costing sheets, results analysis keys, product cost collector, manual settlement, event-based posting errors, production cost analytics, non-material settlement, posting rules]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3F0_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-931
topic: 06-management-accounting/event-based-production-cost-posting
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Event-Based Production Cost Posting (3F0_AE) - SAP S/4HANA Cloud Public Edition (3F0_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3F0_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Event-Based Production Cost Posting** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Event-Based Production Cost Posting (3F0_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232852455)

[2 Prerequisites 4](#_Toc232852456)

[2.1 System Access 4](#_Toc232852457)

[2.2 Roles 4](#_Toc232852458)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232852459)

[2.4 Business Conditions 6](#_Toc232852460)

[2.5 Preliminary Steps 7](#_Toc232852461)

[2.5.1 Check/Update Costing Sheet to Event-Based Costing Sheet 7](#_Toc232852462)

[2.5.2 Check/Update Assignment of Costing Sheet to Valuation Variant 9](#_Toc232852463)

[2.5.3 Change Results Analysis Key and Costing Variant Assignment for Order Type 10](#_Toc232852464)

[2.5.4 Update Event-Based WIP and Variance Posting 11](#_Toc232852465)

[2.5.5 Product Cost Collector: Define Cost-Accounting-Relevant Default Values for Order Types and Plants 12](#_Toc232852466)

[2.5.6 Optional: Create/Change Settlement Rule for Non-Material Settlement 13](#_Toc232852467)

[2.5.7 Optional: Overhead Calculation with Origin Group 15](#_Toc232852468)

[2.5.8 Display Posting Rules (Event-Based) 16](#_Toc232852469)

[3 Overview Table 18](#_Toc232852470)

[4 Test Procedures 19](#_Toc232852471)

[4.1 Period-End Closing Activities 19](#_Toc232852472)

[4.1.1 Optional: Run Actual Cost Rate Calculation 19](#_Toc232852473)

[4.1.1.1 Calculate Actual Cost Rates - Cost Centers 19](#_Toc232852474)

[4.1.2 Optional: Run Actual Cost Revaluation on Order 21](#_Toc232852475)

[4.1.2.1 Optional: Execute Order Revaluation at Actual Cost 21](#_Toc232852476)

[4.1.3 Postprocess Event-Based Order Exception 22](#_Toc232852477)

[4.1.3.1 Postprocess Event-Based Postings - Product Costing 22](#_Toc232852478)

[4.1.3.2 Optional: Event-Based Solution Monitor - Product Costing 24](#_Toc232852479)

[4.1.3.3 Optional: Manage Event-Based Posting Errors - Product Costing 25](#_Toc232852480)

[4.1.4 Optional: Run Manual Order Settlement 26](#_Toc232852481)

[4.1.4.1 Optional: Execute Manual WIP and Variance Settlement 26](#_Toc232852482)

[4.2 Analytics 27](#_Toc232852483)

[4.2.1 Insights 27](#_Toc232852484)

[4.2.1.1 Event-Based Production Accounting Overview 27](#_Toc232852485)

[4.2.2 Summarized Analytics 29](#_Toc232852486)

[4.2.2.1 Analyze Event-Based Production Cost Summarization 29](#_Toc232852487)

[4.2.3 Order Analytics 30](#_Toc232852488)

[4.2.3.1 Analyze Event-Based Production Costs 30](#_Toc232852489)

[4.2.3.2 Analyze Event-Based Order Costs 31](#_Toc232852490)

[4.2.3.3 Optional: Analyze Event-Based Product Cost Collector Details 32](#_Toc232852491)

[4.2.3.4 Display Line Items - Production Accounting 34](#_Toc232852492)

[4.2.3.5 Event-Based Work in Process 34](#_Toc232852493)

[4.2.4 Work Center/Operation Analytics 36](#_Toc232852494)

[4.2.4.1 Analyze Costs by Work Center/Operation 36](#_Toc232852495)

[5 Appendix 38](#_Toc232852496)

[5.1 Situation Handling 38](#_Toc232852497)

[5.1.1 Manage Situation Types 38](#_Toc232852498)

[5.1.2 Manage Teams and Responsibilities 39](#_Toc232852499)

[5.1.3 Finishing Up the Situation Type 40](#_Toc232852500)

## Purpose

Overview

This scope item updates calculations for work-in-process, overhead, and variance by linking postings to specific events. These events can include goods issues, activity confirmations, goods receipts, or manually set technically complete orders within both make-to-stock and make-to-order scenarios. Additionally, it addresses variance by category when the order status is either fully delivered or technically complete. The supported variance categories are input quantity variance, input price variance, output price variance, resource usage variance, lot size variance, and remaining variance.

|  |
| --- |
| Note This scope item supports event-based production cost posting for make-to-stock and make-to-order scenario (valuated sales order stock). Follow this script to complete the setup on the logistic side to make sure the end-to-end process runs smoothly. The same order type cannot be used for event-based and periodic closing. |

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

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log on |
| --- | --- | --- | --- | --- |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Business Process Specialist | SAP_BR_BUSINESS_PROCESS_SPEC | Business Process Management / Business Process Management | SAP_BR_BUSINESS_PROCESS_SPEC / SAP_CA_SPT_BPS_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Controlling Area | A000 |  |  |
| Company Code | 3310 |  |  |
| Plant | 3310 |  |  |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 3KW | Create CO Cost Rates - MDS |

### Business Conditions

Before this scope item can be tested, one of the following business conditions must be met.

|  |
| --- |
| Note The default content is based on event-based result analysis. |

|  |
| --- |
| Note This scope item covers all manufacturing orders, process order, product cost collector including non-material settlement to cost centers, event-based order and WBS elements, and split valuations. |

| Scope Item | Business Condition |
| --- | --- |
| BJ5 - Make-to-Stock Production – Discrete Manufacturing orBJ8 - Make-to-Stock – Process Manufacturing Based on Process Order or3L7 - Make-to-Stock with Co- and By-Products – Process Manufacturing or1BM - Make-to-Order Production – Semifinished Goods Planning and Assembly or1YT - Make-to-Order Production with Variant Configuration orBJE - Make-to-Order Production – Finished Goods Sales and Final Assembly or2UG - Make-to-Stock – Process Manufacturing Based on Production Order orBJN - Rework Processing – Stock-Manufactured Material or42N - Tank Trailer Filling with Residuals or3OK - Make-to-Order Production – Process Manufacturing or21D - Make-to-Stock Production with Variant Configuration or31L - Production Capacity Evaluation or4B5 - Predictive Material and Resource Planning or4B4 - Material Replenishment with Kanban – Stock Transfer or3UK - Inbound Storage Tank Management – Process Manufacturing or3UL - Make-to-Stock with Silo Material – Process Manufacturing orBJH - Make-to-Stock Production – Repetitive Manufacturing or1E3 - Material Replenishment with Kanban – External Procurement or4B3 - Material Replenishment with Kanban – In-House Production or6GD - Engineer Products and Systems – Project with Production or7TO - Production Order Combination | At least one of these scripts must be executed for this test.Note Analyze Event-Based Product Cost Collector Details step is relevant only for Repetitive Manufacturing: Product Cost Collector. As a prerequisite, you must execute one of the following: BJH - Make-to-Stock Production – Repetitive Manufacturing, 1E3 - Material Replenishment with Kanban – External Procurement, 4B3 - Material Replenishment with Kanban – In-House Production. |

### Preliminary Steps

#### Check/Update Costing Sheet to Event-Based Costing Sheet

Purpose

It is mandatory that event-based RA key uses event-based costing sheet. As costing sheets are assigned to valuation variant, in default content, event-based costing sheet XXXXEP (where XXXX represent your country's company code) is assigned to costing variant PYR1 and PYR2 with event-based results analysis key RSEBW.

|  |
| --- |
| Note If you want to change the costing sheet assigned to valuation variant used in event-based, make sure that the costing sheet assigned is always marked as event- based. This step is only relevant if you want to check or update the default costing sheet for event-based. Change of existing costing sheet from event based to non-event based and vice versa are not supported. |

|  |
| --- |
| Note Run actual cost revaluation on orders must be used only if you plan to revalue manufacturing orders based on actual activity prices (optional step). This functionality cannot be used together with a percentage‑based overhead rate key that is calculated on a base G/L account with cost element category 43 (internal activity allocation), as this would result in a recursion.For example, in the default cloud content, base Y002 (Production) is mapped to cost element group 4500_CE, which includes G/L accounts with cost element category 43 and is therefore incompatible with the percentage‑based overhead key YOH2. In this case, replace the percentage‑based overhead key YOH2 with the quantity‑based overhead key YOQ2 for the event‑based costing sheet XXXXEP.Maintain the overhead rate for YOQ2 via the Define Costing Sheets (102922) SSCUI. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Product Costing

1. For the row with Item Name of Product Cost Planning, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Define Costing Sheets row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Costing Sheets activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Check or Create Costing Sheet | Make sure that the costing sheet XXXXEP is marked as Event- Based. | If you want to create your own costing sheet, use this costing sheet XXXXEP for copying.Note You must select Event- Based selected for this scope item.Note You can use origin group in costing sheet base via configuration activity Define Origin Groups based on the configuration environment. |  |

#### Check/Update Assignment of Costing Sheet to Valuation Variant

Purpose

It is mandatory that event-based RA key uses event-based costing sheet. As costing sheets are assigned to valuation variant, in default content, event-based costing sheet XXXXEP (where XXXX represent your country's company code) is assigned to costing variant PYR1 and PYR2 with event-based results analysis key RSEBW.

|  |
| --- |
| Note If you want to change the costing sheet assigned to valuation variant used in event-based, make sure that the costing sheet assigned is always marked as Event- Based. This step is only relevant if you want to check or update the default costing sheet for Event-Based. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Define Valuation Variants per Plant (102608).
6. For the displayed row, choose Details (>).
7. For the Define Valuation Variants per Plant row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Valuation Variants per Plant activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Select the Plant and Valuation Variant | Select the plant and valuation variant. Choose Details and the Overhead tab. |  |  |
| 2 | Check or Assign Costing Sheet | Make sure that the costing sheet XXXXEP or the new event-based costing sheet is assigned. | It is mandatory to have Event- Based selected for this scope item. |  |

#### Change Results Analysis Key and Costing Variant Assignment for Order Type

Purpose

In the activity, you can check the RA Key assignment is to RSEBW - Event Based WIP and Variance Posting for the selected combination of plant and order type.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. If you are working with production orders, search for Define Order-Type-Dependent Parameters for Production Orders (102431). If you are working with process orders, search for Define Order-Type-Dependent Parameters for Process Orders (102810).
6. For the displayed row, choose Details (>).
7. For the Define Order-Type-Dependent Parameters for Production Orders row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Order-Type-Dependent Parameters for Production Orders activity if you are working with production orders. If you are working with process orders, search for Define Order-Type-Dependent Parameters for Process Orders.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Change Entry of the identified combination | Select the entry with plant 3310 and any of the following production/process order types: YBM1, YBM2, YBM3, YBM4, YBM5, YBM9, YBW1, YPK1, YQ01, YQ02, YQ10 (based on your scope requirement) and choose Details on the top menu. | The “Change View“Order Type-Dependent Parameters: Overview”: Details” view displays. |  |
| 2 | Change the RA Key Assignment | Make the following entries:Event-Based Result Analysis Key: <Double-click to select RSEBW>Note Using the dropdown to enter or make the selection will not work. You must double-click in the field to select the value RSEBW.Note This scope item now supports manual settlement with the new RA key ORDMS-Manufacturing Order Manual Settlement. Work in progress and variance are posted periodically (instead of event-based) via a month-end manual run of the job template (see [Optional: Execute Manual WIP and Variance Settlement](#unique_10) [page ] 26 step in this document).Prel./Vers.Cstg: PYR1Simul. Costing: PYR2Save the entries. | The RA key and costing variant have been changed from WIP periodic cost MBMF01 to event-based WIP and variance.Event-based production cost posting supports all orders with order type categories 10 and 40. Standard order types that you can change via this step to event-based is YBM1, YBM2, YBM3, YBM4, YBM5, YBM9, YBW1, YPK1, YQ01, YQ02 and YQ10.Note Event-based overhead must only be used with event-based WIP and variance scope. If not, this would lead to inconsistent and incorrect data. The predelivered costing variants PYR1 and PYR2 come with event-based costing sheet 1010EP. |  |

#### Update Event-Based WIP and Variance Posting

Purpose

In the activity, you can update the configuration relating to event-based WIP and variance.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Make the following entries:

Application Area: Finance

Sub Application Area: Product Costing

1. For the row with Item Name of Product Cost Planning, choose Details (>).
2. For the displayed row, choose Details (>).
3. For the Event-Based WIP and Variance Posting row, choose Configure.
4. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Event-Based WIP and Variance Posting activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Define Event-Based WIP and Variance Posting | For the displayed row, choose RA Key RSEBW, update WIP source G/L and WIP account determination. For details, go [here](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4032610758dc437089f0c28320eec93f/a2ec447cc4174e8abce148dc9ed0fe44.html). |  |  |

#### Product Cost Collector: Define Cost-Accounting-Relevant Default Values for Order Types and Plants

Purpose

In the activity, you can check the RA Key assignment is to PCCEB - PCC Order EB Key for the selected combination of plant and Product Cost Collector (PCC) order type (category 5).

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. If you are working with production orders, search for Define Cost-Accounting-Relevant Default Values for Order Types and Plants (106081).
6. For the displayed row, choose Details (>).
7. For the Define Cost-Accounting-Relevant Default Values for Order Types and Plants row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Cost-Accounting-Relevant Default Values for Order Types and Plants activity if you are working with production orders.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Change Entry of the identified combination | Select the entry with plant 3310 and order type YBMR (based on your scope requirement) and choose Details on the top menu. | The “Change View“Define Cost Accounting Relevant Default Val”: Details view displays. |  |
| 2 | Change the RA Key Assignment | Make the following entries:Event-Based Result Analysis Key: <Double-click to select PCCEB>Note Using the dropdown to enter or make the selection will not work. You must double-click in the field to select the value PCCEB.Note This scope item now supports manual settlement with the new RA key PCCMS - Product Cost Collector Manual Settlement. Work in progress and variance are posted periodically (instead of event-based) via a month-end manual run of the job template (see [Optional: Execute Manual WIP and Variance Settlement](#unique_10) [page ] 26 step in this document).Prel./Vers.Cstg: PERMSimul. Costing: EYRMSave the entries. | If you want to use event-based feature for PCC, you must update RA key and costing variants from periodic to event-based.Event-based production cost posting now supports orders with order type category 5.Product cost collector scenario is supported.Note Event-based overhead must only be used with event-based WIP and variance scope. If not, this would lead to inconsistent and incorrect data. The predelivered costing variants PERM and EYRM come with event-based costing sheet 1010EP. |  |

#### Optional: Create/Change Settlement Rule for Non-Material Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you create the default settlement receiver as cost center or WBS element for event-based production orders/process orders that are not settled to materials. You can change the default settlement rule receiver from material to cost center, WBS element and order (maintenance or production order). All event-based production orders/process orders are settled to materials until you specifically change the receiver object.

|  |
| --- |
| Note Settlement rule must be set before any posting is done on production orders. |

|  |
| --- |
| Note You can now configure the non-material account determination rule to settle production orders. Settlement is done either via the origin cost element (default) or via assigned source accounts (using SSCUI 103940). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Production Order (CO01) (or Create Process Order (COR1) as a Production Supervisor - Process Manufacturing if you want to create a process order). | The Production Order Create: Initial Screen displays. |  |
| 3 | Change | Choose More > Order > Change. | The Production Order Change: Initial Screen displays. |  |
| 4 | Enter Order | Enter the order that you want to edit and choose Order Header. | The Production Order Change: Header displays. |  |
| 5 | Maintain Settlement Rule | In the following screen, choose More > Header > Settlement Rule. | The Event-Based Posting Rules screen displays. |  |
| 6 | Enter Posting Rule | Under the Posting Rule section, choose Create. Make the following entries and choose Apply:Category: Cost CenterReceiver: Any Cost Center or WBS Element within same company code as production order (intercompany settlement will not be supported currently)Percentage: 100%Settlement rules are common for all the standard ledgers and not different by Ledger. | Important notes on Non-MAT receivers:• Either 100% to MAT or 100% to non-MAT is allowed, mix-usage of MAT and non-MAT as receiver is not allowed.• Only one non-MAT receiver category is allowed, mix-usage of cost center, WBS element and order is not allowed.• Do NOT assign cost center that has subsequent activity confirmation as receiver, especially do NOT assign production activity confirmation related cost center as receivers. |  |
| 7 | Save | Press Enter and go back to save the entries. |  |  |

#### Optional: Overhead Calculation with Origin Group

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

You can have different overhead rates for different materials. In this step, you can change default costing sheet to costing sheet with origin groups.

Overhead-based origin groups are supported in standard cost and production orders in target cost and variance calculation of overhead costs for this scope item.

Prerequisites

1. Edit costing X0OG sheet to assign cost center for credit key XC1 and XC2 as per your company codes.

2. In standard content demo data test, test material used is FG126.

Assign origin group Y10 to material RM122, RM128 and RM120 via Material Master app in costing 1 view.

Assign origin group Y20 to material RM20 and RM27 via Material Master app in costing 1 view.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Order screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. In the Area of Responsibility dialog box, choose Production Supervisor. Check if the following displays and choose OK:Plant 1AE (3310)MTS DI - Valuated (YB1)Choose + to select this entry if not displayed; choose the Delete button to remove any other plant entries. Choose OK. |  |  |
| 4 | Select and Check Details of Production Order | On the Manage Production Orders screen, choose Adapt Filters to display more filter options. In the Adapt Filters dialog box, choose More filters. Select Material and Production Plant and choose OK. Choose Go.Enter the following filter criteria, and choose Go:Status: CreatedMaterial: <your production order>Production Plant: 3310Select the order that you want to edit. | The Material and Production Plant fields are added to filter bar.The searched order displays. |  |
| 5 | Change Default Costing Sheet | Select Control and change costing sheet to X0OG. | Note You can create your own costing sheet via the Define Costing Sheets (102922) SSCUI. You can also create origin group in costing sheet base via the Define Origin Groups (103143) SSCUI. |  |

#### Display Posting Rules (Event-Based)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With this app, you can view the posting rules for event‑based manufacturing orders (production orders and process orders) as well as event‑based repetitive manufacturing orders (product cost collectors). You can use the app to review details such as the distribution method applied and the allocation of costs per receiver. When you access the app from the order header in the Change Production Order app, you can create and edit posting rules for event‑based manufacturing orders. Editing posting rules for product cost collectors, however, is not supported in this app.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Posting Rules - Event-Based (F5228). | The Display Posting Rules - Event -Based screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Plant: 3310Order Type: <YBM1, for example>Order Category: 10Order ID: <Enter an order ID> | A list of production orders displays. |  |
| 4 | Select Order | Select the order from the list.You can then edit the posting rule in the Display Posting Rules - Event-Based (F5228) . You can change the distribution method using the dropdown list, add non‑material receivers (such as a cost center or WBS element) using the Create button, or update the equivalences or percentages directly in the table. | You can change the posting rule for order. |  |

## Overview Table

This scope item consists of several process steps provided in the following table:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step, Report or Item | Business Role | App Name | Expected Results |
| --- | --- | --- | --- |
| [Calculate Actual Cost Rates - Cost Centers](#unique_17) [page ] 19 | Cost Accountant - Overhead | Run Actual Cost Rate Calculation - Cost Center (New Version) (F9080) |  |
| [Optional: Execute Order Revaluation at Actual Cost](#unique_18) [page ] 21 | Cost Accountant - Production | Schedule Product Costing Jobs (F3683) |  |
| [Postprocess Event-Based Postings - Product Costing](#unique_19) [page ] 22 | Cost Accountant - Production | Postprocess Event-Based Postings - Product Costing (F3669) |  |
| [Optional: Event-Based Solution Monitor - Product Costing](#unique_20) [page ] 24 | Cost Accountant - Production | Order Exception Monitor - Event-Based (F5133) |  |
| [Optional: Manage Event-Based Posting Errors - Product Costing](#unique_21) [page ] 25 | Cost Accountant - Production | Manage Product Costing Errors (F5132) |  |
| [Optional: Execute Manual WIP and Variance Settlement](#unique_10) [page ] 26 | Cost Accountant - Production | Schedule Product Costing Jobs (F3683) |  |
| [Event-Based Production Accounting Overview](#unique_22) [page ] 27 | Cost Accountant - Production | Production Cost Overview - Event-Based (F6248) |  |
| [Analyze Event-Based Production Cost Summarization](#unique_23) [page ] 29 | Cost Accountant - Production | Production Cost Summarization - Event-Based (F7311) |  |
| [Analyze Event-Based Production Costs](#unique_24) [page ] 30 | Cost Accountant - Production | Analyze Production Costs - Event-Based (F4059) |  |
| [Analyze Event-Based Order Costs](#unique_25) [page ] 31 | Cost Accountant - Production | Order Cost Details - Event-Based (F4254) |  |
| [Optional: Analyze Event-Based Product Cost Collector Details](#unique_26) [page ] 32 | Cost Accountant - Production | Product Cost Collector Details - Event-Based (F6965) |  |
| [Display Line Items - Production Accounting](#unique_27) [page ] 34 | Cost Accountant - Production | Display Line Items (F7288) |  |
| [Event-Based Work in Process](#unique_28) [page ] 34 | Cost Accountant - Production | Work in Process - Event-Based (F3498) |  |
| [Analyze Costs by Work Center/Operation](#unique_29) [page ] 36 | Cost Accountant - Production | Analyze Costs by Work Center/Operation (F3331) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Period-End Closing Activities

#### Optional: Run Actual Cost Rate Calculation

##### Calculate Actual Cost Rates - Cost Centers

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you calculate the actual cost rate of activities. This is done by dividing the actual costs posted to a cost center by the actual quantity consumed in that cost center.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Run Actual Cost Rate Calculation - Cost Center (New Version) (F9080). | The Run Actual Cost Rate Calculation - Cost Centers (New Version) view displays. |  |
| 3 | New Run | Choose the Create New Run button. | The Create New Run dialog box displays. |  |
| 4 | Cost Center Group | Make the following entries and choose the Create New Run button:Run Name: <enter a run name>Cost Center Group: 3310130Ledger: 0LNote Rates must be calculated for each ledger separately, for example, first with 0L and repeat the steps with any other standard ledgers you have such as 2L and 3L.Company Code: 3310Fiscal Year: <enter a year>From Fiscal Period: <Current period, for example 5>To Fiscal Period: <Current period, for example 5>Test Run: NoUpdate Despite Errors: YesCalculation Method: Periodic priceNote Periodic and cumulative price options are supported. Average price is not used in actual costing. | The actual activity prices are calculated. |  |

|  |
| --- |
| Note Alternatively, you can use the Schedule Overhead Accounting Jobs (F3767) app and the Actual Cost Rate Calculation template, or the Actual Cost Rate Calculation - Cost Centers (KSII) app for actual cost rate calculation.You can then use the calculated actual cost rate to revaluate activities in CKMLCP (Edit Actual Costing Runs) at period end. Alternatively, you can revaluate activities at the level of manufacturing orders by using the Run Revaluation at Actual Cost Rates - Order and PCC job in Schedule Product Costing Jobs (F3683). To revaluate on order level, you must request expert configuration to switch the activity update method. |

#### Optional: Run Actual Cost Revaluation on Order

##### Optional: Execute Order Revaluation at Actual Cost

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can update order costs based on actual activity prices instead of planned rates.

|  |
| --- |
| Note Run actual cost revaluation on orders must be used only if you plan to revalue manufacturing orders based on actual activity prices (optional step). This functionality cannot be used together with a percentage‑based overhead rate key that is calculated on a base G/L account with cost element category 43 (internal activity allocation), as this would result in a recursion.For example, in the default cloud content, base Y002 (Production) is mapped to cost element group 4500_CE, which includes G/L accounts with cost element category 43 and is therefore incompatible with the percentage‑based overhead key YOH2. In this case, replace the percentage‑based overhead key YOH2 with the quantity‑based overhead key YOQ2 for the event‑based costing sheet XXXXEP.Maintain the overhead rate for YOQ2 via the Define Costing Sheets (102922) SSCUI. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Product Costing Jobs (F3683). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job view displays. |  |
| 4 | Enter Selection Criteria | In the Template Selection section, make the following entries:Job Template: SAP_FIN_CO_RTPC_ORDER_REVALJob Name: Activity Type Revaluation at Actual Prices: Event-Based OrderChoose Step 2. | The Scheduling Options view displays. |  |
| 5 | Scheduling Options | Select Start Immediately checkbox and choose Step 3. | The Parameters view display. |  |
| 6 | Parameters | Make the following entries and choose the Execute button:Ledger: 0LPlant: 3310Period: <enter a period>Fiscal Year: <enter a year>Test Run: Deselect |  |  |
| 7 | Schedule Job | Choose the Schedule button. |  |  |

#### Postprocess Event-Based Order Exception

##### Postprocess Event-Based Postings - Product Costing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run the report to review and inspect if there is any error or manual additional posting for the event-based WIP, variance and unsettled costs to receivers other than MAT. This step is executed in the same manner for partially delivered production orders and for (totally) delivered production orders.

|  |
| --- |
| Note If you use the RA key ORDMS - Manufacturing Order Manual Settlement or PCCMS - Product Cost Collector Manual Settlement, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Postprocess Event-Based Postings - Product Costing (F3669). | The Postprocess Event-Based Postings - Product Costing screen displays. |  |
| 3 | Enter Selection Parameters | Make the following entries:Posting Date: <Keep the default (the current period-end date of leading ledger)>Company Code: 3310Plant: 3310Order:<Enter the order number you created in one of the scope items under Business Conditions or leave it blank to get the list of applicable orders.>Order Type: <Any order type supported with order type categories 10 and 40, for example, YBM1 and YBM2> |  |  |
| 4 | Postprocess Event-Based Postings - Product Costing | Choose the Go button.At the bottom of the screen:Choose the Orders to Post tab. For orders with no simulation run, select the order and choose Simulate Posting. For orders with Order simulation posted successfully, to post the WIP/variance/overhead, choose the Post WIP/Variance button.Choose the Posted Orders tab. A list of posted orders displays. | For goods issued via the bill of material and routing confirmation, WIP entries are posted automatically with real time WIP. But certain other postings on production order like posting via direct purchase order or FI posting do not trigger automatic WIP. This app shows you posting on production order which do not result in automatic WIP posting. For such postings that are WIP-relevant, you can trigger the WIP posting via this app. This app also shows if event-based WIP did not get posted due to some missing GL in customizing (works as monitor), you can then repost after the fix.For final delivered order from goods receipt or technically completed orders, variance entries are posted automatically with event-based variance posting. But certain other postings on production order (DLV, TECO) such as posting via direct purchase order and FI posting do not trigger automatic event-based variance posting. This app shows you posting on production order which do not result in automatic WIP posting. For such postings that are variance-relevant, you can trigger the variance posting in terms of order status via this app. This app also shows if event-based variance did not get posted due to errors occured (works as monitor), you can then repost after the fix.Variances are posted as cost variance without variance categories split. You can go to Event-Based Production Costs and Event-Based Order Costs for variance values per categories. |  |

|  |
| --- |
| Note Alternatively, you can use the Schedule Product Costing Jobs (F3683) app and run the job Postprocess Event-Based Postings - Product Costing (SAP_FIN_CO_RTPC_INSPECTOR). |

##### Optional: Event-Based Solution Monitor - Product Costing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This step works as central monitoring for all event-based orders.

|  |
| --- |
| Note If you use the RA key ORDMS - Manufacturing Order Manual Settlement or PCCMS - Product Cost Collector Manual Settlement, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Order Exception Monitor - Event-Based (F5133). | The Event-Based Solution Monitor view displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Posting Date/Key Date: <MM/YYYY>Ledger: <keep this field blank>Company Code: 3310Plant: 3310 | This report provides an overview of errors to reprocess and orders to post. |  |

##### Optional: Manage Event-Based Posting Errors - Product Costing

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run this app to review and reprocess objects by Ledger once you fix the root cause of the error.

|  |
| --- |
| Note If you use the RA key ORDMS - Manufacturing Order Manual Settlement or PCCMS - Product Cost Collector Manual Settlement, you can skip this step. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Product Costing Errors (F5132). | The Manage Event-Based Posting Errors view displays. |  |
| 3 | Enter Selection Parameters | Make the following entries and choose Go:Ledger: <keep this field blank>Company Code: 3310 | At the bottom of the screen, the event-based WIP report analysis comes up with the selected orders. It shows all the orders with event-based posting errors which you can then reprocess. This report includes errors with event-based overhead, WIP, and variance. |  |

#### Optional: Run Manual Order Settlement

##### Optional: Execute Manual WIP and Variance Settlement

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This step is required only if you map the RA key ORDMS- Manufacturing Order Manual Settlement or PCCMS- Product Cost Collector Manual Settlement in the order type.

|  |
| --- |
| Note To execute this step, you must create the production order via scope Make-to-Stock Production – Discrete Manufacturing (BJ5) with the RA key ORDMS (manual settlement) instead of RSEBW (event-based default). You can replace the RA key with ORDMS during production order creation. Alternatively, if you always want to settle manually, you can update the RA key from RSEBW to ORDMS in the order type via SSCUI 102431. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Product Costing Jobs (F3683). | The Application Jobs screen displays. |  |
| 3 | Create | Choose the Create button. | The New Job view displays. |  |
| 4 | Enter Selection Criteria | In the Template Selection section, make the following entries:Job Template: Manual Settlement: Event-Based Order and PCCJob Name: Manual Settlement: Event-Based Order and PCCChoose Step 2. | The Scheduling Options view displays. |  |
| 5 | Scheduling Options | Select Start Immediately checkbox and choose Step 3. | The Parameters view display. |  |
| 6 | Parameters | Make the following entries:Posting Date: <keep the default (it is the current period-end date of leading ledger)>Company Code: 3310Plant: 3310Order Category: <select an order category>Order Type: <select an order type>Order: <if you want to execute only orders that you created with RA key ORDMS OR PCCMS>Process OptionsTest Run: DeselectProcessing OptionsPost Order: SelectTest Run: Deselect | The figures for projects display. |  |
| 7 | Schedule Job | Choose the Schedule button. | WIP or variance is posted as per order status. |  |

### Analytics

#### Insights

##### Event-Based Production Accounting Overview

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you should be able to access key information and KPIs within the production accounting area and gain insight into current trends.

After the rework process is finished, the related cost information can be monitored based on a central Event-Based Production Cost Overview which provides, among others, access to key information and KPIs within the production accounting area and insight into current trends.

For further detailed event-based insights or error handling and monitoring the scope item, 3F0 Event-Based Production Cost Posting can be referred.

|  |
| --- |
| Note If you use the RA key ORDMS - Manufacturing Order Manual Settlement or PCCMS - Product Cost Collector Manual Settlement, report key figures and numbers are not updated in an event-based manner but through a manual run of the job template, as described in the [Optional: Execute Manual WIP and Variance Settlement](#unique_10) [page ] 26 step of this document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Production Cost Overview - Event-Based (F6248). | The Event-Based Production Accounting Overview view displays. |  |
| 3 | Enter Selection Parameters | Make the following entries:Fiscal Period From: <Current date>Fiscal Period To: <Current date>Ledger: 0LCurrency Type: <for example, 10>Company Code: 3310Currency: AEDPlant: 3310Order Type: <Enter any order type that is supported, for example YBM1>Order: <Enter the order number you created in one of the scope items under Business Conditions or leave it blank to get the list of applicable orders> |  |  |
| 4 | View Event-Based KPIs | Choose the Go button. | Key highlights:• Production volume per product: The card lists products with actual and planned quantities, it is sorted from the highest actual quantity for selected filters. Clicking the header of the card takes you to Event-Based Production Costs app.• Variances overview: The card presents chart with all supported variances that are split by Plant in default view, but you could change it to view by Product, Profit Center, Product Group, Storage Location. Clicking the header of the card takes you to Event-Based Production Costs app.• Total Production Costs: The card shows chart with Total Actual costs compared to Total Plan Costs. Default view is by Plant, but you could change it the same way as before. Clicking the header of the card takes you to Event-Based Production Costs app.• WIP overview: The card shows Total Work in Process as of last date of fiscal period selected in the Fiscal Period To field. In case it is current month, the key date is set to today. You can change the default view by Plant to any other perspective as for the other cards. The card navigates to Event-Based Work in Process app.• Quick Links: The card provides links to other event-based reporting apps. |  |

#### Summarized Analytics

##### Analyze Event-Based Production Cost Summarization

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run the report to display a list of all order types for a particular cost.

|  |
| --- |
| Note Data collection for summarization hierarchy is not required for this business process. |

|  |
| --- |
| Note If you use the RA key ORDMS - Manufacturing Order Manual Settlement or PCCMS - Product Cost Collector Manual Settlement, report key figures and numbers are not updated in an event-based manner but through a manual run of the job template, as described in the [Optional: Execute Manual WIP and Variance Settlement](#unique_10) [page ] 26 step of this document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Production Cost Summarization - Event-Based (F7311). | The Production Cost Summarization - Event-Based screen displays. |  |
| 3 | Enter Selection Parameters | Make the following entries and choose Go:Fiscal Period From: <Enter the current period>Fiscal Period To: <Enter the current period>Ledger: 0LCompany Code: 3310Currency: <Use the dropdown to select currency based on ledger and company code>Plant: 3310Order Type: <Select an order type, for example, YBM1> | Summarization of all production costs incurred during the period displays by G/L account. |  |
| 4 | View Details | Expand any G/L account and click to view the list of all orders. | You can see a list of all order types for a particular cost. |  |

#### Order Analytics

##### Analyze Event-Based Production Costs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This step allows you to analyze production costs in real time.

|  |
| --- |
| Note For detailed information on reports, see [here](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4032610758dc437089f0c28320eec93f/7907ffc9fef14500912e933cffa2b814.html?state=DRAFT). |

|  |
| --- |
| Note If you use the RA key ORDMS - Manufacturing Order Manual Settlement or PCCMS - Product Cost Collector Manual Settlement, report key figures and numbers are not updated in an event-based manner but through a manual run of the job template, as described in the [Optional: Execute Manual WIP and Variance Settlement](#unique_10) [page ] 26 step of this document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Analyze Production Costs - Event-Based (F4059). | The Event-Based Production Costs screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Fiscal Period From: <enter period>Fiscal Period To: <enter period>Currency: AEDCompany Code: 3310 | A list of production orders displays. |  |
| 4 | Select Order Details | Select the order number and choose More Links. | The options to view more detailed information regarding the order are displayed. |  |

##### Analyze Event-Based Order Costs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity allows you to analyze event-based orders. You can see details of selected order from all possible perspectives, including event-based work in process.

|  |
| --- |
| Note Real-time production cost supports the following categories of variance: Input Quantity Variance, Input Price Variance, Resource Usage Variance, Lot Size Variance, and Remaining Variance. All the variances are posted on same G/L but a new field SLA Line Type help differentiate variance categories: 9130 (input price var), 9131 (input quantity var), 9132 (resource usage var), 9139 (lot-size var), 9140 (remaining var); field origin cost center, origin cost center activity type implies where the variance happens. When you click on Display Line Items in General Ledger, you would see a new field with these categories. |

|  |
| --- |
| Note If you use the RA key ORDMS - Manufacturing Order Manual Settlement or PCCMS - Product Cost Collector Manual Settlement, report key figures and numbers are not updated in an event-based manner but through a manual run of the job template, as described in the [Optional: Execute Manual WIP and Variance Settlement](#unique_10) [page ] 26 step of this document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access App | Open Order Cost Details - Event-Based (F4254). | The Event-Based Order Costs screen displays. |  |
| 3 | View Event-Based Order Costs Details | Make the following entries and choose Go:Order:<your order>Plant: 3310 | The screen provides an overview of production orders showing target and actual costs. |  |

##### Optional: Analyze Event-Based Product Cost Collector Details

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This step allows you to analyze product cost collector cost with event-based orders.

|  |
| --- |
| Note For detailed information on reports, see [here](https://help.sap.com/docs/SAP_S4HANA_CLOUD/4032610758dc437089f0c28320eec93f/6979c7f10b944e1bbc1e0da734e63536.html). |

|  |
| --- |
| Note This report is relevant only for Repetitive Manufacturing : Product Cost Collector. |

|  |
| --- |
| Note If you use the RA key ORDMS - Manufacturing Order Manual Settlement or PCCMS - Product Cost Collector Manual Settlement, report key figures and numbers are not updated in an event-based manner but through a manual run of the job template, as described in the [Optional: Execute Manual WIP and Variance Settlement](#unique_10) [page ] 26 step of this document. |

Prerequisite

You must execute one of the following scripts:

BJH - Make-to-Stock Production – Repetitive Manufacturing

1E3 - Material Replenishment with Kanban – External Procurement

4B3 - Material Replenishment with Kanban – In-House Production

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Product Cost Collector Details - Event-Based (F6965). | The Event-Based Product Cost Collector Details screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Ledger: <for example, 0L>Plant: 3310Product Cost Collector: <enter period> ORProduction Process: <Use the input help to select a product process> | A list of production orders displays. |  |
| 4 | Select Order Details | Select the order number and choose the > button. | The options to view more detailed information regarding the order are displayed. |  |

##### Display Line Items - Production Accounting

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

With this app, you can display line items in production accounting. You can filter, sort, and group the items based on various criteria. By default, the line items are grouped by order, but you can create your own variants to suit your business needs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Line Items (F7288). | The Display Line Items - Production Accounting screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Ledger: 0LCompany Code: 3310Order Category: <defaulted as 05, 10 and 40>Order ID: <enter an order ID>Business transaction type: <EBWP, for example or SLA Line item type>Select a line item and use Line Item Details to display additional information. | A list of production orders displays. |  |

##### Event-Based Work in Process

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you run the report to review event-based WIP and variance. This step is executed in the same manner for partially and totally delivered production orders.

|  |
| --- |
| Note Event-based WIP is posted by Ledger. So if you have any other standard ledgers like 2L OR 3L, you can execute the report for each ledger to review the WIP. |

|  |
| --- |
| Note The Display Journal Entries - In T-Account View (F3664) and Display Document Flow (F3665) apps that are part of the General Ledger Accountant role can be used to review the WIP and variance posted with goods issue, goods receipt, and activity confirmation of orders. |

|  |
| --- |
| Note If you use the RA key ORDMS - Manufacturing Order Manual Settlement or PCCMS - Product Cost Collector Manual Settlement, report key figures and numbers are not updated in an event-based manner but through a manual run of the job template, as described in the [Optional: Execute Manual WIP and Variance Settlement](#unique_10) [page ] 26 step of this document. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Work in Process - Event-Based (F3498). | The Event-Based Work in Process view displays. |  |
| 3 | Enter Selection Parameters | Make the following entries:Key Date: <Current date>Ledger: 0LCompany Code: 3310Currency: AEDPlant: 3310Order Type: <Enter any order type that is supported, for example YBM1>Order: <Enter the order number you created in one of the scope items under Business Conditions or leave it blank to get the list of applicable orders.> |  |  |
| 4 | Run the Event-Based Work in Process | Choose the Go button. | The production order does not display on the result list in the following cases:technically completed (TECO)delivery completed (DLV) including Goods Receipt Quantity >= Order QuantityDel. Completed Ind. is set on the order and/or on the last Goods Receipt posting |  |

#### Work Center/Operation Analytics

##### Analyze Costs by Work Center/Operation

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
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Analyze Costs by Work Center/Operation (F3331). | The Analyze Costs by Work Center/Operation screen displays. |  |
| 3 | Enter Data and Execute | Make the following entries and choose Go:Fiscal Period From: 007/2020, for exampleFiscal Period To: 007/2020, for exampleLedger: 0LCompany Code: 3310Currency: AED | The application retrieves all planned and actual debits in table and chart form. |  |

## Appendix

### Situation Handling

#### Manage Situation Types

Purpose

This template is used for situation handling that informs specific users when a condition is met. In this example the user, Production Accountant, receives a notification (icon located in the upper right side the window) when the event-based posting triggers an error.

|  |
| --- |
| Note This requires the configuration expert role for business processes. |

For additional information on situation handling, see the generic setup documentation for object-based situation type: [https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/92a58a164a4c4320bd6bf563d745baca.html](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/92a58a164a4c4320bd6bf563d745baca.html).

|  |
| --- |
| Note Though you may be able to set up the alerts, there is no error test data provided and therefore notification may not be triggered during testing. |

Prerequisite

Ensure that Situation Handling (31N) scope item is installed before you execute this step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types - Extended (F5437). | The Manage Situation Types - Extended view displays. |  |
| 3 | Copy the Situation Template | In the Search field, enter FIN_ EBPC_ERROR_MONITOR and choose Go.Select the checkbox for the row FIN_ EBPC_ERROR_MONITOR, and then choose Copy. |  |  |
| 4 | Maintain Admin Information | Make the following entries and choose Create (accept all warning and enable messages):ID: <enter your template name>Name: <enter your template description>Situation Monitoring:Monitor Instances: <selected> | The initial situation type for event-based posting error message is created. |  |

#### Manage Teams and Responsibilities

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Teams and Responsibilities (F2412). | The Manage Teams and Responsibilities view displays. |  |
| 3 | Category | Remove any preset category filters.In Category, enter EMPC and choose Go.If no results exist, go the next step to create a new team. |  |  |
| 4 | Manage Teams and Responsibilites | Choose Create.Make the following entries and choose Create (accept all warning and enable messages):Name: <Team Name>Global ID: <Global ID name>Type: Production Cost (S_FIN_PRODN)Responsibility DefinitionsCompany Code: 3310Plant: 3310Team OwnersBusiness Partner: <BPC expert ID>Team MembersBusiness Partner: <Production Accountant user ID>Note To find the production accountant user ID, use the search function with:Last name: ProdnAccountantFunctions: S_FPRODN_AConfirm and save the entries. | A New Situation Type view displays. |  |

#### Finishing Up the Situation Type

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Business Process Specialist. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Situation Types - Extended (F5437). | The Manage Situation Types - Extended view displays. |  |
| 3 | Assign Responsibility to the Template | Using the search function, enter the newly created situation type and choose the Situation Types tab. Choose Go.Select the situation type and choose the > sign on the right of the page. Choose Edit.In the Recipients section, under Responsibility by Teams, choose Add Team Category, make the following entries and choose Save:Responsibility DefinitionsCompany Code: 3310Plant: 3310 | The initial situation type for event-based posting error message is created. |  |

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
> Flagged while digesting this document, not verified: Purpose lists six supported variance categories including output price variance, but the Analyze Event-Based Order Costs note lists only five (input quantity, input price, resource usage, lot size, remaining) with SLA line types 9130, 9131, 9132, 9139, 9140 and no output price type.

## Connections
- part-of :: [[_cluster]]
- see-also :: [[06-management-accounting/product-cost-related-master-data-changes-consumer-products-61w-ae-test]]
- see-also :: [[12-production-and-manufacturing/test-script-make-to-stock-production-discrete-manufacturing-bj5-ae-sap]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3F0_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 73,889 chars in the whole document
