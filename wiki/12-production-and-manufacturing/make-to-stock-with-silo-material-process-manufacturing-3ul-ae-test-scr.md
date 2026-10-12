---
id: 12-production-and-manufacturing/make-to-stock-with-silo-material-process-manufacturing-3ul-ae-test-scr
title: Make-to-Stock with Silo Material – Process Manufacturing (3UL_AE) – Test Script (3UL_S4CLD2608_BPD_EN_AE)
description: "SAP S/4HANA Cloud Public Edition test script for scope item 3UL_AE: PIRs, MRP, process orders, goods issue, backflush confirmation, goods receipt (silo)."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/make-to-stock-process-manufacturing]
aliases: [3UL_S4CLD2608_BPD_EN_AE]
keywords: [Make-to-Stock Process Manufacturing, scope item testing, process manufacturing, silo materials, planned independent requirements, material requirements planning, process order processing, goods issue, production confirmation, goods receipt]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3UL_S4CLD2608_BPD_EN_AE.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-972
topic: 12-production-and-manufacturing/make-to-stock-process-manufacturing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Make-to-Stock with Silo Material – Process Manufacturing (3UL_AE) – Test Script (3UL_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3UL_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Make-to-Stock Process Manufacturing** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| Make-to-Stock with Silo Material – Process Manufacturing (3UL_AE)Purpose PUBLIC 1<!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
|  | Make-to-Stock with Silo Material – Process Manufacturing (3UL_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853731)

[2 Prerequisites 4](#_Toc232853732)

[2.1 System Access 4](#_Toc232853733)

[2.2 Roles 4](#_Toc232853734)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232853735)

[2.4 Business Conditions 7](#_Toc232853736)

[2.5 Preliminary Steps 7](#_Toc232853737)

[2.5.1 Initial Raw Material Stock 7](#_Toc232853738)

[3 Overview Table 10](#_Toc232853739)

[4 Test Procedures 12](#_Toc232853740)

[4.1 Anonymous Forecast and MRP 12](#_Toc232853741)

[4.1.1 Create Planned Independent Requirements 12](#_Toc232853742)

[4.1.2 Material Requirements Planning 13](#_Toc232853743)

[4.1.3 Evaluate the Stock / Requirement Situation 15](#_Toc232853744)

[4.2 Process Order Processing 16](#_Toc232853745)

[4.2.1 Create Process Order 16](#_Toc232853746)

[4.2.2 Review Process Order 18](#_Toc232853747)

[4.2.3 Goods Issue of Batch-Managed Components 19](#_Toc232853748)

[4.2.3.1 Goods Issue via Pick List 19](#_Toc232853749)

[4.2.3.2 Manual Goods Issue (instead of Picking List) 21](#_Toc232853750)

[4.2.4 Confirm Production incl. Component Backflush 22](#_Toc232853751)

[4.2.5 Post Goods Receipt for Process Order 23](#_Toc232853752)

[4.2.6 Review Process Order Confirmation 24](#_Toc232853753)

[4.2.7 Review Scrap Report (Optional) 25](#_Toc232853754)

[5 Appendix 26](#_Toc232853755)

[5.1 Succeeding Processes 26](#_Toc232853756)

## Purpose

Overview

This scope item focuses on process manufacturing with more complex parameters compared to the Make-to-Stock – Process Manufacturing Based on Process Order (BJ8) scope item. It enables production planning in make-to-stock scenarios with silo materials and phantom assemblies. Silo materials are generally stored in big silos or tanks. The silos are modeled as separate storage locations.

The process starts with the creation of a demand forecast for finished goods represented by Planned Independent Requirements (PIRs). Based on PIRs, Material Requirements Planning (MRP) creates a production plan for finished goods, semi-finished components, and raw materials.

The production process itself is entirely covered via conversion of planned into process orders, direct material issue or backflush, confirmation of operations and goods receipt posting. Order-based target and actual costs are created, ensuring fully integrated material and value streams.

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

Manufacturing

| Master | Value | Details | Comments |
| --- | --- | --- | --- |
| Material | FG29-1 | FIN29-1, MTS-PI, with Silo MaterialFinished product |  |
| Material | SG1010 | SEMI1010, PD, Silo material with batchSilo material |  |
| Material | SG22 | SEMI22,PD,PhantomPhantom material |  |
| Material | SG2200 | SEMI2200, MTS-PI, PD, with Co- & By-Product |  |
| Material | RM15 | RAW15,PDBackflush material |  |
| Material | RM16 | RAW16,PD |  |
| Material | RM1420 | RM1420, PD, Solvent |  |
| Material | RM1430 | RM1430, PD, Catalyst |  |
| Material | PIP01 | Pipeline Material 01 |  |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage 2Std. storage for production |  |
| Storage Location | 331C | Raw mat. stoloc.Raw material storage location |  |

Bill of Materials Structure

This overview shows the bill of materials structure and the usage of each component.

| Material | Level | Material Type | Unit | Material description | Optional Enhancements |
| --- | --- | --- | --- | --- | --- |
| FG29-1 | 0 | FERT | KG | FIN29-1, MTS-PI, with Silo Material |  |
| SG1010 | 1 | SEMI | L | SEMI1010, PD, Silo material with batch | Inbound Storage Tank Management – Process Manufacturing (3UK) |
| SG22 | 1 | SEMI | PC | SEMI22,PD,Phantom |  |
| RM16 | 2 | RAW | PC | RAW16,PD |  |
| RM1420 | 1 | RAW | L | RM1420, PD, Solvent |  |
| RM15 | 1 | RAW | PC | RAW15,PD |  |
| SG2200 | 1 | SEMI | KG | SEMI2200, MTS-PI, PD, with Co- & By-Product | Make-to-Stock with Co- and By-Products – Process Manufacturing (3L7) |
| RM1420 | 2 | RAW | L | RM1420, PD, Solvent |  |
| RM1430 | 2 | RAW | L | RM1430, PD, Catalyst |  |
| PIP01 | 1 | PIPE | L | Pipeline Material 01 | Run the step in Procurement of Pipeline Materials(41F): Create Purchasing Info Record first, then consume this material |

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
| 2ZW | Create Batch Management Master Data - MDS |

### Business Conditions

Before this scope item can be tested, the following business conditions must be met.

| Scope Item | Business Condition |
| --- | --- |
| BEG - Standard Cost Calculation | You have completed the step described in the BEG test scrip. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the BNZ test script. Posting Period is up to date. |
| 41F - Procurement of Pipeline Materials | If there is any pipeline material contained in the BOM, you need to refer to 41F test script to handle pipeline component and complete following step:Create Purchasing Info Record: run this step first before consuming pipeline materialNote In 3UL, we post goods issue to process order with movement type 261/P instead of 201/P as described in Record Consumption of 41F. |

### Preliminary Steps

#### Initial Raw Material Stock

Purpose

This process step shows you how to post initial stock directly to the storage location for following materials:

| Sample Value | Description | Comments |
| --- | --- | --- |
| SG1010 | Silo material | You can either directly post initial stock or produce it referring to the process of Inbound Storage Tank Management – Process Manufacturing (3UK). |
| SG2200 | With Co- & By-Product | You can either directly post initial stock or produce it referring to the process of Make-to-Stock with Co- and By-Products – Process Manufacturing (3L7). |
| RM15 | Raw material |  |
| RM1420 | Raw material |  |
| RM16 | Components for Phantom material SG22 |  |

|  |
| --- |
| Note In a real business scenario, the raw materials are usually purchased from external vendors that can be covered by the standard purchasing process. You can either directly post initial stock to the storage location or refer to the process of Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR). For pipeline component PIP01, it flows directly into the production process through pipes or other similar sources. It is not relevant for stock, thus you do not need to make initial stock here. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | Screen name adapts according to entries. |  |
| 3 | Choose Goods Receipt-Other | Make the following entries and press Enter:Trans./Event: Goods ReceiptReference Document: OtherMovement Type: 561 | Screen name adapts according to entries. |  |
| 4 | Specify Material | On the Material tab, make the following entry:Material: <Material Number> |  |  |
| 5 | Specify Quantity | On the Quantity tab, make the following entry:Qty in Unit of Entry: 1000 |  |  |
| 6 | Specify Plant and Storage Location | On the Where tab, make the following entries:Plant: 3310Storage location:331B |  |  |
| 7 | Check Item | Press Enter, and ensure Item OK is selected. |  |  |
| 8 | Post Goods Movement | Choose Post. | Material document XXX is posted.Materials are available in stock. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| Anonymous Forecast and MRP |  |  |  |
| [Create Planned Independent Requirements](#unique_9) [page ] 12 | Production Planner | Maintain PIRs (F3445) | Independent Requirements for finished product are created. |
| [Material Requirements Planning](#unique_10) [page ] 13 | Production Planner | Schedule MRP Runs (F1339) | Independent Requirements for finished product are planned. |
| [Evaluate the Stock / Requirement Situation](#unique_11) [page ] 15 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned material are analyzed. |
| Process Order Processing |  |  |  |
| [Create Process Order](#unique_12) [page ] 16 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Planned Orders for finished product are converted to Process Orders. |
| [Review Process Order](#unique_13) [page ] 18 | Production Supervisor - Process Manufacturing | Display Process Order (COR3) | The Process Order is reviewed. |
| [Goods Issue of Batch-Managed Components](#unique_14) [page ] 19 |  |  |  |
| [Goods Issue via Pick List](#unique_15) [page ] 19 | Production Operator - Process Manufacturing | Pick Components for Process Orders (COIK) | Components under Picking List are posted. |
| [Manual Goods Issue (instead of Picking List)](#unique_16) [page ] 21 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods movements are posted. |
| [Confirm Production incl. Component Backflush](#unique_17) [page ] 22 | Production Operator - Process Manufacturing | Confirm Process Order Phase (COR6N) | Confirmation of the process order is carried out. |
| [Post Goods Receipt for Process Order](#unique_18) [page ] 23 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt for the process order is posted. |
| [Review Process Order Confirmation](#unique_19) [page ] 24 | Production Supervisor - Process Manufacturing | Display Process Order Confirmation (CORT) |  |
| [Review Scrap Report (Optional)](#unique_20) [page ] 25 | Production Supervisor - Process Manufacturing | Material Scrap - Maximum Deviation (F2035) |  |

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
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Month (M)Version Active: Select all optionsSearch: FG29-1 |  |  |
| 5 | Filter Result | Choose Go to execute. | Material item displays. |  |
| 6 | Edit PIRs | Select the material item, and choose Edit on the upper-right part of the screen.On the screen, enter quantities per period, for example:PIR: 100Make sure the version is active.Version Active: Yes |  |  |
| 7 | Save PIRs Draft | Choose Save on the bottom-right of the screen. | The PIRs are saved. |  |

#### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The aim of material requirements planning is to tailor available capacities and receipts on time to suit requirement quantities. This process step shows you how to use MRP or consumption-based planning for this purpose. Single-item multilevel requirement planning is carried out for plant 3310.

Prerequisite

The finished product is planned at plant level. There is now a requirement for it in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for FG29-1>Choose Step 2.For 2. Scheduling Options section:Start Immediately: <select>Choose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: <select>Recurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: FG29-1Changed BOM Components: <select>Planning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for FG29-1 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate the Stock / Requirement Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor the material coverage situation for the material after the requirements planning has been carried out.

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net and Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | On the Monitor Material Coverage - Net and Individual Segments screen, choose the user icon and select APP Settings. In the MRP Settings dialog box, choose Area of Responsibility.Ensure only the following entry is assigned:Plant 1 AE / 001 (MRP Controller 001)Choose Back.In the search area, make the following entries and choose Go.Material: FG29-1Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays. |  |
| 5 | Review Stock / Requirements List | Select the corresponding material in the Materials list. | The detailed Stock / Requirements List for each material displays. |  |
| 6 | Display Planned Order | In the left Materials list, choose the following material for which you want to check the planned order:Material: FG29-1On the right screen, choose PldOrd XXXX in the MRP Element column and check the generated planned order.Note The BOM explosion during the MRP run has generated dependent requirements for the demand-driven planned components. If inventory doesn't cover the requirements, planned orders are created for in-house-produced materials and purchase requisitions for externally procured materials. | The planned order selected displays in the dialog box. Make a note of the number of this planned order.If there is no shortage for those materials, the planned order won't be generated.If you want to display more information about the planned order, choose Document Info at the bottom of this dialog box. |  |

### Process Order Processing

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
| 3 | Check MRP Settings | Choose the user icon, select APP Settings, and then choose Area of Responsibility.On the My Area of Responsibility screen, check if only following entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR status button of this entry if not assigned, choose AOR status button of the corresponding entry to unassign any other entry and then choose Back. |  |  |
| 4 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 5 | Select Material | Make the following entries and choose Go:Shortage Definition: MRP StandardMaterial: FG29-1Select the checkbox of the material, and then choose Manage Materials. |  |  |
| 6 | Choose Action Convert | Choose the corresponding material item. For the planned order you want to convert, select Convert from the dropdown list under column Actions. |  |  |
| 7 | Convert to Process Order | In the dialog box, Convert to Process Order is selected by default. Choose Convert. | Planned orders are converted to process orders.Make a note of the process order numbers. |  |

As an alternative, you can also use some other app to covert the planned order to process order. If you already converted it through above procedure, you do not need to execute below procedure again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Manage Planned Orders (F4170). Then choose the action button: Collective Conversion to Process Orders. | The Collective Conversion of Planned Orders: Initial screen displays. |  |
| 3 | Enter Restriction | Make the following entries and choose Execute:Production Plant: 3310Material: FG29-1 | The system displays a list of all planned orders, which match the restriction. |  |
| 4 | Convert Planned Order to Process Order | Select the planned order for conversion, and then choose Convert Planned Order. | Planned orders were converted to process orders. |  |
|  | Note It is possible to change order quantities (such as merging the quantities of two planned orders into one process order. You may then delete the obsolete planned orders from the selection list before executing order conversion. Run MRP to delete the obsolete planned orders from the database (the planned orders must not be firmed, otherwise MRP would leave them untouched). |  |  |  |

#### Review Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review created process orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order (COR3). | The Display Process Order: Initial screen displays. |  |
| 3 | Enter Process Order Number | Make the following entries and choose Enter.Process Order: XXXX (From previous steps) | The Display Process Order: Header - General Data screen displays.On this screen, you find the order’s detailed information.Process orders are reviewed and checked within your responsibility area. |  |

#### Goods Issue of Batch-Managed Components

Purpose

The withdrawal of the raw materials is used for the process order. This withdrawal can be done by using the picking list or doing a manual goods issue.

Prerequisites

Ensure that sufficient material is present on stock. You can check the stock levels using the Monitor Stock / Requirements List - Old Version (MD04) app available for the Production Planner role.

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Process Orders (COIK). | The Picking List: Initial screen displays. |  |
| 3 | Enter Restriction and Execute | Make the following entries and then choose Execute.Profile: 000002Process Order: XXXX (from previous steps)Plant: 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Select the relevant reservations and choose Picking. | The Picking list screen displays. On this screen, a list of all the selected reservations displays. |  |
| 5 | Perform Batch Determination | Some materials are managed by batch, for example: RM1420, SG1010 and SG2200.Select the picking lines and choose Batch Determination. | The Batch Determination MM: Select Batches screen displays.If the system shows the message Batch determination was carried out without selection specification, ignore it.If only part of the required quantity is found to be available during batch determination, the unconfirmed quantity remains as an open line item within the picking list. You should then delete the line item from the picking list before saving, as this line item can't be posted. |  |
| 6 | Copy Batch Determination Result | Choose Copy. | The Picking list screen displays again. In addition, the batch numbers have been determined. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements are posted. |  |

##### Manual Goods Issue (instead of Picking List)

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
| 3 | Enter Process Order | Make the following entries and then choose Enter.Trans./Event: Goods IssueReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 261 | The screen name adapts accordingly. |  |
| 4 | Check Each Item | For each item displays, select Item OK. | Ensure that detail data is expanded. |  |
| 5 | Perform Batch Determination | For batch-managed material, choose Stock Determ. for All. | The Batch Determination MM: Select Batches screen displays. |  |
| 6 | Copy Batch Determination Result | Check the required batch and choose Copy. Repeat this step for all the materials you selected. | The Goods Issue Order XXXX screen displays. In addition, the batch numbers have been determined. |  |
| 7 | Post Goods Movements | Choose Post. | The goods movements have been posted. |  |

#### Confirm Production incl. Component Backflush

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents contain the processing status of order, operations, phases and individual capacities. It is an instrument to control the order. The time ticket confirmation allows recording either the default times for machine and labour usage, or actual times for major deviations. Backflushed materials will be posted automatically during respective phase confirmations. This process step shows you how to confirm production. We can post scrap quantities as an optional. If no major deviations occurred, only the last phase (milestone) must be confirmed. Using milestone confirmation, all prior phases are confirmed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Process Order Phase (COR6N). | The Enter Time Ticket for Process Order screen displays. |  |
| 3 | Enter Confirmation Option | Make the following entries and then choose Enter.Order: XXXX (from previous steps)Choose Enter or select phase (0040) from search help of Phase fieldConfirm.type: Final confirmationClear open reservations: X | If the system displays the message Total quantity confirmed not equal to planned quantity to be confirmed, press Enter to ignore it. |  |
| 4 | Propose Actual Data | Choose Actual Data.Make the changes for the following fields:Scrap: <enter the amount you want to Scrap>Yield: <Based on the origin quantities minus Scrap>Reason for Var: Enter scarp reason if need>, for example, 0001 | The Quantities and Activities will be filled automatically. You can make necessary change. |  |
| 5 | Choose Goods Movements | Choose Goods Movements and check. | The system displays an overview table of all materials for which the withdrawing is done automatically with the confirmation of the operation.The material RM15 is set for backflush (in material master) so that the withdrawing is done automatically after you confirm the operation. |  |
| 6 | Save Confirmation | Choose Post to save. | Backflushed component is issued with the confirmation posting automatically. The final confirmation of the last operation is carried out. |  |

#### Post Goods Receipt for Process Order

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to post the goods receipt for the process order.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as aWarehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then choose Enter.Trans./Event: Goods ReceiptReference Document: OrderOrder number: XXXX (From previous steps)Movement Type: 101 | Screen name adapts accordingly. |  |
| 4 | Check Product | Check the products listed in the table. |  |  |
| 5 | Check Item | Select Item OK for each line. | Ensure that detail data is expanded. |  |
| 6 | Check | Choose Check in the lower right corner. | The batch number is created automatically. |  |
| 7 | Post Goods Movement | Choose Post. | The goods movements for main product and co-product are posted. |  |

#### Review Process Order Confirmation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review confirmations for process orders.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Display Process Order Confirmation (CORT). | The Display Process Order Confirmation: Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then choose Enter.Process Order: XXXX (from previous steps) | The Display Process Order Confirmation: Operation/Phase Overview screen displays.Confirmations are reviewed and checked within your responsibility area. |  |

#### Review Scrap Report (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the scrap report if there is some scrap posted during confirmation.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Material Scrap - Maximum Deviation (F2035). |  |  |
| 3 | Investigate Scrap | Materials Scrap can display by various filters.You could choose the corresponding material in Chart to display the details. |  |  |

## Appendix

### Succeeding Processes

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
- related-to :: [[12-production-and-manufacturing/test-script-make-to-stock-process-manufacturing-based-on-production-or]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-stock-with-co-and-by-products-process-manufacturin]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3UL_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 41,751 chars in the whole document
