---
id: 06-management-accounting/test-script-standard-cost-calculation-beg-ae-sap-s-4hana-cloud-public
title: "Test Script: Standard Cost Calculation (BEG_AE) - SAP S/4HANA Cloud Public Edition (BEG_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for standard cost calculation (BEG_AE): prerequisites, setup, costing run steps, analytics."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/product-costing-and-standard-cost-updates]
aliases: [BEG_S4CLD2608_BPD_EN_AE]
keywords: [Product Costing Runs and Standard Cost Updates, standard cost calculation, costing run, costing run execution, activity prices, additive costs, origin groups, parallel valuation, material cost estimates, sales order costing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BEG_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1259
topic: 06-management-accounting/product-costing-and-standard-cost-updates
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Standard Cost Calculation (BEG_AE) - SAP S/4HANA Cloud Public Edition (BEG_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BEG_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Product Costing Runs and Standard Cost Updates** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Standard Cost Calculation (BEG_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861348)

[2 Prerequisites 4](#_Toc232861349)

[2.1 System Access 4](#_Toc232861350)

[2.2 Roles 4](#_Toc232861351)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861352)

[2.4 Preliminary Steps 6](#_Toc232861353)

[2.4.1 Product Cost Planning Configuration Steps 6](#_Toc232861354)

[2.4.2 Optional: Origin Groups 7](#_Toc232861355)

[2.4.2.1 Create Origin Group 7](#_Toc232861356)

[2.4.2.2 Assign Origin Group to Condition Type 8](#_Toc232861357)

[2.4.2.3 Create Purchasing Info Record with Freight Condition 9](#_Toc232861358)

[2.4.3 Optional: Additive Costs 10](#_Toc232861359)

[2.4.3.1 Add Additive Cost Line in Cost Component Structure 10](#_Toc232861360)

[2.4.3.2 Update Costing Variant to Allow Additive Costs 11](#_Toc232861361)

[2.4.3.3 Update Valuation Variant to include Additive Costs 12](#_Toc232861362)

[2.4.3.4 Create Additive Costs 13](#_Toc232861363)

[3 Overview Table 15](#_Toc232861364)

[4 Test Procedures 16](#_Toc232861365)

[4.1 Enter Activity Price 16](#_Toc232861366)

[4.2 Create Costing Run 17](#_Toc232861367)

[4.3 Execute Costing Run 18](#_Toc232861368)

[4.4 Analytics 21](#_Toc232861369)

[4.4.1 Manage Material Cost Estimates 21](#_Toc232861370)

[5 Appendix 23](#_Toc232861371)

[5.1 Manage Order BOM Cost Estimates in Parallel Valuation 23](#_Toc232861372)

[5.2 Manage Sales Order Cost Estimates 24](#_Toc232861373)

## Purpose

Overview

This process enables you to update standard costs for products as part of annual operations planning. The costs are entered manually, and the costing run is created and executed.

This scope item also supports parallel standard costing.

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
| Configuration Expert - Business Process Configuration | SAP_BR_BPC_EXPERT | Business Process Configuration / Business Process Configuration - Finance / Business Process Configuration - Procurement / Manage your Solution / Business Process Configuration - Workflow / Business Configuration - Feature Management / Business Process Configuration - Extensibility Explorer / Business Configuration - Transportation | SAP_BR_BPC_EXPERT / SAP_FIN_SPT_BPC_EXPERT_PC / SAP_MM_SPT_BIZ_PROC_CONFIGN_PC / SAP_CA_SPT_IC_LND_BASE_PC / SAP_CA_SPT_BPC_WORKFLOW_PC / SAP_CA_SPT_BPC_FM_PC / SAP_EI_SPT_BPC_EXT_PC / SAP_TM_SPT_TRANSPCFG_PC |  |
| Purchaser | SAP_BR_PURCHASER | Purchasing / Sourcing and Contracting | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

| Data | Sample Value | Details | Comments |
| --- | --- | --- | --- |
| Cost Center | * | All cost centers |  |
| Activity Types | * | All activity types | All activity types used in the routings / work centers of the materials to be calculated. |
| Material Master | * | Material type FERT, HALB, ROH | Select all materials which belong to this material type. |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNM | Create Cost Center and Cost Center Group - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNR | Create Product Master of type "Raw Material" - MDS |
| 3KW | Create CO Cost RatesNote Ledger-specific material prices should be available (in 1ZT: Managing Material Price Changes and Inventory Values) if ledger-specific calculation is used. |

### Preliminary Steps

#### Product Cost Planning Configuration Steps

Purpose

This activity lets you adopt several aspects of product cost planning to meet your business requirements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for the following SSCUIs:
    - Define Costing Sheets (102922)

|  |
| --- |
| Note It is now possible to use origin group in costing sheet base. Create Origin group is via SSCUI Define Origin Groups (103143). |

-
    - Define Cost Component Structure (102427)
    - Define Valuation Variants (102607)
    - Define Valuation Variants per Plant (102608)
    - Define Overhead Keys (106747)
    - Define Overhead Groups (106748)

1. For the displayed row, choose Details (>).

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following:
    - Define Costing Sheets
    - Define Cost Component Structure
    - Define Valuation Variants
    - Define Valuation Variants per Plant

|  |
| --- |
| Note You can create your own valuation and costing variants. |

1. Choose Open Documentation for the found line item to see more details about this configuration activity.

#### Optional: Origin Groups

The example shown below is used to add additive costs and origin group cost to costing of finished materials FG126. RM20 and SG25 are both used in FG material FG126.

##### Create Origin Group

Purpose

Origin groups provide more detailed information on the source of the material costs or on the origin of the overhead.

|  |
| --- |
| Note Default content deliver origin groups YFC. You can create any origin group as per your business requirements. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Define Origin Groups (103143).
6. For the displayed row, choose Details (>).
7. For the Define Origin Groups row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Origin Groups activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Maintain Origin Groups | Choose the New Entries button and make the following entries:Name: <enter a description>Origin Group: for example, Z10Save the entries. |  |  |

##### Assign Origin Group to Condition Type

Purpose

This step is used to store assignment of condition types to origin group data.

|  |
| --- |
| Note Condition types FGW1, FQU1 and FVA1 for valuation variants 001, 00L, 02L and 03L are mapped to default condition type YFC. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Assign Condition Types to Origin Groups (104814).
6. For the displayed row, choose Details (>).
7. For the Assign Condition Types to Origin Groups row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Assign Condition Types to Origin Groups activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Assign Condition Type to Origin Group | Choose the New Entries button and make the following entries:Condition Type: for example, FVA1Controlling Area: A000Valuation Variant: for example, 0Y1Origin Group: for example, YFCSave the entries. |  |  |

##### Create Purchasing Info Record with Freight Condition

Purpose

In this step, you create purchasing info record with freight condition.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Comments |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Purchaser . | The SAP Fiori launchpad is displayed. |  |
| 2 | Access the App | Open Create Purchasing Info Record (ME11). | The Create Info Record: Initial Screen view displays. |  |
| 3 | Enter Header Data | Make the following entries and press Enter:Supplier: 33300001Material: SG25Purchasing Org.::3310Plant: 3310 | Header data is added. |  |
| 4 | Enter General Information | Make the following entries and choose Purch. Organization tab:Available From: TodayAvailable To: Today + 1 year | General information is added. |  |
| 5 | Enter Purchasing Data | Make the following entries and choose the Conditions tab:Standard Qty: <enter a quantity>Net Price: <enter a price>Incoterm: EXWInco. Location1: Vendor | Purchasing data is added. |  |
| 6 | Enter Conditions | In the General Information area, make the following entries:Valid From: TodayValid To: 12/31/9999Amount: 10In the Condition Supplements section, choose Insert Row (+) and make the following entries:Enter condition type FVA1,amount 4 and press Enter. | Condition data is added. |  |
| 7 | Enter Reference Data (optional) | Optionally, you can enter reference data. | Reference data is added. |  |
| 8 | Save your data | Choose Save. | The purchasing info record is saved. |  |

#### Optional: Additive Costs

The example shown below is used to add additive costs and origin group cost to costing of finished materials FG126. RM20 and SG25 are both used in FG material FG126.

##### Add Additive Cost Line in Cost Component Structure

Purpose

You can update cost component structure to add additive costs per your business requirements.

|  |
| --- |
| Note 104 for freight cost is the default for additive cost. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Define Cost Component Structure (102427).
6. For the displayed row, choose Details (>).
7. For the Define Cost Component Structure row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Costing Variants activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Update Cost Component Structure | Update cost component structure to add additive costs.Note 104 for freight cost is the default for additive cost. |  |  |

##### Update Costing Variant to Allow Additive Costs

Purpose

You can update costing variant to suit your business requirements.

|  |
| --- |
| Note PYC1 and PYC2 are set to include additive costs. |

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Define Costing Variants (104233).
6. For the displayed row, choose Details (>).
7. For the Define Costing Variants row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Costing Variants activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Update Costing Variant | Select costing variant PYC1 and choose the Details button.Choose the Additive Costs tab and make the following selection:Additive Cost Comps: 2 Include Additive CostsChoose Save. |  |  |

##### Update Valuation Variant to include Additive Costs

Purpose

You can update valuation variant to include additive costs.

|  |
| --- |
| Note 001 and 0Y1 are set to include additive costs. |

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
| 1 | Include Additive Costs | Update valuation variants 001 and 0Y1 to include additive costs. |  |  |

##### Create Additive Costs

Context

In this activity, you create additive costs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Create Additive Costs (CK74N). | The Create Additive Costs view displays. |  |
| 3 | Create Additive Costs | Make the following entries:Material: RM20Plant: 3310Costing Variant: PYC1Cost Comp Struct w/ Texts: <Select the checkbox>Press Enter as many times as necessary to skip all screens and warning messages until you reach the Cost Item Basic View. |  |  |
| 4 | Create Unit Cost Estimate | Category V must now be displayed in the Cost Item Basic View.Make the following entries and choose Enter.Cost element: 65400000Quantity: 10 PCTotal/Fixed: 4Origin Group: YFCSave the entries. | Condition data is added. |  |

## Overview Table

This scope item consists of several process steps as provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Enter Activity Price](#unique_17) [page ] 16 | Cost Accountant - Overhead | Manage Cost Rates - Plan (F3162) | The Manage Cost Rates - Plan screen displays and activity price entered. |
| [Create Costing Run](#unique_18) [page ] 17 | Cost Accountant - Inventory | Manage Costing Runs - Estimated Costs (F1865) | The Manage Costing Runs Estimated Costs view displays and costing run is created. |
| [Execute Costing Run](#unique_19) [page ] 18 | Cost Accountant - Inventory | Manage Costing Runs - Estimated Costs (F1865) | The Manage Costing Runs Estimated Costs view displays and costing run is executed. |
| [Manage Material Cost Estimates](#unique_20) [page ] 21 | Cost Accountant - Inventory | Manage Material Cost Estimates (F7650) | This activity lists material cost estimates across all costing variants. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Enter Activity Price

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you enter activity price.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Cost Rates - Plan (F3162). | The Manage Cost Rate - Plan screen displays. |  |
| 3 | Enter Variables | Make the following entries :Cost Center: 33101301Activity Type: 1Choose GoSelect the line and choose Edit. | The Edit Cost Rates screen displays. |  |
| 4 | Make Price Changes | In the dialog box, make changes to Fixed Rate and Variable Rate field and choose Save. | Activity prices are posted for the fiscal year. |  |

### Create Costing Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create a costing run.

You can have separate standard product costing for each Ledger. The following table shows the combinations available in standard content:

|  |
| --- |
| Note Ledger-specific prices can be maintained in the material master within creation mode or via the Manage Material Valuations (F2680) app. |

| Costing Type | Ledger | Costing Variant | Valuation Variant | Costing Sheet | Impact |
| --- | --- | --- | --- | --- | --- |
| 01 | Blank - means update to all Ledgers | PPC1-Standard Cost Est. (Mat.) | 001 | XXXXPC (XXXX represents default company code) | Will update all ledgers with same standard cost |
| 01 | Blank - means update to all Ledgers | PYC1-Cost Estimate Standard 0Y1 | 0Y1 | XXXXPC (XXXX represents default company code) | Will update all ledgers with same standard cost |
| 01 | Blank - means update to all Ledgers | PYC2-Cost Estimate Plan 0Y2 | 0Y2 | XXXXPC (XXXX represents default company code) | Will update all ledgers with same standard cost |
| 0L | 0L - only update to 0L | P00L-Legal Mat Cst Est Ldgr-0L | 00L | XXXXPC (XXXX represents default company code) | Will update Ledger 0L only |
| 2L | 2L - only update to 2L | P02L-Legal Mat Cst Est Ldgr-2L | 02L | XXXXPC (XXXX represents default company code) | Will update Ledger 2L (should use only when you have Ledger 2L in FI) |
| 3L | 3L - only update to 3L | P03L-Legal Mat Cst Est Ldgr-3L | 03L | XXXXPC (XXXX represents default company code) | Will update Ledger 3L (should use only when you have Ledger 3L in FI) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs Estimated Costs view displays. |  |
| 3 | Creating Costing Run | Choose the Create button. | The Create New Costing Run view displays. |  |
| 4 | Enter Parameters for Costing Run | Make the following entries and choose Enter.Costing Run: Test1 (XX can be any number)Costing Run Date: <Enter the current date>Description: Costing Run Test1 (XX can be any number)Costing Variant: PYC1Note The ledger is updated based on the costing type mapped to the costing variant. Select per your business needs.Costing Version: 1Controlling Area: A000Company Code: 3310Costing Date From: <Enter the current date>Costing Date To: <Adopt the default value>Qty Structure Date: <Enter the current date>Valuation Date: <Enter the current date> |  |  |
| 5 | Save Costing Run | Choose the Save button. |  |  |

### Execute Costing Run

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you execute the costing run. Configured materials are not included.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs Estimated Costs view displays. |  |
| 3 | Select Costing Run | Search for the costing run created in the previous step.Select the costing run and choose Edit. | The Edit Costing Run view displays. |  |
| 4 | Edit Costing Run | Make the desired changes and choose Continue. Save the changes as required. |  |  |
| 5 | Create Cost Estimates | Open the Process section. From the Selection row, choose the Change Parameter button and make the following entries:Material Type : HALB, ROH, FERTPlant: 3310Select the Explode Multilevel Structure checkbox.Deselect Background Processing indicator and then choose Save.Choose Back and save the entries as required.Choose Execute, which displays in the Execute column, and the status light for the Selection row turns green. | The selection is executed. |  |
| 6 | Create Cost Estimates - Selection | From the Costing row, choose the Change Parameter button. On the Costing Run: Cost Estimate – Change Parameters view, deselect Background Processing indicator and then choose Save.Choose Back.Choose Execute, which displays in the Execute column and the status light for the Costing row turns green. | Costing Run is executed. |  |
| 7 | Create Cost Estimates - Costing | From the menu, in case the Edit is not visible directly, choose Menu > Edit > Costing Results .If the status light for this row is red, review the Costing levels report. Correct errors in the report. To re-run the costing (if necessary), repeat steps for Selection Struct. Explosion and Costing Rows. | Costing Run is executed. |  |
| 8 | Create Cost Estimates - Analysis | On the Analysis row, choose the Change Parameter button. Select SAP&11 for the parameter setting and then select Choose. On the Costing Run: Analysis - Change Parameters view, deselect Background Processing checkbox and then choose Save.Choose Back.Choose Execute, which displays in the Execute column.Choose Back and confirm the message with yes to leave the list. | Costing Run is executed. |  |
| 9 | Create Cost Estimates - Marking | On the Marking row, choose the Lock button.Note The allowance must be set for the period for which the price update is scheduled.On the Price Update: Organizational Measure view, select the company code 3310 row for the appropriate ledger 0L.In the Permitted Costing Variant dialog box, enter the costing variant of PYC1 and the costing version of 1, and then choose Issue allowance for marking. The status light of the row turns green.Choose Back.Choose Change Parameter and deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute.Note Check the log and resolve error messages. Warning messages may also be potential problems later on in the process, so those need to be resolved as well. | Costing Run is executed.The following is an excerpt of potential messages:The messages Costing error for material SGPI*1 to 10: no BOM and routing and Costing error for material FG_FL*0 to FG_FL*2 : no BOM and routing are ok. These materials are sample master data for additional processes.In case no price could be determined for single-level material, the following message displays No price could be determined for material/batch PPPP plant XX10 (PPPP stands for Material number/XX stands for Country ID). For correction, refer to scope item 1ZT: Managing Material Price Changes and Inventory Values. |  |
| 10 | Create Cost Estimates - Release | On the Release row, choose Change Parameter and deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute. | The current prices will be updated in the material master data.Note The new standard price cannot be updated before the first day of the validity of the costing run. For example, if costing run is valid from 01/01/<planning year>, then releasing the standard price is possible on 01/01/<planning year> at the earliest. |  |

### Analytics

#### Manage Material Cost Estimates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

This activity lists material cost estimates across all costing variants. Without switching between local and group currencies, you can display all currencies as separate columns. It also enables navigation to view the cost estimate for an individual material and allows you to create a material cost estimate.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Material Cost Estimates (F7650). | The Manage Material Cost Estimates view displays. |  |
| 3 | Execute Report | Make the following entries and choose GoMaterial: <for example, FG126>Plant: 3310Costing Variant: PYC1Costing Status: <leave the field blank>Note The material must have a valid costing run executed for the costing variant. | The screen displays an itemization breakdown of product costs. You can switch to Display mode or use the Create button to create a material cost estimate. |  |

## Appendix

### Manage Order BOM Cost Estimates in Parallel Valuation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity shows how to do ledger-specific sales order costing. This step is relevant only if you have a make to order scope such as Make-to-Order Production with Variant Configuration(1YT), Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE), or Make-to-Order Production – Process Manufacturing (3OK).

|  |
| --- |
| Note By default, sales order costing is automatically executed with valuation variant PPC4 during sales for creation which updates all standard ledgers with the same sales order cost. This step is relevant only if you maintain different ledger material prices in the MM master data (scope item 1ZT: Managing Material Price Changes and Inventory Values) and want to do ledger-specific sales order costing for parallel ledgers like 2L or 3L. |

Prerequisite

Primary sales order is created in make to order scope Make-to-Order Production with Variant Configuration(1YT), Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE), or Make-to-Order Production – Process Manufacturing (3OK).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Sales Accounting Jobs (F1483). | The Application Jobs view displays. |  |
| 3 | Create | Choose the Create button. | The New Job: Manage Order BOM Cost Estimates in Parallel Valuation view displays. |  |
| 4 | Enter Selection Criteria | In the Template Selection section, make the following entries:Job Template: Manage Order BOM Cost Estimates in Parallel ValuationJob Name: Manage Order BOM Cost Estimates in Parallel ValuationChoose Step 2. | The Scheduling Options view displays. |  |
| 5 | Scheduling Options | Select the Start Immediately checkbox and choose Step 3. | The Parameters view display. |  |
| 6 | Parameters | Make the following entries and choose the Schedule button:Costing Variant: PB2L for ledger 2L or PB3L for ledger 3LTransfer Control: PC03Description for Costing Run: <enter text>Sales Document: <sales order number from scope 1YT, BJE or 3OK for which you want to do parallel sales order costing>Sales Document Item: 0010Created On: <enter a date>Processing Options:Test Selection: <Deselect>Cost VO: <Select>Set Costing Status Marked: <Select> | You are returned to the Application Jobs view. Your sales order costing for parallel valuation is finished. |  |

### Manage Sales Order Cost Estimates

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity shows how to analyze sales order costing. This step is relevant only if you have a make to order scope such as Make-to-Order Production with Variant Configuration(1YT), Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE), or Make-to-Order Production – Process Manufacturing (3OK).

|  |
| --- |
| Note By default, sales order costing is automatically executed with valuation variant PPC4 during sales for creation which updates all standard ledgers with the same sales order cost. |

Prerequisite

Primary sales order is created in make to order scope Make-to-Order Production with Variant Configuration(1YT), Make-to-Order Production – Finished Goods Sales and Final Assembly (BJE), or Make-to-Order Production – Process Manufacturing (3OK).

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Sales Order Cost Estimates (F9245). | The Manage Sales Order Cost Estimates view displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Sales Document: <sales order number from scope 1YT, BJE or 3OK for which you want to do parallel sales order costing>Sales Document Item: 0010Plant: 3310Costing Variant: PB2L for ledger 2L or PB3L for ledger 3LCosting Status: <select from dropdown>Material: <optional> |  |  |

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
- related-to :: [[06-management-accounting/crear-ejecucion-del-calculo-del-coste-mds-bnu-678]]
- related-to :: [[06-management-accounting/criar-execucao-de-calculo-de-custos-mds-bnu-680]]
- related-to :: [[06-management-accounting/kalkulationslauf-anlegen-sds-bnu-676]]
- related-to :: [[06-management-accounting/master-data-script-create-costing-run-mds-bnu-677]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BEG_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 40,059 chars in the whole document
