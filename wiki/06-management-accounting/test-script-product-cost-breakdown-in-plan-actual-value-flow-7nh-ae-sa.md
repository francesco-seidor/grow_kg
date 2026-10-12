---
id: 06-management-accounting/test-script-product-cost-breakdown-in-plan-actual-value-flow-7nh-ae-sa
title: "Test Script: Product Cost Breakdown in Plan/Actual Value Flow (7NH_AE) - SAP S/4HANA Cloud Public Edition (7NH_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition 2608 test script for scope item 7NH: plan/actual product cost breakdown, prerequisites, configuration and Fiori test steps."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/product-costing-and-standard-cost-updates]
aliases: [7NH_S4CLD2608_BPD_EN_AE]
keywords: [Product Costing Runs and Standard Cost Updates, product cost breakdown, origin cost breakdown, universal component breakdown, costing runs, origin groups, product cost planning configuration, cost of goods manufactured, product profitability analysis, scope item testing]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7NH_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1222
topic: 06-management-accounting/product-costing-and-standard-cost-updates
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Product Cost Breakdown in Plan/Actual Value Flow (7NH_AE) - SAP S/4HANA Cloud Public Edition (7NH_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7NH_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Product Costing Runs and Standard Cost Updates** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Product Cost Breakdown in Plan/Actual Value Flow (7NH_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232860505)

[2 Prerequisites 4](#_Toc232860506)

[2.1 System Access 4](#_Toc232860507)

[2.2 Roles 4](#_Toc232860508)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232860509)

[2.4 Business Conditions 6](#_Toc232860510)

[2.5 Preliminary Steps 7](#_Toc232860511)

[2.5.1 Plan for Product Cost Breakdown 7](#_Toc232860512)

[2.5.1.1 Product Cost Planning Configuration Steps 7](#_Toc232860513)

[2.5.1.2 Product Plan Cost Rates from SAP Analytics Cloud 8](#_Toc232860514)

[2.5.2 Optional: Origin Groups 9](#_Toc232860515)

[2.5.2.1 Create Origin Group 9](#_Toc232860516)

[2.5.2.2 Assign Origin Group to Condition Type 10](#_Toc232860517)

[2.5.2.3 Create Purchasing Info Record with Freight Condition 11](#_Toc232860518)

[2.5.3 Actual for Product Cost Breakdown 12](#_Toc232860519)

[2.5.3.1 Update Actual Product Cost Breakdown in Actual Production Process 12](#_Toc232860520)

[2.5.3.2 Product Sell from Stock 12](#_Toc232860521)

[3 Overview Table 14](#_Toc232860522)

[4 Test Procedures 15](#_Toc232860523)

[4.1 Plan for Product Cost Breakdown 15](#_Toc232860524)

[4.1.1 Determine Product Cost Breakdown for Manufactured Products 15](#_Toc232860525)

[4.1.2 Display Product Cost Breakdown in Product Cost Planning 19](#_Toc232860526)

[4.1.3 Monitor Material Prices 20](#_Toc232860527)

[4.2 Actual for Product Cost Breakdown 21](#_Toc232860528)

[4.2.1 Manage Journal Entries 21](#_Toc232860529)

[4.2.2 Display Journal Entries 22](#_Toc232860530)

[4.2.3 Review Production Cost of Goods Manufactured with Universal Component Breakdown 23](#_Toc232860531)

[4.2.4 Analyze Product Profitability with Component Breakdown 24](#_Toc232860532)

## Purpose

Overview

This scope item provides a detailed breakdown of production costs and origin costs for a manufactured product with quantity structure:

- The production cost breakdown explains the cost of goods manufactured (COGM) from the perspective of the manufacturing process including material usage, internal activities, and external activities.
- The origin cost breakdown is an alternative view of the cost of goods manufactured including original production factors. It allows you to identify the impact of any changes to your primary costs on product profitability, such as increases in energy prices, higher wage costs, or changes in depreciation rules. Without the origin cost breakdown these costs are grouped under activity rates and classified as production activity costs.

The product cost breakdown details product costs and forms the basis for the cost of goods sold (COGS) breakdown in product profitability analysis. ​The cost breakdown structure and its corresponding cost components are defined based on configuration settings, with cost breakdown results generated automatically during the creation of material standard cost estimate and the posting of costs from manufacturing and selling process.

To enable the origin cost breakdown, this scope item must be activated along with the following mandatory prerequisite scope items:

- Integrated Financial Planning (4RC)
    - Cost Rate Planning and Cost Rate Split activities
- Import Connection Setup with SAP Analytics Cloud (1YB)
    - Integrate Cost Rate Split with SAP S/4HANA Cloud Public Edition

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
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |
| Cost Accountant - Sales | SAP_BR_SALES_ACCOUNTANT | Sales Accounting | SAP_BR_SALES_ACCOUNTANT |  |
| General Ledger Accountant | SAP_BR_GL_ACCOUNTANT | General Ledger | SAP_BR_GL_ACCOUNTANT |  |

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
| BNM | Create Cost Center and Cost Center Group |
| BNN | Create Activity Type and Activity Type Group |
| BNT | Create Finished Good ("FERT") |
| BNS | Create Semi-Finished Good ("HALB") |
| BNR | Create Raw Material ("ROH") |
| 3KW | Create CO Cost RatesNote Ledger-specific material prices should be available (in 1ZT: Managing Material Price Changes and Inventory Values) if ledger-specific calculation is used. |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

Table 2: Business Conditions

| Scope Item | Business Condition |
| --- | --- |
| 1ZT - Managing Material Price Changes and Inventory Values | Relevant for material price breakdown.The cost component breakdown is updated based on the material price breakdown during goods movement. |
| 4RC - Integrated Financial Planning | Relevant for Plan for Product Cost Breakdown.Financial Planning in SAP Analytics Cloud (SAC) provides the cost breakdown for planned activity cost rates. This information is essential as a basis for the business processes in SAP S/4HANA Cloud Public Edition to generate the cost breakdown.Retrieve (Push) the cost breakdown from SAC for activity cost rates and transfer it to the SAP S/4HANA Cloud Public Edition table ACCOSTRATE.Note SAC story UCB_SAP_FI_IFP_IM_OPEX_ActivityCostRatePlanning_1 is used for data download from SAC. |
| 1YB - Import Connection Setup with SAP Analytics Cloud | Relevant for Plan for Product Cost Breakdown.Integrate cost rate split with SAP S/4HANA Cloud Public Edition |
| J58 - Accounting and Financial Close | Relevant for Actual for Product Cost Breakdown.Execute the journal entries section from the script. |
| 3F0 - Event-Based Production Cost Posting | Relevant for Actual for Product Cost Breakdown.Execute the entire script, making sure that at least one of the production scripts specified in the 3F0 business conditions is run. |
| J55 - Margin Analysis | Relevant for Actual for Product Cost Breakdown.Execute the product profitability section from the script, making sure that one of the sales scripts such as BD9 - Sell from Stock and at least one of the production scripts like BJ5 - Make-to-Stock Production – Discrete Manufacturing is run as specified in the J55 business conditions for Product Profitability. |

### Preliminary Steps

#### Plan for Product Cost Breakdown

##### Product Cost Planning Configuration Steps

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
    - Define Overhead Keys (106747)
    - Define Overhead Groups (106748)
    - Define Cost Component Structure (102427): The cost component Y1 and the PB-production cost breakdown are both utilized for standard costing, so they must remain consistent. Therefore, any changes made to Y1 through the cost component structure also updates the PB-production cost breakdown to maintain alignment. Edits to PB-production cost breakdown must be done only through the Define Cost Component Structure (102427) but not allowed via Define Cost Breakdown Structures (106910).
    - Define Cost Breakdown Structures (106910): The origin cost breakdown is supported only by UCB and operates independently from the PB-production cost breakdown. You can decide whether to include it as part of the optional scope.

|  |
| --- |
| Note We provide standard cost component structures for origin breakdown and PB-production cost breakdown. You need to modify or create these components to ensure that the cost component structures are correctly maintained and that G/L accounts are appropriately assigned to the cost components. |

-
    - Define Valuation Variants for Material Cost Estimates (102607)
    - Define Valuation Variants per Plant (102608)

1. For the displayed row, choose Details (>).

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following:
    - Define Costing Sheets
    - Define Overhead Keys
    - Define Overhead Groups
    - Define Cost Breakdown Structures

|  |
| --- |
| Note We provide standard cost component structures for origin breakdown and PB-production cost breakdown. You need to modify or create these components to ensure that the cost component structures are correctly maintained and that G/L accounts are appropriately assigned to the cost components. |

-
    - Define Valuation Variants for Material Cost Estimates
    - Define Valuation Variants per Plant

|  |
| --- |
| Note You can create your own valuation and costing variants. |

1. Choose Open Documentation for the found line item to see more details about this configuration activity.

##### Product Plan Cost Rates from SAP Analytics Cloud

Use scope items Integrated Financial Planning (4RC) and Financial Plan Data Upload from File (1HB) to plan and calculate the cost rate for the activity type. Integrate the activity cost rate breakdown back to SAP S/4HANA Cloud Public Edition for origin cost breakdown.

|  |
| --- |
| Note There is no origin cost breakdown for the activity type if the cost rate is manually maintained in SAP S/4HANA Cloud Public Edition via the app. |

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

#### Actual for Product Cost Breakdown

##### Update Actual Product Cost Breakdown in Actual Production Process

Purpose

In this activity, you can update the actual production cost breakdown throughout the manufacturing process.

Procedure

Follow all steps from the scope item Make-to-Stock Production – Discrete Manufacturing(BJ5) for the production process using the Universal Component Breakdown (UCB) structure.

##### Product Sell from Stock

Purpose

In this activity, you can perform the sales process based on the Universal Cost Breakdown (UCB).

Procedure

Follow all steps from the scope item Sell from Stock(BD9) from sales order creation to billing, to view Product Profitability with UCB breakdown.

## Overview Table

This scope item consists of several process steps as provided in the table below:

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Plan for Product Cost Breakdown |  |  |  |
| [Determine Product Cost Breakdown for Manufactured Products](#unique_16) [page ] 15 | Cost Accountant - Inventory | Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs Estimated Costs view displays and costing run is created. |
| [Display Product Cost Breakdown in Product Cost Planning](#unique_17) [page ] 19 | Cost Accountant - Inventory | Manage Material Cost Estimates (F7650) | The report presents itemization breakdown of product costs, and includes the Universal Component Breakdown (UCB) based on standard cost. |
| [Monitor Material Prices](#unique_18) [page ] 20 | Cost Accountant - Inventory | Monitor Material Prices (F7245) | Helps review and compare material prices across ledgers. |

Actual for Product Cost Breakdown

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Manage Journal Entries](#unique_19) [page ] 21 | General Ledger Accountant | Manage Journal Entries (F0717A) | You display, change, or reverse a journal entry. |
| [Display Journal Entries](#unique_20) [page ] 22 | General Ledger Accountant | Display Journal Entries (F7697) | You display the journal entries. |
| [Review Production Cost of Goods Manufactured with Universal Component Breakdown](#unique_21) [page ] 23 | Cost Accountant - Production | Cost of Goods Manufactured - Review Booklet (F8625) | You can review and analyze actual production costs at the company code level, product level, or individual order level. |
| [Analyze Product Profitability with Component Breakdown](#unique_22) [page ] 24 | Cost Accountant - Sales | Product Profitability Review Booklet (F8348) | Data for all product groups that meet the selection criteria displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Plan for Product Cost Breakdown

#### Determine Product Cost Breakdown for Manufactured Products

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you create a costing run with product cost breakdown.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Costing Runs - Estimated Costs (F1865). | The Manage Costing Runs - Estimated Costs view displays. |  |
| 3 | Creating Costing Run | Choose the Create button. | The Create New Costing Run view displays. |  |
| 4 | Enter Parameters for Costing Run | Make the following entries and choose Enter.Costing Run: Test1Costing Run Date: <Enter the current date>Description: Costing Run Test1Costing Variant: PYC1Note The ledger is updated based on the costing type mapped to the costing variant. Select per your business needs.Costing Version: 1Controlling Area: A000Company Code: 3310Costing Date From: <Enter the current date>Costing Date To: <Adopt the default value>Qty Structure Date: <Enter the current date>Valuation Date: <Enter the current date> |  |  |
| 5 | Save Costing Run | Choose the Save button. |  |  |
| 6 | Create Cost Estimates | Open the Process section. From the Selection row, choose the Change Parameter button and make the following entries:Material Type: HALB, ROH, FERTPlant: 3310Material: <Material numbers of relevant Materials, for this scope item FG0513 is assumed>Material Type : HALB, ROH, FERTNote For testing purposes, enter material number FG126 instead of material type.Plant: 3310Select the Explode Multilevel Structure checkbox.Deselect Background Processing indicator and then choose Save.Choose Back and save the entries as required.Choose Execute, which displays in the Execute column, and the status light for the Selection row turns green. | The selection is executed. |  |
| 7 | Create Cost Estimates - Selection | From the Costing row, choose the Change Parameter button. On the Costing Run: Cost Estimate – Change Parameters view, deselect Background Processing indicator and then choose Save.Choose Back.Choose Execute, which displays in the Execute column and the status light for the Costing row turns green. | Costing Run is executed. |  |
| 8 | Create Cost Estimates - Costing | From the menu, in case the Edit is not visible directly, choose Menu > Edit > Costing Results .If the status light for this row is red, review the Costing levels report. Correct errors in the report. To re-run the costing (if necessary), repeat steps for Selection Struct. Explosion and Costing Rows. | Costing Run is executed. |  |
| 9 | Create Cost Estimates - Analysis | On the Analysis row, choose the Change Parameter button. Select SAP&11 for the parameter setting and then select Choose. On the Costing Run: Analysis - Change Parameters view, deselect Background Processing checkbox and then choose Save.Choose Back.Choose Execute, which displays in the Execute column.Choose Back and confirm the message with yes to leave the list. | Costing Run is executed. |  |
| 10 | Create Cost Estimates - Marking | On the Marking row, choose the Lock button.Note The allowance must be set for the period for which the price update is scheduled.On the Price Update: Organizational Measure view, select the company code 3310 row for the appropriate ledger 0L.In the Permitted Costing Variant dialog box, enter the costing variant of PYC1 and the costing version of 1, and then choose Issue allowance for marking. The status light of the row turns green.Choose Back.Choose Change Parameter and deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute.Note Check the log and resolve error messages. Warning messages may also be potential problems later on in the process, so those need to be resolved as well. | Costing Run is executed.The following is an excerpt of potential messages:The messages Costing error for material SGPI*1 to 10: no BOM and routing and Costing error for material FG_FL*0 to FG_FL*2 : no BOM and routing are ok. These materials are sample master data for additional processes.In case no price could be determined for single-level material, the following message displays No price could be determined for material/batch PPPP plant XX10 (PPPP stands for Material number/XX stands for Country ID). For correction, refer to scope item 1ZT: Managing Material Price Changes and Inventory Values. |  |
| 11 | Create Cost Estimates - Release | On the Release row, choose Change Parameter and deselect Test Run and Background Processing.Choose Save.Choose Back, and choose Execute. | The current prices will be updated in the material master data.Note The new standard price cannot be updated before the first day of the validity of the costing run. For example, if costing run is valid from 01/01/<planning year>, then releasing the standard price is possible on 01/01/<planning year> at the earliest. |  |

#### Display Product Cost Breakdown in Product Cost Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

You can view material cost estimates calculated in previous steps, as well as the results of cost component split (based on the costing lot size) and the costing itemization results by G/L accounts. This app includes the Universal Component Breakdown (UCB) based on the standard cost.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Material Cost Estimates (F7650). | The Manage Material Cost Estimates view displays. |  |
| 3 | Execute Report | Make the following entries and press Enter.Material: <enter a material, for example FG126>Note The material must have a valid costing run executed for the costing variant selected or the date of your costing run, for example, the first day of the next year as used in the Create Costing Run step.Plant: 3310Costing Variant: PYC1From the material detail row, choose the > Details button. | The Display Material Cost Estimate with Quantity Structure screen displays. |  |
| 4 | UCB Components | Scroll down within the top view and choose the UCB Components button. | The screen shows the UCB based on the standard cost. |  |

#### Monitor Material Prices

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity helps you review and compare material prices across ledgers. You can also compare inventory valuations across different ledgers and accounting principles.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori app | Open Monitor Material Prices (F7245). | The Monitor Material Prices screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:View Type: <Select either Compare Two Valuations OR Prices in All Valuations>Valuations to Compare: <valid for Prices in All Valuations view type; search and select all the options you want to compare, multiple selections possible>Valuation to Compare 1: <valid for Compare Two Valuations view type; search and select all the options you want to compare>Valuation to Compare 2: <valid for Compare Two Valuations view type; search and select all the options you want to compare>Material: <enter a material, for example FG126>Company Code: 3310Plant: 3310Valid On: <select from the dropdown> | All the material price lists display. |  |

### Actual for Product Cost Breakdown

#### Manage Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can display, change, or reverse a journal entry.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Manage Journal Entries (F0717A). |  |  |
| 3 | Select Journal Entry | Make the following entries and choose Go:Company Code: 3310Journal Entry Date: (optional) <date>Posting Date (optional): <date>Fiscal Year: <year of posting document>Fiscal Period: (optional) <period>Journal Entry Type: (optional) For example, SA | Selected journal entries are displayed in the Journal Entries list. |  |
| 4 | Display Journal Entry | Choose the link for the entry in the Journal Entry column. From the dialog box, choose Display Journal Entries. | The Display Journal Entries view is displayed. |  |
| 5 | Review | Review the journal entries and choose Back. |  |  |
| 6 | Manage Journal Entry | For one of the journal entries, choose Details (>).Select a journal entry number and choose Manage Journal Entries. Choose Edit to edit a journal entry or choose New to create a journal entry. | The right pane displays details for the journal entry. |  |
| 7 | Reverse Journal Entry | Select a relevant document and choose Reverse. | The Reverse Journal Entries Details dialog box displays. |  |
| 8 | Enter Reversal Data | Make the following entries and choose OK:Reversal Reason: <for example, Wrong posting>Posting Date: <date after posting date of document to reverse> | The journal entry is reversed. |  |

#### Display Journal Entries

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you display journal entries.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a General Ledger Accountant. |  |  |
| 2 | Access the SAP Fiori App | Open Display Journal Entries (F7697). |  |  |
| 3 | Select Journal Entry | Make the following entries and choose Go:Company Code: 3310Journal Entry Date: (optional) <date>Posting Date (optional): <date>Fiscal Year: <year of posting document>Fiscal Period: (optional) <period>Journal Entry Type: (optional) For example, SANote Leave other fields empty. | Selected journal entries are displayed in the Journal Entries list. |  |
| 4 | Display Journal Entry | For the journal entry you want to review, choose the Details (>) button at the right of the row. | A right pane opens with details of the journal entry. |  |
| 5 | Review | Review the journal entry. When done, choose the Close (x) button at the top of the right pane. |  |  |

#### Review Production Cost of Goods Manufactured with Universal Component Breakdown

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can review and analyze actual production costs at the company code level, product level, or individual order level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Cost of Goods Manufactured - Review Booklet (F8625). | The COGM Review Booklet screen displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Ledger: <keep this field blank>Reporting Date: <enter the currrent date>Company Code: 3310Cost Breakdown Method: <Use the dropdown to select Production Cost Breakdown>Cost Component Hierarchy: <Use the dropdown to select Universal Production Cost Breakdown Group>Currency Role: <Use the dropdown to select Company Code Currency>If these fields aren't visible, choose Adapt Filters and select those from the available options. | This booklet provides year-to-date comparison and period comparison for actual production cost. |  |

#### Analyze Product Profitability with Component Breakdown

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

In this activity, you can analyze information such as contribution margins for individual products with UCB origin cost breakdown, related product information, and profitability characteristics.

Prerequisites

Make sure you have executed at least one of the sales scripts listed in the Margin Analysis (J55) business conditions.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Sales. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Product Profitability Review Booklet (F8348). | The Product Profitability Review booklet view displays. |  |
| 3 | Enter Data | Make the following entries and choose Go:Ledger: 0LCompany Code: 3310Currency Role Field: <Global Currency>Reporting Date: <current date>Product Sold: <optional>Product Sold Group: <optional>Sales Document: <optional>If these fields aren't visible, choose Adapt Filters and select those from the available options. | The booklet includes multiple pages:Margin Overview: Year-to-Date MarginCOGS Breakdown: Year-to-Date COGS BreakdownThe COGS breakdown is only accurate when using scope Product Cost Breakdown in Plan/Actual Value Flow (7NH). |  |

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
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/7NH_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 42,672 chars in the whole document
