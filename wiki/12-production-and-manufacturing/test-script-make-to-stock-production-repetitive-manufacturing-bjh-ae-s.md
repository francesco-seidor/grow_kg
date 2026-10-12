---
id: 12-production-and-manufacturing/test-script-make-to-stock-production-repetitive-manufacturing-bjh-ae-s
title: "Test Script: Make-to-Stock Production – Repetitive Manufacturing (BJH_AE), SAP S/4HANA Cloud Public Edition (BJH_S4CLD2608_BPD_EN_AE)"
description: "SAP Best Practices test script for scope item BJH_AE: repetitive manufacturing from PIRs and MRP to planning table, staging, REM backflush, error handling."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/make-to-stock-discrete-and-repetitive]
aliases: [BJH_S4CLD2608_BPD_EN_AE]
keywords: [Make-to-Stock Discrete and Repetitive Manufacturing, repetitive manufacturing, make-to-stock production, planned independent requirements, material requirements planning, planning table, stock coverage, atp check, material staging, backflush confirmation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJH_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1273
topic: 12-production-and-manufacturing/make-to-stock-discrete-and-repetitive
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Make-to-Stock Production – Repetitive Manufacturing (BJH_AE), SAP S/4HANA Cloud Public Edition (BJH_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJH_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Make-to-Stock Discrete and Repetitive Manufacturing** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Make-to-Stock Production – Repetitive Manufacturing (BJH_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861844)

[2 Prerequisites 4](#_Toc232861845)

[2.1 System Access 4](#_Toc232861846)

[2.2 Roles 4](#_Toc232861847)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232861848)

[2.4 Business Conditions 6](#_Toc232861849)

[2.5 Preliminary Steps 7](#_Toc232861850)

[2.5.1 Initializing Material Stock 7](#_Toc232861851)

[2.5.2 Create Product Cost Collectors 8](#_Toc232861852)

[2.5.3 Create Preliminary Cost for the Product Cost Collector 8](#_Toc232861853)

[3 Overview Table 10](#_Toc232861854)

[4 Test Procedures 11](#_Toc232861855)

[4.1 Anonymous Forecast and MRP 11](#_Toc232861856)

[4.1.1 Create Planned Independent Requirements 11](#_Toc232861857)

[4.1.2 Material Requirements Planning (MRP) 12](#_Toc232861858)

[4.1.3 Adjust Planning in Planning Table 14](#_Toc232861859)

[4.1.4 Check Range of Stock Coverage 15](#_Toc232861860)

[4.2 ATP Check in Planned Orders 16](#_Toc232861861)

[4.3 Material Staging 18](#_Toc232861862)

[4.4 Confirm Repetitive Manufacturing Inclusive Backflush of Materials 20](#_Toc232861863)

[4.5 Post Processing of Error Records 22](#_Toc232861864)

[4.6 Review Manufacturing Object Pages 23](#_Toc232861865)

[5 Appendix 25](#_Toc232861866)

[5.1 Succeeding Processes 25](#_Toc232861867)

[5.2 Add Planned Order Long Text 25](#_Toc232861868)

[5.3 Usage of the Planning Table for Planning Production Quantities 26](#_Toc232861869)

## Purpose

Overview

Repetitive Manufacturing is commonly used when a production process meets the following criteria:

- The same or similar products are produced over an extended period
- Products aren't manufactured in individually defined lots (instead, a total quantity is produced over a specific period at a certain rate)
- Items always follow the same sequence through the machines and work centers in production
- Routings tend to be simple and don't vary significantly

This scenario begins with Planned Independent Requirements (PIR), which are used to perform demand management functions. Material Requirements Planning (MRP) generates planned orders for the materials to be produced. By using the planning table, the production of materials and capacity on the production lines can be planned. Confirming Repetitive Manufacturing triggers multiple activities, such as finished product goods receipt, backflushing of component materials, posting costs to cost collectors, and creating material and journal entries.

In Repetitive Manufacturing, the master plan is represented by the planning table, which is a tool for operative planning and is used to plan production quantities. In a repetitive manufacturing environment, planning and control are usually performed on a period and quantity basis. The planning table's layout has been designed to support this requirement and is also based on periods to provide a clear, easy-to-interpret overview of materials and production lines.

The planning table is the Production Planner's or MRP Controller's most important tool for planning production quantities. At a glance, they can check production quantities, monitor the available capacity of the production lines, and check the availability of the products produced on each line.

Production quantities can be directly entered and changed in the planning table. 'Nonassigned' production quantities can be assigned to the production lines, or production quantities can be reassigned to alternative production lines.

The planning table can be used for planning with planned orders and production orders. The only prerequisite is that a valid production version must be created in the material master record.

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
| Inventory Manager | SAP_BR_INVENTORY_MANAGER | Inventory Management | SAP_BR_INVENTORY_MANAGER |  |
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV | Production Management - Repetitive Manufacturing | SAP_BR_PRODN_SUPERVISOR_RPTV |  |
| Production Operator - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV | Production Execution - Repetitive Manufacturing | SAP_BR_PRODN_OPTR_RPTV |  |
| Cost Accountant - Production | SAP_BR_PRODN_ACCOUNTANT | Product Costing | SAP_BR_PRODN_ACCOUNTANT |  |
| Administrator | SAP_BR_ADMINISTRATOR | Administration / Administration - Workforce Master Data / Administration - License Compliance / Administration - Data Management / Administration - Output Control | SAP_BR_ADMINISTRATOR / SAP_BUM_SPT_ADMINISTRATION_PC / SAP_EI_SPT_ADM_LC_PC / SAP_CA_SPT_TDR_PC / SAP_OC_SPT_ADMINISTRATION_PC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data to go through the test procedure. If you have installed an SAP Best Practices baseline package, you can use the following baseline package sample data:

Manufacturing/Trading

Production Plant

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | RM12 | RAW12,PD,RepetitiveManuf. |  |
| Material | SG21 | SEMI21,PD,RepetitiveManuf. |  |
| Standard Routing | SG21 | SEMI21,PD,RepetitiveManuf. |  |

Accounting

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Cost Center | 33101301 | Manufacturing 1 (AE) |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component.

| Material | Level | Material Type | Unit | Characteristic of Material |
| --- | --- | --- | --- | --- |
| SG21 | 0 | SEMI | PC | Semifinished Good Repetitive Manuf. |
| RM12 | 1 | RAW | PC | Raw Material |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BNU - Create Costing Run - MDS | You have completed the steps described in the Create Costing Run - MDS Master Data Test Script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS master data script. Posting Period is up-to-date. |

### Preliminary Steps

#### Initializing Material Stock

Purpose

In a real business case, the raw materials are usually purchased from external vendors that are handled by the standard purchasing processing. This process step shows you how to post initial stock directly to the storage location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as an Inventory Manager. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Stock (F1062). | The Manage Stock (F1062) screen displays. |  |
| 3 | Enter Material | Make the following entries and press Enter.Material: RM12Plant: Plant 1 AE (3310) |  |  |
| 4 | Select Stock | Select the Unrestricted-Use Stock icon to add the initial stock for your chosen storage location, such as:Storage Location: Raw mat. stoloc 331C | In the Manage Stock dialog box, the Storage Location, Stock Type, and Current Quantity display according to your entries in the previous steps. |  |
| 5 | Add Stock | Make the following entries and choose Post:Document Date: <today>Posting Date: <today>Stock Change: Initial EntryQuantity: <quantity> | The system displays the following message. The stock has been added.1 document has been created: Material Document XXXXXXXXXX/20XX |  |

#### Create Product Cost Collectors

Purpose

The product cost collector might already be created in connection with other scope items.

For a possible check, if the related ones are already created, please use the App Maintain Product Cost Collectors (KKF6N) with the selection based on the given material/plant data. In case the product cost collector already exists, the selectable entry on the left panel is displayed and this step can be skipped.

Prerequisites

This step can only be executed if product cost planning is activated.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Product Cost Collectors - Production Versions - Collective (KKF6M). |  |  |
| 3 | Enter Relevant Values | On the Create Multiple Product Cost Collectors for Production Versions screen, make the following entries:Plant: 3310Material: SG21Order Type: YBMROnly Repetitive Mfg Mat.: selectChoose Execute. |  |  |
| 4 | Exit | Choose Exit. |  |  |

#### Create Preliminary Cost for the Product Cost Collector

Purpose

This process step shows you how to create preliminary cost for the product cost collector.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Cost Accountant - Production. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Preliminary Cost Estimate - Product Cost Collectors (MF30). | The Creation of Preliminary Cost Estimates for Product Cost Collectors screen displays. |  |
| 3 | Enter Relevant Values | Make the following entries and choose Execute.Costing Date: Current DatePlant: 3310 |  |  |

## Overview Table

The scope item Make-to-Stock Production – Repetitive Manufacturing consists of several process steps provided in the following table.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Planned Independent Requirements](#unique_11) [page ] 11 | Production Planner | Maintain PIRs (F3445) | The Manage PIRs screen displays. |
| [Material Requirements Planning (MRP)](#unique_12) [page ] 12 | Production Planner | Schedule MRP Runs (F1339) | The Application Jobs screen displays. |
| [Adjust Planning in Planning Table](#unique_13) [page ] 14 | Production Supervisor - Repetitive Manufacturing | Manage Repetitive Manufacturing (MF50) | The Planning Table Initial Screen: Change Mode displays. |
| [Check Range of Stock Coverage](#unique_14) [page ] 15 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | The Monitor Material Coverage screen displays. |
| [ATP Check in Planned Orders](#unique_15) [page ] 16 | Production Planner | Manage Planned Orders (F4170) | The Manage Planned Orders screen displays. |
| [Material Staging](#unique_16) [page ] 18 | Production Supervisor - Repetitive Manufacturing | Stage Materials for Production (MF60) | The Material Staging for Planned Orders screen displays. |
| [Confirm Repetitive Manufacturing Inclusive Backflush of Materials](#unique_17) [page ] 20 | Production Supervisor - Repetitive Manufacturing | Confirm Repetitive Manufacturing (MFBF) | The REM Confirmation - Transaction Variant: None screen displays |
| [Post Processing of Error Records](#unique_18) [page ] 22 | Production Operator - Repetitive Manufacturing | Reprocess REM Goods Movements. | The Postprocessing List for Components on Line: Initial Screen displays. |
| [Review Manufacturing Object Pages](#unique_19) [page ] 23 | Any role for production listed in chapter Roles | Search function | The list of search result displays. |

## Test Procedures

This section describes test procedures for each process step that belongs to this scope item.

### Anonymous Forecast and MRP

#### Create Planned Independent Requirements

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create planned independent requirements (PIR), which are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, that is, one planned quantity split over time according to dates.

|  |
| --- |
| Note Instead of creating single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Search for Material | On the Maintain PIRs screen, make the following entries and choose Go:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsMaterial: SG21 | The searched material item displays. |  |
| 5 | Edit PIRs | Select the material item and choose Edit in the upper right corner of the screen.On the screen, enter quantities per period, for example:PIR: 100 for all periodsMake sure the version is active.Version Active: Yes |  |  |
| 6 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

#### Material Requirements Planning (MRP)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

MRP generates planned orders for the material to be produced. Access Manage Material Coverage - New Version (F0251A) app to view the planned order generated for SG21.

Prerequisites

You have to add the Schedule MRP Runs (F1339) app to the Production Planning - MRP Runs group.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for SG21 >Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: SG21Changed BOM Components: selectAll Order BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for SG21 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

Results

The system generates planned orders for material and dependent requirements for raw materials.

#### Adjust Planning in Planning Table

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to plan the production of materials on the production lines.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Repetitive Manufacturing (MF50). |  |  |
| 3 | Enter Details | On the Planning Table Initial Screen: Change Mode screen, make the following entries:Plant: 3310Under Selection by Production Version section, choose radio button Material and then enter material number：Material:SG21Choose Execute. | The Planning Table for Repetitive Manufacturing: Change Mode screen displays. |  |
| 4 | Change the Quantity | In the Material Data section, change any planned quantities in the row 0001 WINDING.If you want to change the periods in the planning table, choose Menu > View > Period > Week (Month or Day) . | In the Total Capacity Data section, you can monitor capacity load utilization of the production lines.More information about usage of the planning table for capacity planning and planning quantities, please refer to appendix Usage of the Planning Table for planning Production Quantities. |  |
| 5 | Save | Choose Save. |  |  |

Result

Material production is planned on production lines and the planned orders are fixed.

When there are quantity changes, log on the SAP Fiori launchpad as a Production Planner, access the Monitor Material Coverage app, and review the planned order number.

#### Check Range of Stock Coverage

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open the Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with the following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | Choose Adapt Filters to add the Material filter if not added, enter the following value, and choose Go:Material: RM12Select the material and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Rescheduling Check (Optional) | In the Stock/Requirements List, the Rescheduling column displays the rescheduling status of the following MRP Elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersYou can choose below icons in the Rescheduling column to perform corresponding actions.Reschedule in (Bring operation forward if the receipt element lies after the requirement date)Reschedule out (Postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment | The corresponding actions are performed. |  |
| 6 | Review the Status and Coverage Days | Make the following entries and choose Refresh:Shortage Definition: Stock Day's Supply |  |  |
| 7 | Return to Home | Choose the Home icon. |  |  |

### ATP Check in Planned Orders

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform an ATP check in planned orders. You can reserve or reset the available quantity of components in planned orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Planned Orders (F4170). | The Manage Planned Orders screen displays. |  |
| 3 | Filter Planned Orders | To select planned orders for an ATP check, you can specify various selection fields (choose Adapt filters to display or hide the selection fields):Planning Plant: 3310Material: SG21Order Opening Date: For orders to produce in next cycleComponent Availability: Availability checked, fully confirmed/partial confirmed/not confirmed/not checked | The target planned orders are filtered and displayed in the Planned Orders panel. |  |
| 4 | ATP Check and Reset for Planned Orders | In the Planned Orders panel, select the planned orders and expand the drop-down list for ATP check. The following 2 options are available:Check Component Availability: check the component availabilityReset Availability: release the reserved available quantity of components | When selecting Check Component Availability, notice the color of the symbol in column Component Availability:Green: components are fully confirmedRed: components are not confirmed or partially confirmedGrey: components are not checked or do not exist; when selecting Reset Availability, the symbol in column Component Availability turns to grey, and the reserved ATP quantity is released. |  |

### Material Staging

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to stage materials for production. In case there is sufficient stock available on the production storage location 331B, no line items are generated. If you want to print the Pull List, please also execute relevant steps and check printing result.

Prerequisites

Stock must be available.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Stage Materials for Production (MF60). | The Material Staging for Planned Orders screen displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute.Staging Types: SLoc.Level (Activate checkbox)Plant: 3310Selection Horizon for Remts: <A date>Note Requirements falling on a later date will not be taken into account in the pull list.Planned Orders: <Planned Order Number> Access Manage Material Coverage - New Version (F0251A) app as a Production Planner to view the planned order generated for SG21.Bulk Material: <Adapt Indicator if necessary> | The Pull List: Storage Location Level screen displays. |  |
| 4 | Choose Replenishment Proposal | Select the required line items from the left-hand margin and choose Replenishment proposal from the Top of the screen. |  |  |
| 5 | Choose Replenishment Elements | Review the staged quantity and choose Replenishment elements. |  |  |
| 6 | Enter Replenishment Storage Location | On the bottom half of the split screen, select the lines and enter the replenishment storage location 331C. |  |  |
| 7 | Choose Print | If you want to print the Pull List, you can execute following printing steps, else please go directly to step 13.Choose Print at the upper right of the screen. |  |  |
| 8 | Print List Selection | In the popup window Print List Selection, choose following entries and choose Continue :Print List Selection: Replenishment Proposals | The print list will be displayed. |  |
| 9 | Check Print List | Check the print list, and choose Print at the upper right of the screen. |  |  |
| 10 | Select Output Parameters | In the popup window Print List Selection , choose following entries and choose Continue.Output Device: expand Name of Device list in the system, choose a known device, or the one with exactly the same name with the Queue you created in Preliminary steps, for example, Pull_List_Print (Note: if the Output Device does not exist, please wait for some time until it is valid)Print Time: Immediately | Message “Spool request (number XXXX) sent to SAP printer XXXX” indicates successful printing. |  |
| 11 | Go Back | Go back to the stage screen before Printing. |  |  |
| 12 | Select Stage | Select the replenishment element in the bottom half of the screen, and choose Stage at the middle of the screen. |  |  |
| 13 | Save | Choose Save (Ctrl+S). |  |  |

Result

Missing materials are transferred to the shop floor from the designated storage area.

### Confirm Repetitive Manufacturing Inclusive Backflush of Materials

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This activity executes multiple activities in a single step, such as finished product goods receipt, backflush of component materials, posting of costs to cost collector, and creation of material and Journal Entry.

Errors can occur in backflushing. For example, there may not be sufficient warehouse stock available or important data, such as the issue storage location, may be missing. You then have the following options:

Make corrections immediately in a component overview.

Backlogs are created for the complete requirement quantities of the components with errors.

You can process these backlogs later. If negative stocks are allowed for the material in the storage location, the system posts negative stock quantities in certain circumstances.

|  |
| --- |
| Note Goods Receipt's Goods Movement Type is 131 and Goods Issue's Goods Movement Type is 261. |

|  |
| --- |
| Note If you enabled scope item Handling Unit Management (4MM), you can create handling units at the end of production and post goods receipts for handling units. By this way, the stock can be posted directly into storage and is available for picking. For details, refer to scope item 4MM. |

Prerequisite

Planned orders must exist.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Repetitive Manufacturing role. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Repetitive Manufacturing (MFBF). | The REM Confirmation - Transaction Variant: None screen displays. |  |
| 3 | Enter Selection Data | Make the following entries:Assembly backflush: XMake-to-Stock: system proposesPlanned Order: Planned Order Number (from previous step)Note When the system proposes quantities, change as required.Press Enter. | Note down the Posting Date and Document Date on the screen. |  |
| 4 | Post with Corrections | Choose Post with Correction.Select the production version, if prompted. |  |  |
| 5 | Post | Choose Post. |  |  |

|  |
| --- |
| Note The app Confirm Repetitive Manufacturing (MFBF) can be used to perform Reporting Point (RP) confirmation and backflush.Process step:Reporting point confirmation related steps can be performed by logging in as the Production Operator - Repetitive Manufacturing role.To perform reporting point confirmation in the app, enable the indicator for RP Backflush and provide the operation number of the reporting point in the field Reporting Point.Purpose of RP confirmation:Reporting Points are operations in the routing where milestone confirmation is enabled using the appropriate control key.Reporting Point (RP) confirmation allows users to:Record and calculate the work in process quantitiesRecord component consumption at a specific operation (reporting point)Record scrap quantities at a specific operation (reporting point)Prerequisites for RP confirmation:Enable RP backflush indicator during configuration of the appropriate REM profile and assign the REM profile to the material master. The REM profile can be adjusted to make RP backflush optional or mandatory.In routing, use control keys that have milestone confirmation enabled and assign the routing to appropriate production version.A standard cost estimate or cost estimate based on production version is completed for the material.Additional processes related to reporting point confirmation available for this role are:Use the app Display Reporting Point Quantity (MF26) to provide an overview of confirmation quantities at reporting points.Use the app Reset Reporting Point Confirmations (MF4R) to reverse the confirmation and backflush done at a reporting point. |

Result

Semi-finished material is received into stock and raw materials are issued from stock. To view the Material document, log on to the SAP Fiori launchpad as a Warehouse Clerk, and then open Material Documents Overview (F1077).

### Post Processing of Error Records

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use this function to create a list of components that have to be postprocessed to post process backlogs from backflushing.

Prerequisites

Material movements are missing for previous backflush operations.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Reprocess REM Goods Movements (MF47). | The Postprocessing List for Components on Line: Initial Screen screen displays. |  |
| 3 | Enter Selection Data | Make the following entries and choose Run:Plant: 3310Posting Date and Document Date could be retrieved from previous steps. | The system displays a list of all assemblies that correspond to the selection criteria and that have components to be postprocessed. This list is sorted by assemblies and production versions. If you have to correct the components or if you want to check availability, select the appropriate assembly and choose Change Selected Postprocessing Recs. The system displays the components of the selected assembly. |  |
| 4 | Save | Review the generated list, and then choose Post. |  |  |

### Review Manufacturing Object Pages

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the different objects pages available for different roles in the area of manufacturing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner.Note You can use any role in the Roles section above. | The SAP Fiori launchpad displays. |  |
| 2 | Start Search | Choose Search in the upper right area of the launchpad. | An input field displays. |  |
| 3 | Search Criteria | Make the following entries and choose Search:Products: Material (see the Master Data section) | The system displays a list of objects that use the selected material. |  |
| 4 | Display Object | In the All field, choose Down arrow.Select an object and choose Search. | The list of objects is limited to the object type selected. If no object is selected, a message is displayed instead. |  |
| 5 | Tailor the Result Display | Below the search line, choose a symbol (for example, filter, display as table, sort) to filter the results list. | The results list is filtered according to your selections. |  |
| 6 | Repeat Steps | Repeat steps 1-5 for any other role in this test script and any other object offered in the search function. | The list of objects offered for search differs by the role you used to log on. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3F0 - Event-Based Production Cost Posting (Optional) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Starting from SAP S/4HANA Cloud Public Edition 2302 release, the default Best Practice content is based on event-based result analysis for new customers who install and add new countries only, rather than previous period-end posting. For existing customers (who activated content before 2302 release), the default process remains unchanged to Period-End Closing - Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic, please refer to [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Event-Based Production Cost Posting. |

### Add Planned Order Long Text

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This chapter shows you how to add long text for planned order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Change Planned Order (MD12). | The Change Planned Order: Initial Screen displays. |  |
| 3 | Enter Planned Order | Make the following entry and choose Continue:Planned Orders: <Planned Order Number> | The Change Planned Order: Run schedule quantity screen displays. |  |
| 4 | Enter Long Text | Choose the tab: Long Text, enter the text and choose Save. | Planned order is changed. |  |

### Usage of the Planning Table for Planning Production Quantities

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This chapter provides a detailed procedure and example for adjusting planning table for a certain period of time and quantity. This will be different when running the tests. You can manually assign production quantities to production lines, and taking capacities into account also.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Repetitive Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the Planning Table | Open Manage Repetitive Manufacturing (MF50). | The Planning Table Initial Screen: Change Mode displays. |  |
| 3 | Enter Details | Make the following entries and choose Execute Planning Table:Material:SG21Plant: 3310Choose Execute. | The Planning Table for Repetitive Manufacturing: Change Mode screen displays.The system displays typically several production lines and materials according to the selection criteria you entered. In our case we only use the Capacity WINDING. |  |

Scheduling in the Planning Table

If you use the planning table in conjunction with capacity planning, the system carries out a lead time scheduling for the planned orders. In scheduling, the system calculates the production start and finish dates of the orders. The finish date determines the period to which the production quantities are assigned in the planning table. The system also calculates the dates of the planning operation (that is, the operation with the work center used for scheduling - usually the production line) which are displayed separately.

Capacity Planning in the Planning Table

For each production line and per period, the system displays the available capacity, capacity requirements and the capacity load as a percentage. The capacity data is recalculated after making any changes. Therefore, the planner has an overview of the capacity situation of the production lines and can react quickly to overloads.

Capacity Calculation Example

In our case, values of Standard Routing for SG21:

| Base Quantity | Unit | Setup | Unit | Machine | Unit |
| --- | --- | --- | --- | --- | --- |
| 100 | PC | 10 | min | 10 | min |

Result example of capacity requirements for machine WINDING:

| Required Quantity | Capacity Requirement | Default Capacity by Day | Capacity Load (%) |
| --- | --- | --- | --- |
| 2000 PC | 3.5 H (210 min) | 8 H | 43.75 |
| 3500 PC | 6 H (360 min) | 8 H | 75 |

Continue with the following steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 4 | Change Quantity | In the Material Data section, change planned quantities in the row 0001 WINDING. Change quantities for date 04/17/17 from 2000 to 3500, and save the quantities. Then see results in Capacity Data and Available Quantity. | Check production quantities, monitor the available capacity of the production lines and check up on the availability situation. |  |

In the following case, we have 2000 PC planned independent requirements for SG21 in 04/19/17. The planned quantity for production in 04/18/17 is 2000 PC, and basic dates for the order finished in 04/19/17.

| Total Capacity Data | Unit | Due | 04/17/17 | 04/18/17 | 04/19/17 | 04/20/17 | 04/21/17 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WINDING /001 Spring | % |  | 43.75 |  |  |  |  |
| Requirement - Default Capacity | H |  | 4 |  |  |  |  |
| Available - Default Capacity | H |  | 8 | 8 | 8 | 8 | 8 |

| Material Data | Unit | Due | 04/17/17 | 04/18/17 | 04/19/17 | 04/20/17 | 04/21/17 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Available Quantity | PC |  |  |  |  |  |  |
| Sum Total Requirements | PC |  |  |  | 2000 |  |  |
| 0001 WINDING | PC |  | 2000 |  |  |  |  |

After changing planned quantities for date 04/18/17 from 2000 to 3500, updated planning table as below:

| Total Capacity Data | Unit | Due | 04/17/17 | 04/18/17 | 04/19/17 | 04/20/17 | 04/21/17 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WINDING /001 Spring | % |  | 75 |  |  |  |  |
| Requirement - Default Capacity | H |  | 6 |  |  |  |  |
| Available - Default Capacity | H |  | 8 | 8 | 8 | 8 | 8 |

| Material Data | Unit | Due | 04/17/17 | 04/18/17 | 04/19/17 | 04/20/17 | 04/21/17 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Available Quantity | PC |  |  |  | 1500 | 1500 | 1500 |
| Sum Total Requirements | PC |  |  |  | 2000 |  |  |
| 0001 WINDING | PC |  | 3500 |  |  |  |  |

Continue with the following steps:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 5 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 6 | Check with App Monitor Material Coverage | Open Monitor Material Coverage - Net / Individual Segments (F2101A). Open and review the planned order number. | Quantities of the planned order for date 04/19/17 is changed from 2000 to 3500. Available Qty in the follow-up period are changed accordingly also. |  |

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
> Flagged while digesting this document, not verified: Overview Table lists Production Supervisor - Repetitive Manufacturing as the role for Material Staging (MF60) and Confirm Repetitive Manufacturing (MFBF), but the test procedures for both steps say to log on as Production Operator - Repetitive Manufacturing.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Planning table capacity example is internally inconsistent: text computes 2000 PC as 3.5 H (210 min) at 43.75% load, but the planning table shows Requirement - Default Capacity of 4 H at 43.75%; the quantity change is also dated 04/17/17 in step 4 but 04/18/17 in the later description, while the table shows the quantity in the 04/17/17 column.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-stock-production-discrete-manufacturing-bj5-ae-sap]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJH_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 48,341 chars in the whole document
