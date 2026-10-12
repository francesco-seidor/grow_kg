---
id: 12-production-and-manufacturing/test-script-make-to-stock-with-co-and-by-products-process-manufacturin
title: "Test Script: Make-to-Stock with Co- and By-Products – Process Manufacturing (3L7_AE) (3L7_S4CLD2608_BPD_EN_AE)"
description: "SAP S/4HANA Cloud test script for scope item 3L7 (AE): make-to-stock process manufacturing with co- and by-products, from PIRs and MRP to goods receipt."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/make-to-stock-process-manufacturing]
aliases: [3L7_S4CLD2608_BPD_EN_AE]
keywords: [Make-to-Stock Process Manufacturing, process manufacturing, co-products and by-products, process orders, planned independent requirements, material requirements planning, goods issue, goods receipt, production confirmation, stock requirements analysis]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L7_S4CLD2608_BPD_EN_AE.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-954
topic: 12-production-and-manufacturing/make-to-stock-process-manufacturing
language: EN
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Test Script: Make-to-Stock with Co- and By-Products – Process Manufacturing (3L7_AE) (3L7_S4CLD2608_BPD_EN_AE)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L7_S4CLD2608_BPD_EN_AE.docx`, extracted with `mammoth`. Grouped under **Make-to-Stock Process Manufacturing** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

| <!-- image omitted: unnamed --> | Test ScriptSAP S/4HANA Cloud Public Edition - 19-06-26 |
| --- | --- |
|  | Make-to-Stock with Co- and By-Products – Process Manufacturing (3L7_AE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Table of Contents

[1 Purpose 3](#_Toc232853154)

[2 Prerequisites 4](#_Toc232853155)

[2.1 System Access 4](#_Toc232853156)

[2.2 Roles 4](#_Toc232853157)

[2.3 Master Data, Organizational Data, and Other Data 4](#_Toc232853158)

[2.4 Business Conditions 7](#_Toc232853159)

[2.5 Preliminary Steps 7](#_Toc232853160)

[2.5.1 Initial Raw Material Stock 7](#_Toc232853161)

[3 Overview Table 9](#_Toc232853162)

[4 Test Procedures 11](#_Toc232853163)

[4.1 Anonymous Forecast and MRP 11](#_Toc232853164)

[4.1.1 Create Planned Independent Requirements 11](#_Toc232853165)

[4.1.2 Material Requirements Planning 12](#_Toc232853166)

[4.1.3 Evaluate the Stock / Requirement Situation 14](#_Toc232853167)

[4.2 Process Order Processing 15](#_Toc232853168)

[4.2.1 Create Process Order 15](#_Toc232853169)

[4.2.2 Review Process Order 17](#_Toc232853170)

[4.2.3 Goods Issue of Batch-Managed Components 18](#_Toc232853171)

[4.2.3.1 Goods Issue via Pick List 18](#_Toc232853172)

[4.2.3.2 Manual Goods Issue (Instead of Picking List) 20](#_Toc232853173)

[4.2.4 Monitor Order Progress 21](#_Toc232853174)

[4.2.5 Confirm Production incl.Component Backflush 21](#_Toc232853175)

[4.2.6 Post Goods Receipt for Process Order 23](#_Toc232853176)

[4.2.7 Review Process Order Confirmation 24](#_Toc232853177)

[4.2.8 Review Scrap Report (Optional) 25](#_Toc232853178)

[4.3 Review Manufacturing Object Pages (Optional) 26](#_Toc232853179)

[5 Appendix 27](#_Toc232853180)

[5.1 Succeeding Processes 27](#_Toc232853181)

## Purpose

Overview

This scope item enables the process of manufacturing of co- and by-products along with the main product.

The process starts with the creation of a demand forecast for semifinished goods represented by Planned Independent Requirements (PIRs). Based on PIRs, Material Requirements Planning (MRP) creates a production plan for semifinished components and raw materials. Production planners can analyze and change the planned-order-based production plan manually.

Raw material demand leads to purchase requisitions that trigger alternative procurement scenarios referenced in this scope item.

The production process itself is entirely covered via conversion of planned into process orders, order release, direct material issue or backflush, confirmation of operations and goods receipt posting for main, co-, and by-products. Order-based target and actual costs are created, ensuring fully integrated material and value streams.

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

| Master | Value | Description | Comments |
| --- | --- | --- | --- |
| Material | SG2200 | SEMI2200, MTS-PI, PD, with Co- & By-Product | Main product |
| Material | RM1420 | RM1420, PD, Solvent | Raw Material |
| Material | RM1430 | RM1430, PD, Catalyst | Raw Material |
| Material | SG7100 | SEMI7100, PD, By-Product | By-Product |
| Material | SG9100 | SEMI9100, PD, Co-Product | Co-Product |
| Material | SG8100 | SEMI8100, PD, Co-Product, FIX Price | Co-Product |
| Plant | 3310 | Plant 1 AE |  |
| Storage Location | 331B | Std. storage 2 | Std. storage for production |
| Storage Location | 331C | Raw mat. stoloc. | Raw material storage location |
| Resource | RES-1010 | Polymerisation |  |
| Resource | RES-1020 | Extruder |  |
| Resource | RES-1030 | Drying |  |

Bill of Materials Structure

This overview shows the bill of materials structure and the usage of each component.

BOM Header

| Material | Usage | Base quantity | Unit | Material description |
| --- | --- | --- | --- | --- |
| SG2200 | 1 | 100 | KG | SEMI2200, MTS-PI, PD, with Co- & By-Product |

BOM Item

| Item | Item Category | Component | Quantity | Unit | Material Description |
| --- | --- | --- | --- | --- | --- |
| 0010 | L | RM1420 | 500 | L | RM1420, PD, Solvent |
| 0020 | L | RM1430 | 120 | KG | RM1430, PD, Catalyst |
| 0030 | L | SG7100 | -10 | KG | SEMI7100, PD, By-Product |
| 0040 | L | SG9100 | -400 | L | SEMI9100, PD, Co-Product |
| 0050 | L | SG8100 | -50 | L | SEMI8100, PD, Co-Product, FIX Price |

For more information on creating master data objects, see the following [Master Data Scripts (MDS)](https://help.sap.com/docs/s4hana-best-practices/s4cld2608-master-data)

Master Data Script Reference

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
| BEG - Standard Cost Calculation | You have completed the step described in the test scrip BEG. |
| BNZ - Create New Open MM Posting Period - MDS | You have completed the step described in the test script BNZ. Posting Period is up to date. |
| 3F0 - Event-Based Production Cost Posting | If you want to calculate real time WIP, refer to test script 3F0. |

|  |
| --- |
| Note This scope item describes the manufacturing of co- and by- products along with the main product in process manufacturing. The same business process is supported with production order for discrete manufacturing. |

### Preliminary Steps

#### Initial Raw Material Stock

Purpose

In a real business case, the raw materials are usually purchased from external vendors that can be covered by the standard purchasing processing. Here we post initial stock directly to the storage location.

|  |
| --- |
| Note You can either post initial stock directly to the storage location or referring to the process of Procurement of Direct Materials (J45) or Scheduling Agreements in Procurement (BMR). |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | Screen name adapts according to entries. |  |
| 3 | Choose Goods Receipt-Other | Make the following entries and choose Enter.Trans./Event: Goods ReceiptReference Document: OtherMovement Type: 561 | Screen name adapts after entries are made. |  |
| 4 | Specify Material | In the Material tab, make the following entries:Material: RM1420 | Ensure that detail data is expanded. |  |
| 5 | Specify Quantity | In the Quantity tab, make the following entries:Qty in Unit of Entry: 1000 |  |  |
| 6 | Specify Plant and Storage Location | In the Where tab, make the following entries:Plant: 3310Storage location: 331B |  |  |
| 7 | Check Item | Press Enter, and ensure Item OK is selected. |  |  |
| 8 | Add Other Materials | Choose Next Item, then repeat the steps 4 to 7 for the following materials:Material: RM1430 |  |  |
| 9 | Post Goods Movement | Choose Post. | Material document XXX posted.Materials are available in stock. |  |

## Overview Table

This scope item consists of several process steps provided in the table below.

|  |
| --- |
| Note If your system administrator has enabled spaces and pages on the SAP Fiori launchpad, the homepage will only contain the essential apps for performing the typical tasks of a business role.You can find all other (searchable) apps not included on the homepage using the search bar ([2434549](https://me.sap.com/notes/2434549)).If you want to personalize the homepage and include the hidden apps, navigate to your user profile and choose App Finder. |

| Process Step | Business Role | Transaction/App | Expected Results |
| --- | --- | --- | --- |
| [Create Planned Independent Requirements](#unique_9) [page ] 11 | Production Planner | Maintain PIRs (F3445) | Independent Requirements for main product are created. |
| [Material Requirements Planning](#unique_10) [page ] 12 | Production Planner | Schedule MRP Runs (F1339). | Independent Requirements for main product are planned. |
| [Evaluate the Stock / Requirement Situation](#unique_11) [page ] 14 | Production Planner | Monitor Material Coverage - Net / Individual Segments (F2101A) | Stock/Requirements situation for the planned material are analyzed. |
| [Create Process Order](#unique_12) [page ] 15 | Production Planner | Convert Planned Orders - to Process Orders (COR8) | Planned Orders for main product are converted to Process Orders. |
| [Review Process Order](#unique_13) [page ] 17 | Production Supervisor - Process Manufacturing | Display Process Order (COR3) | The Process Order are reviewed. |
| [Goods Issue via Pick List](#unique_14) [page ] 18 | Production Operator - Process Manufacturing | Pick Components for Process Orders (COIK) | Components under Picking List are posted. |
| [Manual Goods Issue (Instead of Picking List)](#unique_15) [page ] 20 | Warehouse Clerk | Post Goods Movement (MIGO) | Goods movements are posted. |
| [Monitor Order Progress](#unique_16) [page ] 21 | Production Supervisor - Process Manufacturing | Monitor Order Progress (CO46) |  |
| [Confirm Production incl.Component Backflush](#unique_17) [page ] 21 | Production Operator - Process Manufacturing | Confirm Process Order Phase (COR6N) | Confirmation of the process order is carried out. |
| [Post Goods Receipt for Process Order](#unique_18) [page ] 23 | Warehouse Clerk | Post Goods Movement (MIGO) | The goods receipt for the process order is posted. |
| [Review Process Order Confirmation](#unique_19) [page ] 24 | Production Supervisor - Process Manufacturing | Display Process Order Confirmation (CORT) |  |
| [Review Scrap Report (Optional)](#unique_20) [page ] 25 | Production Supervisor - Discrete Manufacturing | Material Scrap - Maximum Deviation (F2035) - Maximum Deviation |  |
| [Review Manufacturing Object Pages (Optional)](#unique_21) [page ] 26 | Any role for production listed in chapter Roles | Search function |  |

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

Planned independent requirements (PIR) are used to perform demand management functions. A planned independent requirement contains one planned quantity and one date, or a number of planned independent requirements schedule lines, that is, one planned quantity split over time according to dates.

|  |
| --- |
| Note Instead of creating single requirement, sometimes a requirements plan that includes one or more planned independent requirements can be maintained for mass processing. In this case, the requirements are grouped and maintained under a requirement plan number. |

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Maintain PIRs (F3445) | The Maintain PIRs screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, choose Area of Responsibility.On the My Area of Responsibility screen, check if the below entry is assigned:Plant 1 AE (3310)MRP Controller 001 (001)Choose AOR Status if the status for the above entry is not yet assigned.Choose AOR Status to unassign the rest of other entries. Then choose Back.Please note that you need to maintain this AOR Status correctly when you go through the whole test script. |  |  |
| 4 | Select Material Items | On the Maintain PIRs screen, make the following entries:Plant: 3310Period Indicator: Weekly (W)Version Active: Select all optionsSearch: SG2200. |  |  |
| 5 | Filter Result | Choose Go to execute . | Material item displays. |  |
| 6 | Edit PIRs | Select the material item, and choose Edit on the upper-right part of the screen.On the screen, enter quantities per period, for example:PIR: 100Make sure the version is active.Version Active: Yes |  |  |
| 7 | Save PIRs Draft | Choose Save at bottom right. | The PIRs are saved. |  |

#### Material Requirements Planning

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to tailor available capacities and receipts on time to suit requirement quantities. You can use MRP or consumption-based planning for this purpose. Single-item multilevel requirement planning is carried out for plant 3310.

Prerequisite

The main product (SG2200) is planned at plant level. There is now a requirement for the material (SG2200) in plant 3310.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Schedule MRP Runs (F1339). | The Application Jobs screen displays. |  |
| 3 | Create New Job | Choose Create.On the New Job screen, make the following entries:For 1. Template Selection section:Job Template: Material Requirement Planning (MRP)Job Name: <MRP for SG2200>Choose Step 2.For 2. Scheduling Options section:Start Immediately: XChoose Define Recurrence Pattern.On the Scheduling Information screen, make the following entries:Start Immediately: XRecurrence Pattern: Single RunChoose OK.Choose Step 3.For 3 Parameters section:Plant: 3310Material: SG2200Changed BOM Components: XPlanning Mode: 1Choose Check at the bottom right.Choose Schedule. | A message appears: You can go ahead and schedule the job. |  |
| 4 | Refresh Application Jobs List | To check the job’s status, enter MRP for SG2200 in the search box and choose Go at the top right section of the screen. | The new job is created and is displayed in the Application Jobs table when refreshed. |  |

#### Evaluate the Stock / Requirement Situation

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to monitor the material coverage situation for the material after the requirements planning is carried out.

Prerequisite

Requirements planning has been carried out.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). | The Monitor Material Coverage - Net / Individual Segments screen displays. |  |
| 3 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 4 | Select Material | In the search area, make the following entries and choose Go.Material: SG2200Select the filtered rows and choose Manage Materials. | The Manage Material Coverage screen displays.Note If you can't find the entry, please check Area of Responsibility settings. Select the user within the app (from the top left corner): MRP Settings > Area of Responsibility , and make sure following values are selected:Plant 1 AE (3310)MRP Controller 001(001) |  |
| 5 | Review Stock / Requirements List | Select the corresponding material in the left Materials list. | The detailed Stock / Requirements List for each material displays. |  |
| 6 | Display Planned Order | In the Materials list on the left side, choose the following material for which you want to check the planned order:Material: SG2200On the right screen, choose PldOrd XXXX in MRP Element column. | The Planned Order selected displays on the dialog box. Make a note of the number of this Planned Order.If there is no shortage for those materials, the planned order won't be generated.If you want to display more information about the planned order, choose Document Info from the bottom of this dialog box. |  |

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

This process step shows you how to create process orders as production can start immediately when the order release is executed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Material Coverage - Net / Individual Segments (F2101A). |  |  |
| 3 | Check MRP Settings | Choose the user icon, and select MRP Settings, and then select Area of Responsibility.On the My Area of Responsibility screen, check if only the following entry is assigned:Plant 1 AE 3310MRP Controller 001 (001)Choose AOR status button of this entry if not assigned, choose AOR status button of the corresponding entry to remove any other entry then choose Back. |  |  |
| 4 | Check Default Setting | Choose the user icon, and select App Settings.In the MRP Settings dialog box, check if the toggle button of Manage Material Coverage - New Version (F0251A) is on.Turn it on if the toggle button is off. | If the toggle button is on, continue with following steps to navigate to Manage Material Coverage - New Version (F0251A).If the toggle button is off, you will be navigated to Check Material Coverage - Old Version (F0251).The following steps are described with the toggle button on. |  |
| 5 | Select Material | Make the following entries and choose Go:Shortage Definition: MRP StandardMaterial: SG2200Select the filtered material, and then choose Manage Materials. |  |  |
| 5 | Choose Action Convert | For the planned order you want to convert, select Convert from the dropdown list under column Actions. |  |  |
| 6 | Convert to Process Order | In the dialog box, Convert to Process Order is selected by default. Choose Convert. | Planned orders are converted to process orders.Make a note of the process order numbers. |  |

As an alternative, you can also use some other app to covert the planned order to process order. If you already converted it through above procedure, you do not need to execute below procedure again.

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Convert Planned Orders - to Process Orders (COR8). | The Collective Conversion of Planned Orders: Initial screen displays. |  |
| 3 | Enter Restriction | Make the following entries and choose Execute:Production Plant: 3310Material: SG2200 | The system displays a list of all planned orders, which match the restriction. |  |
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
| 3 | Enter Process Order Number | Make the following entries and choose Enter.Process Order: <XXXX> (From previous steps) | The Display Process Order: Header - General Data screen displays.On this screen, you find the order’s detailed information.Process orders are reviewed and checked within your responsibility area. |  |

#### Goods Issue of Batch-Managed Components

Purpose

The withdrawal of the raw materials is used for the process order. This withdrawal can be done by using the picking list or doing a manual goods issue.

Prerequisites

Ensure that sufficient material is present on stock. You can check the stock levels using the app Monitor Stock / Requirements List available for the Production Planner role.

##### Goods Issue via Pick List

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step explains how to issue all materials moved to the production storage location to the process order using the pick list once the released process order is ready for picking.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Pick Components for Process Orders (COIK). | The Picking List: Initial screen displays. |  |
| 3 | Enter Restriction and Execute | Make the following entries and then choose Execute.Profile: 000002Process Order: <XXXX> (from previous steps)Plant: 3310 | The Order Information System: Detail List of Components screen displays. |  |
| 4 | Picking Raw Materials | Select the relevant reservations and choose Picking. | The Picking list screen displays. On this screen, a list of all the selected reservations displays. |  |
| 5 | Perform Batch Determination | Select the picking lines and choose Batch Determination. | The Batch Determination MM: Select Batches screen displays.If the system shows the message Batch determination was carried out without selection specification, ignore it.During batch determination, if only part of the required quantity is found available, the unconfirmed quantity remains as an open line item within the picking list. Delete the line item from the picking list before saving because this line item can't be posted. |  |
| 6 | Copy Batch Determination Result | Choose Copy. | The Picking list screen displays again. In addition, the batch numbers are now determined. |  |
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

This process step shows you how the system performs a goods issue.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then choose Enter.Trans./Event: Goods IssueReference Document: OrderOrder number: XXXX (from previous steps)Movement Type: 261 | The screen name adapts after entries are made. |  |
| 4 | Check Each Item | For each item shown, select Item OK. | Ensure that detail data is expanded. |  |
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

This process step shows you how to generate a worklist for process orders, components and operations, with user-specific selection and layout settings.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Monitor Order Progress (CO46). | The Order Progress Report: Selection screen displays. |  |
| 3 | Enter Overall Profile | Make the following entries and choose Production/Process Order tab.Overall Profile: SAP000000002 |  |  |
| 4 | Enter Process Order Number | Make the following entries and choose Execute.Production/Process Order: <XXXX> (from previous steps) | The Stock/Requirements List as of XX hrs screen displays.You can review the required lists, such as order header and components lists. |  |

#### Confirm Production incl.Component Backflush

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

The confirmation documents include the processing status of order, operations, phases and individual capacities. It is an instrument to control the order. The time ticket confirmation allows recording either the default times for machine and labour usage, or record actual times for major deviations. Backflushed materials will be posted automatically during respective phase confirmations. You can post scrap quantities as an optional. If no major deviations occurred, only the last phase (milestone) must be confirmed. Using milestone confirmation, all prior phases are confirmed automatically.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Operator - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Confirm Process Order Phase (COR6N). | The Enter Time Ticket for Process Order screen displays. |  |
| 3 | Enter Confirmation Option | Make the following entries and then choose Enter.Order: <XXXX> (from previous steps)Choose Enter or select phase (0060) from search help of Phase field.Confirm.type: Final confirmationClear open reservations: X | If the system shows the message Total quantity confirmed not equal to planned quantity to be confirmed, press Enter to ignore it. |  |
| 4 | Propose Actual Data | Choose Actual Data, make the changes for the following fields:Scrap: <enter the amount you want to Scrap>Yield: <Based on the origin quantities minus Scrap>Reason for Var: <Enter scarp reason if need>, for example, 0001 | The Quantities and Activities will be filed automatically. You can make necessary change. |  |
| 5 | Choose Goods Movements | Choose Goods Movements. | The Enter Confirmation for Production Order: Goods Movement screen displays. RM1430 and SG7100 should be listed here, check the material entries and quantities. |  |
| 6 | Batch Determination for Backflushed Raw Material | In the Goods Movements Overview table, select the RM1430 line, and choose Batch Determination. | The Batch Determination MM: Select Batches screen displays.If the system shows the message Batch determination was carried out without selection specification , ignore it.If only part of the required quantity is found to be available during batch determination, the unconfirmed quantity remains as an open line item within the picking list. You should then delete the line item from the picking list before saving, as this line item cannot be posted. |  |
| 7 | Copy Batch Determination Result | Choose Copy. | The Enter Confirmation for Production Order: Goods Movement screen displays again. In addition, the batch numbers have been determined. |  |
| 8 | Save Confirmation | Choose Back icon to Enter Time Ticket for Process Order screen. Choose Save. | Backflushed component RM1430 is issued with the confirmation posting automatically. GR posting is done for By- Product SG7100.The final confirmation of the last operation is carried out. Costs and activity quantities are recalculated in proportion to the yield quantity. |  |

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Warehouse Clerk. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Post Goods Movement (MIGO). | The Initial screen displays. |  |
| 3 | Enter Process Order | Make the following entries and then choose Enter.Trans./Event: Goods ReceiptReference Document: OrderOrder number: <XXXX> (From previous steps)Movement Type: 101 | Screen name adapts after entries are made. |  |
| 4 | Check Product | Check the products listed in the table. | Three lines appear, including Main Product (SG2200) and Co- Products (SG9100, SG8100). |  |
| 5 | Check Item | Select Item OK for each line. | Ensure that detail data is expanded. |  |
| 6 | Check | Choose Check in the lower right corner. | The batch number is created automatically. |  |
| 7 | Post Goods Movement | Choose Post. | The goods movements for main product and Co- product are posted. |  |

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
| 3 | Enter Process Order | Make the following entries and then choose Enter.Process Order: <XXXX> (from previous steps) | The Display Process Order Confirmation: Operation/Phase Overview screen displays.Confirmations are reviewed and checked within your responsibility area. |  |

#### Review Scrap Report (Optional)

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
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Supervisor - Process Manufacturing. | The SAP Fiori launchpad displays. |  |
| 2 | Access the App | Open Material Scrap - Maximum Deviation (F2035). |  |  |
| 3 | Investigate Scrap | Materials scrap can be displayed by various filters.You could choose the corresponding material in Chart to display the details. |  |  |

### Review Manufacturing Object Pages (Optional)

Test Administration

Customer project: Fill in the project-specific parts.

|  |  |  |  |
| --- | --- | --- | --- |
| Test Case ID | <X.XX> | Testing Date: |  |
| Tester Name: |  | Duration: |  |
| Business Role(s): |  | Responsibility: | <State the Service Provider, Customer or Joint Service Provider and Customer> |

Purpose

This process step shows you how to review the different objects pages available for different roles in the area of Manufacturing.

Procedure

| Test Step # | Test Step Name | Instruction | Expected Result | Pass / Fail / Comment |
| --- | --- | --- | --- | --- |
| 1 | Log On | Log on to the SAP Fiori launchpad as a Production Planner.Note You can use any role in the Role section above. | The SAP Fiori launchpad displays. |  |
| 2 | Start Search | Choose Search in the upper right area of the launchpad. | An input field displays. |  |
| 3 | Search Criteria | Make the following entries and choose Search:BOM Header Material: <Material> (see Master Data, Organizational Data, and Other Data section) | The system displays a list of objects that use the selected material. |  |
| 4 | Display Object | In All field, choose Down arrow.Select an object and choose Search. | The list of objects is limited to the object type selected. If no object is selected, a message displays instead. |  |
| 5 | Tailor the Result Display | Below the search line, choose a symbol (for example, filter, display as table, sort, and so on) to filter the results list. | The results list are filtered according to your selections. |  |
| 6 | Repeat Steps | Repeat steps 1 to 5 for any other role in this test script and any other object offered in the search function. | The list of objects offered for search differs by the role you used to log on. |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview Table lists the Review Scrap Report (Optional) step under role 'Production Supervisor - Discrete Manufacturing', while the procedure logs on as 'Production Supervisor - Process Manufacturing'; the Roles table does not list a Discrete Manufacturing supervisor.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/make-to-stock-process-manufacturing-based-on-process-order-bj8-ae-test]]
- related-to :: [[12-production-and-manufacturing/make-to-stock-with-silo-material-process-manufacturing-3ul-ae-test-scr]]
- related-to :: [[12-production-and-manufacturing/test-script-make-to-stock-process-manufacturing-based-on-production-or]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/TestScripts/3L7_S4CLD2608_BPD_EN_AE.docx` — full document · extracted with `mammoth` · 44,228 chars in the whole document
