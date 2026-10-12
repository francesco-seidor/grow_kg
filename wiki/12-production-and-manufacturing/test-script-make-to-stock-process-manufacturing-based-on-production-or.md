---
id: 12-production-and-manufacturing/test-script-make-to-stock-process-manufacturing-based-on-production-or
title: "Test Script: Make-to-Stock – Process Manufacturing Based on Production Order (2UG_AE) (2UG_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud Public Edition test script for scope item 2UG_AE: MTS process manufacturing via production orders, from PIRs and MRP to confirmation and scrap review."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/make-to-stock-process-manufacturing]
aliases: [2UG_S4CLD2608_BPD_EN_AE]
keywords: [Make-to-Stock Process Manufacturing, make-to-stock production, process manufacturing, production orders, planned independent requirements, material requirements planning, goods issue, production confirmation, test scripts, stock requirements evaluation]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UG_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-871
topic: 12-production-and-manufacturing/make-to-stock-process-manufacturing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Make-to-Stock – Process Manufacturing Based on Production Order (2UG_AE) (2UG_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UG_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Make-to-Stock Process Manufacturing** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Make-to-Stock – Process Manufacturing Based on Production Order (2UG_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232850551)

[2 Prerequisites 4](#_Toc232850552)

[2.1 System Access 4](#_Toc232850553)

[2.2 Roles 4](#_Toc232850554)

[2.3 Master Data, Organizational Data, and Other Data 5](#_Toc232850555)

[2.4 Business Conditions 6](#_Toc232850556)

[2.5 Preliminary Steps 7](#_Toc232850557)

[2.5.1 Create Raw Material Stock 7](#_Toc232850558)

[3 Overview Table 9](#_Toc232850559)

[4 Test Procedures 11](#_Toc232850560)

[4.1 Anonymous Forecast and MRP 11](#_Toc232850561)

[4.1.1 Create Planned Independent Requirements 11](#_Toc232850562)

[4.1.2 Material Requirements Planning 12](#_Toc232850563)

[4.1.3 Evaluate the Stock / Requirements Situation 14](#_Toc232850564)

[4.2 Production Order Processing 16](#_Toc232850565)

[4.2.1 Create Production Order 16](#_Toc232850566)

[4.2.2 Review Production Order 17](#_Toc232850567)

[4.2.3 Goods Issue of Batch-Managed Components 18](#_Toc232850568)

[4.2.3.1 Goods Issue via Pick List 18](#_Toc232850569)

[4.2.3.2 Manual Goods Issue (Instead of Picking List) 19](#_Toc232850570)

[4.2.4 Monitor Order Progress 20](#_Toc232850571)

[4.2.5 Post Goods Receipt for Order 21](#_Toc232850572)

[4.2.6 Confirm Production incl. Component Backflush 22](#_Toc232850573)

[4.2.7 Review Production Order Confirmation 24](#_Toc232850574)

[4.2.8 Review Scrap Report 25](#_Toc232850575)

[5 Appendix 27](#_Toc232850576)

[5.1 Process Integration 27](#_Toc232850577)

[5.1.1 Succeeding Processes 27](#_Toc232850578)

## Purpose

Overview

This scope item enables production planning in make-to-stock scenarios and quick reactions to incoming sales orders. The focus is on process manufacturing (supported through production orders).

The process starts with the creation of a demand forecast for semi-finished goods represented by planned independent requirements (PIRs). Based on PIRs, Material Requirements Planning (MRP) creates a production plan for semi-finished goods and explodes the entire bill of material structure. As a result, raw material demand is planned.

Production planners can analyze and change the planned-order-based production plan manually.

Raw material demand leads to purchase requisitions that trigger alternative procurement scenarios referenced in this scope item.

The production process itself is entirely covered via conversion of planned orders to production orders, order release, direct material issue or backflush, confirmation of operations and goods receipt posting. Order-based target and actual costs are created, ensuring fully integrated material and value streams.

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
| Production Planner | SAP_BR_PRODN_PLNR | Production Planning | SAP_BR_PRODN_PLNR |  |
| Production Supervisor - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC | Production Management - Discrete Manufacturing | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Production Operator - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC | Production Execution - Discrete Manufacturing | SAP_BR_PRODN_OPTR_DISC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |
| Production Engineer - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC | Production Engineering - Discrete Manufacturing | SAP_BR_PRODN_ENG_DISC |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure.

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | SGPI001-V00 | MTS processing for process industry, batch managed | Unit of measures is kg. |
| Material | RMPI001 | Raw material, backflush | Input 1 (Water) |
| Material | RMPI002 | Raw material, batch managed | Input 2 (Agent 2) |
| Material | RMPI003 | Raw material, batch managed | Input 3 (Agent 3) |
| Material | RMPI004 | Raw material, batch managed | Input 4 (Agent 4) |
| Material | RMPI005 | Raw material, batch managed | Input 5 (Blue Color) |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage location for production |  |

Bill of Material Structure

This overview shows the bill of material structure and the usage of each component.

| Material | Level | Material Type | Unit | Base Quantity |
| --- | --- | --- | --- | --- |
| SGPI001-V00 | 0 | HALB | KG | 100 |
| RMPI001 | 1 | ROH | KG | 86 |
| RMPI002 | 1 | ROH | KG | 2 |
| RMPI003 | 1 | ROH | KG | 3 |
| RMPI004 | 1 | ROH | KG | 4 |
| RMPI005 | 1 | ROH | G | 5000 |

For more information on creating these master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Master Data Script Text |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNJ | Create Production Work Center - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| BNL | Create Routing - MDS |
| BLD | Create Production Version - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item ID | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the Test Script Standard Cost Calculation (BEG). |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the Create New Open MM Posting Period - MDS (BNZ) master data script. Posting Period is up to date. |

### Preliminary Steps

#### Create Raw Material Stock

Purpose

In a real business case, the materials are usually purchased from external suppliers in that case, process is covered by the standard purchasing or subcontracting processes. This process step shows you how to post initial stock directly to the Issue Storage Location.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | Screen name adapts according to entries. |  |
| 3 | Choose Goods Receipt - Other | Make the following entries and choose Enter:Trans./Event: Goods ReceiptReference Document: OtherMovement Type: 561 | Screen name after entries are made. |  |
| 4 | Specify Material | On the Material tab, make the following entries:Material: RMPI001 | Ensure that detail data is expanded. |  |
| 5 | Specify Quantity | On the Quantity tab, make the following entries:Qty in Unit of Entry: For example, 1000 |  |  |
| 6 | Specify Plant and Storage Location | On the Where tab, make the following entries:Plant: 3310Storage location: 331B |  |  |
| 7 | Check Item | Press Enter, and ensure Item OK is selected. |  |  |
| 8 | Add Other Materials | Choose Next Item, then repeat the steps 4 to 7 for the following materials:Material: RMPI002Material: RMPI003Material: RMPI004Material: RMPI005 |  |  |
| 9 | Post Goods Movement | Choose Post. | Material document XXX is posted.Materials are available in stock. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | App/Transaction | Expected Results |
| --- | --- | --- | --- |
| [Create Planned Independent Requirements](#unique_9) [page ] 11 | Production Planner | Maintain PIRs (F3445) | The Maintain PIRs screen displays. |
| [Material Requirements Planning](#unique_10) [page ] 12 | Production Planner | Schedule MRP Runs (F1339) | The Application Jobs screen displays. |
| [Evaluate the Stock / Requirements Situation](#unique_11) [page ] 14 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | The Monitor Material Coverage - Net / Individual Segments (F2101A) screen displays. |
| [Create Production Order](#unique_12) [page ] 16 | Production Planner | Convert Planned Orders - to Production Orders (CO41) | The Collective Conversion of Planned Orders: Initial screen displays. |
| [Review Production Order](#unique_13) [page ] 17 | Production Supervisor - Discrete Manufacturing | Display Production Order (CO03) | The Production Order Display: Initial Screen displays. |
| [Goods Issue via Pick List](#unique_14) [page ] 18 | Production Operator - Discrete Manufacturing | Pick Components for Production Orders (CO27) | The Picking List: Initial Screen displays. |
| [Manual Goods Issue (Instead of Picking List)](#unique_15) [page ] 19 | Warehouse Clerk | Post Goods Movement (MIGO) | The Post Goods Movement (MIGO) screen displays. |
| [Monitor Order Progress](#unique_16) [page ] 20 | Production Supervisor - Discrete Manufacturing | Manage Production Orders (F2336) | The Manage Production Orders (F2336) screen displays |
| [Post Goods Receipt for Order](#unique_17) [page ] 21 | Warehouse Clerk | Post Goods Receipt for Production Order (F3110) | The Post Goods Receipt for Production Order (F3110) screen displays. |
| [Confirm Production incl. Component Backflush](#unique_18) [page ] 22 | Production Operator - Discrete Manufacturing | Confirm Production Operation (F3069) | The Enter Order and Operation screen displays. |
| [Review Production Order Confirmation](#unique_19) [page ] 24 | Production Supervisor - Discrete Manufacturing | Manage Production Operations (F2335) | The Manage Production Operations (F2335) screen displays. |
| [Review Scrap Report](#unique_20) [page ] 25 | Production Supervisor - Discrete Manufacturing | Material Scrap - Maximum Deviation (F2035) | The Material Scrap - Maximum Deviation (F2035) screen displays. |

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

This process step shows you how to use planned independent requirements (PIR) to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, that is, one planned quantity split over time according to dates.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445). | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: SGPI001-V00 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Edit PIRs | Select the material item, and choose Edit on the upper-right part of the screen.On the screen, enter quantities per period, for example:PIR: 100Make sure the version is active.Version Active: Yes |  |  |
| 7 | Save PIRs Draft | Choose Save at the bottom right. | The PIRs are saved. |  |

#### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to use material requirements planning to tailor available capacities and receipts on time to suit requirement quantities. You can use MRP or consumption-based planning for this purpose. Single-item multilevel requirement planning is carried out for plant 3310.

Prerequisite

The product for PI (SGPI001-V00) is planned at plant level. There is now a requirement for the material in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for SGPI001-V00>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: SGPI001-V00Changed BOM Components: <select>Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for SGPI001-V00 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate the Stock / Requirements Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor the material coverage situation for the material (SGPI001-V00) after the requirements planning has been carried out.

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | In the search area, make the following entries and choose Go.Material: SGPI001-V00Material: RMPI001Material: RMPI002Material: RMPI003Material: RMPI004Material: RMPI005Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock / Requirement List | Select the corresponding material in the Materials list on the left. | The detailed Stock / Requirements List for each material displays. |  |
| 6 | Display Planned Order | In the Materials list, choose the following materials for which you want to check the planned order:Material: SGPI001-V00On the right screen, choose PldOrd XXXX in the MRP Element column. | The Planned Order selected displays in the dialog box.If there is no shortage for those materials, the planned order will not be generated.If you want to display more information about the planned order, choose Document Info at the bottom of this dialog box. |  |
| 7 | Rescheduling Check (Optional) | In the Stock/Requirements List, the Rescheduling column displays the rescheduling status of the following MRP Elements.PurReqPurchase OrdersPlanned OrdersProduction OrdersProcess OrdersIf necessary actions can be performed, below Icons in the Rescheduling column are displayed via pushing buttons. Push the buttons and corresponding actions perform directly.Reschedule in (Bring operation forward if the receipt element lies after the requirement date)Reschedule out (Postpone operation, if the receipt element lies before the requirement date)Plan Process according to scheduleCancel ProcessExcess StockExcess in individual segment | Corresponding actions perform. |  |

### Production Order Processing

#### Create Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create production orders. Because the order release is executed automatically, production can start immediately.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Convert Planned Orders - to Production Orders (CO41) | The Collective Conversion of Planned Orders: Initial screen displays. |  |
| 3 | Enter Restriction | Make the following entries and choose Run Selection:Planning Plant: 3310Production Plant: 3310Prodn. Supervisor: YB5Order Type: YBM5 | The system displays a list of all planned orders, which match the restriction. |  |
| 4 | Convert Planned Order to Production Order | Select the planned order for conversion for following material, and then choose Convert.Material: SGPI001-V00 | Planned orders are converted to production orders. Make a note of the production order numbers.Note It is possible to change order quantities (such as merging the quantities of 2 planned orders into one order. You may then delete the obsolete planned orders from the selection list before executing order conversion. Run MRP to delete the obsolete planned orders from the database (the planned orders must not be firmed, otherwise MRP would leave them untouched). |  |

#### Review Production Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the created production orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Production Order (CO03). | The Production Order Display: Initial Screen displays. |  |
| 3 | Enter Production Order Number | Make the following entries and choose Continue:Production Order: XXXX (From previous steps) | The Production order Display: Header screen displays.On this screen, you find the order’s detailed information.Production orders are reviewed and checked within your responsibility area. |  |

#### Goods Issue of Batch-Managed Components

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Context

The withdrawal of the raw materials is used for the order. This withdrawal can be done by using the picking list or doing a manual goods issue.

|  |
| --- |
| Note If the material is set for backflush (in material master or resource), the withdrawing is done automatically after you confirm the operation or the whole order. Backflushing should not be used for batch-managed components (to ensure that the physically picked and consumed batch is the same as the recorded batch). |

Prerequisites

Ensure that sufficient material is present on stock. You can check the stock levels using the app Monitor Stock/Requirements List available for the Production Planner role.

##### Goods Issue via Pick List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The released production order is now ready for picking. This process step shows you how to issue all materials that are moved to the production storage location to order with the pick list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Production Orders (CO27). | The Picking List: Initial Screen displays. |  |
| 3 | Enter Restriction and Execute | Make the following entries and choose Execute:Profile: 000002Production Order: XXXX (from previous steps)Plant : 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Select the relevant reservations and choose Picking on the upper left. | The Picking list screen displays. On this screen, a list of all the selected reservations displays. |  |
| 5 | Batch Determination | Some materials are management by batch, for example: RMPI002, select corresponding line item and choose Batch Determination. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Enter Detail | Make the following entries and choose Copy.Split quantity: Quantity. | Go back to the Picking list screen. |  |
| 7 | Post | Choose Post to post the goods movements. | The goods movements have been posted. |  |

##### Manual Goods Issue (Instead of Picking List)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how the system performs a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Production Order Number | Make the following entries and choose Enter:Trans./Event: Goods IssueReference Document: OrderOrder number: <Order ID> (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Check Each Item | For each item shown, select Item OK. | Ensure that detail data is expanded. |  |
| 5 | Perform Batch Determination | Choose Stock Determ. for All. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Copy Batch Determination Result | Check the required batch and choose Copy. Repeat this step for all the materials you selected. | The Goods Issue Order XXX screen displays. In addition, the batch numbers have been determined. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements have been posted. |  |

#### Monitor Order Progress

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to generate a worklist for production orders, components and operations, with user-specific selection and layout settings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Orders (F2336). | The Manage Production Orders (F2336) screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | Choose the user icon and select App Settings. Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE (3310)MTS DI - Valuated - Process (YB5)Choose Back. | If the Plant 1 AE (3310) is blank on the Area of Responsibility (Supervisor) screen, choose Add to select it and then choose OK.For other plant entries on the Area of Responsibility (Supervisor) screen, choose Delete to remove the others and then choose OK. |  |
| 4 | Select Production Order | On the Manage Production Orders (F2336) screen, enter the following search condition as filter and choose Go.Material: SGPI001-V00Plant: 3310Choose Adapt Filters to display more selection filter if needed. | Selected order displays. |  |
| 5 | Check Detailed Order Information | Check detailed information for selected production orders. |  |  |

|  |
| --- |
| Note To display the inspection lots, you need further authorizations of SAP_BR_QUALITY_TECHNICIAN (app Display Inspection Lots). Ensure that your user has the appropriate authorizations if you want to review the inspection lots. Else this section is empty even though inspection lots are available. |

#### Post Goods Receipt for Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the production order. You may post goods receipt for the total quantity, but already partial quantities of the products are required for further processing, such as consumption for further production or subsequent deliveries for sales orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Production Order (F3110). | The Post Goods Receipt for Production Order (F3110) screen displays. |  |
| 3 | Enter Details | On the Post Goods Receipt for Production Order (F3110) screen, make the following entries and choose Enter:Order: XXXX (from previous steps) |  |  |
| 4 | Select the Item | In the Items section, select the item. | The Item Details screen displays. |  |
| 5 | Input Production Date | In the Production and Shelf Life Expiration Date section, make the following entries and choose Apply:Production Date: <Current Date> | The Goods Receipt screen displays. |  |
| 6 | Post | Choose Post. | Goods receipt for production order has been done. |  |

#### Confirm Production incl. Component Backflush

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

In the process industry, GR and GI postings are usually done immediately during the physical movements of the materials to ensure batch traceability and data consistency. Order confirmations with backflush are done at shift end or day end. The sum of the GI and GR quantity for the given order is then recorded within the confirmation and scrap quantities (optional). The time ticket confirmation allows recording either the default times for machine and labor usage, or record actual times for major deviations.

Prerequisite

The goods receipt posting for the order product (SGPI001-V00) has been done in a previous step and the total quantity was recorded.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Production Operation (F3069). | The Enter Order and Operation screen displays. |  |
| 3 | Enter Order Number and Operation | On the Enter Order and Operation screen, make the following entries, and choose Go:Order: XXXX (from previous steps)Operation: 0010 | The Confirm Production Operation (F3069) screen displays. |  |
| 4 | Enter Fields in Quantities Section | In the Quantities section, make the following entries:Yield: <enter the amount you want to confirm>Scrap: <enter the amount you want to scrap> |  |  |
| 5 | Check Material Movements | In the Material Movements section, check the material list. | The system shows you an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation.The material RMPI001 is set for backflush (in material master) so that the withdrawing is done automatically after you confirm the operation. |  |
| 6 | Enter Fields in Activities Section | In the Activities section, make the following entries:Machine: <enter the setup time you want to confirm for this operation>Labor: <enter the setup time you want to confirm for this operation> |  |  |
| 7 | Save your Entries | Choose Post and Complete to make final confirmation for this operation. | Confirmation has been created. |  |
| 8 | Repeat Steps | Go back and repeat steps 3 to 7 for operation number 0020 and 0030. |  |  |

#### Review Production Order Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review confirmations for the orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Production Operations (F2335). | The Manage Production Operations screen displays. |  |
| 3 | Check Default Area of Responsibility (Supervisor) | On the Manage Production Operations screen, choose the user icon and select App Settings.Choose against Area of Responsibility Production Supervisor.Check if only this entry displays:Plant 1 AE (3310)MTS DI - Valuated - Process (YB5)Choose AOR Status button of this entry if not assigned, choose AOR Status button of the corresponding entry to unassign any other entries, and then choose Back. |  |  |
| 4 | Enter Search Condition | On the Manage Production Operations screen, enter the following search condition as filter and choose Go.Material: SGPI001-V00Plant: 3310Choose Adapt Filters to display more selection filter if needed. | Selected operation displays. |  |
| 5 | Check Detailed Operation Status | Check detailed information for selected production operations. | Detailed operations status displays. |  |

#### Review Scrap Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review confirmations for the orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Material Scrap - Maximum Deviation (F2035). | The Material Scrap - Maximum Deviation (F2035) screen displays. |  |
| 3 | Investigate Scrap | Materials Scrap can display by various filters.You could choose the corresponding material in Chart to display the details. |  |  |

## Appendix

### Process Integration

#### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

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
- related-to :: [[12-production-and-manufacturing/make-to-stock-process-manufacturing-based-on-process-order-bj8-ae-test]]
- related-to :: [[12-production-and-manufacturing/make-to-stock-with-silo-material-process-manufacturing-3ul-ae-test-scr]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-stock-with-co-and-by-products-process-manufacturin]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/2UG_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 41,576 chars in the whole document
