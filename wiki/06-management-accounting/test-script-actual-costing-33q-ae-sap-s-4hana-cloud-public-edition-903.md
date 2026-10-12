---
id: 06-management-accounting/test-script-actual-costing-33q-ae-sap-s-4hana-cloud-public-edition-903
title: "Test Script: Actual Costing (33Q_AE) - SAP S/4HANA Cloud Public Edition (33Q_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for Actual Costing (scope item 33Q_AE): prerequisites, preliminary config and step-by-step test procedures."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/inventory-valuation-and-actual-costing]
aliases: [33Q_S4CLD2608_BPD_EN_AE]
keywords: [Inventory Valuation and Actual Costing, actual costing, actual cost rates, actual costing runs, material ledger, price determination, splitting structure, activity types, wip quantity, event-based production cost posting]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33Q_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-903
topic: 06-management-accounting/inventory-valuation-and-actual-costing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Actual Costing (33Q_AE) - SAP S/4HANA Cloud Public Edition (33Q_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33Q_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Inventory Valuation and Actual Costing** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Actual Costing (33Q_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232851580)

[2 Prerequisites 4](#_Toc232851581)

[2.1 System Access 4](#_Toc232851582)

[2.2 Roles 4](#_Toc232851583)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232851584)

[2.4 Business Conditions 5](#_Toc232851585)

[2.5 Preliminary Steps 6](#_Toc232851586)

[2.5.1 Edit Activity Types 6](#_Toc232851587)

[2.5.2 Update Activity Type Hierarchy and Cost Element Groups 6](#_Toc232851588)

[2.5.3 Define/Update Splitting Structure 7](#_Toc232851589)

[2.5.4 Change Material Price Determination for Material Ledger 9](#_Toc232851590)

[2.5.5 Assign Movement Type Groups of Material Ledger 10](#_Toc232851591)

[2.5.6 Optional: Upload Template for Export of Actual Costing 11](#_Toc232851592)

[3 Overview Table 13](#_Toc232851593)

[4 Test Procedures 14](#_Toc232851594)

[4.1 Calculate Actual Cost Rates - Cost Centers 14](#_Toc232851595)

[4.2 Post WIP Quantity Document 15](#_Toc232851596)

[4.3 Execute Actual Costing Runs 16](#_Toc232851597)

[4.4 Analyze Material Actual Values 20](#_Toc232851598)

[4.5 Manage Custom Exports - Actual Costing (Optional) 21](#_Toc232851599)

[4.6 Display Application Logs 22](#_Toc232851600)

[4.7 Material Price Analysis 23](#_Toc232851601)

[4.8 Monitor Material Value Flow (Optional) 24](#_Toc232851602)

## Purpose

Overview

This solution process enables actual costing for material inventory. Initially, all goods movements in a period are valuated based on standard price. All price and exchange rate differences for the material are collected in the material ledger. Similarly, all confirmations are valuated based on a standard activity rate.

At the end of the period, an actual price (called the periodic unit price) is calculated for each material based on actual costs within the period, and an actual activity rate is calculated based on the actual costs for the cost center. This calculated actual price can then be used to revalue inventory, COGS and WIP at period end. For actual costing, to calculate the periodic unit price for your materials, you need to activate actual costing in addition to the material ledger. You also need to choose single-level or multilevel price determination for your materials and use price control standard price for all materials you want to use in actual costing.

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

|  |
| --- |
| Note Sometimes, with a nonstandard scope item, the following catalogs are not activated by default. Therefore, the status of the relevant catalogs, known as the Business Catalog Scope State, is typically set to Off. This happens when the assigned scope item (33Q - Actual Costing in this case) is not part of an active solution. In this situation, the following catalogs related to Actual Costing must be added after the scope item has been activated: |

- SAP_FIN_BC_IA_OM_REP_PC
- SAP_FIN_BC_IA_AC_PER_ACT_PC
- SAP_FIN_BC_IA_AC_PRD_START_PC
- SAP_FIN_BC_IA_AC_REP_PC
- SAP_FIN_BC_OH_PE_PAC_PC

If you encounter any issues with an app used within this scope, and the app is still missing even after activating this scope, refer to [3420263](https://me.sap.com/notes/3420263).

| Name (Role Template) | ID (Role Template) | Name (Launchpad Space) | ID (Launchpad Space) | Log On |
| --- | --- | --- | --- | --- |
| Cost Accountant - Inventory | SAP_BR_INVENTORY_ACCOUNTANT | Inventory Accounting | SAP_BR_INVENTORY_ACCOUNTANT |  |
| Cost Accountant - Overhead | SAP_BR_OVERHEAD_ACCOUNTANT | Overhead Accounting | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |

### Master Data, Organizational Data, and Other Data

Make sure to use the Change Price Determination app before you start using actual costing in system and update the price determination from 2 to 3 for already created materials. This app is part of the Inventory Accountant role.

|  |
| --- |
| Note This section is only relevant for customers' Q and P system where the content is activated without demo data. |

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| 3KW | Create CO Cost Rates - MDS |
| BNN | Create Activity Type and Activity Type Hierarchy - MDS |
| BNP | Create Cost Element Group - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| 3F0 - Event-Based Production Cost Posting | Test script must be executed for this test. |

|  |
| --- |
| Caution As of SAP S/4HANA Cloud 2408, if you use Period-End Closing – Plant (BEI) instead of Event-Based Production Cost Posting (3F0), BEI is deprecated and is planned to be obsolete in a future release. |

### Preliminary Steps

#### Edit Activity Types

Context

In this activity, you can change activity type master to 5 so that actual rate can be calculated automatically based on activity. This has to be done for actual rate calculation to work.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Manage Activity Types (F1605A). | The Manage Activity Types view is displayed. |  |
| 3 | Select Activity Type | Select the activity type row, for example, 1, 11, 3 or 2 that you would like to edit and choose the Edit button. | The Activity Type view is displayed. |  |
| 4 | Actual Price Indicator | Make the following entry and choose the Save button:Actual price indicator 5Note Only change activity types that are relevant for the Actual Cost Rate Calculation - Cost Centers (KSII) app. Don't perform this change for predelivered professional service activity types that start with T or U.Note You can alternatively use the Manage Cost Rates - Actual (F3422) app if you want manual rate update. Make sure the activity type master for the Act. price indicator field is set to 7 via the Manage Activity Types (F1605A) app. |  |  |

#### Update Activity Type Hierarchy and Cost Element Groups

Context

This activity updates activity type hierarchy and cost element groups.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Overhead. |  |  |
| 2 | Access App | Open Manage Global Hierarchies (F2918). | The Manage Global Hierarchies view is displayed. |  |
| 3 | Enter New Activity Type Hierarchy | Make the following entry and choose the Go button:Hierarchy ID: YBGH_P00Note Assign activity types to activity type hierarchy nodes YBGHP2 through YBGHP8. | The YBGH_P00 - Activity Type Hierarchy view is displayed. |  |
| 4 | Update Activity Type Hierarchy from YBGHP2 to YBGHP8 | Assign activity types to this activity type hierarchy.Note Assign activity types relevant for KSII (actual rate calculation) to the YBGHP2 to YBGHP8 group. This change must not be done for predelivered Professional Service activity types that start with T or U.Note If some country/region has activated actual costing and others have not, you should use different activity type for with and without actual costing. Only actual costing relevant activity type should be added to YBGHP2 through YBGHP8. Once this is done, you can use the Actual Cost Rate Calculation: Cost Center app to calculate the rates used in actual costing month-end process step. | New master data is shown in Activity Type Hierarchy: New view. |  |
| 5 | Save Your Data | Choose Save. | The activity type hierarchy is updated. |  |

|  |
| --- |
| Note To assign cost elements to respective groups YBMF_P02 to YBMF_P08, use the Manage Cost Element Groups (F5373) app or the Manage Global Hierarchies (F2918) app (if you have converted to global hierarchy). Customers can maintain G/L account groups for use in the [Define/Update Splitting Structure](#unique_9) [page ] 7 topic. |

#### Define/Update Splitting Structure

Context

The splitting structure splits costs that belong to cost centers based on the following method activity types:

- 12-Activity quantity
- 22-Activity Quantity Planning
- 0-No splitting

Table 2: Splitting Structure YA

| Assignment | Rule | Cost Element Group | Activity Type Hierarchy |
| --- | --- | --- | --- |
| YA2 | YA1 | YBMF_P02 | YBGHP2 |
| YA3 | YA1 | YBMF_P03 | YBGHP3 |
| YA4 | YA1 | YBMF_P04 | YBGHP4 |
| YA5 | YA1 | YBMF_P05 | YBGHP5 |
| YA6 | YA1 | YBMF_P06 | YBGHP6 |
| YA7 | YA1 | YBMF_P07 | YBGHP7 |
| YA8 | YA2 | YBMF_P08 | YBGHP8 |

|  |
| --- |
| Note We recommend using different activity types for countries or regions that have activated actual costing and those that have not. Only actual costing relevant activity type must be added to YBGHP2 through YBGHP8. Once this is done, you can use the Actual Cost Rate Calculation: Cost Centers app to calculate the rates that will be used in actual costing month-end process step. Alternatively, you can use the Manage Cost Rates - Actual app if you want a manual rate update and do not want to use the Actual Cost Rate Calculation app. Make sure the Activity type master for the Act. price indicator field is set to 7 via the Manage Activity Types app. |

Purpose

This activity lets you update splitting structure used for actual cost rate calculation.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Define Splitting Structure (104795).
6. For the displayed row, choose Details (>).
7. For the Define Splitting Structure row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the Define Splitting Structure activity.
3. Choose Open Documentation for the found line item to see more details about this configuration activity.
4. Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
5. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add/update splitting structure | Update or add assignment line for splitting structure YA, updated cost element group, activity type hierarchy, and change rule per your requirements.The following predelivered splitting rules are provided that you can use in splitting:YA1 with method 12-Activity quantityYA2 with method 0-No splittingYA3 with method 22-Activity Quantity Planning | Note Activity type groups are maintained in Manage Global Hierarchies app.Note If you use YA3 method 22, it is a prerequisite that you have plan data uploaded via Import Financial Plan Data (F1711) for the required cost center. |  |

#### Change Material Price Determination for Material Ledger

Context

In this activity, you can change material price determination for Material Ledger. If you activate actual costing, you must set the price determination control to 3 for the materials that would be part of the actual costing. Price determination 3 should be used only when actual costing is active and while working with this scope item.

|  |
| --- |
| Note This step is a prerequisite before you start with any testing of actual costing scope even in starter systems. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Cost Accountant - Inventory. | The SAP Fiori launchpad is displayed. |  |
| 2 | Access App | Open Change Price Determination (CKMM). | The Change Price Determination screen displays. |  |
| 3 | Select Materials | Make the following entries:Material Type: FERT or HALBPlant: <your plant> | This selection depends on your business requirement. |  |
| 4 | Program Definition | Make the following entries and choose the Execute button:Old Price Determination: 2New Price Determination: 3New Price Control: STest Run: Deselect |  |  |

#### Assign Movement Type Groups of Material Ledger

Purpose

This activity lets you assign movement type groups (of material ledger) to movement types to meet your business requirements.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Assign Movement Type Groups of Material Ledger (104390).
6. For the displayed row, choose Details (>).
7. For the Assign Movement Type Groups of Material Ledger row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app.
3. Search for the Assign Movement Type Groups of Material Ledger activity and choose Go to Activity.
4. Continue with the procedure in the following table.

| Step # | Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Add/update movement type group | Update or add movement type group CC or CF to movement type as per your requirement. | Add or update movement type groups. |  |

#### Optional: Upload Template for Export of Actual Costing

Purpose

This activity enables you to upload custom export file templates in XLSX format, using the SAP‑delivered SACT01 – Standard Export Template for Actual Costing as as starting point.

Procedure

Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:

Configure Your Solution:

1. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.
2. Open Manage Your Solution (F1241).
3. If necessary, change the country by choosing Set Local Version.
4. Choose Configure Your Solution.
5. Search for Upload Template for Export of Actual Costing (107293).
6. For the displayed row, choose Details (>).
7. For the Upload Template for Export of Actual Costing row, choose Configure.
8. Continue with the procedure in the following table.

SAP Central Business Configuration:

1. Log on to the project experience in SAP Central Business Configuration.
2. Go to the Business Processes Configuration app.
3. Search for the Upload Template for Export of Actual Costing activity, and choose Go to Activity.
4. Continue with the procedure in the following table.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Download/Upload Template | Download the standard file templates (SACT01).You can add your own customization, for example, adding columns, key figures, calculation formulas, or changing the default Pivot Table layout. After making your changes, save the file and upload your customized template under Custom Templates.For example, you may add a calculation for manufactured product to show the difference between the actual value and the standard value of raw material consumption. | You added or updated fields and created your own template.Note Once your changes reach the target systems, your uploaded templates are available for selection by business users in apps such as Analyze Material Actual Values (F9097). |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Calculate Actual Cost Rates - Cost Centers](#unique_14) [page ] 14 | Cost Accountant - Overhead | Run Actual Cost Rate Calculation - Cost Center (New Version) (F9080) |  |
| [Post WIP Quantity Document](#unique_15) [page ] 15 | Cost Accountant - Inventory | Schedule Actual Costing Jobs (F9244) |  |
| [Execute Actual Costing Runs](#unique_16) [page ] 16 | Cost Accountant - Inventory | Edit Actual Costing Runs (CKMLCP) |  |
| [Analyze Material Actual Values](#unique_17) [page ] 20 | Cost Accountant - Inventory | Analyze Material Actual Values (F9097) |  |
| [Manage Custom Exports - Actual Costing (Optional)](#unique_18) [page ] 21 | Cost Accountant - Inventory | Manage Custom Exports - Actual Costing (F9098) |  |
| [Display Application Logs](#unique_19) [page ] 22 | Cost Accountant - Inventory | Display Application Logs (F9243) |  |
| [Material Price Analysis](#unique_20) [page ] 23 | Cost Accountant - Inventory | Material Price Analysis (CKM3N) |  |
| [Monitor Material Value Flow (Optional)](#unique_21) [page ] 24 | Cost Accountant - Inventory | Material Value Flow Monitor (ML4HVFM) |  |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Calculate Actual Cost Rates - Cost Centers

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

### Post WIP Quantity Document

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

As delivered in the scope item Event-Based Production Cost Posting (3F0), event-based WIP is posted alongside event-based overhead at the time of goods issue or confirmation, and it is cleared upon goods receipt or technical completion. Event-based variance is calculated and posted when the order is final delivered or technical completed.

In addition, if scope item Actual Costing (33Q) is activated, WIP quantity document should be posted to actual costing to enable WIP revaluation in Actual Costing. This is implemented in Schedule Actual Costing Jobs (F9244) by executing the Run WIP Quantity Calculation (Actual Costing) - Order and PCC job template.

|  |
| --- |
| Note If you use Period-End Closing – Plant (BEI) instead of Event-Based Production Cost Posting (3F0), this step is not required as WIP quantity is posted during a period-end transaction through WIP calculation. As of SAP S/4HANA Cloud Public Edition 2408, BEI is deprecated and is planned to be obsolete in a future release. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Schedule Actual Costing Jobs (F9244). | The Schedule Inventory Accounting Jobs screen displays. |  |
| 3 | Create New Job | Choose Create to create a new job. | The New Job view displays. |  |
| 4 | Enter Data | In the Job Template, select WIP quantity calculation (Actual Costing) - Order and PCC.Choose Step 2.Under Scheduling Options, ensure that Start Immediately is selected and choose Step 3.Under Parameters, enter the following:Company Code: 3310Posting Date: <Search and select appropriate option, for example, LASTDAYOFCURRENTFISCALPERIOD>Deselect Test Run and choose Schedule. |  |  |
| 5 | Check Job | Open the job log after the job is in finished status. | WIP quantity documents are posted successfully. |  |

### Execute Actual Costing Runs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, the actual costing run is executed after completing all period-end steps for Event-Based Production Cost Posting (3F0) to calculate the period unit price, representing the average actual cost for materials or semi-finished goods. This activity involves the following steps:

- Selection
- Preparation
- Settlement
- Post Closing
- Mark Prices

|  |
| --- |
| Note Before starting month-end step for actual costing, make sure you open a subsequent period. For example, if you want to close period 5, you must open period 6 first via the Close Period for Material Master Records app using role Product Master Data Specialist and follow the steps in scope item Create New Open MM Posting Period - MDS (BNZ). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Edit Actual Costing Runs (CKMLCP). | The Cockpit: Actual Costing Ledger Run - Change/Execute screen displays. |  |
| 3 | Create Run Template | Select Menu > Edit > Create/Edit Run Template , make the following entries and choose Create:Run Template: 14100518Valid From: <for example, 01/01/2021>On the Create Run Template dialog box that appears, enter ledger 0L (for example) and press Enter.In the Ledger Run Type, select Single Period Run or Year-to-Date Run based on your business needs.Note For single period run, the system selects periodic price from actual cost rate while for Year-to-Date Run, the system selects cumulative price from actual cost rate.Under Parameters of Closing Posting, select Revaluate Material and Set Account Assignment for Consumption.Choose the Company Code Assignment tab. Choose the < button to assign selected company code or << to assign all company codes from the available company codes section to the assigned company codes section and choose Save. Alternatively, you can also choose the Assign Plants button to assign plants from the available plants section.Note You must create template by ledger separately. For example, if you have additional standard ledger 2L or 3L in FI, you need to create the actual costing template for each ledger. Repeat steps for each valid ledger. | This is a one-time activity that must be created for each standard ledger 0L, 2L or 3L separately.This step is mandatory before the run can be created. The same template is used in subsequent months.Note You could delete the template and create a new one. The template can only be changed if a run has not yet been assigned. If you want to change a template to which a run already belongs, you must choose Modify and enter a future date. You can then change the new version of the template (with the new validity date).Note The template is used to determine the assigned company codes or plants. This assignment can no longer be changed in the run. If you only want to have specific plants of a company code, you must switch to plant selection when creating the template. The default setting for the template, and hence our recommendation is to select the company codes. |  |
| 4 | Create Costing Run | Choose the Create/Edit Actual Costing Ledger Run button. Make the following entries and choose the Create button:Costing run: 14100518Period: <enter a period and a year, for example, 05 2022>In the Create Actual Costing Ledger Run dialog box, enter the following and choose Continue :Run template: <Select the template created in the previous step>Note If you get a Navigation to WIP Quantity Job dialog box, choose Close to continue.Note You must run actual costing by ledger separately. For example, if you have additional standard ledger 2L or 3L in FI, you need to run the actual costing for each ledger. Repeat step for each valid ledger. | The Cockpit: Actual Costing Ledger Run - Change/Execute screen displays. |  |
| 5 | Plant Assignment tab | Based on the template selection, if company code is selected then all plants from that company are preselected here or if you have selected specific plants in the template then only those plants show up here. |  |  |
| 6 | Processing section | Expand the Processing section. |  |  |
| 7 | Selection row | On the Selection row, choose the Change Parameters button. On the Costing Cockpit: Actual Costing - Change/Execute screen, deselect Background Processing and then choose Save.Choose Back.Choose Execute, which displays in the Execute column. | Costing run is executed. |  |
| 8 | Preparation row | On the Preparation row, choose the Lock button to unlock. Choose the Change Parameters button. On the Costing Cockpit: Actual Costing - Change/Execute screen, deselect Background Processing.Choose Save.Choose Back, and choose Execute. | Costing run is executed.Note If you activate Actual Costing after you have posted material in previous period, you will run into an error. You can then select Allow Open Status for Previous Period > Exceptional Processing > F1 . This will set the initial inventory at standard price and perform the calculation for previous period as well. This selection is also relevant when the previous period is not closed properly and needs recalculation. |  |
| 9 | Settlement row | On the Settlement row, choose the Lock button to unlock. Choose the Change Parameters button. On the Costing Cockpit: Actual Costing - Change/Execute screen, deselect Background Processing. Keep the other sections as is.Choose Save.Choose Back, and choose Execute. | This step covers single-level and multi-level price determination, work in progress (WIP), cost of goods sold (COGS) revaluation, and reports them as separate documents. |  |
| 10 | Post Closing row | On the Post Closing row, choose the Lock button to unlock and then choose the Change Parameters button. | The Edit Variants view displays. |  |
| 11 | Post Closing: Edit Variants | Select Revaluate Material and Revaluate Consumption checkboxes.Note Selection of the checkboxes does the following:Revaluate Material: If you set this flag, the post-closing updates inventories.Revaluate Consumption/Set Account assignment : If you set these flags, the post-closing step updates the COGS account and the CO-PA characteristics.If you don’t select Revaluate Consumption/Set Account assignment, anything that's been consumed in the next level of production is be revalued, but not consumption to sales (mainly) and cost center/order/project (where the orders/projects aren't tied to materials).Note If you do not set these flags, the post-closing step only updates inventories. Anything that has been consumed in the next level of production will also be revalued, but not consumption to sales (mainly) and costcenter/order/project (where the orders/projects are not tied to materials). If you set these flags, the post-closing step updates the COGS account and the CO-PA characteristics.Deselect Background Processing and Test Run.Choose Save.Choose Back, and choose Execute. | If you post material consumption on objects other then Production/Process order, for example, if you post consumption on cost center, you must select CO Account Assignment. |  |
| 12 | Mark Prices | Set Validity of Marking as Beginning of Following Period and deselect Background Processing. | If you update Period Unit Price monthly, run the Mark Prices step. In case you run the whole year with the same standard price then you do not need to run this step. It is an optional step based on customer's business needs. |  |
| 13 | Save Costing Run | Choose the Save button. |  |  |

### Analyze Material Actual Values

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity provides inventory and goods movement quantities, along with standard and actual values, for any plant and any period independent of material price determination or price control settings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Analyze Material Actual Values (F9097). | The Analyze Material Actual Values displays. |  |
| 3 | Display Values | Make the following entries and choose the Go button:Ledger: 0LCurrency Type: 10Plant: 3310Fiscal Year/Period: <enter a period>Material: FG126Price Determination: <use the dropdown to select 2 (Transaction-Based) and 3 (Single-/Multilevel)Select the material and choose > at the end of the row. |  |  |

|  |
| --- |
| Note You can launch an export job using the Schedule Custom Export Jobs button. This opens the Schedule Actual Costing Jobs (F9244) app. The initial page displays all jobs launched within the specified date range (including custom export jobs). A number of job templates are available, including (but not limited to):Export Material Actual Values – All Stock TypesExport Material Actual Values - General StockExport Material Actual Values - Sales Order StockExport Material Actual Values - Project Stock |

### Manage Custom Exports - Actual Costing (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In this activity, you can download the exported file generated in the previous step.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Manage Custom Exports - Actual Costing (F9098). | The Manage Custom Exports displays. |  |
| 3 | Display Values | Make the following entry and choose the Go button:Job Status: Completed |  |  |

|  |
| --- |
| Note You can launch an export job using the Schedule Actual Costing Jobs button. This opens the Schedule Actual Costing Jobs (F9244) app. The initial page displays all jobs launched within the specified date range (including custom export jobs). A number of job templates are available, including (but not limited to):Export Material Actual Values – All Stock TypesExport Material Actual Values - General StockExport Material Actual Values - Sales Order StockExport Material Actual Values - Project Stock |

### Display Application Logs

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity shows the job logs and messages for the launched export jobs.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Display Application Logs (F9243). | The Display Application Logs displays. |  |
| 3 | Display Application Logs | Make the following entry and choose the Go button:Type: <Select from the dropdown values>Date From-To: <Today, for example>Category: FIN_ACTSubcategory: Custom Export |  |  |

### Material Price Analysis

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This report app helps you view inventory value, new price, and flow of value change.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Material Price Analysis (CKM3N). | The Material Price Analysis screen displays. |  |
| 3 | Material Valuations | Make the following entries and choose the Go button:Material: FG126Plant: 3310 | The Current Material Valuations view displays. |  |
| 4 | Select the Material | Select the desired line item and choose Material Price Analysis. | The Material Price Analysis screen displays. You can enter the Period/Year and review the inventory details. |  |
| 5 | Report | The report containing the movement price, total stock, and other information related to the material displays. |  |  |

### Monitor Material Value Flow (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

After the material ledger period-end closing, differences that can't be explained or that must be balanced remain on the price difference accounts. You use the Value Flow Monitor to analyze these differences and explain the differences/deltas that are calculated during Actual Costing and how they are handled and rolled up to the next level.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log onto the SAP Fiori launchpad as a Cost Accountant - Inventory. | The SAP Fiori launchpad displays. |  |
| 2 | Access the SAP Fiori App | Open Material Value Flow Monitor (ML4HVFM). | The Value Flow Monitor screen displays. |  |
| 3 | Value Flow Monitor | Make the following entries and choose the Execute button:Company Code: 3310Period: <current period>Year: <current year>Costing Run: <Costing run created in Actual Costing step> | The value flow monitor displays the following information by material and valuation areas:Not distributed differencesNot allocated differencesStatus of single and multi-level material price determination |  |

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
- related-to :: [[06-management-accounting/managing-material-price-changes-and-inventory-values-1zt-ae-test-scrip]]
- related-to :: [[06-management-accounting/test-script-inventory-valuation-for-year-end-closing-bej-ae-1260]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/33Q_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 42,424 chars in the whole document
