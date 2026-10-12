---
id: 12-production-and-manufacturing/make-to-stock-process-manufacturing-based-on-process-order-bj8-ae-test
title: Make-to-Stock – Process Manufacturing Based on Process Order (BJ8_AE) – Test Script (BJ8_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item BJ8_AE: make-to-stock process manufacturing via PIRs, MRP, process orders, goods issue, confirmation and goods receipt."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/make-to-stock-process-manufacturing]
aliases: [BJ8_S4CLD2608_BPD_EN_AE]
keywords: [Make-to-Stock Process Manufacturing, process manufacturing, make-to-stock, process orders, planned independent requirements, material requirements planning, goods issue, production confirmation, goods receipt, test scripts]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJ8_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-1271
topic: 12-production-and-manufacturing/make-to-stock-process-manufacturing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Make-to-Stock – Process Manufacturing Based on Process Order (BJ8_AE) – Test Script (BJ8_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJ8_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Make-to-Stock Process Manufacturing** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Make-to-Stock – Process Manufacturing Based on Process Order (BJ8_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232861766)

[2 Prerequisites 4](#_Toc232861767)

[2.1 System Access 4](#_Toc232861768)

[2.2 Roles 4](#_Toc232861769)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232861770)

[2.4 Business Conditions 6](#_Toc232861771)

[2.5 Preliminary Steps 7](#_Toc232861772)

[2.5.1 Initial Raw Material Stock 7](#_Toc232861773)

[3 Overview Table 9](#_Toc232861774)

[4 Test Procedures 11](#_Toc232861775)

[4.1 Anonymous Forecast and MRP 11](#_Toc232861776)

[4.1.1 Create Planned Independent Requirements 11](#_Toc232861777)

[4.1.2 Material Requirements Planning 12](#_Toc232861778)

[4.1.3 Evaluate the Stock / Requirement Situation 14](#_Toc232861779)

[4.2 Process Order Processing 16](#_Toc232861780)

[4.2.1 Create Process Order 16](#_Toc232861781)

[4.2.2 Review Process Order 18](#_Toc232861782)

[4.2.3 Goods Issue of Batch-Managed Components 20](#_Toc232861783)

[4.2.3.1 Goods Issue via Pick List 21](#_Toc232861784)

[4.2.3.2 Manual Goods Issue (Instead of Picking List) 22](#_Toc232861785)

[4.2.4 Monitor Order Progress 23](#_Toc232861786)

[4.2.5 Confirm Production incl. Component Backflush 25](#_Toc232861787)

[4.2.6 Post Goods Receipt for Process Order 26](#_Toc232861788)

[4.2.7 Review Process Order Confirmation 28](#_Toc232861789)

[4.2.8 Review Scrap Report 30](#_Toc232861790)

[4.3 Review Manufacturing Object Pages 31](#_Toc232861791)

[5 Appendix 33](#_Toc232861792)

[5.1 Succeeding Processes 33](#_Toc232861793)

[5.2 Process Order Creation with Approved Master Recipe (Optional) 34](#_Toc232861794)

[5.2.1 Preceding Procedure: Product Change Management with Change Records - Process Industries (5QC) 34](#_Toc232861795)

[5.2.2 Create Process Order with Approved Master Recipe 35](#_Toc232861796)

[5.3 Additional Functional Information 36](#_Toc232861797)

## Purpose

Overview

This scope item enables production planning in make-to-stock scenarios and quick reactions to incoming sales orders. The focus is on process manufacturing (for example, supported through process orders or batch management).

The process starts with the creation of a demand forecast for finished goods represented by planned independent requirements (PIRs). Based on PIRs, Material Requirements Planning (MRP) creates a production plan for finished goods, semifinished components, and raw materials. Production planners can analyze and change the planned-order-based production plan manually.

Raw material demand leads to purchase requisitions that trigger alternative procurement scenarios referenced in this scope item.

The production process itself is entirely covered via conversion of planned into process orders, order release, direct material issue or backflush, confirmation of operations, and goods receipt posting. Order-based target and actual costs are created, ensuring fully integrated material and value streams.

Regulated industries are also supported with process order approval based on approved master data (master recipe, BOM, and so on).

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
| Production Supervisor - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC | Production Management - Process Manufacturing | SAP_BR_PRODN_SUPERVISOR_PROC |  |
| Production Operator - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC | Production Execution - Process Manufacturing | SAP_BR_PRODN_OPTR_PROC |  |
| Warehouse Clerk | SAP_BR_WAREHOUSE_CLERK | Inventory Processing | SAP_BR_WAREHOUSE_CLERK |  |

### Master Data, Organizational Data, and Other Data

The organizational structure and master data of your company has been created in your system during activation. The organizational structure reflects the structure of your company. The master data represents materials, customers, and vendors, for example, depending on the operational focus of your company.

|  |
| --- |
| Caution Update Behavior of Predelivered Demo DataIn non-productive environments (such as starter systems, sandbox systems, or partner demo systems), SAP initially deploys demo data for your selected scope. You can use this data to test and evaluate business processes.In a customer system, you can receive new or updated demo data after initial activation with further scope enhancements, provided the existing demo data wasn't changed in an incompatible way. If activation errors occur due to incompatible changes in demo data, you're responsible for resolving them. If you don't resolve the errors within a specific time frame, SAP reserves the right to deactivate demo data in your systems. In this case, you can continue by creating your own demo data. Alternatively, you can request that your systems be reprovisioned if you want to work with predelivered demo data again.In partner systems, you can use the demo data deployed with the initial activation. No additional demo data will be deployed in the system with scope enhancements. You can only create additional demo data manually. |

Use your own master data or the following sample data to go through the test procedure:

Manufacturing / Trading

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG29 | FIN29,MTS-PI,PD,Batch-ExpirationDate | MTS processing for process industry with batch processing |
| Material | SG24 | SEMI24,PD,Batch-Fifo | Semifinished Product PI, batch managed |
| Material | RM15 | RAW15,PD | Packaging material, no batch, external procured |
| Material | RM09 | RAW09,PD,Batch-Fifo | Raw material, batch-managed, external procured |
| Material | RM19 | RAW19,PD,Batch-Fifo,LeanQM | Raw material, batch-managed, external procured |
| Material | RM30 | RAW30,VB,Batch-Fifo | Raw material, batch-managed, external procured |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331A | Std. storage 1 | Std. storage for finished products |
| Storage Location | 331B | Std. storage 2 | Std. storage for production Less |
| Storage Location | 331C | Raw mat. stoloc. | Raw material storage location |

Bill of Materials Structure

This overview shows the bill of materials structure and the usage of each component.

| Material | Level | Material Type | Unit | Characteristic of material |
| --- | --- | --- | --- | --- |
| FG29 | 0 | FERT | BT | MTS processing for process industry with batch processing |
| RM15 | 1 | ROH | PC | Packaging material, no batch, external procured |
| SG24 | 1 | HALB | CCM | Semifinished Product PI, batch managed |
| RM09 | 2 | ROH | KG | Raw material, batch-managed, external procured |
| RM19 | 2 | ROH | L | Raw material, batch-managed, external procured |
| RM30 | 2 | ROH | L | Raw material, batch-managed, external procured |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Table 1: Master Data Script Reference

| Master Data ID | Description |
| --- | --- |
| BNR | Create Product Master of type "Raw Material" - MDS |
| BNS | Create Product Master of type "Semi-Finished Good" - MDS |
| BNT | Create Product Master of type "Finished Good" - MDS |
| BNK | Create Material BOM for Production and Sales - MDS |
| 3X8 | Create Resource - MDS |
| 3X9 | Create Master Recipe - MDS |
| BLD | Create Production Version - MDS |

|  |
| --- |
| Note In case you want to create your own number ranges for production orders or process orders, see SAP Note [3388387](https://me.sap.com/notes/3388387). |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the steps described in the test script. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the master data script. Posting Period is up to date. |

### Preliminary Steps

#### Initial Raw Material Stock

Purpose

In a real business case, the raw materials are usually purchased from external vendors that can be covered by the standard purchasing processing. This process step shows you how to directly post initial stock to the storage location.

|  |
| --- |
| Note You can either post initial stock directly to the storage location or referring to the process of Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | Screen name adapts accordingly. |  |
| 3 | Choose Goods Receipt-Other | Make the following entries and choose Enter:Action: Goods ReceiptReference: OtherMovement Type: 561 | Screen name adapts after entries are made. |  |
| 4 | Specify Material | On the Material tab, make the following entries:Material: RM15 | Ensure that detail data is expanded. |  |
| 5 | Specify Quantity | On the Quantity tab, make the following entries:Qty in Unit of Entry: 1000 |  |  |
| 6 | Specify Plant and Storage Location | On the Where tab, make the following entries:Plant: 3310Storage location: 331B |  |  |
| 7 | Check Item | Press Enter, and ensure Item OK is selected. |  |  |
| 8 | Add Other Materials | Choose Next Item, then repeat the steps 4 to 7 for the following materials:Material: RM09Material: RM19Material: RM30 |  |  |
| 9 | Post Goods Movement | Choose Post. | Material document XXX is posted.Materials are available in stock. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Planned Independent Requirements](#unique_9) [page ] 11 | Production Planner | Maintain PIRs (F3445) | The Manage PIRs screen displays. |
| [Material Requirements Planning](#unique_10) [page ] 12 | Production Planner | Schedule MRP Runs (F1339) | The Application Jobs screen displays. |
| [Evaluate the Stock / Requirement Situation](#unique_11) [page ] 14 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | The Monitor Material Coverage screen displays. |
| [Create Process Order](#unique_12) [page ] 16 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | The Collective Conversion of Planned Orders: Initial screen displays. |
| [Review Process Order](#unique_13) [page ] 18 | Production Supervisor - Discrete Manufacturing | Display Process Order (COR3). | The Display Process Order: Initial screen displays. |
| [Goods Issue via Pick List](#unique_14) [page ] 21 | Production Operator - Process Manufacturing | Pick Components for Process Orders (COIK) | The Picking List: Initial screen displays |
| [Manual Goods Issue (Instead of Picking List)](#unique_15) [page ] 22 | Warehouse Clerk | Post Goods Movement (MIGO) | The initial screen displays. |
| [Monitor Order Progress](#unique_16) [page ] 23 | Production Supervisor - Process Manufacturing | Monitor Order Progress (CO46). | The Order Progress Report: Selection screen displays. |
| [Confirm Production incl. Component Backflush](#unique_17) [page ] 25 | Production Operator - Process Manufacturing | Confirm Process Order Phase (COR6N) | The Enter Time Ticket for Process Order screen displays. |
| [Post Goods Receipt for Process Order](#unique_18) [page ] 26 | Warehouse Clerk | Post Goods Movement (MIGO) | The Initial screen displays. |
| [Review Process Order Confirmation](#unique_19) [page ] 28 | Production Supervisor - Process Manufacturing | Display Process Order Confirmation (CORT) | The Display Process Order Confirmation: Initial screen displays. |
| [Review Scrap Report](#unique_20) [page ] 30 | Production Supervisor - Process Manufacturing | Material Scrap - Maximum Deviation (F2035) - Maximum Deviation | The Material Scrap screen displays. |
| [Review Manufacturing Object Pages](#unique_21) [page ] 31 | Any role for production listed in chapter Roles | Search function | The list of search result displays. |

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

Planned independent requirements (PIRs) are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, that is, one planned quantity split over time according to dates. This process step shows you how to create PIRs.

|  |
| --- |
| Note Instead of creating single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445) | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: FG29. |  |  |
| 5 | Filter Result | Choose Go to execute. | The material item displays. |  |
| 6 | Edit PIRs | Select the material item and choose Edit on the upper-right part of the screen.On the screen, enter quantities per period, for example:PIR: 100Make sure the version is active.Version Active: Yes |  |  |
| 7 | Save PIRs Draft | Choose Save on the bottom-right part of the screen. | The PIRs are saved. |  |

#### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The aim of material requirements planning is to tailor available capacities and receipts on time to suit requirement quantities. This process step shows you how to use MRP or consumption-based planning. Single-item multilevel requirement planning is carried out for plant 3310.

Prerequisite

The finished product for PI (FG29) is planned at plant level. There is now a requirement for the material finished product PI (FG29) in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job: Material Requirements Planning (MRP) screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirements Planning (MRP)Job Name: <MRP for FG29>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: FG29Changed BOM Components: selectPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job status, enter MRP for FG29 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate the Stock / Requirement Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor the material coverage situation for the material finished product PI (FG29) after the requirements planning has been carried out.

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | In the search area, make the following entries and choose Go.Material: FG29Material: SG24Material: RM15Material: RM09Material: RM19Material: RM30Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock / Requirements List | Choose the corresponding material in the Materials list on the left side. | The detailed Stock / Requirements List for each material displays.For RM30, no requirements are created because this material is set as bulk material. |  |
| 6 | Display Planned Order | In the Materials list, choose one of the following materials for which you want to check the planned order:Material: FG29Material: SG24On the right screen, choose the PldOrd XXXX in the MRP Element column. | The planned order displays in the dialog box.If there is no shortage for those materials, the planned order won't be generated.If you want to display more information about the planned order, choose Document Info at the bottom of this dialog box. |  |
| 7 | Display Purchase Requisition | In the Materials list on the left side, choose one of the following materials for which you want to check the purchase requisition:Material: RM15Material: RM09Material: RM19Material: RM30On the right screen, choose PurRqs XXXX in the MRP Element column. | The purchase requisition displays in the dialog box.If there is no shortage for those materials, the purchase requisition won't be generated.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. Dependent requirements for the consumption-based components are generated by production orders (planned orders and process orders) at the time of reservation. Therefore MRP runs also generated dependent requirements for the components. If inventory doesn't cover the requirements, planned orders are created for in-house-produced materials and purchase requisitions for externally procured materials. To continue processing of externally procured materials, execute Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR) test script depending on the element created in MRP run. |  |

### Process Order Processing

|  |
| --- |
| Note In this test script, the production process has to be executed at first for the semifinished material (SG24) and afterwards for the finished product (FG29). |

#### Create Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to create process orders. Because the order release is executed automatically, production can start immediately.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). |  |  |
| 3 | Check MRP Settings | Choose the user icon, select APP Settings, and then choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status button to set the status for the above entry to AOR Is Assigned if not yet assigned.Choose AOR Status button to unassign the rest of other entries.Choose Back. |  |  |
| 4 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 5 | Select Material | Make the following entries and choose Go:Shortage Definition: MRP StandardMaterial: <Material>Select the checkbox of the material, and then choose Manage Materials. | Note First convert planned orders for semi-finished material (SG24) and proceed for the whole section Process Order Processing, and afterwards repeat for the finished product (FG29). |  |
| 6 | Add Planned Order Long Text (Optional) | Click on the planned order number (PldOrd XXXX) under column MRP Element. In the quickview screen, choose Change Planned Order.On the Change Planned Order screen, choose tab Long Text, enter the text and choose Save.In the Information dialogue box, choose Exit. | The long text maintained here can be later copied to the the converted process order. |  |
| 7 | Choose Action Convert | For the planned order you want to convert, select Convert from the dropdown list under column Actions. |  |  |
| 8 | Convert to Process Order | In the dialog box, Convert to Process Order is selected by default. Choose Convert. | Planned orders are converted to process orders.Make a note of the process order numbers. |  |

As an alternative, you can also use some other app to covert the planned order to process order. If you already converted it through above procedure, you do not need to execute below procedure again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Planned Orders (F4170). Then choose the action button: Collective Conversion to Process Orders. | The Collective Conversion of Planned Orders: Initial screen displays. |  |
| 3 | Enter Restriction | Make the following entries and choose Execute:Planning Plant: 3310Production Plant: 3310Prodn.Supervisor: YB2Process Order Type: YBM2 | The system displays a list of all planned orders, which match the restriction.Note Convert first planned orders for the semifinished material (SG24) and proceed for the whole section Process Order Processing and afterwards repeat for the finished product (FG29). |  |
| 4 | Convert Planned Order to Process Order | Select the planned order for conversion, and then choose Convert Planned Order. | Planned orders are converted to process orders.Make a note of the process order numbers. |  |

|  |
| --- |
| Note It is possible to change order quantities (such as merging the quantities of two planned orders into one process order). You may then delete the obsolete planned orders from the selection list before executing order conversion. Run MRP to delete the obsolete planned orders from the database (the planned orders must not be firmed, otherwise MRP would leave them untouched).Start from CE2202, it is possible to change the default settlement rule receiver from material to cost center or WBS element for event-based production orders/process orders. For details, you can check the chapter Create/Change Settlement Rule for Non-Material Settlement in Scope Item 3F0 (Event-Based Production Cost Posting). |

#### Review Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review created process orders. It is possible to perform this step with different SAP Fiori apps. We provide 2 options you can leverage, and you can choose either one of them.

Procedure

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order (COR3). | The Display Process Order: Initial Screen displays. |  |
| 3 | Enter Process Order Number | Make the following entries and choose Enter.Process Order: XXXX (from previous steps) | The Display Process Order: Header - General Data screen displays.On this screen, you find the order’s detailed information.Process orders are reviewed and checked within your responsibility area. |  |
| 4 | Navigate to Output Management | Select Menu > Process Order > Output > Manage Output Items . | The Overview Output Management: Output screen displays. |  |
| 5 | Check Output Item | On the Overview Output Management: Output screen, you could check output item lists in the Output section.Typically, following two items should be listed with status of Completed:Output Type: PICK_LIST; Channel: PRINTOutput Type: ORDER_DATA_LIST; Channel: PRINT |  |  |
| 6 | Display PDF Document | Select the output item with Channel: PRINT and choose Display Document. | PDF document displays for the selected item. |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Process Orders (F4587). |  |  |
| 3 | Select AOR | If this is your first time to access the app, a welcome page would appear asking you to select your area of responsibility.Otherwise, choose your user name and the App Settings icon.On the Area of Responsibility screen, choose Production Supervisor.On the Area of Responsibility (Supervisor) screen, choose Production Supervisor.Choose Add or Delete to add or remove entries, and make sure following entry displays:Plant 1 AE/ MTS PI valuated (YB2) |  |  |
| 4 | Choose the Process Order | In the process order list, find your process order and choose it.Process Order: XXXX (from previous steps) | Note In the header area, you can switch between Compact Filter and Visual Filter, to find a proper way to search for your process order number. |  |
| 5 | Review Process Order | In the detailed page of the process order, review relevant information. |  |  |
| 6 | Check Long Text Copied from Planned Order (Optional) | If any long text is maintained for the planned order, you can check it in the converted process order.In the Process Orders section, select an order and choose Edit Order in the upper right corner.On the Change Process Order: Header screen, choose icon Change Long Text next to Process Order number, and check the text. | The long text maintained in the planned order is copied to the converted process order. |  |

#### Goods Issue of Batch-Managed Components

Purpose

The withdrawal of the raw materials is used for the process order. This withdrawal can be done by using the picking list or doing a manual goods issue.

|  |
| --- |
| Note If the material is set for backflush (in material master or resource), the withdrawing is done automatically after you confirm the operation or the whole order. Backflushing should not be used for batch-managed components (to ensure that the physically picked and consumed batch is the same as the recorded batch). |

Prerequisites

Ensure that sufficient material is present on stock. You can check the stock levels using the app Monitor Stock / Requirements List - Old Version (MD04) available for the Production Planner role.

##### Goods Issue via Pick List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The released process order is now ready for picking. This process step shows you how to issue all materials that are moved to the production storage location to the process order using the pick list.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Process Orders (COIK). | The Picking List: Initial screen displays. |  |
| 3 | Enter Restriction and Execute | Make the following entries and then choose Execute:Profile: 000002Process Order: XXXX (from previous steps)Plant: 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Select the relevant reservations and choose Picking. | The Picking list screen displays. On this screen, a list of all the selected reservations displays. |  |
| 5 | Perform Batch Determination | Select the picking lines and choose Batch Determination. | The Batch Determination MM: Select Batches screen displays.If the system shows the message Batch determination was carried out without selection specification , ignore it.If only part of the required quantity is found to be available during batch determination, the unconfirmed quantity remains as an open line item within the picking list. You should then delete the line item from the picking list before saving, as this line item can't be posted. |  |
| 6 | Copy Batch Determination Result | Choose Copy. Repeat this step for all the materials you selected. | The Picking list screen displays again. In addition, the batch numbers have been determined. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements are posted. |  |

##### Manual Goods Issue (Instead of Picking List)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to perform a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then press Enter:Trans./Event: Goods IssueReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Check Each Item | For each item displays, select Item OK. | Note Ensure that detail data is expanded. |  |
| 5 | Perform Batch Determination | Choose Stock Determ. for All. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Copy Batch Determination Result | Check the required batch and choose Copy. Repeat this step for all the materials you selected. | The Goods Issue Order XXXX screen displays. In addition, the batch numbers have been determined. |  |
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

This process step shows you how to monitor process orders. It is possible to perform this step with different SAP Fiori apps. We provide 2 options you can leverage, and you can choose either one of them.

Procedure

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Process Orders (F4587). |  |  |
| 3 | Select AOR | If this is your first time to access the app, a welcome page will be displayed asking you to select your area of responsibility.Otherwise, choose the user icon and select App Settings.Choose tab Production Supervisors.In the AOR Status column, choose the button to assign or unassign entries, and make sure only the following entries are assigned:Plant 1 AE/ MTS PI valuated (YB2)Choose Back. |  |  |
| 4 | Choose the Process Order | In the process order list, find your process order and choose it.Process Order: XXXX (from previous steps) | Note In the header area, you can switch between Compact Filter and Visual Filter, to find a proper way to search for your process order number. |  |
| 5 | Review Process Order | In the detailed page of the process order, review relevant information. |  |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Order Progress (CO46). | The Order Progress Report: Selection screen displayed. |  |
| 3 | Enter Overall Profile | Make the following entries and choose the Production/Process Order tabOverall Profile: SAP000000002 |  |  |
| 4 | Enter Process Order Number | Make the following entries and choose Execute.Production/Process Order: XXXX (from previous steps) | The Stock/Requirements List as of XX hrs screen displays.You can review the required lists, such as order header and components list. |  |

#### Confirm Production incl. Component Backflush

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of order, operations, phases and individual capacities. It is an instrument to control the order. The time ticket confirmation allows recording either the default times for machine and labour usage, or actual times for major deviations. Backflushed materials will be posted automatically during respective phase confirmations. This process step shows you how to confirm production. You can post scrap quantities as an optional. If no major deviations occurred, only the last phase (milestone) must be confirmed. Using milestone confirmation, all prior phases are confirmed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Process Order Phase (COR6N). | The Enter Time Ticket for Process Order screen displays. |  |
| 3 | Enter Confirmation Option | Make the following entries and then choose Enter.Order: XXXX (from previous steps)Choose Enter or select phase (0040 for SG24 / 0020 for FG29) from search help of Phase field.Confirm.type: Final confirmationClear open reservations: X | Note If the system shows the message Total quantity confirmed not equal to planned quantity to be confirmed, press Enter to ignore it. |  |
| 4 | Propose Actual Data | Choose Actual Data.Make the changes for the following fields:Scrap: <enter the amount you want to scrap>Yield: <Based on the origin quantities minus scrap>Reason for Var: < Enter scrap reason if needed>, for example, 0001 | The Quantities and Activities will be filed automatically.If you want to check your backflushed components (required for material FG29), continue with step 5 of this table. Else proceed directly with step 6. |  |
| 5 | Check Backflushed Components (optional step and only required for FG29 process orders) | Choose Goods Movements.After the check, choose Back to go to the the Enter Time Ticket for Process Order screen and continue with the next step. | The Enter Confirmation for Production Order: Goods Movement screen displays. Check the material entries and quantities. |  |
| 6 | Save Confirmation | Click Post. | The final confirmation of the last operation is carried out. Costs and activity quantities are recalculated in proportion to the yield quantity.Backflushed components are issued with the confirmation posting automatically (packaging material RM15 within the confirmation of orders for Finished Product PI FG29). |  |

#### Post Goods Receipt for Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The purpose of this activity is to post the goods receipt for the process order. You may post goods receipt for the total quantity, but usually already partial quantities of the products are required for further processing, such as consumption for further production or subsequent deliveries for sales orders.

It is possible to perform this step with different SAP Fiori apps. We provide 2 options you can leverage, and you can choose either one of them.

|  |
| --- |
| Note If you enabled scope item Handling Unit Management (4MM), you can create handling units at the end of production and post goods receipts for handling units. By this way, the stock can be posted directly into storage and is available for picking. For details, refer to scope item 4MM. |

Procedure

Option 1

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Receipt for Process Order (F6352). |  |  |
| 3 | Enter Process Order | Make the following entry and then press Enter.Process Order: XXXX (from previous steps) | The details of the order is listed. |  |
| 4 | Enter Date of Manufacture for FG29 | Note This step is only needed for Material FG29.Find the Order item and choose it.In the Production and Shelf Life Expiration Date section, make the following entry and choose Apply:Production Date: Current Date |  |  |
| 5 | Post Goods Movement | Ensure the item is selected and choose Post. | The goods movements are posted. The batch number is created automatically during the posting. Production date and shelf life expiration date are recorded within the batch master of the finished product. |  |

Option 2

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log on | Log on to the SAP Fiori Launchpad as Warehouse Clerk. | The SAP Fiori Launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then press Enter:Trans./Event: Goods ReceiptReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 101 | Screen name adapts after entries are made. |  |
| 4 | Enter Date of Manufacture | Choose the Batch tab, and make the following entries:Date of Manufacture: Current DateNote It is only needed for Material FG29. For Material SG24 the date can be entered but is not mandatory. | Note Please be informed that instruction of step 4 is only available for SAP delivered standard content as some customizing changes in SSCUI could make things different.Note Depending on your configuration environment, configuration steps can be accessed under Configure Your Solution in the SAP Fiori launchpad or in the Business Processes Configuration app in the project experience of SAP Central Business Configuration. |  |
| 5 | Check Item | Select item OK. | Ensure that detail data is expanded. |  |
| 6 | Post Goods Movement | Choose Post. | The goods movements are posted. The batch number is created automatically during the posting. Production date and shelf life expiration date are recorded within the batch master of the finished product. |  |

#### Review Process Order Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review confirmations for process orders. It is possible to perform this step with different SAP Fiori apps. We provide several options, and you can choose one of them.

Procedure

Option 1:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Manage Process Orders (F4587). |  |  |
| 3 | Select AOR | If this is your first time to access the app, a welcome page would appear asking you to select your area of responsibility.Otherwise, choose your user name and the App Settings icon.On the Area of Responsibility screen, choose Production Supervisor.On the Area of Responsibility (Supervisor) screen, choose Production Supervisor.Choose Add or Delete to add or remove entries, and make sure following entry displays:Plant 1 AE/ MTS PI valuated (YB2) |  |  |
| 4 | Choose the Process Order | In the process order list, find your process order and choose it.Process Order: XXXX (from previous steps) | In the header area, you can switch between Compact Filter and Visual Filter, to find a proper way to search for your process order number. |  |
| 5 | Review Process Order | In the detailed page of the process order, review conformations of the process order. |  |  |

Option 2:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order Confirmation (CORT). | The Display Process Order Confirmation: Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then choose Enter.Process Order: XXXX (from previous steps) | The Display Process Order Confirmation: Operation/Phase Overview screen displays.Confirmations are reviewed and checked within your responsibility area. |  |

Option 3:

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Process Order Operations (F5323). |  |  |
| 3 | Choose Filter Style | In the header part, you can switch between Compact Filter and Visual Filter, which provides you different styles for filter. |  |  |
| 4 | Enter Process Order Number | Choose Compact Filter, make the following entries and choose Go.Process Order: XXXX (from previous steps) | Operation list displays. |  |

#### Review Scrap Report

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the scrap report.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Discrete Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Material Scrap - Maximum Deviation (F2035). | The Material Scrap screen displays. |  |
| 3 | Investigate Scrap | Materials Scrap can be displayed by various filters.You could choose the corresponding material in Chart to display the details. |  |  |

### Review Manufacturing Object Pages

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review different object pages available for different roles in the manufacturing process.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner.Note You can use any role in section Roles above. | The SAP Fiori launchpad displays. |  |
| 2 | Search Material | Choose the Search icon in the upper right part of the screen.Make the following entries and choose Search:Search: <BOM Header Material>, refer to section Master Data, Organizational Data, and Other Data. | The system displays a list of objects using the selected material. |  |
| 3 | Display Object | In the All field, select an object from the dropdown list and choose the Search icon. | The displaying list of objects is limited to the object type selected. If no object is selected, a message would display instead. |  |
| 4 | Tailor the Result Display | Under the search line, choose an icon (for example, filter, display as table, sort and so on) to filter the results list. | The results list is filtered according to your selections. |  |
| 5 | Repeat Steps | Repeat steps 1 to 5 for any other role in this test script and any other object offered in the search function. | The result list of objects displayed differs by the role you use to log on. |  |

## Appendix

### Succeeding Processes

After completing the activities in this test script, you can continue testing the following business processes:

| Process | Business Condition |
| --- | --- |
| Decoupling Processes Carried out During Confirmation (Optional) | When you carry out a confirmation, processes are triggered that could negatively affect the response time of the confirmation process. For example, goods movements and actual costs determination.You alleviate this situation by decoupling these processes from the actual confirmation.Depending on your configuration environment for SAP S/4HANA Cloud Public Edition, choose one of the following options:Manage Your Solution:Log on to the SAP Fiori Launchpad in the SAP S/4HANA Cloud Public Edition system as a Configuration Expert - Business Process Configuration.Navigate to the Manage Your Solution (F1241) app and choose Configure Your Solution.On the Configure Your Solution screen, search for the following configuration step: Define Time for Confirmation Processes and Define Confirmation Parameters.In the search result, choose the configuration activity and go to the next screen.Choose Configure of the corresponding step in the Configuration Steps area.SAP Central Business Configuration:Log on to the project experience in SAP Central Business Configuration.Go to the Business Processes Configuration app. To locate the activity in the tree view, search for the following activity: Define Confirmation Parameters.Choose Open Documentation for the found line item to see more details about this configuration activity.Choose the link to navigate directly to the SAP S/4HANA Cloud Public Edition system. Log on to the SAP Fiori launchpad as a Configuration Expert - Business Process Configuration.To post these confirmation processes, you can access Schedule Posting of Predefined Confirmation Processes (F5255) app as a Production Supervisor - Process Manufacturing. You use the app to define which processes are to be executed in the job. As a general guide:Automatic goods receipts should be processed soon after the actual confirmation. This applies to materials that are processed further or that are needed in Sales, for which it is particularly important that stock levels are kept up-to-date. Processing should be online or executed as an update task.Backflushing withdrawals can be processed in longer periods (for example twice a day). Since the material has already been withdrawn physically from the storage location, stock levels are not as important. However, other consumers of the material and material requirements planning should be notified.Actual costs determination can take place less frequently (for example once a day). Actual costs determination is not important for smooth production processing. It is needed for controlling and should be adapted to the demands of this department. |
| 3F0 (Event-Based Production Cost Posting) | This procedure updates work-in-process calculation, overhead calculation, and variance calculation by linking the posting to the events.Note Start from CE2105, the default Best Practice content is based on event-based result analysis for new customer install and add new country only, rather than previous period-end posting. For existing customers (who activated content before 2105), the default remain unchanged to Period-End Closing – Plant BEI till customer makes the decision to switch. For migration to Event based from Periodic please refer [Production Settlement in Parallel Ledgers](https://help.sap.com/viewer/4032610758dc437089f0c28320eec93f/LATEST/en-US/e49a3770f22547a392455154f3eef6e2.html). If you are still using period-end posting, you may need to refer to non-standard Scope Item BEI - Period-End Closing – Plant. |

### Process Order Creation with Approved Master Recipe (Optional)

This is a separate process to show how to create process order requiring an approved master recipe. It is independent from the main test procedures described in this test script.

#### Preceding Procedure: Product Change Management with Change Records - Process Industries (5QC)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The approval procedure for Master Recipe is described in engineering change management scope item 5QC (Product Change Management with Change Records – Process Industries). If you use Master Recipe which requires approval, you therefore need to first execute the whole test procedures in scope item 5QC. For integration with manufacturing process, you can execute scope item 5QC with below pre-delivered sample master data:

| Master Data | Value | Details |
| --- | --- | --- |
| Material | SG24 | SEMI24,PD,Batch-Fifo |
| Plant | 3310 | Company Code 3310 |
| Recipe Group | 41010007 |  |
| Recipe | 2 |  |

Result

The Master Recipe has now been approved. It can be used to create process orders requiring an approved Master Recipe.

#### Create Process Order with Approved Master Recipe

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Create Process Order (COR1). |  |  |
| 3 | Select | Make the following entries and choose Continue:Material Number: SG24Production Plant: 3310Process Order Type: YQ03Note In pre-delivered customizing "Order Type-Dependent Parameters", the Approval Required indicator is set for the dedicated order type. |  |  |
| 4 | Enter required entry | Make the following entries:Total Qty: <for example, 100>Basic Dates - Start: <for example, next working day> |  |  |
| 5 | Select Production Version | Choose Production Version button. In the pop-up window, make the following selection and select Choose:Production Version: 0002Note In pre-delivered demo data, the Master Recipe requiring approval is assigned in this production version. | You get a message saying that release carried out. |  |
| 6 | Save | Choose Save. | Process Order is created based on approved recipe. |  |

Result

The process order is created and released, with system status APG (Approval granted) and APRC (Based on approved recipe). You can continue with any subsequent manufacturing process.

### Additional Functional Information

If you want to know functional information for Discrete and Process Manufacturing beyond what is described in the test scripts of the best practice scope items for SAP S/4HANA Cloud Public Edition, you could check SAP Note [3441318](https://me.sap.com/notes/3441318).

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
- related-to :: [[12-production-and-manufacturing/make-to-stock-with-silo-material-process-manufacturing-3ul-ae-test-scr]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-stock-process-manufacturing-based-on-production-or]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-stock-with-co-and-by-products-process-manufacturin]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/BJ8_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 61,512 chars in the whole document
